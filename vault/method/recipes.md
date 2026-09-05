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

## How to run a citation intersection

The provider table, rate limits, biases and traps are in
`vault/method/citation-sources.md`; the null model is in
`vault/method/citation-intersection.md`. This is the procedure.

1. **Check what is available before you start.**

   ```
   cd vault/_scripts && python intersect.py --list-providers
   ```

   Prints every adapter with its auth state, rate limit, keyspace and coverage bias. `NO` in the
   usable column names the missing env var.

2. **Run `--all`, not one provider.**

   ```
   python intersect.py <doiA> <doiB> [<doiB2> ...] --all
   ```

   The first DOI is anchor A; all remaining DOIs are pooled as anchor B (use this when a work has
   several DOIs, or when one side needs a broader canon than a single paper). Output is a
   per-provider table — `N_A`, `N_B`, `AnB`, blanks dropped, status — plus a consensus line.
   `--providers=opencitations,openalex` restricts the set; the default with no flag is
   OpenCitations alone, as before.

3. **Read the `err` rows before the numbers.** An `err` row is a **failed fetch, never a zero**,
   and the three causes are not interchangeable:
   - `BudgetExhausted` — OpenAlex's day is spent; re-run after midnight UTC. Nothing about the
     literature.
   - `no record for DOI …` — a coverage hole in that provider (Semantic Scholar misses many
     pre-1990 and book-level DOIs; Europe PMC is biomedicine-weighted). Nothing about the
     literature.
   - `500 … large-anchor size failure` — OpenCitations above ~10k citers. Use OpenAlex.

   If **every** provider errored, the run is broken. Do not record anything.

4. **Quote the consensus, not one provider.** Where providers agree, say so and name them; the
   number is much stronger than any single run. Where they disagree, quote the range
   `|A n B| in [lo, hi]` — never the provider that flatters the claim. Where only one answered,
   say which and say why the others did not.

5. **Inspect every hit.** A count is not a finding until each hit has been read. `--enrich`
   fetches title / year / journal per hit from Crossref. Hits are marked `*` when every
   responding provider found them; an unstarred hit is one provider's opinion.

6. **Never substitute a near-miss.** If a provider cannot find the anchor DOI, that provider does
   not answer for this pair. Do not swap in a title match, a different edition, or a
   "close enough" record — Semantic Scholar's match for Billinton & Allan 1996 is the **1984
   first edition** under a different DOI with a different citer set. The adapters do no fuzzy
   fallback on purpose.

7. **Report the null model.** `NULL_N=<n> python intersect.py …` prints the expected count under
   independence and `O/E` for the first responding provider. A zero against an expectation below
   1 says nothing at all; quote `O/E` at the union floor **and** at one field-scale `N`, per
   `citation-intersection.md`.

8. **Record the tuple.** Provider **and** exact endpoint **and** fetch date **and** `N_A` **and**
   `N_B` **and** intersection **and** coverage basis **and** the null expectation — one row per
   provider per date. A number missing any of these is not quotable (`CLAUDE.md`). Where two
   dates or two providers disagree, record both: they may be two true numbers about two
   different objects.

9. **Sanity-check the toolkit itself** with `python intersect.py --selftest`, which re-fetches a
   known small pair, asserts no blank key survives the filter, and asserts every adapter still
   satisfies the common interface.

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
