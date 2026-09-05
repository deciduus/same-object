---
name: C37-lolp-starvation-identity
type: computed
exit: computation
extends-to: [sustainability, ecology]
next-step-cost: S
---

# The LOLP–starvation identity, with its failure boundary

> **Conditional, not exact.** Under five stated conditions — discrete time, absorbing
> boundary at 0, a reserve cap, additive inflow/outflow, and the objective
> `P(absorb before T)` under a common discount factor — the storage-constrained
> loss-of-load recursion and the small-bird starvation recursion are *literally the same
> equation*, and VoLL and `∂V/∂x` are the same multiplier on the same constraint; but the
> objective condition fails as each field is normally practised (the grid prices a
> *magnitude*, EENS, not a probability; the bird carries a predation hazard that is not a
> boundary crossing, and a fitness terminal condition), so the identity is **exact on a
> restricted pair of problems, structural-only on the pair the fields actually solve**.

Sharpens §1 of [[C33-lolp-starvation]] into a theorem with a stated failure boundary, in the
manner [[C5-charnov-gittins]] set. Provenance: `_scripts/c37_identity.py cites`.

---

## 1. Both problems in one notation

Discrete periods `t = 0,1,…,T`. Reserve `x ∈ [0, x_max]`. Inflow `g`, outflow `c`, control
`u ∈ U`, exogenous noise `(ξ_t, η_t)`.

```
x_{t+1} = min( x_max , x_t + g_u(ξ_t) − c_u(η_t) ) ,      state 0 absorbing      (1)
```

### 1.1 Grid, classical LOLP (Billinton & Allan)

The textbook construction has **no state variable at all**. Build a capacity-outage
probability table: enumerate generator up/down combinations `j` with probability `p_j` and
available capacity `C_j`. For a load `L_t` drawn against the load-duration curve,

```
LOLP(t) = Σ_j p_j · P( L_t > C_j )                                                  (2)
LOLE    = Σ_{t=1}^{365} LOLP(t)   [days/yr]      or   Σ_{t=1}^{8760}  [LOLH, h/yr]   (3)
```

**LOLE sums a per-period probability over one planning year**, its unit inherited from the
period length: daily-peak periods give days/year (the 1-day-in-10-years criterion is
`LOLE ≤ 0.1 d/yr`), hourly periods give LOLH in h/yr. Equation (2) is memoryless — each
period scored independently, nothing carried forward, **no first-passage problem**. That is
the scope restriction [[G34-lolp-starvation-risk]] already adopted, restated because it is
the first thing an auditor reaches for.

### 1.2 Grid, storage-constrained adequacy

Add a store. `x_t` is state of charge (MWh), `g` available generation, `c` load; unserved
energy in period `t` is `U_t = max(0, c_t − g_t − x_t)`, and

```
LOLP(t) = P( U_t > 0 ) = P( the reserve is exhausted and the period's net draw exceeds it ) (4)
```

Now the trajectory matters, `LOLE = Σ_t LOLP(t)·Δt`, and (1) is the state equation.

### 1.3 Bird, McNamara & Houston

McNamara & Houston, *Starvation and Predation as Factors Limiting Population Size*,
**Ecology 68(5):1515–1519 (1987)**, DOI `10.2307/1939235` — Crossref record fetched
2026-09-05, `is-referenced-by-count` 407; and Houston & McNamara, *A Theoretical
Investigation of the Fat Reserves and Mortality Levels of Small Birds in Winter*, **Ornis
Scandinavica 24(3):205–219 (1993)**, DOI `10.2307/3676736`, count 195, same fetch. Both
resolved live, with title, journal, volume and first page matching. Houston & McNamara 1993
remains paywalled (as in C33); its parameter values were not read.

Day/night structure: within a day, `n` foraging periods with stochastic gain `g(u)` under
action `u` (intensity, patch choice, thermoregulatory state); then one night with draw
`c(η)` set by weather and thermoregulatory choice. Reserve `x` is fat in kJ, capped at
`x_max`. Survival probability satisfies the backward recursion

```
S(x,t) = max_u  E_{ξ,η}[ S( min(x_max, x + g_u(ξ) − c(η)), t+1 ) ]                   (5)
S(x,T) = Φ(x) ;  S(x,·) = 0 for x ≤ 0
```

with **terminal fitness** `Φ`. The marginal value of reserves is `∂S/∂x`, and the optimal
fat level is where it balances the marginal cost of carrying fat.

---

## 2. The theorem

**Conditions.**

- **(C1) Discrete time, finite horizon `T`**, same period length on both sides.
- **(C2) Absorbing boundary at 0**: once `x ≤ 0` the process stops and the run counts as a
  failure. On the grid this is a *convention*, not a physical fact — see FB3.
