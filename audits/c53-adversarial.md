# C53 adversarial review

Run 2026-09-05. Target: the one sentence

> "Regolith adsorption can account for the Gale seasonal methane cycle (0.24–0.65 ppbv,
> Webster 2018) only if the CH₄–regolith adsorption enthalpy at 180–240 K on a Mars analogue is
> ≥ ~28 kJ/mol; the only measurement (Gough et al. 2010, JSC Mars-1) is 18 ± 1.7 kJ/mol at
> 115–135 K; at that value the seasonal inventory swing over the annual thermal skin depth is
> 21 t against 3,820 t required (A = 182), reproducing Meslin et al. 2011; the fitted
> 31.5 kJ/mol of Moores et al. 2019 / Smith et al. 2019 passes with 22× spare, so the
> disagreement in the literature is one number, not physics."

Read for this review: [[C53-mars-exchange-feasibility]], [[C49-mars-methane-audit]],
`vault/_scripts/c53_exchange.py`, `audits/blind-brief-c53-2026-09-05.md`,
[[reservoir-audit]] (F1–F10, Part C step 5, Part D), `audits/c43-adversarial.md`,
`audits/g34-adversarial.md`.

**Instruments.** Crossref REST (`api.crossref.org`, `mailto=deciduusleaf@gmail.com`),
arXiv API + ar5iv full text, Semantic Scholar `graph/v1/paper/DOI:` (answered, unlike in the
G34/C43 reviews), WebSearch, WebFetch, and **local re-execution of C53's own arithmetic**
(`vault/_scripts/c53_exchange.py` scaling law, Python, 2026-09-05). All fetches **2026-09-05**.
**Not obtained:** Gough et al. 2010 full text or abstract (ADS 405, ScienceDirect paywall,
Semantic Scholar returns `abstract: null`), Meslin et al. 2011 abstract (same, `abstract: null`),
LPSC 1289 PDF (`hou.usra.edu` HTTP 403 to this agent — C53 read it, this review could not
re-read it), Ortiz et al. 2022 *Icarus* full text (Elsevier 403; abstract obtained via
Semantic Scholar). Stated, not hidden.

---

## Verdict

**KILL. Grade: REDISCOVERED on the framing, WRONG on the threshold number, OVERCLAIMED on the
last clause.**

Four clauses, three deaths and one arithmetic error.

1. **"only if ΔH ≥ X, against a lower laboratory value" — REDISCOVERED, ten years old, by name.**
   **Hu, Bloom, Gao, Miller & Yung 2016**, *Astrobiology*, `10.1089/ast.2015.1410`
   (Crossref-verified: *Astrobiology*, 2016-07, 86 refs, **26** `is-referenced-by-count`,
   fetched 2026-09-05) states in its **abstract**: *"The adsorption energy needs to be 36 kJ/mol
   to explain the magnitude of the methane spikes, higher than existing laboratory
   measurements."* Its body names the same measurement C53 names — *"E_a has been measured over
   the Martian soil analog JSC-Mars-1 and the measured value is 18±2 kJ mol⁻¹ (Gough et al.
   2010)"* — states the gap — *"The main challenge of this model is that the adsorption energy
   required is 2-fold greater than what is measured by Gough et al. (2010)"* — and issues the
   call to the bench: *"Further laboratory studies are warranted to determine whether the high
   adsorption energy required by this scenario is possible for Martian regolith."* It even uses
   **C53's own soft inputs**: specific surface area **17–100 m² g⁻¹** and ρ ≈ **1300 kg m⁻³**,
   the identical pair in C53 input #8 and §4's sensitivity row. **C53 does not cite Hu 2016
   anywhere** (`grep` over `vault/` and `audits/`: zero hits for `Hu 2016`, `Hu et al`,
   `1604.08279`, `ast.2015.1410`, `deliquesc`). The claim *shape* the sentence sells as new —
   threshold on a measurable enthalpy, requirement above the lab value, go measure it — is Hu
   2016's, verbatim, in an abstract.
