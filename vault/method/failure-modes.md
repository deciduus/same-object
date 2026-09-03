---
name: failure-modes
type: method
---

# Five ways a measured zero can be fake

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
- **Prefer [[citation-intersection]]** wherever the citer count is tractable.
