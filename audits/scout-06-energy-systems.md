# Scout: energy systems

Domain: grid reliability, renewable intermittency and storage, demand response, EROI, exergy,
thermal storage cycling, grid inertia, microgrid islanding, capacity factor, curtailment —
against the biology/ecology objects that may be the same thing.

**Provenance.** Every DOI below was resolved live through Crossref
(`api.crossref.org/works/<doi>?mailto=deciduusleaf@gmail.com`) on **2026-09-05**; the
`cited_by` figures quoted in the anchor tables are Crossref `is-referenced-by-count`, same
fetch. Every intersection was run on **OpenCitations**, endpoint
`https://api.opencitations.net/index/v1/citations/<doi>`, via `vault/_scripts/intersect.py`,
on **2026-09-05**. `N_A`/`N_B` are OpenCitations citer-set sizes on that endpoint and date and
are *not* the same object as the Crossref counts — they differ by 5–20% throughout, as
`citation-sources.md` predicts.

**OpenAlex probe: spent and lost.** One probe was permitted. It resolved both anchors of
candidate #1 (Bird 2016 = `W2503976405`, OpenAlex `cited_by_count` 647; Müller 2001 =
`W1992244454`, `cited_by_count` 2839) and then returned **HTTP 429** on the
`filter=cites:W2503976405,cites:W1992244454` call. The probe is not retried. Every number in
this report is therefore **single-provider (OpenCitations)**, which is one instrument short of
the project's own two-sources-agreeing standard. Rerun the OpenAlex leg on candidates #1 and #2
before either is opened as a vault note.

**`N_universe` is a union floor throughout**, stated as a floor: `N = N_A + N_B − O`. Per
`citation-intersection.md` the floor gives the largest `E` and so the smallest `O/E`, and it
flatters every gap claim here.

---

## Summary

1. **The domain is metaphor-saturated and the citation graph is clean anyway.** Fifteen
   cross-domain pairs were tested. Thirteen returned **exactly zero** co-citers; two returned
   two. Three same-side positive controls returned 25, 27 and 441. The zeros are real zeros,
   not coverage artifacts — the same provider, the same day, found hundreds of co-citers when
   asked about pairs that *are* joined.
2. **But a clean zero is worth almost nothing in this domain, and that is the scout's main
   finding.** "EROI is foraging", "storage sizing is fat reserves", "demand response is
   torpor" are all zero-co-citation *and* all fail the units test at first contact. EROI is
   dimensionless (E_out/E_in); optimal foraging's currency is a **rate** (E/time). Kleiber is a
   **power law in mass**. Three different quantities. The candidates ranked highest below are
   the ones where the same quantity with the same units actually appears on both sides — and
   there are only about four of them.
3. **The strongest candidate is the one nobody would guess: loss-of-load probability against
   starvation-risk first-passage models.** Both sides compute *the probability that a stored
   reserve reaches zero within a horizon under stochastic income and stochastic draw*, both
   report it as a dimensionless probability per season/year, and both solve it by the same
   machinery (stochastic dynamic programming / convolution of a reserve process). ∩ = 0 across
   2,058 × 422 citers. This is the only candidate where the two sides share the estimand, the
   units and the solution method.
4. **The most surprising negative is inside biology.** Insect diapause energetics × mammalian
   torpor (Hahn & Denlinger 2011 × Geiser 2004) returned **∩ = 2 of 723 × 1,006**. Biology is
   not internally joined on "seasonal metabolic depression" either. Any candidate that assumes
   "biology already knows this" needs that assumption checked, not granted.
5. **EROI ↔ biology is already half-bridged, by one person.** Murphy & Hall 2010 × Hall's own
   1972 stream-metabolism paper returns ∩ = 14 — but the hits are dominated by Hall-lineage
   energy-economics work (Murphy 2014 `10.1098/rsta.2013.0126`, Fizaine & Court 2015
   `10.1016/j.ecolecon.2014.12.001`). EROI *was invented out of fish energetics by Charles
   Hall*, and its biological ancestry is cited inside energy economics and essentially nowhere
   in ecology. That makes EROI ↔ foraging a **one-way-borrowing description**, in the
   `G3-cycle-life` sense — not a gap. It is listed below as a rejection, and it is the single
   most important adversarial result in this scout.

---

## Calibration

Same provider, same endpoint, same day.

