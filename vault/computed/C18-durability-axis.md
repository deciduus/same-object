---
name: C18-durability-axis
type: computed
---

# A cycle count cannot be the shared durability axis — but neither can a bare β. There is one β axis *per object class*, and the classes here are unit-lifetime distributions, bulk decay-curve rate constants, and degradation-path first-passage fits.

> **The negative half stands.** A single dimensionless *cycle count* cannot span catalytic and
> energy-storage durability, for the exact [[stress-strength-interference]] discrete-vs-continuous
> reason. Enzymes die by a memoryless per-cycle catastrophe (suicide inactivation is a partition
> ratio: `N_fail = 1/p`, a geometric first-passage → constant hazard → `β = 1`). Li-ion cells die
> by cumulative wear-out (`N_fail = tolerance/f` with a threshold crossing → increasing hazard →
> `β > 1`, reported ~12.7). The *same integer* `N_fail ≈ 500` hides a mean-time-to-catastrophe in
> one case and a wear-out lifetime in the other.
>
> **The positive half is narrower than this note originally claimed.** `β` is a shared *vocabulary*,
> not automatically a shared *coordinate*. [[C26-ews-hazard-shape]] rows 5–6 put the same 100
> C-MAPSS turbofan units through two estimators and got `β = 4.41` (MLE on the ensemble of
> lifetimes) versus `β = 0.97` (Weibull matched to the first-passage law of one unit's degradation
> path) — a factor of 4.5 from the estimator alone. So a `β` is only interpretable once the
> **object** (what the random variable is) and the **estimator** (how the number was obtained) are
> named, and **two β values are comparable only when both match.**
>
> **What survives, restated within class.** Enzyme thermal deactivation and organic flow-battery
> reactant fade are both *bulk first-order decay curves* whose rate constant implies a constant
> hazard: within that class they do coincide, and that within-class coincidence is the note's real
> result. **The claim that flow-battery reactants sit "with enzymes and against Li-ion" on one axis
> is withdrawn** — Li-ion's 12.7 is a fitted *unit-lifetime* distribution and the other three rows
> are not lifetime distributions at all, so no outlier statement can be made across them.
> Within the unit-lifetime class alone, the comparison is legitimate and the neighbours are in
> [[C27-product-lifespan-beta]], [[C29-recovery-beta]] and [[C26-ews-hazard-shape]], not in §3.
>
> **Verdict: NARROW to "same count, different failure law," and BUILD the axis as `(object,
> estimator, β)` — one axis per object class, not one axis.** The reporting asymmetry still holds
> and is still the finding: **everyone reports the mean (`TTN`, cycle life); the battery field also
> reports a fitted lifetime distribution, the enzyme field almost never does** — which is exactly
> why the enzyme rows below carry `not recorded` estimators.

Bears on [[G3-cycle-life]], [[stress-strength-interference]], [[specification-instruments]].
Corrected 2026-09-05 by [[C26-ews-hazard-shape]]; cross-referenced to
[[C27-product-lifespan-beta]] and [[C29-recovery-beta]]. See §Corrections 2026-09-05.

---

## 0. Comparability rule (read before §3)

> **Rows are comparable only within the same `object` class.** A Weibull `β` is a property of a
> fitted distribution, and the distribution is over whatever the `object` column names. Four object
> classes appear in this vault:
>
> | object class | the random variable | β means |
> |---|---|---|
> | **unit lifetime** | time-or-cycles to failure of one unit, sampled across many units | unit-to-unit dispersion in a population |
> | **time-to-event** | time from a start to a state change, right-censored | dispersion of event times across records |
> | **degradation-curve parameter** | first-passage time implied by one unit's fitted degradation path | drift-to-noise ratio of a single path |
> | **fade-curve / deactivation-kinetics parameter** | a bulk decay rate constant, converted to a hazard by assumption | order of the kinetics, not a measured dispersion |
>
> Comparing across classes is the [[C26-ews-hazard-shape]] error: R1 and R2 gave 4.41 and 0.97 on
> the *same units*. Any row whose `estimator` is `not recorded` is **NOT COMPARABLE** to anything,
> including rows in its own class, and may be quoted only as an inference with its model named.

