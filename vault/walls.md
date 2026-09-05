---
name: walls
type: method
---

# Walls — what the vault hit that nobody has measured

> A **wall** is a specific, named, checkable thing that (a) the vault needed to finish a
> computation or close a claim, (b) does not exist in the literature as far as this project's
> searches could reach, and (c) is **not** a gap between two fields but an absence inside one —
> a measurement never made at the right conditions, a dataset never compiled, a theorem never
> proved for the relevant regime, a control never run, a rig never built.
>
> Paywalled-but-existing sources are **not** walls. They are access problems and sit in the
> appendix. The reach limit of every entry below is the vault's own: "unwritten in what we could
> reach," with `appears` carrying its full weight ([[novelty-audit]], the universal caveat).

**23 walls: 11 measurement · 7 dataset · 1 theorem · 3 control · 1 build.**

---

## 1 · Measurement — the number was never taken at the conditions that matter

| ID | Wall | Hit in | What it takes | What it settles | Publishable alone |
|---|---|---|---|---|---|
| **W-01** | **CH₄ adsorption enthalpy on a Mars regolith analogue at 180–240 K, under a 6 mbar CO₂ background, with `γ(T)` reported separately from `ΔH`** | [[C53-mars-exchange-feasibility]] §4 row 1, `audits/c53-adversarial.md` "What would settle it" #1, [[C49-mars-methane-audit]] | One cryostat, one quadrupole MS, JSC Mars-1 and a modern simulant (MGS-1). Weeks, one lab, no spacecraft | Whether Gale's seasonal CH₄ closes on regolith adsorption. Threshold to beat: **26.4 kJ mol⁻¹** on C53's ledger, 36 on Hu's | **yes** |
| **W-03** | **DMS photochemical lifetime `τ` on a K2-18b-like H₂/CO₂ atmosphere, from a photochemical model that includes CO₂** | [[C54-k2-18b-audit]] §"the residual is a demand on `τ`" | One published photochemical code, one run. Desk-scale | C54's inversion needs `τ ≥ 6.95×10³ yr` (`2.5×10⁶ ×` Earth's) for the biogenic-flux row to pass. Either the model reaches it or the biogenic reading dies | **yes** |
| **W-04** | **A soil production rate measured under agricultural land use** — every ¹⁰Be production rate in the literature is from a ridge crest, an undisturbed hillslope, or a basin outlet | [[C42-soil-ha-theory]] §7, [[C43-soil-ha-replication]] §"Production rates are from ridge crests", `audits/c43-adversarial.md` "What would settle it" #3, `blind-brief-c43` §6 | A ¹⁰Be soil-production campaign on cropped profiles, with coordinates. Field season plus AMS time | Whether `T`/`P` ≈ 22 is a real ratio or a land-use artefact. The direction of the bias is known (`P` biased up), the magnitude is not | **yes** |
| **W-05** | **`E(D)` — erosion measured as a function of soil depth through the vegetation-cover feedback** | [[C42-soil-ha-theory]] §3c: *"it needs `E(D)` measured, which no row here has"* | Paired erosion + depth + cover on a depth gradient, one lithology. Multi-year plot work | Whether `dD/dt = P(D) − E(D)` crosses twice, giving an unstable threshold depth `D_crit` — the one place soil is structurally richer than [[C6-damage-healing-ratio]], which denies `Ha = 1` is ever a collapse point | **likely** |
| **W-06** | **Threshold gravitropic angle `θ_min` as a function of statocyte/statolith number `M`, stimulated at multiple angles** — all published columella stimulation is at 90° and no series varies `M` against `θ` | [[C4-inclination-sensing-limit]] §10, §11.6, §11.7 (~10 formulations, **DOES NOT EXIST**) | Ablation series to `M` = {48, 32, 24, 16}, stimulation `θ` = 5–90°, ~500 roots, pre-registered bands. One plant lab, one season | The load-bearing discriminator: ratio **1.73** (pooling) vs **3.00** (linear summation) at `M` = 16. ≤1.25 means correlated noise. All three are results | **yes** |
| **W-07** | **A *fitted* cycles-to-failure distribution for any enzyme** — `β ≈ 1` is asserted from the geometric partition-ratio model and has never been fitted to a unit-lifetime distribution | [[C18-durability-axis]] §3 (`not recorded` estimator; "no fitted distribution exists"), §"What would overturn this" | Fit a Weibull to 3–5 existing single-molecule or time-resolved inactivation series. Desk, days | Whether the durability axis spans enzymes to appliances at all. `β > 1` overturns "batteries fail like enzymes" | **yes** |
| **W-08** | **`k_d` and `k_r` measured separately on one self-healing specimen** — materials science has no lincomycin, so damage and healing are never separated and only the composite `η` is observable | [[C6-damage-healing-ratio]] §4.3, §5 (two rows *deliberately* empty) | A vitrimer loaded below its topology-freezing `T_v` for `k_d`, above it for `k_r`, one specimen. Bench session | The first measured engineering `Ha`. If not separable, the barrier is confirmed experimental rather than conceptual — also a result | **yes** |
| **W-09** | **Cycles-to-failure for a latch contact surface under strike loading** — the field names the property and explicitly defers it | [[G12-latch-fatigue]] "What is specifically absent"; the 2023 *J. Exp. Biol.* LaMSA review defers it | Printed click-beetle latch, cam drive, 240 fps, ≥6 specimens, RH/T logged. Bench session | A Weibull fit that exists for the first time for any latch. Flat to 10⁵ cycles ⇒ not limiting — also publishable | **yes** |
| **W-10** | **Salt-hydrate cycle fade reported per cycle *and* per day separately** — the field's own review asks for the number and no paper separates the two clocks | [[G3-cycle-life]] | 50+ dehydrate/rehydrate cycles, protocol written first. Bench session | A fade number in the units the field asked for. Unmeasurable ⇒ state the floor | **likely** |
| **W-11** | **A Mars-wide bound on electrochemical / dust-storm (triboelectric) CH₄ destruction rate** | [[C49-mars-methane-audit]] §sink table: `NOT TESTED — no published Mars-wide destruction-rate bound obtained` | Chamber work on triboelectric CH₄ loss plus a global dust-activity scaling. Lab plus desk | Whether C49's `EXCHANGE REQUIRED` residual (≥3,820 t/yr each way, `τ_eff` = 0.944 yr) needs a surface reservoir at all | **likely** |
| **W-12** | **A residual hair-bundle offset `µ` for a named bullfrog saccular bundle** — the empty cell on the offset-from-threshold axis | [[C17-offset-from-threshold]], P-027 | Re-analysis of existing bundle recordings, or one fresh preparation. Days to a session | Whether the gain–bandwidth/offset framing has a biological anchor or is amplifier algebra only | **likely** |

