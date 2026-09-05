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

And in four cases the theorem already exists, unread in an adjacent field — all four
citation-tested and all four still unread, see `vault/computed/C13-unread-theorem-audit.md`:

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
of its references come from field B. That single number carries more weight than any
amount of argument — which is exactly why it must be verified before it is quoted.

**Hard precondition, learned the expensive way — twice.** This project reported a *Reviews of
Modern Physics* colloquium on biological criticality as having **578 references, zero from
engineering**, and promoted it as publishable. When the PDF was finally extracted, its printed
bibliography held **595 references**, and **carried no article titles at all** — only venues.

We then recorded that as *"578 was wrong."* **It was not.** Crossref's publisher-deposited
`reference-count` for `10.1103/RevModPhys.90.031001` is exactly **578**
(`https://api.crossref.org/works/10.1103/RevModPhys.90.031001`, fetched 2026-09-05). 578 is the
deposited list; 595 is the printed bibliography. Two different objects, two true numbers — and
APS depositing unstructured references is also why the deposited list has no titles.

**The defect was never the digits. It was that the number was unattributed** — quoted and
promoted without a provider, an endpoint or a fetch date, and without anyone opening the
bibliography it was being used to characterise. An unattributed 595 would have failed the same
rule. What is genuinely false is the claim built on top: five IEEE entries make "zero
engineering" wrong as worded, and the subject characterisation had been reading a field that is
not in the data. The unattributed number reached five files before anyone opened the source.

So: fetch the reference list itself, check which fields it actually contains, and state which
field you classified on. "Zero engineering *by venue*" is supportable. "Zero engineering" is a
claim about subject matter that a title-free bibliography cannot carry.

Two tables from this project are publishable as-is with nothing but these queries:

- The gradient-harvesting zero table
- The multifunctionality zero table

The criticality audit was listed here as a third. **It is withdrawn.**

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
   than its **~9.9σ** suggests, because nothing over-determines it. (That figure was carried as
   "13σ" until 2026-09-03; the largest pair computable from CODATA-2018's own input table is
   ~9.9σ. See `vault/method/fine-structure-discrepancy.md`.)

### How discrepancies actually end

Not with better instruments. Deuterium abundance scattered over an order of magnitude in
the 1990s with rival camps, and resolved through **ruthless target selection and blind
analysis**. The kilogram resolved because two genuinely different methods were forced to
agree **as a precondition for redefinition**.

The transferable finding: **institutionalize cross-method agreement as a requirement.**

---

## 6. The analytical frame

Six moves recur across every field surveyed. None of them is "build a stronger thing."
All six are **structural** rather than **magnitude** moves — they change the arrangement,
not the amount.

| Move | Statement |
|---|---|
| 01 · Manufacture contrast | Signal under the noise floor? Don't amplify — create a local disparity that survives it |
| 02 · Use the noise | Efficiency is often non-monotonic in noise, with an optimum well above zero |
| 03 · Separate timescales | Don't build a faster actuator; decouple slow loading from fast release |
| 04 · Change the actor | When a theorem blocks the route, swap the category of the thing doing the work |
| 05 · Work inside the noise | Three postures — suppress, exploit, redistribute. Each community knows one. |
| 06 · Vary what was held fixed | A bound is rarely wrong; the list of things its derivation silently held fixed usually is. Full treatment in §8 |

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
  land" or "waiting on the four research agents" has not done the work. **Three occurrences
  so far.** Every one reported a plausible-sounding status and wrote no file.

  **Check the artefact, not the report.** The tell is always the same: the summary reads like
  progress, and the deliverable does not exist on disk. Verify the file before believing a
  completion.

  **The cause is delegation.** A capable agent given a large brief spawns sub-agents and
  reports on their behalf. So write the prohibition into the brief: *do not use the Agent
  tool; do the searching and fetching yourself; write the file yourself.*

  **When sending it back, give a priority order.** The failure recurs when the brief is
  large enough to feel unfinishable. Say explicitly which part to sacrifice — "fifteen
  well-sourced rows beat forty guessed ones, and the bias section is worth more than extra
  rows." An agent that knows what to drop does the rest rather than stalling.

- **Give partial-failure an honest home.** Every brief should name a marker for *checked and
  could not resolve* — `UNRESOLVED-IN-SOURCES`, `UNVERIFIED`, `ABSENT`. Without one, an agent
  facing an unanswerable item either guesses or stops. With one, the gap becomes data.

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

---

## 10. What makes a challenge productive

Neither the **size** of a discrepancy nor its **persistence** predicted which way it went.

