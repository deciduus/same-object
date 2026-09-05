---
name: C25-whittle-foraging
type: computed
---

# The Whittle index of a regrowing patch is `λx² − r(1−x)²`

> **A forager should leave a fast-regrowing patch at a *higher* standing crop than the
> marginal value theorem prescribes: at fixed habitat quality the giving-up density rises as
> `GUD(r) ≈ GUD_MVT + [(1−GUD_MVT)²/(2·GUD_MVT)]·(r/λ)`, so a patch regrowing at `r·τ = 0.2`
> should be abandoned at ~1.34× the MVT giving-up density and — once arrival is taken at the
> state the model's own passive dynamics deliver — ~0.20× the MVT residence time.** The
> transfer across [[C5-charnov-gittins]] answers [[Q5-restless-patches]]: the
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

**Consistency check against (2) — not an independent confirmation.** Substituting (3) into (2)
gives `V'(x) = [λx(1−x) + r(1−x)²]/[λx + r(1−x)] = 1 − x`. This is **(2) rearranged at
indifference**, i.e. the definition of the Whittle index solved for `V'`, so re-substituting
`V' = 1−x` into (1) reproduces (3) trivially and confirms nothing beyond internal consistency.
An earlier version of this note called it an independent confirmation; that was circular and
is withdrawn (audit 06).

Two things follow, and the second limits the first. `V(x) = x − x²/2` is a suggestive reading —
the shadow price of standing resource is `1 − x`, the *room left to grow*, and resource in a
full patch is worthless because the patch is capped at `G_max` and cannot bank it. But it is
**not** a value function: `V(x) = x − x²/2` does not solve the HJB with a constant gain, since
the active branch of (1) gives `λx − λx(1−x) = λx²`, which varies with `x` and so cannot equal
a constant `ρ`. Each subsidy `ν` carries its own value function; there is no single `V` across
the family. Read `V' = 1−x` as an interpretive gloss on the index, not as a derived object.

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

Strictly positive everywhere. **Sign: faster regrowth ⟹ higher giving-up density.** The
residence corollary holds only at fixed arrival state (`t_full` below is monotone decreasing);
the self-consistent steady-cycle residence is *non-monotone*, and the table states both. This
confirms the sign conjectured in [[Q5-restless-patches]] and demanded by C5
§12 item 8, and it now has a magnitude.

**Table** (`λ = 1`, `λτ = 1` so `r·τ = r/λ`; `G_max = 1`; `u₀ = 0.30`). Generated by
`vault/_scripts/c25_whittle.py`.

Two residence columns, and the distinction matters. `t_full` is the time to deplete a **full**
patch (`x = 1`) to the threshold — the quantity a first visit to an untouched patch takes, and
the only one earlier versions of this note reported. `t_cycle` is the **self-consistent
steady-cycle** residence: under §7 assumption 4 (round-robin) a forager returning after `τ`
away finds not `x = 1` but the state the note's own passive dynamics deliver,

```
x_arr = 1 − (1 − GUD)·e^{−rτ},     t_cycle = ln( x_arr / GUD ) / λ                (6)
```

`t_cycle` is the correct comparison against `t*_MVT = ln(1/u₀)/λ = 1.204`; the old column was
computed under an arrival state the model forbids in steady state, and its ratios were too high
by up to a factor of ~3.8.

| `r·τ` | `GUD(r)` | `ΔGUD` | `GUD/GUD_MVT` | `x_arr` | `t_full` | `t_full/t*_MVT` | `t_cycle` | `t_cycle/t*_MVT` |
|---|---|---|---|---|---|---|---|---|
| 0.00 | 0.3000 | +0.0000 | 1.000 | 0.3000 | 1.204 | 1.000 | 0.000 | 0.000 |
| 0.05 | 0.3348 | +0.0348 | 1.116 | 0.3673 | 1.094 | 0.909 | 0.092 | 0.077 |
| 0.10 | 0.3616 | +0.0616 | 1.205 | 0.4224 | 1.017 | 0.845 | 0.155 | 0.129 |
| 0.20 | 0.4019 | +0.1019 | **1.340** | 0.5103 | 0.912 | 0.757 | 0.239 | **0.198** |
| 0.50 | 0.4765 | +0.1765 | 1.588 | 0.6825 | 0.741 | 0.616 | 0.359 | 0.298 |
| 1.00 | 0.5450 | +0.2450 | 1.817 | 0.8326 | 0.607 | 0.504 | 0.424 | 0.352 |
| 2.00 | 0.6180 | +0.3180 | 2.060 | 0.9483 | 0.481 | 0.400 | 0.428 | **0.356** |
| 5.00 | 0.7115 | +0.4115 | 2.372 | 0.9981 | 0.340 | 0.283 | 0.338 | 0.281 |
| 10.00 | 0.7743 | +0.4743 | 2.581 | 1.0000 | 0.256 | 0.212 | 0.256 | 0.212 |
| 50.00 | 0.8826 | +0.5826 | 2.942 | 1.0000 | 0.125 | 0.104 | 0.125 | 0.104 |

