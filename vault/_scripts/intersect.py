#!/usr/bin/env python3
"""
intersect.py - citer-set intersection across several providers (stdlib only).

WHY THIS SCRIPT EXISTS
----------------------
The old citation-intersection recipe pulled the citers of anchor A and then fetched
each citer's *reference list* to see whether it also cited anchor B.  That second
step is coverage-limited: only some publishers deposit reference lists, so G25 ran
at 28.4% coverage.

A **citer-set intersection** needs no reference lists at all.  Pull the citer DOI set
of anchor A and the citer DOI set of anchor B from the same provider and intersect
them.  Coverage is then 100% of what the provider indexes, and the only caveat is the
provider's own DOI-to-DOI coverage.

WHY MORE THAN ONE PROVIDER
--------------------------
Each provider has a hard failure that stops a round: OpenCitations 500s above
~10,000 citers, OpenAlex exhausts a **daily** budget when more than about four
agents run in parallel, Semantic Scholar 429s out of a shared anonymous pool.
No single provider's limit should block a round, and -- more importantly --
**one provider is one opinion**.  OpenAlex and OpenCitations counts differ by
10-25% on the same anchor, so an intersection quoted from one provider carries
an unstated error bar.  `--all` prints every provider's row and a consensus
line giving the min/max intersection observed.

    A single-provider intersection is a measurement.
    A consensus range across independent providers is a finding.

USAGE
-----
    python intersect.py <doiA> <doiB> [<doiB2> ...]

  - The first DOI is anchor A.  All remaining DOIs are pooled as anchor B
    (useful when a work has several DOIs, e.g. Shannon 1948 parts I and II).
  - Prints N_A, N_B, |A n B| and every intersecting DOI, one per line.

  Optional flags:
    --providers=a,b   run only these providers (default: opencitations)
    --all             run every currently-available provider and print a
                      per-provider table plus a consensus min/max line
    --list-providers  print the provider table (auth, rate limit, bias) and exit
    --cache DIR       cache raw JSON responses here (default: ./.oc-cache)
    --enrich          after intersecting, fetch title/year/journal for each hit
                      from Crossref so the hits can be inspected by hand.
                      Inspection is mandatory: a count is not a finding until
                      every hit has been read.
    --json FILE       also write the full result as JSON.
    --selftest        fetch one small known DOI pair and assert no blank key
                      survives.

Known provider names: opencitations, openalex, semanticscholar, europepmc,
lens (needs LENS_TOKEN), scopus (documented stub).

BLANK-KEY TRAP
--------------
OpenCitations /citations/ returns some records with an **empty `citing` field**.
Building the set without filtering adds a phantom "" element, which inflates
N_A, N_B and -- because the phantom is in every set -- **every intersection by
exactly 1**.  Every adapter drops blank/DOI-less keys before building sets and
reports how many it dropped.  Any count taken from an older, unfiltered run may
read one high.

A FAILED FETCH IS NOT A ZERO
----------------------------
Every adapter raises rather than returning an empty set when the provider
cannot see the anchor (S2 404s Charnov 1976; Europe PMC does not index
engineering monographs).  `--all` prints those rows as `err` and excludes them
from the consensus range.  **Never copy an `err` row into a note as a zero.**

Set the polite-pool address with the MAILTO env var (default below).
"""

import json
import os
import sys
import time
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import providers  # noqa: E402
from providers import fetch  # noqa: E402

MAILTO = os.environ.get("MAILTO", "deciduusleaf@gmail.com")
OC = providers.opencitations.BASE
UA = providers.UA


# --- backwards-compatible thin wrappers over the OpenCitations adapter -------

def citers(doi, cache_dir=None, stats=None):
    """Set of DOIs (lowercased) of works citing `doi`, per OpenCitations."""
    return providers.opencitations.citers(doi, cache_dir, stats)


def references(doi, cache_dir=None, stats=None):
    """Set of DOIs `doi` cites, per OpenCitations."""
    return providers.opencitations.references(doi, cache_dir, stats)


SELFTEST_A = "10.1038/nature08227"          # Scheffer et al. 2009
SELFTEST_B = "10.1016/j.ejor.2010.11.018"   # Si et al. 2011


