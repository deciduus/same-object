#!/usr/bin/env python3
"""Scopus / Web of Science stub adapter.  NOT IMPLEMENTED -- deliberately.

The repo owner is an ASU student, so both of these are reachable *from campus
or the ASU VPN*.  They are the two providers whose citer sets are genuinely
independent of the Crossref deposit stream that OpenAlex, OpenCitations and
(largely) Semantic Scholar all draw on, so they are the strongest available
check on a gap claim.  Neither is implemented here, because implementing an
adapter that cannot be run is how a fabricated number gets into a note.

WHY A STUB AND NOT AN IMPLEMENTATION
------------------------------------
Both APIs bind the key to an institutional **IP range**, not to the key alone.
A key held on a laptop off-VPN returns `AUTHENTICATION_ERROR` even when it is
valid, so an adapter written blind cannot be tested, and an untested adapter
that returns an empty set on an auth failure would record a **false zero** --
precisely the failure this project has already had to correct once.  When the
owner is on campus and has a key, fill in `citers()` against the endpoints
below and delete this paragraph.

SCOPUS (Elsevier)
-----------------
Get a key: https://dev.elsevier.com/ -> "I want an API key", sign in with the
ASU institutional account.  Free for non-commercial academic use.  The key is
issued instantly; **entitlement comes from ASU's subscription and is checked by
IP**, so requests must originate from an ASU campus network or the ASU
Cisco/GlobalProtect VPN.  An `insttoken` (requested from Elsevier support via
the ASU library) lifts the IP requirement for off-campus use.

    Citing works for a DOI, in two steps:
      GET https://api.elsevier.com/content/search/scopus
          ?query=DOI(<doi>)&field=eid
          -> the anchor's EID, e.g. 2-s2.0-0016961974
      GET https://api.elsevier.com/content/search/scopus
          ?query=REFEID(<eid>)&count=25&start=<n>&field=doi,eid
          -> the citing works, paged 25 at a time (200 with a full key)
    Headers: X-ELS-APIKey: $SCOPUS_API_KEY
             X-ELS-Insttoken: $SCOPUS_INSTTOKEN   (optional, off-campus)
    Quota: 20,000 Scopus Search requests/week, 9 req/s.

    Note `REFEID()` is the citing-works query; `citedby-count` in a record is a
    **count only**, the same trap as Crossref's `is-referenced-by-count`.

WEB OF SCIENCE (Clarivate) -- Starter API
-----------------------------------------
Get a key: https://developer.clarivate.com/ -> register -> subscribe to
"Web of Science Starter API" (free tier, 5 req/s, 5,000 requests/day).  The
free Starter tier works off-campus, but returns **metadata for the WoS Core
Collection only if the institution is entitled**; ASU is, via the library's
subscription, and entitlement is again IP-checked unless a proxy is used.

    GET https://api.clarivate.com/apis/wos-starter/v1/documents
        ?q=DO=(<doi>)                     -> the anchor's UID, e.g. WOS:A1976...
    GET https://api.clarivate.com/apis/wos-starter/v1/documents
        ?q=CITING=(<uid>)&limit=50&page=<n>
    Header: X-ApiKey: $WOS_API_KEY

    Trap: the Starter API's document record carries `citations` as a count
    array per database; that is not a citer set.  Only the `CITING=` query
    enumerates the citing works.

ENV VARS AN IMPLEMENTATION WOULD EXPECT
---------------------------------------
    SCOPUS_API_KEY       required
    SCOPUS_INSTTOKEN     optional, for off-campus
    WOS_API_KEY          required (a separate adapter; not stubbed separately)
"""

import os

from . import NotConfigured

NAME = "scopus"
BASE = "https://api.elsevier.com/content/search/scopus"
ENDPOINT = BASE + "?query=REFEID(<eid>)&field=doi,eid   [STUB, not implemented]"
AUTH_ENV = ("SCOPUS_API_KEY",)
RATE = "20,000 Scopus Search requests/week, 9 req/s, with an entitled key"
KEYSPACE = "doi"
BIAS = ("Curated, journal-selective: excludes much grey literature and many "
        "non-English venues, so counts run BELOW OpenAlex. Independent of the "
        "Crossref deposit stream, which is exactly why it is worth having.")

_MSG = ("scopus: needs SCOPUS_API_KEY and institutional access. The key is "
        "free from dev.elsevier.com with an ASU account, but entitlement is "
        "checked by IP -- run from an ASU campus network or the ASU VPN, or "
        "set SCOPUS_INSTTOKEN. Adapter is a documented STUB and is NOT "
        "implemented: see providers/scopus.py for the exact citing-works "
        "endpoints (Scopus REFEID(), WoS Starter CITING=) to fill in.")


def available():
    if not os.environ.get("SCOPUS_API_KEY"):
        return False, "needs SCOPUS_API_KEY + institutional access (stub)"
    return False, ("SCOPUS_API_KEY is set, but this adapter is still a stub -- "
                   "implement citers() against the endpoints in the docstring")


def citers(doi, cache_dir=None, stats=None):
    raise NotConfigured(_MSG)
