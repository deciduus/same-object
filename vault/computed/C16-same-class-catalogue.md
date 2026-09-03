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
record how each resolved. This is the bias-immune complement to [[C7-discrepancy-catalogue]] and
the live anchor is [[fine-structure-discrepancy]]. Every outcome below was fetched this session;
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
same-class cases as live future tests. It remains bias-immune: adding invisible same-class cases
can only add more systematics. Related: [[C7-discrepancy-catalogue]], [[fine-structure-discrepancy]],
[[G9-discrepancy-base-rate]].
