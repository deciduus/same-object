---
name: reservoir-audit
type: method
---

<!-- FIRST OPEN-CASE RUN: [[C11-flyby-reservoir-audit]], 2026-09-03. The flyby anomaly.
Excluded, of the reservoirs considered: geomagnetic tether (A≈3e6), drag (A≈30, wrong sign),
thermal (A≈300, wrong sign, Rievers-verified), tidal (not formable, Δu=0). Sign+non-recurrence
leave no static reservoir standing. Residual: impulsive 1-9 mN, along-track, scaling as
2ΩR⊕/c, non-stationary in epoch. -->

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

## Part B — hard-positive controls on resolved anomalies

**Renamed 2026-09-05. This was headed "negative controls" and it is not one.** Every row below
is a real anomaly with a real, nonzero residual and a partner that turned out to exist. That is
a *hard positive* control — a case where the answer is known and difficult, testing whether the
instrument recovers a true signal it could plausibly have missed. A **negative** control is the
opposite input: a system with **no** residual, testing whether the instrument can return
*nothing*. This section contains none, and until Part D is run the audit has never been shown
capable of a null output. See Part D below.


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

0. **Establish that there is an agreed observable — before any `A` is computed.** Two parts,
   both mandatory, both prior to step 1.
   **(a) Significance.** State the observable's central value with its uncertainty. If the
   interval contains zero, halt with `NO OBSERVABLE TO EXPLAIN` (D.2) and enumerate nothing.
   **(b) The reductions table.** List **every independent reduction of the same photons or
   records** — team, pipeline, central value, stated significance, and which rows share raw data.
   If the rows span "detected" and "not detected", halt with `NO AGREED OBSERVABLE` (D.3) and do
   not proceed unconditionally. A conditional run downstream of this halt may claim calibration
   against a known enumeration; it may **not** assert its residual specification as real.
   **No `A`, no `Σ`, no candidate enumeration may be written before the table exists.**

   | Case | Step-0 finding | Verdict |
   |---|---|---|
   | [[C11-flyby-reservoir-audit]] — NEAR flyby | one agreed number across groups: `ΔV∞ = +13.46 ± 0.13 mm/s`, `13.46/0.13 ≈ 100σ`; no reduction reports a null for NEAR | **agreed observable → proceed** |
   | [[C30-venus-phosphine-audit]] — Venus PH₃ | same SOFIA photons → `<0.8 ppb` (Cordiner 2022) and `3 ppb at 5.7σ` (Greaves 2023); same ALMA photons → `20 ppb` then `1–7 ppb`; significance carried by the passband polynomial order | **pipeline-dependent → halt, `NO AGREED OBSERVABLE`** |
   | D.2 fabricated thruster | one reduction, `F = (0.4 ± 3.0) µN`; central value inside its own error bar | **halt, `NO OBSERVABLE TO EXPLAIN`** |

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
5. **State the assumed coupling cross-section (the aperture), as a named row, and report `A`
   at 2x and 0.5x that aperture.** MANDATORY, not optional. Per F3 the aperture is a free
   parameter and `A` is not reproducible between analysts without it. Write the assumed area or
   effective radius, what physical feature it corresponds to, and the sensitivity line
   `A(2x aperture)` / `A(nominal)` / `A(0.5x aperture)`. For every reservoir in this note's
   experience `P_avail` is linear in the aperture, so the sensitivity is `A/2` and `2A` — but
   **state the scaling you assumed**, because a lifting-surface coupling is not linear in area
   and the case where it is not is the case that matters. **An exclusion that does not survive
   the 2x row is not an exclusion**; report it as `NOT TESTED` per F7.
6. **Compute `P_avail`** — the power the candidate can surrender through the aperture named in
   step 5, not through an idealised one. For photons this is the intercepted or emitted radiant
   power; for a flow, `½ρAΔu³`; for expelled matter, `½ṁu_e²`.
7. **Run the availability leg.** `A = (F_req·Δu)/P_avail`. For a photon reservoir this reduces
   to `F_req` against `P_avail/c` (absorption) or `2P_avail/c` (reflection). **`A > 1` rules the
   candidate out.**
8. **Run the energy leg.** `Σ = P_useful/(F·Δu)`. Expect it to pass; treat a failure as
   near-conclusive, since `Σ > 1` violates an identity. See F1.
9. **Run the sign leg.** If `Δu` comes out negative — the device outrunning its own reservoir —
   you have a single-reservoir model of a two-reservoir system. Go back to step 3 and find the
   partner. (Part A.4.)
