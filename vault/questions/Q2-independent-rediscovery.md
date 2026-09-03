---
name: Q2-independent-rediscovery
type: question
arises-from: ["[[G1-gradient-coupling]]", "[[G19-safety-factor-derived-twice]]", "[[G28-marginal-value-gittins]]"]
status: open
---

# Is independent rediscovery a countable phenomenon?

> The project keeps finding the same event and has been recording it one instance at a time.
> **It has happened at least five times in twenty gaps.** That is not an anecdote, it is a rate.

## The instances, all found separately

| Result | Derived once | Derived again | Gap |
|---|---|---|---|
| Onsager off-diagonal figure of merit | Kedem & Caplan **1965** | Morrison & Osterle **1965** — same year, no contact | [[G1-gradient-coupling]] |
| Stress–strength interference | Reliability engineering **1967** | Alexander **1997**, from scratch, 30 years late | [[G19-safety-factor-derived-twice]] |
| Optimal stopping rule | Stopping theory | Green **1984**, in foraging vocabulary | [[G28-marginal-value-gittins]] |
| The Charnov ≡ Gittins identity | [[C5-charnov-gittins]] | a 2024 paper, zero occurrences of "Gittins" | [[G28-marginal-value-gittins]] |
| Ordinal passivity ladder | IAEA 1991 | exoskeletons, structural control, façades | [[G7-how-passive]] |

## Why this is the more interesting object

Each gap entry treats its rediscovery as *evidence for that gap*. But the rediscoveries
themselves form a class, and **the class has properties the instances do not:**

- **Two of them are near-simultaneous** (1965/1965). That is not a reading failure — nobody was
  late. It suggests a result becomes derivable when its prerequisites land, and gets derived
  wherever the prerequisites exist.
- **The rest are 20–40 years apart**, which is a reading failure.

Those are different phenomena wearing the same label, and this project has been counting them
together.

## The question

Can independent rediscovery be measured rather than anecdoted? Specifically: **what is the
distribution of lag between first derivation and independent re-derivation**, and is it
bimodal — a simultaneity peak from shared prerequisites, and a long tail from unread literature?

## Why it might be answerable

The detection method already exists here. A rediscovery leaves a signature: two works stating
the same relation with **no citation path between them**. [[citation-intersection]] finds
exactly that, and [[citation-sources]] gives three working providers.

## What it would change

A simultaneity peak is a claim about the **structure of knowledge** — results are ripe or not.
A long tail is a claim about **the literature's plumbing**. The first is not fixable and the
second is. Knowing the ratio tells you whether projects like this one are worth running.
