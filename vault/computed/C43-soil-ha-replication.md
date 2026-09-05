---
name: C43-soil-ha-replication
type: computed
exit: computation
extends-to: [sustainability, conservation]
next-step-cost: M
---

# The paired test of `T` against measured soil formation, and soil's `Ha` outside the US

> **PRE-REGISTERED TEST: H1 PASSES, H2 PASSES.** At **1,053 US sites** where a ¹⁰Be denudation
> rate and a USDA `tfact` were joined point-in-polygon, the median `T`/`P` is **22.3**
> (bootstrap 95% CI **[18.9, 25.9]**; 877 of 1,053 above 2, sign-test p = 2e-112) — inside the
> 10.1–50.7× band [[C35-soil-ha]] §5 predicted, so **C35's falsifier does not fire**. The
> secondary hypothesis passes in its strong form: **Spearman ρ(`T`, `P`) = −0.180**
> (p = 4.5e-9). `T` does not merely overstate formation; across sites it runs **the wrong way**.

Executes the dataset C35 §5 named. Re-runnable: `python _scripts/c43_soil_data.py` from `vault/`.
Pre-registered in `audits/blind-brief-c43-2026-09-05.md`, sha256
`dbae0496666126c4070f518f16d1bf997f6c6b9165469284f940440b5e7ef727`, hashed before any site-level
value was fetched.

---

## 1. What was actually obtained, and what was not

| Side | Source | Access, 2026-09-05 |
|---|---|---|
| `P` | **OCTOPUS v2.2**, layers `be10-denude:crn_int_basins` / `crn_int_outlets`, field `EBE_MMKYR` (CAIRN-harmonised ¹⁰Be denudation) | WFS `http://geoserver.octopusdata.org/geoserver/wfs`. `GetCapabilities` **200**; `GetFeature&outputFormat=csv` **200**. 1,182 outlet points in the US bbox, 1,156 with `CNTRY = USA` and a positive rate. CC BY 4.0 |
| `T`, ρ_b | **USDA-NRCS Soil Data Access**, `tfact` and `dbthirdbar_r` | POST to `https://sdmdataaccess.sc.egov.usda.gov/Tabular/post.rest`, T-SQL joining `SDA_Get_Mukey_from_intersection_with_WktWgs84('point(lon lat)')` → `component` → `chorizon`. **Worked, 1,143 of 1,156 points answered**; 90 returned a map unit with no `tfact` (water, rock outcrop, urban). No Web Soil Survey or STATSGO2 fallback was needed |
| — | Montgomery 2007 **SI** (the n = 188 compilation with coordinates) | **NOT OBTAINED.** `pnas.org` supplementary file **403**; the author-hosted `mssoy.org` PDF is the 5-page article only and its text carries no coordinates. Dixon & von Blanckenburg 2012 (`10.1016/j.crte.2012.10.012`, full PDF read from Centre Mersenne, **200**) has only a summary Table 1, no per-site rows. Stockmann et al. 2014 and Heimsath 1997 are **closed** (OpenAlex `oa_status: closed`, checked per-DOI) |

**So the `P` side is a substitute, and the brief pre-authorised exactly this one.** §2 clause 1
admitted "regolith/soil-mantled denudation used as production under local steady state". What is
joined here is **basin-averaged ¹⁰Be denudation**, not a soil-production function measured at the
soil–bedrock interface. The size of that substitution is measurable, and it is measured in §4.

Two citation corrections fell out. **Stockmann et al. 2014 "How fast does soil grow?" is
*Geoderma* 216:48–61** (Crossref `10.1016/j.geoderma.2013.10.007`, `container-title: Geoderma`),
not *Earth-Science Reviews*. **Bui et al. 2011 on Australian tolerable erosion is *Agric. Ecosyst.
Environ.* `10.1016/j.agee.2011.07.022`**, not *Geoderma*; it is closed and was not used.

## 2. The computation

