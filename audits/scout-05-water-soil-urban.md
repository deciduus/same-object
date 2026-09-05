# Scout: water, soil, urban

Scouting pass, **2026-09-05**. Read-only on `vault/`; no git operations run.

**Instrument.** Citer-set intersection over **OpenCitations**, endpoint
`https://api.opencitations.net/index/v1/citations/<doi>`, one call per anchor, sets intersected
locally (the `vault/_scripts/intersect.py` method, re-implemented with a disk cache so each
anchor was fetched once). **All anchor DOIs verified against Crossref**
`api.crossref.org/works/<doi>?mailto=deciduusleaf@gmail.com`, same day; author, year, title and
`is-referenced-by-count` read from the returned record.

**OpenAlex was not called.** The budget lock allowed one probe; it was not spent, because the
one thing it would have bought — a concept-scoped `N_universe` — is not what the two leading
candidates need (see Summary line 4). The probe is banked.

**Every `E` below is the union floor** `|A|·|B|/(|A|+|B|−O)`, and is labelled as such. Per
`vault/method/citation-intersection.md` the floor gives the largest `E` and so the smallest
`O/E`; it flatters a gap claim and is never quotable alone. The load-bearing statistic in every
row is the **control ratio**, which is invariant under `N`.

Nothing here is a vault standing. These are leads at the strength stated.

## Summary

- **26 pairings run; 13 returned 0, four returned 1–3, and twelve controls fired at 6–257.** The
  controls were run on the same instrument the same day, and they separate cleanly from the
  zeros — the same signature the circularity and resilience scouts got.
- **The two strongest candidates are both "damage accumulation, two vocabularies": mechanical
  fatigue ↔ soil aggregate breakdown under wet–dry cycling, and Archard wear ↔ soil erosion
  detachment.** Seven pairings across four mechanics anchors (1945, 1953, 1963, 1995) and three
  soil anchors (1996, 1999, 2001) returned **0 without exception**, while the mechanics-internal
  control (Miner × Paris) returns **257**, the tribology-internal control (Meng × Archard)
  **242**, the soil-internal control (Denef × Le Bissonnais) **38**, and the erosion-internal
  control (RUSLE × WEPP) **60**.
- **The orchestrator's prediction was right and is now proved: Danckwerts RTD ↔ groundwater
  transit time is bridged.** Danckwerts 1953 × Małoszewski & Zuber 1982 = **21 co-citers**. So
  that pairing is dead as a gap — but it is alive as the **best positive control in this scout**,
  because holding Danckwerts fixed and swapping the partner to soil-carbon transit times gives
  **0**. The soil-carbon side did not import RTD theory *and did not import it second-hand from
  hydrology either*: Małoszewski & Zuber × Sierra 2016 = **0** as well.
- **The fatigue/wear candidates are the only ones robust to the denominator.** `|A|·|B|` is
  5.75×10⁶ (Miner × Le Bissonnais) and 7.63×10⁶ (Archard × WEPP), so `E > 1` for **any**
  `N_universe` below ~6–8 million works — the zeros stay informative at whole-field scale, not
  just at the floor. Every other candidate here needs a scoped `N` below 10⁵–10⁶ to mean
  anything, and does not have one.
- **Two candidates died on inspection rather than on count, which is the useful output.** Urban
  metabolism ↔ ecological network analysis returns 8, and all eight are genuine urban-ENA papers
  (*J. Ind. Ecol.*, *Ecological Modelling*, *Sci. Total Environ.*) — a joined literature, plus
  Bettencourt 2007 × Kennedy 2007 = **110**. Washburn ↔ Philip returns 8, of which **seven are
  building-materials sorptivity papers and one is a book's back-matter bibliography** — the
  G27 trap — leaving exactly one soil-science work.

## Ranked candidates

`E` = **union floor**, always. "Informative at field scale?" asks whether `|A|·|B| > 10⁶`, i.e.
whether `E > 1` survives a realistic `N` — a necessary, not sufficient, condition.

| # | candidate (A ↔ B) | anchors (DOI, Crossref-verified 2026-09-05) | N_A / N_B / ∩ | E (floor) | control ratio | informative at field scale? | cost to close | extends · `extends-to` |
|---|---|---|---|---|---|---|---|---|
| **1** | Cumulative fatigue damage ↔ soil aggregate breakdown under wet–dry cycles | `10.1115/1.4009458` (Miner 1945) ↔ `10.1111/j.1365-2389.1996.tb01843.x` (Le Bissonnais 1996) | 4,762 / 1,207 / **0** | 962.9 | **∞** (ctl 257, 38) | **yes** (\|A\|·\|B\| = 5.75×10⁶) | 6–8 h desk | C18, G12 · `extends-to: sustainability` |
| **2** | Archard wear law ↔ soil detachment / erosion rate | `10.1063/1.1721448` (Archard 1953) ↔ `10.13031/2013.31195` (Nearing/WEPP 1989) | 6,803 / 1,122 / **0** | 963.2 | **∞** (ctl 60, 242) | **yes** (7.63×10⁶) | 5–7 h desk | C6, C18 · `extends-to: conservation` |
| **3** | Chemical-reactor residence-time distribution ↔ soil organic carbon transit-time distribution | `10.1016/0009-2509(53)80001-1` (Danckwerts 1953) ↔ `10.1111/gcb.13556` (Sierra 2016) | 2,463 / 156 / **0** | 146.7 | **∞** (ctl 21 on A, 21 on B) | no (3.8×10⁵) | 4–6 h desk | C31, availability-formula · `extends-to: circularity` |
| **4** | Power-system static state estimation ↔ water-distribution leak detection | `10.1109/TPAS.1970.292680` (Schweppe 1970) ↔ `10.1080/15730621003610878` (Puust 2010) | 323 / 616 / **0** | 211.9 | **∞** (ctl 43, 50) | no (2.0×10⁵, marginal) | 5–8 h desk | G29 · `extends-to: sustainability` |
| **5** | Stretched-exponential / KWW relaxation ↔ streamflow recession curves | `10.1039/tf9706600080` (Williams–Watts 1970) ↔ `10.1029/WR013i003p00637` (Brutsaert & Nieber 1977) | 3,998 / 627 / **0** | 542.0 | **∞** (ctl 19) | borderline (2.5×10⁶) | 6–10 h desk | C15, C29 · `extends-to: ecology` |
| **6** | Langmuir adsorption isotherm ↔ soil carbon saturation ceiling | `10.1021/ja02242a004` (Langmuir 1918) ↔ `10.1023/A:1004213929699` (Hassink 1997); also ↔ `10.1023/A:1016125726789` (Six 2002) | 20,220 / 1,170 / **1**; 20,220 / 3,853 / **2** | 1,106.1; 3,236.6 | **36×**; **60×** (ctl 6) | yes, but **one real bridge** | 3–5 h desk | C31 (`A_circ ≤ r` ceiling) · `extends-to: circularity` |
| **7** | CUSUM / change-point detection ↔ leak detection in water networks | `10.1093/biomet/41.1-2.100` (Page 1954) ↔ `10.1080/15730621003610878` (Puust 2010) | 2,915 / 616 / **1** | 508.7 | **687×** (ctl 50) | borderline (1.8×10⁶) | 4 h desk | G29 · `extends-to: sustainability` |
| **8** | RTD moment analysis ↔ pharmacokinetic statistical moments (MRT) | `10.1016/0009-2509(53)80001-1` ↔ `10.1007/BF01062109` (Yamaoka 1978) | 2,463 / 1,301 / **1** | 851.5 | **41×** (ctl 21) | borderline (3.2×10⁶) | 4 h desk | C31 · `extends-to: circularity` |
| 9 | Washburn capillary imbibition ↔ Green-Ampt/Philip infiltration | `10.1103/PhysRev.17.273` (Washburn 1921) ↔ `10.1097/00010694-195705000-00002` (Philip 1957) | 6,057 / 942 / **8** | 816.1 | **1.8×** on A, 38× on B | — | — | **bridged via building materials — narrowed at best** |
| 10 | Percolation-theory permeability ↔ soil infiltration / hydraulic conductivity | `10.1103/physrevb.34.8179` (Katz & Thompson 1986) ↔ `10.1063/1.1745010` (Richards 1931) | 1,013 / 4,597 / **7** | 831.1 | 17× on B | — | — | **prior art invisible to COCI (Hunt & Ewing 2014 book)** |
| 11 | Urban metabolism ↔ ecological network analysis (ascendency) | `10.1016/j.compbiolchem.2004.09.001` (Ulanowicz 2004) ↔ `10.1162/jie.2007.1107` (Kennedy 2007) | 499 / 1,035 / **8** | 338.4 | — | — | — | **rejected — joined literature** |
| 12 | Monod growth kinetics ↔ anaerobic digestion model (ADM1) | `10.1146/annurev.mi.03.100149.002103` ↔ `10.2166/wst.2002.0292` | 3,759 / 1,803 / **42** | 1,227.8 | — | — | — | **rejected — bridged** |

