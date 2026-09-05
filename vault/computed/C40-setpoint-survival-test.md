---
name: C40-setpoint-survival-test
type: computed
last-checked: 2026-09-05
result: "Pre-registered test of C38 §5. T1 (torpor class vs margin) n=4, Spearman rho=+0.63, exact p=0.500 — direction as predicted, UNDERPOWERED by the brief's own gate (needs n>=8). T2 (survival) run on a PROXY (AnAge maximum longevity, not phi): 25 mass- and latitude-matched pairs, 21/24 in the predicted direction, one-sided sign p=0.00014; Chiroptera-free sensitivity 11/15, p=0.059. T3 falsifier scan: 0 lever-less species with a published margin > +100%. Not falsified; also not yet a test of the survival clause."
exit: prediction
extends-to: [ecology, conservation]
next-step-cost: L
---

# The setpoint lever vs survival — C38 §5 run against a pre-hashed brief

> **PARTIAL PASS, and the pass is the weak half.** The falsifier scan returns **zero** and the
> margin ordering runs the predicted way (`rho = +0.63`, n = 4), but the margin test is
> **UNDERPOWERED by the brief's own pre-declared gate** and the survival test was run on a
> **proxy the brief pre-authorised and this note must not oversell** — maximum longevity, not
> ring-recovery `phi`. **The sentence that survives: no lever-less small endotherm with a
> published margin above +100% exists in the sample, and lever-bearing small temperate mammals
> outlive mass- and latitude-matched lever-less ones (21/24 matched pairs, p = 0.00014) — but
> drop the bats, whose longevity is bought by flight rather than by torpor, and that collapses
> to 11/15, p = 0.059.** C38 §5's survival clause is *consistent with*, not *supported by*,
> what could be fetched.

Brief: `audits/blind-brief-c40-2026-09-05.md`,
`sha256 = 1e2bc903ba59099120b4fb1f300d836cb67cb83261f697a18843ff9d91db5dff` over its first
7,811 bytes, written and hashed **before any survival, longevity or latitude value was
fetched**. Recompute: `python _scripts/c40_setpoint.py --verify-brief`.
Arithmetic: `python _scripts/c40_setpoint.py` from `vault/`. Fetches all **2026-09-05**.

## 1. What was fixed in advance, and what was not

Fixed: the two directional clauses, the ordinal predictor (0 none / 1 daily torpor /
2 hibernation), the outcome definitions, the <100 g and |lat| >= 35 deg filter, migrant
exclusion, the join key, both statistics, and the sample-size gates.

**Not blind, declared in the brief's own second paragraph:** the coder had read
[[C38-reserve-margin-across-species]] in full and therefore already knew every margin in T1.
The brief is blind only with respect to the survival outcome. No C38 row is re-derived here;
all are cited.

## 2. Data actually obtained

| dataset | what it gave | URL |
|---|---|---|
| **Ruf & Geiser 2015** *Biol. Rev.* 90:891–926, `10.1111/brv.12137` — the **per-species Appendix**, 214 species x (T, BM, Tb_min, TMR_min, TMR_rel, TBD_max, LAT) | the predictor, at species level | open PMC copy `PMC4351926`, <https://pmc.ncbi.nlm.nih.gov/articles/PMC4351926/> |
| **AnAge** build 14 (4,645 species) | maximum longevity, adult weight, data quality | <https://genomics.senescence.info/species/dataset.zip> |
| **PanTHERIA** 1.0 WR05 | `26-4_GR_MidRangeLat_dd` mid-range latitude | <https://esapubs.org/archive/ecol/E090/184/PanTHERIA_1-0_WR05_Aug2008.txt> |
| **BTO BirdFacts** | adult annual survival for *Cyanistes caeruleus*, `0.532 ± 0.008` | <https://www.bto.org/understanding-birds/birdfacts/blue-tit> |
| **C38 §2** | all four margins, cited not recomputed | [[C38-reserve-margin-across-species]] |

**C38 §5 said the Ruf & Geiser per-species appendix "was not obtained". It now has been** — it
is present in full in the open PMC author manuscript, which the Europe PMC `fullTextXML`
endpoint returns 404 for while the PMC HTML serves it. That is the single largest new asset
here and it is what makes a species-level predictor possible at all.

**AnAge carries `IMR (per yr)` for 43 of 4,645 species and none of the frame.** No open
compilation of adult annual survival for small mammals was found. BTO gives real `phi` for
British birds, but every resident British passerine falls in class 0 or is unclassifiable, so a
bird-only T2 has no lever-bearing arm and **cannot be run**. Hence the proxy.

