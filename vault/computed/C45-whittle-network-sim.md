---
name: C45-whittle-network-sim
type: computed
exit: prediction
extends-to: [ecology, conservation]
---

# The Whittle patch rule, run forward in a network: the sign survives, the magnitude is a calibration, and the index loses to MVT on intake

> **PRE-REGISTERED, 3 of 5 PREDICTIONS FAIL. Fast/slow GUD ratio = 1.0600 ± 0.0002 (P1
> predicted 1.30 ± 0.10) — FAIL. The sign transfers (the CI excludes 1) and nothing else does.
> The ratio is not a property of the index: it sweeps 1.02 → 1.66 as the habitat subsidy `ν`
> is moved, and at [[C25-whittle-foraging]]'s own anchor `ν = λ·GUD_MVT² = 0.09` it is
> 1.2708 ± 0.0002 with `GUD_fast = 0.3987` against C25's single-patch 0.4019 — 0.8%. And the
> value of the index is negative: the Whittle policy earns −13.27% ± 0.03% against
> MVT-with-regrowth at the pre-registered calibration and −0.48% ± 0.03% when each policy is
> given its own rate-optimal threshold. P4 FAILS in the direction that costs C25 something.**

Programme item P-053. Pre-registered by `audits/blind-brief-c45-2026-09-05.md`, sha256
`fbc48359b5215f6a3f2c4f6cefee4ce7a73257c7c8121c33ef8615f0d49714a7`, written and hashed before
`vault/_scripts/c45_whittle_sim.py` existed. Re-run: `python _scripts/c45_whittle_sim.py` from
`vault/`.

---

## 1. What was run

Complete graph, `N = 20` patches (10 fast, 10 slow), uniform travel `τ` between any pair,
`λ = 1`, `G_max = 1`, dynamics exactly [[C25-whittle-foraging]] §1. Discrete time, `dt = 0.01`,
exact exponential flow per step (`x ← x·e^{−λ dt}` active, `x ← 1 − (1−x)e^{−r dt}` passive),
so the discretisation error is in *when* a decision is taken, not in the flow. Burn-in 200 time
units discarded, 1000 scored, 20 seeds, no seed dropped. Baseline `r_fast·τ = 0.2`,
`r_slow·τ = 0.02`, `τ = 1/λ`. Sweep `r_fast·τ ∈ {0.05, 0.2, 1, 10}` at fixed absolute
`r_slow = 0.02λ`, `τ ∈ {0.5, 1, 2}/λ`. CIs are Student-`t` 95% across the 20 seeds.

Four policies. Each of the two threshold policies carries **one** habitat scalar, learned by a
damped fixed point on the realised long-run intake rate (`ν ← (ν + R̂)/2`, 8 iterations, short
runs, one seed; the converged value is then **frozen** for the 20 production seeds). Destination
is `argmax_j` of the policy's own criterion evaluated at `x_j^arr = 1 − (1−x_j)e^{−r_j τ}` —
the state the patch will actually be in on arrival, which is what "net of travel" means here.

## 2. Table 1 — baseline, four policies

`r_fast·τ = 0.2`, `r_slow·τ = 0.02`, `τ = 1/λ`. `flip` is the fraction of departures at which
the highest-indexed patch *now* and the highest-indexed patch *at its arrival state* belong to
different types.

| policy | `ν`/`R*` | intake rate | `GUD_fast` | `GUD_slow` | `res_fast` | `res_slow` | flip | fast/slow ratio |
|---|---|---|---|---|---|---|---|---|
| **whittle** | 0.2732 | 0.2735 ± 0.0001 | 0.5562 | 0.5247 | 0.571 | 0.628 | 0.274 | **1.0600 ± 0.0002** |
| **mvt** | 0.3141 | **0.3154 ± 0.0001** | 0.3115 | 0.3123 | 1.159 | 1.156 | 0.182 | 0.9975 ± 0.0002 |
| **fullest** | — | 0.0098 ± 0.0000 | 0.9888 | 0.9888 | 0.010 | 0.010 | 0.566 | 1.0000 ± 0.0000 |
| **random** | — | 0.2161 ± 0.0024 | 0.3581 | 0.2176 | 1.209 | 1.230 | 0.000 | 1.6512 ± 0.0585 |

