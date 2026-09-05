---
name: C8-momentum-harvesting-metric
type: computed
---

# The momentum branch has a conjugate pair after all — but no degree of coupling

> **The surviving half of [[G1-gradient-coupling]] closes half-way, and the failure is
> located precisely.** Momentum and field-gradient harvesting *does* admit a shared
> dimensionless figure of merit:
>
> ```
> Σ  ≡  P_useful / (F · Δu)
> ```
>
> — useful power out, divided by the force the harvester transmits between two reservoirs
> times their relative velocity. `F·Δu` is the total dissipation, so `Σ ∈ [0,1]` by
> construction, and it is a genuine bilinear flux–force product in the Onsager sense.
> **The gap note's premise that "a solar sail has no conjugate flux pair" is wrong** — the
> sail's second reservoir is the radiation field, its `Δu` is `c`, and `Σ_sail = v/c`
> falls straight out. Σ evaluates to each field's own existing performance number as a
> special case: the tether's load-voltage fraction of the motional EMF, the sail's `v/c`,
> the drag device's `V/Δu`, the soarer's distance above the minimum-shear condition.
>
> **What does not generalise is [[kedem-caplan]]'s `q`.** The degree of coupling exists
> because in linear response the *maximum* of the efficiency collapses to a function of a
> single state-independent coefficient. Momentum harvesting is quadratic in relative
> velocity, so the coefficients are not constants, reciprocity does not hold, and
> `max Σ` is a **functional of the trajectory** obtained by optimal control, not a ratio of
> coefficients. **The named property that fails is the collapse of the optimum to a
> coefficient.** Σ is well defined for every system; `max Σ` is not a number you can
> tabulate from material properties.
>
> That distinction turns out to be the useful part. It cleaves the family in two — systems
> where `Σ` is a **kinematic identity** (a sail: `v/c`, unimprovable by any arrangement)
> and systems where `Σ` is a **trajectory functional** (soaring: arrangement is the entire
> lever). The project's founding intuition — arrangement beats magnitude — is not
> universally true, and this is the criterion that says where it holds.

---

## 1. Prior art

Searched this session. **No shared figure of merit exists.** What does exist is a set of
partial bridges, all of which stop short of a dimensionless efficiency, and all of which
use lift-to-drag ratio as their transfer currency.

