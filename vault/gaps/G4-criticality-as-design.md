---
id: G4
name: G4-criticality-as-design
type: gap
standing: narrowed
evidence: full-text-read
contact-surface: 99
crosses: formalism
crosses-rank: 4
topology: direct
mediator: 
borrows-from: []
lends-to: []
mutual-with: []
computed-in: ["[[C17-offset-from-threshold]]"]
uses-move: ["[[M2-use-the-noise]]"]
rests-on: []
tags: [node/gap, crosses/formalism, evidence/single-review, standing/narrowed]
last-checked: 2026-09-03
note: "Bibliography audited directly: 595 refs, and it carries no titles at all, so prior subject characterisation read data that is not there. Only the offset-from-threshold figure of merit survives."
---

# Criticality as a design strategy

**STANDING: NARROWED** · evidence: full-text-read · contact surface: 99 · last checked 2026-09-03

> Hair cells self-tune to a Hopf bifurcation for divergent gain. Parametric amplifiers are biased just below threshold. Same law, two vocabularies.

## Downgraded

A re-run found **99 papers** linking Hopf bifurcation to the cochlea, plus titles like *Self-tuned
regenerative amplification and the Hopf bifurcation*. The field-level claim is false.

## The bibliography audit finally ran, on the actual PDF

Muñoz, *Rev. Mod. Phys.* 90, 031001 (2018), pulled from
[arXiv:1712.04499](https://arxiv.org/pdf/1712.04499) and extracted, 34 pages.

**The count is 595 references, not 578.** The 578 figure is **UNVERIFIED** and should be treated
as approximate.

**And the bibliography carries no article titles — only venues.** So every previous
subject-keyword characterisation of this reference list was reading data that is not in it.
That is a methodological failure worth more than the entry: *we characterised a bibliography we
had never opened.*

By venue, the honest result is split. Zero laser, MEMS, superconducting, resonator, sensor or
photonic references — that part is **true**. But there are **five IEEE entries**, so *"cites
zero engineering"* is **false as worded**.

More damning: the review cites **Kern & Stoop, PRL 2003** and **Stoop & Gomez, PRL 2016.**
Stoop is the author of the Hopf-bifurcation electronic cochlea **hardware** — and it is his
hardware papers that are omitted. The review cites the person and skips the device. That is a
sharper and stranger finding than a blanket absence.

## And the surviving sentence was refuted too

The note said the offset-from-threshold question was "apparently never asked as one question."
*Sensors* 11:5808 ([PMC3231456](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3231456/fullTextXML)),
read in full, asks it as one question:

> "The aim in the design of natural and artificial sensors is mainly the implementation of
> signal sensitivity... Behaviors of that sort are common in systems close to bifurcations."

Engineering's name for the class is **Lur'e systems** — a term this project never searched.

## The construction: the real invariant is gain × bandwidth, not distance ([[C17-offset-from-threshold]])

The missing "distance from threshold" figure of merit was built — and it is **portable only in a
near-tautological sense.** Define the offset `ε` as the normalized pole-to-axis distance; then
gain diverges as `ε⁻¹` with the *same* exponent `a = 1` across a Hopf resonator (hair cell), a
parametric amplifier (JPA) and a branching process (cortex). But that sameness is empty — the
resolvent of a simple pole is `1/distance` by construction, so any codimension-1 bifurcation
gives `a = 1`. "Shared axis, shared exponent" says only that a simple pole is a simple pole.

**The content is one level down.** Bandwidth is the *same* pole distance, `Δ ∝ ε`, and settling
time is `τ ∝ ε⁻¹`. So

    gain × bandwidth = (c/ε)(rate·ε) = c·rate — independent of ε

**The gain–bandwidth product is conserved along the offset axis in every class.** Sitting closer
to threshold is provably not a free lunch: the `ε⁻¹` gained in gain is exactly the `ε` lost in
bandwidth. That is the portable figure of merit that was hiding under "distance," and its
fingerprint is the parametric-amplifier community's known constant gain–bandwidth product.

So G4's surviving gap **closes onto a real shared invariant** — but the shared thing is
`gain × bandwidth`, not offset. Cortex sitting at `m ≈ 0.98` and an amplifier biased just below
threshold are both spending the *same* conserved budget, and neither field states it in the
other's terms.

## What actually survives

**Only the missing shared figure of merit for offset-from-threshold.** Cortex sits at m ≈ 0.98,
not 1; amplifiers are biased just below. Both fields know to sit near but not at the bifurcation.
Neither has a number that says *how far*, comparable across the two.
