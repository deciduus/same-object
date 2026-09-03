---
id: G6
name: G6-multifunctionality
type: gap
standing: live
evidence: citation-intersection
contact-surface: 0
crosses: word
crosses-rank: 1
topology: disjoint
mediator: 
borrows-from: []
lends-to: []
mutual-with: []
computed-in: []
uses-move: []
rests-on: ["[[hill-number-multifunctionality]]"]
tags: [node/gap, crosses/word, evidence/full-text-read, standing/live]
last-checked: 2026-09-03
note: "Survived both standards. Intersection 0 across six anchor pairings at 77-100% coverage; 1,033 works, no contact either direction. Control Byrnes x Jost = 17, reproduced by both sources."
---

# Multifunctionality

**STANDING: LIVE** · evidence: citation-intersection · contact surface: 0 · last checked 2026-09-03

> Two mature quantified formalisms share one word and nothing else. **The only entry in the
> project to survive both standards** — full-text reading and citation intersection, which fail
> differently. See [[reading-not-counting]].

## The citation intersection: zero, with strong coverage

Run on six anchor pairings — Byrnes 2023 and Byrnes 2014 against Snyder 2015, the 2020 residual
performance paper, and O'Brien 2011. **OpenCitations set-overlap and an independent Crossref
reference-list scan, in both directions, both return zero.**

| Check | Result |
|---|---|
| **Intersection, all six pairings** | **0** |
| Coverage (COCI citers / Crossref cited-by) | 77.5%–100% |
| Citers fetched with DOI-bearing reference lists | 172/172 engineering, 846/861 ecology |
| 172 engineering citers → any of 8 core ecology journals | **0** |
| 861 ecology citers → Multifunctional Materials, J. Composite Materials, 4 composites journals | **0** |

**No contact in either direction across 1,033 works.** Coverage this high is what makes a zero
a finding rather than an absence of data.

### The positive control is the load-bearing part

**Byrnes 2014 × Jost 2006 = 17**, reproduced exactly by both sources. That control matters more
than the others because it *is* a metric formalism being imported into a multifunctionality
literature — precisely the event whose absence is claimed on the engineering side. The pipeline
detects that event when it happens. It does not happen here.

Also: Byrnes 2014 × Hector & Bagchi = 243 (28.8%); Snyder × O'Brien = 27 (34.2%).

## What the re-read added

The strongest evidence is an **adversarial case**, and it is the right kind. *A residual
performance methodology to evaluate multifunctional systems*
([doi 10.1088/2399-7532/ab8e95](https://iopscience.iop.org/article/10.1088/2399-7532/ab8e95),
*Multifunctional Materials* 2020), read in full, is an engineering paper whose **entire purpose
is that the existing multifunctionality metric is inadequate.** It proposes a replacement.

It uses no diversity, entropy, Hill-number or effective-number concept, and cites no ecology.
Its references are composites, electrochemistry, aerospace and design optimisation.

That is the exact place the ecology formalism would surface if a bridge existed. A field
actively shopping for a better multifunctionality metric did not find the one that already
exists. See [[hill-number-multifunctionality]].

From the ecology side, Byrnes, Roger & Bagchi (*Oikos* 2023 e09402, read via the
[bioRxiv preprint of record](https://www.biorxiv.org/content/10.1101/2022.03.17.484802v2.full))
say so themselves — the concept *"can even be applied outside of"* community and ecosystem
ecology. Domain-neutral by the authors' own statement, and never applied across.

## Correction: the 0.25 figure is withdrawn

The note said structural batteries score **~0.25**, below the threshold, "which is why the
metric bites." **Not reproduced.** The paper read in full reports **1.15–1.17**; other
search-surfaced values were 0.88 and 0.96 (not read).

**0.25 is UNVERIFIED and probably stale or mis-sourced.** If published cells now sit above
unity, the rhetorical line no longer follows and is struck. The gap does not depend on it —
the gap is about which *formalism* is used, not what score it returns.

## The homograph, unchanged

The bare word returns **9,570** hits, entirely materials science. Every query in the re-read
was anchored on formalism names — "Hill numbers", "effective number of functions",
"multifunctional efficiency", "sum of property ratios" — and never on the bare word. That is
the only way to keep the two senses apart. See [[homographs]].

## Reservations, stated

One review per side plus one adversarial engineering case. The Byrnes bibliography was never
inspected (PDF extraction failed), so "cites no engineering" is **UNVERIFIED** from that
direction. The engineering metric's construction — whether η_mf is a sum or a product — was
never seen rendered; **do not quote a formula from this note.**
