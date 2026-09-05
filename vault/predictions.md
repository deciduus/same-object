---
name: predictions
type: method
---

# Predictions register

> **Append-only. Never edit or delete a recorded block — supersede it with a new dated block.**
> Each entry carries the date the prediction was *first made* (from `git log`, not from the date
> this file was created), the exact wording, the falsifier, and a `sha256` of the canonical
> prediction text so a later reader can verify the text has not drifted.

This file exists because `vault/log.md` carries a single date (2026-09-03) on all thirty of its
entries, including the "dated falsifiable prediction" — and a same-day record cannot demonstrate
that a prediction preceded its confirmation, which is the one thing a dated prediction is for
(`audits/03-method-epistemics.md`). Backlog A21 / C16.

## How to verify a hash

The hashed string is the fenced `canonical text` block of that entry, exactly as it appears
below, UTF-8, with no trailing newline. Reproduce with:

```
python -c "import hashlib,sys;print(hashlib.sha256(sys.stdin.read().rstrip('\n').encode()).hexdigest())" < text
```

---

## [2026-09-03] alpha (fine structure constant) resolves to systematics

- **Source note:** [[Q7-same-class-prediction]], anchored by [[fine-structure-discrepancy]].
- **First made:** **2026-09-03**, commit `a12703d` ("Add a question type: seven doors opened, and
  the catalogue's surviving conditional") — the commit that created
  `vault/questions/Q7-same-class-prediction.md`. `fine-structure-discrepancy.md` was already
  present at `1cae2ef` (2026-09-03) and gained the prediction cross-reference in the same series.
  Provenance: `git log --format='%h %ad %s' --date=short -- vault/questions/Q7-same-class-prediction.md vault/method/fine-structure-discrepancy.md`, run 2026-09-05.
- **Caveat, stated:** every commit in that log is dated 2026-09-03, so this register cannot
  establish anything finer than "before 2026-09-05" from repository evidence alone. The
  prediction is nonetheless unresolved as of 2026-09-05 (no third measurement), so it is still
  live and still falsifiable.
- **Status 2026-09-05:** OPEN. No third h/m recoil measurement has landed.
- **Falsifier:** a third measurement lands and the Cs–Rb disagreement resolves to a real physical
  effect rather than a measurement systematic. That kills the prediction and takes
  [[Q7-same-class-prediction]]'s conditional with it.

canonical text:

```
The fine structure constant discrepancy is same-class: caesium and rubidium recoil, both h/m atom interferometry, differing in implementation. Open at 5.4 sigma with no third measurement. It will resolve to systematics. Not new physics. And the suspected culprit - wavefront curvature - is already named.
```

`sha256` = `72fb580c91285dfe21561b2427ad077fa4a4edf65a5047dbe562e2ad9edbc29f`

---

## [2026-09-03] tenth-order QED coefficient resolves to a calculational error

- **Source note:** [[Q7-same-class-prediction]] ("a second live prediction"), row 3 of
  [[C16-same-class-catalogue]].
- **First made:** **2026-09-03**, commit `a12703d`, same commit as the alpha prediction. The
  sigma value was corrected from 4.8σ to ~5σ at `d5cebac` (2026-09-03); the *direction* of the
  prediction is unchanged.
- **Status 2026-09-05:** OPEN. Volkov's evaluation is billed as the first complete independent
  verification, which tilts toward AHKN as the erring side, but nothing is declared closed.
- **Falsifier:** both evaluations are confirmed correct and the disagreement survives, or the
  resolution is anything other than an error in one of the two Monte Carlo evaluations.

canonical text:

```
The tenth-order QED coefficient A_1^(10) disagreement (Aoyama-Hayakawa-Kinoshita-Nio vs Volkov, A_1 = 5.891(61), ~5 sigma) will resolve to a calculational error in one Monte Carlo evaluation. It is a cleaner test than alpha because no new physics is conceivable there.
```

`sha256` = `8f3f0da8896076996db2d44cb8822d5f7c09739b2b1e1d3fa1334ca3877c96dd`

---

## [2026-09-03] statocyte pooling: theta_min(16)/theta_min(48) = 1.73, not 3.00

- **Source note:** [[C4-inclination-sensing-limit]] §11.5–11.6.
- **First made:** on the date `C4-inclination-sensing-limit.md` entered the repository; every
  commit touching it is dated **2026-09-03** (same single-date limitation as above).
- **Status 2026-09-05:** OPEN — the experiment has not been run. This is the only entry in this
  register that is a *proposed* experiment rather than a wait-and-see on an existing dispute.
- **Falsifier:** stated inside the canonical text (three disjoint intervals, pre-registered).

canonical text:

```
Arabidopsis root-cap statocyte ablation, angle-threshold arm. Stimulate at fixed duration >= tau_memory = 13 min at theta = 5, 10, 20, 40, 90 degrees; fit rate = k sin(theta); extract theta_min(M). Predicted ratio theta_min(16)/theta_min(48): 1.73 under statistical pooling (M^-1/2, Berg-Purcell) versus 3.00 under deterministic linear summation (M^-1). Falsifiers stated in advance: ratio >= 2.5 falsifies pooling toward linear summation; ratio <= 1.25 falsifies pooling toward correlated noise or single-cell dominance; 1.5 <= ratio <= 2.0 means pooling survives.
```

`sha256` = `0e16b4423c016fbda883de3d099431d1ddac934a098aa7c0c8d26dca750913ce`

---

## [2026-09-05] pre-registered class assignments for C16's open and ambiguous rows

- **Source note:** [[C16-same-class-catalogue]]; requested by
  `audits/03-method-epistemics.md` (Q7 item: "pre-register the class assignment for the 7 open
  cases now, in the note, with a date, before their outcomes land") and backlog A21.
- **First made:** **2026-09-05** — today, by the agent executing backlog A15–A21, from the
  decision procedure written into [[C16-same-class-catalogue]] on the same date. The assignments
  were made from apparatus + observable + analysis pipeline **before consulting any outcome
  column**; two of them (rows 4 and 8) come out *against* the conditional's interest, which is
  the intended check on the procedure.
- **Status 2026-09-05:** RECORDED. Seven of the nine rows carry no outcome yet.
- **Falsifier:** any of the five CLASS-I rows resolving to real new physics falsifies
  [[Q7-same-class-prediction]]'s conditional outright. A CLASS-II row resolving to new physics
  weakens but does not kill it. A CLASS-III row resolving to new physics is irrelevant to it —
  which is exactly why the assignment had to be fixed in advance.

canonical text:

```
Pre-registered SAME-CLASS assignment for the 7 open and 4 ambiguous rows of C16-same-class-catalogue, produced by the decision procedure (apparatus, observable, analysis pipeline -> class id) written into C16 on 2026-09-05, assigned before any outcome was consulted. CLASS-I (all three match; the conditional is tested on these): row 1 alpha Cs-vs-Rb recoil; row 7 hydrogen 1S-3S MPQ-vs-LKB; row 21 W mass CDF II-vs-D0; row 22 DAMA-vs-COSINE-100/ANAIS-112 NaI(Tl) modulation; row 23 gallium GALLEX/SAGE/BEST. CLASS-II (apparatus and observable match, analysis pipeline differs; reported separately): row 3 tenth-order QED AHKN-vs-Volkov; row 24 Hubble Wars Sandage-vs-de Vaucouleurs ladders. CLASS-III (apparatus or observable differs; NOT same-class, excluded from the conditional): row 4 HUST G time-of-swing vs angular-acceleration-feedback (observable and dynamical model both differ); row 8 electronic-hydrogen proton radius across 2S-4P / 1S-3S / 2S-2P (different transitions are different observables). Consequence recorded in advance: row 8 is a CLOSED case, so if this procedure is adopted the closed same-class tally falls from 17 to 16 (15 SYSTEMATICS + 1 FLUCTUATION), and the Clopper-Pearson one-sided 95 percent upper bound on P(new physics | same class) rises from 0.16 to 1 - 0.05^(1/16) = 0.17.
```

`sha256` = `5c4e2d7543129a33b66b3a362c4fa1b3f8326ce9d65e78ff447c3dc6af2e2caf`

---

## [2026-09-05] full blind re-application of the C16 class procedure — supersedes the partial pass above

- **Source note:** [[C16-same-class-catalogue]], §"The blind re-application to all 24 rows (A20)";
  backlog A20.
- **Relation to the previous block:** the 2026-09-05 pre-registration above recorded a *partial*
  pass (9 rows) and predicted, in advance, that adopting the procedure would drop the closed tally
  17 → 16 and loosen the bound 0.16 → 0.17. **That consequence was understated.** The full sweep
  found 11 changed assignments, not 2, and the strict tally falls to 8 closed with a bound of
  0.31. Per this file's append-only rule the earlier block is left exactly as written; this block
  supersedes its numeric consequence, not its assignments (all 9 stand).
- **Status 2026-09-05:** RECORDED.
- **Falsifier:** an independent analyst, given only the apparatus / observable / pipeline columns
  and never the outcomes, produces materially different grades. That would show the procedure is
  not analyst-independent and the churn number is unreliable.

canonical text:

```
Blind re-application of the C16 decision procedure (apparatus, observable, analysis pipeline -> CLASS-I / CLASS-II / CLASS-III) to all 24 rows of C16-same-class-catalogue plus the three previously excluded candidates, run 2026-09-05. Result: 11 of 24 assignments change. Rows 4, 8 and 19 become CLASS-III (different apparatus or observable). Rows 2, 3, 5, 6, 9, 14, 20 and 24 become CLASS-II (same apparatus and observable, different analysis pipeline). The three excluded candidates - solar neutrinos, lattice-versus-dispersive muon g-2, gravitational-redshift clocks - remain excluded. Strict CLASS-I tally: 8 closed (7 SYSTEMATICS + 1 FLUCTUATION), 5 open, 0 NEW-PHYSICS; Clopper-Pearson one-sided 95 percent upper bound on P(new physics | same class) = 1 - 0.05^(1/8) = 0.31. CLASS-I plus CLASS-II: 15 closed, 0 NEW-PHYSICS, bound 1 - 0.05^(1/15) = 0.18. No counterexample appears at any grade. Limitation: run by the same agent that wrote the procedure, on the same day, with the outcome column visible on the page though not consulted for the apparatus/observable/pipeline reading - blind-in-intent, not an independent replication.
```

`sha256` = `dd517f0d88f870c1934b200c0aa633978cd753f3ee0863bda6a810f6fa767afe`