```
P [mm/yr] = EBE_MMKYR / 1000
T [mm/yr] = tfact [short ton/ac/yr] x 2.2417 [t/ha per ton/ac] x 100 / rho_b [kg/m3]
ratio = T/P        Ha_T = P/T
```

ρ_b is `dbthirdbar_r` of the surface horizon of the dominant component by `comppct_r`; C35's
assumed 1300 kg/m³ was substituted for **14 of 1,053** sites that had none.

## 3. The result

Seven rows of the 1,053, at the extremes and the quartiles of the ratio. The full table is
`_scripts/c43_data/sites.json`; 47 distinct source studies contribute.

| OBSID | lon | lat | `tfact` | ρ_b | `T` mm/yr | `P` mm/yr | `T`/`P` | `Ha_T` | study |
|---|---:|---:|:-:|---:|---:|---:|---:|---:|---|
| S034WTS002 | −116.94 | 34.08 | 1 | 1600 | 0.140 | 2.800 | **0.05** | 19.99 | Binnie 2007 |
| S353WTS014 | −117.68 | 34.31 | 1 | 1500 | 0.149 | 2.550 | 0.06 | 17.06 | DiBiase 2023 |
| S216WTS010 | −124.12 | 47.68 | 3 | 750 | 0.897 | 0.2445 | 3.67 | 0.273 | Adams 2018 |
| **S186WTS051** | **−78.98** | **39.56** | **2** | **1300** | **0.345** | **0.0154** | **22.32** *(median)* | **0.045** | Portenga 2019 |
| S352WTS013 | −114.30 | 45.42 | 4 | 200 | 4.483 | 0.0753 | 59.53 | 0.017 | Mitchell 2023 |
| S026WTS050 | −77.34 | 41.21 | 5 | 100 | 11.209 | 0.0100 | 1120.9 | 0.0009 | Reuter 2005 |
| S046WTS050 | −78.78 | 38.22 | 5 | 100 | 11.209 | 0.0071 | **1576.4** | 0.0006 | Duxburry 2009 |

