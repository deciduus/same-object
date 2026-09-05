---
name: C25-whittle-foraging
type: computed
---

# The Whittle index of a regrowing patch is `λx² − r(1−x)²`

> **A forager should leave a fast-regrowing patch at a *higher* standing crop than the
> marginal value theorem prescribes: at fixed habitat quality the giving-up density rises as
> `GUD(r) ≈ GUD_MVT + [(1−GUD_MVT)²/(2·GUD_MVT)]·(r/λ)`, so a patch regrowing at `r·τ = 0.2`
> should be abandoned at ~1.34× the MVT giving-up density and ~0.76× the MVT residence
> time.** The transfer across [[C5-charnov-gittins]] answers [[Q5-restless-patches]]: the
> restless patch **is** indexable, unconditionally, and the Whittle index is a two-term
> closed form whose `r → 0` limit reproduces C5 eq. (4) exactly — but only once
> non-revisitability is re-imposed by hand, which quantifies C5 §6 row 6.

First Layer-3 derivation in the vault: a result transferred across a proven bridge to a new
falsifiable prediction. Executes backlog E4 / `audits/03` item 25 / `audits/05` item 3, under
the ten-line brief in [[C5-charnov-gittins]] §12.

---

## 1. Model

Continuous time. One patch is a bandit arm; the forager activates one arm at a time.
`G_max` normalised to 1, so the state **is** the giving-up density when the forager departs.

| | |
|---|---|
| **State space** | `x ∈ X = [0, 1]`, standing resource in units of `G_max` |
| **Active** (forager present) | `ẋ = −λx`, reward rate `λx` |
| **Passive** (patch unoccupied) | `ẋ = r(1−x)`, reward rate `0` |
| **Travel** | `τ` per patch transition |
| **Discount** | `δ → 0` (average reward), as in C5 §5.2 via renewal–reward |

Consistency with C5: starting a visit at `x = 1`, the active dynamics integrate to
`g(t) = G_max(1 − e^{−λt})` — Charnov's concave gain function, exactly the standard
exponential-saturation form — and the intake rate is `g'(t) = λx(t)`. So `λx` **is** the
marginal value, and MVT's rule `g'(t*) = R*` reads `λx* = R*`.

The passive dynamics are the exponential-saturation mirror: recovery toward `G_max` at rate
`r`, i.e. `x(s) = 1 − (1 − x_dep)e^{−rs}` after `s` units away. `r = 0` freezes the arm and
recovers the classical (Gittins) bandit; `r → ∞` refills it instantly.

**Dimensionless groups.** `r/λ` (regrowth per unit of depletion) and `λτ` (travel per unit of
depletion). The table below reports `r·τ`; with `λτ = 1` the two coincide numerically.

## 2. Indexability

Whittle's relaxation: drop "exactly one arm active" to "one active on average", attach a
subsidy `ν` per unit time spent passive, and solve the single-arm average-reward problem.
The HJB equation for the relative value `V` and gain `ρ` is

```
ρ = max{ λx − λx·V'(x) ,  ν + r(1−x)·V'(x) }                           (1)
```

so passivity is preferred exactly when

```
ν  ≥  λx − V'(x)·[ λx + r(1−x) ]                                       (2)
```

The bracket is the *difference* in resource flow between passive and active operation; `V'(x)`
is the shadow price of resource left standing. Equation (2) is the whole structure: **the
Whittle index is the immediate intake rate minus the shadow value of the resource you consume
by staying.** MVT is the special case `V' ≡ 0`.

**Indexability** requires the passive set `P(ν) = {x : W(x) ≤ ν}` to grow monotonically from
`∅` to `X` as `ν` sweeps `−∞ → ∞`. With `W` from §3,

```
W'(x) = 2λx + 2r(1−x) > 0   for all x ∈ (0,1),  λ, r > 0
```

