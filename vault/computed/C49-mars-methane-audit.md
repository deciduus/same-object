---
name: C49-mars-methane-audit
type: computed
exit: specification
extends-to: astrobiology
---

# Mars methane, audited blind: the case has no single observable, and the residual is a sink

> **Step 0 does not return one verdict — it returns four, because "methane on Mars" is four
> different observables and they do not have the same standing.** The *globally mixed*
> background is `<0.05 ppbv` (TGO) and therefore **consistent with zero** → `NO OBSERVABLE TO
> EXPLAIN`. The *ground-based plumes* (`45 ppbv`, Mumma 2009) are contested from the same
> spectra by Zahnle 2011 → `NO AGREED OBSERVABLE`. The *2019 spike* read globally is
> `NOT FORMABLE`: 21 ppbv gone in a sol needs `2.3×10⁸ t/yr` of removal, a `3.7×10⁵×` speed-up.
> Only the *Gale near-surface seasonal* observable — `0.41 ± 0.16 ppbv` at **2.56σ**, cycling
> `0.24 → 0.65` — survives step 0, and it survives **conditionally**: one instrument, one team,
> **no second reduction of the TLS records exists**, which is a step-0 condition Part C's table
> has no row for. **On that observable the audit's exclusion is a `SINK`, not a source.**
> The seasonal cycle needs `τ_eff = 0.944 yr`, a `318×` speed-up on the 300-yr photochemistry,
> so photochemistry is `RULED OUT` at `A = 319` and survives the 2× aperture row. **Every
> source passes and one sink fails — and that asymmetry is a property of the instrument, not
> of Mars: the source leg's aperture is free and the sink leg's is not.**

Blind brief archived and hashed **before** the run at `audits/blind-brief-c49-2026-09-05.md`,
sha256 `34a7d8ee823c28b8c776a56d9bfeca62fae177650f8e9059082274efaff2c424`. Arithmetic:
`vault/_scripts/c49_mars.py`. All fetches **2026-09-05**. P-089, Track C.

See [[reservoir-audit]] (Part C, step 0, D.3a blind protocol, F2/F3/F4/F7/F8),
[[C30-venus-phosphine-audit]] (the halt this note partly reproduces and partly does not),
[[C11-flyby-reservoir-audit]] (the residual-specification output shape),
[[C46-reservoir-audit-negative-control]] (`NO RESIDUAL`, the third state).

---

## 1. Step 0(a) — significance

| Observable | Central value | Uncertainty | σ | 0(a) |
|---|---|---|---|---|
| Gale near-surface background (TLS-SAM) | `0.41 ppbv` | `± 0.16` | **2.56** | passes, **weakly** |
| Gale seasonal range | `0.24 → 0.65 ppbv` | — | ~3 on the amplitude | passes |
| Globally mixed background (TGO/ACS) | **`< 0.05 ppbv`** | upper limit | — | **interval contains zero → `NO OBSERVABLE TO EXPLAIN`** |

`2.56σ` is the weakest observable this instrument has been run on. C30's D.2 test is a
one-reduction interval containing zero; this one does not contain zero, but it is a
`0.41/0.16` result being asked to carry a whole ledger. Recorded, not waived.

## 2. Step 0(b) — the reductions table

