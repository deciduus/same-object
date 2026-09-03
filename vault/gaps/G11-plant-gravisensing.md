---
id: G11
name: G11-plant-gravisensing
type: gap
standing: narrowed
evidence: full-text-read
contact-surface: 12
crosses: metaphor
crosses-rank: 2
topology: direct
mediator: 
borrows-from: []
lends-to: []
mutual-with: []
computed-in: []
uses-move: ["[[M1-manufacture-contrast]]", "[[M2-use-the-noise]]"]
rests-on: []
tags: [node/gap, crosses/metaphor, evidence/full-text-read, standing/narrowed]
last-checked: 2026-09-03
note: "Restored and restated. The withdrawal cited an experimental paper as if it were a derivation. But the original gap's premise was also wrong: the sensor measures inclination, not force, and its noise floor is active agitation at ~10x thermal."
---

# Limits to plant gravity sensing

**STANDING: NARROWED** · evidence: full-text-read · contact surface: 12 · last checked 2026-09-03

> The statocyte is an **inclination sensor**, not a force sensor. Gravity beats thermal noise
> by **~200x**. The real noise floor is **active agitation at an effective temperature ~10x
> ambient** — and nobody has derived a detection limit against *that*.

## The withdrawal was wrong, and so was the original claim

Both halves failed, for opposite reasons. This is the specimen case for reading rather than
counting — see [[relationship-description]].

**The withdrawal's basis does not say what the withdrawal said it said.** It rested on
Miyamoto et al., *Noise amplification of plant gravisensing* (*Advances in Space Research*,
2007), treated as a limits-to-sensing analysis. It is not. It is an **experiment**: flax roots
under external oscillation, curvature most enhanced at **5 Hz, 0.5 mm amplitude**. A vibration
study, not a derivation.

**The original claim's number was wrong too.** The note said a single statolith displacement
costs **2–3 k_BT**. Recomputed from Bérut et al. below, a displacement of one statolith
diameter costs **~200 k_BT**. Two orders of magnitude out. The 2–3 k_BT figure is not the cost
of a displacement — it is roughly the cost of a **~66 nm** displacement, which is a derived
*threshold*, not a *cost*. The two were conflated. Logged in [[log]].

## What the physics actually says

Bérut, Chauvet, Legué, Moulia, Pouliquen & Forterre (2018),
*Gravisensors in plant cells behave like an active granular liquid*, **PNAS** 115(20):5123–5128.
Read in full via PMC5960325.

> "the gravity sensor of plants thus functions as an inclination sensor rather than a force or
> acceleration sensor"

> "the position of the statoliths in statocytes, not their weight, is the relevant gravitropic
> stimulus"

The paper works in the inverse Péclet number, `Pe⁻¹ = k_BT / (mgd)`, reporting
**3×10⁻³ to 8×10⁻³** for `d = 4.5 ± 0.5 μm`, `Δρ ≈ 400 kg/m³`.

**Recomputed here as a check** — VERIFIED, arithmetic only:

| Quantity | Value |
|---|---|
| Statolith volume, (π/6)d³ | 4.77×10⁻¹⁷ m³ |
| Buoyant mass, Δρ·V | 1.91×10⁻¹⁴ kg |
| mgd | 8.4×10⁻¹⁹ J |
| k_BT at 298 K | 4.11×10⁻²¹ J |
| **mgd / k_BT** | **≈ 205** |
| **Pe⁻¹** | **4.9×10⁻³** — inside their stated 3–8×10⁻³ |

So thermal noise is **not** the binding constraint. Gravity wins by more than two orders of
magnitude. And yet:

> "Everything thus happens as if statoliths were agitated by an apparent temperature 10 times
> larger than the actual temperature."

That agitation is **active**, not thermal. It is also what makes the sensor work: the pile
behaves as a liquid and flows to level, so the population splits with the **sine of the
inclination angle**. Without the agitation the pile would jam like a granular solid and sense
nothing below its critical angle, `θ_c ≈ 10°`. See [[M2-use-the-noise]] — the noise is not
overcome, it is the mechanism.

## What is still absent

Checked in all three papers. **No derivation of a detection limit exists.**

- Bérut 2018: no first-principles bound on the minimum detectable angle. No Langevin or
  Fokker–Planck. No Berg–Purcell, no Bialek, no information-theoretic treatment. ABSENT.
- Meroz & Bastien 2014, *Stochastic processes in gravitropism*, **Frontiers in Plant Science**:
  states that thermal energy is "a lower bound on sensitivity" — **qualitatively, with no
  numbers**. Stochastic resonance invoked, no model, no parameter values. ABSENT.
- Miyamoto 2007: experimental. ABSENT.

## The surviving gap, stated precisely

The original framing — *is the statolith signal above k_BT?* — is answered, and the answer is
yes by ~200×. Withdraw that question.

**What replaces it is sharper.** The plant statocyte is an **angle** sensor reading the
position of an actively-agitated granular pile at `T_eff ≈ 10 T`. Nobody has asked what the
minimum detectable inclination is for such a device, given the pile size, the agitation
amplitude, and the integration time. That is a Berg–Purcell-shaped question against an
**active** rather than a thermal bath, and cell-sensing physics has the machinery for it.

Neither literature has run the calculation. Physics of active matter has the effective-temperature
formalism; plant biology has the measured `T_eff ≈ 10 T`, `θ_c ≈ 10°`, and `Pe⁻¹ ≈ 5×10⁻³`.
The numbers and the method are in two different rooms.

## What would close it

Derive `δθ_min` for a pile of N statoliths at `T_eff`, integrating for time τ. Then test it:
the response threshold below `θ_c` is already measured, so the prediction is falsifiable
immediately with published data.

## Why this entry matters to the method

It is the third of three over-withdrawals, and the only one re-examined by actually reading the
sources. Both directions of error showed up in one entry: a withdrawal that misdescribed its own
evidence, and an original claim off by 100×. Neither was catchable by counting.
