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
| **Semantic Scholar** | `api.semanticscholar.org/graph/v1/paper/DOI:<doi>/citations` | citers, paginated | **works unauthenticated, 2026-09-05** — the old "429" reading was a shared-pool spike, not a block |

**Correction, 2026-09-05.** The last row previously read "Semantic Scholar — **429
unauthenticated**". That was measured during a burst against a *shared* anonymous pool and then
recorded as a permanent property. It is not one: paced at ~1.1 s between requests, Semantic
Scholar enumerated 4,605 citer records for Scheffer 2009 and 2,095 for Si 2011 with no key at
all (worked table below). This is the **same error shape** as the "OpenAlex budget-locked" claim
that three gap notes carried and that had expired by the next probe. A provider that refused
once is not a provider that refuses.

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

## The full provider table

Six providers, evaluated 2026-09-05. `vault/_scripts/providers/` holds one adapter module per
row, all stdlib-only, behind a common `citers(doi) -> set` interface; `intersect.py --all` runs
every available one and prints a per-provider table plus a consensus range.

| Provider | Auth | Rate limit | Keyspace | Coverage bias | Known traps |
|---|---|---|---|---|---|
| **OpenCitations** | none | none published; be polite (~1/s) | DOI | DOI-to-DOI only, from Crossref deposits; DOI-less works invisible | **500 above ~10k citers** (a size failure, never a zero); the **blank `citing` phantom** inflates every intersection by 1; `/citation-count/` has returned a bogus constant 1 |
| **OpenAlex** | none (`mailto=` for the polite pool) | 100k calls/day, 10/s — a **daily budget**, exhausted by >4 parallel agents | DOI (adapter drops DOI-less citers) | Broadest of the free set; counts run **10–25% above OpenCitations** | "Insufficient budget" arrives as **HTTP 429 with a ~13-hour `retryAfter`**, not an ordinary rate limit — see below. Offset paging caps at 10,000; use `cursor=*` |
| **Semantic Scholar** | none; optional free key | ~1/s in a **shared anonymous** pool → bursty 429s | DOI | Broad, all-field; **misses some pre-1990 DOIs entirely**, and book-level DOIs | Charnov 1976 is a hard **404 by DOI**; offset paging caps at **9,999**, so a >10k-citer anchor would silently truncate (the adapter raises instead) |
| **Europe PMC** | none | none published; be polite | **PMID, not DOI** | **Biomedicine-weighted**: MEDLINE / PMC / preprints / Agricola. Engineering and physical-science anchors are often absent outright | The `/citations` response carries **no `doi` field at all** — see the keyspace trap below. `/references` 503s |
| **Lens.org** | **needs `LENS_TOKEN`** | free academic tier: a small **monthly record** quota | DOI | Merged Crossref + PubMed + MAG + CORE, so genuinely independent of the others; heavy patent content is noise here | Not a bulk provider — a tie-breaker for one disputed pair. Probed unauthenticated 2026-09-05: HTTP 401 `Missing/Incorrect Authorization Header`, i.e. live, credential missing |
| **Scopus / Web of Science** | **needs key + institutional IP** | Scopus 20k/week, 9/s | DOI | Curated and journal-selective; counts run **below** OpenAlex. Independent of the Crossref deposit stream | **Documented stub, deliberately not implemented** — an untested adapter returning `set()` on an auth failure would write a false zero |

### Which work unauthenticated today

**Three carry a DOI-keyed intersection on their own: OpenCitations, OpenAlex, Semantic
Scholar.** Europe PMC also needs no key, but answers in its own keyspace and against a
biomedical denominator. Lens and Scopus/WoS need credentials the owner does not hold.

### The two keys worth getting, and how

- **Semantic Scholar** — free; raises the shared ~1/s pool to a private one and removes the
  burst-429 lottery. Form: <https://www.semanticscholar.org/product/api#api-key-form>. Academic
  use; approval takes days and arrives by email. Set `S2_API_KEY` and the adapter sends it as
  `x-api-key` automatically. **Not required** — the adapter works today without it.
