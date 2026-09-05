---
title: |
  What survives: an audited record of 82 AI-generated cross-domain research claims
author:
  - name: Landon Holden
    affiliation: |
      Independent researcher; Arizona State University (student)
    email: deciduusleaf@gmail.com
    orcid: "AUTHOR TO SUPPLY"
date: 2026-09-05
abstract: |
  One human set the scope rule and the standards of evidence; Claude Fable 5.1 orchestrated;
  Claude Opus 4.8 agents executed under written briefs; the output is a public vault with
  lint-enforced schema and per-number provenance. This paper audits that record rather than
  advertising it. Of 87 headline claims coded on 2026-09-05, 82 were gradable: 26 survived
  (0.317, Wilson 95% CI 0.226-0.424), 26 were narrowed, 19 were prior art, 11 were withdrawn.
  That headline is a weighted average over a question mix nobody chose deliberately: by move
  type it runs from 0.19 to 0.71. "Survival" is not one variable. Splitting it by the field
  the outcome was read from gives `survived_novelty` 5/24 = 0.208 (0.092-0.405) for rows graded
  off the novelty audit and `survived_standing` 21/58 = 0.362 (0.251-0.491) for rows graded off
  a standing or a callout; the two are not the same measurement, and the round effect is
  partly this split. No claim was tested against the world: a written depth gate holds the
  project at Layer 2, so survival here means survived internal audit. The log carries 252
  dated entries across two working days, 97 of them corrections; two are corrections of
  corrections, of which one carries that `kind` and one is filed under `correction`. Twelve
  blind briefs were archived with sha256 hashes before dispatch; two are contaminated by
  recognition rather than by pre-announcement. Three dedicated adversarial reviews were run,
  and 48 of the 82 graded claims received some adversarial leg. No subject-level predictor of
  survival was detected: correlational claims survived 0/6, scale-mismatched data joins 0/3,
  the famous-pair hypothesis reversed, and an adversarial leg changed survival by 1.2 points.
  The one significant contrast is *when* a claim was made (17/35 = 0.486 against 9/47 = 0.191,
  Fisher p = 0.0078); `round` was a pre-registered predictor but this contrast was not a
  pre-registered hypothesis, so it is reported as **exploratory**, and it is confounded with
  how the outcome was read. It survives within the standing-graded stratum (16/33 against
  5/25, p = 0.0307). A companion catalogue records 25 failure modes over 79 logged instances;
  provenance modes dominate, and the list overlaps rather than partitions.
bibliography: refs.bib
csl-refs: true
---

<!-- AUTHOR: the affiliation line in the YAML header is a placeholder the author confirms
     before submission; ORCID is still to be supplied. -->

<!-- All numbers in this manuscript are traceable to notes in the research vault; the
     note ID is given in an HTML comment beside each. -->

# Introduction

There is now no shortage of demonstrations that a language model can produce something that
looks like a research claim. There is a shortage of records that say what fraction of those
claims are still standing after someone tries to kill them, which kinds die, and which guard
caught each death first. This paper is one such record: complete, adversarial to its own
output, and small enough to state its own limits honestly.

The setting is a single cross-domain synthesis project --- the Gradient Coupling Inquiry
[@vault] --- run under one scope rule: *a thread is in scope if it can reach a checkable
claim.* One human author set that rule, the questions and the evidence standards. Claude Fable
5.1 (Anthropic) acted as orchestrator, writing task briefs, auditing returns, and deciding what
was committed. Claude Opus 4.8 agents, run through Claude Code, did the derivations, database
queries, prior-art searches, fits and drafting, each under a written brief. All of the work
graded here was produced or re-graded on two days, 2026-09-03 and 2026-09-05.

The method is Literature-Based Discovery in Swanson's sense [@swanson1986]: two literatures
quantify the same object, do not cross-cite, and therefore each hold half a result. What is
reported here is not the science but the epistemics --- a kill rate, a null on subject-level
predictors, and a taxonomy of the ways the loop failed.

Two results are worth stating at the front. First, **no subject-level predictor of survival
was detected at this sample size** --- not the field, not the fame of the anchors, not whether
an adversary was pointed at the claim. This is a failure to detect, not a demonstration of
absence: two of the four hypotheses show perfect separation *in the predicted direction* on
six and five rows respectively, so the data are weakly consistent with subject-level
prediction, not against it. <!-- C51 §2 --> Second, **schema linting does not substitute for
semantic auditing**: a linter that blocks commits in under a second caught zero of the 25
failure modes, while the mechanical provenance audit caught 11 and one adversarial agent per
claim caught the three that were fatal. The linter's zero is a selection effect and is stated
as one in Section 5 --- `_lint.py` checks frontmatter vocabulary and all 25 modes are semantic
--- and the number is kept because the narrow reading is the useful one.
<!-- failure-taxonomy §"What the guards cost" -->

Nothing in this record was tested against the world. A written depth gate holds the project at
Layer 2 of its own ladder, so no claim here reached an experiment: **survival means survived
internal audit by the same system that produced the claim**, not external replication.

# Setting and method

## The ladder and the scope rule

Findings are staged on a four-layer ladder: (1) locate a gap where two fields quantify one
object without cross-citation; (2) apply the formalism and compute; (3) generate a checkable
prediction; (4) test it. A second, orthogonal lens --- Compare, Produce, Deduce --- sets the
current focus, and a written depth gate holds the project at Layer 2 until a thread is
developed deeply enough to earn Layer 3. <!-- strategy §"The depth gate" --> The gate is itself
an orchestrator artefact: a recorded refusal to advance, dated and argued.

## Closed vocabularies and lint

Every note carries YAML frontmatter checked by `vault/_lint.py`, which must exit 0 before a
commit. Standing is one of `live`, `narrowed`, `withdrawn`, `overturned`. Evidence is one of
`citation-intersection`, `full-text-read`, `string-protocol`, `single-review`, `not-assessed`,
ordered strongest-first. Three earlier words --- `holds`, `weakened`, `collapsed` --- are
*retired* and rejected by the linter, so a vocabulary change cannot be quietly undone.
Cross-domain contact is graded `nothing` / `word` / `metaphor` / `vocabulary` / `formalism` /
`data` with a redundant integer rank the linter cross-checks. Prose is forbidden in machine
fields, and every note must be reachable by wikilink from the index.
<!-- CLAUDE.md §"Closed vocabularies" -->

