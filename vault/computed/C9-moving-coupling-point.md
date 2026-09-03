---
name: C9-moving-coupling-point
type: computed
---

# Moving the coupling point does not evade `q`. It is a Péclet number, and it is thermoacoustics.

> **The claim in [[C8-momentum-harvesting-metric]] §5 — that a harvester whose coupling point
> is driven through the gradient "would not be bounded by `q` at all" — is WRONG, and the
> error is locatable in one line.** `q` is not a bound that assumes a static coupling point.
> `q` is the degree of coupling of *whatever* Onsager matrix you write down. Moving the
> coupling point adds a mechanical conjugate pair `(F, v)` — which [[C8-momentum-harvesting-metric]]
> §3.2 itself established is a legitimate Onsager pair — so the matrix goes from 2×2 to 3×3.
> The optimum still collapses to a coefficient. It collapses to the degree of coupling of the
> **Schur complement**, `q'² = L'₁₂²/(L'₁₁L'₂₂)` with `L'ᵢⱼ = Lᵢⱼ − Lᵢ₃L₃ⱼ/L₃₃`.
>
> Outcome **(b)**, delivered as outcome **(c)**. A modified bound exists, it is computable, and
> it is **monotonically worse** than the static one:
>
> ```
> ZT_eff  =  ZT / (1 + (1−ε)·Pe) ,      Pe ≡ v L / α_th ,      q'² = ZT_eff/(1+ZT_eff)
> ```
>
> `Pe` is the **thermal Péclet number of the moving element** — translation speed times element
> length over thermal diffusivity — and `ε` is the fraction of the advected heat returned on the
> back-stroke. `ZT_eff ≤ ZT` with equality **only** at `v = 0` or `ε = 1`. Moving the coupling
> point cannot raise the degree of coupling. A perfect regenerator can at best *restore* it.
>
> **And a device that carries heat along a gradient and gives it back on the return stroke is a
> regenerator. This is Stirling (1816) and thermoacoustics.** Travelling-wave thermoacoustic
> engines are exactly the case where the working medium is advected along the temperature
> gradient with the phasing that makes each parcel run a Stirling cycle; the field's own
> headline number is *fraction of Carnot*, and its entire design effort goes into `ε`. There is
> no unexplored corner here. The corner is a mature engineering discipline with a `1/(1+(1−ε)Pe)`
> penalty it has been fighting for two centuries under a different name.
>
> **One genuine exception, already known and already quantified: transient Peltier operation.**
> Cycling *does* beat steady-state `ZT`, for times shorter than the element's thermal diffusion
> time, because Peltier cooling is localised at the junction while Joule heat is volumetric and
> arrives late. The gain is repaid, the COP falls with frequency, and the literature says so.
> **This closes by discovery.**
>
> **Recommendation: do not build [[buildable]] item 7.** The calculation it asked for has been
> done, and it says the device is a worse Stirling engine.

Bears on [[G1-gradient-coupling]] and [[kedem-caplan]].

---

## 1. Setup — and "moving the coupling point" is three different problems

The phrase in [[C8-momentum-harvesting-metric]] names three physically distinct machines. They
must be separated before anything can be derived.

| # | Name | Physical content | Where it lives |
|---|---|---|---|
| **A** | **Advection of the working medium** | The medium that couples the reservoirs *flows* along the gradient. Heat and charge are carried by material transport, not only by conduction. | **Thermoacoustics, Stirling regenerators, pulse tubes.** §2. |
| **B** | **Translated coupling element / moving contact** | A solid converter of finite length `L` is mechanically driven along a bar carrying a fixed profile `T(x)`, making and breaking thermal contact. | **The literal reading of C8's claim.** Derived in §3–§4. |
| **C** | **Periodically modulated coupling coefficient `L₁₂(t)`** | Nothing translates; the coupling itself is switched. | **Flashing ratchets, periodically driven Onsager theory.** §2. |

**I derive B**, because it is the literal reading of the C8 sentence and because A and C are
already answered by existing literature (§2). B is also the cleanest: it is a genuine steady
state in the co-moving frame, so linear response applies with a *static* enlarged coefficient
matrix, and one can ask the question sharply rather than in a Floquet expansion.