- OPERA's faster-than-light neutrinos: nominal 6 sigma, dead in ten months to a loose
  fibre connector.
- The solar neutrino deficit: a factor of three, survived 34 years, and was real.

What the successful cases had was not a better argument. It was:

> **A measurement whose dominant systematic is independent of the assumption in dispute.**

SNO is the exemplar. Rather than arguing about the solar model, they measured two channels
**in the same detector** — one flavour-blind (neutral current), one electron-only (charged
current) — and took the ratio. The contested normalization cancelled. Thirty-four years
ended with one instrument built to be indifferent to the argument.

Parity is the other template: a theory named a specific test in advance, and someone ran it
within months.

So the weaker criterion — *propose a mechanism with a measurable signature* — is right but
incomplete. **Persistence alone was never evidence.** The neutron lifetime puzzle has now
outlived the entire period during which CP was assumed exact, sits at ~5 sigma, and the
field's working assumption remains systematics — correctly, on this record, until someone
builds the orthogonal measurement.

### Applying it here

For any open row in this project, the question is not "how big is the anomaly" but: **what
measurement would be insensitive to the thing being disputed?** That is the design target.

---

## 11. The synonym trap — a required step

**Discovered the hard way, and it threatens every co-citation claim in this project.**

    "Miner's rule"     AND "bone"  ->  0
    "Palmgren-Miner"   AND "bone"  ->  6

Identical concept. Different name. **One query manufactures a zero-crossing that does not
exist.**

### The required step

Before reporting any zero, re-run it against **every common name for the concept on both
sides**, including:

- Eponymous vs descriptive forms ("Miner's rule" vs "linear damage accumulation")
- Single-name vs hyphenated-attribution forms ("Miner" vs "Palmgren-Miner")
- The field's own jargon vs the neighbouring field's term for the same object
- British/American and older/newer terminology

A zero survives only if it survives all of them.


### Three failure modes, not one

The synonym trap turned out to be the mildest of four ways a zero can be fake. A systematic
re-run of this project's zeros collapsed two findings and downgraded a third.

1. **Punctuation and tokenization.** `"Miner's rule" AND "bone"` returns 0. `"Miner rule"`
   returns 2 and `"Palmgren-Miner"` returns 6. **The original zero was an apostrophe
   artifact** - not a synonym problem at all.
2. **Homographs.** `"multifunctionality"` is owned by both ecology and materials science with
   different meanings. Querying the bare word returns 9,570 hits that are entirely materials
   science. A careless check would "refute" a finding that is actually real.
3. **Proper-noun narrowness.** `"Paxos"` is one algorithm's name, not a literature. Anchoring
   a query on it measures the name. This is what killed G27.
4. **Synonyms**, the original case.
5. **Boolean relaxation** - and this one manufactures fake *nonzeros*, cutting the opposite
   way from the other four. Search engines relax to partial matching as OR-groups grow:

       two phrases, AND                          ->     1
       same, with synonyms added to each side    -> 1,169

   A thousand-fold jump from adding synonyms is the engine giving up on strict matching, not
   a bridge population. **Only 2-phrase conjunctions are trustworthy.** Treat any 4-way OR
   result as unusable without title inspection.

### The recurring mechanism, named

After nineteen findings re-tested, one failure dominates:

> **Anchoring on the term the *originating* field uses, rather than the term the *target*
> field uses.**

"Buckingham" (the target field does the work without the name), "gravitropism" (the physics
literature says gravisensing), "Berg-Purcell" (nobody outside chemoreception uses it) - each
produced a clean, confident, **wrong** zero.

**Corollary rule:** any zero anchored on a proper noun should be treated as unverified until
re-tested by citation intersection. On this project's evidence the prior for such a finding
surviving is **well under one half**.

### The homograph register

Words confirmed to be owned by more than one field. Never anchor a zero on any of these:

| Word | Owners |
|---|---|
| availability | reliability engineering; nutrient/light availability in biology |
| self-healing | materials science; **IT autonomic computing** (fault recovery, incident response) |
| rate limiting | network engineering; **biochemistry** (rate-limiting enzyme step) |
| autoscaling | cloud computing; **chemometrics** (NMR data normalization) |
| passivity | corrosion science; control theory (a dissipation property); political history; psychology |
| metastability | physics/chemistry; **ADC circuit design**; tumour dormancy; supramolecular polymerization |
| multifunctionality | ecology; materials science |
| quorum sensing | microbiology; social-insect collective decision |
| Buckingham | the Pi theorem; **a developmental biologist's surname** |
| LaMSA | latch-mediated spring actuation; CaMKII text; a **sociolinguistics** corpus |
| click beetle | the insect; **pheromone trap literature** |
| index policy | operations research; crop-insurance rainfall indices |

