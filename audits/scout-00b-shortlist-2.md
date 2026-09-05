# Scout shortlist 2 — 2026-09-05 (second sweep)

Three scouts (conservation genetics, water/soil/urban, energy). OpenCitations only (OpenAlex budget-locked); every E is a union floor unless stated. Full reports: `scout-04-conservation-genetics.md`, `scout-05-water-soil-urban.md`, `scout-06-energy-systems.md`.

| # | Candidate (A ↔ B) | ∩ | Robustness | Extends | Cost | Decision |
|---|---|---|---|---|---|---|
| 1 | Loss-of-load probability (Billinton & Allan) ↔ starvation-risk first passage (McNamara & Houston 1987) | 0 / 2058×422 | same estimand, same units, same method (backward SDP); VoLL ↔ marginal fitness value of fat | C1 | one session | **open G34** |
| 2 | Genetic load W̄ = e^(−U) (Haldane–Muller) ↔ semiconductor die yield Y = e^(−A·D0) (Murphy/Stapper) | 0 on 12/12 pairings, 1963–2022 | mode 6 run on both sides; both in-domain controls fire | new | 6–8 h | **open G35** |
| 3 | Archard wear ↔ soil erosion detachment (WEPP); fatigue (Miner/Paris) ↔ aggregate wet–dry breakdown | 0 on 7/7 | E > 1 for any N under ~6–8M works | C6 (fills the empty Ha row: erosion rate / soil formation T-value) | one session | **open G36** |
| 4 | Adaptive management ↔ Duane reliability growth | 0 on both anchors | flanking controls fire (64, 13) | new | 6 h | **open G37** |
| 5 | Curtailment ↔ non-photochemical quenching | 0, double-anchored | shared dimensionless dumped-input fraction | C14 | short | next round |
| 6 | Danckwerts RTD ↔ soil carbon transit time (Sierra 2016) | 0 both routes; RTD ↔ groundwater = 21 (control) | needs scoped N | new | short | next round |
| 7 | Diapause ↔ torpor (bio–bio) | 2 / 723×1006 | biology not joined internally | — | — | note only |

**Rejected with evidence:** EROI ↔ foraging (one-way borrowing from Hall 1972, ∩ = 14); bet-hedging ↔ Kelly (25); portfolio effect ↔ Markowitz (22); RTD ↔ groundwater (21); urban metabolism ↔ ENA (8 real); Washburn ↔ Philip (7 real + 1 back-matter artifact); frequency regulation ↔ HRV (homograph); percolation ↔ infiltration (Hunt & Ewing 2014 monograph, invisible to DOI indexing).

**Method findings:** `_scripts/intersect.py` counts a blank `citing` key → every N and ∩ inflated by 1; all past single-hit results suspect. Schindler 2010 × Cohen 1966 = 1 against E ≈ 627: ecology's portfolio-effect and bet-hedging literatures barely cite each other.
