# Scout: astrobiology

All DOIs below were resolved live through Crossref (`api.crossref.org/works/<doi>?mailto=deciduusleaf@gmail.com`)
on **2026-09-05**; `cited_by` figures are Crossref `is-referenced-by-count`, same fetch. All
citer-set intersections were run on **OpenAlex** server-side `cites:` filters
(`api.openalex.org/works?filter=cites:<W_A>,cites:<W_B>`), same date, except where marked.
**Flux numbers are not in this report.** Every one of them requires a full-text read, and this
project's rule is that an unfetched number is not a number. What is here is the *skeleton* of the
enumeration with the paper that bounds each row and its verified DOI — the audit's step-3 list,
not its step-6 arithmetic.

## Summary (5 lines)

1. **The right Job-1 case is Venus phosphine, and it is a control, not a discovery.** It is the
   only biosignature case where the field has already published a near-exhaustive abiotic-source
   enumeration with flux bounds (Bains et al. 2021, `10.1089/ast.2020.2352`) — which is exactly
   what makes it the reservoir audit's Pioneer: a hard case with a known published answer to be
   recovered, not invented.
2. **Venus also delivers, for free, the negative control the audit has never had.** The detection
   itself is disputed to the point of non-detection (`10.1051/0004-6361/202039717`,
   `10.1038/s41550-021-01422-z`, `10.3847/2041-8213/abde47`, `10.1029/2022GL101055`), so the
   observable leg fires the missing **step 0** that `reservoir-audit` Part D.2 predicts on a
   *fabricated* input. Running D.2 on a real case is strictly better than running it on a mock-up.
3. **K2-18b is the case the audit should publicly refuse to run.** Taylor 2025
   (`10.3847/2515-5172/add881`) and Luque et al. 2025 (`10.1051/0004-6361/202555580`) put the DMS/DMDS
   features at or below the noise; the correct output is `NO OBSERVABLE TO EXPLAIN`, and saying so is
   more valuable to this project's reputation than an enumeration would be. Mars methane is the one
   genuinely **open** residual, and its residual is a *sink*, not a source.
