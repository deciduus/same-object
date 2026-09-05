---
title: |
  Charnov's marginal value theorem is the Gittins index of the outside option,
  and its restless extension predicts giving-up density rises with patch regrowth
author:
  - Landon Holden
<!-- AUTHOR: insert affiliation, ORCID and corresponding-author email here before submission -->
date: 2026-09-05
abstract: |
  Charnov's marginal value theorem (MVT) and the Gittins index were derived two years
  apart for different reasons and have not been connected. We show they are the same
  object. Bundling travel time into the outside option as a zero-reward prefix, the
  Gittins index of that "habitat arm" is $\sup_t g(t)/(\tau+t) = R^{*}$, and the index of
  a deterministic concave patch is $g'(t)$; the index rule $g'(t)=R^{*}$ is MVT. The
  identity is exact for deterministic concave patches with non-revisitable patches and a
  stationary habitat, generalises under discounting, and fails in exactly three places
  that the bandit literature already names: restlessness (patch regrowth), switching
  costs (revisitable patches), and non-stationarity. We take the first of these across
  the bridge. For a patch at standing crop $x$ depleting at $\lambda x$ and regrowing at
  $r(1-x)$, the Whittle index is $W(x)=\lambda x^{2}-r(1-x)^{2}$; the problem is
  indexable unconditionally, and $dGUD/dr>0$. Faster-regrowing patches should be
  abandoned at a *higher* giving-up density. Kadmon & Shmida (1992) with Kadmon (1992)
  measure departure and nectar renewal in one plant--pollinator system and parameterise
  the test. The two literatures have not met: 5 of 1,013 works citing Gittins (1979) also
  cite Charnov (1976), against 225 of 1,013 for the Gittins $\times$ Auer (2002) positive
  control; the denominator-invariant control ratio is 62.5 (run-time enumeration
  2026-09-03; Crossref and OpenCitations, 2026-09-05).
bibliography: refs.bib
csl-refs: true
---

<!-- All numbers in this manuscript are traceable to notes in the research vault; the
     note ID is given in an HTML comment beside each. -->

# Introduction

## The marginal value theorem

A forager exploits patches whose cumulative yield $g(t)$ is concave in residence time
$t$, and pays travel time $\tau$ at zero reward to reach the next one. Over one
travel-plus-patch cycle the long-run rate is $R(t)=g(t)/(\tau+t)$. Maximising over $t$
gives the first-order condition
$$g'(t^{*}) = \frac{g(t^{*})}{\tau + t^{*}} = R^{*},$$
Charnov's marginal value theorem [@charnov1976]: leave when the marginal intake rate
falls to the long-run habitat rate. <!-- C5 §1.1 -->

MVT is usually taught with an apology for its self-reference. $R^{*}$ is simultaneously
the departure threshold and the optimised objective, and the graphical
tangent-from-$(-\tau,0)$ construction makes this look like a fixed-point trick rather
than a derivation. The apology is unnecessary, and the reason is the subject of this
paper.

## The Gittins index

For a family of alternative bandit processes, each arm $i$ in state $x$ carries an index
$$\nu_\delta(x) \;=\; \sup_{\sigma>0}\;
\frac{\mathbb{E}\!\left[\int_0^{\sigma} e^{-\delta u} r(u)\,du\right]}
     {\mathbb{E}\!\left[\int_0^{\sigma} e^{-\delta u}\,du\right]},$$
the supremum being over positive stopping times, and playing the arm of greatest index is
optimal [@gittins1979; @gittins2011]. Equivalently, in Whittle's retirement formulation,
$\nu_\delta(x)=\delta M(x)$ where $M(x)=\inf\{M: V(x,M)=M\}$ is the retirement reward that
makes the decision-maker indifferent. <!-- C5 §1.2; both forms verified verbatim by text
extraction from arXiv:2405.01157 -->

The retirement reward is a *stock* and the foraging threshold is a *rate*; the bridge
object is $\delta M$, not $M$. This matters because $M^{*}=R^{*}/\delta \to \infty$ in the
undiscounted limit while $\delta M$ stays finite at $R^{*}$. <!-- C5 §5.1 -->

## What "same object" means

We do not claim that MVT is *analogous to*, *a special case of*, or *recoverable from* the
index. We claim the two maximisations are literally the same supremum of the same ratio.
Charnov's maximisation over patch residence time is the supremum over stopping times in
the definition of the Gittins index, applied to a particular arm; $R^{*}$ is the index of
that arm. Two objects that are the same supremum of the same ratio are one object.

## The closest prior statement is a denial

The relation is not in the literature, and the nearest approach to it goes the wrong way.
Kilpatrick, Davidson & El Hady, *Normative theory of patch foraging decisions*
[@kilpatrick2020], devote a subsection --- *Patch foraging as modified multi-armed bandit*
--- to exactly this comparison. The word "Gittins" occurs once in the paper, in reference
[60], which is Banks & Sundaram's *Switching costs and the Gittins index*. The body gets
as far as "patch foraging is fairly well described by a non-stationary bandit with
switching costs" and then concludes, verbatim, that "as formulated these are still
different decision problems". <!-- C5 §11.3 -->

