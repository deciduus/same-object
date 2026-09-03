# Gradient Coupling Inquiry

An open-ended research project. The starting question was whether biomimicry has anything
to say about anomalous propulsion claims. It became something more useful: a repeatable
method for locating **cross-domain gaps** — principles that several fields discovered
independently, quantified in their own vocabulary, and never put on a shared axis.

Twenty such gaps are documented in `vault/gaps/`, each with measured co-citation evidence.
**Six have a unifying theorem already written and sitting unread in an adjacent field** —
which has become the dominant finding of the project.

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
| `vault/` | The vault. 49 linked markdown notes, plain files, opens in Obsidian. Start at `vault/00-index.md` |
| `vault/_lint.py` | Schema check. Run from `vault/` before committing |
| `vault/triage.base` | Obsidian Bases view — the re-test queue, sorted by weakest evidence first |
| `VISION.md` | The four-layer ladder: literature → computation → hypothesis → experiment |
| `METHOD.md` | How the inquiry is run — the gap test, the co-citation audit, the claims register, verification discipline |
| `FINDINGS.md` | Status ledger — confirmed gaps, findings with numbers, closed items, corrections log |
| `inquiry-map.html` | The living map. Layered graph, 62 nodes, notes persist server-side |
| `claims-register.html` | Reported behavior → candidate mechanism → discriminating test |
| `unexplored-window.html` | Where the parameter space is genuinely open |
| `gradient-coupling-dossier.html` | The original evidence ledger — documented / testimony / refuted |

The four HTML files are published as private artifacts. The map carries a database, so
notes added to nodes persist across sessions and can be read back.

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
needs a theorem — and in six cases the theorem already exists, unread.

---

## Ready to run now

Requiring no apparatus, no funding, no access:

- **Co-citation audits.** Three tables are publishable as-is — gradient harvesting,
  multifunctionality, and the 578-reference criticality audit.
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
- Corrections are logged in `FINDINGS.md` rather than silently fixed. The pattern of
  errors is itself information.
