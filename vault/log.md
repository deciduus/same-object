---
name: log
type: method
---

# Operations log

Append-only. One line per structural change to the vault. Format:
`## [YYYY-MM-DD] operation | description`

## [2026-09-03] atomic-schema migration | 20 gap notes converted

Prose frontmatter replaced with filterable data. `contact-surface: "0 crossings, both
directions"` became `contact-surface: 0` plus `crosses`, `crosses-rank`, `topology`,
`mediator`. Six typed directional edge fields added. Tag mirrors added.

Reason: prose in a machine field cannot be sorted, filtered, or linted. The defect that
prompted it — [[verdict-scoring]] was marked retired while a gap still carried
`status: holds` — was a retired word sitting in current frontmatter with nothing to catch it.

## [2026-09-03] lint extended | atomic vocabularies enforced

`_lint.py` now checks the `crosses` vocabulary, that `crosses-rank` agrees with `crosses`,
the `topology` vocabulary, that `mediated` and the `mediator` field agree, that
`contact-surface` is a bare integer, and that all six edge fields are present.

## [2026-09-03] graph and Bases added | zero plugins

`triage.base` and [[graph-view]]. Both are core Obsidian. Bases reads YAML frontmatter only,
which is why the migration had to land first.
