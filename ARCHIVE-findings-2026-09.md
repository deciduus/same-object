# Archived findings — snapshot to 2026-09

> **ARCHIVED. Superseded by `vault/00-index.md` on 2026-09-05.**
>
> - **Do not use this file for current standings.** The vault notes and `vault/00-index.md` are
>   canonical. Where this file and a vault note disagree, the vault note is right.
> - This file uses the **retired verdict vocabulary** — HOLDS / WEAKENED / COLLAPSED /
>   WITHDRAWN — preserved here as history. The live closed vocabulary is
>   `standing: live | narrowed | withdrawn | overturned`, enforced by `vault/_lint.py`. See
>   `vault/method/relationship-description.md` for why the old taxonomy was retired.
> - The **corrections log below has been migrated into `vault/log.md`** as dated entries marked
>   `[migrated from FINDINGS.md]`. That log is now the live one.
> - Renamed from `FINDINGS.md` on 2026-09-05 (backlog D14).

Status ledger as it stood in 2026-09. Every entry is either a measured gap, a finding with
numbers, or a closed item. Corrections were logged at the bottom rather than silently fixed.

---

## Confirmed gaps

A gap qualifies only if it passes the three-part test in `METHOD.md` §1. Co-citation
evidence is given where it was measured.

### G1 · Gradient coupling has no shared figure of merit
Dynamic soaring, solar sails, electrodynamic tethers, thermoelectrics, osmotic power,
evaporation engines and chemiosmosis all extract work by coupling to a pre-existing
gradient. Thermoelectrics have ZT. Nothing spans the class.

**Co-citation:** soaring ↔ osmotic = **0**. Soaring ↔ sails = **0**. Soaring ↔
thermoelectric = **0**. Sails ↔ osmotic = **0**. Thermoelectric ↔ osmotic = 2.

**The unread theorem exists.** Kedem–Caplan degree of coupling (1965) works for any two
conjugate flux–force pairs, and thermoelectric ZT is algebraically a special case:
q² = ZT/(1+ZT). Papers citing both it and the record thermoelectric material: **2**.

**Limit:** linear-response only, so it cannot reach dynamic soaring (nonlinear,
trajectory-dependent) or solar sails (no conjugate flux pair). Extending it is the open
problem.

### G2 · No metastability figure of merit
Energetic materials, nuclear isomers, phase-change storage and biological dormancy each
quantify the same stability-vs-performance geometry in their own vocabulary. No accepted
metric combines stored energy density, barrier height relative to kT, and triggerability.

### G3 · No cycle-life framework
Biology has catalytic-cycles-until-replacement. Industrial biocatalysis has total turnover
number — the same quantity, different name. Batteries have cycle life and fade rate.
Thermochemical storage has cyclic stability. Citation networks barely overlap.

**Where the neglect actually lives:** not batteries, where cycle life is a headline spec.
Thermochemical storage, where a celebrated result reads "stable for at least ten cycles"
while organic flow chemistries quote fade below 0.001% per cycle.

### G4 · Criticality as a design strategy - **DOWNGRADED**
Hair cells self-tune to a Hopf bifurcation for divergent gain. Parametric amplifiers are
biased just below threshold. Same law, two vocabularies — √G·B = κ and gain ∝ f^(−2/3).

**Downgraded from a field-level gap to a single-review omission.** A re-run found **99
papers** linking Hopf bifurcation to the cochlea, plus titles such as *Self-tuned regenerative
amplification and the Hopf bifurcation*. The claim that criticality-as-design is unconnected
across fields is false.

**Reference audit — CORRECTED.** It was reported here as *"a 578-reference Rev. Mod. Phys.
colloquium citing zero engineering, laser, MEMS or superconducting work"*, and promoted as
publishable as-is. The PDF was finally extracted (Muñoz, *RMP* 90:031001, via
arXiv:1712.04499):

- **595 references in the printed bibliography.** *(Corrected 2026-09-05: 578 is not an error —
  it is Crossref's publisher-deposited `reference-count` for this DOI,
  `https://api.crossref.org/works/10.1103/RevModPhys.90.031001`, fetched 2026-09-05. Deposited
  list and printed bibliography are different objects. The real defect was that the number was
  quoted with no provider, endpoint or fetch date. See `vault/log.md`.)*
- **The bibliography has no article titles at all** — only venues. Every subject-keyword
  characterisation of it was reading data that is not there.
- **Five IEEE entries**, so "zero engineering" is false as worded. Zero laser / MEMS /
  superconducting / photonic / sensor entries *by venue* is true.
- The review cites Stoop's Hopf-bifurcation theory papers (PRL 2003, PRL 2016) and omits his
  **cochlea hardware** — a sharper and stranger finding than a blanket absence.

The unverified figure had propagated into five files before anyone opened the source. See
`METHOD.md` §2 for the precondition now imposed on reference-list audits.

**Also refuted:** the surviving sentence "that specific question appears unasked." *Sensors*
11:5808 asks it as one question — *"The aim in the design of natural and artificial sensors is
mainly the implementation of signal sensitivity... Behaviors of that sort are common in systems
close to bifurcations."* Engineering's name for the class is **Lur'e systems**, a term this
project never searched.

**What survives:** only the missing *shared figure of merit* for offset from threshold. Cortex
sits at m ≈ 0.98, not 1; amplifiers are biased just below. Both fields know to sit near the
bifurcation. Neither has a number saying how far, comparable across the two.

### G5 · No dimensionless repair number
Biology quantifies repair as a **rate**. Engineering quantifies healing as an **amplitude
fraction** — roughly 75% toughness recovered, with no time in it. Not commensurable.

**Two unread frames.** Availability A = MTBF/(MTBF+MTTR) is structurally identical to the
photosystem repair steady state k_REP/(k_REP+k_PI); nobody computes an availability for
bone, gut lining or a leaf. And Kirkwood's disposable soma theory (1977) is the strongest
conceptual frame, unread by self-healing materials researchers.

Conventional durability design is the same axis with the repair term set to zero.

### G6 · Multifunctionality
Two mature quantified formalisms share one word. Engineering: sum of property ratios,
multifunctional above 1 (structural batteries score ~0.25). Ecology: a full N-function
formalism giving effective number of functions × average performance, ~926 citations.

**Co-citation: five OpenAlex queries returned zero shared citing papers.** The N-function
math engineering needs already exists, in a journal engineers do not read.

### G7 · How passive is it?
Passive dynamic walking, passive radiative cooling, morphological computation, compliant
mechanisms — six domain-local names, no shared name, no portable metric.