That sentence is the strongest prior art we found, and it is a denial rather than a
statement. Its specific error is diagnosable: travel time is read as a switching cost,
which it is not (Section 3.3). Nearby papers hold both halves without joining them ---
Averbeck [@averbeck2015] names Gittins indices and the marginal value theorem in one MDP
framework and never relates them, and does not cite Charnov at all; Geana, Wilson, Daw &
Cohen [@geana2016] contrast MVT-type and bandit paradigms explicitly and never name the
index; McNamara & Houston [@mcnamara1985] name the two-armed bandit *and* MVT in one paper
and state MVT's circularity, with zero occurrences of "Gittins" or "index". <!-- C5 §8,
§11.3 -->

# The identity

Continuous time. An unlimited supply of statistically identical patches; travel costs
$\tau>0$ at zero reward; a patch left behind is never revisited; the habitat is
stationary.

## The index of the current patch

Take the occupied patch as an arm. It is deterministic, so its state is elapsed residence
time $t$, and operating it for a further $u$ yields rate $g'(t+u)$. At $\delta=0$ the
index definition gives
$$\nu_0(t) \;=\; \sup_{s>0}\;\frac{g(t+s)-g(t)}{s},$$
the maximal forward chord slope of the gain curve from $t$. For concave $g$ the chord
slope is decreasing in $s$, so the supremum is approached as $s\to0^{+}$ and
$$\nu_0(t) = g'(t) \qquad \text{for concave } g. \tag{1}$$
The Gittins index of a deterministic, concave, depleting patch is exactly its
instantaneous intake rate. <!-- C5 §2 -->

Two remarks are load-bearing. First, concavity does real work: for non-concave (sigmoid)
$g$ the supremum is attained at an interior $s>0$ and $\nu_0(t)>g'(t)$ strictly, the index
returning the slope of the *concave hull* of $g$ --- which is the correction foraging
theory applies by hand. Second, $\delta$ drops out of (1): any weighted forward average of
a decreasing $g'$ is at most $g'(t)$, so the supremum sits at $s\to0^{+}$ for every
$\delta\ge0$. All the discount dependence in the final rule lives in the outside option.

Passing $\delta\to0$ inside the supremum requires justification. It is cheap here: for
fixed $s$ the ratio is continuous in $\delta$ at $0$ by dominated convergence provided
$g'$ is bounded on $[t,t+s]$ --- the hypothesis of dominated convergence is met because the
integrand $e^{-\delta u}g'(u)$ is then bounded on the compact interval $[0,s]$, uniformly in
$\delta\ge0$, so the constant bound is itself the dominating function --- and under concavity the maximiser is the same point for all
$\delta$, so the interchange is trivial rather than delicate. It would break for unbounded
$g'$, and non-concave $g$ loses the shortcut and needs a genuine uniform-integrability
argument. <!-- C5 §2 -->

## The index of the outside option

**Theorem.** *Let patches be statistically identical, non-revisitable, and have
deterministic concave gain function $g$ with $g(0)=0$, and let travel time be $\tau>0$ at
zero reward in a stationary habitat. Define the* habitat arm *as the single arm whose
reward stream from activation is*
$$r(u) = 0 \ \ \text{for } u\in[0,\tau), \qquad r(u)=g'(u-\tau) \ \ \text{for } u\ge\tau.$$
*Then its undiscounted Gittins index is*
$$\nu_0(\mathrm{habitat}) \;=\; \sup_{t\ge0}\ \frac{g(t)}{\tau+t} \;=\; R^{*}, \tag{2}$$
*the supremum being attained at Charnov's optimal residence time $t^{*}$; and the index
rule "continue the current arm until its index falls to the index of the best alternative"
is exactly $g'(t)=R^{*}$, the marginal value theorem.*

*Proof.* Apply the index definition to the habitat arm at $\delta=0$. A stopping time
$s\le\tau$ yields numerator $0$ and hence ratio $0$. A stopping time $s=\tau+t$ with
$t\ge0$ yields numerator $\int_\tau^{\tau+t} g'(u-\tau)\,du = g(t)$ and denominator
$\tau+t$, hence ratio $g(t)/(\tau+t)$. The supremum over stopping times is therefore
$\sup_{t\ge0} g(t)/(\tau+t)$, which is (2), attained at the maximiser $t^{*}$ of
Charnov's cycle rate. By (1) the current patch has index $g'(t)$, so
$$\text{leave} \iff \nu_0(t)\le\nu_0(\mathrm{habitat}) \iff g'(t)\le R^{*},$$
with equality at the switching instant. $\blacksquare$ <!-- C5 §3, §4 -->

Three things this pins down that the informal statement does not. (i) $R^{*}$ is not "the
average rate, which happens to be the threshold"; it is the index of the arm you would
switch to, which is *why* it is the threshold. (ii) MVT's self-reference is the index's,
and is not circular: the threshold is a property of a different arm, computed by its own
stopping problem, and coincides with the realised rate only because the habitat is
stationary and the forager is optimal. (iii) The tangent-from-$(-\tau,0)$ construction is
the concave-hull step, i.e. the supremum in (2).

