# Scout: conservation genetics and population viability

## Summary (5 lines)

- **Instrument and provenance, first.** Every intersection below is an **OpenCitations** citer-set intersection, endpoint `https://api.opencitations.net/index/v1/citations/<doi>`, User-Agent `biomimicry/1.0 (mailto:deciduusleaf@gmail.com)`, **fetched 2026-09-05**; `N_A`/`N_B` are counted citer-DOI sets from the same fetch, not `cited_by_count`. Every DOI was resolved through **Crossref** (`api.crossref.org/works/<doi>?mailto=deciduusleaf@gmail.com`, same date) and **two first-pass anchor guesses resolved to the wrong work and were discarded, not reported** (`10.1093/oxfordjournals.jhered.a111612` -> *RAPDSIM*, not the mutational meltdown; `10.1111/j.1523-1739.1996.10041500.x` -> 404). One further anchor, Kuo & Wan 2007 `10.1109/tsmca.2007.897598`, returned an **empty citer set** from OpenCitations and its two rows are void, not zeros.
- **A method bug found and fixed mid-run, which the vault should adopt.** OpenCitations' `/citations/` payload contains records with an **empty `citing` field**. Naively de-duplicating `x["citing"]` adds a phantom `""` element to every citer set, which inflates `N_A`, `N_B` **and every intersection by exactly 1**. My first pass reported five "1-hit" candidates that are in fact clean zeros. `vault/_scripts/intersect.py` builds its set the same way and should filter empty strings. **All numbers in this report are post-fix.**
- **`N_universe` is a union floor throughout, and is quotable only as a floor.** OpenAlex was budget-locked to one probe, and a single probe cannot buy both a concept id and a scoped count; I spent zero probes rather than half-buy one. **Every `E` below is `N_A*N_B/(N_A+N_B-O)`, the smallest defensible denominator, which flatters the gap.** Per `citation-intersection`, no zero here is a finding until a concept-scoped `N` is fetched and the sensitivity run at 10x. This is the weakest link in the scout and it is the same weakness `scout-01` carried.
- **Four positive controls fired, on both sides of the top candidate.** In-domain conservation genetics: Frankham 1995 x Charlesworth 2009 = **135**, Lande 1993 x Shaffer 1981 = **146**, Lynch 1995 x Charlesworth 2009 = **39**. In-domain semiconductor yield: Murphy 1964 x Stapper 1983 = **42**, Murphy 1964 x Cunningham 1990 = **52**. In-domain adaptive management: Walters & Holling 1990 x Williams 2011 = **64**; in-domain reliability: Duane 1964 x Barlow & Hunter 1960 = **13**. **Both literatures in every ranked candidate are demonstrably findable and internally joined**, so the zeros are not indexing artifacts.
- **The brief's warning was correct and I am reporting both famous pairs as closed, not as finds.** Bet-hedging x Kelly (Cohen 1966 x Kelly 1956) = **25**, all inspected hits genuine. Portfolio effect x Markowitz (Schindler 2010 x Markowitz 1952) = **22**, genuine. **What survives is a different shape entirely: conservation genetics writes down an *exponential survival law over independently-acting defects* and a *learning curve*, and both of those objects were parameterised by manufacturing engineering decades ago under names the genetics literature has never cited.**

## Ranked candidates

`E floor` = `N_A*N_B/(N_A+N_B-O)`, **a floor, never quotable alone**. `CR` = control ratio, denominator-invariant, computed against a **shared-anchor** control per `citation-intersection`: `(O_gap/N_B_gap)/(O_ctrl/N_B_ctrl)`. All fetches **OpenCitations, 2026-09-05**.