`W` is a strictly increasing continuous bijection `[0,1] → [−r, λ]`, so `P(ν) = [0, W⁻¹(ν)]`
is a nested family. **Indexable, unconditionally, for every `λ, r > 0`** — no parameter
restriction, no condition to check. This places the model inside the monotone/threshold
families of Whittle (1988, *J. Appl. Prob.* 25A, `10.2307/3214163`), Niño-Mora (2001,
*Adv. Appl. Prob.* 33:76–98, `10.1239/aap/999187898`, partial conservation laws) and
Glazebrook, Ruiz-Hernández & Kirkbride (2006, *Adv. Appl. Prob.* 38:643–672,
`10.1239/aap/1158684996`) — all three DOIs, titles, authors and journals verified against
Crossref `api.crossref.org/works/{doi}`, fetched 2026-09-05 — rather than requiring their
machinery. The single-threshold structure is what those papers establish for harder cases;
here it is direct.

## 3. The index

The relaxed single-arm optimum in continuous time is bang-bang with a singular arc: at the
indifference level `a` the control is the fraction `u` of time active that holds `ẋ = 0`,

```
u*(a) = r(1−a) / [ λa + r(1−a) ],   ρ(a) = A(B + ν)/(A + B),  A = λa, B = r(1−a)
```

Setting `∂ρ/∂a = 0` and clearing (`r > 0`) gives `ν = 2ra + a²(λ − r) − r`, i.e.

```
   W(x)  =  λ x²  −  r (1 − x)²                                        (3)
```

**Cross-check against (2).** Substituting (3) into (2) gives
`V'(x) = [λx(1−x) + r(1−x)²]/[λx + r(1−x)] = 1 − x`, so `V(x) = x − x²/2`. This is an
independent confirmation and it is interpretable: the shadow price of standing resource is
`1 − x`, the *room left to grow*. Resource in a full patch is worthless because the patch is
capped at `G_max` and cannot bank it. Substituting `V' = 1−x` back into (1) reproduces (3)
identically.

**Reading (3).** `λx²` is the immediate rate `λx` discounted by the fraction `x` of it that
represents resource you could have banked; `−r(1−x)²` is the regrowth you forgo by occupying
the patch instead of letting it refill. Both terms push the same way: **stay less.**

## 4. The two limits

**`r → 0`, patches revisitable.** `W(x) → λx²`. This is *not* MVT. The gap is not an error:
with `r = 0` and revisits allowed, resource left behind is not lost, so `V' = 1−x ≠ 0` and the
index correctly deducts it. **This quantifies C5 §6 row 6** — Banks & Sundaram's structural
break under switching costs — which C5 could only name.