### The rule, hardened

**Any zero anchored on a proper noun, a possessive, or a word both fields own is invalid by
default.** Before reporting a zero:

- Run a **calibration query** proving each side is findable at all (e.g. `"dynamic soaring"
  AND "albatross"` -> 101 confirms the soaring side is searchable, so its zeros mean
  something).
- Run the concept under **every name**, including eponymous, descriptive, hyphenated and
  possessive-free forms.
- Prefer **reference-list intersection** over string matching wherever the citer count is
  tractable. The most robust finding in this project (G25) was measured by pulling 1,463
  citers and intersecting their bibliographies. String queries cannot be trusted at this
  level of consequence.

### Which prior findings are safe

Re-run completed, and its results were folded into the vault. **The verdict labels this section
used to carry (HOLDS / WEAKENED / COLLAPSED / DOWNGRADED / WITHDRAWN) are retired** — they
forced choices the evidence did not support, and `vault/_lint.py` now rejects them in any
machine field. See `vault/method/relationship-description.md` for what replaced them.

**Do not read a standing from this file.** Every gap's current standing lives in its note's
`standing:` field — a closed vocabulary of `live`, `narrowed`, `withdrawn`, `overturned` —
alongside an `evidence:` grade of `citation-intersection`, `full-text-read`, `string-protocol`,
`single-review` or `not-assessed`. `vault/00-index.md` is canonical; `vault/triage.base` sorts
the queue by weakest evidence first. The pre-vault snapshot of this table survives, with its old
vocabulary intact as history, in `ARCHIVE-findings-2026-09.md`.

What survives the re-run as a *method* statement, rather than a per-gap verdict:

- **Reference-list intersection beats string matching** wherever the citer count is tractable.
  The project's most robust finding was measured by pulling citers and intersecting their
  bibliographies, not by querying strings.
- **String-protocol findings have survived under half the time** when re-tested by citation
  intersection. Any gap still carrying `evidence: string-protocol` should be read as provisional.
- **A string count cannot overturn a gap either**, for the same reason it cannot confirm one.

### Positive controls now available

Mortality laws vs reliability theory came back **CLOSED**: 218 works co-cite Gompertz and
Weibull; 35 co-cite Weibull with the reliability-theory-of-aging paper. Against **0** for the
confirmed finds.

**The signal separates cleanly.** That is what makes the zeros meaningful — and it is why a
control should be run alongside any new gap claim, not just the claim itself.

### One-way bridges are still gaps

That same control is closed in only one direction. Of 633 works citing the reliability
theory of aging, **6 are reliability engineering** — under 1%. Biology imported the
engineering wholesale; engineering never imported back, and so has not adopted biology's
late-life mortality plateau or heterogeneous-redundancy results.

**Classify every result as TRUE GAP / ONE-WAY BORROWING / NOT YET A SHARED OBJECT / CLOSED.**

- **One-way borrowing** — B took from A; A does not read B. A real gap in the unread direction.
- **Forgotten bridge** — the link was built, used, and then lost. Signal detection theory
  originated in radar, moved to psychophysics, and reached camouflage biology third-hand,
  which no longer uses its sensitivity index at all.
- **Closed** — the signature is threefold: shared vocabulary, shared canonical citations, and
  **performance reported as a fraction of a theoretical bound.** That third property is the
  most diagnostic; a field that quotes its result as "86% of capacity" has a shared axis.

### Retired gap IDs

Eight G-numbers are cited in this file and in `ARCHIVE-findings-2026-09.md` but have **no vault
note**, and none is coming back. They are listed here so that no ID is silently reused and no
reader hunts for a file that does not exist. Reasons are drawn from the archived findings; there
are deliberately **no tombstone notes** — an ID with nothing to describe does not earn one.