**The steady-cycle residence is non-monotone in `r`, and the old column hid that entirely.**
`t_cycle/t*_MVT` rises from 0 at `r·τ = 0` to a maximum of **0.356 near `r·τ = 2`** and then
falls back toward 0 as `r → ∞`. The two limits are both degenerate and pull in opposite
directions: at `r → 0` the patch does not refill, so a round-robin forager arrives at the
density it left and stays no time at all; at `r → ∞` the patch is always full but the threshold
has risen to `G_max`, so again the visit is vanishingly short. The interesting regime is the
interior, and **the model predicts short visits at every `r`** — never more than ~36% of the MVT
residence time under round-robin. The monotone-decreasing story the old `t*` column told was an
artefact of holding arrival at `x = 1`. Note also that `t_full` and `t_cycle` converge for
`r·τ ≳ 5`, where `x_arr → 1` and the two conventions agree.

Small-`r` expansion, from (5) at `r → 0⁺`:

```
GUD(r)  ≈  u₀ + [ (1 − u₀)² / (2u₀) ] · (r/λ)   =  0.300 + 0.817·(r/λ)   at u₀ = 0.30
```

**Boundary condition, 2026-09-05: the prediction requires *saturating* renewal.**
[[C48-kadmon-regrowth-test]] re-derives the index under **linear** renewal (`ẋ = c` up to a cap),
which is what Kadmon (1992) actually measured in *Anchusa*. There the index degenerates:
`W(x) = −c` on the whole interior `(0, 1)` and `W(1) = λ`, i.e. a **step function** with no
`x`-dependence off the cap, so Whittle and MVT are **indistinguishable** as policies — and the
comparative static reverses sign: **`dGUD/dc ≤ 0`**, against `dGUD/dr > 0` here. The sign in (5)
is therefore a property of saturating renewal, not of restlessness. Two consequences: **Kadmon's
system cannot test this prediction** (P-068 closes on the negative branch), and **P-088's
artificial-flower array must implement saturating refill by construction, with a
linear-refill arm as a negative control** — a null on the linear arm is then a check on the
apparatus, and a null on the saturating arm is a real falsification.

**The falsifiable statement.** Two patch types in one habitat, matched in `G_max` and `λ`,
differing only in measured regrowth rate `r`. MVT predicts **equal** giving-up densities (the
threshold `R*` is a habitat property, not a patch property). The Whittle rule predicts the
fast type is left at a strictly higher standing crop, by the amount in (4)–(5). A measured
`ΔGUD` of zero within error falsifies the transfer; a *negative* `ΔGUD` falsifies it and MVT
together.

