# Scout: ecosystem resilience and disturbance

## Summary (5 lines)

- **Method note first: every number below is OpenAlex server-side citer-set intersection (`works?filter=cites:W_A,cites:W_B`), `mailto=deciduusleaf@gmail.com`, fetched 2026-09-05; `N_A`/`N_B` are OpenAlex `cited_by_count` on the same date; every DOI was resolved through Crossref (`api.crossref.org/works/<doi>`) and three of my first-pass guesses resolved to the *wrong work* and were discarded rather than reported.**
- **Two calibrations were run before any gap was believed.** Holling 1973 x Bruneau 2003 (ecological ↔ engineering resilience) = **1,420** co-citers; Scheffer 2009 x Wissel 1984 (early-warning ↔ characteristic return time) = **321**. The ecology side of this domain is demonstrably *joined* to both engineering-resilience discourse and to bifurcation physics, so a zero here is not an artifact of ecology being un-indexed.
- **The famous bridges are real and I am reporting them as closed, not as finds.** Early-warning signals ↔ bifurcation physics (321), ecological reactivity ↔ hydrodynamic non-normality (**44**), Levins ↔ Kermack-McKendrick (**88**). The brief warned about these; they check out as bridged and are ranked at the bottom.
- **What survives is one theme, three times: ecology quantifies disturbance with a *mean* where reliability quantifies it with a *hazard shape*.** Weibull 1951 x ecological recovery = **0** (E = 132 concept-scoped); fire-return interval x age-replacement policy = **0** (E = 20.3); early-warning signals x industrial prognostics/RUL = **2** and x bearing condition monitoring = **0** (E = 670 / 853). All three extend **C18** and the third also extends **C17**.
- **The weakest link in this scout is `N_universe`, not the counts.** Two otherwise attractive candidates (reactivity x Bode design tradeoffs; MVP x redundancy allocation) survive only at the union floor and go to `E < 1` or `E ~ 3` at a fetched concept scope, so per `citation-intersection` their zeros are not quotable findings. I have marked them **not informative** rather than ranking them on the floor.

## Ranked candidates

Endpoint for every intersection: `https://api.openalex.org/works?filter=cites:<W_A>,cites:<W_B>&per-page=25&mailto=deciduusleaf@gmail.com`, **fetched 2026-09-05**.
`E floor` = `N_A*N_B/(N_A+N_B-O)` (union floor, flatters the gap, never quotable alone). `E scoped` uses a fetched OpenAlex concept-union `N` (filter given per candidate). `CR` = control ratio against the Scheffer x Wissel control, denominator-invariant: `(O/N_B)_gap / (321/441)`.

