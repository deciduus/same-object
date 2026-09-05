---
name: C27-product-lifespan-beta
type: computed
closes: G30-weibull-product-lifespan
last-checked: 2026-09-05
result: "21 published product-lifespan Weibull fits placed on C18's beta axis; product classes span beta = 1.00 to 6.0 and split cleanly into a memoryless band (beta approx 1, gas boilers and room air-conditioners) and a wear-out band (beta > 2, cars, furnaces, central AC). Every product class sits below Li-ion's beta = 12.7 and above nothing; the enzyme/flow-battery beta approx 1 corner now has company from consumer durables."
exit: computation
extends-to: [circularity, sustainability]
next-step-cost: S
---

# Product lifespans on the Weibull-β axis

> **21 published product-lifespan Weibull fits, placed on [[C18-durability-axis]]'s β axis, span
> `β = 1.00` to `β = 6.0` and separate into two bands: a memoryless band at `β ≈ 1.0–1.1` (US gas
> boilers `β = 1.000 ± 0.148`, room air-conditioners `β ≈ 1.07–1.08`) and a wear-out band at
> `β ≥ 2` (European passenger cars `β = 2.0–6.0`, US gas furnaces `2.218`, central AC `2.094`).
> The whole product world sits *below* Li-ion's `β = 12.7` and *at or above* the enzyme /
> flow-battery reactant corner at `β = 1`. So consumer durables are not one population: some die
> like enzymes and some die like electrode wear, and which band a class falls in is a *policy*
> discriminator, not a physics one — because product "death" here is discard, not failure.**
> Narrows [[G30-weibull-product-lifespan]] from "no one has drawn the axis" to "the axis is
> drawable, one side of it is contaminated by exit mode, and the contamination is measurable."

Bears on [[C18-durability-axis]], [[G3-cycle-life]], [[G30-weibull-product-lifespan]].

Arithmetic reproduced by `vault/_scripts/c27_beta.py` (no network calls; published parameters in,
median/mean/hazard-fold out).

---

## 1. The quantity

```
S(t) = exp( −((t − θ)/η)^β )         t ≥ θ
h(t) = (β/η)·((t − θ)/η)^(β−1)
H    ≡ h(2M)/h(M/2) = 4^(β−1)        the hazard-fold over one factor-of-four in age
```

`β` is dimensionless and is the *only* parameter that carries the failure law; `η` (characteristic
life, 63.2% quantile) and `θ` (delay) carry the timescale. `H` is `β` restated so it can be read
without a plot: **`H = 1` means a unit's chance of leaving service does not depend on its age;
`H = 100` means a four-times-older unit is a hundred times more likely to leave this year.**

`β` is bounded below by 0 and unbounded above; the empirically occupied range across everything on
this axis is `1.00 ≤ β ≤ 12.7`, i.e. `1 ≤ H ≤ 1.1×10⁷`.

## 2. Inputs — the fits, with source and locator

