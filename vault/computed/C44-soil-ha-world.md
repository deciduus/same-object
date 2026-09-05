---
name: C44-soil-ha-world
type: computed
exit: computation
extends-to: [sustainability, conservation]
next-step-cost: M
---

# The world soil-`Ha` ledger at site level, and what happens to the US `T` finding abroad

> **PRE-REGISTERED TEST: H1 PASSES. H2 NOT TESTED, as the brief predicted.** At **5,611
> ¹⁰Be sites in 55 countries**, median `Ha` = `P`/`E` is **0.410** (bootstrap 95% CI
> **[0.388, 0.439]**; **3,787 of 5,611 below 1**, sign-test p = 1.5e-154). Outside the United
> States: n = 4,447, median **0.463**, p = 7.8e-90. The ledger is negative on five of six
> continents. **H2 could not be posed**: no country outside the US publishes a per-site
> tolerable-loss layer, and none was back-filled. Its replacement is the finding — **the US
> `T` is ~20× measured formation and Europe's *proposed* `T` is ~1×**, so C43's result is
> **local to the USDA convention, not a fact about tolerable-loss values.**

Programme item **P-001**, Track A. Takes [[C43-soil-ha-replication]]'s join off US ground.
Re-runnable: `python _scripts/c44_world.py` from `vault/`. Pre-registered in
`audits/blind-brief-c44-2026-09-05.md`, sha256
`724ae9034bbc61761dad85b1c32ea32479708f4098e51a76b9e94634e806ab6b`, hashed before any site was
joined to any erosion value.

---

## 1. What was obtained, and the join level it forced

| Side | Source | Access, 2026-09-05 |
|---|---|---|
| `P` | **OCTOPUS v2.2**, WFS `http://geoserver.octopusdata.org/geoserver/wfs`, field `EBE_MMKYR` | `GetCapabilities` **200**; it advertises **four** ¹⁰Be basin/outlet pairs, not the two C43 used. All four fetched **globally, no bbox**: `crn_int_*` **200** (5,376 basins, 5,314 usable), `crn_aus_*` **200** (297), `crn_xxl_*` **200** (261) and `crn_inprep_*` **200** (157). Every one of the 418 `xxl`/`inprep` records carries `EBE_MMKYR = −9999.99` — no CAIRN-harmonised rate — so all 418 fall to the brief's positive-rate filter and contribute **nothing**. 5,611 sites survive, all with an outlet `POINT`. CC BY 4.0 |
| `E` | **Borrelli et al. 2017**, *Nat. Commun.* **8**:2013, `10.1038/s41467-017-02142-7` | Article HTML and **all four** Supplementary files fetched **200** and read. The **25 km GeoTIFF was not obtained**: the paper's Data Availability points only at "the article and its Supplementary Information", and the ESDAC landing page for GloSEM states **"Registration is requested: Yes"** — a registration form, which this project does not submit. Neither SI file carries a country table (MOESM1 = notes/figures/C-factors, MOESM2 = the peer-review file, MOESM3/4 = crop groups). Brief clauses 2(a) **and** 2(b) therefore **failed**, and clause **2(c), the printed continental means, is what is used** |
| `E`, Europe | **Panagos et al. 2015**, *Environ. Sci. Policy* **54**:438–447, `10.1016/j.envsci.2015.08.012`, **Table 1** | PDF read in full from the KU Leuven Lirias copy, **200**. A genuine **per-country** mean `E` for EU-28, in two variants (all land; arable land). 11 of those countries carry OCTOPUS sites, 600 of them |
| land cover | ESA CCI / MODIS point query | **NOT OBTAINED.** The one candidate WMS reachable without registration failed TLS verification, and no raster reader (`rasterio`, GDAL) is installed, so a COG could not be sampled. The brief's fallback applies: **Borrelli's own land-cover-stratified rates**, which makes §5 a statement about Borrelli's strata, not about these sites |

**So `E` is constant within continent for 5,011 sites and constant within country for 600.**
`Ha` varies through `P` alone except in those 600. The brief fixed this fallback in advance and
required it be said here; it is the largest single limitation of the note and §7 does not
soften it.

