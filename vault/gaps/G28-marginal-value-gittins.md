---
id: G28
name: G28-marginal-value-gittins
type: gap
standing: narrowed
evidence: citation-intersection
contact-surface: 8
crosses: nothing
crosses-rank: 0
topology: mediated
mediator: neuroeconomics
borrows-from: []
lends-to: ["[[G9-discrepancy-base-rate]]"]
mutual-with: []
computed-in: ["[[C5-charnov-gittins]]"]
uses-move: []
rests-on: []
tags: [node/gap, crosses/nothing, evidence/citation-intersection, standing/narrowed]
last-checked: 2026-09-03
note: "Holds but narrows. Intersection 5 of 1,013 Gittins citers (0.49%) vs control 225/1,013 = 22.2% - a factor of 45. Denominators reconciled in the Provenance table. Griebling 2026 LOCATED, doi 10.1016/j.anbehav.2026.123491, and confirmed to cite Charnov 1976 and Gittins 1979."
---

# Marginal value theorem and the Gittins index

**STANDING: NARROWED** · evidence: citation-intersection · contact surface: 8 · last checked 2026-09-03

> Charnov's rule: leave a depleting patch when the marginal intake rate drops to the average
> for the habitat.
>
> The Gittins index generalises the same optimality condition to the stochastic case.
> **Charnov's rule is not merely its limit — it is the same object.** No paper states that.
>
> *Wording corrected: this read "its deterministic, zero-switching-cost limit." See
> [[C5-charnov-gittins]] — τ is a zero-reward prefix inside the outside arm, and the licensing
> condition is non-revisitability.*

## Why this entry forced a new field in [[relationship-description]]

The count alone is uninteresting: 8 co-citers, against a Gittins-citer base whose size depends
on the provider (see the Provenance table below: 986-1,544) and a Charnov base of 5,424. Under verdict scoring
that reads "small number, gap holds," and the thinking stops.

**Inspecting the eight is where the finding actually is.** All eight are cognitive and
decision neuroscience — *Optimally frugal foraging*, *Raccoons optimally forage for
information*, *Cortical Circuits for Adaptive Foraging Decisions*, *How the threat of losses
makes people explore more than the promise of gains*.

So the topology is: **operations research and behavioural ecology are joined almost entirely by
a third field that reads both and tells neither.** That is a specific structure, and no number
expresses it.

*(This paragraph originally read "no direct contact at all." Corrected above — Griebling et al.
2026 is direct contact, newly emergent.)*

## The control that makes it sharp

| Pair | Co-citers |
|---|---|
| Charnov and Gittins | **8** (0.5% of the Gittins base) |
| **Gittins and Sutton & Barto** | **181 (11.7%)** |

Operations research and reinforcement learning are **one closed literature**. It is
specifically biology that sits outside it. Without this control the 8 means nothing; with it,
the isolation is located.

See [[positive-controls]].

## Independent rediscovery, in-house

Behavioural ecology derived its own stopping rule — Green 1984, *Stopping Rules for Optimal
Foragers*, 248 citations — in its own vocabulary, **without the stopping-theory literature.**
A field re-derived optimal stopping rather than read it.

## What crosses

**Nothing.** Not the formalism, not the vocabulary. The one genuine contact runs the other
way: Srivastava, Reverdy & Leonard, *On optimal foraging and multi-armed bandits* (2013), a
control-theory paper importing foraging framing into bandit regret analysis — **one-way,
from the operations-research side.**

Same asymmetry as information foraging, which took optimal foraging theory into
human-computer interaction and is not read back. See [[one-way-borrowing]].

## What is specifically absent

**The stated equivalence.** That Charnov's threshold *is* the Gittins index in the
deterministic, zero-switching-cost limit. Writing that down is a paragraph of algebra and
would let each field use the other's results.

## What would change it

Write the equivalence. Then the biology inherits the stochastic machinery — index policies,
regret bounds, switching costs — and operations research inherits several decades of field
data on animals actually solving the problem.

## Verification

Survived the full alternate-name gauntlet under the hardened protocol: patch leaving,
optimal foraging, patch residence time, against optimal stopping, secretary problem, index
policy, scheduling. All zero or irrelevant.

## The citation intersection: 5 of 1,013, and one sentence must go

Anchors are the primary works themselves — Charnov `10.1016/0040-5809(76)90040-x` and Gittins
`10.1111/j.2517-6161.1979.tb01068.x`, no proxy substitution needed. **OpenCitations and
Crossref returned the identical five DOIs.**

| Check | Result |
|---|---|
| Intersection | **5 of 1,013 Gittins citers — 0.49%** |
| Coverage | 1,006/1,010 citers (99.4%) had DOI-bearing reference lists |
| **Positive control: Gittins × Auer 2002** | **225 — 22.2%.** A factor of **45** |
| Control: Charnov × Auer 2002 | 3 (0.08%) — so the isolation is not an artifact of Gittins 1979's age |