### Positive controls, same instrument, same day

Five of these are new to the project. The first is the in-domain control the brief required, and
it is also the orchestrator's predicted-bridged pair, proved.

| control | anchors | \|A\| / \|B\| / O | E (floor) | **O/E** | reading |
|---|---|---|---|---|---|
| **In-domain (required):** RTD × groundwater transit time | Danckwerts 1953 × Małoszewski & Zuber 1982 | 2,463 / 663 / **21** | 525.9 | 0.0399 | **closed — prediction confirmed** |
| Soil-carbon-internal | Trumbore 2000 × Sierra 2016 | 918 / 156 / **21** | 136.0 | 0.154 | closed |
| Fatigue-internal | Miner 1945 × Paris 1963 | 4,762 / 5,461 / **257** | 2,609.4 | 0.0985 | closed |
| Tribology-internal | Meng & Ludema 1995 × Archard 1953 | 767 / 6,803 / **242** | 712.0 | 0.340 | closed |
| Soil-aggregate-internal | Denef 2001 × Le Bissonnais 1996 | 604 / 1,207 / **38** | 411.2 | 0.0924 | closed |
| Erosion-internal | RUSLE 1991 × WEPP/Nearing 1989 | 603 / 1,122 / **60** | 406.3 | 0.148 | closed |
| Power-systems-internal | Monticelli 2000 × Schweppe 1970 | 590 / 323 / **43** | 219.0 | 0.196 | closed |
| Water-network-internal | Colombo & Karney 2002 × Puust 2010 | 212 / 616 / **50** | 167.9 | 0.298 | closed |
| Catchment-hydrology-internal | Brutsaert & Nieber 1977 × Kirchner 2000 | 627 / 857 / **19** | 366.8 | 0.0518 | closed |
| Soil-sorption-internal | Langmuir 1918 × Barrow 1986 | 20,220 / 194 / **6** | 192.2 | 0.0312 | closed |
| Unsaturated-flow-internal | Philip 1957 × Richards 1931 | 942 / 4,597 / **232** | 816.0 | 0.284 | closed |
| Urban-scaling × urban-metabolism | Bettencourt 2007 × Kennedy 2007 | 2,175 / 1,035 / **110** | 726.2 | 0.152 | closed |

Endpoint for every row above: `https://api.opencitations.net/index/v1/citations/<doi>`, two
calls per row, sets intersected locally. Fetched **2026-09-05**.

## Per-candidate detail

---

### 1. Cumulative fatigue damage ↔ soil aggregate breakdown under wet–dry cycling

**1. Anchors.** *A:* M. A. Miner, "Cumulative Damage in Fatigue", *J. Appl. Mech.* 12:A159–A164
(1945), DOI `10.1115/1.4009458` — Crossref verified 2026-09-05, `is-referenced-by-count` = 4,962;
OpenCitations citer set = **4,762**. Second A anchor: P. C. Paris & F. Erdogan, "A Critical
Analysis of Crack Propagation Laws", *J. Basic Eng.* 85:528–533 (1963), DOI `10.1115/1.3656900`,
Crossref 5,569 / OC **5,461**. Third: H. C. Meng & K. C. Ludema, "Wear models and predictive
equations: their form and content", *Wear* 181–183:443–457 (1995), DOI
`10.1016/0043-1648(95)90158-2`, Crossref 783 / OC **767**.
*B:* Y. Le Bissonnais, "Aggregate stability and assessment of soil crustability and erodibility:
I. Theory and methodology", *Eur. J. Soil Sci.* 47:425–437 (1996), DOI
`10.1111/j.1365-2389.1996.tb01843.x`, Crossref 1,225 / OC **1,207**. Second B: K. Denef, J. Six
*et al.*, "Influence of dry–wet cycles on the interrelationship between aggregate, particulate
organic matter, and microbial community dynamics", *Soil Biol. Biochem.* 33:1599–1611 (2001),
DOI `10.1016/s0038-0717(01)00076-1`, Crossref 599 / OC **604**. Third B: E. Amézketa, "Soil
Aggregate Stability: A Review", *J. Sustain. Agric.* 14:83–151 (1999), DOI
`10.1300/j064v14n02_08`, Crossref 1,003 / OC **991**.

