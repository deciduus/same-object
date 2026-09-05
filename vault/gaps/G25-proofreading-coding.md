---
id: G25
name: G25-proofreading-coding
type: gap
standing: narrowed
evidence: citation-intersection
contact-surface: 36
crosses: nothing
crosses-rank: 0
topology: disjoint
mediator: 
borrows-from: []
lends-to: []
mutual-with: []
computed-in: ["[[C3-energy-error-axis]]", "[[information-audit]]"]
uses-move: []
rests-on: []
tags: [node/gap, crosses/nothing, evidence/citation-intersection, standing/narrowed]
last-checked: 2026-09-05
note: "Re-run 2026-09-05 as a citer-set intersection (no reference lists needed, 100% of provider index): OpenAlex 36 co-citers of Hopfield 1974 and Shannon 1948 part I, OpenCitations 8 against part II. The old zero-coding-theory result was a 28.4%-coverage artifact - at least four co-citers carry real coding-theory content. Narrowed, not live."
---

# Kinetic proofreading and coding theory

**STANDING: NARROWED** · evidence: citation-intersection · contact surface: 36 · last checked 2026-09-05

> Both fields quantify **energy paid per unit error suppression**, in kT. They read each other at
> 2.2%, and almost always for *entropy* rather than for the channel coding theorem.
>
> *(Was: "Neither reads the other." Falsified 2026-09-05 by the 100%-coverage re-run below.)*

**The bridge is now an exact ledger entry, not a resemblance: [[information-audit]].** A
proofreading step is measurement-and-discard — the generalized second law run backwards — and
biology's entropy sink is the **released phosphate**, paying the `k ln2` per rejected bit out of
ATP's ~20–28 kT. Toyabe's Maxwell-demon memory-erasure cost and a proofreading cycle's ATP cost
are *the same entry in the same ledger*. That is what this gap has been pointing at.

## Contact surface — measured properly

**Superseded 2026-09-05 by the citer-set re-run below. Kept for the record.** All 1,463 papers
citing Hopfield's 1974 proofreading paper were pulled and their reference lists intersected
against Shannon.

**Coverage is the weak point and is stated up front: 416/1,463 = 28.4%.** [[G6-multifunctionality]]
ran the same instrument at **77.5-100%** coverage, and that is the standard this note does not
meet. A zero at 28.4% is worth less than a zero at 90%; the intersection here is not zero (16)
but the *coding-theory* intersection is, and 71.6% of the citer set was never examined.

| | |
|---|---|
| citers with reference lists available | 416 (**28.4% coverage**) |
| ...also citing Shannon | **16 (3.8%)** |
| ...with "Shannon" in the title | **0** |
| ...mentioning coding theory, channel capacity, LDPC, Hamming | **0 each** |
| `"proofreading" AND "rate-distortion"` | **0** |

The sixteen cite Shannon for *entropy*, never the channel coding theorem.

**The sharpest detail:** 33 papers in the proofreading literature use the word **"decoding."
Every one means the ribosome's A-site.** The vocabulary collides exactly; the formalism never
meets.

## What is specifically absent

The shared axis. Three canonical bounds — 1948, 1961, 2015 — all in kT per nat, differing only
in whether the nat is transmitted, erased, or discarded. Built out in [[C3-energy-error-axis]].

## Why this was called the project's strongest finding — and what the re-run did to it

It is the only gap measured by [[citation-intersection]] at full depth, and it survived
[[failure-modes|synonym re-testing]] intact. **The 2026-09-05 re-run at 100% coverage keeps the
shape and breaks the headline:** the co-citer set is real and small (36 of 1,656 = 2.2%), but
"zero with any coding-theory content" is false. Contrast [[positive-controls]]: DNA data storage
co-cites error-correcting codes at 5.4% and reports results as a fraction of Shannon capacity.
This has none of the closed-gap signature.

## Next probe

The T-cell discrimination literature, where proofreading models and mutual-information
estimates of receptor signalling already coexist.

## Provenance

Anchors:

| Role | Work | DOI | Verified |
|---|---|---|---|
| Proofreading anchor | Hopfield 1974, *PNAS* 71(10):4135 | `10.1073/pnas.71.10.4135` | Crossref, 2026-09-05 |
| Coding anchor | Shannon 1948, *Bell Syst. Tech. J.* | `10.1002/j.1538-7305.1948.tb01338.x` | Crossref, 2026-09-05 |

**Both DOIs resolve to the intended works.** Crossref returned the correct titles and authors for
each (`api.crossref.org/works/<doi>?mailto=...`, 2026-09-05).

Pipeline, as reconstructed:

| Step | Provider | Endpoint | Value |
|---|---|---|---|
| Citers of Hopfield 1974 | **provider not recorded at time of run** | — | 1,463 |
| Reference lists of those citers | **provider not recorded at time of run**; Crossref `api.crossref.org/works/<doi>` is the only route in [[citation-sources]] that returns full reference lists | — | 416 retrieved |
| Coverage | — | — | **416/1,463 = 28.4%** |
| Also citing Shannon | — | — | 16 (3.8% of the 416) |

