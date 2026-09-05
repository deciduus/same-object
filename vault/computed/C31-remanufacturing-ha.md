---
name: C31-remanufacturing-ha
type: computed
exit: computation
extends-to: [circularity, sustainability]
next-step-cost: S
---
# Ha for a remanufactured product fleet

> **A remanufacturing system is a repairable population with a computable `Ha = k_r/k_d`, and
> its `A` is the fraction of the installed base in service. But C6's `A = Ha/(1+Ha)` is wrong
> here: with a core return rate `r < 1` it becomes `A = Ha/(Ha + r)`. And the axis stays empty
> anyway — of the two numbers `Ha` needs, published remanufacturing gives one. Return rates and
> product lifetimes are everywhere; the mean core out-of-service time is in no source reached.**

Narrows [[G33-repair-ratio-remanufacturing]]. Extends [[C6-damage-healing-ratio]]'s axis with a
product-fleet row of the kind [[C1-availability-living-tissue]] §3.2 added for wind turbines.
Arithmetic re-runnable: `python _scripts/c31_ha.py` from `vault/`.

---

## 1. The quantity, in remanufacturing's own variables

```
k_d  ≡  1/L   exit rate of a unit in service        [L = mean in-service life]
k_r  ≡  1/T   restore rate of a unit out of service [T = mean core out-of-service time]
Ha   ≡  k_r/k_d  =  L/T
```

`T` runs from the moment a unit leaves service to the moment its remanufactured self re-enters:
collection, inspection, disassembly, reprocessing, redistribution, shelf. It is the fleet's
`MTTR` and nothing else, so [[C6-damage-healing-ratio]] §3.3's `Ha = MTBF/MTTR` transfers with
no new assumption. The remanufacturing literature's **Cycle Time** and **Lead Time** are both
*parts* of `T`, never the whole of it (Graham et al. 2015, DOI `10.1186/s13243-015-0019-2`,
open-access PDF fetched 2026-09-05 — its KPI toolbox has both, plus salvage rates, and no ratio).

**Bounds.** `Ha ∈ (0, ∞)`, `A ∈ (0, 1)`, and `A` is the fraction of the installed base in
service — the **population functional fraction** column of C1 §1, not the unit-availability
column. A fleet is genuinely `N` discrete units, so unlike bone this is a legitimate population
reading.

## 2. Inputs

| # | Input | Value | Source, fetched 2026-09-05 |
|---|---|---|---|
| 1 | Offshore wind turbine failure rate λ | 8.27 /turbine/yr | Carroll, McDonald & McMillan 2016, *Wind Energy* 19:1107–1119, DOI `10.1002/we.1887`, Table 2 — via [[C1-availability-living-tissue]] §3.2, **VERIFIED-PRIMARY** |
| 2 | Offshore wind turbine MTTR | 12.06 h (⇒ MTBF 1,047 h) | same |
| 3 | EV battery mean life `L` | **10 yr** (central; 12 yr alternative) | Huster, Rosenberg, Glöser-Chahoud & Schultmann 2023, *J. Remanufacturing* 13:283–304, DOI `10.1007/s13243-023-00130-3`, open access, PDF fetched and text-extracted. Scenarios BF10/BD10 (σ = 2 yr) / BF12 |
| 4 | EV battery core return rate `r` | **0.50 / 0.75 / 1.00**; RD75 = U(0.65, 0.85); expert elicitation "more than 50%" | same |
| 5 | Trabecular bone revisit / down | 730 d / 200 d and 35 d | [[C6-damage-healing-ratio]] §5, durations VERIFIED |
| 6 | **Core out-of-service time `T`, any fleet** | **NOT PUBLISHED** | see §4 |
| 7 | Cat Reman take-back | 140 million lb (2022); >150 million lb/yr | caterpillar.com sustainability pages via search snippets, 2026-09-05 — **UNVERIFIED** (page fetch timed out) and in any case **mass with no unit denominator**: see §4 |
| 8 | Kodak single-use camera US return rate | "84%, up from 75%" | search snippet only, **no primary source obtained — UNSOURCED, not used below** |
| 9 | Guide 2000 survey's own return figures | — | **NOT OBTAINED**, Wiley paywall |

## 3. The derivation that changes C6's formula

C6's two-state chain has no exit: every failed unit is repaired. A product fleet has two exits —
cores that never come back, and returned cores that fail the quality gate. Write `S` in service,
`O` out of service in the reverse pipeline, `X` lost (absorbing); `r` = fraction of exits
collected as cores, `y` = remanufacturing yield.

```
S --k_d·r--> O        S --k_d·(1−r)--> X
O --k_r·y--> S        O --k_r·(1−y)--> X
```

