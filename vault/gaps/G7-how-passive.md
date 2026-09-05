---
id: G7
name: G7-how-passive
type: gap
standing: narrowed
evidence: full-text-read
contact-surface: 2
crosses: metaphor
crosses-rank: 2
topology: disjoint
mediator: 
borrows-from: []
lends-to: []
mutual-with: []
computed-in: ["[[C14-degree-of-passivity]]"]
uses-move: ["[[M4-change-the-actor]]"]
tags: [node/gap, crosses/metaphor, evidence/full-text-read, standing/narrowed]
rests-on: []
last-checked: 2026-09-05
note: "Ladder reinvented independently in exoskeletons, structural control and facades - not nuclear-only. Citer trace completed 2026-09-05: TECDOC-626 has no DOI, but OpenAlex full-text search finds 57 works citing it and every one is nuclear. So the literal sub-claim is answered YES, nobody outside nuclear uses the A-D ladder. No field has a NUMBER, so the metric gap holds and is sharper."
---

# How passive is it?

**STANDING: NARROWED** · evidence: full-text-read · contact surface: 2 · last checked 2026-09-05

> At least four fields have each built their **own** ordinal passive-to-active ladder. None
> shares a name, none cites another, and **not one of them is a number.**

## The sub-claim resolved — and it split in two

The note called IAEA-TECDOC-626's Category A–D ladder the **"best find"**, an object the rest
of the world lacks. Two different questions were hiding inside that, and they get different
answers.

**The literal question — does anyone outside nuclear cite TECDOC-626's A–D ladder? — was
STILL-UNVERIFIED, and is now ANSWERED: no. Completed 2026-09-05, see the Provenance block below.** It was
recorded as unanswerable because the citation APIs were down; they are up, and the trace runs.
TECDOC-626 has no DOI, so DOI-keyed providers cannot see it at all — but OpenAlex indexes the
full text of citing works, and a full-text search for the report finds **57 works, every one of
them nuclear**. TECDOC-626 itself still could not be read (both IAEA PDFs returned HTTP 402), so
the *content* of Categories A–D remains second-hand here.

**The natural question — does an ordinal how-much-actuation ladder exist only in nuclear
engineering? — is REFUTED by reading.** At least three other fields built one independently:

- **Exoskeletons.** Read in full,
  [PMC7344163](https://pmc.ncbi.nlm.nih.gov/articles/PMC7344163/). A formal intermediate rung
  with a stated criterion: *"QPA refers to any controllable element that cannot apply a
  non-conservative motive force"*, and the ladder as a direction of travel: *"the actuation
  may be simplified moving from an active to a quasi-passive assistance"*. That is
  TECDOC-626's own move — intermediate categories defined by which active ingredient is
  retained — arrived at independently.
- **Structural vibration control.** Passive / semi-active / hybrid / active, graded explicitly
  by external power. **Search-surface only; provisional.**
- **Adaptive façades.** Passive / hybrid / active as a stated axis. **Abstract only; provisional.**

Only the exoskeleton case meets the symmetry rule on its own. It is enough to demote the
"best find" framing.

## The metric was built, and it narrows the gap: [[C14-degree-of-passivity]]

**A portable number exists — but only on one of the two axes.** The naive "fraction of response
surviving" is broken (for protective devices it exceeds 1 by sign inversion, and the subtraction
is meaningless under nonlinearity). Recast as a **cycle-averaged energy fraction** — actuator
energy metered directly, never inferred — it is well-defined and portable across a stride, a
load cycle, a thermal cycle.

**And the ladder is a lattice, confirmed — the Boolean square B².** Two independent bits:
*(1) does it inject non-conservative energy?* and *(2) does it need a control signal?* That
explains everything:

- Exoskeleton **quasi-passive** and structural **semi-active** are **the same cell** (0,1) — two
  names for one lattice position. The G7 phenomenon at single-cell resolution.
