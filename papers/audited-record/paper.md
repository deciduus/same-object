---
title: |
  What survives: an audited record of 82 AI-generated cross-domain research claims
author:
  - Landon Holden
date: 2026-09-05
abstract: |
  One human set the scope rule and the standards of evidence; Claude Fable 5.1 orchestrated;
  Claude Opus 4.8 agents executed under written briefs; the output is a public vault with
  lint-enforced schema and per-number provenance. This paper audits that record rather than
  advertising it. Of 87 headline claims coded on 2026-09-05, 82 were gradable: 26 survived
  (0.317), 26 were narrowed, 19 were prior art, 11 were withdrawn. The log carries 245 dated
  entries, 93 of them corrections, one an explicit correction of a correction. Twelve blind
  briefs were archived with sha256 hashes before dispatch; two are contaminated by recognition
  rather than by pre-announcement. Three adversarial reviews were run. No subject-level
  predictor of survival held: correlational claims survived 0/6, scale-mismatched data joins
  0/3, the famous-pair hypothesis reversed, and running an adversary changed survival by 1.2
  points. The only significant variable was *when* a claim was made, and that result is
  confounded with how the outcome was read. A companion taxonomy records 25 failure modes over
  79 logged instances; provenance modes dominate. Earliest catches: audit 11, adversary 7,
  replication and controls 3, self-test 2, pre-registration 1, the human 1, schema lint 0.
bibliography: refs.bib
csl-refs: true
---

<!-- AUTHOR: insert affiliation, ORCID and corresponding-author email in the YAML header
     above before submission. -->

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

Two results are worth stating at the front. First, **nothing about the subject of a claim
predicted whether it survived.** <!-- C51 §2 --> Second, **the cheap automated guard caught
nothing**: a schema linter that blocks commits in under a second caught zero of the 25 failure
modes, while the mechanical provenance audit caught 11 and one adversarial agent per claim
caught the three that were fatal. <!-- failure-taxonomy §"What the guards cost" -->

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
denominator-invariant control ratio. This addresses a standing complaint that LBD evaluation
lacks controls. The instrument's own failure modes are documented rather than assumed away: an
empty key field that inflates every set built the same way by exactly one; an endpoint that
returns 0 for every query, including one whose answer cannot be zero; and a provider's spent
daily budget recorded as though it were a property of the literature.
<!-- failure-taxonomy I1--I3 -->

## The blind-brief protocol

Twelve blind briefs were written, archived and sha256-hashed **before dispatch** to the
executing agent, covering claims C39--C52. <!-- audits/blind-brief-*.md, 12 files --> Each
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

Three claim clusters were given a dedicated adversarial agent-round whose brief was to kill the
claim: `audits/c43-adversarial.md`, `audits/g34-adversarial.md`, `audits/g36-adversarial.md`.
An adversarial pass is expensive --- a full agent round against one cluster --- and was
therefore pointed, not universal.

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

: Outcomes, all coded claims (n = 87). <!-- C51 §1 -->

| outcome | n |
|---|---|
| SURVIVED | 26 |
| NARROWED | 26 |
| PRIOR_ART | 19 |
| WITHDRAWN | 11 |
| ungraded (open questions) | 5 |

Overall survival is **26/82 = 0.317**. The single most common fate is not death but
*narrowing*: 26 of 82 claims still stand in reduced form. This is the least-discussed outcome
in AI-for-science reporting and, on this record, the modal one.

Broken out by move type (graded rows only, n = 82):

: Survival by move type. Not a pre-registered test; no *p*-values are claimed and four of the
eight cells have n ≤ 5. <!-- C51 §3; claims.csv -->

| move | survived | narrowed | prior art | withdrawn | n | rate |
|---|---|---|---|---|---|---|
| catalogue (pre-registered enumeration) | 5 | 0 | 1 | 1 | 7 | 0.714 |
| instrument run | 3 | 1 | 1 | 0 | 5 | 0.600 |
| data join | 2 | 0 | 1 | 2 | 5 | 0.400 |
| derivation / proof | 5 | 0 | 9 | 1 | 15 | 0.333 |
| citation comparison | 8 | 19 | 1 | 2 | 30 | 0.267 |
| computation on published numbers | 3 | 4 | 6 | 3 | 16 | 0.188 |
| replication | 0 | 2 | 0 | 1 | 3 | 0.000 |
| simulation | 0 | 0 | 0 | 1 | 1 | 0.000 |

The shape is legible even without inference. Moves whose *output is a specification or a count
that is true whichever way the world turns* --- pre-registered enumerations, instrument runs
--- sit at the top; there is no number for an audit to take away. Re-deriving a figure from a
published paper's own numbers sits near the bottom, at 3/16, and it is the move that produced a
withdrawn hormesis window, a withdrawn starvation probability, and a struck headline.
<!-- C51 §4 -->

## Corrections

