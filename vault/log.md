---
name: log
type: method
---

# Operations log

Append-only. One line per structural change to the vault. Format:
`## [YYYY-MM-DD] operation | description`

## [2026-09-03] re-read batch two | G20 overturned, G22 upgraded, G4 audit finally run

**[[G20-resize-vs-throttle]] overturned.** Textbook anchoring on the originating field's term.
Computing has the symmorphosis question with formulas, under **over-provisioning accuracy**
(arXiv:1905.10270) — and the word "safety" appears zero times in that paper. Worse, safety
factors are *native* to mechanical engineering, so "never reached mechanical engineering"
inverted the direction of travel.

**[[G4-criticality-as-design]]: we had characterised a bibliography we never opened.** The
Muñoz *RMP* reference list was finally extracted. **595 refs, not 578** — and **it carries no
article titles at all**, only venues. Every prior subject-keyword characterisation of it was
reading data that does not exist. Five IEEE entries, so "zero engineering" is false as worded.
The review cites Stoop's theory papers and omits his cochlea *hardware*.

**[[G22-scale-transfer-triage]] upgraded to live.** The two-agent disagreement was adjudicated
by pulling Perricone 2021 and searching it directly: Buckingham 0, dimensionless 0, screening 0,
protocol 0. The paper's closing line asks for the guidelines, so it cannot be them. New named
failure: mistaking *naming the problem* for *supplying the procedure*.

## [2026-09-03] hygiene | lint now rejects a UTF-8 BOM

A PowerShell `Set-Content` rewrite prepended a BOM, which silently broke frontmatter parsing —
the note reported `no type` while looking perfectly correct in an editor. Caught by the lint
only because `type` is required. Now checked explicitly.

## [2026-09-03] closed by construction | C5 and C6 write two missing objects

First time this project produced theorems rather than catalogue entries. Both were attempts to
**close** a gap by writing the algebra, per [[what-closes-a-gap]].

**[[C5-charnov-gittins]] — the strongest result here.** Charnov's marginal value theorem *is*
the Gittins index, as an identity in two lines. Charnov's maximisation over residence time is
literally the supremum over stopping times in the index definition. The travel time τ is neither
a switching cost nor zero; it is a zero-reward prefix inside the outside arm, licensed by
patches being non-revisitable. A 2024 bioRxiv paper derives `g'(t*) = λ·EV`, which is Whittle's
`ν = δM`, with zero occurrences of Gittins — independent rediscovery that validates the algebra
and demonstrates the gap at once.

**[[C6-damage-healing-ratio]].** `Ha = k_r/k_d` with fixed point `A = Ha/(1+Ha)`, reducing to
`MTBF/(MTBF+MTTR)`. No prior art. Two by-products beat the group itself: the reason nobody wrote
it is **experimental** — materials science cannot suppress healing while loading — and setting
`ḣ = 0` in the Das & Kumari law gives `h → 1` always, so continuum damage-healing mechanics has
**no interior steady state in the healing variable**. A defect found by trying to use the law.

## [2026-09-03] correction | my own claim about the ablation test was wrong

I wrote that the pooling prediction was "one re-analysis away" from a test against Blancaflor
1998. **It is not.** `τ_p ∝ M⁻¹` is equally the prediction of plain linear summation; the models
separate only in the *angular* exponent, and that stimulation was done at 90° only. The
discriminating measurement was never made. Corrected in [[C4-inclination-sensing-limit]].

Also: `M` resolved to **48**, not 12 — the old figure was a median-section undercount by exactly
4×. And equal-weight pooling is falsified outright: at fixed `M = 16`, presentation time runs
2.62 to 7.13 min depending only on which story survives. **Cell identity dominates cell count.**

## [2026-09-03] unblocked | citation-intersection was never actually blocked

Recorded as blocked because OpenAlex and Semantic Scholar both returned 429 with hours-long
Retry-After. **Wrong conclusion.** Three other providers work, verified live:

- **Crossref** returns full reference lists with DOIs — 71 refs, 70 with DOIs, on the spot check
- **OpenCitations COCI** returns both citers and references, and agreed with Crossref at 71
- **Europe PMC** returns citers by PMID — 49 on the same work

Two independently assembled sources agreeing is the verification. See [[citation-sources]].

The lesson generalises and is now a rule: **a blocked API is not a blocked method.** Never mark
something `not-assessed` on one vendor's failure without checking whether another answers the
same question.

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
