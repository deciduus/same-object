#!/usr/bin/env python3
"""
intersect.py - citer-set intersection over OpenCitations (stdlib only).

WHY THIS SCRIPT EXISTS
----------------------
The old citation-intersection recipe pulled the citers of anchor A and then fetched
each citer's *reference list* to see whether it also cited anchor B.  That second
step is coverage-limited: only some publishers deposit reference lists, so G25 ran
at 28.4% coverage.

A **citer-set intersection** needs no reference lists at all.  Pull the citer DOI set
of anchor A and the citer DOI set of anchor B from the same provider and intersect
them.  Coverage is then 100% of what the provider indexes, and the only caveat is the
provider's own DOI-to-DOI coverage (OpenCitations COCI/Meta is DOI-only; anything
without a DOI is invisible to it).

PROVIDER / ENDPOINT
-------------------
    https://api.opencitations.net/index/v1/citations/<doi>   -> works citing <doi>
    https://api.opencitations.net/index/v1/references/<doi>  -> works <doi> cites
(The legacy host opencitations.net/index/coci/api/v1/ 301-redirects here.)
Do not use /citation-count/ without cross-checking; see vault/method/citation-sources.md.

USAGE
-----
    python intersect.py <doiA> <doiB> [<doiB2> ...]

  - The first DOI is anchor A.  All remaining DOIs are pooled as anchor B
    (useful when a work has several DOIs, e.g. Shannon 1948 parts I and II).
  - Prints N_A, N_B, |A n B| and every intersecting DOI, one per line.

  Optional flags:
    --cache DIR   cache raw JSON responses here (default: ./.oc-cache)
    --enrich      after intersecting, fetch title/year/journal for each hit from
                  Crossref (api.crossref.org/works/<doi>?mailto=...) so the hits can
                  be inspected by hand.  Inspection is mandatory: a count is not a
                  finding until every hit has been read.
    --json FILE   also write the full result as JSON.

Set the polite-pool address with the MAILTO env var (default below).
"""

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

MAILTO = os.environ.get("MAILTO", "deciduusleaf@gmail.com")
OC = "https://api.opencitations.net/index/v1"
UA = "biomimicry-vault/1.0 (mailto:%s)" % MAILTO


def fetch(url, tries=5, timeout=300):
    """GET a URL with retries.  Returns bytes, or raises the last error."""
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001 - retry anything transient
            last = e
            time.sleep(3 * (i + 1))
    raise last


def cached_json(url, cache_dir, key):
    if cache_dir:
        os.makedirs(cache_dir, exist_ok=True)
        path = os.path.join(cache_dir, key + ".json")
        if os.path.exists(path):
            with open(path, "rb") as f:
                return json.loads(f.read().decode("utf-8"))
    raw = fetch(url)
    if cache_dir:
        with open(path, "wb") as f:
            f.write(raw)
    return json.loads(raw.decode("utf-8"))


def slug(doi):
    return doi.replace("/", "_").replace(".", "-")


def citers(doi, cache_dir=None):
    """Set of DOIs (lowercased) of works citing `doi`, per OpenCitations."""
    url = "%s/citations/%s" % (OC, urllib.parse.quote(doi))
    data = cached_json(url, cache_dir, "cit_" + slug(doi))
    out = set()
    for row in data:
        c = (row.get("citing") or "").strip().lower()
        if c.startswith("coci =>"):
            c = c.split("=>", 1)[1].strip()
        if c:
            out.add(c)
    return out


def references(doi, cache_dir=None):
    url = "%s/references/%s" % (OC, urllib.parse.quote(doi))
    data = cached_json(url, cache_dir, "ref_" + slug(doi))
    return {(r.get("cited") or "").strip().lower() for r in data if r.get("cited")}


def crossref_meta(doi):
    url = "https://api.crossref.org/works/%s?mailto=%s" % (
        urllib.parse.quote(doi), MAILTO)
    try:
        m = json.loads(fetch(url, tries=3, timeout=90).decode("utf-8"))["message"]
    except Exception:
        return {"doi": doi, "title": "<crossref lookup failed>"}
    return {
        "doi": doi,
        "title": (m.get("title") or ["<no title>"])[0],
        "year": (m.get("issued", {}).get("date-parts") or [[None]])[0][0],
        "journal": (m.get("container-title") or [""])[0],
        "type": m.get("type", ""),
        "abstract": m.get("abstract", ""),
    }


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    flags = [a for a in argv if a.startswith("--")]
    if len(args) < 2:
        print(__doc__)
        return 2
    cache = "./.oc-cache"
    for f in flags:
        if f.startswith("--cache"):
            cache = f.split("=", 1)[1] if "=" in f else cache
    a_doi, b_dois = args[0], args[1:]

    A = citers(a_doi, cache)
    B = set()
    for d in b_dois:
        B |= citers(d, cache)
    inter = sorted(A & B)

    print("provider: OpenCitations  endpoint: %s/citations/<doi>" % OC)
    print("anchor A: %s   N_A = %d" % (a_doi, len(A)))
    print("anchor B: %s   N_B = %d" % (" + ".join(b_dois), len(B)))
    print("|A n B| = %d   (%.2f%% of A, %.2f%% of B)" % (
        len(inter),
        100.0 * len(inter) / len(A) if A else 0.0,
        100.0 * len(inter) / len(B) if B else 0.0))
    # null model: expected co-citers if the two citer sets were independent draws
    # from a universe of N works.  Pass NULL_N to get observed/expected.
    n_univ = os.environ.get("NULL_N")
    if n_univ:
        exp = len(A) * len(B) / float(n_univ)
        print("expected under independence (N=%s): %.2f  observed/expected = %.2f"
              % (n_univ, exp, len(inter) / exp if exp else float("nan")))
    print()
    rows = []
    if "--enrich" in flags:
        for d in inter:
            rows.append(crossref_meta(d))
            time.sleep(0.2)
        for r in rows:
            print("%s | %s | %s | %s" % (
                r["doi"], r.get("year"), r.get("journal", "")[:40], r["title"][:110]))
    else:
        for d in inter:
            print(d)

    for f in flags:
        if f.startswith("--json="):
            with open(f.split("=", 1)[1], "w", encoding="utf-8") as fh:
                json.dump({"anchor_a": a_doi, "anchor_b": b_dois,
                           "n_a": len(A), "n_b": len(B),
                           "intersection": inter, "meta": rows}, fh, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
