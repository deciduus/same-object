---
name: C41-uncited-parent-sweep
type: computed
exit: computation
extends-to: [none]
next-step-cost: S
---

# Is the C37 "uncited parent" pattern general? Eight pairs, three intersections, two providers

> **NO — 3 of 8, not most.** [[C37-lolp-starvation-identity]] found grid and bird each
> rebuilding ruin theory with neither citing it. Running the same three-way test on eight of
> the project's confirmed same-object pairs gives **3 double rediscoveries (class iii)**,
> **3 one-sided (class ii)**, **2 where both sides already meet the parent (class i)**.
> The hypothesis "cross-domain gaps are usually two fields that both rediscovered an older
> parent" is **not supported**. What *is* supported is weaker and still useful: in **5 of 8**
> rows the parent test changed the reading of the gap — it names which side is the isolated
> one, which a two-way A×B intersection cannot do.

Provenance: `_scripts/c41_parents.py`, providers OpenCitations and Semantic Scholar, run
2026-09-05. Parent DOIs Crossref-verified the same day (`mailto=deciduusleaf@gmail.com`).
`E` is the **union floor** `N_A·N_B/(N_A+N_B−O)` throughout — the smallest defensible
denominator, therefore the largest `E` and the smallest `O/E`; it flatters every gap claim and
is not quotable alone ([[citation-intersection]]).

---

## 1. Parents named, with canonical citation

| # | Pair (A × B) | Candidate parent | Citable anchor, Crossref-verified 2026-09-05 |
|---|---|---|---|
| 1 | Billinton & Allan 1996 × McNamara & Houston 1987 | ruin theory | Asmussen & Albrecher, *Ruin Probabilities* 2010, `10.1142/7431` (refby 583) |
| 2 | Charnov 1976 × Gittins 1979 | optimal stopping | Wald 1945, *Sequential Tests of Statistical Hypotheses*, `10.1214/aoms/1177731118` (1,520) |
| 3 | White 2001 × Kendall 1953 | queueing theory | Bolch et al., *Queueing Networks and Markov Chains*, `10.1002/0471200581` (415) |
| 4 | Billinton & Allan 1996 × Aro et al. 1993 | renewal theory | Barlow & Proschan, *Mathematical Theory of Reliability*, `10.1137/1.9781611971194` (359) |
| 5 | Oguchi 2015 × Jones & Schmitz 2009 | survival analysis | Kaplan & Meier 1958, `10.1080/01621459.1958.10501452` (76,647) |
| 6 | Kimura, Maruyama & Crow 1963 × Murphy 1964 | Poisson mixture | Greenwood & Yule 1920, `10.2307/2341080` (552) |
| 7 | Scheffer 2009 × Si 2011 | first-passage / barrier escape | Kramers 1940, `10.1016/S0031-8914(40)90098-2` (7,867) |
| 8 | Walters & Holling 1990 × Duane 1964 | learning curve | Wright 1936, *Factors Affecting the Cost of Airplanes*, `10.2514/8.155` (2,263) |

**Substitutions forced by indexing, stated up front.** Lundberg 1903, Cramér 1930, Feller 1968,
Erlang 1917, Snell 1952, Chow–Robbins–Siegmund 1971, Cox 1962 and Crow 1974 have **no usable
DOI**; the row-3 and row-8 parents named in the brief (Kleinrock 1975, Crow 1974) are
unreachable and were replaced by an indexable member of the same literature. Snell 1952's
proposed DOI `10.1090/S0002-9947-1952-0050214-2` **404s at Crossref**. Row 3's B side
(Kendall 1953) sits *inside* the parent literature, so its `B×P` is near-tautological and is
reported but not read as evidence.

## 2. The table

`A×B` / `A×P` / `B×P` are the three observed intersections; `E` is the union floor for that
cell. `oc` = OpenCitations, `s2` = Semantic Scholar. `—` = provider blind (see §4).