## 1. What each field actually measures

| Field | Quantity | Units | What it is |
|---|---|---|---|
| Catalysis (industrial) | Total turnover number `TTN` | dimensionless | moles product per mole catalyst over its whole life |
| Catalysis (biology) | Catalytic cycles until replacement `CCR` | dimensionless | metabolic flux / protein turnover ([[G3-cycle-life]], Hanson PNAS 2021) |
| Batteries | Cycle life | dimensionless | charge/discharge cycles to 80% capacity (20% loss) |
| Batteries | Capacity fade `f` | %/cycle | fractional capacity lost per cycle |
| Thermochemical / flow | Cycles (or days) to a stated conversion loss | dimensionless / time | cycles or calendar days to a loss threshold |

Superficially these are one object: **a count of cycles until a degradation threshold is crossed.**
The [[G3-cycle-life]] gap is that nobody has put them on one axis. §2–§4 test whether they *can* be —
and the answer is that the naive shared object (the count) is two different objects wearing one number.

## 2. The crux — a cycle count is `N_fail = degradation_tolerance / degradation_per_cycle`, but the *statistics* of "per cycle" differ

Write the generic durability as
```
N_fail  =  (how much degradation the thing tolerates)  /  (degradation incurred per cycle)
```
The question G3 forces is not whether both sides have an `N_fail` — both do — but whether the
`per-cycle` term is governed by comparable **failure statistics**. It is not. There are two
regimes, and they are the discrete-vs-continuous split [[stress-strength-interference]] already
named in the G5/C6 work.

### 2.1 Discrete catastrophe (enzymes) — geometric first-passage, `N_fail = 1/p`

Suicide inactivation is the textbook case, and it is **already dimensionless and already a cycle
count**. Each turnover, the reactive intermediate either releases product (survival) or covalently
kills the enzyme (catastrophe) with probability `p` per cycle. The enzymology name for `1/p` is the
**partition ratio** `r` = turnovers per inactivation event:
```
survival after N cycles:   S(N) = (1 − p)^N
cycles-to-death:           geometric, mean  N_fail = 1/p = r = TTN
continuous limit:          S(t) = e^(−p t)   → CONSTANT hazard  h(N) = p,  memoryless
```
So for a suicide-inactivated enzyme **`TTN` is literally the partition ratio**, and the failure law
is **exponential / constant-hazard = Weibull `β = 1`.** Real `p` values (VERIFIED via search,
partition-ratio literature):

