---
name: C35-soil-ha
type: computed
exit: computation
extends-to: [sustainability, conservation]
next-step-cost: S
---

# Ha for a soil profile

> **Soil under conventional agriculture runs at `Ha = 0.011` — it is destroyed ~90 times faster
> than it is made — while soil under native vegetation runs at `Ha = 1.31`, and no-till lands
> between at `0.21`. That fills the row [[C6-damage-healing-ratio]] left blank, and it exposes
> the USDA's tolerable-soil-loss `T` as a policy point that sets `Ha ≡ 1` by construction while
> the measured formation rate is 10–51× smaller than `T` allows.**

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
| 8 | USDA soil loss tolerance `T` | **1–5 short ton/acre/yr = 2.24–11.21 t/ha/yr = 0.172–0.862 mm/yr** | USDA-NRCS convention; 1 t/ac/yr for shallow or fragile soils, 5 for deep soils. **VERIFIED-SECONDARY** (NRCS technical-note and encyclopedia summaries, 2026-09-05; no single NRCS handbook page was fetched in full) |
| 9 | Bulk density ρ_b | 1300 kg/m³ | **ASSUMED**, not sourced. §1 |

Montgomery's own Table 1 is the load-bearing input, and it is the right one: it is a global
compilation with the erosion and the formation rates measured in **the same units on the same
axis by the same compilation**, which is exactly what C6's ratio requires and what almost no
other pairing in this vault has had.

## 3. Result — the soil rows of C6's axis

`Ha = k_r/k_d`, `A = Ha/(1+Ha)`, `k_r` = Montgomery's soil-production median (0.017 mm/yr) for
median rows and its mean (0.036) for mean rows.

| System | k_d (damage) | k_r (repair) | **Ha** | **A** | Status |
|---|---|---|---|---|---|
| US electricity distribution, non-major-event | SAIFI 1.043/yr | MTTR 2.01 h | **≈4,400** | 0.99977 | C6 §5 |
| Offshore wind turbine fleet | 8.367 /yr | 726.4 /yr | **86.8** | 0.9886 | [[C31-remanufacturing-ha]] §4 |
| Trabecular bone, resorption-only down | 0.525 /yr | 10.43 /yr | **19.9** | 0.9520 | C6 §5 |
| PSII, community mean, 20 °C | 2.70e-4 /s | 20.4e-4 /s | **7.56** | 0.883 | C6 §5 |
| Trabecular bone, full cycle down | 0.689 /yr | 1.825 /yr | **2.65** | 0.7260 | C6 §5 |
| **Soil, native vegetation (median)** | **0.013 mm/yr** | **0.017 mm/yr** | **1.31** | **0.567** | **VERIFIED-PRIMARY**, computed here |
| **USDA `T`-value policy point** | `T` | **`≡ T` by construction** | **1.00** | **0.500** | **DEFINITIONAL — not a measurement.** §5 |
| PSII, 5 °C cold stress | 3.11e-4 /s | 2.82e-4 /s | **0.91** | 0.476 | C6 §5 |
| **Soil, native vegetation (mean)** | **0.053 mm/yr** | **0.036 mm/yr** | **0.679** | **0.405** | **VERIFIED-PRIMARY** |
| **Soil, no-till / conservation (mean)** | **0.124 mm/yr** | **0.036 mm/yr** | **0.290** | **0.225** | **VERIFIED-PRIMARY** |
| **Soil, no-till / conservation (median)** | **0.082 mm/yr** | **0.017 mm/yr** | **0.207** | **0.172** | **VERIFIED-PRIMARY** |
| **Soil, `T` = 1 ton/ac erosion vs *measured* `k_r`** | 0.172 mm/yr | 0.017 mm/yr | **0.0986** | 0.0897 | computed here |
| **Soil, global mean (Borrelli 2.8 t/ha/yr)** | **0.215 mm/yr** | **0.017 mm/yr** | **0.0789** | **0.0732** | **VERIFIED-SECONDARY** on `k_d` |
| **Soil, `T` = 5 ton/ac erosion vs *measured* `k_r`** | 0.862 mm/yr | 0.017 mm/yr | **0.0197** | 0.0193 | computed here |
| **Soil, conventional agriculture (median)** | **1.537 mm/yr** | **0.017 mm/yr** | **0.0111** | **0.0109** | **VERIFIED-PRIMARY** |
| **Soil, conventional agriculture (mean)** | **3.939 mm/yr** | **0.036 mm/yr** | **0.00914** | **0.00906** | **VERIFIED-PRIMARY** |

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

