# G36/C35 adversarial review

Run 2026-09-05. Target: [[G36-wear-erosion-damage]] and [[C35-soil-ha]]. Brief: kill it if it can
be killed. Instruments this session: **OpenCitations** (`api.opencitations.net/index/v1/`,
citations *and* references endpoints), **Crossref** (`api.crossref.org/works/<doi>?mailto=…`),
**Europe PMC REST** (`ebi.ac.uk/europepmc/webservices/rest/search`, bare-quoted, plus
`fullTextXML`), **WebSearch**, **WebFetch**, and local PDF text extraction. **Semantic Scholar
`graph/v1/paper/search` returned `total: null` on 7 of 8 queries** (rate-limited); the
`graph/v1/paper/DOI:` endpoint worked and was used for record verification. The prior-art leg is
therefore Europe PMC + WebSearch + OpenCitations, matching the `audits/g34-adversarial.md`
standard but not the C5 §11 bar. Stated, not hidden.

---

## Verdict

**NARROW — and one leg dies.**

- **Leg 1 (Archard ↔ soil detachment): NARROW, grade LOCATED, topology `mediated` not
  `disjoint`, `crosses` demoted formalism(4) → metaphor(2).** The zero is real but it measures a
  far smaller absence than the note claims. Earth-surface science has *already* imported
  Archard's law by name: **Hsu, Dietrich & Sklar** write `e_v = kWx/H`, cite Archard 1953 in the
  reference list, name "the literature of tribology" as their source, and add an impact-wear +
  surface-fatigue term (attack 3, **HIT**). And Europe PMC returns **41** `"Archard" AND "soil"`
  papers, including Archard applied literally to soil (`10.3390/ma12132180`) and a *biomimetics*
  paper on low-wear tillage sweeps. The defensible absence is narrow and specific: **tribology
  cites soil as the *abrader* and never as the *abraded*.** That is worth saying; "soil science
  has never once cited them" is not, as written, true of the earth sciences.
- **Leg 2 (Miner ↔ wet–dry aggregate breakdown): KILL.** The damage variable is **not
  monotone**. In one open-access primary source read this session (PMC12907374, 2026), MWD
  **decreased** with successive wetting–drying cycles in bare soil and **increased significantly
  (P < 0.05)** in vegetated soil under the *same* cycling. Miner's `D = Σ n_i/N_i` is monotone
  non-decreasing by construction and carries no repair term. A system whose "damage" runs
  backwards under one treatment is a **two-rate balance**, not cumulative damage — i.e. it is
  [[C6-damage-healing-ratio]]'s `Ha`, which this vault already owns (attack 2, **HIT**). G36's
  "What would close it" item 3 (a Weibull/Miner β for aggregate stability) is **misspecified as
  written** and should not be run in that form.
- **C35 §5, the T-value "prediction": REDISCOVERED.** T *was* set from an assumed formation rate,
  the discrepancy with measured production *is* published, and the ratio is **computable from
  the headline numbers of a 675-citation review** (attack 1/4, **HIT**).
- **C35 §3, the land-use `Ha` table: REPACKAGED at best.** Evans *et al.* 2020 (ERL, CC-BY)
  compiled **10,030 plot-years from 255 sites**, converted t/ha/yr → mm/yr through bulk density
  exactly as C35 §1 does, divided by a ¹⁰Be soil-formation rate, and reported the result by
  management class. C35's dataset (Montgomery's Table 1) is a subset of the same literature and
  smaller (attack 1, **HIT**).
- **Arithmetic: clean.** Every conversion in C35 reproduces exactly (attack 5, **NO HIT**) —
  but the `T` *range* C35 uses contradicts its own primary source (attack 4b, **HIT**).

**Four hits, as in G34.** The note is not fraudulent and the instrument is sound; the claims sit
one to two rungs above what the evidence carries.

---

## Attacks

### 1. Prior art on the ratio — **HIT. The T-vs-formation comparison is a literature, not a gap.**

Europe PMC, bare-quoted (the `FULL_TEXT:` field-prefix trap from `audits/g34-adversarial.md` was
avoided), `format=json`, 2026-09-05. Calibration first: `"soil formation"` → **2,794**, so the
soil side is findable on this index.

