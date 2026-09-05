---
name: C1-availability-living-tissue
type: computed
---

# Availability of living tissue

> **Photosystem II runs at a steady-state functional fraction of 0.883 at 20 °C (community
> mean, `k_PI = 2.70e-4 s⁻¹`, `k_REC = 20.2e-4 s⁻¹`). A leaf holds ~10⁸ of them, so the
> *leaf's* photosynthetic function availability is ≈ 1 — the 0.883 is a population fraction,
> not a system availability, and the two must not be put on the same line.**

Computes [[availability-formula]] — `A = MTBF/(MTBF+MTTR) = k_r/(k_r+k_d)` — on tissue, and
puts the result on the same axis as repairable engineered systems. Extended onto engineering
systems and given a dimensionless form (`Ha = k_r/k_d`) in [[C6-damage-healing-ratio]].

**Every row below carries its inputs, its arithmetic, and a source fetched on the stated date.**
Rows whose inputs could not be sourced are marked UNSUPPORTED and their old numbers struck
rather than quietly retained.

---

## 1. The two objects this note contains

`A` is computed the same way in both cases, but it *means* two different things, and the
headline defect this note used to have was mixing them:

| | **Unit availability** | **Population functional fraction** |
|---|---|---|
| Object | one repairable item, up or down | ~10⁸ units, a fraction down at any instant |
| `A` is | a probability the item is up | an expected fraction of units up |
| Coincide when | — | units fail **independently** |
| Rows here | grid, wind turbine, data centre, bone (approximately) | PSII |

The two coincide numerically and diverge in meaning. **A comparison is only legitimate within
a column.** Section 4 states what happens to the PSII number when it is aggregated to the leaf.

---

## 2. Population functional fraction — photosystem II

**Inputs.** `k_PI` (photoinactivation) and `k_REC` (repair) rate coefficients, both measured on
the same specimens, from Bártolo, Frankenbach & Serôdio, *Photoinactivation vs repair of
photosystem II as target of thermal stress in epipelic and epipsammic microphytobenthos
communities*, **PLOS ONE 18(9): e0292211 (2023)**, DOI `10.1371/journal.pone.0292211`.
Fetched via Europe PMC full text
<https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10538756/fullTextXML>, **2026-09-05**.
Values are seasonally averaged means ± 1 SE, ×10⁻⁴ s⁻¹.

**Arithmetic.** `A = k_REC/(k_REC + k_PI)`.

| Community, temperature | `k_PI` (10⁻⁴ s⁻¹) | `k_REC` (10⁻⁴ s⁻¹) | arithmetic | **A** |
|---|---|---|---|---|
| GE-EPM, 20 °C | 2.78 ± 0.25 | 23.67 ± 3.28 | 23.67/(23.67+2.78) | **0.895** |
| VA-EPL, 20 °C | 2.61 ± 0.11 | 16.80 ± 1.59 | 16.80/(16.80+2.61) | **0.866** |
| **community mean, 20 °C** | **2.695** | **20.235** | 20.235/(20.235+2.695) | **0.8825 → 0.883** |
| VA-EPL, 35 °C heat stress | 4.14 ± 0.52 | 9.92 ± 2.28 | 9.92/(9.92+4.14) | **0.706** |
| GE-EPM, 35 °C heat stress | 4.95 ± 0.61 | 6.36 ± 1.33 | 6.36/(6.36+4.95) | **0.562** |
| VA-EPL, 5 °C cold stress | 3.11 ± 0.21 | 2.82 ± 0.15 | 2.82/(2.82+3.11) | **0.476** |
| GE-EPM, 5 °C cold stress | 3.01 ± 0.14 | 2.50 ± 0.13 | 2.50/(2.50+3.01) | **0.454** |

All seven reproduce [[C6-damage-healing-ratio]] §5 to the quoted digits. **Source status:
VERIFIED-PRIMARY** (open-access full text fetched).

**`k_PI` is not a constant of the organism.** Tyystjärvi & Aro, *The rate constant of
photoinhibition, measured in lincomycin-treated leaves, is directly proportional to light
intensity*, **PNAS 93:2213–2218 (1996)**, DOI `10.1073/pnas.93.5.2213`, PMCID `PMC39937`
(record and abstract fetched from Europe PMC and
<https://pmc.ncbi.nlm.nih.gov/articles/PMC39937/>, **2026-09-05**; **abstract only**, the
numeric proportionality constant was not obtained) establishes that `k_PI ∝ PPFD` across
6.5–1500 µmol m⁻² s⁻¹. So every `A` above is **conditional on the actinic light of that
assay**, and the table is a temperature series at one light level, not a property of PSII.

---

## 3. Unit availability — repairable systems

### 3.1 US electricity distribution