## Log discipline

Corrections are logged, never silently applied. The log is dated per entry, with a free-text
`kind` naming the move --- `correction`, `verification`, `computed`, `honest null`, `method`,
`vocabulary`. The rationale is that the *pattern* of errors is data, and this project has had
to correct a correction. <!-- CLAUDE.md §Corrections -->

Number discipline is the other half: a count is not a claim until it names provider, endpoint
and fetch date. The flagship case is that a reference count of 578 and a reference count of 595
for the same DOI are *both true* --- the first is Crossref's publisher-deposited list, the
second the printed bibliography --- so before calling a number wrong one must establish that
both numbers measure the same object. <!-- log 2026-09-05 "correction of a correction" -->

## The citation-intersection instrument and its null model

The gap test is a citation intersection: enumerate the works citing anchor A and those citing
anchor B, and count the intersection. A raw zero means little on its own, so each run is paired
with a **positive control** --- a pair of anchors known to be co-cited --- and reported as a
denominator-invariant control ratio. LBD evaluation has a literature of its own and the earlier
draft asserted its weakness without one: Swanson and Smalheiser's own interactive system
[@swanson1997] is evaluated by expert inspection of candidate pairings, and the standard
alternative is a time slice --- run the system on a corpus truncated at a past date and score it
against what was published afterwards [@yetisgen2009]. Neither supplies a *negative* control for
a single intersection, which is what the control ratio here is for; the claim made is that
narrow one, not that LBD evaluation is uncontrolled. The instrument's own failure modes are documented rather than assumed away: an
empty key field that inflates every set built the same way by exactly one; an endpoint that
returns 0 for every query, including one whose answer cannot be zero; and a provider's spent
daily budget recorded as though it were a property of the literature.
<!-- failure-taxonomy I1--I3 -->

## The blind-brief protocol

Twelve blind briefs were written, archived and sha256-hashed **before dispatch** to the
executing agent. They are twelve files, not fourteen: C39, C40 and C43--C52. C41 and C42 fall
inside the C39--C52 span and carry no brief.
<!-- audits/blind-brief-c{39,40,43,44,45,46,47,48,49,50,51,52}-2026-09-05.md, 12 files --> Each
fixes the ID set, the predictors, the tests, the power gate and the falsifier in advance. The
protocol exists because of a specific failure: an earlier audit's halt condition had been
pre-announced in the brief the agent ran from, so the run tested only that the halt state was
reachable, not that the instrument halted on its own. <!-- failure-taxonomy Pr1 -->

Two of the twelve are contaminated in a way hashing does not fix. C46 and C50 removed
pre-announcement but not **recognition**: C46's negative-control case is a textbook worked
example an agent can identify on sight, and C50's input was *labelled synthetic*, so it
validated the wording of the halt step rather than the instrument's judgement. Both notes say
so in their own honesty sections; the fix --- a case briefed by a *different* agent on an
unlabelled input --- is named and not yet run.
<!-- failure-taxonomy Pr2; reservoir-audit Part D, D.2/D.4 -->

## The adversarial leg

Two different things are called adversarial in this record, and the referee of the first draft
was right that the paper had run them together. They are separated here and used separately
throughout.

**A dedicated adversarial review** is a full agent-round whose brief was to kill one claim
cluster. There were exactly **three**: `audits/c43-adversarial.md`,
`audits/g34-adversarial.md`, `audits/g36-adversarial.md`. This is expensive --- one agent round
per cluster --- and was pointed, not universal.

**An adversarial leg** is the predictor `adversarial` as its coding rule was fixed in the
hashed C51 brief, §Predictors (e): *1 iff an `audits/*-adversarial.md` file exists for the
claim, **or** the note records a negative control, a positive control, or an explicit
adversarial pass.* Under that rule **48 of the 82 graded claims** carry an adversarial leg. The
rule was pre-registered before any outcome was read; it is quoted here verbatim because the
first draft reported the 48 without it.
<!-- audits/blind-brief-c51-2026-09-05.md §PREDICTORS (e) -->

The leg is **not** a proxy for the 2026-09-05 round, and this is checkable: of the 48, 27 are
post-audit rows and **21 are early rows**, while 8 post-audit rows carry no leg. The two
variables are correlated and not collinear.

## Novelty grading

Separately from standing, results were graded for novelty on a five-level scale: NOVEL,
REPACKAGED, REDISCOVERED, LOCATED (a documented gap or absence, LBD-style), and CORRECTED. The
audit's stated bias is toward humility --- where a grade was uncertain it was set lower, and any
result that *might* be a rediscovery is graded REPACKAGED, never NOVEL.
<!-- novelty-audit §"The grades" --> Where a gap note's `standing` field and a novelty grade
disagree, the standing wins, because the vault note and the index are canonical for standings.

# The record

## Claims and outcomes

One claim = one headline sentence: the callout of a computed note, the `**STANDING:` line of a
gap note, or the headline answer of a question note. The ID set was fixed in the
pre-registration: C1--C22 and C25--C50 (48), G1--G37 as they exist (29), Q1--Q10 (10) = 87
coded rows, of which 5 open questions carry no gradable claim, leaving **n = 82**.
<!-- C51 §1 -->

**The frame, stated in full.** The frame is *every note that exists in the vault* under those
three prefixes on 2026-09-05. Nothing inside the frame was dropped; the absences are IDs that
name no note. **C23 and C24 were never created** --- the computed-note numbering skips them and
no file, log entry or index line has ever carried either ID. **Eight G-IDs are retired**:
G10, G13, G14, G15, G16, G18, G24 and G26, each struck with a written reason in `METHOD.md`
§"Retired gaps" (an experimental frontier inside one field; three proposals with no result; an
intra-field dispute; a real result never written up, to be re-opened under a new ID; a thin
non-zero; and a reclassification to "not yet a shared object"). Retiring them was a scope
decision made before this audit and not by it. Finally, **C51, C52 and C53 postdate the
frame**: C51 is this analysis, and C52 and C53 were written after the ID set was hashed, so
none of the three is a graded row. Where §5 cites "C52 §grade table" it is citing C52 as a
*source* for another claim's grade, not counting C52 as a claim. This is why the 12 briefs
cover 14 IDs but only **10 of the 82 graded claims carry one**: the briefs for C51 and C52 sit
outside the graded set, and C41 and C42 have no brief.

