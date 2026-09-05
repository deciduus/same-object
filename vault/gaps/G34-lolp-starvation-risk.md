---
id: G34
name: G34-lolp-starvation-risk
type: gap
standing: narrowed
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
tags: [node/gap, crosses/formalism, evidence/citation-intersection, standing/narrowed]
last-checked: 2026-09-05
exit: computation
extends-to: [sustainability, ecology]
next-step-cost: S
note: "Power-system adequacy and small-bird winter energetics propagate the same stochastic reserve recursion by backward SDP and read the same shadow price off the value function, but aggregate it into different functionals - expected occupation time on the grid, first passage in the bird - so the shared object is the recursion and the shadow price, not the estimand. Both are special cases of a ruin-theory parent (Lundberg 1903) that neither field cites: a triple zero. In-scope storage-constrained pairing Denholm & Hand 2011 x Houston & McNamara 1993 gives 794 x 196, intersection 0; the four Billinton anchors are the classic static COPT x LDC literature this note disclaims and are retained as an out-of-scope control. Two providers: OpenCitations four pairings 0, Semantic Scholar 4x4 grid 0 in all sixteen cells and every decade bin, 2,713 grid citers against 906 bird citers with no work in both. Pooled E = 55.5 at a scoped N of 44,299 and 5.55 at 10x. Narrowed 2026-09-05: the headline first-passage framing and C33's P(starve) were wrong; the structural identity survives."
---

# Loss-of-load probability and starvation risk are the same reserve recursion, read out by different functionals

**STANDING: NARROWED** · evidence: citation-intersection · contact surface: 0 · last checked 2026-09-05

> **Narrowed 2026-09-05.** Power-system reliability engineering propagates a stored reserve under
> stochastic income and a stochastic draw and reports **how much time the reserve spends at or
> below zero** — loss-of-load probability and its aggregate, loss-of-load expectation. Behavioural
> ecology propagates the same state under the same drivers and reports **whether an overwintering
> bird's fat reserve ever reaches zero** — starvation probability. **The state recursion is shared
> and the shadow price is shared; the estimand is not.** The grid's zero is a reflecting boundary
> and its statistic is an expected occupation time; the bird's zero is absorbing and its statistic
> is a first-passage probability. Both are special cases of a **ruin-theory** parent (Lundberg
> 1903, Cramér 1930) that **neither field cites** — a triple zero, of which the citation
> intersection below measures one branch. Across **twenty anchor pairings on two independent
> citation indexes** — four on OpenCitations, sixteen on Semantic Scholar spanning grid anchors
> from 1978 to 2020 against bird anchors from 1987 to 2017 — the two literatures have never
> co-cited a single work.

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

## Provenance — two providers, re-derived counts, blank keys dropped

### Provider 1: OpenCitations

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

**Anchor scope, stated against this note's own restriction.** The four Billinton pairings above
measure the **classic-LOLP** literature — a capacity-outage probability table convolved against a
load-duration curve, with no integrated state and therefore no reserve — which *"What survives"*
below explicitly places **outside this note's scope**. They are retained as an **out-of-scope
control**, not as the note's evidence. **The in-scope measurement is the storage-constrained
pairing, Denholm & Hand 2011 × Houston & McNamara 1993, `N_A` 794, `N_B` 196, ∩ = 0**
(`audits/scout-06-energy-systems.md` candidate #3, OpenCitations 2026-09-05; the same pairing is
cell G11 × B93 of the Semantic Scholar grid below, also 0). Until that pairing is re-run inside
this note with its own decade bins, the in-scope zero is **imported, not measured here**.

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

---

## Second provider: Semantic Scholar, 4x4 anchor grid

**OpenAlex was attempted first and refused.** `api.openalex.org/works/https://doi.org/10.2307/1939235?mailto=deciduusleaf@gmail.com`,
2026-09-05, returns HTTP 429 `{"error":"Rate limit exceeded","message":"Insufficient budget …
Resets at midnight UTC"}`. No OpenAlex number in this note is fetched; the concept-scoped
`N_universe` the previous revision listed as outstanding is therefore still not available from
OpenAlex, and the estimate below is a substitute, not that number.

