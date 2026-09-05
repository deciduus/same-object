---
id: G32
name: G32-recovery-time-hazard-shape
type: gap
standing: narrowed
evidence: citation-intersection
contact-surface: 1
crosses: formalism
crosses-rank: 4
topology: mediated
mediator: fire-ecology-weibull-10.1016/S0065-2504(08)60216-0
borrows-from: ["[[C18-durability-axis]]"]
lends-to: []
mutual-with: []
computed-in: ["[[C29-recovery-beta]]", "[[C32-recovery-beta-replication]]"]
uses-move: []
rests-on: ["[[C18-durability-axis]]"]
tags: [node/gap, crosses/formalism, evidence/citation-intersection, standing/narrowed, narrowed/b-side-anchor]
last-checked: 2026-09-05
exit: computation
extends-to: [ecology, conservation]
next-step-cost: S
note: "NARROWED 2026-09-05 (audit 07): the B side was never varied, so the old zero measured who cites Weibull 1951, not who fits a Weibull. Re-run against survival-analysis anchors (Cox 1972, Kaplan-Meier 1958, Muenchow 1986) on OpenCitations 2026-09-05: fire ecology DOES cite them (Johnson & Gutsell 1994 x Cox = 11, x Kaplan-Meier = 3, x Muenchow = 2; Clark 1989 x Cox = 2, x Kaplan-Meier = 1), while the recovery meta-analyses do not (Jones & Schmitz and Moreno-Mateos 0 on all three; Pimm 2/1/0 and Crouzeilles 2/1/0, all six hits inspected and none fits a hazard to a recovery duration). The gap survives only as: RECOVERY ecology, not ecology, lacks the shape parameter. Johnson & Gutsell 1994 is reclassified from control to counter-example and mediator. Computation unchanged: C29 beta = 0.587 [0.510, 0.668]; C32 replication pooled beta = 0.733, per-habitat ordering fails (Spearman rho = 0.10, p = 0.95). Computation: C29 β = 0.587 on exact return times; C32 replication on current-status data yields NO identifiable shape (β 0.733 → 0.051 under the correct likelihood) and the per-habitat ordering fails (ρ = 0.10, p = 0.95); only the qualitative early-or-never shape survives."
---

# Recovery time as a hazard shape

**STANDING: NARROWED** · evidence: citation-intersection · contact surface: 1 · topology: mediated (fire ecology) · last checked 2026-09-05

> **Disturbance ecology and reliability engineering both estimate the distribution of a
> time-to-event under stress, and only one of them reports a distribution.** Ecology's
> `engineering resilience` is a *mean return time* or, equivalently, a single exponential return
> rate — one number per system (Pimm 1984). Reliability's answer to the same question is the pair
> `(β, η)`, and the shape `β` is the half that says which failure law is operating (Weibull 1951).
> This is [[C18-durability-axis]]'s central asymmetry — *everyone publishes the mean, one field
> also publishes the distribution* — restated on the recovery axis rather than the failure axis.
> **The gap claim, as re-scoped 2026-09-05: ecology's *recovery* literature — the return-time and
> restoration-meta-analysis line — has never imported the shape parameter. The unqualified form
> ("ecology has never imported it") is false: fire ecology fits Weibull hazards to fire intervals
> and cites the survival-analysis canon while doing it.**

## The two vocabularies

**Ecology, side A.** Pimm 1984, *The complexity and stability of ecosystems*, Nature 307:321–326,
`doi 10.1038/307321a0` (Crossref, fetched 2026-09-05: title, *Nature*, 1984, `is-referenced-by-count
= 2,406`). Pimm's resilience is *how fast a variable returns to equilibrium after a perturbation* —
operationalised as a return time, or its reciprocal a return rate, and in practice as the dominant
eigenvalue of the community matrix. One scalar per system, and it presupposes an exponential
approach: a **constant** relaxation rate.