| # | Reduction | Value | Instrument / altitude | Shares raw data with | Fetch status |
|---|---|---|---|---|---|
| 1 | Webster et al. 2018 | `0.41 ± 0.16 ppbv`, seasonal `0.24–0.65` | Curiosity TLS-SAM, **in situ, ~1 m**, Gale | 2, 3 | DOI `10.1126/science.aaq0131` **Crossref-verified**; full text paywalled, values from the brief |
| 2 | Webster et al. 2015 / 2018 enrichment mode | `~7 ppbv` spike (2013) | same | 1, 3 | as quoted verbatim in Yung 2018, **full-text-read** |
| 3 | Curiosity 2019 | `~21 ppbv` spike | same | 1, 2 | from the brief |
| 4 | Korablev et al. 2019 | **`< 0.05 ppbv`** | ExoMars TGO ACS/NOMAD, **solar occultation, ≳3–5 km** | 5 | DOI `10.1038/s41586-019-1096-4` **Crossref-verified** |
| 5 | Knutsen et al. 2021 | tighter TGO limits | TGO/NOMAD | 4 | DOI `10.1016/j.icarus.2020.114266` **Crossref-verified** |
| 6 | Giuranna et al. 2019 | `15.5 ± 2.5 ppbv`, 16 Jun 2013 | Mars Express PFS, orbital | — | DOI `10.1038/s41561-019-0331-9` **Crossref-verified** |
| 7 | Formisano et al. 2004 | `~10 ppbv` | Mars Express PFS | 6 (instrument) | DOI `10.1126/science.1101732` **Crossref-verified** |
| 8 | Mumma et al. 2009 | `~45 ppbv` plumes, N summer 2003 | ground-based IRTF/Keck | 9 | DOI `10.1126/science.1165243` **Crossref-verified** |
| 9 | **Zahnle, Freedman & Catling 2011** | *the same spectra reduced to a non-detection*: terrestrial telluric CH₄ imperfectly subtracted | **re-reduction of 8** | **8** | DOI `10.1016/j.icarus.2010.11.027` **Crossref-verified**; abstract only, **NOT full-text-read** |
| 10 | Moores et al. 2019 | diurnal variation + microseepage flux at Gale | model on 1 | 1 | DOI `10.1029/2019GL083800` **Crossref-verified**; **NOT obtained** (AGU paywall) |
| 11 | Webster et al. 2021 | day/night split at Gale — nighttime containment | Curiosity TLS-SAM | 1 | DOI `10.1051/0004-6361/202040030` **Crossref-verified**; **NOT full-text-read** |

### The four step-0 verdicts

1. **Globally mixed background → `NO OBSERVABLE TO EXPLAIN` (0(a) halt).** Rows 1 and 4 span
   detected/not-detected, but **not from the same photons** — different instruments, different
   altitudes, different air. D.3's literal trigger is not met; this is METHOD §5's
   same-class-systematic, not F8's pipeline split. What the literature does about it (rows 10,
   11) is not to adjudicate but to **redefine the observable**: a nighttime near-surface
   enhancement in a collapsed boundary layer, destroyed or diluted by day. Under that
   reconciliation the *global* quantity is TGO's `<0.05 ppbv`, an interval containing zero, and
   0(a) halts on it.
2. **Ground-based plumes → `NO AGREED OBSERVABLE` (0(b) halt).** Rows 8 and 9 are the *same
   spectra*, one reporting `45 ppbv` and one reporting an artefact of telluric subtraction.
   This is F8's trigger exactly, and it is C30's failure class on a second case.
3. **The 2019 spike → `NOT FORMABLE` as a global observable.** §4.
4. **Gale near-surface seasonal → PROCEED CONDITIONALLY**, on a condition the table has no row
   for: not a spanning set and not zero-consistent, but **unreplicable** — one instrument, one
   team, no independent reduction of the TLS records has ever been published, so 0(b) cannot be
   run at all. METHOD §5's "single-group claims resolve against the claimant" applies, and the
   audit proceeds with that stated. **Everything below is conditional on row 1 being real.**

## 3. Steps 1–2 — the observable in units, and the required flux

Mars surface area `1.444×10⁸ km²`, atmospheric mass `2.367×10¹⁶ kg` = `5.461×10¹⁷ mol`
(from `P_s = 610 Pa`, `g = 3.721`, `R = 3389.5 km`, `μ = 43.34 g/mol` — all standard values,
**UNVERIFIED**, and the ledger is linear in every one of them).

| Quantity | Value |
|---|---|
| Burden at `0.41 ppbv` | **3,592 t** |
| Burden at `0.24 / 0.65 ppbv` | 2,103 / 5,695 t |
| `R_ss` — hold `0.41 ppbv` against `τ = 300 yr` | **11.97 t/yr** |
| `R_seas` — drive `0.24 → 0.65` over half a Mars year | **3,820 t/yr** |
| `τ_eff` implied by the seasonal *fall* | **0.944 yr** → **318× faster than photochemistry** |
| Burden at `21 ppbv`, read globally | `1.84×10⁵ t` |
| `R_spike` — that gone in one sol | **`2.27×10⁸ t/yr`** (`τ = 7.1 h`, `3.7×10⁵×`) |

