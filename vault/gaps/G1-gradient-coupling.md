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
computed-in: ["[[C8-momentum-harvesting-metric]]"]
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

## Narrowed again: the momentum branch now has a metric

[[C8-momentum-harvesting-metric]] writes one.

**`Σ ≡ P_useful / (F·Δu)`** — the power the harvester keeps, over the total power leaving the
environment. `F` is the force transmitted between two reservoirs, `Δu` their relative velocity.

It comes from an **exact identity**, no linearity assumed: summing the power each reservoir
delivers in its own frame gives `P_total = −F·Δu`. So **`Σ ∈ [0,1]` by construction**, and it
spans branches the Onsager machinery cannot reach.

**It corrected this note's own premise.** We wrote *"a solar sail has no conjugate flux pair."*
False. The sail's second reservoir is the **radiation field**, `Δu = c`, and `Σ_sail = 2v/c`
falls straight out. `F·Δu` is the standard mechanical dissipation bilinear form — conjugate in
exactly the Onsager sense. We had mistaken *no fuel we recognise* for *no conjugate pair*.

**Independent check:** requiring `Σ_soar ≤ 1` reproduces the soaring literature's minimum-shear
condition `dW/dz ≥ g/((L/D)·V)` from scratch. A metric derived for other reasons landing on a
known result is the strongest validation available here.

## And a precise impossibility, not a fudge

**`Σ` spans both branches. `max Σ` does not.**

`q` exists because in linear response the *maximum* efficiency collapses to a single
state-independent coefficient. A cyclic harvester must return to its initial state, and **the
return cost is not a property of any local point.** So `sup Σ` is a trajectory functional — an
HJB problem — not a coefficient.

That is the honest form of the barrier, and it is more useful than the original claim.

## What it buys, and it answers the founding question

Σ splits the class in two:

| | Example | Lever |
|---|---|---|
| **Kinematic identity** | photon sail `2v/c`, gravity assist | none — only magnitude helps |
| **Trajectory functional** | dynamic soaring, shear sailing | **arrangement is the only lever** |

So *simple arrangement beating brute magnitude* stops being an intuition and becomes a
criterion: **arrangement beats magnitude exactly when the optimum fails to collapse to a
coefficient.** Which is the same property, seen from the other side, that stops `q` from
generalising.

## What would change it

The open problem is now sharp: **does `sup Σ` admit a coefficient representation?** Extending
the degree of coupling past linear response is the same question in the other branch's language.
See [[kedem-caplan]] — which the re-read also corrected.

**Prior-art risk, stated:** Greason's *Wind–Pellet Shear Sailing* (arXiv:2205.14117) states the
sailing↔shear analogy directly. **Abstract only.** It is the single result most likely to demote
C8 to rediscovery, and it has not been read.

## Unverified, stated

Bentien 2013 (*J. Power Sources*) is the source of the explicit "fully equivalent to the
thermoelectric figure-of-merit" sentence and `β = 1.1 ± 0.2`. ScienceDirect 403s.
**UNVERIFIED, and the case above does not rest on it.** Stucki 1980 is bibliographically
confirmed but its abstract was not directly fetched.