**MVT-with-regrowth wins on intake.** Whittle vs MVT, paired by seed: **−13.27% ± 0.03%**.
Whittle vs random: +26.65% ± 1.44%. Whittle vs fullest: +2679% — see §5.

## 3. The sweep

Whittle rows; MVT's ratio is 0.996–1.000 in every cell and is omitted. `n_slow` is the mean
number of slow-patch departures per scored run.

| `τ` | `r_fast·τ` | `GUD_fast` | `GUD_slow` | ratio | ± | flip | rate | `n_slow` |
|---|---|---|---|---|---|---|---|---|
| 0.5 | 0.05 | 0.5685 | 0.5579 | 1.0189 | 0.0000 | 0.457 | 0.3117 | 185 |
| 0.5 | 0.20 | 0.6451 | 0.6119 | 1.0542 | 0.0003 | 0.119 | 0.3733 | 56 |
| 0.5 | 1.00 | 0.7118 | 0.5827 | 1.2214 | 0.0000 | 0.082 | 0.3437 | 10 |
| 0.5 | 10.0 | 0.8437 | — | **undefined** | — | 0.000 | 0.2334 | **0** |
| 1.0 | 0.05 | 0.4816 | 0.4737 | 1.0167 | 0.0000 | 0.241 | 0.2207 | 186 |
| 1.0 | 0.20 | 0.5562 | 0.5247 | **1.0600** | 0.0002 | 0.274 | 0.2735 | 59 |
| 1.0 | 1.00 | 0.6250 | 0.5066 | 1.2337 | 0.0000 | 0.119 | 0.2557 | 10 |
| 1.0 | 10.0 | 0.7866 | — | **undefined** | — | 0.000 | 0.1720 | **0** |
| 2.0 | 0.05 | 0.3993 | 0.3973 | 1.0052 | 0.0000 | 0.000 | 0.1550 | 163 |
| 2.0 | 0.20 | 0.4623 | 0.4360 | 1.0603 | 0.0002 | 0.337 | 0.1887 | 61 |
| 2.0 | 1.00 | 0.5326 | 0.4274 | 1.2461 | 0.0000 | 0.154 | 0.1783 | 10 |
| 2.0 | 10.0 | 0.7118 | — | **undefined** | — | 0.000 | 0.1231 | **0** |

Value of the index (Whittle rate / MVT rate − 1) is **negative in all twelve cells**: −15.2 /
−11.7 / −18.9 / −45.0% at `τ = 0.5`; −16.2 / −13.3 / −19.6 / −45.9% at `τ = 1`; −15.5 / −13.8 /
−19.7 / −44.5% at `τ = 2`. Every CI half-width is ≤ 0.06%.

**A design constraint P-067 does not currently state.** At `r_fast·τ = 10` the forager visits
slow patches **zero times** in every scored run at every `τ`. The between-type GUD contrast is
then not small, it is *undefined* — a field test at a large regrowth contrast will collect no
slow-patch departures at all. The ratio is measurable only at modest contrast, and it is
smallest exactly there.

## 4. Pass/fail against the hashed brief

| | prediction | measured | verdict |
|---|---|---|---|
| **P1** | fast/slow GUD ratio 1.30 ± 0.10, CI overlapping [1.20, 1.40] | **1.0600 ± 0.0002** | **FAIL** |
| **P2** | MVT ratio = 1.00, CI containing 1.00, half-width < 0.02 | 0.9975 ± 0.0002 | **FAIL on the letter, pass on the substance** |
| **P3** | type-flip fraction > 0 and increasing in `τ` | 0.119 → 0.274 → 0.337 | **PASS** |
| **P4** | Whittle beats MVT on intake by 2–10% | **−13.27% ± 0.03%** | **FAIL, wrong sign** |
| **P5** | homogeneous destination agreement ≥ 99% | **100.00%** at all four `r` | **PASS** |

**P1.** The brief's own partial-pass clause applies to the sign only: the CI excludes 1.0, so
faster-regrowing patches *are* abandoned at a higher standing crop, as C25 §5 says. The
magnitude is 1.06, not 1.34. §5 locates why, and it is not the network.