: Outcomes, all coded claims (n = 87). <!-- C51 §1 -->

| outcome | n |
|---|---|
| SURVIVED | 26 |
| NARROWED | 26 |
| PRIOR_ART | 19 |
| WITHDRAWN | 11 |
| ungraded (open questions) | 5 |

Overall survival is **26/82 = 0.317**, Wilson 95% CI **0.226--0.424**. Narrowing is
**26/82 = 0.317** (0.226--0.424), prior art **19/82 = 0.232** (0.154--0.334) and withdrawal
**11/82 = 0.134** (0.077--0.224). All intervals in this paper are Wilson score intervals at 95%,
computed on the counts printed beside them. The single most common fate is not death but
*narrowing*: 26 of 82 claims still stand in reduced form. This is the least-discussed outcome
in AI-for-science reporting and, on this record, the modal one.

Broken out by move type (graded rows only, n = 82):

: Survival by move type, with Wilson 95% intervals. Not a pre-registered test; no *p*-values
are claimed and four of the eight cells have n ≤ 5. Every interval overlaps every other.
<!-- C51 §3; claims.csv -->

| move | survived | narrowed | prior art | withdrawn | n | rate | Wilson 95% CI |
|---|---|---|---|---|---|---|---|
| catalogue (pre-registered enumeration) | 5 | 0 | 1 | 1 | 7 | 0.714 | 0.359--0.918 |
| instrument run | 3 | 1 | 1 | 0 | 5 | 0.600 | 0.231--0.882 |
| data join | 2 | 0 | 1 | 2 | 5 | 0.400 | 0.118--0.769 |
| derivation / proof | 5 | 0 | 9 | 1 | 15 | 0.333 | 0.152--0.583 |
| citation comparison | 8 | 19 | 1 | 2 | 30 | 0.267 | 0.142--0.444 |
| computation on published numbers | 3 | 4 | 6 | 3 | 16 | 0.188 | 0.066--0.430 |
| replication | 0 | 2 | 0 | 1 | 3 | 0.000 | 0.000--0.561 |
| simulation | 0 | 0 | 0 | 1 | 1 | 0.000 | 0.000--0.793 |

The shape is legible even without inference. Moves whose *output is a specification or a count
that is true whichever way the world turns* --- pre-registered enumerations, instrument runs
--- sit at the top; there is no number for an audit to take away. Re-deriving a figure from a
published paper's own numbers sits near the bottom, at 3/16, and it is the move that produced a
withdrawn hormesis window, a withdrawn starvation probability, and a struck headline.
<!-- C51 §4 -->

## Survival is two variables, not one

The first referee's central design objection was that `outcome` is not one variable: early rows
were graded off the novelty audit, later rows off their own standing or callout, so a single
column carries two instruments. That is correct, and the fix here is to stop pooling them. Each
graded row's `source_line` names the file and line the outcome was read from, so the split is
mechanical, not a judgement:

- **`survived_novelty`** --- the outcome was read from a `novelty-audit` grade table. **n = 24.**
- **`survived_standing`** --- the outcome was read from a gap note's `**STANDING:` line, a
  computed note's callout or `## Corrections` section, or a log entry. **n = 58.**

: The two outcome variables. <!-- claims.csv, `source_line` column -->

| variable | n | SURVIVED | NARROWED | PRIOR_ART | WITHDRAWN | rate | Wilson 95% CI |
|---|---|---|---|---|---|---|---|
| `survived_novelty` | 24 | 5 | 0 | 19 | 0 | 0.208 | 0.092--0.405 |
| `survived_standing` | 58 | 21 | 26 | 0 | 11 | 0.362 | 0.251--0.491 |
| pooled | 82 | 26 | 26 | 19 | 11 | 0.317 | 0.226--0.424 |

The table settles the question by itself. **The two instruments cannot return each other's
verdicts.** The novelty scale has no way to say NARROWED or WITHDRAWN, so every one of its 24
rows is either SURVIVED or PRIOR_ART; the standing scale has no way to say PRIOR_ART, so all 19
prior-art rows and none of the 37 narrowed-or-withdrawn rows come from it. Pooling them
produces a four-level column no single grader ever applied. The pooled 0.317 is a weighted
average of 0.208 and 0.362 with weights 24 and 58 that were set by which notes happened to be
covered by the novelty audit.

This is also where a large part of the round effect lives: 22 of the 24 novelty-graded rows are
early rows, and 33 of the 35 post-audit rows are standing-graded. The confound named in Section
4 is, at least in part, this split. It is not all of it --- Section 4 reports the round contrast
*within* the standing-graded stratum, where it survives.

## Corrections

`vault/log.md` holds **252 dated entries** across the two working days, 30 under 2026-09-03 and
222 under 2026-09-05. Ninety-seven carry a `kind` containing "correction" (77 `correction`,
19 `correction (archived)`, 1 `correction of a correction`). The `kind` field is free text, so
the remainder is given in full rather than truncated: `method` 41, `computed` 28,
`verification` 25, `honest null` 11, `gap` 9, `vocabulary` 4, `provenance` 3, `negative
control` 3, `computed + verification` 2, and **29 other kinds appearing once each**
(`Layer-2 batch`, `Layer-2 five-fan`, `atomic-schema migration`, `blind negative control`,
`citation-intersection`, `closed by construction`, `corpus mined`, `counted`, `disclosure
thread`, `graph and Bases added`, `headline hardened`, `honest scorecard`, `hygiene`,
`ingested`, `instruments at the antifragile level`, `lint extended`, `migration`, `our own
claims tested`, `pre-registered non-replication`, `prediction failed`, `prior-art check`,
`re-read batch`, `re-read batch two`, `restored`, `review response`, `schema`, `simulation`,
`two free buildables run`, `unblocked`). The eleven named categories plus the 29 singletons
plus the 97 corrections total 252.
<!-- log.md, entry headers, recounted at commit f1faab3, 2026-09-05:
     grep -c "^## \[" vault/log.md -->

The earlier draft reported 245 entries and 93 corrections; those were counted before the last
seven entries were written, and the figures here supersede them.

