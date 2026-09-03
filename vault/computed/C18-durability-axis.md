---
name: C18-durability-axis
type: computed
---

# The shared durability axis is not the cycle count — it is the Weibull shape parameter β. The count N_fail conflates two failure laws; β separates them, and it reclassifies organic flow-battery reactants with enzymes, against Li-ion.

> **A single dimensionless *cycle count* cannot span catalytic and energy-storage durability, for
> the exact [[stress-strength-interference]] discrete-vs-continuous reason. Enzymes die by a
> memoryless per-cycle catastrophe (suicide inactivation is a partition ratio: `N_fail = 1/p`, a
> geometric first-passage → constant hazard → Weibull `β = 1`). Li-ion cells die by cumulative
> wear-out (`N_fail = tolerance/f` with a threshold crossing → increasing hazard → Weibull
> `β > 1`, measured up to ~12.7). The *same integer* `N_fail ≈ 500` hides a mean-time-to-catastrophe
> in one case and a wear-out lifetime in the other — two different reliability distributions.**
>
> **The shared coordinate that DOES span both is the Weibull shape parameter `β`** — reliability's
> distinction between random/catastrophic failure (`β = 1`, exponential, "mean cycles between
> failures") and wear-out (`β > 1`, Weibull). That single parameter locates each field, and it does
> real classifying work: **organic flow-battery molecular reactants degrade by calendar-time
> chemical decay (`β ≈ 1` in *time*), which is the SAME failure law as enzyme death, not Li-ion's.**
> The bridge is not "everyone counts cycles"; it is "put each on the `β` axis and Li-ion is the
> outlier, while flow-battery chemistry and enzyme chemistry coincide."
>
> **Verdict: NARROW to "same count, different failure law," and BUILD the axis: `β`, not `N_fail`.**
> On the distribution data: **battery-side is rich** (published Weibull fits, `β = 12.7` for
> NCR18650GA, mixture-Weibull SoH models). **Enzyme-side is thin** — the `β = 1` claim rests on
> bulk first-order deactivation kinetics (an ensemble exponential *is* `β = 1`), not on published
> molecule-level cycle-to-failure histograms. So the `β` bridge is constructible and testable on
> one side, and *inferred but under-reported* on the other. That asymmetry is itself the finding:
> **everyone reports the mean (`TTN`, cycle life); the battery field also reports the distribution,
> the enzyme field almost never does.**

Bears on [[G3-cycle-life]], [[stress-strength-interference]], [[specification-instruments]].

---

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

**Enzymes live at `β ≤ 1`. That is the signature of catastrophe, not wear.**

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

| System | failure mechanism | axis | Weibull `β` | statistics |
|---|---|---|---|---|
| Enzyme, suicide inactivation | per-cycle covalent catastrophe (`p = 1/r`) | cycles | **≈ 1** | geometric / memoryless |
| Enzyme, thermal | first-order denaturation | time | **≈ 1** (`<1` if biphasic) | exponential |
| Organic flow reactant | chemical decomposition of the molecule | **time** | **≈ 1** | exponential |
| Li-ion cell | SEI growth + electrode fatigue, threshold at 80% | cycles | **> 1** (≈ 12.7 measured) | wear-out |

**`β` is the missing shared coordinate.** It spans both legs of G3, it is dimensionless, and it does
non-trivial work: it does **not** group by field (catalysis vs storage) — it groups by *failure
physics*, putting enzyme chemistry and flow-battery chemistry together at `β ≈ 1` and isolating
Li-ion electrode wear at `β > 1`. That is a genuine [[stress-strength-interference]]-style bridge:
the same discrete-catastrophe-vs-continuous-wear distinction, now carried by one published parameter.

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
durability object is 2-D, `(N_fail, β)`**, and `β` is the coordinate G3's fields never share because
each reports only its own `N_fail`.

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
2. **The shared axis that DOES exist is the Weibull shape parameter `β`** — reliability's
   random-vs-wear-out coordinate. It is dimensionless, it locates each field, and it reclassifies:
   **organic flow-battery reactants sit with enzymes at `β ≈ 1` (molecular chemical death), and
   Li-ion is the wear-out outlier at `β > 1`.** This is the [[specification-instruments]] residual
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

See [[G3-cycle-life]], [[stress-strength-interference]], [[specification-instruments]].
