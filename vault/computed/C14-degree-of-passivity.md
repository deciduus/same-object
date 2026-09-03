---
name: C14-degree-of-passivity
type: computed
---

# The degree of passivity is a cycle-averaged energy fraction on ONE axis of a 2×2 lattice — so it narrows G7, it does not close it

> **Verdict: NARROWS.** The portable number [[G7-how-passive]] says nobody has built *is*
> buildable and *is* well-defined across all four domains — but only as a **cycle-averaged
> energy-delivery fraction** `P = W_passive / W_total ∈ [0,1]`, and that number measures exactly
> **one** of the two independent bits the ordinal ladders were secretly encoding. The ladder
> `{passive, quasi-passive, semi-active, hybrid, active}` is **not a total order; it is a 2×2
> (Boolean B²) lattice** on two independent axes — **(1) does the device inject non-conservative
> energy into the load?** and **(2) does it need a control signal / sensor?** `P` refines axis 1
> into a continuum and is blind to axis 2. So two systems with the same `P` can sit in different
> lattice cells (a passive-dynamic walker and a semi-active MR damper both have `P≈1`, yet one
> needs no signal and one does). `P` therefore closes the **energy-passivity** question and leaves
> the **signal-passivity** question exactly where G7 found it. "No portable ordinal ladder" is
> *explained*: each field linearised the same 2D lattice along a **different diagonal**, the same
> lattice-lock failure as [[C12-pi-space-lattice]] — a chain cannot carry a poset of width 2.
> And the control-theory homograph turns out to be **half a synonym, not a false friend**:
> control's passivity index measures axis 1 too, so it and `P` agree on the energy axis and both
> miss the signal axis.

Instrument in the sense of [[specification-instruments]]: the conserved object is **mechanical
work delivered to the load over a cycle** (`P = W_passive/W_total` is bookkeeping on that work, not
a model of any mechanism); the finite enumeration is the **two Boolean bits**; the deliverable is a
**lattice with each field's categories placed on it** and a continuous refinement of one axis.

---

## Part A — The metric, and the non-additivity crux

### A.1 The naive definition and why it breaks

The candidate from the gap note:

```
P = R_passive / R_total = (response with the actuation path cut) / (full response)
```

with `P=1` fully passive, `P=0` fully active. This is fine for a system whose passive and active
contributions **add linearly at a fixed operating point** — but three failures kill it as written:

1. **Sign / protective inversion.** For a *protective* device (a damper, a shock isolator) the
   "response" people care about is a displacement the device is trying to **reduce**. Cutting the
   actuation path makes the displacement *larger*, so `R_passive > R_total` and `P > 1`. The naive
   ratio is not even in `[0,1]`.
2. **Non-additivity under nonlinearity.** If `R = f(passive, active)` with `f` nonlinear (contact,
   clutching, saturation, hysteresis — all four domains have this), then `R_total ≠ R_passive +
   R_active` and `R_total − R_passive` is not "the active contribution." The subtraction is
   meaningless.
3. **"Response" is a different physical quantity in each field** (a displacement, a force, a gait,
   a cooling rate), so a *displacement* ratio and a *cooling-rate* ratio are not the same number
   and cannot be compared — which is the very portability G7 demands.

### A.2 The fix: cycle-averaged energy-delivery fraction

Replace the response ratio by a ratio in a **single conserved currency common to all four domains —
mechanical work / energy delivered to the load** — integrated over one **operating cycle** (a stride,
a load cycle, a diurnal thermal cycle, an accident transient):

```
        ∮ P_passive(t) dt              W_passive
  P  =  ─────────────────────  =  ───────────────────────
        ∮ |P_delivered(t)| dt     W_passive + W_active,inj
```

where `W_active,inj` is the **net non-conservative work the actuator injects into the load** over the
cycle and `W_passive` is the net work delivered by the conservative / dissipative passive structure
(springs, gravity, geometry, material damping). Three properties make this the right object:

- **It is dimensionless and domain-neutral** because energy is energy: a stride's elastic return, a
  damper's dissipated joules, a façade's radiative heat flux, and a reactor's stored-energy release
  are all measured in the same unit before the ratio is taken. This is what buys portability.
- **It handles non-additivity** because it never subtracts responses. Work injected by the actuator
  is measured *directly at the actuator* (`∮ F_act · v dt`), not inferred from `R_total − R_passive`.
  Nonlinearity in how passive and active effects combine at the load is irrelevant — the numerator
  and denominator are separately-metered energy flows, and energy **is** additive even when the
  response is not. This is the crux, and it is why the definition must live in energy, not in `R`.
- **It fixes the sign problem** because for a purely dissipative device `W_active,inj = 0` regardless
  of how much displacement it removes, so `P = 1` — correctly calling an MR damper "energy-passive"
  even though it is "semi-active" on its field's ladder. The protective inversion of A.1 disappears.

**Operating-point caveat, stated honestly.** For a strongly nonlinear system `P` is a functional of
the demand trajectory, so it must be reported *at a stated cycle* (amplitude, frequency, duty), the
same way a damper's loss factor or a gait's cost of transport is. It is not a single scalar property
of the hardware; it is a property of hardware **× operating cycle**. A device can move across `[0,1]`
as the demand changes (a variable-recruitment exo delivers more actuator work at higher speeds). This
is a real limitation and is the honest form of "well-defined": well-defined *given a cycle*, not
context-free.

### A.3 What "response" and "cutting the actuation path" mean in each domain

| Domain | The demand | The delivered "response" (energy currency) | "Cut the actuation path" = |
|---|---|---|---|
| **Nuclear safety (Cat A–D)** | An accident transient (heat, pressure) | Decay-heat removal / reactivity shutdown **energy per transient** | Remove all AC/DC power, signals, operator action; keep only gravity, natural convection, stored springs |
| **Exoskeletons** | A gait cycle at the joint | Net **positive mechanical work** delivered to the limb per stride | Disconnect motors/batteries; keep springs, clutches-as-mechanical-latches, structure |
| **Structural control** | A seismic / wind load cycle | **Energy dissipated + work exchanged** with the structure per cycle | Cut the control power and command signal; device reverts to its uncontrolled (fail-safe) mechanical state |
| **Adaptive façades** | A diurnal thermal / daylight cycle | **Heat flux modulated / cooling energy** per day | Remove actuators and controller; keep passive material response (thermochromism, buoyancy-driven venting, static shading) |

In every row, `P=1` names the system whose **entire delivered energy comes from the passive
structure driven by the demand itself** (gravity, elastic storage, buoyancy, the load), and `P=0`
names the system whose entire delivered energy comes from an injected external source.

### A.4 Relationship to the control-theory passivity index (the homograph, refined)

G7 flagged control theory's *passivity* as a **homograph** — "does not generate energy," not "needs
no actuation" — and called it a different object. That is right, but the relationship is sharper and
more useful than "unrelated":

- Control-theory passivity is the property `∫ u·y dt ≥ − (stored energy)`, i.e. **the system injects
  no net energy** — with the passivity index (IF-OFP, storage-function based, arXiv:2601.04796 as
  cited in G7) quantifying *how far* from that boundary.
- That is **exactly axis 1** of the lattice below (`injects energy?`), and it is the **same axis `P`
  measures**. A purely dissipative MR damper is control-theoretically *passive* (storage function
  exists, injects no energy) **and** has `P = 1` — the two agree.
- Where they diverge is **axis 2**: control-theory passivity says nothing about whether the device
  needs a signal. A semi-active damper is control-passive and `P≈1`, yet its field calls it
  *semi-active* precisely because it needs a control current. "Needs no actuation" = passive on
  **both** axes; "control-theory passive" = passive on axis 1 **only**.

