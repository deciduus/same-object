#!/usr/bin/env python3
"""Lens.org scholarly API citer-set adapter.  TOKEN-GATED.

Endpoint:
    POST https://api.lens.org/scholarly/search
    Authorization: Bearer $LENS_TOKEN
    body: {"query": {"terms": {"reference.lens_id": ["<lens_id>"]}},
           "include": ["lens_id","doi"], "size": 500, "scroll": "1m"}

Two requests are needed: resolve the anchor DOI to a Lens id, then search for
works whose `reference.lens_id` contains it.  Lens does not expose a
`/citations/<doi>` convenience route.

**NO TOKEN IS PRESENT AND NONE HAS BEEN FABRICATED.**  `available()` returns
False with the reason below until `LENS_TOKEN` is set, and `citers()` raises
`NotConfigured`.  Probed unauthenticated 2026-09-05: HTTP 401
`{"message":"Missing/Incorrect Authorization Header","code":401}` -- i.e. the
host is reachable and the endpoint is live; only the credential is missing.

HOW THE OWNER GETS A TOKEN
--------------------------
1. Create a free account at https://www.lens.org/lens/user/subscriptions
2. Apply for the **Scholarly API** under the free *academic / non-commercial*
   tier at https://www.lens.org/lens/about/api/ (the "Request access" form
   asks for institution and intended use; an ASU affiliation qualifies).
3. Approval is manual and takes days to weeks.  The token appears under
   Profile -> API access as a JWT.
4. `setx LENS_TOKEN "<jwt>"` (Windows) or `export LENS_TOKEN=...` (POSIX).

Free academic tier at time of writing: request quota is per-month, not
per-second, and is small (order 10^3-10^4 records/month) -- so Lens is a
**tie-breaker for a disputed pair**, not a bulk provider.  Do not run `--all`
against Lens on large anchors.

WHY IT IS WORTH HAVING: Lens merges Crossref, PubMed, Microsoft Academic and
CORE, so its citer set is a genuinely different assembly from OpenAlex's or
OpenCitations' -- which is what makes a three-provider consensus meaningful
rather than two views of one deposit stream.
"""

import json
import os
import urllib.request

from . import NotConfigured, ProviderError, UA, norm_doi, record

NAME = "lens"
BASE = "https://api.lens.org/scholarly/search"
ENDPOINT = BASE + "  (POST, terms:{reference.lens_id:[<lens_id>]})"
AUTH_ENV = ("LENS_TOKEN",)
RATE = ("free academic tier: monthly record quota (small), ~10 req/min; "
        "tie-breaker only, not a bulk provider")
KEYSPACE = "doi"
BIAS = ("Merged index (Crossref + PubMed + MAG + CORE), so genuinely "
        "independent of the OpenAlex/OpenCitations deposit stream. Strong "
        "patent-literature coverage, which is noise for citer-set work.")


def available():
    if not os.environ.get("LENS_TOKEN"):
        return False, ("needs LENS_TOKEN env var -- free academic token from "
                       "lens.org/lens/about/api/ (manual approval)")
    return True, "using LENS_TOKEN"


def _post(payload, timeout=180):
    tok = os.environ.get("LENS_TOKEN")
    if not tok:
        raise NotConfigured(
            "lens: needs LENS_TOKEN env var. Free academic token: "
            "https://www.lens.org/lens/about/api/ -- see this module's "
            "docstring for the four steps. No token has been fabricated.")
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        BASE, data=body, method="POST",
        headers={"Authorization": "Bearer " + tok,
                 "Content-Type": "application/json",
                 "User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
    except Exception as e:  # noqa: BLE001
        raise ProviderError("lens POST failed: %r" % (e,)) from e


def lens_id(doi):
    d = _post({"query": {"term": {"doi": doi}},
               "include": ["lens_id", "doi"], "size": 1})
    hits = d.get("data") or []
    if not hits:
        raise ProviderError("lens: no record for DOI %s (coverage hole, not "
                            "zero citers)" % doi)
    return hits[0]["lens_id"]


def citers(doi, cache_dir=None, stats=None):
    lid = lens_id(doi)
    out, raw, dropped, scroll = set(), 0, 0, None
    while True:
        payload = {"query": {"terms": {"reference.lens_id": [lid]}},
                   "include": ["lens_id", "doi"], "size": 500, "scroll": "1m"}
        if scroll:
            payload = {"scroll_id": scroll, "scroll": "1m"}
        d = _post(payload)
        rows = d.get("data") or []
        raw += len(rows)
        for r in rows:
            v = r.get("doi")
            if isinstance(v, list):
                v = v[0] if v else None
            v = norm_doi(v)
            if v:
                out.add(v)
            else:
                dropped += 1
        scroll = d.get("scroll_id")
        if not rows or not scroll:
            break
    record(stats, NAME, doi, raw, dropped, len(out))
    return out