| Control | Kind | `N_A` | `N_B` | ∩ | ∩ as % of smaller set |
|---|---|---|---|---|---|
| Motter & Lai 2002 × Buldyrev 2010 | in-domain (network cascade) | 1,478 | 3,741 | **441** | 29.8% |
| Denholm & Hand 2011 × Bird 2016 | **in-domain positive control (energy systems)** | 794 | 555 | **27** | 4.9% |
| McNamara & Houston 1987 × Houston & McNamara 1993 | in-domain (behavioural ecology) | 422 | 196 | **25** | 12.8% |
| Murphy & Hall 2010 × Hall 1972 | cross-domain but **known bridged** | 384 | 188 | **14** | 7.4% |

Against those, every cross-domain candidate below sits at 0 or 2 — i.e. 0.0–0.3% of the
smaller set. **Note the floor's limitation honestly:** at the union floor `E` is inflated
enough that even the controls give `O/E` of 0.08–0.38, so `O/E` does not separate joined from
disjoint here. What separates them is raw `O` and ∩-as-%-of-smaller-set: 4.9–29.8% for joined
literatures, 0.0–0.3% for these candidates. Quote that ratio, not `O/E`.

---

## Ranked candidates

| # | Candidate (A ↔ B) | `N_A` | `N_B` | ∩ | `N` floor | `E` (floor) | Units test | Extends | Cost | Recommend |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Loss-of-load probability (Billinton & Allan 1996) ↔ starvation-risk first passage (McNamara & Houston 1987) | 2,058 | 422 | **0** | 2,480 | 350.2 | **PASSES** — dimensionless P(reserve→0 \| horizon) both sides | C1, G3 | 8–12 h | **open first** |
| 2 | Curtailment fraction (Bird 2016) ↔ non-photochemical quenching (Müller 2001) | 555 | 2,467 | **0** | 3,022 | 453.0 | **PASSES** — dimensionless dumped fraction of incident input, both sides | C1, C14 | 10–14 h | **open second** |
| 3 | Storage sizing for a reliability target (Denholm & Hand 2011) ↔ optimal fat reserves (Houston & McNamara 1993) | 794 | 196 | **0** | 990 | 157.2 | **PASSES** — energy-store size chosen to hit a survival probability | C1, G3 | 8–10 h | open next |
| 4 | Demand response / load shedding (Palensky & Dietrich 2011) ↔ torpor and metabolic depression (Geiser 2004) | 2,415 | 1,006 | **0** | 3,421 | 710.1 | **partial** — both have a depression depth *and* a rebound/arousal cost; the ratio is the shared object | C14, M3 | 12–16 h | open next |
| 5 | Thermal-storage seasonal cycling (Denholm & Hand 2011) ↔ diapause energetics (Hahn & Denlinger 2011) | 794 | 723 | **0** | 1,517 | 378.4 | **partial** — self-discharge rate vs metabolic drawdown, same units (fraction/day) | G3 | 10–14 h | hold |
| 6 | Microgrid islanding / cascade arrest (Motter & Lai 2002) ↔ food-web compartmentalisation (Stouffer & Bascompte 2011) | 1,478 | 636 | **2** | 2,112 | 445.0 | **partial**, mediator risk high | new | 8 h | hold |
| 7 | Curtailment (Bird 2016) ↔ photoinhibition in nature (Long 1994) | 555 | 1,262 | **0** | 1,817 | 385.5 | duplicate of #2, weaker anchor | C1 | — | fold into #2 |
| 8 | Storage sizing (Denholm & Hand 2011) ↔ bet-hedging in a random environment (Cohen 1966) | 794 | 1,135 | **0** | 1,929 | 467.2 | **partial** — geometric-mean objective vs expected-cost objective are not the same functional | — | 12 h | hold |
| 9 | Curtailment (Bird 2016) ↔ bet-hedging revisited (Philippi & Seger 1989) | 555 | 745 | **0** | 1,300 | 318.1 | **fails** — no shared quantity | — | — | reject |
| 10 | Demand response (Palensky 2011) ↔ starvation/predation (McNamara & Houston 1987) | 2,415 | 422 | **0** | 2,837 | 359.2 | subsumed by #1 and #4 | C1 | — | fold |
| 11 | Grid inertia / low-inertia systems (Milano 2018) ↔ allostatic load (McEwen 1998) | 751 | 5,278 | **0** | 6,029 | 657.4 | **fails** — "buffering" is a word, not a quantity | — | — | reject |
| 12 | Grid frequency regulation (Milano 2018) ↔ heart rate variability (Task Force 1996) | 751 | 12,122 | **0** | 12,873 | 707.3 | **fails** — both are spectra of a rate; the *estimand* differs (control error vs autonomic tone) | — | — | reject |
| 13 | EROI (Murphy & Hall 2010) ↔ marginal value theorem (Charnov 1976) | 384 | 4,088 | **0** | 4,472 | 351.0 | **fails on units** (ratio vs rate) *and* is one-way bridged upstream | — | — | reject, see §5 |
| 14 | EROI (Murphy & Hall 2010) ↔ metabolic scaling (West 1997) | 384 | 4,132 | **0** | 4,516 | 351.4 | **fails** — power law in mass, not a return ratio | — | — | reject |
| 15 | Diapause (Hahn & Denlinger 2011) ↔ torpor (Geiser 2004) | 723 | 1,006 | **2** | 1,727 | 421.1 | **bio–bio control, near-zero** | — | — | finding, not candidate |

