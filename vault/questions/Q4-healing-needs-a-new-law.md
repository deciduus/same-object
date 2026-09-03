---
name: Q4-healing-needs-a-new-law
type: question
arises-from: ["[[G5-repair-number]]", "[[C6-damage-healing-ratio]]"]
status: answered-by-C10
---

# What replaces a healing law that cannot reach steady state?

> Trying to *use* an equation broke it. That is the most productive kind of failure available,
> and it leaves a specific thing to build.

## The defect

Set `ḣ = 0` in the Das & Kumari damage-healing evolution law and you get `D²(1−h) = 0`, so
`h → 1` always. **Continuum damage-healing mechanics has no interior steady state in the healing
variable**, because nothing in the law un-heals.

Healing there is a **ratchet**, not a rate balance.

## Why that is a door and not a wall

Every real self-healing system reaches a steady state under continuous loading. Bone does.
Photosystem II does — that is the whole content of [[C1-availability-living-tissue]]. A law that
cannot represent the observed regime is missing a term, and **the missing term is nameable**.

## The question

What is the correct un-healing term? The candidates are physically distinct and would be
distinguishable by experiment:

- **Healing agent depletion** — the capacity to heal is consumed, so `h` saturates below 1
- **Re-damage of healed material** — healed bonds are weaker and fail preferentially
- **Finite healing quality** — each cycle recovers less, which is the observed fade in cycled
  self-healing polymers

Only the second gives a genuine rate balance in `h`. The first and third give a decaying
envelope, which is a different mathematical object with a different steady state.

## Answered: [[C10-healing-curve-fit]]

Seven cycled datasets fit. **Candidate 2 — a genuine rate balance reaching a nonzero steady
state — is supported by none of them.** Healing efficiency decays monotonically with cycle
number in every series. The correct un-healing term is not a re-damage balance; it is a
**depleting envelope**, and *which* envelope is material-class-dependent:

| Material class | Winning shape | Un-healing term |
|---|---|---|
| Extrinsic microcapsule | decay to a **positive floor** | **candidate 1, depletion** — a finite non-refillable reservoir, stated in the review's own words |
| Vitrimer, high crosslink / neat imine | decay to a floor (~17–31%) | candidate 1, depletion |
| Vitrimer, low crosslink | **exponential decay to ~0** | **candidate 3, finite quality** — no steady state |

The load-bearing dataset (PMC11510012, five formulations, VERIFIED verbatim) splits by crosslink
density: `r ≈ 0.79` clean exponential for the low-crosslink formulations, a sharp drop onto a
floor for the rest.

**So candidate 1 is real and [[kirkwood-disposable-soma]] is the right frame** — a finite repair
budget — and it is still uncited by the self-healing literature. That is now confirmed, not
conjectured.

## Why it was answerable

Cycled self-healing polymer data exists and reports **healing efficiency against cycle number**.
Those three candidates predict different curve shapes — saturating, linear-decaying, and
exponentially-decaying respectively. **The discrimination is a curve fit on published data.**

## What it connects to

`Ha = k_r/k_d` in [[C6-damage-healing-ratio]] assumes a two-state rate balance. If healing is
really a ratchet with a depleting reservoir, **`Ha` is only valid over a window** and needs a
depletion parameter. That is the first real test of the group.

Also: [[kirkwood-disposable-soma]] is exactly a theory of *finite repair budget*, which is
candidate one. It is still unread by this literature.