**A. US residential appliances.** Lutz, Hopkins, Letschert, Franco & Sturges, *Using National
Survey Data to Estimate Lifetimes of Residential Appliances*, LBNL report, October 2011 —
[osti.gov/servlets/purl/1182737](https://www.osti.gov/servlets/purl/1182737), **PDF fetched and
read in full 2026-09-05, `VERIFIED-fetched`.** Delayed two-parameter Weibull, least-squares fit of
survival function to RECS + AHS household-survey stock-by-age against AHAM shipments. Errors are
the report's own standard errors on the fitted parameter. Locators are that report's table numbers.

**B. European passenger cars.** Held, Rosat, Georges, Pengg & Boulouchos, "Lifespans of passenger
cars in Europe: empirical modelling of fleet turnover dynamics", *Eur. Transp. Res. Rev.* 13:9
(2021), DOI `10.1186/s12544-020-00464-0` — Crossref-verified 2026-09-05 (title, journal, 2021-01-25,
`is-referenced-by-count` = 50); parameters read from the open-access full text at
[PMC7829067](https://pmc.ncbi.nlm.nih.gov/articles/PMC7829067/), **Table 1**, `VERIFIED-fetched`
(10-country subset of a 31-country table; the other 21 rows were not transcribed).

**C. The C18 rows**, carried over unchanged from [[C18-durability-axis]] §2–3 with their existing
grades (Li-ion `β = 12.7` is `VERIFIED-via-search` only, not fetch-verified).

**D. Rows that could NOT be sourced to a fetched number** — recorded here rather than dropped:

| Wanted | Status |
|---|---|
| Oguchi & Fuse 2015 ES&T `10.1021/es505245q`, automobile shape parameter and the *constant* value proposed for the simplified method | **NOT OBTAINED.** Crossref record verified (title, ES&T, 2015-01-17, `is-referenced-by-count` = 98); ACS full text HTTP 403, no OA copy, Semantic Scholar carries no abstract. The paper's headline claim — "the shape parameter can be replaced by a constant for all countries and years" — is `VERIFIED-via-search` (search snippet) but **the constant itself is unknown to this note.** |
| Murakami/Oguchi et al., *Lifespan of Commodities* Parts I & II, *J. Ind. Ecol.* 14:598–612 and 613–626 (2010), DOIs `10.1111/j.1530-9290.2010.00250.x` / `.00251.x` | **NOT OBTAINED.** Both DOIs Crossref-verified 2026-09-05 (Part I 172 citations, Part II 116). Wiley full text 403. Per-commodity β not in hand. *Note the DOI supplied in the task brief, `10.1111/j.1530-9290.2010.00272.x`, is a different paper — Crossref resolves it to "Environmental Metrics", J. Ind. Ecol. 2010. The correct Part I/II DOIs are the two above.* |
| Bakker, Wang, Huisman & den Hollander, "Products that go round", *J. Cleaner Prod.* 69:10–16 (2014), DOI `10.1016/j.jclepro.2014.01.028` | Crossref-verified 2026-09-05 (`is-referenced-by-count` = 623). **No Weibull β expected or found** — it is a design-strategy paper reporting *mean* lifetimes, not fitted distributions. It stays off the axis, which is itself the point of §5. |
| Krych, Pettersen et al., "Long-term lifetime trends of large appliances since the introduction in Norwegian households", *J. Ind. Ecol.* (2025), DOI `10.1111/jiec.13608` | Semantic Scholar reports it open-access; Wiley returned 403 to both HTML and `pdfdirect`. Abstract retrieved: washing-machine lifetimes fell **−45%** and ovens **−39%** around the 1990s–2000s. **Shape parameters NOT OBTAINED** — this is the single most valuable missing row, because it is a *mean* shift with an unreported shape (see §5's prediction). |
| Korean WEEE, eight product classes | Shape parameters reported as ranging **1.49–2.43** (population-balance model, 1,000-household questionnaire). `VERIFIED-via-search` **only** — abstract snippet, no DOI resolved, no table locator. Quoted once, as a range, never as a row. |

## 3. Result — the axis

`H = 4^(β−1)`, computed in `_scripts/c27_beta.py`. Sorted by β.

| System | class | axis | **β** | η (yr) | **H** | source · locator |
|---|---|---|---|---|---|---|
| Enzyme, suicide inactivation | catalyst | cycles | **1.00** | — | 1.0 | [[C18-durability-axis]] §2.1 |
| Enzyme, thermal denaturation | catalyst | time | **1.00** | — | 1.0 | [[C18-durability-axis]] §2.1 |
| Organic flow-battery reactant | storage | time | **1.00** | — | 1.0 | [[C18-durability-axis]] §2.3 |
| **Gas boiler (US)** | durable | time | **1.000 ± 0.148** | 25.31 | **1.0** | Lutz 2011 Table 5 |
| **Room air-conditioner, pre-2000 (US)** | durable | time | **1.067 ± 0.090** | 6.92 (θ = 8.0) | 1.10 | Lutz 2011 Table 9 |
| **Room air-conditioner, post-2000 (US)** | durable | time | **1.08 ± 0.06** | 10.27 | 1.12 | Lutz 2011 Table 10 |
| **Electric storage water heater (US)** | durable | time | **1.174 ± 0.020** | 13.19 | 1.27 | Lutz 2011 Table 7 |
| **Refrigerator (US)** | durable | time | **1.272 ± 0.187** | 11.75 (θ = 8.87) | 1.46 | Lutz 2011 Table 11 |
| **Gas storage water heater (US)** | durable | time | **1.307 ± 0.061** | 11.64 (θ = 3.20) | 1.53 | Lutz 2011 Table 6 |
| **Room air-conditioner, pooled (US)** | durable | time | **1.442 ± 0.040** | 14.29 | 1.85 | Lutz 2011 Table 8 |
| **Heat pump (US)** | durable | time | **1.525 ± 0.525** | 18.62 | 2.07 | Lutz 2011 Table 3 |
| **Freezer (US)** | durable | time | **1.885 ± 0.730** | 17.92 (θ = 6.46) | 3.41 | Lutz 2011 Table 12 |
| **Passenger car, Luxembourg** | durable | time | **2.0** | 8.0 | 4.0 | Held 2021 Table 1 |
| **Passenger car, Belgium** | durable | time | **2.0** | 11.7 | 4.0 | Held 2021 Table 1 |
| **Central air-conditioner (US)** | durable | time | **2.094 ± 0.271** | 21.49 | 4.56 | Lutz 2011 Table 2 |
| **Gas furnace (US)** | durable | time | **2.218 ± 0.320** | 26.68 | 5.41 | Lutz 2011 Table 4 |
| **Passenger car, Germany** | durable | time | **2.4** | 14.8 | 6.96 | Held 2021 Table 1 |
| **Passenger car, Italy** | durable | time | **2.7** | 19.6 | 10.6 | Held 2021 Table 1 |
| **Passenger car, Spain** | durable | time | **3.2** | 19.4 | 21.1 | Held 2021 Table 1 |
| **Passenger car, Austria** | durable | time | **3.4** | 15.9 | 27.9 | Held 2021 Table 1 |
| **Passenger car, Switzerland** | durable | time | **3.6** | 15.4 | 36.8 | Held 2021 Table 1 |
| **Passenger car, Greece** | durable | time | **4.2** | 33.9 | 84.5 | Held 2021 Table 1 |
| **Passenger car, Netherlands** | durable | time | **4.4** | 17.2 | 111 | Held 2021 Table 1 |
| **Passenger car, Poland** | durable | time | **6.0** | 35.1 | 1,024 | Held 2021 Table 1 |
| Li-ion cell NCR18650GA | storage | cycles | **12.7** | — | 1.1×10⁷ | [[C18-durability-axis]] §2.2 (`VERIFIED-via-search`) |

Korean WEEE, eight EEE classes, `β ∈ [1.49, 2.43]` — consistent with the appliance band above, but
`VERIFIED-via-search` only and therefore **not given rows**.

### Internal consistency check on the source

Re-deriving `median = θ + η·(ln2)^(1/β)` and `mean = θ + η·Γ(1+1/β)` from each row's own `(β, η, θ)`
reproduces the published median and mean to ±0.01 yr for **ten of eleven** LBNL rows. The exception
is **Table 10 (RAC, post-2000)**: from `β = 1.08, η = 10.27, θ = 0` the median is **7.31 yr** and the
mean **9.97 yr**, against the published 8.36 and 11.27. The published median implies `η ≈ 11.96`.
**Table 10's scale parameter is internally inconsistent with its own median at the printed
precision** — flagged, not corrected, and the β (which is what this note uses) is unaffected.

## 4. The circularity claim, stated as a discriminator

**The discriminator.** For a product class, `β ≈ 1` means the annual probability of leaving service
is flat in age — a memoryless loss process: theft, breakage-by-accident, moving house, a phone
contract ending, an obsolescence event that arrives on a clock unrelated to the unit's own wear.
`β > 1` means the annual probability climbs with age — accumulating physical damage, or an
economic decision whose threshold is crossed with age (repair cost vs residual value).

| band | classes here | what is limiting the life | policy that moves the mean |
|---|---|---|---|
| `β ≈ 1.0–1.1`, `H ≤ 1.1` | gas boilers, room air-conditioners | **not the unit's condition** | design-life and durability specs are *wasted*; the binding lever is the loss/obsolescence process — warranty length, resale and re-use channels, standards that stop the unit being stranded |
| `β ≈ 1.2–1.9`, `H = 1.3–3.4` | water heaters, refrigerators, freezers, heat pumps | mixed | **repairability and spares availability**: the hazard climbs slowly, so a repair right extends a long tail of survivors |
| `β ≥ 2`, `H ≥ 4` | cars, gas furnaces, central AC | age-dependent, sharp | **design life**: the population hits a wall together; repair rights change little near the wall, and raising `η` (build quality, corrosion protection) is the lever |

This is the same partition [[C18-durability-axis]] drew between enzymes (`β = 1`, memoryless
catastrophe) and Li-ion (`β > 1`, wear-out), applied to consumer durables — and it does the same
non-trivial work: **it does not group by product category.** A gas boiler groups with an enzyme; a
gas furnace, its near neighbour in a basement, groups with a passenger car. The grouping is by
failure law, not by object.

**The policy consequence, in one line: right-to-repair and warranty extension are `β`-dependent
instruments.** On a `β ≈ 1` class they raise the mean without touching the shape (the loss process
is untouched); on a `β ≈ 1.3` class they act on the tail; on a `β ≥ 3` class they act on almost
nothing, because the survivors are already close to the wall.

## 5. The prediction

**Prediction P1 (shape-invariance under a mean-shifting intervention).** A right-to-repair regime,
or an extended-warranty mandate, applied to a class whose current fit has `β ≤ 1.5`, will raise
`η` (and the mean and median) **without raising `β` by more than its own standard error.** In
`H` terms: `H` stays inside `[1, 2]` while the mean moves by ≥10%.

This is testable on the next lifespan survey round for any class where a pre-intervention fit is
already published — EU refrigerators and washing machines under the 2021 ecodesign
repairability/spare-parts rules are the obvious case, against the LBNL refrigerator baseline
`β = 1.272 ± 0.187` and any pre-2021 European fit. **The refutation is a `β` that climbs with the
mean**, which would say the intervention converted a loss process into a wear-out process — i.e.
that units are now being kept until they physically fail.

**P1 has no measurement yet. The "natural experiment" this note previously claimed is
withdrawn.** An earlier version paired LBNL's room air-conditioners fitted separately on pre-2000
and post-2000 survey data (Tables 9, 10) — "the mean fell 14.75 → 11.27 yr (−24%) while β moved
1.067 → 1.08, well inside the standard errors" — and called it a passing natural-experiment
measurement of P1. It is not one, for three independent reasons, any one of which is sufficient:

1. **The two rows are not comparable, by this note's own §6(c).** The pre-2000 fit carries
   `θ = 8.0` and the post-2000 fit `θ = 0`. §6(c) states that a large `θ` "absorbs early exits and
   therefore **inflates `β`** relative to a delay-free fit — those two `β` are not directly
   comparable with the `θ = 0` rows." The comparison being offered as evidence is precisely the
   one the honesty section rules out, three sections later.
2. **The mean shift uses a figure §3 has just shown is self-inconsistent.** 11.27 yr is Table 10's
   *published* mean; §3's internal-consistency check re-derives **9.97 yr** from Table 10's own
   `(β = 1.08, η = 10.27, θ = 0)`, and flags Table 10's scale parameter as inconsistent with its
   own median. Using the published mean gives −24%; using the row's own parameters gives −32%.
   The note cannot quote a number it has itself flagged as unreliable as the measured effect.
3. **No intervention occurred.** P1 is a claim about behaviour *under a mean-shifting
   intervention*. These are two survey vintages fitted separately — a change of measurement
   period, with no policy, no treatment and no control. Whatever moved the mean between them is
   unidentified, and could as easily be a change in the survey instrument as a change in the
   product.

The honest status is therefore: **P1 is stated and untested.** It remains falsifiable exactly as
written above — the EU ecodesign case against the LBNL refrigerator baseline is still the obvious
first test, and it has not been run here. The RAC pair is retained in §3 as two tabulated rows,
not as a paired measurement.

**Prediction P2 (which class moves).** Of the classes above, the one whose `β` *should* shift under
a durability intervention is a `β ≥ 2` class, not a `β ≈ 1` one — a repair right cannot make a
memoryless process memoryful. So the sharpest single test is: **passenger cars in a country with a
scrappage-incentive change should move `β`, and boilers under a warranty change should not.**

## 6. What it does not settle · §Honesty

**(a) These fits are from surveys of *possession*, not records of *failure*.** Every LBNL row is a
least-squares reconciliation of household-survey stock-by-age (RECS, AHS) against manufacturer
shipments; every Held row is inferred from registration stock by vintage. Nobody measured a failure.
The random variable is **time from purchase to leaving the household**, which pools wear-out failure
with obsolescence, resale, gift, theft, export and moving house. Held say so outright: cars leave
"either for foreign markets (exports of used cars) or for being dismantled", and "cars are typically
sold on long before they fail irreparably." **So a car's `β = 3.6` is not evidence that a car wears
out on a Weibull-3.6 schedule — it is evidence that the composite economic-plus-administrative exit
process has that shape.** This is the metaphor objection [[G30-weibull-product-lifespan]] is built
around, and it is not answered here; it is bounded. What survives it is the *comparative* claim: on
one instrument, one method, one country, gas boilers and gas furnaces differ by `β = 1.00` vs
`2.22`, and that difference is about the exit process, whatever it is made of.

**(b) Discard ≠ failure is not a small correction — it can flip the reading.** A class could have a
wear-out failure law (`β_fail > 1`) hidden inside a memoryless discard law (`β_discard ≈ 1`) if
obsolescence removes units faster than they wear. The `β` this note tabulates is always
`β_discard`. **No row here is a `β_fail`.** C18's enzyme and Li-ion rows *are* failure laws. So the
axis in §3 is honest only if it is read as "time-to-exit-of-service", and the top and bottom of the
table are measuring exit for different reasons. That is a real seam through the middle of the table
and it is the main thing a critic should attack.

**(c) Censoring and truncation.** Survey-reconciliation fits are dominated by units *still in
service* — right-censored by construction, and the fit is not a likelihood over censored data but a
least-squares match of stock counts by bin. LBNL's own delay parameter `θ` is where warranty
replacement is deliberately excluded ("appliances replaced under warranty are included in the
manufacturer shipments … so by allowing the delay parameter in the fits to be zero, the physical
lifetime of each appliance is consistently chosen"). Two rows (refrigerator `θ = 8.87`, freezer
`θ = 6.46`) carry a *large* delay, which absorbs early exits and therefore **inflates `β`** relative
to a delay-free fit — those two `β` are not directly comparable with the `θ = 0` rows.

**(d) Standard errors are wide where it matters most.** Heat pump `β = 1.525 ± 0.525` and freezer
`β = 1.885 ± 0.730` do not exclude `β = 1`. Only the boiler (`1.000 ± 0.148`), the water heaters and
the RACs have errors tight enough to place them in a band with confidence. Held's Table 1 β values
are printed without uncertainties in the text available, so **no error bar is claimed for any car
row.**

**(e) Some classes are not Weibull at all.** *Lifespan of Commodities* Part I/II fit lognormals to
some commodity classes. A lognormal has no `β` and cannot be forced onto this axis. Those classes
are absent from §3 not because they were checked and excluded, but because they were **never
obtained** (§2D) — the axis in §3 is `n = 21` of a much larger published population.

**(f) The intersection denominator is missing.** The G30 zero rests on a union-floor `E = 102`,
which flatters the claim by construction; the concept-scoped `N_universe` could not be fetched
(OpenAlex daily budget exhausted, §2 of [[G30-weibull-product-lifespan]]). The load-bearing
statistic remains the shared-B control ratio, which is denominator-free.

**(g) Li-ion's `β = 12.7` is still `VERIFIED-via-search`.** It anchors the top of the axis and has
never been fetch-verified. If it is wrong, the "everything is below Li-ion" framing goes with it;
the two-band structure among products does not.

See [[G30-weibull-product-lifespan]], [[C18-durability-axis]], [[G3-cycle-life]],
[[citation-intersection]].

## Corrections 2026-09-05 (audit 06)

`audits/06-math-rounds3-6.md` item 15. No fitted value changed; a claimed *measurement* is
withdrawn.

**§5's "natural experiment" is withdrawn.** The note read: "**P1 already has one
natural-experiment measurement, and it passes.** … the mean fell 14.75 → 11.27 yr (−24%) while β
moved 1.067 → 1.08, i.e. by 0.01, well inside the ±0.06–0.09 standard errors." It now reads that
**P1 is stated and untested**. Three independent defects, any one fatal:

| # | defect | where the note already said so |
|---|---|---|
| 1 | The pre-2000 row carries `θ = 8.0`, the post-2000 row `θ = 0`; a large `θ` absorbs early exits and inflates `β` | §6(c), verbatim: "those two `β` are not directly comparable with the `θ = 0` rows" |
| 2 | The quoted post-2000 mean 11.27 yr is the one figure §3's consistency check rejects; the row's own `(β = 1.08, η = 10.27, θ = 0)` give **9.97 yr**, so the shift is **−32%**, not −24% | §3, "Table 10's scale parameter is internally inconsistent with its own median" |
| 3 | No intervention occurred — two survey vintages fitted separately, no treatment, no control, no identified cause | — (this one was simply not noticed) |

Defect 1 is the sharpest: §5 was offering as its evidence exactly the comparison §6(c) forbids,
one section later in the same note. Defect 2 means the note quoted, as its measured effect, a
number it had itself flagged as unreliable eight paragraphs earlier.

**What is unchanged.** Every `β`, `η`, `θ` and `H` in §3 stands; the ten-of-eleven internal
consistency check stands; P1 and P2 stand **as predictions**, falsifiable exactly as written, with
the EU ecodesign case against the LBNL refrigerator baseline still the obvious first test. The RAC
pre-2000 and post-2000 rows remain in §3 as two tabulated fits — they are simply not a pair.

**Script.** `vault/_scripts/c27_beta.py` gains section `[4]`, which prints both mean shifts
(−24% from the published mean, −32% from the row's own parameters), the `θ` mismatch, and the
verdict `P1 is STATED AND UNTESTED`, so the withdrawn claim cannot be re-imported from the
numbers.
