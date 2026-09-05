---
name: C30-venus-phosphine-audit
type: computed
exit: specification
extends-to: astrobiology
---

# Venus phosphine, audited: the step-0 halt, and the conditional ledger behind it

> **Step 0 returns `NO AGREED OBSERVABLE` — and that is the audit's top-line output.** The
> 266.94 GHz feature is `~2σ` on re-reduction (Snellen 2020), bootstrap-insignificant
> (Thompson 2020), SO₂-degenerate at `1.32 km/s` separation (Villanueva 2021), and bounded at
> `<0.8 ppb` above 75 km (Cordiner 2022) — while the *claim* migrated from `20 ppb` (Greaves
> 2020) to `~1–7 ppb` after recalibration and to `~3 ppb at 5.7σ` from **Cordiner's own SOFIA
> data** (Greaves 2023 GRL Comment). A central value that moved `20×` under recalibration, and
> which two teams extract with opposite sign of significance *from the same photons*, is
> METHOD §5's same-method disagreement, not a measurement. **The audit halts.**
> Run **conditionally** — *if* 1 ppb above 55 km were real — `S_req = 1×10⁸ cm⁻² s⁻¹
> = 26 kg/s = 2.41×10¹⁰ mol/yr`, and every abiotic route fails the availability leg: volcanic
> `8×10³`, meteoritic `8×10⁴`, lightning `1.4×10⁵`, subsurface geochemistry `10⁸–10¹⁵`.
> **The exclusion list matches Bains et al. 2021's exactly. One row diverges, against Bains:**
> at their *own* extremal aperture (`τ ×10³`) the volcanic row falls to `A = 8`, which under
> [[reservoir-audit]] F7 is `NOT TESTED`, not `RULED OUT`. **And the biotic row `SURVIVES` the
> same ledger** (`A ≤ 1` on redox energetics and on required biomass) — a statement about the
> ledger's resolving power, not about life.

See [[reservoir-audit]] (Part C procedure, Part D.2 design, F3/F4/F7),
[[specification-instruments]], [[information-audit]] Part C, [[C11-flyby-reservoir-audit]] (the
output shape this note copies), and — same claim class, diagnostic-test framing —
[[G31-biosignature-diagnostic-theory]], [[C28-biosignature-roc]].

All numbers fetched **2026-09-05**. Arithmetic: `_scripts/c30_phosphine.py`.

---

## 1. Step 0 — is there an observable to explain?

[[reservoir-audit]] Part D.2 predicts a fifth state, `NO OBSERVABLE TO EXPLAIN`, reached before
any enumeration when the observable is consistent with zero. Venus is the first real input on
which it is available.

