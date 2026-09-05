---
name: C48-kadmon-regrowth-test
type: computed
exit: prediction
extends-to: [ecology, conservation]
---

# Under linear nectar renewal the Whittle index goes flat, and C25's GUD prediction reverses sign

> **DERIVED, NOT TESTED — both source papers are paywalled.** Re-deriving
> [[C25-whittle-foraging]] with the renewal law Kadmon (1992) actually measured
> (`ẋ = c`, constant, capped) kills the graded prediction twice over. The Whittle index
> collapses to a step function, `W(x) = −c` on `(0,1)` and `W(1) = λ`: flat, so
> **`dGUD/dc = 0`** and the rule degenerates to "skim the fullest patch" — the policy
> [[C45-whittle-network-sim]] Table 1 measured at intake `0.0098` against MVT's `0.3154`,
> worst of four. With travel explicit the self-consistent cycle gives
> `GUD*(c) = max(a_MVT(λτ), 1 − cτ)`, so **`dGUD/dc = −τ` below the kink and 0 above —
> never positive.** C25 predicts `dGUD/dr > 0`; the linear law predicts `≤ 0`. **P-068
> cannot confirm C25 on this system whatever the data say, and P-088 is now required, not
> optional.** Access: Kadmon (1992) abstract obtained (Europe PMC) and it confirms linearity;
> Kadmon & Shmida (1992) not obtainable at all, not even an abstract.

Programme item **P-068** (Track B). Pre-registered by
`audits/blind-brief-c48-2026-09-05.md`, sha256
`4e6fe72f283fe1eb074d8f2f3e8e7f17b1b4a35ad640751360df7422b2941572`, written and hashed
before any access attempt and before `vault/_scripts/c48_kadmon.py` existed. Every number
below is reproduced by `python _scripts/c48_kadmon.py` from `vault/`.

---

## 1. Why the model had to change

C25 §1 takes passive dynamics `ẋ = r(1−x)` — saturating regrowth — and its §6 nominates the
Kadmon pair as the dataset while recording, **against interest**, that Kadmon (1992) measured
*linear* renewal. That is a model/system mismatch, not a data problem, and it has to be fixed
before any statistic is computed. So: same model, one line changed.

| | C25 | C48 (here) |
|---|---|---|
| Passive | `ẋ = r(1−x)`, reward 0 | `ẋ = c` for `x < 1`, `ẋ = 0` at `x = 1`, reward 0 |
| Active | `ẋ = −λx`, reward `λx` | identical |

The cap is load-bearing: linear renewal without one has no steady state.

## 2. The index goes flat

Whittle relaxation with subsidy `ν`. The optimal single-arm policy is still
active-above-threshold, so it chatters on the singular arc at `a`, active fraction
`u* = c/(λa + c)` holding `ẋ = 0`, with long-run gain

```
g(a) = A(B + ν)/(A + B),     A = λa,   B = c                              (1)
```

— **the same functional form as C25 (3), with `B` now constant in `a`** instead of
`B = r(1−a)`. That is the entire difference, and it is fatal:

```
∂g/∂a = λ · c(c + ν) / (λa + c)²                                          (2)
```

which never vanishes for `ν ≠ −c`. In C25 the `a`-dependence of `B` supplied the competing
term that produced an interior stationary point (`argmax_a g = 0.4765` at `λ=1, r=0.5,
ν=0.09` — verified in the script). With linear renewal that term does not exist, `g` is
strictly increasing in `a` for every `ν > −c`, and the maximiser is the boundary `a = 1`.
Hence

```
   W(x) = −c   for all x ∈ (0,1),        W(1) = λ                          (3)
```

`P(ν) = {x : W(x) ≤ ν}` is `∅` for `ν < −c`, `[0,1)` for `−c ≤ ν < λ`, `[0,1]` above:
nested, so the arm is **indexable — but the index is a step function**, flat on the interior,
carrying no state information and no `c` information. Predicted departure state `GUD = G_max`;
`dGUD/dc = 0`.

