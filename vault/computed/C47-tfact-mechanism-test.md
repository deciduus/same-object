---
name: C47-tfact-mechanism-test
type: computed
exit: computation
extends-to: [sustainability, conservation]
next-step-cost: M
---

# Is `T` a depth label? The C43 mechanism, pre-registered and run on independent sites

> **H1 PARTIAL, H2 FAILS, H3 FAILS.** The depth rule alone predicts only **64.6%** of `tfact`
> values at 800 random CONUS points (**37.7%** at the 114 independent ¹⁰Be sites) against a
> pre-registered ≥ 90% gate, while **84.5% / 92.1%** fall inside the three-column band the USDA
> handbook actually publishes — so `tfact` is depth **plus a renewability group**, not depth. And
> on 114 outcrop sites C43 did not use, **ρ(`tfact`, `P`) = +0.090 (p = 0.34, 95% CI
> [−0.095, 0.269])** — C43's −0.206 lies **outside** that interval. The anti-correlation does not
> replicate here, and it is not slope: the partial ρ controlling `slope_r` is +0.075.

Programme item P-079. Pre-registered in `audits/blind-brief-c47-2026-09-05.md`, sha256
`13a3dad415f32d327eb9666111e0c5268d380cbdd543730ae5e5077cfe6daad6`, hashed before any new site's
`tfact`, restriction depth or erosion rate was fetched. Re-runnable: `python _scripts/c47_tfact.py`
from `vault/`.

---

## 1. The USDA rule, verified from the primary source

[[C43-soil-ha-replication]] §3 asserted the mechanism from the data: "`T` is assigned on **profile
depth and fragility**". The handbook says something more specific. National Soil Survey Handbook,
Part 618 Subpart B (Amended August 2024) §618.91, read 2026-09-05 from
`https://directives.nrcs.usda.gov//sites/default/files2/1725389663/National%20Soil%20Survey%20Handbook%20%28entire%20handbook%29.pdf`
(HTTP 200, 11,795,683 bytes, 1,177 pp.; §618.91 on p. 431):

> "Soil loss tolerance 'T' is assigned according to properties of root and plant growth limiting
> subsurface soil layers."

Figure 618B-3, "Soil Loss Tolerance in Tons Per Acre by Group", verbatim:

| Depth to Limiting (cm) | Group 1 | Group 2 | Group 3 |
|---|:-:|:-:|:-:|
| 0 – 25 | 1 | 1 | 3 |
| 25 – 50 | 1 | 2 | 3 |
| 50 – 100 | 2 | 3 | 4 |
| 100 – 150 | 3 | 4 | 4 |
| > 150 | 5 | 5 | 5 |

Group 1 is a permanent (nonrenewable) root limitation, Group 3 one that "can be overcome through
natural or managed processes". Two exceptions are in the handbook and were quoted in the brief
before the test: subaqueous soils "are excluded from assignment of T factors", and "Severely
eroded soils, as designated by the local phase or erosion class of 3 or 4, are adjusted one class
of T factor lower." Figure 618B-4 then gives ~20 criteria rows — bedrock, permafrost, cemented
pans, organic materials — each with its own depth ladder, and Alaska ladders that differ again.

**So the object C43 named is real and is written down, but it is a two-argument function
(depth, renewability class), not the one-argument function the mechanism claim assumed.** That is
what H1 was written to measure.

## 2. What was joined

| Side | Source | Access, 2026-09-05 |
|---|---|---|
| `P` | **Portenga & Bierman 2011**, *GSA Today* 21(8):4–10, `10.1130/G111A.1` (Crossref: title, container-title, volume, issue, pages confirmed). GSA supplemental item 2011216, now on Figshare `10.1130/2011216`, CC BY-NC 4.0, `2011216.pdf`, 1,753,000 bytes. **Table DR2, Bedrock Outcrop Data**, CRONUS-recalculated erosion rate in m My⁻¹ = mm kyr⁻¹ | Figshare API + `ndownloader` **200**. 126 unique CONUS coordinates with a positive CRONUS rate parsed from pp. 22–24 |
| `T`, depth, slope | **USDA-NRCS Soil Data Access**, same endpoint as C43, extended to `co.slope_r`, `MIN(corestrictions.resdept_r)` and `muaggatt.brockdepmin` | POST `Tabular/post.rest`, 1,626 point queries. 114 of the 123 non-excluded outcrop points answered with a `tfact`; 800 of 1,500 random CONUS points did |

