---
name: novelty-audit
type: method
---

# The honest novelty audit

> **What this project actually produced that is new, stated straight.** Across ~50 gradable
> results the genuinely-novel output is small and namable: **one strong bridge** (Charnov's
> marginal value theorem *is* the Gittins index of the outside option, [[C5-charnov-gittins]]),
> **two named dimensionless objects that appear unwritten** (the healing Damköhler number
> `Ha = k_r/k_d`, [[C6-damage-healing-ratio]]; and a hedged new sensing-limit derivation with a
> pooling prediction, [[C4-inclination-sensing-limit]]), and **one bias-immune empirical
> conditional with a dated falsifiable prediction** (same-class disagreements resolve to
> systematics, never new physics — [[C16-same-class-catalogue]]/[[Q7-same-class-prediction]]).
> Everything else is honest work of four lesser kinds: roughly **twenty useful repackagings**
> (two audit instruments, the Π-lattice/kernel operators, Σ, the Weibull-β and gain-bandwidth
> and passivity axes — real, portable, but assembled from textbook physics), **two rediscoveries
> the project derived and then found already existed** ([[C9-moving-coupling-point]],
> thermoacoustics + Bezsudnov-Snarskii 2014; and [[kedem-caplan]], in active use not unread),
> **~twenty located gaps** (the C-note substrate and the theorem-bridges — locating a gap is real
> work but is *not* producing novelty), and **a running column of self-corrections** (the 578
> reference fix, the sail conjugate-pair fix, the neutron-lifetime frame, two stale citation
> counts, and several withdrawn zeros). The project's real product is a **method and a catalogue**,
> with a handful of genuine bridges inside it — not a pile of new physics. See
> [[what-closes-a-gap]], [[reading-not-counting]], [[precedent]].

The bias of this audit points at humility: where a grade was uncertain it was set lower, and any
result that *might* be a rediscovery is graded REPACKAGED or flagged, never NOVEL.

## The grades

- **NOVEL** — appears genuinely unwritten in reachable sources; the note ran a prior-art search and found none.
- **REPACKAGED** — real and useful, but assembles/renames known pieces; the physics/math is standard, the packaging is the contribution.
- **REDISCOVERED** — the project derived something that already exists and was found to exist.
- **LOCATED** — not a new result but a documented gap/absence (LBD-style). Most gap entries.
- **CORRECTED** — a self-correction of the project's own error. Honesty, not novelty.

## Grade table — computed notes