## 5. The prediction

**The `T`-value convention sets `Ha ≡ 1`, and therefore `A = 0.5` in C6's reading. Soil science
has never said this.**

`T`, tolerable soil loss, is defined as the maximum erosion rate that permits productivity to be
maintained *indefinitely* — i.e. the rate at which loss is exactly balanced by formation. Written
in C6's variables that is `k_d ≡ k_r`, hence `Ha = 1` and `A = 0.5` **by construction, not by
measurement**. The number carries no information about any soil; it is the definition restated.

The checkable content is what happens when the convention meets the data:

> **Claim.** Published USDA `T`-values exceed measured soil formation rates for comparable soils
> by **10.1× to 50.7×**. `T` = 1–5 ton/ac/yr is 0.172–0.862 mm/yr at ρ_b = 1300; Montgomery's
> compiled soil-production median is 0.017 mm/yr (n = 188). **The policy point that claims
> `Ha = 1` sits, when the formation rate is measured rather than assumed, at `Ha = 0.020–0.099`.**
> Montgomery says the same thing in words — his measured rates are "substantially lower than the
> `T` values endorsed by the USDA" — and does not put a number on the ratio. This is that number.

Even against the *most generous* published formation rate reached here (0.083 mm/yr, input 6),
`T` = 5 ton/ac still overstates by 10.4×, and `T` = 1 ton/ac by 2.1×.

**Falsifier.** A paired dataset in which `T`-values and independently measured soil production
rates for **the same soil series at the same sites** agree within a factor of 2 — i.e. a median
`T`/`k_r` ratio in [0.5, 2]. That would say `T` is a formation-rate estimate after all and the
`Ha = 1` policy point is physical, not nominal. The claim above says the ratio is ≥ 10.

**Dataset that would settle it.** Montgomery 2007's SI compilation of soil-production rates
(n = 188, overwhelmingly ¹⁰Be cosmogenic-nuclide profiles with site coordinates) joined by
location to **USDA-NRCS SSURGO's `tfact` attribute**, which publishes a `T` value for every
mapped soil component in the United States. Both are open. The join is a desk task; the US-only
subset of Montgomery's compilation is the sample size to check first, and if it is too thin the
same join runs against the ¹⁰Be compilations of the CRONUS/OCTOPUS databases.

## 6. Honesty

**Erosion is not damage to a fixed unit, and this is the load-bearing objection.** C6's `Ha`
comes from a two-state chain over a *conserved population* of units that are either functional or
damaged. Soil is a **stock**: eroded material leaves, and what remains is not a damaged unit but
a thinner profile. The correct structural analogue is [[C31-remanufacturing-ha]]'s finding — with
an absorbing loss state and no replenishment there is **no interior steady state at all**, and
here `k_r` (weathering of bedrock into new soil) *is* the replenishment. So the `A` column for the
soil rows should be read as **the steady-state profile thickness relative to the thickness that
the same formation rate would sustain against zero erosion**, not as "fraction of units
functional". It is a ratio of rates that happens to be the same algebra, not the same object.
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

**What could not be fetched.** Borrelli 2017's full text: `nature.com` 303-redirects to an
identity provider and the PMC copy was not located, so its 2.8 Mg/ha/yr and 35.9 Pg/yr are
search-snippet figures against a Crossref-verified record — **VERIFIED-SECONDARY**, and the row
that uses them is marked as such. No NRCS handbook page defining `T` was fetched in full either;
the 1–5 ton/ac/yr range is consistent across three independent secondary summaries and is still
not a primary read.
