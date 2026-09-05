# C43/C44 adversarial review

Run 2026-09-05. Target: the one sentence

> "USDA tolerable soil loss values (`tfact`) are negatively correlated with measured soil
> formation across 1,053 US sites (Spearman rho = -0.18, p = 4.5e-9), because `tfact` is
> assigned on profile depth and depth anti-correlates with formation; the EU's proposed
> tolerable rates, by contrast, sit at 0.2-1.0x measured formation."

Read for this review: [[C43-soil-ha-replication]], [[C44-soil-ha-world]], [[C42-soil-ha-theory]],
[[C35-soil-ha]], `audits/g36-adversarial.md`, [[failure-modes]], [[novelty-audit]],
`vault/_scripts/c43_soil_data.py`.

**Instruments.** The C43 and C44 caches (`vault/_scripts/c43_data/sites.json`, 1,053 rows; the
932 cached SDA point responses; `octopus_basins.csv`; `c44_data/sites.json`, 5,611 rows) were
**re-analysed locally** — every number in Attacks 2, 3, 4 and 5 is a fresh computation on the
notes' own cached data using the notes' own `spearman`, `median` and `boot_ci`, seed 20260905.
Literature legs: **Crossref** (`api.crossref.org`, `mailto=deciduusleaf@gmail.com`), **Europe
PMC REST** (bare-quoted), **EUR-Lex**, **WebSearch/WebFetch**, all 2026-09-05, ~16 query
formulations. **OpenAlex returned `Rate limit exceeded / Insufficient budget ... Resets at
midnight UTC`** and **Semantic Scholar `graph/v1/paper/search` returned HTTP 429 / `total: null`
on every attempt** — the same rate limits `audits/g34-adversarial.md` and `g36-adversarial.md`
hit. The prior-art leg is Crossref + Europe PMC + web and does **not** meet the C5 section-11
bar. Stated, not hidden.

---

## Verdict

**KILL. Grade: REDISCOVERED on the mechanism, withdrawn on the number, false on the EU clause.**

Three clauses, three different deaths.

1. **"negatively correlated ... rho = -0.18, p = 4.5e-9" — KILL, spatial pseudoreplication plus a
   slope confound.** Aggregating C43's own 1,053 sites to **0.5-degree cells** (n = 189) gives
   **rho(`T`,`P`) = -0.041, p = 0.58**; at **1 degree** (n = 100), **+0.023, p = 0.82**. A
   **cluster bootstrap over the 48 source studies** gives **95% CI [-0.341, +0.053]** — zero
   inside. Controlling for basin gradient, the rank-partial **rho(`tfact`,`P` | slope) = -0.074**
   (from -0.206). And on low-gradient basins — the only ones resembling land a `tfact` governs —
   **the sign reverses**: `SLP_AVE` < 150, **rho(`tfact`,`P`) = +0.172, p = 0.0031**;
   `SLP_AVE` < 100, **+0.237, p = 0.0014**. The negative rho lives entirely in steep bedrock
   catchments (`SLP_AVE` >= 300: rho(`T`,`P`) = **-0.276**). The quoted p is off by roughly eight
   orders of magnitude.