**Two** entries are corrections *of* corrections, and the abstract, this section and the
`kind` tally now say two. The reason only **one** carries the `kind` string "correction of a
correction" is that the second was filed under the plain `kind` `correction` --- its header
reads `## [2026-09-05] correction | "46 citations was stale" was itself the error`. The
`kind`-field tally is therefore 1 and the count of the move is 2, and the discrepancy is a
property of a free-text field, not of the record. They are the most instructive rows in the
file. In the first, the project's flagship lesson had been recorded as "578 was wrong, the real
count is 595"; on re-fetch, 578 is Crossref's publisher-deposited reference list for
`10.1103/RevModPhys.90.031001` and 595 is the printed PDF bibliography. Two objects, two true
numbers. The defect in the original was never the value --- it was that the value carried no
provider, and *an unattributed 578 and an unattributed 595 fail the same rule.*
<!-- log 2026-09-05 --> In the second, a theorem note had retracted a gap note's "46 citations"
for Alexander (1997) as stale, offering 36/39/28 instead. Re-fetched the same day: OpenAlex
returns 46, OpenCitations 40, Crossref 36. A provider disagreement had been misread as a
decayed number, so **the retraction was the error** and was itself reversed.
<!-- log 2026-09-05; failure-taxonomy Pr5 -->

## Pre-registration

Twelve blind briefs are on file --- **C39, C40, C43, C44, C45, C46, C47, C48, C49, C50, C51,
C52**, one file each, each sha256-hashed before dispatch. That is twelve files spanning
fourteen IDs; C41 and C42 have none.
The meta-analysis reported in Section 4 is one of them:
`audits/blind-brief-c51-2026-09-05.md`, hash
`8844d375b302b987d7bc83ebbb8f2e4157f26df7f93fd7bcdc6517ac697d786a`, hashed before any outcome
column was read or coded. <!-- C51 header --> Ten of the 82 graded claims carry a brief --- C39, C40 and
C43--C50 --- and the other 72 predate the protocol; the briefs for C51 and C52 lie outside the
graded ID set, as Section 3.1 states. Separately, a `predictions.md` register holds dated,
sha256-stamped prediction texts. It exists because the project's first thirty log entries all
carry one date, and a same-day record cannot demonstrate that a prediction preceded its
confirmation --- which is the one thing a dated prediction is for.
<!-- predictions.md header -->

# What predicts survival

Four hypotheses were pre-registered in `audits/blind-brief-c51-2026-09-05.md`. Three fail and
the fourth is direction-only. Every rate below carries a Wilson 95% interval.
<!-- C51 §2 -->

**No multiplicity adjustment is applied, and the reason is stated rather than assumed.** The
brief fixed four hypotheses, alpha 0.05, and "no multiplicity correction (four pre-registered
tests, reported as such)" before any outcome was read. All four are reported here whatever they
returned, together with every exploratory contrast that was run, so there is no selection of
tests to correct for; a reader who wants a correction can apply one to a complete list. For the
record, Bonferroni over the four pre-registered tests plus the two exploratory contrasts (six)
puts the threshold at 0.0083, which the round contrast's *p* = 0.0078 clears --- and it is
confounded anyway, which is the actual objection.

Each hypothesis is reported pooled and then within each of the two outcome variables of Section
3.2, wherever the stratum contains both levels of the predictor.

**H1 --- derivations and catalogues survive more than correlations.** *Fails as stated, holds
in direction.* Pooled: n = 49; identity/taxonomy 14/43 = 0.326 (0.205--0.475), correlational
**0/6 = 0.000** (0.000--0.390); Fisher two-sided *p* = 0.1639. All six correlational rows are
standing-graded, so the test is re-runnable in one stratum only: within `survived_standing`,
10/27 = 0.370 (0.215--0.558) against 0/6 = 0.000, *p* = 0.1445. Within `survived_novelty` there
are no correlational rows and the test does not exist. Correlation is perfectly separated in
the predicted direction --- no correlational claim in this vault survived --- but six rows
cannot carry a *p*-value, and the correct statement is that no effect was *detected*.

**H2 --- famous pairings are more often prior art.** *Fails, and reverses.* Pooled: n = 82;
famous 1/11 = 0.091 (0.016--0.377) prior art, obscure 18/71 = 0.254 (0.167--0.366); *p* =
0.4430. The stratified version shows why the pooled test is nearly meaningless: PRIOR_ART is a
novelty-scale verdict, so within `survived_standing` the rate is 0/9 against 0/49 by
construction, and within `survived_novelty` it is 1/2 against 18/22 = 0.818 (0.611--0.930), *p*
= 0.3804 on two famous rows. H2 was, unrecognised at pre-registration, a hypothesis about one
of the two instruments. The famous pairs mostly ended `narrowed`, an outcome the novelty scale
cannot express.

**H3 --- claims made after blind briefs were introduced die at a higher rate.** *Falsified in
direction.* Pooled: blind brief 5/10 = 0.500 (0.237--0.763) survived against 21/72 = 0.292
(0.199--0.405) without; *p* = 0.2754. All ten brief-carrying rows are standing-graded; within
that stratum, 5/10 = 0.500 against 16/48 = 0.333 (0.215--0.470), *p* = 0.4709.

**H4 --- data joins across a scale mismatch die.** *Direction only, and the direction is
perfect.* Mismatch 0/3 = 0.000 (0.000--0.561) --- soil `T` map units against point cosmogenic
rates, half-degree cell medians, 800 CONUS points --- against same-scale 2/2 = 1.000
(0.342--1.000), site-to-site and species-to-species; *p* = 0.1000, smaller margin 2, which the
brief's own gate forbids calling evidence. Two of the five rows are standing-graded and two are
novelty-graded, so neither stratum can carry the test. It is the cleanest-looking pattern in
the dataset and the one with the least data behind it.

A logistic model was **not fitted**. The counts gate passed (n = 82, every level ≥ 5), but
`claim_kind = correlation` is completely separated on the outcome, so the maximum-likelihood
estimate does not exist and a penalised fit would report a coefficient the data do not contain.

## Two exploratory contrasts

Neither of the following was a pre-registered hypothesis. `adversarial` and `round` were both
pre-registered *predictors* --- items (e) and (h) in the hashed brief's predictor list, defined
before any outcome column was read --- but the brief named four hypotheses and neither contrast
is among them. **Both are therefore labelled exploratory, here and in the abstract.**