**2. Same object, two sentences.** Both fields measure the fraction of a solid body that has
been destroyed by *N* applications of a sub-critical cyclic load, and both fit a rule for how
that fraction accumulates with *N*. Mechanics writes `D = Σ n_i/N_i` (Miner) or `da/dN = C(ΔK)^m`
(Paris) and reads the exponent as a statement about the damage mechanism; soil science applies
*n* wetting–drying or slaking cycles to aggregates, reports mean weight diameter or the
percentage of aggregates surviving, and reports the *number* without ever fitting a damage law
to it.

**Strongest metaphor objection.** *Slaking is not fatigue.* Aggregate breakdown on the first
wetting is dominated by entrapped-air compression and differential clay swelling — a
single-event, quasi-static failure — whereas fatigue by definition requires the load to be
below the single-cycle failure threshold. If most aggregate loss happens on cycle 1, the object
is fracture toughness, not cumulative damage, and a `D = Σ n_i/N_i` framing would be arithmetic
on the wrong variable. This is the same error `C18-durability-axis` warns about when it says one
`N_fail` hides two failure laws. **It is also why the candidate is interesting rather than fatal:
the discriminator is measurable and is already in the published data.** Denef 2001 and the
wet–dry-cycle literature report aggregate stability at successive cycle numbers, so whether
breakdown is first-cycle-dominated (slaking) or accumulates progressively (Miner-like) can be
read off the published cycle series. A soil that keeps losing stability at cycle 5 is not
slaking.

**3. Intersection.** Grid, OpenCitations, 2026-09-05:

| | Le Bissonnais 1996 (1,207) | Denef 2001 (604) | Amézketa 1999 (991) |
|---|---|---|---|
| **Miner 1945** (4,762) | **0** (E floor 962.9) | **0** (E 536.0) | **0** (E 820.3) |
| **Paris 1963** (5,461) | **0** (E 988.5) | **0** (E 543.8) | not run |
| **Meng & Ludema 1995** (767) | **0** (E 469.0) | not run | not run |
| *Archard 1953* (6,803) | **0** (E 1,025.1) | not run | not run |

Seven pairings, seven zeros. **Controls:** Miner × Paris = **257**; Denef × Le Bissonnais =
**38**. Control ratio on the shared-A form (Miner fixed, swap B from Le Bissonnais to Paris):
`(0/1,207)/(257/5,461)` = **∞**. On the shared-B form (Le Bissonnais fixed, swap A from Miner to
Denef): `(0/4,762)/(38/604)` = **∞**.

**Denominator.** Union floors only, 469–989. **But `|A|·|B| = 5.75×10⁶`,** so `E > 1` holds for
any `N` under ~6 million works — this zero does not depend on getting a scoped `N`, which is why
it ranks first. Sensitivity: at `N = 10⁶`, `E = 5.75`; at `N = 10⁷`, `E = 0.58` and the zero
becomes uninformative. A soil-science ∪ fatigue universe is not plausibly 10⁷.

**Mode 6 (diachronic drift).** Addressed structurally rather than by decade-binning the citer
sets: the mechanics anchors span **1945 / 1963 / 1995** and the soil anchors **1996 / 1999 /
2001**, so the grid samples both a 1940s-vocabulary and a 1990s-vocabulary version of the damage
side against a single soil decade. **Not addressed:** the soil side is entirely 1990s–2001. A
1960s soil-structure anchor (Emerson, Yoder) has not been tested and should be, before any note
is written.

**4. Inspection.** Nothing to inspect — every cell is 0.

**5. What would close it.** The missing object is **a Weibull/Miner damage curve for aggregate
stability against wet–dry cycle number, with its shape parameter placed on `C18`'s β axis** next
to the flow-battery β ≈ 1 and Li-ion β = 12.7 rows. The prediction that follows and that
discriminates against the slaking objection: aggregates stabilised by *organic* binding agents
should show progressive (β ≈ 1–2, Miner-like) loss, while aggregates held by physical
entrapment alone should show first-cycle-dominated (β ≫ 1) loss — so an organic-matter
amendment moves the **shape**, not only the mean. Computed from cycle-resolved stability series
already printed in Denef 2001 and the Amézketa 1999 review's compiled tables. **6–8 hours desk
work, no data access.** Trap: many wet–dry studies report only cycles 1 and *n*, which cannot
distinguish the two shapes; the fit needs ≥3 cycle points, and papers that give two must be
excluded and said to be excluded.

**6. Extends.** **`C18-durability-axis`** directly — a fourth population on the β axis, and the
first soil one after `C29`'s ecological recovery β. Also **`G12-latch-fatigue`**, which is the
same "nobody measured the second cycle" complaint in a different substrate.
`extends-to: sustainability` (soil structure under changing wet–dry frequency is a
climate-adaptation quantity).

---

### 2. Archard wear law ↔ soil detachment and erosion rate

**1. Anchors.** *A:* J. F. Archard, "Contact and Rubbing of Flat Surfaces", *J. Appl. Phys.*
24:981–988 (1953), DOI `10.1063/1.1721448` — Crossref verified, `is-referenced-by-count` = 7,175;
OC citer set **6,803**. Second A: Meng & Ludema 1995, `10.1016/0043-1648(95)90158-2`, OC **767**.
*B:* M. A. Nearing, G. R. Foster, L. J. Lane & S. C. Finkner, "A Process-Based Soil Erosion Model
for USDA-Water Erosion Prediction Project Technology", *Trans. ASAE* 32:1587–1593 (1989), DOI
`10.13031/2013.31195`, Crossref 1,142 / OC **1,122**. Second B: Le Bissonnais 1996 (erodibility
half), OC **1,207**. Control A: K. G. Renard *et al.*, "RUSLE: Revised universal soil loss
equation", *J. Soil Water Conserv.* 46:30–33 (1991), DOI `10.1080/00224561.1991.12456571`,
Crossref 680 / OC **603**.

**2. Same object, two sentences.** Both compute a **volume of solid removed per unit of
mechanical work done by a moving contact against a surface**, and both write it as a linear law
in an applied stress divided by a material resistance: Archard's `V = K·(F·s)/H` (wear volume =
wear coefficient × load × sliding distance / hardness) and WEPP's `D_c = K_r(τ − τ_c)` (detachment
capacity = rill erodibility × excess shear). `K` and `K_r` are the same kind of object — an
empirically fitted dimensional constant standing in for an unresolved contact mechanism — and
`H` and `τ_c` are both the material's threshold resistance.