| rank | A ↔ B | anchors (DOI, Crossref-verified) | N_A / N_B / O | E floor / scoped | informative? (E>1) | bridge? | cost to close | extends |
|---|---|---|---|---|---|---|---|---|
| **1** | Early-warning signals ↔ industrial prognostics / remaining useful life | Scheffer 2009 `10.1038/nature08227` ↔ Si 2011 `10.1016/j.ejor.2010.11.018` | 4,891 / 2,098 / **2** | 1,469 / **670** | **yes, decisively** | 2 hits, both real but isolated | 1 desk session | C18, C17 |
| **1b** | same, second B anchor (vibration condition monitoring) | Scheffer 2009 ↔ Randall & Antoni 2011 `10.1016/j.ymssp.2010.07.017` | 4,891 / 2,670 / **0** | 1,727 / **853** | **yes** | none | — | C18, C17 |
| **2** | Weibull hazard shape beta ↔ ecological recovery / return-time distributions | Weibull 1951 `10.1115/1.4010337` ↔ Hillebrand & Kunze 2020 `10.1111/ele.13457` | 11,512 / 173 / **0** | 170 / **132** | **yes** | none | 1 desk session | C18 |
| **2b** | same, second ecology anchor | Weibull 1951 ↔ Neubert & Caswell 1997 `10.1890/0012-9658(1997)078[0653:ATRFMT]2.0.CO;2` | 11,512 / 497 / **0** | 476 / — | yes (floor only) | none | — | C18 |
| **3** | Fire-return interval ↔ age-replacement / preventive-maintenance interval | Johnson & Gutsell 1994 `10.1016/S0065-2504(08)60216-0` ↔ Barlow & Hunter 1960 `10.1287/opre.8.1.90` | 419 / 1,368 / **0** | 321 / **20.3** | **yes** | none | 1-2 desk sessions | C18 |
| **4** | Extinction time as first passage ↔ actuarial ruin theory | Lande 1993 `10.1086/285580` ↔ Gerber & Shiu 1998 `10.1080/10920277.1998.10595671` | 2,179 / 797 / **0** | 584 / **371** | **yes** | none | 2 sessions | C18, C25 |
| **5** | Odum subsidy-stress gradient ↔ hormesis ZED window | Odum, Finn & Franz 1979 `10.2307/1307690` ↔ Calabrese & Baldwin 2003 `10.1146/annurev.pharmtox.43.100901.140223` | 546 / 785 / **0** | 322 / **7.1** | yes, but marginal | 0 here; **2** and **1** against alternate hormesis anchors, all genuine | 1 session | C19, G23 |
| **6** | Extinction debt ↔ cumulative-damage / committed-failure accounting | Tilman 1994 `10.1038/371065a0` ↔ Miner 1945 `10.1115/1.4009458` | 2,808 / 6,326 / **0** | 1,945 / **418** | **yes** | none | 2 sessions | C18 |
| **7** | Ecological reactivity / resilience trade-off ↔ Bode-RHP design tradeoffs | Neubert & Caswell 1997 (above) ↔ Freudenberg & Looze 1985 `10.1109/tac.1985.1104004` | 497 / 638 / **0** | 279 / **0.35** | **NO at concept scope** | none | 1 session, but null model is void | C17 |
| **8** | Regime-shift hysteresis ↔ Schmitt-trigger noise margin | Scheffer 2001 `10.1038/35098000` ↔ Schmitt 1938 `10.1088/0950-7671/15/1/305` | 7,476 / 219 / **1** | 213 / — | floor only | 1 hit, genuine (army-ant construction) | 1 session | G4, M2 |
| **9** | Minimum viable population ↔ redundancy allocation / k-out-of-n | Traill 2007 `10.1016/j.biocon.2007.06.011` ↔ Coit & Smith 1996 `10.1109/24.510811` | 456 / 758 / **0** | 285 / **2.95** | marginal | none | 2 sessions | — |
| **10** | Metapopulation capacity ↔ epidemic threshold (leading eigenvalue) | Hanski & Ovaskainen 2000 `10.1038/35008063` ↔ Pastor-Satorras & Vespignani 2001 `10.1103/PhysRevLett.86.3200` | 1,160 / 5,839 / **11** | 969 / **241** | yes | **11 hits, several real** | — | — |
| ctrl | Neubert & Caswell ↔ Trefethen 1993 `10.1126/science.261.5121.578` | non-normality | 497 / 1,825 / **44** | 398 / — | — | **bridged** | — | — |
| ctrl | Levins 1969 `10.1093/besa/15.3.237` ↔ Kermack & McKendrick 1927 `10.1098/rspa.1927.0118` | | 3,477 / 12,128 / **88** | 2,718 / 1,485 | — | **bridged** | — | — |
| ctrl | Scheffer 2009 ↔ Wissel 1984 `10.1007/bf00384470` | | 4,891 / 441 / **321** | 430 / **254** (O/E = 1.26) | — | **closed** | — | — |
| ctrl | Holling 1973 `10.1146/annurev.es.04.110173.000245` ↔ Bruneau 2003 `10.1193/1.1623497` | | 18,334 / 5,408 / **1,420** | 4,442 / **126** (O/E = 11.3) | — | **closed** | — | — |

Control ratios (vs Scheffer x Wissel): rank 1 = **0.0013**, 1b = 0, 2 = 0, 3 = 0, 4 = 0, 5 = 0, 6 = 0, 7 = 0, 8 = 0.0063, 9 = 0, 10 = 0.0026. Against the Holling x Bruneau control the ratios are ~2.8x larger and the ordering is unchanged.

## Per-candidate detail

### 1 / 1b - Early-warning signals ↔ industrial prognostics and condition monitoring

