# Audited-record preprint: build notes

Draft methods / meta-research preprint, assembled from vault notes
`computed/C51-vault-meta-analysis`, `method/failure-taxonomy`, `log.md`, `novelty-audit`,
`predictions`, `strategy`, `method/reservoir-audit` (Part D), `_scripts/c51_data/claims.csv`,
and the twelve `audits/blind-brief-*.md` files. Nothing in this folder edits the vault; the
vault remains the source of truth for every number.

Target venues: a meta-research or research-on-research outlet, or arXiv `cs.CY` / `cs.DL`.

## Build

```
pandoc paper.md --citeproc --bibliography=refs.bib -o paper.pdf
```

Requires a LaTeX engine on PATH (TeX Live / MiKTeX) for PDF output. For a quick check
without LaTeX:

```
pandoc paper.md --citeproc --bibliography=refs.bib -o paper.html
```

Add `--csl=<style>.csl` if a journal style is required; without it Pandoc uses its default
(Chicago author–date). The manuscript uses Pandoc's table-caption syntax (a line beginning
`: ` above each table), so build with a Pandoc new enough to support it (2.x+).

## What the author must fill in before submission

1. **Affiliation.** `paper.md` carries an HTML comment placeholder immediately below the YAML
   header. Replace it with the affiliation line inside the header.
2. **ORCID.** Not present anywhere in the file; add it alongside the affiliation.
3. **Corresponding-author contact email.** Same place. No email address is included in the
   draft.
4. **`icmje2025` in `refs.bib` is `% UNVERIFIED`.** The ICMJE recommendations URL was recorded
   from the vault's existing disclosure practice and was *not* fetched during preparation.
   Confirm `https://www.icmje.org/recommendations/` resolves, identify the current dated
   revision, and add an access date. If COPE guidance is also to be cited by key rather than
   in prose, add that entry too.
5. **`paper1` in `refs.bib` is `% UNVERIFIED`.** The companion Charnov–Gittins manuscript has
   no DOI and is not posted to a preprint server as of 2026-09-05. Replace the `@unpublished`
   entry with the posted record once it exists.
6. **Decide the title.** The alternative considered was *"Kill rates and failure modes in
   agent-driven cross-domain research: a one-project, one-day record"*. The current title was
   chosen because the survival rate, not the taxonomy, is the paper's lead result.

## Reference verification

Five entries were resolved at `api.crossref.org/works/{doi}?mailto=deciduusleaf@gmail.com` on
2026-09-05 and checked field-by-field against the returned record: `swanson1986`,
`verheijen2009`, `turbill2011`, `quarrier2023`, `evans2020`. Each carries a `note` recording
that check. Two entries are marked `% UNVERIFIED` (`icmje2025`, `paper1`) with the reason
stated inline. `vault` is a self-citation of the object under audit and is not independently
verified. No DOI, page range or ISBN was constructed or inferred; do not add DOIs without a
provider fetch.

One note on `quarrier2023`: Crossref's `issued` date is 2022-12-02 (online first) while the
print issue is dated 2023. The entry uses the print year and records the discrepancy in its
`note`, per the vault's rule that two objects may carry two different true values.

## Traceability

Every count in `paper.md` carries an HTML comment naming the vault note (and section) it comes
from. If a vault note is revised, grep `paper.md` for that note ID before re-submitting. The
figures most likely to drift are the log-entry counts (245 entries, 93 corrections), which are
derived by counting `## [date] kind |` headers in `vault/log.md` and will change with any new
entry:

```
grep -c "^## \[" vault/log.md
grep "^## \[" vault/log.md | sed 's/^## \[[0-9-]*\] //;s/ *|.*//' | grep -c correction
```

The move-type table in Section 3 is derived from `vault/_scripts/c51_data/claims.csv`
restricted to the 82 rows whose `outcome` is not `ungraded`; its marginal survival rates match
C51 §3 exactly.

## Key hygiene

All eight `refs.bib` entries are cited in `paper.md`. No dangling keys, no orphans, checked
2026-09-05.