`"let physics do the control"` → 0 hits. `"morphological computation" "radiative cooling"`
→ 0.

**Re-run: HOLDS, with one crack.** All four domains calibrate strongly, and every crossing
is zero except passive dynamic walking against morphological computation, which returns
**2 real bridges** inside embodied robotics. The "six names, no contact" claim is slightly
overstated there.

**One sub-claim is UNVERIFIED.** The passivity ladder cannot be tested by term query -
`"degree of passivity"` returns 60 hits owned by corrosion science, control theory,
political history and psychology. Establishing its invisibility requires citation-tracing
the document's citers, and that lookup rate-limited before completing.

**Best find:** IAEA-TECDOC-626 (1991) already defines an ordinal degree-of-passivity
ladder, Category A (no signal inputs, no external power, no moving parts, no moving fluid)
through D. Invisible outside nuclear engineering. Generalized: *the fraction of the
response that survives when the actuation path is cut.*

**Hazard:** control-theoretic "passivity" is a homonym — a closed-loop dissipation
property fully compatible with active control.

### G8 · Energy per bit, one axis - **WITHDRAWN**
Neuroscience counts ATP molecules per bit. Chip design counts femtojoules per operation.
Biophysics counts kT per methylation cycle. Superconducting logic counts zeptojoules per
gate at 4 K. Nobody normalizes to kT.

**This finding is withdrawn.** `"Landauer" AND (neuron OR synapse OR brain)` returns **575**
papers, including titles such as *Using the Maximum Entropy Method to Obtain an Optimal
Bits-Per-Joule Neuron* and *Communication consumes 35 times more energy than computation in
the human cortex*. That is precisely the connection the finding claimed did not exist, and at
575 papers it is not a niche.

**What survives:** the *specific figure* built in this project - molecular, neural, CMOS,
superconducting and communication substrates on one kT-normalized axis with a per-decade band
separated out - may still be novel in that combination. But the claim "no cross-substrate
energy-per-bit axis exists" is false and has been removed from the figure.

### G9 · Discrepancy base rate
No cross-domain literature treats persistent inter-method disagreement as a class. The one
statistical framework ("dark uncertainty") is explicitly designed to *absorb* discrepancy
into an inflated error bar rather than interrogate it. Philosophy has the sharpest
statement of the hole: the standard defence is *robustness* — agreement across methods
validates — and there is no corresponding account of what to do when they disagree.

**WEAKENED - half of this was wrong.** Two literatures already treat inter-method
discrepancy as a class: metrology's **dark uncertainty** work (which models excess
between-method scatter as a class-level random effect) and **epidemiological triangulation**
(reasoning from agreement between methods with unrelated bias structures).

**What survives, and it is the important half:** nobody has computed the base rate. Every
query aimed at *how often such disagreements resolved to systematics versus new physics*
returns zero, and the dark-uncertainty literature inflates error bars rather than asking
historically what the discrepancies turned out to be. **No apparatus. All public data.**

### G10 · Sub-38.6 µm gravity
Below 38.6 µm, gravity at its own strength has never been tested. Below 1 µm, a force a
trillion times stronger than gravity would have escaped notice. The frontier moved only
56 → 38.6 µm in thirteen years; the blocker is electrostatic patch potentials —
engineering, not physics. The dark-energy length scale sits at ~85 µm, right where the
experiments run out.

### G11 · Plant gravisensing limits
A single statolith displacement costs only ~2–3 k_BT — marginally above thermal noise. The
limits-to-sensing analysis exists for chemoreception and photon counting. **No equivalent
paper exists for plant gravity sensing.** Physics set up, analysis missing.

### G12 · Latch cycles-to-failure - **WITHDRAWN**
Trap-jaw ant strikes show no decline in peak velocity over repeated use; fatigue appears in
the muscle, not the latch.

**WITHDRAWN.** Dirks, Parle & Taylor, "Fatigue of insect cuticle," *J. Exp. Biol.* 216:1924
(2013) gives explicit force-controlled cyclic-loading **S-N curves** - cycles to failure
against applied cyclic stress - for locust hind tibiae and hind wings. Tibiae failed at
100,000 cycles at 76% of ultimate strength; wings at 46%. **The locust hind leg is the
canonical latch-mediated spring system.**

Narrow residual: nobody has cycled a *latch contact surface* under strike loading
specifically. That is a much smaller claim than the one made.

### G13 · Measure a negative energy density
Negative energy density is routinely made — that is the Casimir effect. Dynamical Casimir
pulls real correlated photon pairs from vacuum. Nobody has done Wigner tomography on that
output to reconstruct the local energy density and test a Ford–Roman bound. Hardware
exists and works.

Related: no quantum energy inequality is known for **any** interacting 4D theory, and
state-independent QEIs *provably fail* for non-minimal coupling — including conformal
coupling at ξ = 1/6.

### G14 · Weigh vacuum energy
Nobody has put negative energy on a scale. A cryogenic balance weighing Casimir cavities,
modulating reflectivity through the superconducting transition, would test whether a
localized *negative* energy density gravitates as GR demands. Under construction, no result.

### G15 · Settle the Casimir puzzle
Precision data fits the plasma model of metals and excludes the Drude model — the
thermodynamically correct one. A 2025 proposal identifies transverse-electric evanescent
waves as the culprit and proposes a decisive non-Casimir test. Not done. It would also firm
up every sub-micron gravity limit, which rest on the disputed subtraction.

### G16 · Classical-gravity noise floor
A 2026 result derives a model-independent minimum noise floor any classical-gravity theory
must inject. Measure below it and you have shown Newtonian gravity is entangling — with no
superposition required. Converts an eight-orders-of-magnitude coherence problem into a
force-noise problem on an ordinary mass.

### G17 · Uncertainties are overconfident - **WITHDRAWN**
A 1986 study found reported uncertainties in fundamental constants systematically
underestimate actual error — successive recommended values routinely fall outside the
previous stated error bar, connected explicitly to overconfidence psychology. Essentially
never followed up. The fine structure constant makes it live: two atom-interferometry
measurements, same class of technique, disagree at **5.4σ**.

### G18 · Peak vs average / turndown vs metabolic scope
Engineering measures capacity factor, turndown ratio and part-load efficiency. Physiology
measures factorial aerobic scope. Same ratio, two vocabularies.

**Co-citation: 0, twice** (metabolic scope ↔ peak-to-average-power; symmorphosis ↔ same),
against an internal biology **control of 159 works**. An empty crossing, not sparse data.

