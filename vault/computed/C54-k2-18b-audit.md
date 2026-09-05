---
name: C54-k2-18b-audit
type: computed
exit: specification
extends-to: astrobiology
next-step-cost: S
---

# K2-18 b DMS, audited in a two-agent blind: `NO AGREED OBSERVABLE`, and the free parameter is not the aperture

> **Step 0(b) halts: `NO AGREED OBSERVABLE`.** Independent reductions of the *same* JWST photons
> span detected and not-detected — Madhusudhan 2025 reports DMS/DMDS at `2.9–3.2σ`, `≳10 ppmv`,
> from MIRI/LRS; Taylor 2025 re-tests **those same MIRI photons** as Gaussian features and prefers
> a flat line in **5 of 6 tests**, `χ²_ν = 1.06`, `~2σ`; Schmidt 2025 re-reduces the
> NIRISS+NIRSpec photons through **60 data treatments and >250 retrievals** and finds no reliable
> DMS *or CO₂*; Luque 2025 finds nothing above `3σ`, all below `~2σ` absent a strong haze prior.
> This is D.3 / F8's **second real case after Venus, and the first with an uncontaminated blind**.
> Run **conditionally** — *if* 10 ppmv were real — the inventory is `1.21×10¹⁷ mol` (`7.54×10¹² t`)
> above 1 bar and `F_req = 4.44×10¹⁹ mol/yr` at Earth's DMS lifetime, **`5.1×10⁷ ×` Earth's marine
> flux**. That `A` is not an exclusion: **step 1's `A ≫ 10⁴` diagnostic fires**, and the
> mis-specification is `τ`, not the aperture. The inversion is the real output:
> **`τ_photo ≥ 6.95×10³ yr`**, `2.5×10⁶ ×` Earth's DMS lifetime.

Blind brief archived and hashed **before** dispatch at `audits/blind-brief-c54-2026-09-05.md`,
sha256 `ec039762abc96170a570932a69886e2c905e5eb5af6041c4bbc91605a0c3d840` — **verified this
session** over the content above the hash line (trailing whitespace stripped, one terminal
newline; the file is LF-only, so the CRLF-normalised digest is identical). Arithmetic:
`vault/_scripts/c54_k218b.py`, re-runnable, every input marked in the source.

## 1. Step 0(a) — significance, per reduction

`0(a)` does **not** halt on the claim row. Madhusudhan et al. 2025's MIRI/LRS detection is
`2.9–3.2σ` across their canonical retrievals (`3.4σ` against a featureless model), an interval
that does not contain zero. Run on that row alone the audit proceeds. **`0(a)` is not the test
that catches this case** — which is precisely the D.3 §"Not D.2" distinction, now demonstrated on
a real input rather than argued.

The abundance is reported as a **lower bound** (`≳10 ppmv`; §IV gives `~10⁻⁵–10⁻³`), so there is
no central value with a symmetric uncertainty to state. Logged as a step-0(a) irregularity: the
step asks for "the central value with its uncertainty" and the literature supplies a bound. C46
had to *invent* its missing uncertainty; here the correct move is to carry the range forward and
report `F_req` across it (§4), not to invent a σ.

## 2. Step 0(b) — the reductions table (the halt)

