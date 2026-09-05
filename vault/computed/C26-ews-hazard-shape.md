---
name: C26-ews-hazard-shape
type: computed
closes: G29-early-warning-prognostics
last-checked: 2026-09-05
result: "beta from an EWS-derived hazard is estimator-dependent and does not discriminate: Cariaco 5.84 [1.98, 10.63] vs no-bifurcation surrogate 7.39, p = 0.66"
exit: computation
extends-to: [ecology, conservation]
next-step-cost: S
---

# An early-warning indicator can be converted into a Weibull hazard shape — and the shape does not discriminate

> **RESULT — the discriminator fails, and the failure is the finding.** Converting the
> Dakos/Scheffer critical-slowing-down indicator into a Si-2011-style first-passage RUL gives
> the Cariaco Younger-Dryas record **β = 5.84, 95% CI [1.98, 10.63]** — nominally "wear-out",
> nominally the bifurcation arm. But a **stationary AR(1) surrogate with no bifurcation at all
> returns β = 7.39 [1.99, 15.09]** (one-sided surrogate `p = 0.66`), and the **same record with
> the transition cut off returns β = 4.97 [1.70, 8.21]**. Worse, β is not even a property of the
> system: on one engineering fleet (C-MAPSS FD001) the ensemble-lifetime MLE gives **β = 4.41
> [3.90, 5.30]** while the degradation-to-first-passage route on the *same 100 units* gives
> **β = 0.97 [0.78, 1.20]** — a factor of 4.5 from the estimator alone. **The `β` axis of
> [[C18-durability-axis]] is not estimator-invariant, and the scout's proposed
> `β > 1 bifurcation / β ≈ 1 noise` discriminator is not measurable from a single ecological
> time series.** [[G29-early-warning-prognostics]] stays **live**: this closes the computation
> the gap named, and the answer is negative.

