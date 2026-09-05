---
name: C11-flyby-reservoir-audit
type: computed
---

# The flyby anomaly, audited: what a real reservoir would have to be

> **Of the reservoirs considered, none supplies NEAR's +13.46 mm/s with the right sign and
> magnitude.** The geomagnetic/rotation coupling is ruled out by `A ≈ 1.7×10⁶` (an uncharged
> 730 kg body is not a tether); anisotropic thermal radiation by `A ≈ 160` *and independently
> on sign* (Rievers & Lämmerzahl compute a **−2.5 mm/s deceleration** for Rosetta against an
> observed **+1.8 mm/s** increase); atmospheric drag by sign and by `A ≈ 18` at 539 km. Tidal /
> gravitational-gradient coupling is `NOT FORMABLE` — Earth's Newtonian field is static, so
> `Δu = 0` and it is a reaction, not a harvester. The only candidate that `SURVIVES` the
> availability leg is an Earth-bound dark-matter halo (Adler), and it survives only as a
> *specification*: it requires a local density `~10⁻¹⁵ kg/m³`, some `10⁷–10¹¹×` the galactic
> halo, in severe tension with ephemeris bounds. **The residual specification is an impulsive,
> geometry-signed coupling delivering `F ≈ 0.5–5 mN` on a 730 kg body over one perigee passage,
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
`K = 2×7.292115e−5×6.371e6 / 2.9979e8 = 3.0993×10⁻⁶` — agrees with the value quoted in the
source.

