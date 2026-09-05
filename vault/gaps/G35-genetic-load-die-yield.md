---
id: G35
name: G35-genetic-load-die-yield
type: gap
standing: live
evidence: citation-intersection
contact-surface: 0
crosses: nothing
crosses-rank: 0
topology: disjoint
mediator: 
borrows-from: []
lends-to: []
mutual-with: []
computed-in: ["[[C34-load-yield-clustering]]"]
uses-move: []
rests-on: []
tags: [node/gap, crosses/nothing, evidence/citation-intersection, standing/live]
last-checked: 2026-09-05
exit: computation
extends-to: [conservation]
next-step-cost: S
note: "Haldane-Muller mean fitness e^(-U) and Poisson die yield e^(-A*D0) are the same survival law, both independent of per-defect severity. Citer-set intersection 0 on 18 of 18 pairings (6 genetics anchors 1963-2022 x 3 yield anchors 1964-1990), OpenCitations 2026-09-05, against E floors 113-289; 15 in-domain controls fire 14-82. No concept-scoped N could be fetched (OpenAlex 429-locked), so the zero rests on union floors only."
---

# Genetic load and die yield

**STANDING: LIVE** · evidence: citation-intersection · contact surface: 0 · last checked 2026-09-05

> Population genetics and semiconductor manufacturing each write down the same survival law —
> **exp(−expected number of independently-acting lethal defects), with per-defect severity
> cancelling out** — and neither has ever cited the other. Genetics calls it the
> **Haldane–Muller principle**, `W̄ = e^(−U)`; yield engineering calls it the **Poisson defect
> model**, `Y = e^(−A·D0)`. Yield engineering then spent four decades measuring the correction
> term that genetics has never written down. The missing object is that correction's parameter:
> computed in [[C34-load-yield-clustering]].

## The two vocabularies

**Population genetics.** Haldane 1937 and Muller 1950 established that at mutation–selection
balance the equilibrium reduction in mean fitness — the **mutation load** — depends on the
**genomic deleterious mutation rate `U`** and *not* on the selection coefficient `s` of each
mutation. A mutation of small effect persists longer and is removed at the same rate it arises;
a lethal is removed at once. The bookkeeping cancels. Under multiplicative fitness across
independent loci this gives `W̄ = e^(−U)`. The surrounding apparatus is **mutation–selection
balance**, **drift load** (Kimura, Maruyama & Crow 1963: in small populations drift fixes
deleterious alleles that selection would have removed, and the load rises as `Ne` falls), the
**mutational meltdown** (Lynch, Conery & Bürger 1995), and, in the modern conservation-genomics
form, per-genome counts of **realised** versus **masked** load (Bertorelle 2022) feeding
extinction-risk simulations (Kyriazis 2021). Agrawal & Whitlock 2012 is the field's own review of
where the principle holds and where epistasis and dominance break it.

**Semiconductor manufacturing.** Yield engineering asks what fraction of dies on a wafer work.
With **defect density `D0`** (killer defects per cm²) and **die area `A`**, and defects placed
independently and uniformly, the number of killer defects on a die is Poisson and the **Poisson
yield** is `Y = e^(−A·D0)` — *independent of how severe each defect is*, because any killer
defect kills. Murphy 1964 is the founding paper and already observed that the pure exponential
under-predicts observed yield, because real defects **cluster**. Stapper 1983 gave the standard
fix: let the local defect density itself vary, gamma-distributed with shape `α`, and the count
becomes negative binomial, so

```
Y = (1 + A·D0/α)^(−α)        ->  e^(−A·D0)  as  α -> inf
```

`α` is the **clustering parameter**: small `α` means strongly clustered defects and *higher*
yield than Poisson at the same mean. Cunningham 1990 is the comparative evaluation of the
competing yield models. Alongside sits the **yield-learning curve** — cumulative wafers started
against `D0`, the industry's own instrument for whether a fab is learning.

**The correspondence.** `A·D0 ↔ U`; die ↔ individual; killer defect ↔ deleterious mutation;
yield ↔ mean fitness; severity-independence ↔ the Haldane–Muller principle. Genetics has `A·D0`
and no `α`. Manufacturing has both, and has published fitted values of `α` since 1983.

## What was searched

