---
id: G36
name: G36-wear-erosion-damage
type: gap
standing: narrowed
evidence: citation-intersection
contact-surface: 0
crosses: formalism
crosses-rank: 4
topology: disjoint
mediator: 
borrows-from: []
lends-to: []
mutual-with: []
computed-in: ["[[C35-soil-ha]]", "[[C42-soil-ha-theory]]", "[[C43-soil-ha-replication]]"]
uses-move: []
rests-on: ["[[C6-damage-healing-ratio]]"]
tags: [node/gap, crosses/formalism, evidence/citation-intersection, standing/narrowed]
last-checked: 2026-09-05
exit: computation
extends-to: [sustainability, conservation]
next-step-cost: S
note: "NARROWED 2026-09-05 by a four-leg deep inquiry. Leg 2 (cumulative fatigue <-> aggregate breakdown) is WITHDRAWN on sign: Miner damage D = sum n_i/N_i is monotone non-decreasing, while mean weight diameter under identical wet-dry cycling can rise as well as fall - aggregates strengthen under cycling in vegetated soil and weaken in bare soil - so MWD is not a damage variable and no Weibull beta fitted to MWD(n) means anything. Leg 1 (wear <-> erosion detachment) survives, but only as a citation gap: the 40-cell decade grid (four mechanics anchors 1945-1995 x ten soil anchors 1936-2022) is 0 on OpenCitations and 0 on Semantic Scholar wherever S2 sees both anchors, nine controls fire including the age controls Yoder 1936 x Le Bissonnais 110/105 and W&S 1959 x RUSLE 26 that close failure mode 6, and E = 75.6 on Archard x Nearing at the narrow scoped N (7.6 at 10x) so the Archard/Miner/Paris rows survive. But the gap names NO MISSING OBJECT: crosses stays formalism because the two sides do write laws of the same species, and the formalism does not transfer - Archard is linear in F.s through the origin with resistance as a divisor (V ~ 1/H), WEPP is linear in EXCESS shear with resistance as a threshold (D_c = K_r(tau - tau_c)), and C35 section 4 shows the dimensionless soil analogue K_soil is not a constant but sweeps orders of magnitude within one soil as tau varies. Topology stays DISJOINT: a mediator must be read by both sides, and Sklar & Dietrich 2001/2004 and Hsu, Dietrich & Sklar 2008 read tribology only - Hsu x all six soil anchors = 0 while Hsu x Sklar 2004 fires at 7, so nothing traverses. A parallel adversarial leg reports that Hsu 2008 writes Archard's law out in full and cites Archard 1953 in its printed text; Crossref's 102 deposited references contain no archard/wear/tribolog match. If the text-level citation is real it is a ONE-WAY BORROW, geomorphology -> tribology, which does not make the topology mediated; the disagreement is open and needs a full-text read. Computed in C35 (soil on C6's Ha axis), C42 (Ha is structural-only for a stock; no steady state above P0 = 0.077 mm/yr; 300 mm gone in ~197 yr under conventional agriculture) and C43 (1,053 US sites: median T/P = 22.3, and Spearman rho(T, P) = -0.180, p = 4.5e-9)."
---

# Wear, fatigue, and the removal of soil

**STANDING: NARROWED** · evidence: citation-intersection · contact surface: 0 · last checked 2026-09-05

> **Narrowed 2026-09-05.** Tribology has spent eighty years writing `V = K·F·s/H` for **how much
> solid a repeated mechanical insult removes from a surface**, and agricultural soil-erosion
> modelling has spent the same eighty years writing `D_c = K_r(τ − τ_c)` for the same measurement
> on soil without ever citing it. That absence is measured — forty decade-binned cells, two
> providers, nine controls, all zero — and it is **all that survives**. What does *not* survive:
> the fracture-mechanics leg (`D = Σ n_i/N_i` against mean weight diameter under wet–dry cycling)
> is **withdrawn on sign**, because MWD is not a damage variable; and the claim that soil science
> is missing an object it could import is **withdrawn on transfer**, because the Archard form does
> not survive the crossing ([[C35-soil-ha]] §4). The surviving claim is a **citation gap with no
> missing object**: two fields fit the same species of constant to the same measurement, each has
> forty years of published trouble fitting it, and neither has read the other's.

Two legs were claimed; **one survives.**

