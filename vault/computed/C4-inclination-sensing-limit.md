---
name: C4-inclination-sensing-limit
type: computed
---

# Minimum detectable inclination for a plant statocyte

> A single statocyte, modelled as a Berg–Purcell counter reading the population
> imbalance of `N ≈ 20–50` actively-agitated statoliths over one presentation time
> `τ ≈ 70 s`, with pile correlation time `τ_c ≈ 60–120 s`, has
> **`δθ_min ≈ 8°–17°`, central value ≈ 11°**.
>
> That is **at or above** the smallest inclination plants are demonstrated to
> respond to, and it lands almost exactly on the measured jamming angle
> `θ_c ≈ 10°`. **The single-cell equilibrium-at-`T_eff` model does not close.**
> It reproduces `θ_c` — which may be a coincidence or may be the point — but it
> cannot produce the observed *absence* of an angular threshold. Closing it
> requires pooling across statocytes and/or the longer `τ_memory ≈ 13 min`, which
> is a falsifiable prediction: sensitivity must scale as `1/√(M N τ)`.

Companion to [[G11-plant-gravisensing]]. The mechanism is [[M2-use-the-noise]]: the
agitation is not the obstacle, it is what unjams the pile and creates the sine law.

---

## 0. Sanity check — reproducing the published `Pe⁻¹`

Bérut et al. report `Pe⁻¹ = k_BT/(mgd)` between `3×10⁻³` and `8×10⁻³` for
`d = 4.5 ± 0.5 μm`, `Δρ ≈ 400 kg m⁻³`. Recomputed here from those two inputs only:

| `d` (μm) | `V = (π/6)d³` (m³) | `m = Δρ·V` (kg) | `mgd` (J) | `Pe⁻¹ = k_BT/mgd` |
|---|---|---|---|---|
| 4.0 | 3.351×10⁻¹⁷ | 1.340×10⁻¹⁴ | 5.26×10⁻¹⁹ | **7.8×10⁻³** |
| 4.5 | 4.771×10⁻¹⁷ | 1.909×10⁻¹⁴ | 8.42×10⁻¹⁹ | **4.9×10⁻³** |
| 5.0 | 6.545×10⁻¹⁷ | 2.618×10⁻¹⁴ | 1.284×10⁻¹⁸ | **3.2×10⁻³** |

with `k_BT = 1.381×10⁻²³ × 298 = 4.114×10⁻²¹ J`, `g = 9.81 m s⁻²`.

The `±0.5 μm` spread alone maps onto `3.2×10⁻³ – 7.8×10⁻³`. That **is** their
quoted `3–8 ×10⁻³`, to the digit. The stated range is a diameter-uncertainty band,
not a species or measurement scatter. Check passes.

Corollary carried from [[G11-plant-gravisensing]]: `mgd/k_BT ≈ 205`. Thermal noise
loses to gravity by two orders of magnitude. The bath that matters is the **active**
one, `T_eff ≈ 10 T`, giving `mgd/k_BT_eff ≈ 20`.

---

## 1. The signal