def selftest(cache_dir=None):
    """Fetch one small known DOI pair and assert no blank key survives.

    Asserts (a) no member of either citer set is empty or whitespace and (b) the
    intersection contains no empty key, then reports what the count would have
    been unfiltered, so the phantom is visible rather than merely absent.
    """
    stats = {}
    A = citers(SELFTEST_A, cache_dir, stats)
    B = citers(SELFTEST_B, cache_dir, stats)
    for name, S in (("A", A), ("B", B)):
        bad = [x for x in S if not x or not x.strip()]
        assert not bad, "blank key survived in set %s: %r" % (name, bad)
    inter = A & B
    assert not any((not x or not x.strip()) for x in inter), "blank key in intersection"
    ka = ("opencitations", SELFTEST_A)
    kb = ("opencitations", SELFTEST_B)
    print("selftest OK: A=%s |A|=%d (%d blanks dropped); B=%s |B|=%d (%d blanks dropped); "
          "|A n B|=%d, no blank keys survive"
          % (SELFTEST_A, len(A), stats[ka]["blank_dropped"],
             SELFTEST_B, len(B), stats[kb]["blank_dropped"],
             len(inter)))
    if stats[ka]["blank_dropped"] or stats[kb]["blank_dropped"]:
        print("  (unfiltered, the phantom \"\" would have joined both sets and "
              "reported |A n B| = %d)" % (len(inter) + 1))
    # second assertion: the provider registry is wired and every module
    # satisfies the common interface.
    for m in providers.ALL:
        assert isinstance(m.NAME, str) and m.NAME in providers.BY_NAME
        assert callable(m.citers) and callable(m.available)
        assert isinstance(m.ENDPOINT, str) and isinstance(m.BIAS, str)
    print("provider interface OK: %s" % ", ".join(m.NAME for m in providers.ALL))
    return 0


def list_providers():
    print("%-16s %-9s %s" % ("provider", "usable", "auth / note"))
    print("-" * 96)
    for m in providers.ALL:
        ok, why = m.available()
        print("%-16s %-9s %s" % (m.NAME, "yes" if ok else "NO", why))
        print("%-16s %s" % ("", "endpoint: " + m.ENDPOINT))
        print("%-16s %s" % ("", "rate:     " + m.RATE))
        print("%-16s %s" % ("", "bias:     " + m.BIAS))
        print()
    return 0


def crossref_meta(doi):
    url = "https://api.crossref.org/works/%s?mailto=%s" % (
        urllib.parse.quote(doi), MAILTO)
    try:
        m = json.loads(fetch(url, tries=3, timeout=90).decode("utf-8"))["message"]
    except Exception:  # noqa: BLE001
        return {"doi": doi, "title": "<crossref lookup failed>"}
    return {
        "doi": doi,
        "title": (m.get("title") or ["<no title>"])[0],
        "year": (m.get("issued", {}).get("date-parts") or [[None]])[0][0],
        "journal": (m.get("container-title") or [""])[0],
        "type": m.get("type", ""),
        "abstract": m.get("abstract", ""),
    }


def run_provider(mod, a_doi, b_dois, cache):
    """One provider's whole run.  Returns a row dict; never raises."""
    stats = {}
    row = {"provider": mod.NAME, "endpoint": mod.ENDPOINT,
           "keyspace": getattr(mod, "KEYSPACE", "doi"),
           "n_a": None, "n_b": None, "inter": None, "blanks": None,
           "error": None, "hits": []}
    try:
        A = mod.citers(a_doi, cache, stats)
        B = set()
        for d in b_dois:
            B |= mod.citers(d, cache, stats)
        hits = sorted(A & B)
        row.update(n_a=len(A), n_b=len(B), inter=len(hits), hits=hits,
                   blanks=sum(v["blank_dropped"] for v in stats.values()))
    except Exception as e:  # noqa: BLE001 - one provider must not kill the run
        row["error"] = "%s: %s" % (type(e).__name__, e)
    return row