2. **"≥ ~28 kJ/mol" — WRONG on C53's own ledger.** Available mass scales as
   `ΔH·exp(ΔH/RT̄)`. Holding C53's `A(18.0) = 182` fixed and bisecting for `A = 1` at
   `T̄ = 210 K` gives **ΔH_threshold = 26.42 kJ mol⁻¹**, not 28. At **28 kJ mol⁻¹ the ledger
   already passes by 2.6×** (`A = 0.381`). The sentence's headline number — the only number in
   it that is C53's own contribution rather than a quotation — is high by 1.6 kJ mol⁻¹ and
   states as a *floor* a value that is comfortably inside the pass region.
3. **"21 t against 3,820 t required (A = 182)" — the two numbers are on different apertures,
   and the paper C53 is arguing with says so.** `3,820 t` is C49's **planet-wide** burden swing,
   obtained by reading Gale's `0.24 → 0.65 ppbv` as a global mixing ratio. **Moores et al. 2019
   *Nat. Geosci.*'s own abstract** (Semantic Scholar, 2026-09-05) says the opposite: *"Gale's
   unique dynamical environment makes such seeps easier to detect in surface sampling
   measurements. Over most of the Martian surface, atmospheric mixing is stronger or atmospheric
   transport more effective, and we expect the amplitude of the seasonal cycle to be smaller for
   the same strength of seep."* The observable is local and nighttime-contained (C53's own input
   #5: only `2.7×10⁴ km²` need emit). C53 records the problem — *"the last row is asymmetric on
   purpose … that is C49 §6 row 4's ×9.8 aperture problem again, **unresolved here**"* — and the
   sentence deletes the admission. The mandated step-5 rows vary the **available** side only, so
   they cannot test this; `A = 182` is not aperture-robust in the direction that matters.
4. **"the disagreement in the literature is one number, not physics" — FALSE, and refuted by an
   uncited 2022 paper.** **Ortiz, Rajaram, Stauffer et al. 2022**, *Icarus* **385**, 115079,
   `10.1016/j.icarus.2022.115079` (Crossref-verified, 8 cites): *"barometric pumping driven by
   seasonal variation of atmospheric pressure, **along with** adsorption and desorption of
   methane in the shallow subsurface driven by temperature change, can explain the observed
   bimodal peaks in the seasonal variations of methane concentration."* That is added transport
   **physics**, not a re-tuned ΔH, and it claims the same explanandum. The field also does not
   have *one* number: Hu 2016 needs **36** (spikes, deliquescence), Smith/Moores 2019 fit
   **31.5** (seasonal cycle, 1-D adsorption+diffusion), C53's ledger demands **26.4** (seasonal
   cycle, thermal skin depth) — three requirements from three models of two observables.

**What is not a hit.** The depth integral (attack 3) is correct as written — the script does
integrate the damped amplitude, `∫₀^∞ e^{−z/δ}dz = δ`, not the surface swing over the column.
The Meslin agreement (§5) is fairly stated and fairly discounted. The single-component upper
bound is the right direction for a FAIL.

---

## Attacks

### 1. Prior art on the enthalpy-threshold framing — **HIT, fatal.**

