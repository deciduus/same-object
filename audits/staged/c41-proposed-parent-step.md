---
name: PENDING-log-C41
type: method
---

# PENDING for C41 — log entry and index line, not yet applied

This file is a staging area written by the C41 run. Nothing here has been merged into
`log.md`, `00-index.md` or `method/citation-intersection.md`. Apply or discard by hand.

---

## 1. Proposed entry for `log.md` (newest first, at the top)

```
## [2026-09-05] honest null | The C37 "uncited parent" pattern is not general: 3 of 8, not most

C37 found grid adequacy and bird starvation each rebuilding Cramer-Lundberg ruin theory with
neither citing it, and asked whether the project's cross-domain gaps are usually two fields
that both rediscovered an older parent. C41 named a candidate parent for eight confirmed
same-object pairs and measured all three pairwise citer-set intersections (A x B, A x P,
B x P) on OpenCitations and Semantic Scholar, 2026-09-05, script _scripts/c41_parents.py.

Result: 2 class-i (both sides meet the parent), 3 class-ii (one side), 3 class-iii (neither -
the C37 pattern). The hypothesis is NOT supported, and the sample was the most favourable
one available. What survives is a diagnostic: in 5 of 8 rows the third anchor names WHICH
side is isolated, which a two-way intersection cannot. Ecology co-cites Kramers 1940 21-23
times while prognostics does so 0 times; reliability meets Wright 1936 5-6 times while
adaptive management does not.

Six anchors are invisible to Semantic Scholar (three monograph DOIs, Wald 1945, Kimura 1963
and Charnov 1976), and Kaplan-Meier 1958 exceeds its paging cap, so rows 1, 2 and 4 are
single-provider. Lundberg 1903, Cramer 1930, Feller 1968, Erlang 1917, Snell 1952,
Chow-Robbins-Siegmund 1971, Cox 1962 and Crow 1974 have no usable DOI and were replaced by
an indexable member of the same literature; Snell's proposed DOI 404s at Crossref.
```

## 2. Proposed line for `00-index.md`, in the computed block

```
- [[C41-uncited-parent-sweep]] — **is C37's uncited-parent pattern general? No — 3 of 8.** Eight confirmed same-object pairs, a named candidate parent theory each, and all three pairwise citer-set intersections on two providers (OpenCitations, Semantic Scholar, 2026-09-05): 2 rows where both sides meet the parent, 3 where one does, **3 double rediscoveries**. The hypothesis that cross-domain gaps are usually two fields that both rediscovered an older formalism is not supported on the project's own most favourable sample. What survives is a diagnostic that fires in 5 of 8 rows: the third anchor names *which* side is isolated — ecology co-cites Kramers 1940 21–23 times against prognostics' 0, reliability meets Wright 1936 5–6 times against adaptive management's 0 — turning a symmetric "gap" into a one-way borrow. Union-floor `E` only; six anchors invisible to Semantic Scholar, so rows 1, 2 and 4 are single-provider
```

## 3. PROPOSED edit to `method/citation-intersection.md` — NOT APPLIED

**The trigger the brief set was not met.** It asked for a mandatory "parent search first" step
*if most gaps turn out to be class iii*. Three of eight is not most, so the proposal below is
deliberately weaker: an optional third anchor, justified by its diagnostic value rather than by
a base rate. **Do not apply it as written without deciding whether an optional step earns a
place in a method note that is otherwise all mandatory.**

> ### The third anchor: search for the parent
>
> A two-way intersection `A × B` answers "do these literatures meet?". It cannot answer "is
> either of them already inside an older literature that contains the shared object?" — and
> when a gap is stated as a *shared formalism*, that older literature usually exists and is
> nameable. Before quoting an `A × B` zero, name the candidate parent theory `P`, find a
> **citable** anchor for it, and run all three intersections.
>
> Four outcomes, each a different claim:
>
> | | `A × P` | `B × P` | reading |
> |---|---|---|---|
> | **(i)** | > 0 | > 0 | Both fields are already in the parent literature. The gap is the sibling link only, and is smaller than it looks |
> | **(ii)** | > 0 | 0 | **One-way borrow.** One field stands outside a literature the other is inside. Repair is a one-directional import, not an introduction — see [[one-way-borrowing]] |
> | **(iii)** | 0 | 0 | **Double rediscovery.** Two fields rebuilt the parent independently. The strongest form of the gap claim, and the rarest |
> | **(iv)** | — | — | The parent has no usable DOI. Say so; do not report a zero |
>
> **Outcome (iv) is common and must be reported, not worked around.** Pre-1960 classics and
> monographs are badly indexed: [[C41-uncited-parent-sweep]] could not reach Lundberg 1903,
> Cramér 1930, Feller 1968, Erlang 1917, Snell 1952, Chow–Robbins–Siegmund 1971, Cox 1962 or
> Crow 1974 at all, and Semantic Scholar holds no record for three monograph DOIs, for Wald
> 1945, or for Charnov 1976. A substituted anchor is a proxy for the literature, never the
> parent itself, and the substitution belongs in the note.
>
> **Two cautions.** The intersection measures **co-citation, not descent**: `A × P > 0` says
> the two literatures share readers, not that A cites P. And **the parent is a judgement** —
> a different `P` can move a row's class, so name the alternatives you rejected.
>
> Worked in full: [[C41-uncited-parent-sweep]], on eight pairs. Its headline is a negative —
> the double-rediscovery outcome (iii) fired in 3 of 8 rows, so this step is a **diagnostic
> that sharpens a gap's description**, not a filter expected to overturn most gaps.
