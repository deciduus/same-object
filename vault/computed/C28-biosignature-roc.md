---
name: C28-biosignature-roc
type: computed
exit: computation
extends-to: [astrobiology]
next-step-cost: S
---
# The O₂ biosignature as a diagnostic test

> **A detection of atmospheric O₂ is more likely true than false only above a break-even
> prevalence `p* = (1−spec)/(sens + 1−spec)` — which at *illustrative* specificities of
> 0.90–0.99 is a base rate of 1-in-11 to 1-in-101 planets bearing life. No specificity for the
> O₂ test is published, and the body below shows none is currently estimable from the
> literature: 0.90–0.99 is a span chosen to show the arithmetic, not a range the field's
> false-positive enumeration supports.** Turned around: if life is present on 1 in 1,000 of the
> planets we look at, the O₂ test must have specificity **≥ 0.999** for a detection to be worth
> believing. This narrows [[G31-biosignature-diagnostic-theory]] by building the object the gap
> says is missing. **It does not close it**: prevalence is unknown, no specificity has ever been
> published, and the arithmetic below is Bayes' rule — the contribution is the framing plus a
> number nobody in the field has stated.

## The quantity

```
"disease"  ≡  life present on the observed planet
"test +"   ≡  O2 detected above the instrument's stated threshold

sens  ≡  P(O2 detected | life)          = 1 − false-negative rate
spec  ≡  P(no O2 detected | no life)    = 1 − false-positive rate
prev  ≡  P(life)  over the observed sample                    ← the missing term

PPV   =  sens·prev / [ sens·prev + (1−spec)(1−prev) ]         = P(life | O2 detected)
LR+   =  sens / (1−spec)                                       = the Bayes factor
p*    =  (1−spec) / (sens + 1−spec)                            where PPV = 0.5
```

All four are dimensionless and bounded in [0,1] (LR+ in [0,∞)). `PPV` is bounded because it is a
probability, not because of any assumption about planets. Script: `vault/_scripts/c28_roc.py`.

## Inputs

### The test being characterised

O₂ alone, not the O₂+CH₄ disequilibrium pair. Reason: the disequilibrium pair has a *joint*
false-positive structure that would need a two-test combination rule (serial vs parallel
testing), which is a second calculation. O₂ alone is the case the field itself has written up
most completely, in Meadows, Reinhard, Arney et al. 2018, *Exoplanet Biosignatures:
Understanding Oxygen as a Biosignature in the Context of Its Environment*, `10.1089/ast.2017.1727`
— DOI resolved through Crossref (`mailto=deciduusleaf@gmail.com`) **2026-09-05**, Astrobiology
18:630–662, `is-referenced-by-count` = 301.

**Full text NOT read this session.** The abstract was fetched from Europe PMC
(`ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:"10.1089/ast.2017.1727"&resultType=core`,
2026-09-05) and establishes, in the authors' own words, that the paper (a) reviews *"the most
recent knowledge of false positives for O₂, planetary processes that may generate abundant
atmospheric O₂ without a biosphere"*, and (b) separately treats mechanisms *"producing a false
negative for biologically generated O₂."* Both legs of a 2×2 table, named as such. The
per-mechanism list below is therefore recorded at **review level, `UNVERIFIED`** for
completeness and for attribution of each row to a specific section.

### The abiotic-source enumeration — and what it does not carry