| Work | DOI | Venue / date | Crossref refs / cited-by |
|---|---|---|---|
| **Hu, Bloom, Gao, Miller & Yung 2016**, *Hypotheses for Near-Surface Exchange of Methane on Mars* | `10.1089/ast.2015.1410` | *Astrobiology*, 2016-07 | 86 / **26** |
| Gough, Tolbert, McKay & Toon 2010 | `10.1016/j.icarus.2009.11.030` | *Icarus*, 2010-05 | 67 / 32 |
| Meslin, Gough, Lefèvre & Forget 2011 | `10.1016/j.pss.2010.09.022` | *PSS*, 2011-02 | 43 / 24 |
| Moores, Gough, Martinez, Meslin et al. 2019 | `10.1038/s41561-019-0313-y` | *Nat. Geosci.*, 2019-03-04 | 43 / **34** |
| Knak Jensen, Skibsted, Jakobsen & ten Kate 2014, *A sink for methane on Mars? The answer is blowing in the wind* | `10.1016/j.icarus.2014.03.036` | *Icarus*, 2014-07 | 25 / **57** | 
| Webster, Mahaffy, Pla-Garcia, Rafkin et al. 2021 | `10.1051/0004-6361/202040030` | *A&A*, 2021-06 | 34 / 47 |
| **Ortiz, Rajaram, Stauffer et al. 2022** | `10.1016/j.icarus.2022.115079` | *Icarus*, 2022-09 | — / 8 |
| Ortiz et al. 2024 (sub-diurnal, barometric pumping + PBL) | `10.1029/2023JE008043` | *JGR Planets*, 2024-01 | 115 / 6 |
| Ortiz et al. 2024 (short-term variation, barometric pumping) | `10.1016/j.icarus.2023.115810` | *Icarus*, 2024-01 | — / 4 |

All rows Crossref-verified 2026-09-05 (`mailto=deciduusleaf@gmail.com`). The Knak Jensen 2014
title and DOI the brief asked me to check are **correct as given**.

**Hu 2016 is the kill.** Full text read via `ar5iv.labs.arxiv.org/html/1604.08279`; abstract
also pulled verbatim from the arXiv API (`export.arxiv.org/api/query?id_list=1604.08279`), so
the abstract sentence is **VERIFIED-PRIMARY**, not a search-engine paraphrase. Hu 2016 is
Hypothesis I of three, it is built on a Langmuir isotherm `θ_CH4 = K_eq·n_CH4·(1−θ_CO2)` whose
equilibrium constant is exponential in `E_a`, and it reports the requirement, the shortfall
against Gough 2010, and the laboratory ask.

**What the sentence still owns, and it is small.** Hu's 36 kJ mol⁻¹ answers a *different*
observable (the ~7 ppbv **spikes**, Webster 2015) by a *different* release mechanism
(perchlorate **deliquescence** wetting the regolith, not thermal desorption), over a stated
storage depth of 10–60 cm rather than an annual thermal skin depth. C53's 26.4 kJ mol⁻¹ is the
first threshold stated for **Webster 2018's 0.24–0.65 ppbv background cycle** on a
thermal-wave ledger, and the first to name a **temperature window (180–240 K)** for the
experiment. That is a variant of a published claim, not a new one — grade **REDISCOVERED**,
same class as `audits/c43-adversarial.md` attack 1.

**Yung et al. 2018 — the near miss C49 had already read.** C49 records Yung 2018 as
`full-text-read` (Europe PMC `PMC6205098`). Re-fetched 2026-09-05: it contains the prose form
of the same idea — *"the regolith in Gale crater could adsorb methane when dry and release this
methane to the atmosphere if deliquescence or a thin film of water/rock reactions occurs.
**A large but not prohibitive adsorption coefficient is required in this mechanism.**"* — with
no kJ mol⁻¹ figure and no comparison to Gough. Yung is a co-author of Hu 2016 and Hu 2016 is in
Yung 2018's reference list. **The prior art was one citation away from a paper this project had
already opened in full.**

### 2. The physics of the estimate — **HIT: the pressure term is in the hashed brief and absent from the code.**

`audits/blind-brief-c53-2026-09-05.md` pre-commits to

```
Delta_M_ads = A * integral [ (dq/dT)*Delta_T(z) + (dq/dp)*Delta_p ] rho_reg dz
```

and says in prose "driven by Mars' actual surface temperature **and pressure** swing".
`vault/_scripts/c53_exchange.py` has **no pressure term**: `CHI` and `P_SURF` are module
constants, `coverage()` evaluates `p = CHI*P_SURF` once, and `run()` forms
`dM_m2 = RHO*q*coef*dT*d` with `coef = dH/(R T²)` only. **A term the blind brief named was
dropped without a line in §7's honesty section.** That is the finding; the magnitude is
secondary.

