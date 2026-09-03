---
id: G5
name: G5-repair-number
type: gap
standing: narrowed
evidence: full-text-read
contact-surface: 1
crosses: metaphor
crosses-rank: 2
topology: direct
mediator: 
borrows-from: []
lends-to: []
mutual-with: []
computed-in: ["[[C1-availability-living-tissue]]"]
uses-move: []
rests-on: ["[[availability-formula]]", "[[kirkwood-disposable-soma]]"]
tags: [node/gap, crosses/metaphor, evidence/full-text-read, standing/narrowed]
last-checked: 2026-09-03
note: "Zero survives the homograph (all 6 MTTR hits are IT). But 'no time in it' is wrong: CDHM has healing rate constants. The missing object is the ratio, not the rate."
---

# No dimensionless repair number

**STANDING: NARROWED** · evidence: full-text-read · contact surface: 1 · last checked 2026-09-03

> The zero survived the homograph. **One sentence did not:** engineering healing is not
> time-free. The missing object is the **ratio**, not the rate.

## The correction

The note said engineering quantifies healing as "an amplitude fraction with no time in it."
**False.** Das & Kumari, [arXiv:2503.18771](https://arxiv.org/html/2503.18771v1), read in full,
put explicit timescales into a constitutive law — healing and rebonding times
`τ_h = η_h/M` and `τ_D = η_D/M`, with a diffusion-governed evolution law for the healing
variable. Continuum damage-healing mechanics has rate constants.

**What it does not have is the ratio.** No dimensionless group comparing healing rate to damage
rate. No healing-efficiency definition. No citation to reliability engineering, availability,
or biology. So the named missing object survives — sharper, because it is now a specific
missing *construction* rather than a missing *concept*.

**Restated:** self-healing mechanics has healing rate constants but forms no dimensionless
damage/healing ratio and no steady-state functional fraction. The availability form is written
on neither side.

## The zero survived the homograph, which is the point

This is the entry that predicted its own fake nonzero, and was right.

| Query | Hits | What they actually are |
|---|---|---|
| `"disposable soma"` — calibration | 908 | — |
| `"disposable soma" AND "self-healing"` | **1** | a cancer-stem-cell paper. Effectively 0 |
| `"mean time to repair" AND "self-healing"` | 6 | **all six IT/computing.** Zero materials science |
| `"mean time between failures" AND "bone"` | 5 | none about bone biology. Effectively 0 |

The six MTTR hits are the homograph in full view. A careless check counts six and refutes the
gap. See [[homographs]]. [[kirkwood-disposable-soma]] is genuinely unread in this direction.

## The one real bridge is a metaphor, and says so

[PMC6784298](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6784298/fullTextXML)
(*Biomimetics* 4(3):46), the most direct bone-biology → self-healing-materials paper found,
read in full. Its own scope statement:

> "The examples of bone remodeling and healing may provide inspiration for applications in
> very different scenarios."

Concept transfer only. One descriptive number carried across (trabecular bone remodelling at
20% of volume per year), no rate constants, no healing metric, no reliability citation. That is
`crosses: metaphor` measured rather than assumed.

## And the biology side does not already write the answer

Checked, because it would have made [[C1-availability-living-tissue]] a restatement rather
than a result.
[PMC10538756](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10538756/fullTextXML),
read in full, relates photoinhibition to `k_PI` and `k_REC` but gives **no steady-state
expression of the form `k_REC/(k_REC + k_PI)`**. Its framing is a rate inequality:

> "Physiologically relevant photoinhibition of PSII occurs when the rate of PSII
> photoinactivation exceeds the rate of PSII repair."

An inequality, not a normalised fraction. **C1 stands as computing something new.**

## Provisional

The only CDHM paper read is Das & Kumari 2025. The founding papers (Barbero et al.;
Voyiadjis & Mozaffari) were not obtainable. **If one of those already writes a damage/healing
ratio, this narrowing goes further.** Flagged as the weakest link in the re-read.