**Strongest metaphor objection.** *The abrasive medium is the difference, and it is not a
detail.* Archard's law is derived for two solids in dry contact where the real area of contact
is set by plastic yielding at asperities; soil detachment by overland flow is a fluid shear
acting on a cohesive granular bed with no solid counterface, so `H` (indentation hardness) has
no counterpart and `K` cannot be interpreted the way tribology interprets it. The honest reply
is that the *comparison worth making is between `K` and `K_r` as fitted constants* — how many
orders of magnitude each spans across materials, and whether either has ever been predicted
rather than fitted — not a claim that the mechanisms are identical. Meng & Ludema 1995 exists
precisely because tribology's several hundred wear equations do not predict `K`; whether soil
erodibility has the same pathology is a checkable question, and nobody has asked it in these
terms.

**3. Intersection.** OpenCitations, 2026-09-05: Archard × Nearing = **0** (E floor 963.2);
Archard × Le Bissonnais = **0** (E 1,025.1); Meng & Ludema × Nearing = **0** (E 455.6); Meng &
Ludema × Le Bissonnais = **0** (E 469.0). Four pairings, four zeros.
**Controls:** RUSLE 1991 × Nearing 1989 = **60**; Meng & Ludema × Archard = **242**.
Control ratio, shared B (Nearing fixed, swap A from Archard to RUSLE): `(0/6,803)/(60/603)` =
**∞**. Shared A (Archard fixed, swap B from Nearing to Meng): `(0/1,122)/(242/767)` = **∞**.
**`|A|·|B| = 7.63×10⁶`** — the most denominator-robust zero in this scout.

**4. Inspection.** Nothing to inspect — all four cells are 0.

**5. What would close it.** The missing object is **`K` and `K_r` on one dimensionless axis**:
normalise Archard's wear coefficient and WEPP's rill erodibility to the same form (removed
volume per unit work per unit resisting stress) and tabulate the range each spans. The
prediction: both span 4–6 orders of magnitude and neither is predictable from bulk properties,
which would say the two fields have independently hit the *same* failure of a constitutive law —
the `Q4-healing-needs-a-new-law` pattern, in a third substrate. Computed from Archard's own
table plus Meng & Ludema's compilation, against WEPP's published `K_r` calibration ranges.
**5–7 hours desk, no data access.** Trap: unit reconciliation is where this dies — WEPP's `K_r`
is in s/m and Archard's `K` is dimensionless; the normalisation must be written out before any
number is quoted, or the comparison is a units artifact.

**6. Extends.** **`C6-damage-healing-ratio`** — soil has both a destruction rate (erosion) and a
formation rate (aggregation, weathering), so `Ha = k_r/k_d` is directly instantiable and the
soil-formation-rate literature (tolerable soil loss, `T` values) already publishes `k_r`. That
makes this the **only candidate in this scout that reaches an existing vault object with both
numerator and denominator already published.** Also `C18`. `extends-to: conservation`.

---

### 3. Reactor residence-time distribution ↔ soil organic carbon transit-time distribution

**1. Anchors.** *A:* P. V. Danckwerts, "Continuous flow systems: Distribution of residence
times", *Chem. Eng. Sci.* 2:1–13 (1953), DOI `10.1016/0009-2509(53)80001-1` — Crossref verified,
`is-referenced-by-count` = 2,456; OC citer set **2,463**.
*B:* C. A. Sierra, A. Ceballos-Núñez, S. E. Trumbore *et al.*, "The muddle of ages, turnover,
transit, and residence times in the carbon cycle", *Glob. Change Biol.* 23:1763–1773 (2016/2017),
DOI `10.1111/gcb.13556`, Crossref 139 / OC **156**. Second B: C. A. Sierra, M. Müller & S. E.
Trumbore, "Models of soil organic matter decomposition: the SoilR package", *Geosci. Model Dev.*
5:1045–1060 (2012), DOI `10.5194/gmd-5-1045-2012`, Crossref 129 / OC **161**.
*Mediator anchor:* P. Małoszewski & A. Zuber, "Determining the turnover time of groundwater
systems with the aid of environmental tracers", *J. Hydrol.* 57:207–231 (1982), DOI
`10.1016/0022-1694(82)90147-0`, Crossref 654 / OC **663**. Control B partner: S. E. Trumbore,
"Age of soil organic matter and soil respiration", *Ecol. Appl.* 10:399–411 (2000), DOI
`10.1890/1051-0761(2000)010[0399:aosoma]2.0.co;2`, Crossref 870 / OC **918**.

**2. Same object, two sentences.** Both fields define a probability density over the time a
tagged parcel spends between entering and leaving an open system, both distinguish the
*age* distribution of material currently inside from the *transit-time* distribution of material
leaving, and both compute the mean of the second as inventory divided by throughflow. Danckwerts
wrote that distinction down in 1953 for a chemical reactor; Sierra 2016 is an entire paper
untangling exactly that confusion for soil carbon, and it does not cite him.

**Strongest metaphor objection.** *Nonlinearity and non-stationarity.* Danckwerts' RTD algebra
assumes a steady, linear, conservative flow field; soil carbon decomposition is
microbially mediated, transformation-not-just-transport (carbon leaves as a different molecule),
and the pools are demonstrably non-steady under land-use and climate change. The reply is that
Sierra's own framework *is* the linear compartmental case — SoilR's transit-time machinery is
linear-system theory — so the objection bites the general claim and not the specific pairing;
but any note must say that the RTD identities transfer only in the linear autonomous regime, and
say which of Sierra's results already live there.

**3. Intersection.** OpenCitations, 2026-09-05:

| | Sierra 2016 (156) | SoilR 2012 (161) |
|---|---|---|
| **Danckwerts 1953** (2,463) | **0** (E floor 146.7) | **0** (E 151.1) |
| **Małoszewski & Zuber 1982** (663) | **0** (E 126.3) | **0** (E 129.5) |

**Controls, both directions.** Same A: Danckwerts × Małoszewski & Zuber = **21** (E floor 525.9,
O/E 0.0399) — *this is the pairing the brief said was probably bridged, and it is.* Same B:
Trumbore 2000 × Sierra 2016 = **21** (E 136.0, O/E 0.154).
Control ratio, shared A: `(0/156)/(21/663)` = **∞**. Shared B: `(0/2,463)/(21/918)` = **∞**.

**The mediator row is the finding.** Groundwater hydrology imported RTD theory (21 co-citers).
Soil carbon did not import it from chemical engineering **and did not import it from
groundwater hydrology either** — both routes are 0. The two literatures that quantify a transit
time in a porous medium a metre apart do not meet.

**Denominator.** Union floors 126–151 only; `|A|·|B| = 3.8×10⁵`, so `E > 1` requires
`N < 3.8×10⁵`. A biogeochemistry ∪ chemical-reaction-engineering universe is plausibly at or
above that, so **this candidate genuinely needs a scoped `N`** and does not have one. Stated as
a limit, not glossed.