`vault/log.md` holds **245 dated entries**, 30 under 2026-09-03 and 215 under 2026-09-05.
Ninety-three carry a `kind` containing "correction" (73 `correction`, 19 `correction
(archived)`, 1 `correction of a correction`); the remainder are `method` (40), `computed` (27),
`verification` (25), `honest null` (11), `gap` (9) and smaller kinds.
<!-- log.md, entry headers, counted 2026-09-05 -->

Two entries are corrections *of* corrections, and they are the most instructive rows in the
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

Twelve blind briefs are on file, one per claim C39--C52, each sha256-hashed before dispatch.
The meta-analysis reported in Section 4 is one of them:
`audits/blind-brief-c51-2026-09-05.md`, hash
`8844d375b302b987d7bc83ebbb8f2e4157f26df7f93fd7bcdc6517ac697d786a`, hashed before any outcome
column was read or coded. <!-- C51 header --> Ten of the 82 graded claims carry a brief; the
other 72 predate the protocol. Separately, a `predictions.md` register holds dated,
sha256-stamped prediction texts. It exists because the project's first thirty log entries all
carry one date, and a same-day record cannot demonstrate that a prediction preceded its
confirmation --- which is the one thing a dated prediction is for.
<!-- predictions.md header -->

# What predicts survival

Four hypotheses were pre-registered. Three fail and the fourth is direction-only.
<!-- C51 §2 -->

**H1 --- derivations and catalogues survive more than correlations.** *Fails as stated, holds
in direction.* n = 49; identity/taxonomy claims 14/43 = 0.326, correlational claims **0/6 =
0.000**; Fisher two-sided *p* = 0.1639. Correlation is perfectly separated --- no correlational
claim in this vault survived --- but six rows cannot carry a *p*-value.

**H2 --- famous pairings are more often prior art.** *Fails, and reverses.* n = 82; famous
1/11 = 0.091 prior art, obscure 18/71 = 0.254; *p* = 0.4430. The famous pairs mostly ended
`narrowed`; it was the obscure pairs whose computations turned out to be textbook.

**H3 --- claims made after blind briefs were introduced die at a higher rate.** *Falsified in
direction.* Blind brief 5/10 = 0.500 survived against 21/72 = 0.292 without; *p* = 0.2754. The
broader form of the same variable is the only significant result on the record: post-audit
(2026-09-05) claims survive 17/35 = 0.486 against 9/47 = 0.191 for the 2026-09-03 vault, Fisher
two-sided ***p* = 0.0078**.

**H4 --- data joins across a scale mismatch die.** *Direction only, and the direction is
perfect.* Mismatch 0/3 (soil `T` map units against point cosmogenic rates, half-degree cell
medians, 800 CONUS points), same-scale 2/2 (site-to-site, species-to-species); *p* = 0.1000
with a smaller margin of 2, which the brief's own gate forbids calling evidence. It is the
cleanest-looking pattern in the dataset and the one with the least data behind it.

A logistic model was **not fitted**. The counts gate passed (n = 82, every level ≥ 5), but
`claim_kind = correlation` is completely separated on the outcome, so the maximum-likelihood
estimate does not exist and a penalised fit would report a coefficient the data do not contain.

**The honest null.** Nothing about the *subject* of a claim --- its field, its fame, whether
its anchors were obscure, whether an adversary was pointed at it --- predicted survival.
Running an adversarial pass changed the survival rate by **1.2 points**: 15/48 = 0.312 with,
11/34 = 0.324 without. What adversarial passes did instead was convert `live` into `narrowed`.
**An adversarial pass is not a kill mechanism; it is a narrowing mechanism.**

**The round confound, stated as the source states it.** The one significant result must not be
quoted as evidence that the loop got better at making claims. Early claims were graded mostly
by the novelty audit, which hands out REPACKAGED freely; post-audit claims were graded mostly
by their own callouts and standings, which record a pre-registered result as standing *even
when the tested hypothesis failed*. A pre-registered null is therefore coded SURVIVED because
its stated result stands, while an early repackaging is coded not-survived. That is a
defensible reading of "survived adversarial review", and it is also exactly the kind of reading
that could manufacture *p* = 0.0078. Compounding it: survival is a function of audit intensity,
which changed *within the day* --- the 2026-09-05 round applied blind briefs, negative controls
and adversarial files that 2026-09-03 never faced, and those same notes carry the highest
survival. Both directions of that relationship are present in the data, and this design cannot
separate them. <!-- C51 §5 -->

# How it fails

A companion note catalogues **25 failure modes in six groups across 79 logged instances**, all
from one day. Every entry is a failure the project committed *and caught*, with how it was
caught, the guard now standing, and the responsible actor: the model, the tooling, the
orchestration, or the human. Ownership across the 25: the model owns 15 modes outright, the
orchestration 5, the tooling 3 --- not exculpatory, since the orchestration chose the workload.
<!-- failure-taxonomy header and table -->

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