**So they are distinct concepts but not disjoint objects: the control passivity index is a rigorous
storage-function version of `P`'s energy axis.** They coincide on axis 1 and both are blind to axis 2.
That is a stronger statement than G7's "different object, dead end" — it says `P` already has a mature
mathematical twin for half of what it measures, and the *unbuilt* half is the signal axis.

---

## Part B — The discrete structure: the ladder is a 2×2 lattice, not a chain

### B.1 The two independent bits

Read the four fields' own defining criteria and two orthogonal yes/no questions fall out:

- **Axis 1 — Injects energy?** Does the device add **non-conservative motive energy** to the load?
  (The exoskeleton criterion is verbatim this: quasi-passive = *"any controllable element that
  cannot apply a non-conservative motive force"* — VERIFIED, [PMC7344163](https://pmc.ncbi.nlm.nih.gov/articles/PMC7344163/),
  fetched this session.)
- **Axis 2 — Needs a signal?** Does the device require a **sensor / controller / command** to
  function? (The structural criterion is verbatim this: semi-active = *"power only to change device
  properties, not to generate force"* — needs a signal to set the property, injects no force.)

These are **logically independent** — neither implies the other — so the state space is the Boolean
lattice **B² = {0,1} × {0,1}**, a 2×2 with bottom = fully passive, top = fully active, and **two
incomparable middle elements**. That width-2 antichain in the middle is the whole story.

### B.2 The lattice, drawn, with each field placed

```
                    ACTIVE  (1,1)
                  injects energy
                  AND needs signal
                   /            \
                  /              \
   SEMI-ACTIVE / QUASI-PASSIVE   OPEN-LOOP / "POWERED-PASSIVE"
        (0,1)                        (1,0)
   no energy injected,          injects energy,
   BUT needs a signal           needs NO signal
                  \              /
                   \            /
                    PASSIVE  (0,0)
                  no injection, no signal
```

`∨` = join (either bit set → the more-active element), `∧` = meet. `(0,1)` and `(1,0)` are
**incomparable**: neither is "more passive." This is a genuine lattice (every pair has a unique join
and meet) but **not a chain** — and that non-comparability is what no ordinal ladder can represent.

**Placing every field's categories:**

| Field | Category | Injects energy? | Needs signal? | Lattice cell |
|---|---|---|---|---|
| Exoskeleton | passive (Collins clutch+spring) | no | no | **(0,0)** |
| Exoskeleton | quasi-passive (controllable clutch) | no | yes | **(0,1)** |
| Exoskeleton | active (powered) | yes | yes | **(1,1)** |
| Structural | passive (TMD, base isolation) | no | no | **(0,0)** |
| Structural | semi-active (MR / variable-orifice) | no | yes | **(0,1)** |
| Structural | active (active mass driver) | yes | yes | **(1,1)** |
| Structural | **hybrid** (passive + active in parallel) | — | — | **spans (0,0)+(1,1)**; not a point |
| Nuclear | Category A (fully passive) | no | no | **(0,0)** |
| Nuclear | Cat B/C (stored energy, passive signal) | partial | partial | **(0,1)/(1,0) boundary** |
| Nuclear | Category D (active safety) | yes | yes | **(1,1)** |
| Façade | passive (static / thermochromic) | no | no | **(0,0)** |
| Façade | adaptive-no-actuator (buoyancy vent, sensor-gated) | no | yes | **(0,1)** |
| Façade | active (motorized louver) | yes | yes | **(1,1)** |

### B.3 The result G7 was missing: no portable ordinal ladder because each field linearises a different diagonal

Three structural facts, all visible only once the lattice is drawn:

1. **The field-independent "quasi-passive" and "semi-active" land in the *same* cell (0,1).** The
   task hypothesised they might occupy *different* positions; the honest finding is the opposite and
   is stronger — **two fields invented two different names for the exact same lattice cell** (no
   energy, needs signal) and never noticed, which is precisely the G7 phenomenon at the resolution of
   a single cell. (They differ only in *mechanism* — clutch vs. variable damping — not in lattice
   position.)
2. **The occupied cell `(1,0)` — injects energy, needs no signal — has essentially no standard name**
   in any of the four ladders (open-loop constant actuation: a fixed-power heater, a constant motor).
   Every field's ordinal ladder **skips it**, because a chain through B² can only pass through *one*
   of the two middle elements. Nuclear's A–D and structural's 4-rung ladder each pick a **different
   diagonal** through the square, which is why they cannot be aligned rung-for-rung.
3. **"Hybrid" is not a lattice element at all** — it is a *sum* of `(0,0)` and `(1,1)` components in
   parallel, i.e. a point in a richer product space, not a rung. Trying to insert it into a linear
   ladder (structural control puts it between semi-active and active) is exactly the category error
   of linearising a lattice.

> **This is the same lattice-lock failure as [[C12-pi-space-lattice]].** There, the "missing"
> Π-regime map was a projection artefact — a poset of crossovers flattened onto one axis loses the
> lock structure. Here, the "missing portable ladder" is a **width-2 lattice flattened onto a chain**:
> any total order must delete one of the two incomparable middle cells, and different fields delete
> different ones. A chain cannot represent an antichain of width 2. The non-portability is a
> **theorem about order dimension**, not a sociological accident of non-citation.

---

## The consistency check: does continuous `P` refine the lattice? Real systems, both representations

Every empirical figure is marked VERIFIED (with the fetch that produced it this session) or
UNVERIFIED (search-summary only, not fetched from primary).

| # | System | `P` (energy fraction) | Lattice cell | Supporting figure |
|---|---|---|---|---|
| 1 | **Passive-dynamic walker** (McGeer-type) | **≈ 1.0** — all propulsive energy from gravity, `W_active,inj = 0` | **(0,0)** | Walks stably down a shallow slope with *no actuation and no control*, energy lost to collision/friction recovered from gravity. UNVERIFIED (WebSearch summary this session: McGeer walker ~1.4° slope, ~0.4 m/s; "no actuation" is definitional) |
| 2 | **Unpowered ankle exoskeleton** (Collins 2015, clutch+spring) | **≈ 1.0** — "produces force without consuming any energy," no motor/battery, `W_active,inj = 0` | **(0,0)** — mechanical self-engaging clutch, **no controller** | ~**7%** metabolic-cost reduction; "mechanical clutch engages when the foot is on the ground"; operates "entirely without external energy sources." VERIFIED (phys.org fetch this session, reporting Nature 2015 / nature14288) |
| 3 | **Quasi-passive exoskeleton** (controllable clutch on elastic band) | **≈ 1.0 on the injection axis** — "cannot apply a non-conservative motive force"; delivered assistance is stored elastic energy | **(0,1)** — needs a signal to time the clutch | Assistance ratios (fraction of joint power delivered): hip **26.6%** avg / knee **9.3%** / ankle **12.6%** avg. VERIFIED (PMC7344163 fetch this session) |
| 4 | **Semi-active MR damper** (structural) | **≈ 1.0 on the injection axis** — purely dissipative, injects no mechanical energy; control current only sets viscosity | **(0,1)** — needs a signal (control current) | ~**58%** peak / ~**83%** RMS response reduction under semi-active (LQR) vs. ~**20%** in passive-off mode. UNVERIFIED (WebSearch summary this session; primary building-control paper not fetched) |
| 5 | **Active mass driver / powered exo** | **≈ 0** — delivered energy comes from an injected external source, `W_passive ≈ 0` relative to `W_active,inj` | **(1,1)** | definitional; no figure needed |

### What the check shows

- **`P` orders the cells it can see, correctly.** Along the `(0,0) → (0,1)/(1,0) → (1,1)` energy
  progression, `P` runs 1 → (1 on axis 1) → 0. Within the energy axis, `P` is a faithful continuous
  refinement: system 5 sits at `P≈0`, systems 1–4 at `P≈1`.
- **But `P` cannot separate `(0,0)` from `(0,1)`.** Systems 1, 2 (cell `(0,0)`) and systems 3, 4
  (cell `(0,1)`) **all have `P≈1`** — identical on the continuous axis, yet on opposite sides of the
  signal axis. The passive walker and the semi-active damper are **equal in `P` and different in
  kind.** This is the failure of `P` to refine the *second* dimension, demonstrated with real
  systems. A single number collapses a 2D object; the collapse is exactly along the axis control
  theory also cannot see (A.4).
- **Consistency verdict:** `P` refines the lattice **consistently but incompletely** — it is a
  monotone map `B² → [0,1]` that is injective on axis 1 and constant on axis 2. It never *contradicts*
  the ordinal structure (nothing with a higher cell gets a more-passive `P`), so it is a legitimate
  refinement; it is just not a *faithful* one, because the lattice has order-dimension 2 and `[0,1]`
  has dimension 1.

---

## Verdict

**NARROWS G7 — it does not close it, and it does not fail.**

- **Does `P` exist and is it well-defined across all four domains?** **Yes**, as the cycle-averaged
  **energy-delivery fraction** `P = W_passive/W_total` (Part A). It survives nonlinearity and
  non-additivity *because it meters energy flows separately instead of subtracting responses*, and it
  is portable *because energy is a common currency*. Its one honest caveat: it is defined per stated
  operating cycle, not context-free. The naive response-ratio `R_passive/R_total` is **not**
  well-defined (sign inversion, non-additivity); the energy form is. So the specific object G7 named
  — "the fraction of the response that survives when the actuation path is cut" — is buildable, but
  only after being **re-cast from response to energy**.
- **Is the ladder really a lattice, and on what axes?** **Yes — the Boolean lattice B²** on
  **(1) injects non-conservative energy?** and **(2) needs a control signal?** The two field-neutral
  middle rungs (quasi-passive, semi-active) are the same cell `(0,1)`; the cell `(1,0)` is real but
  unnamed; "hybrid" is a sum, not a rung. No total order can carry a width-2 lattice, which is
  **why no portable ordinal ladder exists** — the same linearise-a-lattice failure as
  [[C12-pi-space-lattice]], stated here as an order-dimension theorem rather than a citation gap.
- **Why "narrows" and not "closes":** `P` closes the **energy-passivity** question (a portable number
  now exists, with a mature control-theory twin, A.4) but is **blind to the signal axis**. Two systems
  with the same `P` can be in different lattice cells (walker vs. semi-active damper, both `P≈1`), so
  **cross-cell comparison along axis 2 remains meaningless** — exactly the "works only within a
  lattice cell" narrowing the brief anticipated. The full "how passive is it?" concept was always
  two-dimensional; one number can carry one dimension of it. To fully close G7 you need `P` **plus a
  second portable bit** for axis 2 (e.g. an information/actuation-bandwidth measure — the signal-side
  analogue, a natural next instrument in the sense of [[specification-instruments]]).

**Net:** the missing metric is real and buildable (energy fraction `P`); the missing *ladder* was
missing because it was a **2×2 lattice all along**; `P` refines one of its two axes faithfully and the
other not at all; and the control-theory "passivity" homograph is really the rigorous form of `P`'s
energy axis, agreeing where `P` sees and blind where `P` is blind.

See [[specification-instruments]]: conserved object = delivered work per cycle; enumeration = the two
Boolean bits; deliverable = the B² lattice with each field placed and a continuous refinement of its
energy axis. Ties to [[C12-pi-space-lattice]] through the identical lattice-lock / linearisation
failure, and to [[G7-how-passive]] as its narrowing.