**Which denominator, and the arithmetic.** Both headline percentages are computed against the
**same base of 1,013** — the citer set actually enumerated at run time (2026-09-03), *not*
against any of the live counts in the Provenance table:

- intersection: `5 / 1,013 = 0.004936` → **0.49%**
- positive control: `225 / 1,013 = 0.2221` → **22.2%**
- ratio: `0.2221 / 0.004936 = 45.0` → the stated **factor of 45**

The `1,006/1,010` coverage line uses a slightly different figure (1,010) because four DOIs
failed to resolve on the reference-list pass; it is a coverage statistic, not the denominator of
either percentage. **Neither percentage is recomputed against Crossref's 986 or OpenAlex's
1,544** — doing so would move 0.49% to 0.51% or 0.32% respectively, and 22.2% to 22.8% or 14.6%.
The factor-of-45 is denominator-invariant, since both numerator sets share the base.

**The positive-control query.** Auer, Cesa-Bianchi & Fischer 2002, *Finite-time Analysis of the
Multiarmed Bandit Problem*, *Machine Learning* 47:235-256, **`10.1023/A:1013689704352`**
— DOI verified against Crossref 2026-09-05 (title, authors and journal all match;
`is-referenced-by-count` = 3,906). The control is the **set intersection of the citer list of
Gittins 1979 with the citer list of Auer 2002** — i.e. works citing both — computed on the same
1,013-work Gittins base, giving 225.

**All five inspected. Zero are real bridges.** Bhat/Bénichou/Redner 2018 (*Phys. Rev. E*, read
in full) cites both in separate background lists and never uses the phrase "marginal value
theorem."

Lejarraga & Hertwig 2016, read in full, is the sharp near-miss — **the gap restated by someone
who could not see it.** It says no general optimal solution to the explore/exploit tradeoff has
been proposed, *"(but see Gittins, 1979)"*, and separately uses Charnov's rule. Both objects, in
one paper, unconnected. Again.

### The sentence that is now false

The note said **"operations research and behavioural ecology have no direct contact at all."**
**That is no longer true.** Griebling et al., *Animal Behaviour* (2026) cites Charnov 1976,
Gittins 1979 **and** the Gittins 2011 book — direct ecology → operations-research contact.

**LOCATED and verified, 2026-09-05.** Griebling, Johnson & Benson-Amram, *Raccoons optimally
forage for information: exploration-exploitation trade-offs in innovation*, *Animal Behaviour*,
April 2026, **`10.1016/j.anbehav.2026.123491`** (Crossref works search on
`query.bibliographic=Griebling+Animal+Behaviour+2026`, then the full record at
`api.crossref.org/works/10.1016/j.anbehav.2026.123491?mailto=...`). Its deposited reference list
(100 references) **contains Charnov 1976 `10.1016/0040-5809(76)90040-X`, Gittins 1979
`10.1111/j.2517-6161.1979.tb01068.x`, and Gittins 2011** — so the co-citation is confirmed from
the primary record, not inferred. **Full text still not obtained**, so whether it *states the
equivalence* remains an outstanding check, alongside Houston & McNamara 1999.

Note this is the same paper already listed among the eight co-citers above
(*Raccoons optimally forage for information*) — so the "direct contact" and the
"joined only by a third field" readings are in tension, and the honest statement is that this
one work is behavioural ecology proper, not neuroscience.

**Restated:** contact is *newly emergent and vanishingly thin* — 0.49% against a 22.2% control —
and no work read in full states the equivalence.

### Correction to an old control

The **181 / 11.7%** Gittins × Sutton & Barto figure in the control table above came from OpenAlex. The
same query here returns **24**, because the book has no proper DOI. **Do not carry 24 forward**,
and treat the 181 as method-dependent.

## The equivalence has now been written: [[C5-charnov-gittins]]

**It is an identity, not an analogy**, and it is two lines.

- **Current patch.** Its Gittins index is the maximum forward chord slope of `g` from `t`.
  Under Charnov's concavity assumption the supremum is attained as `s → 0⁺`, so `ν(t) = g'(t)`.
- **Outside option.** Bundle travel plus a fresh patch into one *habitat arm*, rewarding `0` on
  `[0, τ)` then `g'(u − τ)`. Its index is `sup_t g(t)/(τ + t) = R*`.

