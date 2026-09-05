#!/usr/bin/env python3
"""
refsweep.py - sweep an anchor's own one-hop neighbourhood for prior art.

WHY THIS EXISTS
---------------
Three times on 2026-09-05 this project claimed novelty for something that was
sitting in the reference list or the citer set of a paper it had already read:

  * C53 stated an adsorption-enthalpy threshold "against a lower laboratory
    value" as its own framing.  **Hu et al. 2016** (10.1089/ast.2015.1410) says
    it in its abstract - "The adsorption energy needs to be 36 kJ/mol ...
    higher than existing laboratory measurements" - and Hu 2016 is entry
    e_1_3_3_52_1 of the **deposited reference list of Yung et al. 2018**, which
    C49 had graded `full-text-read`.  The prior art was one hop from an open
    paper and C53 cited it nowhere.
  * C43's T-value mechanism is Skidmore 1982 / Schertz 1983 / Johnson 1987 /
    Alexander 1988.
  * C35's T-vs-formation ratio is Verheijen et al. 2009, which sits in
    Montgomery 2007's **citer** set - and Montgomery 2007 is C35's own
    load-bearing source.

Searching the open literature is the hard problem.  Reading the bibliography of
the paper you already opened is not, and this script makes that step mechanical
rather than a matter of the reader's attention.  See
`vault/method/failure-taxonomy.md` mode **R5** and `vault/method/recipes.md`
"How to add a computed note" step 4.

WHAT IT DOES
------------
Given 1-5 anchor DOIs and a list of claim phrases:

  1. **Backwards** - fetches each anchor's *deposited reference list*
     (Crossref `works/<doi>`, `message.reference`; OpenCitations
     `/references/<doi>` as fallback when Crossref deposits none).
  2. **Forwards** - fetches each anchor's *citers* through the existing
     `providers/` adapters (OpenCitations by default; `--providers` to widen).
  3. **Resolves** every DOI found to title + year + abstract, in bulk:
     Crossref `works?filter=doi:...` (40 at a time), then Europe PMC
     `resultType=core` (25 at a time) for the abstracts Crossref does not
     deposit, then Semantic Scholar `paper/batch` (100 at a time, best-effort,
     skipped silently on 429 - the abstract is a bonus, not a dependency).
  4. **Matches** each phrase, case-insensitively, against title + abstract, and
     prints every work with at least one hit, ranked by match count.

Stdlib only.  Every HTTP response is cached under `_scripts/.oc-cache/`, so a
re-run costs nothing and a second sweep with different phrases is free.

WHAT IT IS NOT
--------------
Not a literature search.  It reads exactly two hops - what the anchors cite and
what cites them - so a work that neither cites nor is cited by any anchor is
invisible to it.  A clean sweep is **not** evidence of novelty; a dirty sweep is
proof of its absence.  Report it as the latter only.

**Units are the trap.**  Matching is a plain case-insensitive substring, and a
unit is written differently by every source: the selftest's `"kJ/mol"` does
**not** match Hu 2016, because Europe PMC renders that abstract's figure as
`36 kJ mol(-1)`.  Hu 2016 comes back anyway, on `"adsorption energy"` and
`"laboratory measurements"` — which is the reason to pass several phrases and
to include the *words* of the claim rather than only its units.  Pass unit
variants explicitly (`"kJ/mol" "kJ mol" "kJ mol-1"`) when the unit is the
phrase that matters.

Absence of an abstract is not absence of a match: Crossref deposits abstracts
for a minority of works, and a DOI resolved to title only is matched on the
title alone.  The per-anchor summary prints how many works were resolved with
an abstract, so a sweep over a corpus that is 90% title-only is visible as such
rather than being read as ten clean zeros (failure-taxonomy I2).

USAGE
-----
    python refsweep.py --anchors 10.1089/ast.2018.1917 \
        --phrases "adsorption energy" "kJ/mol" "laboratory measurements"

    python refsweep.py --anchors DOI1,DOI2 --phrases "..." --no-citers
    python refsweep.py --selftest

`--selftest` runs the C53 case: the phrases above against Yung et al. 2018, and
asserts that Hu et al. 2016 (10.1089/ast.2015.1410) comes back.  That is the
work whose absence from C53 the adversarial review graded REDISCOVERED.
"""

