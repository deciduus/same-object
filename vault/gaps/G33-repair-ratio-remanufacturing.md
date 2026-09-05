---
id: G33
name: G33-repair-ratio-remanufacturing
type: gap
standing: narrowed
evidence: citation-intersection
contact-surface: 1
crosses: vocabulary
crosses-rank: 3
topology: direct
mediator: 
borrows-from: []
lends-to: []
mutual-with: []
computed-in: ["[[C31-remanufacturing-ha]]"]
uses-move: []
rests-on: ["[[availability-formula]]", "[[C6-damage-healing-ratio]]"]
tags: [node/gap, crosses/vocabulary, evidence/citation-intersection, standing/narrowed]
last-checked: 2026-09-05
note: "One bridge exists and was identified: Alqahtani 2017, a Northeastern PhD applying Barlow-Hunter preventive maintenance to remanufactured product warranties. It moves the policy mathematics across and never forms a rate ratio or an availability. OpenCitations returns 0 on the same pairing, so contact-surface 1 is provider-dependent."
exit: computation
extends-to: [circularity, sustainability]
next-step-cost: S
---

# The repair-rate ratio is never formed for a remanufactured fleet

**STANDING: NARROWED** · evidence: citation-intersection · contact surface: 1 · last checked 2026-09-05

> Reliability engineering computes a restoration rate over a failure rate and calls the
> compression of that ratio **availability**. Remanufacturing and closed-loop supply-chain
> research computes the same two flows for a product fleet — cores coming back, units going
> out — and calls them **core return rate** and **remanufacturing throughput**, forming no
> ratio and reporting no in-service fraction. **This is not a zero.** One work bridges the two
> anchors, and it is a real bridge: it carries Barlow & Hunter's preventive-maintenance
> optimisation onto remanufactured products. What it does not carry is the ratio. The gap is
> narrow, named, and closed by a computation rather than by a search.

## The two vocabularies

**Reliability / maintenance.** A repairable unit has a failure rate `k_d` (hazard, `1/MTBF`)
and a repair rate `k_r` (`1/MTTR`). [[availability-formula]] compresses them:
`A = MTBF/(MTBF+MTTR)`. [[C6-damage-healing-ratio]] writes the same pair as the dimensionless
`Ha = k_r/k_d` and shows `A = Ha/(1+Ha)`, which is the Erlang-B blocking complement of a
one-server loss system at offered load `ρ = 1/Ha`. The founding optimisation is **Barlow &
Hunter, "Optimum Preventive Maintenance Policies", *Operations Research* 8:90–100 (1960),
DOI `10.1287/opre.8.1.90`** — title, journal, year and month (1960-02) **verified against
Crossref 2026-09-05**, `is-referenced-by-count` = 1,133.