- **(C3) Reserve cap `x_max`**, imposed by the same truncation `min(x_max, ·)`.
- **(C4) Additive, state-independent inflow/outflow** as in (1): `g, c` may depend on `u`,
  `t` and the exogenous state, not on `x`.
- **(C5) Objective `P(absorb before T)` on both sides**, same discount factor (in
  particular, none on either side), terminal condition `Φ(x) = 1{x > 0}`.

**Theorem.** Under (C1)–(C5), let `B_u` be the one-period Bellman operator

```
(B_u f)(x) = E_{ξ,η}[ f( min(x_max, x + g_u(ξ) − c(η)) ) · 1{ x + g_u(ξ) − c(η) > 0 } ]
```

Then the storage-constrained loss-of-load recursion and the starvation-probability
recursion are the *same* backward iteration of `B`:

```
S(·,t) = max_u B_u S(·,t+1) ,  S(·,T) = 1{x>0}   and   LOLP over [0,T] = 1 − S(x_0, 0)
```

*Proof.* `S(x,t)` is by definition the probability that (1) has not hit 0 by `T`, started
from `x` at `t`. Condition on the first transition: the indicator in `B_u` implements (C2),
the `min` implements (C3), giving `S(·,t) = max_u B_u S(·,t+1)`. The grid's
`LOLP(t) = P(U_t > 0)` is, under (C2), the probability of first absorption at `t`; those
events are disjoint across `t`, so summing them over `[0,T]` telescopes to `1 − S(x_0,0)`.
No fixed point and no vanishing-discount argument: the horizon is finite and `U` is finite. ∎

**Multiplier lemma.** Attach `λ_t` to the reserve constraint `x_{t+1} ≥ 0` in period `t`'s
Lagrangian. The envelope theorem for (5) gives `λ_t = ∂V/∂x |_{x=0⁺}`: the shadow value of
one more stored unit at the moment the constraint binds. On the grid that multiplier on the
energy-balance constraint *is* the **value of lost load** — what the adequacy optimum
equates against the marginal cost of capacity. In the bird it is the **marginal fitness
value of a unit of fat**, equated against the marginal predation cost of carrying it. Same
constraint, same value function, same derivative: **two quantities matching, not one**,
which is what makes this an identity claim rather than an analogy.

It says nothing about whether the two `∂V/∂x` are *commensurable* — one is currency, the
other fitness, and there is no exchange rate (C33 §5.3). Identity of the multiplier's
*role*, not of its units.

---

## 3. Five failure boundaries

### FB1 — No control on the grid side. Verdict: **survives, as a special case.**

Grid LOLP is a *reliability evaluation*, not an optimisation: (2) and (4) are computed under
a fixed dispatch rule `π₀`, with no `max_u`. The bird chooses `u`. But this is not a
disagreement about the equation — it is `max_u B_u` versus `B_{π₀}`, and `B_{π₀}` is the
policy-evaluation operator of the *same* dynamic program. Formally:

```
grid LOLP  =  1 − S^{π₀}(x_0, 0)      where   S^π(·,t) = B_{π(t)} S^π(·,t+1)
```

i.e. **grid LOLP is the bird's `S` under a fixed policy** — the evaluation half of the DP
with the optimisation half switched off. Storage-*dispatch* optimisation (adequacy-aware
charge/discharge scheduling) restores `max_u`: charge/discharge choice is the bird's `u`,
and the two problems then coincide as *optimisations*, not merely as recursions.

### FB2 — Objective: survival vs expected cost. Verdict: **conditional; the sharpest of the five.**

The bird maximises `S` (a probability). The grid minimises expected cost,

```
J(π) = E[ Σ_t κ(u_t) ] + VoLL · E[ Σ_t U_t ] ,     E[Σ_t U_t] = EENS                (6)
```

which prices the *magnitude* of unserved energy. **EENS and LOLP are different
functionals**: two policies can share an LOLP and differ severalfold in EENS, and (6) ranks
by the second. The objectives coincide in exactly two cases.

1. **Constant severity.** If every absorption event carries the same unserved energy `e`,
   then `EENS = e · E[#events]`, and under (C2) — absorption terminates the run — that is
   `e · P(absorb)`. Then `argmin J = argmax S` for any `VoLL > 0`. The bird satisfies this
   trivially: there is exactly one absorption event and it costs one life.
2. **`VoLL → ∞`.** With `κ` bounded, (6)'s second term dominates and the ranking is by
   EENS; if the severity *distribution* is also policy-independent, this reduces to case 1.
   Survival-as-cost (`κ ≡ 0`, `VoLL = 1`, `U ∈ {0,1}`) is the same statement inverted.

