# Blind brief — C45: the Whittle patch index run forward in a mixed-`r` network

**Written 2026-09-05, BEFORE `vault/_scripts/c45_whittle_sim.py` existed and before any
simulated forager took a step.** Purpose: programme item P-053 asks whether the C25 index
survives being *run as a policy* in a network with transit, one habitat subsidy, and finite
`N`. A derivation that only ever solves its own single-patch equation cannot be wrong. This
brief fixes the predictions, the pass/fail thresholds, and the design, so that the simulation
can return a number that contradicts them.

**Blindness is partial, and the limit is stated.** The author has read
[[C25-whittle-foraging]] in full and therefore knows the single-patch table: `GUD_MVT = 0.30`,
`GUD/GUD_MVT = 1.34` at `r·τ = 0.2`, `1.12 / 1.34 / 1.82 / 2.58` at `r·τ = 0.05 / 0.2 / 1 / 10`,
and the corrected `t_cycle` column (0.198 at `r·τ = 0.2`, non-monotone, peak 0.356 near
`r·τ = 2`). Those are the **priors**, and they are exactly what the network is being asked to
break. Nothing about the network — no policy trajectory, no long-run rate, no simulated GUD —
has been computed or inspected. No line of the simulator has been written.

## 1. Design, fixed in advance

Complete graph, `N = 20` patches, uniform travel time `τ` between any pair. Ten patches of a
**fast** type and ten of a **slow** type, matched in `G_max = 1` and in `λ = 1`, differing only
in regrowth `r`. Baseline: `r_fast·τ = 0.2`, `r_slow·τ = 0.02`, `τ = 1/λ`.

Dynamics exactly C25 §1: active `ẋ = −λx` with intake rate `λx`; passive `ẋ = r(1−x)`.
Discrete time, step `dt`, forward Euler on the exact exponentials (`x ← x·e^{−λ dt}` active,
`x ← 1 − (1−x)e^{−r dt}` passive), so the discretisation error is in *when* a decision is taken,
not in the flow.

Four policies, all sharing one habitat-level scalar learned by fixed-point iteration on the
realised long-run intake rate:

- **(a) Whittle.** Leave the current patch when `W(x) = λx² − r(1−x)²` falls below the habitat
  subsidy `ν`. Move to `argmax_j W_j(x_j^arr)` with `x_j^arr = 1 − (1−x_j)e^{−r_j τ}` — the
  index evaluated at the state the patch will actually be in on arrival, i.e. net of travel.
- **(b) MVT-with-regrowth.** Leave when the marginal intake `λx` falls below `R*`, the network's
  learned long-run rate. Destination by fullest-at-arrival, because MVT names no destination
  rule.
- **(c) Fullest-greedy.** Leave when the current patch is no longer the fullest at arrival;
  destination `argmax_j x_j^arr`.
- **(d) Random.** Residence drawn uniform on `(0, 2·t*_MVT)`, destination uniform over the
  other 19 patches.

Run to stationarity, 20 seeds; burn-in and run length are stated in the script and the note.
Sweep `r_fast·τ ∈ {0.05, 0.2, 1, 10}` at **fixed absolute `r_slow = 0.02λ`**, and
`τ ∈ {0.5, 1, 2}·(1/λ)`.

## 2. Predictions

> **(P1 — the headline.)** Under the Whittle policy the long-run giving-up density on fast
> patches is ≈ **1.34× `GUD_MVT`** and on slow patches ≈ **1.03×**, so the **fast/slow GUD
> ratio ≈ 1.30 ± 0.10**. PASS if the measured ratio's 95% CI overlaps [1.20, 1.40]; FAIL
> otherwise. A ratio whose CI excludes 1.0 but lies outside the band is a **partial pass**: the
> sign transfers, the magnitude does not.

> **(P2 — the negative control.)** Under a single network `ν`, MVT-with-regrowth gives **equal**
> GUD on both types: fast/slow ratio = 1.00. PASS if the CI contains 1.00 and its half-width is
> below 0.02. This is close to a tautology given the leave rule `λx = R*`; it is included
> because if it fails, the harness is broken, not the theory.

> **(P3 — transit reordering.)** The identity of the best-indexed patch flips *type* across a
> transit in a strictly positive fraction of cycles, and that fraction **increases with `τ`**
> over `τ ∈ {0.5, 1, 2}/λ`. PASS if the fraction is monotone increasing in `τ` at the baseline
> `r_fast`; FAIL if flat or decreasing.

> **(P4 — the value of the index.)** The Whittle policy's long-run intake rate exceeds
> MVT-with-regrowth's by a margin in **2–10%**, at the baseline. PASS if the point estimate
> lies in [2%, 10%]; a positive margin outside the band is a partial pass; a margin whose CI
> contains zero or is negative is a FAIL of P4 and would say the index buys nothing.

> **(P5 — the degeneracy.)** With `N` **identical** patches the Whittle destination rule agrees
> with fullest-greedy on ≥ 99% of moves. PASS on that agreement fraction. The brief predicts
> further that the homogeneous GUD then tracks the single-patch `GUD(r)` curve rather than being
> `r`-independent, because `ν` is itself learned from the habitat — this sub-clause is stated so
> that the note cannot later claim whichever outcome appears.

## 3. What would falsify the transfer

A fast/slow GUD ratio of 1.00 within CI under the Whittle policy — the index prescribing
type-blind departure once it is embedded in a network — falsifies P-067's field test before it
is run. A **negative** value-of-the-index margin (P4) would say the C25 index is a worse policy
than the MVT rule it claims to generalise, which would be a result against C25 rather than for
it. Neither outcome is retracted after the fact; both are reported.

## 4. Analysis, fixed in advance

Per-seed statistics; across the 20 seeds a Student-`t` 95% CI on the per-seed ratio and on the
per-seed intake margin. No seed is dropped. No policy is re-tuned after its numbers are seen.
`dt`, burn-in and run length are fixed before the first production run and are not changed to
move a number.