**Concrete device.** A single thermoelectric leg (cleanest of the three offered — thermoelectric,
osmotic, electrokinetic — because `q² = ZT/(1+ZT)` gives a directly tabulated benchmark). Cross
section `A`, length `L` along the direction of motion, Seebeck `α`, electrical conductance `G`,
thermal conductance `K = κA/L`, volumetric heat capacity `ρc_p`. It is driven at velocity `v`
along a bar whose temperature profile `T(x)` is held fixed by two reservoirs at `T_h`, `T_c`.
Electrical output is taken through sliding leads. A pump supplies the force `F` to move it.

### 1.1 The moving-frame Onsager equations

The move that decides the whole problem is the one [[C8-momentum-harvesting-metric]] §3.2 already
made and then failed to apply here: **`F·v/T` is a bilinear conjugate flux–force pair in exactly
the Onsager sense.** So the local entropy production of the moving converter is not two terms but
three:

```
σ  =  J₁·X₁  +  J₂·X₂  +  J₃·X₃                                       (1)

X₁ = −∇(μ/T)     electrochemical force     J₁ = particle/charge flux
X₂ = ∇(1/T)      thermal force             J₂ = heat flux
X₃ = F/T         mechanical force          J₃ = v   (the translation velocity)
```

In the co-moving frame the medium streams past at `−v`, and the balance laws pick up advective
terms `∇·(n v)` and `∇·(s v)`. Those advective terms are precisely what the third row and column
of the matrix encode. Linear response, time-reversal symmetric, no magnetic field:

```
⎛J₁⎞   ⎛L₁₁ L₁₂ L₁₃⎞ ⎛X₁⎞
⎜J₂⎟ = ⎜L₂₁ L₂₂ L₂₃⎟ ⎜X₂⎟ ,     L = Lᵀ ,   L ⪰ 0                       (2)
⎝J₃⎠   ⎝L₃₁ L₃₂ L₃₃⎠ ⎝X₃⎠
```

`L₃₃` is a mechanical mobility: `1/L₃₃` is the drag coefficient (viscous, bearing friction,
sliding contact) divided by `T`. `L₂₃` is the *thermophoretic/advective* cross coefficient — the
heat dragged by the motion. `L₁₃` is charge dragged by the motion.

**This is the whole refutation in structural form.** [[kedem-caplan]]'s derivation does not assume
the coupling point is fixed. It assumes *a set of conjugate pairs*. Moving the coupling point
does not step outside the framework; it **enlarges the framework by one pair**, which is the one
[[C8-momentum-harvesting-metric]] had already identified.

---

## 2. Prior art — and the first three rows are the answer

Searched this session. **Every one of the three variants is occupied, and two of them are
mature engineering disciplines.**