**Provider** Semantic Scholar Graph API, endpoint
`https://api.semanticscholar.org/graph/v1/paper/DOI:<doi>/citations?fields=externalIds,title,year&limit=1000&offset=…`,
paginated to exhaustion, ~1.6 s between requests. **Run 2026-09-05** by a standalone fetcher
written for this leg (not `_scripts/intersect.py`, which was under concurrent repair).
Enumerated citer counts matched each anchor's own `citationCount` exactly on all eight anchors,
so no pagination was truncated. Intersections were computed on `paperId` **and** re-computed on
normalised DOI as a duplicate-record check; the two agree everywhere.

**Anchor set widened to test [[failure-modes]] mode 6 properly.** The previous revision's grid
side was two 1990s books, so its 1980s bin was structurally empty. Four anchors per side, one
per decade of first publication:

| | Anchor | DOI | Year | S2 citers |
|---|---|---|---|---|
| **G78** | Billinton & Harrington, *Reliability Evaluation in Energy Limited Generating Capacity Studies*, IEEE Trans. PAS | `10.1109/tpas.1978.354711` | 1978 | 74 |
| **G94** | Billinton & Li, *Reliability Assessment … Monte Carlo Methods* | `10.1007/978-1-4899-1346-3` | 1994 | 1,595 |
| **G11** | Denholm & Hand, *Grid flexibility and storage required …*, Energy Policy | `10.1016/j.enpol.2011.01.019` | 2011 | 955 |
| **G20** | *Additional Capacity Value From Synergy of Variable Renewable Energy and Energy Storage*, IEEE Trans. Sust. Energy | `10.1109/tste.2019.2940421` | 2020 | 93 |
| **B87** | McNamara & Houston, Ecology | `10.2307/1939235` | 1987 | 551 |
| **B93** | Houston & McNamara, Ornis Scand. | `10.2307/3676736` | 1993 | 260 |
| **B06** | Brodin, *Theoretical models of adaptive energy management in small wintering birds*, Phil. Trans. R. Soc. B | `10.1098/rstb.2006.1812` | 2006 | 117 |
| **B17** | Brodin, Nilsson & Nord, *Adaptive temperature regulation in the little bird in winter: predictions from a stochastic dynamic programming model*, Oecologia | `10.1007/s00442-017-3923-3` | 2017 | 44 |

**Billinton & Allan 1996 (`10.1007/978-1-4899-1860-4`) is not in Semantic Scholar** — the DOI
returns `Paper with id … not found`, 2026-09-05. The OpenCitations table's headline pairing
therefore has no Semantic Scholar counterpart, and G94 carries the 1990s grid decade here.

### The 4x4 grid: sixteen pairings, sixteen zeros

| **O** | B87 (1987) | B93 (1993) | B06 (2006) | B17 (2017) |
|---|---|---|---|---|
| **G78 (1978)** | 0 | 0 | 0 | 0 |
| **G94 (1994)** | 0 | 0 | 0 | 0 |
| **G11 (2011)** | 0 | 0 | 0 | 0 |
| **G20 (2020)** | 0 | 0 | 0 | 0 |

Union of the four grid citer sets **2,713**; union of the four bird citer sets **906**;
intersection of the two unions **0**. **Not one of 3,619 distinct works cites any grid anchor
and any bird anchor.** This agrees with the OpenCitations run, which used a partly different
anchor set and a wholly different citation index.

### Per-decade, both sides populated

Binning every citer by its own publication decade, the 1980s hole in the previous revision is
now closed: G78 has **19** citers in the 1980s and 11 in the 1990s, so the 1980s bin has a live
grid side to compare against B87's 34.

