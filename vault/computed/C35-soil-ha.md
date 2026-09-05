---
name: C35-soil-ha
type: computed
exit: computation
extends-to: [sustainability, conservation]
next-step-cost: S
---

# Ha for a soil profile

> **Narrowed 2026-09-05: that `T` exceeds measured soil formation by an order of magnitude is
> already published (Montgomery 2007, Verheijen 2009), the `Ha` framing is structural only for a
> stock ([[C42-soil-ha-theory]]), and the one thing here that is the project's own is
> [[C43-soil-ha-replication]]'s site-level result — across 1,053 US sites `T` is *anti*-correlated
> with measured formation (Spearman ρ = −0.180, p = 4.5e-9), so `T` is not a bad formation
> estimate but not a formation estimate at all.**

> Soil under conventional agriculture runs at `Ha = 0.011` — destroyed ~90 times faster than it is
> made — while soil under native vegetation runs at `Ha = 1.31` and no-till lands between at
> `0.21`. That fills the row [[C6-damage-healing-ratio]] left blank. The USDA's tolerable-soil-loss
> `T` is a policy point that sets `Ha ≡ 1` by construction, while the measured formation rate is
> **22.6–54.3× smaller** than Montgomery's own stated `T` range allows.

Computes the object named missing in [[G36-wear-erosion-damage]] leg 2, and puts soil on C6's
axis next to PSII, bone, the offshore wind fleet ([[C31-remanufacturing-ha]]) and the grid.
Arithmetic re-runnable: `python _scripts/c35_soil.py` from `vault/`.

---

## 1. The quantity

```
k_d  ≡  soil loss rate          [mm/yr of profile depth]
k_r  ≡  soil formation rate     [mm/yr of profile depth]
Ha   ≡  k_r/k_d                 A = Ha/(1+Ha)
```

C6's `Ha` needs two rates in the same units. Soil publishes erosion two ways — **mass**
(t ha⁻¹ yr⁻¹, the USLE/RUSLE/WEPP/T-value convention) and **depth** (mm/yr, the
geomorphology/cosmogenic-nuclide convention) — and they are the same quantity only through a
bulk density:

```
depth [mm/yr]  =  mass [t/ha/yr] × 100 / ρ_b [kg/m³]
```

(1 t/ha = 0.1 kg/m²; divide by ρ_b for metres; ×1000 for mm.) With **ρ_b = 1300 kg/m³ — an
assumption, not a measurement** — 1 t/ha/yr = **0.0769 mm/yr**. The plausible range 1100–1600
moves every mass-derived depth by −15%/+18%. **Every row below that could be taken depth-native
was**, precisely to avoid the conversion; only the Borrelli and T-value rows pass through it.

## 2. Inputs

