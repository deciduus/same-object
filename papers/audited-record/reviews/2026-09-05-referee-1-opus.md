# Referee report 1

**Manuscript:** "What survives: an audited record of 82 AI-generated cross-domain research claims"
**Referee:** anonymous, meta-research / research-integrity methods
**Date:** 2026-09-05
**Materials seen:** `papers/audited-record/paper.md`, `papers/audited-record/refs.bib`. Nothing else. I did not consult the vault, so every check below is internal to the manuscript.
**Recommendation:** Major revision.

---

## 1. Summary of claims

The authors audit the complete claim output of a single human-scoped, LLM-orchestrated cross-domain synthesis project, coding 87 headline claims (82 gradable) as survived / narrowed / prior art / withdrawn and reporting a 26/82 = 0.317 survival rate, with narrowing rather than death as the modal outcome. They report four pre-registered hypotheses about what predicts survival — claim kind, fame of the anchor pairing, presence of a blind brief, scale mismatch in data joins — all of which fail or are direction-only, and conclude an "honest null": nothing about a claim's subject predicted its fate, with the only significant variable being the audit round, which the authors themselves declare confounded with how outcomes were graded. A companion taxonomy of 25 failure modes over 79 instances is summarised, together with a table attributing each mode to the guard that caught it first, from which the authors draw the headline that the sub-second schema linter caught nothing while an adversarial agent caught all the fatal errors, and five practice rules.

## 2. Internal consistency

I recomputed every rate and every table total from the paper's own figures.

**What is correct.** The move-type table (§3.1) is internally exact: all eight row sums match the stated `n`; all eight rates match; the four outcome columns total 26 / 26 / 19 / 11; the `n` column totals 82. The outcome table sums to 87 with 5 ungraded. 26/82 = 0.3171. The ID arithmetic 48 + 29 + 10 = 87 holds. Every 2×2 in §4 partitions correctly: H2 11 + 71 = 82 and 1 + 18 = 19 (matching the prior-art total); H3 10 + 72 = 82 and 5 + 21 = 26; the round split 35 + 47 = 82 and 17 + 9 = 26; the adversary split 48 + 34 = 82 and 15 + 11 = 26; H1 43 + 6 = 49; H4 3 + 2 = 5, which matches the data-join row (n = 5, 2 survived). All quoted proportions round correctly (0.326, 0.091, 0.254, 0.500, 0.292, 0.486, 0.191, 0.312, 0.324), and the "1.2 points" adversary delta is right. The Fisher *p* = 0.1000 for H4 is the correct exact two-sided value for [[0,3],[2,0]]. The log split 30 + 215 = 245 and the correction split 73 + 19 + 1 = 93 both hold. The catch table sums to 25, matching the 25 modes. The six failure groups sum to 25 (4+4+5+4+5+3).

**Mismatches, in order of seriousness.**

1. **Three adversarial reviews vs. 48 claims with an adversarial pass.** §2.6 states that exactly three claim clusters received a dedicated adversarial round, and names the three files; the abstract repeats "Three adversarial reviews were run." §4 then reports survival "15/48 = 0.312 with, 11/34 = 0.324 without" an adversarial pass. Three cannot become 48 without an unstated coding rule (cluster membership? any critical pass? the whole 2026-09-05 round?). As written, the paper's single most quotable operational result — "an adversarial pass is not a kill mechanism; it is a narrowing mechanism" — rests on a predictor whose definition contradicts the methods section. This must be defined explicitly, and if `adversary` is in fact a proxy for the 2026-09-05 round, it is collinear with the one significant variable and the sentence must be withdrawn.

2. **One correction of a correction, or two?** The abstract says "one an explicit correction of a correction"; the `kind` tally in §3.2 gives exactly 1 such entry; §3.2's next paragraph says "Two entries are corrections *of* corrections" and narrates both (the 578/595 case and the Alexander-1997 "46 was stale" reversal). Pick one and reconcile the tally.

3. **One day or two.** §1 says the graded work was "produced or re-graded on two days, 2026-09-03 and 2026-09-05," and the log is split across both. §7 says "One project, one day," and §5 says the 79 failure instances are "all from one day." The limitation is presumably about the taxonomy only; as written the two statements contradict.

4. **Twelve briefs for fourteen IDs.** §2.5 and §3.3 both say "twelve blind briefs ... one per claim C39--C52." C39 through C52 inclusive is fourteen IDs. Separately, §3.3's "Ten of the 82 graded claims carry a brief" is reconcilable only if C51 and C52 fall outside the graded ID set (C1--C22, C25--C50) — which they do, but the paper never says so, and it simultaneously cites C52 as a graded row in §5 ("C52 §grade table"). State the mapping explicitly.

5. **Failure-mode ownership sums to 23, not 25.** §5: "the model owns 15 modes outright, the orchestration 5, the tooling 3." That is 23. The same sentence names four possible actors including "the human," who receives no count. Two modes are unaccounted for.

6. **The `kind` tally leaves 40 entries in "smaller kinds."** 245 − 93 = 152; the enumerated remainder (method 40, computed 27, verification 25, honest null 11, gap 9) is 112. Forty entries — 16% of the log — are invisible. Give the full distribution or a tail count.

7. **Silent gaps in the population.** C23 and C24 are excluded without comment, and "G1--G37 as they exist (29)" means eight G IDs are absent, also without comment. For a paper whose claim to authority is completeness, ten silently missing IDs need one sentence each.

## 3. Design validity

**Survival is not a defined outcome; it is a moving target, and the paper says so.** Nowhere are SURVIVED, NARROWED, PRIOR_ART and WITHDRAWN given operational definitions. §3.1 defines what a *claim* is (one headline sentence) and then never defines the levels. Worse, §4's round-confound paragraph states in plain terms that the definition *changed within the sample*: early claims were graded off novelty grades (which "hand out REPACKAGED freely"), later ones off their own standings, so "a pre-registered null is coded SURVIVED because its stated result stands." That is not a confound in a well-defined outcome; it is two different outcome variables sharing a column name. The honesty is creditable and the analysis is not rescued by it. The outcome scale is also a hybrid of two source vocabularies: three levels map onto the vault's `standing` set, PRIOR_ART comes from the novelty scale, and `overturned` — a legal standing value — never appears. Provide a codebook: one paragraph per level, with the decision rule and a worked boundary case for each adjacent pair (narrowed vs. withdrawn; prior art vs. narrowed).

