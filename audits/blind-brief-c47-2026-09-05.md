# Blind brief — C47, the `tfact` mechanism pre-registered and tested on independent sites

**Written 2026-09-05, BEFORE any new site's `tfact`, restriction depth, slope or ¹⁰Be erosion
rate was fetched, joined or inspected.** Purpose: convert the mechanism [[C43-soil-ha-replication]]
§3 found *in the data* — "`T` is assigned on profile depth, so `T` anti-correlates with measured
formation by construction" — into a pre-registered test on sites C43 did not use. Programme item
P-079.

**What is already known and is therefore not blind.** The coder has read C43 in full and knows
its aggregate results (ρ(`T`,`P`) = −0.180, ρ(`tfact`,`P`) = −0.206, the class table with median
`P` = 0.173 mm/yr at `tfact` = 1 and 0.026–0.029 at classes 3–5). The coder has also read the
USDA rule text quoted in §2 below — that is the *content* of the hypothesis, not an outcome.
Blind with respect to: every new site's coordinates-to-`tfact` join, every new site's restriction
depth, every new site's erosion rate, and every statistic computed from them.

## 1. Hypotheses, fixed in advance

> **H1 (mechanism).** At US sites not used in C43, `tfact` is a deterministic function of the
> SSURGO depth to a root-restricting layer with the NRCS class boundaries. **Predicted agreement
> ≥ 90%** between observed `tfact` and the depth-predicted class.
>
> **H2 (consequence).** ¹⁰Be erosion rate `P` decreases with depth class:
> **Spearman ρ(`P`, depth class) < 0 with p < 0.01**, and ρ(`tfact`, `P`) < 0 replicates on the
> new sites.
>
> **H3 (the sharper claim).** Within a single `tfact` class, `T` does not track `P` at all:
> **|ρ| < 0.1** in each class with n ≥ 25. `T` carries no formation information beyond the
> depth class.

H1 is the mechanism. H2 is the bridge from mechanism to C43's correlation. H3 is what separates
"`T` is a depth label" from "`T` is a noisy formation estimate".

## 2. The USDA rule, quoted before the test

National Soil Survey Handbook, Part 618 Subpart B (Amended August 2024), §618.91, read
2026-09-05 from the NRCS directives PDF
`https://directives.nrcs.usda.gov//sites/default/files2/1725389663/National%20Soil%20Survey%20Handbook%20%28entire%20handbook%29.pdf`
(HTTP 200, 11,795,683 bytes, 1,177 pp.; §618.91 begins on p. 431 of the PDF):

> "Soil loss tolerance 'T' is assigned according to properties of root and plant growth limiting
> subsurface soil layers."

Figure 618B-3, "Soil Loss Tolerance in Tons Per Acre by Group", depth to limiting layer in cm:

| Depth to Limiting | Group 1 | Group 2 | Group 3 |
|---|:-:|:-:|:-:|
| 0 – 25 | 1 | 1 | 3 |
| 25 – 50 | 1 | 2 | 3 |
| 50 – 100 | 2 | 3 | 4 |
| 100 – 150 | 3 | 4 | 4 |
| > 150 | 5 | 5 | 5 |

Group 1 = permanent/nonrenewable root limitation; Group 2 = moderate or less-than-permanent;
Group 3 = overcome by natural or managed processes. Two documented exceptions are quoted here so
that H1 is not tested against a rule the handbook does not state: subaqueous soils "are excluded
from assignment of T factors", and "Severely eroded soils, as designated by the local phase or
erosion class of 3 or 4, are adjusted one class of T factor lower."

**The predicted class used for H1's headline number is the Group 2 column**
(< 25 → 1, 25–50 → 2, 50–100 → 3, 100–150 → 4, > 150 → 5), because it is the column that matches
the plain depth rule the mechanism claim asserts. A **band agreement** is reported alongside:
the observed `tfact` falls inside the min–max of the three group columns for its depth bin. Both
numbers are pre-registered; the ≥ 90% gate applies to the Group 2 number, and if that fails while
band agreement passes, the honest conclusion is "depth **plus** a renewability group", not "not
depth".

## 3. Independent sites, fixed in advance

C43 used OCTOPUS v2.2 `be10-denude:crn_int_outlets` + `crn_int_basins` inside a CONUS bbox,
basin-averaged `EBE_MMKYR`, and cached the resulting 1,053 joins in
`_scripts/c43_data/sites.json`. Two OCTOPUS layers outside that cache were checked first and are
recorded here as exhausted: `crn_xxl_basins` has 6 USA rows, all with `EBE_MMKYR` = −9999.99
(no rate); `crn_inprep_basins` has 0 USA rows. **So OCTOPUS supplies no usable independent US
sites** and the second compilation is the sample.

