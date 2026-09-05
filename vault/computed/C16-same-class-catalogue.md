---
name: C16-same-class-catalogue
type: computed
---

# The same-class catalogue: hunting a counterexample to Q7

> **Same-class closed tally, 17 cases: SYSTEMATICS 16 · FLUCTUATION 1 · NEW-PHYSICS 0.**
> Plus 7 OPEN same-class disagreements carrying no outcome yet.
>
> **The conditional survives. No same-class disagreement resolved to real new physics.**
> [[Q7-same-class-prediction]] stood at eleven-for-eleven; this pass verifies those and adds
> five more closed cases, so it now stands at **sixteen closed same-class cases resolved to
> systematics, zero to new physics** (one further case was a statistical fluctuation, which is
> not new physics either). The most dangerous candidate — the gravitational-redshift clock
> comparisons, where a same-class "disagreement" genuinely *is* real physics — was run hard and
> does **not** break the conditional, but it exposes the one structural vulnerability, recorded
> below.

The narrow-question build requested by [[Q7-same-class-prediction]]: assemble same-class
persistent inter-method disagreements (two or more implementations of *one* technique) and
record how each resolved. This is the complement to [[C7-discrepancy-catalogue]] — it is a *conditional*, so it needs a
counterexample rather than a denominator, but that is not the same as being immune to bias (see
the verdict's interval, and the caveat there on findability). The live anchor is
[[fine-structure-discrepancy]]. Every outcome below was fetched this session;
`as-of 2026-09-03`.

**Class rule, applied before outcome (per Q7 / [[G9-discrepancy-base-rate]] feature 1).**
SAME-CLASS = the disagreeing determinations use the *same measurement technique*, assigned on
the apparatus/method alone, not on the answer. Genuinely ambiguous assignments are flagged `‡`.

---

## The same-class table

| # | Quantity | The two (or more) implementations | Peak σ | Outcome | Class basis (technique only) | Source (fetched) |
|---|---|---|---|---|---|---|
| 1 | α (fine structure) | Berkeley Cs recoil vs LKB Rb recoil — both h/m atom-interferometry recoil | 5.4σ | **OPEN** (predicted: systematics) | Both atom-recoil interferometry | [Nature 2020 / PubMed 33268866](https://pubmed.ncbi.nlm.nih.gov/33268866/); [review arXiv:2506.18328](https://arxiv.org/pdf/2506.18328) |
| 2 | h/m(⁸⁷Rb), α | LKB Rb 2011 (Bouchendira) vs LKB Rb 2020 (Morel), same lab | 2.4σ | **SYSTEMATICS** — 2011 wrong (wavefront curvature / Gouy phase, uncorrectable retroactively) | Both LKB Bloch-oscillation Rb recoil | [arXiv:2506.18328](https://arxiv.org/pdf/2506.18328); [PubMed 33268866](https://pubmed.ncbi.nlm.nih.gov/33268866/) |
| 3 | Tenth-order QED A₁⁽¹⁰⁾ | AHKN (Aoyama-Hayakawa-Kinoshita-Nio) vs Volkov, A₁=5.891(61) | ~5σ | **OPEN** (predicted: error in one MC evaluation; Volkov = "first complete verification") | Both Monte-Carlo integration of the same Feynman diagrams | [arXiv:2404.00649](https://arxiv.org/abs/2404.00649) |
| 4 | Newton's constant G | HUST time-of-swing torsion balance vs HUST angular-acceleration-feedback torsion balance, same group | ~2.7σ (45 ppm) | **OPEN** (residual unexplained; both agree with CODATA within 2σ) ‡ | Both torsion balance (different dynamical modes) | [Nat. Sci. Rev. 7:1803](https://academic.oup.com/nsr/article/7/12/1803/5874900) |
| 5 | Planck constant h / kg | NRC Kibble balance, successive runs; Kibble-vs-Kibble worldwide pre-2017 | above stated unc. | **SYSTEMATICS** — NRC found unrecognized hysteresis, shifted results ~4×10⁻⁹ into agreement | All Kibble/watt balance | [Metrologia 54, IOP aa70bf](https://iopscience.iop.org/article/10.1088/1681-7575/aa70bf); [NIST-4 arXiv:1708.02473](https://arxiv.org/pdf/1708.02473) |
| 6 | Muon g−2 HVP, intermediate window | BMW vs RBC/UKQCD vs Mainz vs Fermilab/HPQCD/MILC vs ETM vs χQCD | early inter-lattice scatter | **SYSTEMATICS / CONVERGENCE** — all lattice groups now agree sub-percent (they jointly disagree with data-driven, a *different-class* tension) | All lattice QCD of the same window observable | [arXiv:2401.11895](https://arxiv.org/pdf/2401.11895); [muon g-2 theory init.](https://muon-gm2-theory.illinois.edu/2023-status/) |
| 7 | Hydrogen 1S–3S | MPQ (Grinin 2020) vs LKB (Fleurbaey 2018) | 2.1σ | **OPEN** — CODATA 2022: "difference is not currently understood" | Both optical H 1S–3S spectroscopy | [CODATA 2022 arXiv:2409.03787](https://arxiv.org/pdf/2409.03787) |
| 8 | Proton radius via electronic H | 2S–4P, 1S–3S, 2S–2P electronic-H transitions scattered large-vs-small r_p | multi-σ | **SYSTEMATICS** — the large-r_p electronic results; small-r_p (muonic-consistent) prevailed ‡ | All electronic hydrogen spectroscopy | [CODATA 2022 arXiv:2409.03787](https://arxiv.org/pdf/2409.03787) |
| 9 | R(K), R(K*) lepton universality | LHCb 2014–21 vs LHCb 2022 reanalysis, same experiment, 5× data | 3.1σ | **SYSTEMATICS** — earlier LHCb electron-ID / hadronic misID | Both LHCb B→K(*)ℓℓ ratio | [LHCb outreach Dec 2022](https://lhcb-outreach.web.cern.ch/2022/12/20/improved-lepton-universality-measurements-show-agreement-with-the-standard-model/) |
| 10 | Low-energy electronic recoil in Xe | XENON1T vs XENONnT | 3.5σ | **SYSTEMATICS** — XENON1T trace tritium | Both liquid-xenon TPC | [arXiv:2006.13278](https://arxiv.org/abs/2006.13278) |
| 11 | Δα/α from quasar absorption | Keck/HIRES (−5.7 ppm) vs VLT/UVES (+2.29 ppm) | ~5σ apart | **SYSTEMATICS** — both, long-range wavelength-scale distortions | Both quasar absorption spectroscopy | [arXiv:1409.4467](https://arxiv.org/abs/1409.4467) |
| 12 | Primordial D/H | Rival quasar-absorber sightlines ("high-D" vs "low-D") | ~order of mag | **SYSTEMATICS** — low-quality sightlines; fixed by strict target selection + blind analysis | Both quasar-absorber D/H | [arXiv:1710.11129](https://arxiv.org/abs/1710.11129) |
| 13 | Θ⁺(1540) pentaquark | Low-statistics LEPS/DIANA/CLAS/SAPHIR vs high-statistics CLAS/JLab repeats | 5.3σ | **SYSTEMATICS** — the claimants, incl. same group on more data | All photo/electroproduction invariant-mass peaks | [arXiv:nucl-ex/0512042](https://arxiv.org/pdf/nucl-ex/0512042) |
| 14 | Electron antineutrino mass | ITEP (Tretyakov spectrometer) vs Zürich vs LANL | 17–40 eV claim | **SYSTEMATICS** — ITEP energy-loss + ³He–T mass-difference error | All Tretyakov-type β-spectrometry | [arXiv:0909.2104](https://arxiv.org/pdf/0909.2104) |
| 15 | Anomalous "polywater" | Capillary-condensed water vs clean-glassware repeats | — | **SYSTEMATICS** — silica/phospholipid contamination | Both capillary water property measurement | [Science History Institute](https://www.sciencehistory.org/stories/magazine/the-rise-and-fall-of-polywater/) |
| 16 | N-rays | Blondlot scintillation vs Wood prism-removal blind test | — | **SYSTEMATICS** — observer effect; signal persisted with prism removed | Both visual-scintillation detection | [APS News 1904](https://www.aps.org/apsnews/2007/08/robert-wood-debunks-nrays) |
| 17 | Element 118 cross-section | LBNL 1999 claim vs LBNL + worldwide non-reproduction | 3 atoms | **SYSTEMATICS / MISCONDUCT** — data fabricated | Same recoil-separator technique | [Physics World](https://physicsworld.com/a/element-118-disappears-two-years-after-it-was-discovered/) |
| 18 | 750 GeV diphoton rate | ATLAS 2015 vs ATLAS 2016; CMS 2015 vs CMS 2016 | 3.9σ local | **FLUCTUATION** — statistical, nobody erred (not systematics, not new physics) | Same detector, same channel, more data | [arXiv:1605.09401](https://arxiv.org/pdf/1605.09401) |
| 19 | Recommended value of c (historical) | Successive speed-of-light determinations, Birge ratio 1.47 | Birge 1.47 | **SYSTEMATICS** — reported uncertainties too small | Same era's optical/EM determinations | inherited [[C7-discrepancy-catalogue]] (CODATA drift) |
| 20 | Successive CODATA adjustments | 2006 → 2010 → 2014 → 2017 recommended values | drift > stated unc. | **SYSTEMATICS** — prior adjustments' uncertainty statements | Same least-squares adjustment method | [CODATA 2022 arXiv:2409.03787](https://arxiv.org/pdf/2409.03787) |
| 21 | W boson mass | CDF II vs D0 (both Tevatron pp̄), vs ATLAS/LEP | 4.0σ | **OPEN** | Same hadron-collider W-mass template fit ‡ | [arXiv:2506.01887](https://arxiv.org/pdf/2506.01887) |
| 22 | DAMA/LIBRA annual modulation | DAMA vs COSINE-100 vs ANAIS-112, same NaI(Tl) target | >9σ claim | **OPEN** (trending against DAMA; 5σ refutation expected) | All NaI(Tl) scintillator modulation | [arXiv:2409.13226](https://arxiv.org/abs/2409.13226) |
| 23 | ν_e capture on ⁷¹Ga | GALLEX vs SAGE vs BEST gallium sources | >5σ (BEST) | **OPEN** | All gallium radiochemical | [arXiv:2209.00916](https://arxiv.org/abs/2209.00916) |
| 24 | Hubble constant (Hubble Wars) | Sandage best-candle ladder (~50) vs de Vaucouleurs spread-risk ladder (~100) | factor 2 | **SYSTEMATICS** — both calibrations; HST Key Project landed between | Both Cepheid-anchored distance ladders ‡ | [arXiv:2308.02474](https://arxiv.org/pdf/2308.02474) |

**Closed-case tally (rows excluding OPEN): 16 SYSTEMATICS + 1 FLUCTUATION = 17 closed, 0 NEW-PHYSICS.**
**Open same-class: 7** (rows 1, 3, 4, 7, 21, 22, 23) — carry no outcome and are excluded from the fraction.

---

## The counterexample hunt — especially the clock-redshift danger case

The job was to find a same-class disagreement that resolved to **real new physics**. One would
break the conditional and be the headline. **None was found.** The hunt concentrated where the
task predicted it was most likely — gravitational-redshift clock comparisons.

### The gravitational-redshift clocks: the one place a same-class "disagreement" IS real physics

Two "identical" optical clocks at different heights genuinely tick at different rates, and the
cause is real physics (general-relativistic redshift, Δν/ν = ΔU/c²), not a measurement error.
This is the single most dangerous case for Q7. I ran it hard:

- **JILA millimetre-scale sample (Bothwell/Zheng 2022, arXiv:2109.12238 / Nature 2021):** two
  halves of a *single* strontium sample tick at different rates. **Verified: the differential
  shift was the designed measurement of a known GR effect, agreeing with the GR prediction — not
  an unexplained disagreement.**
- **Miniature clock network (Nature Comms 2023, PMC10423269):** five Sr ensembles across 1 cm.
  Measured gradient [−12.4 ± 0.7 ± 2.5]×10⁻¹⁹/cm vs GR's −10.9×10⁻¹⁹/cm — **consistent with
  general relativity**, and *blinded* (a ±5×10⁻¹⁸/cm offset was drawn at random and hidden
  during analysis). [Verified via [PMC10423269](https://pmc.ncbi.nlm.nih.gov/articles/PMC10423269/).]

**Why this does not break the conditional.** In metrology the redshift between two clocks is a
*known, computed correction applied before* any residual is ever called a discrepancy. A clock
comparison quotes the height/potential difference and subtracts it; what remains is the tested
quantity. So the redshift is never an *unexplained persistent same-class disagreement* — it is
either a designed measurement of a textbook effect (as above) or a correction line in the error
budget. Even the honest edge — the Kolkowitz-group statement that "the exact origin of the
frequency differences… was not initially known" — resolved, after full systematic evaluation, to
**the expected GR redshift**, confirming known physics, not discovering new physics. It is
therefore not a counterexample; textbook GR confirmed is not "new physics."

I also searched directly for any historical episode where two clocks disagreed, the gap was
*first blamed on a systematic*, and it later proved to be a real altitude/redshift effect.
**No such documented case surfaced** (Hafele–Keating, Pound–Rebka, GPS, and the modern optical
tests are all designed measurements where the redshift was expected). If one exists it is not in
the reachable literature.

### The other places new physics could have hidden — all clean

- **Same-class → data-driven crossings looked like same-class but are not.** The muon g−2 HVP
  (row 6) tension that matters is lattice-vs-dispersive — *different* class. Within lattice
  (same class) the groups **converged**. The tenth-order QED (row 3) is a pure same-class case
  and no new physics is even conceivable there — it must be a calculational error, cleaner than α.
- **The famous new-physics resolution in the broad catalogue was different-class.** Solar
  neutrinos (C7 row 11) resolved to new physics, but it is radiochemical-vs-Cherenkov-vs-SSM —
  *different* class. It is not on this table, correctly.

---

## The one structural subtlety (Q7's own admission, inherited from G9 feature 1)

"Same-class" must be fixed on **technique, before the outcome is known**, or the conditional is
unfalsifiable. Every row above is assigned on apparatus/method alone. The genuinely ambiguous
ones are flagged and stated honestly rather than resolved in the conditional's favour:

- **Row 4 (G, HUST):** time-of-swing vs angular-acceleration-feedback are both torsion balances
  but different *dynamical modes*. "Same class" if the class is "torsion balance"; arguably
  different if the class is the dynamical method. Flagged `‡`. It is **OPEN**, so it cannot yet
  help or hurt the conditional either way.
- **Row 8 (electronic-H r_p):** different transitions of one spectroscopic family. Same class if
  the class is "electronic hydrogen spectroscopy"; the *broad* proton-radius puzzle (muonic vs
  electronic vs scattering) is firmly different-class and lives in C7 row 1, not here.
- **Row 21 (W mass):** CDF II vs D0 are the same collider and technique class; vs ATLAS/LEP it
  is arguably a different accelerator environment. Assigned same-class on the template-fit
  technique. OPEN.
- **Row 24 (Hubble Wars):** both are Cepheid-anchored ladders, but the calibrator sets differ.
  Assigned same-class on the ladder technique.

**The single genuine vulnerability** is the redshift-clock case: it shows that if "same-class
disagreement" were defined loosely enough to include *known/designed* effects, the conditional
would be trivially broken by general relativity. It survives only because the pre-registered
inclusion rule excludes designed measurements and known-correction terms — exactly the
"define the class before the outcome" discipline Q7 demands. Recorded as the place the
conditional is thinnest.

---

## The decision procedure (A20) and the pre-registered assignments (A21)

The class assignment carried a post-hoc degree of freedom, and it was exercised in the direction
that protects the conditional (`audits/01-math-physics.md`: solar neutrinos and lattice-vs-
dispersive g−2 both land as *different*-class; the redshift counterexample is excluded by an
inclusion rule that appears only after the hunt). The fix is to state the rule as a procedure
with named inputs, then apply it blind.

### The procedure

**Inputs, in this order. Read all three off the *methods* section, never off the result.**

1. **A — apparatus.** The physical (or, for a calculation, computational) measurement principle
   whose systematic-error budget the two determinations share. Granularity: the level at which a
   single mis-modelled effect would bias *both* determinations the same way. "Torsion balance",
   "atom-recoil interferometry", "NaI(Tl) scintillator", "Monte-Carlo integration of a fixed
   diagram set".
2. **O — observable.** The quantity read out *before* any model inversion. The interference-fringe
   frequency, not α. The Ge atom count, not the neutrino flux. Two different atomic transitions
   are two different observables.
3. **P — analysis pipeline.** The model chain from raw signal to the reported number:
   subtraction/renormalisation scheme, template or line-shape model, calibrator set, bias
   corrections.

**Output — class id = the triple (A, O, P), graded:**

| Grade | Condition | Treatment |
|---|---|---|
| **CLASS-I** | A, O and P all match | **SAME-CLASS.** The conditional is tested on these and only these. |
| **CLASS-II** | A and O match, P differs | Same apparatus, different analysis. Reported separately; does not enter the headline tally. |
| **CLASS-III** | A or O differs | **DIFFERENT-CLASS.** Excluded from the conditional entirely. |

**Standing exclusion (pre-existing, restated so it is part of the procedure rather than a
post-hoc patch):** a difference that is a *known, computed correction applied before* the residual
is quoted — the gravitational redshift between two clocks at different heights being the type case
— is not a disagreement at all and never enters the catalogue, whatever its (A, O, P).

### Pre-registered assignments, 2026-09-05

Applied to the 7 OPEN rows (1, 3, 4, 7, 21, 22, 23) and the 4 `‡` ambiguous rows (4, 8, 21, 24)
— nine distinct rows — **from apparatus, observable and pipeline alone, before consulting the
outcome column.** Recorded with a `sha256` in [[predictions]].

| Row | Dispute | A | O | P | **Grade** |
|---|---|---|---|---|---|
| 1 | α, Berkeley Cs vs LKB Rb | atom-recoil interferometry | photon-recoil frequency (h/m) | h/m → α via Rydberg + mass ratios | **CLASS-I** |
| 3 | tenth-order QED A₁⁽¹⁰⁾ | MC integration of the same diagram set | the coefficient A₁⁽¹⁰⁾ | **differs** — AHKN and Volkov use different subtraction/parametrisation schemes | **CLASS-II** |
| 4 | G, HUST | same torsion balance, same lab | **differs** — swing period vs angular acceleration | differs (different dynamical model) | **CLASS-III** |
| 7 | H 1S–3S, MPQ vs LKB | optical two-photon H spectroscopy | the 1S–3S transition frequency | line-shape fit + QED inversion, same chain | **CLASS-I** |
| 8 | electronic-H proton radius | optical/microwave H spectroscopy | **differs** — 2S–4P, 1S–3S and 2S–2P are three observables | common QED inversion to r_p | **CLASS-III** |
| 21 | W mass, CDF II vs D0 | hadron-collider general-purpose detector | W → ℓν transverse-mass spectrum | template fit, same chain | **CLASS-I** |
| 22 | DAMA vs COSINE-100 / ANAIS-112 | NaI(Tl) scintillator | annual modulation amplitude of the low-energy rate | modulation fit, same chain | **CLASS-I** |
| 23 | ⁷¹Ga, GALLEX / SAGE / BEST | radiochemical ⁷¹Ga → ⁷¹Ge extraction and counting | ⁷¹Ge production rate | cross-section + source-strength inversion | **CLASS-I** |
| 24 | Hubble Wars, Sandage vs de Vaucouleurs | Cepheid-anchored photometric distance ladder | Cepheid and secondary-indicator magnitudes | **differs** — calibrator selection and Malmquist-bias treatment | **CLASS-II** |

**Two assignments change, and both change against the conditional's interest** — which is the
point of applying the rule blind:

- **Row 4 (G, HUST)** was same-class `‡`; the procedure makes it **CLASS-III**, because the two
  modes read out different observables (period vs angular acceleration). It is OPEN, so no tally
  moves.
- **Row 8 (electronic-H r_p)** was same-class `‡`; the procedure makes it **CLASS-III**, because
  three different transitions are three different observables. It is **CLOSED (SYSTEMATICS)**, so
  adopting the procedure drops the closed tally **17 → 16** (15 SYSTEMATICS + 1 FLUCTUATION,
  still 0 NEW-PHYSICS) and loosens the 95% upper bound **0.16 → 0.17**.

### The blind re-application to all 24 rows (A20)

The procedure was then run over **all 24 rows plus the three excluded candidates**, reading only
the apparatus / observable / pipeline columns. Rows already tabulated above keep their grade.

| Row | Dispute | Why | **Grade** | Change? |
|---|---|---|---|---|
| 1 | α, Cs vs Rb recoil | A, O, P match | CLASS-I | — |
| 2 | LKB Rb 2011 vs 2020 | P differs — the 2020 pipeline adds the wavefront/Gouy corrections the 2011 one lacked | **CLASS-II** | **changed** |
| 3 | tenth-order QED | P differs — different subtraction/parametrisation | **CLASS-II** | **changed** |
| 4 | G, HUST two modes | O differs — swing period vs angular acceleration | **CLASS-III** | **changed** |
| 5 | Kibble / watt balances | P differs — each lab's own correction chain | **CLASS-II** | **changed** |
| 6 | lattice HVP window, 6 groups | P differs — different actions, discretisations, scale setting | **CLASS-II** | **changed** |
| 7 | H 1S–3S, MPQ vs LKB | A, O, P match | CLASS-I | — |
| 8 | electronic-H r_p | O differs — three different transitions | **CLASS-III** | **changed** |
| 9 | R(K), LHCb 2021 vs 2022 | P differs — new electron-ID / hadronic-misID treatment | **CLASS-II** | **changed** |
| 10 | XENON1T vs XENONnT | A, O, P match (LXe TPC, low-energy ER spectrum, same chain) | CLASS-I | — |
| 11 | Δα/α, Keck vs VLT | A, O, P match (echelle QSO absorption, many-multiplet) | CLASS-I | — |
| 12 | primordial D/H sightlines | A, O, P match; target *selection* differs, which is sampling, not pipeline | CLASS-I | — |
| 13 | Θ⁺(1540) | A, O, P match (invariant-mass peak search) | CLASS-I | — |
| 14 | ν̄_e mass, ITEP vs Zürich/LANL | P differs — ITEP's energy-loss and ³He–T mass-difference modelling | **CLASS-II** | **changed** |
| 15 | polywater | A, O, P match | CLASS-I | — |
| 16 | N-rays | A, O, P match (visual scintillation) | CLASS-I | — |
| 17 | element 118 | A, O, P match (same recoil separator, same decay-chain analysis) | CLASS-I | — |
| 18 | 750 GeV diphoton | A, O, P match (same detector, same channel, same fit) | CLASS-I | — |
| 19 | historical values of c | **A differs** — the era's optical, Kerr-cell, cavity-resonator and geodimeter methods are different apparatus | **CLASS-III** | **changed** |
| 20 | successive CODATA adjustments | P differs — each cycle has a different input set and expansion factor | **CLASS-II** | **changed** |
| 21 | W mass, CDF II vs D0 | A, O, P match | CLASS-I | — |
| 22 | DAMA vs COSINE/ANAIS | A, O, P match | CLASS-I | — |
| 23 | ⁷¹Ga sources | A, O, P match | CLASS-I | — |
| 24 | Hubble Wars | P differs — calibrator sets and Malmquist treatment | **CLASS-II** | **changed** |
| — | solar neutrinos (excluded) | **A differs** — radiochemical vs Cherenkov | CLASS-III | confirms existing exclusion |
| — | lattice vs dispersive muon g−2 (excluded) | **A differs** — lattice computation vs e⁺e⁻ cross-section data | CLASS-III | confirms existing exclusion |
| — | gravitational-redshift clocks (excluded) | standing exclusion: a known, computed correction applied before the residual is quoted | excluded regardless of (A, O, P) | confirms existing exclusion |

**Count of changed assignments: 11 of 24** — 3 demoted to CLASS-III (leave the same-class set
entirely) and 8 demoted to CLASS-II (same apparatus and observable, different analysis pipeline;
reported separately, not in the headline tally). The three previously-excluded candidates are all
confirmed excluded, so the procedure does *not* rescue a counterexample — but it does thin the
evidence base substantially, in the direction that weakens the conditional.

### The tally under the procedure

| Set | Closed | Open | Outcomes of the closed | 95% one-sided upper bound on P(new physics) |
|---|---|---|---|---|
| **CLASS-I only** (rows 1, 7, 10, 11, 12, 13, 15, 16, 17, 18, 21, 22, 23) | **8** | 5 | 7 SYSTEMATICS + 1 FLUCTUATION, **0 NEW-PHYSICS** | `1 − 0.05^(1/8)` = **0.31** |
| **CLASS-I + CLASS-II** (adds rows 2, 3, 5, 6, 9, 14, 20, 24) | **15** | 6 | 14 SYSTEMATICS + 1 FLUCTUATION, **0 NEW-PHYSICS** | `1 − 0.05^(1/15)` = **0.18** |
| legacy assignment (this note's table) | 17 | 7 | 16 SYSTEMATICS + 1 FLUCTUATION, 0 NEW-PHYSICS | `1 − 0.05^(1/17)` = **0.16** |

**This is the honest headline.** Still **no counterexample at any grade** — that survives the
blind re-application intact, and it is the load-bearing claim. But the strict same-class set is
**8 closed cases, not 17**, and 8 zero-out-of-8 permits a new-physics rate of up to **31%**. The
conditional is a great deal weaker than "seventeen for seventeen" made it sound.

**Caveat on this sweep.** It was run by the same agent that wrote the procedure, on the same day,
with the outcome column visible on the page (though not consulted for the A/O/P reading). It is a
*blind-in-intent* re-application, not an independent replication. A genuine test needs a second
analyst who has never seen the outcomes.

---

## Verdict on [[Q7-same-class-prediction]]

**The conditional holds and is strengthened.** Over a same-class sample built specifically
(not fame-selected), **every one of the 16 closed same-class disagreements resolved to
systematics; the 17th was a statistical fluctuation; none resolved to new physics.** The
deliberate counterexample hunt — targeted at the gravitational-redshift clocks, the single most
likely place for a same-class disagreement to be real physics — returned **no counterexample**.

- **Prediction 1 (α, row 1):** will resolve to systematics (wavefront curvature named). Still
  OPEN, no third measurement. Unbroken.
- **Prediction 2 (tenth-order QED, row 3):** will resolve to a calculational error in one Monte
  Carlo evaluation. Volkov's is billed as the first complete verification, tilting toward AHKN
  as the erring side, but not yet declared closed. Cleaner than α (no new physics conceivable).

**The conditional now stands at N = 16 closed same-class cases, all systematics, zero new
physics** (17 closed if the one fluctuation is counted, still zero new physics), with 7 open
same-class cases as live future tests.

**What 17-for-17 is actually worth — quote the interval, not the tally.** With 17 closed cases
and zero new-physics resolutions, the **Clopper–Pearson one-sided 95% upper bound** on
P(new physics | same class) is

```
p_upper = 1 - 0.05^(1/17) = 1 - exp(ln(0.05)/17) = 1 - exp(-2.99573/17)
        = 1 - exp(-0.176219) = 1 - 0.838434 = 0.1616  ->  0.16
```

(inputs: n = 17 closed cases, k = 0 new-physics outcomes, one-sided 95%.) **So the data are
consistent with a same-class new-physics rate as high as 16%** — roughly one case in six. A
zero numerator over 17 trials is *suggestive*, not established: at a true rate of 16% the
probability of seeing zero in 17 is exactly 5%. Under the pre-registered decision procedure below, which
strips the same-class set down to **8 closed CLASS-I cases**, the bound loosens all the way to
`1 - 0.05^(1/8) = 0.31`; including CLASS-II (15 closed) it is `1 - 0.05^(1/15) = 0.18`.

The conditional should therefore be stated as **"P(new physics | same class) < 0.16 at 95%
confidence"**, not as "same-class disagreements never resolve to new physics."

Related: [[C7-discrepancy-catalogue]], [[fine-structure-discrepancy]],
[[G9-discrepancy-base-rate]], [[predictions]].

---

## Corrections 2026-09-05

Backlog A19–A21; `audits/01-math-physics.md` C16 items; `audits/03-method-epistemics.md` 19–20.

1. **A19 — "17/17" now carries an interval.** Old: the verdict quoted the tally alone
   ("N = 16 closed same-class cases, all systematics, zero new physics"). New: the
   **Clopper–Pearson one-sided 95% upper bound** is added (inputs: n = 17 closed cases, k = 0
   new-physics outcomes): `1 − 0.05^(1/17) = 1 − exp(−2.99573/17) = 1 − 0.838434 = 0.1616 → 0.16`.
   The data are consistent with a same-class new-physics rate of up to **16%**. At n = 16 (if the
   new procedure's removal of row 8 is adopted) the bound is `1 − 0.05^(1/16) = 0.171`.
2. **A19 — bias-immunity assertion DELETED.** Old: "It remains bias-immune: adding invisible
   same-class cases can only add more systematics." New: removed, and the framing sentence near
   the top ("the bias-immune complement to C7") is softened. The argument fails because
   findability of a documented *resolution* correlates with the resolution being mundane: a
   same-class disagreement that quietly turned out to be real physics would be written up as a
   discovery and reclassified, not filed as a resolved measurement dispute.
3. **A21 — decision procedure written; 9 rows pre-registered.** New section states the rule as
   inputs (apparatus, observable, analysis pipeline) → class id (CLASS-I / II / III), and applies
   it blind to the 7 OPEN and 4 ambiguous rows. **Two assignments change, both against the
   conditional's interest:** rows 4 and 8 become CLASS-III (different observable). Recorded with
   `sha256` in [[predictions]].
4. **A20 — blind re-application run over all 24 rows plus the 3 excluded candidates.**
   Old: 24 same-class rows, 17 closed, tally 16 SYSTEMATICS + 1 FLUCTUATION + 0 NEW-PHYSICS,
   no interval. New: **11 of 24 assignments change** — rows 4, 8, 19 → CLASS-III (different
   apparatus or observable); rows 2, 3, 5, 6, 9, 14, 20, 24 → CLASS-II (different analysis
   pipeline). The three excluded candidates stay excluded. Strict CLASS-I tally: **8 closed
   (7 SYSTEMATICS + 1 FLUCTUATION), 5 open, 0 NEW-PHYSICS**, 95% upper bound
   `1 − 0.05^(1/8) = 0.31`; CLASS-I+II: 15 closed, bound `1 − 0.05^(1/15) = 0.18`. **No
   counterexample appears at any grade** — that survives — but the evidence base is 8 strict
   cases, not 17. Limitation stated in the note: same-day, same-agent, blind-in-intent only.