**Same object.** Both fields estimate *how close a system is to an irreversible transition, from a noisy time series, before it happens*: ecology reads rising lag-1 autocorrelation and variance as the leading eigenvalue approaches zero; prognostics/PHM reads a degradation-signal drift-plus-diffusion model to a failure threshold and reports remaining useful life with a confidence band. The estimand in both cases is a first-passage distribution to a threshold, and both fields use the same statistic family (variance and kurtosis of a residual).

**Metaphor risk, strongest form.** EWS assume the transition is a *bifurcation of the system's own dynamics* - the loss of stability is endogenous. PHM assumes a monotone exogenous damage state with the dynamics fixed. If an ecological transition is noise-induced rather than bifurcation-induced there is no eigenvalue for PHM machinery to track, and conversely a bearing has no alternative stable state to shift to. The bridge could be nothing more than "both do change-point detection".

**Counts.** O = **2** against Si 2011, **0** against Randall & Antoni 2011. Concept-scoped `N` = 15,304 from `works?filter=concepts.id:C114725131|C129364497,from_publication_date:2011-01-01` (Tipping point union Prognostics), giving E = 670 and 853 - the largest informative expectations in this scout. Informative at 10x N as well (E = 67, 85).

**Hits inspected (2 of 2).** *System reliability and system resilience* (2021) and *Physics-Based Landau-Ginzburg Features for Survival Prognostics* (2026). Both are genuine bridges - and that is the point: the entire crossing is **two papers wide** against an expectation of ~670, and one of the two is from this year.

**What would close it.** The missing object is **the hazard function `h(t)` implied by an early-warning indicator** - convert a published EWS time series into a PHM-style RUL distribution, then fit its Weibull beta. Computable from already-published numbers: the Dakos/Scheffer EWS benchmark series (public), plus any published lake or reef regime-shift series with a dated transition, run through the standard Wiener-process-to-threshold RUL estimator in Si 2011. **~4-6 hours.** Deliverable: does an approaching ecological bifurcation produce beta = 1 (memoryless) or beta > 1 (wear-out)? C18 predicts beta > 1 for a bifurcation and beta ~ 1 for a noise-induced shift, which is a **discriminator ecology currently has no instrument for.**

**Extends.** `C18-durability-axis` (beta as the shared coordinate) and `C17-offset-from-threshold` (the EWS indicator *is* the offset, and the gain x bandwidth conservation predicts the variance-vs-warning-time trade-off). `extends-to: [ecology, conservation]`.

### 2 / 2b - Weibull hazard shape ↔ ecological recovery / return time

**Same object.** Both sides estimate the distribution of a time-to-event under stress: reliability reports shape and scale for time-to-failure; disturbance ecology reports a *mean* recovery time or a single exponential recovery rate for time-to-return. C18 already established that the mean hides the failure law and that beta separates it - ecology is in exactly the position C18 diagnosed for the enzyme side (means published, distributions not).

**Metaphor risk.** Recovery is the *reverse* direction from failure. A Weibull fit to recovery times describes an assembly process (colonisation, regrowth), not a degradation process, so "increasing hazard" would mean "recovery becomes more likely the longer you wait" - arguably a re-parameterised logistic and not a hazard at all. If ecological recovery times are lognormal because they are products of rates, beta carries no mechanism.

**Counts.** 0 against both ecology anchors. Concept-scoped `N` = 15,057 from `works?filter=concepts.id:C173291955|C2779720641,from_publication_date:2020-01-01` (Weibull distribution union Ecological resilience) -> E = 132. Informative; still E = 13 at 10x N.

**Hits.** None to inspect.

**What would close it.** The missing object is **a fitted beta for ecological recovery-time data**, computed from Hillebrand & Kunze 2020's own supplementary recovery-duration table (open data, `10.1111/ele.13457`) plus one or two long-term restoration datasets. **~3-4 hours** for the fit; the finding is C18's asymmetry transplanted - ecology reports the mean, reliability reports the distribution. **~5-6 hours** if a second dataset class (coral bleaching recovery) is added.

**Extends.** `C18-durability-axis`, directly and with no new machinery. `extends-to: [ecology, conservation, sustainability]`.