- **Leg 1 — wear ↔ erosion detachment. SURVIVES, as a citation gap only.** Archard 1953 /
  Meng & Ludema 1995 against Nearing 1989 (WEPP) / Le Bissonnais 1996. The zeros are real and
  the objects are the same species (§*The two vocabularies*). The **formalism does not transfer**:
  Archard's resistance is a divisor and his law is linear through the origin, WEPP's is a
  threshold and its law is linear only in excess shear, and [[C35-soil-ha]] §4 shows the
  dimensionless soil analogue `K_soil` is *not a constant* — it sweeps orders of magnitude within
  a single soil just by varying `τ`. So `crosses: formalism` records that both sides write laws of
  the same kind, **not** that either could adopt the other's.
- **Leg 2 — cumulative fatigue ↔ aggregate breakdown under wet–dry cycling. WITHDRAWN
  2026-09-05, on sign.** Miner's `D = Σ n_i/N_i` is monotone non-decreasing and carries no repair
  term. Mean weight diameter is not: under identical wet–dry cycling **aggregates can strengthen**
  — MWD rises in vegetated soil and falls in bare soil, and rises over the first cycles before
  falling later even in a single treatment. Two opposed rates run at once, so the state variable is
  not a damage fraction and a Weibull `β` fitted to MWD(`n`) would be a shape parameter fitted to a
  non-monotone series. The right object for aggregates is not Miner but
  [[C6-damage-healing-ratio]]'s `Ha = k_r/k_d` itself.

The `Ha` instantiation that leg 2 was reaching for stands on its own, independent of the fatigue
framing: erosion rates as `k_d`, soil-formation rates as `k_r`, filling a row C6 left blank. That
computation is [[C35-soil-ha]], and its theory and replication are [[C42-soil-ha-theory]] and
[[C43-soil-ha-replication]].

## The two vocabularies

| | Mechanics side | Soil-science side |
|---|---|---|
| **The removal law** | Archard: wear volume `V = K·(F·s)/H` — removed volume ∝ normal load × sliding distance ÷ indentation hardness | WEPP (Nearing 1989): detachment capacity `D_c = K_r(τ − τ_c)` — mass removed per area per time ∝ excess hydraulic shear |
| **The fitted constant** | `K`, the **Archard wear coefficient**, dimensionless, spanning orders of magnitude and not predicted from bulk properties (Meng & Ludema 1995 exists because several hundred wear equations do not predict it) | `K_r`, **rill erodibility** (s/m), and `K_i`, **interrill erodibility**; and USLE/RUSLE's **K-factor**, a soil erodibility index. All calibrated, none derived |
| **The threshold** | none in Archard's form; wear is linear in `F·s` through the origin | `τ_c`, **critical shear stress** — below it, detachment is zero |
| **The repeated-insult law** | Miner: `D = Σ n_i/N_i`, failure at `D = 1`. Paris: `da/dN = C(ΔK)^m`, damage per cycle as a power of the driving range | **aggregate stability under wet–dry cycles**: apply *n* wetting/drying or slaking cycles, report **mean weight diameter (MWD) loss** or the % of aggregates surviving. The cycle count is reported; no damage law is fitted to it |
| **What accumulates** | a scalar damage fraction, or a crack length | an aggregate-size distribution, or a soil depth |

Both sides are quantified, both are published as calibrated laws, and the four objects
`K`, `K_r`, `K_i`, `K_USLE` are the same *species* of object: an empirically fitted dimensional
constant standing in for an unresolved contact mechanism.

## Provenance — two providers, decade-binned, mediator-probed 2026-09-05

**Instrument.** Citer-set intersection, `python _scripts/intersect.py` (self-test passed
2026-09-05: phantom blank key dropped, provider interface OK). Citer sets pulled once per
anchor per provider and intersected locally. Providers actually run:

| provider | endpoint | status this run |
|---|---|---|
| **OpenCitations** | `api.opencitations.net/index/v1/citations/<doi>` | all 19 anchors OK |
| **Semantic Scholar** | `api.semanticscholar.org/graph/v1/paper/DOI:<doi>/citations` | 17 of 19 OK; **no record** for Miner 1945 `10.1115/1.4009458` or RUSLE 1991 `10.1080/00224561.1991.12456571` — a coverage hole, recorded as `err`, **never as a zero** |
| **OpenAlex** | `api.openalex.org` | one probe resolved Archard to `W1990351237`, the next call returned *"insufficient budget … resets at midnight utc"*. **Daily budget exhausted; OpenAlex contributes nothing to this round.** |

