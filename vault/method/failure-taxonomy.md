---
name: failure-taxonomy
type: method
---

# A taxonomy of agent-driven research failures

> **25 modes, six groups, 79 logged instances in one day.** Most frequent: **P2 — the unattributed
> count** (7), a figure promoted without provider, endpoint and fetch date. Next: **P1 — two
> numbers in one field** and **P4 — a published margin adopted as if computed** (6 each).
> This is a **catalogue of modes, not a partition of events**: the modes overlap, one event can
> populate several, and 79 counts annotations rather than distinct events.

One project, one day (2026-09-05), one orchestrator. Every entry is a failure this vault committed
and caught, with how it was caught, the guard now standing, and the **actor**: the **model**
(reasoning), the **tooling** (API/parse), the **orchestration** (parallelism, briefs), or the
**human** (scope, over-trust). All instances are logged in [[log]] under that date.

Companion to [[failure-modes]] — six ways a measured **zero** can be fake inside one instrument.
This note covers the whole loop.

## Group 1 — Provenance

**P1. Two numbers in one field.** *Two measurements — of two objects, two runs, or one work in two
roles — carried as one.* 578 vs 595 references for `10.1103/RevModPhys.90.031001` (Crossref's
deposited list vs the printed PDF bibliography, both true); [[G28-marginal-value-gittins]] carrying
co-citer counts of **8 and 5** from two runs without saying so; Griebling et al. 2026
(`10.1016/j.anbehav.2026.123491`) cited in G28 both as its one direct ecology→OR contact **and** as
proof the fields meet only through a third field; [[G29-early-warning-prognostics]]'s frontmatter
saying "zero in all three decade bins" while its body table says 1.
**Caught by** audit. **Guard:** CLAUDE.md §Numbers — establish both numbers measure the same object
before calling one wrong; nothing checks frontmatter against body. **Actor:** human over-trust via
the model.

**P2. The unattributed count.** *A figure without provider, endpoint and fetch date.* The 578,
whose defect was an unattributed number, not a hallucination — **the same event is the first
instance of P1** (578 and 595 are two objects carried in one field) and is the entry logged as a
*correction of a correction* under **Pr5**, so one event populates three modes;
[[G25-proofreading-coding]]'s 1,463 citers, provider never logged, against today's
1,340 / 1,593 / 1,656; G28's 1,542 / 1,013 / 1,010 / implied, which were **one number badly
measured**; every [[disclosure-ledger]] row before the `Fetched` column.
**Caught by** audit. **Guard:** CLAUDE.md §Numbers; the `Fetched` column; the provider table in
[[citation-sources]]. **Actor:** model.

**P3. Secondary as primary; the failed lookup written down as a fact.**
[[G21-dimensionless-regime-map]]'s three "Vogel" quotes come from a magazine feature, not either
book; `10.1038/s41467-022-30804-8` recorded "not located" — it resolves, is by
Jordan/Shorttle/Rimmer, and re-grades [[C30-venus-phosphine-audit]]'s biotic row. **Caught by**
audit. **Guard:** novelty grades
record **access level**, not "unobtained"; [[citation-sources]] §"a blocked API is not a blocked
method". **Actor:** model.

**P4. A published margin adopted as if computed.** *A number the source already published is
restated — or evaluated by hand beside a script that could have done it — and the agreement called
confirmation.* [[C30-venus-phosphine-audit]] §Corrections: three of seven errors are one habit
(the round `τ ×10³`, the fugacity order-count, the back-derived shortfalls), and rows 5 and 7 are
`[RESTATED]` because three ledger rows re-divided Bains' own margins; [[C29-recovery-beta]] §5.3
giving 40^(−0.413) = 0.30 when it is 0.2179. **Caught by** audit — `audits/06-math-rounds3-6.md`'s script-vs-note table. **Guard:**
every division performed from raw inputs inside the script. **Actor:** model.

## Group 2 — Statistics

