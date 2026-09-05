#!/usr/bin/env python3
"""Europe PMC citer-set adapter (DOI -> PMID -> citations).

Endpoints:
    https://www.ebi.ac.uk/europepmc/webservices/rest/search
        ?query=DOI:"<doi>"&format=json                     -> resolve to a PMID
    https://www.ebi.ac.uk/europepmc/webservices/rest/<src>/<id>/citations
        ?format=json&pageSize=1000&page=<n>                -> citers

COVERAGE BIAS -- STATE THIS WHENEVER YOU QUOTE A EUROPE PMC NUMBER
------------------------------------------------------------------
Europe PMC is **biomedicine-weighted**.  It indexes MEDLINE, PubMed Central,
preprint servers and Agricola, and it reaches well outside biomedicine, but its
denominator is not the literature -- it is the life-sciences literature plus
whatever else happens to be deposited.

For this project that bias is *asymmetric across an anchor pair*, which is the
dangerous case.  A behavioural-ecology anchor (McNamara & Houston 1987) is
indexed; a power-systems engineering monograph (Billinton & Allan 1996) is not
indexed at all.  A zero intersection from Europe PMC across such a pair is a
**statement about Europe PMC**, not about the literature, and must never be
recorded as a gap finding on its own.  Use it as a *third* opinion where both
anchors resolve, and say so.

TWO-STEP RESOLUTION
-------------------
Most works this project touches have no PMID.  The adapter resolves the DOI
first; if the search returns no MEDLINE/PMC record, it raises `ProviderError`
saying "not indexed" -- **which is not a zero**.

KEYSPACE TRAP -- THE ONE THAT NEARLY PRODUCED A FALSE ZERO
----------------------------------------------------------
The `/citations` endpoint **returns no `doi` field at all**.  Each citation
record carries only `id` + `source` (a PMID, PMCID or preprint id), a title and
an author string.  A first cut of this adapter read `row["doi"]`, got `None`
every time, and reported Charnov 1976 as **1,719 records -> 0 unique DOIs** --
i.e. it would have contributed a clean 0 to every intersection while looking
like a working provider.

So Europe PMC does not live in the DOI keyspace.  This module sets
`KEYSPACE = "europepmc-id"` and returns keys of the form `epmc:MED:12345678`.
Those are comparable **only against another Europe PMC set**, which is fine --
an intersection is always within one provider.  `intersect.py` keeps each
keyspace separate when it builds the cross-provider hit union, and calls
`resolve_hits()` here to turn the handful of intersecting ids into DOIs for
inspection.  Resolving the *whole* citer set would cost one request per citer.

Note: the sibling `/references` endpoint 503'd on test (2026-09-03) and is not
wrapped here; use Crossref for reference lists.
"""

import urllib.parse

from . import ProviderError, cached_json, norm_doi, record

NAME = "europepmc"
BASE = "https://www.ebi.ac.uk/europepmc/webservices/rest"
ENDPOINT = BASE + "/<source>/<id>/citations?format=json&pageSize=1000"
AUTH_ENV = ()
RATE = "no key; no published hard limit, be polite (~1 req/s)"
KEYSPACE = "europepmc-id"
BIAS = ("BIOMEDICINE-WEIGHTED. MEDLINE/PMC/preprints/Agricola only. Physical-"
        "science and engineering anchors are often absent entirely, so a zero "
        "across a mixed pair says nothing about the literature. Citing records "
        "are keyed by PMID, not DOI -- see KEYSPACE TRAP in this module.")


def available():
    return True, "no key required"


def resolve(doi, cache_dir=None):
    """(source, id) for a DOI, or raise ProviderError if not indexed."""
    url = ("%s/search?query=DOI:%%22%s%%22&format=json&pageSize=5"
           % (BASE, urllib.parse.quote(doi, safe="/()")))
    data = cached_json(url, cache_dir, "epmc_res_" + doi, timeout=120)
    results = ((data.get("resultList") or {}).get("result") or [])
    for r in results:
        if r.get("id") and r.get("source"):
            return r["source"], r["id"]
    raise ProviderError(
        "Europe PMC does not index DOI %s -- coverage hole (Europe PMC is "
        "biomedicine-weighted), NOT zero citers." % doi)


def citers(doi, cache_dir=None, stats=None):
    src, pid = resolve(doi, cache_dir)
    out, raw, dropped, page = set(), 0, 0, 1
    while True:
        url = ("%s/%s/%s/citations?format=json&pageSize=1000&page=%d"
               % (BASE, src, pid, page))
        data = cached_json(url, cache_dir,
                           "epmc_cit_%s_p%d" % (doi, page), timeout=180)
        rows = ((data.get("citationList") or {}).get("citation") or [])
        raw += len(rows)
        for r in rows:
            rid, rsrc = r.get("id"), r.get("source")
            if rid and rsrc:
                out.add("epmc:%s:%s" % (rsrc, rid))
            else:
                dropped += 1
        if len(rows) < 1000:
            break
        page += 1
    record(stats, NAME, "%s (%s:%s)" % (doi, src, pid), raw, dropped, len(out))
    return out


def resolve_hits(keys, cache_dir=None):
    """Turn `epmc:SRC:ID` keys into DOIs, for inspecting an intersection.

    One search request per 20 ids.  Only ever call this on the intersection --
    resolving a whole citer set would be one request per citer.
    """
    out, keys = {}, list(keys)
    for i in range(0, len(keys), 20):
        chunk = [k.split(":", 2)[2] for k in keys[i:i + 20] if k.count(":") >= 2]
        if not chunk:
            continue
        q = " OR ".join('EXT_ID:"%s"' % c for c in chunk)
        url = ("%s/search?query=%s&format=json&pageSize=25"
               % (BASE, urllib.parse.quote(q)))
        try:
            data = cached_json(url, cache_dir, "epmc_hits_%d_%s"
                               % (i, chunk[0]), timeout=120)
        except ProviderError:
            continue
        for r in ((data.get("resultList") or {}).get("result") or []):
            d = norm_doi(r.get("doi"))
            if r.get("id"):
                out["epmc:%s:%s" % (r.get("source"), r["id"])] = d or "<no DOI>"
    return out