## 2. The computation

```
P [mm/yr] = EBE_MMKYR / 1000
E [mm/yr] = erosion [t/ha/yr] * 100 / rho_b,  rho_b = 1300 kg/m3 (fixed in the brief)
Ha        = P / E
```

Borrelli's printed continental means, baseline 2001, Mg ha⁻¹ yr⁻¹: South America 3.53, Africa
3.51, Asia 3.47, North America 2.23, Europe 0.92, Oceania 0.90; global 2.8.

## 3. The result

**Pre-registered statistics, n = 5,611:**

- median `Ha` = **0.4102**, percentile bootstrap 95% CI **[0.3877, 0.4385]**, 10,000 resamples,
  seed 20260905
- sign test vs 1: **3,787 of 5,611 below**, exact two-sided **p = 1.53e-154**
- non-US subset, n = 4,447: median **0.4631**, CI [0.4293, 0.4909], 2,889 below, p = 7.75e-90
- global median `P` = **0.0762 mm/yr** (the US median is 0.0413, C43)

**H1 passes, and it passes against the bias.** C43 §4 measured the substitution: basin-averaged
denudation exceeds soil production by ~1.62× at the global median (Dixon & von Blanckenburg
2012). `P` is inflated, so `Ha` is inflated, so the true median is nearer **0.25**.

### `Ha` by continent

| Continent | `E` t/ha | n | median `Ha` | 95% CI | below 1 |
|---|---:|---:|---:|:-:|---:|
| Africa | 3.51 | 348 | **0.027** | [0.024, 0.031] | 348/348 |
| Oceania | 0.90 | 343 | **0.177** | [0.157, 0.203] | 296/343 |
| South America | 3.53 | 831 | **0.162** | [0.139, 0.194] | 706/831 |
| North America | 2.23 | 1,364 | **0.284** | [0.239, 0.314] | 1,073/1,364 |
| Asia | 3.47 | 1,884 | **0.618** | [0.547, 0.683] | 1,126/1,884 |
| **Europe** | 0.92 | 841 | **3.290** | [2.689, 3.868] | 238/841 |

**Europe is the one continent above 1, and it is an artefact of where geomorphologists work.**
235 of the 841 European sites are Swiss; drop Switzerland and the European median falls to
**1.506** (n = 606) — still above 1, because Borrelli's European `E` (0.92 t/ha/yr) is the
lowest continental value in the table while OCTOPUS's European basins are Alpine, Apennine and
Pyrenean. This is C43 §5's slope problem, unfixed: C43 handled it by filtering on `SLP_AVE`,
this note does not, because no slope filter was pre-registered. **The European row is a
statement about the Alps.** The other five continents are not near the boundary in either
direction.

### `Ha` by country, n ≥ 10 (47 countries qualify; 15 shown, both tails and the middle)

| ISO | continent | n | median `P` mm/yr | `E` mm/yr | median `Ha` | 95% CI |
|---|---|---:|---:|---:|---:|:-:|
| NZL | Oceania | 46 | 2.336 | 0.069 | **33.74** | [20.58, 49.89] |
| CHE | Europe | 235 | 0.629 | 0.071 | 8.888 | [8.010, 10.131] |
| TWN | Asia | 102 | 1.536 | 0.267 | 5.756 | [4.543, 8.107] |
| NPL | Asia | 183 | 0.845 | 0.267 | 3.165 | [2.559, 3.668] |
| BTN | Asia | 140 | 0.259 | 0.267 | 0.968 | [0.673, 1.340] |
| GBR* | Europe | 33 | 0.163 | 0.183 | 0.891 | [0.722, 0.981] |
| PAN | N. America | 58 | 0.112 | 0.172 | 0.655 | [0.560, 0.736] |
| ITA* | Europe | 202 | 0.401 | 0.651 | 0.617 | [0.531, 0.727] |
| CHN | Asia | 699 | 0.137 | 0.267 | 0.514 | [0.472, 0.573] |
| DEU* | Europe | 89 | 0.044 | 0.096 | 0.461 | [0.426, 0.574] |
| IND | Asia | 295 | 0.080 | 0.267 | 0.299 | [0.221, 0.463] |
| **USA** | N. America | 1,164 | 0.041 | 0.172 | **0.241** | [0.206, 0.294] |
| AUS | Oceania | 297 | 0.010 | 0.069 | 0.149 | [0.137, 0.168] |
| BRA | S. America | 193 | 0.010 | 0.272 | 0.037 | [0.032, 0.041] |
| ZAF | Africa | 92 | 0.004 | 0.270 | 0.015 | [0.014, 0.017] |

