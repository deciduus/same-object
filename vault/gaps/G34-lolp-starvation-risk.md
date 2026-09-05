---
id: G34
name: G34-lolp-starvation-risk
type: gap
standing: live
evidence: citation-intersection
contact-surface: 0
crosses: formalism
crosses-rank: 4
topology: disjoint
mediator: 
borrows-from: []
lends-to: []
mutual-with: []
computed-in: ["[[C33-lolp-starvation]]"]
uses-move: []
rests-on: ["[[availability-formula]]"]
tags: [node/gap, crosses/formalism, evidence/citation-intersection, standing/live]
last-checked: 2026-09-05
exit: computation
extends-to: [sustainability, ecology]
next-step-cost: S
note: "Power-system adequacy and small-bird winter energetics both compute P(a stored reserve hits zero before a horizon) by backward stochastic dynamic programming, and both read the shadow price off the same value function. Four anchor pairings, intersection 0 in every decade bin, against E floors 166-350; same-side controls 25.2% and 12.8% of the smaller set."
---

# Loss-of-load probability and starvation risk are the same first-passage problem

**STANDING: LIVE** · evidence: citation-intersection · contact surface: 0 · last checked 2026-09-05

> Power-system reliability engineering asks *what is the probability that a stored reserve hits
> zero before the horizon ends, given stochastic income and a stochastic draw* and calls the
> answer **loss-of-load probability**. Behavioural ecology asks the identical question of an
> overwintering bird's fat reserve and calls the answer **starvation probability**. Both solve it
> by backward stochastic dynamic programming on a value function over the reserve state; both
> read a shadow price off the derivative of that value function — **value of lost load** on one
> side, **marginal fitness value of a unit of fat** on the other. Two quantities matching, not
> one, and across four anchor pairings the two literatures have never co-cited a single work.

## The two vocabularies

| | **Power systems** | **Behavioural ecology** |
|---|---|---|
| State | state of charge / available capacity margin | fat reserve `x`, in kJ or g |
| Income | generation, stochastic (outages, wind, solar) | foraging gain, stochastic (Bernoulli success) |
| Draw | load, stochastic | metabolic expenditure, weather-dependent |
| Absorbing boundary | unserved demand | `x = 0`, death by starvation |
| Estimand | **LOLP** (dimensionless), **LOLE** (d/yr), **LOLH** (h/yr) | **starvation probability over a winter** (dimensionless) |
| Method | backward recursion / convolution of a state-of-charge process | backward stochastic dynamic programming on `V(x,t)` |
| Shadow price | **value of lost load** (VoLL, currency per MWh unserved) | **marginal value of reserves** `∂V/∂x` (fitness per unit fat) |
| Design lever | storage sizing; **planning reserve margin**, % of peak | **optimal fat reserve**; state-dependent foraging |
| Demand-side lever | demand response, load shedding | nocturnal hypothermia, torpor |

The ecology side's canon for this: McNamara & Houston, *Starvation and Predation as Factors
Limiting Population Size*, **Ecology 68(5):1515–1519 (1987)**, DOI `10.2307/1939235` — Crossref
`is-referenced-by-count` 407, fetched 2026-09-05; and Houston & McNamara, *A Theoretical
Investigation of the Fat Reserves and Mortality Levels of Small Birds in Winter*, **Ornis
Scandinavica 24(3):205–219 (1993)**, DOI `10.2307/3676736` — Crossref count 195, fetched
2026-09-05. **Both DOIs resolved live**; the Ornis Scandinavica DOI is the one this note asserts
and it is the only Crossref record carrying that exact title.

The power side's canon: Billinton & Allan, *Reliability Evaluation of Power Systems* (Springer,
1996), DOI `10.1007/978-1-4899-1860-4`, Crossref count 2,095; and Billinton & Li, *Reliability
Assessment of Electric Power Systems Using Monte Carlo Methods* (Springer, 1994), DOI
`10.1007/978-1-4899-1346-3`, Crossref count 1,095. Both fetched 2026-09-05.