**S1. Pseudoreplication, and the confound already in the file.**
[[C43-soil-ha-replication]]'s ρ(T, P) = −0.180, p = 4.5e-9 over 1,053 SSURGO sites: on 0.5° cell
medians it is −0.041 (p = 0.58), and a cluster bootstrap over the 48 source studies gives
[−0.341, +0.053]. `SLP_AVE` sat in C43's own `sites.json` and ρ(slope, P) = **+0.610,
p = 2.1e-108** — larger than anything the note reported, collapsing the partial to −0.074.
Withdrawn. **Caught by** adversary (`audits/c43-adversarial.md`), then replication
([[C47-tfact-mechanism-test]]: ρ = +0.090 on 114 independent sites). **Guard:** every site-level join
reports cluster count, cluster medians and a cluster-bootstrap CI, declustering unit fixed **in the
pre-registration**; any topographic field has its correlation reported. **Actor:** model.

**S2. The pre-registration not honoured — found in the data, or the power gate ignored.**
C43 §3's depth-assignment mechanism, presented as the project's own and as a pre-registered H2 pass;
[[C40-setpoint-survival-test]] T1 (ρ = +0.63, n = 4, p = 0.500) and
[[C39-duane-governance-blind]], both underpowered by their own gates. **Caught by** the pre-registration itself, then a hashed non-replication. **Guard:** [[predictions]]
— append-only, sha256-stamped, dated; briefs archived before dispatch. **Actor:** model; guard owned
by orchestration.

**S3. Estimator dependence, and the wrong likelihood for the censoring scheme.**
[[C32-recovery-beta-replication]] certified β = 0.733 on two variants that were **both the same
wrong likelihood**; the correct current-status likelihood gives 0.051 [0.014, 0.089] — a factor of
14 — and the shape is not identifiable at all, leaving "early-or-never" with no number; also
[[C18-durability-axis]]'s mixed-estimator β axis. **Caught by** audit. **Guard:** every row names its estimator; one axis per object class.
**Actor:** model.

**S4. Incommensurable axes pooled; design artifacts read as results.**
[[C19-hormesis-biphasic-fit]]'s "≥15× window" was 1500%/100%, the ratio of the highest to the lowest
**tested** dose, scored against toxicology's 10–20× — renamed "tested dose range", verdict now "no
comparison possible"; the same note's "+20% to +80%" pooled a σ'_f-equivalent *estimate* with a
*measured* endurance limit. **Caught by** audit. **Guard:** like-for-like restatement
before any comparison verdict. **Actor:** model.

## Group 3 — Instruments

**I1. The phantom key.** *A blank field enters a set and inflates every set built the same way by
exactly 1.* `_scripts/intersect.py` built citer sets from `row["citing"]` with only a truthiness
guard, and OpenCitations returns records with an **empty `citing` field**. Ten of twenty re-run
pairings would have read one higher, and an intersection of 1 is exactly where a gap claim becomes a
bridge claim. **Caught by** a script self-test, after a scout pass reported five phantom "1-hit"
candidates that are clean zeros.
**Guard:** `_key()` strips both keys, drop counts printed, `--selftest` asserts no blank survives.
**Actor:** tooling.

**I2. The false zero from a field that does not exist.** Europe PMC does not honour the `FULL_TEXT:`
prefix and returns **0 for everything**, including `FULL_TEXT:"fat reserves"` alone, which cannot be
zero — ten clean confident zeros averted. The same endpoint's `/citations` response carries no
`doi` field at all, which made an earlier adapter report 1,719 records as **0 unique DOIs**.
**Caught by** a calibration query whose answer cannot be zero, and the printed drop count.
**Guard:** calibrate both sides; **print the dropped count, always**. **Actor:** tooling.

**I3. Provider state read as data: coverage holes and spent budgets.** "OpenAlex blocked" was carried
in three gap notes when it was a spent **daily budget** (HTTP 429, `"Insufficient budget… Resets at
midnight UTC"`, `retryAfter` 47,052 s); "Semantic Scholar is 429 unauthenticated" was a
burst against a shared pool — paced at 1.1 s it enumerated 4,605 citers with no key; and Semantic
Scholar's pre-1990 holes sink four of one round's anchors. **Caught by** the `--all` provider table and a re-probe. **Guard:** `err`
rows are failed fetches, **never zeros**; `providers.fetch` raises `BudgetExhausted` rather than
parking the round. **Actor:** tooling, triggered by Pr3.