| Decade | G78 | G94 | G11 | G20 | B87 | B93 | B06 | B17 | **O, all 16 pairings** |
|---|---|---|---|---|---|---|---|---|---|
| 1980s | 19 | 0 | 0 | 0 | 34 | 0 | 0 | 0 | **0** |
| 1990s | 11 | 23 | 0 | 0 | 119 | 54 | 0 | 0 | **0** |
| 2000s | 12 | 355 | 0 | 0 | 162 | 82 | 7 | 0 | **0** |
| 2010s | 28 | 825 | 527 | 0 | 149 | 88 | 72 | 13 | **0** |
| 2020s | 4 | 385 | 422 | 92 | 82 | 35 | 37 | 31 | **0** |
| undated | 0 | 7 | 6 | 1 | 5 | 1 | 1 | 0 | **0** |

**The honest window widens from 1994-onwards to 1978-onwards.** Mode 6's objection to the
previous revision — that the pre-1994 zero was an artifact of anchor vintage, not a measurement
— no longer applies to the 1980s or 1990s rows.

### Null model at three denominators

`N` was not obtainable from OpenAlex. **Estimated instead from Semantic Scholar's
`paper/search/bulk` total**, boolean phrase match over title and abstract, `year=1987-2026`,
fetched 2026-09-05:

```
paper/search/bulk?query="power system reliability" | "resource adequacy" | "loss of load"
  | "generating capacity reliability" | "behavioral ecology" | "behavioural ecology"
  | "energy reserves" | "starvation risk" | "optimal foraging" | "energy homeostasis"
  &year=1987-2026                                            ->  total = 44,299
```

(The two halves separately: power terms **7,414**, ecology terms **36,895**.) **This is an
estimate, not a concept scope.** It is a phrase match on two term-lists this note chose, so it
inherits every weakness [[failure-modes]] lists for string queries; it is quoted only as a
denominator, never as a count of anything. It does pass the sanity check that voided the
[[citation-intersection]] G25 row: `N = 44,299` comfortably exceeds both citer-set unions.

Against the **pooled** measurement (`|A| = 2,713`, `|B| = 906`, `O = 0`):

| `N` | E = 2,713·906/N | O | O/E | verdict |
|---|---|---|---|---|
| **3,619 (union floor)** | **679.2** | 0 | **0** | finding, but floor flatters it |
| **44,299 (S2 bulk estimate)** | **55.5** | 0 | **0** | **finding — `E` far above 1** |
| 442,990 (10x, sensitivity) | 5.55 | 0 | **0** | **finding — `E > 1`** |
| 4,429,900 (100x) | 0.55 | 0 | — | *uninformative* |

**The zero survives two orders of magnitude of denominator**, which is the test
[[citation-intersection]] says G6 only barely passed and G28 failed. That robustness comes from
pooling: taken singly, only 5 of the 16 cells clear `E > 1` at the scoped `N` (largest
G94 x B87, `E = 19.8`; smallest G78 x B17, `E = 0.07`). **The load-bearing statistic here is the
pooled union, not any individual cell**, and the 4x4 grid's value is coverage of the decade
window, not sixteen independent tests.

### Same-side controls — and one that fails

| | `N_A` | `N_B` | **O** | O as % of smaller set |
|---|---|---|---|---|
| ecology: B93 x B06 | 260 | 117 | **25** | **21.4%** |
| ecology: B06 x B17 | 117 | 44 | **10** | **22.7%** |
| ecology: B87 x B93 | 551 | 260 | **28** | **10.8%** |
| ecology: B87 x B06 | 551 | 117 | 4 | 3.4% |
| ecology: B87 x B17 | 551 | 44 | 2 | 4.5% |
| ecology: B93 x B17 | 260 | 44 | 1 | 2.3% |
| power: G94 x G20 | 1,595 | 93 | 3 | 3.2% |
| power: G94 x G11 | 1,595 | 955 | **1** | **0.1%** |
| power: G11 x G20 | 955 | 93 | **0** | **0.00%** |
| power: G78 x G94, G78 x G11, G78 x G20 | 74 | 1,595 / 955 / 93 | **0** | **0.00%** |

**The ecology leg of this instrument is calibrated; the power leg is not.** Four of six power
controls return zero, including `G11 x G20` — two storage-adequacy papers nine years apart,
where contact is certain. That is a **positive-control failure**, and under
[[positive-controls]] it means a Semantic Scholar zero involving a grid anchor cannot be read as
absence of contact on its own.