**Magnitude, after [[C45-whittle-network-sim]] (2026-09-05).** The 1.34× is the ratio *at the
MVT anchor* `ν = λ·GUD_MVT² = 0.09`, and the anchor is doing most of the work: run forward in a
20-patch network, the same anchor returns **1.2708 ± 0.0002** (`GUD_fast = 0.3987` against this
table's single-patch 0.4019, 0.8%), while learning `ν` as the network's realised long-run intake
rate returns **1.0600 ± 0.0002**. **The sign is calibration-free; the magnitude is not.** The
between-type ratio to predict is therefore **~1.06 to ~1.27 depending on how `ν` is set**, and
the usable design window is `r_fast·τ ∈ [0.2, 1]` — at `r_fast·τ = 10` the simulated forager
never visits the slow type at all and the ratio is undefined.

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
   `ẋ = const` up to a cap, not saturating-exponential. **Corrected 2026-09-05**: it was written
   here that "the *sign* of (5) survives, the coefficients do not." It does not.
   [[C48-kadmon-regrowth-test]] carries out the linear-renewal derivation: `W(x) = −c` on
   `(0, 1)` and `W(1) = λ`, a **step function**, so the Whittle policy is indistinguishable from
   MVT, and the comparative static is **`dGUD/dc ≤ 0`** — the opposite sign. **Saturating
   renewal is a boundary of the prediction, not a convenience**: §5's contrast is testable only
   in a system whose patches refill saturatingly, which Kadmon's does not.
2. Active intake proportional to standing crop (`λx`). Handling-time-limited foragers violate
   this.
3. Deterministic patches, stationary habitat, identical foragers, no learning, no competition,
   no predation — GUD in the Brown tradition is a *joint* measure of energetic and predation
   costs, and this model contains none of the latter.
4. Round-robin / symmetric visitation when converting a threshold into `t*`.

**Not closed.**

- **The renewal form is a boundary, not an assumption to be relaxed.** Under linear renewal the
  index is a step function and the regrowth effect vanishes or reverses ([[C48-kadmon-regrowth-test]]).
  Any test of §5 must state the measured renewal form first, and any array built for it must
  implement saturating refill and carry a linear-refill negative control.
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
  a signed comparative static, not a bounded approximation. **Measured, 2026-09-05
  ([[C45-whittle-network-sim]]): the gap is negative.** In a 20-patch network the Whittle
  policy earns −13.27% ± 0.03% against MVT-with-regrowth at the pre-registered calibration and
  −0.48% ± 0.03% when each policy is given its own rate-optimal threshold — negative in all
  twelve sweep cells. At `M = 1` the index is not merely un-bounded; it is empirically no
  better than the classical rule it generalises, and the classical rule is simpler.
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

## 9. Review response — 2026-09-05

An external review of `papers/charnov-gittins/paper.md` by an unnamed language model
(`papers/charnov-gittins/reviews/2026-09-05-gemini-flash-3.8.md`) recomputed `W(x)`, `W'(x)`,
`dGUD/dr` and the §5 table by hand and confirmed all of them. **No number in this note
changed.** Three scope clarifications were added to the paper and are mirrored here.
(Numbered §9 rather than §8 because §8 is occupied; the paper's `C25 §8` references are
unaffected.)

**1. The sparse-activation gap is now named, not just noted.** §7's "no optimality gap is
stated" stands. What is new is that the gap was searched for and is open. Weber & Weiss 1990
(`10.2307/3214547`, verified Crossref 2026-09-05) assumes `N → ∞` with the active fraction
`α = M/N` **fixed**. So do the papers that sharpen it: Hu & Frazier (arXiv:1707.00205) and
Zhang & Frazier (arXiv:2107.11911, *Beating the Central Limit Theorem*, both verified via the
arXiv API 2026-09-05) hold the pulled fraction constant, and Gast, Gaujal & Yan
(`10.1007/s11134-023-09875-x`, verified Crossref 2026-09-05 — the candidate DOI
`10.1007/s11134-022-09855-2` does **not** resolve) require activations to scale
proportionally with arms. Brown & Smith (`10.1287/mnsc.2019.3342`, verified Crossref
2026-09-05) is the nearest usable object: their Lagrangian upper bound is a **finite-`N`**
bound and is therefore evaluable at `M = 1`, but their optimality claim is again for many
items, so it would give a numerical certificate for a particular patch network rather than an
asymptotic guarantee for the index. The single-server queueing literature the reviewer
pointed at is the closest structural match to `M = 1`, but it proves heavy-traffic limits for
a system with arrivals, not an `N → ∞` limit over a fixed patch set. **Conclusion: no located
result covers `M = 1`, `α → 0`.
Foraging's own regime is uncovered, and this is open work, not an oversight.**

**2. The zero-switching-delay scope is now stated where the index is stated.** `W(x)` in §3 is
derived with no transit interval. During a transit of length `τ` every passive patch advances
by `ẋ = r(1−x)`. Because `W` is strictly increasing in `x` and the passive flow is
order-preserving on `[0,1]`, patches of a **common `r`** keep their rank across transit, so
within-type priority is untouched. Across types the advance over `τ` is `(1−x)(1−e^{−rτ})`,
which is increasing in `r`, so arrival rank can invert departure rank. And `τ` enters only
through the renewal-cycle anchor that fixes `ν`, so a mixed-`r` habitat has **one** `ν` set by
the whole network, not one per patch type — which is precisely why §5's claim is a relative,
between-type statement at fixed habitat quality. None of this supplies the missing bound; §7's
"largest hole" entry is unchanged.

**3. GUD scope.** GUD in §1 and §5 is **Charnov's** quantity: residual density at departure
under pure rate maximisation. Brown's operational GUD (Brown 1988, `10.1007/BF00395696`,
verified Crossref 2026-09-05) is the broader `H = C + P + MOC`, adding metabolic and predation
cost. Those enter this model as shifts in the shadow price `V'(x)`, not as new state. The sign
result `dGUD/dr > 0` is asserted for the Charnov quantity only. §7 assumption 3 already said
the model has no predation term; this makes the vocabulary match the assumption.

