---
id: G29
name: G29-early-warning-prognostics
type: gap
standing: live
evidence: citation-intersection
contact-surface: 3
crosses: vocabulary
crosses-rank: 3
topology: direct
mediator: 
borrows-from: []
lends-to: []
mutual-with: []
computed-in: ["[[C26-ews-hazard-shape]]"]
uses-move: []
rests-on: []
tags: [node/gap, crosses/vocabulary, evidence/citation-intersection, standing/live]
last-checked: 2026-09-05
note: "Ecology's early-warning indicators and industrial prognostics estimate the same first-passage-to-threshold object and do not meet. OpenAlex Scheffer 2009 x Si 2011 = 2 against E = 670; OpenCitations re-run = 1 against E = 458, control Scheffer x Wissel = 268 (control ratio 7.6e-4). Zero in the 2009-2013 and 2014-2018 decade bins and 1 in 2019-2026, and zero across a 3x3 matrix of decade-appropriate anchors. All 3 co-citers inspected; none transfers the formalism, and one is an SSRN preprint. C26 computed the missing object and the discriminator failed. Re-run 2026-09-05 with the blank-key-filtering intersect.py: every count unchanged, standing unchanged."
exit: computation
extends-to: [ecology, conservation]
next-step-cost: S
---

# Early-warning signals and industrial prognostics

**STANDING: LIVE** · evidence: citation-intersection · contact surface: 3 · last checked 2026-09-05

> Both fields estimate **how close a system is to an irreversible transition, from a noisy time
> series, before it happens** — and neither reads the other. *Ecology* watches lag-1
> autocorrelation and variance rise as the leading eigenvalue approaches zero, and reports
> critical slowing down as a **trend in an indicator**, with a significance test against
> surrogates. *Reliability and prognostics/PHM* fits a degradation signal to a drift-plus-diffusion
> model, runs it to a failure threshold, and reports **remaining useful life as a distribution**,
> with a hazard and a Weibull shape parameter. The estimand is the same in both:
> a **first-passage distribution to a threshold**. The vocabularies, the anchors and the
> bibliographies are disjoint to within three papers.

Bears on [[C18-durability-axis]] (β as the shared coordinate) and [[C17-offset-from-threshold]]
(the early-warning indicator *is* C17's offset ε, and gain × bandwidth predicts a
variance-against-warning-time trade-off). Computed in [[C26-ews-hazard-shape]].

## Statement in both vocabularies

| | Ecology / regime shifts | Reliability / prognostics (PHM) |
|---|---|---|
| Object | distance to a fold bifurcation | remaining useful life to a failure threshold |
| Observable | detrended residual of a state variable | degradation signal (vibration RMS, sensor drift) |
| Statistic | rolling lag-1 AR coefficient, variance, skewness | drift `μ` and diffusion `σ` of a Wiener/gamma process |
| Reported as | a **trend**, with a Kendall τ and a surrogate test | a **distribution**: `RUL ~ IG(m, λ)`, hazard `h(t)`, Weibull `β` |
| Failure of the method | the shift was noise-induced, not bifurcation-induced | the damage state was not monotone |
| Canonical anchor | Scheffer *et al.* 2009 *Nature* | Si *et al.* 2011 *EJOR* |

**The same-object claim, stated so it can be attacked.** Both compute a first-passage law to a
threshold, and both use the variance and kurtosis of a residual to do it. **The strongest
objection** is that early-warning signals assume the transition is a *bifurcation of the system's
own dynamics* — stability is endogenously lost — whereas PHM assumes a monotone *exogenous*
damage state with dynamics held fixed. A noise-induced ecological shift has no eigenvalue for the
PHM machinery to track; a bearing has no alternative stable state to shift to. If that objection
holds, the shared object is only "both do change-point detection". **[[C26-ews-hazard-shape]] was
built to settle it, and the objection largely wins** — see *What survives*.

## Provenance

### Starting provenance — taken verbatim from `audits/scout-02-resilience.md`, candidate #1

