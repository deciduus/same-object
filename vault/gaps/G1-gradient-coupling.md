---
id: G1
name: G1-gradient-coupling
type: gap
standing: narrowed
evidence: full-text-read
contact-surface: 2
crosses: formalism
crosses-rank: 4
topology: direct
mediator: 
borrows-from: []
lends-to: []
mutual-with: []
computed-in: []
uses-move: ["[[M5-work-inside-the-noise]]"]
rests-on: ["[[kedem-caplan]]"]
tags: [node/gap, crosses/formalism, evidence/full-text-read, standing/narrowed]
last-checked: 2026-09-03
note: "Thermodynamic branch is already unified: the ZT-form q is in active use for thermoelectric, electrokinetic, hydronic and oxphos. Gap survives only across the momentum branch."
---

# Gradient coupling has no shared figure of merit

**STANDING: NARROWED** · evidence: full-text-read · contact surface: 2 · last checked 2026-09-03

> The claim split in half when read. **The thermodynamic branch is already unified and in
> active use.** What survives is the gap between that branch and momentum/field-gradient
> harvesting — soaring, sails, tethers — which the Onsager machinery cannot reach.

## What the re-read overturned

Two sub-claims were false. Both were string artifacts.

**"Chemiosmosis sits on a third, biochemical island" — false.** Chimal-Eguia et al.,
*Entropy* 25(12):1575 (2023), [PMC10743106](https://pmc.ncbi.nlm.nih.gov/articles/PMC10743106/),
read in full, handles thermoelectric generators **and** oxidative phosphorylation in one
framework and writes the identity out:

> "where q = L₁₂²/(L₁₁L₂₂) is the degree of coupling (it is worth mentioning that the value of
> q is related to what, in thermoelectricity, we call the figure of merit (Z))"

It cites Kedem & Caplan 1965 directly. It does not print the closed form `q² = ZT/(1+ZT)`,
but the connection is stated, not latent.

**"thermoelectric and osmotic: 2" understates the relationship in kind, not degree.**
Electrokinetic energy conversion has its own figure of merit of the same algebraic shape,
[PMC5712061](https://pmc.ncbi.nlm.nih.gov/articles/PMC5712061/) Eq. 17, read in full:

> "β = K₁₃²/(K₁₁K₃₃ − K₁₃²) = σ·υ²/κH"

That is the Onsager off-diagonal-squared-over-product form — the same object as `q²/(1−q²)` —
and it traces to **Morrison & Osterle 1965**, the same year as Kedem & Caplan. Two
contemporaneous derivations of one structure is **parallel derivation**, not disjointness.
Two co-citers measured the traffic between them and missed that they are the same result.

**And the template is still spreading.** arXiv:[2403.20209v2](https://arxiv.org/html/2403.20209v2),
read in full, builds a hydronic figure of merit:

> "This definition of the hydronic figure of merit is inspired by its thermoelectric analogue."

> "in contrast to its thermoelectric analogue, this figure of merit combines independently
> tunable parameters of the solid and the liquid, and can thus significantly exceed unity"

So: thermoelectric, electrokinetic/osmotic, hydronic and chemiosmotic are **one literature
with one figure of merit.** Not a gap.

## What survives, and survives cleanly

**The momentum / field-gradient branch is untouched by any of it.** Dynamic soaring, solar
sails and tethers extract work from a gradient and share no figure of merit with the
thermodynamic branch — or with each other. A targeted search surfaced no candidate framework
at all. Linear-response Onsager machinery cannot reach them: soaring is nonlinear and
trajectory-dependent, and a solar sail has no conjugate flux pair.

This half remains **string-protocol**, not full-text-read. No soaring papers were read in full.

## What would change it

Unchanged, and now better located: extend the degree of coupling past linear response. Genuine
open research. See [[kedem-caplan]] — which the re-read also corrected.

## Unverified, stated

Bentien 2013 (*J. Power Sources*) is the source of the explicit "fully equivalent to the
thermoelectric figure-of-merit" sentence and `β = 1.1 ± 0.2`. ScienceDirect 403s.
**UNVERIFIED, and the case above does not rest on it.** Stucki 1980 is bibliographically
confirmed but its abstract was not directly fetched.
