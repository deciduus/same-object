# Pitfalls seen in this project, with the guard for each

Full detail: `vault/method/failure-taxonomy.md` (26 modes, 82 instances). This is the short list
an orchestrator needs in working memory.

| What went wrong | Instance | Guard |
|---|---|---|
| Prior art sat in an anchor's own reference list | C53: Hu 2016 in Yung 2018's deposited refs, which C49 had read in full | `refsweep.py` before any novelty claim |
| A correlation found in the data was written up as pre-registered | C43 ρ(T,P) | Hash the brief before the join; anything found after is exploratory |
| Pseudoreplication by source study | C43: five studies supplied a third of 1,053 sites | Cluster bootstrap by source, in the brief |
| An obvious covariate not reported | C43 slope; C40 bats; C52 migration | Name the covariates in the brief; report with and without |
| Energy ratio vs capacity margin; lifetime shape vs decay rate; global column vs local signal | C33; C18; C53 | Same object, same scale, or state why not |
| A published margin adopted as if computed | C30 three rows; C29 40^−0.413 | Every number shows its inputs; "restated" vs "independent" column |
| Halt announced in the brief | C30 | Blind brief, different writer, no verdict words |
| Single-agent blind | C46, C50 | Two-agent blind; next: anonymised case |
| A correction that was itself wrong | "46 was stale"; 578/595 | A withdrawal meets the evidence bar of what it withdraws |
| Two true numbers for two objects treated as one wrong number | 578 vs 595; G28's 8 vs 5 | Say which object each number measures |
| Phantom count from a blank key | intersect.py | Drop blank keys; `--selftest` |
| False zero from a missing field | Europe PMC citations lack `doi` | Own keyspace per provider; a zero is a claim about the instrument until calibrated |
| Parallel agents exhaust one API | OpenAlex daily budget with 5 agents | One owner per budget per round |
| Two agents on one file | 00-index drift; duplicate bib keys | One owner per file; PENDING logs; the orchestrator merges |
| A state assumption hidden in a table column | C25 t* assumed arrival at a full patch, ×3.8 | Check every state assumption per column |
| Positive control never run | C33 policy overshoot 2.3× | Reproduce the source's own number before extending it |
| Headline says more than the body | C28 callout; C19 window | Write the callout last and check it against §Honesty |
| Famous-pair same-object comparisons | C9, kedem-caplan, C6, G36 | Use comparisons to locate, not to claim |
| Stale watcher notifications mistaken for results | several | A notification is not a result; check `git status` |