`*` = `E` is the Panagos 2015 country mean; unmarked rows carry their continent's Borrelli
mean, so within a continent the ranking is a ranking of `P` and nothing else. The full 47-row
table is `_scripts/c44_data/out.txt`; the per-site rows are `c44_data/sites.json`.

**Every country whose median `Ha` exceeds 1 is a mountain belt** — New Zealand, Switzerland,
Taiwan, Nepal, Tajikistan (3.68), Azerbaijan (4.83). **Every country with a large agricultural
plain is deep below 1.** The ledger does not balance anywhere it has been sampled outside
tectonically active topography.

## 4. `P` against `E`: the pre-registered independence check

- **Continental `E`** (6 distinct values, n = 5,611): **ρ = −0.074**, p = 3.5e-8. Near zero, as
  the brief said independence would look, but this ρ is only a statement about which continents
  have fast basins.
- **Country-level `E`** (Panagos 2015, 11 countries, n = 600): **ρ = +0.706, p = 1.4e-91.**

**That positive ρ is the run's most interesting number and it is a warning, not a result.**
Where `E` actually varies at country level, modelled erosion and measured denudation track each
other hard. The honest reading is **shared inputs**: RUSLE's LS-factor is computed from a DEM,
and ¹⁰Be denudation is driven by the same relief. The brief named this failure mode in §6
before the number was seen. **It is also the exact opposite of C43's sign.** A *modelled*
erosion layer tracks formation **positively** (ρ = +0.71); the USDA's *policy* layer tracks it
**negatively** (ρ = −0.18). Both cannot be measuring the same thing about a landscape, and the
one that is anti-correlated with relief is the permit, not the model.

## 5. `Ha` by land cover — Borrelli's strata, not these sites

The sites are not land-cover classified (§1). What can be computed is the conditional ledger:
what `Ha` a site would run at under each of Borrelli's land-use rates.

| Borrelli 2017 stratum | `E` t/ha/yr | `E` mm/yr | global median `Ha` |
|---|---:|---:|---:|
| cropland | 12.70 | 0.977 | **0.078** |
| all land (global mean) | 2.80 | 0.215 | 0.354 |
| other natural vegetation | 1.84 | 0.142 | 0.538 |
| forest | 0.16 | 0.012 | **6.188** |

**A factor of 79 across land use, against a factor of 23 across continents.** Cropland `Ha` by
continent: Africa 0.008, Oceania 0.013, South America 0.045, North America 0.050, Asia 0.169,
Europe 0.238. C43 §5 reported the same shape — the spread between land uses inside one region
exceeds the spread between regions — on continental means; it survives at site level.

## 6. H2 replaced: `T`/`P` where a national number exists

H2 as posed is **NOT TESTED**. No non-US per-site tolerable-loss layer was found; the European
Soil Database has no `tfact` analogue, and Verheijen et al. 2009 is a proposed range, not a
mapped attribute. The brief pre-authorised this outcome and forbade back-filling.

