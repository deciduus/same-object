---
name: C53-mars-exchange-feasibility
type: computed
exit: specification
extends-to: astrobiology
next-step-cost: M
---

# C49's exchange residual, tested against regolith adsorption: the answer is one number, and it is `ΔH`

> **WITHDRAWN AS NOVEL 2026-09-05 (adversarial pass, `audits/c53-adversarial.md`).** Hu, Bloom, Gao, Miller & Yung 2016, *Astrobiology*, `10.1089/ast.2015.1410`, states in its abstract that ~36 kJ/mol is needed to explain the methane spikes, "higher than existing laboratory measurements", names Gough 2010's 18 kJ/mol, and calls for the lab study. Hu 2016 is in the reference list of Yung 2018, which C49 read in full; this note cites it nowhere. Two further defects: the `A = 1` threshold on this note's own scaling law is **26.4 kJ/mol, not 28** (at 28 the ledger already passes 2.6×); and the hashed brief pre-committed to a `(dq/dp)·Δp` term that `c53_exchange.py` never implements — the seasonal `p_CH₄` swing (~170%) exceeds the thermal driver and its sign threatens the 31.5 kJ/mol pass, not the fail. Ortiz et al. 2022 (*Icarus* 385:115079) adds barometric pumping, so "one number, not physics" is false. What survives: the 180–240 K temperature window and the seasonal-background (not spike) framing are sharper than Hu 2016; the ten-year-old lab ask stands. Grade: **REDISCOVERED**.

