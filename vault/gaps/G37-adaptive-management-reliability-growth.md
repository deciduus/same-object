---
id: G37
name: G37-adaptive-management-reliability-growth
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
computed-in: ["[[C36-conservation-duane]]"]
uses-move: ["[[M6-vary-what-was-held-fixed]]"]
rests-on: []
tags: [node/gap, crosses/formalism, evidence/citation-intersection, standing/live]
last-checked: 2026-09-05
note: "Both fields ask how fast a programme of deliberate trials drives its failure rate down. Reliability engineering fits a growth exponent beta; conservation has never computed one. Intersection 0 on 15 of 15 anchor pairings across three decades of each side's vocabulary, four in-domain controls firing at 20-64."
exit: computation
extends-to: [conservation]
next-step-cost: S
---

# Adaptive management has no growth exponent

**STANDING: LIVE** · evidence: citation-intersection · contact surface: 0 · last checked 2026-09-05

> Conservation's **adaptive management** and reliability engineering's **reliability growth**
> describe the same object: *a programme that deliberately runs trials in order to drive a
> failure rate down, and asks how fast the rate falls with cumulative experience.* Engineering
> has fitted that rate of fall since 1964 and calls its slope the **growth exponent β**.
> Conservation argues about whether its programmes are learning, qualitatively, and **has never
> computed one**. The missing object is a number: β for a named conservation programme.

## The two vocabularies