2. **"because `tfact` is assigned on profile depth ..." — REDISCOVERED, and never tested in
   C43's own data.** That `T` is scaled by rooting depth rather than derived from a measured
   formation rate is the founding statement of the `T`-value critique literature:
   **Skidmore 1982** (ASA Spec. Publ. 45 ch. 8, in an edited volume literally titled
   *Determinants of Soil Loss Tolerance*), **Schertz 1983**, **Johnson 1987
   ("Soil loss tolerance: fact or myth?")**, **Alexander 1988** (titled *"Rates of soil
   formation: implications for soil-loss tolerance"*). USDA-facing documentation states the rule
   outright — 5 ton/ac/yr for rooting depth above 5 ft, reduced for shallower soils. Montgomery
   2007, C35's own load-bearing source, already reports that others hold `T` values are set above
   soil production rates for political and economic reasons. **Separately, C43 never fetched a
   depth field**: its SDA query returns `comppct_r`, `tfact` and `dbthirdbar_r` and nothing
   else. The causal clause is asserted in the note and measured nowhere in it.
   **Independently confirmed while this review was running:** [[C47-tfact-mechanism-test]],
   a pre-registered run on sites C43 did not use, reads the rule from the primary source —
   National Soil Survey Handbook Part 618 Subpart B §618.91, Figure 618B-3 — and finds `tfact`
   is depth **plus a renewability group**, not depth alone (the depth rule alone predicts 64.6%
   of values at 800 random CONUS points). On **114 independent outcrop sites** it finds
   **rho(`tfact`,`P`) = +0.090, p = 0.34, 95% CI [-0.095, 0.269]** — **C43's -0.206 lies outside
   that interval.** Two independent routes, the re-analysis below and C47's fresh sites, kill the
   same number.
3. **"the EU's proposed tolerable rates, by contrast, sit at 0.2-1.0x measured formation" —
   FALSE as a contrast, on three independent grounds.** (a) Verheijen et al. 2009's 0.3-1.4
   t/ha/yr **is defined as the soil formation rate** and its range **is** the reviewed European
   formation compilation, so dividing it by measured formation is a **positive control, not a
   contrast** — it recovers its own construction. (b) It is a review's recommendation, not the
   EU's proposal and not any jurisdiction's standard. (c) The EU's **actual** proposed number,
   COM(2023)416 Annex I, was **<= 2 t/ha/yr** — and the **adopted Directive (EU) 2025/2360
   deleted it**, moving erosion to Annex I Part B with the criterion "Member States shall lay
   down their own maximum value" under a column headed **"non-binding sustainable target
   values"**. Run through C44's own pipeline the independent European numbers land **inside the
   USDA range, not opposite it**: against the 89 German OCTOPUS sites (median `P` = 0.0443
   mm/yr), the EU's proposed 2 t/ha/yr gives **`T`/`P` = 3.5** and Germany's own operative
   harmful-change trigger of 13 t/ha/yr gives **22.6** — indistinguishable from C43's US
   headline of 22.3. **And the one operative European standard is itself depth-scaled**:
   Switzerland's VBBo (SR 814.12) Annex 3 sets 2 t/ha/yr for rootable depth up to 70 cm and 4
   above it. The rule the sentence blames on the USDA is in force in Europe.

**What survives is C43's H1, which is not this sentence.** The magnitude claim survives every
decluster: 0.5-degree cell median `T`/`P` = **23.98**, CI [12.11, 34.44], **90% of 189 cells
above 2**; study-median `T`/`P` = **7.89**, 83% of 48 studies above 2. That claim is also already
published — Montgomery 2007, Verheijen 2009, Evans et al. 2020 (per `g36-adversarial.md`),
Stockmann et al. 2014, and **Quarrier et al. 2023**, the nearest miss (below).

**Not a hit:** the map-unit-component attack. Weighting `tfact` by `comppct_r` over all
components at the point instead of taking the dominant one moves rho from -0.206 to **-0.181**.
Real sloppiness, no leverage.

---

## Attacks

### 1. Prior art — **HIT on the mechanism; the site-level statistic is unpublished but Quarrier 2023 is one step away.**

Crossref record verification, `mailto=deciduusleaf@gmail.com`, fetched 2026-09-05:

| Work | DOI | Venue | Crossref `is-referenced-by-count` |
|---|---|---|---:|
| Skidmore 1982, *Soil Loss Tolerance* (in *Determinants of Soil Loss Tolerance*, ASA Spec. Publ. 45) | `10.2134/asaspecpub45.c8` | ASA Special Publications | — |
| Schertz 1983, *The basis for soil loss tolerances* | `10.1080/00224561.1983.12436238` | J. Soil Water Conserv. **38**(1):10-14 | **45** |
| Johnson 1987, *Soil loss tolerance: Fact or myth?* | `10.1080/00224561.1987.12456064` | J. Soil Water Conserv. **42**(3):155-160 | **25** |
| Alexander 1988, *Rates of soil formation: implications for soil-loss tolerance* | `10.1097/00010694-198801000-00005` | Soil Science **145**(1):37-45 | **61** |
| Verheijen et al. 2009 | `10.1016/j.earscirev.2009.02.003` | Earth-Sci. Rev. **94**:23-38 | **595** |
| Stockmann et al. 2014, *How fast does soil grow?* | `10.1016/j.geoderma.2013.10.007` | Geoderma **216**:48-61 | **112** |

Both papers the brief guessed at exist and say what it guessed. A 1982 ASA volume is titled
*Determinants of Soil Loss Tolerance*, with companion chapters `...c6` (rangelands) and `...c11`
(*Improved Criteria for Developing Soil Loss Tolerance Levels for Cropland*). **The claim
"`T` is depth-based, not formation-based" is not this project's; it is the 44-year-old founding
complaint of a critique literature.**

**Prior comparisons of a tolerable-loss value against cosmogenic rates already exist, four times
over**, all at distribution-vs-benchmark level rather than site-matched:

- **Montgomery 2007** (`10.1073/pnas.0611508104`) — 10Be soil-production compilation, median
  0.017 mm/yr, against USDA `T` as ~0.4-1 mm/yr.
- **Stockmann et al. 2014** — TCN soil-production distribution with soil-loss-tolerance lines at
  5 and 12 t/ha/yr drawn on it.
- **Quarrier et al. 2023**, *Pre-agricultural soil erosion rates in the midwestern United
  States*, Geology **51**(1):44-48, `10.1130/G50667.1` (supplement `10.1130/geol.s.21200461`) —
  **the nearest miss.** In-situ 10Be at 14 remnant native prairies in IA/MN/SD/NE/KS, median
  pre-agricultural erosion 0.04 mm/yr, framed explicitly against the ~1 mm/yr USDA soil loss
  tolerance at those locations (one to four orders of magnitude lower) and arguing that
  cosmogenic nuclides should be used to redefine tolerable erosion. Its `T` side is a
  near-constant benchmark, so it is a per-site ratio and not a correlation between a *varying*
  `tfact` and a varying 10Be rate — but it is the same idea, in the same country, at site level.
- **Kwang, Thaler & Larsen 2023**, Earth's Future, `10.1029/2022EF003104` — couples **gSSURGO**
  to a formation rate and finds erosion at USDA-guideline rates is ~25x topsoil formation.

Europe PMC, bare-quoted, `format=json`, 2026-09-05:

| Query (verbatim) | Hits |
|---|---:|
| `"soil loss tolerance" AND "cosmogenic"` | **1** — Montgomery 2007 |
| `"tolerable soil loss" AND "10Be"` | **1** — the same paper |
| `"soil loss tolerance" AND "soil production rate"` | **0** |
| `"tolerable soil loss" AND "denudation"` | **0** |
| `"soil loss tolerance" AND "soil depth"` | 7 |
| `"soil loss tolerance" AND "rooting depth"` | 2 (neither on topic) |
| `"T value" AND "soil loss tolerance"` | 4 |

So the *statistical* comparison of a **spatially varying** mapped `T` layer against cosmogenic
rates does appear unpublished. That is the only novelty the sentence has left, and Attacks 2-3
show the statistic it produced is not real. **A gap occupied only by a dead number is not a
finding.** Quarrier et al. 2023 must be read in full — GeoScienceWorld returned **403** here, and
its supplement may already tabulate per-site `T` — before any residual novelty claim is made.

**Grade: REDISCOVERED.**

### 2. Is the correlation an artifact of the join? — **HIT twice, MISS once.**

**MISS — the dominant-component choice.** Over the 932 cached SDA responses carrying a `tfact`,
**695 (74.6%)** have more than one component, and in **518 of those 695 (74.5%)** the components
**disagree on `tfact`**. The dominant component's median `comppct_r` is **55**, and **51%** of
points have a dominant component below 60% — the assigned `tfact` is close to a coin flip within
its own map unit. But recomputing with a `comppct_r`-weighted mean `tfact` gives **rho = -0.181**
against the dominant-component **-0.206**. This attack fails; it is reported as failed.

**HIT — one point stands in for a whole basin.** Basin `AREA` for the 1,053 joined sites
(OCTOPUS `crn_int_basins`): median **8.45 km2**; deciles 0.75 / 1.77 / 3.16 / 5.02 / 8.45 /
13.97 / 26.29 / 64.01 / 244.37 km2; **87.0%** exceed 1 km2, **46.5%** exceed 10 km2, **16.9%**
exceed 100 km2. SSURGO delineations are typically 1-40 ha. **Every basin but a handful spans
tens to thousands of map units, and `tfact` is read at a single coordinate — the outlet, the
lowest and most depositional point in the catchment, systematically unrepresentative of the
hillslopes the 10Be integrates.** C43 section 6 calls this "the weakest joint in the note" and is
right. (The correlation is *stronger* in small basins — `AREA` < 1 km2, n = 137,
rho(`tfact`,`P`) = -0.395 — than large — `AREA` > 10 km2, n = 490, -0.128. That is not evidence
for the join: small OCTOPUS basins are the steep headwater ones. See Attack 3.)

**HIT — `P` is not soil formation, and the sentence says it is.** C43's `P` is `EBE_MMKYR`,
**basin-averaged 10Be denudation**, integrating hillslope soil production *plus* channel
incision, landsliding and bedrock lowering; Heimsath's production function is measured at
ridge-crest soil-bedrock interfaces. C43 section 4 bounds the *median* offset at 1.62x (Dixon &
von Blanckenburg 2012) and treats it as conservative for H1 — correct for a **median ratio**,
**invalid for a correlation**, because the offset is not a constant: it grows with relief. That
relief term is exactly what Attack 3 finds. **"Measured soil formation" is not what was
measured, and the difference is the entire result.**

### 3. Slope confound — **HIT. This is the kill.**

On C43's own `SLP_AVE` field, n = 1,053 (every site carries one):

```
rho(slope, P)     = +0.610  p = 2.1e-108
rho(slope, tfact) = -0.245  p = 7.7e-16
rho(slope, T)     = -0.143  p = 3.4e-06
rho(T, P)         = -0.180  p = 4.5e-09   (C43's headline, reproduced exactly)
rho(tfact, P)     = -0.206  p = 1.5e-11
```

Slope predicts `P` **three times more strongly than `tfact` does**, and is itself correlated with
`tfact`. Rank-partial correlations controlling for `SLP_AVE`:

```
partial rho(tfact, P | slope) = -0.074   (was -0.206)   z = -2.39
partial rho(T,     P | slope) = -0.118   (was -0.180)
```

**About two thirds of the association is topography.** Stratifying is worse for the sentence than
partialling:

| stratum | n | rho(`T`,`P`) | rho(`tfact`,`P`) |
|---|---:|---:|---:|
| `SLP_AVE` < 100 | 179 | +0.056 (p = 0.46) | **+0.237** (p = 0.0014) |
| `SLP_AVE` < 150 | 294 | -0.013 (p = 0.83) | **+0.172** (p = 0.0031) |
| 150 <= `SLP_AVE` < 300 | 416 | +0.025 (p = 0.62) | -0.163 (p = 0.00086) |
| `SLP_AVE` >= 300 | 343 | **-0.276** (p = 2.0e-07) | -0.184 (p = 0.00062) |

**The negative correlation exists only in the steepest third and reverses in the flattest third**
— and the flattest third is the only stratum resembling land where a USDA `T` is applied to a
farm. The honest causal story is not "a depth-based `T` anti-correlates with formation"; it is
**"steep basins denude fast and carry thin, low-`tfact` soils"** — trivially true, and a
statement about topography rather than about the assignment rule.

Spatial declustering then removes the correlation outright:

| aggregation | n units | rho(`T`,`P`) | p |
|---|---:|---:|---:|
| raw sites | 1,053 | -0.180 | 4.5e-09 |
| 0.5-degree cell medians | 189 | **-0.041** | 0.58 |
| 1-degree cell medians | 100 | **+0.023** | 0.82 |
| source-study medians | 48 | -0.291 | 0.045 |
| source-study medians, `tfact` vs `P` | 48 | -0.202 | **0.17** |
| cluster bootstrap over studies, 2,000 draws | — | median -0.172 | **95% CI [-0.341, +0.053]** |

The 1,053 sites are not 1,053 independent draws. The five largest contributing studies supply
**29%** of them, and sites within a study share region, lithology, relief and often the same
SSURGO map units. **The p-value is the pseudoreplication, not the effect.**

**The same confound eats C43 section 3's showpiece.** Section 3 reports "`tfact` = 1 is
calibrated, median `T`/`P` = 0.93" and C35's blockquote repeats it. Of the 99 `tfact` = 1 sites,
only **7** are low-gradient, and on those 7 the median `T`/`P` is **12.40**, not 0.93. The
calibrated-looking class is a bundle of steep Californian and Sierran bedrock catchments.
Low-gradient class medians run **12.4 / 12.9 / 57.6 / 71.9 / 40.9** for `tfact` = 1...5 — **the
permit is out by an order of magnitude in every class, including the one called calibrated.**

**Bonus hit on section 3's table.** It says "under H2 the third column should be flat and the
fourth should rise with `tfact`. Both do the opposite." The third column (median `T`/`P` by
class) **cannot** be flat: `T` is proportional to `tfact` by construction. Shuffling `P` at
random across sites — destroying any real relation — still yields **rho(`tfact`, `T`/`P`) =
+0.255, 95% [0.204, 0.298]** against an observed **+0.376**. Most of that column is arithmetic.
Only the fourth column carries information, and that is the slope confound again.

