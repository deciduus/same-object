---
name: recipes
type: method
---

# Recipes

Step-by-step procedures for the two things an agent most often has to add to this vault. The
rules they operate under are in `CLAUDE.md`; the reasoning behind them is in the method notes
linked below.

## How to add a gap

1. **Run the three-part test** (`METHOD.md` §1): each field has its own *quantified* metric; the
   metrics are the same quantity under different names; the citation networks genuinely do not
   overlap. One out of three is an analogy — say so and keep it out of `vault/gaps/`.
2. **Run a positive control** alongside the claim (`vault/method/positive-controls.md`). A known-
   closed pair, same query shape. If the control does not separate from the claim, you have
   measured your query, not the literatures.
3. **Check the failure modes before reporting a zero** (`vault/method/failure-modes.md`,
   `homographs.md`, `METHOD.md` §11). Punctuation, homographs, proper-noun narrowness, synonyms,
   boolean relaxation. Any zero anchored on a proper noun, a possessive, or a word both fields
   own is invalid by default.
4. **Copy `vault/_templates/gap.md`** into `vault/gaps/G<n>-<slug>.md`. Do not reuse a retired ID
   — see the retired-ID table in `METHOD.md`.
5. **Fill the machine fields**: `type: gap`, `standing`, `evidence`, `crosses` + `crosses-rank`,
   `topology` (+ `mediator` if mediated), `contact-surface`, and all six edge fields. Legal
   values are in the template comments and in the vocabularies above.
6. **Write the `**STANDING:` line** in the body, and describe the relationship along the six
   fields in `vault/method/relationship-description.md` — a count is an input, never a verdict.
7. **Record provenance**: anchor DOIs, provider, endpoint, query date, N, and the coverage
   denominator. A `citation-intersection` grade without that tuple is not reproducible.
8. **Link it from `vault/00-index.md`** (the gaps block between the `IDX:GAPS` sentinels is
   generated — run `python _idx.py` from `vault/`, do not hand-edit it) and log the addition in
   `vault/log.md`.
9. **`python _lint.py` from `vault/`**, then `check.ps1` from the root.

## How to add a computed note

1. **A computed note closes something.** Name the gap or question it answers before starting; if
   nothing is closed or narrowed, it is a log entry, not a note.
2. **Create `vault/computed/C<n>-<slug>.md`** with `type: computed`, `name:` matching the
   filename stem, and `closes:` / `last-checked:` / `result:` fields.
3. **Show inputs, arithmetic and source per row.** Every number needs the fetch that produced it.
   Mark anything you could not source `UNSOURCED` or `UNVERIFIED` rather than dropping it.
4. **State the negative result plainly if you get one.** A computation that fails to close its
   gap is a result — `vault/questions/` and the log are full of them, deliberately.
5. **Reciprocate the edge**: the gap note's `computed-in` and this note's `closes` must point at
   each other.
6. **Link from `vault/00-index.md`**, log it in `vault/log.md`, then lint.
