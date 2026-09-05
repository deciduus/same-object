---
id: G31
name: G31-biosignature-diagnostic-theory
type: gap
standing: live
evidence: citation-intersection
contact-surface: 0
crosses: formalism
crosses-rank: 4
topology: disjoint
mediator: 
borrows-from: ["[[citation-intersection]]", "[[failure-modes]]", "[[specification-instruments]]"]
lends-to: []
mutual-with: []
computed-in: ["[[C28-biosignature-roc]]"]
uses-move: []
rests-on: []
tags: [node/gap, crosses/formalism, evidence/citation-intersection, standing/live]
exit: computation
extends-to: [astrobiology]
next-step-cost: S
last-checked: 2026-09-05
note: "Biosignature assessment computes P(life|signal) from P(signal|life), P(signal|no life) and a prior, and never once cites diagnostic-test theory, which has computed the identical object as positive predictive value since 1982. Two independent anchor pairs, two providers, intersection 0; astro-native Bayes control fires at 4. Re-run 2026-09-05 with the blank-key-filtering intersect.py: Catling 188 to 187, Schwieterman 496 to 495, Kass 11,867 to 11,866, every intersection unchanged, standing unchanged."
---

# Biosignature assessment × diagnostic-test theory

**STANDING: LIVE** · evidence: citation-intersection · contact surface: 0 · last checked 2026-09-05

> **Astrobiology and clinical epidemiology compute the same three numbers and share no
> citations.** Exoplanet biosignature assessment asks: given a spectral feature, how likely is
> it that life produced it? It answers with a Bayesian network over an enumerated list of
> *false-positive scenarios*, and reports an ordinal *confidence level* (the CoLD scale).
> Diagnostic-test theory has computed the identical quantity since the 1970s under the name
> **positive predictive value**, assembled from **sensitivity**, **specificity** and
> **prevalence**, with an operating-point curve (**ROC**) and a **likelihood ratio** attached.
> The two vocabularies map term-for-term. The citation graph between them is empty: across
> **565** citers of two astrobiology framework anchors and **32,176** citers of four diagnostic
> anchors spanning 1982–2011, the intersection is **0**.

## The two vocabularies, aligned

| Astrobiology | Diagnostics | The object |
|---|---|---|
| Signature detected above threshold | Test positive | The observable |
| Life present on the planet | "Disease" present | The latent state |
| False-positive scenario (abiotic O₂ route) | 1 − specificity | P(signal \| no life) |
| False negative (O₂ suppressed by sinks; Meadows 2018 §"false negatives") | 1 − sensitivity | P(no signal \| life) |
| *(no term)* | Prevalence / base rate | P(life) over the observed sample |
| Bayesian model comparison, Bayes factor | Positive likelihood ratio `LR+ = sens/(1−spec)` | The evidence multiplier |
| CoLD level 1–7 (ordinal) | Positive predictive value (a probability) | P(life \| signal) |
| *(no term)* | ROC curve, AUC | The threshold trade-off |

The row with *(no term)* on the left twice is the finding. Astrobiology has the numerator and
one of the two denominator legs. It has no base-rate term at all, and no notion of an operating
point. What it reports as a *confidence level* is an ordinal grade where diagnostics reports a
probability — and the probability cannot be formed without the missing row.

## Provenance

**Taken verbatim from `audits/scout-03-astrobiology.md` (2026-09-05, Job 2 candidate G-E) as the
starting measurement**, then re-run independently here on a second provider and a second anchor
pair. The audit's row:

| Field | Value |
|---|---|
| Anchor A | Catling, Krissansen-Totton, Kiang et al. 2018, *Exoplanet Biosignatures: A Framework for Their Assessment*, `10.1089/ast.2017.1737` |
| Anchor B | Hanley & McNeil 1982, *The meaning and use of the area under a receiver operating characteristic (ROC) curve*, `10.1148/radiology.143.1.7063747` |
| Provider / endpoint | OpenAlex, `works?filter=cites:W2949593113,cites:W2157825442&per-page=1` |
| Date | 2026-09-05 |
| N_A, N_B | 215, 21,924 |
| **∩** | **0** |
| Union floor `N` | 22,139 → `E = 212.9` |
| Fetched `N` | **152,971** — `concepts.id:C163479331\|C58471807,from_publication_date:2018-01-01` → `E = 30.8` |
| Control | Catling 2018 × Kass & Raftery 1995 `10.1080/01621459.1995.10476572` = **4**; all four inspected, all astro-native Bayesian model comparison |

