# Scout: circularity and industrial ecology

Scouting pass, **2026-09-05**. Read-only on `vault/`. All counts are OpenAlex
`api.openalex.org`, polite pool `mailto=deciduusleaf@gmail.com`; all DOIs verified against
Crossref `api.crossref.org/works/<doi>?mailto=...` the same day. Every number below names its
endpoint. Nothing here is a vault standing; these are leads at the strength stated.

## Summary (5 lines)

- **Twelve pairs tested by citer-set intersection; ten returned 0, one returned 1, one returned 1.** Against three positive controls run on the same instrument the same day (**89**, **101**, **15** co-citers), the separation is as clean as the vault's best cases — reliability/maintenance mathematics and industrial-ecology stock-and-lifetime modelling are two literatures that share objects and do not share citations.
- **The single strongest candidate is C18's Weibull β ↔ product-lifespan distributions.** Weibull 1951 × Oguchi 2015 = **0** (E_floor = 102), Weibull 1951 × Murakami 2010 = **1**, while the industrial-ecology control on the *same B anchor* (Müller 2006 × Oguchi 2015) = **15**. The product-lifespan field fits Weibulls and never touches reliability's β-classification; C18 already owns the axis and the battery-side numbers.
- **The second is C6's `Ha = k_r/k_d` ↔ remanufacturing-vs-discard flows**, and its honesty is that it is *not* a zero: Barlow & Hunter 1960 × Guide 2000 = **1**, a 2017 warranty-plus-preventive-maintenance paper on remanufactured products. One real bridge, denominator-invariant isolation ≈ **100×** against the reliability-internal control. That is a narrow gap, correctly described.
- **Three of the five candidates the scope audit named are weaker than it assumed.** Hill numbers ↔ material-circularity indicators and Kirkwood ↔ maintenance budgets both fail the same-object test on inspection (mass-fraction ≠ effective-number-of-types; no reproduction term in an asset budget) — they are metaphor risks, not gaps. Cox 1972 × Oguchi is a G25-shaped trap: its concept-scoped `N` will be void because Cox's citer set fits inside no nameable concept.
- **The concept-scoped denominators were not obtained.** OpenAlex returned HTTP 429 on every `concepts.id:` count from 16:00 onward (IP-level, sustained across ~25 min of backoff). Every `E` below is therefore the **union floor only**, which flatters gap claims by construction. Per `citation-intersection`, no `O/E` here is quotable until a second denominator is fetched; the load-bearing statistic is the **control ratio**, which is denominator-free and is quoted.

## Ranked candidates

`E` = union floor `|A|·|B|/(|A|+|B|−O)`. Scoped `N` **not obtained** (429) — see Summary line 5.
"Informative?" asks only whether `E > 1` at the floor, which is a necessary and *not* sufficient
condition.

