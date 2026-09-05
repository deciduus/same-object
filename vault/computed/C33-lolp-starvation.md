---
name: C33-lolp-starvation
type: computed
exit: computation
extends-to: [sustainability, ecology]
next-step-cost: S
---

# Loss-of-load expectation and starvation probability, on one axis

> **A published blue-tit winter model runs at a starvation probability of `8.2×10⁻⁸` per
> 100-night winter — an LOLE of `6.6×10⁻⁷` unserved hours per winter, about five orders of
> magnitude safer than the North American grid's 1-day-in-10-years criterion — and it buys that
> margin with a dusk fat reserve `57%` above the night's draw, against the grid's `15–20%`
> planning reserve margin.** Closes the computation leg of [[G34-lolp-starvation-risk]]. It does
> **not** put one dataset through both formalisms, so the gap moves from unclosed to
> `crosses: formalism`, not to `crosses: data`.

Arithmetic and fetches: `vault/_scripts/c33_lolp.py compute`.

---

## 1. One notation

Let `x(t)` be a stored reserve on `[0, x_max]`, `t` a discrete period, `T` the horizon. Each
period the reserve takes a stochastic **inflow** `g_u(ξ_t)` under control `u` and a stochastic
**outflow** `c(η_t)` under exogenous state `η_t`:

```
x(t+1) = min( x_max ,  x(t) + g_u(ξ_t) − c(η_t) ) ,      0 absorbing
```

| Symbol | Power system, storage-constrained adequacy | Small bird in winter |
|---|---|---|
| `x` | state of charge (MWh) | fat reserve (kJ) |
| `g_u(ξ)` | generation available, `ξ` = outage/wind/solar draw | foraging gain, `ξ` = success of a foraging bout |
| `c(η)` | load, `η` = weather/demand state | metabolic expenditure, `η` = weather state |
| `u` | dispatch / charge decision | forage intensively, forage safely, rest, thermoregulate |
| `x_max` | storage energy capacity | maximum fat deposits |
| `T` | planning year | winter |

Define `S(x,t)` = probability the reserve survives to `T` from state `x` at `t`. Then

```
S(x,t) = max_u  E_{ξ,η} [ S( min(x_max, x + g_u(ξ) − c(η)), t+1 ) ]      (★)
S(x,T) = 1 for x > 0 ;   S(x,·) = 0 for x ≤ 0
```

**(★) is the LOLP recursion and the starvation backward equation.** The grid writes its answer
as `LOLP(t) = P(x(t) ≤ 0)` and aggregates it as `LOLE = Σ_t P(x(t) ≤ 0)·Δt`; the bird writes
`P(starve) = 1 − S(x₀, 0)`. Same functional equation, same absorbing boundary, same backward
sweep — only the aggregation differs, and the aggregation is a reporting convention.

**The shadow price is the same object too.** Differentiate the value function in the reserve:

```
∂V/∂x  =  marginal value of a stored unit
```

On the grid this is the **value of lost load** — the multiplier on the energy-balance
constraint, the currency the adequacy optimum equates against the marginal cost of capacity. In
the bird it is the **marginal fitness value of a unit of fat** — the multiplier on the reserve
constraint, the fitness the optimum equates against the marginal predation cost of carrying it.
Both are read off the derivative of the value function that (★) computes. **Two quantities
matching, not one.**

---

## 2. Inputs

**Bird side — every parameter from one open-access, fully specified SDP.** Brodin, Nilsson &
Nord, *Adaptive temperature regulation in the little bird in winter: predictions from a
stochastic dynamic programming model*, **Oecologia 185(1):43–54 (2017)**, DOI
`10.1007/s00442-017-3923-3`. Open-access full text fetched from Europe PMC
<https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5596050/fullTextXML>, **2026-09-05**.
Model animal: a non-hoarding parid of 10–13 g, e.g. a blue tit *Cyanistes caeruleus*.
**Houston & McNamara 1993 itself is paywalled and its parameters were not obtained**; this is
its open successor in the same model family, and the substitution is stated rather than hidden.

| Symbol | Parameter | Value | Source |
|---|---|---|---|
| `X_max` | max fat deposits | **148 kJ** (= 4 g fat, 100 steps) | Table 2 |
| `D` | days in winter | **100** | Table 2 |
| — | periods per day | **288** (5 min), of which **96** daylight (8 h) | Table 2 + text |
| `α` | gain, a full day of intensive foraging | **80 kJ** | Table 1 |
| `C_RM` | resting metabolism | **45 kJ/day** | Table 1 |
| `λ` | P(a foraging period succeeds) | **0.8** | Table 1 |
| `δ` | gain reduction on an unsuccessful period | **20%** | Table 2 |
| `γ` | expenditure increase, bad weather | **20%** | Table 2 |
| `ε` | expenditure saving, maximum hypothermia | **30%** | Table 2 |
| `x_start` | fat at start of forward iteration | **12 kJ** | Table 2 |
| `p_GG`, `p_BB` | weather persistence per period | **0.9983**, **0.9965** | text |

