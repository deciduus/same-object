---
name: Q3-theory-cited-hardware-omitted
type: question
arises-from: ["[[G4-criticality-as-design]]"]
status: open
---

# Why cite a person's theory and omit their device?

> The strangest thing found in the whole audit, and it was almost thrown away as a footnote.

## The observation

The *Reviews of Modern Physics* colloquium on biological criticality cites **Kern & Stoop PRL
2003** and **Stoop & Gomez PRL 2016**. Stoop is also the author of the **Hopf-bifurcation
electronic cochlea** — working hardware implementing the exact principle the review is about.

**The review cites the person and skips the device.**

This was found while checking whether the bibliography contained engineering work. It is far
more interesting than the answer to that question.

## Why it matters more than a blanket absence

A review citing *no* engineering is a plumbing failure — two literatures that never met. This is
different and stranger: **the author was read, and the hardware half of their work was
filtered out.**

That is a selection happening inside a single reader's attention, not between fields. It cannot
be explained by "they don't read that journal," because they read that author.

## The question

Is there a systematic **artefact filter** — do theoretical reviews preferentially cite the
theoretical output of authors whose work spans theory and device, even when the device paper is
the more direct evidence for the review's own thesis?

## Why it might be answerable

It is directly measurable and the method already exists here. Take authors with both theory and
device publications on one principle. Take reviews citing them. **Compute the ratio of theory
citations to device citations, against the base rate of what those authors published.**
[[citation-sources]] supplies everything needed.

A positive control is available too: engineering reviews citing the same authors should show the
opposite skew, or the effect is an artefact of what got indexed.

## What it would change

If real, it is a named and correctable bias with a direct bearing on this project's whole
method — every gap here rests on reading bibliographies, and **a bibliography would then be a
biased sample of what its author actually knows.** That weakens the reference-list audit as an
instrument, which is worth knowing given how much weight [[co-citation-audit]] puts on it.
