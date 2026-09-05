# Blind brief — C52, the setpoint→survival test on real adult annual survival

**Written 2026-09-05, BEFORE any adult-annual-survival (`phi`) value was fetched, scraped,
joined or inspected.** This brief is the pre-registration for programme item **P-008** (Ruf &
Geiser × ring-recovery survival) and carries **P-072** (the setpoint falsifier) as a rider.

It exists because two prior runs in this vault were killed or wounded by attacks that a brief
could have pre-empted. `audits/c43-adversarial.md` killed C43 with five moves: spatial
pseudoreplication, a confound with an obvious covariate (slope), effect size vs p-value,
prior art on the mechanism, and a comparison clause that turned out to be a **positive control
by construction**. [[C40-setpoint-survival-test]] survived but on a proxy, with the blind broken
mid-run and a p-value that moved from `0.00014` to `0.240` under a different torpor coding.
**Every section below is written to make those same attacks land on the brief rather than on the
result.** Where an attack cannot be pre-empted, the brief says so and pre-commits to reporting
the failure rather than routing around it.

## 0. What this brief is blind to, stated first

The coder (an AI) has read [[C38-reserve-margin-across-species]] and
[[C40-setpoint-survival-test]] in full and therefore already knows every C38 margin, C40's
longevity result, and C40's torpor coding problem. It has, before writing this brief, also read
the **abstract** of Turbill, Bieber & Ruf 2011 (§4 below) — deliberately, because the prior-art
verdict must be fixed before the outcome is fetched, not discovered afterwards.

**This brief is blind with respect to exactly one thing: the value of adult annual survival
`phi` for any species in the frame.** No `phi` number has been fetched, and no survival page,
table or file has been opened, at the time of hashing. It is **not** blind with respect to
margins, longevity, or the general background fact that hibernating mammals are long-lived.

## 1. Hypothesis

> **H1.** Among **small (adult mass < 100 g), non-migratory, temperate/boreal (|mid-range
> latitude| >= 35 deg) endotherms**, species with a **metabolic lever** (daily torpor or
> hibernation) have **higher adult annual survival `phi`** than **matched lever-less** species.

**Direction is fixed: lever-bearing > lever-less.** One-sided tests throughout, declared here.

### 1.1 Coding the lever — the asymmetric rule that fixes C40's §5.2 failure

C40 coded lever class from presence in the Ruf & Geiser 2015 appendix and then had to amend the
rule mid-run, with the outcome column already on screen, because **absence from a positive-record
compilation is "not measured", not "no lever".** That amendment is the single most attackable
thing in C40. This brief fixes it in advance with a deliberately **asymmetric** rule:

| code | rule | source requirement |
|---|---|---|
| **lever = 1** | species appears in the **Ruf & Geiser 2015 per-species Appendix** (`10.1111/brv.12137`, open copy PMC4351926, 214 species with `T`, `BM`, `Tb_min`, `TMR_min`, `TMR_rel`, `TBD_max`, `LAT`) | that presence alone is sufficient — it is a positive record |
| **lever = 0** | requires an **explicit negative statement in a second source**: COMBINE (Soria et al. 2021, *Ecology* 102:e03344, `10.1002/ecy.3344`) field `hibernation_torpor` **= 0** in `trait_data_reported.csv`, **or** a named review stating homeothermy for that species | absence from Ruf & Geiser is **never** sufficient |
| **UNCODED** | everything else — absent from Ruf & Geiser **and** carrying no explicit negative | **dropped from every test**, and the count of dropped species is reported |

**Conflicts** (present in Ruf & Geiser **and** COMBINE `hibernation_torpor = 0`) are coded
**UNCODED** and dropped, not resolved in favour of either. The count is reported.

**Sub-class, secondary only:** within lever = 1, `TBD_max >= 24 h` or `TMR_rel <= 0.10` →
hibernator, else daily torpor. Used only for the §4 novelty split, never for H1.

**Coding discipline.** No `phi`, longevity, mortality or population-trend value is admissible
evidence for a lever code. The coding table is written to disk **before** the survival join, in
`vault/_scripts/c52_data/lever_codes.csv`, and the script records that file's sha256 so the
order of operations is checkable after the fact.

## 2. The outcome — `phi`, and the pre-commitment not to substitute longevity

**Outcome: adult annual survival probability `phi`.** NOT maximum longevity. C40's headline was
a longevity proxy and this brief exists partly to stop that recurring.

Sources, tried **in this order**, with the URL and fetch date recorded per species:

1. **BTO BirdFacts** per-species survival pages (`https://www.bto.org/understanding-birds/birdfacts/<slug>`) — real ring-recovery adult annual survival for British birds. Scraped per species; URL cited.
2. **EURING / Robinson et al.** ring-recovery compilations, if a machine-readable table is reachable.
3. **Amniote life-history database** (Myhrvold et al. 2015, *Ecology* 96:3109, `10.1890/15-0846R.1`) — its `adult_survival` field **if that field exists and is populated**; if it does not exist, that is recorded as a negative result, not passed over.
4. **Mammal survival compilations** — Sibly et al., or a "long-term studies" compendium, if reachable.
5. **COMBINE `max_longevity_d`** — permitted **only as an explicitly downgraded fallback**, flagged `PROXY` in every sentence that uses it, and **never** reported as `phi`.

**Pre-committed power gate.** *If no `phi` source yields **n >= 10 lever-less species** in the
frame, the test is reported **DIRECTION ONLY**, with no p-value promoted to a headline and no
substitution of longevity for `phi`.* This gate is the brief's main defence against the C40
failure mode and it is expected, on the evidence of C40 §4, to **fire**.

## 3. Pre-empted confounds, each with its planned control

Each row is an attack from `audits/c43-adversarial.md` transposed onto this design. Each is
**run and reported whether or not it helps.**

| # | attack | planned control | reported as |
|---|---|---|---|
| i | **phylogenetic pseudoreplication** — C40's signal was 25 bats out of 43 lever rows | analyse at **family level** (family-mean `phi`, one row per family) as well as species level; **report with and without Chiroptera** as a pre-declared, not post-hoc, split | both effect sizes, both n |
| ii | **body mass** — survival scales with mass and levers are size-biased | matched pairs **within 2x mass** (abs delta log10 mass <= 0.301); mass also reported as a covariate on the unmatched frame | matched and unmatched |
| iii | **latitude / climate** | frame restricted to abs lat >= 35 deg; pairs matched within **delta lat <= 10 deg** | pair latitude spread |
| iv | **flight** — birds vs mammals differ in `phi` for reasons unrelated to torpor | **stratify**: the bird leg and the mammal leg are computed and reported **separately**; no pooled bird+mammal test is promoted | two legs, never pooled |
| v | **source-study clustering** — C43 died on this | **no two species from the same survival study may appear in the same pair**; the source study is recorded per `phi` value and pairs violating the rule are dropped | count of pairs dropped |
| vi | **migrants** | excluded by the stated rule: any species whose BTO/COMBINE status is obligate long-distance migrant, plus C40's named migratory-bat list. The rule is fixed here and applied blind; **C40's own §6.4 records that this exclusion is expensive and it is accepted again** | count excluded, and the names |
| vii | **effect size, not only p** | headline is a **difference in `phi`** (lever-bearing minus lever-less) with a **bootstrap 95% CI**, seed `20260905`, 10,000 resamples, resampled **over pairs**; the p-value is reported second | delta phi [CI], then p |

**Positive-control check (the C43 clause-3 death).** Before any result is quoted, the script
asserts that the `phi` source and the lever source are **different files with different
provenance**. If any survival number turns out to be derived from a torpor-conditioned model —
e.g. a `phi` imputed from body mass and life-history traits that already include a torpor flag —
that leg is **void by construction** and reported as void, not as a result. COMBINE
`trait_data_imputed.csv` is therefore **forbidden**; only `trait_data_reported.csv` is used.

## 4. Prior-art pre-check — run BEFORE the join, recorded here

Searched 2026-09-05: **Crossref** (`api.crossref.org`, `mailto=deciduusleaf@gmail.com`),
**Europe PMC REST** (bare-quoted, 10 formulations), **WebSearch**. **Semantic Scholar
`graph/v1/paper/search` returned HTTP 429 on every attempt**, the same rate limit
`audits/c43-adversarial.md`, `g34-adversarial.md` and `g36-adversarial.md` hit; the prior-art
leg is therefore Crossref + Europe PMC + web and **does not meet the C5 section-11 bar**. Stated,
not hidden.

**The mammal leg is PRIOR ART, and this is fixed before the outcome is fetched.**

> **Turbill, Bieber & Ruf 2011**, *"Hibernation is associated with increased survival and the
> evolution of slow life histories among mammals"*, *Proc. R. Soc. B* — DOI
> `10.1098/rspb.2011.0190`, **verified against Crossref 2026-09-05** (title, venue,
> authors Turbill/Bieber/Ruf, issued 2011-03-30, `is-referenced-by-count` = **283**).
> Abstract, read 2026-09-05 via Europe PMC `resultType=core` (PMID 21450735): phylogenetically
> informed GLS models; monthly survival higher during hibernation than the active season;
> **"Hibernators also have approximately 15 per cent higher annual survival than similar sized
> non-hibernating species"**; small hibernators have ~50% greater maximum lifespan at 50 g,
> slower reproduction, later maturity, longer generation times.