Citer-set intersection over **OpenCitations**, endpoint
`https://api.opencitations.net/index/v1/citations/<doi>`, User-Agent
`biomimicry-vault/1.0 (mailto:deciduusleaf@gmail.com)`, **fetched 2026-09-05**. `N_A`/`N_B` are
counted citer-DOI sets from that fetch, not `citation-count`. Every anchor DOI was resolved
through **Crossref** (`api.crossref.org/works/<doi>?mailto=deciduusleaf@gmail.com`, same date)
and returned the intended title and authors.

**The blank-`citing` filter is load-bearing and was applied.** OpenCitations `/citations/`
returns some records with an empty `citing` field; an unfiltered set carries a phantom `""` that
belongs to *every* set and therefore inflates `N_A`, `N_B` **and every intersection by exactly
one**. This run dropped **25 blank records across the nine anchor fetches**. Without the filter
every zero below would have read `1`. The fetch used for this note is a private client that
filters at set-construction time; `vault/_scripts/intersect.py` documents the same trap.

### Anchors

| Side | Work | DOI | Crossref-verified 2026-09-05 | citers |
|---|---|---|---|---|
| Genetics 1960s | Kimura, Maruyama & Crow 1963, *Genetics* | `10.1093/genetics/48.10.1303` | *The mutation load in small populations* | 349 |
| Genetics 1990s | Lynch, Conery & Bürger 1995, *Am. Nat.* | `10.1086/285812` | *Mutation accumulation and the extinction of small populations* | 872 |
| Genetics 2000s | Charlesworth 2009, *Nat. Rev. Genet.* | `10.1038/nrg2526` | *Effective population size and patterns of molecular evolution* | 1,596 |
| Genetics 2010s | Agrawal & Whitlock 2012, *Annu. Rev. Ecol. Evol. Syst.* | `10.1146/annurev-ecolsys-110411-160257` | *Mutation load* | 214 |
| Genetics 2020s | Kyriazis 2021, *Evolution Letters* | `10.1002/evl3.209` | *Strongly deleterious mutations … extinction risk* | 251 |
| Genetics 2020s | Bertorelle 2022, *Nat. Rev. Genet.* | `10.1038/s41576-022-00448-x` | *Genetic load: genomic estimates* | 250 |
| Yield 1960s | Murphy 1964, *Proc. IEEE* | `10.1109/proc.1964.3442` | *Cost-size optima of monolithic integrated circuits* | 318 |
| Yield 1980s | Stapper 1983, *IBM J. Res. Dev.* | `10.1147/rd.276.0549` | *Modeling of integrated circuit defect sensitivities* | 238 |
| Yield 1990s | Cunningham 1990, *IEEE Trans. Semicond. Manuf.* | `10.1109/66.53188` | *The use and evaluation of yield models* | 277 |

### Result: 18 of 18 zero

Every genetics anchor against every yield anchor. `E floor = N_A·N_B/(N_A+N_B−O)`, **a floor and
never quotable alone** — it is the smallest defensible denominator and therefore flatters the
claim ([[citation-intersection]]).

| genetics ↓ / yield → | Murphy 1964 | Stapper 1983 | Cunningham 1990 |
|---|---|---|---|
| Kimura 1963 | **0** (E floor 166) | **0** (142) | **0** (154) |
| Lynch 1995 | **0** (233) | **0** (187) | **0** (210) |
| Charlesworth 2009 | **0** (265) | **0** (207) | **0** (236) |
| Agrawal & Whitlock 2012 | **0** (128) | **0** (113) | **0** (121) |
| Kyriazis 2021 | **0** (140) | **0** (122) | **0** (132) |
| Bertorelle 2022 | **0** (140) | **0** (122) | **0** (131) |

**Hits inspected: none exist to inspect.** All eighteen intersections are empty sets, so the
inspection step of [[citation-intersection]] is vacuous here — which is a weaker position than
G25's, where the count was non-zero and reading it changed the answer.

### Mode-6 decade run

[[failure-modes]] mode 6 requires the concept under *each decade's own name* across the whole
window, on both sides, not a pooled query. That is what the anchor set above is: the genetics
side is sampled at 1963 (*mutation load in small populations*), 1995 (*mutation accumulation /
meltdown*), 2009 (*effective population size*), 2012 (*mutation load*), 2021–22 (*genetic load,
realised and masked*); the yield side at 1964 (*cost-size optima*), 1983 (*defect sensitivities*),
1990 (*yield models*). **The zero holds in every decade bin, under that decade's own vocabulary,
on both sides.** No anchor here is a proper noun, a possessive or a shared homograph — the two
literatures share no word at all, which is why this gap is graded `crosses: nothing` rather than
`crosses: word` like [[G6-multifunctionality]].