| ID | Was | Why it has no note |
|---|---|---|
| G10 | Sub-38.6 µm gravity — untested regime below the shortest-range test | An experimental frontier, not a cross-domain gap: one field, no second literature to intersect. Fails the three-part test at step 1 |
| G13 | Measure a negative energy density (Wigner tomography on dynamical-Casimir output) | An undone experiment inside one field. Nothing to co-cite; belongs to `unexplored-window.html`, not the gap catalogue |
| G14 | Weigh vacuum energy (cryogenic balance on Casimir cavities) | Same class as G13 — under construction, no result. A proposal, not a measured absence |
| G15 | Settle the Casimir puzzle (plasma vs Drude model) | An open dispute internal to one literature; both sides read each other. There is no missing shared axis |
| G16 | Classical-gravity noise floor as a model-independent bound | A single 2026 theory result awaiting a measurement. One field, no crossing |
| G18 | Peak-to-average / turndown ratio vs factorial aerobic scope | Real and measured (co-citation 0 twice, against a 159-work internal control) but never written up as a vault note. Live candidate — re-open under a **new** ID with a full evidence block rather than reviving this one |
| G24 | Miner's rule vs bone fatigue | Not a zero: ~6 works over ~28 years. Thin, not absent, so it fails the third clause of the test. Its cautionary value — the apostrophe artifact — was promoted into §11 and `vault/method/failure-modes.md` |
| G26 | Crypsis vs stealth / signal detection theory | Reclassified NOT YET A SHARED OBJECT: 0 of 169 camouflage papers cite either founding text, and the fields measure different things. Nothing was borrowed and lost, so there is no gap to describe |

---

## 12. Precedent — this method has a name, and it is not ours

**Checked deliberately. The result is deflationary and must be carried forward honestly.**

The method is **Literature-Based Discovery (LBD)**, founded by Don R. Swanson in 1986.
The title of his 1987 paper is essentially this project's thesis statement:

> Swanson, "Two medical literatures that are logically but not bibliographically
> connected," *JASIS* 38(4):228-233 (1987).

**Non-co-citation as evidence of a real gap is Swanson's founding move**, not a refinement
we added. He found fish oil for Raynaud's syndrome that way, and it was confirmed in a
clinical trial in 1989.

### What must be cited, and stop being claimed

| Source | What it already established |
|---|---|
| Swanson 1986, *Library Quarterly* 56(2):103; *Perspect. Biol. Med.* 30(1):7 | Undiscovered public knowledge; the fish oil / Raynaud's discovery |
| Swanson 1987, *JASIS* 38(4):228 | Logically-but-not-bibliographically connected literatures |
| Small 1973, *JASIS* 24:265 | Co-citation as a measure |
| Kessler 1963 | Bibliographic coupling |
| Stirling 2007, *J. R. Soc. Interface* 4 | Rao-Stirling disparity - the standard measure of cognitive distance between fields |
| Uzzi et al. 2013, *Science* 342:468 | Atypical combinations quantified and shown valuable |
| Foster, Rzhetsky & Evans 2015, *Am. Sociol. Rev.* 80:875 | The risk/reward tradeoff of bridging strategies |
| Kostoff, *TFSC* 75:165 (2008) and the LRD series | Explicitly cross-domain, non-biomedical literature-related discovery |
| **Douard et al. 2025, *Sci. Rep.*, doi 10.1038/s41598-025-15067-9** | **101 million abstracts, engineering-biology topic graph, four validated case studies** |
| Boulding 1956, *Management Science* 2(3):197 | General Systems Theory - cataloguing cross-disciplinary isomorphisms, seventy years ago |

**We walked into our own synonym trap** (§11). This entire project has been running
literature-based discovery without using the term. Had the right name been queried at the
start, the precedent would have surfaced immediately.

### What honestly survives

| Feature | Status |
|---|---|
| Cross-disciplinary rather than biomedical | **Underexplored, not new.** Kostoff's LRD branch exists and is cited |
| Co-citation counts as gap evidence | **Fully standard.** Claim nothing |
| **Quantified metric on both sides as an entry criterion** | **Defensible.** No LBD method found gates candidates on commensurable quantification |
| TRUE GAP / ONE-WAY BORROWING / CLOSED | Mildly novel as a stated schema; the field names gap heterogeneity as an open problem |
| **Positive controls** | **A real contribution** - see below |

### Why the positive controls matter more than expected

After forty years, LBD's canonical set of *experimentally validated* discoveries is roughly
**two**, both Swanson's own. Kostoff (2007) showed three published LBD "discoveries" were
not valid discoveries at all, having passed peer review. Moreau (*Bioinformatics* 2023,
doi 10.1093/bioinformatics/btad090) argues the field "is built on sand" because its
evaluation rests on a cherry-picked handful of Swanson replications.

Running known-closed pairs as controls — which this project started doing by accident —
answers that documented, published, recent complaint directly. **That, and the
quantification filter, are the only two features worth claiming.**

### The honest positioning

An instrument built **on top of** literature-based discovery, not beside it. Working in its
thin non-biomedical branch, with two methodological additions and a curated standing
catalogue that does not appear to exist elsewhere — though that last absence rests on about
fifteen searches, not a systematic review.

---

## 13. Admitting other knowledge systems as data