The pile behaves as a liquid (that is the paper's central claim), so its free
surface relaxes toward horizontal. Take a 2-D section of the statocyte floor of
width `w`, pile of mean depth `h₀`, surface tilted by `θ` about the centre:

    h(x) = h₀ + x·tan θ,    x ∈ [−w/2, +w/2]

Area transferred from the up-slope half to the down-slope half:

    ΔA = 2 · ∫₀^{w/2} x tan θ dx = (w²/4) tan θ

Total area `A = w h₀`. So the **fractional population imbalance** is

    p(θ) ≡ (N_L − N_R)/N = ΔA/A = (w / 4h₀) · tan θ ≈ α · sin θ,   α ≡ w/(4h₀)

Numbers: Bérut's biomimetic statocyte is `100 × 30 × 50 μm`; the pile is
`2–3` layers of `d = 4.5 μm`, so `h₀ ≈ 9–14 μm`. Taking `w ≈ 50 μm`:

    α = 50 / (4 × 11) ≈ 1.1

So `α ≈ 1` (range ~0.5–2), and the signal is

    ΔN_signal = α N sin θ  ≈  N θ   (small θ)

This is the microscopic origin of the macroscopic sine law, and it is geometric,
not thermal. **`T_eff` does not set the signal amplitude.**

*Cross-check against the equilibrium route.* If instead one writes a Boltzmann
occupancy at `T_eff` for the two sides, `p = tanh(ΔE / 2k_BT_eff)` with
`ΔE ≈ mg (w/2) sin θ`, then

    ΔE / k_BT_eff = (mgd / k_BT_eff) · (w/2d) · sin θ ≈ 20 × 5.6 × sin θ ≈ 110 sin θ

which exceeds 1 for `θ > 0.5°`. The Boltzmann route **saturates almost immediately**:
the pile fully levels. That is consistent with — and reduces to — the geometric
result `α ≈ 1`. Two independent routes agree that the signal is `≈ N sin θ`, and
neither is limited by `T_eff`.

## 2. The noise

Take each statolith as independently assignable to one side or the other with
`p ≈ 1/2` at small `θ`. Then `N_L ~ Binomial(N, 1/2)` and

    Var(N_L − N_R) = 4 · N · p(1−p) = N
    σ_ΔN = √N   per independent configuration

This is the **counting shot noise** of the pile. It is a conservative (upper)
bound: a dense, nearly incompressible pile has *sub*-Poissonian occupancy
fluctuations, which would only improve the sensitivity. `T_eff` does not appear
here either.

**`T_eff` enters the calculation in exactly one place: the correlation time.**
That is the honest statement of where the active bath does its work.

## 3. The correlation time — and which one I used

The Berg–Purcell step needs the number of statistically independent readings
inside the integration window, `N_ind = τ / τ_c`.

Two candidate clocks:

- **(A) The measured pile relaxation / avalanche time.** Bérut et al. measure the
  pile angle decaying with characteristic time `t_a ≈ 2 min`; Chauvet et al. fit
  `τ_aval = 1.04 min` at 1 g. **I use this**, `τ_c = 60–120 s`, because it is
  measured on the actual object and is the *shorter* of the two candidates —
  i.e. it is the choice most favourable to the plant, and therefore the one that
  makes the bound hardest to beat by fudging.
- **(B) A diffusive decorrelation time at `T_eff`.** Time to diffuse one grain
  diameter, `τ_D = d²/D_eff = 3πηd³ / (k_B T_eff)`. Using the identity
  `τ_D = (mgd/k_BT_eff) × (d / v_sed) ≈ 20 × d/v_sed`, this is **~20 sedimentation
  times per grain diameter** — order 10 min for plausible statolith settling
  speeds. Longer than (A), so it would make `δθ_min` worse by a further ~2–3×.
  Marked UNVERIFIED; I did not obtain a measured `v_sed` or a cytoplasmic
  viscosity this session, and I am not reconstructing one from memory.

Note (A) is a *gravity-driven collective* relaxation, not a thermal one. Using it
as a decorrelation time is an approximation (see Assumption A4).

## 4. Setting SNR = 1

    SNR(θ) = ΔN_signal / (σ_ΔN / √N_ind)
           = α N sin θ · √(τ/τ_c) / √N
           = α √N · sin θ · √(τ/τ_c)

Set `SNR = 1`:

    ┌──────────────────────────────────────────┐
    │   sin δθ_min = (1 / α√N) · √(τ_c / τ)    │
    └──────────────────────────────────────────┘

Scaling: `δθ_min ∝ N^{-1/2} τ^{-1/2}`. And — the notable structural result —
**`T_eff` appears only inside `τ_c`**, not as an amplitude. Raising the agitation
*improves* the sensor (shorter `τ_c`, more independent samples) until the pile
stops being a pile. That is [[M2-use-the-noise]] in one line.

## 5. Arithmetic

`τ = 70 s` (presentation time, Arabidopsis control roots, 1.16 min).
`α = 1`.

| `N` | `τ_c` (s) | `√(τ_c/τ)` | `1/√N` | `sin δθ_min` | `δθ_min` |
|---|---|---|---|---|---|
| 20 | 62 | 0.941 | 0.2236 | 0.2104 | **12.1°** |
| 20 | 120 | 1.309 | 0.2236 | 0.2928 | **17.0°** |
| 50 | 62 | 0.941 | 0.1414 | 0.1331 | **7.6°** |
| 50 | 120 | 1.309 | 0.1414 | 0.1851 | **10.7°** |

**`δθ_min ≈ 8°–17°`, central ≈ 11°.**

With `α = 2` (a shallower pile) the whole band halves to ~4–9°; with `α = 0.5` it
roughly doubles to ~15–35°. The `α` uncertainty is comparable to the `N` uncertainty.

## 6. Inputs

| Quantity | Value | Status | Source |
|---|---|---|---|
| Statolith diameter `d` | 4.5 ± 0.5 μm | **VERIFIED** | https://pmc.ncbi.nlm.nih.gov/articles/PMC5960325 |
| Density contrast `Δρ` | ~400 kg m⁻³ | **VERIFIED** | same |
| `Pe⁻¹` | 3×10⁻³ – 8×10⁻³ | **VERIFIED** | same |
| Effective temperature | "apparent temperature 10 times larger than the actual temperature" | **VERIFIED** | same |
| Critical angle `θ_c` | ≃10° | **VERIFIED** | same |
| Sine-law population split | "proportion varies with the sine of the cell inclination" | **VERIFIED** | same |
| `N`, statoliths per statocyte | "typically contain a few tens" → taken as **20–50** | **VERIFIED (qualitative only)** | same |
| Pile layers | "typically 2 to 3" | **VERIFIED** | same |
| Cell dimensions (biomimetic) | 100 × 30 × 50 μm | **VERIFIED** | same |
| Avalanche time `t_a` | ≃2 min | **VERIFIED** | same |
| Avalanche time `τ_aval` at 1 g | 1.04 min | **VERIFIED** | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6436155/fullTextXML |
| Memory / integration time `τ_memory` | 13 min | **VERIFIED** | same |
| Presentation time `τ` (Arabidopsis root, control) | **1.16 min ≈ 70 s** | **VERIFIED** | https://pmc.ncbi.nlm.nih.gov/articles/PMC35160/ (Blancaflor, Fasano & Gilroy 1998, *Plant Physiol* 116:213) |
| Presentation-time definition | "the minimum exposure time to a 1 g field to induce a response" | **VERIFIED** | same |
| Sine law, macroscopic, 4 species | response ∝ sin θ, independent of g | **VERIFIED** | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5064399/fullTextXML |
| Smallest angle bin with measured response | `10° < θ_init < 20°` (Fig. 2d) | **VERIFIED** | same |
| "No angular threshold" claim | "no gravisensing threshold nor plateau could be observed" | **VERIFIED** | same |
| Classic minimum response angle | "The angle of 10° seemed to be the minimum angle to induce a gravitropic response" | **VERIFIED** | https://www.frontiersin.org/articles/10.3389/fpls.2014.00610/full |
| Statolith count, *Chara* rhizoids (contrast case) | 5–10 or 50–60 per cell depending on growth medium | **VERIFIED** | Europe PMC search, https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&query=%22statoliths%20per%20cell%22 |
| Statolith sedimentation velocity `v_sed` | — | **UNVERIFIED — not obtained** | — |
| Cytoplasmic viscosity η | — | **UNVERIFIED — not obtained** | — |
| Number of statocytes `M` pooled by the root cap | — | **UNVERIFIED** — a 2-D median section shows 3 tiers × 4 files = 12, but the 3-D count is larger and I did not fetch a source that states it | — |
| `k_B`, `g`, `T = 298 K` | standard | VERIFIED (constants) | — |

**No source I fetched states a numerical `N`.** "A few tens" is the best the
primary literature gives for higher-plant statocytes. `N = 20–50` is my reading of
that phrase and is carried through as a range, not a point. The *Chara* numbers
(5–10 vs 50–60) show the count is not even fixed within a species — it is set by
growth conditions — so treating `N` as a constant is itself an assumption.

## 7. Assumptions, stated

**A1 — Equilibrium at `T_eff`.** *This is the non-rigorous step and I am not
dressing it up.* An active bath is characterised by a single scalar `T_eff` only
if the fluctuation–dissipation relation holds with that temperature at the
frequency being probed. Bérut et al. extract `T_eff ≈ 10 T` from a *static*
observable (the inverse Péclet number inferred from pile shape), not from a
measured FDT ratio. It is entirely possible that `T_eff(ω)` is strongly
frequency-dependent — active cytoskeletal driving typically is — in which case the
`T_eff` relevant to fluctuations on the 70 s timescale is not the one that sets
the static pile shape.
**What would break it:** measure the statolith mean-square displacement spectrum
and the response to an applied force (optical tweezers) in the same cell, and take
the ratio. If FDT-with-a-constant-`T_eff` fails, this whole calculation's noise
term is wrong by an unknown factor. *This measurement does not appear to have
been done.* It is exactly the "orthogonal measurement" that METHOD §10 asks for.

**A2 — Binomial (independent) occupancy.** Statoliths are treated as
independently assigned to the two halves. A real pile is dense and sterically
correlated; correlations suppress number fluctuations, so `√N` is an **upper**
bound on the noise and `δθ_min` as computed is an upper bound on the bound. This
error is in the safe direction.

**A3 — `α ≈ 1` from an idealised wedge.** Real statocyte floors are not flat
rectangles, the pile does not have a sharp free surface at 2–3 layers thick, and
the relevant `w` is a guess from the biomimetic cell rather than a measured wheat
statocyte. `α` is uncertain by a factor ~2 in each direction and propagates
linearly into `δθ_min`.

**A4 — `τ_c = τ_aval`.** The avalanche time is a *driven, gravity-relaxation*
timescale measured after a large step tilt. Using it as the *equilibrium*
decorrelation time of the pile at small `θ` conflates a response time with a
correlation time. These coincide in a genuine equilibrium system (regression
hypothesis), which is precisely what A1 puts in doubt. The diffusive estimate (B)
disagrees with it by ~5×.

**A5 — Single statocyte, single presentation time.** The plant may pool over many
cells and integrate for longer (`τ_memory = 13 min` is measured). Section 8.

**A6 — Downstream transduction is noiseless.** The bound is a *sensor* bound.
Auxin transport, PIN relocalisation and growth response add noise, so the true
behavioural threshold can only be worse than this.

**A7 — Root presentation time applied to a shoot-derived pile geometry.** `τ = 70 s`
is Arabidopsis *root*; `d`, `Δρ`, `θ_c` are from wheat coleoptile statocytes and
biomimetic mimics. Mixing organs. Roots and shoots have different presentation
times, and I did not obtain a coleoptile value.

## 8. Comparison to observation

**Observed:** the smallest inclination with a directly measured gravitropic
response in Chauvet et al. 2016 is the `10°–20°` bin. The older literature quotes
`10°` as "the minimum angle to induce a gravitropic response". Against that,
Chauvet et al. state explicitly that **no angular threshold exists** — the sine law
extrapolates to zero with no plateau — and Bérut et al. make the same point
mechanistically: the agitation is what stops the pile jamming, so statoliths "move
even at small inclination."

**Computed:** `δθ_min ≈ 8°–17°` (central 11°) for one statocyte over one
presentation time.

**Verdict: the bound sits AT or ABOVE the observed sensitivity.** It does not
close. Three readings, in order of how much I believe them:

1. **The plant averages over more than one cell and more than one presentation
   time.** This is the boring and most likely answer, and it is a quantitative
   prediction: with `M` statocytes pooled and `τ = τ_memory = 13 min`,
   `δθ_min → 11° / (√M · √(780/70)) = 11°/(3.34√M)`. For `M = 12` that is
   **0.95°**; for `M = 30`, **0.6°**. So sub-degree sensitivity is reachable, but
   *only* with pooling — a single cell provably cannot do it under this model.
   **Falsifiable:** ablate columella cells and the threshold angle should degrade
   as `M^{-1/2}`. Blancaflor et al. already did the ablations and reported
   presentation time, not threshold angle. The experiment is one re-analysis away.
2. **`T_eff ≈ 10 T` understates the agitation on the 70 s timescale.** A larger
   `T_eff` shortens `τ_c`, buying `√` of the increase. This is assumption A1
   failing in the direction that helps.
3. **The equilibrium-at-`T_eff` picture is simply the wrong statistics.** Active
   baths can have strongly non-Gaussian, correlated fluctuations that do not
   average as `1/√n`. If the noise is *sub*-diffusive or the occupancy is
   collectively rigid, the effective `σ` is smaller than `√N` and the bound moves
   down without any change to `T_eff`.

**The coincidence worth flagging.** `δθ_min ≈ 11°` and the measured jamming angle
`θ_c ≈ 10°` agree to well within the uncertainty of either. These are supposed to
be independent quantities — one is a granular-mechanics angle of repose, the other
a signal-to-noise limit. Either that is chance (the band is wide enough that it
could be), or the pile is tuned so that its statistical detection floor coincides
with its mechanical jamming angle, which would be a genuinely interesting design
statement. **I am not claiming the latter.** Distinguishing them needs `N` and `α`
measured rather than inferred; at present the error bars swallow the claim.

## 9. Weakest step

Ranked:

1. **A4/A1 together — the correlation time.** `τ_c` enters as `√τ_c` and I have two
   estimates that differ by 5×, one of which (the avalanche time) is a driven
   response misused as an equilibrium correlation time. Everything downstream
   inherits this.
2. **`N` is not measured.** "A few tens" is the entire primary-literature basis.
   `δθ_min ∝ N^{-1/2}`, so the 20–50 range alone is a 1.6× spread.
3. **`α`** — a wedge model with a guessed cell width.

## 10. What would settle it

- Measure `N` per wheat/Arabidopsis statocyte directly. Trivial with the confocal
  data that already exists in these groups.
- Measure the statolith MSD spectrum **and** the mechanical response in the same
  cell, and test FDT at `T_eff = 10 T`. This is the assumption nobody has varied,
  in the sense of METHOD §8.
- Re-analyse the columella ablation series for **threshold angle** rather than
  presentation time, and test `δθ_min ∝ M^{-1/2}`.

---

Links: [[G11-plant-gravisensing]] · [[M2-use-the-noise]]

---

## Testing the pooling prediction

*Added 2026-09-03. §8 reading (1) predicted that if the plant beats the single-cell bound by
pooling over `M` statocytes, then `δθ_min ∝ M^{-1/2}`, and it named the test: the columella
ablation series. That series was run. This section retrieves it, resolves `M`, fits the
scaling, and reports where the test is and is not decisive.*

### 11.1 `M` is resolved: **48** for the Arabidopsis columella

The source is the ablation paper itself, which states the 3-D geometry explicitly.

> "Transmission-detector images obtained from the confocal microscope of the root cap of a
> 3-d-old Arabidopsis seedling showed three horizontal stories and four vertical files of
> columella cells"

> "In two dimensions, the columella cells (numbered) are typically organized into three
> horizontal stories and four vertical files."

> "S1, cells 9–12; S2, cells 5–8; and S3, cells 1–4"

> "a single columella cell ablation in two dimensions is actually a total of four cells
> ablated one on top of another. A single-story ablation is actually a total of 16 ablated
> cells"

**VERIFIED** — https://pmc.ncbi.nlm.nih.gov/articles/PMC35160/ (Blancaflor, Fasano & Gilroy
1998, *Plant Physiol* 116:213–222, "Mapping the functional roles of cap cells in the response
of Arabidopsis primary roots to gravity"). Article identity independently confirmed via
`https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=35160` and
`https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:9449842`
(PMID 9449842). Note: Europe PMC lists this article as **not** open access and serves no full
text for it; the numbers below come from the NCBI PMC HTML, which was reachable this session
for PMC35160 (it was **not** reachable for PMC5960325, which required the eutils route).

    16 cells per story × 3 stories  →  M = 48 statocytes

This **replaces the UNVERIFIED "12" in §6**, which was a 2-D median-section count (3 × 4) and
undercounted by exactly the factor 4 of the Z-direction. Consequences for §8 reading (1):

    δθ_min = 11° / (√M · √(τ_memory/τ)) = 11° / (√48 × 3.34) = 0.48°

not 0.95°. Sub-degree sensitivity is comfortably reachable *if* pooling is real.

**Correction to the brief that commissioned this section:** the graded ablation study is
**Arabidopsis**, not maize. Blancaflor, Fasano & Gilroy also published the same dataset as
"Laser ablation of root cap cells: implications for models of graviperception", *Adv Space
Res* 1999 (PMID 11542616, abstract only — **VERIFIED abstract**, full text not obtained, via
the Europe PMC `EXT_ID:11542616` core record). It is a restatement, not new data. No second,
independent graded columella-ablation series was found.

### 11.2 What was measured: presentation time, not threshold angle

To answer the key question directly: **nobody measured a threshold angle as a function of
statocyte number.** Blancaflor et al. measured three things — curvature time course, final
angle, and **presentation time** (minimum 90° stimulus duration producing a response). All
stimulation was at **90°**. There is no angular series.

But presentation time is *not* useless here, because the pooling model makes a definite
prediction for it. From §4, at fixed angle and fixed detection criterion:

    SNR ∝ α √M · sin θ · √(τ/τ_c) = const   ⟹   τ_p ∝ M⁻¹

So the pooling hypothesis, applied to this experiment, predicts **`τ_p × M = constant`** —
exponent **1**, not 1/2. (The 1/2 lives in the angle; the presentation time is the square of
the angular sensitivity.) That is testable with the published numbers.

### 11.3 The data

Figure 4 legend, quoted verbatim from the fetch:

> "A, Inner versus outer story ablations. Presentation time was 1.16 min for control roots,
> 1.28 min for S3/tip cell ablations, and 7.13 min for S1/S2 cell ablations. B, Individual
> story ablations. Presentation time was 2.55 min for S1 cell ablations and 3.53 min for S2
> cell ablations. C, Individual stories intact. The presentation time was 2.62 min for roots
> with only S2 cells intact and 4.85 min for roots with S1 cells intact. D, Central columella
> versus flank columella cell ablations. Presentation time was 4.07 min for roots with the
> central columella cells ablated and 1.91 min for roots with the flank columella cells
> ablated. ... Each data point represents a mean ± se of 15 to 30 roots."

Converting ablation treatment to surviving statocyte count `M` using 16 cells/story, and
2-of-4 files (× 3 stories × 4 deep = 24 cells) for the central/flank split:

| Treatment (ablated) | Surviving `M` | `τ_p` (min) | Regression `r` |
|---|---|---|---|
| none (control) | 48 | 1.16 | 0.99 |
| S3 + tip cells | 32 | 1.28 | 0.99 |
| S1 | 32 | 2.55 | 0.99 |
| S2 | 32 | 3.53 | 0.96 |
| flank files | 24 | 1.91 | 0.95 |
| central files | 24 | 4.07 | 0.98 |
| S1 + S2 (S3 intact) | 16 | 7.13 | 0.99 |
| S1 + S3 (S2 intact) | 16 | 2.62 | 0.97 |
| S2 + S3 (S1 intact) | 16 | 4.85 | 0.87 |

Internal consistency check: the abstract states the S1+S2 ablation gave "a presentation time
6-fold longer than the controls". 7.13/1.16 = **6.1**. Passes.

Also from the paper, and important for what follows: **a single-cell ablation did nothing.**

> "a single line of columella cells in S2 along the Z axis (i.e. a total of four cells: two
> flank and two central columella cells)" — no measurable reduction.

