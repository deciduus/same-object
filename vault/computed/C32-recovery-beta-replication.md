---
name: C32-recovery-beta-replication
type: computed
exit: computation
extends-to: [ecology, conservation]
next-step-cost: M
---

# Replicating [[C29-recovery-beta]] on Moreno-Mateos 2017: early-or-never reproduces qualitatively, the per-habitat *ordering* does not, and no `β` is identifiable.

> **Prediction 1 of [[C29-recovery-beta]] §5 — that the per-habitat Weibull `β` would rank-correlate
> positively across two independent recovery meta-analyses — is a FAIL in substance and a
> coin-flip on the letter: Spearman `ρ = +0.100` (n = 5, exact two-sided p = 0.950) at the
> outcome-measure level and `ρ = −0.300` (p = 0.683) at the study level, so the *sign* the
> prediction named flips with a defensible change of analysis unit and is indistinguishable from
> zero either way.**

What replicates is **weaker than a number, and the note must not pretend otherwise.** Under
C29's likelihood this database gives pooled `β = 0.733` (95% profile CI 0.703–0.764) on 3,688
records, `β < 1` in four of five habitat classes. But §2(b) establishes that these are
*current-status* (case-1 interval-censored) data, so C29's exact-event-time likelihood is the
**wrong** one here; under the correct current-status likelihood the same rows give
`β = 0.051 [0.014, 0.089]` with `η` in the billions of years — a factor of 14 away.
**The shape parameter is therefore not identifiable from this database.** What survives is the
qualitative claim underneath it: the fraction of outcome measures that have reached their
reference is nearly *flat* in elapsed time (0.29 at ≤2 yr, 0.36 above 80 yr, over a 190-fold
span), which is "early-or-never" in its most extreme form and is what both likelihoods are
reacting to. **The corner of [[C18-durability-axis]]'s axis holds qualitatively; neither the
map within the corner nor any specific `β` does.** Replicates the computation of
[[G32-recovery-time-hazard-shape]] *qualitatively only*; uses the estimator of
[[C29-recovery-beta]] unchanged, and shows that on this dataset that estimator is misapplied.

## 1. Target and why this one

Moreno-Mateos, D. *et al.* (2017) "Anthropogenic ecosystem disturbance and the recovery debt",
*Nature Communications* **8**:14163, `doi 10.1038/ncomms14163` — named by [[C29-recovery-beta]] §5.1
as one of two admissible replication targets.

| Input | Value | Source / fetch |
|---|---|---|
| Per-study database | 3,816 outcome-measure rows × 26 cols, 356 primary studies; cols incl. `Habitat category / Disturbance category / Metric type / Time since restoration started / Start / End / Goal` | Dryad `doi:10.5061/dryad.t5c97`, file **`Moreno, Jones database.xlsx`** (400,066 bytes), **fetched 2026-09-05**. The paper's own Data Availability statement names this deposit |
| Nature Comms supplement | 30 pp PDF: Supplementary Figures 1–7, Tables 1–3, reference list. **No machine-readable per-study table** | `media.springernature.com/.../41467_2017_BFncomms14163_MOESM1146_ESM.pdf`, fetched 2026-09-05 (937,400 bytes) |
| Second target, **rejected** | Crouzeilles *et al.* 2016, `doi 10.1038/ncomms11666`, Dryad `doi:10.5061/dryad.k3479`, `Meta_analysis.txt`: `Site / Disturbance_Conversion / taxon-and-metric dummies / RR`. **No time column and no recovery yes/no** — no survival time can be built from it at all | Dryad, fetched 2026-09-05 |
| Fit code | `vault/_scripts/c32_replication.py`; the MLE and profile-likelihood CI are C29's, unchanged | this vault |

`datadryad.org` sits behind a proof-of-work bot check; the deposit was retrieved through an
ordinary browser session rather than by defeating the check, and the script takes the file by path
rather than pretending it can fetch it.