**The adversarial leg.** Survival with an adversarial leg (as defined in Section 2.6) 15/48 =
0.312 (0.199--0.453), without 11/34 = 0.324 (0.191--0.492); Fisher *p* = 1.0000. The difference
is **1.2 points in the unexpected direction with n = 82**, and the intervals are nested. What
the record shows instead is compositional: the leg is associated with `narrowed` rather than
with death. Stated at the strength the design supports: **on this record an adversarial leg did
not change the survival rate, and the claims that received one ended narrowed more often than
killed.** The earlier draft's bolded general finding --- "an adversarial pass is not a kill
mechanism; it is a narrowing mechanism" --- is withdrawn as over-claimed. Within strata the
sign is not even stable: `survived_novelty` 4/11 = 0.364 with against 1/13 = 0.077 without (*p*
= 0.1421); `survived_standing` 11/37 = 0.297 against 10/21 = 0.476 (*p* = 0.2558). Two
sub-samples, two opposite signs, neither significant. Only three of the 48 rows received a
*dedicated adversarial review*, and nothing here is a statement about those three.

**The round.** Post-audit (2026-09-05) claims survive 17/35 = 0.486 (0.330--0.644) against 9/47
= 0.191 (0.104--0.325) for the 2026-09-03 vault, Fisher two-sided ***p* = 0.0078**. This is the
only contrast on the record that clears alpha, and it is exploratory and confounded.

**The round confound, and what stratification does to it.** The one significant result must not
be quoted as evidence that the loop got better at making claims. Early claims were graded mostly
by the novelty audit, which hands out REPACKAGED freely; post-audit claims were graded mostly by
their own callouts and standings, which record a pre-registered result as standing *even when
the tested hypothesis failed*. A pre-registered null is therefore coded SURVIVED because its
stated result stands, while an early repackaging is coded not-survived. Section 3.2 quantifies
the overlap: 22 of the 24 novelty-graded rows are early. The referee's stratification is the
direct test of what remains, and it is now run: **within the standing-graded stratum the round
contrast persists**, 16/33 = 0.485 (0.325--0.648) against 5/25 = 0.200 (0.089--0.391), *p* =
0.0307 on n = 58. Within `survived_novelty` the contrast has two post-audit rows and is
untestable (1/2 against 4/22, *p* = 0.3804). So the effect is not *only* the instrument change
--- but the stratified test still compares 33 rows to 25 across the same day boundary, and audit
intensity changed across that boundary too: the 2026-09-05 round applied blind briefs, negative
controls and adversarial files that 2026-09-03 never faced, and those same notes carry the
highest survival. Both directions of that relationship are present in the data, and this design
cannot separate them. Re-grading a random sample of the early claims under the later rubric ---
the referee's highest-value suggestion --- would bound the remaining instrument component, and
has not been done.
<!-- C51 §5 -->

**The honest null, restated at the strength the design supports.** No subject-level predictor of
survival --- field, fame, obscurity of the anchors, presence of an adversarial leg --- was
*detected* at n = 82. Two hypotheses (H1, H4) show perfect separation in the predicted direction
on six and five rows, so the data are weakly *consistent with* subject-level prediction and not
against it. The earlier draft's "nothing about the subject of a claim predicted survival" is an
acceptance of the null from tests with power near zero, and is withdrawn.

# How it fails

A companion note catalogues **25 failure modes in six groups across 79 logged instances**, all
from 2026-09-05, the second of the two working days. Every entry is a failure the project
committed *and caught*, with how it was caught, the guard now standing, and the responsible
actor: the model, the tooling, the orchestration, or the human.

**Ownership, recounted so that it sums to 25.** The earlier draft said "the model owns 15 modes
outright, the orchestration 5, the tooling 3," which is 23 and left the fourth named actor, the
human, with no count at all. Recounting the taxonomy table's `actor` column: **the model owns 16
modes outright, the orchestration 4, the tooling 2, and 3 modes are jointly owned** --- P1
(human / model), I3 (tooling / orchestration) and Pr5 (model / human). 16 + 4 + 2 + 3 = 25.
**The human owns no mode alone and co-owns two**, P1 and Pr5, both by over-trust in a number
that arrived without a provider. Counting joint ownership as implication rather than as sole
ownership: model 18, orchestration 5, tooling 3, human 2. None of this is exculpatory, since
the orchestration chose the workload.
<!-- failure-taxonomy §"The table"; corrected 2026-09-05, see PENDING-log-REV3 -->

**It is a catalogue of modes, not a partition of events.** The modes overlap by construction:
one event can populate several. At least **three logged events populate more than one mode** ---
the 578/595 reference count is the named exemplar of **P2** and the first instance of **P1**, and
is also the entry logged as a correction of a correction under **Pr5**; C46's tautological
Σ ≡ 1 is both **I4** and, as a brief contaminated by recognition, **Pr2**; and the spent
OpenAlex daily budget is both **I3** and **Pr3**. So "79 instances across 25 modes" is a count of
**annotations, not of distinct events**, the three-most-frequent ranking is a ranking of
annotations, and no exclusivity should be read into the six groups. The count of distinct events
behind the 79 annotations was not recorded contemporaneously and is not recoverable from the log
without re-coding.

The six groups are **Provenance** (P1--P4), **Statistics** (S1--S4), **Instruments** (I1--I5),
**Reasoning** (R1--R4), **Process** (Pr1--Pr5) and **Framing** (Fr1--Fr3). The three most
frequent modes are all provenance failures:

- **P2, the unattributed count** (7 instances) --- a figure promoted without provider, endpoint
  and fetch date. Its exemplar is the 578, whose defect was attribution, not hallucination.
- **P1, two numbers in one field** (6) --- two measurements, of two objects or two runs, or of
  one work in two roles, carried as one. The 578/595 case; a gap note carrying co-citer counts
  of 8 and 5 from two runs without saying so; a note whose frontmatter says "zero in all three
  decade bins" while its own body table says 1.
- **P4, a published margin adopted as if computed** (6) --- a number the source already
  published is restated, or evaluated by hand beside a script that could have done it, and the
  agreement is called confirmation.