Removing 4 of 48 cells (8%) is below the noise of the assay. Pooling predicts a 9% change in
`τ_p` — undetectable, so this is consistent but carries no information.

### 11.4 The fit

Model `τ_p = A · M^{−b}`. Ordinary least squares on `ln τ_p` vs `ln M`.

**All nine points:**

    b = 1.13 ± 0.40   (1 s.e.)      R² = 0.53      residual s = 0.44 in ln units (±55%)

**Geometric means at each of the four distinct `M`:**

    b = 1.20 ± 0.12                 R² = 0.980     residual s = 0.097 in ln units (±10%)

| `M` | geo-mean `τ_p` (min) | fit `M^{−1.20}` | resid | pure `M⁻¹` from control | resid |
|---|---|---|---|---|---|
| 48 | 1.16 | 1.24 | −6.3% | 1.16 | (anchor) |
| 32 | 2.26 | 2.01 | +12% | 1.74 | +30% |
| 24 | 2.79 | 2.84 | −2.0% | 2.32 | +20% |
| 16 | 4.49 | 4.63 | −2.9% | 3.48 | +29% |

**Verdict on the fit.** The pooling exponent `b = 1` is **not rejected**: it is 1.7 s.e. from
the group-mean estimate, and its worst residual over a 3× range of `M` is +30%. The
no-pooling null `b = 0` is 10 s.e. away and dead. The parallel-sensors picture therefore
survives its first quantitative contact with data, with a mild systematic pull toward a
slightly *steeper* exponent (~1.2).

