---
name: citation-intersection
type: method
---

# Citation intersection

The strongest evidence standard this project has, and the only one that has not been
embarrassed.

**Method:** pull every paper citing the anchor on one side, fetch their reference lists, and
intersect against the other side's canon. Report the count *and* inspect the intersection.

## Why it beats string matching

[[G17-overconfident-uncertainties]] is the specimen. Same claim, same day:

| Instrument | Result |
|---|---|
| String query | **2** |
| Citation graph | **279** |

Opposite answers. Only one was measuring the relationship.

## But it is not sufficient either

The same entry shows the reverse failure. **279 citations is not 279 follow-ups.** Roughly
six engaged the actual claim. Counting citations and calling it refutation is the mirror of
counting string hits and calling it a gap.

**Both instruments require reading.** See [[relationship-description]], field 1.

## Where it has been applied

- [[G25-proofreading-coding]] — 1,463 citers pulled, 416 with available reference lists, 16
  co-cite Shannon, **zero with any coding-theory content**
- [[G19-safety-factor-derived-twice]] — all 46 citing works individually inspected

Those two are the project's strongest findings, and that is not a coincidence.

## Outstanding

Eight surviving gaps have **never** faced this test. Listed in [[00-index]].

---

## Expected co-citers under independence

A raw intersection count is uncalibrated. Two large citer sets will overlap by chance alone, and
how much depends on how big the surrounding literature is. **Report every intersection as
observed-over-expected, never as a bare count.**

```
E  =  |citers_A| · |citers_B| / N_universe
O/E  =  observed / E
```

`O/E ≈ 1` is what independence predicts. `O/E ≫ 1` is a joined literature. `O/E ≪ 1` is a gap —
*provided `N_universe` is defensible*, which is the whole difficulty.

### Defining `N_universe`, per provider

`N` is the number of works that *could* have cited both. State which one you used:

| Route | How to get it | Comment |
|---|---|---|
| **OpenAlex concept/year window** | `api.openalex.org/works?filter=concepts.id:<Cxxxx>,from_publication_date:<first citer year>` → `meta.count` | The defensible choice when both sides sit inside one nameable concept. Use the *union* of the two concepts, not the intersection |
| **OpenAlex year window, unrestricted** | same, dropping the concept filter | The whole-of-science denominator. Almost always too large — see the sensitivity below |
| **Union of the two citer sets** | `|A| + |B| − O` | A *floor* on `N`, computable from numbers already recorded. Because it is the smallest defensible `N`, it gives the **largest** `E` and therefore the **smallest** `O/E`. It flatters a gap claim, and must be labelled as a floor, never quoted alone |

**Sensitivity is mandatory.** `E ∝ 1/N`, so a gap that looks decisive at one denominator can
vanish at another. Worked below: [[G6-multifunctionality]]'s zero sits against `E ≤ 143` at the
union floor but `E ≈ 0.15` against a 10⁶-work universe, where a zero means nothing at all.
**Quote `O/E` at the floor and at one field-scale `N`, or do not quote it.**

### The robust statistic is the control ratio, not `O/E`

`N` cancels when the same universe is used for a gap and its [[positive-controls|positive
control]]:

```
(O/E)_gap / (O/E)_control  =  (O_gap/|B_gap|) / (O_control/|B_control|)
```

This is denominator-invariant, and it is the number a gap claim should rest on. It also corrects
the raw percentage comparisons this project has been quoting, which divide both sides by the
*same* base and so ignore that the two partner sets differ in size.

### Worked: G28 — Charnov × Gittins

Inputs, all from [[G28-marginal-value-gittins]]'s Provenance table: `|citers(Gittins 1979)| =
1,013` (run-time enumeration, 2026-09-03); `|citers(Charnov 1976)| = 5,424`; observed
intersection **5**. Control partner Auer, Cesa-Bianchi & Fischer 2002
(`10.1023/A:1013689704352`), `is-referenced-by-count = 3,906` (Crossref, 2026-09-05); observed
Gittins × Auer **225**.

| | `|A|` | `|B|` | O | `N` floor | E | **O/E** |
|---|---|---|---|---|---|---|
| **Gap:** Gittins × Charnov | 1,013 | 5,424 | **5** | 6,432 | 854 | **0.0059** |
| **Control:** Gittins × Auer | 1,013 | 3,906 | **225** | 4,694 | 843 | **0.267** |

**Control ratio = 62.5**, denominator-invariant: `(225/3,906)/(5/5,424) = 0.0576/0.000922`.

**`N_universe` fetched 2026-09-05** *(added from `audits/staged`)* — OpenAlex, union of the
foraging/behavioural-ecology and bandit/optimal-stopping concepts from Charnov's year:

```
works?filter=concepts.id:C165287380|C9343608|C123197309|C99414536,
  from_publication_date:1976-01-01,to_publication_date:2026-09-05   →  meta.count = 100,685