| # | Input | Value | Source, fetched 2026-09-05 |
|---|---|---|---|
| 1 | Erosion, conventional agriculture | median **1.537**, mean 3.939 mm/yr (n = 448) | Montgomery 2007, *PNAS* 104:13268, DOI `10.1073/pnas.0611508104`, **Table 1**, read from the author-hosted PDF (`mssoy.org/sites/default/files/documents/montgomery-2007.pdf`), text-extracted. **VERIFIED-PRIMARY** |
| 2 | Erosion, conservation/no-till | median **0.082**, mean 0.124 mm/yr (n = 47) | same, Table 1 |
| 3 | Erosion, native vegetation | median **0.013**, mean 0.053 mm/yr (n = 65) | same, Table 1 |
| 4 | **Soil production** (`k_r`) | median **0.017**, mean 0.036 mm/yr (n = 188) | same, Table 1 |
| 5 | Geological erosion | median 0.029, mean 0.173 mm/yr (n = 925) | same, Table 1 |
| 6 | Independent global soil production | 0.058–0.083 mm/yr | same, Discussion, citing its refs 51–52 — **VERIFIED-SECONDARY** (Montgomery's report of them, not the originals) |
| 7 | Global area-specific erosion | **2.8 Mg ha⁻¹ yr⁻¹**; 35.0 Pg/yr (2001), 35.9 Pg/yr (2012, +2.5%) | Borrelli *et al.* 2017, *Nat. Commun.* 8:2013, DOI `10.1038/s41467-017-02142-7`. DOI, title, authors, journal, year **Crossref-verified**; the numbers are **VERIFIED-SECONDARY** — see §6 |
| 8 | **USDA soil loss tolerance `T` — PRIMARY** | **5–12 t/ha/yr at ρ_b = 1200 kg/m³ ≈ 0.42–1.00 mm/yr (≈0.41 mm/yr at the low end); at this note's ρ_b = 1300, 0.385–0.923 mm/yr** | **Montgomery 2007** — the same VERIFIED-PRIMARY source as rows 1–5, which states `T` in its own text. Corrected 2026-09-05: this range, not row 8b, is the one to quote |
| 8b | USDA `T`, the policy range as written in the regulations | 1–5 short ton/acre/yr = 2.24–11.21 t/ha/yr = 0.172–0.862 mm/yr at ρ_b 1300 | USDA-NRCS convention; 1 t/ac/yr for shallow or fragile soils, 5 for deep soils. **VERIFIED-SECONDARY** (NRCS technical-note and encyclopedia summaries, 2026-09-05; no single NRCS handbook page fetched in full). **Retained as the secondary policy range.** Using a secondary number for a quantity the primary source states, without saying so, was the error |
| 9 | Bulk density ρ_b | 1300 kg/m³ | **ASSUMED**, not sourced. §1 |

Montgomery's own Table 1 is the load-bearing input, and it is the right one: it is a global
compilation with the erosion and the formation rates measured in **the same units on the same
axis by the same compilation**, which is exactly what C6's ratio requires and what almost no
other pairing in this vault has had.

## 3. Result — the soil rows of C6's axis

`Ha = k_r/k_d`, `k_r` = Montgomery's soil-production median (0.017 mm/yr) for median rows and its
mean (0.036) for mean rows.

**The `A` column is deleted for every soil row, 2026-09-05.** [[C42-soil-ha-theory]] §3 shows
`A = Ha/(1+Ha)` has no availability reading for a stock: there is no functional/damaged partition
of a depth, bedrock is absorbing so nothing cycles, and §6's proposed "steady-state thickness
relative to zero-erosion thickness" gloss is **false** — zero erosion sends `D → ∞` under an
exponential production function, so the denominator diverges. The only surviving reading,
`P/(P+E)`, is a monotone rescaling of `Ha` carrying no extra information. The non-soil rows keep
their `A` because for a conserved population of units it *is* an availability.

| System | k_d (damage) | k_r (repair) | **Ha** | **A** | Status |
|---|---|---|---|---|---|
| US electricity distribution, non-major-event | SAIFI 1.043/yr | MTTR 2.01 h | **≈4,400** | 0.99977 | C6 §5 |
| Offshore wind turbine fleet | 8.367 /yr | 726.4 /yr | **86.8** | 0.9886 | [[C31-remanufacturing-ha]] §4 |
| Trabecular bone, resorption-only down | 0.525 /yr | 10.43 /yr | **19.9** | 0.9520 | C6 §5 |
| PSII, community mean, 20 °C | 2.70e-4 /s | 20.4e-4 /s | **7.56** | 0.883 | C6 §5 |
| Trabecular bone, full cycle down | 0.689 /yr | 1.825 /yr | **2.65** | 0.7260 | C6 §5 |
| **Soil, native vegetation (median)** | **0.013 mm/yr** | **0.017 mm/yr** | **1.31** | — | **VERIFIED-PRIMARY**, computed here |
| **USDA `T`-value policy point** | `T` | **`≡ T` by construction** | **1.00** | — | **DEFINITIONAL — not a measurement.** §5 |
| PSII, 5 °C cold stress | 3.11e-4 /s | 2.82e-4 /s | **0.91** | 0.476 | C6 §5 |
| **Soil, native vegetation (mean)** | **0.053 mm/yr** | **0.036 mm/yr** | **0.679** | — | **VERIFIED-PRIMARY** |
| **Soil, no-till / conservation (mean)** | **0.124 mm/yr** | **0.036 mm/yr** | **0.290** | — | **VERIFIED-PRIMARY** |
| **Soil, no-till / conservation (median)** | **0.082 mm/yr** | **0.017 mm/yr** | **0.207** | — | **VERIFIED-PRIMARY** |
| **Soil, `T` = 1 ton/ac erosion vs *measured* `k_r`** (policy range, secondary) | 0.172 mm/yr | 0.017 mm/yr | **0.0986** | — | computed here |
| **Soil, global mean (Borrelli 2.8 t/ha/yr)** | **0.215 mm/yr** | **0.017 mm/yr** | **0.0789** | — | **VERIFIED-SECONDARY** on `k_d` |
| **Soil, `T` = 5 ton/ac erosion vs *measured* `k_r`** (policy range, secondary) | 0.862 mm/yr | 0.017 mm/yr | **0.0197** | — |
| **Soil, `T` = 5 t/ha/yr, Montgomery's own low end** | 0.385 mm/yr | 0.017 mm/yr | **0.0442** | — |
| **Soil, `T` = 12 t/ha/yr, Montgomery's own high end** | 0.923 mm/yr | 0.017 mm/yr | **0.0184** | — | computed here |
| **Soil, conventional agriculture (median)** | **1.537 mm/yr** | **0.017 mm/yr** | **0.0111** | — | **VERIFIED-PRIMARY** |
| **Soil, conventional agriculture (mean)** | **3.939 mm/yr** | **0.036 mm/yr** | **0.00914** | — | **VERIFIED-PRIMARY** |

**What the axis now shows.** Soil under conventional agriculture is the **lowest-`Ha` system in
this vault by two orders of magnitude** — below PSII under cold stress, which was previously the
floor. Native vegetation sits at `Ha ≈ 1`, i.e. exactly where a landscape in long-term balance
should sit, and that agreement is not circular: `k_d` (n = 65 erosion measurements) and `k_r`
(n = 188 soil-production measurements) are independent sample sets. **The whole span from native
vegetation to the plough is a factor of ~120 in `Ha`, and the entire span is a land-management
choice.** No-till recovers about one order of that and no more, which is the same conclusion
Montgomery draws in words, now on a scale shared with a leaf and a power grid.

## 4. The Archard mapping, written out

[[G36-wear-erosion-damage]] leg 1 claims `V = K·(F·s)/H` and `D_c = K_r(τ − τ_c)` are the same
kind of law. Here is the map, term by term, and where it fails.

| Archard | soil | comment |
|---|---|---|
| `V`, wear volume | detached volume per unit area = `D_c/ρ_b`, i.e. surface recession `[m/s]` | the bulk density of §1 is what makes these commensurable |
| `K`, wear coefficient (dimensionless) | **`K_r`, rill erodibility `[s/m]`** — *not* dimensionless | the two are the same *species* (fitted, unpredicted) and not the same *object* |
| `H`, indentation hardness `[Pa]` | **`τ_c`, critical shear stress `[Pa]`** | the resistance term, and the place the mapping breaks — see below |
| `F·s`, load × sliding distance = work `[J]` | **hydraulic work: `τ·v·t` per unit area**, i.e. stream power × time `[J/m²]` | flow shear × flow velocity is the erosive work rate; there is no "load" and no "distance", only a rate |

The dimensionless soil analogue of `K` is therefore

```
K_soil  ≡  (D_c/ρ_b)·τ_c / (τ·v)          [dimensionless]
```

and substituting WEPP,

```
K_soil  =  K_r·τ_c·(τ − τ_c) / (ρ_b·τ·v)
```

**Verdict: the mapping is exact in the objects and wrong in the functional form, and the
difference is diagnosable in one line.** `K_soil` is not a constant. It is 0 at `τ = τ_c`, rises
with `τ`, and asymptotes to `K_r·τ_c/(ρ_b·v)` as `τ ≫ τ_c`. Archard's `K`, by construction, is
independent of load. Two structural reasons:

1. **Threshold vs divisor.** Archard's resistance enters as a *divisor* (`V ∝ 1/H`), setting the
   magnitude at every load. WEPP's resistance enters as a *subtraction* (`D ∝ τ − τ_c`), setting
   an *onset*. A strictly Archard-shaped soil law would read `D = K·τ·v/τ_c` with no dead zone.
   WEPP is not that law, and the dead zone is not a nuisance term — below `τ_c` the erosion rate
   is exactly zero, which is why conservation practice works at all.
2. **Linearity holds only above threshold, and only in `τ`.** WEPP is linear in excess shear,
   so on the interval `τ > τ_c` the two laws are both affine and the comparison of slopes is
   legitimate. Extended to `τ → τ_c` it is not: Archard predicts finite wear where WEPP predicts
   none. **So `K` and `K_r` may be compared as slopes at high excess shear and nowhere else, and
   any such comparison must quote the `τ/τ_c` at which it was taken.** That single requirement is
   what kills the naive "both span 4–6 orders of magnitude" statement of G36's step 2 unless it
   is done carefully: `K_soil` spans orders of magnitude *within one soil* just by sweeping `τ`.

This is the unit-reconciliation trap G36 flags, worked through rather than deferred. It is also
why the leg-1 computation is the harder of the two and leg 2 was done first.

## 5. The prediction — REDISCOVERED, 2026-09-05

> **Grade: REDISCOVERED, not a prediction.** This section was written as a checkable claim about
> `T` versus measured formation. That comparison is **already published**. **Verheijen, Jones,
> Rickson & Smith 2009** (*Earth-Sci. Rev.* 94:23–38, DOI `10.1016/j.earscirev.2009.02.003`,
> Crossref-verified) sets tolerable ≡ formation at 0.3–1.4 t/ha/yr for Europe and reports actual
> arable erosion at **3–40× the upper tolerable limit** — the ratio follows by one division.
> **Montgomery 2007**, this note's own primary source, states the discrepancy at one to two orders
> of magnitude in his abstract. The soil-loss-tolerance review literature names the "1 inch in 30
> years" renewal assumption directly, and the arithmetic confirms it: `T` = 5 short ton/ac/yr =
> 0.862 mm/yr at ρ_b 1300 = **1 inch per 29.5 years**, to within 1.8%. So `Ha ≡ 1` at `T` is not a
> hidden convention this vault uncovered — **it is `T`'s construction.** The ratio below is
> retained as arithmetic on an established finding.
>
>
> **The residue — WITHDRAWN 2026-09-05. There is none.** This paragraph asserted that
> [[C43-soil-ha-replication]]'s site-level **Spearman ρ(`T`, `P`) = −0.180** was "nowhere in the
> prior art above" and "the one candidate here for a genuinely new empirical claim". Its own
> adversarial pass (`audits/c43-adversarial.md`) killed it: the correlation is spatial
> pseudoreplication plus a basin-gradient confound (0.5° cell medians ρ = −0.041, p = 0.58;
> cluster bootstrap over 48 source studies 95% CI [−0.341, +0.053]; rank-partial on slope
> −0.074; the sign **reverses** to +0.237 on low-gradient basins), it fails to replicate on 114
> independent sites ([[C47-tfact-mechanism-test]]: ρ = +0.090, p = 0.34, 95% CI [−0.095,
> +0.269]), and the depth-assignment mechanism is Skidmore 1982 / Schertz 1983 / Johnson 1987 /
> Alexander 1988. The "`tfact` = 1 is calibrated, median ratio 0.93" line falls with it (12.40 on
> the 7 low-gradient sites of that class). **Stated plainly: the soil thread yields no novel
> claim.** What it yields is a well-provenanced re-computation — median `T`/`P` ≈ 22 across 1,053
> US sites — already published in dimensioned form by Montgomery 2007, Stockmann et al. 2014,
> Evans et al. 2020, Kwang et al. 2023 and, at site level for 14 midwestern prairies, Quarrier et
> al. 2023. That is worth having; it is not new.


**The `T`-value convention sets `Ha ≡ 1`. That is `T`'s definition, not a finding.**

`T`, tolerable soil loss, is defined as the maximum erosion rate that permits productivity to be
maintained *indefinitely* — i.e. the rate at which loss is exactly balanced by formation. Written
in C6's variables that is `k_d ≡ k_r`, hence `Ha = 1` and `A = 0.5` **by construction, not by
measurement**. The number carries no information about any soil; it is the definition restated.

The checkable content is what happens when the convention meets the data:

> **Claim, restated on the primary `T` range.** Published `T`-values exceed measured soil
> formation rates for comparable soils by **22.6× to 54.3×**. Montgomery's own stated `T` range is
> **5–12 t/ha/yr** (at his ρ_b = 1200, ≈0.42–1.00 mm/yr; at this note's ρ_b = 1300, 0.385–0.923
> mm/yr) against his compiled soil-production median of 0.017 mm/yr (n = 188). **The policy point
> that claims `Ha = 1` sits, when the formation rate is measured rather than assumed, at
> `Ha = 0.018–0.044`.** On the secondary 1–5 short ton/ac policy range the ratio is 10.1–50.7× and
> `Ha` = 0.020–0.099; **both are quotable, the Montgomery range is the primary one, and the
> earlier revision of this note quoted only the secondary without saying so.** C43's independent
> 1,053-site median of 22.3 lands at the bottom of the primary band.

Even against the *most generous* published formation rate reached here (0.083 mm/yr, input 6),
`T` = 5 ton/ac still overstates by 10.4×, and `T` = 1 ton/ac by 2.1×.

**Falsifier.** A paired dataset in which `T`-values and independently measured soil production
rates for **the same soil series at the same sites** agree within a factor of 2 — i.e. a median
`T`/`k_r` ratio in [0.5, 2]. That would say `T` is a formation-rate estimate after all and the
`Ha = 1` policy point is physical, not nominal. The claim above says the ratio is ≥ 10.

**Dataset that would settle it — RUN, 2026-09-05.** The named desk task (Montgomery's SI joined
to SSURGO `tfact`, falling back to CRONUS/OCTOPUS if the US subset was thin) was executed in
[[C43-soil-ha-replication]]. Montgomery's SI was not obtainable (PNAS supplement 403), so OCTOPUS
v2.2 ¹⁰Be denudation was substituted as pre-authorised — which *inflates* `P` and so biases
against the claim by ~1.6×. **The falsifier did not fire**: 13.0% of sites land in [0.5, 2],
median 22.3, 877 of 1,053 above a ratio of 2 (p = 2e-112).

### The numbers policy can actually use — and they are Evans's, not this note's

The `Ha` ratio is dimensionless and therefore says nothing about *when*. The dimensioned object
is a lifespan, and **it is prior art**: Evans, Quinton, Davies, Zhao & Govers 2020 (*Environ. Res.
Lett.* 15:0940b2, DOI `10.1088/1748-9326/aba2fd`, Crossref-verified 2026-09-05, CC-BY) define
**soil lifespan `L = D/(E − F)`** at `D` = 300 mm over 10,030 plot-years from 255 sites, dividing
by a ¹⁰Be formation rate of 0.053 ± 0.005 mm/yr, and report 16% of conventional soils below 100
years and 39% of conservation soils above 10,000. **This note did not compute that and did not
cite it; both are corrected here.** [[C42-soil-ha-theory]] §4 supplies the exact version under a
depth-dependent production function:

| System | `L = D₀/(E − F)` | exact time to bedrock |
|---|---|---|
| Conventional agriculture (median 1.537 mm/yr) | **197 yr** | 203 yr |
| USDA `T` = 5 short ton/ac/yr | **355 yr** | 372 yr |
| USDA `T` = 1 short ton/ac/yr | **1,930 yr** | 2,592 yr |
| Native vegetation | thickening | never (`D_ss` = 773 mm) |

`D₀` = 300 mm. **`T` = 5 ton/ac/yr does not preserve the A-horizon; it licenses spending it over
roughly the lifetime of a nation.** And C42 §2 is sharper still: the steady state
`D_ss = D*·ln(P₀/E)` **exists only if `E` < `P₀` = 0.077 mm/yr**, which *no* managed row of §3
satisfies — including both `T` values. Above `P₀` there is no fixed point at all, only bedrock.

## 6. Honesty

**Erosion is not damage to a fixed unit, and this is the load-bearing objection.** C6's `Ha`
comes from a two-state chain over a *conserved population* of units that are either functional or
damaged. Soil is a **stock**: eroded material leaves, and what remains is not a damaged unit but
a thinner profile. The correct structural analogue is [[C31-remanufacturing-ha]]'s finding — with
an absorbing loss state and no replenishment there is **no interior steady state at all**, and
here `k_r` (weathering of bedrock into new soil) *is* the replenishment. ~~So the `A` column for
the soil rows should be read as the steady-state profile thickness relative to the thickness that
the same formation rate would sustain against zero erosion.~~ **That gloss is WITHDRAWN 2026-09-05
and the `A` column is deleted for soil** ([[C42-soil-ha-theory]] §3): under an exponential
production function zero erosion gives `D → ∞`, so the denominator of that ratio diverges. `Ha`
here is a ratio of rates that happens to be the same algebra, not the same object.
C6 §4.1's conditions C1 (quantised independent units) and C2 (constant hazard) both **fail** for
soil: there are no units, and both rates depend on the current profile depth (soil production is
famously depth-dependent — thin soil weathers faster, which is the humped soil-production
function). **A soil `Ha` is a flow balance, exactly as C31's fleet `Ha` is, and not a hazard
ratio.**

**C6's own grade limits the claim.** `Ha` is graded REPACKAGED in this vault's novelty audit —
`1/Ha` is the Erlang-B offered load, standard since Erlang, and C6 §7 withdrew the "no
cross-domain name" claim. This note adds a **fifth** application of a standard object plus one
number nobody had put together. It does not add a dimensionless group and must not be written up
as if it did. What is genuinely new here is (a) the `T`/`k_r` ratio of §5 and (b) placing soil on
the same axis as a photosystem.

**Depth vs mass is a real fork, not a units chore.** Erosion policy is written in mass, erosion
science increasingly in depth, and the conversion runs through a bulk density that erosion itself
changes — eroded soils compact, so a fixed ρ_b understates late-stage depth loss. Worse, the two
conventions do not measure the same thing even in principle: mass loss counts the whole eroded
mass while depth loss is what the *profile* records after deposition downslope. Rows 1–5 above are
depth-native and dodge this; the Borrelli and `T` rows do not, and the ±18% ρ_b band is the
smallest of their errors.

**The `T`-value has a political history and it is in the number.** `T` was not derived. Soil
Conservation Service groups assigned values of 2–6 ton/ac/yr in 1961–62 on rough estimates, the
range was later cut to 1–5, and the modern convention was fixed in 1973 "after intense debate"
over soil thickness and renewability. Nearing (2002) and Bazzoffi have both argued the values are
inadequate — the evidence base was thin and is now old, and the concept ignores off-site effects
entirely. A number set by committee in 1973 to be economically survivable is being used here as if
it were a claim about a rate balance. **It was always a permit, and `Ha = 1` is what a permit
looks like when you write it as physics.**

**A factor-of-2 ambiguity sits in `k_r`, and it is larger than the bulk-density band.**
[[C42-soil-ha-theory]] §7 evaluates Heimsath's soil-production function at the 300 mm horizon and
gets `P(300 mm)` = **0.0386 mm/yr — 2.3× Montgomery's compiled median of 0.017** that this note
uses as `k_r` in every row. Both are defensible and they are not measuring the same thing: a
*median across sites of unstated depth* is not `P` at a stated depth. **Every `Ha` above therefore
carries a factor-of-~2 ambiguity from a variable — soil depth — that neither source reports.**
That is a bigger error than the ±18% ρ_b band this note does discuss, and it was invisible until
the production function was written down. It changes no sign and no order of magnitude.

**What could not be fetched.** Borrelli 2017's full text: `nature.com` 303-redirects to an
identity provider and the PMC copy was not located, so its 2.8 Mg/ha/yr and 35.9 Pg/yr are
search-snippet figures against a Crossref-verified record — **VERIFIED-SECONDARY**, and the row
that uses them is marked as such. No NRCS handbook page defining `T` was fetched in full either;
the 1–5 ton/ac/yr range is consistent across three independent secondary summaries and is still
not a primary read — which is exactly why §2 now leads with Montgomery's own 5–12 t/ha/yr instead.
**Correction, 2026-09-05:** Borrelli 2017 *is* fetchable. It is gold OA (OpenAlex →
`nature.com/articles/s41467-017-02142-7.pdf`), read in full by [[C43-soil-ha-replication]], whose
printed text gives 2.8 Mg ha⁻¹ yr⁻¹ for 2001. The `k_d` for the global-mean row is now
**VERIFIED-PRIMARY**, and one extra datum came with it: Borrelli's own generic global `T`-value of
**10 Mg ha⁻¹ yr⁻¹** = 0.769 mm/yr at ρ_b 1300 is **45× Montgomery's formation median**, i.e. the
`Ha ≡ 1` construction identified here in USDA practice is being carried into global erosion
modelling at a value above the top of the USDA range.

## Corrections 2026-09-05 (deep inquiry)

Four legs ran against this note and [[G36-wear-erosion-damage]] on 2026-09-05 — an adversarial
review, a provenance re-run, [[C42-soil-ha-theory]] and [[C43-soil-ha-replication]]. **Every unit
conversion and every arithmetic result in this note reproduced exactly and none is in question.**
What changed:

| # | What was wrong or missing | What it is now | Where |
|---|---|---|---|
| 1 | `T` quoted only as 1–5 short ton/ac from **secondary** NRCS summaries, while this note's own VERIFIED-PRIMARY source states `T` | Montgomery's **5–12 t/ha/yr at ρ_b 1200 (≈0.41 mm/yr at the low end)** is the primary range; the 1–5 ton/ac policy range is retained as secondary and labelled | §2 rows 8/8b |
| 2 | Ratio stated as **10.1–50.7×** on the secondary range only | **22.6–54.3×** on Montgomery's own range, `Ha` = 0.018–0.044; the secondary figures kept alongside | §5 |
| 3 | An `A = Ha/(1+Ha)` column on every soil row | **Deleted for soil.** `A` has no availability reading for a stock | §3 |
| 4 | §6's gloss on `A` — "steady-state thickness relative to zero-erosion thickness" | **Withdrawn as false**; zero erosion gives `D → ∞`, the denominator diverges | §6 |
| 5 | §5 presented as a prediction | **Regraded REDISCOVERED** — Verheijen 2009 (tolerable ≡ formation, actual 3–40× the upper limit) and Montgomery 2007 both published it; `T` = 5 ton/ac = 1 inch/29.5 yr, so `Ha ≡ 1` is `T`'s construction | §5 |
| 6 | No dimensioned, policy-usable number, and no citation to the published one | Evans *et al.* 2020's soil lifespan `L = D/(E−F)` cited (correct DOI `10.1088/1748-9326/aba2fd`), plus C42's exact time-to-bedrock: **197 yr** conventional, **355 yr** at `T` = 5, **1,930 yr** at `T` = 1 | §5 |
| 7 | No statement of the depth ambiguity in `k_r` | Heimsath `P(300 mm)` = 0.0386 vs Montgomery median 0.017 — a **factor-2 ambiguity** in every `Ha` here | §6 |
| 8 | Borrelli 2017 recorded as unfetchable, `k_d` VERIFIED-SECONDARY | Gold OA, read in full by C43; **VERIFIED-PRIMARY**. Its generic global `T` = 10 Mg/ha/yr is 45× formation | §6 |
| 9 | §5's falsifier named but not run | **Run on 1,053 US sites** in C43; did not fire (median 22.3, 13.0% inside [0.5, 2]) | §5 |
| 10 | Two citations carried by this note's brief | Stockmann *et al.* 2014 is *Geoderma* 216:48–61, not *Earth-Sci. Rev.*; Bui *et al.* 2011 is *Agric. Ecosyst. Environ.*, not *Geoderma* | C43 §1 |

**Novelty, restated honestly.** This note grades **REPACKAGED (+ CORRECTED)**, with §5
**REDISCOVERED**. The erosion÷formation ratio is mainstream soil science; the `Ha` framing is the
project's and [[C42-soil-ha-theory]] shows it is the weakest of the three available framings — it
is the USDA's own Erosion Index `EI` = potential erosion / `T` reciprocated, with a measured `P`
swapped in for `T`. The single candidate for a genuinely new empirical claim in this cluster is
**C43's site-level `ρ(T, P)` = −0.180**, and it awaits its own adversarial pass.