### 3 - Fire-return interval ↔ age-replacement / preventive-maintenance interval

**Same object.** Fire ecology fits a Weibull hazard to time-since-last-fire and asks when the system is "due"; reliability's age-replacement policy fits a Weibull hazard to time-since-last-replacement and *solves for the optimal intervention interval* by minimising the cost rate `C(T) = [c_p R(T) + c_f F(T)] / integral_0^T R(t) dt`. Fire ecology has the hazard and the cost asymmetry (prescribed burn cheap, wildfire expensive) but does not write down the optimisation. Barlow & Hunter wrote it down in 1960.

**Metaphor risk.** Age replacement assumes renewal - the unit is restored to as-good-as-new and the clock resets. A landscape after fire is not as-good-as-new (fuel structure, seedbank age and species composition carry state forward), so the renewal-reward argument that makes the Barlow-Hunter integral valid may simply fail, leaving a formula without a theorem.

**Counts.** O = **0**. Concept-scoped `N` = 28,274 from `works?filter=concepts.id:C195330766|C24090081,from_publication_date:1994-01-01` (Fire ecology union Preventive maintenance) -> E = 20.3. Informative, though an order of magnitude weaker than rank 1, and it would fail at 10x N. Cross-check run: Weibull 1951 x Johnson & Gutsell 1994 = **1** (a 1998 dendroecology fire-history paper), so fire ecology *does* touch Weibull - it just does not touch maintenance theory.

**What would close it.** The missing object is **the cost-optimal prescribed-burn interval T\* derived from published fire-interval Weibull fits**, using Barlow-Hunter's age-replacement cost rate with the cost ratio taken from published prescribed-burn vs suppression figures. Inputs: Johnson & Gutsell's tabulated shape and scale parameters for named boreal and chaparral stands, plus agency cost-per-hectare figures. **~6 hours**, and the output is a number a fire manager could argue with - a genuine Layer-3 prediction.

**Extends.** `C18-durability-axis`. `extends-to: [ecology, conservation, sustainability]`.

### 4 - Extinction time ↔ actuarial ruin theory

**Same object.** Population viability analysis computes the probability that a stochastic process hits an absorbing barrier (N = 0) within a horizon; ruin theory computes the probability that a stochastic surplus process hits an absorbing barrier (U = 0), and has a century of results on exactly the case ecology finds hard - **heavy-tailed catastrophes**, where the ruin probability is dominated by one large claim rather than by diffusion.

**Metaphor risk.** Lande's diffusion approximation already *is* first-passage theory; the risk is that ruin theory adds only vocabulary, since both reduce to the same Kolmogorov backward equation. The transfer is non-trivial only if the catastrophe distribution is subexponential, which is an empirical question about catastrophe magnitudes that ecology may not have the data to answer.

**Counts.** O = **0**. Concept-scoped `N` = 4,678 from `works?filter=concepts.id:C116607704|C29859451,from_publication_date:1998-01-01` (Population viability analysis union Ruin theory) -> E = 371. Strongly informative, and still E = 37 at 10x N. Caveat: this scope is narrow by construction and both concepts are small, so the fetched N may be under-inclusive of the works that could have cited both.

**What would close it.** The missing object is **the subexponential ruin asymptotic applied to a published catastrophe-magnitude distribution**: the integrated-tail approximation makes extinction probability tail-dominated, which *contradicts* the Gaussian-catastrophe intuition built into standard PVA software. Computed from Lande's own catastrophe frequency and magnitude parameters plus a published catastrophe-size dataset. **~8 hours**; higher risk than ranks 1-3 because it needs a real tail fit.

**Extends.** `C18-durability-axis` (both are first-passage) and, loosely, `C25-whittle-foraging`'s indexability machinery. `extends-to: [conservation, ecology]`.

### 5 - Odum's subsidy-stress gradient ↔ hormesis

**Same object.** Both are the *same biphasic dose-response curve*: a low dose of a perturbation raises the response above baseline, a high dose depresses it below, and both fields care about the crossover dose and the width of the stimulatory window. Odum named it in 1979 for ecosystems; toxicology named it hormesis and parameterised it (~30-60% ceiling, 10-20x window width), which is exactly the numeric asset G23/C19 has been chasing.

