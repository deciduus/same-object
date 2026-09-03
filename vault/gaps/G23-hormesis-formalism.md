---
id: G23
name: G23-hormesis-formalism
type: gap
standing: narrowed
evidence: full-text-read
contact-surface: 0
crosses: vocabulary
crosses-rank: 3
topology: disjoint
mediator: 
borrows-from: []
lends-to: []
mutual-with: []
computed-in: ["[[C19-hormesis-biphasic-fit]]"]
uses-move: ["[[M2-use-the-noise]]"]
rests-on: []
tags: [node/gap, crosses/vocabulary, evidence/full-text-read, standing/narrowed]
last-checked: 2026-09-03
note: "Headline sentence false: shot peening names its own descending limb (over-peening). What survives is the parameterised curve - no ceiling amplitude, no window width, no sweep."
---

# Hormesis has no engineering formalism

**STANDING: NARROWED** · evidence: full-text-read · contact surface: 0 · last checked 2026-09-03

> Engineering **does** know the dose-response turns over — it has a name for the descending
> limb. What it does not have is the **curve**: no ceiling amplitude, no window width, no
> force sweep.

## The headline sentence was false

The note said *"stress-strengthening materials exist; nobody has written a dose-response curve
for one."* The first half of that is wrong. Shot peening names its own non-monotonicity, in one
of the note's own keywords.

[PMC8586029](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8586029/fullTextXML)
(*Sci Rep* 2021), read in full:

> "by using higher intensities and coverages than the ones considered in SSP, over shot peening
> (OSP) phenomenon appears"

> "These defects have high detrimental effects on mechanical properties of the SP treated
> material, often leading to fatigue strength reduction."

Corroborated independently in
[PMC7579628](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7579628/fullTextXML)
(*Materials* 2020):

> "commonly called as over peening effect which may cause the formation of microcracks and
> delamination on the surface"

with a stated optimum at **≤5 min for S60 shots**. That is a stimulatory window with a turnover
into damage — a biphasic dose-response, discovered and named independently. Engineering has the
*shape*.

## The curve was fitted, and the two missing numbers now exist: [[C19-hormesis-biphasic-fit]]

The deliverable G23 said was absent — a **parameterised** biphasic curve with a ceiling and a
window — was extracted from published shot-peening dose sweeps.

| Number | Engineering (fitted) | Biology (toxicology) |
|---|---|---|
| **Window width** | **≥15× measured, ~73× fitted** | 10–20× |
| **Amplitude ceiling** (fatigue *strength*) | +20–80% (AA 7075: **+82%** verified) | 30–60% |
| Amplitude ceiling (fatigue *life*) | +400–800% | — |

**The window width is the strong bridge** — engineering lands on the same decade scale as
biology, arrived at independently. The ceiling **overlaps biology only when the response axis is
matched** to a direct strength measure; raw fatigue-*life* gains are an order of magnitude larger,
and the **Basquin exponent (`N ∝ σ⁻¹⁰`) is the translation rule** between strength and life —
structurally the same amplification by which a small physiological gain becomes a large lifespan
gain in organismal hormesis.

**Verdict: narrows strongly toward partial closure.** The parameterised curve now exists and,
matched on axis, transfers into biology's regime. It does *not* fully close — two materials gave
two ceilings, no single theorem fixing a shared figure of merit (per [[what-closes-a-gap]]). And
a real mechanistic difference surfaced: shot peening's descending limb is surface **damage**
competing against a *monotone* residual-stress benefit — the beneficial variable never itself
peaks — so the engineering window is wider and shallower than a toxicological one.

## What survives, and it is the sharper half

**No parameterised biphasic formalism.** Nobody states a ceiling amplitude or a window width.
The optimum is reported as an operating recommendation, not as a curve with fitted constants.
Biology's importable numbers — the ~30–60% amplitude ceiling and the 10–20× window width —
have no engineering counterpart.

**And on the molecular side the original claim is intact.** Ramirez / Craig 2013,
[PMC3896090](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3896090/fullTextXML), read in
full — the mechanochemical self-strengthening work — reports a **single operating point.** No
force sweep. No curve. A field demonstrating stress-induced strengthening never varied the dose.

That is [[M6-vary-what-was-held-fixed]] pointing at an experiment nobody ran, which is a better
gap than a missing literature.

## Restated

*Engineering has the biphasic phenomenon and names its descending limb, but nowhere
parameterises the curve — no ceiling, no window width, no dose sweep — while toxicology has had
the quantified dose-response for decades.*

## Unchanged

Both sides calibrate strongly — hormesis 901, mechanophore 547 — which is what makes the zero
contact surface mean something. Honest note carried forward: hormesis is genuinely contested in
regulatory toxicology.