**Original run date: 2026-09-03** (per `last-checked`). The 1,463 figure's provider was not
logged, and none of the three live counts reproduce it exactly.

### Citer counts re-derived live, 2026-09-05

| Provider | Endpoint | N citers of Hopfield 1974 |
|---|---|---|
| Crossref | `api.crossref.org/works/10.1073/pnas.71.10.4135?mailto=...` (`is-referenced-by-count`) | **1,340** |
| OpenCitations | `api.opencitations.net/index/v1/citation-count/10.1073/pnas.71.10.4135` | **1,593** |
| OpenAlex | `api.openalex.org/works?filter=doi:10.1073/pnas.71.10.4135` (`cited_by_count`, W2074616759) | **1,656** |

Original: **1,463**. Today: 1,340 / 1,593 / 1,656 depending on provider. The spread across
providers (24%) is larger than any plausible 2-day growth, so **1,463 is provider-dependent, not
a fact about the literature.** The 3.8% and the coding-theory zero are computed within the 416
that were actually inspected and do not depend on which denominator is right.

*Note on [[citation-sources]]: `opencitations.net/index/coci/api/v1/` now 301-redirects to
`api.opencitations.net/index/v1/`, and on that host `/citation-count/` no longer returns the
bogus constant `1` — it agreed exactly with a counted `/citations/` list on a second DOI
(Alexander 1997: 40 = 40). Still cross-check before trusting it.*

### The 2026-09-05 re-run: citer-set intersection, 100% coverage

The 2026-09-03 pipeline was a *reference-list* intersection — pull A's citers, fetch each
citer's bibliography, look for B. That second step is what capped coverage at 28.4%. **A citer-set
intersection needs no reference lists at all:** pull the citer DOI set of A, pull the citer DOI
set of B, intersect. Coverage is then 100% of what the provider indexes. Script:
`vault/_scripts/intersect.py`; recipe in [[citation-sources]].

**Provider 1 — OpenAlex, `api.openalex.org/works?filter=cites:W2074616759,cites:W1995875735&mailto=…`, fetched 2026-09-05.**
(OpenAlex evaluates the two-`cites` filter server-side, so this *is* the intersection.)

| | Hopfield 1974 (W2074616759) | Shannon 1948 pt I (W1995875735) | Shannon 1948 pt II (W2041404167) |
|---|---|---|---|
| `cited_by_count`, 2026-09-05 | **1,656** | **82,198** | **9,741** |
| co-citers with Hopfield | — | **36** | **0** |

**Provider 2 — OpenCitations, `api.opencitations.net/index/v1/citations/<doi>`, fetched 2026-09-05.**

| Anchor | N citers |
|---|---|
| Hopfield 1974 `10.1073/pnas.71.10.4135` | **1,542** |
| Shannon 1948 pt II `10.1002/j.1538-7305.1948.tb00917.x` | **9,771** |
| **intersection** | **8** |

**Re-derived on the repaired instrument, 2026-09-05 (FIX1 blank-key re-check).** Re-run with
`_scripts/intersect.py` after the blank-`citing` filter landed: Hopfield **1,542 → 1,542** (51
blank/DOI-less records dropped), Shannon pt II **9,771 → 9,771** (70 dropped), intersection
**8 → 8**, the same eight DOIs. Nothing moved — these figures were already post-filter when
published. **Semantic Scholar has no record for Shannon 1948 pt II
`10.1002/j.1538-7305.1948.tb00917.x`** — a coverage hole, reported as `err` and excluded from the
consensus, never as a zero; it does index Hopfield (1,285 citers after dropping 174 blanks), so
the hole is on the Shannon side only. Standing, evidence and `contact-surface` are unchanged.

**Shannon 1948 part I could not be fetched from OpenCitations at all.**
`api.opencitations.net/index/v1/citations/10.1002/j.1538-7305.1948.tb01338.x` returns
**HTTP 500** (`something unexpected happened - SystemExit: 1 (line 1412)`) after ~3 min 47 s,
2026-09-05 — the citer list is too large for the endpoint. That is a third endpoint trap and is
recorded in [[citation-sources]]. Part II (9,771 citers) returns 200 in ~19 s.

Null model, `N = 1.6×10⁸` (approximate size of the DOI universe): expected co-citers under
independence = 1,542 × 9,771 / 1.6×10⁸ = **0.09**; observed 8 → **observed/expected ≈ 85**. The
overlap is far from accidental. It is also far below a closed gap's signature.

### Every hit was inspected — and the coding-theory zero does not survive

Titles and abstracts were pulled for all 36 OpenAlex hits and all 8 OpenCitations hits
(`api.openalex.org/works/doi:<doi>`, `api.crossref.org/works/<doi>?mailto=…`, 2026-09-05).
Four of the 36 are preprint/published duplicates of two works, so the OpenAlex set is **32
distinct works**; the OpenCitations 8 adds three not in it.

**Contradicting the old result, at least four carry real coding-theory content:**

