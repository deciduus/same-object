---
name: log
type: method
---

# Operations log

## [2026-09-05] correction of a correction | 578 was never wrong — Crossref deposited 578, the printed PDF has 595

This project recorded a flagship lesson as *"578 was wrong, the real count is 595."* That
correction is itself wrong as worded, and the audit of 2026-09-05 caught it.

**Crossref**, `https://api.crossref.org/works/10.1103/RevModPhys.90.031001`, fetched
**2026-09-05**, returns `message.reference-count: 578` and `message.references-count: 578` for
Muñoz, *Rev. Mod. Phys.* 90:031001 (2018), publisher American Physical Society.

**Two objects, two true numbers.** 578 is the publisher-deposited reference list; 595 is the
bibliography printed in the PDF (extracted from arXiv:1712.04499). A deposited list and a
printed bibliography are not the same object and are not obliged to agree. This also explains
the "no article titles at all" finding: APS deposits unstructured references.

**So what the actual defect was.** Not a hallucinated number. The number was **unattributed** —
reported and promoted as publishable without naming the provider, the endpoint or the fetch
date, and without anyone opening the bibliography it was used to characterise. An unattributed
578 and an unattributed 595 fail the same rule. The subject-matter claim built on top of it
("zero engineering") remains false as worded: five IEEE entries, and a title-free bibliography
cannot support a claim about subject matter at all.

**Rewritten in:** `METHOD.md` §2, [[co-citation-audit]], [[G4-criticality-as-design]],
`ARCHIVE-findings-2026-09.md`, and this log. No file now says 578 was simply wrong.

## [2026-09-05] verification | OpenAlex returns 46 citing works for Alexander 1997

Recorded so the G19 / [[stress-strength-interference]] reconciliation has a trace before it is
run. **OpenAlex `cited_by_count` = 46** for Alexander, *A theory of mixed chains applied to
safety factors in biological systems* (doi 10.1006/jtbi.1996.0270), checked **2026-09-05** per
`audits/02-sources-citations.md`.

This contradicts the vault's own retraction: [[stress-strength-interference]] withdrew the "46
citations" figure as stale (offering 36/39/28 instead) while [[G19-safety-factor-derived-twice]]
still asserts 46. The external check says 46 stands, so the retraction is the error — the same
failure mode as the 578 entry above, uncaught until now. The "753 works" figure is a separate
question and is still a string-match artifact until someone attaches a provider and a date to
it. Reconciliation is backlog B2; this entry exists so that work starts from a dated number
rather than from a preference.

## [2026-09-05] migration | corrections log moved out of FINDINGS.md

`FINDINGS.md` was renamed to `ARCHIVE-findings-2026-09.md` and marked superseded by
[[00-index]] (backlog D14). Its **Corrections log** section is reproduced below, one entry
each, so that the live log is the only place corrections have to be looked for. Every entry is
preserved and marked `[migrated from FINDINGS.md]`. The date on each is the **migration** date,
2026-09-05 — the archive did not date its rows individually, and no date has been invented.

## [2026-09-05] correction (archived) | Neurons vs Landauer  [migrated from FINDINGS.md]

Claimed 10⁴; actually **10⁶–10⁸**. The 10⁴ is ATP *molecules*, and one ATP ≈ 20 kT

## [2026-09-05] correction (archived) | Vesicle cost  [migrated from FINDINGS.md]

Claimed 2.34 × 10⁴ ATP; actually **1.64 × 10⁵**. Kills the "one vesicle ≈ one bit" line

## [2026-09-05] correction (archived) | Halbach as a 20° switch  [migrated from FINDINGS.md]

Wrong. Field varies as the **half**-angle — 20° changes it by 1.5%; null is at 180°

## [2026-09-05] correction (archived) | Siberian permafrost seeds  [migrated from FINDINGS.md]

Not seed germination — tissue culture from immature fruit tissue

## [2026-09-05] correction (archived) | Fat vs TNT  [migrated from FINDINGS.md]

Barrier height is not the main reason. **TNT carries its own oxidizer**, so the reaction is intramolecular and can propagate supersonically. A power-density difference

## [2026-09-05] correction (archived) | Enzymes "not consumed"  [migrated from FINDINGS.md]

Wrong. 10³–10⁷ turnovers, then scrapped

## [2026-09-05] correction (archived) | G apparatus transplant  [migrated from FINDINGS.md]

Two agents disagreed on rebuild vs transplant; balance of evidence and the paper title favour **transplant**. Flagged, not settled

## [2026-09-05] correction (archived) | Loihi energy figure  [migrated from FINDINGS.md]

Quoted 23.6 pJ/SOP — not in the primary paper. Removed

## [2026-09-05] correction (archived) | Frugality asymmetry  [migrated from FINDINGS.md]

**Claim did not survive.** Reproductive effort runs ~25% of an annual energy budget. Conflated numerosity with cost per unit, then with total share. Biology is not profligate with reproduction — it is expensive, which is what life-history theory is about

## [2026-09-05] correction (archived) | Meteor vs Galileo contrast  [migrated from FINDINGS.md]

**Wrong as stated.** The Galileo Project does publish calibration, a 41% acceptance rate and 36% detection efficiency. The real contrast is capability - multi-station astrometry gives range, an infrared array does not

## [2026-09-05] correction (archived) | Crypsis as a forgotten bridge  [migrated from FINDINGS.md]

**Wrong.** 0 of 169 camouflage papers cite either founding text of signal detection theory. Nothing was borrowed and lost; the fields measure different things. Reclassified NOT YET A SHARED OBJECT

## [2026-09-05] correction (archived) | G27, collective decision  [migrated from FINDINGS.md]

**Withdrawn.** 26 hits in the original query. The zero was anchored on Paxos, an algorithm name rather than a literature

## [2026-09-05] correction (archived) | The energy-per-bit axis claim  [migrated from FINDINGS.md]

**Withdrawn.** 575 papers connect Landauer to neural systems. The specific figure may survive; the absence claim does not

## [2026-09-05] correction (archived) | G4, criticality  [migrated from FINDINGS.md]

**Downgraded.** 99 papers link Hopf bifurcation to the cochlea. A single-review omission, not a field gap

## [2026-09-05] correction (archived) | G11 plant gravisensing  [migrated from FINDINGS.md]

**Withdrawn.** Synonym artifact - the field says gravisensing, and the thermal-threshold calculation exists

## [2026-09-05] correction (archived) | G12 latch cycles-to-failure  [migrated from FINDINGS.md]

**Withdrawn.** S-N curves published for locust cuticle in 2013

## [2026-09-05] correction (archived) | G17 overconfident uncertainties  [migrated from FINDINGS.md]

**Withdrawn.** 279 citations including a direct quantitative follow-up. String matching would have confirmed it; the citation graph destroyed it

## [2026-09-05] correction (archived) | G21, G22, G9  [migrated from FINDINGS.md]

**Weakened.** Each overstated; narrower claims survive in all three

## [2026-09-05] correction (archived) | Hessdalen citation  [migrated from FINDINGS.md]

An agent invented a paper attribution. See `METHOD.md` §4

## [2026-09-03] verification | C8 novelty risk resolved by reading Greason in full

The novelty audit's top rediscovery risk was [[C8-momentum-harvesting-metric]] (Σ), because
Greason's shear-sailing paper had been read in abstract only. Read in full via ar5iv
(arXiv:2205.14117). It **does** define a bounded extraction efficiency (Eq. 11, `η_ext < 1`) — so
the *concept* of a bounded shear-extraction efficiency is not ours — but the specific
`Σ = P/(F·Δu)` bilinear identity, the `v/Δu` form, and the cross-branch span (soaring + sails +
tethers unified) are **absent** there. Verdict: **C8 is REPACKAGED, confirmed — not a straight
rediscovery**, and it was never in the NOVEL-4, so no headline change. Updated C8, novelty-audit
grade table, and the risk shortlist. The biggest open novelty question is now closed.

## [2026-09-03] correction | AARO is a contested referee, not a neutral arbiter

User flagged that AARO is widely cited as still on a discredit/opacity footing, not real
transparency. Sourced and correct — and it broke an assumption in our own [[disclosure-ledger]],
which had graded Version B "actively contradicted by the one investigation empowered to look."
That over-trusted AARO. Documented critique is multi-directional (Congress: "lack of
transparency," secret budget, Stars & Stripes 2025 + House Oversight; Kirkpatrick's pre-emptive
op-ed; the report omitting agencies and not engaging Grusch) — and the decisive point: Grusch
alleged AARO was **stonewalled / denied access**, so "no evidence found" may be
absence-of-access, not absence-of-thing.

**Fix:** Version B softened from "refuted" to **uncorroborated**, its main institutional refuter
downgraded from verdict to contested evidence. Does NOT move Version B toward true — a contested
refuter widens uncertainty, it does not fill it. Symmetry kept: much of the loudest AARO
criticism is from the camp AARO declined to validate (motive to discredit the discreditor), so
"AARO is contested" is sourced while "AARO is a cover-up" stays a testimonial claim. Generalised
into [[evidence-lanes]] as the **referee-is-a-player trap**: the body being investigated cannot
be the trusted arbiter; downgrade its conclusion to evidence and require an orthogonal check it
does not control — which [[Q1-what-gets-checked]] says does not exist here.

## [2026-09-03] corpus mined | ledger faceted, primaries archived, prediction holds only weakly

[[C22-ledger-faceting]]. All 24 ledger entries faceted on the seven [[testimony-taxonomy]] axes.
**The access-basis prediction holds qualitatively, not statistically**: firsthand-data/documentary
confirms ~69%, firsthand-observation ~17%, secondhand/hearsay 0/2 — but 16 of 24 rows are
institutional documents, so the witness-claim subset is **N≈9**, and there the *referent* confirms
**0 of 9**. Honest landscape reading: firsthand sensor-data gets acknowledged; secondhand
recovery/biologics claims stay open. Too small to weight further.

Q1 sort of open items: **checked-and-unresolved** = Fravor/Graves (expensive unfunded multi-sensor
check); **unfalsifiable/unfundable-from-outside** = Grusch, Nell, Gallaudet, Mellon, Stratton
(classification-gated).

Primary text archived to `vault/sources/` (verbatim via pdftotext): **ODNI 2021** (Wayback mirror,
archive.dni.gov 403'd), **Gallaudet 2024 testimony**, **2023 House Oversight hearing transcript**
(GPO 118-53, carrying Grusch's verbatim "I was informed" secondhand framing). **AARO FY2024 could
not be fetched** on any route (403 everywhere, no Wayback) — recorded as blocked, nothing
reconstructed. PURSUE portal 403'd; a clearly-labelled SECONDARY extract saved instead. Raw PDFs
gitignored under `sources/raw/`; extracts committed under `vault/sources/` (excluded from lint).

## [2026-09-03] honest scorecard | [[novelty-audit]] grades the whole vault

Every substantive result graded, bias set toward the lower grade. ~50 gradable results:
**4 NOVEL** (C5 strongest, then the [[Q7-same-class-prediction]]/C16 conditional, C6, C4 hedged),
**~20 REPACKAGED**, **2 REDISCOVERED** (C9 thermoacoustics, kedem-caplan in active use),
**~20 LOCATED** (gaps + C15's impossibility), **~8 CORRECTED** (the 578 fix, sail conjugate-pair,
neutron-lifetime, two citation counts, three overturned zeros, the G11 100× fix).

Honest one-line product: **a method plus a curated catalogue holding a handful of genuine
bridges — not a body of new physics.** The largest bucket is REPACKAGED; locating a
well-measured gap is real work but not novelty. Strongest novel: [[C5-charnov-gittins]]. Most at
risk of being an unrecognised rediscovery: [[C8-momentum-harvesting-metric]] (Greason
arXiv:2205.14117 read in abstract only). The audit predates C21/C22, which are themselves a
method-finding and a provenance-faceting, not new-physics claims.

## [2026-09-03] honest null | Q10's strong reading refuted by its own test

[[C21-rediscovery-clustering]] ran the falsifiable edge Q10 set for itself. **The rediscovered
objects do not concentrate** — 18 instances across 11 object-types, Hill N2 ≈ 9.0, near-uniform.
The clean bias-controlled sample (Q2's six independent rediscoveries) scatters one-per-type. The
apparent 72%-into-six-types is the selection confound made visible: the specification-instrument
method is built to retrieve those forms, and the only real repetition (Weibull ×3, index-policy
×3) is the project reusing its own lenses. Strong claim (knowledge = one substrate-independent
logic) refuted; weak claim (the *method* converges on a small toolkit) survives. The frame is
demoted from a fact about the world to a fact about the tool. The method was allowed to kill the
hunch, and did — which is the point.

## [2026-09-03] disclosure thread | sourced ledger, PURSUE added, and the lane doctrine

**[[disclosure-ledger]]** — 24-entry provenance ledger of the post-2017 US UAP disclosure thread,
built to the claims-register discipline (testimony sets specification, not mechanism). Primaries
read verbatim (ODNI 2021, AARO FY24). Honest split: **Version A** (official secrecy + unexplained
sensor data were real and got acknowledged) **checked out**; **Version B** (recovered non-human
hardware/biologics) is not established and was pushed back on by AARO. Collapsing A into B is the
topic's central reasoning error.

**Corrected my own hedge and added [[disclosure-ledger]] rows 23–24.** The user pointed to a real
2026 development I had waved off as probably-unverifiable; a verified web search confirmed the
**PURSUE** release (2026-05-08, five tranches) including declassified Apollo astronaut transcripts.
Tiered DOCUMENTED (transcript) / OPEN (referent) — a genuine upgrade of Apollo "unexplained lights"
from lore to primary source, strengthening Version A, silent on Version B. Note on my own epistemics:
edge-of-cutoff recall is unreliable, so I default to fetching rather than asserting — the same
reading-not-counting rule applied to myself.

**[[evidence-lanes]] — the doctrine the user articulated.** Verification is non-negotiable, but no
lane earns 100% trust: academic, documentary, testimony, and traditional/oral each carry a
characteristic bias, and the project has proven its *own* home lane leaks (Q1, Q8, unread theorems,
the 578 error). The referee is not authority within a lane but **convergence across
orthogonally-biased lanes on the same checkable observable** — the same logic as the reservoir
audit and the same-class conditional. Explicitly not relativism: the method is the one thing that
is not biased, applied identically everywhere. The ledger's selection-bias section now states this
symmetry.

## [2026-09-03] method | press, feel, dig — WASD by resistance gradient

The user named the method's own shape: the way we work a gap is the same move as the instrument
([[reservoir-audit]]) and the founding engine — press, feel where it resists, dig where it
gives. Sharpened to a WASD analogy: don't choose a heading, tap each button, read the resistance
gradient, follow it. **The project studies coupling to a gradient and proceeds by coupling to a
resistance gradient** — the map runs the territory's algorithm. [[press-feel-dig]].

Operational change adopted: task agents with an **object and a set of buttons, not a verb.** The
verb (build/narrow/kill/harden) is an output read off the resistance. Evidence: every strong
result this session came from verb-agnostic "build it or prove it can't" briefs.

## [2026-09-03] Layer-2 five-fan | Q7 hardened, G3 bridged

**[[C16-same-class-catalogue]] hardens [[Q7-same-class-prediction]] to N=16.** A 24-case
same-class sample built to hunt a counterexample found none: 16 systematics, 1 fluctuation, 0
new-physics. The flagged danger case — gravitational-redshift clock comparisons — survives,
because the redshift is a computed correction applied *before* any residual is called a
discrepancy. The conditional holds and stays bias-immune. (Tenth-order QED corrected to ~5σ.)

**[[C18-durability-axis]] narrows [[G3-cycle-life]] and produces a bridge.** A cycle count hides
the failure law; the shared coordinate is the **Weibull shape β** — β=1 enzyme catastrophe
(memoryless), β>1 Li-ion wear-out. New result: organic flow-battery reactants fail by
calendar-time chemical decay, **β≈1, the same law as enzyme death** — reclassified with enzymes,
isolating Li-ion as the outlier. Ties to [[stress-strength-interference]]'s discrete-vs-continuous
split.

**[[C17-offset-from-threshold]] narrows [[G4-criticality-as-design]] with a real invariant.**
"Distance from threshold" is near-tautological — gain ∝ ε⁻¹ with exponent 1 in every class
*because* a simple pole's resolvent is 1/distance. One level down: bandwidth ∝ ε, so
**gain × bandwidth = c·rate, conserved along the offset axis in all three classes** (hair cell,
parametric amplifier, cortex). The parametric-amp field already states `B·√G = const`; it
transfers unchanged to cochlea and cortex, neither of which writes it.

**[[C19-hormesis-biphasic-fit]] narrows [[G23-hormesis-formalism]].** The parameterised biphasic
curve — the deliverable G23 said was absent — was fitted from shot-peening dose sweeps. **Window
width ≥15× (≈73× fitted) meets biology's 10–20×**; the amplitude ceiling matches biology's 30–60%
*once the response axis is matched* to fatigue strength (AA 7075 +82% verified), and the Basquin
exponent `N∝σ⁻¹⁰` is the translation to the order-of-magnitude-larger fatigue-*life* gains. Narrows
toward partial closure; not a full close (two ceilings, no single theorem).

**[[C20-release-the-constant]] turns move [[M6-vary-what-was-held-fixed]] into an integer
operator — and it re-derives gecko contact-splitting blind.** A capability is constant-bound when
a Π-group carries a lone fixed constant; the operator adds a column carrying that constant's
signature so it re-enters a tunable ratio, and emits the dimensional signature the new quantity
must have. Run blind on the gecko matrix (`σ_c ∝ (Ew/R)^½`, `R ∝ √A` → `A^{−1/4}`), it emits
"add a length independent of A" — exactly the sub-contact radius, recovering the Arzt–Gorb–
Spolenak `√n` law. On a kT wall it emits the active-drive `kT_eff` escape. Honest limit: it
returns the *dimension* a fix must have, not that a fix exists — separating a real impossibility
(ratio of two fixed constants, e.g. Schmidt) from a lead. Makes [[G22-scale-transfer-triage]]'s
triage the actionable, finite search G22 said nobody had built.

**Five-fan complete.** Pressed five nodes; the resistance wrote five different verbs — Q7
*hardened*, G3 *bridged*, G4 *narrowed to a real invariant*, G23 *narrowed toward closure*, M6
*formalised into an operator that validated blind*. Not one verb was assigned in advance.

## [2026-09-03] headline hardened | four unread theorems citation-tested, all survive

[[C13-unread-theorem-audit]]. After [[kedem-caplan]] collapsed under an actual check, the other
four "unread theorem" claims were tested the same way — inspected citation intersection, not the
bare co-citer count that sank Kedem-Caplan. **All four are genuinely still-unread. None is in
active use.** The headline pattern is hardened, not damaged further.

- **Kirkwood** strongest: 0 of 5,075 self-healing citers cite it, 99.4% coverage; reverse sweep
  0 materials venues among 368 journals.
- **Hill-number** validated the pipeline: control (Byrnes × Jost) fired at 7, so its 0 is real.
- **Availability** and **stress-strength** both 0, the former weaker because availability is
  textbook not a citable paper.

Two more stale vault numbers corrected in passing: Alexander 1997 is **36/39/28 citations, not
46**, and the engineering "**753 works**" was a string artifact (relaxed match ~1.8M),
withdrawn. The "0.25" structural-battery figure — already withdrawn in G6 — was still sitting in
[[hill-number-multifunctionality]] and is now struck there too.

Honest residual: hardened only to the citation-intersection level. A parallel derivation that
never cites the anchor is invisible to counting; the next move on any is a full-text near-miss
pass, not another count.

Endpoint traps logged in [[citation-sources]]: OpenCitations `/citation-count/` returned a bogus
constant 1 all session; Crossref `select=reference` 400s.

## [2026-09-03] Layer-2 batch | two gaps given constructions, both instructive

**[[C14-degree-of-passivity]] narrows [[G7-how-passive]].** The naive "fraction of response
surviving" is broken (exceeds 1 for protective devices; the subtraction is meaningless under
nonlinearity). Recast as a cycle-averaged **energy** fraction, `P` is portable. And the ladder
is the **Boolean square B²** on two independent bits — *injects energy?* and *needs a signal?*
Exoskeleton "quasi-passive" and structural "semi-active" are the **same cell**; cell (1,0) is
unnamed in every field; "hybrid" is a sum, not a rung. No total order carries a width-2 lattice,
so each field linearised it differently — the same failure as [[C12-pi-space-lattice]]. `P`
closes the energy axis (control theory's passivity index is its rigorous twin there) but is blind
to the signal axis. Narrows, does not close.

**[[C15-metastability-metric]] kills the [[G2-metastability-metric]] unifier — cleanly.** The
"6 kJ/mol buys 10×" arithmetic silently drops the prefactor `ln τ₀`. Backed out from real data,
τ₀ spans **~20 orders**: TST period for MOST, 10⁻² s for seeds, no kT at all for nuclear isomers,
non-Arrhenius for PCM. No single number on `exp(ΔG/kT)` can span them. Salvage: a 2-D map holds
the two thermally-activated classes and separates them by prefactor, not barrier — **biology buys
lifetime in the prefactor, chemistry in the barrier.** A C9-style negative.

Both are Layer-2 constructions per [[strategy]]: take a gap, build the missing object, and read
what the attempt reveals. One narrowed, one produced a clean impossibility plus a salvage.

## [2026-09-03] instruments at the antifragile level | two more built, one gap closed

The user named the through-line: the reservoir audit is a **specification instrument** — an
antifragile tool that turns "impossible" into "here is what the missing partner must be." Wrote
[[specification-instruments]] and built two siblings, one energetic-discrete, one purely discrete.

**[[information-audit]] — the entropy sibling.** Same four steps, conserved quantity = entropy.
Validated **3/3** on measured experiments (Bérut 2012 Landauer, Toyabe 2010 Maxwell demon, Koski
2014 Szilard), **naming the sink each time.** Toyabe was its Pioneer: the audit identifies the
demon's **memory register** as the initially-unnamed sink closing the balance. Then it ties
[[G25-proofreading-coding]] to the same ledger — proofreading pays `k ln2` per rejected bit out
of ATP, the exact analogue of memory-erasure cost. (My brief gave the wrong arXiv id for Bérut;
the agent caught it and used the review with the same numbers.)

**[[C12-pi-space-lattice]] — the discrete one, and it closes a gap.** Buckingham's Π-groups are
the integer kernel of the dimension matrix. A 3×10 matrix mixing organism and process quantities
has rank 3 → 7 Π-groups, and Froude, Reynolds, Péclet, Damköhler are **all vectors in one
lattice.** So [[G21-dimensionless-regime-map]]'s surviving half — "no Π-space co-locates
organisms and processes" — **closes by construction.** New object: transport crossovers are
lattice-locked (Π-difference supported only on Schmidt/Prandtl/Lewis constants), which turns
[[G22-scale-transfer-triage]]'s constant-bound criterion into lattice arithmetic. The two gaps
are now tied through one integer-lattice object.

Both output files verified on disk before the agents reported done.

## [2026-09-03] two free buildables run | both compounded

**[[C10-healing-curve-fit]] — the curve fit that tests our own number.** Seven cycled datasets.
The rate-balance case ([[Q4-healing-needs-a-new-law]] candidate 2) is supported by **none** of
them; healing efficiency decays monotonically. So `k_r` is not constant, `Ha` becomes `Ha(N)`,
and [[C6-damage-healing-ratio]] describes at most the first cycle. The failure is
class-dependent — microcapsules and high-crosslink vitrimers deplete to a floor (Kirkwood
confirmed and still uncited), low-crosslink vitrimers decay to zero. This **answered Q4** and
**re-specified the paid vitrimer measurement**: measure the depletion parameter, not a scalar.

**[[C11-flyby-reservoir-audit]] — the audit's first open case.** Reproduces the flyby empirical
formula to 1.3%, then excludes every static reservoir on availability: geomagnetic tether
A≈3×10⁶ (the tempting one — K literally contains Ω — fails hardest), drag A≈30 wrong sign,
thermal A≈300 wrong sign (Rievers-verified against Rosetta). Sign + non-recurrence leave **no
static reservoir standing**. Residual specification: 1–9 mN, along-track, scaling as 2ΩR⊕/c,
non-stationary in epoch — which points at an analysis systematic first.

Neither delegated. Both output files verified on disk before the agent reported done — the
placeholder check from §7 held.

## [2026-09-03] schema | a `question` type, because the vault could only record damage

Every machine field measured whether a claim **survives**. There was nowhere to put what a
finding **opened**. So the vault reported demolition even in a session whose substantive output
was two theorems, a named experiment and a falsifiable prediction — and the reporting followed
the instrument.

Same error as [[verdict-scoring]], turned inward: a taxonomy that measures one thing gets
mistaken for the terrain.

Seven questions harvested, six of them from findings that had been filed purely as losses. See
[[Q6-negative-results-in-the-vault]]. Open question raised there: **one door per gap damaged may
be the natural rate**, in which case earlier audits generated them too and nobody wrote them down.

## [2026-09-03] computed | C7, and the conditional that survives its own bias

39 cases. Raw tally 20 SYSTEMATICS / 14 OPEN / 1 NEW-PHYSICS / 2 THEORY-ERROR / 1 REDEFINITION /
1 UNRESOLVED — **explicitly not a base rate.** Three of five biases push the same way; the true
systematics share is higher and new-physics lower, by an unknown amount.

**The finding is not the fraction.** Every closed *same-class* disagreement resolved to
systematics, seven for seven. A conditional needs no denominator, and the missing invisible cases
can only add more systematics — so the bias cannot cut against it. That becomes a dated,
falsifiable prediction about the fine structure constant in [[Q7-same-class-prediction]], and it
tells us where **not** to look, which is new.

Two schema findings for the next pass: FLUCTUATION and MISCONDUCT labels are needed with
multi-labelling (3 rows in 39 do not fit), and **outcome labels have a shelf life** — muon g−2
was reclassified mid-catalogue after the 2025 White Paper; the reactor anomaly was closed in 2021
and has partly revived.

Append-only. One line per structural change to the vault. Format:
`## [YYYY-MM-DD] operation | description`

## [2026-09-03] our own claims tested | G9's four features, one refuted and one wrong on facts

The first time this project turned the counterexample hunt on **its own reasoning** rather than
on a literature. Three of four survived only in weakened form.

**Feature 2 — "single-group claims resolve against the claimant" — REFUTED.** Homestake, CP
violation 1964, and Wu 1957 are all vindicated single-group claims. Number of groups predicts
nothing; the cost and motivation of the check does. The corollary — a decade of silence means
the claim is dead — cannot separate *obviously false* from *unfundable*, and its own flagship
case refutes it: **DAMA was checked**, by ANAIS-112 and COSINE-100, because refuting it was
publishable.

**Feature 4's flagship example was factually wrong.** We wrote that an independent relation
picks a side in the neutron lifetime. It does not: meson-decay V_ud favours beam, superallowed
0⁺→0⁺ V_ud favours bottle, and PERKEO III and aSPECT split the same way.

**Feature 1 is unfalsifiable as used** — "same method" is undefined and gets assigned after the
answer is known.

**The reframe that saves them:** three of the four do not classify outcomes at all. They
localise where the residual uncertainty lives. Under that reading every counterexample is
consistent. Smaller claim, true one.

**And Homestake was already in the note** — listed as the counterexample to the base rate. Nobody
had noticed it also falsifies one of the note's own features. The instances were catalogued and
never cross-checked against each other.

## [2026-09-03] citation-intersection | both survivors tested at the hardest standard

Run on Crossref + OpenCitations per [[citation-sources]]. **Both hold.**

**[[G6-multifunctionality]] — intersection 0** across six anchor pairings, coverage 77.5–100%,
and widened: 172 engineering citers cite zero references from eight core ecology journals, 861
ecology citers cite zero from six composites journals. **No contact either direction across
1,033 works.** Positive control Byrnes × Jost = **17**, reproduced exactly by both sources —
and it is the right control, because it is a metric formalism *being* imported into a
multifunctionality literature. The pipeline detects that event. It does not happen here.

**This is the only entry in the project to survive both standards**, which fail differently.

**[[G28-marginal-value-gittins]] — intersection 5 of 1,013 (0.49%)** against a positive control
of **22.2%**, a factor of 45. Both sources returned the identical five DOIs. All five inspected;
**zero are real bridges.**

But one sentence is now false: *"operations research and behavioural ecology have no direct
contact at all."* **Griebling et al., *Animal Behaviour* (2026) cites Charnov, Gittins 1979 and
the Gittins 2011 book.** Direct contact, newly emergent. Restated as vanishingly thin rather
than absent, and added to the outstanding checks.

Also corrected: the old **181 / 11.7%** Sutton & Barto control came from OpenAlex and returns
**24** here, because the book has no proper DOI. Method-dependent; the 24 is not carried forward.

## [2026-09-03] re-read batch two | G20 overturned, G22 upgraded, G4 audit finally run

**[[G20-resize-vs-throttle]] overturned.** Textbook anchoring on the originating field's term.
Computing has the symmorphosis question with formulas, under **over-provisioning accuracy**
(arXiv:1905.10270) — and the word "safety" appears zero times in that paper. Worse, safety
factors are *native* to mechanical engineering, so "never reached mechanical engineering"
inverted the direction of travel.

**[[G4-criticality-as-design]]: we had characterised a bibliography we never opened.** The
Muñoz *RMP* reference list was finally extracted. The printed PDF bibliography holds **595
refs** against the **578** that had been quoted — and **it carries no article titles at all**,
only venues. Every prior subject-keyword characterisation of it was reading data that does not
exist. Five IEEE entries, so "zero engineering" is false as worded. The review cites Stoop's
theory papers and omits his cochlea *hardware*.

*(Corrected 2026-09-05 — see the entry at the top of this log. 578 is not an error: it is
Crossref's publisher-deposited `reference-count`. Two objects, both true. The defect was that
the number was unattributed.)*

**Propagation traced and corrected.** The 578 figure was tracked back through the session
transcript to a research agent's report, and from there to my own relay of it as *"directly
publishable as-is... needs nothing but a database query"* — asserted without ever opening the
bibliography, and without naming where it came from. It had reached **five files**: `FINDINGS.md`
(now `ARCHIVE-findings-2026-09.md`), `README.md`, `METHOD.md`,
`vault/method/co-citation-audit.md` and the published `inquiry-map.html`. All corrected except
the artifact, which needs a republish.

The criticality audit is **withdrawn from the "publishable as-is" list** in all three places
that carried it. Two remain.

`METHOD.md` §2 and [[co-citation-audit]] now carry a hard precondition: fetch the reference
list itself, check which fields it contains, and state which field you classified on. A
title-free bibliography cannot support a claim about subject matter.

**[[G22-scale-transfer-triage]] upgraded to live.** The two-agent disagreement was adjudicated
by pulling Perricone 2021 and searching it directly: Buckingham 0, dimensionless 0, screening 0,
protocol 0. The paper's closing line asks for the guidelines, so it cannot be them. New named
failure: mistaking *naming the problem* for *supplying the procedure*.

## [2026-09-03] hygiene | lint now rejects a UTF-8 BOM

A PowerShell `Set-Content` rewrite prepended a BOM, which silently broke frontmatter parsing —
the note reported `no type` while looking perfectly correct in an editor. Caught by the lint
only because `type` is required. Now checked explicitly.

## [2026-09-03] closed by construction | C5 and C6 write two missing objects

First time this project produced theorems rather than catalogue entries. Both were attempts to
**close** a gap by writing the algebra, per [[what-closes-a-gap]].

**[[C5-charnov-gittins]] — the strongest result here.** Charnov's marginal value theorem *is*
the Gittins index, as an identity in two lines. Charnov's maximisation over residence time is
literally the supremum over stopping times in the index definition. The travel time τ is neither
a switching cost nor zero; it is a zero-reward prefix inside the outside arm, licensed by
patches being non-revisitable. A 2024 bioRxiv paper derives `g'(t*) = λ·EV`, which is Whittle's
`ν = δM`, with zero occurrences of Gittins — independent rediscovery that validates the algebra
and demonstrates the gap at once.

**[[C6-damage-healing-ratio]].** `Ha = k_r/k_d` with fixed point `A = Ha/(1+Ha)`, reducing to
`MTBF/(MTBF+MTTR)`. No prior art. Two by-products beat the group itself: the reason nobody wrote
it is **experimental** — materials science cannot suppress healing while loading — and setting
`ḣ = 0` in the Das & Kumari law gives `h → 1` always, so continuum damage-healing mechanics has
**no interior steady state in the healing variable**. A defect found by trying to use the law.

## [2026-09-03] correction | my own claim about the ablation test was wrong

I wrote that the pooling prediction was "one re-analysis away" from a test against Blancaflor
1998. **It is not.** `τ_p ∝ M⁻¹` is equally the prediction of plain linear summation; the models
separate only in the *angular* exponent, and that stimulation was done at 90° only. The
discriminating measurement was never made. Corrected in [[C4-inclination-sensing-limit]].

Also: `M` resolved to **48**, not 12 — the old figure was a median-section undercount by exactly
4×. And equal-weight pooling is falsified outright: at fixed `M = 16`, presentation time runs
2.62 to 7.13 min depending only on which story survives. **Cell identity dominates cell count.**

## [2026-09-03] unblocked | citation-intersection was never actually blocked

Recorded as blocked because OpenAlex and Semantic Scholar both returned 429 with hours-long
Retry-After. **Wrong conclusion.** Three other providers work, verified live:

- **Crossref** returns full reference lists with DOIs — 71 refs, 70 with DOIs, on the spot check
- **OpenCitations COCI** returns both citers and references, and agreed with Crossref at 71
- **Europe PMC** returns citers by PMID — 49 on the same work

Two independently assembled sources agreeing is the verification. See [[citation-sources]].

The lesson generalises and is now a rule: **a blocked API is not a blocked method.** Never mark
something `not-assessed` on one vendor's failure without checking whether another answers the
same question.

## [2026-09-03] re-read batch | eight gaps read in full, six damaged

Fanned out on the eight `string-protocol` survivors. **Two held, six narrowed. None overturned.**

| Gap | Outcome |
|---|---|
| G6, G28 | held |
| G1 | thermodynamic branch already unified; only the momentum branch survives |
| G2 | "absent from biology" false — seed ageing uses Arrhenius Ea |
| G3 | one leg bridged by name in PNAS 2021 |
| G5 | "no time in it" false — CDHM has healing rate constants |
| G7 | the ladder is reinvented in four fields, not nuclear-only |
| G23 | shot peening names its own descending limb |

**Every one of the six was damaged in the same way**: a supporting sentence claimed a field
lacked a *concept*, when the field had the concept under another name. The surviving claims are
all about missing **formalism** — a parameterised curve, a dimensionless ratio, a shared axis.
That is the sharper class of claim, so the batch improved the catalogue rather than shrinking it.

Also corrected: `structural batteries score ~0.25` in G6 is **UNVERIFIED and withdrawn**; papers
read give 1.15–1.17.

## [2026-09-03] correction | kedem-caplan is not an unread theorem

Catalogued as one. The re-read found it in active use — *Entropy* 25:1575 (2023) applies it to
thermoelectrics and oxidative phosphorylation together, and arXiv:2403.20209 clones the form
into a hydronic figure of merit. The "2 co-citers" figure measured traffic between two named
papers, not whether the result had travelled. It had.

This damages the project's headline pattern for that entry specifically. Recorded rather than
quietly fixed.

## [2026-09-03] computed | C4, and it does not close

`C4-inclination-sensing-limit`: minimum detectable tilt for a single statocyte comes out
**≈11°**, which is **above** the observed thresholdless response. The single-cell model fails,
and that is the result — it forces pooling across statocytes, predicting threshold degrading as
M^(−1/2). An ablation series that could test it already exists (Blancaflor 1998), analysed for
presentation time instead.

## [2026-09-03] correction | G11 statolith energy was wrong by ~100x

The note claimed a single statolith displacement costs **2–3 k_BT**. Recomputed from Bérut
et al. 2018 (PNAS 115:5123): buoyant mass 1.91×10⁻¹⁴ kg, d = 4.5 μm, so mgd = 8.4×10⁻¹⁹ J
= **~205 k_BT**. The check: this gives Pe⁻¹ = 4.9×10⁻³, inside the paper's stated 3–8×10⁻³.

2–3 k_BT is roughly the cost of a **66 nm** displacement — a derived *threshold*, not the
*cost* of a displacement. The two were conflated.

## [2026-09-03] restored | G11 withdrawn → narrowed, evidence full-text-read

The withdrawal cited Miyamoto 2007 as a limits-to-sensing analysis. It is an experiment
(flax roots, 5 Hz, 0.5 mm oscillation). A withdrawal misdescribed its own source — the exact
failure the symmetry rule was written to catch, caught only by reading.

## [2026-09-03] vocabulary | evidence gains full-text-read

Ranked between citation-intersection and string-protocol. Means the primary sources were
read, not counted. Added because [[G11-plant-gravisensing]] had no honest grade available:
three papers read in full is not `single-review` and is plainly stronger than
`string-protocol`. Enforced by `_lint.py`.

## [2026-09-03] atomic-schema migration | 20 gap notes converted

Prose frontmatter replaced with filterable data. `contact-surface: "0 crossings, both
directions"` became `contact-surface: 0` plus `crosses`, `crosses-rank`, `topology`,
`mediator`. Six typed directional edge fields added. Tag mirrors added.

Reason: prose in a machine field cannot be sorted, filtered, or linted. The defect that
prompted it — [[verdict-scoring]] was marked retired while a gap still carried
`status: holds` — was a retired word sitting in current frontmatter with nothing to catch it.

## [2026-09-03] lint extended | atomic vocabularies enforced

`_lint.py` now checks the `crosses` vocabulary, that `crosses-rank` agrees with `crosses`,
the `topology` vocabulary, that `mediated` and the `mediator` field agree, that
`contact-surface` is a bare integer, and that all six edge fields are present.

## [2026-09-03] graph and Bases added | zero plugins

`triage.base` and [[graph-view]]. Both are core Obsidian. Bases reads YAML frontmatter only,
which is why the migration had to land first.

## [2026-09-05] provenance | G25's coverage was 28.4%, and the note never said so

[[G25-proofreading-coding]] is the project's headline citation-intersection finding, and its
coverage figure was buried inside a table cell: **416 reference lists retrieved out of 1,463
citers = 28.4%.** [[G6-multifunctionality]] ran the same instrument at **77.5–100%**. Surfaced
the number in the body and in the frontmatter `note`, with the G6 comparison stated as the
standard this note does not meet. Added a full `## Provenance` block: both anchor DOIs verified
live against Crossref (Hopfield 1974 `10.1073/pnas.71.10.4135`; Shannon 1948
`10.1002/j.1538-7305.1948.tb01338.x` — both correct), and citer counts re-derived today:
**Crossref 1,340 / OpenCitations 1,593 / OpenAlex 1,656** against the original **1,463**. The
24% spread between providers is larger than two days of growth, so **1,463 is provider-dependent
and its provider was never logged.** The 3.8% and the coding-theory zero are computed inside the
416 actually inspected and survive the ambiguity.

## [2026-09-05] provenance | four Gittins denominators were one number, badly measured

[[G28-marginal-value-gittins]] carried 1,542, 1,013, 1,010 and an implied base for "0.5%".
Replaced with one provider table: run-time enumeration **1,013** (2026-09-03, provider not
logged, most likely OpenCitations), **Crossref 986**, **OpenCitations 1,026**, **OpenAlex 1,544**
— all fetched 2026-09-05. **1,542 was OpenAlex**; today it returns 1,544, which confirms the
identification. Stated explicitly that **both headline percentages use 1,013** and showed the
arithmetic: `5/1013 = 0.49%`, `225/1013 = 22.2%`, ratio `45.0`. The factor of 45 is
denominator-invariant; the individual percentages are not. Added the positive control's anchor —
Auer, Cesa-Bianchi & Fischer 2002, **`10.1023/A:1013689704352`**, verified against Crossref —
and stated the query behind 22.2% as a set intersection of the two citer lists.

## [2026-09-05] verification | Griebling 2026 located; it is the raccoon paper

The one asserted direct ecology→operations-research contact in [[G28-marginal-value-gittins]]
was an unlocated reference. **Found via Crossref works search:** Griebling, Johnson &
Benson-Amram, *Raccoons optimally forage for information: exploration–exploitation trade-offs in
innovation*, *Animal Behaviour*, April 2026, **`10.1016/j.anbehav.2026.123491`**. Its deposited
reference list (100 refs) **contains Charnov 1976, Gittins 1979 and Gittins 2011**, so the
co-citation is confirmed from the primary record rather than inferred. **Full text not
obtained**, so whether it states the equivalence remains open.

**And it is already in the note's own list of eight co-citers** — the paper cited as evidence
that "operations research and behavioural ecology are joined almost entirely by a third field"
is the same paper cited as evidence of direct contact. That tension is now stated in the note:
this one work is behavioural ecology proper, not neuroscience. No `00-index` edit was needed.

## [2026-09-05] correction | "46 citations was stale" was itself the error

[[stress-strength-interference]] had corrected [[G19-safety-factor-derived-twice]]'s "46
citations" for Alexander 1997 to "36/39/28, the 46 was stale." **Re-fetched today: OpenAlex
returns 46, OpenCitations 40, Crossref 36.** 46 is not stale — it is OpenAlex, and it is
current. A provider disagreement had been misread as a decayed number. Reversed the correction
in the theorem note, added the provider/endpoint/date table to both files, and made them agree.
`standing` untouched. **The "753 works" withdrawal stands** — that one really was a string
artifact (relaxed matching returns ~1.8M) — and G19 still asserted it; now withdrawn there too,
with no replacement offered, because a defensible figure needs an anchor set rather than a
phrase. The finding is unaffected either way: the intersection is a measured, inspected zero.

## [2026-09-05] provenance | two figures marked unreproducible rather than guessed

[[G6-multifunctionality]]: added provider, endpoint and date to the six-pairing intersection
table (OpenCitations set-overlap + Crossref reference-list scan, both directions, 2026-09-03),
and noted that the coverage column is a **ratio between two providers' counts**, not a retrieval
success rate. Two things are recorded as *not* recorded rather than reconstructed: the **six
anchor DOIs** were never logged, and the **9,570 homograph hits** have no provider, endpoint or
query behind them — marked "provider not recorded at time of run" and demoted to a scale
indicator. [[G17-overconfident-uncertainties]]: Bailey *Not Normal* corrected to **R. Soc. Open
Sci. 4:160600 (2017), `10.1098/rsos.160600`** (was "2016", no volume, no DOI; verified against
Crossref). The **279 → 6 screening is not recoverable** — four of six given by title only, no
DOIs, no criterion, no provider — so a "screening protocol not recorded" admission was added
instead of a fabricated enumeration.

## [2026-09-05] method | the OpenCitations trap has moved

`opencitations.net/index/coci/api/v1/` now **301-redirects to `api.opencitations.net/index/v1/`**,
and on the new host `/citation-count/` **no longer returns the bogus constant `1`** documented in
[[citation-sources]] — it agreed exactly with a counted `/citations/` list (Alexander 1997:
40 = 40). Recorded in G25's provenance block. The Crossref `?select=reference` → HTTP 400 trap
was not re-tested; full records were pulled as the method already prescribes.

## [2026-09-05] correction | C8 albatross L/D sourced at 21.2; Sigma_albatross 1.5e-2 -> 2.8e-2

A7. The wandering-albatross lift-to-drag ratio had stood at 20, marked UNVERIFIED. Sourced to
21.2 from Richardson (2015), *Prog. Oceanogr.* 130:146 ("the cruise airspeed, Vc = 16 m/s, of a
wandering albatross is its speed at the maximum glide ratio, which is around 21.2 in straight
flight (Pennycuick, 2008)"), fetched 2026-09-05. Tagged VERIFIED-SECONDARY: Richardson quotes
Pennycuick (2008), a book not obtained, and Sachs (2005) *Ibis* 147:1-10 is paywalled (Wiley
403, same date). Combined with the A6 factor of 2, Sigma_albatross = 68.14 W / 2396.5 W =
2.8e-2, from 1.5e-2.

## [2026-09-05] correction | C8 soaring availability was 2x too generous; Sigma <= 1 no longer reproduces the field's constant

A6. `P_available = m V^2 (dW/dz)` set climb rate and downwind speed both equal to the airspeed
V simultaneously, which the constraint `zdot^2 + vx^2 <= V^2` forbids; AM-GM gives
`zdot vx <= V^2/2`. With the half, `P_available = 2.40 kW` (was 4.8 kW) and eq. (3) becomes
`Sigma_soar = 2g/((L/D) V dW/dz)`, so `Sigma <= 1` reads `dW/dz >= 2g/((L/D) V)` - twice the
shear previously required. Consequence, and this is the part that matters: the note's claim
that Sigma <= 1 "reproduces the field's own criterion" survives only as a functional-form match.
The bound evaluates to 0.0597 s^-1, about 0.12 m/s of shear across the 2 m layer, against the
~3.6 m/s minimum wind Richardson (2015) derives - loose by ~30x. Restated as order-of-magnitude.
The previous exact-looking agreement at coefficient 1 was an artefact of the missing half.

## [2026-09-05] correction | C8 Sigma_drag has no 1/3 ceiling; "reproduces all four" -> three

A5. `Sigma_drag = FV/(F du) = V/du` is monotone in V with supremum 1 and no stationary point.
The 1/3 was imported from a different objective: `V = du/3` maximises extracted *power*
`P ∝ (du − V)^2 V`, the Cp = 4/27 drag-machine limit behind Betz. A power optimum is not a bound
on Sigma. Deleting it removes one of the four "known bounds Sigma recovers", and A6 demotes the
soaring case from exact to order-of-magnitude, so section 5 item 1 now claims three: two exact
special cases (tether load fraction, sail v/c), one order-of-magnitude recovery (soaring), and
one expression that is not a bound (drag).

## [2026-09-05] correction | C8 Sigma_sail is v/c, not 2v/c; IKAROS row and closed form now agree exactly

A4. The note's own definition `Sigma = P_useful/(F du)` with `du = c` gives `Fv/(Fc) = v/c`;
F cancels, so the 2 cannot be in Sigma. It belongs to the force: a perfect mirror gets
`F = 2 Phi A / c` from reflected-photon momentum reversal, and that 2 then divides out. The
populated IKAROS row compounded the error by using the incident flux `Phi A` = 2.67e5 W as the
denominator, which is not `F du` (for a mirror `Phi A = Fc/2`), giving 1.3e-4 against a closed
form of 2e-4 - a 60% mismatch the note called agreement. Denominator corrected to
`F c` = 3.36e5 W; Sigma = 33.6/3.36e5 = 1.00e-4 = v/c, exactly, by construction.

## [2026-09-05] verification | C11 NEAR declinations sourced; formula check re-runs to 13.28 vs 13.46

A3. `delta_i = -20.76 deg`, `delta_o = -71.96 deg` had been marked UNVERIFIED, "from memory".
Both are confirmed in Table 1 of Acedo, Piqueras & Morano (2019), MNRAS 489:3232 (open access),
attributed there to Anderson et al. (2008) and Jouannic et al. (2015), fetched 2026-09-05. The
memory was right. Recomputed: `cos(20.76) − cos(71.96) = 0.62539`, so
`dVinf = 6851 × 3.0993e-6 × 0.62539 = 13.28 mm/s` against the observed 13.46 - 1.3% low, and
within 0.1% of the source's own 13.295. Tagged VERIFIED-SECONDARY, not PRIMARY: the source
quotes the PRL, and PRL 100:091102 itself is paywalled with no arXiv preprint located.

## [2026-09-05] correction | C11 required charge was 3 C / 10 orders; it is 1.7 mC / 6.2 orders

A2. `Q_req = F_req/(V_p B) = 5.284e-4/(12739 × 2.43e-5) = 1.7e-3 C`, and against the assumed
floating charge of 1e-9 C that is 6.2 orders, not 10. The old figure was three orders too large
and, worse, contradicted the same section's own `A`: since both are linear in Q, `Q_req/Q_float`
is identically A. The three statements 1.7 mC, 6.2 orders and `A = 1.7e6` are now one number.
(The audit's intermediate 3.2 mC / 6.5 orders used the pre-Oberth `F_req = 1 mN`.)

## [2026-09-05] correction | C11 F_req omitted the Oberth factor; 1-9 mN -> 0.5-5 mN, every A down 1.86x

A1. The note computed the required force from `Delta p = m dVinf`, but `dVinf` is a change in
hyperbolic *excess* speed while the impulse is applied at perigee. Energy is the invariant that
connects them: `dE = m Vinf dVinf = m Vp Delta v_p` gives the Oberth conversion
`Delta v_p = (Vinf/Vp) dVinf = 0.5378 × 13.46 = 7.24 mm/s`, from the note's own
`dE = 6.73e4 J`. So `Delta p = 5.28` rather than 9.83 kg m/s, and
`F_req = 0.53 mN` (1e4 s) to `4.87 mN` (tau_peri = 1085 s). Headline specification 1-9 mN ->
0.5-5 mN. Every availability ratio falls by the same 1.86: `A` = 3e6 -> 1.7e6 (Lorentz),
300 -> 160 (thermal), 30 -> 18 (drag). **No verdict flips** - all three stay above 1 and RULED
OUT, and drag and thermal remain independently excluded on sign. Also removed two stray XML
tags left at the end of C11 by an earlier editing session.


## [2026-09-05] correction | C6: `Ha = 1` is not a collapse threshold — the two-state model is globally stable for every `Ha > 0`

**What was wrong.** [[C6-damage-healing-ratio]] §6 item 2 read the `Ha` axis as having a
break-even at `Ha = 1`: the 5 °C photosystem rows (`Ha = 0.907`, `0.831`) were described as
"already over the line" and as "a system running below break-even". That is a threshold claim,
and the note's own model has no threshold.

**What it is now.** `Ha = 1` is the point at which `A = 0.5` — half the population damaged at
steady state — and nothing more. Any collapse language is retracted.

**What produced the correction.** C6 §3.1, unchanged: `dp/dt = k_d(1−p) − k_r p` is linear in
`p` with coefficient `−(k_r + k_d) < 0`, so `p* = k_d/(k_r+k_d)` is the unique fixed point and
is globally stable for **every** positive rate pair. `A = Ha/(1+Ha)` is smooth and strictly
increasing on `(0, ∞)` with `A > 0` throughout — no bifurcation, no critical value. The
correction is derived from the note's own algebra; no new data was fetched.

**What a genuine threshold would require**, now stated in the note: an unbounded damage pool
(repair capacity saturating at `k_r^max`, so damage grows without bound once `k_d > k_r^max` —
a capacity limit, not a rate ratio), or an autocatalytic damage term
(`dp/dt = k_d(1−p) + c p(1−p) − k_r p`, which has a saddle-node at finite `c`). Neither is
supported by the PSII data in C6 §5.

**Numbers unchanged:** every row of the §5 table. This is a framing correction. (Backlog A8.)

---

## [2026-09-05] correction | C6: the `k_r/(k_r+k_d)` form *does* have a cross-domain name — it is the Erlang-B complement of an M/M/1/1 loss system

**What was wrong.** C6 §1 concluded "it has no cross-domain name", and §7 stated "No prior art
found". The §1 search covered Damköhler, healing-rate/damage-rate phrasings, and the algebraic
form as a *named group in damage/healing contexts*. **Queueing theory was never searched.**

**What it is now.** New C6 §1.1. In a loss system the offered load / traffic intensity is
`ρ = λ/μ`. The Erlang-B blocking formula `B(ρ,m) = (ρ^m/m!)/Σ_{i=0}^{m} ρ^i/i!` at `m = 1`
(the M/M/1/1 system: one server, no queue) reduces to `B = ρ/(1+ρ)`, hence
`1 − B = 1/(1+ρ)`. Mapping failures to arrivals (`λ = k_d`) and repair to holding time
(`1/μ = 1/k_r`) gives `ρ = k_d/k_r = 1/Ha` and `A = 1/(1+ρ) = Ha/(1+Ha)` — C6's equation (★)
exactly. So `Ha` is the reciprocal of the offered load and `A` is the Erlang-B blocking
complement.

**Provider and date.** Erlang-B formula and the offered-load definition from
`https://en.wikipedia.org/wiki/Erlang_(unit)`, fetched **2026-09-05**, which cites Kleinrock,
*Queueing Systems Vol. 1: Theory* (Wiley 1975) and Freeman, *Fundamentals of
Telecommunications* (Wiley 2005). Open-textbook pointer: Zukerman, *Introduction to Queueing
Theory and Stochastic Teletraffic Models*, `https://arxiv.org/abs/1307.2968` — **author and
title VERIFIED from the arXiv abstract page, fetched 2026-09-05; the Erlang-B chapter itself
was not fetched** (the arXiv PDF would not extract), so this is **VERIFIED-SECONDARY** under the
B16 grading. The `m = 1` reduction was done in the note, not quoted.

**What survives.** The claim is narrowed, not withdrawn. The *algebra* has at least three names
(offered load in teletraffic, MTBF/MTTR in reliability, unnamed steady-state ratios in
pharmacokinetics). What no source does is (a) apply the group to damage and repair, or (b) put
biological and engineered repairing systems on one such axis. [[G5-repair-number]] is
**narrowed, not filled**, and C6's novelty grade should read *repackaged/located*, not
*new object*. (Backlog A9.)

---

## [2026-09-05] vocabulary | C6: `Ha` collides with the Hartmann number — kept with a note, not renamed

`Ha` is the established symbol for the **Hartmann number** in magnetohydrodynamics
(`Ha = BL√(σ/μ)`, Lorentz vs viscous forces), and "Damköhler" conventionally denotes
reaction-vs-*transport* (`Da_I`, `Da_II`), not repair-vs-damage. C6 §3.2 defined
`Ha ≡ k_r/k_d` with no note of either.

**Decision: keep `Ha`, add an explicit collision callout in §3.2.** A rename is not local to
one file — `Ha` is load-bearing in [[C1-availability-living-tissue]], [[C10-healing-curve-fit]]
and [[G5-repair-number]] — so renaming inside C6 alone would trade one confusion for broken
cross-references. **`Da_h` is recorded as the recommended spelling for any external write-up**,
and the note now instructs writing the group out in full on first use outside the vault. No
number changed. (Backlog A10.)

---

## [2026-09-05] correction | C4: `N_ind` floored at 1 — single-statocyte band moves from 8°–17° to 7.6°–12.9°, and three framing claims in §1 are withdrawn

Four changes to [[C4-inclination-sensing-limit]], one of which moves numbers.

**1. The wedge gives `tan θ`, not `sin θ` (A11).** §1 derived `p(θ) = (w/4h₀)·tan θ` and then
wrote `≈ α sin θ`, concluding "This is the microscopic origin of the macroscopic sine law".
Withdrawn. `tan θ/sin θ = 1/cos θ = 1 + θ²/2 + …`, so the wedge reproduces a sine law **only to
first order**. The model is geometrically invalid above **θ = arctan(2h₀/w) = arctan(2×11/50)
= arctan 0.44 = 23.7°**, where the up-slope edge of the floor goes bare; the macroscopic sine
law is verified experimentally to 90°, so it is **not** derived in this note. Discrepancy vs a
true sine law: +1.5% at 10°, +6.4% at 20°, +9.2% at the 23.7° boundary. Nothing downstream
changes — every angle C4 computes is under 13°.

**2. The Boltzmann "cross-check" is not a second route (A12).** §1 claimed "Two independent
routes agree that the signal is ≈ N sin θ". Deleted. `p = tanh(55 sin θ)` gives 0.74 at 1°,
0.96 at 2°, 0.9999 at 5° — it saturates, and at 10° returns 1 against the geometric 0.19, a
factor of five. The two routes are also not independent: both use `mgd/k_BT_eff ≈ 20` and the
same `w`. What the calculation *does* show is retained and is worth keeping: since
`ΔE/k_BT_eff ≫ 1` at every angle of interest, **`T_eff` does not limit signal amplitude**.

**3. `N_ind = max(1, τ/τ_c)` (A13) — this is the number change.** The Berg–Purcell averaging
factor `√(τ/τ_c)` was applied with `τ = 70 s` against `τ_c = 60–120 s`, i.e. with
`τ/τ_c = 0.583` in the `τ_c = 120 s` rows: averaging *less than one* independent sample, which
is outside the regime where the formula is defined and inflates the noise unphysically. The
correct reading of `τ < τ_c` is one look at the pile, `N_ind = 1`. §5 regenerated with an
explicit `N_ind` column; **no row now has `N_ind < 1`**:

| `N` | `τ_c` (s) | `N_ind` | `sin δθ_min` | was | now |
|---|---|---|---|---|---|
| 20 | 62 | 1.129 | 0.21044 | 12.1° | **12.1°** (unchanged) |
| 20 | 120 | **1** (floored, from 0.583) | 0.22361 | 17.0° | **12.9°** |
| 50 | 62 | 1.129 | 0.13309 | 7.6° | **7.6°** (unchanged) |
| 50 | 120 | **1** (floored, from 0.583) | 0.14142 | 10.7° | **8.1°** |

Inputs: `sin δθ_min = (1/α√N)·(1/√N_ind)`, `α = 1`, `τ = 70 s` (Blancaflor 1998, VERIFIED),
`τ_c = 62 s` (Chauvet `τ_aval` 1.04 min) / `120 s` (Bérut `t_a ≈ 2 min`), `N = 20, 50`.

**Band: `8°–17°`, central 11° → `7.6°–12.9°`, central ~10°** (geometric mean
`√(7.6 × 12.9) = 9.9°`). Propagated: the pull-quote; §8's computed band; §8's pooling estimates
`11°/(3.34√M)` → `9.9°/(3.34√M)`, giving **0.86°** at `M = 12` (was 0.95°) and **0.54°** at
`M = 30` (was 0.6°); and §11.1's pooled figure **0.48° → 0.43°** (`9.9/(√48 × 3.34)`).

*Note on the backlog's target number.* `BACKLOG.md` A13 anticipated `7.6°–12.1°`. That band
results from **deleting** the `τ_c = 120 s` rows; this correction **floors** them instead,
because `τ_c = 120 s` is a VERIFIED measurement and the defect was in applying the averaging
formula to it, not in the input. Hence 12.9° rather than 12.1°. Both routes agree on ~10°
central and on removing the 17° tail. Recorded here because it is a deliberate departure from
the commissioning brief.

*Second-order caveat now in §8:* the pooling gain `√(τ_memory/τ) = √(780/70) = 3.34` is exact
only at `τ_c = 62 s`; at `τ_c = 120 s` the short window is floored and the long one is not, so
the gain is `√6.5 = 2.55`. The pooled figures are optimistic by up to 1.3×.

**4. §11.6's absolute column relabelled (A14).** §11.6 presented an "absolute `θ_min`" column
anchored on §11.1 while §11.8 recorded "Equal-weight pooling: **Falsified**" (2.1–2.8× spread
in `τ_p` at fixed `M`). The two sections contradicted each other. The column is now headed
**"equal-weight-pooling upper bound on θ_min (optimistic)"** with `≥` on every entry, because
unequal weights give `M_eff = (Σwᵢ)²/Σwᵢ² ≤ M` and true `θ_min` can therefore only be larger.
§11.8's row carries the same label. The **ratio columns are unchanged and are restated as the
load-bearing prediction: 1.73 (pooling) vs 3.00 (deterministic linear summation) at
`M = 16` vs `M = 48`.** Rescaled bound entries: 0.43 / 0.53 / 0.61 / 0.74° (pooling) and
0.43 / 0.64 / 0.86 / 1.29° (summation).

**Not done:** the optional recomputation of the absolute bound with an S2-weighted `M_eff`.
C4 §11.4 records that the weights are unidentifiable from four group means, so a weighted fit
would be unfalsifiable on this dataset.

---

## [2026-09-05] prior-art check | C4 pooling discriminator survives against distributed-detection theory, but the grade splits three ways

Backlog **E5** / `audits/05-scope-strategy.md` item 11. C4 §11.7 had searched only the plant
literature; this check searched the physics/engineering side. **Six distinct query
formulations**, WebSearch, all **2026-09-05**, tabulated verbatim with their returns in C4's new
`## Prior-art check 2026-09-05` section.

**Verdict: the `M^{−1/2}` vs `M^{−1}` discriminator does not already exist for plant
statocytes.** Nearest miss is McDonnell et al.'s **stochastic pooling networks**
([PRE 88:022118](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.88.022118),
[PRE 79:041107](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.79.041107)) — the right
object class, explicitly covering biological sensory neurons, but posed as capacity and
sensor-selection results, never as a two-model exponent discrimination and never on a
gravisensor.

**Weakness of the null, stated:** this is a *search* absence — English-language, web-index only.
No citation intersection of Berg–Purcell 1977 × Blancaflor 1998 was run. That is the obvious
hardening step and is the recommended follow-up.

---


## [2026-09-05] correction | C19's "≥15× window" was the tested dose range, not a window; removed from the toxicology comparison

The headline "model-free lower bound ≥ 15×" was the ratio of the highest to the lowest *tested*
coverage (1500%/100%) — an experimental-design artifact that would have read 10× or 100× under
different endpoints — and §5 scored it "meets or exceeds" toxicology's 10–20×. Renamed "tested
dose range, all beneficial: 15×" and struck from the comparison verdict, which now reads "no
comparison possible." Backlog A15.

## [2026-09-05] correction | C19's 73× fitted hormesis window withdrawn; admissible refit constrains no window at all

The log-quadratic fit implied `Nf` below baseline for coverage < 77%, i.e. that light peening is
harmful, contradicting `Nf → N₀` as coverage → 0. Refit on `Nf = N₀(1 + a·c·e^{−bc})` (inputs:
c = 100/400/1000/1500%, Nf = 28,300/96,522/90,336/82,120, N₀ = 19,113; least squares on the
excess ratio, numpy 2.4.3, 20,000-point grid on `b`) gives **a = 1.4707×10⁻², b = 1.29299×10⁻³,
SSE = 1.065, optimum 773% coverage, peak Nf = 99,089 (+418%)**. That form decays to baseline only
asymptotically, so **no finite zero-equivalent dose exists and the data constrain no window**;
only a one-sided descending-limb extrapolation survives (benefit falls to +10%/+5%/+1% at
c ≈ 5,120/5,750/7,160%, all 3.4–4.8× beyond the highest tested dose). The fit also misses the
100% point by +55%, so no window number is quotable until a 6–8 dose sweep exists. Backlog A16.

## [2026-09-05] correction | C19's two "strength ceilings" are two different axes and were wrongly pooled

AISI 4140's +18–25% is a **σ'_f-equivalent ESTIMATE** (Basquin coefficient inferred from a life
ratio under assumed `b ≈ −0.10`: R_N = 5.05 ⇒ 1.176; R_N = 8.97 ⇒ 1.245). AA 7075's +82% is a
**measured endurance limit** (275 → 500 MPa), a run-out asymptote outside Basquin's power-law
regime, and it is the **best of two doses**, not a fitted ceiling. The pooled range "+20% to +80%,
straddling biology's 30–60%" is withdrawn: the two are not on a common axis, and +82% *exceeds*
30–60%. Backlog A17.

## [2026-09-05] computed | C12's Smith normal form is now actually computed — diag(1,1,1) — and correspondingly demoted

§3.3 had asserted the SNF without computing one. Computed this session in Python (integer
arithmetic, standard SNF algorithm) on the 3×10 dimension matrix: **invariant factors (1, 1, 1),
rank 3**, verified by explicit multiplication `U·D·V = SNF(D)` with `det U = −1`. All-ones
invariant factors certify only that the kernel basis is integral. The load-bearing result — that
the Re = 1, Pe = 1 and Pe_th = 1 crossovers are parallel — follows from ν, D and α all having
dimension L²T⁻¹, readable off the note's own §1 table, with no kernel and no normal form
involved. The "lattice lock" framing is replaced by that plain statement, and the G22
constant-bound restatement is kept but relabelled a **definition**, not a derived criterion.
Backlog A18.

## [2026-09-05] correction | C16's 17-for-17 now quotes an interval, and the bias-immunity claim is deleted

Clopper–Pearson one-sided 95% upper bound on P(new physics | same class) with n = 17 closed and
k = 0: `1 − 0.05^(1/17) = 1 − exp(−2.99573/17) = 0.1616` → **0.16**. The data are consistent with
a same-class new-physics rate of one case in six. Deleted: "It remains bias-immune: adding
invisible same-class cases can only add more systematics" — findability of a documented
*resolution* correlates with the resolution being mundane, so the invisible population is not
guaranteed to be systematics. Backlog A19.

## [2026-09-05] method | C16's SAME-CLASS rule written as a decision procedure and re-applied blind: 11 of 24 rows change class

Procedure: inputs are **apparatus** (the principle whose systematic-error budget is shared),
**observable** (the quantity read out before model inversion), and **analysis pipeline**; output
is CLASS-I (all three match — the conditional is tested here), CLASS-II (apparatus and observable
match, pipeline differs), CLASS-III (apparatus or observable differs — not same-class). Standing
exclusion for known, computed corrections (the redshift-clock case) is folded into the procedure
rather than applied after the hunt. Blind re-application to all 24 rows plus the 3 excluded
candidates changed **11 of 24**: rows 4, 8, 19 → CLASS-III; rows 2, 3, 5, 6, 9, 14, 20, 24 →
CLASS-II. All three excluded candidates stay excluded. **Strict CLASS-I tally: 8 closed
(7 SYSTEMATICS + 1 FLUCTUATION), 5 open, 0 NEW-PHYSICS** — bound `1 − 0.05^(1/8) = 0.31`;
CLASS-I+II: 15 closed, bound `1 − 0.05^(1/15) = 0.18`. **No counterexample at any grade** — the
conditional survives — but on 8 strict cases, not 17. Limitation: same agent, same day,
blind-in-intent, not an independent replication. Backlog A20.

## [2026-09-05] method | New append-only, hash-stamped predictions register with real per-prediction dates

`vault/predictions.md` created (`type: method`). Records five blocks: the α / fine-structure
prediction (first made 2026-09-03, commit `a12703d`, per
`git log --format='%h %ad %s' --date=short -- vault/questions/Q7-same-class-prediction.md vault/method/fine-structure-discrepancy.md`),
the tenth-order QED coefficient prediction (same commit), C4's statocyte-pooling prediction
(1.73 under `M^{−1/2}` pooling vs 3.00 under `M^{−1}` linear summation), the 2026-09-05
pre-registration of CLASS-I/II/III for C16's 7 open and 4 ambiguous rows, and the 2026-09-05 full
24-row sweep that supersedes its numeric consequence. Each block carries a `sha256` of its
canonical text. Stated limitation: every commit in the repository's history is dated 2026-09-03,
so the register can establish "before 2026-09-05" and no finer from repository evidence alone —
which is precisely the defect it exists to stop recurring. Backlog A21 / C16.


## [2026-09-05] correction | C9: the section-3 Schur object is ZT_Schur, not ZT_eff; eq. (6) and eq. (8) reconciled by identity (8e)

A25. `ZT_eff` named two different quantities. §3 defined it on the Schur complement `L'` via
`q'² = ZT_eff/(1+ZT_eff)` and showed it *rises*; §4 defined it as `α²GT/(K+(1−ε)cv)` and showed
it *falls*. The §3 object is renamed **`ZT_Schur`** and eq. (6a) added:
`ZT_Schur = ZT/(1−φ)` with `φ ≡ L₂₃²/(L₂₂L₃₃) ∈ [0,1)`. New §4.1a writes all three as `α²GT`
over a conductance — `K`, `K' = K(1−φ)`, `K_tot = K+(1−ε)cv` — giving the identity
`ZT_eff = ZT_Schur·K'/K_tot`, equivalently
`1/ZT_eff − 1/ZT_Schur = [(1−ε)cv + φK]/(α²GT) ≥ 0`, hence `ZT_eff ≤ ZT ≤ ZT_Schur` (8f). The
Schur complement flattered the leg by exactly `φK` of thermal conductance; the physical
accounting charges that back and adds `(1−ε)cv`. **No number changed** — §5's `Pe = 3.97`,
`ZT_eff = 0.201`, `q' = 0.409`, the 3.8× fall, the 25 µm/s ceiling and the 0.025 J contact
penalty all come from eq. (8), untouched. Renaming plus an added identity; nothing fetched.

## [2026-09-05] correction | C2: "nine orders vs half an order" is 8.74 vs 0.51 at SF=3, V_R=0.20; at V_R=0.10 the load-CV sweep is 4.70 orders, not half

A24. The two sensitivities were evaluated at different, unstated operating points. Point now
stated: `SF = μ_R/μ_S = 3`, `V_R = 0.20`, `V_S ∈ [0.05, 0.30]`, normal–normal with `μ_S = 1`,
`μ_R = 3`, `σ_R = SF·V_R`, `σ_S = V_S`, `β = (μ_R−μ_S)/√(σ_R²+σ_S²)`, `P_f = Φ(−β)`. At that
point the strength-CV sweep `V_R` 0.10→0.30 gives 2.42e-11 → 1.33e-2 = **8.74 orders** (7.85 at
`V_S = 0.11`), and the load-CV sweep gives 4.47e-4 → 1.43e-3 = **0.51 orders**. Move only the
strength CV to `V_R = 0.10` and the same load-CV sweep gives 2.42e-11 → 1.21e-6 = **4.70
orders**. Cause is algebraic: `V_S` enters `β` only as `V_S²` added to `(SF·V_R)²`, which is
0.36 at `V_R = 0.20` and 0.09 at `V_R = 0.10`. A lognormal cross-check on the same grid gives
4.09 orders for the load-CV sweep at `V_R = 0.20`, so **the half-order figure is
normal-model-specific**, not a property of stress–strength interference. Full Python and both
6×3 tables pasted into a new §S. The note's existing illustrative pair (normal 5.2e-4,
lognormal 8.2e-7) is reproduced to 2 s.f. and its point identified as `V_S = 0.11`. Qualitative
claim — strength variability dominates load variability for bone — survives both models.
Recomputation only; nothing fetched.

## [2026-09-05] computed | C1: wind turbine fleet A = 0.9886 from lambda = 8.27/yr and MTTR = 12.06 h — first repairable *product* on the availability axis

E9. Carroll, McDonald & McMillan, *Wind Energy* 19(6):1107–1119 (2016),
DOI 10.1002/we.1887, author-accepted PDF fetched from Strathclyde repository 2026-09-05
(Wiley version 403'd). Population ~350 offshore turbines, 1,768 turbine-years. Table 2:
minor 6.81/yr × 6.67 h, major 1.17/yr × 17.64 h, replacement 0.29/yr × 116.19 h, total
λ = 8.27/yr and 99.76 h/yr of repair. `MTTR = 99.76/8.27 = 12.06 h`;
`MTBF = (8760−99.76)/8.27 = 1047 h`; `A = 1047/(1047+12.06) = 0.98861`. Two caveats recorded
against the row: it is a **unit** availability (same object as the grid row, *not* the same
object as PSII's population fraction), and it is an **upper bound**, because the source's
repair time is technician-on-turbine time and excludes travel, vessel waiting, spare-part lead
time and weather inaccessibility — which is why operators report ~0.97–0.98. Also noted: the
paper's Table 2 column head reads "Repair Time (Days)" while its Figure 13 plots the same
quantity in hours; read as hours.

## [2026-09-05] correction | C1 headline: "a leaf is less available than a power grid" struck — it compared a population fraction to a system availability

A23. The old headline read *"Photosystem II = 0.883. Cortical bone = 0.984. A leaf is less
available than a power grid."* Two defects. (1) The 0.984 has no supporting datum (see next
entry). (2) 0.883 is an expected *functional fraction* over ~10⁸ redundant photosystems, while
the grid figure is a *system availability probability*; the note's own caveat 1 said so and the
headline asserted the comparison anyway. New headline states PSII's steady-state functional
fraction with its two rate inputs and adds that with `N ≈ 10⁸` independent units the
probability that photosynthetic function is unavailable at the leaf is `(1−0.883)^N`, i.e.
**leaf-level function availability ≈ 1**. A new §1 tabulates the two columns — unit
availability vs population functional fraction — so no future row can cross them silently. The
35 °C row is retained as the counterexample: correlated damage defeats the redundancy and the
fraction falls to 0.562.

## [2026-09-05] correction | C1 rebuilt: every row now carries (k_d, k_r) or (MTBF, MTTR), the arithmetic and a fetched source; trabecular 0.939 -> band 0.726-0.952; cortical 0.984 UNSUPPORTED

A22. The note was a 35-line table of three headline numbers with no derivation, no rate inputs
and no sources, one of which contradicted [[C6-damage-healing-ratio]]. Row by row:

- **PSII** — `A = k_REC/(k_REC+k_PI)` from Bártolo, Frankenbach & Serôdio, *PLOS ONE* 18(9):
  e0292211 (2023), DOI 10.1371/journal.pone.0292211, full text fetched via Europe PMC
  PMC10538756, 2026-09-05. 20 °C community mean `k_PI = 2.695e-4 s⁻¹`, `k_REC = 20.235e-4 s⁻¹`
  → `A = 0.8825` — reproduces the old 0.883 exactly and reproduces C6 §5. Stress rows now given
  per community (35 °C: 0.706 / 0.562; 5 °C: 0.476 / 0.454) instead of as the ranges
  "0.56–0.71" and "0.45–0.48". Added the light-dependence caveat from Tyystjärvi & Aro, *PNAS*
  93:2213 (1996), DOI 10.1073/pnas.93.5.2213, PMCID PMC39937 (**abstract only**, fetched
  2026-09-05; the numeric proportionality constant was not obtained): `k_PI ∝ PPFD` over
  6.5–1500 µmol m⁻² s⁻¹, so every `A` is conditional on the assay light.
- **Trabecular bone 0.939 → band 0.726–0.952.** Replaced by C6 §5's two definition-dependent
  endpoints: revisit 730 d with the full 200 d remodelling cycle down gives
  `(730−200)/730 = 0.726`; with only the 35 d resorption phase down gives
  `(730−35)/730 = 0.952`. The 0.939 came by an unsourced "remodelling space" route. **The width
  0.23 is the finding**: bone is not two-state, so C6's condition C2 fails.
- **Cortical bone 0.984 → UNSUPPORTED.** C6 §5 marks cortical PARTIAL: the remodelling cycle
  median (120 d) is verified but the turnover/revisit interval was not found, so there is no
  denominator. Withdrawn until one is sourced.
- **US power grid 0.9998 → 0.99976 (excl. major event days) and 0.99874 (incl.).** EIA
  *Electric Power Annual* Table 11.1, <https://www.eia.gov/electricity/annual/html/epa_11_01.html>,
  fetched 2026-09-05: 2024 SAIDI 126.0 min / SAIFI 1.043 and SAIDI 662.6 min / SAIFI 1.531.
  `MTTR = SAIDI/SAIFI` = 2.01 h and 7.21 h; `MTBF = (525960 − SAIDI)/SAIFI` = 8,403 h and
  5,718 h. Consistent with C6 §5's grid rows.
- **Data centre "five nines" 0.99999 → UNSUPPORTED design target.** `1 − 0.99999` = 5.26 min/yr.
  Uptime Institute's own journal (Andy Lawrence, "99 Red Flags", 2019-10-28, fetched
  2026-09-05) says such figures are "market-driven", to be treated "with extreme caution", and
  that there is no direct relationship between a number of nines and a Tier level. Kept as a
  target, not as a datum, and no longer anchors the top of the axis.
- **Commercial aviation dispatch 0.995 → UNSUPPORTED and the wrong object.** No primary
  obtained (FAA ETEB summary PDF 403'd 2026-09-05); and dispatch reliability has a
  *per-departure* denominator with an MEL allowance, not a time denominator, so it is not
  `MTBF/(MTBF+MTTR)`.
- **Gut epithelium — dropped, not left blank.** A 3–5 day turnover is scheduled replacement
  before failure; there is no `k_d`, so no source was sought.

Net: no number in C1 now contradicts C6, and every surviving number states its inputs, its
arithmetic and a source with a URL and a fetch date. **Not obtained:** cortical bone
turnover/revisit interval; Tyystjärvi & Aro numeric constant; FAA dispatch figure; Wiley
version of Carroll et al.


## [2026-09-05] verification | E3 prior-art kill-check on C5: NOVEL holds; the two books are no longer the threat

The novelty audit rested C5's NOVEL grade on two unread books, "either of which could falsify
C5's novelty": Houston & McNamara (1999), *Models of Adaptive Behaviour*, and
Gittins–Glazebrook–Weber (2011), *Multi-armed Bandit Allocation Indices*. Both were pursued.
Neither full text was obtained — archive.org holds `modelsofadaptive0000hous` and
`foragingtheory0000step` under lending restriction (HTTP 403 on the text derivative; the
BookReader search-inside endpoint returns Bad Request), and Wiley's book page returns 403 —
but both were reached at **Google Books term-index level**, which is a frequency list over the
whole scanned text. Houston & McNamara: no "Gittins", "bandit", "index", "Charnov" or
"marginal value"; its high-frequency vocabulary is state-dependent dynamic programming, not
patch-use theory, so it was always a weaker threat than G28 assumed.
Gittins–Glazebrook–Weber: no "foraging", "Charnov", "animal" or "ecology". Stephens & Krebs
(1986), checked the same way as a third candidate, has *Charnov* and *marginal-value theorem*
and **no** "Gittins", "bandit" or "index" — the same asymmetry from the ecology side.
Verdict unchanged: **NOVEL**. What changed is the caveat's shape, from "two unobtained books"
to "three unread full texts", the third being Griebling et al. 2026.

## [2026-09-05] verification | The strongest prior art for C5 is an explicit denial, not a statement

Twelve web queries and five OpenAlex `fulltext.search` queries were run, and five full texts
were extracted and grepped. Nothing states that Charnov's `R*` is a Gittins index. The closest
anyone comes is **Kilpatrick, Davidson & El Hady**, *Normative theory of patch foraging
decisions* ([arXiv:2004.10671](https://arxiv.org/pdf/2004.10671)) — which C5 §8 had listed as
"abstract fetched only, provisional" and which is now **read in full**. It has a subsection
titled *Patch foraging as modified multi-armed bandit*, cites Banks & Sundaram's *Switching
costs and the Gittins index* (its one and only occurrence of the word "Gittins", in the
reference list), and concludes the opposite of C5: "as formulated these are still different
decision problems". It reaches "patch foraging is fairly well described by a non-stationary
bandit with … switching costs" and stops. Under the adversarial standard set for E3 — a bandit
treatment identifying patch residence with an index policy counts as prior art even without the
word "Charnov" — this is the nearest miss on record, and it is a denial. C5 §8's provisional
entry is discharged.

## [2026-09-05] verification | Two new near-misses located: Kacelnik 1979 and McNamara & Houston 1985

The Krebs–Kacelnik–Taylor 1978 lineage was checked at its source. **Kacelnik's 1979 Oxford DPhil
thesis** (ORA `uuid:8155d6b1-2df4-4e13-987d-a4d3b1ee3b68`, full PDF extracted, ~420 kB of text)
devotes three chapters to the two-armed bandit — Thompson 1933, Bellman, Jones 1975/1976,
Wahrenberger 1977, DeGroot — and solves it by **dynamic programming**, with **zero occurrences
of "Gittins" or "dynamic allocation"**. Bandits for *sampling*, never for patch residence.
**McNamara & Houston (1985)**, *Optimal foraging and learning*, *J. Theor. Biol.* 117:231, names
the two-armed bandit explicitly *and* MVT *and* MVT's circularity — `γ*` "can only be achieved
by behaving optimally" — in one paper, with **zero occurrences of "Gittins" or "index"**. Same
structure as Averbeck 2015: both halves in hand, no connection drawn. G28's "no direct contact"
topology is corroborated at two more points.

## [2026-09-05] verification | The OR side's silence measured: 240 "Gittins", zero "foraging"

Scully & Terenin (2025), *The Gittins Index: A Design Principle for Decision-Making Under
Uncertainty*, INFORMS TutORials ([arXiv:2506.10872](https://arxiv.org/pdf/2506.10872)),
extracted in full: 165 kB of text, **240 occurrences of "Gittins"**, **zero occurrences of
"foraging", "Charnov" or "marginal value"**. Jacko (2019)'s self-described *multidisciplinary*
two-armed-bandit survey ([arXiv:1906.10173](https://arxiv.org/pdf/1906.10173)) has **zero**
"foraging", "Charnov", "ecology" or "animal". The current state-of-the-art survey of the index
does not know foraging exists. This is the cleanest single measurement of G28's gap from the
operations-research side, and it is stronger evidence than the citation intersection.

## [2026-09-05] honest null | Zero ecological applications of the Whittle index found; E4's ground is empty

The query `"Whittle index" foraging patch regrowth restless bandit ecology` returned only
operations-research papers. No application of Whittle's restless-bandit index to a foraging,
patch-regrowth or ecological problem was located. This is a null with a use: it says backlog row
E4 (Whittle index for a regrowing patch) is unoccupied ground rather than a re-derivation, and
it is the reason C5 now carries a §12 "What E4 must do" spec instead of leaving the next agent
to re-litigate novelty.

## [2026-09-05] method | Novelty grades should record access level, not just "unobtained"

E3 exposed a vocabulary gap in the novelty audit. "Unobtained book" collapsed three different
epistemic states: never looked for, found but paywalled, and *found, full text blocked, but
term-index read and clean*. The last is much stronger than the first and the audit could not
say so. The C5 row now states the access level explicitly (Google Books term-index level, full
text 403) and names the residual threat by DOI rather than by category. Recommend the same
treatment wherever the audit's "biggest threat" column names an unread source — it pairs with
the VERIFIED-PRIMARY / VERIFIED-SECONDARY split proposed in `audits/01-math-physics.md` item 25.

## [2026-09-05] method | Citer-set intersection replaces reference-list intersection as the first pass

A citation intersection does not need reference lists. Pull the citer DOI set of anchor A, pull
the citer DOI set of anchor B, intersect. Coverage is then **100% of what the provider indexes**
instead of the publisher-deposit-limited fraction that capped G25 at 28.4%, and it costs two
requests instead of thousands. Written up in `citation-sources.md` with the script
`vault/_scripts/intersect.py` (stdlib only, caching, `--enrich` for hand inspection, `NULL_N=`
for the observed/expected null model).

## [2026-09-05] correction | G25's "zero coding-theory content" was a coverage artifact; standing live → narrowed

Re-ran Hopfield 1974 (`10.1073/pnas.71.10.4135`) × Shannon 1948 as a citer-set intersection.

- **OpenAlex**, `api.openalex.org/works?filter=cites:W2074616759,cites:W1995875735&mailto=…`,
  2026-09-05: Hopfield `cited_by_count` 1,656, Shannon pt I 82,198, **intersection 36** (32
  distinct works after preprint/published duplicates).
- **OpenCitations**, `api.opencitations.net/index/v1/citations/<doi>`, 2026-09-05: Hopfield 1,542,
  Shannon pt II (`10.1002/j.1538-7305.1948.tb00917.x`) 9,771, **intersection 8**; expected under
  independence at N=1.6×10⁸ is 0.09, so obs/exp ≈ 85.
- Hopfield × Shannon **pt II** on OpenAlex: 0.

Original run: 16 co-citers out of 416 reference lists (28.4% coverage), **0 with coding-theory
content**. The fraction barely moved (3.8% → 2.2%). **The zero did not survive.** All 44 hits
were inspected by title and abstract; at least four carry real coding theory, two decisively:

- `10.1016/j.tpb.2019.03.007` (*Theor. Pop. Biol.* 2019) — "used results from **coding theory** to
  prove bounds … including **proofreading**", genotypes built on **extended Hamming codes**.
- `10.3390/e20050368` (*Entropy* 2018) — *Writing, Proofreading and Editing in Information Theory*.
- `10.1109/memb.2006.1578663` — *The quest for error correction in biology*.
- `10.3390/e25060881` — error correction on an explicit memoryless channel model.

**Applied to the note:** `standing` `live` → **`narrowed`**, `contact-surface` 16 → **36**, tag
line and STANDING line updated, `note:` rewritten. `evidence: citation-intersection` unchanged
and now better supported. Narrowed rather than overturned: 2.2% co-citation with four bridges is
still well under the closed-gap signature in `positive-controls` (DNA data storage co-cites
error-correcting codes at 5.4% *and* reports results as a fraction of Shannon capacity).

## [2026-09-05] method | New endpoint trap: OpenCitations 500s on very large citer sets

`api.opencitations.net/index/v1/citations/10.1002/j.1538-7305.1948.tb01338.x` (Shannon 1948 part
I, ~82,000 citers) returns `HTTP 500 — something unexpected happened - SystemExit: 1 (line 1412)`
after 3 min 47 s. Part II (9,771 citers) returns 200 in 19 s. Above roughly 10,000 citers, use
OpenAlex's server-side `cites:A,cites:B` filter instead. **A 500 here is a size failure, not a
zero.** Recorded in `citation-sources.md`, alongside: the host moved to
`api.opencitations.net/index/v1/`, and `/citation-count/` no longer reproduces the bogus constant
`1` on the new host (control: Alexander 1997, 40 = 40) but is still to be cross-checked.

## [2026-09-05] correction | G21's three "Vogel" quotes are from a magazine feature, not either book

B8 asked for edition + page. There is no edition: all three quoted crossover passages come from
**Vogel, S., "Exposing Life's Limits with Dimensionless Numbers," *Physics Today* 51(11):22–27
(November 1998), `10.1063/1.882079`** — republished online 2026-01-27 as *Physics Today*
79(2):32–41, `10.1063/pt.b72840e67d`. Both DOIs confirmed via Crossref
`query.bibliographic` + `filter=container-title:Physics Today`, 2026-09-05; all three phrases
verified present in the online reprint, fetched 2026-09-05.

So the note's `evidence: full-text-read` rests on a **six-page magazine article**, not on *Life in
Moving Fluids* (2nd ed. 1994) or *Comparative Biomechanics*. The ABSENT check was re-run against
that article and **holds on its own terms**: it names Froude, Bond, Weber, Reynolds, the
Bernoulli–Hagen–Poiseuille ratio and Froude propulsion efficiency, **never Péclet**, and has no
figure placing organisms and processes on shared axes. The finding survives; the object it was
measured on was much smaller than the note implied, and no full-text ABSENT check against either
book has ever been run. No page number inside the article is claimed — the print PDF is
paywalled and the reprint has no folios.

Could not reach: `archive.org/…/comparativebiome00voge_djvu.txt` **HTTP 403** (lending
restriction); Google Books renders search-inside snippets client-side and returned none;
`googleapis.com/books/v1/volumes` **HTTP 429**. All 2026-09-05.

## [2026-09-05] verification | G21's Ortega Π values sourced, and one of them relocated

Πpe values were marked UNVERIFIED (ScienceDirect 403, Europe PMC 503). A different, open-access
Ortega paper answers the same question: **Ortega, J. K. E., "Dimensionless Numbers to Analyze
Expansive Growth Processes," *Plants* 8(1):17 (2019), `10.3390/plants8010017`, PMID 30634577,
PMCID PMC6359133**, fetched from
`www.ebi.ac.uk/europepmc/webservices/rest/PMC6359133/fullTextXML`, HTTP 200, 167,179 bytes,
2026-09-05.

- **Πpe = 32**, *P. satinis* L. stem — **Table 2**. Confirmed.
- **Πpe = 564**, *C. corallina* internode — **Table 2**. Confirmed.
- **Πpe = 1524**, *P. blakesleeanus* sporangiophore — **not in Table 2.** Table 2 gives
  1148 / 1791 / 1240 for the three measured stages. 1524 is a *single fitted constant across
  stages* quoted in the discussion. The vault implied it was one measurement. Corrected in place.

## [2026-09-05] verification | G8's overturn was reached with a bad instrument and is nonetheless correct

The 575 behind `"Landauer" AND (neuron OR synapse OR brain)` has **no host, endpoint or date and
does not reproduce**: OpenAlex `title_and_abstract.search` = 887, `fulltext.search` = 50,957,
Europe PMC = 1,031 (all 2026-09-05). **Left marked UNSOURCED** — new numbers do not source an
old one.

Re-tested as a citer-set intersection. **OpenCitations, `…/index/v1/citations/<doi>`, 2026-09-05:**
Landauer 1961 `10.1147/rd.53.0183` = 4,292 citers; Laughlin 1998 `10.1038/236` + Attwell 2001
`10.1097/00004647-200110000-00001` pooled = 3,881; **intersection 35**; expected under
independence at N=1.6×10⁸ = 0.10, **obs/exp ≈ 340**. All 35 inspected by title (Crossref,
2026-09-05) and they are the claimed connection itself — *Energetic costs of cellular
computation*, *The Cost of Sending a Bit*, *Capacity and energy cost of information in biological
and silicon photoreceptors*, and the "35 times more energy" paper the original overturn named.

**Proposed, not applied** (frontmatter left alone per this round's scope): keep
`standing: overturned`; `evidence` `string-protocol` → **`citation-intersection`**;
`contact-surface` 575 → **35**. Reason: the retraction should meet the same bar as an assertion,
and now it can.

## [2026-09-05] correction | G27 was overturned by a query that never tested the gap; propose overturned → narrowed

`"ant colony optimization" AND "honeybee"` is **swarm-internal** — ants against bees. G27 is about
**swarm intelligence against distributed-systems consensus**. The 26 (and the 551 under synonyms)
never touched that pairing. Both are UNSOURCED and neither reproduces (OpenAlex
title+abstract 32, fulltext 1,019; Europe PMC 38; all 2026-09-05).

Run on the pairing the gap names. **OpenCitations, `…/index/v1/citations/<doi>`, 2026-09-05:**

| A | B | N_A | N_B | ∩ | exp (N=1.6×10⁸) |
|---|---|---|---|---|---|
| Dorigo 1996 `10.1109/3477.484436` | Lamport 1998 `10.1145/279227.279229` | 8,814 | 1,914 | **0** | 0.11 |
| Seeley 1999 `10.1007/s002650050536` | Lamport 1998 | 267 | 1,914 | **0** | 0.003 |
| Dorigo 1996 | Byzantine `10.1145/357172.357176` + FLP `10.1145/3149.214121` | 8,814 | 6,735 | **1** | 0.37 |
| Seeley 1999 | same pooled | 267 | 6,735 | **1** | 0.01 |

Both hits inspected. `10.1201/9781420038880.bmatt` is a book's back-matter "References", a
cataloguing artifact. `10.1145/2168260.2168264` — *Host selection through collective decision*,
ACM TAAS 2012 — is a **genuine bridge**. **Honest contact surface: 1.**

**Proposed, not applied:** `standing` `overturned` → **`narrowed`**; `evidence` `string-protocol`
→ **`citation-intersection`**; `contact-surface` 26 → **1**. Reason: the zero that was retracted
was never measured, and when measured properly it is one bridge across ~8,800 swarm citers and
~6,700 consensus citers. Narrowed rather than live because that one bridge is real, and because
the surviving claim is the sharper one the note already named — **message complexity, cost per
unit communication**, formalised only on the distributed-systems side.

Two caveats kept in the note so the revert is not itself an overclaim: (1) a zero against an
expectation of 0.11 is weakly informative — the *low* numbers carry the evidence, not the zeros;
(2) Dorigo 1996 and Lamport 1998 are single-algorithm papers, the same trap the note originally
diagnosed, which is why the consensus side was broadened to Byzantine + FLP.

## [2026-09-05] verification | G7's TECDOC-626 citer trace completed: 57 citing works, all nuclear

The sub-claim recorded as "STILL-UNVERIFIED and formally closed as unanswerable" is answered.

**IAEA-TECDOC-626 has no DOI** — grey literature, invisible to Crossref, OpenCitations and
OpenAlex as a work. No citer-set intersection is possible on it, and that is a property of the
anchor, not a failed lookup. The route that works is full-text search over citing works:

| Provider | Endpoint | Date | N |
|---|---|---|---|
| OpenAlex | `works?filter=fulltext.search:"TECDOC-626"&per-page=100&mailto=…` | 2026-09-05 | **57** |
| OpenAlex | same with `"TECDOC 626"` (spacing control) | 2026-09-05 | **57**, identical set |
| Europe PMC | `…/rest/search?query="TECDOC-626"&format=json` | 2026-09-05 | **0** (calibrated zero — biomedicine-weighted, indexes no nuclear engineering) |
| OpenCitations | `…/citations/10.3327/jaesj.34.1116` (1992 *J. At. Energy Soc. Japan* note introducing TECDOC-626, the only DOI-bearing proxy) | 2026-09-05 | **1** |

All 57 classified by OpenAlex primary topic and venue: ~44 nuclear engineering / thermal-hydraulics
/ reactor physics / nuclear materials, ~8 reliability engineering applied to nuclear passive
systems, 3 nuclear licensing and policy, 2 technology ethics with nuclear energy as the case.
**Zero exoskeleton, structural-control, façade, robotics or control-theory works.** The 57 is a
lower bound (a work citing "IAEA (1991)" without the number is invisible), but a larger true
number would not change the classification unless the missing works are systematically
non-nuclear.

**Proposed standing change: none.** `narrowed` / `full-text-read` / contact-surface 2 all stand.
The trace hardens the note and retires open-work item 3 on `00-index.md` ("Trace citers of the
nuclear passivity ladder — rate-limited before completing"). TECDOC-626 itself still could not be
read (both IAEA PDFs HTTP 402), so the content of Categories A–D remains second-hand.

## [2026-09-05] method | New file: vault/_scripts/intersect.py

The one new script this round. Stdlib only, no key, caches raw JSON, usage documented at the top.
`python intersect.py <doiA> <doiB> [<doiB2> …] --cache=<dir> --enrich`, with `NULL_N=` for the
observed/expected null model. Pooling several DOIs into anchor B is how a multi-part work
(Shannon 1948) or a too-narrow anchor (Paxos alone) gets a fair test.


## [2026-09-05] method | Citation intersection gets a null model; two gaps turn out denominator-sensitive

`method/citation-intersection.md` gains "Expected co-citers under independence":
`E = |citers_A|·|citers_B| / N_universe`, with `N` defined per provider (OpenAlex concept/year
window; or the union of the two citer sets as a computable *floor*, which because it is the
smallest `N` gives the largest `E` and therefore flatters gap claims — labelled as such).

Worked. **G28:** Gittins 1,013 x Charnov 5,424, observed 5, union floor N = 6,432, E = 854,
O/E = **0.0059**; control Gittins x Auer 2002 (`10.1023/A:1013689704352`, Crossref
`is-referenced-by-count` = 3,906, 2026-09-05) 1,013 x 3,906, observed 225, N = 4,694, E = 843,
O/E = **0.267**. The **control ratio 62.5** is denominator-invariant and replaces the note's
"factor of 45", which divided both sides by the same 1,013 base without correcting for the two
partner sets' different sizes. Correcting it makes the isolation slightly *stronger*.

**G6:** 172 engineering x 861 ecology, observed 0, union floor N = 1,033 gives E = **143**. But
`E ∝ 1/N`: at N = 10⁵, E = 1.5; at N = 10⁶, E = 0.15. **A zero intersection is a finding only
where E > 1.** G6's zero therefore requires a fetched, concept-scoped `N` below ~1.5×10⁵ works,
and no such number has been fetched. This is a real weakening and is recorded as one.

**G25:** the Shannon-side citer count was never logged, so `E` is not computable. The null model
reduces to one query — is Shannon 1948 cited by more or less than 3.85% of the universe? — but
the load-bearing claim (0 of 416 inspected citers carry coding-theory content) is
denominator-free and unaffected.

`method/positive-controls.md` restated in the same units. **Five of the six original controls
turn out to be unstateable there** — Gompertz x Weibull, Weibull x reliability-theory-of-aging,
Levy-flight, Gittins x Sutton & Barto and DNA-storage x ECC all lack at least one citer-set size,
recorded as "inputs not recorded" rather than filled in. "The signal separates cleanly" now rests
on **one** fully specified control pair.

## [2026-09-05] method | Failure mode 6 added: diachronic terminology drift

`method/failure-modes.md` (now "Six ways a measured zero can be fake") and `METHOD.md` §11. The
first non-synchronic mode: modes 1-5 assume both names coexist, mode 6 is the case where they
never did — a citer window spans decades, a vocabulary does not. Required step: bin the window by
decade and re-run the concept under each decade's own name, taken from a review published *in*
that decade; a zero survives only if it is a zero in every bin.

Specimen: **kedem-caplan**, from this log's own 2026-09-03 correction. The 1965 degree-of-coupling
result was called unread on 2 co-citers between two named 1960s papers; the re-read found it in
active use (*Entropy* 25:1575, arXiv:2403.20209). It had travelled into thermoelectrics as the
figure of merit `ZT` and dropped the eponym. Chosen over the symmorphosis /
over-provisioning-accuracy case, which is a *cross-field* synonym with both names in use at once
— synchronic, and already covered by the "originating field's term" mechanism.

## [2026-09-05] method | A string count may no longer overturn a gap without host + query + date

`method/failure-modes.md`. The string protocol fails re-test more than half the time in both
directions, and an overturning is a withdrawal, so `relationship-description`'s symmetry rule
applies. Host, exact query string and date are now all three required before
`standing: overturned` on a string-protocol basis; absent any of them the count is an unverified
lead and must be re-tested under citation intersection.

Specimens are the project's own two: **G8** (575 on `"Landauer" AND (neuron OR synapse OR
brain)` — query recorded, host and date not, and a four-term disjunction is exactly the shape
failure mode 5 says relaxes) and **G27** (26 unmodified, 551 under synonyms — the 21-fold jump is
mode 5's signature, so the load-bearing figure is the 26, whose host and date are not recorded).
Neither standing is changed by this; both are flagged as resting on numbers no one can re-run.

## [2026-09-05] method | Reservoir-audit Part B renamed hard-positive; aperture sensitivity now mandatory

`method/reservoir-audit.md`. Part B was headed "negative controls on resolved anomalies" and is
not one — every row is a real anomaly with a real nonzero residual and a partner that turned out
to exist, i.e. a hard *positive* control. Renamed, with the distinction stated: a negative
control is an input with no residual, testing whether the instrument can return nothing. There
has never been one.

New mandatory Part C step 5: **state the assumed coupling cross-section and report `A` at 2x and
0.5x that aperture.** F3 conceded the aperture is a free parameter and instructed "prefer the
largest defensible one" — a preference, not a reproducible procedure. An exclusion that does not
survive the 2x row is now `NOT TESTED`, not `RULED OUT`. Procedure renumbered to 12 steps.

Part D added: **negative-control designs, not run** — (a) a Betz-calibrated wind turbine, with
the correct null output specified as "the reservoir considered supplies the required coupling; no
residual", and (b) a fabricated zero-consistent thrust report `F = (0.4 ± 3.0) µN at 50 W`, whose
correct output is a new fifth verdict state `NO OBSERVABLE TO EXPLAIN` reached before candidate
enumeration. D.2 predicts a missing step 0: *if the observable is consistent with zero, the audit
does not run.*

## [2026-09-05] correction | specification-instruments Q7 row: "bias-immune, 11/11" was wrong twice

`method/specification-instruments.md`. Replaced with C16's post-blind-rule numbers: strict
CLASS-I **N = 8** closed, 7 systematics + 1 fluctuation, **0 new physics**, Clopper–Pearson
one-sided 95% upper bound `1 − 0.05^(1/8)` = **0.31**; CLASS-I+II N = 15, bound **0.18**. The
"11" came from hand assignment; the blind rule changes 11 of 24 assignments.

Bias-immunity softened the same way C16 softened it: findability of a documented *resolution*
correlates with the resolution being mundane, so the invisible cases are not a random sample and
"adding invisible same-class cases can only add more systematics" fails. **0 of 8 is consistent
with a same-class new-physics rate as high as 31%.**

---

## Part 2 — proposed edits to notes owned by other agents

### 2a. `vault/computed/C11-flyby-reservoir-audit.md` — aperture retrofit (backlog C7)

Another agent owns C11. Proposed: append an **aperture** column and a sensitivity block to the
per-reservoir table in §2, satisfying the new `reservoir-audit` Part C step 5. All values below
are the current post-Oberth ones (`F_req = 5.28×10⁻⁴ N`); nothing is recomputed and no verdict
changes.

**Scaling assumed:** `A = F_req/F_max` and `F_max` is linear in the aperture for all three
reservoirs — Lorentz `F = QvB` with `Q = CV` and capacitance linear in effective radius; drag
`F = ½ρV²C_dA` linear in frontal area; thermal `F = P_rad/c` with radiated power linear in
radiating area. So `A(2x) = A/2` and `A(0.5x) = 2A`. **State this scaling in the note** — it is
the assumption that makes the sensitivity two lines instead of a re-derivation.

Proposed replacement rows:

| Reservoir | Assumed aperture (nominal) | `F_max` | **A (nominal)** | A (2x aperture) | A (0.5x aperture) | Verdict |
|---|---|---|---|---|---|---|
| Earth rotation via geomagnetic field (Lorentz) | spacecraft floating-charge capacitance `C ≈ 10⁻¹⁰ F` at `V ≈ 10 V`, i.e. a ~1 m effective conducting radius; **no deployed conductor** | `QV_pB ≈ 3.1×10⁻¹⁰ N` | **1.7×10⁶** | 8.5×10⁵ | 3.4×10⁶ | **RULED OUT** — survives 2x by six orders |
| Anisotropic thermal radiation | full spacecraft radiating envelope at `P_rad ≤ ~1 kW`, `η = 1` (fully collimated) | `P_rad/c ≈ 3.34×10⁻⁶ N` | **160** | 80 | 320 | **RULED OUT** — survives 2x by ~2 orders; also excluded on sign |
| Atmosphere / exosphere drag at 539 km | NEAR frontal area with `C_d` order unity, `ρ ≈ 10⁻¹³ kg/m³` | `≈ 3×10⁻⁵ N` | **18** | **9** | 36 | **RULED OUT** — survives 2x, but this is the row where the rule bites |

Proposed prose to accompany it:

> **The drag row is the one the aperture rule was written for.** `A = 18` nominal falls to
> **9** at twice the assumed frontal area — still an exclusion, but a one-order one resting on an
> exospheric density marked UNVERIFIED and solar-cycle dependent. Per F7 (`1 < A < 10` on
> unverified inputs is `NOT TESTED`, not `RULED OUT`), **the drag exclusion at 2x aperture sits
> exactly on that boundary and is carried by the sign argument, not by `A`.** The Lorentz and
> thermal exclusions are aperture-insensitive to any defensible factor: an aperture large enough
> to rescue the Lorentz coupling would need to be ~10⁶ times NEAR's, which is not a spacecraft.

### 2b. `vault/method/information-audit.md` — Part C negative-control design (backlog C6)

Not in this agent's file list. Proposed section, design only, mirroring `reservoir-audit` Part D:

> **## Part C — negative controls (design; NOT YET RUN)**
>
> The 3/3 validation is a positive-only control set, and it is not blind: all three cases
> (Bérut 2012, Toyabe 2010, Koski 2014) are textbook results whose entropy sink is stated in the
> source the audit quotes, and Bérut has only one sink available by construction, so it cannot
> discriminate. The audit has never been shown to return "no unnamed sink."
>
> **C.1 — A device whose entropy books already close.** Feed a system with a fully accounted
> entropy budget and no unnamed sink: a measured, near-quasistatic isothermal gas expansion, or a
> Carnot-cycle heat engine at published efficiency, where `ΔS_total` is accounted to within
> measurement uncertainty by the named reservoirs alone. **What counts as returning nothing:**
> the audit's sink enumeration terminates with the *already-named* sinks supplying the full
> balance, `ΔS_residual` reported as an interval containing zero, and **no new sink specified.**
> If it names an additional sink, the Toyabe result — where naming the demon's memory register as
> the unnamed sink is the audit's headline success — is an artefact of the procedure.
>
> **C.2 — A blind case.** Compute the sink for one case *before* reading the source's conclusion,
> and record the pre-registration in the note with a date and the source withheld until after.
> The three existing cases cannot be un-read, so this needs a fourth. **What counts as passing:**
> the pre-registered sink matches the published one, and the pre-registration is timestamped
> ahead of the read.
>
> **C.3 — An adversarial case.** A published claim whose sink attribution was **later corrected**.
> The audit passes if it reproduces the correction, not the original attribution.
>
> **Until C.1 and C.2 are run, "validated 3/3" should be read as *validated against positives
> only, non-blind*.**

### 2c. Per-gap `expected` lines (backlog C1)

The gap notes are owned elsewhere. Proposed one-line additions, to sit beside each note's
existing intersection figure. Each names its `N` route, because `O/E` is meaningless without it.

**`vault/gaps/G28-marginal-value-gittins.md`**, into the *citation intersection* section:

> **Expected under independence.** `E = |A|·|B|/N`. With `|citers(Gittins 1979)| = 1,013`
> (run-time, 2026-09-03) and `|citers(Charnov 1976)| = 5,424`, the union floor `N = 6,432` gives
> `E = 854` against `O = 5`, i.e. **O/E = 0.0059**. The Gittins × Auer control at the same
> construction gives `E = 843` against `O = 225`, **O/E = 0.267**. The **control ratio is 62.5**
> and is invariant under the choice of `N` — it supersedes the "factor of 45", which divided both
> numerator sets by the same 1,013 base and so ignored that Charnov's citer set is 39% larger than
> Auer's. `N_universe` has **not** been fetched; the union floor is a floor, and at `N = 10⁶` the
> raw `O/E` rises to 0.91. **Quote the control ratio, not the raw O/E.** See
> `method/citation-intersection.md`.

**`vault/gaps/G6-multifunctionality.md`**, into the intersection table's surroundings:

> **Expected under independence.** `E = 172 × 861 / N`. At the union floor `N = 1,033` (the note's
> own "1,033 works"), `E = 143` against `O = 0`. But `E ∝ 1/N`: `E = 1.5` at `N = 10⁵` and
> `E = 0.15` at `N = 10⁶`, where a zero is uninformative because fewer than one co-citer is
> expected anyway. **This zero is a finding only if the shared universe is smaller than
> ~1.5×10⁵ works, and that number has not been fetched.** The required query is an OpenAlex
> concept/year window over the union of the materials-multifunctionality and
> ecosystem-multifunctionality concepts from the earliest citer year. The positive control
> Byrnes 2014 × Jost 2006 = 17 **cannot be restated in these units: `|citers(Jost 2006)|` was not
> recorded.** See `method/citation-intersection.md`.

**`vault/gaps/G25-proofreading-coding.md`**, into the contact-surface section:

> **Expected under independence.** Not computable as recorded: `|citers(Shannon 1948)|` was never
> logged. The model reduces to `O/E = (16/416) / f_Shannon = 0.0385 / f_Shannon`, where
> `f_Shannon` is Shannon 1948's base rate in the universe — **one query**
> (`cited_by_count` for `10.1002/j.1538-7305.1948.tb01338.x` over the same concept/year window
> that defines `N`) settles whether this literature over- or under-cites Shannon. **The gap's
> load-bearing figure is denominator-free**: `O = 0` works with coding-theory content among the
> 416 inspected gives `O/E = 0` for any positive `E`. The binding limitation on this note remains
> **28.4% coverage**, not the null model. See `method/citation-intersection.md`.

---

## Part 3 — not done, and why

- **`positive-controls.md` five unstateable rows.** Recovering them needs the citer-set size for
  the second anchor of each pair, and those anchors' DOIs were not recorded at time of run. This
  is B13/B14 work, not C1 work.
- **`N_universe` never fetched for any gap.** Every `O/E` above uses a union floor, which is a
  floor and is labelled as one. Fetching concept-scoped denominators is the natural follow-on and
  would change G6's standing argument materially.
- **Parts D.1/D.2 and information-audit C.1–C.3 are designs.** Running them creates computed
  notes (backlog C5, C6), which this pass was scoped out of.


## [2026-09-05] computed | First Layer-3 derivation: Whittle index of a regrowing patch is W(x) = lam*x^2 - r*(1-x)^2

Backlog E4, per C5 section 12. Transferred the C5 Charnov-Gittins identity across the bridge
into the restless (regrowing-patch) case. Model: standing crop x in [0, G_max]; active
xdot = -lam*x with intake lam*x (reproduces Charnov's g(t) = G_max(1 - e^-lam*t)); passive
xdot = r(G_max - x); average-reward limit. Whittle relaxation with subsidy nu, single-arm HJB,
singular arc: W(x) = lam*x^2 - r*(1-x)^2, cross-checked by recovering V'(x) = 1 - x from it and
substituting back. INDEXABLE UNCONDITIONALLY (W' = 2*lam*x + 2r(1-x) > 0), so no condition to
check against Whittle 1988 / Nino-Mora 2001 / Glazebrook et al. 2006 (three DOIs verified,
Crossref, 2026-09-05).

Prediction: at fixed habitat quality, giving-up density RISES with regrowth rate,
dGUD/dr = (1-GUD)^2 / (2[lam*GUD + r(1-GUD)]) > 0. At r*tau = 0.2 (lam*tau = 1, GUD_MVT = 0.30):
GUD = 1.34x the MVT baseline, residence time 0.76x. Sign confirms the Q5 conjecture.

Both limit checks pass. r -> infinity: GUD -> G_max, t* -> 0 (degenerate skimming). r -> 0:
reproduces C5 eq. (4) g'(t*) = R* = max_t g(t)/(tau+t) EXACTLY, but only once
non-revisitability is re-imposed (V' = 0). The residual W(x) = lam*x^2 at r = 0 with revisits
allowed is not an error - it is C5 section 6 row 6 (Banks-Sundaram switching costs), now
quantified rather than merely named. That is an unasked-for second result.

Honest limits, stated in the note: (i) W is monotone in x, so in a HOMOGENEOUS habitat the
priority rule degenerates to "visit the fullest patch" and carries no r-signal - the prediction
is necessarily a between-patch-type contrast; (ii) tau sits outside the Whittle relaxation and
is re-inserted only at renewal-cycle level, so the r*tau axis is a reporting convention, not a
derived scaling - the largest hole; (iii) no optimality gap is stated, because one forager
among N patches is not the Weber-Weiss asymptotic regime.

Dataset named: Kadmon & Shmida 1992 Evol. Ecol. 6:142-151 (10.1007/BF02270708, departure rules)
paired with Kadmon 1992 Oecologia 92:552-555 (10.1007/BF00317848, measured nectar renewal in
the same Anchusa strigosa / Anthophora system). Both verified via Crossref 2026-09-05. The pair
parameterises the test but does not run it: departures are not stratified by renewal rate. Note
against interest: Kadmon 1992 measured LINEAR renewal, not the saturating form assumed here.

Files: new vault/computed/C25-whittle-foraging.md, new vault/_scripts/c25_whittle.py, pointer
section appended to vault/questions/Q5-restless-patches.md. Lint 0 errors.


## [2026-09-05] correction | Ledger totals were wrong in two places at once; recounted row-by-row to 12/8+1/3/1 = 25

B12. The disclosure ledger carried **two disagreeing tier counts**: the header said "13 DOCUMENTED
+ 1 hybrid, 7 TESTIMONIAL, 3 ATTRIBUTED/REFUTED — 24 entries" and the Findings summary said
"12 DOCUMENTED, 7 TESTIMONIAL, 3 ATTRIBUTED/REFUTED (22 entries)". Neither matched the table.
Recounted from the rows themselves: DOCUMENTED = 1,2,3,4,5,6,10,11,14,21,22,23 (**12**);
TESTIMONIAL = 7,8,9,16,17,18,19,20 (**8**); ATTRIBUTED/REFUTED = 12,13,15 (**3**);
SECONDARY-sourced = 24 (**1**); plus new row 25, TESTIMONIAL-anonymous (**1**) = **25 entries**.
The header's error was in TESTIMONIAL (7 for 8) and in double-counting row 24 as DOCUMENTED *and*
hybrid; the summary's error was both TESTIMONIAL and a total that predated rows 23–24. One
consistent set now, stated once in the header and once, cross-referenced, in the summary. Nothing
was fetched to produce these numbers — they are a recount of text already in the note.

## [2026-09-05] correction | Ledger row 24 (Apollo/PURSUE) downgraded DOCUMENTED -> SECONDARY-sourced: we never held the primary

B12. Adding the per-row `Fetched` column made an existing overreach visible. Row 24 asserted "the
transcripts are authentic primary records — a genuine upgrade from lore to primary source," but
**no Apollo debriefing transcript was ever fetched**: the PURSUE portal `https://www.war.gov/ufo/`
returned **HTTP 403** to both `curl` and WebFetch on 2026-09-03, and the only primary-adjacent
extract in the vault is explicitly labelled SECONDARY. Worse, the one *fetched* secondary (TIME,
2026-05-11) foregrounds **Gemini 7** (Borman/Lovell, 1965) with its "particles" reported as
**explained as booster debris** — a mundane attribution, not an Apollo-lunar account. The Apollo
framing came from unfetched outlets. Row 24 is now **SECONDARY-sourced (documented) / OPEN
(referent)**, restorable to DOCUMENTED on a fetched primary. This is the ledger's own rule —
VERIFIED means a fetched URL — applied to the ledger.

## [2026-09-05] method | Ledger gains a per-row `Fetched` column; every row's provenance now carries a date

B12. All 24 pre-existing rows read **2026-09-03** (the single session in which the ledger was built
and its URLs fetched — `log.md`, "[2026-09-03] disclosure thread" / "[2026-09-03] corpus mined");
row 25 reads 2026-09-05. **No row needed "date not recorded."** Three things the single date hides
are now stated under the table: row 4's AARO founding memo was never fetched, rows 5 and 23 rest
on secondary reporting only, and the AARO FY24 PDF was unfetchable on every route in that session
so rows 12–15 have no `sources/` extract. The column's value showed up immediately — it is what
exposed row 24.

## [2026-09-05] ingested | New witness is anonymous: the "4chan UFO whistleblower," archived as ledger row 25 at the tier floor

E17. The owner flagged YouTube `HM3oUMvvTe8`. Fetched: oembed **HTTP 200** (title "The 4chan UFO
Whistleblower", channel *Lately*); watch page **HTTP 200**, 1,265,145 bytes, giving upload
**2026-08-31**, 2,320 s, 394,102 views. `yt-dlp` is **not installed**; `youtube_transcript_api`
**is**, so nothing was installed — the **auto-generated** `en` caption track (1,146 segments, no
manual English track) was pulled and archived verbatim, bucketed at ~60 s, as
`vault/sources/src-4chan-ufo-whistleblower-video-2026-09-05.md`, with its ASR errors left uncorrected.

**The primary was NOT obtained.** The claim originates in anonymous 4chan `/x/` threads, and
`archive.4plebs.org` (thread and search and API), `desuarchive.org` all returned **HTTP 403**; the
Adobe PDF of the thread linked in the video's own description resolves only to a JPEG page image
with no extractable text. Two concordant secondary pages (reveil.blog, smbtech.au, both fetched
2026-09-05) identify the primary as `/x/` **No. 34629564** (2023-04-24) and **No. 34704869**
(2023-05-04) — VERIFIED-SECONDARY, not primary-verified.

Filed **TESTIMONIAL-anonymous**, a new tier floor: the claimant is unidentifiable *in principle*,
so access basis is not merely hearsay but unverifiable, and even "firsthand" cannot be graded.
Per [[specification-instruments]] only the **specification** was extracted — materials, dimensions,
behaviours, dates, places, named programs, in a new §2a table — and no mechanism was assessed.
Recorded discrepancy: the owner's flag described a *reconstruction worker*; the source describes
**crash retrieval** ("team two" of four) and places reverse-engineering with contractors. Also
recorded: nearly every specification line has a public antecedent (Lazar's element 115, Majestic-12,
the Wilson memo), so the account's detail is not independent of the corpus it sits in — equally
consistent with a well-read hoax and with an insider account, and the ledger takes no position.

## [2026-09-05] counted | "A growing narrative" is now countable: 11 witnesses, 0 non-US, 0 firsthand-with-primary on the extraordinary claims

E17. New disclosure-ledger §5, "Cross-witness meta-narrative table," built from every ledger row
plus row 25, with the counting rule stated first: one witness = one natural person in their own
voice (institutions are not witnesses); one row can carry two witnesses (row 24: Aldrin, Schmitt);
claim class = [[testimony-taxonomy]] facet 3, counted as occupied cells.

**The count: 25 ledger rows, 26 table rows, 11 distinct witnesses** — 10 named, 1 anonymous —
**15 rows institutional.** What the count shows: **every witness is American and US-program-
adjacent, so the corpus contains no cross-national independence at all**; and while all six claim
classes are occupied, the two extraordinary ones (materials/craft retrieval, biologics) are held
by 3 witnesses of whom **zero** are firsthand-with-primary — one sworn secondhand (Grusch), one
bare assertion (Nell), one anonymous (row 25). Row 25 grew the witness count by one and the
evidence by nothing: no new class, no new country, no primary. The narrative grows faster than the
evidence, which is what the selection filter (§3) predicts and is *not*, by itself, an argument
that it is false. This converts the E2-vs-E17 conflict the owner left open — freeze the ledger, or
keep ingesting — into the third option: keep ingesting, but only into a counted structure.

## [2026-09-05] method | Exit condition named for an institutional null, so "contested referee" cannot become an unfalsifiable veto

C14. [[evidence-lanes]] gains "Exit condition for an institutional null." Downgrading a contested
referee's null to evidence is only honest if it is reversible; otherwise it is dismissal wearing
skepticism's coat. Stated condition: a null becomes a **verdict** when a second body reruns the
check on a **different access basis** and four things hold — (1) no institutional stake (not a
subject, not the funder/supervisor, not the proponent); (2) access **independently verified**, not
asserted, so the result is demonstrably absence-of-thing rather than absence-of-access; (3) the
same specified observable, not a reformulated one; (4) the same null returned. Two convergent
nulls from orthogonal access bases are the null-side form of the orthogonal-lane rule. Applied to
AARO in disclosure-ledger §4 in one sentence; short of it, Version B stays *uncorroborated*, and
[[Q1-what-gets-checked]] says the second check is unfunded/classification-gated rather than tried
and failed.

## [2026-09-05] method | Staged R3C edits landed in the three notes their author did not own

`computed/C11-flyby-reservoir-audit.md` §2.0 gains the aperture-sensitivity retrofit required by
`reservoir-audit` Part C step 5: the assumed cross-section is now stated per reservoir, `A` is
reported at 2x and 0.5x aperture under the stated linear-`F_max` scaling, and **no verdict
changes** — Lorentz 1.7x10^6 -> 8.5x10^5, thermal 160 -> 80, drag 18 -> **9**. The drag row is
the one the rule was written for: at 2x aperture it sits exactly on the F7 `1 < A < 10`
`NOT TESTED` boundary and is carried by the sign argument, not by `A`.

`method/information-audit.md` gains **Part C — negative controls (design; NOT RUN)**, mirroring
`reservoir-audit` Part D: C.1 a device whose entropy books already close, C.2 a blind
pre-registered case, C.3 an adversarial case with a later-corrected sink attribution. Until C.1
and C.2 run, "validated 3/3" reads as *validated against positives only, non-blind*.

## [2026-09-05] correction | G28's "factor of 45" is wrong; the control ratio is 62.5

`gaps/G28-marginal-value-gittins.md` body and frontmatter `note`. The 45 divides both numerator
sets by the same 1,013 Gittins base, cancelling the base but not the difference in *partner* set
size — Charnov's citer set (5,424) is 39% larger than Auer's (3,906). The denominator-invariant
statistic per `method/citation-intersection.md` is `(225/3,906)/(5/5,424) = 62.5`. Correcting
45 -> 62.5 makes the isolation slightly **stronger**. Quote the control ratio, never the raw O/E.

## [2026-09-05] computed | N_universe fetched for three gaps; G6's weakening is retracted, G25's concept scope is void

OpenAlex `works?filter=...&per-page=1`, all fetched 2026-09-05, `meta.count`:

- **G28** — `concepts.id:C165287380|C9343608|C123197309|C99414536,from_publication_date:1976-01-01,to_publication_date:2026-09-05` -> **100,685**. `E = 54.6`, `O/E = 0.092`. `E > 1`, so the low count **is** a finding; at 10x `N`, `O/E = 0.92` and it is not. Control at the same `N`: `O/E = 5.73`.
- **G6** — `concepts.id:C200329591|C2988890453,from_publication_date:2011-01-01,to_publication_date:2026-09-05` -> **13,830**. `E = 10.7`, `O = 0`. R3C recorded G6's zero as a real weakening pending a fetched `N` below ~1.5x10^5 works. The fetched universe is an order of magnitude under that. **The zero survives and the weakening is retracted.** Scope caveat: OpenAlex has no "multifunctional materials", "structural battery", "ecosystem multifunctionality" or "Hill numbers" concept, so Advanced composite materials x Functional diversity are proxies. At 10x `N`, `E = 1.07` — marginal.
- **G25** — `concepts.id:C170748874|C113709454,from_publication_date:1974-01-01,to_publication_date:2026-09-05` -> **8,851**, which is **void as a universe**: `|citers(Shannon 1948 pt I, W1995875735)| = 82,198` (OpenAlex `cited_by_count`, 2026-09-05) is larger than it. Shannon's citer set does not fit inside any nameable concept scope. The union floor `N = 83,818` binds: `E = 1,624`, `O/E = 0.022`, and at 10x floor `O/E = 0.222`. `E >> 1` on every valid row, so the low count is a finding and, unusually, `N`-insensitive across an order of magnitude. This also settles the note's open "one query": `f_Shannon = 0.98` at the floor, far above 3.85% — the proofreading literature **under**-cites Shannon.

`method/positive-controls.md` restated with the fetched denominators; its G6 row's
"`E < 1` above `N ~ 1.5x10^5`" caveat is retired.

---


## [2026-09-05] correction | G28 carried two co-citer counts (8 and 5) from two runs without saying so

The 8 is the 2026-09-03 OpenAlex-base run (1,542 citers), the 5 is the OpenCitations/Crossref reference-list run (1,013). Both now labelled in the note. Surfaced by drafting the preprint (`papers/charnov-gittins/`). Also: Q5 gave a revisitability mechanism for the regrowth sign; C25 derives it from forgone regrowth. Q5 now says which is derived.

## [2026-09-05] computed | C30: Venus phosphine audited — step-0 halt, and every abiotic route excluded by A = 10^2 to 10^15 conditional on the detection

Ran [[reservoir-audit]] Part C on the Greaves et al. 2020 phosphine claim
(`10.1038/s41550-020-1174-4`). **Step 0 returns `NO AGREED OBSERVABLE`**: the 266.94 GHz
feature is ~2σ on re-reduction (Snellen 2020, `10.1051/0004-6361/202039717`), bootstrap-
insignificant (Thompson 2020, `10.1093/mnrasl/slaa187`), SO₂-degenerate (Villanueva 2021,
`10.1038/s41550-021-01422-z`), and `<0.8 ppb` above 75 km from SOFIA (Cordiner 2022,
`10.1029/2022GL101055`) — while the claim itself moved from 20 ppb to ~1–7 ppb on
recalibration, and Greaves et al. 2023 (`10.1029/2023GL103539`) extract `~3 ppb at 5.7σ` from
Cordiner's *own* SOFIA data. Same photons, opposite verdicts: METHOD §5 systematics.

Run conditionally, `S_req = 1×10⁸ molecules cm⁻² s⁻¹ = 26 kg/s = 2.41×10¹⁰ mol/yr` (Bains
et al. 2021, `10.1089/ast.2020.2352`, full PDF read 2026-09-05). Availability ratios computed
this session: volcanic **8.0×10³** (and 7.0×10³ by an independent P-outgassing route),
lightning **1.4×10⁵**, meteoritic **8.0×10⁴**, photochemistry **≥10⁵**, surface/subsurface
**10⁸–10¹⁵**, tribochemical **≥10²**. Arithmetic in `_scripts/c30_phosphine.py`.

## [2026-09-05] method | Bains-calibration: the audit reproduces a published enumeration route-for-route, and declines one exclusion Bains asserts

The exclusion list matches Bains et al. 2021's on every row Bains bounds. **One substantive
divergence, and it runs conservative:** at Bains' *own* extremal aperture (`τ` inflated 10³×,
their supplementary transport-only bound of `1.3×10⁵ cm⁻² s⁻¹`) the volcanic row falls to
`A = 8.0`, which under [[reservoir-audit]] F7 is `NOT TESTED`, not `RULED OUT`. Bains reject
that scenario on physical grounds (transport assumptions *"not physically plausible, or even
self-consistent"*) — a mechanism argument the ledger is not entitled to make. Two further
divergences are wording: F2 ("of the routes considered" vs the title's "cannot be explained"),
and scoring the biotic row as a ledger state rather than as prose.

## [2026-09-05] honest null | the biotic row SURVIVES the same ledger that excludes every abiotic route — and that is a fact about the ledger

Bains 2021's own thermodynamics puts the reducing power needed to make PH₃ from phosphate
inside the range of terrestrial biochemicals (NADH and two Fe–S proteins suffice); Lingam &
Loeb 2020 (arXiv:2009.07835) put the required biomass orders of magnitude *below* Earth's
aerial biosphere. So `A ≤ 1` on both legs and the biotic route is not excluded. Per
[[reservoir-audit]] F4, `A ≤ 1` is necessary and never sufficient — the ledger is blind to
water activity, to concentrated H₂SO₄, and to membrane integrity, which is where Bains locate
the real obstacles. Recorded as *specified, not endorsed*, exactly as C11's dark-matter row.

## [2026-09-05] method | first Part-D negative-control datum: the instrument was TOLD to halt, and D.2 needs a new failure class

The step-0 halt was pre-announced in `audits/scout-03-astrobiology.md` and in the
commissioning instruction, so it was executed, not discovered. **Part D's question — can this
audit produce a null unprompted? — is still unanswered.** What the run does establish: the
step-0 state is reachable and well-defined on a real input, and Venus exhibits a failure class
D.2 did not anticipate — not "a central value inside its own error bar" but **"a central value
that is a function of the reduction pipeline."** A genuine blind control still needs the K2-18b
run, with the halt not pre-announced.

## [2026-09-05] computed | the 266.94 GHz observable is degenerate in principle, not in practice

Computed this session: PH₃ `1–0` at 266.9445 GHz and SO₂ `J=30(9,21)–31(8,24)` at
266.943329 GHz are separated by **1.17 MHz = 1.32 km/s**, comparable to the several-km/s line
widths reported. More 266.94 GHz spectroscopy therefore cannot settle the case at the
resolutions flown, however long it integrates. The discriminating observables are the vertical
profile, the P-bearing companion inventory (P₂H₄, P₄, PO), and in-situ mass spectrometry on a
descent probe through 50–60 km. Isotopes are unavailable: ³¹P has no stable partner.


## [2026-09-05] computed | C26: the EWS-to-hazard discriminator fails its own controls, and C18's beta axis is estimator-dependent

Opened as the missing object of G29: convert a published ecological early-warning series into a
prognostics-style remaining-useful-life distribution and read off its Weibull shape `β`. Built
with `vault/_scripts/c26_ews.py` (stdlib + numpy) on the Cariaco Basin Younger-Dryas → Preboreal
greyscale record (2,111 points; the `YD2PB_grayscale` series shipped with the `earlywarnings` R
package, behind Dakos *et al.* 2008 PNAS, `10.1073/pnas.0802430105`) and NASA C-MAPSS
`train_FD001`/`train_FD004`, all fetched 2026-09-05.

**Result: negative, and reported as one.** Cariaco gives `β = 5.84`, 95% CI [1.98, 10.63] — but a
*stationary AR(1) surrogate with no bifurcation at all* gives `β = 7.39` (one-sided surrogate
`p = 0.66`), and the same record with the transition removed gives `β = 4.97`. The
drift-to-noise statistic fails too (`p = 0.35`). The fitted first-passage mean over-predicts the
observed time-to-transition by about **8×** (3,861 yr against 491 yr of remaining record). So
the scout's proposed `β > 1` bifurcation / `β ≈ 1` noise-induced discriminator is **not
measurable from a single ecological series**.

**Correction to `C18-durability-axis`, not a refutation of it.** On the *same* 100 C-MAPSS
units, the ensemble-lifetime Weibull MLE gives `β = 4.41` [3.90, 5.30] and the
degradation-to-first-passage route gives `β = 0.97` [0.78, 1.20] — a factor of 4.5 from the
estimator alone. **C18's `β` axis is well-defined only once the estimator is named.** C18's own
worked cases are all of the first kind and stay internally consistent.

What could not be fetched, and is left as an empty row rather than an estimate: the Carpenter
*et al.* 2011 *Science* (`10.1126/science.1203672`) Peter Lake chlorophyll series (no reachable
machine-readable archive; **no number from that paper appears in C26, not even from its
figures**) and the IMS bearing run-to-failure set (~6 GB of raw vibration, out of budget).

## [2026-09-05] gap | G29 opened live: ecology's early-warning signals and industrial prognostics compute the same first-passage law and do not meet — nine zeros under decade-appropriate anchors

Opened from `audits/scout-02-resilience.md` candidate #1, whose OpenAlex provenance is carried
verbatim: Scheffer 2009 (`10.1038/nature08227`) × Si 2011 (`10.1016/j.ejor.2010.11.018`),
`N_A = 4,891`, `N_B = 2,098`, `O = 2`, `N_universe = 15,304`, `E = 670`, `O/E = 0.0030`; control
Scheffer × Wissel 1984 (`10.1007/bf00384470`) `O = 321`, `O/E = 1.26`; control ratio 0.0013.

**Re-run on a second provider, because OpenAlex refused.** `api.openalex.org/works?filter=cites:`
returned HTTP 429 for this whole session (~90 attempts, backoff to 20 s, ~40 minutes; single-work
`works/<id>` fetches succeeded throughout). The re-run therefore used **OpenCitations**
(`api.opencitations.net/index/v1/citations/<doi>`, citer DOI sets intersected, 2026-09-05):
`N_A = 3,934`, `N_B = 1,783`, **`O = 1`**, `E = 458`, `O/E = 0.0022`; control Scheffer × Wissel
`O = 268`, `O/E = 2.89`; **control ratio 7.6 × 10⁻⁴**, same order as the scout's on a different
instrument. The finding survives the union floor (`E = 1,227`) and 10× the concept scope
(`E = 45.8`).

**A cleaning trap worth recording.** OpenCitations returns citation records with an **empty
`citing` DOI**. Deduplicated as a set, one blank key manufactures a false intersection in *every*
pairing; dropping blanks moves Scheffer × Randall & Antoni from 1 to **0** and every other row
down by one. Any future citer-set intersection on this provider must drop blank DOIs first.

**`failure-modes` mode 6 was run and the zero survives it.** Year bins 2009–2013 / 2014–2018 /
2019–2026 give `O = 0 / 0 / 1` against a control that is joined in every bin at a stable
`O/N_B ≈ 0.73–0.82`. Under decade-appropriate anchors on *both* sides — Scheffer 2001, Dakos
2008, Wissel 1984 against Si 2011, Jardine 2006, Randall & Antoni 2011 — the 3 × 3 matrix is
**nine zeros**. The object did not travel under an earlier name.

**All three co-citers inspected to a verdict**, and the scout's "two papers wide" is now
"three, and thinner than that": `10.1007/s42524-021-0176-y` (*Frontiers of Engineering
Management* 2021) bridges the two *terminologies* and transfers no formalism;
`10.3390/s23020965` (*Sensors* 2023) is engineering reading ecology — the wrong direction;
`10.2139/ssrn.7266197` (2026) is an **SSRN preprint**, which the scout did not note.

**Standing: live**, `contact-surface: 3`, `crosses: vocabulary`, `topology: direct`.
[[C26-ews-hazard-shape]] closes the computation the gap named and returns a negative, which
sharpens the gap rather than narrowing it: the literatures do not meet, and the reason may be
good — the transfer ecology needs from prognostics is not the hazard model but the *fleet*.


## [2026-09-05] gap | G30 opened — the Weibull shape parameter β is fitted twice, as a hazard law and as a stock-outflow input, with 0 co-citers between the two anchors

Reliability engineering and industrial ecology fit the same two-parameter Weibull to the same
random variable (time from entry-into-service to exit-from-service of a population of nominally
identical artefacts) and both report the shape parameter. Reliability reads β as a hazard law and
selects a maintenance policy from it; industrial ecology passes the fitted β into a stock-driven
outflow model and does not interpret it. Anchors: Weibull 1951 `10.1115/1.4010337` (OpenAlex
`W2727420541`, `cited_by_count` = 11,512) × Oguchi et al. 2015 `10.1021/es505245q`
(`W2320647648`, 103) → **`meta.count` = 0**, OpenAlex `works?filter=cites:…`, fetched 2026-09-05
(via `audits/scout-01-circularity.md`). Same-B control Müller 2006 × Oguchi 2015 = **15**;
control ratio `(0/103)/(15/103)` = 0, isolation unbounded and denominator-free. Contact surface
**1** — a single co-citer on the Murakami Part I pairing, a 2023 *RCR* agent-based-model paper
that cites both as separate ingredients and puts no two β on one axis. Opened `live`, evidence
`citation-intersection`, crosses `formalism`, exit `computation`, `next-step-cost: S`.

## [2026-09-05] computed | C27 — 21 published product-lifespan Weibull fits placed on C18's β axis; products span β = 1.00 to 6.0 and split into a memoryless and a wear-out band

Fetched primary parameters: LBNL (Lutz et al. 2011, `osti.gov/servlets/purl/1182737`, PDF read in
full) gives nine US residential appliance classes with β and standard errors — gas boiler
**1.000 ± 0.148**, room air-conditioner **1.07–1.08**, electric water heater **1.174 ± 0.020**,
refrigerator **1.272 ± 0.187**, gas water heater **1.307 ± 0.061**, heat pump **1.525 ± 0.525**,
freezer **1.885 ± 0.730**, central AC **2.094 ± 0.271**, gas furnace **2.218 ± 0.320**. Held et
al. 2021 (`10.1186/s12544-020-00464-0`, Table 1 via PMC7829067) gives European passenger cars
**β = 2.0–6.0**, characteristic life 8.0–35.1 yr. Against [[C18-durability-axis]]'s enzyme and
organic-flow-reactant rows at β = 1 and Li-ion at β = 12.7: **every product class lies at or above
the enzyme corner and below Li-ion, and the banding cuts across product categories** — a gas
boiler groups with an enzyme, a gas furnace groups with a passenger car. Discriminator stated in
`H = 4^(β−1)`, the hazard-fold over one factor of four in age. Arithmetic in
`vault/_scripts/c27_beta.py`, no network calls.

## [2026-09-05] verification | LBNL Table 10 (room air-conditioners, post-2000) is internally inconsistent; ten of eleven other rows reproduce exactly

Re-deriving `median = θ + η(ln2)^(1/β)` and `mean = θ + ηΓ(1+1/β)` from each row's own printed
(β, η, θ) reproduces the published median and mean to ±0.01 yr for ten of eleven LBNL rows. Table
10 does not: β = 1.08, η = 10.27, θ = 0 give median **7.31** and mean **9.97** yr against the
printed 8.36 and 11.27; the printed median implies η ≈ 11.96. Flagged, not corrected; β is
unaffected and is the only quantity C27 uses.

## [2026-09-05] correction | the DOI circulated for Murakami 2010 "Lifespan of commodities" resolves to a different paper

`10.1111/j.1530-9290.2010.00272.x` is **not** *Lifespan of Commodities*. Crossref resolves it to
*"Environmental Metrics"*, *J. Ind. Ecol.* 2010, `is-referenced-by-count` = 25 (fetched
2026-09-05). The correct DOIs are `10.1111/j.1530-9290.2010.00250.x` (Part I, 172) and
`10.1111/j.1530-9290.2010.00251.x` (Part II, 116), both Crossref-verified the same day. Recorded
because the wrong DOI was carried into a task brief and would have silently produced a wrong
citation.

## [2026-09-05] honest null | the mode-6 decade-binned re-run for G30 could not be made; both instruments failed and no number from either is quoted

Weibull 1951 anchors a 75-year citer window, the textbook [[failure-modes]] mode-6 danger. (a)
The OpenAlex citer-decade route is blocked: the API now returns an explicit
`{"error":"Rate limit exceeded","message":"Insufficient budget … Resets at midnight UTC",
"retryAfter":54004}` on every endpoint including `/concepts?search=`, so the concept IDs for
"reliability engineering", "industrial ecology" and "product lifetime" were never resolved and
**no concept-scoped `N_universe` exists** — every `E` for G30 remains a union floor (102.1) and no
`O/E` is quotable. (b) The Crossref term-frequency route was run over seven decade bins for six
decade-appropriate term sets and **is not selective**: every term's counts track the growth of the
Crossref corpus itself (e.g. "lifespan distribution" 27,451 → 279,154 and "discard function"
22,679 → 286,670 across the same bins, with near-identical curves), because `query.bibliographic`
and `query.title` are relevance queries, not phrase matches. The mode-6 check on G30 is
**outstanding, not passed**, and the note says so.

## [2026-09-05] method | a mediating literature for G30 was found while computing C27, and it threatens the note's own `topology: disjoint`

Lutz et al. 2011 (LBNL) cites Weibull 1951 directly, fits delayed Weibulls to US appliance stocks
from RECS/AHS surveys, prints β with standard errors, and **states the hazard reading** ("β … the
shape parameter, which determines the way in which the failure rate changes"), while separating
physical from consumer/economic lifetime via the delay parameter. It does not take the classifying
step and it cites neither Oguchi nor Murakami, so no Weibull × Oguchi intersection can see it.
`topology` is left `disjoint` only because that literature is not yet anchored and counted;
`citers(Weibull 1951) ∩ citers(Lutz 2011)` and `citers(Lutz 2011) ∩ citers(Oguchi 2015)` should be
expected to move it to `mediated`. Recorded before the fact rather than after.


## [2026-09-05] gap | G31 opened: biosignature assessment has no base-rate term, and no citation to the field that does

Audit `scout-03-astrobiology.md` Job-2 candidate G-E, taken verbatim as starting provenance and
then re-run independently. Catling et al. 2018 (`10.1089/ast.2017.1737`) x Hanley & McNeil 1982
(`10.1148/radiology.143.1.7063747`), OpenAlex `cites:W2949593113,cites:W2157825442`, 2026-09-05:
intersection **0**, `E = 30.8` at the audit's fetched `N = 152,971`.

**The OpenAlex re-run could not be made.** The intersection filter returned
`{"error":"Rate limit exceeded", "dailyRemainingUsd":0}` — daily budget exhausted, probably by
the parallel agents. Work IDs and `cited_by_count` were fetched before exhaustion. The re-run was
therefore done on **OpenCitations** (`api.opencitations.net/index/v1/citations/<doi>`, 2026-09-05)
with a **second anchor pair** — Schwieterman et al. 2018 `10.1089/ast.2017.1729` x Altman & Bland
1994 `10.1136/bmj.308.6943.1552` — plus two further B-side anchors for the mode-6 decade re-run
(Deeks 2001 `10.1136/bmj.323.7305.157`; QUADAS-2 2011
`10.7326/0003-4819-155-8-201110180-00009`).

**Eight pairings, all zero.** Pooled: 565 astro citers x 32,176 diagnostic citers, intersection
**0**, `E = 118.8` at `N = 152,971` and still `E = 11.9` at 10x — the zero survives an order of
magnitude of denominator, which the single Schwieterman x Altman pairing does **not** (`E = 0.56`
at 10x, the G6 lesson). **The control reproduces the audit exactly on a different provider:**
Catling x Kass & Raftery = **4**, the same four DOIs OpenAlex returned, all astro-native Bayesian
model comparison, none diagnostic-test theory. Five DOIs re-resolved through Crossref the same
day. Decade bins (1982 ROC / 1994 sens-spec / 2001 diagnostic review / 2011 QUADAS-2; citing
works 2010s and 2020s): zero in every bin.

`standing: live`, `evidence: citation-intersection`, `crosses: formalism`, `exit: computation`,
`next-step-cost: S`. Open risk stated in the note: the zero may measure a citation-community
boundary rather than a conceptual absence. The 565 citers have **not** been read.



## [2026-09-05] computed | C28: at a prevalence of 1-in-1,000, an O2 detection needs specificity 0.999 to be worth believing

Built the object G31 says is missing. O2 alone (not the O2+CH4 pair, which needs a two-test
combination rule) as a diagnostic test: "disease" = life present, "test +" = O2 above threshold.
The abiotic-source enumeration was taken from Meadows et al. 2018 `10.1089/ast.2017.1727`
(Crossref 2026-09-05, cited-by 301) at **review level — full text not read**; the abstract was
fetched from Europe PMC and states in the authors' own words that the paper covers both false
positives and false negatives for O2.

**Six abiotic routes, zero published probabilities.** That empty column is the result. The field
attaches a *discriminant* to each false-positive scenario and a *rate* to none, so specificity is
not merely unpublished — it is not estimable from the published literature. Prevalence is
therefore carried as a free parameter.

`PPV = sens*prev / [sens*prev + (1-spec)(1-prev)]`, computed over prevalence 1e-3 .. 0.5 and
specificity 0.9 .. 0.999 (`vault/_scripts/c28_roc.py`). Break-even prevalence
`p* = (1-spec)/(sens + 1-spec)`: **0.091 at spec 0.90, 0.0099 at spec 0.99, 0.0010 at spec
0.999.** Inverted: at prevalence 1e-3 a detection needs **spec >= 0.999** to be more likely true
than false, and >= 0.99989 to reach PPV 0.9.

Second half: what the diagnostic frame adds that the CoLD scale (Green et al. 2021
`10.1038/s41586-021-03804-9`) lacks is a **base-rate slot**. Ascending CoLD rungs raises LR+ and
nothing else; the row of the PPV table is chosen by prevalence, so two identical CoLD-6 claims
from a 20-target and a 10,000-target survey carry different posteriors and the same grade.
Also: ordinal levels do not multiply, likelihood ratios do; and nobody has drawn the operating
curve. Honest limit recorded in the note: the arithmetic is Bayes' rule, the contribution is the
framing plus one number nobody has stated.


---


## [2026-09-05] computed | Ecological recovery has a decreasing hazard: Weibull beta = 0.587 [0.510, 0.668] over 221 censored records

C29-recovery-beta fits Jones & Schmitz 2009's own Table S1 (240 recovery studies, doi
10.1371/journal.pone.0005653.s001, fetched 2026-09-05) as a right-censored survival problem:
"Recovered? = Yes" is an event at the stated return time, "No" is right-censoring at the stated
end of observation. 221 usable rows, 127 events, 94 censored (42.5%). Pooled Weibull shape
beta = 0.587, profile-likelihood 95% CI [0.510, 0.668]; four of five habitat classes have a CI
entirely below 1 (Forest 0.769, Marine 0.644, Brackish 0.501, Terrestrial 0.570), Freshwater
0.893 [0.644, 1.186] covers 1. Robust to the free-text range coding (0.580-0.590) and to
dropping the censored rows (0.640). This is the first entry in the vault sitting at beta < 1
with a fitted CI rather than by inference, and it places ecological recovery at the opposite
end of C18's axis from Li-ion wear-out. Produced by vault/_scripts/c29_recovery.py.
Honest limit recorded in the note: beta < 1 on a pooled meta-analysis is equally the signature
of genuine deceleration and of a fast/slow mixture, and this dataset cannot separate them.

## [2026-09-05] correction | Moreno-Mateos et al. 2017 recovery-debt DOI was wrong in the brief

The DOI given as 10.1038/s41467-017-00109-4 returns Crossref HTTP 404. The recovery-debt paper
is "Anthropogenic ecosystem disturbance and the recovery debt", Nature Communications 8:14163,
doi 10.1038/ncomms14163 (Crossref, fetched 2026-09-05, is-referenced-by-count = 293). The
wrong DOI was not used for any count. Same pattern as the three mis-resolved anchors that
audits/scout-02-resilience.md discarded: guessed DOIs for Nature-family papers resolve to the
wrong work often enough that Crossref verification is not optional.

## [2026-09-05] gap | G32 opened - Weibull hazard shape x ecological recovery-time distributions

Rank 2 of audits/scout-02-resilience.md, opened at evidence: citation-intersection with a
computation exit that C29 then took. Provenance and the mode-6 decade re-run are in the note.
Instrument note: OpenAlex returned HTTP 429 on every intersection attempt for the whole session
(five agents in parallel on the polite pool), so the re-run was carried out on OpenCitations
instead, and the note states which numbers are the scout's OpenAlex figures and which are this
run's OpenCitations figures. Two providers, two coverage bases; they are not interchangeable
and the note does not pool them.


## [2026-09-05] gap | G33 opened `narrowed`: reliability's repair-rate ratio is never formed for a remanufactured fleet, and one real bridge exists

Barlow & Hunter 1960 (`10.1287/opre.8.1.90`) x Guide 2000 (`10.1016/s0272-6963(00)00034-6`),
both Crossref-verified 2026-09-05. **The Guide DOI ending `-7` 404s; the correct suffix is
`-6`.** OpenAlex reports intersection = **1** (scout run, 2026-09-05); **OpenCitations COCI,
fetched independently this session, reports 0** over |A| = 1,131 and |B| = 845 citers. Both
numbers are true of their own object: COCI indexes DOI-bearing Crossref reference lists and the
bridging work is a dissertation, whose reference list Crossref does not carry.
`contact-surface: 1` recorded on the gap-unfavourable reading.

The bridge is **Alqahtani, *Warranty cost analysis with preventive maintenance strategy for
remanufactured products in reverse supply chain*, PhD, Northeastern University, DOI
`10.17760/d20249105`** (Crossref record fetched 2026-09-05: type dissertation, sole author,
Northeastern University Library). It carries Barlow-Hunter preventive-maintenance mathematics
onto remanufactured fleets — a real crossing — and its output is warranty **cost**, not a rate
ratio and not an availability. **Full text NOT obtained** (handle redirects to
`repository.library.northeastern.edu`, HTTP 418 to WebFetch / 403 to curl; fulltext.pdf over the
10 MB cap; Routledge pages for the derived book `10.1201/b22308` 403), so "forms no ratio" is
UNVERIFIED and is the note's stated weak link.

Isolation rests on the control ratio, which is denominator-invariant: Barlow & Hunter x Dekker
1996 = 89/966 against 1/1,093, **~100x**. Mode-6 decade binning run on the COCI sets: the true
overlap window is only 2000s-2020s (Guide cannot be cited before 2000), and the co-citer count
is 0 in each of those three decades while both citer sets peak together in the 2010s — a
synchronic separation, not a renaming.

## [2026-09-05] correction | OpenAlex 429 on this vault is a spent daily budget, not IP rate limiting

`audits/scout-01-circularity.md` recorded the 2026-09-05 429s as "IP-level, sustained across
~25 min of backoff". The 429 body seen this session is
`"Insufficient budget. This request costs $0.0001 but you only have $0 remaining. Resets at
midnight UTC"` with `retryAfter` = 53,949 s. Three retries at 20/40/60 s backoff returned the
same. **No backoff inside a session can recover it**, and every scoped `N_universe` blocked on
2026-09-05 must be re-fetched on a later UTC day. Single-work `works/<id>` lookups still
succeeded earlier the same session, so the budget is consumed per request, not per host block.

## [2026-09-05] computed | C31: Ha = L/T for a product fleet, and C6's A = Ha/(1+Ha) is wrong once cores fail to return

Wind-turbine fleet put on C6's axis: **Ha = 86.8** (k_d = 8.367/yr, k_r = 726.4/yr from
Carroll et al. 2016 via C1 §3.2), **A = 0.9886**, between trabecular bone (19.9) and the US
grid. Derived here: with core return rate `r`, the three-state chain gives **A = Ha/(Ha + r)**,
reducing to C6's form only at `r = 1`; with a lossy loop and no new production there is **no
interior steady state at all**, the structural mirror of C6 §4.2's ratchet finding. Prediction:
**A_circ = r·y ≤ r** — core return rate is a ceiling on circular content that no yield gain can
lift. Closest published case, Huster et al. 2023 (`10.1007/s13243-023-00130-3`, open access,
PDF fetched 2026-09-05): German EV batteries, L = 10 yr, r ∈ {0.50, 0.75, 1.00} → **2032
circular ceiling 0.75 at their central return rate, 0.50 at their low one, before any yield
loss.** Three remanufacturing rows left **empty**: the missing input is the mean core
out-of-service time `T`, published nowhere reached. Cat Reman publishes mass with no unit
denominator; the field's own KPI toolbox (Graham et al. 2015, `10.1186/s13243-015-0019-2`) has
Lead Time, Cycle Time and salvage rates and forms no ratio. Arithmetic: `_scripts/c31_ha.py`.

## [2026-09-05] review response | External review of the Charnov–Gittins preprint: three scope clarifications, six references added, no number changed

An unnamed external language model reviewed `papers/charnov-gittins/paper.md` with the paper
only (no vault). It recomputed by hand the current-patch index, the habitat-arm index, the
discounted MVT limit, `W(x) = λx² − r(1−x)²`, `W'(x) > 0`, `dGUD/dr` and Table 1
(`r/λ = 1`: GUD 0.5450, `t*` 0.607) and confirmed every one. Review on file at
`papers/charnov-gittins/reviews/2026-09-05-gemini-flash-3.8.md`.

**No result, number or Limitations entry was withdrawn or softened.** Three scope statements
were added to the paper and mirrored in [[C25-whittle-foraging]] §9.

1. *Sparse-activation gap, now named as open.* Weber & Weiss 1990 (`10.2307/3214547`) needs a
   fixed active fraction `α = M/N`; foraging is `M = 1`, `α → 0`. Four candidate covering
   results were checked and none covers `α → 0`: Hu & Frazier (arXiv:1707.00205) and Zhang &
   Frazier (arXiv:2107.11911) hold the pulled fraction constant; Gast, Gaujal & Yan
   (`10.1007/s11134-023-09875-x`) scale activations with arms; Brown & Smith
   (`10.1287/mnsc.2019.3342`) give a finite-`N` Lagrangian bound evaluable at `M = 1` but
   prove optimality only in the many-item regime. Single-server queueing results, the closest
   structural match to `M = 1`, prove heavy-traffic limits for a system with arrivals, which
   is a different limit. Three further searches ("restless bandit" + "single active arm";
   "Whittle index" + "one arm at a time"; "polling system" + "Whittle index") returned nothing
   that drops the fixed-fraction hypothesis. Limitations item 3 now says the gap is open and
   names it, rather than only noting its absence.
2. *Zero switching delay.* A paragraph after eq. (4) states that `W` is derived with no
   transit; that the passive flow over `τ` preserves within-type rank (because `W` is strictly
   increasing in `x` and the flow is order-preserving) but can reorder patches of differing
   `r`; and that `τ` enters only through the renewal-cycle anchor, so a mixed-`r` network has
   one global `ν`.
3. *GUD scope.* §3.1 now says GUD here is Charnov's residual density at departure under pure
   rate maximisation, and that Brown's operational `H = C + P + MOC` (Brown 1988,
   `10.1007/BF00395696`) enters this model as shifts in the shadow price `V'(x)`;
   `dGUD/dr > 0` is stated for the Charnov quantity.

**Verification, and one DOI corrected.** All four Crossref-held DOIs above were resolved at
`api.crossref.org/works/{doi}?mailto=deciduusleaf@gmail.com` on 2026-09-05 and checked
field-by-field. The candidate DOI supplied for Gast, Gaujal & Yan,
`10.1007/s11134-022-09855-2`, **does not resolve** ("Resource not found"); the record was
relocated by bibliographic query and the correct DOI is `10.1007/s11134-023-09875-x`,
*Queueing Systems* 104(1–2):107–150, 2023. The candidate title for Zhang & Frazier,
*"beating the Lagrangian relaxation"*, is also **wrong**; the arXiv API (2026-09-05) gives
*Restless Bandits with Many Arms: Beating the Central Limit Theorem*. Both arXiv entries are
cited as preprints: neither carries a Crossref record or a journal reference. Six entries were
added to `refs.bib`, each with a `note` recording provider, date and what was not obtained
(no full text was read for any of the six).

**Polish.** The `δ → 0` passage now names the dominating function explicitly (`e^{−δu}g'(u)`
is bounded on the compact `[0, s]` uniformly in `δ ≥ 0`, so a constant dominates), and an
Acknowledgements section records the review.

## [2026-09-05] correction | C18's β axis was not well defined: rows mixed objects and estimators; it narrows to one axis per object class

C18 claimed a single Weibull-β axis spanning catalysis and energy storage, and used it to
reclassify organic flow-battery reactants "with enzymes, against Li-ion". The rows being compared
were not the same kind of quantity. Two were bulk decay-rate constants (enzyme thermal
deactivation; flow-reactant %/day fade), one was an unfitted geometric model (enzyme suicide
inactivation), and only one — Li-ion NCR18650GA, β = 12.7 — was a fitted distribution of unit
lifetimes. C26 supplied the decisive evidence that this matters: the same 100 C-MAPSS FD001
turbofan units give β = 4.41 by direct Weibull MLE on the sample of lifetimes (its R1) and
β = 0.97 by the degradation-to-threshold first-passage route (its R2), a factor of 4.5 from the
estimator alone.

What is now in C18: a comparability rule (§0) naming four object classes; `object` and `estimator`
columns on every row of the §3 table, with `not recorded` on two rows (enzyme suicide inactivation
has no fit at all; the Li-ion source's fitting method is absent from the accessible snippet and the
primary returned 403), both flagged not comparable; a within-class restatement (§3.1); and a linked
cross-reference table (§3.2) to C26, C27 and C29 that keeps each number's provenance in its owning
note. C27's rows are additionally marked as *discard* lifetimes from household surveys, not failure
records.

Withdrawn: "put each on the β axis and Li-ion is the outlier, while flow-battery chemistry and
enzyme chemistry coincide", and the verdict-2 form of the same claim. Restated within class: the
flow-reactant / thermal-enzyme coincidence holds inside the bulk decay-curve class, and the real
result there is that flow-battery fade is first-order in *time*, not in cycles — the authors' own
statement. Li-ion's 12.7 is comparable only with other fitted lifetime distributions, where its
neighbours (C27 product classes 1.00–6.0, C26 R1 4.41) all sit below it. The honest outcome is that
"one durability axis" narrows to "one axis per object class"; C18's `(N_fail, β)` pair becomes
`(N_fail, β, object+estimator)`. G3's construction paragraph was updated to match. Full
sentence-by-sentence diff is in C18 § Corrections 2026-09-05.


## [2026-09-05] prediction failed | C29's prediction 1 does not replicate: per-habitat recovery β does not rank-correlate across datasets

[[C29-recovery-beta]] §5.1 predicted that refitting its Weibull recovery `β` on an independent
meta-analysis would reproduce the per-habitat ordering, with the sign of the rank correlation as
the falsifiable object. [[C32-recovery-beta-replication]] ran it on Moreno-Mateos et al. 2017
(Dryad `doi:10.5061/dryad.t5c97`, `Moreno, Jones database.xlsx`, 3,688 usable outcome measures from
353 studies, fetched 2026-09-05) using C29's estimator unchanged. Spearman `ρ = +0.100`, n = 5,
exact two-sided p = 0.950 at the outcome-measure level; `ρ = −0.300`, p = 0.683 at study level. The
sign flips with the analysis unit and is nowhere near significance. Of C29's five named habitat
statements only "brackish lowest" holds. By C29's own stated terms the claim that `β` measures
something about ecosystem types is dead. Produced by `vault/_scripts/c32_replication.py`.

## [2026-09-05] computed | Pooled recovery β replicates at 0.733 [0.703, 0.764] on a second meta-analysis

Same run. `β < 1` with the profile CI clear of 1 on a dataset with a different recovery criterion,
a different unit of observation and 69.1% censoring (against C29's 42.5%), and stable across
analysis units (0.733 outcome-measure level, 0.721 study level). [[C18-durability-axis]]'s
infant-mortality corner survives; what does not survive is resolution *within* the corner.

## [2026-09-05] honest null | C29's prediction 2 (frailty split) is undecided, not answered

Splitting by Moreno-Mateos' `Metric type` raises `β` toward 1 in the compositional/species class
(0.733 → 0.824) and above 1 in several habitat × class cells (Forest × compositional 1.166
[1.011, 1.328]) but leaves the structural/biomass class — 84% of rows — at 0.723, indistinguishable
from pooled. Neither the clean frailty signature nor the clean null. Recorded as undecided rather
than scored either way.

## [2026-09-05] correction | "Independent replication" overstated: the two recovery meta-analyses share ~95 primary studies

The Dryad deposit for Moreno-Mateos 2017 is named `Moreno, Jones database.xlsx` and its R script
credits data manipulation to Peter Jones — the first author of Jones & Schmitz 2009, C29's dataset.
Matching first-author surname + year across the two reference lists gives **95 shared primary
studies: 37.3% of Jones & Schmitz's 255 references, 27.0% of Moreno-Mateos' 352**. Any future
citation of C32 as an *independent* replication must carry this number. Direction of the bias:
shared studies inflate agreement, so the pooled-`β` agreement is worth less than it looks, while
the ordering failure is if anything harder to explain away.

## [2026-09-05] method | Crouzeilles 2016 rejected as a replication target: its deposited data has no time variable

C29 §5.1 named Crouzeilles et al. 2016 (`doi 10.1038/ncomms11666`) as the alternative target. Its
Dryad deposit (`doi:10.5061/dryad.k3479`, `Meta_analysis.txt`, fetched 2026-09-05) carries site,
disturbance-conversion, taxon/metric dummies and a log response ratio `RR` — and no elapsed-time
column and no recovery yes/no. No survival time can be constructed from it. Recorded so the target
is not re-attempted.

## [2026-09-05] method | Moreno-Mateos' recovery *debt* converted to a survival time, and the conversion is the weak point

The dataset records `Start`, `End`, `Goal` and elapsed `Time since restoration started`, not a
return time. C32 §2 codes recovery as `End` crossing `Goal` in the direction of travel from
`Start`, event or right-censoring at the elapsed time. This treats current-status data as exact
event times and therefore overstates recovery times. Fitting the correct current-status likelihood
degenerates (`β = 0.051`, `η` ~10⁹ yr) because the recovered fraction is nearly flat in elapsed
time: 0.287 at ≤2 yr rising only to 0.360 beyond 80 yr, over 3,688 rows. That flatness is the
single most informative number the run produced and it cuts both ways — extreme "early-or-never",
and a warning that elapsed time carries little information about recovery status in this database.

## [2026-09-05] method | Dryad is behind a proof-of-work bot check; deposits were retrieved by browser, not by defeating it

`datadryad.org` returns an Anubis proof-of-work challenge to scripted requests (HTTP 403, or a
"Validating…" HTML body, for every non-browser user agent tried on 2026-09-05). The two deposits
above were fetched through an ordinary browser session. `vault/_scripts/c32_replication.py`
therefore takes the database by `--xlsx` path and does not pretend it can fetch it, unlike
`c29_recovery.py`. Note for future data-availability work: a Nature Communications "Data
availability" statement pointing at Dryad is not scriptable today.


## [2026-09-05] method | Reservoir audit gains F8 and Part D.3: "the central value is a function of the reduction pipeline" — step 0 now requires a table of independent reductions before any A is computed

The first real run of the audit's step-0 halt ([[C30-venus-phosphine-audit]], Venus PH₃) surfaced
a failure class Part D.2 did not anticipate. D.2 covers a single central value inside its *own*
error bar. Venus is worse: the same three November 2021 SOFIA flights reduce to `<0.8 ppb`
(Cordiner 2022) and to `3 ppb at 5.7σ` (Greaves 2023), and the same ALMA photons gave `20 ppb`
then `1–7 ppb` — each reduction internally significant, the *set* spanning "detected" and "not
detected". That is not METHOD §5's same-class systematic either: there is only one measurement,
and what disagrees is the software downstream of it, so re-observation settles nothing.

What changed in [[reservoir-audit]]: a new **Part C step 0**, mandatory and prior to step 1 —
(a) significance, halting with `NO OBSERVABLE TO EXPLAIN` if the interval contains zero; (b) a
table of every independent reduction of the same photons or records, halting with
`NO AGREED OBSERVABLE` if the rows span detected/not-detected. No `A`, no `Σ`, no enumeration may
be written before that table exists. A three-row contrast is carried in the step itself: C11
(NEAR `+13.46 ± 0.13 mm/s`, agreed → proceed), C30 (pipeline-dependent → halt), D.2's fabricated
`(0.4 ± 3.0) µN` (inside its error bar → halt). New **Part D.3** defines the class and bounds
what a conditional run may claim — calibration against a known enumeration (C30 vs Bains 2021)
yes; a residual specification asserted as real, no. New **F8** in the failure-modes list; the
Standing summary now names five conditions, adding step 0 (F8) and the aperture row (step 5 / F3),
both added 2026-09-05.

Recorded honestly and against the project's interest, in new **D.3a**: the C30 halt was announced
in advance in `audits/scout-03-astrobiology.md` §Job 1 and in the commissioning brief, so the
agent was told the case halts and then reported that it halts. The datum shows the step-0 state is
reachable and well-defined on a real, messy input; it does **not** test whether the instrument
halts on its own, and Part D's central question stays unanswered. The uncontaminated test is
specified: a future run briefed **blind** (agent not told whether the case is resolved, no
expected outcome, no D-class named), with the five-line brief archived verbatim and dated at
`audits/blind-brief-<case>-<YYYY-MM-DD>.md` *before* dispatch and cited in the resulting note.

Also: one pointer line each in [[specification-instruments]] (every instrument in that table
converts a handed number into a required supply, so all of them inherit the exposure) and in
C30 §5. `python _lint.py` → 0 errors.

## [2026-09-05] method | intersect.py now drops blank `citing`/`cited` keys, prints the drop count, and self-tests

`vault/_scripts/intersect.py` built its citer sets from `row["citing"]` with only a truthiness
guard and reported nothing about what it discarded. OpenCitations `/citations/<doi>` returns
records with an **empty `citing` field**; a set built without filtering carries a phantom `""`
which, being present in *every* set built the same way, inflates `N_A`, `N_B` **and every
intersection by exactly 1**. An intersection of 1 is precisely the size at which a gap claim
becomes a bridge claim, so the artefact is maximally load-bearing where it is hardest to see.
What is now different: `_key()` normalises and strips both `citing` and `cited`; blank and
whitespace-only keys are dropped before the set is built; the per-anchor drop count is printed to
stderr and the run total to stdout; and `--selftest` fetches Scheffer 2009 × Si 2011 and asserts
no blank key survives in either set or in the intersection. Produced by: live fetch, 2026-09-05
(`selftest OK: |A| = 3,934, 65 blanks dropped; |B| = 1,783, 12 dropped; |A ∩ B| = 1`; unfiltered
the same pair reports 2). First diagnosed in `audits/scout-04-conservation-genetics.md`, where an
uncorrected pass reported five phantom "1-hit" candidates that are clean zeros. Documented in
`vault/method/citation-sources.md` under the endpoint traps.

## [2026-09-05] verification | every intersection in G29, G30, G31, G33 re-derived on the fixed instrument; no standing moves

Nineteen anchor payloads re-fetched and twenty pairings re-intersected, OpenCitations
`api.opencitations.net/index/v1/citations/<doi>`, 2026-09-05. **No intersection count in any of
the four notes changed, and no `standing`, `contact-surface`, `evidence` or tag moved.** Three
citer-set *sizes* in G31 were one high and are corrected: Catling 2018 188 → **187**,
Schwieterman 2018 496 → **495**, Kass & Raftery 1995 11,867 → **11,866**. What was wrong there is
not the intersections but the *base*: G31 published three pre-filter `|A|`/`|B|` figures beside
post-filter intersections, and asserted that one blank value "appears in every set", when in fact
all seven of its anchors carry blanks and they carry many (14, 49, 713, 52, 47, 237, 358), not
one. G29 was already clean, having stripped blanks by hand at first write; G33's two payloads
contain no blank records at all. Produced by: `_scripts/intersect.py`, blanks dropped, 2026-09-05.

## [2026-09-05] verification | the phantom is real, and would have manufactured ten bridges

Counted directly by rebuilding each set both ways. Unfiltered, these rows would read one higher
than the truth: G29 Scheffer × Si 2 (true **1**), × Randall 1 (true **0**), × Jardine 2 (true
**1**), control × Wissel 269 (true **268**); all eight G31 gap pairings and the pooled row 1 (true
**0**), controls 5 and 3 (true **4** and **2**); G30 Weibull × Bakker 1 (true **0**). Ten of the
twenty pairings re-run. G33 (Barlow & Hunter, Guide 2000), G30's Weibull × Oguchi, × Murakami I
and Müller × Oguchi are unaffected because the *partner* payload carries no blank, which is the
trap's one mercy and also why a clean run on one anchor is no evidence about another.

## [2026-09-05] correction | G29's frontmatter and index said "zero in all three decade bins"; its own body table says 1

`G29:note` now reads "Zero in the 2009-2013 and 2014-2018 decade bins and 1 in 2019-2026". The
body's `§(a) Year bins` table has said `O = 1` in the 2019–2026 bin since it was written; the
summary contradicted the table it summarises. Raised as recurrence of the Griebling-2026 class in
`audits/07-provenance-rounds3-6.md`. **`vault/00-index.md:143` still carries the old wording** and
is owned by another agent this round — it must be brought into line with the corrected `note:`.

## [2026-09-05] correction | G30's control anchor Müller 2006 now carries a DOI, and the control ratio is restated denominator-invariantly

The load-bearing statistic of G30 was a control ratio whose control anchor was unidentified in the
note. Resolved by Crossref bibliographic lookup, 2026-09-05: Müller, *Stock dynamics for
forecasting material flows — case study for housing in the Netherlands*, *Ecological Economics*
59:142–156 (2006), DOI `10.1016/j.ecolecon.2005.09.025`, `is-referenced-by-count` = 460. The
OpenAlex W-id is still not fetched. The ratio was written `(0/103)/(15/103)`, dividing both sides
by the same base — the form `citation-intersection` forbids. Because Oguchi 2015 is held fixed and
the *mathematics-side* anchor is what varies, the invariant divides by the varying side:
`(O_ctrl/|A_ctrl|)/(O_gap/|A_gap|)` = `(15/511)/(0/11,512)` on OpenAlex and `(15/439)/(0/9,239)`
on OpenCitations — unbounded either way, so nothing moves except the basis. Newly stated: the
22× size asymmetry between the two A-side anchors runs *against* the gap, which strengthens it.

## [2026-09-05] verification | G30's OpenAlex zeros reproduce on OpenCitations with the fixed script

G30's published counts are OpenAlex server-side `meta.count` intersections, so the OpenCitations
phantom cannot have touched them — OpenAlex never hands this project a set of DOI strings to
de-duplicate. Cross-checked anyway: Weibull × Oguchi **0**, × Murakami I **1**
(`10.1016/j.resconrec.2023.107216`), × Bakker **0**, control Müller × Oguchi **15** — all four
agree with the OpenAlex figures on an independently assembled provider. Citer-set sizes differ by
provider (Oguchi 96 vs 103, Müller 439 vs 511, Weibull 9,239 vs 11,512) and are not pooled, per
the two-true-numbers rule.

---


## [2026-09-05] correction | C30 row 10: Bains' extremal bound is 1,066 t/yr, not 800 — volcanic A = 10.7, and divergence D1 is withdrawn

The row equated Bains' extremal-aperture bound 1.3e5 molecules cm^-2 s^-1 with 800 t/yr. That
figure was 8e5 / 1000 — a round tau x10^3, not a conversion. Over Venus' surface area
4.602e18 cm^2 (r = 6051.8 km): 1.3e5 x 4.602e18 = 5.98e23 molecules/s / 6.022e23 = 0.993 mol/s
x 33.998 g/mol = 33.8 g/s x 3.1557e7 s/yr = 1.07e9 g/yr = 1,066 t/yr. The implied lifetime
inflation is 769x, the ratio _scripts/c30_phosphine.py had been printing and the note ignoring.
Against volcanic 100 t/yr, A = 10.7, not 8.0 — outside reservoir-audit F7's 1 < A < 10 band, so
the verdict is RULED OUT, not NOT TESTED. C30's only claimed divergence from Bains et al. 2021
(D1) is struck, and the callout's "One row diverges, against Bains" is gone. What survives is
weaker and true: the volcanic exclusion is aperture-fragile, and a further 1.07x of lifetime
inflation would carry it into the NOT TESTED band. Produced by: recomputation from the note's
own conversion chain; audits/06-math-rounds3-6.md row 10.

## [2026-09-05] correction | C30 row 6: "8-15 orders of magnitude" is an oxygen fugacity, not a flux ratio — A withdrawn

Bains 2021's crust/mantle f(O2) excess "8-15 orders of magnitude too high to support reduction
of phosphate" had been tabulated as A = 1e8-1e15, with the "max available <= 1e-3 t/yr" column
back-derived to make it land there. f(O2) and PH3 production flux are related through a redox
equilibrium, not linearly, so no order-count transfers. No S_max in t/yr is published for this
route. The row now reads "A: not formable as flux — fugacity margin only", is moved out of the
A-ranked ledger, and its verdict is restated as RULED OUT (no flux bound published) — on Bains'
thermodynamics, not on this ledger. C30 section 6's "the largest robust abiotic A is 1e15" is
corrected: the largest computed A is 1.4e5 (lightning). Produced by: re-reading the bounding
quote's axis; audits/06-math-rounds3-6.md row 6.

## [2026-09-05] correction | C30 rows 5 and 7 marked RESTATED: three ledger rows re-divided Bains' own margins, so the calibration was tautological there

Rows 5 (photochemistry) and 7 (tribochemistry) had S_max values back-derived from Bains' own
"at least 5 orders" and "at least two orders", so dividing them by S_req returns Bains' margin
rather than an independent check. C30 section 3 now states which rows the ledger computes from a
published physical flux — 1, 1b, 3, 4, 10 — and which two merely echo; section 4 concedes that
"the ledger excludes exactly that set" is tautological on rows 5 and 7 and carries no A at all
on row 6. The Pioneer-style calibration claim holds on five rows, not eight. Produced by:
audits/06-math-rounds3-6.md row 6 note on back-derivation.

## [2026-09-05] correction | 10.1038/s41467-022-30804-8 was recorded "not located"; it resolves, is by Jordan/Shorttle/Rimmer not Bains, and it re-grades C30's biotic row

C30 section 6 recorded "Bains et al. 2022 Nat. Commun. (10.1038/s41467-022-30804-8) — not
located under that DOI". Crossref (api.crossref.org/works/..., mailto query, fetched 2026-09-05)
returns it cleanly: Jordan, Shorttle & Rimmer, "Proposed energy-metabolisms cannot explain the
atmospheric chemistry of Venus", Nature Communications, published 2022-06-14, is-referenced-by
12. Open-access full text read via Europe PMC PMC9198073. Two errors in one line: a failed
lookup written down as a bibliographic fact (audit 02's class, second instance), and an
attribution to Bains that the record does not support.

The paper is adverse to the row C30 graded BIOTIC — SURVIVES. Jordan et al. couple each of the
three proposed Venusian sulfur energy-metabolisms to a photochemical-kinetics code and find all
three reproduce the observed SO2 depletion only "by violating other observational constraints on
Venus's atmospheric chemistry", capping sulfur-metabolising cloud biomass at ~1e-5 to 1e-3
mg m^-3 against Earth's aerial biosphere at 44 mg m^-3. Added to C30 as ledger row 14. Row 13
is re-graded SURVIVES -> NARROWED: every named energy source proposed for a Venusian cloud
biosphere is excluded, and what remains standing is only what Jordan et al. themselves leave —
"a low mass biosphere ... the only observable effect of which is to release relatively small
amounts of trace metabolic gases", phosphine named among them. The row clears the availability
leg only with its metabolism unspecified, which makes it a specification of an unknown rather
than a surviving candidate. No A is recorded for row 14: a biomass ceiling is not a flux ratio,
the same discipline the row-6 correction enforces. Lingam & Loeb 2020 publish no numeric biomass
density, so the row-13 biomass leg stays qualitative and the comparison to Jordan's ceiling
cannot be closed. Produced by: audits/07-provenance-rounds3-6.md, Crossref + Europe PMC.

## [2026-09-05] method | C30's script and table reconciled on the 769x ratio; three of four errors were one habit

_scripts/c30_phosphine.py gained Venus' surface area and a flux_to_t_yr() conversion; the
extremal-aperture line now computes 1,066 t/yr and A = 10.7 from the 769x ratio instead of a
hard-coded 1e3, rows 5 and 7 are tagged [RESTATED], row 6 moved to a FUGACITY_ONLY block with no
A, and a cross-check prints 1e8 cm^-2 s^-1 -> 8.20e5 t/yr against Bains' independently quoted
8e5, confirming the conversion chain. Pattern worth recording: three of the four numeric
corrections above are the same habit — a published margin adopted as if it were a computed one
(the round tau x10^3, the fugacity order-count, the back-derived shortfalls). The A-ledger's
whole value is the independent division; wherever C30 restated instead, it manufactured
agreement it had not earned.


## [2026-09-05] correction | C25's residence-time column assumed an arrival state its own model forbids

The t* column of C25 section 5 and Table 1 of papers/charnov-gittins/paper.md were computed from
an arrival at x = 1, while the note's passive dynamics give a round-robin steady-cycle arrival at
x_arr = 1 - (1 - GUD)e^{-r*tau}. At r*tau = 0.2 the residence ratio is 0.198, not 0.757 - a factor
of 3.8 - and the corrected column is non-monotone, peaking at 0.356 near r*tau = 2, where the old
one fell monotonically. The old column is retained under the honest label t_full (depletion time
from a full patch). W(x) = lam*x^2 - r(1-x)^2, indexability, GUD(rho) and dGUD/dr are unaffected
and were re-verified digit for digit; the arrival state enters none of them. Produced by
vault/_scripts/c25_whittle.py, which now prints both columns and the non-monotonicity.

## [2026-09-05] correction | C25's "independent confirmation" of the Whittle index was circular

Section 3 obtained V'(x) = 1-x by substituting nu = W(x) into the indifference condition at every
x - which is the definition of the Whittle index, not a check on it - and then called
re-substituting it a confirmation. Worse, V(x) = x - x^2/2 is not a value function: the active
branch gives lam*x - lam*x(1-x) = lam*x^2, which varies with x and cannot equal a constant gain.
Restated as a consistency check; the shadow-price "room left to grow" reading is now marked an
interpretive gloss.

## [2026-09-05] correction | C29's recovery-debt corollary: 40^(-0.413) is 0.218, not 0.30

Section 5.3 reported h(40)/h(1) = 0.30x and "three times less promising". The correct value is
0.2179 and its inverse 4.59, so "~4.6 times". beta = 0.587 and eta = 39.4 yr are unchanged - the
error was a hand evaluation of the power, not the fit. The correction STRENGTHENS the note's
claim. (20^(-0.413) = 0.290, so 0.30 is what a 20-year horizon would have given; the exponent was
applied to the wrong base.) vault/_scripts/c29_recovery.py now computes the corollary at 10/20/40/
100 yr from the fitted beta so it cannot drift again.

## [2026-09-05] correction | C32's pooled beta = 0.733 is not identifiable; the robustness sentence omitted the disagreeing variant

Section 5 certified beta = 0.733 as "not damaged" on the strength of two analysis-unit variants
agreeing (0.733 and 0.721) - both runs of C29's exact-event-time likelihood, which the note's own
section 2(b) shows is the wrong likelihood for current-status data. The correct current-status
likelihood gives 0.051 [0.014, 0.089], eta in the billions of years: a factor of 14. The Weibull
shape is NOT identifiable from the Moreno-Mateos database. What survives is qualitative - the
recovered fraction is nearly flat in elapsed time (0.287 at T <= 2 yr, 0.360 at T > 80 yr) - i.e.
early-or-never as a claim about shape, with no number attached. Also corrected the read-across to
C29, which was pointed the wrong way: current-status does not transfer (Jones & Schmitz report
exact return times); design-chosen censoring times do.

## [2026-09-05] correction | C28's callout attributed a specificity range to an enumeration that supports none

The pull-quote read "at the specificities the field's own false-positive enumeration can plausibly
support (0.90-0.99)" while the body concludes specificity "is not currently estimable from the
published literature" and the honesty section calls 0.9-0.999 "illustrative, not measured". An
enumeration of false-positive mechanisms is a list, not a rate over a reference population. No
arithmetic changed; the callout now carries the disclaimer the body always did. The note's real
output - the inversion, prev = 1e-3 requires spec >= 0.999 - is untouched.

## [2026-09-05] correction | C27's RAC "natural experiment" is withdrawn; P1 is untested

Section 5 called the LBNL room-air-conditioner pre-2000/post-2000 pair a natural-experiment
measurement of prediction P1 "and it passes". Withdrawn for three independent reasons: (1) the two
rows carry theta = 8.0 and theta = 0, and section 6(c) of the same note says a large theta inflates
beta and makes those rows non-comparable; (2) the quoted mean shift 14.75 -> 11.27 yr uses the
published post-2000 mean that section 3 flags as internally inconsistent with its own (beta, eta,
theta), which give 9.97 yr and -32%, not -24%; (3) no intervention occurred - two survey vintages
fitted separately. No fitted value changed. P1 and P2 remain stated and untested.

## [2026-09-05] method | c32_replication.py fails with an explicit message when the Dryad file is absent

The Moreno-Mateos database (Dryad doi:10.5061/dryad.t5c97, 'Moreno, Jones database.xlsx',
400,066 bytes) is not in the repository and datadryad.org sits behind a proof-of-work bot check,
so the script cannot fetch it. Missing --xlsx now exits 2 with the deposit, filename, byte size
and manual download step named, instead of a bare FileNotFoundError. C32's numbers remain
unreproduced in CI - stated, not silent. Every run now also prints all three pooled-beta variants
together and the recovered-fraction-vs-elapsed-time table.


## 4. Audit-06 items left open by this pass (out of scope, listed so they are not lost)

- Items 1–4 (C30 row 10 = 1,066 t/yr and `A = 10.7`; rows 5/6/7 `RESTATED`; the callout's
  "with a published bound") — C30 is another pass's file.
- Item 9 (C25 §4's `r → 0` revisitable limit restated as a limit of the `r > 0` family, and the
  `λx²` vs `λx` transform carrying no behavioural content under §5's anchoring) — **not done**;
  it is a §4 rewrite this pass did not have a mandate for and it does not affect any number.
- Item 12 (C32 overlap rerun with surname+initial+year keys; reconcile 352/353/356).
- Items 18–21 (C31), 22–23 (C26), 24 (C29 retitle + `result:`), 25 (vault-wide `RUN:` fields and
  a SHA-256 for the C32 Dryad file).


## [2026-09-05] correction | G32 narrowed: fire ecology has the Weibull shape parameter; recovery ecology does not

G32 claimed "ecology's recovery literature has never imported the shape parameter" and was read
as the general claim about ecology. Every intersection row anchored side B on Weibull 1951
(`10.1115/1.4010337`), a *J. Appl. Mech.* methods paper, so the zeros measured who cites that 1951
paper, not who fits a Weibull — the B-side form of the [[failure-modes]] mode 1 synonym trap.

Re-run with the B side varied (OpenCitations, `api.opencitations.net/index/v1/citations/<doi>`,
fetched 2026-09-05, blank `citing` keys dropped before intersecting; a purpose-written fetch, not
`_scripts/intersect.py`, whose current version has the blank-key bug):

- **Fire ecology cites the survival canon.** Johnson & Gutsell 1994 × Cox 1972 = **11**,
  × Kaplan–Meier 1958 = **3**, × Muenchow 1986 = **2**; Clark 1989 × Cox = **2**,
  × Kaplan–Meier = **1**. Hits include *Quantifying Fire Cycle from Dendroecological Records Using
  Survival Analyses* (`10.3390/f7070131`) and *White pine weevil attack on white spruce: a survival
  time analysis* (`10.1890/1051-0761(2000)010[0225:wpwaow]2.0.co;2`).
- **Recovery ecology does not.** Jones & Schmitz 2009 and Moreno-Mateos 2017 return **0** against
  all three B anchors; Pimm 1984 returns 2 / 1 / 0 and Crouzeilles 2016 returns 2 / 1 / 0. All six
  hits inspected: a corporate-reputation paper, an organism-longevity paper, a kelp-heatwave paper,
  a narrative restoration review, and three Cox/Kaplan–Meier fits to **individual** seedling,
  tadpole and planted-tree survival. None fits a hazard to an ecosystem's recovery duration.

`standing: live → narrowed`; `topology: disjoint → mediated` with Johnson & Gutsell 1994 as
mediator; `contact-surface: 0 → 1` (the single recovery↔fire co-citation
`10.1016/j.biocon.2013.08.029`, recorded on the gap-unfavourable reading). Claim re-scoped
everywhere to *recovery* ecology. Produced by the intersection table in the note's
"The B side, varied" section.

## [2026-09-05] correction | G32's "positive control" was the counter-example

Johnson & Gutsell 1994 is *Fire Frequency Models, Methods and Interpretations* (Adv. Ecol. Res.
25, `10.1016/S0065-2504(08)60216-0`) — an ecology review **of Weibull hazard fitting** that
tabulates shape and scale parameters. `audits/scout-02-resilience.md` §3 had already written "fire
ecology *does* touch Weibull"; G32 demoted that into a control row and kept the general claim. A
control that does not fire is not a control. It is now a named counter-example and the topology's
mediator; the four ecology-internal controls carry the pipeline-detects-the-event job unchanged.

## [2026-09-05] correction | Muenchow 1986 DOI: `10.2307/1938954` resolves to the wrong work

`10.2307/1938954` is a 1982 *Ecology* paper on cotton-rat thermoregulation, not *Ecological Use of
Failure Time Analysis*. The correct DOI is **`10.2307/1938524`** (Crossref bibliographic search,
2026-09-05). Clark 1989, *Ecological Disturbance as a Renewal Process* (*Oikos* 56), had no DOI on
file and is **`10.2307/3566083`**. Both were verified before any count was run against them.

## Re-check list for the orchestrator (not done here, by instruction)

- `vault/00-index.md` line for G32 still renders `standing/live` and the inflated control range
  "controls 7–31"; blanks-stripped values are 6–30 (audit 07 items 8 and 3).
- G32's Provenance block still omits anchor DOIs for Hillebrand & Kunze 2020 (`10.1111/ele.13457`)
  and Johnson & Gutsell 1994; both are now recorded in the note's body instead.
- `vault/method/failure-modes.md` mode 6 should gain the rule that binning the citer window is
  insufficient when the **B-side** anchor is a proper-noun methods paper. G32 is the specimen.
- `C29-recovery-beta` and `C32-recovery-beta-replication` are untouched and their numbers stand;
  neither was edited under this fix.


## [2026-09-05] computed | a published blue-tit winter model runs at LOLE 6.6e-7 h/winter, five orders below the grid's 1-in-10

C33-lolp-starvation writes power-system adequacy and small-bird winter energetics in one
notation and shows the LOLP recursion and the starvation backward equation are the same dynamic
program: S(x,t) = max_u E[S(min(x_max, x + g_u(xi) − c(eta)), t+1)], 0 absorbing, with value of
lost load and the marginal fitness value of fat both read off dV/dx. New number: the starvation
probability of Brodin, Nilsson & Nord 2017's fully parameterised blue-tit SDP (Oecologia
185:43-54, DOI 10.1007/s00442-017-3923-3, open-access full text fetched from Europe PMC
PMC5596050 on 2026-09-05), recomputed here by exact forward propagation of the joint (reserve,
weather) distribution at the model's own 5-min resolution = 8.25e-8 per 100-night winter, i.e.
LOLE = 6.6e-7 unserved h/winter. The paper publishes trajectories, not this probability. Two-way:
North America's LOLE <= 0.1 d/yr (1-in-10) reads as P(starve|winter) = 0.100, p/night 1.05e-3,
and is matched by the bird only after a 43.8% cut in foraging gain; GB/France/Belgium/Poland's
LOLH <= 3 h/yr reads as P = 0.375 (47.5% cut); Ireland's 8 h/yr saturates the mapping. Grid
criteria from ESIG 2024, New Resource Adequacy Criteria for the Energy Transition, DOI
10.2172/2372882, PDF fetched from osti.gov/servlets/purl/2372882 on 2026-09-05. Reserve-margin
leg: the bird's dusk reserve (33.0 kJ, derived as x_start 12 kJ + the 21.0 kJ good-night draw)
sits +57.1% above a typical night's draw and +31.0% above a cold night's — two to four times the
15-20% planning reserve margin convention (ESIG: WECC-CAMX PRM >= 15%, mainland Spain >= 10%).
Mechanism, and the transferable claim: remove the bird's demand-side lever (nocturnal
hypothermia, 30% saving) and the margin falls to +10% on a typical night and to a -8.3% deficit
on a cold one, so the bird buys most of its adequacy on the demand side and only a modest part on
the supply side. Falsifier stated: if measured dusk fat over overnight expenditure in wild parids
sits at 0.10-0.20 rather than near 0.5, the quantitative leg fails. Honest limits in the note:
the bird's daily foraging-gain CV is 0.85% against a grid's one-to-two-orders-larger correlated
inflow noise, so the five-decade LOLE gap is partly a variance statement not only a sizing one;
the 8-h "mean remaining night" charge is this note's convention and rescales every absolute LOLE;
fitness and currency are not commensurable, so the shadow-price identity is exact as a dynamic
program and analogical as an economics; grid outages are restorable and starvation is terminal.
Script vault/_scripts/c33_lolp.py (own OpenCitations fetcher; intersect.py not used).

## [2026-09-05] gap | G34 opened: LOLP and starvation risk are one first-passage problem, 0 co-citers on 4 of 4 pairings in every decade bin

Power-system reliability and behavioural ecology both compute the probability that a stored
reserve hits zero before a horizon under stochastic income and stochastic draw, both solve it by
backward stochastic dynamic programming on a value function over the reserve state, and both read
a shadow price off that value function's derivative (value of lost load; marginal fitness value
of fat). Citer-set intersection over OpenCitations
(api.opencitations.net/index/v1/citations/<doi>, fetched 2026-09-05 by vault/_scripts/c33_lolp.py,
which carries its own fetcher because intersect.py's blank-key handling was under repair):
Billinton & Allan 1996 (10.1007/978-1-4899-1860-4, N=2,058) x McNamara & Houston 1987
(10.2307/1939235, N=422) = 0; Billinton & Li 1994 (10.1007/978-1-4899-1346-3, N=1,094) x Houston &
McNamara 1993 (10.2307/3676736, N=196) = 0; the two cross pairings = 0. Same-side controls
separate: power x power 276 (25.23% of the smaller set), ecology x ecology 25 (12.76%). Six
records with an empty `citing` key were dropped across the six fetches; without that filter the
phantom "" joins every set and each zero would have read 1. Failure-modes mode 6 applied: both
citer sets binned by the OpenCitations `creation` decade and the intersection recomputed per bin
— zero in every bin on every pairing, while both controls vary across decades. The 1980s bin is
uninformative rather than a zero (the grid anchors are 1994 and 1996), so the honest window is
1994 onward. Scope restriction adopted from the scout's own objection: the claim is against
storage-constrained adequacy, where LOLE depends on a state-of-charge trajectory, not against
classic LOLP-of-a-thermal-fleet, which convolves an outage table against a load-duration curve
and has no integrated state. Single-provider: the OpenAlex leg is still outstanding, and no
concept-scoped N_universe was fetched, so every E is a union floor and flatters the claim.


## 2. Add to `vault/00-index.md`

Gaps block (between the `IDX:GAPS` sentinels — regenerate with `python _idx.py`, do not
hand-edit):


- [[G34-lolp-starvation-risk]] — *citation-intersection* — Grid adequacy and small-bird winter energetics compute the same first-passage probability, P(a stored reserve hits 0 before a horizon), by the same backward stochastic dynamic program, and read the same shadow price off dV/dx (value of lost load; marginal fitness value of fat). Four anchor pairings over OpenCitations, 2026-09-05: intersection 0, in every decade bin, against E floors 166-350. Same-side controls 25.23% and 12.76% of the smaller set. Scoped to storage-constrained adequacy, not classic thermal-fleet LOLP. Closed by computation in C33.


Computed block:


- [[C33-lolp-starvation]] — **LOLE and starvation probability on one axis.** A published blue-tit winter SDP (Brodin et al. 2017) runs at P(starve) = 8.2×10⁻⁸ per 100-night winter — LOLE 6.6×10⁻⁷ h/winter, five orders below the grid's 1-day-in-10-years — and would need a 43.8% cut in foraging gain to reach it. Read the other way, Europe's LOLH ≤ 3 h/yr is a 37.5% per-winter death rate. The bird's dusk reserve is +57% over a typical night's draw and +31% over a cold one, two to four times the 15–20% planning reserve margin; strip its demand-side lever (hypothermia) and the margin falls to +10%


## [2026-09-05] computed | alpha for genetic load is ~45, not the wafer's ~3: Haldane-Muller is right to 1.6%

C34-load-yield-clustering fits the negative-binomial clustering parameter alpha to human de novo
mutation counts, via a method-of-moments mixture fit on Jonsson 2017's published parental-age
regression (b_f = 1.51/y, b_m = 0.37/y, mu = 70.0; DOI 10.1038/nature24018, Crossref-verified
2026-09-05). alpha = 45.0 point, 45.4 [25.9, 91.5] by Monte Carlo over the uncertain inputs
(2x10^5 draws); Kong 2012's slopes give 22.2. Semiconductor yield's fitted alpha for real wafers
is 0.3-5, so genetic mutation counts sit an order of magnitude deeper in the Poisson limit than
silicon defects do. Consequence: Stapper's (1+U/alpha)^(-alpha) exceeds Haldane-Muller's e^(-U)
by only +1.59% at U = 1.2 and +5.35% at U = 2.2, against +21% at the wafer alpha = 3. The excess
is exp(U^2/2alpha) for U << alpha, so alpha must fall below 7.6 (at U = 1.2) or 25.4 (at U = 2.2)
before the correction reaches 10%. Load-bearing intermediate result: alpha is exactly invariant
under Poisson thinning, so the alpha fitted on total DNM counts is the one that belongs in the
load formula and the unknown deleterious fraction p cancels. Honest limits, all stated in the
note: the paternal-age SD is ASSUMED (6.0 y) and swept 3-10 y, which is what the interval is made
of; liveborn ascertainment has already thinned the upper tail and inflates alpha-hat by an
unknown one-directional amount; and the fitted object is the per-generation mutation *rate*, not
the segregating *load* that conservation genomics actually simulates. Script
vault/_scripts/c34_yield.py, seed 20260905.

## [2026-09-05] gap | G35 opened: Haldane-Muller e^(-U) and Poisson die yield e^(-A*D0) are the same law, 0 co-citers on 18 of 18 pairings

Population genetics' mutation load and semiconductor yield engineering's defect-density model
write the same survival law - exp(-expected number of independently-acting lethal defects), with
per-defect severity cancelling out - and have never cited each other. Citer-set intersection over
OpenCitations (api.opencitations.net/index/v1/citations/<doi>, fetched 2026-09-05): six genetics
anchors spanning 1963-2022 (Kimura, Maruyama & Crow 1963 10.1093/genetics/48.10.1303, N=349;
Lynch, Conery & Burger 1995 10.1086/285812, N=872; Charlesworth 2009 10.1038/nrg2526, N=1596;
Agrawal & Whitlock 2012 10.1146/annurev-ecolsys-110411-160257, N=214; Kyriazis 2021
10.1002/evl3.209, N=251; Bertorelle 2022 10.1038/s41576-022-00448-x, N=250) against three yield
anchors spanning 1964-1990 (Murphy 1964 10.1109/proc.1964.3442, N=318; Stapper 1983
10.1147/rd.276.0549, N=238; Cunningham 1990 10.1109/66.53188, N=277). O = 0 on all 18, against E
floors 113-289. All nine DOIs Crossref-verified 2026-09-05 and each returned the intended work.
Fifteen in-domain controls fire - genetics side 16-82 co-citers, yield side 14-52 - so both
literatures are findable and internally joined and the zeros are not an indexing artifact. This
is failure-modes mode 6 run properly: the zero holds in every decade bin on both sides under that
decade's own vocabulary, and no anchor is a proper noun, a possessive or a shared homograph (the
two fields share no word at all, hence crosses: nothing).

Two method points. (a) The blank-`citing` filter is load-bearing: OpenCitations /citations/
returns records with an empty `citing` field, and an unfiltered set carries a phantom "" that
belongs to every set and inflates N_A, N_B and every intersection by exactly 1. This run dropped
25 blank records across nine anchor fetches; without the filter all 18 zeros would have read 1.
(b) Honest null-model failure: N_universe could not be fetched. OpenAlex
api.openalex.org/concepts?search=... returned HTTP 429 on all 15 attempts across three probe
rounds with exponential backoff, 2026-09-05, so only union floors exist and per
citation-intersection the mandatory sensitivity run has NOT been done. The zero is therefore
recorded as not yet quotable as a finding, and the gap's evidence rests on the same-object
argument first and the E floors second. Every control ratio is exactly 0 because every gap
intersection is 0, so the control ratio carries no ordering information here.


## 2. Two lines for `vault/00-index.md`

The gaps block between the `IDX:GAPS` sentinels is **generated** — run `python _idx.py` from
`vault/` rather than pasting the gap line by hand. It should produce, under `### Live`:


- [[G35-genetic-load-die-yield]] — *citation-intersection* — Haldane-Muller mean fitness e^(-U) and Poisson die yield e^(-A*D0) are the same survival law, both independent of per-defect severity. Citer-set intersection 0 on 18 of 18 pairings (6 genetics anchors 1963-2022 x 3 yield anchors 1964-1990), OpenCitations 2026-09-05, against E floors 113-289; 15 in-domain controls fire 14-82. No concept-scoped N could be fetched (OpenAlex 429-locked), so the zero rests on union floors only.


The computed line is hand-maintained; add it to the computed-notes list beside `C31`/`C32`:


- [[C34-load-yield-clustering]] — **α = 45 [26, 92]** for human de novo mutation counts, against **0.3–5** for defects on a wafer. Stapper's clustered-defect yield exceeds Haldane–Muller's `e^(−U)` by only +1.6% at `U = 1.2` and +5.4% at `U = 2.2`; the correction needs α ≤ 7.6 to reach 10%. α is invariant under Poisson thinning, so the deleterious fraction cancels. Narrows [[G35-genetic-load-die-yield]]; the segregating-load α is a different and untested number


## [2026-09-05] computed | Soil on C6's Ha axis: conventional agriculture Ha = 0.011, native vegetation 1.31, and the USDA T-value is a Ha = 1 by construction that overstates measured soil formation 10-51x

C6's soil row was blank. C35 fills it from Montgomery 2007 (PNAS, doi 10.1073/pnas.0611508104,
Table 1, author-hosted PDF text-extracted 2026-09-05, VERIFIED-PRIMARY): erosion medians 1.537
(conventional, n=448), 0.082 (conservation, n=47), 0.013 (native vegetation, n=65) mm/yr against
a soil-production median of 0.017 mm/yr (n=188). Ha = k_r/k_d gives 0.0111 / 0.207 / 1.31, i.e.
A = 0.011 / 0.172 / 0.567. Conventional agriculture is now the lowest-Ha system in the vault,
two orders below PSII under cold stress. The USDA tolerable-soil-loss T sets k_d = k_r by
definition, hence Ha = 1 and A = 0.5 with no measurement in it; against the measured formation
rate the same erosion sits at Ha = 0.020-0.099, so T overstates soil formation by 10.1x-50.7x
(1-5 short ton/acre/yr = 0.172-0.862 mm/yr at an ASSUMED bulk density of 1300 kg/m3). Falsifier
and dataset stated (SSURGO tfact joined to Montgomery's SI 10-Be sites). Borrelli 2017 numbers
are VERIFIED-SECONDARY only: nature.com 303-redirects to an IdP, DOI Crossref-verified.
Arithmetic: python _scripts/c35_soil.py.



## [2026-09-05] gap | G36 opened: wear/fatigue mechanics and soil removal do not meet - 13 pairings, 13 zeros, 5 controls at 60-257

Two legs on one gap. Leg 1, Archard 1953 / Meng & Ludema 1995 against Nearing 1989 (WEPP) /
Le Bissonnais 1996. Leg 2, Miner 1945 / Paris & Erdogan 1963 against Le Bissonnais 1996 /
Denef 2001 / Amezketa 1999. Counts re-derived here, not copied from audits/scout-05: citer-set
intersection over OpenCitations api.opencitations.net/index/v1/citations/<doi>, 2026-09-05, with
blank `citing` records dropped before set construction (dropped: Archard 21, Paris 15, Miner 13,
Meng 2, Amezketa 1). All nine anchor DOIs re-verified on Crossref the same day. Thirteen gap
cells, every one 0, against union-floor E of 338-1,025. Controls on the same instrument: Miner x
Paris 257, Meng x Archard 242, Amezketa x Le Bissonnais 204 (NEW, not in the scout), Denef x
Le Bissonnais 38, RUSLE x Nearing 60 - all four control ratios infinite. |A|.|B| = 7.63e6
(Archard x Nearing) and 5.75e6 (Miner x Le Bissonnais), so E > 1 for any N below ~6-8M; the
Meng rows are weaker (3.4-9.3e5) and are corroboration only. Nothing inspected because every
gap cell is 0; the five control intersections were NOT inspected and are counts, not verified
bridges. Mode 6 only half addressed - mechanics anchors span 1945/1953/1963/1995, the soil
anchors are all 1989-2001, and a 1930s-1960s soil anchor (Yoder, Emerson, Ellison) has not been
run. That is the cheapest thing that could overturn the zero, and the note says so.


## [2026-09-05] gap | G37 opened: adaptive management ↔ Duane reliability growth, 0 intersection on 15 of 15 pairings

Conservation's adaptive management and reliability engineering's reliability growth both ask how
fast a programme of deliberate trials drives its failure rate down; engineering fits a growth
exponent β and conservation has never computed one. OpenCitations citer-set intersection
(`api.opencitations.net/index/v1/citations/<doi>`, all fetches 2026-09-05, empty `citing` records
dropped), five A anchors 1990–2013 × three B anchors 1964–1982: **0 in all 15**, E floors 23–358.
`scout-04`'s two headline rows reproduce exactly on an independent client (996/500/0, E floor
333; 569/500/0, E floor 266). Four in-domain controls fire — Walters & Holling × Williams = 64,
Allen × Walters & Holling = 45, Westgate × Williams = 46, Fischer & Lindenmayer × Westgate = 20,
Crow 1982 × Duane 1964 = 36 — so the zeros are not an indexing artifact.

**Two corrections carried in the note.** (a) Fischer & Lindenmayer 2000 is
`10.1016/s0006-3207(00)00048-3`; the widely copied `10.1016/S0006-3207(99)00048-3` **404s at
Crossref** and was replaced by bibliographic title search. (b) Seddon 2007
(`10.1111/j.1523-1739.2007.00724.x`) returns an OpenCitations citer set of size **1** and its row
is **void, not a zero**.

**Not done and it matters:** the concept-scoped `N_universe` (OpenAlex, `C200601418` ∪
`C2775917145`, from 1964) returned **HTTP 429 on all three attempts, 2026-09-05**. Every `E` in
G37 is a union floor and is labelled as one. The gap is at floor strength until that call lands.



## [2026-09-05] computed | C36: conservation's first Crow-AMSAA growth exponent — β = 0.67–1.11 against engineering's 0.3–0.6

Balanced 1990–2015 panel of RAM Legacy v4.65 (Zenodo record 11995054, `RAMLDB v4.65.zip`,
117,140,306 bytes, fetched 2026-09-05); each assessed stock-year is one unit of cumulative
programme operating time, each stock-year with `U/Umsy > 1` one failure of a repairable system;
time-truncated Crow-AMSAA MLE with exact χ² bounds. **US West Coast β = 0.672 [0.589, 0.761];
US East Coast 0.815 [0.730, 0.904]; US Southeast & Gulf 0.861 [0.774, 0.952]; European Union
0.916 [0.861, 0.973]; Mediterranean–Black Sea 1.105 [0.943, 1.279]; Indian Ocean 1.362
[0.990, 1.793].** MIL-HDBK-189 plans hardware development at β ≈ 0.3–0.6 — conservation
programmes learn, and roughly half as fast.

**The estimator sensitivity is the second finding and it is C26's lesson again.** Dropping the
balanced-panel requirement moves US West Coast from **0.672 to 2.597** on identical data, because
RAM's assessed-stock count grows through the record and the unbalanced fit measures the growth of
the *assessment* programme rather than the learning of the *management* programme. No unbalanced
number is quotable. Two controls run: a homogeneous-Poisson null returns β median 1.004–1.017
(estimator unbiased), and recovery of a known β on integer exposure slots reads 0.4 as 0.591, so
the low βs are **upper bounds** and the engineering comparison is conservative.

**The prediction G37 licenses is consistent but not yet tested:** four US Magnuson-Stevens regions
average β = 0.82 with three CIs excluding 1; four RFMO/weak-governance rows average β = 1.13 with
none excluding 1 — difference 0.31, in the predicted direction. **The structure coding was
assigned by me after seeing the βs**, so it is a consistency check, not a test. The named test
dataset is **DIISE** (per-attempt island-eradication outcomes), which **could not be fetched**:
the site serves no data endpoint. Fischer & Lindenmayer 2000's relocation table (Elsevier) and the
IUCN reintroduction databases were also not reached; those rows are **empty, not estimated**.
MIL-HDBK-189's 0.3–0.6 band is marked **UNVERIFIED** — quoted from the reliability-growth
literature, not read from the handbook.

## [2026-09-05] computed | C37: the LOLP-starvation identity is conditional, not exact - and ruin theory is the uncited parent of both


C33 §1 asserted that the storage-constrained loss-of-load recursion and the small-bird
starvation recursion are "the same dynamic program" and called it exact. C37 states the
theorem properly and finds five conditions it needs: discrete time, absorbing boundary at 0,
a reserve cap, additive inflow/outflow, and the objective `P(absorb before T)` with terminal
condition `Φ(x) = 1{x>0}` under a common discount factor. Under those the two backward
recursions are the same operator iteration and VoLL and `∂V/∂x` are the same Lagrange
multiplier on the same reserve constraint; the proof is a three-line finite-horizon backward
induction. Three of the five conditions fail as each field normally practises it: the grid
minimises EENS, a *magnitude*, not a probability (coinciding only under constant severity or
`VoLL → ∞`); the bird's predation cost is a state-dependent killing rate, an interior
absorption that is not a boundary crossing and has no grid analogue; and a non-indicator
terminal fitness makes the bird's value function not a probability at all. Grid LOLP is
shown to be the bird's `S` under a fixed policy (the evaluation half of the same DP), which
repairs the "no control" objection rather than breaking anything. C33's §1 claim is
re-scoped, not retracted; none of C33's arithmetic changes.

Second finding, new: **both fields are solving the Cramér–Lundberg ruin problem and neither
cites it.** OpenCitations, run 2026-09-05 by `vault/_scripts/c37_identity.py cites`, 8 blank
`citing` records dropped: Asmussen & Albrecher, *Ruin Probabilities* 2nd ed. (DOI
`10.1142/7431`, N = 515) shares **zero** citers with Billinton & Allan 1996 (N = 2,058),
with McNamara & Houston 1987 (N = 422) and with Houston & McNamara 1993 (N = 196). The two
anchor `N` reproduce C33's exactly. Eight web formulations returned no source stating the
identity; the nearest grid-side approach (Deulkar, Nair & Kulkarni, arXiv:1904.04771, 2019)
reaches the same object as a Markov-modulated fluid queue with no ruin-theory language.
Honest limit, stated in C37 §5: the test cannot distinguish "did not know" from "cited
Feller instead".

## 2. Line for `vault/00-index.md`, computed block, after the `C36-conservation-duane` line


- [[C37-lolp-starvation-identity]] — **the LOLP–starvation identity, made precise and then broken in three places.** Under five stated conditions the storage-constrained loss-of-load recursion and the small-bird starvation recursion are the same operator iteration, and VoLL and `∂V/∂x` are the same multiplier on the same reserve constraint. Grid LOLP is the bird's `S` under a fixed policy. But the grid minimises EENS (a magnitude) not a probability, the bird's predation hazard is an interior killing rate with no grid analogue, and a non-indicator terminal fitness makes the bird's value function not a probability — so exact on a restricted pair, structural-only on the pair the fields actually solve. Both are Cramér–Lundberg ruin problems; Asmussen & Albrecher (N = 515) shares 0 citers with all three anchors


## [2026-09-05] computed | The parid's 2-4x reserve margin replicates across 8 species and is a
## demand-side artifact, not a supply-side one

C33 s4 computed a dusk-reserve/overnight-draw margin of +57.1% (typical night) and +31.0% (cold
night) for a 10-13 g parid from Brodin, Nilsson & Nord 2017, and showed it collapsing to
+10.0%/-8.3% with nocturnal hypothermia removed. It asked whether that 2-4x over the grid's
15-20% planning reserve margin was a blue-tit artifact.

C38 recomputes the identical division for every other system with published numbers.
VERDICT: not an artifact, but the headline phrasing was wrong. The biological range is
-74% to +2400%, three orders wide -- wider than any grid band -- and the sorting variable is
the demand-side lever, not the taxon.

  lever ENGAGED:  rufous hummingbird torpid +2421%, bat (Hranac medians) +383%, rufous
                  normothermic +354%, deer mouse warm-acclimated +265%, bat selected roost
                  +99%, bat mean microclimate +75%, parid +57%
  NERC 2025 LTRA design band, 15 of 15 assessment areas:  7.0% - 26.3%
  lever WITHDRAWN or DEGRADED: parid normothermic +10%/-8.3%, cold-acclimated deer mouse
                  +1.5%, bat in worst available microclimate -2.8%, bat under WNS -27%
  NO LEVER AT ALL: common shrew -38% to -74% -- Sorex cannot hold a 16 h winter night on
                  stored energy at any dusk fat load, and forages through it instead

Every animal above the NERC band is exercising a lever; every animal that falls into or below
the band is the SAME KIND of animal with the lever off. C33's mechanism claim, inferred from one
species by switching one parameter, replicates with the switch thrown by nature.

Grid rows are VERIFIED-PRIMARY from NERC, 2025 Long-Term Reliability Assessment, "Summary of
Planning Reserve Margins and Reference Margin Levels by Assessment Area", pp. 175-176, PDF
fetched from nerc.com 2026-09-05 and text-extracted.

TWO CITATIONS IN THE BRIEF WERE WRONG AND ARE CORRECTED IN C38 s6, both Crossref-verified
2026-09-05 (mailto=deciduusleaf@gmail.com):
  - "Shankar 2020 J. Avian Biol., Hummingbirds budget energy flexibly" conflates two papers.
    "Hummingbirds budget energy flexibly in response to changing resources" is Funct. Ecol.
    33:1904-1916 (2019), 10.1111/1365-2435.13404. The J. Avian Biol. 51 (2020) paper is
    "Hummingbird torpor in context", 10.1111/jav.02305.
  - "Hiebert 1993 Physiol. Zool." is The Auk 110:787-797, 10.2307/4088634.
Lehikoinen 1987 10.2307/3676769, Humphries 2002 10.1038/nature00828 and Geiser & Ruf 1995
10.1086/physzool.68.6.30163788 were all verified exactly as the brief gave them.

TWO PUBLISHED SOURCES CONTRADICT THEMSELVES; C38 uses one side and flags both. Eberts 2019
Table 1 heads its column "kJ" while its own footnote and Results give J (J is correct).
Ruf & Geiser 2015's Results text ("~40%/~30%/~6%") disagrees with its own Table 2
(35.3%/18.8%/4.3%); Table 2 is used.

THE LARGEST HOLE, stated in C38 s6: the great-tit/willow-tit leg failed completely. Haftorn
1992, Lehikoinen 1987, Gosler 1996, both Bednekoff & Houston 1994 papers and Houston & McNamara
1993 are all paywalled at JSTOR and none was read. The species C33's falsifier is written
against is the species this replication could not reach. Humphries 2002 is paywalled and
file-restricted at its green-OA record, so the hibernator rows are built on Haase 2019
(10.1371/journal.pone.0222311) and Hranac 2021 (10.1002/ece3.7641) instead, named as a
substitution.

Arithmetic: vault/_scripts/c38_margins.py, no network, every input a transcribed literal.
G34 and C33 were NOT edited by this leg.


## 2. Paste into `vault/00-index.md`, in the `## Computed` block, after the `C33` line


- [[C38-reserve-margin-across-species]] — **replication of C33's reserve margin across 8 species: not a blue-tit artifact, but the headline was wrong.** The biological range is −74% to +2400%, three orders wide and wider than any grid band, and the sorting variable is the demand-side lever, not the taxon. Lever engaged: rufous hummingbird +2421% torpid / +354% normothermic, little brown bat +383% (Hranac medians) and +75–99% (Haase), deer mouse +265%, parid +57%. NERC 2025 LTRA design band across all 15 assessment areas: 7.0–26.3%. Lever withdrawn or degraded, all falling into or below that band: parid normothermic +10%/−8.3%, cold-acclimated deer mouse +1.5%, bat in the worst available microclimate −2.8%, bat under white-nose syndrome −27%. No lever at all — the common shrew — −38% to −74%, structurally unable to hold a 16 h winter night. C33's demand-side mechanism replicates with the switch thrown by nature instead of by a parameter. The great-tit leg failed entirely: every gram-level parid dusk/dawn table is paywalled at JSTOR


## 3. Reciprocation deliberately NOT done

`G34-lolp-starvation-risk`'s `computed-in:` still lists only `[[C33-lolp-starvation]]`. C38 is a
replication of C33 §4, not a second closure of G34, and the brief forbade editing G34. If the
merger judges that C38 should also be an edge on G34, that is a separate decision — make it
explicitly and log it, do not fold it into this paste.


## [2026-09-05] correction | G34: LOLE is not a first-passage quantity; title and thesis corrected
The gap was titled "...are the same first-passage problem". On the bird side 0 is absorbing and
P(starve) is a first-passage probability; on the grid side 0 is NOT absorbing — load is shed, the
shortfall ends, storage recharges — so LOLE = Sum_t P(x(t)<=0)*dt is an expected occupation time
counting repeated crossings. Those are different functionals of the same process. What the two
fields share is the state recursion and the shadow price, not the estimand. C33 sec 1's clause
"only the aggregation differs, and the aggregation is a reporting convention" is withdrawn. The
error was visible in C33's own sec 5.5 ("terminal vs restorable") and in table B's saturation for
Ireland, and was not carried into sec 1 or the title. Produced by adversarial review,
audits/g34-adversarial.md attack 3.

## [2026-09-05] correction | C33: simulated policy is not the paper's optimal policy; daily gain overshoots by 2.3x
C33 sec 3 computed P(starve) = 8.25e-8 "under the policy the paper reports as optimal under almost
all conditions — forage intensively every daylight period". Brodin et al. 2017 attaches that
qualifier to hypothermia alone; on foraging it reports a switch to cautious foraging (behaviour 2,
alpha = 60 kJ) after noon. The paper states its own outcome: total daily fat gain 0.74 g = 27.4 kJ
at the model's 37 kJ/g. C33's budget gives 76.80 - 15.0 = 61.8 kJ = 1.67 g, a 2.3x overshoot. The
five-order-of-magnitude LOLE separation in sec 3 is therefore substantially a policy artifact.
Source: Europe PMC PMC5596050 full text fetched 2026-09-05.

## [2026-09-05] correction | C33: warming-up cost C_WU omitted; hypothermia lever overstated ~4x
Brodin Table 2 gives C_WU = "0 or 6 kJ" and the paper reports both treatments (Fig. 3a, dashed vs
solid). C33's sec 2 parameter table omits C_WU and its 21.0 kJ hypothermic overnight draw is the
C_WU = 0 branch. Charging 6 kJ gives 27.0 kJ against 30.0 kJ normothermic — the hypothermia lever
saves 3 kJ, not 9. The paper's own stabilised cycle corroborates ~27.4 kJ (0.74 g/day). The
demand-side claim in sec 4 falls from a 47-point lever (57% -> 10%) to ~12 points (22% -> 10%).
The omitted branch was the one that flattered the note.

## [2026-09-05] correction | C33: +57% reserve margin compares an energy ratio against a capacity ratio
Planning reserve margin is (firm capacity - peak load)/peak load, MW/MW at one annual instant. The
bird's (x_dusk - R)/R is kJ/kJ over a 16-hour integral. The like-for-like grid quantity is the
energy margin over the critical period (stored energy entering the net-peak window over the energy
discharged across it); for 4-hour storage sized to a 4-hour net peak that is ~0-0.25. On the
paper's own budget the bird's margin is 12/27.4 = +43.8%, so the honest statement is ~0.44 against
~0-0.25, roughly 2x — and PRM should not be named. Note also that the margin is algebraically just
x_start / R: the whole sec 4 prediction is one ratio of two model parameters.

## [2026-09-05] method | G34's citation-intersection anchors measure a literature G34's own scope excludes
All four cross-domain pairings in G34 are anchored on Billinton & Allan 1996 and Billinton & Li
1994 — classic LOLP, a capacity-outage probability table convolved against a load-duration curve,
with no integrated state and therefore no reserve. G34's own "What survives" section says the
comparison must be to storage-constrained adequacy, not to that. The concession was never carried
into the measurement. The in-scope zero exists and is already measured — Denholm & Hand 2011 x
Houston & McNamara 1993, N_A 794, N_B 196, intersection 0, audits/scout-06-energy-systems.md
candidate #3 — but is imported rather than run inside G34 with its own decade bins.

## [2026-09-05] verification | G34's analogy is not prior art; bio-inspired power systems contact is word-level only
Europe PMC, 12 two-phrase conjunctions plus 3 calibration controls, and 4 WebSearch formulations,
all 2026-09-05. No source states the reserve-margin/fat or LOLP/starvation identity. The
prediction that bio-inspired power-systems work would prove to be swarm/metaheuristic is confirmed
by name: all 8 hits on '"loss of load probability" AND "bird"' are optimisation algorithms named
after birds (black-winged kite, honey badger); the 3 hits on '"loss of load expectation" AND
"foraging"' are metaheuristic sizing papers. Grade on the analogy: not REDISCOVERED, not merely
LOCATED. Instruments were degraded — Semantic Scholar returned HTTP 429 on 12 queries and OpenAlex
returned an exhausted daily budget — so the C5 sec 11 bar (>=8 formulations, >=2 working indices)
is NOT met on the engineering side and an IEEE-side sweep is still owed.

## [2026-09-05] method | Europe PMC FULL_TEXT: field prefix silently returns 0 — a fake-zero trap
The first prior-art pass used FULL_TEXT:"..." AND FULL_TEXT:"..." on
https://www.ebi.ac.uk/europepmc/webservices/rest/search and returned 0 on all ten queries,
including FULL_TEXT:"fat reserves" alone, which cannot be zero. The endpoint does not honour that
field prefix and returns 0 for everything. Bare-quoted phrases work ('"fat reserves"' -> 3,992).
This is failure-modes mode 1 (a field/punctuation artifact, not a synonym problem) and it would
have manufactured ten clean confident zeros. Candidate for the homographs/failure-modes register.

## [2026-09-05] correction | C33: the demand-side reading is borrowed grid -> bird, not bird -> grid
C33 sec 4 calls "the bird buys most of its adequacy on the demand side" the transferable claim.
Demand response counted as capacity toward resource adequacy is mature grid practice (MISO Demand
Response 101, 2024; PJM capacity auction; "negawatt" since Lovins 1989). The concept runs grid ->
bird. What is new is the quantity — no published figure exists for the demand-side share of an
animal's adequacy margin — and that quantity is currently uncertain by a factor of ~4 (see the
C_WU entry above).


---

## Exact replacement sentences

Reproduced verbatim from `audits/g34-adversarial.md` § *Proposed edits to G34 and C33*. Apply
there; nothing in this file is a vault edit.

### G34

**H1.** `# Loss-of-load probability and starvation risk are the same first-passage problem`
→ `# Loss-of-load probability and starvation risk are the same reserve recursion, read out by different functionals`

**Blockquote, first sentence.** Replace `Power-system reliability engineering asks *what is the
probability that a stored reserve hits zero before the horizon ends, given stochastic income and a
stochastic draw* and calls the answer **loss-of-load probability**.` with:

> Power-system reliability engineering propagates a stored reserve under stochastic income and a
> stochastic draw and reports **how much time the reserve spends at or below zero** — loss-of-load
> probability and its aggregate, loss-of-load expectation. Behavioural ecology propagates the same
> state under the same drivers and reports **whether an overwintering bird's fat reserve ever
> reaches zero** — starvation probability. **The state recursion is shared and the shadow price is
> shared; the estimand is not.** The grid's zero is a reflecting boundary and its statistic is an
> expected occupation time; the bird's zero is absorbing and its statistic is a first-passage
> probability.

**Frontmatter `note:`.** Replace with:

> `note: "Power-system adequacy and small-bird winter energetics propagate the same stochastic reserve recursion by backward SDP and read the same shadow price off the value function, but aggregate it into different functionals (occupation time vs first passage). Storage-constrained anchor pairing (Denholm & Hand 2011 x Houston & McNamara 1993) intersection 0 at 794 x 196; classic-LOLP anchors also 0 but are out of the claimed scope; same-side controls 25.2% and 12.8% of the smaller set."`

**After the provenance table.** Insert:

> **Anchor scope, stated against this note's own restriction.** The four Billinton pairings above
> measure the **classic-LOLP** literature, which *"What survives"* below explicitly places outside
> this note's scope. They are retained as an out-of-scope control. **The in-scope measurement is
> the storage-constrained pairing, Denholm & Hand 2011 × Houston & McNamara 1993, `N_A` 794,
> `N_B` 196, ∩ = 0** (`audits/scout-06-energy-systems.md` candidate #3, OpenCitations 2026-09-05).
> Until that pairing is re-run inside this note with its own decade bins, the in-scope zero is
> imported, not measured here.

**End of "What survives".** Append:

> **A second scope restriction, from `audits/g34-adversarial.md`.** Even under storage-constrained
> scoping, **LOLE is not a first-passage quantity**: unserved load is shed and the reserve
> recovers, so the grid's zero is not absorbing and LOLE counts repeated crossings. The bird's
> `P(starve)` is a first-passage probability on an absorbing boundary. **What the two fields share
> is the state recursion and the shadow price, not the estimand.** The claim is corrected to that,
> and the word "first-passage" is removed from the grid side throughout.

### C33

**§1.** Replace `Same functional equation, same absorbing boundary, same backward sweep — only the
aggregation differs, and the aggregation is a reporting convention.` with:

> Same state recursion, same backward sweep — **and there the identity stops.** The bird's zero is
> absorbing and `P(starve)` is a first-passage probability. **The grid's zero is not absorbing**:
> load is shed, the shortfall ends, and storage recharges, so `LOLE` is an expected **occupation
> time** of a non-absorbing process, counting repeated crossings. First-passage probability and
> expected occupation time are different functionals of the same process and they diverge exactly
> where the risk is interesting — a system that dips below zero ten times for an hour each has
> LOLE 10 h and would have died at the first dip. **The aggregation is not a reporting
> convention; it is the difference between the two estimands.**

**§1, displayed recursion.** `0 absorbing` → `0 absorbing on the bird side only; reflecting on the
grid side`.

**§2, parameter table.** Add row:

> `| C_WU | extra warming-up cost, hypothermic bird | **0 or 6 kJ** — the paper reports both | Table 2, Eq. 10 |`

**§2, derived budget.** Replace `Overnight draw \`45 × 16/24 × 0.7\` = **21.0 kJ** hypothermic
(25.2 cold)` with:

> Overnight draw, `C_WU = 0`: `45 × 16/24 × 0.7` = **21.0 kJ** hypothermic (25.2 cold). **With the
> paper's other treatment, `C_WU = 6 kJ`: 27.0 kJ hypothermic (31.2 cold)** — against 30.0 kJ
> normothermic, so the hypothermia lever saves **3 kJ, not 9**. **The paper's own stabilised cycle
> independently puts the overnight draw at ≈27.4 kJ**: it reports a total daily fat gain of
> **0.74 g**, which at the model's 37 kJ/g is 27.4 kJ, and in a stabilised cycle the night's draw
> equals the day's gain. **Every number below that uses 21.0 kJ is the low-draw branch, and it is
> the branch that flatters this note.**

**§3, policy sentence.** Replace `under the policy the paper reports as optimal under almost all
conditions — forage intensively every daylight period, maximum hypothermia every night` with:

> under **maximum foraging** — forage intensively every daylight period, maximum hypothermia every
> night. **This is not the paper's optimal policy and the note previously mis-described it as
> such.** The paper's "under almost all conditions" qualifier attaches to hypothermia alone; on
> foraging it reports the bird switching to cautious foraging (behaviour 2, α = 60 kJ) after noon
> once dusk fat is within reach. **The consequence is measurable: this note's budget gives 61.8 kJ
> (1.67 g) of net daily fat gain against the paper's own reported 0.74 g — a 2.3× overshoot. The
> `8.25 × 10⁻⁸` is therefore an upper bound on safety, and the five-decade separation in §3 is
> substantially an artifact of the policy, not a property of the bird.** Re-running under the
> mixed behaviour-1/behaviour-2 policy is the outstanding fix.

**§3, table B heading.** `### B. Grid criterion → bird units` →
`### B. Grid criterion → bird units — illustrative only, not a result`, and prepend:

> **This direction converts an expected occupation time into a first-passage probability, and
> those are different functionals (§1).** The saturation for Ireland is the symptom, not a
> curiosity. The table is retained to show the scale, and **no claim in this note rests on it.**

**§4, comparator.** Replace `roughly **two to four times** the 15–20% grid convention (ESIG 2024:
WECC-CAMX PRM ≥ 15%, mainland Spain ≥ 10%)` with:

> **and the grid's planning reserve margin is the wrong comparator for it.** PRM is
> `(firm capacity − peak load)/peak load`, **MW/MW at a single annual instant**; the bird's ratio
> is **kJ/kJ over a 16-hour integral**. Both are dimensionless and they are not the same
> dimensionless number. **The like-for-like quantity is the energy margin over the critical
> period** — stored energy entering the net-peak window over the energy discharged across it,
> equivalently residual state of charge at the end of the critical period as a fraction of that
> period's energy. For the 4-hour storage fleets that dominate current accreditation, sized to a
> 4-hour net peak, that margin is **≈0–0.25**. On the paper's own budget the bird's margin is
> `12 / 27.4` = **+43.8%** on a typical night (not +57.1%). **The honest statement is: ≈0.44
> against ≈0–0.25, roughly 2×** — and PRM should not be named.

**§4, headline claim.** Replace `**The bird meets a far stricter adequacy standard than any grid
while carrying a supply-side margin that is only modestly larger, because it buys most of its
adequacy on the demand side.** That is the transferable claim.` with:

> **The demand-side reading is the grid's own, not a transfer from the bird.** Demand response
> counted as capacity toward resource adequacy is mature grid practice — MISO's *Demand Response
> 101* (2024), PJM's capacity auction, and "negawatt" as a term since Lovins 1989. **The borrowing
> here runs grid → bird.** What is new is not the concept but the **quantity**: no published
> figure exists for the demand-side share of an animal's adequacy margin. **On the low-draw branch
> that share is large (57% → 10% when hypothermia is removed); on the paper's own budget, with the
> 6 kJ warming cost charged, it is 22% → 10% — a 12-point lever, not a 47-point one.** The claim
> is the existence and rough size of the quantity, and its size is currently uncertain by a factor
> of four.

**§4, falsifier.** Append:

> **The second falsifier is not yet tested even in-model.** The normothermic rows above are a
> counterfactual inside one parameterisation — `x_dusk` held at its `ε = 30%` optimum with `ε`
> switched off. A bird that genuinely cannot use hypothermia would **re-optimise `x_dusk` upward**,
> which is what the DP exists to compute. Re-running Brodin's DP at `ε = 0` and reading the new
> optimal dusk reserve is a small job and is the minimum before the demand-side mechanism is
> claimed.

**§5.** Append items 8 and 9:

> 8. **Species label vs parameter source.** The paper labels its animal a non-hoarding parid,
>    "such as a blue tit", but states that **"the parameter values are taken from data on willow
>    tits"** and flags that blue tits "may not be as cold-adapted". The willow tit is additionally
>    **a large-scale hoarder**, and the model deliberately excludes caching. A cache is a second
>    reserve invisible to a fat-only formalism, so the margins here are a **lower bound** for any
>    hoarding species — and the grid analogue, off-book contracted firm imports, is exactly what
>    PRM accounting argues about.
> 9. **Prior-art instruments were degraded on 2026-09-05.** The adversarial prior-art sweep behind
>    these corrections ran on **Europe PMC + WebSearch only**: Semantic Scholar returned HTTP 429
>    on 12 queries and OpenAlex returned an exhausted daily budget. No source states the analogy in
>    what was reachable, but the C5 §11 bar (≥8 formulations across ≥2 working indices) is **not**
>    met on the engineering side.

---

## Not proposed, and why

- **No `standing:` change.** The gap survives as a narrowed claim; `live` is still correct and
  nothing here meets the bar in `failure-modes` for `overturned`.
- **No `crosses:` change.** `formalism` (rank 4) still holds: the shared object is the state
  recursion plus the shadow price, which is a formalism-level correspondence. The estimand
  difference narrows what is shared; it does not drop it to `vocabulary`.
- **No edit to `vault/_scripts/c33_lolp.py`.** The policy and `C_WU` faults are in the script, but
  fixing them is a recomputation, not a text edit, and the recomputed numbers should land in C33
  in one motion rather than as a sequence of partial corrections.


## [2026-09-05] verification | G34's zero survives a second index and a 4x4 decade grid - but Semantic Scholar's power-side control fails


G34 was single-provider (OpenCitations only), four pairings, both grid anchors 1990s books, no
scoped `N`. OpenAlex was tried first and refused (HTTP 429, `Insufficient budget … Resets at
midnight UTC`, 2026-09-05), so Semantic Scholar's Graph API was used instead. Anchors were
widened to four per side, one per decade: grid 1978 / 1994 / 2011 / 2020, bird 1987 / 1993 /
2006 / 2017. **All sixteen cross-domain pairings return 0**, on `paperId` and independently on
normalised DOI. Pooling the anchors: 2,713 distinct grid citers, 906 distinct bird citers, and
**not one work in both**. The 1980s bin, which the previous revision had to declare
uninformative because no citer of a 1994 book can predate 1994, is now populated on both sides
(19 grid citers vs 34 bird citers) and is still zero — so the honest window widens from
1994-onwards to **1978-onwards** and [[failure-modes]] mode 6 is answered rather than deferred.
`N_universe` was estimated at **44,299** from Semantic Scholar `paper/search/bulk` (documented
phrase query, `year=1987-2026`), giving pooled `E = 55.5` and `E = 5.55` at 10x, so the zero is
a finding across two orders of magnitude of denominator. **The caveat is the load-bearing part:
four of six Semantic Scholar power-side positive controls return zero**, including two
storage-adequacy papers nine years apart where contact is certain. Diagnosed by pulling twelve
citers' reference lists — seven have no reference list in that index at all. So Semantic Scholar
*corroborates* the zero and calibrates cleanly on the ecology side (10.8-22.7%), but cannot
establish the grid side alone; the calibration still rests on OpenCitations (25.2% / 12.8%).
Standing unchanged at `live`, contact surface unchanged at 0.


## [2026-09-05] correction | Brodin's wintering-bird energy-management review is 10.1098/rstb.2006.1812, not 10.1098/rstb.2007.2074


The DOI `10.1098/rstb.2007.2074` was carried into this leg's brief as Brodin 2007, *Theoretical
models of adaptive energy management in small wintering birds*. It resolves, on Crossref and on
Semantic Scholar (both 2026-09-05), to *Synthetic Turing protocells: vesicle self-reproduction
through symmetry-breaking instabilities* — an unrelated Phil. Trans. B paper. The correct record
is **`10.1098/rstb.2006.1812`**, Phil. Trans. R. Soc. B, issued 2006-04-19, Crossref
`is-referenced-by-count` 106, fetched 2026-09-05. Nothing in the vault had yet been built on the
wrong DOI; it is logged because a plausible-looking DOI that resolves to a real paper in the
right journal is exactly the failure this project's numbers rule exists to catch.

## 2. Addition for `vault/method/citation-sources.md`

Two provider facts worth recording alongside the existing endpoint traps:

- **OpenAlex is now metered.** Anonymous and `mailto:` requests can return HTTP 429 with
  `{"error":"Rate limit exceeded","message":"Insufficient budget … Resets at midnight UTC"}`.
  This is a *budget* exhaustion, not a per-second throttle — retrying with backoff never
  succeeds. Plan for OpenAlex to be unavailable for a whole session and have a second provider
  ready.
- **Semantic Scholar has two rate-limit pools, and `/paper/search` is the strict one.**
  `/paper/DOI:<doi>`, `/citations` and `/references` sustain roughly 1 request per 1.5 s
  unauthenticated; `/paper/search` returned 429 through seven exponential backoffs up to 72 s.
  Use **`/paper/search/bulk`** instead — it accepts boolean phrase syntax (`"a" | "b"`,
  `"a" + "b"`), respects `year=`, returns an exact `total`, and shares the permissive pool.
- **Semantic Scholar's reference-list coverage of recent power engineering is thin.** Of twelve
  citers of a 2020 IEEE capacity-value paper, seven had no reference list at all. Any zero this
  provider reports on an engineering literature needs its own same-side positive control before
  it is read as absence. See the worked failure in
  [[G34-lolp-starvation-risk]]'s provenance block.

## 3. `00-index.md`

No standing change, so no index edit is required. G34 stays `live`, `contact-surface: 0`,
`evidence: citation-intersection`.


## [2026-09-05] method | Citation toolkit: six providers behind one interface, so no single rate limit blocks a round
## [2026-09-05] correction | Semantic Scholar is NOT "429 unauthenticated" - that reading was a shared-pool spike, not a property
## [2026-09-05] verification | Scheffer 2009 x Si 2011 = 1 confirmed on a second provider (Semantic Scholar), same hit DOI


**Entry 1.** `vault/_scripts/providers/` now holds one stdlib-only adapter per provider behind a
common `citers(doi) -> set` interface — `opencitations`, `openalex`, `semanticscholar`,
`europepmc`, `lens` (token-gated), `scopus` (documented stub). `intersect.py` gains
`--providers=a,b`, `--all` (per-provider table plus a consensus min/max line) and
`--list-providers`. The default single-provider behaviour, the blank-key filter, `--enrich`,
`--json` and `--selftest` are unchanged, and `--selftest` reproduces the audit's
3,934 / 1,783 / **1** exactly. Every adapter **raises** rather than returning an empty set when a
provider cannot see an anchor, because a failed fetch and a zero intersection are different
facts and the project has already had to correct one for the other.

**Entry 2.** `citation-sources.md` recorded "Semantic Scholar — 429 unauthenticated" from a
2026-09-03 burst. Paced at ~1.1 s, Semantic Scholar enumerated 4,605 citer records for Scheffer
2009 and 2,095 for Si 2011 with no key at all, 2026-09-05. The old row measured a *shared* pool
under contention and wrote it down as a property of the provider — the same error shape as the
"OpenAlex budget-locked" claim in three gap notes that had expired by the next probe. The table
row is corrected and the correction is stated in place rather than the old row being deleted.

**Entry 3.** `audits/07-provenance-rounds3-6.md` re-derived G29's Scheffer × Si intersection of
**1** from OpenCitations. Semantic Scholar, independently assembled, returns the same
intersection of 1 and **the same hit DOI** `10.1007/s42524-021-0176-y`, from N_A 3,957 / N_B
1,891 against OpenCitations' 3,934 / 1,783. Two providers, 1% and 6% apart on N, identical hit.

## 2. Numbers a G34 agent may want

Billinton & Allan 1996 (`10.1007/978-1-4899-1860-4`) × McNamara & Houston 1987
(`10.2307/1939235`), OpenCitations `api.opencitations.net/index/v1/citations/<doi>`,
fetched **2026-09-05**:

| | N_A | N_B | ∩ | blanks dropped |
|---|---|---|---|---|
| opencitations | 2,058 | 422 | **0** | 1 |

**One provider only.** OpenAlex was budget-exhausted (`retryAfter` 47,052 s); Semantic Scholar
and Europe PMC both fail to index the Billinton & Allan book DOI. Union floor `N = 2,480` gives
`E = 350`, so the zero is not trivially explained by a small universe — **but a field-scale `N`
is still owed** before `O/E` is quotable, per `citation-intersection.md`, and a single-provider
zero should be re-run against OpenAlex after the daily budget resets at midnight UTC.

**Do not substitute Semantic Scholar's Billinton & Allan.** S2 holds
`10.1007/978-1-4615-7731-7` — the **1984 first edition**, 3,001 citations — which is a different
work with a different citer set.

## 3. Not done, deliberately

- **No `00-index.md` link for this file**, per the same convention as `PENDING-log-C37`. Lint
  reports it as a warning, not an error.
- **No Lens or Scopus token fabricated.** Both adapters are gated and say what the owner must do.
- **Scopus/WoS left as a stub.** Both bind entitlement to an institutional IP range, so an
  adapter written off-campus cannot be tested, and an untested one that swallowed an auth failure
  into an empty set would write a false zero. The exact citing-works endpoints and env var names
  are in `vault/_scripts/providers/scopus.py` and in `citation-sources.md`.
- **No gap or computed note touched.**

## [2026-09-05] honest null | C33: the positive control FAILS - Brodin's 0.74 g/day is not reproducible from the open text
The adversarial review's highest-value item was to re-run the forward propagation under the
paper's own mixed foraging policy with C_WU = 6 kJ and check it against Brodin, Nilsson & Nord
2017's own stated total daily fat gain of 0.74 g. Run: it does not reproduce, and it cannot. The
paper says the bird "should keep on foraging all daylight hours until dusk", switching between
behaviour 1 (alpha = 80 kJ) and behaviour 2 (alpha = 60 kJ) after noon. Every mixture of those two
has a floor of 60 x 0.96 - 15.0 = 42.60 kJ = 1.15 g/day, still 1.56x the paper's own 0.74 g. The
policy C33 rev.1 actually simulated (behaviour 1 all day) gives 61.80 kJ = 1.67 g = 2.26x. The
missing parameters are named in the paper but not given: the mass-dependent foraging metabolism
(Table 1 fn a) and the mass-dependent gain ceiling ("up to 1 g of fat"). C33 rev.2 therefore FITS
a single effective alpha_eff = 44.15 kJ/day to the paper's 0.74 g/day and labels it a fit
everywhere. Source: Europe PMC PMC5596050 full text, re-read 2026-09-05.

## [2026-09-05] correction | C33: P(starve) withdrawn - an open-loop propagation cannot estimate a state-dependent DP's first passage
Under the calibrated policy the 100-night starvation probability is 0.9992; under the rev.1
max-foraging policy with C_WU = 6 kJ charged it is 2.31e-5 (rev.1 printed 8.25e-8 with C_WU = 0).
The bracket spans the whole probability scale, so the estimator is uninformative, and the reason
is structural: Brodin's bird runs a state-dependent optimal policy from the backward DP - it
forages harder when its reserve is low - and no fixed-gain forward propagation can represent that
feedback. C33's P(starve) = 8.25e-8 and LOLE = 6.6e-7 h/winter are WITHDRAWN with no replacement
number, and so is the "five orders of magnitude safer than the grid" headline. The paper's own
published figures are the quotable ones and they bound everything: winter survival 0.71 with
hypothermia and 0.13 without (Results, Fig. 2), i.e. P(die) = 0.29 all causes, so P(starve) <=
0.29 = 3.4e-3 per night. The withdrawn 8.25e-8 sat 6.5 orders below the paper's own ceiling,
which alone rejects it. This is one step worse than PENDING-log-G34ADV expected: that file
predicted the numbers could be reissued with a tolerance after a re-run. They cannot.

## [2026-09-05] correction | C33: the two-way LOLE <-> P(starve) table is withdrawn, both directions
Rev.1 converted between the two using an invented 8-hour "mean remaining night" charge. LOLE is an
expected occupation time of a non-absorbing process; P(starve) is a first-passage probability on
an absorbing one. The 8-hour charge does not make them one object, and the saturation of the
Ireland row was the symptom rather than a curiosity. No like-for-like replacement was found: a
per-period first-passage probability for a storage-constrained adequacy study was searched for and
not located this session. The union bound P(first hit 0 within a year) <= LOLE = 0.1 d/yr bounds
the grid from ABOVE only and therefore cannot order the two systems in either direction. Stated as
a null.

## [2026-09-05] correction | C33: reserve margin restated like-for-like as an energy margin; +57.1% -> +43.8%
Planning reserve margin is (firm capacity - peak load)/peak load, MW/MW at one annual instant; the
bird's ratio is kJ/kJ over a 16-hour integral. The like-for-like quantity is the energy margin over
the critical period. On the paper's own budget the bird's margin is x_start/R = 12/27.4 = +43.8%,
against ~0% for a 4-hour lithium fleet sized to a 4-hour net peak - roughly 2x, not "two to four
times the 15-20% convention", and PRM is no longer named. NERC's 7.0-26.3% band (2025 LTRA
pp. 175-176) is retained as a CAPACITY quantity for context only. With C_WU = 6 kJ charged the
hypothermia lever is +12.2 points (22.2% -> 10.0%), not +47.1 (57.1% -> 10.0%); the cold-night
margin falls from +31.0% to +5.8%. Better still, the paper reports the lever in its own currency:
winter survival 0.13 -> 0.71, a 58-point published lever that C33 should have quoted from the
start.

## [2026-09-05] method | c33_lolp.py compute rewritten: four policies, C_WU charged, positive control as section 0
The script's compute half now (i) prints the positive control FIRST and states pass/fail, (ii)
carries ALPHA1 and ALPHA2 separately and a C_WU constant defaulting to 6 kJ charged in the first
daylight period after a hypothermic night, (iii) runs four labelled daylight policies including a
CALIBRATED one, (iv) prints the paper's own 0.13/0.71 survival as the ceiling on everything it
computes, and (v) ends with an explicit null on the grid-side first-passage number. One unresolved
ambiguity is now printed rather than hidden: Brodin's Eq. 7 writes the unsuccessful-period gain as
Delta*G_i*delta, i.e. gain reduced TO 20%, while Table 2's wording is "reduced energy gain
unsuccessful foraging 20%", i.e. reduced BY 20%. The script takes the second reading; the two
differ by 12% on realised daily gain and the calibration absorbs the difference.

## [2026-09-05] vocabulary | G34 standing live -> narrowed
The gap's H1 claimed the two fields solve "the same first-passage problem". They do not: the
grid's zero is reflecting and its statistic is an expected occupation time. The title, the
blockquote and the frontmatter note are rewritten to "the same reserve recursion, read out by
different functionals", the four Billinton anchors are demoted to an out-of-scope classic-LOLP
control with the in-scope Denholm & Hand 2011 x Houston & McNamara 1993 zero (794 x 196, 0) stated
in their place, and the computation leg's withdrawn numbers are carried into "What survives".
PENDING-log-G34ADV proposed NO standing change on the grounds that the gap survives as a narrowed
claim; that is exactly what `narrowed` is for in this vault's vocabulary, and the headline number
being wrong as well as the headline framing puts it over the bar. standing: narrowed, and the
STANDING line in the body with it.

## [2026-09-05] method | G34/C33 graded REPACKAGED, with the two things that are actually new
Added to vault/novelty-audit.md. The dynamic program is ruin theory (Lundberg 1903, Cramer 1930)
in both fields and the demand-side reading is mature grid practice (MISO Demand Response 101 2024,
PJM capacity auction, "negawatt" since Lovins 1989), so the borrowing runs grid -> bird. What is
new: (1) the ruin-parent TRIPLE zero - neither field cites ruin theory and neither cites the
other, the third leg measured across 20 anchor pairings on two providers, 0 in every cell and
decade bin; (2) the cross-species margin/setpoint table in C38 - 19 systems on one energy-margin
axis, sorted by whether the metabolic setpoint is movable and currently moved, with no published
figure existing for the demand-side share of an animal's adequacy margin.


---

## What is still owed

1. **Re-run the in-scope intersection inside G34 with its own decade bins** — Denholm & Hand 2011
   × Houston & McNamara 1993 and × McNamara & Houston 1987, OpenCitations, same blank-key filter
   and mode-6 binning as the Billinton rows. The zero is currently imported from
   `audits/scout-06-energy-systems.md` candidate #3.
2. **Re-run Brodin's backward DP itself**, not a forward propagation under a fixed policy. That is
   the only instrument that can produce a defensible `P(starve)` for this model, and it is also the
   only version of C33's second falsifier the formalism can answer (re-optimise `x_dusk` at
   `ε = 0`).
3. **A cited duration-dependent ELCC or storage-adequacy study** reporting either a per-period
   first-passage statistic or an energy margin over the critical period. Both grid-side numbers in
   C33 §4 (`≈0%`) are reasoned from duration matching, not fetched.
4. **Repeat the prior-art sweep on a power-engineering index.** Europe PMC + WebSearch only is one
   instrument short of the C5 §11 bar, and the NOVEL-on-the-analogy finding rests on it.


## [2026-09-05] method | C36's governance ordering re-coded blind: direction survives, test declared underpowered by its own pre-registration

C36 §5 grouped management programmes as "statutory" vs "RFMO/weak" *after* seeing their
Crow-AMSAA beta, and said so. C39 redoes the coding blind: a three-component rule (mandated
assessment cycle / assessment-triggered rebuilding obligation / stated response deadline, 0-1
each) was written into `audits/blind-brief-c39-2026-09-05.md` with the ten-region list and the
prediction, and sha256-hashed (885ffef666798d784ec67260dbf7573a236e81007b893d6a24e3fa8f3d405d3d,
first 4,615 bytes) before `computed/C36-conservation-duane.md` was opened. Regions were then
scored from statute and regulation text only (MSA 16 U.S.C. 1854(e); CFP Reg. 1380/2013;
Fisheries Act ss. 6.1-6.2 and Fishery (General) Regs; GFCM; IOTC; CCAMLR).

Result: Spearman rho = -0.709 on n = 8 joined regions, exact two-sided p = 0.0596 (40,320
permutations enumerated); score-3 mean beta 0.841 vs score-<=1 mean beta 1.234, difference
-0.392, one-sided permutation p = 0.0476 (21 splits). The direction predicted in advance holds.
The brief also pre-declared that either comparison group falling below 3 members makes the test
underpowered, and the score-<=1 group has 2 members - so the pre-registered verdict is
UNDERPOWERED, direction only, and it is recorded as such rather than as a pass. The blind is
partial: the AI coder had prior knowledge of which regions did well, and six beta values appeared
in the instruction that commissioned the work. Melnychuk et al. 2017 PNAS
(10.1073/pnas.1609915114, DOI verified at Crossref 2026-09-05) was checked as an external
pre-registered index; pnas.org returns 403 and no open per-region FMI score table was reached, so
the second external code was not run.


## 2. Line for `vault/00-index.md` (computed notes list, after the C36 line)


- [[C39-duane-governance-blind]] — C36's governance ordering re-coded blind against a pre-hashed rule: rho = −0.709, exact p = 0.0596, n = 8; direction holds, test underpowered by its own pre-registration


## [2026-09-05] verification | the two load-bearing `∩ = 1` rows in G27 are real bridges, not phantoms; `narrowed` stands

The whole reversion of [[G27-collective-decision]] from `overturned` to `narrowed`, and its
`contact-surface: 26 → 1`, rested on two intersections of exactly 1 — the one value the
OpenCitations blank-`citing` artefact manufactures out of nothing. All four G27 pairings re-run on
the filtered script, 2026-09-05: Dorigo × Paxos **0 → 0**, Seeley × Paxos **0 → 0**, Dorigo ×
(Byzantine + FLP) **1 → 1**, Seeley × (Byzantine + FLP) **1 → 1**. Citer-set sizes unchanged on
every anchor (Dorigo 8,814, Seeley 267, Paxos 1,914, Byzantine + FLP 6,735), which establishes
that G27's published figures were already post-filter. The Seeley pairing's single hit reproduces
**on Semantic Scholar as the identical DOI**; the Dorigo pairing errors on S2, which has no record
for `10.1109/3477.484436` — a coverage hole, not a zero. Produced by: `_scripts/intersect.py`,
blanks dropped, 2026-09-05.

## [2026-09-05] verification | ACM TAAS 2012 confirmed to cite both of G27's anchors, from the publisher's own deposit

The bridge was found by a citation index, so it was checked against a second, independent object:
the publisher-deposited reference list. Crossref, 2026-09-05, `10.1145/2168260.2168264` — Saffre &
Simaitis, *Host selection through collective decision*, *ACM Trans. Autonomous and Adaptive
Systems*, April 2012, `reference-count` = 43. Its abstract names both sides ("inspired by
biological swarms", "the emergence of a consensus within a population of agents", host selection
in application migration). Its deposited references contain Seeley & Buhrman 1999
`10.1007/s002650050536` **and** Fischer, Lynch & Paterson 1985 `10.1145/3149.214121`, plus Seeley
2003 `10.1007/s00265-003-0598-z`. **It cites both anchors.** Had it not, G27 would have reverted
to `standing: overturned` with `contact-surface: 0`; it does, so **nothing moves**.

## [2026-09-05] verification | G7's bare OpenCitations 1 is confirmed, and the citer is nuclear

[[G7-how-passive]] quoted a single citer of the TECDOC-626 proxy anchor
`10.3327/jaesj.34.1116` — a bare 1 on a small anchor, the artefact's signature shape. Re-enumerated
on the filtered script, 2026-09-05: the anchor returns **one record and zero blank keys**, so there
was no phantom available to inflate it, and **Semantic Scholar independently returns the same
single citer**. Identified by Crossref: `10.3390/en13112898`, Zeliang et al., *Integral PWR-Type
Small Modular Reactor Developmental Status, Design Characteristics and Passive Features: A
Review*, *Energies* 2020 — a nuclear SMR review, i.e. **inside** the nuclear literature and
consistent with the note's "all 57 citers are nuclear" finding rather than a counterexample to it.
The 1 stands; no standing, tag or `contact-surface` moves.

## [2026-09-05] verification | G25, G28 and G8's intersections all re-derive unchanged; only a set size moves

Three notes re-run, no standing changed in any of them. **[[G25-proofreading-coding]]**: Hopfield
1974 × Shannon 1948 pt II — sets **1,542 → 1,542** (51 blanks dropped) and **9,771 → 9,771** (70
dropped), intersection **8 → 8**, same eight DOIs; already post-filter as published.
**[[G28-marginal-value-gittins]]**: intersection **5 → 5**, the same five DOIs, on the endpoint the
repair also covers (`cited`, reference-list side). Newly recorded there is the *de-blanked base* —
Gittins 1,026 records, 14 blank, **1,012** distinct citers; Charnov 4,115 records, 28 blank,
**4,087** — which shows the Provenance table's OpenCitations 1,026 is an unfiltered server-side
count of the same object the 1,012 enumerates. The control ratio 62.5 is untouched.
**[[G8-energy-per-bit-axis]]**: intersection **35 → 35**, same 35 DOIs, `N_A` **4,292 → 4,292**;
the pooled `N_B` is corrected **3,881 → 3,882** (Laughlin 1,012 + Attwell 3,054), which is one
*low*, so it is a transcription slip and not the phantom — the phantom only ever reads high. The
0.82% / 0.90% percentages are unchanged to two figures and the overturn is untouched. Produced by:
`_scripts/intersect.py`, blanks dropped, 2026-09-05.

## [2026-09-05] correction | G19's OpenCitations citer count was a counted list and reads one high: 40 → 39

[[G19-safety-factor-derived-twice]] tabulated OpenCitations citers of `10.1006/jtbi.1996.0270` at
**40 records counted**, with the `/citation-count/` endpoint "agreeing at 40". Re-enumerated with
blank keys dropped, 2026-09-05: of the 40 records **one carries an empty `citing` field**, so the
distinct citing set is **39**. The two 40s were never independent confirmation — `/citation-count/`
is an *unfiltered* server-side count, so it agrees with the raw record list by construction and
says nothing about the de-blanked set; the note now says so. Semantic Scholar, run as a second
provider, returns **34** after dropping 3 blanks, and is added to the table. Nothing load-bearing
moves: this note's finding is the *composition* of the citing set — comparative biomechanics
throughout — not its cardinality, and the provider spread the note already reports (28–46) simply
widens by one at the OpenCitations row. `standing`, `evidence` and `contact-surface` unchanged.

## [2026-09-05] method | Semantic Scholar's coverage holes are `err` rows, and four of this round's anchors fall in them

Running a second provider was the point of the round, and on four of the six notes it could not
answer. Semantic Scholar has **no record at all** for Dorigo, Maniezzo & Colorni 1996
`10.1109/3477.484436`, Shannon 1948 pt II `10.1002/j.1538-7305.1948.tb00917.x`, Landauer 1961
`10.1147/rd.53.0183`, or Charnov 1976 `10.1016/0040-5809(76)90040-x` — four canonical, heavily
cited works. The adapter raises rather than returning an empty set, `--providers` prints the row as
`err`, and the consensus line excludes it, exactly as `_scripts/intersect.py`'s "a failed fetch is
not a zero" contract requires. **Where a second opinion was obtainable it agreed exactly**: Seeley
× Paxos 0 on both, Seeley × (Byzantine + FLP) 1 on both and on the same DOI, G7's single citer the
same DOI on both. Where it was not, this round's numbers rest on one provider, and with OpenAlex
budget-locked that is a stated limitation of the round, not a silent one. Provider `N` spreads,
where both answered, ran 4–18% — consistent with the 10–25% band in [[citation-sources]].

## [2026-09-05] computed | C38's setpoint prediction pre-registered and run: partial pass, strong half is a proxy

C38 section 5 predicted (i) reserve margin monotone in torpor depth and (ii) lever-less small
endotherms paying in mortality rather than in supply-side reserve, and named Ruf & Geiser 2015
crossed with ring-recovery survival as the test. C40 wrote and sha256-hashed a blind brief
first (audits/blind-brief-c40-2026-09-05.md, sha256 1e2bc903...db5dff over its first 7811
bytes) fixing the ordinal predictor, the <100 g / |lat|>=35 deg / resident-only filter, the
join key, both statistics and the sample-size gates, then fetched outcome data.

Obtained: Ruf & Geiser 2015's per-species Appendix, 214 species with T / BM / Tb_min /
TMR_min / TMR_rel / TBD_max / LAT, open at PMC4351926 - C38 section 5 recorded this appendix
as "not obtained", and that gap is now closed. Also AnAge build 14 and PanTHERIA 1.0 WR05.

T1 (torpor class vs published margin, margins cited from C38 not recomputed): rho = +0.6325,
exact two-sided p = 0.5000, n = 4. Direction as predicted; UNDERPOWERED by the brief's own
gate (n >= 8 and two classes with n >= 3). The pre-fixed migrant filter removed both
hummingbird rows, which are C38's largest margins - the filter was fixed before they counted.

T2 (survival): no open compilation of adult annual phi for small mammals exists. AnAge carries
IMR for 43 of 4645 species and none of the frame. The brief's pre-authorised PROXY (maximum
longevity) was used, flagged PROXY throughout. 75 species, 25 mass- and latitude-matched
pairs, 21/24 in the predicted direction, one-sided sign p = 0.00014. Two sensitivities that
matter more than the headline: drop Chiroptera (bat longevity is bought by flight, not by
torpor) -> 11/15, p = 0.0592; code torpor by the literal brief-source-1 rule -> 11/18,
p = 0.240. T2's p-value is a function of the torpor coding, not of the survival data.

T3 (falsifier scan): 0 lever-less species with a published margin > +100%. NOT FALSIFIED, over
a sample of one - the only lever-less species with a published margin is Sorex araneus.

Blind broken, disclosed: the clade-level torpor coding rule for the 57 species Ruf & Geiser do
not carry at species level was written with the longevity column already on screen. Script
_scripts/c40_setpoint.py; --verify-brief rechecks the hash.


## 2. Index line inserted into `00-index.md` by this run


- [[C40-setpoint-survival-test]] — **C38 §5's setpoint prediction, pre-registered against a
sha256-hashed brief, comes back a partial pass whose strong half is a proxy.** Torpor class vs
published margin: Spearman rho = +0.63, exact p = 0.500, n = 4 — direction as predicted,
UNDERPOWERED by the brief's own gate, and the pre-fixed migrant filter is what cost it the two
hummingbird rows. Survival: no open compilation of adult annual phi for small mammals exists, so
the brief's pre-authorised PROXY (AnAge maximum longevity) was used — 75 species, 25 mass- and
latitude-matched pairs, 21/24 in the predicted direction, one-sided p = 0.00014; drop Chiroptera,
whose longevity is bought by flight, and it is 11/15, p = 0.059; code torpor by the literal
source-1 rule and it is 11/18, p = 0.240. Falsifier scan: **0** lever-less species with a
published margin > +100%, over a sample of one. New asset: Ruf & Geiser 2015's per-species
Appendix (214 species, TMR_rel / Tb_min / TBD_max / latitude), which C38 said was not obtained,
is open at PMC4351926


(The line as inserted is a single unwrapped line; it is wrapped here for readability.)

## 3. What this run did NOT touch

`C38-reserve-margin-across-species.md`, `C33-lolp-starvation.md`, `G34-lolp-starvation-risk.md`
and `log.md` are unmodified. C38's rows are cited, never re-derived or re-graded.


## [2026-09-05] honest null | The C37 "uncited parent" pattern is not general: 3 of 8, not most

C37 found grid adequacy and bird starvation each rebuilding Cramer-Lundberg ruin theory with
neither citing it, and asked whether the project's cross-domain gaps are usually two fields
that both rediscovered an older parent. C41 named a candidate parent for eight confirmed
same-object pairs and measured all three pairwise citer-set intersections (A x B, A x P,
B x P) on OpenCitations and Semantic Scholar, 2026-09-05, script _scripts/c41_parents.py.

Result: 2 class-i (both sides meet the parent), 3 class-ii (one side), 3 class-iii (neither -
the C37 pattern). The hypothesis is NOT supported, and the sample was the most favourable
one available. What survives is a diagnostic: in 5 of 8 rows the third anchor names WHICH
side is isolated, which a two-way intersection cannot. Ecology co-cites Kramers 1940 21-23
times while prognostics does so 0 times; reliability meets Wright 1936 5-6 times while
adaptive management does not.

Six anchors are invisible to Semantic Scholar (three monograph DOIs, Wald 1945, Kimura 1963
and Charnov 1976), and Kaplan-Meier 1958 exceeds its paging cap, so rows 1, 2 and 4 are
single-provider. Lundberg 1903, Cramer 1930, Feller 1968, Erlang 1917, Snell 1952,
Chow-Robbins-Siegmund 1971, Cox 1962 and Crow 1974 have no usable DOI and were replaced by
an indexable member of the same literature; Snell's proposed DOI 404s at Crossref.


## 2. Proposed line for `00-index.md`, in the computed block


- [[C41-uncited-parent-sweep]] — **is C37's uncited-parent pattern general? No — 3 of 8.** Eight confirmed same-object pairs, a named candidate parent theory each, and all three pairwise citer-set intersections on two providers (OpenCitations, Semantic Scholar, 2026-09-05): 2 rows where both sides meet the parent, 3 where one does, **3 double rediscoveries**. The hypothesis that cross-domain gaps are usually two fields that both rediscovered an older formalism is not supported on the project's own most favourable sample. What survives is a diagnostic that fires in 5 of 8 rows: the third anchor names *which* side is isolated — ecology co-cites Kramers 1940 21–23 times against prognostics' 0, reliability meets Wright 1936 5–6 times against adaptive management's 0 — turning a symmetric "gap" into a one-way borrow. Union-floor `E` only; six anchors invisible to Semantic Scholar, so rows 1, 2 and 4 are single-provider


## 3. PROPOSED edit to `method/citation-intersection.md` — NOT APPLIED

**The trigger the brief set was not met.** It asked for a mandatory "parent search first" step
*if most gaps turn out to be class iii*. Three of eight is not most, so the proposal below is
deliberately weaker: an optional third anchor, justified by its diagnostic value rather than by
a base rate. **Do not apply it as written without deciding whether an optional step earns a
place in a method note that is otherwise all mandatory.**

> ### The third anchor: search for the parent
>
> A two-way intersection `A × B` answers "do these literatures meet?". It cannot answer "is
> either of them already inside an older literature that contains the shared object?" — and
> when a gap is stated as a *shared formalism*, that older literature usually exists and is
> nameable. Before quoting an `A × B` zero, name the candidate parent theory `P`, find a
> **citable** anchor for it, and run all three intersections.
>
> Four outcomes, each a different claim:
>
> | | `A × P` | `B × P` | reading |
> |---|---|---|---|
> | **(i)** | > 0 | > 0 | Both fields are already in the parent literature. The gap is the sibling link only, and is smaller than it looks |
> | **(ii)** | > 0 | 0 | **One-way borrow.** One field stands outside a literature the other is inside. Repair is a one-directional import, not an introduction — see [[one-way-borrowing]] |
> | **(iii)** | 0 | 0 | **Double rediscovery.** Two fields rebuilt the parent independently. The strongest form of the gap claim, and the rarest |
> | **(iv)** | — | — | The parent has no usable DOI. Say so; do not report a zero |
>
> **Outcome (iv) is common and must be reported, not worked around.** Pre-1960 classics and
> monographs are badly indexed: [[C41-uncited-parent-sweep]] could not reach Lundberg 1903,
> Cramér 1930, Feller 1968, Erlang 1917, Snell 1952, Chow–Robbins–Siegmund 1971, Cox 1962 or
> Crow 1974 at all, and Semantic Scholar holds no record for three monograph DOIs, for Wald
> 1945, or for Charnov 1976. A substituted anchor is a proxy for the literature, never the
> parent itself, and the substitution belongs in the note.
>
> **Two cautions.** The intersection measures **co-citation, not descent**: `A × P > 0` says
> the two literatures share readers, not that A cites P. And **the parent is a judgement** —
> a different `P` can move a row's class, so name the alternatives you rejected.
>
> Worked in full: [[C41-uncited-parent-sweep]], on eight pairs. Its headline is a negative —
> the double-rediscovery outcome (iii) fired in 3 of 8 rows, so this step is a **diagnostic
> that sharpens a gap's description**, not a filter expected to overturn most gaps.

## [2026-09-05] computed | C42: soil has no steady state above P0; C35's A column withdrawn and C35 regraded REPACKAGED

C42-soil-ha-theory writes the soil-depth balance dD/dt = P(D) − E with Heimsath et al. 1997's
exponential soil production function P(D) = P0·exp(−D/D*) (DOI 10.1038/41056, Crossref-verified
2026-09-05; P0 = 0.077 mm/yr, D* = 434 mm, VERIFIED-SECONDARY on the parameters) and asks what
C6's Ha = k_r/k_d and A = Ha/(1+Ha) mean for a stock.

Results. (a) The steady state is D_ss = D*·ln(P0/E), unique and globally asymptotically stable
because d/dD[P−E] < 0 everywhere — but it exists only if E < P0. Every managed erosion rate in
C35, including BOTH USDA T values, exceeds P0 = 0.077 mm/yr, so there is no steady state and the
profile runs to bedrock: the exact structural mirror of C31's draining fleet. (b) A = Ha/(1+Ha)
has no availability reading. C35 §6's gloss ("steady-state thickness relative to the thickness
the same formation rate would sustain against zero erosion") is WRONG and is withdrawn here —
zero erosion gives D → ∞ under an exponential P, so the denominator diverges. The only surviving
reading, P/(P+E), is a monotone rescaling of Ha and carries no extra information; the A column
should be deleted for every soil row. (c) Derived the exact time to bedrock
t_bed = D0/E + (D*/E)·ln[(E − P0·e^(−D0/D*))/(E − P0)], checked numerically to 3e-10.

The depth-loss horizon for a 300 mm A-horizon: conventional agriculture ~197 yr (Montgomery
median 1.537 mm/yr) or 202 yr at a round 1.5 mm/yr; USDA T = 5 ton/ac/yr 355 yr; T = 1 ton/ac/yr
1,930 yr; no-till 4,615 yr; native vegetation thickens.

Prior art, and it is the correction. Evans, Quinton, Davies & Zhao 2020, Environ. Res. Lett.
15:0940b2, DOI 10.1088/1748-9326/aba2fd (Crossref-verified 2026-09-05; text read) define "soil
lifespan" as L = D/(E − F) with D = 300 mm — that IS the horizon above, published, and C35 does
not cite it. The USDA's own Erosion Index EI = potential erosion / T is 1/Ha with T substituted
for the formation rate. Verheijen et al. 2009 (DOI 10.1016/j.earscirev.2009.02.003,
Crossref-verified) reviews T vs actual erosion for Europe. So: the horizon is prior art, the
T-vs-measured-P discrepancy is Montgomery 2007's (C35 supplies its number, 10.1–50.7×), and the
Ha framing is the project's and is the weakest of the three. **C35-soil-ha is regraded
REPACKAGED**, one grade below its own §6 self-assessment, for a reason §6 did not identify: it
defended against C6's novelty grade, not against soil science's prior art.

Five failure boundaries: (a) depth-dependent P — BREAKS, no scalar Ha describes a soil, and the
humped production function makes the endgame worse not better; (b) conveyor not pool — BREAKS
flux equivalence, depth Ha is an upper bound on quality Ha since erosion takes carbon-rich
topsoil and production adds carbon-free saprolite; (c) cover feedback — the one place soil is
structurally RICHER than C6, since two decreasing curves can cross twice and give a genuine
unstable threshold depth D_crit, which is the collapse point C6 §3.2 denies Ha = 1 ever was
(asserted, not solved; the Kirkby attribution is UNVERIFIED); (d) time scales — 10^4-yr
cosmogenic P against decadal E SURVIVES as a policy comparison, FAILS for any dynamical claim,
so "native vegetation is at Ha ≈ 1" is not balance observed; (e) bulk density — SURVIVES,
rho_b 1100–1600 moves T:k_r from 10–51× to 8–60×, never near 1, though compaction biases it with
a sign.

Also found, and it is bigger than the rho_b band: Heimsath's P at D = 300 mm is 0.0386 mm/yr,
2.3× Montgomery's compiled median of 0.017 that C35 uses as k_r throughout. A median across
sites of unstated depth is not P at a stated depth, so every soil Ha carries a factor-~2
ambiguity from a variable neither source reports. No sign or order of magnitude changes.

Produced by: python _scripts/c42_soil_theory.py (no network). DOIs via Crossref
(mailto=deciduusleaf@gmail.com), fetched 2026-09-05.

Correction to the task brief as given: the DOI supplied for Evans et al. 2020 was
10.1016/j.envsci.2020.09.019, which Crossref resolves to López-Rodríguez et al., "Delineating
participation in conservation governance", Environ. Sci. Policy 114:486–496 — a different paper
in a different journal. The correct record is 10.1088/1748-9326/aba2fd, Environ. Res. Lett.


## 2. For `vault/00-index.md` — computed block, insert after the `C35-soil-ha` line


- [[C42-soil-ha-theory]] — **soil is a stock, and the mapping is structural-only.** Writing dD/dt = P(D) − E with Heimsath 1997's P(D) = P0·exp(−D/D*) gives a unique globally stable steady state D_ss = D*·ln(P0/E) that **exists only if E < P0 = 0.077 mm/yr** — which no managed row of C35 satisfies, including both USDA T values, so the profile runs to bedrock in the finite time D0/E + (D*/E)·ln[(E − P0·e^(−D0/D*))/(E − P0)], derived here. A = Ha/(1+Ha) has no availability reading and C35 §6's thickness gloss is withdrawn: the only surviving sense, P/(P+E), is a monotone rescaling of Ha. The 300 mm depth-loss horizon is **197 yr** under conventional agriculture and **355 yr** at T = 5 ton/ac/yr — and it is prior art, Evans et al. 2020 ERL 15:0940b2's "soil lifespan" L = D/(E−F), uncited by C35; the USDA's Erosion Index is already 1/Ha with T for k_r. **C35 regraded REPACKAGED.** Five boundaries: state-dependent P breaks the scalar Ha, the conveyor breaks flux equivalence (depth Ha bounds quality Ha from above), cover feedback gives a real threshold depth D_crit where C6's Ha = 1 never was, the 10⁴-yr/decadal window mismatch survives only as policy comparison, bulk density survives (8–60×)


## [2026-09-05] computed + verification | C35's falsifier run against real data: T does not track measured formation, and Borrelli 2017 turned out to be fetchable after all

[[C43-soil-ha-replication]] executes the paired test [[C35-soil-ha]] section 5 named. Pre-registered
in `audits/blind-brief-c43-2026-09-05.md`, sha256
`dbae0496666126c4070f518f16d1bf997f6c6b9165469284f940440b5e7ef727`, hashed before any site-level
value was fetched.

Two live APIs, both worked, both named: OCTOPUS v2.2 WFS
(`http://geoserver.octopusdata.org/geoserver/wfs`, GetCapabilities and GetFeature CSV, 200) for
Be-10 denudation with coordinates, and USDA-NRCS Soil Data Access
(`https://sdmdataaccess.sc.egov.usda.gov/Tabular/post.rest`, POST T-SQL with
`SDA_Get_Mukey_from_intersection_with_WktWgs84`) for `tfact` and `dbthirdbar_r` at each point.
Re-runnable: `python _scripts/c43_soil_data.py` from `vault/`.

**Two corrections to citations C35 and its brief carried.** (a) Stockmann et al. 2014 "How fast
does soil grow?" is *Geoderma* 216:48-61, not *Earth-Science Reviews* — Crossref
`10.1016/j.geoderma.2013.10.007`, fetched 2026-09-05, `container-title: Geoderma`. (b) Bui et al.
2011 on Australian tolerable erosion is *Agriculture, Ecosystems & Environment* 144:136-144,
`10.1016/j.agee.2011.07.022`, not *Geoderma*; it is closed access and was not used.

**One provenance upgrade that C35 must eventually take.** C35 section 6 records Borrelli et al.
2017 as unfetchable and its 2.8 Mg/ha/yr as VERIFIED-SECONDARY. It is gold open access:
OpenAlex `doi:10.1038/s41467-017-02142-7` gives `oa_url = https://www.nature.com/articles/
s41467-017-02142-7.pdf`, fetched 2026-09-05 (9.06 MB, 13 pp.), and the printed text reads
"an area-specific soil erosion average of 2.8 Mg ha-1 yr-1" for 2001. C43 does not edit C35;
this is the standing instruction to do so.


## 2. Line for `vault/00-index.md`, in the computed block next to `[[C35-soil-ha]]`


- [[C43-soil-ha-replication]] — **C35's falsifier, run.** Pre-registered (brief sha256 dbae0496...) and executed against OCTOPUS Be-10 denudation joined point-in-polygon to SSURGO `tfact` via the USDA Soil Data Access API. The pre-registered test is reported with its power stated in the note. Spearman rho(T, P) is the load-bearing number: it decides whether `T` is a biased formation estimate or not a formation estimate at all. Adds non-US erosion-vs-formation rows (Europe, Australia, China) to C35's axis from Borrelli 2017 and Panagos 2015, both now full-text-read


## [2026-09-05] correction | G36 narrowed to leg 1 and mediated; C35 §5 regraded REDISCOVERED


Body: leg 2 withdrawn as a fatigue analogy — MWD is non-monotone and reverses sign between bare
and vegetated soil under identical wet–dry cycling (PMC12907374, 2026), so Miner's monotone `D`
is the wrong formalism and `Ha` is the right one; `topology` disjoint → mediated, via
bedrock-incision geomorphology (Sklar & Dietrich 2001 co-cited with Archard 1953, Meng & Ludema
1995 and Nearing 1989 on OpenCitations 2026-09-05; Hsu, Dietrich & Sklar 2008 writes Archard's
law out in full and names tribology); `crosses` formalism(4) → metaphor(2) on C35 §4's own
demonstration that the functional form does not survive; the `T`-versus-formation discrepancy
located in Montgomery 2007, Verheijen 2009 and the soil-loss-tolerance review literature, so C35
§5 is a rediscovery; `T` = 5 short ton/ac/yr shown to equal 1 inch per 29.5 years, making the
"`T` was defined as the assumed production rate" claim quantitative; `T`-range provenance
conflict with Montgomery's own 5–12 t/ha/yr logged. **All of C35's unit conversions reproduce
exactly and are not in question.** Produced by `audits/g36-adversarial.md`.


## [2026-09-05] verification | G36 failure mode 6 closed: soil side extended to 1936-2022, still 40 zeros, on two providers

The standing hole in G36 was that its soil anchors were all 1989-2001, so a pooled zero could not
be told from a vocabulary that had moved. Six soil anchors added and Crossref-verified: Yoder 1936
(10.2134/agronj1936.00021962002800050001x), Ellison 1948 (10.2136/sssaj1948.036159950012000c0107x),
Wischmeier & Smith 1959 (10.2136/sssaj1959.03615995002300030027x), Emerson 1967 (10.1071/sr9670047),
Borrelli 2017 (10.1038/s41467-017-02142-7), Rieke 2022 (10.1016/j.geoderma.2022.116156). Ellison
1947 (Agricultural Engineering 28) and the Wischmeier & Smith USLE handbooks (Agriculture Handbook
282/537) have no DOI in Crossref and were replaced by the nearest DOI-bearing work of the same
decade and lineage. All 40 mechanics x soil cells are 0 on OpenCitations and 0 on Semantic Scholar
wherever S2 sees both anchors. Two new age controls fire - Yoder 1936 x Le Bissonnais 1996 = 110
(OC) / 105 (S2) and Wischmeier & Smith 1959 x RUSLE 1991 = 26 - so the pre-1970 anchors are visible
to the instrument and their zero is a measurement. Standing unchanged: live.

## [2026-09-05] method | Two provider traps recorded: an S2 coverage hole is not a zero; chapter DOIs inflate a cell

Semantic Scholar holds no record for Miner 1945 (10.1115/1.4009458) or RUSLE 1991
(10.1080/00224561.1991.12456571); both rows are recorded as err, never as zeros. OpenAlex returned
"insufficient budget ... resets at midnight utc" on the second call of the round and contributed
nothing. Separately, the Sklar & Dietrich x Borrelli 2017 cell read 23 hits which resolve to ONE
monograph deposited with chapter-level DOIs (Rhoads 2020, River Dynamics, 10.1017/9781108164108 and
.001-.022) plus one review article. Any book-heavy cell will read high for the same reason.

## [2026-09-05] honest null | G36's mediated-topology objection run and rejected: the mediator does not carry

The adversary's move on G36 is that soil science need not cite Archard because bedrock-incision
geomorphology already runs a wear model. Run, both providers: Sklar & Dietrich 2001/2004 x each
mechanics anchor is 0-1, and their own deposited reference lists (59 and 12 DOIs, OpenCitations
2026-09-05) contain none of the four mechanics anchors. No work co-cites a mechanics anchor and a
soil anchor. The two alternative mediators are flat zero - Van Oost 2000 (tillage erosion) x Archard
= 0 and Shao 2001 (wind-erosion abrasion) x Archard = 0 - while Van Oost x Nearing = 26/28 confirms
tillage erosion sits inside soil erosion. topology stays disjoint; contact-surface stays 0. Two
named nearest misses were found and inspected: Lefebvre & Jop 2013 (Phys. Rev. E 88, 032205), which
co-cites Sklar, Archard and Meng & Ludema, and Bodek & Jerolmack 2021 (Earth Surf. Dynam. 9, 1531),
which co-cites Sklar and Paris & Erdogan.


---

## D1 — open disagreement with the adversarial leg, for whoever reconciles them

`PENDING-log-G36ADV.md` proposes `topology: mediated` with the mediator
*"bedrock-incision geomorphology (Sklar & Dietrich 2001; Hsu, Dietrich & Sklar 2008, JGR Earth
Surf. 113, which writes Archard's law out in full and cites Archard 1953)"*. This leg tested that
claim and reaches the opposite verdict. The two findings, so the reconciler can weigh them:

1. **The Archard citation in Hsu 2008 is not corroborated by metadata, and is not settled.**
   Crossref deposits **102** references for `10.1029/2007JF000778`; **none** matches `archard`,
   `wear` or `tribolog` in structured or unstructured form, and OpenCitations resolves 85 of them
   to DOIs without `10.1063/1.1721448`. Deposited lists can be incomplete and a printed
   bibliography is a different object, so **this does not disprove the adversarial leg's claim** —
   it means the claim rests on a full-text read that neither leg has recorded. **Do not apply
   either verdict on this point without opening the PDF.**
2. **The second hop is empty, which decides the topology on its own.** Hsu 2008 has 69 citers
   (OpenCitations, 2026-09-05) and its intersection with **all six** soil anchors — Nearing 1989,
   Le Bissonnais 1996, Amézketa 1999, Denef 2001, Yoder 1936, Borrelli 2017 — is **0**, while the
   control Hsu × Sklar & Dietrich 2004 fires at 7. Whatever Hsu cites, **no soil-science work
   reaches the mechanics literature through it.** A mediator nothing traverses does not make a
   topology mediated, so `topology: disjoint` was kept and the whole probe written into G36's
   Provenance block rather than the frontmatter.

The two legs do **not** conflict on `crosses` or on leg 2's fate; this leg took no view on either
and did not touch the claim sections.

---

## D2 — cells that should stop being quoted

The Meng & Ludema row and the four small soil anchors fall at or below `E = 1` once a field-scale
denominator is used (`N ≈ 1.0×10⁵` from Semantic Scholar bulk phrase totals): Meng × Rieke 2022 is
`E = 0.87`, Meng × Emerson 1967 `E = 1.96`, Meng × W&S 1959 `E = 3.00`, and Ellison 1948's whole
row is uninformative at any `N` because its citer set is 21 works. They are corroboration, not
evidence, and G36's Provenance now says so. The load-bearing cells are Archard, Miner and Paris
against Yoder 1936, Nearing 1989, Le Bissonnais 1996, Amézketa 1999, Denef 2001 and Borrelli 2017.


## [2026-09-05] correction | G36 narrowed: leg 2 withdrawn on sign, leg 1 survives as a citation gap with no missing object; topology stays disjoint

Four legs ran against G36-wear-erosion-damage and C35-soil-ha on 2026-09-05: an adversarial
review, a provenance re-run, and two computations (C42-soil-ha-theory, C43-soil-ha-replication).
G36 standing live -> narrowed.

Leg 2 (cumulative fatigue <-> aggregate breakdown under wet-dry cycling) is WITHDRAWN ON SIGN.
Miner's D = sum n_i/N_i is monotone non-decreasing and carries no repair term. Mean weight
diameter is not monotone under wet-dry cycling: aggregates can STRENGTHEN, MWD rising in
vegetated soil and falling in bare soil under an identical protocol, and rising over early cycles
before falling later within a single treatment. Two opposed rates run at once, so the state
variable is not a damage fraction and a Weibull beta fitted to MWD(n) would be a shape parameter
fitted to a series that changes direction. G36's "what would close it" item 3 is withdrawn with
it. The replacement object is C6-damage-healing-ratio itself: MWD(n) approaches a
treatment-specific asymptote MWD_inf set by Ha = k_r/k_d, from below where re-aggregation wins and
from above where breakdown does, so the sign of dMWD/dn at n = 1 does not predict MWD_inf. Needs
>=3 cycle points; Denef 2001 and Amezketa 1999 print cycle-resolved tables and are the cheap test.

Leg 1 (wear <-> erosion detachment) SURVIVES, but only as a citation gap with NO MISSING OBJECT.
crosses stays formalism(4) because K, K_r, K_i and K_USLE are one species of object - an
empirically fitted dimensional constant standing in for an unresolved contact mechanism,
unpredicted from bulk properties in both fields - but the note now says explicitly that the
formalism DOES NOT TRANSFER. Archard's resistance is a divisor and his law passes through the
origin; WEPP's is a threshold and below tau_c detachment is exactly zero; C35 section 4's
dimensionless soil analogue K_soil is not a constant but sweeps orders of magnitude within one
soil as tau varies. So soil science is not missing a law it could import from tribology. What it
is missing is the other field's forty years of published failure to predict its own constant.

topology stays DISJOINT, against the adversarial leg's proposed mediated. A mediator must be read
by BOTH sides. The proposed mediator, Hsu, Dietrich & Sklar 2008 (10.1029/2007JF000778), is read
by neither soil anchor: Hsu x all six soil anchors (Nearing, Le Bissonnais, Amezketa, Denef,
Yoder, Borrelli) = 0 on OpenCitations 2026-09-05, while the control Hsu x Sklar & Dietrich 2004
fires at 7; Sklar & Dietrich's own deposited reference lists (59 and 12 DOIs) contain none of the
four mechanics anchors. The adversarial leg reports that Hsu 2008 writes Archard's e_v = kWx/H out
in full and cites Archard 1953 in its printed text; Crossref's 102 deposited references for that
DOI contain no archard/wear/tribolog match and OpenCitations resolves 85 of them without
10.1063/1.1721448. A deposited list can be incomplete and a printed bibliography is a different
object, so the metadata does not disprove the claim - IT IS AN OPEN DISAGREEMENT NEEDING A
FULL-TEXT READ, and it is recorded as one in G36's new "Narrowing" section. Ruling applied: if the
full text confirms the citation it is a ONE-WAY BORROW, geomorphology -> tribology, which does not
make the topology mediated, because nothing traverses back to soil science.

computed-in on G36 extended to C35-soil-ha, C42-soil-ha-theory and C43-soil-ha-replication.
contact-surface stays 0. The 40-cell decade grid, the nine controls and the E figures are
unchanged and the Provenance block was not edited.

## [2026-09-05] correction | C35 corrected on the T range, the A column and the grade: section 5 is REDISCOVERED, and C43's site-level anti-correlation is the only new thing in the cluster

C35-soil-ha corrected on ten points; ALL OF ITS UNIT CONVERSIONS AND ARITHMETIC REPRODUCE EXACTLY
and none is in question.

(1) T-range provenance. C35 quoted T only as 1-5 short ton/ac/yr from secondary NRCS summaries
while Montgomery 2007 - its own VERIFIED-PRIMARY source for every other rate - states T as 5-12
t/ha/yr at rho_b = 1200 kg/m3, about 0.42-1.00 mm/yr (0.41 mm/yr at the low end). Montgomery's
range is now the primary input, row 8; the 1-5 short ton/ac policy range is retained as the
secondary policy range, row 8b, and labelled as such. (2) The ratio is restated as 22.6-54.3x on
Montgomery's range at this note's rho_b 1300 (0.385-0.923 mm/yr against a formation median of
0.017), Ha = 0.018-0.044; the previous 10.1-50.7x and Ha = 0.020-0.099 are kept as the secondary
reading. (3) The A = Ha/(1+Ha) column is DELETED for every soil row per C42 section 3 - a stock
has no functional/damaged partition, bedrock is absorbing so nothing cycles, and the only
surviving reading P/(P+E) is a monotone rescaling of Ha carrying no extra information. Non-soil
rows keep A. (4) C35 section 6's gloss on A - "steady-state profile thickness relative to the
thickness the same formation rate would sustain against zero erosion" - is WITHDRAWN AS FALSE:
under an exponential production function zero erosion gives D -> infinity and the denominator
diverges.

(5) Section 5 is REGRADED REDISCOVERED. Verheijen, Jones, Rickson & Smith 2009 (Earth-Sci. Rev.
94:23-38, 10.1016/j.earscirev.2009.02.003, Crossref-verified) sets tolerable = formation at 0.3-1.4
t/ha/yr for Europe and reports actual arable erosion at 3-40x the upper tolerable limit, from which
the ratio follows by one division; Montgomery 2007's abstract states the discrepancy at one to two
orders of magnitude; and the arithmetic confirms the provenance - T = 5 short ton/ac/yr = 0.862
mm/yr at rho_b 1300 = 1 inch per 29.5 years, the Soil Conservation Service's "1 inch in 30 years"
renewal assumption to within 1.8%. So Ha = 1 at T is T's construction, not a convention this vault
uncovered. (6) The policy-relevant dimensioned numbers are now cited and stated: Evans, Quinton,
Davies, Zhao & Govers 2020, Environ. Res. Lett. 15:0940b2, DOI 10.1088/1748-9326/aba2fd
(Crossref-verified; note the brief's DOI 10.1016/j.envsci.2020.09.019 is a DIFFERENT PAPER,
Lopez-Rodriguez et al. in Environ. Sci. Policy) defines soil lifespan L = D/(E-F) at D = 300 mm
over 10,030 plot-years from 255 sites - prior art C35 did not cite - and C42 section 4 supplies the
exact time to bedrock: 197 yr under conventional agriculture, 355 yr at T = 5 short ton/ac, 1,930
yr at T = 1. (7) A factor-2 depth ambiguity is now stated in section 6: Heimsath's P at D = 300 mm
is 0.0386 mm/yr against Montgomery's compiled median of 0.017 used as k_r throughout, and a median
across sites of unstated depth is not P at a stated depth. That is larger than the +-18% rho_b band
C35 does discuss and changes no sign and no order of magnitude.

(8) Borrelli et al. 2017 is fetchable after all - gold OA, OpenAlex doi:10.1038/s41467-017-02142-7
-> nature.com/articles/s41467-017-02142-7.pdf, read in full by C43, printed text "an area-specific
soil erosion average of 2.8 Mg ha-1 yr-1" for 2001 - so the global-mean k_d is upgraded from
VERIFIED-SECONDARY to VERIFIED-PRIMARY. One datum came with it: Borrelli's own generic global
T-value of 10 Mg/ha/yr is 0.769 mm/yr at rho_b 1300, 45x Montgomery's formation median, i.e. the
Ha = 1 construction is being carried into global erosion modelling ABOVE the top of the USDA range.
(9) Section 5's falsifier, named but never run, was run on 1,053 US sites in C43 and did not fire.
(10) Two citations the brief carried are corrected: Stockmann et al. 2014 "How fast does soil
grow?" is Geoderma 216:48-61 (10.1016/j.geoderma.2013.10.007), not Earth-Science Reviews; Bui et
al. 2011 is Agric. Ecosyst. Environ. (10.1016/j.agee.2011.07.022), not Geoderma.

Grades: C35 REPACKAGED (+ CORRECTED) with section 5 REDISCOVERED; G36 LOCATED (narrowed). The one
candidate for a genuinely new empirical claim in the whole cluster is C43's site-level Spearman
rho(T, P) = -0.180, p = 4.5e-9, and it is logged in novelty-audit.md as pending its own
adversarial pass. All three grades are in vault/novelty-audit.md.

## [2026-09-05] computed | C42: soil has no steady state above P0; C35's A column withdrawn and C35 regraded REPACKAGED

C42-soil-ha-theory writes the soil-depth balance dD/dt = P(D) - E with Heimsath et al. 1997's
exponential soil production function P(D) = P0*exp(-D/D*) (DOI 10.1038/41056, Crossref-verified
2026-09-05; P0 = 0.077 mm/yr, D* = 434 mm, VERIFIED-SECONDARY on the parameters) and asks what
C6's Ha = k_r/k_d and A = Ha/(1+Ha) mean for a stock.

Results. (a) The steady state is D_ss = D*.ln(P0/E), unique and globally asymptotically stable
because d/dD[P-E] < 0 everywhere - but it exists only if E < P0. Every managed erosion rate in
C35, including BOTH USDA T values, exceeds P0 = 0.077 mm/yr, so there is no steady state and the
profile runs to bedrock: the exact structural mirror of C31's draining fleet. (b) A = Ha/(1+Ha)
has no availability reading. C35 section 6's gloss ("steady-state thickness relative to the
thickness the same formation rate would sustain against zero erosion") is WRONG and is withdrawn -
zero erosion gives D -> infinity under an exponential P, so the denominator diverges. The only
surviving reading, P/(P+E), is a monotone rescaling of Ha and carries no extra information; the A
column is deleted for every soil row. (c) Derived the exact time to bedrock
t_bed = D0/E + (D*/E).ln[(E - P0.e^(-D0/D*))/(E - P0)], checked numerically to 3e-10.

The depth-loss horizon for a 300 mm A-horizon: conventional agriculture ~197 yr (Montgomery median
1.537 mm/yr) or 202 yr at a round 1.5 mm/yr; USDA T = 5 ton/ac/yr 355 yr; T = 1 ton/ac/yr 1,930
yr; no-till 4,615 yr; native vegetation thickens.

Prior art, and it is the correction. Evans, Quinton, Davies & Zhao 2020, Environ. Res. Lett.
15:0940b2, DOI 10.1088/1748-9326/aba2fd (Crossref-verified 2026-09-05; text read) define "soil
lifespan" as L = D/(E - F) with D = 300 mm - that IS the horizon above, published, and C35 did not
cite it. The USDA's own Erosion Index EI = potential erosion / T is 1/Ha with T substituted for the
formation rate. Verheijen et al. 2009 (DOI 10.1016/j.earscirev.2009.02.003, Crossref-verified)
reviews T vs actual erosion for Europe. So: the horizon is prior art, the T-vs-measured-P
discrepancy is Montgomery 2007's (C35 supplies its number), and the Ha framing is the project's and
is the weakest of the three. C35-soil-ha is regraded REPACKAGED, one grade below its own section 6
self-assessment, for a reason section 6 did not identify: it defended against C6's novelty grade,
not against soil science's prior art.

Five failure boundaries: (a) depth-dependent P - BREAKS, no scalar Ha describes a soil, and the
humped production function makes the endgame worse not better; (b) conveyor not pool - BREAKS flux
equivalence, depth Ha is an upper bound on quality Ha since erosion takes carbon-rich topsoil and
production adds carbon-free saprolite; (c) cover feedback - the one place soil is structurally
RICHER than C6, since two decreasing curves can cross twice and give a genuine unstable threshold
depth D_crit, which is the collapse point C6 section 3.2 denies Ha = 1 ever was (asserted, not
solved; the Kirkby attribution is UNVERIFIED); (d) time scales - 10^4-yr cosmogenic P against
decadal E SURVIVES as a policy comparison, FAILS for any dynamical claim, so "native vegetation is
at Ha ~ 1" is not balance observed; (e) bulk density - SURVIVES, rho_b 1100-1600 moves T:k_r from
10-51x to 8-60x, never near 1, though compaction biases it with a sign.

Also found, and it is bigger than the rho_b band: Heimsath's P at D = 300 mm is 0.0386 mm/yr, 2.3x
Montgomery's compiled median of 0.017 that C35 uses as k_r throughout. A median across sites of
unstated depth is not P at a stated depth, so every soil Ha carries a factor-~2 ambiguity from a
variable neither source reports. No sign or order of magnitude changes.

Produced by: python _scripts/c42_soil_theory.py (no network). DOIs via Crossref
(mailto=deciduusleaf@gmail.com), fetched 2026-09-05.

Correction to the task brief as given: the DOI supplied for Evans et al. 2020 was
10.1016/j.envsci.2020.09.019, which Crossref resolves to Lopez-Rodriguez et al., "Delineating
participation in conservation governance", Environ. Sci. Policy 114:486-496 - a different paper in
a different journal. The correct record is 10.1088/1748-9326/aba2fd, Environ. Res. Lett.

## [2026-09-05] computed + verification | C35's falsifier run against real data: T does not track measured formation, and Borrelli 2017 turned out to be fetchable after all

C43-soil-ha-replication executes the paired test C35-soil-ha section 5 named. Pre-registered
in `audits/blind-brief-c43-2026-09-05.md`, sha256
`dbae0496666126c4070f518f16d1bf997f6c6b9165469284f940440b5e7ef727`, hashed before any site-level
value was fetched.

Two live APIs, both worked, both named: OCTOPUS v2.2 WFS
(`http://geoserver.octopusdata.org/geoserver/wfs`, GetCapabilities and GetFeature CSV, 200) for
Be-10 denudation with coordinates, and USDA-NRCS Soil Data Access
(`https://sdmdataaccess.sc.egov.usda.gov/Tabular/post.rest`, POST T-SQL with
`SDA_Get_Mukey_from_intersection_with_WktWgs84`) for `tfact` and `dbthirdbar_r` at each point.
Re-runnable: `python _scripts/c43_soil_data.py` from `vault/`.

Two corrections to citations C35 and its brief carried. (a) Stockmann et al. 2014 "How fast
does soil grow?" is Geoderma 216:48-61, not Earth-Science Reviews - Crossref
`10.1016/j.geoderma.2013.10.007`, fetched 2026-09-05, `container-title: Geoderma`. (b) Bui et al.
2011 on Australian tolerable erosion is Agriculture, Ecosystems & Environment 144:136-144,
`10.1016/j.agee.2011.07.022`, not Geoderma; it is closed access and was not used.

One provenance upgrade that C35 must eventually take. C35 section 6 records Borrelli et al.
2017 as unfetchable and its 2.8 Mg/ha/yr as VERIFIED-SECONDARY. It is gold open access:
OpenAlex `doi:10.1038/s41467-017-02142-7` gives `oa_url = https://www.nature.com/articles/
s41467-017-02142-7.pdf`, fetched 2026-09-05 (9.06 MB, 13 pp.), and the printed text reads
"an area-specific soil erosion average of 2.8 Mg ha-1 yr-1" for 2001. (APPLIED 2026-09-05 by the
integration pass; C35 section 6 now records it as VERIFIED-PRIMARY.)

## [2026-09-05] verification | G36 failure mode 6 closed: soil side extended to 1936-2022, still 40 zeros, on two providers

The standing hole in G36 was that its soil anchors were all 1989-2001, so a pooled zero could not
be told from a vocabulary that had moved. Six soil anchors added and Crossref-verified: Yoder 1936
(10.2134/agronj1936.00021962002800050001x), Ellison 1948 (10.2136/sssaj1948.036159950012000c0107x),
Wischmeier & Smith 1959 (10.2136/sssaj1959.03615995002300030027x), Emerson 1967 (10.1071/sr9670047),
Borrelli 2017 (10.1038/s41467-017-02142-7), Rieke 2022 (10.1016/j.geoderma.2022.116156). Ellison
1947 (Agricultural Engineering 28) and the Wischmeier & Smith USLE handbooks (Agriculture Handbook
282/537) have no DOI in Crossref and were replaced by the nearest DOI-bearing work of the same
decade and lineage. All 40 mechanics x soil cells are 0 on OpenCitations and 0 on Semantic Scholar
wherever S2 sees both anchors. Two new age controls fire - Yoder 1936 x Le Bissonnais 1996 = 110
(OC) / 105 (S2) and Wischmeier & Smith 1959 x RUSLE 1991 = 26 - so the pre-1970 anchors are visible
to the instrument and their zero is a measurement. Standing at the time of this run: live;
narrowed the same day by the integration pass, on leg 2 and on the missing-object question, NOT on
any of these measurements.

## [2026-09-05] method | Two provider traps recorded: an S2 coverage hole is not a zero; chapter DOIs inflate a cell

Semantic Scholar holds no record for Miner 1945 (10.1115/1.4009458) or RUSLE 1991
(10.1080/00224561.1991.12456571); both rows are recorded as err, never as zeros. OpenAlex returned
"insufficient budget ... resets at midnight utc" on the second call of the round and contributed
nothing. Separately, the Sklar & Dietrich x Borrelli 2017 cell read 23 hits which resolve to ONE
monograph deposited with chapter-level DOIs (Rhoads 2020, River Dynamics, 10.1017/9781108164108 and
.001-.022) plus one review article. Any book-heavy cell will read high for the same reason.

## [2026-09-05] honest null | G36's mediated-topology objection run and rejected: the mediator does not carry

The adversary's move on G36 is that soil science need not cite Archard because bedrock-incision
geomorphology already runs a wear model. Run, both providers: Sklar & Dietrich 2001/2004 x each
mechanics anchor is 0-1, and their own deposited reference lists (59 and 12 DOIs, OpenCitations
2026-09-05) contain none of the four mechanics anchors. No work co-cites a mechanics anchor and a
soil anchor. The two alternative mediators are flat zero - Van Oost 2000 (tillage erosion) x Archard
= 0 and Shao 2001 (wind-erosion abrasion) x Archard = 0 - while Van Oost x Nearing = 26/28 confirms
tillage erosion sits inside soil erosion. topology stays disjoint; contact-surface stays 0. Two
named nearest misses were found and inspected: Lefebvre & Jop 2013 (Phys. Rev. E 88, 032205), which
co-cites Sklar, Archard and Meng & Ludema, and Bodek & Jerolmack 2021 (Earth Surf. Dynam. 9, 1531),
which co-cites Sklar and Paris & Erdogan.


---

## 2. For `vault/00-index.md` — computed block, insert after the `C35-soil-ha` line

Copied verbatim from `PENDING-log-C42.md` §2 and `PENDING-log-C43.md` §2.


- [[C42-soil-ha-theory]] — **soil is a stock, and the mapping is structural-only.** Writing dD/dt = P(D) − E with Heimsath 1997's P(D) = P0·exp(−D/D*) gives a unique globally stable steady state D_ss = D*·ln(P0/E) that **exists only if E < P0 = 0.077 mm/yr** — which no managed row of C35 satisfies, including both USDA T values, so the profile runs to bedrock in the finite time D0/E + (D*/E)·ln[(E − P0·e^(−D0/D*))/(E − P0)], derived here. A = Ha/(1+Ha) has no availability reading and C35 §6's thickness gloss is withdrawn: the only surviving sense, P/(P+E), is a monotone rescaling of Ha. The 300 mm depth-loss horizon is **197 yr** under conventional agriculture and **355 yr** at T = 5 ton/ac/yr — and it is prior art, Evans et al. 2020 ERL 15:0940b2's "soil lifespan" L = D/(E−F), uncited by C35; the USDA's Erosion Index is already 1/Ha with T for k_r. **C35 regraded REPACKAGED.** Five boundaries: state-dependent P breaks the scalar Ha, the conveyor breaks flux equivalence (depth Ha bounds quality Ha from above), cover feedback gives a real threshold depth D_crit where C6's Ha = 1 never was, the 10⁴-yr/decadal window mismatch survives only as policy comparison, bulk density survives (8–60×)



- [[C43-soil-ha-replication]] — **C35's falsifier, run.** Pre-registered (brief sha256 dbae0496...) and executed against OCTOPUS Be-10 denudation joined point-in-polygon to SSURGO `tfact` via the USDA Soil Data Access API. The pre-registered test is reported with its power stated in the note. Spearman rho(T, P) is the load-bearing number: it decides whether `T` is a biased formation estimate or not a formation estimate at all. Adds non-US erosion-vs-formation rows (Europe, Australia, China) to C35's axis from Borrelli 2017 and Panagos 2015, both now full-text-read


## 3. Also owed on `vault/00-index.md`

- The **G36 standing line** must change from `live` to **narrowed** to match the note
  (`CLAUDE.md`: the index is canonical for standings, so this is a real inconsistency until it is
  merged). Its one-line summary is also stale — it still says "three soil anchors (1996, 1999,
  2001)" and "thirteen anchor pairings", both superseded by the 40-cell 1936–2022 grid, and it
  still asserts leg 2. Suggested replacement:


- [[G36-wear-erosion-damage]] — *citation-intersection* — **NARROWED 2026-09-05.** Tribology and agricultural soil-erosion modelling fit the same species of constant to the same measurement and cite each other nowhere: 40 decade-binned cells (four mechanics anchors 1945–1995 × ten soil anchors 1936–2022), 0 on OpenCitations and 0 on Semantic Scholar wherever S2 sees both anchors, nine controls firing, E = 75.6 on Archard × Nearing at the narrow scoped N and 7.6 at 10×. But the gap names **no missing object** — the Archard form does not transfer (divisor vs threshold; C35 §4's K_soil is not constant) — and **leg 2 (Miner ↔ aggregate breakdown) is withdrawn on sign**, because MWD is non-monotone under wet–dry cycling while Miner's D cannot be. topology stays disjoint: the proposed mediator (Hsu 2008) is read by neither soil anchor. Computed in C35, C42, C43


- The **C35 line** is stale on one number: it says "overstates measured soil formation by 10-51x",
  which is the secondary policy range; the primary figure is **22.6–54.3×** on Montgomery's own
  stated `T` range. Suggested replacement:


- [[C35-soil-ha]] — **soil on C6's axis.** Conventional agriculture Ha = 0.011, no-till 0.21, native vegetation 1.31 (Montgomery 2007 Table 1, VERIFIED-PRIMARY). The USDA T-value is Ha = 1 by construction and overstates measured soil formation by 22.6-54.3x on Montgomery's own T range (10.1-51x on the secondary 1-5 ton/ac policy range); Archard's linearity survives only above WEPP's shear threshold, and the formalism does not transfer. **§5 regraded REDISCOVERED 2026-09-05** (Verheijen 2009, Montgomery 2007); the A column is deleted for soil rows per C42


## 4. Adjudication of `PENDING-log-G36ADV.md`, so it can be deleted

| Proposal | Disposition |
|---|---|
| **P1** frontmatter | **PART-APPLIED.** `standing: narrowed` applied. `crosses: metaphor` / rank 2 **REJECTED** — the two sides genuinely write constitutive laws of the same species; the note now says instead that the formalism does not *transfer*. `topology: mediated` + `mediator:` **REJECTED** — see §1's first entry and the open disagreement. `note:` rewritten rather than appended |
| **P2** epigraph | **APPLIED in substance, reworded.** "Never once citing them" is narrowed to agricultural soil-erosion modelling and the missing-object claim is withdrawn. The Europe PMC "soil is the abrader, never the abraded" figure was **not** reproduced here — it rests on one instrument and is one short of the C5 §11 bar; it belongs in the backlog, not in the note |
| **P3** what-would-close-it item 3 | **APPLIED**, rewritten in the note's own voice; the `dMWD/dn` prediction is kept |
| **P4** strongest objection item 2 | **APPLIED**, rewritten |
| **P5** C35 §5 claim box | **APPLIED in substance.** §5 is regraded REDISCOVERED with Verheijen 2009 and Montgomery 2007 named and the 1-inch-in-29.5-years arithmetic stated. The residue is stated more narrowly than P5 proposed: C43's site-level ρ(T, P) is the project's own, and it is the only thing in the cluster that is |
| **P6** C35 §2 row 8 | **APPLIED**, as rows 8 (Montgomery, primary) and 8b (policy range, secondary) |
| **P7** C35 §6 Evans 2020 | **APPLIED**, in §5 rather than §6, with the corrected DOI `10.1088/1748-9326/aba2fd` and alongside C42's time-to-bedrock |
| **P8** C35 §4 Hsu 2008 | **NOT APPLIED.** It rests on the same unverified full-text read as the mediator claim. Recorded in G36's Narrowing section as an open disagreement and a possible one-way borrow instead |
| **P9** novelty-audit rows | **APPLIED**, reworded, plus a fifth entry for C43's ρ(T, P) as the one new-claim candidate |
| **P10** log entry | **SUPERSEDED** by §1 above, which reaches a different verdict on topology and on `crosses` |
| **P11** backlog lines | **NOT APPLIED** — `BACKLOG.md` was out of scope for the integration pass. Still owed, and the highest-value line is unchanged: **read Hsu, Dietrich & Sklar 2008 in full** and settle whether it cites Archard 1953, which is the one document that decides the open disagreement. Verheijen 2009 in full, Li et al. 2009 on the "1 inch in 30 years" provenance, an NRCS primary on `T`, the positive control on the mediator, the P3 test on Denef 2001 / Amézketa 1999, and the C43 adversarial pass are the rest |

## 5. Files to delete once §1–§3 are merged

`PENDING-log-C42.md`, `PENDING-log-C43.md`, `PENDING-log-G36ADV.md`, `PENDING-log-G36PROV.md`,
and this file. The integration pass was not authorised to delete them.

## [2026-09-05] computed | Soil's Ha ledger goes global: 5,611 sites, median Ha = 0.41 — and the US T finding does not generalise

P-001 (Track A) ran C43's join off United States ground. Pre-registered in
`audits/blind-brief-c44-2026-09-05.md`, sha256
724ae9034bbc61761dad85b1c32ea32479708f4098e51a76b9e94634e806ab6b, hashed before any site was
joined to an erosion value.

**What produced the numbers.** OCTOPUS v2.2 WFS `GetFeature`, all four 10-Be layers, globally,
no bbox (C43 used a CONUS bbox): 5,611 sites in 55 countries with a positive `EBE_MMKYR`. The
418 `crn_xxl` / `crn_inprep` records all carry `EBE_MMKYR = -9999.99` and contribute nothing.
Erosion from Borrelli et al. 2017 (`10.1038/s41467-017-02142-7`), continental means printed in
the article, plus Panagos et al. 2015 Table 1 per-country means for 11 European countries
(600 sites). `rho_b` = 1300 kg/m3.

**H1 passes:** median `Ha` = 0.4102, bootstrap 95% CI [0.3877, 0.4385], 3,787 of 5,611 below 1,
p = 1.5e-154; non-US n = 4,447, median 0.4631, p = 7.8e-90. Africa 0.027, Oceania 0.177, South
America 0.162, North America 0.284, Asia 0.618 — and Europe 3.29, which is an Alpine sampling
artefact (235 of 841 European sites are Swiss; excluding them gives 1.51).

**H2 was NOT TESTED, as the brief predicted in advance.** No country outside the US publishes a
per-site tolerable-loss layer; nothing was back-filled from the US result.

**The correction to how C43 should be read.** Against the published national numbers, median
`T`/`P` is 0.22–1.01 in Europe (Verheijen et al. 2009's proposed 0.3–1.4 t/ha/yr), 4.17–20.88
in the US (USDA `tfact` 1–5 short ton/ac/yr) and 10.10 globally (Borrelli's generic 10 t/ha/yr
`T`-value). C43's finding is therefore **local to the USDA convention** and is not a general
fact about tolerable-loss values: Europe's proposal is calibrated to measured formation where
the USDA's is 4–21x it. C43 is not wrong and nothing in it is withdrawn; what changes is the
scope of the claim it supports.

**Two access facts worth keeping.** The Borrelli 25 km GeoTIFF is behind an ESDAC registration
form ("Registration is requested: Yes") and was not obtained; the paper's Data Availability
names only the article and its SI, and no SI file carries a country table. So `E` is constant
within continent for 5,011 of the 5,611 sites, and every per-country `Ha` outside the 11
Panagos countries varies through `P` alone.

**One unregistered observation to treat as a hypothesis.** Where `E` does vary at country level,
Spearman rho(`P`, `E`) = +0.706 (n = 600, p = 1.4e-91) — a RUSLE product and 10-Be denudation
track each other hard, most plausibly because the DEM enters both. The brief named this failure
mode before the number was seen. It is the opposite sign to C43's rho(`T`, `P`) = -0.18.


## 2. Add to `vault/00-index.md`, in the computed-notes list, after the `C43` line


- [[C44-soil-ha-world]] — **the soil ledger, worldwide and site-level, and the limit of C43.** P-001 (Track A). Pre-registered (brief sha256 724ae903...) and run on **5,611 OCTOPUS ¹⁰Be sites in 55 countries**, no bbox, joined to Borrelli 2017's erosion rates. **H1 passes:** median `Ha` = `P`/`E` = **0.410** (CI [0.388, 0.439]; 3,787/5,611 below 1, p = 1.5e-154); non-US median 0.463. Negative on five of six continents — Africa 0.027, Oceania 0.177, South America 0.162, North America 0.284, Asia 0.618 — with **Europe 3.29 an Alpine sampling artefact** (1.51 without Switzerland). **H2 NOT TESTED and not back-filled**: no country outside the US publishes a per-site tolerable-loss layer. Its replacement is the finding — median `T`/`P` is **0.22–1.01 in Europe** (Verheijen 2009's proposed 0.3–1.4 t/ha/yr), **4.17–20.88 in the US** (USDA `tfact` 1–5) and **10.10 globally** (Borrelli's generic `T`), so **C43's anti-correlation is local to the USDA convention, not a fact about tolerable-loss values**; Europe's proposal is calibrated where the USDA's is 4–21× measured formation. Land use still beats geography: cropland `Ha` 0.078 against forest 6.19, a factor of 79, versus 23 across continents. Access facts: the Borrelli 25 km GeoTIFF is behind an ESDAC registration form, so `E` is constant within continent for 5,011 sites; and unregistered, ρ(`P`, `E`) = **+0.706** where `E` varies at country level — a RUSLE product and ¹⁰Be denudation share the DEM, the opposite sign to C43's ρ(`T`, `P`) = −0.18


## [2026-09-05] simulation | C25's Whittle rule run forward in a 20-patch network: 3 of 5 pre-registered predictions fail, the fast/slow GUD ratio is 1.06 not 1.34, and the value of the index is -0.5%

Programme item P-053, pre-registered against `audits/blind-brief-c45-2026-09-05.md`, sha256
fbc48359b5215f6a3f2c4f6cefee4ce7a73257c7c8121c33ef8615f0d49714a7, written and hashed before
`vault/_scripts/c45_whittle_sim.py` existed. Complete graph, N = 20 (10 fast, 10 slow), uniform
travel tau, dt = 0.01, burn-in 200, 1000 scored time units, 20 seeds, four policies. P1 FAILS:
the fast/slow giving-up-density ratio under the Whittle rule is 1.0600 +/- 0.0002 against a
pre-registered 1.30 +/- 0.10. P4 FAILS with the wrong sign: the Whittle policy earns -13.27%
+/- 0.03% against MVT-with-regrowth at the pre-registered calibration, negative in all twelve
sweep cells (-11.7% to -45.9%), and -0.48% +/- 0.03% when each policy is given its own post-hoc
rate-optimal threshold. P2 fails on the letter (MVT ratio 0.9975 +/- 0.0002, CI misses 1.000 by
0.25%, a dt overshoot) and passes on the substance. P3 PASSES: the type-ranking flips across
transit on 0.119 / 0.274 / 0.337 of departures at tau = 0.5 / 1 / 2, monotone increasing as
predicted -- C25 section 9 item 2 measured for the first time. P5 PASSES exactly: 100.00%
destination agreement with fullest-greedy in a homogeneous network at all four r.

What was wrong, and it is a calibration, not the network. C25 section 5 anchors the habitat
subsidy at nu = lam*GUD_MVT^2 = 0.09; the brief pre-registered nu as the learned long-run intake
rate, which the fixed point returns as 0.2732. Re-run at C25's own anchor, the single-patch
table survives the network to 0.8%: GUD_fast = 0.3987 against C25's 0.4019, GUD_slow = 0.3138
against the small-r expansion's 0.3163, ratio 1.2708 +/- 0.0002 -- inside the brief's band. So
C25 section 7's third hole ("nu is anchored, not solved") is the whole of the discrepancy, and
C25's 1.34 must be read as "1.34 at the MVT anchor". Two further results the brief did not ask
for: at r_fast*tau = 10 the forager visits slow patches ZERO times in every scored run, so the
between-type contrast P-067 wants is undefined at large regrowth contrast and the usable window
is r_fast*tau in [0.2, 1]; and "visit the fullest" with no leaving rule is not a policy at all
-- it earns 0.0098, 3.1% of the MVT rate, with a residence of exactly one dt, which sharpens
C25 section 5's degeneracy into a statement about the destination half only. Expected effect
size for P-067 is now 1.27, not 1.34.


## 2. For `vault/00-index.md`, in the `## Computed` list


- [[C45-whittle-network-sim]] — **P-053: the C25 index run forward as a policy, and 3 of 5 pre-registered predictions fail.** Pre-registered (brief sha256 `fbc48359...`). 20 patches, 10 fast / 10 slow, complete graph, uniform `τ`, 20 seeds. Fast/slow GUD ratio **1.0600 ± 0.0002** against a briefed 1.30 ± 0.10 (**P1 FAIL** — only the sign transfers), and the **value of the index is negative**: −13.27% ± 0.03% against MVT-with-regrowth at the pre-registered calibration, negative in all twelve sweep cells, **−0.48% ± 0.03%** at each policy's own rate-optimal threshold (**P4 FAIL, wrong sign**). The discrepancy is located exactly and it is *not* the network: at C25's own anchor `ν = λ·GUD_MVT² = 0.09` the single-patch table survives to **0.8%** (`GUD_fast` 0.3987 vs 0.4019) and the ratio is **1.2708 ± 0.0002**, inside the band — so C25 §7's "`ν` is anchored, not solved" is the whole of it. **P3 PASS**: type-ranking flips across transit on 0.119 / 0.274 / 0.337 of departures at `τ` = 0.5 / 1 / 2, C25 §9's transit reordering measured. **P5 PASS**: 100.00% destination agreement with fullest-greedy in a homogeneous network — but fullest-greedy alone earns 3.1% of the MVT rate, so the degeneracy is about the *destination* half only. For P-067: expected effect size **1.27**, usable window `r_fast·τ ∈ [0.2, 1]` — at `r_fast·τ = 10` slow patches receive **zero** visits and the contrast is undefined


## [2026-09-05] negative control | The reservoir audit CAN return nothing: blind D.1 run on a Betz-calibrated turbine returns NO RESIDUAL at step 11, a third null state distinct from both step-0 halts

First negative control of [[reservoir-audit]] run against a brief archived and hashed before
the run (`audits/blind-brief-c46-2026-09-05.md`, sha256 5e39ef6f84ed2c6eec4b17c434a6db7717683744
df1bf099983c36c0ca922308; five-line D.3a template, no verdict word, no D-class label). Case: a
90 m rotor reporting 2.0 MW at 11 m/s, rho = 1.225, stated C_p = 0.44. All thirteen steps ran,
none skipped. P_avail = 5.1863 MW (script `vault/_scripts/c46_betz.py`), Betz ceiling 3.0734 MW,
required C_p = 0.3856 = 0.651 of Betz, A = 0.386 at the swept disc (0.193 at 2x aperture, 0.771
at 0.5x). Ambient flow SURVIVES with a required property the stated C_p already supplies; the
gravitational, geomagnetic and thermal candidates are NOT FORMABLE (Delta u = 0 or undefined);
no second reservoir demanded. The -0.282 MW aerodynamic-to-electrical gap is a drivetrain
efficiency of 0.876, already in the published loss budget. What was wrong: Part D assumed the
audit's null output would be a halt. It is not — `NO RESIDUAL` fires at step 11 after a complete
run, and is a distinct third state from D.2's `NO OBSERVABLE TO EXPLAIN` (step-0(a) halt) and
D.3's `NO AGREED OBSERVABLE` (step-0(b) halt, C30). Two caveats logged, not buried: the blind is
single-agent (the brief was written by the agent that ran it — weaker than D.3a's two-agent
design, stronger than C30's pre-announced halt), and the case is textbook and was recognised on
sight. New failure mode F9: for a generator, F_req = P_useful/v at step 2 forces Sigma = 1 at
step 8, so the energy leg is not merely weak (F1) but a tautology that can never fire.


## 2. For `vault/00-index.md`, in the `## Computed` list


- [[C46-reservoir-audit-negative-control]] — **the audit's first negative control, run blind against a hashed brief.** A Betz-calibrated 90 m turbine: `P_avail = 5.186 MW`, Betz ceiling `3.073 MW`, required `C_p = 0.3856` (0.651 of Betz), `A = 0.386` at the swept disc and `0.193 / 0.771` at 2× / 0.5× aperture. The ambient flow `SURVIVES` with a property the stated `C_p = 0.44` already supplies; **no second reservoir demanded, no residual**. Answers Part D: the audit *can* return nothing — but `NO RESIDUAL` fires at **step 11 after a full run**, a third null state distinct from both step-0 halts. Blind is single-agent and the case is textbook, so the datum is weaker than D.3a asks for. New F9: on generator-form inputs `Σ = 1` identically


## 3. Proposed one-paragraph update for `reservoir-audit.md` Part D (PROPOSED ONLY — not applied)

To be inserted in Part D, after D.1's "What would count as a failure" paragraph:


**D.1 — RUN, 2026-09-05: [[C46-reservoir-audit-negative-control]].** A 90 m rotor at 11 m/s
reporting 2.0 MW with a stated `C_p = 0.44`, briefed on the D.3a five-line template archived and
hashed before dispatch (`audits/blind-brief-c46-2026-09-05.md`). All three D.1 conditions are
met: `A = 0.386 ≤ 1` at the swept disc and consistent with the accounted value (`0.193 / 0.771`
at 2× / 0.5× aperture), the step-11 union is non-empty and already occupied by the stated `C_p`,
and no second reservoir is demanded. **The instrument can return nothing — but not in the shape
this section predicted.** Part D assumed a null would be a halt; the D.1 null is `NO RESIDUAL`,
fired at **step 11 after all thirteen steps ran**, and it is a third state distinct from D.2's
`NO OBSERVABLE TO EXPLAIN` and D.3's `NO AGREED OBSERVABLE`, which are both step-0 refusals to
audit. It should be named as a state alongside step 10's four. Two things the datum does not
establish, both stated in C46 §4: the blind was **single-agent** — the brief was written by the
agent that ran it, which removes pre-announcement but not recognition — and the case is
**textbook**, so it exercises the arithmetic path rather than the judgement. The next D.1-class
case must be one the agent cannot recognise as resolved: a published Betz-exceeding
diffuser-augmented turbine claim (`C_p` normalised to throat rather than exit area) or a
low-head hydro efficiency claim above its ceiling, briefed by a different agent. C46 also
returns **F9**: for a generator, `F_req = P_useful/v` at step 2 makes `Σ = 1` at step 8
identically, so the energy leg is a tautology, not merely weak.

## [2026-09-05] computed | The Whittle GUD ratio is 1.27 at the MVT anchor and 1.06 with the subsidy learned, and the index does not out-earn Charnov's rule in a 20-patch network

C45 ran C25's §5 rule forward as a policy on a complete graph of N = 20 patches (10 fast, 10
slow, uniform travel, lambda = 1, G_max = 1, dynamics exactly C25 §1) against a pre-registration
hashed before the script existed. What was wrong: C25's callout advertised "~1.34x the MVT
giving-up density" without saying that the number is a ratio *at the MVT anchor*
nu = lambda·GUD_MVT^2 = 0.09. Sweeping nu moves the ratio 1.02 -> 1.66. At C25's own anchor the
network returns GUD_fast = 0.3987 against C25's single-patch 0.4019 (0.8%) and a ratio of
1.2708 +/- 0.0002; at the pre-registered calibration (nu learned as the realised long-run intake
rate, 0.2732) the ratio is 1.0600 +/- 0.0002. What it is now: the sign is calibration-free, the
magnitude is not, and the field prediction is a between-type GUD ratio in [1.06, 1.27] at
r·tau = 0.2, with a usable design window r_fast·tau in [0.2, 1] — at r_fast·tau = 10 the forager
makes zero slow-patch visits and the ratio is undefined. The harder result: Whittle loses to
MVT-with-regrowth on intake in all twelve sweep cells, by -13.27% +/- 0.03% at the pre-registered
calibration and -0.48% +/- 0.03% when each policy gets its own rate-optimal threshold. C25 §7's
"no optimality gap is stated" is therefore not an abstract caveat; the gap is measured and
negative. The "value of the index" framing is dropped from C25 and the paper: what survives is
dGUD/dr > 0 and the between-type contrast. The derivation is untouched — W(x) = lambda·x^2 −
r(1−x)^2 is still the Whittle index of the relaxed arm, still unconditionally indexable, still
reduces to C5 eq. (4) under non-revisitability. Produced by `vault/_scripts/c45_whittle_sim.py`,
20 seeds, brief `audits/blind-brief-c45-2026-09-05.md`.


## 2. For `vault/log.md`


## [2026-09-05] method | The paper now states the field prediction as a ratio band [1.06, 1.27] and makes no claim of improved intake

Propagation of C45 into `papers/charnov-gittins/paper.md`. Three minimal edits, no number in the
derivation or in Table 1 changed. Section 3's falsifiable-statement paragraph gains one sentence
giving the network results (1.271 at the MVT anchor, 1.060 with nu learned) and states the
quantity to power for as a between-type GUD ratio in [1.06, 1.27] at r·tau = 0.2, not a single
number. Table 1's caption now says the GUD/GUD_MVT column is a ratio *at this anchor*.
Limitations item 3 (the optimality gap) records that the gap is simulated and negative — the
Whittle policy loses 13.3% at the pre-registered calibration and 0.5% at rate-optimal thresholds
— and states explicitly that no claim of improved intake is made. What was wrong: the paper's
Section 3 could be read as asserting that a forager using W does better than one using R*. It
never derived that, and it is now measured false in the one network where it has been checked.


## 3. For `vault/log.md`


## [2026-09-05] negative control | The reservoir audit CAN return nothing: NO RESIDUAL is a third output state, fired at step 11 after a full run, and F9 says the energy leg is a tautology for generators

Part D of `vault/method/reservoir-audit.md` gains D.4 and the F-list gains F9, both from
[[C46-reservoir-audit-negative-control]]. What was wrong: Part D assumed the instrument's null
output would be a halt. It is not. On a 90 m rotor at 11 m/s reporting 2.0 MW with a stated
C_p = 0.44, briefed on the D.3a five-line template archived and hashed before dispatch
(`audits/blind-brief-c46-2026-09-05.md`, sha256 5e39ef6f84ed2c6eec4b17c434a6db7717683744df1bf099
983c36c0ca922308), all thirteen steps ran and none was skipped: P_avail = 5.1863 MW (script
`vault/_scripts/c46_betz.py`), Betz ceiling 3.0734 MW, required C_p = 0.3856 = 0.651 of Betz,
A = 0.386 at the swept disc and 0.193 / 0.771 at 2x / 0.5x aperture. The ambient flow SURVIVES
with a property the stated C_p already supplies, gravitational / geomagnetic / thermal candidates
are NOT FORMABLE, no second reservoir is demanded, and the -0.282 MW aerodynamic-to-electrical
gap is a drivetrain efficiency of 0.876 already in the published loss budget. What it is now:
NO RESIDUAL fires at step 11 after a complete run and is a distinct third state from D.2's
NO OBSERVABLE TO EXPLAIN and D.3's NO AGREED OBSERVABLE, both step-0 halts; it is named in Part D
as a state alongside step 10's four. This is the first input on which the instrument has been
shown to return nothing unprompted, and it is a weak yes: the blind is single-agent (the brief
was written by the agent that ran it) and the case is textbook (the worked example of the Wind
Energy Handbook), so it exercises the arithmetic path, not the judgement. Step 0(a) also had to
be improvised — the brief gave no uncertainty and the run assigned +/-3%. Next D.1-class case
named and it must be briefed by a different agent: a published Betz-exceeding diffuser-augmented
turbine claim whose C_p is normalised to throat rather than exit area. New failure mode F9: for a
generator, step 2's F_req = P_useful/v is divided straight back out by step 8, so Sigma = 1
identically and the energy leg can never fire — not merely weak (F1) but tautological. Fix
recorded: on generator-form inputs skip the energy leg and say so, or state a non-tautological
F_req measured independently of P_useful. The Standing paragraph's condition count goes five to
six to carry that fix.


## 4. For `vault/log.md`


## [2026-09-05] correction | C43's T-vs-P anti-correlation is a fact about the USDA tfact assignment rule, not about tolerable-loss standards in general

[[C44-soil-ha-world]] supplies the control group C43 lacked, and C43 gains a "Scope 2026-09-05"
paragraph restating its claim. What was wrong: C43 could be read as "tolerable-loss values
overstate soil formation." What it is now: the USDA's does, and its European counterpart does
not. Across 600 sites with a European per-country erosion number, Verheijen et al. 2009's
proposed range gives median T/P = 0.22 at its 0.30 t/ha/yr lower bound and 1.01 at its
1.40 t/ha/yr upper bound — calibrated to measured formation, or conservative — while the same
pipeline puts USDA tfact = 1 at 4.17 [3.42, 4.87] and tfact = 5 at 20.88 [17.11, 24.39] over
1,164 sites, bracketing C43's own per-site median of 22.3. The mechanism is C43 §3's, now with a
control: Verheijen's range was derived from the soil-formation literature and tfact was assigned
from profile depth and fragility. Borrelli et al. 2017's "generic T-value" of 10 Mg/ha/yr sits at
median T/P = 10.1 over 5,611 sites — the USDA-shaped convention carried into global erosion
modelling. Produced by `vault/_scripts/c44_world.py`; OCTOPUS v2.2 WFS and Panagos et al. 2015
Table 1, both fetched 2026-09-05.

## [2026-09-05] correction | C43's Spearman rho(T,P) = -0.180, p = 4.5e-9 withdrawn: spatial pseudoreplication and a slope confound

**Was.** C43 reported "Spearman rho(`T`, `P`) = -0.180 (p = 4.46e-9)" as a pre-registered H2 pass
in its strong form, concluding "`T` does not merely overstate formation; across sites it runs
**the wrong way**", and C35's blockquote called this "the one candidate here for a genuinely new
empirical claim".

**Is.** The correlation does not survive declustering or a gradient control, and it reverses on
low-gradient land. Re-analysis of C43's own cache (`_scripts/c43_data/sites.json`, 1,053 rows,
C43's own `spearman`/`median`/`boot_ci`, seed 20260905, 2026-09-05):

- 0.5-degree cell medians, n = 189: **rho = -0.041, p = 0.58**; 1-degree, n = 100: **+0.023,
  p = 0.82**
- cluster bootstrap over the 48 source studies, 2,000 draws: **95% CI [-0.341, +0.053]**;
  study-median rho(`tfact`,`P`) = -0.202, **p = 0.17**
- rank-partial controlling `SLP_AVE`: **rho(`tfact`,`P` | slope) = -0.074** (from -0.206)
- **sign reversal** on low-gradient basins: `SLP_AVE` < 150, **rho(`tfact`,`P`) = +0.172,
  p = 0.0031**; `SLP_AVE` < 100, **+0.237, p = 0.0014**. The negative rho lives only in
  `SLP_AVE` >= 300 (rho(`T`,`P`) = -0.276)
- the largest correlation in the dataset is one C43 never reported: **rho(slope, `P`) = +0.610,
  p = 2.1e-108**

**What produced the new number.** No new data. The C43 cache re-analysed with three additions
C43 did not run: spatial aggregation, a cluster bootstrap over source studies, and stratification
on the `SLP_AVE` field C43 already carried in `sites.json`. The mechanism is now read as
topographic — steep basins denude fast and carry thin, low-`tfact` soils — not as an artefact of
the assignment rule. H2's honest pre-registered outcome is **"no relation detected"**, not a pass.

Two dependent numbers fall with it. C43 section 3's "`tfact` = 1 is calibrated, median `T`/`P` =
0.93" is a steep-catchment artefact: only 7 of the 99 `tfact` = 1 sites are low-gradient and on
those the median is **12.40**. And section 3's `tfact`-class ratio column is largely forced —
shuffling `P` at random still yields rho(`tfact`, `T`/`P`) = **+0.255** [0.204, 0.298] against an
observed +0.376, because `T` is proportional to `tfact` by construction.

**Independently confirmed.** [[C47-tfact-mechanism-test]], pre-registered and run the same day on
114 ¹⁰Be outcrop sites C43 did not use, finds **rho(`tfact`, `P`) = +0.090, p = 0.34, 95% CI
[-0.095, 0.269]** — C43's -0.206 lies **outside** that interval — and its partial rho controlling
`slope_r` is +0.075. Two independent routes, this re-analysis and C47's fresh sites, kill the
same number.

**What does not fall.** C43's H1. Median `T`/`P` over 189 0.5-degree cells is **23.98**
[12.11, 34.44] with **90% of cells above 2**; study-median 7.89, 83% of 48 studies above 2. The
magnitude survives every specification tried.

---

## [2026-09-05] correction | "T is assigned on profile depth, not formation" is 44-year-old prior art, not this project's

**Was.** C43 section 3 and C35's blockquote presented the depth-based assignment of `T` as the
project's own mechanism, discovered in the data.

**Is.** It is the founding complaint of the `T`-value critique literature. Crossref-verified
2026-09-05 (`api.crossref.org`, `mailto=deciduusleaf@gmail.com`):

- Skidmore 1982, *Soil Loss Tolerance*, `10.2134/asaspecpub45.c8` — chapter 8 of an edited ASA
  volume titled *Determinants of Soil Loss Tolerance* (companions `...c6`, `...c11`)
- Schertz 1983, *The basis for soil loss tolerances*, `10.1080/00224561.1983.12436238`,
  J. Soil Water Conserv. 38(1):10-14, `is-referenced-by-count` = **45**
- Johnson 1987, *Soil loss tolerance: Fact or myth?*, `10.1080/00224561.1987.12456064`,
  J. Soil Water Conserv. 42(3):155-160, count = **25**
- Alexander 1988, *Rates of soil formation: implications for soil-loss tolerance*,
  `10.1097/00010694-198801000-00005`, Soil Science 145(1):37-45, count = **61**

USDA-facing documentation states the rule plainly: 5 ton/ac/yr for rooting depth above 5 ft,
reduced for shallower soils. Montgomery 2007, C35's own source, already reports that others hold
`T` values are set above soil production rates for political and economic reasons.

Two comparisons of a tolerable-loss value against cosmogenic rates also predate this vault:
**Stockmann et al. 2014** (`10.1016/j.geoderma.2013.10.007`, Geoderma 216:48-61 — note the
container correction C43 already logged) draws 5 and 12 t/ha/yr tolerance lines on a TCN
soil-production distribution, and **Quarrier et al. 2023** (`10.1130/G50667.1`, Geology
51(1):44-48) measures in-situ 10Be at 14 midwestern prairie sites and frames it explicitly
against the ~1 mm/yr USDA soil loss tolerance, arguing cosmogenic nuclides should redefine
tolerable erosion. **Kwang et al. 2023** (`10.1029/2022EF003104`) couples gSSURGO to a formation
rate for a ~25x national ratio.

**What is left.** Europe PMC bare-quoted, 2026-09-05: `"soil loss tolerance" AND "cosmogenic"`
returns **1** hit (Montgomery 2007); `"tolerable soil loss" AND "10Be"` returns **1** (the same);
`"soil loss tolerance" AND "soil production rate"` and `"tolerable soil loss" AND "denudation"`
return **0**. A site-level statistic between a *spatially varying* `tfact` and varying 10Be rates
does appear unpublished — but the statistic this project produced is the one withdrawn above.
Grade for the mechanism: **REDISCOVERED**. `Ha` stays REPACKAGED.

**Also unmeasured.** C43's SDA query returns `comppct_r`, `tfact` and `dbthirdbar_r` and no depth
field, so "depth anti-correlates with formation" was never tested on C43's own points. One added
column (`component.brockdepmin` or `chorizon.hzdepb_r`) would test it.

---

## [2026-09-05] correction | The EU "by contrast" clause is circular, misattributed, and factually backwards

**Was.** "The EU's proposed tolerable rates sit at 0.2-1.0x measured formation" was used as a
contrast against the USDA, sourced to C44 section 6's Verheijen 2009 rows.

**Is.** Three independent failures, all verifiable:

1. **Circular.** Verheijen et al. 2009 (`10.1016/j.earscirev.2009.02.003`, Crossref-verified,
   `is-referenced-by-count` = 595) *defines* its upper limit as equal to soil formation and reads
   0.3-1.4 t/ha/yr off a review of European soil formation rates. Dividing it by a formation rate
   recovers its own construction. It is a **positive control on the pipeline**, not a contrast —
   which is how C44 section 6 should head those rows.
2. **Misattributed.** It is a review's recommendation, adopted nowhere. The EU's actual proposed
   number, **COM(2023)416 Annex I**, was "Soil erosion rate (tonnes per hectare per year)",
   criterion **"<= 2 t ha-1 y-1"**. The adopted **Directive (EU) 2025/2360** (OJ L, 26.11.2025,
   ELI `data.europa.eu/eli/dir/2025/2360/oj`, in force 16 Dec 2025) **deleted it**: erosion moved
   to Annex I Part B, "established at Member State level", column headed "non-binding sustainable
   target values", entry "Member States shall lay down their own maximum value". **As of 2026 the
   EU has no operative numeric tolerable soil loss value.** The JRC/EUSO 2 t/ha/yr is a reporting
   indicator; Panagos et al. 2015's ~1 t/ha/yr cites formation rates, i.e. the Verheijen lineage.
3. **Backwards.** European numbers *not* defined from formation land inside the USDA range. Run
   through C44's own pipeline (`c44_data/sites.json`, rho_b = 1300 kg/m3) against the 89 German
   OCTOPUS sites, median `P` = 0.0443 mm/yr: EU-proposed 2 t/ha/yr → `T`/`P` = **3.47**; Swiss
   VBBo 2 and 4 → **3.47** and **6.94**; Lower Saxony's operative 13 t/ha/yr harmful-change
   trigger → **22.56**, against C43's US headline of 22.3. And **Switzerland's VBBo (SR 814.12)
   Annex 3 — the one operative European tolerable-erosion table — assigns its value by rootable
   soil depth** (2 t/ha/yr up to 70 cm, 4 above), which is the very rule the withdrawn sentence
   presented as the USDA's distinguishing defect.

**What produced the new numbers.** EUR-Lex and the COM(2023)416 annexes PDF read 2026-09-05;
VBBo Annex 3 and BBodSchV 2023 section 9 / DIN 19708 located the same day; the `T`/`P` column
computed from C44's existing cache. **C44's finding restated correctly:** numbers *defined from*
soil formation match soil formation; numbers not so defined — USDA, EU-proposed, Swiss, German —
sit at **3-23x** measured rates, on both continents. It is not a US-versus-Europe contrast.

---

## [2026-09-05] method | Cluster-bootstrap and spatial declustering added to the depth-gate checklist for any site-level join

C43 is the first note in this vault to compute an inferential p on thousands of geographic points
drawn from a compilation of other people's field campaigns. Its p = 4.5e-9 was wrong by roughly
eight orders of magnitude for one reason: **the 1,053 sites are not 1,053 independent draws.**
Five source studies supply 29% of them; sites within a study share region, lithology, relief and
often the same SSURGO map units.

**Rule adopted.** Any future site-level join in this vault must, before quoting a p-value,
report (a) the number of independent source studies or spatial clusters, (b) the statistic
recomputed on cluster medians, and (c) a cluster bootstrap CI — and must fix the declustering
unit **in the pre-registration**, because on C43 that choice moves rho from -0.18 to +0.02.

**Second rule.** When a compilation carries a topographic field (`SLP_AVE`, relief, elevation),
its correlation with the outcome must be reported alongside the correlation of interest. C43
carried `SLP_AVE` in `sites.json`, never reported it, and it was the largest correlation in the
dataset (+0.610 with `P`) and the confound that killed the finding.

Companion to [[failure-modes]], which covers the ways a measured **zero** can be fake; this is the
way a measured **nonzero** can be fake.


## [2026-09-05] pre-registered non-replication | C43's mechanism does not reproduce: rho(tfact, P) = +0.090 on 114 independent sites

P-079 ran C43's *found-in-the-data* mechanism as a hashed pre-registered test
([[C47-tfact-mechanism-test]]). Brief `audits/blind-brief-c47-2026-09-05.md`, sha256
13a3dad415f32d327eb9666111e0c5268d380cbdd543730ae5e5077cfe6daad6, hashed before any new
site's tfact, restriction depth or erosion rate was fetched.

What was wrong: C43 §3 explained rho(T, P) = -0.180 by "T is assigned on profile depth and
fragility". Two things are now corrected. (a) The rule is a **two**-argument function, not
one: NSSH Part 618 Subpart B (Amended August 2024) Figure 618B-3 publishes three columns —
depth to limiting layer crossed with a renewability group — so depth alone predicts only
64.6% of tfact at 800 random CONUS points (37.7% at the 114 test sites), against 84.5% /
92.1% falling inside the three-column band. H1 fails its >=90% gate as "depth plus group".
(b) The consequence does not replicate. On 114 Portenga & Bierman 2011 Table DR2 bedrock
outcrop sites (GSA item 2011216, Figshare 10.1130/2011216, CC BY-NC 4.0), 3 dropped for
falling within 0.005 deg of a C43 site, rho(tfact, P) = +0.090 (p = 0.34, Fisher 95% CI
[-0.095, +0.269], which EXCLUDES C43's -0.206); rho(P, depth bin) = +0.026 (p = 0.78). H2
fails. H3 fails on one of two qualifying classes (tfact 2, rho(T, P) = +0.390, p = 0.025),
but within a class T varies only through bulk density, so that row is rho(1/rho_b, P), not
evidence that T tracks formation; on depth it is -0.178 (p = 0.32) and +0.048 (p = 0.79).

The pre-registered slope check exonerates the covariate rather than the claim: partial
rho(tfact, P | slope_r) = +0.075 against a raw +0.090, so there is no anti-correlation left
for terrain to explain on this sample.

What produced the numbers: `vault/_scripts/c47_tfact.py`, 1,626 USDA Soil Data Access point
queries (tfact, slope_r, comppct_r, dbthirdbar_r, MIN(corestrictions.resdept_r),
muaggatt.brockdepmin), all fetched 2026-09-05, cached in `_scripts/c47_data/`.

What this does NOT establish: power to detect -0.206 at n = 114 is 0.60, so one
non-replication is not a refutation; and the outcrop sample has median P = 0.0082 mm/yr with
IQR 0.0047-0.0178 against C43's median 0.0378, IQR 0.0141-0.1415 — P is nearly flat here, and
a flat variable cannot correlate. C43's primary result (median T/P = 22.3, falsifier did not
fire) is untouched. What C43 loses is its §3 explanation, which is now one dataset for and
one against.

Access facts logged: OCTOPUS supplies no usable independent US sites — `crn_xxl_basins` has 6
USA rows, all EBE_MMKYR = -9999.99, and `crn_inprep_basins` has 0. The GSA Data Repository
has moved to Figshare; `rock.geosociety.org/pub/reposit/2011/2011216.*` is 404 and the item
is found through the Figshare search API.


## For `00-index.md`, in the computed block after the `C46` line


- [[C47-tfact-mechanism-test]] — **P-079: C43's mechanism pre-registered and run on independent sites — H1 partial, H2 fails, H3 fails.** Brief sha256 `13a3dad4...`, hashed first. §1 verifies the rule from the primary source: NSSH Part 618 Subpart B (Amended August 2024) Fig. 618B-3 assigns `T` from **depth to a root-restricting layer crossed with a renewability group**, three columns, not one — so depth alone predicts **64.6%** of `tfact` at 800 random CONUS points and **37.7%** at the test sites, against **84.5% / 92.1%** inside the published band; C43 §3's "assigned on profile depth" is right in kind, too simple in form. On **114 bedrock-outcrop ¹⁰Be sites** (Portenga & Bierman 2011 Table DR2, Figshare `10.1130/2011216`, 3 dropped within 0.005° of a C43 site), **ρ(`tfact`, `P`) = +0.090, p = 0.34, Fisher 95% CI [−0.095, +0.269] — C43's −0.206 is outside it**, and ρ(`P`, depth bin) = +0.026, p = 0.78. The pre-registered slope covariate does **not** explain it away: partial ρ = **+0.075**. Within-class ρ(`T`, `P`) = +0.390 (n = 33, `tfact` 2) is ρ(1/ρ_b, `P`) by construction, and on depth the same classes give −0.178 and +0.048. Power vs −0.206 is **0.60**, and outcrop `P` is nearly flat (median 0.0082, IQR 0.0047–0.0178 mm/yr vs C43's 0.0378, IQR 0.0141–0.1415), so this is a non-replication, not a refutation. **C43's median `T`/`P` = 22.3 stands; its §3 explanation is now one dataset for and one against**


## [2026-09-05] computed | P-068: under Kadmon's measured LINEAR nectar renewal the Whittle index goes flat and C25's GUD sign reverses; test not run, both papers paywalled

C25-whittle-foraging derives `W(x) = λx² − r(1−x)²` under saturating passive dynamics
`ẋ = r(1−x)` and predicts `dGUD/dr > 0`. Its own §6 records, against interest, that
Kadmon (1992, Oecologia 92:552–555, 10.1007/BF00317848) measured renewal that is *linear*
and independent of standing crop. C48-kadmon-regrowth-test re-derives the rule for that law.
Result: the singular-arc gain `g(a) = λa(c+ν)/(λa+c)` has no interior stationary point for
any `ν ≠ −c`, so the Whittle index degenerates to the step function `W(x) = −c` on `(0,1)`,
`W(1) = λ` — flat, `dGUD/dc = 0`, and the destination rule collapses to C45's `fullest`
policy, measured there at intake 0.0098 against MVT's 0.3154. With travel explicit the
self-consistent cycle gives `GUD*(c) = max(a_MVT(λτ), 1 − cτ)` with `a_MVT` the `c`-free root
of `(1−a)/a + ln a = λτ` (= 0.3178 at `λτ = 1`), so `dGUD/dc = −τ` below the kink at
`cτ = 0.6822` and 0 above — **never positive**. C25 and C48 therefore disagree in *sign*
across C25's whole usable window. Produced by `vault/_scripts/c48_kadmon.py`; blind brief
`audits/blind-brief-c48-2026-09-05.md`, sha256
`4e6fe72f283fe1eb074d8f2f3e8e7f17b1b4a35ad640751360df7422b2941572`, hashed before any
access attempt. Consequence: P-068 cannot confirm C25 whatever the data say, and P-088
(programmed-refill array) is promoted from "the clean version" to the only version, now with
a linear-refill negative-control arm.

## [2026-09-05] verification | Kadmon 1992's linearity confirmed from the source abstract, via Europe PMC

Europe PMC REST, `EXT_ID:28313227`, `resultType=core`, fetched 2026-09-05, returned the
abstract of Kadmon (1992) Oecologia 92:552–555 (`inEPMC = N`, `isOpenAccess = N`): the rate
of nectar renewal is independent of the amount of nectar in the flower and the renewal
process is strongly linear; inter-arrival-time SD/mean 0.44–0.79. C25 §6's against-interest
remark was previously carried without a cited fetch; it is now sourced.

## [2026-09-05] correction | the Dreisig 1995 DOI in circulation is wrong: 10.2307/3545806 is McGeoch & Chown 1997

`10.2307/3545806` was carried into P-068 as Dreisig (1995) "Ideal free distributions of
nectar foraging bumblebees", Oikos. Crossref (`api.crossref.org/works/10.2307/3545806`,
fetched 2026-09-05) returns McGeoch & Chown (1997), "Evidence of Competition in a
Herbivorous, Gall-Inhabiting Moth (Lepidoptera) Community", Oikos 78:107. The correct DOI is
`10.2307/3546218` — Dreisig, Oikos 72:161, 1995-03 (Crossref, same fetch). Nothing in the
vault cited the bad DOI in a standing; it was reading-list only.

## [2026-09-05] honest null | Kadmon & Shmida 1992 is unobtainable through every permitted open route

`10.1007/BF02270708`: Unpaywall `is_oa = false` with 0 OA locations; Semantic Scholar
`openAccessPdf.status = CLOSED` with the abstract elided by the publisher; link.springer.com
returns HTTP 303 to `idp.springer.com/authorize`. All fetched 2026-09-05. Sci-Hub not used.
The P-068 empirical test was therefore **not run**, and C48 says so in its first ten lines.
Next cheapest move: Taneyhill (2010) Psyche 2010:872736, `10.1155/2010/872736`, which
Unpaywall reports open.


## 2. For `vault/00-index.md`, in the computed-notes list


- [[C48-kadmon-regrowth-test]] — **P-068: change one line of C25's model to the renewal law its own dataset obeys, and the prediction dies twice.** Pre-registered (brief sha256 `4e6fe72f...`, hashed before any access attempt). Under linear renewal `ẋ = c` the singular-arc gain loses the `a`-dependent term that made C25's index interior, so `∂g/∂a` never vanishes and **`W(x) = −c` on `(0,1)`, `W(1) = λ`** — a step function, flat, carrying no state and no rate information: `dGUD/dc = 0`, and the destination rule becomes [[C45-whittle-network-sim]]'s `fullest`, measured there at intake **0.0098** against MVT's 0.3154. With travel explicit, `GUD*(c) = max(a_MVT(λτ), 1 − cτ)`, `a_MVT` the `c`-free root of `(1−a)/a + ln a = λτ` (**0.3178** at `λτ = 1`, kink at `cτ = 0.6822`), so **`dGUD/dc = −τ` then 0 — never positive**, against [[C25-whittle-foraging]]'s `dGUD/dr > 0`, across the whole `r·τ ∈ [0.2, 1]` design window. **Not tested:** Kadmon & Shmida 1992 (`10.1007/BF02270708`) is unobtainable by every permitted route (Unpaywall 0 OA locations, S2 `CLOSED` with abstract elided, Springer 303 to an auth wall); Kadmon 1992 (`10.1007/BF00317848`) yielded an abstract only, via Europe PMC — which **confirms the linearity from the source**, so C25 §6's against-interest note is now sourced rather than inferred. §6 gives the ten-column table a human with library access fills in an hour, with the Spearman gate unchanged. Consequence: **P-088 is promoted from the clean version to the only version**, and gains a linear-refill negative-control arm that must return a ratio ≤ 1. Self-named first line of attack: Kadmon's linearity is measured *between forager arrivals*, so if bees hold flowers far from `G_max`, "linear" and "saturating" are the same law seen on its linear part and the degeneracy is an extrapolation artefact


## [2026-09-05] blind negative control | Mars methane has no single observable: step 0 returns four different verdicts, and the audit's one reproducible exclusion is a SINK at A = 319

[[C49-mars-methane-audit]], P-089 Track C, run against a brief written and hashed before the run
(`audits/blind-brief-c49-2026-09-05.md`, sha256 34a7d8ee823c28b8c776a56d9bfeca62fae177650f8e9059
082274efaff2c424) that names no verdict, no halt and no D-class. What was assumed: that a case
carries one observable and step 0 returns one state. It does not. "Methane on Mars" is four
observables with four standings: the globally mixed background is TGO's <0.05 ppbv, an interval
containing zero, so 0(a) halts with NO OBSERVABLE TO EXPLAIN; the ground-based plumes are
Mumma 2009's 45 ppbv against Zahnle, Freedman & Catling 2011's re-reduction of the same spectra
to a telluric-subtraction artefact, so 0(b) halts with NO AGREED OBSERVABLE — F8's trigger on a
second case after Venus; the 2019 21 ppbv spike read globally needs 2.27e8 t/yr of removal
(tau = 7.1 h, A = 1.9e7) and is NOT FORMABLE as a global quantity; and only the Gale
near-surface seasonal observable (0.41 +/- 0.16 ppbv, 2.56 sigma, cycling 0.24-0.65) survives,
conditionally, on a condition Part C's step-0 table has no row for — one instrument, one team, no
independent reduction of the TLS records has ever been published, so 0(b) cannot be run at all.
What it is now, on that observable: burden 3,592 t (Mars atmosphere 2.367e16 kg = 5.461e17 mol),
steady-state maintenance 11.97 t/yr against a 300-yr photochemical lifetime, but the seasonal
amplitude needs 3,820 t/yr in each direction and an effective residence time of 0.944 yr —
318x shorter than photochemistry — derived from the amplitude and the Mars year alone, with no
chemistry, and matching Lefevre & Forget 2009's "shorter than 1 year" independently. Gas-phase
photochemistry is RULED OUT at A = 319 and survives the 2x aperture row. Every SOURCE passes:
UV degradation of meteoritic/IDP organics at A = 0.164 for the background (over-sufficient 6x)
but RULED OUT at A = 52.3 for the seasonal amplitude, serpentinisation microseepage at
A = 0.025 on Oehler & Etiope 2017's own 30,000 km2 Nili Fossae aperture and 5 t/km2/yr,
clathrate / volcanic / biological all NOT TESTED for want of a published flux bound. The residual
is therefore not a source: a surface reservoir exchanging CH4 in BOTH directions at >= 3,820 t/yr
per phase, season-locked, 0.072 mg/m2/day planet-wide — two to three orders BELOW terrestrial
microseepage, so capacity is not the problem and the sign alternation is. Calibration against
Yung et al. 2018 (full-text-read, Europe PMC PMC6205098): five routes, two matches (tau_eff, the
IDP 5-6x over-prediction), two tautological rows that are Yung's own numbers re-divided (the
C30 lesson, applied to this note's own margins), and one located divergence — Yung's 75,000 t/yr
for the ~7 ppbv spike against this note's 7.36e5 t/yr, a factor of 9.8 that is entirely the
local-vs-global aperture, F3 made checkable. New output shape, proposed to the method note but
not yet written into it: on a mass budget the SOURCE leg's aperture is free and the SINK leg's is
fixed by the observable (P_avail = burden/tau), so source rows carry no information and only sink
rows are reproducible between analysts — proposed as F10, with source rows reported
NOT DISCRIMINATED rather than SURVIVES. Also proposed: a sixth step-10 state EXCHANGE REQUIRED
for periodic observables whose residual is two-signed; a fourth step-0 condition
UNREPLICABLE OBSERVABLE; and a step-1 diagnostic that A >> 1e4 reports a mis-specified observable
rather than an excluded reservoir. Honesty: the blind is single-agent, the case is recognisable,
the case-line numbers are the brief's rather than a fetch, and Moores 2019 and Webster 2021 — the
two papers the whole step-0 verdict turns on — are Crossref-verified but NOT full-text-read.
Arithmetic: `vault/_scripts/c49_mars.py`.


## [2026-09-05] negative control | D.2 fires: the audit halts at step 0(a) on (0.4 ± 3.0) µN, enumerating nothing

The reservoir audit's D.2 negative control was run for the first time
([[C50-reservoir-audit-d2-control]]). Input: a fabricated bench thruster reporting
F = 0.4 µN with 1σ = 3.0 µN at 50 W — 0.13σ, interval containing zero. Part C step 0(a)
fired `NO OBSERVABLE TO EXPLAIN` and the run stopped there: no F_req, no candidate list,
no aperture, no A, no Σ, no residual. Brief archived and hashed before dispatch at
`audits/blind-brief-c50-2026-09-05.md`, sha256
fae035f866bf1bbfa4136b6f3dc44c26d57a98743091b69174f451e44ac97ca6.

What is new: three null states are now observed at three distinct steps — 0(a) halt (D.2,
this run), 0(b) halt (D.3, C30), step-11 `NO RESIDUAL` after a full run (D.1, C46). Also
settled by reading the procedure: the conditional-run licence belongs to step 0(b) only, so
computing the photon-rocket bound P/c = 0.167 µN after a 0(a) halt is not permitted and is
recorded as a temptation, not an output.

What this does not establish: the brief labelled the case synthetic in its first line, so the
datum tests the wording of step 0(a), not the instrument's judgement; and the blind was
single-agent again. Next case named: Tajmar et al. 2021, doi:10.1007/s12567-021-00385-1
(Crossref, fetched 2026-09-05), briefed by a different agent on its reported thrusts and
uncertainties alone.

## [2026-09-05] correction | C43's rho(T,P) = -0.180 withdrawn: spatial pseudoreplication, a slope confound, and a failed replication

**Was.** [[C43-soil-ha-replication]] reported "Spearman rho(`T`, `P`) = -0.180 (p = 4.46e-9)" as a
pre-registered H2 pass in its strong form — "`T` does not merely overstate formation; across sites
it runs the wrong way" — and [[C35-soil-ha]] §5 called it "the one candidate here for a genuinely
new empirical claim".

**Is.** Withdrawn. `audits/c43-adversarial.md` re-analysed C43's own cache
(`_scripts/c43_data/sites.json`, 1,053 rows, C43's own `spearman`/`median`/`boot_ci`, seed
20260905): 0.5-degree cell medians n = 189, **rho = -0.041, p = 0.58**; 1-degree n = 100,
**+0.023**; cluster bootstrap over the 48 source studies, 2,000 draws, **95% CI [-0.341, +0.053]**;
rank-partial on `SLP_AVE`, **rho(`tfact`,`P` given slope) = -0.074** (from -0.206); and the **sign
reverses** on low-gradient basins — `SLP_AVE` < 100, **+0.237, p = 0.0014**. The negative lives
only in `SLP_AVE` >= 300. The largest correlation in the dataset is one C43 never reported,
**rho(slope, `P`) = +0.610, p = 2.1e-108**. Independently, [[C47-tfact-mechanism-test]] (P-079,
pre-registered, 114 outcrop sites C43 did not use) returns **rho(`tfact`,`P`) = +0.090, p = 0.34,
95% CI [-0.095, +0.269]** — C43's -0.206 lies outside it. Two dependent numbers fall with it:
"`tfact` = 1 is calibrated, median `T`/`P` = 0.93" (12.40 on the 7 low-gradient sites of that
class) and §3's ratio column, which a full `P`-shuffle already reproduces at +0.255.

**What produced the new numbers.** No new data on the re-analysis leg: three specifications C43
did not run — spatial aggregation, a cluster bootstrap over source studies, and stratification on
the `SLP_AVE` field its own cache carried. Fresh data on the replication leg: C47's independent
sites. H2's honest pre-registered outcome is **"no relation detected"**, not a pass.

**What does not fall.** H1. Median `T`/`P` = **23.98** [12.11, 34.44] over 189 0.5-degree cells,
90% above 2; study-median 7.89, 83% of 48 studies above 2.

Applied to: C43 (top callout replaced, `## Withdrawal 2026-09-05` added, §3 mechanism paragraphs
marked withdrawn in place rather than deleted — the data and the join description are kept), C35
§5, [[novelty-audit]].

## [2026-09-05] correction | "T is assigned on profile depth, not formation" is 44-year-old prior art, and the surviving magnitude is published five times over

**Was.** C43 §3 and C35 §5 presented the depth-based assignment of `T` as this project's own
mechanism, found in the data.

**Is.** REDISCOVERED. Crossref-verified 2026-09-05 (`api.crossref.org`,
`mailto=deciduusleaf@gmail.com`): **Skidmore 1982**, *Soil Loss Tolerance*,
`10.2134/asaspecpub45.c8`, chapter 8 of a volume titled *Determinants of Soil Loss Tolerance*;
**Schertz 1983**, `10.1080/00224561.1983.12436238`, `is-referenced-by-count` = 45; **Johnson
1987**, "Soil loss tolerance: fact or myth?", `10.1080/00224561.1987.12456064`, count = 25;
**Alexander 1988**, `10.1097/00010694-198801000-00005`, count = 61. C47 further finds the rule is
depth **times a renewability group** (NSSH Part 618 subpart B §618.91), not depth alone — depth
alone predicts 64.6% of values at 800 random CONUS points. And C43 never fetched a depth field at
all: its SDA query returns `comppct_r`, `tfact` and `dbthirdbar_r`, so the causal clause was
asserted and measured nowhere in the note.

The magnitude that survives is published: **Montgomery 2007** (`10.1073/pnas.0611508104`),
**Stockmann et al. 2014** (`10.1016/j.geoderma.2013.10.007`), **Evans et al. 2020**
(`10.1088/1748-9326/aba2fd`), **Kwang, Thaler & Larsen 2023** (`10.1029/2022EF003104`), and at
site level for 14 midwestern prairies **Quarrier et al. 2023** (`10.1130/G50667.1`), which frames
in-situ 10Be explicitly against the USDA tolerance and argues cosmogenic nuclides should redefine
it. **The soil thread therefore yields no novel claim** — what it yields is a well-provenanced
re-computation, and C35 §5 now says so plainly.

**Novelty count unchanged at 3** (C5, C16/Q7, C4c): the withdrawn C43 statistic was carried in
[[novelty-audit]] as "NEW CANDIDATE, not yet graded NOVEL" and was never counted. Its entry is now
**WITHDRAWN / REDISCOVERED** and removed from the strongest-genuinely-novel list.

**Prior-art leg limitation, stated.** OpenAlex returned budget-exhausted and Semantic Scholar HTTP
429 throughout, so the leg is Crossref + Europe PMC + web and does **not** meet the C5 §11 bar.

## [2026-09-05] correction | The EU "by contrast" clause is circular, misattributed, and factually backwards

**Was.** "The EU's proposed tolerable rates sit at 0.2-1.0x measured formation", used as a
contrast against the USDA and sourced to [[C44-soil-ha-world]] §6's Verheijen 2009 rows.

**Is.** Three independent failures. **(a) Circular.** Verheijen et al. 2009
(`10.1016/j.earscirev.2009.02.003`, Crossref-verified, `is-referenced-by-count` = 595) *defines*
its upper limit as equal to soil formation and reads 0.3-1.4 t/ha/yr off a review of European
formation rates, so dividing it by a formation rate recovers its own construction — it is a
**positive control on the pipeline**, and §6 now heads those rows that way. **(b)
Misattributed.** It is a review's recommendation, adopted nowhere. The EU's actual proposal,
COM(2023)416 Annex I, was "<= 2 t ha-1 y-1", and the adopted **Directive (EU) 2025/2360** (OJ L,
26.11.2025, ELI `data.europa.eu/eli/dir/2025/2360/oj`, in force 16 Dec 2025) **deleted it**:
erosion moved to Annex I Part B, "established at Member State level", under a column headed
"non-binding sustainable target values". **As of 2026 the EU has no operative numeric tolerable
soil loss value.** **(c) Backwards.** Through C44's own pipeline (`c44_data/sites.json`,
rho_b = 1300 kg/m3) against the 89 German OCTOPUS sites (median `P` = 0.0443 mm/yr): EU-proposed
2 t/ha/yr gives `T`/`P` = **3.47**; Swiss VBBo 2 and 4 give **3.47** and **6.94**; Lower Saxony's
operative 13 t/ha/yr harmful-change trigger gives **22.56**, against C43's US headline of 22.3.
And **Switzerland's VBBo (SR 814.12) Annex 3, the one operative European tolerable-erosion table,
assigns its value by rootable soil depth** (2 t/ha/yr to 70 cm, 4 above) — the very rule the
withdrawn sentence presented as the USDA's distinguishing defect.

**What produced the new numbers.** EUR-Lex and the COM(2023)416 annexes PDF read 2026-09-05; VBBo
Annex 3 and BBodSchV 2023 §9 / DIN 19708 located the same day; the `T`/`P` column computed from
C44's existing cache. **C44's finding restated correctly:** numbers *defined from* soil formation
match soil formation; numbers not so defined — USDA, EU-proposed, Swiss, German — sit at **3-23x**
measured rates, on both continents. It is not a US-versus-Europe contrast. C44 §4's `rho = +0.71`
between country-level RUSLE erosion and 10Be denudation is recorded as the **DEM artefact the
brief predicted before the number was seen**, and its former reading as "the exact opposite of
C43's sign" is withdrawn with C43's sign.

## [2026-09-05] method | Cluster-bootstrap and spatial declustering added to the depth-gate checklist for any site-level join

C43 is the first note in this vault to compute an inferential p on thousands of geographic points
drawn from a compilation of other people's field campaigns, and its p = 4.5e-9 was wrong by
roughly eight orders of magnitude for one reason: **the 1,053 sites are not 1,053 independent
draws.** Five source studies supply 29% of them; sites within a study share region, lithology,
relief and often the same SSURGO map units.

**Rule adopted.** Any future site-level join must, before quoting a p-value, report (a) the number
of independent source studies or spatial clusters, (b) the statistic recomputed on cluster
medians, and (c) a cluster bootstrap CI — and must fix the declustering unit **in the
pre-registration**, because on C43 that choice moves rho from -0.18 to +0.02. **Second rule.**
When a compilation carries a topographic field (`SLP_AVE`, relief, elevation), its correlation
with the outcome must be reported alongside the correlation of interest: C43 carried `SLP_AVE`,
never reported it, and it was both the largest correlation in the dataset (+0.610 with `P`) and
the confound that killed the finding. Companion to [[failure-modes]], which covers the ways a
measured **zero** can be fake; this is the way a measured **nonzero** can be fake.

## [2026-09-05] method | Four additions to the reservoir audit from C49, and D.2's first datum from C50

[[reservoir-audit]] gained four things C49 proposed and one Part D revision C50 proposed; both
were staged as proposals and are now written into the method note.

From [[C49-mars-methane-audit]] (P-089): **(1) F10** — on a mass-budget input the **source**
aperture is free while the **sink** aperture is fixed by the observable (`P_avail` = burden/tau),
so source rows carry no information and are reported **`NOT DISCRIMINATED`**, never `SURVIVES`;
only sink rows are quotable as exclusions. C49's own case: photochemistry `RULED OUT` at
`A` = 319 reproducibly, against source rows running `A` = 0.164 to 52.3 depending on the aperture
chosen, and a factor-9.8 divergence from Yung et al. 2018 that is **entirely** local-vs-global
aperture. **(2) `EXCHANGE REQUIRED`**, a sixth step-10 state, for a **periodic** observable whose
amplitude no one-way reservoir can meet — C49's Gale seasonal cycle needs 3,820 t/yr in each
direction at tau_eff = 0.944 yr, 318x shorter than photochemistry. **(3) `UNREPLICABLE
OBSERVABLE`**, a fourth step-0 condition: one instrument, one team, no independent reduction ever
published, so 0(b) cannot be run at all — proceed **conditionally** and label everything. **(4)**
a step-1 diagnostic: **`A` >> 1e4 on an ordinary candidate reports a mis-specified observable, not
an excluded reservoir** (C49's global reading of the 2019 spike, `A` = 1.9e7). Step 0 also now
runs **per observable, not per case**: C49's four observables return four different states.

From [[C50-reservoir-audit-d2-control]] (P-093): **D.2 is run**, at step 0(a), on
`F = (0.4 +/- 3.0) uN` at 50 W — 0.13 sigma — with **nothing** enumerated. Part D's D.4 table
gains a **"ran before firing"** column with the three values *nothing* / *the reductions table
only* / *steps 0-10 in full*, which is what now distinguishes the three null states. The datum is
weak by construction: the brief labelled the case synthetic in its first line, so it validates the
wording of step 0(a), not the instrument's judgement, and the blind was single-agent again. Also
settled: the conditional-run licence belongs to **step 0(b) only**, so computing `P/c` = 0.167 uN
after a 0(a) halt is a temptation, not an output. **Next unlabelled cases named:** Tajmar et al.
2021 (`10.1007/s12567-021-00385-1`) for D.2, briefed by a different agent on its reported thrusts
and uncertainties alone; a Betz-exceeding diffuser-augmented turbine for D.1. Standing count
updated: step 10 now has six per-candidate states, plus `NO RESIDUAL` and three step-0 conditions,
and the procedure carries eight conditions rather than six.

## [2026-09-05] correction | C25's regrowth prediction is specific to saturating renewal; under linear renewal the index is a step function and the sign reverses

**Was.** [[C25-whittle-foraging]] §7 assumption 1 said that although Kadmon (1992) measured
**linear** renewal in *Anchusa*, "the derivation runs the same way with linear renewal but (3)
changes; the *sign* of (5) survives, the coefficients do not."

**Is.** It does not survive. [[C48-kadmon-regrowth-test]] carries the derivation out: under
`x_dot = c` up to a cap the Whittle index is **`W(x) = -c` on the interior (0,1) with
`W(1) = lambda`** — a **step function** with no `x`-dependence off the cap, so the Whittle policy
and MVT are **indistinguishable** as policies — and the comparative static is **`dGUD/dc <= 0`**,
the opposite sign to §5's `dGUD/dr > 0`.

**Consequences.** (a) **Kadmon 1992 cannot test the prediction**, which closes P-068 on its
negative branch, the branch the programme row named in advance. (b) **P-088 is promoted** and its
specification tightens: the artificial-flower array must implement **saturating** refill by
construction, and must carry a **linear-refill negative-control arm** — a null on the linear arm
checks the apparatus, a null on the saturating arm falsifies the transfer. (c) The saturating form
is now stated as a **boundary of the prediction** in C25 §5 and §7, and as a Limitations item in
`papers/charnov-gittins/paper.md`: *"The prediction is specific to saturating patch renewal; under
linear renewal the Whittle index degenerates to a step function and the regrowth effect vanishes
or reverses (vault C48). The Kadmon 1992 system, which measured linear renewal, therefore cannot
test it; a controlled-refill array can."*

## [2026-09-05] method | Seven programme items closed and their outcomes recorded

[[program]] gains a `## Done 2026-09-05` block: **P-001** (C44, world ledger, §6 corrected),
**P-053** (C45, ordering survives, magnitude calibration-dependent, optimality gap negative),
**P-068** (done on the negative branch, P-088 promoted), **P-079** (done, H2/H3 fail, C43
withdrawn), **P-089** (done, C49, four method returns), **P-092** (done, C46, `NO RESIDUAL`, F9),
**P-093** (done, C50, D.2 fires). Two of the seven closed by **failing**, which is the point of
having written the minus branch into the row before running it.

## [2026-09-05] computed | C51: nothing about a claim's subject predicts its survival — only the round it was made in, and that is confounded with how the outcome was read

Pre-registered meta-analysis of the vault's own graded record. Brief
`audits/blind-brief-c51-2026-09-05.md`, sha256
`8844d375b302b987d7bc83ebbb8f2e4157f26df7f93fd7bcdc6517ac697d786a`, hashed before any outcome
column was read or coded. 87 claims coded (C1–C22, C25–C50, G1–G37 as they exist, Q1–Q10),
82 graded, dataset at `_scripts/c51_data/claims.csv` with a per-row `source_line`.

Overall survival 26/82 = 0.317. Of four pre-registered hypotheses: **H1** (derivations and
catalogues outlive correlations) fails on n — direction as predicted, correlation perfectly
separated at 0/6, Fisher p = 0.1639 on n = 49. **H2** (famous pairs are more often prior art)
fails and reverses — famous 1/11 = 0.091 against obscure 18/71 = 0.254, p = 0.4430. **H3**
(post-blind-brief claims die at a higher rate) is falsified in direction — blind-brief claims
survive at 0.500 against 0.292, and the broader round variable gives post-audit 17/35 = 0.486
against early 9/47 = 0.191, Fisher p = 0.0078. **H4** (scale-mismatched data joins die) is
direction-only per the brief's own n gate: mismatch 0/3, same-scale 2/2, smaller margin 2.

Two findings the programme should act on and one it should not. Act on: computation on
already-published numbers is the weakest move at 3/16, while pre-registered enumeration (5/7)
and instrument runs (3/5) are the strongest — their honest null is still a publishable object.
And an adversarial pass is not a kill mechanism: survival with a pass 0.312, without 0.324;
what the passes did was convert `live` into `narrowed`, the fate of 26 of 82 claims. Do **not**
act on H3b as evidence the vault got better: early claims were graded mostly by the novelty
audit, post-audit claims mostly by their own callouts, and that difference in *how the outcome
was read* could manufacture the whole p = 0.0078. Said so in C51 §5.

Logistic model declared in the brief was not fitted: the counts gate passed but `correlation` is
completely separated on the outcome, so the MLE does not exist and a penalised fit would report
a coefficient the data do not contain.

New: `vault/computed/C51-vault-meta-analysis.md`, `vault/_scripts/c51_meta.py`,
`vault/_scripts/c51_data/claims.csv`, `audits/blind-brief-c51-2026-09-05.md`.


## 2. Add to `vault/00-index.md`

In the computed-notes section, after the C50 line:


- [[C51-vault-meta-analysis]] — across 82 graded claims, no property of a claim's subject
  predicts survival; only the round it was made in does, and that is confounded with how the
  outcome was read. Correlations 0/6; scale-mismatched joins 0/3; an adversarial pass moves
  survival by 1.2 points and moves `live` to `narrowed` instead.


C51 is unreachable by wikilink from `00-index.md` until this line lands, so `_lint.py` reports
one reachability WARNING against it in the meantime (a warning, not an error; lint still exits 0).
That warning is this file's whole reason to
exist; it clears the moment §2 is applied.

## 3. Gitignore exception required

`.gitignore` carries `vault/_scripts/*_data/`, which would swallow the coded dataset. Add,
immediately after that line:


!vault/_scripts/c51_data/


`c51_data/claims.csv` is the analysis's evidence and must be committed. This agent did not edit
`.gitignore`.


## [2026-09-05] honest null | C52: the mammal half of the setpoint→survival claim is Turbill 2011; the bird half cannot be run because the migrant rule empties its treatment arm

P-008 run against `audits/blind-brief-c52-2026-09-05.md`, sha256
`bc2259e6984a3895a199f3585dc11ffad496162af7a50cb65c79948cac9f2547` over all 14,767 bytes,
hashed before any adult-annual-survival value was fetched. Arithmetic
`python _scripts/c52_survival.py`; verify the brief with `--verify-brief`.

Prior-art check run BEFORE the join, as the brief required: Turbill, Bieber & Ruf 2011,
Proc. R. Soc. B, `10.1098/rspb.2011.0190` (Crossref 2026-09-05, `is-referenced-by-count` = 283;
abstract via Europe PMC, PMID 21450735) already reports that hibernators have ~15% higher annual
survival than similar-sized non-hibernators under phylogenetic GLS. **The mammal leg of the C38
§5 survival clause is REDISCOVERED**, not this project's. P-008 was written without knowing that
and should be rewritten to name Turbill 2011 as its baseline. Semantic Scholar returned HTTP 429
throughout, so the prior-art reach is Crossref + Europe PMC + web only.

The only new leg is birds. It does not run: of 27 British species with BTO ring-recovery adult
annual survival, exactly 3 appear in the Ruf & Geiser 2015 appendix (*Apus apus* φ = 0.808,
*Caprimulgus europaeus* 0.700 ± 0.05, *Delichon urbicum* 0.410) and all 3 are obligate
long-distance migrants, removed by a rule fixed in the hashed brief. Lever-bearing arm n = 0.
The lever-less arm is also n = 0, for an independent reason: the brief's asymmetric coding rule
requires an explicit negative from a second source, COMBINE covers mammals only, and no avian
compilation states homeothermy per species. **In temperate avifauna the metabolic lever and
long-distance migration are alternative solutions to the same winter energy problem, so any
migration-controlled test of the lever on birds removes its own treatment group.**

What was wrong before: C40's lever coding had to infer "lever-less" from absence in a
positive-record compilation. Under the asymmetric rule that refuses that inference, only
240 of 671 small (<100 g) temperate (|lat| ≥ 35°) Chiroptera/Rodentia/Eulipotyphla can be coded
at all — 24 lever-bearing, 216 lever-less, 425 UNCODED (63.3%), 6 conflicts
(`_scripts/c52_data/lever_codes.csv`, sha256
`e6554ce84043db91d1a996d0e54626be8126f31150948bbda68284f76e7be0e2`, written before any φ was
read). C40's 75-species table was reachable only by inferring the other ~64%.

φ sources: BTO BirdFacts worked (27/27 slugs; `pied-wagtail` HTTP 404). The Amniote database
(Myhrvold et al. 2015, `10.1890/15-0846R.1`) has **no** `adult_survival` field — asserted in code,
recorded as a negative result. No open mammal φ compilation was obtained. COMBINE
`max_longevity_d` was available as a pre-authorised downgraded proxy and was **not used**:
longevity was not substituted for φ, which is the failure C40 §6.1 discloses.

Void-by-construction control, reported so it is never quoted as a result: under the two moves
the brief forbids (code lever-less by absence, keep migrants) the same data give a naive
Δφ = +0.147, which the brief's own 2× mass matching alone reduces to +0.059, bootstrap 95% CI
[−0.132, +0.295] (seed 20260905), sign test 2/3, p = 0.500, gate not met at 3 pairs.

P-072 falsifier: 8 Europe PMC formulations found no new lever-less species with a published
reserve margin. Count of lever-less species with a published margin remains 1 (*Sorex araneus*,
−69%); above +100%: 0. NOT FALSIFIED over a reach of n = 1 — P-072's own quotability condition
(a ≥10-candidate scan) is not met, so the falsifier is still a formality, not a test.

Nothing in C38, C40 or the index changes standing. H1 is NOT TESTED — not supported, not refuted.


## 2. Add to `vault/00-index.md`, in the computed-notes list


- [[C52-setpoint-survival-ringing]] — **P-008 run on real `phi`, pre-registered, and it does not run: the mammal leg is Turbill 2011 and the bird leg has an empty treatment arm.** Brief `bc2259e6...` (14,767 bytes) hashed before any survival value was fetched; the prior-art check was run **before** the join and found Turbill, Bieber & Ruf 2011 (`10.1098/rspb.2011.0190`, Crossref 283 cites) already reporting **~15% higher annual survival in hibernators than similar-sized non-hibernators** under phylogenetic GLS — **the mammal leg of C38 §5's survival clause is REDISCOVERED.** The only new leg, birds, is structurally unrunnable: of **27** British species with BTO ring-recovery adult annual survival, exactly **3** are Ruf & Geiser heterotherms (*Apus apus* 0.808, *Caprimulgus europaeus* 0.700, *Delichon urbicum* 0.410) and **all 3 are obligate long-distance migrants**, removed by a rule fixed in advance → lever-bearing arm **n = 0**; the lever-less arm is **n = 0** too, because the asymmetric coding rule needs an explicit negative and no avian compilation states homeothermy. **In temperate avifauna the lever and migration are alternative solutions to the same winter energy problem, so a migration-controlled avian test deletes its own treatment group.** That rule also shows what C40 paid: only **240 of 671** small temperate mammals can be coded without inferring "lever-less" from absence (24/216/**425 UNCODED**/6 conflicts). The Amniote database has **no** `adult_survival` field; **longevity was not substituted for `phi`**. Void-by-construction control: the forbidden rules give Δ`phi` = **+0.147** unmatched, which the pre-registered 2× mass matching alone collapses to **+0.059, 95% CI [−0.132, +0.295]**, sign test 2/3, p = 0.500. P-072 scan: still **0** above +100%, over a reach of **n = 1** — the ≥10-candidate condition is not met, so the falsifier remains a formality. **H1 NOT TESTED.**


## [2026-09-05] method | 25 failure modes named from one day's caught failures; the most frequent is the unattributed count

New note: vault/method/failure-taxonomy.md. Every 2026-09-05 correction, honest null and
adversarial hit in this log was read as a specimen of a failure mode rather than as a fact about
its own claim. 25 modes, six groups (Provenance, Statistics, Instruments, Reasoning, Process,
Framing), 79 logged instances. Each mode carries its instances with wikilinks, how it was caught
(audit, adversary, replication, positive control, negative control, self-test, pre-registration,
lint, the human), the guard now standing, and which actor owns it — the model, the tooling, the
orchestration, or the human.

Most frequent: P2, the unattributed count (7) — a figure promoted without provider, endpoint and
fetch date. Then P1, two numbers in one field (6: the 578/595 two-objects case, G28's 5-and-8
dual count, G29's frontmatter contradicting its own table, Griebling cited in two contradictory
roles) and P4, a published margin adopted as if computed (6, of which three are C30's single
habit). Three modes have no guard at all: the single-agent blind (C46, C50), stale watchers in
the orchestration loop, and the frontmatter-vs-body half of P1.

Observed catch counts by earliest catch: audit 11 modes, adversary 7, replication and controls 3,
self-test and calibration 2, pre-registration 1, the human 1, **lint 0**. Lint blocks schema
drift and catches none of these; the cheapest effective guards are the calibration query and the
printed drop count; the only guard that caught the fatal ones (C43's pseudoreplication, G36 leg
2's sign error, G34's metaphor) is one adversary per claim.

Distinct from [[failure-modes]], which is about how a measured zero can be fake inside the
citation-intersection instrument; this one is about the whole agent-run research loop and is
cross-linked from it. The note ends by recording that it was written by an agent of the same kind
that committed the failures, and that the counts are of caught failures, not committed ones.


---

## 2. Add to `vault/00-index.md`, in the method / instruments section


- [[failure-taxonomy]] — **25 failure modes from one day of agent-run science, grouped
  Provenance / Statistics / Instruments / Reasoning / Framing / Process, with the actor and the
  guard for each.** 79 instances, all from 2026-09-05. Most frequent: the unattributed count (7).
  Three modes have no guard yet. Observed catch counts: audit 11, adversary 7, replication and
  controls 3, self-test and calibration 2, lint 0. Companion to [[failure-modes]], which covers
  the same question for one instrument.


---

## 3. Optional cross-link in `vault/method/failure-modes.md`

`failure-taxonomy` already points at `failure-modes`. The reciprocal line, if the owner of that
file wants it, belongs under its title:


Scoped to one instrument. For the whole research loop — provenance, statistics, reasoning,
process and framing — see [[failure-taxonomy]].