import argparse
import json
import os
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import providers                                              # noqa: E402
from providers import (DEFAULT_CACHE, ProviderError, cached_json,  # noqa: E402
                       norm_doi)

MAILTO = os.environ.get("MAILTO", "deciduusleaf@gmail.com")

CROSSREF_WORK = "https://api.crossref.org/works/%s?mailto=" + MAILTO
CROSSREF_BULK = ("https://api.crossref.org/works?filter=%s&rows=100"
                 "&select=DOI,title,issued,abstract,container-title&mailto="
                 + MAILTO)
EPMC = ("https://www.ebi.ac.uk/europepmc/webservices/rest/search"
        "?query=%s&format=json&resultType=core&pageSize=25")
S2_BATCH = "https://api.semanticscholar.org/graph/v1/paper/batch"

CROSSREF_CHUNK = 40      # DOIs per bulk Crossref filter query
EPMC_CHUNK = 25          # DOIs per Europe PMC boolean query
S2_CHUNK = 100           # DOIs per Semantic Scholar batch POST

SELFTEST_ANCHOR = "10.1089/ast.2018.1917"          # Yung et al. 2018
SELFTEST_PHRASES = ["adsorption energy", "kJ/mol", "laboratory measurements"]
SELFTEST_EXPECT = "10.1089/ast.2015.1410"          # Hu et al. 2016


# --- helpers ---------------------------------------------------------------

def chunks(seq, n):
    seq = list(seq)
    for i in range(0, len(seq), n):
        yield seq[i:i + n]


def strip_tags(s):
    """Crossref deposits JATS-wrapped abstracts; flatten to plain text."""
    if not s:
        return ""
    out, depth = [], 0
    for ch in s:
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth = max(0, depth - 1)
        elif depth == 0:
            out.append(ch)
    return " ".join("".join(out).split())


def first(v):
    if isinstance(v, list):
        return v[0] if v else ""
    return v or ""


def year_of(item):
    for f in ("issued", "published-print", "published-online", "created"):
        d = item.get(f) or {}
        parts = d.get("date-parts") or []
        if parts and parts[0] and parts[0][0]:
            return int(parts[0][0])
    return None


# --- step 1: the anchor's own reference list --------------------------------

def anchor_references(doi, cache_dir):
    """(refs, note) - refs is {doi: seed_title}; seed_title may be "".

    Crossref's deposited `message.reference` is the primary source: it is what
    the publisher deposited, entry by entry, and many entries carry a DOI with
    no title (Yung 2018 deposits 155 references, most DOI-only).  Entries with
    no DOI at all are kept only if they carry a title, matched on that title,
    and flagged `no-DOI` in the output - dropping them silently would be
    failure-taxonomy I1 with the sign reversed.
    """
    url = CROSSREF_WORK % urllib.parse.quote(doi)
    refs, untitled_nodoi = {}, 0
    try:
        msg = cached_json(url, cache_dir, "cr_work_" + doi, pause=0.2)["message"]
    except ProviderError as e:
        print("  [crossref] refs for %s FAILED: %s" % (doi, e), file=sys.stderr)
        msg = {}
    for r in (msg.get("reference") or []):
        d = norm_doi(r.get("DOI"))
        t = (r.get("article-title") or r.get("volume-title")
             or r.get("unstructured") or "").strip()
        if d:
            refs[d] = t
        elif t:
            refs["nodoi:" + t.lower()[:120]] = t
        else:
            untitled_nodoi += 1
    note = "crossref deposit: %d entries, %d usable, %d unusable (no DOI, no title)" % (
        len(msg.get("reference") or []), len(refs), untitled_nodoi)

    if not refs:
        # Crossref deposited no reference list at all.  Not a zero - a coverage
        # hole (failure-taxonomy I3).  Try OpenCitations before believing it.
        try:
            oc = providers.opencitations.references(doi, cache_dir=cache_dir)
            refs = {d: "" for d in oc}
            note = "crossref deposited none; opencitations /references: %d" % len(refs)
        except ProviderError as e:
            note += "; opencitations fallback failed: %s" % e
    print("  [refs] %s -> %s" % (doi, note), file=sys.stderr)
    return refs, note


# --- step 2: the anchor's citers -------------------------------------------

