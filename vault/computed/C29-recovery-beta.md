---
name: C29-recovery-beta
type: computed
exit: prediction
extends-to: [ecology, conservation]
next-step-cost: M
---

# Ecological recovery has a *decreasing* hazard: pooled Weibull β = 0.587 (95% profile CI 0.510–0.668) over 221 censored recovery records. Recovery is not a clock — it is early-or-never.

> **Fitting Jones & Schmitz 2009's own 240-study recovery table as a right-censored survival
> problem gives a Weibull shape parameter `β = 0.587 [0.510, 0.668]` pooled, and `β < 1` with the
> CI clear of 1 in four of five habitat classes.** On [[C18-durability-axis]]'s axis that is the
> *infant-mortality* corner — the same corner C18 assigned to biphasic enzyme death, and the
> opposite corner from Li-ion wear-out (`β ≈ 12.7`). **The hazard of recovering falls with time
> since disturbance: a system that has not come back in the first decade is less likely to come
> back next year than it was in year one.** That is [[G32-recovery-time-hazard-shape]]'s missing
> object, and it makes Moreno-Mateos et al.'s "recovery debt" a *distributional* statement rather
> than a mean one. It does **not** show a mechanism: `β < 1` is equally the signature of a
> genuinely decelerating process and of a pooled mixture of fast and slow recoverers, and §6 says
> honestly that this dataset cannot separate them.

Closes the computation exit of [[G32-recovery-time-hazard-shape]]. Extends
[[C18-durability-axis]]. Same instrument as [[C26-ews-hazard-shape]] on a different estimand;
the consumer-product analogue is [[C27-product-lifespan-beta]] via
[[G30-weibull-product-lifespan]].

## 1. The quantity

```
S(t) = exp( −(t/η)^β )        h(t) = (β/η)·(t/η)^(β−1)
   t  = time since the disturbance ceased, in years
   event      = "Recovered? = Yes"  at the stated return time
   censored   = "Recovered? = No"   at the stated end-of-observation time
```

- `β > 1` — recovery hazard **rises**: the longer since disturbance, the more likely recovery is
  *this* year. Recovery "accelerates"; the system has positive memory (successional facilitation,
  compounding regrowth).
- `β = 1` — memoryless. A constant annual probability of recovering, independent of how long the
  system has already been broken. This is the exponential-return assumption implicit in
  [[G32-recovery-time-hazard-shape]]'s Pimm-1984 vocabulary: a single return **rate**.
- `β < 1` — recovery hazard **falls**: early recovery or effectively none. The recovery-debt shape.

`η` is the scale (the 63.2nd percentile of recovery time), in years. `β` is dimensionless, which
is what lets it sit on C18's axis next to a battery and an enzyme.

## 2. Inputs

| Input | Value | Source / fetch |
|---|---|---|
| Recovery table | 240 studies, cols `Habitat / Disturbance / Response Variable(s) / Recovered? / Return Time / Control / Citation` | Jones & Schmitz 2009, *PLoS ONE* 4(5):e5653, Table S1, `doi 10.1371/journal.pone.0005653.s001`, **fetched 2026-09-05** from `journals.plos.org/plosone/article/file?type=supplementary&id=info:doi/10.1371/journal.pone.0005653.s001` (200, `application/vnd.ms-excel`, 144,896 bytes) |
| Article DOI verification | "Rapid Recovery of Damaged Ecosystems", *PLoS ONE*, 2009-05-27, `is-referenced-by-count = 285` | Crossref `api.crossref.org/works/10.1371/journal.pone.0005653`, **fetched 2026-09-05** |
| Fit code | `vault/_scripts/c29_recovery.py` | this vault; MLE with `η` profiled out, profile-likelihood CI at Δ logL = 1.921 |

**Row accounting** (all 240 data rows; rows 241+ of the sheet are the appended reference list and
are discarded by the loader):

| | rows |
|---|---|
| Data rows read | 240 |
| Dropped — `Return Time` carries no parseable duration ("Several decades", "Few years", "1 growing season", "NA") | 10 |
| Dropped — `Recovered?` is neither yes nor no (blank or "NA - modeling") | 7 |
| Dropped — habitat not one of the five groups ("NA") | 2 |
| **Used** | **221** (127 events, 94 right-censored) |

Censoring is **42.5%** of the usable rows. That is the number ecology's mean return time discards:
the mean over the recovered rows only is **17.95 yr (n = 127)**, and it cannot see the 94 studies
that ended without recovery at all.

## 3. Result — β by habitat

Profile-likelihood 95% CI. `*` marks a CI lying entirely below 1.