## Provenance — re-derived counts, blank keys dropped

**Provider** OpenCitations, endpoint `https://api.opencitations.net/index/v1/citations/<doi>`.
**Run 2026-09-05** by `vault/_scripts/c33_lolp.py cites`, which carries its own fetcher rather
than `intersect.py` (whose blank-key handling was under repair at the time of this run).
**6 records with an empty `citing` key were dropped across the six anchor fetches.** That
filter is load-bearing here: the phantom `""` element joins every set, so an unfiltered run
would have reported each of the four zeros below as **1**.

| Pairing | `N_A` | `N_B` | **O** | `N` floor | `E` (floor) | O as % of smaller set |
|---|---|---|---|---|---|---|
| **Billinton & Allan 1996 × McNamara & Houston 1987** | 2,058 | 422 | **0** | 2,480 | 350.2 | 0.00% |
| **Billinton & Li 1994 × Houston & McNamara 1993** *(second anchor pair)* | 1,094 | 196 | **0** | 1,290 | 166.2 | 0.00% |
| Billinton & Allan 1996 × Houston & McNamara 1993 | 2,058 | 196 | **0** | 2,254 | 179.0 | 0.00% |
| Billinton & Li 1994 × McNamara & Houston 1987 | 1,094 | 422 | **0** | 1,516 | 304.5 | 0.00% |
| **Control, power × power:** Billinton & Allan × Billinton & Li | 2,058 | 1,094 | **276** | 2,876 | 782.8 | **25.23%** |
| **Control, ecology × ecology:** McNamara & Houston × Houston & McNamara | 422 | 196 | **25** | 593 | 139.5 | **12.76%** |

`N_A = 2,058` and `N_B = 422` reproduce `audits/scout-06-energy-systems.md` exactly, and the
ecology-side control reproduces its 25. **Read the separation off the last column, not off
`O/E`**: at the union floor `E` is inflated enough that the joined controls themselves sit at
`O/E` = 0.35 and 0.18, so `O/E` does not discriminate in this domain. Joined literatures return
12.8–25.2% of the smaller set here; all four cross-domain pairings return 0.00%.

**`N` is a union floor throughout, and is labelled as one.** No concept-scoped OpenAlex
denominator was fetched for this note (see *What could not be fetched*), so the `E` column is
the largest defensible `E` and therefore flatters the claim, per [[citation-intersection]].

### Mode-6 decade re-run

[[failure-modes]] mode 6 requires that a zero spanning more than one decade be reported per
decade under that decade's own name, not pooled. OpenCitations `/citations/` records carry a
`creation` date for the citing work, so both citer sets were binned by decade and the
intersection recomputed **inside each bin**. Every bin is zero on every pairing:

| Decade | Billinton & Allan citers | Billinton & Li citers | McN & H 1987 citers | H & McN 1993 citers | **O, any pairing** |
|---|---|---|---|---|---|
| 1980s | 0 | 0 | 31 | 0 | **0** |
| 1990s | 16 | 21 | 72 | 31 | **0** |
| 2000s | 379 | 203 | 119 | 62 | **0** |
| 2010s | 1,127 | 567 | 113 | 59 | **0** |
| 2020s | 424 | 244 | 85 | 42 | **0** |
| undated | 112 | 59 | 2 | 2 | **0** |

The two controls are *not* flat across decades (power × power: 2 / 75 / 132 / 50; ecology ×
ecology: 0 / 4 / 12 / 6 / 3), which is the check that the binning has resolution. The 1980s row
is the one bin where mode 6 could still bite: the grid anchors are 1994 and 1996, so no citer of
theirs can exist before 1994, and the 31 pre-1990 ecology citers are compared against an empty
set. **That bin is uninformative rather than a zero**, and the honest window for this finding is
**1994 onwards**, where both sides are populated and all four pairings are zero.