| # | Query (verbatim) | Hits |
|---|---|---|
| C1 | `"soil formation"` | **2,794** (calibration) |
| 1 | `"soil loss tolerance"` | **42** |
| 2 | `"soil erosion" AND "soil formation rate"` | **23** |
| 3 | `"tolerable soil erosion"` | **12** |
| 4 | `"net soil loss" AND "formation"` | **15** |
| 5 | `"exceed" AND "soil formation rate"` | **8** |
| 6 | `"soil production function"` | **6** |
| 7 | `"tolerable soil loss" AND "soil formation"` | **3** |
| 8 | `"erosion rate" AND "soil production rate"` | **2** |
| 9 | `"soil sustainability" AND "formation rate"` | **2** |
| 10 | `"erosion exceeds" AND "soil formation"` | **2** |
| 11 | `"soil loss tolerance" AND "soil production"` | **1** — *and it is Montgomery 2007 itself* |
| 12 | `"soil lifespan"` / `"soil lifespans"` | **1** / **1** (Europe PMC is thin here; see below) |
| 13 | `"soil budget" AND "production rate"` | **1** |
| 14 | `"T value" AND "soil formation rate"` | **0** |

**Nothing is zero on the substantive formulations.** The hits are the claim: Sci Rep 2025,
*Exploring the relationship between annual soil loss and formation rate in different land use
scenarios* — which is C35 §3's table, by land use, with a machine-learning wrapper; Heliyon 2023,
*Soil loss tolerance in the context of the European Green Deal*; Agric. Ecosyst. Environ. 2011,
*'Tolerable' hillslope soil erosion rates in Australia: linking science and policy*.

**Three primary anchors verified and read.**

1. **Verheijen, Jones, Rickson & Smith 2009, *Tolerable versus actual soil erosion rates in
   Europe*, Earth-Sci. Rev.** DOI `10.1016/j.earscirev.2009.02.003` — **Crossref-verified**
   2026-09-05, title and journal exact, `is-referenced-by-count` = **595**; Semantic Scholar
   `citationCount` = **675**; OpenCitations citer set = **591**. Content confirmed by WebSearch
   (the Cranfield green-OA PDF is behind Anubis bot protection and could not be read in full —
   **VERIFIED-SECONDARY**): *"the upper limit of tolerable soil erosion, as equal to soil
   formation, is approximately 1.4 t ha⁻¹ yr⁻¹ while the lower limit is approximately 0.3 t ha⁻¹
   yr⁻¹"*, and *"actual soil erosion rates for tilled, arable land in Europe are, on average, 3
   to 40 times greater than the upper limit of tolerable soil erosion."* **This paper does
   exactly what C35 §5 claims is unsaid: it defines the tolerable rate as the formation rate,
   measures the formation rate, and publishes the ratio to actual erosion.**
2. **Evans, Quinton, Davies, Zhao & Govers 2020, *Soil lifespans…*, ERL 15:094 (DOI
   `10.1088/1748-9326/aba2fd`, CC-BY, abstract read in full via S2; body via WebFetch).**
   10,030 plot-years, 255 sites; erosion converted to mm/yr through bulk density; soil formation
   **0.053 ± 0.005 mm/yr** from 264 ¹⁰Be measurements; result reported as a *lifespan* (30 cm ÷
   net rate) rather than as `Ha`, with **16% of conventional soils < 100 yr** and **39% of
   conservation soils > 10,000 yr**. `1/Ha` and a lifespan are the same information under a
   fixed profile depth. **This is C35 §3, on a dataset ~40× larger.**
3. **Montgomery 2007** — C35's own load-bearing source. Text-extracted from the author-hosted
   PDF this session and grepped. It already contains the whole argument: *"erosion rates from
   conventionally plowed agricultural fields average 1–2 orders of magnitude greater than rates
   of soil production"* (abstract) and *"other researchers have expressed concern that T values
   themselves are set substantially higher than soil production rates, because of political and
   economic considerations (ref 34)"*.

**Co-citation check.** Montgomery 2007 (OC set **1,777**) × Verheijen 2009 (OC set **591**) =
**77 shared citers**. A 77-work co-citing population is not a gap; it is a subfield.

**Outcome.** The ratio-of-erosion-to-formation comparison is mainstream soil science with its
own review literature. C35 §5's headline is **REDISCOVERED**. What is *not* found anywhere is the
`Ha` **name** and the placement of soil beside PSII/bone/grid — but `Ha` is already graded
REPACKAGED in [[novelty-audit]], so that is axis construction, not a result.

### 2. Metaphor test on the two legs — **HIT on leg 2 (fatal), HIT on leg 1 (demotion)**