**I4. The tautological check.** *A test that cannot fail, reported as a passed test.*
[[reservoir-audit]] **F9** — on generator-form inputs `Σ = P_useful/(F·Δu)` divides step 2's
`F_req = P_useful/v` straight back out, so `Σ ≡ 1` exactly, found at `Σ = 1.0000` by
[[C46-reservoir-audit-negative-control]]; and [[C25-whittle-foraging]] §3 called re-substituting the
Whittle index into its own defining condition a confirmation. **Caught by** a negative control
(C46). **Guard:** F9 — on generator inputs, skip the energy
leg and say so, or state an `F_req` measured independently of `P_useful`. **Actor:** model.

**I5. The positive control never run.** [[C33-lolp-starvation]] rev.1 propagated a forward energy
budget for a full round before anyone checked it against Brodin, Nilsson & Nord 2017's own stated
0.74 g/day. It does not reproduce: every admissible mixture of the paper's two behaviours floors at
1.15 g/day, 1.56× the paper's figure. C33 rev.2 **fits**
α_eff = 44.15 kJ/day and labels it a fit everywhere; P(starve) is withdrawn. **Caught by** the
positive control, once adversarial review demanded it. **Guard:** `c33_lolp.py` runs it **as
section 0**. **Actor:** model.

## Group 4 — Reasoning

**R1. The arrival-state assumption.** [[C25-whittle-foraging]]'s residence-time column `t*` was
computed from arrival at x = 1, while the passive dynamics give a round-robin steady-cycle arrival
at x_arr = 1 − (1 − GUD)e^(−rτ). At rτ = 0.2 the ratio is 0.198, not 0.757 — a factor of 3.8 — and
the corrected column is **non-monotone** where the old one fell monotonically. **Caught by** audit;
the script reproduced the note **and the defect**, so a reproduction check is not a correctness
check. **Guard:** the script prints both columns.
**Actor:** model.

**R2. Metaphor mistaken for the same object.** [[G34-lolp-starvation-risk]] — LOLE is **not** a
first-passage quantity; title and thesis corrected, and all eight `"loss of load probability" AND
"bird"` hits are bio-inspired **metaheuristics**, not biology. **Caught by** adversary (metaphor
test), hit by hit.
**Guard:** [[homographs]]; [[failure-modes]] mode 2; irrelevant nonzero is still a zero.
**Actor:** model.

**R3. A sign error pointing at the hoped-for result.** C19's log-quadratic fit implied `Nf` below
baseline for coverage < 77% — that light peening is *harmful*, contradicting `Nf → N₀` as
coverage → 0 — so the 73× window is withdrawn and the admissible refit constrains no window at all;
G36 leg 2 **dies on sign** after a four-leg inquiry. **Caught by** replication against real data, and a refit under an admissible functional form.
**Guard:** run the falsifier against data before quoting the fit. **Actor:** model.

**R4. The anchor measures the wrong literature.** G34's citation-intersection anchors measure a
literature **G34's own scope excludes**; [[G31-biosignature-diagnostic-theory]]'s four B-anchors are
all clinical, so the ROC ancestry astronomers would plausibly cite (Peterson & Birdsall 1954, Green
& Swets 1966) was never run. **Caught by** adversary and audit. **Guard:** calibrate both sides;
re-test by [[citation-intersection]]. **Actor:** model.

## Group 5 — Process

**Pr1. The pre-announced halt.** [[C30-venus-phosphine-audit]]'s step-0 halt was named in advance in
`audits/scout-03-astrobiology.md` §Job 1 and restated in the brief the agent ran from, so it tests
only that the state is reachable, not that the instrument halts on its own ([[reservoir-audit]]
D.3a). **Caught by** an audit of the brief. **Guard:** the five-line blind-brief template, archived
and **sha256-hashed before dispatch**. **Actor:** orchestration.

