---
id: G25
name: G25-proofreading-coding
type: gap
standing: live
evidence: citation-intersection
contact-surface: 16
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
tags: [node/gap, crosses/nothing, evidence/citation-intersection, standing/live]
last-checked: 2026-09-03
note: "1,463 citers pulled, 416 reference lists retrieved - 28.4% coverage, well below the 77-100% standard set by G6. The project's strongest finding, on the thinnest coverage."
---

# Kinetic proofreading and coding theory

**STANDING: LIVE** · evidence: citation-intersection · contact surface: 16 · last checked 2026-09-03

> Both fields quantify **energy paid per unit error suppression**, in kT. Neither reads the other.

**The bridge is now an exact ledger entry, not a resemblance: [[information-audit]].** A
proofreading step is measurement-and-discard — the generalized second law run backwards — and
biology's entropy sink is the **released phosphate**, paying the `k ln2` per rejected bit out of
ATP's ~20–28 kT. Toyabe's Maxwell-demon memory-erasure cost and a proofreading cycle's ATP cost
are *the same entry in the same ledger*. That is what this gap has been pointing at.

## Contact surface — measured properly

All 1,463 papers citing Hopfield's 1974 proofreading paper were pulled and their reference
lists intersected against Shannon.

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

## Why this is the project's strongest finding

It is the only gap measured by [[citation-intersection]] at full depth, and it survived
[[failure-modes|synonym re-testing]] intact. Contrast [[positive-controls]]: DNA data storage
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
