---
name: C7-discrepancy-catalogue
type: computed
---

# Catalogue of persistent inter-method disagreements

> **Raw tally, 39 cases: SYSTEMATICS 20 · OPEN 14 · NEW-PHYSICS 1 · THEORY-ERROR 2 ·
> REDEFINITION 1 · UNRESOLVED-IN-SOURCES 1.**
>
> **This is not a base rate and must not be quoted as one.** The sample is assembled from
> what is findable, and findability correlates with outcome in at least four directions
> documented below. Of the 25 closed cases, 20 are SYSTEMATICS — but the denominator is
> wrong in ways that are known and, in one direction, large. Read the selection-bias section
> before using any number from this file.

The data-collection half of [[G9-discrepancy-base-rate]]. Bailey 2017 computed the
distribution of discrepancy *magnitudes* over 41,000 measurements; this is an attempt at the
distribution of *outcomes*. The live anchor case is [[fine-structure-discrepancy]].

**Inclusion rule.** Two or more measurements of the same quantity, by named methods,
disagreeing by a stated significance for a stated period — not a one-off outlier. Sources
were fetched this session; where a figure is approximate it is marked so.

---

## The table

| # | Quantity | Disagreeing methods | Peak σ (year) | Duration | Outcome | Which side was wrong | Class | Over-det. | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Proton charge radius | Muonic-H Lamb shift vs e-p scattering + H spectroscopy | ~7σ (2010) | 2010→2019, 9 yr | SYSTEMATICS | Older electron-based determinations | DIFFERENT | yes | [arXiv:2502.16185](https://arxiv.org/abs/2502.16185) |
| 2 | Fine structure constant α | Berkeley Cs recoil vs LKB Rb recoil (both h/m atom interferometry) | 5.4σ (2020) | 2020→open, 6 yr | OPEN | — | **SAME** | yes (electron g−2 to 0.11 ppb) | [arXiv:2506.18328](https://arxiv.org/pdf/2506.18328) |
| 3 | Newton's constant G | Torsion balance vs beam balance vs atom interferometry | spread 550 ppm; CODATA-2022 applied expansion factor 3.9 | ~1995→open, 30 yr | OPEN | — | DIFFERENT | **no** | [arXiv:2505.00170](https://arxiv.org/pdf/2505.00170) |
| 4 | Neutron lifetime | Beam (counts decay products) vs bottle (counts survivors) | 4.1σ (2018); J-PARC 2024 now 2.3σ vs proton-beam average | ~1990→open, 36 yr | OPEN | — | DIFFERENT | yes (V_ud, g_A) | [arXiv:2412.19519](https://arxiv.org/abs/2412.19519), [arXiv:1812.09671](https://arxiv.org/pdf/1812.09671) |
| 5 | Muon anomalous moment a_μ | Fermilab/BNL storage-ring measurement vs SM prediction | ~5σ vs the 2020 White Paper prediction | 2001→2025, 24 yr | **THEORY-ERROR** | The prediction, not the experiment. WP25: a_μ^exp − a_μ^SM = 38(63)×10⁻¹¹, "no tension between the SM and experiment"; the shift came from replacing data-driven HVP with lattice QCD | DIFFERENT | yes (HVP obtainable two independent ways) | [WP25, arXiv:2505.21476](https://arxiv.org/abs/2505.21476) |
| 6 | Hadronic vacuum polarisation | Lattice QCD (BMW) vs dispersive e⁺e⁻ R-ratio; also CMD-3 vs BaBar/KLOE | "new muon g−2 puzzle" (2021→) | 2020→open, 6 yr | OPEN | — | DIFFERENT | no | [arXiv:2112.08312](https://arxiv.org/abs/2112.08312) |
| 7 | Hubble constant H₀ | Cepheid+SNIa distance ladder (SH0ES) vs Planck CMB+ΛCDM | >5σ (2021-25) | 2013→open, 13 yr | OPEN | — | DIFFERENT | partially | [arXiv:2606.20434](https://arxiv.org/html/2606.20434) |
| 8 | Hubble constant H₀ ("Hubble Wars") | Sandage best-candle ladder (~50) vs de Vaucouleurs spread-the-risk ladder (~100) | factor of 2; no σ stated | ~1975→2001, 26 yr | SYSTEMATICS | Both calibrations; HST Key Project landed at 72±8 between them | SAME | no | [arXiv:2308.02474](https://arxiv.org/pdf/2308.02474) |
| 9 | S₈ / σ₈ | Cosmic shear (KiDS, DES, HSC) vs Planck CMB | ~2-3σ (2020-23) | 2013→2025, 12 yr | SYSTEMATICS | Earlier weak-lensing analyses; KiDS-Legacy now 0.73-1.01σ from Planck, a 2.2σ reduction | DIFFERENT | no | [arXiv:2503.19442](https://arxiv.org/pdf/2503.19442) |
| 10 | Primordial B-mode amplitude r | BICEP2 150 GHz vs Planck 353 GHz dust polarisation | r=0.20 claimed (2014) | 2014→2015, 1 yr | SYSTEMATICS | BICEP2 — polarised galactic dust foreground | DIFFERENT | yes | [arXiv:1405.5857](https://arxiv.org/abs/1405.5857) |
| 11 | Solar neutrino flux | Radiochemical (Homestake, GALLEX/SAGE) + water Cherenkov vs Standard Solar Model | factor ~3 deficit | 1968→2002, 34 yr | **NEW-PHYSICS** | Neither measurement — the no-flavour-change assumption | DIFFERENT | **yes (SNO NC/CC ratio in one detector)** | [arXiv:hep-ph/0204253](https://arxiv.org/pdf/hep-ph/0204253) |
| 12 | Neutrino time-of-flight | OPERA timing vs SN1987A / ICARUS / relativity | 6σ (2011) | 2011→2012, 0.8 yr | SYSTEMATICS | OPERA — loose fibre-optic connector on the GPS timing chain | DIFFERENT | yes | [Physics World](https://physicsworld.com/a/doubts-grow-over-superluminal-neutrino-result/) |
| 13 | 750 GeV diphoton rate | ATLAS 2015 vs ATLAS 2016; CMS 2015 vs CMS 2016 | 3.9σ local ATLAS, 3.4σ CMS (2015) | 2015→2016, 0.7 yr | SYSTEMATICS † | Neither — statistical fluctuation (see schema note) | SAME | no | [arXiv:1605.09401](https://arxiv.org/pdf/1605.09401) |
| 14 | Θ⁺(1540) pentaquark | LEPS/DIANA/CLAS/SAPHIR low-statistics vs CLAS & JLab high-statistics repeats | 5.3±0.5σ (CLAS, 2003) | 2003→2006, 3 yr | SYSTEMATICS | The claimants — including the same group on more data | **SAME** | no | [arXiv:nucl-ex/0512042](https://arxiv.org/pdf/nucl-ex/0512042) |
| 15 | X17 boson in ⁸Be/⁴He/¹²C transitions | ATOMKI pair spectrometer vs MEG-II vs PADME | ~6.8σ claimed by ATOMKI | 2016→open, 10 yr | OPEN | — (MEG-II 2025 finds no significant signal; p=6% consistency with ATOMKI) | DIFFERENT | no | [arXiv:2501.05507](https://arxiv.org/abs/2501.05507) |
| 16 | W boson mass | CDF II vs ATLAS/LEP/D0 world average, and vs electroweak fit | 4.0σ vs ATLAS; ~7σ vs SM (2022) | 2022→open, 4 yr | OPEN | — | SAME | yes (global EW fit) | [arXiv:2506.01887](https://arxiv.org/pdf/2506.01887) |
| 17 | R(K), R(K*) lepton universality | LHCb 2014-21 analysis vs LHCb 2022 reanalysis with 5× data | ~3.1σ (2021) | 2014→2022, 8 yr | SYSTEMATICS | LHCb's own earlier analysis — electron ID and misidentified hadronic backgrounds | **SAME** | no | [LHCb outreach, Dec 2022](https://lhcb-outreach.web.cern.ch/2022/12/20/improved-lepton-universality-measurements-show-agreement-with-the-standard-model/) |
| 18 | Dark matter annual modulation in NaI(Tl) | DAMA/LIBRA vs COSINE-100 and ANAIS-112 (same target material) | DAMA claims >9σ modulation; COSINE-100 excludes at >3σ (2024) | 1998→open, 28 yr | OPEN | — (trending against DAMA; 5σ refutation expected from full ANAIS-112) | **SAME** | no | [arXiv:2409.13226](https://arxiv.org/abs/2409.13226), [arXiv:2503.19559](https://arxiv.org/abs/2503.19559) |
| 19 | ν_e appearance excess at short baseline | LSND + MiniBooNE (Cherenkov) vs MicroBooNE (LAr TPC) | 4.8σ MiniBooNE LEE (2018) | 1996→open, 30 yr | OPEN | — | DIFFERENT | no | [arXiv:2201.01724](https://arxiv.org/pdf/2201.01724) |
| 20 | Low-energy electronic recoil rate in Xe | XENON1T vs XENONnT | 3.5σ excess (2020) | 2020→2022, 2 yr | SYSTEMATICS | XENON1T — trace tritium contamination | SAME | no | [XENON1T observes tritium, arXiv:2006.13278](https://arxiv.org/abs/2006.13278) |
| 21 | Pioneer 10/11 anomalous acceleration | Doppler navigation solution vs finite-element thermal model from flight telemetry | no σ stated in sources | 1980→2012, 32 yr | SYSTEMATICS | The navigation analysis — omitted anisotropic thermal recoil | DIFFERENT | yes | [arXiv:1204.2507](https://arxiv.org/abs/1204.2507) |
| 22 | Primordial ⁷Li/H | BBN+CMB baryon density prediction vs metal-poor halo star spectroscopy | factor ~3 | 1982→open, 44 yr | OPEN | — (leading candidate is stellar depletion, i.e. the stars-preserve-Li assumption) | DIFFERENT | yes (CMB Ω_b) | [A&A 2025, cosmological lithium problem](https://www.aanda.org/articles/aa/full_html/2025/09/aa54482-25/aa54482-25.html) |
| 23 | Primordial D/H | Rival quasar-absorber sightlines ("high-D" vs "low-D" camps) | scattered ~order of magnitude; no single σ | ~1994→2014, 20 yr | SYSTEMATICS | Low-quality sightlines and unblinded analyses; fixed by strict target selection + blind analysis | **SAME** | yes (CMB Ω_b) | [arXiv:1710.11129](https://arxiv.org/abs/1710.11129), [arXiv:1308.3240](https://arxiv.org/abs/1308.3240) |
| 24 | Δα/α from quasar absorption | Keck/HIRES (−5.7±1.1 ppm) vs VLT/UVES (+2.29±0.95 ppm) | ~5σ apart from each other | 2001→2014, 13 yr | SYSTEMATICS | Both — long-range wavelength-scale distortions, ±200 m/s per 1000 Å | SAME | no | [arXiv:1409.4467](https://arxiv.org/abs/1409.4467) |
| 25 | Solar interior sound speed / Z/X | Helioseismic inversion vs 3D-spectroscopic abundances in standard solar models | no single σ stated | 2005→open, 21 yr | OPEN | — (suspicion on opacities and mixing below the convection zone) | DIFFERENT | no | [arXiv:2105.01661](https://arxiv.org/pdf/2105.01661) |
| 26 | Excess heat in Pd-D electrolysis | Fleischmann-Pons calorimetry vs replication attempts + nuclear-product detection | no σ stated in sources | 1989→1989/2004, <1 yr to consensus | SYSTEMATICS | The claimants — calorimetry flaws; no nuclear byproducts detected | DIFFERENT | yes | [UC Berkeley Understanding Science case study](https://undsci.berkeley.edu/cold-fusion-a-case-study-for-scientific-behavior/the-smoke-clears/) |
| 27 | Anomalous properties of "polywater" | Capillary-condensed water measurements vs clean-glassware repeats + chemical/EM analysis | no σ stated | 1962→1973, 11 yr | SYSTEMATICS | The claimants — silica and phospholipid contamination | SAME | no | [Science History Institute](https://www.sciencehistory.org/stories/magazine/the-rise-and-fall-of-polywater/) |
| 28 | N-rays | Blondlot's visual scintillation observations vs Wood's prism-removal blind test | no σ stated | 1903→1904, 1 yr | SYSTEMATICS | Blondlot — observer effect; signal persisted with the prism removed | SAME | no | [APS News, Sept 1904](https://www.aps.org/apsnews/2007/08/robert-wood-debunks-nrays) |
| 29 | Composition-dependent "fifth force" | Fischbach reanalysis of Eötvös data vs ~10 new torsion-balance and float experiments | claimed ~1% of gravity | 1986→1990, 4 yr | SYSTEMATICS | The reanalysis; repetitions in different locations and substances were consistently null | DIFFERENT | no | [SEP, The Fall of the Fifth Force](https://plato.stanford.edu/entries/physics-experiment/app4.html) |
| 30 | Electron antineutrino mass | ITEP tritiated-valine + Tretyakov spectrometer vs Zürich and LANL | claimed 17-40 eV "model independent" | 1980→1987, 7 yr | SYSTEMATICS | ITEP — overestimated energy-loss correction, and a wrong ³He-T mass difference | **SAME** (all Tretyakov-type) | yes | [arXiv:0909.2104](https://arxiv.org/pdf/0909.2104) |
| 31 | Element 118 production cross-section | LBNL 1999 claim vs worldwide non-reproduction incl. Berkeley itself | 3 claimed atoms; no σ | 1999→2002, 3 yr | SYSTEMATICS † | The claimant — data found fabricated | SAME | no | [Physics World](https://physicsworld.com/a/element-118-disappears-two-years-after-it-was-discovered/) |
| 32 | Seasonal variation in nuclear decay rates | Jenkins-Fischbach archival power-spectrum analyses vs PTB and metrology repeats | claimed Earth-Sun-distance correlation | 2008→2016, 8 yr | SYSTEMATICS | The claimants — ambient environmental and instrumental effects | DIFFERENT | no | [PTB via ScienceDaily](https://www.sciencedaily.com/releases/2014/10/141010083857.htm) |
| 33 | Reactor antineutrino flux (rate) | Short-baseline IBD rate measurements vs Huber-Mueller conversion prediction | 2.5σ (2011) | 2011→2023, 12 yr | **THEORY-ERROR** | The prediction — Kurchatov conversion and Estienne-Fallot summation models agree with the data | DIFFERENT | yes | [arXiv:2110.06820](https://arxiv.org/abs/2110.06820), [arXiv:2310.13070](https://arxiv.org/abs/2310.13070) |
| 34 | ν_e capture rate on ⁷¹Ga at calibration | GALLEX/SAGE/BEST gallium sources vs reactor rate + spectral + solar constraints | >5σ anomaly (BEST 2022); 4-5σ tension with reactor bounds | 1995→open, 31 yr | OPEN | — | **SAME** (all gallium radiochemical) | yes (reactor/solar) | [arXiv:2209.00916](https://arxiv.org/abs/2209.00916) |
| 35 | Planck constant h / the kilogram | Kibble (watt) balance vs XRCD silicon-sphere Avogadro route | disagreed above stated uncertainties pre-2014 | 2011→2017, 6 yr | **REDEFINITION** | Neither, ultimately — agreement was made a precondition for the 2019 SI | DIFFERENT | yes | [EURAMET: experiments reach agreement](https://www.euramet.org/publications-media-centre/news/news/experiments-to-redefine-the-kilogram-reach-agreement) |
| 36 | Age of the universe | Globular-cluster main-sequence-turnoff ages (16±3 Gyr) vs expansion age (9±2 Gyr) | no σ stated; a stated contradiction | ~1990→1998, 8 yr | SYSTEMATICS ‡ | **Both sides moved**: Hipparcos showed GC distances underestimated (~0.2 mag), *and* Λ was needed | DIFFERENT | yes | [arXiv:astro-ph/9706128](https://arxiv.org/pdf/astro-ph/9706128) |
| 37 | Cosmic magnetic monopole flux | Cabrera SQUID induction single candidate vs all subsequent induction and MACRO/IceCube searches | one flux-quantum event (1982) | 1982→open in the literal sense | **UNRESOLVED-IN-SOURCES** | Sources say "likely experimental error" / "mechanically induced offset" — never definitively diagnosed | SAME then DIFFERENT | no | [arXiv:2605.02869](https://arxiv.org/pdf/2605.02869) |
| 38 | Hydrogen 1S-3S transition frequency | MPQ (Grinin 2020) vs LKB (Fleurbaey 2018) | 2.1σ | 2018→open, 8 yr | OPEN | — CODATA 2022: "The difference between these results is not currently understood" | **SAME** | yes (Rydberg + r_p) | [CODATA 2022, arXiv:2409.03787](https://arxiv.org/pdf/2409.03787) |
| 39 | Dark energy equation of state w₀, wₐ | DESI DR2 BAO + CMB + SNIa vs ΛCDM; also DESI vs DES-SN5YR | ~2.95σ DESI-vs-DES-SN5YR tension | 2024→open, 2 yr | OPEN | — (low-z SN calibration systematics can reduce the preference below significance) | DIFFERENT | no | [arXiv:2602.05368](https://arxiv.org/html/2602.05368) |

† **Schema strain, recorded rather than hidden.** Rows 13 and 31 are classified SYSTEMATICS
because there is no better box, but neither is a systematic error. Row 13 was a *statistical
fluctuation* — nobody made a mistake. Row 31 was *fabrication* — a misconduct case, not a
measurement error. A second pass should add FLUCTUATION and MISCONDUCT as categories, because
lumping them into SYSTEMATICS inflates the "someone measured wrong" fraction by 2/39.

‡ **Row 36 is the mixed case and the most instructive one.** The distance scale was wrong
*and* the cosmological model was wrong. Forcing a single label destroys the finding. At least
one closed case in 24 resolved to both boxes at once, which means the categories are not a
partition of the outcome space.

---

## Selection bias — read this before using the tally

**Four biases operate, and they do not cancel. Three push the same way.**

### 1. Findability bias — pushes SYSTEMATICS *down*, and is the largest effect

A disagreement that quietly evaporated leaves no paper. There is no "we stopped disagreeing"
publication genre. Every row above exists because somebody wrote a resolution document, and
resolution documents are written when the resolution is *interesting* — a real effect, a
dramatic error, a redefinition. The boring case — two labs converge over three years as
techniques improve, nobody publishes on it — is structurally invisible to this method.

**Direction and magnitude.** Almost every invisible case is a SYSTEMATICS case, because that
is what quiet convergence *is*. My honest guess is that the invisible population is at least
as large as the visible one and possibly several times larger; Bailey's 41,000 measurements
contain thousands of 3-5σ disagreements, and 39 of them made it into this table. **If the
invisible population is 5× the visible one and is 90% systematics, the true SYSTEMATICS
fraction rises from 20/25 (80%) to something above 90%, and NEW-PHYSICS falls below 2%.**
This is the single biggest correction and it points one way.

### 2. Fame bias — pushes NEW-PHYSICS *up*

The known-starting-points list I was given is a fame-sorted list, and fame correlates with
dramatic outcome. The solar neutrino problem is on every such list precisely *because* it
resolved to new physics. Its structural twins that resolved to a systematic are not household
names. **This inflates NEW-PHYSICS. The 1/24 in this table is already the ceiling, not the
floor.** Every closed case here was famous enough to have a Wikipedia-tier profile; the
population of unfamous closed cases is far larger and almost certainly more boring.

### 3. Erratum bias — pushes SYSTEMATICS *down* within the visible set

SYSTEMATICS outcomes are announced in errata, internal notes, CODATA footnotes, and
conference talks; NEW-PHYSICS outcomes get a paper, a press release, and a review article.
Concretely in this table: rows 17 (R(K)) and 20 (XENON1T) resolved through a collaboration's
own follow-up publication rather than a paper *about* the discrepancy, and I found row 17's
resolution through an outreach blog post, not the literature. Row 9 (S₈) resolved inside a
survey's own consistency paper. **Any search that indexes on "the X puzzle" as a phrase will
systematically miss cases that died quietly inside a collaboration.** I estimate this cost me
several rows I could not name, all of them SYSTEMATICS.

### 4. Survivorship-into-OPEN bias — pushes the OPEN fraction *up*, spuriously

15 of 39 are OPEN. That is not a property of discrepancies; it is a property of *now*. Open
cases are maximally visible because they are actively worked, actively reviewed, and actively
publicised. Closed-and-forgotten cases have to be excavated. **The OPEN fraction in this
table is an artifact of the sampling date and should be excluded from any base rate
entirely.** The base rate must be computed over closed cases only, and even then only over
closed cases with matched visibility.

### 5. The counter-bias, stated for honesty — pushes SYSTEMATICS *up* spuriously

The pathological-science cases (26-32: cold fusion, polywater, N-rays, fifth force, ITEP,
element 118, decay rates) are over-represented because they are *taught*. They are pedagogic
exemplars, so they are easy to find, and they are all SYSTEMATICS. Seven of 20 SYSTEMATICS
rows are drawn from this teaching canon. Several also barely meet the inclusion rule — cold
fusion and N-rays resolved in months, not years. **Drop the pedagogic canon and the closed
tally becomes 13 SYSTEMATICS / 1 NEW-PHYSICS / 1 THEORY-ERROR / 1 REDEFINITION out of 17.**
The fraction barely moves, which is mildly reassuring, but the sample size collapses.

### Net assessment

Biases 1, 2 and 3 all push the same direction: **the true SYSTEMATICS fraction is higher than
the 83% this table shows, and the true NEW-PHYSICS fraction is lower than the 4%.** Bias 5
pushes the other way but is small and demonstrably does not move the ratio. Bias 4 means the
OPEN column carries no information about outcomes at all.

**The honest statement this catalogue supports is directional, not numerical:** persistent
inter-method disagreements resolve to systematics far more often than to new physics, and the
observed ratio understates it. Any specific fraction quoted from this table is an
overestimate of the new-physics rate by an unknown factor greater than one.

### A sixth bias, discovered while building this table: outcomes move after they are recorded

Row 5 was drafted as OPEN at 5.1σ on the strength of the 2020 White Paper, and had to be
re-classified THEORY-ERROR after fetching WP25, which reports no tension at all. Nothing
announced this. The prediction moved onto the measurement because the e⁺e⁻ data stopped
combining and lattice QCD was adopted instead. **A resolution that happens by a change of
input convention leaves no resolution paper**, and a catalogue built even a year stale would
have coded this case wrongly and confidently. The same hazard runs the other way: the reactor
antineutrino anomaly (row 33) was declared closed around 2021 and has since been partially
revived. **Outcome labels have a shelf life, and any base rate built on them needs a
recorded as-of date.** This one is 2026-09-03.

### One structural finding that is *not* bias-limited

The catalogue independently confirms feature 1 from [[G9-discrepancy-base-rate]]. **Every
closed SAME-CLASS case in this table resolved to systematics — rows 14, 17, 23, 27, 28, 30,
31 — with no exceptions.** Not one same-class disagreement resolved to new physics. That
finding does not depend on the denominator, because it is a statement about a conditional
with no surviving counterexample. It is the strongest thing here, and it is exactly what makes
[[fine-structure-discrepancy]] (row 2, SAME-CLASS, 5.4σ, open) predictable rather than
interesting.

---

## What a less-biased sample would require

The bias analysis names five defects. Four are fixable, and each fix is a specific, runnable
piece of work on public data.

1. **A denominator that is not fame-selected.** Sample discrepancies from a *register*, not
   from memory or a puzzle list. Two exist: successive CODATA adjustment input tables (every
   input that was down-weighted or expanded is a logged disagreement, whether or not anyone
   wrote about it), and BIPM/CIPM key comparison reports (every key comparison with a
   nonzero degrees-of-equivalence outlier is a logged inter-method disagreement, and the
   subsequent comparison round records what happened to it). Both publish the boring cases,
   which is exactly what this table cannot reach.

2. **Prospective cohort framing, not retrospective.** Fix a cutoff year — say 2000 — take
   *every* disagreement above 3σ flagged in that year's Particle Data Group and CODATA
   inputs, and follow all of them forward. This eliminates findability bias by construction,
   because the cohort is defined before the outcome is known. It is the only design that
   produces a real base rate, and every input is public.

3. **A search protocol that catches quiet deaths.** Do not search on "the X puzzle". Search
   forward from the *claiming* paper's citation graph and check whether the claim's central
   value moved, using the tools in [[citation-sources]]. A discrepancy that died quietly
   shows up as a value drift with no accompanying announcement.

4. **Closed cases only, with matched visibility.** Exclude all OPEN rows from the fraction.
   Then stratify closed cases by a visibility proxy — citation count of the original claim,
   or presence of a dedicated review article — and check whether the outcome fraction
   differs across strata. If it does, the bias is measured rather than argued, and can be
   corrected for.

5. **A wider category schema.** Add FLUCTUATION and MISCONDUCT, and permit multi-label
   outcomes. Three rows here (13, 31, 36) are mislabelled by force. Three of 39 is 8% of the
   sample distorted by the instrument.

The unfixable defect is the genuinely unrecorded disagreement — two labs who never published
their mutual inconsistency. Nothing recovers those, and their existence is the reason the
base rate, even done properly, will be a lower bound on the systematics fraction.