| # | candidate (A ↔ B) | anchors (DOIs, Crossref-verified 2026-09-05) | N_A / N_B / ∩ | E (floor / scoped) | informative? | bridge found? | cost to close | extends |
|---|---|---|---|---|---|---|---|---|
| **1** | Weibull shape β, reliability ↔ product-lifespan distribution, industrial ecology | `10.1115/1.4010337` (Weibull 1951) ↔ `10.1021/es505245q` (Oguchi et al. 2015) | 11,512 / 103 / **0** | 102.1 / — | yes at floor | no | 4–6 h desk | C18, G3 · `extends-to: circularity` |
| **2** | Healing Damköhler `Ha = k_r/k_d` ↔ remanufacturing throughput vs discard throughput | `10.1287/opre.8.1.90` (Barlow & Hunter 1960) ↔ `10.1016/s0272-6963(00)00034-6` (Guide 2000) | 1,368 / 1,093 / **1** | 607.8 / — | yes at floor | **yes, 1** | 3–5 h desk | C6, C1 · `extends-to: circularity` |
| **3** | Availability `A = MTBF/(MTBF+MTTR)` ↔ in-use stock utilisation intensity | `10.1016/0951-8320(95)00076-3` (Dekker 1996) ↔ `10.1080/21681015.2016.1172124` (Bocken et al. 2016) | 966 / 3,860 / **0** | 772.6 / — | yes at floor | no | 2–3 h desk | C1, C6 · `extends-to: circularity` |
| **4** | Optimal age-replacement policy ↔ LCA-optimal product replacement timing | `10.1287/opre.8.1.90` (Barlow & Hunter 1960) ↔ `10.1021/es0345221` (Kim, Keoleian & Horie 2003) | 1,368 / 101 / **0** | 94.1 / — | yes at floor | no | 3–4 h desk | C18, C1 · `extends-to: sustainability` |
| **5** | Remaining-useful-life estimation ↔ dynamic-MFA residence time / stock outflow | `10.1016/j.ejor.2010.11.018` (Si et al. 2011) ↔ `10.1021/es403506a` (Müller et al. 2014) | 2,098 / 517 / **0** | 414.8 / — | yes at floor | no | 5–8 h desk | C18 · `extends-to: industrial-ecology` |
| **6** | Gamma-process degradation modelling ↔ dynamic-MFA stock degradation | `10.1016/j.ress.2007.03.019` (van Noortwijk 2009) ↔ `10.1021/es403506a` (Müller et al. 2014) | 1,337 / 517 / **0** | 372.8 / — | yes at floor | no | 5–8 h desk | C18, C10 · `extends-to: industrial-ecology` |
| **7** | Availability / repairability ↔ global in-use material stock | `10.1016/0951-8320(95)00076-3` (Dekker 1996) ↔ `10.1073/pnas.1613773114` (Krausmann et al. 2017) | 966 / 700 / **0** | 405.8 / — | yes at floor | no | 4 h desk | C1 · `extends-to: circularity` |
| **8** | Weibull β ↔ design-for-product-life-extension | `10.1115/1.4010337` (Weibull 1951) ↔ `10.1016/j.jclepro.2014.01.028` (Bakker et al. 2014) | 11,512 / 717 / **0** | 674.9 / — | yes at floor | no | folds into #1 | C18 · `extends-to: circularity` |
| **9** | Reliability theory of ageing ↔ deteriorating-infrastructure life-cycle models | `10.1006/jtbi.2001.2430` (Gavrilov & Gavrilova 2001) ↔ `10.1002/pse.180` (Frangopol et al. 2004) | 633 / 387 / **0** | 240.2 / — | yes at floor | no | 6 h desk | C18, one-way-borrowing · `extends-to: conservation` |
| 10 | Kirkwood disposable soma ↔ infrastructure maintenance-budget allocation | `10.1038/270301a0` (Kirkwood 1977) ↔ `10.1002/pse.180` (Frangopol et al. 2004) | 1,976 / 387 / **0** | 323.6 / — | yes at floor | no | 8 h+ | C6/C10 · **metaphor risk high** |
| 11 | Kirkwood disposable soma ↔ remanufacturing | `10.1038/270301a0` ↔ `10.1016/s0272-6963(00)00034-6` | 1,976 / 1,093 / **0** | 703.7 / — | yes at floor | no | 8 h+ | **metaphor risk high** |
| 12 | Hill numbers ↔ material-circularity indicators | `10.1111/j.2006.0030-1299.14714.x` (Jost 2006) ↔ `10.1016/j.jclepro.2018.10.014` (Saidani et al. 2019); also ↔ `10.1111/jiec.12552` (Linder et al. 2017) | 4,718 / 1,064 / **0**; 4,718 / 472 / **0** | 868.2; 429.0 / — | yes at floor | no | — | G6 · **fails same-object test** |
| 13 | Ecosystem multifunctionality metric ↔ CE indicator taxonomy | `10.1111/2041-210X.12143` (Byrnes et al. 2014) ↔ `10.1016/j.jclepro.2018.10.014` (Saidani et al. 2019) | 926 / 1,064 / **0** | 495.1 / — | yes at floor | no | — | G6 · **fails same-object test** |
| 14 | Cox proportional-hazards ↔ product-discard hazard | `10.1111/j.2517-6161.1972.tb00899.x` (Cox 1972) ↔ `10.1021/es505245q` (Oguchi 2015) | 39,688 / 103 / **0** | 102.7 / — | **no — G25 trap** | no | — | **denominator void by construction** |

### The positive controls, run on the same instrument the same day

These are what make the zeros above mean anything, and two of them are new to the project.

| Control | anchors | \|A\| / \|B\| / O | E (floor) | **O/E** | reading |
|---|---|---|---|---|---|
| Reliability-internal | Dekker 1996 × Barlow & Hunter 1960 | 966 / 1,368 / **89** | 588.7 | **0.151** | closed |
| Maintenance × infrastructure | van Noortwijk 2009 × Frangopol 2004 | 1,337 / 387 / **101** | 318.8 | **0.317** | closed |
| Industrial-ecology-internal | Müller 2006 × Oguchi 2015 | 511 / 103 / **15** | 87.9 | **0.171** | closed |

Endpoint for all rows above:
`https://api.openalex.org/works?filter=cites:<W_A>,cites:<W_B>&per-page=5&mailto=deciduusleaf@gmail.com`,
reading `meta.count`; per-side counts from `https://api.openalex.org/works/<W_id>` field
`cited_by_count`. Fetched **2026-09-05**.

**The control-ratio statistic**, which is invariant under `N` and is the number these candidates
should rest on:

| shared anchor | gap | control | `(O_gap/|B_gap|) / (O_ctl/|B_ctl|)` |
|---|---|---|---|
| Barlow & Hunter 1960 | × Guide 2000 = 1/1,093 | × Dekker 1996 = 89/966 | isolation **≈ 100×** |
| Barlow & Hunter 1960 | × Kim 2003 = 0/101 | × Dekker 1996 = 89/966 | isolation **∞** (O = 0) |
| van Noortwijk 2009 | × Müller 2014 = 0/517 | × Frangopol 2004 = 101/387 | isolation **∞** (O = 0) |
| Oguchi 2015 (shared **B**) | Weibull 1951 = 0/11,512 | Müller 2006 = 15/511 | isolation **∞** (O = 0) |