| Standard | `T` t/ha/yr | n sites | median `T`/`P` | 95% CI | above 2 |
|---|---:|---:|---:|:-:|---:|
| **EU**, Verheijen 2009 lower | 0.30 | 600 | **0.22** | [0.16, 0.25] | 6/600 |
| **EU**, Verheijen 2009 upper | 1.40 | 600 | **1.01** | [0.76, 1.17] | 178/600 |
| **USA**, USDA `tfact` = 1 | 2.24 | 1,164 | 4.17 | [3.42, 4.87] | 724/1,164 |
| **USA**, USDA `tfact` = 5 | 11.21 | 1,164 | **20.88** | [17.11, 24.39] | 1,051/1,164 |
| **global**, Borrelli's generic `T` | 10.00 | 5,611 | **10.10** | [9.37, 10.73] | 4,439/5,611 |

The USA rows bracket C43's per-site median of **22.3**, which is the cross-check that this
different pipeline reproduces the earlier one.

**The multi-country finding is a difference in kind.** Europe's *proposed* tolerable loss sits
at `T`/`P` ≈ **1.0** at its upper bound and **0.22** at its lower — it is **calibrated to
measured formation, or conservative**. The USDA's is **4–21×** it. The number being carried
into global erosion modelling as a "generic `T`-value" is **10×**. So the C43 result does not
generalise as "tolerable-loss values overstate formation"; it generalises as **"the USDA's does,
by a factor its own European counterpart does not."** Verheijen's 0.3–1.4 was derived *from* the
soil-formation literature; `tfact` was assigned from profile depth. The two conventions differ
because one was built to be a formation rate and the other never was — which is exactly C43 §3's
mechanism, now with a control group.

Australia, China and India carry 297, 699 and 295 sites and **no published national `T` number
was verified for them in this run**. That is the single highest-value missing row and it is a
literature task, not a data task.

## 7. Honesty

**`E` is constant within continent for 89% of the sites.** Every per-country `Ha` outside those
11 European countries is `P_country / E_continent`. It is a real site-level `P` divided by a
regional constant, and it must never be quoted as a spatially resolved erosion ratio. The
25 km grid the brief wanted sits behind a registration form.

**Basin-averaged denudation is not soil production**, and the direction is known: ~1.62× too
high (C43 §4), so `Ha` is inflated and H1's pass is conservative. **RUSLE-modelled erosion is
not measured erosion**, and §4 shows it shares a driver with `P` — a 0.71 correlation that is
most plausibly the DEM appearing on both sides.

**ρ_b = 1300 kg/m³ enters `E` and not `P`.** A ±20% band is a ±20% band on every `Ha` in this
note. It does not move the sign of H1 and it does move Bhutan (0.97) and Britain (0.89) across
the boundary.

**¹⁰Be integrates 10³–10⁴ yr; Borrelli's `E` is a 2012 model year.** Four orders of magnitude
of averaging window separate numerator from denominator. They are commensurable in units and in
nothing else, and this is the same joint C42 and C43 flagged.

**OCTOPUS is a geomorphology collection, not a sample of farmland.** Its basins are chosen for
bedrock, relief and access. The Alpine European row and the mountain-belt tail of §3 are that
sampling showing through, not a discovery about Europe or New Zealand. The countries best
represented are the countries geomorphologists work in.

**What was not pre-specified.** The Switzerland-excluded European median, the cropland-by-
continent row of §5 and the reading of §4's positive ρ were all found after the data were seen.
They are hypotheses for someone else, not results. The pre-registered quantities are §3's
median, CI and sign test, §4's two ρ, and §6's `T`/`P` medians.

**What this adds.** `Ha` remains REPACKAGED in this vault's novelty audit and C44 inherits that
grade. What is new is (a) a pre-registered, site-level, 55-country execution of the ledger C35
and C43 had only computed from regional means, (b) the demonstration that C43's US `T` result
does **not** generalise — Europe's proposed `T` is calibrated where the USDA's is 20× out — and
(c) the ρ = +0.71 between a RUSLE product and ¹⁰Be denudation, which is a caution for every
study that treats the two as independent measurements of the same landscape.

**Next.** The registration-gated GloSEM 25 km raster is the one artefact that turns every row
here into a real site-level join; obtaining it is a request, not a fetch. Verified national
tolerable-loss numbers for Australia, China and India would triple §6.
