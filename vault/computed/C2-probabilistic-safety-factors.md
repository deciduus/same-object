---
name: C2-probabilistic-safety-factors
type: computed
---

# Probabilistic safety factors for biological structures

> **For bone, failure probability is set by the variability of the tissue, not the variability of locomotion.**

[[stress-strength-interference]] applied to biological cases. Biology has only a
deterministic ratio; the formalism yields a probability of failure — which is precisely the
objection raised against symmorphosis since 1987.

## The robust result

**Operating point.** The contrast below is evaluated at **`SF = μ_R/μ_S = 3`**, **`V_R = 0.20`**
(strength CV), **`V_S ∈ [0.05, 0.30]`** (load CV), **normal–normal** stress–strength
interference with `μ_S = 1`, `μ_R = 3`. This point was previously implicit — it is the
`SF × V_R = 0.6` mentioned below — and stating it is necessary because the contrast does not
survive moving it (see "The sensitivity is to the operating point" and §S).

At that point: holding `SF = 3`, moving strength CV from 0.10 to 0.30 swings P_f across
**8.7 orders of magnitude** (2.42e-11 → 1.33e-2 at `V_S = 0.05`; 7.9 orders at `V_S = 0.11`).
Moving load CV from 0.05 to 0.30 **at `V_R = 0.20`** moves it **0.51 of an order**
(4.47e-4 → 1.43e-3). Measured locomotor load CV is only 0.05-0.11, small against SF x V_R of
about 0.6.

Holds in both distributional models at every safety factor from 1.4 to 4.1. **And it points
at the term Alexander's mixed-chain argument de-emphasises** — he reasoned that links with
more variable *loading* should carry higher safety factors.

## The sensitivity is to the operating point, not to biology

**At `V_R = 0.10` the load-CV sensitivity is ~5 orders, not half an order.** Same `SF = 3`,
same normal–normal model, only the strength CV moved:

```
V_R = 0.20 :  V_S 0.05 → 0.30  gives  4.47e-04 → 1.43e-03   =  0.51 orders
V_R = 0.10 :  V_S 0.05 → 0.30  gives  2.42e-11 → 1.21e-06   =  4.70 orders
V_R = 0.30 :  V_S 0.05 → 0.30  gives  1.33e-02 → 1.75e-02   =  0.12 orders
```

The reason is elementary and worth writing down, because it is the whole content of the
"robust result": with `μ_S = 1`, `μ_R = SF`,

```
β  =  (μ_R − μ_S) / √(σ_R² + σ_S²)  =  (SF − 1) / √( (SF·V_R)² + V_S² )
```

so the load term `V_S` enters only through `V_S²` **added to `(SF·V_R)²`**. At `SF = 3`,
`V_R = 0.20` that is `0.36`, against `V_S²  ≤ 0.09` — the load variance is at most a quarter of
the strength variance and barely moves `β`. At `V_R = 0.10` it is `0.09`, so `V_S = 0.30`
*doubles* the total variance and `β` falls from 6.58 to 4.71, which in the far tail is five
orders. **The asymmetry is not a fact about locomotion; it is `(SF·V_R)² ≫ V_S²` at one chosen
point.** The honest statement is the partial derivative at a named point, and the named point
must be given.

**Restated for quoting:** *at `SF = 3` and `V_R = 0.20`, `∂log₁₀P_f/∂V_S` over `[0.05, 0.30]`
is about 2 per unit CV (0.51 orders across the range), against about 44 per unit CV for `V_R`
over `[0.10, 0.30]` (8.7 orders). Both figures are conditional on `V_R = 0.20`; at
`V_R = 0.10` the load-CV figure rises to ~19 per unit CV (4.7 orders).*

## §S. The interference arithmetic, in full

**Model: normal–normal**, `R ~ N(SF, (SF·V_R)²)`, `S ~ N(1, V_S²)`, independent, so
`R − S` is normal and `P_f = P(R < S) = Φ(−β)` exactly. A **lognormal–lognormal** cross-check
(matched means and CVs, `P_f = Φ(−(λ_R−λ_S)/√(ζ_R²+ζ_S²))`) is given below; it is *not*
interchangeable — see "What is not quotable".

```python
from math import erfc, sqrt, log, log10
def Phi(z): return 0.5*erfc(-z/sqrt(2))

def pf_normal(SF, VR, VS):                  # mu_S = 1, mu_R = SF
    sR, sS = VR*SF, VS
    return Phi(-(SF-1)/sqrt(sR*sR + sS*sS))

def pf_lognormal(SF, VR, VS):
    zR = sqrt(log(1+VR**2)); zS = sqrt(log(1+VS**2))
    lR = log(SF) - 0.5*zR*zR; lS = -0.5*zS*zS
    return Phi(-(lR-lS)/sqrt(zR*zR + zS*zS))

VS = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30]
for VR in (0.10, 0.20, 0.30):
    row = [pf_normal(3, VR, v) for v in VS]
    print(VR, ["%.2e" % p for p in row], "span %.2f orders" % log10(row[-1]/row[0]))
```

