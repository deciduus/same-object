---
name: C50-reservoir-audit-d2-control
type: computed
exit: specification
---

# D.2 run: the audit halts at step 0(a) on an observable inside its own error bar

> **`NO OBSERVABLE TO EXPLAIN`, fired at step 0(a), with nothing enumerated.** On a fabricated
> bench thruster reporting `F = (0.4 ± 3.0) µN at 50 W`, the significance line is
> `0.4/3.0 = 0.13σ`; the interval `[−2.6, +3.4] µN` contains zero; the procedure's step 0(a)
> says *halt and enumerate nothing*, and the run halted there. **No `F_req`, no candidate list,
> no aperture, no `A`, no `Σ`, no residual.** The case was **labelled synthetic** in the first
> line of the archived brief, so this datum tests the *wording of step 0(a)* — that the halt is
> reachable, unambiguous and correctly placed ahead of step 1 — and **not** the instrument's
> judgement on an unlabelled input. Three null states are now observed, and they fire at three
> different places.

Brief archived and hashed before the run: `audits/blind-brief-c50-2026-09-05.md`, sha256
`fae035f866bf1bbfa4136b6f3dc44c26d57a98743091b69174f451e44ac97ca6` (of the five-line brief plus
its `SYNTHETIC CONTROL` header, before the hash line was appended). See [[reservoir-audit]]
Part D, [[C46-reservoir-audit-negative-control]], [[C30-venus-phosphine-audit]],
[[C11-flyby-reservoir-audit]].

## 1. The input

Fabricated, per the D.2 design in [[reservoir-audit]]: *"a thruster ... reporting a thrust whose
central value is smaller than its own stated uncertainty — e.g. `F = (0.4 ± 3.0) µN at 50 W`."*
**This is not a device. No number below is a measurement of anything in the world.** Brief case
line, verbatim: mean thrust `F = 0.4 µN`, `1σ = 3.0 µN`, 40 runs, 50 W input, torsion balance,
vacuum `10⁻⁵ Pa`, no drift correction reported.

Methods entry point named in the brief: Tajmar, Kößling, Weikert & Monette, *The SpaceDrive
project — Thrust balance development and new measurements of the Mach-Effect and EMDrive
Thrusters*, *Acta Astronautica*. **VERIFIED** — Crossref
`api.crossref.org/works?query.bibliographic=...`, fetched 2026-09-05: DOI
`10.1016/j.actaastro.2019.05.020`, that title, container *Acta Astronautica*, issued 2019-08.
It was **not read**: the run halted before any source was needed.

## 2. The run

| Step | Ran? | Result |
|---|---|---|
| 0(a) significance | **ran** | `0.4 ± 3.0 µN` → `0.13σ`; interval contains zero → **HALT, `NO OBSERVABLE TO EXPLAIN`** |
| 0(b) reductions table | not reached | one reduction stated; moot after 0(a) |
| 1–12 | **not run** | 0(a) directs: *"halt ... and enumerate nothing"* |

**The temptation, recorded because the control exists to record it.** The obvious next move is
one line: the photon-rocket ceiling `P/c = 50/2.998×10⁸ = 1.67×10⁻⁷ N = 0.167 µN`, which lies
inside the reported interval, so "the electromagnetic field is not even excluded." **That is
steps 3, 6 and 7, and it is not allowed here.** Step 0(a) permits no conditional run: the
conditional-run licence in Part C step 0 belongs to **0(b)** alone (*"A conditional run
downstream of this halt may claim calibration ..."*), and D.2 states the requirement without a
conditional escape — *"and **no candidate enumeration performed at all**."* The asymmetry is
correct. A 0(b) halt has a real observable whose value is disputed, so a ledger run against a
published enumeration still says something about the instrument; a 0(a) halt has **no number**,
and every downstream quantity would be a specification for a coupling that was never reported.
The `0.167 µN` above is therefore quoted as a *temptation*, not as an audit output, and does not
enter any standing.

## 3. Three ways this instrument returns nothing

| Output | Fires at | Ran before it fires | Case | What it says |
|---|---|---|---|---|
| `NO OBSERVABLE TO EXPLAIN` (D.2) | **step 0(a) halt** | nothing | **this note** (synthetic) | the central value is inside its own error bar; there is no observable |
| `NO AGREED OBSERVABLE` (D.3) | **step 0(b) halt** | the reductions table only | [[C30-venus-phosphine-audit]] | the central value is a function of the reduction pipeline; a conditional run is permitted and must be written as one |
| `NO RESIDUAL` (D.1) | **step 11, after all steps** | steps 0–10 in full | [[C46-reservoir-audit-negative-control]] | the reservoirs considered supply the coupling; the books balance |

The three are not degrees of the same answer. The two halts say *there is nothing to audit* and
differ in **why the number fails** — width of one interval vs disagreement between several.
`NO RESIDUAL` says *the audit ran and found the ledger closed*. Only the third is a statement
about a device; the first two are statements about a report.

**Proposed Part D text** (for the section-D table, to replace the D.4 table's first row and add
a column) is given in §5.

## 4. Honesty

- **Labelled synthetic.** The brief's first line says the report is fabricated. The agent
  therefore knew it was a control — but not **which** control, nor which of the five states to
  return; D.1, D.3 and a plain `SURVIVES` were all available shapes. So this tests whether step
  0(a) is **worded** such that a competent reader lands on it and stops: it is, and the halt was
  unambiguous. It does **not** test judgement, and it is a weaker datum than C46 on the axis
  C46 was weak on for a different reason: C46's case was real but textbook; this case is not
  real at all.
- **Single-agent blind, again.** The brief was written by the agent that ran it, exactly the
  contamination D.3a asks to remove. Both negative-control data now carry this.
- **The halt was cheap.** `0.13σ` is not a marginal call. A case at `2.5σ` — where the
  significance line has to be *argued* — would test step 0(a) far harder, and no such case has
  been run.
- **What an unlabelled D.2 needs.** A **real, published, null-result thrust paper** briefed
  without the synthetic flag, so the agent cannot infer from the labelling that a null is
  wanted. Named next case: **Tajmar et al. 2021, TU Dresden**, *High-accuracy thrust
  measurements of the EMDrive and elimination of false-positive effects*, *CEAS Space Journal*
  — **VERIFIED** DOI `10.1007/s12567-021-00385-1`, Crossref, fetched 2026-09-05: that title,
  container *CEAS Space Journal*, issued 2021-07-27. Brief it with the reported thrusts and
  their uncertainties **only**, no abstract and no conclusion sentence, per the D.3a template,
  and have a **different agent** write the brief.

## 5. Proposed Part D text

To be inserted by whoever next edits [[reservoir-audit]] (this note does not edit it):

- **D.2 status line** — change `D.2 unrun` in the Part D heading to
  `D.2 RUN 2026-09-05, labelled-synthetic input`.
- **D.4 table** — add a column `Ran before firing` with the three values `nothing` /
  `the reductions table only` / `steps 0–10 in full`, and change the D.2 row's `Case` cell from
  `unrun` to `[[C50-reservoir-audit-d2-control]] (synthetic)`.
- **New sentence after the table**: *"D.2 fired at step 0(a) on the first input built for it,
  with nothing enumerated — but the input was labelled synthetic, so it validates the wording of
  step 0(a), not the instrument's judgement. The unlabelled replacement is named in
  [[C50-reservoir-audit-d2-control]] §4: Tajmar et al. 2021 (doi:10.1007/s12567-021-00385-1),
  briefed on its reported thrusts and uncertainties alone."*
- **Standing section** — `D.2 remains unrun` becomes `D.2 has one labelled-synthetic datum`.