Outside those, **the grid is not solving the bird's problem** even while running the bird's
recursion. This is why C33 could put LOLE and `P(starve)` on one axis only by inventing a
conversion (its 8-hour charge): that conversion is the missing severity model.

### FB3 — Horizon, terminal condition, restoration. Verdict: **narrows the claim to LOLP; breaks it for LOLE-as-a-count.**

The bird's winter is finite with a genuine terminal condition `Φ`. LOLE is a *per-year,
stationary* statistic on a renewed system: unserved load is restored, the store recharges,
the year is one cycle of a regenerative process, so `LOLE = Σ_t LOLP(t)` is an **expected
count of events**, well-defined because 0 is reflecting-with-a-penalty rather than
absorbing. A starved bird does not come back. So the §2 identity holds for `LOLP` over a
horizon (a first-passage probability) and fails for `LOLE` read as an event count, which has
no bird analogue — C33's table B saturating for Ireland is that failure surfacing
numerically. And (C5) requires `Φ(x) = 1{x>0}`: any other terminal fitness makes (5) an
expected-terminal-reward DP, not an absorption probability (FB5).

### FB4 — Carrying cost of the reserve. Verdict: **splits. One half harmless, one half breaks (C4) and the theorem with it.**

Fat is not free, in two distinct ways, and they behave differently.

- **(d1) Metabolic and flight cost of mass.** Heavier birds burn more, making outflow
  state-dependent, `c = c(η, x)`, which violates (C4) as literally stated. **Harmless**:
  `B_u` is unchanged in form, backward induction is unaffected, and the grid has a real
  analogue in charge-dependent round-trip efficiency and self-discharge. Relax (C4) to
  "`g, c` may depend on `x`" and the theorem survives verbatim.
- **(d2) Predation.** Carrying fat raises the *hazard of being killed*, `m(x)` increasing in
  `x`. This does not change the reserve dynamics at all; it inserts a second, **interior**
  absorbing mechanism:

```
S(x,t) = max_u (1 − m(x,u)) · E[ S(x_{t+1}, t+1) ]                                  (7)
```

  (7) is a *killed* process whose absorption is not a boundary crossing. So `S` is no longer
  a first-passage probability and §2's theorem does not apply; and `∂V/∂x` acquires a
  negative predation term, making the bird's optimum **interior** — an optimal fat level,
  not "as much as possible" — whereas LOLP is monotone decreasing in storage and the grid's
  optimum is set by capital cost alone. **This is the one failure boundary with no grid
  analogue:** storage degradation is a *cost* term in (6), not a killing rate, and a degraded
  battery does not delete the grid. The identity is recovered only if `m(x,u) ≡ m`, in which
  case (7) is (5) with a uniform discount factor `1−m`, which (C5) already allows. C33's
  `8.25×10⁻⁸` is a starvation-only figure computed strictly inside this boundary — which is
  what makes it comparable to a LOLE, and what makes it not the bird's real mortality.

### FB5 — Fitness vs probability. Verdict: **identity holds only for pure overwinter survival.**

If the objective is lifetime reproductive success, survival is a *factor*, not the
objective: `V(x,t) = E[future reproduction | survive] · S(x,t)`, and a bird that should
reach spring in condition trades survival probability for terminal reserves, moving the
argmax. **The identity requires `Φ(x) = 1{x>0}`** — the winter as a pure survival bottleneck
with no condition-dependent spring payoff. Under any increasing `Φ`, (5) is still a backward
DP with the same operator, but its solution is not a probability and there is nothing on the
grid side for it to equal. The grid's counterpart of a non-trivial `Φ` — end-of-horizon
value of stored energy, standard in hydro water-value functions — is a cost DP, i.e. FB2.

**Summary.** FB1 survives; FB4(d1) survives once (C4) is relaxed; FB3 narrows the claim from
LOLE to LOLP; FB2, FB4(d2) and FB5 are genuine breaks, repaired only by constant severity,
constant predation hazard, and indicator terminal fitness respectively.

---

## 4. Ruin theory is the parent, and neither field cites it

Both are **ruin problems**: a reserve process with stochastic income and outgo, estimand =
probability of first passage to 0 before a horizon. That is the Cramér–Lundberg problem of
actuarial risk theory (Lundberg 1903; Cramér 1930), whose modern canon is Asmussen &
Albrecher, *Ruin Probabilities*, 2nd ed., World Scientific 2010, **DOI `10.1142/7431`** —
Crossref record fetched 2026-09-05, title and publisher confirmed, with a published review
under DOI `10.1365/s13291-011-0026-7` (*Jahresbericht der DMV*, 2011) naming both authors.
Finite horizon with a cap is gambler's ruin; the grid's fluid version is the buffer-content
process whose overflow problem is that literature's standard queueing–ruin duality.

