---
name: C46-reservoir-audit-negative-control
type: computed
exit: specification
---

# The reservoir audit's first blind negative control: a Betz-calibrated wind turbine

> **The audit ran to completion and returned no residual — it did not halt and it did not stop
> early: it reached step 11 and the step-11 union came back *already occupied*.** On a 90 m
> rotor at 11 m/s, `P_avail = 5.186 MW`, the Betz ceiling is `3.073 MW`, and the reported
> 2.0 MW electrical needs `C_p = 0.3856` — `0.651` of Betz, `A = 0.386` at the swept disc and
> `0.193` / `0.771` at 2× / 0.5× aperture. The ambient flow `SURVIVES` with a required property
> the stated `C_p = 0.44` already supplies; **no second reservoir is demanded**, and the
> `−0.282 MW` gap between aerodynamic and electrical power is a drivetrain efficiency of
> `0.876`, a line the published loss budget already carries. **So Part D's central question
> answers yes — but "nothing" here is the D.1 state (`NO RESIDUAL`), a third output distinct
> from D.2's `NO OBSERVABLE TO EXPLAIN` and D.3's `NO AGREED OBSERVABLE`, both of which are
> step-0 halts and neither of which fired.** The blind is single-agent — the brief was written
> by the agent that ran it — so this is weaker than the two-agent blind D.3a specifies.

Brief archived before the run at `audits/blind-brief-c46-2026-09-05.md`, sha256
`5e39ef6f84ed2c6eec4b17c434a6db7717683744df1bf099983c36c0ca922308`. Arithmetic:
`vault/_scripts/c46_betz.py`. See [[reservoir-audit]] (Part D), [[C11-flyby-reservoir-audit]],
[[C30-venus-phosphine-audit]].

## 1. Sources

- Betz, *The Maximum of the Theoretically Possible Exploitation of Wind by Means of a Wind
  Motor*, Wind Engineering **37**(4):441–446 — the 2013 English reprint of the 1920
  *Zeitschrift für das gesamte Turbinenwesen* paper. **VERIFIED** — Crossref
  `api.crossref.org/works/10.1260/0309-524X.37.4.441`, fetched 2026-09-05: that title,
  container `Wind Engineering`, volume 37, issue 4, pages 441-446, published-print 2013-08,
  publisher SAGE Publications.
- Burton et al., *Wind Energy Handbook*, Wiley. **VERIFIED** — Crossref
  `api.crossref.org/works/10.1002/9781119992714`, fetched 2026-09-05: title *Wind Energy
  Handbook*, publisher Wiley, created 2011-05-06 (the 2nd edition).

## 2. The run, step by step

**Step 0(a) — significance. RUN.** The brief states no uncertainty on any of the four numbers.
Rather than halt on a missing interval, the run assigned one and said so: the manufacturer's
`C_p` carries an implicit tolerance, taken as **±3% relative** (`0.44 ± 0.013`) because neither
source states one. The observable — 2.0 MW — is not an excess over a background; it is the
device's entire output, and no metering error puts it near zero. Interval does not contain zero
→ **proceed**. *This is a weakness the control surfaced: step 0(a) is written for an anomaly (a
small excess with an error bar) and has no clean reading for a primary observable. The run
supplied the missing tolerance rather than refusing.*

**Step 0(b) — reductions table. RUN.**

| Row | Team / pipeline | Central value | Significance | Shares raw data with |
|---|---|---|---|---|
| 1 | manufacturer power curve at `U = 11 m/s` | `P_e = 2.0 MW`, `C_p = 0.44` | none stated | — |

One reduction, not several. The set does not span "detected" and "not detected", so the D.3
trigger does not fire. **Proceed — noting that a single-row table is the minimum that can pass,
and that a one-vendor row is exactly the single-group claim METHOD §5 resolves against the
claimant.** Flagged, not halted.

**Step 1 — observable in units. RUN.** `P_e = 2.0 MW` at `U = 11 m/s`, `ρ = 1.225 kg/m³`,
`D = 90 m`. A generator, not a thruster.

