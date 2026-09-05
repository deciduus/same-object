---
name: C33-lolp-starvation
type: computed
exit: computation
extends-to: [sustainability, ecology]
next-step-cost: S
---
# Loss-of-load expectation and starvation probability, on one axis

> **What survives is the recursion, not the numbers.** Power-system adequacy and small-bird
> winter energetics run the same reserve recursion and read the same shadow price off it, but
> they report **different functionals** of it — an expected occupation time on the grid, a
> first-passage probability in the bird — so no exchange rate exists; this note's `P(starve)` is
> **withdrawn** because a fixed-gain forward propagation cannot estimate a state-dependent DP's
> first passage; and the reserve margin, computed like-for-like as an energy margin over the
> critical period, is **+43.8%** for the bird against **≈0%** for a 4-hour storage fleet, with
> the hypothermia lever worth **12 points**, not 47.

Computation leg of [[G34-lolp-starvation-risk]], narrowed. Theory in
[[C37-lolp-starvation-identity]]; cross-species replication in
[[C38-reserve-margin-across-species]]; the adversarial review that forced this rewrite is
`audits/g34-adversarial.md`. Arithmetic: `python _scripts/c33_lolp.py compute` from `vault/`.

---

## 1. One notation, and where the identity stops

Let `x(t)` be a stored reserve on `[0, x_max]`, `t` a discrete period, `T` the horizon. Each
period the reserve takes a stochastic **inflow** `g_u(ξ_t)` under control `u` and a stochastic
**outflow** `c(η_t)` under exogenous state `η_t`:

```
x(t+1) = min( x_max ,  x(t) + g_u(ξ_t) − c(η_t) )
         0 absorbing on the bird side only; reflecting on the grid side
```

| Symbol | Power system, storage-constrained adequacy | Small bird in winter |
|---|---|---|
| `x` | state of charge (MWh) | fat reserve (kJ) |
| `g_u(ξ)` | generation available, `ξ` = outage/wind/solar draw | foraging gain, `ξ` = success of a foraging bout |
| `c(η)` | load, `η` = weather/demand state | metabolic expenditure, `η` = weather state |
| `u` | dispatch / charge decision | forage intensively, forage cautiously, rest, thermoregulate |
| `x_max` | storage energy capacity | maximum fat deposits |
| `T` | planning year | winter |

Define `S(x,t)` = probability the reserve survives to `T` from state `x` at `t`. Then

```
S(x,t) = max_u  E_{ξ,η} [ S( min(x_max, x + g_u(ξ) − c(η)), t+1 ) ]      (★)
S(x,T) = 1 for x > 0 ;   S(x,·) = 0 for x ≤ 0
```

**(★) is the storage-constrained adequacy recursion and the starvation backward equation.** The
grid writes its answer as `LOLP(t) = P(x(t) ≤ 0)` and aggregates it as
`LOLE = Σ_t P(x(t) ≤ 0)·Δt`; the bird writes `P(starve) = 1 − S(x₀, 0)`.