**Pre-registered statistics, n = 1,053** (well above the brief's n = 12 direction-only floor):

- median `T`/`P` = **22.322**, percentile bootstrap 95% CI **[18.882, 25.918]**, 10,000 resamples, seed 20260905
- sign test on log ratio > log 2: **877 of 1,053** above, exact two-sided **p = 2.12e-112**
- **Spearman ρ(`T`, `P`) = −0.180, p = 4.46e-9**
- median `Ha_T` = **0.045** — a `T`-permitted US field runs at one twenty-second of replacement
- only **13.0%** of sites fall in the falsifier window `T`/`P` ∈ [0.5, 2]

**Robustness.** Fixing ρ_b = 1300 everywhere (removing the organic-horizon densities as low as
100 kg/m³ that inflate `T` at 130 sites): median **16.47**, CI [13.89, 18.68], ρ = **−0.206**.
Mineral surface horizons only (ρ_b ≥ 1000, n = 918): median **18.21**, CI [14.72, 21.85],
ρ = **−0.303**. Every specification lands between 16 and 23 and every ρ is negative.

**The `tfact`-class table is the finding.** Under H2 the third column should be flat and the
fourth should rise with `tfact`. Both do the opposite.

| `tfact` (ton/ac/yr) | n | median `T`/`P` | median `P` (mm/yr) |
|:-:|---:|---:|---:|
| 1 | 99 | **0.93** | **0.1733** |
| 2 | 104 | 2.84 | 0.1049 |
| 3 | 216 | 24.50 | 0.0288 |
| 4 | 136 | **47.35** | 0.0255 |
| 5 | 498 | 29.93 | 0.0288 |

**Soils permitted to lose the most are the soils measured to make the least**, by a factor of six
in `P` between class 1 and class 4–5. Spearman ρ(`tfact`, `P`) = −0.206.

**The mechanism, and it is not a fluke.** `T` is assigned on **profile depth and fragility** — a
deep soil gets 5, a shallow or fragile one gets 1. Depth is an **inventory**. ¹⁰Be denudation is a
**rate**, and it is fastest exactly where soil is thin, because thin soil sits on the steep limb
of the humped soil-production function and on steep ground. So `T` and `P` are anti-correlated by
construction of the two conventions. **`T` is a stock-based permit written in the units of a flux,
and it has never been a formation-rate estimate at all.** That is stronger than C35's §5 claim,
which allowed `T` to be a formation estimate that was merely 10–51× too generous.

The one place the convention is nearly right is **`tfact` = 1**, median ratio **0.93** — inside
the falsifier window. The permit for shallow, fragile soils is calibrated. The permit for deep
soils, which is 498 of 1,053 sites, is not.

## 4. How much of this is the denudation-for-production substitution?

It is bounded, from a primary read. Dixon & von Blanckenburg 2012 Table 1 (PDF read in full,
Centre Mersenne, 2026-09-05) reports, in t km⁻² yr⁻¹ at the ρ = 2600 kg/m³ the compilers used:

| quantity | median | n | as mm/yr |
|---|---:|---:|---:|
| **soil production**, global compilation | 71 | 288 | **0.0273** |
| catchment-wide denudation from cosmogenic nuclides | 115 | 1209 | **0.0442** |

Denudation exceeds soil production by **1.62×** at the global median, and the OCTOPUS US median
(**0.0413** mm/yr, n = 1,164) reproduces Dixon's catchment median to 7%. **The substitution
inflates `P`, therefore deflates the ratio, therefore biases against H1 by about 1.6×.** Corrected
for it the median ratio would be ~36, not 22. The pass is conservative.

## 5. The erosion side outside the US, on C35's axis

`Ha = P/k_d`, `k_d` from area-specific erosion at ρ_b = 1300 kg/m³, `P` = regional median OCTOPUS
¹⁰Be rate computed here. Both erosion sources were **read in full on 2026-09-05**, which upgrades
C35 §6's "what could not be fetched": **Borrelli et al. 2017 is gold OA** (OpenAlex
`doi:10.1038/s41467-017-02142-7` → `nature.com/articles/s41467-017-02142-7.pdf`, 13 pp.), and its
printed text gives 2.8 Mg ha⁻¹ yr⁻¹ for 2001 and the continental rates below. Panagos et al. 2015
(`10.1016/j.envsci.2015.08.012`) was read from the KU Leuven Lirias repository copy: mean
**2.46**, median 1.27 t ha⁻¹ yr⁻¹.

| Region | `k_d` source | `k_d` mm/yr | `P` mm/yr (n) | **Ha** | **A** |
|---|---|---:|---:|---:|---:|
| Europe | Panagos 2015, erosion-prone land, 2.46 | 0.1892 | 0.0353 (141, slope-filtered) | **0.187** | 0.157 |
| Europe | Borrelli 2017, 0.92 | 0.0708 | 0.0353 (141) | **0.499** | 0.333 |
| Australia | Borrelli 2017 Oceania, 0.90 | 0.0692 | 0.0083 (214) | **0.120** | 0.107 |
| Asia / China | Borrelli 2017 Asia, 3.47 | 0.2669 | 0.0205 (26, slope-filtered) | **0.077** | 0.071 |
| North America | Borrelli 2017, 2.23 | 0.1715 | 0.0164 (337, slope-filtered) | **0.096** | 0.087 |
| *(C35 reference)* global mean | Borrelli 2.8 | 0.2154 | 0.017 (Montgomery) | 0.0789 | 0.073 |

`P` is the median over basins with `SLP_AVE` below the collection's low-gradient cut, because the
unfiltered regional medians are dominated by alpine catchments (Europe unfiltered: 0.238 mm/yr
from 835 basins, 240 of them Swiss — that would put Europe at `Ha` = 1.26 and is a statement about
the Alps, not about European farmland). **Every region lands in the 0.08–0.5 band, between C35's
no-till row (0.21) and its `T` = 1 ton/ac row (0.099).** No region reaches the native-vegetation
row at 1.31. The result replicates: soil is being spent everywhere it has been mapped, and the
spread across four continents is smaller than the spread between land uses within one.

