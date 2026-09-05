---
name: PENDING-log-FIX1
type: method
---

# PENDING log entries — FIX1, the OpenCitations blank-key phantom

Staged `vault/log.md` entries and a re-check list from the FIX1 instrument repair, 2026-09-05.
**Not yet merged into `log.md`**, and deliberately not wikilinked from anywhere, so that the
orchestrator merges these by hand in the project's newest-first order. Nothing here is a standing.

## [2026-09-05] method | intersect.py now drops blank `citing`/`cited` keys, prints the drop count, and self-tests

`vault/_scripts/intersect.py` built its citer sets from `row["citing"]` with only a truthiness
guard and reported nothing about what it discarded. OpenCitations `/citations/<doi>` returns
records with an **empty `citing` field**; a set built without filtering carries a phantom `""`
which, being present in *every* set built the same way, inflates `N_A`, `N_B` **and every
intersection by exactly 1**. An intersection of 1 is precisely the size at which a gap claim
becomes a bridge claim, so the artefact is maximally load-bearing where it is hardest to see.
What is now different: `_key()` normalises and strips both `citing` and `cited`; blank and
whitespace-only keys are dropped before the set is built; the per-anchor drop count is printed to
stderr and the run total to stdout; and `--selftest` fetches Scheffer 2009 × Si 2011 and asserts
no blank key survives in either set or in the intersection. Produced by: live fetch, 2026-09-05
(`selftest OK: |A| = 3,934, 65 blanks dropped; |B| = 1,783, 12 dropped; |A ∩ B| = 1`; unfiltered
the same pair reports 2). First diagnosed in `audits/scout-04-conservation-genetics.md`, where an
uncorrected pass reported five phantom "1-hit" candidates that are clean zeros. Documented in
`vault/method/citation-sources.md` under the endpoint traps.

## [2026-09-05] verification | every intersection in G29, G30, G31, G33 re-derived on the fixed instrument; no standing moves

Nineteen anchor payloads re-fetched and twenty pairings re-intersected, OpenCitations
`api.opencitations.net/index/v1/citations/<doi>`, 2026-09-05. **No intersection count in any of
the four notes changed, and no `standing`, `contact-surface`, `evidence` or tag moved.** Three
citer-set *sizes* in G31 were one high and are corrected: Catling 2018 188 → **187**,
Schwieterman 2018 496 → **495**, Kass & Raftery 1995 11,867 → **11,866**. What was wrong there is
not the intersections but the *base*: G31 published three pre-filter `|A|`/`|B|` figures beside
post-filter intersections, and asserted that one blank value "appears in every set", when in fact
all seven of its anchors carry blanks and they carry many (14, 49, 713, 52, 47, 237, 358), not
one. G29 was already clean, having stripped blanks by hand at first write; G33's two payloads
contain no blank records at all. Produced by: `_scripts/intersect.py`, blanks dropped, 2026-09-05.

## [2026-09-05] verification | the phantom is real, and would have manufactured ten bridges

Counted directly by rebuilding each set both ways. Unfiltered, these rows would read one higher
than the truth: G29 Scheffer × Si 2 (true **1**), × Randall 1 (true **0**), × Jardine 2 (true
**1**), control × Wissel 269 (true **268**); all eight G31 gap pairings and the pooled row 1 (true
**0**), controls 5 and 3 (true **4** and **2**); G30 Weibull × Bakker 1 (true **0**). Ten of the
twenty pairings re-run. G33 (Barlow & Hunter, Guide 2000), G30's Weibull × Oguchi, × Murakami I
and Müller × Oguchi are unaffected because the *partner* payload carries no blank, which is the
trap's one mercy and also why a clean run on one anchor is no evidence about another.

## [2026-09-05] correction | G29's frontmatter and index said "zero in all three decade bins"; its own body table says 1

`G29:note` now reads "Zero in the 2009-2013 and 2014-2018 decade bins and 1 in 2019-2026". The
body's `§(a) Year bins` table has said `O = 1` in the 2019–2026 bin since it was written; the
summary contradicted the table it summarises. Raised as recurrence of the Griebling-2026 class in
`audits/07-provenance-rounds3-6.md`. **`vault/00-index.md:143` still carries the old wording** and
is owned by another agent this round — it must be brought into line with the corrected `note:`.

## [2026-09-05] correction | G30's control anchor Müller 2006 now carries a DOI, and the control ratio is restated denominator-invariantly

The load-bearing statistic of G30 was a control ratio whose control anchor was unidentified in the
note. Resolved by Crossref bibliographic lookup, 2026-09-05: Müller, *Stock dynamics for
forecasting material flows — case study for housing in the Netherlands*, *Ecological Economics*
59:142–156 (2006), DOI `10.1016/j.ecolecon.2005.09.025`, `is-referenced-by-count` = 460. The
OpenAlex W-id is still not fetched. The ratio was written `(0/103)/(15/103)`, dividing both sides
by the same base — the form `citation-intersection` forbids. Because Oguchi 2015 is held fixed and
the *mathematics-side* anchor is what varies, the invariant divides by the varying side:
`(O_ctrl/|A_ctrl|)/(O_gap/|A_gap|)` = `(15/511)/(0/11,512)` on OpenAlex and `(15/439)/(0/9,239)`
on OpenCitations — unbounded either way, so nothing moves except the basis. Newly stated: the
22× size asymmetry between the two A-side anchors runs *against* the gap, which strengthens it.