**4. Inspection.** Nothing to inspect on the gap rows. The 21 control co-citers were not
individually read — that is an outstanding step, and until it is done the control is a count,
not a verified bridge.

**5. What would close it.** The missing object is **Danckwerts' F- and E-curve identities
written in soil-carbon variables, with the resulting closed-form relations checked against
SoilR's numerical transit times** — specifically whether the reactor-theory result that mean
transit time = inventory/throughflow holds under Sierra's non-autonomous case, and what the
variance of the transit-time distribution buys that the mean does not. A concrete number: the
RTD **variance-to-mean-squared ratio** is chemical engineering's standard mixing diagnostic
(σ²/τ² = 1 for perfect mixing, → 0 for plug flow), and soil carbon has never been placed on it.
Computed from transit-time densities SoilR already outputs for published site parameterisations.
**4–6 hours desk.** Trap: Sierra 2016's own vocabulary section may already cite a hydrology
review that cites Danckwerts, making the gap `mediated` rather than `disjoint` — read Sierra's
reference list in full (Crossref `message.reference`) before opening the note.

**6. Extends.** **`C31-remanufacturing-ha`** (`Ha = L/T` is a residence-time ratio) and
**`availability-formula`** (`MTBF/(MTBF+MTTR)` is a two-state residence-time partition).
`extends-to: circularity`.

---

### 4. Power-system state estimation ↔ water-network leak detection

**1. Anchors.** *A:* F. C. Schweppe *et al.*, "Power System Static-State Estimation, Part III:
Implementation", *IEEE Trans. Power App. Syst.* PAS-89:130–135 (1970), DOI
`10.1109/TPAS.1970.292680` — Crossref verified, 329; OC **323**.
Control A: A. Monticelli, "Electric power system state estimation", *Proc. IEEE* 88:262–282
(2000), DOI `10.1109/5.824004`, Crossref 599 / OC **590**.
*B:* R. Puust, Z. Kapelan, D. A. Savic & T. Koppel, "A review of methods for leakage management
in pipe networks", *Urban Water J.* 7:25–45 (2010), DOI `10.1080/15730621003610878`, Crossref
635 / OC **616**. Control B: A. F. Colombo & B. W. Karney, "Energy and Costs of Leaky Pipes",
*J. Water Resour. Plann. Manage.* 128:441–450 (2002), DOI
`10.1061/(asce)0733-9496(2002)128:6(441)`, Crossref 210 / OC **212**.

**2. Same object, two sentences.** Both estimate the state of a conserved flow on a metered
network from redundant, noisy sensor readings, and both locate an unmetered sink by testing
whether the measurement residuals are consistent with the conservation law — Kirchhoff's current
law in one case, continuity at nodes in the other. Power systems named the machinery (weighted
least squares, observability analysis, bad-data detection by the largest normalised residual, a
`χ²` test on the residual objective) in 1970 and has a 55-year literature on it; water-network
leak detection solves the same problem and its 2010 review does not cite it.

**Strongest metaphor objection.** *The physics is not linear the same way.* Power flow residuals
are algebraic in complex voltages with a well-conditioned Jacobian and near-real-time telemetry
at nearly every node; water networks are governed by a nonlinear head-loss law, are metered at
perhaps 1–5% of nodes, and demand itself is stochastic and unmeasured — so what power systems
calls "bad data" is, in a water network, the *signal* competing with a far larger unmodelled
demand variance. Observability, the concept that makes the power method work, may simply fail.
That objection is real, and the *right* form of the candidate is therefore narrower than "the
same method": it is **whether water-network sensor placement has ever been posed as an
observability problem in the power-systems sense**, which is a checkable literature question.

**3. Intersection.** OpenCitations, 2026-09-05: Schweppe 1970 × Puust 2010 = **0**, union floor
`N = 939`, **E = 211.9**.
**Controls:** Monticelli 2000 × Schweppe 1970 = **43** (E 219.0, O/E 0.196); Colombo & Karney
2002 × Puust 2010 = **50** (E 167.9, O/E 0.298).
Control ratio, shared A: `(0/616)/(43/590)` = **∞**. Shared B: `(0/323)/(50/212)` = **∞**.
Both sides' internal controls fire at comparable `E`, so neither anchor is obscure.

**Denominator.** `|A|·|B| = 1.99×10⁵`. `E > 1` only for `N < 1.99×10⁵` — a power-engineering ∪
water-resources universe is very plausibly larger. **This is the weakest denominator among the
zeros here and must be labelled as such.** Its strength is the two-sided control, not `E`.

**4. Inspection.** Nothing to inspect.

**5. What would close it.** The missing object is **the observability/redundancy number for a
water distribution network**: given a metering configuration, the rank of the measurement
Jacobian and the resulting minimum detectable leak, computed the way power systems computes
critical measurements and measurement redundancy. Prediction: real water networks sit far below
the observability threshold power systems requires, so the leak-detection problem is not
under-solved but *structurally unobservable* at current metering densities — and the actionable
output is a metering-density number, not a better algorithm. Computed on a published benchmark
network (Net3, or L-Town from the BattLeDIM leak-detection challenge; both open). **5–8 hours**,
and it needs a hydraulic solver, so it is the most tooling-dependent item here.

**6. Extends.** **`G29-early-warning-prognostics`** — the same "one field's detection theory,
another field's unimported problem" shape, and `G29` already owns the detection-threshold axis.
`extends-to: sustainability`.

---

### 5. Stretched-exponential (KWW) relaxation ↔ streamflow recession curves

**1. Anchors.** *A:* G. Williams & D. C. Watts, "Non-symmetrical dielectric relaxation behaviour
arising from a simple empirical decay function", *Trans. Faraday Soc.* 66:80–85 (1970), DOI
`10.1039/tf9706600080` — Crossref verified, 4,051; OC **3,998**.
*B:* W. Brutsaert & J. L. Nieber, "Regionalized drought flow hydrographs from a mature glaciated
plateau", *Water Resour. Res.* 13:637–643 (1977), DOI `10.1029/WR013i003p00637`, Crossref 626 /
OC **627**. Control B partner: J. W. Kirchner, X. Feng & C. Neal, "Fractal stream chemistry and
its implications for contaminant transport in catchments", *Nature* 403:524–527 (2000), DOI
`10.1038/35000537`, Crossref 857 / OC **857**.

**2. Same object, two sentences.** Both describe the discharge of a stored quantity from a medium
with a *distribution* of relaxation times rather than a single one, and both diagnose that
distribution from the shape of the decay rather than from its magnitude. Condensed matter fits
`φ(t) = exp[−(t/τ)^β]` and reads `β < 1` as evidence of a broad, correlated spectrum of
relaxation modes; hydrology fits `−dQ/dt = aQ^b` and reads `b ≠ 1` as evidence of nonlinear or
heterogeneous storage — and the two parameterisations are competing statements about the same
underlying spectrum.

