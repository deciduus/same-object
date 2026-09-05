#!/usr/bin/env python3
"""OpenCitations (COCI / Meta) citer-set adapter.

Endpoint: https://api.opencitations.net/index/v1/citations/<doi>
The legacy host `opencitations.net/index/coci/api/v1/` 301-redirects here; use
the new host directly, because some clients drop the User-Agent across the
redirect.

TRAPS
-----
* **The phantom co-citer.**  Some records carry an empty `citing` field.
  Building a set without filtering adds a blank key `""`, which is in *every*
  set built the same way, so it inflates N_A, N_B **and every intersection by
  exactly 1** -- and 1 is exactly the count at which a gap claim becomes a
  bridge claim.  Blank keys are dropped here and the number dropped is printed.
* **HTTP 500 above ~10,000 citers.**  Shannon 1948 part I (~82,000 citers)
  returns `SystemExit: 1 (line 1412)` after ~4 minutes.  That is a size
  failure, not a missing work: **never record it as a zero.**  Fall through to
  OpenAlex, which handles the same anchor server-side.
* `/citation-count/<doi>` has returned a constant bogus `1` for a whole
  session.  Do not quote it without a counted `/citations/` cross-check.
"""

from . import ProviderError, cached_json, norm_doi, record

NAME = "opencitations"
BASE = "https://api.opencitations.net/index/v1"
ENDPOINT = BASE + "/citations/<doi>"
AUTH_ENV = ()
RATE = "no published per-second limit; be polite (~1 req/s)"
KEYSPACE = "doi"
BIAS = ("DOI-to-DOI only (COCI is built from Crossref deposits). Anything "
        "without a DOI is invisible. Broad discipline coverage, but only as "
        "good as publisher reference deposits.")


def available():
    return True, "no key required"


def _key(row, field):
    c = (row.get(field) or "").strip()
    if c.lower().startswith("coci =>"):
        c = c.split("=>", 1)[1]
    return norm_doi(c)


def citers(doi, cache_dir=None, stats=None):
    url = "%s/citations/%s" % (BASE, doi)
    try:
        data = cached_json(url, cache_dir, "oc_cit_" + doi, timeout=420)
    except ProviderError as e:
        if "500" in str(e):
            raise ProviderError(
                "OpenCitations 500 on %s -- this is the known large-anchor size "
                "failure (>~10k citers), NOT a zero. Use openalex for this "
                "anchor." % doi) from e
        raise
    out, dropped = set(), 0
    for row in data:
        c = _key(row, "citing")
        if c:
            out.add(c)
        else:
            dropped += 1
    record(stats, NAME, doi, len(data), dropped, len(out))
    return out


def references(doi, cache_dir=None, stats=None):
    """Set of DOIs `doi` cites.  Same blank-key filter, on the `cited` field."""
    url = "%s/references/%s" % (BASE, doi)
    data = cached_json(url, cache_dir, "oc_ref_" + doi, timeout=420)
    out, dropped = set(), 0
    for row in data:
        c = _key(row, "cited")
        if c:
            out.add(c)
        else:
            dropped += 1
    record(stats, NAME, doi + " (refs)", len(data), dropped, len(out))
    return out