Deeper in the list sit the modes that killed claims rather than merely staining them: spatial
pseudoreplication with a confound already sitting in the note's own data file (S1); a check
that cannot fail reported as a passed test (I4); a positive control never run until an
adversary demanded it (I5); a metaphor mistaken for the same object (R2); a sign error pointing
at the hoped-for result (R3). Several of the prior-art deaths have the same shape --- a
cross-domain ratio the project built from scratch turned out to be mainstream soil science,
already published as tolerable-versus-actual erosion [@verheijen2009] and as a dimensioned soil
lifespan over 10,030 plot-years [@evans2020], with the site-level version of the same
comparison also prior art [@quarrier2023]; and a survival claim for hibernating mammals was
already established under phylogenetic GLS [@turbill2011].
<!-- novelty-audit C35/C42/C43 row; C52 §grade table -->
Prior art of this kind is the second-largest outcome class on the record, at 19 of 82.

## The catch table

Counting by *earliest* catch across the 25 modes. The denominator column is the exposure ---
how many claims, notes, commits, clusters or runs the guard was actually applied to --- because
without it the tally compares a guard that ran hundreds of times to one that ran three times.
The units in that column are not commensurable with each other, so the column is a statement of
asymmetry, not a rate to be divided across rows.

: Guards, by earliest catch, with exposures. <!-- failure-taxonomy §"What the guards cost";
exposures counted at commit f1faab3 -->

| guard | modes caught first | applied to (exposure) | cost |
|---|---|---|---|
| provenance audit (re-fetch every number with provider and date) | 11 | all 87 coded notes, over 7 audit reports | moderate, mechanical |
| dedicated adversarial review | 7 | 3 claim clusters | expensive |
| replication, positive and negative controls, forward simulation | 3 | 5 runs (C47, C33, C46, C50, C45) | most expensive |
| script self-test and calibration query | 2 | 2 instrument adapters | minutes each |
| the pre-registration itself | 1 | 12 blind briefs | cheap |
| the human, watching the loop | 1 | continuous; no denominator | --- |
| schema lint (`_lint.py`) | **0** | 89 commits × ~140 notes | under one second |

Three readings follow, the first of them narrowed from what the earlier draft claimed.
**Schema linting does not substitute for semantic auditing.** The linter caught zero of the 25
modes --- the number stands, and it was checked --- but that zero is a **selection effect and
not an efficacy result**: `_lint.py` validates frontmatter vocabulary, field types and wikilink
reachability, and all 25 modes are semantic (provenance, statistics, instruments, reasoning,
process, framing). A guard scoring zero on a class of failure it is not designed to detect has
been shown to have the wrong scope, not to be worthless; the linter also ran on a denominator
three orders of magnitude larger than the adversary's, at a cost three orders of magnitude
smaller. The useful reading is the narrow one, and the earlier draft's "the cheap automated
guard caught nothing" is withdrawn as bigger than the design supports. Its one contribution was
surfacing a half-landed parallel edit as a dead link. The **cheapest effective guards have the
best ratio on the record**: a script self-test and a calibration query --- a term whose answer
*cannot* be zero --- cost minutes each and caught the two failures that would have manufactured
the most claims, namely ten phantom bridges from a blank key and ten fake zeros from an
endpoint that silently ignores a query prefix. And the **adversary is the only guard that
caught the fatal ones**: the pseudoreplication that killed a site-level correlation, the sign
error that killed a fatigue leg, the metaphor that mis-titled a gap. Adversaries cannot be run
on everything, so *what they are pointed at is the orchestrator's most consequential decision
of the day.*

## The unguarded modes

Three modes have **no guard at all**. **Pr2**, the single-agent blind --- hashing removes
pre-announcement but not recognition, and the fix is named and unrun. **Pr4**, stale watchers
and notification loops, where orchestration keeps watching artifacts and sessions whose state
has moved and re-reports finished work as new; this one has *no vault note*, which is the
finding: the failures a record can enumerate are the ones some agent was asked to write down.
And the **frontmatter-versus-body half of P1** --- nothing checks a note's machine fields
against its own prose.

# Five rules for running agents on science

Reproduced verbatim from the taxonomy.
<!-- failure-taxonomy §"For anyone running agents on science" -->

1. **A number without a provider, an endpoint and a fetch date is not a number.** An
   unattributed 578 and an unattributed 595 fail the same rule.

2. **A zero from an instrument is a claim about the instrument until it is calibrated.** Run a
   query whose answer cannot be zero, print what the adapter dropped, and record a failed fetch
   as `err`.

3. **Fix the analysis before you see the data, and archive the brief with a hash.** On one
   soil-erosion join the declustering unit alone moves ρ from −0.18 to +0.02, so any such
   choice made after the fact is not a result.

4. **Point the instrument at a case whose answer you already know, in both directions.** A
   check that cannot fail has told you nothing, and an instrument that has never returned
   "nothing here" is exercised, not validated.

5. **A correction is a claim, and concurrency is a source of error.** Hold a withdrawal to the
   standard of what it withdraws; give every file and every quota one owner per round.

Rules 1 and 5 are corollaries of one another: the "46 was stale" retraction failed rule 5
because it failed rule 1 in the withdrawing direction.

# Related work

Nothing in the first draft placed 0.317 against a published number, and a reader was handed a
rate with no yardstick. There is no exact comparator --- no other complete audit of an agentic
pipeline's whole claim output --- but there are three literatures that bound the question, and
the honest statement is what each one is *not*.

**Reproducibility base rates** are the natural yardstick for "a third of claims stood". The
large replication projects report outcomes in the same broad territory: the Open Science
Collaboration replicated 100 psychology studies and found 36 of 97 replications reaching
statistical significance against 97% of the originals [@osc2015], and the Reproducibility
Project: Cancer Biology reports substantially attenuated effects across the preclinical
experiments it could repeat at all [@errington2021]; the theoretical case for why a high failure
rate is the expected state of any exploratory literature is Ioannidis's [@ioannidis2005]. Those
rates are quoted as their own abstracts report them and were not recomputed here. **AI-for-science
outcome reports** are the closest thing to a comparator in kind. Automated-discovery pipelines
report reviewer-scored outputs on generated papers [@lu2024]; the controlled human study of
LLM-generated research ideas finds them judged *more novel* than expert-written ideas and no
better on feasibility [@si2024]; and the 2025 follow-up, which had those ideas actually executed
and audited, finds the novelty advantage does not survive execution [@si2025] --- which is the
same shape as this record's 19/82 PRIOR_ART and its narrowing-as-modal-outcome. **The caveat that
governs all of it: none of these is the same outcome.** A psychology replication is a
pre-registered repeat of an experiment against a fresh sample; a reviewer score is a judgement of
a manuscript; this paper's 0.317 is "the headline sentence still stands after an internal audit
of the same project's own record, having never left Layer 2 of its ladder". They are three
different objects, and 0.317, 0.37 and a reviewer score cannot be subtracted from one another.
What the comparison does establish is that a third of claims standing is not anomalous, in either
direction, against what published research reports about itself --- so the interesting content of
this record is not the rate but the failure taxonomy and the guard-cost accounting, for which no
base rate exists at all.