**The independence rule, applied.** OCTOPUS was checked first and is exhausted for this purpose:
`crn_xxl_basins` has 6 USA rows and every one carries `EBE_MMKYR = −9999.99`; `crn_inprep_basins`
has 0 USA rows. So Portenga's outcrop table is the independent sample. **3 of 126 points fell
within 0.005° of a C43 site and were dropped**, leaving 123 offered and 114 joined. The two
samples also differ in *kind*: C43's `P` is a basin-averaged denudation rate at an outlet;
these are ¹⁰Be concentrations in bedrock outcrop, a point measurement.

## 3. H1 — the depth rule, on 800 random CONUS points

Predicted class = the Group 2 column at the map unit's restriction depth (`resdept_r`, else
`brockdepmin`, else > 150 cm assumed).

| sample | n | Group-2 agreement | band agreement | depth from `resdept_r` / `brockdepmin` / assumed |
|---|---:|---:|---:|---|
| random CONUS points | 800 | **64.6%** | **84.5%** | 305 / 30 / 465 |
| DR2 outcrop sites | 114 | **37.7%** | **92.1%** | 100 / 8 / 6 |

Observed `tfact` by depth bin, the 800-point sample (columns `tfact` = 1…5):

| depth bin | 1 | 2 | 3 | 4 | 5 | G1/G2/G3 |
|---|--:|--:|--:|--:|--:|:-:|
| 0–25 | **23** | 4 | 0 | 0 | 5 | 1/1/3 |
| 25–50 | **56** | 17 | 4 | 0 | 7 | 1/2/3 |
| 50–100 | 2 | **55** | **63** | 18 | 11 | 2/3/4 |
| 100–150 | 0 | 0 | 22 | **33** | 3 | 3/4/4 |
| > 150 | 6 | 21 | 40 | 29 | **381** | 5/5/5 |

**H1 fails its ≥ 90% gate and the failure is informative in the direction the brief pre-specified.**
The mass sits inside the published band nearly everywhere; what the plain depth rule gets wrong is
which *group* a soil is in. Row "25–50" is the clearest: 56 sites read 1 (Group 1, permanent
limitation) against 17 reading 2 (Group 2). The residual disagreements — 6 sites at `tfact` = 1
with depth > 150 cm, 5 at `tfact` = 5 with depth < 25 cm — are consistent with the handbook's own
severe-erosion downgrade, with Figure 618B-4's organic and Alaska ladders, and with SSURGO
generalisation: `resdept_r` is a representative value for a map unit, not a profile at the point.
The 465 points with no restriction row at all are the largest single source of noise, and they are
where the assumed "> 150" is doing the work.

**The honest statement of the mechanism is therefore: `tfact` is a function of depth to a
root-restricting layer and the renewability class of that layer, and depth alone recovers about
two-thirds of it.** C43 §3's sentence is right in kind and too simple in form.

## 4. H2 — the consequence does not replicate on these sites

| statistic, n = 114 | ρ | p |
|---|---:|---:|
| ρ(`P`, depth bin) | **+0.026** | 0.781 |
| ρ(`P`, restriction depth cm) | +0.035 | 0.710 |
| ρ(`tfact`, `P`) | **+0.090** | 0.344 |
| ρ(`T`, `P`) | +0.221 | 0.018 |
| **partial ρ(`tfact`, `P` \| `slope_r`)** | **+0.075** | — |
| ρ(`slope_r`, `P`) | +0.167 | 0.076 |

**H2 fails.** It required ρ(`P`, depth class) < 0 at p < 0.01 and got +0.026 at p = 0.78. The
95% Fisher interval on ρ(`tfact`, `P`) is **[−0.095, +0.269]**, which **excludes C43's −0.206**.
Power to detect −0.206 at n = 114 is **0.60**, so this is a genuine non-replication and not a
null from n alone — but a single failure at 60% power is not a refutation either.

**The slope covariate was pre-registered as the thing that could hollow the claim out, and it
does not.** ρ(`slope_r`, `P`) = +0.167 and the partial ρ of `tfact` with `P` controlling slope is
+0.075 — barely moved from the raw +0.090. Whatever produced C43's sign, on this sample it is not
terrain confounding, because there is no anti-correlation left to explain.

The class table, next to C43's:

| `tfact` | n (C47) | median `P` mm/yr (C47) | median `P` mm/yr (C43) |
|:-:|---:|---:|---:|
| 1 | 21 | 0.0084 | **0.1733** |
| 2 | 33 | 0.0070 | 0.1049 |
| 3 | 23 | 0.0081 | 0.0288 |
| 4 | 3 | 0.0071 | 0.0255 |
| 5 | 34 | **0.0107** | 0.0288 |

