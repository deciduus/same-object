---
name: citation-sources
type: method
---

# Citation data sources that actually work

> OpenAlex and Semantic Scholar are not the only options, and assuming they were cost this
> project a blocked session. **Three independent sources work, are free, and need no key.**

## The working set

Verified by live fetch, 2026-09-03.

| Source | Endpoint | Gives | Status |
|---|---|---|---|
| **Crossref** | `api.crossref.org/works/<doi>?mailto=<email>` | **full reference lists with DOIs** | works |
| **OpenCitations** | `opencitations.net/index/coci/api/v1/references/<doi>` and `/citations/<doi>` and `/citation-count/<doi>` | both directions, DOI-keyed | works |
| **Europe PMC** | `ebi.ac.uk/europepmc/webservices/rest/MED/<pmid>/citations?format=json` | citers, paginated | works |
| Europe PMC references | `.../references?format=json` | — | **503 on test.** Use Crossref instead |
| OpenAlex | `api.openalex.org` | — | **429, hours-long Retry-After** |
| Semantic Scholar | `api.semanticscholar.org` | — | **429 unauthenticated** |

Spot check on `10.1073/pnas.2023348118`: Crossref returned **71 references, 70 with DOIs**;
OpenCitations returned **71**; the two agree. Europe PMC returned **49 citers** for the same
work by PMID.

## Why this matters more than it looks

[[citation-intersection]] — the strongest evidence standard here — needs exactly two things:
the citers of a work, and the reference lists of those citers. **Crossref supplies the second
and OpenCitations supplies both.** So the standard was never actually blocked; one vendor was.

## The rule that follows

**A blocked API is not a blocked method.** Before recording anything as
`not-assessed` because a lookup failed, check whether a different source answers the same
question. Citation data is mirrored across at least four independent providers.

The same logic that [[M4-change-the-actor]] applies to physics applies to infrastructure: when
a route is blocked, swap the category of the thing doing the work rather than waiting.

## Practical notes

- Crossref: pass `mailto=` for the polite pool. Reference lists are publisher-deposited, so
  coverage varies — some publishers deposit none. Check `reference-count` before trusting a zero.
- OpenCitations COCI is DOI-to-DOI only. Anything without a DOI is invisible to it.
- Europe PMC is biomedicine-weighted but indexes far outside it; calibrate before trusting a
  zero, per [[failure-modes]].
- **Two sources agreeing is the check.** Crossref and OpenCitations are independently
  assembled, so a match is meaningful.

## Two endpoint traps, found the hard way

- **OpenCitations `/citation-count/<doi>` returned a constant bogus `1`** for a whole session.
  Do not trust it. Use `/citations/<doi>` and count the returned list instead.
- **Crossref `?select=reference` returns HTTP 400.** Pull the full record and read
  `message.reference` from it.
- **String counts are not citation counts.** A relaxed Crossref match for "753 works" returned
  ~1.8M. Two catalogued figures (Alexander's "46 citations", the "753 works") were string
  artifacts, corrected in [[stress-strength-interference]]. Only inspected intersections count.
