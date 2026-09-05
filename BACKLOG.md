# Merged backlog — 2026-09-05

**Status 2026-09-05 (after rounds 1–2):** ✅ done and committed, ⚠ partial. Rounds: `aa0f842` (round 1), `60beb4a` (round 2), round 3 = this commit.

**Round 4 (applied):** C11 aperture rows, `expected` blocks with fetched N_universe (G28 100,685; G6 13,830; G25 void, floor binds), information-audit Part C design, G28 5-vs-8 reconciled, Q5 mechanism corrected. Preprint draft in `papers/charnov-gittins/`. **Open follow-ups:** run the Kadmon 1992 test of C25; refs.bib has 12 unverified DOIs; abstract is 216 words.

Five Opus 4.8 audits (math/physics, sources, method, structure, scope). ~130 raw actionables, merged and deduplicated to 62. Grouped into batches an agent can run as one job. Effort: S = under 1 hour, M = a few hours, L = a session.

Full reports sit next to this file: `01-math-physics.md` … `05-scope-strategy.md`.

---

## Headline findings (what the audits agree on)

1. **The arithmetic is clean. The pull-quotes overclaim.** ~60 numbers recomputed, all reproduced. Defects are in the step from a correct number to the headline sentence.
2. **The vault's flagship correction is itself wrong.** "578 was wrong, 595 is right" — Crossref's deposited reference count for RMP 90:031001 is exactly 578. Two objects, not a hallucination. The same error class is live now in G19 vs its theorem note.
3. **Evidence grades are not reproducible.** No citation-intersection gap names anchor DOI + provider + endpoint + date + N + coverage. G25 ("strongest finding") has 28% coverage against G6's own 77–100% bar.
4. **Canonical drift.** FINDINGS.md still uses the retired verdict vocabulary and contradicts vault standings on six gaps. METHOD.md §11 same. README counts all stale. `_idx.py` does not exist. G21 listed twice.
5. **No negative controls** on the specification instruments. Step 4 always returns a spec.
6. **Owner's wider interests are absent** from the vault (no circularity, resilience, biosignature source cited). Four instruments map directly onto them.
7. **Zero bridges have been exploited into a prediction.** Strategy note diagnosed this, nothing schedules it.

---

## Batch A — Corrections to computed notes (math/physics)
All edits stay inside one note each. Log every change in `vault/log.md`.

