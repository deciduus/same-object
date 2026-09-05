# Charnov–Gittins preprint: build notes

Draft preprint for EcoEvoRxiv / arXiv q-bio.PE, assembled from vault notes
`C5-charnov-gittins`, `C25-whittle-foraging`, `G28-marginal-value-gittins`,
`Q5-restless-patches` and `method/citation-intersection`. Nothing in this folder edits
the vault; the vault remains the source of truth for every number.

## Build

```
pandoc paper.md --citeproc --bibliography=refs.bib -o paper.pdf
```

Requires a LaTeX engine on PATH (TeX Live / MiKTeX) for PDF output. For a quick check
without LaTeX:

```
pandoc paper.md --citeproc --bibliography=refs.bib -o paper.html
```

Add `--csl=<style>.csl` if a journal style is required; without it Pandoc uses its
default (Chicago author–date).

## What the author must fill in before submission

1. **Affiliation.** `paper.md` carries an HTML comment placeholder immediately after the
   `author:` field in the YAML header. Replace it with the affiliation line.
2. **ORCID.** Not present anywhere in the file; add it alongside the affiliation.
3. **Corresponding-author contact email.** Same place. (No email address is included in
   the draft.)
4. **`genmvt2024` author list in `refs.bib`.** The vault records the 2024 bioRxiv
   generalised-MVT paper by title and DOI only. The entry is deliberately author-less
   rather than guessed; look up
   `10.1101/2024.10.28.620618` and complete it.

## Reference verification

Every DOI in `refs.bib` is one a vault note records as verified against a named provider
on a named date. Entries with no verified DOI carry a `% UNVERIFIED` comment saying what
is missing and why. No DOI was constructed or inferred. Do not add DOIs without a
provider fetch.

**Superseded 2026-09-05 — see "Reference verification 2026-09-05" below.** Entries that
previously lacked a verified DOI: `gittins2011` (string recorded, Wiley page 403),
`kilpatrick2020` (arXiv id only), `nonacs2001`, `banks1994`, `averbeck2015`,
`geana2016`, `mcnamara1985`, `houston1999`, `stephens1986`, `green1984`,
`srivastava2013`, `scully2025`. All twelve are now resolved; only `geana2016` still has
no DOI, because none exists.

## Numerics

Table 1 and the two limits in Section 3 are reproduced by
`vault/_scripts/c25_whittle.py` (Python standard library only):

```
python vault/_scripts/c25_whittle.py
```

## Traceability

Each number in `paper.md` carries an HTML comment naming the vault note (and section)
it comes from. If a vault note is revised, grep `paper.md` for that note ID before
re-submitting.

## Reference verification 2026-09-05

Every entry in `refs.bib` was re-checked against Crossref
(`api.crossref.org/works/{doi}`, or a `query.bibliographic` search where no DOI was on
record), with Open Library / dblp / eScholarship / bioRxiv / OpenAlex used for records
Crossref does not hold. Every entry now carries a `note` field recording its status, so
verification travels with the bib. All twelve previously `% UNVERIFIED` entries were
resolved; ten gained a DOI or ISBN, one (`geana2016`) is confirmed to have no DOI in
existence, and none remain unresolved.

### Status table