Counting by *earliest* catch across the 25 modes:

: Guards, by earliest catch. <!-- failure-taxonomy §"What the guards cost" -->

| guard | modes caught first | cost |
|---|---|---|
| provenance audit (re-fetch every number with provider and date) | 11 | moderate, mechanical |
| one adversarial agent per claim | 7 | expensive |
| replication, positive and negative controls, forward simulation | 3 | most expensive |
| script self-test and calibration query | 2 | minutes each |
| the pre-registration itself | 1 | cheap |
| the human, watching the loop | 1 | --- |
| schema lint (`_lint.py`) | **0** | under one second |

Three readings follow. The **schema linter caught nothing**: it blocks a commit on frontmatter
drift in under a second, and zero of the 25 modes were caught by it; its one contribution was
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

# Limitations

**One project, one day, one orchestrator, one model family.** The 82 graded claims come from a
single vault, the 79 failure instances from a single date, and both were produced under one
orchestration policy using Anthropic models only. Nothing here generalises past this repository
without replication elsewhere.

**The coder of outcomes is an agent, and it is not blind to outcome.** Every predictor was
defined and hashed before an outcome column was read, and the predictors are mostly structural
facts about a note --- its move, its date, whether a brief file exists. But the two
judgement-bearing predictors (`famous`, `move`) were coded by an agent that had already read
the notes. <!-- C51 §5 -->

**Survival is relative to an audit whose strength changed during the day.** That is the round
confound of Section 4; the design cannot separate "later claims were better" from "later claims
were graded by a different instrument."

**The sample of claims is not random.** It is the complete output of one inquiry choosing its
own questions under a scope rule, so the mix of move types is a property of the orchestrator's
choices, not of AI-generated research in general. Eight rows carry an explicit `AMBIGUOUS` flag
and were marked rather than resolved.

**The recurrence counts are of caught failures, not committed ones.** There is no denominator
of failures attempted, so "25 modes" describes one day's harvest and the list is a floor. The
taxonomy was written by an agent of the same kind that committed the failures, reading a log
the same kind of agent wrote; it is blind in the way its own modes predict, most plainly at
Pr4, whose single instance exists only because a human watched the loop.

**No human-only baseline exists.** Nothing here says whether 26/82 is a good survival rate. A
comparable audit of an unassisted researcher's one-day claim output, graded by the same
vocabulary, has not been run --- and until it is, the kill rate is a description of this loop,
not a comparison.

# Use of AI tools

This work was produced with substantial use of large language models, disclosed here per ICMJE
and COPE guidance [@icmje2025]. The models are not authors and bear no responsibility for the
content. Claude Fable 5.1 (Anthropic, model `claude-fable-5-1`) acted as orchestrator: it
reviewed the vault, designed the audits and task briefs, integrated results, and drafted this
manuscript's structure. Claude Opus 4.8 (Anthropic) instances, run through Claude Code, carried
out the derivations, the literature and citation-database queries, the prior-art searches, the
statistical coding, and the first draft of the text, each under a written brief and each
reporting sources with provider and fetch date. The coding of claim outcomes analysed in
Section 4 was performed by such an agent; this is stated as a limitation in Section 7 rather
than as a footnote. Every query, count, and correction is logged in the vault (`vault/log.md`,
`audits/`). The author set the research question, the scope rule, and the standards of
evidence; chose which results to keep, downgrade, or withdraw; and reviews and takes full
responsibility for every claim and citation in this paper. No AI tool was used to generate or
alter data.

# Data availability

Every number in this paper is traceable to a note in a public research vault, and each carries
the note ID in an HTML comment in the manuscript source. The load-bearing objects are:

- `vault/computed/C51-vault-meta-analysis.md` --- the outcome coding, the four pre-registered
  tests, the honest null and the round confound.
- `vault/_scripts/c51_data/claims.csv` --- 87 rows, one per claim, each with a `source_line`
  naming the file and line where the outcome was read. Re-runnable with
  `python vault/_scripts/c51_meta.py` from `vault/`.
- `vault/method/failure-taxonomy.md` --- the 25 modes, the catch table, and the five rules.
- `vault/log.md` --- the 245 dated entries, including both corrections of corrections.
- `vault/novelty-audit.md` --- the novelty grade tables.
- `vault/predictions.md` --- the hash-stamped prediction register.
- `audits/blind-brief-*.md` --- the twelve pre-registrations (C39--C52), each sha256-hashed
  before dispatch; `audits/c43-adversarial.md`, `audits/g34-adversarial.md`,
  `audits/g36-adversarial.md` --- the three adversarial reviews.

Repository: <https://github.com/deciduus/same-object>. Archived snapshot, Zenodo concept DOI:
`10.5281/zenodo.22334047` [@vault]. Licence: CC-BY-4.0. A companion manuscript reporting the
one result that survived every audit is at `papers/charnov-gittins/paper.md` in the same
repository [@paper1].

# References