The last row is the best-shaped comparison in this scout: it holds the *industrial-ecology* side
fixed and swaps only the mathematics-side anchor, so it cannot be explained by Oguchi 2015 being
a small or obscure paper.

## Per-candidate detail

Only the candidates that survive scrutiny get full treatment; the ones that fail get the reason
they fail, which is the more useful output.

---

### 1. Weibull shape β (C18) ↔ product-lifespan distributions (Oguchi & Daigo and successors)

**1. Anchors.** *A:* W. Weibull, "A Statistical Distribution Function of Wide Applicability",
*J. Appl. Mech.* 18:293–297 (1951), DOI `10.1115/1.4010337` — Crossref title and year verified
2026-09-05, Crossref `is-referenced-by-count` = 9,513; OpenAlex `W2727420541`,
`cited_by_count` = 11,512. *B:* Oguchi, Daigo, Sugimoto & Kanari, "Regional and Longitudinal
Estimation of Product Lifespan Distribution: A Case Study for Automobiles and a Simplified
Estimation Method", *Environ. Sci. Technol.* 49:1738–1745 (2015), DOI `10.1021/es505245q` —
Crossref verified, `is-referenced-by-count` = 98; OpenAlex `W2320647648`,
`cited_by_count` = 103. Secondary B anchors: Murakami, Oguchi, Tasaki, Daigo & Hashimoto,
"Lifespan of Commodities, Part I", *J. Ind. Ecol.* 14:598–612 (2010),
DOI `10.1111/j.1530-9290.2010.00250.x` (OpenAlex `W2603909978`, 185); Part II,
DOI `10.1111/j.1530-9290.2010.00251.x` (`W2171683314`, 144).

**2. Same object, two sentences.** Both fields fit a two-parameter Weibull to the *same random
variable* — time (or cycles) from entry-into-service to exit-from-service of a population of
identical artefacts — and both report the shape parameter of that fit. Reliability reads β as a
statement about the hazard function (β = 1 memoryless, β > 1 wear-out) and uses it to choose a
maintenance policy; industrial ecology reads the same fitted β as an input to a stock-driven
outflow model and never interprets it.

**Strongest metaphor objection** (`failure-modes`): *discard is not failure*. A product-lifespan
distribution pools wear-out failure with obsolescence, resale, theft, export and hoarding, so the
fitted β is a mixture parameter over exit modes, not a hazard shape for a degradation process.
The reliability β and the lifespan β would then be the same *arithmetic* on different objects —
which is exactly the error C18 itself warns about when it says a single `N_fail` "hides two
failure laws". This objection is real and must be answered before the gap is opened, not after.
It is also the reason the candidate is interesting: β ≈ 1 in a product class *is* the signature
of exit-by-random-loss rather than exit-by-wear-out, and no one has said so in these words.

**3. Intersection.**
`https://api.openalex.org/works?filter=cites:W2727420541,cites:W2320647648&per-page=5&mailto=...`
→ `meta.count = 0`. Fetched 2026-09-05.
N_A = 11,512, N_B = 103, |A∩B| = **0**. Union floor `N = 11,615`, **E = 102.1**.
Second measurement on the other B anchor: `cites:W2727420541,cites:W2603909978` →
`meta.count = 1` (N_B = 185; union floor 11,696, E = 182.1, O/E = 0.0055). The single hit is
inspected below. Third: `cites:W2727420541,cites:W2005386442` (Bakker 2014) → **0**.
**Concept-scoped `N` not obtained** — `concepts.id:C173291955|C70401792` (Weibull distribution ∪
Industrial ecology) returned HTTP 429 on every attempt after ~16:00 on 2026-09-05, sustained
across 8 retries with 15–120 s backoff. **The `E = 102.1` is therefore a floor and nothing
else**, and by `citation-intersection`'s own rule the `O/E` is not quotable until a second
denominator exists. Whether the zero is informative rests instead on the shared-B control.
*Is E > 1?* Yes at the floor (102). *Is that sufficient?* No, and the note should say so.

**4. Inspection.** Only one hit exists across the three pairings: *"Agent-based model for
assessment of multiple circular economy strategies: Quantifying product-service system…"*,
*Resources, Conservation and Recycling*, 2023. **This is not a bridge in the sense required.** It
co-cites Weibull and Murakami as two separate methodological ingredients of a simulation; it does
not put a reliability β and a lifespan β on one axis, and it does not read β as a failure law.
It is the single work that would have to be read in full before the gap is opened, and it is the
one place the candidate could die.