### Controls: both literatures are findable and internally joined

Fifteen in-domain pairings from the same nine citer sets, same fetch:

| Control | O |
|---|---|
| Kimura 1963 × Lynch 1995 | **82** |
| Kimura 1963 × Agrawal & Whitlock 2012 | **34** |
| Kimura 1963 × Kyriazis 2021 / × Bertorelle 2022 / × Charlesworth 2009 | **24 / 23 / 20** |
| Lynch 1995 × Kyriazis 2021 / × Bertorelle 2022 / × Charlesworth 2009 / × Agrawal 2012 | **51 / 40 / 39 / 38** |
| Kyriazis 2021 × Bertorelle 2022 | **50** |
| Agrawal 2012 × Bertorelle 2022 / × Charlesworth 2009 / × Kyriazis 2021 | **28 / 19 / 18** |
| Bertorelle 2022 × Charlesworth 2009; Kyriazis 2021 × Charlesworth 2009 | **23 / 16** |
| Murphy 1964 × Cunningham 1990 | **52** |
| Murphy 1964 × Stapper 1983 | **42** |
| Stapper 1983 × Cunningham 1990 | **14** |

Both sides are joined internal literatures — sixty years of genetics anchors co-cited 16–82
times, and the three yield anchors co-cited 14–52 times. **The eighteen zeros are not an indexing
artifact.** Every control ratio is nonetheless exactly `0`, because every gap intersection is
zero, so the control ratio carries no ordering information and the claim rests on the
same-object argument and the E floors, in that order.

## What survives

**The identity survives; the null model does not yet.** `N_universe` could not be fetched:
OpenAlex `api.openalex.org/concepts?search=…` returned **HTTP 429 on all 15 attempts across three
separate probe rounds with exponential backoff, 2026-09-05** (seven agents were on the polite pool
concurrently), so no concept-scoped denominator exists for this pair and only the union floors
above are available. Per [[citation-intersection]] the sensitivity run is mandatory and has not
been done, so **this zero is not yet quotable as a finding** — the same weakness the scout that
raised the candidate declared. The floors are 113–289, so a concept-scoped `N` up to roughly
10× the floor would leave `E > 1`; that is the query that has to run.

**The independence assumption is where the honest objection lives.** `A·D0` and `U` are both
counts of independent lethal events, and both fields know independence fails — but they break it
differently. Genetics breaks it through **epistasis and dominance**: synergistic epistasis makes
load sub-exponential and recessivity makes deleterious alleles conditionally invisible. Yield
breaks it through **spatial clustering**, which is exactly why negative-binomial models replaced
the exponential. If the two failures are structurally unrelated, the shared exponential is a
coincidence of the independent-events limit and every interesting case sits outside it.
[[C34-load-yield-clustering]] takes that objection seriously and answers it with a number rather
than an argument.

**Relation to [[G25-proofreading-coding]].** These are the project's two information/coding-shaped
gaps and they behave oppositely. G25's zero *collapsed* on re-test — 36 co-citers, four with real
coding-theory content — because Shannon 1948's citer set spans most of quantitative science and
some of it was always going to touch proofreading. G35's anchors have no such promiscuous partner:
Murphy, Stapper and Cunningham are cited by 238–318 works, all of them semiconductor
manufacturing. That makes G35's zero *cheaper to get* and therefore less impressive per unit
count, and it is why the load-bearing evidence here is the same-object argument, not the
intersection. G25 also warns about the adjacent candidate this gap is **not**: mutational meltdown
↔ error-correcting codes, which the scout ranked separately and which is likely a scope artifact
of the quasispecies literature.

## What would close it

**The clustering parameter `α` on the genetics side, and the discrimination between `W̄ = e^(−U)`
and `W̄ = (1 + U/α)^(−α)`.** Computed in [[C34-load-yield-clustering]], from published per-trio de novo mutation counts and their
parental-age regression. The gap closes to `narrowed` if `α` is large enough that the correction
is negligible (the Haldane–Muller form is then right for the reason yield engineers would give,
and genetics gains a bound rather than a formula), and stays `live` and gets sharper if `α` is
small enough to bias published extinction-risk-from-load estimates in a known direction by a
computable amount. The exit is `computation`, the cost is `S`, and the answer is already in
[[C34-load-yield-clustering]].