Henry's law is fine at `θ ~ 10⁻¹²–10⁻⁸` (attack premise granted), and `exp(ΔH/RT)` is applied
to the right quantity *given* fixed `p`. Two seasonal pressure effects are unmodelled:

- **The CO₂ condensation cycle** (~25 % peak-to-peak in surface pressure) moves `P_SURF`, hence
  `p_CH4 = χ·P`, hence `q ∝ p` at Henry's law.
- **`χ` itself cycles by 2.7×** (0.24 → 0.65 ppbv). This is the larger term: over the same
  season the *fractional* swing in `p_CH4` is **170 %**, against the thermal swing
  `(ΔH/RT²)·ΔT_pp` = **9.8 %** at ΔH = 18 and 17.2 % at ΔH = 31.5. The neglected driver is an
  order of magnitude larger than the retained one.

**Sign.** `q ∝ p`, so the regolith *takes up* as atmospheric CH₄ rises and *releases* as it
falls — exactly out of phase with the thermal term if warming is what raises the atmosphere.
Including it therefore **reduces** net seasonal exchange and makes the measured-ΔH failure more
robust while eating into the fitted-ΔH row's 22× spare. **C53's `A = 182` is not overturned by
this attack; the `A = 0.046` PASS is the row at risk**, which is the opposite of the direction
C53 flags in §7.

**And the deeper circularity.** In the hypothesis under test the regolith *sets* the atmospheric
mixing ratio; C53 holds `χ` fixed at 0.41 ppbv as an external boundary condition while asking
whether the regolith can produce a 2.7× swing in that same `χ`. A self-consistent version has
to solve the coupled reservoir, and the back-pressure is negative feedback throughout.

### 3. The depth integral — **FAILS TO KILL as posed; a smaller, real error one level down.**

The attack supposed C53 might have applied the surface swing to the whole 1.25 m column. It did
not: the brief pre-committed to the damped form, the note writes
`ΔT(z) = ΔT_pp·e^{−z/δ}, ∫₀^∞ dz = δ`, and the code implements exactly that
(`dM_m2 = RHO*q*coef*dT*d`). **Clean.**

But the thermal wave carries a **depth-dependent phase** as well as an amplitude:
`ΔT(z,t) ∝ e^{−z/δ}·cos(ωt − z/δ)`. Contributions from different depths are not in phase, so
the seasonally coherent inventory swing is
`|∫₀^∞ e^{−(1+i)z/δ}dz| = δ/√2`, not `δ`. C53 overstates the available exchange by **√2 = 1.414**
at every ΔH. Re-running the scaling law with that correction:

| | C53 as published | phase-corrected |
|---|---|---|
| `A_exchange`, ΔH = 18 | 182 | **257** |
| `A_exchange`, ΔH = 31.5 | 0.046 (22× spare) | **0.065 (15× spare)** |
| threshold ΔH for `A = 1` | 26.42 (not 28) | **26.99** |

**Direction favourable to the FAIL**, as the attack anticipated, and it moves the corrected
threshold back toward — but still below — the sentence's "~28".

### 4. The aperture — **HIT, and it is the attack the ledger structurally cannot answer.**

C49's `3,820 t` is a planet-wide burden requirement built from `0.24 → 0.65 ppbv` treated as a
global mixing ratio. Every reason to doubt that is already inside C53's own inputs: input #5
(Moores 2019 *GRL*) says only `2.7×10⁴ km²` need emit; Webster et al. 2021 (`10.1051/0004-6361/202040030`,
47 cites) is titled *Day-night differences in Mars methane suggest nighttime containment at Gale
crater*; and Moores 2019 *Nat. Geosci.*'s abstract expects a **smaller** amplitude over most of
Mars for the same seep. The step-5 rows C53 runs scale the **available** side with area and
leave `3,820 t` fixed — which is why the Gale row reports `A = 9.7×10⁵` and C53 itself calls the
row "asymmetric on purpose … unresolved here".