**Remanufacturing / closed-loop supply chains.** The same fleet is described by a **core return
rate** (what fraction of units leaving service comes back), a **remanufacturing yield** or
salvage rate (what fraction of returned cores is restorable), a **throughput**, and a **cycle
time**. The founding statement of the planning problem is **Guide, "Production planning and
control for remanufacturing: industry practice and research needs", *J. Operations Management*
18:467–483 (2000), DOI `10.1016/s0272-6963(00)00034-6`** — Crossref-verified 2026-09-05,
`is-referenced-by-count` = 842. **The DOI with terminal `-7` 404s; the correct suffix is `-6`**
(this is the scout's correction, re-confirmed here against Crossref).

**Industrial ecology's third name for it.** Stock–flow modelling asks the same question as
"repair or replace" and answers it with residence times and outflow rates, never with a rate
ratio. That side is [[G30-weibull-product-lifespan]]'s and [[C27-product-lifespan-beta]]'s
axis, not this one; the two gaps meet at the same fleet and measure different parameters of it.

**The sharpest single piece of evidence is not a count.** Graham et al., *Performance
measurement and KPIs for remanufacturing*, **Journal of Remanufacturing 5:10 (2015), DOI
`10.1186/s13243-015-0019-2`** (open access, PDF fetched from
`link.springer.com/content/pdf/10.1186/s13243-015-0019-2.pdf`, **2026-09-05**, 18 pp.,
text-extracted) is the field's own canonical KPI toolbox, built with Centro Ricerche FIAT and
SKF. Its list contains **Lead Time, Cycle Time, Work In Progress, Hours Per Unit, Product
Salvage Rate, Component Salvage Rate and Core/Product Value Ratio**. Those are precisely the
ingredients of `Ha`. **The list contains no ratio of the two rates and no availability.** A
field that has enumerated its own performance indicators and stopped one arithmetic operation
short is a better demonstration of the gap than any citer count.

## Provenance

| Item | Value |
|---|---|
| Anchor A | Barlow & Hunter 1960, `10.1287/opre.8.1.90`, OpenAlex `W2109281751` |
| Anchor B | Guide 2000, `10.1016/s0272-6963(00)00034-6`, OpenAlex `W2029123070` |
| DOI verification | Crossref `api.crossref.org/works/<doi>?mailto=deciduusleaf@gmail.com`, **2026-09-05**, both titles/years/journals matched |
| Provider 1 | OpenAlex `works?filter=cites:W2109281751,cites:W2029123070`, `meta.count` = **1** (scout run, 2026-09-05). `N_A` = 1,368, `N_B` = 1,093 (`cited_by_count`, re-read this session and unchanged) |
| Provider 2 | **OpenCitations COCI**, `api.opencitations.net/index/v1/citations/<doi>`, fetched **2026-09-05** here. `\|A\|` = **1,131**, `\|B\|` = **845**, intersection = **0** |
| Union floor `N` | 2,460 (OpenAlex); `E` = 607.8; `O/E` = 0.00165 — **a floor, not quotable alone** |
| Scoped `N_universe` | **NOT OBTAINED.** See below |
| Control (same A anchor) | Barlow & Hunter × Dekker 1996 (`10.1016/0951-8320(95)00076-3`) = **89** of 966 (scout, 2026-09-05) |
| **Control ratio** | `(1/1,093)/(89/966)` = 0.000915/0.0921 → **isolation ≈ 100×**, denominator-invariant |

**`N_universe` could not be fetched, and the reason has changed since the scout.** The scout
recorded HTTP 429 as IP-level rate limiting. This session's 429 body is different:
`"Insufficient budget. This request costs $0.0001 but you only have $0 remaining. Resets at
midnight UTC"`, `retryAfter` = 53,949 s. Three retries at 20 s, 40 s and 60 s backoff all
returned 429 with the same body (2026-09-05). **This is a spent daily quota, not a transient
limit**, so no amount of backoff inside one session recovers it, and any concept-scoped `E` for
this pairing must wait for a later UTC day. Per [[citation-intersection]], the `O/E` above is
therefore **not quotable**, and the load-bearing statistic is the control ratio, which does not
depend on `N`.

**The two providers disagree, and the disagreement is the honest headline.** OpenAlex sees one
bridging work; COCI sees none. Both numbers can be true of their own object — COCI indexes only
DOI-bearing Crossref reference lists, and the bridging work is a **dissertation** whose
reference list Crossref does not carry. `contact-surface: 1` is recorded on the stronger
(gap-unfavourable) reading. Per `CLAUDE.md`'s two-true-numbers rule, neither figure is called
wrong.

## The bridge, read and characterised

**Alqahtani, Ammar Yahya, *Warranty cost analysis with preventive maintenance strategy for
remanufactured products in reverse supply chain*, PhD dissertation, Northeastern University
(degree 2017; Crossref record created 2021-05-10), DOI `10.17760/d20249105`.** Crossref record
fetched **2026-09-05**: `type` = `dissertation`, sole author Alqahtani, institution Northeastern
University, publisher Northeastern University Library, resource URL
`hdl.handle.net/2047/D20249105`. **Crossref carries no abstract for it, and the full text was
not obtained**: the handle 302-redirects to
`repository.library.northeastern.edu/files/neu:cj82q470q`, which returns **HTTP 418** to
WebFetch and **HTTP 403** to `curl` (both 2026-09-05); the `fulltext.pdf` route exceeds the
10 MB fetch cap; the Routledge pages for the derived book are **403**. The characterisation
below therefore rests on **verified Crossref metadata plus the derived book's chapter titles**,
and is marked accordingly.

The work became **Alqahtani & Gupta, *Warranty and Preventive Maintenance for Remanufactured
Products: Modeling and Analysis*, CRC Press (2019), DOI `10.1201/b22308`**, whose chapter DOIs
were fetched from Crossref 2026-09-05 and are titled *Product Warranty and Preventive
Maintenance* (`-3`), *Warranty Policies for Remanufactured Products with Preventive Maintenance
Strategy* (`-4`), *Modeling Warranty Costs with Preventive Maintenance for Remanufactured
Products* (`-5`) and *Cost Analysis of Renewing Warranties* (`-10`). Crossref carries no
abstracts for these.

**What it bridges.** It is the maintenance-policy mathematics of the Barlow & Hunter line —
age replacement, preventive-maintenance intervals, renewal-based cost integrals — applied to a
population of *remanufactured* products inside a reverse supply chain, with 27 warranty policies
evaluated by discrete-event simulation. That is a genuine crossing: the object is a
remanufactured fleet and the instrument is reliability mathematics. This candidate is
consequently **not a zero and must never be reported as one.**

**What it does not bridge.** Its output is a **cost** — expected warranty cost per policy — and
its decision variable is a **policy**. Nothing in the metadata, the chapter titles or the
derived book's structure forms a dimensionless ratio of a restoration rate to a failure rate, or
reports a fleet in-service fraction, or connects the core return rate to an availability.
**UNVERIFIED against the full text**, which is the one weak link in this note and the cheapest
thing to fix: a library copy of `10.1201/b22308`, checked for a rate ratio, either kills the gap
or hardens it. Until then the claim is stated at the strength of its evidence.

## Decade-binned re-run — [[failure-modes]] mode 6

The pooled citer window here is 1960–2026, so a single pooled count is six measurements
pretending to be one. Binning the COCI citer sets by their `creation` field, from the two JSON payloads at
`api.opencitations.net/index/v1/citations/10.1287/opre.8.1.90` and
`.../10.1016/s0272-6963(00)00034-6`, both fetched **2026-09-05** and intersected as
lower-cased DOI sets:

| Decade | citers of Barlow & Hunter | citers of Guide 2000 | co-citers |
|---|---|---|---|
| 1960s | 8 | — | — |
| 1970s | 28 | — | — |
| 1980s | 71 | — | — |
| 1990s | 99 | — | — |
| 2000s | 191 | 143 | **0** |
| 2010s | 465 | 459 | **0** |
| 2020s | 246 | 223 | **0** |
| undated | 23 | 20 | — |
| **total** | **1,131** | **845** | **0** |

**The overlap window is three decades wide, not six**, because Guide 2000 cannot be cited before
2000 — which is itself the mode-6 discipline doing its job, by making the true window visible.
The zero holds in every decade in which a co-citer was possible, and the two citer sets grew
together (both peak in the 2010s), so the zero is not an artefact of one side being young or
dormant. **The vocabularies do coexist**, which rules mode 6 out rather than in: this is a
synchronic separation, not a renaming. The one OpenAlex hit is a 2017 work, i.e. in the 2010s
bin, the densest decade on both sides.

## What would close it

**The missing object is the first `Ha` for a remanufactured product fleet**, with C6's four
conditions checked rather than assumed, and its `A` compared against that fleet's published
in-service fraction. Written in [[C31-remanufacturing-ha]], which finds that:

1. the identification is **`Ha = L/T`** — mean in-service life over mean core out-of-service
   time — and that this is the same arithmetic as `MTBF/MTTR`;
2. C6's `A = Ha/(1+Ha)` is **wrong for a product fleet** and becomes `A = Ha/(Ha + r)` once a
   core return rate `r < 1` is admitted, reducing to C6's form only at `r = 1`;
3. **no published case gives `T`.** Return rates and lifetimes are published; the out-of-service
   residence time that would complete the pair is not, in any source reached this session.

So the gap does not close on a search. It closes on **one number that a single remanufacturer
already has in its ERP system**: the mean elapsed time from a core leaving service to its
remanufactured successor entering service. That is `next-step-cost: S` and it is the whole
remaining cost. See [[what-closes-a-gap]].