The `0.944 yr` is the load-bearing number and it is **derived here from the amplitude alone**,
with no chemistry: `τ = Δt / ln(χ_hi/χ_lo)`.

## 4. Steps 3–7 and 10 — the enumeration, with the step-5 aperture row

`A = required flux ÷ available flux`. `A > 1` rules out. Sensitivity at 2× / 0.5× the stated
aperture; every row is **linear in its aperture** except where marked.

| Side | Candidate | Required (t/yr) | Available (t/yr) | `A(2×)` | **`A`** | `A(0.5×)` | State |
|---|---|---|---|---|---|---|---|
| SOURCE | UV degradation of meteoritic/IDP organics — **background only** | 11.97 | 73.0 | 0.082 | **0.164** | 0.328 | `SURVIVES` (6.1× spare) |
| SOURCE | the same — **seasonal amplitude** | 3,820 | 73.0 | 26.2 | **52.3** | 105 | `RULED OUT` (×52) |
| SOURCE | Serpentinisation / abiotic FTT microseepage | 3,820 | `1.5×10⁵` | 0.013 | **0.025** | 0.051 | `SURVIVES` (40× spare) |
| SOURCE | Clathrate destabilisation | 3,820 | — | — | — | — | `NOT TESTED` — no Mars-wide release-rate bound in the sources read |
| SOURCE | Volcanic degassing | 3,820 | — | — | — | — | `NOT TESTED` — Yung 2018 calls it a minor emitter even on Earth; no Mars bound |
| SOURCE | Biological (methanogens) | 3,820 | — | — | — | — | `NOT TESTED` — **and see §6: the ledger cannot rule it out, which is a fact about the ledger** |
| SINK | **Gas-phase photochemistry, `τ = 300 yr`, vs the seasonal fall** | 3,820 | **11.97** | **159** | **319** | 638 | **`RULED OUT` (×319), survives the 2× row** |
| SINK | the same, vs the 2019 spike read globally | `2.27×10⁸` | 11.97 | `9.5×10⁶` | **`1.9×10⁷`** | `3.8×10⁷` | `RULED OUT` — i.e. **the spike is not a global observable** |
| SINK | Enhanced oxidant chemistry (H₂O₂ boost, Atreya 2007) | 3,820 | free — `[OH]` is a fitted scalar | — | **`≤ 1` by construction** | — | `SURVIVES` **the ledger**, and is `RULED OUT` by an observable the audit does not use: the same oxidants destroy CO and H₂, which sit at normal abundance (Yung 2018). **F4 in action** |
| SINK | Regolith adsorption / **two-way surface exchange** | 3,820 | `5.78×10⁸` | `3.3×10⁻⁶` | **`6.6×10⁻⁶`** | `1.3×10⁻⁵` | `SURVIVES` by **six orders** |
| SINK | Electrochemical / dust-storm (triboelectric) destruction | 3,820 | — | — | — | — | `NOT TESTED` — no published Mars-wide destruction-rate bound obtained |

**Aperture rows, stated as step 5 requires.**
IDP source: infall mass × organic content × UV yield — the Yung 2018 model itself; linear.
Serpentinisation: the **30,000 km² Nili Fossae olivine outcrop** at Oehler & Etiope's own
`5 t km⁻² yr⁻¹`; linear in area. Regolith exchange: the whole planet at the **lowest**
terrestrial microseepage rate `4 t km⁻² yr⁻¹`; linear in area.
**Photochemistry: the aperture is the atmospheric column already carrying the burden — it is
not free.** `P_avail = burden/τ`, both terms of which the observable fixes. That is why this is
the only row on the table whose `A` is reproducible between analysts, and §6 is about it.

## 5. Step 11 — the residual specification, with sign

Of the reservoirs considered, the source side is **over-supplied** and the sink side is
**short by two orders**. The residual is therefore not a source at all:

> **A surface reservoir exchanging CH₄ with the atmosphere in BOTH directions, at
> `≥ 3,820 t/yr` in each phase, phase-locked to the Martian season, with an effective
> atmospheric residence time of `0.944 yr` — 318× shorter than gas-phase photochemistry
> supplies. Areally that is `0.072 mg m⁻² day⁻¹` over the whole planet, two to three orders
> BELOW terrestrial microseepage (10–100 mg m⁻² day⁻¹), so the capacity is not the problem;
> the *sign alternation* is. Conditional on the Gale near-surface observable of §2.4 being
> real.**