**Strongest metaphor objection.** *`b` and `β` are not related by an identity, and pretending
they are is exactly the word-level failure this project keeps catching.* `−dQ/dt = aQ^b` is a
statement about the *storage–discharge* relation `Q(S)`, and it produces a power-law recession,
not a stretched exponential; a stretched exponential and a power law are different functions and
the hydrology literature already knows its recessions are often better fit by power laws. The
candidate therefore has to be posed at the level of the **underlying relaxation-time spectrum**,
where both are moment problems over the same density — and if that reduction cannot be written
in closed form, the candidate is a metaphor and should be dropped. **This is the candidate most
likely to die on contact, and it is ranked fifth for that reason.**

**3. Intersection.** OpenCitations, 2026-09-05: Williams–Watts 1970 × Brutsaert & Nieber 1977 =
**0**, union floor `N = 4,625`, **E = 542.0**.
**Control:** Brutsaert & Nieber 1977 × Kirchner 2000 = **19** (E 366.8, O/E 0.0518). Control
ratio, shared B: `(0/3,998)/(19/857)` = **∞**.
**Counter-check, and it matters:** Williams–Watts × Kirchner 2000 = **2** (E 706.0). So the KWW
side is isolated even from the *fractal-catchment* literature, which is the sub-literature most
likely to have imported it. That strengthens the zero and simultaneously suggests the reason —
hydrology's heterogeneity vocabulary is fractal/power-law, not stretched-exponential.
`|A|·|B| = 2.5×10⁶`, so `E > 1` up to `N ≈ 2.5×10⁶`.

**4. Inspection.** The two Williams–Watts × Kirchner co-citers were not enriched (budget); doing
so is the first step if this is opened.

**5. What would close it.** The missing object is **the relaxation-time density `ρ(τ)` implied by
a published recession-curve `(a, b)` pair, compared against the `ρ(τ)` implied by a KWW `β`** —
i.e. run both through the same inverse-Laplace moment representation and ask whether the two
spectra are the same family. Prediction, if they are: `b` and `β` are related by a single map,
and hydrology's `b ≈ 1.5` catchments correspond to a `β` that condensed matter would call
moderately stretched. Computed from published `(a, b)` values in the recession literature.
**6–10 hours**, and the first two are the ones that decide whether it lives.

**6. Extends.** **`C15-metastability-metric`** — the note that was killed by the prefactor is
exactly about separating a barrier from an attempt frequency, which is the same decomposition a
relaxation spectrum makes — and `C29-recovery-beta`'s decreasing-hazard result, which is a
stretched-exponential-shaped statement in survival language. `extends-to: ecology`.

---

### 6. Langmuir adsorption ↔ soil carbon saturation

**1. Anchors.** *A:* I. Langmuir, "The Adsorption of Gases on Plane Surfaces of Glass, Mica and
Platinum", *J. Am. Chem. Soc.* 40:1361–1403 (1918), DOI `10.1021/ja02242a004` — Crossref
verified, `is-referenced-by-count` = 20,719; OC **20,220**.
*B:* J. Hassink, "The capacity of soils to preserve organic C and N by their association with
clay and silt particles", *Plant Soil* 191:77–87 (1997), DOI `10.1023/A:1004213929699`, Crossref
1,204 / OC **1,170**. Second B: J. Six, R. T. Conant, E. A. Paul & K. Paustian, "Stabilization
mechanisms of soil organic matter", *Plant Soil* 241:155–176 (2002), DOI
`10.1023/A:1016125726789`, Crossref 4,054 / OC **3,853**. Control B: N. J. Barrow, "Reaction of
Anions and Cations with Variable-Charge Soils", *Adv. Agron.* 38:183–230 (1986), DOI
`10.1016/s0065-2113(08)60676-8`, Crossref 192 / OC **194**.

**2. Same object, two sentences.** Both describe a finite number of surface sites filling toward
an asymptote, with an equilibrium loading that rises hyperbolically in the bulk concentration and
saturates at a capacity set by the surface, not by the supply. Soil science calls the asymptote
the "carbon saturation deficit" and estimates it from a linear regression of C against clay+silt
content; Langmuir wrote the isotherm that has the asymptote *and* the affinity constant, and the
soil-carbon-saturation literature uses the first and never fits the second.

**Strongest metaphor objection.** *Mineral-associated organic matter is not monolayer adsorption
of a single sorbate.* Langmuir assumes identical non-interacting sites, one adsorbate, and
reversible equilibrium; soil organic matter is a heterogeneous mixture accumulating in
multi-layer and occluded configurations with irreversible and microbially mediated steps. A
fitted "Langmuir capacity" for soil C would be a lumped parameter with no site interpretation.
**This is not hypothetical — it is what the one real bridge found (below) actually argues.**

**3. Intersection.** OpenCitations, 2026-09-05: Langmuir × Hassink = **1** (union floor
`N = 21,389`, E = 1,106.1, O/E = 0.0009); Langmuir × Six 2002 = **2** (floor 24,071, E = 3,236.6,
O/E = 0.0006).
**Control:** Langmuir × Barrow 1986 = **6** (E 192.2, O/E 0.0312) — the soil-*sorption*
literature does cite Langmuir at 36–60× the rate the soil-*carbon-saturation* literature does.
Control ratio, shared A: Hassink `(1/1,170)/(6/194)` = **36×**; Six `(2/3,853)/(6/194)` = **60×**.
**Note on the floor:** Langmuir's 20,220-citer set is ~100× Barrow's, which is the re-anchoring
configuration `scout-00` flagged (the G25 shape). The union floor is therefore uninformative
here and the control ratio is the *only* usable statistic. Said plainly.

**4. Inspection — all three hits read.**
- `10.1007/s10533-021-00759-x`, *Biogeochemistry* 2021, **"How much carbon can be added to soil
  by sorption?"** — **this is a real bridge and it is the paper this candidate is about.** It
  poses soil C accrual as a sorption problem explicitly. The candidate must therefore be opened
  as `narrowed` with `contact-surface: 1`, not as a clean gap, and this paper must be read in
  full before anything is claimed.
- `10.1016/j.still.2023.105840`, *Soil Till. Res.* 2023 — **phosphorus** adsorption–desorption,
  not carbon. Off-object.
- `10.1016/j.agsy.2005.08.011`, *Agric. Syst.* 2007 — West African SOC management review,
  co-cites both as background. Not a bridge.

**So: one bridge, one off-object hit, one background co-citation.** That is the honest count.