def anchor_citers(doi, mods, cache_dir, cap):
    """Union of citer DOIs across the named provider modules."""
    out, notes = set(), []
    for m in mods:
        ok, why = m.available()
        if not ok:
            notes.append("%s unusable (%s)" % (m.NAME, why))
            continue
        try:
            got = m.citers(doi, cache_dir=cache_dir)
        except ProviderError as e:
            # A failed fetch is never a zero.  Say so and keep the other legs.
            notes.append("%s err: %s" % (m.NAME, str(e)[:120]))
            continue
        notes.append("%s %d" % (m.NAME, len(got)))
        out |= got
    truncated = False
    if cap and len(out) > cap:
        out = set(sorted(out)[:cap])
        truncated = True
        notes.append("TRUNCATED to --max-citers=%d (raise it or the sweep is "
                     "partial)" % cap)
    print("  [citers] %s -> %s" % (doi, "; ".join(notes) or "none"),
          file=sys.stderr)
    return out, "; ".join(notes), truncated


# --- step 3: bulk metadata resolution --------------------------------------

def resolve_crossref(dois, cache_dir):
    meta = {}
    for batch in chunks(sorted(dois), CROSSREF_CHUNK):
        filt = ",".join("doi:" + d for d in batch)
        url = CROSSREF_BULK % urllib.parse.quote(filt, safe=":,")
        key = "cr_bulk_" + str(abs(hash(filt)) % (10 ** 12))
        try:
            items = cached_json(url, cache_dir, key, pause=0.2)["message"]["items"]
        except (ProviderError, KeyError) as e:
            print("  [crossref] bulk batch failed: %s" % str(e)[:120],
                  file=sys.stderr)
            continue
        for it in items:
            d = norm_doi(it.get("DOI"))
            if not d:
                continue
            meta[d] = {"doi": d,
                       "title": first(it.get("title")),
                       "year": year_of(it),
                       "venue": first(it.get("container-title")),
                       "abstract": strip_tags(it.get("abstract")),
                       "src": "crossref"}
    return meta


def resolve_epmc(dois, cache_dir, meta):
    """Fill missing abstracts from Europe PMC (biomedicine-weighted, but it
    carries Astrobiology, Icarus and PSS)."""
    want = [d for d in dois if not (meta.get(d) or {}).get("abstract")]
    for batch in chunks(sorted(want), EPMC_CHUNK):
        q = " OR ".join('DOI:"%s"' % d for d in batch)
        url = EPMC % urllib.parse.quote(q)
        key = "epmc_bulk_" + str(abs(hash(q)) % (10 ** 12))
        try:
            res = cached_json(url, cache_dir, key,
                              pause=0.3)["resultList"]["result"]
        except (ProviderError, KeyError) as e:
            print("  [europepmc] batch failed: %s" % str(e)[:120],
                  file=sys.stderr)
            continue
        for r in res:
            d = norm_doi(r.get("doi"))
            if not d:
                continue
            m = meta.setdefault(d, {"doi": d, "title": "", "year": None,
                                    "venue": "", "abstract": "", "src": "epmc"})
            if not m.get("abstract"):
                m["abstract"] = strip_tags(r.get("abstractText"))
                if m["abstract"]:
                    m["src"] = m["src"] + "+epmc"
            if not m.get("title"):
                m["title"] = r.get("title") or ""
            if not m.get("year") and r.get("pubYear"):
                m["year"] = int(r["pubYear"])
    return meta