**Reading (3).** In C25 both terms of `W = λx² − r(1−x)²` are `x`-dependent because the
regrowth you forgo by occupying the patch, `r(1−x)`, depends on how empty it is. Under linear
renewal the forgone regrowth is `c` **regardless of standing crop** — flat — so the only thing
left in the index is the flat penalty. The `λx²` term of C25 is likewise an artefact of the
shadow price `V' = 1−x` that the saturating law generates; it does not survive.

**What this costs the index.** A flat index makes the Whittle destination rule identical to
`argmax_j x_j`. That is C45's `fullest` policy, and C45 Table 1 measured it at intake
`0.0098 ± 0.0000` against MVT's `0.3154 ± 0.0001` and Whittle's own `0.2735` — a factor of 32
worse than the naive alternative. **Under linear renewal the transfer does not merely lose its
prediction; it loses to random search** (C45: random `0.2161 ± 0.0024`).

## 3. With travel explicit, the sign is negative

§2 inherits C25's convention that `τ` enters only through `ν`. Put it in the flow. A forager
departing at `a`, travelling `τ`, returning to the same patch, arrives at
`x_arr = min(1, a + cτ)` — C25 §5 eq. (6)'s convention under the new law — with long-run
intake rate

```
R(a) = (x_arr − a) / ( ln(x_arr/a)/λ + τ )                                 (4)
```

Where the cap binds (`a ≥ 1 − cτ`), `∂R/∂a = 0` reduces to

```
   f(a) ≡ (1−a)/a + ln a  =  λτ                                            (5)
```

`f` decreases strictly from `+∞` to `0` on `(0,1)`, so (5) has a unique root `a_MVT(λτ)` that
is **independent of `c`**. Where the cap does not bind, the numerator of (4) is the constant
`cτ`, so `R` is maximised by pushing `a` to the regime boundary. Therefore

```
   GUD*(c) = max( a_MVT(λτ), 1 − cτ )                                      (6)
```

At `λ = 1`, `λτ = 1`: `a_MVT = 0.3178` (script check: `f = 1.000000`), kink at `cτ = 0.6822`.
Numeric `argmax_a R` over a 2×10⁵ grid reproduces (6) to four decimals in every cell.

| `cτ` | 0.05 | 0.10 | 0.20 | 0.50 | 0.682 | 1.00 | 2.00 | 5.00 |
|---|---|---|---|---|---|---|---|---|
| **`GUD*` linear (6)** | 0.950 | 0.900 | 0.800 | 0.500 | 0.318 | 0.318 | 0.318 | 0.318 |
| `GUD` saturating, C25 (`u₀=0.30`) | 0.335 | 0.362 | 0.402 | 0.477 | — | 0.545 | 0.618 | 0.712 |
| `dGUD/dc` | −τ | −τ | −τ | −τ | −τ | 0 | 0 | 0 |

