---
name: PENDING-log-C50
type: method
---

# Pending log entry for C50 (merge into `log.md`, newest-first, then delete this file)

Not linked from `00-index.md` by design: `log.md` is being edited by another agent this session,
so this entry is staged rather than written in place.

```
## [2026-09-05] negative control | D.2 fires: the audit halts at step 0(a) on (0.4 ± 3.0) µN, enumerating nothing

The reservoir audit's D.2 negative control was run for the first time
([[C50-reservoir-audit-d2-control]]). Input: a fabricated bench thruster reporting
F = 0.4 µN with 1σ = 3.0 µN at 50 W — 0.13σ, interval containing zero. Part C step 0(a)
fired `NO OBSERVABLE TO EXPLAIN` and the run stopped there: no F_req, no candidate list,
no aperture, no A, no Σ, no residual. Brief archived and hashed before dispatch at
`audits/blind-brief-c50-2026-09-05.md`, sha256
fae035f866bf1bbfa4136b6f3dc44c26d57a98743091b69174f451e44ac97ca6.

What is new: three null states are now observed at three distinct steps — 0(a) halt (D.2,
this run), 0(b) halt (D.3, C30), step-11 `NO RESIDUAL` after a full run (D.1, C46). Also
settled by reading the procedure: the conditional-run licence belongs to step 0(b) only, so
computing the photon-rocket bound P/c = 0.167 µN after a 0(a) halt is not permitted and is
recorded as a temptation, not an output.

What this does not establish: the brief labelled the case synthetic in its first line, so the
datum tests the wording of step 0(a), not the instrument's judgement; and the blind was
single-agent again. Next case named: Tajmar et al. 2021, doi:10.1007/s12567-021-00385-1
(Crossref, fetched 2026-09-05), briefed by a different agent on its reported thrusts and
uncertainties alone.
```
