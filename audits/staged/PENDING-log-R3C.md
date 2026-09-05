---
name: PENDING-log-R3C
type: method
---

# PENDING — round 3, batch C (method/epistemics)

**Not a note. A staging file.** It holds (a) log entries for `vault/log.md` written in that
file's format, and (b) proposed edits to notes this agent did not own. Nothing here is
canonical, nothing links to it, and it should be emptied into its destinations and deleted by
whoever owns those files. Backlog rows: C1, C2, C3, C7, C15, plus the design halves of C5/C6.

---

## Part 1 — proposed log entries for `vault/log.md`

Copy verbatim, newest first, into `vault/log.md`.

## [2026-09-05] method | Citation intersection gets a null model; two gaps turn out denominator-sensitive

`method/citation-intersection.md` gains "Expected co-citers under independence":
`E = |citers_A|·|citers_B| / N_universe`, with `N` defined per provider (OpenAlex concept/year
window; or the union of the two citer sets as a computable *floor*, which because it is the
smallest `N` gives the largest `E` and therefore flatters gap claims — labelled as such).

Worked. **G28:** Gittins 1,013 x Charnov 5,424, observed 5, union floor N = 6,432, E = 854,
O/E = **0.0059**; control Gittins x Auer 2002 (`10.1023/A:1013689704352`, Crossref
`is-referenced-by-count` = 3,906, 2026-09-05) 1,013 x 3,906, observed 225, N = 4,694, E = 843,
O/E = **0.267**. The **control ratio 62.5** is denominator-invariant and replaces the note's
"factor of 45", which divided both sides by the same 1,013 base without correcting for the two
partner sets' different sizes. Correcting it makes the isolation slightly *stronger*.

**G6:** 172 engineering x 861 ecology, observed 0, union floor N = 1,033 gives E = **143**. But
`E ∝ 1/N`: at N = 10⁵, E = 1.5; at N = 10⁶, E = 0.15. **A zero intersection is a finding only
where E > 1.** G6's zero therefore requires a fetched, concept-scoped `N` below ~1.5×10⁵ works,
and no such number has been fetched. This is a real weakening and is recorded as one.

**G25:** the Shannon-side citer count was never logged, so `E` is not computable. The null model
reduces to one query — is Shannon 1948 cited by more or less than 3.85% of the universe? — but
the load-bearing claim (0 of 416 inspected citers carry coding-theory content) is
denominator-free and unaffected.

`method/positive-controls.md` restated in the same units. **Five of the six original controls
turn out to be unstateable there** — Gompertz x Weibull, Weibull x reliability-theory-of-aging,
Levy-flight, Gittins x Sutton & Barto and DNA-storage x ECC all lack at least one citer-set size,
recorded as "inputs not recorded" rather than filled in. "The signal separates cleanly" now rests
on **one** fully specified control pair.

## [2026-09-05] method | Failure mode 6 added: diachronic terminology drift

`method/failure-modes.md` (now "Six ways a measured zero can be fake") and `METHOD.md` §11. The
first non-synchronic mode: modes 1-5 assume both names coexist, mode 6 is the case where they
never did — a citer window spans decades, a vocabulary does not. Required step: bin the window by
decade and re-run the concept under each decade's own name, taken from a review published *in*
that decade; a zero survives only if it is a zero in every bin.

Specimen: **kedem-caplan**, from this log's own 2026-09-03 correction. The 1965 degree-of-coupling
result was called unread on 2 co-citers between two named 1960s papers; the re-read found it in
active use (*Entropy* 25:1575, arXiv:2403.20209). It had travelled into thermoelectrics as the
figure of merit `ZT` and dropped the eponym. Chosen over the symmorphosis /
over-provisioning-accuracy case, which is a *cross-field* synonym with both names in use at once
— synchronic, and already covered by the "originating field's term" mechanism.

## [2026-09-05] method | A string count may no longer overturn a gap without host + query + date

`method/failure-modes.md`. The string protocol fails re-test more than half the time in both
directions, and an overturning is a withdrawal, so `relationship-description`'s symmetry rule
applies. Host, exact query string and date are now all three required before
`standing: overturned` on a string-protocol basis; absent any of them the count is an unverified
lead and must be re-tested under citation intersection.

