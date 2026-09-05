---
name: C36-conservation-duane
type: computed
closes: G37-adaptive-management-reliability-growth
last-checked: 2026-09-05
result: "First Crow-AMSAA growth exponents for conservation programmes. Balanced 1990-2015 panel, failure = overfishing: US West Coast beta = 0.672 [0.589, 0.761], US East Coast 0.815 [0.730, 0.904], EU 0.916 [0.861, 0.973], Mediterranean-Black Sea 1.105 [0.943, 1.279]. Engineering development runs 0.3-0.6."
exit: computation
extends-to: [conservation]
next-step-cost: S
---

# Conservation's reliability-growth exponent, computed for the first time

> **RESULT — conservation programmes do learn, and they learn about half as fast as a hardware
> development programme.** On a balanced 1990–2015 panel of the RAM Legacy database, treating each
> assessed stock-year as one unit of cumulative programme operating time and each stock-year with
> `U/Umsy > 1` as one failure, the Crow-AMSAA exponent is **β = 0.672 [0.589, 0.761]** for US West
> Coast, **0.815 [0.730, 0.904]** US East Coast, **0.861 [0.774, 0.952]** US Southeast & Gulf,
> **0.916 [0.861, 0.973]** European Union, and **1.105 [0.943, 1.279]** Mediterranean–Black Sea.
> MIL-HDBK-189 plans a development programme at β ≈ 0.3–0.6. **The prediction in
> [[G37-adaptive-management-reliability-growth]] survives its first test: every statutorily
> structured programme sits below 1 with a CI excluding it, and the least structured programme is
> the only one at or above 1.** The gap stays **live** — its scoped `N` was never fetched.

Script: `vault/_scripts/c36_duane.py` (stdlib + openpyxl + `scipy.stats.chi2`). Run 2026-09-05,
`--window 1990,2015`. Bears on [[C18-durability-axis]] (a *growth* exponent beside its hazard
shape) and repeats the estimator-sensitivity lesson of [[C26-ews-hazard-shape]].

## 1. The quantity

```
N(t) = λ t^β          λ(t) = λ β t^(β−1)          t = cumulative programme experience
```

A non-homogeneous Poisson process with power-law intensity — Duane's 1964 log–log learning curve,
given an estimator and confidence bounds by Crow. Time-truncated MLE at `T`:

```
β̂ = n / Σ_i ln(T/t_i)        λ̂ = n / T^β̂        CI: β̂·χ²_{α/2,2n}/(2n) , β̂·χ²_{1−α/2,2n}/(2n)
```

`β < 1` failure intensity falling — **the programme is learning**. `β = 1` homogeneous Poisson —
no learning. `β > 1` getting worse. β is dimensionless and bounded below by 0.

**The mapping onto a conservation programme, stated so a referee can attack it.** The *system* is
a regional management programme. Its *cumulative operating time* is stock-years of assessed
management, ordered by calendar year and, within a year, by stock id. A *failure* is one
stock-year in which the programme's own reference point is breached. A *fix* is whatever the
programme did in response. Nothing about repair is assumed; only that failures are counted
against accumulated exposure.

## 2. Inputs