Sharper: biology already uses the phrases "peak-to-average" and "capacity factor" in its
own sense, with no awareness of the engineering literature using them.

Real numbers: gas peaker plants 13.9% capacity factor; average car driven ~4% of the time;
humans cannot sustain more than ~2.5× basal indefinitely.

**Neither side has the other's axis.** Engineering lacks duration-dependence; physiology
lacks the efficiency penalty. Nobody has written efficiency as a joint function of load
fraction and duration.

### G19 · Safety factor, derived independently twice
Alexander's *A Theory of Mixed Chains Applied to Safety Factors in Biological Systems*
(1997) — how much excess capacity a series system needs when its links vary. **46
citations, all comparative biomechanics** (all fetched and checked).

Engineering's **stress–strength interference theory dates to 1967 — 753 works.** Load
distribution, strength distribution, probability of interference in a weakest-link series
system. **The same object**, with a thirty-year head start. **Zero crossings either way.**

The trade runs both directions: engineering offers biology a *probabilistic* safety factor
— precisely the objection raised against symmorphosis since Garland & Huey 1987. Biology
offers engineering the duration axis and the **remodeling option** — a link that thickens
under load, which stress–strength interference cannot express because its strengths are
fixed at manufacture.

**Caveat:** symmorphosis itself is contested — only ~28 works total, with critiques at 100
and 79 citations against the canon's 483. Importing "enough but not too much" into
engineering imports a disputed claim.

### G20 · Resize vs throttle
Engineering fixes capacity at build time and runs below it. Biology rebuilds capacity to
match demand — mitochondrial density, muscle mass, capillary networks, gut lining.

Co-citation: symmorphosis ↔ design margin = **0**; symmorphosis ↔ engineering design = 2.
A thin genuine bridge exists in cloud elasticity ("auto-scaling" ∧ "biologically inspired"
= 45, one small cluster), but it carries no quantities — no fold-change, no timescale, no
cost of remodeling.

**WEAKENED on re-run.** The claim implied biology lacks a design-margin framing. It does
not - **symmorphosis *is* a safety-factor formalism**, written in engineering language
deliberately (`"symmorphosis" AND "safety factor"` = 5, all real). The surviving gap is
narrower: that formalism never reached computing or mechanical engineering
(`"symmorphosis" AND "engineering design"` = 0). And the literature is only ~5 papers, a
thin base either way.

**The unmeasured quantity still stands:** the cost and latency of a capacity change. Biology
pays it in ATP and weeks; engineering pays it in capex and years. No shared axis.

### G21 · No unified dimensionless regime map - **WEAKENED**
No single published figure or framework places organisms and processes in
dimensionless-number space across physics domains. Verified against the two most likely
candidates: a 2026 *Physics Today* feature on dimensionless numbers in biology offers
scattered examples and explicitly no comprehensive table; the field's 2021 biomimetics
scale review organizes by physics domain and uses Reynolds "descriptively rather than
systematically." The canonical books are fluid-media only — no optics, acoustics, thermal
noise or information.

**WEAKENED.** Vogel, "Exposing Life's Limits with Dimensionless Numbers," *Physics Today*
51(11):22 (1998) is an explicitly cross-domain framework spanning locomotion, respiration
and circulation. The claim must narrow to: **no *tabulated* regime map with crossover
conditions**, and none placing processes alongside organisms in a single Pi-space.

Also: `"Buckingham"` is contaminated by a developmental biologist's surname and must not be
used as a search handle.

### G22 · Scale-transfer triage - **WEAKENED, agents disagree**
Biomimetics uses the word "scaling" in **9,960** works. The intersection with
Buckingham-theorem terminology is **9** — all single-application engineering papers, **zero
methodology**. Terminological overlap without a methodological one.

**The decisive datum:** the field's dedicated review on scale in biomimetic transfer, 200
references, contains **no Buckingham Pi analysis**, and states in its own words that
universal scaling guidelines are "far from being identified," with "no decision tree or
algorithm."

**Two agents read the same paper differently, and the disagreement is recorded rather than
resolved.** Perricone et al., "Organismal Design and Biomimetics: A Problem of Scale,"
*Biomimetics* 6(4):56 (2021):

- The **first agent fetched the full text** and reported no Buckingham Pi analysis, no
  decision tree or algorithm, and quoted the authors' own statement that universal scaling
  guidelines are "far from being identified."
- The **second agent** read its thesis - that scaling rules must be considered in biomimetic
  transfer, surveyed across mechanics, optics, electricity and acoustics - as being the
  triage itself.

The full-text read is the better evidence, so this is recorded as **weakened, not
collapsed**. The 9-paper Buckingham intersection reproduces but is a **proper-noun
artifact**: the field does this work without ever writing the name.

**What survives:** no formal Pi-group screening checklist as a numbered design step. A much
weaker claim than "none methodological."

### Positive control · mortality laws and reliability theory — CLOSED
Biology's Gompertz law and engineering's Weibull distribution are the same hazard function.
**Co-citation: 218** (Gompertz-Weibull) and **35** (Weibull with the reliability theory of
aging), against **0** for this project's confirmed finds. The signal separates cleanly —
this is the calibration control.

**But closed one-way.** Of 633 works citing the reliability theory of aging, **6 are
reliability engineering** — under 1%. The unread direction is engineering never adopting
biology's late-life mortality plateau or heterogeneous-redundancy results.

**The explanation is worth keeping.** Organisms follow Gompertz because they are born with a
**high initial damage load**; manufactured devices follow Weibull because they start
near-defect-free. Same failure law, different initial conditions.

*(Contested: the late-life plateau itself. An age-misreporting rate of 1 in 10,000
reproduces it artifactually, and French data show continued increase past 105.)*

### G23 · Hormesis has no engineering formalism — **HOLDS, cleanest of the batch**
**The original hypothesis was wrong.** Engineering does now build stress-responsive
strengthening: mechanophore chemistry, and a 2021 polymer gel that self-strengthens under
vibration with a **66x modulus increase**, localizing along the stress distribution and
explicitly framed as bone-like.

So the asymmetry is **vocabulary, not capability.** Both fields build adaptive strengthening;
only biology has the quantitative dose-response apparatus — the ~30-60% amplitude ceiling
and the 10-20x stimulatory window width.

**Re-run, with both sides calibrating strongly** (hormesis 901, mechanophore 547 - which is
what makes these zeros mean something):