**The required mass for a Gale-scale boundary-layer reservoir was not computed by C53 and is not
computable from what C53 fetched** (it needs a nocturnal boundary-layer height and a horizontal
residence time, neither of which is in the note). Order of magnitude, the planet-to-Gale area
ratio alone is `1.444×10⁸ / 2.7×10⁴ ≈ 5.3×10³`, and a collapsed nocturnal boundary layer is
~10²–10³ m against a `~11 km` scale height, i.e. two more orders off the column mass. Either
factor alone exceeds `A = 182`. **The exclusion does not survive an aperture row run on the
required side, and reservoir-audit F3/F7 make that row mandatory in principle even though step 5
as written only varies availability.** This is C49 §6 row 4's ×9.8 aperture divergence — the one
case the project has already logged as *fully explained by the aperture* — recurring unfixed.

Under F10 the sink leg was supposed to be the reproducible one because `P_avail = burden/τ` is
fixed by the observable. That argument holds for the **photochemistry** row in C49. It does
**not** hold here: this row's `P_avail` is a regolith isotherm with a free area, and its
*required* side inherits a globalisation the source papers disavow. **The row C53 excludes has
free apertures on both sides.** Proposed for the F-list as F11 in the PENDING log.

### 5. Competing adsorbates — **NOT A KILL; one unverifiable clause in the sentence.**

Gough 2010 could not be obtained by any route open to this review (ADS HTTP 405,
ScienceDirect paywall, Semantic Scholar `abstract: null`, WebSearch returns the 18 ± 2 value but
explicitly *not* the temperature range). **The sentence's "at 115–135 K" is therefore
VERIFIED-SECONDARY at best and unconfirmed by this review**, while the sentence states it as
flatly as it states the enthalpy. C53's §7 admits it never read Gough; the sentence does not.

On competition itself, what is known: Hu 2016's isotherm carries an explicit `(1 − θ_CO2)`
site-blocking factor, so CO₂ competition is a term the prior literature models and C53 asserts
away. C53's direction argument (competition lowers `q`, so the FAIL is an upper bound) is
physically standard and **probably right**, but it is asserted with no source, and it is not
sign-safe across the extrapolation: at 115–135 K the surface is in a regime where CO₂ is far
more strongly bound than at 180–240 K, so the measured `γ(T)` was taken on a **differently
covered surface** than the one the threshold is stated for. That cuts both ways and nobody has
measured which. **Not a kill; a reason the extrapolation the sentence leans on is worse than
"18 ± 1.7" makes it look.**

### 6. "One number, not physics" — **HIT, unfair on three grounds.**

- **A fit is not a measurement, and the sentence hides that.** C53 §7 says the 31.5 row is
  "soft — it is a fit, and its inputs are the generous ones". The sentence says only "the fitted
  31.5 kJ/mol … passes with 22× spare", which reads as a pass on a par with the 18 row's fail.
  Two rows of a ledger, one of which is a free parameter tuned to the target, are not two
  competing values of a measurable.
- **The resolution is quoted, not derived.** LPSC 1289's own sentence — *"Current values for
  γ/η and ΔH determined from laboratory studies … do not produce good fits"* — already
  announces the lab/fit divergence, in the primary source, from the authors of the fit. C53's
  §5 credits this correctly. The sentence's "the disagreement in the literature is one number"
  is a restatement of what one party to the disagreement wrote down.
- **There is physics on the table that C53 never fetched.** Ortiz et al. 2022 (above) adds
  barometric pumping to temperature-driven adsorption and claims the bimodal seasonal peaks;
  Ortiz et al. 2024 ×2 extend it sub-diurnally. None appears in C53. **The "not physics" clause
  is falsified by a 2022 *Icarus* paper whose mechanism is precisely the term C53's own blind
  brief promised to include and the code omitted (attack 2).**

### 7. Does it give a lab something new to do? — **NO. The ask is Hu 2016's and is ten years unanswered.**

