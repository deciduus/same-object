---
name: research-round
description: How to plan and run one research round in this vault as the orchestrator — diagnose the record first, pick a method shape that is not the last one, run new ideas through a researcher→critic gauntlet (2 rounds, 3 for release candidates), use one-to-one comparisons only to locate a place to dig, and integrate results with the vault's provenance and lint rules. Use this whenever you are about to launch agents on a lead, a gap, a computed note, an audit, a critic pass, a scout, a deep dive, a paper draft, or when the user says "keep pushing", "next round", "go deep on X", "critic pass", "what's next", or asks what to work on. Use it even for a single agent, because the brief rules and the file-ownership rules apply to one agent as much as to eight.
---

# Research round

You are the orchestrator. You own the diagnosis, the choice of method shape, the briefs, and the
integration. Agents (Opus 4.8) execute one well-scoped task each and report back. The vault's
contract is `CLAUDE.md`; this skill is about how to run a round so that what comes back is
trustworthy and not a repeat of the last round.

Read `references/pitfalls.md` once per session. Read `references/briefs.md` when you write a brief.

## 1. Diagnose before you delegate

Write two or three sentences, for yourself, before launching anything: what survived the last
round, what died, and why. Then pick the move that follows from that, even if it is not on the
backlog. The record so far says:

- Derivations, pre-registered catalogues, and instrument runs survive audits.
- Empirical correlations found in joins, and same-object comparisons of famous pairs, mostly
  land on prior art or join artefacts.
- A comparison finds a place to dig. The digging is where results live.

If your plan is "run the next backlog item with the same four legs as last time", stop and ask
what a different shape would look like. Name the previous round's shape in your diagnosis, and
name the shape you are choosing instead. A plan that does not say what it is not repeating
usually repeats it. The registers to pick from are `vault/program.md`
(what could be computed), `vault/walls.md` (what nobody has measured), and
`vault/method/failure-taxonomy.md` (what went wrong before).

## 2. Choose a method shape

Rotate among these. Do not run the same one twice in a row unless the first run explicitly
asked for a second.

| Shape | Use when | Output that counts |
|---|---|---|
| Derivation-first | A bridge or identity already holds and could emit a number that can be wrong | A prediction with a named dataset or experiment |
| Data-first | An open dataset with an API exists and a join nobody ran is cheap | A table with per-row provenance and a pre-registered pass/fail |
| Instrument-first | A validated audit exists and there is an open public case | An output state (halt, NO RESIDUAL, residual spec) and a calibration against a known answer |
| Simulation | A model was derived but never run forward | A pre-registered prediction table with seeds and a failure list |
| Gauntlet | A new idea, synthesis, or candidate finding | A claim that survived two independent critics, or a documented kill |
| One-to-one comparison | Only to locate where two fields might hold halves of a result | A place to dig, never a headline |
| Build | The only remaining test is physical | A protocol and analysis script for a human at a bench |

## 3. The gauntlet for new ideas

Use this for anything that might be a new claim: a synthesis, a proposed identity, a candidate
finding, a paper draft. Two rounds by default. Three if it is a release candidate.

1. **Researcher** produces the claim with its derivation or computation, a `>` callout in the
   first ten lines, a Provenance block, and an §Honesty section naming the first attack.
2. **Critic 1** has only the researcher's output (not the vault's prior view, not your opinion).
   Its job is to kill the claim: prior art via `refsweep.py` on the anchors, metaphor test, join
   scale, effect size vs p, pseudoreplication by source, the comparator clause, what a referee
   from each side attacks first. Ask it for at least one test the researcher did not run: a
   permutation null stratified on the confound, an out-of-sample split, a practitioner-decision
   test ("what would a soil scientist do differently on Monday"). A critic that only re-reads
   the researcher's own tests confirms them. Verdict: KILL / NARROW / SURVIVES with a grade.
3. **Researcher revises** against the critic's exact sentences. Every number old → new.
4. **Critic 2** is a different agent with a different angle (theory if critic 1 was empirical,
   empirical if critic 1 was theory). Same verdict format.
5. **Synthesis** is yours: decide the standing, record any disagreement between critics without
   resolving it by fiat, and write the log entry. Do not let a critic edit the note; critics write
   to `audits/` and stage proposed edits in a PENDING file.