def print_table(rows, a_doi, b_dois):
    print()
    print("anchor A: %s" % a_doi)
    print("anchor B: %s" % " + ".join(b_dois))
    print()
    print("%-16s %8s %8s %6s %8s  %s"
          % ("provider", "N_A", "N_B", "AnB", "blanks", "status"))
    print("-" * 78)
    for r in rows:
        if r["error"]:
            print("%-16s %8s %8s %6s %8s  %s"
                  % (r["provider"], "-", "-", "err", "-", r["error"][:120]))
        else:
            print("%-16s %8d %8d %6d %8d  ok"
                  % (r["provider"], r["n_a"], r["n_b"], r["inter"], r["blanks"]))
    good = [r for r in rows if not r["error"]]
    print()
    if not good:
        print("consensus: NONE -- every provider errored. This is a broken run, "
              "not a zero intersection.")
        return
    lo = min(r["inter"] for r in good)
    hi = max(r["inter"] for r in good)
    print("consensus over %d provider(s) [%s]: |A n B| in [%d, %d]%s"
          % (len(good), ", ".join(r["provider"] for r in good), lo, hi,
             "  -- providers AGREE" if lo == hi else "  -- providers DISAGREE"))
    na = [r["n_a"] for r in good]
    nb = [r["n_b"] for r in good]
    if len(good) > 1 and max(na) and max(nb):
        print("  N_A spread %d-%d (%.0f%%)   N_B spread %d-%d (%.0f%%)"
              % (min(na), max(na), 100.0 * (max(na) - min(na)) / max(na),
                 min(nb), max(nb), 100.0 * (max(nb) - min(nb)) / max(nb)))
    if len(good) > 1 and lo != hi:
        print("  QUOTE THE RANGE, not one number. Providers disagree on N by "
              "10-25% routinely; an intersection quoted from one provider "
              "carries an unstated error bar.")

    # Hits are only comparable inside one keyspace.  Europe PMC keys are PMIDs,
    # not DOIs (see providers/europepmc.py), so a union across keyspaces would
    # be arithmetic on incommensurable ids.
    spaces = {}
    for r in good:
        spaces.setdefault(r["keyspace"], []).append(r)
    for ks, group in sorted(spaces.items()):
        union, common = set(), None
        for r in group:
            union |= set(r["hits"])
            common = set(r["hits"]) if common is None else common & set(r["hits"])
        if not union:
            continue
        print()
        print("hits in keyspace %r across [%s] -- union %d, in every one %d "
              "(* = found by all):"
              % (ks, ", ".join(r["provider"] for r in group),
                 len(union), len(common or ())))
        labels = {}
        for r in group:
            mod = providers.BY_NAME[r["provider"]]
            if hasattr(mod, "resolve_hits"):
                try:
                    labels.update(mod.resolve_hits(union))
                except Exception:  # noqa: BLE001
                    pass
        for d in sorted(union):
            mark = "*" if common and d in common else " "
            lab = labels.get(d)
            print("  %s %s%s" % (mark, d, "  -> " + lab if lab else ""))


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    flags = [a for a in argv if a.startswith("--")]
    cache = "./.oc-cache"
    for f in flags:
        if f.startswith("--cache="):
            cache = f.split("=", 1)[1]
    if "--list-providers" in flags:
        return list_providers()
    if "--selftest" in flags:
        return selftest(cache if any(f.startswith("--cache=") for f in flags)
                        else None)
    if len(args) < 2:
        print(__doc__)
        return 2
    a_doi, b_dois = args[0], args[1:]

    mods = [providers.opencitations]
    for f in flags:
        if f.startswith("--providers="):
            mods = providers.resolve(f.split("=", 1)[1].split(","))
    if "--all" in flags:
        mods = providers.usable()
        skipped = [(m.NAME, m.available()[1]) for m in providers.ALL
                   if m not in mods]
        for n, why in skipped:
            print("skipping %s: %s" % (n, why), file=sys.stderr)

    rows = [run_provider(m, a_doi, b_dois, cache) for m in mods]

    if len(rows) > 1 or "--all" in flags:
        print_table(rows, a_doi, b_dois)
        primary = next((r for r in rows if not r["error"]), rows[0])
    else:
        r = primary = rows[0]
        if r["error"]:
            print("provider %s FAILED: %s" % (r["provider"], r["error"]))
            print("This is a failed fetch, NOT a zero intersection. "
                  "Try --all or --providers=openalex.")
            return 1
        print("blank/DOI-less records dropped: %d" % r["blanks"])
        if r["blanks"]:
            print("  (without the filter every count below would read one "
                  "higher; see vault/method/citation-sources.md)")
        print("provider: %s  endpoint: %s" % (r["provider"], r["endpoint"]))
        print("anchor A: %s   N_A = %d" % (a_doi, r["n_a"]))
        print("anchor B: %s   N_B = %d" % (" + ".join(b_dois), r["n_b"]))
        print("|A n B| = %d   (%.2f%% of A, %.2f%% of B)" % (
            r["inter"],
            100.0 * r["inter"] / r["n_a"] if r["n_a"] else 0.0,
            100.0 * r["inter"] / r["n_b"] if r["n_b"] else 0.0))

    # null model: expected co-citers if the two citer sets were independent
    # draws from a universe of N works.  Pass NULL_N to get observed/expected.
    n_univ = os.environ.get("NULL_N")
    if n_univ and not primary["error"]:
        exp = primary["n_a"] * primary["n_b"] / float(n_univ)
        print("expected under independence (N=%s, provider %s): %.2f  "
              "observed/expected = %.2f"
              % (n_univ, primary["provider"], exp,
                 primary["inter"] / exp if exp else float("nan")))
    print()
    rows_meta = []
    inter = primary["hits"]
    if "--enrich" in flags:
        for d in inter:
            rows_meta.append(crossref_meta(d))
            time.sleep(0.2)
        for r in rows_meta:
            print("%s | %s | %s | %s" % (
                r["doi"], r.get("year"), r.get("journal", "")[:40], r["title"][:110]))
    elif len(rows) == 1:
        for d in inter:
            print(d)

    for f in flags:
        if f.startswith("--json="):
            with open(f.split("=", 1)[1], "w", encoding="utf-8") as fh:
                json.dump({"anchor_a": a_doi, "anchor_b": b_dois,
                           "fetched": time.strftime("%Y-%m-%d"),
                           "providers": rows,
                           "n_a": primary["n_a"], "n_b": primary["n_b"],
                           "intersection": inter, "meta": rows_meta},
                          fh, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
