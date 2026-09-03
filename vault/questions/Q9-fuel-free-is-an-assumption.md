---
name: Q9-fuel-free-is-an-assumption
type: question
arises-from: ["[[C8-momentum-harvesting-metric]]", "[[G1-gradient-coupling]]"]
status: open
---

# "Fuel-free" names our ignorance, not the physics

> Absence of what we recognise as fuel is not absence of a reservoir. **This project made
> exactly that error and it was caught by its own derivation.**

## The worked example is ours

[[G1-gradient-coupling]] stated flatly that **a solar sail has no conjugate flux pair.** It was
written as a physical fact and it is false. The sail's second reservoir is the **radiation
field**, with `Δu = c`. Once that is named, `Σ_sail = 2v/c` falls out in one line, and the
pairing is conjugate in the ordinary Onsager sense.

Nothing was missing from the physics. **What was missing was the identification of the
reservoir**, and because no fuel was carried aboard, we recorded a gap in nature instead of a
gap in our bookkeeping.

## Why this makes Σ more than a scorecard

`Σ ≡ P_useful / (F·Δu)` is bounded in `[0,1]` **by construction**, from an exact identity — not
by assumption, not by linearity, not by any model of the mechanism. That has a consequence the
derivation did not set out to produce:

> **A measured Σ greater than 1 is not evidence of impossible physics. It is proof that a
> reservoir has been misidentified.**

## Correction: Σ alone is too weak, and [[reservoir-audit]] found out why

**True but nearly useless on its own.** `Σ = P_useful/(F·Δu)` reduces to `v/Δu`, so `Σ ≤ 1` is
automatic for any device slower than its reservoirs' relative velocity. **Σ would have cleared
solar radiation pressure as the source of the Pioneer anomaly** — a candidate that is in fact
excluded by a factor of nearly seven.

The test that actually does the work is a **second leg the identity implies but this note did
not name**: the availability ratio

`A = (F_required · Δu) / P_available`

Every exclusion in the validated audit is an `A` result, not a `Σ` result. A third signature
also appeared: misidentification can surface as a **negative Δu** rather than as `Σ > 1`.

**And one claim below is wrong.** "Electrodynamic tether → planetary rotation" holds only above
geosynchronous orbit. **For every tether actually flown, the orbit is the net source and the
planet's rotation is a sink.** Caught by exactly the mechanism this note is about — being forced
to write a *number* for `Δu` where a *word* had been standing.

So Σ inverts into a **detector**. Point it at any device that appears to produce useful work
without carried fuel, and it returns one of three verdicts:

| Result | Means |
|---|---|
| `Σ ≤ 1` with a named `F` and `Δu` | ordinary harvesting; the reservoir is identified and the efficiency is measured |
| `Σ > 1` | **an unidentified reservoir**, or a measurement error. Those two, and nothing else |
| No `F·Δu` can be constructed | the device is not exchanging momentum with anything we can name — which is a *statement about our model*, not about the device |

The third row is the honest home for the reports that started this project. It replaces
*"impossible"* with *"we cannot name the second reservoir"*, which is a checkable claim rather
than a dismissal.

## The question

**Can Σ be applied to a reported anomalous device as a reservoir audit rather than a verdict?**

The procedure would be: take the reported output power, enumerate every candidate reservoir the
device is in contact with, and for each compute the `Δu` and the `F` that would be required.
Then ask what `Σ` each candidate implies. Reservoirs implying `Σ > 1` are ruled out as the
source. **Whatever remains is the specification of what the second reservoir would have to be** —
a mass, a field, a flow, with a required relative velocity and coupling force.

That is [[M6-vary-what-was-held-fixed]] applied to bookkeeping instead of to a bound. It also
matches the discipline in `claims-register.html`: *testimony sets the specification, never the
mechanism.*

## Why this is not special pleading

The same audit, run on things we already understand, has to reproduce known answers — and it
does. Albatross → the wind-shear layer. Solar sail → the radiation field. Electrodynamic tether
→ the planet's rotation, through the magnetic field. Each was once described as fuel-free, and
each turned out to have a nameable partner and a computable `Σ`.

**Three for three, and one of them we ourselves got wrong first.** That is the base rate that
justifies asking the question a fourth time.

## The unexplored corner it points at

`q` assumes the coupling point does not move. A **cyclically driven thermodynamic harvester** —
one whose coupling point is deliberately moved through the gradient — would not be bounded by
`q` at all. Nobody has built or analysed one, and it sits precisely where this project's
founding intuition says to look: **arrangement, not magnitude.**