## 3. T1 — margin vs torpor class

| species | class | margin (C38 §2 row) |
|---|:-:|---|
| *Peromyscus maniculatus* | 1 | **+265%** warm-acclimated, lever engaged (Rezende 2009 T1) |
| *Myotis lucifugus* | 2 | **+99%** median of the three lever-engaged rows (+75 / +99 / +383) |
| *Cyanistes caeruleus* | 1 | **+57%** hypothermia ON (Brodin 2017 via [[C33-lolp-starvation]] §4) |
| *Sorex araneus* | 0 | **−69%** median of −38 / −69 / −74 (Keicher 2017) |

`n = 4`; class counts {0:1, 1:2, 2:1}. **Spearman rho = +0.6325, exact two-sided p = 0.5000**
(all 24 permutations). Direction **as predicted**. Gate (n >= 8 and two classes with n >= 3):
**NOT MET → DIRECTION-ONLY, no pass claimed.** Over all 36 combinations of the alternative C38
rows per species rho stays positive (`+0.63` to `+0.95`); recoding the parid to class 0 gives
`+0.74`. The secondary `Tb_min` Spearman was pre-conditioned on >= 8 species and is **skipped**
(2 available).

Excluded by the pre-registered filter, and this is where the power went: **both hummingbirds**
(*Selasphorus rufus* +2421%, *Archilochus colubris* +116%) are obligate long-distance migrants,
and they are exactly the rows that would have made the ordering steep. The filter cost the test
its two strongest points, and it was fixed before they were counted.

## 4. T2 — survival, on a proxy

Frame: AnAge Mammalia in Chiroptera / Rodentia / Eulipotyphla, mass < 100 g, AnAge data quality
`acceptable` or `high`, PanTHERIA |mid-range latitude| >= 35 deg, six migratory bats excluded by
name. **n = 75** (43 lever-bearing, 32 lever-less). Classes: 18 from the Ruf & Geiser Appendix
at species level; 57 from a clade rule at family or genus level (see §5.2).

- **Matched pairs**, |Δlog10 mass| <= 0.3 and |Δlat| <= 10 deg, greedy: **25 pairs**.
- **Sign test, one-sided:** **21 of 24** non-tied pairs in the predicted direction,
  **p = 0.00014**. Gate (>= 4 pairs): **MET**.
- Unmatched Wilcoxon rank-sum: `W = 690.5, z = −5.63, p = 1.8e−08`.
- Mean proxy: lever-less **4.52 yr** vs lever-bearing **14.84 yr**. **AS PREDICTED.**
- **POST-HOC, not pre-registered — Chiroptera dropped** (bat longevity is bought by flight and
  predation escape, not by the lever): 16 pairs, **11/15, one-sided p = 0.0592**; rank-sum
  `z = −2.67, p = 0.0076`; means 4.52 vs **6.44 yr**. Direction survives; the effect size falls
  by a factor of five and the sign test stops clearing 0.05.

## 5. T3 — the falsifier scan, and the coding that decides it

**Zero.** The only lever-less species in the sample carrying a published margin is *Sorex
araneus* at −69%. **No lever-less small endotherm with a published margin > +100% exists in
this sample. The mechanism claim is NOT FALSIFIED.**

**5.1** The scan's reach is one species. C38 §5 wrote the falsifier knowing the shrew was its
only lever-less row; this run did not widen it, because no additional lever-less dusk-reserve /
overnight-cost pair was found. **A falsifier scanned over n = 1 is a formality, not a test.**