**Leg 1 — formalism or word?** C35 §4 has already done the honest work and shown that the
Archard functional form does not survive: Archard's resistance is a **divisor** (`V ∝ 1/H`),
WEPP's is a **subtraction** (`D ∝ τ − τ_c`); `K_soil` is not a constant, is 0 at `τ = τ_c`, and
sweeps orders of magnitude within a single soil just by varying `τ`. Archard's `K` is also not a
"fitted dimensional constant" in the same sense — it is a **probability that an asperity contact
produces a wear particle**, a mechanistic quantity with a physical interpretation; WEPP's `K_r`
is a shear-excess slope in s/m with no such reading. Once the functional form, the dimensions,
and the mechanistic interpretation have all failed, **what remains is the observation that both
fields have empirical constants they cannot predict.** That is true, and it is a *word*-level
correspondence — `crosses: metaphor` (rank 2) at most, not `formalism` (rank 4). The note's own
§4 is the evidence against its own `crosses-rank`.

**Leg 2 — cumulative damage or reversible equilibrium? Decided: equilibrium.**

- *Cumulative-cycle law, found:* PMC12907374 (Front. sci., 2026, open access, full text read via
  Europe PMC `fullTextXML`) — **bare** soil: *"the MWD of bare soils decreased significantly with
  the successive wetting-drying cycles (P < 0.05). Specifically, the proportion of large
  aggregates (>1 mm) gradually decreased with increasing wetting-drying cycles."* Progressive,
  not first-cycle-dominated. Leg 2's own discriminator ("a soil still losing stability at cycle 5
  is not slaking") passes here.
- *Recovery between cycles, found — in the same paper:* **vegetated** soil, same cycling
  protocol: *"The MWD of vegetated soils increased significantly during the process of
  wetting-drying cycles (P < 0.05)."* Corroborated across the wider literature (WebSearch,
  2026-09-05): fast-wetting MWD reported **up 5–36% after the first two cycles then down 15–44%
  after 15**; 1–2 mm aggregates described as *"in the dynamic equilibrium state between the two
  reverse processes."* Denef 2001, one of the note's own B-anchors, is itself a paper about
  dry–wet cycles **stimulating** aggregate formation via microbial and POM dynamics.

**Decision.** The slaking objection was the wrong objection. Leg 2 does not die on
first-cycle dominance — it dies on **sign**. `D = Σ n_i/N_i` is monotone non-decreasing and has
no repair term; a state variable that rises under one treatment and falls under another, driven
by two opposed processes running simultaneously, is a **rate balance**. The correct formalism for
wet–dry aggregate dynamics is not Miner. **It is `Ha = k_r/k_d` — the object [[C6-damage-healing-ratio]]
already defines.** So the second leg of G36 collapses into the first computation, and the
"unread fatigue law" framing is removed rather than repaired. A Weibull β fitted to MWD-vs-cycle
would be fitting a shape parameter to a non-monotone series, which is a category error and would
have produced a number.

### 3. Citation anchors and mediators — **HIT. The topology is `mediated`, not `disjoint`.**

**Are the soil anchors right?** Yes. Le Bissonnais 1996, Denef 2001 and Amézketa 1999 are what a
soil physicist cites for aggregate breakdown mechanics; Nearing 1989 is the WEPP process paper.
No complaint here — the anchor *choice* is sound and the OpenCitations sets re-derived cleanly
(Archard 6,803; Nearing 1,122; Meng 767; all matching the note).

**Would a tribologist cite Nearing 1989?** No, and that is the point — but it is also why the
zero on that cell is unsurprising rather than informative. The informative question is whether
*anyone* bridges wear formalism and earth-surface material removal, and the answer is yes.

**Mediator hunt — OpenCitations, 2026-09-05.** Sklar & Dietrich 2001, *Sediment and rock strength
controls on river incision into bedrock*, Geology 29:1087, DOI
`10.1130/0091-7613(2001)029<1087:SARSCO>2.0.CO;2` — **Crossref-verified**, `is-referenced-by-count`
= **437**, OC citer set = **706**. Its erosion law goes as **1/(tensile strength)²** — a wear law
with the resistance as a *divisor*, i.e. Archard-shaped, and **not** WEPP-shaped.

| pair | O |
|---|---|
| Sklar & Dietrich 2001 × **Archard 1953** | **1** |
| Sklar & Dietrich 2001 × **Meng & Ludema 1995** | **1** |
| Sklar & Dietrich 2001 × **Nearing 1989** | **1** |
| Archard 1953 × Nearing 1989 | 0 (confirmed, as G36 reports) |
| Montgomery 2007 × Archard 1953 | 0 |