## Corrections 2026-09-05 (audit 06)

`audits/06-math-rounds3-6.md` items 6, 7 and 8. Three changes, one of them a real number.

**1. The residence-time column was computed under an arrival state the model forbids.**
§5's table caption said "residence times from an arrival at `x = 1`", but under §7 assumption 4
(round-robin visitation) a forager returning to a patch it left at `GUD` after `τ` away finds
`x_arr = 1 − (1 − GUD)e^{−rτ}`, not `x = 1`. At `r·τ = 0.2`: `GUD = 0.4019`, so
`x_arr = 0.5103` and the steady-cycle residence is `ln(0.5103/0.4019) = 0.239` against
`t*_MVT = 1.204`.

| `r·τ` | 0.00 | 0.05 | 0.10 | 0.20 | 0.50 | 1.00 | 2.00 | 5.00 | 10.00 | 50.00 |
|---|---|---|---|---|---|---|---|---|---|---|
| **old** `t*/t*_MVT` | 1.000 | 0.909 | 0.845 | **0.757** | 0.616 | 0.504 | 0.400 | 0.283 | 0.212 | 0.104 |
| **new** `t_cycle/t*_MVT` | 0.000 | 0.077 | 0.129 | **0.198** | 0.298 | 0.352 | **0.356** | 0.281 | 0.212 | 0.104 |

The headline figure moves **0.757 → 0.198**, a factor of 3.8, and the callout's "~0.76× the
MVT residence time" is now "~0.20×". The old column is retained under the honest label
`t_full` (time to deplete a full patch), which is the quantity it actually measured. The new
column is **non-monotone**, peaking at 0.356 near `r·τ = 2` — a qualitative feature the old
convention hid completely, and which changes the prediction from "residence falls with `r`" to
"residence is short at every `r`, never above ~36% of MVT". §5's sign sentence is requalified
accordingly, and the same correction is propagated to `papers/charnov-gittins/paper.md`
Table 1 (`t*` column, caption, and the one sentence under eq. (6) that described it).

**2. §3's "independent confirmation" was circular and is withdrawn.** `V'(x) = 1 − x` is
obtained by substituting `ν = W(x)` into (2) at every `x`, i.e. by asserting indifference
everywhere — that is the *definition* of the Whittle index, not a check on it, so
re-substituting it into (1) reproduces (3) trivially. Worse, `V(x) = x − x²/2` is not a value
function at all: the active branch of (1) gives `λx − λx(1−x) = λx²`, which varies with `x` and
cannot equal a constant gain `ρ`, and each `ν` carries its own `V`. §3 now states the
substitution as a consistency check and marks the "room left to grow" shadow-price story as an
interpretive gloss, not a derived result.

**3. `W(x)` and `dGUD/dr` are unaffected, and this was re-verified.** The defect is entirely in
the *conversion of a threshold into a residence time*; the arrival state enters nowhere in the
derivation of the index or the comparative static. `W(x) = λx² − r(1−x)²` comes from
`∂ρ/∂a = 0` on the singular arc, `W'(x) = 2λx + 2r(1−x) > 0` gives indexability, eq. (4)'s
closed-form `GUD(ρ)` solves `W(x) = ν` at `ν = λu₀²`, and eq. (5)'s
`dGUD/dr = (1−GUD)²/(2[λ·GUD + r(1−GUD)])` follows by implicit differentiation of the same
equation. Re-running `vault/_scripts/c25_whittle.py` after the fix reproduces the `GUD(r)`,
`ΔGUD` and `GUD/GUD_MVT` columns **digit for digit**, the 0.8167 small-`r` slope, both limits
and the zero monotonicity violations. **The note's headline result — the index, its
unconditional indexability, and the strictly positive `dGUD/dr` — survives intact.** So does
the falsifiable statement in §5, which is a claim about `ΔGUD` across patch types and never
depended on the residence column.

