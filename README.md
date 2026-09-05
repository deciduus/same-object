# Gradient Coupling Inquiry

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22334047.svg)](https://doi.org/10.5281/zenodo.22334047)

An inquiry in **cross-domain synthesis**, run under one rule: **a thread is in scope if it can
reach a checkable claim.** The starting question was whether biomimicry has anything to say
about anomalous propulsion claims. It became something more useful: a repeatable method for
locating **cross-domain gaps** — principles that several fields discovered independently,
quantified in their own vocabulary, and never put on a shared axis.

The method is to find places where two fields quantify the *same physical object* in different
vocabularies, never cross-cite, and therefore each hold half of a result — then either build the
missing shared object or prove it cannot exist. The recurring objects are the ones that govern
how living and engineered systems **persist**: how available a repairable thing is, how it fails
as a distribution rather than a mean, how much repair a finite budget buys, what dose of stress
strengthens it before it breaks, and when to abandon a depleting patch. Those are the physics of
durability, maintenance, recovery and foraging — which is to say they are the physics that
**ecology, circularity and conservation** are made of, and the physics any account of life
elsewhere would also have to obey. So the named destinations are biomimicry, ecology,
conservation, sustainability, circularity, **astrobiology**, and **meta-research** on how
science resolves disagreements. Nothing is excluded for being unfashionable; a thread is
excluded when it cannot reach a number someone else could check.

This reads as biomimicry in the strict sense: not copying shapes, but transporting *quantified*
design laws between biology, engineering and ecosystem-scale resource use, in whichever
direction the gap runs.

Twenty such gaps are documented in `vault/gaps/`, each with measured co-citation evidence.
**Four "the unifying theorem already exists, unread" claims have been citation-tested and all
four survive** — Kirkwood's disposable soma, the availability formula, stress-strength
interference, and Hill-number multifunctionality (`vault/computed/C13-unread-theorem-audit.md`,
fetches 2026-09-03). A fifth, Kedem–Caplan, failed the same test: it is in active use, and that
failure is recorded rather than quietly dropped (`vault/novelty-audit.md`). Six theorem notes
sit in `vault/theorems/`; four of them are the tested ones. That pattern — the result exists, in
a literature the field that needs it does not read — is the dominant finding of the project, and
it is hardened only to the citation-intersection level: a parallel derivation that never cites
the anchor is still invisible to it.

Nineteen were then **re-tested against a harder standard**, and roughly half were damaged:
two overturned, seven narrowed, one withdrawn. That audit, not the original catalogue, is the
most reliable thing here. Entries carry a `standing` and an `evidence` grade, and
string-protocol findings have survived under half the time when re-tested by citation
intersection. Weight accordingly.

A bound is rarely wrong. What is usually wrong is the list of things its derivation held
fixed without saying so. See `METHOD.md` §8.

---

## Files

| File | What it is |
|---|---|
| `vault/` | The vault. **92 linked markdown notes** as of 2026-09-05 (20 in `gaps/`, 22 in `computed/`), plain files, opens in Obsidian. **Canonical for all standings.** Start at `vault/00-index.md` |
| `vault/_lint.py` | Schema check. Run from `vault/` before committing |
| `vault/triage.base` | Obsidian Bases view — the re-test queue, sorted by weakest evidence first |
| `VISION.md` | The four-layer ladder: literature → computation → hypothesis → experiment |
| `METHOD.md` | How the inquiry is run — the gap test, the co-citation audit, the claims register, verification discipline |
| `ARCHIVE-findings-2026-09.md` | **Archived history, superseded 2026-09-05.** The old status ledger, in the retired HOLDS/WEAKENED/WITHDRAWN vocabulary. Not current; do not read standings from it |
| `CLAUDE.md` | Working rules for anyone (human or agent) editing this repo — canonical sources, closed vocabularies, lint-before-commit |
| `BACKLOG.md` | The open work: 62 actionables in five batches, with IDs |
| `audits/` | Five 2026-09-05 audit reports (math/physics, sources, method, structure, scope) — the full reasoning behind every backlog line |
| `inquiry-map.html` | The living map. Layered graph, **77 nodes**, notes persist server-side |
| `claims-register.html` | Reported behavior → candidate mechanism → discriminating test |
| `unexplored-window.html` | Where the parameter space is genuinely open |
| `gradient-coupling-dossier.html` | The original evidence ledger — documented / testimony / refuted |
| `error-energy-axis.html` | The kT-normalized energy-per-bit / error-rate axis, as far as it has been built |
| `findings-synthesis.html` | Ranked findings, predictions and negatives, as of its snapshot date |

**The six HTML files are snapshots, and they drift.** They are published as private artifacts
and are regenerated by hand, so any of them can lag the vault — where a page and a vault note
disagree, the vault note is right. `inquiry-map.html` is the special case: the notes added to
its nodes live in a **server-side artifact database, not in this repository**, so they are not
in git, not diffable, and not recoverable from a clone. Read them back through the published
artifact, and treat anything only recorded there as unbacked until it is written into a vault
note.

---

## Precedent, stated up front

This method is **Literature-Based Discovery**, founded by Swanson in 1986. Non-co-citation
as evidence of a connectable gap is his founding move, not our innovation, and an
engineering-biology version at 101-million-abstract scale was published in 2025.

Two features appear defensible: requiring a **quantified metric on both sides** as an entry
criterion, and running **positive controls** — which answers a documented 2023 complaint
that LBD evaluation lacks them. See `METHOD.md` §12 for the full accounting and the
citation list.

---

## The through-line

Six moves recur across every field surveyed, and none of them is *build a stronger
thing*:

1. **Manufacture contrast** — signal under the noise floor? Create a local disparity that survives it
2. **Use the noise** — efficiency is often non-monotonic in noise, with an optimum above zero
3. **Separate timescales** — don't build a faster actuator; decouple slow loading from fast release
4. **Change the actor** — when a theorem blocks the route, swap the category of the thing doing the work
5. **Work inside the noise** — suppress, exploit, redistribute; each community knows one
6. **Vary what was held fixed** — a bound is rarely wrong; the list of things its derivation silently held fixed usually is

All six are **structural** moves rather than **magnitude** moves. Engineering defaults to
raising signal or lowering noise. Evolution cannot turn up the power, so it searches
arrangement instead — which is why it keeps finding these first.

---

## What closes a gap

The strongest result here. **Work-extracted-per-bit came back *not* a gap** — that metric
is shared across colloidal, single-electron, cavity-QED and diamond platforms, which are
directly comparable despite sharing no hardware.

Why? Someone gave it a **theorem** that fixed the denominator, and the shared figure of
merit followed within a decade.

Every other gap is missing exactly that. Closing one does not need a review article. It
needs a theorem — and in four citation-tested cases the theorem already exists, unread
(`vault/computed/C13-unread-theorem-audit.md`). A fifth candidate, Kedem–Caplan, turned out to
be in active use when read rather than counted.

---

## Ready to run now

Requiring no apparatus, no funding, no access:

- **Co-citation audits.** Two tables are publishable as-is — gradient harvesting and
  multifunctionality. A third, the criticality reference audit, was listed here and is
  **withdrawn**: its reference count was wrong and the bibliography it characterised has no
  article titles in it. See `METHOD.md` §2.
- **The discrepancy base rate.** Build the catalogue of persistent inter-method
  disagreements, compute what fraction resolved to systematics versus new physics, and
  test which features predicted each outcome. Every input is public.

Requiring about $100 of kitchen equipment:

- **Salt hydrate cycling.** Dehydrate, weigh, rehydrate, weigh, log temperature rise, plot
  against cycle number for 50+ cycles. Reporting fade per cycle and per day separately.
  Measures the exact variable that field's own review calls under-served.

---

## Working notes

- The register's discipline: **testimony sets the specification, never the mechanism.**
  Rows stay valid regardless of how any account is assessed.
- Verification: a figure is quotable only if the source names the fetch that produced it.
  Two research failures in this project had the same tell — specific numbers with no URL.
- Corrections are logged in `vault/log.md` rather than silently fixed. The pattern of
  errors is itself information — and one entry there is a correction *of* a correction.

## AI use disclosure

This vault is AI-assisted research. Claude Fable 5.1 (Anthropic) orchestrates: it audits, writes task briefs, integrates results, and decides what is committed. Claude Opus 4.8 agents, run through Claude Code, do the derivations, database queries, prior-art searches, fits, and drafting, each under a written brief. The human author (Landon Holden) sets the questions, the scope rule, and the evidence standards, and reviews and takes responsibility for every claim. All queries, counts, and corrections are logged in `vault/log.md` and `audits/`. Models are not authors. Cite this disclosure if you reuse the material in a context that requires it.

## Cite

Holden, L. (2026). *Gradient Coupling Inquiry: a cross-domain gap-finding vault*. Zenodo. https://doi.org/10.5281/zenodo.22334047 (concept DOI, resolves to the latest release; v0.1.0 is 10.5281/zenodo.22334048). Licensed CC-BY-4.0.