**DOIs re-resolved through Crossref** (`api.crossref.org/works/<doi>?mailto=deciduusleaf@gmail.com`),
**2026-09-05**, all five live, `is-referenced-by-count` as of that fetch:

| DOI | Title | Venue, year | Crossref cited-by |
|---|---|---|---|
| `10.1089/ast.2017.1737` | Exoplanet Biosignatures: A Framework for Their Assessment (Catling et al.) | Astrobiology 2018 | 202 |
| `10.1089/ast.2017.1729` | Exoplanet Biosignatures: A Review of Remotely Detectable Signs of Life (Schwieterman et al.) | Astrobiology 2018 | 514 |
| `10.1089/ast.2017.1727` | Understanding Oxygen as a Biosignature in the Context of Its Environment (Meadows et al.) | Astrobiology 2018 | 301 |
| `10.1148/radiology.143.1.7063747` | The meaning and use of the area under an ROC curve (Hanley & McNeil) | Radiology 1982 | 17,581 |
| `10.1136/bmj.308.6943.1552` | Statistics Notes: Diagnostic tests 1: sensitivity and specificity (Altman & Bland) | BMJ 1994 | 1,652 |

**The OpenAlex re-run could not be made.** The `cites:W_A,cites:W_B` filter query was issued on
2026-09-05 and returned `{"error":"Rate limit exceeded", ... "dailyRemainingUsd":0}` — the daily
budget on this key was exhausted before the intersection calls. Work IDs and `cited_by_count`
were fetched before exhaustion (Catling **W2949593113** 213; Schwieterman **W2616637335** 522;
Hanley & McNeil **W2157825442** 22,114; Altman & Bland **W1644997609** 2,083; Kass & Raftery
**W4211177544** 12,519), so the filter string above is recorded but **its result on this date is
the audit's, not a fresh fetch.** The independent re-run below used a different provider instead.

## Second anchor pair, second provider

A single anchor pair measures one pair of papers, not two literatures. Guard run:

- **A′** Schwieterman et al. 2018, `10.1089/ast.2017.1729` — the companion *review* of remotely
  detectable signs of life, chosen because it is four times more cited than Catling and is the
  paper an outsider would read first.
- **B′** Altman & Bland 1994, `10.1136/bmj.308.6943.1552` — chosen because it is the opposite
  kind of paper from Hanley & McNeil: a one-page BMJ statistics note, maximally citable, no ROC
  machinery, just the two conditional probabilities. If the zero were an artifact of Hanley &
  McNeil being a *Radiology* methods paper, a BMJ note would leak.

**Provider: OpenCitations**, `api.opencitations.net/index/v1/citations/<doi>` (the
`opencitations.net/index/api/v1/...` path 301-redirects; follow it — see [[citation-sources]]),
citer lists intersected as lower-cased DOI sets, fetched **2026-09-05**.

**The blank-key filter, corrected and re-run 2026-09-05.** OpenCitations returns records with an
empty `citing` field; a set built without filtering carries a phantom `""` that is shared by every
set and so inflates `|A|`, `|B|` **and every intersection by exactly 1** (see [[citation-sources]]).
The note's earlier sentence "one malformed empty-string value appears in every set" was wrong in
both directions: **every** one of these seven anchors carries blanks, and there are many per
anchor, not one — and three of the published `|A|`/`|B|` figures were **pre**-filter while the
intersections were post-filter, so the note was mixing bases. Re-run with the repaired
`_scripts/intersect.py`, raw records → blanks dropped → unique citers:

| Anchor | raw records | blank `citing` dropped | **unique citers** | as previously published |
|---|---|---|---|---|
| Catling 2018 | 201 | 14 | **187** | 188 — one high |
| Schwieterman 2018 | 544 | 49 | **495** | 496 — one high |
| Hanley & McNeil 1982 | 19,229 | 713 | **18,516** | 18,516 ✓ |
| Altman & Bland 1994 | 1,770 | 52 | **1,718** | 1,718 ✓ |
| Deeks 2001 | 1,023 | 47 | **976** | 976 ✓ |
| Whiting 2011 (QUADAS-2) | 11,580 | 237 | **11,343** | 11,343 ✓ |
| Kass & Raftery 1995 | 12,224 | 358 | **11,866** | 11,867 — one high |

**No intersection moves.** All eight gap pairings were 0 and remain 0; the controls were 4 and 2
and remain 4 and 2, on the same DOIs. Unfiltered, every one of those ten rows would have read one
higher — eight phantom "bridges" where there are none, which is exactly the failure this gap would
have been destroyed by. `standing: live`, `contact-surface: 0`, `evidence: citation-intersection`
and the tags are unchanged.