## 2. The coding step, which is the whole methodological risk

**Moreno-Mateos does not measure a recovery time. It measures a recovery *debt*.** Each row records
the value of one outcome measure when recovery started (`Start`, `Xs`), its value at the end of the
observation window (`End`, `Xe`), the reference-system value (`Goal`, `Xr`), and the elapsed
`Time since restoration started` (`T`, years). The paper's estimand is the integrated shortfall of
`Xe` against `Xr` — a magnitude, not a duration.

The conversion actually used:

```
recovered  iff  Xe reached or crossed Xr in the direction of travel from Xs
                (Xs < Xr → Xe ≥ Xr ;  Xs > Xr → Xe ≤ Xr)
time       =    T
recovered      → EVENT          at T
not recovered  → RIGHT-CENSORED at T
```

**What that assumes, stated plainly.** (a) That the direction of travel is set by `sign(Xr − Xs)`,
so "recovered" means crossing the reference from the disturbed side — which is Moreno-Mateos'
own scenario set (their Supplementary Fig. 5) but converts their continuous debt into a
threshold crossing and discards the magnitude. (b) **That a row coded as an event *at* `T` reached
its goal *at* `T`.** It did not: Moreno-Mateos observed status at `T`, so a recovered row reached
`Xr` at some unknown time ≤ `T`. This is *current-status* (case-1 interval-censored) data being
fed to a likelihood written for exact event times, and it systematically **overstates** the
recovery times of the recovered rows. §5 reports what happens when the correct likelihood is used
instead, and it is not reassuring. (c) That one outcome measure is one observation — 3,816 rows
come from 353 studies, so the rows are not independent. §5 refits at study level.

Row accounting, all 3,816 data rows:

| | rows |
|---|---|
| Data rows read | 3,816 |
| Dropped — `Start` equals `Goal` (already at the reference; no recovery to observe) | 128 |
| **Used** | **3,688** (1,139 events, 2,549 right-censored; 353 distinct studies) |

Censoring is **69.1%**, against C29's 42.5%.

**Habitat mapping, declared before fitting** (Moreno-Mateos `Habitat category` → C29 class):
Forest → Forest; Marine (benthic) + Marine (pelagic) → Marine; Lake + River + Freshwater wetland →
Freshwater; Tidal wetland + Mangrove → Brackish; Grassland → Terrestrial.

## 3. Result — β by habitat, C29's estimator

Profile-likelihood 95% CI at Δ logL = 1.921. `*` marks a CI lying entirely below 1.

| Habitat | N | events | censored | **β** | 95% CI | η (yr) | | C29's β |
|---|---|---|---|---|---|---|---|---|
| Forest | 1,568 | 499 | 1,069 | **0.886** | [0.828, 0.946] | 88.4 | `*` | 0.769 |
| Marine | 690 | 209 | 481 | **0.810** | [0.729, 0.895] | 26.1 | `*` | 0.644 |
| Freshwater | 953 | 261 | 692 | **0.689** | [0.633, 0.746] | 111.6 | `*` | 0.893 |
| Brackish | 226 | 89 | 137 | **0.620** | [0.540, 0.701] | 23.5 | `*` | 0.501 |
| Terrestrial (grassland) | 251 | 81 | 170 | **1.136** | [0.946, 1.344] | 47.6 | — | 0.570 |
| **ALL POOLED** | **3,688** | **1,139** | **2,549** | **0.733** | **[0.703, 0.764]** | **79.9** | `*` | 0.587 |

Four of five habitat classes reject `β = 1` downward, as in C29 — but **not the same four**. C29's
one non-rejecting class was Freshwater; here Freshwater is the *second lowest* and the
non-rejecting class is Terrestrial, which C29 put near the bottom at 0.570.

### By disturbance category (N ≥ 30)