| # | Abiotic O₂ route | Discriminant the field proposes | Published probability or frequency |
|---|---|---|---|
| 1 | H₂O photolysis + hydrogen escape on a desiccating planet (runaway greenhouse, M-dwarf pre-main-sequence) | O₂–O₂ collision-induced absorption at high abundance; absence of H₂O | **NONE** |
| 2 | CO₂ photolysis with inefficient CO+O recombination (dry, low-N₂, M-dwarf) | CO detection alongside O₂ | **NONE** |
| 3 | O₂ accumulation from a deficit of non-condensable background gas | pressure / N₂ inference from Rayleigh slope | **NONE** |
| 4 | Massive residual abiotic O₂ atmosphere on a post-runaway desiccated world | O₄ CIA; stellar age and type | **NONE** |
| 5 | O₂ built up for lack of surface/interior sinks (frozen, low outgassing) | surface temperature, geological context | **NONE** |
| 6 | Not a planetary process at all: spectral degeneracy / stellar contamination in the retrieval | S/N, repeat observation, instrument systematics | **NONE** |
| — | *(the false-negative leg: O₂ suppressed by sinks for most of Earth's own history)* | — | **NONE** |

**Six routes, seven rows, zero numbers.** That empty right-hand column is the result of this
note, not an omission from it. The field enumerates false-positive *scenarios* and attaches to
each a *discriminant* — an additional observable that would rule it out. It does not attach to
any of them a rate, a frequency among lifeless planets, or a probability. Consequently
**specificity is not merely unpublished; it is not currently estimable from the published
literature**, because estimating it needs the fraction of lifeless planets on which at least one
of routes 1–6 fires, and no row supplies it.

The completeness of the enumeration is also unbounded: it is *of those considered*, in the sense
[[specification-instruments]] step 2 requires. A seventh route discovered tomorrow lowers
specificity and moves every number below in the same direction.

### Prevalence

**Free parameter.** No published numeric prior on the fraction of planets bearing detectable
life exists in either anchor's framework, and finding one would overturn
[[G31-biosignature-diagnostic-theory]]. The range 10⁻³ … 0.5 below is a span, not an estimate;
it is chosen to bracket "rare" and "common" without asserting either.

## Result

**PPV = P(life | O₂ detected), sensitivity = 1.0** — i.e. the assumption most favourable to the
detection, that life always shows up if it is there:

| prevalence | spec = 0.900 | spec = 0.950 | spec = 0.990 | spec = 0.999 |
|---|---|---|---|---|
| **0.001** | **0.010** | 0.020 | 0.091 | **0.500** |
| 0.003 | 0.029 | 0.057 | 0.231 | 0.751 |
| **0.01** | 0.092 | 0.168 | **0.503** | 0.910 |
| 0.03 | 0.236 | 0.382 | 0.756 | 0.969 |
| **0.1** | **0.526** | 0.690 | 0.917 | 0.991 |
| 0.3 | 0.811 | 0.896 | 0.977 | 0.998 |
| 0.5 | 0.909 | 0.952 | 0.990 | 0.999 |

**The same table at sensitivity = 0.5** — the field's own false-negative leg says O₂ was absent
for most of Earth's history, so a sensitivity near 1 is not defensible:

| prevalence | spec = 0.900 | spec = 0.950 | spec = 0.990 | spec = 0.999 |
|---|---|---|---|---|
| 0.001 | 0.005 | 0.010 | 0.048 | 0.334 |
| 0.01 | 0.048 | 0.092 | 0.336 | 0.835 |
| 0.1 | 0.357 | 0.526 | 0.847 | 0.982 |
| 0.5 | 0.833 | 0.909 | 0.980 | 0.998 |

Halving sensitivity halves LR+ and shifts the break-even prevalence up by a factor of ~2. It
does **not** rescue a low specificity: at spec = 0.90 no sensitivity whatever makes a detection
at prevalence 10⁻³ better than 1-in-100.

### The break-even, which is the number to quote

`p*`, the prevalence at which a detection is exactly as likely true as false:

| specificity | LR+ (sens=1) | **p\* (sens=1)** | p\* (sens=0.5) |
|---|---|---|---|
| 0.900 | 10 | **0.0909** — 1 in 11 planets | 0.167 |
| 0.950 | 20 | **0.0476** — 1 in 21 | 0.0909 |
| 0.990 | 100 | **0.00990** — 1 in 101 | 0.0196 |
| 0.999 | 1,000 | **0.00100** — 1 in 1,000 | 0.00200 |

And the inversion — the specificity a survey must demonstrate for its detections to be worth
believing at an assumed base rate (sens = 1):

| prevalence | spec for PPV = 0.5 | spec for PPV = 0.9 |
|---|---|---|
| 0.001 | **0.99900** | 0.99989 |
| 0.01 | 0.98990 | 0.99888 |
| 0.1 | 0.88889 | 0.98765 |
| 0.3 | 0.57143 | 0.95238 |

**Stated plainly, and this is the sentence the field has not written:** *given its own
enumeration of six abiotic O₂ routes, a single O₂ detection is more likely a true positive than
a false one only if either (a) fewer than one lifeless planet in a thousand triggers any of
routes 1–6, or (b) at least one planet in a hundred bears detectable life. Neither number has
been published, and the first is the one the field could actually estimate.*

## What the diagnostic frame adds that the CoLD scale lacks

The Confidence of Life Detection scale (Green, Hoehler, Neveu et al. 2021, *Call for a framework
for reporting evidence for life beyond Earth*, `10.1038/s41586-021-03804-9` — Crossref, Nature,
2026-09-05, cited-by 58) grades a claim on an ordinal ladder: signal detected, contamination
ruled out, biological origin plausible, alternatives excluded, independent confirmation, and so
on. Every rung is a statement about **the evidence in front of you**.

**The missing term is the base rate, and no rung of an ordinal ladder can carry it.** The
diagnostic frame adds exactly three things, in order of how much they matter:

1. **A prevalence slot.** PPV is not a property of the test. Ascending every CoLD rung raises
   LR+ and nothing else; the row of the table you land in is still chosen by `prev`. Two
   identical CoLD-6 claims — one from a survey of 20 nearby M-dwarfs, one from a blind survey of
   10,000 targets — carry different posterior probabilities, and CoLD by construction gives them
   the same grade. This is the base-rate fallacy in its textbook form, on a field-sized scale.
2. **A cardinal output.** CoLD level 6 is not 0.6, and it does not compose: two independent
   level-5 claims do not make a level-10. Likelihood ratios multiply; ordinal levels do not.
3. **An operating point.** Hanley & McNeil's ROC curve exists because the detection threshold is
   a *choice*, and moving it trades sensitivity against specificity along a curve. Astrobiology
   sets thresholds (σ levels, abundance floors) without ever drawing that curve or naming where
   on it a mission sits. AUC is prevalence-independent — which is why it is the right summary of
   the *instrument* and the wrong summary of a *claim*.

What CoLD has that the diagnostic frame lacks: a vocabulary for **contamination and
provenance**, which is not a conditional probability at all. The two are complements. The claim
here is not that CoLD is wrong; it is that CoLD plus a prevalence is a posterior, and CoLD alone
is not.

## §Honesty

- **Prevalence is unknown and this note does not estimate it.** Every number above is
  conditional on a free parameter. Anyone quoting a single PPV from this note without its
  prevalence is misusing it.
- **The framing is only as good as the enumeration.** Specificity is defined against "no life",
  and the six routes are *of those considered*. The list is not provably complete and never can
  be; a new abiotic route lowers spec and moves every row down.
- **The calculation is arithmetic.** Bayes' rule, four lines, no physics. Nothing here is
  difficult and nothing here is novel *as mathematics*. The contribution is the framing — that a
  biosignature claim is a diagnostic test, with the base-rate slot that implies — plus one
  number nobody has stated: **at prevalence 10⁻³, the required specificity is 0.999.**
- **Meadows 2018 and Catling 2018 were not read in full.** The mechanism list is at review level
  and marked `UNVERIFIED` above. What *is* fetched and quotable is the Meadows abstract's own
  statement that the paper reviews both false positives and false negatives for O₂ — which is
  enough to establish that the field owns both legs of the 2×2 table and neither of its rates.
- **The specificity values 0.9–0.999 are illustrative, not measured.** No published estimate
  exists. They are a grid, and the note's honest output is the *inversion* — the specificity a
  claim would need — not a PPV read off a guessed column.
- **`sens = 1.0` is used as the favourable bound, not as a belief.** The field's own
  false-negative discussion makes it clearly false for Earth's own history.

## Corrections 2026-09-05 (audit 06)

`audits/06-math-rounds3-6.md` item 13. No arithmetic changed; the callout was claiming an
evidential grade for its inputs that the body denies them.

**The pull-quote attributed a specificity range to the field.** It read: "at the specificities
the field's own false-positive enumeration can plausibly support (0.90–0.99)". The body says the
opposite in two places — §"The abiotic-source enumeration" concludes "**specificity is not
merely unpublished; it is not currently estimable from the published literature**", and §Honesty
says "The specificity values 0.9–0.999 are illustrative, not measured." An enumeration of
false-positive *mechanisms* is a list; a specificity is a rate over a reference population, and
the field has never defined that population. The enumeration therefore supports **no**
specificity, plausibly or otherwise.

| | old | new |
|---|---|---|
| status of 0.90–0.99 | "the specificities the field's own false-positive enumeration can plausibly support" | "*illustrative* specificities … No specificity for the O₂ test is published, and the body below shows none is currently estimable" |

Every number is unchanged: `p* = (1−spec)/(sens + 1−spec)` still gives 1-in-11 to 1-in-101 over
that span, and the note's real output — **the inversion**, that `prev = 10⁻³` demands
`spec ≥ 0.999` for a detection to be worth believing — is untouched and is not an assumption
about specificity but a *requirement* on it, which is why it was worth stating. The change is
that the callout now carries the same disclaimer the body always did.
`vault/_scripts/c28_roc.py` carries a matching comment on the `SPECS` grid so the illustrative
status travels with the numbers.