---

## Per-candidate detail

### 1. Loss-of-load probability ↔ starvation-risk first passage — **open first**

- **A.** Billinton & Allan, *Reliability Evaluation of Power Systems* (Springer, 1996),
  `10.1007/978-1-4899-1860-4`. Crossref `is-referenced-by-count` 2,095, fetched 2026-09-05.
  OpenCitations `N_A` = 2,058.
- **B.** McNamara & Houston, "Starvation and Predation as Factors Limiting Population Size",
  *Ecology* 68 (1987), `10.2307/1939235`. Crossref count 407. OpenCitations `N_B` = 422.
- **Intersection.** ∩ = **0**. OpenCitations `/index/v1/citations/`, 2026-09-05.
  `N` floor = 2,480; `E` = 350.2 at the floor; `O/E` = 0. Nothing to inspect.
- **Same-object argument.** Both sides define a *reserve* `x(t)` driven by a stochastic income
  process and a stochastic draw, and both compute the probability that `x` hits an absorbing
  boundary at zero within a horizon. Grid side: LOLP / LOLE, "probability that available
  generation is insufficient to meet demand", solved by convolving a capacity-outage
  probability table against a load-duration curve. Ecology side: probability an overwintering
  bird's fat reserve hits zero before dawn / before spring, solved by backward stochastic
  dynamic programming on the reserve state. **Same estimand, same state variable, same
  absorbing boundary, both dimensionless.** Both fields also carry the *same second quantity*:
  a shadow price of reserve (grid: value of lost load, £/MWh unserved; ecology: marginal
  fitness value of a unit of fat), and both obtain it as the derivative of the value function.
  That is two quantities matching, not one.
- **Metaphor-risk objection, stated at full strength.** The grid problem is stationary and
  the reserve is *generation capacity*, which is not a stock — LOLP in its classic form
  convolves capacity outages, with no integrated state at all. The bird problem is
  intrinsically a stock problem. If the comparison is to LOLP-of-a-thermal-fleet, the objection
  lands and the candidate dies. **The comparison must be to storage-constrained
  LOLP** — LOLE computed on a system whose adequacy depends on a state-of-charge trajectory,
  which is the modern VRE-plus-storage formulation and is exactly a first-passage problem.
  Scope the candidate that way or not at all.
- **What closes it.** Object: the value function `V(x,t)` and the resulting hitting
  probability. Numbers: (i) take one published storage-adequacy study's LOLE and re-derive it
  as a first-passage probability of the state-of-charge process; (ii) take Houston & McNamara's
  published optimal-reserve trajectory and re-express it as a "reserve margin" in the grid's
  own units (hours of autonomy at mean draw); (iii) check whether the two optimal-reserve
  rules have the same shape in the same non-dimensional group (reserve / (mean draw × recharge
  interval)). If the two optimal policies collapse onto one curve in that group, the gap is
  real and closed in the same motion. **8–12 h.**
- **Vault instrument extended.** `C1-availability-living-tissue` — `A = MTBF/(MTBF+MTTR)` is
  the *stationary* version of exactly this; LOLP is `1 − A` with a horizon attached, and the
  candidate supplies C1's missing non-stationary form. Also feeds `G3-cycle-life` via the
  reserve-cycling leg. `extends-to: [[C1-availability-living-tissue]]`.