**5.2 The coding rule that had to be amended mid-run, disclosed.** Applying the brief's source-1
rule literally — absent from the Ruf & Geiser Appendix → class 0 — coded ~20 obligate
hibernators (*Myotis daubentonii*, *M. brandtii*, *Eptesicus nilssonii*, *Tamias sibiricus*,
*Dryomys nitedula*, …) as lever-less, because that Appendix is a **positive-record compilation**
and absence from it means "not measured", not "not capable". The brief's §2 precedence chain
does handle this — non-carrying sources fall through to source 3 — so a clade rule from
Geiser 2004 review-level classes was applied: Vespertilionidae / Rhinolophidae / Gliridae /
Heteromyidae / Dipodidae and genus *Tamias*, *Dipodomys* → 2; *Crocidura*, *Peromyscus*,
*Phodopus*, *Mus*, *Mystacina* → 1; *Sorex*, *Neomys*, *Blarina*, *Apodemus*, *Micromys*,
*Microtus*, *Myodes*, *Lemmus*, *Dicrostonyx*, *Lagurus*, *Alticola*, *Lasiopodomys*,
*Ellobius*, *Talpa*, *Mogera*, *Scalopus*, *Meriones*, *Allactaga*, *Onychomys*, *Reithrodon*,
*Pseudomys* → 0. **The longevity column was already on screen when that rule was written.** The
rule is taxonomic and not outcome-tuned, but the blind was broken at that point and the reader
should discount T2 accordingly. Under the **literal** source-1 rule the direction still holds
(lever-less 9.66 yr vs lever-bearing 12.89 yr) but **all significance is lost**: 11/18 pairs,
one-sided `p = 0.240`; rank-sum `z = −1.38, p = 0.167`. **T2's p-value is a function of the
torpor coding, not of the survival data.**

## 6. Honesty

1. **The survival outcome is not survival.** It is AnAge maximum longevity — a right-tail
   order statistic that scales with sampling effort and captivity, correlated with but not
   equal to adult annual `phi`. The brief pre-authorised this and required the `PROXY` flag;
   this note carries it. **No number in §4 is a survival probability.** Real `phi` was obtained
   for exactly one species in the frame (*Cyanistes caeruleus*, 0.532, BTO) and one species is
   not a test.
2. **The bats are the result.** Chiroptera are 25 of the 43 lever-bearing rows and carry the
   longest longevities in the table. Flight and roost inaccessibility depress predation
   independently of torpor; hibernation and volancy are confounded across the whole clade and
   this design cannot separate them. Dropping them (§4, post-hoc) leaves the direction intact
   at p = 0.059 — which is the honest headline for the survival clause.
3. **Predation is uncontrolled and runs the same way as the hypothesis.** Voles and shrews are
   staple prey for owls, mustelids and foxes; bats and hibernating rodents in burrows are not.
   A predation-only model predicts the §4 result with no reference to metabolic setpoints at
   all. Nothing here distinguishes the two.
4. **Migrants were excluded and the exclusion was expensive.** It removed both hummingbird rows
   from T1 — the largest margins C38 has — and six bats from T2. The rule was fixed in advance
   and applied; it is not a post-hoc filter, but it is why T1's n is 4.
5. **Torpor coding quality is the weakest link and is quantified in §5.2**: 18 of 75 species
   coded from a species-level source, 57 from a clade rule written with the outcome column
   visible. Under the strict source-1 rule T2's p goes from 0.00014 to 0.240. **This is the
   single result a replication would most likely overturn.**
6. **The margin data are sparse and almost entirely C38's.** Four species, four rows, three of
   them requiring a within-species choice among C38 rows (median taken, all 36 combinations
   reported). **No new margin pair was found in this run.** T1 is C38 re-sorted, not
   independent evidence.
7. **Prior knowledge.** The AI coder had read C38 in full — including its §5 prediction, its
   falsifier and its lever labels — before writing the brief. It also knew, as general
   background, that bats and dormice are long-lived and shrews are not; the §4 direction was
   never in doubt to the coder. **T2 is therefore not a prediction that was risked.** The only
   genuinely risked quantity in this note is T3's count.
8. **What a human-coded replication needs.** (a) Torpor class coded from primary literature per
   species by a coder blind to longevity and survival, with an explicit "not measured" category
   distinct from "normothermic", and inter-coder agreement reported. (b) Real adult annual
   `phi` from EURING/BTO for birds and from CMR studies for mammals — not longevity. (c) A
   phylogenetic mixed model (PGLS or a Brownian random effect on the tree), because 25 of 43
   lever-bearing rows are one order and the 75 rows are not independent. (d) At least ten new
   published dusk-reserve/overnight-cost pairs, of which at least three lever-less, before T1
   or T3 mean anything.

## 7. What this changes about C38

Nothing is overturned. C38 §5's first three clauses (margin monotone in lever depth) get a
direction and no power. Its fourth clause (lever-less pay in mortality) gets a large,
confounded, proxy-based signal that survives the obvious confound at p = 0.059 and dies if the
torpor coding is done strictly. **C38's falsifier stands unfired, over a sample of one.**

See [[C38-reserve-margin-across-species]], [[C33-lolp-starvation]],
[[C39-duane-governance-blind]], [[reservoir-audit]].