**Nobody was blind, and there was one coder.** §7 concedes that the coding agent "is not blind to outcome" and that the two judgement-bearing predictors (`famous`, `move`) were coded by an agent that had already read the notes. `move` is not a minor covariate — it is the entire §3.1 table and the paper's most-cited structural finding. There is no second coder, no inter-rater agreement statistic, and no adjudication procedure. For a meta-research venue this is the central omission: a double-coding of a random 25–30% of rows by an independent agent (different model, brief containing the codebook and nothing else), reported as Cohen's κ per variable, is a day's work and would convert the coding from assertion to measurement. Also state how the eight `AMBIGUOUS` rows (§7) were treated in every rate — "marked rather than resolved" does not say whether they are in the 82, and if they are, which cell they entered.

**Population or convenience sample?** Both, and the paper conflates them. It is a *census* of one project's output (good: no selection within the frame) and a *convenience sample of one frame* (fatal for generalisation). §7 says this. But §3.1 then calls the ID set "fixed in the pre-registration," which invites the reader to treat the frame as principled when it is simply "what this vault contained on one day," minus ten silently absent IDs. The mix of move types is an artefact of the orchestrator's choices, which means the headline 0.317 is a weighted average over a weighting nobody chose deliberately — a different question mix moves it from 0.19 to 0.71 by the paper's own table. The abstract should carry that range, not just the point estimate.

**The round confound is named, not handled.** Naming is necessary and insufficient. Three things could have been done and none were: (a) re-grade a random subsample of the 2026-09-03 claims under the 2026-09-05 rubric and report how many outcomes flip — this directly estimates the size of the instrument change and is by far the highest-value additional analysis in the paper; (b) report the round test stratified by grading source (novelty-derived vs. standing-derived) and show whether the effect survives within strata; (c) present the round result in a supplement rather than the abstract. As it stands, the abstract asserts "The only significant variable was *when* a claim was made" and then, in the same breath, that the result is confounded. A referee reads that as a result being banked and disclaimed at once. Either the effect is estimable or it is not; if it is not, it does not belong in the abstract as a finding.

**Are H1--H4 tested?** Partly. Four 2×2 Fisher tests are reported with exact *p*-values, which is a test. But: (i) no confidence intervals appear anywhere in the manuscript — 26/82 has a Wilson 95% interval of roughly [0.22, 0.43], which is the single most important number the reader needs and it is absent; (ii) no multiplicity adjustment is made across at least five tests, and the one significant *p* = 0.0078 would want a stated correction (Bonferroni at five tests gives 0.039 — still nominally significant, and still confounded, which is the actual objection); (iii) three of the four "tests" are separation or near-separation (0/6, 0/3-vs-2/2, 1/11) where Fisher is being asked to adjudicate patterns with essentially no power, and the paper knows this ("six rows cannot carry a *p*-value," "the brief's own gate forbids calling evidence") yet the abstract still reports the pattern as substantive; (iv) the round test — the paper's only significant result — is described as "the broader form of the same variable" as H3, which is a *post hoc* redefinition of a pre-registered predictor. Was `round` in the hashed brief as a separate hypothesis, or is it an analytic variant discovered after H3 failed? The answer determines whether *p* = 0.0078 is a pre-registered result or an unregistered one, and it is not currently answerable from the text. Say so explicitly, and if it was unregistered, label it exploratory in the abstract. The refusal to fit a logistic model on separation grounds is correct and well argued; a Firth penalised fit with an explicit statement that the correlation coefficient is not interpretable would still be worth reporting for the non-separated predictors.

**The taxonomy is a list, not a taxonomy.** It is not exhaustive — §7 concedes it is a floor with no denominator of attempted failures — and it is not mutually exclusive: the 578 case is the named exemplar of **P2** (unattributed count) *and* the first-named instance of **P1** (two numbers in one field) in consecutive bullets. If a single event populates two modes, "79 instances across 25 modes" is a count of annotations, not of events, and the three-most-frequent ranking is unstable under recoding. Either enforce a single primary mode per instance (with secondaries recorded separately) or rename the object a catalogue and drop the frequency ranking.

**The catch table.** It does not double-count in the narrow sense you might fear — the column is explicitly "earliest catch" across modes, so each mode is assigned once. Four other problems are worse. (i) **The unit is modes, not instances.** A guard that first caught one singleton mode scores the same as one that first caught a seven-instance mode. Report the catch table over the 79 instances as well; the ordering may not survive. (ii) **The denominators are absent and wildly unequal.** The linter ran on every commit; the adversary ran on three clusters (§2.6). "Adversary 7, lint 0" therefore compares a handful of exposures to hundreds, and the paper's marquee finding — the cheap automated guard caught nothing — is an artefact of that asymmetry as much as of anything about linting. Give exposures per guard and a per-exposure catch rate, or withdraw the comparison. (iii) **The assignment is retrospective and unrecorded.** "Earliest catch" was reconstructed after the fact by the same agent that wrote the taxonomy; there is no contemporaneous field recording which guard fired first. That should be stated as a limitation. (iv) **The linter's zero is definitional.** `_lint.py` checks frontmatter vocabulary; the 25 modes are all semantic (provenance, statistics, instruments, reasoning, process, framing). A guard scoring zero on a set of failures it is not designed to detect is a selection effect, not an efficacy result. The one honest version of this finding is narrow and worth keeping: *schema linting does not substitute for semantic auditing*. The version currently in the abstract and §1 — "the cheap automated guard caught nothing" — is a bigger claim than the design supports.

**Layer 4 was never reached.** §2.1 states the depth gate holds the project at Layer 2. So no claim in the record was empirically tested against the world; "survival" means "survived internal audit by the same system that produced the claim." That deserves a sentence in the abstract, because most readers will import the ordinary meaning of survival (external replication) into the 0.317.