# Limitations

**One project, two working days, one orchestrator, one model family.** The 82 graded claims come
from a single vault and were produced or re-graded on 2026-09-03 and 2026-09-05; the 79 failure
instances are all from the second of those two days. Both were produced under one orchestration
policy using Anthropic models only. Nothing here generalises past this repository
without replication elsewhere.

**The coder of outcomes is an agent, and it is not blind to outcome.** Every predictor was
defined and hashed before an outcome column was read, and the predictors are mostly structural
facts about a note --- its move, its date, whether a brief file exists. But the two
judgement-bearing predictors (`famous`, `move`) were coded by an agent that had already read
the notes. <!-- C51 §5 -->

**Survival is relative to an audit whose strength changed between the two days.** That is the
round confound of Section 4. Stratifying by grading source removes part of it and the contrast
survives within the standing-graded stratum, but the design still cannot separate "later claims
were better" from "later claims faced a stronger audit."

**Layer 4 was never reached.** The depth gate held the project at Layer 2, so no claim in this
record was tested against the world. "Survival" here means survived internal audit by the same
system that produced the claim, and a reader importing the ordinary meaning --- external
replication --- will read 0.317 as a stronger number than it is.

**The direction of the remaining biases is not symmetric.** The author is the operator of the
system under study; the agent family that produced the claims also coded their outcomes, wrote
the taxonomy, drafted the rules and drafted this manuscript. The plausible direction of each is
favourable to the system: an unblinded coder that has read the notes resolves borderline rows
toward the project's preferred reading; a taxonomy written by the kind of agent that committed
the failures is blind where that kind of agent is blind (most plainly at Pr4, whose single
instance exists only because a human noticed); a floor count of failure modes with no
denominator understates the failure rate by an unknown factor; and the guard-attribution table
was reconstructed after the fact, by the beneficiary, with no contemporaneous field recording
which guard fired first. The inference the record supports is: *within this repository, on these
two days, these rows were coded this way.* It supports no statement of the form "AI-generated
research claims survive at rate X."

**The sample of claims is not random.** It is the complete output of one inquiry choosing its
own questions under a scope rule, so the mix of move types is a property of the orchestrator's
choices, not of AI-generated research in general. Eight rows carry an explicit `AMBIGUOUS` flag
and were marked rather than resolved.

**The recurrence counts are of caught failures, not committed ones.** There is no denominator
of failures attempted, so "25 modes" describes the 2026-09-05 harvest and the list is a floor. The
taxonomy was written by an agent of the same kind that committed the failures, reading a log
the same kind of agent wrote; it is blind in the way its own modes predict, most plainly at
Pr4, whose single instance exists only because a human watched the loop.

**No human-only baseline exists.** Nothing here says whether 26/82 is a good survival rate. A
comparable audit of an unassisted researcher's one-day claim output, graded by the same
vocabulary, has not been run --- and until it is, the kill rate is a description of this loop,
not a comparison.

# Use of AI tools

This work was produced with substantial use of large language models, disclosed here per ICMJE
guidance [@icmje2026] (Section V, "Use of Artificial Intelligence in Publishing"; the page was
fetched 2026-09-05, returns HTTP 200 and carries "Updated January 2026") and consistently with
publisher policy that AI tools cannot be authors [@nature2023]. The models are not authors and bear no responsibility for the
content. Claude Fable 5.1 (Anthropic, model `claude-fable-5-1`) acted as orchestrator: it
reviewed the vault, designed the audits and task briefs, integrated results, and drafted this
manuscript's structure. Claude Opus 4.8 (Anthropic) instances, run through Claude Code, carried
out the derivations, the literature and citation-database queries, the prior-art searches, the
statistical coding, and the first draft of the text, each under a written brief and each
reporting sources with provider and fetch date. The coding of claim outcomes analysed in
Section 4 was performed by such an agent; this is stated as a limitation in Section 8 rather
than as a footnote. Every query, count, and correction is logged in the vault (`vault/log.md`,
`audits/`). The author set the research question, the scope rule, and the standards of
evidence; chose which results to keep, downgrade, or withdraw; and reviews and takes full
responsibility for every claim and citation in this paper. No AI tool was used to generate or
alter data.

**Who fixed the ID set.** The frame of Section 3.1 was written by the orchestrator into
`audits/blind-brief-c51-2026-09-05.md` and hashed before any outcome was read; it is a
mechanical enumeration of the notes that existed (every `computed/C*.md`, every `gaps/G*.md`,
Q1--Q10), not a selection, and the author confirmed it before dispatch. No model chose which
claims entered the set.

**Which text is model-drafted.** All of it, in first draft: the orchestrator drafted the
structure and an executing agent drafted the prose, both under written briefs. The author
revised, cut and approved every sentence and is responsible for all of them. The revision
answering the first referee report was drafted the same way, from the referee's own text. Since
the manuscript's rhetorical framing is part of the object under study, the reader should assume
that any sentence here that flatters the loop was written by the loop.

# Data availability

Every number in this paper is traceable to a note in a public research vault, and each carries
the note ID in an HTML comment in the manuscript source.

**Pinned snapshot.** Repository <https://github.com/deciduus/same-object>, commit
**`f1faab396bf80c7dc6eb8a8eef86a935e23c46fe`** (short `f1faab3`). Every hash below is a sha256 of
the file's bytes as they stand in that tree, computed 2026-09-05, except the two files this
revision edits, which are given twice: as committed at `f1faab3`, and as they stand in the
revision. **Archived snapshot: Zenodo version DOI `10.5281/zenodo.22334048` (v0.1.0), which is
the citable, fixed record; the concept DOI `10.5281/zenodo.22334047` resolves to the latest
release and is a moving target** [@vault]. Cite the version DOI. Licence: CC-BY-4.0.

: Load-bearing files, sha256 at commit `f1faab3`.

