---
name: C10-healing-curve-fit
type: computed
---

# The cycled-healing curve fit: it is a decaying envelope, not a rate balance

> **Across every multi-cycle dataset extracted, healing efficiency `η(N)` is a monotone
> decaying envelope — Q4's candidate 2 (a genuine rate balance approaching a nonzero steady
> state) is supported by NONE of them.** The envelope decays two ways, and which one is
> material-dependent: toward a *positive floor* (candidate 1, healing-agent depletion — the
> [[kirkwood-disposable-soma]] frame) or toward *zero* (candidate 3, finite healing quality —
> no steady state at all). Within a single intrinsic-vitrimer paper the two coexist, selected
> by crosslink chemistry. Extrinsic microcapsule healers are the extreme of candidate 1:
> one-shot, because the reservoir is finite.
> **Consequence for [[C6-damage-healing-ratio]]:** the clean steady state `A = Ha/(1+Ha)` is
> *not reached across cycles*. `k_r` is not constant in `N` — it decays — so `Ha` is a
> first-window quantity, `Ha(N)`, and needs a cycle-depletion parameter. The group is valid
> as written only within one healing cycle, never across the cycled envelope.

Answers the curve-fit posed in [[Q4-healing-needs-a-new-law]]. Feeds back onto
[[C6-damage-healing-ratio]]. Vindicates [[kirkwood-disposable-soma]] as the correct frame for
the floor-decaying class.

---

## 1. The three shapes being discriminated

From [[Q4-healing-needs-a-new-law]], the three physically distinct un-healing mechanisms
predict three different `η(N)` shapes:

| Candidate | Mechanism | Shape | Steady state? |
|---|---|---|---|
| **1 · depletion** | finite repair budget consumed | saturating decay to a **positive floor** `η_∞ > 0` | yes, a floor (Kirkwood) |
| **2 · re-damage of healed material** | healed bonds fail preferentially → rate balance | approach a **nonzero** `η*` from either side | genuine steady state |
| **3 · finite healing quality** | each cycle recovers less | decaying envelope **toward 0** | none |

Discriminators used, honest about a 3-point limitation:
- **Constant decrement** `η_N − η_{N+1}` → linear (a special sub-case).
- **Constant ratio** `η_{N+1}/η_N = r` → exponential envelope `η_0 r^N` → **candidate 3** (heads to 0).
- **Decelerating decrements toward a plateau** → saturating `η_∞ + (η_0−η_∞)e^{−N/τ}` with
  `η_∞ > 0` → **candidate 1**.
- **Approach from below, or overshoot/oscillation** → **candidate 2**. *Not seen in any dataset.*

For a 3-decrement series the decrement ratio `g = (η_2−η_3)/(η_1−η_2)` and the implied floor
`η_∞ = η_1 − (η_1−η_2)²/[(η_1−η_2)−(η_2−η_3)]` are computed below. **Caveat stated up front:**
with three points the floor is *exactly determined* (zero degrees of freedom), so it is fragile.
The robust discriminator is `g`: `g ≈ 0.75` steady → exponential/envelope; `g` small →
sharp-drop-then-floor.

---

## 2. The extracted data

### Dataset A — intrinsic dynamic-covalent vitrimer (imine + disulfide), VERIFIED

Bio-based epoxy vitrimer, Table 3, tensile-strength recovery `η_σ`, healed by hot-pressing
120 °C / 1 MPa / 2 h per cycle. Same specimen re-cut and re-healed three times.
Source: [PMC11510012 fullTextXML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11510012/fullTextXML) — **VERIFIED, fetched this session, Table 3 quoted verbatim.**

| Sample (imine/disulfide) | η(1) % | η(2) % | η(3) % | Marker |
|---|---|---|---|---|
| BEV-VD (imine only) | 74.7 ± 8.9 | 39.4 ± 4.1 | 32.8 ± 1.3 | VERIFIED |
| BEV-VC/VD-1/3 | 77.8 ± 5.0 | 61.2 ± 7.5 | 48.4 ± 3.1 | VERIFIED |
| BEV-VC/VD-1/1 | 76.8 ± 3.9 | 46.3 ± 3.3 | 33.6 ± 4.5 | VERIFIED |
| BEV-VH/VD-1/3 | 75.5 ± 6.7 | 56.0 ± 4.8 | 41.4 ± 2.7 | VERIFIED |
| BEV-VH/VD-1/1 | 76.3 ± 6.7 | 46.3 ± 4.8 | 31.6 ± 1.5 | VERIFIED |

