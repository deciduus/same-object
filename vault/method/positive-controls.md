---
name: positive-controls
type: method
---

# Positive controls

Running a known-**closed** pair alongside a gap claim. Not standard practice in
[[precedent|literature-based discovery]], and it directly answers a documented 2023 complaint
that the field's evaluation "is built on sand."

## The calibration

| Pair | Co-citers | Reading |
|---|---|---|
| Gompertz and Weibull mortality/reliability | **218** | closed |
| Weibull and the reliability theory of aging | **35** | closed |
| Levy-flight search: physics and movement ecology | **183 (23% of base)** | closed |
| Gittins and Sutton & Barto | **181 (11.7%)** | closed |
| DNA storage and error-correcting codes | **5.4%** | closed |
| **This project's surviving gaps** | **0–8** | — |

**The signal separates cleanly.** That is what makes the zeros mean anything — but the table
above is not in comparable units, and the next section says so.

## The same table in null-model units

Per [[citation-intersection]], "Expected co-citers under independence": `E = |A|·|B|/N_universe`,
`O/E` reported against a stated `N`. The counts above mix absolutes (218, 35) with
fractions-of-one-base (23%, 11.7%, 5.4%) and are then compared to a range of absolutes ("0-8").
**None of those three quantities is the same quantity.** Restated below with whatever inputs the
project actually recorded; where a side's citer-set size was never logged, the row says so rather
than inventing one.

`N` here is the **union floor** `|A| + |B| - O` — the smallest defensible denominator, which
makes `E` the largest and `O/E` the smallest, i.e. it flatters gap claims. It is quoted because
it is computable from recorded numbers; it is not a substitute for a fetched concept-scoped `N`.

| Pair | `|A|` | `|B|` | O | E (union floor) | **O/E** | Reading |
|---|---|---|---|---|---|---|
| Gompertz and Weibull mortality/reliability | — | — | 218 | — | — | **inputs not recorded** (neither citer-set size logged) |
| Weibull and the reliability theory of aging | — | 633 | 35 | — | — | **inputs not recorded** (Weibull-side citer count never logged; the 633 is the RTA side, from the one-way section below) |
| Levy-flight search: physics and movement ecology | 796 *(derived: 183/0.23)* | — | 183 | — | — | **inputs not recorded** (the 23% names one base; the partner base was never logged) |
| Gittins and Sutton & Barto | 1,547 *(derived: 181/0.117, OpenAlex)* | — | 181 | — | — | **inputs not recorded**, and the 181 is **method-dependent** — the DOI route returns 24 (see [[G28-marginal-value-gittins]]) |
| DNA storage and error-correcting codes | — | — | — | — | — | **inputs not recorded**: only the 5.4% survives, with no absolute count and no stated base |
| **Gittins x Auer 2002** *(the one fully specified control)* | 1,013 | 3,906 | **225** | 843 | **0.267** | closed |
| **Gap: Gittins x Charnov** ([[G28-marginal-value-gittins]]) | 1,013 | 5,424 | **5** | 854 | **0.0059** | gap; **control ratio 62.5** |
| **Gap: engineering x ecology multifunctionality** ([[G6-multifunctionality]]) | 172 | 861 | **0** | 143 | **0** | gap at this `N`; `E < 1` above `N ~ 1.5x10^5` |
| **Gap: Hopfield x coding theory** ([[G25-proofreading-coding]]) | 416 *(inspected)* | — | **0** | — | **0** | `O = 0` is denominator-free; Shannon-side base **not recorded** |

**What the restatement costs the claim.** Five of the six original controls cannot be put in
these units at all, so "the signal separates cleanly" is currently supported by **one** fully
specified control pair (Gittins x Auer) and by two gaps whose zeros are denominator-sensitive.
The separation is real where it has been measured; the table overstated how much of it had been.

**What it adds.** The control ratio `(O/E)_gap / (O/E)_control` is invariant under the choice of
`N` and is therefore the statistic to quote. For G28 it is **62.5**, replacing the note's
denominator-dependent "factor of 45".

## The closed-gap signature

Three properties, and the third is the most diagnostic:

1. shared vocabulary
2. shared canonical citations
3. **performance reported as a fraction of a theoretical bound**

A DNA-storage paper reporting *"1.57 bits/nt against a Shannon capacity of 1.83 — 86% of
capacity"* as its headline is a field with a shared axis. [[G25-proofreading-coding]] has none
of the three.

## One-way closure

The mortality/reliability control is closed in only one direction: of 633 works citing the
reliability theory of aging, **6 are reliability engineering.** Under 1%. Biology imported
wholesale; engineering never imported back. See [[one-way-borrowing]].
