# Program synthesis — working notes, 2026-09-05

Working notes behind `vault/program.md`. What was read, what was extracted, how many, and what the
extraction is and is not.

**Scope of the task.** Extract, exhaustively, every concrete research move the vault has already
named and not done; tag each; organise into a programme. Read-only on existing notes. Two files
written: `vault/program.md` and this one. No git operations. No existing file edited.

---

## 1 · What was read

Read in full by the synthesising agent:

- `CLAUDE.md`, `README.md`, `VISION.md`, `METHOD.md` (all 13 sections), `BACKLOG.md` (all five
  batches A–E plus the five status blocks at the top)
- `vault/00-index.md` (canonical standings block, all 20 gaps), `vault/strategy.md` (including the
  2026-09-03 depth gate), `vault/buildable.md`, `vault/predictions.md`, `vault/novelty-audit.md`
- `vault/PENDING-log-C42.md`, `PENDING-log-C43.md`, `PENDING-log-G36ADV.md`, `PENDING-log-G36PROV.md`
  — four unapplied staging buffers, including the **open disagreement** between the two G36 review
  legs on whether the topology is mediated (that disagreement became item P-109)
- `vault/log.md` (entry headers for all ~80 entries; several entries in full)
- `papers/charnov-gittins/README.md` (build notes, reference-verification table, the three
  corrections the author still owes `paper.md`)
- `unexplored-window.html`, `claims-register.html`, `findings-synthesis.html` (text-extracted)

Read in full by six parallel extraction agents, one directory or report-set each, under a common
output contract (`SOURCE | title | what would be done | data + access | category guess`):

| Agent | Corpus | Files | Items returned |
|---|---|---|---|
| A | `audits/scout-*.md` | 8 | 118 |
| B | `audits/0*-*.md`, `blind-brief-*`, `g34-adversarial`, `g36-adversarial`, `staged/` | 13 | 243 |
| C | `vault/method/`, `moves/`, `questions/`, `theorems/`, plus ledger and taxonomy notes | 39 | 132 |
| D | `vault/computed/C1`–`C22` | 22 | 130 |
| E | `vault/computed/C25`–`C43` | 19 | 166 |
| F | `vault/gaps/` (all 27) | 27 | 121 |

**Total files read: 128 notes and reports** plus the six root documents and three HTML artifacts.
**Total raw extracted items: 910.**

Concurrency note, as briefed: another agent was editing G36 / C35 / `novelty-audit.md` during this
session. Agents were told to read what was on disk and expect churn. Nothing in `program.md`
depends on a G36 standing; it cites G36's *open work*, which is stable across the churn.

---

## 2 · How 910 became 120

Deduplication passes, in order:

1. **Cross-corpus duplicates.** The same move is frequently named in a scout report, a gap note, a
   computed note and an audit. Example: the soil `Ha` computation appears in `scout-05`, `G36`,
   `C6`, `C35`, `C42`, `C43` and `g36-adversarial`. One item.
