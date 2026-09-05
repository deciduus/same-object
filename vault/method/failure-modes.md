---
name: failure-modes
type: method
---

# Six ways a measured zero can be fake

Learned by failing all five. Nineteen findings re-tested; **five withdrawn, four weakened.**

## 1. Punctuation and tokenization
`"Miner's rule" AND "bone"` -> **0**. `"Miner rule"` -> 2. `"Palmgren-Miner"` -> 6.
Same concept. **An apostrophe artifact** — not a synonym problem at all.

## 2. Homographs
A word both fields own. See [[homographs]] for the twelve-entry register. The
multifunctionality check threw up **9,570** hits that were entirely materials science and
would have "refuted" a finding that is genuinely real.

## 3. Proper-noun narrowness
`"Paxos"` is one algorithm's name, not a literature. This killed [[G27-collective-decision]].
`"Buckingham"` is also **a developmental biologist's surname**, and it killed
[[G22-scale-transfer-triage]].

## 4. Synonyms
The mildest case, and the one this section was originally named for. Killed
[[G11-plant-gravisensing]]: the literature says *gravisensing*, not *gravitropism*.

## 5. Boolean relaxation — this one manufactures fake **nonzeros**
Search engines relax to partial matching as OR-groups grow:

    two phrases, AND                          ->     1
    same, with synonyms added to each side    -> 1,169

A thousand-fold jump from adding synonyms is the engine giving up on strict matching, not a
bridge population. **Only 2-phrase conjunctions are trustworthy.**

## 6. Diachronic terminology drift

**The first mode on this list that is not synchronic.** Modes 1-5 all assume the two names
coexist and you failed to try both. Mode 6 is the case where they *never* coexisted: the concept
was called one thing in the 1960s and something else by the 2010s, so a single string or citer
query run "now" sees only the later half of its own window and calls the earlier half absent.

A citer window is typically decades wide. A vocabulary is not.

### The required step

**Run the concept under each decade's name, across the whole citer window.** Concretely, before
reporting a zero from a search whose window spans more than one decade:

1. Bin the citer window by decade.
2. For each decade, establish what that decade's literature called the object — from a review
   published *in* that decade, not from today's vocabulary.
3. Re-run the query under each decade's name and report the per-decade counts, not the pooled
   one.
4. A zero survives only if it is a zero in **every** decade bin under that decade's own name.

A pooled zero across a 60-year window is not one measurement; it is six, and mode 6 is what
happens when five of them were never made.

### Specimen: kedem-caplan

**Chosen over the symmorphosis / [[G20-resize-vs-throttle]] case**, which is genuinely a
*cross-field* renaming (computing says "over-provisioning accuracy" where physiology says
"symmorphosis") and is already covered by the mechanism named below — anchoring on the
originating field's term. That one is synchronic: both names are in use at the same time. The
kedem-caplan case is the diachronic one.

From [[log|vault/log.md]], 2026-09-03, `correction | kedem-caplan is not an unread theorem`:
the Kedem-Caplan degree-of-coupling result (1965) was catalogued as unread on the strength of
**2 co-citers** between two named 1960s papers. The re-read found it in active use — *Entropy*
25:1575 (2023) applying it to thermoelectrics and oxidative phosphorylation together, and
arXiv:2403.20209 cloning the form into a hydronic figure of merit.

**Why this is mode 6 and not mode 4.** The 1960s object did not stay under its 1960s name. It
travelled into thermoelectrics as the **figure of merit `ZT`**, and later work carries the
formalism under that name without the eponym. A co-citer count anchored on the two 1965-era
papers was therefore measuring 1960s-vocabulary traffic across a window whose later decades had
stopped using 1960s vocabulary. The log's own diagnosis — *"the 2 co-citers figure measured
traffic between two named papers, not whether the result had travelled"* — is exactly the
diachronic failure: the result had travelled, and it changed its name on the way.

The correction cost the project one of its headline entries, which is why it is the specimen.

## Rule: a string count cannot overturn a gap on its own

**A string-match count may not move a gap to `overturned` unless it names host + query string +
date.** Without those three, the number is not re-testable, and this project's own record says
the string protocol fails re-test **more than half the time, in both directions** — manufacturing
fake zeros (modes 1-4, 6) and fake nonzeros (mode 5).

An overturning is a withdrawal, and [[relationship-description]]'s symmetry rule says a
withdrawal must meet at least the standard of the claim it withdraws. A bare count meets no
standard at all.

**Required before `standing: overturned` on a string-protocol basis:**

- **host** — which index answered (Europe PMC, OpenAlex, Crossref, Google Scholar, a publisher
  site); the same query returns different counts on different hosts;
- **query** — the exact string, verbatim, including quoting and Boolean structure, since modes 1
  and 5 both live in punctuation and operator handling;
- **date** — counts move.

Absent any of the three, the correct action is to record the count as an *unverified lead* and
re-test under [[citation-intersection]] before touching `standing`.

### Specimens: G8 and G27

Both are currently `standing: overturned` with `evidence: string-protocol`, and neither carries
the three fields.

- **[[G8-energy-per-bit-axis]]** — overturned on `"Landauer" AND (neuron OR synapse OR brain)`
  returning **575**. The query is recorded; **the host and the date are not.** A four-term
  disjunction is also exactly the shape mode 5 says relaxes to partial matching, so 575 is a
  number that this note's own rules say to distrust.
- **[[G27-collective-decision]]** — overturned on a query returning **26** unmodified and **551**
  under synonyms. The 21-fold jump on adding synonyms is mode 5's signature, so the 551 is
  unusable by rule; the load-bearing figure is the 26, and **its host and date are not
  recorded.**

Neither retraction meets the bar this section sets. That does not restore either gap — the
underlying readings may well be right — but both standings rest on numbers no one can re-run,
and they are the reason the rule is written.

## The mechanism underneath all of them

> **Anchoring on the term the *originating* field uses, rather than the term the *target*
> field uses.**

"Buckingham," "gravitropism," "Berg-Purcell" each produced a clean, confident, wrong zero.

**Corollary:** any zero anchored on a proper noun is unverified until re-tested by
[[citation-intersection]]. On this project's evidence the prior for such a finding surviving
is well under one half.

## The protocol

- **Calibrate first** — prove each side is findable at all.
- **Every alternate name** on both sides.
- **Never anchor** on a proper noun, a possessive, or a shared word.
- **Inspect the hits.** Irrelevant nonzero is still a zero; relevant nonzero is a collapse.
- **Bin by decade** and re-run under each decade's own name (mode 6). A pooled zero across a
  multi-decade window is not one measurement.
- **Never overturn on a bare count.** Host + query + date, or it is a lead, not a retraction.
- **Prefer [[citation-intersection]]** wherever the citer count is tractable.
