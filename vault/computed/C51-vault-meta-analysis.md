---
name: C51-vault-meta-analysis
type: computed
exit: computation
extends-to: [none]
next-step-cost: S
---

# What predicts whether this vault's own claims survived

> **Nothing about the *subject* of a claim predicts its survival; the only thing that does is
> *when it was made*.** Across **82 graded claims** (87 coded, 5 open questions carry no graded
> claim), overall survival is **26/82 = 0.317**. Claims produced during the 2026-09-05 audit
> rounds survive at **17/35 = 0.486** against **9/47 = 0.191** for the 2026-09-03 vault
> (Fisher two-sided **p = 0.0078**) — the **opposite** of the pre-registered direction. Of the
> four pre-registered hypotheses, **H1, H2 and H3 fail and H4 is direction-only**: correlations
> are the one claim kind that never survived (**0/6**), every scale-mismatched data join died
> (**0/3**) while both same-scale joins lived (**2/2**), and running an adversarial pass changed
> a claim's survival rate by **1.2 points** (0.312 vs 0.324) — the audits reshaped claims far more
> often than they killed them.

Pre-registered in `audits/blind-brief-c51-2026-09-05.md`, sha256
`8844d375b302b987d7bc83ebbb8f2e4157f26df7f93fd7bcdc6517ac697d786a`, hashed **before any outcome
column was read or coded**. Dataset: `_scripts/c51_data/claims.csv` (87 rows, one per claim,
each with a `source_line` naming where the outcome was read). Re-runnable:
`python _scripts/c51_meta.py` from `vault/`.

## 1. The unit and the outcome

One claim = one headline sentence: the `>` callout of a computed note, the `**STANDING:` line of a
gap note, or the headline answer of a question note. ID set fixed in the brief: C1–C22 and C25–C50
(48), G1–G37 as they exist (29), Q1–Q10 (10) = **87**.

Outcome vocabulary is the vault's own: `SURVIVED` (novelty-audit **NOVEL**, or `standing: live`
with the claim intact), `NARROWED`, `WITHDRAWN` (includes `overturned`), `PRIOR_ART` (the
REPACKAGED / REDISCOVERED / LOCATED grades), `ungraded`.

| outcome | n |
|---|---|
| SURVIVED | 26 |
| NARROWED | 26 |
| PRIOR_ART | 19 |
| WITHDRAWN | 11 |
| ungraded | 5 |

Two coding rules were needed that the brief did not fix and that are recorded here rather than
buried. **(i) Precedence** when a claim carries both a novelty grade and a standing change:
WITHDRAWN > PRIOR_ART > NARROWED > SURVIVED. **(ii) Authority.** For gap notes the
`standing` field wins over the novelty audit's LOCATED grade, per `CLAUDE.md` — the vault note and
the index are canonical for standings, and LOCATED is a novelty grade, not a standing. This is why
`PRIOR_ART` is almost entirely a computed-note outcome.

## 2. The four pre-registered tests

**H1 — derivations and catalogues survive more than correlations. FAILS as stated, holds in
direction.** n = 49; identity/taxonomy **14/43 = 0.326**, correlation **0/6 = 0.000**;
Fisher p = 0.1639. The direction is as predicted and correlation is perfectly separated — no
correlational claim in this vault survived — but six rows cannot carry a p-value.

**H2 — famous pairs are more often prior art. FAILS, and reverses.** n = 82; famous
**1/11 = 0.091** prior art, obscure **18/71 = 0.254**; Fisher p = 0.4430. The famous pairs
(Charnov × Gittins, Landauer × Shannon, Hopfield × Shannon, Archard × USLE) mostly ended
`narrowed`, not repackaged; it was the obscure pairs whose computations turned out to be textbook.

**H3 — claims made after blind briefs were introduced die at a HIGHER rate. FALSIFIED in
direction.** n = 82; blind brief **5/10 = 0.500** survived, no brief **21/72 = 0.292**;
Fisher p = 0.2754. The broader form of the same variable is the paper's only significant result:

| round | survived | died | rate |
|---|---|---|---|
| post-audit (2026-09-05) | 17 | 18 | 0.486 |
| early (2026-09-03) | 9 | 38 | 0.191 |

n = 82, Fisher two-sided **p = 0.0078**. §5 argues this is at least partly a coding artifact.

**H4 — data joins with scale mismatch die. DIRECTION ONLY, and the direction is perfect.**
n = 5; mismatch **0/3** (C35, C43, C47 — USDA `T` map units against point ¹⁰Be, 0.5° cell
medians, 800 CONUS points), same-scale **2/2** (C38, C44 — site-to-site, species-to-species).
Fisher p = 0.1000, smaller margin 2, so the brief forbids calling this evidence. It is the
cleanest-looking pattern in the dataset and the one with the least data behind it.