**Same state recursion, same backward sweep — and there the identity stops.** The bird's zero is
absorbing and `P(starve)` is a **first-passage probability**. **The grid's zero is not
absorbing**: load is shed, the shortfall ends, and storage recharges, so `LOLE` is an expected
**occupation time** of a non-absorbing process, counting repeated crossings. First-passage
probability and expected occupation time are different functionals of the same process, and they
diverge exactly where the risk is interesting — a system that dips below zero ten times for an
hour each has LOLE 10 h and would have died at the first dip. **The aggregation is not a
reporting convention; it is the difference between the two estimands.** The previous revision of
this note asserted the opposite ("only the aggregation differs, and the aggregation is a
reporting convention"); that clause is withdrawn.

[[C37-lolp-starvation-identity]] states the surviving identity as a theorem with five conditions
(C1 discrete time, C2 absorbing boundary at 0, C3 a reserve cap, C4 additive inflow/outflow, C5
the objective `P(absorb before T)` under a common discount factor) and shows that **C2 and C5
both fail as the two fields are normally practised** — the grid's boundary is reflecting and it
prices a magnitude (EENS), not a probability. The identity is exact on a restricted pair of
problems and structural-only on the pair the fields actually solve.

**The shadow price is the same object, and this part is unharmed.** Differentiate the value
function in the reserve:

```
∂V/∂x  =  marginal value of a stored unit
```

On the grid this is the **value of lost load** — the multiplier on the energy-balance constraint.
In the bird it is the **marginal fitness value of a unit of fat** — the multiplier on the reserve
constraint. Both are read off the derivative of the value function that (★) computes. **Two
quantities matching, not one**, and the shadow-price half of the match does not depend on the
estimand.

**Neither field cites the parent.** First passage of a reserve driven by stochastic income
against a stochastic draw is **ruin theory** (Lundberg 1903, Cramér 1930) — the surplus process,
the ruin probability, the adjustment coefficient. Power-system adequacy does not cite it,
behavioural ecology does not cite it, and neither cites the other: a **triple zero**, one branch
of which is the citation-intersection measurement in [[G34-lolp-starvation-risk]]. Both fields
re-derived a special case of an actuarial result from 1903.

---

## 2. Inputs

**Bird side — every parameter from one open-access, fully specified SDP.** Brodin, Nilsson &
Nord, *Adaptive temperature regulation in the little bird in winter: predictions from a
stochastic dynamic programming model*, **Oecologia 185(1):43–54 (2017)**, DOI
`10.1007/s00442-017-3923-3`. Open-access full text fetched from Europe PMC
<https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5596050/fullTextXML>, **2026-09-05**, and
**re-read in full 2026-09-05** for this revision. Model animal: a non-hoarding parid of 10–13 g,
e.g. a blue tit *Cyanistes caeruleus*. **Houston & McNamara 1993 itself is paywalled and its
parameters were not obtained**; this is its open successor in the same model family, and the
substitution is stated rather than hidden.

| Symbol | Parameter | Value | Source |
|---|---|---|---|
| `X_max` | max fat deposits | **148 kJ** (= 4 g fat, 100 steps) ⇒ **37 kJ/g** | Table 2 |
| `D` | days in winter | **100** | Table 2 |
| — | periods per day | **288** (5 min), of which **96** daylight (8 h) | Table 2 + text |
| `α₁` | gain, a full day of **behaviour 1** (forage intensively) | **80 kJ** | Table 1 |
| `α₂` | gain, a full day of **behaviour 2** (forage cautiously) | **60 kJ** | Table 1 |
| `C_RM` | resting metabolism | **45 kJ/day** | Table 1 |
| `C_WU` | **extra warming-up cost, hypothermic bird** | **0 or 6 kJ — the paper reports both** | Table 2, Fig. 3a |
| `λ` | P(a foraging period succeeds) | **0.8** | Table 1 |
| `δ` | gain reduction on an unsuccessful period | **20%** | Table 2 |
| `γ` | expenditure increase, bad weather | **20%** | Table 2 |
| `ε` | expenditure saving, maximum hypothermia | **30%** | Table 2 |
| `x_start` | fat at start of forward iteration | **12 kJ** | Table 2 |
| `p_GG`, `p_BB` | weather persistence per period | **0.9983**, **0.9965** | text |
| — | **the paper's own daily outcome** | **0.74 g/day = 27.4 kJ** | Results |
| — | **the paper's own winter survival** | **0.71 with hypothermia, 0.13 without** | Results, Fig. 2 |

Night length is **16 h** (the model's complement of its 8 daylight hours).

**Derived budget** (`c33_lolp.py compute`). Realised daily gain is `α × (λ + (1−λ)(1−δ))` =
`α × 0.96`. Daylight cost `45 × 8/24` = **15.0 kJ** (18.0 cold).

Overnight draw, `C_WU = 0`: `45 × 16/24 × 0.7` = **21.0 kJ** hypothermic (25.2 cold). **With the
paper's other treatment, `C_WU = 6 kJ`: 27.0 kJ hypothermic (31.2 cold)** — against **30.0 kJ**
normothermic (36.0 cold), so **the hypothermia lever saves 3 kJ, not 9.** **The paper's own
stabilised cycle independently puts the overnight draw at ≈27.4 kJ**: it reports a total daily
fat gain of **0.74 g**, which at the model's 37 kJ/g is 27.4 kJ, and in a stabilised cycle the
night's draw equals the day's gain. **Every number in the previous revision used the 21.0 kJ
branch, and that is the branch that flattered this note.** This revision charges `C_WU = 6 kJ`
throughout.

**Grid side.** Energy Systems Integration Group, *New Resource Adequacy Criteria for the Energy
Transition* (Reston VA, 2024), DOI `10.2172/2372882`, PDF fetched from
<https://www.osti.gov/servlets/purl/2372882>, **2026-09-05**: *"the maximum allowable LOLE is set
to 0.1 days/year (or 1 day in 10 years) … across much of North America"*; LOLH ≤ 3 h/yr for
Belgium, France, GB and Poland, ≤ 8 for Ireland. Capacity-margin band, for context only: **NERC
2025 LTRA, pp. 175–176, 7.0–26.3%** across 15 assessment areas (transcribed in
[[C38-reserve-margin-across-species]]).

---

## 3. The positive control the note never ran — and it FAILS

The single highest-value item in `audits/g34-adversarial.md` was: re-run the forward propagation
under the paper's own policy with `C_WU = 6 kJ` and check it against the paper's own **0.74
g/day**. Run:

| Daylight policy | realised gross gain | net day gain | g/day | × 0.74 |
|---|---|---|---|---|
| **A** behaviour 1 all day — *what rev.1 actually simulated* | 76.80 kJ | 61.80 kJ | **1.67 g** | **2.26×** |
| **B1** behaviour 1 to noon, behaviour 2 after | 67.20 kJ | 52.20 kJ | 1.41 g | 1.91× |
| **B2** behaviour 2 all day — *the lowest the paper's text allows* | 57.60 kJ | 42.60 kJ | **1.15 g** | **1.56×** |
| **C** **CALIBRATED**: `α` fitted to 0.74 g/day | 42.38 kJ | 27.38 kJ | 0.74 g | 1.00× |

**Verdict: the positive control fails, and the policy cannot be reconstructed from the open
text.** The paper says the bird *"should keep on foraging all daylight hours until dusk"*,
switching between behaviours 1 and 2 after noon. **Every mixture of behaviours 1 and 2 has a
floor of 42.60 kJ = 1.15 g/day, still 1.56× the paper's own 0.74 g.** No mixture reaches it. The
missing pieces are named in the paper but not parameterised in it: the **mass-dependent foraging
metabolism** (Table 1 footnote a — *"Metabolism when foraging is linearly mass-dependent"*) and
the **mass-dependent gain ceiling** (*"a bird can gain up to 1 g of fat before mass-dependent
effects … will have an effect on predation risk"*). Without those, the trajectory is not
reproducible from Tables 1–2.

So policy **C** fits a single effective `α_eff = 44.15 kJ/day` nominal (against the printed 80
and 60) to reproduce the paper's stated 0.74 g/day. **`α_eff` is a fit, not a parameter**, and is
labelled as such everywhere it is used.

### 3.1 And the first-passage number is withdrawn

| Policy | **P(starve \| 100-night winter)** | p/night, first passage |
|---|---|---|
| A max foraging, now with `C_WU = 6` | **2.31 × 10⁻⁵** | 2.3 × 10⁻⁷ |
| B1 mixed, half/half | 8.52 × 10⁻⁴ | 8.5 × 10⁻⁶ |
| B2 all-cautious | 1.81 × 10⁻² | 1.8 × 10⁻⁴ |
| **C CALIBRATED to the paper's own 0.74 g/day** | **0.9992** | 6.9 × 10⁻² |

**The bracket spans the entire probability scale, so the estimator is uninformative.** The reason
is structural, not arithmetic: **the paper's bird runs a state-dependent optimal policy produced
by the backward DP** — it forages harder when its reserve is low — and **no fixed-gain open-loop
forward propagation can estimate the first-passage probability of a closed-loop process.** A
policy generous enough to be safe overshoots the paper's realised trajectory by 2.3×; a policy
calibrated to that trajectory has no feedback left and dies almost surely.

**`P(starve) = 8.25 × 10⁻⁸` and `LOLE = 6.6 × 10⁻⁷ h/winter` are withdrawn, and no replacement
number is issued.** Under `C_WU = 6` the same open-loop policy A gives `2.31 × 10⁻⁵` — already
2.8 decades worse than the withdrawn figure, from the parameter alone.

**The paper's own published numbers are the quotable ones, and they bound everything above.**
Brodin 2017, Results, sentence 1: *"The probability of winter survival increased dramatically
from 0.13 to 0.71 if birds used hypothermia to save 30% of the overnight energy expenditure."*
So the model's own **P(die over a winter), all causes including predation, is 0.29 with
hypothermia and 0.87 without** — a hard ceiling of `P(starve) ≤ 0.29`, i.e. **≤ 3.4 × 10⁻³ per
night**. The withdrawn `8.25 × 10⁻⁸` sat **6.5 orders of magnitude below the paper's own
ceiling**, which is by itself sufficient to reject it. And the hypothermia lever in the paper's
own currency — **survival 0.13 → 0.71, 58 points** — is a *published* number and strictly better
evidence than anything this note computed for it.

### 3.2 The like-for-like probability comparison: not available

The previous revision printed a two-way conversion table between LOLE and `P(starve)` using an
invented 8-hour "mean remaining night" charge. **Both directions are withdrawn** — they convert
between non-commensurable functionals (§1), which is why the mapping saturated for Ireland. That
saturation was the symptom, not a curiosity.

What a like-for-like comparison needs is a **per-period first-passage probability** for a
storage-constrained system against the bird's per-night first passage. **No published one was
found in this session.** The two things that are available do not substitute:

- `LOLE ≤ 0.1 d/yr` is a per-day **occupation** probability of `2.74 × 10⁻⁴`, not a first
  passage.
- The union bound gives `P(first hit 0 within a year) ≤ LOLE = 0.1`. That bounds the grid from
  **above only**, so it cannot order the two systems in either direction.

**Stated as a null.** Getting a duration-dependent ELCC or storage-adequacy study that reports a
first-passage statistic is the open item; `audits/g34-adversarial.md` §*What would settle it* #4
gives the alternative — compute both functionals on one trace and derive the exchange rate
instead of inventing it.

---

## 4. Reserve margin — the surviving quantitative claim

**Like-for-like requires an energy margin, not a capacity margin.** The grid's planning reserve
margin is `(firm capacity − peak load)/peak load`, **MW/MW at a single annual instant**; the
bird's is **kJ/kJ over a 16-hour integral**. Both are dimensionless and they are not the same
dimensionless number. **The like-for-like quantity is the energy margin over the critical
period**: stored energy entering the net-peak window over the energy discharged across it.

**On the paper's own budget the bird's margin is `x_start / R` = `12 / 27.4` = +43.8%.** Note
that the margin is algebraically just `x_start / R` — the whole prediction is one ratio of two
model parameters.

Holding `x_dusk` at its derived **33.0 kJ** (`x_start` 12 + the `C_WU = 0` good-night draw 21.0),
the branch comparison is:

| Night | draw `R` (kJ) | `(x_dusk − R)/R` |
|---|---|---|
| **typical night, hypothermia, `C_WU = 6`** | 27.0 | **+22.2%** |
| cold night (γ = 20%), hypothermia, `C_WU = 6` | 31.2 | **+5.8%** |
| typical night, **normothermic** | 30.0 | **+10.0%** |
| cold night, normothermic | 36.0 | **−8.3%** (deficit) |
| *typical night, hypothermia, `C_WU = 0` — the rev.1 branch* | *21.0* | *+57.1%* |

**The hypothermia lever is 12.2 points (22.2% → 10.0%), not 47.1 (57.1% → 10.0%).** The
undisclosed `C_WU = 0` choice was the one that maximised the headline.

**The grid comparator, like-for-like.** For the 4-hour lithium fleets that dominate current
storage accreditation, sized against a 4-hour net peak, the energy margin over the critical
period is **≈0%** (and negative against a 5-hour event) — the `Li-ion storage` row in
[[C38-reserve-margin-across-species]]. **NERC's 7.0–26.3% planning band (2025 LTRA, pp. 175–176)
is a *capacity* margin and is quoted here for context only; it is not the comparator.** Against
the energy comparator the bird's ≈0.44 is roughly **2×**, not "two to four times the 15–20%
convention", and PRM should not be named.

**Prediction, narrowed.** The optimal-fat rule in a published small-bird winter model corresponds
to an energy margin over the critical period of **≈+44%** on the paper's own budget, against
**≈0%** for a duration-matched storage fleet, and **the difference is bought on the demand side**:
remove the bird's nocturnal hypothermia and the margin falls to **+10%**, and to a **−8.3%
deficit** on a cold night.

**The demand-side reading is the grid's own, not a transfer from the bird.** Demand response
counted as capacity toward resource adequacy is mature grid practice — MISO's *Demand Response
101* (2024), PJM's capacity auction, and "negawatt" as a term since Lovins 1989. **The borrowing
runs grid → bird.** What is new is not the concept but the **quantity**: no published figure
exists for the demand-side share of an animal's adequacy margin. The claim is the existence and
rough size of that quantity, and its size is uncertain by roughly a factor of four across the two
`C_WU` branches.

**The mechanism replicates across species, and that is now the strongest leg.**
[[C38-reserve-margin-across-species]] runs the identical division over **19 systems** and finds
the sorting variable is neither taxon, body mass nor horizon but **whether the metabolic setpoint
is movable and currently moved**: every animal exercising a lever sits far above the grid band
(+75% bat, +265% deer mouse, +354% rufous hummingbird), every one of those same animals falls
into or below it with the lever withdrawn (+1.5% cold deer mouse, −2.8% bat in a bad roost), and
the one species with no lever at all — the common shrew — sits at **−38% to −74%** and **cannot
hold a winter night on stored energy at any dusk fat load**, which is why it forages around the
clock instead of sizing a dusk reserve. The single-species parameter switch in this note is
therefore corroborated by nature throwing the same switch across a clade.

**Falsifier.** Measure dusk fat load and overnight energy expenditure in the same wild wintering
parids. If the energy margin on typical nights sits near **0.10–0.20** rather than near 0.44, the
quantitative leg fails and the correspondence is structural only. **The second falsifier is still
not tested even in-model**: the normothermic rows above are a counterfactual inside one
parameterisation — `x_dusk` held at its `ε = 30%` optimum with `ε` switched off. A bird that
genuinely cannot use hypothermia would **re-optimise `x_dusk` upward**, which is what the DP
exists to compute. Re-running Brodin's DP at `ε = 0` is a small job and is the minimum before the
demand-side mechanism is claimed in-model; C38's shrew and cold-deer-mouse rows are the
out-of-model substitute currently carrying it.

---

## 5. Honesty

1. **The estimand is not shared, and the previous revision said it was.** §1's clause "only the
   aggregation differs, and the aggregation is a reporting convention" was false in the direction
   that flattered the note. LOLE is an expected occupation time on a non-absorbing boundary;
   `P(starve)` is a first-passage probability on an absorbing one. The error was visible in this
   note's own rev.1 §5.5 ("terminal vs restorable") and in table B's saturation for Ireland, and
   was not carried into §1 or into G34's title.
2. **The positive control failed and the simulation is retired as an estimator.** No fixed-gain
   forward propagation reproduces the paper's own 0.74 g/day, and none can represent a
   state-dependent DP policy. `P(starve)` is withdrawn with no replacement. The honest object
   here is the paper's own published survival (0.71 / 0.13), which this note should have quoted
   from the start instead of recomputing.
3. **`C_WU` was silently set to zero.** Table 2 offers "0 or 6 kJ" and the paper reports both
   branches (Fig. 3a). Rev.1's parameter table omitted the row entirely and every number used the
   0 branch. Charging 6 kJ moves the overnight draw 21.0 → 27.0 kJ, within 2% of the paper's own
   stabilised 27.4, and cuts the demand-side lever from 47 points to 12.
4. **`δ` has two readings and this note takes the flattering one.** Eq. 7 in the paper writes the
   unsuccessful-period gain as `ΔG_i·δ`, which with δ = 0.20 means the gain is reduced **to** 20%,
   not **by** 20%. This note computes `(1 − δ)`, i.e. 80%, following Table 2's wording "reduced
   energy gain … 20%". The two readings differ by 12% on the realised daily gain and the
   ambiguity is unresolved. It does not change any conclusion above, because the calibration in
   §3 absorbs it.
5. **The margin comparison is capacity-free but still not clean.** The bird's number and the
   4-hour-storage number are both energy over a critical period, so they are dimensionally
   commensurable, but the storage figure is *reasoned* from duration matching rather than fetched
   from an accreditation study. A cited duration-dependent ELCC study would make it quotable.
   NERC's 7–26% band is a capacity quantity and is context only.
6. **The bird's "value" is fitness, not cost.** `∂V/∂x` in currency is a price a regulator can
   compare against the cost of new entry; `∂V/∂x` in fitness is not commensurable with money and
   there is no exchange rate. The shadow-price identity is exact *as a dynamic program* and
   analogical *as an economics*.
7. **The direction of borrowing runs grid → bird.** Demand-side resources counted toward adequacy
   is standard, mature grid practice. Rev.1 framed the demand-side reading as "the transferable
   claim", i.e. bird → grid. What transfers is the *quantity*, not the concept.
8. **Species label vs parameter source.** The paper labels its animal a non-hoarding parid, "such
   as a blue tit", but states that *"the parameter values are taken from data on willow tits"* and
   flags that blue tits *"may not be as cold-adapted"*. The willow tit is additionally a
   **large-scale hoarder**, and the model deliberately excludes caching (*"we did not include
   food-storing in our model"*). A cache is a second reserve invisible to a fat-only formalism, so
   these margins are a **lower bound** for any hoarding species — and the grid analogue, off-book
   contracted firm imports, is exactly what margin accounting argues about.
9. **`x_dusk = 33.0 kJ` is derived, not printed.** It is `x_start` (12 kJ, Table 2) plus the
   `C_WU = 0` good-night draw. The paper's Fig. 3 dusk value was not read off the figure. The
   like-for-like +43.8% avoids it entirely by using `x_start / R` directly.
10. **Prior-art instruments were degraded on 2026-09-05.** The adversarial sweep behind these
    corrections ran on **Europe PMC + WebSearch only**: Semantic Scholar returned HTTP 429 on 12
    queries and OpenAlex an exhausted daily budget. No source states the analogy in what was
    reachable, but the C5 §11 bar (≥8 formulations across ≥2 working indices) is **not** met on the
    engineering side, and an IEEE-side sweep is still owed.

---

## Corrections 2026-09-05 (deep inquiry)

Every number this revision changed, old → new. Log entries in `vault/log.md`; the evidence is
`audits/g34-adversarial.md` plus the re-read of Europe PMC `PMC5596050`.

| Quantity | Old | New | Why |
|---|---|---|---|
| Estimand claim, §1 | "only the aggregation differs … a reporting convention" | **withdrawn**; occupation time vs first passage | grid zero is reflecting, bird's is absorbing |
| `C_WU` | absent (silently 0) | **6 kJ**, charged | Table 2 reports "0 or 6 kJ"; both branches published |
| Overnight draw, typical night | 21.0 kJ | **27.0 kJ** (paper's stabilised cycle: 27.4) | `C_WU = 6` branch |
| Overnight draw, cold night | 25.2 kJ | **31.2 kJ** | same |
| Hypothermia saving | 9 kJ | **3 kJ** | same |
| Simulated daily fat gain | 61.8 kJ = 1.67 g | **paper's own 27.4 kJ = 0.74 g**; policy floor 42.6 kJ = 1.15 g | positive control; 2.26× overshoot |
| Policy description | "the policy the paper reports as optimal" | **behaviour 1 all day, which is not the paper's policy**; the paper's mixed policy is not reconstructible from the open text | "under almost all conditions" attaches to hypothermia only |
| `P(starve \| winter)` | 8.25 × 10⁻⁸ | **withdrawn.** Bracket 2.31 × 10⁻⁵ … 0.9992; paper's own ceiling **≤ 0.29** | open-loop estimator cannot represent a state-dependent DP |
| `LOLE_bird` | 6.6 × 10⁻⁷ h/winter | **withdrawn** | non-commensurable functionals |
| "five orders of magnitude safer than the grid" | asserted | **withdrawn**; no like-for-like grid first-passage number found | §3.2 |
| Two-way conversion table (A and B) | printed as a result | **withdrawn**, both directions | 8-hour charge converts between different functionals |
| Reserve margin, typical night | +57.1% | **+43.8%** like-for-like (`12/27.4`); +22.2% at `x_dusk` 33.0 | energy margin over the critical period |
| Reserve margin, cold night | +31.0% | **+5.8%** | `C_WU = 6` |
| Hypothermia lever | 47.1 points (57% → 10%) | **12.2 points** (22.2% → 10.0%) | `C_WU = 6` |
| Grid comparator | PRM 15–20% (ESIG) | **4-h storage vs 4-h net peak ≈ 0%**; NERC 7.0–26.3% named as a *capacity* quantity, context only | capacity vs energy |
| Direction of borrowing | bird → grid ("the transferable claim") | **grid → bird**; only the quantity is new | demand response is mature grid practice |
| Ruin-theory parent | not mentioned | **Lundberg 1903 / Cramér 1930, uncited by both fields** | triple zero, new |

See [[G34-lolp-starvation-risk]], [[C37-lolp-starvation-identity]],
[[C38-reserve-margin-across-species]], [[C1-availability-living-tissue]],
[[availability-formula]], [[C6-damage-healing-ratio]].
