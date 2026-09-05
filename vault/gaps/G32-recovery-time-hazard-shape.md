---
id: G32
name: G32-recovery-time-hazard-shape
type: gap
standing: live
evidence: citation-intersection
contact-surface: 0
crosses: formalism
crosses-rank: 4
topology: disjoint
mediator:
borrows-from: ["[[C18-durability-axis]]"]
lends-to: []
mutual-with: []
computed-in: ["[[C29-recovery-beta]]"]
uses-move: []
rests-on: ["[[C18-durability-axis]]"]
tags: [node/gap, crosses/formalism, evidence/citation-intersection, standing/live]
last-checked: 2026-09-05
exit: computation
extends-to: [ecology, conservation]
next-step-cost: S
note: "Ecology reports a mean return time where reliability reports a hazard shape. Weibull 1951 x five recovery/return-time anchors: intersection 0 on OpenCitations, every decade bin, against E floors 145-1933. Ecology-internal controls 7-31. Closed by computation in C29: beta = 0.587 [0.510, 0.668], decreasing hazard."
---

# Recovery time as a hazard shape

**STANDING: LIVE** · evidence: citation-intersection · contact surface: 0 · last checked 2026-09-05

> **Disturbance ecology and reliability engineering both estimate the distribution of a
> time-to-event under stress, and only one of them reports a distribution.** Ecology's
> `engineering resilience` is a *mean return time* or, equivalently, a single exponential return
> rate — one number per system (Pimm 1984). Reliability's answer to the same question is the pair
> `(β, η)`, and the shape `β` is the half that says which failure law is operating (Weibull 1951).
> This is [[C18-durability-axis]]'s central asymmetry — *everyone publishes the mean, one field
> also publishes the distribution* — restated on the recovery axis rather than the failure axis.
> **The gap claim is that ecology's recovery literature has never imported the shape parameter.**

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
| **control** Weibull 1951 × Johnson & Gutsell 1994 (fire ecology) | 307 | **0** | 0 | 297 | 188 | 18.8 |

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

## What survives

**The claim survives in its strong form, and it is a formalism gap rather than a word gap.** Both
fields carry a quantified estimator for the same censored duration; ecology's estimator is a first
moment and reliability's is a two-parameter distribution, and no work cites both anchors in any
decade. What does **not** survive is any presumption that importing `β` carries a mechanism with
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
