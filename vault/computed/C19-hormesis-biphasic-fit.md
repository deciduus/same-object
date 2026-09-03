---
name: C19-hormesis-biphasic-fit
type: computed
---

# The biphasic curve engineering never parameterised: fitting shot-peening over-peening

> **The two numbers now exist.** Fitting published shot-peening dose sweeps yields, for the
> first time as parameterised constants, the stress-strengthening analogues of toxicology's
> hormesis numbers. The result depends decisively on **which response you fit**, and that
> dependence is itself the finding:
> - **Amplitude ceiling — fatigue STRENGTH (endurance limit):** ≈ **+80%** (AA 7075, 275 → 500
>   MPa, VERIFIED); ≈ **+20–30%** for AISI 4140 via Basquin conversion. This **straddles /
>   modestly exceeds** biology's **30–60%**.
> - **Amplitude ceiling — fatigue LIFE (cycles):** ≈ **+400% to +800%** (AISI 4140, VERIFIED).
>   Far above biology — because life is strength passed through a steep power law (Basquin),
>   exactly as organismal lifespan hormesis amplifies a small physiological gain.
> - **Window width:** ≥ **15×** read straight off the data (all coverages 100–1500% stay above
>   baseline), **≈ 73×** from the fitted biphasic curve's zero-equivalent span. This **meets or
>   exceeds** biology's **10–20×**.
> - **Peak/optimum:** coverage ≈ **400–660%** (medium-carbon steel, rotating bending).
>
> **Verdict: NARROWS G23, strongly, toward partial closure.** The parameterised biphasic curve
> is now written down with fitted constants. Matched on response axis, engineering's ceiling and
> window land in the *same regime* as toxicology's — the hormesis formalism transfers. But the
> numbers are **material- and response-axis-specific**; no single universal constant emerged from
> two materials, so it does not close in the "shared figure of merit / theorem" sense of
> [[what-closes-a-gap]]. The new deliverable is the fitted numbers **plus a translation rule**
> (the Basquin exponent) between the strength-ceiling and the life-ceiling.

Answers the curve-fit posed in [[G23-hormesis-formalism]]. Layer-2 construction by curve fit on
published data (zero cost), same class as [[C10-healing-curve-fit]]. Points at no unknown case.

---

## 1. What G23 said was missing

[[G23-hormesis-formalism]] (narrowed at full-text read) established that engineering **has** the
biphasic phenomenon and even names its descending limb — "over-peening / over shot peening
(OSP)". What is absent is the **parameterised curve**: no stated ceiling amplitude, no window
width, no fitted dose sweep, whereas toxicology has quantified hormesis for decades with
importable numbers (~30–60% amplitude ceiling, 10–20× stimulatory-window width). Mechanochemical
self-strengthening reports a single operating point. **This file supplies the missing
parameters by fitting a published sweep.**

---

## 2. The extracted data

### Dataset A — AISI 4140 medium-carbon steel, coverage sweep — VERIFIED