**Sample.** Portenga & Bierman 2011, "Understanding Earth's eroding surface with ¹⁰Be",
*GSA Today* 21(8):4–10, `10.1130/G111A.1` (Crossref, fetched 2026-09-05: title, container-title,
volume, issue and pages confirmed). GSA supplemental data item 2011216, now on Figshare
(`10.1130/2011216`, CC BY-NC 4.0, `2011216.pdf`, 1,753,000 bytes), **Table DR2 — Bedrock Outcrop
Data**, a per-sample table with published decimal-degree latitude and longitude.

Table DR2 is used, not DR3, for one pre-registered reason: DR2 rows are **outcrop point
samples**, so the point-vs-basin scale mismatch C43 §6 named as its weakest joint is reduced,
and outcrop samples are a different measurement type from OCTOPUS's basin averages.

**Inclusion.** A DR2 row is used iff it carries a latitude and longitude, the coordinate lies in
the CONUS box (lon −125 to −66, lat 24 to 50), and it carries a positive CRONUS erosion rate.
`P` [mm/yr] = CRONUS erosion rate [m My⁻¹] / 1000.

**Exclusion (the independence rule).** Any site within **0.005°** of any of the 1,053 C43 site
coordinates in `c43_data/sites.json` is dropped, and the number dropped is reported.

**H1's second sample.** H1 needs no erosion rate, so it is also run on **1,500 pseudo-random
CONUS points**, uniform in the CONUS box, `random.Random(20260905)`, drawn before any SDA call,
non-answering points discarded. This is the powered test of the depth rule; the DR2 sites give
the same test on the H2/H3 sample.

## 4. The queries and the derived quantities, fixed in advance

Soil Data Access REST, `SDA_Get_Mukey_from_intersection_with_WktWgs84('point(lon lat)')`, the
same endpoint C43 used. Per point, the **dominant component by `comppct_r`** supplies
`tfact`, `slope_r`, `comppct_r`, and surface `dbthirdbar_r`.

**Restriction depth** = the minimum `resdept_r` over that component's rows in `corestrictions`.
If the component has no restriction row, `muaggatt.brockdepmin` for the map unit is used; if that
is also absent, the site is treated as **> 150 cm (no restriction)**, predicted class 5, and
flagged. Which of the three sources supplied each depth is reported.

`T` [mm/yr] = `tfact` × 2.2417 × 100 / ρ_b, ρ_b in kg/m³, ρ_b = 1300 where SSURGO has none —
identical to C43, so the two notes' `T` values are commensurable.

## 5. Statistics and gates, fixed in advance

Spearman ρ with the C43 script's tie-corrected ranks and Student-t p; seed 20260905 wherever a
draw is needed. Gates:

- **n < 30 joined sites with both `P` and `tfact`** ⇒ H2 and H3 are an **honest null on data
  availability**, reported as such, and H1 stands on the 1,500-point sample alone.
- **H1 passes** iff Group-2 agreement ≥ 90%. Between 70% and 90% ⇒ **partial**, and the band
  agreement decides whether the failure is the rule or the group.
- **H2 passes** iff ρ(`P`, depth class) < 0 **and** p < 0.01. A positive ρ at p < 0.01 falsifies
  the mechanism and C43 §3 must be withdrawn as an explanation.
- **H3 passes** iff every `tfact` class with n ≥ 25 has |ρ(`T`, `P`)| < 0.1. Any class with
  |ρ| ≥ 0.3 at p < 0.05 fails it.
- **The slope covariate.** Partial Spearman of `P` with `tfact` controlling SSURGO `slope_r`,
  by the rank-residual method. **If the partial |ρ| falls below 0.05, the anti-correlation is
  slope and the claim is restated as the weaker one**: `tfact` is a proxy for terrain, not an
  independent stock label. This is written down now precisely so that it cannot be reported as a
  robustness check afterwards.

## 6. What runs against the hypotheses, named in advance

Outcrop ¹⁰Be samples are taken **on** bedrock or thin regolith, so the sample is biased toward
shallow soils and low `tfact`; that compresses the depth range and works **against** H2's
detectability, not for it. SSURGO `resdept_r` is a map-unit representative value, not a measured
profile at the sample point, so H1's disagreements include map-unit generalisation and not only
rule violations. And the handbook's own exceptions in §2 put a ceiling below 100% on H1 that is
not a failure of the mechanism.

## 7. Scope

This tests the **USDA** assignment rule. [[C44-soil-ha-world]] already shows non-US proposed
tolerable-loss ranges are calibrated to the soil-formation literature and would not be expected
to show the depth mechanism. Nothing here is a claim about tolerable-loss standards in general.