## [2026-09-05] verification | G30's OpenAlex zeros reproduce on OpenCitations with the fixed script

G30's published counts are OpenAlex server-side `meta.count` intersections, so the OpenCitations
phantom cannot have touched them — OpenAlex never hands this project a set of DOI strings to
de-duplicate. Cross-checked anyway: Weibull × Oguchi **0**, × Murakami I **1**
(`10.1016/j.resconrec.2023.107216`), × Bakker **0**, control Müller × Oguchi **15** — all four
agree with the OpenAlex figures on an independently assembled provider. Citer-set sizes differ by
provider (Oguchi 96 vs 103, Müller 439 vs 511, Weibull 9,239 vs 11,512) and are not pooled, per
the two-true-numbers rule.

---

## To re-check — notes quoting intersection results that may carry the phantom

**Read-only survey; none of these files was edited.** Every note below quotes a count from an
OpenCitations citer-set intersection run before the instrument was repaired. Anything reported as
`∩ = 1` is the highest-priority class, because a phantom bridge and a real one are the same
number; a set size may also be one high per blank-bearing anchor. Each needs one re-run of
`_scripts/intersect.py` on its own stated anchors before its figure is quoted again.

| File | Line | Figure at risk | Priority |
|---|---|---|---|
| `vault/gaps/G27-collective-decision.md` | 20 | `note:` — "returns 0, 0, 1, 1 (OpenCitations, 2026-09-05)"; **two ∩ = 1 rows**, and the whole reversion from `overturned` to `narrowed` and `contact-surface: 26 → 1` rests on them | **HIGH** |
| `vault/gaps/G27-collective-decision.md` | 87–88 | Dorigo 1996 × (Byzantine + FLP) = **1**; Seeley 1999 × (Byzantine + FLP) = **1**, quoted at obs/exp 2.7 and 89 | **HIGH** |
| `vault/gaps/G27-collective-decision.md` | 79–83 | citer-set sizes 8,814 / 267 / 1,914 / 6,735 | MED |
| `vault/gaps/G27-collective-decision.md` | 106, 116, 119 | "one real bridge", "moved the count from 0 to 1", `contact-surface` 1 — all downstream of the two 1s | **HIGH** |
| `vault/gaps/G7-how-passive.md` | 141 | OpenCitations `citations/10.3327/jaesj.34.1116` → **1** — a bare 1 on a single small anchor | **HIGH** |
| `vault/gaps/G32-recovery-time-hazard-shape.md` | 96, 100, 108–115 | Note is owned by another agent this round. Its `O raw (blank key)` column already records the artefact, but `audits/07-provenance-rounds3-6.md` reports the four ecology-internal controls are still pre-filter (31/10/7/7 → **30/10/6/7**) and that `00-index.md:146` renders the inflated range "7-31" | **HIGH** |
| `vault/gaps/G25-proofreading-coding.md` | 146 | Hopfield 1974 × Shannon 1948 pt II, OpenCitations ∩ = **8**; sets 1,542 and 9,771 | MED |
| `vault/gaps/G25-proofreading-coding.md` | 186 | the "8 OpenCitations" row of the before/after comparison table | MED |
| `vault/gaps/G25-proofreading-coding.md` | 20 | `note:` — "OpenCitations 8 against part II" | MED |
| `vault/gaps/G8-energy-per-bit-axis.md` | 68–72 | Landauer 1961 × (Laughlin 1998 + Attwell 2001): sets 4,292 and 3,881, ∩ = **35**. A phantom moves 35 → 34, which does not touch the overturn, but the two set sizes and the "0.82% / 0.90%" percentages are affected | LOW/MED |
| `vault/gaps/G8-energy-per-bit-axis.md` | 20, 25 | `note:` and the STANDING line — "35 co-citers", `contact-surface: 35` | LOW/MED |
| `vault/gaps/G6-multifunctionality.md` | 40–60 | OpenCitations set-overlap, 172 engineering / 861 ecology citers, ∩ **0** across six pairings. Zeros cannot be inflated *into* existence, but a published zero here means the run was already filtered or the payloads were clean — worth confirming which, since the union floor `N = 1,033` and `E = 143.4` depend on the two set sizes | LOW |
| `vault/computed/C13-unread-theorem-audit.md` | 79, 103, 135 | three "Intersection (OpenCitations set overlap): 0" verdicts, plus citer counts 5,075 / 84 / 39 / 54. Same reasoning as G6: the zeros are safe, the sizes and coverage percentages are not | LOW |
| `vault/gaps/G28-marginal-value-gittins.md` | 112, 318–324 | ∩ = **5 of 1,013**; the run is a *reference-list* intersection (`cited` field) rather than a citer-set one, and the repaired script now filters blank `cited` keys too, so the same trap applies on the other endpoint | MED |
| `vault/gaps/G19-safety-factor-derived-twice.md` | 42–43 | OpenCitations citers of `10.1006/jtbi.1996.0270` counted at **40**, and `/citation-count/` agreeing at 40 — a counted list, so a blank record would make it 39 | LOW/MED |