| Pair | Count |
|---|---|
| shot peening AND hormesis (and the -ic suffix variant) | **0** |
| hormesis/hormetic AND mechanophore / self-strengthening / stress-responsive material | **0** |
| hormesis/hormetic AND work hardening / strain hardening / cold working | **0** |
| hormesis/hormetic AND "training effect" | **0** |
| hormesis AND fatigue AND metal | **0** |

Meanwhile the engineering side demonstrably has the *phenomenon* - `"mechanophore"` against
training/strengthening/adaptive returns 31, including *Mechanochemical strengthening of a
synthetic polymer in response to typically destructive shear forces*. **Stress-strengthening
materials exist; nobody has written a dose-response curve for one.**

Materials scientists building dose-dependent adaptive strengthening are not using hormesis's
formalism, and hormesis's claim that the amplitude ceiling is "highly conserved and remains
to be elucidated" is exactly what a mechanophore system could test.

*(Honest note: hormesis is genuinely contested in regulatory toxicology. Do not present it as
settled.)*

### G24 · Miner's rule vs bone fatigue — thin, and a cautionary tale
Only **6** works over ~28 years connect linear cumulative-damage fatigue theory to bone.
Not a zero-crossing, but thin.

The sharper sub-question: **Miner's rule assumes damage is irreversible and additive. Bone
violates both** — it remodels. The known failure modes of Miner's rule (load-sequence
effects, non-linearity) mapping onto bone's remodeling response is unexplored, and bone is
the one tissue that both accumulates fatigue damage and hormetically strengthens against it.

**This candidate produced the synonym-trap discovery.** See `METHOD.md` §11.

### G25 · Energy per unit error suppression — the strongest find
**The measurement.** All 1,463 papers citing Hopfield's 1974 kinetic-proofreading paper were
pulled and their reference lists intersected against Shannon.

| | |
|---|---|
| Citers with reference lists available | 416 |
| …also citing Shannon | **16 (3.8%)** |
| …with "Shannon" in the title | **0** |
| …with "coding theory" / "channel capacity" / "codeword" / "LDPC" / "Hamming" | **0 each** |
| `"proofreading"` AND `"rate-distortion"` | **0** |

The 16 co-citers cite Shannon for *entropy*, never for the channel coding theorem. And the
sharpest detail: **33 papers in the proofreading literature use "decoding"; every one means
the ribosome's A-site.** The vocabulary collides perfectly; the formalism never meets.

**The unifying result already exists, and it is three lines of algebra.**

Shannon's limit is E_b >= N_0 ln2 per bit. With thermal noise N_0 = kT, so the Shannon limit
**is kT ln2 per bit — which is Landauer's bound.** Same number, 1948 and 1961.

The 2015 thermodynamics-of-error-correction result gives dW >= kT ln(eta_eq/eta) per error
suppressed — **2.303 kT per decade of accuracy.**

| Substrate | Bound | Value |
|---|---|---|
| Molecular copying | dW_p >= kT ln(eta_eq/eta) | **2.303 kT per decade** |
| Communication | E_b >= N_0 ln2, N_0 = kT | **0.693 kT per bit** |
| Computation | Landauer erasure | **0.693 kT per bit** |

All three are kT per nat, differing only in whether the nat is transmitted or discarded.
Three canonical bounds — 1948, 1961, 2015 — all in kT, cited by disjoint communities.

**This is not a gap that lacks a name. It lacks a citation path.** It sharpens G8: *energy
per unit error suppression* is a candidate universal figure of merit spanning molecular
biology, communications and computation, and the algebra to build it is already published in
three papers nobody reads together.

Real numbers on both sides: raw thermodynamic discrimination gives >5% error; translation
achieves ~1e-4; proofreading DNA polymerase 1e-6 to 1e-7. LDPC codes reach within 0.0045 dB
of the Shannon limit.

**Highest-yield next probe:** the T-cell discrimination literature, where proofreading models
and mutual-information estimates of receptor signalling already coexist.

### Positive control · DNA data storage — CLOSED
`"DNA data storage"` AND `"error-correcting code"` = **5.4%**, against **0.53%** for kinetic
proofreading — ten times higher, on a narrower base.

**The closed-gap signature, now nameable:** shared vocabulary, shared canonical citations,
and **performance reported as a fraction of a theoretical bound.** One DNA-storage paper
reports 1.57 bits/nt against a Shannon capacity of 1.83 — 86% of capacity — as its headline
result, using fountain codes and Reed-Solomon. That is what a field with a shared axis
sounds like. Candidate G25 has none of the three properties.

### G26 · Crypsis vs stealth — NOT YET A SHARED OBJECT (revised)
Signal detection theory **originated in radar** (Neyman-Pearson 1933; Peterson, Birdsall &
Fox 1954), moved into psychophysics in 1954, and reached camouflage biology third-hand —
where it lost its provenance entirely.

| Pair | Count | Composition |
|---|---|---|
| `"camouflage"` AND `"radar cross section"` | 82 | **100% engineering** |
| `"camouflage"` AND `"signal detection theory"` | 9 | **100% biology** |
| both together | **0** | — |
| `"radar"` AND `"Neyman-Pearson"` | 374 | |
| `"camouflage"` AND `"Neyman-Pearson"` | 3 | |
| `"camouflage"` AND `"d-prime"` | **0** | biology does not use SDT's own index |

The word partitions perfectly by discipline. **Weaker than G25** because there is no common
scalar: engineering has radar cross section in m^2, biology has only behavioural detection
latency, and no cost-normalized detectability metric exists on either side.

**REVISED after a decisive follow-up measurement.** The union of 509 papers citing the
canonical camouflage literature was checked against both founding texts of signal detection
theory: **0 of 169 with available reference lists cite the radar original, and 0 cite the
psychophysics original.** Combined with `"camouflage" AND "d-prime"` = 0, modern camouflage
biology **does not use signal detection theory at all** - it measures detection latency and
survival curves.

So nothing was borrowed and then forgotten. This **fails the same-quantity test**, not the
citation test: engineering has radar cross section in square metres, biology has
seconds-to-detection. New classification: **NOT YET A SHARED OBJECT.** Someone would have to
build a detectability scalar for crypsis before the comparison could even be posed.

*(Coverage caveat: 169 of 509 reference lists available. Zero of 169 is strong but not
proof.)*

### G27 - Collective decision - **WITHDRAWN**
Swarm intelligence and distributed-systems consensus both solve "reach agreement across
unreliable distributed agents."

| Pair | Co-citers |
|---|---|
| Ant colony optimisation (1996) and Paxos | **0** |
| ACO survey and Paxos | **0** |
| Paxos and honeybee nest-site selection (1999 / 2012) | **0 / 0** |
| ACO and Seeley 1999 | 1, and it is an ACO paper reaching sideways |
| *Internal control:* Seeley 1999 and Seeley 2012 | 33 |