- **Provider:** OpenAlex, polite pool, `mailto=deciduusleaf@gmail.com`. **Fetched 2026-09-05.**
- **Endpoint:** `https://api.openalex.org/works?filter=cites:<W_A>,cites:<W_B>&per-page=25&mailto=deciduusleaf@gmail.com`
- **Anchors** (both DOIs Crossref-verified by the scout via `api.crossref.org/works/<doi>`):
  - A = Scheffer *et al.* 2009, *Early-warning signals for critical transitions*,
    [10.1038/nature08227](https://doi.org/10.1038/nature08227) → `W2116199452`
  - B = Si *et al.* 2011, *Remaining useful life estimation — a review on the statistical data
    driven approaches*, [10.1016/j.ejor.2010.11.018](https://doi.org/10.1016/j.ejor.2010.11.018)
    → `W2055873761` (OpenAlex `publication_year` = **2010**, online-first; the printed year is 2011)
  - B′ = Randall & Antoni 2011, *Rolling element bearing diagnostics — a tutorial*,
    [10.1016/j.ymssp.2010.07.017](https://doi.org/10.1016/j.ymssp.2010.07.017) → `W1964511482`
- **Counts:** `N_A = 4,891`, `N_B = 2,098`, **`O = 2`**. Against B′: `N_B′ = 2,670`, **`O = 0`**.
- **`N_universe` = 15,304**, from
  `works?filter=concepts.id:C114725131|C129364497,from_publication_date:2011-01-01`
  (Tipping point ∪ Prognostics).
- **`E = 4,891 · 2,098 / 15,304 = 670`**, so **`O/E = 0.0030`**. Against B′, `E = 853`, `O/E = 0`.
  Still informative at 10× `N` (`E = 67` and `85`).
- **Control pair:** Scheffer 2009 × Wissel 1984, *A universal law of the characteristic return
  time near thresholds*, [10.1007/bf00384470](https://doi.org/10.1007/bf00384470) → `W2066648930`.
  `N_A = 4,891`, `N_B = 441`, **`O = 321`**; `E = 254` concept-scoped, **`O/E = 1.26`**.
- **Control ratio** (denominator-invariant): `(2/2,098) / (321/441)` = **0.0013**.
  A second control, Holling 1973 × Bruneau 2003, gives `O = 1,420`, `O/E = 11.3`; the ordering
  is unchanged against it.
- **Cost to close, as scouted:** 1 desk session.

### Independent re-run — OpenCitations, 2026-09-05

**OpenAlex's `filter=cites:` endpoint returned HTTP 429 for the whole of this session's window**
(single-work fetches at `works/<id>` succeeded; the intersection filter did not, across ~90
attempts with backoff to 20 s over ~40 minutes). The re-run therefore used a **different
provider**, which is the stronger test anyway.

- **Provider:** OpenCitations Index. **Endpoint:**
  `https://api.opencitations.net/index/v1/citations/<doi>`, citer DOI sets intersected.
  **Fetched 2026-09-05.**
- **Cleaning:** OpenCitations returns some citation records with an **empty `citing` DOI**
  (e.g. `oci:06022989134-06260366631`). Deduplicated as a set, a single blank key produces a
  **false intersection in every pairing**. Blanks are dropped; without that step every row below
  reads one higher, and the Randall row reads 1 instead of 0.
- **Re-verified 2026-09-05 with the repaired `_scripts/intersect.py`** (blank/whitespace `citing`
  keys dropped before the sets are built, drop count printed, `--selftest` asserting no blank key
  survives). Raw records → blanks dropped → unique citers: Scheffer 3,999 → 65 → **3,934**;
  Si 1,795 → 12 → **1,783**; Randall 2,237 → 12 → **2,225**; Jardine 3,668 → 15 → **3,653**;
  Wissel 374 → 13 → **361**. **Every count in the table below is unchanged**, because this note's
  original run already stripped the blanks by hand. The phantom **was** present in the raw
  payloads of all five anchors: unfiltered, the four rows would read 2 / 1 / 2 / 269 instead of
  1 / 0 / 1 / 268. `contact-surface: 3`, `standing: live` and the tags are unchanged.

| Pairing | `N_A` | `N_B` | **`O`** | Hits |
|---|---|---|---|---|
| Scheffer 2009 × **Si 2011** | 3,934 | 1,783 | **1** | `10.1007/s42524-021-0176-y` |
| Scheffer 2009 × **Randall & Antoni 2011** | 3,934 | 2,225 | **0** | — |
| Scheffer 2009 × **Jardine 2006** (CBM, the earlier B-side name) | 3,934 | 3,653 | **1** | `10.3390/s23020965` |
| **Control:** Scheffer 2009 × **Wissel 1984** | 3,934 | 361 | **268** | not enumerated |

Against the scout's `N_universe = 15,304`: `E = 3,934 · 1,783 / 15,304 = 458`, **`O/E = 0.0022`**.
Control `E = 3,934 · 361 / 15,304 = 92.8`, `O/E = **2.89**`.
**Control ratio = `(1/1,783) / (268/361)` = 7.6 × 10⁻⁴** — same order as the scout's 1.3 × 10⁻³
on a different provider, and three orders of magnitude below a joined literature.

Sensitivity, per [[citation-intersection]]: union floor `N = 5,716` → `E = 1,227`, `O/E =
8.1 × 10⁻⁴`; 10× the concept scope, `N = 153,040` → `E = 45.8`, still `> 1`, **so the low count
is a finding at every defensible denominator**. The two providers disagree by one co-citer
(2 vs 1) because OpenCitations is DOI-only; that disagreement is a coverage fact, not a
contradiction, and neither number is near `E`.

## Every hit inspected

**Three distinct works, all three read to a verdict.** Two from OpenCitations, plus the third
OpenAlex hit named by the scout.

1. **`10.1007/s42524-021-0176-y` — *System reliability and system resilience*,
   *Frontiers of Engineering Management* 8(4), 2021** (Crossref, fetched 2026-09-05; 44
   references). **Verdict: a genuine bridge at the level of terminology, not formalism.** It is a
   perspective piece that puts reliability engineering and resilience side by side and cites
   both anchors as representatives of the two discourses. It does not fit an ecological series
   with a prognostics model, nor an engineering series with an early-warning indicator. This is
   `crosses: vocabulary`, and it is the reason this note is not `topology: disjoint`.
2. **`10.3390/s23020965` — *An Adaptive Sampling Framework for Life Cycle Degradation
   Monitoring*, *Sensors* 23(2), 2023** (Crossref + OpenAlex abstract, fetched 2026-09-05).
   **Verdict: a genuine one-way borrowing, engineering → ecology.** A condition-monitoring paper
   on sampling-interval strategy that reaches into the critical-transitions literature for its
   framing. The traffic runs the *opposite* way to the one this gap cares about: engineering
   reads Scheffer, ecology does not read Si. This is the `one-way-borrowing` signature.
3. **`10.2139/ssrn.7266197` — *Physics-Based Landau–Ginzburg Features for Survival
   Prognostics*, 2026** (Crossref bibliographic search, fetched 2026-09-05).
   **Verdict: genuine, and materially weaker than it looks — it is an SSRN preprint, not a
   peer-reviewed paper**, and it is from the current year. The scout reported it as one of two
   hits without noting the venue.

**So the crossing is three papers wide against `E ≈ 458–670`, one of them a preprint, one of them
running the wrong way, and none of them transferring the estimator.**

## The decade-binned re-run (`failure-modes` mode 6)

`failure-modes` mode 6 is mandatory here because a citer-set intersection anchored on named
papers measures traffic between those papers, not whether the object travelled under a later
name. **Two things were run.**

**(a) Year bins across the citer window.** The window is only 2009–2026, because both anchors
are ~2010 works; per-bin counts from the OpenCitations `creation` field:

| Bin | gap `N_A` | gap `N_B` | gap `O` | ctrl `N_B` | ctrl `O` | ctrl `O/N_B` | **bin control ratio** |
|---|---|---|---|---|---|---|---|
| 2009–2013 | 494 | 81 | **0** | 56 | 46 | 0.821 | **0** |
| 2014–2018 | 1,092 | 507 | **0** | 102 | 81 | 0.794 | **0** |
| 2019–2026 | 2,309 | 1,176 | **1** | 187 | 137 | 0.733 | **1.2 × 10⁻³** |

**The zero is a zero in every bin under contemporaneous anchors, and the control is joined in
every bin** at a stable ~0.75–0.82 — so the instrument is working in each decade, and the single
co-citer is a 2021 arrival, not a long-standing connection.

**(b) Decade-appropriate anchors on both sides**, which is the substantive form of mode 6.
Before ~2009 the ecology side did not say "early-warning signal": it said *catastrophic shift*
(Scheffer 2001) or *characteristic return time* (Wissel 1984), and Dakos 2008 is the
palaeoclimate specimen. Before ~2010 the engineering side did not say "prognostics and RUL": it
said *condition-based maintenance* (Jardine 2006) or, earlier still, *life data analysis*.
A full 3 × 3 (OpenCitations, 2026-09-05, blanks dropped):

| | Si 2011 (`N_B` 1,783) | Jardine 2006 (`N_B` 3,653) | Randall 2011 (`N_B` 2,225) |
|---|---|---|---|
| **Scheffer 2001** (`N_A` 5,972) | **0** | **0** | **0** |
| **Dakos 2008** (`N_A` 885) | **0** | **0** | **0** |
| **Wissel 1984** (`N_A` 361) | **0** | **0** | **0** |

**Nine zeros.** The object did not travel under an earlier name either. Mode 6 does not rescue
this literature; if anything the pooled `O = 1–2` is generous, and it belongs entirely to the
most recent bin under the most recent names.

**What mode 6 cannot rule out** and is stated as a limit: a third vocabulary neither side owns —
change-point detection, survival analysis in biostatistics, structural health monitoring — could
be carrying the same object between them without citing either anchor. No mediator was found, so
`topology: direct` rather than `mediated`, but that is an absence of evidence.

## What survives

**The citation gap survives at full strength. The scientific promise attached to it does not.**

[[C26-ews-hazard-shape]] built the missing object — the Si-2011 Wiener-degradation first-passage
estimator composed with the Dakos/Scheffer critical-slowing-down indicator — and ran it on the
Cariaco Younger-Dryas record against NASA C-MAPSS turbofan fleets. **The discriminator the scout
proposed (`β > 1` bifurcation-driven, `β ≈ 1` noise-induced) fails its own controls**: Cariaco
gives β = 5.84 [1.98, 10.63], a *stationary AR(1) surrogate with no bifurcation at all* gives
β = 7.39 (one-sided `p = 0.66`), and the same record with the transition cut off gives β = 4.97.
Worse, β is estimator-dependent: on 100 C-MAPSS units the ensemble-lifetime MLE gives β = 4.41
and the degradation-to-first-passage route on the *same units* gives β = 0.97.

So the honest reading of this gap is now sharper than the scout's:

- **The literatures genuinely do not meet.** Nine zeros under decade-appropriate anchors, three
  inspected co-citers, control ratio 7.6 × 10⁻⁴. That part is not in doubt.
- **The reason may be good.** The metaphor risk named at the top — endogenous bifurcation versus
  exogenous monotone damage — is exactly what C26's controls detect. The transfer that ecology
  actually needs from prognostics is **not** the hazard model. It is the **fleet**: prognostics
  reports a distribution because it has 100 replicate units, and ecology has one lake.
- This is [[C18-durability-axis]]'s asymmetry recurring for a third time, and it also **corrects
  C18**: β is well-defined only once the estimator is named.

## What would close it

1. **A mechanism-labelled collection of ≥10 published regime-shift series** (bifurcation-induced
   versus noise-induced, assigned independently of the indicator), run through C26's R2 estimator
   against matched stationary surrogates. Separation at `p < 0.05` would revive the
   discriminator; overlap would move this note to `narrowed` with the negative attached.
   **Cost: M.** This is the single highest-value next step and it needs no new mathematics.
2. **The published bearing β values** (IMS run-to-failure, and the Weibull fits in the
   bearing-prognostics literature) added to C26's table — one desk session, and it settles
   whether the engineering R1/R2 split in C26 is general or an artifact of C-MAPSS being a
   simulator. **Cost: S.**
3. **A full-text read of the three co-citers' reference lists**, to check whether any of them
   carries the estimator across rather than only the words. The verdicts above rest on titles,
   abstracts and venue, not on full text. **Cost: S.**
4. A **mediator search** in change-point detection and structural health monitoring, which is
   the one route mode 6 cannot close from citer sets alone. **Cost: M.**