**5. What would close it.** The missing object is **a table of fitted Weibull β by product class,
labelled by exit mode, on the same axis as C18's battery and enzyme β values** — and the
prediction that follows: product classes exiting by wear-out sit at β > 1 while classes exiting by
obsolescence sit at β ≈ 1, so a "designed-for-circularity" intervention that extends physical life
without addressing obsolescence moves the mean and *not* the shape. Computed from: the lifespan
distribution parameters already published in Oguchi 2015 (automobiles, regional and longitudinal)
and Murakami 2010 Parts I–II (multiple commodity classes, Weibull and lognormal fits given), plus
C18's existing battery-side β = 12.7 (NCR18650GA) and the enzyme-side β = 1 argument.
**4–6 hours desk work, no data access needed**, because both sides' parameters are printed in
open or obtainable papers. Watch the trap: Murakami 2010 fits some classes lognormal, not Weibull,
and a lognormal cannot be forced onto the β axis without saying so.

**6. Extends.** **[[C18-durability-axis]]** directly — it is the same axis with a third population
on it — and **[[G3-cycle-life]]**, whose "the shared coordinate is β" claim currently has two
domains and would gain a third. `extends-to: circularity`.

---

### 2. Healing Damköhler `Ha = k_r/k_d` (C6) ↔ repair-vs-replace / remanufacturing flows

**1. Anchors.** *A:* Barlow & Hunter, "Optimum Preventive Maintenance Policies",
*Operations Research* 8:90–100 (1960), DOI `10.1287/opre.8.1.90` — Crossref verified
2026-09-05, `is-referenced-by-count` = 1,133; OpenAlex `W2109281751`, `cited_by_count` = 1,368.
*B:* Guide, "Production planning and control for remanufacturing: industry practice and research
needs", *J. Operations Management* 18:467–483 (2000), DOI `10.1016/s0272-6963(00)00034-6` —
Crossref verified, `is-referenced-by-count` = 842; OpenAlex `W2029123070`,
`cited_by_count` = 1,093. (Note: the DOI with terminal `-7` **404s** on both Crossref and
OpenAlex; the correct suffix is `-6`.)

**2. Same object.** `Ha = k_r/k_d` is the ratio of a restoration rate to a degradation rate on one
clock, and the remanufacturing literature computes exactly those two rates for a product fleet —
cores returned and restored per unit time over units failing or discarded per unit time — while
never forming the dimensionless ratio or noticing that it is the reciprocal of an offered load.
C6 has already shown `Ha` collapses to `A = Ha/(1+Ha)`, the Erlang-B one-server complement, so a
fleet's remanufacturing-to-discard flow ratio *is* a fleet availability, computed and reported as
a percentage recovery rate instead.

**Strongest metaphor objection.** Remanufacturing flows are **cohort** flows over a supply chain
with lead times and inventory, not **rates on one item's clock**; a returned core is not the same
unit restored, so `k_r` and `k_d` are not acting on a common population and the ratio is a
throughput balance, not a hazard ratio. C6's own §on conditions makes this fatal if true: the
`Ha → A` reduction needs the four stated conditions, and "same unit, up or down" is one of them.
The honest form of the candidate is therefore about the *population functional fraction* column of
C1's two-object table, not the *unit availability* column — and C1 already warns that mixing those
two columns was its headline defect.

**3. Intersection.**
`https://api.openalex.org/works?filter=cites:W2109281751,cites:W2029123070&per-page=5&mailto=...`
→ `meta.count = 1`. Fetched 2026-09-05. N_A = 1,368, N_B = 1,093, |A∩B| = **1**.
Union floor `N = 2,460`, **E = 607.8**, `O/E = 0.00165`. Reliability-internal control on the same
A anchor: `cites:W2109281751,cites:W2097279435` (Dekker 1996) → **89**, `O/E = 0.151` at its own
floor. **Control ratio = (1/1,093)/(89/966) = 0.000915/0.0921 = 99.4×**, denominator-invariant.
Concept-scoped `N` (`C2777448596|C2778738845`, Circular economy ∪ Remanufacturing, from 2000)
**not obtained — HTTP 429**. `E > 1` at the floor by three orders of magnitude, and the control
ratio does not depend on that.

**4. Inspection.** The one hit is *"Warranty cost analysis with preventive maintenance strategy
for remanufactured products in reverse supply chain"* (2017; OpenAlex reports no source for the
record, which is itself worth checking before citing it). **This is a real bridge** — it is
maintenance-policy mathematics applied to remanufactured product fleets, which is the object. What
it is not, on the title alone, is a *dimensionless rate ratio* or a statement that the recovery
fraction is an availability. **It must be read in full before this candidate is opened**; if it
forms the ratio, the candidate dies, and if it optimises warranty cost without ever forming it,
the candidate is a genuine narrow gap of exactly the C6 shape. This is a one-paper decision and it
is cheap.