| # | File | Task | Done | Effort |
|---|---|---|---|---|
| A1 ✅ | `vault/computed/C11-flyby-reservoir-audit.md` | Add Oberth factor: Δv_p = 7.24 mm/s, F_req = 0.53–4.87 mN; propagate 1.86× to every A; headline → 0.5–5 mN | No verdict flips; headline updated | S |
| A2 ✅ | same | Fix charge shortfall: Q ≈ 3 mC, ~6.5 orders (not 3 C, 10 orders) | Consistent with A ≈ 3×10⁶ | S |
| A3 ✅ | same | Fetch NEAR declinations from Anderson 2008 PRL 100:091102; re-run 13.28 vs 13.46 check | Values sourced or check deleted | S |
| A4 ✅ | `vault/computed/C8-momentum-harvesting-metric.md` | Resolve Σ_sail = v/c vs 2v/c; fix IKAROS "agrees" sentence | Closed form and row agree | S |
| A5 ✅ | same | Delete the "Σ_drag ≤ 1/3" bound; state it is the power optimum; weaken "reproduces all four" to three | No 1/3 ceiling claim | S |
| A6 ✅ | same | Insert AM-GM ½ into P_available; recompute Σ_albatross (~3.0×10⁻²) and eq. (3); re-check minimum-shear recovery | §3.4 confirmed or restated as order-of-magnitude | M |
| A7 ✅ | same | Source albatross L/D (currently 20, unverified) | Fetched primary | S |
| A8 ✅ | `vault/computed/C6-damage-healing-ratio.md` | Remove "Ha = 1 is collapse" framing; steady state is globally stable for all Ha > 0 | No "over the line" sentence | S |
| A9 ✅ | same | Add queueing prior art: 1/Ha = offered load ρ of M/M/1/1; A = Erlang-B complement. Adjust "no cross-domain name" claim | Row exists with verdict | M |
| A10 ✅ | same | Symbol-collision note (Ha = Hartmann number) | Reader cannot confuse | S |
| A11 ✅ | `vault/computed/C4-inclination-sensing-limit.md` | Wedge gives tan θ not sin θ; valid only θ ≲ 24°; qualify "microscopic origin of sine law" | Breakdown angle stated | S |
| A12 ✅ | same | Rewrite Boltzmann cross-check; delete "two independent routes agree" | No such claim | S |
| A13 ✅ | same | Impose N_ind = max(1, τ/τ_c); regenerate §5 table; band → ~7.6–12.1°; update §8 and pull-quote | No row with N_ind < 1 | M |
| A14 ✅ | same | Relabel §11.6 absolute θ_min as optimistic upper bound; keep 1.73 vs 3.00 as load-bearing | §11.6 and §11.8 agree | S |
| A15 ✅ | `vault/computed/C19-hormesis-biphasic-fit.md` | Rename "≥15× window" to "tested range, all beneficial"; drop from "meets or exceeds" verdict | Pull-quote fixed | S |
| A16 ✅ | same | Refit with a form that has correct coverage→0 asymptote, e.g. Nf = N₀(1 + a·c·e^{−bc}); or restrict to descending limb | Physically admissible fit | M |
| A17 ✅ | same | Label AISI 4140 numbers σ'_f-equivalent; "+82%" → "best of two doses"; fix "straddles 30–60%" | Axis mismatch stated | S |
| A18 ✅ | `vault/computed/C12-pi-space-lattice.md` | Demote SNF claim: crossovers parallel because ν, D, α share L²T⁻¹; no SNF computed | Reduced to footnote or backed | M |
| A19 ✅ | `vault/computed/C16-same-class-catalogue.md` | Add Clopper-Pearson 95% upper bound 0.16 on P(new physics); delete "bias-immune" sentence | Verdict quotes an interval | S |
| A20 ✅ | same | Write SAME-CLASS rule as explicit decision procedure; re-apply blind to 24 rows + 3 excluded candidates | Table with count of changed assignments | L |
| A21 ✅ | same (or new `vault/predictions.md`) | Pre-register class for the 7 open + 4 ambiguous cases, dated | Append-only block linked from Q7 | S |
| A22 ✅ | `vault/computed/C1-availability-living-tissue.md` | Rebuild with inputs + arithmetic + source per row; bone → C6 bands (0.726–0.952); mark cortical 0.984 unsupported | Every number reproducible; no contradiction with C6 | M |
| A23 ✅ | same | Replace "leaf less available than a power grid" headline; note 10⁸ redundancy | Headline compares like with like | S |
| A24 ✅ | `vault/computed/C2-probabilistic-safety-factors.md` | State operating point (SF=3, V_R=0.20); add V_R=0.10 sensitivity (~5 orders, not half) | Sensitivity line present | S |
| A25 ✅ | `vault/computed/C9-moving-coupling-point.md` | Rename ZT_Schur vs ZT_eff; add the identity that maps them | Eq. 6 and 8 reconciled in equations | M |

## Batch B — Provenance and sources