| DOI | Work | What it actually does |
|---|---|---|
| `10.1016/j.tpb.2019.03.007` | Match fitness landscapes for macromolecular interaction networks, *Theor. Pop. Biol.* 2019 | "We used **results from coding theory** to prove bounds and equalities on fitness … including **proofreading** … Using genotypes based on **extended Hamming codes**". Proofreading kinetics and algebraic coding in one model. **Decisive.** |
| `10.3390/e20050368` | Writing, Proofreading and Editing in Information Theory, *Entropy* 2018 (OpenCitations set) | Builds proofreading and editing as operations on information chains; "underlies any communication system". **Decisive.** |
| `10.1109/memb.2006.1578663` | The quest for error correction in biology, *IEEE EMB Mag.* 2006 | "recent developments in **codes** and biology … applications of **coding and information theory** to biology". |
| `10.3390/e25060881` | Improvement of Error Correction in Nonequilibrium Information Dynamics, *Entropy* 2023 | Error correction on an explicit **memoryless channel model**, with the thermodynamic cost. |

Two more are channel-adjacent rather than coding-theoretic: `10.48550/arxiv.1603.07758` (a
power–precision–speed bound "in any physical communication channel") and
`10.1088/1361-6633/add6b3` (Landauer/thermodynamics-of-computation review that mentions error
correction). The remaining ~26 are what the old note described: Shannon cited for **entropy**
or **mutual information**, never for the channel coding theorem.

### What this changes

| | 2026-09-03 | 2026-09-05 |
|---|---|---|
| instrument | reference-list intersection | **citer-set intersection** |
| coverage | 416/1,463 = **28.4%** | **100%** of provider index |
| intersection | **16** (3.8% of 416) | **36** (2.2% of 1,656) OpenAlex; **8** OpenCitations |
| coding-theory content | **0** | **≥4**, two of them decisive |

The two intersections measure different objects and both are true of their object; the fraction
barely moved (3.8% → 2.2%). **The zero did not survive.** It was a coverage artifact: the works
that do carry coding theory were in the 71.6% never examined.

**Standing changed `live` → `narrowed`, 2026-09-05.** The gap is not overturned — 2.2% co-citation
with four substantive bridges is still far under [[positive-controls]]' closed-gap signature
(DNA data storage co-cites error-correcting codes at 5.4% *and* reports results as a fraction of
Shannon capacity). But "neither field reads the other" is now false as stated, and a `live`
standing cannot carry a claim its own instrument contradicts. Contact surface 16 → **36**
(the OpenAlex number, the one measured at full coverage). `evidence` is unchanged and is now
better supported than before. Logged in [[log]].

### Expected under independence — *added 2026-09-05 from `audits/staged`*

The staged version of this block said `E` was not computable because `|citers(Shannon 1948)|` was
never logged. It is computable now, from the same 2026-09-05 OpenAlex run as the citer-set
re-intersection above: `|citers(Hopfield 1974, W2074616759)| = 1,656`,
`|citers(Shannon 1948 pt I, W1995875735)| = 82,198` (OpenAlex `cited_by_count`, fetched
2026-09-05), `O = 36`.

**`N_universe`, fetched 2026-09-05** — OpenAlex, works in either the proofreading or the
coding-theory concept, from Hopfield's publication year:

```
https://api.openalex.org/works?filter=concepts.id:C170748874|C113709454,
  from_publication_date:1974-01-01,to_publication_date:2026-09-05&per-page=1&mailto=...
meta.count = 8,851
```

(C170748874 Proofreading, C113709454 Coding theory; OpenAlex has no "kinetic proofreading"
concept.) **This fetch fails as a universe, and the failure is itself the result.** `N = 8,851`
is an order of magnitude *smaller* than `|citers(Shannon)| = 82,198`; a universe cannot be
smaller than a subset of itself. Shannon 1948's citer set is not contained in any
proofreading-or-coding-theory scope — it spans most of quantitative science. So for this pair the
concept-scoped route is void and the **union floor is the binding denominator.**

| `N` route | `N` | E | O | **O/E** |
|---|---|---|---|---|
| Concept-scoped fetch | 8,851 | 15,379 | 36 | 0.0023 — **void**, `N < |B|` |
| **Union floor** `|A|+|B|−O` | **83,818** | **1,624** | 36 | **0.022** |
| 10× floor (sensitivity) | 838,180 | 162 | 36 | **0.222** |

**Is the low count a finding?** *Yes, on every valid row.* `E ≫ 1` throughout (1,624 down to 162),
so the 36 is a genuine deficit rather than a small-numbers artifact — and unlike [[G6-multifunctionality]]
this conclusion is insensitive to `N` across an order of magnitude, because the union floor is
already large. The remaining caveat is the one the note already carries: the load-bearing figure
is the *content* of the 36, not the count.

The next probe is unchanged and is now better aimed: `10.1016/j.tpb.2019.03.007` is the closest
thing to the missing shared axis that exists, and it is a fitness-landscape paper, not an
energy-per-error one.
