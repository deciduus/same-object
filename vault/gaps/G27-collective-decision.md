---
name: G27-collective-decision
type: gap
status: overturned
---

# Collective decision

> Swarm intelligence and distributed-systems consensus both solve *reach agreement across unreliable distributed agents.*

## Overturned, and instructive

The claim was zero co-citation in every pairing. `"ant colony optimization" AND "honeybee"`
returns **26 in the original, unmodified query** — and 551 under synonyms. Papers exist titled
*A Distributed Consensus Model for House-Hunting in Temnothorax Ant Colonies* and *Efficient
Swarm Consensus: RLR vs Raft.*

**Only the literal string "Paxos" is isolated, because Paxos is one algorithm's proper noun
rather than a literature.** The zero measured a name.

This is the specimen case for [[failure-modes]] mode 3.

## What might still be there

**Message complexity.** The speed-accuracy tradeoff is explicit on both sides — quorum thresholds
in bees, latency bounds in consensus protocols — but the third axis, cost per unit communication,
is formalised only in distributed systems. Untested since the withdrawal.