**Conservation.** *Adaptive management* (Holling, ed., 1978, *Adaptive Environmental Assessment
and Management* — a book, **no DOI resolves**, Crossref returns only a 1979 review of it,
`10.1177/030913257900300423`; Walters 1986, *Adaptive Management of Renewable Resources*,
Macmillan — **no DOI**), *learning by doing* (Walters & Holling 1990, Ecology,
[10.2307/1938620](https://doi.org/10.2307/1938620), Crossref title "Large-Scale Management
Experiments and Learning by Doing", `is-referenced-by-count` 933, fetched 2026-09-05),
*structured decision making* and *monitoring-driven revision* (Williams 2011, *J. Environ.
Manage.* 92:1346, [10.1016/j.jenvman.2010.10.041](https://doi.org/10.1016/j.jenvman.2010.10.041),
verified title "Adaptive management of natural resources—framework and issues", refby 549;
Allen *et al.* 2011, same issue,
[10.1016/j.jenvman.2010.11.019](https://doi.org/10.1016/j.jenvman.2010.11.019), "Adaptive
management for a turbulent future", refby 398; Westgate, Likens & Lindenmayer 2013, *Biol.
Conserv.*, [10.1016/j.biocon.2012.08.016](https://doi.org/10.1016/j.biocon.2012.08.016)).

**Reliability.** *Reliability growth* (Duane 1964, *IEEE Trans. Aerospace* 2:563, "Learning Curve
Approach to Reliability Monitoring",
[10.1109/TA.1964.4319640](https://doi.org/10.1109/TA.1964.4319640) — **DOI verified**, Crossref
refby 499, fetched 2026-09-05), the *Crow/AMSAA* model (Crow 1974, AMSAA TR-138 — a technical
report with **no DOI**; the citable journal statement is Crow 1982, *Technometrics* 24:67,
"Confidence Interval Procedures for the Weibull Process With Applications to Reliability Growth",
[10.1080/00401706.1982.10487711](https://doi.org/10.1080/00401706.1982.10487711), refby 121, and
the 1977 report [10.21236/ada044788](https://doi.org/10.21236/ada044788)), the *growth exponent*
`β` of the NHPP power-law intensity

```
λ(t)  =  λ β t^(β−1) ,      E[N(t)] = λ t^β
```

and the test-analyse-and-fix planning standard **MIL-HDBK-189** (US DoD, 1981; its worked
planning range for a development programme is β ≈ 0.3–0.6, and the *Handbook* is a government
document with no DOI — see [[C36-conservation-duane]] §Inputs for how that range is sourced).

Both objects are *the same estimator applied to the same experiment*: run a trial, observe an
outcome, revise, run another, and ask whether the failure intensity per unit of accumulated
programme experience is falling, flat, or rising. `β < 1` falling, `β = 1` flat, `β > 1` rising.

## Provenance

**Instrument: OpenCitations**, endpoint `https://api.opencitations.net/index/v1/citations/<doi>`,
User-Agent `biomimicry/1.0 (mailto:deciduusleaf@gmail.com)`, **all fetches 2026-09-05**. Citer
sets are counted distinct **non-empty** lowercased `citing` DOIs — records with a blank `citing`
field are dropped, per the bug `scout-04` found and fixed (a naive de-duplication adds a phantom
`""` to every set and inflates `N_A`, `N_B` and every intersection by exactly 1). DOIs resolved
through **Crossref**, `api.crossref.org/works/<doi>?mailto=deciduusleaf@gmail.com`, same date.

**Re-derived counts.** `scout-04` reported `|citers(Walters & Holling 1990)| = 996`,
`|citers(Duane 1964)| = 500`, `O = 0`, E floor 333; and `|citers(Williams 2011)| = 569`, `O = 0`,
E floor 266. **Both reproduce exactly** on an independent fetch with an independently written
client.

**Mode 6 run in full** ([[failure-modes]] §6): five A-side anchors spanning 1990–2013 against
three B-side anchors spanning 1964–1982. `E floor = N_A·N_B/(N_A+N_B−O)`.

| A ↔ B | Duane 1964 (500) | Crow 1977 TR (25) | Crow 1982 Technometrics (78) |
|---|---|---|---|
| Walters & Holling 1990 (996) | **0** — E floor 333 | **0** — 24.4 | **0** — 72.3 |
| Williams 2011 (569) | **0** — 266 | **0** — 23.9 | **0** — 68.6 |
| Allen 2011 (408) | **0** — 225 | **0** — 23.6 | **0** — 65.5 |
| Westgate 2013 (342) | **0** — 203 | **0** — 23.3 | **0** — 63.5 |
| Fischer & Lindenmayer 2000 (1,257) | **0** — 358 | **0** — 24.5 | **0** — 73.4 |

**15 of 15 zeros. Nothing to inspect: the intersections are empty sets, so no hit was read.**

**Second anchors and the DOI correction.** Fischer & Lindenmayer 2000 was carried into this note
as `10.1016/S0006-3207(99)00048-3`; that DOI **404s at Crossref**. The correct one, recovered by
bibliographic title search, is
[10.1016/s0006-3207(00)00048-3](https://doi.org/10.1016/s0006-3207(00)00048-3) ("An assessment of
the published results of animal relocations", *Biol. Conserv.* 96:1, refby 1,187). Seddon *et
al.* 2007 (`10.1111/j.1523-1739.2007.00724.x`) was tried as a further A anchor and **discarded**:
OpenCitations returns a citer set of size **1**, too thin to support any null model, so its row is
void rather than zero.

**Four in-domain controls fire**, so both literatures are findable and internally joined and the
zeros are not an indexing artifact:

| Control | N_A / N_B / **O** |
|---|---|
| Walters & Holling 1990 × Williams 2011 | 996 / 569 / **64** |
| Allen 2011 × Walters & Holling 1990 | 408 / 996 / **45** |
| Westgate 2013 × Williams 2011 | 342 / 569 / **46** |
| Fischer & Lindenmayer 2000 × Westgate 2013 | 1,257 / 342 / **20** |
| Crow 1982 × Duane 1964 | 78 / 500 / **36** |
| Duane 1964 × Barlow & Hunter 1960 | 500 / 1,131 / **13** *(scout-04, reproduced)* |

**Every `E` above is a union floor, and a floor is not quotable alone** ([[citation-intersection]]).
A concept-scoped `N_universe` — OpenAlex, union of `C200601418` (Reliability engineering) and
`C2775917145` (Adaptive management), from 1964 — was attempted **three times on 2026-09-05 and
returned HTTP 429 every time**. **It is not in this note, and the zero is therefore a lead at
floor strength, not a calibrated finding.** That is the single missing number here.

## What survives

The shared object is real and the isolation is total at the instrument's own resolution. What the
zero does **not** license is the claim that the transfer is easy: Duane's `β` presumes a
**repairable system with a fixed failure-mode inventory** monotonically depleted by fixes. A
managed ecosystem has a non-stationary inventory — climate and land-use change generate new
failure modes while management retires old ones — so `β ≈ 1` is ambiguous between "not learning"
and "learning exactly as fast as the world changes." [[C36-conservation-duane]] computes β anyway
and reports that ambiguity as its principal limit.

## What would close it

A fitted **β with a confidence interval for a named conservation programme**, on a countable
record of trials, against engineering's development-programme range. [[C36-conservation-duane]]
does this for regional fishery-management programmes and returns β from **0.67 to 1.11**; it is
what makes this note `evidence: citation-intersection` with an `exit: computation` already taken
rather than promised. Two things would close the gap outright and neither is done here:

1. **The scoped `N`.** Without it the fifteen zeros sit on union floors. One successful OpenAlex
   call settles it. See [[what-closes-a-gap]].
2. **A second, non-fishery programme** with a genuine trial record — island-eradication attempts
   (DIISE), reintroduction outcomes, or a recovery-plan objectives-met audit. C36 could fetch
   none of them and says so.
