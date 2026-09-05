# Blind brief — C44, the world soil-`Ha` ledger at site level

**Written 2026-09-05, BEFORE any non-US site was joined to any erosion value, before any
country median, any land-cover stratum and any correlation coefficient was computed or seen.**
Purpose: fix the sample, the join rule, the unit chain, the statistics and the failure
conditions for taking [[C43-soil-ha-replication]]'s join off United States ground, and hash this
file. Programme item P-001, Track A.

**Blindness is partial and the limit is stated up front.** The coder (an AI) has read C43 in
full and therefore knows the **US** result (median `T`/`P` = 22.3, n = 1,053, ρ(`T`,`P`) =
−0.18) and C43 §5's **regional** `Ha` rows computed from continental *mean* erosion (Europe
0.187 / 0.499, Australia 0.120, Asia 0.077, North America 0.096). Those are priors. This brief
is blind with respect to **every per-site non-US quantity**: no site's erosion value, no country
median, no land-cover stratum, no Spearman coefficient has been looked at. A site-level country
median near C43 §5's continental row is a confirmation; one far from it is the result that
matters, because §5's rows divide a regional median `P` by a *continental mean* `E` and
therefore cannot see within-country covariance between the two at all.

## 1. Hypotheses

> **(H1 — primary.)** At matched sites worldwide — a ¹⁰Be denudation rate joined to a modelled
> erosion rate for the same location — site-level `Ha` = `P`/`E` is **below 1** for the
> **majority** of sites (> 50%), and the **median** `Ha` is below 1. Soil is being spent faster
> than it is made, everywhere it has been measured, not only in the regions C43 §5 averaged.
>
> **(H2 — secondary, as posed.)** The US finding — that the policy tolerable-loss value `T`
> anti-correlates with measured formation `P` — reproduces outside the United States at site
> level.

**H2 is expected to be untestable as posed, and this brief says so in advance.** `T` is a
per-map-unit attribute of a national soil survey. The USDA `tfact` field has no counterpart in
the European Soil Database, which publishes **no per-site tolerable-loss layer**; Verheijen et
al. 2009 is a *proposed* single range for Europe, not a mapped per-polygon value. Australia,
China and India likewise publish national or class-level numbers, not queryable per-site layers.
**If no per-site `T` layer is reachable for any non-US country, H2 is recorded as NOT TESTED —
never as failed, and never back-filled from the US result.** Its replacements, fixed here, are:

> **(H2a — replacement, per-country ledger.)** Median site-level `Ha` per country, with a
> percentile bootstrap 95% CI, reported only for countries with **n ≥ 10** sites.
>
> **(H2b — replacement, land-cover ledger.)** Median site-level `Ha` per land-cover class.
>
> **(H2c — replacement, the multi-country version of the US finding.)** Where a country has a
> **published national tolerable-loss number**, compute `T`/`P_measured` at that country's
> sites, `T` taken from the publication and applied uniformly to the country. This is a
> country-constant `T` against a site-varying `P`, so it can test the **level** of the US
> finding but **cannot** test its correlation; that limitation is fixed here, in advance.

## 2. Sample and join rule, fixed in advance

**Sites (`P` side).** Every record in the OCTOPUS v2.2 ¹⁰Be collection — layers
`be10-denude:crn_int_basins`, `crn_int_outlets`, `crn_aus_basins` (and any further ¹⁰Be
basin/outlet layer the WFS `GetCapabilities` advertises) — satisfying all of:

1. a positive `EBE_MMKYR` (CAIRN-harmonised ¹⁰Be denudation rate);
2. a geometry from which a point can be taken: an outlet `POINT`, else the basin centroid;
3. a non-empty `CNTRY`.

No bounding box. United States sites are retained for comparison but reported separately, since
C43 already owns them.

**Erosion (`E` side).** Borrelli et al. 2017, *Nat. Commun.* **8**:2013,
`10.1038/s41467-017-02142-7`, gold OA — the global RUSLE-based soil-erosion product, ~25 km,
2012 (and 2001). Precedence, first reachable wins, recorded in the note:

- (a) the **global raster** (GeoTIFF) from the paper's Data Availability — ESDAC/JRC, else
  figshare/Zenodo — sampled at the site point;
- (b) the paper's **country-level table** of mean erosion rate, joined on `CNTRY`;
- (c) the paper's **continental** rates, joined on continent.

**If only (b) or (c) is reachable the join is at country or continent level, `E` is constant
within the joined unit, and the note must say so in its first section.** Under (b) or (c) the
P-vs-E Spearman of §4 is uninformative about within-country covariance and must be reported as
such, not suppressed.