### 4. The EU comparison — **HIT, three ways. The strongest single hit in this review.**

**(a) Circular.** Verheijen et al. 2009 (`10.1016/j.earscirev.2009.02.003`, Crossref-verified,
595 citing works) sets the upper limit of tolerable erosion **equal to soil formation** and reads
the value off a review of European soil formation rates. Dividing it by a soil formation rate
measures how well two formation compilations agree. That is a **positive control on the
pipeline** — genuinely worth reporting, and C44 section 6 does report it that way ("calibrated to
measured formation"). As a *contrast* it is question-begging.

**(b) It is not the EU's, and the EU's own number went the other way.** Verheijen is a review's
recommendation; no jurisdiction adopted 0.3-1.4. The EU's actual proposal, **COM(2023)416
Annex I**, carried the descriptor "Soil erosion rate (tonnes per hectare per year)" with the
criterion **"<= 2 t ha-1 y-1"**. The **adopted Directive (EU) 2025/2360** (OJ L, 26.11.2025,
ELI `data.europa.eu/eli/dir/2025/2360/oj`, in force 16 Dec 2025) **removed it**: erosion sits in
Annex I **Part B**, criteria "established at Member State level", under a column headed
**"non-binding sustainable target values"**, the entry reading "Member States shall lay down
their own maximum value". Annex III prescribes methodology and no number. **As of 2026 the EU has
no operative numeric tolerable soil loss value at all.** Panagos et al. 2015 uses ~1 t/ha/yr,
citing formation rates (the Verheijen lineage); the JRC/EUSO **2 t/ha/yr** is a reporting
indicator, not a limit.

**(c) Where a European number is independent of the formation literature, it lands in the USDA
range — and the operative one is depth-scaled.** Run through C44's own pipeline
(`c44_data/sites.json`, rho_b = 1300 kg/m3) against the 89 German OCTOPUS sites, median
`P` = 0.0443 mm/yr — the least Alpine-contaminated European sample available:

| Standard | status | t/ha/yr | `T` mm/yr | median `T`/`P`, DEU sites |
|---|---|---:|---:|---:|
| Verheijen 2009 lower | review proposal, defined from formation | 0.30 | 0.0231 | 0.52 |
| Verheijen 2009 upper | review proposal, defined from formation | 1.40 | 0.1077 | 2.43 |
| COM(2023)416 Annex I | **proposed, then deleted** | 2.00 | 0.1538 | **3.47** |
| Switzerland VBBo Annex 3, rootable depth <= 70 cm | **in force** | 2.00 | 0.1538 | 3.47 |
| Switzerland VBBo Annex 3, rootable depth > 70 cm | **in force** | 4.00 | 0.3077 | **6.94** |
| Lower Saxony harmful-change trigger (DIN 19708 basis) | **in force** | 13.00 | 1.0000 | **22.56** |
| *(USDA `tfact` = 1 / = 5, C44 section 6, US sites)* | in force | 2.24 / 11.21 | 0.172 / 0.862 | 4.17 / 20.88 |

**Germany's operative trigger lands at 22.6 — C43's US headline is 22.3.** And **Switzerland's
VBBo (SR 814.12) Annex 3, the one genuinely operative European tolerable-erosion table, assigns
its value by rootable soil depth** — 2 t/ha/yr up to 70 cm, 4 above — which is precisely the
assignment rule the sentence presents as the USDA's distinguishing defect. **The "by contrast"
clause is not merely circular; its factual content is backwards.**

The defensible residue: *Verheijen's proposal is calibrated to formation because it was defined
from formation; every tolerable-loss number that was **not** so defined — USDA, EU-proposed,
Swiss, German — sits at 3-23x measured rates.* That is C44's own section 6 finding, correctly
scoped, and it is not a US-versus-Europe contrast.

### 5. Effect size — **HIT. Overstated even before the confound.**

rho = -0.18 is **3.2% of rank variance**. Within-class `P` distributions overlap almost totally:
`tfact` = 3 spans p10-p90 = 0.0075-0.2123 mm/yr (28-fold), `tfact` = 5 spans 0.0073-0.3752
(51-fold), against a 6-fold spread in class medians. **`tfact` carries essentially no information
about `P` at a site** — a stronger and more defensible statement than "runs the wrong way", and
the one the data support. C43 section 3 leans its whole reclassification of `T` "from a bad
estimate of a rate to **not** an estimate of a rate" on a sign that does not survive
declustering. The null — a mapped policy layer with **no** measurable relation to measured
landscape denudation — is the real result and needs no sign at all.

### 6. Actionability — **not as written; yes after the rewrite.**

The sentence offers a sign, an implausible p, and a mechanism from 1982. Nothing follows. What
the same data do support:

- **A magnitude map, not a correlation.** **61.7%** of the 1,053 sites have `T`/`P` > 10 and
  **83.3%** have `T`/`P` > 2; on low-gradient basins (n = 294), **82%** exceed 10x, median 50.8.
  "Where does the permit exceed the measured rate by more than 10x" is a map an agency can act
  on; "rho = -0.18" is not. Quarrier et al. 2023 makes exactly this argument for the Midwest and
  is the venue-appropriate precedent.
- **A stated null.** `tfact` class predicts ~3% of the rank variance in 10Be denudation, and the
  residual sign is topographic. If `tfact` were meant to track formation, this is the test it
  fails; failing it flat is cleaner than failing it backwards.
- **A reassignment rule** needs per-site soil depth and a production-function `P` at a stated
  depth. C43 fetched neither. See "What would settle it".

---

## The sentence that survives, verbatim

> **Across 1,053 US sites where a USDA `tfact` was joined to an OCTOPUS 10Be basin-averaged
> denudation rate, `tfact` carries essentially no information about the measured rate: it
> explains ~3% of rank variance, and the small negative Spearman correlation (rho = -0.18) does
> not survive spatial declustering (0.5-degree cell medians: rho = -0.041, p = 0.58; cluster
> bootstrap over the 48 source studies: 95% CI [-0.341, +0.053]) or a control for basin gradient
> (partial rho = -0.07), and reverses sign on low-gradient basins (rho(`tfact`,`P`) = +0.24,
> p = 0.001). What survives every specification is the magnitude: median `T`/`P` = 24.0
> [12.1, 34.4] over 189 0.5-degree cells, 90% of cells above 2 — already published in dimensioned
> form by Montgomery 2007, Stockmann et al. 2014, Evans et al. 2020, Kwang et al. 2023 and, at
> site level for 14 midwestern prairies, Quarrier et al. 2023. That `T` is scaled by rooting
> depth rather than derived from a measured formation rate is not new either: it is Skidmore
> 1982, Schertz 1983, Johnson 1987 and Alexander 1988. Nor is depth-based assignment a USDA
> peculiarity — Switzerland's VBBo Annex 3, the one operative European tolerable-erosion table,
> assigns 2 or 4 t/ha/yr by rootable depth.**

Everything in the original sentence after "1,053 US sites" is withdrawn or reattributed.

## Proposed edits

For [[C43-soil-ha-replication]], [[C44-soil-ha-world]] and [[C35-soil-ha]]. **No vault note was
edited by this review**; the log entry is staged in `vault/PENDING-log-C43ADV.md`.

1. **C43 blockquote and section 3 — withdraw the Spearman result as a finding.** Replace
   "**Spearman rho(`T`, `P`) = -0.180** (p = 4.5e-9). `T` does not merely overstate formation;
   across sites it runs **the wrong way**" with the declustered numbers and the null reading.
   Record the pre-registered **H2 as not passing in its strong form**: the sign is not robust, so
   the honest pre-registered outcome is "no relation detected", not a pass. That is the point of
   pre-registration, and it should be honoured against the project's own preferred result.
2. **C43 section 3 — delete or demote "The `tfact`-class table is the finding."** Column 3 is
   arithmetically forced (rho = +0.26 under a full `P`-shuffle); column 4's gradient is the slope
   confound. Keep the table as description, not evidence.
3. **C43 section 3 and C35 blockquote — withdraw "`tfact` = 1 is calibrated (median ratio
   0.93)".** On the 7 low-gradient `tfact` = 1 sites the median is 12.40. Both notes quote the
   0.93; both need the correction in the same pass.