| Disturbance | N | **β** | 95% CI | η (yr) | C29's β |
|---|---|---|---|---|---|
| Hurricane | 543 | **0.531** | [0.482, 0.581] | 40.7 | — |
| Eutrophication | 786 | **0.750** | [0.685, 0.816] | 112.0 | 1.025 |
| Overfishing | 84 | 0.792 | [0.566, 1.054] | 11.5 | — |
| Damming / hydrologic | 118 | 0.843 | [0.650, 1.059] | 32.5 | — |
| Oil | 300 | 1.044 | [0.900, 1.194] | 13.9 | 0.652 |
| Agriculture | 614 | **1.165** | [1.033, 1.307] | 95.5 | 1.254 |
| Logging | 494 | **1.165** | [1.029, 1.308] | 96.0 | 0.679 |
| Mining | 620 | **1.181** | [1.050, 1.320] | 35.0 | — |
| Invasive species | 71 | **1.513** | [1.111, 1.976] | 14.8 | 0.972 |

C29's *qualitative* disturbance story — acute physical pulses lowest, chronic land-use presses at
or above 1 — is recognisable here (hurricane lowest at 0.531; agriculture, logging, mining all
above 1). But on the five categories the two datasets share, the rank correlation is
**`ρ = +0.051`, n = 5, exact p = 1.000**: another honest zero. Logging moves from 0.679 to 1.165
and oil from 0.652 to 1.044, both across non-overlapping CIs.

## 4. The two predictions

### Prediction 1 — sign of the per-habitat rank correlation

| Unit of analysis | ρ | n | exact two-sided p | verdict on the stated sign |
|---|---|---|---|---|
| Outcome measure (headline) | **+0.100** | 5 | 0.950 | passes |
| Study × habitat (§5) | **−0.300** | 5 | 0.683 | fails |