**Search leg, 2026-09-05.** Eight formulations: `"starvation" AND "loss of load"`;
`"fat reserve" AND "reserve margin"`; `"ruin probability" AND "starvation"`;
`Cramér–Lundberg AND animal energy reserves`; `"gambler's ruin" AND foraging`;
`"gambler's ruin" AND "loss of load"`; `ruin/risk theory AND power-system adequacy`;
`risk-sensitive foraging AND absorbing barrier`. **None returned a source stating the
LOLP ↔ starvation identity, or either field citing ruin theory for it.** Two near misses:

- Deulkar, Nair & Kulkarni, *Sizing Storage for Reliable Renewable Integration: A Large
  Deviations Approach*, arXiv:1904.04771 (2019), abstract fetched 2026-09-05: models LOLP
  for a renewable generator bundled with a battery as a **Markov-modulated fluid queue**,
  large-deviations limit in battery capacity. That is the ruin problem reached through
  queueing, with **no ruin, Cramér–Lundberg or Lundberg-exponent language** in the abstract.
  The grid arrives at the parent under an alias.
- Behavioural ecology's risk-sensitivity literature (Caraco's energy-budget rule and
  descendants) is explicitly about a threshold-crossing objective and is *conceptually*
  gambler's ruin; no surfaced work says so or cites the ruin literature.

**Citation check.** `c37_identity.py cites`, provider OpenCitations
`https://api.opencitations.net/index/v1/citations/<doi>`, run 2026-09-05. Eight blank
`citing` records were dropped before any set was built — the phantom `""` member joins every
set and would have turned each zero below into a 1.

| Pairing | `N_A` | `N_B` | **O** |
|---|---|---|---|
| Asmussen & Albrecher 2010 × Billinton & Allan 1996 | 515 | 2,058 | **0** |
| Asmussen & Albrecher 2010 × McNamara & Houston 1987 | 515 | 422 | **0** |
| Asmussen & Albrecher 2010 × Houston & McNamara 1993 | 515 | 196 | **0** |

The two anchor `N` reproduce [[C33-lolp-starvation]]'s exactly (2,058 and 422) — the check
that this is the same instrument on the same objects. **Three literatures,
three pairwise zeros:** grid × bird was already 0 across four pairings in
[[G34-lolp-starvation-risk]], and ruin theory shares no citer with either anchor. On this
evidence the gap is larger than G34 states — not two fields that failed to find each other,
but **two fields that independently rebuilt a 1903 result, neither citing the parent.**

Caveat, as in G34: citer-set intersection cannot see a third work that cites neither anchor
while making the connection, and one monograph is a narrow proxy for a literature. A zero
here is absence of evidence at anchor level, nothing stronger; see §5.5.

---

## 5. Honesty

1. **The status is conditional.** (C5) is the condition doing all the work, and FB2,
   FB4(d2) and FB5 each name a standard practice in one field that violates it. The honest
   one-liner: *the two fields run the same recursion and do not optimise the same
   functional.*
2. **This narrows C33 rather than confirming it.** C33 §1 called the recursion "exact"
   without stating (C5), and its five-decade LOLE comparison lives inside FB2 and FB3, both
   now named as breaks. No C33 arithmetic is retracted; its §1 claim is re-scoped.
3. **Nothing here was computed numerically except the citation table.** No model was solved;
   §2 is algebra, §3 case analysis. The only new numbers are three zeros and four `N`
   values, single-provider — one instrument short of the two-source standard.
4. **Houston & McNamara 1993 was still not read.** §1.3's day/night structure and terminal
   condition are reconstructed from the standard form of that model family (as C33 used it
   via Brodin et al. 2017). If its terminal condition is not an indicator, FB5 applies to
   the anchor itself and (C5) is violated by the very paper the identity is claimed against.
   **This is the load-bearing unread source.**
5. **The ruin-theory finding is about anchors, not fields.** "Neither literature cites ruin
   theory" is shorthand for "neither anchor's citer set meets Asmussen & Albrecher's". A
   paper citing Feller's gambler's-ruin chapter instead is invisible to this test, and
   Feller is where a careful author would go. It **cannot distinguish "did not know" from
   "cited a different textbook"**, which weakens §4's strong reading.
6. **The multiplier lemma is stated, not proved.** The envelope step needs `V` differentiable
   in `x`; on a discretised reserve grid it is a finite difference. The continuum limit was
   not attempted.
7. **§2 is an identity of *operators*, and says nothing about inputs.** C33 §5.1 showed the
   bird's inflow CV is 0.85% against a grid's one-to-two orders larger and correlated. The
   identity transfers the method, not the answer.

See [[G34-lolp-starvation-risk]], [[C33-lolp-starvation]], [[C5-charnov-gittins]],
[[what-closes-a-gap]], [[failure-modes]].