So **Charnov's maximisation over residence time literally is the supremum over stopping times
in the Gittins definition**, and `R*` is the index of the arm you would switch to. "Leave when
the current index drops to the alternative's" gives `g'(t) = R*` exactly.

### Both versions of the switching-cost quarrel were half right

τ is **neither** a switching cost **nor** zero. It is a **zero-reward prefix absorbed inside the
outside arm.** The bandit genuinely is a zero-switching-cost bandit — the original wording was
right about that — and τ still survives into the answer — the correction was right about that.
The condition neither identified is the real licence: **patches must be non-revisitable.**

A repair to the proposed route as well: Whittle's retirement reward `M` is a *stock*, and
`M* = R*/δ → ∞` undiscounted. The bridge object is **`δM`, not `M`**. And the limit can be
skipped entirely — the problem is regenerative, so renewal-reward gives the average-reward index
directly.

### Where it breaks — in exactly the three places bandit theory already knows

Each maps onto a real foraging complication: **patch renewal** (restless bandit, arms not
frozen), **revisitable patches** (no index policy is optimal under switching costs),
**non-stationary habitat**. Discounting does *not* break it; it generalises.

### Two results fell out that were not asked for

Non-concave gain curves make naive MVT wrong while **the index self-corrects to the concave
hull.** And for *informative* patches the index exceeds the immediate rate by a signed
exploration bonus, **predicting over-staying** — which is the documented empirical anomaly
(Nonacs 2001, 26 studies). That turns the equivalence into a discriminating experiment.

### The near-miss that proves the gap

A 2024 bioRxiv generalised-MVT paper derives `g'(t*) = λ·EV`. **That is Whittle's `ν = δM`.**
The paper contains zero occurrences of Gittins, Whittle or bandit. Someone re-derived the
identity in foraging notation without knowing it existed — which simultaneously **validates the
algebra** and **demonstrates the gap.**

Geana, Wilson, Daw & Cohen (2016) is arguably better-placed than Averbeck: it contrasts MVT and
"bandit" paradigms explicitly and never names Gittins.

**Novelty is stated as "appears unwritten," carrying its weight honestly:** Houston & McNamara
(1999) and Gittins–Glazebrook–Weber were not obtained.

## The full-text re-read: holds, with one correction

**The best-placed paper in existence does not state the relation.** Averbeck 2015,
[*PLoS Comput Biol*](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4401555/fullTextXML),
read in full, formalises bandit, sampling **and** foraging tasks in one MDP framework — and
names both objects without ever relating them:

> "It is also possible to use Gittins indices to select optimal actions in stationary bandit
> tasks"

and separately:

> "some foraging tasks have been modeled using the marginal value theorem"

**Charnov is not cited at all.** One paper, both halves in hand, no connection drawn. That is
the gap in a single document.

Europe PMC confirms the isolation: `"Gittins" AND "Charnov"` → **3**, all psychology and
neuroscience. `"Gittins index" AND "marginal value theorem"` → **1**, a review adjacency.

**One-way borrowing confirmed and understated.** Srivastava, Reverdy & Leonard 2013, read in
full: it **never mentions Gittins.** McNamara & Houston 1985 and Green's 1990 field overview
contain zero Gittins, index or stopping hits.

### Correction to the claim's own wording

The note says Charnov's rule is the Gittins index in the **"zero-switching-cost limit."** That
is probably wrong on its own terms — **MVT has a switching cost**: the travel time τ. The clean
reduction more likely runs through **Whittle's retirement reward**, where τ maps to the
retirement option rather than to zero. *This is a reading, not a sourced claim, and is marked
as such.* It sharpens what would have to be written, and makes writing it slightly harder.

### Not obtained

Green 1987, Stephens & Krebs 1986, and Houston & McNamara 1999 are books that could not be
obtained. **The last is the most likely place for a stated relation to be hiding**, and this
entry stays provisional on it.

## Provenance: the Gittins-citer denominators

Four different Gittins-citer counts appeared in this note (1,542, 1,013, 1,010, and an implied
base for "0.5%"). They are one number measured by different instruments. Replaced by this table.

Anchors: Charnov 1976 `10.1016/0040-5809(76)90040-x`; Gittins 1979
`10.1111/j.2517-6161.1979.tb01068.x` (Crossref, 2026-09-05: *Bandit Processes and Dynamic
Allocation Indices*, J. R. Stat. Soc. B — correct work).

| Provider | Endpoint | N citers of Gittins 1979 | Date |
|---|---|---|---|
| **Run-time enumeration** (provider not recorded; OpenCitations COCI is the likely source, since it and Crossref "returned the identical five DOIs") | — | **1,013** | 2026-09-03 |
| Crossref | `api.crossref.org/works/10.1111/j.2517-6161.1979.tb01068.x?mailto=...` → `is-referenced-by-count` | **986** | 2026-09-05 |
| OpenCitations | `api.opencitations.net/index/v1/citation-count/10.1111/j.2517-6161.1979.tb01068.x` | **1,026** | 2026-09-05 |
| OpenAlex | `api.openalex.org/works?filter=doi:10.1111/j.2517-6161.1979.tb01068.x` → `cited_by_count` (W3125634603) | **1,544** | 2026-09-05 |

**1,542 was OpenAlex** (1,544 today — two works' growth, consistent). **1,013 is closest to
OpenCitations** (1,026 today). **986 is Crossref.** The 1,010/1,006 pair is the subset that
survived reference-list retrieval, not a separate measurement of the base.

The percentages in this note are all computed against **1,013**; see the arithmetic under
*The citation intersection* above.
