---
id: G8
name: G8-energy-per-bit-axis
type: gap
standing: overturned
evidence: citation-intersection
contact-surface: 35
crosses: formalism
crosses-rank: 4
topology: direct
mediator: 
borrows-from: []
lends-to: []
mutual-with: []
computed-in: ["[[C3-energy-error-axis]]"]
uses-move: []
rests-on: []
tags: [node/gap, crosses/formalism, evidence/citation-intersection, standing/overturned]
last-checked: 2026-09-05
note: "Overturned, and the overturn survived re-test: citer-set intersection Landauer 1961 x (Laughlin 1998 + Attwell 2001) = 35 co-citers, ~340x the independence expectation, all inspected and on-topic (OpenCitations, 2026-09-05). The 575 string count itself is UNSOURCED and does not reproduce."
---

# The cross-substrate energy-per-bit axis

**STANDING: OVERTURNED — do not cite as a gap** · evidence: citation-intersection · contact surface: 35 (was an unsourced string count of 575) · last checked 2026-09-05

> Neuroscience counts ATP per bit. Chip design counts femtojoules per operation. Biophysics counts kT per methylation cycle.

## Overturned

`"Landauer" AND (neuron OR synapse OR brain)` returns **575** papers - **575 is UNSOURCED, see
the Provenance block below** - including *Using the Maximum
Entropy Method to Obtain an Optimal Bits-Per-Joule Neuron* and *Communication consumes 35 times
more energy than computation in the human cortex.*

That is exactly the connection the finding denied, and at 575 it is not a niche.

## What survives

The **specific figure** in [[C3-energy-error-axis]] — molecular, neural, CMOS, superconducting and
communication substrates together, with per-decade quantities on a separate band — may still be
novel in that combination. The absence claim was not, and has been removed from the page.

## Provenance

### The 575 is UNSOURCED and does not reproduce

No host, no endpoint and no date were recorded for it. Re-run 2026-09-05, nothing returns 575:

| Provider | Endpoint / query | N |
|---|---|---|
| OpenAlex | `api.openalex.org/works?filter=title_and_abstract.search:Landauer AND (neuron OR synapse OR brain)&mailto=...` | **887** |
| OpenAlex | same with `fulltext.search:` | **50,957** |
| Europe PMC | `www.ebi.ac.uk/europepmc/webservices/rest/search?query=Landauer AND (neuron OR synapse OR brain)&format=json` | **1,031** |

All fetched 2026-09-05. The counts span two orders of magnitude across query scopes, which is
[[failure-modes|the string instrument behaving exactly as documented]]. **575 stays marked
UNSOURCED** rather than quietly replaced: three new numbers do not retroactively source an old one.

### Re-tested under citation intersection - and the overturn holds

Per [[citation-intersection]], a string count may not settle a gap on its own. Run as a
**citer-set intersection** (no reference lists needed, so coverage is 100% of what the provider
indexes; script `vault/_scripts/intersect.py`, recipe in [[citation-sources]]):

**Provider: OpenCitations. Endpoint: `api.opencitations.net/index/v1/citations/<doi>`. Date: 2026-09-05.**

| Anchor | DOI | N citers |
|---|---|---|
| A - thermodynamic cost of a bit | Landauer 1961, *IBM J. Res. Dev.* 5(3):183, `10.1147/rd.53.0183` | **4,292** |
| B - energy per bit in neurons | Laughlin, de Ruyter van Steveninck & Anderson 1998, `10.1038/236` **+** Attwell & Laughlin 2001, `10.1097/00004647-200110000-00001` (pooled) | **3,882** |
| **intersection** | | **35** (0.82% of A, 0.90% of B) |

Null model, `N = 1.6x10^8` DOIs: expected co-citers under independence = 0.10, so
**observed/expected is about 340**.

Anchor DOIs verified against Crossref (`api.crossref.org/works/<doi>?mailto=...`, 2026-09-05):
Landauer `is-referenced-by-count` 4,339; Laughlin 983; Attwell 3,040.

**Re-derived on the repaired instrument, 2026-09-05 (FIX1 blank-key re-check).** Re-run with
`_scripts/intersect.py` after the blank-`citing` filter landed, `--providers=opencitations,semanticscholar`:
OpenCitations `N_A` **4,292 → 4,292** (180 blank/DOI-less records dropped), pooled `N_B`
**3,881 → 3,882** (Laughlin 1,012 + Attwell 3,054, 80 blanks dropped; the published 3,881 was one
*low*, not one high — a transcription slip, not the phantom), intersection **35 → 35**, the same
35 DOIs. The percentages are unchanged to two figures (0.82% / 0.90%). **Semantic Scholar has no
record for Landauer 1961 `10.1147/rd.53.0183`** — a coverage hole, reported as `err` and excluded
from the consensus, never as a zero. The overturn is untouched: `contact-surface` stays **35**.

**All 35 were inspected by title (Crossref, 2026-09-05).** They are not noise - they are the
claimed connection, already done:

- `10.1073/pnas.2008173118` - *Communication consumes 35 times more energy than computation in the human cortex* (the very paper the original overturn cited)
- `10.1073/pnas.1207814109` - *Energetic costs of cellular computation*
- `10.1103/physrevlett.131.068401` - *Physical Constraints in Intracellular Signaling: The Cost of Sending a Bit*
- `10.1109/5.939817` - *Capacity and energy cost of information in biological and silicon photoreceptors* - this one spans neural **and** silicon, the exact cross-substrate move
- `10.1098/rsta.2016.0343` - *The thermodynamic efficiency of computations made in cells across the range of life*
- `10.1371/journal.pcbi.1003157`, `10.1007/s10827-009-0153-7`, `10.3390/e26090779`,
  `10.1561/3500000006` (*Of Brains and Computers*), and 26 more in the same register

**Verdict: the overturn was reached with a bad instrument and is nonetheless correct.** The
absence claim is refuted by an inspected citation intersection at ~340x chance, not by a string
count. What [[C3-energy-error-axis]] may still own is the *specific* five-substrate figure with
a per-decade band - none of the 35 assembles that.

A standing change is **proposed in [[log]]**, not applied here: keep `overturned`, move
`evidence` from `string-protocol` to `citation-intersection`, and move `contact-surface` from
the unsourced 575 to the inspected **35**, so the retraction meets the same bar as an assertion.