- **Lens.org** — free academic / non-commercial tier. Account at
  <https://www.lens.org/lens/user/subscriptions>, then request Scholarly API access at
  <https://www.lens.org/lens/about/api/>; the form asks for institution and intended use, and an
  ASU affiliation qualifies. Approval is manual, days to weeks. The token appears under
  Profile → API access as a JWT; set `LENS_TOKEN`.
  **No token has been fabricated anywhere in this toolkit.**

### ASU institutional access — documented, not implemented

The owner is an ASU student, so the two subscription providers are reachable from campus or the
ASU VPN. Both are **documented in `vault/_scripts/providers/scopus.py` and left as a stub**,
because both bind entitlement to an **institutional IP range** rather than to the key: an
adapter written blind cannot be tested, and one that swallowed an auth failure into an empty set
would manufacture a false zero — the exact failure this project has already had to correct once.

| | Get a key | Citing-works endpoint | Env vars |
|---|---|---|---|
| **Scopus** (Elsevier) | <https://dev.elsevier.com/> → "I want an API key", signed in with the ASU account. Issued instantly; entitlement is ASU's subscription and is checked by IP | `GET api.elsevier.com/content/search/scopus?query=DOI(<doi>)&field=eid` → the EID, then `?query=REFEID(<eid>)&count=25&start=<n>&field=doi,eid`. Header `X-ELS-APIKey` | `SCOPUS_API_KEY`; optional `SCOPUS_INSTTOKEN` (an insttoken, requested from Elsevier support via the ASU library, lifts the IP requirement off-campus) |
| **Web of Science Starter** (Clarivate) | <https://developer.clarivate.com/> → register → subscribe to the free "Web of Science Starter API" tier (5/s, 5,000/day) | `GET api.clarivate.com/apis/wos-starter/v1/documents?q=DO=(<doi>)` → the UID, then `?q=CITING=(<uid>)&limit=50&page=<n>`. Header `X-ApiKey` | `WOS_API_KEY` |

Trap in both: `citedby-count` (Scopus) and the per-database `citations` array (WoS Starter) are
**counts only** — the same trap as Crossref's `is-referenced-by-count`. Only `REFEID()` and
`CITING=` enumerate the citing works.

### The three that cannot do this job — verdicts

- **Crossref Event Data — NO, and the host is unreachable.** `api.eventdata.crossref.org`
  resolves (`34.251.73.224`) but the TCP connection **times out** on every attempt, 2026-09-05.
  Even when it answered, Event Data collected *social and web* events — tweets, Wikipedia
  edits, blogs, DataCite links — **not journal-to-journal citations**, so it was never a
  citer-set source. Crossref's own `is-referenced-by-count` is a **count only** and yields no
  citing DOIs. **Verdict: not a provider; do not build an adapter.**
- **CORE (`api.core.ac.uk/v3`) — NO.** Reachable unauthenticated. A work record carries
  `citationCount` (a count) and `references` (**outgoing**), and the v3 API exposes
  `/search/works` and `/outputs/{id}` and **no citing-works route at all**. Its value to this
  project is full text, not citation direction. Related trap seen while probing:
  `q=title:"marginal value theorem"` returned **758,409** hits — relaxed matching, the
  string-count trap again. **Verdict: not a citer-set provider.**
- **BASE — NO.** `api.base-search.net` replies
  `{"error": "Access denied for IP address … and user agent …"}`: it is **IP-whitelist only**,
  granted by application, and it is a discovery index with no citing-works endpoint regardless.
  **Verdict: not a provider.**

### The Europe PMC keyspace trap

The `/citations` endpoint returns **no `doi` field**. Each record carries only `id` + `source`
(a PMID, PMCID or preprint id), a title and an author string. The first cut of the adapter read
`row["doi"]`, got `None` every time, and reported Charnov 1976 as **1,719 records → 0 unique
DOIs** — a provider that looks like it is working while contributing a clean **0** to every
intersection. That is the false-zero failure mode in its purest form, and it was caught only
because the adapter prints its dropped count per anchor.

