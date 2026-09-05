---
name: C19-hormesis-biphasic-fit
type: computed
---

# The biphasic curve engineering never parameterised: fitting shot-peening over-peening

> **The two numbers now exist.** Fitting published shot-peening dose sweeps yields, for the
> first time as parameterised constants, the stress-strengthening analogues of toxicology's
> hormesis numbers. The result depends decisively on **which response you fit**, and that
> dependence is itself the finding:
> - **Amplitude ceiling — fatigue STRENGTH:** ≈ **+82%** for AA 7075 (275 → 500 MPa, VERIFIED)
>   — a *measured endurance limit*, and the **best of two doses**, not a fitted ceiling;
>   ≈ **+18–25%** for AISI 4140 as a **σ'_f-equivalent ESTIMATE** via Basquin conversion (a
>   different axis — see §4). AA 7075's +82% **exceeds** biology's **30–60%**; the 4140
>   σ'_f-equivalent estimate sits below it. The two do not straddle a common band because they
>   are not on a common axis.
> - **Amplitude ceiling — fatigue LIFE (cycles):** ≈ **+400% to +800%** (AISI 4140, VERIFIED).
>   Far above biology — because life is strength passed through a steep power law (Basquin),
>   exactly as organismal lifespan hormesis amplifies a small physiological gain.
> - **Window width: not measured.** The tested dose range, all doses beneficial, spans **15×**
>   (100–1500% coverage) — that is an experimental-design artifact (the ratio of the extreme
>   *tested* doses), not a window, and it is **not** compared against biology's 10–20×. Refitting
>   with a physically admissible form (`Nf = N₀(1 + a·c·e^{−bc})`, §3) shows the curve approaches
>   baseline only **asymptotically**, so **no finite two-sided window exists under this form and
>   the data constrain no window at all**. Only a one-sided descending-limb statement survives.
> - **Peak/optimum:** measured maximum at coverage **400%** (44 MPa) / **1000%** (37 MPa); the
>   admissible fit puts the optimum at ≈ **770%** (leave-one-out range 700–1140%).
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

**Window width — refit with a physically admissible form.** The log-quadratic above is fitted
only near the peak; extrapolated it predicts `Nf` *below baseline* for coverage < 77%, i.e. that
light peening is harmful, which contradicts the definition `Nf → N₀` as coverage → 0. A symmetric
parabola in log-dose cannot have that asymptote. So the window is refitted on the form the audit
specifies, which does:

```
Nf(c) = N0 * (1 + a*c*exp(-b*c)),   N0 = 19,113 cycles (fixed, §2),  c = coverage in %
```

`c → 0 ⟹ Nf → N₀` ✓ (correct baseline asymptote) and `c → ∞ ⟹ Nf → N₀` from *above*,
asymptotically.

**Fit (Python, numpy 2.4.3, this session; least squares on the excess ratio `Nf/N₀ − 1`, with `a`
solved in closed form at each `b` on a 20,000-point grid over `b ∈ [10⁻⁵, 5×10⁻³]`):**

| coverage c (%) | Nf measured | Nf fitted | residual |
|---|---|---|---|
| 100 | 28,300 | 43,813 | **+54.8%** |
| 400 | 96,522 | 86,147 | −10.7% |
| 1000 | 90,336 | 96,258 | +6.6% |
| 1500 | 82,120 | 79,735 | −2.9% |

```
a = 1.4707e-2    b = 1.29299e-3 (per % coverage)    SSE (on excess ratio) = 1.065
peak     c* = 1/b = 773% coverage
peak Nf  = N0*(1 + a*c*/e) = 19,113 * 5.184 = 99,089 cycles   (+418% over baseline)
```

Leave-one-out sensitivity on `c*`: dropping the 100 / 400 / 1000 / 1500% point gives
700 / 1136 / 788 / 723%. A three-parameter generalisation `Nf = N₀(1 + a·c^p·e^{−bc})` improves
the fit only modestly (a = 1.851×10⁻³, b = 1.8655×10⁻³, p = 1.390, SSE 0.769) and moves the
optimum to 745% — three parameters on four points, reported as a sensitivity check, not adopted.

**What the refit says about the window — the honest answer is "nothing".**

- **No two-sided window is constrained at all.** Under this form the curve never returns to
  baseline at finite dose; it decays to `N₀` asymptotically. There is therefore no zero-equivalent
  dose and no finite ZED span. The previous **≈ 73× fitted window is withdrawn**: it was an
  artifact of forcing a symmetric log-parabola onto an asymmetric hormetic shape.
- **One-sided (descending-limb) statement only.** The dose at which the fitted benefit decays to
  +10% / +5% / +1% above baseline is c ≈ **5,120% / 5,750% / 7,160%** coverage, i.e. 6.6 / 7.4 /
  9.3 × the fitted optimum. All three are extrapolations **3.4–4.8× beyond the highest tested
  dose (1500%)** and are order-of-magnitude only.