**Step 2 — required coupling. RUN.** Generator form: `F_req = P_useful / v = 2.0e6 / 11 =
1.818e5 N`.

**Step 3 — enumerate candidates. RUN.** From the standing list: **(i)** ambient fluid at a bulk
velocity — the wind; **(ii)** a second fluid or solid at a different bulk velocity — tower and
ground at `u = 0`; **(iii)** a static field — gravitational and geomagnetic; **(iv)** thermal —
the ambient air's internal energy; **(v)** the laboratory frame itself. Here (ii) and (v) are
the same object (tower footing → planet).

**Step 4 — name a Δu for each. RUN.**

| Candidate | `Δu` | State |
|---|---|---|
| Ambient flow (wind) against tower/ground | `11 − 0 = 11 m/s` | formable → tested |
| Earth's gravitational field | `0`, static in the lab frame | `NOT FORMABLE` |
| Geomagnetic field | `0`, corotating with the tower | `NOT FORMABLE` |
| Ambient thermal energy | no bulk velocity; a temperature, not a `Δu` | `NOT FORMABLE` |

The wind/ground pair is one reservoir *pair*, exactly as Part A.4's Blackbird row. Naming the
air alone would give `Δu = 11 − v_rotor` and the sign leg would misfire; it was named as a pair
from the start.

**Step 5 — aperture, as a named row. RUN.** Nominal aperture = the **swept disc**,
`A_area = π(45)² = 6361.7 m²`, the physical feature being the rotor circle. For a flow
`P_avail = ½ρA_area·U³` is **linear in area**, so the sensitivity rows are `A/2` and `2A`.

| Aperture | Area (m²) | `P_avail` (MW) | `A` |
|---|---|---|---|
| 2× | 12,723.5 | 10.373 | **0.193** |
| nominal | 6,361.7 | 5.186 | **0.386** |
| 0.5× | 3,180.9 | 2.593 | **0.771** |

The direction is untouched at every row: the flow is never ruled out.

**Step 6 — P_avail. RUN.** `½ × 1.225 × 6361.7 × 11³ = 5.1863 MW`; Betz ceiling
`(16/27) × 5.1863 = 3.0734 MW`.

**Step 7 — availability leg. RUN.** `A = (F_req·Δu)/P_avail = (1.818e5 × 11)/5.186e6 =
**0.3856** ≤ 1` → the ambient flow **`SURVIVES`**. Required property: a power coefficient
`C_p ≥ 0.3856`, i.e. `0.651` of Betz.

**Step 8 — energy leg. RUN, and it is vacuous.** `Σ = P_useful/(F·Δu) = 1.0000` **identically**,
because step 2 defined `F_req = P_useful/v` and step 8 divides it straight back out. For a
generator the energy leg is not merely weak (F1) — it is a tautology and can never fire.
Recorded as F9 below.

**Step 9 — sign leg. RUN.** `Δu = +11 m/s > 0`. No inversion; the two-reservoir naming at step 4
is what kept it positive.

**Step 10 — states.** Ambient flow **`SURVIVES`**, required `C_p ≥ 0.3856`. Gravitational field,
geomagnetic field, ambient thermal: **`NOT FORMABLE`**. Nothing `RULED OUT`; nothing `NOT TESTED`.

**Step 11 — residual specification. RUN.** The union of surviving required properties is
`{C_p ≥ 0.3856}`. The stated `C_p = 0.44 ± 0.013` **already satisfies it**, with margin
`0.44/0.3856 = 1.14` and the whole tolerance band above the requirement. **Union non-empty and
already occupied → no residual.** The `2.000 − 2.282 = −0.282 MW` difference between aerodynamic
and electrical power has the *sign of a loss*, not of an excess: implied drivetrain efficiency
`0.8764`, ordinary for a geared 2 MW machine and inside any published loss budget.

**Step 12 — prefix. RUN.** *Of the reservoirs considered*, the ambient flow supplies the required
coupling and no other is needed.

**Steps skipped: none.** Every step 0 through 12 was run.

## 3. Did the instrument return nothing on its own?