| Key | Status | Fields changed |
|---|---|---|
| `charnov1976` | verified | `note` added |
| `gittins1979` | corrected | journal expanded to "Journal of the Royal Statistical Society: Series B (Methodological)"; `note` |
| `gittins2011` | verified (was UNVERIFIED) | Crossref monograph record confirmed authors/title/publisher/year; `isbn = 9780470670026` added; title case fixed to "Multi-Armed"; `note` |
| `whittle1988` | corrected | `volume` 25A split into `volume = 25`, `number = A` per Crossref; `note` |
| `ninomora2001` | verified | `note` added |
| `glazebrook2006` | verified | `note` added |
| `kadmonshmida1992` | verified | `note` added |
| `kadmon1992` | **corrected** | title was wrong -- see "Corrections the author must make" below; `note` |
| `possingham1989` | verified | title case matched to Crossref; `note` |
| `ohashi2005` | verified | `note` added |
| `auer2002` | verified | `number = {2-3}` added; `note` |
| `griebling2026` | **corrected** | second author's given name was wrong; `volume = 234`, `pages = 123491` added; `note` |
| `kilpatrick2020` | verified (was UNVERIFIED) | entry type `@article` to `@misc`; `doi = 10.48550/arXiv.2004.10671` added; bioRxiv DOI recorded in `note`; `primaryClass` added |
| `genmvt2024` | **corrected** (author list filled in) | `author = {Zylberberg, Joel}` added; `note` |
| `nonacs2001` | verified (was UNVERIFIED) | `doi = 10.1093/oxfordjournals.beheco.a000381` added; `note` |
| `banks1994` | verified (was UNVERIFIED) | `doi = 10.2307/2951664` added; title case fixed; `note` |
| `averbeck2015` | verified (was UNVERIFIED) | `doi = 10.1371/journal.pcbi.1004164`, `volume = 11`, `number = 3`, `pages = e1004164` added; journal "PLoS" to "PLOS"; title case fixed; `note` |
| `geana2016` | **unverified -- no DOI exists** | subtitle ": A Normative Approach to Adaptive Exploration", `pages = 1793--1798`, `address` added; `note` explains that CogSci proceedings deposit no DOIs |
| `mcnamara1985` | verified (was UNVERIFIED) | `doi = 10.1016/S0022-5193(85)80219-8`, `number = 2`, end page 249 added; `note` |
| `houston1999` | verified (was UNVERIFIED) | subtitle ": An Approach Based on State", `isbn = 9780521384803`, `address` added; `note` |
| `stephens1986` | verified (was UNVERIFIED) | `isbn = 9780691084411`, `address`, `series` added; `note` |
| `green1984` | verified (was UNVERIFIED) | `doi = 10.1086/284184`, `volume = 123`, `number = 1`, `pages = 30--43` added; title case fixed; `note` |
| `srivastava2013` | verified (was UNVERIFIED) | `doi = 10.1109/Allerton.2013.6736565`, `pages = 494--499`, `publisher`, full Allerton proceedings title added; `note` |
| `scully2025` | verified (was UNVERIFIED) | published version located: entry type `@article` to `@incollection`, `doi = 10.1287/educ.2025.0290`, `pages = 28--70`, `isbn = 9798988285632`, INFORMS booktitle/publisher added; title "Decision-Making" to "Decision Making"; `note` |

No DOI, page range or ISBN in `refs.bib` was constructed or inferred; each was read off
a provider record on 2026-09-05.

### Corrections the author must make in `paper.md`

`paper.md` was not edited. Three items, one of them substantive:

1. **Kadmon (1992) title was wrong in the bib.** It carried *"Dynamics of forager
   arrivals and nectar renewal **rates in patches of** Anchusa strigosa"*. Crossref
   (`10.1007/BF00317848`) gives *"Dynamics of forager arrivals and nectar renewal **in
   flowers of** Anchusa strigosa"*. `refs.bib` is fixed. `paper.md` cites this work by
   venue and pages only ("Kadmon (1992), *Oecologia* 92:552--555"), so it contains no
   wrong title and **no in-text edit is required**.

2. **Griebling et al. (2026) second author was wrong in the bib.** It had "Johnson,
   Christina M."; Crossref (`10.1016/j.anbehav.2026.123491`) gives **"Johnson, Shylo
   R."**. `paper.md` names the author by surname only ("Griebling, Johnson &
   Benson-Amram (2026)"), so **no in-text edit is required** -- but the author should
   correct the given name anywhere it appears outside this manuscript.

3. **`genmvt2024` now has an author, and it is a single author.** Section 2.6 refers to
   the work impersonally: "A 2024 preprint, *Generalized marginal value theorem with
   temporal discounting* [@genmvt2024], derives ...". The author is **Joel Zylberberg
   (York University)**, sole author, confirmed by Crossref, the bioRxiv details API and
   OpenAlex independently. The sentence should name him, e.g. "Zylberberg's 2024
   preprint ... derives". **This is the one substantive `paper.md` edit required.**

