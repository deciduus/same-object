---
id: G36
name: G36-wear-erosion-damage
type: gap
standing: live
evidence: citation-intersection
contact-surface: 0
crosses: formalism
crosses-rank: 4
topology: disjoint
mediator: 
borrows-from: []
lends-to: []
mutual-with: []
computed-in: ["[[C35-soil-ha]]"]
uses-move: []
rests-on: ["[[C6-damage-healing-ratio]]"]
tags: [node/gap, crosses/formalism, evidence/citation-intersection, standing/live]
last-checked: 2026-09-05
exit: computation
extends-to: [sustainability, conservation]
next-step-cost: S
note: "Mechanics of material removal and soil science meet nowhere. Thirteen anchor pairings across four mechanics anchors (1945, 1953, 1963, 1995) and three soil anchors (1996, 1999, 2001) return 0 on OpenCitations; four internal controls fire at 257, 242, 204/38 and 60. |A|.|B| = 4.6e5 to 8.2e6, so E > 1 survives any N under ~6-8M on the two leading cells. Leg 2 reaches C6's empty soil row and C35 fills it."
---

# Wear, fatigue, and the removal of soil

**STANDING: LIVE** · evidence: citation-intersection · contact surface: 0 · last checked 2026-09-05

> Two engineering literatures have spent eighty years writing laws for **how much solid a
> repeated mechanical insult removes from a surface**, and soil science has spent the same
> eighty years measuring exactly that on soil and never once citing them. Tribology writes
> `V = K·F·s/H`; fracture mechanics writes `D = Σ n_i/N_i` and `da/dN = C(ΔK)^m`; soil science
> writes `D_c = K_r(τ − τ_c)` and reports mean weight diameter after *n* wet–dry cycles. The
> claim here is not that the mechanisms are identical — they are not — but that the
> **constitutive objects are the same kind of object**, and that neither field has ever looked
> at the other's forty years of trouble with fitting them.

Two legs, one gap, because they share the mechanics anchors and fail together:

- **Leg 1 — wear ↔ erosion detachment.** Archard 1953 / Meng & Ludema 1995 against Nearing 1989
  (WEPP) / Le Bissonnais 1996.
- **Leg 2 — cumulative fatigue ↔ aggregate breakdown under wet–dry cycling.** Miner 1945 /
  Paris & Erdogan 1963 against Le Bissonnais 1996 / Denef 2001 / Amézketa 1999.

Leg 2 is the one that reaches an existing vault object with **both numerator and denominator
already published**: it instantiates [[C6-damage-healing-ratio]]'s `Ha = k_r/k_d` with erosion
rates as `k_d` and soil-formation rates as `k_r`, filling a row C6 left blank. That computation
is [[C35-soil-ha]].

## The two vocabularies

| | Mechanics side | Soil-science side |
|---|---|---|
| **The removal law** | Archard: wear volume `V = K·(F·s)/H` — removed volume ∝ normal load × sliding distance ÷ indentation hardness | WEPP (Nearing 1989): detachment capacity `D_c = K_r(τ − τ_c)` — mass removed per area per time ∝ excess hydraulic shear |
| **The fitted constant** | `K`, the **Archard wear coefficient**, dimensionless, spanning orders of magnitude and not predicted from bulk properties (Meng & Ludema 1995 exists because several hundred wear equations do not predict it) | `K_r`, **rill erodibility** (s/m), and `K_i`, **interrill erodibility**; and USLE/RUSLE's **K-factor**, a soil erodibility index. All calibrated, none derived |
| **The threshold** | none in Archard's form; wear is linear in `F·s` through the origin | `τ_c`, **critical shear stress** — below it, detachment is zero |
| **The repeated-insult law** | Miner: `D = Σ n_i/N_i`, failure at `D = 1`. Paris: `da/dN = C(ΔK)^m`, damage per cycle as a power of the driving range | **aggregate stability under wet–dry cycles**: apply *n* wetting/drying or slaking cycles, report **mean weight diameter (MWD) loss** or the % of aggregates surviving. The cycle count is reported; no damage law is fitted to it |
| **What accumulates** | a scalar damage fraction, or a crack length | an aggregate-size distribution, or a soil depth |

Both sides are quantified, both are published as calibrated laws, and the four objects
`K`, `K_r`, `K_i`, `K_USLE` are the same *species* of object: an empirically fitted dimensional
constant standing in for an unresolved contact mechanism.

## Provenance — counts re-derived 2026-09-05

**Instrument.** Citer-set intersection over **OpenCitations**, endpoint
`https://api.opencitations.net/index/v1/citations/<doi>`, one call per anchor, sets intersected
locally. **Blank `citing` records dropped before set construction** — the phantom-element trap
documented in `_scripts/intersect.py`; drop counts on this run were Archard 21, Paris 15,
Miner 13, Meng 2, Amézketa 1, and 0 for Nearing, Le Bissonnais, Denef and RUSLE. All nine anchor
DOIs re-verified against **Crossref** `api.crossref.org/works/<doi>?mailto=deciduusleaf@gmail.com`
the same day. Re-runnable: `python _scripts/c35_soil.py --fetch` from `vault/`. **OpenAlex was
not called** — see the denominator paragraph for why it was not needed.