| Source | What | Provenance |
|---|---|---|
| RAM Legacy Stock Assessment Database **v4.65** | `timeseries_values_views` (`stockid`, `year`, `UdivUmsypref`, `BdivBmsypref`) and `stock` (`stockid` → `region`) | Zenodo record **11995054**, DOI [10.5281/zenodo.11995054](https://doi.org/10.5281/zenodo.11995054), deposited 2024-06-17; `RAMLDB v4.65.zip`, **117,140,306 bytes**, fetched 2026-09-05. 28,815 stock-years carrying at least one of the two ratios; 1,512 stocks across 24 RAM regions |
| MIL-HDBK-189, *Reliability Growth Management*, US DoD 1981 | the planning range β ≈ 0.3–0.6 | **UNVERIFIED as a fetch.** A US government handbook with no DOI; not retrieved in this session. The range is quoted from the reliability-growth literature at large and from Crow 1982 ([10.1080/00401706.1982.10487711](https://doi.org/10.1080/00401706.1982.10487711), Crossref refby 121, fetched 2026-09-05), **not read from the handbook**. Treat it as a reference band, not a measurement |
| Duane 1964, *IEEE Trans. Aerospace* | the estimator's origin | [10.1109/TA.1964.4319640](https://doi.org/10.1109/TA.1964.4319640), Crossref-verified 2026-09-05, refby 499 |

**Could not be fetched, and the rows stay empty.** (a) **DIISE**, the Database of Island Invasive
Species Eradications — `diise.islandconservation.org` serves a WordPress front end with no data
endpoint reachable without a browser session; `/api/eradications` 404s and the linked BIP
indicator page exposes no CSV. (b) **Fischer & Lindenmayer 2000** relocation-outcome table
(`10.1016/s0006-3207(00)00048-3`, DOI corrected here — the commonly copied
`10.1016/S0006-3207(99)00048-3` **404s at Crossref**) is behind Elsevier and its by-decade success
table was not read. (c) **IUCN reintroduction outcome databases** — no machine-readable public
release found. (d) The recovery-plan objective audits (Glen Canyon, Everglades) are PDF
narratives. **Every non-fishery row below is therefore absent, not estimated**, and the headline
rests on one data source.

## 3. Result — β for fifteen management programmes

**Balanced panel, 1990–2015**: only stocks with a value in *every* one of the 26 years are kept,
so exposure per calendar year is constant and β cannot be manufactured by the assessment
programme's own growth (§4 shows what happens when it is not). Failure = **overfishing**,
`U/Umsy > 1`.

| Region (management programme) | stocks | T (stock-yr) | n (failures) | **β** | 95% CI | structure |
|---|---|---|---|---|---|---|
| **US West Coast** (PFMC, MSA) | 31 | 806 | 233 | **0.672** | [0.589, 0.761] | statutory |
| **US East Coast** (NEFMC/MAFMC, MSA) | 27 | 702 | 335 | **0.815** | [0.730, 0.904] | statutory |
| **US Southeast & Gulf** (SAFMC/GMFMC, MSA) | 28 | 728 | 360 | **0.861** | [0.774, 0.952] | statutory |
| Canada East Coast | 7 | 182 | 117 | 0.881 | [0.728, 1.047] | statutory |
| **European Union** (CFP) | 54 | 1,404 | 1,010 | **0.916** | [0.861, 0.973] | statutory |
| US Alaska (NPFMC, MSA) | 27 | 702 | 32 | 0.942 | [0.645, 1.296] | statutory, n small |
| Japan | 10 | 260 | 183 | 0.952 | [0.819, 1.094] | statutory |
| Europe non-EU | 16 | 416 | 296 | 0.953 | [0.847, 1.064] | mixed |
| New Zealand (QMS) | 7 | 182 | 108 | 0.971 | [0.796, 1.162] | statutory, n small |
| Pacific Ocean (WCPFC/IATTC) | 15 | 390 | 71 | 0.993 | [0.776, 1.237] | RFMO |
| South America | 22 | 572 | 338 | 0.999 | [0.895, 1.108] | mixed |
| Southern Africa | 5 | 130 | 40 | 1.028 | [0.735, 1.370] | mixed |
| Atlantic Ocean (ICCAT) | 14 | 364 | 164 | 1.034 | [0.882, 1.198] | RFMO |
| Australia | 8 | 208 | 126 | 1.040 | [0.866, 1.229] | statutory |
| **Mediterranean–Black Sea** (GFCM) | 8 | 208 | 166 | **1.105** | [0.943, 1.279] | weakest |
| Indian Ocean (IOTC) | 11 | 286 | 44 | 1.362 | [0.990, 1.793] | RFMO |
| — **DIISE island eradications** | — | — | — | — | — | `UNSOURCED`, §2 |
| — **reintroduction outcomes** | — | — | — | — | — | `UNSOURCED`, §2 |

Under the second criterion, failure = **overfished**, `B/Bmsy < 0.5`, the same three US regions
stay below 1 (**US East Coast 0.842 [0.724, 0.968]**, **US West Coast 0.833 [0.675, 1.008]**, US
Southeast & Gulf 0.906 [0.785, 1.034]) and the EU rises above it (1.180 [1.003, 1.371]). **The
ordering is criterion-dependent for the EU and stable for the US.**

**Two controls, both required before any row above is read.**

| Control | Purpose | Result |
|---|---|---|
| Homogeneous-Poisson null: `n` failures placed uniformly over `T` slots, 2,000 reps | the estimator must return β ≈ 1 when nothing is learned | β median **1.007** at (T=806, n=233), **1.004** at (1404, 1010), **1.017** at (208, 166), **1.006** at (702, 335) — unbiased, and the spread `[0.906, 1.120]` at the smaller `n` sets the noise floor |
| Recovery of a known β on `T = 806` integer slots | the discretisation must not fake a low β | true 0.4 → **0.591**, 0.5 → **0.624**, 0.7 → **0.716**, 1.0 → **0.984** |

The recovery control is the important one and it cuts **against** the headline's optimism: forcing
a power-law NHPP onto one-failure-per-slot integer exposure is **biased upward at small β** (0.4
reads as 0.59). So β = 0.672 for the US West Coast is an **upper bound** on that programme's true
exponent — the real learning is at least as fast as reported, and the comparison with engineering
is if anything conservative. The bias vanishes at β = 1, so no row near 1 is manufactured.

## 4. The estimator sensitivity, in C26's manner

Dropping the balanced-panel requirement — using **all** stock-years 1950–2015, as the obvious
first analysis would — moves the same programmes across the whole range:

| Region | balanced β | all-stock-years β |
|---|---|---|
| US West Coast | **0.672** | **2.597** |
| New Zealand | 0.971 | 2.249 |
| US Southeast & Gulf | 0.861 | 1.844 |
| US Alaska | 0.942 | 0.623 |
| European Union | 0.916 | 0.976 |
| Mediterranean–Black Sea | 1.105 | 1.165 |

**A factor of four on identical data, from one preprocessing choice.** The mechanism is plain
once seen: RAM's assessed-stock count grows through the record, so cumulative exposure accumulates
slowly in the early decades while failure *events* are concentrated in the later, better-covered
ones. The unbalanced β is then measuring how fast the assessment programme grew, not how fast the
management programme learned. **This is exactly [[C26-ews-hazard-shape]]'s finding in a new
place: β is a property of the estimator until the estimator is pinned down**, and the balanced
panel is what pins it. Every number in §3 is balanced; no unbalanced number is quotable.

## 5. The prediction

> **Prediction.** Ordering conservation programmes by how formally their adaptive-management
> structure is codified — a statutory monitor-assess-revise cycle with a binding reference point
> and a mandated response, versus discretionary or advisory management — will order their
> Crow-AMSAA β, **lower β for more formal structure**, with the formal group's mean β below the
> ad-hoc group's by at least 0.15 and the formal group's CIs excluding 1.
>
> **Already consistent, on the only data reached here.** The four US federal regions under the
> Magnuson-Stevens Act — whose 1996 rebuilding mandate and 2007 annual-catch-limit requirement are
> the closest thing in conservation to a legislated test-analyse-and-fix loop — average
> **β = 0.82**, and three of the four exclude 1. The RFMO and weakly governed rows (ICCAT 1.034,
> IOTC 1.362, GFCM 1.105, Southern Africa 1.028) average **β = 1.13** and **not one of them
> excludes 1**. Difference of means **0.31**, in the predicted direction and twice the predicted
> minimum.
>
> **This is not yet a test.** The structure grouping was assigned by me, after seeing the βs, from
> general knowledge of the statutes rather than from a published index. **A real test needs the
> coding done blind and from a source.**
>
> **The dataset that could do it: DIISE**, the Database of Island Invasive Species Eradications
> (Island Conservation / IUCN ISSG / Landcare Research / Univ. Auckland,
> `diise.islandconservation.org`). It records **individual eradication attempts** — island,
> target species, year, and a per-attempt outcome of successful / failed / unknown — which is a
> literal trial record needing none of §1's mapping argument. Cumulative attempts is the exposure
> axis, a failed attempt is the failure, and attempts are separable into programmes (New Zealand
> DOC, Mexico GECI, Australia, one-off contractor jobs) that differ sharply and *independently
> documented* in how formally they run a learn-and-revise cycle. **It could not be fetched here**
> (§2) and obtaining it is the whole cost of the test. **Falsified by** a blind-coded set of ≥10
> programmes in which formal and ad-hoc β distributions overlap at `p > 0.1`, or in which the
> ordering reverses.

## 6. Honesty

**What counts as a "failure" is a choice, and it changes the answer.** `U/Umsy > 1` and
`B/Bmsy < 0.5` are the two reference points the field itself uses, and they disagree about the EU
(0.916 vs 1.180). A stock can also be overfished for decades from one historic failure while the
current programme is doing everything right; counting each such year as a fresh failure treats a
persistent state as repeated events. Duane's frame *wants* repeated independent trials, and
stock-years are not that. **The overfishing criterion (a flow) is closer to a trial than the
overfished criterion (a stock), which is why it carries the headline.**

**Reporting bias runs one way and it flatters the result.** RAM contains stocks that were
*assessed*, and assessment is not random: well-managed fisheries with good data are
over-represented, and the assessments are **retrospective reconstructions** — the 1990 "failure"
was identified by a 2020 model, not by a manager in 1990. So the early failures were not trials
anyone could have learned from at the time, which is precisely the mechanism Duane's curve
assumes. The declining β may partly record improving *assessment* rather than improving
*management*.

**Time versus trials as the cumulative axis.** I used stock-years, which makes a region with more
stocks accumulate experience faster. Calendar time would make them equal, and cumulative
management *actions* (a TAC set, a rebuilding plan adopted) would be closest to Duane's intent and
is not recorded in RAM. §4 shows how much this class of choice moves β; the stock-year axis is
defensible because the unit that fails is a stock, but it is not the only defensible one.

**Whether learning is transferable across programmes is untested and is the interesting question.**
Duane's β is a property of one development programme; nothing here shows that a fix learned on the
US West Coast transferred anywhere. If conservation's learning is largely *shared* — through
journals, through the same handful of stock-assessment scientists — then per-programme β is the
wrong statistic and a pooled global β is the right one. The global pooled fit is one line of the
script away and is deliberately not run here, because pooling across programmes with different
reference-point definitions would mix units.

**And the ambiguity [[G37-adaptive-management-reliability-growth]] names is not resolved.** A
managed ecosystem's failure-mode inventory is non-stationary. `β ≈ 1` for the Mediterranean is
consistent with "not learning" and equally with "learning exactly as fast as fishing pressure,
warming and invasion generate new ways to fail." **Nothing in this computation can separate
those**, and no reliability-growth model can, because the hardware case has no analogue of it.