One extra from the Borrelli read: its **"generic tolerable soil erosion threshold (`T`-value)
(10 Mg ha⁻¹ yr⁻¹)"** — 0.769 mm/yr at ρ_b = 1300, i.e. **45× Montgomery's formation median**. The
`Ha ≡ 1` construction C35 identified in USDA practice is being carried into global erosion
modelling at a value above the top of the USDA range.

## Scope 2026-09-05 — the claim is about the USDA convention, not tolerable-loss standards

[[C44-soil-ha-world]] supplies the control group this note lacked. Where a *non-US* national
tolerable-loss number exists, the anti-correlation and the overstatement do not appear:
Verheijen et al. 2009's proposed European range sits at median `T`/`P` = **0.22** at its lower
bound (0.30 t/ha/yr) and **1.01** at its upper (1.40 t/ha/yr) across 600 sites — calibrated to
measured formation, or conservative — while the same pipeline puts the USDA at **4.17** for
`tfact` = 1 and **20.88** for `tfact` = 5, bracketing this note's per-site median of 22.3. The
mechanism §3 names is why: Verheijen's range was derived *from* the soil-formation literature
and `tfact` was assigned from profile depth and fragility. **So C43's claim is restated as a
statement about the USDA `tfact` assignment rule, not about tolerable-loss standards in
general.** The one number that does generalise badly is Borrelli et al. 2017's "generic
`T`-value" of 10 Mg ha⁻¹ yr⁻¹, at median `T`/`P` = **10.1** over 5,611 sites — the USDA-shaped
convention, carried into global erosion modelling.

## 6. Honesty

**¹⁰Be integrates 10³–10⁴ yr; `tfact` is an annual management permit.** No statistic here repairs
that. A ratio of 22 is a ratio between a Holocene-averaged landscape flux and a number a committee
fixed in 1973. They are commensurable in units and in nothing else.

**"The same site" is a fiction at two different scales.** The ¹⁰Be datum is a **basin**-averaged
rate whose sample is one sediment collection at an outlet; the `tfact` is a polygon attribute of a
soil map unit at the outlet **point**. The join is therefore between a catchment-integrated flux
and a map-unit attribute at a single coordinate inside it. Both are real, neither is the other,
and this is the weakest joint in the note.

**Production rates are from ridge crests and outlets, not fields.** Nothing in either dataset is a
cropped field, which is where `T` is applied. §4 quantifies the direction (against H1, ~1.6×) and
not the magnitude of the land-use mismatch, which is larger and unquantified.

**Bulk density does real damage at the tails.** `dbthirdbar_r` of 100 kg/m³ is an O horizon, and
it turns `tfact` = 5 into `T` = 11.2 mm/yr and a ratio of 1576. Those rows are honest reads of
SSURGO and dishonest as mineral-soil erosion rates. The §3 robustness block exists because of
them; the finding does not depend on them.

**The falsifier, as pre-registered, did not fire, and the pre-registration is what makes that
worth anything.** The brief fixed the [0.5, 2] window, the n = 12 floor, the seed and the
exclusions before any site value was seen, and its §6 named the ridge-crest bias as running
against H1 in advance. What was *not* pre-specified is the `tfact`-class mechanism of §3, which
was found in the data and must be treated as a hypothesis for someone else to test, not a result.

**What this does and does not add.** It does not add a dimensionless group; `Ha` remains
REPACKAGED in this vault's novelty audit and C43 inherits that grade. What is new is (a) a
pre-registered per-site execution of a falsifier a vault note had only named, on 1,053 joins from
two live public APIs, and (b) the sign of ρ(`T`, `P`), which reclassifies `T` from a bad estimate
of a rate to not an estimate of a rate.

**Next.** The clean version of this test needs the Montgomery SI or an equivalent per-site
soil-production compilation with coordinates — a request to the authors, or a page-image OCR of
the PNAS supplement, neither of which was in scope here. Until then §3's `P` is denudation.
