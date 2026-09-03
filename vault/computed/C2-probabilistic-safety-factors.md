---
name: C2-probabilistic-safety-factors
type: computed
---

# Probabilistic safety factors for biological structures

> **For bone, failure probability is set by the variability of the tissue, not the variability of locomotion.**

[[stress-strength-interference]] applied to biological cases. Biology has only a
deterministic ratio; the formalism yields a probability of failure — which is precisely the
objection raised against symmorphosis since 1987.

## The robust result

Holding the safety factor at 3, moving strength CV from 0.10 to 0.30 swings P_f across **nine
orders of magnitude**. Moving load CV from 0.05 to 0.30 moves it **half an order**. Measured
locomotor load CV is only 0.05-0.11, small against SF x V_R of about 0.6.

Holds in both distributional models at every safety factor from 1.4 to 4.1. **And it points
at the term Alexander's mixed-chain argument de-emphasises** — he reasoned that links with
more variable *loading* should carry higher safety factors.

## What is not quotable

The specific numbers. The model choice decides the answer: normal gives P_f 5.2e-4,
lognormal 8.2e-7 — three orders apart, straddling the EN 1990 structural target from opposite
sides. No obtainable biological dataset can test the tail.

The comparison to engineering targets is **formally invalid** and flagged rather than deleted:
biological P_f here is *per load cycle*, EN 1990 is per fifty years, and an animal takes
1e6-1e7 steps a year.

## The remodeling objection is the deliverable

Stress-strength interference assumes strength is **fixed at manufacture**. In bone it is a
*function of realised load history*, with negative feedback — the individual in the weak tail
while being loaded hard is exactly the one that remodels, so **the interference region is
actively depleted.** Every P_f is an upper bound.

**This inverts the trade.** Engineering's assumption is the **zero-gain limit of a control
loop biology runs with positive gain.** A formalism for load-adaptive strength would be a
contribution *from* biology *to* reliability engineering.