## 4. Claims vs. evidence

- **Title.** "82 AI-generated ... claims" understates the human's role, which the paper itself emphasises (the human set the scope rule, the questions, the evidence standards, and chose what was kept). "AI-produced under a human scope rule" is what the record supports. Second, "What survives" and "survival" evoke survival analysis; there is no time-to-event model and no censoring. Consider retitling to make the object explicit: an audit of one project's claim record.
- **"Nothing about the *subject* of a claim ... predicted survival"** (§1, §4, abstract) is an acceptance of the null from tests with power near zero. The correct statement is that no subject-level predictor was *detected* at this sample size, and that H1 and H4 show perfect separation in the hypothesised direction — i.e. the data are weakly *consistent with* subject-level prediction, not against it. As written, §1's bolded sentence contradicts §4's own admission that H1 "holds in direction" and H4's direction "is perfect."
- **"An adversarial pass is not a kill mechanism; it is a narrowing mechanism"** is stated in bold as a general finding from a predictor whose definition conflicts with §2.6 (see §2, item 1 above) and from a 1.2-point difference in the *unexpected* direction with n = 82. This is over-claimed by a wide margin.
- **The five rules are folk wisdom with instances attached.** Rule 1 (provenance on every number), rule 2 (calibrate an instrument before believing a zero), rule 4 (positive and negative controls), rule 5 (concurrency discipline; hold a retraction to the standard of what it retracts) are standard research hygiene; rule 3 is pre-registration. None is derived from the survival data — no hypothesis in §4 tests any rule, and the section itself says the rules are "reproduced verbatim from the taxonomy," i.e. they were written before this analysis and are not its output. The only quantitative content in the whole section is rule 3's ρ moving from −0.18 to +0.02 under a declustering choice, which is n = 1 join. Either (a) present the rules honestly as *practice recommendations illustrated by* the record rather than derived from it — that is a legitimate and useful contribution — or (b) test them: e.g. do claims whose notes carry full provider/endpoint/date provenance survive at a different rate? That is a codable predictor from the existing rows and would turn rule 1 into a result. Also, "Rules 1 and 5 are corollaries of one another" is not what a corollary is; the relation described is that one instance violated both.

## 5. Missing comparisons

§7's "No human-only baseline exists" is candid but treats the absence as unavoidable. It is not: what is missing is not a bespoke matched experiment but a **literature section**, and its absence is the largest gap for a meta-research venue. `refs.bib` contains seven entries, of which four are subject-matter soil/hibernation citations, one is a self-citation, one is a companion manuscript, and one is a guidance page. There is **not a single meta-research or AI-for-science reference in the bibliography.** For this venue that is disqualifying on its own. At minimum the paper needs, and should position 0.317 against:

- **Reproducibility base rates.** The large replication projects and the biomedical preclinical audits give published rates in the 11–61% range depending on field and criterion. These are the natural yardstick for "a third of claims stood."
- **The theoretical literature on why most claims fail**, which is the standard framing citation for a kill-rate paper.
- **AI-for-science claim-quality reports**: automated-discovery pipelines and their reviewer-scored outputs, and the controlled studies comparing LLM-generated to human-generated research ideas on novelty and feasibility. These are the closest existing comparators and are directly citable; several report exactly the "novel-looking but repackaged" failure the authors observe as PRIOR_ART at 19/82.
- **The LBD evaluation literature.** The paper invokes Swanson and then asserts that "LBD evaluation lacks controls" (§2.4) with no citation. There is a body of work on LBD evaluation and its false-positive problem; either engage it or drop the claim of novelty for the positive-control ratio.
- **Cross-domain / interdisciplinary claim error rates and the citation-accuracy literature** (quotation and citation-error studies), which speak directly to the provenance failure modes P1/P2/P4.
- **AI-disclosure and reporting-guideline work** beyond the ICMJE page, and any emerging checklist for reporting agentic research pipelines.

Without these, "the kill rate is a description of this loop" is true but leaves the reader unable to place the number at all — and a meta-research reader will not accept that the placement is impossible.

## 6. Generalisability and conflicts

The confounding here is structural and stacked: one project, one vault, one to two days, one human operator, one orchestration policy, one model family, and — most consequentially — **the authors are the system under study and the AI that produced the claims also coded their outcomes, wrote the failure taxonomy, drafted the rules, and drafted the manuscript.** §7 states each of these. Stating them does not neutralise them, and the paper should be explicit about the direction of the resulting bias rather than leaving it symmetric. The plausible directions are all favourable to the system: a coder that read the notes and knows the project's preferred narrative will resolve borderline rows toward the outcome that fits; a taxonomy written by the same kind of agent that committed the failures is blind precisely where that agent kind is blind (§5 concedes this at Pr4, whose single instance exists only because a human noticed); a "floor" count of failure modes with no denominator understates the failure rate by an unknown factor; and the guard-attribution table was reconstructed by the beneficiary. The inference this permits is: *within this repository, on these two days, these rows were coded this way.* It does not support any statement of the form "AI-generated research claims survive at rate X," and one or two sentences in the abstract and §1 currently drift toward that reading.

What would fix it, in descending value per unit effort:

1. **Independent re-coding.** A blinded second coder — ideally a human, at minimum a different model family under a codebook-only brief with note text stripped of standing/novelty fields — on a random subsample, reported as κ per variable with disagreements listed. This is the single change that would move the paper from testimony to evidence.
2. **Re-grade under one rubric.** Apply the 2026-09-05 rubric to the 2026-09-03 claims and report the flip rate; this bounds the round confound directly.
3. **A second frame.** Even one additional short project — different domain, different operator, or a different model family as orchestrator — turns n = 1 project into n = 2 and makes the phrase "does not generalise" a measured statement rather than a disclaimer.
4. **A human comparator, however small.** Twenty claims from an unassisted researcher's day, graded by the same codebook and the same coders, would give the abstract its missing denominator. Underpowered but interpretable beats absent.
5. **Pre-register the guard comparison prospectively** with exposure counts per guard, so the catch table becomes a rate rather than a tally.