**Pr2. The single-agent blind.** [[C46-reservoir-audit-negative-control]] (brief hash `5e39ef6f…`)
and [[C50-reservoir-audit-d2-control]] (`fae035f8…`) removed pre-announcement contamination but not
**recognition**: C46's case is a textbook worked example, and C50's input was *labelled synthetic*,
validating the wording of step 0(a) rather than the instrument's judgement. **Caught by** the notes'
own §4 honesty sections. **Guard: no guard yet** — the fix is named (the next case briefed by a
*different* agent on an unlabelled input) and not yet run. **Actor:** orchestration.

**Pr3. Parallel agents sharing one budget and one file.** OpenAlex's 100k calls/day is exhausted by
more than four parallel agents — the 429 hit `audits/g34-adversarial.md` on its **first** call, so
every `N_universe` blocked that day must be re-fetched on a later UTC day; and
`00-index.md:143` still carried superseded wording because it was "owned by another agent this
round". **Caught by** reading the 429 **body**, not the status code; audit; lint. **Guard:** stagger
agents or route to OpenCitations; per-round file ownership plus `PENDING-*` staging.
**Actor:** orchestration.

**Pr4. Stale watchers and notification loops.** *Orchestration keeps watching artifacts and sessions
whose state has moved, re-reporting finished work as new.* Observed during this day's rounds. **No
vault note records it** — which is the finding: the failures the vault can enumerate are the ones
some agent was asked to write down. **Caught by** the human, watching the loop. **Guard: no guard
yet.** **Actor:** orchestration.

**Pr5. A correction that is itself wrong.** [[stress-strength-interference]] withdrew
[[G19-safety-factor-derived-twice]]'s "46 citations" for Alexander 1997 as stale, offering 36/39/28 —
but 46 is **OpenAlex and current**: a provider disagreement misread as a decayed number, so the
retraction was the error. The 578/595 case is logged as a *correction of
a correction*. **Caught by** audit, on a re-fetch. **Guard:**
[[relationship-description]]'s symmetry rule — a withdrawal must meet at least the standard of the
claim it withdraws — and [[failure-modes]]'s "never overturn on a bare count: host + query + date".
**Actor:** model, enabled by human over-trust in whichever number arrived second.

## Group 6 — Framing

**Fr1. The headline overclaims relative to its own body.** [[C28-biosignature-roc]]'s pull-quote
attributed specificity 0.90–0.99 to "the field's own false-positive enumeration" while the body
concludes specificity is **not currently estimable** — an enumeration of mechanisms is a list, not a
rate over a reference population. **Caught by** audit. **Guard:** the callout carries the body's disclaimer; no lint rule.
**Actor:** model.

**Fr2. "Value of the index" language.** [[C45-whittle-network-sim]] — the Whittle rule run forward in
a 20-patch network fails **3 of 5** pre-registered predictions, the fast/slow GUD ratio is **1.06,
not 1.34**, and the value of the index over Charnov's rule is **−0.5%**. The paper now states the
field prediction as a ratio band [1.06, 1.27] and claims **no improved intake**. **Caught by**
simulation against the pre-registration. **Guard:** pre-register the number the method must beat;
publish the band, not the claim. **Actor:** model.

**Fr3. A prediction stated without its required conditions.** [[C25-whittle-foraging]]'s regrowth
prediction is specific to **saturating** renewal; under Kadmon 1992's measured **linear** nectar
renewal the index goes flat and the GUD sign reverses ([[C48-kadmon-regrowth-test]], P-068 — test
not run, both papers paywalled). **Caught by** adversary, then a literature check on the renewal
form. **Guard:** the note names the renewal class in the prediction sentence. **Actor:** model.

## The table