Blank/DOI-less records dropped before set construction (OpenCitations): Archard 21, Paris 15,
Miner 13, Meng 2, Amézketa 1, Yoder 1, Emerson 1, Borrelli 9, Van Oost 1, Shao 1; 0 for
Nearing, Le Bissonnais, Denef, RUSLE, Wischmeier & Smith 1959, Rieke, both Sklar & Dietrich.
Every anchor DOI below re-verified against **Crossref**
`api.crossref.org/works/<doi>?mailto=deciduusleaf@gmail.com`, same day, title + year + first
author + `is-referenced-by-count`.

**Anchors added this round** (all Crossref-verified 2026-09-05; the four mechanics anchors and
the 1989–2001 soil anchors are unchanged and their counts reproduce the previous run exactly):

| side | anchor | DOI | Crossref refby | OC set | S2 set |
|---|---|---|---|---|---|
| B 1930s | Yoder 1936, *A Direct Method of Aggregate Analysis of Soils*, Agron. J. | `10.2134/agronj1936.00021962002800050001x` | 1,142 | **1,123** | **1,232** |
| B 1940s | Ellison 1948, *Soil Erosion*, SSSAJ | `10.2136/sssaj1948.036159950012000c0107x` | 21 | **21** | **16** |
| B 1950s | Wischmeier & Smith 1959, *A Rainfall Erosion Index for a Universal Soil-Loss Equation*, SSSAJ | `10.2136/sssaj1959.03615995002300030027x` | 398 | **395** | **467** |
| B 1960s | Emerson 1967, *A classification of soil aggregates based on their coherence in water*, Aust. J. Soil Res. | `10.1071/sr9670047` | 252 | **258** | **272** |
| B 2010s | Borrelli 2017, *Global impact of 21st century land use change on soil erosion*, Nat. Commun. | `10.1038/s41467-017-02142-7` | 2,344 | **2,260** | **2,311** |
| B 2020s | Rieke *et al.* 2022, *Evaluation of aggregate stability methods for soil health*, Geoderma | `10.1016/j.geoderma.2022.116156` | 130 | **114** | **117** |
| M | Sklar & Dietrich 2001, *Sediment and rock strength controls on river incision into bedrock*, Geology | `10.1130/0091-7613(2001)029<1087:SARSCO>2.0.CO;2` | 437 | **706** | **710** |
| M | Sklar & Dietrich 2004, *A mechanistic model for river incision into bedrock by saltating bed load*, WRR | `10.1029/2003WR002496` | 612 | **653** | **621** |
| M | Van Oost *et al.* 2000, *Evaluating … soil erosion by water and tillage*, Landscape Ecol. | `10.1023/a:1008198215674` | 476 | **476** | **464** |
| M | Shao 2001, *A model for mineral dust emission*, JGR-Atmos. | `10.1029/2001JD900171` | 395 | **447** | **424** |

**Anchors that do not exist as citable DOI records.** Ellison 1947 *Soil erosion studies*,
Agricultural Engineering **28** has no DOI in Crossref; Wischmeier & Smith's Agriculture
Handbooks **282** (1965) and **537** (1978) likewise. Both were replaced by the nearest
DOI-bearing work of the same decade and lineage (Ellison 1948 SSSAJ; Wischmeier & Smith 1959
SSSAJ, the paper that defines the USLE R-factor). Ellison 1948's citer set is 21/16 works and
is **too small to be informative at any field-scale `N`** — it is listed for completeness and
carries no weight.

### Per-provider agreement

