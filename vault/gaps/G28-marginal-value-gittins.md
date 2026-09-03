---
id: G28
name: G28-marginal-value-gittins
type: gap
standing: live
evidence: full-text-read
contact-surface: 8
crosses: nothing
crosses-rank: 0
topology: mediated
mediator: neuroeconomics
borrows-from: []
lends-to: ["[[G9-discrepancy-base-rate]]"]
mutual-with: []
computed-in: []
uses-move: []
rests-on: []
tags: [node/gap, crosses/nothing, evidence/full-text-read, standing/live]
last-checked: 2026-09-03
note: "Held under the full-text re-read. Averbeck 2015 formalises bandits and foraging in one MDP framework and names both objects without relating them; Charnov not cited."
---

# Marginal value theorem and the Gittins index

**STANDING: LIVE** · evidence: full-text-read · contact surface: 8 · last checked 2026-09-03

> Charnov's rule: leave a depleting patch when the marginal intake rate drops to the average
> for the habitat.
>
> The Gittins index generalises the same optimality condition to the stochastic case.
> **Charnov's rule is its deterministic, zero-switching-cost limit.** No paper states that.

## Why this entry forced a new field in [[relationship-description]]

The count alone is uninteresting: 8 co-citers out of 1,542 and 5,424. Under verdict scoring
that reads "small number, gap holds," and the thinking stops.

**Inspecting the eight is where the finding actually is.** All eight are cognitive and
decision neuroscience — *Optimally frugal foraging*, *Raccoons optimally forage for
information*, *Cortical Circuits for Adaptive Foraging Decisions*, *How the threat of losses
makes people explore more than the promise of gains*.

So the topology is: **operations research and behavioural ecology have no direct contact at
all.** They are joined only by a third field that reads both and tells neither. That is a
specific structure, and no number expresses it.

## The control that makes it sharp

| Pair | Co-citers |
|---|---|
| Charnov and Gittins | **8** (0.5% of Gittins) |
| **Gittins and Sutton & Barto** | **181 (11.7%)** |

Operations research and reinforcement learning are **one closed literature**. It is
specifically biology that sits outside it. Without this control the 8 means nothing; with it,
the isolation is located.

See [[positive-controls]].

## Independent rediscovery, in-house

Behavioural ecology derived its own stopping rule — Green 1984, *Stopping Rules for Optimal
Foragers*, 248 citations — in its own vocabulary, **without the stopping-theory literature.**
A field re-derived optimal stopping rather than read it.

## What crosses

**Nothing.** Not the formalism, not the vocabulary. The one genuine contact runs the other
way: Srivastava, Reverdy & Leonard, *On optimal foraging and multi-armed bandits* (2013), a
control-theory paper importing foraging framing into bandit regret analysis — **one-way,
from the operations-research side.**

Same asymmetry as information foraging, which took optimal foraging theory into
human-computer interaction and is not read back. See [[one-way-borrowing]].

## What is specifically absent

**The stated equivalence.** That Charnov's threshold *is* the Gittins index in the
deterministic, zero-switching-cost limit. Writing that down is a paragraph of algebra and
would let each field use the other's results.

## What would change it

Write the equivalence. Then the biology inherits the stochastic machinery — index policies,
regret bounds, switching costs — and operations research inherits several decades of field
data on animals actually solving the problem.

## Verification

Survived the full alternate-name gauntlet under the hardened protocol: patch leaving,
optimal foraging, patch residence time, against optimal stopping, secretary problem, index
policy, scheduling. All zero or irrelevant.

## The full-text re-read: holds, with one correction

**The best-placed paper in existence does not state the relation.** Averbeck 2015,
[*PLoS Comput Biol*](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4401555/fullTextXML),
read in full, formalises bandit, sampling **and** foraging tasks in one MDP framework — and
names both objects without ever relating them:

> "It is also possible to use Gittins indices to select optimal actions in stationary bandit
> tasks"

and separately:

> "some foraging tasks have been modeled using the marginal value theorem"

**Charnov is not cited at all.** One paper, both halves in hand, no connection drawn. That is
the gap in a single document.

Europe PMC confirms the isolation: `"Gittins" AND "Charnov"` → **3**, all psychology and
neuroscience. `"Gittins index" AND "marginal value theorem"` → **1**, a review adjacency.

**One-way borrowing confirmed and understated.** Srivastava, Reverdy & Leonard 2013, read in
full: it **never mentions Gittins.** McNamara & Houston 1985 and Green's 1990 field overview
contain zero Gittins, index or stopping hits.

### Correction to the claim's own wording

The note says Charnov's rule is the Gittins index in the **"zero-switching-cost limit."** That
is probably wrong on its own terms — **MVT has a switching cost**: the travel time τ. The clean
reduction more likely runs through **Whittle's retirement reward**, where τ maps to the
retirement option rather than to zero. *This is a reading, not a sourced claim, and is marked
as such.* It sharpens what would have to be written, and makes writing it slightly harder.

### Not obtained

Green 1987, Stephens & Krebs 1986, and Houston & McNamara 1999 are books that could not be
obtained. **The last is the most likely place for a stated relation to be hiding**, and this
entry stays provisional on it.