C29 §5.1 also named a *content*: "`β` lowest for marine benthic and brackish systems (0.4–0.7),
highest for freshwater pelagic and agricultural-press systems (0.9–1.3), forest intermediate
(~0.75)." Scored item by item: **brackish lowest — correct** (0.620, the lowest of the four
aquatic/marine classes). **Marine low — wrong** (0.810, second highest). **Freshwater highest —
wrong** (0.689, second lowest, and its CI excludes C29's 0.893). **Forest intermediate at ~0.75 —
near-miss** (0.886). **Agricultural presses high — correct** (1.165). One of five habitat
statements survives, plus the agricultural-press clause.

**Verdict: prediction 1 fails.** The sign is positive in the headline coding, negative in the
study-level coding, and no coding gets within a factor of ten of significance. C29 §5.1 said a
"null or negative correlation kills the claim that `β` measures anything about ecosystems rather
than about how each meta-analyst coded the free text." That is the outcome, and this note records
it against C29 rather than around it.

### Prediction 2 — the frailty split by response-variable class

Moreno-Mateos' `Metric type` is a clean categorical, which is exactly why C29 §5.2 named this
dataset for the test. Structural/biomass = Abundance, C, N, Organic matter; compositional/species
= Diversity.

| Split | N | **β** | 95% CI |
|---|---|---|---|
| **Pooled** | 3,688 | **0.733** | [0.703, 0.764] |
| Class: structural/biomass | 3,083 | 0.723 | [0.689, 0.756] |
| Class: compositional/species (Diversity) | 605 | 0.824 | [0.741, 0.910] |
| — metric: Abundance | 2,378 | 0.708 | [0.672, 0.744] |
| — metric: Carbon | 296 | 0.737 | [0.608, 0.877] |
| — metric: Nitrogen | 247 | 0.685 | [0.549, 0.836] |
| — metric: Organic matter | 162 | 1.154 | [0.947, 1.378] |
| Forest × structural | 1,264 | 0.834 | [0.773, 0.898] |
| Forest × compositional | 304 | **1.166** | [1.011, 1.328] |
| Marine × structural | 566 | 0.825 | [0.731, 0.925] |
| Marine × compositional | 124 | 0.966 | [0.771, 1.178] |
| Freshwater × structural | 845 | 0.691 | [0.632, 0.752] |
| Brackish × structural | 196 | 0.596 | [0.514, 0.682] |
| Terrestrial × structural | 212 | 1.220 | [0.992, 1.473] |

**The frailty signature is present but partial, and it is not the clean result C29 asked for.** The
classic signature C29 named — within-class `β` rising toward 1 while the pooled `β` stays at its
low value — appears in the *compositional* class (0.733 → 0.824) and much more strongly in the
habitat × class cells (Forest × compositional 1.166 with its CI **above** 1; Marine × compositional
0.966; Terrestrial × structural 1.220). It does **not** appear in the class that carries 84% of the
rows: structural/biomass sits at 0.723, statistically indistinguishable from the pooled 0.733, and
Freshwater × structural and Brackish × structural go *down*, to 0.691 and 0.596.

The honest reading is that **stratifying moves `β` upward wherever stratification actually reduces
the timescale mixture, and does nothing where it does not** — which is what C29 §6 said the
problem was, restated as a measurement. Abundance-of-something-in-a-forest is still a mixture of a
5-year bird count and a 200-year biomass chronosequence; the metric label does not separate those.
Prediction 2 is therefore **not decided by this run**: it is neither the null result (no change) nor
the frailty result (uniform rise to 1), and the fact that the split works in the small class and
fails in the large one is more consistent with "residual mixture" than with either clean story.

## 5. §Honesty — what is wrong with this replication

- **The two datasets are not independent, and this is the largest single caveat.** The Dryad file
  is literally named **`Moreno, Jones database.xlsx`**, and the paper's own R script credits data
  manipulation to "Peter Jones". Matching first-author surname + publication year across the two
  reference lists: **95 primary studies appear in both** — **37.3% of Jones & Schmitz's 255
  references and 27.0% of Moreno-Mateos' 352**. (Surname+year matching over-merges homonyms and
  under-merges renamed authors, so read 95 as a point estimate with a spread of perhaps ±10, not
  an exact count.) Roughly a third of the "independent" replication set is the discovery set.
  **Shared studies inflate agreement, and this replication still failed on ordering** — which
  makes the failure harder to explain away, not easier, but also means the pooled `β = 0.733`
  agreeing with `β = 0.587` is worth substantially less than an independent agreement would be.
- **The event times are not event times.** §2(b): recovered rows are coded at the observation time
  `T`, not the (unobserved) crossing time. Fitting the correct current-status likelihood
  (`log F(T)` for recovered, `log S(T)` for not) instead **degenerates**: pooled
  `β = 0.051 [0.014, 0.089]` with `η` in the billions of years, and every habitat the same. The
  reason is visible in the raw data and is the single most informative number in this note —
  the fraction of outcome measures that have reached their reference is **flat in time**:

  | `T` (yr) | (0,2] | (2,5] | (5,10] | (10,20] | (20,40] | (40,80] | >80 |
  |---|---|---|---|---|---|---|---|
  | n | 908 | 448 | 661 | 744 | 483 | 358 | 86 |
  | fraction recovered | 0.287 | 0.297 | 0.300 | 0.323 | 0.308 | 0.355 | 0.360 |

  Over a 190-fold span of elapsed time the recovered fraction moves from 0.29 to 0.36. Read as
  survival, that is "early-or-never" in its most extreme form. Read as measurement, **it means `T`
  carries almost no information about recovery status in this dataset**, so the per-habitat `β`
  differences in §3 are driven mainly by how the `T` distribution differs between habitats. That
  is a sufficient explanation for prediction 1's failure on its own.

  **What transfers to C29, and what does not.** An earlier version of this bullet said the flat
  table "is a warning about C29's `β` as much as about this one". That transfer was stated in the
  wrong direction and is withdrawn. The **current-status objection does not reach C29**: Jones &
  Schmitz report a stated `Return Time` per recovered study, i.e. exact event times, so C29's
  likelihood is the right one for C29's data. What *does* transfer, and was not named, is
  **design-chosen censoring times**: `T` is a design variable on both sides — Moreno-Mateos'
  chronosequences choose their elapsed window, and Jones & Schmitz's censored rows are censored
  at study end-dates chosen by funding and publication, not by a follow-up that ran out. C29 §6
  already flags informative censoring as "the worst problem here"; this note supplies the
  independent second instance of it, which is the honest read-across.