### 2. Curtailment fraction ↔ non-photochemical quenching — **open second**

- **A.** Bird, Lew, Milligan et al., "Wind and solar energy curtailment: A review of
  international experience", *Renew. Sustain. Energy Rev.* 65 (2016),
  `10.1016/j.rser.2016.06.082`. Crossref count 611. OpenCitations `N_A` = 555.
  (OpenAlex `W2503976405`, `cited_by_count` 647, 2026-09-05.)
- **B.** Müller, Li & Niyogi, "Non-Photochemical Quenching. A Response to Excess Light
  Energy", *Plant Physiology* 125 (2001), `10.1104/pp.125.4.1558`. Crossref count 2,400.
  OpenCitations `N_B` = 2,467. (OpenAlex `W1992244454`, `cited_by_count` 2,839.)
- **Intersection.** ∩ = **0**. `N` floor = 3,022; `E` = 453.0; `O/E` = 0.
  Cross-check at the same anchors against Long 1994 photoinhibition (`10.1146/annurev.pp.45.060194.003221`,
  `N_B` = 1,262): ∩ = **0** as well. Two independent B-side anchors, same zero.
- **Same-object argument.** Both quantify **the fraction of incident energy deliberately
  dissipated because the downstream sink cannot accept it, in order to avoid damage or
  instability.** Grid: curtailment rate = curtailed MWh / available MWh, reported per year per
  region, with the driver named as transmission congestion or minimum-generation/inertia
  limits. Photosynthesis: NPQ dissipates absorbed photons as heat when electron transport
  saturates; the field's `qN`/NPQ parameter is likewise a fraction of absorbed excitation
  routed to heat rather than to the sink. **Both are dimensionless dump fractions of an
  uncontrollable input against a rate-limited sink, and both have the same three-way budget:
  used / stored / dumped.** Both fields also have the same failure mode when the dump
  mechanism is too slow — photoinhibition (D1 damage) and over-voltage/over-frequency trips —
  and both quantify the recovery time constant of the protective state.
- **Metaphor-risk objection.** NPQ is regulated at the *photosystem* on a seconds-to-minutes
  timescale by a pH-gradient-gated conformational switch; curtailment is an economic dispatch
  decision on a five-minute-to-hour market. The obvious objection is that "safely dumping
  excess" is a functional description that fits a car's brakes too, and functional descriptions
  are exactly what `failure-modes.md` §4 warns about. **The defence must be numeric, not
  functional:** if the two dump fractions do not obey the same saturation relation against
  the sink-limited fraction of input (`dumped ≈ max(0, 1 − sink_capacity/input)` plus a
  hysteresis term), the candidate is a metaphor and should be recorded as one.
- **What closes it.** Object: the dump fraction as a function of (input / sink capacity).
  Numbers: (i) take a published regional curtailment curve versus VRE penetration; (ii) take a
  published NPQ light-response curve versus PPFD relative to the light-saturation point;
  (iii) non-dimensionalise both on `input/sink_capacity` and test whether the two curves
  superpose, and whether the hysteresis (curtailment's must-run floor; NPQ's slow qI
  component) enters with the same sign. **10–14 h.**
- **Vault instrument extended.** `C14-degree-of-passivity`'s `P = W_passive/W_total` is a
  cycle-averaged energy-delivery fraction; the dump fraction is its complement on the *input*
  side, and it is defined without needing C14's axis-2 signal question. Also touches
  `C1-availability-living-tissue`, which already computes a PSII functional fraction (0.883)
  and would gain the input-side companion number. `extends-to: [[C14-degree-of-passivity]]`.

### 3. Storage sizing to a reliability target ↔ optimal fat reserves — open next

- **A.** Denholm & Hand, "Grid flexibility and storage required to achieve very high
  penetration of variable renewable electricity", *Energy Policy* 39 (2011),
  `10.1016/j.enpol.2011.01.019`. Crossref count 828. OpenCitations `N_A` = 794.
- **B.** Houston & McNamara, "A Theoretical Investigation of the Fat Reserves and Mortality
  Levels of Small Birds in Winter", *Ornis Scandinavica* 24 (1993), `10.2307/3676736`.
  Crossref count 195. OpenCitations `N_B` = 196.
