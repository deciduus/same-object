---
name: C34-load-yield-clustering
type: computed
closes: "[[G35-genetic-load-die-yield]]"
last-checked: 2026-09-05
result: "alpha = 45 [26, 92]; mean fitness is 1.6% above e^(-U) at U = 1.2, 5.4% at U = 2.2"
exit: prediction
extends-to: [conservation]
next-step-cost: S
---

# The clustering parameter α for genetic load

> **`α ≈ 45` (95% interval 26–92) for human de novo mutation counts, against `α ≈ 0.3–5` for
> defects on a silicon wafer — so the Haldane–Muller `W̄ = e^(−U)` is right to within +1.6% at
> `U = 1.2` and +5.4% at `U = 2.2`.** This narrows [[G35-genetic-load-die-yield]] from "genetics
> is missing a correction term" to "genetics is missing the *bound* that shows the correction is
> small, and missing the vocabulary to say why." It does **not** show the correction is small for
> the object conservation genomics actually measures — segregating load per individual — which is
> a different and far more overdispersed count. See §Honesty.

Script: `vault/_scripts/c34_yield.py` (stdlib only, seed 20260905). Every number below is
reproduced by running it.

## The quantity

```
Poisson  (Murphy 1964 limit)  Y   = exp(−A·D0)          W̄ = exp(−U)
Stapper 1983 (clustered)      Y   = (1 + A·D0/α)^(−α)   W̄ = (1 + U/α)^(−α)
                              α   -> ∞  recovers the Poisson form
```

`α` is the shape of the gamma distribution the Poisson mean is mixed over. It is dimensionless
and bounded in `(0, ∞)`: `α -> ∞` is "every unit sees the same expected defect count"; `α -> 0`
is "all the defects on a few units and none on the rest". **Clustering always raises survival
above the Poisson prediction at fixed mean**, because concentrating defects wastes them on units
that were already dead. In moments, for a count `K` with mean `μ`:

```
α  =  μ² / (Var[K] − μ)        equivalently   α = E[λ]² / Var[λ]
```

for `K | λ ~ Poisson(λ)` and `λ` varying across units. The biological reading of `λ` varying is
**variance in the mutation rate among individuals or lineages** — the exact analogue of a wafer
whose defect density is not uniform across its face.

## Inputs

| Input | Value | Source |
|---|---|---|
| Mean de novo mutations per proband, `μ` | **70.0** | Jónsson et al. 2017, *Nature* 549:519, `10.1038/nature24018`, 1,548 Icelandic trios. Crossref-verified 2026-09-05 |
| Paternal-age slope `b_f` | **1.51 / year** | same |
| Maternal-age slope `b_m` | **0.37 / year** | same |
| Cross-check `μ`, `b_f` | **63.2**, **~2.01 / year** | Kong et al. 2012, *Nature* 488:471, `10.1038/nature11396`, 78 trios. Crossref-verified 2026-09-05 |
| Paternal-age SD `s_f` | **6.0 y** — **ASSUMED, UNSOURCED** | not tabulated in either paper's main text; swept 3–10 y below |
| Maternal-age SD `s_m`, correlation `ρ` | **5.0 y**, **0.7** — **ASSUMED, UNSOURCED** | swept 3.5–6.5 y and 0.45–0.90 in the Monte Carlo |
| Deleterious rate `U` | **0.5 / 1.2 / 2.2** — **UNVERIFIED as a point value** | swept, not asserted; human `U_del` estimates span this range |
| Wafer `α` | **0.3–5** — **UNVERIFIED** | Stapper 1983 / Cunningham 1990 fitted range as reported in the yield-model literature; not read off a table in this run |

**Why this route and not a fitted per-trio table.** The trio-level DNM tables behind Jónsson 2017
and Kong 2012 are under controlled access and were not fetched. But the source literature itself
models the per-trio count as Poisson with a mean linear in parental age, so `Var[λ]` across a
cohort is fully determined by the published slopes and the cohort's parental-age variances:

```
Var[λ] = b_f²s_f² + b_m²s_m² + 2·b_f·b_m·ρ·s_f·s_m
```

That is a method-of-moments fit of the negative binomial done on published coefficients rather
than on rows. It is weaker than a likelihood fit to counts and is labelled as such.