| Habitat | N | events | censored | **β** | 95% CI | η (yr) | |
|---|---|---|---|---|---|---|---|
| Forest | 78 | 45 | 33 | **0.769** | [0.611, 0.937] | 79.6 | `*` |
| Marine (benthic + pelagic) | 47 | 30 | 17 | **0.644** | [0.487, 0.813] | 7.4 | `*` |
| Freshwater (benthic + pelagic) | 52 | 29 | 23 | **0.893** | [0.644, 1.186] | 25.3 | — |
| Brackish | 25 | 15 | 10 | **0.501** | [0.309, 0.751] | 13.3 | `*` |
| Terrestrial (non-forest) | 19 | 8 | 11 | **0.570** | [0.295, 0.925] | 71.8 | `*` |
| **ALL POOLED** | **221** | **127** | **94** | **0.587** | **[0.510, 0.668]** | **39.4** | `*` |

**Four of five habitat classes reject `β = 1` downward at 95%.** Freshwater is the one class whose
CI covers 1 (`β = 0.893 [0.644, 1.186]`) — memorylessness is not excluded there.

### By disturbance type (N ≥ 10)

| Disturbance | N | events | **β** | 95% CI | η (yr) |
|---|---|---|---|---|---|
| Trawling | 12 | 8 | **0.421** | [0.229, 0.654] | 7.5 |
| Oil spill | 39 | 27 | **0.652** | [0.469, 0.868] | 4.2 |
| Logging | 50 | 26 | **0.679** | [0.505, 0.867] | 78.3 |
| Deforestation | 10 | 8 | 0.884 | [0.455, 1.486] | 34.0 |
| Invasive species | 12 | 3 | 0.972 | [0.295, 2.078] | 22.1 |
| Eutrophication | 45 | 22 | **1.025** | [0.697, 1.423] | 29.1 |
| Agriculture | 27 | 15 | **1.254** | [0.815, 1.774] | 81.0 |

The ordering is the interesting half and it is not the one intuition supplies. **Acute physical
pulses (trawling, oil spill) sit lowest — the most sharply decreasing hazard — while chronic
land-use presses (eutrophication, agriculture) sit at or above `β = 1`.** No disturbance class
rejects `β = 1` *upward*; agriculture is the only one whose point estimate exceeds 1.25, and its
CI still covers 1.

### Sensitivity