**Verdict on what the fit hides, which matters more.** At fixed `M` the spread is enormous:

| `M` | `τ_p` range | ratio |
|---|---|---|
| 32 | 1.28 – 3.53 | **2.8×** |
| 24 | 1.91 – 4.07 | **2.1×** |
| 16 | 2.62 – 7.13 | **2.7×** |

The within-`M` scatter (pooled s = 0.52 in ln units) is **larger** than the residual scatter
about the power law (s = 0.44). In plain terms: **which** cells you remove matters more than
**how many**. Removing all 16 of S3 costs 10% of the presentation time; removing all 16 of S2
costs 200%. Statocytes are not interchangeable, and equal-weight pooling is wrong as stated.

The paper says why, and its explanation is mechanical rather than statistical:

> "the central cells of story 2 contributed the most to root gravitropism. These cells also
> exhibited the largest amyloplast sedimentation velocities."

So the honest model is **weighted** pooling, `SNR ∝ √(Σᵢ wᵢ)` with `wᵢ` set by each cell's
statolith mobility. That has enough free parameters to fit four group means and is therefore
not falsifiable on this dataset. I am not fitting it.

### 11.5 The degeneracy that makes this test non-decisive

This is the load-bearing caveat and it kills the temptation to declare victory.

`τ_p ∝ M⁻¹` is **not** a signature of pooling. A completely deterministic model — each
statocyte emits an auxin-asymmetry signal, the signals sum linearly, and the root responds
when the accumulated dose crosses a fixed threshold — predicts exactly `τ_p ∝ M⁻¹` with no
noise, no averaging and no `√` anywhere. Both models pass §11.4 identically. **The
presentation-time series cannot separate them.**