Forouzanmehr et al., *J. Manuf. Mater. Process.* **10**(4):141 (2026), open access, MDPI.
Source: [https://www.mdpi.com/2504-4494/10/4/141](https://www.mdpi.com/2504-4494/10/4/141) —
**VERIFIED, page text fetched this session.** Rotating-bending fatigue (R = −1, 50 Hz), fixed
18 A Almen intensity, S230 shot; **dose = coverage** at 100 / 400 / 1000 / 1500%; three stress
amplitudes. The complete numeric series is the 44 MPa set, read verbatim from the Figure 14
captions (Nf per coverage) and cross-checked against the stated improvement ratios.

**44 MPa series (Class C), fatigue life Nf (cycles):**

| Coverage (dose) | Nf (cycles) | vs baseline | Marker |
|---|---|---|---|
| 0% (as-received baseline) | ≈ 19,113 | — | **VERIFIED-DERIVED** (from IR = +405% at 400%) |
| 100% | 28,300 | **+48%** | VERIFIED (Fig. 14a caption) |
| 400% | 96,522 | **+405% (PEAK)** | VERIFIED (Fig. 14b caption; stated optimum) |
| 1000% | 90,336 | +373% | VERIFIED (Fig. 14c caption) |
| 1500% | 82,120 | +330% (over-peening, −15% vs 400%) | VERIFIED (Fig. 14d caption) |

Baseline check: the paper states +405% improvement at the 400% optimum, so
N_baseline = 96,522 / (1 + 4.05) = **19,113**. Back-substituting reproduces every row:
28,300/19,113 = 1.48 (+48%); 90,336/19,113 = 4.73 (+373%); 82,120/19,113 = 4.30 (+330%); and
82,120/96,522 = 0.851 = the stated **−15%** over-peening drop. All four rows are internally
consistent, so the derived baseline is trustworthy.

**37 MPa series (Class A), partial — VERIFIED:** peak at 1000% coverage = **271,907 cycles,
+797%** (Fig. 8a text); **−33%** at 1500% (over-peening). Implied baseline 271,907/8.97 = 30,313.
This is a *second* biphasic curve on the same material with the peak shifted to higher coverage
at lower stress — the over-peening turnover appears at both stress levels.

**Residual stress (FE-Cell depth profiles, Fig. 13) — VERIFIED, and it does NOT turn over:**
100% → −294 MPa; 400% → −380 MPa; 1000% → −460 MPa; 1500% → −530 MPa (monotonically rising in
magnitude). **Key mechanistic point:** the compressive residual stress keeps growing with dose;
the fatigue turnover is driven by competing **surface damage** (microcracks, roughness Ra rising
0.2 → 6.15 μm, tensile "hotspots" up to +1266 MPa at 1500%), not by any peak-and-fall in the
beneficial stress. The biphasic shape is a **difference of two monotone processes** — precisely
the mechanistic form toxicology's hormesis is also usually given (stimulation minus toxicity).

### Dataset B — AA 7075 aluminium, micro-shot-peening intensity sweep — VERIFIED

Su et al., *Materials* **16**(3):1160 (2023), open access.
Source: [https://pmc.ncbi.nlm.nih.gov/articles/PMC9920401/](https://pmc.ncbi.nlm.nih.gov/articles/PMC9920401/)
— **VERIFIED, full text fetched this session.** Rotating bending (R = −1). **Dose = Almen
intensity**; response = **endurance limit (fatigue STRENGTH), MPa** — the axis most directly
comparable to a biological hormetic response.

| Condition (dose) | Endurance limit | vs baseline | Marker |
|---|---|---|---|
| Base metal, unpeened | ≈ 275 MPa | — | VERIFIED (quoted, from authors' ref [31]) |
| Low peen, 0.110 mmA | ≈ 500 MPa | **+82% (PEAK)** | VERIFIED (quoted, from ref [31]) |
| High peen, 0.204 mmA | worse than LP, fluctuating | descending limb | VERIFIED (quoted: "not better than LP", high-roughness degradation) |

The paper states plainly: "the fatigue properties of the HP sample were not better than those of
the LP specimen … the HP sample exhibited high fluctuation." That is the over-peening descending
limb on the **strength** axis — the stimulatory optimum is at the *lower* intensity. (An anodized
sub-series — BMA 180 → LPA 300 → HPA 400 MPa — is confounded by the oxide coating and is not used
for the ceiling.)

---

## 3. The biphasic fit, with visible arithmetic

Fit form: **quadratic in log-dose** — the standard near-peak approximation of a hormetic curve
(a log-scaled inverted parabola; equivalent to the log-normal stimulation used in toxicology
near its maximum). Applied to Dataset A, 44 MPa, on `x = log10(coverage%)`, `y = ln(Nf)`.

Points (dropping the untreated point, which has no defined log-coverage):

| coverage % | x = log10(cov) | Nf | y = ln Nf |
|---|---|---|---|
| 100 | 2.000 | 28,300 | 10.2506 |
| 400 | 2.602 | 96,522 | 11.4776 |
| 1000 | 3.000 | 90,336 | 11.4114 |
| 1500 | 3.176 | 82,120 | 11.3161 |

**Note on conditioning (stated up front):** the three high-coverage points (400/1000/1500) are a
broad, nearly flat plateau, so a 4-point least-squares quadratic is ill-conditioned (the normal
equations nearly cancel — the leading coefficient is not stably determined). The honest robust
route is an **exact quadratic through the three bracketing points** 100 / 400 / 1500%, which
pins curvature without leaning on the flat interior. (The 1000% point is then a held-out check.)

**Divided differences** through (2.000, 10.2506), (2.602, 11.4776), (3.176, 11.3161):

```
f[x1,x2] = (11.4776 − 10.2506)/(2.602 − 2.000) = 1.2270/0.602 = 2.0382
f[x2,x3] = (11.3161 − 11.4776)/(3.176 − 2.602) = −0.1615/0.574 = −0.28136
c = f[x1,x2,x3] = (−0.28136 − 2.0382)/(3.176 − 2.000) = −2.3196/1.176 = −1.9724
```

Curvature `c = −1.9724` (negative ⇒ concave ⇒ a genuine peak). Vertex:

```
dy/dx = f[x1,x2] + c·(2x − x1 − x2) = 0
2x − x1 − x2 = 2.0382/1.9724 = 1.0334
x* = (1.0334 + 2.000 + 2.602)/2 = 2.8177  →  coverage* = 10^2.8177 ≈ 657%
```

Peak value:

```
y* = 10.2506 + 2.0382·(0.8177) + (−1.9724)·(0.8177)(0.2157)
   = 10.2506 + 1.6667 − 0.3479 = 11.5694  →  Nf* = e^11.5694 ≈ 105,800 cycles
```

Held-out check at 1000% (x = 3.000): predicts y = 11.504, Nf = 99,100 vs actual 90,336 —
+10%, acceptable given the flat plateau. **Ceiling (life):** 105,800/19,113 = 5.53× = **+453%**
above baseline, consistent with the raw peak of +405%.

**Window width (life axis).** In vertex form `y = 11.5694 − 1.9724·(x − 2.8177)²`. The
zero-equivalent dose (ZED) is where the curve returns to baseline `y = ln 19,113 = 9.8583`:

```
1.9724·(x − 2.8177)² = 11.5694 − 9.8583 = 1.7111
(x − 2.8177)² = 0.8675  →  x − 2.8177 = ±0.9314
x_low  = 1.886  →  cov ≈ 77%
x_high = 3.749  →  cov ≈ 5,610%
window = 5610/77 ≈ 73×   (equivalently 10^(2·0.9314) = 72.9×)
```

**Two window numbers, both honest:**
- **Model-free lower bound: ≥ 15×.** Every tested dose from 100% to 1500% coverage stays net
  beneficial (even 1500% is +330%), so the beneficial span is *at least* 1500/100 = 15× wide —
  read with no fitting at all.
- **Fitted ZED span: ≈ 73×.** The over-peening descending limb is *shallow* (only −15% from peak
  across a 3.75× dose increase), so extrapolating it back to baseline gives a very wide window.

---

## 4. The strength ceiling, and the Basquin translation rule

The life ceiling (+405%) and the strength ceiling are **not** the same number, and the converter
between them is the material's own Basquin exponent — this is the rule G23 was missing.

Basquin: `σ_a = σ'_f·(2N_f)^b`. At fixed stress, a life ratio `R_N` between peened and unpeened
corresponds to a fatigue-strength-coefficient ratio `ρ = R_N^(−b)`. Using a typical steel
`b ≈ −0.10`:

```
44 MPa peak:  R_N = 5.05  →  ρ = 5.05^0.10 = e^(0.10·1.619) = 1.176  →  +17.6% strength
37 MPa peak:  R_N = 8.97  →  ρ = 8.97^0.10 = e^(0.10·2.194) = 1.245  →  +24.5% strength
```

So the AISI 4140 **strength** ceiling is ≈ **+18–25%** (marked ESTIMATE — depends on the assumed
exponent; a steeper `b ≈ −0.15` gives +28%). The AA 7075 **strength** ceiling is a *directly
measured* **+82%** (Dataset B, VERIFIED). Across the two materials the strength-axis ceiling
spans ≈ **+20% to +80%** — the same order of magnitude as, and straddling, biology's 30–60%.

The general lesson: **fatigue life is a steep power-law transform of fatigue strength** (`N ∝
σ^(1/b)`, and `1/b ≈ −10`), so a ~20% strength gain becomes a ~5× life gain. This is the exact
structural parallel to biological hormesis, where a modest physiological improvement (heat-shock
protein upregulation, DNA-repair upregulation — the ~30–60% response) produces a large downstream
survival or lifespan gain. **The response-axis ambiguity is shared by both fields, not a defect
of the engineering data.**

---

## 5. Comparison to toxicology's 30–60% / 10–20×

| Quantity | Toxicology (hormesis) | This work (stress-strengthening) | Match? |
|---|---|---|---|
| Amplitude ceiling, **direct-response axis** | +30–60% | +20–80% (fatigue strength: 7075 +82%, 4140 est. +18–25%) | **overlaps / modestly exceeds** |
| Amplitude ceiling, **amplified-outcome axis** | (organismal lifespan hormesis, similar %) | +400–800% (fatigue life) | far larger — steep Basquin transform |
| Stimulatory window width | 10–20× | ≥15× (raw) / ≈73× (fitted ZED) | **meets or exceeds** |
| Peak location | low-dose (sub-toxic) | 400–660% coverage; shifts with load | qualitatively analogous |
| Mechanistic form | stimulation − toxicity (two monotone terms) | compressive-stress benefit − surface-damage penalty (two monotone terms; residual stress alone is monotone) | **structurally identical** |

The window-width agreement is the strongest quantitative bridge: **≥15× measured, ~73× fitted,
against biology's 10–20×** — the same decade-scale span, arrived at independently. The
amplitude-ceiling agreement holds only once the response axes are matched (direct strength ↔
30–60%); the raw fatigue-life numbers are an order of magnitude larger, and the Basquin exponent
is the conversion factor that reconciles them.

---

## 6. Verdict on G23: NARROWS (toward partial closure)

- **The two numbers now exist as fitted constants**, which they did not before this file:
  ceiling ≈ +80% (strength) / +450% (life); window ≈ 15–73×; peak ≈ 400–660% coverage. That is
  the parameterised biphasic curve G23 said was absent — supplied here.
- **They transfer, matched on axis.** Window width lands squarely in biology's 10–20× band;
  strength-ceiling overlaps biology's 30–60%. So the hormesis *formalism* is importable, with the
  Basquin exponent as the translation rule between the two response axes.
- **But not a universal constant, and not a theorem.** Two materials give two different amplitude
  ceilings (+82% vs +18–25% strength) and the window is bounded from only one of them. Per
  [[what-closes-a-gap]], closure needs a *theorem* fixing a shared figure of merit, not two fits.
  What exists is a transferable *shape and decade-scale*, not a single number both fields quote.
- **A real difference also surfaced.** Stress-strengthening's descending limb is driven by
  surface-damage competing against a *monotone* residual-stress benefit — the beneficial variable
  itself never peaks. Chemical hormesis often has the stimulatory process itself turn over. So the
  two biphasic curves share arithmetic but differ in mechanism, and the engineering window is
  *wider* (shallower over-peening limb) than a typical toxicological one.

**Net:** G23 stays **narrowed**, moved materially toward closure. The parameterised curve is no
longer missing; what remains open is a cross-material theorem that would make the ceiling and
window a single shared axis rather than a fitted family.

## 7. Weakest links (stated plainly)

- **One primary complete curve.** Dataset A's 44 MPa series (4 doses + derived baseline) carries
  the window and life-ceiling. The baseline is VERIFIED-DERIVED from the stated +405%, not read
  from Table 4 directly (the table body did not render in the fetched text); the four-way internal
  consistency check makes it solid but it is one arithmetic step removed from a printed cell.
- **Two Nf points define the over-peening limb** (1000%, 1500%), and it is shallow, so the fitted
  73× window is an extrapolation — hence both the ≥15× model-free bound and the 73× fit are given.
- **Strength ceiling for AISI 4140 is an ESTIMATE** via an assumed Basquin `b`; only AA 7075's
  +82% is a direct measured endurance-limit ratio.
- **Fit is quadratic-in-log through 3 points** (exact, robust to the flat plateau) rather than a
  full nonlinear hormesis model; a 6–8 dose sweep would let a proper log-normal be fit and the
  ZED measured rather than extrapolated. None was found open-access with a tabulated fine sweep —
  itself a mild echo of G23's original complaint that experiments report the optimum, not the
  full curve.