**Ecology, side A', modern.** The recovery meta-analyses inherited the scalar and added a
yes/no. Jones & Schmitz 2009, *Rapid Recovery of Damaged Ecosystems*, *PLoS ONE* 4(5):e5653,
`doi 10.1371/journal.pone.0005653` (Crossref, fetched 2026-09-05, `is-referenced-by-count = 285`)
tabulate 240 studies as `Recovered? yes/no` plus a prose `Return Time`, and report **central
tendencies** by habitat and disturbance. Moreno-Mateos et al. 2017, *Anthropogenic ecosystem
disturbance and the recovery debt*, *Nature Communications* 8:14163, **`doi 10.1038/ncomms14163`**
(Crossref, fetched 2026-09-05, `is-referenced-by-count = 293`) report a *deficit* — the integrated
shortfall of a recovering system against its reference — again as a magnitude, not a hazard.
Crouzeilles et al. 2016, `doi 10.1038/ncomms11666` (Crossref, fetched 2026-09-05,
`is-referenced-by-count = 551`) meta-analyse forest-restoration success the same way.

> **DOI correction.** The Moreno-Mateos DOI carried into this note's brief,
> `10.1038/s41467-017-00109-4`, returns Crossref **HTTP 404**. The paper's DOI is
> `10.1038/ncomms14163`, recovered by Crossref bibliographic search 2026-09-05. No count in this
> note was ever run against the wrong DOI. Logged as a correction.

**Reliability, side B.** Weibull 1951, *A Statistical Distribution Function of Wide
Applicability*, *J. Appl. Mech.* 18:293–297, `doi 10.1115/1.4010337` (Crossref, fetched
2026-09-05, `is-referenced-by-count = 9,513`). `S(t) = exp(−(t/η)^β)`; `h(t) = (β/η)(t/η)^(β−1)`.
The **shape** `β` is dimensionless and is the whole content of the "which law" question:
`β > 1` rising hazard, `β = 1` memoryless, `β < 1` falling hazard.

**Why these are the same object and not an analogy.** Both estimate the distribution of a duration
from a disturbance to a defined threshold crossing, from censored observations. Ecology's
"not recovered after 19 years" *is* a right-censored observation, and it is already tabulated as
such in Jones & Schmitz's own supplement — the field records the censoring and then throws it away
by averaging the recovered rows. What is missing is not data. It is the estimator.

**Metaphor risk, stated up front.** Recovery runs the opposite direction from failure. A Weibull
fitted to recovery times describes assembly (colonisation, regrowth), so `β > 1` would read
"recovery becomes more likely the longer you wait", which is not damage accumulation and may be a
re-parameterised logistic rather than a hazard with a mechanism. And if recovery times are
lognormal because they are products of rates, `β` carries no mechanism at all. The gap is a gap in
the *instrument*; whether the instrument means anything is settled in [[C29-recovery-beta]] §6,
which does not fully clear it.

## What was searched

### Provenance