4. **Six gap candidates measured; one is dead on arrival and one fails its own null model.**
   Landauer × England returns 45 co-citers (joined literature — kill it). Spores × Kirkwood returns a
   spectacular zero at the union floor that collapses to `E = 0.28` at any defensible field-scale `N`
   (uninformative — the project's own G6 lesson).
5. **The strongest gap by a distance is biosignature assessment × diagnostic-test theory:**
   Catling et al. 2018 × Hanley & McNeil 1982 = **0** co-citers, `E = 30.8` at a fetched
   `N = 152,971`, with the Bayes-factor control firing at 4. The field does Bayesian *model
   comparison* and has never touched sensitivity/specificity, base rates, or ROC.

---

## Job 1: specification-instrument target

### The pick, and the ranking that produced it

| Case | Observable survives step 0? | Enumeration published? | Residual open? | Verdict |
|---|---|---|---|---|
| **Venus PH₃** | **No** — three independent reanalyses drive it toward zero | **Yes, near-exhaustive** | Conditional residual open ("unsolved problem", `10.3389/fspas.2024.1372057`) | **RUN FIRST — hard-positive + real negative control** |
| **Mars CH₄** | Marginal — Curiosity in-situ vs TGO non-detection | Partial, scattered | **Yes, and the residual is a *sink*** | Run second — the open case |
| **K2-18b DMS/DMDS** | **No** — features consistent with noise | No | n/a | Run as a 2-hour `NO OBSERVABLE` demonstration only |
| Generic O₂+CH₄ | n/a (no single system) | Yes, but as a review literature | Not a case, a framework | Feeds Job-2 gap G-A, not Job 1 |

**Pick: Venus phosphine.** Reasons, adversarially: it is *not* the exciting choice, and that is the
point. It is the only case where the audit can be scored. If the audit cannot reproduce Bains 2021's
enumeration and its conclusion, the audit has no business being aimed at Mars methane, exactly as
`reservoir-audit` says an instrument that cannot reproduce Pioneer has no business being aimed at a
flyby.

### (a) Primary papers — DOIs verified via Crossref, 2026-09-05

**Venus PH₃ — the claim**

| Role | Paper | DOI | Year / venue | cited_by |
|---|---|---|---|---|
| Claim | Greaves et al., *Phosphine gas in the cloud decks of Venus* | `10.1038/s41550-020-1174-4` | 2020, Nat Astron | 255 |
| Claim, addendum | Greaves et al., *Addendum: Phosphine gas in the cloud deck of Venus* | `10.1038/s41550-021-01423-y` | 2021, Nat Astron | 22 |
| Enumeration | Bains et al., *Phosphine on Venus Cannot Be Explained by Conventional Processes* | `10.1089/ast.2020.2352` | 2021, Astrobiology | 72 |

**Venus PH₃ — the rebuttals and reanalyses**

| Role | Paper | DOI | Year / venue | cited_by |
|---|---|---|---|---|
| Reanalysis (pipeline) | Snellen et al., *Re-analysis of the 267 GHz ALMA observations of Venus* | `10.1051/0004-6361/202039717` | 2020, A&A | 59 |
| Reanalysis (independent) | Villanueva et al., *No evidence of phosphine in the atmosphere of Venus from independent analyses* | `10.1038/s41550-021-01422-z` | 2021, Nat Astron | 81 |
| Misidentification | Lincowski et al., *Claimed detection of PH₃ … is consistent with mesospheric SO₂* | `10.3847/2041-8213/abde47` | 2021, ApJL | 56 |
| Independent upper limit | Cordiner et al., *Phosphine in the Venusian atmosphere: a strict upper limit from SOFIA GREAT* | `10.1029/2022GL101055` | 2022, GRL | 34 |
| Source problem, still open | *Source of phosphine on Venus — An unsolved problem* | `10.3389/fspas.2024.1372057` | 2024, Front Astron Space Sci | 12 (OpenAlex) |

**K2-18b DMS/DMDS — for the refusal demo**

| Role | Paper | DOI | Year / venue | cited_by |
|---|---|---|---|---|
| Claim (NIRISS/NIRSpec) | Madhusudhan et al., *Carbon-bearing Molecules in a Possible Hycean Atmosphere* | `10.3847/2041-8213/acf577` | 2023, ApJL | 284 |
| Claim (MIRI) | Madhusudhan et al., *New Constraints on DMS and DMDS … from JWST MIRI* | `10.3847/2041-8213/adc1c8` | 2025, ApJL | 74 |
| Rebuttal (features) | Taylor, *Are There Spectral Features in the MIRI/LRS Transmission Spectrum of K2-18b?* | `10.3847/2515-5172/add881` | 2025, RNAAS | 14 |
| Rebuttal (evidence) | Luque et al., *Insufficient evidence for DMS and DMDS in the atmosphere of K2-18 b* | `10.1051/0004-6361/202555580` | 2025, A&A | 27 |
| Reanalysis | Schmidt et al., *A Comprehensive Reanalysis of K2-18 b's JWST NIRISS+NIRSpec Transmission Spectrum* | `10.3847/1538-3881/ae019a` | 2025, AJ | 34 |
| Alternative interior | Wogan et al., *JWST Observations of K2-18b Can Be Explained by a Gas-rich Mini-Neptune with No Habitable Surface* | `10.3847/2041-8213/ad2616` | 2024, ApJL | 101 |
| Alternative (aerosols) | *Investigating aerosols as a way to reconcile K2-18 b JWST MIRI and NIRISS/NIRSpec observations* | `10.1051/0004-6361/202556905` | 2025, A&A | 7 |
| **Abiotic DMS** | *Abiotic Production of Dimethyl Sulfide, Carbonyl Sulfide, and Other Organosulfur Gases via Photochemistry* | `10.3847/2041-8213/ad74da` | 2024, ApJL | 17 |
| **Abiotic DMS, in situ** | Hänni et al., *Evidence for Abiotic Dimethyl Sulfide in Cometary Matter* | `10.3847/1538-4357/ad8565` | 2024, ApJ | (OpenAlex W4403444475) |

**Mars CH₄ — for the open case**

| Role | Paper | DOI | Year / venue | cited_by |
|---|---|---|---|---|
| Claim (seasonal) | Webster et al., *Background levels of methane in Mars' atmosphere show strong seasonal variations* | `10.1126/science.aaq0131` | 2018, Science | 253 |
| Non-detection | Korablev et al., *No detection of methane on Mars from early ExoMars TGO observations* | `10.1038/s41586-019-1096-4` | 2019, Nature | 153 |
| Seasonality disputed | Gillen et al., *Statistical analysis of Curiosity data shows no evidence for a strong seasonal cycle of martian methane* | `10.1016/j.icarus.2019.113407` | 2019, Icarus | 25 (OpenAlex) |
| Diurnal containment | Webster et al., *Day–night differences in Mars methane suggest nighttime containment at Gale crater* | `10.1051/0004-6361/202040030` | 2021, A&A | 50 (OpenAlex) |
| Sink/lifetime problem | Yung et al., *Methane on Mars and Habitability: Challenges and Responses* | `10.1089/ast.2018.1917` | 2018, Astrobiology | 102 (OpenAlex) |
| Abiotic: seepage | Etiope & Oehler, *Methane Seepage on Mars: Where to Look and Why* | `10.1089/ast.2017.1657` | 2017, Astrobiology | 106 (OpenAlex) |
| Abiotic: UV on meteoritic organics | *Methane from UV-irradiated carbonaceous chondrites under simulated Martian conditions* | `10.1029/2011je004023` | 2012, JGR Planets | 47 (OpenAlex) |
| Abiotic: cometary delivery | *A cometary origin for martian atmospheric methane* | `10.7185/geochemlet.1602` | 2015, Geochem Persp Let | 34 (OpenAlex) |
| Microseepage flux bound | *The Methane Diurnal Variation and Microseepage Flux at Gale Crater* | `10.1029/2019gl083800` | 2019, GRL | 49 (OpenAlex) |

**The framework anchors for the generic disequilibrium argument**

| Paper | DOI | Year | note |
|---|---|---|---|
| Krissansen-Totton et al., *Disequilibrium biosignatures over Earth history and implications for detecting exoplanet life* | `10.1126/sciadv.aao5747` | 2018, Sci Adv | Crossref cited_by 166 |
| Catling et al., *Exoplanet Biosignatures: A Framework for Their Assessment* | `10.1089/ast.2017.1737` | 2018, Astrobiology | OpenAlex N_citers = 215 |
| Meadows, *Reflections on O₂ as a Biosignature in Exoplanetary Atmospheres* | `10.1089/ast.2016.1578` | 2017, Astrobiology | O₂ false-positive canon |

### (b) The enumeration — Venus PH₃

The identity that plays the role of `P_total = −F·Δu` is the **steady-state mass balance of a
trace gas in a well-mixed atmospheric layer**:

```
S  =  L  =  n(PH3) · V_layer / tau_chem          (production = loss at steady state)
A_i  =  S_required / S_i,max                     (availability ratio for abiotic route i)
A_i > 1  =>  route i RULED OUT
```

`S` is a molecular flux (molecules cm⁻² s⁻¹, convertible to mol/yr); `tau_chem` is the photochemical
lifetime; the *aperture* of `reservoir-audit` step 5 becomes the **assumed mixing volume and the
assumed lifetime**, and the mandatory 2×/0.5× sensitivity line runs on `tau_chem`, which is the single
most contested number in the case (`10.1051/0004-6361/202142548`).

**Candidate abiotic reservoirs, with the paper that bounds each.** Flux column deliberately left as
`EXTRACT` — Bains 2021 tabulates them and the read has not been done:

| # | Abiotic route | Bounding paper | DOI | Flux bound |
|---|---|---|---|---|
| 1 | Atmospheric photochemistry (H/P radical chains in the cloud deck) | Bains 2021 | `10.1089/ast.2020.2352` | EXTRACT |
| 2 | Lightning / electrical discharge | Bains 2021 | `10.1089/ast.2020.2352` | EXTRACT |
| 3 | Volcanic outgassing of PH₃ directly | Bains 2021 | `10.1089/ast.2020.2352` | EXTRACT |
| 4 | **Volcanic phosphide (P³⁻) extrusion, then hydrolysis** — the strongest abiotic proposal | Truong & Lunine 2021 | `10.1073/pnas.2021689118` | EXTRACT (implies an eruption rate) |
| 5 | Same route, rebutted on the required eruption rate | Bains et al. 2022 | `10.1073/pnas.2121702119` | EXTRACT — this is the paper that *converts* route 4 into a specification ("only extraordinary volcanism") |
| 6 | Meteoritic / cometary delivery of reduced phosphorus | Bains 2021 | `10.1089/ast.2020.2352` | EXTRACT |
| 7 | Mineral–acid surface reactions (phosphide-bearing rock + H₂SO₄) | Bains 2021 | `10.1089/ast.2020.2352` | EXTRACT |
| 8 | Corona / UV-driven aqueous chemistry in droplets | Bains 2021 | `10.1089/ast.2020.2352` | EXTRACT |
| 9 | Triboelectric / dust processes | Bains 2021 | `10.1089/ast.2020.2352` | EXTRACT |
| 10 | **`tau_chem` inflation** — not a source but an aperture change: a longer lifetime lowers required `S` | *Uncertainty in phosphine photochemistry…* | `10.1051/0004-6361/202142548` | EXTRACT |
| 11 | **The observable is SO₂, not PH₃** — the `NOT FORMABLE` row: if the line is misidentified there is no flux to supply | Lincowski 2021 | `10.3847/2041-8213/abde47` | n/a |
| 12 | **The observable is a baseline-fitting artefact** — the step-0 row | Snellen 2020; Villanueva 2021 | `10.1051/0004-6361/202039717`; `10.1038/s41550-021-01422-z` | n/a |
| 13 | Proposed *microbial* metabolisms, tested and failed on the same ledger | Bains et al. 2022 (Nat Commun) | `10.1038/s41467-022-30804-8` | EXTRACT — this rules out the *biotic* row too |

Row 13 is the row this project should be loudest about: the same bookkeeping that excludes abiotic
routes also excludes the proposed *biotic* ones. A specification instrument that returns "no known
partner, biotic or abiotic" is doing its job; a press release that returns "life" is not.

### (c) The residual specification

Written in `C11` shape, and conditional on the observable surviving step 0:

> **Of the reservoirs considered, if PH₃ is present at ~1–5 ppb in the Venusian cloud deck, none of
> routes 1–9 supplies the required source flux `S_req = n·V/tau_chem` at the nominal mixing volume and
> nominal `tau_chem`. The residual is a specification: a source delivering `S_req` mol/yr of PH₃ (or of
> a P³⁻-bearing precursor at the stoichiometric equivalent), spatially confined to the 50–60 km cloud
> layer, and — from routes 4/5 — implying a phosphide extrusion rate ≥ X× the nominal Venusian volcanic
> rate.**
>
> **The discriminating observable is not more PH₃.** It is (i) the **vertical profile** — a
> photochemical, a surface and a cloud-layer source put PH₃ in different places — and (ii) the
> phosphorus-bearing companion-species inventory (P₂H₄, P₄, PO). In-situ mass spectrometry on a descent
> probe discriminates; more sub-mm spectroscopy at 266.94 GHz does not, because 266.94 GHz is exactly
> where the SO₂ degeneracy (row 11) lives.

And, decisively: **run honestly, the audit's actual top-line output on Venus is the step-0 halt.**
`NO OBSERVABLE TO EXPLAIN` — because three independent reanalyses put the line at or below the
noise. Everything above is the *conditional* branch, and it must be labelled conditional in the
note or the note is dishonest.

### (d) Hours to run fully

| Stage | Hours |
|---|---|
| Step-0 leg: read Snellen, Villanueva, Lincowski, Cordiner; state the observable's significance and its uncertainty | 3–4 |
| Read Bains 2021 in full and extract the ~9 route rows with their flux bounds | 6–8 |
| Read Truong & Lunine 2021 + Bains 2022 (the volcanism pair) and extract the required eruption rate | 2–3 |
| Aperture step: `tau_chem` at 2× and 0.5×, per route; the mandatory sensitivity line | 2–3 |
| Write-up in C11 shape + a `vault/gaps/G31` note + lint | 3–4 |
| **Total** | **16–22 h** |

Mars methane, if run after: **12–16 h**. The K2-18b `NO OBSERVABLE` demo: **2–3 h**, and it is the
cheapest high-value item in this whole report.

### (e) Closed or open — honestly

**The detection is closed against the claim; the source problem is open; and those are two
different objects.** Precisely:

- **Closed:** the 2020 ALMA 266.94 GHz feature. Snellen's re-reduction, Villanueva's independent
  reduction, Lincowski's SO₂ degeneracy, and Cordiner's SOFIA upper limit are four independent lines,
  three of them from different instruments or pipelines. By `reservoir-audit` F6 / METHOD §5
  (single-group claims resolve against the claimant), this is resolved.
- **Open:** *if* PH₃ is ever confirmed at ppb level, no known abiotic route supplies it — and the
  field says so in its own words as recently as 2024 (`10.3389/fspas.2024.1372057`).

So Venus is a **hard-positive control with a genuine step-0 negative attached** — the most useful
single input the reservoir audit could be given right now, precisely because it is *not* going to
produce a discovery. That is what the instrument is for.

---

## Job 2: ranked gap candidates

### The table

Provider **OpenAlex**, endpoint `works?filter=cites:<W_A>,cites:<W_B>&per-page=1`, fetched
**2026-09-05**. `E` at the union floor `N = N_A + N_B − ∩` (the smallest defensible `N`, which
*flatters* the gap and must never be quoted alone), plus a fetched concept-scoped `N` where one is
defensible.

| # | Candidate | Anchor A | Anchor B | N_A | N_B | ∩ | N floor | E floor | fetched N | E@N | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **G-E** | biosignature false positives ↔ diagnostic-test theory | Catling 2018 `10.1089/ast.2017.1737` | Hanley & McNeil 1982 `10.1148/radiology.143.1.7063747` | 215 | 21,924 | **0** | 22,139 | 212.9 | **152,971** | **30.8** | **live, strongest** |
| **G-A** | Σ (C8) ↔ planetary redox free-energy budget | Krissansen-Totton 2018 `10.1126/sciadv.aao5747` | Hoehler & Jørgensen 2013 `10.1038/nrmicro2939` | 170 | 800 | **0** | 970 | 140.2 | **36,725** | **3.70** | **live, modest E** |
| **G-D** | continuously-habitable duration ↔ reliability survival function | Kasting 1993 `10.1006/icar.1993.1010` | Weibull 1951 `10.1115/1.4010337` | 2,538 | 11,502 | **0** | 14,040 | 2,079.2 | **921,015** | **31.7** | live, metaphor risk high |
| **G-F** | chemiosmosis / PMF ↔ Kedem–Caplan degree of coupling | Lane & Martin 2012 `10.1016/j.cell.2012.11.050` | Kedem & Caplan 1965 `10.1039/tf9656101897` | 454 | 407 | **0** | 861 | 214.6 | not fetched | 1.85 @10⁵ | live, fragile null |
| **G-C** | availability/repair (C1/C6) ↔ spore dormancy vs radiation damage | Nicholson 2000 `10.1128/mmbr.64.3.548-572.2000` | Kirkwood 1977 `10.1038/270301a0` | 2,024 | 1,969 | **0** | 3,993 | 998.1 | **14,071,245** | **0.28** | **fails its own null model** |
| **G-B** | energy per bit (G8/G25) ↔ self-replicator free energy | Landauer 1961 `10.1147/rd.53.0183` | England 2013 `10.1063/1.4818538` | 4,970 | 427 | **45** | 5,352 | 396.5 | — | — | **not a gap — joined** |
| **G-G** | detection significance ↔ look-elsewhere / trials factor | Madhusudhan 2023 `10.3847/2041-8213/acf577` | Gross & Vitells 2010 `10.1140/epjc/s10052-010-1470-8` | 229 (OC) | **0 (OC)** | — | — | — | — | **NOT MEASURED** |

**Controls run (denominator-invariant `O/|B|` comparison):**

| Pair | ∩ | O/\|B\| |
|---|---|---|
| G-E control: Catling 2018 × Kass & Raftery 1995 `10.1080/01621459.1995.10476572` | **4** / 12,461 | 3.2×10⁻⁴ |
| G-E gap: Catling 2018 × Hanley & McNeil | 0 / 21,924 | 0 |
| G-A control: KT 2018 × Amend & Shock 2001 `10.1111/j.1574-6976.2001.tb00576.x` | **1** / 765 | 1.3×10⁻³ |
| G-A gap: KT 2018 × Hoehler & Jørgensen | 0 / 800 | 0 |

The control ratio is formally infinite on both (gap side is zero), which is *less* impressive than it
looks and is stated here as a weakness, not a headline — see the adversarial notes per candidate.

---

### G-E — biosignature false positives ↔ diagnostic-test theory  **[rank 1]**

- **Anchors.** A: Catling, Krissansen-Totton, Kiang et al. 2018, *Exoplanet Biosignatures: A Framework
  for Their Assessment*, `10.1089/ast.2017.1737`. B: Hanley & McNeil 1982, *The meaning and use of the
  area under a receiver operating characteristic (ROC) curve*, `10.1148/radiology.143.1.7063747`.
- **Same-object argument.** Both fields compute **P(life | signal)** from **P(signal | life)**,
  **P(signal | no life)** and a prior. Astrobiology writes this as a Bayesian network over
  "false-positive scenarios" and reports a posterior; clinical epidemiology writes the identical
  quantity as **positive predictive value** from sensitivity, specificity and prevalence, and has a
  century of machinery for the part astrobiology has not built: **operating points, the
  sensitivity/specificity trade-off curve, and the base-rate correction.** Same three numbers, same
  identity, all dimensionless — commensurable by construction.
- **Metaphor risk: MODERATE, and it is specifically the risk of a vocabulary artifact.** Astronomers do
  Bayesian inference constantly — they cite Trotta, Skilling, `MultiNest`, Kass & Raftery, not
  *Radiology*. The zero against Hanley & McNeil may measure a **citation-community boundary** rather
  than a conceptual absence. **What bears on this:** the control already helps — Catling × Kass &
  Raftery is only **4**, i.e. even the astro-native model-comparison canon is barely read by this set.
  The remaining test is whether any of the 215 citers states a **base rate** (a prior on the fraction of
  planets bearing life) *numerically*, or names an operating point. If none does, the gap is real and it
  is about the **base-rate correction**, not about Bayes.
- **Intersection.** N_A = 215, N_B = 21,924, ∩ = **0**. Union floor `N = 22,139`, `E = 212.9`.
  Fetched `N` = 152,971 (OpenAlex `concepts.id:C163479331|C58471807,from_publication_date:2018-01-01`,
  2026-09-05), `E = 30.8`. `E > 1` at both denominators, so **the zero is a finding at both** — the
  property G6 needed and G-C below lacks. No hits to inspect (∩ = 0). **The four control hits were
  inspected:** *Evaluating Biosignatures for Life Detection* (`10.1089/ast.2019.2151`),
  *Deconstructing Alien Hunting* (`10.3847/1538-3881/ad0cbe`), `10.3847/1538-3881/ada384`
  (interior convection / predicted CO₂), `10.1093/mnras/stad2822` (Twinkle / LTT 1445 Ab) — all four
  are astro-native Bayesian model comparison; **none** is diagnostic-test theory. That is the
  substantive confirmation.
- **What would close it.** Read the 215 Catling citers for any numeric prior/base rate or stated
  operating point. Then compute, for one published biosignature claim (K2-18b DMS is the obvious one),
  the **positive predictive value** as a function of assumed prevalence, and report the prevalence at
  which a 3σ detection is more likely false than true. Checkable, on public data, in a desk session.
- **Instrument extended.** `information-audit` and `Q7-same-class-prediction` — G-E is the same
  Clopper–Pearson / base-rate posture `specification-instruments` already applied to this project's own
  record, pointed outward. Also the natural home for `positive-controls`.

### G-A — Σ (C8) ↔ planetary redox-disequilibrium free-energy budget  **[rank 2]**

- **Anchors.** A: Krissansen-Totton, Olson & Catling 2018, `10.1126/sciadv.aao5747`. B: Hoehler &
  Jørgensen 2013, *Microbial life under extreme energy limitation*, `10.1038/nrmicro2939`. Secondary
  B-side canon for pooling: Amend & Shock 2001 `10.1111/j.1574-6976.2001.tb00576.x`; Hoehler 2007
  *A "Follow the Energy" Approach for Astrobiology* `10.1089/ast.2007.0207`.
- **Same-object argument.** Krissansen-Totton computes the **available Gibbs free energy of a
  planetary atmosphere–ocean system** (J per mole of atmosphere) — the numerator of a whole-planet
  power budget. Hoehler & Jørgensen compute the **power a chemolithotroph actually harvests from a
  redox couple** (W per cell, plus the maintenance-power floor below which life cannot persist). These
  are the two ends of exactly the C8 ratio under the substitution `F·Δu → J_redox · ΔG` — a genuine
  bilinear flux–force product in the Onsager sense, which is the form C8 §1 established. `Σ ∈ [0,1]`
  is then a check, not a model.
- **Metaphor risk: LOW.** Both sides are in J and W and both name the same reservoir pair (oxidant and
  reductant). The cleanest same-object case in the list, and `audits/05` item 18 already names it.
- **Intersection.** N_A = 170, N_B = 800, ∩ = **0**. Union floor `N = 970`, `E = 140.2`. Fetched
  `N` = 36,725 (`concepts.id:C163479331|C100206155,from_publication_date:2018-01-01`, 2026-09-05),
  `E = 3.70` — above 1, so the zero survives, but by a modest margin and it will **not** survive a 10×
  denominator. **Report both rows or do not report it.** Control KT × Amend & Shock = **1**, inspected:
  *Nitrogen Oxide Concentrations in Natural Waters on Early Earth* (`10.1029/2018gc008082`) — a
  geochemistry paper, not a bioenergetics one, so the control is weak and the note must say so.
- **What would close it.** Form Σ for one named chemolithotroph on one named redox couple with
  published `ΔG` and cell-specific rate (the anaerobic-methanotroph and sulfate-reducer literatures
  both have them), then place it on the C8 table beside the albatross and the sail. If `Σ ∈ [0,1]` with
  its reservoir pair named, C8 extends from momentum to chemical potential with the identity intact. If
  it does not, that is the more interesting result.
- **Instrument extended.** `C8-momentum-harvesting-metric` directly; `reservoir-audit` by supplying a
  second conserved quantity (chemical free energy) for the availability leg — which is also what Job 1
  needs.

### G-D — continuously habitable duration ↔ reliability survival function  **[rank 3]**

- **Anchors.** A: Kasting, Whitmire & Reynolds 1993, `10.1006/icar.1993.1010`. B: Weibull 1951,
  `10.1115/1.4010337`. Data-bearing companion on the A side: Rushby et al. 2013, *Habitable Zone
  Lifetimes of Exoplanets around Main Sequence Stars*, `10.1089/ast.2012.0938` (Crossref cited_by 82).
- **Same-object argument.** "Continuously habitable zone duration" is a **first-passage time**: the
  time until a planet's insolation leaves a bounded interval. Reliability's `S(t)` is the same object,
  and the Weibull shape β separates memoryless exit (β ≈ 1) from accelerating exit (β > 1) — exactly the
  mean-vs-distribution asymmetry C18 identified in enzymes and `audits/05` flagged in ecological
  resilience. Astrobiology reports **mean HZ lifetime in Gyr** and never a hazard function.
- **Metaphor risk: HIGH — this is the candidate most likely to be a metaphor.** MTBF presupposes a
  *repairable* item and a failure *event*; a planet leaving the HZ is a deterministic trajectory, not a
  stochastic failure. The gap survives only if the randomness is real — and it is, but it lives in the
  **population** (stellar mass, metallicity, orbital-distance distributions), not in the individual
  planet. The legitimate object is therefore the survival function of a *population* of HZ residence
  times, and the note must say that or it is metaphor.
- **Intersection.** N_A = 2,538, N_B = 11,502, ∩ = **0**. Union floor `N = 14,040`, `E = 2,079.2`.
  Fetched `N` = 921,015 (`concepts.id:C163479331|C200601418,from_publication_date:1993-01-01`,
  2026-09-05), `E = 31.7` — the zero survives a nearly-million-work denominator, the most robust null
  in the table. No hits to inspect.
- **What would close it.** Take Rushby 2013's published HZ-lifetime distribution (or recompute from a
  public stellar catalogue), fit a Weibull, report β with its CI. β ≈ 1 versus β > 1 is a real,
  checkable, previously unstated discriminator about whether "continuous habitability" is memoryless.