def resolve_s2(dois, cache_dir, meta):
    """Best-effort third abstract source.  Semantic Scholar's shared pool 429s
    unauthenticated (failure-taxonomy I3); a failure here is logged and the
    sweep continues on what Crossref and Europe PMC gave."""
    import urllib.request
    want = [d for d in dois if not (meta.get(d) or {}).get("abstract")]
    for batch in chunks(sorted(want), S2_CHUNK):
        body = json.dumps({"ids": ["DOI:" + d for d in batch]}).encode()
        url = S2_BATCH + "?fields=title,year,abstract,externalIds"
        req = urllib.request.Request(
            url, data=body,
            headers={"Content-Type": "application/json",
                     "User-Agent": providers.UA})
        key = os.path.join(cache_dir or "", "s2_batch_%d.json"
                           % (abs(hash(tuple(batch))) % (10 ** 12)))
        try:
            if cache_dir and os.path.exists(key):
                with open(key, "rb") as f:
                    rows = json.loads(f.read().decode("utf-8"))
            else:
                with urllib.request.urlopen(req, timeout=120) as r:
                    raw = r.read()
                rows = json.loads(raw.decode("utf-8"))
                if cache_dir:
                    os.makedirs(cache_dir, exist_ok=True)
                    with open(key, "wb") as f:
                        f.write(raw)
        except Exception as e:                                # noqa: BLE001
            print("  [semanticscholar] batch skipped: %s" % str(e)[:120],
                  file=sys.stderr)
            return meta
        for row in rows or []:
            if not row:
                continue
            d = norm_doi(((row.get("externalIds") or {}).get("DOI")))
            if not d:
                continue
            m = meta.setdefault(d, {"doi": d, "title": "", "year": None,
                                    "venue": "", "abstract": "", "src": "s2"})
            if not m.get("abstract") and row.get("abstract"):
                m["abstract"] = row["abstract"]
                m["src"] = m["src"] + "+s2"
            if not m.get("title"):
                m["title"] = row.get("title") or ""
            if not m.get("year"):
                m["year"] = row.get("year")
    return meta


# --- step 4: match ----------------------------------------------------------

def match(meta, phrases):
    hay = ((meta.get("title") or "") + " \n " +
           (meta.get("abstract") or "")).lower()
    return [p for p in phrases if p.lower() in hay]


def sweep(anchors, phrases, provider_names=("opencitations",), do_citers=True,
          max_citers=400, cache_dir=DEFAULT_CACHE, s2=True):
    """Returns (rows, report).  `rows` is sorted strongest match first."""
    mods = providers.resolve(list(provider_names)) if do_citers else []
    origin, seeds, report = {}, {}, []

    for a in anchors:
        a = norm_doi(a) or a
        refs, rnote = anchor_references(a, cache_dir)
        for d, t in refs.items():
            origin.setdefault(d, []).append((a, "reference"))
            if t and not seeds.get(d):
                seeds[d] = t
        cnote, trunc = "", False
        if do_citers:
            cits, cnote, trunc = anchor_citers(a, mods, cache_dir, max_citers)
            for d in cits:
                origin.setdefault(d, []).append((a, "citer"))
        report.append({"anchor": a, "refs": rnote, "citers": cnote,
                       "citers_truncated": trunc})

    real = sorted(d for d in origin if not d.startswith("nodoi:"))
    meta = resolve_crossref(real, cache_dir)
    meta = resolve_epmc(real, cache_dir, meta)
    if s2:
        meta = resolve_s2(real, cache_dir, meta)

    # DOI-less reference entries: matched on their deposited title alone.
    for d in origin:
        if d.startswith("nodoi:"):
            meta[d] = {"doi": "(no DOI deposited)", "title": seeds.get(d, ""),
                       "year": None, "venue": "", "abstract": "",
                       "src": "crossref-reference-string"}
    for d, m in meta.items():
        if not m.get("title") and seeds.get(d):
            m["title"] = seeds[d]

    rows = []
    for d in origin:
        m = meta.get(d)
        if not m:
            continue
        hits = match(m, phrases)
        if hits:
            rows.append({"key": d, "meta": m, "hits": hits,
                         "origin": origin[d]})
    rows.sort(key=lambda r: (-len(r["hits"]),
                             -(r["meta"].get("year") or 0),
                             r["key"]))
    stats = {"candidates": len(origin),
             "resolved": sum(1 for d in origin if meta.get(d, {}).get("title")),
             "with_abstract": sum(1 for d in origin
                                  if meta.get(d, {}).get("abstract")),
             "matched": len(rows)}
    return rows, {"anchors": report, "stats": stats}


