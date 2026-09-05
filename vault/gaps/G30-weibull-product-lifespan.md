---
id: G30
name: G30-weibull-product-lifespan
type: gap
standing: live
evidence: citation-intersection
contact-surface: 1
crosses: formalism
crosses-rank: 4
topology: disjoint
mediator: 
borrows-from: []
lends-to: []
mutual-with: []
computed-in: ["[[C27-product-lifespan-beta]]"]
uses-move: []
rests-on: ["[[C18-durability-axis]]"]
tags: [node/gap, crosses/formalism, evidence/citation-intersection, standing/live]
last-checked: 2026-09-05
exit: computation
extends-to: [circularity, sustainability]
next-step-cost: S
note: "Reliability and industrial ecology fit the same two-parameter Weibull to the same random variable and report the same shape parameter; reliability reads it as a hazard law and chooses a maintenance policy, industrial ecology reads it as a stock-outflow input and never interprets it. Weibull 1951 x Oguchi 2015 = 0 co-citers against the same-B control Mueller 2006 x Oguchi 2015 = 15. Denominator is a union floor only."
---

# The Weibull shape parameter is fitted twice — as a hazard law and as a stock-outflow input

**STANDING: LIVE** · evidence: citation-intersection · contact surface: 1 · last checked 2026-09-05

> **In reliability engineering**, the shape parameter `β` of a fitted Weibull is *the* diagnostic
> quantity: `β = 1` is a constant hazard (memoryless, random loss), `β > 1` is an increasing hazard
> (wear-out), `β < 1` is infant mortality, and the value chosen determines whether age-based
> preventive replacement is worth doing at all. **In industrial ecology**, the same two-parameter
> Weibull is fitted to product-lifespan distributions — Oguchi & Daigo and successors fit it to
> automobiles, appliances and electronics — and the fitted `β` is passed into a stock-driven
> outflow model as a shape input for waste and secondary-material forecasting. The random variable
> is the same object (time from entry-into-service to exit-from-service, for a population of
> nominally identical artefacts) and the estimator is the same estimator, **but the industrial-
> ecology side does not read `β` as a statement about a hazard function, and the reliability side
> has never been given a table of product-class `β` values to classify.** The missing object is one
> table and one reading of it. [[C27-product-lifespan-beta]] builds the table.

Extends [[C18-durability-axis]], which already established `β` as the shared durability coordinate
across catalysis and energy storage, with a third population.

## What was searched

**Anchors.** *A (reliability):* W. Weibull, "A Statistical Distribution Function of Wide
Applicability", *J. Appl. Mech.* 18:293–297 (1951), DOI `10.1115/1.4010337` — Crossref-verified
2026-09-05, `is-referenced-by-count` = 9,513; OpenAlex `W2727420541`, `cited_by_count` = 11,512
(2026-09-05, via `audits/scout-01-circularity.md`).
*B (industrial ecology):* Oguchi, Daigo, Sugimoto & Kanari, "Regional and Longitudinal Estimation
of Product Lifespan Distribution: A Case Study for Automobiles and a Simplified Estimation Method",
*Environ. Sci. Technol.* 49:1738–1745 (2015), DOI `10.1021/es505245q` — Crossref-verified
2026-09-05 (title, ES&T, issued 2015-01-17, `is-referenced-by-count` = 98); OpenAlex `W2320647648`,
`cited_by_count` = 103.
*Secondary B:* Murakami, Oguchi, Tasaki, Daigo & Hashimoto, "Lifespan of Commodities, Part I",
*J. Ind. Ecol.* 14:598–612 (2010), DOI `10.1111/j.1530-9290.2010.00250.x` (Crossref-verified
2026-09-05, `is-referenced-by-count` = 172; OpenAlex `W2603909978`, 185); Part II,
`10.1111/j.1530-9290.2010.00251.x` (Crossref-verified, 116; OpenAlex `W2171683314`, 144);
Bakker, Wang, Huisman & den Hollander, "Products that go round", *J. Cleaner Prod.* 69:10–16
(2014), DOI `10.1016/j.jclepro.2014.01.028` (Crossref-verified 2026-09-05, 623; OpenAlex 717).

**DOI correction, logged.** The task brief cited `10.1111/j.1530-9290.2010.00272.x` for Murakami
2010 "Lifespan of commodities". Crossref resolves that DOI to a different paper — *"Environmental
Metrics"*, *J. Ind. Ecol.* 2010, `is-referenced-by-count` = 25 (fetched 2026-09-05). The two
correct DOIs are `…00250.x` (Part I) and `…00251.x` (Part II).

### Provenance block