| mode | actor | caught by | guard | recur. |
|---|---|---|---|---|
| P1 two numbers in one field | human / model | audit | CLAUDE.md §Numbers | 6 |
| P2 unattributed count | model | audit | provider + endpoint + date | **7** |
| P3 secondary as primary; failed lookup as fact | model | audit | access-level grades | 4 |
| P4 published margin as computed | model | audit (script vs note) | divide from raw inputs | 6 |
| S1 pseudoreplication + hidden confound | model | adversary, then replication | declustering + bootstrap | 2 |
| S2 pre-registration not honoured | model | pre-registration, then non-replication | hashed briefs | 4 |
| S3 estimator / wrong likelihood | model | audit | estimator per row; one axis/class | 4 |
| S4 incommensurable axes; design artifact | model | audit | like-for-like restatement | 4 |
| I1 phantom blank key | tooling | script self-test | strip keys; `--selftest` | 1 (10 rows) |
| I2 false zero from a missing field | tooling | calibration + drop count | print drops | 2 |
| I3 coverage holes and spent budgets | tooling / orchestr. | provider table | `err` is never 0 | 6 |
| I4 tautological check | model | negative control; adversary | [[reservoir-audit]] F9 | 4 |
| I5 positive control never run | model | positive control | control as section 0 | 1 |
| R1 arrival-state assumption | model | audit | script prints both columns | 1 |
| R2 metaphor as same object | model | adversary | [[homographs]]; inspect hits | 3 |
| R3 sign error toward the hope | model | replication + refit | falsifier before the fit | 3 |
| R4 anchor measures wrong literature | model | adversary + audit | calibrate both sides | 3 |
| Pr1 pre-announced halt | orchestration | audit of the brief | hashed blind brief | 1 |
| Pr2 single-agent blind | orchestration | the note's honesty section | **no guard yet** | 2 |
| Pr3 parallel agents, one budget/file | orchestration | 429 body; audit; lint | stagger; file ownership | 4 |
| Pr4 stale watchers | orchestration | the human | **no guard yet** | 1 |
| Pr5 a correction that is itself wrong | model / human | audit re-fetch | symmetry rule | 5 |
| Fr1 headline overclaims body | model | audit | callout carries the disclaimer | 3 |
| Fr2 "value of the index" | model | simulation | pre-register the number to beat | 1 |
| Fr3 prediction without conditions | model | adversary | name the regime | 1 |

`recur.` counts logged instances on 2026-09-05, not only those itemised above.

**Ownership, summing to 25.** Counting the `actor` column above: the **model** owns 16 modes
outright (P2, P3, P4, S1, S2, S3, S4, I4, I5, R1, R2, R3, R4, Fr1, Fr2, Fr3), the
**orchestration** 4 (Pr1, Pr2, Pr3, Pr4), the **tooling** 2 (I1, I2), and **3 modes are jointly
owned**: P1 (human / model), I3 (tooling / orchestration), Pr5 (model / human). 16 + 4 + 2 + 3 =
25. **The human owns no mode alone and co-owns two**, P1 and Pr5, both by over-trust in a number
that arrived without a provider. Counting joint ownership as implication rather than sole
ownership: model 18, orchestration 5, tooling 3, human 2. An earlier version of this line read
"15 modes outright, the orchestration 5, the tooling 3", which sums to 23 and gave the human no
count; the recount is logged in [[log]].

**This list is not a partition.** The modes overlap and one event can populate several. At least
three logged events do: the **578/595** reference count is the exemplar of P2, the first instance
of P1, and the correction-of-a-correction under Pr5; **C46's Σ ≡ 1** is both I4 and, as a brief
contaminated by recognition, Pr2; the **spent OpenAlex daily budget** is both I3 and Pr3. So the
79 instances are annotations, not distinct events, and the three-most-frequent ranking is a
ranking of annotations. The count of distinct underlying events was not recorded and is not
recoverable without re-coding.

**No guard at all:** Pr2, Pr4, and the frontmatter-vs-body half of P1.

## What the guards cost

**Cheap, and it catches none of these — by design, not by failure.** `_lint.py` blocks a commit
on schema drift in under a second, and ran on every commit (89 to date) over roughly 140 notes.
**Zero of the 25 modes were caught by lint.** That zero is a **selection effect**: the linter
checks frontmatter vocabulary, field types and wikilink reachability, and all 25 modes are
semantic. The honest reading is the narrow one — *schema linting does not substitute for
semantic auditing* — not "the cheap guard caught nothing". Its one contribution is Pr3, where a
half-landed parallel edit surfaces as a dead link.

