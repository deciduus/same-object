---
name: C42-soil-ha-theory
type: computed
exit: computation
extends-to: [sustainability, conservation]
next-step-cost: S
---

# Soil is a stock: what `Ha` is, and is not, in the depth balance

> **Structural-only.** `Ha = k_r/k_d` is an exact ratio of two fluxes at the *current* depth,
> but `A = Ha/(1+Ha)` is not an availability, not a fraction of time in service, and not a
> steady-state thickness ratio: under the depth-dependent production function the steady state
> is `D_ss = D*·ln(P0/E)` and it **ceases to exist entirely once `E ≥ P0`**, which is where
> every managed row of [[C35-soil-ha]] sits.

Tests the mapping [[C35-soil-ha]] §6 flagged and [[G36-wear-erosion-damage]] leg 2 relies on,
against the standard soil-depth balance. Structural precedent: [[C31-remanufacturing-ha]]'s
"no interior steady state" for a draining stock. Written to the standard of
[[C37-lolp-starvation-identity]]: theorem, conditions, failure boundaries.
Arithmetic re-runnable: `python _scripts/c42_soil_theory.py` from `vault/`.

---

## 1. The model, and where `Ha` lives in it

Soil depth `D` [mm] obeys a one-dimensional mass balance:

```
dD/dt  =  P(D)  −  E(slope, cover, erosivity)                                     (1)
P(D)   =  P0 · exp(−D/D*)                                                          (2)
```

(2) is the **soil production function** of Heimsath, Dietrich, Nishiizumi & Finkel 1997,
*Nature* 388:358, DOI `10.1038/41056` — **Crossref-verified** (title, journal, all four
authors, 1997-07-24, fetched 2026-09-05). Its Tennessee Valley (CA) parameters:
`P0 = 0.077 mm/yr` on bare bedrock, falling to `0.0077 mm/yr` under 1 m of soil, hence
`D* = 1000/ln 10 = 434 mm` — **VERIFIED-SECONDARY** (the two endpoints are from secondary
summaries; the *Nature* PDF was not fetched).

The **humped alternative** (Ahnert 1977; Carson & Kirkby 1972) has `P(0) < P(D_peak)`: bare
rock weathers slowly because it holds no water, production peaks under a thin mantle, then
declines. Everything below is stated for (2); §3a says what the hump changes and what it does
not.

**`Ha` in these variables.** Put `k_r ≡ P(D)` and `k_d ≡ E`. Then

```
Ha(D)  =  P(D)/E  =  (P0/E)·exp(−D/D*)                                             (3)
```

This is exact, and it is the whole of what `Ha` is here: **the instantaneous ratio of two
fluxes evaluated at the current depth**. It is not a hazard ratio, not an MTBF/MTTR, and not a
property of a soil — it is a property of a soil *at a moment*, declining monotonically as the
profile thickens. C35's rows quote `Ha` at an unstated `D`.

## 2. Steady state and stability

Setting (1) to zero:

```
P(D_ss) = E     ⟹     D_ss = D*·ln(P0/E) ,   and this exists iff  E < P0.          (4)
```

**Stability.** `d/dD [P(D) − E] = −(P0/D*)·exp(−D/D*) < 0` for all `D ≥ 0`. The right-hand
side of (1) is strictly decreasing, so when the root (4) exists it is the **unique** root and
is **globally asymptotically stable** on `D ≥ 0`: thin soil produces fast and thickens, thick
soil produces slowly and thins. This is Heimsath's landscape-equilibrium result, and it is the
soil analogue of C6 §3.1's globally stable fixed point — reached by a different route, since
the restoring force here is the *depth dependence of `k_r`*, not the linearity of a two-state
chain.

**When `E ≥ P0` there is no fixed point at all.** `dD/dt = P0·e^{−D/D*} − E < 0` for every
`D ≥ 0`, so the profile decreases monotonically to bedrock. This is the exact structural mirror
of [[C31-remanufacturing-ha]] §3 — a stock with a drain the replenishment cannot match has no
interior steady state, only an absorbing boundary. **The bedrock is C31's empty fleet.**

With `P0 = 0.077 mm/yr`, *every* managed erosion rate in C35 clears that bar: conventional
median 1.537, no-till median 0.082, global mean 0.215, and **both USDA `T` values** (0.172 and
0.862 mm/yr). Only native vegetation (0.013 mm/yr) sits below `P0`, at a stable
`D_ss = 773 mm`.

## 3. `A = Ha/(1+Ha)` has no availability reading here

C6 derives `A` as the steady-state fraction of a *conserved population of units* that are
functional. Soil has no units and no conservation: eroded material leaves the column. So `A`
cannot be a fraction of time in service. Three candidate readings, all of which fail or shrink:

| Candidate meaning of `A` | Verdict |
|---|---|
| Fraction of the profile in service | **No object.** There is no functional/damaged partition of a depth. |
| Fraction of time the profile is "up" | **No absorbing-return.** Bedrock is absorbing; the process does not cycle. |
| Steady-state thickness relative to zero-erosion thickness (C35 §6's proposal) | **False.** Zero erosion gives `D → ∞` under (2). The ratio's denominator diverges. C35 §6's gloss is withdrawn here. |
| Retained fraction of the gross two-flux budget, `P/(P+E)` | **True but empty — a rename.** |

The last row is the only survivor and it is worth stating precisely, because it is the trap.
`P/(P+E)` is algebraically identical to `Ha/(1+Ha)`, and it *is* the fraction of the gross
vertical flux budget that is addition rather than removal. But the two fluxes act at **opposite
ends of the column** (§3b), so their sum is not a budget of anything physical; and the map
`x ↦ x/(1+x)` is a monotone bijection, so `A` carries exactly the information `Ha` carries and
no more. **It is a rescaling, not a quantity.** Report `Ha` and drop the `A` column for every
soil row.

What (1) *does* license is a genuinely useful, dimensioned object: the **net rate** `P − E`,
and the horizon it implies. That is §4.

## 4. The number policy cares about: the depth-loss horizon

Take `D0 = 300 mm`, the 0.3 m surface horizon (nutrient- and organic-matter-enriched; FAO/IPCC
convention). Two horizons, both computed by the script:

**(i) The constant-formation lifespan**, `L = D0/(E − F)` — this is Evans, Quinton, Davies &
Zhao 2020's soil lifespan exactly (§5).

**(ii) The exact time to bedrock under (1)**, integrating `dt = dD/(E − P(D))`:

```
t_bed  =  D0/E  +  (D*/E)·ln[ (E − P0·e^{−D0/D*}) / (E − P0) ] ,     requires E > P0.  (5)
```

(5) is derived here; differentiating it returns `1/(E − P(D0))`, checked numerically in
`c42_soil_theory.py` to 3e-10. It reduces to `D0/E` as `D* → 0`.

| System | `E` mm/yr | `Ha` at `F` = 0.017 | `L` = D0/(E−F) | `t_bed` (5) |
|---|---|---|---|---|
| Conventional agriculture, median (Montgomery) | 1.537 | 0.0111 | **197 yr** | **203 yr** |
| Conventional agriculture, at a round 1.5 mm/yr | 1.500 | 0.0113 | **202 yr** | **208 yr** |
| Conventional agriculture, mean | 3.939 | 0.0091 | 77 yr | 77 yr |
| USDA `T` = 5 short ton/ac/yr | 0.862 | 0.0197 | **355 yr** | **372 yr** |
| Global mean (Borrelli 2.8 t/ha/yr) | 0.215 | 0.0789 | 1,512 yr | 1,887 yr |
| USDA `T` = 1 short ton/ac/yr | 0.172 | 0.0986 | **1,930 yr** | **2,592 yr** |
| No-till / conservation, median | 0.082 | 0.207 | 4,615 yr | 15,105 yr |
| Native vegetation, median | 0.013 | 1.308 | thickening | never (`D_ss` = 773 mm) |

**Assumptions, stated because the number is quotable only with them:** `D0` = 300 mm and the
horizon is uniform in depth; `E` constant in time; `F` = 0.017 mm/yr (Montgomery 2007 Table 1
median, n = 188) for column `L`; `P0` = 0.077, `D*` = 434 mm for column `t_bed`; erosion
strictly removes from the top and production strictly adds at the base; bulk density constant
(§3e); no deposition, no tillage translocation, no subsoil substitution of function.

**The headline.** *At conventional-agriculture erosion rates a 30 cm A-horizon is gone in about
two centuries, and at the USDA's most permissive `T` in about three and a half.* `T` = 5
ton/ac/yr does not preserve the horizon; it licenses spending it over roughly the lifetime of
a nation.

**Two structural readings of the table.** (a) The two columns agree closely at high `E` and
diverge badly at low `E` — 4,615 yr vs 15,105 yr for no-till — because the depth dependence of
`P` matters only when `E` is within reach of `P0`. **The constant-`F` lifespan is conservative
where it is dangerous and pessimistic where it is not.** (b) `t_bed` is *finite for every row
above native vegetation*, including both `T` values, which is (4) restated in years.

## 5. The `T`-value, stated exactly, and the prior-art grade

**Definition.** USDA "soil loss tolerance" `T` is the maximum average annual rate of soil
erosion that will permit crop productivity to be sustained economically and indefinitely; the
historical basis was an assumed renewal rate of roughly **1 inch of topsoil in 30 years**
(= 0.85 mm/yr), which is precisely how the 5 ton/ac/yr upper value survives. **VERIFIED-
SECONDARY** — no NRCS handbook page was fetched in full, as in C35 §2 row 8.

**So `Ha ≡ 1` at `T` is a definition, not a measurement.** "The rate at which loss is exactly
balanced by formation" is `k_d ≡ k_r`. Restating it in C6's variables adds nothing. C35 §5 is
right about this, and this note adds only the sharpening: the *empirical* claim is not about
`Ha` at all, it is the two-sample comparison **`T` vs measured `P`** — 0.172–0.862 mm/yr
against 0.017 mm/yr, i.e. 10.1×–50.7×.

### Prior art: three names already exist, and C35 met none of them

| Prior object | What it is | Relation to C35 |
|---|---|---|
| **Soil lifespan**, `L = D/(E − F)`, `D` = 300 mm | Evans, Quinton, Davies & Zhao 2020, *Environ. Res. Lett.* 15:0940b2, DOI `10.1088/1748-9326/aba2fd` — **Crossref-verified** (title, journal, four authors, 2020-09-15, fetched 2026-09-05); text read for the definition, which is verbatim `L = D/(E−F)` with `D` = 300 mm, reporting median 491 yr conventional, 333 yr bare, 16% and 34% of soils under 100 yr respectively | **This IS §4's horizon.** Prior art, published, and C35 does not cite it. |
| **Erosion Index**, `EI = potential erosion / T` | USDA/NRCS conservation-planning convention | `EI = 1/Ha` **with `T` substituted for the formation rate**. The reciprocal ratio is already an agency metric. |
| **Tolerable vs actual erosion** | Verheijen, Jones, Rickson & Smith 2009, *Earth-Sci. Rev.* 94:23–38, DOI `10.1016/j.earscirev.2009.02.003` — **Crossref-verified** | The `T`-vs-measured-formation comparison as a European review. |

**Grade for [[C35-soil-ha]], honestly.**

- The **depth-loss horizon is prior art** — Evans et al. 2020, with the same 300 mm and the
  same subtraction. C35 did not compute it and did not cite it; this note supplies both.
- The **`T`-vs-`P` discrepancy is Montgomery's**, stated in his words in the 2007 *PNAS* paper
  (DOI `10.1073/pnas.0611508104`, Crossref-verified). C35's contribution is the *number*
  (10.1×–50.7×) on a comparison Montgomery made qualitatively — a **quantification of someone
  else's claim**, which is a real but small contribution.
- The **`Ha` framing is the project's**, and §1–§3 above show it is the weakest of the three:
  it is `EI` reciprocated, with a measured `P` swapped in for `T`.
- **Verdict: C35 grades REPACKAGED, not novel** — one grade below what its own §6 claims, and
  for a reason §6 did not identify (it defended against C6's novelty grade, not against soil
  science's own prior art). Its `A` column should be deleted per §3.

## 6. The five failure boundaries

**(a) `P` depends on `D`, so `Ha` is state-dependent.** C6 condition C2 (constant hazard)
fails, as C35 §6 already said; §1–§2 now say what it costs. Under sustained `E > P0` there is
**no steady state**, and the profile reaches bedrock in the finite time (5). The humped
production function makes this *worse*, not better: with `P(0) < P_peak`, the last stretch of
thinning is also the slowest-producing, so (5) understates `t_bed` near `D → 0`. **The hump
does not create a low-`D` refuge; it removes one.** **VERDICT: BREAKS. `Ha` is `Ha(D)`, and no
scalar `Ha` describes a soil.**

**(b) Conveyor, not pool.** Erosion removes the top; production converts bedrock at the base.
A pool model is indifferent to which molecules leave; a conveyor is not. Organic carbon,
nitrogen, available phosphorus and aggregate structure are all strongly depth-stratified and
concentrated in exactly the horizon erosion takes, while what production adds at the base is
mineral saprolite with near-zero organic carbon. **So depth-`Ha` = 1 does not imply
quality-`Ha` = 1: a profile can be depth-stationary and still lose fertility monotonically,
because the two fluxes are not fungible.** The formation rate at which *productive* soil is
made is bounded above by the pedogenic rate at which fresh saprolite acquires carbon, which is
slower than the physical production rate. **VERDICT: BREAKS the equivalence of the fluxes.
Depth `Ha` is an upper bound on quality `Ha`, never an estimate of it.**

**(c) Cover feedback makes a real threshold, which `Ha = 1` never was.** Let `E = E(D)` fall
with `D` through vegetation cover — thin soil holds less water, supports less biomass, gives
less cover, and erodes faster (Kirkby's cover-competition formulation). Then (1) becomes
`dD/dt = P(D) − E(D)` with `P` decreasing and `E` decreasing. Two decreasing curves can cross
**twice**: a stable thick-soil state and, below it, an **unstable threshold depth** `D_crit`
separating recovery from runaway stripping. That is a genuine bifurcation — the collapse point
C6 §3.2 explicitly denies exists for `Ha` ("`Ha = 1` is not a threshold, a break-even or a
collapse point"). **VERDICT: this is where soil is structurally richer than C6, and the
threshold is `D_crit`, a depth — not `Ha = 1`, a ratio.** The one place the soil row could add
something back to C6's axis, and it needs `E(D)` measured, which no row here has.

**(d) Time scales are not commensurable.** `P` from cosmogenic ¹⁰Be is an integrated rate over
the nuclide's accumulation window — 10³–10⁵ yr, typically ~10⁴. `E` under agriculture is a
decadal plot or model estimate. Forming `Ha = P/E` divides a Holocene-averaged quantity by a
post-war one. It is legitimate *only* as a comparison of a long-run supply ceiling against a
present-day demand — which is exactly the comparison policy wants, so the mismatch is
tolerable — but it is **not** a statement about a single system at a single time, and any
claim that native vegetation "is at `Ha ≈ 1`" is comparing a 10⁴-yr numerator with a decadal
denominator and should not be read as balance observed. **VERDICT: SURVIVES for the policy
comparison, FAILS for any dynamical claim.** C35's "not circular, independent sample sets" is
true and insufficient: independence does not make the windows commensurable.

**(e) Bulk density.** `ρ_b` enters only the mass-derived rows (the `T` values and Borrelli),
where `k_d ∝ 1/ρ_b`, so `Ha ∝ ρ_b` linearly. Over 1100–1600 kg/m³:

| `T` | `ρ_b` = 1100 | 1300 | 1600 |
|---|---|---|---|
| 1 ton/ac: `Ha` / `T`:`k_r` | 0.083 / 12.0× | 0.099 / 10.1× | 0.121 / 8.2× |
| 5 ton/ac: `Ha` / `T`:`k_r` | 0.017 / 59.9× | 0.020 / 50.7× | 0.024 / 41.2× |

**VERDICT: SURVIVES.** The band moves the discrepancy from "10–51×" to "8–60×" and never
approaches 1, so C35 §5's claim is robust to `ρ_b`. But management *changes* `ρ_b` — compaction
under conventional tillage raises it, which lowers depth-loss for a given mass-loss, so a fixed
`ρ_b` is a bias with a sign, not just a band. It is the smallest of the five.

## 7. Honesty

**The most important number in this note contradicts C35's inputs.** Under Heimsath's
parameters, production at `D` = 300 mm is `P(300) = 0.0386 mm/yr` — **2.3× larger** than
Montgomery's compiled median of 0.017 mm/yr that C35 uses as `k_r` everywhere. Both are
defensible (Montgomery's is a global compilation across depths and lithologies; Heimsath's is
one Californian catchment), and they are not measuring the same thing: a *median across sites of
unstated depth* is not `P` at a stated depth. **Every `Ha` in C35 and in §4's table therefore
carries a factor-of-~2 ambiguity from a variable — soil depth — that neither number reports.**
That is a larger error than the bulk-density band C35 does discuss, and it was not visible until
the production function was written down. It does not change any sign or any order of magnitude.

**Nothing here is a measurement.** `P0`, `D*` and the 300 mm horizon are all borrowed
parameters; (5) is exact arithmetic on a model, and the model is the standard one, not a fitted
one. The failure boundaries are analytic, not empirical. Equation (5) is derived here and I did
not search for it in the geomorphology literature — depth-integrated stripping times are the
kind of thing exhumation studies compute routinely, so it should be assumed prior art until
checked, and it is not offered as a contribution.

**The cover-feedback bifurcation of §3c is asserted, not solved.** Two decreasing curves *can*
cross twice; whether real `E(D)` and `P(D)` do, and where `D_crit` sits, is unresolved here.
Kirkby's formulation is cited from memory of its structure, **UNVERIFIED** — no Kirkby paper was
fetched this session, and that citation must be checked before the claim is quoted anywhere.

**What this note takes away is larger than what it adds.** It withdraws C35 §6's proposed
reading of `A`, deletes the `A` column for soil, downgrades C35 to REPACKAGED, and shows the
horizon C35 never computed was already published by Evans et al. in 2020. What it adds is (5),
the stated non-existence of the steady state above `P0`, the five verdicts, and the
`P(300)`-vs-median discrepancy above. On this vault's own standard that is a **correction note
with a small positive residue**, and it should be written up as one.