## 2 · Dataset — the compilation was never made

| ID | Wall | Hit in | What it takes | What it settles | Publishable alone |
|---|---|---|---|---|---|
| **W-13** | **A published specificity — or an abiotic-route occurrence frequency — for any exoplanet biosignature detection.** No published numeric prior on the fraction of planets bearing detectable life exists in either anchor's framework either | [[C28-biosignature-roc]] §prevalence, §result note "the specificity values are illustrative, not measured" | A frequency among lifeless planets for each of the six published abiotic-O₂ routes (Meadows 2018). Modelling programme, months | Makes PPV computable. At prevalence 10⁻³ the required specificity is **0.999** — a mission-design number astrobiology does not have. Unestimable *is itself* C28's result | **yes** |
| **W-14** | **An open compilation of adult annual survival `φ` for small mammals.** AnAge carries `IMR` for 43 of 4,645 species and none of the frame | [[C40-setpoint-survival-test]] §3 | Aggregate published CMR studies into one species-level `φ` table. Months, one comparative-ecology group | Replaces C40's longevity proxy. `p` = 0.00014 rests on maximum longevity and falls to 0.059 without bats | **yes** |
| **W-15** | **Ring-recovery `φ` for resident temperate heterothermic birds** — *Calypte anna*, *Phalaenoptilus nuttallii* and kin. Also: **no avian compilation states homeothermy per species**, so no bird can be coded lever = 0 under a rule that refuses to infer absence | [[C52-setpoint-survival-ringing]] §4 | Non-European ringing/CMR programmes on resident heterotherms, plus a negative-record avian heterothermy compilation. Years for `φ`; months for the compilation | Whether the metabolic setpoint buys survival. **Verdict on C52's own question: the British empty treatment group is a fact about nature — migration and torpor are alternative solutions to the same deficit, so any migration-controlled design removes its own treatment arm. The wall is the missing non-British `φ` and the missing negative-record compilation, not the emptiness itself** | **yes** |
| **W-16** | **A per-site tolerable-loss (`T`) layer outside the United States.** SSURGO `tfact` has no counterpart anywhere; H2 was **not posable** in C44 for this reason | [[C44-soil-ha-world]] §6 | A national soil survey electing to publish per-polygon `T`. Institutional, not a project | Whether "numbers not defined from formation sit at 3–23×" is a US artefact. C44 already shows it is not, at national resolution | **likely** |
| **W-17** | **Mean core out-of-service time `T` for a remanufactured fleet** — core-out to successor-in-service. Caterpillar publishes mass flow with no installed base; the field's own KPI list has Lead Time and Cycle Time, neither of which is residence time | [[C31-remanufacturing-ha]] §4 | One ERP query at one remanufacturer, plus permission to publish. A session, if the door opens | Fills three empty rows and makes `A_circ ≤ r·y`, circularity's only ceiling theorem, testable. Unmeasurable anywhere ⇒ structurally unmeasurable, which is also the finding | **likely** |
| **W-18** | **≥10 regime shifts labelled bifurcation-vs-noise *independently of the early-warning indicator*** | [[C26-ews-hazard-shape]] §mechanism, P-030 | Mechanism adjudication by domain experts blind to the indicator, over an existing shift catalogue. Months desk | Revives or hardens the vault's best honest negative. Without it, every EWS validation is circular | **yes** |
| **W-19** | **A same-class physics-disagreement catalogue beyond 24 rows, with `same class` fixed before the outcome is read** | [[C16-same-class-catalogue]] §A20; P-107 records that "same method" is currently assigned post hoc, making the rule unfalsifiable as used | Extend the enumeration under a pre-committed apparatus/observable/pipeline codebook, second analyst blind to outcome. Desk, weeks | The conditional "same-class disagreements resolve to systematics" currently sits at 0 NEW-PHYSICS in 16–17 closed rows, 95% upper bound 0.17. More rows tighten or break it | **likely** |