| Variant | β | 95% CI |
|---|---|---|
| Ranges coded at the midpoint (headline) | 0.587 | [0.510, 0.668] |
| Ranges coded at the low end | 0.580 | [0.504, 0.661] |
| Ranges coded at the high end | 0.590 | [0.513, 0.672] |
| Censored rows dropped entirely (ecology's implicit estimator) | 0.640 | [0.556, 0.731] |

The free-text range coding moves `β` by under 2%. Dropping the censored rows moves it by 9% and —
note the direction — **still leaves `β < 1`**: the decreasing hazard is not manufactured by the
censoring convention. It also collapses `η` from 39.4 to 13.0 yr, which is the recovery-debt
optimism restated as a scale parameter.

## 4. Placing it on C18's axis

| System | axis | β | corner |
|---|---|---|---|
| Li-ion cell (NCR18650GA) | cycles | ≈ 12.7 | wear-out |
| Enzyme, suicide inactivation / thermal | cycles / time | ≈ 1 | memoryless catastrophe |
| Organic flow-battery reactant | time | ≈ 1 | memoryless catastrophe |
| Enzyme, biphasic (fragile subpopulation) | time | < 1 | infant mortality |
| **Ecological recovery, pooled (this note)** | **time** | **0.587 [0.510, 0.668]** | **infant mortality** |

Two things follow. First, **ecological recovery is the far end of the axis from Li-ion**, and it is
the *only* entry in the vault that sits at `β < 1` with a fitted confidence interval rather than by
inference. Second — the uncomfortable one — **the ecological entry lands in the same corner C18
assigned to enzyme *heterogeneity*, not to any mechanism of recovery.** C18 §2.1 says a fragile
subpopulation dying first pushes `β` below 1. A meta-analysis pooling day-scale water-column
chemistry with century-scale forest biomass is a subpopulation mixture by construction. §6 does not
let this pass.

## 5. Prediction

**Which ecosystem types should show `β < 1` on a new meta-analysis, and how to check it.**

1. **The primary prediction, stated to be falsifiable.** Re-fit on a recovery dataset that was
   *not* Jones & Schmitz — Moreno-Mateos et al. 2017 (`10.1038/ncomms14163`, the recovery-debt
   paper) or Crouzeilles et al. 2016 (`10.1038/ncomms11666`, 221 forest-restoration studies) — and
   the habitat ordering above should reproduce: **`β` lowest for marine benthic and brackish
   systems (0.4–0.7), highest for freshwater pelagic and agricultural-press systems (0.9–1.3),
   forest intermediate (~0.75).** The prediction is not the numbers, which the CIs already
   bracket loosely; it is **the sign of the rank correlation between the two datasets' per-habitat
   `β`**, which should be positive. A null or negative correlation kills the claim that `β`
   measures anything about ecosystems rather than about how each meta-analyst coded the free text.
2. **The mechanism discriminator, which this dataset cannot run and a new one could.** Split each
   habitat by **response variable class** before fitting: structural/biomass variables versus
   compositional/species variables. If `β < 1` is real deceleration, it should survive the split
   *within* a variable class. If `β < 1` is mixture heterogeneity, **the within-class `β` should
   rise toward 1 while the pooled `β` stays at 0.59** — the classic frailty signature. Jones &
   Schmitz's `Response Variable(s)` column is free text with multiple variables per row, so the
   split is not machine-runnable here; Moreno-Mateos 2017 reports per-variable effect sizes and
   is.
3. **The recovery-debt corollary.** `β = 0.587` and `η = 39.4 yr` imply that a system still
   unrecovered at 40 years has an annual recovery hazard **≈ 0.30×** its hazard in year one
   (`h(40)/h(1) = 40^(β−1) = 40^(−0.413)`). That is a number a restoration programme can be held
   to: **conditional on 40 years of failure, the next year is three times less promising than the
   first year was** — which is the opposite of the "give it time" default and is checkable against
   any long-term restoration monitoring series with dated non-recoveries.

## 6. §Honesty — what this fit does not establish

- **Censoring is informative, and that is the worst problem here.** Studies stop for funding and
  publication reasons, not at random with respect to recovery. A study that ends at year 5 with
  "not recovered" is coded as censored at 5, but the reason it ended at 5 may be correlated with
  how badly it was going. Standard right-censoring MLE assumes independence of censoring and
  event time, and that assumption is certainly violated in a publication-derived table. Direction
  of the resulting bias is not determined by this note.
- **Site and timescale heterogeneity is not separated from mechanism.** This is the §4 objection
  in full force. Pooling a 5-day plankton recovery with a 175-year forest-biomass recovery
  produces a mixture whose marginal hazard is decreasing even if every component is memoryless.
  **`β < 1` measured on a pooled meta-analysis is consistent with "recovery decelerates" and with
  "recovery rates vary enormously across systems", and this dataset cannot tell them apart.**
  Prediction 5.2 is the test; until it is run, the honest reading of `β = 0.587` is *"the marginal
  hazard of the pooled ecological-recovery population is strongly decreasing"*, not *"any
  individual ecosystem's recovery hazard decreases"*.
- **"Recovery" is not one definition.** Each of the 240 rows applies its own criterion — return to
  a pre-disturbance value, to an undisturbed reference site, or to a modelled baseline (the
  `Control` column records which, and it varies row to row). A stricter criterion lengthens the
  time and converts events into censorings, and the criteria are not distributed at random across
  habitats. `η` in particular should not be quoted across habitats as if it measured one thing.
- **Free-text duration coding is mine, not the authors'.** `Return Time` is prose; the loader
  takes the first duration expression it finds, collapses ranges to a midpoint, and ignores
  qualifiers ("~", ">", "at least"). 10 rows had no parseable duration and were dropped rather
  than imputed. The §3 sensitivity shows the collapse rule barely matters, but it does not defend
  the choice of *which* number to take when a cell lists several ("2 months; 17 months of study
  and little recovery for others").
- **Recovery is not failure, and the hazard metaphor is borrowed.** [[G32-recovery-time-hazard-shape]]
  states the risk: a Weibull fit to recovery times describes assembly (colonisation, regrowth), not
  degradation, so the reliability intuition for `β` — accumulating damage — has no counterpart. The
  parameter is well-defined as a hazard either way; what does *not* transfer is C18's mechanistic
  reading of `β > 1` as wear-out. Nothing in this note depends on that reading, and the result
  happens to sit on the side of the axis where the metaphor is least strained.
- **A rejected alternative was not fitted.** The scout note for G32 raised lognormal recovery times
  (products of rates) as the competitor to Weibull. This note fits Weibull only, because `β` is the
  object C18 needs; **no goodness-of-fit comparison against a lognormal or a gamma was run**, so
  "Weibull with β = 0.587" is a parameterisation, not a demonstration that the Weibull family is
  the right one.
