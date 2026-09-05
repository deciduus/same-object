#!/usr/bin/env python3
"""
providers/ - citer-set adapters, one module per provider.  Stdlib only.

WHY
---
Every citer-set intersection this project quotes has come from one of two
providers, and each of them has a hard failure mode that stops a round dead:

  * OpenAlex exhausts a **daily** budget when more than about four agents run
    against it at once (the body says "Insufficient budget", not a 429).
  * OpenCitations returns **HTTP 500** on anchors above roughly 10,000 citers.

A blocked API is not a blocked method (see vault/method/citation-sources.md).
This package makes that rule executable: name a provider with `--providers`, or
run `--all` and read the per-provider table.

THE INTERFACE
-------------
Every provider module exposes:

    NAME        str    short lowercase id, matches the module name
    ENDPOINT    str    the exact URL template, for the provenance record
    AUTH_ENV    tuple  env var names required, () if none
    BIAS        str    one line on coverage bias, for the provenance record
    available() -> (bool, reason)      is this provider usable right now?
    citers(doi, cache_dir=None, stats=None) -> set[str]

`citers` returns **lower-cased DOI strings** with no scheme or `doi.org/`
prefix, blank/whitespace keys dropped.  It records
`stats[(NAME, doi)] = {"raw", "blank_dropped", "unique"}` when `stats` is
given, so the caller can print how many phantom keys were filtered.

Failures raise `ProviderError` (or `NotConfigured` for a missing key, or
`BudgetExhausted` for a spent daily quota) rather than returning an empty set.
**An empty set and a failed fetch must never be confused**: one is a finding,
the other is a broken run.
"""

import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

MAILTO = os.environ.get("MAILTO", "deciduusleaf@gmail.com")
UA = "biomimicry-vault/1.0 (mailto:%s)" % MAILTO

# Cache directory.  Kept as `.oc-cache` -- the name is historical (it was
# OpenCitations-only) but it is already gitignored, and renaming it would
# orphan every cached response from the 2026-09-05 rounds.  Each provider
# namespaces its own files with a `<NAME>_` prefix, so the shared directory is
# safe.
DEFAULT_CACHE = os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "_scripts", ".oc-cache")


class ProviderError(RuntimeError):
    """A provider failed in a way that is not a zero-citer answer."""


class NotConfigured(ProviderError):
    """Provider needs a key/token that is not present in the environment."""


class BudgetExhausted(ProviderError):
    """Provider refused on a spent daily/period quota, not a per-second limit.

    Distinct from a rate limit: waiting a few seconds will not help.
    """


def norm_doi(s):
    """Lower-case a DOI and strip any scheme/host prefix.  "" if not a DOI."""
    if not s:
        return ""
    s = str(s).strip().lower()
    s = re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", s)
    s = re.sub(r"^doi:", "", s)
    s = s.strip()
    return s if s.startswith("10.") else ""


def slug(s):
    """Filesystem-safe key for a cache filename."""
    return re.sub(r"[^A-Za-z0-9._-]", "_", str(s))[:180]


def fetch(url, headers=None, tries=5, timeout=180, pause=1.0):
    """GET a URL, honouring Retry-After and separating budget from rate limit.

    Returns the response body as bytes.

    * **429** -> read `Retry-After`; if it is a small number of seconds, sleep
      and retry.  If the header is absent, back off 3s, 6s, 9s ...  If the
      server asks for longer than `MAX_RETRY_AFTER` seconds, give up rather
      than parking the run for hours (OpenAlex has returned multi-hour
      Retry-After values).
    * **403 with "insufficient budget" in the body** -> `BudgetExhausted`.
      OpenAlex signals a spent *daily* quota this way, and retrying is
      pointless; the caller should drop this provider and continue with the
      others rather than failing the whole run.
    """
    h = {"User-Agent": UA, "Accept": "application/json"}
    if headers:
        h.update(headers)
    max_retry_after = float(os.environ.get("MAX_RETRY_AFTER", "120"))
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=h)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                body = r.read()
            if pause:
                time.sleep(pause)
            return body
        except urllib.error.HTTPError as e:
            body = b""
            try:
                body = e.read()
            except Exception:  # noqa: BLE001
                pass
            text = body.decode("utf-8", "replace").lower()
            if "insufficient budget" in text or "daily limit" in text:
                raise BudgetExhausted(
                    "%s: daily budget exhausted (HTTP %s) -- not a rate limit; "
                    "waiting will not help. Body: %s"
                    % (url, e.code, text[:200]))
            if e.code in (429, 503):
                ra = e.headers.get("Retry-After") if e.headers else None
                wait = None
                if ra:
                    try:
                        wait = float(ra)
                    except ValueError:
                        wait = None          # HTTP-date form; fall through
                if wait is not None and wait > max_retry_after:
                    raise ProviderError(
                        "%s: HTTP %s with Retry-After %ss, above MAX_RETRY_AFTER=%s"
                        % (url, e.code, ra, max_retry_after))
                time.sleep(wait if wait is not None else 3.0 * (i + 1))
                last = e
                continue
            last = e
            if e.code in (400, 401, 404):
                raise ProviderError("%s: HTTP %s %s"
                                    % (url, e.code, text[:200])) from e
            time.sleep(2.0 * (i + 1))
        except Exception as e:  # noqa: BLE001 - retry anything transient
            last = e
            time.sleep(2.0 * (i + 1))
    raise ProviderError("%s: gave up after %d tries (%r)" % (url, tries, last))


def cached_json(url, cache_dir, key, headers=None, **kw):
    """Fetch and JSON-decode `url`, caching the raw bytes under `key`."""
    path = None
    if cache_dir:
        os.makedirs(cache_dir, exist_ok=True)
        path = os.path.join(cache_dir, slug(key) + ".json")
        if os.path.exists(path):
            with open(path, "rb") as f:
                raw = f.read()
            try:
                return json.loads(raw.decode("utf-8"))
            except ValueError:
                os.remove(path)              # poisoned cache entry; refetch
    raw = fetch(url, headers=headers, **kw)
    data = json.loads(raw.decode("utf-8"))
    if path:
        with open(path, "wb") as f:
            f.write(raw)
    return data


def record(stats, name, doi, raw, dropped, unique):
    """Write one provider/anchor row into the shared stats dict and log it."""
    print("  [%s] %s -> %d records, %d blank/DOI-less dropped, %d unique"
          % (name, doi, raw, dropped, unique), file=sys.stderr)
    if stats is not None:
        stats[(name, doi)] = {"raw": raw, "blank_dropped": dropped,
                              "unique": unique}


# --- registry ---------------------------------------------------------------

from . import opencitations, openalex, semanticscholar, europepmc, lens, scopus  # noqa: E402

#: Order matters: the first two are the historical pair, the rest are additions.
ALL = [opencitations, openalex, semanticscholar, europepmc, lens, scopus]
BY_NAME = {m.NAME: m for m in ALL}


def resolve(names):
    """Turn a list of provider names into modules, erroring on unknown ones."""
    out = []
    for n in names:
        n = n.strip().lower()
        if not n:
            continue
        if n not in BY_NAME:
            raise SystemExit("unknown provider %r; known: %s"
                             % (n, ", ".join(BY_NAME)))
        out.append(BY_NAME[n])
    return out


def usable():
    """Providers whose `available()` says yes right now."""
    return [m for m in ALL if m.available()[0]]