**Anchors** (Crossref `is-referenced-by-count` / OpenCitations citer set, both 2026-09-05):

| side | anchor | DOI | Crossref | OC set |
|---|---|---|---|---|
| A | Archard 1953, *Contact and Rubbing of Flat Surfaces*, J. Appl. Phys. | `10.1063/1.1721448` | 7,175 | **6,803** |
| A | Meng & Ludema 1995, *Wear models and predictive equations*, Wear | `10.1016/0043-1648(95)90158-2` | 783 | **767** |
| A | Miner 1945, *Cumulative Damage in Fatigue*, J. Appl. Mech. | `10.1115/1.4009458` | 4,962 | **4,762** |
| A | Paris & Erdogan 1963, *A Critical Analysis of Crack Propagation Laws*, J. Basic Eng. | `10.1115/1.3656900` | 5,569 | **5,461** |
| B | Nearing *et al.* 1989, *A Process-Based Soil Erosion Model … (WEPP)*, Trans. ASAE | `10.13031/2013.31195` | 1,142 | **1,122** |
| B | Le Bissonnais 1996, *Aggregate stability … crustability and erodibility I*, Eur. J. Soil Sci. | `10.1111/j.1365-2389.1996.tb01843.x` | 1,225 | **1,207** |
| B | Denef *et al.* 2001, *Influence of dry–wet cycles …*, Soil Biol. Biochem. | `10.1016/s0038-0717(01)00076-1` | 599 | **604** |
| B | Amézketa 1999, *Soil Aggregate Stability: A Review*, J. Sustain. Agric. | `10.1300/j064v14n02_08` | 1,003 | **991** |
| ctl | Renard *et al.* 1991, *RUSLE*, J. Soil Water Conserv. | `10.1080/00224561.1991.12456571` | 680 | **603** |

**The grid. Thirteen pairings, thirteen zeros.** `E` is the **union floor**
`|A|·|B|/(|A|+|B|−O)`, which gives the largest `E` and so flatters the claim; it is never
quotable alone.

| A \ B | Nearing 1989 (1,122) | Le Bissonnais 1996 (1,207) | Denef 2001 (604) | Amézketa 1999 (991) |
|---|---|---|---|---|
| **Archard 1953** (6,803) | **0** (E 963.2) | **0** (E 1,025.1) | **0** (E 554.7) | **0** (E 865.0) |
| **Meng & Ludema 1995** (767) | **0** (E 455.6) | **0** (E 469.0) | **0** (E 337.9) | not run |
| **Miner 1945** (4,762) | not run | **0** (E 962.9) | **0** (E 536.0) | **0** (E 820.3) |
| **Paris & Erdogan 1963** (5,461) | not run | **0** (E 988.5) | **0** (E 543.8) | **0** (E 838.8) |

Leg 1 is the four upper-left cells plus Archard × Denef/Amézketa; leg 2 is the eight cells on
the fatigue rows plus Meng × Denef. Both legs are zero without exception.

**Four internal controls, same instrument, same day.** These are the load-bearing statistic:
`N_universe` cancels in a control ratio, so it is invariant under the denominator.

| control | pair | \|A\| / \|B\| / O | E (floor) | O/E |
|---|---|---|---|---|
| mechanics-internal | Miner 1945 × Paris 1963 | 4,762 / 5,461 / **257** | 2,609.4 | 0.0985 |
| tribology-internal | Meng & Ludema × Archard | 767 / 6,803 / **242** | 712.0 | 0.340 |
| **soil-aggregate-internal (new)** | **Amézketa 1999 × Le Bissonnais 1996** | 991 / 1,207 / **204** | 599.9 | **0.340** |
| soil-aggregate-internal | Denef 2001 × Le Bissonnais 1996 | 604 / 1,207 / **38** | 411.2 | 0.0924 |
| erosion-internal | RUSLE 1991 × Nearing 1989 | 603 / 1,122 / **60** | 406.3 | 0.148 |

Control ratios, in the two forms that hold one anchor fixed:

- **Leg 1, shared B** (Nearing fixed, swap A from Archard to RUSLE): `(0/6,803)/(60/603)` = **∞**.
- **Leg 1, shared A** (Archard fixed, swap B from Nearing to Meng): `(0/1,122)/(242/767)` = **∞**.
- **Leg 2, shared A** (Miner fixed, swap B from Le Bissonnais to Paris): `(0/1,207)/(257/5,461)` = **∞**.
- **Leg 2, shared B** (Le Bissonnais fixed, swap A from Miner to Amézketa): `(0/4,762)/(204/991)` = **∞**.

The instrument detects the event when it happens — four times, in both directions, on the same
anchors. It does not happen across the gap.

