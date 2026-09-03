# Method

How this inquiry is run. Written down because the method turned out to be as much the
output as the findings.

---

## 1. The gap-hunting test

We are looking for one specific thing: **a principle that multiple fields discovered
independently, quantified in their own vocabulary, with no shared figure of merit and no
cross-citation.**

The failure mode is obvious and must be guarded against: once you are looking for
unifying principles, you find them everywhere, because almost any two things can be
described abstractly enough to sound like the same move. That produces a theory of
everything that predicts nothing.

A candidate is only a real gap if **all three** hold:

1. **Each field has its own quantified metric.** Not a vibe — a number, measured and
   published. Catalytic cycles until replacement. Fade per cycle. Turndown ratio.
2. **The metrics are the same quantity** under different names. You could put them on one
   axis today without inventing anything.
3. **The citation networks genuinely do not overlap.** This is checkable, not
   impressionistic. See §2.

If only (1) holds, it is an analogy. Say so and keep it out of the gaps list.

### The positive control

**Stochastic resonance** is the case where the cross-domain synthesis *did* get written —
discovered in climate science (~1981), found in crayfish and paddlefish, then engineering,
then unified in a *Reviews of Modern Physics* article in 1998. That is what a closed gap
looks like, and it proves the pattern is real.

### What closes a gap

The strongest single result of this project. **Work extracted per bit came back NOT a
gap** — the metric η = W/(k_BT·I) is shared across colloidal, single-electron, cavity-QED
and NV-centre platforms, which are directly comparable despite sharing no hardware.

Why? Sagawa and Ueda gave it a **theorem** rather than a convention. Fix the denominator
and the shared figure of merit follows within a decade.

**Every other gap on the list is missing exactly that.** Closing one does not require a
review article. It requires a theorem.

And in three cases the theorem already exists, unread in an adjacent field:

| Gap | The unread result |
|---|---|
| Gradient coupling | Kedem–Caplan degree of coupling (1965) — provably contains thermoelectric ZT: q² = ZT/(1+ZT) |
| Repair vs durability | Availability A = MTBF/(MTBF+MTTR) ≡ photosystem steady state k_REP/(k_REP+k_PI) |
| Repair vs durability | Kirkwood's disposable soma theory (1977) — unread by self-healing materials |
| Multifunctionality | Ecology's Hill-number N-function formalism — mathematically domain-neutral |

---

## 2. The co-citation audit

The methodological upgrade that turned this from pattern-noticing into measurement.

Take two literatures that describe the same move. Query how many papers cite both.
**Report the number. Zero is a finding.**

Run against OpenAlex (`api.openalex.org`) or Crossref (`api.crossref.org`) — both are
free, unmetered, and do not require a general web search budget.

Also useful: **reference-list audits.** Take a major review in field A and count how many
of its references come from field B. A 578-reference *Reviews of Modern Physics*
colloquium on biological criticality cites zero engineering work. That single number
carries more weight than any amount of argument.

Three tables from this project are publishable as-is with nothing but these queries:

- The gradient-harvesting zero table
- The multifunctionality zero table
- The 578-reference criticality audit

---

## 3. The claims register

For turning reported behaviors into testable physics. Three columns:

1. **Reported behavior**, stated as a physical observable with units where possible.
2. **Candidate mechanisms** that produce it, each with real numbers and its scaling law.
3. **The discriminating measurement** — what separates candidate A from candidate B.

The third column is what makes it a research instrument rather than a list. A row without
one is a note, not an entry.

### The discipline that makes it work

**Testimony sets the specification. It never sets the mechanism.** That separation is why
the register stays valid regardless of how any account is eventually assessed — the rows
are about physics, and physics does not depend on who reported what.

### Three outcomes, all useful

| Outcome | What it means | What you do |
|---|---|---|
| Reduces to ordinary physics | The observable carries no discriminating information | Stop spending attention. Record the reduction. |
| Multiple live candidates | Several mechanisms fit | Run the discriminating protocol |
| No candidate at any magnitude | Nothing known produces this, and you can say why | The genuine anomaly, now sharply stated |

Enter behaviors only as observables. "Excludes matter at ~1 m in open air" is a row.
"Uses an unknown energy source" is not — it names an absence, and absences cannot be
measured.

---

## 4. Verification discipline

Two research failures occurred in this project and both had the same tell: **very
specific numbers with no URL that produced them.**