| # | A ↔ B | anchors (Crossref-verified 2026-09-05) | N_A / N_B / **O** | E floor | CR | same-object strength | extends | cost |
|---|---|---|---|---|---|---|---|---|
| **1** | Genetic load / Haldane–Muller principle ↔ Poisson defect-density yield model | Lynch, Conery & Bürger 1995 `10.1086/285812` ↔ Murphy 1964 `10.1109/proc.1964.3442` | 872 / 318 / **0** | **233** | **0** (ctrl 39/1596) | **exact algebraic identity** | new; C6/C19 mould | 6–8 h |
| 1b–1l | same, **12 pairings across 5 decades of A-vocabulary x 3 of B-vocabulary** | Kimura 1963 `10.1093/genetics/48.10.1303`, Lynch 1995, Agrawal & Whitlock 2012 `10.1146/annurev-ecolsys-110411-160257`, Kyriazis 2021 `10.1002/evl3.209`, Bertorelle 2022 `10.1038/s41576-022-00448-x` x Murphy 1964, Stapper 1983 `10.1147/rd.276.0549`, Cunningham 1990 `10.1109/66.53188` | — / — / **0 in all 12** | 113–233 | 0 | — | — | — |
| **2** | Adaptive management ↔ reliability growth (Duane learning curve) | Walters & Holling 1990 `10.2307/1938620` ↔ Duane 1964 `10.1109/ta.1964.4319640` | 996 / 500 / **0** | **333** | **0** (ctrl 64/569) | strong | C18, G29 | 6 h |
| 2b | same, modern A anchor | Williams 2011 `10.1016/j.jenvman.2010.10.041` ↔ Duane 1964 | 569 / 500 / **0** | 266 | 0 | — | — | — |
| **3** | Genetic rescue / translocation timing ↔ sequential analysis and optimal stopping | Whiteley 2015 `10.1016/j.tree.2014.10.009` ↔ Wald 1945 `10.1214/aoms/1177731118` | 762 / 1,517 / **0** | **507** | 0 | good, some metaphor risk | C25, G28 | 5–8 h |
| 3b–3d | same, 3 further pairings | Tallmon 2004 `10.1016/j.tree.2004.07.003`, Seddon 2014 `10.1126/science.1251818` x Wald 1945, Ferguson 1989 `10.1214/ss/1177012493` | — / — / **0 x3** | 241–472 | 0 | — | — | — |
| **4** | PVA planning horizon ↔ age-replacement / preventive-maintenance interval | Boyce 1992 `10.1146/annurev.es.23.110192.002405` ↔ Barlow & Hunter 1960 `10.1287/opre.8.1.90` | 757 / 1,131 / **0** | **454** | 0 | weak — see objection | C18 | 6 h |
| **5** | Minimum viable population ↔ k-out-of-n redundancy allocation | Shaffer 1981 `10.2307/1308256` ↔ Coit & Smith 1996 `10.1109/24.510811` | 1,385 / 600 / **0** | **419** | 0 | weak (independence) | — | — |
| **6** | Metapopulation capacity ↔ redundancy allocation | Hanski & Ovaskainen 2000 `10.1038/35008063` ↔ Coit & Smith 1996 | 931 / 600 / **0** | **365** | 0 | weak | — | — |
| **7** | Seed banks / germination fraction ↔ multi-echelon inventory theory | Cohen 1966 `10.1016/0022-5193(66)90188-3` ↔ Clark & Scarf 1960 `10.1287/mnsc.6.4.475` | 1,135 / 1,181 / **0** | **579** | 0 (ctrl 25/1120) | moderate | C25, G28 | 5 h |
| 7b–7c | same, seed-ecology A anchors | Venable 2007 `10.1890/06-1495`, Long 2014 `10.1111/brv.12095` x Clark & Scarf 1960 | — / — / **0 x2** | 312–324 | 0 | — | — | — |
| **8** | Demographic stochasticity near extinction ↔ heavy-traffic queueing | Lande 1993 `10.1086/285580` ↔ Kingman 1961 `10.1017/s0305004100036094` | 1,767 / 339 / **0** | **284** | 0 (ctrl 146/1385) | moderate | C18, G32 | 8 h |
| 8b–8c | same | Charlesworth 2009 `10.1038/nrg2526`, Shaffer 1981 x Kingman 1961 | — / — / **0 x2** | 272–280 | 0 | — | — | — |
| **9** | Mutational meltdown / error threshold ↔ error-correcting codes | Lynch 1995 ↔ Hamming 1950 `10.1002/j.1538-7305.1950.tb00463.x` | 872 / 4,141 / **0** | **720** | 0 | **weakest** — see objection | **G25** | — |
| 9b–9c | same | Lynch 1995 x Gallager 1962 `10.1109/TIT.1962.1057683`; Charlesworth 2009 x Hamming 1950 | — / — / **0 x2** | 750 / **1,152** | 0 | — | G25 | — |
| **10** | Effective population size `Ne` ↔ survey design effect / effective sample size | Charlesworth 2009 ↔ Kish 1957 `10.2307/2088852` | 1,596 / 46 / **0** | **44.7** | 0 | good, but null model too thin | — | — |
| 10b | same | Frankham 1995 `10.1017/S0016672300034455` x Kish 1957 | 1,312 / 46 / **0** | 44.4 | 0 | — | — | — |
| ctrl | Frankham 1995 x Charlesworth 2009 | in-domain, conservation genetics | 1,312 / 1,596 / **135** | 755 | — | — | — | — |
| ctrl | Lande 1993 x Shaffer 1981 | in-domain, PVA | 1,767 / 1,385 / **146** | 814 | — | — | — | — |
| ctrl | Lynch 1995 x Charlesworth 2009 | in-domain, load x Ne | 872 / 1,596 / **39** | 573 | — | — | — | — |
| ctrl | Murphy 1964 x Stapper 1983 | in-domain, IC yield | 318 / 238 / **42** | 147 | — | — | — | — |
| ctrl | Murphy 1964 x Cunningham 1990 | in-domain, IC yield | 318 / 277 / **52** | 162 | — | — | — | — |
| ctrl | Walters & Holling 1990 x Williams 2011 | in-domain, adaptive mgmt | 996 / 569 / **64** | 378 | — | — | — | — |
| ctrl | Duane 1964 x Barlow & Hunter 1960 | in-domain, reliability/OR | 500 / 1,131 / **13** | 350 | — | — | — | — |
| ctrl | Coit & Smith 1996 x Barlow & Hunter 1960 | in-domain, reliability/OR | 600 / 1,131 / **5** | 393 | — | — | — | — |
| **rej** | Bet-hedging ↔ Kelly criterion | Cohen 1966 x Kelly 1956 `10.1002/j.1538-7305.1956.tb03809.x` | 1,135 / 1,120 / **25** | 570 | — | **BRIDGED** | — | — |
| **rej** | Portfolio effect ↔ Markowitz | Schindler 2010 `10.1038/nature09060` x Markowitz 1952 `10.1111/j.1540-6261.1952.tb01525.x` | 1,401 / 5,375 / **22** | 1,115 | — | **BRIDGED** | — | — |

