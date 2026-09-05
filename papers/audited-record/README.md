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

## Revision 2026-09-05 (referee 1)

Revised against `reviews/2026-09-05-referee-1-opus.md` (major revision). What changed:

1. **Seven internal mismatches fixed.** (i) *Adversarial* split into two named objects: three
   **dedicated adversarial reviews** and the pre-registered predictor **adversarial leg** (48/82),
   whose coding rule is now quoted verbatim from the hashed brief; the "narrowing mechanism"
   finding is withdrawn. (ii) Corrections of corrections: **two**, of which one carries that
   `kind` and one is filed under `correction` — abstract, §3.3 and the tally now agree.
   (iii) "Two working days" everywhere; the 79 failure instances are from the second day.
   (iv) The twelve briefs are listed by ID (C39, C40, C43–C52; C41 and C42 have none).
   (v) Ownership recounted to 25 (model 16, orchestration 4, tooling 2, jointly owned 3; the
   human owns none alone and co-owns two); `vault/method/failure-taxonomy.md` corrected too.
   (vi) The `kind` distribution is given in full, with "29 other kinds appearing once each".
   (vii) The frame is stated: C23/C24 never created, eight retired G-IDs per `METHOD.md`,
   C51–C53 outside the hashed set, and the frame is every note that exists.
2. **Survival split into two variables**, `survived_novelty` (5/24 = 0.208) and
   `survived_standing` (21/58 = 0.362), with H1–H4 re-run per stratum. New §3.2 in the paper;
   `vault/computed/C51-vault-meta-analysis.md` carries the same split.
3. **Wilson 95% intervals on every rate**, and a stated no-multiplicity-adjustment rationale.
4. **The taxonomy is a catalogue with overlap, not a partition**; three overlapping events named.
5. **Catch table gains an exposure column**, and lint's zero is stated as a selection effect —
   the number is kept, the reading narrowed.
6. **New related-work section** with nine new verified references (reproducibility base rates,
   AI-for-science outcome reports, LBD evaluation, AI-authorship policy).
7. **Data availability** pins commit `f1faab3`, the Zenodo **version** DOI `10.5281/zenodo.22334048`
   alongside the concept DOI, and sha256 hashes for `claims.csv`, `failure-taxonomy.md`, `log.md`
   and all twelve briefs.
8. **Front matter and declarations**: affiliation placeholder "Independent researcher; Arizona
   State University (student)" (author to confirm), plus competing interests, funding,
   contributions and ethics statements.

**Recounted numbers that changed.** `vault/log.md` now holds **252** entries (was 245) and **97**
corrections (was 93); the earlier figures were counted before the last seven entries existed.

**Reference verification, revision 2.** Six DOIs resolved at
`api.crossref.org/works/{doi}?mailto=deciduusleaf@gmail.com` on 2026-09-05: `osc2015`,
`errington2021`, `ioannidis2005`, `nature2023`, `swanson1997`, `yetisgen2009`. Three arXiv
preprints are absent from Crossref and were verified at
`export.arxiv.org/api/query?id_list=…`: `lu2024` (2408.06292), `si2024` (2409.04109), `si2025`
(2506.20803). `icmje2025` is retired in favour of `icmje2026`: the page returned HTTP 200 on
2026-09-05, carries "Updated January 2026", and the relevant section is
**V. Use of Artificial Intelligence in Publishing**. `paper1` remains `% UNVERIFIED` (unposted).

**Still outstanding**, and declined rather than faked in this round: the blinded second coding
with κ, the re-grade of early claims under the later rubric, a second frame, a human comparator,
the three figures, and the glossary of claim IDs. Each is named in the author response.

**Staged, not yet applied.** `vault/PENDING-log-REV3.md` holds the eight `log.md` entries this
revision generates. It is deliberately unlinked from `00-index.md`; append its entries to
`vault/log.md` and delete the file.