**5. What would close it.** The missing object is **the first `Ha` values for a repairable product
fleet**: `Ha = (remanufacture + repair throughput)/(failure + discard throughput)` for one product
class, with the four C6 conditions checked explicitly and the resulting `A = Ha/(1+Ha)` compared
against the fleet's published in-service fraction. Computed from published core-return rates and
remanufacturing volumes (automotive parts and heavy equipment are the best-documented classes) and
published failure/discard rates for the same class. **3–5 hours** once the class is chosen, plus
the one full-text read above. The deliverable that makes it non-trivial is the *discrepancy*: if
`Ha/(1+Ha)` does not match the observed in-service fraction, the gap between them measures how
much of the fleet is down for reasons that are neither failure nor repair — which is the
utilisation-vs-availability distinction candidate 3 is about.

**6. Extends.** **[[C6-damage-healing-ratio]]** (a fourth system on the `Ha` axis, and the first
non-material one) and **[[C1-availability-living-tissue]]** (a product row beside cortical bone).
`extends-to: circularity`.

---

### 3. Availability `A` (C1) ↔ in-use stock utilisation intensity

**1. Anchors.** *A:* Dekker, "Applications of maintenance optimization models: a review and
analysis", *Reliab. Eng. Syst. Saf.* 51:229–240 (1996), DOI `10.1016/0951-8320(95)00076-3` —
Crossref verified 2026-09-05, `is-referenced-by-count` = 669; OpenAlex `W2097279435`,
`cited_by_count` = 966. *B:* Bocken, de Pauw, Bakker & van der Grinten, "Product design and
business model strategies for a circular economy", *J. Ind. Prod. Eng.* 33:308–320 (2016),
DOI `10.1080/21681015.2016.1172124` — Crossref verified, `is-referenced-by-count` = 2,298;
OpenAlex `W2342540942`, `cited_by_count` = 3,860.

**2. Same object.** Both compute a *fraction of elapsed time a unit is delivering function*, from
a partition of that unit's timeline; reliability calls the partition up/down and the fraction
availability, industrial ecology calls it in-use/idle and the fraction utilisation intensity.
Slowing-loops strategies are explicitly attempts to raise that fraction, and the arithmetic is
the same arithmetic C1 runs on photosystem II and on the US distribution grid.

**Strongest metaphor objection**, and it is strong: **idle is not down**. A parked car is
available and unused; a failed car is unavailable. The two fractions partition the same timeline
differently, so `A` and utilisation intensity are two *different* fractions and equating them is
precisely the "unit availability vs population functional fraction" conflation C1 lists as its own
worst historical defect. The defensible form of the candidate is not "these are the same number"
but "**these are two of the three fractions of one three-way partition (in-use / idle-but-up /
down), and neither field computes all three**" — which is a weaker and much more honest claim.

**3. Intersection.** `cites:W2097279435,cites:W2342540942` → `meta.count = 0`, fetched
2026-09-05. N_A = 966, N_B = 3,860, |A∩B| = **0**. Union floor `N = 4,826`, **E = 772.6**.
Second pairing, `cites:W2097279435,cites:W2586080738` (Krausmann et al. 2017, global in-use
stocks, `10.1073/pnas.1613773114`) → **0**; N_A = 966, N_B = 700, floor `N = 1,666`, E = 405.8.
Scoped `N` (`C2777448596|C70401792` from 1996) **not obtained — HTTP 429**. `E > 1` at the floor
on both pairings. Control ratio against the reliability-internal control (shared A = Dekker):
`(0/3,860)/(89/1,368)` = **0** — isolation unbounded.

**4. Inspection.** No hits to inspect on either pairing. Nothing to report, which is also the
weakness: an unexamined zero.

**5. What would close it.** The missing object is **the three-way time partition computed for one
product class and one tissue on the same figure**: in-use fraction, idle-but-serviceable fraction,
and down-for-repair fraction, so that C1's `A` and the CE literature's utilisation intensity are
visibly two different slices of one pie. Computed from published passenger-car utilisation figures
(the ~4–5% in-use fraction that the sharing-economy literature quotes) plus published fleet
availability/downtime statistics for the same vehicle class, against C1's existing PSII and bone
rows. **2–3 hours.** The claim it would support is narrow but genuinely new: *living tissue and
engineered fleets differ far more in the idle fraction than in the down fraction*, which is a
statement about what circularity has to attack.

**6. Extends.** **[[C1-availability-living-tissue]]** (adds the third column its two-object table
implies but does not have) and **[[C6-damage-healing-ratio]]**. `extends-to: circularity`.

---

### 4. Optimal age-replacement policy ↔ LCA-optimal replacement timing

*A:* Barlow & Hunter 1960, `10.1287/opre.8.1.90` (as above, 1,368). *B:* Kim, Keoleian & Horie,
"Life Cycle Optimization of Automobile Replacement: Model and Application", *Environ. Sci.
Technol.* 37:5407–5413 (2003), DOI `10.1021/es0345221` — Crossref verified 2026-09-05,
`is-referenced-by-count` = 79; OpenAlex `W2027467198`, `cited_by_count` = 101.