The angular series can, and that is precisely why it is the missing experiment:

| Model | `δθ_min(M)` | `τ_p(M)` |
|---|---|---|
| Statistical pooling (Berg–Purcell over `M` cells) | `∝ M^{−1/2}` | `∝ M⁻¹` |
| Deterministic linear summation, fixed dose threshold | `∝ M⁻¹` | `∝ M⁻¹` |
| No pooling (one dominant cell) | `∝ M⁰` | `∝ M⁰` |

The two live models **differ by a factor of 2 in the angular exponent and not at all in the
temporal one.** Blancaflor et al. measured the exponent that does not discriminate.

### 11.6 The experiment that would settle it

Blancaflor's ablation protocol crossed with Chauvet's angular protocol. Nothing new is needed.

**Design.** Arabidopsis primary roots, laser-ablate to leave `M ∈ {48, 32, 24, 16}` — i.e.
control, S3-ablated, flank-ablated, and S1+S3-ablated (S2 intact). Use the *S2-intact* arm at
`M = 16` rather than S3-intact, because §11.4 shows S3 is nearly inert and would confound cell
count with cell quality. Hold the ablated *fraction of S2* constant across arms if possible;
if not, report it, because it is the dominant nuisance variable.

**Measure.** Not presentation time. Stimulate at a fixed, long duration (≥ `τ_memory` = 13 min,
so integration is saturated and only the angle is limiting) at each of θ = 5°, 10°, 20°, 40°,
90°. Measure initial curvature rate. Fit the sine law, `rate = k sin θ`, and extract the angle
at which curvature becomes indistinguishable from zero — the same regression-to-`y = 0`
construction Blancaflor already used for time, applied to angle. Call it `θ_min(M)`.