| Enzyme / inactivator | partition ratio `r` = `TTN` | `p = 1/r` (catastrophe prob/cycle) | source |
|---|---|---|---|
| thioether S-methyltransferase / ethyl vinyl sulfide | 100 | 0.010 | [pubs.acs.org/10.1021/bi9600815](https://pubs.acs.org/doi/10.1021/bi9600815) — search-snippet `VERIFIED` |
| cytochrome P-450 / allylisopropylacetamide | 184 | 5.4×10⁻³ | [sciencedirect S0021925819689015](https://www.sciencedirect.com/science/article/pii/S0021925819689015) — search-snippet `VERIFIED` |
| cystathionine γ-synthase / propargylglycine | 4 | 0.25 | [pubmed 387077](https://pubmed.ncbi.nlm.nih.gov/387077/) — search-snippet `VERIFIED` |
| methionine γ-lyase / propargylglycine | 6 | 0.17 | same |

And the *in vivo* biological figure from [[G3-cycle-life]] (Hanson PNAS 2021, PMC8020674, read in
full in the vault): `CCR` ranges `<10³` to `>10⁷`, medians 3–4×10⁴. That range **is a range of
`1/p`** — a distribution of catastrophe probabilities from `~10⁻³` to `<10⁻⁷` per cycle.

Thermal (non-suicide) inactivation gives the same `β`: enzyme thermal deactivation is
"described by the simple exponential equation of a first-order process, `(A)t/(A)o = exp(−k·t)`"
([sciencedirect S0141022900002581](https://www.sciencedirect.com/science/article/abs/pii/S0141022900002581),
search-snippet `VERIFIED`). First-order population decay **is** a constant hazard **is** Weibull
`β = 1`. The one deviation the literature documents is *biphasic* decay from subpopulation
heterogeneity — a fragile fraction dying first — which pushes `β < 1` (decreasing hazard,
"infant-mortality" shape), **never `β > 1`**
([Sadana 1987, Biotech.Bioeng. 30:604](https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/abs/10.1002/bit.260300604);
microheterogeneity model [pubmed 18588183](https://pubmed.ncbi.nlm.nih.gov/18588183/) — search-snippets `VERIFIED`).

**Enzymes live at `β ≤ 1`** — but note what kind of statement this is: it is a *model* claim from
first-order kinetics and the geometric partition-ratio model, not a fitted lifetime distribution.
Per §0 it is not comparable with any fitted `β`.

### 2.2 Continuous wear-out (Li-ion) — threshold crossing, `N_fail = tolerance / f`

A Li-ion cell loses a roughly fixed fractional capacity `f` per cycle and is declared dead at 20%
loss. Deterministically `N_fail = 0.20/f`. Real fade rates (VERIFIED):

| System | fade `f` | `N_fail = 0.20/f` | source |
|---|---|---|---|
| Li-ion, typical (2003 survey) | 0.025–0.048 %/cycle | ~420–800 cycles | [en.wikipedia/Capacity_loss](https://en.wikipedia.org/wiki/Capacity_loss) `VERIFIED` (fetched) |
| Li-ion, aggressive 4C/2C | 0.85 %/cycle | ~24 cycles | search-snippet `VERIFIED` |

But the *distribution* of `N_fail` across nominally identical cells is not a spike — it is a
**Weibull with `β > 1`**, because death is a cumulative-damage threshold crossing (SEI growth,
electrode fatigue/fracture): the hazard *increases* as damage accumulates toward the wall.
Published shape parameters:
- **`β = 12.7`** from cycle-life testing of NCR18650GA cells ("wear-out failure mode with low
  cell-to-cell variability") — search-snippet, primary is ResearchGate (403 on fetch), reported
  as **`VERIFIED-via-search`, not fetch-verified.**
- Reliability texts: `1 < β < 4` early wear-out, `β > 4` rapid wear-out
  ([reliamag](https://reliamag.com/articles/weibull-analysis/) search-snippet `VERIFIED`).
- Mixture-Weibull SoH modelling of Li-ion, `k > 1` "consistent with wear-out dominated
  degradation" ([PMC11176627](https://pmc.ncbi.nlm.nih.gov/articles/PMC11176627/) fetched — the
  paper uses mixture-Weibull but does not print a single scalar `β`, so no number is quoted from it).

**Li-ion lives at `β > 1`. That is the signature of wear, not catastrophe.**

### 2.3 The third regime — organic flow reactants are chemically-driven, `β ≈ 1` in *time*

The sharpest new result. For organic flow batteries the fade is **not cycling-driven at all** —
it is calendar-time chemical decomposition of the redox molecule, first-order in time. From the
symmetric-cell cycling study ([iopscience 10.1149/2.0891807jes](https://iopscience.iop.org/article/10.1149/2.0891807jes),
fetched, `VERIFIED`): DHAQ fades "0.1%/cycle … about 7.6%/day", AQDS "0.08 ± 0.02%/day", and the
authors state outright that **time-based metrics are more appropriate than cycle-based metrics
because degradation is chemically driven.** The celebrated low-fade organic ("Methuselah")
quotes **< 0.001%/cycle**
([sciencedaily 2018](https://www.sciencedaily.com/releases/2018/07/180723142859.htm), search-snippet
`VERIFIED`; primary IOP paywalled).

A molecule decaying by a fixed per-unit-time probability is **exactly the enzyme thermal-inactivation
statistics**: constant hazard, exponential survival, **Weibull `β = 1`** — just on the time axis
rather than the cycle axis. **The organic flow-battery reactant is an enzyme-like molecular
catastrophe, not a Li-ion wear-out.**

## 3. The Weibull-β bridge, stated as the shared axis

Reliability engineering already carries the coordinate G3 says is missing. The Weibull hazard is
```
h(N) = (β/η)·(N/η)^(β−1)
   β = 1  →  h constant           →  random / catastrophic failure   (exponential life)
   β > 1  →  h increasing in N     →  wear-out failure                (accumulating damage)
   β < 1  →  h decreasing in N     →  infant mortality / fragile subpopulation
```
Place each field:

| System | failure mechanism | axis | **object** | **estimator** | Weibull `β` | comparable? |
|---|---|---|---|---|---|---|
| Enzyme, suicide inactivation | per-cycle covalent catastrophe (`p = 1/r`) | cycles | unit lifetime (per-molecule cycles-to-catastrophe) | **not recorded** — sources (§2.1) report a mean partition ratio only; `β = 1` is *asserted* from the geometric model, never fitted | **≈ 1** (model) | **NO** — no fitted distribution exists |
| Enzyme, thermal | first-order denaturation | time | deactivation-kinetics parameter (bulk residual-activity decay constant `k`) | read from the paper's own first-order fit `(A)t/(A)o = exp(−kt)` | **≈ 1** (implied by first-order kinetics; `<1` if biphasic, Sadana 1987) | within the decay-curve class only |
| Organic flow reactant | chemical decomposition of the molecule | **time** | fade-curve parameter (%/day capacity-fade rate) | read from the paper's own fade rate (IOP 10.1149/2.0891807jes); no Weibull fit performed anywhere | **≈ 1** (implied) | within the decay-curve class only |
| Li-ion cell NCR18650GA | SEI growth + electrode fatigue, threshold at 80% | unit lifetime (cycles-to-80% across nominally identical cells) | the source's own Weibull fit to cycle-life test lifetimes; the fitting method (MLE vs rank regression) is **not recorded** in the accessible snippet, and the primary returned 403 | **12.7** (`VERIFIED-via-search`) | unit-lifetime class only, and see §3.1 |

### 3.1 What this table does and does not license

**`β` is a shared vocabulary across these rows; it is a shared *coordinate* only inside a class.**
Three of the four rows are not lifetime distributions at all: two are bulk decay-rate constants and
one is an unfitted model assertion. Only the Li-ion row is a fitted `β` of the kind
[[C26-ews-hazard-shape]] row 5 calls R1.

**Withdrawn.** "Put each on the `β` axis and Li-ion is the outlier, while flow-battery chemistry and
enzyme chemistry coincide." That sentence compares a fitted unit-lifetime `β` against three
non-lifetime numbers and is not well defined. There is no outlier here, because there is no single
population.

**Restated, within class:**

1. *Decay-curve class.* Enzyme thermal deactivation and organic flow-battery reactant fade are both
   first-order in time, so both imply a constant hazard on their own decay curve. **Within that
   class they genuinely coincide**, and the reclassification of flow-battery reactants away from
   cycle-counting toward calendar-time chemical death (§2.3, the authors' own statement) survives
   untouched — it is a claim about *which variable the fade is first-order in*, not about β.
2. *Unit-lifetime class.* Li-ion's `β = 12.7` is a wear-out shape and can be compared only with
   other fitted lifetime distributions. Its legitimate neighbours are the product classes in
   [[C27-product-lifespan-beta]] (`β = 1.00–6.0`) and C-MAPSS R1 in [[C26-ews-hazard-shape]]
   (`β = 4.41`) — all of which sit **below** it. Against those, 12.7 is high but not a different
   kind of thing.
3. *No cross-class statement is made.* The enzyme suicide-inactivation row is quotable only as
   "the geometric model implies constant hazard", never as a measured `β`.

## 3.2 Cross-reference — β values in other notes, with their object and estimator

These rows are **not** merged into §3: each number's provenance, CI and caveats stay in its owning
note, and only the owning note may be cited for it.

| owning note | row | object | estimator | β |
|---|---|---|---|---|
| [[C26-ews-hazard-shape]] | C-MAPSS FD001, **R1** | unit lifetime (100 turbofan lifetimes) | direct Weibull MLE on the sample of failure times | 4.41 |
| [[C26-ews-hazard-shape]] | C-MAPSS FD001, **R2**, *same 100 units* | degradation-curve parameter (Wiener drift-to-threshold first passage per unit) | Wiener fit + IG→Weibull least-squares match on `log(−log S)` | 0.97 |
| [[C26-ews-hazard-shape]] | Cariaco YD→Preboreal, R2 | degradation-curve parameter (rolling AR(1) indicator to `L = 1`) | same R2 route | 5.84 |
| [[C27-product-lifespan-beta]] | 11 US appliance classes (Lutz 2011) | **discard** lifetime from household survey stock-by-age — a leaving-service time, not a failure time | the report's own least-squares fit of a delayed Weibull survival function | 1.00–2.22 |
| [[C27-product-lifespan-beta]] | 10 European passenger-car fleets (Held 2021) | discard lifetime from fleet-turnover data | the paper's own fit, Table 1 | 2.0–6.0 |
| [[C29-recovery-beta]] | ecosystem recovery, pooled (Jones & Schmitz 2009) | time-to-event (years from disturbance to recovery) | Weibull MLE with right-censoring (42.5% censored), profile-likelihood CI | 0.587 |

**Note the object caveat on C27:** those are *discard* distributions from surveys, not failure
records. A discarded appliance need not have failed, so C27's `β` measures an exit process that
mixes physical wear with replacement decisions — C27 says this itself. It is a lifetime-class
number, but a different lifetime than Li-ion's cycles-to-80%.

## 4. Why the raw cycle count fails as the axis (the negative half)

`N_fail` alone is meaningless as a *unifier* because it is a first moment stripped of its
distribution. Two systems with identical `N_fail ≈ 500`:
- **Enzyme, `p = 2×10⁻³`:** `N_fail = 1/p = 500`, but this is a *mean cycles between catastrophes* —
  the survival curve is `e^{−N/500}`, 37% still alive at `N = 500`, a long exponential tail, hazard
  flat. Failure is a coin that comes up "dead" with fixed odds every cycle.
- **Li-ion, `f = 0.04%/cycle`, `β = 12.7`:** `N_fail = 500`, but this is a *wear-out lifetime* —
  almost every cell survives to ~450 and almost none past ~560, hazard climbing steeply. Failure is
  a wall the whole population hits together.

**The same number `500` encodes a flat-hazard lottery and a synchronized wall.** Reporting only
`N_fail` (TTN, cycle life) is reporting `η` and discarding `β` — the half that says *which failure
law*. This is the same lesson as [[C6-damage-healing-ratio]] §6 (the pair `(A, τ_relax)`, not a
single group) and [[C15-metastability-metric]] (a single number hid the prefactor): **the honest
durability object is at least 3-D, `(N_fail, β, object+estimator)`** — 2-D was this note's original
answer, and [[C26-ews-hazard-shape]] added the third slot by showing `β` alone is not
estimator-invariant. `β` is the coordinate G3's fields never share, because each reports only its
own `N_fail` — and when they do report a `β`, they report it for different objects.

The two bullets above are a comparison of two *models* at a matched mean, which is legitimate and is
the negative half of this note. It is not a comparison of two measured `β` values, and §0's rule
forbids reading it as one.

## 5. Does the distribution data exist to test the bridge?

The bridge is `β`, and `β` is only measurable from a **cycle-to-failure distribution**, not a mean.
So the operational question is: who publishes distributions?

- **Batteries — YES.** Weibull cycle-life fits are standard: scalar `β` values (12.7 reported),
  mixture-Weibull SoH models ([PMC11176627](https://pmc.ncbi.nlm.nih.gov/articles/PMC11176627/)),
  sealed-lead-acid Weibull life models. The battery field routinely fits and reports `β`. The bridge
  is directly testable on this side.
- **Enzymes — MOSTLY NO, but inferable.** Enzymology reports `TTN`/partition ratio as a **single
  mean**, and thermal stability as a **bulk first-order decay curve**. The good news: a bulk
  first-order curve *is* the ensemble signature of `β = 1`, so the enzyme `β ≈ 1` claim is supported
  by the pervasive first-order-kinetics literature — but it is almost never reported *as* a
  molecule-level cycle-to-failure histogram. Single-molecule enzymology could produce one directly;
  the bulk literature substitutes the exponential decay curve for it.

**So the verdict on data is asymmetric, and that asymmetry is a finding in the [[G3-cycle-life]]
sense:** both fields report the mean (TTN, cycle life); the battery field *also* reports the failure
distribution and fits Weibull `β`; the enzyme field reports the mean plus an ensemble decay curve
that implies `β = 1` but rarely names it. The shared axis is not absent — it is **published on one
side and left implicit on the other.** Nobody has drawn the two `β` values on one plot because the
enzyme community never labels its first-order kinetics as "Weibull `β = 1`," and the battery
community never connects its `β` to a partition ratio.

## 6. Verdict

1. **A single dimensionless cycle count CANNOT span the two legs — NARROW G3 to "same count,
   different failure law."** Catalytic durability is a discrete Poisson/geometric catastrophe
   (`N_fail = 1/p`, `β = 1`); Li-ion durability is continuous wear-out (`N_fail = tolerance/f`,
   `β > 1`). The shared "cycle count" conflates a mean-time-to-catastrophe with a wear-out lifetime.
2. **The shared axis that exists is `(object, estimator, β)` — one β axis per object class, not one
   axis.** `β` is reliability's random-vs-wear-out coordinate and it is dimensionless, but
   [[C26-ews-hazard-shape]] showed it is estimator-dependent (4.41 vs 0.97 on the same 100 units),
   so a bare `β` does not locate a field. What survives: **within the bulk decay-curve class,
   organic flow-battery reactants and thermally-inactivated enzymes share a first-order,
   constant-hazard law** — a real reclassification of flow chemistry off the cycle axis onto the
   time axis. **The claim that Li-ion is "the outlier" against them is withdrawn**: its `β = 12.7`
   is a fitted unit-lifetime shape and the others are not lifetime fits at all. This is the
   [[specification-instruments]] residual
   made positive: the specification for a shared durability axis is *"one parameter that encodes the
   failure law, not the failure count,"* and `β` satisfies it where `N_fail` does not.
3. **Distribution data to test it: rich on the battery side (`β = 12.7`, mixture-Weibull), thin and
   implicit on the enzyme side** (bulk first-order kinetics ⇒ `β = 1`, but molecule-level cycle-to-
   failure histograms are essentially unpublished). So the bridge is *constructible and half-tested*;
   the untested half is limited by reporting convention, not by physics — everyone publishes the
   mean, only one field publishes the distribution.

## 7. Status

- **§2.1 enzyme partition ratios** (100, 184, 4, 6) and `CCR 10³–10⁷`: `VERIFIED` — partition-ratio
  search snippets + [[G3-cycle-life]] vault full-text (Hanson PMC8020674). First-order thermal
  deactivation exponential: `VERIFIED` (sciencedirect snippet). Biphasic ⇒ `β<1`: `VERIFIED` (Sadana
  1987, microheterogeneity snippets).
- **§2.2 Li-ion fade** 0.025–0.048%/cycle: `VERIFIED` (Wikipedia Capacity_loss, fetched). `β = 12.7`
  NCR18650GA: **`VERIFIED-via-search` only** — primary ResearchGate returned 403, so treated as
  reported-not-fetched, in the `METHOD.md` §4 sense. The qualitative `β > 1` (wear-out) is
  over-determined across [PMC11176627](https://pmc.ncbi.nlm.nih.gov/articles/PMC11176627/) (fetched),
  reliamag, and reliability texts.
- **§2.3 organic flow reactants**: DHAQ 0.1%/cycle ≈7.6%/day, AQDS 0.08%/day, and the
  chemically-driven / time-metric statement: `VERIFIED` (IOP 10.1149/2.0891807jes, fetched). Methuselah
  <0.001%/cycle: `VERIFIED-via-search` (ScienceDaily snippet; primary IOP paywalled).
- **What would overturn this.** A published enzyme *cycle-to-failure distribution* with `β > 1`
  (wear-out, e.g. progressive misfolding accumulation rather than single-hit catastrophe) would break
  the clean enzyme=`β=1` half. A Li-ion chemistry with genuinely constant hazard (`β = 1`, calendar-
  dominated) would blur the outlier claim — the organic flow reactants already sit there, which is
  why they cross the bridge rather than break it.

## Corrections 2026-09-05

Trigger: [[C26-ews-hazard-shape]] §5 showed `β` is estimator-dependent — the same 100 C-MAPSS
FD001 units give `β = 4.41` by direct Weibull MLE on the ensemble of lifetimes (R1) and
`β = 0.97` by the degradation-path first-passage route (R2). Every sentence below was changed
because the original made a comparison across object classes.

| # | was | now |
|---|---|---|
| 1 | Headline: "The shared durability axis is not the cycle count — it is the Weibull shape parameter β … it reclassifies organic flow-battery reactants with enzymes, against Li-ion." | Headline: "A cycle count cannot be the shared durability axis — but neither can a bare β. There is one β axis *per object class* …" |
| 2 | Pull-quote: "**The shared coordinate that DOES span both is the Weibull shape parameter `β`**" | Pull-quote: `β` is a shared *vocabulary*, not automatically a shared *coordinate*; a `β` is interpretable only once `object` and `estimator` are named. |
| 3 | Pull-quote: "The bridge is not 'everyone counts cycles'; it is 'put each on the `β` axis and Li-ion is the outlier, while flow-battery chemistry and enzyme chemistry coincide.'" | **Withdrawn as cross-class.** Restated: within the bulk decay-curve class, flow reactant and thermal enzyme deactivation coincide; no outlier statement is made, because Li-ion's β is a fitted lifetime distribution and the other three rows are not. |
| 4 | Pull-quote verdict: "BUILD the axis: `β`, not `N_fail`." | "BUILD the axis as `(object, estimator, β)` — one axis per object class, not one axis." |
| 5 | §2.1: "**Enzymes live at `β ≤ 1`. That is the signature of catastrophe, not wear.**" | Kept, but labelled a *model* claim from first-order kinetics / the geometric partition-ratio model, not a fitted distribution, and therefore not comparable with any fitted β. |
| 6 | §3 table columns: `System / mechanism / axis / β / statistics` | `System / mechanism / axis / **object** / **estimator** / β / **comparable?**`. Two rows now carry `not recorded` estimators (enzyme suicide inactivation: no fit exists; Li-ion NCR18650GA: fitting method absent from the accessible snippet, primary 403). |
| 7 | §3: "**`β` is the missing shared coordinate.** It spans both legs of G3 … putting enzyme chemistry and flow-battery chemistry together at `β ≈ 1` and isolating Li-ion electrode wear at `β > 1`." | Replaced by §3.1: `β` is a shared vocabulary across these rows and a shared coordinate only inside a class; the "isolating Li-ion" clause is withdrawn. |
| 8 | §4: "**the honest durability object is 2-D, `(N_fail, β)`**" | "at least 3-D, `(N_fail, β, object+estimator)`" — C26 added the third slot. |
| 9 | §4: the matched-`N_fail ≈ 500` enzyme-vs-Li-ion pair | Kept, with an added line saying it compares two *models* at a matched mean and must not be read as a comparison of two measured `β` values. |
| 10 | §6 verdict 2: "organic flow-battery reactants sit with enzymes at `β ≈ 1` … and Li-ion is the wear-out outlier at `β > 1`." | "one β axis per object class, not one axis"; the within-decay-curve-class coincidence survives, the outlier claim is withdrawn. |
| 11 | — (new) | §0 comparability rule; §3.1 within-class restatement; §3.2 linked cross-reference table to [[C26-ews-hazard-shape]], [[C27-product-lifespan-beta]], [[C29-recovery-beta]] with each row's object and estimator, and no numbers imported into §3. |

**The honest outcome, plainly: the "one durability axis" claim narrows to "one axis per object
class."** G3's two legs are still connected by the *failure-law* distinction, but not by a single
comparable number, because catalysis publishes decay-rate constants and energy storage publishes
lifetime distributions, and a `β` read off one is not the same quantity as a `β` fitted to the other.

See [[G3-cycle-life]], [[stress-strength-interference]], [[specification-instruments]],
[[C26-ews-hazard-shape]], [[C27-product-lifespan-beta]], [[C29-recovery-beta]].