- **Intersection.** ∩ = **0**. `N` floor = 990; `E` = 157.2; `O/E` = 0.
- **Same-object argument.** Both choose the size of an energy store to trade a **carrying
  cost** against a **ruin probability**. Grid: MWh of storage per MW of peak load, chosen so
  LOLE meets a standard, against capital cost. Bird: grams of fat, chosen so overnight
  starvation risk is acceptable, against mass-dependent predation risk and foraging cost. Both
  produce the same qualitative signature — an interior optimum, and a store size that scales
  with the *variance* of the income process, not its mean.
- **Metaphor-risk objection.** The costs are not the same kind of object. The bird's carrying
  cost is a mortality hazard (dimension 1/time); the grid's is capital (currency). The
  optimisation problems are only isomorphic after both are pushed through a value function
  with a common numeraire, and choosing that numeraire is where a metaphor can hide. This
  candidate is strictly weaker than #1 for that reason and should be opened *after* #1
  establishes the shared value function.
- **What closes it.** Object: `d(store)/d(σ_income)`. Numbers: published storage-vs-penetration
  curves versus published reserve-vs-winter-severity curves, both non-dimensionalised on
  (store / mean daily draw). **8–10 h.** `extends-to: [[C1-availability-living-tissue]]`.

### 4. Demand response ↔ torpor and metabolic depression — open next

- **A.** Palensky & Dietrich, "Demand Side Management: Demand Response, Intelligent Energy
  Systems, and Smart Loads", *IEEE Trans. Ind. Informatics* 7 (2011), `10.1109/TII.2011.2158841`.
  Crossref count 2,469. OpenCitations `N_A` = 2,415.
- **B.** Geiser, "Metabolic Rate and Body Temperature Reduction During Hibernation and Daily
  Torpor", *Annu. Rev. Physiol.* 66 (2004), `10.1146/annurev.physiol.66.032102.115105`.
  Crossref count 999. OpenCitations `N_B` = 1,006. (Note: the commonly cited DOI
  `…150716` is a **404** at Crossref; `…115105` is the live one. Recorded here so the next
  scout does not repeat the miss.)
- **Intersection.** ∩ = **0**. `N` floor = 3,421; `E` = 710.1. A second cut against
  McNamara & Houston 1987 also gave ∩ = 0 (2,415 × 422).
- **Same-object argument.** The shared quantity is not "turning down" — it is the **payback
  ratio**: energy saved during depression divided by the energy cost of returning to normal
  operation. Grid: DR "rebound" or "payback" peak after a load-shed event, and the net energy
  saved is famously a small fraction of the shed energy. Torpor: metabolic saving during the
  bout divided by the cost of arousal (rewarming), which is the field's own central accounting
  and is why bout length has an optimum. Both fields report a saving fraction, a payback
  fraction, and an optimal event duration set by their ratio. Those three numbers are the same
  three numbers.
- **Metaphor-risk objection.** "Load shedding = torpor" as a phrase is pure metaphor and
  should be refused. The candidate survives only if the payback-ratio framing is really how
  both fields compute it — which needs a full-text check on the DR side, since much of that
  literature reports peak-kW reduction and never closes the energy balance at all. If the
  energy balance is not closed on the grid side, there is no shared quantity and this drops
  to reject.
- **What closes it.** Object: net saving = shed − payback, and the optimal bout/event duration
  that maximises it. Numbers: published DR payback fractions for thermostatic loads versus
  published arousal-cost fractions for daily heterotherms; test whether optimal duration scales
  the same way with the fixed re-entry cost. **12–16 h**, most of it full-text on the DR side.
  `extends-to: [[C14-degree-of-passivity]]`, and uses `[[M3-separate-timescales]]` — both
  systems work by putting a slow depression against a fast, expensive recovery.

### 5. Thermal-storage seasonal cycling ↔ diapause energetics — hold

- **A.** Denholm & Hand 2011, `10.1016/j.enpol.2011.01.019`, `N_A` = 794.
- **B.** Hahn & Denlinger, "Energetics of Insect Diapause", *Annu. Rev. Entomol.* 56 (2011),
  `10.1146/annurev-ento-112408-085436`. Crossref count 714. OpenCitations `N_B` = 723.
- **Intersection.** ∩ = **0**. `N` floor = 1,517; `E` = 378.4.
- **Same-object argument.** Seasonal thermal storage and diapause both hold an energy stock
  across months against a **self-discharge / basal-drawdown rate** in units of fraction per
  day, and both size the store as (required duration × drawdown rate) with a margin. Diapause
  research reports lipid depletion rates and the resulting minimum entry mass; seasonal-storage
  research reports standing losses and the resulting sizing penalty. Same arithmetic.