- Cell (1,0) — injects energy, needs no signal (open-loop) — is real and **unnamed in every
  field.**
- "Hybrid" is a *sum* of (0,0)+(1,1), not a rung.

No total order can carry a width-2 lattice, so each field linearised the square along a
different diagonal — the **same linearisation failure as [[C12-pi-space-lattice]]**, stated here
as an order-dimension result.

**Verdict: narrows.** The energy number `P` closes the energy axis (and control theory's
passivity index turns out to be its rigorous twin on that same axis — a half-synonym, not the
false friend the homograph register assumed). But `P` is blind to the signal axis: a
passive-dynamic walker (0,0) and a semi-active MR damper (0,1) both score `P ≈ 1` yet differ in
kind. **Fully closing G7 needs `P` plus a second portable bit for the signal axis.**

## Why this makes the gap stronger

A "one field already has the answer" gap is weak — it just needs a librarian. A "several
fields each built their own and none of them talk" gap is the real thing, and that is what
this now is.

**And none of the ladders is a metric.** All are qualitative bins. The generalisation the note
proposes — *the fraction of the response that survives when the actuation path is cut* — was
found stated by **nobody, in any field.** That named missing object survives untouched. It is
the whole gap now.

Not even standardised inside a single field:
[PMC12299220](https://pmc.ncbi.nlm.nih.gov/articles/PMC12299220/), a 2025 elbow-exoskeleton
review read in full, uses only a **binary** active/passive split.

## The homograph, now confirmed rather than suspected

Control theory has a genuinely quantitative degree of passivity — passivity indices. From
arXiv:[2601.04796](https://arxiv.org/html/2601.04796), read in full: *"it is essential to
quantify the degree of passivity a system possesses or how far it deviates from being
passive"*, with IF-OFP indices defined through a storage function.

But its *passive* means **does not generate energy**, not **needs no actuation**. Different
object. It cites no nuclear or IAEA work. This is the homograph the register warns about, and
it is now a **confirmed** dead end rather than an untested one. See [[homographs]].

## Unchanged

Contact surface stays 2 — passive dynamic walking against morphological computation returns two
real bridges inside embodied robotics, and the "no contact" claim was always overstated there.

## Provenance

### Completing the rate-limited citer trace, 2026-09-05

**The anchor has no DOI.** IAEA-TECDOC-626, *Safety Related Terms for Advanced Nuclear Plants*
(IAEA, Vienna, 1991), is grey literature: no Crossref record, no OpenCitations node, no
OpenAlex work of its own. **Every DOI-keyed provider in [[citation-sources]] is therefore blind
to it**, and no citer-set intersection of the kind used on [[G8-energy-per-bit-axis]] or
[[G27-collective-decision]] can be run. That is a fact about the anchor, not a failed lookup, and
it is why the earlier session recorded the question as unanswerable.

**The route that does work is a full-text search over citing works.** OpenAlex indexes the body
text and reference strings of indexed works, so a report cited only by an unstructured string is
still findable.

| Provider | Endpoint | Date | N |
|---|---|---|---|
| OpenAlex | `api.openalex.org/works?filter=fulltext.search:"TECDOC-626"&per-page=100&mailto=...` | 2026-09-05 | **57** |
| OpenAlex | same, `fulltext.search:"TECDOC 626"` (spacing control) | 2026-09-05 | **57** (identical set) |
| Europe PMC | `www.ebi.ac.uk/europepmc/webservices/rest/search?query="TECDOC-626"&format=json` | 2026-09-05 | **0** |
| Europe PMC | same, `"TECDOC 626"` | 2026-09-05 | **0** |
| OpenCitations | `api.opencitations.net/index/v1/citations/10.3327/jaesj.34.1116` (the 1992 *J. At. Energy Soc. Japan* note introducing TECDOC-626 — the only DOI-bearing proxy that exists) | 2026-09-05 | **1** |
| Semantic Scholar | `api.semanticscholar.org/graph/v1/paper/DOI:10.3327/jaesj.34.1116/citations` (same proxy anchor, second provider) | 2026-09-05 | **1** (the identical DOI) |

**The bare 1 is confirmed, not a phantom** *(FIX1 blank-key re-check, 2026-09-05)*. A single hit
on a small anchor is exactly the shape the OpenCitations blank-`citing` artefact manufactures, so
it was re-enumerated with the repaired `_scripts/intersect.py`: the anchor returns **one record and
zero blank keys**, so there was no phantom to drop, and **Semantic Scholar independently returns
the same single citer**. The hit is `10.3390/en13112898` — Zeliang, Mi, Tokuhiro, Lu & Rezvoi,
*Integral PWR-Type Small Modular Reactor Developmental Status, Design Characteristics and Passive
Features: A Review*, *Energies* 2020 (Crossref, 2026-09-05). It is a nuclear SMR review, so it
falls **inside** the nuclear literature and is consistent with — not a counterexample to — the
"every citer is nuclear" finding the 57 carries. The 1 stands.

Europe PMC returning 0 is a **calibrated zero**, not evidence: it is biomedicine-weighted and
indexes essentially no nuclear-engineering literature, exactly the miscalibration
[[failure-modes]] warns about. The load-bearing number is the OpenAlex 57.

### All 57 classified by venue and topic - none is outside nuclear

Every one of the 57 was listed with its publication year, OpenAlex primary topic and source
(same query, 2026-09-05). The distribution:

| Field of the citing work | count |
|---|---|
| Nuclear engineering / thermal-hydraulics / reactor physics / nuclear materials | ~44 |
| Reliability and probabilistic engineering design, applied to **nuclear passive systems** | ~8 |
| Nuclear licensing, regulation and energy policy | 3 |
| Ethics of technology, with nuclear energy as the case (*NanoEthics* 2017 "Safe-by-Design"; *Sci. Eng. Ethics* 2024 on energy-system values) | 2 |
| **Exoskeletons, structural vibration control, adaptive facades, robotics, control theory** | **0** |

Representative titles: *Emerging small modular nuclear power reactors: A critical review*
(`10.1016/j.physo.2020.100038`), *A review: passive system reliability analysis*, *Quantitative
functional failure analysis of a thermal-hydraulic passive system*
(`10.1016/j.anucene.2010...`), *Pathways and frameworks for the licensing and regulation of
advanced nuclear reactors* (MIT), *Inherent Safety Characteristics of Advanced Fast Reactors*.
The two ethics papers are still about nuclear energy; they are not another field borrowing the
ladder.

**Result: the A-D ladder has zero uptake outside nuclear engineering, N = 57, OpenAlex full-text,
2026-09-05.** This is the sub-claim the note flagged as unresolvable, now resolved in the
direction the note guessed - and it *strengthens* the gap rather than weakening it. Combined with
the exoskeleton, structural-control and facade ladders read earlier, the picture is now measured
on both sides: **four fields, four independently invented ordinal ladders, and the one with a
formal published taxonomy is cited by nobody outside its own field.** That is the definition of
this gap.

### Caveat on what 57 measures

`fulltext.search` matches the report's designator wherever OpenAlex has body text or a reference
string, so 57 is a **lower bound**: a work citing the report as "IAEA (1991)" without the TECDOC
number is invisible to it, and OpenAlex's full-text coverage is far from complete. A larger true
number would not change the classification result unless the missing works are systematically
non-nuclear, which there is no reason to expect.

### Proposed standing change

**None.** `standing: narrowed`, `evidence: full-text-read`, `contact-surface: 2` all stand. The
trace closes an outstanding sub-claim and hardens the note; it does not move the gap, because
the gap's whole content is now the **missing metric**, and no citer trace bears on that. What
this does retire is item 3 on the [[00-index]] open-work list ("Trace citers of the nuclear
passivity ladder - rate-limited before completing"). Noted in [[log]].
