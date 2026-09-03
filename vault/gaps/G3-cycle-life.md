---
id: G3
name: G3-cycle-life
type: gap
standing: narrowed
evidence: full-text-read
contact-surface: 4
crosses: formalism
crosses-rank: 4
topology: direct
mediator: 
borrows-from: []
lends-to: []
mutual-with: []
computed-in: ["[[C18-durability-axis]]"]
uses-move: ["[[M3-separate-timescales]]"]
rests-on: []
tags: [node/gap, crosses/formalism, evidence/full-text-read, standing/narrowed]
last-checked: 2026-09-03
note: "Narrowed: Hanson PNAS 2021 adopts CCR 'guided by catalyst engineering' as the in vivo TTN - that leg is bridged one-way. The unbridged leg is energy storage: cycle life vs TTN = 0."
---

# No cycle-life framework

**STANDING: NARROWED** · evidence: full-text-read · contact surface: 4 · last checked 2026-09-03

> The four-way claim was wrong. **One leg is already bridged by name, in PNAS.** What survives
> is the other leg: catalysis durability and *energy storage* durability share no axis in
> either direction.

## The leg that is bridged

Hanson et al., *PNAS* 118 (2021),
[PMC8020674](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8020674/fullTextXML),
read in full:

> "Guided by catalyst engineering, we adopted catalytic cycles until replacement (CCR) as a
> metric for enzyme functional life span in vivo."

> "the number of catalytic cycles that each enzyme molecule carries out in its lifetime —
> often called 'total turnover number' — is a key industrial performance criterion."

That is not a metaphor. Biology **took the metric from catalyst engineering and said so.**
It is [[one-way-borrowing]]: nothing indicates catalysis reads back. Under
[[relationship-description]] that is a description, not a zero.

The paper also gives the numbers: CCR ranges `<10³` to `>10⁷`, with medians of 3–4×10⁴ in
*L. lactis* and yeast against 4×10⁵ in *Arabidopsis*.

## The leg that survives, cleanly

Energy storage. Both sides calibrate strongly and the intersection is noise:

| Query (Europe PMC) | Hits |
|---|---|
| `"cycle life"` — calibration | 11,391 |
| `"total turnover number"` — calibration | 600 |
| **`"cycle life" AND "total turnover number"`** | **0** |
| **`"capacity fade" AND "turnover number"`** | **0** |
| `"cycle life" AND "turnover number"` | 4, all incidental broad reviews |
| `"cycling stability" AND "total turnover number"` | 3, incidental |

**Restated gap:** no shared durability axis between turnover-number catalysis — biological and
industrial, already unified — and cyclic energy storage: battery cycle life, capacity fade,
thermochemical cyclic stability.

## The construction: the shared axis is a failure-law shape, not a cycle count ([[C18-durability-axis]])

A single cycle count `N_fail` does **not** span the two legs — it hides the failure law.
Enzymes die by a **discrete per-cycle catastrophe**, `N_fail = 1/p` where `p` is the enzymology
partition ratio (TTN *is* the partition ratio) — a memoryless, constant-hazard process. Li-ion
cells die by **cumulative wear-out**, `N_fail = tolerance/f`, a threshold crossing. The same
`N_fail ≈ 500` encodes a flat-hazard lottery in one and a synchronized wall in the other. Same
number, two different reliability distributions — the [[stress-strength-interference]]
discrete-vs-continuous split again.

**The bridge that does span both is the Weibull shape parameter β.** `β = 1` (constant hazard,
exponential) is the enzyme signature — first-order thermal deactivation *is* `β = 1`. Li-ion is
`β > 1` (wear-out; ~12.7 reported for one cell, VERIFIED-via-search only). β is dimensionless,
spans both legs, and classifies by **failure physics, not by field.**

**The new result it produced:** organic flow-battery reactants degrade by **calendar-time
chemical decay, β ≈ 1** — the *same failure law as enzyme death*, not Li-ion's. So the bridge
reclassifies flow-battery chemistry **with** enzymes and isolates Li-ion electrode wear as the
outlier. Nobody has drawn both β values on one plot — battery-side β fits are routine, enzyme-side
β is left implicit in bulk decay curves. So G3 **narrows to: same count, different failure law,
and the shared coordinate is β.**

## Two things the reading added

**Biology has a repair break-even formalism, and it is sealed inside biology.**
[PMC6282526](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6282526/fullTextXML),
read in full, writes it out:

> "(Repair Cost) < (TON × ATP/cycle) [ATP]"

> "PS II requires only 500–1000 cycles to generate the ATP required for repair"

Genuine cycles-until-replacement economics. No benchmarking against artificial catalysts.

**TTN is contested on its own side.**
[PMC6804192](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6804192/fullTextXML),
read in full, says **"TTN alone is a poor measure of catalyst performance"** — activity and
stability both feed it, and it depends on operating conditions. Worth knowing before proposing
it as anyone's shared axis.

## Unchanged

Where the neglect actually lives: not batteries, where cycle life is a headline spec.
Thermochemical storage, where a celebrated result reads *"stable for at least ten cycles"*
while organic flow chemistries quote fade below **0.001% per cycle**.

Biology's strategy remains **a cheap catalyst plus a continuous replacement line**, not a
durable one. ATP holds ~50 g against ~60 kg/day turnover — the carrier is a bus, not a tank.

## Limit, stated

Europe PMC is biomedicine-weighted. The `"cycle life"` calibration at 11,391 shows the
energy-storage literature is findable there, so the zeros mean something — but a Scopus or Web
of Science replication would strengthen them. Bommarius 2023 was not obtained (Wiley paywall)
and is not used as evidence.