**Same object:** both solve for the replacement age that minimises a cost rate over an infinite
horizon of a deteriorating unit — reliability minimises expected cost per unit time under a
failure distribution, LCA minimises life-cycle energy or emissions per km under a degradation and
technology-improvement trajectory. **Metaphor objection:** the LCA problem's objective has a term
reliability's has not — the *improving replacement*, i.e. a new unit is better than the old one
was when new — so it is a technology-vintage problem, not a renewal-reward problem, and the two
optima have different structure. This is a genuine difference and it is the interesting part.

`cites:W2109281751,cites:W2027467198` → **0** (2026-09-05). Floor `N = 1,469`, **E = 94.1**.
Scoped `N` not obtained. Control ratio against Dekker 1996: isolation unbounded. No hits to
inspect. **To close:** state the renewal-reward problem with a vintage-improvement term and show
the classical age-replacement optimum is its zero-improvement limit; then compute the optimal
replacement age for one vehicle class under both objectives and report the gap in years.
**3–4 hours desk.** Extends **[[C18-durability-axis]]** and **[[C1-availability-living-tissue]]**;
`extends-to: sustainability`.

---

### 5–6. RUL estimation and gamma-process degradation ↔ dynamic material flow analysis

*A₁:* Si, Wang, Hu & Zhou, "Remaining useful life estimation — A review on the statistical data
driven approaches", *Eur. J. Oper. Res.* 213:1–14 (2011), DOI `10.1016/j.ejor.2010.11.018` —
Crossref verified, 1,879; OpenAlex `W2055873761`, 2,098. *A₂:* van Noortwijk, "A survey of the
application of gamma processes in maintenance", *Reliab. Eng. Syst. Saf.* 94:2–21 (2009),
DOI `10.1016/j.ress.2007.03.019` — Crossref verified; OpenAlex `W2147664181`, 1,337.
*B:* Müller, Hilty, Widmer, Schluep & Faulstich, "Modeling Metal Stocks and Flows: A Review of
Dynamic Material Flow Analysis Methods", *Environ. Sci. Technol.* 48:2102–2113 (2014),
DOI `10.1021/es403506a` — Crossref verified; OpenAlex `W2072838135`, 517. Secondary:
Müller, "Stock dynamics for forecasting material flows", *Ecol. Econ.* 59:142–156 (2006),
DOI `10.1016/j.ecolecon.2005.09.025`; OpenAlex `W2061335538`, 511.

**Same object:** a stock-driven dynamic MFA propagates an inflow cohort through a residence-time
distribution to predict outflow — which is a renewal equation on a lifetime distribution, the same
equation prognostics solves when it predicts remaining useful life from a degradation state.
**Metaphor objection:** MFA works on *aggregate mass* with no observed per-unit state, while RUL is
defined by conditioning on a measured degradation signal for one unit; without the conditioning
there is no "remaining useful life", only an unconditional residual-lifetime expectation. That is a
real difference in the object, and it caps the candidate at "MFA is doing unconditional renewal
theory and does not know it", which is a smaller claim.

`cites:W2055873761,cites:W2072838135` → **0**; floor `N = 2,615`, **E = 414.8**.
`cites:W2055873761,cites:W2061335538` → **0**; floor `N = 2,609`, **E = 410.9**.
`cites:W2147664181,cites:W2072838135` → **0**; floor `N = 1,854`, **E = 372.8**.
Control on shared A₂: van Noortwijk × Frangopol 2004 = **101**, `O/E = 0.317` at floor — so the
gamma-process literature *is* joined to civil infrastructure and *is not* joined to material-flow
analysis, one anchor apart. That is the sharpest structural result in this scout after candidate 1.
All fetched 2026-09-05; scoped `N` not obtained. No hits to inspect.
**To close:** write the MFA outflow convolution and the renewal-theoretic residual-lifetime
expression side by side, show they are the same integral, and compute residual lifetime of an
existing in-use stock two ways from one published dataset. **5–8 hours.** Extends
**[[C18-durability-axis]]** and **[[C10-healing-curve-fit]]**; `extends-to: industrial-ecology`.

---

### 7. Availability/repairability ↔ global in-use material stock

Dekker 1996 × Krausmann et al. 2017 (`10.1073/pnas.1613773114`, Crossref verified; OpenAlex
`W2586080738`, 700) → **0**; floor `N = 1,666`, **E = 405.8**. Fetched 2026-09-05. Folded into
candidate 3: it is the same claim measured against a stock-accounting rather than a design anchor,
and it is reported here only because it is a second independent zero on the same side. `4 h`.
Extends **[[C1-availability-living-tissue]]**; `extends-to: circularity`.

---

### 8. Weibull β ↔ design for product life extension

Weibull 1951 × Bakker, Wang, Huisman & den Hollander, "Products that go round: exploring product
life extension through design", *J. Clean. Prod.* 69:10–16 (2014),
DOI `10.1016/j.jclepro.2014.01.028` (Crossref verified, 623; OpenAlex `W2005386442`, 717) →
**0**; floor `N = 12,229`, **E = 674.9**. Fetched 2026-09-05. **This is the same candidate as #1
measured on the design-side rather than the measurement-side anchor**, and it should be reported
inside #1 rather than opened separately — a separate note would double-count one absence, which is
the error `positive-controls` flags when it says the original table mixed non-comparable
quantities. `extends-to: circularity`.