**5. What would close it.** The missing object is **a two-parameter Langmuir fit (capacity
`q_max` *and* affinity `K`) to published soil C-vs-clay saturation datasets, where the literature
currently fits only a one-parameter ceiling** — and the prediction that `K`, not `q_max`,
is what distinguishes mineralogies, so two soils with the same saturation capacity approach it at
different rates and therefore respond differently to the same carbon input. **3–5 hours desk**
from Hassink 1997's and Six 2002's compiled datasets. **Do the Biogeochemistry 2021 read first**;
if it already fits `K`, the candidate is closed and should be recorded as closed.

**6. Extends.** **`C31-remanufacturing-ha`**'s ceiling structure (`A_circ ≤ r` — a hard asymptote
that no rate improvement can exceed) is the same shape as a saturation capacity.
`extends-to: circularity`.

---

### 7. CUSUM / change-point detection ↔ leak detection in water networks

**1. Anchors.** *A:* E. S. Page, "Continuous Inspection Schemes", *Biometrika* 41:100–115 (1954),
DOI `10.1093/biomet/41.1-2.100` — Crossref verified, 3,029; OC **2,915**. (The JSTOR duplicate
`10.2307/2333009` is a distinct DOI carrying 1,500 — do not pool them without saying so.)
*B:* Puust 2010, `10.1080/15730621003610878`, OC **616**.

**2. Same object.** Both detect the earliest sample at which a monitored stream's mean has
shifted, subject to a fixed false-alarm rate, and both trade detection delay against that rate.
Water networks call it minimum-night-flow analysis and burst detection.

**Metaphor objection.** Weak, and that is the problem — the objects really are the same, which
means the more likely explanation for a low count is that the water field re-derived it, not that
it is unaware of it. A clean `0` here would have been suspicious.

**3. Intersection.** Page × Puust = **1**, union floor `N = 3,530`, **E = 508.7**, O/E = 0.0020.
Control: Colombo & Karney × Puust = **50**. Control ratio, shared B: `(1/2,915)/(50/212)` =
**687×**. `|A|·|B| = 1.8×10⁶`.

**4. Inspection — the single hit read.** `10.1061/jwrmd5.wreng-6969`, *J. Water Resour. Plann.
Manage.* **2025**, "Addressing Practical Challenges of Stochastic Process Control for Leakage
Detection in Water Distribution Networks". **A genuine bridge, and it is one year old.** So this
gap is closing in real time, under the name *statistical process control* rather than CUSUM.
That is a mode-4 synonym warning for anyone re-running it, and it caps the candidate: the honest
description is `narrowed`, `contact-surface: 1`, with a note that the bridge post-dates the
review anchor by 15 years.

**5. What would close it.** The missing object is the **average-run-length curve for a water
network** — false-alarm rate against minimum detectable leak size, in litres per hour — which
SPC has computed since 1954 and which the water literature reports only as case-study hit rates.
**4 hours desk** on the BattLeDIM benchmark.

**6. Extends.** `G29-early-warning-prognostics`. `extends-to: sustainability`.

---

### 8. RTD moment analysis ↔ pharmacokinetic statistical moments

**1. Anchors.** Danckwerts 1953 (OC **2,463**) ↔ K. Yamaoka, T. Nakagawa & T. Uno, "Statistical
moments in pharmacokinetics", *J. Pharmacokinet. Biopharm.* 6:547–558 (1978), DOI
`10.1007/BF01062109` — Crossref verified, 1,044; OC **1,301**.

**2. Same object.** Mean residence time as the first normalised moment of an exit-time density,
and the variance as the second — identical algebra, identical interpretation (`MRT = AUMC/AUC`
is `τ = ∫t·E(t)dt`), different symbols.

**Metaphor objection.** The body is not a reactor with a single well-defined exit; MRT in
pharmacokinetics is defined on a plasma-concentration curve that mixes distribution and
elimination, so the "system" whose residence time is measured is not the one the dose entered.
That is a real difference in what the density is *over*, and it must be resolved before the
identity is asserted.

**3. Intersection.** Danckwerts × Yamaoka = **1**, union floor 3,763, **E = 851.5**, O/E = 0.0012.
Second measurement: Małoszewski & Zuber × Yamaoka = **0** (E 439.2). Control, shared A:
Danckwerts × Małoszewski & Zuber = 21/663 → control ratio `(1/1,301)/(21/663)` = **41×**.

**4. Inspection.** The single hit is `10.1023/a:1012206330281`, *J. Pharmacokinet. Pharmacodyn.*
2001, a hepatobiliary diffusion model — a real but narrow bridge, internal to pharmacokinetics.

**5–6.** Ranked eighth despite a clean number because it is only marginally in this scout's
domain. It earns its place as the **third leg of the RTD triangle** — chemical engineering
exported RTD to hydrology (21) and to nobody else — which is what makes candidate 3's zero
interpretable rather than accidental. Extends `C31`. `extends-to: circularity`.

## Checked and rejected

- **Danckwerts RTD ↔ groundwater transit time (Małoszewski & Zuber 1982) — 21 co-citers.**
  Bridged, as the brief predicted. Repurposed as this scout's in-domain positive control. **Do
  not reopen.**
- **Danckwerts RTD ↔ catchment transit time (Kirchner 2000) — 13 co-citers** (E floor 638.3).
  Same story one field over. Bridged.
- **Danckwerts RTD ↔ anaerobic digestion kinetics (ADM1, Batstone 2002) — 3 co-citers, all three
  inspected and all three genuine**: *Bioresour. Technol.* 2012 (two-phase grass digester
  design), *J. Environ. Chem. Eng.* 2020 (Aspen Plus AD model), and decisively *Crit. Rev.
  Environ. Sci. Technol.* 2015, **"Current Views on Hydrodynamic Models of Nonideal Flow
  Anaerobic Reactors"** — a review of exactly this transfer. Bridged.
- **Monod chemostat kinetics ↔ ADM1 — 42 co-citers.** Bridged, unsurprisingly; ADM1's growth
  terms are Monod. Reject.
- **Urban metabolism ↔ ecological network analysis / ascendency — 8 co-citers, all eight
  inspected and all eight on-object**: *Ecol. Modell.* 2012 "Cities as ecosystems", *J. Ind.
  Ecol.* 2020 "Ecological network analysis of urban–industrial ecosystems", *J. Ind. Ecol.* 2023
  (virtual-water ENA, Quito), *Water* 2021 (ENA of urban water pollution metabolism, Fuzhou),
  *J. Clean. Prod.* 2019, *Sci. Total Environ.* 2019, *Procedia CIRP* 2018, *Energy Sustain.
  Dev.* 2026. **This is a real, active, joined literature**, and Bettencourt 2007 × Kennedy 2007
  = **110** confirms the urban side is well connected. Reject as a gap. (Ulanowicz 2004 × Zhang
  2011 = 0, but Zhang 2011 is an *emergy* paper, not an ENA paper — that pairing was
  mis-specified and is reported here only so it is not mistaken for evidence.)