Europe PMC therefore does not live in the DOI keyspace. The adapter sets
`KEYSPACE = "europepmc-id"` and returns `epmc:MED:12345678` keys, which are comparable only
against another Europe PMC set — which is all an intersection ever needs, since both sides come
from one provider. `intersect.py` keeps keyspaces separate when it unions hits across providers,
and resolves only the intersecting handful back to DOIs for inspection.

**Print the dropped count, always.** It is the only thing that distinguishes "this provider sees
nothing" from "this adapter is reading the wrong field".

### OpenAlex: budget exhaustion is not a rate limit

Measured 2026-09-05, mid-round, with four other agents live:

```
HTTP 429 {"error":"Rate limit exceeded",
          "message":"Insufficient budget. This request costs $0.0001 but you only have
                     $0 remaining. Resets at midnight UTC. ...",
          "retryAfter":47052, "dailyRemainingUsd":0}
```

The status code says rate limit; the body says the day is over. `retryAfter` is **47,052
seconds — 13 hours**. A client that honours `Retry-After` blindly parks the round until
tomorrow; a client that retries on 429 burns its remaining tries for nothing. `providers.fetch`
therefore inspects the body: `"insufficient budget"` raises `BudgetExhausted`, which `--all`
reports as an `err` row and steps past, keeping every other provider's numbers. Ordinary 429s
still sleep and retry, and any `Retry-After` above `MAX_RETRY_AFTER` (default 120 s) aborts
rather than parking.

This is why three gap notes recorded "OpenAlex blocked" as a property of OpenAlex when it was a
property of that afternoon.

## Worked example: `intersect.py --all`, 2026-09-05

Endpoints exactly as in the provider table. `AnB` is the intersection; `blanks` counts
blank/DOI-less keys dropped before the sets were built; `err` rows are **failed fetches, never
zeros**.

### G28 anchors — Charnov 1976 × Gittins 1979

`10.1016/0040-5809(76)90040-x` × `10.1111/j.2517-6161.1979.tb01068.x`

```
provider              N_A      N_B    AnB   blanks  status
opencitations        4088     1012      5       41  ok
openalex                -        -    err        -  BudgetExhausted: daily budget spent, retryAfter 47052s
semanticscholar         -        -    err        -  no record for DOI 10.1016/0040-5809(76)90040-x (coverage hole)
europepmc               -        -    err        -  does not index 10.1111/j.2517-6161.1979.tb01068.x

consensus over 1 provider(s) [opencitations]: |A n B| in [5, 5]
hits: 10.1007/978-3-319-51721-6_6, 10.1016/b978-0-12-820480-1.00058-9,
      10.1016/j.anbehav.2026.123491, 10.1103/physreve.97.022110, 10.3758/s13423-016-1158-7
```

**The intersection of 5 reproduces [[citation-intersection]]'s G28 row exactly**, and it is the
only number here that anyone can quote. Three of the four free providers cannot see this pair
at all, for three *different* reasons — a spent budget, a missing old DOI, a biomedical
denominator. Note also that `N_A` = 4,088 against the note's recorded 5,424: **a same-provider
disagreement across dates that must not be silently reconciled** (CLAUDE.md, two-true-numbers).

### G34 anchors — Billinton & Allan 1996 × McNamara & Houston 1987

`10.1007/978-1-4899-1860-4` × `10.2307/1939235`

```
provider              N_A      N_B    AnB   blanks  status
opencitations        2058      422      0        1  ok
openalex                -        -    err        -  BudgetExhausted: daily budget spent
semanticscholar         -        -    err        -  no record for DOI 10.1007/978-1-4899-1860-4 (book-level DOI)
europepmc               -        -    err        -  does not index 10.1007/978-1-4899-1860-4

consensus over 1 provider(s) [opencitations]: |A n B| in [0, 0]
```

**A one-provider zero.** Union floor `N = 2,480`, so `E = 2058·422/2480 = 350` — which is why
this zero looks striking and why one provider is not enough to bank it. `E` is quoted at the
floor only; a field-scale `N` is still owed, per [[citation-intersection]].

