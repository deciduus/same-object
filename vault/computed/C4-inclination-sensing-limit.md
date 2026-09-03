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