That is H1, for mammals, on annual survival, with body mass controlled and phylogeny controlled,
published in 2011 with 283 citations. **The mammal leg of H1 is REDISCOVERED. It is not a
finding of this project and this brief forbids it being written as one.** Any mammal number this
run produces is a **replication attempt against a published effect size of ~+15% annual
survival**, and must be labelled so.

Also located and recorded: **Geiser & Turbill 2009**, *Naturwissenschaften*
`10.1007/s00114-009-0583-0` (heterothermy and recent mammalian extinctions — 93.5% of 61
recently extinct mammals homeothermic); Ruf & Geiser 2015 itself, which reviews the longevity
association.

**What is left that is new, declared before running anything:**

- **NEW — the bird leg.** Ten Europe PMC formulations (`"torpor" AND "annual survival" AND "birds"`, `"heterothermy" AND "survival" AND "birds"`, `"torpor" AND "life history" AND "birds"`, `"hummingbird" AND "torpor" AND "survival"`, `"daily torpor" AND "survival"`, `"heterothermy" AND "longevity"`, `"torpor" AND "adult survival"`, `"hibernation" AND "annual survival" AND "comparative"`, `"torpor" AND "slow-fast continuum"`, `"nightjar" AND "torpor" AND "survival"`) plus web search return **no comparative test of adult annual survival in torpid vs non-torpid bird species.** The literature is single-species torpor energetics (superb fairy-wren, torpor-assisted migration, hummingbird adipostats), not a survival comparison.
- **NEW — the cross-taxon comparison.** Whether the lever→survival association has the **same sign and comparable magnitude** in birds as Turbill 2011 reports in mammals. Untested as far as the above searches reach.
- **NEW, weakly — daily torpor as distinct from hibernation.** Turbill 2011's contrast is hibernators vs non-hibernators. Whether **daily heterotherms** separate from strict homeotherms is a different cell; reported only if the sub-class in §1.1 yields n >= 5 per arm.
- **REDISCOVERED — everything else.** The mammal hibernation leg.

**Pre-committed consequence.** If the bird leg cannot be powered (§2's gate fires) and the
mammal leg is prior art, then **the honest result of this run is a null with a named owner**,
and C52 must say so in its callout rather than promoting the mammal replication as a result.

## 5. Statistics and gates

- **Primary:** paired difference in `phi`, lever-bearing minus lever-less, over matched pairs (§3 ii/iii/v). Headline = **mean delta phi with a 10,000-resample bootstrap 95% CI over pairs, seed 20260905**.
- **Secondary:** exact one-sided sign test over non-tied pairs. **Gate: >= 8 non-tied pairs.** Below 8 → direction only, no p promoted.
- **Frame gate (§2): >= 10 lever-less species with `phi`.** Below 10 → **DIRECTION ONLY** for that leg.
- **Family-level rerun** (§3 i) reported alongside every species-level number.
- **Chiroptera-free rerun** reported alongside every mammal number. This is **pre-declared here**, unlike C40 §4 where it was post-hoc.
- A leg that fails a gate is reported as **failed**, with its n. No gate may be relaxed after the outcome is seen; the gates are in this hashed file.

**Pass / fail for H1, per leg:**

- **PASS** — delta phi > 0 with a bootstrap CI excluding 0, >= 8 non-tied pairs, surviving the family-level rerun.
- **DIRECTION ONLY** — delta phi > 0 but a gate fails.
- **FAIL** — delta phi <= 0, or the CI spans 0 with the gates met.
- **VOID** — the positive-control check in §3 fires, or the `phi` source proves torpor-conditioned.

## 6. The falsifier (P-072)

Inherited verbatim from C38 §5 via C40 §5: **one lever-less small endotherm with a published
reserve margin above +100% kills the demand-side reading.** C40's scan returned **zero over a
reach of n = 1** (*Sorex araneus*, −69%) and C40 §5.1 calls that "a formality, not a test".

This run **widens the scan or reports that it could not**: >= 6 search formulations for published
dusk-reserve / overnight-cost or autumn-fat / overwinter-draw pairs in species coded lever = 0
by §1.1's asymmetric rule. **Recorded outcome: the number of lever-less species with a published
margin found, and the number of those exceeding +100%.** A scan that again reaches only one
species is reported as **still a formality**, not as a survived falsifier.

## 7. What would make this brief wrong

- If a comparative torpor-vs-`phi` study **in birds** exists and was missed, the bird leg is rediscovered too and this run has no new leg at all. The search reach in §4 is 10 Europe PMC formulations + web, with Semantic Scholar down; that is the honest bound.
- If the BTO frame contains **fewer than 3 lever-bearing British bird species** — which the coder suspects and states here before looking — the bird leg is unrunnable and §2's gate fires immediately. **That suspicion is recorded in advance so that reporting it later is not a rationalisation.**
