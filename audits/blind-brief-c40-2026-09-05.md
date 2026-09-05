# Blind brief — C40 setpoint-vs-survival test of the C38 prediction

**Written 2026-09-05, BEFORE any adult-survival, life-table or margin outcome value was
fetched, joined or inspected.** Purpose: turn C38 §5's prediction from a stated expectation
into a pre-registered test, by fixing the predictor coding, the sample filter, the join key,
the statistics and the failure conditions in advance, and hashing this file.

**Blindness is partial and the limit is stated up front.** The coder (an AI) has read C38 in
full and therefore already knows C38's own 19 rows, their margins and their lever labels. This
brief is therefore blind *only* with respect to the survival outcome (b) and to any margin row
not already in C38. It is **not** blind with respect to (a) for the C38 species. Every C38
margin used below is a citation, not a re-derivation, and no C38 row may be re-graded here.

## 1. The hypothesis, as two directional clauses

> **(H1 — supply side.)** Reserve margin (dusk-or-autumn reserve over expected overnight or
> overwinter draw, minus one) is **monotone increasing** in the depth of the animal's available
> metabolic-setpoint lever: none < daily torpor < hibernation.
>
> **(H2 — no supply-side substitution.)** Lever-less small endotherms do **not** compensate
> with a larger supply-side reserve. They pay instead in mortality (lower adult annual
> survival at matched body mass and latitude) or abandon the fasting problem (round-the-clock
> foraging). Equivalently: at equal margin, the lever-less group's survival is lower.

## 2. The predictor

**Torpor capacity**, an ordinal class fixed before the outcome join:

| class | code | definition |
|---|:-:|---|
| none | **0** | no published record of daily torpor or hibernation; strict normothermy |
| daily torpor | **1** | bouts < 24 h, arousal within a circadian cycle |
| hibernation | **2** | multi-day torpor bouts, seasonal |

Coding sources, in strict precedence order (first that carries the species wins; the source
used is recorded per species):

1. **Ruf & Geiser 2015**, *Biol. Rev.* 90:891–926, `10.1111/brv.12137` — per-species appendix
   if obtainable open-access.
2. **COMBINE** (Soria et al. 2021, *Ecology* 102:e03344, `10.1002/ecy.3344`) — its
   heterothermy / torpor field, if that field exists and is populated.
3. **Nowack et al. 2020** torpor compilation, or **Geiser 2004** (`10.1146/annurev.physiol.66.032102.115105`)
   abstract/table-level class.
4. Species-level primary literature, cited.

Where available, two continuous covariates of lever *depth* are also recorded but are **not**
the primary predictor: `TMR_rel` (torpid metabolic rate / BMR) and `T_b,min` (minimum body
temperature, °C). If ≥ 8 species carry `T_b,min`, a secondary Spearman on `T_b,min` vs margin
is run and reported; otherwise it is skipped and that is stated.

**Coding discipline.** Outcome information (survival, margin, mortality, population trend) is
inadmissible evidence for the torpor class. Ambiguity — a single anecdotal torpor report, or
"hypothermia" without bout data — is coded to the **lower** class (conservative against H1).

## 3. The outcomes

- **(a) Margin.** `(reserve − expected draw) / expected draw`, dimensionless. Sources: the
  C38 §2 rows, **cited not recomputed**, plus any additional published dusk-reserve /
  overnight-cost pair found in this run. A species contributes **one** margin: the row with
  the lever in its *normally exercised* state (torpor engaged if the species uses it in
  winter), so that predictor and outcome describe the same animal-state.
- **(b) Adult survival.** Adult annual (or overwinter, where that is what is published)
  apparent survival probability φ, from open compilations in this precedence order: **AnAge**
  (genomics.senescence.info, open CSV), the **amniote life-history database** (Myhrvold et al.
  2015, *Ecology* 96:3109, `10.1890/15-0846R.1`, open), **BTO/EURING** ring-recovery estimates
  if fetchable, else species-level primary literature. Where AnAge carries only maximum
  longevity and no survival, **maximum longevity is used as a declared proxy** and every such
  row is flagged `PROXY`; a proxy-only test is reported separately and never pooled with true φ.