Paper's own words: *"The healing efficiencies, based on tensile strength after the first
healing treatment, were 75–78%, which gradually decreased as the healing cycle was repeated."*

### Dataset B — extrinsic microcapsule healers (class contrast), VERIFIED qualitative + one series

Review, [PMC11477567 fullTextXML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11477567/fullTextXML) — **VERIFIED, fetched this session.**

- Depletion stated explicitly: *"microcapsules have some limitations, particularly with regard
  to the amount of repairing agent they contain"*; *"the number of capsules is finite"*; after
  a second crack *"the failures must follow a path that ensures that the crack meets the
  unbroken microcapsules."* This is candidate 1 in prose: a **finite reservoir**.
- One per-cycle series relayed by the review (Zhang et al.): **η(1) ≈ 65 %, then reduced by
  20–30 % after the 2nd and 3rd repairs.** Marked **VERIFIED-VIA-REVIEW** (secondary; the
  primary was not fetched — treat the exact figure as indicative, the direction as solid).
- Intrinsic contrast: intrinsic healers give *"repeatability of self-repair"*; thermoplastic
  (refillable) healers *"theoretically ... unlimited cycles."*

### Dataset C — intrinsic H-bond poly(urethane-urea) + TiO₂, APPROXIMATE-FROM-FIGURE

[PMC6680434 fullTextXML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6680434/fullTextXML) — **VERIFIED that it is 3-cycle and decreasing; numbers only in Fig. 6, not extractable from text.** Paper's words: *"The healing efficiency decreased with the number of
cuts."* No numeric `η(N)` is quoted here because none is in the text — **not fabricated**,
marked ABSENT-FROM-TEXT. Direction: monotone decrease, consistent with Datasets A/B.

### Dataset D — the counter-example that is NOT candidate 2

Shape-memory-alloy-reinforced vitrimer with a PCL-diol external healing layer reports
`η` **increasing** from 41.1 % (2nd fracture) to 58.6 % (5th) — source ScienceDirect
S1359835X22003529, **paywalled, NOT fetched; only the two endpoint numbers are secondary and
marked UNVERIFIED.** This looks superficially like "approach from below" (candidate 2) but the
authors attribute it to *compaction of the PCL adhesive layer and growing interfacial
entanglement* — a mechanically-improving contact, not a bond rate balance. Logged as a caution:
a rising envelope here is an extrinsic-adhesive artifact, not evidence for candidate 2. Not fit.

---

## 3. The three fits, with arithmetic

Cycle index `k = 1, 2, 3`. Two contrasting Dataset-A formulations are fit in full; the decrement
diagnostics are then tabulated for all five.

### 3a. BEV-VC/VD-1/3 → **exponential envelope (candidate 3)**

Data: (1, 77.8), (2, 61.2), (3, 48.4).

**Envelope `η = C·r^k`** (linearise, `y = ln η`):
`ln η = 4.354, 4.114, 3.879`. Successive differences: **−0.240, −0.235** — near-identical, so
the log is linear in `k`. Least squares: slope `= −0.2375` ⇒ `r = e^−0.2375 = 0.789`; intercept
`ln C = 4.5915` ⇒ `C = 98.6`. Predictions: `k=1: 77.8, k=2: 61.4, k=3: 48.4`.
Residuals ≈ **(0.0, −0.2, 0.0)**, SSR ≈ **0.05**.

**Linear `η = A − Bk`:** `mean k = 2, mean η = 62.47`; `S_xy = −29.4, S_xx = 2` ⇒ `B = 14.7`,
`A = 91.87`. Predictions: `77.17, 62.47, 47.77`. Residuals **(+0.63, −1.27, +0.63)**, SSR ≈ **2.41**.

**Saturating floor:** `d1 = 16.6, d2 = 12.8, g = 0.771`; `η_∞ = 77.8 − 16.6²/(16.6−12.8) =
77.8 − 72.5 = 5.3 %`. Floor ≈ 5 %, i.e. **indistinguishable from zero**.