**Logistic model: not fitted.** The counts gate passed (n = 82; every level ≥ 5) but
`claim_kind = correlation` is completely separated on the outcome, so the maximum-likelihood
estimate does not exist. A penalised fit would report a coefficient the data do not contain.

## 3. Descriptive — survival by move type

| move | survived / n | rate |
|---|---|---|
| catalogue (pre-registered enumeration) | 5/7 | 0.714 |
| instrument run | 3/5 | 0.600 |
| data join | 2/5 | 0.400 |
| derivation / proof | 5/15 | 0.333 |
| citation comparison | 8/30 | 0.267 |
| computation on published numbers | 3/16 | 0.188 |
| replication | 0/3 | 0.000 |
| simulation | 0/1 | 0.000 |

Not a pre-registered test; no p-values are claimed and four of the eight cells have n ≤ 5.

## 4. What it means for the method

Three readings survive their own caveats:

1. **Computation on already-published numbers is the vault's weakest move** — 3/16, and it is the
   move that produced C19's withdrawn hormesis window, C33's withdrawn `P(starve)`, and C1's
   struck headline. Re-deriving a number from a paper's own figures buys a result that the
   paper's own literature usually already owns.
2. **Pre-registered enumeration and instrument runs are the strongest** — 5/7 and 3/5. Both share
   a property the losing moves lack: the *output* is a specification or a count that is true
   whichever way the world turns, so there is no number for an audit to take away. Weight the
   programme toward moves whose honest null is still a publishable object.
3. **Scale discipline, not sample size, is what killed the soil cluster.** Every join that crossed
   a scale boundary died and every join that did not survived. n = 5, so this is a hypothesis for
   the next round, not a finding — but it is cheap to enforce in advance.

And the one thing the numbers say plainly: **an adversarial pass is not a kill mechanism.**
Survival with an adversarial pass 15/48 = 0.312, without 11/34 = 0.324. What the passes did was
convert `live` into `narrowed` — 26 of 82 claims sit there — which is the vault's most common
fate and its least-discussed one.

## 5. Honesty

- **Single coder, not blind to outcome.** The coder is an agent that had read the notes before
  coding them. The mitigation is real but partial: every predictor was defined in
  `audits/blind-brief-c51-2026-09-05.md` and hashed before a single outcome column was read,
  and predictors (a)–(h) are mostly structural facts about a note — its move, its date, whether
  a brief file exists — rather than judgements about its quality. The two predictors that *are*
  judgements are `famous` and `move`, and both were coded from the note's own named anchors.
- **The significant result is confounded with how the outcome was read.** Early claims were graded
  mostly by the novelty audit (which hands out REPACKAGED freely); post-audit claims were graded
  mostly by their own callouts and standings (which record a pre-registered result as standing
  even when the tested hypothesis failed). A pre-registered null such as C46 or C50 is coded
  SURVIVED because its stated result stands, while an early repackaging is coded not-survived.
  That is a defensible reading of "survived adversarial review" and it is also exactly the kind of
  reading that could manufacture the p = 0.0078. **Do not quote H3b as evidence that the vault got
  better at making claims.**
- **Survival is a function of audit intensity, which changed within the day.** The 2026-09-05
  round applied blind briefs, negative controls and adversarial files that 2026-09-03 never faced;
  those same notes are also the ones with the highest survival. Both directions of that
  relationship are present in the data and this design cannot separate them.
- **Ambiguous rows are marked, not resolved.** Eight rows carry an `AMBIGUOUS` flag in the `notes`
  column: C4 (a three-way SPLIT compressed to one row), C15 and G22 (LOCATED grades where no prior
  art was actually found), C25 (derivation intact, prediction dead), C37 (born conditional rather
  than narrowed later), and the pre-registered nulls C26/C45/C47 (the *claim* died; the *note*
  stands as its record).
- **n is small and the tests are four.** No multiplicity correction was applied, as pre-registered.
  Three of the four tests have a smaller margin under 12.
- **One project, one vault, one day.** Nothing here generalises past this repository.

## 6. Sources

The dataset's `source_line` column cites, per row, the file and line where the outcome was read:
[[novelty-audit]] grade tables, each gap note's `**STANDING:` line, each computed note's callout
and `## Corrections` section, `log.md`, and `audits/c43-adversarial.md`,
`audits/g34-adversarial.md`, `audits/g36-adversarial.md`.