| pair | OC N_A / N_B / ∩ | S2 N_A / N_B / ∩ | verdict |
|---|---|---|---|
| Archard × Nearing | 6,803 / 1,122 / **0** | 6,912 / 1,193 / **0** | agree |
| Archard × Le Bissonnais | 6,803 / 1,207 / **0** | 6,912 / 1,193 / **0** | agree |
| Paris × Le Bissonnais | 5,461 / 1,207 / **0** | 6,027 / 1,193 / **0** | agree |
| Meng & Ludema × Archard (ctl) | 767 / 6,803 / **242** | 832 / 6,912 / **272** | agree, 12% spread |
| Amézketa × Le Bissonnais (ctl) | 991 / 1,207 / **204** | 977 / 1,193 / **202** | agree |
| Denef × Le Bissonnais (ctl) | 604 / 1,207 / **38** | 613 / 1,193 / **35** | agree |
| Yoder 1936 × Le Bissonnais (ctl) | 1,123 / 1,207 / **110** | 1,232 / 1,193 / **105** | agree |
| Borrelli × Nearing (ctl) | 2,260 / 1,122 / **65** | 2,311 / 1,193 / **62** | agree |
| Rieke 2022 × Le Bissonnais (ctl) | 114 / 1,207 / **9** | 117 / 1,193 / **8** | agree |
| Miner × Paris (ctl) | 4,762 / 5,461 / **257** | *err — S2 has no Miner record* | OC only |
| RUSLE × Nearing (ctl) | 603 / 1,122 / **60** | *err — S2 has no RUSLE record* | OC only |

Set sizes differ by 2–13% between providers, as the method note predicts; **no gap cell and no
control changed sign.** The two Miner-row and RUSLE controls are single-provider and are marked
as such.

### The decade grid — 40 cells, 40 zeros, on both providers

Soil side now spans **1936–2022**; mechanics side spans **1945–1995**. Every cell is the
intersection count; every one is 0 on OpenCitations, and 0 on Semantic Scholar wherever S2 sees
both anchors (the Miner row is OpenCitations-only). `E` is the **union floor** — the largest
`E` and therefore the friendliest number to this claim; never quotable alone.

| A ＼ B (decade) | Yoder 36 (1,123) | Ellison 48 (21) | W&S 59 (395) | Emerson 67 (258) | Nearing 89 (1,122) | Le Biss 96 (1,207) | Amézketa 99 (991) | Denef 01 (604) | Borrelli 17 (2,260) | Rieke 22 (114) |
|---|---|---|---|---|---|---|---|---|---|---|
| **Archard 1953** (6,803) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Meng & Ludema 1995** (767) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Miner 1945** (4,762) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Paris & Erdogan 1963** (5,461) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

E at the union floor for the four corner cells: Archard × Yoder 963.9, Archard × Rieke 112.1,
Paris × Yoder 931.5, Meng × Rieke 99.2.

**Mode 6 (diachronic drift) is now addressed, and the age control is what closes it.** The
worry was that a 1989–2001 soil sample could not tell a real gap from a vocabulary that had
simply moved. Two new controls answer it directly: **Yoder 1936 × Le Bissonnais 1996 = 110/105**
and **W&S 1959 × RUSLE 1991 = 26** — the instrument sees 1930s and 1950s soil anchors being
co-cited with 1990s ones, so the 1936 and 1959 anchors are *visible*, not merely old. Their zero
against every mechanics anchor is therefore a measurement, not an artifact of age. Symmetrically
**Rieke 2022 × Le Bissonnais = 9/8** and **Borrelli 2017 × Nearing = 65/62** show the modern end
is visible too. The zero is a nine-decade zero.

Age-held control ratios (each holds the soil anchor fixed and swaps the mechanics anchor for a
soil one):

- Yoder 1936 fixed: `(0/6,803) / (110/1,207)` = **∞**
- W&S 1959 fixed: `(0/6,803) / (26/603)` = **∞**
- Rieke 2022 fixed: `(0/6,803) / (9/1,207)` = **∞**
- Borrelli 2017 fixed: `(0/6,803) / (65/1,122)` = **∞**

### The mediator probe — the objection an adversary will raise, run rather than answered