| # | Team | Photons | Instruments | Reduction / test | Central value | Significance |
|---|---|---|---|---|---|---|
| 1 | Madhusudhan et al. 2023 | 2023 JWST | NIRISS SOSS + NIRSpec G395H | own retrieval | DMS "tentative hint" | `≲2σ` (their own later wording) |
| 2 | Hänni et al. 2024 §1 | same as row 1 | same | characterisation of row 1 | — | **"1σ–2.4σ"** |
| 3 | Schmidt et al. 2025 | **same as row 1** | same | **60 data treatments, >250 retrievals**, multiple pipelines *and* retrieval codes | CH₄ only, `−2.14 ≤ log₁₀ CH₄ ≤ −0.53` | CH₄ `~4σ`; **"no statistically significant or reliable evidence for CO₂ or DMS"** |
| 4 | Madhusudhan et al. 2025 | **new** JWST | MIRI/LRS 6–12 µm | own retrieval suite | DMS and/or DMDS `≳10 ppmv` (`~10⁻⁵–10⁻³`) | **`2.9–3.2σ`**; `3.4σ` vs featureless |
| 5 | Taylor 2025 | **same as row 4** | same | Gaussian-feature suite, 6 tests | flat line preferred in **5/6**, `χ²_ν = 1.06`; `ln B = 1.21` at the DMS/DMDS peak | **`~2σ`**, "no strong statistical evidence" |
| 6 | Luque et al. 2025 | 4 new NIRSpec transits | NIRSpec | independent | CH₄, CO₂ detected; DMS, CH₃SH, N₂O **marginal** | **"none exceeding 3σ … all falling below ~2σ without imposing a strong super-Rayleigh haze"** |

Rows 4 and 5 are the **same MIRI/LRS photons** reduced to a `3σ` detection and to a flat line.
Rows 1 and 3 are the **same NIRISS+NIRSpec photons** reduced to a DMS hint and to no reliable DMS
*or CO₂* — row 3 removes a molecule (CO₂) that row 1 reported at `3σ` and on which the whole
hycean reading rests. The set spans "detected" and "not detected" for the same observable.

**Halt: `NO AGREED OBSERVABLE`.** Everything below §3 is conditional and may not be quoted without
its antecedent.

`0(c)` does **not** apply. Unlike C49's Gale cycle, this observable has been independently
re-reduced — four times over. The failure is the opposite of C49's: not too few reductions, but
reductions that disagree.

## 3. Steps run and steps skipped

Run: `0(a)`, `0(b)`, `0(c)`; then conditionally `1`, `2` (as the identity below), `3`, `4`, `5`,
`6`, `7`, `10`, `11`, `12`. **Skipped: step 8, the energy leg** — this is a mass-budget input, not
a thruster or a generator; `P_useful` and `Δu` are not defined and `Σ` is not formable. Stated
rather than faked, per F9's instruction to skip and say so. **Skipped: step 9, the sign leg** —
`Δu` does not exist here, so it cannot come out negative.

## 4. The identity, and step 5's aperture rows

**`F_req = N_col / τ_photo`** — a steady-state column against first-order photochemical loss.