- **Instrument extended.** `C18` (the Weibull-β axis) — and it would give C18 its first non-terrestrial
  row.

### G-F — chemiosmosis / proton-motive force ↔ Kedem–Caplan degree of coupling  **[rank 4]**

- **Anchors.** A: Lane & Martin 2012, *The Origin of Membrane Bioenergetics*,
  `10.1016/j.cell.2012.11.050`. B: Kedem & Caplan 1965, `10.1039/tf9656101897`.
- **Same-object argument.** The proton-motive force `Δp` times the proton flux `J_H+` is a bilinear
  flux–force product; the alkaline-vent origin-of-life argument is precisely that a *natural* proton
  gradient across an inorganic membrane can drive carbon fixation. Kedem & Caplan's `q` is the exact
  figure of merit for that converter class, and C8 §1 already established where `q` does and does not
  generalise. Origin-of-life bioenergetics has never written `q` for a vent.
- **Metaphor risk: LOW on the object, HIGH on the utility.** C8 showed `q` fails to generalise when the
  coefficients are not constants. A vent gradient is near-linear-response, so `q` probably *does* form
  here — which would make this the one place the project shows `q` working after showing where it
  fails. Satisfying, but small.
- **Intersection.** N_A = 454, N_B = 407, ∩ = **0**. Union floor `N = 861`, `E = 214.6`. **No
  concept-scoped `N` was fetched** (OpenAlex 429'd late in the session); at `N = 10⁵` `E = 1.85` and at
  `N = 10⁶` `E = 0.18`. **This null is fragile and is not quotable until a defensible `N` is fetched.**
- **What would close it.** Fetch the `N`. Then compute `q` for one published alkaline-vent gradient
  (Δp in mV, flux in mol s⁻¹ m⁻²) and report it. If `q` is near 1, the vent is a good converter and the
  origin-of-life argument acquires a number it does not currently have.
- **Instrument extended.** `kedem-caplan`, `C8-momentum-harvesting-metric`.

### G-C — availability/repair ↔ spore dormancy vs radiation damage  **[rank 5 — demoted]**

- **Anchors.** A: Nicholson et al. 2000, *Resistance of Bacillus Endospores to Extreme Terrestrial and
  Extraterrestrial Environments*, `10.1128/mmbr.64.3.548-572.2000`. B: Kirkwood 1977, *Evolution of
  ageing*, `10.1038/270301a0`.
- **Same-object argument.** `Ha = k_r/k_d` for a dormant spore: cosmic-ray and desiccation damage
  accrue at `k_d` while the spore is dormant with `k_r = 0`, and `k_r` becomes finite only on
  germination. That is a **genuinely different regime** from C6's continuous rate balance — a system
  where availability is deliberately driven to zero in order to make `k_d` small. Interesting object.
- **Metaphor risk: LOW on the object.**
- **Intersection.** N_A = 2,024, N_B = 1,969, ∩ = **0**. Union floor `N = 3,993`, `E = 998.1` — which
  looks spectacular and **is not.** The fetched concept-scoped `N`
  (`concepts.id:C89423630|C2779343474,from_publication_date:2000-01-01`, 2026-09-05) is **14,071,245**,
  giving `E = 0.28 < 1`. **A zero against an expectation below 1 says nothing** — precisely the lesson
  `citation-intersection` records from G6. **Demoted on the project's own rule.**
- **What would rescue it.** A narrower, defensible `N`. The two concepts used (Microbiology, Senescence)
  are far too broad and are the wrong scopes; a "spore/dormancy" × "DNA repair kinetics" scope would be
  defensible if OpenAlex has one. If it does not, this candidate should not be opened at all.
- **Instrument extended.** `C6-damage-healing-ratio`, `kirkwood-disposable-soma`.

### G-B — energy per bit ↔ self-replicator free energy  **[kill]**

- Landauer 1961 × England 2013: N_A = 4,970, N_B = 427, ∩ = **45**, union floor `N = 5,352`,
  `E = 396.5`, `O/E = 0.113` at the floor — but the floor *maximises* `E`, and at any field-scale `N`
  (10⁶ gives `E = 2.1`, `O/E = 21`) this is a **strongly joined literature**.
- **Five hits inspected, all on-topic:** *Dissipative adaptation in driven self-assembly*
  (`10.1038/nnano.2015.250`), *Nonequilibrium physics in biology* (`10.1103/revmodphys.91.045004`),
  *Theory of Nonequilibrium Free Energy Transduction by Molecular Machines*
  (`10.1021/acs.chemrev.9b00254`), *On Markov blankets and hierarchical self-organisation*
  (`10.1016/j.jtbi.2019.110089`), *Defining Lyfe in the Universe* (`10.3390/life10040042`). The last is
  explicitly an astrobiology paper doing exactly this bridge.
- **This is the same shape as G8's overturn.** Record it as a checked-and-closed non-gap so the project
  does not spend a session rediscovering it. Note that the Lane & Martin `10.1038/nature09486`
  "energetics of genome complexity" angle is a *different* object (energy per gene, not per bit) and
  was **not** tested here.

### G-G — detection significance ↔ look-elsewhere effect  **[not measured]**

Madhusudhan 2023 × Gross & Vitells 2010 (`10.1140/epjc/s10052-010-1470-8`). **The measurement could
not be completed.** OpenAlex returned **HTTP 429** partway through this session — the trap already
recorded in `citation-sources.md` — and the OpenCitations fallback returned `N_A = 229`, `N_B = 0` for
the Gross & Vitells DOI, which is a **coverage void, not a zero**, and must not be recorded as an
intersection of zero. Flagged because the substance is strong: the K2-18b episode is a textbook
trials-factor problem (molecules searched × wavelength bins × retrieval configurations), and if the
intersection really is zero it belongs with G-E as one gap, not two. **Re-run when OpenAlex recovers.**

---

## Recommendation

### The one Job-1 case to run: **Venus phosphine**

Run it as the **hard-positive-plus-negative control pair** it actually is, in this order:

1. **The step-0 leg first.** Read Snellen, Villanueva, Lincowski and Cordiner, and let the audit halt
   with `NO OBSERVABLE TO EXPLAIN`. This is the **first real negative control the reservoir audit has
   ever been given** — Part D currently specifies a *fabricated* input for exactly this test, and a
   fabricated control is weaker than a real one. If the procedure as written cannot produce that state,
   the control has earned the step-0 amendment Part D.2 predicts, on a real case rather than a mock-up.
2. **Then the conditional leg**, clearly labelled conditional: enumerate rows 1–9 with flux bounds from
   Bains 2021, run the `tau_chem` aperture sensitivity at 2× and 0.5×, and check whether the audit
   recovers Bains's own published conclusion. **That is the score.** If it does, the instrument has a
   second Pioneer. If it does not, we learn that before pointing it at Mars.
3. Budget **16–22 h**. Add the **2–3 h K2-18b `NO OBSERVABLE` demonstration** as a separate short note —
   the cheapest, most reputationally valuable item in this report, because it shows the project
   declining the most publicised biosignature claim of the decade on its own stated rule.

Do **not** lead with K2-18b or with Mars. K2-18b has no observable to audit; Mars is open but its
residual is a *sink* problem (the ~300-year photochemical lifetime against the observed variability),
which is a different identity and should be run only after Venus has scored the instrument.

### The two gaps to open

- **G-E — biosignature false positives ↔ diagnostic-test theory.** Open it. It has the only null that
  survives a fetched field-scale denominator with `E = 30.8`; it has a control that fires (4) while the
  gap is zero; and all four control hits were inspected and confirmed to be astro-native Bayesian model
  comparison rather than diagnostic-test theory. It is the only candidate whose closing move is a
  *number* — the base rate at which a 3σ biosignature is more likely false than true — computable on
  public data in a desk session. It serves the owner's astrobiology interest directly and extends the
  project's own `Q7` / `positive-controls` posture. Fold G-G into it if the re-run confirms.

- **G-A — Σ (C8) ↔ planetary redox free-energy budget.** Open it, with its weakness stated in the note.
  Its `E = 3.70` is modest and its control fired only once, so it is *not* as strong a citation finding
  as G-D. It gets the second slot anyway because it is the only candidate that extends the project's
  **founding instrument** into the owner's stated domain, its same-object argument is the cleanest in
  the table (both sides in J and W, both naming the same reservoir pair), `audits/05` item 18 already
  committed to it, and it supplies the second conserved quantity the Job-1 audit needs.

**Not G-D**, despite the best statistics in the table, because the metaphor risk is highest and the
same-object argument survives only if the population framing is adopted explicitly. **Not G-C**, which
fails its own null model at any honest denominator. **Not G-B**, which is a joined literature and should
be recorded as a checked non-gap. **Not G-F** until its `N` is fetched.

### The adversarial closing note

Astrobiology's failure mode is not bad arithmetic, it is **premature naming**: converting a residual
into "life" the way `Q9-fuel-free-is-an-assumption` converted a residual into "impossible". Both are the
same error — a specification promoted to a verdict. This project's contribution to the field is not a
new biosignature; it is the refusal to promote. The K2-18b `NO OBSERVABLE` note is therefore worth more
per hour than any enumeration in this report, and the Venus step-0 halt is worth more than the Venus
enumeration that follows it.