**The two renewal laws disagree in sign across the entire usable window.** C25's `r·τ ∈
[0.2, 1]` design window (C45) is exactly where the disagreement is largest.

## 4. What this does to P-068 and P-088

- The C25 field prediction **does not transfer** to a linear-renewal system. A positive
  measured `dGUD/dc` in the Kadmon data would falsify *this* note; it could not confirm C25,
  because C25's own nominated dataset does not satisfy C25's own model.
- MVT with a habitat threshold `λx = R*` also gives `dGUD/dc = 0` per patch. On §2's reading,
  **Whittle and MVT are behaviourally indistinguishable here** — the pair is not merely
  under-powered, it is *empty*. This is the P-068 row's negative branch, and it fires.
- **P-088 is therefore promoted from "clean version" to "the only version".** The array must
  impose a *saturating* refill law by construction, because no natural system with linear
  renewal can discriminate the two rules. Concretely: programmed refill `ẋ = r(G_max − x)`
  with `r_fast·τ = 0.2`, `r_slow·τ = 0.02`, `G_max` and `λ` matched, expected ratio 1.06–1.27
  (C45), and — new here — a third arm with `ẋ = c` as a **negative control that must return a
  ratio ≤ 1**. That control is this note's contribution to the build.

## 5. Access status, honestly

| item | provider, fetched 2026-09-05 | result |
|---|---|---|
| Kadmon & Shmida 1992, *Evol. Ecol.* 6:142–151, `10.1007/BF02270708` | Crossref `api.crossref.org/works` | metadata verified: title, both authors, journal, volume, pages, 1992-03; `is-referenced-by-count` 62 |
| " | Unpaywall `api.unpaywall.org/v2` | `is_oa = false`, **0** OA locations |
| " | Semantic Scholar graph v1 | `openAccessPdf.status = CLOSED`; abstract **elided by publisher** (`abstract: null`) |
| " | `link.springer.com` | HTTP 303 to `idp.springer.com/authorize` — authentication wall |
| **verdict** | | **no access, not even an abstract** |
| Kadmon 1992, *Oecologia* 92:552–555, `10.1007/BF00317848` | Crossref | metadata verified; `is-referenced-by-count` 16 |
| " | Unpaywall | `is_oa = false`, 0 OA locations |
| " | Semantic Scholar | `CLOSED`, abstract elided |
| " | **Europe PMC REST**, `EXT_ID:28313227`, `resultType=core` | **abstract obtained**; `inEPMC = N`, `isOpenAccess = N` |
| **verdict** | | **abstract only; no full text, no per-flower data** |

The Europe PMC abstract settles the modelling question outright: it states that the rate of
nectar renewal is independent of the amount of nectar in the flower and that the renewal
process is strongly linear, and it reports inter-arrival-time SD/mean ratios of 0.44–0.79.
**C25 §6's against-interest note is confirmed from the source, not inferred.** No renewal-rate
value in physical units (µl · flower⁻¹ · h⁻¹) appears in the abstract, so §3's table cannot be
instantiated at Kadmon's measured `c`.

Sci-Hub was not used. Of the 12 papers Semantic Scholar lists as citing the *Oecologia* paper,
four are open access and none reproduces Kadmon's renewal-rate figures; the closest
theoretical citer, Ohashi & Thomson (2005) *Behav. Ecol.* 16:592–605, `10.1093/beheco/ari031`
(Crossref-verified), is itself closed (Unpaywall `is_oa = false`) and is a model, not data.

**A correction to this item's own reading list.** The DOI carried into P-068 for Dreisig
(1995) "Ideal free distributions of nectar foraging bumblebees", `10.2307/3545806`, resolves
in Crossref to **McGeoch & Chown (1997), "Evidence of Competition in a Herbivorous,
Gall-Inhabiting Moth (Lepidoptera) Community", *Oikos* 78:107** — a different paper. The
correct DOI is **`10.2307/3546218`**, Dreisig, *Oikos* 72:161, 1995-03 (Crossref, fetched
2026-09-05). Logged.

## 6. The table a human with library access fills in an hour

One row per bee departure from a flower. Both papers open on a desk; the join key is the
flower.

| col | field | units | source paper | why the model needs it |
|---|---|---|---|---|
| 1 | `flower_id` | — | both | the join key; without it the pair cannot be merged and §7 is unanswerable |
| 2 | `plant_id` | — | K&S 1992 | clustering unit for the Spearman CI |
| 3 | `t_arrive` | s since dawn | K&S 1992 | fixes the depletion window |
| 4 | `t_depart` | s | K&S 1992 | `t_res = t_depart − t_arrive` |
| 5 | `V_at_arrival` | µl | K&S 1992 | with col 6 and col 4 gives `λ` |
| 6 | `V_at_departure` | µl | K&S 1992 | **the GUD. The dependent variable.** |
| 7 | `Δt_since_last_visit` | s | Kadmon 1992 (inter-arrival dist.) | the `c`-proxy stratifier |
| 8 | `c_flower` | µl·h⁻¹ | Kadmon 1992 | the independent variable, per flower |
| 9 | `G_max_flower` | µl | Kadmon 1992 | the cap; (6) is stated in units of it |
| 10 | `τ_next` | s | K&S 1992 | sets `λτ`, hence `a_MVT` via (5) |

Fill it, then run: Spearman `ρ_s` of col 6 on col 8 (primary) and of col 4 on col 8
(secondary), clustered on col 2. The brief's gate applies unchanged: `ρ_s > 0` at `p < 0.05`
falsifies this note; `ρ_s < 0` confirms §3; a CI containing 0 but excluding `+0.3` is
consistent with §2 and still refutes C25's direction. **`n ≥ 30` flowers with cols 6 and 8
both present is the minimum; below that, report the null and stop.** If cols 8 and 6 cannot be
joined per flower — the most likely outcome, since the two papers report different flower
samples — the honest answer is "the pair was never a dataset", and §4 stands as the result.

## 7. Other published nectar-renewal-with-departure datasets, ranked by fit

Ranked by whether departure standing crop and renewal rate are measured on the same flowers.
DOIs Crossref-verified 2026-09-05; OA status from Unpaywall, same date.

1. **None found that satisfies the design.** This is a finding, not a search failure: the
   requirement that `c` be measured per flower *and* departure crop recorded per visit is
   met nowhere in the open literature reachable here.
2. Taneyhill (2010), *Psyche* 2010:872736, `10.1155/2010/872736` — **open access**
   (Unpaywall; Hindawi PDF, which returned HTTP 403 to this agent's fetcher, so it is open
   but unread here). A review of bumble-bee patch-departure rules: the right place to look
   for a secondary dataset, and the single highest-value next fetch.
3. Dreisig (2012), *Arthropod-Plant Interactions* 6:315–325, `10.1007/s11829-011-9169-9`,
   "How long to stay on a plant: the response of bumblebees to encountered nectar levels" —
   departure vs *encountered nectar* on real plants; renewal rate not manipulated. Closest
   natural-system fit after Kadmon. Closed.
4. Dreisig (1995), *Oikos* 72:161, `10.2307/3546218` — standing crop and forager
   distribution; departure rule inferred, not measured. Closed.
5. Ohashi & Thomson (2005), `10.1093/beheco/ari031`; Possingham (1989), *Am. Nat.* 133:42–60,
   `10.1086/284900` — **models, not measured foragers** (C25 §6 already rules both out; they
   are listed so the exclusion is not re-litigated).
6. The gap this leaves is exactly P-088's warrant.

## 8. Honesty

**What was derived.** Everything in §2 and §3, from the same relaxation C25 uses, with one
line of the model changed. The singular-arc form (1) is C25's own eq. (3) with `B` held
constant; that substitution is the whole argument and it is checkable in two lines.

**What was tested.** Nothing empirical. Three *analytical* claims were verified numerically
against brute-force optimisation in `_scripts/c48_kadmon.py`: no interior optimum of (1) for
eight subsidies spanning `ν = −1 … 5` (zero sign changes in `∂g/∂a` in every case); `a_MVT =
0.3178` as the root of (5) to `10⁻⁶`; and (6) reproduced to four decimals by grid `argmax` of
(4) in all eight `cτ` cells. These confirm the algebra, not the biology.

**Access.** §5. Kadmon & Shmida (1992) is wholly unobtainable through open routes; Kadmon
(1992) yielded an abstract only. So P-068's stated test **was not run**, and this note does
not claim it was.

**The three real weaknesses.**
1. §2 assumes the optimal single-arm policy is active-above-threshold. That is argued from
   monotonicity of the active branch, not proved; a non-threshold optimum would break (3). It
   is the same assumption C25 §2 makes, so the two notes fail together if it fails.
2. §3's cycle is single-patch round-robin, C25 §5's convention. A network run — the C45
   treatment — is not done here and could move the kink. It should not move the *sign*,
   because (5) is `c`-free, but that is an argument, not a simulation.
3. Kadmon's linearity is reported for renewal *between successive forager arrivals*, i.e.
   over the observed inter-arrival window, with SD/mean 0.44–0.79. Linearity over that window
   does not exclude saturation at longer intervals or near a cap that bees rarely let the
   flower reach. **If bees keep flowers far from `G_max`, "linear" and "saturating" are the
   same law observed on its linear part**, and the whole of §2's degeneracy would be an
   artefact of extrapolating a locally-linear fit to the cap. This is the first line of attack
   on this note, and it is testable from the *Oecologia* full text alone: does the reported
   renewal rate hold at standing crops approaching the maximum observed?

**What would change the standing.** Obtaining either full text, or Taneyhill (2010). The
cheapest decisive move is item 3 above — one figure in one paywalled paper.

Rests on [[C25-whittle-foraging]], [[C45-whittle-network-sim]], [[C5-charnov-gittins]];
answers part of [[Q5-restless-patches]].