**With `X` absorbing and `r·y < 1` there is no interior steady state at all** — the population
drains, and the only fixed point is the empty fleet. This is the exact structural mirror of C6
§4.2's finding that continuum damage-healing mechanics has no steady state because healing is a
*ratchet*; here there is none because return is a *drain*. A remanufacturing fleet only has an
`A` because **new production replenishes it**, at rate `q` per year.

Balance on `O` at steady state: `k_r N_O = r k_d N_S`, so `N_O = r N_S / Ha`, and

```
A  =  N_S/(N_S + N_O)  =  Ha/(Ha + r)                                   (★★)
```

which reduces to C6's `A = Ha/(1+Ha)` **iff `r = 1`**. Balance on `S` gives the replenishment
`q = k_d N_S (1 − r y)`, i.e. new production is needed in exact proportion to the loop's leak.

**Erlang-B reading.** C6 §1.1 maps `ρ = 1/Ha` to the offered load of an M/M/1/1 loss system.
That survives here with the arrival stream thinned by `r`: the effective offered load is
`ρ_eff = r/Ha`, and `1 − A = ρ_eff/(1+ρ_eff)` is still the one-server blocking probability. A
low return rate does not make the fleet *unavailable*; it makes the pipeline *emptier* and the
factory busier. That is a genuinely counter-intuitive consequence of (★★), and it is why `A`
alone can never diagnose a circularity failure.

## 4. Result — the axis, with the reman rows empty and the reason stated

`Ha = L/T`. `A` from (★★). `ρ_eff = r/Ha`. Computed by `_scripts/c31_ha.py`.

| System | `k_d` | `k_r` | `r` | **Ha** | **A** | `ρ_eff` | Status |
|---|---|---|---|---|---|---|---|
| US grid, excl. major events | SAIFI 1.043/yr | MTTR 2.01 h | 1 | **≈4,400** | 0.99977 | 2.3e-4 | VERIFIED, C6 §5 |
| **Offshore wind turbine fleet** | **8.367 /yr** | **726.4 /yr** | **1** | **86.8** | **0.9886** | **0.0115** | **VERIFIED-PRIMARY**, computed here from C1 §3.2 |
| Trabecular bone, resorption-only down | 0.525 /yr | 10.43 /yr | 1 | **19.9** | 0.9520 | 0.050 | VERIFIED durations, C6 §5 |
| PSII, community mean, 20 °C | 2.70e-4 /s | 20.4e-4 /s | 1 | **7.56** | 0.883 | 0.132 | VERIFIED-PRIMARY, C1 §2 |
| Trabecular bone, full cycle down | 0.689 /yr | 1.825 /yr | 1 | **2.65** | 0.7260 | 0.377 | VERIFIED durations, C6 §5 |
| PSII, 5 °C cold stress | 3.11e-4 /s | 2.82e-4 /s | 1 | **0.91** | 0.476 | 1.10 | VERIFIED-PRIMARY |
| **EV battery fleet, Germany 2022–32** | 0.100 /yr (`L` = 10 yr) | **`T` not published** | 0.50–1.00 | **—** | **—** | — | **GAP.** Row 6 of §2 |
| **Cat Reman, heavy equipment** | mass only | mass only | — | **—** | **—** | — | **GAP — no unit denominator.** §2 row 7 |
| **Automotive core exchange** | not published as a fleet rate | not published | — | **—** | **—** | — | **GAP.** No source reached pairs `L` and `T` |

**The wind-turbine row is the load-bearing new number**: `Ha = 86.8` from λ = 8.27/yr and
MTTR = 12.06 h, reproducing C1's `A = 0.98861` exactly on C6's axis. It is a **repairable
product fleet** — the closest thing the vault now has to a remanufacturing row, and it sits
between bone and the grid.

**Three remanufacturing rows are deliberately empty, and the absence is the measurement**, in
the same sense as C6's two empty polymer rows. What is missing is not a formalism and not a
return rate. It is `T`. Caterpillar publishes a **mass** flow with no installed base; Huster et
al. publish `L` and `r` and forecast *quantities* rather than balance a *stock*; the field's own
KPI list (Graham et al. 2015) has Lead Time and Cycle Time but neither is the full out-of-service
residence time. **`Ha` for a remanufactured fleet is one ERP query away and has never been run.**

### Where the row would land — sensitivity, not data

`L` = 10 yr (input 3), `T` swept. **These are not measurements.**

| `T` | **Ha** | `A` at `r`=1 | `A` at `r`=0.75 | `A` at `r`=0.50 |
|---|---|---|---|---|
| 1 month | 120.0 | 0.9917 | 0.9938 | 0.9959 |
| 3 months | 40.0 | 0.9756 | 0.9816 | 0.9877 |
| 6 months | 20.0 | 0.9524 | 0.9639 | 0.9756 |
| 12 months | 10.0 | 0.9091 | 0.9302 | 0.9524 |
| 24 months | 5.0 | 0.8333 | 0.8696 | 0.9091 |