The three ones were **inspected, not counted** (Crossref metadata pulled for each):

- `10.1103/physreve.88.032205` — *Erosion dynamics of a wet granular medium*, **Phys. Rev. E**
  88:032205 (2013). Cites Sklar & Dietrich **and** Archard **and** Meng & Ludema.
- `10.1016/b978-0-444-53802-4.00124-x` — *Landscape Evolution*, **Treatise on Geophysics** (2015).
  Cites Sklar & Dietrich **and** Nearing.

**So a two-hop path exists: Archard → {granular-erosion physics, bedrock incision} → landscape
evolution → Nearing/WEPP.** `topology: disjoint` with an empty `mediator:` field is wrong.

**And the direct hit.** The Hsu/Dietrich/Sklar bedrock-erosion work (JGR Earth Surf. 113:F02001,
2008, DOI `10.1029/2007JF000778`, Crossref-verified, 61 citations; the dissertation version
`escholarship.org/content/qt55v19271` was downloaded and text-extracted this session) writes
Archard's law out in full, **twice**, verbatim:

> *"Sliding wear (all-slip) is described by Archard's Law, `e_v = kWx/H`, where `e_v` is eroded
> volume, `k` is a nondimensional wear coefficient dependent on the materials in contact, `W` is
> the applied load, `x` is the sliding distance, and `H` is the hardness of the surface being
> worn away."*

