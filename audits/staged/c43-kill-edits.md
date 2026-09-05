---
name: PENDING-log-C43ADV
type: method
---

# Staged `log.md` entries from the C43/C44 adversarial pass

Not yet merged. These four blocks go at the **top** of `vault/log.md` (newest first) when the
[[C43-soil-ha-replication]] / [[C44-soil-ha-world]] / [[C35-soil-ha]] edits proposed in
`audits/c43-adversarial.md` are applied. This file is deleted in the same commit that merges
them. Nothing in the vault was edited by the review itself.

---

## [2026-09-05] correction | C43's Spearman rho(T,P) = -0.180, p = 4.5e-9 withdrawn: spatial pseudoreplication and a slope confound

**Was.** C43 reported "Spearman rho(`T`, `P`) = -0.180 (p = 4.46e-9)" as a pre-registered H2 pass
in its strong form, concluding "`T` does not merely overstate formation; across sites it runs
**the wrong way**", and C35's blockquote called this "the one candidate here for a genuinely new
empirical claim".

**Is.** The correlation does not survive declustering or a gradient control, and it reverses on
low-gradient land. Re-analysis of C43's own cache (`_scripts/c43_data/sites.json`, 1,053 rows,
C43's own `spearman`/`median`/`boot_ci`, seed 20260905, 2026-09-05):

- 0.5-degree cell medians, n = 189: **rho = -0.041, p = 0.58**; 1-degree, n = 100: **+0.023,
  p = 0.82**
- cluster bootstrap over the 48 source studies, 2,000 draws: **95% CI [-0.341, +0.053]**;
  study-median rho(`tfact`,`P`) = -0.202, **p = 0.17**
- rank-partial controlling `SLP_AVE`: **rho(`tfact`,`P` | slope) = -0.074** (from -0.206)
- **sign reversal** on low-gradient basins: `SLP_AVE` < 150, **rho(`tfact`,`P`) = +0.172,
  p = 0.0031**; `SLP_AVE` < 100, **+0.237, p = 0.0014**. The negative rho lives only in
  `SLP_AVE` >= 300 (rho(`T`,`P`) = -0.276)
- the largest correlation in the dataset is one C43 never reported: **rho(slope, `P`) = +0.610,
  p = 2.1e-108**

**What produced the new number.** No new data. The C43 cache re-analysed with three additions
C43 did not run: spatial aggregation, a cluster bootstrap over source studies, and stratification
on the `SLP_AVE` field C43 already carried in `sites.json`. The mechanism is now read as
topographic — steep basins denude fast and carry thin, low-`tfact` soils — not as an artefact of
the assignment rule. H2's honest pre-registered outcome is **"no relation detected"**, not a pass.

Two dependent numbers fall with it. C43 section 3's "`tfact` = 1 is calibrated, median `T`/`P` =
0.93" is a steep-catchment artefact: only 7 of the 99 `tfact` = 1 sites are low-gradient and on
those the median is **12.40**. And section 3's `tfact`-class ratio column is largely forced —
shuffling `P` at random still yields rho(`tfact`, `T`/`P`) = **+0.255** [0.204, 0.298] against an
observed +0.376, because `T` is proportional to `tfact` by construction.

**Independently confirmed.** [[C47-tfact-mechanism-test]], pre-registered and run the same day on
114 ¹⁰Be outcrop sites C43 did not use, finds **rho(`tfact`, `P`) = +0.090, p = 0.34, 95% CI
[-0.095, 0.269]** — C43's -0.206 lies **outside** that interval — and its partial rho controlling
`slope_r` is +0.075. Two independent routes, this re-analysis and C47's fresh sites, kill the
same number.

**What does not fall.** C43's H1. Median `T`/`P` over 189 0.5-degree cells is **23.98**
[12.11, 34.44] with **90% of cells above 2**; study-median 7.89, 83% of 48 studies above 2. The
magnitude survives every specification tried.

---

## [2026-09-05] correction | "T is assigned on profile depth, not formation" is 44-year-old prior art, not this project's

**Was.** C43 section 3 and C35's blockquote presented the depth-based assignment of `T` as the
project's own mechanism, discovered in the data.

**Is.** It is the founding complaint of the `T`-value critique literature. Crossref-verified
2026-09-05 (`api.crossref.org`, `mailto=deciduusleaf@gmail.com`):

- Skidmore 1982, *Soil Loss Tolerance*, `10.2134/asaspecpub45.c8` — chapter 8 of an edited ASA
  volume titled *Determinants of Soil Loss Tolerance* (companions `...c6`, `...c11`)
- Schertz 1983, *The basis for soil loss tolerances*, `10.1080/00224561.1983.12436238`,
  J. Soil Water Conserv. 38(1):10-14, `is-referenced-by-count` = **45**
- Johnson 1987, *Soil loss tolerance: Fact or myth?*, `10.1080/00224561.1987.12456064`,
  J. Soil Water Conserv. 42(3):155-160, count = **25**
- Alexander 1988, *Rates of soil formation: implications for soil-loss tolerance*,
  `10.1097/00010694-198801000-00005`, Soil Science 145(1):37-45, count = **61**

USDA-facing documentation states the rule plainly: 5 ton/ac/yr for rooting depth above 5 ft,
reduced for shallower soils. Montgomery 2007, C35's own source, already reports that others hold
`T` values are set above soil production rates for political and economic reasons.