- One agent invented a paper attribution.
- One agent presented unfetched figures as sourced.

### The rule

A figure is quotable only if the source names the fetch that yielded it. Everything else
is marked `UNVERIFIED` or stays out.

Require every reported number to carry one of:

- `VERIFIED` — fetched this session, with the URL that produced it
- `UNVERIFIED` — stated from memory or a secondary route, do not publish

When a paywall blocks extraction, the correct answer is "I could not get this," never a
reconstruction from memory.

### Why this matters beyond hygiene

It is the same principle the discrepancy survey produced: **prior-choice fragility is
diagnostic.** A number that moves depending on how you obtained it was never a
measurement. That applies to research pipelines exactly as it applies to torsion balances.

---

## 5. Reading a discrepancy

From the survey of persistent inter-method disagreements. Four features now have
empirical support:

1. **Same-method disagreements are systematics, essentially always.** Two implementations
   of one technique disagreeing offers no new physics — only a shared-model error one side
   got wrong. Caesium vs rubidium recoil (5.4σ). Two gravity methods in one lab (2.7σ).
2. **Single-group claims resolve against the claimant.** With a corollary: when the
   measurement is cheap enough for outsiders and outsiders still have not confirmed it
   after a decade, *the absence is the result.*
3. **Prior-choice fragility is diagnostic.** A lensing result went from a 2% measurement
   to an 8% one purely by relaxing an assumption, with no new data.
4. **The interesting survivors are over-determined.** The neutron lifetime matters because
   an independent relation over-determines it and picks a side. G is *less* interesting
   than its 13σ suggests, because nothing over-determines it.

### How discrepancies actually end

Not with better instruments. Deuterium abundance scattered over an order of magnitude in
the 1990s with rival camps, and resolved through **ruthless target selection and blind
analysis**. The kilogram resolved because two genuinely different methods were forced to
agree **as a precondition for redefinition**.

The transferable finding: **institutionalize cross-method agreement as a requirement.**

---

## 6. The analytical frame

Five moves recur across every field surveyed. None of them is "build a stronger thing."
All five are **structural** rather than **magnitude** moves — they change the arrangement,
not the amount.

| Move | Statement |
|---|---|
| 01 · Manufacture contrast | Signal under the noise floor? Don't amplify — create a local disparity that survives it |
| 02 · Use the noise | Efficiency is often non-monotonic in noise, with an optimum well above zero |
| 03 · Separate timescales | Don't build a faster actuator; decouple slow loading from fast release |
| 04 · Change the actor | When a theorem blocks the route, swap the category of the thing doing the work |
| 05 · Work inside the noise | Three postures — suppress, exploit, redistribute. Each community knows one. |

Engineering culture defaults to raising signal or lowering noise. Both are magnitude
moves. Evolution cannot turn up the power, so it searches arrangement instead — which is
why it keeps finding these first.

---

## 7. Running the agents

- **Fan out on independent roots.** Parallel agents on non-overlapping topics; never two
  on the same literature.
- **Ask for the negative result explicitly.** "If no unifying framework exists, say so
  plainly — that absence is the deliverable." Without this they pad.
- **Demand co-citation counts** as the primary deliverable, not prose.
- **Ask them to correct the premise.** Several briefs contained errors that agents caught
  precisely because they were told to.
- **Watch for placeholder returns.** An agent that reports "I'll wait for the surveys to
  land" has not done the work. Send it back.

---

## 8. Vary what was held fixed

The sharpest formulation of the project's central move, and the one that most reliably
points at live physics.

**A hard bound is rarely wrong. What is usually wrong is the list of things its derivation
held fixed without saying so.**

The historical record favours this reading over "the constant is wrong":

| Case | The constant survived | The neighbour was free |
|---|---|---|
| Dysprosium-163 | Nuclear stability | The **electron environment** — stable neutral, 47-day half-life fully stripped |
| Rhenium-187 | Beta decay physics | The **available final state** — 4.2 x 10^10 yr to 32.9 yr when the electron can land in a bound orbital |
| Solar neutrinos | The solar model | **Flavour** — a degree of freedom nobody was varying |
| Muon g-2 | The measurement | The **hadronic input** |
| Continental drift | The geology | **Seafloor spreading** |

### The procedure

1. Take the bound. Write down what its derivation **assumed**, not what it concluded.
2. For each assumption, ask whether it has actually been varied experimentally, or merely
   inherited.