Bears on [[C18-durability-axis]] (the β axis, corrected) and [[C17-offset-from-threshold]] (the
EWS indicator is C17's offset ε; the RUL is its settling time).

Script: `vault/_scripts/c26_ews.py` (stdlib + numpy). Run 2026-09-05, `--boot 300`.

---

## 1. The quantity

```
β  ≡  Weibull shape parameter of the time-to-transition distribution
      S(t) = exp[ −(t/η)^β ] ,   hazard  h(t) = (β/η)(t/η)^(β−1)
```

`β = 1` is constant hazard (memoryless, noise-induced kicks over a fixed barrier). `β > 1` is
increasing hazard (wear-out; a system whose own stability is being eroded). `β < 1` is infant
mortality. The scout's claim was that ecology has no instrument to tell these apart for a
regime shift, and that prognostics does. §3 tests that.

## 2. Two estimators, applied to both sides

| | What it needs | Ecology has it? | Engineering has it? |
|---|---|---|---|
| **R1** direct Weibull MLE on a sample of failure times | many independent run-to-failure records | **no** — one transition per palaeo/lake series | yes |
| **R2** degradation-to-threshold: fit `D(t) = D₀ + μt + σW(t)`, first passage to `L` is Inverse-Gaussian `IG(m=(L−D₀)/μ, λ=(L−D₀)²/σ²)`, report the Weibull matching it over the 1–99% quantile range | one signal that drifts toward a threshold | **yes** — the rolling lag-1 autocorrelation, `L = 1` | yes |

R2 is Si (2011)'s own Wiener-degradation RUL estimator composed with the Dakos *et al.* (2008)
early-warning indicator. **That composition is the object G29 says nobody has built**, and R2 is
run on *both* sides here so the two numbers are one estimator rather than two.

R1's absence on the ecology side is [[C18-durability-axis]]'s asymmetry, transplanted: everyone
reports the mean (return time), only one side reports the distribution.

## 3. Inputs

| Source | What | Provenance |
|---|---|---|
| Cariaco Basin greyscale, Younger Dryas → Preboreal, 2,111 samples, 12,549–11,569 yr BP (≈0.464 yr/sample) | ecology, **field** | `YD2PB_grayscale.rda` in the `earlywarnings` R package, `github.com/earlywarningtoolbox/earlywarnings-R/data/`, fetched 2026-09-05. The series behind Dakos *et al.* 2008 PNAS 105:14308, [10.1073/pnas.0802430105](https://doi.org/10.1073/pnas.0802430105) |
| Thermohaline-circulation collapse, 783 samples | ecology, **model output** | `circulation.rda`, same package, same fetch. Context row only — **not field data**, and nothing in the headline rests on it |
| NASA C-MAPSS `train_FD001`, 100 units, 1 fault mode, 1 operating condition | engineering | NASA Prognostics Data Repository; fetched 2026-09-05 from the mirror `github.com/hankroark/Turbofan-Engine-Degradation/CMAPSSData` |
| NASA C-MAPSS `train_FD004`, 249 units, 2 fault modes, 6 conditions | engineering | same fetch |

**Could not be fetched, and it matters.** (a) Carpenter *et al.* 2011 *Science*
[10.1126/science.1203672](https://doi.org/10.1126/science.1203672) — the Peter Lake whole-ecosystem
chlorophyll series is not in a machine-readable public archive I could reach, and **no number
from that paper appears in this note**, not even from its figures. (b) The **IMS bearing**
run-to-failure set (~6 GB of raw vibration) is out of budget for a desk session; the bearing row
of the table below is therefore **empty and stays empty**. Both are `UNSOURCED`, not estimated.

## 4. Result — one β axis

| # | Row | Estimator | **β** | 95% CI | n | Provenance / caveat |
|---|---|---|---|---|---|---|
| 1 | **ECO** Cariaco YD→Preboreal greyscale | R2 | **5.84** | [1.98, 10.63] | 2,111 pts → 1,057 indicator pts; 300 moving-block bootstrap reps, block 25 | field data; `μ = 2.90×10⁻⁶`, `σ = 5.56×10⁻⁵`, AR(1) 0.9759 → 0.9789 |
| 2 | **ECO** thermohaline collapse | R2 | 9.52 | [5.99, 11.96] | 783 pts → 393 | **MODEL output**, context only |
| 3 | **CTRL** stationary AR(1) surrogate, φ = 0.9772, no bifurcation | R2 | **7.39** | [1.99, 15.09] | 200 realisations; 97 (48.5%) gave **no passage at all** | *higher* than row 1. One-sided `p(β_surr ≥ β_obs) = 0.66` |
| 4 | **CTRL** Cariaco **first half only**, transition removed | R2 | **4.97** | [1.70, 8.21] | 1,055 pts → 529 | inside row 1's CI |
| 5 | **ENG** C-MAPSS FD001 | **R1** | **4.41** | [3.90, 5.30] | 100 lifetimes, 2,000 bootstrap reps; η = 225.0 cycles, mean 206.3, range 128–362 | the estimator ecology cannot run |
| 6 | **ENG** C-MAPSS FD001, **same 100 units** | **R2** | **0.97** | [0.78, 1.20] | per-unit, threshold `L` = 2.344 (fleet median health index at failure) | 4.5× below row 5 on identical data |
| 7 | **ENG** C-MAPSS FD004 | **R1** | 3.47 | [3.16, 3.86] | 249 lifetimes; η = 272.9, mean 246.0, range 128–543 | |
| 8 | **ENG** C-MAPSS FD004, same units | **R2** | 0.52 | [0.52, 0.57] | only 140/249 units fitted; `L` = −0.095 | **NOT QUOTABLE** — the health index is not normalised across FD004's six operating conditions, so this row measures my preprocessing |
| — | **ENG** IMS bearing run-to-failure | R1 | — | — | — | `UNSOURCED`: dataset not fetched, row deliberately empty |
| — | **ECO** Carpenter 2011 Peter Lake | R2 | — | — | — | `UNSOURCED`: series not machine-readable, row deliberately empty |

**Discriminator as stated by the scout:** `β > 1` ⇒ wear-out / bifurcation-driven;
`β ≈ 1` ⇒ memoryless / noise-induced.

**It does not survive contact with its own controls.** Rows 3 and 4 are the two things the
discriminator must beat, and it beats neither:

- Row 3 has **no bifurcation by construction** and returns a *larger* β than the real
  transition. Surrogate `p = 0.66`.
- Row 4 is the *same physical record* with the transition removed and lands inside row 1's
  confidence interval.
- The one statistic that looked promising — the indicator's drift-to-noise ratio, observed
  `0.0522` against a surrogate median `0.0066` — also fails: `p = 0.35` one-sided, because a
  rolling-window AR(1) estimate is itself strongly autocorrelated and drifts upward about half
  the time under a stationary null (48.5% of surrogates drifted the *other* way and gave no
  passage at all).

**And the extrapolation is quantitatively wrong.** Row 1's fitted first-passage mean is
`m = 8,316` samples ≈ **3,861 years** of remaining useful life. The record has **1,057 samples
≈ 491 years** left at that point, and then it transitions. The fitted RUL over-predicts
time-to-transition by roughly **8×**.

## 5. What this does to C18

[[C18-durability-axis]] proposed β as "the shared coordinate that DOES span both" fields. Rows 5
and 6 are the same 100 turbofans, and β moves from **4.41 to 0.97** purely by changing which
Weibull one fits — the ensemble of lifetimes, or the first-passage law implied by a single
unit's degradation path. These are different objects wearing one Greek letter: R1's β is a
property of *unit-to-unit dispersion in a fleet*; R2's β is a property of the *drift-to-noise
ratio of one degradation path*. **C18's β axis is well-defined only once the estimator is
named.** That is a correction to C18, not a refutation of it: C18's own worked cases
(enzyme partition ratios, cell cycle-life histograms) are all R1, and are internally consistent.

## 6. The prediction this licenses

Not the one the scout wanted. What survives is falsifiable and cheap:

> **Prediction.** For any ecological regime shift with a *single* pre-transition record,
> the R2 Weibull β estimated from a critical-slowing-down indicator will not separate
> bifurcation-induced from noise-induced transitions: across a set of published series with
> independently known mechanism, the two groups' β distributions will overlap with
> `p > 0.1` under a stationary-AR(1) surrogate test, and the mean fitted RUL will exceed the
> observed time-to-transition by more than 2× in the majority of cases.
>
> **Falsified by** any collection of ≥10 mechanism-labelled series in which R2 β separates the
> two classes at `p < 0.05` against matched surrogates. **The C-MAPSS FD001 row shows what a
> pass looks like** — with 100 replicate units, R1 β = 4.41 with CI [3.90, 5.30] cleanly excludes
> 1. **Replication, not the indicator, is the binding constraint.** The transplant ecology
> actually needs from prognostics is not the hazard model; it is the *fleet*.

## 7. Honesty

**Assumptions, each of which a referee can attack.**

1. **The Wiener model.** R2 assumes the indicator is a Brownian motion with constant drift. A
   rolling-window AR(1) estimate is nothing of the kind: successive windows overlap by
   `win − 1` points, so its increments are heavily autocorrelated and `σ` from `diff().std()`
   is badly biased low. The moving-block bootstrap (block 25) is a partial repair and is why
   the CIs are wide, not a fix.
2. **The threshold `L = 1`.** AR(1) → 1 is the textbook critical-slowing-down limit, but the
   indicator is a *finite-window estimate*, which is biased below the true lag-1 coefficient and
   never reaches 1 in practice. Choosing `L` smaller would shorten every fitted RUL and raise
   every β; the headline is sensitive to this and I did not sweep it.
3. **The IG→Weibull match.** Least squares on `log(−log S)` over the 1–99% quantile band. An IG
   is not a Weibull; the reported β is the best-matching shape, not a shape the data possess.
4. **One field series.** Row 1 is `n = 1` transition. Rows 2–4 are a model run and two
   surrogates. **Nothing here is an ecological sample.**
5. **Detrending.** Gaussian-kernel bandwidth 5% of series length, window 50% — the
   `earlywarnings::generic_ews` defaults. Dakos *et al.* showed the indicator's trend is
   bandwidth-sensitive; I did not re-run that sensitivity.
6. **C-MAPSS is simulation.** FD001/FD004 are the output of a turbofan degradation *simulator*,
   not measured engines. Its β is the simulator's β.

**What a referee attacks first.** Not any of the above — the **direction of the negative
result**. A hostile reading is: "you built a bad estimator, it failed, and you are reporting the
failure as a fact about ecology." The defence is row 6: the *same* estimator on real
prognostics-style data returns the textbook `β ≈ 1` for a Wiener-to-threshold process, which is
exactly right and shows the code is not broken. The estimator works; the *composition* — EWS
indicator as degradation signal — is what does not carry mechanism. The second attack is that
`p = 0.66` is a test with `n = 1` observed series and therefore has almost no power, which is
true, and is precisely why §6's prediction is stated over a *collection* of series.

**What it does not settle.** Whether a β-based discriminator would work given replicate
ecological records (§6 says test it). Whether variance or spatial-EWS indicators behave better
than AR(1) as a degradation signal — not tested. Whether the published bearing β values
(IMS, and the Weibull fits in the bearing-prognostics literature) sit near row 5 or row 6 — the
single most useful missing row in the table above, and one desk session away.