```

| `N` | E (gap) | O/E (gap) | E (control) | O/E (control) |
|---|---|---|---|---|
| 6,432 / 4,694 (union floors) | 854 | 0.0059 | 843 | 0.267 |
| **100,685 (fetched)** | **54.6** | **0.092** | 39.3 | **5.73** |
| 1,006,850 (10×, sensitivity) | 5.46 | 0.916 | 3.93 | 57.3 |

`E = 54.6 > 1` at the fetched `N`, so **the low count is a finding there**; at 10× it is not
(`O/E = 0.92`). The control ratio 62.5 is unchanged on every row.

Two things follow. **(a)** The note's headline "factor of 45" is the same comparison done against
a shared 1,013 base without correcting for the two partner sets' different sizes; correcting it
moves 45 → **62.5**, i.e. the isolation is slightly *stronger* than claimed, and now stated in a
form that does not depend on which Gittins citer count is used. **(b)** The raw `O/E` is not
safe on its own: at `N = 10⁵` the expected count falls to 55 and `O/E` rises to 0.09; at
`N = 10⁶` it falls to 5.5 and `O/E ≈ 0.91` — indistinguishable from chance. **G28's finding
lives in the control ratio, not in the intersection count.**

### Worked: G25 — Hopfield × Shannon

From [[G25-proofreading-coding]]: 1,463 citers of Hopfield 1974 pulled, **416** reference lists
retrieved (28.4% coverage), of which **16** also cite Shannon 1948 and **0** carry any
coding-theory content.

`|citers(Shannon 1948)|` is **not recorded in the note** and was not fetched, so `E` is not
computable as stated. What *is* computable is the reduction: with `f_Shannon ≡
|citers(Shannon)|/N` the base rate at which any work cites Shannon,

```
E  =  416 · f_Shannon           O/E  =  (16/416) / f_Shannon  =  0.0385 / f_Shannon
```

so the whole null model turns on one unfetched number: **is Shannon 1948 cited by more or less
than 3.85% of this universe?** If more, the proofreading literature under-cites Shannon; if
less, it over-cites him. *That is the query to run:* `cited_by_count` for
`10.1002/j.1538-7305.1948.tb01338.x` over the same concept/year window used for `N`.

**`N_universe` fetched 2026-09-05, and it fails** *(added from `audits/staged`)*. OpenAlex
`works?filter=concepts.id:C170748874|C113709454,from_publication_date:1974-01-01,to_publication_date:2026-09-05`
returns `meta.count = 8,851` — but `|citers(Shannon 1948 pt I, W1995875735)| = 82,198`
(OpenAlex `cited_by_count`, 2026-09-05), so the concept-scoped `N` is *smaller than one of its
own subsets* and is void. **Shannon's citer set does not fit inside any nameable concept scope.**
The union floor binds instead, against the note's current full-coverage numbers
(`|citers(Hopfield)| = 1,656`, `O = 36`):

| `N` | E | O | O/E |
|---|---|---|---|
| 8,851 (concept-scoped) | 15,379 | 36 | **void** — `N < |B|` |
| **83,818 (union floor)** | **1,624** | 36 | **0.022** |
| 838,180 (10×, sensitivity) | 162 | 36 | 0.222 |

`E ≫ 1` on every valid row, so **the low count is a finding**, and unusually for this project it
is insensitive to `N` across an order of magnitude. This also answers the "one query" above:
`f_Shannon = 82,198/83,818 = 0.98` at the floor, far above 3.85% — this literature **under**-cites
Shannon relative to the universe that contains both sets.

**The load-bearing claim is denominator-free.** The gap is not the 16 — it is the **0** works
with coding-theory content in the inspected 416. `O = 0` gives `O/E = 0` for any positive `E`,
so no choice of `N` rescues it. The 28.4% coverage, not the null model, is what limits this
finding.

### Worked: G6 — multifunctionality, engineering × ecology

From [[G6-multifunctionality]]: 172 engineering citers, 861 ecology citers, **0** intersection
across six anchor pairings, 1,033 works total.

| `N` | E = 172·861/N | O | O/E |
|---|---|---|---|
| 1,033 (union floor) | **143.4** | 0 | **0** |
| 10⁴ | 14.8 | 0 | 0 |
| 10⁵ | 1.48 | 0 | 0 |
| 10⁶ | 0.148 | 0 | — *uninformative* |
| **13,830 — fetched 2026-09-05** | **10.7** | 0 | **0** *(a finding: `E > 1`)* |
| 138,300 (10×, sensitivity) | 1.07 | 0 | 0, marginal |

**This is the clearest demonstration of why the null model was needed.** At the union floor the
zero is spectacular: 143 expected, none observed. Against a whole-of-science denominator, fewer
than one co-citer is expected anyway and the zero carries no information. **A zero intersection
is a finding only if the two literatures share a universe small enough that `E > 1`.** G6's
claim therefore required a stated concept-scoped `N` below ~1.5×10⁵ works.

**That number has now been fetched** *(added 2026-09-05 from `audits/staged`)*. OpenAlex
`works?filter=concepts.id:C200329591|C2988890453,from_publication_date:2011-01-01,to_publication_date:2026-09-05`
returns `meta.count = 13,830` — an order of magnitude *under* the ~1.5×10⁵ threshold, giving
`E = 10.7` and leaving the zero standing. Caveat on scope: OpenAlex has no "multifunctional
materials", "structural battery", "ecosystem multifunctionality" or "Hill numbers" concept, so
C200329591 (Advanced composite materials) and C2988890453 (Functional diversity) are proxies for
the two sides, not exact scopes.

The positive control `Byrnes 2014 × Jost 2006 = 17` cannot be put in these units:
`|citers(Jost 2006)|` is **not recorded** in the note.
