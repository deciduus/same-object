---
name: C5-charnov-gittins
type: computed
---

# Charnov's marginal value theorem is a Gittins index identity

> **Charnov's habitat rate R\* is not *analogous to* an index. It *is* the Gittins index of
> the outside option, in the vanishing-discount limit, and the maximisation over patch
> residence time that defines R\* is literally the supremum over stopping times that defines
> the index.** The travel time τ is neither a switching cost nor zero — it is a zero-reward
> prefix absorbed *inside* the outside arm, which is legitimate exactly when patches are not
> revisitable. The equivalence is exact for deterministic concave patches; it holds and
> *generalises* under discounting; and it **fails in three identified places**, each of which
> is a known hard case in the bandit literature that behavioural ecology has been handling by
> hand.

Closes — or rather, supplies the missing object for — [[G28-marginal-value-gittins]]. Under
[[what-closes-a-gap]] the requirement was a theorem, not a review. This is the theorem, with
the failure boundary stated.

---

## 1. Setup and notation

Continuous time throughout. One symbol set for both fields.

| Symbol | Foraging meaning | Bandit meaning |
|---|---|---|
| `g(t)` | cumulative energy gained after residence time `t` in a patch; `g(0)=0` | cumulative reward from operating an arm for time `t` |
| `g'(t)` | instantaneous intake rate | instantaneous reward rate `r(t)` |
| `τ` | travel time between patches | unproductive prefix of the "habitat arm" |
| `R*` | long-run habitat intake rate | **the index of the habitat arm** (this is the result) |
| `δ` | — | discount rate; `γ = e^{-δh}` per step of length `h` |
| `ν_δ(·)` | — | Gittins index at discount rate `δ` |
| `M` | — | Whittle retirement reward (a **stock**, not a rate) |

**Environment.** An unlimited supply of statistically identical patches. Reaching a new patch
costs travel time `τ > 0` at zero reward. A patch left behind is never revisited. The habitat
is stationary.

### 1.1 Charnov's marginal value theorem

Over one travel-plus-patch cycle of residence time `t`, the rate is

```
R(t) = g(t) / (τ + t)
```

MVT maximises `R` over `t`. With `g` differentiable, the first-order condition is

```
g'(t*)·(τ + t*) − g(t*) = 0
⟹  g'(t*) = g(t*)/(τ + t*) = R(t*) ≡ R*                              (MVT)
```

Leave when the marginal rate falls to the long-run habitat rate. `R*` is simultaneously the
threshold and the optimised objective — the tangent-from-`(−τ, 0)` construction.

### 1.2 The Gittins index, and Whittle's calibration