**P2.** The brief asked for a CI *containing* 1.000. The measured CI is [0.9973, 0.9977] and
misses it by 0.25%. That shortfall is the `dt` overshoot — departure fires at the first step
after `λx` crosses `R*`, and the two types are sampled at different visit frequencies (fast
patches take ~87% of departures) — and across the sweep the MVT ratio runs 0.9961–1.0000 with
no dependence on `r`. The substantive claim is confirmed: **under one network `ν`,
MVT-with-regrowth is type-blind.** The criterion is recorded as failed rather than widened
after the fact.

**P5.** In a homogeneous network the Whittle destination rule and fullest-greedy chose the
**same** patch on 100.00% of moves at `r·τ = 0.05, 0.2, 1, 10` — C25 §5's degeneracy, confirmed
exactly. The brief's sub-clause is also confirmed and the "GUD independent of `r`" reading is
falsified: homogeneous GUD is 0.5057 / 0.5594 / 0.6250 / 0.7866 at those four `r`, rising with
`r` as C25 eq. (5) requires, because `ν` is itself learned from the habitat.

## 5. Why the network differs from C25's single-patch table — and the one line that reconciles them

Three candidate causes were named in advance: one `ν`, transit reordering, finite `N`. **Only
the first matters, and it is not a network effect at all — it is a calibration.**

C25 §5 anchors the habitat index at the MVT baseline, `ν = λ·GUD_MVT² = 0.09`. The brief
pre-registered `ν` as the *learned long-run intake rate*, which the fixed point returns as
**0.2732** — three times larger. Re-run the identical baseline cell at C25's own anchor:

| `ν` | source | `GUD_fast` | C25 single-patch | `GUD_slow` | ratio | rate vs MVT |
|---|---|---|---|---|---|---|
| 0.0900 | **C25 §5 anchor** | **0.3987** | **0.4019** | 0.3138 | **1.2708 ± 0.0002** | −1.69% |
| 0.2732 | learned long-run rate (pre-registered) | 0.5562 | — | 0.5247 | 1.0600 ± 0.0002 | −13.27% |
| 0.030 | post-hoc rate-optimal | 0.3403 | — | 0.2051 | 1.6592 ± 0.0004 | −0.48% |

**C25's single-patch number survives the network to 0.8%** — 0.3987 against 0.4019 — once the
subsidy is the one C25 actually used. The slow-patch value, 0.3138, is likewise within 0.8% of
C25's small-`r` expansion at `r·τ = 0.02` (`0.300 + 0.817 × 0.02 = 0.3163`). The ratio at that
anchor, 1.2708, falls **inside** the brief's [1.20, 1.40] band. P1 still fails, because the
brief fixed the calibration in advance and the pre-registered calibration is the one that
counts — but the failure is located precisely, and it is a failure of the C25 §7 hole "`ν` is
anchored, not solved", not of the index.

The other two causes are real but small. **Transit reordering** fires on 12–34% of departures
and rises with `τ` (P3), which is C25 §9 item 2 measured for the first time; it perturbs the
route, not the threshold, because the departure rule compares `W(x_cur)` to `ν` alone.
**Finite `N`** shows up as the visit imbalance — 87% of departures are from fast patches at the
baseline, and 100% at `r_fast·τ = 10`.

## 6. The sharper question: the value of the index

Comparing two threshold policies at two differently-chosen thresholds measures the thresholds,
not the rules. So each policy was given its own rate-optimal threshold by a post-hoc grid search
over `ν ∈ {0, 0.01, …, 0.6}` (three seeds, short runs), then re-run on the 20 production seeds.
This search is **not pre-registered** and is labelled as such.

- Whittle at `ν* = 0.030`: rate **0.3138**
- MVT-with-regrowth at `R* = 0.300`: rate **0.3153**
- **Value of the index = −0.48% ± 0.03%.**