The Semantic Scholar row is worth reading closely. S2 *does* hold Billinton & Allan — under
`10.1007/978-1-4615-7731-7`, the **1984 first edition**, with 3,001 citations. A title match
returns that record. **Do not substitute it**: different edition, different DOI, different citer
set. The adapter deliberately does no fuzzy title fallback for exactly this reason (the same
probe matched "Optimal foraging, the marginal value theorem" to a 2012 paper titled
"… the Marginal Value Theorem revisited", 1 citation). A near-miss title match is a
**different work**, and swapping one in is how a fabricated citer set enters a note.

### Control — Scheffer 2009 × Si 2011 (the `--selftest` pair, where providers overlap)

`10.1038/nature08227` × `10.1016/j.ejor.2010.11.018`

```
provider              N_A      N_B    AnB   blanks  status
opencitations        3934     1783      1       77  ok
openalex                -        -    err        -  BudgetExhausted: daily budget spent
semanticscholar      3957     1891      1      803  ok
europepmc               -        -    err        -  does not index 10.1016/j.ejor.2010.11.018

consensus over 2 provider(s) [opencitations, semanticscholar]: |A n B| in [1, 1]  -- providers AGREE
  N_A spread 3934-3957 (1%)   N_B spread 1783-1891 (6%)
hit found by both: 10.1007/s42524-021-0176-y
```

**This is the row that makes the toolkit worth having.** Two independently assembled providers,
different corpora, different DOI-less drop rates (77 vs 803) — and they return **the same single
hit DOI**. `audits/07-provenance-rounds3-6.md` re-derived that 1 from OpenCitations alone;
it now stands on two providers.

And a second biomedical control, where Europe PMC does answer:

```
10.1371/journal.pone.0176493 x 10.1186/s12864-017-3608-7
provider              N_A      N_B    AnB   blanks  status
europepmc              44       45      0        0  ok
opencitations          56       48      0        2  ok
consensus: |A n B| in [0, 0]   N_A spread 44-56 (21%)   N_B spread 45-48 (6%)
```

The 21% `N_A` spread on a pair both providers fully index is the **10–25% provider disagreement**
from `audits/07-provenance-rounds3-6.md`, reproduced on demand.

### What the consensus line is for

A single-provider intersection is a measurement; a range across independent providers is a
finding. Where providers agree (`[1, 1]` above) the number is far stronger than any one run.
Where they disagree, **quote the range** — `|A n B| in [lo, hi]` — rather than picking the
provider that flatters the claim. Where only one answers, say so and say why the others did not:
a spent budget, a coverage hole and a biomedical denominator are three different reasons and
only one of them is about the literature.

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
- **`/citations/<doi>` returns records with an empty `citing` field — the phantom co-citer.**
  De-duplicating `row["citing"]` without filtering puts a single blank key `""` into the set. That
  key is in *every* set built the same way, so it inflates `N_A`, `N_B` **and every intersection by
  exactly 1** — and an intersection of 1 is exactly the size at which a gap claim turns into a
  bridge claim. Measured 2026-09-05: Scheffer 2009 3,999 records → 65 blanks → 3,934 unique;
  Hanley & McNeil 1982 19,229 → 713 → 18,516; Catling 2018 201 → 14 → 187. Some sets carry none
  (Barlow & Hunter 1960: 0 of 1,131), so a run that looks clean on one anchor is not evidence the
  trap is absent on another. `vault/_scripts/intersect.py` drops blank and whitespace-only `citing`
  (and `cited`) keys before building sets, prints how many it dropped per anchor, and has a
  `--selftest` that fetches a known small pair and asserts no blank key survives. **Any count taken
  from a pre-2026-09-05 run of that script, or from any hand-rolled set build, may read one high;
  re-run before quoting it.** First caught in `audits/scout-04-conservation-genetics.md`, where an
  uncorrected pass reported five phantom "1-hit" candidates that are clean zeros.

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