**This finding is withdrawn.** A systematic re-run found `"ant colony optimization" AND
"honeybee"` returns **26 in the original, unmodified query** - and 551 under synonyms. The
bridge is explicitly present: papers exist titled *A Distributed Consensus Model for
House-Hunting in Temnothorax Ant Colonies* and *Efficient Swarm Consensus: RLR vs Raft*.

Only the literal string "Paxos" is isolated, **because Paxos is one algorithm's proper noun,
not a literature.** The zero measured a name. See METHOD.md 11.

**The unread formalism:** the speed-accuracy tradeoff is explicit on both sides - quorum
thresholds and dance-decay tuning in bees, latency bounds in consensus protocols. But the
third axis, **message complexity**, is formalised only in distributed systems and appears
nowhere in the bee literature. That is the missing shared surface.

### G28 - Marginal value theorem vs the Gittins index
Charnov's rule, leave a patch when marginal intake drops to the habitat average, is the
deterministic zero-switching-cost limit of the same optimality condition the Gittins index
generalises to the stochastic case. **No paper states that equivalence.**

| Pair | Co-citers |
|---|---|
| Charnov and Gittins | **8** (0.5% of Gittins) |
| *Control:* Gittins and Sutton & Barto | **181 (11.7%)** |

The control is what makes this sharp: operations research and reinforcement learning are
**one closed literature**. It is specifically biology that sits outside it. And all 8
co-citers are **neuroeconomics** - a third field reading both - so operations research and
behavioural ecology have no direct contact at all.

