# Charnov–Gittins preprint: build notes

Draft preprint for EcoEvoRxiv / arXiv q-bio.PE, assembled from vault notes
`C5-charnov-gittins`, `C25-whittle-foraging`, `G28-marginal-value-gittins`,
`Q5-restless-patches` and `method/citation-intersection`. Nothing in this folder edits
the vault; the vault remains the source of truth for every number.

## Build

```
pandoc paper.md --citeproc --bibliography=refs.bib -o paper.pdf
```

Requires a LaTeX engine on PATH (TeX Live / MiKTeX) for PDF output. For a quick check
without LaTeX:

```
pandoc paper.md --citeproc --bibliography=refs.bib -o paper.html
```

Add `--csl=<style>.csl` if a journal style is required; without it Pandoc uses its
default (Chicago author–date).

## What the author must fill in before submission

1. **Affiliation.** `paper.md` carries an HTML comment placeholder immediately after the
   `author:` field in the YAML header. Replace it with the affiliation line.
2. **ORCID.** Not present anywhere in the file; add it alongside the affiliation.
3. **Corresponding-author contact email.** Same place. (No email address is included in
   the draft.)
4. **`genmvt2024` author list in `refs.bib`.** The vault records the 2024 bioRxiv
   generalised-MVT paper by title and DOI only. The entry is deliberately author-less
   rather than guessed; look up
   `10.1101/2024.10.28.620618` and complete it.

## Reference verification

Every DOI in `refs.bib` is one a vault note records as verified against a named provider
on a named date. Entries with no verified DOI carry a `% UNVERIFIED` comment saying what
is missing and why. No DOI was constructed or inferred. Do not add DOIs without a
provider fetch.

Entries currently lacking a verified DOI: `gittins2011` (string recorded, Wiley page
403), `kilpatrick2020` (arXiv id only), `nonacs2001`, `banks1994`, `averbeck2015`,
`geana2016`, `mcnamara1985`, `houston1999`, `stephens1986`, `green1984`,
`srivastava2013`, `scully2025`.

## Numerics

Table 1 and the two limits in Section 3 are reproduced by
`vault/_scripts/c25_whittle.py` (Python standard library only):

```
python vault/_scripts/c25_whittle.py
```

## Traceability

Each number in `paper.md` carries an HTML comment naming the vault note (and section)
it comes from. If a vault note is revised, grep `paper.md` for that note ID before
re-submitting.