→ Exponential envelope wins outright (SSR 0.05 vs 2.41); constant ratio `r ≈ 0.79`; implied
floor ~0. **Candidate 3 — no steady state.**

### 3b. BEV-VD → **saturating to a positive floor (candidate 1)**

Data: (1, 74.7), (2, 39.4), (3, 32.8).

**Envelope `η = C·r^k`:** `ln η = 4.313, 3.674, 3.490`; differences **−0.639, −0.184** — far
from constant (strongly curved). LSQ slope `−0.4115`, intercept `4.649` ⇒ predictions
`69.3, 45.9, 30.4`; residuals **(+5.4, −6.5, +2.4)**, SSR ≈ **77**. Poor.

**Linear:** `B = 20.95, A = 90.87` ⇒ `69.92, 48.97, 28.02`; residuals **(+4.78, −9.57, +4.78)**,
SSR ≈ **137**. Worse.

**Saturating floor:** `d1 = 35.3, d2 = 6.6, g = 0.187`; `η_∞ = 74.7 − 35.3²/(35.3−6.6) =
74.7 − 43.4 = 31.3 %`. A sharp first-cycle drop, then a **plateau at ≈ 31 %**.

→ Neither 2-parameter monotone-to-zero model fits; the data is a sharp drop onto a positive
floor. **Candidate 1 — depletion to a reservoir-limited floor.**

### 3c. Decrement diagnostics, all five formulations

| Sample | d1 | d2 | ratio `g` | implied floor `η_∞` | verdict |
|---|---|---|---|---|---|
| BEV-VD | 35.3 | 6.6 | 0.19 | **31.3 %** | candidate **1** (floor) |
| BEV-VC/VD-1/1 | 30.5 | 12.7 | 0.42 | **24.5 %** | candidate **1** (floor) |
| BEV-VH/VD-1/1 | 30.0 | 14.7 | 0.49 | **17.5 %** | candidate **1** (floor) |
| BEV-VH/VD-1/3 | 19.5 | 14.6 | 0.75 | ≈ −2 % (→0) | candidate **3** (envelope) |
| BEV-VC/VD-1/3 | 16.6 | 12.8 | 0.77 | ≈ 5 % (→0) | candidate **3** (envelope) |

The split is chemically ordered: the two **1/3** formulations (lower crosslink density, more
free dynamic bonds) give constant-ratio envelopes decaying to ~0; the neat-imine and **1/1**
formulations give a fast drop onto a 17–31 % floor. **Candidate 2 (approach to a nonzero
steady state from below, or any overshoot) appears in none of the five.**

---

## 4. Per-material decision

| System | Class | Shape that wins | Un-healing mechanism |
|---|---|---|---|
| Dataset A, 1/3 formulations | intrinsic vitrimer | exponential envelope → 0 | **3 · finite healing quality** |
| Dataset A, 1/1 + neat-VD | intrinsic vitrimer | saturating → floor 17–31 % | **1 · depletion** |
| Dataset B, microcapsule | extrinsic reservoir | sharp decay, finite reservoir (one-/few-shot) | **1 · depletion (extreme)** |
| Dataset C, H-bond PU-urea | intrinsic | monotone decrease (figure only) | 1 or 3, not resolved |
| Dataset D, PCL-vitrimer | extrinsic adhesive | rising envelope (artifact) | not candidate 2 — contact compaction |

**The finding the brief anticipated: the correct un-healing term is material-class-dependent —
and, more finely, *chemistry*-dependent within one class.** Extrinsic microcapsule healers are
unambiguously candidate 1 (a finite, non-refillable reservoir; the Kirkwood disposable-soma
budget made literal). Intrinsic dynamic-covalent healers split by crosslink density between a
depletion floor (candidate 1) and a to-zero envelope (candidate 3). **No dataset supports
candidate 2** — the one shape that would give `Ha` a genuine steady state.

---

## 5. Feedback to [[C6-damage-healing-ratio]]

C6 offered `Ha = k_r/k_d` with steady state `A = Ha/(1+Ha)`, valid under conditions C1–C4,
one of which (C4) is that `k_r` is a constant, not a function of loading history. The cycled
data speaks directly to that:

1. **`k_r` is not constant across cycles — it decays.** Every dataset shows `η` falling with
   `N`. Since `η` is the observable proxy for recovered capacity, healing effectiveness — and
   therefore the effective `k_r` — is a **decreasing function of cycle number**. C6's condition
   C4 (constant rate) fails not only within a loading history but *across the cycled envelope*.
   `Ha` is therefore `Ha(N)`, declining, exactly as [[Q4-healing-needs-a-new-law]] predicted:
   *"`Ha` is only valid over a window."* **Confirmed, quantitatively.**

2. **Candidate 2 loses, so C6's steady state is NOT reached across cycles.** C6 §6 states the
   clean case: if a rate balance holds, `A = Ha/(1+Ha)` is genuinely reached and the group is
   valid as written. The multi-cycle data does **not** show a rate balance — no approach to a
   nonzero `η*` from either side, in any of the seven series examined. So the "genuinely reached
   steady state" branch of C6 is **not the regime cycled materials are in.** Within a *single*
   healing cycle C6's two-state balance may still hold (that is a different, faster observable);
   the group describes the first cycle, not the envelope.

3. **Which failure branch depends on class, and Kirkwood is vindicated for one of them.**
   - Floor-decaying (candidate 1: microcapsules; crosslink-rich vitrimers): `Ha` is valid over
     a **window** before the reservoir runs down, and C6 needs an explicit **depletion
     parameter** — a budget `B(N)` multiplying `k_r`, `k_r,eff(N) = k_r·B(N)/B(0)`. This is
     precisely [[kirkwood-disposable-soma]]: a finite repair budget. C6 §4.3 and the brief both
     flag this theory as *unread by self-healing materials*; the microcapsule review (Dataset B)
     confirms the field describes the finite reservoir in its own words but **never cites the
     disposable-soma formalism.** The unread-theorem status holds.
   - Envelope-to-zero (candidate 3: dynamic-bond-rich vitrimers): there is **no steady state at
     all**, and `Ha` describes only the first cycle. This is the same defect C6 §4.2 found
     analytically — CDHM's `h → 1` ratchet — reappearing empirically as `η → 0`: the model with
     no un-healing term and the material with a to-zero envelope are two faces of *no stationary
     balance*.

4. **Net edit to C6:** the two empty rows in C6's table (self-healing polymer / vitrimer) cannot
   be filled with a single `Ha` — they need a **cycle label** and a **depletion parameter**.
   `Ha` as a scalar is a first-cycle quantity. The honest object for cycled healing is
   `Ha(N) = A(N)/(1−A(N))` read off the decaying envelope, plus the class tag {depletion-floor |
   finite-quality-to-zero}. C6's group survives *within a cycle*; across cycles it is replaced
   by the envelope, and Kirkwood is the right frame for the floor class.

---

## 6. Standing and weakest links

- **Dataset A is the load-bearing result** — five formulations, VERIFIED verbatim from Table 3
  via a fetched URL, three cycles each, all three fits done with visible arithmetic. The
  candidate-2 rejection rests on it and on Dataset B.
- **Three-point fragility, stated plainly:** with `k = 1,2,3` the floor `η_∞` is exactly
  determined and the saturating (3-param) model can always match three points. The robust
  discriminator is the decrement ratio `g`, not `η_∞`. The clean-exponential verdicts (`g ≈ 0.77`,
  SSR ≈ 0.05) are strong; the floor verdicts (`g` small) are directional. A 5–10 cycle series
  would settle floor-vs-zero decisively; none was found open-access with tabulated numbers.
- **Extrinsic per-cycle numbers are the gap.** The microcapsule depletion mechanism is VERIFIED
  in prose and one secondary series; a primary extrinsic `η(N)` table (e.g. the Toohey
  microvascular data) could not be fetched — the Beckman PDF certificate had expired and the
  Nature source is paywalled. Marked as the next fetch, not fabricated.
- **Candidate 2 is unsupported, not disproven.** No cycled dataset showed a rate balance; that is
  the finding. If a re-damage-dominated system (healed bonds failing preferentially with a
  refilling matrix) were found to plateau at a nonzero `η*` from below without an adhesive-
  compaction confound, candidate 2 would reopen. Dataset D is not it.