**Metaphor risk, and it is serious here.** Odum's subsidy limb is *energetic* - an input that would otherwise cost the system energy is being used as a resource, so the stimulation is real work done. Hormesis's stimulatory limb is a *regulatory overshoot* of a repair response. Same curve shape, arguably different generating mechanism - and C19 already found the fitted constants to be response-axis-specific, so a shared window width may not exist even in principle.

**Counts.** Odum x Calabrese & Baldwin 2003 = **0**; Odum x Stebbing 1982 (`10.1016/0048-9697(82)90066-3`, N_B = 721) = **2**; Odum x Calabrese & Baldwin 2002 *Defining hormesis* (`10.1191/0960327102ht217oa`, N_B = 741) = **1**. Concept-scoped `N` = 60,008 from `works?filter=concepts.id:C186256576|C115346097,from_publication_date:1982-01-01` (Hormesis union Ecotoxicology) -> E = 6.6-7.1. Informative, but the thinnest margin among the ranked candidates and it fails at 10x N.

**Hits inspected (3 of 3).** *Hormesis - Its Relevance in Phytotoxicology* (2009), *Stimulatory Responses, Hormesis, and Essentiality, in Ecotoxicology* (2013), *The Microbiome Stress Project* (2019). All three are **real bridges** - the crossing exists, at three papers, all on the ecotoxicology side and none at the ecosystem scale Odum wrote for. **That is the honest form of this candidate: not "no one has crossed" but "the crossing exists only below the ecosystem scale".**

**What would close it.** The missing object is **the ecosystem-scale ZED window width**, fitted to a published subsidy-stress dose sweep (nutrient-loading and thermal-effluent gradients have the sweeps) and compared against toxicology's 10-20x. This is exactly the fit C19 did for shot peening, on a third response class. **~5 hours.**

**Extends.** `C19-hormesis-biphasic-fit`, `G23-hormesis-formalism`, `M2-use-the-noise`. `extends-to: [ecology, sustainability]`.

### 6 - Extinction debt ↔ cumulative-damage / committed-failure accounting

**Same object.** Both name a system that has already accumulated enough damage to fail but has not yet failed, and both want the *lag* between the committing event and the realised loss. Miner's rule sums fractional damage and calls failure at 1; extinction debt sums habitat loss and calls the species committed at a threshold, with relaxation time as the lag.

**Metaphor risk, the strongest of the ranked set.** Miner's rule is a *linear damage summation with no state dynamics and no recovery*; extinction debt is a *relaxation to a new equilibrium* governed by demographic rates, and the lag is a property of the post-perturbation dynamics, not of the damage accounting. The shared idea is "already committed"; the mathematics are a sum versus an eigenvalue. This is the candidate I most expect to fail a full-text read.

**Counts.** O = **0**, E floor 1,945, concept-scoped `N` = 42,530 from `works?filter=concepts.id:C51916926|C173291955,from_publication_date:1994-01-01` -> E = 418. Numerically the second-strongest zero here, which is precisely why the same-object argument must be attacked before any effort goes in. Note also `failure-modes` mode 1: "Miner's rule" is the apostrophe specimen, so any string-side follow-up must use "Palmgren-Miner".

**What would close it.** Relaxation half-life against habitat-loss fraction, fitted from published extinction-debt datasets and tested against a linear-damage-accumulation prediction. A **falsification** of the Miner analogy would be as useful as a confirmation. **~6 hours.**

**Extends.** `C18-durability-axis`. `extends-to: [conservation, ecology]`.

### 7 - Ecological reactivity ↔ Bode / right-half-plane design tradeoffs

**Same object.** C17's finding is that gain x bandwidth is conserved along the offset axis; control theory's statement of the same conservation is the Bode sensitivity integral and the RHP pole/zero tradeoffs Freudenberg & Looze catalogued. Neubert & Caswell's reactivity is the ecological measurement of transient amplification - the numerator of exactly that trade-off - and ecology's resistance-vs-recovery-rate trade-off is a waterbed effect written without the integral.