| Note | Result (one line) | Grade | Prior-art basis | Biggest threat to novelty |
|---|---|---|---|---|
| [[C1-availability-living-tissue]] | First availability figures for biological tissue (PSII 0.883, bone 0.984) | REPACKAGED | Applies textbook [[availability-formula]]; C13 confirms the *formula* is unread by biology, but the computation is a direct application | A biophysics paper having already computed PSII "availability"; only co-citation (not full-text) checked |
| [[C2-probabilistic-safety-factors]] | Bone failure probability set by tissue, not locomotor, variability | REPACKAGED | [[stress-strength-interference]] (1967) applied to biology; the load-adaptive-strength inversion is stated as a direction, not derived | The symmorphosis P_f literature (Alexander mixed chains) — this is exactly [[G19-safety-factor-derived-twice]] |
| [[C3-energy-error-axis]] | Every information substrate on one kT-normalized axis | REPACKAGED (+CORRECTED) | Note itself withdrew the "no such axis exists" claim ([[G8-energy-per-bit-axis]] overturned, 575 Landauer-neural papers); composed identity "may still be novel" | Landauer/Shannon composition is standard; the specific figure the only possibly-new piece |
| [[C4-inclination-sensing-limit]] | Berg-Purcell bound for a statocyte forces cross-cell pooling; δθ_min∝1/√(MNτ), falsifiable | **SPLIT** (2026-09-05): (a) M^−1/2 pooling law NOT NOVEL, textbook Berg–Purcell; (b) pooling-vs-summation model contrast LOCATED in stochastic-pooling networks (McDonnell et al. PRE 88:022118); (c) the statocyte application and the 1.73 vs 3.00 angular experiment **NOVEL (hedged)**, 16 query formulations | Search absence, not citation-intersection absence; Berg–Purcell 1977 × Blancaflor 1998 intersection not yet run | See C4 `## Prior-art check 2026-09-05` |
| [[C5-charnov-gittins]] | Charnov's R\* **is** the Gittins index of the outside option, exact identity | **NOVEL** (E3 kill-check 2026-09-05, held) | 12 web queries + 5 OpenAlex full-text queries; full texts of Kacelnik 1979 thesis, McNamara & Houston 1985, Kilpatrick et al. 2020, Scully & Terenin 2025, Jacko 2019 extracted and grepped — **none state it**. Both books reached at Google Books term-index level: H&M 1999 has no "Gittins"/"bandit"/"index"/"Charnov"; Gittins-Glazebrook-Weber has no "foraging"/"Charnov"/"animal". Strongest prior art is an explicit **denial** — Kilpatrick et al.: "as formulated these are still different decision problems" | No longer the two books. Three **unread full texts**: H&M 1999, Gittins-Glazebrook-Weber 2011 (both archive.org/Wiley 403), and **Griebling et al. 2026** ([10.1016/j.anbehav.2026.123491](https://doi.org/10.1016/j.anbehav.2026.123491)), the only document known to cite Charnov 1976 + Gittins 1979 + the Gittins book — abstract is empirical, full text SD 403. See C5 §11 |
| [[C6-damage-healing-ratio]] | Healing Damköhler number `Ha = k_r/k_d = MTBF/MTTR`, reduces to availability | **REPACKAGED** (downgraded 2026-09-05, was NOVEL) | `1/Ha` is the offered load ρ of an M/M/1/1 loss system; `A = Ha/(1+Ha)` is the Erlang-B blocking complement (C6 §1.1) | What survives: no source applies the group to damage/repair or spans biology and engineering on one axis — an axis-construction contribution, not a new group |
| [[C7-discrepancy-catalogue]] | 39 inter-method disagreements tallied; fraction explicitly not a base rate | REPACKAGED | Assembled from known resolved cases; the selection-bias analysis is the contribution | Bailey 2017 (magnitudes); the surviving finding is the conditional, which lives in C16 |
| [[C8-momentum-harvesting-metric]] | Σ = P/(F·Δu)∈[0,1] spans soaring, sails, tethers; reproduces min-shear | REPACKAGED (+CORRECTED) | Identity P=−F·Δu is textbook; each special case (2v/c, V/Δu≤1/3) known; corrected gap-note's "sail has no conjugate pair" | **RESOLVED 2026-09-03**: Greason read in full — it has a bounded shear-extraction efficiency (η_ext<1), so the *concept* is not ours; but Σ's bilinear form and cross-branch span are ABSENT there. Confirms REPACKAGED, not a straight rediscovery |
| [[C9-moving-coupling-point]] | Moving coupling point doesn't beat q; it's a Péclet number = thermoacoustics | **REDISCOVERED** | Note self-classifies "CLOSED three times over": Bezsudnov-Snarskii 2014 found the Péclet parameter; Proesmans-Van den Broeck 2015; Stirling 1816 | Fully known — thermoacoustics is a mature discipline scoring itself in % of Carnot |
| [[C10-healing-curve-fit]] | Cycled healing is a decaying envelope, not a rate balance; class-dependent | REPACKAGED | Standard decay-fitting on 7 published datasets; the mechanistic discrimination + Kirkwood frame is the contribution | Self-healing-polymer community reports η(N) decay routinely; discrimination may exist |
| [[C11-flyby-reservoir-audit]] | Flyby anomaly residual specification (1-9 mN, 2ΩR⊕/c, non-stationary) | REPACKAGED | Application of the reservoir-audit instrument; reproduces known exclusions (Rievers thermal, Adler DM); resolves nothing | Flyby-anomaly literature already carries these exclusions; output is a specification, not a result |
| [[C12-pi-space-lattice]] | Froude/Reynolds/Péclet/Damköhler as integer vectors in one dimension-matrix kernel | REPACKAGED | Note: integer-kernel/SNF framing is **classical** (Kitano; textbook); micro-scale co-location already exists | The Foraging Mandala (Stocker group) already co-locates transport dimensionless numbers |
| [[C13-unread-theorem-audit]] | Four theorem-bridges survive citation intersection (0 co-citers) | REPACKAGED (+CORRECTED) | Applies [[citation-intersection]]; verification not discovery; corrected two stale vault numbers (46 citations, 753 works) | It hardens the pattern only to citation-intersection level, not full-text (its own caveat) |
| [[C14-degree-of-passivity]] | Passivity is a cycle-averaged energy fraction P on one axis of a 2×2 Boolean lattice | REPACKAGED | Energy bookkeeping + Boolean lattice; note admits control-theory passivity index is the rigorous twin of P's energy axis | Control-theory passivity index (already measures axis 1) |
| [[C15-metastability-metric]] | The single metastability figure of merit does NOT exist; prefactor spans ~20 orders | LOCATED | A clean negative: no shared exponential/prefactor across the 5 classes; establishes non-constructibility | The positive residual (prefactor discriminates the Arrhenius subset) is a minor new observation |
| [[C16-same-class-catalogue]] | 24-case same-class sample: 16 systematics / 0 new-physics; conditional holds | **NOVEL** | Bias-immune, purpose-built (not fame-selected) sample; redshift-clock danger case survives | Metrology folklore already holds "same-method disagreement = systematic" (METHOD §5); the *quantified stated conditional* is the new part |
| [[C17-offset-from-threshold]] | The portable invariant is gain × bandwidth, conserved along the offset axis | REPACKAGED | Note: shared gain exponent is a **tautology**; the invariant is the JPA field's own published `B·√G = const` | The parametric-amplifier B·√G law — identical content, already in one of the three fields |
| [[C18-durability-axis]] | Shared durability axis is Weibull shape β, not cycle count; flow batteries fail like enzymes | REPACKAGED | Weibull β is textbook reliability; the cross-domain axis + reclassification is the packaging | Battery-side Weibull fits are standard; enzyme β=1 inferred from bulk first-order kinetics |
| [[C19-hormesis-biphasic-fit]] | Fitted shot-peening biphasic curve: window ≥15× matches biology's 10-20× | REPACKAGED | Curve fit on published data + toxicology hormesis formalism; note: "not a universal constant, not a theorem" | Calabrese hormesis quantification (decades old); over-peening is a named engineering effect |
| [[C20-release-the-constant]] | M6 as an integer operator; re-derives gecko contact-splitting blind | REPACKAGED | Note: matrix augmentation is textbook (Szirtes); the directed operator + blind validation is "underexplored, not first" | Szirtes' applied dimensional analysis (adds/suppresses variables for singular matrices) |
| [[C33-lolp-starvation]] / [[G34-lolp-starvation-risk]] | Grid adequacy and bird winter energetics run one reserve recursion with one shadow price, but report different functionals | **REPACKAGED** (graded 2026-09-05, `audits/g34-adversarial.md`) | The dynamic program is **ruin theory** (Lundberg 1903, Cramér 1930) in both fields, and the demand-side reading — counting load reduction toward adequacy — is **mature grid practice** (MISO *Demand Response 101* 2024; PJM capacity auction; "negawatt" since Lovins 1989), so the borrowing runs **grid → bird**, not bird → grid | Both halves are old; and the quantitative leg failed its own positive control — rev.1's `P(starve) = 8.25e-8` is withdrawn (policy overshot Brodin 2017's 0.74 g/day by 2.26×; `C_WU = 6 kJ` zeroed). Prior-art sweep ran on Europe PMC + WebSearch only (S2 429, OpenAlex budget), so the C5 §11 bar is not met on the engineering side |
| [[C35-soil-ha]] / [[C42-soil-ha-theory]] / [[C43-soil-ha-replication]] | Soil on C6's `Ha` axis (conventional agriculture 0.011, no-till 0.21, native vegetation 1.31); USDA `T` sets `Ha` ≡ 1 by construction and exceeds measured formation by 22.6–54.3× | **REPACKAGED (+ CORRECTED)**, with **§5 REDISCOVERED** (graded 2026-09-05, four-leg deep inquiry) | The erosion÷formation ratio is mainstream soil science: **Verheijen et al. 2009** (*Earth-Sci. Rev.*, `10.1016/j.earscirev.2009.02.003`) sets tolerable ≡ formation and reports actual arable erosion at 3–40× the upper tolerable limit; **Montgomery 2007** states the discrepancy at 1–2 orders of magnitude; **Evans et al. 2020** (*Environ. Res. Lett.*, `10.1088/1748-9326/aba2fd`) already publishes the dimensioned version as soil lifespan `L = D/(E−F)` over 10,030 plot-years; and the USDA's own Erosion Index `EI` = erosion/`T` is `1/Ha` with `T` swapped for the formation rate. `T` = 5 short ton/ac = 1 inch per 29.5 yr, so `Ha ≡ 1` at `T` is `T`'s **definition** | The `Ha` framing is the weakest of the three available framings (C42), `A = Ha/(1+Ha)` has **no meaning for a stock** and its column is deleted, and `k_r` carries an unreported factor-2 depth ambiguity (Heimsath `P(300 mm)` = 0.0386 vs Montgomery median 0.017). Corrected: `T` had been quoted from a secondary range while the note's own primary source states it |

