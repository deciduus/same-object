---
id: G22
name: G22-scale-transfer-triage
type: gap
standing: live
evidence: full-text-read
contact-surface: 9
crosses: vocabulary
crosses-rank: 3
topology: direct
mediator: 
borrows-from: []
lends-to: []
mutual-with: []
computed-in: ["[[C12-pi-space-lattice]]"]
uses-move: ["[[M6-vary-what-was-held-fixed]]"]
rests-on: []
tags: [node/gap, crosses/vocabulary, evidence/full-text-read, standing/live]
last-checked: 2026-09-03
note: "Disagreement adjudicated on the full text: Buckingham 0, dimensionless 0, screening 0. The paper asks for the guidelines, so it cannot be them. Holds."
---

# Scale-transfer triage in biomimetics

**STANDING: LIVE** · evidence: full-text-read · contact surface: 9 · last checked 2026-09-03

> Is there a **screening step** that tests whether a mechanism survives the scale change before you copy it?

## The disagreement is now adjudicated — for the first agent

Two agents had read Perricone et al., *Organismal Design and Biomimetics: A Problem of Scale*
(2021) differently: one found no screening procedure, the other read the paper's thesis *as*
the triage. A third pass pulled the full text independently
([PMC8544225](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8544225/fullTextXML),
129k characters) and searched it directly.

| Term | Occurrences |
|---|---|
| Buckingham | **0** |
| dimensionless | **0** |
| decision | **0** |
| criteri- | **0** |
| screening | **0** |
| protocol | **0** |

And the paper's own closing sentence:

> "Future research should be carried out to establish some guidelines in the scaling transfer
> for each field of knowledge"

**A paper asking for the thing cannot be the thing.** The second agent mistook *naming the
problem* for *supplying the procedure* — a distinct failure from the anchoring error that
damaged the other entries, and worth naming separately.

The gap **holds** rather than merely narrowing.

The 9-paper Buckingham intersection reproduces but is a **proper-noun artifact** — the field does
this work without ever writing the name. See [[failure-modes]] mode 3.

## The criterion, which appears unstated anywhere

> A capability is **scale-transferable** iff the governing dimensionless group can be held fixed
> by co-varying the free parameters. It is **constant-bound** iff the group contains a fixed
> constant appearing **alone** — kT, lambda, g, c — rather than in a compensable ratio.

"Appears alone" is a statement about the *current formulation*, not about impossibility — which
makes it the input to [[M6-vary-what-was-held-fixed]].

**This criterion is now computable: [[C12-pi-space-lattice]].** In the integer-lattice Π-space,
two crossovers are **locked** iff the Π-difference vector between them is supported only on
non-tunable constants. That is exactly "constant appearing alone," turned from a prose test into
lattice arithmetic on the Smith-normal-form basis. Worked case: `Pe/Re = Sc` has support only on
`ν` and `D`, so the Reynolds and Péclet crossovers are rigidly locked and cannot be varied
independently — a capability governed by their ratio is constant-bound, by construction. G21 and
G22 are now tied through one object.

**The empirical test:** gecko adhesion scales as A^(-1/4). A *negative* exponent — intrinsically
anti-scaling, not merely hard to manufacture.