**Diagnosed, not assumed.** Twelve of G20's 93 citers were pulled and their reference lists
inspected: **seven have no reference list in Semantic Scholar at all** (`references` returns
zero rows), and none of the remaining five records Denholm & Hand 2011. The mechanism is thin
reference-list coverage of the recent power-engineering corpus, not a genuine disjointness. So:

> **Semantic Scholar corroborates the zero; it does not independently establish it.**
> OpenCitations is the calibrated instrument here (power x power control **25.2%**, ecology x
> ecology **12.8%**), and the two-provider claim rests on OpenCitations' controls plus Semantic
> Scholar's agreement, its properly calibrated ecology leg, and its decade coverage.

### Controls inspected

First five of each nonzero control, newest first — all topically where they should be, so the
pipeline detects contact when it exists:

- **power G94 x G20 (3):** `10.1109/TIA.2022.3228977` (fast frequency response reserve
  planning), `10.1109/SyNERGYMED55767.2022.9941435` (*Capacity Value of Pumped-Hydro Energy
  Storage*), `10.3390/en14165146` (*Battery Energy Storage Contribution to System Adequacy*).
- **power G94 x G11 (1):** *The Potential of Energy Storage Systems with Respect to Generation
  Adequacy and Economic Viability* (2013).
- **ecology B87 x B93 (28):** `10.1007/s10641-021-01176-7`, `10.1111/OIK.03476`,
  `10.1098/rspb.2015.2443`, `10.1007/s11252-016-0546-0`, `10.1111/1365-2664.12383`.
- **ecology B93 x B06 (25):** `10.7120/09627286.31.1.013`, `10.1093/BEHECO/ARAA134`,
  `10.1111/JAV.01766`, and two 2019 records without DOIs.
- **ecology B06 x B17 (10):** `10.1016/j.jtherbio.2025.104059`, `10.1111/1365-2656.13999`,
  `10.1096/fj.202201613R`, and two 2022 bioRxiv preprints of the same two papers.
- **ecology B87 x B06 (4):** `10.1098/rspb.2015.2443`, `10.1890/13-1795.1`,
  `10.1098/rspb.2009.1000` (*How climate change might influence the starvation-predation risk
  trade-off response*).
- **ecology B87 x B17 (2):** `10.1098/rsbl.2019.0211`, `10.1098/rspb.2018.2370` — both torpor
  and energy-expenditure papers.
- **ecology B93 x B17 (1):** `10.1016/j.jtbi.2018.05.010`, *Optimal gut size of small birds*.

**Cross-domain hits requiring inspection: none.** All sixteen cells are empty, on `paperId` and
on DOI.

### One anchor DOI corrected

The 2000s bird anchor is **`10.1098/rstb.2006.1812`**, not `10.1098/rstb.2007.2074`. The latter
DOI resolves, on both Crossref and Semantic Scholar (2026-09-05), to *Synthetic Turing
protocells: vesicle self-reproduction through symmetry-breaking instabilities* — an unrelated
paper. Brodin's *Theoretical models of adaptive energy management in small wintering birds* is
Phil. Trans. R. Soc. B, issued 2006-04-19, Crossref `is-referenced-by-count` 106, fetched
2026-09-05.


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

The claim survives **in narrowed form**, with two scope restrictions taken from adversarial
objections and adopted rather than argued with. **The comparison is not to classic
LOLP-of-a-thermal-fleet.** Classic LOLP convolves a capacity-outage probability table against a
load-duration curve and has no integrated state at all, so there is no reserve and no
first-passage problem — that version of the grid side is *not* the same object as the bird's fat
reserve, and if the gap were scoped to it the gap would be false. **The comparison is to
storage-constrained adequacy**: LOLE computed on a system whose adequacy depends on a
state-of-charge trajectory. That is the modern variable-renewables-plus-storage formulation, it
carries a genuine reserve state, and it is the scope this note claims. **It is still not a
first-passage problem** — see the second restriction below.