## Grade table — theorem-bridges

| Note | Result | Grade | Prior-art basis | Biggest threat |
|---|---|---|---|---|
| [[kedem-caplan]] | Degree of coupling (1965) contains thermoelectric ZT: q²=ZT/(1+ZT) | **REDISCOVERED** | Note self-corrects: found **in active use** (Chimal-Eguia 2023; Morrison-Osterle 1965 parallel derivation), not unread | Already applied to thermoelectrics + oxidative phosphorylation in one 2023 document |
| [[availability-formula]] | MTBF/(MTBF+MTTR) ≡ photosystem repair steady state | LOCATED | Textbook formula; C13 intersection 0 (99% coverage biology side, thin engineering anchor) | The formula is not new; only the *unread-by-biology* gap is the finding |
| [[stress-strength-interference]] | 1967 reliability; biology re-derived it 1997 (Alexander) | LOCATED | C13 STILL-UNREAD, 0 co-citers, all 39 Alexander citers are biomechanics | One-way gap; theorem itself 30 years old |
| [[hill-number-multifunctionality]] | Ecology's N-function math is what engineering multifunctionality needs | LOCATED | [[G6-multifunctionality]] intersection 0 across 1,033 works; C13 positive control fired at 7 | Located gap, not a produced object |
| [[kirkwood-disposable-soma]] | 1977 disposable-soma theory unread by self-healing materials | LOCATED | C13 strongest: 99.4% coverage across 5,075 self-healing citers, 0; 368 citing journals, no materials venue | Non-citing parallel derivation invisible to citation intersection |
| [[LaMSA-latch]] | The latch design rule exists; the latch itself is uncharacterized | LOCATED | [[G12-latch-fatigue]] full-text-read; 2023 JEB review explicitly defers reusability | Located gap |