**Predicted numbers.** Normalising to the control arm:

| `M` | pooling, `√(48/M)` | linear summation, `48/M` | absolute `θ_min` if control is 0.48° |
|---|---|---|---|
| 48 | 1.00 | 1.00 | 0.48° / 0.48° |
| 32 | 1.22 | 1.50 | 0.59° / 0.72° |
| 24 | 1.41 | 2.00 | 0.68° / 0.96° |
| 16 | **1.73** | **3.00** | **0.83° / 1.44°** |

The absolute column uses §11.1; it is model-dependent and the *ratios* are the real prediction.

**Falsification, stated in advance.**

- `θ_min(16)/θ_min(48) ≥ 2.5` → **pooling is falsified**; the system is a deterministic linear
  summer and the Berg–Purcell framing of C4 is the wrong idealisation.
- `θ_min(16)/θ_min(48) ≤ 1.25` → **pooling is also falsified**, in the other direction: the
  cells are not independent samples, or one cell dominates, or the noise is correlated across
  cells (which would be its own finding — correlated active noise does not average).
- `1.5 ≤ ratio ≤ 2.0` → pooling survives.
- Any measurable `θ_min > 0` in the control arm falsifies Chauvet's no-threshold claim and
  refutes the premise of this whole note. That is a useful side result either way.