Hu 2016: *"Further laboratory studies are warranted to determine whether the high adsorption
energy required by this scenario is possible for Martian regolith"* and *"laboratory studies of
the adsorption energy of methane for fine, porous silicate materials"*. Crossref bibliographic
queries for a CH₄-on-Mars-analogue adsorption measurement, 2020–2026, return **nothing**: the
hits are regolith-simulant formulation, 3-D printing and rheology papers. The only active
program on this observable is the Ortiz/Los Alamos **modelling** series (2022, 2024 ×2, and
`10.1016/j.icarus.2025.…` on Perseverance core gas loss). **No one is measuring it, and no one
has been since 2016 despite being asked.**

C53's genuine increment over Hu's ask is the **temperature window** — 180–240 K, chosen because
it is where the existing measurement stops — and a threshold tied to the seasonal rather than
the spike observable. That is a sharpening of an existing request, worth stating, and it is not
a discovery.

---

## The sentence that survives, verbatim

> **Regolith adsorption driven by the annual thermal wave cannot supply C49's planet-wide
> seasonal methane requirement unless the CH₄–regolith adsorption enthalpy at 180–240 K on a
> Mars analogue is ≥ 26.4 kJ/mol (27.0 with the thermal-wave phase correction), against
> 18 ± 1.7 kJ/mol reported by Gough et al. 2010 for JSC Mars-1 below Mars temperatures and
> extrapolated; that the required enthalpy exceeds the laboratory value is not new — Hu et al.
> 2016 (Astrobiology, 10.1089/ast.2015.1410) states in its abstract that "the adsorption energy
> needs to be 36 kJ/mol to explain the magnitude of the methane spikes, higher than existing
> laboratory measurements," and calls for the same experiment. What this ledger adds is the
> threshold for Webster 2018's 0.24–0.65 ppbv background cycle rather than the spikes, and the
> temperature window at which the existing measurement stops. Neither the 182 nor the 22× is
> apples-to-apples: the required mass is a planet-wide burden and the observable is a
> nighttime-contained Gale-local signal that Moores et al. 2019 expects to be smaller elsewhere,
> and the ledger omits the seasonal CH₄ partial-pressure swing its own blind brief specified.**

## Proposed edits

Written as text in `vault/PENDING-log-C53ADV.md`. No vault note was edited.

## What would settle it

1. **The measurement Hu 2016 asked for in 2016.** CH₄ uptake on JSC Mars-1 (and a modern
   simulant — MGS-1, or a phyllosilicate-bearing one) at **180–240 K**, under a **6 mbar CO₂**
   background rather than vacuum, with `γ(T)` reported separately from `ΔH` so the `τ₀`/`ΔH`
   degeneracy C53 flags in §7 is broken. Threshold to beat: **26.4 kJ mol⁻¹** on this ledger,
   36 on Hu's. One cryostat, one quadrupole, no spacecraft.
2. **Recompute the required side at the Gale aperture.** Nocturnal boundary-layer height ×
   `2.7×10⁴ km²` × the 0.24 → 0.65 ppbv swing gives the local required mass. Until that number
   exists, `A = 182` is a ratio of a local supply to a global demand and no verdict on this row
   is reproducible.
3. **Put `(dq/dp)·Δp` back in.** The brief specified it, the code omits it, and the fitted-ΔH
   PASS is the row it threatens. One term, one line of Python.
4. **Read Gough 2010.** Three clauses of the sentence — the value, its uncertainty, and the
   115–135 K range — are all second-hand, and its published `γ(T)` would let row 1 be redone
   without `γ = 1`.
5. **Read Ortiz et al. 2022 (`10.1016/j.icarus.2022.115079`).** If barometric pumping plus
   temperature-driven adsorption reproduces the bimodal seasonal peaks with a laboratory `ΔH`,
   the sentence's last clause is dead outright rather than merely overclaimed, and C49's
   `EXCHANGE REQUIRED` residual has a published claimed successor that this project has not read.