def render(rows, report, phrases, top=None):
    out = []
    s = report["stats"]
    out.append("PRIOR-ART SWEEP")
    out.append("phrases: " + " | ".join(phrases))
    for r in report["anchors"]:
        out.append("anchor %s" % r["anchor"])
        out.append("    references: %s" % r["refs"])
        if r["citers"]:
            out.append("    citers:     %s" % r["citers"])
    out.append("%d works in the two-hop neighbourhood; %d resolved to a title; "
               "%d carry an abstract; %d match."
               % (s["candidates"], s["resolved"], s["with_abstract"],
                  s["matched"]))
    if s["candidates"] and s["with_abstract"] < 0.25 * s["candidates"]:
        out.append("WARNING: under a quarter of the corpus has an abstract. "
                   "Most rows were matched on title only; a clean sweep here "
                   "is weak evidence of anything.")
    out.append("")
    shown = rows[:top] if top else rows
    for i, r in enumerate(shown, 1):
        m = r["meta"]
        org = "; ".join("%s (%s)" % (a, k) for a, k in r["origin"])
        out.append("%2d. [%d hit%s] %s" % (i, len(r["hits"]),
                                           "" if len(r["hits"]) == 1 else "s",
                                           m.get("title") or "(no title)"))
        out.append("    %s  %s  %s" % (m.get("doi"),
                                       m.get("year") or "n.d.",
                                       m.get("venue") or ""))
        out.append("    from: %s" % org)
        out.append("    matched: %s" % ", ".join(r["hits"]))
        out.append("    verdict: ____ (one line: prior art / adjacent / "
                   "irrelevant, and why)")
        out.append("")
    if top and len(rows) > top:
        out.append("(%d further matches below the top %d)"
                   % (len(rows) - top, top))
    return "\n".join(out)


def selftest():
    """The C53 case. Hu et al. 2016 must come back from Yung et al. 2018's own
    deposited reference list."""
    print("SELFTEST: %s, phrases %s" % (SELFTEST_ANCHOR, SELFTEST_PHRASES),
          file=sys.stderr)
    rows, report = sweep([SELFTEST_ANCHOR], SELFTEST_PHRASES, do_citers=False)
    print(render(rows, report, SELFTEST_PHRASES, top=10))
    keys = {r["key"] for r in rows}
    assert SELFTEST_EXPECT in keys, (
        "SELFTEST FAILED: %s (Hu et al. 2016) not returned by a sweep of %s. "
        "This is the exact case C53 missed; if the sweep cannot find it the "
        "guard is not standing." % (SELFTEST_EXPECT, SELFTEST_ANCHOR))
    hu = [r for r in rows if r["key"] == SELFTEST_EXPECT][0]
    assert hu["origin"][0][1] == "reference", \
        "SELFTEST FAILED: Hu 2016 was expected via the reference leg."
    assert len(hu["hits"]) >= 2, \
        "SELFTEST FAILED: Hu 2016 matched only %s" % hu["hits"]
    rank = [r["key"] for r in rows].index(SELFTEST_EXPECT) + 1
    print("SELFTEST PASS: %s returned at rank %d of %d matches, via the "
          "reference leg, on %d phrases (%s)."
          % (SELFTEST_EXPECT, rank, len(rows), len(hu["hits"]),
             ", ".join(hu["hits"])), file=sys.stderr)
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Sweep an anchor's references and citers for prior art.")
    ap.add_argument("--anchors", default="",
                    help="1-5 anchor DOIs, comma-separated")
    ap.add_argument("--phrases", nargs="*", default=[],
                    help="claim keywords/phrases to match, case-insensitive")
    ap.add_argument("--providers", default="opencitations",
                    help="citer providers (see intersect.py --list-providers)")
    ap.add_argument("--no-citers", action="store_true",
                    help="backwards leg only (references)")
    ap.add_argument("--no-s2", action="store_true",
                    help="skip the Semantic Scholar abstract leg")
    ap.add_argument("--max-citers", type=int, default=400,
                    help="cap citers resolved per anchor (0 = no cap)")
    ap.add_argument("--top", type=int, default=10,
                    help="how many matches to print (0 = all)")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)

    if a.selftest:
        return selftest()

    anchors = [x.strip() for x in a.anchors.split(",") if x.strip()]
    if not anchors or not a.phrases:
        ap.error("--anchors and --phrases are both required (or --selftest)")
    if len(anchors) > 5:
        ap.error("1-5 anchors; %d given. More than five is a literature "
                 "search, not a sweep." % len(anchors))

    rows, report = sweep(anchors, a.phrases,
                         provider_names=a.providers.split(","),
                         do_citers=not a.no_citers,
                         max_citers=a.max_citers,
                         s2=not a.no_s2)
    if a.json:
        print(json.dumps({"rows": rows, "report": report}, indent=1))
    else:
        print(render(rows, report, a.phrases, top=a.top or None))
    return 0


if __name__ == "__main__":
    sys.exit(main())
