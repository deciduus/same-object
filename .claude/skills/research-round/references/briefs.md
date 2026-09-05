# Brief templates by role

Fill every `<...>`. Keep the file-ownership block verbatim. Every brief ends with a "Report:" line.

## Common header (every brief)

Work in: `<repo root>`. Read CLAUDE.md first and obey it. Do NOT run git commit/stash/checkout/push.
`<N>` other agents run in parallel; touch ONLY: `<exact file list, new files marked new>`. Do NOT edit
`<files owned by others>`. Log entries go to new `vault/PENDING-log-<ID>.md` (frontmatter
`name: PENDING-log-<ID>`, `type: method`) in the `## [YYYY-MM-DD] kind | summary` format, plus
the 00-index line; do not link to the PENDING file from any note. Providers: `<which; which are
budget-locked>`. Run `python _lint.py` from vault/ at the end; 0 errors (unlinked-PENDING warnings
are expected).

## Researcher (derivation-first)

Read: `<the bridge/identity note in full>`, `<the standard note for "is an identity": C5 §1–§6 or
C37>`, `<audits that attacked the last attempt>`.
Task: make the identity emit a number that can be wrong.
1. Write the pre-registration first: the quantity, the prediction with sign and rough magnitude,
   the dataset or experiment that would test it, the pass/fail rule. Hash it to
   `audits/blind-brief-<ID>-<date>.md` before computing.
2. Derive. State every condition. Name every failure boundary with a verdict.
3. Compute the prediction table; script in `vault/_scripts/<id>.py`, stdlib/numpy only.
4. Run `refsweep.py` on the anchors with the claim's phrases; paste the top 10 with verdicts.
5. §Honesty: what a referee from each side attacks first. `>` callout in first 10 lines.
Report: the pre-registration hash, the theorem/prediction as stated, the table, the sweep hits.

## Researcher (data-first)

Read: `<the note that named the dataset>`, `<the method note for joins/null model>`, `<the prior
adversarial reviews on joins; audits/c43-adversarial.md is the standard>`.
Task: `<the computation>`. The brief must pre-empt the attacks that killed C43: source-study
clustering, obvious covariates (slope, mass, latitude), effect size with CI not only p, join
scale (same object, same scale), and a comparator clause that is not a positive control by
construction. Write those controls into the hashed brief before any outcome is joined.
1. Blind brief, hashed. 2. Fetch (state every endpoint that worked). 3. Run the pre-registered
tests. 4. Falsifier scan. 5. §Honesty. `>` callout.
Report: hash, endpoints, n, statistics with CI, pass/fail per hypothesis.

## Critic

You are the adversarial reviewer for one claim. Kill it if it can be killed. Read ONLY `<the
researcher's note and its script>`, `<the method notes it relies on>`, `<audits/*-adversarial.md as
the standard>`. Do NOT read the vault's prior view of this claim.
Attacks, each with evidence: (1) prior art: refsweep on the anchors, plus ≥8 search
formulations across providers; (2) metaphor vs same object; (3) join/scale/aperture; (4)
statistics: clustering, covariates, effect size, multiple tests; (5) the comparator clause;
(6) does it give a practitioner anything to do; (7) the honest sentence that survives.
Write ONLY `audits/<id>-adversarial.md` and `vault/PENDING-log-<ID>ADV.md` (proposed edits as text).
Output: Verdict (KILL / NARROW / SURVIVES; grade NOVEL / REPACKAGED / REDISCOVERED / LOCATED),
attacks numbered with outcome, the surviving sentence verbatim, proposed edits, what would settle it.

## Brief-writer (two-agent blind)

You are the BRIEF-WRITER. A different agent runs the audit. Read ONLY the method note's Part D
template and this prompt. Write the five-line template verbatim: case in units and parameters
(no verdict word, no discoverer name if avoidable), the standard run instruction, sources listed
in shuffled order without annotation (verify each DOI via Crossref; list only those that
resolve), the standard output line, the non-disclosure line. Append the sha256. Excluded words:
refuted, rebutted, confirmed, detection, non-detection, tentative, robust, artefact,
biosignature, life, biotic, abiotic, controversy.
Report: path, hash, DOIs that resolved.

## Runner (two-agent blind)

STRICT ORDER. Step 1: read ONLY the method note and the brief; verify the brief's sha256 before
proceeding. Step 2: run the procedure from step 0; record every step run and skipped; fetch only
the brief's sources. Step 3: only now read the vault's prior notes on the case; state whether
your blind verdict matched the vault's prior guess. §Honesty: did you recognise the case.
Report: hash check, step-0 verdict with the reductions table, enumeration, residual or halt,
match/mismatch with the prior view.

## Cold referee (paper or note)

You have ONLY the manuscript. Do not read anything else in the repository. Recompute every
derivation and every number. Sections: summary in your words; verification per item
(correct / error / cannot verify); major issues; minor issues; recommendation (accept / minor /
major / reject) with one paragraph; three questions for the author. Do not praise.

## Integrator

Apply a decided set of edits. ORCHESTRATOR DECISIONS (do not re-litigate): `<list>`. Touch ONLY
`<files>`. Add `## Corrections <date>` to each edited note listing every changed sentence old →
new. Record any critic disagreement as open, with both positions. Log entries to PENDING.
Report: every field changed, the new callout verbatim.