## 3 · Theorem — never proved for the regime that is actually used

| ID | Wall | Hit in | What it takes | What it settles | Publishable alone |
|---|---|---|---|---|---|
| **W-02** | **A Whittle-index performance bound at `M` = 1, `N → ∞`, active fraction `α → 0`** — the regime every foraging application is in | [[C25-whittle-foraging]] §9.1, [[C45-whittle-network-sim]], `papers/charnov-gittins/paper.md` §Limitations 3 | Stochastic-control theory. Weber & Weiss 1990 fixes `α = M/N`; Hu & Frazier 2017, Zhang & Frazier 2021 and Gast, Gaujal & Yan 2023 all keep that hypothesis; Brown & Smith 2020 gives a finite-`N` certificate for one instance, not an asymptotic guarantee; the single-server queueing results are heavy-traffic limits with arrivals. **No located bound covers `α → 0`** | Whether the index is an approximation with a gap or a heuristic. Simulated, the gap at `M` = 1 is **negative** — −13.3% at the pre-registered `ν`, −0.5% at each policy's own optimum, in every sweep cell | **yes** |

## 4 · Control — designed, never run, and the claim rests on it

| ID | Wall | Hit in | What it takes | What it settles | Publishable alone |
|---|---|---|---|---|---|
| **W-20** | **An independent second coding of the vault's own 82 graded claims, with Cohen's κ per variable** | [[C51-vault-meta-analysis]] §5, `papers/audited-record/reviews/2026-09-05-referee-1-opus.md` ("Nobody was blind, and there was one coder … conceded and **not fixed**") | A different model, given the codebook and nothing else, double-coding 25–30% of rows. A day | Converts `move` — the paper's most-cited structural finding — from assertion to measurement | **no** |
| **W-21** | **The reservoir audit's D.2 negative control run on an unlabelled real null-result thrust paper, briefed by a different agent** — the run that exists used a case *labelled synthetic*, so it validates the wording of step 0(a), not the judgement. Also unrun: a **≈2.5σ** case where the significance line has to be argued | [[C50-reservoir-audit-d2-control]] §4, [[reservoir-audit]] Part D | Brief Tajmar et al. 2021 (`10.1007/s12567-021-00385-1`) on reported thrusts and uncertainties only, written by an agent that did not run it. Hours | Whether the instrument returns a null *unprompted* on a real input. Currently "returns nothing" is not yet a result | **no** |
| **W-22** | **An anonymised-case blind for the reservoir audit (D.3)** — the only D.3 datum is contaminated because the halt was pre-announced | [[reservoir-audit]] §D.3a | A case stripped of identifying frame, not told a halt is expected, not told which control it is. Hours | Part D's own question — *does it halt unprompted?* — is currently **unanswered**, and D.3 must not be counted as a passed negative control until it is | **no** |

## 5 · Build — the apparatus does not exist

| ID | Wall | Hit in | What it takes | What it settles | Publishable alone |
|---|---|---|---|---|---|
| **W-23** | **A controlled-refill artificial flower array** — interleaved flowers on two programmed refill rates, saturating regrowth with a linear-refill negative-control arm, `G_max` and `λ` matched by construction | [[C48-kadmon-regrowth-test]] §4 (P-088 **promoted from "clean version" to the only version**), [[C25-whittle-foraging]] §7 | Programmable feeder array, one pollinator system, one field season | The only surviving route to the 1.34× GUD prediction. Under Kadmon's *measured linear* renewal the two policies are indistinguishable and `dGUD/dc ≤ 0` — the opposite sign — so no collected dataset can test it | **yes** |