**The sign is the specification.** A one-way sink of any strength cannot produce a periodic
signal: the same mechanism must remove `3,820 t/yr` for half a Mars year and return it for the
other half. Yung 2018 says this in prose — soil sequestration "produces a short lifetime for
CH₄ without actually destroying it" — and the ledger turns it into the number above and into a
state step 10's vocabulary does not have (§7).

## 6. The calibration against Yung et al. 2018, route by route

Yung 2018 is **full-text-read** (Europe PMC `PMC6205098`, fetched 2026-09-05) and is the
published synthesis this run is scored against. Five routes, four matches, one located divergence:

| # | Yung 2018 | This audit | Verdict |
|---|---|---|---|
| 1 | gas-phase lifetime `~300 yr` (Summers 2002, Atreya 2007) | used as input | shared input, not a match |
| 2 | "the lifetime has to be shorter than 1 year (Lefèvre and Forget, 2009)" | **`τ_eff = 0.944 yr`**, derived from the `0.24–0.65 ppbv` amplitude alone | **MATCH**, and independently derived |
| 3 | IDP/meteoritic UV models "predict mean background levels of about 2.5 ppbv, some five times larger than that observed by TLS" | `2.5/0.41 = 6.1×`; ledger reads it as `A = 0.164`, i.e. **the source is over-sufficient by 6×** | **MATCH** on magnitude and direction |
| 4 | approximating the `~7 ppbv` spike "required a lifetime of 1 month with a source strength of **75,000 t/year** (`5×10⁹ mol/year`)" | global-burden arithmetic gives **`7.36×10⁵ t/yr`** | **DIVERGENCE ×9.8** — and it is *located*: theirs is a **local** Martz-crater source producing a local 7 ppbv; ours treats 7 ppbv as globally mixed. **F3 exactly** — the whole factor is the aperture |
| 5 | enhanced H₂O₂ "unlikely because the hypothetical oxidants will also oxidize CO and H₂" | `SURVIVES` the ledger, `RULED OUT` externally | **PROCEDURAL DIVERGENCE** — the audit's leg cannot fire on a free-scalar sink; **F4** |

Row 4 is the useful one. It is the first case in this project where an `A`-style divergence
from a published synthesis is **fully explained by the aperture**, and the explanation is
checkable: `9.8 ≈` the ratio of a plume's footprint to the planet.

## 7. Does a sink residual behave differently from a source residual? Yes — a new output shape

**Claim: on this input the instrument is an exclusion instrument on the sink side and not an
instrument at all on the source side.** Three differences, all visible in §4's table:

1. **The source leg's aperture is free; the sink leg's is fixed by the observable.** F3 says
   `P_avail` depends on an assumed coupling cross-section and that assumption is free. For a
   *source* on Mars the aperture is an emitting area with no upper bound short of the planet, so
   any source can be made to pass — serpentinisation at `A = 0.025`, IDP at `0.164`, and a
   biological source at whatever you like. For the *photochemical sink*, `P_avail = burden/τ`
   and **both terms come from the observable**. There is nothing to tune. Every `SURVIVES` in
   the SOURCE block is therefore uninformative and the single `RULED OUT` in the SINK block is
   the only reproducible result on the page.
2. **A source residual is one-signed; a periodic observable's residual is two-signed.** C11's
   flyby residual needed *both signs* and that was treated as a special constraint. Here it is
   structural: any observable that returns to its starting value demands a reservoir that is
   alternately source and sink at equal magnitude. Step 10's five states — `RULED OUT`,
   `SURVIVES`, `NOT FORMABLE`, `NOT TESTED`, plus C46's `NO RESIDUAL` — have no word for it.
3. **The spike row is a reductio, not an exclusion.** `A = 1.9×10⁷` on the 2019 spike does not
   rule out photochemistry; it rules out the *reading of the observable as global*. An `A` that
   large is the instrument reporting that the observable was mis-specified in step 1, which is a
   diagnostic the procedure does not currently name.