**Denominator, stated as a limit.** Every `E` above is a union floor. The reason this pairing
does not need a scoped `N` is that `|A|·|B|` is large: **7.63×10⁶** for Archard × Nearing and
**5.75×10⁶** for Miner × Le Bissonnais, so `E > 1` holds for any `N` below ~6–8 million works.
Sensitivity on the Archard × Nearing cell: `E = 7.6` at `N = 10⁶`; `E = 0.76` at `N = 10⁷`, where
the zero would stop being informative. A tribology ∪ soil-erosion universe is not plausibly 10⁷.
**The weakest cells are the Meng & Ludema rows** (`|A|·|B| = 3.4–9.3×10⁵`), which need
`N < ~5×10⁵` and do not have one; they are corroboration, not evidence.

**Hits inspected: none, because there are none.** Every one of the thirteen gap cells is 0, so
there is nothing to read. The five control intersections were **not** individually inspected —
they are counts, not verified bridges, and are used here only as instrument checks, which is all
a control ratio requires.

**Failure modes, checked before reporting the zero** ([[failure-modes]]).

- Modes 1–5 do not apply in their usual form: this is a **citer-set intersection**, not a string
  query, so punctuation, homographs, synonyms and Boolean relaxation cannot manufacture the
  count. What *can* is anchor choice, which is why four mechanics anchors and three soil anchors
  were used rather than one of each.
- **Mode 6 (diachronic drift), partly addressed.** The mechanics side samples **1945 / 1953 /
  1963 / 1995**, so both a 1940s-vocabulary and a 1990s-vocabulary version of the damage side is
  tested. **The soil side is entirely 1989–2001 and this is the standing hole in the note.** A
  1960s soil-structure anchor (Emerson, Yoder's wet-sieving) and a 1930s–1960s erosion anchor
  (Ellison 1947, the original USLE) have **not** been tested. Under this vault's own rule a
  pooled zero across a 60-year window is not one measurement, and the mechanics half of that
  requirement is met while the soil half is not. **The zero is therefore reported as live, not
  as settled**, and the first cheap thing that could overturn it is a decade-binned soil anchor.

**Strongest objection, both legs, stated rather than answered.**

1. *Leg 1: the abrasive medium is the difference and it is not a detail.* Archard's law is
   derived for two solids in dry contact with the real contact area set by plastic yielding at
   asperities. Soil detachment by overland flow is fluid shear on a cohesive granular bed with no
   solid counterface, so indentation hardness `H` has no counterpart and `K` cannot be read the
   way tribology reads it. The defensible comparison is between `K` and `K_r` **as fitted
   constants** — how many orders each spans, and whether either was ever predicted rather than
   fitted — not a claim of shared mechanism. [[C35-soil-ha]] §4 works the mapping through and
   reports where it breaks.
2. *Leg 2: slaking is not fatigue.* Aggregate breakdown on first wetting is dominated by
   entrapped-air compression and differential clay swelling — a single-event quasi-static
   failure — while fatigue requires the load to sit below the single-cycle failure threshold. If
   most loss happens on cycle 1, the object is fracture toughness and a Miner framing is
   arithmetic on the wrong variable. **This is checkable in already-published data**: Denef 2001
   and the Amézketa 1999 review print stability at successive cycle numbers, so first-cycle
   dominance versus progressive accumulation can be read off. A soil still losing stability at
   cycle 5 is not slaking.

## What would close it

Two objects, both computable from published tables, in the cheap order:

1. **The soil row of C6's axis** — `Ha = k_r/k_d` with erosion rate as `k_d` and soil formation
   rate as `k_r`. **Done, in [[C35-soil-ha]]**, which is why `exit: computation` and
   `next-step-cost: S`. It closes the *reachability* half of leg 2 and produces the T-value
   prediction; it does not close the gap, because a computation performed here is not a citation
   made there.
2. **`K` and `K_r` on one dimensionless axis** — normalise Archard's wear coefficient and WEPP's
   rill erodibility to the same form (removed volume per unit work per unit resisting stress) and
   tabulate the range each spans, from Archard's own table and Meng & Ludema's compilation
   against WEPP's published `K_r` calibration ranges. The prediction that follows: **both span
   4–6 orders of magnitude and neither is predictable from bulk properties**, which would say two
   fields independently hit the *same* failure of a constitutive law. C35 §4 shows the unit
   reconciliation is where this dies if it is not written out first, and does write it out.
3. **A Weibull/Miner damage curve for aggregate stability against wet–dry cycle number**, with
   its shape parameter placed on [[C18-durability-axis]]'s β axis next to the flow-battery β ≈ 1
   and Li-ion β = 12.7 rows — the first soil entry after [[C29-recovery-beta]]'s ecological β.
   Discriminating prediction: aggregates held by *organic* binding should show progressive
   (β ≈ 1–2, Miner-like) loss, aggregates held by physical entrapment first-cycle-dominated
   (β ≫ 1) loss, so an organic amendment moves the **shape**, not only the mean. Trap: many
   wet–dry studies report only cycles 1 and *n*, which cannot separate the two shapes; the fit
   needs ≥3 cycle points and papers giving two must be excluded and said to be excluded.

What would **overturn** it, cheaply: a decade-binned soil anchor from the 1930s–1960s
(Ellison 1947, Yoder 1936, Emerson 1967) returning a non-zero against any mechanics anchor. That
is the mode-6 hole above, and it has not been run.