Both standard definitions, **VERIFIED** by text extraction from
[arXiv:2405.01157](https://arxiv.org/pdf/2405.01157) this session.

Ratio form, quoted verbatim:

> "the Gittins index for arm i in state x, denoted by Gi(x) is given by: Gi(x) = sup σ>0
> Gi(x, σ) where Gi(x, σ) = E{Σ_{t=0}^{σ−1} γ^t r_i(s_t(i), 1) | s_0(i) = x} / E{Σ_{t=0}^{σ−1}
> γ^t | s_0(i) = x}. … The supremum here is over all positive stopping times σ."

Whittle's retirement form, quoted verbatim:

> "you can either pull the arm and collect reward or choose to retire and receive a terminal
> reward M. … the Gittins index for state x is given by G(x) = M(x)(1 − γ) where M(x) = inf
> {M : Vr(x, M) = M}."

In continuous time with `γ = e^{-δh}`, `h → 0`, so `(1−γ) → δh`, these become

```
ν_δ(x) = sup_{σ>0}  E[∫_0^σ e^{−δu} r(u) du] / E[∫_0^σ e^{−δu} du]      (G1)

ν_δ(x) = δ · M(x),    M(x) = inf{M : V(x, M) = M}                        (G2)
```

**(G2) is the first correction to G28's own reading.** The note proposed routing through
Whittle's retirement reward. That is the right route, but the retirement reward `M` is a
*stock* and the foraging threshold is a *rate*. The bridge object is `δM`, not `M`. §5 shows
why this matters: `M → ∞` in the undiscounted limit while `δM` stays finite.

---

## 2. Step 1 — the index of the patch you are in

Take the current patch as an arm. Because the patch is deterministic, its state is fully
described by elapsed residence time `t`. Operating it for a further `s` yields reward rate
`g'(t+u)` at horizon `u ∈ [0, s)`. From (G1):

```
ν_δ(t) = sup_{s>0}  [∫_0^s e^{−δu} g'(t+u) du] / [∫_0^s e^{−δu} du]     (1)
```

Set `δ = 0`. Numerator `→ g(t+s) − g(t)`, denominator `→ s`:

```
ν_0(t) = sup_{s>0}  [g(t+s) − g(t)] / s                                  (2)
```

**Equation (2) is the maximal forward chord slope of the gain curve from `t`.**

Now use concavity. Charnov assumes diminishing returns, i.e. `g` concave, i.e. `g'` decreasing.
For concave `g` the chord slope `[g(t+s) − g(t)]/s` is decreasing in `s`, so the supremum is
approached as `s → 0⁺`, where the chord slope tends to `g'(t)`. Hence

```
ν_0(t) = g'(t)                     for concave g                         (3)
```

> **The Gittins index of a deterministic, concave, depleting patch is exactly its
> instantaneous intake rate.**

Two notes, both load-bearing.

- **Concavity is doing real work.** If `g` is *not* concave — a sigmoid gain curve with an
  accelerating phase, which is common when handling time precedes reward — the supremum in (2)
  is attained at some interior `s > 0` and `ν_0(t) > g'(t)` **strictly**. The index returns
  the chord slope, i.e. the slope of the *concave hull* of `g`. This is exactly the correction
  foraging theory applies by hand to sigmoid gain curves. The index does it automatically. See
  §6, row 2.
- **`δ` drops out of (1) under concavity.** Any weighted forward average of a decreasing `g'`
  is `≤ g'(t)`, so the sup is at `s → 0⁺` for *every* `δ ≥ 0`, giving `ν_δ(t) = g'(t)`. The
  current-patch index is discount-independent. All the `δ`-dependence in the final rule lives
  in the outside option. This is what makes §5 come out cleanly.

**Interchange of limit and supremum (the step not to hand-wave).** Passing `δ → 0` inside
`sup_s` in (1) requires justification. It is available cheaply here: for each fixed `s` the
ratio is continuous in `δ` at `δ = 0` by dominated convergence provided `g'` is bounded on
`[t, t+s]`; and under concavity the sup is attained at the *same* point (`s → 0⁺`) for all
`δ`, so the interchange is trivial rather than delicate. **Where this would break:** if `g'`
is unbounded (unbounded intake rate) the dominating function fails and (3) is not established
by this argument. Non-concave `g` also loses the "same maximiser for all `δ`" shortcut and
needs the genuine uniform-integrability argument. Flagged, not papered over.

---

## 3. Step 2 — the index of the outside option (the theorem)

The alternative to continuing is not "another patch." It is **travel, then a fresh patch**.
Bundle these into one arm — call it the **habitat arm** — whose reward stream from activation is

```
r(u) = 0          for u ∈ [0, τ)          (travelling)
r(u) = g'(u − τ)  for u ≥ τ              (harvesting a fresh patch)
```

Apply (G1) at `δ = 0`. The stopping time `s` can fall in either segment.

- For `s ≤ τ`: numerator is `0`, ratio is `0`.
- For `s = τ + t` with `t ≥ 0`: numerator is `∫_τ^{τ+t} g'(u−τ) du = g(t)`, denominator is
  `τ + t`. Ratio is `g(t)/(τ + t)`.

Therefore

```
ν_0(habitat) = sup_{t ≥ 0}  g(t) / (τ + t) = R*                          (4)
```

**This is the whole result.** The supremum over stopping times in the definition of the
Gittins index, applied to the habitat arm, *is* Charnov's maximisation over patch residence
time. They are the same supremum of the same ratio. Charnov (1976) computed a Gittins index
two years after Gittins & Jones (1974), for a different reason, and neither literature
noticed.

Note also that the *maximiser* coincides: the `t` attaining (4) is `t*`, the MVT-optimal
residence time. So the habitat arm's optimal stopping time is the MVT patch residence time.
This is not an extra assumption; it falls out of the same equation.

---

## 4. Step 3 — the leaving rule

The Gittins index theorem: play the arm of greatest index. Equivalently, continue the current
arm until its index falls to the index of the best alternative. With (3) and (4):

```
leave  ⟺  ν_0(t) ≤ ν_0(habitat)  ⟺  g'(t) ≤ R*
```

with equality at the switching instant. That is **(MVT)**. ∎

Three things this derivation pins down that the informal statement does not:

1. **`R*` is an index, and specifically the index of the outside option.** The MVT threshold
   is not "the average rate, which happens to be the threshold." It is the index of the arm
   you would switch to, which is *why* it is the threshold.
2. **The self-reference in MVT is the index's self-reference.** MVT is often taught as
   awkwardly circular: `R*` is both the threshold and the outcome. In index terms there is no
   circularity — the threshold is a property of a *different* arm, computed by its own
   stopping problem, and it coincides with the realised rate only because the habitat is
   stationary and the forager is playing optimally.
3. **The tangent construction is the concave-hull step.** Charnov's graphical
   tangent-from-`(−τ,0)` is the same operation as taking the sup over stopping times in (4).

---

## 5. The discounting, handled properly — and what τ actually is

This is the crux the brief flagged, and it splits into two questions.

### 5.1 The retirement reward degenerates; the index does not

From (G2), `ν = δM`. Therefore the retirement reward corresponding to the habitat threshold is

```
M* = R* / δ  →  ∞   as δ → 0
```

**Whittle's retirement-reward formulation does not survive the undiscounted limit.** The
lump sum that makes you indifferent to continuing forever at rate `R*` is infinite when
nothing is discounted. The object that survives is the *index* — the rate `δM` — which is
exactly `R*`.

So G28's proposed correction is directionally right and needs one repair: the route does run
through the calibration/retirement formulation, but one must work with `δM` throughout. Stated
as "τ maps to the retirement option," it is wrong; stated as "the threshold is the retirement
*rate* of the outside arm," it is right.

### 5.2 The undiscounted limit needs no limit argument at all

The clean route avoids `δ → 0` entirely. The foraging problem is **regenerative**: travel plus
patch is a renewal cycle. By renewal–reward, the long-run average rate of any cycle policy is
`E[cycle reward]/E[cycle length]`, and maximising that over the cycle's stopping rule is (4)
verbatim. **The average-reward index is the renewal-reward ratio, obtained directly.** The
vanishing-discount limit then merely *reproduces* the same number, which is a consistency
check rather than the proof. This matters because vanishing-discount arguments for
average-reward bandits are the standard technical soft spot; here they can be sidestepped.

### 5.3 With discounting the equivalence generalises rather than breaking

Keep `δ > 0`. By §2 the current-patch index stays `g'(t)` under concavity. The habitat index
becomes, using `∫_0^{τ+t} e^{−δu} du = (1 − e^{−δ(τ+t)})/δ`:

```
                       δ · e^{−δτ} · ∫_0^t e^{−δu} g'(u) du
ν_δ(habitat) = sup_t  ─────────────────────────────────────                (5)
                            1 − e^{−δ(τ+t)}
```

and the rule is `g'(t) = ν_δ(habitat)`. As `δ → 0`, (5) → `sup_t g(t)/(τ+t) = R*`. ✓

So there is a **discounted marginal value theorem**, and it is just MVT with `R*` replaced by
the discounted habitat index. The `e^{−δτ}` factor penalises travel: discounting devalues the
delayed fresh patch, lowering the outside index, so the forager **stays longer**.

**Independent corroboration, and it is strong.** Someone has derived precisely this threshold
in the foraging vocabulary without knowing it was Whittle's calibration. *Should I stay or
should I go? Generalized marginal value theorem with temporal discounting*
([bioRxiv 2024.10.28.620618](https://www.biorxiv.org/content/10.1101/2024.10.28.620618v1.full),
**VERIFIED by fetch**) obtains a departure threshold in which the instantaneous reward rate is
matched to **`λ · EV`** — the discount rate times the expected value function. That is `δM`.
It is (G2). The paper contains **no occurrence of Gittins, bandit, index policy, or Whittle**
(verified by fetch). It has rediscovered the Whittle calibration identity from scratch.

Better still, its two-sided empirical claim falls out of the two mechanisms above as separate
terms. That paper reports that stronger discounting causes **over-staying for monotonically
depleting patches** and **under-staying for patches with delayed rewards**. In the index
decomposition:

- *Depleting patches* are concave. Current-patch index is pinned at `g'(t)`; only the outside
  index moves, and `e^{−δτ}` lowers it. Threshold falls ⟹ **over-stay.** ✓
- *Delayed-reward patches* are **non-concave** (an accelerating phase). Now §2's exception
  bites: `ν_δ(t) > g'(t)` strictly. The current arm's index is raised above its instantaneous
  rate, so it crosses the threshold sooner ⟹ **under-stay.** ✓

Two signs, two mechanisms, one framework. The index formulation explains a result the foraging
derivation reports as a case distinction.

### 5.4 What τ actually is — resolving G28's own correction

G28's original wording called MVT the "zero-switching-cost limit" of Gittins, then corrected
itself on the grounds that MVT *has* a switching cost, τ. **Both halves are half right, and
the derivation says exactly which half.**

- The bandit in §3 **is a zero-switching-cost bandit.** Switching between arms is free. This is
  what licenses the index theorem.
- τ **does not vanish.** It appears as a zero-reward prefix *inside* the habitat arm's own
  reward stream, and it survives into the answer — it is the `τ` in the denominator of (4).

So τ is neither a switching cost nor zero: **it is absorbed into the definition of the outside
arm.** The precise statement:

> Absorbing travel time into the outside arm is legitimate **iff a departed patch is never
> revisited.** Then τ is paid once per activation of a fresh arm and is a property of that
> arm. If patches may be revisited, τ is paid on every transition, is a genuine switching
> cost, and the index theorem fails (§6, row 6).

That is a sharper statement than either version in G28, and it identifies the exact assumption
— non-revisitability — that the original phrasing was groping at.

---

## 6. Where it holds and where it breaks

| # | Condition | Verdict | What actually happens |
|---|---|---|---|
| 1 | Deterministic, concave `g`; non-revisitable patches; stationary habitat; `δ → 0` | **HOLDS exactly** | §2–§4. MVT and the Gittins rule are the same equation. |
| 2 | Non-concave (sigmoid) `g` | **Index holds; naive MVT is WRONG** | `ν_0(t) = ` max forward chord slope `> g'(t)`. `g'(t) = R*` gives the wrong departure time; the index gives the concave-hull rule automatically. |
| 3 | Stochastic patch yields, distribution **known**, no learning | **HOLDS in expectation** | State is still elapsed time; (1)–(4) run with `E[g]`. |
| 4 | Stochastic patches, forager **learns patch quality from its own catches** | **MVT FAILS; index holds** | The state is now a posterior, and the sup over stopping times captures option value. `ν(x) ≥ E[immediate rate]`, **strictly** whenever residual uncertainty remains. MVT is not merely noisy here — it is **biased in one direction**. See §7. |
| 5 | Patches **renew/regrow while the forager is away** | **BREAKS** | Arms are no longer frozen when not played. This is a **restless** bandit; the Gittins theorem does not apply, and only Whittle's index (heuristic, requires indexability, optimal only asymptotically) is available. MVT's `R*` fails for the same reason. |
| 6 | Patches are **revisitable** (τ paid per transition) | **BREAKS structurally** | τ becomes a true switching cost and can no longer be absorbed into an arm. **Banks & Sundaram (1994)** — no optimal index policy exists under switching costs. Not an approximation failure: no index rule of any kind is optimal. |
| 7 | **Non-stationary** habitat | **BREAKS on both sides** | `R*` is undefined; the arms' reward processes are time-inhomogeneous, so the index is not a function of state alone. |
| 8 | `δ > 0`, everything else as row 1 | **HOLDS, generalised** | Eq. (5). The threshold is the discounted habitat index, not `R*`. Reproduces the two-sided discounting result of §5.3. |

**The honest summary.** The equivalence is exact in the classical case and in the discounted
case. It breaks in exactly the three places where the *bandit* literature already knows the
Gittins theorem breaks — restlessness, switching costs, non-stationarity — and those three map
onto three real and well-known complications in foraging: patch renewal, patch revisiting, and
changing environments. **The correspondence is faithful enough that its failure modes
correspond too.** That is stronger evidence that it is the right correspondence than the
positive result alone.

---

## 7. The one place this makes a testable prediction

Row 4 deserves its own statement, because it converts the identity into an empirical claim.

When patch quality is uncertain and the forager's own intake is informative about it, the
index exceeds the immediate expected rate:

```
ν(x) − E[g'(t) | x]  ≥  0,   strictly > 0 with residual uncertainty
```

because the sup over stopping times can wait for good news and stop on bad. This difference is
an **exploration bonus**, and it is **signed**. Therefore:

> Where patches are informative, the optimal residence time is **longer** than MVT predicts,
> by an amount equal to the exploration bonus.

The documented empirical anomaly in foraging is over-staying, and it is systematic.
**Nonacs (2001)**, *State dependent behavior and the Marginal Value Theorem*, *Behavioral
Ecology* 12(1):71–83
([fetched](https://academic.oup.com/beheco/article/12/1/71/392385), **VERIFIED**): 26 studies
surveyed, and — quoted verbatim from the abstract — "foragers rather consistently 'erred' in
staying too long in patches."

Nonacs attributes this to state dependence. The index derivation supplies a **second,
independent, and non-competing** contributor with the same sign, present even for a
state-independent energy-maximising forager, provided only that patches are informative. It is
also quantitative: the bonus is computable from the posterior, so the two explanations are
separable by manipulating patch *informativeness* while holding energetic state fixed. That is
a discriminating experiment in the sense of METHOD §3, and it does not appear to have been run.

---

## 8. Prior art

Checked this session. **No statement of the relation was found.** Under the classification
scheme of [[what-closes-a-gap]], G28 remains a **TRUE GAP**.

| Source | Checked how | Result |
|---|---|---|
| Wikipedia, *Gittins index* | fetched | **VERIFIED**: "does not mention foraging, Charnov, or the marginal value theorem anywhere." |
| Geana, Wilson, Daw & Cohen (2016), *Information-Seeking, Learning and the Marginal Value Theorem*, CogSci 38 ([PDF](https://escholarship.org/content/qt5339f64z/qt5339f64z.pdf)) | full text extracted locally | **VERIFIED: no occurrence of Gittins or Whittle.** Explicitly contrasts MVT-type and "bandit" scenarios as the two paradigms and *still* never names the index. A second "best-placed paper," arguably better placed than Averbeck 2015. |
| *Generalized marginal value theorem with temporal discounting* (2024), [bioRxiv 2024.10.28.620618](https://www.biorxiv.org/content/10.1101/2024.10.28.620618v1.full) | fetched | **VERIFIED: no Gittins, bandit, index policy, or Whittle.** Independently derives `g'(t*) = λ·EV`, which is Whittle's `ν = δM`. **Rediscovery, not prior art.** Strongest single piece of evidence that the gap is real *and* that the algebra is right. |
| *Normative theory of patch foraging decisions*, [arXiv:2004.10671](https://arxiv.org/abs/2004.10671) | abstract fetched only | No Gittins/bandit/index in abstract. **Full text not obtained** — provisional. |
| Gittins, Glazebrook & Weber, *Multi-armed Bandit Allocation Indices*, 2nd ed. | ToC PDF fetched but **scanned images, no text layer** | **NOT OBTAINED.** Cannot exclude. |
| Stephens & Krebs, *Foraging Theory*; Houston & McNamara, *Models of Adaptive Behaviour* | not obtainable | **NOT OBTAINED.** G28 already flags Houston & McNamara as the most likely hiding place; this entry stays provisional on it. |

**Supporting citations used above, verification status:**

- Gittins ratio definition; Whittle retirement `G(x) = M(x)(1−γ)` — **VERIFIED**, text
  extracted from [arXiv:2405.01157](https://arxiv.org/pdf/2405.01157).
- Banks, J. S. & Sundaram, R. K. (1994). *Switching costs and the Gittins index.*
  **Econometrica** 62(3), 687–694 — **citation VERIFIED** by bibliography extraction from
  [arXiv:1808.06314](https://arxiv.org/pdf/1808.06314), which lists it under "MAB processes
  with switching cost/delay." The specific claim *that no optimal index policy exists under
  switching costs* comes from secondary descriptions; **the primary paper was not obtained**
  and that claim is marked **UNVERIFIED at the primary source**.
- Nonacs (2001) — **VERIFIED** by fetch, quoted above.
- Gittins & Jones (1974), Whittle (1980), Whittle (1988) restless bandits — standard
  attributions, **not independently fetched this session**.

---

## 9. What each field gains

### Behavioural ecology gains

1. **A correct rule where MVT is provably wrong.** Rows 2 and 4. For sigmoid gain curves and
   for informative patches, MVT's `g'(t) = R*` is not an approximation — it is the wrong
   equation, and the index is the right one.
2. **A signed, quantitative, independent account of the over-staying anomaly** (§7), separable
   from state dependence by an experiment nobody has run.
3. **A negative result worth having.** Banks & Sundaram says that if patches are revisitable,
   *no* threshold rule of any kind is optimal. Foraging theory has spent decades searching for
   better patch-leaving rules; for that regime the search is provably futile, and the effort
   should go to approximation guarantees instead.
4. **Restless-bandit and indexability machinery for renewing patches** — nectar, regrowth,
   territory revisiting — which foraging theory currently treats ad hoc.
5. **Regret bounds.** Foraging theory has optimality results but essentially no theory of how
   costly it is to be *suboptimal*. Regret analysis is exactly that, and it is what one needs
   to interpret animals that are close to but not at the optimum.

### Operations research gains

1. **A rare closed-form index.** Equation (4): the index of an arm with an unproductive prefix
   of length τ followed by a concave reward stream is `max_t g(t)/(τ+t)`. Exactly solvable
   indices are scarce; this one is a two-line calculation.
2. **The absorption construction** (§5.4): a setup delay can be modelled as an arm prefix
   rather than a switching cost — recovering index optimality in a regime that looks like it
   should be a Banks–Sundaram failure — **iff** arms are not returned to. That is a usable
   sufficient condition for scheduling and clinical-trial problems with setup times.
3. **An average-reward index without a vanishing-discount argument** (§5.2), via
   renewal–reward. Clean where the standard route is technically awkward.
4. **A field dataset.** Foraging is very likely the largest body of empirical data anywhere on
   a real system executing something close to an index policy, complete with a documented,
   replicated, systematically signed deviation from optimality across 26 studies. OR has index
   theory and almost no natural experiments; biology has the natural experiments and did not
   know it was testing an index policy.
5. **Green (1984) and the parallel stopping literature** — an independently derived body of
   optimal-stopping results in foraging vocabulary, currently invisible to OR.

---

## 10. Status

The derivation is complete for rows 1, 2, 3 and 8 of §6. Rows 5, 6 and 7 are failures
identified at a named step, not gaps papered over. Row 4's inequality `ν(x) ≥ E[immediate
rate]` is argued from the structure of the sup over stopping times but **is not proved here in
generality**; making it a theorem with a computable bonus for a specific posterior family
(Beta–Bernoulli patches, say) is the obvious next computed note.

Two things could still falsify the novelty claim, both books that could not be obtained:
Houston & McNamara (1999) and Gittins–Glazebrook–Weber. Until one of those is read, this is
**a theorem that is correct and appears to be unwritten**, with "appears" carrying its full
weight.

See [[G28-marginal-value-gittins]] and [[what-closes-a-gap]].