**Why it is ranked 7 despite being the most elegant C17 extension.** O = **0**, but the concept-scoped `N` = 907,956 (`concepts.id:C2779720641|C133731056`, Ecological resilience union Control engineering) gives **E = 0.35 < 1**, so per `citation-intersection` **the zero is not a finding**. Control engineering has no scope small enough to contain this pair. Worse, the positive control on the same ecology anchor - Neubert & Caswell x Trefethen 1993 = **44**, with hits including *Spectra and Pseudospectra*, *Structure and dynamical behavior of non-normal networks* and *Transient dynamics and pattern formation: reactivity is necessary for Turing instabilities* - shows ecology *does* read non-normality theory. The gap, if real, is narrower than "ecology has not met control theory": it is "ecology has met pseudospectra but not the conservation law".

**What would close it.** Compute the Bode sensitivity integral for a published community matrix and check whether ecological resistance/recovery trade-offs obey it. Attractive, but **do not open until a defensible N exists** - a narrower fetched scope, or a claim resting on the control ratio alone.

**Extends.** `C17-offset-from-threshold`. `extends-to: [ecology]`.

### 8 - Regime-shift hysteresis ↔ Schmitt-trigger noise margin

**Same object.** Both concern a bistable element with a *finite* hysteresis width, so that noise near the switching point cannot cause chattering; ecology calls the width the distance between the two fold bifurcations, electronics calls it the noise margin, and both trade width against responsiveness.

**Metaphor risk.** Schmitt's hysteresis width is a *chosen design parameter*; an ecosystem's is an emergent consequence of its feedbacks, and nothing selected it. Without a selection argument the shared quantity is a coincidence of shape - which is exactly what a `crosses: metaphor` rank means.

**Counts.** O = **1**: *Hysteresis stabilizes dynamic control of self-assembled army ant constructions* (2022), a genuine bridge, and notably a biology paper reaching into electronics rather than the reverse - the `one-way-borrowing` signature. E floor 213; **no defensible concept-scoped N was obtainable**, because Schmitt 1938's OpenAlex concepts are junk ("Simple (philosophy)", "Cathode", "Thermionic emission"). This row therefore rests on the union floor only and I am not quoting it as a finding.

**Extends.** `G4-criticality-as-design`, `M2-use-the-noise`. `extends-to: [ecology]`.

### 9 - Minimum viable population ↔ redundancy allocation / k-out-of-n

**Same object, weakly.** Both ask how many nominally interchangeable units are needed for a system to survive stochastic unit loss at a target probability over a horizon.

**Metaphor risk, probably fatal.** k-out-of-n units fail *independently*; populations fail through *correlated* environmental stochasticity, inbreeding depression and Allee effects, which is why MVP estimates are large and variable. Reliability's common-cause-failure literature is the honest counterpart, not plain redundancy allocation - and that needs a different B anchor before this is worth re-measuring.

**Counts.** O = 0, but concept-scoped `N` = 117,085 (`concepts.id:C116607704|C152124472,from_publication_date:1996-01-01`) -> **E = 2.95**, barely informative and gone at 10x N. Do not quote.

**Extends.** `extends-to: [conservation]`. Low priority.

### 10 - Metapopulation capacity ↔ epidemic threshold

**Same object, and largely already bridged - reported as a negative result.** Metapopulation capacity is the leading eigenvalue of a landscape connectivity matrix; the epidemic threshold is the leading eigenvalue of a contact matrix - one theorem. Hanski & Ovaskainen x Pastor-Satorras = **11** (E scoped 241) with real hits: *Metapopulation dynamics as a contact process on a graph* (2004), *Extinction thresholds: insights from simple models* (2003), *Rendezvous effects in the diffusion process on bipartite metapopulation networks* (2011); inspected 6 of 11. The classical pair Levins 1969 x Kermack-McKendrick 1927 = **88**, and Hanski & Ovaskainen x Kermack-McKendrick = 5. **Report as bridged.** The residual - that ecology has not imported the result that the threshold *vanishes* for a divergent-variance degree distribution - is a narrow reading claim, not a citation gap, and this scout's instrument cannot support it.

## Recommendation: which 2 to open first, and why

**Open rank 1 (early-warning signals ↔ prognostics/RUL) and rank 2 (Weibull beta ↔ ecological recovery-time distributions), in that order.**

