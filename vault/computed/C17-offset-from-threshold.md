---
name: C17-offset-from-threshold
type: computed
---

# Offset from threshold is portable, but the exponent that makes it portable is a tautology — the real invariant is gain × bandwidth

> **VERDICT: the naive "distance from threshold" closes [[G4-criticality-as-design]] only in a
> weak, near-tautological sense, and the honest portable object is the gain–bandwidth product.**
>
> Define the offset as the normalized distance of the system's leading pole/eigenvalue from the
> imaginary axis, `ε`. Then across all three classes — a Hopf resonator (hair cell), a degenerate
> parametric amplifier (JPA), and a branching/avalanche process (cortex) — the **linear
> susceptibility (gain) diverges as `ε⁻¹`, with the *same* exponent `a = 1`.** But this sameness
> is not a discovered coincidence: `ε` is *defined* as the pole-to-axis distance, and the resolvent
> of a simple pole is `1/(distance)` by construction. Any codimension-1 bifurcation, reduced to its
> one leading mode, gives `a = 1`. So "the offset is a shared axis with a shared gain exponent" is
> true but empty — it says only that a simple pole is a simple pole.
>
> The content is one level down. The **bandwidth** of the response is the *same* pole distance,
> `Δ ∝ ε`, and the **settling time** (critical slowing down) is `τ ∝ ε⁻¹`. Therefore
>
> ```
> gain × bandwidth  =  (c/ε) × (rate·ε)  =  c·rate   —  independent of ε
> ```
>
> **The gain–bandwidth product is conserved along the offset axis in every class.** Sitting closer
> to threshold is provably not a free lunch: the `ε⁻¹` you gain in gain is the `ε` you lose in
> bandwidth and the `ε⁻¹` you pay in response time, exactly. This is the portable figure of merit
> that was hiding under "distance." Its verified fingerprint is the parametric-amplifier community's
> own **fixed gain–bandwidth product `B·√G = const`** (VERIFIED below) — identical content, since
> `√G` is the amplitude gain.
>
> **What does *not* collapse is the class label.** The *nonlinear response at* `ε = 0` is
> class-specific: the Hopf and parametric normal forms are both cubic and both give a **cube-root
> compression `R ∝ F^{1/3}`**; the branching process at criticality gives instead an **avalanche-size
> law `P(S) ∝ S^{-3/2}`** (mean-field directed percolation). So the fully honest portable object is
> the **pair `(ε, at-threshold universality class)`**, and the scalar invariant that survives across
> the pair is **gain × bandwidth**.
>
> This is the same shape as [[C8-momentum-harvesting-metric]]: a quantity that is defined and
> comparable everywhere (`Σ` there, `ε` here), sitting beside a second object that provably does not
> generalise (`max Σ` there, the at-threshold exponent here). See [[specification-instruments]].

---

## 0. What G4 actually asks, in its surviving form

The gap, full-text-read and narrowed, is down to one sentence: hair cells sit just below a Hopf
bifurcation, parametric amplifiers just below their pump threshold, cortex at a branching ratio
`m ≈ 0.98` rather than `1`. All three know to sit **near but not at** the instability. **There is no
shared number for "how far below," comparable across the three.** This note builds that number, then
asks the only question that decides whether it is worth anything: is it the *same* number — same
scaling — or three different curves wearing one name.

---

## 1. The candidate metric, per class

The natural object is the **normalized distance of the leading eigenvalue/pole from the imaginary
axis.** Write the slowest relaxation rate as `s` (units 1/time); `s > 0` on the stable side, `s = 0`
at the bifurcation. Normalize by the natural rate scale of the class to get a dimensionless offset
`ε`.

### 1.1 Hopf resonator (hair cell)

Normal form for the complex hair-bundle amplitude `z`, forced at the characteristic frequency `ω₀`
(Camalet–Duke–Jülicher–Prost; Eguíluz–Ospeck–Choe–Hudspeth–Magnasco):

```
ż = (μ + iω₀) z − b|z|² z + F e^{iω₀ t}
```

