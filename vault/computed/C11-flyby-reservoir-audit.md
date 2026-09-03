---
name: C11-flyby-reservoir-audit
type: computed
---

# The flyby anomaly, audited: what a real reservoir would have to be

> **Of the reservoirs considered, none supplies NEAR's +13.46 mm/s with the right sign and
> magnitude.** The geomagnetic/rotation coupling is ruled out by `A ≈ 3×10⁶` (an uncharged
> 730 kg body is not a tether); anisotropic thermal radiation by `A ≈ 300` *and independently
> on sign* (Rievers & Lämmerzahl compute a **−2.5 mm/s deceleration** for Rosetta against an
> observed **+1.8 mm/s** increase); atmospheric drag by sign and by `A ≈ 30` at 539 km. Tidal /
> gravitational-gradient coupling is `NOT FORMABLE` — Earth's Newtonian field is static, so
> `Δu = 0` and it is a reaction, not a harvester. The only candidate that `SURVIVES` the
> availability leg is an Earth-bound dark-matter halo (Adler), and it survives only as a
> *specification*: it requires a local density `~10⁻¹⁵ kg/m³`, some `10⁷–10¹¹×` the galactic
> halo, in severe tension with ephemeris bounds. **The residual specification is an impulsive,
> geometry-signed coupling delivering `F ≈ 1–9 mN` on a 730 kg body over one perigee passage,
> `ΔE ≈ 6.7×10⁴ J`, whose empirical fingerprint is the factor `2ΩR_⊕/c` — the effect scales as
> Earth's equatorial rotation speed (929 m/s) divided by `c`.** Two constraints then bind any
> real reservoir: it must supply **both signs** (which excludes every purely dissipative
> reservoir as sole cause), and it must be **non-stationary between epochs** (Juno 2013 and
> Rosetta II/III were null). No static field — magnetic, gravitational, or tidal — can be
> non-stationary in epoch, so the sign+non-recurrence pair leaves **no known static reservoir
> standing**; it points, per [[reservoir-audit]] F6, at the analysis as much as at the physics.

See [[reservoir-audit]] (the validated instrument, five-for-five plus Pioneer to 7%),
[[Q9-fuel-free-is-an-assumption]] (Σ inverted as a specification instrument), and
[[C8-momentum-harvesting-metric]] (the identity `P = −F·Δu` this whole audit runs on).

---

## 1. Observables

The anchor is **Anderson et al. (2008)**, *Anomalous Orbital-Energy Changes Observed during
Spacecraft Flybys of Earth*, PRL 100, 091102, and its empirical formula. Numbers below were
fetched this session from arXiv HTML mirrors; each carries its status per METHOD §4.

