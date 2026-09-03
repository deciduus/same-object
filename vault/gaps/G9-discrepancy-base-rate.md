---
id: G9
name: G9-discrepancy-base-rate
type: gap
standing: narrowed
evidence: full-text-read
contact-surface: 8
crosses: vocabulary
crosses-rank: 3
topology: direct
mediator: 
borrows-from: []
lends-to: ["[[fine-structure-discrepancy]]"]
mutual-with: []
computed-in: []
uses-move: []
rests-on: []
tags: [node/gap, crosses/vocabulary, evidence/string-protocol, standing/narrowed]
last-checked: 2026-09-03
note: "Outcome distribution still uncomputed. Our own four discriminating features tested: one refuted (Homestake), three narrowed, and the neutron-lifetime example was wrong on the facts."
---

# The discrepancy base rate

**STANDING: NARROWED** · evidence: full-text-read · contact surface: 7 · last checked 2026-09-03

> **Nobody has computed how often persistent inter-method disagreements resolved to systematics versus new physics.**

## What was wrong

The claim that nobody treats inter-method discrepancy as a class. **Two literatures already
do:** metrology's dark-uncertainty work, which models excess between-method scatter as a
class-level random effect; and epidemiological triangulation, which reasons from agreement
between methods with unrelated bias structures.

**And a third, stronger instance the note had missed.** Bailey, *Not Normal: the uncertainties
of scientific measurements* (arXiv:[1612.00778](https://arxiv.org/abs/1612.00778)):

> "Reported scientific uncertainties were studied by analysing 41000 measurements of 3200
> quantities from medicine, nuclear and particle physics, and interlaboratory comparisons
> ranging from chemistry to toxicology. Outliers are common, with 5σ disagreements up to five
> orders of magnitude more frequent than naively expected."

> "Such errors appear to have power-law distributions consistent with how designed complex
> systems fail"

That is the discrepancy class quantified, at scale, under another name — *heavy-tailed pulls*
and *uncertainty-normalised difference distributions*. Abstract fetched verbatim; the body was
blocked, so this is the abstract only.

## What survives, and the distinction is exact

**Bailey computes the distribution of discrepancy *magnitudes*. Nobody has computed the
distribution of *outcomes*.**

He partitions variance — statistical, evaluated systematic, unknown error. He does not partition
history. No source found tabulates past disagreements against what they eventually turned out to
be. The dark-uncertainty literature likewise **inflates error bars** rather than asking what the
discrepancies became.

Having the phenomenon quantified is not having the base rate.

## The catalogue exists now: [[C7-discrepancy-catalogue]]

39 cases. Raw tally: **20 SYSTEMATICS, 14 OPEN, 1 NEW-PHYSICS, 2 THEORY-ERROR, 1 REDEFINITION,
1 UNRESOLVED**.

**That is not a base rate and the note says so.** Three of five identified biases push the same
way: quiet convergence has no publication genre, and quiet convergence is exactly what a
systematics resolution looks like. Bailey's 41,000 measurements contain thousands of 3–5σ
disagreements; 39 reached a table. The true systematics fraction is **higher** than 80% and the
new-physics fraction **lower** than 4%, by an unknown amount.

The OPEN column carries no outcome information and must be excluded from any fraction — it is an
artefact of the sampling date.

**What survives the bias is not the fraction. It is a conditional:** every closed *same-class*
disagreement resolved to systematics, seven for seven. See [[Q7-same-class-prediction]], which
turns that into a dated prediction about the fine structure constant.

Two structural findings for the next pass: the outcome schema needs **FLUCTUATION** and
**MISCONDUCT** labels and multi-labelling (3 rows in 39 do not fit), and **outcome labels have a
shelf life** — the muon g−2 row had to be reclassified mid-catalogue after the 2025 White Paper,
and the reactor anomaly was declared closed in 2021 and has partly revived. Any base rate needs
an as-of date.

## Four discriminating features — tested, and three of four damaged

These were stated with one or two supporting examples each and never tested. They have now been
run against the historical record with a deliberate counterexample hunt.

### 1. Same-method disagreements are systematics — SUPPORTED BUT NARROWER

Newton's constant is a **better** confirming case than the ones originally cited:
torsion-balance-dominated, parts in 10⁴ apart, with no new physics on offer.

But **"same method" is undefined here, and in practice gets assigned after the answer is
known** — which makes the rule unfalsifiable as used. Under the note's own coarse convention,
SNO charged-current versus Super-K elastic-scattering counts as same-method, and that
disagreement was real physics.

### 2. Single-group claims resolve against the claimant — REFUTED

Three vindicated single-group claims: **Homestake**, **CP violation (1964)**, **Wu (1957)**.

**The number of groups predicts nothing.** What predicts is the *cost and motivation of the
check*.

**The corollary is worse — UNTESTABLE AS STATED, and directionally wrong.** It said that when
outsiders could check cheaply and have not in a decade, the absence is itself the result. It
cannot separate *obviously false* from *unfundable*. And its own flagship case refutes its
premise: **DAMA was checked**, by two purpose-built same-target experiments — ANAIS-112 and
COSINE-100 — precisely because refuting it was publishable.

### 3. Prior-choice fragility is diagnostic — SUPPORTED BUT NARROWER

TDCOSMO IV (2% → 8–9%, verified), BICEP2 and EDGES all confirm it. But it runs **one direction
only**: OPERA was prior-robust and wrong; the standard solar model was prior-fragile and right.

**Fragility indicts the number, not the phenomenon.**

### 4. Interesting survivors are over-determined — SUPPORTED BUT NARROWER, and our example was wrong

**The flagship case is factually incorrect.** The note said an independent relation picks a side
in the neutron lifetime. **It does not.** Meson-decay V_ud favours beam; superallowed 0⁺→0⁺
V_ud favours bottle. PERKEO III and aSPECT split the same way.

And over-determination predicts **resolvability, not new physics** — it delivered the solar
answer and dissolved the muon g−2 anomaly equally.

## The reframe that saves three of them

**Three of the four do not classify outcomes at all. They localise where the residual
uncertainty lives.** Read that way, every counterexample above is consistent with them.

That is a smaller claim and a true one, and it is probably the useful form.

## The counterexample that matters, and now matters twice

The solar neutrino problem fit the pattern exactly and **did** resolve to new physics. The rate
is not zero — it is uncomputed and era-biased.

**Homestake is also the single strongest counterexample to feature 2**: a single-group claim,
unreplicated for roughly two decades, whose default explanation for thirty years was a
systematic in the claimant's own apparatus or in Bahcall's model — and it resolved *for* the
claimant. This entry already listed solar neutrinos against the base rate. It had not noticed
the same case falsifies one of its own discriminating features.

Related: [[G17-overconfident-uncertainties]].
