---
name: PENDING-log-C54
type: method
---

# PENDING — proposed text for C54

Not linked from `00-index.md` by instruction. Two blocks: a `vault/log.md` entry to be prepended,
and proposed Part D / F-list text for `vault/method/reservoir-audit.md`. **Neither is applied
here** — this runner was scoped not to edit `reservoir-audit.md` or `log.md`.

---

## Block 1 — proposed `vault/log.md` entry (newest first)

```
## [2026-09-05] verification | K2-18 b DMS halts at step 0(b), not 0(a): the first uncontaminated two-agent blind, and the vault's advance guess named the wrong halt

C54-k2-18b-audit. Brief written by a different agent, archived and hashed before dispatch
(audits/blind-brief-c54-2026-09-05.md, sha256 ec039762abc96170a570932a69886e2c905e5eb5af6041c4bbc91605a0c3d840,
verified by the runner over the content above the hash line before any source was fetched). The
runner read reservoir-audit.md and the brief only, ran Part C step 0, and read no vault note until
after the enumeration was written.

WHAT WAS EXPECTED: audits/scout-03-astrobiology.md called K2-18 b "the case the audit should
publicly refuse to run" and specified a "2-hour NO OBSERVABLE demonstration" — i.e. a step-0(a)
halt, NO OBSERVABLE TO EXPLAIN.

WHAT THE BLIND RUN RETURNED: a step-0(b) halt, NO AGREED OBSERVABLE. 0(a) does not fire:
Madhusudhan et al. 2025's MIRI/LRS claim is 2.9-3.2 sigma and its interval does not contain zero.
What fires is the reductions table — Taylor 2025 re-tests the SAME MIRI photons as Gaussian
features and prefers a flat line in 5 of 6 tests (chi2_nu = 1.06, ~2 sigma); Schmidt et al. 2025
re-reduces the SAME NIRISS+NIRSpec photons through 60 data treatments and >250 retrievals and
finds no reliable DMS or CO2; Luque et al. 2025 finds nothing above 3 sigma. The set spans
detected and not-detected.

WHY IT MATTERS: 0(a) and 0(b) are exactly the pair reservoir-audit D.3 section "Not D.2" warns are
easily confused, and the project's own advance guess confused them. The error is in the scout
report, not in the instrument. D.3a is now satisfied in full for the first time: brief hashed
before dispatch, written by a different agent, carrying no verdict word, and the runner halted
unprompted. C30's halt was pre-announced; C46's and C50's blinds were single-agent.

WHAT PRODUCED THE NEW NUMBERS: vault/_scripts/c54_k218b.py, from the identity
F_req = N_col / tau_photo. Planet parameters M = 8.63 +/- 1.35 M_earth, R = 2.61 +/- 0.09 R_earth
and photospheric T = 422 (+141 -133) K at 1 mbar all VERIFIED from ar5iv/2504.12267 fetched
2026-09-05. Conditional result: inventory 1.214e17 mol (7.54e12 t) above 1 bar at 10 ppmv,
F_req = 4.44e19 mol/yr at Earth's DMS lifetime (~1 day, VERIFIED-as-quoted from the same source),
= 5.08e7 x Earth's marine DMS flux. Aperture rows 1.02e8 / 5.08e7 / 2.54e7 at 2x / 1x / 0.5x the
1 bar reference — a clean factor of 2, fully reproducible.

CORRECTION TO THE SHAPE OF F10, NOT TO ITS CONTENT: F10 says the SOURCE aperture is the free
parameter on a mass-budget input. On K2-18 b the aperture is not free at all and the SINK is:
F_req spans six orders of magnitude (A = 4.06e8 to 1.39e2) across tau = 3 h to 1 kyr, and no
reduction measures tau. Step 1's own A >> 1e4 diagnostic therefore fires on every candidate at
every aperture, and it is right to: A = 5e7 on a biological source is Earth's DMS lifetime
imported into an H2 atmosphere around an M2.5V star. The audit's real output is the inversion:
tau_photo >= 6.95e3 yr, a factor 2.5e6 over Earth's DMS lifetime, for the >=20x-Earth biogenic
flux Madhusudhan 2025 quotes (from Tsai et al. 2024) to close the books.

ONE APERTURE-FREE EXCLUSION SURVIVES: Reed et al. 2024's laboratory ceiling is a MIXING RATIO, not
a flux, so it needs no aperture. DMS reaches 0.39-0.81 ppmv from 20 ppmv H2S without CO2 and
0.04-0.06 ppmv with CO2; against the required 10 ppmv that is A = 12.3 and A = 167. CO2 is
reported abundant, so 167 is operative. Gas-phase CH4/H2S photochemistry RULED OUT. Every other
source row is NOT DISCRIMINATED (F10) or NOT TESTED (no delivery rate for comets, no outgassing
flux, in any brief source).

DEFECT IN THE BRIEF, LOGGED NOT FIXED: the brief's Tsai DOI 10.3847/2041-8213/ad1405 resolves via
Crossref (fetched 2026-09-05) to "Day-Night Transport-induced Chemistry and Clouds on WASP-39b:
Gas-phase Composition" — a different planet and not a DMS paper. The Tsai et al. 2024 carrying the
>=20x-Earth result is a different work, cited by Madhusudhan 2025 but not identified by DOI
anywhere in the brief. Every Tsai number in C54 is therefore SECONDARY, quoted from Madhusudhan
2025's text about Tsai, and the tau_req inversion must be re-run against Tsai's own flux once the
correct DOI is supplied.

STILL WEAK: recognition. The runner recognised K2-18 b immediately and unprompted; the brief names
the planet, the molecule and Madhusudhan. The two-agent design removes pre-announcement but not
recognition. Single runner, one pass, no independent re-derivation. Earth's marine DMS flux
(28 Tg S/yr) is UNVERIFIED and is the note's weakest input.
```