10. **Report per candidate**, in one of four states:
   - `RULED OUT` with the factor by which `A` exceeds 1;
   - `SURVIVES` with the **required property** — anisotropy fraction, mass flux, field
     strength, relative velocity, coupling force;
   - `NOT FORMABLE` — the candidate names no `Δu`, so no `Σ` exists. A statement about the
     model, not the device;
   - `NOT TESTED` — you did not have the numbers. Say which.
11. **Write the residual specification, never a verdict.** The output is the union of the
    `SURVIVES` rows' required properties: *"a reservoir of mass flux ≥ X at relative velocity
    ≥ Y, coupling with force Z."* If the union is empty, the output is *"of the reservoirs
    considered, none supplies the required coupling"* — and the required coupling itself is
    then the specification.
12. **Prefix every negative with "of the reservoirs considered."** Not as hedging. See F2.

---

## Part D — negative controls (D.1/D.2 design, NOT YET RUN; D.3 has one contaminated datum)

Part A is a soft-positive set, Part B a hard-positive set. **There is no input on which this
instrument has ever returned "nothing here."** Step 11 guarantees an output by construction — if
the union of surviving specifications is empty, the required coupling *itself* becomes the
specification. An instrument that cannot return a null is not validated, it is only exercised.

This section specifies the negative controls and, crucially, **what output would count as
the instrument correctly returning nothing.** D.1 and D.2 are design only — neither is run here,
and no number in them is a result. **D.3 is different: it was written after a real run
([[C30-venus-phosphine-audit]], 2026-09-05) surfaced a failure class D.2 did not anticipate, and
its status is stated honestly in D.3a — the datum exists but is contaminated.**

### D.1 — A fully accounted device: a Betz-calibrated wind turbine

**The input.** A utility-scale horizontal-axis turbine with published rotor diameter, hub-height
wind speed, air density and measured electrical output, at a point on its power curve where the
measured power coefficient `C_p` is a documented fraction of the Betz limit `16/27 = 0.593`.
Every watt is accounted: one reservoir (the ambient flow), one sink (the grid), a known loss
budget. There is no anomaly, because there is no unexplained force.

**Why this is the right null.** It is the exact structural mirror of Part A's rows — same
reservoir class (a fluid at a bulk velocity), same identity, same arithmetic — differing only in
that the residual is zero by construction. If the audit manufactures a specification here, it
manufactures one everywhere, and the Part B outputs (Pioneer's 3.2% anisotropy, the EmDrive's
2.4 mg/s) are artefacts of the procedure rather than of the devices.

**What counts as returning nothing.** All three of:

1. `A ≤ 1` for the ambient flow at the nominal aperture (the swept disc), *and* the required
   coupling recovered from the observable is inside the uncertainty of the coupling the flow can
   actually supply — i.e. `A` is not merely under 1 but consistent with the accounted value.
2. The step-11 union is **non-empty and already occupied**: the surviving specification names the
   ambient flow with a required property that the published `C_p` already satisfies. The correct
   null output is *"the reservoir considered supplies the required coupling; no residual"* — not
   an empty candidate list.
3. **No second reservoir is demanded.** If the procedure, run honestly, emits a specification for
   an *additional* partner, that is a failure of the negative control and must be recorded as
   such.

**What would count as a failure.** Any of: the aperture step (step 5) being tuned until a
residual appears; a `1 < A < 2` exclusion of the ambient flow at nominal aperture (which would
mean the instrument rules out the reservoir that is demonstrably doing the work); or a residual
specification stated in units the published loss budget already covers.

### D.2 — A fabricated thrust report consistent with zero

**The input.** A synthetic, clearly-labelled fabricated report: a thruster of stated mass and
input power reporting a thrust whose central value is **smaller than its own stated
uncertainty** — e.g. `F = (0.4 ± 3.0) µN at 50 W`. Nothing else about it is anomalous. The
fabrication is deliberate and must be flagged in the note that carries it so it can never be
mistaken for a real device; it exists to test the procedure, not the physics.

**Why this is the right null.** Part B's inputs all had a central value many sigma from zero.
This one does not, and step 2 (`compute the required coupling from the observable`) will happily
convert a zero-consistent observable into a finite `F_req` and carry it through to a residual
specification. **That is the specific failure the control is built to catch:** the instrument
has no step that asks whether the observable is distinguishable from zero before it starts
specifying what would have to explain it.

**What counts as returning nothing.** The procedure must halt at step 1 or 2 with:

- `F_req` reported as an **interval containing zero**, and therefore
- the verdict `NO OBSERVABLE TO EXPLAIN` — a fifth state alongside step 10's four (`RULED OUT`,
  `SURVIVES`, `NOT FORMABLE`, `NOT TESTED`) — and **no candidate enumeration performed at all.**

