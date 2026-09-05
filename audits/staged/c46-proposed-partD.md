---
name: PENDING-log-C46
type: method
---

# PENDING edits from P-092 (C46, reservoir-audit negative control)

Three edits this agent was not permitted to make, staged verbatim for whoever holds the files.
Delete this note once they are applied. See [[C46-reservoir-audit-negative-control]].

## 1. For `vault/log.md`, newest-first at the top

```
## [2026-09-05] negative control | The reservoir audit CAN return nothing: blind D.1 run on a Betz-calibrated turbine returns NO RESIDUAL at step 11, a third null state distinct from both step-0 halts

First negative control of [[reservoir-audit]] run against a brief archived and hashed before
the run (`audits/blind-brief-c46-2026-09-05.md`, sha256 5e39ef6f84ed2c6eec4b17c434a6db7717683744
df1bf099983c36c0ca922308; five-line D.3a template, no verdict word, no D-class label). Case: a
90 m rotor reporting 2.0 MW at 11 m/s, rho = 1.225, stated C_p = 0.44. All thirteen steps ran,
none skipped. P_avail = 5.1863 MW (script `vault/_scripts/c46_betz.py`), Betz ceiling 3.0734 MW,
required C_p = 0.3856 = 0.651 of Betz, A = 0.386 at the swept disc (0.193 at 2x aperture, 0.771
at 0.5x). Ambient flow SURVIVES with a required property the stated C_p already supplies; the
gravitational, geomagnetic and thermal candidates are NOT FORMABLE (Delta u = 0 or undefined);
no second reservoir demanded. The -0.282 MW aerodynamic-to-electrical gap is a drivetrain
efficiency of 0.876, already in the published loss budget. What was wrong: Part D assumed the
audit's null output would be a halt. It is not — `NO RESIDUAL` fires at step 11 after a complete
run, and is a distinct third state from D.2's `NO OBSERVABLE TO EXPLAIN` (step-0(a) halt) and
D.3's `NO AGREED OBSERVABLE` (step-0(b) halt, C30). Two caveats logged, not buried: the blind is
single-agent (the brief was written by the agent that ran it — weaker than D.3a's two-agent
design, stronger than C30's pre-announced halt), and the case is textbook and was recognised on
sight. New failure mode F9: for a generator, F_req = P_useful/v at step 2 forces Sigma = 1 at
step 8, so the energy leg is not merely weak (F1) but a tautology that can never fire.
```

## 2. For `vault/00-index.md`, in the `## Computed` list

```
- [[C46-reservoir-audit-negative-control]] — **the audit's first negative control, run blind against a hashed brief.** A Betz-calibrated 90 m turbine: `P_avail = 5.186 MW`, Betz ceiling `3.073 MW`, required `C_p = 0.3856` (0.651 of Betz), `A = 0.386` at the swept disc and `0.193 / 0.771` at 2× / 0.5× aperture. The ambient flow `SURVIVES` with a property the stated `C_p = 0.44` already supplies; **no second reservoir demanded, no residual**. Answers Part D: the audit *can* return nothing — but `NO RESIDUAL` fires at **step 11 after a full run**, a third null state distinct from both step-0 halts. Blind is single-agent and the case is textbook, so the datum is weaker than D.3a asks for. New F9: on generator-form inputs `Σ = 1` identically
```

## 3. Proposed one-paragraph update for `reservoir-audit.md` Part D (PROPOSED ONLY — not applied)

To be inserted in Part D, after D.1's "What would count as a failure" paragraph:

```
**D.1 — RUN, 2026-09-05: [[C46-reservoir-audit-negative-control]].** A 90 m rotor at 11 m/s
reporting 2.0 MW with a stated `C_p = 0.44`, briefed on the D.3a five-line template archived and
hashed before dispatch (`audits/blind-brief-c46-2026-09-05.md`). All three D.1 conditions are
met: `A = 0.386 ≤ 1` at the swept disc and consistent with the accounted value (`0.193 / 0.771`
at 2× / 0.5× aperture), the step-11 union is non-empty and already occupied by the stated `C_p`,
and no second reservoir is demanded. **The instrument can return nothing — but not in the shape
this section predicted.** Part D assumed a null would be a halt; the D.1 null is `NO RESIDUAL`,
fired at **step 11 after all thirteen steps ran**, and it is a third state distinct from D.2's
`NO OBSERVABLE TO EXPLAIN` and D.3's `NO AGREED OBSERVABLE`, which are both step-0 refusals to
audit. It should be named as a state alongside step 10's four. Two things the datum does not
establish, both stated in C46 §4: the blind was **single-agent** — the brief was written by the
agent that ran it, which removes pre-announcement but not recognition — and the case is
**textbook**, so it exercises the arithmetic path rather than the judgement. The next D.1-class
case must be one the agent cannot recognise as resolved: a published Betz-exceeding
diffuser-augmented turbine claim (`C_p` normalised to throat rather than exit area) or a
low-head hydro efficiency claim above its ceiling, briefed by a different agent. C46 also
returns **F9**: for a generator, `F_req = P_useful/v` at step 2 makes `Σ = 1` at step 8
identically, so the energy leg is a tautology, not merely weak.
```