**`r → 0`, patches non-revisitable (C5's licensing condition).** A departed patch is gone, so
its stored resource has value `0`: `V' ≡ 0` by fiat. Then (2) gives `W(x) = λx = g'(t)`, and
the leaving rule `W(x*) = ν(habitat)` is

```
g'(t*) = R* = max_t  g(t)/(τ + t)
```

which is **C5 eq. (4), exactly.** The check demanded by C5 §12 item 7 passes, and it passes
*conditionally on precisely the condition C5 identified as the licence.* That is a stronger
result than an unconditional pass would have been.

**`r → ∞`.** `W(x) → −∞` for every `x < 1`, with `W(1) = λ`. The departure threshold →
`G_max`, residence time → `0`: skim the top of a patch that is always full, travel, repeat.
The degenerate answer, and the numerics confirm it (`r/λ = 10⁶` → `GUD = 0.99905`,
`t* = 9.5 × 10⁻⁴`).

## 5. The prediction

**The degeneracy that must be stated first.** `W` is strictly increasing in `x`, so in a
habitat of *identical* patches `argmax_i W(x_i) = argmax_i x_i`: the Whittle priority rule
collapses to "go to the fullest patch" and the `r`-dependence cancels out of it entirely.
**The index carries no testable signal in a homogeneous habitat.** It bites only across patch
types that differ in `r` (or `λ`). Any test must be a *contrast*, and this is the single most
important design constraint the derivation imposes.

Fix the habitat indifference index `ν` (the equilibrium Whittle subsidy — the restless
analogue of `R*`) and anchor it so the rule agrees with MVT at `r = 0`: `ν = λ·GUD_MVT²`.
Then `W(x) = ν` solves in closed form, with `ρ ≡ r/λ` and `u₀ ≡ GUD_MVT`:

```
GUD(ρ) = [ −ρ + √( ρ + u₀²(1 − ρ) ) ] / (1 − ρ),      GUD(1) = (1 + u₀²)/2     (4)
```

and the comparative static, obtained by implicit differentiation of `W(x) = ν`, is the
**one equation** of this note:

```
   d GUD / d r  =  (1 − GUD)² / ( 2[ λ·GUD + r(1 − GUD) ] )   >  0     (5)
```

Strictly positive everywhere. **Sign: faster regrowth ⟹ higher giving-up density and shorter
residence.** This confirms the sign conjectured in [[Q5-restless-patches]] and demanded by C5
§12 item 8, and it now has a magnitude.

**Table** (`λ = 1`, `λτ = 1` so `r·τ = r/λ`; `G_max = 1`; `u₀ = 0.30`; residence times from an
arrival at `x = 1`). Generated by `vault/_scripts/c25_whittle.py`.

| `r·τ` | `GUD(r)` | `ΔGUD` | `GUD/GUD_MVT` | `t*(r)` | `t*/t*_MVT` |
|---|---|---|---|---|---|
| 0.00 | 0.3000 | +0.0000 | 1.000 | 1.204 | 1.000 |
| 0.05 | 0.3348 | +0.0348 | 1.116 | 1.094 | 0.909 |
| 0.10 | 0.3616 | +0.0616 | 1.205 | 1.017 | 0.845 |
| 0.20 | 0.4019 | +0.1019 | **1.340** | 0.912 | **0.757** |
| 0.50 | 0.4765 | +0.1765 | 1.588 | 0.741 | 0.616 |
| 1.00 | 0.5450 | +0.2450 | 1.817 | 0.607 | 0.504 |
| 2.00 | 0.6180 | +0.3180 | 2.060 | 0.481 | 0.400 |
| 5.00 | 0.7115 | +0.4115 | 2.372 | 0.340 | 0.283 |
| 10.00 | 0.7743 | +0.4743 | 2.581 | 0.256 | 0.212 |
| 50.00 | 0.8826 | +0.5826 | 2.942 | 0.125 | 0.104 |

Small-`r` expansion, from (5) at `r → 0⁺`:

```
GUD(r)  ≈  u₀ + [ (1 − u₀)² / (2u₀) ] · (r/λ)   =  0.300 + 0.817·(r/λ)   at u₀ = 0.30
```

**The falsifiable statement.** Two patch types in one habitat, matched in `G_max` and `λ`,
differing only in measured regrowth rate `r`. MVT predicts **equal** giving-up densities (the
threshold `R*` is a habitat property, not a patch property). The Whittle rule predicts the
fast type is left at a strictly higher standing crop, by the amount in (4)–(5). A measured
`ΔGUD` of zero within error falsifies the transfer; a *negative* `ΔGUD` falsifies it and MVT
together.

## 6. Dataset

**Kadmon & Shmida (1992), *Evolutionary Ecology* 6:142–151, `10.1007/BF02270708`** — departure
rules of *Anthophora* and *Eucera* bees on *Anchusa strigosa*; paired with **Kadmon (1992),
*Oecologia* 92:552–555, `10.1007/BF00317848`**, which measures nectar renewal in the *same
plant–pollinator system*. Both DOIs, titles, authors, journals and years verified against
Crossref (`api.crossref.org/works/{doi}`), fetched 2026-09-05; `is-referenced-by-count` 62 and
16 respectively.

Why this pair: it is the rare case where `r` and the departure decision are measured on the
same system. The *Oecologia* paper supplies the regrowth side (and reports that renewal is
**linear** and independent of standing crop — see §7); the *Evolutionary Ecology* paper
supplies departure probability as a function of the reward received at the last two flowers.

**What a test needs, and what this pair does not yet give.** Required: (i) `r` measured per
patch type, independently of the forager; (ii) standing crop *at the moment of departure*, per
patch type; (iii) ≥ 2 patch types differing in `r` with `G_max` and `λ` matched; (iv) `τ`
between patches. Kadmon & Shmida give (ii) only in the coarse form of a departure probability
against last-flower reward, and do not stratify by renewal rate — so the pair **motivates and
parameterises** the test but does not itself run it. The clean version is a manipulation:
artificial flowers on two programmed refill rates, interleaved in one array. Related but
unsuitable as-is: Possingham (1989) *Am. Nat.* 133:42–60, `10.1086/284900` (verified, Crossref,
2026-09-05) and Ohashi & Thomson (2005) *Behav. Ecol.* 16:592–605, `10.1093/beheco/ari031`
(verified, Crossref, 2026-09-05) — both are **models/simulations**, not measured foragers.

## 7. Honesty: assumptions, gaps, first line of attack

**Assumed.**

1. Passive dynamics `ẋ = r(1−x)`. **Kadmon (1992) measured linear renewal** in *Anchusa*,
   `ẋ = const` up to a cap, not saturating-exponential. The derivation runs the same way with
   linear renewal but (3) changes; the *sign* of (5) survives, the coefficients do not.
2. Active intake proportional to standing crop (`λx`). Handling-time-limited foragers violate
   this.
3. Deterministic patches, stationary habitat, identical foragers, no learning, no competition,
   no predation — GUD in the Brown tradition is a *joint* measure of energetic and predation
   costs, and this model contains none of the latter.
4. Round-robin / symmetric visitation when converting a threshold into `t*`.

**Not closed.**

- **`τ` is outside the Whittle relaxation.** The index (3) is derived for zero switching
  *delay*. Travel is re-inserted only at the level of the renewal cycle and the equilibrium
  subsidy `ν`. A restless bandit with switching delay is not the problem Whittle solved, and
  §5's `r·τ` axis is therefore a *reporting* convention (`λτ = 1`), not a derived scaling.
  **This is the largest hole.**
- **`ν` is anchored, not solved.** The equilibrium subsidy is fixed by the `r → 0` agreement
  with MVT rather than computed from an `N`-patch fixed point. That makes the table a
  statement about *relative* GUD across patch types at one habitat quality — which is what the
  falsifiable claim needs — but not an absolute prediction of GUD.
- **No optimality gap is stated.** Whittle indices are optimal only asymptotically
  (Weber–Weiss), and that regime is many arms with a *fixed* active fraction. A single forager
  among `N` patches is `N → ∞` with active fraction `1/N → 0`, which is **not** the regime the
  asymptotic-optimality theorems cover. Q5 anticipated "an approximation with a stated
  optimality gap"; the gap is **not** stated here. Honest status: an indexable heuristic with
  a signed comparative static, not a bounded approximation.
- The singular-arc argument in §3 is a continuous-time relaxation. The discrete-time index may
  differ at `O(Δt)`; not checked.

**What a referee attacks first.** The homogeneous-habitat degeneracy in §5. A hostile reader
will say: your index is a monotone function of standing crop, so your policy is "visit the
fullest patch", which is what every forager already does and what MVT already implies; the
`r`-dependence survives only in a between-type contrast requiring an experiment nobody has
run. That is correct, and it is why §5 states it before the prediction rather than after. The
second attack is the `λx²` at `r → 0` — a referee will read it as a failure to recover MVT
until §4's revisitability argument is understood, so that paragraph carries the result.

## 8. What it does not settle

It does not answer whether real foragers do this. It does not close [[Q5-restless-patches]] —
it answers Q5's *first* question (yes, indexable; here is the index; here is the signed
regrowth term) and leaves Q5's optimality-gap question open. And it does not touch C5 §6 rows
6 and 7 beyond quantifying row 6's residual: switching costs and non-stationarity still admit
no index at all.

Script: `vault/_scripts/c25_whittle.py` (stdlib only; reproduces §2, §4, §5).