2. **Already done.** ~140 raw items had been executed between the report that named them and today
   (all of Batch A, most of Batch D, C43 executing C35 §5's falsifier, C32 executing C29 §5.1). These
   were dropped, except where the execution *failed* — those became items in their own right
   (P-057, P-071).
3. **Blocked-fetch consolidation.** ~45 raw items were single blocked primaries. Where the block is
   the same class (publisher 403 reachable with an institutional login) they were batched into
   P-032, P-004, P-010 and P-045. Where the document is uniquely load-bearing they stayed separate
   (P-033 Verheijen, P-034 Griebling, P-035 the two books).
4. **Provider/scoped-N consolidation.** ~30 raw items were "fetch a scoped N" or "run a second
   provider" for one gap each. Batched into P-050, P-051, P-052, P-086, P-087.
5. **Housekeeping excluded.** ~110 raw items from `04-structure-tooling` and Batch D are lint rules,
   file renames, tag fixes and template work with no research content. Excluded by design: the brief
   asked for research moves. The four that change what the vault can *say* were kept (P-085, P-100,
   P-105, P-108).
6. **Below the bar.** ~55 raw items were "read X in full before quoting it" on a document that no
   claim currently rests on. Excluded.

**Result: 120 items.** DATA 52 · PREDICTION 15 · SIMULATION 13 · METHOD 11 · THREAD 11 ·
INSTRUMENT 10 · BUILD 8. Sixty-three carry a full table row; fifty-seven are compressed to one line
each, purely to hold `program.md` under its 40 KB budget. Nothing was dropped for space — the
compressed entries carry ID, title, category, source and action.

---

## 3 · What the categories caught

- **DATA (52).** Every "dataset named" line in a computed note; every empty table row with a stated
  data need (C1's cortical bone revisit interval, C6 §5's two polymer rows, C18's estimator column,
  C28's six-route specificity column, C31's three blank `T` rows, C38's parid leg); every "could not
  be fetched" that a different route can reach. C43 is the model the brief named: two named open
  APIs (OCTOPUS WFS, USDA Soil Data Access) plus a join nobody had run.
- **PREDICTION (15).** Includes the two **failed** predictions and what the notes say replaces them:
  C29's per-habitat ordering (failed in C32, replaced by the recovery-debt corollary, P-071) and
  C39's underpowered governance ordering (P-073). Also the two standing hash-stamped predictions in
  `vault/predictions.md` (P-069, P-070) and C4's 1.73-vs-3.00 pooling test (P-066).
- **INSTRUMENT (10).** The reservoir and information audits pointed at named open cases — Mars
  methane, K2-18b DMS — plus the negative controls both instruments have *designed and never run*,
  the blind-brief protocol's own recorded weakness, and the diagnostic-test frame's transfer test.
- **SIMULATION (13).** Models the vault derived and never propagated: the Whittle policy with
  regrowth, the soil depth balance with cover feedback and its double-crossing threshold, the
  reserve recursion with predation as an interior absorption, the clustered-mutation load run
  forward through a published extinction simulation.
- **BUILD (8).** The `buildable.md` register plus what later notes imply: latch fatigue as a Weibull
  fit rather than a single cycle count, salt hydrate with its protocol written first, the
  shot-peening dose sweep, the columella experiment, and the tooling debts (S2/Lens keys, Scopus and
  WoS adapters, reproducibility).
- **METHOD (11).** Scoped N for every gap, the parent-search diagnostic, structural blindness for
  briefs, provider coverage holes, the LBD retro-test, the withdrawal-symmetry rule.
- **THREAD (11).** Q1, Q2, Q3, Q5, Q6, Q8, Q10 and the four gaps whose "what would close it" is an
  unattempted computation (G1, G7, G20, G27), plus two never-opened candidate gaps.

Q4, Q7 and Q9 appear under PREDICTION and SIMULATION rather than THREAD, because each already names
a specific computation rather than an open question.

---

## 4 · Access status, counted

Of the 120 items: **74 need nothing but a desk and an open API** (owner `agent`); **32 need an
institutional login, an ILL, an author email or an industry contact** (`library`); **8 need
apparatus** (`bench`); the remaining 6 are tooling that needs a credential application.

Named blockers that recur, and which the programme routes around rather than repeating:

- Publisher 403 on ACS, Wiley, Elsevier and JSTOR — 11 distinct documents, all ASU-reachable.
- OpenAlex daily-budget exhaustion — the direct cause of every union-floor denominator in the
  2026-09-05 gap round. One batched run clears it (P-051).
- Semantic Scholar coverage holes — eight named anchors have no S2 record and one exceeds the paging
  cap. These are recorded as `err`, never as zeros, which is correct, but it leaves several rows
  single-provider (P-050).
- `war.gov`, `aaro.mil` and `archive.dni.gov` 403 with no Wayback snapshot — six ledger rows.
- Two datasets behind bot protection that a browser can fetch and a script cannot (P-085).

---

## 5 · What this extraction is not

- **Not a validity judgement.** An item's presence means a note named it as missing, not that it is
  worth doing. The leverage ranking in `program.md` §2 and the abandon list in §5 carry that
  judgement, and they are mine, not the notes'.
- **Not complete on housekeeping.** ~110 lint, template and file-hygiene actions from Batch D and
  `04-structure-tooling` were deliberately excluded. They are still in `BACKLOG.md`.
- **Not independent of the churn.** G36, C35 and `novelty-audit.md` were being edited concurrently.
  Items P-002, P-033 and P-109 may need restating once that edit lands.
- **Effort figures are estimates.** `hours` / `days` / `session` are the notes' own words where they
  gave one, and my read of comparable completed work where they did not.

## 6 · Lint

`vault/program.md` carries `name: program`, `type: method`, which are legal under
`_lint.py`'s `TYPES`. It is **deliberately not linked from `00-index.md`** — the owner will add the
index line. Until then `_lint.py`'s reachability check will flag it, and that is expected, not a
defect. No existing file was edited to accommodate it.