- **Metaphor-risk objection and why it holds this back.** Denholm & Hand is a
  *diurnal-to-multiday* storage paper, not a seasonal one, so anchor A is mis-scoped for the
  claim. Re-anchor to a seasonal thermal-storage review before this is opened. Also, the
  round-trip-efficiency object on the thermal side has no diapause counterpart — insects do
  not put energy back into the store.
- **What closes it.** A correctly scoped seasonal-storage anchor, then: minimum entry stock =
  drawdown × duration, both sides, non-dimensionalised on duration. **10–14 h.**
  `extends-to: [[G3-cycle-life]]`.

### 6. Microgrid islanding / cascade arrest ↔ food-web compartmentalisation — hold

- **A.** Motter & Lai, "Cascade-based attacks on complex networks", *Phys. Rev. E* 66 (2002),
  `10.1103/PhysRevE.66.065102`. Crossref count 1,543. OpenCitations `N_A` = 1,478.
- **B.** Stouffer & Bascompte, "Compartmentalization increases food-web persistence", *PNAS*
  108 (2011), `10.1073/pnas.1014353108`. Crossref count 660. OpenCitations `N_B` = 636.
- **Intersection.** ∩ = **2**. `N` floor = 2,112; `E` = 445.0; `O/E` = 0.0045.
- **Both hits inspected** (Crossref, 2026-09-05):
  - `10.1038/s41467-021-23292-9` — Kaiser et al. 2021, "Network isolators inhibit failure
    spreading in complex networks". **Closest thing to a bridge found in this scout**, and it
    is still a physics paper: it is about topological isolators in supply networks and cites
    the food-web work as an instance of network structure, not as a source of method.
  - `10.1038/srep42956` — Jin et al. 2017, "Coupling effect of nodes popularity and similarity
    on social network persistence". Incidental complex-networks co-citation. Not a bridge.
  - So ∩ = 2 is **not** two bridges; it is one weak partial and one accident.
- **Metaphor-risk objection.** This pair's mediator is *complex-network science*, and the whole
  point of a mediated topology is that neither side is reading the other — both are reading
  the mediator. That is a `topology: mediated` situation, and per the vault's own conventions
  the mediator field must be named. The shared quantity — cascade size versus modularity `Q` —
  is genuinely the same measurable, but a large share of it is already published inside network
  science, which is where the novelty risk lives, not the citation risk.
- **What closes it.** Object: cascade extent vs modularity. Numbers: published grid
  cascade-size distributions with the network's `Q` computed, against Stouffer's persistence
  vs compartmentalisation. **8 h**, but the novelty audit must come first. New instrument
  (partition-persistence); no existing computed note fits.

---

## Checked and rejected

- **EROI ↔ optimal foraging (Charnov 1976), ∩ = 0 across 384 × 4,088.** Rejected on two
  independent grounds. (i) **Units.** EROI is dimensionless energy out over energy in; the
  marginal value theorem's currency is a long-term net *rate*, E/time, and its result is a
  patch-residence time, not a ratio. Different quantities. (ii) **It is not a gap anyway.**
  EROI's own genealogy runs through Charles Hall's fish-energetics work (Hall 1972,
  `10.2307/1934773`), and Murphy & Hall 2010 × Hall 1972 returns ∩ = **14** — a real link, but
  one carried almost entirely by the Hall/Murphy energy-economics lineage itself
  (`10.1098/rsta.2013.0126`, `10.1016/j.ecolecon.2014.12.001`, plus ten *Energies*/
  *Sustainability* papers). This is **one-way borrowing** in the `G3-cycle-life` sense: energy
  economics took the idea from ecological energetics and says so; ecology does not read back.
  A description, not a zero. **Do not open "EROI is foraging" as a gap.**
- **EROI ↔ metabolic scaling (West 1997), ∩ = 0 across 384 × 4,132.** Kleiber is a power law
  of metabolic rate in body mass. There is no return-on-investment ratio anywhere in it. Word
  level only.
- **Grid inertia ↔ allostatic load (Milano 2018 × McEwen 1998), ∩ = 0 across 751 × 5,278.**
  Rejected. "Buffering capacity" is a shared word. Grid inertia is `H` in MW·s/MVA — a stored
  kinetic energy normalised by rating, with an exact defining equation. Allostatic load is a
  composite index of biomarkers with no conserved quantity behind it. Nothing to put on one
  axis.