**Cheap, and the best ratio on the record.** The script self-test (I1), the calibration query — a
term whose answer *cannot* be zero (I2) — and the printed drop count cost minutes each and caught
the two failures that would have manufactured the most claims: ten phantom bridges, ten fake zeros.

**Moderate, and mechanical: the provenance audit.** Re-fetching every number with a named provider
and date caught 11 modes — all four P rows, S3, S4, R1, I3, Pr3, Pr5, Fr1.

**Expensive: one adversary per claim.** Each of the three adversarial reviews is a full agent-round
against one cluster. They caught 7 modes — S1, I4, R2, R3, R4, Fr3, and the demand that produced I5
— and are the **only** guard that caught the fatal ones: the pseudoreplication that killed C43's
headline, the sign error that killed G36 leg 2, the metaphor that mis-titled G34.

**Most expensive, and irreplaceable: replication and controls.** A pre-registered non-replication, a
positive control, two negative controls and a forward simulation caught 3 modes — but only they can
catch **I5** and **Fr2**, where the claim is internally consistent and simply untrue.

**Catch counts, by earliest catch, with the exposure each guard was applied to:** audit 11 (all
87 coded notes, 7 audit reports) · adversary 7 (3 claim clusters) · replication and controls 3
(5 runs) · self-test and calibration 2 (2 instrument adapters) · pre-registration 1 (12 blind
briefs) · the human 1 (continuous, no denominator) · **lint 0** (89 commits × ~140 notes). The
exposures are in different units and are not divisible into a common rate; they are printed
because a tally without them compares three exposures to hundreds. The cheap guards are worth running
always and are not sufficient; the expensive ones cannot be run on everything, so **what they are
pointed at is the orchestrator's most consequential decision of the day.**

## For anyone running agents on science

1. **A number without a provider, an endpoint and a fetch date is not a number.** From P1 (578 and
   595 are both true, of two different objects) and P2 (G25's 1,463; G28's four denominators, one
   number badly measured). An unattributed 578 and an unattributed 595 fail the same rule.

2. **A zero from an instrument is a claim about the instrument until it is calibrated.** From I2
   (Europe PMC's `FULL_TEXT:` prefix returning 0 on everything, including a term that cannot be
   zero) and I3 (a spent OpenAlex budget recorded as a property of OpenAlex). Run a query whose
   answer cannot be zero, print what the adapter dropped, and record a failed fetch as `err`.

3. **Fix the analysis before you see the data, and archive the brief with a hash.** From S2 (C43's
   mechanism found in the data, written up as a pre-registered pass) and Pr1 (C30's halt
   pre-announced to the agent that reported it). On C43 the declustering unit alone moves ρ from
   −0.18 to +0.02, so any such choice made after the fact is not a result.

4. **Point the instrument at a case whose answer you already know, in both directions.** From I5
   (C33's propagation trusted for a full round, then failing Brodin's own 0.74 g/day) and I4 (the
   reservoir audit's Σ ≡ 1 on generator inputs). A check that cannot fail has told you nothing, and
   an instrument that has never returned "nothing here" is exercised, not validated.

5. **A correction is a claim, and concurrency is a source of error.** From Pr5 (the "46 was stale"
   retraction, itself the error) and Pr3 (OpenAlex's budget spent by a parallel agent before
   another's first call; `00-index.md` left carrying superseded wording because two agents held one
   file). Hold a withdrawal to the standard of what it withdraws; give every file and every quota
   one owner per round.

## Honesty

One project, one day, one orchestrator. The 79 instances come from a single vault's 2026-09-05
record, and the recurrence counts are of **caught and logged** failures, not of failures committed;
that ratio is unknown. Nothing here is a rate — there is no denominator of claims attempted — so
"25 modes" describes one day's harvest.

The taxonomy was written by an agent of the same kind that committed the failures, reading a log the
same kind of agent wrote. It is blind in the way its own modes predict — most plainly at
**Pr4**, whose single instance has no vault note because no agent was asked to write one, and at **P3**, since a mode nobody looked for reads identically to
a mode that does not exist. Treat the list as a floor.