## 7. Ethics and disclosure

The AI-use disclosure (§6) is better than most submissions and I would not ask for more on the LLM front specifically: models named with versions, roles separated (orchestration vs. execution vs. drafting), the outcome-coding disclosed as a limitation rather than buried, authorship declined for the models, and human responsibility asserted. Two additions: state whether the models were used to *select* which claims entered the ID set (§3.1 says the set was "fixed in the pre-registration" but not by whom), and state which parts of the final text are model-drafted versus human-written, since the manuscript's rhetorical framing is part of the object under study.

What is missing is everything else a venue of this kind requires:

- **No affiliation, ORCID, or corresponding-author email.** The YAML still carries the author's own to-do comment. Fix before any submission.
- **No competing-interests statement.** One is genuinely needed and it is not pro forma: the author is auditing his own system, the vendor of the models is not the author but the entire object of study is the author's project, and the audit's favourable readings accrue to the author. Say it plainly.
- **No funding statement.** Even "no funding" must be stated.
- **No ethics statement** (presumably "no human subjects; not applicable" — state it).
- **No author-contribution statement**, which is precisely the item this paper of all papers should model well, given that most of the contributions were made by non-authors.
- **Data availability lacks hashes and violates the paper's own Rule 1.** §8 lists files and a Zenodo *concept* DOI which, per `refs.bib`, "resolves to the latest release" — a moving target. A paper whose first rule is that a number without a provider and a fetch date is not a number must cite a **versioned** DOI (the bib already knows it: 10.5281/zenodo.22334048), a **git commit SHA**, and **sha256 hashes** for at least `claims.csv`, `failure-taxonomy.md`, `log.md` and the twelve blind briefs. The paper hashes its briefs and then ships its own evidence unhashed. Add a table: file, sha256, size, retrieval date.
- **The bibliography contains a self-declared unverified citation.** `icmje2025` carries "UNVERIFIED: not fetched during preparation of this manuscript." The paper cites it as the authority for its disclosure practice. Fetch it, record an access date, and cite the specific recommendation section. Leaving it as-is is not a minor slip in this manuscript; it is a violation of the paper's headline rule inside the paper's own reference list. Likewise `paper1` is unpublished with no DOI or preprint posting — post it or cite it as "in preparation," and do not lean on it in §8.
- **Verification policy in the bib header is exemplary** and should be described in §8 of the paper itself, not left only in a comment in a build file readers will not see.

## 8. Minor