## Travel time as a zero-reward prefix

The step that has to be made explicit is what $\tau$ is. The bandit in (2) *is* a
zero-switching-cost bandit --- switching between arms is free, which is what licenses the
index theorem --- and yet $\tau$ does not vanish: it appears as a zero-reward prefix
*inside* the habitat arm's own reward stream, and survives into the denominator of (2).

> Absorbing travel time into the outside arm is legitimate **iff a departed patch is never
> revisited.** Then $\tau$ is paid once per activation of a fresh arm and is a property of
> that arm. If patches may be revisited, $\tau$ is paid on every transition, is a genuine
> switching cost, and the index theorem fails.

<!-- C5 §5.4 -->

This is the assumption Kilpatrick et al.'s "different decision problems" was groping at.
Non-revisitability, not zero travel, is the licence.

## The vanishing-discount limit, and the discounted MVT

The undiscounted limit needs no limit argument. The foraging problem is regenerative:
travel plus patch is a renewal cycle, so by renewal--reward the long-run average rate of
any cycle policy is $\mathbb{E}[\text{cycle reward}]/\mathbb{E}[\text{cycle length}]$, and
maximising it over the cycle's stopping rule is (2) verbatim. The average-reward index
*is* the renewal--reward ratio, obtained directly; the $\delta\to0$ limit merely reproduces
the same number, a consistency check rather than the proof. This sidesteps the standard
technical soft spot of vanishing-discount arguments for average-reward bandits.
<!-- C5 §5.2 -->