**Every ranked control ratio is exactly 0**, because every gap intersection is 0. The control ratio therefore carries no ordering information in this scout and **the ranking rests on the same-object argument and the E floor, in that order** — which is the honest statement, and weaker than `scout-02` could make.

## Per-candidate detail

### 1 — Genetic load (Haldane–Muller) ↔ Poisson defect-density yield model

**Same object, and this one is an algebraic identity rather than an analogy.** Population genetics' Haldane–Muller principle states that at mutation–selection balance mean fitness is `W̄ = e^(−U)`, where `U` is the genomic deleterious mutation rate — **and is independent of the selection coefficient of each mutation**. Semiconductor yield's Poisson model states that die yield is `Y = e^(−A·D0)`, where `A` is die area and `D0` defect density — **and is independent of the severity of each defect**. Both are "survival probability = exp(−expected number of independently-acting lethal defects), with the per-defect severity cancelling out." The two fields also share the same downstream question — *how many independent units before the expected number of defects exceeds one* — and the same policy use: yield engineering sets die area from `D0`, conservation genetics sets `Ne` from `U`.

**Metaphor risk, strongest form.** `A·D0` and `U` are both counts of independent lethal events, but the *independence* is doing all the work and the two fields break it differently. Genetics breaks it through **epistasis and dominance** — synergistic epistasis makes the load sub-exponential, recessivity makes deleterious alleles conditionally invisible, so the effective `U` is not a simple count. Yield modelling breaks it through **spatial clustering** — defects are not Poisson, they cluster, which is exactly why negative-binomial (Stapper) and compound (Murphy, Seeds) models replaced the pure exponential. If the two failures of independence are structurally different, the shared exponential is a coincidence of the independent-events limit and every interesting case is outside it. **This objection is also the strongest reason to open the candidate**: it names a specific, published, fitted correction on the engineering side that genetics has never applied.