| # | File | Task | Done | Effort |
|---|---|---|---|---|
| B1 ✅ | `FINDINGS.md`, `METHOD.md` §2, `vault/log.md`, `vault/method/co-citation-audit.md`, `vault/gaps/G4-criticality-as-design.md` | Rewrite 578/595: Crossref deposited = 578, printed = 595, different objects; real defect was an unattributed number | No file says 578 was "wrong" | M |
| B2 ✅ | `vault/gaps/G19-safety-factor-derived-twice.md`, `vault/theorems/stress-strength-interference.md` | Reconcile Alexander-1997 count (OpenAlex = 46, 2026-09-05) and "753 works"; name provider + date | Files agree | M |
| B3 ✅ | `vault/gaps/G25-proofreading-coding.md` | Add Provenance block: Hopfield DOI `10.1073/pnas.71.10.4135`, Shannon DOI, provider, endpoint, date; surface 28.4% coverage | 1,463 / 416 / 16 re-derivable | S |
| B4 ✅ | same | Re-run intersection via OpenCitations COCI to raise coverage >70% | Two providers recorded | M |
| B5 ✅ | `vault/gaps/G28-marginal-value-gittins.md` | One table of (provider, endpoint, date, N) for Gittins citers incl. Crossref 986; say which denominator 0.49% uses; add Auer 2002 DOI and 22.2% control query | Numbers reconstructable | S |
| B6 ✅ | same + `vault/00-index.md` + `vault/log.md` | Locate "Griebling 2026 Animal Behaviour" via Crossref; else mark UNLOCATED everywhere | No file asserts it as established | S |
| B7 ⚠ (Bailey fixed; 279→6 enumeration unrecoverable) | `vault/gaps/G17-overconfident-uncertainties.md` | State screening 279 → 6 with DOIs; fix Bailey *Not Normal* = R. Soc. Open Sci. 4:160600 (2017) | Six enumerable | M |
| B8 ✅ | `vault/gaps/G21-dimensionless-regime-map.md` | Vogel edition + page for three quotes; source or strike Ortega Π values | No quote without locator | M |
| B9 ✅ | `vault/gaps/G8-energy-per-bit-axis.md`, `G27-collective-decision.md` | Add host + date behind 575 / 26 / 551; re-test under citation intersection before "overturned" stands | Retraction meets assertion bar | M |
| B10 ✅ | `vault/gaps/G6-multifunctionality.md` | Provider + endpoint + date on six-pairing table and "9,570 hits" | Fully reproducible | S |
| B11 ✅ | `vault/gaps/G7-how-passive.md` | Complete the rate-limited citer trace via Crossref/OpenCitations/Europe PMC | Standing updated | S |
| B12 ✅ | `vault/disclosure-ledger.md` | Per-row `fetched` date column; row 24 Apollo → SECONDARY (PURSUE 403'd; TIME foregrounds Gemini 7); fix header 24 vs summary 22 totals | Tier matches evidence held | M |
| B13 | `vault/gaps/` (new template) | EVIDENCE BLOCK template modelled on `vault/sources/*.md` headers; apply to G6, G17, G19, G25, G28 | Five CI gaps carry it | L |
| B14 | whole vault | `grep -rnE '\b[0-9][0-9,]{2,} (citers|citations|works|papers|hits|references)\b'`; attach provider + date or mark UNSOURCED | No bare count survives | L |
| B15 ✅ | `vault/log.md` | Log this audit's two contradictions (Crossref 578; OpenAlex 46) | Corrections-of-corrections traceable | S |
| B16 | `vault/computed/*`, `vault/theorems/*` | Split VERIFIED into VERIFIED-PRIMARY / VERIFIED-SECONDARY; re-tag C19 Dataset B, C11 Anderson values, C5 Gittins/Whittle | One tag per provenance grade | L |

## Batch C — Method and epistemics

| # | File | Task | Done | Effort |
|---|---|---|---|---|
| C1 ✅ | `vault/method/citation-intersection.md`, `positive-controls.md`, each CI note | Add null model: expected co-citers = |A|·|B|/N; report observed/expected; restate control table in same units | Every CI note has `expected` | M |
| C2 ✅ | `vault/method/failure-modes.md`, `METHOD.md` §11 | Add failure mode 6: diachronic terminology drift, with specimen | Present in both | S |
| C3 ✅ | same | Rule: a string count cannot overturn a gap without host + query + date; cite G8/G27 | Rule written | S |
| C4 | `vault/moves/M1..M5-*.md` | Add `falsifier:` frontmatter + one pre-registered counterexample search each | Five falsifiers | M |
| C5 | new `vault/computed/C23-reservoir-audit-negative-control.md` | Feed (a) fully-accounted device (Betz-calibrated turbine), (b) fabricated zero-consistent thrust report; record whether audit returns nothing | Input class on which audit returns nothing stated | M |
| C6 | `vault/method/information-audit.md` | Part C: negative control + one blind (pre-registered) case | Both results recorded | M |
| C7 ✅ | `vault/method/reservoir-audit.md` | Rename Part B (hard-positive, not negative); add mandatory aperture-assumption row with A at 2× and 0.5×; retrofit C11 | Step numbered, C11 updated | S |
| C8 | `vault/method/what-closes-a-gap.md`, each live/narrowed gap | Review-sweep subsection: two most recent reviews per side read, ABSENT recorded, dated | Each live gap has it | L |
| C9 | `vault/method/precedent.md` | Add Arrowsmith, SemMedDB open/closed discovery, LION-LBD, embedding/KG LBD; re-derive "what survives" table | Table re-derived | M |
| C10 | new `vault/computed/C24-timeslice-validation.md` | LBD-standard retro-test: rebuild citation universe at a cut-off year for a gap that later closed; hit or miss | Result stated with cut-off | L |
| C11 | `vault/_lint.py`, `relationship-description.md`, withdrawn/overturned notes | `withdrawal-evidence:` field; lint it ≥ original evidence grade | Lint rejects weak withdrawals | M |
| C12 | `vault/novelty-audit.md` | Humility rule as procedure: NOVEL requires ≥N query formulations, count recorded per note | Each NOVEL carries search count | M |
| C13 | `vault/method/press-feel-dig.md` | Split: keep tasking rule as method; move map-runs-territory claim to a framing note marked aesthetic | Method note has only evidenced rules | S |
| C14 ✅ | `vault/method/evidence-lanes.md`, `disclosure-ledger.md` §4 | State the condition under which an institutional null (AARO) becomes a verdict | Named checkable condition | S |
| C15 ✅ | `vault/method/specification-instruments.md` | Q7 "11/11" → C16 numbers (24 cases, 17 closed, 16/1/0) | Matches C16 | S |
| C16 ✅ | new `vault/predictions.md` | Append-only home for α, tenth-order QED coefficient, C4 pooling, C16 classes; real timestamps + content hash | Timestamps not all identical | S |

## Batch D — Structure, tooling, agent-readiness

| # | File | Task | Done | Effort |
|---|---|---|---|---|
| D1 ✅ | new `vault/_idx.py` | Generate gaps block from frontmatter between sentinels in `00-index.md`; idempotent; dedupes G21 | 20 gaps once each | M |
| D2 ✅ | `vault/_lint.py` | `--idx-check` mode: fail if index block differs from generated | Lint catches hand edits | S |
| D3 ✅ | `vault/_lint.py` | Tag-consistency rule (`evidence/`, `standing/`, `crosses/` tags match fields) | 3 errors before D4 | S |
| D4 ✅ | `G4`, `G6`, `G9` | Fix the three desynced tag lines | Lint passes | S |
| D5 ✅ | `vault/sources/*` + `_lint.py` | Strip BOM from three source files; lint BOM-checks `sources/`; add `source` to TYPES with `tier`, URL, date-fetched checks | Sources lint as a real type | S |
| D6 | `vault/_lint.py` | Per-type required fields: computed `closes`, `last-checked`, `result`; move `used-by`; theorem `era`, `read-status`; coverage required on CI gaps; size warning at 15 KB + lead callout | ~25 bare notes flagged then filled | L |
| D7 ✅ | `vault/computed/*` | Backfill `last-checked` from `git log --diff-filter=A` | Populated without guessing | S |
| D8 | `vault/gaps/*`, `_lint.py` | `sources:` list (DOIs), required on CI gaps; `retrieved:` per evidence block; backfill G6/G17/G19/G25/G28 | Machine-readable provenance | M |
| D9 | `vault/_lint.py` | Reciprocal-edge check: gap `computed-in` ↔ computed `closes` | Bidirectional enforced | M |
| D10 ✅ | new `CLAUDE.md` | Canonical = `vault/00-index.md`; lint before commit; closed vocabularies verbatim; corrections logged never silently fixed; commit subjects state result; pre-commit command | Cold agent can make a compliant edit | M |
| D11 ✅ | new `vault/_templates/gap.md`, `computed.md` | Full frontmatter with legal values in comments | Copy-fill is lint-clean | S |
| D12 ✅ | `CLAUDE.md` or `vault/method/` | "How to add a gap" recipe (three-part test, control, template, six fields, STANDING line, index, lint, idx) | References only existing files | S |
| D13 | `vault/method/citation-sources.md` | Executable "Run a citation intersection" recipe with exact endpoints and the two known API traps (`/citation-count/` bogus 1; `?select=reference` 400s) | Agent can run end to end | M |
| D14 ✅ | `FINDINGS.md` → `ARCHIVE-findings-2026-09.md` | Rename, add superseded header; migrate corrections log into `vault/log.md`; update README/VISION links | No doc presents FINDINGS as current | M |
| D15 ✅ | `METHOD.md` | Reconcile §11 with vault standings (delete retired-vocab table); fix 13σ → ~9.9σ, "five moves" → six, "three cases" → four; account for G10, G13–16, G18, G24, G26 | No retired labels; every G-number 1–28 is a file or logged retirement | M |
| D16 | `vault/gaps/` | Tombstone notes for the 8 dropped IDs with `standing: retired` + `exit:` reason | 28 contiguous IDs | M |
| D17 | `METHOD.md` | Reduce to router pointing at vault notes (<8 KB) | No duplicated section | L |
| D18 ✅ | `README.md`, `VISION.md` | Fix counts (91 notes, 77 nodes, six HTML); "24 times" → real count with source; "six unread theorems" → C13's four + kedem-caplan | No number contradicts filesystem | S |
| D19 | `vault/method/citation-intersection.md` | "Eight surviving gaps" → pointer to `triage.base` view (true count 12) | No hardcoded count | S |
| D20 ✅ | `.gitignore` | Add `vault/.obsidian/workspace*.json`, `.DS_Store`, `Thumbs.db`, `*.tmp`, `*.bak`; `git rm --cached` workspace.json | Status clean after Obsidian | S |
| D21 | six `*.html` + `README.md` | Stamp each with `<!-- snapshot @ sha, date -->`; document `inquiry-map.html` server-side notes DB; add session-close export to `vault/map-notes.json` | README no longer implies repo is complete | M |
| D22 | `vault/sources/src-2023-house-oversight-uap-hearing-transcript.md` | `## Extract index` of cited passages with line ranges | 40 lines instead of 158 KB | M |
| D23 | `vault/log.md` | Split into `vault/log/YYYY-MM.md` with index | No log >15 KB | M |
| D24 ✅ | new `check.ps1` | Runs lint, idx-check, link check | One command verifies repo | S |
| D25 ⚠ (schema only, fields not populated) | `vault/triage.base`, `_lint.py` | Add `exit:` (prediction/computation/experiment/specification/none-yet), `extends-to:` (astrobiology/ecology/circularity/conservation/sustainability/none), `next-step-cost:` fields; populate all gaps and questions | Bases view sorts by expected value | M |

## Batch E — Scope and new threads (the growth work)

| # | File | Task | Done | Effort |
|---|---|---|---|---|
| E1 ✅ | `README.md`, `VISION.md`, `vault/strategy.md` | Rewrite frame paragraph: cross-domain synthesis reaching checkable science; ecology, circularity, conservation, astrobiology named in scope under the same rule | Scope stated without weakening rule | S |
| E2 | `vault/disclosure-ledger.md`, `testimony-taxonomy.md`, `symbol-display-testimony.md`, `00-index.md` | Freeze banner: retained as worked example of evidence-lane discipline; closed as research thread | Index no longer lists it as active | S |
| E3 ✅ | `vault/computed/C5-charnov-gittins.md`, `novelty-audit.md` | Obtain Houston & McNamara 1999 and Gittins-Glazebrook-Weber; grep for Gittins + marginal value | C5 novelty hardened with page cite or downgraded | M |
| E4 ✅ | `C5`, `Q5-restless-patches.md`, new `C25-whittle-foraging.md` | Whittle index for a regrowing patch → numeric giving-up-density prediction with regrowth rate r free; name a foraging dataset to test it | Prediction stated or indexability failure located | L |
| E5 ✅ | `C4`, `novelty-audit.md` | Prior-art kill-check: distributed-detection literature for M^(−1/2) vs M^(−1) | Grade confirmed or downgraded | S |
| E6 | `C18`, new `C23-beta-enzyme-distributions.md` | Fit Weibull β to 3–5 enzyme/catalyst inactivation datasets | Measured enzyme β with CI | M |
| E7 | `C18` | Add product-lifetime Weibull fits (Oguchi & Daigo et al.); state circularity claim β≈1 loss vs β>1 wear-out | Axis spans enzymes → products | M |
| E8 | new `G29-availability-utilisation.md` | Citation-intersect reliability availability vs industrial-ecology "utilisation intensity"; positive control | Count + coverage + standing | M |
| E9 ✅ | `C1`, `C6` | Compute A and Ha for one repairable product class (wind turbine fleet / laptop repair) | Product row on the axis; conditions checked | S |
| E10 | new `G30-resilience-hazard-shape.md` | Weibull β vs ecological return time; test "resilience erosion = β>1" | Intersection measured | M |
| E11 | `C19`, `G23` | Fit window + ceiling to 2–3 subsidy-stress / grazing productivity curves | Three fields on matched axes | M |
| E12 | `G6`, new `C26-hill-multifunctionality.md` | Hill numbers q=0,1,2 on one structural-battery dataset | Index computed or clean negative | M |
| E13 | new `G31-biosignature-reservoir-audit.md` | Specification-instrument on an atmospheric disequilibrium claim (O2/CH4 or K2-18b DMS): enumerate abiotic sources, bound each, residual spec in mol/yr | One worked case, C11 output shape on public data | L |
| E14 | `C8` or new note | Σ for a chemolithotroph on a redox gradient | Bridge built or shown not to form | M |
| E15 | `vault/theorems/kirkwood-disposable-soma.md`, new gap | Citation-intersect Kirkwood 1977 vs infrastructure maintenance-budget literature | Count + coverage | M |
| E16 | `vault/buildable.md` | Latch build: deliverable → Weibull fit over ≥6 specimens; add RH/T logging + wet specimen; Π-group same-object argument; add time column; mark salt-hydrate as "start here" and write its full protocol | Protocol executable without design decisions | M |
| E17 ✅ | `vault/disclosure-ledger.md`, new `vault/sources/src-<witness>-<date>.md` | Ingest the new witness the owner flagged 2026-09-05 (YouTube HM3oUMvvTe8, t=256s; a reported reconstruction worker; possibly a 4chan-origin report). Pull transcript, archive verbatim with URL + fetch date, locate the original 4chan post if any, file as TESTIMONIAL (secondhand unless firsthand is shown), extract only the *specification* the claim implies, and add a row to a new "cross-witness meta-narrative" table (who, country, service, year, claim class) so the "growing ex-military narrative" can be counted rather than felt | Source file archived; ledger row with tier + status; meta-narrative table has ≥1 row and a stated counting rule | M |

---

## Suggested order

1. **D3, D4, D1, D2, D10, D11, D12, D18, D20, D24** — make the vault safe for agents first (all S/M).
2. **B1, B2, B15, D14, D15** — fix the wrong correction and the canonical drift.
3. **Batch A** — computed-note corrections (independent, parallelisable across agents).
4. **Batch B rest + C1–C3, C15, C16** — provenance and null model.
5. **E1, E3, E5, E17** (E2 freeze is now the owner's call, see note) — scope frame and novelty kill-checks.
6. **E4, E6–E16, C5–C14** — the growth work.


**Note on E2 vs E17.** The scope audit recommended freezing the disclosure ledger. The owner then flagged a new witness and a growing cross-witness pattern. These conflict. Resolution proposed: do not freeze; instead convert the ledger from a per-witness list into a *counted* meta-narrative table (E17) so it can reach a checkable claim about testimony structure, which is the owner's stated rule.