| Flyby | Date | `ΔV∞` (mm/s) | `V∞` (km/s) | Perigee alt (km) | mass (kg) | Status |
|---|---|---|---|---|---|---|
| Galileo I | 1990 | **+3.92 ± 0.08** | 8.949 | 960 | — | **VERIFIED** [1210.7333](https://ar5iv.labs.arxiv.org/html/1210.7333) |
| Galileo II | 1992 | **−4.6** (also quoted −8; **−3.4 from atmospheric drag**) | 8.877 | 303 | — | **VERIFIED** [1701.05735](https://ar5iv.labs.arxiv.org/html/1701.05735), [1711.02875](https://ar5iv.labs.arxiv.org/html/1711.02875) |
| **NEAR** | 1998 | **+13.46 ± 0.13** | 6.851 | 539 | **730** | **VERIFIED** [1210.7333](https://ar5iv.labs.arxiv.org/html/1210.7333), mass+`V_p` [1711.02875](https://ar5iv.labs.arxiv.org/html/1711.02875) |
| Cassini | 1999 | **−2 ± 1** | 16.010 | 1173 | — | **VERIFIED** [1210.7333](https://ar5iv.labs.arxiv.org/html/1210.7333) |
| Rosetta I | 2005 | **+1.80 ± 0.05** | 3.863 | 1954 | — | **VERIFIED** [1210.7333](https://ar5iv.labs.arxiv.org/html/1210.7333) |
| MESSENGER | 2005 | **+0.02 ± 0.01** | 4.056 | 2347 | — | **VERIFIED** [1210.7333](https://ar5iv.labs.arxiv.org/html/1210.7333) |
| Rosetta II / III | 2007 / 2009 | **~0 (null)** | — | — | — | **VERIFIED** null [1711.02875](https://ar5iv.labs.arxiv.org/html/1711.02875) |
| Juno | 2013 | **0 (null)** | 10.389 | 559 | — | **VERIFIED** null [1701.05735](https://ar5iv.labs.arxiv.org/html/1701.05735) |

**NEAR anchor** (largest, cleanest, and solar-powered — so the thermal reservoir is weakest
exactly where the effect is largest): `m = 730 kg`, `V_p = 12.739 km/s` (**VERIFIED**
[1711.02875](https://ar5iv.labs.arxiv.org/html/1711.02875)), `r_p = 6.371×10⁶ + 539×10³ =
6.91×10⁶ m`.

**The Anderson empirical formula** (**VERIFIED** [1711.02875](https://ar5iv.labs.arxiv.org/html/1711.02875)):

```
ΔV∞ / V∞  =  K (cos δ_i − cos δ_o) ,     K = 2 Ω R_⊕ / c
```

with `Ω = 7.292115×10⁻⁵ s⁻¹`, `R_⊕ = 6371 km`. **Computed this session:**
`K = 2×7.292115e−5×6.371e6 / 2.9979e8 = 3.099×10⁻⁶` — agrees with the value quoted in the
source. Using NEAR declinations `δ_i = −20.76°, δ_o = −71.96°` (**UNVERIFIED** — from memory,
not fetched), the formula returns `ΔV∞ = 6851 × 3.099e−6 × (0.935 − 0.310) = 13.28 mm/s`
against the observed **13.46** — a 1.3% match. Whatever the reservoir is, the effect scales
as `2ΩR_⊕ = 929 m/s` (twice Earth's equatorial surface speed) divided by `c`. **That factor
is the specification's fingerprint and every candidate below is measured against it.**

**Required coupling for NEAR** (audit step 2). Momentum change
`Δp = m ΔV∞ = 730 × 0.01346 = 9.83 kg·m/s`. Delivered over the encounter timescale:
perigee-localized `τ_peri = 2r_p/V_p = 1085 s` gives `F_req = 9.06×10⁻³ N`; the full near-Earth
passage `τ ≈ 10⁴ s` gives `F_req = 9.83×10⁻⁴ N`. **`F_req ≈ 1–9 mN`.** Energy gained
`ΔE = m V∞ ΔV∞ = 6.73×10⁴ J`, specific `Δε = V∞ΔV∞ = 92.2 m²/s²`. Following [[reservoir-audit]]
F3, exclusions below use the *conservative* `F_req = 1 mN` (largest defensible aperture / longest
timescale), which makes the exclusions harder to earn and therefore trustworthy.

---

## 2. Per-reservoir audit

Availability leg `A = (F_req·Δu)/P_avail = F_req / F_max`, where `F_max` is the greatest force
the reservoir can couple through NEAR's actual cross-section. `A > 1` rules a candidate out.

| Reservoir | `Δu` | `F_max` (couplable) | **A** | Verdict |
|---|---|---|---|---|
| Earth rotation via geomagnetic field (Lorentz/tether) | `Ω r_p = 504 m/s` | `Q v B ≈ 3.1×10⁻¹⁰ N` | **≈ 3×10⁶** | **RULED OUT** |
| Atmosphere / exosphere drag at perigee | `Ω r_p ≈ 504 m/s` (corotation) | `≈ 3×10⁻⁵ N` (539 km) | **≈ 30**, and **wrong sign** | **RULED OUT** |
| Anisotropic thermal radiation (Pioneer mechanism) | `c` | `P_rad/c ≈ 3.3×10⁻⁶ N` (η=1) | **≈ 300**, and **wrong sign** | **RULED OUT** |
| Tidal / gravitational-gradient coupling | `0` (static field) | — | `F·Δu = 0` | **NOT FORMABLE** |
| Earth-bound dark-matter halo (Adler) | ~few×10² m/s | set by `ρ_DM, σ` | `≤ 1` by construction | **SURVIVES (as spec)** |

### 2.1 Earth rotation via the geomagnetic field — RULED OUT, `A ≈ 3×10⁶`

The tempting candidate: `K = 2ΩR_⊕/c` *contains Earth's rotation*, so the formula reads like a
rotational coupling. Run the audit. The reservoir is Earth's rotational KE; the coupling is the
Lorentz force `F = Q v × B`. NEAR is **not a tether** — no deployed conductor, no driven current.
Its natural floating charge in the plasmasphere is `Q ~ C·V ~ (10⁻¹⁰ F)(10 V) ~ 10⁻⁹ C`. The
dipole field at perigee is `B = 3.1×10⁻⁵ (R_⊕/r_p)³ = 2.43×10⁻⁵ T`. Then
`F_max = Q V_p B = 10⁻⁹ × 12739 × 2.43×10⁻⁵ = 3.1×10⁻¹⁰ N`, and

```
A = F_req / F_max = 1×10⁻³ / 3.1×10⁻¹⁰ ≈ 3×10⁶     →  RULED OUT
```

To reach `F_req` the spacecraft would need `Q ≈ 3 C` — a charge no ~1 m body can hold by ~10
orders of magnitude. The **gravitomagnetic** reading of the same `2ΩR_⊕/c` (frame-dragging from
Earth's spin) is a genuine GR effect but its magnitude is `~10⁻⁹` of the Newtonian term, known
too small by 5–6 orders. Either way the rotation reservoir is ruled out. *This is the row the
Anderson formula bait-and-switches on: the formula's algebraic form mimics a rotational coupling
whose physical coupling is `~10⁶` too weak to be it.*

### 2.2 Atmosphere / exosphere drag — RULED OUT on sign, `A ≈ 30`

Sign first. NEAR moves at `V_p = 12.7 km/s`, vastly faster than the corotating atmosphere
(`Ω r_p ≈ 0.5 km/s`), so drag **removes** along-track energy: `ΔV∞ < 0`. NEAR gained
(`+13.46`) → **wrong sign**. Magnitude at 539 km: with `ρ ~ 10⁻¹³ kg/m³` (**UNVERIFIED**
estimate; solar-cycle dependent), `F_drag ≈ ½ρV_p²C_dA ≈ 3×10⁻⁵ N`, giving `A ≈ 30`. Both
legs exclude it for NEAR. **Where drag *is* the reservoir and is correctly signed: Galileo II**
at 303 km, whose `−3.4 mm/s` atmospheric contribution is explicitly modeled and **VERIFIED**
([1711.02875](https://ar5iv.labs.arxiv.org/html/1711.02875)). Drag is a real, correctly-signed,
low-perigee *negative* reservoir; it cannot supply NEAR's positive 13 mm/s.

### 2.3 Anisotropic thermal radiation (the Pioneer mechanism) — RULED OUT, `A ≈ 300`, and on sign

`Δu = c`. NEAR is solar-powered; the total radiated power (absorbed sunlight + internal
dissipation) at 1 AU is at most `~1 kW`. Fully collimated ceiling `F_max = P_rad/c =
1000/2.9979×10⁸ = 3.34×10⁻⁶ N`, so

```
A = 1×10⁻³ / 3.34×10⁻⁶ ≈ 300     →  RULED OUT (at η=1; realistic η~few % → A~10⁴)
```

Independently **RULED OUT on sign** — the strongest kind of exclusion, per [[reservoir-audit]]:
**Rievers & Lämmerzahl (2011)** modeled thermal recoil pressure for the first Rosetta flyby and
found *"a velocity decrease of the craft of about 2.5×10⁻³ m/s … in contradiction to this the
observed flyby anomaly has shown an increase"* — a **−2.5 mm/s** deceleration against the
observed **+1.8 mm/s** (**VERIFIED**, [1104.3985](https://ar5iv.labs.arxiv.org/html/1104.3985)).
Their verdict verbatim: *"the TRP cannot be the source of the Rosetta flyby anomaly."* The same
model resolves Pioneer. **The Pioneer partner is here, tested, and fails on sign** — the datum
[[reservoir-audit]] B.4 flagged, now quantified. Temporal signature also fails: thermal recoil
is continuous, the anomaly is a perigee-localized velocity jump.

### 2.4 Tidal / gravitational-gradient coupling — NOT FORMABLE

Earth's Newtonian gravity field is static: it does not rotate with the planet's mass. For the
spacecraft's center of mass the field's relative velocity is `Δu = 0`, so `F·Δu = 0` — the
coupling transmits momentum but extracts **no energy**. It is a reaction force, not a harvester
([[reservoir-audit]] classifies the lab-frame/planet reaction this way for the Mach thruster's
B-field). The gravity **assist itself** is momentum exchange with Earth's *heliocentric orbital*
motion (`Δu = 29.8 km/s`), but that is already modeled and subtracted — the anomaly is the
residual *after* it. Tidal stretching of the extended body integrates to `~0` net CM force
(differential `L/r ~ 3 m / 6.9×10⁶ m ~ 4×10⁻⁷` of local `g`). `NOT FORMABLE` as an energy
reservoir for the residual.

### 2.5 Earth-bound dark-matter halo — SURVIVES, as a specification only

This is the one candidate the availability leg does not kill, because its `F_max` is a free
function of the assumed density. **Adler (2008/2009)**,
[0805.2895](https://ar5iv.labs.arxiv.org/html/0805.2895) (**VERIFIED**): reproducing mm/s flyby
`Δv` by DM scattering requires a local Earth-bound density `~10⁷ (GeV/c²) cm⁻³ ≈ 10⁻¹⁵ kg/m³`
for `σ ~ 10⁻²⁸ cm²`, i.e. **`10⁷–10¹¹×` the galactic halo** (`0.3 GeV cm⁻³`), with
`σ_DM-nucleon ≳ 10⁻³³–10⁻²⁹ cm²`, DM mass `≪ 1 GeV`, non-self-annihilating. Crucially Adler's
mechanism gives **both signs** (isotropic elastic scattering decreases `V∞`, exothermic
inelastic increases it) and is trajectory-dependent — exactly the properties §3 demands. So it
`SURVIVES` the availability leg **as the residual reservoir made concrete**, with the required
`(ρ_DM, σ, Δu)` triple as its specification. It is in severe tension (~4–8 orders) with
planetary-ephemeris bounds on bound DM within 1 AU (`~10⁻¹⁹–10⁻²⁰ g/cm³`), and `A ≤ 1` here is
necessary, never sufficient ([[reservoir-audit]] F4). It is not endorsed. It is *specified*.

---

## 3. The two binding constraints: sign and non-recurrence

**Sign.** The anomaly is positive for NEAR (+13.46), Galileo I (+3.92), Rosetta I (+1.8) and
negative for Galileo II and Cassini (−2). **A real reservoir must supply both signs, selected by
the flyby geometry.** The Anderson `(cos δ_i − cos δ_o)` does this automatically; a purely
dissipative reservoir (drag, thermal recoil) cannot — it gives one sign only. **This alone
excludes drag and thermal recoil as the *sole* cause**, independent of every `A` above. The
property forced: the coupling sign must flip with the in/out asymmetry of the trajectory
(`δ_i ↔ δ_o`), i.e. it is odd under time-reversal of the encounter — a real constraint that
narrows the reservoir class sharply.

**Non-recurrence.** Juno (2013) and Rosetta II/III (2007/2009) returned **null** where the
Anderson formula predicts non-null (**VERIFIED**,
[1711.02875](https://ar5iv.labs.arxiv.org/html/1711.02875),
[1701.05735](https://ar5iv.labs.arxiv.org/html/1701.05735)). A real reservoir must explain why
the effect **appears and disappears across epochs, not merely across geometry.** The property
forced: **non-stationarity in time.** No static field — magnetic, gravitational, tidal — can be
non-stationary in epoch; each would reproduce identically at every matched geometry. That
eliminates every *static* reservoir on the list as the sole cause and leaves only (a) a
genuinely time-variable reservoir (Adler's DM cascade; a solar-cycle-dependent atmosphere at
low perigee), or (b) an **analysis artifact** present in the early Doppler reductions and absent
once tracking geometry, station coverage, and drag modeling improved. Per METHOD §5 and
[[reservoir-audit]] F6, non-recurrence *points at the analysis before the physics*: a
single-era signal that did not reproduce when the measurement sharpened is, on this project's
own base rate, the signature of a systematic. **This is the case's sharpest instrument, and it
is not the availability leg.**

---

## 4. The residual specification

Of the reservoirs considered, none of the mundane ones (rotation/Lorentz, drag, thermal, tidal)
supplies NEAR's `+13.46 mm/s` with the right sign and magnitude. The output is therefore the
residual — what any real reservoir must be:

- **Coupling force** `F ≈ 1×10⁻³ N` (over the ~hours passage) to `9×10⁻³ N` (perigee-localized),
  on a 730 kg body. Energy `ΔE ≈ 6.7×10⁴ J`, specific `Δε ≈ 92 m²/s²`.
- **Direction:** along-track (prograde for NEAR — energy gain), sign set by the geometric factor
  `(cos δ_i − cos δ_o)`; **must be able to take either sign.**
- **Temporal profile:** impulsive — delivered over a *single perigee passage*, not continuous.
- **Reservoir relative velocity `Δu`:** whatever the reservoir, the coupling must reproduce the
  empirical fingerprint `2ΩR_⊕/c = 3.099×10⁻⁶` — the effect scales as **Earth's equatorial
  rotation speed (929 m/s) divided by `c`**. Any real reservoir must generate this `ΩR_⊕/c`
  structure, which is why the rotation reservoir is so tempting and why (§2.1) its *physical*
  coupling is `~10⁶` too weak to be it.
- **Non-stationary across epochs** (from §3): the reservoir's state, or the analysis, differed
  between 1998–2005 and 2009–2013.

**Does any known reservoir survive sign + non-recurrence?** No static one. Of the reservoirs
considered, the sign constraint kills drag and thermal recoil as sole cause; the non-recurrence
constraint kills every static field (magnetic, gravitational, tidal); the availability leg had
already killed the rotation/Lorentz coupling by `3×10⁶` and thermal by `300`. **What is left is
either a time-variable dark-matter reservoir carrying the (ρ, σ, Δu) specification above — in
4–8 orders of tension with ephemeris bounds — or an epoch-dependent analysis systematic.** Per
METHOD §5 the correct order is to test the measurement first; on this project's base rate for
single-era, non-reproducing signals, that is where the weight sits. The audit's honest output is
not a verdict but this specification — the force, its geometry-signed direction, its
`ΩR_⊕/c` fingerprint, and the demand that any real reservoir be non-stationary in time. **That
is a positive result: it is exactly what testimony-sets-the-specification means.**

---

## Sources fetched this session

- Anderson formula, K, NEAR mass & `V_p`, Galileo II drag, Rosetta II/III & Juno nulls: [ar5iv 1711.02875](https://ar5iv.labs.arxiv.org/html/1711.02875)
- Flyby `ΔV∞`, `V∞`, perigee-altitude table (Anderson 2008 values): [ar5iv 1210.7333](https://ar5iv.labs.arxiv.org/html/1210.7333)
- Latitudes/inclinations, Juno null, formula: [ar5iv 1701.05735](https://ar5iv.labs.arxiv.org/html/1701.05735)
- Rievers & Lämmerzahl thermal (−2.5 mm/s, wrong sign): [ar5iv 1104.3985](https://ar5iv.labs.arxiv.org/html/1104.3985)
- Adler dark-matter density/cross-section: [ar5iv 0805.2895](https://ar5iv.labs.arxiv.org/html/0805.2895)
- Original: Anderson et al., PRL 100, 091102 (2008), [APS](https://link.aps.org/doi/10.1103/PhysRevLett.100.091102) (abstract/record only, not full-text fetched)

**UNVERIFIED items** (from memory, not fetched): NEAR declinations `δ_i=−20.76°, δ_o=−71.96°`
(used only for the 13.3 vs 13.46 formula check); exospheric density `~10⁻¹³ kg/m³` at 539 km;
spacecraft floating charge `~10⁻⁹ C`; ephemeris DM bound `~10⁻¹⁹–10⁻²⁰ g/cm³`. All are inputs
to exclusions that hold by 1–3 orders of margin even under generous variation, per the F3
conservative-aperture rule.
</content>
</invoke>
