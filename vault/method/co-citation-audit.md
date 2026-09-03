---
name: co-citation-audit
type: method
---

# The co-citation audit

The measurement that turned this project from pattern-noticing into something checkable.

**Method:** take two literatures that describe the same move; query how many papers cite
both; **report the number and inspect the hits.**

Run against OpenAlex (`api.openalex.org`) or Semantic Scholar
(`api.semanticscholar.org/graph/v1`). Both free. OpenAlex has a daily budget that exhausts
quickly; Semantic Scholar has been more reliable.

## Also useful: reference-list audits — with one hard precondition

Take a major review in field A and count how many of its references come from field B.

**Open the bibliography first.** This project ran that audit on a *Reviews of Modern Physics*
colloquium on biological criticality, reported it as **578 references citing zero engineering
work**, and promoted it as publishable. When someone finally extracted the PDF it was
**595 references** — and **the bibliography carries no article titles at all**, only venues.
The subject characterisation was reading a field that does not exist in the data, and five
IEEE entries make "zero engineering" false as worded. See [[G4-criticality-as-design]].

The precondition, therefore:

1. **Fetch the reference list itself.** Not a summary of it, not a count someone reported.
2. **Check what fields it actually contains.** Titles, venues, DOIs — you can only classify on
   what is there.
3. **State which field you classified on.** "Zero engineering *by venue*" is a claim. "Zero
   engineering" is a claim about subject matter, and a title-free bibliography cannot support it.

A reference-list audit is a strong instrument precisely because one number carries so much
weight. That is also why an unverified one propagates so far — this one reached five files.

## What it cannot do

Everything in [[failure-modes]]. Five ways a zero can be fake, all five observed here, and
five findings lost to them.

**It is an input to [[relationship-description]], not a verdict.** See
[[verdict-scoring|why]].

## Ready to run

**Two** tables from this project are publishable with nothing but the queries: the
gradient-harvesting zeros and the multifunctionality zeros — the latter now also survived a
full-text re-read, see [[G6-multifunctionality]].

**The criticality audit was the third and is withdrawn from that list.** Its numbers did not
survive contact with the actual bibliography.
