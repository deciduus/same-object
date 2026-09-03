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
> sail's second reservoir is the radiation field, its `Δu` is `c`, and `Σ_sail = 2v/c`
> falls straight out. Σ evaluates to each field's own existing performance number as a
> special case: the tether's load-voltage fraction of the motional EMF, the sail's `2v/c`,
> the drag turbine's `V/Δu ≤ 1/3`, the soarer's distance above the minimum-shear condition.
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
> where `Σ` is a **kinematic identity** (a sail: `2v/c`, unimprovable by any arrangement)
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

For a soarer, take the most favourable instantaneous configuration (all of `V` devoted to
both climb and downwind travel). Then `P_available = m V² (dW/dz)` and the power that must
be recovered is the drag power `D·V = mgV/(L/D)`. So

```
Σ_soar  =  g / [ (L/D) · V · (dW/dz) ]                                 (3)
```

and `Σ_soar ≤ 1` is `(dW/dz) ≥ g / ((L/D)·V)` — **the minimum-shear condition the soaring
literature derives independently.** The metric's own bound reproduces the field's own
criterion. That is the strongest evidence the construction is the right one.

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
| **Wandering albatross**, cruise in 12 m/s wind | `m V² (dW/dz)` = 9.5 × 15.5² × 2.1 ≈ 4.8 kW | `mgV/(L/D)` = 9.5×9.81×15.5/20 ≈ 72 W | **≈ 1.5×10⁻²** | m = 9.5 kg, wing area 0.65 m², `Vc` = 15.5 m/s, `λ` = 24.3 m, δ = 2 m, `W₀` = 25–50% of the 10 m wind — all **VERIFIED** from [PMC5665832](https://pmc.ncbi.nlm.nih.gov/articles/PMC5665832/). `dW/dz ≈ W₀/δ ≈ 4.2/2 = 2.1 s⁻¹` is **computed** from those. **L/D = 20 is UNVERIFIED** (not obtained this session; the result scales as 1/(L/D)). |
| **IKAROS**, 1 AU idealisation | intercepted flux `≈ Φ·A` = 1361 × 196 ≈ 2.67×10⁵ W | `F·v` = 1.12×10⁻³ × 3×10⁴ ≈ 34 W | **≈ 1.3×10⁻⁴** | Thrust 1.12 mN **VERIFIED** ([JAXA](https://www.jaxa.jp/press/2010/07/20100709_ikaros_e.html), quoted: "The thrust by solar light pressure is 1.12 mili-Newton"). Mass 310 kg, sail 14 m × 14 m = 196 m², 7.5 µm polyimide **VERIFIED** ([Wikipedia/IKAROS](https://en.wikipedia.org/wiki/IKAROS)). Solar constant 1361 W m⁻² and heliocentric speed 30 km/s **UNVERIFIED** (standard values, and IKAROS actually flew inward toward Venus, so both are approximations). Closed form `Σ = 2v/c` = 2×10⁻⁴ agrees. |
| **Electrodynamic tether**, LEO generator | `F·Δu` = `I·L·B·v_rel` = `I × V_emf` | `I × V_load` | **`Σ = V_load / V_emf`** — order 0.3–0.7 by design | The reduction is exact and follows from `F = ILB` and `V_emf = vBL`, both **VERIFIED** ([Wikipedia](https://en.wikipedia.org/wiki/Electrodynamic_tether)). The 0.3–0.7 range is **UNVERIFIED** — the Sanmartín reviews (oa.upm.es PDFs) and the 2024 *Acta Astronautica* review were **NOT OBTAINED** (PDFs returned undecodable binary; ScienceDirect 403s). What is established is the *identity*, not the number. |
| *Reference — drag device* (parachute, magnetic sail, dead-downwind hull) | `F·Δu` | `F·V` | `Σ = V/Δu`, **max 1/3** at `V = Δu/3` | Elementary; the classical drag-machine limit that motivates Betz. Included to show Σ recovers known bounds. |

**The finding in the table.** Σ ranges over more than two orders of magnitude across three
systems that previously had no common axis at all — and the ordering is not the one the
fields' own vocabulary suggests. The tether, the least glamorous of the three, is the best
converter by two orders of magnitude. The solar sail, which the sail literature scores by a
*force* ratio β and which IKAROS scored well on as a demonstrator (β ≈ 6×10⁻⁴, computed from
`a_c` = 1.12 mN / 310 kg = 3.6×10⁻⁶ m s⁻²), is the worst *energy* converter on the list by a
factor of ~10⁴ against the tether. **β and Σ rank sails and tethers in opposite orders, and
only Σ is an efficiency.**

---

## 5. What it buys

**1. It puts three fields on one axis for the first time, and each keeps its own number as a
special case.** `Σ_EDT` = load fraction of the motional EMF. `Σ_sail` = `2v/c`.
`Σ_drag` = `V/Δu`. `Σ_soar ≤ 1` *is* the minimum-shear criterion. A unification that
reproduced none of the local results would be suspect; this one reproduces all four.

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
| Examples | photon sail (`2v/c`), gravity assist (`2u_planet` per pass) | dynamic soaring, sailing craft, cyclic tether |
| Can arrangement raise Σ? | **No.** No trajectory, no shape, no cleverness changes `2v/c`. Only raising `v` does — magnitude. | **Yes, and it is the only lever.** The whole gap between the ceiling (3) and the achieved value is trajectory. |

So the founding intuition is **conditionally true, and the condition is now stated**:
arrangement beats magnitude exactly when the optimum fails to collapse to a coefficient —
which is the same property, seen from the other side, that stops `q` from generalising.
**The thing that breaks the unification is the thing that creates the design freedom.**

**5. The unexplored corner it points at.** Every mature harvester on the thermodynamic
branch is a *steady-state* device, and its `q` is a material property. The momentum branch
is dominated by *cyclic* devices whose performance is a trajectory functional. Nobody
appears to have asked what a **cyclically-driven thermodynamic harvester** looks like — a
device that traverses a thermal or chemical gradient on a closed path rather than bridging
it statically. On this analysis its performance would not be bounded by `q` at all, because
`q` is derived under exactly the steady-state assumption such a device abandons. That is a
[[what-closes-a-gap]]-shaped follow-on and METHOD §8 in its purest form: **the thing the
Kedem–Caplan derivation silently held fixed is that the coupling point does not move.**

---

## 6. Status

- §3.1 (the identity `P = F·Δu`), §3.2 (conjugacy), §3.4 (recovery of the minimum-shear
  condition): **derivation holds.**
- §3.3 (no generalisation of `q`): **the negative result, argued from the definition of `q`
  as the coefficient to which the optimum collapses.** It is an argument, not a theorem;
  making it a theorem means exhibiting a class of trajectory-dependent harvesters and
  proving no state function reproduces `sup Σ`. Not done here.
- §4 row 3: the *identity* `Σ_EDT = V_load/V_emf` holds; **the numerical range is
  UNVERIFIED** and both Sanmartín reviews and the 2024 *Acta Astronautica* review were
  **NOT OBTAINED**. The albatross `L/D = 20` is likewise **UNVERIFIED**.
- Prior art: **Greason's shear-sailing paper was read in abstract only.** If its full text
  contains a normalised extraction efficiency, that is the single result most likely to
  demote this note from construction to rediscovery. It should be obtained.

Recommended standing for [[G1-gradient-coupling]]: **narrowed again** — from "the momentum
branch has no figure of merit" to "the momentum branch has `Σ`, and the open problem is
whether `sup Σ` admits any coefficient representation."

See [[kedem-caplan]] and [[what-closes-a-gap]].