- **Grid frequency regulation ↔ heart rate variability (Milano 2018 × Task Force 1996),
  ∩ = 0 across 751 × 12,122.** Rejected despite the superficially perfect match (both are
  power spectra of the deviations of a rate about a setpoint, both partition the spectrum into
  named bands). The estimands are opposed: in the grid, spectral power at low frequency is
  *control error to be minimised*; in HRV, it is *healthy adaptive capacity to be maximised*.
  Same mathematics, contradictory interpretations, no shared normative quantity. This is the
  cleanest homograph in the domain and should be recorded as such in `failure-modes.md` §2 if
  anyone proposes it again.
- **Storage sizing ↔ bet-hedging (Denholm × Cohen 1966; Denholm × Philippi & Seger 1989),
  ∩ = 0 both.** Rejected for now. Bet-hedging optimises a **geometric mean** of fitness across
  environments; storage sizing minimises an **expected cost** subject to a reliability
  constraint. Those are different functionals, and the difference is exactly the interesting
  part — which means the honest version of this candidate is a claim that the grid *should*
  use a geometric-mean objective, i.e. a Layer-3 prediction, not a Layer-1 gap. Park it.
- **Curtailment ↔ photoinhibition (Long 1994), ∩ = 0.** Not rejected — folded into candidate
  #2 as its second B-side anchor, where it does useful work as a robustness check on the zero.
- **Exergy destruction ↔ entropy production in metabolism.** Not tested, and deliberately so.
  The Prigogine/Schrödinger/Jørgensen lineage has been explicitly joined to ecosystem
  thermodynamics for four decades; the shortlist's own "Landauer ↔ England" rejection is the
  same shape (45 co-citers, joined literature). Testing it would spend probes to confirm a
  bridge. If someone wants the number, the pair to run is Jørgensen's ecological-exergy work
  against a mainstream exergy-analysis anchor — expect a large positive.
- **Capacity factor ↔ PSII duty cycle.** Not opened as a separate candidate: `C1` already
  computes a photosynthetic functional fraction (0.883) and already places grid availability on
  that axis. Extending C1 with capacity factor is vault work, not a new gap — and C1's own
  warning applies, that a *population functional fraction* and a *unit availability* must not
  share a line. Capacity factor is neither; it is an output-weighted mean, a third object.
  Say so in C1 rather than opening a gap.

---

## Recommendation: which two to open first

**Open #1 (loss-of-load probability ↔ starvation-risk first passage) first.** It is the only
candidate in this scout that passes the strict test the brief demands — the *same quantity with
the same units* appears on both sides (a dimensionless probability that a reserve hits zero
within a horizon), computed by the *same method* (backward stochastic dynamic programming on a
value function), with a *second* matching quantity for free (the shadow price of reserve as the
derivative of that value function). ∩ = 0 across 2,058 × 422 citers with a 350-expected floor.
It extends `C1-availability-living-tissue` in the direction C1 is currently missing — C1's
`A = k_r/(k_r+k_d)` is the stationary limit, and this supplies the horizon-dependent form. And
it carries its own scoping discipline: it only works against storage-constrained LOLE, which
means the claim is falsifiable at the first anchor read.

**Open #2 (curtailment ↔ non-photochemical quenching) second.** It is the more striking
candidate and the more likely to be a metaphor, which is why it goes second rather than first.
Its strength is that the shared object is a plain dimensionless fraction of the *input* that
neither system can use and both must dump to avoid damage, that both fields close a
three-way budget (used / stored / dumped), and that both quantify the same downstream failure
when dumping is too slow. Its weakness is that "safely dumping excess" is a functional
description of the kind `failure-modes.md` §4 exists to catch — so it must be opened with the
numeric superposition test written into the note *before* any reading starts: if the two dump
fractions do not collapse onto one curve against `input/sink_capacity`, the note records a
metaphor and closes. The zero is doubly anchored on the biology side (NPQ and photoinhibition,
both ∩ = 0), which is more than any other candidate here has.

**Before either is written up as a vault note, rerun the OpenAlex leg.** Both rest on a single
provider today because the one permitted probe was consumed by a 429, and the project's own
standard in `citation-sources.md` is that two sources agreeing is the check.