**A second scope restriction, from `audits/g34-adversarial.md`, and it is why this note is
`narrowed`.** Even under storage-constrained scoping, **LOLE is not a first-passage quantity**:
unserved load is shed and the reserve recovers, so the grid's zero is not absorbing and LOLE
counts repeated crossings. The bird's `P(starve)` is a first-passage probability on an absorbing
boundary. **What the two fields share is the state recursion and the shadow price, not the
estimand.** The claim is corrected to that, and the word "first-passage" is removed from the grid
side throughout. [[C37-lolp-starvation-identity]] gives the surviving identity as a theorem with
five conditions and shows that two of them (absorbing boundary at 0; objective = `P(absorb before
T)`) fail as each field is normally practised.

**And the computation leg's headline numbers did not survive.** [[C33-lolp-starvation]] rev.1
reported a bird `P(starve)` of `8.25 x 10^-8` and "five orders of magnitude safer than the grid";
both are **withdrawn**. The simulated foraging policy overshot Brodin 2017's own reported daily
fat gain (0.74 g) by 2.26x, the 6 kJ warming-up cost was silently zeroed, and no fixed-gain
forward propagation can estimate the first passage of a state-dependent DP. The surviving
quantitative claim is the **energy margin over the critical period**: `12/27.4` = **+43.8%** for
the bird against **~0%** for a duration-matched 4-hour storage fleet, with the demand-side
(hypothermia) lever worth **12 points**, not 47. The mechanism — a movable metabolic setpoint
sorts the margin — replicates across 19 systems in [[C38-reserve-margin-across-species]].

**The parent both fields skip.** A reserve driven by stochastic income against a stochastic draw,
first passage to zero, is **ruin theory** — Lundberg 1903, Cramér 1930. Power-system adequacy
does not cite it, behavioural ecology does not cite it, and they do not cite each other. The
citation intersection here measures one leg of that triple zero.

`crosses: formalism` (rank 4) rather than `data`: the two fields share the dynamic program and
the shadow-price construction, but no dataset has been put through both. The estimand difference
narrows what is shared; it does not drop the rank.

## What would close it

Closed in one motion by [[C33-lolp-starvation]], which (i) writes both problems in one notation
and shows the LOLP recursion and the starvation backward equation are the same dynamic program,
(ii) **withdrew** its two-way conversion between a bird starvation probability and an LOLE,
because those are different functionals, and (iii) states the bird's optimal reserve as an
energy margin over the critical period against a duration-matched storage fleet. What C33 does **not** do, and what
would finish the job: put one dataset through both formalisms — take a real state-of-charge
trace from a storage-constrained adequacy study and a real dusk-fat/overnight-expenditure series
from a wintering parid, and fit the same reserve recursion to both. That is the step from
`crosses: formalism` to `crosses: data`. See [[what-closes-a-gap]].

## What could not be fetched

- **A concept-scoped `N_universe` from OpenAlex.** Attempted 2026-09-05 and refused with
  `Insufficient budget … Resets at midnight UTC` (HTTP 429), so OpenAlex answered nothing on this
  run and the `N` above is a Semantic Scholar phrase-match **estimate**, not a concept scope.
  Re-run the OpenAlex concept query after the budget resets and replace the 44,299 row.
- **A Semantic Scholar counterpart to Billinton & Allan 1996.** The DOI is absent from that
  index, so the OpenCitations headline pairing is not reproduced on the second provider; G94
  stands in for the 1990s grid decade.
- **A passing power-side positive control on Semantic Scholar.** Four of six return zero and the
  cause is diagnosed (missing reference lists), but no substitute grid control that *passes* on
  that provider has been found. Until one is, the second provider's grid-side zeros are
  corroboration, not independent evidence.
- **Houston & McNamara 1993 full text.** Paywalled at JSTOR; the DOI, title, journal, volume,
  pages and Crossref citation count were verified, the model's parameter values were not. C33
  therefore takes its bird parameters from an open-access successor model rather than from this
  anchor, and says so.

See [[C33-lolp-starvation]], [[C1-availability-living-tissue]], [[availability-formula]],
[[citation-intersection]], [[failure-modes]], [[positive-controls]].