| # | Result | PH₃ value | Line / instrument | Epoch | DOI | Status |
|---|---|---|---|---|---|---|
| 1 | Greaves et al. 2020, *Nat. Astron.* | **~20 ppb**, "quality up to ~15σ" | PH₃ 1–0, 266.9445 GHz; JCMT + ALMA | 2017 / 2019 | `10.1038/s41550-020-1174-4` | **VERIFIED** abstract, [arXiv:2009.06593](https://arxiv.org/abs/2009.06593) |
| 2 | Greaves et al. 2021, Addendum | **~1–7 ppb** after ALMA recalibration | same | same data | `10.1038/s41550-021-01423-y` | **VERIFIED-SECONDARY** (quoted in Cordiner 2022 §1) |
| 3 | Snellen et al. 2020, *A&A* | **~2σ**, "below the common threshold for significance"; the "12th-order polynomial fit … leads to spurious results" | ALMA 267 GHz | 2020 | `10.1051/0004-6361/202039717` | **VERIFIED** abstract, [arXiv:2010.09761](https://arxiv.org/abs/2010.09761) |
| 4 | Thompson 2020, *MNRAS Lett.* | bootstrap: **neither** low- nor high-order polynomial fit recovers a significant detection | JCMT 267 GHz | 2020 | `10.1093/mnrasl/slaa187` | **VERIFIED** Crossref + abstract |
| 5 | Villanueva et al. 2021, *Nat. Astron.* | **no evidence**; SO₂ `J=30(9,21)–31(8,24)` at **266.943329 GHz** contaminates | ALMA+JCMT | 2021 | `10.1038/s41550-021-01422-z` | **VERIFIED** abstract, [arXiv:2010.14305](https://arxiv.org/abs/2010.14305) |
| 6–7 | Lincowski 2021 ("consistent with mesospheric SO₂"); Akins 2021 ("Complications in the ALMA detection…") | no PH₃ needed | modelling; ALMA archival | 2021 | `10.3847/2041-8213/abde47`; `10.3847/2041-8213/abd56a` | DOIs verified; texts **NOT FETCHED** |
| 8 | **Cordiner et al. 2022, *GRL*** | **`<0.8 ppb`**, 99%, **75–110 km**; 4G2 `a = 0.74–0.77 ppb`; 4G1 `χ²` min at 2.3 ppb is only **1.5σ** | PH₃ `J=4–3`, 1067.2063 + 533 GHz; SOFIA/GREAT, 3 flights | **Nov 2021** | `10.1029/2022GL101055` | **VERIFIED** full text, [NTRS 20220015999](https://ntrs.nasa.gov/api/citations/20220015999/downloads/venusPH3_221017.pdf) |
| 9 | **Greaves, Petkowski & Richards 2023, *GRL* Comment** | **`~3 ppb`, "5.7σ candidate detection"**, from **the same SOFIA data**, bypassing "spectral artefacts … from non-essential calibration-load signals" | SOFIA/GREAT | Nov 2021 data | `10.1029/2023GL103539` | **VERIFIED** Crossref record + [arXiv:2211.09852](https://arxiv.org/abs/2211.09852) abstract |
| 10 | Frontiers review 2024 | JCMT-Venus campaign M22AL006: "new mm absorption evidence for phosphine … with high significance" — **no abundance given** | JCMT/Namakanui | 2022– | `10.3389/fspas.2024.1372057` | **VERIFIED** full text; **no peer-reviewed abundance paper found** (2026-09-05) |

### The step-0 verdict, stated explicitly

**`NO AGREED OBSERVABLE`.** Not quite D.2's `NO OBSERVABLE TO EXPLAIN`, and the extra word is
earned. D.2's design case is a central value inside its own error bar; Venus is worse in a more
instructive way — **the central value is a function of the reduction.** Rows 8 and 9 are *the
same photons*, same aircraft, same three November 2021 flights, reduced by two teams to
`<0.8 ppb` and to `3 ppb at 5.7σ`. Rows 1–2 are the same ALMA photons before and after
recalibration, differing `20×`. Row 3 shows the significance is carried by the order of the
passband polynomial.

Per METHOD §5 and [[reservoir-audit]] F6 — *same-method disagreements are systematics;
single-group claims resolve against the claimant* — the 266.94 GHz feature's amplitude is
**analysis-dependent at the level of the claim itself**, and there is no number here for a
source flux to be required to supply. **The audit halts; §2–§4 are conditional and labelled so.**
**What would un-halt it:** an amplitude stable across independently written, pre-registered
reduction pipelines, at a frequency where the SO₂ degeneracy (§4) does not live.

---

## 2. Conditional enumeration — *if* 1 ppb above 55 km were real

**The identity.** Steady-state mass balance in a well-mixed layer, `S = L = n(PH₃)·V / τ` —
bookkeeping, not chemistry: production equals loss regardless of mechanism.
`A ≡ S_req / S_i,max`; `A > 1` rules route `i` out.

**The required flux.** Bains et al. 2021 (`10.1089/ast.2020.2352`), verbatim from
[arXiv:2009.06499](https://arxiv.org/abs/2009.06499) (full PDF read this session): *"a flux of
~10⁸ phosphine molecules cm⁻² s⁻¹ (averaged across the whole planet) is needed to reproduce the
observed phosphine mixing ratio of 1 ppb above 55 km … equivalent to ~26 kg/second or ~8×10⁵
tonnes year⁻¹."* Converted here: **`2.41×10¹⁰ mol PH₃/yr`** (`26 kg/s ÷ 33.998 g/mol ×
3.1557×10⁷ s/yr`).

**The aperture is the lifetime.** [[reservoir-audit]] step 5 makes the coupling cross-section a
mandatory named row; here it is `τ`, the PH₃ lifetime, because `S_req ∝ 1/τ`. Bains, verbatim:
*"< 1 second in the high atmosphere (> 78–98 km)"*; in the UV-shielded deep atmosphere *"up to
10¹¹ seconds"*; transport-limited *"as high as ~400 years"*, or *"≤ 700 years"* on Bierson &
Zhang radical profiles. Nominal `S_req` uses the full photochemical model. **Scaling assumed:
`S_req ∝ 1/τ` exactly, so `A(2τ) = A/2` and `A(0.5τ) = 2A`** — linear by construction of the
identity, not an approximation, which is why the sensitivity line is two divisions.

### The ledger

`A = S_req / S_max`, fluxes in tonnes PH₃ per Earth year against `S_req = 8.0×10⁵ t/yr`.

| # | Abiotic route | Bounding source | DOI | Max available | **A** | A(2τ) | A(0.5τ) | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | **Volcanic outgassing of PH₃ directly** | Bains 2021 (Holland 1984): *"maximum production rate of phosphine on the early Earth is only ~100 tonnes per year"* | `10.1089/ast.2020.2352` | `1×10² t/yr` | **8.0×10³** | 4.0×10³ | 1.6×10⁴ | **RULED OUT** |
| 1b | *Same, via P outgassing* | Bains 2021 Fig. 9: *"few conditions require a total flux of less than 10⁹ grams of phosphorus per second"*; Earth's is *"~143 kg/second"* | same | `1.43×10⁵ g P/s` | **7.0×10³** | 3.5×10³ | 1.4×10⁴ | **RULED OUT** — agrees with row 1 to 14% by a separate calculation |
| 2 | **Volcanic phosphide (P³⁻) extrusion + hydrolysis** | Truong & Lunine 2021; rebutted on eruption rate by Bains 2022 (`10.1073/pnas.2121702119`) | `10.1073/pnas.2021689118` | extraordinary plume volcanism | **not computed** | — | — | **NOT TESTED** — neither PNAS paper fetched |
| 3 | **Lightning / electrical discharge** | Bains 2021: PH₃ *"produced by lightning in one Venusian year under some very optimistic assumptions is 3.5 tonnes … 5 orders of magnitude lower than … necessary"* | `10.1089/ast.2020.2352` | `5.7 t/yr` (3.5 t per 0.6152 Earth-yr Venus year) | **1.4×10⁵** | 7.0×10⁴ | 2.8×10⁵ | **RULED OUT** |
| 4 | **Meteoritic / cometary delivery of phosphides** | Bains 2021: 20–70 kt/yr accretion, 6% Fe/Ni, 0.25% P, hydrolysis *"100% efficient"* → *"~10 tonnes of phosphine … every year"* | same | `1×10¹ t/yr` | **8.0×10⁴** | 4.0×10⁴ | 1.6×10⁵ | **RULED OUT** |
| 5 | **Atmospheric photochemistry (H/P radical chains)** | Bains 2021: *"at least 5 orders of magnitude below the rate required"* | same | ≤`8 t/yr` | **≥1×10⁵** | ≥5×10⁴ | ≥2×10⁵ | **RULED OUT** |
| 6 | **Surface / subsurface geochemistry** | Bains 2021: crust/mantle f(O₂) *"8–15 orders of magnitude too high to support reduction of phosphate"* | same | ≤`10⁻³ t/yr` | **10⁸–10¹⁵** | /2 | ×2 | **RULED OUT** — widest margin on the ledger |
| 7 | **Tribochemical / mechanochemical (Glindemann)** | Bains 2021: scaled to global earthquake activity, *"at least two orders of magnitude too small"*; crust *"extremely desiccated with no local hydrogen source"* | same | ≤`8×10³ t/yr` | **≥1×10²** | ≥50 | ≥2×10² | **RULED OUT**, but the *narrowest* abiotic margin — see F7 note below |
| 8 | **Cloud-droplet photochemistry in H₂SO₄** | Bains 2021 §5.2: *"completely unknown"*; Frontiers 2024: an *"open option"*, *"uncertain by many orders of magnitude"* | `10.3389/fspas.2024.1372057` | **bounded by nobody** | — | — | — | **NOT TESTED** — the only genuinely unquantified abiotic row |
| 9 | **Large-impact transient reduced atmosphere** | Bains 2021: needs an impact ≥ the ~4.48 Ga terrestrial event; *"even the Chicxulub impactor … did not manage to significantly change the redox state"*; recurrence 50–100 Myr, no recent Venus crater on radar | `10.1089/ast.2020.2352` | epoch-excluded | — | — | — | **NOT FORMABLE** now |
| 10 | **Aperture inflation itself** (`τ ×10³`) | Bains 2021 Supp.: destruction assumed transport-only, surface→98 km at `K_z = 2200 cm² s⁻¹`, `T = 2.2×10¹⁰ s`; bound falls to **`1.3×10⁵ cm⁻² s⁻¹`** = 800 t/yr, *"~10⁻³ times the rate estimated from a full photochemical model"* | same | `S_req` falls `769×` | **volcanic A → 8.0** | 4.0 | 16 | **the row that bites — §3** |
| 11 | **The observable is SO₂, not PH₃** | Villanueva 2021; Lincowski 2021 | `10.1038/s41550-021-01422-z` | n/a | — | — | — | **NOT FORMABLE** |
| 12 | **The observable is a passband-fitting artefact** | Snellen 2020; Thompson 2020 | `10.1051/0004-6361/202039717` | n/a | — | — | — | **the step-0 row (§1)** |
| 13 | **BIOTIC — same ledger** | Bains 2021: reducing phosphate to PH₃ *"is not beyond that deployed by terrestrial biochemistry"* (NADH and two Fe–S proteins suffice, FADH₂ and ubiquinone do not); Lingam & Loeb 2020: required biomass *"orders of magnitude lower than … Earth's aerial biosphere"* | `10.1089/ast.2020.2352`; [arXiv:2009.07835](https://arxiv.org/abs/2009.07835) | not flux-limiting | **≤1** | ≤0.5 | ≤2 | **SURVIVES (as spec)** |

---

## 3. Exclusion — what falls, what is marginal, what survives

**Below `A = 1`:** none — every abiotic route with a published bound is *above* it, which is the
whole content of Bains' title.

**`RULED OUT` (`A > 1`, robust at 2× aperture):** volcanic (`8.0×10³`, `7.0×10³` independently),
lightning (`1.4×10⁵`), meteoritic (`8.0×10⁴`), photochemistry (`≥10⁵`), surface/subsurface
geochemistry (`10⁸–10¹⁵`) — all surviving the 2× row by three or more orders. These are the
exclusions the ledger actually earns.

**Marginal — the audit's own finding, not Bains':**

- **Row 7, tribochemical, `A ≥ 10²`.** Bains scale one laboratory result (Glindemann 2005b) to
  "plausible global earthquake activity" on a planet whose seismicity is unmeasured. Two orders
  on an unmeasured input is thin, and it holds only because a *separate, non-ledger* argument
  buttresses it (no crustal hydrogen source). **Recorded `RULED OUT`; the ledger alone gives
  `NOT TESTED`.**
- **Row 10 — the row the step-5 aperture rule was written for.** At Bains' *own* extremal
  aperture (`τ ×10³`), `S_req` falls to 800 t/yr and the volcanic `A` falls from `8.0×10³` to
  **`8.0`**, into `1 < A < 10` on contested inputs: under [[reservoir-audit]] F7 that is
  **`NOT TESTED`, not `RULED OUT`.** Bains reach the same destination differently — conceding
  the arithmetic and rejecting the *transport assumptions* as *"not physically plausible, or
  even self-consistent"* (a mechanism argument, and a persuasive one). **The divergence is
  procedural, not factual, and runs conservative** — the instrument declines an exclusion
  Bains asserts.

**`NOT TESTED`:** rows 2 (PNAS pair not fetched) and 8 (cloud-droplet photochemistry in H₂SO₄,
bounded by nobody). **`NOT FORMABLE`:** rows 9 (impact, epoch-excluded) and 11 (SO₂ — the
observable dissolves).

**`SURVIVES`: row 13, the biotic route — the availability leg does not exclude it.** Bains' own
thermodynamics puts the required reducing power inside the range of terrestrial biochemicals;
Lingam & Loeb's biomass requirement sits orders of magnitude *below* Earth's aerial biosphere.
`A ≤ 1` on both the energy and the standing-crop legs. **Per [[reservoir-audit]] F4, `A ≤ 1` is
necessary and never sufficient** — Bains spend pages on obstacles the ledger is blind to: water
activity, concentrated H₂SO₄ that *"rapidly destroys the large majority of terrestrial
biochemicals"*, membrane integrity against that gradient. **So the audit returns: of the routes
considered, this ledger excludes every abiotic route and does not exclude the biotic one — a
measurement of the ledger's resolving power, not evidence for life.** Same discipline as
`C11`'s dark-matter row: *specified, not endorsed*.

---

## 4. Residual specification — conditional on the detection

Of the routes considered, none supplies `S_req` at nominal aperture, so per Part C step 11 the
required coupling itself is the specification:

- **Magnitude.** `S = 1×10⁸ cm⁻² s⁻¹` planet-averaged `= 26 kg/s = 2.41×10¹⁰ mol/yr`, or the
  stoichiometric equivalent in a P³⁻-bearing precursor, in steady state.
- **Location.** The **53–61 km cloud layer** (Bains' detection altitudes), *not* the mesosphere:
  above 78–98 km the lifetime is `<1 s` and no abundance can stand there. That is what makes
  Cordiner's `<0.8 ppb` **75–110 km** limit less decisive than it reads — it bounds the wrong
  altitude for the claim, and the audit must say so.
- **The discriminating observable is not more PH₃ at 266.94 GHz.** Computed this session: the
  PH₃ `1–0` line at **266.9445 GHz** and the SO₂ `J=30(9,21)–31(8,24)` line at
  **266.943329 GHz** are separated by **1.17 MHz = 1.32 km/s** — comparable to the several-km/s
  line widths Villanueva et al. report. **At the resolutions flown the two species are not
  separable**, so more 266.94 GHz spectroscopy cannot resolve the case however long it
  integrates. That is the single most useful line in this note.
- **What does discriminate.** (i) The **vertical profile** — surface, cloud-layer and
  photochemical sources put PH₃ in three different places, and the 53–61 km vs 75–110 km split
  is already the seam where published results disagree; (ii) the **P-bearing companion
  inventory** (P₂H₄, P₄, PO), which no two candidate routes predict alike; (iii) **not
  isotopes** — ³¹P has no stable partner, so the discriminant must be molecular; (iv) **in-situ
  mass spectrometry on a descent probe** through 50–60 km, which measures (i) and (ii) at once
  and is the only non-degenerate entry on the list.

### The scoring — does the audit's exclusion list match Bains 2021's?

**Yes, on every row Bains bounds.** Their summary lists photochemistry (`≥5` orders),
equilibrium thermodynamics (`~100 kJ/mol` too costly), surface and subsurface chemistry
(`8–15` orders), volcanism, lightning, meteoritic delivery, tribochemistry and impacts — and
the audit, run from Bains' own fluxes with the `A`-ledger imposed on top, excludes exactly that
set and nothing else. **This is the Pioneer-style calibration result: the instrument reproduces
a published enumeration's verdict list, route for route.** Weaker than Pioneer's, because it
read the answer's own numbers rather than pre-resolution inputs — see §6.

**Three divergences, all of them procedural:**

| # | Bains 2021 | This audit | Why |
|---|---|---|---|
| D1 | Volcanism `RULED OUT` even at the extremal-`τ` scenario, rejected on physical grounds | **`NOT TESTED` at `τ ×10³`** (`A = 8.0`) | Step 5 makes the aperture a first-class row; F7 forbids a `1 < A < 10` exclusion on contested inputs. Bains' rejection is a mechanism argument the ledger may not make |
| D2 | Title: "cannot be explained by conventional processes" | **"of the routes considered"** | F2. Bains hedge in the body (*"every plausible … process"*), but the title is a verdict where the body is a specification — the failure mode this instrument exists to avoid |
| D3 | Biotic row at length; "not ruled out on thermodynamic grounds", inside habitability caveats | **`SURVIVES`, `A ≤ 1`, flagged F4** | Same conclusion as a ledger state, not prose. The gain: the biotic row sits *on the same table*, scored by the same rule |

**And one divergence Bains could not have made:** rows 11–12. They state plainly *"We have
assumed here that it is present, at ~1 ppb, and that presence requires an explanation."* Step 0
is the leg they deliberately did not run — why the two outputs are compatible, and why the
audit's top line is the halt, not the ledger.

---

## 5. Negative-control outcome — the first real datum for Part D

**The instrument did not return "nothing here" on its own: it was told.** The halt was named in
advance in `audits/scout-03-astrobiology.md` §Job 1 and restated in the commissioning
instruction, so it was executed, not discovered, and Part D's central question — *can this audit
produce a null unprompted?* — **remains unanswered.** What the run does establish is weaker and
still worth having: **the step-0 state is reachable and well-defined on a real, messy input**,
and it surfaced a class D.2 did not anticipate — not "a central value inside its own error bar"
but **"a central value that is a function of the reduction pipeline."** D.2 should be amended to
name it. A blind control still needs the K2-18b run, halt *not* pre-announced (2–3 h).

**Amended 2026-09-05:** that class is now [[reservoir-audit]] **D.3 / F8**, with the mandatory
step-0 reductions table, the `NO AGREED OBSERVABLE` halt, and — in D.3a — the record that this
run's halt was pre-announced and therefore contaminated, plus the blind-brief template the
uncontaminated test requires.

---

## 6. Honesty

**What this is.** Desk arithmetic on other people's fluxes. Every `S_max` in §2 is Bains et al.
2021's, read from their PDF and supplement; nothing was recomputed from primary thermochemistry,
no photochemical model run, no spectrum re-reduced. The unit conversions, the `A` divisions, the
`mol/yr` figure, the Venus-year normalisation of the lightning number and the 1.32 km/s
separation are the only quantities computed here.

**What it adds.** Three things, discipline rather than physics. (i) **The ledger form** — one
table, one ratio, one rule, with the biotic row scored like the abiotic ones; Bains reach the
same conclusions in prose across forty pages, and prose does not make row 13 commensurable with
rows 1–9. (ii) **The mandatory aperture sensitivity**, which turns Bains' own extremal-`τ`
scenario from a footnote into row 10 and shows the volcanic exclusion is not aperture-robust in
Bains' own numbers. (iii) **Step 0 run before the enumeration** — the leg Bains explicitly
declined, changing the headline from "no conventional process explains it" to "there is no
agreed *it*."

**What a Venus atmospheric chemist would attack first.** The `τ` treatment, and rightly.
`S_req ∝ 1/τ` is exact only for a well-mixed single box, and Venus is not one: the lifetime runs
from `<1 s` at 98 km to `~10¹¹ s` in the shielded deep atmosphere, so the real object is a
coupled transport–photochemistry profile and "the aperture" is a vertical function this note
collapses to a scalar. `10.1051/0004-6361/202142548` exists precisely because the PH₃
photochemical network is uncertain by orders of magnitude; a chemist would say every `A` here
inherits that, and the three-order exclusions are really one-to-two-order exclusions with a long
tail. **That moves no verdict** — the smallest robust abiotic `A` is `10²`, the largest `10¹⁵` —
**but it does move row 10, already the row this audit refuses to call excluded.** Second attack:
the exercise is conditional on an observable §1 says does not exist. True, and in the callout.

**Not obtained this session.** Lincowski 2021 (`10.3847/2041-8213/abde47`) and Akins 2021
(`10.3847/2041-8213/abd56a`) — DOIs Crossref-verified, texts not fetched, so the SO₂-degeneracy
claim rests on Villanueva's abstract and Cordiner's account of it. Truong & Lunine 2021 and the
Bains 2022 PNAS reply — neither fetched, so row 2 is `NOT TESTED` rather than scored. Bains
et al. 2022 *Nat. Commun.* (`10.1038/s41467-022-30804-8`) — not located under that DOI; the
biotic row therefore rests on Bains 2021 §biology and on Lingam & Loeb, whose DOI Crossref did
not return (cited by arXiv id). Greaves 2021 Addendum — not fetched; `1–7 ppb` is quoted from
Cordiner 2022. **No peer-reviewed JCMT-Venus re-detection paper with an abundance was found**
(searched 2026-09-05); the Frontiers review's "high significance" is a claim, not a number, and
§1 row 10 must not be quoted as a detection.