Two further points, neither an error in `paper.md`:

- **`kilpatrick2020` has no published journal version.** The verification brief expected
  one. There is none under this title: arXiv:2004.10671 lists no journal reference and
  the bioRxiv publication API returns "no articles found for published version". The
  same three authors published *"Uncertainty drives deviations in normative foraging
  decision strategies"*, J. R. Soc. Interface **18**(180):20210337, 2021,
  `10.1098/rsif.2021.0337` -- a **different, differently-titled** paper. Section 1.4 of
  `paper.md` quotes the *preprint's* "Patch foraging as modified multi-armed bandit"
  subsection and its "as formulated these are still different decision problems"
  sentence, so citing the preprint is correct and the RSIF paper is **not** a
  substitute. If a referee asks for a published version, the answer is that the quoted
  passage exists only in the preprint. Both preprint DOIs (arXiv and bioRxiv) are now
  recorded in the entry.
- **`scully2025` is now published, not a preprint.** It appeared as an INFORMS TutORials
  chapter in October 2025 (`10.1287/educ.2025.0290`, pages 28--70). `paper.md` does not
  cite it (see orphans below), so nothing changes there.

### Key hygiene

Checked by extracting all `@key` tokens from `paper.md` against all entry keys in
`refs.bib`.

- **Dangling keys (cited but absent from `refs.bib`): none.** All 20 keys cited in
  `paper.md` resolve.
- **Orphans (in `refs.bib` but never cited): four --** `green1984`, `srivastava2013`,
  `stephens1986`, `scully2025`.

All four orphans are load-bearing for the novelty argument rather than decorative, so
the author should decide deliberately between citing and deleting them:

- `green1984` (*Stopping Rules for Optimal Foragers*, Am. Nat. 123:30--43) is the
  closest 1984 statement of a foraging stopping rule and belongs in Section 1.4's list
  of near-misses.
- `srivastava2013` (*On optimal foraging and multi-armed bandits*) was read in full and
  never mentions Gittins -- direct negative evidence for the gap claim in Section 5,
  currently unused.
- `stephens1986` (*Foraging Theory*) is the canonical foraging monograph and one of the
  term-index-only checks behind the novelty claim. The Limitations section names
  Houston & McNamara (1999) and Gittins et al. (2011) as the unread texts but omits
  Stephens & Krebs (1986), which was checked the same way -- an inconsistency worth
  closing in one direction or the other.
- `scully2025` is a 2025 Gittins tutorial with 240 occurrences of "Gittins" and zero of
  "foraging", "Charnov" or "marginal value" -- the strongest single piece of
  contemporary negative evidence for the gap, and currently uncited.

## Revision 2026-09-05 (review 1)

Responds to the external model review in
`reviews/2026-09-05-gemini-flash-3.8.md` (vetted by the orchestrator the same day; the
reviewer's arithmetic re-check confirmed every number, and its praise is disregarded because
it had no literature access). **No number, table entry or result was altered, and no
Limitations item was softened.** Four insertions:

- **A. Sparse-activation limit.** Limitations item 3 and `vault/computed/C25-whittle-foraging.md`
  now say exactly which asymptotic-optimality regimes exist and that none covers a fixed
  active set of size `M = 1` with `N → ∞`.
- **B. Zero switching delay.** A paragraph in Section 3.3, immediately after equation (4),
  states what a transit of length `τ` does to the index ranking: within-type rank preserved,
  across-type rank not, one global `ν` for a mixed-`r` network.
- **C. GUD scope.** Section 3.1 now defines GUD as Charnov's residual density at departure
  under pure rate maximisation and distinguishes it from Brown's operational
  `H = C + P + MOC` (@brown1988, added to `refs.bib`).
- **D. Polish.** The `δ → 0` passage in Section 2.1 names the dominating bound; an
  Acknowledgements section records the review.

