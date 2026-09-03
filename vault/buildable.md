---
name: buildable
type: method
---

# Buildable

> The register the vault was missing. Gaps, questions and derivations all live here — **nothing
> tracked what could actually be done.** Sorted by what it costs to find out.

A row earns its place by naming a **measurement nobody has published**, not a demo. Every one
below traces to a gap that survived a full-text read, so the absence is checked rather than
assumed.

---

## Reachable at home

### 1. Cycle a latch to failure · ~$300, a 3D printer and a phone

**Nobody has ever run a latch to failure.** From [[G12-latch-fatigue]], which held at
`full-text-read` in the strongest possible form: the field's own 2023 review says the
distinctions among single-use, re-useable and re-settable mechanisms "are considered elsewhere",
and the most latch-specific paper in the literature measures **one** cycle, on **dried**
specimens.

Meanwhile engineering treats latch cycle life as routine — there is a patent titled *Method to
detect end-of-life in latches*. So the method exists and has never been pointed at biology's
version. See [[LaMSA-latch]].

| | |
|---|---|
| **Build** | Printed latch geometry after the click-beetle hinge, a spring of known stiffness, a cam to load and release |
| **Measure** | Peak release velocity against cycle number, to failure or 10⁵ cycles |
| **Camera** | A modern phone at 240 fps is enough if the throw is scaled up; the point is the *trend*, not the absolute |
| **The number** | Cycles to a 10% loss of release velocity. **This number does not exist for any latch, biological or printed** |
| **Kills it if** | Velocity is flat to 10⁵ and the rig fails elsewhere first — then the latch is not the limiting element, which is also worth knowing |

**Why it is the best first build:** the variable is one-dimensional, the failure is visible, and
the null result is publishable either way.

### 2. Sweep the dose on a self-strengthening material · ~$100

From [[G23-hormesis-formalism]]. Engineering *knows* the response turns over — shot peening
calls the far side "over-peening". **What nobody has done is sweep the dose and plot the curve.**
The mechanochemistry paper that started this reports a **single operating point.**

| | |
|---|---|
| **Measure** | A stress-responsive material's property against stimulus amplitude, 8–10 points spanning weak to destructive |
| **The number** | Amplitude ceiling and window width — the two constants toxicology has had for decades and materials science has never written down |
| **Kills it if** | The response is monotonic up to fracture. Then engineering's biphasic case is peening-specific, not general |

### 3. Salt hydrate cycling · ~$100 of kitchen equipment

From [[G3-cycle-life]]. Thermochemical storage publishes *"stable for at least ten cycles"*
while flow batteries quote fade below **0.001% per cycle**. The field's own review calls the
variable under-served.

Dehydrate, weigh, rehydrate, weigh, log temperature rise, 50+ cycles. **Report fade per cycle
and per day separately** — that separation is the actual contribution.

---

## Needs a lab, but the data may already exist

### 4. Re-analyse the columella ablation series

From [[C4-inclination-sensing-limit]]. Pooling predicts minimum detectable tilt scaling as
`M^(−1/2)`; plain linear summation predicts `M^(−1)`. **The existing 1998 data cannot tell them
apart**, because stimulation was at 90° only.

The discriminating run: ablate to `M = {48, 32, 24, 16}`, stimulate at 5/10/20/40/90°, regress
curvature rate on sin θ. **Pooling predicts a ratio of 1.73; linear summation predicts 3.00.**
About 500 roots. A plant lab with a laser could do it in a season.

### 5. Gate healing with temperature, and measure `Ha`

From [[C6-damage-healing-ratio]]. The reason nobody has formed the damage/healing ratio is
**experimental, not conceptual**: you cannot switch healing off while loading, so only the mixed
result is observable.

**Vitrimers can be switched off.** Bond exchange is gated at the topology-freezing temperature.
Load below it to get the damage rate alone, then above it for the healing rate. That yields the
first measured `Ha` for an engineered material, and fills a row the table currently leaves empty.

---

## Fit a curve to data already published

### 6. Discriminate the three healing laws

From [[Q4-healing-needs-a-new-law]]. Continuum damage-healing mechanics has no interior steady
state — nothing un-heals. The three candidate repairs predict **different shapes** for healing
efficiency against cycle number: saturating, linear-decaying, exponentially-decaying.

Cycled self-healing polymer data reporting exactly that curve is already published. **This is a
curve fit, not an experiment.** Cheapest real test on the list.

---

## What is not here, and why

No row for [[G1-gradient-coupling]] yet — the surviving momentum branch has no metric to build
toward until `C8-momentum-harvesting-metric` lands. That is the founding question and the
gating item.

Nothing from [[G9-discrepancy-base-rate]]. It is meta-research and cannot be built.