1. **They are the same instrument, twice.** Both ask ecology to publish a *distribution* where it currently publishes a *mean* - C18's central finding transplanted into the owner's own field. Doing rank 1 produces the hazard function that rank 2 then fits beta to, so the second costs well under half its standalone estimate if the first is done first. Rank 3 (fire-return interval x age-replacement) rides on the same fitted beta and is the natural third.
2. **Rank 1 has the best-conditioned null model in the scout and the best positive controls.** E = 670 concept-scoped with O = 2, still informative at 10x N, and the two flanking controls (Scheffer x Wissel = 321, Holling x Bruneau = 1,420) prove the low count is not an indexing artifact of the ecology side. Control ratio 0.0013 - roughly three orders of magnitude below a joined literature.
3. **Both are one desk session on public data and both emit a falsifiable number.** Rank 1's discriminator (beta > 1 for a bifurcation-driven shift versus beta ~ 1 for a noise-induced one) is a Layer-3 prediction ecology has no existing instrument to make; rank 2's beta fit on open supplementary data is a Layer-2 computation with no data-access risk. Per `audits/05`, C18 was already the highest EV/cost item in the vault and was parked - this gives it an ecology-facing target rather than a second engineering one.

**Do not open rank 7 (reactivity ↔ Bode) yet**, despite it being the most elegant extension of C17: its concept-scoped E is 0.35, so its zero currently means nothing, and its own positive control (44 against Trefethen) shows the neighbouring bridge is already built. **Do not open rank 6 (extinction debt ↔ Miner) on the strength of its large E** - attack the same-object argument first; I expect it to fail.

**Suggested `extends-to` values, per the closed vocabulary in `vault/_templates/gap.md` (astrobiology | ecology | circularity | conservation | sustainability | none):** rank 1 `[ecology, conservation]`, 2 `[ecology, conservation, sustainability]`, 3 `[ecology, conservation, sustainability]`, 4 `[conservation, ecology]`, 5 `[ecology, sustainability]`, 6 `[conservation, ecology]`, 7 `[ecology]`, 8 `[ecology]`, 9 `[conservation]`.

## Provenance

- Provider: **OpenAlex**, polite pool, `mailto=deciduusleaf@gmail.com`. Intersection endpoint `https://api.openalex.org/works?filter=cites:<W_A>,cites:<W_B>&per-page=25`. Citer counts are `cited_by_count` from `https://api.openalex.org/works/doi:<doi>`. Concept-scoped `N` from `https://api.openalex.org/works?filter=concepts.id:<a>|<b>,from_publication_date:<yyyy-mm-dd>` -> `meta.count`. Concept ids from `https://api.openalex.org/concepts?search=<term>`.
- DOI verification: **Crossref**, `https://api.crossref.org/works/<doi>?mailto=deciduusleaf@gmail.com`; title, year, container and `is-referenced-by-count` read from `message`.
- **All fetches 2026-09-05.** Coverage basis: OpenAlex-indexed works only; no reference lists were pulled, so coverage is 100% of what OpenAlex indexes (the citer-set method in `citation-sources.md`), not the 28% reference-list coverage that capped G25.
- **Discarded, not reported:** three candidate B anchors whose DOIs resolved to the wrong work (`10.1109/PROC.1983.12801` -> "An improved conference circuit"; `10.1109/TAC.1985.1103980` -> "Model reduction: Identifying partitions for structured aggregates"; `10.1016/j.ress.2003.09.006` -> an HRA paper, not an engineering-resilience anchor). The first two were replaced by title search; the third was replaced by Bruneau 2003.
- **Not done, and it matters:** `failure-modes` mode 6 (diachronic terminology drift) has **not** been run on any of these. Several windows are 30-60 years wide (Weibull 1951, Barlow & Hunter 1960, Miner 1945, Schmitt 1938), and a citer-set intersection anchored on a 1940s-60s paper measures traffic between named papers, not whether the object travelled under a later name. Before any of these zeros is written into a gap note, the per-decade re-run that `failure-modes` requires must happen - this scout produces leads at `evidence: citation-intersection`, not standings.