The linear eigenvalue pair is `λ = μ ± iω₀`. Its real part `μ` is the control parameter: `μ < 0`
quiescent (stable), `μ = 0` the Hopf bifurcation, `μ > 0` spontaneous oscillation. The leading pole
sits a distance `|μ|` from the imaginary axis, so

```
ε_Hopf ≡ |μ| / ω₀            (real part of the eigenvalue pair, normalized by the imaginary part)
```

### 1.2 Degenerate parametric amplifier (JPA)

Cavity linewidth `κ`, parametric pump rate `λ` (∝ pump amplitude). Quadrature equations of motion:

```
Ẋ₁ = (−κ/2 + λ) X₁ + √κ X₁^in      (amplified quadrature)
Ẋ₂ = (−κ/2 − λ) X₂ + √κ X₂^in      (squeezed quadrature)
```

The amplified quadrature's pole is at `−(κ/2 − λ)`; it reaches the axis at the **threshold**
`λ_th = κ/2`. So

```
ε_para ≡ 1 − λ/λ_th = 1 − p/p_th        (pump amplitude below threshold, normalized to threshold)
```

and the pole distance is `κ/2 − λ = (κ/2)·ε_para`.

### 1.3 Branching / avalanche process (cortex)

Subcritical branching (Galton–Watson / Hawkes / AR(1)) with branching ratio `m` — the mean number of
descendant spikes per spike. Mean activity obeys `⟨A_{t+1}⟩ = m⟨A_t⟩ + drive`, so the discrete
eigenvalue is `m`; in continuous time the relaxation rate is `s = −ln m /Δt ≈ (1−m)/Δt`. The offset is

```
ε_branch ≡ 1 − m
```

the distance of the multiplier `m` from the critical value `1`.

**All three `ε` are the same geometric object** — normalized distance of the leading mode's pole from
the stability boundary — expressed in each field's native control parameter. That much *is* a free
unification: the axis exists and every system has a value on it. The question is whether points on it
mean the same thing.

---

## 2. THE CRUX — gain versus offset. Is it the same exponent?

Gain near a bifurcation diverges as `gain ∼ ε^{-a}`. If `a` is shared, the offset is a genuine common
axis; if not, each class trades offset for gain on a different curve and only the pair `(ε, a)` is
portable. **Derivations, not assertions.**

### 2.1 Hopf — linear susceptibility `∝ ε⁻¹`, cube-root compression at `ε = 0`

Seek the steady on-resonance response `z = R e^{iω₀ t}`, `R` real ≥ 0. Substituting and cancelling
`e^{iω₀t}` (on the stable side `μ = −|μ|`):

```
0 = −|μ| R − b R³ + F        ⇒        F = |μ| R + b R³            (★)
```

Two regimes fall straight out of (★):

- **At the bifurcation** `|μ| = 0`: `F = bR³ ⇒ R = (F/b)^{1/3}`. **Cube-root compression, exponent
  1/3.** The differential gain `dR/dF ∝ F^{-2/3} → ∞` as `F → 0`: the "essential nonlinearity" —
  sharper the softer the sound (Eguíluz et al., VERIFIED §5).
- **Below the bifurcation**, small `F` (linear term dominates, `|μ|R ≫ bR³`): `R ≈ F/|μ|`. The linear
  susceptibility is

  ```
  χ_Hopf = R/F = 1/|μ| = 1/(ω₀ ε_Hopf)   ∝  ε_Hopf⁻¹          ⇒   a = 1
  ```

  The two regimes meet at the crossover force `F* ∼ |μ|^{3/2}/√b ∝ ε^{3/2}`: below `F*`, gain is the
  linear `ε⁻¹`; above, the system is driven onto the critical cube root.

### 2.2 Parametric amplifier — amplitude gain `∝ ε⁻¹`, power gain `∝ ε⁻²`

Input–output relation `X^out = √κ X − X^in` on the steady state `X₁ = √κ X₁^in/(κ/2 − λ)`:

```
g ≡ X₁^out/X₁^in = κ/(κ/2 − λ) − 1 = (κ/2 + λ)/(κ/2 − λ)
```

Write `λ = λ_th(1 − ε) = (κ/2)(1 − ε)`:

```
g = (κ/2 + (κ/2)(1−ε)) / ((κ/2)ε) = (2 − ε)/ε ≈ 2/ε_para   (small ε)   ⇒   a = 1 (amplitude)
```

The **power gain** `G = g² ≈ 4/ε²` diverges as `ε⁻²`. This is the one place a naive reading gets
"different exponents": amplitude vs power. It is a bookkeeping choice, not a physical difference — the
Hopf `χ` and the branching `⟨S⟩` are *also* amplitude/linear-response quantities, so the like-for-like
comparison is amplitude gain, and **`a = 1` in all three.** Stated in power, all three are `a = 2`
consistently. The exponent is shared; one must only not compare an amplitude to a power.

### 2.3 Branching — susceptibility `∝ ε⁻¹`

A single seed spike spawns `m` on average, each of which spawns `m`, ad infinitum. Expected total
avalanche size (the DC susceptibility, response of integrated activity to a unit input):

```
χ_branch = ⟨S⟩ = Σ_{k≥0} m^k = 1/(1 − m) = 1/ε_branch    ∝ ε_branch⁻¹    ⇒   a = 1
```

At criticality `m = 1` the sum diverges and the avalanche-size distribution is the mean-field
directed-percolation power law `P(S) ∝ S^{-3/2}` (exponent τ = 3/2) — the class-specific object that
replaces the cube root (§4).

### 2.4 Why `a = 1` is universal — and why that makes the closure honest but shallow

The three derivations are one derivation. `ε` was *defined* as the normalized distance of the leading
pole from the imaginary axis. A codimension-1 bifurcation, reduced to its single slow mode, has a
resolvent (linear response at the resonant or DC frequency)

```
χ(ω_res) = c / (leading pole distance) = c / (rate · ε)   ∝  ε⁻¹.
```

A simple pole approaching the axis **forces** peak susceptibility `∝ ε⁻¹`. So the shared exponent is
not evidence of a deep common mechanism; it is the statement that all three headline numbers (`μ`,
`p/p_th`, `m`) are, by construction, the same simple-pole distance. **The offset closes G4's surviving
sentence — a shared, comparable "how far below" with a shared gain law — but it closes it the way
"both are simple poles" closes it.** The real physics is in what §2.4's universality *cannot* reach:
the bandwidth trade (§3) and the nonlinear class label (§4).

---

## 3. THE REAL DESIGN TRADE — gain × bandwidth is the conserved invariant

Sitting closer to threshold buys gain but costs bandwidth (the resonance narrows), noise/stability
margin (fluctuations diverge), and settling time (critical slowing down). The claim to test: is
**gain × bandwidth** the quantity actually conserved along the offset axis in each class?

The same simple-pole structure that forced `a = 1` fixes this too. The response is a Lorentzian whose
**half-width equals the pole distance**:

```
Δ (bandwidth)  ∝  pole distance  ∝  ε          (rate · ε, same rate as the gain denominator)
τ (settling)   =  1/(pole distance) ∝ ε⁻¹      (critical slowing down)
```

Multiply:

```
gain × bandwidth = (c / (rate·ε)) × (rate·ε) = c   —   independent of ε.       (INVARIANT)
```

Per class, explicitly:

| Class | gain (amplitude) | bandwidth Δ | settling τ | gain × Δ |
|---|---|---|---|---|
| **Hopf** | `1/|μ|` | `∝ |μ|` (resonance half-width = `|μ|`) | `1/|μ|` | **const** |
| **Parametric** | `2/ε` | `(κ/2)ε` (amplified-quadrature linewidth) | `2/(κε)` | **const** |
| **Branching** | `1/(1−m)` | `∝ (1−m)/Δt` (= `1/τ`, AR(1) corner freq.) | `Δt/(1−m)` | **const** |

So the trade is universal and tight: **gain ↑ `ε⁻¹`, bandwidth ↓ `ε`, response time ↑ `ε⁻¹`, product
fixed.** The parametric-amplifier field states exactly this as its own design law — the **fixed
gain–bandwidth product `B·√G = const`** (VERIFIED, §5), and since `√G` *is* the amplitude gain, that
is `amplitude-gain × bandwidth = const`, i.e. this invariant, already published inside one of the
three classes. Neither of the other two fields writes it, and it transfers to both unchanged. **That
is the portable figure of merit under the naive "distance."**

