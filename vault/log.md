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
