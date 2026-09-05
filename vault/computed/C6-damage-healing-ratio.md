---
name: C6-damage-healing-ratio
type: computed
---

# The healing Damköhler number, Ha = k_r/k_d

> **The group is well-defined, it reduces to availability under four stated conditions, and
> three systems can be put on it with verified numbers. But it is information-*lossy*, not
> information-adding — and the reason nobody wrote it is a missing experimental control, not
> a missing idea.**

Writes down the object named missing in [[G5-repair-number]], and populates it. Rests on
[[availability-formula]]; extends [[C1-availability-living-tissue]] onto engineering systems.

> **UPDATE 2026-09-03 — the curve fit is in, and it narrows Ha's regime.**
> [[C10-healing-curve-fit]] fit seven cycled datasets. **The rate-balance case (a steady state
> reached from either side) is supported by none of them.** Healing efficiency decays
> monotonically with cycle number, so `k_r` is not constant — `Ha` becomes `Ha(N)`, declining,
> and condition C4 below fails across the envelope. **`Ha` describes at most the first cycle.**
>
> The failure is class-dependent: microcapsule and high-crosslink systems decay onto a positive
> floor (finite repair budget — [[kirkwood-disposable-soma]] vindicated as the right frame, and
> still uncited), while low-crosslink vitrimers decay to zero (no steady state at all, the
> empirical echo of the `h → 1` ratchet defect noted in §on the constitutive law). The two empty
> polymer rows below cannot take a scalar `Ha` — each needs a **cycle label, a depletion
> parameter, and a class tag** {depletion-floor | finite-quality-to-zero}.

---

## 1. Prior art check — the *ratio* is named in queueing theory; the *healing* application is not

Searched for: a named dimensionless damage/healing group; a "healing Damköhler number"; a
self-healing availability metric; a steady-state damage fraction of the form
`k_r/(k_r + k_d)`.