- **Washburn capillary imbibition ↔ Philip/Green-Ampt infiltration — 8 co-citers, all inspected,
  and the inspection is what kills it.** Seven are porous-building-materials sorptivity papers
  (*Transport in Porous Media* 2020 on quarry limestones, *Materials and Structures* 2017 on
  sorptivity temperature dependence, *J. Appl. Phys.* 2009 fibrous sheets, *J. Colloid Interface
  Sci.* 2009, JSCE 2021, SAE 2008) and **one is `10.1201/b12840-15`, the back-matter
  bibliography of *Water Transport in Brick, Stone and Concrete*** — the identical artifact
  `G27` was caught by. Exactly one hit is soil science (*Eur. J. Soil Sci.* 2013). The
  Washburn-side control ratio is only **1.8×** (Washburn × Richards = 72, O/E 0.0274). Verdict:
  **the two capillary literatures meet, through construction-materials sorptivity, and soil
  science is the member of the trio that is out of the room.** That is a narrower and less
  interesting claim than the one proposed, and it is `topology: mediated` with the mediator
  named. Not recommended.
- **Percolation-theory permeability (Katz & Thompson 1986) ↔ Philip/Richards infiltration — 3
  and 7 co-citers, inspected.** Six of seven on the Richards pairing are cement/concrete/ceramics
  (*Cem. Concr. Res.* 2014, *J. Am. Ceram. Soc.* 2021, *J. Mater. Civ. Eng.* 2019, *Mater.
  Struct.* 2025, *Rev. Geophys.* 2023), one is the same `b12840-15` bibliography, one is a 2026
  permeable-pavement paper. So COCI sees no soil bridge — **but Hunt & Ewing, *Percolation
  Theory for Flow in Porous Media* (Springer 2014, `10.1007/978-3-319-03771-4`) is a book-length
  treatment of exactly this transfer, and a monograph is largely invisible to DOI-to-DOI
  citation indexing.** Prior art is near-certain. Reject on prior art, not on count — and log
  this as the scout's clearest reminder that a COCI zero does not see books.
- **Stormwater detention routing ↔ Moran dam-storage theory — not tested.** Moran's 1954 *Aust.
  J. Appl. Sci.* paper has no DOI, so no DOI-keyed provider can see it; per `citation-sources`
  this needs an OpenAlex `fulltext.search:` pass, which the budget lock forbade. Recorded as
  **untested**, not as a zero.

## Recommendation: which two to open first

**Open #1 (fatigue ↔ soil aggregate wet–dry breakdown) and #2 (Archard wear ↔ soil erosion).**
They should be opened as a pair, because they are the same claim about the same soil at two
length scales and they share their controls.

Three reasons, in order of weight.

1. **They are the only candidates whose zero survives an honest denominator.** `|A|·|B|` is
   5.75×10⁶ and 7.63×10⁶, so `E > 1` for any `N` short of ~6–8 million works. Every other zero in
   this scout — including candidate 3, which is otherwise more elegant — needs a concept-scoped
   `N` below 10⁵–10⁶ that this session could not fetch and that `scout-01` also failed to fetch.
   `citation-intersection`'s own G6 worked example is the warning: a spectacular floor-`E` zero
   that means nothing at field scale. These two do not have that exposure.
2. **The zero is a seven-cell grid, not a single pairing, and it is decade-spread on the
   mechanics side** (1945 Miner, 1953 Archard, 1963 Paris, 1995 Meng & Ludema) against three
   independent soil anchors — with four internal controls firing at 38, 60, 242 and 257. That is
   the multi-anchor, multi-decade shape `failure-modes` mode 6 demands, and no other candidate
   here has it.
3. **#2 reaches an existing vault object with both of its numbers already published.**
   `C6-damage-healing-ratio`'s `Ha = k_r/k_d` has two empty rows because the data do not exist;
   soil has a destruction rate (erosion, measured in every erosion study) *and* a formation rate
   (soil formation / tolerable-loss `T` values, tabulated by USDA), so `Ha` for soil can be
   computed this week. A candidate that fills an admitted blank in an existing computed note is
   worth more than a candidate that opens a new one.

**What would make me drop them.** For #1, if the published wet–dry-cycle series turn out to be
two-point (cycle 1 and cycle *n*) across the board, the damage law is unfittable and the
candidate is dead on data availability rather than on argument — check that *first*, in the
Amézketa 1999 review's compiled tables, before spending the 6–8 hours. For #2, if `K` and `K_r`
cannot be reduced to a common dimensionless form in under an hour of algebra, the comparison is a
units artifact and should be abandoned.

**Third in line is #3 (RTD ↔ soil carbon transit time)**, and it is the most intellectually
satisfying result in this scout — the double zero through the hydrology mediator is a genuinely
surprising structural fact. It is ranked below the first two only on the denominator, and it
should be promoted the moment an OpenAlex concept-scoped `N` can be fetched. **The banked
OpenAlex probe should be spent on exactly that**: a union count over the biogeochemistry and
chemical-reaction-engineering concepts from 1953, to see whether it lands under 3.8×10⁵.

## Outstanding, stated as debts

- **No concept-scoped `N_universe` was obtained for any candidate.** Every `E` here is a union
  floor and is labelled one. Candidates 3 and 4 are not quotable as `O/E` until that changes.
- **Positive-control co-citers were counted, not read.** The 6, 19, 21, 38, 43, 50, 60, 110, 232,
  242 and 257 are counts; `citation-intersection`'s own G17 specimen says a citation is not a
  follow-up. Controls are being used here only to establish that the anchors are *findable*,
  which is what a control is for, but no control should be quoted as a bridge without inspection.
- **Mode 6 is only half-addressed on candidate 1**: the mechanics side spans 1945–1995, the soil
  side is 1996–2001 only. A pre-1980 soil-structure anchor is needed.
- **The COCI blind spot is now demonstrated twice in one scout** (Hunt & Ewing 2014; the
  `b12840-15` bibliography hit appearing in two different intersections). A monograph-shaped
  bridge is invisible to this instrument, and a note resting on a COCI zero should say so.
- **Crossref and OpenCitations agreed within a few percent on every anchor** (e.g. Danckwerts
  2,456 vs 2,463; Le Bissonnais 1,225 vs 1,207; Puust 635 vs 616), which is the two-source check
  `citation-sources` asks for. The one gap-relevant divergence is Yamaoka 1978 (Crossref 1,044,
  OC 1,301) and it is noted rather than reconciled.