Two comparisons of a tolerable-loss value against cosmogenic rates also predate this vault:
**Stockmann et al. 2014** (`10.1016/j.geoderma.2013.10.007`, Geoderma 216:48-61 — note the
container correction C43 already logged) draws 5 and 12 t/ha/yr tolerance lines on a TCN
soil-production distribution, and **Quarrier et al. 2023** (`10.1130/G50667.1`, Geology
51(1):44-48) measures in-situ 10Be at 14 midwestern prairie sites and frames it explicitly
against the ~1 mm/yr USDA soil loss tolerance, arguing cosmogenic nuclides should redefine
tolerable erosion. **Kwang et al. 2023** (`10.1029/2022EF003104`) couples gSSURGO to a formation
rate for a ~25x national ratio.

**What is left.** Europe PMC bare-quoted, 2026-09-05: `"soil loss tolerance" AND "cosmogenic"`
returns **1** hit (Montgomery 2007); `"tolerable soil loss" AND "10Be"` returns **1** (the same);
`"soil loss tolerance" AND "soil production rate"` and `"tolerable soil loss" AND "denudation"`
return **0**. A site-level statistic between a *spatially varying* `tfact` and varying 10Be rates
does appear unpublished — but the statistic this project produced is the one withdrawn above.
Grade for the mechanism: **REDISCOVERED**. `Ha` stays REPACKAGED.

**Also unmeasured.** C43's SDA query returns `comppct_r`, `tfact` and `dbthirdbar_r` and no depth
field, so "depth anti-correlates with formation" was never tested on C43's own points. One added
column (`component.brockdepmin` or `chorizon.hzdepb_r`) would test it.

---

## [2026-09-05] correction | The EU "by contrast" clause is circular, misattributed, and factually backwards

**Was.** "The EU's proposed tolerable rates sit at 0.2-1.0x measured formation" was used as a
contrast against the USDA, sourced to C44 section 6's Verheijen 2009 rows.

**Is.** Three independent failures, all verifiable:

1. **Circular.** Verheijen et al. 2009 (`10.1016/j.earscirev.2009.02.003`, Crossref-verified,
   `is-referenced-by-count` = 595) *defines* its upper limit as equal to soil formation and reads
   0.3-1.4 t/ha/yr off a review of European soil formation rates. Dividing it by a formation rate
   recovers its own construction. It is a **positive control on the pipeline**, not a contrast —
   which is how C44 section 6 should head those rows.
2. **Misattributed.** It is a review's recommendation, adopted nowhere. The EU's actual proposed
   number, **COM(2023)416 Annex I**, was "Soil erosion rate (tonnes per hectare per year)",
   criterion **"<= 2 t ha-1 y-1"**. The adopted **Directive (EU) 2025/2360** (OJ L, 26.11.2025,
   ELI `data.europa.eu/eli/dir/2025/2360/oj`, in force 16 Dec 2025) **deleted it**: erosion moved
   to Annex I Part B, "established at Member State level", column headed "non-binding sustainable
   target values", entry "Member States shall lay down their own maximum value". **As of 2026 the
   EU has no operative numeric tolerable soil loss value.** The JRC/EUSO 2 t/ha/yr is a reporting
   indicator; Panagos et al. 2015's ~1 t/ha/yr cites formation rates, i.e. the Verheijen lineage.
3. **Backwards.** European numbers *not* defined from formation land inside the USDA range. Run
   through C44's own pipeline (`c44_data/sites.json`, rho_b = 1300 kg/m3) against the 89 German
   OCTOPUS sites, median `P` = 0.0443 mm/yr: EU-proposed 2 t/ha/yr → `T`/`P` = **3.47**; Swiss
   VBBo 2 and 4 → **3.47** and **6.94**; Lower Saxony's operative 13 t/ha/yr harmful-change
   trigger → **22.56**, against C43's US headline of 22.3. And **Switzerland's VBBo (SR 814.12)
   Annex 3 — the one operative European tolerable-erosion table — assigns its value by rootable
   soil depth** (2 t/ha/yr up to 70 cm, 4 above), which is the very rule the withdrawn sentence
   presented as the USDA's distinguishing defect.

**What produced the new numbers.** EUR-Lex and the COM(2023)416 annexes PDF read 2026-09-05;
VBBo Annex 3 and BBodSchV 2023 section 9 / DIN 19708 located the same day; the `T`/`P` column
computed from C44's existing cache. **C44's finding restated correctly:** numbers *defined from*
soil formation match soil formation; numbers not so defined — USDA, EU-proposed, Swiss, German —
sit at **3-23x** measured rates, on both continents. It is not a US-versus-Europe contrast.

---

## [2026-09-05] method | Cluster-bootstrap and spatial declustering added to the depth-gate checklist for any site-level join

C43 is the first note in this vault to compute an inferential p on thousands of geographic points
drawn from a compilation of other people's field campaigns. Its p = 4.5e-9 was wrong by roughly
eight orders of magnitude for one reason: **the 1,053 sites are not 1,053 independent draws.**
Five source studies supply 29% of them; sites within a study share region, lithology, relief and
often the same SSURGO map units.

**Rule adopted.** Any future site-level join in this vault must, before quoting a p-value,
report (a) the number of independent source studies or spatial clusters, (b) the statistic
recomputed on cluster medians, and (c) a cluster bootstrap CI — and must fix the declustering
unit **in the pre-registration**, because on C43 that choice moves rho from -0.18 to +0.02.

**Second rule.** When a compilation carries a topographic field (`SLP_AVE`, relief, elevation),
its correlation with the outcome must be reported alongside the correlation of interest. C43
carried `SLP_AVE` in `sites.json`, never reported it, and it was the largest correlation in the
dataset (+0.610 with `P`) and the confound that killed the finding.

Companion to [[failure-modes]], which covers the ways a measured **zero** can be fake; this is the
way a measured **nonzero** can be fake.