**Land cover.** ESA CCI or MODIS land cover at the site point via a point/WMS query if one is
reachable without registration; else Borrelli's own land-cover-stratified rates, in which case
the land-cover ledger is a statement about Borrelli's strata and not about the sites.

## 3. The computation, fixed in advance

```
P [mm/yr] = EBE_MMKYR / 1000
E [mm/yr] = erosion [t/ha/yr] * 100 / rho_b [kg/m3],  rho_b = 1300 (C35/C43 assumption)
Ha        = P / E
T/P       = (T_national [t/ha/yr] * 100 / rho_b) / P      (H2c only)
```

ρ_b = 1300 kg/m³ is fixed here and is not tuned. No site is dropped after its `Ha` is seen; the
only permitted exclusions are the §2 filters.

## 4. Statistics, fixed in advance

1. **Median `Ha`** overall and **per country**, each with a **percentile bootstrap 95% CI**,
   10,000 resamples, seed **20260905**. **Countries with n < 10 sites are not reported
   individually** and appear only in their continent's row.
2. **Sign test** on `log Ha < 0`: two-sided exact binomial, H0 = median `Ha` is 1. Reported as
   k of n below 1 with its p-value.
3. **Spearman ρ of `P` against `E`** across sites, with its p-value. **If formation and erosion
   are independent, ρ ≈ 0.** A strong positive ρ would mean the two products co-vary (shared
   topographic driver, or `E` partly reconstructing relief); a strong negative ρ would mean
   erosion is worst where formation is slowest — the global form of the C43 §3 mechanism.
4. **Median `Ha` by continent** and **by land-cover class**, as tables, no test.
5. **H2c:** median `T`/`P` per country with a published national `T`, n and CI, alongside C43's
   US median of 22.3.

## 5. Pass / fail, and the direction-only threshold

- **H1 PASSES** if the median site-level `Ha` < 1 **and** the sign test rejects at p < 0.05 in
  the direction `Ha` < 1.
- **H1 FAILS** if the median `Ha` ≥ 1, or the sign test rejects in the direction `Ha` > 1. A
  median `Ha` in **[0.8, 1.25]** with a non-rejecting sign test is reported as **the ledger
  balances**, which is a fail of H1 and is the outcome that would matter most.
- **H2** is **NOT TESTED** if no per-site non-US tolerable-loss layer is reachable. This is the
  expected outcome and is not a failure of the run.
- **Direction-only threshold: n < 12 matched sites** in any reported cell. Below 12, no CI, no
  p-value and no Spearman may be quoted for that cell; only the sign of the median and the
  counts above and below 1. Below **n = 5**, not reported at all.
- If the Borrelli product is unreachable in **all three** forms of §2, the outcome is an **honest
  null on data access**, and no `Ha` is back-filled from C43 §5 or C35.
- No country is dropped, merged or renamed after its median is seen.

## 6. What would make me wrong in a way I would not notice

- **Basin-averaged denudation is not soil production.** C43 §4 measured the direction and size
  from Dixon & von Blanckenburg 2012: denudation exceeds soil production by ~1.62× at the global
  median. `P` is therefore **inflated**, `Ha` is **inflated**, and the bias runs **against** H1.
  A pass is conservative; a fail is not.
- **RUSLE-modelled erosion is not measured erosion.** Borrelli's `E` is a model output driven by
  rainfall erosivity, slope, soil erodibility and a land-cover C-factor. Where it is wrong it is
  wrong in a way correlated with terrain — the same terrain that drives `P` — so §4's ρ can be
  manufactured by shared inputs rather than by any physical coupling. This is the weakest joint
  in the run and no statistic here repairs it.
- **25 km cells against basins of every size.** A cell is a regional average; an OCTOPUS basin
  may be 1 km² or 10⁵ km². The join is between two different supports and agreement will look
  stronger than it is.
- **ρ_b = 1300 kg/m³ enters `E` and not `P`.** A ±20% ρ_b band is a ±20% band on every `Ha`,
  which is smaller than the factor H1 asks about and larger than a near-boundary verdict.
- **10⁴-yr `P` against a 2012 modelled `E`.** Commensurable in units and in nothing else. Modern
  agricultural erosion is a decadal quantity; ¹⁰Be is Holocene-averaged. Every `Ha` in this note
  is a ratio across four orders of magnitude of averaging window.
- **`CNTRY` is where the sample was taken, not where the erosion problem is.** OCTOPUS is a
  geomorphology collection: its basins are chosen for mountains, bedrock and accessibility, not
  for farmland. A per-country median is a median over that sampling, and the countries best
  represented are the ones geomorphologists work in.