| Searched | Result |
|---|---|
| `"Damköhler number"` + self-healing damage/healing ratio | Damköhler exists (reaction vs transport). **No healing variant.** |
| `"healing rate"` + `"damage rate"` + dimensionless + steady state | Only **healing efficiency** η = (property recovered)/(property lost). Amplitude, not a rate ratio. |
| Europe PMC `"self-healing" AND "damage rate" AND "healing rate"` | 6 hits, all asphalt/composite **healing indices** (67.8%, 90%, 19–55%) — amplitude fractions again. |
| arXiv self-healing network/elastomer models | [arXiv:2401.11087](https://arxiv.org/html/2401.11087v1) non-dimensionalises *time* (τ̄ = t/τ). Never forms a rate **ratio**, gives no numerical rate constants. |
| `k_repair/(k_repair + k_damage)` as a named number in *damage/healing* | Nothing. No self-healing, damage-mechanics or repair-biology source names the group. |
| **`"traffic intensity"` / `"offered load"` / `"Erlang B"` / M/M/1/1** (added 2026-09-05, A9) | **HIT — the ratio itself is standard.** See §1.1. `1/Ha = k_d/k_r` is the offered load `ρ`; `A = 1/(1+ρ)` is the Erlang-B blocking complement for one server. |

### 1.1 The queueing-theory row, stated properly

In a loss system the **offered load** (traffic intensity, measured in erlangs) is
`ρ = λ/μ` = arrival rate × mean holding time (Little's law applied to the offered stream)
— [Erlang (unit), Wikipedia, fetched 2026-09-05](https://en.wikipedia.org/wiki/Erlang_(unit)),
which cites Kleinrock, *Queueing Systems Vol. 1: Theory* (Wiley 1975) and Freeman,
*Fundamentals of Telecommunications* (Wiley 2005) as the standard texts; a modern open
textbook treatment is Zukerman, *Introduction to Queueing Theory and Stochastic Teletraffic
Models*, [arXiv:1307.2968](https://arxiv.org/abs/1307.2968) (author and title **VERIFIED** from
the arXiv abstract page, fetched 2026-09-05; the Erlang-B chapter itself was **not** fetched
this session — VERIFIED-SECONDARY).

The Erlang-B blocking probability for `m` servers is `B(ρ,m) = (ρ^m/m!) / Σ_{i=0}^{m} ρ^i/i!`.
Put `m = 1` (the M/M/1/1 loss system — one server, no queue) and it collapses, by arithmetic
done here:

    B(ρ,1) = ρ / (1 + ρ)        and        1 − B(ρ,1) = 1/(1 + ρ)

Now map: a unit that fails at hazard `k_d` and is restored at hazard `k_r` is a single server
whose "arrivals" are failures (rate `k_d`) and whose "holding time" is the repair (mean
`1/k_r`), so

    ρ = k_d / k_r = 1/Ha        ⟹        A = 1/(1 + ρ) = Ha/(1 + Ha)

which is (★) of §3.1 exactly. **`Ha` is the reciprocal of the offered load, and `A` is the
Erlang-B blocking complement of the one-server loss system.**

**Verdict on the row: the algebra is prior art; the axis is not.** What is genuinely absent is
any source that (a) applies this group to *damage and repair* rather than calls and channels,
or (b) puts biological and engineered repairing systems on one such axis. The honest claim is
therefore **not** "the ratio has no cross-domain name" — it has at least three (offered load /
traffic intensity in teletraffic, MTBF/MTTR in reliability, and unnamed steady-state ratios in
pharmacokinetics) — but "**no source connects them, and none applies the group to healing**".
`Ha`'s novelty grade should be read as *located/repackaged*, not *new object*.

**The gap survives in its narrowed form.** Engineering's `η` and biology's rate inequality are
both what you write when you cannot form the ratio; the ratio *does* exist, three domains away,
under a name nobody in either literature cites.

---

## 2. Das & Kumari, read in full — what they actually have

[arXiv:2503.18771v1](https://arxiv.org/html/2503.18771v1) (VERIFIED, fetched this session).

- **Damage variable `D`** — "ratio of the number of broken polymeric chains to the intact
  chains in a spherical RVE."
- **Healing variable `h`** — "ratio of the number of recovered bonds to the number of severed
  bonds."
- **What recovers:** the stiffness degradation factor `(1 − D(1−h))`, "the ratio of the
  effective area to the undamaged area." Fracture toughness recovers as
  `M_h = M(1 − exp(−√3·t_h /(2τ_D)))` (Eq. 59).
- **Timescales:** `τ_h = η_h/M` (chain diffusion), `τ_D = η_D/M` (bond rebonding); `M` is the
  resistive modulus, `η_h, η_D` are "the inverse of timescales associated with the evolution
  of damage and healing respectively."
- **Damage evolution** (Eq. 49):
  `(3/2)(1/√3)M l_R² ΔD + (3/2)μ(1−D)^{1/2}(Λ̄_r²−1) + (3K/4)(1−D)^{1/2}(J^{0.5}−1)² − 2(1/√3)M D − η_D Ḋ = 0`
- **Healing evolution** (Eq. 53):
  `2(1/√3)D²(1−h) + 1.5(1/√3) l_R²(1−h)(∇D)² + 1.5(1/√3) l_R² D² Δh − τ_h ḣ = 0`

**No dimensionless ratio of healing to damage rate appears anywhere.** The G5 narrowing is
confirmed against the primary source.

---

## 3. The group, derived

### 3.1 Two-state kinetics

Take one repairable unit, functional `U` or damaged `X`, with constant hazards
`U →(k_d) X` and `X →(k_r) U`. Let `p` be the probability of being damaged:

    dp/dt = k_d (1 − p) − k_r p

Set `dp/dt = 0`:

    k_d − k_d p* = k_r p*   ⟹   p* = k_d /(k_r + k_d)

so the **steady-state functional fraction** is

    A = 1 − p* = k_r /(k_r + k_d)                                  (★)

and the approach to it is exponential with **relaxation time**

    τ_relax = 1/(k_r + k_d)

Derived, not asserted: (★) is the unique fixed point of a linear first-order ODE, and it is
globally stable because the coefficient of `p` is `−(k_r + k_d) < 0`.

### 3.2 The dimensionless group

Define the **healing Damköhler number**

    Ha ≡ k_r / k_d    (repair rate / damage rate)

Dividing (★) top and bottom by `k_d`:

    A = Ha/(1 + Ha)         and, inverting,        Ha = A/(1 − A)

`Ha` runs on (0, ∞), `A` on (0, 1). `Ha = 1` is simply the point where `A = 0.5`: at steady
state half the population is damaged. It is **not** a threshold, a break-even or a collapse
point — see §6 item 2 and §3.1, which proves the steady state is globally stable for *every*
`Ha > 0`.

> **Symbol collision — read this before quoting `Ha` (added 2026-09-05, A10).** Two collisions,
> both real, and the symbol is retained anyway for the reason given:
>
> 1. **`Ha` is the Hartmann number in magnetohydrodynamics**, `Ha = BL√(σ/μ)`, the ratio of
>    Lorentz to viscous forces. That is an established, widely used group and this note's `Ha`
>    is unrelated to it. Outside this vault, always write it out as "healing Damköhler number
>    `Ha ≡ k_r/k_d`" on first use, or use the disambiguated form **`Da_h`**.
> 2. **"Damköhler" conventionally means reaction vs *transport***, not repair vs damage. `Da_I`
>    is reaction rate / convective transport rate; `Da_II` reaction / diffusion. This group is a
>    ratio of two *reaction-like* rates, so the name is an analogy to Damköhler's construction
>    (fast process / slow process), not an instance of it.
>
> **Decision: keep `Ha`, do not rename.** The symbol is load-bearing in
> [[C1-availability-living-tissue]], [[C10-healing-curve-fit]] and [[G5-repair-number]], so a
> rename is not local to this file and would trade one confusion for a broken cross-reference.
> `Da_h` is the recommended spelling in any external write-up.

### 3.3 Reduction to reliability availability

`MTBF = 1/k_d`, `MTTR = 1/k_r`. Then

    Ha = k_r/k_d = MTBF/MTTR
    A  = Ha/(1+Ha) = (MTBF/MTTR)/(1 + MTBF/MTTR) = MTBF/(MTBF + MTTR)

which is [[availability-formula]] exactly. `Ha` is the **MTBF-to-MTTR ratio**, which
reliability engineering computes constantly and has never named as a dimensionless group.

### 3.4 The Kedem-style algebra

`x ↦ x/(1+x)` is the same Möbius map that carries the thermoelectric figure of merit into the
Kedem–Caplan degree of coupling, `q² = ZT/(1+ZT)` (the G1 identity). So `Ha : A` stands to
availability exactly as `ZT : q²` stands to coupling. This is a **formal** correspondence of
the map, not a physical claim: in both cases an unbounded ratio of a "good" rate to a "bad"
rate is compressed onto (0,1). Worth one line, no more.

---

## 4. Binary vs continuous — the honest part

Reliability availability is a two-state Markov chain. Damage in continuum damage-healing
mechanics is a **field** `D(x,t) ∈ [0,1]`. These are not the same object, and the reduction is
conditional.

### 4.1 When it is legitimate

Let `φ(t)` be any continuous functional fraction obeying **linear** relaxation
`dφ/dt = k_r(1−φ) − k_d φ`. Then `φ* = k_r/(k_r+k_d)` — identical algebra, identical answer.
The binary chain is the special case where `φ` is an indicator variable.

The bridge is the **ensemble average**: for `N` statistically independent binary units, the
expected up-fraction obeys exactly the linear ODE above. So a continuous field is legitimately
read as an availability *iff* it is the mean of independent two-state units. Four conditions:

| # | Condition | Why it is needed |
|---|---|---|
| C1 | Damage is quantised into statistically independent units, or the field is their ensemble mean | Otherwise `φ` is not a probability of anything |
| C2 | Both rates are first-order in the state variable (constant hazard) | Otherwise no single `k_d`, `k_r` exist |
| C3 | No spatial gradient coupling (local limit, `l_R → 0`, or damage correlation length ≪ specimen) | Otherwise steady state is a boundary-value problem |
| C4 | Loading is stationary, so `k_d` is a constant and not a functional of history | Availability's `k_d` is exogenous |

**Photosystem II satisfies all four.** ~10⁸ independent complexes per leaf, first-order
photoinactivation at constant PPFD, no spatial coupling between complexes. Its `A` is both a
probability and a fraction, and the two coincide. This is caveat 1 of
[[C1-availability-living-tissue]] restated as a theorem rather than a worry.

### 4.2 Where it fails, specifically

Das & Kumari's system violates C1–C4 in three separable ways:

1. **Nonlinearity in the field.** Their healing driver is `2(1/√3) D²(1−h)` — healing runs
   *quadratically faster where damage is worse*. There is no constant `k_r`. `Ha` becomes a
   field `Ha(x)`, not a number.
2. **Nonlocality.** The `l_R² ΔD` and `l_R² D² Δh` terms make a point's steady state depend on
   its neighbours. A two-state chain has no spatial coupling.
3. **Load coupling and thresholds.** Damage is driven by `(1−D)^{1/2}(Λ̄_r²−1)`, i.e. by the
   current stretch. `k_d` is a functional of the loading history, not a constant.

**Does a closed-form steady state exist?** No, and here is exactly why. Setting `Ḋ = ḣ = 0` in
(49) and (53) does not eliminate the fields — it leaves a coupled pair of **nonlinear elliptic
PDEs** in `(D, h)`, because the Laplacian terms survive the time derivative going to zero.
Only in the strictly local limit `l_R → 0` does it collapse to an algebraic system, and even
then (49) reads `2(1/√3)M D = (3/2)μ(1−D)^{1/2}(Λ̄_r²−1) + (3K/4)(1−D)^{1/2}(J^{0.5}−1)²`,
which is implicit in `D` through `(1−D)^{1/2}` and solvable in closed form only for special
stress states. And (53) at `ḣ = 0` gives `D²(1−h) = 0`, i.e. `h → 1` for any `D > 0` — the
healing variable has **no interior steady state at all**, because nothing in their formulation
un-heals. Their model has damage-vs-healing *competition in time* but no *stationary balance*.

**That is a real finding.** CDHM as formulated cannot produce a steady-state functional
fraction, because healing is monotone: `h` is a ratchet, not a rate balance. To get a steady
state you must add a term that destroys healed bonds — which is what continuous loading does
physically and what the constitutive law omits.

### 4.3 So is *this* why nobody wrote it?

Partly. But the sharper reason is experimental, and it is the more useful finding:

> To form `Ha` you need `k_d` and `k_r` measured **separately on one specimen**. Biology can
> do this: lincomycin blocks D1 protein synthesis, so photoinactivation runs with repair
> switched off, giving `k_PI` alone; recovery in dim light then gives `k_REC`. **Materials
> science has no lincomycin.** You cannot suppress healing while continuing to load, so
> `k_d` and `k_r` are never separated — and the only observable left is the composite
> amplitude ratio `η`.

**The missing dimensionless group is missing because of a missing experimental control.** That
is testable, and it names a design target in the sense of METHOD §10: the control exists and
has not been used this way. In a **vitrimer**, bond exchange is thermally gated by the
topology-freezing temperature `T_v`. Load below `T_v` (healing off) to measure `k_d`, then
above (healing on) to measure `k_r`. That is the lincomycin of self-healing polymers, and the
row it would fill is empty in the table below.

---

## 5. The table — one axis, biology and engineering

> **Soil row filled 2026-09-05:** [[C35-soil-ha]] computes Ha for soil (erosion k_d vs soil production k_r): native vegetation 1.31, the USDA T-value policy point ≡ 1.00 by construction, conventional agriculture 0.011 — the lowest-Ha system in the vault by two orders. Remanufacturing rows are in [[C31-remanufacturing-ha]].

`Ha = k_r/k_d`. `A = Ha/(1+Ha)`. `τ_relax = 1/(k_r+k_d)`.

| System | k_d (damage) | k_r (repair) | **Ha** | **A** | τ_relax | Status |
|---|---|---|---|---|---|---|
| US electricity distribution, 2024 incl. major events | SAIFI 1.5 /yr | MTTR 7.3 h | **795** | **0.9987** | ~7.3 h | **VERIFIED** [EIA](https://www.eia.gov/todayinenergy/detail.php?id=66744) |
| US electricity distribution, non-major-event | — | SAIDI ≈ 2 h/yr | **≈4400** | **0.99977** | — | **VERIFIED** (same) |
| PSII, epipelic diatoms (GE-EPM), 20 °C | 2.78e-4 s⁻¹ | 23.67e-4 s⁻¹ | **8.51** | **0.895** | 378 s | **VERIFIED** [PMC10538756](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10538756/fullTextXML) |
| PSII, epipsammic (VA-EPL), 20 °C | 2.61e-4 s⁻¹ | 16.80e-4 s⁻¹ | **6.44** | **0.866** | 515 s | **VERIFIED** (same) |
| PSII, community mean, 20 °C | 2.70e-4 s⁻¹ | 20.4e-4 s⁻¹ | **7.56** | **0.883** | 433 s | **VERIFIED** (same) — reproduces C1 |
| PSII, VA-EPL, 35 °C heat stress | 4.14e-4 s⁻¹ | 9.92e-4 s⁻¹ | **2.40** | **0.706** | 711 s | **VERIFIED** (same) |
| PSII, GE-EPM, 35 °C heat stress | 4.95e-4 s⁻¹ | 6.36e-4 s⁻¹ | **1.28** | **0.562** | 885 s | **VERIFIED** (same) |
| PSII, VA-EPL, 5 °C cold stress | 3.11e-4 s⁻¹ | 2.82e-4 s⁻¹ | **0.907** | **0.476** | 1686 s | **VERIFIED** (same) |
| PSII, GE-EPM, 5 °C cold stress | 3.01e-4 s⁻¹ | 2.50e-4 s⁻¹ | **0.831** | **0.454** | 1815 s | **VERIFIED** (same) |
| Human trabecular bone — *full remodelling cycle* counted as down | site revisited every 730 d | cycle 200 d | **2.65** | **0.726** | — | **VERIFIED durations**, [PMC3028072](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3028072/fullTextXML); definition-dependent |
| Human trabecular bone — *resorption phase only* counted as down | site revisited every 730 d | resorption 35 d | **19.9** | **0.952** | — | **VERIFIED durations** (same) |
| Human cortical bone | cycle median 120 d; turnover rate **not obtained** | — | — | — | — | **PARTIAL** — cycle VERIFIED (same), revisit interval not found |
| Metallised-film capacitor, PEI, 200 MV/m, 80 °C | 165 events / 16 h = **2.9e-3 s⁻¹** | arc extinction "several µs" | **~1e7–1e8** | **1 − ~1e-8** | ~10 µs | k_d **VERIFIED** [PMC12429509](https://pmc.ncbi.nlm.nih.gov/articles/PMC12429509/); k_r **UNVERIFIED** (search snippet only; primary sources 403) |
| *Chlamydomonas reinhardtii* CC124 | 1.45e-3 s⁻¹ | 1.62e-3 s⁻¹ | 1.12 | 0.528 | — | **UNVERIFIED** — search-snippet only, primary not fetched |
| **Self-healing polymer / vitrimer** | **not published** | healing times published | **—** | **—** | — | **GAP.** No paper pairs a damage rate with a healing rate on one specimen. See §4.3 |
| **Self-healing concrete** | **not published** | healing times published (days) | **—** | **—** | — | **GAP.** Same reason |

Three systems populated with verified numbers, spanning biology (PSII, bone) and engineering
(the grid). One partial. **Two rows deliberately left empty** — the two the gap is actually
about. That absence is the measurement.

### Bone: a correction flagged against C1

The verified route here gives **0.726 or 0.952 depending on whether the formation phase counts
as downtime**, against C1's 0.939 (trabecular) which came by the remodelling-space route.
Caveat 2 of [[C1-availability-living-tissue]] — "a resorption cavity degrades stiffness rather
than eliminating it" — is exactly condition **C2** failing: bone is not two-state, and its
`A` is definition-dependent over a range of 0.23. **The C1 bone figures should be read as a
band, not a number.** The PSII figure, by contrast, reproduces exactly (0.883).

---

## 6. What the number buys — and what it costs

**Honest accounting first: `Ha` adds no information.** Given `(k_d, k_r)` you can compute
`Ha`; given `Ha` you cannot recover them. The map `(k_d,k_r) ↦ Ha` discards exactly one degree
of freedom — the **absolute timescale**. So as an information-theoretic matter this is a
lossy projection, not a gain.

That loss is precisely what it is for, and it buys three things the separate rates do not:

1. **Commensurability.** Rates carry units and system-specific magnitudes; a photosystem
   turns over in minutes and a distribution grid in hours. `Ha` is scale-free, so the table
   above exists. That is the whole point of the gap: *the shared axis*.
2. **Graded margin where the literature has only a binary.** Biology's published statement is
   the **inequality** "photoinhibition occurs when photoinactivation exceeds repair" — i.e.
   `Ha < 1`. The inequality is binary and says nothing about magnitude. `Ha` gives the
   magnitude: 7.6 at 20 °C (`A = 0.883`), 2.4 at 35 °C (`A = 0.706`), **0.91 at 5 °C**
   (`A = 0.476`). Cold stress is a system whose steady state has fallen from 88% functional to
   48% functional. An inequality cannot say that.

   > **Correction 2026-09-05 (A8) — `Ha = 1` is not a collapse threshold, and earlier wording
   > here said it was.** This item previously read "already over the line … running below
   > break-even". That is wrong for the model actually written down. §3.1 proves that
   > `dp/dt = k_d(1−p) − k_r p` has the unique fixed point `p* = k_d/(k_r+k_d)`, globally
   > stable for **every** `k_r, k_d > 0` because the coefficient of `p` is `−(k_r+k_d) < 0`.
   > There is no bifurcation, no critical `Ha`, and no runaway anywhere on `Ha ∈ (0, ∞)`:
   > `A = Ha/(1+Ha)` is smooth and strictly increasing, and `A > 0` for all `Ha > 0`.
   > `Ha = 1` is the `A = 0.5` point and nothing else — a *conventional* reference mark, like
   > the half-maximum of a titration curve, not a physical transition.
   >
   > **What a real collapse threshold would need.** Two model changes, either of which produces
   > a genuine critical `Ha`, and neither of which is in this note's kinetics:
   > - **An unbounded damage pool.** If damaged units accumulate outside the `[0,1]` budget —
   >   `dX/dt = k_d − k_r X` with `X` unbounded rather than `p ∈ [0,1]` — then repair capacity
   >   saturates at some `k_r^max` and `X` grows without bound once `k_d > k_r^max`. The
   >   threshold is a *capacity* limit, not the rate ratio.
   > - **Autocatalytic damage.** If damage begets damage, `dp/dt = k_d(1−p) + c p(1−p) − k_r p`,
   >   the fixed point can go unstable and a saddle-node appears at finite `c`; below it the
   >   system runs away to `p = 1`.
   >
   > Neither modification is supported by the PSII data used in §5, so **no collapse claim is
   > made anywhere in this note**. The 5 °C rows are low-availability, not collapsing. The
   > separate, real failure mode found in this vault is [[C10-healing-curve-fit]]'s declining
   > `k_r(N)` — a *depletion* result, which is again not a threshold in `Ha`.
3. **Better conditioning.** Both `k_PI` and `k_REC` are normalised by sample-specific PSII
   content, extraction efficiency and instrument calibration. Those factors **cancel in the
   ratio**. `Ha` is a more robust observable than either rate — the SNO move of METHOD §10,
   applied to a rate pair rather than a detector channel.

**And the negative result, stated plainly:** one number is not enough. `A` fixes *where* the
balance sits; it says nothing about *how fast* the system gets there, which is
`τ_relax = 1/(k_r+k_d)`. Two systems with identical `A = 0.883` — one relaxing in 400 s, one
in 400 days — behave completely differently under a fluctuating load. The complete
dimensionless reduction of a damage/healing pair is therefore the **pair `(A, τ_relax)`**, not
a single group. Anyone reporting only `Ha` has thrown away the half that determines dynamic
response.

---

## 7. Standing

- The group is **well-defined** and reduces to [[availability-formula]] by derivation.
- The binary→continuous reduction is **legitimate under C1–C4**, satisfied by PSII, violated
  by bone (C2, C4) and by CDHM (C1–C3).
- **CDHM as published has no steady state at all** in its healing variable — `h` is monotone.
  That is a defect in the constitutive law, not in this construction.
- **Prior art: partial hit, recorded 2026-09-05.** The *algebra* is standard queueing theory —
  `1/Ha` is the offered load `ρ` of an M/M/1/1 loss system and `A = 1/(1+ρ)` is the Erlang-B
  blocking complement (§1.1). The earlier claim that the form "has no cross-domain name" is
  **withdrawn**: it has three names in three literatures. What survives is the narrower and
  still-checkable claim that **no source applies the group to damage/repair, and none puts
  biology and engineering on one such axis**. [[G5-repair-number]] is narrowed, not filled.
- **`Ha = 1` is not a threshold.** The two-state model is globally stable for all `Ha > 0`;
  `Ha = 1` is the `A = 0.5` point. Any collapse language in earlier versions of §6 is retracted
  (§6 item 2, correction of 2026-09-05).
- Weakest link: the two empty rows are empty because of an experimental control that exists
  (`T_v` gating in vitrimers) and has not been used. That is the next measurement.

---

## Corrections 2026-09-05

Batch A items A8, A9, A10 from `BACKLOG.md`, sourced to `audits/01-math-physics.md` findings on
C6. Logged in [[log]].

| # | Was | Is now | What produced the change |
|---|---|---|---|
| A8 | §6 item 2: `Ha = 0.91` at 5 °C is "already over the line", a system "running below break-even"; `Ha = 1` framed as a collapse threshold | `Ha = 1` is the `A = 0.5` point only; the linear two-state model is globally stable for **all** `Ha > 0`; the 5 °C rows are low-availability (`A = 0.476`, `A = 0.454`), not collapsing; a real threshold needs an unbounded damage pool or an autocatalytic damage term, and neither is in this model | The note's own §3.1: `dp/dt = k_d(1−p) − k_r p` is linear with `p`-coefficient `−(k_r+k_d) < 0`, hence one globally stable fixed point for every positive rate pair. No new data. |
| A9 | §1: "`k_repair/(k_repair + k_damage)` … has no cross-domain name"; §7: "No prior art found" | §1.1 added: `ρ = k_d/k_r` is the **offered load / traffic intensity** of a loss system; `A = 1 − B(ρ,1) = 1/(1+ρ)` is the Erlang-B blocking complement at `m = 1`. §7 claim narrowed to "no source applies the group to healing / spans biology and engineering" | Erlang-B formula `B(ρ,m) = (ρ^m/m!)/Σ_{i=0}^m ρ^i/i!` from [Erlang (unit), Wikipedia](https://en.wikipedia.org/wiki/Erlang_(unit)) (fetched 2026-09-05; cites Kleinrock 1975 and Freeman 2005). `m = 1` reduction `B = ρ/(1+ρ)` done here. Textbook pointer: Zukerman, [arXiv:1307.2968](https://arxiv.org/abs/1307.2968), author/title verified from the abstract page, chapter not fetched → VERIFIED-SECONDARY. |
| A10 | §3.2 defined `Ha` with no note of any symbol clash | Collision callout added: `Ha` = Hartmann number in MHD; "Damköhler" conventionally = reaction/transport. **Kept, not renamed** — `Ha` is referenced from C1, C10 and G5, so a rename is not local to this file. `Da_h` recommended for external write-ups | Naming decision only; no number changed. |

**Numbers unchanged by this pass:** every row of the §5 table, all `Ha`, `A` and `τ_relax`
values, and the §5 bone band (0.726 / 0.952). A8–A10 are framing and prior-art corrections; no
arithmetic was recomputed.
