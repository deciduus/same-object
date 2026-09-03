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

## Also useful: reference-list audits

Take a major review in field A and count how many of its references come from field B. A
**578-reference** *Reviews of Modern Physics* colloquium on biological criticality cites
**zero** engineering work. One number, more weight than any amount of argument.

## What it cannot do

Everything in [[failure-modes]]. Five ways a zero can be fake, all five observed here, and
five findings lost to them.

**It is an input to [[relationship-description]], not a verdict.** See
[[verdict-scoring|why]].

## Ready to run

Three tables from this project are publishable with nothing but the queries: the
gradient-harvesting zeros, the multifunctionality zeros, and the 578-reference criticality
audit.