If the procedure as currently written cannot produce that state, then the control has found a
missing step, and the fix is a step 0: *state the observable's significance; if the observable is
consistent with zero, the audit does not run.* That would be a real amendment earned by a
negative control, which is the point of running one.

**Relationship to F5.** D.2 is adjacent to but distinct from the apparatus-artefact failure. F5
says the audit cannot detect that a real, significant reading came from the balance mount rather
than the device. D.2 says the audit does not currently check whether there is a reading at all.
The first is out of the instrument's reach; the second is inside it and unguarded.

### D.3 — The pipeline-dependent central value (first real datum: [[C30-venus-phosphine-audit]])

**The failure class.** *The central value is a function of the reduction pipeline.* An observable
whose reported magnitude, extracted from the **same raw photons or the same raw records**, changes
the **sign of the conclusion** across independently written reductions — one pipeline reports a
detection, another reports an upper bound excluding it. The quantity being audited is then not a
property of the source but of the analysis, and there is no number for a reservoir to be required
to supply.

**How it differs from the two neighbours it is easily confused with.**

- **Not D.2.** D.2 is a *single* central value sitting inside its *own* stated error bar —
  `F = (0.4 ± 3.0) µN`. One reduction, one interval, the interval contains zero. The verdict is
  `NO OBSERVABLE TO EXPLAIN`. In D.3 each individual reduction may be internally significant —
  Greaves 2023 reports `3 ppb at 5.7σ`, Cordiner 2022 reports `<0.8 ppb` at 99% — and it is the
  *disagreement between* them, not the width of either, that voids the observable. The verdict is
  `NO AGREED OBSERVABLE`. A D.3 case can pass D.2's test row by row and still have nothing to explain.
- **Not METHOD §5 same-class systematics.** §5 governs two *measurements* that disagree — different
  apparatus, different epochs, same class — and rules that the disagreement is a systematic. D.3 is
  narrower and worse: there is only one measurement. The photons were taken once. What disagrees is
  the software downstream of them, so no amount of re-observation with the same pipeline family
  settles it, and the "independent check" that would settle a §5 case does not exist here.

**The step-0 test that detects it.** Before any `F_req`, `S_req` or `A` is computed:

> List **every independent reduction of the same photons or records** as a row: team, pipeline,
> central value, stated significance, and whether the raw data are shared with another row.
> If the set of rows spans **"detected"** and **"not detected"** — i.e. one row's central value lies
> outside another row's stated exclusion interval — **halt with `NO AGREED OBSERVABLE`** and do not
> proceed unconditionally.

The Venus rows that trip it: rows 8 and 9 of C30 §1 are the *same three November 2021 SOFIA flights*
reduced to `<0.8 ppb` and to `3 ppb at 5.7σ`; rows 1 and 2 are the same ALMA photons before and
after recalibration, differing `20×`.

**What a conditional run may claim, and what it may not.** The halt does not forbid running §2
onward; it forbids running them unconditionally. A conditional run:

- **May claim calibration.** Run the ledger against a *known, published enumeration* of the same
  routes and report whether the instrument reproduces that enumeration's verdict list route for
  route. C30 does exactly this against Bains et al. 2021 and matches on every row Bains bounds.
  That is a statement about the **instrument**, and it is valid whether or not the observable exists.