| # | Pair | prov | `N_A` | `N_B` | `N_P` | **A×B** (E) | **A×P** (E) | **B×P** (E) | class |
|---|---|---|---|---|---|---|---|---|---|
| 1 | LOLP × starvation | oc | 2,058 | 422 | 515 | **0** (350) | **0** (412) | **0** (232) | **iii** |
| | | s2 | — | 482 | — | — | — | — | |
| 2 | Charnov × Gittins | oc | 4,088 | 1,012 | 1,517 | **5** (812) | **5** (1,107) | **13** (610) | **i** |
| | | s2 | — | 1,164 | — | — | — | — | |
| 3 | healing × Erlang-B | oc | 4,063 | 742 | 418 | **0** (627) | **0** (379) | **5** (269) | **ii** |
| | | s2 | 3,826 | 823 | 704 | **0** (677) | **0** (595) | **13** (383) | |
| 4 | availability × PSII repair | oc | 2,058 | 2,155 | 364 | **0** (1,053) | **1** (309) | **0** (311) | **iii** |
| | | s2 | — | 2,158 | — | — | — | — | |
| 5 | product β × recovery hazard | oc | 96 | 286 | 38,055 | **0** (72) | **0** (96) | **0** (284) | **iii** |
| | | s2 | 90 | 312 | — | **0** (70) | — | — | |
| 6 | genetic load × die yield | oc | 349 | 318 | 624 | **0** (166) | **1** (224) | **1** (211) | **i** |
| | | s2 | — | 332 | 677 | — | — | **2** (223) | |
| 7 | early warning × prognostics | oc | 3,934 | 1,783 | 7,837 | **1** (1,227) | **23** (2,624) | **0** (1,453) | **ii** |
| | | s2 | 3,957 | 1,891 | 5,509 | **1** (1,280) | **21** (2,308) | **0** (1,408) | |
| 8 | adaptive mgmt × Duane | oc | 996 | 500 | 2,217 | **0** (333) | **1** (688) | **5** (409) | **ii** |
| | | s2 | 1,132 | 515 | 2,375 | **0** (354) | **1** (767) | **6** (424) | |

Where both providers ran (rows 3, 5, 7, 8) they **agree on every intersection to within one
hit**, and agree exactly on all eight zeros. That is the two-instrument check the C37 table
lacked.

## 3. Hits inspected (up to 3 per nonzero cell, all Crossref-verified)

- **2 A×P** — 10.1101/2022.06.24.497481 *Control Limited Perceptual Decision Making*;
  10.1101/2024.06.07.597954 *…near-optimal confidence-guided waiting in rats*;
  10.1111/cogs.12743 *Make-or-Break* (Cog. Sci. 2019). **Decision neuroscience, not foraging
  ecology** — Charnov's contact with Wald is through a third community.
- **2 B×P** — 10.1007/978-3-031-05988-9_12 *Encounters with Martingales in Statistics and
  Stochastic Optimization*; 10.1016/j.ejor.2006.01.011; 10.1016/j.jet.2019.01.005 *Optimal
  learning before choice*. **Genuine**: the bandit literature descends from Wald openly.
- **3 B×P** — 10.1007/978-3-319-78822-7_1 and `_2` (two chapters of one Springer OR monograph);
  10.1007/978-3-540-79992-4_59; 10.1007/978-1-4614-3713-0 *Fundamentals of Queuing Systems*.
  Queueing texts citing queueing texts — the tautology §1 flagged.
- **4 A×P** — 10.1002/9781118029039.biblio is a **book's bibliography section deposited as its
  own DOI**. Not a work engaging either side; row 4 is a clean 0/0/0 once it is removed.