The 1980s vocabulary question is answered separately and negatively for the concept: the grid
side already used *loss-of-load probability* under that name in the 1960s–70s (Telson, *The
Economics of Alternative Levels of Reliability for Electric Power Generation Systems*, **Bell J.
Econ. 6(2) (1975)**, DOI `10.2307/3003250`, Crossref count 97, fetched 2026-09-05, is the
standard citation for the 1-day-in-10-years criterion), and the ecology side used *starvation
risk* and *energy reserves* from Lima 1986 onward. The two names did not drift; they coexisted
and stayed apart.

## Hits inspected

**There are none to inspect on the four cross-domain pairings** — the intersection is empty, so
the inspection burden falls on the controls instead, and both were inspected to confirm the
pipeline detects contact when it exists:

- **Power × power, 276 hits**, sampled: `10.1109/tpwrs.2012.2227843`, `10.1109/tsg.2012.2190997`,
  `10.1109/tr.2013.2241133`, `10.3390/en12030343` — all IEEE/MDPI power-system reliability, i.e.
  the expected joined population.
- **Ecology × ecology, all 25 hits enumerated**, including `10.1006/anbe.1996.0279`,
  `10.1086/664457` (*The Starvation-Predation Trade-Off Predicts Trends in Body Size,
  Muscularity, and Adiposity*), `10.1098/rspb.2015.2443`, `10.1111/j.1461-0248.2007.01088.x`.
  Every one is behavioural ecology or ornithology; none is engineering.

**What was not inspected:** no third-party bridge search was run outside the citer sets — a
paper citing *neither* anchor while making the connection would be invisible to this instrument.
That is the standing limitation of citer-set intersection and it is not repaired here.

## What survives

The claim as stated survives, with one scope restriction taken from the scout's own adversarial
objection and adopted here rather than argued with. **The comparison is not to classic
LOLP-of-a-thermal-fleet.** Classic LOLP convolves a capacity-outage probability table against a
load-duration curve and has no integrated state at all, so there is no reserve and no
first-passage problem — that version of the grid side is *not* the same object as the bird's fat
reserve, and if the gap were scoped to it the gap would be false. **The comparison is to
storage-constrained adequacy**: LOLE computed on a system whose adequacy depends on a
state-of-charge trajectory. That is the modern variable-renewables-plus-storage formulation, it
is exactly a first-passage problem, and it is the scope this note claims.

`crosses: formalism` (rank 4) rather than `data`: the two fields share the dynamic program and
the shadow-price construction, but no dataset has been put through both.

## What would close it

Closed in one motion by [[C33-lolp-starvation]], which (i) writes both problems in one notation
and shows the LOLP recursion and the starvation backward equation are the same dynamic program,
(ii) computes a published bird model's winter starvation probability as an LOLE and a published
grid criterion as a per-night starvation risk, and (iii) states the bird's optimal reserve as a
planning reserve margin against the grid's 15–20% convention. What C33 does **not** do, and what
would finish the job: put one dataset through both formalisms — take a real state-of-charge
trace from a storage-constrained adequacy study and a real dusk-fat/overnight-expenditure series
from a wintering parid, and fit the same first-passage model to both. That is the step from
`crosses: formalism` to `crosses: data`. See [[what-closes-a-gap]].

## What could not be fetched

- **A concept-scoped `N_universe` from OpenAlex.** Not attempted for this note; the OpenAlex leg
  the scout report asks for (it lost its one probe to HTTP 429) is still outstanding, so every
  number here is **single-provider**, one instrument short of this project's two-sources standard.
- **Houston & McNamara 1993 full text.** Paywalled at JSTOR; the DOI, title, journal, volume,
  pages and Crossref citation count were verified, the model's parameter values were not. C33
  therefore takes its bird parameters from an open-access successor model rather than from this
  anchor, and says so.

See [[C33-lolp-starvation]], [[C1-availability-living-tissue]], [[availability-formula]],
[[citation-intersection]], [[failure-modes]], [[positive-controls]].