Different knowledge systems have **different systematics**. Where an oral record and a
sediment core agree, the agreement carries weight precisely because their failure modes are
unrelated. That is METHOD 10 applied across knowledge systems rather than across instruments.

### The criterion, sharpened

Not "is it old?" but:

> **Does it have replication structure and error independence?**

Three properties, all required:

1. **Repeated observation**, not a single event
2. **Independently dated**, by something other than the phenomenon being inferred
3. **Observer motive uncorrelated** with the hypothesis now being tested

### The exemplar

Lake Suwa, Japan: **571 annual ice-freeze dates, 1443-2014**, recorded by Shinto priests as
a religious observance. Torne River, Finland: 320 years of ice breakup. The priests were
recording a ritual, so **their errors cannot correlate with a climate hypothesis nobody had
yet formed.** That is what makes it a dataset rather than a story.

### The criterion tested against every case

| Case | Repeated? | Independent date? | Motive independent? | Verdict |
|---|---|---|---|---|
| Lake Suwa / Torne | 571 / 320 annual | Calendar | Yes, ritual | **Passes cleanly** |
| Cascadia 1700 | 9 accounts | **Yes** - Japanese records, tree rings | Yes | **Passes** |
| Indigenous fire management | Continuous practice, tested prospectively | Tested by measurement | Yes | **Passes** |
| Terra preta | Physical, not oral | Radiocarbon | N/A | Passes as soil evidence |
| Artemisinin | Single preparation | N/A | - | **Fails as a dataset** - hypothesis generator only |
| Aboriginal sea-level traditions | **n = 1 per location** | **No - derived from the story** | Unknown | **Fails** |

**Cascadia's decisive feature:** the oral tradition was used to infer a Pacific Northwest
tsunami **eleven years before** Japanese documents dated the event. It was not fitted to a
known answer. That architecture is what escapes post-hoc matching, and it worked only
because a second, independently dated documentary system happened to exist.

### The failure modes, plainly

- **Post-hoc matching.** Know an event happened, go looking for a matching myth, and you
  will find one. Only independent dating escapes this.
- **Transmission decay.** Laboratory measurement gives roughly 0.2 information loss per
  transmission, an effective half-life of about three links. Critically, **evaluative gist
  survives while specific content degrades** - exactly backwards from what deep-time
  geomythology needs.
- **Structural blindness to long latency.** Traditional empiricism reliably catches acute
  toxicity and is systematically blind to delayed, low-base-rate harm with no felt link to
  the dose. Aristolochic acid: roughly 39% of a national population exposed, the world's
  highest urinary-tract cancer incidence, a unique mutational signature.
- **The base rates are worse than the romantic version.** Tested properly, n = 1,294 plant
  samples: traditional antimalarial use gave **17.9% highly active against a 21.1%
  baseline** - no better than random. The famous "74-80% of drugs match traditional use"
  conditions on drugs that already exist and **has no denominator.**

### The formalism already exists, in epidemiology

**Triangulation**: integrate approaches whose key biases are unrelated to each other and
ideally point in opposite directions. A quantitative version now exists that assesses bias
direction and magnitude per design, then meta-analyses with bias adjustment.

**This is the SNO move, formalised.** Nobody has applied it across knowledge systems, and
the leading indigenous-knowledge framework explicitly declines to, holding that evaluation
belongs within rather than across systems. So that argument is available to make, with a
ready-made skeleton and two worked cases where error independence demonstrably held.

### On independent and amateur researchers

Verified contributions: one man built a 9.6 m dish in his back yard in 1937 and essentially
founded radio astronomy alone. Amateur variable-star observation, **74 million observations
since 1911**. Amateur comet discovery, **over 4,000 since 1995**. Volunteer protein folding
solved a retroviral protease structure that molecular replacement and expert
crystallographers had failed to solve, with the players as literal co-authors.

**Correction to an earlier claim in this project.** I asserted that amateur meteor networks
publish uncertainty budgets while funded anomaly programs publish none. **That is wrong
about the Galileo Project**, which publishes intrinsic and extrinsic calibration, a 41%
acceptance rate, 36% mean detection efficiency, and calls its own outlier search a "toy."
The defensible contrast is **capability, not virtue**: multi-station astrometry yields
range, an infrared array does not, which is exactly why its ambiguous cases stay ambiguous.

**And there is no base rate for heterodox claims being right.** It may be ill-posed. The
denominator does not exist because publication deletes the failures; "turned out right"
selects on the outcome variable; and the category is defined relative to a shifting
consensus, so a claim stops being heterodox exactly when it wins. **If anyone quotes a
number, ask for the denominator.**

