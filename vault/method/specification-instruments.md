---
name: specification-instruments
type: method
---

# Specification instruments

> The move that runs under the strongest results in this project, named once the user saw it:
> **when you cannot predict the unknown, build the exact identity that specifies it.** It does
> not forecast the black swan. It pre-commits the bookkeeping that makes the swan legible the
> moment it lands. That is the antifragile posture — the instrument gains from the anomaly
> instead of breaking on it.

## The template

Every instrument here has the same four steps. The first is analysis; the middle two are
**discrete**; the last is the deliverable.

1. **An exact identity in a conserved quantity.** Not a model, not a bound with assumptions — an
   accounting identity that holds regardless of mechanism. `Σ = P/(F·Δu) ∈ [0,1]` because
   `P_total = −F·Δu` is bookkeeping, not physics.
2. **A finite enumeration of candidate reservoirs / mechanisms.** This is the combinatorial
   step: list every partner the system is in contact with. The list is never provably complete,
   so every output is prefixed *of those considered*.
3. **Exclusion by availability.** For each candidate compute the quantity it would have to
   supply and the ratio to what it can supply. `A = (F·Δu)/P_avail > 1` rules it out. A decision
   procedure over a finite set.
4. **The residual is a specification, never a verdict.** What survives is a description of what
   a real partner would have to be — a mass, a field, a rate, with required magnitude, sign and
   time-dependence. Testimony sets the specification, never the mechanism.

## Why this is the antifragile / black-swan form

A predictive model is fragile to the unknown: an event outside its training breaks it. A
specification instrument is not, because **it never claimed to know the mechanism** — it only
constrains what any mechanism must satisfy. Feed it an anomaly and it does not fail; it returns
the tighter specification. The rarer and stranger the input, the more the instrument earns its
keep. That is antifragility in the exact Taleb sense: convex response to disorder.

The failure mode it replaces is the flat *"impossible."* [[Q9-fuel-free-is-an-assumption]]: a
`Σ > 1` is not impossible physics, it is a misidentified reservoir. The project made that error
itself about solar sails and caught it with its own instrument.

## The instruments we have

| Instrument | Conserved quantity | Discrete core | Status |
|---|---|---|---|
| [[reservoir-audit]] / [[C8-momentum-harvesting-metric]] | energy–momentum | reservoir enumeration | validated 5/5; [[C11-flyby-reservoir-audit]] is the first open case |
| [[information-audit]] | entropy | sink enumeration; **bits** | validated 3/3, sink named each time |
| [[Q7-same-class-prediction]] | — (a conditional, not an identity) | the same-class partition | strict CLASS-I: **8 closed, 7 systematics + 1 fluctuation, 0 new physics**; Clopper–Pearson 95% upper bound on P(new physics) = **0.31**. Adding CLASS-II: 15 closed, bound **0.18**. **Not bias-immune** — see below |
| [[citation-intersection]] | — | **set intersection over bibliographies** | the project's evidence standard |
| [[C5-charnov-gittins]] | optimality | **the Gittins index — a discrete allocation object** | closed by identity |

**Step 2 has a prior step these instruments did not have until 2026-09-05.** Before any
enumeration, check that the observable exists: [[reservoir-audit]] Part D.3 / F8 names the failure
class **"the central value is a function of the reduction pipeline"** — independent reductions of
the *same* raw data spanning "detected" and "not detected" — and halts with `NO AGREED OBSERVABLE`.
Every instrument in this table converts whatever number it is handed into a required supply, so
every one of them inherits the exposure.

**The Q7 row, corrected 2026-09-05 (backlog C15).** It read *"bias-immune, 11/11"*. Both halves
were wrong. The count came from a hand-assigned sample; re-applying [[C16-same-class-catalogue]]'s
decision procedure **blind** — class assigned on apparatus / observable / analysis pipeline
before the outcome is consulted — changes 11 of 24 assignments and leaves **N = 8** strict
CLASS-I closed cases, not 11.

And the bias-immunity claim is softened exactly as C16 softened it. The old argument was that
adding invisible same-class cases could only add more systematics. **That fails**, because
findability of a documented *resolution* correlates with the resolution being mundane: a
same-class disagreement that quietly turned out to be real physics gets written up as a
discovery and reclassified, not filed as a resolved measurement dispute. So the missing cases
are not a random sample, and the correct posture is a stated interval rather than an immunity
claim — hence the Clopper–Pearson bound in the row above. **0 of 8 is consistent with a
same-class new-physics rate as high as 31%.**

The middle column is the point. This project keeps landing on **integer and combinatorial
objects**: the Gittins index (discrete stopping), Hill numbers (effective *count* of functions,
[[hill-number-multifunctionality]]), Buckingham Π-groups (integer kernel of a dimension matrix),
citation intersection (finite set overlap). Discrete mathematics is not a flavour added on top —
it is where these instruments actually live.

## The template for building a new one

To point this at a new domain, find:

- a conserved or bounded quantity with an **exact** accounting identity (energy, momentum,
  angular momentum, information/entropy, probability mass);
- a way to **enumerate** the finite set of channels through which it can flow;
- a computable **required-versus-available** ratio per channel.

Then it validates the same way the reservoir audit did: run it on cases whose answer is known
and confirm it recovers them, before pointing it at an open one. An instrument that cannot
reproduce Pioneer has no business being aimed at a flyby.

## Open instruments being built

- **The information / Landauer audit — BUILT and validated: [[information-audit]].** Conserved
  quantity = entropy. Validated **three for three** on measured experiments (Bérut 2012 Landauer,
  Toyabe 2010 Maxwell demon, Koski 2014 single-electron Szilard), **naming the entropy sink each
  time.** Toyabe was its Pioneer: the audit correctly identifies the demon's **memory register**
  as the initially-unnamed sink that closes the balance. Then it linked to biology — a
  proofreading step is measurement-and-discard, and biology pays the `k ln2` per rejected bit out
  of ATP. That is the unread bridge [[G25-proofreading-coding]] measures.
- **The Π-space as an integer lattice — BUILT: [[C12-pi-space-lattice]].** A 3×10 dimension
  matrix mixing organism and process quantities has rank 3, so 7 Π-groups, and Froude, Reynolds,
  Péclet and Damköhler are **all integer vectors in the one kernel.** That co-located Π-space is
  constructible, so **the surviving half of [[G21-dimensionless-regime-map]] closes by
  construction.** New object: the transport crossovers (Re, Pe, Pe_th) are **lattice-locked**
  (parallel, offset by Schmidt/Prandtl/Lewis constants) while Froude and Damköhler cross them
  transversally — and "locked" is now computable, giving [[G22-scale-transfer-triage]]'s
  constant-bound criterion as lattice arithmetic. The two gaps are tied through one object.