| item | value | provider · endpoint · date |
|---|---|---|
| `|citers(Weibull 1951)|` | 11,512 | OpenAlex `works/W2727420541`, `cited_by_count`, 2026-09-05 (scout-01) |
| `|citers(Oguchi 2015)|` | 103 | OpenAlex `works/W2320647648`, 2026-09-05 (scout-01) |
| **Weibull × Oguchi 2015** | **0** | OpenAlex `works?filter=cites:W2727420541,cites:W2320647648`, `meta.count`, 2026-09-05 |
| Weibull × Murakami 2010 Part I | **1** | same endpoint, `cites:W2727420541,cites:W2603909978`, 2026-09-05 |
| Weibull × Bakker 2014 | **0** | same endpoint, `cites:W2727420541,cites:W2005386442`, 2026-09-05 |
| **Control: Müller 2006 × Oguchi 2015** | **15** | same endpoint, 2026-09-05; `|citers(Müller 2006)| = 511` |
| `E` at union floor, Oguchi pairing | **102.1** (`11,512·103/11,615`) | arithmetic, `_scripts/c27_beta.py` |
| `O/E` at union floor | **0** | — |
| Murakami pairing | `E = 182.1`, `O/E = 0.0055` | arithmetic |
| **Concept-scoped `N_universe`** | **NOT OBTAINED** | see below |
| Control ratio, shared **B** | `(0/103)/(15/103)` = **0** → isolation unbounded | denominator-invariant |
| Cost to close | **4–6 h desk**, no data access (scout-01 estimate) | — |

**The denominator is missing, and the note says so rather than quoting `O/E`.** Two attempts:

1. `audits/scout-01-circularity.md` recorded HTTP 429 on every `concepts.id:` count from ~16:00 on
   2026-09-05, sustained across 8 retries.
2. Re-attempted here, 2026-09-05, with backoff. OpenAlex now returns an explicit body:
   `{"error":"Rate limit exceeded","message":"Insufficient budget. This request costs $0.001 but
   you only have $0 remaining. Resets at midnight UTC.","retryAfter":54004}` — for
   `https://api.openalex.org/concepts?search=industrial%20ecology&per-page=3&mailto=…` and for every
   other endpoint. **The daily budget is exhausted; this is not a transient 429 and no backoff
   inside this session can clear it.** The concept IDs for "reliability engineering", "industrial
   ecology" and "product lifetime" were therefore never resolved, and no scoped `N` exists.

Consequence, per [[citation-intersection]]: **`E = 102.1` is a union floor, which flatters the gap
claim by construction, and `O/E` is not quotable.** The load-bearing statistic is the shared-**B**
control ratio — Oguchi 2015 held fixed, only the mathematics-side anchor swapped, 15 co-citers with
Müller 2006 against 0 with Weibull 1951 — which is denominator-free and cannot be explained by
Oguchi 2015 being a small paper.

### Hits inspected

**One hit exists across the three pairings** (hence `contact-surface: 1`): *"Agent-based model for
assessment of multiple circular economy strategies: quantifying product-service system…"*,
*Resources, Conservation and Recycling*, 2023, the Weibull × Murakami Part I co-citer. Inspected in
scout-01 at abstract level: it cites Weibull and Murakami as two separate methodological
ingredients of a simulation. **It does not put a reliability `β` and a lifespan `β` on one axis and
does not read `β` as a failure law.** It is not a bridge in the required sense. It has not been read
in full, and it remains the single place this gap could die.

### The near-bridge found while computing C27 — the strongest objection to `topology: disjoint`

