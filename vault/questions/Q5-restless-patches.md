---
name: Q5-restless-patches
type: question
arises-from: ["[[C5-charnov-gittins]]", "[[G28-marginal-value-gittins]]"]
status: open
---

# Does the identity survive patches that renew?

> [[C5-charnov-gittins]] holds where patches are non-revisitable and frozen. **Real patches
> regrow.** The break is named, located, and has machinery waiting on the other side.

## Where it breaks, precisely

The identity requires arms to be **frozen** — a patch you are not in does not change. Three
foraging realities violate that, and each maps onto a bandit problem that is already solved or
already known to be hard:

| Foraging reality | Bandit name | Status in that field |
|---|---|---|
| **Patches regrow** | restless bandit | Whittle index — provably not optimal, but asymptotically good |
| **Patches revisitable** | switching costs | **no index policy is optimal** |
| Habitat non-stationary | non-stationary bandit | active area |

## Why this is the most valuable open item here

Patch renewal is not an edge case. **It is the normal condition** for grazers, pollinators and
territorial foragers. The clean identity covers the case biology cares least about.

And the answer already exists on the other side: **the Whittle index is exactly the tool for
arms that evolve while unobserved.** Nobody has written it as a foraging rule.

## The question

What is Charnov's rule for a regrowing patch? Concretely: **does the Whittle index of a
regenerating patch reduce to a modified marginal-value condition** — leave when the marginal
rate drops to the habitat average *plus a term in the regrowth rate of the patch you are
leaving*?

That extra term is the thing to derive, and it should be signed: a fast-regrowing patch is worth
leaving *sooner*, because it will be there when you return.

> **Mechanism corrected 2026-09-05.** That sentence gives a *revisitability* reason. [[C25-whittle-foraging]] derives the same sign from a different mechanism: the `−r(1−x)²` term is regrowth *forgone by occupying the patch*, and the r→0 limit recovers MVT only under non-revisitability. Same sign, different cause; C25's is the derived one. The revisitability effect is C5 §6 row 6 (switching costs), quantified there as the residual `λx²`.

## Why it might be answerable

Same two lines as [[C5-charnov-gittins]]. The Whittle relaxation is standard and the regenerative
structure survives — a patch cycle is still a renewal. The likely obstacle is that Whittle
indices are not generally optimal, so the result would be an **approximation with a stated
optimality gap** rather than an identity. That is still a publishable object and an honest one.

## What it would change

Behavioural ecology inherits the whole restless-bandit literature: indexability conditions,
regret bounds, and the known failure cases. And bandit theory inherits **decades of field data
on animals solving the restless problem** — which is the one thing operations research does not
have.

## Answered in part: [[C25-whittle-foraging]] (2026-09-05)

The derivation is done. `W(x) = λx² − r(1−x)²` for a patch at standing crop `x` regrowing at
rate `r`, depleting at `λx`. **Indexable unconditionally** (`W` strictly increasing). The
signed regrowth term this note asked for is `−r(1−x)²`, and its sign is the one conjectured
here: **fast-regrowing patches are left sooner, at a higher giving-up density**, with
`dGUD/dr = (1−GUD)²/(2[λ·GUD + r(1−GUD)]) > 0`.

Still open from this note: **the optimality gap is not stated.** A single forager among `N`
patches sits outside the regime the Weber–Weiss asymptotic-optimality result covers, so C25
delivers an indexable heuristic with a signed comparative static, not a bounded approximation.
Also open: travel time `τ` is re-inserted at the renewal-cycle level, not inside the Whittle
relaxation.