**C43's six-fold fall in `P` from class 1 to classes 4–5 is simply absent here — the C47 column is
flat at 0.007–0.011 mm/yr across all five classes.** The reason is visible in the same numbers:
these outcrop rates have median 0.0082 mm/yr and interquartile range 0.0047–0.0178, against C43's
median 0.0378 and IQR 0.0141–0.1415. **Outcrop ¹⁰Be is both slower and far less variable than
basin denudation, and a flat `P` cannot correlate with anything.** The brief named exactly this in
§6 as running against detection.

## 5. H3 — within a class, `T` still does not track `P`, with one exception

Two classes reach the pre-registered n ≥ 25:

| `tfact` | n | ρ(`T`, `P`) | p | ρ(depth, `P`) | p |
|:-:|---:|---:|---:|---:|---:|
| 2 | 33 | **+0.390** | 0.025 | −0.178 | 0.321 |
| 5 | 34 | +0.037 | 0.836 | +0.048 | 0.786 |

**H3 fails as written**, on the class-2 row: the gate said any class with |ρ| ≥ 0.3 at p < 0.05
fails it. But the failure has a mechanical reading that must be stated because the gate did not
anticipate it. **Within a `tfact` class, `T` is constant up to bulk density** — `T` = `tfact` ×
2.2417 × 100 / ρ_b — so ρ(`T`, `P`) within a class is ρ(1/ρ_b, `P`), a correlation between soil
bulk density and erosion rate, not between a permit and a formation rate. The class-2 row says
low-density surface horizons sit where ¹⁰Be rates are higher. That is a real soil fact and it is
not evidence that `T` carries formation information. The variable H3 was reaching for is the
depth column, and there ρ = −0.178 (p = 0.32) and +0.048 (p = 0.79): **nothing**.

## 6. Honesty

**The pre-registration cost this note its headline and that is the point.** All three hypotheses
were written and hashed before the join; all three came back negative or partial. A note that
found the mechanism confirmed would have been the more quotable one, and it is not what the data
say.

**SDA answers at map-unit scale, and half the random points have no restriction row.** 465 of 800
random points carried neither `resdept_r` nor `brockdepmin` and were assigned "> 150 cm" by the
pre-registered fallback. If SSURGO records no restriction where one exists, H1's agreement is
understated; the DR2 subsample, where only 6 of 114 needed the fallback, gives the cleaner read of
the *band* (92.1%) and the worse read of the Group-2 column (37.7%), which is consistent with
outcrop sites being disproportionately Group 1 — shallow soils on hard rock.

**¹⁰Be on an outcrop is not soil formation either.** C43 §6 called basin-average-versus-point its
weakest joint; this note trades that for a different one. A bedrock outcrop erosion rate is the
lowering of exposed rock, measured where by definition there is little or no soil, and the
`tfact` joined to it is the map unit's attribute at that coordinate. The two ends of the join have
moved closer in space and further apart in kind.

**The depth ladder may have exceptions that this test scores as failures.** Quoted in §1 and
repeated here because it bounds H1 from above: T is "adjusted one class of T factor lower" for
severely eroded phases, subaqueous soils get no T at all, and Figure 618B-4 runs ~20 criteria with
Alaska variants. No agreement statistic against a single five-row ladder can reach 100%.

**This tests the USDA rule only.** [[C44-soil-ha-world]] already established that Verheijen et
al. 2009's proposed European range was derived from the soil-formation literature and is
calibrated (median `T`/`P` 0.22–1.01), so the depth mechanism is not expected to appear there and
was not looked for.

**What C43 keeps and what it loses.** C43's *primary* result — median `T`/`P` = 22.3 on 1,053
sites, the falsifier that did not fire — is untouched by this note, and the ratio here is larger
still (median 87) because outcrop `P` is small. What C43 loses is the §3 explanation: the sign of
ρ(`T`, `P`) was found in the data, was flagged there as "a hypothesis for someone else to test,
not a result", and on the first independent sample it does not reproduce. **`T` remains a
stock-based permit written in the units of a flux — §1 verifies that from the handbook — but the
claim that it runs *against* measured formation across sites is now one dataset for and one
dataset against.**

**Next.** The discriminating test is a sample with C43's spread in `P` and C47's independence:
basin-averaged rates from a compilation outside OCTOPUS, or Portenga's Table DR3 basins with the
OCTOPUS overlap removed by coordinate — the overlap was not measured here and DR3 was excluded by
the brief before the fact. A second lever is the renewability class itself: NASIS component
restriction *kind* is in SDA (`corestrictions.reskind`) and would turn H1's two-argument function
into a testable three-column prediction rather than a band.