Why two critics: one critic anchors on one attack. The two together cover theory and data. Why
the researcher never sees the vault's prior guess before critic 1: the project's own advance
prediction of an audit's halt state was once wrong, and a runner who had read it would have
reproduced the error.

The order is the point, so keep it sequential. Two critics launched at the same time on the
first draft are one round of criticism, not two: they attack the same weaknesses, the researcher
never answers either, and nothing tests whether the revision holds. Critic 2 reads the revised
note and critic 1's report, so it can attack what the revision introduced. If you find yourself
launching critics in parallel with researchers to save wall-clock time, you have turned the
gauntlet back into a one-pass audit.

Every researcher brief carries three things that the critics will check for and that a plan
without them will fail on: a pre-registration hashed before any outcome is fetched (the
prediction, the pass/fail rule, the named test); at least one positive control (reproduce a
number the source already reports) and, where the instrument can return nothing, a negative
control; and a single owner for each API budget the round uses.

For a release candidate, add a **cold referee**: an agent that reads only the manuscript or note,
recomputes every number, and returns accept / minor / major / reject with three questions.

## 4. Briefs

A brief is the whole contract with an agent. Write it so the agent can work without this
conversation. Every brief carries:

- The exact files it may touch, and the files it must not. One owner per file per round.
- What to read first, in order, and what not to read before which step (blinding).
- The task as numbered steps with a done-condition each.
- Which API providers to use and which are budget-locked. One owner per API budget per round;
  parallel agents on OpenAlex exhaust it in minutes. Put the assignment in the plan as a table
  (provider → agent) and give every other agent "Providers: none" or Crossref only. A brief that
  names an owner and then hands a second agent "eight search formulations" has two owners.
- Log entries go to a `PENDING-log-<ID>.md` file, never to `log.md` or `00-index.md`; you merge.
- A `>` callout in the first ten lines stating the result in one sentence.
- "Report: …" listing exactly what you want back.

Templates for each role are in `references/briefs.md`. For anything pre-registered, the brief is
written and sha256-hashed before any outcome is fetched, and for a blind run it is written by a
different agent than the one that runs it, with no verdict words. "Anything pre-registered"
includes a build protocol that states an expected effect size, a covariate list, or a falsifier:
those are predictions, and a protocol that fixes them after the pilot is not a test.

## 5. Before any claim of novelty

Run `python vault/_scripts/refsweep.py --anchors <dois> --phrases "<phrase>" ...` on the claim's
anchors before the callout is written. Paste the top hits with a one-line verdict each. The
note may not claim novelty for anything that appears there. Pass every spelling of a unit
("kJ/mol" and "kJ mol"). This step exists because three kills in one day were prior art sitting
in the deposited reference list of a source the project had already read in full.

## 6. Integrate

After agents report, in this order:

1. Merge `PENDING-log-*.md` entries into `vault/log.md`; add index lines to `vault/00-index.md`
   (computed notes by hand, gaps via `python _idx.py`); delete the PENDING files; replace any
   `[[PENDING-log-*]]` link with `[[log]]`.
2. Apply staged edits that are yours to decide (standing changes, disagreements) and record the
   decision in the log. Do not silently pick a side between two critics; write both.
3. `cd vault && python _lint.py` → 0 errors; `powershell -ExecutionPolicy Bypass -File check.ps1`
   from the root → CHECK OK.
4. Commit with a subject that states what the project now believes, push to master. Never tag a
   release for an incremental round; only for a verified no-caveats finding the user has read.
5. Report to the user in plain language: what died, what survived, what is new, what is next.
   Numbers in a table, not prose.

## 7. Things that look like progress and are not

- Another scout sweep when the last two produced kills. Scouts find places to dig, not results.
- A deep dive with the same four legs as the last deep dive. Vary the legs.
- A "correction" that is not held to the standard of what it corrects.
- A headline that compares an energy ratio to a capacity margin, a fitted lifetime shape to a
  decay rate, or a global column to a local signal. Same object, same scale, or say why not.
- A halt or verdict announced in the brief. Then the agent reports it, and nothing was tested.
- Five agents on one API. One budget, one owner.