---

### 9. Reliability theory of ageing ↔ deteriorating-infrastructure models

Gavrilov & Gavrilova, "The Reliability Theory of Aging and Longevity", *J. Theor. Biol.*
213:527–545 (2001), DOI `10.1006/jtbi.2001.2430` (Crossref verified, 371; OpenAlex `W2001082461`,
633) × Frangopol, Kallen & van Noortwijk, "Probabilistic models for life-cycle performance of
deteriorating structures: review and future directions", *Prog. Struct. Eng. Mater.* 6:197–212
(2004), DOI `10.1002/pse.180` (Crossref verified, 299; OpenAlex `W1966267801`, 387) → **0**;
floor `N = 1,020`, **E = 240.2**. Fetched 2026-09-05.

**Why this one is worth keeping despite ranking ninth.** It is a direct, cheap extension of
`[[one-way-borrowing]]`, whose existing specimen is exactly this pair of fields: of 633 works
citing the reliability theory of ageing, 6 are reliability engineering. The infrastructure
deterioration literature is a *third* corner of the same triangle and has no traffic with either.
**To close:** re-run the one-way-borrowing classification with infrastructure as the third node and
report the 3×3 traffic matrix. **6 hours.** Extends **[[C18-durability-axis]]** and
`[[one-way-borrowing]]`; `extends-to: conservation`.

---

### 10–11. Kirkwood disposable soma ↔ maintenance budgets and remanufacturing — **do not open**

Kirkwood, "Evolution of ageing", *Nature* 270:301–304 (1977), DOI `10.1038/270301a0` (Crossref
verified, 1,774; OpenAlex `W1993091967`, 1,976) × Frangopol 2004 → **0** (floor `N = 2,363`,
E = 323.6); × Guide 2000 → **0** (floor `N = 3,069`, E = 703.7). Fetched 2026-09-05.