**Covariates:** adult body mass (g) and breeding-range mid-latitude (° absolute), from COMBINE
/ amniote / AnAge, same precedence.

## 4. The sample filter — fixed here, applied before the join

A species is in the frame iff **all** of:

1. Endotherm (bird or mammal).
2. Adult body mass **< 100 g**.
3. Breeding/wintering range centred at **absolute latitude ≥ 35°** (temperate or boreal), so a
   winter night is a real fasting problem.
4. **Resident** — obligate long-distance migrants are excluded, because migration converts the
   fasting problem into a relocation problem and contaminates apparent survival with permanent
   emigration. Partial migrants are excluded too, conservatively.
5. Torpor class codeable from §2 sources 1–4.

## 5. The join rule

Join key is **binomial species name**, normalised to lowercase, whitespace-collapsed, with a
manually maintained synonym map applied (e.g. *Parus caeruleus* → *Cyanistes caeruleus*). A
species enters a test only if it carries the predictor **and** the outcome for that test; the
two tests therefore have different n and both n are reported. Unmatched names are listed, not
dropped silently.

## 6. The statistics, pre-registered

- **T1 (H1).** Spearman rank correlation ρ between ordinal torpor class (0/1/2) and margin.
  Exact permutation p over all n! orderings if n ≤ 9, else 200,000 random permutations with the
  seed recorded. **Predicted sign: positive.**
- **T2 (H2).** Lever-bearing (class ≥ 1) vs lever-less (class 0) adult survival, controlling
  body mass and latitude by **matched pairs** — each lever-less species paired to the nearest
  lever-bearing species with |log10 mass ratio| ≤ 0.3 and |Δlatitude| ≤ 10°, each species used
  once, greedy on total distance. Test: exact one-sided sign test on paired differences.
  **If fewer than 4 pairs form, fall back to a Wilcoxon rank-sum on the unmatched groups,
  reported as such, with mass and latitude ranges of both groups printed** so the reader can
  judge the confound directly. **Predicted direction: lever-less survival lower.**
- **T3 (falsifier scan, not a statistic).** Enumerate every class-0 species in the sample with
  a published margin **> +100%**. C38 §5's falsifier: one such species falsifies the mechanism
  claim. Expected count if the hypothesis holds: **zero**.

## 7. Sample-size threshold — pre-declared

- **T1** is a claimable pass/fail only if **n ≥ 8 species and ≥ 2 distinct torpor classes with
  ≥ 3 members each**. Below that: **direction only, DIRECTION-ONLY verdict, no p-value gate.**
- **T2** is claimable only with **≥ 4 matched pairs**, or ≥ 5 species per group under the
  fallback. Below that: **DIRECTION-ONLY.**
- **T3** always runs; it needs no n.

## 8. Pre-declared failure conditions

- **H1 FAILS** if Spearman ρ is negative (any n, reported as direction-only when underpowered).
- **H2 FAILS** if lever-less survival is **higher** than matched lever-bearing survival.
- **The mechanism claim FAILS outright** if T3 returns ≥ 1 lever-less small endotherm with a
  published margin > +100%.

## 9. Order of operations (binding on the coder)

1. This file is written and its sha256 recorded below.
2. Torpor classes and the species frame are coded from §2/§4 sources only.
3. Only then are survival, mass and latitude fetched and joined.
4. `vault/_scripts/c40_setpoint.py` carries every literal and prints every statistic.

## sha256 of this file (bytes above this line)

`python vault/_scripts/c40_setpoint.py --verify-brief` recomputes it.

`sha256(first 7811 bytes of this file) = 1e2bc903ba59099120b4fb1f300d836cb67cb83261f697a18843ff9d91db5dff`

Hashed 2026-09-05, before any outcome datum was fetched.