**The number a field study could aim at is approximately zero, and the sign is against the
index.** In this network, under this model, the Whittle rule buys nothing over the Charnov
rule in intake, and buys −13% if you calibrate its subsidy the obvious way. Note what the
rate-optimal Whittle threshold does to the *observable*: at `ν* = 0.030` the fast/slow GUD ratio
is **1.659**, far outside the brief's band in the other direction. The intake-optimal policy and
the C25-predicted policy are not the same policy.

This does not overturn C25's derivation. `W(x) = λx² − r(1−x)²` is still the Whittle index of
the relaxed single-arm problem, still unconditionally indexable, and still reduces to C5 eq. (4)
under non-revisitability. What C45 says is that C25 §7's third hole — "no optimality gap is
stated" — is not an abstract caveat. Run at `M = 1` active arm among `N = 20`, the regime
Weber–Weiss does not cover, the index is not merely un-bounded, it is **empirically no better
than the classical rule it generalises**, and the classical rule is simpler.

## 7. A fourth result: "visit the fullest" is not a policy

Fullest-greedy earns **0.0098 ± 0.0000**, 3.1% of MVT's rate, with a residence time of exactly
one `dt`. It arrives at the patch that was fullest at departure, finds that during transit some
other patch has overtaken it, and leaves immediately — forever. It starves.

This sharpens C25 §5's degeneracy statement in a way the note does not currently say. The
degeneracy is real (P5: 100% destination agreement) but it is a statement about the
**destination** rule only. "Visit the fullest" supplies no leaving rule, and a foraging policy
is a leaving rule with a destination attached, not the reverse. The referee attack C25 §7
anticipates — *your index is just "go to the fullest patch", which everyone already does* — is
answered by this row: the destination half is indeed degenerate, and the destination half alone
is worth 3% of the achievable rate.

## §8 Honesty

**The simulation tests the rule, not the animal.** Every row above is a statement about a
deterministic policy in a deterministic model. No forager was observed. A real bee that fails
to reproduce these ratios has falsified nothing here.

**`ν` is learned, not solved.** The pre-registered calibration (fixed point on the realised
intake rate) is a *choice*, and §5 shows the headline observable is more sensitive to that
choice than to anything else in the design. The principled object — the subsidy at which the
relaxed problem has active fraction `1/N` — was not computed. Until it is, "the Whittle GUD
ratio" is not a single number, and C25 §5's 1.34 should be read as "1.34 *at the MVT anchor*",
which is what C25 says but not what its callout emphasises.

**`dt` discretisation.** All thresholds fire at the first step past the crossing. This is the
whole of P2's 0.25% letter-failure and is worth ≤ 0.5% on any GUD here. It was not varied; a
`dt` halving check is not run and should be.

**The degeneracy is confirmed and is worse than stated.** 100% destination agreement in a
homogeneous network (P5), and the destination rule alone is nearly worthless (§7).

**Two things this does not settle.** Whether some other network calibration of `ν` makes the
index beat MVT — the grid search says no over `[0, 0.6]` at the baseline cell, but only there.
And whether stochastic patches, competitors, or a handling-time-limited intake change the
ordering; all three are C25 §7 assumptions and none was relaxed.

**What P-067 needs from this, concretely.** (i) The **expected effect size is the C25-anchor
number, 1.27**, not 1.34, and the network shifts it by under 1% — so a field test should be
powered for a fast/slow GUD ratio of ~1.27 at `r_fast·τ = 0.2`. (ii) The contrast must be
**modest**: at `r_fast·τ = 10` the slow type receives zero visits and the ratio is undefined,
so a design that maximises the regrowth contrast to maximise the signal destroys the
measurement. `r_fast·τ ∈ [0.2, 1]` is the usable window, giving a predicted ratio between
~1.27 and ~1.23 at the anchor. (iii) MVT-with-regrowth remains the correct null and it is
genuinely type-blind under one habitat rate (P2), so a measured ratio indistinguishable from
1.00 is a clean negative. (iv) P-088's artificial-flower array should record **visit counts per
type**, not only departure densities: the visit imbalance (87:13 at the baseline) is itself a
prediction of the index and is easier to measure than a giving-up density.

Script: `vault/_scripts/c45_whittle_sim.py` (stdlib only).
Brief: `audits/blind-brief-c45-2026-09-05.md`.