**Power.** The two live predictions differ by 73% at `M = 16`. Blancaflor's presentation-time
regressions reached `r = 0.87–0.99` with n = 15–30 roots per point. A 73% effect is far above
that noise; ~25 roots × 5 angles × 4 arms ≈ 500 roots, one experiment.

### 11.7 Has anyone proposed statocyte pooling before?

**Not found, and I searched for it specifically.** Roughly ten queries across Europe PMC
full-text and web search — `"number of statocytes"`, `"statocyte" AND ("signal averaging" OR
"pooling")`, averaging/ensemble/noise-reduction phrasings, and Berg–Purcell-anchored variants
(the last per METHOD §11's warning about anchoring on the originating field's term). Returns
were Meroz & Bastien 2014, Miyamoto 2007, Bérut 2018 and reviews — none proposing across-cell
averaging as a sensitivity mechanism.

The one genuinely close hit is worth recording precisely, because it is a *methodological*
statement that lands one inference short of the hypothesis:

> "While θ(t) for a single pile exhibits large fluctuations due to the small number of
> statoliths per pile, the averaged value of the pile angle over several cells is
> well-defined."

Bérut et al. 2018, **VERIFIED** via
`https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=5960325` (the
`pmc.ncbi.nlm.nih.gov` HTML and the Europe PMC `PMC5960325/fullTextXML` route both failed this
session — captcha and 404 respectively).