**Inputs.** SAIDI (min/customer/yr) and SAIFI (interruptions/customer/yr), 2024, from EIA
*Electric Power Annual*, **Table 11.1 Reliability Metrics of U.S. Distribution System**,
<https://www.eia.gov/electricity/annual/html/epa_11_01.html>, fetched **2026-09-05**.
Context article: EIA *Today in Energy*, "Hurricanes in 2024 led to the most hours without power
in the United States in 10 years", <https://www.eia.gov/todayinenergy/detail.php?id=66744>,
published 2025-12-01, fetched **2026-09-05**.

**Arithmetic.** `MTTR = SAIDI/SAIFI`; `MTBF = (525,960 min/yr − SAIDI)/SAIFI`;
`A = MTBF/(MTBF+MTTR)` (identically `1 − SAIDI/525,960`).

| Case | SAIDI | SAIFI | MTTR | MTBF | **A** |
|---|---|---|---|---|---|
| incl. major event days | 662.6 min | 1.531 /yr | 432.8 min = **7.21 h** | 343,107 min = **5,718 h** | **0.99874** |
| excl. major event days | 126.0 min | 1.043 /yr | 120.8 min = **2.01 h** | 504,155 min = **8,403 h** | **0.99976** |

Replaces the old unsourced "US power grid, normal operations = 0.9998". **VERIFIED-PRIMARY.**

### 3.2 Wind turbine fleet — the repairable-product row (E9)

**Inputs.** Carroll, McDonald & McMillan, *Failure rate, repair time and unscheduled O&M cost
analysis of offshore wind turbines*, **Wind Energy 19(6):1107–1119 (2016)**, DOI
`10.1002/we.1887`. Author-accepted PDF fetched from the Strathclyde repository
<https://strathprints.strath.ac.uk/54141/1/Carroll_etal_WE_2015_Failure_rate_repair_time_and_unscheduled_O_and_M_cost_analysis_of_offshore.pdf>,
**2026-09-05**, and text-extracted. Population: ~350 offshore turbines in Europe, **1,768
turbine-years ≈ 15.5 million turbine-hours**. Table 2 of that paper:

| Category | λ (/turbine/yr) | repair time (h) | λ × time (h/yr) |
|---|---|---|---|
| Minor repair | 6.81 | 6.67 | 45.42 |
| Major repair | 1.17 | 17.64 | 20.64 |
| Major replacement | 0.29 | 116.19 | 33.69 |
| **total** | **8.27** | — | **99.76** |

**Arithmetic.** `MTTR = 99.76/8.27 = 12.06 h`. `MTBF = (8760 − 99.76)/8.27 = 1047 h`.

```
A = MTBF/(MTBF+MTTR) = 1047/(1047 + 12.06) = 0.98861
```

**A(wind turbine, offshore fleet) = 0.9886.** The paper's own headline failure rate is 8.3
/turbine/yr (6.2 minor, 1.1 major, 0.3 replacement), consistent with the 8.27 summed from
Table 2. **VERIFIED-PRIMARY.**

**Two caveats specific to this row.**

1. **Population vs unit — this row is a *unit* availability, and that is the point of adding
   it.** Each turbine is genuinely two-state (generating / not generating) and genuinely
   repairable, so `A = 0.9886` reads as *"the probability that a randomly chosen turbine at a
   randomly chosen instant is not down for corrective maintenance"*. That is the same object as
   the grid row and **not** the same object as PSII's 0.883. λ and repair time are fleet
   averages over 1,768 turbine-years, so the number is a fleet mean of a unit probability, not
   a fraction-of-a-population quantity like PSII's.
2. **It is an upper bound.** Carroll et al. define repair time as technician time on the
   turbine; it **excludes travel, vessel waiting, spare-part lead time and weather
   inaccessibility**, which offshore dominate real downtime. Two independent notes: the paper's
   Table 2 column is printed as "Repair Time (Days)" while Figure 13 plots the same quantity in
   hours (max ~298 h for a gearbox major replacement) — **the units in Table 2 are hours**, and
   this note reads them as hours. Fleet *time-based* availability reported by operators is
   commonly ~0.97–0.98, i.e. **below** this bound, consistent with the excluded logistics time.

### 3.3 Data centre "five nines" — UNSUPPORTED as a measurement

The old row "Data centre, five nines = 0.99999" is **struck as a measured figure.** Arithmetic
of the claim: `1 − 0.99999 = 1e-5`, ×525,960 min/yr = **5.26 min/yr** of downtime.

Uptime Institute — the body that owns the Tier classification the number is usually attached
to — disowns it. Andy Lawrence, "99 Red Flags", *Uptime Institute Journal*, 2019-10-28,
<https://journal.uptimeinstitute.com/99-red-flags/>, fetched **2026-09-05**: availability
figures in SLAs are "market-driven", set "high enough to attract (or not scare away) customers,
but low enough to ensure minimum compensation is paid"; readers should "treat this number, and
any SLAs that use this number, with extreme caution". CTO Chris Brown, same piece: there is **no
direct relationship between a number of nines and a Tier level**, and the early Uptime paper
giving expected availability per Tier "is no longer considered relevant".

