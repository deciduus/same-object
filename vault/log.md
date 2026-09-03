---
name: log
type: method
---

# Operations log

Append-only. One line per structural change to the vault. Format:
`## [YYYY-MM-DD] operation | description`

## [2026-09-03] re-read batch | eight gaps read in full, six damaged

Fanned out on the eight `string-protocol` survivors. **Two held, six narrowed. None overturned.**

| Gap | Outcome |
|---|---|
| G6, G28 | held |
| G1 | thermodynamic branch already unified; only the momentum branch survives |
| G2 | "absent from biology" false — seed ageing uses Arrhenius Ea |
| G3 | one leg bridged by name in PNAS 2021 |
| G5 | "no time in it" false — CDHM has healing rate constants |
| G7 | the ladder is reinvented in four fields, not nuclear-only |
| G23 | shot peening names its own descending limb |

**Every one of the six was damaged in the same way**: a supporting sentence claimed a field
lacked a *concept*, when the field had the concept under another name. The surviving claims are
all about missing **formalism** — a parameterised curve, a dimensionless ratio, a shared axis.
That is the sharper class of claim, so the batch improved the catalogue rather than shrinking it.

Also corrected: `structural batteries score ~0.25` in G6 is **UNVERIFIED and withdrawn**; papers
read give 1.15–1.17.

## [2026-09-03] correction | kedem-caplan is not an unread theorem

Catalogued as one. The re-read found it in active use — *Entropy* 25:1575 (2023) applies it to
thermoelectrics and oxidative phosphorylation together, and arXiv:2403.20209 clones the form
into a hydronic figure of merit. The "2 co-citers" figure measured traffic between two named
papers, not whether the result had travelled. It had.

This damages the project's headline pattern for that entry specifically. Recorded rather than
quietly fixed.

## [2026-09-03] computed | C4, and it does not close

`C4-inclination-sensing-limit`: minimum detectable tilt for a single statocyte comes out
**≈11°**, which is **above** the observed thresholdless response. The single-cell model fails,
and that is the result — it forces pooling across statocytes, predicting threshold degrading as
M^(−1/2). An ablation series that could test it already exists (Blancaflor 1998), analysed for
presentation time instead.

## [2026-09-03] correction | G11 statolith energy was wrong by ~100x

The note claimed a single statolith displacement costs **2–3 k_BT**. Recomputed from Bérut
et al. 2018 (PNAS 115:5123): buoyant mass 1.91×10⁻¹⁴ kg, d = 4.5 μm, so mgd = 8.4×10⁻¹⁹ J
= **~205 k_BT**. The check: this gives Pe⁻¹ = 4.9×10⁻³, inside the paper's stated 3–8×10⁻³.

2–3 k_BT is roughly the cost of a **66 nm** displacement — a derived *threshold*, not the
*cost* of a displacement. The two were conflated.

## [2026-09-03] restored | G11 withdrawn → narrowed, evidence full-text-read

The withdrawal cited Miyamoto 2007 as a limits-to-sensing analysis. It is an experiment
(flax roots, 5 Hz, 0.5 mm oscillation). A withdrawal misdescribed its own source — the exact
failure the symmetry rule was written to catch, caught only by reading.

## [2026-09-03] vocabulary | evidence gains full-text-read

Ranked between citation-intersection and string-protocol. Means the primary sources were
read, not counted. Added because [[G11-plant-gravisensing]] had no honest grade available:
three papers read in full is not `single-review` and is plainly stronger than
`string-protocol`. Enforced by `_lint.py`.

## [2026-09-03] atomic-schema migration | 20 gap notes converted

Prose frontmatter replaced with filterable data. `contact-surface: "0 crossings, both
directions"` became `contact-surface: 0` plus `crosses`, `crosses-rank`, `topology`,
`mediator`. Six typed directional edge fields added. Tag mirrors added.

Reason: prose in a machine field cannot be sorted, filtered, or linted. The defect that
prompted it — [[verdict-scoring]] was marked retired while a gap still carried
`status: holds` — was a retired word sitting in current frontmatter with nothing to catch it.

## [2026-09-03] lint extended | atomic vocabularies enforced

`_lint.py` now checks the `crosses` vocabulary, that `crosses-rank` agrees with `crosses`,
the `topology` vocabulary, that `mediated` and the `mediator` field agree, that
`contact-surface` is a bare integer, and that all six edge fields are present.

## [2026-09-03] graph and Bases added | zero plugins

`triage.base` and [[graph-view]]. Both are core Obsidian. Bases reads YAML frontmatter only,
which is why the migration had to land first.