Note it also cleanly reframes the "how far below" design choice: you do not choose `ε`, you choose a
required bandwidth (a stimulus frequency resolution for the cochlea, a readout bandwidth for the JPA,
an integration window for cortex). The invariant then *fixes* the gain you can have, and `ε` is the
dependent variable. Cortex's `m ≈ 0.98` is not a free set-point; given an integration time of a few
hundred ms (§4) it is *the* offset the invariant allows.

---

## 4. Populated — real operating points

Every number carries `VERIFIED` (fetched this session, URL given) or `UNVERIFIED`.

| System | control param | offset `ε` | linear gain `∼ ε⁻¹` | at-threshold class | source / status |
|---|---|---|---|---|---|
| **Cortex** (in-vivo spiking, monkey PFC / cat V1 / rat hippocampus) | `m = 0.98` (median; range 0.963–0.998, 4 ms bins) | **`ε = 0.02`** (0.002–0.037) | `⟨S⟩ = 1/(1−m) = 50` (27–500) | avalanche `P(S)∝S^{-3/2}`, mean-field DP | **VERIFIED** — Wilting & Priesemann, *Nat. Commun.* 9:2325 (2018), values via [arXiv:1804.07864](https://arxiv.org/abs/1804.07864) / [nature.com/articles/s41467-018-04725-4](https://www.nature.com/articles/s41467-018-04725-4). τ = 100 ms–2 s, median **247 ms**, consistent with `τ = Δt/(1−m)`. |
| **Josephson parametric amplifier**, at the conventional 20 dB operating gain | `p/p_th ≈ 0.82` | **`ε ≈ 0.18`** | amplitude gain `√G = 10`, power `G = 100` | cube-root saturation `R∝F^{1/3}` (cubic normal form) | Gain formula `G = [(1+p/p_th)/(1−p/p_th)]²` standard; `G = 100 ⇒ p/p_th = 9/11 = 0.818 ⇒ ε = 0.18` **computed** from it. 20 dB as the standard JPA operating point **VERIFIED** qualitatively ([EPJ Quantum Tech. review, springer 10.1140/epjqt2](https://link.springer.com/article/10.1140/epjqt2); [arXiv:2305.04184](https://arxiv.org/pdf/2305.04184)). The exact `p_th` of any specific device: **UNVERIFIED** (device PDFs returned undecodable binary). |
| **Hair-cell / Hopf bundle** (bullfrog sacculus, active bundle) | `μ` (real part) | **`ε` a few ×10⁻² : UNVERIFIED numerically** | `χ = 1/|μ|`; observed compression over ~ two decades of level | cube-root compression `R∝F^{1/3}` | Cube-root essential nonlinearity + operation *at/near* the Hopf point **VERIFIED** — Eguíluz–Ospeck–Choe–Hudspeth–Magnasco, *PRL* 84:5232 (2000), [arXiv:nlin/0005042](https://arxiv.org/abs/nlin/0005042); Camalet–Duke–Jülicher–Prost, *PNAS* 97:3183 (2000). A *numeric* `μ` for a specific bundle was **NOT OBTAINED** this session (PNAS 403, PDF binary). The bundle self-tunes to `μ ≈ 0⁻`, which is the qualitative content; the exact residual `ε` is the unmeasured quantity. |

**Reading of the table.** The offset spans `ε ≈ 0.02` (cortex, deepest into the sub-threshold,
gain 50) to `ε ≈ 0.18` (JPA at 20 dB, gain 10) — and this ordering is now *meaningful* because all
three sit on one axis with one gain law. Cortex runs at the highest gain / narrowest bandwidth /
longest memory of the three, which is exactly the "reverberating regime" reading: `ε = 0.02` is a
~250 ms integration window, deliberately not `m = 1`. The JPA, needing readout bandwidth, sits an
order of magnitude further out. The hair cell self-tunes toward the smallest `ε` any of them targets,
but the residual is precisely the number the field has not pinned — the honest open value.

---

## 5. Verification log

| Claim | Status | Fetch |
|---|---|---|
| Cortex `m` median 0.98, range 0.963–0.998 (4 ms), τ 100 ms–2 s median 247 ms, reverberating (not `m=1`) | **VERIFIED** | search-resolved from [arXiv:1804.07864](https://arxiv.org/abs/1804.07864) and Wilting & Priesemann *Nat. Commun.* 9:2325 (2018), [s41467-018-04725-4](https://www.nature.com/articles/s41467-018-04725-4) |
| Fixed gain–bandwidth product for parametric amplifiers, `B·√G = const` | **VERIFIED** | [arXiv:2305.04184](https://arxiv.org/pdf/2305.04184) ("fixed gain-bandwidth product", `κ̄ ≈ B√G`); corroborated [springer 10.1140/epjqt2](https://link.springer.com/article/10.1140/epjqt2) |
| Hopf cochlear amplifier: cube-root / essential compressive nonlinearity, operation at Hopf point | **VERIFIED** | Eguíluz et al. *PRL* 84:5232 (2000), [arXiv:nlin/0005042](https://arxiv.org/abs/nlin/0005042) (title/finding: "compression of the dynamic range… essentially nonlinear… more marked the smaller the forcing") |
| JPA standard operating gain ≈ 20 dB | **VERIFIED (qualitative)** | JPA reviews above; the 20 dB → `ε = 0.18` mapping is **computed** from the standard gain formula, not measured on a device |
| Exact `p_th` of a named JPA device; numeric `μ`/`ε` of a named hair bundle | **UNVERIFIED / NOT OBTAINED** | PNAS 403; device and Camalet PDFs returned undecodable binary this session |
| All scaling derivations (§2, §3) | **derivation, self-contained** | normal-form / input–output / branching algebra above; no external number needed |

---

## 6. Verdict on G4

- **Does the offset close G4?** In the weak sense, **yes**: `ε` is defined in all three classes, every
  system has a value, and the linear gain obeys the *same* law `∝ ε⁻¹` (`a = 1` amplitude, `a = 2`
  power, consistently). But this shared exponent is **forced by the definition of `ε` as a simple-pole
  distance** — it is a tautology, not a discovered unification. Closing G4 on it alone would be
  closing it on "a simple pole is a simple pole."
- **Do the exponents differ?** For the *linear* gain, no. For the **nonlinear response at threshold,
  yes** — Hopf and parametric share the cubic-normal-form cube root `R ∝ F^{1/3}`; branching gives
  the mean-field avalanche law `P(S) ∝ S^{-3/2}` instead. So the fully honest portable object is the
  **pair `(ε, at-threshold universality class)`**, and only the first component is class-free.
- **Is gain–bandwidth the hidden invariant?** **Yes — this is the real result.** `gain × bandwidth`
  (equivalently `gain / settling-time-rate`) is **conserved along the offset axis in all three
  classes**, `= c·rate`, independent of `ε`. It is the quantity the parametric-amplifier field
  already publishes as its `B·√G = const` law, and it transfers unchanged to the cochlea and to
  cortex, neither of which states it. The offset is what you read; **the gain–bandwidth product is
  what is actually conserved**, and it makes the design trade exact: closer to threshold buys gain
  only by spending bandwidth and response time in the same proportion.

**Recommended standing for [[G4-criticality-as-design]]: NARROWED, and the narrowing is a
construction.** From "no shared number for distance-from-threshold" to: the offset `ε` is a shared
axis with a *tautologically* shared linear-gain exponent; the substantive shared figure of merit is
the **gain–bandwidth invariant** `gain × Δ = const`; and the one object that genuinely does not
collapse across the three is the **at-threshold universality class** (cube root for the two
cubic-normal-form amplifiers, `S^{-3/2}` avalanches for the branching process). Portable: `ε` and
`gain × bandwidth`. Not portable: the nonlinear exponent. Same cleavage as
[[C8-momentum-harvesting-metric]] — a metric defined everywhere beside an optimum/exponent that is
not.

See [[specification-instruments]] and [[what-closes-a-gap]].
