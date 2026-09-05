# Blind brief — C48: the Whittle patch rule under LINEAR nectar renewal (P-068)

Written and sha256-hashed **before** any attempt to obtain Kadmon & Shmida (1992) or
Kadmon (1992), and before `vault/_scripts/c48_kadmon.py` existed. Nothing below is
conditioned on data.

## 0. Why this brief exists

`C25-whittle-foraging` derives `W(x) = λx² − r(1−x)²` under **saturating** passive dynamics
`ẋ = r(1−x)`, and predicts `dGUD/dr > 0`. Its own §6 names the Kadmon pair as the dataset —
and records, against interest, that Kadmon (1992) measured **linear** nectar renewal,
independent of standing crop. So the model whose prediction is to be tested is not the model
the system obeys. This brief re-derives the rule for the renewal law the system actually has,
and fixes the prediction, before looking.

## 1. Model (linear renewal)

Identical to C25 §1 except the passive law. `G_max` normalised to 1.

| | |
|---|---|
| Active (forager present) | `ẋ = −λx`, reward rate `λx` |
| Passive (unoccupied) | `ẋ = c` for `x < 1`, `ẋ = 0` at `x = 1`; reward `0` |
| Travel | `τ` per transition |
| Discount | `δ → 0` (average reward) |

`c` is the constant refill rate (C25's `r` has no analogue with the same units; `c` is
`G_max`·(fraction refilled)/time). The **cap is essential**: without it linear renewal is
unbounded and the problem has no steady state.

## 2. Derivation A — the Whittle index

Whittle relaxation, subsidy `ν` per unit passive time. HJB for relative value `V`, gain `g`:

```
g = max{ λx − λx·V'(x) ,  ν + c·V'(x)·1{x<1} }                         (1)
```

Passivity preferred exactly when `ν ≥ λx − V'(x)·[λx + c]`.

The optimal single-arm policy is active-above-threshold (`active` gains with `x`, `passive`
does not), so it chatters on the singular arc at the threshold `a` with active fraction `u`
holding `ẋ = 0`:

```
u*(a) = c / (λa + c),      g(a) = A(B + ν)/(A + B),   A = λa,  B = c        (2)
```

— the same functional form as C25 (3), but with `B` now **constant in `a`** instead of
`B = r(1−a)`. That single change is the whole result. Differentiate:

```
∂g/∂a = λ · B(B + ν) / (A + B)²                                           (3)
```

**`∂g/∂a` never vanishes for `ν > −c`.** In C25 the `a`-dependence of `B` supplied the
competing term that produced an interior stationary point; with linear renewal there is no
such term, and the gain is strictly increasing in `a` for every `ν > −c` (strictly decreasing
for `ν < −c`). The maximiser is the boundary `a = 1`. Hence

```
   W(x) = −c   for all x ∈ (0,1),        W(1) = λ                          (4)
```

The passive set `P(ν) = {x : W(x) ≤ ν}` is `∅` for `ν < −c`, `[0,1)` for `−c ≤ ν < λ`, and
`[0,1]` for `ν ≥ λ`: nested, so the arm is **indexable but the index is a step function**.
It is flat on the interior and therefore carries **no state information and no `c`
information**. Predicted departure state: `GUD = G_max`, and

```
   d GUD / d c  =  0                                                        (5)
```

**Sign, stated blind: ZERO.** The graded `dGUD/dr > 0` of C25 is an artefact of the
saturating form. Under linear renewal the Whittle rule collapses to "go to the fullest
patch and skim it" — which is exactly the `fullest` policy that `C45-whittle-network-sim`
Table 1 measured at intake `0.0098` against MVT's `0.3154`, i.e. the worst of four policies.

## 3. Derivation B — the self-consistent cycle with explicit travel

Derivation A inherits C25's convention that `τ` lives only in the calibration of `ν`. With
`τ` explicit, and the forager returning to the same patch after `τ` (C25 §5 eq. 6 convention),
the arrival state is `x_arr = min(1, a + cτ)` and the long-run intake rate is

```
R(a) = (x_arr − a) / ( ln(x_arr/a)/λ + τ )                                  (6)
```