| Source | Checked how | What it settles |
|---|---|---|
| **Scalo, Lele & Hesselink**, *Linear and Nonlinear Modeling of a Traveling-Wave Thermoacoustic Heat Engine*, [arXiv:1408.4176](https://arxiv.org/abs/1408.4176), *J. Fluid Mech.* (2014) | abstract **VERIFIED by fetch** | Variant **A**, exactly. Quoted verbatim: "such thermoacoustic instability is a **Lagrangian thermodynamic process resembling a Stirling cycle**", driven by "a network of traveling waves amplified by looping around the REG/HX unit **in the direction of the imposed temperature gradient**." A working medium displaced along a temperature gradient, executing a cycle. This *is* the device C8 proposed, in a field with its own journals. |
| Thermoacoustic-Stirling engine performance: Backhaus & Swift, 710 W acoustic, thermal efficiency 0.30 ≈ **41% of Carnot**; travelling-wave phasing argued to reach ~70% of Carnot | via **search snippet only**; *Nature* 403 | **UNVERIFIED at primary source.** Reported here because the *form* of the number is the finding: the field quotes performance as **a fraction of Carnot**, which is [[what-closes-a-gap]]'s own signature of a CLOSED literature. The specific figures should not be quoted onward without a fetch. |
| **Bezsudnov & Snarskii**, *Rotating thermoelectric device in periodic steady state*, [arXiv:1409.1969](https://arxiv.org/abs/1409.1969) (2014) | **VERIFIED by fetch** | Variant **C** on a thermoelectric leg. Quoted: "The efficiency and the cooling temperature of rotating (TE) device was found to depend **not only on the dimensionless TE figure of merit, but also upon an additional dimensionless parameter**" incorporating "rotation period, conductor size, and thermal diffusivity." **That additional parameter is a Péclet number**, and this note's §4 rederives it. Someone got here in 2014. |
| **Proesmans & Van den Broeck**, *Onsager Coefficients in Periodically Driven Systems*, **Phys. Rev. Lett. 115, 090601 (2015)**, [arXiv:1507.00841](https://arxiv.org/abs/1507.00841) | abstract **VERIFIED by fetch**, quoted verbatim | Variant **C**, general. "We evaluate the Onsager matrix for a system under time-periodic driving by considering all its Fourier components. By application of the second law, we prove that all the fluxes converge to zero in the limit of zero dissipation. **Reversible efficiency can never be reached at finite power.** The implication for an Onsager matrix, describing reduced fluxes, is that its determinant has to vanish. **In the particular case of only two fluxes, the corresponding Onsager matrix becomes symmetric.**" — i.e. periodic driving does not even break reciprocity for two fluxes, and the power–efficiency trade-off survives. |
| **Gómez-Marín & Sancho**, *Tight coupling in thermal Brownian motors*, **Phys. Rev. E 74, 062102 (2006)**, [arXiv:cond-mat/0609069](https://arxiv.org/abs/cond-mat/0609069) | **VERIFIED by fetch** | Ratchet with a moving/modulated coupling. "the reciprocity relation holds and **the determinant of the Onsager matrix vanishes**", which "implies that the device is built with **tight coupling**", and "explains why Carnot's efficiency can be achieved **in the limit of infinitely slow velocities**." Ratchets reach `q = 1` — **at `v → 0`**. Exactly the trade this note derives. |
| **Brandner & Seifert**, *Multi-terminal thermoelectric transport in a magnetic field: bounds on Onsager coefficients and efficiency*, **New J. Phys. 15, 105003 (2013)** | **VERIFIED by fetch**, abstract quoted | The general theorem for the enlarged matrix: "We derive a **universal bound on the Onsager coefficients** that depends only on the number of terminals. This bound implies **bounds on the efficiency** and on efficiency at maximum power." And the machinery is the same one §3 uses: the effective kinetic coefficient matrix "represents **the Schur complement**", with "a fair amount of original matrix algebra for doubly substochastic matrices and their Schur complements." **Adding channels does not remove the bound; it replaces it with an n-dependent one.** |
| **Mazza, Bosisio, Benenti, Giovannetti, Fazio & Taddei**, *Thermoelectric efficiency of three-terminal quantum thermal machines*, **New J. Phys. 16, 085001 (2014)**, [arXiv:1404.0924](https://arxiv.org/abs/1404.0924) | **VERIFIED by fetch** | Explicitly gives "analytical expressions for the efficiency at maximum power, which can be written in terms of **generalized figures of merit**." The three-channel machine has a figure of merit. It is not unbounded. |
| **Liu, Cheng, Malen & Xiong**, *Thermoelectric active cooling for transient hot spots in microprocessors*, *Nat. Commun.* (2024), [PMC11106063](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11106063/fullTextXML) | full text **VERIFIED by fetch**, quoted verbatim | The one real exception, with its cost stated. Mechanism: "instantaneous Peltier cooling at the cold side of the device can further depress temperatures **before it is opposed by parasitic Joule heat, that is generated volumetrically and takes time to diffuse**." Cost: "the additional electrical energy input will result in Joule heating that increases the second order harmonic temperature and the steady-state temperature", and "when the frequency is sufficiently high, **COP_trans decreases exponentially** with increasing square root value of operating frequency." |

**Classification under [[what-closes-a-gap]]: NOT A GAP — CLOSED, three times over.**
Variant A is thermoacoustics. Variant C is periodically driven stochastic thermodynamics *and*
has a 2014 thermoelectric paper that already found the extra dimensionless parameter. Variant B,
the one derived below, sits between them and is bounded by the same algebra.

---

## 3. Derivation — the Schur complement, and the apparent win

### 3.1 Eliminating the driven channel

The motion is *prescribed*: the pump sets `v`, and `X₃ = F/T` is whatever it has to be. From the
third row of (2):

```
X₃  =  ( v − L₃₁X₁ − L₃₂X₂ ) / L₃₃                                     (3)
```

Substitute into rows 1 and 2:

```
Jᵢ  =  Σ_{j=1,2} L'ᵢⱼ Xⱼ  +  (Lᵢ₃/L₃₃)·v ,     i = 1,2

L'ᵢⱼ  ≡  Lᵢⱼ − Lᵢ₃L₃ⱼ/L₃₃                                              (4)
```

`L'` is the **Schur complement** `L/L₃₃`. Two consequences, both exact:

**(i) The algebra of `q` survives verbatim.** The Schur complement of a positive-semidefinite
symmetric matrix is positive-semidefinite and symmetric. So `L'` is a legitimate 2×2 Onsager
matrix, reciprocity holds in it, and

```
q'²  ≡  L'₁₂² / (L'₁₁ L'₂₂)  ∈  [0,1] ,     max η  =  η_C · (√(1+ZT_eff) − 1)/(√(1+ZT_eff) + 1)

with   q'²  =  ZT_eff/(1 + ZT_eff)                                      (5)
```

**The optimum still collapses to a coefficient.** This is the precise point on which
[[C8-momentum-harvesting-metric]] §5 is wrong. C8 §3.3 correctly identified that the *momentum*
branch loses the collapse-to-a-coefficient property because a cyclic vehicle's return cost is not
a local state function. It then assumed the same failure transfers to a cyclically driven
*thermodynamic* harvester. It does not: at steady `v` the moving converter has a genuine steady
state in its own frame, and the coefficient exists.

**(ii) A pump term appears.** `(Lᵢ₃/L₃₃)·v` is a flux at *zero* thermodynamic force — the
signature of a Brownian motor. It is real, and it is what makes the structure look promising.

### 3.2 The apparent win, stated as strongly as it can be

Take the case that looks best: the motion drags heat but not charge, `L₁₃ = 0`, `L₂₃ ≠ 0`. Then

```
L'₁₁ = L₁₁ ,   L'₁₂ = L₁₂ ,   L'₂₂ = L₂₂ − L₂₃²/L₃₃  <  L₂₂

⟹   q'²  =  L₁₂² / [L₁₁(L₂₂ − L₂₃²/L₃₃)]  =  q² · L₂₂/(L₂₂ − L₂₃²/L₃₃)   >  q²   (6)
```

**The effective degree of coupling is raised.** As `L₂₃² → L₂₂L₃₃` — the positive-semidefinite
boundary — `q' → 1`, so `ZT_eff → ∞` and `max η → η_C`. Algebraically the bound *is* evaded: the
static `q` of the material no longer bounds the device.

This is (6) taken at face value, and it is the reason the C8 conjecture is not stupid. It is also
wrong, for a reason that is entirely bookkeeping, and §4 is where it dies.

---

## 4. Where it dies — the accounting, in full

### 4.1 The Schur complement moved the leak, it did not remove it

`L₂₂` is the leg's thermal conductance: the parasitic channel that makes `ZT` finite. Equation (6)
reduces it. Ask what physically happened.

Eliminating `X₃` at fixed `v` means: *of the heat flowing through the cross-section, the part that
is slaved to the prescribed motion has been reclassified as "advected" and taken out of `J₂`.* It
has not stopped flowing. It is still leaving the hot reservoir and it is still arriving somewhere
cold. The Schur complement made the leg look stiffer by relabelling a heat current, not by
stopping one.

Put it back. Let `c ≡ ρc_p A` be the heat capacity per unit length of the moving element. Each
second the element carries `c·v·ΔT` of heat from hot to cold as pure convection, extracting **no
work**. Let `ε` be the fraction returned to the hot side on the back-stroke (`ε = 0`: shuttled
straight to cold; `ε = 1`: perfectly returned). The residual advected heat load is a parasitic
thermal conductance **in parallel with the leg**:

```
K_para  =  (1 − ε)·c·v                                                  (7)
```

so the honest effective thermal conductance is `K + (1−ε)cv`, and

```
             α² G T                    ZT
ZT_eff  =  ───────────────  =  ─────────────────                        (8)
           K + (1−ε)c v          1 + (1−ε)·Pe
```

where, dividing (7) by `K = κA/L`,

```
      (1−ε) ρc_p A v            v L                        κ
Pe ≡  ──────────────  ÷ (1−ε) = ───   ,    α_th  ≡  ──────────           (9)
          κA/L                  α_th                   ρ c_p
```

**`Pe` is the thermal Péclet number of the moving element** — precisely the group [[METHOD]] §9
tabulates. This is the "additional dimensionless parameter" Bezsudnov & Snarskii reported in 2014
(**VERIFIED**, §2), arrived at from the other direction.

> **The cancellation, stated exactly.** The Schur complement lowers `L₂₂` by `L₂₃²/L₃₃`. The
> advected heat load raises the physical thermal conductance by `(1−ε)cv`. Netting them,
> `ZT_eff = ZT/(1 + (1−ε)Pe) ≤ ZT`, with equality **iff `v = 0` or `ε = 1`**.
>
> The apparent gain in (6) is a positive-semidefiniteness statement about a matrix; the loss in
> (8) is the same heat, counted where it actually goes. **Moving the coupling point cannot raise
> the degree of coupling of a converter. At best a perfect regenerator restores the value it
> would have had standing still.**

And a device whose entire job is to carry heat one way and give it back on the return stroke, so
that `ε → 1`, **is a regenerator.** That is Stirling's 1816 patent and the `ε` in every
thermoacoustic paper. The field's whole engineering effort goes into `ε` for exactly this reason.

### 4.2 The cost of the motion

`ZT_eff ≤ ZT` already settles it, but the drag has not been charged yet, and it is a second,
independent penalty. From (3) with `X₁ = X₂ = 0`:

```
σ  =  J₃X₃  =  v²/L₃₃  >  0        ⟹     P_drag  =  T v² / L₃₃  ≡  γ v²   (10)
```

Pure viscous dissipation, quadratic in `v`, unavoidable, and the pump pays it. Note the shape of
the trade: **the Brownian-motor pump term in (4) is linear in `v`; the drag is quadratic.** There
is a finite optimum `v`, but it optimises a quantity that is already `≤` the static value.

### 4.3 Contact make-and-break

Variant B breaks and remakes thermal contact each cycle. Bringing an element of heat capacity
`C = ρc_p A L` from `T₁` into contact with a reservoir at `T₂` generates

```
ΔS  =  C[ ln(T₂/T₁) + T₁/T₂ − 1 ]  ≈  C (ΔT)² / (2T²)                   (11)
```

irreversibly, i.e. lost work `T ΔS ≈ C(ΔT)²/(2T)` **per contact event**. §5 puts a number on this
and it is the single most damaging term in the balance.

### 4.4 The full balance, per cycle

```
IN      Q_h        from the hot reservoir  =  Q_cond + (1−ε)·c v ΔT · τ
        W_pump     from the drive          =  γ v² τ  +  Σ_contacts T ΔS  +  (elastic/bearing)

OUT     W_elec     electrical              =  η(ZT_eff) · Q_h
        Q_c        to the cold reservoir

NET     W_net  =  W_elec − W_pump  =  Q_h − Q_c   ≤  η_C Q_h             (12)

        η_net  =  [ η(ZT_eff)·Q_h − γv²τ − Σ T ΔS ] / Q_h   <   η(ZT_eff)  ≤  η(ZT)
```

Three strict inequalities, three independent mechanisms, all pointing the same way. **A device
that "beats `q`" in the Schur-complement bookkeeping and pays for it in the pump has beaten
nothing**, which is precisely the trap the brief named.

### 4.5 Where a real gain does exist, and why it does not help here

Everything above assumes a steady state in the moving frame — `Pe` is a ratio of *steady*
conductances. If the cycle is faster than the element's thermal diffusion time `L²/α_th`, no
steady state is reached and `ZT` is not the operative object at all. That regime is **transient
Peltier operation**, and it genuinely beats steady-state `ZT` — verified, quoted in §2 — because
Peltier cooling is a *surface* effect at the junction while Joule heating is *volumetric* and
arrives by diffusion. The gain is a timing arbitrage against a diffusion delay, not a change in
the coupling.

It is also repaid: the same source states the extra electrical input raises the steady-state
temperature, and that `COP_trans` falls exponentially in `√f`. **Cycling buys depth, not
efficiency.** For a *generator* — which is what item 7 proposes — depth is not the product.

---

## 5. Populated — one concrete case

Bismuth telluride leg, room temperature, `ZT ≈ 1`. Geometry: `A = 1 mm²`, `L = 5 mm`.
`T_h = 325 K`, `T_c = 275 K`, `ΔT = 50 K`, `η_C = 0.1538`.

| Quantity | Value | Source |
|---|---|---|
| `ZT` (Bi₂Te₃, 300 K) | ≈ 1 | **UNVERIFIED** — standard value, not fetched this session. The conclusion is insensitive to it. |
| `κ` | 1.5 W m⁻¹ K⁻¹ | **UNVERIFIED** — handbook value |
| `ρ c_p` | 1.2 × 10⁶ J m⁻³ K⁻¹ | **UNVERIFIED** — handbook (ρ ≈ 7700 kg m⁻³, c_p ≈ 154 J kg⁻¹ K⁻¹) |
| `α_th = κ/ρc_p` | **1.26 × 10⁻⁶ m² s⁻¹** | computed from the two above |
| `K = κA/L` | 3.0 × 10⁻⁴ W K⁻¹ | computed |
| `C = ρc_p A L` | 5.95 × 10⁻³ J K⁻¹ | computed |

**Static benchmark.** `q² = ZT/(1+ZT) = 0.5`, `q = 0.707`.
`max η = η_C·(√2−1)/(√2+1) = 0.1538 × 0.1716 = ` **2.64 %**.
Heat throughput `Q̇_h ≈ KΔT = 0.015 W`; electrical output ≈ **3.9 × 10⁻⁴ W**.

**Moving, no regenerator (`ε = 0`), `v = 1 mm/s`:**

```
Pe = vL/α_th = (10⁻³)(5×10⁻³)/(1.26×10⁻⁶) = 3.97
ZT_eff = 1/(1+3.97) = 0.201
q'² = 0.201/1.201 = 0.167 ,  q' = 0.409           (down from 0.707)
max η = η_C·(√1.201−1)/(√1.201+1) = 0.1538 × 0.0455 = 0.70 %
```

**Efficiency falls by a factor of 3.8 at one millimetre per second**, before any drag or contact
loss is charged.

**Tolerance.** To keep `ZT_eff` within 10 % of `ZT` requires `(1−ε)Pe ≤ 0.1`, i.e.

```
(1−ε)·v  ≤  0.1 α_th / L  =  2.5 × 10⁻⁵ m/s  =  25 µm/s                 (13)
```

With no regenerator you must crawl at 25 µm/s. With a 99 %-effective regenerator you may run at
2.5 mm/s — **and a 99 %-effective regenerator is a thermoacoustic engine.**

**The contact term, which is the killer.** From (11), one make-or-break event costs

```
T ΔS  ≈  C(ΔT)²/(2T)  =  5.95×10⁻³ × 2500 / 600  =  0.025 J
```

Against an electrical output of 3.9 × 10⁻⁴ W, that is **64 seconds of full-power output lost per
contact event.** A cycle with two contact events must therefore have a period well over ~130 s
just to break even on contact irreversibility alone — at which point `Pe ~ 10⁻⁴` and the motion
is doing nothing whatever.

> **The two constraints are not in tension; they are the same constraint.** Contact losses force
> slow cycling; slow cycling forces `Pe → 0`; `Pe → 0` returns `ZT_eff → ZT`. **The device
> converges to the stationary thermoelectric generator it was supposed to beat, from below.**

---

## 6. Verdict and what it means for building

**Which of the three offered outcomes.** Formally **(b)**: a modified bound exists, it is
`ZT_eff = ZT/(1+(1−ε)Pe)`, and deriving it is the useful part. Practically **(c)**: the modified
bound is never better than the original, the gain in the Schur complement is exactly the advected
heat counted twice, and the motion is charged again for drag and for contact.

**What the prior art already knew.**

1. Advecting the working medium along a gradient in a cycle is **thermoacoustics** — a field that
   already scores itself as a fraction of Carnot, i.e. a CLOSED literature by
   [[what-closes-a-gap]]'s own third criterion.
2. A *rotating* thermoelectric device was analysed in 2014 and already found that performance
   depends on `ZT` **plus a second dimensionless group built from period, size and thermal
   diffusivity**. That group is `Pe`. §4 rederives it from the Onsager side.
3. Periodic driving does not break the framework: **reciprocity survives for two fluxes**, and
   reversible efficiency is unreachable at finite power (Proesmans–Van den Broeck).
4. Enlarging the Onsager matrix does not remove the bound; it yields **generalized figures of
   merit** and `n`-dependent bounds, obtained by exactly the Schur-complement algebra used here
   (Brandner–Seifert; Mazza et al.).
5. Ratchets reach `q = 1` — **at zero velocity** (Gómez-Marín & Sancho). The same trade.
6. Transient Peltier really does beat steady-state `ZT`, at a stated and quantified cost, and
   buys temperature depth rather than conversion efficiency.

**Recommendation on [[buildable]] item 7: do not build it.** Its own "before building" clause
asked for exactly this calculation and named the disqualifying outcome — *"confirm the bound
actually differs rather than reappearing in another form."* It reappears in another form. The
device is a Stirling engine with a bad regenerator, and the honest version of the idea has a
two-hundred-year head start.

**What survives as worth something.** Two things, both small and both real:

- **The `Pe` form of the bound.** `ZT_eff = ZT/(1+(1−ε)Pe)` puts thermoelectrics, regenerators
  and thermoacoustics on one axis with the regenerator effectiveness `ε` and a Péclet number as
  the only two knobs. It connects directly to [[METHOD]] §9's scale-transfer triage, and it is a
  one-line statement of why the regenerator is the whole game.
- **The correction to [[C8-momentum-harvesting-metric]] §5**, which is the more important output.

---

## 7. Correction to be propagated

[[C8-momentum-harvesting-metric]] §5 item 5 states: *"On this analysis its performance would not
be bounded by `q` at all, because `q` is derived under exactly the steady-state assumption such a
device abandons"*, and *"the thing the Kedem–Caplan derivation silently held fixed is that the
coupling point does not move."*

**Both sentences are false and should be struck.**

- [[kedem-caplan]] holds nothing fixed about coupling-point motion. It fixes a *set of conjugate
  pairs*. Motion adds a pair — the one C8 §3.2 itself identified — and the theorem applies to the
  enlarged matrix.
- The steady-state assumption is not abandoned by a device moving at constant `v`: that device
  has a steady state in its own frame. Where it *is* abandoned (fast cycling), the answer is
  known and is transient Peltier.
- The collapse-to-a-coefficient property, which C8 §3.3 correctly showed fails for *momentum*
  harvesters, **does not fail here.** The coefficient is `q'`, from the Schur complement.

This is a case of [[METHOD]] §8 applied to the wrong assumption. The procedure — *take the bound,
list what its derivation held fixed* — was run, but the item written down was not on the list. The
list for `q` is: linearity, reciprocity, two pairs, steady state. **Motion of the coupling point
is not an independent entry; it is "two pairs."** And varying it enlarges the matrix rather than
escaping it.

---

## 8. Status

- **§3 (Schur complement, `q'` exists, apparent gain in (6)): derivation holds**, and is the same
  algebra Brandner–Seifert use (**VERIFIED**).
- **§4.1 (the cancellation, eq. 8): derivation holds**, and independently corroborated by the 2014
  rotating-thermoelectric result finding the same extra dimensionless group (**VERIFIED**).
- **§4.2–§4.4 (drag, contact, balance): standard, and each is a strict inequality.** Equation (11)
  is the textbook irreversible-contact entropy; not fetched, but elementary.
- **§5 numbers:** the *ratios* — `Pe`, the 3.8× fall, the 25 µm/s ceiling, the 64 s contact
  penalty — follow from `α_th` and `C`, which rest on **UNVERIFIED** handbook values for Bi₂Te₃.
  The qualitative conclusion does not depend on them: `Pe = vL/α_th` exceeds 1 at millimetre
  scales and millimetre-per-second speeds for **any** solid.
- **Not obtained:** Backhaus & Swift (1999) primary text (*Nature*, 403); Swift's thermoacoustics
  monograph. The 30 % / 41 %-of-Carnot figures are **UNVERIFIED**. They are decorative — the
  argument rests on the arXiv-verified statement that the mechanism is a Lagrangian Stirling
  cycle, not on the efficiency number.
- **What would overturn this.** A mechanism by which `ε > 1` — heat returned to the hot side in
  excess of what was carried away — which is forbidden; or a regime where the mechanical channel
  couples to charge (`L₁₃ ≠ 0`) *without* dragging heat, so the pump term is a genuine
  work-to-work converter with no advective penalty. That second case is worth one paragraph of
  thought and is **not treated here**: it would be an electro-mechanical converter in parallel
  with a thermoelectric one, and parallel converters do not beat the better of the two.

See [[C8-momentum-harvesting-metric]], [[kedem-caplan]], [[G1-gradient-coupling]] and
[[what-closes-a-gap]].