**NEAR declinations, now sourced** (was UNVERIFIED "from memory"). `δ_i = −20.76°`,
`δ_o = −71.96°`, with `(cos δ_i − cos δ_o) = 0.626`, are tabulated in Table 1 of
**Acedo, Piqueras & Moraño (2019)**, *A possible flyby anomaly for Juno at Jupiter*, MNRAS
489:3232, which attributes them to Anderson et al. (2008) and Jouannic et al. (2015):
[academic.oup.com/mnras/article/489/3/3232/5555577](https://academic.oup.com/mnras/article/489/3/3232/5555577),
fetched **2026-09-05**. Tag: **VERIFIED-SECONDARY** — an open-access paper quoting the PRL's
values, not the PRL itself, which remains paywalled (the APS record was not full-text fetched).
The same table gives the Anderson-formula prediction **13.295 mm/s** against the observed
`13.46 ± 0.01 mm/s`, which is the check below, independently computed by the same source.

**Check recomputed this session** from those sourced declinations:
`cos(20.76°) = 0.93507`, `cos(71.96°) = 0.30968`, difference `0.62539`;
`ΔV∞ = 6851 × 3.0993×10⁻⁶ × 0.62539 = 1.328×10⁻² m/s = 13.28 mm/s`
against the observed **13.46** — **1.3% low** (agreeing with the source's own 13.295 to
0.1%). Whatever the reservoir is, the effect scales
as `2ΩR_⊕ = 929 m/s` (twice Earth's equatorial surface speed) divided by `c`. **That factor
is the specification's fingerprint and every candidate below is measured against it.**

**Required coupling for NEAR** (audit step 2).

*The Oberth conversion — corrected 2026-09-05.* `ΔV∞` is a change in **hyperbolic excess**
speed, not the impulse applied at perigee. The impulse must be taken where it is applied, and
energy is the invariant that connects them. Energy gained is

```
ΔE = m V∞ ΔV∞ = 730 × 6851 × 0.01346 = 6.73×10⁴ J        (specific Δε = V∞ΔV∞ = 92.2 m²/s²)
```

The same `ΔE` delivered as a prograde impulse at perigee, where the speed is `V_p`, is
`ΔE = m V_p Δv_p`, so

```
Δv_p = ΔE / (m V_p) = (V∞/V_p)·ΔV∞
     = 6.73×10⁴ / (730 × 12739)
     = (6851/12739) × 13.46 mm/s
     = 7.24 mm/s
```

This is the Oberth factor `V∞/V_p = 0.5378`. The perigee impulse is *smaller* than `ΔV∞`,
because at perigee the spacecraft is moving faster and buys more energy per unit `Δv`.

Momentum change `Δp = m Δv_p = 730 × 7.2388×10⁻³ = 5.28 kg·m/s`. Delivered over the encounter
timescale: perigee-localized `τ_peri = 2r_p/V_p = 1085 s` gives
`F_req = 5.284/1085 = 4.87×10⁻³ N`; the full near-Earth passage `τ ≈ 10⁴ s` gives
`F_req = 5.28×10⁻⁴ N`. **`F_req ≈ 0.5–5 mN`.**

*Superseded:* the pre-2026-09-05 version of this note used `Δp = m ΔV∞ = 9.83 kg·m/s` directly,
giving `F_req ≈ 1–9 mN`. That omitted the Oberth factor and is **1.86× too large**
(`9.83/5.284 = 1.860`). Every `A` below is correspondingly 1.86× smaller than previously
quoted; no verdict flips (§2).

Following [[reservoir-audit]] F3, exclusions below use the *conservative*
`F_req = 5.28×10⁻⁴ N ≈ 0.53 mN` (largest defensible aperture / longest timescale), which makes
the exclusions harder to earn and therefore trustworthy.

---

## 2. Per-reservoir audit

Availability leg `A = (F_req·Δu)/P_avail = F_req / F_max`, where `F_max` is the greatest force
the reservoir can couple through NEAR's actual cross-section. `A > 1` rules a candidate out.
All `A` below use the post-Oberth conservative `F_req = 5.28×10⁻⁴ N` (§1).

| Reservoir | `Δu` | `F_max` (couplable) | **A** | Verdict |
|---|---|---|---|---|
| Earth rotation via geomagnetic field (Lorentz/tether) | `Ω r_p = 504 m/s` | `Q v B ≈ 3.1×10⁻¹⁰ N` | **≈ 1.7×10⁶** | **RULED OUT** |
| Atmosphere / exosphere drag at perigee | `Ω r_p ≈ 504 m/s` (corotation) | `≈ 3×10⁻⁵ N` (539 km) | **≈ 18**, and **wrong sign** | **RULED OUT** |
| Anisotropic thermal radiation (Pioneer mechanism) | `c` | `P_rad/c ≈ 3.3×10⁻⁶ N` (η=1) | **≈ 160**, and **wrong sign** | **RULED OUT** |
| Tidal / gravitational-gradient coupling | `0` (static field) | — | `F·Δu = 0` | **NOT FORMABLE** |
| Earth-bound dark-matter halo (Adler) | ~few×10² m/s | set by `ρ_DM, σ` | `≤ 1` by construction | **SURVIVES (as spec)** |

### 2.0 Aperture sensitivity — *added 2026-09-05 from `audits/staged`*

[[reservoir-audit]] Part C step 5 now requires the assumed coupling cross-section to be stated
and `A` reported at **2×** and **0.5×** that aperture. An exclusion that does not survive the 2×
row is `NOT TESTED`, not `RULED OUT`. Nothing below is recomputed; all values are the current
post-Oberth ones (`F_req = 5.28×10⁻⁴ N`) and **no verdict changes.**

**Scaling assumed:** `A = F_req/F_max` with `F_max` linear in the aperture for all three
reservoirs — Lorentz `F = QvB` with `Q = CV` and capacitance linear in effective conducting
radius; drag `F = ½ρV²C_dA` linear in frontal area; thermal `F = P_rad/c` with radiated power
linear in radiating area. Hence `A(2×) = A/2` and `A(0.5×) = 2A`. Stating this scaling is what
makes the sensitivity two lines rather than a re-derivation.

| Reservoir | Assumed aperture (nominal) | `F_max` | **A (nominal)** | A (2× aperture) | A (0.5× aperture) | Verdict |
|---|---|---|---|---|---|---|
| Earth rotation via geomagnetic field (Lorentz) | spacecraft floating-charge capacitance `C ≈ 10⁻¹⁰ F` at `V ≈ 10 V`, i.e. a ~1 m effective conducting radius; **no deployed conductor** | `QV_pB ≈ 3.1×10⁻¹⁰ N` | **1.7×10⁶** | 8.5×10⁵ | 3.4×10⁶ | **RULED OUT** — survives 2× by six orders |
| Anisotropic thermal radiation | full spacecraft radiating envelope at `P_rad ≤ ~1 kW`, `η = 1` (fully collimated) | `P_rad/c ≈ 3.34×10⁻⁶ N` | **160** | 80 | 320 | **RULED OUT** — survives 2× by ~2 orders; also excluded on sign |
| Atmosphere / exosphere drag at 539 km | NEAR frontal area with `C_d` order unity, `ρ ≈ 10⁻¹³ kg/m³` | `≈ 3×10⁻⁵ N` | **18** | **9** | 36 | **RULED OUT** — survives 2×, but this is the row where the rule bites |

**The drag row is the one the aperture rule was written for.** `A = 18` nominal falls to **9** at
twice the assumed frontal area — still an exclusion, but a one-order one resting on an exospheric
density marked UNVERIFIED and solar-cycle dependent. Per [[reservoir-audit]] F7 (`1 < A < 10` on
unverified inputs is `NOT TESTED`, not `RULED OUT`), **the drag exclusion at 2× aperture sits
exactly on that boundary and is carried by the sign argument, not by `A`.** The Lorentz and
thermal exclusions are aperture-insensitive to any defensible factor: an aperture large enough to
rescue the Lorentz coupling would need to be ~10⁶ times NEAR's, which is not a spacecraft.

### 2.1 Earth rotation via the geomagnetic field — RULED OUT, `A ≈ 1.7×10⁶`

The tempting candidate: `K = 2ΩR_⊕/c` *contains Earth's rotation*, so the formula reads like a
rotational coupling. Run the audit. The reservoir is Earth's rotational KE; the coupling is the
Lorentz force `F = Q v × B`. NEAR is **not a tether** — no deployed conductor, no driven current.
Its natural floating charge in the plasmasphere is `Q ~ C·V ~ (10⁻¹⁰ F)(10 V) ~ 10⁻⁹ C`. The
dipole field at perigee is `B = 3.1×10⁻⁵ (R_⊕/r_p)³ = 2.43×10⁻⁵ T`. Then
`F_max = Q V_p B = 10⁻⁹ × 12739 × 2.43×10⁻⁵ = 3.1×10⁻¹⁰ N`, and

```
A = F_req / F_max = 5.28×10⁻⁴ / 3.1×10⁻¹⁰ ≈ 1.7×10⁶     →  RULED OUT
```

**Charge shortfall — corrected 2026-09-05.** To reach `F_req` the spacecraft would need

```
Q_req = F_req / (V_p B) = 5.284×10⁻⁴ / (12739 × 2.43×10⁻⁵)
      = 5.284×10⁻⁴ / 0.3096
      = 1.71×10⁻³ C  ≈  1.7 mC
```

against the assumed floating `Q ~ 10⁻⁹ C` — a shortfall of `log₁₀(1.71×10⁻³/10⁻⁹) = 6.2`, i.e.
**~6 orders of magnitude**, which is by construction the same number as `A ≈ 1.7×10⁶` (both
are linear in `Q`, so `Q_req/Q_float ≡ A` exactly). *Superseded:* this note previously said
`Q ≈ 3 C` and "~10 orders of magnitude", which was three orders too large and inconsistent
with its own `A`. (The audit's intermediate figure of 3.2 mC / 6.5 orders used the
pre-Oberth `F_req = 1 mN`; with the corrected `F_req` the self-consistent values are 1.7 mC
and 6.2 orders.) The **gravitomagnetic** reading of the same `2ΩR_⊕/c` (frame-dragging from
Earth's spin) is a genuine GR effect but its magnitude is `~10⁻⁹` of the Newtonian term, known
too small by 5–6 orders. Either way the rotation reservoir is ruled out. *This is the row the
Anderson formula bait-and-switches on: the formula's algebraic form mimics a rotational coupling
whose physical coupling is `~10⁶` too weak to be it.*

### 2.2 Atmosphere / exosphere drag — RULED OUT on sign, `A ≈ 18`

Sign first. NEAR moves at `V_p = 12.7 km/s`, vastly faster than the corotating atmosphere
(`Ω r_p ≈ 0.5 km/s`), so drag **removes** along-track energy: `ΔV∞ < 0`. NEAR gained
(`+13.46`) → **wrong sign**. Magnitude at 539 km: with `ρ ~ 10⁻¹³ kg/m³` (**UNVERIFIED**
estimate; solar-cycle dependent), `F_drag ≈ ½ρV_p²C_dA ≈ 3×10⁻⁵ N`, giving `A = 5.28×10⁻⁴/3×10⁻⁵ ≈ 18`. Both
legs exclude it for NEAR. **Where drag *is* the reservoir and is correctly signed: Galileo II**
at 303 km, whose `−3.4 mm/s` atmospheric contribution is explicitly modeled and **VERIFIED**
([1711.02875](https://ar5iv.labs.arxiv.org/html/1711.02875)). Drag is a real, correctly-signed,
low-perigee *negative* reservoir; it cannot supply NEAR's positive 13 mm/s.

### 2.3 Anisotropic thermal radiation (the Pioneer mechanism) — RULED OUT, `A ≈ 160`, and on sign

`Δu = c`. NEAR is solar-powered; the total radiated power (absorbed sunlight + internal
dissipation) at 1 AU is at most `~1 kW`. Fully collimated ceiling `F_max = P_rad/c =
1000/2.9979×10⁸ = 3.34×10⁻⁶ N`, so

```
A = 5.28×10⁻⁴ / 3.34×10⁻⁶ ≈ 160     →  RULED OUT (at η=1; realistic η~few % → A~10³–10⁴)
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

- **Coupling force** `F ≈ 5.3×10⁻⁴ N` (over the ~hours passage) to `4.9×10⁻³ N`
  (perigee-localized), on a 730 kg body — i.e. the perigee impulse
  `Δv_p = (V∞/V_p)·ΔV∞ = 7.24 mm/s`, not `ΔV∞` itself (§1). Energy `ΔE ≈ 6.7×10⁴ J`,
  specific `Δε ≈ 92 m²/s²`.
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
already killed the rotation/Lorentz coupling by `1.7×10⁶` and thermal by `160`. **What is left is
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

**UNVERIFIED items** (from memory, not fetched): exospheric density `~10⁻¹³ kg/m³` at 539 km;
spacecraft floating charge `~10⁻⁹ C`; ephemeris DM bound `~10⁻¹⁹–10⁻²⁰ g/cm³`. All are inputs
to exclusions that hold by 1–3 orders of margin even under generous variation, per the F3
conservative-aperture rule.

---

## Corrections 2026-09-05

Source for all three: `audits/01-math-physics.md` (items 13, 14 and priority actions 1-3);
backlog rows A1-A3.

| # | What was wrong | What it is now | Why |
|---|---|---|---|
| A1 | `F_req` computed as `m·ΔV∞/τ`, giving **1-9 mN** | `F_req` = **0.53 mN** (10^4 s) to **4.87 mN** (`tau_peri` = 1085 s); headline **0.5-5 mN** | `ΔV∞` is a change in hyperbolic *excess* speed; the impulse is applied at perigee. `ΔE = m V∞ ΔV∞ = m V_p Δv_p` gives the Oberth conversion `Δv_p = (V∞/V_p)·ΔV∞ = 0.5378 × 13.46 = 7.24 mm/s`, so `Δp = 5.28` not `9.83 kg·m/s`. Factor **1.86** |
| A1 | `A ≈ 3×10^6` / `300` / `30` | `A ≈ 1.7×10^6` / `160` / `18` | Same 1.86 divided through; `F_max` values unchanged. **No verdict flips** - all three remain `A > 1` and RULED OUT, and drag and thermal are independently excluded on sign |
| A2 | "the spacecraft would need `Q ≈ 3 C` ... by ~10 orders of magnitude" | `Q_req = F_req/(V_p B) = 5.284×10^-4/(12739 × 2.43×10^-5) = 1.7 mC`; shortfall **6.2 orders** | The old figure was 3 orders too large and contradicted the note's own `A`. `Q_req/Q_float` is identically `A`, so 1.7 mC / 6.2 orders / `A = 1.7×10^6` are now one number stated three ways |
| A3 | NEAR declinations marked **UNVERIFIED**, "from memory" | `δ_i = -20.76°`, `δ_o = -71.96°` sourced from Acedo, Piqueras & Morano (2019), MNRAS 489:3232, Table 1, fetched 2026-09-05; tagged **VERIFIED-SECONDARY** | The values were right. The check re-runs to **13.28 mm/s** vs observed 13.46 (1.3% low), matching the source's own 13.295 to 0.1%. Secondary, not primary: the source quotes Anderson et al. (2008); the PRL itself is paywalled and was not full-text fetched |

Also removed: two stray XML-ish tags (`</content>`, `</invoke>`) left at the end of the file by
a previous editing session. No content change.

**Not done.** The PRL 100:091102 full text was not obtained (APS paywall; no arXiv preprint
found for Anderson et al. 2008 - searched 2026-09-05). Per backlog B16 the declinations are
therefore VERIFIED-SECONDARY, and the remaining UNVERIFIED inputs (exospheric density,
floating charge, ephemeris DM bound) are unchanged by this pass.