**Thinning invariance — the step that makes `α` transferable, and it is exact.** Only a fraction
`p` of DNMs are deleterious, so `U = p·μ`. If the total count is `NB(μ, α)` then the deleterious
count is `NB(p·μ, α)` — *the same `α`*. Proof: NB is a gamma–Poisson mixture; independently
thinning `Poisson(λ)` gives `Poisson(pλ)`, and `p·Gamma(α, θ) = Gamma(α, pθ)`, whose shape is
still `α`. **The unknown `p` cancels**, so an `α` fitted on total DNM counts is the `α` that
belongs in the load formula. Confirmed numerically in §[4] of the script (total `α̂ = 45.0`;
deleterious `α̂ = 53.7` on 4×10⁵ draws — consistent, but the deleterious estimate is
moment-noisy because it divides by a variance excess of ~0.03 on a mean of 1.2, and should be
read as "not distinguishable from 45", not as a second estimate).

## Result

**`α` from the mixture.**

| Route | `μ` | `Var[λ]` | **`α`** |
|---|---|---|---|
| Jónsson 2017 slopes | 70.0 | 109.0 | **45.0** |
| Kong 2012 slopes | 63.2 | 180.1 | **22.2** |
| **Monte Carlo, 2×10⁵ draws over all uncertain inputs** | — | — | **45.4, 95% interval [25.9, 91.5]** |

The interval is dominated by `s_f`, the assumed input:

| `s_f` (y) | 3.0 | 4.0 | 5.0 | **6.0** | 7.0 | 8.0 | 10.0 |
|---|---|---|---|---|---|---|---|
| `α` | 137 | 88 | 61 | **45** | 34 | 27 | 18 |

Across the whole plausible range `α` stays **above 18**, an order of magnitude above the wafer
range. **That ordering is the robust part of this note**; the point value is not.

**`e^(−U)` versus `(1 + U/α)^(−α)`.**

| `U` | `α` | `e^(−U)` | NB | NB/Poisson | excess |
|---|---|---|---|---|---|
| 0.5 | **45.0** | 0.60653 | 0.60821 | 1.0028 | **+0.28%** |
| 1.2 | **45.0** | 0.30119 | 0.30597 | 1.0159 | **+1.59%** |
| 1.2 | 25.9 (CI low) | 0.30119 | 0.30941 | 1.0273 | +2.73% |
| 1.2 | 91.5 (CI high) | 0.30119 | 0.30355 | 1.0078 | +0.78% |
| 2.2 | **45.0** | 0.11080 | 0.11673 | 1.0535 | **+5.35%** |
| 2.2 | 25.9 (CI low) | 0.11080 | 0.12103 | 1.0923 | +9.23% |
| 1.2 | 5.0 (wafer, loose) | 0.30119 | 0.34111 | 1.1325 | +13.25% |
| 1.2 | 3.0 (wafer, typical) | 0.30119 | 0.36443 | 1.2100 | **+21.00%** |
| 2.2 | 0.3 (wafer, tight) | 0.11080 | 0.52936 | 4.7775 | +377.75% |

For `U ≪ α` the excess is `exp(U²/2α) − 1` (checked: +1.586% exact vs +1.614% approximate at
`U = 1.2, α = 45`). Inverting it gives the **threshold `α` at which the correction reaches 10%**:

| `U` | 0.5 | 1.2 | 2.2 | 5.0 |
|---|---|---|---|---|
| `α` must be ≤ | 1.31 | 7.55 | 25.4 | 131 |

**So the human de novo `α ≈ 45` is inside the "matters at 10%" region only if `U ≳ 2.2`** — which
is the upper end of the swept range and precisely where the load literature's own estimates are
most contested.

## What the yield literature already knows that genetics could use

1. **`α` is a measurable, published quantity with four decades of fitted values.** Yield
   engineers do not treat clustering as a nuisance to be absorbed into an effective `D0`; they
   fit `α` per process line and report it. Genetics currently absorbs the same physics into
   epistasis as a free parameter. The negative-binomial form is one parameter, is nested (Poisson
   at `α -> ∞`), and is testable by a likelihood-ratio test on counts genetics already collects.