**Verdict: keep as a stated design target with no MTBF/MTTR behind it. It is not a datum and
must not anchor the top of the axis.**

### 3.4 Commercial aviation dispatch — UNSUPPORTED, and the wrong object

The old row "Commercial aviation dispatch = 0.995" is **struck.** Two defects:

- **No primary source obtained.** Figures of 99.4 % (737 fleet) and >99.7 % (A320neo) appear in
  search results 2026-09-05; the FAA document carrying the 99.4 % figure
  (<https://www.faa.gov/sites/faa.gov/files/2022-11/eteb%20findings%20and%20recs%20summary.pdf>)
  returned **HTTP 403** on fetch, so nothing here is verified.
- **Dispatch reliability is not availability.** It is the fraction of scheduled departures not
  delayed beyond a threshold (commonly 15 min) or cancelled for a technical cause. Its
  denominator is *departures*, not *time*, and deferred defects carried under an MEL count as
  successful dispatches while the aircraft is degraded. `A = MTBF/(MTBF+MTTR)` is not the
  quantity being reported.

---

## 4. Bone — replaced by [[C6-damage-healing-ratio]] §5's bands

**Inputs.** Human bone remodelling durations from PMC3028072, fetched via Europe PMC
<https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3028072/fullTextXML> (durations VERIFIED
in C6 §5; that fetch is C6's, this note inherits it and does not re-assert it).

**Arithmetic.** Take the revisit interval as MTBF + MTTR and the down phase as MTTR:
`A = (revisit − down)/revisit`.

| Row | revisit | down-state definition | arithmetic | **A** | `Ha` |
|---|---|---|---|---|---|
| Trabecular, *full remodelling cycle* down | 730 d | 200 d | (730−200)/730 | **0.726** | 2.65 |
| Trabecular, *resorption phase only* down | 730 d | 35 d | (730−35)/730 | **0.952** | 19.9 |
| **Cortical** | **not obtained** | cycle median 120 d | — | **UNSUPPORTED** | — |

**Old value struck: trabecular 0.939.** It came by a "remodelling space" route with no stated
inputs and sits inside, but not at either end of, the definition-dependent band. **Trabecular
bone's availability is 0.726–0.952, a band of width 0.23, and the width is the finding**: bone
is not two-state (a resorption cavity degrades stiffness rather than eliminating it), so
condition C2 of [[C6-damage-healing-ratio]] fails and `A` is definition-dependent.

**Old value struck: cortical 0.984.** C6 §5 lists cortical bone as PARTIAL — the remodelling
cycle median (120 d) is verified but the **turnover/revisit interval was not found**, so there
is no denominator. **0.984 has no supporting datum anywhere in this vault and is withdrawn**
until a revisit interval is sourced. It was one of the two numbers in the old headline.

---

## 5. Gut epithelium — dropped, not blank

Previously "left blank deliberately". It is now **dropped**, with the reason promoted from a
caveat to a rule: a 3–5 day enterocyte turnover is **scheduled replacement before failure** —
preventive maintenance — and `A = MTBF/(MTBF+MTTR)` is defined on *corrective* repair of a
failed unit. No `(k_d, k_r)` pair exists for it because there is no `k_d`: the units are not
failing, they are being retired on a clock. Forcing the formula on it would be the
merely-cute failure mode. **No source sought; row deleted rather than marked.**

---

## 6. The axis, with only sourced rows

| System | column | inputs | **A** | status |
|---|---|---|---|---|
| Data centre "five nines" | unit | *none* — design target | (0.99999) | **UNSUPPORTED**, §3.3 |
| US grid, excl. major events | unit | SAIDI 126.0 min, SAIFI 1.043 | **0.99976** | VERIFIED-PRIMARY |
| US grid, incl. major events | unit | SAIDI 662.6 min, SAIFI 1.531 | **0.99874** | VERIFIED-PRIMARY |
| **Offshore wind turbine fleet** | **unit** | **λ 8.27/yr, MTTR 12.06 h** | **0.98861** | **VERIFIED-PRIMARY** (upper bound) |
| Commercial aviation dispatch | — | *none* | (0.995) | **UNSUPPORTED**, wrong object, §3.4 |
| Trabecular bone, resorption-only | ~unit | 730 d / 35 d | **0.952** | VERIFIED durations |
| Trabecular bone, full cycle | ~unit | 730 d / 200 d | **0.726** | VERIFIED durations |
| Cortical bone | — | revisit interval **not obtained** | **UNSUPPORTED** | was 0.984 |
| PSII, 20 °C community mean | **population** | k_PI 2.70e-4, k_REC 20.2e-4 s⁻¹ | **0.883** | VERIFIED-PRIMARY |
| PSII, 35 °C heat stress | population | see §2 | 0.562–0.706 | VERIFIED-PRIMARY |
| PSII, 5 °C cold stress | population | see §2 | 0.454–0.476 | VERIFIED-PRIMARY |

---

## 7. The caveats, restated as they now stand

1. **Population, not unit — and the headline now says so.** A leaf holds ~10⁸ photosystems and
   a *fraction* is down, never the whole. `A_PSII = 0.883` is an **expected functional
   fraction**. Aggregated over `N ≈ 10⁸` independent units, the probability that photosynthetic
   function is *unavailable at the leaf* is `(1−0.883)^N ≈ 10^(−9.3×10⁷)`, i.e. **leaf-level
   function availability ≈ 1** and no engineered system on this axis is close. The old headline
   "a leaf is less available than a power grid" compared a population fraction to a system
   availability probability and is **struck**; see §8.
2. **Independence is the load-bearing assumption**, and the 35 °C row is the counterexample:
   heat hits every unit at once, correlated damage defeats the redundancy, and the *fraction*
   falls to 0.562. Correlated stress, not baseline turnover, is what a leaf has to survive.
3. **Down-while-repaired holds for PSII, not bone** — hence §4's band rather than a number.
4. **Preventive replacement is not availability** — hence §5's deletion.

---

## 8. Corrections 2026-09-05

**A22 — every row rebuilt with inputs, arithmetic and a fetched source.**

| Row | old | new | why |
|---|---|---|---|
| PSII, 20 °C | 0.883, no inputs, no source | **0.883** from `k_PI = 2.695e-4`, `k_REC = 20.235e-4 s⁻¹` | Bártolo et al. 2023, PLOS ONE, DOI 10.1371/journal.pone.0292211, fetched 2026-09-05; reproduces to 3 s.f. |
| PSII, 35 °C / 5 °C | "0.56–0.71" / "0.45–0.48" | **0.562, 0.706** / **0.454, 0.476** | same source; per-community rather than a range |
| Trabecular bone | **0.939** | **0.726–0.952 band** | contradicted C6 §5; replaced by C6's two definition-dependent endpoints |
| Cortical bone | **0.984** | **UNSUPPORTED** | C6 §5 marks cortical PARTIAL: revisit interval not found, so no denominator exists |
| US power grid | 0.9998, no source | **0.99976** (excl. MED) and **0.99874** (incl. MED) | EIA *Electric Power Annual* Table 11.1, fetched 2026-09-05 |
| Data centre five nines | 0.99999 as a datum | **UNSUPPORTED design target** | Uptime Institute "99 Red Flags" (2019-10-28) disowns the nines-to-Tier mapping; fetched 2026-09-05 |
| Aviation dispatch | 0.995 | **UNSUPPORTED, wrong object** | FAA source 403'd; dispatch reliability has a per-departure denominator, not a time denominator |
| Gut epithelium | blank with a caveat | **dropped** | preventive replacement, no `k_d` |

**A23 — headline replaced.** Old: *"Photosystem II = 0.883. Cortical bone = 0.984. A leaf is
less available than a power grid."* Two defects: `0.984` had no source (see above), and the
comparison put a population functional fraction against a system availability probability. New
headline states the PSII steady-state functional fraction with its two rate inputs and states
that ~10⁸-fold redundancy makes leaf-level function availability ≈ 1. §1 now separates the two
columns so no future row can cross them silently.

**E9 — repairable-product row added.** Offshore wind turbine fleet, **A = 0.9886** from
λ = 8.27 failures/turbine/yr and MTTR = 12.06 h (Carroll, McDonald & McMillan 2016, *Wind
Energy* 19:1107–1119, DOI 10.1002/we.1887, author PDF fetched 2026-09-05, 1,768 turbine-years).
Population-vs-unit caveat restated for the row in §3.2: this is a **unit** availability, same
object as the grid row, and an **upper bound** because the source's repair time excludes travel,
vessel and weather waiting.

**Sources fetched 2026-09-05, all URLs above:** EIA Electric Power Annual Table 11.1; EIA Today
in Energy id=66744; Europe PMC PMC10538756 full text (PLOS ONE 2023); PMC39937 / Europe PMC
record (PNAS 1996, abstract only); Strathclyde repository Carroll et al. 2016 PDF; Uptime
Institute Journal "99 Red Flags". **Not obtained:** FAA ETEB summary PDF (403); Carroll et al.
publisher version (Wiley 403); Tyystjärvi & Aro numeric proportionality constant; cortical bone
turnover/revisit interval.

See [[C6-damage-healing-ratio]], [[availability-formula]], [[G5-repair-number]].