**Counts.** `O = 0` on **12 of 12 pairings**, spanning A-side vocabulary from 1963 to 2022 (Kimura, Maruyama & Crow 1963; Lynch, Conery & Bürger 1995; Agrawal & Whitlock 2012; Kyriazis 2021; Bertorelle 2022) and B-side vocabulary across 1964 / 1983 / 1990 (Murphy; Stapper; Cunningham). **This is `failure-modes` mode 6 run properly**: the zero survives under each decade's own name on *both* sides, which none of `scout-02`'s ranked candidates could claim. E floors 113–233. **No concept-scoped `N` was fetched and the zero is therefore not yet quotable as a finding.**

**Hits.** None to inspect on any of the 12.

**What would close it.** The missing object is **the clustering parameter `α` of deleterious genetic load, and the discrimination between `W̄ = e^(−U)` (Poisson) and `W̄ = (1 + U/α)^(−α)` (negative binomial / Stapper's clustered-defect form).** Yield engineering knows the pure exponential systematically *under*-predicts survival because defects cluster, and has fitted `α` for four decades; conservation genetics still writes the multiplicative-independent-loci form and then adds epistasis as a separate free parameter. Computable from already-published numbers: Kyriazis 2021's and Bertorelle 2022's tabulated simulated and empirical genetic-load distributions, plus per-genome deleterious-allele counts already published for the vaquita, Isle Royale wolves and the great apes. **~6–8 hours.** Deliverable: a fitted `α` for genomic load and a statement of whether the negative-binomial form beats the exponential — which, if it does, means published extinction-risk-from-load estimates are biased in a known direction by a known amount.

**Extends.** No existing instrument cleanly. It is in the **C6 / C19 mould** — the dimensionless number the field never wrote down — and it puts a genetics-side survival law on the same shelf as `C29-recovery-beta`'s hazard. `extends-to: [conservation, ecology]`.

### 2 — Adaptive management ↔ reliability growth (Duane learning curve)

**Same object.** Both describe *a programme that deliberately runs trials to drive a failure rate down, and asks how fast it falls with cumulative experience*. Duane 1964 observed that cumulative failure rate plots as a straight line against cumulative operating time on log–log paper, with slope `β` (the growth exponent); the Crow/AMSAA formalisation turned that into an estimator with confidence bounds and a stopping rule for a test-fix-test programme. Walters & Holling's "learning by doing" is the identical structure — managed system, deliberate perturbation, monitored outcome, revised model — and conservation asks the identical question ("is this programme actually learning?") **without ever computing a growth exponent.**

**Metaphor risk.** Duane's `β` presumes a **repairable system with a fixed failure-mode inventory** monotonically depleted by fixes. An ecosystem under adaptive management has a non-stationary failure-mode inventory: climate and land-use change generate new modes faster than management retires old ones, so a flat log–log slope would mean "not learning" in Duane's frame but could mean "learning at exactly the rate the world is changing." A negative result here is ambiguous in a way a hardware programme's is not.

**Counts.** `O = 0` against both A anchors; E floors 333 and 266. Both flanking controls fire — Walters & Holling x Williams 2011 = **64** (adaptive management is a joined internal literature), Duane x Barlow & Hunter = **13** (reliability growth touches maintenance optimisation).

**Hits.** None.

**What would close it.** The missing object is **a Duane growth exponent `β` for a named conservation adaptive-management programme**: cumulative interventions against cumulative unmet-objective events on log–log, slope fitted. Published numbers exist in the recovery-plan audit literature and in long-running programmes that already tabulate objectives-met-by-year (Glen Canyon, Everglades, Australian threatened-species recovery-plan audits). **~6 hours.** Deliverable: conservation's `β` against engineering's typical 0.3–0.5. A `β ≈ 0` would be the first quantitative statement that adaptive-management programmes are not, on their own published records, learning — a claim the field argues about qualitatively and has no instrument for.

**Extends.** `C18-durability-axis` (a *growth* exponent alongside the hazard shape) and `G29-early-warning-prognostics`'s reliability-engineering side. `extends-to: [conservation, ecology, sustainability]`.

### 3 — Genetic rescue / translocation timing ↔ sequential analysis and optimal stopping

**Same object.** The genetic-rescue decision is: *keep observing a declining population, accumulating evidence that inbreeding depression rather than demography is the binding constraint, and choose a moment to act* — acting too early risks outbreeding depression and wastes a scarce translocation, acting too late means the population is below the size at which rescue works. That is Wald's sequential probability ratio test with an explicit cost of delay, and the version with a hard horizon and no recall is the optimal-stopping family Ferguson 1989 catalogues. The field's own reviews frame it as "when to pull the trigger" and stop there.

**Metaphor risk.** The SPRT presumes **i.i.d. observations from a fixed pair of hypotheses**. Genetic-rescue evidence is neither: the population's state changes *while* you observe it decline, so the hypotheses drift, and the cost of a wrong decision is neither symmetric nor bounded. This is closer to optimal control with an absorbing state than to a hypothesis test, and the honest B anchor may be Bayesian sequential decision theory rather than Wald.

**Counts.** `O = 0` on 4 pairings — Whiteley 2015, Tallmon 2004 and Seddon 2014 against Wald 1945 and Ferguson 1989. E floors 241–507.

**Hits.** None.

**What would close it.** The missing object is **the stopping boundary itself** — the threshold on accumulated inbreeding-depression evidence at which translocation maximises expected persistence, with the loss function taken from published outbreeding-depression frequencies and published rescue success rates. Whiteley 2015's own tabulated rescue case studies carry pre-rescue `Ne` and post-rescue fitness rebound; Frankham's outbreeding-depression risk tabulation supplies the other arm. **~5–8 hours.** Deliverable: a number of monitoring years, or an `Ne` threshold, that a recovery team could argue with.

**Extends.** `C25-whittle-foraging` and `G28-marginal-value-gittins` — the same indexability/optimal-stopping machinery already imported into foraging, applied one field over. `extends-to: [conservation, ecology]`.

### 4 — PVA planning horizon ↔ age-replacement policy

**Same object, claimed weakly.** PVA reports "probability of persistence over 100 years" and never derives the 100; age-replacement theory derives the optimal intervention interval `T*` by minimising a cost rate. Both are horizon-selection problems with an asymmetric cost.

**Metaphor risk, probably fatal, and it is the same objection `scout-02` raised at its rank 3.** Age replacement is a **renewal** argument — the unit resets to as-good-as-new. A managed population never resets, and the PVA horizon is chosen for institutional reasons (funding cycles, IUCN criteria) rather than by any optimisation, so there may be no cost rate to minimise. `O = 0`, E floor 454. **Do not open on the E floor.** `extends-to: [conservation]`.

### 5 and 6 — MVP and metapopulation capacity ↔ k-out-of-n redundancy allocation

**Same object, weakly, and `scout-02` already tested and shelved the MVP case at its rank 9 against a different A anchor (Traill 2007, E *scoped* 2.95).** I re-measured against Shaffer 1981 (`O = 0`, E floor 419) and added metapopulation capacity (`O = 0`, E floor 365); the same-object objection is unchanged and, I think, decisive: **k-out-of-n units fail independently; populations and patches fail through correlated environmental stochasticity, Allee effects and shared catastrophes.** The honest engineering counterpart is the **common-cause-failure** literature, not redundancy allocation — and I could not obtain a DOI-bearing common-cause anchor with a usable OpenCitations citer set inside this session. **These two rows are a lead for a different B anchor, not candidates.** Note also that `scout-02` obtained a *scoped* `E` of 2.95 for the MVP pairing, an order of magnitude below anything I can claim from a floor — **that scoped number should be believed over my floor.** `extends-to: [conservation]`.

### 7 — Seed banks / germination fraction ↔ multi-echelon inventory theory

**Same object.** A seed bank is a buffer stock held against stochastic demand, and the germination fraction `G` is a release policy. Cohen 1966 solved it by maximising the geometric-mean growth rate; Clark & Scarf 1960 solved the structurally identical multi-echelon problem by proving an `(s,S)` policy optimal. Both ask what fraction of a stock to commit each period under uncertainty, and both know the answer is not "all of it."

**Metaphor risk.** Inventory theory optimises an **expected cost with a stockout penalty**; bet-hedging maximises a **geometric-mean growth rate**, a different objective and the reason Cohen's answer is Kelly-like rather than newsvendor-like. Since Cohen x Kelly = 25 (bridged) and Cohen x Clark & Scarf = 0, the honest reading may be that ecology *did* import the right formalism and correctly declined the wrong one. **That possibility should be attacked before any hours go in.**

**Counts.** `O = 0` on all three pairings; E floors 312 / 324 / 579.

**What would close it.** The missing object is **the (s,S) reorder structure of a seed bank** — whether observed germination fractions are consistent with a threshold policy rather than a fixed fraction, fitted to Venable 2007's own multi-year desert-annual germination series. **~5 hours.** `extends-to: [ecology, conservation]`.

### 8 — Demographic stochasticity near extinction ↔ heavy-traffic queueing

**Same object.** A population with birth rate `b` and death rate `d` is a linear birth–death chain; an M/M/1 queue with arrival rate `λ` and service rate `μ` is the same chain. Kingman's heavy-traffic result governs the regime `λ → μ` — precisely the near-critical regime `b → d` where demographic stochasticity dominates and PVA is hardest — and delivers the reflected-Brownian limit and its diffusion scaling. Ecology derives the same diffusion approximation from scratch (Lande 1993) without the queueing results on the correction terms.

**Metaphor risk.** Lande's diffusion approximation **already is** the heavy-traffic limit, so the transfer may add only vocabulary. It is non-trivial only if queueing's results on *non-exponential* service and *bursty* arrivals map onto non-Poisson reproduction and catastrophe clustering — an empirical question. This overlaps `scout-02`'s rank 4 (Lande x ruin theory, E *scoped* 371), which is the better-conditioned version of the same idea; **prefer that one.**

**Counts.** `O = 0` on 3 pairings; E floors 272–285.

### 9 — Mutational meltdown / error threshold ↔ error-correcting codes

**The biggest E floor in the scout and the weakest same-object argument, which is why it is ranked here and not at the top.** `O = 0` against Hamming 1950 (E floor 720), Gallager 1962 (750) and Charlesworth 2009 x Hamming (1,152). The tempting claim — "mutation–selection balance is a code with a rate, and Eigen's error threshold is a channel capacity" — **is Eigen's own claim and belongs to the quasispecies literature, which I did not test.** The conservation-genetics anchors may show zero simply because conservation genetics is not where that bridge lives. **Do not open without first measuring Eigen 1971 x Shannon/Hamming**; if that fires, this is a scope artifact, not a gap. It is also the candidate closest to `G25-proofreading-coding`, which is currently `narrowed` precisely because coding-theory content *was* found in the co-citers on re-test — the vault's own record argues against this one. `extends-to: [conservation]`.

### 10 — `Ne` ↔ survey design effect / effective sample size

**Same object, and rather cleanly.** `Ne` is a variance-inflation-corrected count: the size of an ideal Wright–Fisher population with the same drift variance as the real one. Kish's design effect `deff = N/n_eff` is a variance-inflation-corrected count: the size of a simple random sample with the same estimator variance as the real clustered one. Both are "the number of *independent* units this thing behaves like," both are a ratio of variances, and both are routinely misread as headcounts.

**Why it is ranked last despite the clean argument.** `N_B = 46`. The B side has no citer set large enough to support a null model — E floor 44.7, and any realistic scoped `N` drives it below 1, where a zero means nothing. A better B anchor (MCMC effective sample size, or the `deff` methodological literature at large) is needed before this is measurable at all. **Recorded as a lead, not a candidate.**

## Checked and rejected

- **Bet-hedging ↔ Kelly criterion — BRIDGED, as the brief predicted.** Cohen 1966 x Kelly 1956 = **25**. Inspected 5 of 25: *The fitness value of information* (Oikos 2010), *The fitness value of ecological information in a variable world* (Ecol Lett 2023), *When Unreliable Cues Are Good Enough* (Am Nat 2013), *Pareto-optimal trade-off for phenotypic switching of populations in a stochastic environment* (JSTAT 2022), *A new long-term measure of sustainable growth under uncertainty* (PNAS Nexus 2022). All five are genuine transfers of the Kelly / log-optimal formalism into population biology. Venable 2007 x Kelly = 6, also genuine. **Closed. Do not reopen.**
- **Portfolio effect ↔ Markowitz — BRIDGED.** Schindler 2010 x Markowitz 1952 = **22**. Inspected 5: *Performance of salmon fishery portfolios across western North America* (J Appl Ecol 2014), *Emergent stability in a large, free-flowing watershed* (Ecology 2015), *Biodiversity as insurance: from concept to measurement and application* (Biol Rev 2021), *Development of a predation index to assess trophic stability in the Gulf of Alaska* (Ecol Appl 2020), *Changing salmon* (Fish & Fisheries 2019). All genuine mean–variance portfolio applications. **Closed.**
- **An in-domain negative worth recording:** Schindler 2010 x Cohen 1966 = **1** (*Growth portfolios buffer climate-linked environmental change in marine systems*, Ecology 2023), against E floor 627 and against both works being separately well-connected to finance and information theory. **Ecology's portfolio-effect literature and ecology's bet-hedging literature have each imported a different half of the same log-optimal-growth mathematics and barely cite each other.** That is an *intra*-ecology gap, outside this scout's cross-domain remit, but it is the most surprising number in the run and someone should look at it.
- **MVP ↔ redundancy allocation** — already tested and shelved by `scout-02` at rank 9 with a *scoped* `E` of 2.95. My floor-only re-measure does not improve on it. Not reopened.
- **Kuo & Wan 2007 (`10.1109/tsmca.2007.897598`)** — Crossref-resolvable but OpenCitations returns an empty citer set. Two planned rows are **void, not zero**, and are not reported as measurements.

## Recommendation: which 2 to open first, and why

**Open #1 (genetic load ↔ Poisson defect-density yield) and #2 (adaptive management ↔ Duane reliability growth), in that order.**

1. **#1 is the only candidate in this scout whose same-object claim is an algebraic identity rather than a resemblance.** `W̄ = e^(−U)` and `Y = e^(−A·D0)` are the same law, both derived from independently-acting lethal defects, both with the per-defect severity cancelling — and both fields then discovered that independence fails and patched it, one with epistasis and one with clustering, **without either knowing the other had done it.** Every other ranked candidate here is a shared *shape*; this is a shared *equation*.
2. **#1 is also the only candidate whose zero survives `failure-modes` mode 6 as run rather than as promised.** Twelve pairings, five decades of genetics vocabulary against three decades of yield-modelling vocabulary, all zero — and both literatures pass their own internal positive controls (39 on the genetics side; 42 and 52 on the yield side). `scout-02` correctly flagged that none of its candidates had had mode 6 run; this one has.
3. **#2 is the cheapest falsifiable number in the set, and it is a number conservation is currently arguing about without an instrument.** "Is adaptive management actually learning?" is a live, contested, qualitative debate; Duane's `β` turns it into a log–log slope fitted to programme records that are already published. Six hours, public data, and a negative result (`β ≈ 0`) is as publishable as a positive one.
4. **#3 is the natural third** — it reuses `C25`/`G28`'s optimal-stopping machinery on a new field and needs no new formalism — but it carries real metaphor risk (the SPRT's i.i.d. assumption) that #1 and #2 do not.

**Do not open #9 (meltdown ↔ coding theory) despite it having the largest E floor in the scout.** Its claim is Eigen's, its likely home is the quasispecies literature I did not measure, and the vault's own `G25-proofreading-coding` was *narrowed* on exactly this kind of re-test. Measure Eigen x Shannon first; if it fires, #9 is a scope artifact.

**And a standing caveat that applies to every row above.** Every `E` in this report is a **union floor**. `citation-intersection` is explicit that a floor flatters a gap and is not quotable alone, and `scout-02`'s own experience is the warning: its rank 7 looked excellent at the floor and collapsed to `E = 0.35` at a fetched concept scope. **Before #1 or #2 becomes a gap note, a concept-scoped `N` must be fetched from OpenAlex and the 10x sensitivity run.** For #1 the scope to fetch is the union of a genetic-load / population-genetics concept and a semiconductor-yield / defect concept from 1964; for #2, adaptive management ∪ reliability engineering from 1964. Until then these are leads at `evidence: citation-intersection`, not standings.

## Provenance

- **Provider: OpenCitations.** Endpoint `https://api.opencitations.net/index/v1/citations/<doi>`, User-Agent `biomimicry/1.0 (mailto:deciduusleaf@gmail.com)`. `N_A`, `N_B` are counted distinct non-empty `citing` DOIs from that response, lowercased. **All fetches 2026-09-05.** Coverage basis: OpenCitations' DOI-to-DOI index only; anything without a DOI is invisible to it. No reference lists were pulled, so coverage is 100% of what the provider indexes.
- **DOI verification: Crossref**, `https://api.crossref.org/works/<doi>?mailto=deciduusleaf@gmail.com`, all 2026-09-05; title, year, container and `is-referenced-by-count` read from `message`.
- **OpenAlex: zero calls made.** Budget-locked to one probe; a single probe cannot buy both a concept id and a scoped count, so none was spent and **every `N_universe` here is a union floor, stated as a floor.** A scoped `N` must be fetched later before any row is quoted.
- **Known bug, fixed mid-run, and a recommended change to `vault/_scripts/intersect.py`:** OpenCitations returns records with an empty `citing` field; de-duplicating without filtering them adds a phantom element that inflates `N_A`, `N_B` and every intersection by 1. Filter `if x.get("citing","").strip()`. My uncorrected first pass reported five candidates at `O = 1` that are clean zeros, and every control at one above its true value.
- **Discarded, not reported:** `10.1093/oxfordjournals.jhered.a111612` (resolved to *RAPDSIM*, not the mutational meltdown; replaced by `10.1086/285812` after title search), `10.1111/j.1523-1739.1996.10041500.x` (Crossref 404), `10.1109/tsmca.2007.897598` (empty OpenCitations citer set; its two rows void).
- **Not done, and it matters:** no hit was full-text read, because there were no hits on any ranked candidate. The two rejected pairs were inspected at title/journal level only (5 of 25 and 5 of 22) — enough to establish they are genuine bridges, not enough to characterise them.