| Pair | \|A\| | \|B\| | **∩** |
|---|---|---|---|
| Catling 2018 × Hanley & McNeil 1982 | 187 | 18,516 | **0** |
| Catling 2018 × Altman & Bland 1994 | 187 | 1,718 | **0** |
| **Schwieterman 2018 × Hanley & McNeil 1982** | 495 | 18,516 | **0** |
| **Schwieterman 2018 × Altman & Bland 1994** | 495 | 1,718 | **0** |
| Catling 2018 × Deeks 2001 `10.1136/bmj.323.7305.157` | 187 | 976 | **0** |
| Catling 2018 × Whiting 2011 (QUADAS-2) `10.7326/0003-4819-155-8-201110180-00009` | 187 | 11,343 | **0** |
| Schwieterman 2018 × Deeks 2001 | 495 | 976 | **0** |
| Schwieterman 2018 × QUADAS-2 | 495 | 11,343 | **0** |
| **Pooled: (Catling ∪ Schwieterman) × (all four diagnostic anchors)** | **565** | **32,176** | **0** |
| *Control:* Catling 2018 × Kass & Raftery 1995 | 187 | 11,866 | **4** |
| *Control:* Schwieterman 2018 × Kass & Raftery 1995 | 495 | 11,866 | **2** |

**The control reproduces the audit exactly, on a different provider.** The four Catling ×
Kass & Raftery hits are the same four DOIs OpenAlex returned: `10.1089/ast.2019.2151`,
`10.3847/1538-3881/ad0cbe`, `10.3847/1538-3881/ada384`, `10.1093/mnras/stad2822`. Two providers,
same four works. That is the pipeline demonstrating it can detect a co-citation event of exactly
this kind when one occurs — the [[positive-controls]] requirement.

### Expected under independence

`E = |A|·|B|/N`, per [[citation-intersection]]. Denominators: the union floor (a floor, which
flatters the claim and is never quoted alone), the audit's fetched concept-scoped
`N = 152,971`, and 10× that as the mandatory sensitivity row.

| Pairing | union floor | `E` @ floor | `E` @ 152,971 | `E` @ 1,529,710 |
|---|---|---|---|---|
| Catling × Hanley (OpenCitations) | 18,703 | 185.1 | **22.6** | 2.26 |
| Catling × Hanley (OpenAlex, audit) | 22,139 | 212.9 | **30.8** | 3.08 |
| Schwieterman × Altman | 2,213 | 384.2 | **5.56** | 0.56 — *uninformative* |
| **Pooled astro × pooled diagnostics** | 32,741 | 555.3 | **118.8** | **11.9** |

`O = 0` on every row, so `O/E = 0` wherever `E > 1`. The single second-anchor pairing
(Schwieterman × Altman) **dies at 10×** — `E = 0.56`, fewer than one co-citer expected anyway,
which is precisely the [[G6-multifunctionality]] lesson. The **pooled** row is the one that
carries the claim: `E = 11.9` even at a denominator ten times the audit's, so the zero is a
finding across an order of magnitude of `N`. Report the pooled row or report nothing.

The denominator-invariant statistic, per [[citation-intersection]]:
`(O/|B|)_control = 4/11,866 = 3.4×10⁻⁴` against `(O/|B|)_gap = 0/32,176 = 0`. The ratio is
formally infinite, which is **less** impressive than it looks and is stated here as a weakness:
an infinite ratio only says the gap side is exactly zero, and it cannot be compared with G28's
finite 62.5.

## Hits inspected

**The gap side has no hits.** ∩ = 0 across eight pairings, so there is nothing to inspect and
the finding cannot be softened by a "the co-citers were irrelevant anyway" reading — nor
strengthened by one.

**All six control hits — five distinct works — were inspected** (titles from Crossref, same fetch):

| DOI | What it is | Diagnostic-test content? |
|---|---|---|
| `10.1089/ast.2019.2151` | *Evaluating Biosignatures for Life Detection* | No — astro-native Bayesian model comparison |
| `10.3847/1538-3881/ad0cbe` | *Deconstructing Alien Hunting* | No — nested-sampling model selection |
| `10.3847/1538-3881/ada384` | interior convection / predicted CO₂ | No |
| `10.1093/mnras/stad2822` | Twinkle / LTT 1445 Ab | No |
| `10.1073/pnas.1921655117` | Schwieterman-side control hit | No |

