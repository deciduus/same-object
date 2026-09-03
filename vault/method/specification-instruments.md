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
| [[Q7-same-class-prediction]] | — (a conditional, not an identity) | the same-class partition | bias-immune, 11/11 |
| [[citation-intersection]] | — | **set intersection over bibliographies** | the project's evidence standard |
| [[C5-charnov-gittins]] | optimality | **the Gittins index — a discrete allocation object** | closed by identity |

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

- **The information / Landauer audit.** Same shape, conserved quantity = entropy. Any device
  claiming computation, measurement or sorting below the thermodynamic floor must export the
  missing entropy somewhere; enumerate the sinks, exclude by availability, specify the residual.
  Validated against measured Landauer and Maxwell-demon experiments. Sibling of the reservoir
  audit for bits.
- **The Π-space as an integer lattice.** Buckingham's theorem says the dimensionless groups are
  the integer kernel of the dimension matrix. [[G21-dimensionless-regime-map]]'s surviving gap
  is that no single Π-space co-locates organisms and processes. That space is a *computable
  lattice object* — build it and read whether a Froude transition and a Péclet transition share
  an axis. Pure discrete linear algebra meeting a surviving gap.
