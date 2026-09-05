---
id: G19
name: G19-safety-factor-derived-twice
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
computed-in: ["[[C2-probabilistic-safety-factors]]"]
uses-move: []
rests-on: ["[[stress-strength-interference]]"]
tags: [node/gap, crosses/nothing, evidence/citation-intersection, standing/live]
last-checked: 2026-09-03
note: "46 is the OpenAlex count and is confirmed live, not stale; Crossref returns 36 and OpenCitations 40 for the same work. Citing works individually inspected, all comparative biomechanics. The 753-works figure is withdrawn as a string artifact."
---

# Safety factor, derived independently twice

**STANDING: LIVE** · evidence: citation-intersection · contact surface: 0 · last checked 2026-09-03

> Alexander (1997) and [[stress-strength-interference]] (1967) are **the same object.** Thirty-year head start, zero crossings.

## Contact surface

Alexander's *A Theory of Mixed Chains Applied to Safety Factors in Biological Systems*
(*J. Theor. Biol.* 1997, **`10.1006/jtbi.1996.0270`**) has **46 citations by OpenAlex's count.
The citing works were fetched and inspected; every one is comparative biomechanics** —
alligator limb bones, crab claw cuticle, intestinal lactase capacity.

### The count, by provider (B2 reconciliation)

| Provider | Endpoint | N | Date |
|---|---|---|---|
| **OpenAlex** | `api.openalex.org/works?filter=doi:10.1006/jtbi.1996.0270` → `cited_by_count` (W2144457609) | **46** | 2026-09-05 |
| Crossref | `api.crossref.org/works/10.1006/jtbi.1996.0270?mailto=...` → `is-referenced-by-count` | **36** | 2026-09-05 |
| OpenCitations | `api.opencitations.net/index/v1/citations/10.1006/jtbi.1996.0270`, records counted | **40** | 2026-09-05 |
| OpenCitations | `.../citation-count/10.1006/jtbi.1996.0270` | **40** (agrees with the counted list) | 2026-09-05 |
| Europe PMC | not re-run this session; earlier figure was 28 | 28 | 2026-09-03 |

**46 was never stale — it is OpenAlex, and OpenAlex still returns 46 today.**
[[stress-strength-interference]] previously called it "stale (real: 36/39/28)"; that was a
provider disagreement misread as an error, and it is corrected there. All four providers agree
on the *composition* — comparative biomechanics throughout — which is the load-bearing claim.
Which provider the original run used is **not determinable from the note**; 46 matches OpenAlex
exactly, which is the strongest available inference.

### The engineering side: 753 is withdrawn

**"Engineering's stress-strength interference literature: 753 works" is withdrawn.** It was a
**string-match artifact** — a relaxed Crossref query for the phrase returns ~1.8M, so 753 was an
arbitrary cut of a string search, not a count of a literature. See [[citation-sources]], "String
counts are not citation counts." No replacement figure is offered, because a defensible one
requires a defined anchor set rather than a phrase.

The finding does not rest on either number: the intersection is a **measured, inspected zero**,
confirmed in [[stress-strength-interference]] against four IEEE / *Microelectronics Reliability*
interference papers (84 citers) → **0 overlap**.

## The trade runs both ways

- Engineering offers biology a **probabilistic** safety factor — precisely the objection raised
  against symmorphosis since 1987.
- Biology offers engineering the **remodeling option** — a link that thickens under load, which
  stress-strength interference cannot express because its strengths are fixed at manufacture.

Computed out in [[C2-probabilistic-safety-factors]], where the second half turned out to be the
more interesting direction.

## And biology stated the logic without the citation

Diamond (2002) writes the interference argument **verbatim** in a physiology journal, and lists
*safety factors of series systems* as unsolved — the thing reliability engineering solved
decades earlier. **Biology has the concept, stated correctly, and never carried it to a number.**

## Caveat

Symmorphosis itself is contested: ~28 works total, with critiques at 100 and 79 citations
against the canon's 483. Importing "enough but not too much" imports a disputed claim.