- **May claim divergences from that enumeration**, provided they are procedural and stated as such
  (C30's D1/D2/D3).
- **May not claim a residual specification as real.** The step-11 output of a conditional run is
  *"if the observable were real, a source would have to supply X"* — a conditional, and it must be
  written as one, in the callout as well as in the section. It is not a specification of anything
  in the world, it may not be quoted without its antecedent, and it may not be counted as an
  instrument output in any standing.
- **May not upgrade the halt.** No amount of ledger structure downstream converts
  `NO AGREED OBSERVABLE` into an observable. What would un-halt it is stated in C30 §1: an amplitude
  stable across independently written, pre-registered reduction pipelines.

### D.3a — The first negative-control datum is contaminated

Recorded here so it cannot be read as stronger than it is. **The C30 halt was announced in advance**
— named in `audits/scout-03-astrobiology.md` §Job 1 and restated in the commissioning brief the
agent ran from. The agent was told the case halts and then reported that it halts. **It therefore
tests only that the step-0 state is reachable and well-defined on a real, messy input; it does not
test whether the instrument halts on its own.** Part D's central question — *can this audit produce
a null unprompted?* — remains **unanswered**, and D.3 must not be counted as a passed negative
control.

**The uncontaminated test.** A future run must be **briefed blind**: the agent is not told whether
the case is resolved, not told a halt is expected, and not told which of D.1/D.2/D.3 (if any) the
case belongs to. **The brief must be archived, verbatim and dated, before the run begins**, so that
what the agent was and was not told is checkable afterwards rather than reconstructed. A halt
reported from a blind brief is the first uncontaminated datum; a halt reported from any brief that
mentions the expected outcome is contaminated by construction and must be logged as such.

**The blind-brief template** (five lines; nothing else may be added):

```
1. Case: <system + observable, in units, with no verdict word>.
2. Run [[reservoir-audit]] Part C from step 0. Report every step you run and every step you skip.
3. Sources: <the literature entry points, listed without annotation as to what they conclude>.
4. Output: the four (or five) step-10 states per candidate, plus the step-11 residual — or the halt.
5. Do not ask whether this case is resolved, and do not read this brief's archive before reporting.
```

Archive the filled template at `audits/blind-brief-<case>-<YYYY-MM-DD>.md` **before** dispatching,
and cite that path in the resulting note's negative-control section.

### The deliverable

One sentence, per the audit's own discipline: **the input class on which this audit returns
nothing.** On the design above the expected answer is *"observables consistent with zero, and
devices whose reservoir is already accounted to within its measured uncertainty"* — but that
sentence is a prediction until D.1 and D.2 are actually run, and it is recorded here as a
prediction, not a result.

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
specification instrument. **This is now Part C step 5 and is mandatory, with `A` reported at
2x and 0.5x the assumed aperture.** "Prefer the largest defensible" was a preference and
preferences are not reproducible; the sensitivity line is.

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

**F8 — a central value can be a function of the reduction pipeline, and the audit will happily
specify a source for it.** Steps 1–2 convert whatever number they are handed into a finite
`F_req` or `S_req`, with no leg that asks whether independent reductions of the *same raw data*
agree on the number's existence. Venus is the case: `<0.8 ppb` and `3 ppb at 5.7σ` from the same
three SOFIA flights, `20 ppb` and `1–7 ppb` from the same ALMA photons. This is not F6's
same-class systematic — there is only one measurement, and what disagrees is the software
downstream of it, so re-observation with the same pipeline family settles nothing. **The
mandatory reductions table is now Part C step 0(b); a spanning set halts the audit with
`NO AGREED OBSERVABLE`, and anything run past the halt is conditional and must be written as a
conditional.** Designed as D.3; the first datum ([[C30-venus-phosphine-audit]]) is contaminated
because the halt was pre-announced — see D.3a for the blind-brief protocol that would fix it.

---

## Standing

Part A: **passed, five for five**, with two corrections to this project's own bookkeeping
(albatross `L/D` closed at 21.2; the tether's reservoir renamed from planetary rotation to
orbital kinetic energy for every tether actually flown). Part B: the Pioneer case
**reproduces the published resolution to 7% from pre-resolution inputs**, which is the
strongest evidence this procedure works. The EmDrive returns a checkable mass-flux
specification rather than a verdict. The flyby anomaly returns
`UNRESOLVED-IN-SOURCES` and a sign-based exclusion of the Pioneer mechanism.

**The procedure is sound enough to point at an unresolved case**, with five conditions: run
**step 0 before anything else — significance, and the table of independent reductions of the
same raw data** (F8, added 2026-09-05); report the **aperture as a named row with `A` at 2x and
0.5x** (step 5, F3, added 2026-09-05); run the availability leg and not only Σ; run METHOD §5 on
the measurement first; and prefix every negative with *of the reservoirs considered*.

The instrument is a [[positive-controls]] construction applied to physics rather than to
citation counts — the five Part A rows are the known-closed pairs, and they are what makes the
Part B results mean anything.

**What that construction is still missing, stated plainly:** [[positive-controls]] is half of a
control set. Part A is soft-positive, Part B hard-positive, and **there is no negative control** —
no input on which this audit has been shown to return nothing. Part D specifies three (D.1, D.2, D.3) and **none has been run uncontaminated**: D.1 and D.2 are
unrun, and D.3's first datum ([[C30-venus-phosphine-audit]], 2026-09-05) halted correctly but had
the halt pre-announced in its commissioning brief, so it shows the state is reachable, not that
the instrument reaches it unprompted. Every "validated" claim above should still be read as
*validated against positives only*.

See [[Q9-fuel-free-is-an-assumption]], [[C8-momentum-harvesting-metric]], [[positive-controls]].