They observe that the single-cell signal is too noisy to read and that averaging over cells
recovers it — which is C4 §8 reading (1) in miniature — but they invoke it as *their own
measurement procedure*, not as *the plant's*. A Europe PMC search shows theirs is the only
indexed work containing the phrase "number of statocytes," and it gives no count.

**Status: NOT YET A SHARED OBJECT** (METHOD §11 taxonomy). The physics of cellular sensing has
the `M^{−1/2}` machinery; the plant literature has the ablation series and the sine law; the
one paper that touches both uses the averaging as an instrument rather than a hypothesis.

### 11.8 Standing after this section

| Claim | Before | After |
|---|---|---|
| `M` for Arabidopsis columella | UNVERIFIED, guessed 12 | **VERIFIED = 48** |
| `δθ_min` with pooling + `τ_memory` | 0.95° | **0.48°** |
| Graded ablation data exist | assumed | **Yes — 9 treatments, 4 distinct `M`** |
| Threshold angle vs `M` measured | assumed re-analysable | **No. Never measured. All stimulation at 90°** |
| `τ_p ∝ M⁻¹` | untested | **b = 1.20 ± 0.12, R² = 0.98 on group means; b = 1 not rejected** |
| Pooling confirmed | — | **No.** Test is degenerate with deterministic linear summation |
| Equal-weight pooling | implicit | **Falsified.** 2.1–2.8× spread in `τ_p` at fixed `M` |
| Anyone proposed pooling | unknown | **No published proposal found** |

The §8 sentence "the experiment is one re-analysis away" was **wrong** and is corrected here:
the required observable was never recorded, so it is one *experiment* away, not one
re-analysis. The experiment is §11.6 and costs about 500 roots.

### 11.9 Inputs added

| Quantity | Value | Status | Source |
|---|---|---|---|
| Columella stories | 3 | **VERIFIED** | https://pmc.ncbi.nlm.nih.gov/articles/PMC35160/ |
| Columella files (2-D) | 4 | **VERIFIED** | same |
| Cells per story (3-D) | 16 | **VERIFIED** | same |
| **`M`, total statocytes** | **48** | **VERIFIED** | same |
| Presentation times, 9 treatments | table §11.3 | **VERIFIED** | same |
| Curvature rates / final angles, 10 treatments | Table II | **VERIFIED** | same |
| Central S2 cells have largest amyloplast sedimentation velocity | qualitative | **VERIFIED** | same + PMID 11542616 abstract |
| Adv Space Res 1999 restatement | same dataset | **VERIFIED (abstract only)** | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:11542616 |
| Cross-cell averaging quote | Bérut 2018 | **VERIFIED** | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=5960325 |
| Threshold angle vs `M` | — | **DOES NOT EXIST** | ~10 queries, §11.7 |
| Statolith `v_sed` absolute value | — | still **UNVERIFIED** | Blancaflor reports *relative* velocities only; no absolute figure obtained |

Assumptions specific to this section, stated:

**A8 — the `M` bookkeeping.** Story ablations map cleanly (16 cells each, stated by the
authors). The **central/flank** split does not: the paper classifies files in 2-D and the
ablation removes all four Z-positions, so I take flank = files 1,4 = 24 cells and central =
files 2,3 = 24 cells. If the Z-outermost cells are functionally "flank" too, the two `M = 24`
points are mis-assigned. Dropping both `M = 24` points changes the group-mean fit to
`b = 1.19` — negligible, so the fit does not rest on this.

**A9 — presentation time as an inverse-SNR proxy.** `τ_p` is the *stimulus* duration, which
maps to the integration window `τ` in §4 only if the cell integrates for exactly as long as it
is stimulated and forgets nothing. `τ_memory = 13 min` exceeds every `τ_p` here (1.2–7.1 min),
so this is at least self-consistent, but it is an assumption.

**A10 — ablation is clean.** Laser-ablated cells are assumed to remove sensing capacity without
wounding responses, altered auxin transport geometry, or damage to neighbours. The paper's own
S3 result argues against full cleanliness: ablating S3 barely changed presentation time but
*did* inhibit bending, which the authors attribute to blocked signal **translocation** rather
than lost perception. Any `M`-scaling fit therefore mixes sensing loss with transport damage.
This is the weakest step in §11.4 and is worse than the statistics.

