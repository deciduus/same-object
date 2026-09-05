---
id: G27
name: G27-collective-decision
type: gap
standing: narrowed
evidence: citation-intersection
contact-surface: 1
crosses: formalism
crosses-rank: 4
topology: direct
mediator: 
borrows-from: []
lends-to: []
mutual-with: []
computed-in: []
uses-move: []
rests-on: []
tags: [node/gap, crosses/formalism, evidence/citation-intersection, standing/narrowed]
last-checked: 2026-09-05
note: "Overturned on a query that never tested this gap - ants vs bees is swarm-internal. Citer-set intersection of swarm anchors against consensus anchors returns 0, 0, 1, 1 (OpenCitations, 2026-09-05); the one real bridge is ACM TAAS 2012. The 26 and 551 are UNSOURCED. Reverted to narrowed 2026-09-05 (orchestrator, on the agent's evidence)."
---

# Collective decision

**STANDING: NARROWED** (was overturned on a string count that tested the wrong pair; reverted 2026-09-05) · evidence: citation-intersection · contact surface: 1 · last checked 2026-09-05

> Swarm intelligence and distributed-systems consensus both solve *reach agreement across unreliable distributed agents.*

## Overturned, and instructive

The claim was zero co-citation in every pairing. `"ant colony optimization" AND "honeybee"`
returns **26 in the original, unmodified query** — and 551 under synonyms. **Both numbers are
UNSOURCED, neither reproduces, and the query does not test this gap. See the Provenance block
below.** Papers exist titled
*A Distributed Consensus Model for House-Hunting in Temnothorax Ant Colonies* and *Efficient
Swarm Consensus: RLR vs Raft.*

**Only the literal string "Paxos" is isolated, because Paxos is one algorithm's proper noun
rather than a literature.** The zero measured a name.

This is the specimen case for [[failure-modes]] mode 3.

## What might still be there

**Message complexity.** The speed-accuracy tradeoff is explicit on both sides — quorum thresholds
in bees, latency bounds in consensus protocols — but the third axis, cost per unit communication,
is formalised only in distributed systems. Untested since the withdrawal.

## Provenance

### The 26 and the 551 are UNSOURCED, and they measured the wrong pair

No host, endpoint or date was ever recorded. Re-run 2026-09-05:

| Provider | Query | N |
|---|---|---|
| OpenAlex | `filter=title_and_abstract.search:"ant colony optimization" AND honeybee&mailto=...` | **32** |
| OpenAlex | same with `fulltext.search:` | **1,019** |
| Europe PMC | `.../webservices/rest/search?query="ant colony optimization" AND honeybee&format=json` | **38** |

Neither 26 nor 551 reproduces. Both stay **UNSOURCED**.

**The deeper problem is not the number.** `"ant colony optimization" AND "honeybee"` is a
*swarm-internal* query - ants against bees. This gap is about **swarm intelligence against
distributed-systems consensus**. The 26 never touched the pairing it was used to overturn. The
note correctly diagnosed that "Paxos" measured a name; it then overturned on a query that
measured a different relationship entirely.

### Citer-set intersection, run on the pairing the gap actually names

**Provider: OpenCitations. Endpoint: `api.opencitations.net/index/v1/citations/<doi>`. Date: 2026-09-05.**
Script `vault/_scripts/intersect.py`; recipe in [[citation-sources]]. No reference lists are
involved, so coverage is 100% of the provider's index.

Anchors, all DOI-verified against Crossref (`api.crossref.org/works/<doi>?mailto=...`, 2026-09-05):

| Side | Work | DOI | N citers (OpenCitations) |
|---|---|---|---|
| swarm | Dorigo, Maniezzo & Colorni 1996, *Ant system* | `10.1109/3477.484436` | 8,814 |
| swarm | Seeley & Buhrman 1999, *Group decision making in swarms of honey bees* | `10.1007/s002650050536` | 267 |
| consensus | Lamport 1998, *The part-time parliament* (Paxos) | `10.1145/279227.279229` | 1,914 |
| consensus | Lamport, Shostak & Pease 1982, *The Byzantine Generals Problem* | `10.1145/357172.357176` | pooled |
| consensus | Fischer, Lynch & Paterson 1985, *Impossibility of distributed consensus with one faulty process* | `10.1145/3149.214121` | pooled with the above: 6,735 |

| Pairing | intersection | expected (N=1.6x10^8) | obs/exp |
|---|---|---|---|
| Dorigo 1996 x Paxos | **0** | 0.11 | - |
| Seeley 1999 x Paxos | **0** | 0.003 | - |
| Dorigo 1996 x (Byzantine + FLP) | **1** | 0.37 | 2.7 |
| Seeley 1999 x (Byzantine + FLP) | **1** | 0.01 | 89 |

Both hits inspected (Crossref, 2026-09-05):

- `10.1201/9781420038880.bmatt` - *Disruptive Security Technologies...*, item title "References".
  A book's **back-matter bibliography**, indexed as a work in its own right. Not a bridge; a
  cataloguing artifact.
- `10.1145/2168260.2168264` - **Host selection through collective decision**, *ACM Trans.
  Autonomous and Adaptive Systems* 2012. A **genuine bridge**: bee-style collective decision
  making inside a distributed-systems venue, citing the Byzantine/FLP canon.

**So the honest contact surface is 1, not 26.**

### Why `overturned` should be reverted

The zero this note retracted was never measured. When it *is* measured - five anchor pairings,
100% coverage, both hits read - the answer is **one real bridge across ~8,800 swarm citers and
~6,700 consensus citers**. That is a gap, not a closed one.

Two caveats, stated so the revert is not itself an overclaim:

1. **A zero here is weakly informative.** Under independence the Dorigo x Paxos pairing expects
   0.11 works, so observing 0 is exactly what chance predicts. The *low* numbers, not the zeros,
   are what carries the evidence.
2. **Algorithm-paper anchors risk the very trap this note diagnosed.** Dorigo 1996 and Lamport
   1998 are single-algorithm papers. Broadening the consensus side to Byzantine + FLP (6,735
   citers) is the corrective, and it moved the count from 0 to 1 - not to a literature.

**Proposed in [[log]], not applied here:** `standing` `overturned` -> **`narrowed`**, `evidence`
`string-protocol` -> **`citation-intersection`**, `contact-surface` 26 -> **1**. Narrowed rather
than live, because one real bridge does exist, and because the surviving claim is the sharper one
this note already identified: **message complexity - cost per unit communication** - formalised
on the distributed-systems side and absent on the swarm side.