**The zeros are real and the gap is not.** Disposable soma is an *evolutionary optimality* argument:
the allocation is optimal with respect to inclusive fitness, and the whole force of the theorem is
that somatic maintenance is under-provided *because* the soma is discarded after reproduction.
An infrastructure maintenance budget has no reproduction term, no fitness objective, and no
germ-line, so the shared structure is "there is a finite budget split between two uses" — which is
every constrained-optimisation problem ever written. Under `failure-modes`' own mechanism
(anchoring on the originating field's term) this is a **word-level** crossing at best, and the
project already has one entry, G6, that is honestly graded `crosses: word`. Opening this as a gap
would add a second and weaker one. **Recommendation: record as a checked-and-rejected candidate,
not as a gap.** The salvageable residue is C10's *depletion parameter* — a finite repair budget
that empties — which is a mathematical object, not a metaphor, and which the asset-management
literature does have in the form of deferred-maintenance backlogs.

---

### 12–13. Hill numbers ↔ circularity indicators — **do not open**

Jost, "Entropy and diversity", *Oikos* 113:363–375 (2006),
DOI `10.1111/j.2006.0030-1299.14714.x` (Crossref verified, 4,081; OpenAlex `W2120474334`, 4,718)
× Saidani, Yannou, Leroy, Cluzel & Kendall, "A taxonomy of circular economy indicators",
*J. Clean. Prod.* 207:542–559 (2019), DOI `10.1016/j.jclepro.2018.10.014` (Crossref verified, 949;
OpenAlex `W2894903066`, 1,064) → **0** (floor `N = 5,782`, E = 868.2). Jost 2006 × Linder,
Sarasini & van Loon, "A Metric for Quantifying Product-Level Circularity", *J. Ind. Ecol.*
21:545–558 (2017), DOI `10.1111/jiec.12552` (Crossref verified, 426; OpenAlex `W2591143445`, 472)
→ **0** (floor `N = 5,190`, E = 429.0). Byrnes et al. 2014
(`10.1111/2041-210X.12143`; OpenAlex `W2117867889`, 926) × Saidani 2019 → **0** (floor
`N = 1,990`, E = 495.1). All fetched 2026-09-05.

**Three clean zeros, and the same-object test still fails.** A Hill number is an *effective number
of types* — the exponential of a Rényi entropy over a proportional abundance vector. A material
circularity indicator is a *mass fraction*: recirculated mass over total mass, sometimes weighted
by a utility ratio. Those are not the same functional on the same object; one counts types, the
other counts mass, and no choice of `q` turns the second into the first. G6's Hill-number claim is
about counting **functions a material serves**, and the CE indicator literature is not counting
functions at all. **Recommendation: rejected as stated.** If a version survives it is the *other*
half of the scope audit's phrasing — Hill numbers applied to **material-stock type diversity**
(how many distinct alloys, polymers, or component types a stock contains, and how evenly), which
*is* an abundance vector and *is* a legitimate Hill-number target. That reformulated candidate was
not tested here and is the single most useful follow-up query in this section.

---

### 14. Cox proportional hazards ↔ product-discard hazard — **do not open, and the reason is instructive**

Cox, "Regression Models and Life-Tables", *JRSS B* 34:187–202 (1972),
DOI `10.1111/j.2517-6161.1972.tb00899.x` (Crossref verified, 36,657; OpenAlex `W3147894994`,
39,688) × Oguchi 2015 → **0**; floor `N = 39,791`, **E = 102.7**. Fetched 2026-09-05.

`E > 1` at the floor, so by the letter of the rule the zero is "informative". **It is not.** This is
the G25 configuration exactly: an anchor with ~40,000 citers spanning all of clinical medicine
cannot be contained in any nameable concept scope, so the concept-scoped `N` will come back smaller
than `|A|` and be **void** — the same failure that voided the Shannon-side denominator in
`[[G25-proofreading-coding]]`. The union floor is then the only available `N`, and a union floor
dominated by one giant citer set gives an `E` that is an artifact of that set's size, not of a
shared universe. **Rule this scout would propose adding to `citation-intersection`: when one side's
citer set exceeds the other's by more than ~100×, the union floor is uninformative and the pair
must be re-anchored on a smaller, field-specific A.** Weibull 1951 (11,512 vs 103, ~110×) sits
right at that boundary, which is why candidate 1 leans on the shared-B control rather than on `E`.

---

## What this scout did not do, stated plainly

- **No concept-scoped `N` was obtained for any candidate.** OpenAlex `concepts.id:` counts
  returned HTTP 429 continuously from mid-session (8 retries, 15–120 s backoff, both raw `|` and
  `%7C` encodings). Every `E` above is a **union floor**, which `citation-intersection` says
  flatters gap claims and must never be quoted alone. The four control-ratio rows are the only
  denominator-free numbers here and are the only ones fit to travel into a note.
- **No hit was read in full.** Two hits exist across twelve pairings and both are named above;
  both are one-paper decisions that could kill their candidate. `citation-intersection` is explicit
  that a count is not a finding until every hit is read.
- **Diachronic check (failure-mode 6) not run.** Weibull 1951's citer window is 75 years wide and
  the industrial-ecology anchors are all post-2000; the pooled zero in candidate 1 has not been
  binned by decade under each decade's own vocabulary. For a citation intersection this matters
  less than for a string query, but it is not zero risk: "lifespan distribution", "product
  lifetime", "residence time" and "sojourn time" are four names for candidate 5's object and only
  one was anchored on.
- **One-provider only.** Everything is OpenAlex. `citation-sources` says two independent providers
  agreeing is the check; OpenCitations was not run, and for anchors under ~10,000 citers it could
  have been for all but Weibull and Cox.

## Recommendation: which two to open first

**Open candidate 1 — Weibull β ↔ product-lifespan distributions — as a gap note.**
It is the only candidate here where (a) the same object survives inspection as literally the same
fitted parameter of the same distribution family, (b) the isolation is measured against a control
that holds the industrial-ecology side fixed (Müller 2006 × Oguchi 2015 = 15 versus Weibull ×
Oguchi = 0, so the zero is not an artifact of Oguchi being small), (c) both sides' numbers are
already printed and the closing computation is 4–6 hours of desk work with no data access, and
(d) it lands directly on **C18**, which the scope audit already ranks first in the whole portfolio
and which currently sits parked. It also converts C18's central asymmetry — *everyone reports the
mean, only some report the distribution* — from a two-domain observation into a three-domain one,
with a policy-relevant discriminator (β ≈ 1 obsolescence versus β > 1 wear-out) that nobody has
stated. **Before opening it, do the two cheap kill-checks:** read the 2023 *RCR* agent-based paper
in full, and re-run the pairing against a fifth product-lifetime anchor to make sure the zero is
not an Oguchi/Murakami-group artifact.

**Open candidate 2 — `Ha` ↔ remanufacturing-vs-discard flows — second, and open it as a *narrowed*
gap from the start.**
Its virtue is exactly that it is not a zero. One genuine bridge exists, the isolation is ≈100× on a
denominator-free statistic, and the object is C6's, which the vault has already built and already
knows the limits of. Opening it as `standing: narrowed` with contact-surface 1 is the honest shape,
and it avoids the failure the project's own audits found — string-protocol gaps failing re-test
more than half the time — because it is not resting on an absence at all. The gating step is one
full-text read, and the deliverable (`Ha` for a product fleet, checked against the fleet's
in-service fraction) is small, checkable and directly on the owner's interests.

**Do not open** candidates 10–14. Kirkwood-to-budgets and Hill-numbers-to-MCI both fail the
same-object test on inspection despite clean zeros, and Cox-to-discard is a denominator artifact.
Recording them as *checked and rejected* is worth more than recording them as gaps: it is four
measured zeros that the project can point to as ones it declined to claim.