*(W-23 is also the only entry that is simultaneously a build and the sole remaining test of a
Layer-3 derivation; W-08, W-09 and W-10 need benches too, but their deliverable is a number, so they are counted as measurements.)*

---

## 6 · Ranking — cheapest **and** publishable on its own

1. **W-03 — DMS photochemical lifetime on K2-18b with CO₂.** One existing code, one run, a
   number the field is actively arguing about. Nothing to buy.
2. **W-07 — a fitted enzyme `β`.** Desk work on already-published inactivation series. Days.
   Either anchors a cross-class axis or kills it, and both are short papers.
3. **W-09 — cycle a latch to failure.** Printed part, cam, high-speed camera, six specimens.
   The number does not exist for any latch, and the review that defers it names the gap.
4. **W-01 — CH₄ adsorption enthalpy at 180–240 K.** One cryostat and a mass spectrometer.
   The ask is ten years old, in print, by name, and unanswered.
5. **W-23 — the controlled-refill flower array.** One season, modest hardware, and it is now
   the *only* possible test of the vault's one Layer-3 prediction.

W-06 (columella angular series) is the highest-value bench item and misses this list only on
cost: ~500 roots and an ablation protocol.

---

## 7 · Appendix — behind a paywall, not a wall

These exist. The vault could not read them. That is an access problem and must never be quoted
as an absence.

- **Kadmon 1992 (*Oecologia* 92:552) raw departure data** and **Kadmon & Shmida 1992** — both
  `is_oa = false`, 0 OA locations (Unpaywall, 2026-09-05); the latter not obtainable even as an
  abstract. [[C48-kadmon-regrowth-test]] §5. *One figure in one paywalled paper is the cheapest
  decisive move on that thread.*
- **The parid dusk–dawn tables** — Haftorn 1992, Lehikoinen 1987, Gosler 1996, both Bednekoff &
  Houston 1994, Houston & McNamara 1993: all JSTOR, none read. [[C38-reserve-margin-across-species]] §6.
- **Montgomery 2007 SI** (PNAS 403), **Heimsath 1997** and **Stockmann 2014** (OpenAlex
  `closed`), **Quarrier et al. 2023** supplement (GeoScienceWorld 403). [[C43-soil-ha-replication]].
- **Gough et al. 2010** *Icarus* 207:165 — paywalled; the 18 ± 1.7 kJ mol⁻¹ and its 115–135 K
  range are **VERIFIED-SECONDARY** in [[C53-mars-exchange-feasibility]]. **Ortiz et al. 2022**
  *Icarus* 385:115079 — not fetched.
- **Verheijen et al. 2009** (Cranfield green OA behind Anubis, ScienceDirect 403) and
  **Li, Du, Wu & Liu 2009** *Catena*. `audits/g36-adversarial.md`.
- **Griebling et al. 2026** — the only work citing Charnov 1976 + Gittins 1979 + the Gittins
  book; SD 403, no repository copy. [[C5-charnov-gittins]].
- **Held's remaining 21 per-commodity lifespan rows** — three publisher 403s.
  [[C27-product-lifespan-beta]].
- **Churchfield 1981** (shrew body fat) — 403 on every route.
- **DIISE** per-attempt island eradication records — no data endpoint, not a paywall and not a
  wall; a release decision. [[G37-adaptive-management-reliability-growth]].
- **Scopus / Web of Science / Semantic Scholar / Lens keys** — institutional or application
  barriers, listed here so no coverage hole is mistaken for a literature absence.
  [[citation-sources]].

---

## 8 · What it means

A two-day AI-run inquiry produced twenty-three named absences and no new law. That is the
correct outcome and it should be read literally, not as modesty. Finding that a number is
missing is cheap: it costs a search, a definition, and the discipline to write down what the
computation needed and did not get. Producing a law is expensive: it costs an apparatus, a
season, an institution, and years. This project ran the cheap operation at machine speed across
seven fields and returned exactly what that operation returns — a list of places where somebody
else's bench time is the binding constraint. Twenty-three walls in two days is a statement about
the cost asymmetry between searching and measuring, not about the instrument's power. Nothing on
this list becomes knowledge until somebody with a cryostat, a plant lab, a ringing scheme, or a
theorem does the part that cannot be automated, and the vault's own record says the same thing
from the other side: three novel results against roughly twenty repackagings, no claim ever
carried past Layer 2, and the most trustworthy file in the repository is the corrections log. A
register of walls is a work order for other people. It is not a contribution to any of the
fields it names.
