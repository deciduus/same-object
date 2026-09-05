---
name: PENDING-log-C49
type: method
---

# PENDING `log.md` entry from the C49 Mars-methane blind run (P-089, Track C)

One entry this agent was not permitted to write into `vault/log.md` directly. Staged verbatim for
whoever holds that file; it belongs at the top, newest-first. **Delete this note once applied.**
Deliberately not wikilinked from `00-index.md`; the lint reachability check emits a warning, not
an error.

Files written in this pass: `audits/blind-brief-c49-2026-09-05.md` (new),
`vault/computed/C49-mars-methane-audit.md` (new), `vault/_scripts/c49_mars.py` (new), one line in
`vault/00-index.md`. `vault/method/reservoir-audit.md` was **read but not edited** — it is held by
another agent — so C49 §7's proposed F10, the `EXCHANGE REQUIRED` state, the `UNREPLICABLE
OBSERVABLE` step-0 condition and the `A >> 1e4` step-1 diagnostic are **proposals only** and are
not yet in the method note.

---

## For `vault/log.md`

```
## [2026-09-05] blind negative control | Mars methane has no single observable: step 0 returns four different verdicts, and the audit's one reproducible exclusion is a SINK at A = 319

[[C49-mars-methane-audit]], P-089 Track C, run against a brief written and hashed before the run
(`audits/blind-brief-c49-2026-09-05.md`, sha256 34a7d8ee823c28b8c776a56d9bfeca62fae177650f8e9059
082274efaff2c424) that names no verdict, no halt and no D-class. What was assumed: that a case
carries one observable and step 0 returns one state. It does not. "Methane on Mars" is four
observables with four standings: the globally mixed background is TGO's <0.05 ppbv, an interval
containing zero, so 0(a) halts with NO OBSERVABLE TO EXPLAIN; the ground-based plumes are
Mumma 2009's 45 ppbv against Zahnle, Freedman & Catling 2011's re-reduction of the same spectra
to a telluric-subtraction artefact, so 0(b) halts with NO AGREED OBSERVABLE — F8's trigger on a
second case after Venus; the 2019 21 ppbv spike read globally needs 2.27e8 t/yr of removal
(tau = 7.1 h, A = 1.9e7) and is NOT FORMABLE as a global quantity; and only the Gale
near-surface seasonal observable (0.41 +/- 0.16 ppbv, 2.56 sigma, cycling 0.24-0.65) survives,
conditionally, on a condition Part C's step-0 table has no row for — one instrument, one team, no
independent reduction of the TLS records has ever been published, so 0(b) cannot be run at all.
What it is now, on that observable: burden 3,592 t (Mars atmosphere 2.367e16 kg = 5.461e17 mol),
steady-state maintenance 11.97 t/yr against a 300-yr photochemical lifetime, but the seasonal
amplitude needs 3,820 t/yr in each direction and an effective residence time of 0.944 yr —
318x shorter than photochemistry — derived from the amplitude and the Mars year alone, with no
chemistry, and matching Lefevre & Forget 2009's "shorter than 1 year" independently. Gas-phase
photochemistry is RULED OUT at A = 319 and survives the 2x aperture row. Every SOURCE passes:
UV degradation of meteoritic/IDP organics at A = 0.164 for the background (over-sufficient 6x)
but RULED OUT at A = 52.3 for the seasonal amplitude, serpentinisation microseepage at
A = 0.025 on Oehler & Etiope 2017's own 30,000 km2 Nili Fossae aperture and 5 t/km2/yr,
clathrate / volcanic / biological all NOT TESTED for want of a published flux bound. The residual
is therefore not a source: a surface reservoir exchanging CH4 in BOTH directions at >= 3,820 t/yr
per phase, season-locked, 0.072 mg/m2/day planet-wide — two to three orders BELOW terrestrial
microseepage, so capacity is not the problem and the sign alternation is. Calibration against
Yung et al. 2018 (full-text-read, Europe PMC PMC6205098): five routes, two matches (tau_eff, the
IDP 5-6x over-prediction), two tautological rows that are Yung's own numbers re-divided (the
C30 lesson, applied to this note's own margins), and one located divergence — Yung's 75,000 t/yr
for the ~7 ppbv spike against this note's 7.36e5 t/yr, a factor of 9.8 that is entirely the
local-vs-global aperture, F3 made checkable. New output shape, proposed to the method note but
not yet written into it: on a mass budget the SOURCE leg's aperture is free and the SINK leg's is
fixed by the observable (P_avail = burden/tau), so source rows carry no information and only sink
rows are reproducible between analysts — proposed as F10, with source rows reported
NOT DISCRIMINATED rather than SURVIVES. Also proposed: a sixth step-10 state EXCHANGE REQUIRED
for periodic observables whose residual is two-signed; a fourth step-0 condition
UNREPLICABLE OBSERVABLE; and a step-1 diagnostic that A >> 1e4 reports a mis-specified observable
rather than an excluded reservoir. Honesty: the blind is single-agent, the case is recognisable,
the case-line numbers are the brief's rather than a fetch, and Moores 2019 and Webster 2021 — the
two papers the whole step-0 verdict turns on — are Crossref-verified but NOT full-text-read.
Arithmetic: `vault/_scripts/c49_mars.py`.
```