(Schwieterman's second control hit is `10.3847/1538-3881/ad0cbe`, already listed — five distinct works across the six hits.)

Five works that reach *outside* their field for inference machinery, and every one of them
reaches for the astro-native Bayesian canon. **None reaches for sensitivity, specificity,
prevalence, ROC or predictive value.** That is the substantive confirmation: the boundary is not
"this literature never imports statistics", it is "this literature imports one statistics and
not the other."

## Decade-binned re-run — [[failure-modes]] mode 6

A citer window is decades wide and a vocabulary is not. Two bins were needed, one per side.

**B side — the diagnostic vocabulary, binned by the decade that named it.** The four B anchors
above are deliberately one per era: **1982** ROC/AUC (Hanley & McNeil), **1994**
sensitivity/specificity (Altman & Bland), **2001** diagnostic-accuracy systematic review (Deeks),
**2011** QUADAS-2 (Whiting et al., the current reporting standard). The zero holds under all
four names. This is the mode-6 requirement discharged on the side where it bites: the concept
did travel across decades and did change its wording, and the astrobiology literature cites
none of its aliases.

**A side — binned by the publication year of the citing work.** Both astro anchors are 2018, so
their citer window is short, but the bins were run anyway:

| Citing-work bin | astro citers | ∩ with pooled diagnostic canon |
|---|---|---|
| 2010s (2018–2019) | 87 | **0** |
| 2020s (2020–2026) | 465 | **0** |
| no creation date in the OpenCitations record | 13 | **0** |

A pooled zero across a multi-decade window is six measurements, not one. Here it is seven, and
every one of them is zero.

**The failure mode this does not clear.** Neither the ROC literature nor the astrobiology
literature is anchored on a proper noun in the *query* — the queries are DOI-anchored citation
sets, not strings — so modes 1–5 do not apply. What remains is the risk named in the audit and
restated below: a **citation-community boundary** rather than a conceptual absence.

## What survives — and the risk that is still open

**Metaphor risk: MODERATE, and specifically the risk of a vocabulary artifact.** Astronomers do
Bayesian inference constantly; they cite Trotta, Skilling, `MultiNest`, Kass & Raftery — not
*Radiology* and not the *BMJ*. A zero against a clinical canon may measure which journals a
field reads.

What bears against that reading, in order of strength:

1. **The control is 4 and 2, not 400.** Even the astro-native model-comparison canon is barely
   read by these citer sets. The gap is not that this literature ignores *clinical* statistics;
   it barely imports *any* named inference canon.
2. **Four B-side anchors across four decades and two journals** (Radiology, BMJ ×2, Annals of
   Internal Medicine), including a one-page note with 1,652 Crossref citations that requires no
   methodological commitment to cite. All zero.
3. **The missing term is not a citation, it is a number.** [[C28-biosignature-roc]] is the test:
   if the framework had the base-rate concept under a different name, someone would have written
   a prevalence down. Nobody has.

**What would still overturn it:** a single work in either citer set that states a numerical
prior on the fraction of planets bearing life *and* uses it to convert a detection into a
posterior probability, or that names an operating point / threshold trade-off. The reading of
the 565 citers has **not** been done; it is the M-cost step and it is why this note's `exit` is
`computation`, not `experiment`.

## What would close it

Three steps, in cost order. The first is done.

1. **Done — build the missing object.** Express one published biosignature (O₂) as a diagnostic
   test and compute PPV over prevalence × specificity, since the field publishes neither number.
   [[C28-biosignature-roc]]. Result: at the field's own enumeration, a detection is more likely
   true than false only above a break-even prevalence set entirely by specificity, and the
   specificity required at a plausible prevalence of 10⁻³ is **≥ 0.999**.
2. **Read the 565 citers for a number.** Any numeric base rate, any stated operating point. A
   single hit narrows this note; a clean zero across 565 works moves the evidence grade from
   `citation-intersection` to `full-text-read` and makes the claim ordinal-vs-probability rather
   than merely uncited.
3. **Put a real specificity on one case.** The one biosignature case with a published,
   near-exhaustive abiotic-source enumeration is Venus phosphine (Bains et al. 2021,
   `10.1089/ast.2020.2352`) — the target of the parallel reservoir audit, [[C30-venus-phosphine-audit]].
   An enumeration with flux bounds per route is exactly the object that a specificity estimate
   would be built from, which is why the two threads meet there and not on O₂.

The relationship along [[relationship-description]]: astrobiology **borrows** a complete,
century-old formalism it has not touched; diagnostics gets nothing back. The direction is
one-way and the contact surface is 0.