---

## Block 2 — proposed Part D text for `reservoir-audit.md`

To be inserted as **D.3b**, immediately after D.3a:

> ### D.3b — the first uncontaminated blind, and it named a different halt than the project expected
>
> **RUN 2026-09-05: [[C54-k2-18b-audit]], K2-18 b DMS/DMDS.** The first run satisfying D.3a in
> full: brief written by a **different agent**, archived and hashed before dispatch
> (`audits/blind-brief-c54-2026-09-05.md`, sha256
> `ec039762abc96170a570932a69886e2c905e5eb5af6041c4bbc91605a0c3d840`, verified by the runner
> before any source was fetched), **carrying no verdict word**, and the runner forbidden to read
> any vault note until after the enumeration was written. The instrument **halted unprompted**:
> step 0(b), `NO AGREED OBSERVABLE`.
>
> **And it halted at a different step than the project had guessed.**
> `audits/scout-03-astrobiology.md` predicted a step-0(a) `NO OBSERVABLE TO EXPLAIN` — "features
> consistent with noise". `0(a)` in fact **passes**: Madhusudhan et al. 2025's MIRI/LRS claim is
> `2.9–3.2σ` and its interval does not contain zero. What fires is the reductions table. **The
> pair D.3 §"Not D.2" warns are easily confused were in fact confused, by this project, in
> advance** — which is the strongest available evidence that the two states are doing distinct
> work and that the table, not intuition, is what separates them.
>
> **What D.3 is still missing after C54: recognition.** The case is famous and the brief names the
> planet, the molecule and the claimant; the runner recognised it at once. A two-agent blind
> removes pre-announcement, not recognition. The next D.3-class case must be one the runner
> **cannot name** — a contested reduction in a low-profile system, briefed in units only.

To be appended to the D.4 output-state table as a fourth data row:

> | `NO AGREED OBSERVABLE` (D.3) | step 0(b) halt | [[C54-k2-18b-audit]] | **the reductions table only** | first **uncontaminated** blind; two-agent, hashed, no verdict word — and the halt the project had predicted was the wrong one |

---

## Block 3 — proposed F-list text for `reservoir-audit.md`

**F8 amendment** — append to the existing F8 paragraph:

> **Amended 2026-09-05 by [[C54-k2-18b-audit]]: the reductions table must list
> feature-significance tests alongside retrievals.** K2-18 b's disagreement is not between two
> retrieval pipelines but between **two different statistical questions asked of one spectrum** —
> *does a retrieval prefer this molecule against a model grid* (Madhusudhan 2025: `2.9–3.2σ`) and
> *does a Gaussian beat a flat line at the same wavelengths* (Taylor 2025: flat line preferred in
> 5 of 6 tests, `χ²_ν = 1.06`). These are not the same observable, and a table that lists only
> retrievals will record unanimity where none exists. Row 3 of C54's table sharpens it further:
> Schmidt et al. 2025's 60-treatment reanalysis of the **same** NIRISS+NIRSpec photons removes
> **CO₂** as well as DMS — a molecule the 2023 paper reported at `3σ` and on which the entire
> hycean reading rests — so the spanning set is not confined to the disputed molecule.

**F11, proposed and new** — the sink counterpart to F10:

> **F11 — on a mass budget the *lifetime* can be freer than the aperture, and step 5 does not
> test it.** Found by [[C54-k2-18b-audit]] (2026-09-05). F10 located the free parameter in the
> **source aperture** and prescribed a sensitivity row at 2× and 0.5×. On K2-18 b that row is
> perfectly behaved — `A = 1.02×10⁸ / 5.08×10⁷ / 2.54×10⁷`, a clean factor of two — and the
> instrument is nonetheless carrying six orders of magnitude of freedom, all of it in `τ`:
> `A = 4.06×10⁸` at `τ = 3 h` and `1.39×10²` at `τ = 1 kyr`, and **no reduction measures `τ`**.
> Step 5 makes the aperture reproducible and says nothing about the sink timescale, so an analyst
> who honours step 5 in full can still move `A` by `10⁶` by importing a lifetime from the wrong
> planet — which is exactly what happens if Earth's `~1 day` DMS lifetime is used for an H₂
> atmosphere around an M2.5V star where self-shielding is the whole point.
> **Rule: where `F_req = N_col/τ`, `τ` is a named row with its own 2×/0.5× sensitivity and its own
> provenance line, and if no source measures `τ` for *this* system, do not report an `A` at all —
> invert and report the required `τ` instead.** C54's output is that inversion:
> `τ_photo ≥ 6.95×10³ yr`, `2.5×10⁶ ×` Earth's, a number a photochemical model reports and a
> laboratory cross-section constrains. **Corollary, and the reason this is F11 rather than a
> footnote to F10: the step-1 `A ≫ 10⁴` diagnostic is a detector for a mis-specified `τ` just as
> much as for a mis-specified observable**, and C54 is the case that separates the two — the
> observable was correctly specified and `A` was still `10⁷·⁵`.