| | |
|---|---|
| **Provider (intersections, this run)** | **OpenCitations**, `api.opencitations.net/index/v1/citations/<doi>`, citer-DOI-set intersection per [[citation-intersection]] and `_scripts/intersect.py` |
| **Query date** | **2026-09-05** |
| **Header** | `User-Agent: biomimicry/1.0 (mailto:deciduusleaf@gmail.com)` |
| **DOI verification** | **Crossref**, `api.crossref.org/works/<doi>?mailto=deciduusleaf@gmail.com`, all six anchors, 2026-09-05 |
| **Coverage basis** | 100% of what OpenCitations indexes DOI-to-DOI; no reference lists were pulled, so this is not reference-list-coverage-limited (contrast G25's 28%). Works without a DOI are invisible |
| **Instrument substitution, stated** | **OpenAlex returned HTTP 429 on every intersection attempt for the whole session** (five agents on the polite pool concurrently), across ~25 retries with backoff to 90 s. The `cites:W_A,cites:W_B` server-side intersection this project prefers could **not** be run today. OpenCitations was substituted. Where an OpenAlex figure appears below it is **the scout's**, `audits/scout-02-resilience.md`, fetched 2026-09-05 — a different provider on a different coverage basis, quoted as such and never pooled with this run's numbers |
| **Data artefact caught** | OpenCitations returns a **blank `citing` DOI** in several citer lists. Joining on it manufactures a spurious intersection of exactly 1 in five of six pairings. Blank keys are stripped before intersecting; the raw pre-strip counts are given below so the artefact is on the record |

### Anchor pairs and counts

`N_A` = |citers(Weibull 1951)| = **9,239** (OpenCitations, blank stripped; 9,240 raw).
`E floor` uses `N = N_A + N_B − O`, which is the smallest defensible universe and therefore
**flatters the gap** — it is a floor and is never quoted alone. `E @ 15,057` uses the scout's
fetched OpenAlex concept-union `N` (`works?filter=concepts.id:C173291955|C2779720641,from_publication_date:2020-01-01`
→ `meta.count = 15,057`, Weibull distribution ∪ Ecological resilience, fetched 2026-09-05); that
window opens in 2020 and so is **strictly appropriate only to the Hillebrand row** — for the older
anchors it is an under-inclusive scope and is shown for sensitivity, not as the denominator.

| Pair | `N_B` | **O** | O raw (blank key) | `E` floor | `E` @ 15,057 | `E` @ 150,570 (10×) |
|---|---|---|---|---|---|---|
| **Weibull 1951 × Pimm 1984** | 2,445 | **0** | 1 | 1,933 | 1,500 | 150 |
| **Weibull 1951 × Jones & Schmitz 2009** | 286 | **0** | 1 | 277 | 175 | 17.6 |
| Weibull 1951 × Moreno-Mateos 2017 | 281 | **0** | 0 | 273 | 172 | 17.2 |
| Weibull 1951 × Crouzeilles 2016 | 560 | **0** | 1 | 528 | 344 | 34.4 |
| Weibull 1951 × Hillebrand & Kunze 2020 | 147 | **0** | 1 | 145 | **90.2** | 9.0 |
| *(counter-example, not a control — see below)* Weibull 1951 × Johnson & Gutsell 1994 (fire ecology) | 307 | **0** | 0 | 297 | 188 | 18.8 |

**Every `E` exceeds 1 at every denominator tried, including 10× the fetched one.** By
[[citation-intersection]]'s own rule that is the condition under which a zero is a finding, and it
is met with three orders of magnitude of margin on the Pimm row.

**Ecology-internal positive controls**, same instrument, same day — these are the load-bearing part,
because they show the pipeline detects the event whose absence is claimed:

| Control pair | O |
|---|---|
| Pimm 1984 × Crouzeilles 2016 | **31** |
| Jones & Schmitz 2009 × Moreno-Mateos 2017 | **10** |
| Pimm 1984 × Jones & Schmitz 2009 | **7** |
| Pimm 1984 × Moreno-Mateos 2017 | **7** |

The recovery literature is internally joined — a 2016 restoration meta-analysis and a 1984
return-time paper are co-cited 31 times — and joined to its own ancestor. It is not joined to
Weibull. Control ratio `(O/N_B)_gap / (O/N_B)_control` is **0** on every gap row by construction,
which is the strongest value the statistic takes.

**Hits inspected.** There were none to inspect: the true intersection is 0 in all six pairings.
The one thing that *was* inspected is the five spurious blank-DOI joins, which is why they are
reported rather than quietly dropped.

### Mode 6: the decade-binned re-run

[[failure-modes]] mode 6 says a pooled zero over a window this wide (Weibull 1951 → 2026) is six
measurements, not one, and a citer-set intersection anchored on a 1951 paper measures traffic
between *named papers*, not whether the object travelled under a later name. The required step is
to re-run under **each decade's own name for the ecological object**. Executed by using a
decade-appropriate side-A anchor rather than re-slicing one anchor:

| Decade | What that decade called the object | Side-A anchor | **O vs Weibull 1951** |
|---|---|---|---|
| 1980s | resilience / **return time**, relaxation rate | Pimm 1984 | **0** |
| 1990s | **fire-return interval** / time-since-disturbance | Johnson & Gutsell 1994 | **0** |
| 2000s | **recovery** / recovery rate | Jones & Schmitz 2009 | **0** |
| 2010s | **restoration success**, **recovery debt** | Crouzeilles 2016; Moreno-Mateos 2017 | **0**; **0** |
| 2020s | **pulse-disturbance recovery** | Hillebrand & Kunze 2020 | **0** |

And the citer windows are populated on both sides in every one of those decades, so no bin is
empty for want of literature (OpenCitations `creation` year of the citing work, 2026-09-05):

| Anchor | <1980 | 1980s | 1990s | 2000s | 2010s | 2020s | unknown |
|---|---|---|---|---|---|---|---|
| Weibull 1951 | 259 | 399 | 811 | 1,449 | 3,205 | 2,970 | 147 |
| Pimm 1984 | — | 48 | 136 | 329 | 835 | 1,057 | 41 |
| Johnson & Gutsell 1994 | — | — | 27 | 140 | 116 | 20 | 4 |
| Jones & Schmitz 2009 | — | — | — | 2 | 159 | 125 | 1 |
| Crouzeilles 2016 | — | — | — | — | 116 | 440 | 5 |
| Moreno-Mateos 2017 | — | — | — | — | 68 | 211 | 2 |
| Hillebrand & Kunze 2020 | — | — | — | — | — | 142 | 6 |

**The zero is a zero in every decade bin, under that decade's own name.** Weibull has thousands of
citers in each of the last four decades; ecology's recovery vocabulary has hundreds in each; the
overlap is empty throughout.

**One instrument discrepancy, recorded not resolved.** The scout reported Weibull 1951 × Johnson
& Gutsell 1994 = **1** on OpenAlex (a 1998 dendroecology fire-history paper). OpenCitations returns
**0** for the same pair today. Two providers, two DOI-coverage bases, and per `CLAUDE.md` neither
number is wrong until both are shown to measure the same object. The fire row is a *control*, not
a gap row, and the discrepancy makes it a weak control in either direction — it is reported for
that reason and nothing in the claim rests on it.

### The B side, varied (2026-09-05, audit 07 re-test)

Every row above anchors B on **Weibull 1951**, a *J. Appl. Mech.* methods paper. Users of a
distribution routinely cite neither its founding paper nor each other, so those zeros measure
*who cites a 1951 paper*, not *who fits a Weibull* — [[failure-modes]] mode 1 (the synonym trap)
on the B side, the mirror of the mode-6 step already run on A. This section runs the missing half.

**Provider.** OpenCitations, `api.opencitations.net/index/v1/citations/<doi>`, fetched
**2026-09-05**, `User-Agent: biomimicry/1.0 (mailto:deciduusleaf@gmail.com)`. Citer-DOI sets,
**blank `citing` keys dropped before intersecting**. Raw/clean citer counts:
Pimm 2,458/**2,445**; Jones & Schmitz 288/**286**; Moreno-Mateos 281/**281**; Crouzeilles
561/**560**; Johnson & Gutsell 307/**307**; Clark 1989 96/**96**; Cox 1972 35,957/**35,863**;
Kaplan–Meier 1958 38,157/**38,056**; Muenchow 1986 148/**148**.

**B-side anchors, Crossref-verified 2026-09-05.**

| Anchor | DOI | Title / venue |
|---|---|---|
| Cox 1972 | `10.1111/j.2517-6161.1972.tb00899.x` | *Regression Models and Life-Tables*, JRSS-B (`is-referenced-by-count` 36,657) |
| Kaplan & Meier 1958 | `10.1080/01621459.1958.10501452` | *Nonparametric Estimation from Incomplete Observations*, JASA (76,647) |
| Muenchow 1986 | **`10.2307/1938524`** | *Ecological Use of Failure Time Analysis*, *Ecology* 67(1) — ecology's own survival-analysis primer |
| Johnson & Gutsell 1994 | `10.1016/S0065-2504(08)60216-0` | *Fire Frequency Models, Methods and Interpretations*, Adv. Ecol. Res. 25 (294) |
| Clark 1989 | **`10.2307/3566083`** | *Ecological Disturbance as a Renewal Process*, *Oikos* 56(1) |

> **Two DOI corrections made here.** The Muenchow DOI carried in the re-test brief,
> `10.2307/1938954`, resolves to a 1982 *Ecology* paper on cotton-rat thermoregulation — a wrong
> work, not a dead link. The correct DOI is `10.2307/1938524`, recovered by Crossref
> bibliographic search 2026-09-05. Clark 1989 had no DOI on file and is `10.2307/3566083`.

`E` floors below use the union floor `N = N_A + N_B − O`; it flatters the gap and is labelled as a
floor. What carries the section is not `E` but the **contrast between the two A-side blocks**,
which share the B side and therefore need no denominator at all.

| A anchor | B anchor | `N_A` | `N_B` | **O** | `E` floor | `O/E` |
|---|---|---|---|---|---|---|
| **Recovery ecology** | | | | | | |
| Pimm 1984 | Cox 1972 | 2,445 | 35,863 | **2** | 2,289.1 | 0.0009 |
| Pimm 1984 | Kaplan–Meier 1958 | 2,445 | 38,056 | **1** | 2,297.5 | 0.0004 |
| Pimm 1984 | Muenchow 1986 | 2,445 | 148 | **0** | 139.6 | 0 |
| Jones & Schmitz 2009 | Cox 1972 | 286 | 35,863 | **0** | 283.7 | 0 |
| Jones & Schmitz 2009 | Kaplan–Meier 1958 | 286 | 38,056 | **0** | 283.9 | 0 |
| Jones & Schmitz 2009 | Muenchow 1986 | 286 | 148 | **0** | 97.5 | 0 |
| Moreno-Mateos 2017 | Cox 1972 | 281 | 35,863 | **0** | 278.8 | 0 |
| Moreno-Mateos 2017 | Kaplan–Meier 1958 | 281 | 38,056 | **0** | 278.9 | 0 |
| Moreno-Mateos 2017 | Muenchow 1986 | 281 | 148 | **0** | 96.9 | 0 |
| Crouzeilles 2016 | Cox 1972 | 560 | 35,863 | **2** | 551.4 | 0.0036 |
| Crouzeilles 2016 | Kaplan–Meier 1958 | 560 | 38,056 | **1** | 551.9 | 0.0018 |
| Crouzeilles 2016 | Muenchow 1986 | 560 | 148 | **0** | 117.1 | 0 |
| **Fire ecology** | | | | | | |
| Johnson & Gutsell 1994 | Cox 1972 | 307 | 35,863 | **11** | 304.5 | 0.036 |
| Johnson & Gutsell 1994 | Kaplan–Meier 1958 | 307 | 38,056 | **3** | 304.6 | 0.0099 |
| Johnson & Gutsell 1994 | Muenchow 1986 | 307 | 148 | **2** | 100.3 | 0.020 |
| Clark 1989 | Cox 1972 | 96 | 35,863 | **2** | 95.7 | 0.021 |
| Clark 1989 | Kaplan–Meier 1958 | 96 | 38,056 | **1** | 95.8 | 0.010 |
| Clark 1989 | Muenchow 1986 | 96 | 148 | **0** | 58.2 | 0 |

And the two A-side blocks against each other (recovery ↔ fire):

| Pair | O | Hit |
|---|---|---|
| Jones & Schmitz 2009 × Clark 1989 | **1** | `10.1016/j.biocon.2013.08.029`, *Challenges of ecological restoration: lessons from forests in northern Europe*, Biol. Conserv. 2013 |
| Pimm 1984 × Johnson & Gutsell 1994 | 0 | — |
| Pimm 1984 × Clark 1989 | 0 | — |
| Jones & Schmitz 2009 × Johnson & Gutsell 1994 | 0 | — |
| Moreno-Mateos 2017 × Johnson & Gutsell 1994; × Clark 1989 | 0; 0 | — |
| Crouzeilles 2016 × Johnson & Gutsell 1994; × Clark 1989 | 0; 0 | — |

**Every hit inspected (Crossref titles, 2026-09-05).**

*Recovery block, six hits, none of them a hazard fitted to a recovery duration:*

| Hit | What it is | Verdict |
|---|---|---|
| `10.1057/s41299-017-0014-7` | *Influence Your Firm's Resilience Through Its Reputation*, Corporate Reputation Review 2017 | not ecology at all |
| `10.1098/rspb.2004.2722` | *Life-history trade-offs and ecological dynamics in the evolution of longevity*, Proc. B 2004 | survival analysis of **organism** lifespan, not ecosystem recovery |
| `10.1186/s44419-025-00002-z` | kelp sporophyte sensitivity to marine heatwaves, Ocean Ecosystems 2026 | survival of individuals under heatwave; no recovery-time hazard |
| `10.1016/j.biocon.2013.08.029` | *Challenges of ecological restoration*, Biol. Conserv. 2013 | narrative review; co-cites, does not fit |
| `10.1111/rec.12879` | transgenic chestnut litter and **wood frog larval** survival, Restor. Ecol. 2018 | Cox model on tadpole survival in a restoration experiment |
| `10.1177/1940082918807178` | enrichment-planted **seedling** performance, Trop. Conserv. Sci. 2018 | Cox model on seedling survival |
| `10.1016/j.ecoleng.2021.106237` | cloud-forest **tree-species** performance, Ecol. Eng. 2021 | Kaplan–Meier on planted-tree survival |

So where recovery ecology touches survival analysis at all, it fits a hazard to the **survival of
individual organisms** — a seedling, a tadpole, a kelp sporophyte — never to the **duration of an
ecosystem's return to a reference state**, which is the object of this gap.

*Fire block, on point:*

| Hit | What it is |
|---|---|
| `10.3390/f7070131` | ***Quantifying Fire Cycle from Dendroecological Records Using Survival Analyses***, Forests 2016 — the object, explicitly |
| `10.1071/wf12021` | fire frequency in northern-Australian savannas from a satellite fire atlas, IJWF 2012 |
| `10.1139/x05-005` | fire frequency, Timiskaming mixedwood, Can. J. For. Res. 2005 |
| `10.1890/1051-0761(2000)010[0225:wpwaow]2.0.co;2` | ***White pine weevil attack on white spruce: a survival time analysis***, Ecol. Appl. 2000 |
| `10.1002/2017jg003826` | forest **fire cycles** post-Little-Ice-Age, JGR-Biogeosciences 2017 |
| the remaining 8 Cox / Kaplan–Meier co-citers | all fire-interval or forest-disturbance survival fits (e.g. `10.1016/j.foreco.2016.10.035`, `10.1071/wf15120`, `10.3390/f7100211`) |

One of the Clark 1989 × Cox 1972 co-citers is **Johnson & Gutsell 1994 itself**
(`10.1016/s0065-2504(08)60216-0` is in both citer sets): the review that tabulates fire-interval
Weibull shape and scale parameters cites the survival-analysis canon while doing it.

## Counter-example: fire ecology already has the shape parameter

**Johnson & Gutsell 1994 is not a control and never was.** It is *Fire Frequency Models, Methods
and Interpretations* (Adv. Ecol. Res. 25, Crossref-verified `10.1016/S0065-2504(08)60216-0`) — an
ecology review **of Weibull hazard fitting**, which tabulates shape and scale parameters for named
boreal and chaparral stands. `audits/scout-02-resilience.md` §3 said so plainly at the time:

> "fire ecology *does* touch Weibull - it just does not touch maintenance theory"

and proposed closing that scout's candidate 3 using "Johnson & Gutsell's tabulated **shape and
scale** parameters". This note demoted that sentence into a control row and kept the unqualified
claim. That was the error; it is corrected here. The fire row is the **counter-example**, and its
zero against Weibull 1951 is now positively explained — fire ecology reaches the Weibull hazard
through Cox, Kaplan–Meier and Muenchow, not through the 1951 paper.

A control that does not fire is not a control. The four **ecology-internal** controls above do that
job and are unaffected.

## Topology: mediated, and the mediator is fire ecology

The two literatures are not disjoint for want of a concept; they are separated by one hop. Fire
ecology holds the estimator (11 / 3 / 2 co-citers with the survival canon) and is co-cited with the
recovery literature exactly **once** (Jones & Schmitz × Clark 1989 = 1,
`10.1016/j.biocon.2013.08.029`). The path recovery-ecology → fire-ecology → hazard-shape exists and
is one hit wide at its first leg, which is why `topology` is now `mediated`, `mediator` is Johnson
& Gutsell 1994, and `contact-surface` is **1** — the gap-unfavourable reading, recording that one
co-citation rather than the 0 hits of the exactly-right kind.


## What survives

**The claim survives in a narrowed form, and it is still a formalism gap rather than a word gap.**
What does not survive is the general form. *Ecology* has the shape parameter: fire ecology fits
Weibull hazards to fire intervals and cites Cox, Kaplan-Meier and Muenchow while doing it. What
survives is the *recovery* scope — the return-time line (Pimm) and the restoration and
recovery-debt meta-analyses (Jones & Schmitz, Moreno-Mateos, Crouzeilles) report a mean, a yes/no
or a deficit, and their only contact with survival analysis is at the level of an individual
organism's survival, never the duration of an ecosystem's return. Both fields carry a quantified
estimator for the same censored duration; recovery ecology's estimator is a first moment and
reliability's is a two-parameter distribution. What does **not** survive is any presumption that importing `β` carries a mechanism with
it — see the metaphor risk above and [[C29-recovery-beta]] §6.

## What would close it

**The missing object is a fitted `β` for ecological recovery times.** That is a computation, not a
reading, and the data are already public in the ecology field's own supplements. It has now been
run: **[[C29-recovery-beta]]** fits Jones & Schmitz's Table S1 as a right-censored survival problem
and returns pooled `β = 0.587` (95% profile CI 0.510–0.668) with `β < 1` clear of 1 in four of five
habitat classes — the *decreasing*-hazard corner of [[C18-durability-axis]]'s axis, opposite Li-ion
wear-out.

What that leaves open, and what would close the gap rather than the computation:

1. **Reproduce the per-habitat `β` ordering on an independent recovery dataset** (Moreno-Mateos
   2017 or Crouzeilles 2016). [[C29-recovery-beta]] §5 states the prediction as the sign of a rank
   correlation, which is falsifiable and cheap.
   **Run 2026-09-05 and failed:** [[C32-recovery-beta-replication]] refits on Moreno-Mateos 2017 and
   gets pooled `β = 0.733 [0.703, 0.764]` (so `β < 1` replicates) but Spearman `ρ = +0.100`, n = 5,
   p = 0.950 on the per-habitat ordering, flipping to `−0.300` at study level — `β` does not resolve
   between ecosystem types.
2. **Separate frailty from mechanism** by re-fitting within a single response-variable class. If
   `β` rises toward 1 within class while the pooled `β` stays at 0.59, the finding is
   heterogeneity, not deceleration — and that is still a result, just a different one.
3. **A published ecological recovery `β`, by an ecologist, in an ecology venue** would close the
   gap in the sense that matters: the point is not that the number cannot be computed but that the
   field has never adopted the estimator.

Neighbouring work on the same instrument: [[C26-ews-hazard-shape]] (hazard shape implied by an early-warning indicator; its gap note
`G29-early-warning-prognostics` is being opened in parallel and is not yet linkable here), and
[[C27-product-lifespan-beta]] via [[G30-weibull-product-lifespan]] (the same estimator on
consumer-product lifespans).

## Corrections 2026-09-05 (audit 07)

1. **The B-side anchor was never varied** — every row of the anchor-pair table sat on Weibull 1951,
   so the zero measured citation traffic to one 1951 *J. Appl. Mech.* paper, not use of the
   estimator. Fixed by *The B side, varied*: three survival-analysis B anchors × six A anchors,
   OpenCitations 2026-09-05.
2. **The claim was overstated.** "Ecology's recovery literature has never imported the shape
   parameter" was written and read as if it said "ecology has never imported it". The general form
   is **false**; the narrow form holds. Blockquote, *What survives*, `note:` and the STANDING line
   are re-scoped to *recovery* ecology.
3. **Johnson & Gutsell 1994 was mislabelled a positive control.** It is the counter-example — an
   ecology review of Weibull hazard fitting — and is now a named counter-example and the
   `mediator`. `audits/scout-02-resilience.md` §3 said this before this note was written.
4. **`standing: live` → `narrowed`; `topology: disjoint` → `mediated`; `contact-surface: 0` → `1`.**
   The surviving gap is narrower than the one first opened: recovery ecology, not ecology.
5. **Two anchor DOIs corrected/added.** Muenchow 1986 is `10.2307/1938524`, not `10.2307/1938954`
   (which resolves to a 1982 cotton-rat thermoregulation paper). Clark 1989 is `10.2307/3566083`.
6. **Instrument note.** `_scripts/intersect.py` was **not** used; its current version carries the
   blank-`citing`-key bug this note already documented. A purpose-written fetch dropping empty
   `citing` values before set construction produced every number in *The B side, varied*.
7. **Not fixed here** (other audit-07 items, other files): the ecology-internal control range
   printed as 7–31 where the blanks-stripped values are 6–30, and the two anchor DOIs missing from
   the Provenance block for Hillebrand & Kunze 2020 (`10.1111/ele.13457`) and Johnson & Gutsell
   1994 (`10.1016/S0065-2504(08)60216-0`), recorded above instead.