**Scope of the §9 review response.** §9's "No number in this note changed" recorded the outcome
of the 2026-09-05 external review, which recomputed `W`, `W'`, `dGUD/dr` and the table under
the *then-current* arrival convention and reproduced them. That review did not question the
convention. This correction supersedes it for the residence column only; §9's three scope
clarifications are unaffected.

## 10. Network simulation 2026-09-05 — [[C45-whittle-network-sim]]

The §5 rule was run forward as a policy on a complete graph of `N = 20` patches (10 fast, 10
slow, uniform travel `τ`, `λ = 1`, `G_max = 1`, dynamics exactly §1), against a hashed
pre-registration. Nothing in §1–§4 changes: `W(x) = λx² − r(1−x)²` is still the Whittle index of
the relaxed single-arm problem, still unconditionally indexable, still reduces to C5 eq. (4)
under non-revisitability. What changes is what §5 and §7 may claim.

**1. The sign survives; the magnitude is a calibration.** Fast patches are abandoned at a
strictly higher standing crop in every cell (the CI excludes 1). But the ratio sweeps 1.02 →
1.66 as the habitat subsidy `ν` is moved. At this note's own anchor, `ν = λ·GUD_MVT² = 0.09`,
the network returns `GUD_fast = 0.3987` against §5's single-patch **0.4019 — 0.8%** — and a
ratio of **1.2708 ± 0.0002**. At the pre-registered calibration (`ν` learned as the realised
long-run intake rate, converging to 0.2732) the ratio is **1.0600 ± 0.0002**. §7's "`ν` is
anchored, not solved" is therefore not a bookkeeping caveat: it is the largest term in the
predicted effect size. **The 1.34× must always be read as "1.34 at the MVT anchor".**

**2. For P-067.** Expected effect size **~1.27 at the anchor, ~1.06 with `ν` learned**; power
the test for the low end. Usable window `r_fast·τ ∈ [0.2, 1]` (ratio ~1.27 down to ~1.23 at the
anchor). At `r_fast·τ = 10` the forager makes **zero slow-patch visits** in every scored run at
every `τ`, so the contrast is undefined — a design that maximises regrowth contrast to maximise
signal destroys the measurement. MVT-with-regrowth is genuinely type-blind under one habitat
rate (ratio 0.996–1.000 in all twelve cells), so it remains the correct null and a measured
ratio indistinguishable from 1.00 is a clean negative.

**3. The harder fact: the index does not out-earn Charnov's rule.** Against MVT-with-regrowth in
the same network the Whittle policy earns **−13.27% ± 0.03%** at the pre-registered calibration
and **−0.48% ± 0.03%** when each policy is given its own post-hoc rate-optimal threshold —
negative in **all twelve** sweep cells (−11.7% to −45.9%). And the intake-optimal Whittle
threshold (`ν* = 0.030`) is not the C25-predicted policy: it yields a fast/slow GUD ratio of
1.659, outside the predicted band in the other direction.

**What this does to the framing.** The "value of the index" reading — that a forager using `W`
does better than one using `R*` — is **dropped**. It was never derived here (§7: no optimality
gap is stated) and it is now measured to be false in the one network where it has been checked.
What survives is what the derivation actually supports: the index exists and is exact for the
relaxed arm; `dGUD/dr > 0` (eq. 5) is a signed comparative static; and the **between-type GUD
contrast** is the observable. The Whittle rule is a *description of the optimal single-patch
departure rule*, not a better foraging policy.

**4. Two side results.** §5's homogeneous-habitat degeneracy is confirmed exactly — 100.00%
destination agreement with fullest-greedy at `r·τ = 0.05, 0.2, 1, 10` — and is worse than
stated: "visit the fullest" carries no leaving rule and earns **3.1% of MVT's rate**, so the
referee attack §7 anticipates is answered by noting the destination half alone is nearly
worthless. §9 item 2's transit reordering is measured for the first time: it fires on 12–34% of
departures and rises with `τ`.

**What the simulation does not settle.** It tests the rule, not the animal; no forager was
observed. `ν` is still learned, not solved — the principled object (the subsidy at which the
relaxed problem has active fraction `1/N`) was not computed. `dt` was not varied. Stochastic
patches, competitors and handling-time-limited intake are all §7 assumptions and none was
relaxed.