4. **C43 — add a gradient section.** rho(slope,`P`) = +0.610 is the largest correlation in the
   dataset and the note never reports it. Every statement about `tfact` and `P` must be
   conditioned on it, and the four-stratum table above should appear verbatim.
5. **C43 — stop calling `P` "measured soil formation".** It is basin-averaged denudation. The
   1.62x median correction of section 4 licenses the substitution for a median, not for a
   correlation.
6. **C35 blockquote (approx. lines 174-182) — withdraw "the residue that is the project's own".**
   It asserts the site-level anti-correlation "is nowhere in the prior art above, and it is the
   one candidate here for a genuinely new empirical claim". The mechanism is Skidmore 1982 /
   Schertz 1983 / Johnson 1987 / Alexander 1988, the site-level ratio framing is Quarrier et al.
   2023, and the number does not survive. Replace with the null.
7. **C44 section 6 — relabel the EU rows.** Head the Verheijen rows **positive control** rather
   than comparison, and add the four independent European numbers (EU-proposed 2, Swiss 2 and 4,
   German 13) with their `T`/`P` against German sites, plus the facts that Directive (EU)
   2025/2360 deleted the EU threshold and that the Swiss standard is depth-scaled. This turns
   C44 section 6 from a US-vs-Europe contrast into the correct claim: **numbers defined from
   formation match formation; numbers not so defined sit at 3-23x, on both continents.**