with `Archard, J. F. (1953), Contact And Rubbing Of Flat Surfaces, Journal Of Applied Physics
24(8), 981–988` in the reference list, four separate uses of "tribology" (*"the literature of
tribology (the study of wear, friction, and lubrication) contains abundant examples…"*), an
explicit **surface-fatigue** wear mode (*"the large boulders impact the bedrock channel, causing
abrasion and surface-fatigue wear"*), and citations to the slurry-erosion wear literature
(Elkholy 1983; Gandhi 1999; Tian 2005). It cites **no** WEPP, **no** Nearing, **no** USLE
(grep: 0 hits for all three).

**Europe PMC, `"Archard" AND "soil"` → 41 hits**, e.g. *Forecasting the Wear of Operating Parts
in an Abrasive Soil Mass Using the Holm-Archard Model* (Materials 2019, `10.3390/ma12132180`),
*Simulation and experimental study on frictional wear of plough blades in soil cultivation*
(Biosyst. Eng. 2024), and *Parameter Optimization and DEM Simulation of Bionic Sweep with Lower
Abrasive Wear* (Biomimetics 2023, `10.3390/biomimetics8020201`).

**Outcome.** G36's headline — *"soil science has spent the same eighty years measuring exactly
that on soil and never once citing them"* — is **false as written**. What survives, and is worth
the note, is a sharper claim: **tribology and agricultural soil-erosion modelling are disjoint,
mediated at two hops through bedrock-incision geomorphology; and in the whole
soil-meets-tribology literature soil appears as the *abrader* (tool wear) and never as the
*abraded body*.** That is a real, narrow, checkable absence.

### 4. The number — **HIT (a) and (b)**

**(a) `Ha ≡ 1` at `T` is the definition of `T`, and the "10–51×" clause is Montgomery's own
sentence.** C35 §5 is right that `T` sets `Ha ≡ 1` by construction — and the historical record
makes it stronger and simultaneously less novel: **`T` was set *from* an assumed production
rate.** WebSearch 2026-09-05 recovers the convention explicitly — *"a default SLTL value of
11.2 Mg ha⁻¹ yr⁻¹ … assuming a soil formation rate of 1 inch in 30 years"* — and the same
sources already run the comparison: *"soils form at a rate of 25.4 mm over 300 to 1000 years
(0.08–0.02 mm a⁻¹) … which significantly contradicts the '1 inch in 30 years' assumption."*
**That is C35's claim, published.** The arithmetic seals it (below): **T = 5 short ton/ac/yr =
11.21 t/ha/yr = 0.862 mm/yr = 1 inch per 29.5 years.** The top of the `T` range *is* the assumed
renewal rate, to within 2%. So the whole content of §5 reduces to *"the assumed P was wrong by
~10–50×"* — and Montgomery 2007 says 1–2 orders of magnitude in its abstract.

And the ratio **is** already numerically available: Verheijen 2009 publishes formation = tolerable
= **0.3–1.4 t/ha/yr**, against the conventional `T` of 5–12 t/ha/yr → **T/formation = 3.6–40×**,
bracketing C35's 10.1–50.7×. **One review, both numbers, one division.**

**(b) C35's `T` range contradicts its own primary source.** C35 takes `T` = 1–5 short ton/ac/yr =
2.24–11.21 t/ha/yr from *"NRCS technical-note and encyclopedia summaries"* (VERIFIED-SECONDARY).
But Montgomery 2007 — the note's VERIFIED-PRIMARY input, whose PDF C35 says it text-extracted —
states on the same page: *"soil conservation programs consider T values to be ~5–12 tons/hectare
per year, equivalent to ~0.41 mm/yr of erosion (assuming a soil bulk density of 1,200 kg/m³)."*
Montgomery's range is **5–12 t/ha/yr at ρ_b = 1200**, C35's is **2.24–11.21 t/ha/yr at
ρ_b = 1300**. Substituting Montgomery's own range into C35's own conversion gives
**0.385–0.923 mm/yr** and `T`/`k_r` = **22.6–54.3×**, not 10.1–50.7×. Neither range is wrong, but
a note that reads a source, quotes it as primary, and then uses a *different* secondary number
for the same quantity without saying so has a provenance defect. Montgomery also uses
ρ_b = 1200, not C35's ASSUMED 1300 — a source-consistent value was available and was not taken.

### 5. Units — **NO HIT. Every conversion reproduces.**

Recomputed independently, exact factor `1 short ton/acre = 907.18474 kg / 0.40468564224 ha =
2241.702 kg/ha`:

| C35 claim | recomputed | verdict |
|---|---|---|
| 1 t/ha/yr = 0.0769 mm/yr at ρ_b 1300 | 100/1300 = **0.07692** | ✓ |
| 2.8 t/ha/yr → 0.215 mm/yr | **0.21538** | ✓ |
| 1 short ton/ac/yr = 2.24 t/ha/yr = 0.172 mm/yr | 2.24170 t/ha → **0.17244** | ✓ |
| 5 short ton/ac/yr = 11.21 t/ha/yr = 0.862 mm/yr | 11.2085 t/ha → **0.86219** | ✓ |
| `T`/`k_r` = 10.1×–50.7× | 0.17244/0.017 = **10.14**; 0.86219/0.017 = **50.72** | ✓ |
| vs most generous `k_r` 0.083: 2.1× and 10.4× | **2.08** and **10.39** | ✓ |
| "1 in/30 yr" | 25.4/30 = **0.8467 mm/yr** | ✓ — **and note it equals `T` = 5 ton/ac (0.862 mm/yr) to within 1.8%**, i.e. 0.862 mm/yr *is* 1 inch per 29.5 yr |

The arithmetic leg of C35 is clean and re-derivable. The `1 in/30 yr` identity is the single most
useful number in the audit — it is the quantitative proof of attack 4(a).

### 6. Does the wear/fatigue framing give a soil scientist anything? — **Mostly no; one residue**

Working through what a soil scientist would actually *do* differently:

- *Leg 1's prediction ("both `K` and `K_r` span 4–6 orders and neither is predictable")* — C35 §4
  already shows the comparison is only legal at high `τ/τ_c` and must quote the `τ/τ_c` at which
  it was taken. What remains after that constraint is a **statement about the sociology of two
  fields' constitutive laws**, not a prediction about any soil. A soil scientist gets nothing
  actionable: knowing that tribology also fails to predict its coefficient does not change a
  `K_r` calibration.
- *Leg 2's prediction (organic binding → β ≈ 1–2, physical entrapment → β ≫ 1)* — killed by
  attack 2. The data it would be fitted to are non-monotone.
- **The residue, and it is real.** Attack 2's finding is itself the useful output, and it is a
  *correction*, not an import: **wet–dry aggregate dynamics should be modelled as a two-rate
  balance (breakdown vs re-aggregation) and reported as a ratio, not as a cumulative damage
  fraction or a single MWD endpoint.** That prediction *is* testable and the soil literature does
  **not** routinely make it — most wet–dry studies report an endpoint MWD, and the
  sign-reversal between bare and vegetated soil in PMC12907374 is reported as a curiosity rather
  than as evidence of two competing rates. Testable form: **in any wet–dry cycling series, MWD(n)
  should approach a treatment-specific asymptote `MWD_∞` set by `k_r/k_d`, approached from below
  in aggregating treatments and from above in degrading ones — so the sign of `dMWD/dn` at n = 1
  predicts nothing about `MWD_∞`, and a study reporting only cycles 1 and n can report the wrong
  direction.** That is a claim a soil physicist could falsify with three cycle points.

So: **the gap is real (the zeros re-derive), narrower than stated (attack 3), and largely empty
of a missing object (no importable formalism survives) — except that running the check produced
a correction to the soil side worth more than the import would have been.**

---

## What is actually new, if anything

Stripped to what survives all five hits:

1. **Nothing at the level of C35's §5 headline.** The `T`-vs-formation discrepancy is published
   with numbers in at least Montgomery 2007 (1–2 orders of magnitude), Verheijen 2009
   (formation 0.3–1.4 t/ha/yr, actual 3–40× the upper tolerable limit), and the SLTL review
   literature (the "1 inch in 30 years" assumption named and contradicted). **REDISCOVERED.**
2. **Nothing at the level of C35's §3 table.** Evans *et al.* 2020 computed erosion/formation by
   management class on 10,030 plot-years and reported it as a lifespan. **REPACKAGED** (the
   `Ha` *name* and the shared axis are the only differences, and `Ha` is already REPACKAGED).
3. **The mediator map is new to this vault and is a correction, not a discovery.** That
   Archard's law reached earth-surface science through bedrock incision and *not* through
   agricultural erosion modelling is a finding about the citation topology, and it makes the
   surviving absence statable in one honest sentence: **tribology meets soil only as the abrader,
   never as the abraded.** Grade **LOCATED**, and narrower than G36 currently claims.
4. **The leg-2 kill is the most valuable output of this review.** "Wet–dry aggregate breakdown is
   a two-rate balance, not cumulative damage, and the evidence is the sign reversal between bare
   and vegetated soil under identical cycling" is a genuine correction to the project's own
   posted plan, and it comes with a falsifiable prediction (§6 above) the soil literature does
   not make. Grade **CORRECTED**, plus a small **LOCATED**.
5. **`1 inch per 30 years` ≡ `T` = 5 short ton/ac/yr to within 1.8%.** A clean, checkable,
   re-derivable identity that makes the "T was defined as P_assumed" claim quantitative rather
   than rhetorical. It is arithmetic, so it is not novelty — but it is the sentence C35 should
   lead §5 with, replacing the ratio claim.

**Proposed overall grades.** G36: **LOCATED (narrowed)** — leg 1 only, mediated topology.
C35: **REPACKAGED (+CORRECTED)**, with §5 demoted to **REDISCOVERED**.

---

## Proposed edits (exact sentences)

*Text only — no vault note was edited by this agent, per brief. Mirrored in
`vault/PENDING-log-G36ADV.md`.*

**E1 — `G36` frontmatter.** `topology: disjoint` → `topology: mediated`;
`mediator: ` → `mediator: "bedrock-incision geomorphology (Sklar & Dietrich 2001; Hsu, Dietrich & Sklar 2008, which writes Archard's law out and cites Archard 1953)"`;
`crosses: formalism` / `crosses-rank: 4` → `crosses: metaphor` / `crosses-rank: 2`;
`standing: live` → `standing: narrowed`. Add `[[C35-soil-ha]]` stays in `computed-in`.

**E2 — `G36` epigraph, replacing "and soil science has spent the same eighty years measuring
exactly that on soil and never once citing them":**

> …and **agricultural** soil-erosion modelling has spent the same eighty years measuring exactly
> that on soil without citing them. The absence is real but it is not total and it is not direct:
> **bedrock-incision geomorphology imported Archard's law explicitly** — Hsu, Dietrich & Sklar
> write `e_v = kWx/H`, cite Archard 1953, and name tribology as their source — while citing no
> WEPP, no USLE and no Nearing. Two hops, therefore, not zero. And across the whole
> soil-meets-tribology literature (41 `"Archard" AND "soil"` papers on Europe PMC, 2026-09-05)
> **soil appears as the abrader — tillage tools, plough blades, slurry pumps — and never as the
> abraded body.** That, and not "never once cited", is the checkable absence.

**E3 — `G36`, replace "What would close it" item 3 in full:**

> 3. ~~A Weibull/Miner damage curve for aggregate stability against wet–dry cycle number~~ —
> **withdrawn 2026-09-05 (`audits/g36-adversarial.md` attack 2).** MWD is not a monotone damage
> variable. In PMC12907374 (2026), under identical wetting–drying cycling, **MWD decreased
> significantly in bare soil and increased significantly (P < 0.05) in vegetated soil**; the
> wider literature reports MWD rising 5–36% over the first two cycles before falling 15–44% by
> cycle 15, and describes 1–2 mm aggregates as being in *"dynamic equilibrium between the two
> reverse processes."* Miner's `D = Σ n_i/N_i` is monotone non-decreasing and has no repair term,
> so a Weibull β fitted to MWD(n) would be a shape parameter fitted to a non-monotone series.
> **The replacement object is [[C6-damage-healing-ratio]] applied to aggregates:** MWD(n) should
> approach a treatment-specific asymptote `MWD_∞` set by `Ha = k_r/k_d` (re-aggregation over
> breakdown), approached **from below** in aggregating treatments and **from above** in degrading
> ones. **Discriminating prediction: the sign of `dMWD/dn` at n = 1 does not predict `MWD_∞`, so
> any study reporting only cycles 1 and n can report the wrong direction of effect.** Needs ≥3
> cycle points; two-point papers must be excluded and said to be excluded.

**E4 — `G36`, replace the second numbered "Strongest objection" (leg 2, "slaking is not
fatigue"):**

> 2. *Leg 2 is not a fatigue problem at all, and the reason is not slaking.* The objection this
> note originally raised — that breakdown is first-cycle-dominated — **is not what the data show**;
> bare soils keep losing MWD through five cycles. What the data show is worse for the framing:
> the same protocol **raises** MWD in vegetated soil. Two opposed rates run simultaneously, so
> the state variable is not a damage fraction. **Leg 2 is withdrawn as a fatigue analogy and
> retained only as an `Ha` instantiation.** See `audits/g36-adversarial.md` attack 2.

**E5 — `C35` §5, replace the boxed Claim paragraph:**

> **Claim, restated after `audits/g36-adversarial.md` (2026-09-05) — REDISCOVERED, not new.**
> `T` was **defined from an assumed formation rate**, and the arithmetic proves it: `T` = 5 short
> ton/ac/yr = 11.21 t/ha/yr = **0.862 mm/yr at ρ_b 1300 = 1 inch per 29.5 years**, i.e. the
> Soil Conservation Service's "1 inch in 30 years" renewal assumption, to within 1.8%. So
> `Ha ≡ 1` at `T` is not a hidden convention this vault uncovered — it is `T`'s construction,
> and the entire content of the clause is *"the assumed production rate was too high by roughly
> an order of magnitude."* **That is already published**: Montgomery 2007's abstract says 1–2
> orders of magnitude; the soil-loss-tolerance review literature names the "1 inch in 30 years"
> assumption and contrasts it with measured 0.02–0.08 mm/yr; and **Verheijen et al. 2009**
> (Earth-Sci. Rev., DOI `10.1016/j.earscirev.2009.02.003`, Crossref `is-referenced-by-count` 595,
> 2026-09-05) sets tolerable ≡ formation at **0.3–1.4 t/ha/yr** for Europe and reports actual
> arable erosion at **3–40× the upper tolerable limit** — from which `T`/formation = 3.6–40×
> follows by one division, bracketing the 10.1–50.7× computed here. The ratio below is retained
> as **arithmetic on an established finding**, not as a prediction.

**E6 — `C35` §2, add to input row 8 (`T`):**

> **Provenance conflict, logged 2026-09-05.** Montgomery 2007 — this note's VERIFIED-PRIMARY
> source — states `T` = **5–12 t/ha/yr at ρ_b = 1200 kg/m³, ≈0.41 mm/yr**, which is *not* the
> 1–5 short ton/ac (2.24–11.21 t/ha) range taken here from secondary NRCS summaries. On
> Montgomery's own range and this note's ρ_b = 1300, `T` = 0.385–0.923 mm/yr and `T`/`k_r` =
> **22.6–54.3×**. Both ranges are defensible; using a secondary number for a quantity the
> primary source states, without saying so, is not. Montgomery's ρ_b = 1200 was also available
> and was not taken (§1 marks 1300 ASSUMED).

**E7 — `C35` §6, add a paragraph:**

> **The land-use `Ha` table is not the first of its kind.** Evans, Quinton, Davies, Zhao &
> Govers 2020 (*Environ. Res. Lett.* 15, DOI `10.1088/1748-9326/aba2fd`, CC-BY) compiled **10,030
> plot-years from 255 sites**, converted t/ha/yr to mm/yr through bulk density exactly as §1 does,
> divided by a ¹⁰Be soil-formation rate of **0.053 ± 0.005 mm/yr** (n = 264), and reported the
> result by management class as a **lifespan** — 16% of conventional soils below 100 years, 39%
> of conservation soils above 10,000. A lifespan at fixed profile depth is `1/Ha` up to a
> constant. §3's table is the same computation on a smaller dataset under a different name.

**E8 — `C35` §4, add one sentence at the end:**

> **And the mapping has already been made, in a neighbouring field, better.** Hsu, Dietrich &
> Sklar (JGR Earth Surf. 2008, DOI `10.1029/2007JF000778`) apply Archard's `e_v = kWx/H` to
> bedrock erosion by granular flows, decompose the basal force into a mean (sliding wear,
> Archard) and a fluctuating part (impact wear, Bagnold inertial stress), and add a
> surface-fatigue mode — all with tribology cited by name. §4's `K_soil` derivation is a
> reconstruction of a move geomorphology made in 2008.

**E9 — `vault/log.md`, newest first:**

```
## [2026-09-05] correction | G36 narrowed to leg 1 and mediated; C35 §5 regraded REDISCOVERED
```
with body: leg 2 withdrawn as a fatigue analogy (MWD non-monotone, sign reverses between bare and
vegetated soil under identical cycling — PMC12907374); `topology` disjoint → mediated via
bedrock-incision geomorphology (Sklar & Dietrich 2001 co-cited with Archard, Meng and Nearing;
Hsu/Dietrich/Sklar 2008 writes Archard's law out); `crosses` formalism → metaphor; the
`T`-vs-formation discrepancy located in Montgomery 2007, Verheijen 2009 and the SLTL review
literature; `T` = 5 ton/ac shown to equal 1 inch/29.5 yr; `T`-range provenance conflict with
Montgomery's own 5–12 t/ha/yr logged.

---

## What would settle it

Cheapest first.

1. **Read Verheijen 2009 in full.** It is the single document that most threatens C35 §5 and it
   was reached only through WebSearch this session (Cranfield green OA is behind Anubis;
   ScienceDirect 403). If its Table of formation rates prints a `T`-versus-formation ratio
   explicitly, §5 is REDISCOVERED beyond argument; if it stops at "3–40× the tolerable limit"
   without dividing `T` by formation, a thin sliver of §5 survives as arithmetic-not-stated. **1
   hour.** This is the highest-value outstanding item.
2. **Read Li, Du, Wu & Liu 2009, *An overview of soil loss tolerance*, Catena** (surfaced this
   session, not fetched). It is the review of `T`'s derivation and is where the "1 inch in 30
   years" provenance should be nailed to a primary citation rather than a WebSearch synthesis.
3. **Fetch one NRCS primary on `T`.** C35 concedes no handbook page was read; the provenance
   conflict in E6 cannot be resolved without one. NSSH Part 618 or the SSURGO `tfact` definition.
4. **Run the mode-6 decade-binned soil anchor G36 already owes** (Ellison 1947, Yoder 1936,
   Emerson 1967) — unchanged by this review, still the cheapest thing that could overturn the
   zero, and now more urgent because the surviving claim is narrower and rests on fewer cells.
5. **Test the E3 prediction on published data.** Denef 2001 and the Amézketa 1999 tables print
   cycle-resolved stability. Fit `MWD(n)` to a two-rate approach-to-asymptote in ≥3-point series
   and check whether the sign of `dMWD/dn` at n = 1 fails to predict `MWD_∞`. If it does fail,
   the project has a genuine soil-side prediction and leg 2 is worth keeping in the new form. **6
   hours desk.**
6. **Re-run the intersection with a geomorphology anchor in the B set** (Sklar & Dietrich 2001,
   Whipple 2004, Hsu 2008) as a *positive control on the mediator*. It should fire. If it does
   not, the mediated-topology claim above is itself wrong and should be retracted.
7. **Instrument debt.** Semantic Scholar `paper/search` was rate-limited (7/8 queries returned
   `total: null`) and OpenAlex was not called at all. The prior-art leg of attack 1 stands on
   Europe PMC (biomedical-skewed, thin on Catena/Geoderma/Soil Sci. Soc. Am. J.) plus WebSearch.
   A working S2 key would let this be re-run to the C5 §11 bar; until then attack 1's hits are
   sufficient to demote but the *completeness* of the prior-art picture is not established.