### Proposed additions — **PROPOSED ONLY**, not written into `reservoir-audit.md`

`vault/method/reservoir-audit.md` is held by another agent this session. These are offered for
Part D and the F-list, unapplied:

- **F10 — the source leg has a free aperture and the sink leg does not.** On a mass-budget
  input the required *source* flux can be supplied by any reservoir given enough emitting area,
  so `A ≤ 1` on the source side carries no information; the *sink* side's `P_avail` is
  `burden/τ`, fixed by the observable, so its `A` is reproducible. **On a mass budget, run the
  sink leg first, and report source rows as `NOT DISCRIMINATED` rather than `SURVIVES`.**
  Found by C49, where every source passes and one sink fails by 319×.
- **A sixth step-10 state, `EXCHANGE REQUIRED`.** When the observable is periodic, the residual
  is a two-way reservoir, not a one-way source or sink, and its specification carries a phase
  and a sign alternation as well as a magnitude. `SURVIVES` misdescribes it.
- **A fourth step-0 condition, `UNREPLICABLE OBSERVABLE`.** C49's surviving observable is not
  zero-consistent (D.2) and not pipeline-split (D.3): it is a single instrument on a single
  vehicle whose records **no second team has ever reduced**, so step 0(b) cannot be run. Part C's
  step-0 table should carry the state and the rule that a run past it is conditional in the D.3
  sense.
- **A step-1 diagnostic for `A ≫ 10⁴`.** An `A` of `1.9×10⁷` reports a mis-specified observable
  (local read as global), not a ruled-out reservoir.

## 8. Honesty

**The blind is single-agent.** The brief was written and hashed by the agent that ran it, per
`audits/blind-brief-c49-2026-09-05.md`. That removes pre-announcement contamination — nothing in
the brief names a verdict, a halt, or a D-class — but it does not remove recognition, and Mars
methane is a case an agent can recognise. **Weaker than the two-agent blind D.3a asks for**, and
weaker than C46's on a further count: C46's case was textbook and closed, this one is open, and
the case-line numbers themselves came from the brief rather than from a fetched paper.

**The C30 lesson, applied to this note's own margins.** C30 found that three of its rows were
Bains et al.'s own stated margins re-divided, so agreement there was tautological. Here:

- **Tautological rows.** The photochemical sink's `P_avail = burden/300 yr` and the required
  `R_ss` are the *same division of the same two numbers*; row 1 of §6 is an input, not a match.
  The IDP row is Yung's own model output re-divided by Yung's own lifetime — §6 row 3 agrees
  with Yung because it *is* Yung. **Two of five calibration rows are tautological.**
- **Genuinely independent rows.** `τ_eff = 0.944 yr` (§6 row 2) is computed from the amplitude
  and the Mars year, and nothing else; the `×9.8` aperture divergence (row 4) is a real
  disagreement with a published number, located. **Two rows.**
- **Others' numbers, re-divided but not re-derived.** Every availability figure in §4 is Oehler
  & Etiope's or Yung's, converted. No photochemical model was run, no spectrum re-reduced, no
  boundary-layer calculation done.

**What was not obtained.** Webster 2018, Webster 2021, Moores 2019, Korablev 2019, Zahnle 2011
and Giuranna 2019 are **Crossref-verified for DOI, title, author, journal and date, but not
full-text-read** — Science, Nature, AGU and Elsevier paywalls. Rows 10 and 11 of §2 are the
reconciliation the whole step-0 verdict turns on and **neither was read**; that is the single
largest weakness in this note. The `0.41 ± 0.16`, `0.24–0.65`, `21 ppbv` and `<0.05 ppbv`
figures are the brief's, not a fetch. Yung 2018 and Oehler & Etiope 2017 **were** full-text-read
(Europe PMC, 2026-09-05) and every number attributed to them here is quoted from that text.

**What a Mars atmospheric chemist would attack first.** The single-box, well-mixed treatment,
and rightly — the same objection C30 records. `R = burden/τ` is exact only for one box, and the
entire reconciliation in rows 10–11 is that Mars is *not* one box near the ground at night. A
scalar `τ_eff` is a summary of a transport problem, and the `0.944 yr` should be read as "the
timescale a one-box model would need", not as a chemical lifetime.
