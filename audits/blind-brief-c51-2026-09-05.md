# Blind brief — C51, vault meta-analysis of claim survival

Written 2026-09-05, **before any outcome column was read or coded**. Hash of this file
(sha256, computed on the file as committed) is the pre-registration token.

## Question

Across every graded claim this vault has produced, what predicts whether a claim SURVIVED
adversarial review and prior-art search?

## Unit of analysis

One claim = one headline sentence (the `>` callout result line of a computed note, the
`**STANDING:` line of a gap note, or the headline question-answer of a question note).
Exactly one row per note. No note contributes two rows even where its body carries several
sub-results; sub-results are folded into the headline and any residual is recorded in `notes`.

## ID set to be coded (fixed now, before coding)

- Computed notes: every `vault/computed/C*.md` present in the repo — C1–C22 and C25–C50
  (C23 and C24 do not exist in this vault). n = 48.
- Gap notes: every `vault/gaps/G*.md` present — G1–G9, G11, G12, G17, G19–G23, G25,
  G27–G37 (G10, G13–G16, G18, G24, G26 do not exist). n = 29.
- Question notes: Q1–Q10. n = 10.

Expected total n = 87. Any note that turns out to carry no gradable claim is coded
`outcome = ungraded` and excluded from the hypothesis tables, with the exclusion counted.

## OUTCOME vocabulary (taken from the vault's own words)

- `SURVIVED` — novelty-audit verdict NOVEL, or `standing: live` with the headline claim
  intact and no `## Corrections` entry that changes the number or the direction.
- `NARROWED` — `standing: narrowed`, or a Corrections entry that keeps the claim but
  restricts scope, sample, or conditions.
- `WITHDRAWN` — `standing: withdrawn` / `overturned`, or a Corrections/log entry that
  withdraws the number or reverses the sign. ("KILLED" is coded here.)
- `PRIOR_ART` — the vault's REPACKAGED / REDISCOVERED / LOCATED verdicts: the result is
  real but already in the literature.
- `ungraded` — no adversarial pass, no novelty verdict, no standing change; open item.

Binary for the models: `survived = 1` iff outcome == SURVIVED; else 0. NARROWED is coded
0 in the primary analysis and 1 in a stated sensitivity analysis, because a narrowed claim
partially survived.

## PREDICTORS, each with its coding rule

(a) `move` — the move type that produced the claim, read from the note's method section:
`derivation` (proof or algebraic identity), `catalogue` (pre-registered enumeration),
`computation` (arithmetic on already-published numbers), `data_join` (join across two or
more independently fetched sources), `citation_compare` (same-object citation/overlap
comparison), `instrument` (an API/instrument run producing new measurements),
`simulation`, `replication` (re-run of an earlier vault result).

(b) `famous` — `famous` if the anchor works on BOTH sides carry cited_by > 2,000 (as
recorded in the note or its sources note); `obscure` if either side is below; `unknown`
if the note records no citation counts.

(c) `provenance` — `primary` (the note fetched the numbers itself, with provider+date),
`secondary` (numbers quoted from a paper or a prior vault note), `none`.

(d) `blind_brief` — 1 iff an `audits/blind-brief-*` file exists for this claim.

(e) `adversarial` — 1 iff an `audits/*-adversarial.md` exists for it, or the note records
a negative control, positive control, or explicit adversarial pass.

(f) `scale_mismatch` — `same` if both joined sides are the same object at the same scale;
`mismatch` if the join crosses scales (basin-vs-point, map-unit-vs-site, species-vs-site,
country-vs-plot); `na` if the claim involves no join.

(g) `claim_kind` — `correlation`, `number` (a ratio, constant, or point estimate),
`identity` (a proof or exact equivalence), `taxonomy` (a classification or catalogue).

(h) `round` — `early` (produced before the 2026-09-05 audit rounds) or `post_audit`
(produced during or after them), read from the log date.

## Hypotheses (directions stated now)

- **H1** Derivations and pre-registered catalogues survive at a higher rate than
  correlations. Test: `claim_kind in {identity, taxonomy}` vs `correlation` × survived.
- **H2** Famous pairs are more often prior art. Test: `famous` × `outcome == PRIOR_ART`.
- **H3** Claims produced after blind briefs were introduced die at a HIGHER rate — the
  audit got stronger, not the claims worse. Expected direction: survival LOWER in
  `blind_brief = 1`. A higher survival rate there would falsify H3.
- **H4** Data joins with scale mismatch die. Test: within `move == data_join`,
  `scale_mismatch` × survived; expect mismatch → not-survived.

## Analysis, fixed now

Contingency table per hypothesis; two-sided Fisher exact test on the 2×2 collapse;
alpha = 0.05, no multiplicity correction (four pre-registered tests, reported as such).
A logistic model on `survived` with `claim_kind`, `blind_brief`, `provenance` is fitted
only if n_graded >= 60 and each level has >= 5 observations; otherwise omitted.

**n threshold.** Any table whose smaller margin is < 5 is reported as DIRECTION ONLY —
counts and the sign of the difference, no p-value claimed as evidence. Any Fisher p is
reported but never called a finding when the smaller margin is < 5.

## What this design cannot do

One coder, one vault, one day. Coding is not blind to outcome; the mitigation is that
predictors were defined in this file before any outcome was read, and that predictors
(a)–(h) are mostly structural facts about the note rather than judgements about it.