`refs.bib` gained six entries: `brown1988`, `weberweiss1990`, `brownsmith2020` and `gast2023`
verified against `api.crossref.org/works/{doi}` on 2026-09-05, and `zhangfrazier2021` and
`hufrazier2017` verified against the arXiv API the same day and cited as preprints (neither
has a Crossref record or a journal reference). Each carries a `note` recording the provider,
the fetch date, and what was *not* obtained — no full text was read for any of the six. Two
candidate identifiers supplied with the review were wrong and are corrected in the `note`
fields: the DOI `10.1007/s11134-022-09855-2` does not resolve (the Gast, Gaujal & Yan record
is `10.1007/s11134-023-09875-x`), and Zhang & Frazier's subtitle is *Beating the Central Limit
Theorem*, not "beating the Lagrangian relaxation".

## Revision 2026-09-05 (review 1)

External review by an unnamed language model, held at
`reviews/2026-09-05-gemini-flash-3.8.md`. The reviewer had the paper only. It recomputed the
current-patch index, the habitat-arm index, the discounted MVT limit, `W(x) = λx² − r(1−x)²`,
`W'(x) > 0`, `dGUD/dr` and Table 1 by hand and confirmed all of them.

**No number, result or Limitations entry changed.** The revision adds scope, and one
Limitations item was strengthened rather than softened.

