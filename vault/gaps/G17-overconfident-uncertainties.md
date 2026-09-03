---
id: G17
name: G17-overconfident-uncertainties
type: gap
standing: narrowed
evidence: citation-intersection
contact-surface: 279
crosses: vocabulary
crosses-rank: 3
topology: mediated
mediator: [[G9-discrepancy-base-rate]]
borrows-from: []
lends-to: ["[[fine-structure-discrepancy]]"]
mutual-with: []
computed-in: []
uses-move: []
rests-on: []
tags: [node/gap, crosses/vocabulary, evidence/citation-intersection, standing/narrowed]
last-checked: 2026-09-03
note: "Restored with correction. A citation is not a follow-up. Specimen case for the symmetry rule."
---

# Reported uncertainties in physical constants are overconfident

**STANDING: NARROWED** · evidence: citation-intersection · contact surface: 279 · last checked 2026-09-03

> Successive recommended values for fundamental constants routinely fall outside the
> previous value's stated error bar. The 1986 paper connects this explicitly to the
> psychology of overconfidence in subjective probability.

## What happened to this entry

**Withdrawn, then restored with a correction.** The withdrawal counted **279 citations** and
called that refutation of "essentially never followed up."

That was the error the [[relationship-description]] symmetry rule now forbids: *a citation
is not a follow-up.* The correct question is how many engage the **specific claim** — that
uncertainties in physical constants are systematically underestimated — and the answer is
roughly **six across forty years.**

The finding is real. Its original phrasing was too absolute.

## Contact surface

279 citing works. Composition matters more than the count:

- **The bulk** are risk analysis and expert elicitation — the paper travelled into decision
  science, where overconfidence was already a live topic.
- **Roughly six** are physics or metrology, engaging the actual claim:
  - Bailey, *Not Normal: the uncertainties of scientific measurements*, R. Soc. Open Sci.
    (2016) — the direct quantitative follow-up. Analyses repeated-measurement datasets of
    physical constants and finds the errors are **heavy-tailed, not Gaussian**.
  - *Blind Analysis as a Correction for Confirmatory Bias in Physics and in Psychology* (2015)
  - *Assessing accuracy in measurement: the dilemma of safety versus precision in the
    adjustment of the fundamental physical constants* (2019)
  - *Escape from Zanzibar: The Epistemic Value of Precision in Measurement* (2022)

## What crosses

**Vocabulary, outward only.** Decision science took the overconfidence framing and ran with
it. Metrology kept adjusting constants.

## Direction

**One-way, and outward.** The paper is heavily cited *away from* the field it was about.
Physics did not absorb its own critique; risk analysis did.

## What is specifically absent

Not "follow-up." **A standing practice.** Nobody re-runs the Henrion–Fischhoff analysis on
each new CODATA cycle, though the data to do it is published every four years and the method
is forty years old.

Related live evidence: [[fine-structure-discrepancy]] — two atom-interferometry measurements
of the same quantity, same technique class, disagreeing at **5.4 sigma**.

## What would change it

Recompute it. Every CODATA adjustment publishes the inputs. Asking *how often did the new
recommended value fall outside the old error bar* is arithmetic on public data, and it has
apparently been done once, in 1986.

Connects directly to [[G9-discrepancy-base-rate]], which is the same question asked about
discrepancies rather than about error bars.

## Methodological note

**String queries returned near-zero** (`"overconfidence" AND ("CODATA" OR "metrology")` = 2)
while the citation graph returned 279. Same claim, same day, opposite answers.

This is the specimen case for [[citation-intersection]] over string matching — and, in the
same breath, for why a raw citation count is not a reading. Both instruments failed here, in
opposite directions.