The adversary's move: *soil science does not need to cite Archard, because fluvial geomorphology
already runs a wear model (Sklar & Dietrich's saltating-bedload abrasion), and soil science cites
geomorphology.* If that path carried, the topology would be **mediated**, not disjoint, and the
gap would be a routing fact rather than an absence.

| mediator pairing | OC ∩ | S2 ∩ | distinct works |
|---|---|---|---|
| Sklar & Dietrich 2001 × Archard 1953 | **1** | 0 | 1 |
| Sklar & Dietrich 2004 × Archard 1953 | **1** | 0 | 1 |
| Sklar & Dietrich 2001/04 × Meng & Ludema 1995 | **1** / **1** | 0 / 0 | 1 (same work) |
| Sklar & Dietrich 2001/04 × Paris & Erdogan 1963 | **1** / **1** | 1 / 1 | 1 |
| Sklar & Dietrich 2001/04 × Miner 1945 | 0 / 0 | *err* | 0 |
| Sklar & Dietrich 2001 × Nearing 1989 | **1** | 2 | 1–2 |
| Sklar & Dietrich 2004 × Nearing 1989 | **2** | 3 | 2–3 |
| Sklar & Dietrich 2001/04 × Le Bissonnais 1996 | 0 / 0 | 0 / 0 | 0 |
| Sklar & Dietrich 2001/04 × Borrelli 2017 | **23** / **23** | 16 / 15 | **2** (see below) |
| Van Oost 2000 × Archard 1953 / Meng | 0 / 0 | 0 / 0 | 0 |
| Shao 2001 × Archard 1953 / Meng | 0 / 0 | 0 / 0 | 0 |
| *ctl* Van Oost 2000 × Nearing 1989 | **26** | 28 | fires |
| *ctl* Sklar 2001 × Sklar 2004 | **281** | 276 | fires |
| **Hsu, Dietrich & Sklar 2008** × Archard 1953 | **2** | — | 2 |
| Hsu 2008 × Meng & Ludema | **1** | — | 1 |
| Hsu 2008 × Miner / Paris | 0 / 0 | — | 0 |
| **Hsu 2008 × every soil anchor** (Nearing, Le Bissonnais, Amézketa, Denef, Yoder, Borrelli) | **0 ×6** | — | **0** |
| *ctl* Hsu 2008 × Sklar & Dietrich 2004 | **7** | — | fires |

**Every non-zero cell was inspected; there are eight of them and they resolve to five works.**

- `10.1103/physreve.88.032205` — **Lefebvre & Jop 2013, *Erosion dynamics of a wet granular
  medium*, Phys. Rev. E.** Co-cites Sklar & Dietrich **and** Archard **and** Meng & Ludema. This
  is the single work in the whole run that touches tribology and erosion in one reference list.
  It is soft-matter physics, not soil science.
- `10.5194/esurf-9-1531-2021` — **Bodek & Jerolmack 2021, *Breaking down chipping and
  fragmentation in sediment transport*, Earth Surf. Dynam.** Co-cites Sklar & Dietrich and
  **Paris & Erdogan** — fracture mechanics applied to sediment attrition. The nearest miss in
  the vault: it is leg 2's formalism, on grains, in a geomorphology journal.
- `10.1016/b978-0-444-53802-4.00124-x` — Tucker 2015, *Landscape Evolution*, Treatise on
  Geophysics (review, cites Sklar and Nearing).
- `10.1016/j.catena.2017.01.023` — Yang *et al.* 2017, CATENA, gully-bed hydraulics (cites Sklar
  and Nearing).
- `10.1017/9781108164108` — **Rhoads 2020, *River Dynamics*, Cambridge.** The 23-hit
  Sklar × Borrelli cell is **one monograph deposited with chapter-level DOIs**
  (`…108`, `…108.001` … `…108.022`), plus one 2026 Earth-Sci. Rev. article on S2. Counting it as
  23 would be a chapter-DOI inflation artifact; it is 2 works. **Recorded here because the same
  trap will inflate any future book-heavy cell.**

**The strongest form of the objection, and where it actually fails.** A parallel review of this
gap proposes **Hsu, Dietrich & Sklar 2008**, *Experimental study of bedrock erosion by granular
flows*, JGR-Earth Surf. `10.1029/2007JF000778`, as the mediator on the grounds that it writes
Archard's law out in full and cites Archard 1953. Two checks, 2026-09-05:

- **Crossref deposits 102 references for Hsu 2008 and not one of them matches Archard, "wear" or
  "tribolog"** in either structured or unstructured form; OpenCitations resolves 85 of those to
  DOIs and Archard's `10.1063/1.1721448` is not among them. That is evidence against the
  citation, **not proof of its absence** — a deposited list can be incomplete and the printed
  bibliography is a different object (see `CLAUDE.md`, *Numbers*). **Settling it needs a
  full-text read**, which this leg did not do; it is logged as an open disagreement.
- **The second hop is empty regardless.** Hsu 2008 has 69 citers on OpenCitations and its
  intersection with **all six** soil anchors — Nearing, Le Bissonnais, Amézketa, Denef, Yoder,
  Borrelli — is **0**, while its control against Sklar & Dietrich 2004 fires at 7. So even
  granting the first hop in full, **no soil-science work reaches mechanics through Hsu**: the
  proposed path terminates inside geomorphology. A mediator that nothing traverses does not make
  a topology mediated.

**Verdict: the mediator does not carry, and `topology` stays `disjoint`.** Three findings, in
descending force:

1. **Sklar & Dietrich cite no wear anchor at all.** Their deposited reference lists
   (OpenCitations `/references/`, 2026-09-05) are 59 DOIs for the 2004 WRR paper and 12 for the
   2001 Geology paper, and **none of the four mechanics anchors appears in either.** The
   geomorphology → mechanics leg of the proposed path is empty at the anchor level. A wear-like
   model was written there independently; it was not imported.
2. **No work co-cites a mechanics anchor and a soil-science anchor.** The two mechanics-side
   mediator hits (Lefebvre & Jop; Bodek & Jerolmack) are physics and geomorphology; the
   soil-side hits (Tucker; Yang; Rhoads) cite no mechanics anchor. The chain is
   A—(2 works)—M—(3 works)—B with **no overlap at M**, so nothing is routed end to end.
3. **The two obvious alternative mediators are flat zero on both providers**: tillage erosion
   (Van Oost 2000) × Archard = 0, wind-erosion abrasion (Shao 2001) × Archard = 0, while
   Van Oost × Nearing = 26/28 confirms tillage erosion sits *inside* soil erosion. The
   mediator-side controls fire; the mediator-to-mechanics cells do not.

`contact-surface` therefore stays **0**: it counts works bridging the gap as stated, and there
are none. What the probe did buy is a named, inspected **nearest miss** — Lefebvre & Jop 2013
and Bodek & Jerolmack 2021 — which is the first place a real bridge would appear if one ever did.

### Scoped `N_universe`, and `E` at three denominators

OpenAlex concept counts were unavailable (budget). The denominator is therefore a **Semantic
Scholar `paper/search/bulk` total**, fetched 2026-09-05, which matches a phrase against title and
abstract and so **understates** each field (not every tribology paper prints the word). It is an
**estimate**, and is used only to bound `E`:

| phrase | S2 bulk total |
|---|---|
| `tribology` | 13,267 |
| `"wear coefficient"` | 1,785 |
| `"fatigue damage"` | 24,077 |
| `"soil erosion"` | 54,225 |
| `"aggregate stability"` | 7,359 |
| `tribology \| wear` | 387,111 |
| `"bedrock incision"` (mediator field, for scale) | 319 |

- **Narrow scoped `N` ≈ 1.0×10⁵** — the union of the five field-defining phrases, overlaps
  ignored (which makes it slightly high, i.e. conservative for this claim).
- **Broad scoped `N` ≈ 4.5×10⁵** — `tribology | wear` plus the soil terms; the generous reading.
- **10× the narrow figure, `N = 1.0×10⁶`** — the mandatory sensitivity step.

`E = |A|·|B| / N`:

| cell | \|A\|·\|B\| | E at floor | E at 1.0×10⁵ | E at 4.5×10⁵ | E at 1.0×10⁶ |
|---|---|---|---|---|---|
| Archard × Nearing 1989 | 7.63×10⁶ | 963.2 | **75.6** | 17.0 | 7.6 |
| Archard × Yoder 1936 | 7.64×10⁶ | 963.9 | **75.6** | 17.0 | 7.6 |
| Archard × Borrelli 2017 | 1.54×10⁷ | 1,696.4 | **152.2** | 34.2 | 15.4 |
| Miner × Le Bissonnais 1996 | 5.75×10⁶ | 962.9 | **56.9** | 12.8 | 5.7 |
| Archard × Emerson 1967 | 1.76×10⁶ | 248.6 | **17.4** | 3.9 | 1.8 |
| Meng & Ludema × Rieke 2022 | 8.74×10⁴ | 112.1 | **0.87** | 0.19 | 0.09 |

The Archard, Miner and Paris rows survive all three denominators: a zero against `E = 7.6` is
still a 7.6-fold deficit at ten times the narrow universe. **The Meng & Ludema row and the small
soil anchors (Emerson, W&S 1959, Rieke, Ellison) fall below or near `E = 1` at field scale and
are corroboration, not evidence** — an honest reading is that the claim rests on Archard, Miner
and Paris against Yoder, Nearing, Le Bissonnais, Amézketa, Denef and Borrelli, and that the
decade extension is carried by Yoder 1936 (`E = 75.6` narrow, `7.6` at 10×) more than by any
other new anchor.

**Superseded.** The last line of *What would close it* — that a 1930s–1960s soil anchor "has not
been run" — is discharged by this round: Yoder 1936, Ellison 1948, Wischmeier & Smith 1959 and
Emerson 1967 were run against all four mechanics anchors and returned 0 on both providers. The
mode-6 hole is closed; the claim is unchanged in direction and better supported in span.
`standing` stays **live**: nothing narrowed it, and no bridge appeared.

**Failure modes, re-checked** ([[failure-modes]]). Modes 1–5 still do not apply (citer-set
intersection, not a string query). **Mode 6 addressed** as above. Two new instrument traps were
met and are recorded: (a) **provider coverage holes are not zeros** — S2 holds no record for
Miner 1945 or RUSLE 1991 and those cells are `err`; (b) **chapter-level DOIs inflate a cell** —
one Cambridge monograph produced 23 apparent hits.

**Strongest objection, both legs, stated rather than answered.**

1. *Leg 1: the abrasive medium is the difference and it is not a detail.* Archard's law is
   derived for two solids in dry contact with the real contact area set by plastic yielding at
   asperities. Soil detachment by overland flow is fluid shear on a cohesive granular bed with no
   solid counterface, so indentation hardness `H` has no counterpart and `K` cannot be read the
   way tribology reads it. The defensible comparison is between `K` and `K_r` **as fitted
   constants** — how many orders each spans, and whether either was ever predicted rather than
   fitted — not a claim of shared mechanism. [[C35-soil-ha]] §4 works the mapping through and
   reports where it breaks.
2. *Leg 2: the objection was right and its diagnosis was wrong — the leg is withdrawn.* The
   original worry was **first-cycle dominance** (slaking, not fatigue). That is not what kills it.
   What kills it is **sign**: the same cycling protocol *raises* MWD in some treatments and lowers
   it in others, and raises it over early cycles before lowering it later, so aggregate breakdown
   and re-aggregation run simultaneously and MWD(`n`) is not monotone. Miner's `D` cannot be
   non-monotone. **Leg 2 is withdrawn as a fatigue analogy 2026-09-05** and retained only as the
   `Ha` instantiation of [[C35-soil-ha]]. The residual, and it is real: `MWD(n)` should approach a
   treatment-specific asymptote `MWD_∞` set by `Ha = k_r/k_d`, approached *from below* where
   re-aggregation wins and *from above* where breakdown does — so **the sign of `dMWD/dn` at
   `n` = 1 does not predict `MWD_∞`**, and any study reporting only cycles 1 and *n* can report the
   wrong direction of effect. That needs ≥3 cycle points and is a soil-side prediction, not a
   mechanics import.

## What would close it

Revised 2026-09-05. Two objects, both computable from published tables, in the cheap order:

1. **The soil row of C6's axis** — `Ha = k_r/k_d` with erosion rate as `k_d` and soil formation
   rate as `k_r`. **Done three times over**: [[C35-soil-ha]] computes the rows,
   [[C42-soil-ha-theory]] shows what `Ha` can and cannot mean for a *stock* (structural only; no
   steady state at all once `E ≥ P0` = 0.077 mm/yr, which every managed row exceeds; the `A`
   column deleted), and [[C43-soil-ha-replication]] runs C35 §5's own falsifier on 1,053 US sites.
   That is why `exit: computation` and `next-step-cost: S`. **It does not close the gap**, because
   a computation performed here is not a citation made there — and after the depth gate it does
   not even close leg 2, which is withdrawn.
2. **`K` and `K_r` on one dimensionless axis** — normalise Archard's wear coefficient and WEPP's
   rill erodibility to the same form (removed volume per unit work per unit resisting stress) and
   tabulate the range each spans, from Archard's own table and Meng & Ludema's compilation
   against WEPP's published `K_r` calibration ranges. The prediction that follows: **both span
   4–6 orders of magnitude and neither is predictable from bulk properties**, which would say two
   fields independently hit the *same* failure of a constitutive law. C35 §4 shows the unit
   reconciliation is where this dies if it is not written out first, and does write it out.
3. ~~**A Weibull/Miner damage curve for aggregate stability against wet–dry cycle number**, with
   its shape parameter placed on [[C18-durability-axis]]'s β axis.~~ **WITHDRAWN 2026-09-05.**
   MWD is not a monotone damage variable — see the legs list above and objection 2 — so a Weibull
   `β` fitted to MWD(`n`) is a shape parameter fitted to a series that changes direction. **The
   replacement is [[C6-damage-healing-ratio]] applied to aggregates**: `MWD(n) → MWD_∞` set by
   `Ha = k_r/k_d`, approached from below in aggregating treatments and from above in degrading
   ones. Discriminating prediction: **the sign of `dMWD/dn` at `n` = 1 does not predict `MWD_∞`**,
   so a study reporting only cycles 1 and *n* can report the wrong direction of effect. Needs ≥3
   cycle points; two-point papers must be excluded and said to be excluded. Denef 2001 and the
   Amézketa 1999 review print cycle-resolved tables and are the cheap test.

What would **overturn** what is left of it: a work that cites a mechanics anchor **and** a
soil-science anchor in one reference list. None exists in this run; the nearest misses are
Lefebvre & Jop 2013 and Bodek & Jerolmack 2021, both outside soil science. The 1930s–1960s
decade hole named here in the previous revision has since been run and returned zero (Provenance
above), and is discharged.

## Narrowing — 2026-09-05, four-leg deep inquiry

**`standing: live` → `narrowed`.** Four legs ran against this gap on 2026-09-05: an adversarial
review, a provenance re-run, and two computations ([[C42-soil-ha-theory]],
[[C43-soil-ha-replication]]). What changed, and what did not.

| Field | Before | After | Why |
|---|---|---|---|
| `standing` | live | **narrowed** | leg 2 withdrawn; leg 1 demoted to a citation gap with no missing object |
| `crosses` / `crosses-rank` | formalism / 4 | **unchanged** | both sides do write constitutive laws of the same species — but see the transfer caveat below |
| `topology` | disjoint | **unchanged** | a mediator must be read by *both* sides; the proposed one is read by neither soil anchor |
| `contact-surface` | 0 | **unchanged** | still no work bridging the gap as stated |
| `computed-in` | C35 | **C35, C42, C43** | the theory and replication legs |

**`crosses: formalism` does not mean the formalism transfers.** It records that `K`, `K_r`, `K_i`
and `K_USLE` are one species of object — an empirically fitted dimensional constant standing in
for an unresolved contact mechanism, unpredicted from bulk properties in both fields. It does
**not** license the import: Archard's resistance is a divisor and his law passes through the
origin; WEPP's resistance is a threshold and below `τ_c` detachment is exactly zero.
[[C35-soil-ha]] §4 does the algebra and finds `K_soil` is not constant. **The soil literature is
not missing an object it could take from tribology.** What it is missing is the other field's
forty years of published failure to predict its own constant.

**The mediator disagreement, recorded open.** The adversarial leg proposes `topology: mediated`
via bedrock-incision geomorphology, on the ground that **Hsu, Dietrich & Sklar 2008**
(`10.1029/2007JF000778`) writes Archard's `e_v = kWx/H` out in full and cites Archard 1953 in its
printed text. The provenance leg checked and reaches the opposite verdict. Both findings, so a
later reader can weigh them:

1. **The citation is not corroborated by metadata and is not settled.** Crossref deposits 102
   references for Hsu 2008 and none matches `archard`, `wear` or `tribolog`; OpenCitations
   resolves 85 to DOIs without `10.1063/1.1721448`. A deposited list can be incomplete and a
   printed bibliography is a different object (`CLAUDE.md`, *Numbers*), so this **does not
   disprove** the adversarial leg's claim — it means the claim rests on a full-text read neither
   leg recorded. **Settling it needs the PDF.**
2. **Granting it in full changes nothing, because the second hop is empty.** Hsu 2008 × all six
   soil anchors = **0** while its control against Sklar & Dietrich 2004 fires at 7. Sklar &
   Dietrich's own deposited lists (59 and 12 DOIs) contain no mechanics anchor at all.

**Orchestrator's ruling: `topology` stays `disjoint`, and the Archard citation in Hsu 2008 — if
the full text confirms it — is recorded as a ONE-WAY BORROW, geomorphology → tribology.** A
mediator has to be *read by both sides*; this one is read by neither soil anchor. A field that
borrows from tribology and is not itself cited by soil science does not route anything between
them. **The disagreement is open and is logged here rather than resolved.**