For `a ≥ 1 − cτ` the cap binds, `x_arr = 1`, and `∂R/∂a = 0` reduces to

```
   f(a) ≡ (1−a)/a + ln a  =  λτ                                            (7)
```

`f` is strictly decreasing on `(0,1)` from `+∞` to `0`, so (7) has a unique root `a_MVT(λτ)`,
**independent of `c`**. For `a < 1 − cτ` the numerator of (6) is the constant `cτ` and `R` is
maximised by making `a` as large as the regime allows, i.e. at the boundary. Therefore

```
   GUD*(c) = max( a_MVT(λτ), 1 − cτ ),   d GUD/dc = −τ  below the kink, 0 above   (8)
```

**Sign, stated blind: NEGATIVE-or-zero, never positive.** At `λ = 1`, `λτ = 1`: `a_MVT =
0.3179`, kink at `cτ = 0.6821`.

| `cτ` | 0.05 | 0.10 | 0.20 | 0.50 | 0.6821 | 1.0 | 2.0 |
|---|---|---|---|---|---|---|---|
| `GUD*` | 0.950 | 0.900 | 0.800 | 0.500 | 0.318 | 0.318 | 0.318 |

## 4. The blind prediction being registered

**P1.** Under linear renewal the Whittle index is flat on the interior (eq. 4); `dGUD/dc = 0`.
**P2.** Under the explicit-travel cycle, `dGUD/dc ≤ 0` (eq. 8), strictly negative for
`cτ < 1 − a_MVT`.
**P3.** Therefore the C25 field prediction (`GUD` rises with renewal rate) **does not
transfer** to the Kadmon system, and P-068 cannot confirm C25 no matter what the data say;
the only outcomes available are a **negative** measured slope (consistent with P2) or a
**zero** slope (consistent with P1) or a positive slope, which would falsify both.
**P4.** MVT with a habitat threshold `λx = R*` also gives `dGUD/dc = 0` per patch, so
Whittle and MVT are **behaviourally indistinguishable** in this system on derivation A. The
discriminating design must supply a saturating renewal law by construction — programme item
**P-088**.

## 5. What the data must contain

Required, in order of necessity:

1. **Per-flower standing crop at the moment of bee departure** (nectar volume, µl), or
   per-flower residence time with a known depletion law `λ`.
2. A **renewal-rate stratifier**: either measured per-flower/per-plant renewal rate `c`, or
   **time since last visit** as a proxy for accumulated `cΔt`, or an experimental
   bagging/renewal-rate manipulation.
3. `G_max` (cap on nectar per flower) and `λ` (extraction rate per bee-second), matched or
   measured across strata.
4. `τ`, the inter-flower flight time.

Kadmon (1992) supplies 2 and part of 3; Kadmon & Shmida (1992) supplies a coarse form of 1
(departure probability vs reward at the last flowers). Whether they can be joined **per
flower** is the access question, not a modelling question.

## 6. Statistic and gate

**Primary.** Spearman `ρ_s` of (departure standing crop) against (renewal rate `c`, or its
proxy), one point per flower, clustered by plant. Two-sided.
**Secondary.** Spearman of (residence time) against `c`.

**Gate, registered before looking:**

- `ρ_s > 0` at `p < 0.05` → **C25's sign survives even under linear renewal**; this brief's
  P1/P2 are falsified and the derivation above is wrong.
- `ρ_s < 0` at `p < 0.05` → **P2 confirmed**; C25's saturating-form prediction is contradicted
  in sign, and C25 §5 must be narrowed to "saturating renewal only".
- `|ρ_s|` not distinguishable from 0 (95% CI contains 0) → **P1 consistent**; but with `n`
  reported, and only declared informative if the CI excludes `+0.3` (C25's direction).
- `n < 30` usable flowers, or strata not separable → **honest null on access**, no verdict on
  C25 either way, and the brief's analytical content (§2–§3) stands as the deliverable.

**Sci-Hub is not permitted.** Access routes allowed: Europe PMC, Semantic Scholar open PDFs,
author-hosted copies, and figures/numbers reproduced in citing papers, each recorded with
provider + fetch date.