3. The unexamined assumptions are the work.

### Worked example — the 1/r^7 wall

The result (no matter-excluding barrier projected at standoff) assumes four things:

| Held fixed | Varied? |
|---|---|
| Matter is neutral | Yes — charged and polarizable cases explored |
| Free space, no cavity | Yes — this is precisely why cavities work |
| Ambient temperature | Yes — this is flux pinning |
| **The field is static in time** | **Open** |

And the live physics sits exactly there. Photonic time crystals. Floquet rotational
superradiance — you cannot spin a medium fast enough, so modulate it in time and obtain
effective rotation. The dynamical Casimir effect — a mechanical mirror is hopeless, so make
the boundary a boundary *condition* with no mass and win twelve orders of magnitude.

Every one is the same move: **the thing everyone held constant was time-invariance, and
varying it was worth more than any amount of pushing on the other three.**

### Why this is not special pleading

The distinction that keeps it honest: the assumptions that fell, fell to **experiments
designed to test them**, not to arguments that they might be wrong. Parity fell because Wu
built the apparatus. Neutrino mass fell because Davis and Koshiba counted for thirty years.

That is not a defence of institutions — it is the opposite. It says the challenge succeeds
when someone **measures**, which requires no permission.

### Consequence for the scale triage

"Constant-bound" is the wrong phrase and has been corrected throughout. A measured bound
should be stated as:

> The bound is measured. Here is how tightly. Here is what would have to be wrong for it to
> move — and here is which of its assumptions has never been varied.

That is honest in both directions, and it makes a bound **actionable** rather than closing.

---

## 9. The scale-transfer triage

Before copying a mechanism, test whether it survives the scale change. The criterion is
one line and appears not to have been stated anywhere:

> A capability is **scale-transferable** iff the governing dimensionless group can be held
> fixed by co-varying the free parameters (L, v, mu, rho, gamma). It is **constant-bound**
> iff the group contains a fixed constant appearing **alone** — kT, lambda, g, c — rather
> than in a ratio you can compensate.

Note what this does and does not say. "Appears alone" is a statement about the *current
formulation*, not about impossibility. It is the input to §8: a constant appearing alone is
exactly the place to ask what the derivation held fixed.

### Worked crossovers

| Group | Ratio | Crossover |
|---|---|---|
| Peclet, Pe = vL/D | advection / diffusion | ~10 um for a cytoplasmic protein with motor transport |
| Reynolds | inertia / viscous | ~0.1-1 mm for a mm/s swimmer; bacteria sit at Re ~ 1e-4, whales at 2e8 |
| Bond | gravity / surface tension | capillary length in water ~2.7 mm — the water-strider boundary |
| Knudsen | mean free path / size | ~70 nm in air |

**The maximum-cell-size question and the Peclet number are the same equation.** Diffusion
time goes as x^2/D: 1 um takes 0.01 s, 20 um takes 10 s, 1 cm takes two weeks. Motors run
at ~1 um/s, so transport beats diffusion above ~10 um — and that crossover *is* Pe = 1.
Cell biology and fluid mechanics asking one question in two vocabularies.

### Documented transfer failures

- **Gecko adhesion.** Maximum shear stress scales as A^(-1/4) — a *negative* exponent.
  Not merely hard to manufacture at scale: **intrinsically anti-scaling.** Synthetic tape
  fails beyond ~1 cm^2; human-scale (~200 cm^2) remains unrealized. The van der Waals
  interaction length is fixed at ~nm while real surfaces are rough at hundreds of um — a
  constant-bound failure, exactly the category the triage would have caught.
- **Structural colour.** Wavelength-locked. You cannot build a 10x-scale morpho wing that
  is still blue.
- **Compliant thin shells.** Self-weight deformation; weight goes as L^3 and strength as
  L^2. Only material substitution helps, and that is not rescaling.
- **Leonardo's ornithopters.** The first documented case, and a Reynolds failure.

### Status of this as a contribution

Honest framing, preserved from the survey: Buckingham Pi is 111 years old, biologists know
Reynolds, and the biomimetics literature has already framed the problem correctly. The
unclaimed piece is narrow — the criterion above, applied as a **pre-transfer screening
step**, with crossover scales tabulated in metres. That is methodology packaging on known
machinery, not a discovery, and should be pitched that way.