Specimens are the project's own two: **G8** (575 on `"Landauer" AND (neuron OR synapse OR
brain)` — query recorded, host and date not, and a four-term disjunction is exactly the shape
failure mode 5 says relaxes) and **G27** (26 unmodified, 551 under synonyms — the 21-fold jump is
mode 5's signature, so the load-bearing figure is the 26, whose host and date are not recorded).
Neither standing is changed by this; both are flagged as resting on numbers no one can re-run.

## [2026-09-05] method | Reservoir-audit Part B renamed hard-positive; aperture sensitivity now mandatory

`method/reservoir-audit.md`. Part B was headed "negative controls on resolved anomalies" and is
not one — every row is a real anomaly with a real nonzero residual and a partner that turned out
to exist, i.e. a hard *positive* control. Renamed, with the distinction stated: a negative
control is an input with no residual, testing whether the instrument can return nothing. There
has never been one.

New mandatory Part C step 5: **state the assumed coupling cross-section and report `A` at 2x and
0.5x that aperture.** F3 conceded the aperture is a free parameter and instructed "prefer the
largest defensible one" — a preference, not a reproducible procedure. An exclusion that does not
survive the 2x row is now `NOT TESTED`, not `RULED OUT`. Procedure renumbered to 12 steps.

Part D added: **negative-control designs, not run** — (a) a Betz-calibrated wind turbine, with
the correct null output specified as "the reservoir considered supplies the required coupling; no
residual", and (b) a fabricated zero-consistent thrust report `F = (0.4 ± 3.0) µN at 50 W`, whose
correct output is a new fifth verdict state `NO OBSERVABLE TO EXPLAIN` reached before candidate
enumeration. D.2 predicts a missing step 0: *if the observable is consistent with zero, the audit
does not run.*

## [2026-09-05] correction | specification-instruments Q7 row: "bias-immune, 11/11" was wrong twice

`method/specification-instruments.md`. Replaced with C16's post-blind-rule numbers: strict
CLASS-I **N = 8** closed, 7 systematics + 1 fluctuation, **0 new physics**, Clopper–Pearson
one-sided 95% upper bound `1 − 0.05^(1/8)` = **0.31**; CLASS-I+II N = 15, bound **0.18**. The
"11" came from hand assignment; the blind rule changes 11 of 24 assignments.

Bias-immunity softened the same way C16 softened it: findability of a documented *resolution*
correlates with the resolution being mundane, so the invisible cases are not a random sample and
"adding invisible same-class cases can only add more systematics" fails. **0 of 8 is consistent
with a same-class new-physics rate as high as 31%.**

---

## Part 2 — proposed edits to notes owned by other agents

### 2a. `vault/computed/C11-flyby-reservoir-audit.md` — aperture retrofit (backlog C7)

Another agent owns C11. Proposed: append an **aperture** column and a sensitivity block to the
per-reservoir table in §2, satisfying the new `reservoir-audit` Part C step 5. All values below
are the current post-Oberth ones (`F_req = 5.28×10⁻⁴ N`); nothing is recomputed and no verdict
changes.

**Scaling assumed:** `A = F_req/F_max` and `F_max` is linear in the aperture for all three
reservoirs — Lorentz `F = QvB` with `Q = CV` and capacitance linear in effective radius; drag
`F = ½ρV²C_dA` linear in frontal area; thermal `F = P_rad/c` with radiated power linear in
radiating area. So `A(2x) = A/2` and `A(0.5x) = 2A`. **State this scaling in the note** — it is
the assumption that makes the sensitivity two lines instead of a re-derivation.

Proposed replacement rows:

| Reservoir | Assumed aperture (nominal) | `F_max` | **A (nominal)** | A (2x aperture) | A (0.5x aperture) | Verdict |
|---|---|---|---|---|---|---|
| Earth rotation via geomagnetic field (Lorentz) | spacecraft floating-charge capacitance `C ≈ 10⁻¹⁰ F` at `V ≈ 10 V`, i.e. a ~1 m effective conducting radius; **no deployed conductor** | `QV_pB ≈ 3.1×10⁻¹⁰ N` | **1.7×10⁶** | 8.5×10⁵ | 3.4×10⁶ | **RULED OUT** — survives 2x by six orders |
| Anisotropic thermal radiation | full spacecraft radiating envelope at `P_rad ≤ ~1 kW`, `η = 1` (fully collimated) | `P_rad/c ≈ 3.34×10⁻⁶ N` | **160** | 80 | 320 | **RULED OUT** — survives 2x by ~2 orders; also excluded on sign |
| Atmosphere / exosphere drag at 539 km | NEAR frontal area with `C_d` order unity, `ρ ≈ 10⁻¹³ kg/m³` | `≈ 3×10⁻⁵ N` | **18** | **9** | 36 | **RULED OUT** — survives 2x, but this is the row where the rule bites |

Proposed prose to accompany it:

> **The drag row is the one the aperture rule was written for.** `A = 18` nominal falls to
> **9** at twice the assumed frontal area — still an exclusion, but a one-order one resting on an
> exospheric density marked UNVERIFIED and solar-cycle dependent. Per F7 (`1 < A < 10` on
> unverified inputs is `NOT TESTED`, not `RULED OUT`), **the drag exclusion at 2x aperture sits
> exactly on that boundary and is carried by the sign argument, not by `A`.** The Lorentz and
> thermal exclusions are aperture-insensitive to any defensible factor: an aperture large enough
> to rescue the Lorentz coupling would need to be ~10⁶ times NEAR's, which is not a spacecraft.

### 2b. `vault/method/information-audit.md` — Part C negative-control design (backlog C6)

Not in this agent's file list. Proposed section, design only, mirroring `reservoir-audit` Part D:

> **## Part C — negative controls (design; NOT YET RUN)**
>
> The 3/3 validation is a positive-only control set, and it is not blind: all three cases
> (Bérut 2012, Toyabe 2010, Koski 2014) are textbook results whose entropy sink is stated in the
> source the audit quotes, and Bérut has only one sink available by construction, so it cannot
> discriminate. The audit has never been shown to return "no unnamed sink."
>
> **C.1 — A device whose entropy books already close.** Feed a system with a fully accounted
> entropy budget and no unnamed sink: a measured, near-quasistatic isothermal gas expansion, or a
> Carnot-cycle heat engine at published efficiency, where `ΔS_total` is accounted to within
> measurement uncertainty by the named reservoirs alone. **What counts as returning nothing:**
> the audit's sink enumeration terminates with the *already-named* sinks supplying the full
> balance, `ΔS_residual` reported as an interval containing zero, and **no new sink specified.**
> If it names an additional sink, the Toyabe result — where naming the demon's memory register as
> the unnamed sink is the audit's headline success — is an artefact of the procedure.
>
> **C.2 — A blind case.** Compute the sink for one case *before* reading the source's conclusion,
> and record the pre-registration in the note with a date and the source withheld until after.
> The three existing cases cannot be un-read, so this needs a fourth. **What counts as passing:**
> the pre-registered sink matches the published one, and the pre-registration is timestamped
> ahead of the read.
>
> **C.3 — An adversarial case.** A published claim whose sink attribution was **later corrected**.
> The audit passes if it reproduces the correction, not the original attribution.
>
> **Until C.1 and C.2 are run, "validated 3/3" should be read as *validated against positives
> only, non-blind*.**

### 2c. Per-gap `expected` lines (backlog C1)

The gap notes are owned elsewhere. Proposed one-line additions, to sit beside each note's
existing intersection figure. Each names its `N` route, because `O/E` is meaningless without it.

**`vault/gaps/G28-marginal-value-gittins.md`**, into the *citation intersection* section:

> **Expected under independence.** `E = |A|·|B|/N`. With `|citers(Gittins 1979)| = 1,013`
> (run-time, 2026-09-03) and `|citers(Charnov 1976)| = 5,424`, the union floor `N = 6,432` gives
> `E = 854` against `O = 5`, i.e. **O/E = 0.0059**. The Gittins × Auer control at the same
> construction gives `E = 843` against `O = 225`, **O/E = 0.267**. The **control ratio is 62.5**
> and is invariant under the choice of `N` — it supersedes the "factor of 45", which divided both
> numerator sets by the same 1,013 base and so ignored that Charnov's citer set is 39% larger than
> Auer's. `N_universe` has **not** been fetched; the union floor is a floor, and at `N = 10⁶` the
> raw `O/E` rises to 0.91. **Quote the control ratio, not the raw O/E.** See
> `method/citation-intersection.md`.

**`vault/gaps/G6-multifunctionality.md`**, into the intersection table's surroundings:

> **Expected under independence.** `E = 172 × 861 / N`. At the union floor `N = 1,033` (the note's
> own "1,033 works"), `E = 143` against `O = 0`. But `E ∝ 1/N`: `E = 1.5` at `N = 10⁵` and
> `E = 0.15` at `N = 10⁶`, where a zero is uninformative because fewer than one co-citer is
> expected anyway. **This zero is a finding only if the shared universe is smaller than
> ~1.5×10⁵ works, and that number has not been fetched.** The required query is an OpenAlex
> concept/year window over the union of the materials-multifunctionality and
> ecosystem-multifunctionality concepts from the earliest citer year. The positive control
> Byrnes 2014 × Jost 2006 = 17 **cannot be restated in these units: `|citers(Jost 2006)|` was not
> recorded.** See `method/citation-intersection.md`.

**`vault/gaps/G25-proofreading-coding.md`**, into the contact-surface section:

> **Expected under independence.** Not computable as recorded: `|citers(Shannon 1948)|` was never
> logged. The model reduces to `O/E = (16/416) / f_Shannon = 0.0385 / f_Shannon`, where
> `f_Shannon` is Shannon 1948's base rate in the universe — **one query**
> (`cited_by_count` for `10.1002/j.1538-7305.1948.tb01338.x` over the same concept/year window
> that defines `N`) settles whether this literature over- or under-cites Shannon. **The gap's
> load-bearing figure is denominator-free**: `O = 0` works with coding-theory content among the
> 416 inspected gives `O/E = 0` for any positive `E`. The binding limitation on this note remains
> **28.4% coverage**, not the null model. See `method/citation-intersection.md`.

---

## Part 3 — not done, and why

- **`positive-controls.md` five unstateable rows.** Recovering them needs the citer-set size for
  the second anchor of each pair, and those anchors' DOIs were not recorded at time of run. This
  is B13/B14 work, not C1 work.
- **`N_universe` never fetched for any gap.** Every `O/E` above uses a union floor, which is a
  floor and is labelled as one. Fetching concept-scoped denominators is the natural follow-on and
  would change G6's standing argument materially.
- **Parts D.1/D.2 and information-audit C.1–C.3 are designs.** Running them creates computed
  notes (backlog C5, C6), which this pass was scoped out of.
