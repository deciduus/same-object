#!/usr/bin/env python3
"""Semantic Scholar Graph API citer-set adapter.

Endpoint:
    https://api.semanticscholar.org/graph/v1/paper/DOI:<doi>/citations
        ?fields=externalIds,year&limit=1000&offset=<n>

STATUS, 2026-09-05
------------------
**Works unauthenticated.**  The 2026-09-03 note in citation-sources.md that
called it "429 unauthenticated" was measured during a shared-pool spike, not a
permanent block -- the same failure mode as the OpenAlex "budget-locked" claim
that had expired by the next probe.  Unauthenticated calls go into a *shared*
pool of roughly 1 request/second across all anonymous users worldwide, so two
calls fired back to back will 429 while the same two spaced a second apart
succeed.  This adapter paces itself at ~1.1 s between requests and honours
`Retry-After`.

GETTING A KEY (raises the limit to a private 1 req/s, and lifts the shared-pool
lottery): the form at https://www.semanticscholar.org/product/api#api-key-form
-- free, academic use, approval takes a few days and arrives by email.  Set it
as `S2_API_KEY` and this adapter will send it as the `x-api-key` header
automatically.  **A key is not required for the adapter to work today.**

PAGING TRAP
-----------
`limit` is capped at 1000, and offset paging is capped at **offset 9999** --
past that the API returns HTTP 400.  An anchor with more than 10,000 citers
therefore cannot be fully enumerated here, exactly like OpenCitations' 500.
The adapter raises `ProviderError` rather than silently returning a truncated
set, because a truncated citer set produces a *smaller* intersection and so
manufactures the gap the method is meant to test.

DOI COVERAGE TRAP
-----------------
`DOI:<doi>` lookups are exact-match against S2's own `externalIds.DOI`, which
is stored **upper-cased**.  Case is handled server-side, but S2 simply does not
hold some old DOIs at all: Charnov 1976 (`10.1016/0040-5809(76)90040-x`) is
404 by DOI even though the paper is in the corpus under a `CorpusId`.  A 404
here means "this provider cannot see this anchor", **not zero citers**.
"""

import os
import urllib.parse

from . import ProviderError, cached_json, norm_doi, record

NAME = "semanticscholar"
BASE = "https://api.semanticscholar.org/graph/v1"
ENDPOINT = BASE + "/paper/DOI:<doi>/citations?fields=externalIds,year&limit=1000"
AUTH_ENV = ()          # optional, not required
OPTIONAL_AUTH_ENV = ("S2_API_KEY",)
RATE = ("~1 req/s in a SHARED anonymous pool (bursty 429s); a free key from "
        "semanticscholar.org/product/api#api-key-form gives a private 1 req/s")
KEYSPACE = "doi"
BIAS = ("Broad, all-field, includes non-DOI works; but its DOI index misses "
        "some pre-1990 records entirely (Charnov 1976 404s), and books/"
        "monographs by book-level DOI are largely absent.")

MAX_OFFSET = 9999


def available():
    return True, ("no key required; set S2_API_KEY for a private rate limit"
                  if not os.environ.get("S2_API_KEY") else "using S2_API_KEY")


def _headers():
    k = os.environ.get("S2_API_KEY")
    return {"x-api-key": k} if k else None


def citers(doi, cache_dir=None, stats=None):
    out, raw, dropped, offset, page = set(), 0, 0, 0, 0
    while True:
        url = ("%s/paper/DOI:%s/citations?fields=externalIds,year&limit=1000"
               "&offset=%d" % (BASE, urllib.parse.quote(doi, safe="/()"),
                               offset))
        try:
            data = cached_json(url, cache_dir, "s2_cit_%s_p%d" % (doi, page),
                               headers=_headers(), timeout=180, pause=1.1)
        except ProviderError as e:
            if "404" in str(e) and page == 0:
                raise ProviderError(
                    "Semantic Scholar has no record for DOI %s -- this is a "
                    "coverage hole, NOT zero citers. Do not record it as a "
                    "zero." % doi) from e
            raise
        rows = data.get("data") or []
        raw += len(rows)
        for r in rows:
            cp = r.get("citingPaper") or {}
            d = norm_doi((cp.get("externalIds") or {}).get("DOI"))
            if d:
                out.add(d)
            else:
                dropped += 1
        nxt = data.get("next")
        page += 1
        if not nxt:
            break
        if nxt > MAX_OFFSET:
            raise ProviderError(
                "Semantic Scholar offset paging caps at %d; anchor %s has more "
                "than that many citers, so the set would be TRUNCATED. A "
                "truncated citer set shrinks the intersection and manufactures "
                "a gap -- use openalex for this anchor." % (MAX_OFFSET, doi))
        offset = nxt
    record(stats, NAME, doi, raw, dropped, len(out))
    return out
