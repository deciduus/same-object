# CLAUDE.md — working rules for this repo

Read this before editing anything. It is the contract, not a summary.

## What this project is

A cross-domain synthesis inquiry run under one rule: **a thread is in scope if it can reach a
checkable claim.** Named destinations: biomimicry, ecology, conservation, sustainability,
circularity, astrobiology, and meta-research on how science resolves disagreements. Nothing is
out of scope for being unfashionable; a thread is out of scope when it cannot reach a number
someone else could check.

The four-layer ladder (`VISION.md`): **1** find the gap (two fields quantify the same object, no
cross-citation) → **2** apply the formalism and compute → **3** generate a checkable prediction →
**4** test it. `vault/strategy.md` holds the orthogonal Compare/Produce/Deduce lens and the
current depth gate.

## Canonical source of truth

- **`vault/00-index.md` is canonical for standings.** If any other file disagrees about a gap's
  status, the vault note and the index win, and the other file is the bug.
- **`ARCHIVE-findings-2026-09.md` is archived history, not current state.** It uses the retired
  HOLDS/WEAKENED/WITHDRAWN vocabulary. Never cite it for a standing.
- `BACKLOG.md` holds the open work (batches A–E, with IDs). `audits/` holds the five 2026-09-05
  audit reports that produced it, with the full reasoning behind every backlog line.

## Before any commit

```
cd vault && python _lint.py     # must exit 0
powershell -ExecutionPolicy Bypass -File check.ps1   # from repo root: lint + idx-check + link check
```

A failing lint is a blocked commit. Do not edit `_lint.py` to make an error go away.

## Closed vocabularies (verbatim from `vault/_lint.py`)

```python
STANDING = {"live", "narrowed", "withdrawn", "overturned"}
EVIDENCE = {"citation-intersection", "full-text-read", "string-protocol",
            "single-review", "not-assessed"}
RETIRED  = {"holds", "weakened", "collapsed"}
TYPES    = {"gap", "move", "method", "theorem", "computed", "index", "question", "source"}
CROSSES  = {"nothing": 0, "word": 1, "metaphor": 2,
            "vocabulary": 3, "formalism": 4, "data": 5}
TOPOLOGY = {"disjoint", "direct", "mediated"}
EDGES    = ("borrows-from", "lends-to", "mutual-with",
            "computed-in", "uses-move", "rests-on")
```

`evidence` is ordered strongest-first as written. `crosses-rank` must equal the integer
`CROSSES` maps its `crosses` value to. `topology: mediated` and a `mediator:` field must agree.
`contact-surface` is a bare integer. All six `EDGES` fields must be present on a gap note.
Retired words are rejected in `standing`, `evidence` and `type`. Prose belongs in `note:` —
never in a machine field.

Gap notes also need a `**STANDING:` line in the body, and every note must be reachable by
wikilink from `00-index.md`.

## Corrections

**Corrections are logged in `vault/log.md` and never silently fixed.** The pattern of errors is
itself information, and this project has already had to correct a correction. Log format,
newest first:

```
## [YYYY-MM-DD] kind | one-line summary
```

`kind` is free text describing the move (`correction`, `verification`, `computed`, `vocabulary`,
`method`, `honest null`, …). Say what was wrong, what it is now, and what produced the new
number.

## Numbers

**Every count or citation number must name provider + date.** "578 references" is not a claim;
"Crossref deposited `reference-count` = 578 for DOI 10.1103/RevModPhys.90.031001, fetched
2026-09-05" is. A figure is quotable only if the source names the fetch that produced it.

Two different objects can carry two different true numbers — deposited reference list vs printed
bibliography, string-match count vs inspected intersection. Before calling a number wrong,
establish that both numbers measure the same object. See `vault/method/citation-sources.md` for
the working providers and the two known endpoint traps.

## Commits

**Commit subjects state the result, not the action.** Not "update METHOD.md" — "Correct G's
sigma from 13 to 9.9". Not "fix files" — "Depth gate: Layer 2 is broad but shallow". A reader
scanning `git log` should learn what the project now believes.

## Recipes

`vault/method/recipes.md` holds the step-by-step "How to add a gap" and "How to add a computed
note" procedures. Follow them rather than improvising a note shape.