## Grade table — gaps' surviving claims (LOCATED unless noted)

| Gap | Surviving claim | Grade |
|---|---|---|
| [[G1-gradient-coupling]] | Thermodynamic branch already unified & in active use; momentum-branch gap survives | LOCATED (thermo branch = a rediscovered closed case) |
| [[G2-metastability-metric]] | Cross-class axis missing — and C15 shows it is non-constructible | LOCATED |
| [[G3-cycle-life]] | Catalysis vs energy-storage durability, 0 both ways | LOCATED |
| [[G4-criticality-as-design]] | Shared design principle; earlier downgraded to single-review omission | LOCATED (narrowed) |
| [[G5-repair-number]] | Missing object is the ratio; supplied by C6 | LOCATED |
| [[G6-multifunctionality]] | **The only entry to survive both standards** — intersection 0, 1,033 works | LOCATED (best-measured gap; still not a produced novelty) |
| [[G7-how-passive]] | Ladder reinvented in ≥4 fields, no field has a number | LOCATED |
| [[G8-energy-per-bit-axis]] | Absence claim **withdrawn** (575 Landauer-neural papers) | CORRECTED (overturned) |
| [[G9-discrepancy-base-rate]] | Distribution of *outcomes* still uncomputed (meta-research) | LOCATED |
| [[G11-plant-gravisensing]] | Noise floor is active agitation ~10× ambient; no limit derived vs that | LOCATED (+CORRECTED: 100× error & source misdescription fixed) |
| [[G12-latch-fatigue]] | Held in strongest form; 2023 JEB review defers re-usability | LOCATED |
| [[G17-overconfident-uncertainties]] | Restored with correction: a citation is not a follow-up | LOCATED (+CORRECTED) |
| [[G19-safety-factor-derived-twice]] | Alexander 1997 = stress-strength 1967, zero crossings, 46 works inspected | LOCATED |
| [[G20-resize-vs-throttle]] | **Overturned** — symmorphosis IS a design-margin formalism; direction inverted | CORRECTED |
| [[G21-dimensionless-regime-map]] | Surviving half closed by construction (C12) | LOCATED |
| [[G22-scale-transfer-triage]] | Live; Perricone 2021 asks for the guidelines. Criterion is "methodology packaging" | LOCATED (criterion itself REPACKAGED) |
| [[G23-hormesis-formalism]] | Nobody parameterises the curve; C19 supplies partial numbers | LOCATED |
| [[G25-proofreading-coding]] | kT-per-error-suppression shared, neither field reads other; 1,463 citers intersected | LOCATED (project's strongest-measured gap) |
| [[G27-collective-decision]] | **Overturned/withdrawn** — anchored on "Paxos", a proper noun | CORRECTED |
| [[G28-marginal-value-gittins]] | Charnov's rule IS the Gittins index; identity supplied by C5 | LOCATED (identity itself = C5, NOVEL) |
| [[G34-lolp-starvation-risk]] | Shared reserve recursion + shared shadow price, different estimands; 20 pairings, two providers, 0 | LOCATED (narrowed 2026-09-05: the first-passage framing and C33's headline numbers were wrong) |
| [[G36-wear-erosion-damage]] | **Leg 1 only.** Tribology and agricultural soil-erosion modelling fit the same species of constant to the same measurement and cite each other nowhere — 40 decade-binned cells 1936–2022 × 1945–1995, two providers, all zero, nine controls firing, `E` = 75.6 at the narrow scoped `N`. But the gap names **no missing object**: the Archard form does not transfer (divisor vs threshold; `K_soil` is not constant), so what soil science lacks is not a law but the other field's forty years of published failure to predict its own constant. **Leg 2 (Miner ↔ aggregate breakdown) withdrawn on sign** — MWD is non-monotone under wet–dry cycling, Miner's `D` cannot be. `topology` stays **disjoint**: the proposed mediator (Hsu, Dietrich & Sklar 2008) is read by geomorphology and by neither soil anchor, so any Archard borrowing there is **one-way, geomorphology → tribology** | LOCATED (narrowed 2026-09-05) |

## Grade table — instruments and question-notes

| Note | Result | Grade | Basis / threat |
|---|---|---|---|
| [[reservoir-audit]] | Σ-inversion as availability audit; validated 5/5, reproduces Pioneer to 7% | REPACKAGED | Assembles textbook P=−F·Δu into a procedure; Pioneer reproduction is validation, not new physics |
| [[information-audit]] | Entropy sibling; validated 3/3 (Bérut, Toyabe, Koski), names the sink | REPACKAGED | Landauer/Sagawa-Ueda identities packaged into an audit; the ledger is standard stochastic thermodynamics |
| [[specification-instruments]] | The meta-template: exact identity → finite enumeration → exclusion → residual specification | REPACKAGED | A named meta-pattern over the project's own instruments; useful framing, not a result |
| [[positive-controls]] / quantification filter | Known-closed pairs run alongside claims; commensurable-metric entry gate | REPACKAGED | Per [[precedent]], the two features LBD does not already have — "defensible," claim nothing more |
| [[Q7-same-class-prediction]] | Same-class conditional + dated falsifiable α prediction | **NOVEL** | Same finding as C16; the one result selection bias cannot touch |
| [[Q9-fuel-free-is-an-assumption]] | Σ>1 inverts into a reservoir detector; Σ>1 = misidentified reservoir | REPACKAGED (+CORRECTED) | Inversion of the C8 identity; the project made the exact sail error and caught it |
| [[Q4-healing-needs-a-new-law]] | The broken healing constitutive law names three testable replacements | LOCATED | A located gap with a discriminating curve-fit (delivered in C10) |

## The strongest genuinely-novel results (survived prior-art search)

1. **[[C5-charnov-gittins]] — Charnov's marginal value theorem is the Gittins index of the outside
   option.** An exact two-line identity, with the failure boundary stated (restlessness, switching
   costs, non-stationarity — the three places the bandit theorem is *known* to break, mapping onto
   three known foraging complications). Survived a full-text prior-art sweep; a 2024 bioRxiv paper
   independently rediscovers the same threshold *without ever naming Gittins*, which is positive
   evidence the gap is real. **Re-checked adversarially on 2026-09-05 under backlog row E3 and it
   held** (C5 §11): the closest prior statement anyone has published is a *denial* — Kilpatrick,
   Davidson & El Hady, having compared patch foraging with the bandit directly, conclude "as
   formulated these are still different decision problems". Two more near-misses were added by
   that sweep: Kacelnik's 1979 thesis solves the foraging bandit by dynamic programming with zero
   occurrences of "Gittins", and McNamara & Houston 1985 names the two-armed bandit *and* MVT's
   circularity in one paper without connecting them. The single strongest result in the project.
2. **[[C16-same-class-catalogue]] / [[Q7-same-class-prediction]] — same-class disagreements resolve
   to systematics, never new physics.** Bias-immune (a conditional with no surviving counterexample,
   so the denominator cannot hurt it), purpose-built sample of 24, and it makes a dated falsifiable
   prediction about the fine-structure-constant discrepancy. The redshift-clock danger case was hunted
   hard and did not break it.
3. **[[C6-damage-healing-ratio]] — the healing Damköhler number `Ha = k_r/k_d`.** A named
   dimensionless group with a prior-art search that came back empty, populated with verified numbers
   across biology and engineering. Weaker than the above because it is algebraically MTBF/MTTR — the
   novelty is the name and the cross-domain axis, not new physics.
4. **[[C4-inclination-sensing-limit]] — a new sensing-limit derivation forcing cross-cell pooling.**
   No published statocyte-pooling proposal was found in ~10 queries, and it emits a falsifiable
   ~500-root experiment. Hedged: the Berg-Purcell machinery is textbook and the search was thin.
5. **NEW CANDIDATE, 2026-09-05, not yet graded NOVEL — [[C43-soil-ha-replication]]'s
   `ρ(T, P) = −0.180`.** Across **1,053 US sites** (OCTOPUS ¹⁰Be denudation joined point-in-polygon
   to SSURGO `tfact` via the USDA Soil Data Access API), the USDA's tolerable-soil-loss `T` is
   **anti-correlated** with measured soil formation (Spearman ρ = −0.180, p = 4.5e-9; every
   robustness specification negative, down to −0.303 on mineral horizons only). The mechanism is
   named: `T` is assigned on profile **depth**, an inventory, and depth anti-correlates with
   formation **rate** because thin soil sits on the steep limb of the production function. `tfact`
   class 1 is calibrated (median ratio 0.93); classes 3–5 run at 24–47×. **This reclassifies `T`
   from a bad estimate of a formation rate to not an estimate of a rate at all**, which is
   strictly stronger than the prior art ([[C35-soil-ha]] §5, Verheijen 2009, Montgomery 2007), all
   of which allows `T` to be a formation estimate that is merely too generous. It is stated here
   as **the one candidate in this cluster for a genuinely new empirical claim, pending its own
   adversarial pass** — and it was found in the data rather than pre-specified (C43's own
   pre-registration covered the median and the sign test, not the class mechanism), so on this
   project's rules it is a hypothesis for someone else to test until that pass is run.

## The results most at risk of being unrecognized rediscoveries

1. **[[C8-momentum-harvesting-metric]] (Σ) — RESOLVED 2026-09-03.** Greason read in full: it
   **does** carry a bounded shear-extraction efficiency (`η_ext < 1`), so the *concept* of a
   bounded extraction efficiency is not ours — but Σ's specific `P/(F·Δu)` bilinear form and its
   cross-branch span (soaring + sails + tethers) are **absent** from Greason. Verdict:
   **REPACKAGED confirmed, not a straight rediscovery.** No longer the top risk; moved off this
   list. It was already outside the NOVEL-4, so no headline changes.
2. **[[C6-damage-healing-ratio]] (Ha).** It is MTBF/MTTR passed through the Möbius map. Reliability
   engineering and pharmacokinetics both use the form unnamed; a named cross-domain version may exist
   in a corner not reached by ~a dozen searches.
3. **[[C20-release-the-constant]] and [[C12-pi-space-lattice]].** Both rest on augmenting/reading the
   integer kernel of a dimension matrix — 111-year-old textbook machinery (Szirtes does the exact
   augmentation; Kitano the exact SNF framing; the Foraging Mandala the exact micro-scale
   co-location). The directed-operator packaging is plausibly novel but sits one literature search
   away from being ordinary.
4. **[[C4-inclination-sensing-limit]].** Listed here as well as in the strongest set: it is graded
   NOVEL only on a thin search against standard Berg-Purcell physics, and unread active-matter sensing
   work could contain it.

## The honest tally

- **NOVEL: 3** — C5 (strong; survived a 17-query kill-check 2026-09-05, see C5 §11), the C16/Q7 same-class conditional (now 8 strict cases under a blind class rule, bound 0.31), C4 part (c) (hedged). **C6 downgraded to REPACKAGED 2026-09-05** (Erlang-B).
- **REPACKAGED: ~20** — C1, C2, C3, C7, C8, C10, C11, C12, C13, C14, C17, C18, C19, C20; the reservoir- and information-audit instruments; specification-instruments; positive-controls/quantification filter; Q9.
- **REDISCOVERED: 2** — C9 (thermoacoustics + Bezsudnov-Snarskii 2014); kedem-caplan (in active use).
- **LOCATED: ~20** — five theorem-bridges (availability, stress-strength, Hill-number, Kirkwood, LaMSA) plus the live/narrowed gaps G1-G7, G9, G11, G12, G17, G19, G21-G25, G28, and the C15 non-constructibility result.
- **CORRECTED: ~8 notable** — the 578→595 titleless-bibliography fix; the sail conjugate-pair fix (C8, refuted again by C9); the neutron-lifetime over-determination frame (METHOD §5); two stale citation counts (C13: 46, 753); withdrawn/overturned zeros G8, G20, G27; the G11 100× and source-misdescription fix; the G17 "citation ≠ follow-up" restoration.

**What this project produced that is new, in one paragraph.** One genuinely novel bridge that
survived a real prior-art search (Charnov = Gittins). One bias-immune empirical conditional with a
dated prediction (same-class → systematics). Two named objects that appear unwritten but are hedged
by thin searches and standard underlying math (the healing Damköhler number; the statocyte-pooling
sensing bound). Around twenty useful repackagings — two working audit instruments, a family of
dimension-matrix/kernel tools, and several portable axes (Σ, Weibull β, gain×bandwidth, the passivity
lattice) — every one built on textbook physics, with the packaging as the contribution. Two honest
rediscoveries the project derived and then found already in the literature. Around twenty located
gaps, several of them measured to the strongest standard the project has (G6, G25, Kirkwood) — real
work, but locating an absence is not producing a novelty. And a steady column of self-corrections that
is arguably the project's most trustworthy output, because a project that publicly overturns its own
578-reference claim and its own solar-sail error is one whose surviving claims can be believed. The
real deliverable is a **method with a curated catalogue**, holding a small number of genuine bridges —
not a body of new physics.

## The universal caveat

"Novel" here means **unwritten in sources we could reach**, nothing stronger. This audit is blind to:
paywalled full texts; unread books named repeatedly as the most likely hiding places (**Houston &
McNamara, *Models of Adaptive Behaviour*, 1999** and **Gittins-Glazebrook-Weber, *Multi-armed Bandit
Allocation Indices*** — *E3 update 2026-09-05: both were pursued and reached at Google Books
term-index level, neither shows the crossing vocabulary; full texts still unread, and the live
threat to C5 is now Griebling et al. 2026, not the books — see C5 §11*); and
**non-citing parallel derivations**, which citation intersection cannot see by construction (the exact
mechanism by which [[kedem-caplan]] was a rediscovery all along, and Morrison-Osterle 1965 sat
invisible). Every NOVEL grade above should be read as "appears unwritten in what we reached," with
"appears" carrying its full weight. See [[what-closes-a-gap]], [[reading-not-counting]], [[precedent]].

## G34 / C33 — what is actually new, 2026-09-05

The graded row above is **REPACKAGED**, and the two halves that make it so are both old: the
backward recursion on a stored reserve with an absorbing boundary is **ruin theory**, and reading
demand reduction as adequacy is **standard grid practice**. Two things in this cluster are not
old, and they are the only things worth claiming:

1. **The ruin-parent triple zero.** Power-system adequacy does not cite ruin theory, behavioural
   ecology does not cite ruin theory, and the two do not cite each other. The third leg is the one
   the project measured — 20 anchor pairings on two independent citation indexes, 0 in every cell
   and every decade bin ([[G34-lolp-starvation-risk]]). Two fields independently re-deriving a
   1903 actuarial result and neither naming it is the finding; the analogy between them is not.
2. **The cross-species margin/setpoint table.** [[C38-reserve-margin-across-species]] puts 19
   systems on one energy-margin axis and shows the sorting variable is neither taxon nor body mass
   nor horizon but **whether the metabolic setpoint is movable and currently moved** — the same
   animal crosses the engineered band when its lever is withdrawn, and the one species with no
   lever (*Sorex araneus*) cannot hold a winter night at any dusk fat load. **No published figure
   exists for the demand-side share of an animal's adequacy margin**, and that quantity, not the
   concept, is the transferable object.

Everything else in the cluster is located, corrected, or withdrawn.