- **6 A×P** — 10.1017/s0016672300034686 (Gessler 1995, *Genetical Research*, Muller's ratchet).
  **6 B×P** — 10.1109/proc.1983.12619 (Stapper, *Integrated circuit yield statistics*) and
  10.1016/s0026-2714(96)00064-9 *Poisson mixture yield models for ICs: a critical review*.
  **Both genuine**, one hit per side: each field reached Greenwood–Yule separately.
- **7 A×P** — 10.1007/s00382-025-07880-9 (Greenland ice-core stochastic forcing);
  10.1007/s10884-014-9419-5 (random Poincaré maps); 10.1007/s11431-019-9557-2 (slowing critical
  transitions). **Genuine escape-rate physics.** The critical-transitions literature co-cites
  Kramers 21–23 times; **prognostics does so zero times on both providers.**
- **7 A×B** — 10.1007/s42524-021-0176-y *System reliability and system resilience* (the single
  co-citer, unchanged from [[G29-early-warning-prognostics]]).
- **8 A×P** — 10.1016/j.ecolmodel.2023.110609, an agent-based smallholder-adaptation model, not
  adaptive-management theory. **8 B×P** — 10.1016/j.cie.2018.11.055 *Uncertain learning curve
  and its application in scheduling*; 10.1108/jqme-09-2017-0060; 10.1016/s0360-8352(00)00063-2
  *Modeling the reliability of repairable systems in the aviation industry*. **Genuine** on the
  reliability side only.

## 4. What could not be indexed

Semantic Scholar returned **no record** for six anchors — a coverage hole, never a zero:
Billinton & Allan 1996 `10.1007/978-1-4899-1860-4`, Asmussen & Albrecher `10.1142/7431`,
Barlow & Proschan `10.1137/1.9781611971194` (three **monograph** DOIs), Wald 1945, Kimura,
Maruyama & Crow 1963, and **Charnov 1976** — the last already documented in
`providers/semanticscholar.py`'s DOI-coverage note and confirmed again here. Kaplan & Meier
1958 (76,647 Crossref refby) exceeds S2's offset-9999 paging cap; OpenCitations enumerated it
at 38,055. The adapter raises rather than truncating, because a truncated citer set
manufactures the gap the method tests. **Rows 1, 2 and 4 therefore rest on one provider.**

## 5. Class counts, and what they mean for the method

| class | rows | n |
|---|---|---|
| **(i)** both sides meet the parent — the gap is only A × B | 2, 6 | **2** |
| **(ii)** one side meets the parent | 3, 7, 8 | **3** |
| **(iii)** neither meets the parent — the C37 double rediscovery | 1, 4, 5 | **3** |
| **(iv)** parent not indexable at all | none whole; 8 named parents partly (§1) | **0** |

**The hypothesis fails as stated.** Three of eight is not "often", and this is the most
favourable sample available — a pair only reaches "confirmed same object" after someone already
noticed a shared formalism. **C37 is a real instance, not a rule.**

**What survives is a diagnostic, not a reordering.** In the three class-(ii) rows the parent
test says something a two-way intersection cannot: *which side is isolated*. Ecology co-cites
Kramers 21–23 times while prognostics does so zero times; reliability meets Wright 5–6 times
while adaptive management does not; queueing owns its own parent while self-healing polymers do
not touch it. In each case the "cross-domain gap" is really **one field standing outside a
literature the other is already inside** — a one-way borrow ([[one-way-borrowing]]), not a
mutual introduction, and a different repair job. That reclassification fires in 5 of 8 rows
(three class-ii plus the two class-i, where the honest verdict is *the parent is already shared
and only the sibling link is missing*). **Because the "most gaps are class iii" trigger was NOT
met, no mandatory edit to [[citation-intersection]] is proposed**; an optional third-anchor step
is drafted in `PENDING-log-C41.md`, deliberately weaker than the brief anticipated.

## 6. Honesty

1. **The instrument does not measure "cites the parent".** An intersection `A×P` counts works
   citing *both* A and P. It is co-citation, not a citation from A to P. Every "meets the
   parent" verdict above is really "the two literatures share readers". Whether Charnov 1976
   itself cites Wald was **not** checked and cannot be checked this way.
2. **Parent choice is a judgement, and it is the load-bearing one.** Eight different parents
   would give eight different tables. Row 3's parent and its B side are the same literature;
   row 5's parent is 400× larger than either side, so its floor `E` is set almost entirely by
   the small side. A hostile reviewer could name a different parent for any row and move its
   class.
3. **Monographs have poor DOI coverage.** Three of the eight parents are books, S2 holds none
   of them, and OpenCitations holds book-level DOIs unevenly. Row 1's three zeros are a
   **single-provider** result on a monograph proxy — exactly the caveat C37 §5.5 made about
   itself. This note reproduces that limitation, it does not remove it.
4. **`E` is the union floor only.** No concept-scoped `N` was fetched for any row, so every
   `O/E` computable from this table is the most flattering one available, and none is quoted.
5. **Rows 5 and 7 reuse prior work.** Row 5's survival-analysis leg was already run in
   [[G32-recovery-time-hazard-shape]] (recovery ecology 0 against Cox, Kaplan–Meier and
   Muenchow, six hits inspected); this note reproduces the Kaplan–Meier zero on the same
   provider and adds the product-lifespan side. Row 7's A×B = 1 reproduces
   [[G29-early-warning-prognostics]] exactly.
6. **Zeros are absence at anchor level.** As in C37, a third work making the connection while
   citing neither anchor is invisible to this test.
7. **Eight rows is not a rate.** [[C21-rediscovery-clustering]] already found the project's
   rediscovery instances scatter across ~9 effective object-types; three class-iii rows out of
   eight is consistent with that scatter and does not distinguish it from noise.

See [[C37-lolp-starvation-identity]], [[C21-rediscovery-clustering]],
[[Q2-independent-rediscovery]], [[citation-intersection]], [[one-way-borrowing]].
