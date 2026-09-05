---
name: citation-sources
type: method
---

# Citation data sources that actually work

> OpenAlex and Semantic Scholar are not the only options, and assuming they were cost this
> project a blocked session. **Three independent sources work, are free, and need no key.**

## The working set

Verified by live fetch, 2026-09-03; endpoints and status re-verified 2026-09-05.

| Source | Endpoint | Gives | Status |
|---|---|---|---|
| **Crossref** | `api.crossref.org/works/<doi>?mailto=<email>` | **full reference lists with DOIs** | works |
| **OpenCitations** | `api.opencitations.net/index/v1/citations/<doi>` and `/references/<doi>` | both directions, DOI-keyed | works |
| **OpenAlex** | `api.openalex.org/works?filter=cites:<W-id>&mailto=<email>` (and `fulltext.search:`) | citers; **server-side intersection**; full-text search for DOI-less anchors | works, 2026-09-05 |
| **Europe PMC** | `ebi.ac.uk/europepmc/webservices/rest/MED/<pmid>/citations?format=json` | citers, paginated | works |
| Europe PMC references | `.../references?format=json` | — | **503 on test.** Use Crossref instead |
| OpenAlex (2026-09-03) | `api.openalex.org` | — | was **429, hours-long Retry-After**; polite pool works again as of 2026-09-05 |
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

## Endpoint moves and traps

### The OpenCitations host moved

`opencitations.net/index/coci/api/v1/` now **301-redirects** to `api.opencitations.net/index/v1/`.
Use the new host directly; the old path still resolves but the redirect is an extra round trip and
some clients drop the User-Agent across it.

### The traps, found the hard way

- **`/citation-count/<doi>` returned a constant bogus `1`** for a whole session on the old host.
  **Status 2026-09-05: no longer reproduces on `api.opencitations.net/index/v1/`.** It agreed
  exactly with a counted `/citations/` list on a control DOI (Alexander 1997: 40 = 40). Treat it
  as *usable but unproven*: it has been wrong before, so cross-check it against a counted
  `/citations/` list before quoting it.
- **`/citations/<doi>` returns HTTP 500 on very large citer sets.** Shannon 1948 part I
  (`10.1002/j.1538-7305.1948.tb01338.x`, ~82,000 citers) returns
  `HTTP status code 500: something unexpected happened - SystemExit: 1 (line 1412)` after ~3 min
  47 s (2026-09-05). Part II (9,771 citers) returns 200 in ~19 s. **For anchors above roughly
  10,000 citers, use OpenAlex instead** — see the recipe below. A 500 here is a size failure, not
  a missing work; never record it as a zero.
- **Crossref `?select=reference` returns HTTP 400.** Pull the full record and read
  `message.reference` from it.
- **String counts are not citation counts.** A relaxed Crossref match for "753 works" returned
  ~1.8M. Two catalogued figures (Alexander's "46 citations", the "753 works") were string
  artifacts, corrected in [[stress-strength-interference]]. Only inspected intersections count.

## Run a citation intersection: the citer-set method (preferred first pass)

**Do this before anything else.** The older recipe pulled anchor A's citers and then fetched each
citer's *reference list* to test for anchor B. That second step is what capped
[[G25-proofreading-coding]] at **28.4% coverage**, because reference lists are
publisher-deposited and many publishers deposit none.

**A citer-set intersection needs no reference lists at all.** Pull the citer DOI set of A, pull
the citer DOI set of B, intersect the two sets. **Coverage is then 100% of what the provider
indexes** - the only remaining caveat is the provider's own DOI-to-DOI coverage. It is also one
request per anchor instead of thousands.

### The script

`vault/_scripts/intersect.py` (stdlib only, caches raw responses, documents its own usage):

```
cd vault/_scripts
python intersect.py <doiA> <doiB> [<doiB2> ...] --cache=<dir> --enrich
```

- First DOI is anchor A; **all remaining DOIs are pooled as anchor B** - use this when a work has
  several DOIs (Shannon 1948 parts I and II) or when one side needs a broader canon than a single
  algorithm paper.
- `--enrich` fetches title / year / journal for each hit from Crossref so you can inspect them.
  **Inspection is not optional**: a count is not a finding until every hit has been read. Both
  [[G8-energy-per-bit-axis]] and [[G27-collective-decision]] turned on what the hits actually
  were, and one of G27's two hits was a book's back-matter bibliography.
- `NULL_N=160000000 python intersect.py ...` prints the [[citation-intersection]] null model:
  expected co-citers under independence = |A|x|B|/N, and observed/expected. **Report it.** A
  zero against an expectation of 0.1 says nothing at all.

### Worked results, 2026-09-05

| Gap | Anchors | N_A | N_B | intersection | obs/exp |
|---|---|---|---|---|---|
| G25 | Hopfield 1974 x Shannon 1948 pt I (**OpenAlex**, server-side `cites:` filter) | 1,656 | 82,198 | **36** | - |
| G25 | Hopfield 1974 x Shannon 1948 pt II (OpenCitations) | 1,542 | 9,771 | **8** | 85 |
| G8 | Landauer 1961 x (Laughlin 1998 + Attwell 2001) | 4,292 | 3,881 | **35** | ~340 |
| G27 | Dorigo 1996 x Lamport 1998 | 8,814 | 1,914 | **0** | - |
| G27 | Seeley 1999 x (Byzantine 1982 + FLP 1985) | 267 | 6,735 | **1** | 89 |

### When OpenCitations cannot do it

- **Anchor above ~10,000 citers** → OpenCitations 500s. Use OpenAlex, which will compute the
  intersection **server-side**:
  `api.openalex.org/works?filter=cites:<W_A>,cites:<W_B>&per-page=200&mailto=<email>`
  (comma is AND). Get the `W` ids from `api.openalex.org/works/doi:<doi>?mailto=<email>`.
- **Anchor has no DOI** (grey literature - IAEA TECDOCs, standards, agency reports) → no
  DOI-keyed provider can see it. Use `filter=fulltext.search:"<designator>"` on OpenAlex and
  classify the returned works by field. This is what completed the
  [[G7-how-passive]] trace (57 works, all nuclear). Treat the count as a **lower bound**.
- **Reference lists genuinely needed** (e.g. testing what a specific citer cites) → Crossref
  `api.crossref.org/works/<doi>?mailto=<email>` and read `message.reference`.

### Record this, every time

Provider + **exact endpoint** + fetch date + N for each side + intersection + coverage basis +
the null expectation. A number without all six is not quotable - see `CLAUDE.md`.