Building [[C27-product-lifespan-beta]] surfaced a work that is *not* in any of the intersections
above and that does most of what the gap says is missing: **Lutz, Hopkins, Letschert, Franco &
Sturges, *Using National Survey Data to Estimate Lifetimes of Residential Appliances*, LBNL, 2011**
([osti.gov/servlets/purl/1182737](https://www.osti.gov/servlets/purl/1182737), PDF fetched and read
in full 2026-09-05). It cites Weibull 1951 directly, fits delayed Weibulls to nine US appliance
classes from RECS/AHS household surveys, prints `β` with standard errors, **and states the hazard
reading** — "β is the shape parameter, which determines the way in which the failure rate changes"
— while distinguishing physical from consumer/economic lifetime via the delay parameter.

What it does **not** do is the classifying step: it never compares its own `β` values across
classes, never labels a class by exit mode, and never connects them to a reliability policy. And it
sits in the energy-efficiency-policy literature, citing neither Oguchi nor Murakami — so no
Weibull × Oguchi intersection can see it.

**This is a mediating literature, and its existence is the strongest live threat to this note's
`topology: disjoint`.** The field is set to `disjoint` only because that mediating literature has
not been anchored and counted; a single run of `citers(Weibull 1951) ∩ citers(Lutz 2011)` and
`citers(Lutz 2011) ∩ citers(Oguchi 2015)` would settle it, and **`topology` should be expected to
move to `mediated`.** Recording it here rather than after the fact.

### Decade-binned re-run ([[failure-modes]] mode 6) — attempted, NOT achieved

Weibull 1951 anchors a 75-year citer window, which is exactly the mode-6 danger: the object was
called different things in different decades ("distribution function of wide applicability" and
fatigue life in the 1950s; "hazard rate" / "failure rate" in 1960s–70s reliability; "survival
function" and "discard function" in 1980s–90s materials-flow analysis; "lifespan distribution"
in the 2000s; "lifetime distribution" and "residence time" in dynamic MFA today). A pooled zero
across that window is six measurements of which five were never made.

**Both instruments failed, and neither number is quoted as evidence.**

- **OpenAlex citer-decade route:** blocked by the budget exhaustion above. No per-decade citer
  counts exist for either anchor.
- **Crossref term-frequency route:** `api.crossref.org/works?query.bibliographic=…` and
  `query.title=…` were run over seven decade bins (1951–1969, 1970s, 1980s, 1990s, 2000s, 2010s,
  2020–2026) for six decade-appropriate term sets, 2026-09-05. **The instrument is not selective.**
  Every term returned counts that track the growth of the Crossref corpus itself and nothing else —
  e.g. "lifespan distribution" 27,451 → 279,154 and "discard function" 22,679 → 286,670 across the
  same bins, with essentially identical growth curves for unrelated terms. Crossref's query fields
  are not phrase-exact, so these are OR-soup relevance counts, not term frequencies.
  **They measure the index, not the vocabulary, and are reported here only so the failure is on
  the record.**

**Consequence for standing.** The mode-6 check on this gap is **outstanding, not passed.** The zero
is reported as a zero on the *citation* instrument at one point in time, and the note does not claim
it has been shown to be a zero in every decade under that decade's own name. That is a stated
weakness of this note, not a hidden one, and it is the second thing (after the `disjoint` topology)
that a re-run should attack.

### The metaphor objection, stated before the claim rather than after

*Discard is not failure.* A product-lifespan distribution pools wear-out failure with obsolescence,
resale, theft, export and hoarding, so the fitted `β` is a mixture parameter over exit modes, not a
hazard shape for a degradation process. Held et al. 2021 say it plainly for cars: they leave "for
foreign markets … or for being dismantled", and "are typically sold on long before they fail
irreparably". **The reliability `β` and the lifespan `β` would then be the same arithmetic on
different objects** — the exact error [[C18-durability-axis]] warns about when it says one `N_fail`
hides two failure laws.

The objection is not refuted here; it is bounded, in [[C27-product-lifespan-beta]] §6. What survives
it is a comparative claim on a single instrument: within one method, one country and one survey,
US gas boilers fit `β = 1.000 ± 0.148` and US gas furnaces `β = 2.218 ± 0.320`. Whatever the exit
process is made of, it has different shapes for different product classes, and **`β ≈ 1` in a
product class is the signature of exit-by-random-loss rather than exit-by-wear-out.** Nobody has
said so in those words.

## What survives

The claim in its narrowed form:

1. **Both fields fit the same estimator to the same random variable and report `β`.** Not disputed;
   both literatures print it.
2. **Only one field reads `β` as a hazard law.** Supported by the intersection (0 co-citers with the
   canonical hazard-law anchor at `|B| = 103`, against 15 for the industrial-ecology-internal
   control on the same `B`) and by the absence of any exit-mode-labelled `β` table in the
   industrial-ecology literature that could be found.
3. **The axis is drawable, and drawing it classifies.** [[C27-product-lifespan-beta]] places 21
   published product-class fits between `β = 1.00` and `β = 6.0`, splitting into a memoryless band
   and a wear-out band that cuts across product categories.
4. **What does not survive:** any quotable `O/E`, any claim that the zero holds decade by decade,
   and any claim that no mediating literature exists — the LBNL 2011 near-bridge is a real one.

## What would close it

Per [[what-closes-a-gap]], three things, in cost order:

- **S — done, partially:** the table. Fitted `β` by product class with exit mode named, on the same
  axis as C18's enzyme, flow-battery and Li-ion rows. Built in [[C27-product-lifespan-beta]] from
  fetched primary parameters; incomplete because the Oguchi/Murakami per-class `β` are behind
  paywalls (ACS and Wiley both 403 on 2026-09-05) and Oguchi & Fuse's proposed **constant** shape
  parameter for the simplified method — the single most quotable number on the industrial-ecology
  side — **was not obtained.** Getting those three papers' tables closes the data half.
- **S — the two missing counts:** `citers(Weibull 1951) ∩ citers(Lutz 2011)` and
  `citers(Lutz 2011) ∩ citers(Oguchi 2015)`, plus a concept-scoped `N_universe`, once the OpenAlex
  budget resets. These decide `topology` and make `O/E` quotable.
- **M — the prediction, tested:** [[C27-product-lifespan-beta]] §5 asserts that an intervention
  which extends life on a `β ≤ 1.5` class raises `η` and the mean while leaving `β` inside its own
  standard error. It already has one natural-experiment pass in the shortening direction (US room
  air-conditioners, mean 14.75 → 11.27 yr with `β` 1.067 → 1.08). Testing it in the lengthening
  direction needs one post-right-to-repair lifespan survey with a published fit — which does not
  exist yet, and is the measurement this gap is really asking for.

See [[C18-durability-axis]], [[C27-product-lifespan-beta]], [[G3-cycle-life]],
[[citation-intersection]], [[failure-modes]], [[what-closes-a-gap]], [[positive-controls]].