A plausible reman fleet lands at `Ha` ≈ 5–120, i.e. **straddling trabecular bone (19.9) and the
offshore wind fleet (86.8)** and below the grid by one to three orders of magnitude. The
measurement therefore has to resolve `T` to better than a factor of ~2 to place the row, which
is an easy target.

### C6's four conditions, checked

| | Condition | Remanufactured fleet |
|---|---|---|
| C1 | independent quantised units / ensemble mean | **PASSES.** A fleet is `N` discrete units; this is a cleaner population than bone and as clean as PSII |
| C2 | constant hazard, first-order in the state | **FAILS.** Product exit is wear-out plus obsolescence (Weibull β > 1 — [[C18-durability-axis]], [[C27-product-lifespan-beta]]), and reman restoration is **capacity-limited**, not first-order in the number of cores waiting. `k_r` is a throughput ceiling, not a hazard |
| C3 | no coupling between units | **PARTIAL.** Units do not interact physically, but they queue for one shared reman capacity, which couples them exactly as C3 forbids |
| C4 | stationary loading | **FAILS for a growing fleet.** The EV-battery case is explicitly a new market: returns lag sales by a full lifetime, so 2022–2032 has no steady state. It is why Huster et al. forecast instead of balancing |

**Verdict: two of four fail, both for the same reason — a young, capacity-constrained fleet.
Both are recoverable by choosing a *mature, stationary* product class** (automotive cores,
heavy-equipment components), where sales have been flat for decades and reman capacity is not
the binding constraint. That is a selection criterion for the closing measurement, and it is the
concrete thing this note contributes to the next step.

## 5. The prediction

Every unit-year of service is supplied either by a new unit or by a remanufactured one. At
steady state with a constant installed base, exits are `k_d N_S` per year, cores collected are
`r k_d N_S`, and units successfully restored are `r y k_d N_S`. So the fraction of service
supplied by the loop is

```
A_circ  =  r · y   ≤   r          with equality iff  y = 1
```

**The core return rate is a hard ceiling on the circular fraction, and no yield improvement can
lift it.** Yield moves you up to the ceiling; only collection raises the ceiling. This is
falsifiable in one line: **any published claim that a product system's circular content exceeds
its own core return rate is either measuring mass rather than units, or importing cores from
outside the fleet it reports on.**

**The closest published case is Huster et al. 2023's German EV-battery fleet**, the only source
reached that states `r` explicitly as a modelling variable. Its central assumptions cap the 2032
circular fraction at

- `r` = 0.75 (RD75 / RF75) → **`A_circ` ≤ 0.75**, and 0.638 at a generous `y` = 0.85;
- `r` = 0.50 (RF50, and the floor of their expert elicitation) → **`A_circ` ≤ 0.50**;
- `r` = 1.00 (RF100) is the only scenario admitting a fully closed loop, and the paper treats it
  as an upper bracket, not a forecast.

So: **the German EV-battery fleet's circular ceiling in 2032 is 0.75 before any yield loss, and
the paper's own sensitivity finding — that return rate and core quality dominate capacity
planning — is this inequality observed without being written down.**

## 6. Honesty

**Return is not failure.** `k_d` here is an *exit* rate, and exits pool wear-out with
obsolescence, lease end, trade-in, accident and export. That is the same mixture objection
[[G30-weibull-product-lifespan]] carries, and it means `k_d` is not a hazard for any single
degradation process. A fleet's `Ha` is therefore a **flow balance**, not a hazard ratio, and the
two coincide only when exit is dominated by physical failure.

**Units leave the system.** C6's chain conserves population; a fleet does not. §3 shows the
consequence is not a correction term but a structural one: without new production there is no
steady state to compute an `A` of. Every number in §4's reman rows would be conditional on a
replenishment rate that none of the sources publish either.

**C6's own grade limits what this can claim.** `Ha` is graded REPACKAGED in the vault's novelty
audit — it is the reciprocal of the Erlang-B offered load, standard since Erlang. This note adds
a **fourth** application of a standard object, plus one genuinely new piece of algebra ((★★),
the `r`-corrected availability, derived here and not found in either literature). It does not add
a new dimensionless group, and should not be written up as if it did.

**One bridge exists.** G33 is `narrowed`, not a zero: Alqahtani 2017 (`10.17760/d20249105`)
already carries Barlow & Hunter's mathematics onto remanufactured fleets. Its full text was not
obtained (HTTP 418/403), so the claim that it forms no rate ratio is **UNVERIFIED** and is the
one thing that could overturn this note cheaply.

**And the empty rows are the result.** Three of nine rows are blank for want of a single
duration. Stating that plainly is the finding, per `recipes.md` step 4.