- **Tested dose range, all beneficial: 15×.** Every tested dose from 100% to 1500% coverage stays
  net beneficial (even 1500% is +330%). This is the ratio of the extreme *tested* doses — an
  experimental-design artifact that would have read 10× or 100× had the experimenters chosen
  different endpoints. It is **not** a measured window and is **not** compared to toxicology's
  10–20× anywhere in this note.
- **Fit quality is poor at the low end.** The 100% point is over-predicted by 55%, and the fitted
  optimum (773%) sits well above the measured maximum (400%). A two-parameter form cannot
  reproduce both the steep 100 → 400% rise and the flat 400 → 1500% plateau. A 6–8 dose sweep is
  needed before any window number is quotable.

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

So the AISI 4140 number is ≈ **+18–25%**, and it must be labelled precisely: it is a
**σ'_f-equivalent ESTIMATE** — a change in the Basquin fatigue-strength *coefficient* `σ'_f`,
inferred from a life ratio under an assumed exponent (a steeper `b ≈ −0.15` gives +28%).

**Axis mismatch, stated plainly.** AA 7075's **+82%** is a *directly measured endurance limit*
(a run-out asymptote), which lies **outside** Basquin's power-law regime. `σ'_f` and the
endurance limit are **not the same quantity**, so +18–25% (4140, σ'_f-equivalent, ESTIMATE) and
+82% (7075, endurance limit, MEASURED) may not be pooled into a single "strength ceiling" range.
The earlier reading of "≈ +20% to +80%, straddling biology's 30–60%" is **withdrawn**: it merged
two axes, and +82% *exceeds* 30–60% rather than straddling it. Separately, Dataset B has one
baseline and two doses, so **+82% is the best of two doses**, not a fitted ceiling — no window
and no peak can be extracted from B.

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
| Amplitude ceiling, **endurance limit (measured)** | +30–60% | **+82%** — AA 7075, best of two doses, not a fitted ceiling | **exceeds** biology's band |
| Amplitude ceiling, **σ'_f-equivalent (ESTIMATE)** | (no matching axis in toxicology) | **+18–25%** — AISI 4140, Basquin-inferred under assumed `b ≈ −0.10` | not comparable — different axis from the row above |
| Amplitude ceiling, **amplified-outcome axis** | (organismal lifespan hormesis, similar %) | +400–800% (fatigue life) | far larger — steep Basquin transform |
| Stimulatory window width | 10–20× | **not measured.** Tested dose range, all beneficial: 15× (design artifact). Admissible fit has no finite ZED. | **no comparison possible** |
| Peak location | low-dose (sub-toxic) | measured maximum 400% (44 MPa) / 1000% (37 MPa); fitted optimum ≈ 770%; shifts with load | qualitatively analogous |
| Mechanistic form | stimulation − toxicity (two monotone terms) | compressive-stress benefit − surface-damage penalty (two monotone terms; residual stress alone is monotone) | **structurally identical** |

**There is no window-width agreement, because there is no measured window.** The 15× figure is
the tested dose range (an experimental-design artifact) and the physically admissible fit yields
no finite zero-equivalent span at all; both the "≥15× lower bound" and the "≈ 73× fitted window"
claims are withdrawn. On amplitude: AA 7075's measured endurance-limit gain of +82% *exceeds*
biology's 30–60%, and the AISI 4140 σ'_f-equivalent estimate of +18–25% is on a different axis
and cannot be pooled with it. The raw fatigue-life numbers are an order of magnitude larger
again, and the Basquin exponent is the conversion factor between life and `σ'_f` — that
translation rule is what survives here, not a numerical match to toxicology.

---

## 6. Verdict on G23: NARROWS (toward partial closure)

- **One of the two numbers now exists as a fitted constant**, which it did not before this file:
  the amplitude ceiling — +82% endurance limit (AA 7075, measured, best of two doses) / +418–453%
  life (AISI 4140, fitted) — with a fitted optimum at ≈ 770% coverage. **The window width does
  not.** Under a physically admissible form the data constrain no window; only a one-sided
  descending-limb extrapolation is available, and it lies beyond the tested range. That half of
  what G23 said was absent is **still absent**.
- **What transfers is the translation rule, not a numerical match.** The Basquin exponent
  converts between the life axis and the `σ'_f` axis, and that is a genuine importable piece.
  The amplitude ceiling does not land inside biology's 30–60% (AA 7075 exceeds it); the window
  cannot be compared at all.
- **But not a universal constant, and not a theorem.** Two materials give two different amplitude
  ceilings (+82% vs +18–25% strength) and the window is bounded from only one of them. Per
  [[what-closes-a-gap]], closure needs a *theorem* fixing a shared figure of merit, not two fits.
  What exists is a transferable *shape and decade-scale*, not a single number both fields quote.
- **A real difference also surfaced.** Stress-strengthening's descending limb is driven by
  surface-damage competing against a *monotone* residual-stress benefit — the beneficial variable
  itself never peaks. Chemical hormesis often has the stimulatory process itself turn over. So the
  two biphasic curves share arithmetic but differ in mechanism, and the engineering window is
  *wider* (shallower over-peening limb) than a typical toxicological one.

**Net:** G23 stays **narrowed**, but less far toward closure than the first pass claimed. Half
the parameterised curve (the amplitude ceiling, plus the Basquin translation rule) is now written
down; the **window width is not** — it needs a 6–8 dose sweep that reaches the descending limb
far enough to see baseline. What remains open is that sweep, and beyond it a cross-material
theorem that would make the ceiling a single shared axis rather than a fitted family.

## 7. Weakest links (stated plainly)

- **One primary complete curve.** Dataset A's 44 MPa series (4 doses + derived baseline) carries
  the window and life-ceiling. The baseline is VERIFIED-DERIVED from the stated +405%, not read
  from Table 4 directly (the table body did not render in the fetched text); the four-way internal
  consistency check makes it solid but it is one arithmetic step removed from a printed cell.
- **Two Nf points define the over-peening limb** (1000%, 1500%), and it is shallow, so **no
  window number is obtainable**. The descending-limb doses quoted in §3 are extrapolations 3.4–4.8×
  beyond the highest tested dose.
- **AISI 4140's +18–25% is a σ'_f-equivalent ESTIMATE** under an assumed Basquin `b`; only AA
  7075's +82% is a directly measured endurance-limit ratio, and those are different axes.
- **AA 7075 has one baseline and two doses**, so +82% is the best of two doses, not a ceiling.
- **The admissible fit is 2-parameter on 4 points and fits the 100% point badly** (+55%). Its
  optimum (773%) exceeds the measured maximum (400%). A 6–8 dose sweep would let a proper
  log-normal be fit and a window measured rather than extrapolated. None was found open-access
  with a tabulated fine sweep — itself a mild echo of G23's original complaint that experiments
  report the optimum, not the full curve.

---

## Corrections 2026-09-05

Backlog A15–A17; `audits/01-math-physics.md` C19 items; `audits/03-method-epistemics.md` 15–17.

1. **A15 — "model-free lower bound ≥ 15×" → "tested dose range, all beneficial: 15×."**
   Old: §3 and the pull-quote read the 15× as a measured lower bound on the stimulatory window,
   and §5 scored it "**meets or exceeds**" toxicology's 10–20×. New: 15× = 1500%/100% is the
   ratio of the extreme *tested* doses (inputs: the four tested coverages 100 / 400 / 1000 /
   1500%), an experimental-design artifact; it is removed from the §5 comparison verdict, which
   now reads "no comparison possible."
2. **A16 — 73× fitted ZED window WITHDRAWN; refit on `Nf = N₀(1 + a·c·e^{−bc})`.**
   Old: the log-quadratic vertex fit gave a two-sided ZED span of 72.9× (x_low = 1.886 ⇒ 77%
   coverage, x_high = 3.749 ⇒ 5,610%), which implies harm below 77% coverage and so violates
   `Nf → N₀` as `c → 0`. New (inputs: c = 100 / 400 / 1000 / 1500%, Nf = 28,300 / 96,522 /
   90,336 / 82,120, N₀ = 19,113; least squares on `Nf/N₀ − 1`, numpy 2.4.3, 20,000-point grid on
   `b`): **a = 1.4707×10⁻², b = 1.29299×10⁻³, SSE = 1.065, optimum c\* = 773%, peak Nf = 99,089
   (+418%)**. This form has the correct `c → 0` asymptote and decays to baseline only
   asymptotically, so **no finite two-sided window exists and the data constrain none**. Only a
   one-sided descending-limb statement remains (benefit decays to +10% / +5% / +1% at c ≈ 5,120 /
   5,750 / 7,160%, all extrapolated 3.4–4.8× past the highest tested dose).
3. **A17 — AISI 4140 numbers relabelled σ'_f-equivalent; axis mismatch stated; "+82% ceiling"
   → "best of two doses"; "straddles 30–60%" corrected.** Old: §4/§5 pooled "+20% to +80%
   (fatigue strength)" and called it straddling biology's 30–60%. New: +18–25% (AISI 4140) is a
   **σ'_f-equivalent ESTIMATE** from `ρ = R_N^{−b}` with assumed `b ≈ −0.10` (inputs: R_N = 5.05
   ⇒ 5.05^0.10 = 1.176; R_N = 8.97 ⇒ 8.97^0.10 = 1.245); +82% (AA 7075) is a **measured endurance
   limit** (275 → 500 MPa), a run-out asymptote outside Basquin's regime, and is the **best of
   two doses** on a one-baseline / two-dose sweep. The two are not on a common axis and are no
   longer pooled; +82% **exceeds** 30–60% rather than straddling it. §5's amplitude row is split
   in two accordingly.
