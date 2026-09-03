---
name: reservoir-audit
type: method
---

# The reservoir audit

> **Σ inverted is a specification instrument, not a verdict instrument.** Run on five systems
> whose partner reservoir is already known, it returns the right partner five times — and
> corrects the project's own naming of the tether's reservoir on the way. Run on the Pioneer
> anomaly *using only pre-2002 numbers*, it rules out solar radiation pressure by a factor of
> 6.7 and returns the surviving specification **"onboard thermal photon field, required
> anisotropy ≈ 3.2%"** — which is within 9% of what [Turyshev et al.
> (2012)](https://arxiv.org/abs/1204.2507) later measured.
>
> **But the audit as stated in [[Q9-fuel-free-is-an-assumption]] is too weak, and Part A is
> what exposed it.** `Σ ≤ 1` is automatic whenever the vehicle moves slower than the reservoirs'
> relative velocity, so `Σ > 1` almost never fires. The test that actually does the work is a
> second leg the derivation implies but Q9 did not name: the **availability ratio**
>
> ```
> A  ≡  (F_required · Δu) / P_available
> ```
>
> — the power the candidate reservoir would have to surrender, over the power it can actually
> surrender through the device's coupling cross-section. **`A > 1` rules a candidate out.
> `Σ > 1` is the special case of `A > 1` you notice by accident.** Every ruling-out in Part B
> below is an `A` result, not a `Σ` result.

---

## 0. The two legs

From the exact identity of [[C8-momentum-harvesting-metric]] §3.1, `P_total = −F·Δu`.

| Leg | Quantity | Fires when | What it catches |
|---|---|---|---|
| **Energy** | `Σ = P_useful / (F·Δu)` | `Σ > 1` | the device's *output* exceeds what the pairing can deliver |
| **Availability** | `A = (F_req·Δu) / P_avail` | `A > 1` | the *coupling* exceeds what the reservoir can supply through the device's aperture |

`Σ = P_useful/(F·Δu)` with `P_useful = F·v` reduces to `v/Δu`, so for any device slower than
its reservoirs' relative velocity `Σ ≤ 1` holds trivially. **This is why the Part A validation
was necessary and why it changed the procedure.** For a photon reservoir `Δu = c` and `Σ ≈ v/c`
is always minuscule — the sail passes the energy leg with fourteen orders of margin while
saying nothing. The availability leg is where a photon reservoir is actually tested, because
`P_avail` for photons is bounded by `F ≤ P_avail/c` (absorption) or `2P_avail/c` (reflection).

---

## Part A — validation on known systems

Every parameter below is marked. `VERIFIED` means fetched this session with the URL that
produced it, per METHOD §4.

| System | Reservoir 1 | Reservoir 2 | `F` | `Δu` | **Σ** | In [0,1]? |
|---|---|---|---|---|---|---|
| Wandering albatross | air above shear layer | air below / sea surface | aerodynamic force transmitted across the layer | `ΔW` across shear ≈ **8 m/s** over ≈ **10 m** | **3.6×10⁻²** | ✔ |
| Solar sail (IKAROS) | radiation field | vehicle rest frame | `Φ A / c` = 8.89×10⁻⁴ N | **`c`** | **1.26×10⁻⁴** | ✔ |
| Electrodynamic tether (TSS‑1R) | orbital kinetic energy | corotating geomagnetic field | `I L B`, `I` > 1 A | `v_orb − v_corot` ≈ 7.1 km/s | **`V_load/V_emf`** ≤ 1 identically | ✔ |
| DDWFTTW craft (Blackbird) | air, `u₁ = W` | ground, `u₂ = 0` | force transmitted rotor↔wheels | **`W` = 4.47 m/s** | ≤ 1, **`v/W` unbounded** | ✔ |
| Wave-devouring ship (Suntory Mermaid II) | wave orbital-velocity field | hull / deep water | foil thrust | `πH/T` ≈ **1.18 m/s** | **≈ 0.66** (ceiling) | ✔ |

**Five for five. No system in Part A returns Σ outside [0,1], and each returns the partner the
field already knows about.** Details and sourcing follow.

### A.1 Albatross → the shear layer ✔

`Σ_soar = g / [ (L/D) · V · (dW/dz) ]` — C8 eq. (3), a ceiling not a tight value.

- `L/D = 21.2` — **VERIFIED**, quoted "maximum glide ratio of 21.2" from
  [PMC5840797](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5840797/fullTextXML)
  (Richardson et al., flight speed of the wandering albatross).
  **This closes an item C8 §4 carried as UNVERIFIED** (`L/D = 20`); the albatross Σ moves from
  1.5×10⁻² to 1.38×10⁻² on C8's own shear numbers. The finding is unaffected.
- `V = 16 m/s` — **VERIFIED**, same source: "16 m/s cruise airspeed coinciding with the
  maximum glide ratio".
- Shear layer ≈ 10 m, minimum sustaining wind 3–4 m/s, maximum performance above 8 m/s —
  all **VERIFIED**, same source.
- `dW/dz ≈ 8/10 = 0.8 s⁻¹` — **COMPUTED** from the two verified values above.

```
Σ = 9.81 / (21.2 × 16 × 0.8) = 0.036
```

**Inverse check.** `Σ ≤ 1` requires `dW/dz ≥ g/((L/D)·V) = 0.0289 s⁻¹`, i.e. `ΔW ≥ 0.29 m/s`
across a 10 m layer. The observed minimum wind for sustained dynamic soaring is 3–4 m/s
(**VERIFIED**) — an order of magnitude above the bound, which is the expected direction: the
bound is a ceiling and the trajectory cost (C8 §3.4's honest caveat) eats the rest. **The audit
returns the shear layer and the minimum-shear condition without being told about either.**

### A.2 Solar sail → the radiation field at `Δu = c` ✔

This is the case the project got wrong; see [[Q9-fuel-free-is-an-assumption]].

- Thrust 1.12 mN, sail 14 m × 14 m = 196 m², mass 310 kg — **VERIFIED in
  [[C8-momentum-harvesting-metric]] §4** against
  [JAXA](https://www.jaxa.jp/press/2010/07/20100709_ikaros_e.html) and
  [Wikipedia/IKAROS](https://en.wikipedia.org/wiki/IKAROS). Not re-fetched this session.
- Solar constant 1361 W m⁻², heliocentric speed 30 km/s — **UNVERIFIED** (standard values;
  carried forward from C8 with its caveat that IKAROS flew inward toward Venus).

```
F·Δu = Φ A     = 1361 × 196            = 2.67×10⁵ W
F     = Φ A / c                        = 8.89×10⁻⁴ N   (momentum flux intercepted)
P_useful = F_thrust · v = 1.12e−3 × 3e4 = 33.6 W
Σ = 33.6 / 2.67×10⁵                     = 1.26×10⁻⁴
```

**Availability leg — the leg that matters here.** Perfect reflection caps the coupling at
`2ΦA/c = 1.78×10⁻³ N`. Observed thrust 1.12×10⁻³ N sits at **0.63 of the cap**, i.e. between
pure absorption (1.0×) and pure reflection (2.0×), at an effective 1.26×. `A = 0.63 ≤ 1`.
**The radiation field is not ruled out, and the reflectivity falls out of the audit as a
by-product.** Had the reported thrust been 3 mN, the audit would have ruled the radiation field
out and demanded a second partner.

### A.3 Electrodynamic tether → **the orbit, not (in LEO) planetary rotation** ✔ *with a correction*

- TSS‑1R: EMF and current "reached values in excess of 3500 volts and 1 amp"; maximum EMF
  3.8 kV; deployed 19.7 km; STS‑75, 24 Feb 1996 — **SECONDARY** (search-result summary of
  [NTRS 20160007056](https://ntrs.nasa.gov/api/citations/20160007056/downloads/20160007056.pdf);
  the PDF itself would not decode this session, so these are marked *not fetched*).
- `V_emf = ∫(v × B)·dL`, `F = ∫I dL × B` — **VERIFIED in C8 §2.3** against
  [Wikipedia](https://en.wikipedia.org/wiki/Electrodynamic_tether).

```
F·Δu = (I L B)(v_rel) = I · V_emf ≈ 1 A × 3500 V ≈ 3.5 kW
Σ    = I·V_load / I·V_emf = V_load / V_emf     ≤ 1 identically
```

**The audit corrects the project a second time.** [[Q9-fuel-free-is-an-assumption]] names the
tether's partner as "planetary rotation via the magnetic field." For a **LEO** tether that is
wrong in the same way the solar-sail claim was wrong — imprecise rather than absent. The
conjugate velocity is `Δu = v_orb − v_corot ≈ 7.7 − 0.46 ≈ 7.1 km/s` (**UNVERIFIED**, standard
LEO values), and the energy ledger splits: the drag `F` removes `F·v_orb` from the *orbit*
while the corotating field delivers `F·v_corot` to the *planet*. In LEO the orbit is the net
source and the planet's rotation is a **sink**. The sign reverses only above synchronous orbit.
**"Planetary rotation" is the right partner for a tether beyond geosynchronous and the wrong
one for every tether flown.** The audit caught this by being made to name `Δu` explicitly,
which is the entire mechanism by which it caught the sail.

`Σ = V_load/V_emf` in [0,1] survives either way; the numerical load fraction remains
**UNVERIFIED** exactly as C8 §6 states.

### A.4 Craft faster than the wind → two reservoirs, `Δu` between them ✔

- Blackbird: "dead downwind speed of about 2.8 times the speed of the wind", 27.7 mph in
  10 mph winds, 2 July 2010, certified by NALSA; upwind "about 2.1 times the speed of the
  wind", 16 June 2012 — **VERIFIED**,
  [Wikipedia/Blackbird](https://en.wikipedia.org/wiki/Blackbird_(wind-powered_vehicle)).

`v = 12.38 m/s`, `W = 4.47 m/s`, `v/W = 2.77`.

**This is the system that proves the energy leg is not the detector.** Take the naive
single-reservoir model — "the wind" alone, ground inert. Then `Δu = W − v = −7.91 m/s`: the
audit returns a **negative Δu**, not `Σ > 1`. The device appears to be pumping energy *into*
the environment. That sign inversion is the misidentification signature, and it is a *third*
diagnostic distinct from both `Σ > 1` and `A > 1`.

Name both reservoirs and it closes in one line. The vehicle draws `F·v` from the ground and
returns `F·(v − W)` to the air; net extraction `F·W = F·Δu`, exactly the identity, with

```
Σ = P_useful / (F·W)  ≤ 1        and v/W is unbounded by Σ.
```

**Σ places no ceiling whatsoever on `v/W`.** What limits Blackbird to 2.8 is the product of
turbine and propeller efficiencies — a `1 − Σ` loss term — not the identity. The audit returns
the right partner *and* the right reason the folk objection ("you can't outrun your own wind")
is void.

### A.5 Wave-powered ship → the wave orbital-velocity field ✔ *weakly sourced*

- Suntory Mermaid II: "3-tonne", "9.5-metre" catamaran, "two fin tails which absorb wave
  energy and generate thrust", "average speed of 1.5 knots", 110-day Hawaii→Japan crossing
  2008 — **VERIFIED**,
  [Wikipedia](https://en.wikipedia.org/wiki/Suntory_Mermaid_II).
- "Fuel savings of about 15–20% were obtained in a wave height of 3 m by using the foils at
  speeds of 4–8 knots" (Terao, wave-devouring propulsion) — **SECONDARY**, search-result
  summary of the ScienceDirect WDPS review; ScienceDirect 403s and the paper was **NOT
  OBTAINED**.

Reservoirs: the surface layer carrying wave orbital velocity, and the hull / deep water.
`Δu = πH/T`. Taking `H = 3 m` (from the secondary above) and `T = 8 s` (**UNVERIFIED**):

```
Δu = π × 3 / 8 = 1.18 m/s ,  v = 1.5 kn = 0.77 m/s
Σ_ceiling = v/Δu = 0.66
```

In [0,1] ✔, and **the highest Σ in the table by a factor of 18** — which is worth noticing and
is also the row I would trust least. `T` is unverified and the ceiling assumes drag-type
coupling where a hydrofoil is a lifting device. Treat 0.66 as an order-of-magnitude ceiling,
not a measurement.

### Part A verdict

**The procedure reproduces all five known answers, and produces two corrections to this
project's own bookkeeping in the process** (the albatross `L/D`, and the tether's reservoir).
Nothing in Part A failed. The procedure may be pointed at unresolved cases — with the
`A`-leg amendment, without which it would have passed everything in Part B too.

---

## Part B — negative controls on resolved anomalies

### B.1 Pioneer anomaly — the decisive test

An unexplained acceleration whose reservoir was real, ordinary, and initially unnamed.
**The audit is run below on pre-resolution inputs only.**

| Input | Value | Status |
|---|---|---|
| `a_P` | `(8.74 ± 1.33) × 10⁻¹⁰ m/s²` | **VERIFIED**, quoted from [ar5iv/1204.2507](https://ar5iv.labs.arxiv.org/html/1204.2507) |
| Pioneer 10 launch mass | `258 kg` | **VERIFIED**, [Wikipedia/Pioneer 10](https://en.wikipedia.org/wiki/Pioneer_10) |
| RTG electrical power at launch | `about 155 W` | **VERIFIED**, same |
| High-gain antenna | `2.74 m` parabolic dish | **VERIFIED**, same |
| RTG **thermal** power at launch | `Q_rtg(t₀) = 2578.179 W`, half-life `τ = 87.74 yr` | **VERIFIED**, ar5iv/1204.2507 |
| Heliocentric speed | ~12 km/s | **UNVERIFIED** |

Required coupling: `F_req = 258 × 8.74×10⁻¹⁰ = **2.26×10⁻⁷ N**`.

**Candidate 1 — solar radiation pressure.** `Δu = c`.
At 40 AU, `Φ = 1361/40² = 0.851 W m⁻²`; dish area `π(1.37)² = 5.90 m²`; `P_avail = 5.02 W`.
Maximum coupling under perfect reflection `2P/c = 3.35×10⁻⁸ N`.

```
A = 2.26×10⁻⁷ / 3.35×10⁻⁸ = 6.7  >  1     →  RULED OUT
```

Equivalently `F_req·c = 67.5 W` against 5.02 W available. **Note that the energy leg does not
fire**: `Σ = P_useful/(F·Δu) = v/c ≈ 4×10⁻⁵`, comfortably inside [0,1]. Solar radiation
pressure is eliminated by availability alone — and independently by its `r⁻²` signature, which
the audit does not use.

**Candidate 2 — the onboard thermal photon field.** `Δu = c`.
At ~25 yr post-launch, `Q = 2578.179 × 2^(−25/87.74) = 2116 W`. Fully collimated ceiling
`Q/c = 7.05×10⁻⁶ N`.

```
A = 2.26×10⁻⁷ / 7.05×10⁻⁶ = 0.032  ≤ 1    →  SURVIVES
Required anisotropy  η_req = 3.2%
Σ = F_req·v / Q = 2.26e−7 × 1.2e4 / 2116 = 1.3×10⁻⁶     ✔ in [0,1]
```

**That 3.2% is the audit's entire output — a specification, not a verdict.** Compare it with
what was later measured: Turyshev et al. fit `η_rtg = 0.0104` and `η_elec = 0.406`
(**VERIFIED**, ar5iv/1204.2507). With `Q_rtg ≈ 2116 W` and `P_elec ≈ 100 W`:

```
F_thermal = (0.0104 × 2116 + 0.406 × 100)/c = (22.0 + 40.6)/c = 2.09×10⁻⁷ N
F_thermal / F_req = 0.93
```

**Agreement to 7%.** And the paper's own parameterised recoil model gives
`a₀ = (7.4 ± 2.5) × 10⁻¹⁰ m/s²` against `a_P = (8.74 ± 1.33) × 10⁻¹⁰` — the ~80% the authors
quote, both **VERIFIED**. Their conclusion, verbatim from the abstract: *"no anomalous
acceleration remains."*

> **The audit run in 1998 would have said: of the reservoirs considered, only the onboard
> thermal photon field can supply the coupling, and it needs a 3% front-back asymmetry.**
> It would not have said the anomaly was thermal — it would have said what a thermal
> explanation would have to look like, in a number a finite-element model can be built to
> check. Fourteen years later someone built it and got 3.0%.

This is the register discipline of METHOD §3 working exactly as advertised: **testimony sets
the specification, never the mechanism.**

### B.2 EmDrive / RF resonant cavity thruster

| Input | Value | Status |
|---|---|---|
| Eagleworks 2014 | "a net mean thrust over five runs was measured at 91.2 μN at 17 W of input power" | **VERIFIED**, [Wikipedia/RF resonant cavity thruster](https://en.wikipedia.org/wiki/RF_resonant_cavity_thruster) |
| Eagleworks 2016 vacuum | "a thrust-to-power ratio of 1.2±0.1mN/kW" at "40-80W" | **VERIFIED**, same |
| Dresden 2021 | "Our measurements refute all EmDrive claims by at least 3 orders of magnitude" | **VERIFIED**, same, and [phys.org](https://phys.org/news/2021-04-comprehensive-emdrive.html) |
| Stated cause | "When power flows into the EmDrive, the engine warms up. This also causes the fastening elements on the scale to warp, causing the scale to move to a new zero point." | **VERIFIED**, phys.org |

**Candidate — the electromagnetic field, `Δu = c`.** Photon-rocket ceiling `P/c`:

```
1 kW → 3.34×10⁻⁶ N = 0.0033 mN/kW
A(1.2 mN/kW)     = 360        →  RULED OUT
A(91.2 µN, 17 W) = 1608       →  RULED OUT
```

**Candidate — expelled matter (outgassing, ablation, heated residual gas).** Not ruled out by
the audit, and this is the row that carries the deliverable. The residual specification:

```
ṁ · u_e = 1.2×10⁻³ N
  at u_e = c        →  ṁ = 4×10⁻¹² kg/s
  at u_e = 500 m/s  →  ṁ = 2.4×10⁻⁶ kg/s  =  2.4 mg/s continuous
```

> **The audit's output for the EmDrive is a number a vacuum gauge can bound: 2.4 mg/s of
> expelled mass at thermal velocity, continuously, for the duration of the run.** Not
> "impossible" — *that*. It is a measurement, and the measurement is cheap.

The actual resolution is outside the audit's reach entirely, and that is a finding about the
procedure rather than the device: **the thing exchanging momentum was the balance mount, not
the thruster.** No reservoir enumeration can catch an apparatus artefact, because the
apparatus is not in the momentum ledger being audited. Recorded as failure mode F5 below.

### B.3 Mach-effect / Woodward thruster

| Input | Value | Status |
|---|---|---|
| Tajmar conclusion | "the Mach-Effect-Thruster (an idea by J. Woodward) is unfortunately a vibration artifact and also not a real thrust" | **SECONDARY** — search-result summary; the *Acta Astronautica* paper (S0094576521001119) 403s and was **NOT OBTAINED** |
| Named artefacts | thermal and vibrational artefacts; Lorentz forces from the Earth's magnetic field via insufficiently shielded cables | **SECONDARY**, same |
| Claim scale | ~µN at ~100 W | **UNVERIFIED** |

**Candidate — radiation, `Δu = c`.** `A = 1.2×10⁻⁶ / (100/c) = 1.2×10⁻⁶/3.34×10⁻⁷ = 3.6 > 1`
→ **RULED OUT**, though only by a factor of 4, so the exclusion is weak and rests on an
unverified claim magnitude.

**Candidate — distant matter (the theory's own stated reservoir).** The audit returns Q9's
third row: **no `Δu` can be constructed.** Mach's principle names a partner but assigns it no
relative velocity, so `F·Δu` is not formable and no `Σ` exists. That is a statement about the
model, not the device.

**Candidate — the Earth's magnetic field.** Real, nameable, and instructive: in the lab frame
the field is at rest with respect to the apparatus, so `Δu = 0` and `F·Δu = 0`. **A Lorentz
reaction against the planet transmits force and extracts no energy.** The audit classifies it
correctly and immediately as a reaction force rather than a harvester — which is exactly the
distinction the claim depends on.

### B.4 Flyby anomaly — **UNRESOLVED-IN-SOURCES**

| Input | Value | Status |
|---|---|---|
| Magnitude | "a small, unexpected increase of the geocentric range-rate of approximately 1-10 mm/s" for Galileo, NEAR, Rosetta | **SECONDARY** — search summary of [arXiv:1505.06884](https://arxiv.org/pdf/1505.06884) |
| Thermal candidate | Rievers et al. found thermal radiation pressure on Rosetta "insufficiently small to account for the anomaly as well as wrong in sign" | **SECONDARY**, same |
| Non-recurrence | no anomaly in the Juno Earth flyby of 9 Oct 2013, nor in Rosetta flybys 2 and 3 | **SECONDARY**, same |

**No resolution was found.** The audit's honest report: the Pioneer partner — anisotropic
thermal emission — has been explicitly tested here and **fails on sign**, which is the strongest
kind of exclusion because it does not depend on getting the magnitude right. Of the reservoirs
considered, none survives; the residual specification is an impulsive coupling delivering
~1–10 mm/s over a perigee passage of order hours, direction-correlated with the flyby geometry.

**And the audit is not the sharpest instrument available on this case.** The non-recurrence at
Juno and at later Rosetta flybys is a stronger datum than any `A` computation, because it
points at the *analysis* rather than the *physics*. Recorded as failure mode F6.

---

## Part C — the procedure

Run on any device reported to produce useful work without carried fuel.

1. **State the observable in units.** Thrust in N, or power in W, with its uncertainty and the
   input power that accompanied it. Per METHOD §3: enter observables, never absences.
   *"Produces 1.2 mN at 1 kW"* is a row. *"Uses an unknown energy source"* is not.
2. **Compute the required coupling** `F_req` from the observable — for a thruster
   `F_req = m·a`; for a generator `F_req = P_useful / v`.
3. **Enumerate candidate reservoirs.** Anything the device is in physical contact or field
   contact with. The standing list, which the Part A/B cases between them exhaust:
   radiation field (emitted, reflected, or ambient) · ambient fluid at a bulk velocity ·
   a second fluid or solid at a *different* bulk velocity · expelled or ablated matter ·
   a magnetic or gravitational field with a relative velocity · orbital kinetic energy ·
   the laboratory frame itself (the planet). **The last is the one people forget, and it is
   the one that turns "thrust" into "pushing on the Earth."**
4. **For each candidate, name `Δu` explicitly and write it down.** This step is not
   bookkeeping — it is the whole instrument. Both errors this procedure has caught in this
   project (the sail, the tether) were caught here, by forcing a number where a word had been.
   *If you cannot write a number, the candidate is not a candidate yet.*
5. **Compute `P_avail`** — the power the candidate can surrender through the device's actual
   coupling cross-section, not through an idealised one. For photons this is the intercepted
   or emitted radiant power; for a flow, `½ρAΔu³`; for expelled matter, `½ṁu_e²`.
6. **Run the availability leg.** `A = (F_req·Δu)/P_avail`. For a photon reservoir this reduces
   to `F_req` against `P_avail/c` (absorption) or `2P_avail/c` (reflection). **`A > 1` rules the
   candidate out.**
7. **Run the energy leg.** `Σ = P_useful/(F·Δu)`. Expect it to pass; treat a failure as
   near-conclusive, since `Σ > 1` violates an identity. See F1.
8. **Run the sign leg.** If `Δu` comes out negative — the device outrunning its own reservoir —
   you have a single-reservoir model of a two-reservoir system. Go back to step 3 and find the
   partner. (Part A.4.)
9. **Report per candidate**, in one of four states:
   - `RULED OUT` with the factor by which `A` exceeds 1;
   - `SURVIVES` with the **required property** — anisotropy fraction, mass flux, field
     strength, relative velocity, coupling force;
   - `NOT FORMABLE` — the candidate names no `Δu`, so no `Σ` exists. A statement about the
     model, not the device;
   - `NOT TESTED` — you did not have the numbers. Say which.
10. **Write the residual specification, never a verdict.** The output is the union of the
    `SURVIVES` rows' required properties: *"a reservoir of mass flux ≥ X at relative velocity
    ≥ Y, coupling with force Z."* If the union is empty, the output is *"of the reservoirs
    considered, none supplies the required coupling"* — and the required coupling itself is
    then the specification.
11. **Prefix every negative with "of the reservoirs considered."** Not as hedging. See F2.

---

## The procedure's own failure modes

**F1 — the energy leg almost never fires, and Q9 built the instrument around it.**
`Σ = P_useful/(F·Δu)` reduces to `v/Δu` for a steady harvester, so any device slower than its
reservoirs' relative velocity passes automatically. Every photon-reservoir case passes by
`~10⁻⁴` or better. **`Σ > 1` as a detector would have cleared solar radiation pressure for the
Pioneer anomaly.** The availability leg is doing the work; Σ's role is to guarantee that
whatever survives is thermodynamically coherent, not to eliminate anything.

**F2 — you cannot know the candidate list is complete, and you never will.**
This is not a limitation to be reduced by trying harder; it is the structure of the problem.
The Pioneer case *is* the proof: the surviving reservoir was onboard, ordinary, and sat
unnamed for over a decade while the list was searched. **The honest output is therefore always
"of the reservoirs considered," never "there is none."** A procedure that returns "no
reservoir exists" has silently converted a specification into a verdict, which is the exact
failure this instrument was built to avoid.

**F3 — `P_avail` depends on an assumed coupling cross-section, and that assumption is
free.** The Pioneer solar-pressure exclusion used the 2.74 m dish. Assume a larger effective
area and `A` falls; assume enough area and any photon reservoir survives. State the aperture
you assumed, and prefer the geometrically largest defensible one — because that makes
exclusions conservative and admissions cheap, which is the right direction of error for a
specification instrument.

**F4 — `A ≤ 1` is necessary, never sufficient.** Solar radiation pressure passes the *energy*
leg for Pioneer and is nonetheless wrong. The audit tests only the momentum-energy ledger; it
is blind to spatial signature (`r⁻²` dependence), temporal signature, and direction. **A
surviving candidate is a candidate, not an answer.** The discriminating measurement of
METHOD §3 column 3 remains a separate obligation.

**F5 — apparatus artefacts are outside the ledger entirely.** The EmDrive's resolution was a
balance mount warping under thermal load. There is no reservoir enumeration that finds this,
because the reported force was never in the device's momentum ledger at all. **Before running
the audit, ask whether the observable is a property of the device or of the instrument.** The
audit assumes the measurement; METHOD §5 governs the measurement.

**F6 — the audit is often not the sharpest instrument on the case.** For the flyby anomaly,
non-recurrence at Juno and later Rosetta flybys carries more weight than any `A` computation,
and points at the analysis rather than the physics. METHOD §5's rules — same-method
disagreements are systematics; single-group claims resolve against the claimant — should be
applied *first*, and the audit run on what survives them.

**F7 — weak sourcing propagates into the exclusion factor.** The Mach-effect exclusion above
is `A = 3.6`, a factor of four, resting on an **UNVERIFIED** claim magnitude and a
**SECONDARY** account of the null result. A factor-of-four exclusion built on a factor-of-two
uncertainty is not an exclusion. **Report `A` with the uncertainty of its weakest input**, and
treat `1 < A < 10` on unverified inputs as `NOT TESTED`, not as `RULED OUT`.

---

## Standing

Part A: **passed, five for five**, with two corrections to this project's own bookkeeping
(albatross `L/D` closed at 21.2; the tether's reservoir renamed from planetary rotation to
orbital kinetic energy for every tether actually flown). Part B: the Pioneer case
**reproduces the published resolution to 7% from pre-resolution inputs**, which is the
strongest evidence this procedure works. The EmDrive returns a checkable mass-flux
specification rather than a verdict. The flyby anomaly returns
`UNRESOLVED-IN-SOURCES` and a sign-based exclusion of the Pioneer mechanism.

**The procedure is sound enough to point at an unresolved case**, with three conditions: run
the availability leg and not only Σ, run METHOD §5 on the measurement first, and prefix every
negative with *of the reservoirs considered*.

The instrument is a [[positive-controls]] construction applied to physics rather than to
citation counts — the five Part A rows are the known-closed pairs, and they are what makes the
Part B results mean anything.

See [[Q9-fuel-free-is-an-assumption]], [[C8-momentum-harvesting-metric]], [[positive-controls]].