> **FAIL on the measured isotherm, PASS on the fitted one, and that is the whole result.**
> Driving physisorbed CH₄ off the regolith with Mars' *annual* temperature swing supplies
> **`ΔM_ads = 1.45×10⁻¹⁰ kg m⁻²`** per season planet-wide — **`21.0 t`** against `3,820 t`
> required, **`A_exchange = 182`**, `RULED OUT`, and it survives the 2× aperture row at `91`.
> Re-run with the enthalpy that Smith/Moores 2019 had to **fit** to the Gale data
> (`31.5` vs Gough 2010's measured `18 ± 1.7 kJ mol⁻¹`) and the same arithmetic gives
> **`8.37×10⁴ t`**, `A_exchange = 0.046` — a **PASS by 22×**. The two published conclusions —
> Meslin 2011's "little variability" and Moores 2019's "consistent with regolith adsorption" —
> **are not a physics disagreement; they are `exp(ΔH/RT)` evaluated at two different `ΔH`,
> a factor of 3,989 across a 13.5 kJ mol⁻¹ gap.** I reproduce Meslin 2011 when I use measured
> numbers. **The residual therefore does not close: it tightens to a demand on a laboratory
> quantity.**

Blind brief archived and hashed **before** the run at `audits/blind-brief-c53-2026-09-05.md`,
sha256 `7529887e8233ede93ab66860c2d900ae37e41323f125f59d9f5890f837d5857f`. Arithmetic:
`vault/_scripts/c53_exchange.py`. All fetches **2026-09-05**. P-089, Track C.

See [[C49-mars-methane-audit]] (the `EXCHANGE REQUIRED` residual this tests),
[[reservoir-audit]] (step 5 aperture rows, F3, F7, F10),
[[C30-venus-phosphine-audit]] (§Corrections: do not adopt a published margin as if computed).

---

## 1. The inputs, each sourced

| # | Quantity | Value | Source | Status |
|---|---|---|---|---|
| 1 | Adsorption enthalpy, CH₄ on JSC Mars-1 | **`ΔH_obs = 18 ± 1.7 kJ mol⁻¹`**, from `γ` measured **115–135 K** and *extrapolated* to Mars T | Gough, **Tolbert, McKay & Toon** 2010, *Icarus* 207, 165–174, `10.1016/j.icarus.2009.11.030` | Crossref-verified (title/authors/journal/date/67 refs/32 cites, 2026-09-05). Paywalled → **VERIFIED-SECONDARY** on the value |
| 2 | Best-fit `ΔH` needed to reproduce the Gale cycle | **`31.5 kJ mol⁻¹`**, `γ/η = 1`, EADT `30` sols, seep `2.8×10⁻¹⁶ kg m⁻² s⁻¹`, `χ²_ν = 0.91`; **"Current values for `γ/η` and `ΔH` determined from laboratory studies … do not produce good fits"** | Smith, Moores, Gough, Martinez, Meslin, Atreya, Mahaffy, Newman & Webster, LPSC 50 (2019) abs. **1289** | **VERIFIED-PRIMARY, full-text-read** (2 pp., fetched 2026-09-05) |
| 3 | Peer-reviewed form of #2 | 1-D adsorption+diffusion reproduces amplitude **and phase lag** if the regolith is impregnated by a prior plume or fed by microseepage `≤ 3×10⁻⁵ t km⁻² yr⁻¹` | Moores et al. 2019, *Nat. Geosci.* 12, 321, `10.1038/s41561-019-0313-y` | Crossref-verified; **abstract read**, body not obtained (HAL bot-wall) |
| 4 | The adverse published conclusion | seasonal variation from adsorptive regolith transfer at Gale's latitude is **"less than a few percent"**, from a GCM with a coupled subsurface module | Meslin, Gough, Lefèvre & Forget 2011, *PSS* 59, 247–258, `10.1016/j.pss.2010.09.022` | Crossref-verified (43 refs, 24 cites); paywalled → **VERIFIED-SECONDARY** |
| 5 | Nighttime near-surface enhancement | `≤ 50 pptv` above 5 km vs `410 pptv` overnight at Gale, reconciled by inhibited nocturnal mixing; only **`2.7×10⁴ km²`** of Mars need be emitting | Moores et al. 2019, *GRL*, `10.1029/2019GL083800` | Crossref-verified; **abstract read**, PDF 403 |
| 6 | Seasonal amplitude | `0.24 → 0.65 ppbv` (LPSC 1289 prints `0.23–0.65`) | Webster et al. 2018, `10.1126/science.aaq0131`, via #2 | inherited from C49 |
| 7 | Regolith gas transport | Sizemore & Mellon 2008, *Icarus*, `10.1016/j.icarus.2008.05.013` | Crossref-verified (67 refs, 68 cites) | paywalled; **`D_eff` NOT obtained** — the bracket in §2 is mine |
| 8 | `τ₀ = 10⁻¹³ s`, `ρ = 1300 kg m⁻³`, `I = 300`, `c = 800`, `S = 100 m² g⁻¹`, `T̄ = 210 K`, `ΔT_pp = 20 K` | standard values | — | **UNVERIFIED**; §4 gives the sensitivity on each |

## 2. The accessible depth is thermal, not diffusive — and the brief pre-committed to that

Annual thermal skin depth `δ = √(κP/π)` with `κ = I²/(ρc)²`: **`1.254 m`** (diurnal: `4.85 cm`).
Diffusive reach over half a Mars year, `√(D_eff·t)`: **17.2 m** at `D_eff = 10⁻⁵ m² s⁻¹`,
**54.5 m** at `10⁻⁴`, **158 m** at a Knudsen estimate `8.4×10⁻⁴`. Diffusion is **not** the
limit at any plausible `D_eff`; the brief said *use the smaller* before either was computed, and
the smaller is the thermal one by **14–126×**. **Below ~1.3 m there is no seasonal temperature
swing to desorb against, however permeable the soil.** This is the one place the calculation
could have been rigged, and it was fenced in advance.

## 3. The computation

Frenkel residence-time physisorption, low coverage (`θ ≈ 10⁻¹²–10⁻⁸`, so Henry's law is exact
and Langmuir saturation never binds — consistent with C49's "capacity survives by six orders"):

```
N_ads = γ · Z · τ₀ · exp(ΔH/RT)      Z = p/√(2πm kT)   (Hertz–Knudsen)
∂ln q/∂T = −ΔH/(RT²)                 ΔT(z) = ΔT_pp · e^(−z/δ),  ∫₀^∞ dz = δ
ΔM_ads = ρ · q · (ΔH/RT²) · ΔT_pp · δ    [kg m⁻²]
```

with `p = 0.41 ppbv × 610 Pa = 2.50×10⁻⁷ Pa`.

| `ΔH` (kJ mol⁻¹) | `τ_res` | `θ` | `q` (kg CH₄/kg soil) | **`ΔM_ads`** (kg m⁻²) | planet total | **`A_exchange`** | verdict |
|---|---|---|---|---|---|---|---|
| **18.0** (Gough, measured) | `3.0×10⁻⁹ s` | `5.4×10⁻¹²` | `9.07×10⁻¹⁴` | **`1.452×10⁻¹⁰`** | **`21.0 t`** | **`182`** | **`RULED OUT`** |
| **31.5** (Smith/Moores, fitted) | `6.8×10⁻⁶ s` | `1.2×10⁻⁸` | `2.07×10⁻¹⁰` | **`5.794×10⁻⁷`** | **`8.37×10⁴ t`** | **`0.046`** | `SURVIVES`, 22× spare |

**The entire distance between `RULED OUT` and `SURVIVES` is `exp(13.5 kJ mol⁻¹ / RT̄) × 1.75 =
3,989`.** `ΔH` and `τ₀` are degenerate: 13.5 kJ mol⁻¹ at 210 K is the same as a factor **2,280**
in the pre-exponential. Nothing else in the ledger has that leverage.

### Step-5 aperture rows (MANDATORY; available is linear in area)

| Aperture | `ΔH = 18` available / `A_exchange` | `ΔH = 31.5` available / `A_exchange` |
|---|---|---|
| 2× planet | `41.9 t` / **`91.1`** | `1.67×10⁵ t` / `0.023` |
| **planet, `1.444×10⁸ km²` (nominal, = C49's own row)** | **`21.0 t` / `182`** | **`8.37×10⁴ t` / `0.046`** |
| 0.5× planet | `10.5 t` / `364` | `4.18×10⁴ t` / `0.091` |
| Gale-like emitting terrain, `2.7×10⁴ km²` (Moores 2019 GRL) | `3.9 kg` / `9.7×10⁵` | `15.6 t` / `244` |

The measured-`ΔH` exclusion **survives the 2× row** (`91 > 1`), so it is an exclusion under F7,
not a `NOT TESTED`. The last row is asymmetric on purpose: C49's `3,820 t` is a **planet-wide
burden** requirement, so shrinking the aperture shrinks *available* only. Read Gale-locally the
required mass falls too — that is C49 §6 row 4's `×9.8` aperture problem again, unresolved here.

## 4. Sensitivity on the soft inputs (measured-`ΔH` row)

`ΔT_pp = 10 / 20 / 30 K` → `A = 364 / 182 / 121` (linear). `S = 17 / 100 m² g⁻¹` →
`A = 1,072 / 182` (linear). `τ₀` is linear. **To rescue the measured-`ΔH` row you need `182×`
from `ΔT_pp`, `S` and `τ₀` jointly, and each is bounded within a factor of a few.** The exclusion
is robust to everything except `ΔH` itself.

**Why the diurnal cycle cannot substitute.** Its `ΔT_pp` is ~4.5× larger but its skin depth is
26× smaller, so the driving integral `ΔT·δ` is `4.36 K·m` against the annual `25.1 K·m` — the
annual cycle wins by **5.75×**, and only the annual cycle is season-locked. A diurnal mechanism
(Moores 2019 GRL, input #5) has **zero seasonal net**: it explains day/night, not `0.24 → 0.65`.

## 5. Agreement with Meslin 2011 — and what in it is not independent

**I reproduce their conclusion.** Meslin et al. get "less than a few percent" of the seasonal
variability from regolith adsorption at Gale's latitude; I get supply short of requirement by
`182×`, i.e. **`0.55%`** of the needed amplitude. Two routes with no shared arithmetic: theirs is
a GCM with a coupled subsurface transport module and full adsorption kinetics; mine is a one-line
Frenkel estimate damped by a thermal skin depth. The **only** shared input is Gough 2010's `ΔH`,
which is an input to both and a result of neither.

**Per the C30 lesson, what is *not* independent:** I did not read Meslin 2011, so "a few percent"
against my `0.55%` is agreement in *direction and order*, not a matched number — and I take no
credit for the digit. I also did not read Gough 2010; `18 ± 1.7 kJ mol⁻¹` is quoted at second
hand. **The agreement is a genuine second derivation of a published conclusion; the numerical
closeness is not evidence, because neither margin was re-derived from raw data.**

**And the reconciliation with the adverse-looking Moores 2019 is complete.** Meslin is a
co-author of Moores 2019. Nothing was retracted between them. Meslin 2011 asked whether
adsorption *with laboratory parameters* produces the variability — no. Moores 2019 asked whether
an adsorptive-diffusive model *fitted to the data, with a subsurface seep supplying the methane*,
reproduces it — yes, at `ΔH = 31.5`. **LPSC 1289 says outright that the lab values do not fit.**
The literature is consistent; the load-bearing quantity is unmeasured at Mars temperatures.

## 6. What C49's residual now specifies

C49's `EXCHANGE REQUIRED` residual said: a two-way surface reservoir at `≥ 3,820 t/yr` per phase,
season-locked, `τ_eff = 0.944 yr`. **It does not close on adsorption, and it does not keep its
shape either.** It splits into three disjoint successors, one of which is cheap:

> **(a) A laboratory measurement.** Adsorption closes the residual **iff** the CH₄–regolith
> adsorption enthalpy at 180–240 K on a real Mars analogue is **`≥ ~28 kJ mol⁻¹`** (the value at
> which `A_exchange` crosses 1 on this ledger at `S = 100 m² g⁻¹`, `ΔT_pp = 20 K`), against a
> measured `18 ± 1.7` obtained at **115–135 K and extrapolated**. That is a checkable prediction
> about a bench experiment, not about Mars.
> **(b) Or a non-adsorptive two-way process** — clathrate destabilisation, subsurface barometric
> pumping, microbial cycling — which must supply the *sign alternation* adsorption cannot.
> **(c) Or the observable is not real.** C49 already flagged the Gale seasonal cycle as a single
> instrument with no independent reduction (`UNREPLICABLE OBSERVABLE`).

**(a) is new and it is the useful one.** C49 ended with a residual stated about *Mars*; C53 ends
with a residual stated about a *cryostat*. A residual that names a laboratory measurement is
strictly tighter than one that names a planetary process, and this one names the temperature
range at which the existing measurement stops.

## 7. Honesty

**The blind is single-agent**, as in C49 and C52: the brief was written and hashed by the agent
that ran it. Nothing in the brief names a verdict, and the brief pre-committed to the two moves
that could have rigged the answer — *use the smaller of thermal and diffusive depth*, and
*single-component isotherms give an upper bound, so a failure is robust and a pass is soft*. Both
were honoured. But Mars methane adsorption is recognisable, and **Meslin 2011's adverse
conclusion was named in the brief**, so this is a confirmation, not a discovery.

**The direction of the bounds matters, and it favours the FAIL.** Every soft assumption was set
generously toward a pass: `γ = 1` (perfect sticking), `S = 100 m² g⁻¹` (JSC Mars-1's high end,
~6× real Mars regolith estimates), single-component adsorption with **no** competition from the
95% CO₂ atmosphere or from adsorbed H₂O, both of which would displace CH₄ and lower `q` further.
The `21 t` is therefore an **upper bound** and `A = 182` a **lower** bound on the shortfall. The
`ΔH = 31.5` pass, by the same logic, is **soft** — it is a fit, and its inputs are the generous
ones.

**What was not obtained.** Gough 2010, Meslin 2011, Sizemore & Mellon 2008, Moores 2019 (both
papers) — Crossref-verified for DOI, title, author, journal and date; **none full-text-read**
(Elsevier, Wiley and Nature paywalls, and a bot-wall on the HAL green copy). Only LPSC 1289 was
read in full, and it is a two-page conference abstract. `D_eff` was never fetched; §2's bracket
is mine, and it does not matter only because the thermal depth wins by more than an order.

**A number in C49 does not check out, and it is not mine to fix.** C49 §5 states the residual as
`0.072 mg m⁻² day⁻¹`. `3,820 t yr⁻¹ ÷ 1.444×10¹⁴ m² ÷ 365.25 d` = **`7.24×10⁻⁵ mg m⁻² day⁻¹`** —
a factor of **10³**, i.e. the figure is in **µg**, not mg. The direction is *favourable* to C49's
own argument (the requirement is 5–6 orders below terrestrial microseepage, not 2–3), so nothing
in its verdict moves. **Logged, not edited** — C49 is held by another agent this session.

**What a surface chemist would attack first.** `τ₀ = 10⁻¹³ s` with `γ = 1` is a textbook
transition-state estimate, not a measured pre-exponential for this surface, and it is exactly the
quantity degenerate with `ΔH`. If Gough 2010's `γ`-versus-`T` data pin `τ₀` directly, my
"measured" row could move by an order without touching `ΔH`. It cannot move by 182 — but a reader
who has the paper should redo row 1 with the published `γ(T)` rather than my `γ = 1`.
