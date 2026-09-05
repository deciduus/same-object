#!/usr/bin/env python3
"""OpenAlex citer-set adapter, with retry-after and budget handling.

Endpoints:
    https://api.openalex.org/works/doi:<doi>?mailto=<email>        -> W id
    https://api.openalex.org/works?filter=cites:<Wid>&per-page=200
        &cursor=*&select=id,doi&mailto=<email>                     -> citers

WHY THE CURSOR AND NOT `page=`
------------------------------
OpenAlex caps offset paging at 10,000 results.  Every anchor this project cares
about can exceed that (Shannon 1948 pt I has 82,198 citers), so the adapter
uses `cursor=*` paging, which has no ceiling.

TWO DIFFERENT REFUSALS, AND WHY THEY MUST NOT BE CONFLATED
----------------------------------------------------------
* **Rate limit (HTTP 429).**  Transient.  `Retry-After` is honoured
  automatically by `providers.fetch`; a few seconds of sleep fixes it.
* **Daily budget exhausted.**  The body says "Insufficient budget" and the run
  is over *for the day*, regardless of how long you wait.  This is what
  happened when more than about four agents ran against OpenAlex in parallel
  during the 2026-09-05 rounds, and three gap notes recorded a false
  "OpenAlex blocked" that had in fact expired by the next probe.
  `providers.fetch` raises `BudgetExhausted` for this case so `--all` can drop
  OpenAlex and keep the other providers' numbers.

Anchors with no DOI are invisible here too; use `filter=fulltext.search:"..."`
by hand for those (see vault/method/citation-sources.md).
"""

import urllib.parse

from . import ProviderError, cached_json, norm_doi, record, MAILTO

NAME = "openalex"
BASE = "https://api.openalex.org"
ENDPOINT = BASE + "/works?filter=cites:<Wid>&per-page=200&cursor=*"
AUTH_ENV = ()
RATE = ("100k calls/day and 10/s in the polite pool (mailto=); over-parallel "
        "agents exhaust the DAILY budget, which returns an 'Insufficient "
        "budget' body, not a 429")
KEYSPACE = "doi"
BIAS = ("Broadest coverage of the free providers; indexes non-DOI works, but "
        "this adapter keys on DOI so DOI-less citers are dropped (counted as "
        "'DOI-less dropped'). Counts run 10-25% above OpenCitations.")


def available():
    return True, "no key required (set MAILTO for the polite pool)"


def work_id(doi, cache_dir=None):
    """OpenAlex W id for a DOI, or raise ProviderError."""
    url = "%s/works/doi:%s?mailto=%s&select=id,doi,cited_by_count" % (
        BASE, urllib.parse.quote(doi, safe="/()"), MAILTO)
    data = cached_json(url, cache_dir, "oa_work_" + doi, timeout=120)
    wid = (data.get("id") or "").rsplit("/", 1)[-1]
    if not wid.startswith("W"):
        raise ProviderError("OpenAlex: no W id for %s" % doi)
    return wid


def citers(doi, cache_dir=None, stats=None):
    wid = work_id(doi, cache_dir)
    out, raw, dropped, cursor, page = set(), 0, 0, "*", 0
    while cursor:
        url = ("%s/works?filter=cites:%s&per-page=200&cursor=%s"
               "&select=id,doi&mailto=%s"
               % (BASE, wid, urllib.parse.quote(cursor, safe=""), MAILTO))
        data = cached_json(url, cache_dir,
                           "oa_cit_%s_p%d" % (doi, page), timeout=180)
        results = data.get("results") or []
        raw += len(results)
        for r in results:
            d = norm_doi(r.get("doi"))
            if d:
                out.add(d)
            else:
                dropped += 1
        cursor = (data.get("meta") or {}).get("next_cursor")
        page += 1
        if not results:
            break
    record(stats, NAME, doi, raw, dropped, len(out))
    return out