| Source | Checked how | What it does — and does not — do |
|---|---|---|
| **Dynamic Soaring as a Means to Exceed the Solar Wind Speed**, *Front. Space Technol.* 3:1017442 (2022), also [arXiv:2211.14643](https://arxiv.org/abs/2211.14643) — [full text fetched](https://www.frontiersin.org/journals/space-technologies/articles/10.3389/frspt.2022.1017442/full) | **VERIFIED by fetch** | The strongest bridge found. Models soaring as "a sequence of elastic collisions between the vehicle and the two regions of different wind speed," carries it from seabirds to spacecraft in the solar wind, and **explicitly contrasts solar sails and magnetic sails** ("predominately drag devices, more similar to parachutes than sails"). Its figure of merit is **L/D**, which is not dimensionally comparable to a sail's β and is not an efficiency. It compares the branches; it does not put them on one axis. |
| **Wind–Pellet Shear Sailing**, Greason, [arXiv:2205.14117](https://arxiv.org/abs/2205.14117) / *Acta Astronautica* (2022) | abstract **VERIFIED by fetch**; full text not obtained | States the analogy directly — exploits pellet/ISM velocity difference "in a manner analogous to the way ocean sailing vessels exploit the velocity difference between the wind and the ocean." Identifies "the critical role of the efficiency of the power extraction and transfer process" but the abstract names no dimensionless group. **Nearest thing to prior art on the Class-A half.** |
| **Bousquet, Triantafyllou & Slotine**, *J. R. Soc. Interface* 14:20170496 (2017), [PMC5665832](https://pmc.ncbi.nlm.nih.gov/articles/PMC5665832/) | **VERIFIED by fetch** | Full nondimensionalisation of the soaring problem, but entirely internal to soaring. No sails, no tethers. |
| **Sánchez-Arriaga, Lorenzini & Bilén**, *Acta Astronautica* 225:158 (2024), "…Historical trend, **dimensionless parameters**, and opportunities" | title/abstract via search; ScienceDirect 403 | A dimensionless-parameter review **for tethers only**. No soaring, no sails. |
| Solar-sail literature: lightness number β = a_c/g_⊙, characteristic acceleration a_c | via search; [Wikipedia](https://en.wikipedia.org/wiki/Solar_sail) | β is a *force ratio against solar gravity*, not an efficiency, and is meaningless for a soarer or a tether. |
| "energy harvesting factor", "soaring number", "specific extraction rate", "Rayleigh cycle", "McCready", "energy-height rate" as cross-field terms | searched | **ABSENT** as shared objects. "Rayleigh cycle" and "McCready" are soaring-internal; "energy-height rate" is soaring-internal. |

**Classification under [[what-closes-a-gap]]: TRUE GAP, with one qualification.** The
soaring↔sailing↔shear-sailing chain is a live and recent cross-domain literature (2022
onward, and it cites seabirds explicitly), so this is not a zero-contact gap. But its
shared object is L/D, which cannot reach a photon sail. The unifying object below does not
appear in any source read.

---

## 2. What each field actually uses

### 2.1 Dynamic soaring

The governing energy equation (standard Rayleigh form; horizontal wind `W(z)`, airspeed `V`,
climb rate `ż`, ground-frame horizontal velocity component `v_x`):

```
d/dt (E/m)  =  − (dW/dz)·ż·v_x  −  D·V/m
```

Energy neutrality over a cycle is `⟨(dW/dz)·ż·v_x⟩ ≥ ⟨D·V⟩/m`. The field's headline number
is the **minimum wind shear** required, and the field's dimensionless scheme (Bousquet et
al., **VERIFIED**) is

```
v = V/Vc ,   ẑ = z/λ ,   τ = t/tc ,   w = W/Vc
λ = Vc²/g ,   tc = Vc/g
W(z) = W₀ tanh(z/δ)
```

with the thin-shear minimum-wind result quoted verbatim from the fetched text:

> "w\* = (2/π) × √(2k × C̄p,min)"

Units: `w*` dimensionless (`W₀/Vc`); `dW/dz` in s⁻¹; `λ` in m.

### 2.2 Solar sails

Two numbers, neither an efficiency.

```
a_c  =  characteristic acceleration  =  F/m at 1 AU        [m s⁻²]
β    =  a_c / g_⊙(1 AU)  =  a_c / 5.93×10⁻³                [dimensionless]
```

`β` is the ratio of radiation-pressure force to solar gravity, and is **constant with
heliocentric distance** because both go as `1/r²` — which is exactly why it is not an
efficiency: it does not reference any energy the environment supplies.

### 2.3 Electrodynamic tethers

```
V_emf  =  ∫₀^L (v_orb × B) · dL                            [V]      (VERIFIED, Wikipedia)
F      =  ∫₀^L I(L) dL × B                                 [N]      (VERIFIED, Wikipedia)
```

Performance is reported as collected current, and (Sánchez-Arriaga et al.) as a **normalised
average current** with a characteristic ohmic length `L*` and the ratio `L*/L_t`. The
community's own efficiency statement is the fraction of `V_emf` that reaches the load rather
than the tether resistance and the plasma contactor drops.

**None of these three quantities can be plotted on one axis.** `w*` is a wind speed ratio,
`β` a force ratio, `L*/L_t` a length ratio.

---

## 3. Derivation

### 3.1 The identity

Take a fuel-free harvester in contact with two reservoirs moving at `u₁` and `u₂`. It
transmits force `F₁` from reservoir 1 and `F₂` from reservoir 2. In steady cruise
`F₁ + F₂ = 0`; write `F ≡ F₁`, `Δu ≡ u₁ − u₂`.

Power delivered *by* reservoir *i* is the force times the velocity of the contact surface
**in that reservoir's own frame**, `F_i·(v − u_i)`. Summing:

```
P_total  =  F₁·(v − u₁) + F₂·(v − u₂)
         =  (F₁ + F₂)·v  −  F₁·u₁ − F₂·u₂
         =  0  −  F·u₁ + F·u₂
         =  − F·Δu                                                    (1)
```

So the environment surrenders power at rate `|F·Δu|`, and — this is the whole content —

> **The power available to a fuel-free harvester is the force it transmits between two
> reservoirs, dotted into their relative velocity. Nothing else.**

Equation (1) is exact. It assumes no linearity, no small gradients, no reciprocity. It
holds for a sailboat, an albatross, a tether, a gravity assist, a wind turbine.

Define

```
Σ  ≡  P_useful / (F · Δu)                                             (2)
```

Because `F·Δu` is the *total* power leaving the environment and `P_useful` is a part of it,
`Σ ∈ [0,1]` identically. `1 − Σ` is dumped into the media as wake, ohmic heat, or
redshifted photons.

### 3.2 Why the pairing is conjugate — correcting the gap note

`F·Δu` is the standard mechanical dissipation bilinear form; divided by `T` it is a term in
the entropy production `σ`. **Force and relative velocity are a conjugate flux–force pair in
exactly the Onsager sense**, with `Δu` the flux and `F` the force (or the transpose; the
product is what matters). [[G1-gradient-coupling]] and [[kedem-caplan]] both assert that a
solar sail "has no conjugate flux pair." That is false as stated. The sail's second
reservoir is the radiation field, and its `Δu` is `c`.

**Where the factor 2 lives — corrected 2026-09-05.** Put `Δu = c` into (2):

```
Σ_sail  =  P_useful / (F·Δu)  =  F v / (F c)  =  v / c                (2a)
```

The `F` cancels, so **`Σ_sail = v/c`, not `2v/c`** — the 2 is not in Σ. It is in the *force*.
Reflected-photon bookkeeping for a perfect mirror of area `A` at flux `Φ`: each photon
reverses momentum rather than being absorbed, so `F = 2ΦA/c`, twice the absorber's `ΦA/c`.
That 2 then appears identically in numerator (`P_useful = Fv`) and denominator (`F·c`) and
divides out. The earlier `Σ_sail = 2v/c` double-counted it: it took the doubled force in the
numerator and the *incident* flux `ΦA = Fc/2` in the denominator. Under (2) the denominator
is `F·Δu = F·c`, which for a perfect mirror is `2ΦA`, not `ΦA`.

### 3.3 Where it breaks — the crux, answered

The thermodynamic branch gets more than an efficiency: it gets `q`, a single number such
that `max η = f(q)` alone. That requires three things, and the momentum branch has one:

| Requirement | Thermodynamic branch | Momentum branch |
|---|---|---|
| A bilinear `Σ = J·X` form | ✔ | ✔ **(this note)** |
| Constitutive law linear in the force, `J = L·X` | ✔ | ✘ — aerodynamic `F ∝ ρv²`, tether current is a nonlinear OML sheath law |
| **The optimum collapses to a state-independent coefficient** | ✔ `q² = L₁₂²/(L₁₁L₂₂)` | ✘ — `max Σ` is `sup` over trajectories |

The third row is the one that matters and it is not merely a consequence of the second.
Even granting nonlinearity, one could hope for a local coefficient. One cannot get one,
because for the cyclic harvesters the vehicle must **return to its initial state**, and the
cost of returning is not a property of any local point on the trajectory. Bousquet et al.
solve exactly this as an optimal-control problem; the 2026 seabird work
([arXiv:2604.14310](https://arxiv.org/abs/2604.14310), abstract **VERIFIED by fetch**) states
the same object as a "simplified Hamilton–Jacobi–Bellman optimal-control model."

> **Statement of the negative result.** No single dimensionless number can span the
> thermodynamic and momentum branches *in the role `q` plays*, because `q` is defined as the
> coefficient to which the optimisation collapses, and for trajectory-dependent harvesters
> the optimisation does not collapse. It collapses to a functional. **`Σ` spans both
> branches; `max Σ` does not.**

This is not a fudge in either direction: `Σ` is a real shared axis on which every system has
a computable value, and the thing the thermodynamic branch has that the momentum branch
provably cannot have is named.

### 3.4 Consistency check — Σ ≤ 1 reproduces the minimum-shear condition

For a soarer the available power is the shear term of §2.1, `m (dW/dz) ż v_x`, where `ż` is
climb rate and `v_x` the ground-frame horizontal component. These are two components of the
same airspeed vector, so `ż² + v_x² ≤ V²`, and by AM–GM `ż v_x ≤ V²/2`, with equality at
`ż = v_x = V/√2`. **The ceiling therefore carries a factor ½** (corrected 2026-09-05; the
earlier `P_available = m V²(dW/dz)` implicitly set `ż = v_x = V` simultaneously, which is
kinematically impossible):

```
P_available  =  ½ m V² (dW/dz)
```

The power that must be recovered is the drag power `D·V = mgV/(L/D)`. So

```
Σ_soar  =  [mgV/(L/D)] / [½ m V²(dW/dz)]  =  2g / [ (L/D) · V · (dW/dz) ]        (3)
```

and `Σ_soar ≤ 1` is `(dW/dz) ≥ 2g / ((L/D)·V)` — **twice the shear** the previous version of
this note required.

**Does it still reproduce the field's criterion? Functional form yes, constant no — restated
as order-of-magnitude.** The scaling `dW/dz ∝ g/((L/D)V)` is the one the soaring literature
derives, and that much survives. The constant does not, and it never did: (3) is a *ceiling*
(the caveat below), so the previous exact-looking match at coefficient 1 was a coincidence of
an over-generous `P_available`, not a recovery. Numerically, with the §4 albatross inputs
(`L/D = 21.2`, `V = 15.5 m/s`):

```
(dW/dz)_min  =  2 × 9.81 / (21.2 × 15.5)  =  0.0597 s⁻¹
```

i.e. a shear of only ~0.12 m/s across the 2 m layer, versus the ~3.6 m/s minimum wind
Richardson (2015) obtains for a wandering albatross from a Rayleigh-cycle model. The bound is
loose by a factor of ~30, exactly as a ceiling should be. **Claim now stated as: Σ ≤ 1
recovers the minimum-shear condition's functional form to within an order of magnitude; it
does not reproduce the field's constant, and §5 no longer claims it does.**

**Honest caveat, stated because it is load-bearing.** (3) is a *bound*, not tight: a real
soarer cannot climb at `V` while also running downwind at `V`, and it must reverse. The
missing factor is precisely `w*`, i.e. precisely the optimal-control problem of §3.3. So
`Σ` computed this way is a **ceiling ratio**, and the gap between it and the achieved value
is exactly the trajectory functional. That is a feature — it is where the design freedom
lives — but it means Σ for cyclic harvesters is not measured the same way as Σ for steady
ones, and any table mixing them must say so. This one does.

---

## 4. Populated

| System | `F·Δu` (power processed) | `P_useful` | **Σ** | Verification |
|---|---|---|---|---|
| **Wandering albatross**, cruise in 12 m/s wind | `½ m V² (dW/dz)` = 0.5 × 9.5 × 15.5² × 2.1 ≈ **2.40 kW** | `mgV/(L/D)` = 9.5×9.81×15.5/21.2 ≈ **68.1 W** | **≈ 2.8×10⁻²** | m = 9.5 kg, wing area 0.65 m², `Vc` = 15.5 m/s, `λ` = 24.3 m, δ = 2 m, `W₀` = 25–50% of the 10 m wind — all **VERIFIED** from [PMC5665832](https://pmc.ncbi.nlm.nih.gov/articles/PMC5665832/). `dW/dz ≈ W₀/δ ≈ 4.2/2 = 2.1 s⁻¹` is **computed** from those. The ½ is the AM–GM ceiling derived in §3.4 (corrected 2026-09-05; was omitted, making `F·Δu` 2× too generous and Σ 2× too small). **L/D = 21.2 is now sourced: VERIFIED-SECONDARY** — "the cruise airspeed, Vc = 16 m/s, of a wandering albatross is its speed at the maximum glide ratio, which is around 21.2 in straight flight (Pennycuick, 2008)", Richardson (2015), *Prog. Oceanogr.* 130:146, [PDF](https://www2.whoi.edu/staff/prichardson/wp-content/uploads/sites/75/2018/11/Richardson-2015-PinO-upwind.pdf), fetched **2026-09-05**; secondary because Richardson quotes Pennycuick (2008), a book not obtained. Result scales as 1/(L/D); at the old unsourced L/D = 20, Σ = 3.0×10⁻². |
| **IKAROS**, 1 AU idealisation | `F·Δu` = `F·c` = 1.12×10⁻³ × 2.9979×10⁸ = **3.36×10⁵ W** | `F·v` = 1.12×10⁻³ × 3×10⁴ = **33.6 W** | **= 1.00×10⁻⁴** | Thrust 1.12 mN **VERIFIED** ([JAXA](https://www.jaxa.jp/press/2010/07/20100709_ikaros_e.html), quoted: "The thrust by solar light pressure is 1.12 mili-Newton"). Mass 310 kg, sail 14 m × 14 m = 196 m², 7.5 µm polyimide **VERIFIED** ([Wikipedia/IKAROS](https://en.wikipedia.org/wiki/IKAROS)). Heliocentric speed 30 km/s **UNVERIFIED** (standard value, and IKAROS actually flew inward toward Venus, so it is an approximation). Closed form `Σ = v/c` = 3×10⁴/2.9979×10⁸ = **1.0007×10⁻⁴**, which the populated row reproduces **exactly** — as it must, since `F` cancels. *Corrected 2026-09-05:* the row previously used the incident flux `Φ·A` = 1361 × 196 = 2.67×10⁵ W as the denominator, which is not `F·Δu`; it gave Σ = 1.26×10⁻⁴ against a closed form of 2×10⁻⁴ and the note called that agreement. Both halves were wrong (see §3.2). |
| **Electrodynamic tether**, LEO generator | `F·Δu` = `I·L·B·v_rel` = `I × V_emf` | `I × V_load` | **`Σ = V_load / V_emf`** — order 0.3–0.7 by design | The reduction is exact and follows from `F = ILB` and `V_emf = vBL`, both **VERIFIED** ([Wikipedia](https://en.wikipedia.org/wiki/Electrodynamic_tether)). The 0.3–0.7 range is **UNVERIFIED** — the Sanmartín reviews (oa.upm.es PDFs) and the 2024 *Acta Astronautica* review were **NOT OBTAINED** (PDFs returned undecodable binary; ScienceDirect 403s). What is established is the *identity*, not the number. |
| *Reference — drag device* (parachute, magnetic sail, dead-downwind hull) | `F·Δu` | `F·V` | `Σ = V/Δu ∈ [0,1]` | Elementary. *Corrected 2026-09-05:* the row previously read "max 1/3 at `V = Δu/3`". That is false under (2): `Σ = FV/(FΔu) = V/Δu` is **monotone increasing in V with supremum 1** and has no stationary point. `V = Δu/3` is the optimum of a *different* objective — the extracted **power** `P = FV ∝ (Δu−V)²V`, maximised at `V = Δu/3` with `Cp = 4/27`, the classical drag-machine limit that motivates Betz. A power optimum is not a bound on Σ. This row therefore does **not** recover a known bound; see §5 item 1. |

**The finding in the table.** Σ ranges over more than three orders of magnitude
(1.0×10⁻⁴ → 0.3–0.7) across three systems that previously had no common axis at all — and
the ordering is not the one the fields' own vocabulary suggests. The tether, the least
glamorous of the three, is the best converter: ~18× the albatross (0.5/2.8×10⁻²) and
~5×10³× the sail. The solar sail, which the sail literature scores by a
*force* ratio β and which IKAROS scored well on as a demonstrator (β ≈ 6×10⁻⁴, computed from
`a_c` = 1.12 mN / 310 kg = 3.6×10⁻⁶ m s⁻²), is the worst *energy* converter on the list by a
factor of ~5×10³ against the tether (0.5 / 1.0×10⁻⁴). **β and Σ rank sails and tethers in opposite orders, and
only Σ is an efficiency.**

---

## 5. What it buys

**1. It puts three fields on one axis for the first time, and each keeps its own number as a
special case.** `Σ_EDT` = load fraction of the motional EMF. `Σ_sail` = `v/c`.
`Σ_drag` = `V/Δu`. `Σ_soar ≤ 1` recovers the minimum-shear criterion's *functional form*
(§3.4), to within an order of magnitude — not its constant. A unification that reproduced
none of the local results would be suspect; this one reproduces **three**.

*Corrected 2026-09-05 (was "all four").* The fourth was the drag device's claimed
`Σ ≤ 1/3`, which §4 row 4 shows is not a bound on Σ at all but the optimum of extracted
power. `Σ_drag = V/Δu` is still recovered as an expression; it is not a recovered *bound*.
And the soaring case is a functional-form match, not the exact-constant match previously
claimed. So: two exact special cases (tether, sail), one order-of-magnitude recovery
(soaring), one expression that is not a bound (drag).

**2. It kills a false premise that was blocking the gap.** "A solar sail has no conjugate
flux pair" appears in both [[G1-gradient-coupling]] and [[kedem-caplan]]. It is wrong, and
it was the stated reason the Onsager machinery could not reach the momentum branch. The
bilinear form reaches it fine. What genuinely fails is one step further in — §3.3 — and
naming the right step is the whole difference between "cannot be done" and "can be done
except for this."

**3. It identifies a regime, and it is not the expected one.** Momentum harvesting is not
uniformly worse than thermodynamic harvesting. A thermoelectric generator runs at roughly
10–20% of Carnot; an electrodynamic tether can put most of its motional EMF across a load.
The momentum branch's problem is not efficiency — it is **that `Δu` must exist**. A sail
works where nothing else works precisely because it accepts `Σ ~ 10⁻⁴` in exchange for
needing no second reservoir. **Σ separates efficiency from feasibility, which β and L/D
conflate.**

**4. It tests the project's founding intuition and returns a criterion rather than a
slogan.** *Arrangement beats magnitude* — sometimes. Σ splits the family:

| | Σ is a **kinematic identity** | Σ is a **trajectory functional** |
|---|---|---|
| Examples | photon sail (`v/c`), gravity assist (`2u_planet` per pass) | dynamic soaring, sailing craft, cyclic tether |
| Can arrangement raise Σ? | **No.** No trajectory, no shape, no cleverness changes `v/c`. Only raising `v` does — magnitude. | **Yes, and it is the only lever.** The whole gap between the ceiling (3) and the achieved value is trajectory. |

So the founding intuition is **conditionally true, and the condition is now stated**:
arrangement beats magnitude exactly when the optimum fails to collapse to a coefficient —
which is the same property, seen from the other side, that stops `q` from generalising.
**The thing that breaks the unification is the thing that creates the design freedom.**

**5. The unexplored corner it points at.** Every mature harvester on the thermodynamic
branch is a *steady-state* device, and its `q` is a material property. The momentum branch
is dominated by *cyclic* devices whose performance is a trajectory functional. Nobody
appears to have asked what a **cyclically-driven thermodynamic harvester** looks like — a
device that traverses a thermal or chemical gradient on a closed path rather than bridging
it statically.

> **REFUTED 2026-09-03 by [[C9-moving-coupling-point]]. The two sentences that stood here are
> struck.** They claimed such a device would not be bounded by `q`, because `q` silently holds
> the coupling point fixed.
>
> **`q` does not assume a static coupling point. It assumes a set of conjugate pairs.** Moving
> the coupling point adds the mechanical pair `(F, v)` — the very pair §3.2 of this document
> established is legitimate — so the Onsager matrix goes 2×2 → 3×3 and the optimum still
> collapses to a coefficient: the degree of coupling of the **Schur complement**.
>
> The error is instructive. §3.2 proved that `(F, v)` is a conjugate pair, and §5 then reasoned
> as though it were outside the formalism. **The refutation was already inside this document.**

What survives is the useful half: `ZT_eff = ZT / (1 + (1−ε)·Pe)`, with `Pe = vL/α_th` a thermal
Péclet number and `ε` regenerator effectiveness. Motion degrades the figure of merit unless the
regenerator recovers it. **The regenerator is the whole game** — which is exactly what
thermoacoustics has always said.

---

## 6. Status

- §3.1 (the identity `P = F·Δu`) and §3.2 (conjugacy): **derivation holds.**
- §3.4 (minimum-shear): **derivation holds with the AM–GM ½ inserted 2026-09-05**, but the
  claim is now weaker. `Σ ≤ 1` gives `dW/dz ≥ 2g/((L/D)V)`, which recovers the literature
  criterion's *functional form* only; the constant is not recovered and the bound sits ~30×
  below the observed minimum wind. **Order-of-magnitude, not exact.**
- §3.3 (no generalisation of `q`): **the negative result, argued from the definition of `q`
  as the coefficient to which the optimum collapses.** It is an argument, not a theorem;
  making it a theorem means exhibiting a class of trajectory-dependent harvesters and
  proving no state function reproduces `sup Σ`. Not done here.
- §4 row 3: the *identity* `Σ_EDT = V_load/V_emf` holds; **the numerical range is
  UNVERIFIED** and both Sanmartín reviews and the 2024 *Acta Astronautica* review were
  **NOT OBTAINED**.
- §4 row 1: the albatross `L/D` is **no longer UNVERIFIED** — 21.2, VERIFIED-SECONDARY from
  Richardson (2015) quoting Pennycuick (2008), fetched 2026-09-05. Pennycuick's own book was
  not obtained, so it is not VERIFIED-PRIMARY.
- Prior art: **Greason's shear-sailing paper — RESOLVED 2026-09-03, read in full via
  ar5iv.** It **does** define a bounded extraction efficiency (Eq. 11: `η_ext`, useful power as a
  fraction of the ISM kinetic-energy loss, with `η_ext < 1`, `η_acc < 1`). So the *concept of a
  bounded shear-extraction efficiency is not ours* — it exists, in-domain, for pellet/ISM
  sailing. **But the specific object Σ = P/(F·Δu) is ABSENT**, as is the `v/Δu` form and the
  cross-branch span (Greason is shear-sailing only — no soaring, no tethers, no unifying
  identity). Verdict: **Σ is REPACKAGED, not novel.** Its nearest neighbour independently has a
  bounded extraction efficiency; the contribution is the exact `F·Δu` bilinear form and the
  span across momentum/field-gradient harvesting, not the idea of bounded extraction. The
  demotion the note flagged as possible **is confirmed** — honestly, and it is a small demotion:
  the founding-question *answer* stands as a useful unification, it just is not a new concept.

Recommended standing for [[G1-gradient-coupling]]: **narrowed again** — from "the momentum
branch has no figure of merit" to "the momentum branch has `Σ`, and the open problem is
whether `sup Σ` admits any coefficient representation."

See [[kedem-caplan]] and [[what-closes-a-gap]].

---

## Corrections 2026-09-05

Source for all four: `audits/01-math-physics.md` (items 15, 16, 17 and priority actions 4-7);
backlog rows A4-A7.

| # | What was wrong | What it is now | Why |
|---|---|---|---|
| A4 | `Σ_sail = 2v/c` | **`Σ_sail = v/c`** = 1.0007×10^-4 for IKAROS | (2) with `Δu = c` gives `Σ = Fv/(Fc) = v/c`; `F` cancels. The 2 belongs to the *force* of a perfect mirror (`F = 2ΦA/c`, reflected-photon bookkeeping), where it appears in numerator and denominator alike. Justified and then dropped, per the audit's either/or |
| A4 | IKAROS row denominator = incident flux `Φ·A` = 2.67×10^5 W, Σ = 1.3×10^-4, "closed form 2×10^-4 agrees" | denominator = `F·c` = 1.12×10^-3 × 2.9979×10^8 = **3.36×10^5 W**; `P` = 33.6 W; **Σ = 1.00×10^-4** | `Φ·A` is not `F·Δu`. For a perfect mirror `ΦA = Fc/2`, so the old row was low by 2 while the old closed form was high by 2 - a 60% mismatch presented as agreement. Row and closed form now agree **exactly**, by construction |
| A5 | `Σ_drag = V/Δu`, **max 1/3** at `V = Δu/3` | `Σ_drag = V/Δu ∈ [0,1]`, monotone, no stationary point | `V = Δu/3` maximises extracted **power** `P ∝ (Δu−V)²V` (`Cp = 4/27`), a different objective. A power optimum is not a ceiling on Σ |
| A5 | §5 item 1: "reproduces all four" known results | **three** | Deleting the 1/3 bound removes one recovered bound; the soaring case is demoted from exact to order-of-magnitude (A6). Two exact (tether, sail), one order-of-magnitude (soaring), one expression-but-not-a-bound (drag) |
| A6 | `P_available = m V²(dW/dz)` | **`½ m V²(dW/dz)`** = 2.40 kW (was 4.8 kW) | `ż` and `v_x` are components of one airspeed vector: `ż² + v_x² ≤ V²`, so `ż v_x ≤ V²/2` by AM-GM. The old form set both to `V` at once |
| A6 | eq. (3) `Σ_soar = g/((L/D)V dW/dz)` | **`2g/((L/D)V dW/dz)`**; `Σ ≤ 1` is `dW/dz ≥ 2g/((L/D)V)` | Follows from the ½ |
| A6 | "§3.4 reproduces the field's own criterion" | **functional form only, to within an order of magnitude** | `2g/(21.2 × 15.5) = 0.0597 s^-1`, i.e. ~0.12 m/s across the 2 m layer, against the ~3.6 m/s minimum wind Richardson (2015) obtains. Loose by ~30x, as a ceiling should be. The old exact-looking match at coefficient 1 was an artefact of the 2x-too-generous `P_available` |
| A7 | albatross `L/D = 20`, **UNVERIFIED** | **21.2**, VERIFIED-SECONDARY | Richardson (2015), *Prog. Oceanogr.* 130:146, [PDF](https://www2.whoi.edu/staff/prichardson/wp-content/uploads/sites/75/2018/11/Richardson-2015-PinO-upwind.pdf), fetched 2026-09-05, quoting Pennycuick (2008) |
| A6+A7 net | `Σ_albatross ≈ 1.5×10^-2` | **`≈ 2.8×10^-2`** | `68.14 / 2396.5`. The ½ raises it 2x; the L/D change lowers it by 20/21.2. At the old L/D = 20 it would be 3.0×10^-2, the audit's predicted value |

**Not done.** Sachs (2005), *Ibis* 147:1-10, the paper the backlog named first for the L/D, is
paywalled (Wiley returned HTTP 403, 2026-09-05) and Pennycuick (2008) is a book that was not
obtained - hence VERIFIED-SECONDARY rather than PRIMARY. The soaring minimum-shear comparison
uses Richardson's Rayleigh-cycle minimum wind (3.6 m/s) rather than Sachs's own criterion, so
the "~30x loose" figure is indicative, not a matched-object comparison. The tether range
0.3-0.7 remains UNVERIFIED (§6, unchanged by this pass).