Behavioural ecology even derived its own stopping rule independently (Green 1984, "Stopping
Rules for Optimal Foragers"), in its own vocabulary, without the stopping-theory literature.

**Information foraging is a ONE-WAY BORROWING**, taken from behavioural ecology into
human-computer interaction, with the reverse direction unmeasured and expected near zero.

### Positive control - Levy-flight search: CLOSED
Physics and movement ecology genuinely read each other. The intermittent-search review
shares **183 co-citers, 23% of its own base**, with the founding Levy-flight paper, and 71
with the paper that overturned it. Against **0.5%** for Charnov-Gittins.

Worth keeping for the correction too: the original albatross Levy signature came from
wetness-logger dry periods that were **birds sitting on their nests**, and those spurious
"flights" were precisely the tail carrying the signal.

### Explore/exploit - shared phrase, not shared formalism
March 1991 and Sutton & Barto share **122 co-citers out of 21,727**, or 0.6%. The phrase is
ubiquitous; the formalism is not. The organisational literature cites reinforcement learning
as a metaphor - no regret bound, no index, no exploration parameter that maps onto anything.
**A shallower gap, because people in the field already suspect it.**

---

## Key findings with numbers

### The 1/r⁷ wall
Neutral matter has no monopole coupling to any field. You must induce a dipole first, so
force is second-order in the field; combined with fields falling as 1/r³, **force on
neutral matter falls as 1/r⁷**. The 1400 T²/m that levitates matter at 3 cm becomes
~10⁻² T²/m at 3 m — five orders short, unrecoverable. Radiation pressure is capped at
3.3 nN/W; acoustic needs a standing wave, hence a cavity, hence not free space.

**Consequence:** no known mechanism produces a matter-excluding barrier projected into
open air at standoff, at ambient temperature, without a cavity.

### Barrier arithmetic
Lifetime goes as exp(ΔG‡/kT). At room temperature **every ~6 kJ/mol buys 10× lifetime**.
One year needs ~100 kJ/mol; a million years needs ~135. Barrier grows logarithmically
while energy density is unbounded — so **stability and energy density are nearly
independent parameters.** Diamond: 2.9 kJ/mol driving force against a 370–540 kJ/mol
barrier.

### Stored energy is cheap; release control is expensive
Hafnium-178m2 holds 1.33 × 10⁶ MJ/kg and cannot be opened — triggering was claimed,
funded at ~$30M, and refuted at 100,000× the original sensitivity. Tantalum-180m is stable
past 10¹⁶ years with no release mechanism ever proposed. **Fat, at 37 MJ/kg, is the best
demonstrated room-temperature-stable triggerable store there is.**

Thorium-229m succeeded (laser-excited, 2024) for the opposite reason: only 8.4 eV up, low
multipolarity — the barrier was actually reachable.

### The carrier is a bus, not a tank
~50 g of free ATP, ~60 kg/day turnover. **Carrier inventory ≈ 0.1% of daily throughput.**
Flow batteries reach 10,000–27,000 cycles by the same architecture — circulating carrier,
fixed machinery, serviced separately — arrived at independently with no reference to
biology.

### Enzymes are consumed
10³–10⁷ turnovers until replacement, medians ~30–40 thousand. The usual killer is
mechanism-based inactivation — the enzyme is destroyed by the reaction it catalyzes.
Biology's strategy is a **cheap catalyst plus a continuous replacement line**, not a
durable one.

### Synapse ≈ transistor  *(both sides primary-sourced)*
| | J/bit | × Landauer |
|---|---|---|
| Mammalian cortical synapse | 1.99 × 10⁻¹⁵ | 6.9 × 10⁵ |
| CMOS 32-bit add, 45 nm 0.9 V | 3.13 × 10⁻¹⁵ | 1.09 × 10⁶ |

**Agree within a factor of 1.6** (1.2–1.8 propagating ATP free-energy uncertainty).
Durable because the firing-rate assumption does not propagate — energy and transmitted bits
both scale with release rate.

**Reliability does not explain the gap.** kT·ln(1/ε) at ε = 10⁻¹⁵ gives ~50× Landauer
against an observed ~10⁶ — under a third of it in log terms. Remaining candidate: both
substrates move ~10³–10⁴ carriers across structures far larger than the bit, making the
convergence architectural rather than a deep law.

### Measure from inside
A shark reads nanovolt-per-centimetre fields because it is *immersed in* the field,
sampling across a 10 cm baseline in a conductive medium. It never fights distance. **When
a measurement is falloff-limited, the highest-leverage move is to get closer, not more
sensitive.**

### Nature is not always optimal
CETCH beats the Calvin cycle at CO₂ fixation using nature's own parts. The primate retina
deliberately sits *below* the single-photon limit, trading sensitivity for contrast
fidelity. **Biomimicry works because biology has been searched, not because it is optimal.**

### Manufacturing, not design
We reproduce nacre's architecture but not its ambient self-assembly from seawater. We have
closed most of the molecular gap on spider silk — the bottleneck is the spinning duct, not
the protein. Photosystem II rebuilds its own damaged subunit every ~30 minutes; **no
engineered material has a repair cycle at all.**

### Assumed invariants that fell
Not arguments — experiments. Each held with confidence until someone built the apparatus.

| Assumption | Overturned by | Note |
|---|---|---|
| Parity is conserved | Wu et al., 1957 | Fell within a year of Lee & Yang proposing the test |
| Neutrinos are massless | Super-K 1998, SNO 2001-02 | Assumed, not measured. Built into the Standard Model |
| CP is conserved | Cronin & Fitch, 1964 | |
| Continents are fixed | Seafloor spreading | The geology was fine; the mechanism was missing |

**This corrects a claim made earlier in the project.** The discrepancy survey found that
every *recently* resolved inter-method disagreement went to systematics, not new physics.
The solar neutrino problem is the counterexample: a persistent, decades-long,
method-vs-method discrepancy that resolved to **new physics**, with two Nobel Prizes. The
base rate is not zero — it is uncomputed and era-biased. See G9.

### The property that looked intrinsic and was environmental
The sharpest documented case of "the constant survived, the neighbour was free."

| Nuclide | Neutral atom | Fully stripped |
|---|---|---|
| Dysprosium-163 | **Stable** | 47-day half-life |
| Rhenium-187 | 4.2 x 10^10 yr | **32.9 yr** |

Mechanism: with the electrons removed, the emitted beta can land in a *bound* orbital of
the daughter rather than the continuum, raising the effective decay energy about thirtyfold.
Nothing was added to the nucleus. A different door opened.

"This nuclide is stable" reads like a property of the nucleus. It is a property of the
nucleus **plus its environment**.

**Honest limit:** this is full ionization in a storage ring, not a chemical environment.
Chemically accessible control tops out at 0.1-1.5% (beryllium-7 in a fullerene cage, the
most favourable case in the periodic table), and 10^-4 or less for heavy nuclei.

### Regimes where the intuitive impossibility is real
A documented category, not a hypothetical one:

- **Negative absolute temperature** — nuclear spins (1951), motional degrees of freedom in
  cold atoms (2013)
- **Negative refractive index** — predicted 1968, demonstrated 2000-01
- **Negative effective mass** — in a Bose-Einstein condensate, 2017
- **Negative energy density** — the Casimir effect, measured to ~0.5%
- **Superluminal phase velocity** — real, and carries no information

### The 1/r^7 assumption audit
Applying the neighbour procedure (METHOD.md §8) to this project's own load-bearing wall.

| The derivation held fixed | Varied experimentally? |
|---|---|
| Matter is neutral | Yes |
| Free space, no cavity | Yes — this is why cavities work |
| Ambient temperature | Yes — this is flux pinning |
| **The field is static in time** | **No. This is the open neighbour** |

And the live physics sits exactly there: photonic time crystals, Floquet rotational
superradiance, and the dynamical Casimir effect — all of which win by varying
time-invariance rather than by pushing harder on the other three.

### Complex form without cellular machinery
*Caulerpa* is a single cell metres long with differentiated stolon, frond and holdfast — no
transverse walls, no cell division. Transcripts partition into "pseudo-organs." Proposed
mechanism: **per-nucleus positional identity** — nuclei apparently detect their own position
and express position-specific nuclear-pore genes, so patterning runs through selective
nucleocytoplasmic transport rather than membranes. *Acetabularia* removes even the
many-nuclei escape hatch: macroscopic, differentiated, and **uninucleate** for most of its
life cycle.

*Physarum* solves the size problem differently — its **peristaltic wavelength scales with
network size**, converting a diffusion-limited problem into a transport problem it controls.

**Honest negative:** this framing is already published. A 2015 paper titled *Plant
architecture without multicellularity* argues explicitly for "the relative independence of
organismal morphology from cell division patterns." Not novel in biology. **Never carried
into design literature as an existence proof about achievable form** — that transfer is
where any novelty lives.

### How tightly are the constants actually constant?
The honest answer is regime-dependent, and the weak regimes are much weaker than the
headline numbers suggest.

| Regime | Bound |
|---|---|
| Present-day alpha drift (Yb+ clocks) | **1.0(1.1) x 10^-18 /yr** — effectively closed |
| alpha over 1.8 Gyr (Oklo reactor) | ~10 ppb, model-dependent at factor 2-3 |
| alpha at z ~ 0.9 (ALMA molecular) | < 0.55 ppm |
| **alpha at z ~ 1000 (CMB)** | **(3.6 +/- 3.7) x 10^-3 — five orders weaker** |
| **Spatial variation across the sky** | **percent-level — three orders weaker than temporal** |
| **G at nucleosynthesis** | **|dG/G| <~ 5-6%** |
| G, present day (lunar laser ranging) | (-5.0 +/- 9.6) x 10^-15 /yr — ~3 orders looser than alpha |
| **Strong field / high density, alpha and mu** | **no constraint exists at all** |

**The structural caveat, which is the most important line in this survey.** The leading
theory class that predicts varying alpha (Bekenstein-Sandvik-Barrow-Magueijo) has alpha
becoming constant once Lambda-driven acceleration begins — i.e. now. **So the tightest
measurement in the field is aimed at exactly the epoch where the leading theory predicts the
least signal.** A null at 10^-18/yr does not exclude ppm-level variation in the matter era.
The strongest bound and the strongest prediction are not measuring the same thing.

Also: clock bounds constrain *linear drift*, not oscillation. Oscillatory variation requires
a separate ultralight-dark-matter analysis, which covers 10^-24 to 10^-17 eV and leaves other
mass ranges open.

**On varying c.** Since 2019 c is fixed by definition, so the question is not well posed —
a measurement of c is now a measurement of your length standard. Only **dimensionless**
ratios carry physical content. "Did c change?" must be recast as "did alpha change?"

**What a detection would mean.** Any constant varying in space or time implies an almost
massless field coupling to matter. By the same coupling it generically produces
equivalence-principle violations and fifth forces — which is why torsion-balance and
atom-interferometry tests constrain varying-constant models without ever measuring alpha.
This connects directly to G10 (sub-38.6 um gravity).

### More properties that looked intrinsic and were environmental
Beyond the nuclear cases above:

- **Spontaneous emission lifetime.** Set by the density of electromagnetic modes at the
  transition frequency, not by the atom. A resonant cavity speeds emission; a waveguide
  below cutoff or a photonic bandgap can suppress it so far that an excited atom will not
  decay. Same atom, same matrix element, different boundary conditions. The Lamb shift is
  the same lesson applied to levels rather than rates.
- **Mass.** The proton is ~99% binding energy — gluon field energy and confined quark
  kinetic energy. Mass is not "amount of stuff"; additive mass is a low-binding-energy
  approximation that works for chemistry and fails for QCD.

**The cautionary counter-case, included deliberately.** Claimed X-ray triggering of the
hafnium-178m2 isomer was never independently reproduced. The nuclear cases above are
credible because they were measured in a storage ring with a clean, calculable mechanism —
not because "environment affects nuclei" is a free pass.

---

## Computed results (Layer 2)

Not catalogue entries. Numbers this project produced.

### C1 · Availability of living tissue — first computation of its kind

**The derivation, which is the actual result.** For a two-state system,

    A = MTBF/(MTBF + MTTR) = (1/k_damage) / [(1/k_damage) + (1/k_repair)] = k_repair/(k_repair + k_damage)

Engineering's availability formula and the photosystem repair steady state are **not
analogous — they are identically the same expression.** That is a derivation, not a
coincidence, and it closes the formal half of G5.

**Computed from published rate constants:**

| System | Damage rate / MTBF | Repair rate / MTTR | **A** |
|---|---|---|---|
| Data centre, "five nines" | — | 5.3 min/yr | 0.99999 |
| US power grid, normal ops | — | ~2 h/yr | 0.9998 |
| US power grid, all events | — | 11 h/yr | 0.9987 |
| Commercial aviation dispatch | — | — | 0.995 |
| **Cortical bone** | 5%/yr turnover, MTBF 20 yr | 17-week remodeling period | **0.984** |
| **Trabecular bone** | 20%/yr turnover, MTBF 5 yr | same | **0.939** |
| **Photosystem II, 20 C** | k_PI = 2.70e-4 /s (MTBF 61.7 min) | k_REC = 20.4e-4 /s (MTTR 8.2 min) | **0.883** |
| Photosystem II, 35 C heat stress | k_PI ~ 4.1-5.0e-4 /s | k_REC ~ 6.4-9.9e-4 /s | **0.56-0.71** |
| Photosystem II, 5 C cold stress | k_PI ~ 3.0-3.1e-4 /s | k_REC ~ 2.5-2.8e-4 /s | **0.45-0.48** |

**A leaf is less available than a power grid.** That sentence was previously unwriteable
because nobody had computed the left-hand side.

**Caveats, all load-bearing:**

1. **Population, not unit.** A leaf holds ~1e8 photosystems; nothing is ever "down," a
   *fraction* is down. So biological A is an **expected functional fraction**, not a
   probability the system works. Those coincide for large ensembles — **but only if units
   fail independently.** Correlated damage breaks the identity, which is exactly what the
   35 C row shows: heat hits every unit at once and A collapses to 0.56.
2. **Down-while-repaired holds for PSII, not for bone.** A photoinactivated PSII genuinely
   evolves zero oxygen until D1 is replaced — the binary assumption is true at unit level,
   which is why PSII is the clean case. A resorption cavity degrades stiffness rather than
   eliminating it, so bone's 0.984 should be read as **"1.6% of tissue volume is in the
   remodeling space"** and treated as a lower bound.
3. **Continuous, not episodic.** Repair is a steady-state flux. Mathematically fine — the
   two-state Markov model never required episodicity — but it kills the managerial reading
   of MTTR as "time the technician spends."
4. **Gut epithelium left blank deliberately.** A 3-5 day turnover is not damage-plus-repair;
   it is **scheduled replacement before failure**. The engineering analogue is
   MTBF-extension policy, not availability. Forcing A onto it would be the "merely cute"
   failure mode this computation was built to avoid.

**Verdict:** rigorous for PSII, defensible for bone as remodeling-space fraction, not
meaningful for scheduled-replacement tissues. Also verified: PSII repair costs ~24,000 ATP
per complex, up to 4.6% of gross photophosphorylation.

**Open:** DNA repair half-times could not be sourced; that row stays blank. No paper reports
a steady-state functional PSII fraction *as such* — every value above is computed here from
published rate-constant pairs.

### C2 - Probabilistic safety factors for biological structures

Applying engineering's stress-strength interference formalism to Alexander's biological
cases. Biology has only a deterministic ratio; the formalism yields a probability of
failure - which is precisely the objection raised against symmorphosis since 1987.

**A find that strengthens G19.** Diamond (2002, J Physiol) states stress-strength
interference *verbatim* in a physiology journal, with **no reliability-engineering
citation**:

> "Safety factors serve to minimize the overlap zone (resulting in performance failure)
> between the low tail of capacity distributions and the high tail of load distributions.
> Safety factors increase with coefficients of variation of load and capacity, with capacity
> deterioration with time, and with cost of failure, and decrease with costs of initial
> construction, maintenance, operation, and opportunity."

He also lists *"safety factors of series systems"* as an unsolved question - which is
exactly what reliability engineering solved decades earlier. **Biology has the concept,
stated correctly, and never carried it to a number.**

#### The robust result

**For bone, failure probability is governed by the variability of the tissue, not the
variability of locomotion.**

With the safety factor held at 3, moving strength CV from 0.10 to 0.30 swings P_f across
**nine orders of magnitude**. Moving load CV from 0.05 to 0.30 moves it **half an order**.
Measured locomotor load CV is 0.05-0.11 - small against SF x V_R ~ 0.6.

This holds in both the normal and lognormal models, at every safety factor from 1.4 to 4.1.
And it points at the term **Alexander's mixed-chain argument de-emphasises**: he reasoned
that links with more variable *loading* should carry higher safety factors.

#### Worked central case (all inputs verified)

Goat limb bone, SF = 3, load CV 0.11 (measured in vivo), strength CV 0.20 (human rib
cortical coupons):

| Model | beta | P_f |
|---|---|---|
| Normal | 3.28 | 5.2e-4 |
| Lognormal | 4.79 | 8.2e-7 |

**The model choice decides the answer.** Three orders of magnitude apart, straddling the
EN 1990 structural target (beta = 3.8, P_f = 7.2e-5) from opposite sides. No biological
dataset obtainable is powerful enough to test the tail and settle it.

#### What is invalid, flagged rather than deleted

Comparing these to engineering targets is **formally invalid as stated**. Biological P_f
here is *per load cycle*; EN 1990 is per 50 years, FAA is per flight hour. An animal takes
1e6-1e7 steps a year, so a per-cycle 5e-4 implies certain fracture within days. Reconciling
them needs a load-cycle-counting fatigue model - a different formalism.

#### The remodeling objection is the deliverable

Stress-strength interference assumes strength is **fixed at manufacture** and thereafter
independent of load. In bone it is neither: strength is a *function of the realised load
history*, with negative feedback. The individual sitting in the weak tail while being loaded
hard is precisely the one that remodels, so **the interference region is actively depleted.**
Every P_f above is therefore an upper bound of unknown tightness.

**This inverts the trade.** Reliability engineering's assumption - strength fixed at
manufacture, degrading monotonically - is the **zero-gain limit of a control loop biology
runs with positive gain**. A formalism for load-adaptive strength would be a contribution
*from* biology *to* reliability engineering, not the other way round.

#### Blocked and weak joins, stated plainly

- **Crab claw and intestinal transport: blocked.** Safety factors are published; no variance
  data obtainable behind paywalls.
- **Tendon load CV: never obtained.** Its numbers are conditional on an assumed value.
- **Weakest join:** bone strength CV is human rib; load CV is goat, horse and dog limb. No
  source gives paired strength and load variability from one population - and that paired
  measurement is exactly what would settle the question.
- Alexander 1997's own equations could not be fetched (403 everywhere), so the claim that
  his model is *formally* isomorphic to stress-strength interference is verified only at the
  level of stated structure, not at the equation level.

**Verdict:** the specific P_f numbers are not quotable as facts. The sensitivity structure
is robust across the whole plausible parameter box and is a real, sourced, quantitative
statement the deterministic safety-factor literature cannot make.

---

## Closed / refuted

| Item | Status |
|---|---|
| EmDrive | Refuted. Thermal expansion of the mounting bracket; null bounded 3 orders below claim |
| Mach-effect thruster | Refuted. Signal decreases monotonically as artifact control improves |
| Podkletnov gravity shielding | Refuted. Null at 0.001%, three orders below smallest claim |
| Pais patents | Not physics. ~$508k Navy program, no result, no derivation, no data |
| Hafnium-178m2 triggering | Refuted at 10⁵× sensitivity. Congress zeroed the program |
| NEEC isomer depletion (2018) | Not replicated. Independent limit ≥500× below the claim |
| Shark denticle drag reduction | Popular story falsified. Real denticles *increased* drag 44–50% in DNS |
| Positive-energy warp drive | Contested. Constant velocity only, cannot accelerate; 2026 no-go theorems |
| Proton radius puzzle | Resolved to systematics (spectroscopy). Scattering analysis still disputed |
| Muon g−2 anomaly | Migrated to theory-vs-theory. Residual ~0.6σ. Two pion datasets disagree at 5σ |
| S₈ tension | Fading. The old low value was a photo-z systematic |
| X17 | Not an inter-method discrepancy — single group; the "independent replication" shares four authors |

---

## Corrections log — MIGRATED

**These entries now live in `vault/log.md`**, dated 2026-09-05 and marked
`[migrated from FINDINGS.md]`. That log is the live one; the table below is kept only so the
archive stays readable on its own.

Kept visible rather than silently fixed, because the pattern of errors is itself
information.

| Correction | Detail |
|---|---|
| Neurons vs Landauer | Claimed 10⁴; actually **10⁶–10⁸**. The 10⁴ is ATP *molecules*, and one ATP ≈ 20 kT |
| Vesicle cost | Claimed 2.34 × 10⁴ ATP; actually **1.64 × 10⁵**. Kills the "one vesicle ≈ one bit" line |
| Halbach as a 20° switch | Wrong. Field varies as the **half**-angle — 20° changes it by 1.5%; null is at 180° |
| Siberian permafrost seeds | Not seed germination — tissue culture from immature fruit tissue |
| Fat vs TNT | Barrier height is not the main reason. **TNT carries its own oxidizer**, so the reaction is intramolecular and can propagate supersonically. A power-density difference |
| Enzymes "not consumed" | Wrong. 10³–10⁷ turnovers, then scrapped |
| G apparatus transplant | Two agents disagreed on rebuild vs transplant; balance of evidence and the paper title favour **transplant**. Flagged, not settled |
| Loihi energy figure | Quoted 23.6 pJ/SOP — not in the primary paper. Removed |
| Frugality asymmetry | **Claim did not survive.** Reproductive effort runs ~25% of an annual energy budget. Conflated numerosity with cost per unit, then with total share. Biology is not profligate with reproduction — it is expensive, which is what life-history theory is about |
| Meteor vs Galileo contrast | **Wrong as stated.** The Galileo Project does publish calibration, a 41% acceptance rate and 36% detection efficiency. The real contrast is capability - multi-station astrometry gives range, an infrared array does not |
| Crypsis as a forgotten bridge | **Wrong.** 0 of 169 camouflage papers cite either founding text of signal detection theory. Nothing was borrowed and lost; the fields measure different things. Reclassified NOT YET A SHARED OBJECT |
| G27, collective decision | **Withdrawn.** 26 hits in the original query. The zero was anchored on Paxos, an algorithm name rather than a literature |
| The energy-per-bit axis claim | **Withdrawn.** 575 papers connect Landauer to neural systems. The specific figure may survive; the absence claim does not |
| G4, criticality | **Downgraded.** 99 papers link Hopf bifurcation to the cochlea. A single-review omission, not a field gap |
| G11 plant gravisensing | **Withdrawn.** Synonym artifact - the field says gravisensing, and the thermal-threshold calculation exists |
| G12 latch cycles-to-failure | **Withdrawn.** S-N curves published for locust cuticle in 2013 |
| G17 overconfident uncertainties | **Withdrawn.** 279 citations including a direct quantitative follow-up. String matching would have confirmed it; the citation graph destroyed it |
| G21, G22, G9 | **Weakened.** Each overstated; narrower claims survive in all three |
| Hessdalen citation | An agent invented a paper attribution. See `METHOD.md` §4 |

---

## Open questions carried forward

- Does the gradient-coupling formalism extend beyond linear response to reach dynamic
  soaring and sails?
- What sets the ~10⁶ × Landauer floor, if not reliability?
- Does the Alexander / stress-strength bridge actually close, and what does a probabilistic
  safety factor do to the symmorphosis debate?
- What is the cost and latency of a capacity change, on a shared axis?
- Which design principles are scale-invariant vs constant-bound? *(survey in progress)*
- What patterns a giant single cell, with no cellular machinery to do it? *(survey in progress)*