2. **Clustering always raises survival — the sign is known before any fitting.** Any genetics
   result that assumes Poisson load is therefore *conservative* about mean fitness, never
   anti-conservative. That is a free directional bound the field has not stated.
3. **The window model.** Stapper's second contribution is that `α` depends on the *area window*
   over which clustering is measured — a wafer-scale `α` differs from a die-scale one. The
   genetics analogue is that `α` depends on whether you count per gamete, per individual, per
   family or per population, and the field's estimates silently mix these levels.

## Prediction

**For a population with clustered deleterious mutations, mean fitness exceeds the Haldane–Muller
prediction by the factor `exp(U²/2α)`, computable from the per-individual count distribution
alone.** Concretely: fit a negative binomial to per-individual deleterious-allele counts, take
`α̂`, and published `e^(−U)` load estimates for that population are low by
`(1 + U/α̂)^(−α̂)·e^{U} − 1`.

**The dataset that could test it: the vaquita genomes.** Robinson et al. 2022, *Science*,
`10.1126/science.abm1742` (Crossref-verified 2026-09-05) reports **per-individual counts of
strongly deleterious and loss-of-function alleles for 20 vaquita genomes** — a directly
countable per-individual load distribution, in the single population whose extinction risk was
then simulated forward under an explicit load model. Fitting `α` to those 20 counts and rerunning
their forward simulation with `(1 + U/α)^(−α)` in place of the multiplicative-independent form is
a self-contained test of whether the correction changes a published extinction probability. The
Isle Royale wolves (Robinson et al. 2019, *Sci. Adv.*, `10.1126/sciadv.aau0757`,
Crossref-verified 2026-09-05) are the second such dataset, with a known bottleneck that should
have *reduced* `α` relative to the source population — a directional prediction the two datasets
can be paired to test.

## Honesty

**Are per-individual mutation counts the right object?** Not obviously. The Haldane–Muller `U` is
a *rate* — new deleterious mutations per genome per generation — and this note fits `α` to
exactly that (de novo counts per trio). But the object conservation genomics measures and
simulates is **segregating load**: the number of deleterious alleles an individual carries,
accumulated over many generations and shared with relatives. That count is far more overdispersed
than the per-generation one, because it inherits variance from relatedness, demographic history
and ancestry, none of which enter the age model here. **`α ≈ 45` is an upper-region estimate for
the de novo rate and says nothing directly about the segregating-load `α`,** which could plausibly
sit in the wafer range and which the vaquita test above is designed to measure. The headline
"Haldane–Muller is fine to 1.6%" is therefore a statement about the *mutation rate*, not about the
*load*, and the note's own prediction is what would extend it.

**Has selection already thinned the distribution?** Yes, and it cuts against the estimate. The
de novo counts are measured in liveborn probands, so the most severely loaded conceptuses are
already absent. Selection removes the upper tail preferentially, which *reduces* the observed
variance and therefore *inflates* `α̂`. The true pre-selection `α` is smaller than 45 by an
unknown amount. This is one-directional and unquantified here, and it is the reason the note
reports "α is large" rather than "α = 45".

**Is `A·D0 ↔ U` exact?** Not quite, in two places. (i) `A·D0` is a product of two separately
measurable quantities and yield engineering routinely varies `A` at fixed `D0` to trace the yield
curve; genetics has no free analogue of die area, so the correspondence is between `U` and the
*product*, not between any genetic quantity and `D0` alone. Genome size is the closest analogue
of `A` and is not experimentally variable. (ii) Yield's per-defect severity cancels because any
killer defect kills — a hard threshold. Genetics' severity cancels for a subtler reason (weak
mutations persist longer at exactly the compensating rate), which holds at equilibrium and fails
away from it. **The two exponentials are the same function reached by two different arguments**;
the algebra transfers, and the license to transfer *the correction* rests on both fields' counts
being gamma-Poisson mixtures, which is an assumption on the genetics side and a fitted fact on
the wafer side.

**What this note is not.** It is not a likelihood fit to per-trio counts — those tables are under
controlled access and were not fetched. It is a method-of-moments estimate from published
regression coefficients, with the dominant input (`s_f`) assumed and swept rather than sourced.
A reader who wants the point value rather than the ordering should treat `α = 45` as UNVERIFIED
and the interval [26, 92] as the honest content.
