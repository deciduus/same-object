# Blind brief — C43 paired test of the C35 `T`-vs-measured-formation prediction

**Written 2026-09-05, BEFORE any soil-production coordinate, any SSURGO `tfact` value, any
site-level join and any ratio was fetched, computed or inspected.** Purpose: turn C35 §5's
falsifier from a sentence into a pre-registered test by fixing the sample, the join rule, the
unit conversion, the statistics and the failure conditions in advance, and hashing this file.

**Blindness is partial and the limit is stated up front.** The coder (an AI) has read
[[C35-soil-ha]] in full and therefore already knows the *aggregate* numbers: Montgomery 2007
Table 1 soil-production median 0.017 mm/yr (n = 188), the `T` range 1–5 short ton/ac/yr, and
C35's derived 10.1–50.7× overstatement. This brief is blind with respect to **every per-site
quantity**: no site's coordinates, no site's `P`, no site's `tfact`, no site's bulk density and
no per-site ratio has been looked at. The aggregate ratio is a *prior*, not an outcome; a
per-site median ratio near it is a confirmation, and a per-site median ratio far from it is the
result that matters. C35 rows may be cited, never re-derived here.

## 1. Hypotheses

> **(H1 — primary, the C35 falsifier.)** At matched sites — a ¹⁰Be soil-production measurement
> joined to the USDA `T`-value of the soil map unit it falls in — the ratio `T / P_measured`
> exceeds **2** for the **majority** of sites (> 50%), and the **median** ratio exceeds 2.
>
> **(H2 — secondary, the sharper one.)** The ratio does **not** depend on the `T`-value class
> (1, 2, 3, 4, 5 ton/ac/yr). Equivalently, `T` does not track `P` across sites: Spearman
> ρ(T, P) is not distinguishable from 0. If `T` were an estimate of formation, higher-`P` sites
> would carry higher `T`, and ρ would be strongly positive.

H1 is C35's prediction restated per site. H2 is the stronger claim and is the one that decides
whether `T` is a *biased* formation estimate or *not a formation estimate at all*.

## 2. Sample and join rule, fixed in advance

**Sites.** Every soil-production (`P`) datum that satisfies all of:

1. a **¹⁰Be (or ¹⁰Be+²⁶Al) cosmogenic-nuclide** determination of soil production or of
   regolith/soil-mantled denudation used as production under local steady state;
2. a **published latitude and longitude** (or a locality precise enough that a published
   coordinate exists in the source paper — never a coordinate I infer from a place name);
3. located in the **conterminous United States, Alaska or Hawaii**, i.e. inside SSURGO/STATSGO2
   coverage. Non-US sites are excluded from the paired test by construction and appear only in
   §5's replication rows.

Source precedence, first that carries the site wins, recorded per row: (a) Montgomery 2007 SI
compilation; (b) the primary Heimsath papers it draws on (Nature `10.1038/41056` and the
Geomorphology / ESPL companions); (c) Dixon & von Blanckenburg 2012 (`10.1016/j.crte.2012.10.012`)
compiled table; (d) Stockmann et al. 2014 (`10.1016/j.geoderma.2013.10.007`) compiled table;
(e) the OCTOPUS ¹⁰Be database. A site appearing in two sources is entered once, from the earlier
source in this order, and the duplicate is noted.

**T-values.** `tfact` from USDA-NRCS SSURGO/gSSURGO, obtained by point-in-polygon at the site
coordinate via the Soil Data Access REST endpoint
(`SDA_Get_Mukey_from_intersection_with_WktWgs84` → `component`/`mapunit` join). Where SSURGO is
absent at a point, STATSGO2 `tfact` is used and the row is flagged. Where a map unit has several
components, the **dominant component by `comppct_r`** supplies both `tfact` and bulk density; if
components tie, the area-weighted mean is used and the row is flagged.

**Bulk density.** `dbthirdbar_r` of the surface horizon of the same dominant component. If
absent, C35's ρ_b = 1300 kg/m³ is substituted and the row is flagged as assumed.

## 3. The computation, fixed in advance

```
P   [mm/yr]  =  as published (10Be production/denudation rate)
T   [mm/yr]  =  tfact [short ton/ac/yr] x 2.2417 [t/ha per ton/ac] x 100 / rho_b [kg/m3]
ratio        =  T / P
Ha_T         =  P / T          (the C6-axis quantity: what Ha a T-permitted field runs at)
```

Ratios are analysed in **log10**. No site is dropped after its ratio is seen; the only permitted
exclusions are the §2 filters, which are fixed here.

## 4. Statistics, fixed in advance

1. **Median ratio** with a **percentile bootstrap 95% CI**, 10,000 resamples, seed **20260905**.
2. **Sign test** on `log(ratio) − log(2)`: two-sided exact binomial, H0 = median ratio is 2.
   Reported as k of n above 2 with its p-value.
3. **Spearman ρ** of `T` (mm/yr) against `P` (mm/yr) across sites, with its p-value, for H2.
4. **Stratification** of the median ratio by `tfact` class, reported as a table, no test.

## 5. Pass / fail, and the direction-only threshold

- **H1 PASSES** (C35's prediction survives) if the median ratio > 2 **and** the sign test rejects
  at p < 0.05 in the direction ratio > 2.
- **H1 FAILS** — C35's falsifier fires — if the median ratio falls in **[0.5, 2]**, or if the
  sign test rejects in the direction ratio < 2.
- **H2 PASSES** (T is not a formation estimate) if Spearman ρ is not significant at p < 0.05, or
  is negative.
- **Direction-only threshold: n < 12 matched sites.** Below 12, no CI, no p-value and no Spearman
  coefficient may be quoted as a result. The finding is reported as **direction only** — the sign
  of the median log-ratio and the count of sites above and below 2 — and the note must say the
  pre-registered test was **underpowered, not passed**. Below **n = 5** even the direction is not
  reported and the outcome is an **honest null on data availability**.
- If the SSURGO API is unreachable and no `tfact` can be obtained for any site, the outcome is an
  honest null on data access, and the ratio is **not** back-filled from C35's aggregate numbers.

## 6. What would make me wrong in a way I would not notice

- **The join is at map-unit scale.** A ¹⁰Be site is a ridge-crest point; a `tfact` is a polygon
  attribute for a soil series over a field. Agreement or disagreement at this scale is weaker
  evidence than the numbers will look.
- **Ridge crests are not fields.** Soil production is measured where soil is thin and production
  is fastest on the humped production function; `T` is assigned to farmed profiles. This biases
  `P` **upward** relative to a cropped site, which biases the ratio **downward** — i.e. against
  H1. A pass is therefore conservative and a fail is not.
- **¹⁰Be integrates 10³–10⁴ yr; `T` is an annual management permit.** They are not the same
  averaging window and no statistic here repairs that.
- **ρ_b enters both sides differently.** `T` passes through it, `P` does not. A ±18% ρ_b band is
  a ±18% band on every ratio and is smaller than the effect H1 predicts, but not than a
  near-boundary one.