Night length is **16 h** (the model's complement of its 8 daylight hours), which is midwinter at
the study latitudes (Lund 56°N / Oulu 65°N in the same group's fieldwork).

**Derived budget** (`c33_lolp.py compute`): realised daily gain `96 × (80/96) × (0.8 + 0.2×0.8)`
= **76.80 kJ**, sd **0.653 kJ**, **CV = 0.85%**. Daylight cost `45 × 8/24` = 15.0 kJ (18.0 cold).
Overnight draw `45 × 16/24 × 0.7` = **21.0 kJ** hypothermic (25.2 cold), **30.0 kJ**
normothermic (36.0 cold). Net per day: **+40.8 kJ** good weather, **+33.6 kJ** bad.

**Grid side.** Energy Systems Integration Group, *New Resource Adequacy Criteria for the Energy
Transition: Modernizing Reliability Requirements* (Reston VA, 2024), DOI `10.2172/2372882`,
NREL subcontract LAT-9-92162-01. PDF fetched from <https://www.osti.gov/servlets/purl/2372882>,
**2026-09-05**, and text-extracted. Verbatim from its criteria survey: *"the maximum allowable
LOLE is set to 0.1 days/year (or 1 day in 10 years) … across much of North America"*; **LOLH ≤ 3
hours/year** for Belgium, France, Great Britain and Poland, **≤ 4** for the Netherlands, **≤ 8**
for Ireland; **PRM ≥ 15%** for WECC-CAMX and **≥ 10%** for mainland Spain. Historical anchor for
the criterion: Telson, **Bell J. Econ. 6(2) (1975)**, DOI `10.2307/3003250` (Crossref-resolved
2026-09-05); ESIG's own verdict on it is that *"the origins of this specific standard are
nebulous."*

---

## 3. Result — the two-way conversion

**Conversion rule, stated once so it can be attacked.** A starvation event ends the night, so it
is charged the **mean remaining night, 8 h**, and a winter is **100 nights**:

```
LOLE_bird (h/winter)  =  P(starve | winter) × 8 h
p_night               =  1 − (1 − P_winter)^(1/100)
```

### A. Bird → grid units

`P(starve)` computed by exact forward propagation of the joint (reserve, weather) distribution
at the model's own 5-minute resolution, under the policy the paper reports as optimal under
almost all conditions — forage intensively every daylight period, maximum hypothermia every
night — with 0 absorbing. `scale` multiplies foraging gain; it is the paper's own food-
availability knob (its `Δ`).

| foraging-gain `scale` | **P(starve \| winter)** | p/night | **LOLE, h/winter** |
|---|---|---|---|
| **1.00 (published parameterisation)** | **8.25 × 10⁻⁸** | 8.2 × 10⁻¹⁰ | **6.6 × 10⁻⁷** |
| 0.80 | 6.89 × 10⁻⁵ | 6.9 × 10⁻⁷ | 5.5 × 10⁻⁴ |
| 0.70 | 1.30 × 10⁻³ | 1.3 × 10⁻⁵ | 1.04 × 10⁻² |
| **0.5617** | **0.100** | 1.05 × 10⁻³ | **0.80** |
| 0.5253 | 0.375 | 4.7 × 10⁻³ | 3.00 |
| 0.50 | 0.837 | 1.8 × 10⁻² | 6.70 |

### B. Grid criterion → bird units

| Criterion | source | **P(starve \| 100-night winter)** | **p/night** |
|---|---|---|---|
| North America, LOLE ≤ 0.1 d/yr (1-in-10) | ESIG 2024 | **0.100** | 1.05 × 10⁻³ |
| GB / France / Belgium / Poland, LOLH ≤ 3 h/yr | ESIG 2024 | **0.375** | 4.69 × 10⁻³ |
| Netherlands, LOLH ≤ 4 h/yr | ESIG 2024 | 0.500 | 6.91 × 10⁻³ |
| Ireland, LOLH ≤ 8 h/yr | ESIG 2024 | **mapping saturates** (≥ 1) | — |

### C. Both on one axis

```
LOLE, unserved hours per year-equivalent horizon
  10^-7 ┤ ● blue tit, Brodin et al. 2017 published parameters (6.6e-7)
  10^-4 ┤ ● same bird at 80% of published foraging gain
  10^-2 ┤ ● same bird at 70%
  10^0  ┤ ● North America 1-in-10 (0.8)   ≡ bird at 56.2% of gain
        ┤ ● GB/FR/BE/PL LOLH 3 h/yr (3.0) ≡ bird at 52.5% of gain
  10^1  ┤ ● Ireland LOLH 8 h/yr — off the bird's scale entirely
```

**The headline reading.** The published bird model is not marginally safer than a grid — it is
safer by about **five orders of magnitude in LOLE**, and it would have to lose **43.8%** of its
foraging gain before its winter starvation risk fell to the North American 1-in-10 criterion,
or **47.5%** before it reached the British LOLH standard. Read in reverse, **European LOLH
standards translate into per-winter mortality of 37–50%** for a bird, which is in the range of
real passerine overwinter mortality and is *not* in the range of anything a utility means by
"reliable". The grid and the bird are not solving the same problem to the same tolerance; they
are solving the same problem at tolerances separated by five decades.

---

## 4. Reserve margin — the prediction

The grid's deterministic sizing statistic is the **planning reserve margin**: firm capacity over
peak load, minus one. The bird's exact analogue is the dusk reserve over the night's draw.
`x_dusk = x_start + overnight draw = 12.0 + 21.0 =` **33.0 kJ** (from Table 2's forward-iteration
start, which the paper describes as the level the iteration settles on).

| Night | draw `R` (kJ) | `(x_dusk − R)/R` |
|---|---|---|
| typical night, maximum hypothermia | 21.0 | **+57.1%** |
| **cold night (γ = 20%), maximum hypothermia** — the peak-load case | 25.2 | **+31.0%** |
| typical night, **normothermic** (hypothermia removed) | 30.0 | +10.0% |
| cold night, normothermic | 36.0 | **−8.3%** (deficit) |

**Prediction.** The optimal-fat rule in a published small-bird winter model corresponds to a
planning reserve margin of **≈31% against the peak (coldest) night** and **≈57% against a
typical night** — roughly **two to four times** the 15–20% grid convention (ESIG 2024: WECC-CAMX
PRM ≥ 15%, mainland Spain ≥ 10%). And the mechanism of the difference is legible: strip the
bird's **demand-side** lever (nocturnal hypothermia, `ε = 30%` — the grid's demand response) and
its margin collapses to **+10%**, *below* the grid convention, and to a **−8.3% deficit** on a
cold night. **The bird meets a far stricter adequacy standard than any grid while carrying a
supply-side margin that is only modestly larger, because it buys most of its adequacy on the
demand side.** That is the transferable claim.

**Falsifier.** Measure dusk fat load and overnight energy expenditure in the same wild wintering
parids. If `(x_dusk − R)/R` on typical nights sits at **0.10–0.20** rather than near 0.5, the
quantitative leg fails and the correspondence is structural only. If the margin does *not* fall
towards the grid's 15% band when hypothermia is unavailable — e.g. in a species or roost
microclimate where facultative hypothermia is not used — the demand-side mechanism claim fails
independently of the first.

---

## 5. Honesty

1. **Units of the inflow variance.** The bird's inflow noise is Bernoulli-in-time on a 5-minute
   period: mean 0.800 kJ, variance 0.00444 kJ² per period, giving **CV = 0.85%** on the day's
   gain. A grid's inflow noise is dominated by *correlated* multi-hour renewable and outage
   events, and its CV on a day's energy is one to two orders of magnitude larger. Putting the two
   `P(x→0)` on one axis does **not** put the two noise processes on one axis, and the five-decade
   LOLE gap in §3 is substantially a statement about how much less variable this bird's income is
   than a grid's — not only about how much more conservatively it is sized.
2. **Horizons differ, and the conversion is a convention.** A grid year is 8,760 h with an
   annual peak; the bird's horizon is 100 nights with a nightly minimum. The 8-h "mean remaining
   night" charge in §3 is an assumption, chosen because it is the only unserved-duration the bird
   problem admits. Halving it halves every LOLE in column 4 and doubles every `P(winter)` in
   table B. **Nothing in §4 depends on it**; only §3's absolute LOLE values do.
3. **The bird's "value" is fitness, not cost.** `∂V/∂x` in currency is a price a regulator can
   compare against the cost of new entry. `∂V/∂x` in fitness is not commensurable with money and
   there is no exchange rate. The identity in §1 is exact *as a dynamic program* and only
   analogical *as an economics* — VoLL and marginal fat value are the same multiplier on the same
   constraint in the same value function, and that is all that is claimed.
4. **Exact or structural?** The recursion (★) is **exact**: both fields solve that equation, and
   this note did not have to bend either to make them match. The *numbers* are structural: the
   grid criteria are read off a survey table, the bird's `P(starve)` is recomputed here rather
   than quoted from the paper, and the two are then placed on one axis by a conversion rule this
   note invented in §3.
5. **Terminal vs restorable.** A grid's unserved load is restored; a starved bird is dead.
   `P(hit 0)` is the same quantity in both, but *repeated* events are possible only on the grid,
   so LOLE as an expected *count* is well-defined there and is a probability in disguise here.
   This is why table B saturates for Ireland.
6. **What the bird model itself never reports.** Brodin et al. publish trajectories, not a
   starvation probability. **The `8.25 × 10⁻⁸` is this note's number, not theirs**, computed from
   their parameters under their stated near-optimal policy. Their own model also carries
   predation, which dominates mortality in it and is deliberately excluded here — this is a
   starvation-only figure, and the bird's *total* winter mortality is not 8×10⁻⁸.
7. **`x_dusk = 33.0 kJ` is derived, not printed.** It is `x_start` (12 kJ, Table 2) plus the
   good-night draw computed in §2. The paper's Fig. 3 dusk value was not read off the figure.

See [[G34-lolp-starvation-risk]], [[C1-availability-living-tissue]], [[availability-formula]],
[[C6-damage-healing-ratio]].
