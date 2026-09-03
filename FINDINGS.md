# Findings

Status ledger. Every entry is either a measured gap, a finding with numbers, or a closed
item. Corrections are logged at the bottom rather than silently fixed.

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

### G4 · Criticality as a design strategy
Hair cells self-tune to a Hopf bifurcation for divergent gain. Parametric amplifiers are
biased just below threshold. Same law, two vocabularies — √G·B = κ and gain ∝ f^(−2/3).

**Reference audit:** a 578-reference *Rev. Mod. Phys.* colloquium on biological
criticality cites **zero** engineering, laser, MEMS or superconducting work. The amplifier
papers cite **zero** hair-cell work. The only bridge traces to one researcher's biography.

**Shared missing object:** a theory of optimal *distance* from threshold. Cortex sits at
m̂ ≈ 0.98, not 1. Amplifiers are biased just below. One question, asked twice.

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

**Best find:** IAEA-TECDOC-626 (1991) already defines an ordinal degree-of-passivity
ladder, Category A (no signal inputs, no external power, no moving parts, no moving fluid)
through D. Invisible outside nuclear engineering. Generalized: *the fraction of the
response that survives when the actuation path is cut.*

**Hazard:** control-theoretic "passivity" is a homonym — a closed-loop dissipation
property fully compatible with active control.

### G8 · Energy per bit, one axis
Neuroscience counts ATP molecules per bit. Chip design counts femtojoules per operation.
Biophysics counts kT per methylation cycle. Superconducting logic counts zeptojoules per
gate at 4 K. Nobody normalizes to kT.

The closest published attempt covers molecular biology and supercomputers only — no
neurons, no reversible logic, no neuromorphic. The definitive theory review supplies the
machinery and no numbers.

### G9 · Discrepancy base rate
No cross-domain literature treats persistent inter-method disagreement as a class. The one
statistical framework ("dark uncertainty") is explicitly designed to *absorb* discrepancy
into an inflated error bar rather than interrogate it. Philosophy has the sharpest
statement of the hole: the standard defence is *robustness* — agreement across methods
validates — and there is no corresponding account of what to do when they disagree.

Nobody has built the catalogue, computed the base rate, or asked which features at time t
predicted each outcome. **No apparatus. All public data.**

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

### G12 · Latch cycles-to-failure
Trap-jaw ant strikes show no decline in peak velocity over repeated use; fatigue appears in
the muscle, not the latch. **No paper gives a cycles-to-failure number for any biological
latch.** A measurement gap, not a hidden result.

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

### G17 · Uncertainties are overconfident
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

**The unmeasured quantity:** the cost and latency of a capacity change. Biology pays it in
ATP and weeks; engineering pays it in capex and years. No shared axis.

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

## Corrections log

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