With $\delta>0$ the identity generalises rather than breaking. The current-patch index
stays $g'(t)$, and
$$\nu_\delta(\mathrm{habitat}) \;=\; \sup_{t}\;
\frac{\delta\, e^{-\delta\tau}\int_0^{t} e^{-\delta u} g'(u)\,du}{1-e^{-\delta(\tau+t)}},
\tag{3}$$
with rule $g'(t)=\nu_\delta(\mathrm{habitat})$; (3) $\to R^{*}$ as $\delta\to0$. There is
therefore a discounted marginal value theorem, and it is MVT with $R^{*}$ replaced by the
discounted habitat index. The $e^{-\delta\tau}$ factor devalues the delayed fresh patch,
lowering the outside index, so the forager stays longer. <!-- C5 §5.3 -->

This is independently corroborated by a rediscovery. Zylberberg (2024), in a preprint titled
*Generalized marginal value theorem with temporal discounting* [@genmvt2024], derives a
departure threshold matching instantaneous reward rate to $\lambda\cdot EV$ --- the
discount rate times the expected value function, which is $\delta M$, which is Whittle's
calibration --- and contains no occurrence of Gittins, bandit, index policy, or Whittle.
Its two-sided empirical claim also falls out of the decomposition above as separate terms:
depleting (concave) patches have a pinned current-arm index and only the outside index
moves, so stronger discounting causes over-staying; delayed-reward patches are non-concave,
so $\nu_\delta(t)>g'(t)$ raises the current arm's index and causes under-staying. Two
signs, two mechanisms, one framework. <!-- C5 §5.3 -->

## The three failure boundaries

| Condition | Verdict | Bandit-literature name |
|---|---|---|
| Patches renew/regrow while the forager is away | Breaks; only a heuristic index survives | **Restless bandit** [@whittle1988] --- arms not frozen when passive; Gittins' theorem does not apply |
| Patches are revisitable ($\tau$ paid per transition) | Breaks structurally | **Switching costs** [@banks1994] --- no optimal index policy of any kind exists |
| Habitat non-stationary | Breaks on both sides | **Non-stationary bandit** --- $R^{*}$ undefined; the index is not a function of state alone |

<!-- C5 §6 rows 5, 6, 7. The Banks & Sundaram citation is verified; the specific claim that
no optimal index policy exists under switching costs comes from secondary descriptions ---
the primary paper was not obtained. -->

Two further rows hold rather than break, and are worth stating because they are places
where MVT is wrong and the index is right. Non-concave gain curves: naive MVT's
$g'(t)=R^{*}$ gives the wrong departure time, while the index self-corrects to the
concave-hull rule. Informative patches, where the forager learns quality from its own
catches: the state is a posterior, $\nu(x)\ge\mathbb{E}[\text{immediate rate}]$ with strict
inequality whenever residual uncertainty remains, so the optimal residence time is *longer*
than MVT predicts by a signed exploration bonus. The documented anomaly is over-staying,
consistently, across 26 surveyed studies [@nonacs2001]. <!-- C5 §6 rows 2, 4; §7 -->

The failure boundaries are the strongest evidence for the correspondence. The identity
breaks in exactly the three places where the bandit literature already knows the Gittins
theorem breaks, and those three map onto three real complications in foraging. A
correspondence whose failure modes correspond too is more likely to be the right one.

# The restless extension

Of the three breaks, only regrowth is a heuristic failure rather than a structural one, so
it is the one that can be pushed through.

## Model

One patch is an arm; the forager activates one at a time. Normalise $G_{\max}=1$, so the
state *is* the giving-up density (GUD) at departure. **GUD is used here in Charnov's sense:
the residual resource density in the patch at the moment of departure under pure rate
maximisation.** This is narrower than the operational quantity of @brown1988, for which the
harvest rate at departure equals $H = C + P + \mathrm{MOC}$ --- metabolic cost, predation
cost, and the missed-opportunity cost of not doing something else. In the present model $C$
and $P$ have no separate term; they would enter as shifts in the shadow price $V'(x)$, which
is what prices the resource left behind. The sign result $d\mathrm{GUD}/dr>0$ below is stated
for the Charnov quantity. State $x\in[0,1]$; active,
$\dot x=-\lambda x$ with reward rate $\lambda x$; passive, $\dot x = r(1-x)$ with reward
rate $0$; travel $\tau$ per transition; $\delta\to0$. Starting a visit at $x=1$ the active
dynamics integrate to $g(t)=1-e^{-\lambda t}$, Charnov's concave gain in its standard
exponential-saturation form, with $g'(t)=\lambda x(t)$. So $\lambda x$ *is* the marginal
value and MVT reads $\lambda x^{*}=R^{*}$. Setting $r=0$ freezes the arm and recovers the
classical bandit. <!-- C25 §1 -->

## Indexability

Whittle's relaxation replaces "exactly one arm active" by "one active on average", attaches
a subsidy $\nu$ per unit time passive, and solves the single-arm average-reward problem.
The HJB equation for relative value $V$ and gain $\rho$ is
$\rho=\max\{\lambda x - \lambda x V'(x),\ \nu + r(1-x)V'(x)\}$, so passivity is preferred
exactly when $\nu \ge \lambda x - V'(x)[\lambda x + r(1-x)]$: **the Whittle index is the
immediate intake rate minus the shadow value of the resource you consume by staying**, and
MVT is the special case $V'\equiv0$. Indexability requires the passive set
$P(\nu)=\{x: W(x)\le\nu\}$ to grow monotonically from $\emptyset$ to $[0,1]$ as $\nu$
sweeps the line. With $W$ from (4) below, $W'(x)=2\lambda x + 2r(1-x)>0$ for all
$x\in(0,1)$ and $\lambda,r>0$, so $W$ is a strictly increasing continuous bijection
$[0,1]\to[-r,\lambda]$ and $P(\nu)=[0,W^{-1}(\nu)]$ is nested. The problem is **indexable
unconditionally** --- no parameter restriction, nothing to check. This places the model
inside the monotone/threshold families of @whittle1988, @ninomora2001 (partial conservation
laws) and @glazebrook2006 rather than requiring their machinery; the single-threshold
structure they establish for harder cases is here direct. <!-- C25 §2; the three DOIs,
titles, authors and journals verified against api.crossref.org/works/{doi}, 2026-09-05 -->

## The index

The relaxed single-arm optimum is bang-bang with a singular arc: at indifference level $a$
the active fraction holding $\dot x=0$ is $u^{*}(a)=r(1-a)/[\lambda a + r(1-a)]$, with gain
$\rho(a)=A(B+\nu)/(A+B)$, $A=\lambda a$, $B=r(1-a)$. Setting $\partial\rho/\partial a=0$ and
clearing $r>0$ gives
$$\boxed{\;W(x) \;=\; \lambda x^{2} \;-\; r(1-x)^{2}\;} \tag{4}$$
Cross-check: substituting (4) into the passivity condition gives
$V'(x)=[\lambda x(1-x)+r(1-x)^{2}]/[\lambda x + r(1-x)] = 1-x$, hence $V(x)=x-x^{2}/2$, and
substituting $V'=1-x$ back into the HJB equation reproduces (4) identically. The shadow
price of standing resource is $1-x$, the *room left to grow*: resource in a full patch is
worthless because the patch is capped and cannot bank it. Reading (4): $\lambda x^{2}$ is
the immediate rate $\lambda x$ discounted by the fraction $x$ of it that represents
bankable resource; $-r(1-x)^{2}$ is the regrowth forgone by occupying the patch instead of
letting it refill. Both terms push the same way --- stay less. <!-- C25 §3 -->

**What zero switching delay does and does not cost us.** Equation (4) is derived for zero
switching *delay*: the relaxed single-arm problem has no transit interval. Reinstating travel
changes the state the forager arrives at, because during a transit of length $\tau$ every
passive patch advances under $\dot x = r(1-x)$. Three consequences, and no more. (i) Within a
single patch type, transit does not disturb the priority order: $W$ is strictly increasing in
$x$ and the passive flow is order-preserving on $[0,1]$, so patches of a common $r$ keep their
rank across the transit. (ii) Across types with different $r$, rank *can* change during
transit, because two patches advance by different amounts over the same $\tau$; the ranking at
departure is therefore not the ranking at arrival, and this is exactly the between-type
contrast the prediction rests on. (iii) $\tau$ enters only through the renewal-cycle anchor
that fixes the global subsidy $\nu$ --- so a habitat mixing patch types has **one** $\nu$, set
by the network as a whole, not one $\nu$ per type. Nothing here supplies the optimality gap
that a genuine switching-delay analysis would; see Limitations items 2 and 3.

## The two limits

**$r\to0$, patches revisitable.** $W(x)\to\lambda x^{2}$, which is *not* MVT. The gap is
not an error: with revisits allowed, resource left behind is not lost, so $V'=1-x\neq0$ and
the index correctly deducts it. This quantifies the switching-cost break that Section 2.5
could only name.

**$r\to0$, patches non-revisitable.** A departed patch is gone, so its stored resource has
value $0$ and $V'\equiv0$ by fiat. Then $W(x)=\lambda x = g'(t)$ and the leaving rule
$W(x^{*})=\nu(\mathrm{habitat})$ reads $g'(t^{*})=R^{*}=\max_t g(t)/(\tau+t)$, which is
equation (2) exactly. The reduction passes, and it passes *conditionally on precisely the
condition identified as the licence* in Section 2.3 --- a stronger result than an
unconditional pass would have been.

**$r\to\infty$.** $W(x)\to-\infty$ for every $x<1$, with $W(1)=\lambda$: skim the top of a
patch that is always full, travel, repeat. Numerically $r/\lambda=10^{6}$ gives
$\mathrm{GUD}=0.99905$, $t^{*}=9.5\times10^{-4}$. <!-- C25 §4 -->

## The prediction, and the degeneracy that precedes it

**State the degeneracy first.** $W$ is strictly increasing in $x$, so in a habitat of
*identical* patches $\arg\max_i W(x_i)=\arg\max_i x_i$: the Whittle priority rule collapses
to "visit the fullest patch", and the $r$-dependence cancels out of it entirely. The index
carries no testable signal in a homogeneous habitat. It bites only across patch types that
differ in $r$ (or $\lambda$), so **any test must be a between-patch-type contrast.** This is
the single most important design constraint the derivation imposes. <!-- C25 §5 -->

Fix the habitat indifference index $\nu$ --- the equilibrium Whittle subsidy, the restless
analogue of $R^{*}$ --- and anchor it so the rule agrees with MVT at $r=0$:
$\nu=\lambda\,\mathrm{GUD}_{\mathrm{MVT}}^{2}$. With $\rho\equiv r/\lambda$ and
$u_0\equiv\mathrm{GUD}_{\mathrm{MVT}}$, solving $W(x)=\nu$ gives
$$\mathrm{GUD}(\rho) = \frac{-\rho+\sqrt{\rho+u_0^{2}(1-\rho)}}{1-\rho},
\qquad \mathrm{GUD}(1)=\tfrac{1}{2}(1+u_0^{2}), \tag{5}$$
and implicit differentiation of $W(x)=\nu$ gives the one equation of the extension:
$$\frac{d\,\mathrm{GUD}}{dr} \;=\;
\frac{(1-\mathrm{GUD})^{2}}{2\left[\lambda\,\mathrm{GUD} + r(1-\mathrm{GUD})\right]}
\;>\;0. \tag{6}$$
Strictly positive everywhere. **Faster regrowth implies a higher giving-up density**; the
residence corollary holds only at a fixed arrival state, and once arrival is taken
self-consistently the residence ratio is non-monotone in $r$ (Table 1). The small-$r$ expansion is
$\mathrm{GUD}(r)\approx u_0 + [(1-u_0)^{2}/(2u_0)](r/\lambda) = 0.300 + 0.817\,(r/\lambda)$
at $u_0=0.30$. <!-- C25 §5 -->

Table 1 ($\lambda=1$, $\lambda\tau=1$ so $r\tau=r/\lambda$; $G_{\max}=1$; $u_0=0.30$),
generated by `vault/_scripts/c25_whittle.py`. Residence times are taken at the arrival state
the model's own passive dynamics deliver in a round-robin steady cycle,
$x_{\mathrm{arr}}=1-(1-\mathrm{GUD})e^{-r\tau}$, so
$t^{*}=\ln(x_{\mathrm{arr}}/\mathrm{GUD})/\lambda$ against
$t^{*}_{\mathrm{MVT}}=\ln(1/u_0)/\lambda=1.204$; an earlier version forced arrival to a full
patch ($x=1$), a state the passive dynamics forbid in steady state, which overstated the ratio
by up to a factor of 3.8 and concealed that the ratio is *non-monotone* in $r$ --- rising from
$0$ at $r\tau=0$, peaking at $0.356$ near $r\tau=2$, and falling back toward $0$ as
$r\to\infty$. The $\mathrm{GUD}/\mathrm{GUD}_{\mathrm{MVT}}$ column is a ratio *at this anchor*:
run forward as a policy in a 20-patch network the same anchor returns $1.271$ and a learned
$\nu$ returns $1.060$, so the magnitude is anchor-dependent and only the sign is not:

| $r\tau$ | $\mathrm{GUD}(r)$ | $\Delta\mathrm{GUD}$ | $\mathrm{GUD}/\mathrm{GUD}_{\mathrm{MVT}}$ | $x_{\mathrm{arr}}$ | $t^{*}(r)$ | $t^{*}/t^{*}_{\mathrm{MVT}}$ |
|---|---|---|---|---|---|---|
| 0.05 | 0.3348 | +0.0348 | 1.116 | 0.3673 | 0.092 | 0.077 |
| 0.20 | 0.4019 | +0.1019 | 1.340 | 0.5103 | 0.239 | 0.198 |
| 1.00 | 0.5450 | +0.2450 | 1.817 | 0.8326 | 0.424 | 0.352 |
| 10.00 | 0.7743 | +0.4743 | 2.581 | 1.0000 | 0.256 | 0.212 |

<!-- C25 §5 table, rows r·τ ∈ {0.05, 0.2, 1, 10}; MVT baseline GUD = 0.3000, t*_MVT = 1.204; steady-cycle arrival, corrected 2026-09-05 (audit 06) -->

**The falsifiable statement.** Two patch types in one habitat, matched in $G_{\max}$ and
$\lambda$, differing only in measured regrowth rate $r$. MVT predicts *equal* giving-up
densities, because the threshold $R^{*}$ is a habitat property and not a patch property.
The Whittle rule predicts the fast type is left at a strictly higher standing crop, by the
amount in (5)--(6). A measured $\Delta\mathrm{GUD}$ of zero within error falsifies the
transfer; a *negative* $\Delta\mathrm{GUD}$ falsifies the transfer and MVT together. A
20-patch network simulation of this rule recovers a fast/slow GUD ratio of $1.271$ at the
MVT anchor $\nu=\lambda u_0^{2}$ used above and $1.060$ when $\nu$ is instead learned as the
network's realised long-run intake rate, so the quantity a field test should be powered for
is a between-type GUD ratio in $[1.06,\,1.27]$ at $r\tau=0.2$, not a single number.

# A test

Kadmon & Shmida (1992), *Evolutionary Ecology* 6:142--151 [@kadmonshmida1992], report
departure rules of *Anthophora* and *Eucera* bees on *Anchusa strigosa*, giving departure
probability as a function of the reward received at the last two flowers. Kadmon (1992),
*Oecologia* 92:552--555 [@kadmon1992], measures nectar renewal in the *same
plant--pollinator system*. Both DOIs, titles, authors, journals and years were verified
against `api.crossref.org/works/{doi}`, fetched 2026-09-05, with `is-referenced-by-count`
62 and 16 respectively. <!-- C25 §6 -->

The pair is rare in measuring $r$ and the departure decision on one system, which is what
makes it the natural parameterisation. What a test needs is: (i) $r$ measured per patch
type independently of the forager; (ii) standing crop at the moment of departure, per patch
type; (iii) at least two patch types differing in $r$ with $G_{\max}$ and $\lambda$
matched; (iv) $\tau$ between patches. Kadmon & Shmida give (ii) only in the coarse form of
a departure probability against last-flower reward, and do not stratify by renewal rate. The
pair therefore **motivates and parameterises** the test but does not run it. The clean
version is a manipulation: artificial flowers on two programmed refill rates, interleaved in
one array. Possingham (1989) [@possingham1989] and Ohashi & Thomson (2005)
[@ohashi2005] are related but unsuitable as-is --- both are models or simulations, not
measured foragers. <!-- C25 §6 -->

**Caveat, and it is not small.** Kadmon (1992) measured *linear* renewal in *Anchusa*,
$\dot x = \mathrm{const}$ up to a cap, not the saturating-exponential $\dot x = r(1-x)$
assumed in Section 3.1. The derivation runs the same way with linear renewal, but (4)
changes. The *sign* of (6) survives; the coefficients in Table 1 do not. Applying Table 1
numerically to *Anchusa* would be wrong. <!-- C25 §7 -->

# Evidence that the two literatures have not met

Anchors are the primary works: Charnov 1976 (`10.1016/0040-5809(76)90040-X`) and Gittins
1979 (`10.1111/j.2517-6161.1979.tb01068.x`); no proxy substitution was needed.
OpenCitations and Crossref returned the identical five DOIs.

| | $|A|$ | $|B|$ | observed | $N$ floor | $E$ | $O/E$ |
|---|---|---|---|---|---|---|
| **Gap:** Gittins $\times$ Charnov | 1,013 | 5,424 | **5** | 6,432 | 854 | **0.0059** |
| **Control:** Gittins $\times$ Auer 2002 | 1,013 | 3,906 | **225** | 4,694 | 843 | **0.267** |

<!-- G28 (intersection, controls, denominators); citation-intersection (null model, O/E,
control ratio) -->

As percentages of the enumerated Gittins base, the intersection is $5/1{,}013 = 0.49\%$
against a positive control of $225/1{,}013 = 22.2\%$. The base of 1,013 is the citer set
actually enumerated at run time on 2026-09-03 (provider not recorded; OpenCitations COCI is
the likely source). Crossref's `is-referenced-by-count` for the same DOI was 986,
OpenCitations' citation count 1,026, and OpenAlex's `cited_by_count` 1,544, all fetched
2026-09-05; the percentages are not recomputed against these. The control partner is Auer,
Cesa-Bianchi & Fischer 2002 (`10.1023/A:1013689704352`), DOI verified against Crossref
2026-09-05, `is-referenced-by-count` 3,906 [@auer2002].

**The statistic to quote is the control ratio, not the raw count or $O/E$.** Under
independence, $E = |A|\cdot|B|/N_{\text{universe}}$, and $E\propto 1/N$, so a gap that looks
decisive at one denominator vanishes at another: at $N=10^{6}$ the expected Gittins
$\times$ Charnov count falls to 5.5 and $O/E\approx0.91$, indistinguishable from chance. $N$
cancels when the same universe is used for gap and control, giving
$$\frac{(O/E)_{\text{gap}}}{(O/E)_{\text{control}}}
= \frac{O_{\text{control}}/|B_{\text{control}}|}{O_{\text{gap}}/|B_{\text{gap}}|}
= \frac{225/3{,}906}{5/5{,}424} = \frac{0.0576}{0.000922} = 62.5 .$$
The headline "factor of 45" that comes from dividing both percentages by the same 1,013
base ignores that the two partner sets differ in size; correcting for that moves 45 to
**62.5**, so the isolation is slightly stronger than the uncorrected figure, and is now
stated in a form that does not depend on which Gittins citer count is used.

All five works in the intersection were inspected. **None is a bridge.** Bhat, Bénichou &
Redner (2018, *Phys. Rev. E*), read in full, cites both in separate background lists and
never uses the phrase "marginal value theorem". Lejarraga & Hertwig (2016), read in full,
is the sharp near-miss: it states that no general optimal solution to the explore/exploit
tradeoff has been proposed, "(but see Gittins, 1979)", and separately uses Charnov's rule.

**The one exception.** Griebling, Johnson & Benson-Amram (2026), *Raccoons optimally forage
for information: exploration--exploitation trade-offs in innovation*, *Animal Behaviour*,
`10.1016/j.anbehav.2026.123491` [@griebling2026], is the only document known to cite
Charnov 1976, Gittins 1979 *and* the Gittins--Glazebrook--Weber monograph together. Its
deposited reference list (100 references) was retrieved from Crossref on 2026-09-05 and
confirmed to contain all three, so the co-citation is established from the primary record
rather than inferred. **Its full text was not obtained** (ScienceDirect returned HTTP 403;
no OA repository copy; no Europe PMC record), and we therefore cannot state that it does
not contain the identity. The abstract, retrieved via OpenAlex, describes an empirical
multi-access-puzzle-box study of captive raccoons with the Gittins citations in an
explore/exploit background frame, which makes it an unlikely place for a theorem; but this
is a judgement about an unread paper and is flagged as such.

# Limitations

In the order a referee will reach for them.

1. **The homogeneous-habitat degeneracy.** $W$ is a monotone function of standing crop, so
   the policy is "visit the fullest patch" --- which is what every forager already does and
   what MVT already implies. The $r$-dependence survives only in a between-type contrast
   requiring an experiment nobody has run. This is correct, which is why Section 3.5 states
   it before the prediction rather than after.

2. **$\tau$ is outside the Whittle relaxation. This is the largest hole.** The index (4) is
   derived for zero switching *delay*. Travel is re-inserted only at the level of the
   renewal cycle and the equilibrium subsidy $\nu$. A restless bandit with switching delay
   is not the problem Whittle solved, and the $r\tau$ axis of Table 1 is therefore a
   *reporting convention* ($\lambda\tau=1$), not a derived scaling.

3. **No optimality gap is stated, and the regime we need is not covered.** Whittle indices
   are optimal only asymptotically, and the Weber--Weiss regime [@weberweiss1990] is many
   arms with a *fixed* active fraction $\alpha=M/N$. A single forager among $N$ patches is
   $M=1$, $N\to\infty$, $\alpha\to0$, which is not the regime that theorem covers. We looked
   for one that does and did not find it. The many-arm literature that sharpens Weber--Weiss
   keeps its hypothesis: Hu & Frazier [@hufrazier2017] and Zhang & Frazier
   [@zhangfrazier2021] work in the finite-horizon version of Whittle's regime with the
   pulled fraction held constant --- the latter obtaining an $O(1)$ rather than
   $O(\sqrt{N})$ gap under a non-degeneracy condition --- and Gast, Gaujal & Yan [@gast2023]
   sharpen the average-reward rate to exponential in $N$ under indexability plus a global
   attractor, again with activations scaling proportionally to arms. The nearest applicable
   object is Brown & Smith's Lagrangian upper bound on the optimal value [@brownsmith2020],
   which is a *finite-$N$* bound and so can be evaluated at $M=1$; but their optimality
   result is likewise stated for many items, so it would certify a numerical bound for a
   given patch network, not an asymptotic guarantee for the index at $\alpha\to0$. The
   single-server queueing literature, where one server does serve many classes
   [@ninomora2001; @glazebrook2006], is the closest structural match to $M=1$, but its
   optimality statements are heavy-traffic limits for a system with arrivals, not
   $N\to\infty$ limits for a fixed set of patches, so they answer a different question. **We
   therefore name the gap rather than close it: the sparse-activation limit $M=1$,
   $\alpha\to0$ --- the regime every foraging application is in --- has no Whittle-index
   performance bound we could locate, and closing it is open work.** The honest status of
   Section 3 is unchanged: an indexable heuristic with a signed comparative static, not a
   bounded approximation. **Simulated, the gap is negative.** In a 20-patch network the
   Whittle policy does *not* out-earn the MVT-with-regrowth rule: it loses $13.3\%$ of
   the intake rate at the pre-registered calibration of $\nu$ and $0.5\%$ when each
   policy is given its own rate-optimal threshold, in every cell of the sweep. **We
   therefore make no claim that the index improves intake.** What the extension claims
   is the signed comparative static (6) and the between-type contrast it implies.

4. **$\nu$ is anchored, not solved.** The equilibrium subsidy is fixed by agreement with MVT
   at $r\to0$ rather than computed from an $N$-patch fixed point. Table 1 is a statement
   about *relative* GUD across patch types at one habitat quality --- which is what the
   falsifiable claim needs --- but not an absolute prediction of GUD.

5. **Modelling assumptions that the named dataset violates or that the model omits.**
   Passive dynamics are assumed saturating-exponential; Kadmon (1992) measured linear
   renewal. Active intake is assumed proportional to standing crop, which
   handling-time-limited foragers violate. Patches are deterministic, the habitat
   stationary, foragers identical, with no learning, no competition and no predation ---
   and GUD in the Brown tradition is a *joint* measure of energetic and predation costs, of
   which this model contains none of the latter. Converting a threshold into $t^{*}$ assumes
   round-robin/symmetric visitation. The singular-arc argument is a continuous-time
   relaxation; the discrete-time index may differ at $O(\Delta t)$, and this was not checked.

Two further limits belong to Section 2 rather than Section 3. The exploration-bonus
inequality $\nu(x)\ge\mathbb{E}[\text{immediate rate}]$ for informative patches is argued
from the structure of the supremum over stopping times but is **not proved here in
generality**; making it a theorem with a computable bonus for a specific posterior family
would be the next step. And the novelty claim rests on four unread full texts: Houston &
McNamara (1999) [@houston1999], Stephens & Krebs (1986) [@stephens1986] and Gittins, Glazebrook & Weber (2011) [@gittins2011], all three
reached only at Google Books term-index level (neither term list contains the crossing
vocabulary; a single sentence below the frequency cutoff could still exist), and Griebling
et al. (2026). The claim is "appears unwritten", not "is unwritten".

<!-- C25 §7, §8; C5 §10, §11.4 -->

# Acknowledgements

An external review by an unnamed language model, dated 2026-09-05 and on file in the
repository at `papers/charnov-gittins/reviews/`, independently recomputed the index, its
derivative, and Table 1, and confirmed them; its three substantive points are addressed in
Section 3 and in Limitations.

# Use of AI tools

This work was produced with substantial use of large language models, disclosed here per ICMJE and COPE guidance. The models are not authors and bear no responsibility for the content. Claude Fable 5.1 (Anthropic, model `claude-fable-5-1`) acted as orchestrator: it reviewed the vault, designed the audit and task briefs, integrated results, and drafted this manuscript's structure. Claude Opus 4.8 (Anthropic) instances, run through Claude Code, carried out the derivations, the literature and citation-database queries, the prior-art searches, the numerical fits, and the first draft of the text, each under a written brief and each reporting sources with provider and fetch date. Every query, count, and correction is logged in the vault (`vault/log.md`, `audits/`). The author set the research question, the scope rule, and the standards of evidence; chose which results to keep, downgrade, or withdraw; and reviewed and takes full responsibility for every claim, derivation, and citation in this paper. No AI tool was used to generate or alter data.

# Data and code availability

All derivations, verification records, provider queries and fetch dates behind this paper
are held as notes in a public research vault: `C5-charnov-gittins` (the identity and the
prior-art check), `C25-whittle-foraging` (the restless extension),
`G28-marginal-value-gittins` (the citation evidence), `Q5-restless-patches` (the open
question), and `method/citation-intersection` (the null model and the control-ratio
statistic). Numerics for Section 3, including the indexability check, the two limits and
Table 1, are reproduced by `vault/_scripts/c25_whittle.py` (Python standard library only).

- Repository: <https://github.com/deciduus/same-object>
- Archived snapshot, Zenodo concept DOI: `10.5281/zenodo.22334047`
- Licence: CC-BY-4.0

# References