| Symbol | Value | Provenance |
|---|---|---|
| `M_p` | `8.63 ± 1.35 M⊕` | **VERIFIED**, [ar5iv/2504.12267](https://ar5iv.labs.arxiv.org/html/2504.12267) §I, quoting Cloutier 2019 / Benneke 2019a |
| `R_p` | `2.61 ± 0.09 R⊕` | **VERIFIED**, same |
| `g` | `12.44 m/s²` | **COMPUTED**, `GM/R²` |
| `A_p` | `3.475×10¹⁵ m²` | **COMPUTED**, `4πR²` |
| `µ` | `2.3` | **UNVERIFIED**, solar-composition H₂/He |
| `T` at 1 mbar | `422 (+141 −133) K` | **VERIFIED**, ar5iv/2504.12267 §IV |
| `H` | `123 km` | **COMPUTED**, `RT/(µg)` — reported for scale; the column is written in pressure, so `H` does not enter `N_col` |
| `f_DMS` | `10⁻⁵` nominal, `10⁻⁶–10⁻³` | **VERIFIED**, ar5iv/2504.12267 abstract + §IV |
| `τ_photo` | **`~1 day`** (Earth); few hours–1 day | **VERIFIED-as-quoted**, ar5iv/2504.12267 §IV.2: DMS/DMDS have "very short lifetimes … in the Earth's atmosphere (i.e., between a few hours to `~1 day`)", citing Seager 2013b. **This is an Earth number, not a K2-18 b number** — see §5 |
| Earth marine DMS flux | `28 Tg S/yr → 8.7×10¹¹ mol/yr` | **UNVERIFIED**, mid of the commonly quoted 20–30 Tg S/yr; the weakest input here, and the exponent of the answer does not turn on it |

`N_col(1 bar) = P/(m̄g) = 2.105×10³⁰ m⁻²`; at 10 ppmv, `N_DMS = 2.105×10²⁵ m⁻²`; inventory
`= 1.214×10¹⁷ mol = 7.54×10¹² t`.

**Step 5, the aperture, as a named row.** On a mass-budget input the aperture is the **reference
pressure** to which the retrieved mixing ratio is taken to extend — assumed **1 bar**, the base of
a shallow H₂ envelope. `N_col` is linear in `P_ref`, so the sensitivity is exactly `2A` / `A/2`:

| Aperture | `F_req` (mol/yr) | `A = F_req / F_Earth` |
|---|---|---|
| 2× (2 bar) | `8.87×10¹⁹` | `1.02×10⁸` |
| **nominal (1 bar)** | **`4.44×10¹⁹`** | **`5.08×10⁷`** |
| 0.5× (0.5 bar) | `2.22×10¹⁹` | `2.54×10⁷` |

Every row is `A ≫ 10⁴`. **The exclusion survives the 2× row and is still not an exclusion** — §5.

## 5. The finding: on this input `τ`, not the aperture, is the free parameter

C49 produced F10: on a mass budget the *source* aperture is free and only *sink* rows are
reproducible. **K2-18 b sharpens it in an unexpected direction.** Here the aperture behaves
perfectly — a clean factor of 2 either way, fully reproducible — and the free parameter has moved
into the sink term:

| `τ_photo` | `F_req` (mol/yr) | per-area (cm⁻² s⁻¹) | `A` |
|---|---|---|---|
| 3 h | `3.55×10²⁰` | `1.95×10¹⁷` | `4.06×10⁸` |
| **1 day (Earth)** | `4.44×10¹⁹` | `2.44×10¹⁶` | `5.08×10⁷` |
| 1 yr | `1.21×10¹⁷` | `6.67×10¹³` | `1.39×10⁵` |
| 1 kyr | `1.21×10¹⁴` | `6.67×10¹⁰` | `1.39×10²` |

Six orders of magnitude across a parameter no reduction measures. Part C step 1's diagnostic —
*"if the enumeration returns `A ≫ 10⁴` on an ordinary candidate, go back to step 1"* — **fires
here on every candidate at every aperture**, and the diagnostic is right: `A = 5×10⁷` on a
biological source is not a statement that biology is excluded by seven orders; it is a statement
that Earth's DMS lifetime was imported into an H₂ atmosphere around an M2.5V star where it does
not belong. Madhusudhan et al. 2025 §IV name the three reasons it does not belong — the M-dwarf UV
SED, DMS/DMDS **self-shielding at high column density**, and the absence of an ocean return sink
in the models.

**So the audit's real output is the inversion.** What `τ` closes the books on the `≳20×`-Earth
biogenic flux that Madhusudhan 2025 quotes (from Tsai et al. 2024) as sufficient?

```
τ_req = inventory / (20 · F_Earth) = 1.214e17 / 1.74e13 = 6.95e3 yr     (10 ppmv)
                                                        = 6.95e5 yr     (1000 ppmv)
```

**`τ_photo ≥ 6.95×10³ yr`, a factor `2.5×10⁶` over Earth's DMS lifetime.** That is a number a
photochemical model reports and a laboratory cross-section constrains. It is the C53 move applied
to a different case: the residual tightens from a statement about a planet to a statement about a
measurable coefficient.

## 6. Step 10 — the enumeration

Per F10 every **source** row on a mass-budget input is `NOT DISCRIMINATED`, not `SURVIVES`.

| # | Reservoir | Source + bound | `A` | State |
|---|---|---|---|---|
| 1 | **Gas-phase photochemistry from CH₄ + H₂S** | Reed et al. 2024 (`10.3847/2041-8213/ad74da`), lab: DMS `0.39–0.81 ppmv` from 20 ppmv H₂S **without** CO₂; `0.04–0.06 ppmv` **with** CO₂ | `12.3` (no CO₂) / **`167`** (with CO₂) at 10 ppmv; `1.2×10³` / `1.7×10⁴` at 1000 ppmv | **`RULED OUT`** — and *aperture-free*, because Reed's bound is a **mixing ratio**, not a flux. CO₂ is reported abundant (`~1%`), so `167` is the operative row. Two squeezes from one source: DMS production also needs H₂S, which **no reduction detects** |
| 2 | **Cometary / meteoritic delivery** | Hänni et al. 2024: DMS/methanol `= (0.13 ± 0.04)%` at 67P — the first abiotic DMS identified anywhere | — | **`NOT TESTED`**. The composition is measured; the **delivery rate** to K2-18 b is in none of the brief's sources. Say which: an infall mass flux in kg/yr |
| 3 | **Interior outgassing** | no brief source bounds a K2-18 b sulfur outgassing flux | — | **`NOT TESTED`** |
| 4 | **Biogenic ocean flux** | Tsai et al. 2024 *via* Madhusudhan 2025 §I/§IV: `10⁻²` reachable at `≳20×` Earth levels | `2.5×10⁶` on `τ_Earth`; **`≈1` at `τ = 6.95×10³ yr`** | **`NOT DISCRIMINATED`** (F10). Its `A` is a statement about `τ`, not about a biosphere; it "passes" only on the model's own self-shielded lifetime |
| 5 | **The laboratory frame — the cross-sections** | Madhusudhan 2025 §IV: DMS/DMDS cross-sections exist only "for an Earth-like atmosphere at nearly STP conditions, using N₂ as a broadener" | — | **Not a reservoir.** F5-adjacent: a property of the retrieval, not of the planet. Logged because it can move `f_DMS` and therefore every row above |

**Step 11 residual, conditional.** *If* DMS/DMDS at `≳10 ppmv` were real on K2-18 b, then **of the
reservoirs considered**, gas-phase CH₄/H₂S photochemistry is excluded by `167×` in mixing-ratio
space independently of any aperture, and what remains is a source of `≥4.4×10¹⁹ mol/yr` **or** a
photochemical lifetime of `≥6.95×10³ yr` — `2.5×10⁶ ×` Earth's — with the two trading off exactly.
**The residual is a demand on `τ`, and `τ` is the quantity nobody has measured.**

## 7. Against Venus and Mars

| | Venus PH₃ ([[C30-venus-phosphine-audit]]) | Mars CH₄ ([[C49-mars-methane-audit]]) | **K2-18 b DMS (here)** |
|---|---|---|---|
| Step-0 state | `NO AGREED OBSERVABLE` | four states at once | **`NO AGREED OBSERVABLE`** |
| Blind | contaminated (halt pre-announced) | single-agent | **two-agent, uncontaminated** |
| What disagrees | passband polynomial order | one pipeline vs a re-reduction | **feature test vs retrieval, on the same photons** |
| Free parameter | source aperture | source aperture (F10) | **`τ`, the sink** |
| Reproducible exclusion | none quotable | one *sink* row (`A = 319`) | one **mixing-ratio** row (`A = 167`), aperture-free |
| Residual | a conditional flux | `EXCHANGE REQUIRED` | conditional: a **lifetime** |

The three cases now sit at three distinct places on the same halt. Venus's disagreement lives
inside one team's calibration; Mars's between two epochs of instrument; **K2-18 b's between two
statistical questions asked of one spectrum** — *does a retrieval prefer this molecule* and *does a
Gaussian beat a flat line* — which is a failure mode neither Venus nor Mars exhibits and which
F8's current wording ("independent reductions") only barely covers. Proposed as an F8 amendment in
the Part D text carried in `vault/PENDING-log-C54.md`: a reductions table must list
**feature-significance tests** alongside retrievals, because a retrieval preference and a feature
detection are not the same observable, and the audit will otherwise tabulate half the set and
believe it has tabulated all of it.

## 8. Honesty

**Two-agent blind, and what it does and does not establish.** A different agent wrote the brief and
did not run the audit; this agent ran the audit and read no vault note, no scout report and no
computed note until §1–§6 were complete. The brief carries **no verdict word** — checked by reading
it. Its hash matched. This is the first datum satisfying D.3a's protocol in full, and it answers
the question C46 and C50 left open, in the *opposite* direction from C46: **the instrument halts
unprompted on a real, contested case.**

**What the vault expected, read only at step 4.** `audits/scout-03-astrobiology.md` line 24 calls
K2-18 b "the case the audit should publicly refuse to run", and its table row reads
*"No — features consistent with noise … Run as a 2-hour `NO OBSERVABLE` demonstration only."*
**The direction matched; the state did not.** The scout predicted a step-0(a)
`NO OBSERVABLE TO EXPLAIN`. The blind run returns a step-0(b) **`NO AGREED OBSERVABLE`**, because
the claim row is `2.9–3.2σ` and does *not* contain zero — `0(a)` passes on it. These are exactly
the pair D.3 §"Not D.2" warns are easily confused, and the vault's own advance guess confused
them. **That disagreement is worth more than agreement would have been**: an announced halt would
have been contaminated, and the announced halt was the wrong one.

**Recognition.** I recognised the case immediately and unprompted — K2-18 b is famous, and the
brief names the planet, the molecule and Madhusudhan. What I knew before fetching: that a DMS
claim exists, that it is disputed, and that Madhusudhan is its proponent. What I did **not** know
and got only from the sources: the `2.9–3.2σ` figure, Taylor's 5-of-6 flat-line result, Schmidt's
60-treatment reanalysis removing CO₂ as well as DMS, Reed's ppmv ceilings, Hänni's `0.13%`, and
every number in §4–§6. **Recognition is a real contaminant here and the two-agent design does not
neutralise it.** The next D.3-class blind should use a case the runner cannot name.

**What I fetched.** Crossref metadata for all nine brief DOIs (`api.crossref.org`, 2026-09-05).
Full text: ar5iv/2504.12267 (Madhusudhan 2025). Abstracts: Taylor 2025 (IOP), Schmidt 2025 (arXiv),
Luque 2025 (arXiv), Hänni 2024 (IOP), Reed 2024 (IOP).

**What I could not get.** (a) **Tsai et al. 2024's own paper.** The brief's Tsai DOI,
`10.3847/2041-8213/ad1405`, resolves via Crossref to *"Day–Night Transport-induced Chemistry and
Clouds on WASP-39b: Gas-phase Composition"* — a different planet, and not a DMS paper. The Tsai et
al. 2024 that carries the `≳20×`-Earth result is a different work, cited by Madhusudhan 2025 but
not identified by DOI in the brief. **This is a defect in the brief**, logged not fixed; every Tsai
number in §5–§6 is therefore **SECONDARY**, quoted from Madhusudhan 2025's text *about* Tsai, and
the `τ_req = 6.95×10³ yr` inversion should be re-run against Tsai's own flux once the correct DOI
is supplied. (b) A K2-18 b-specific `τ_photo` from any brief source — none publishes one, which is
exactly why §5 is the finding rather than a caveat. (c) Schwieterman et al. 2018's Earth DMS flux;
the `28 Tg S/yr` in §4 is **UNVERIFIED** and is this note's weakest input.

**Single runner.** One agent, one pass, no independent re-derivation of the arithmetic. The script
is committed so that the next reader can disagree with a number rather than with a claim.

See [[reservoir-audit]], [[C30-venus-phosphine-audit]], [[C49-mars-methane-audit]],
[[C53-mars-exchange-feasibility]], [[C28-biosignature-roc]],
[[C46-reservoir-audit-negative-control]], [[C50-reservoir-audit-d2-control]].