- **Pseudo-replication.** 3,688 rows, 353 studies, up to 72 outcome measures from one study. The
  CIs in §3 are far too narrow: they treat correlated measures as independent. Collapsing to one
  record per study × habitat (recovered if any measure recovered, at the study's median `T`) gives
  pooled `β = 0.721 [0.658, 0.786]` — the point estimate barely moves, which is reassuring — but
  Forest 0.913, Marine 0.769, Freshwater 0.647, Brackish 0.659, Terrestrial 0.948, and **that is
  the reordering that flips prediction 1's sign to −0.300.** No CI in §3 or §4 should be quoted
  without this sentence attached.
- **The recovery criterion is mine and it is harsher than Moreno-Mateos'.** Crossing `Xr` exactly
  is a stricter event than any debt-based criterion, and it throws away the magnitude that is the
  paper's actual finding. A row at 99% of its reference after 200 years is coded identically to a
  row at 5%. The 69.1% censoring rate is a consequence of that choice, not a property of ecology.
- **Censoring is informative here for the same reason it was in C29 §6**, and additionally because
  `T` is a *design* variable (how long the study ran) rather than a follow-up that ended when
  someone stopped watching — chronosequence studies choose their `T`.
- **`η` is not comparable across the two notes.** C29's pooled `η` was 39.4 yr against 79.9 yr
  here, but the event-time overstatement in §2(b) inflates this one by an unknown factor. Nothing
  in this note rests on `η`.
- **What is *not* damaged — and it is a qualitative claim, not a number.** Three likelihood
  variants were run on these data:

  | variant | likelihood | pooled `β` | 95% CI |
  |---|---|---|---|
  | Outcome-measure rows (headline §3) | C29's, exact event times | 0.733 | [0.703, 0.764] |
  | Study × habitat (pseudo-replication fix) | C29's, exact event times | 0.721 | [0.658, 0.786] |
  | **Outcome-measure rows, correct likelihood** | **current-status (case-1)** | **0.051** | **[0.014, 0.089]** |

  The first two agree with each other because they share a likelihood that §2(b) shows is the
  wrong one for this data; that agreement is **not** robustness. The third disagrees by a factor
  of 14 and is the one entitled to the data. **Under the correct likelihood the Weibull shape is
  not identifiable from this database**, and no value of `β` — 0.733, 0.721 or 0.051 — should be
  quoted from here as a measurement of the object [[C29-recovery-beta]] measured. `η` is worse
  still (billions of years under the correct likelihood) and nothing rests on it.

  What survives all three variants is one qualitative fact, read straight off the raw data
  without any Weibull at all: **the recovered fraction is nearly flat in elapsed time** — 0.287 at
  `T ≤ 2` yr against 0.360 at `T > 80` yr, a 190-fold span of time for a 0.07 change in fraction.
  Whatever else is true, ecosystems in this database that have not reached their reference early
  overwhelmingly do not reach it later. That is **early-or-never as a qualitative claim**, it is
  the corner of [[C18-durability-axis]] that C29 named, and it is all this replication delivers.

  What does **not** survive: any specific `β`; the `η` scale; any claim that `β` resolves
  *between* ecosystem types (prediction 1, failed in §4); and the earlier framing of 0.733 as a
  robust replication of 0.587.

## Corrections 2026-09-05 (audit 06)

`audits/06-math-rounds3-6.md` items 10 and 11. No number changed; what changed is which
numbers the note is willing to certify.

**1. The headline `β` was certified as robust by a comparison that omitted the disagreeing
variant.** §5's "what is *not* damaged" bullet read: "`β < 1` pooled … at `0.733 [0.703, 0.764]`.
Both the analysis-unit variants agree (0.733 and 0.721)." Those two variants share **C29's
likelihood**, which §2(b) of this same note establishes is the wrong likelihood for
current-status data. The third variant — the correct current-status likelihood, run and reported
three bullets earlier in the same section — gives `β = 0.051 [0.014, 0.089]`, a factor of 14
away, with `η` in the billions of years. Quoting the agreement of two runs of the wrong
estimator as robustness was the defect.

| pooled `β` | likelihood | status |
|---|---|---|
| 0.733 [0.703, 0.764] | C29's, exact event times | wrong likelihood for this data |
| 0.721 [0.658, 0.786] | C29's, exact event times, study × habitat | wrong likelihood for this data |
| **0.051 [0.014, 0.089]** | **current-status (case-1)** | **the one entitled to the data** |

The callout and §5 now say plainly: **under the correct likelihood the Weibull shape is not
identifiable from this database**, and no specific `β` may be quoted from here.

**What survives, stated as a qualitative claim.** The recovered fraction is nearly flat in
elapsed time — 0.287 at `T ≤ 2` yr, 0.360 at `T > 80` yr, across a 190-fold span. That is read
straight off the raw data with no Weibull involved, it is what both likelihoods are reacting to,
and it is **early-or-never as a qualitative statement**. The infant-mortality corner of
[[C18-durability-axis]] survives on that basis and on no other.

**What does not survive.** Any specific `β` from this database; the `η` scale; any claim that
`β` resolves between ecosystem types (prediction 1 already failed in §4); and the framing of
`0.733` as a robust replication of C29's `0.587`.

**2. The read-across to C29 was pointed the wrong way.** §5 said the flat table "is a warning
about C29's `β` as much as about this one". It is not. Jones & Schmitz report a stated
`Return Time` per recovered study — **exact event times** — so the current-status pathology is
specific to Moreno-Mateos and does not transfer. What *does* transfer, and was unnamed, is
**design-chosen censoring times**, shared by both datasets. §5 now states both directions.

**Proposed C29-facing sentence** (for whoever edits [[C29-recovery-beta]]; not applied here
beyond the note it already carries):

> C32's replication does **not** confirm `β = 0.587` numerically: the Moreno-Mateos database is
> current-status data, and under the correct likelihood its shape parameter is not identifiable
> (`β = 0.051 [0.014, 0.089]`, `η` in the billions of years), so the `β = 0.733` sometimes quoted
> from it is a run of *this* note's likelihood on data that likelihood does not fit. What C32
> independently corroborates is the qualitative shape only — the recovered fraction is nearly
> flat in elapsed time — and what it independently *falsifies* is prediction 5.1, the
> per-habitat ordering. The current-status objection does not reach this note's own fit; the
> **design-chosen censoring times** objection does, and is the same one §6 already names as the
> worst problem here.

**Script.** `vault/_scripts/c32_replication.py` now prints all three variants together under
`ROBUSTNESS ACROSS LIKELIHOOD AND UNIT`, plus the recovered-fraction-vs-elapsed-time table, on
every run, so the three can no longer be quoted apart. The Dryad file
`Moreno, Jones database.xlsx` (`doi:10.5061/dryad.t5c97`) is **not in this repository** and
`datadryad.org` sits behind a proof-of-work bot check, so the script cannot fetch it; the
`--xlsx` path argument is retained and a missing file now produces an explicit message naming
the deposit, the file, the byte size and the manual download step, and exits 2 rather than
raising a bare `FileNotFoundError`. This note's numbers therefore remain **unreproduced in CI**;
that is a known and stated limitation, not a silent one.