| file | sha256 | bytes |
|---|---|---|
| `vault/_scripts/c51_data/claims.csv` | `df21dd8e6d87c03970bbbd1e1a48074e853375c4cf0d0d8e9a8eea25070811a6` | 15,619 |
| `vault/method/failure-taxonomy.md` (at `f1faab3`) | `f70b687f3a806b4d78aec4043fc9baa37b02f118f9f0ee485dfb5ee6407889cc` | 22,505 |
| `vault/method/failure-taxonomy.md` (this revision) | `51c0da83f6635f84833aafdf0af6e46943a9d55a51c86a8748dd9030fef06112` | 25,250 |
| `vault/computed/C51-vault-meta-analysis.md` (at `f1faab3`) | `1be02158ebd15835bb5e98d47d1c3c60eb4aece97b92d29c6cfa4cb478f39489` | --- |
| `vault/computed/C51-vault-meta-analysis.md` (this revision) | `9910168badbcdfa9535a15ba623a13a9d2d10cd117eac09a67f6ce7aad6036d4` | 14,348 |
| `vault/log.md` | `7f7660815bc109a0c750aee3a59817c7a8d79bf7143d18c75242f8f3b734f84a` | 379,441 |

: The twelve blind briefs, sha256 at commit `f1faab3`. Each was hashed before dispatch; the C51
entry is the pre-registration token quoted in Section 3.4.

| brief | sha256 | bytes |
|---|---|---|
| `audits/blind-brief-c39-2026-09-05.md` | `e719611401c58b1269e5368b970ce3b05ecbd2c76d5eb4d76e8d1ccc33e4ef93` | 4,859 |
| `audits/blind-brief-c40-2026-09-05.md` | `9cf0f0cbdc03425b5e5d597a355299fcc03d058c00e4f8f3de75357034113e9c` | 7,977 |
| `audits/blind-brief-c43-2026-09-05.md` | `dbae0496666126c4070f518f16d1bf997f6c6b9165469284f940440b5e7ef727` | 6,953 |
| `audits/blind-brief-c44-2026-09-05.md` | `724ae9034bbc61761dad85b1c32ea32479708f4098e51a76b9e94634e806ab6b` | 9,310 |
| `audits/blind-brief-c45-2026-09-05.md` | `fbc48359b5215f6a3f2c4f6cefee4ce7a73257c7c8121c33ef8615f0d49714a7` | 5,661 |
| `audits/blind-brief-c46-2026-09-05.md` | `4d16ca706dd9709f53150c844e772c337e07d750ad62c3c4e83c71adb9cf7a71` | 999 |
| `audits/blind-brief-c47-2026-09-05.md` | `13a3dad415f32d327eb9666111e0c5268d380cbdd543730ae5e5077cfe6daad6` | 8,694 |
| `audits/blind-brief-c48-2026-09-05.md` | `4e6fe72f283fe1eb074d8f2f3e8e7f17b1b4a35ad640751360df7422b2941572` | 7,632 |
| `audits/blind-brief-c49-2026-09-05.md` | `31c4712ab7aabe39d5eb367810090df4266a9b258847c3c97bf0a7e793678bfa` | 1,182 |
| `audits/blind-brief-c50-2026-09-05.md` | `c6a1d7806b3578ed0846d47ff38bf2d1f0887f4202b00170e20b46cba7eb2712` | 991 |
| `audits/blind-brief-c51-2026-09-05.md` | `8844d375b302b987d7bc83ebbb8f2e4157f26df7f93fd7bcdc6517ac697d786a` | 5,550 |
| `audits/blind-brief-c52-2026-09-05.md` | `bc2259e6984a3895a199f3585dc11ffad496162af7a50cb65c79948cac9f2547` | 14,767 |

What each object carries: `C51-vault-meta-analysis.md` --- the outcome coding, the two outcome
variables, the four pre-registered tests, the two exploratory contrasts and the round confound.
`claims.csv` --- 87 rows, one per claim, each with a `source_line` naming the file and line where
the outcome was read; the `source_line` column is also what the `survived_novelty` /
`survived_standing` split is computed from. Re-runnable with `python vault/_scripts/c51_meta.py`
from `vault/`. `failure-taxonomy.md` --- the 25 modes, the ownership recount, the overlap
statement, the catch table with exposures, and the five rules. `log.md` --- the 252 dated
entries, including both corrections of corrections. `vault/novelty-audit.md` --- the novelty
grade tables. `vault/predictions.md` --- the hash-stamped prediction register.
`audits/c43-adversarial.md`, `audits/g34-adversarial.md`, `audits/g36-adversarial.md` --- the
three dedicated adversarial reviews.

**Reference verification policy.** Every entry in `refs.bib` carries a `note` recording how it
was checked. "verified Crossref 2026-09-05" means the DOI was resolved at
`api.crossref.org/works/{doi}?mailto=deciduusleaf@gmail.com` on that date and authors, title,
venue, volume, issue, pages and year were compared field-by-field against the returned record.
Three arXiv preprints are not in Crossref and were verified against the arXiv API
(`export.arxiv.org/api/query?id_list=...`) on the same date. The ICMJE page was fetched directly.
No DOI, page range or ISBN in the file was constructed, guessed or inferred from a pattern. One
entry remains unverifiable by fetch: `paper1`, the companion Charnov--Gittins manuscript, which
is unpublished and unposted as of 2026-09-05 and is cited here as a manuscript in preparation
[@paper1]; no claim in this paper rests on it.

# Declarations

**Competing interests.** The author declares a competing interest of a kind that is not pro
forma: he is the operator and sole author of the system under audit, the vault is his own
project, and every favourable reading in this paper accrues to him. The models used are
commercial products of a vendor with which the author has no financial relationship beyond
ordinary paid subscription access; the vendor had no role in the design, analysis, or drafting,
and did not see the manuscript. No other competing interests.

**Funding.** None. No grant, institutional, or commercial funding supported this work.

**Author contributions.** Single author. Landon Holden set the research question, the scope rule
and the standards of evidence; fixed the ID set; decided what was kept, narrowed or withdrawn;
revised and approved the manuscript; and takes responsibility for every claim and citation in
it. Large language models performed orchestration, execution and first drafting as described in
Section 6; per ICMJE [@icmje2026] and publisher policy [@nature2023] they are not authors and
are named as tools, not contributors.

**Ethics.** Not applicable. The study involves no human or animal subjects, no personal data,
and no intervention; its unit of analysis is a research note in the author's own public
repository.

# References