**Normal–normal, `SF = 3`** (rows = `V_R`, columns = `V_S`):

| `V_R` \ `V_S` | 0.05 | 0.10 | 0.15 | 0.20 | 0.25 | 0.30 | **span** |
|---|---|---|---|---|---|---|---|
| **0.10** | 2.42e-11 | 1.27e-10 | 1.24e-09 | 1.45e-08 | 1.52e-07 | 1.21e-06 | **4.70 orders** |
| **0.20** | 4.47e-04 | 5.05e-04 | 6.11e-04 | 7.83e-04 | 1.05e-03 | 1.43e-03 | **0.51 orders** |
| **0.30** | 1.33e-02 | 1.36e-02 | 1.42e-02 | 1.50e-02 | 1.61e-02 | 1.75e-02 | **0.12 orders** |

Down a column (`V_R` 0.10 → 0.30) at `V_S = 0.05`: **8.74 orders**; at `V_S = 0.11`
(top of the measured locomotor band): **7.85 orders**.

**Lognormal–lognormal, same `SF = 3`, same grid:**

| `V_R` \ `V_S` | 0.05 | 0.10 | 0.15 | 0.20 | 0.25 | 0.30 | **span** |
|---|---|---|---|---|---|---|---|
| **0.10** | 4.91e-23 | 3.41e-15 | 3.72e-10 | 2.58e-07 | 1.16e-05 | 1.23e-04 | **18.40 orders** |
| **0.20** | 6.15e-08 | 5.08e-07 | 5.49e-06 | 4.38e-05 | 2.23e-04 | 7.66e-04 | **4.09 orders** |
| **0.30** | 1.93e-04 | 3.13e-04 | 5.99e-04 | 1.20e-03 | 2.30e-03 | 4.07e-03 | **1.32 orders** |

**The lognormal model does not reproduce the "half an order" claim anywhere.** At `V_R = 0.20`
it gives 4.1 orders. So the load-CV insensitivity is a property of the *normal* model at
`V_R = 0.20`, not of stress–strength interference. The strength-CV dominance survives both
models; the *size* of the contrast does not.

## What is not quotable

The specific numbers. The model choice decides the answer: at `SF = 3`, `V_R = 0.20`,
`V_S = 0.11` normal gives P_f 5.2e-4, lognormal 8.2e-7 — three orders apart, straddling the
EN 1990 structural target from opposite sides. No obtainable biological dataset can test the tail.

The comparison to engineering targets is **formally invalid** and flagged rather than deleted:
biological P_f here is *per load cycle*, EN 1990 is per fifty years, and an animal takes
1e6-1e7 steps a year.

## The remodeling objection is the deliverable

Stress-strength interference assumes strength is **fixed at manufacture**. In bone it is a
*function of realised load history*, with negative feedback — the individual in the weak tail
while being loaded hard is exactly the one that remodels, so **the interference region is
actively depleted.** Every P_f is an upper bound.

**This inverts the trade.** Engineering's assumption is the **zero-gain limit of a control
loop biology runs with positive gain.** A formalism for load-adaptive strength would be a
contribution *from* biology *to* reliability engineering.

---

## Corrections 2026-09-05

**A24 — the "nine orders vs half an order" contrast now carries its operating point, and a
sensitivity-to-that-choice line.**

| | old | new |
|---|---|---|
| Operating point | unstated (implicit `SF × V_R ≈ 0.6`) | **stated: `SF = 3`, `V_R = 0.20`, `V_S ∈ [0.05, 0.30]`, normal–normal, `μ_S = 1`, `μ_R = 3`** |
| Strength-CV swing | "nine orders of magnitude" | **8.74 orders** at `V_S = 0.05` (2.42e-11 → 1.33e-2); 7.85 orders at `V_S = 0.11` |
| Load-CV swing | "half an order" — no point given | **0.51 orders at `V_R = 0.20`** (4.47e-4 → 1.43e-3) |
| Sensitivity to that choice | absent | **at `V_R = 0.10` the same load-CV sweep gives 4.70 orders** (2.42e-11 → 1.21e-6), not half an order |
| Model dependence of the contrast | absent | **lognormal gives 4.09 orders for the load-CV sweep at `V_R = 0.20`** — the half-order figure is normal-model-specific |
| Illustrative pair 5.2e-4 / 8.2e-7 | point not stated | evaluated at **`SF = 3`, `V_R = 0.20`, `V_S = 0.11`** — reproduces both to 2 s.f. |

**Inputs behind every changed number:** `μ_S = 1`, `μ_R = SF = 3`, `σ_R = SF·V_R`,
`σ_S = V_S`, `β = (μ_R−μ_S)/√(σ_R²+σ_S²)`, `P_f = Φ(−β)`; lognormal by the matched-moment
transform in §S. Arithmetic run in the §S Python block, 2026-09-05; both tables are its output
verbatim. No external source was needed or fetched for this correction — it is a
recomputation, not a datum.

**What did not change.** The qualitative claim — *strength variability dominates load
variability for bone at biological safety factors* — survives both models and the whole grid,
and the remodelling objection (every P_f is an upper bound) is untouched.