8. **[[novelty-audit]] — hold the C35/C42/C43 row at REPACKAGED** and add to its "biggest threat"
   cell that C43's rho(`T`,`P`), the one claim flagged as a possible NOVEL residue, was
   **withdrawn 2026-09-05** for spatial pseudoreplication and a gradient confound, and that
   Quarrier et al. 2023 is prior art for the site-level `T`-vs-10Be framing.

## What would settle it

1. **Fetch soil depth.** One column added to the existing SDA query — `component.brockdepmin`, or
   `chorizon.hzdepb_r` of the deepest horizon — tests the sentence's own causal clause at the
   same 1,053 points: is rho(depth, `tfact`) positive and rho(depth, `P`) negative? C43 asserts
   both and measured neither. Cost: one script edit plus a cache re-run. **Substantially done
   already** by [[C47-tfact-mechanism-test]], which fetched restriction depth and found the rule
   is depth *plus a renewability group*; what remains is running that depth field against `P` at
   C43's own 1,053 points rather than C47's independent ones.
2. **Read Quarrier et al. 2023 in full**, including supplement `10.1130/geol.s.21200461`
   (GeoScienceWorld returned **403** here; the UMass thesis mirror also 403). If its supplement
   tabulates per-site `T` alongside per-site 10Be, the remaining novelty claim is gone entirely
   and the grade moves from REDISCOVERED to fully scooped.
3. **Replace denudation with production.** The Montgomery 2007 SI (PNAS 403), Stockmann et al.
   2014's compilation, or any per-site 10Be **soil-production** dataset with coordinates, through
   the same join. Until then no sentence in C43 may say "measured soil formation". This is C43's
   own "Next" item and it is the load-bearing one.
4. **Restrict to cropland.** NLCD is free and needs no registration; masking to cultivated
   classes puts the test on the land `tfact` governs — which is exactly where the sign flips.
   C44 section 1 records that no raster reader is installed; installing one is the smallest of
   these tasks.
5. **Pre-register the declustering unit.** Any re-run must fix the spatial unit (0.5-degree cell,
   or source study) **before** computing the statistic, because that choice moves rho from -0.18
   to +0.02.
6. **Read Skidmore 1982, Schertz 1983 and Johnson 1987 in full.** All Crossref-verified, none
   read here; the Skidmore chapter is on a public USDA-ARS server. A full-text read fixes whether
   the depth rule is stated in the words the sentence uses.
7. **Re-run the prior-art leg unthrottled.** OpenAlex (budget exhausted) and Semantic Scholar
   (HTTP 429) both refused today; the C5 section-11 bar is not met.