- **Abstract** is roughly 230 words and reads as a results dump: eleven distinct numbers, several unexplained on first encounter ("the famous-pair hypothesis reversed," "1.2 points," "audit 11, adversary 7"). Check the venue's structured-abstract requirement. Cut the guard tally and the log tally; keep the rate, the interval, the null, and the confound.
- **Terminology drift.** At least four scales are in play — outcome (SURVIVED/NARROWED/PRIOR_ART/WITHDRAWN), vault standing (`live`/`narrowed`/`withdrawn`/`overturned`), novelty (NOVEL/REPACKAGED/REDISCOVERED/LOCATED/CORRECTED), and evidence strength — and the text moves between them without signposting ("survived" in §3, "still stand" in §3.1, "`live`" in §4's adversary paragraph, "NOVEL" in §2.7). Add a single figure or table mapping the three graded scales onto one another, showing which outcome levels derive from which source field. `overturned` appears in the vocabulary and never in the data: say why.
- **No figures at all.** Three would earn their space: (a) survival by move type as a dot-and-interval plot with Wilson intervals, which would show instantly that all eight cells overlap; (b) a flow diagram from 87 coded rows to 82 graded to the four outcomes, with the excluded IDs named; (c) the failure taxonomy as a 25-row table with group, instance count, owner, guard and whether a guard now exists — currently the reader is asked to trust prose summaries of a table they cannot see. The taxonomy table in particular should be in the paper, not only in the vault.
- **Missing table:** the guard/exposure/catch-rate table requested in §3 above.
- **§3.2's Alexander (1997) example** cites provider counts 46 / 40 / 36 from OpenAlex, OpenCitations and Crossref without giving the DOI, and it is one of the paper's two flagship provenance narratives. Give the DOI and the fetch timestamps, as the paper does for the RevModPhys case.
- **Numbered claim IDs (C51, G36, Pr2, I4, S1...) are used throughout without a key.** A reader without the vault cannot follow §5's paragraph on "the modes that killed claims." Either expand each on first use or add a glossary.
- **Citation formatting.** `evans2020` gives `pages = {0940b2}` for an article number — use an `eid`/article-number field or the journal's convention rather than a page range. `quarrier2023` has a Crossref/print year discrepancy documented in the note; make sure the rendered year matches what a reader will find. `swanson1986` volume 30 issue 1 with an issued date of 1986-09 is fine but worth a glance against the journal's own numbering. Seven references is far too few for the venue regardless of formatting.
- The Rule 3 figure "ρ from −0.18 to +0.02" needs the n and the two declustering definitions inline; as written it is exactly the kind of unattributed number Rule 1 forbids.

## 9. Recommendation

**Major revision.** The manuscript is doing something the literature genuinely lacks — a complete, adversarial, self-incriminating audit of an agentic research pipeline's entire claim output, with a failure taxonomy and a guard-cost analysis — and its arithmetic is, where I could check it, unusually clean: the move-type table, the outcome table, every 2×2 partition and every quoted proportion recompute correctly. The candour is real and is the paper's main asset. But three defects block acceptance in its present form. First, the outcome variable is undefined and demonstrably non-constant across the sample, and it was coded once, unblinded, by an agent from the same family as the one that produced the claims; until a blinded second coding and an inter-rater statistic exist, every rate in the paper is testimony rather than measurement. Second, the paper's two most quotable findings are over-claimed relative to the design: "the schema linter caught nothing" is a selection effect over unequal and unreported exposures, and "an adversarial pass is a narrowing mechanism" rests on a predictor (48 claims) that flatly contradicts the methods section (three adversarial rounds). Third, for a meta-research venue the manuscript has no meta-research literature in it at all — no reproducibility base rates, no AI-for-science comparators, no LBD-evaluation engagement — so the reader is handed 0.317 with nothing to compare it to and is then told, correctly, that no comparison exists. Fixing the seven internal mismatches in §2 is a day; the blinded re-coding, the re-grade-under-one-rubric analysis, the guard-exposure denominators, the hash table, and a real related-work section are perhaps a week. All are within reach with the materials the authors already have, and I would review a revision willingly.

## 10. Questions for the author

1. **How exactly was the `adversary` predictor coded such that 48 of 82 claims carry it, when §2.6 reports three adversarial rounds against three named clusters — and is that variable separable from the 2026-09-05 round, which is your one significant effect?**
2. **Was `round` (2026-09-03 vs. 2026-09-05) named as a predictor in the sha256-hashed C51 brief before any outcome column was read, or was it constructed after H3 failed? If the latter, will you relabel *p* = 0.0078 as exploratory in the abstract?**
3. **Will you re-grade a random sample of the 2026-09-03 claims under the 2026-09-05 rubric and report the flip rate — and have a second, independent coder (different model family, codebook-only brief, standing and novelty fields stripped) re-code a subsample so the paper can report κ for `outcome`, `move` and `famous`?**

---

## Author response

Referee 1, 2026-09-05. Revision prepared the same day. The referee recomputed every rate and
every table total from the manuscript's own figures before writing; that is more than the paper
was owed, and the seven mismatches were all real. Below, each point is answered with the
sentence or the number that changed. Where a request was not met, it says so plainly rather than
substituting something easier.

**Files changed:** `papers/audited-record/paper.md`, `papers/audited-record/refs.bib`,
`papers/audited-record/README.md`, `vault/computed/C51-vault-meta-analysis.md`,
`vault/method/failure-taxonomy.md`, and a new `vault/PENDING-log-REV3.md` staging the log
entries. `vault/_scripts/c51_data/claims.csv` is **unchanged**: every new number is a different
cut of the same rows, not a re-coding.

---

### §2 — the seven internal mismatches

**(1) Three adversarial reviews vs. 48 claims with an adversarial pass.** Correct, and the
paper's most quotable sentence rested on the confusion. Two objects are now named separately in
§2.6 and used separately throughout:

- a **dedicated adversarial review** is a full agent-round briefed to kill one claim cluster.
  There are exactly **three**: `audits/c43-adversarial.md`, `g34-adversarial.md`,
  `g36-adversarial.md`.
- an **adversarial leg** is the pre-registered predictor `adversarial`, whose coding rule is now
  quoted verbatim from the hashed brief, §Predictors (e): *1 iff an `audits/*-adversarial.md`
  file exists for the claim, **or** the note records a negative control, a positive control, or
  an explicit adversarial pass.* **48 of 82** graded claims carry one.

The referee's collinearity worry is answered with counts rather than assurance: of the 48, **27
are post-audit rows and 21 are early rows**, and 8 post-audit rows carry no leg. Correlated, not
collinear. The sentence **"An adversarial pass is not a kill mechanism; it is a narrowing
mechanism" is withdrawn** — from the abstract, from §1 and from §4 — as over-claimed from a
1.2-point difference in the unexpected direction at n = 82 with nested intervals. What replaces
it: *"on this record an adversarial leg did not change the survival rate, and the claims that
received one ended narrowed more often than killed."* The revision also reports that the sign is
not stable within strata (novelty 4/11 = 0.364 with vs 1/13 = 0.077 without; standing 11/37 =
0.297 vs 10/21 = 0.476), which is the strongest argument against the old sentence and is now in
the text. `C51 §4` carries the same withdrawal.

**(2) One correction of a correction, or two?** **Two**, and the abstract, §3.3 (Corrections) and the tally now
all say two. The discrepancy had a mundane cause, now stated: only one entry carries the `kind`
string `correction of a correction` (the 578/595 re-fetch); the second is filed under plain
`correction`, with the header `## [2026-09-05] correction | "46 citations was stale" was itself
the error`. So *the `kind`-field tally is 1 and the count of the move is 2*, and the gap is a
property of a free-text field, not of the record. The paper now says exactly that.

**(3) One day or two.** **Two working days**, everywhere. §1 already said it; the Limitations section's "One project,
one day" now reads "One project, two working days, one orchestrator, one model family", and the
79 failure instances are described as coming from *the second of those two days* (2026-09-05)
rather than "one day", in the How-it-fails and Limitations sections. The taxonomy limitation was indeed only about the
taxonomy; it now says so.

**(4) Twelve briefs for fourteen IDs.** The twelve are now listed by ID in §2.5 and §3.4: **C39,
C40, C43, C44, C45, C46, C47, C48, C49, C50, C51, C52**. **C41 and C42 fall inside the C39–C52
span and carry no brief.** The "ten of the 82 graded claims carry a brief" line is now
reconciled explicitly: the briefs for C51 and C52 lie outside the graded ID set, leaving C39,
C40 and C43–C50 = 10. On the referee's second point: §5's "C52 §grade table" cites C52 as a
*source* for another claim's grade, not as a graded row, and the text now says so.

**(5) Failure-mode ownership sums to 23, not 25.** Recounted from the taxonomy table's own
`actor` column rather than from prose. **Model 16 outright** (P2, P3, P4, S1, S2, S3, S4, I4,
I5, R1, R2, R3, R4, Fr1, Fr2, Fr3), **orchestration 4** (Pr1–Pr4), **tooling 2** (I1, I2), and
**3 jointly owned** — P1 (human/model), I3 (tooling/orchestration), Pr5 (model/human).
16 + 4 + 2 + 3 = **25**. The human, per the referee's request, gets a count: **owns no mode alone
and co-owns two**, P1 and Pr5, both by over-trust in a number that arrived without a provider.
Counting joint ownership as implication rather than sole ownership: model 18, orchestration 5,
tooling 3, human 2. `vault/method/failure-taxonomy.md` §"The table" carries the same recount, and
the correction is staged for `log.md`.

**(6) Forty entries in "smaller kinds".** Given in full instead. `log.md` was also recounted at
the pinned commit and had grown since the draft: **252 entries** (not 245), 30 under 2026-09-03
and 222 under 2026-09-05, of which **97** carry a `kind` containing "correction" (not 93) — 77
`correction`, 19 `correction (archived)`, 1 `correction of a correction`. The remainder is now
printed completely: `method` 41, `computed` 28, `verification` 25, `honest null` 11, `gap` 9,
`vocabulary` 4, `provenance` 3, `negative control` 3, `computed + verification` 2, and **29 other
kinds appearing once each**, all 29 named in §3.3 (Corrections). 97 + 126 + 29 = 252. The paper states that
245/93 are superseded and why.

**(7) Silent gaps in the population.** §3.1 now carries a paragraph headed *"The frame, stated in
full."* **C23 and C24 were never created** — the computed-note numbering skips them; no file, log
entry or index line has ever carried either ID. **Eight G-IDs are retired**, with a written
reason each in `METHOD.md`: G10, G13, G14, G15, G16, G18, G24, G26 (an experimental frontier
inside one field; three proposals with no result; an intra-field dispute; a real result never
written up, to be re-opened under a new ID; a thin non-zero; a reclassification to "not yet a
shared object"). Retirement was a scope decision made *before* this audit and not by it.
**C51, C52 and C53 postdate the hashed ID set** and are not graded rows. The frame is therefore
**every note that exists** under the three prefixes on 2026-09-05, and nothing inside it was
dropped — the absences are IDs that name no note.

---

### §3 — design validity

**Survival is not one variable.** Accepted in full, and it is the largest change in the revision.
Rather than defend a hybrid column, the outcome is **split into two variables** using each row's
own `source_line`, which names the file and line the outcome was read from — a mechanical split,
not a judgement:

| variable | n | SURVIVED | NARROWED | PRIOR_ART | WITHDRAWN | rate | Wilson 95% CI |
|---|---|---|---|---|---|---|---|
| `survived_novelty` | 24 | 5 | 0 | 19 | 0 | **0.208** | 0.092–0.405 |
| `survived_standing` | 58 | 21 | 26 | 0 | 11 | **0.362** | 0.251–0.491 |
| pooled | 82 | 26 | 26 | 19 | 11 | 0.317 | 0.226–0.424 |

The table makes the referee's point better than prose could: **the two instruments cannot return
each other's verdicts.** The novelty scale has no NARROWED and no WITHDRAWN, so all 24 of its
rows are SURVIVED or PRIOR_ART; the standing scale has no PRIOR_ART, so all 19 prior-art rows
come from the novelty side. The pooled 0.317 is a weighted average under weights nobody chose.
H1–H4 are re-run within each stratum wherever the stratum contains both levels of the predictor,
and where it does not — H1 within novelty, H4 in either — the paper says the test does not exist
rather than reporting a number. This is a new §3.2 in the paper and a new subsection in
`C51 §1`. A codebook — one paragraph per level with a decision rule and a worked boundary case —
is *not* added; the level definitions and the two coding rules (precedence WITHDRAWN >
PRIOR_ART > NARROWED > SURVIVED; standing beats a LOCATED novelty grade) live in the hashed brief
and in `C51 §1`, and the split above is the more honest fix. The referee is right that a codebook
is still owed and it is listed as outstanding.

**Nobody was blind, and there was one coder.** Conceded and **not fixed**. No second coder, no κ,
no adjudication. The revision does not paper over this: §8 (Limitations) now states the *direction* of the
bias rather than leaving it symmetric — an unblinded coder that has read the notes resolves
borderline rows toward the project's preferred reading; a taxonomy written by the kind of agent
that committed the failures is blind where that agent kind is blind; a floor count with no
denominator understates by an unknown factor; the guard table was reconstructed by the
beneficiary — and closes with the inference the design permits: *within this repository, on these
two days, these rows were coded this way.* The eight `AMBIGUOUS` rows **are** in the 82; each was
coded into a cell by the precedence rule and flagged, and `C51 §5` names all eight and the cell
each entered.

**Population or convenience sample.** The frame paragraph (above) removes the "ten silently
missing IDs" problem, and §3.1 no longer implies the frame is principled beyond what it is: the
notes that existed. The abstract now carries the **range**, not only the point estimate: *"That
headline is a weighted average over a question mix nobody chose deliberately: by move type it
runs from 0.19 to 0.71."*

**The round confound is named, not handled.** The referee listed three remedies; **(b) is now
done**, (a) is not, (c) is partly done. Stratified by grading source, the round contrast
**persists on the standing side**: 16/33 = 0.485 (0.325–0.648) against 5/25 = 0.200
(0.089–0.391), Fisher p = 0.0307, n = 58; within the novelty stratum there are two post-audit
rows and the contrast is untestable. So the effect is not *only* the instrument change — and the
paper says so, immediately followed by what the stratification does not fix: audit intensity also
changed across the same day boundary. The abstract still reports the result, but now labelled
**exploratory** and with the stratified figure beside it, so the reader is not handed a banked
result and a disclaimer in one breath. Remedy (a), re-grading a random sample of early claims
under the later rubric, is **not done** and is named in the paper as the highest-value
outstanding analysis.

**Are H1–H4 tested?** (i) **Wilson 95% intervals now appear on every rate in the paper**,
including 26/82 = 0.317 [0.226, 0.424], every cell of the move-type table (where the paper now
states that every interval overlaps every other), both survival variables, and both sides of
every 2×2. (ii) **No multiplicity adjustment**, with the reason stated rather than assumed: the
brief fixed four hypotheses and "no multiplicity correction … reported as such" before any
outcome was read, and all four are reported whatever they returned, *together with every
exploratory contrast run*, so there is no selection of tests to correct for. For the record, the
paper gives Bonferroni over six (four pre-registered plus two exploratory): threshold 0.0083,
which p = 0.0078 clears — and it is confounded anyway, which is the referee's actual objection.
(iii) Accepted: the near-separated tests are now reported as *failures to detect* with intervals
that make the absence of power visible, and the abstract no longer asserts the pattern as
substantive. (iv) Answered directly, and the answer is in the file: `round` **was** in the hashed
brief, as predictor (h), defined before any outcome column was read — but the brief named **four**
hypotheses and the round contrast is not among them. It is therefore a pre-registered predictor
in an unregistered contrast, and it is **labelled exploratory in the abstract and in §4**, as the
referee asked. The same label is applied to the adversarial-leg contrast. A Firth fit is still not
reported; the paper's reason for declining the logistic model is unchanged and the referee agreed
with it.

**The taxonomy is a list, not a taxonomy.** Accepted, and the object is renamed in function if
not in title: the taxonomy note's callout and a new §"This list is not a partition" state that
**the modes overlap and one event can populate several**. The overlap is given a count and named
instances: **at least three logged events populate more than one mode** — the 578/595 reference
count (P2 exemplar, first P1 instance, and the Pr5 correction-of-a-correction: one event, three
modes); C46's Σ ≡ 1 (I4 and Pr2); the spent OpenAlex daily budget (I3 and Pr3). Consequently
**"79 instances" is a count of annotations, not of events**, the three-most-frequent ranking is a
ranking of annotations, and the paper says so. Enforcing a single primary mode per instance would
require a re-coding that has not been done; the count of distinct underlying events was not
recorded contemporaneously and is not recoverable from the log.

**The catch table.** (ii) and (iv) are fixed; (i) and (iii) are conceded. The table now carries a
**denominator column** giving the exposure each guard was applied to: provenance audit — all 87
coded notes over 7 audit reports; dedicated adversarial review — 3 clusters; replication and
controls — 5 runs; self-test and calibration — 2 instrument adapters; pre-registration — 12 blind
briefs; the human — continuous, no denominator; **lint — 89 commits × ~140 notes**. The paper
states that the units are not commensurable and the column is a statement of asymmetry rather
than a rate. And the marquee finding is narrowed to exactly the referee's honest version: **the
zero is kept and is stated as a selection effect** — `_lint.py` checks frontmatter vocabulary,
field types and wikilink reachability, and all 25 modes are semantic — with the reading now
*"schema linting does not substitute for semantic auditing"* in the abstract, §1, §5 and the
taxonomy note. "The cheap automated guard caught nothing" is withdrawn. (i) The instance-level
version of the table is not produced, and (iii) the retrospective, uncontemporaneous nature of
the "earliest catch" assignment is now stated as a limitation in §8 (Limitations).

**Layer 4 was never reached.** Accepted; **this is now in the abstract** ("No claim was tested
against the world: a written depth gate holds the project at Layer 2, so survival here means
survived internal audit"), in §1, and as its own limitation in §8 (Limitations).

---

### §4 — claims vs. evidence

- **Title.** Kept for this revision, with the substance of the objection moved into the text: the
  human's role is stated in the abstract's first clause and in the new author-contributions
  statement, and the "survival" reading is disarmed by the Layer-2 sentence now in the abstract.
  A retitle is a venue decision and is listed as outstanding rather than made unilaterally.
- **"Nothing about the subject of a claim predicted survival."** **Withdrawn** and replaced,
  in the abstract, §1 and §4: *"No subject-level predictor of survival was detected at n = 82…
  Two hypotheses (H1, H4) show perfect separation in the predicted direction on six and five
  rows, so the data are weakly consistent with subject-level prediction and not against it."*
  §1 and §4 no longer contradict each other.
- **The adversarial-pass sentence.** Withdrawn; see (1) above.
- **The five rules.** Presented as *practice recommendations illustrated by* the record — option
  (a); the section already said "reproduced verbatim from the taxonomy" and now does not imply
  derivation. The referee's option (b) — coding provenance completeness as a predictor and
  testing rule 1 against survival — is a genuinely good analysis, is cheap from the existing
  `provenance` column, and is **not done** in this round; it is listed as outstanding. The
  "corollaries of one another" sentence is not defended: the relation is that one instance
  violated both, which is what the record shows. The ρ figure now needs its n and its two
  declustering definitions inline, and that is also outstanding.

---

### §5 — missing comparisons

Accepted as the largest gap for the venue. The bibliography goes from seven entries to sixteen,
and a **new "Related work" section** is added. Every new entry was verified by fetch on
2026-09-05, six at `api.crossref.org/works/{doi}?mailto=deciduusleaf@gmail.com` and three at the
arXiv API because they are not in Crossref: reproducibility base rates [@osc2015;
@errington2021; @ioannidis2005]; AI-for-science outcome reports [@lu2024; @si2024], with the 2025
audited follow-up the referee's "closest existing comparator" describes [@si2025]; LBD evaluation
[@swanson1997; @yetisgen2009]; and AI-authorship policy [@icmje2026; @nature2023]. The §2.4 claim
that "LBD evaluation lacks controls" is **withdrawn as stated** and replaced with a cited, narrow
version: expert inspection and time-sliced evaluation both exist, neither supplies a negative
control for a single intersection, and that is the only novelty claimed for the control ratio.
Two of the referee's six categories are **not** added — cross-domain error rates and the
citation-accuracy literature, and reporting guidelines for agentic pipelines — because nothing was
verified for them in the time available and an unverified citation in this manuscript would be a
worse failure than an absent one.

The paragraph placing 0.317 ends on the caveat the referee's own §5 implies, that none of these
is the same outcome: a psychology replication is a pre-registered repeat against a fresh sample,
a reviewer score is a judgement of a manuscript, and 0.317 is "the headline sentence still stands
after an internal audit of the same project's own record, having never left Layer 2." The
comparison establishes that a third of claims standing is not anomalous in either direction, and
that the interesting content of this record is the taxonomy and the guard-cost accounting, for
which no base rate exists at all.

---

### §6 — generalisability and conflicts

The five remedies are ranked by the referee in descending value; **none of the five is done**, and
the revision says so rather than substituting cheaper work. What *is* done is the referee's own
first sentence of the section: the direction of the bias is now stated rather than left
symmetric, in a new limitation paragraph that names each mechanism and the direction it pushes,
and ends with the inference the design permits. The abstract and §1 sentences that drifted toward
"AI-generated research claims survive at rate X" are gone: the abstract now carries the 0.19–0.71
range, the two-variable split, the Layer-2 caveat and the exploratory label.

---

### §7 — ethics and disclosure

- **Model use in selecting the ID set.** Now stated in §6: the frame was written into the hashed
  C51 brief by the orchestrator as a mechanical enumeration of the notes that existed, and the
  author confirmed it before dispatch. No model chose which claims entered the set.
- **Which text is model-drafted.** Also now in §6, and answered without hedging: all of it, in
  first draft, including this revision; the author revised, cut and approved every sentence.
  Since the rhetorical framing is part of the object under study, the section tells the reader to
  assume that any sentence flattering the loop was written by the loop.
- **Affiliation, ORCID, corresponding author.** The YAML to-do comment is gone. Affiliation is
  now **"Independent researcher; Arizona State University (student)"**, carried as a placeholder
  the author confirms before submission; the corresponding email is in the header. **ORCID is
  still absent** and is flagged in `README.md` as the one item the author must supply.
- **Competing interests, funding, ethics, contributions.** All four added as a new
  **Declarations** section. The competing-interests statement is written as the referee asked —
  plainly, and not pro forma: the author is the operator and sole author of the system under
  audit, and every favourable reading accrues to him.
- **Data availability.** Rebuilt to satisfy the paper's own Rule 1. It now pins the **commit
  SHA `f1faab396bf80c7dc6eb8a8eef86a935e23c46fe`**, cites the **version DOI
  `10.5281/zenodo.22334048`** as the citable record while naming the concept DOI
  `10.5281/zenodo.22334047` as the moving target it is, and gives **sha256 hashes and byte counts
  in two tables**: `claims.csv`, `failure-taxonomy.md`, `log.md` and `C51`, plus all **twelve**
  blind briefs individually. The two files this revision edits are hashed twice, as committed and
  as revised, so neither number is ambiguous.
- **`icmje2025` unverified.** Fetched. `https://www.icmje.org/recommendations/` returned HTTP 200
  on 2026-09-05, carries "Updated January 2026", and the relevant section is **V. Use of
  Artificial Intelligence in Publishing**; the entry is rekeyed `icmje2026` with the access date
  and the section recorded, and is no longer marked UNVERIFIED. `paper1` remains unposted and is
  now cited as a manuscript in preparation, with the paper stating explicitly that no claim rests
  on it.
- **Verification policy described in the paper.** Done: §10 (Data availability) now carries the policy in prose, not
  only as a comment in `refs.bib`.

---

### §8 — minor

Done: the ICMJE and `paper1` fixes; the verification policy in §10 (Data availability); the terminology point is
partly served by §3.2, which shows exactly which outcome levels derive from which source field
and why `overturned` never appears in the data (it is folded into WITHDRAWN by the brief's own
vocabulary rule).

**Not done**, and listed here rather than quietly skipped: the abstract is still long and still
a results dump, though the guard tally has been cut from it; the three figures; the scale-mapping
table; the glossary of claim IDs; the Alexander (1997) DOI and fetch timestamps; the `evans2020`
article-number field; the ρ = −0.18 → +0.02 figure's inline n and declustering definitions.
The `quarrier2023` year discrepancy and the `swanson1986` numbering were re-checked against the
`note` fields and stand.

---

### §10 — the three questions

**1. How was `adversary` coded such that 48 of 82 claims carry it, and is it separable from the
round?** By the rule fixed in the hashed brief before any outcome was read, §Predictors (e):
*1 iff an `audits/*-adversarial.md` file exists for the claim, **or** the note records a negative
control, a positive control, or an explicit adversarial pass.* The three dedicated reviews cover
three clusters; the negative controls (C46, C50), the positive control (C33), the pre-registered
non-replication (C47) and the notes that record an explicit adversarial pass supply the rest, to
48. **It is separable from the round**: 27 of the 48 are post-audit and **21 are early**, and 8
post-audit rows carry no leg — so the two variables are correlated and not collinear, and the
counts are now in §2.6 so a reader can check the separation rather than take it on trust. The
sentence that rested on the confusion is withdrawn regardless, because 1.2 points in the
unexpected direction at n = 82 does not support a general finding whatever the predictor means.

**2. Was `round` in the hashed brief before any outcome column was read, or constructed after H3
failed? Will you relabel p = 0.0078 as exploratory?** It was in the brief: **predictor (h),
`early` vs `post_audit`, read from the log date**, defined before any outcome column was read.
But the brief names **four** hypotheses, H1–H4, and the round contrast is not one of them. So the
honest description is neither "pre-registered result" nor "constructed after the fact": a
**pre-registered predictor analysed in an unregistered contrast**. **Yes — it is relabelled
exploratory**, in the abstract, in §4 and in `C51 §2`, alongside the adversarial-leg contrast,
which gets the same label for the same reason.

**3. Will you re-grade a random sample of the 2026-09-03 claims under the 2026-09-05 rubric, and
have a second independent coder re-code a subsample for κ?** **Not in this revision, and neither
is faked.** The re-grade is named in §4 as the highest-value outstanding analysis and its absence
is stated where the round result is reported. The second coding is conceded in §8 (Limitations) as the central
omission, with the referee's specification — different model family, codebook-only brief, standing
and novelty fields stripped, κ per variable with disagreements listed — recorded as the design to
run. What this revision could do without either, it did: it split the outcome into the two
variables the referee identified, and ran the round contrast *within* the standing-graded stratum,
where it persists at p = 0.0307 on n = 58. That bounds part of what the re-grade would measure
and none of what the second coding would.

---

**One last note on process.** The referee observed that the paper hashes its briefs and ships its
own evidence unhashed. That is exactly the failure the paper's own Rule 1 describes, committed
inside a paper about committing it, and it is now logged as such in the vault rather than quietly
repaired — `vault/PENDING-log-REV3.md`, eight entries staged for `log.md`. The pattern of errors
is the data.