| Review point | Where addressed |
|---|---|
| A. Asymptotic gap (`α = M/N` fixed vs. foraging's `M = 1`, `α → 0`) | Limitations item 3, rewritten and expanded; `C25-whittle-foraging` §9 item 1 |
| B. Zero-delay paradox | New paragraph in §3.3 after eq. (4); `C25` §9 item 2 |
| C. GUD scope (Charnov vs. Brown's `H = C + P + MOC`) | §3.1, after GUD is defined; `C25` §9 item 3 |
| Polish: dominated convergence at `δ → 0` | §2.1 |
| Polish: acknowledge the review | New "Acknowledgements" section |

### Does any located result cover `α → 0`?

**No.** This was searched, and the answer is stated in the paper as an open gap rather than
papered over. Weber & Weiss 1990 assumes `N → ∞` with `α` fixed. Hu & Frazier
(arXiv:1707.00205) and Zhang & Frazier (arXiv:2107.11911) hold the pulled fraction constant
in a finite-horizon setting. Gast, Gaujal & Yan (2023) require activations to scale
proportionally with arms. Brown & Smith (2020) give a Lagrangian upper bound that is
finite-`N` and therefore evaluable at `M = 1`, but prove optimality only for many items, so
it yields a numerical certificate for a specific network, not an asymptotic guarantee for the
index at `α → 0`. Limitations item 3 says so in those terms.

### References added to `refs.bib`

Six entries, appended in a commented block at the end of the file. Every DOI was resolved at
`api.crossref.org/works/{doi}?mailto=deciduusleaf@gmail.com` on 2026-09-05 and checked
field-by-field; the two preprints were verified against the arXiv API the same day. No full
text was obtained for any of the six, and each `note` says so.

| Key | Identifier | Status |
|---|---|---|
| `weberweiss1990` | `10.2307/3214547` | verified Crossref — *J. Appl. Probab.* 27(3):637–648, 1990 |
| `brownsmith2020` | `10.1287/mnsc.2019.3342` | verified Crossref — *Management Science* 66(7):3029–3050, 2020 |
| `gast2023` | `10.1007/s11134-023-09875-x` | **DOI corrected** — see below |
| `zhangfrazier2021` | arXiv:2107.11911 | **title corrected** — see below; no Crossref record, cited as a preprint |
| `hufrazier2017` | arXiv:1707.00205 | verified arXiv API; no Crossref record, cited as a preprint |
| `brown1988` | `10.1007/BF00395696` | verified Crossref — *Behav. Ecol. Sociobiol.* 22(1):37–47, 1988 |

Two candidate identifiers supplied with the review brief were wrong and were corrected
against the providers:

- **Gast, Gaujal & Yan.** `10.1007/s11134-022-09855-2` does not resolve (Crossref returns
  "Resource not found"). The record was relocated by `query.bibliographic` and the correct
  DOI is `10.1007/s11134-023-09875-x`, *Queueing Systems* 104(1–2):107–150, 2023-05-21.
- **Zhang & Frazier.** The candidate title *"beating the Lagrangian relaxation"* is not the
  paper's title. arXiv:2107.11911 is *Restless Bandits with Many Arms: Beating the Central
  Limit Theorem*.

### Vault

`vault/computed/C25-whittle-foraging.md` gained a section mirroring the three changes. It is
numbered **§9**, not §8, because §8 ("What it does not settle") already exists; the paper's
existing `C25 §8` traceability comments are unaffected. A log entry is staged in
`vault/PENDING-log-REV1.md` for merging into `vault/log.md`.

## Revision 2026-09-05 (referee 2)

Responds to `reviews/2026-09-05-referee-2-opus.md` (verdict: major revision). That referee
had the manuscript and `refs.bib` only, and recomputed every derivation and number reachable
from them. Three were wrong; all three are corrected here. **No number in Table 1 changed** —
the referee re-derived all sixteen non-trivial cells independently and they agree. A point-by-
point author response is appended to the review file itself.

Ten changes, in the order the brief lists them:

1. **§4 linear renewal (ERROR 1, the referee's M6).** The caveat claimed "the *sign* of (6)
   survives" under linear renewal. It does not. §4 now carries the derivation:
   `∂ρ/∂a = λc(c+ν)/(λa+c)² > 0` everywhere, so no interior stationary point exists, the index
   degenerates to `W = −c` on `(0,1)` with `W(1) = λ`, there is no analogue of (4) or (6), and
   `dGUD/dc` is `−τ` below the kink and `0` above — never positive. §4 now agrees with
   Limitations item 5 and with `vault/computed/C48-kadmon-regrowth-test.md`.
2. **Control-ratio identity (ERROR 2).** The displayed equation is reoriented to
   `(O/E)_ctrl / (O/E)_gap`, which is the 62.5; the reciprocal orientation is noted
   parenthetically. No number moved.
3. **"Factor of 3.8" (ERROR 3).** Restated as row-dependent: 3.8 at `rτ = 0.2`, 11.8 at
   `rτ = 0.05`, diverging as `r → 0`.
4. **Simulation described.** New §3.7, "The simulation behind that interval", gives the C45
   setup in full and reconciles the network's 1.271 with Table 1's 1.340.
5. **Theorem hypotheses.** Attainment of the supremum is now assumed, with two sufficient
   conditions given and the failure case `g(t) = ct` stated; `g'` strictly decreasing is named
   as what makes `t*` unique.
6. **Non-revisitability.** The referee's restructuring is adopted (option (a)) and verified:
   one arm type, τ-prefixed, with a departed arm frozen rather than deleted. The "iff" becomes
   "if". Recorded as `C5-charnov-gittins` §13.
7. **`V' ≡ 0` no longer "by fiat".** §3.5's second limit derives it from the frozen-arm
   argument and the absorbing-departure structure, and the two `r → 0` branches are shown not
   to commute.
8. **Auer control.** §5 now says the control is same-field and measures field distance as well
   as neglect. The number is kept.
9. **Abstract.** Now states the negative simulation result and the saturating-renewal
   restriction.
10. **Referee's three questions** answered in the author response.

### Vault

`vault/computed/C5-charnov-gittins.md` gained **§13**, "Referee-2 restatement" — the proof in
§2–§4 is untouched; §13 records the added hypotheses and the weakened licence.
`vault/computed/C25-whittle-foraging.md` was **not edited**: its §5 boundary-condition
paragraph already stated the linear-renewal degeneracy correctly, so the bug was in the paper
alone. Draft `log.md` entries and the open items this round did not close are staged in
`vault/PENDING-log-REV2.md` (deliberately not linked from `00-index.md`; `_lint.py` warns
about that and the warning is expected). `refs.bib` was not changed in this round.