**D.1's three conditions are all met.** (1) `A = 0.386 ≤ 1` at the swept disc, and the required
`C_p` is not merely under 1 but consistent with the accounted value — the ±3% band on the stated
`C_p` sits wholly above the requirement. (2) The step-11 union is non-empty and already occupied.
(3) **No second reservoir was demanded at any step.** None of D.1's failure signatures appeared:
the aperture was fixed before `A` was computed and never retuned; there was no `1 < A < 2`
exclusion of the reservoir demonstrably doing the work; the only residual-shaped quantity is a
loss the published budget covers.

**Did it manufacture a specification?** It emitted one — `C_p ≥ 0.3856` — but that is D.1's
*correct* null output, not an artefact: it is a property of the reservoir already doing the work,
and it is satisfied on arrival. The instrument did **not** invent an additional partner, which is
the failure that would have discredited Pioneer's 3.2% and the EmDrive's 2.4 mg/s.

**Where it stopped: nowhere.** It ran every step. That is the finding that matters for Part D's
taxonomy — there are now **three distinct "nothing" outputs, and only two of them are halts**:

| Output | Fires at | Case | What it says |
|---|---|---|---|
| `NO OBSERVABLE TO EXPLAIN` (D.2) | step 0(a) halt | unrun (fabricated thruster) | the observable is inside its own error bar |
| `NO AGREED OBSERVABLE` (D.3) | step 0(b) halt | [[C30-venus-phosphine-audit]] | the central value is a function of the pipeline |
| **`NO RESIDUAL` (D.1)** | **step 11, after a full run** | **this note** | **the reservoir considered supplies the coupling; nothing is left over** |

A halt says *there is nothing to audit*. `NO RESIDUAL` says *the audit ran and the books
balance*. The first two are refusals; only the third is an audit that found nothing. Part D does
not currently name `NO RESIDUAL` as a state alongside step 10's four (five with D.2's), and it
should.

**So: can the audit return nothing? Yes — on a fully accounted device, unprompted, in the D.1
sense.** It is a weaker yes than Part D hoped for, for the reasons below.

## 4. What this control does not establish

- **The blind is single-agent.** The same agent wrote the brief and ran it. D.3a asks for an
  agent not told whether the case is resolved; an agent writing its own brief knows. This
  removes the *pre-announcement* contamination that voided D.3 — the brief carries no verdict
  word and no D-class label, and its sha256 fixes that fact before the run — but it cannot
  remove agent knowledge. **Weaker than a two-agent blind; stronger than C30.**
- **The case is textbook.** A Betz-calibrated turbine is the worked example of the Wind Energy
  Handbook. The agent recognised it on sight. A control the agent recognises tests the
  instrument's *arithmetic path*, not its *judgement*.
- **Step 0(a) had to be improvised.** The brief gave no uncertainty and the run assigned ±3%.
  A mandatory first step that can be satisfied by inventing the missing input is not yet a hard
  gate; on a real contested case that improvisation is where a bias would enter.
- **F9, new from this run — for a generator the energy leg is an identity.** `F_req = P_useful/v`
  at step 2 forces `Σ = 1` at step 8. F1 says Σ rarely fires; on generator-form inputs it
  *cannot*, and every Part A row using the generator form should be re-read accordingly.

**The next D.1-class case must not be textbook.** Proposal: a *published* anomalous-yield flow
claim later explained by ordinary bookkeeping. Strongest candidates: **(a)** a Betz-exceeding
shrouded / diffuser-augmented wind turbine, where `C_p > 16/27` is reported because the
coefficient is normalised to the throat area rather than the diffuser exit area — the correct
output is `NO RESIDUAL` once step 5's aperture row is written honestly, so the audit's own
aperture discipline is what decides it; **(b)** a low-head hydro or vortex-turbine efficiency
claim above the theoretical ceiling, later traced to an overstated head or an unmetered bypass
flow. In both the naive reading shows an excess and the honest run must return nothing — the
property this control lacked. The brief for either must be written by a **different agent**, per
D.3a.
