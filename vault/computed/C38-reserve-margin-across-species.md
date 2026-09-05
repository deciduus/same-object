---
name: C38-reserve-margin-across-species
type: computed
exit: prediction
extends-to: [ecology, sustainability]
next-step-cost: M
---

# Reserve margin across species — is the parid's 2–4× an artifact?

> **No. Across eight species the dusk-or-autumn reserve divided by the expected draw spans
> `−74%` to `+2400%`, and the spread is not noise — it is the demand-side lever. Every animal
> that can lower its own metabolic setpoint carries a margin far above the grid's `15–20%`
> (`+75%` bat, `+265%` deer mouse, `+354%` rufous hummingbird); every one of those same animals
> falls *into or below* the grid band the moment the lever is unavailable (`+1.5%` cold deer
> mouse, `−2.8%` bat in a bad roost, `+10%/−8.3%` normothermic parid); and the one species with
> no lever at all — the common shrew — sits at `−38% to −74%` and cannot hold a winter night on
> stored energy at any dusk fat load.** Replication leg of [[C33-lolp-starvation]] §4. The
> parid number replicates; the *interpretation* narrows from "biology is conservative" to
> "biology is sized on the demand side."

Arithmetic, every input a transcribed literal: `python _scripts/c38_margins.py` from `vault/`.

---

## 1. The quantity, unchanged from C33 §4

```
margin  =  (reserve − expected draw) / expected draw          ratio = 1 + margin
```

Grid convention for the same statistic is the **planning reserve margin**: firm capacity over
peak demand, minus one. C33 computed the left-hand side for one 10–13 g parid and got **+57.1%**
typical / **+31.0%** cold, collapsing to **+10.0% / −8.3%** with nocturnal hypothermia removed.
This note recomputes the identical division for every other system with published numbers, and
adds the engineered rows on the right.

Grades: **PRIMARY** = both numbers read off the source's own table; **DERIVED** = both numbers
primary, ratio is this note's; **PUBLISHED** = the source prints the ratio itself; **ASSUMED** =
an input is a convention. Fetches all **2026-09-05**.

---

## 2. One table, one axis

| System | reserve | expected draw | worst-case draw | **margin** | worst | demand-side lever | source, and where the number sits | grade |
|---|---|---|---|---|---|---|---|---|
| **Rufous hummingbird**, torpid all night | 59.4 kJ (1.5 g fat) | 2.36 kJ | 4.58 kJ | **+2421%** | +1197% | torpor **engaged** | Hiebert 1993, *Auk* 110:787–797, `10.2307/4088634`, §*Body Mass and Torpor — Autumn* (1.5 g above lean mass) × §*Seasonality of Torpor* (661 mL O₂ / 12 h night); saving from Shankar 2020 `10.1111/jav.02305` | DERIVED |
| **Little brown bat**, Hranac medians | 2.32 g fat | 0.48 g fat | 1.69 g (WNS) | **+383%** | +37% | hibernation | Hranac 2021, *Ecol. Evol.* 11:11604, `10.1002/ece3.7641`, Results *Body mass* + *Overwinter hibernation survival* | PUBLISHED |
| **Rufous hummingbird**, normothermic night | 59.4 kJ | 13.09 kJ | 13.09 kJ | **+354%** | +354% | torpor available, unused | as above | DERIVED |
| **Deer mouse**, warm-acclimated ♀, 12 h night | 113.8 kJ (3.077 g) | 31.2 kJ | 61.4 kJ | **+265%** | +86% | daily torpor (facultative) | Rezende 2009, *JEB* 212:2795, `10.1242/jeb.032789`, **Table 1** — fat and V̇O₂ on the *same animals* | DERIVED |
| **Ruby-throat**, crop only vs torpid night | 2.65 kJ | 1.23 kJ | 2.67 kJ | **+116%** | −0.9% | torpor engaged | Eberts 2019, *Diversity* 11:9, `10.3390/d11010009`, Table 2 fn × Shankar 2020 | DERIVED |
| **Little brown bat**, selected roost | 360 d | 181 d | 181 d | **+99%** | +99% | hibernation + microclimate choice | Haase 2019, *PLoS ONE* 14:e0222311, `10.1371/journal.pone.0222311`, Results | PUBLISHED |
| **Little brown bat**, mean microclimate | 317.5 d | 181 d | 181 d | **+75%** | +75% | hibernation | same, **Fig. 3A** | PUBLISHED |
| **Parid 10–13 g**, night, hypothermia ON | 33.0 kJ | 21.0 kJ | 25.2 kJ | **+57%** | **+31%** | hypothermia, ε = 30% | Brodin 2017 `10.1007/s00442-017-3923-3` T1+T2, via [[C33-lolp-starvation]] §4 | PRIMARY |
| — *NERC design band, 15 of 15 assessment areas* — | — | — | — | **7.0 – 26.3%** | — | demand response (external) | **NERC, 2025 LTRA**, *Summary of Planning Reserve Margins and Reference Margin Levels by Assessment Area*, **pp. 175–176**, PDF fetched from nerc.com | PRIMARY |
| **Parid**, hypothermia **OFF** | 33.0 kJ | 30.0 kJ | 36.0 kJ | **+10%** | **−8.3%** | *lever removed* | as above | PRIMARY |
| **Li-ion storage**, 4 h vs 4 h net-peak window | 4 h | 4 h | 5 h | **0%** | −20% | DR, external to the asset | NREL ATB 2024, utility-scale battery storage (4 h default duration) | SECONDARY |
| **Deer mouse**, cold-acclimated ♂, 12 h night | 62.3 kJ (1.683 g) | 61.4 kJ | 61.4 kJ | **+1.5%** | +1.5% | torpor available, **not** engaged | Rezende 2009 Table 1 | DERIVED |
| **Little brown bat**, worst microclimate available | 176 d | 181 d | 181 d | **−2.8%** | −2.8% | hibernation, poor site | Haase 2019 Fig. 3A | PUBLISHED |
| **Human adult**, horizon = 90-d famine | 555 MJ (15 kg) | 630 MJ | 630 MJ | **−12%** | −12% | slow BMR downregulation | **ASSUMED** conventions; ceiling anchored to Stewart & Fleming 1973, *Postgrad. Med. J.* 49:203, `10.1136/pgmj.49.569.203` (382-day fast; **title-level verification only**) | ASSUMED |
| **Little brown bat**, WNS-infected | 131.2 d | 181 d | 181 d | **−27%** | −27% | lever degraded by pathogen | Haase 2019 Fig. 3A | PUBLISHED |
| **Common shrew**, endurance 10 h vs 16 h night | 10 h | 16 h | 16 h | **−38%** | −38% | **NONE** — *Sorex* does not use torpor | Keicher 2017, *JEB* 220:2834, `10.1242/jeb.159947`, Results (5–10 h, after Hanski 1994) | PRIMARY |
| **Common shrew**, endurance 5 h | 5 h | 16 h | 16 h | **−69%** | −69% | none | same | PRIMARY |
| **Common shrew**, all fat gone in 4.2 h | 4.2 h | 16 h | 16 h | **−74%** | −74% | none | same, Discussion — the **authors' inference** from t₅₀ = 2.1 h, not a measurement | PRIMARY |
| **Ruby-throat**, crop only vs normothermic night | 2.65 kJ | 6.81 kJ | 7.64 kJ | **−61%** | −65% | torpor not used in these trials | Eberts 2019 Table 1 — **crop alone; endogenous fat not measured**, so a strict lower bound | PRIMARY |

**Human, horizon = 1 day: +7829%.** Left out of the ordering above because it says nothing about
sizing and everything about horizon — see §4.2.

The lever's own size, for scale: **TMR as % of BMR**, adjusted to 30 g — avian daily heterotherms
**35.3%**, mammalian daily heterotherms **18.8%**, mammalian hibernators **4.3%** (Ruf & Geiser
2015, *Biol. Rev.* 90:891–926, `10.1111/brv.12137`, **Table 2**; the paper's own Results text says
"~40% / ~30% / ~6%" and **does not match its own Table 2** — both are reported here and the
discrepancy is not resolved). Daily torpor buys ~3–5×; hibernation buys ~25×.

---

## 3. The reading

**Biology does consistently carry a margin above the grid's — and the excess is bought back by
the demand-side lever, near-exactly.** Sort the table by margin and the sorting variable is not
taxon, body mass, or horizon; it is whether the metabolic setpoint is movable *and currently
moved*. Every row above the NERC band is an animal exercising a lever (hibernation, torpor,
facultative hypothermia), and every row that falls into or below the band is the *same kind of
animal* with the lever withdrawn, degraded, or unused: the parid goes +57% → +10%, the deer
mouse +265% → +1.5% on cold acclimation, the bat +99% → −2.8% in a bad roost and → −27% under
*Pseudogymnoascus destructans*. The one species with no lever in its repertoire, *Sorex araneus*,
does not merely sit near 15% — it is **structurally unable to reach 0%**, and its ecology is the
consequence: a shrew cannot fast a winter night, so it forages around the clock rather than
sizing a dusk reserve at all. So the answer to "is the 2–4× a blue-tit artifact" is no on both
halves. The magnitude is not an artifact — the parid is in fact the *most conservative* lever-
using animal here, not the least — and the mechanism C33 inferred from a single species by
switching one parameter off replicates as a cross-species pattern with the switch thrown by
nature instead. What does *not* survive is the phrasing "biology is 2–4× the grid": the true
biological range is roughly **−70% to +2400%**, three orders wide, and the grid's 7–26% band is
narrower than any single taxon's. The transferable claim is the one C33 already stated and this
note now has independent support for: **supply-side margin is the wrong place to look; the
adequacy is bought on the demand side.**

---

## 4. Honesty

1. **Horizons differ by four orders of magnitude and are not made commensurable.** The parid,
   hummingbird, mouse and shrew rows are **one night** (11–16 h). The bat rows are **one winter**
   (181 d). The human row is **90 days**. A ratio computed over one night and a ratio computed
   over one winter are the same *arithmetic* and not the same *object*: the long-horizon rows
   integrate over weather that the short-horizon rows treat as a single draw, so the bat's +75%
   already has its bad nights averaged in while the parid's +57% does not. **The ordering in §2
   is therefore not a ranking of conservatism.** It is a ranking of one ratio, and the only
   comparisons this note leans on are *within* a system with the lever on and off — parid,
   deer mouse, bat — where the horizon is held fixed by construction.
2. **The grid's margin is capacity, not energy.** PRM is firm MW over peak MW. Every biological
   row is joules over joules. These are different physical quantities and no conversion between
   them is offered or exists; the grid rows are on this axis **by analogy**, exactly as in C33
   §5.3, and the 4-hour battery row is the only engineered row that is even dimensionally an
   energy-duration statistic. The NERC band is a *design rule* — the margin an area plans to —
   not a realised outcome, so it is the correct object to compare against an optimal-policy model
   and the wrong object to compare against a field measurement.
3. **Fat is not the only reserve.** Glycogen (hours, not days), mobilisable protein, and — in the
   ruby-throat row explicitly — crop-stored sucrose all carry overnight energy. The Eberts row is
   *crop only* and is labelled a lower bound for that reason; its −61% is not a claim that a
   ruby-throat goes to roost in deficit, it is a claim that the crop alone does not cover the
   night. Conversely the rufous row's 1.5 g "above lean mass" is **not all mobilisable lipid**,
   so +354% is an upper bound. Two rows, bounded in opposite directions, and neither is a
   measured dusk *fat* load.
4. **Sample sizes are small and several are single-study.** Bat fat mass N = 46; hummingbird
   respirometry N = 6; Shankar's torpor saving spans 43 individuals of 8 species; the shrew
   endurance figure (5–10 h) is Keicher's *citation of Hanski 1994*, not Keicher's own
   measurement; the shrew's 4.2 h is the authors' own inference from a t₅₀. **No row here is a
   meta-analysis.** The deer mouse row is the strongest in the table precisely because fat mass
   and metabolic rate come from one table on one set of animals.
5. **What the primary sources refused.** Humphries, Thomas & Speakman 2002 (`10.1038/nature00828`,
   Crossref-verified) is paywalled at Nature and its green-OA record is file-restricted; its
   abstract carries no numbers, so **the hibernator row is not built on it** — Haase 2019 and
   Hranac 2021, same species and same model lineage, are used instead and are named as the
   substitution rather than hiding it. Geiser & Ruf 1995 (`10.1086/physzool.68.6.30163788`,
   Crossref-verified) is paywalled; its TMR figures come from the same authors' 2015 update.
   **The great-tit/willow-tit leg failed entirely** — see §6.
6. **Two published typos are silently relied on being typos.** Eberts 2019 Table 1 heads its
   column "kJ" while its own footnote and Results give J; J is used here. Ruf & Geiser 2015's
   Results text and its Table 2 disagree; Table 2 is used here. Both are flagged, neither is
   resolved with the authors.
7. **The human row is `ASSUMED` and load-bearing on nothing.** 70 kg / 15 kg fat / 7 MJ·d⁻¹ are
   conventions this note supplied, not a table it read; the 382-day fast is verified only at
   title level via Crossref, since the PMC scan would not extract. It is in the table as a scale
   check and is excluded from §3's conclusion.

---

## 5. Prediction, and the dataset that tests it

**Prediction.** Across heterothermic birds and mammals, the dusk-or-autumn reserve margin is a
**monotone increasing function of the depth of the available torpor lever**, and species with no
lever do not compensate by carrying a larger supply-side reserve — they pay in mortality instead.
Concretely, with `TMR_rel` = torpid metabolic rate as a fraction of BMR:

- lever-less endotherms (`TMR_rel = 1`) carry margins **at or below 20%**, i.e. inside the NERC
  band, *or* abandon the fasting problem altogether by foraging nocturnally (the shrew route);
- daily heterotherms (`TMR_rel ≈ 0.19–0.35`) carry **+50% to +400%**;
- hibernators (`TMR_rel ≈ 0.043`) carry **+75% and up**;
- and after controlling for body mass and latitude, **overwinter survival should be lower in the
  lever-less group at equal margin** — the margin is not a substitute for the lever.

**The comparative dataset that would test it, named.** Cross **Ruf & Geiser 2015**, *Biol. Rev.*
90:891–926, `10.1111/brv.12137` (Crossref-verified 2026-09-05) — 214 heterothermic species with
`TMR_rel`, `T_b,min` and `TBD_max` per species in one compilation, the modern successor to the
Geiser & Ruf 1995 the brief named — against **ring-recovery adult annual survival estimates from
the EURING/BTO recovery archive** for the passerine species that appear in both. The join key is
species; the covariates are body mass, latitude and a hoarding/non-hoarding flag. **This cross
has not been run here** and naming it is not doing it: Ruf & Geiser's Table 2 is grouped, not
per-species, in the form this note read, and the per-species appendix was not obtained.

**Falsifier, inherited and sharpened from C33.** C33's falsifier was: measured dusk-fat /
overnight-expenditure in wild parids at **0.10–0.20** kills the quantitative leg. This note adds
a second, independent one: **if a lever-less small endotherm is found carrying a margin above
+100%, the mechanism claim fails** — the margin would then be buyable on the supply side after
all, and the demand-side reading of §3 collapses to a correlation. The shrew is the only
lever-less row here and it is a single genus; one counter-example is enough.

---

## 6. What could not be fetched

- **The great tit / willow tit leg — a complete failure, and the largest hole.** Haftorn 1992
  (*Ornis Scand.* 23:435, `10.2307/3676674`), Lehikoinen 1987 (*Ornis Scand.* 18:216,
  `10.2307/3676769` — **DOI verified, exactly as the brief gave it**), Gosler 1996, both
  Bednekoff & Houston 1994 papers, and Houston & McNamara 1993 are all paywalled at JSTOR and
  **none was read**. Haftorn 1989 (*Wilson Bull.* 101:217, no deposited DOI) yielded only the
  diurnal weight amplitude — **9–12% of body mass in great, blue and coal tits, 7–8% in marsh and
  willow tits** (p. 224, Fig. 6) — which is a mass cycle, not a reserve-over-draw ratio, and is
  therefore **not in §2**. The one *Parus major* winter FMR found (66.3 kJ/d) has **n = 2** in an
  un-peer-reviewed preprint and is excluded. **The species C33's falsifier is written against is
  the species this replication could not reach.**
- **Humphries 2002 and Geiser & Ruf 1995** — paywalled; substitutions named in §4.5.
- **Absolute nightly kJ for Shankar's eight hummingbird species** — reported mass-corrected, with
  the table an image in the readable preprint. Only the 82% saving was recoverable.
- **Shrew body fat in grams or percent** — Churchfield 1981 returned 403 on every route, so the
  shrew rows are in *hours*, not joules, and cannot be put in the same unit as the rest.
- **Two citations in the brief were wrong and are corrected here**: "Shankar 2020 *J. Avian Biol.*
  *Hummingbirds budget energy flexibly*" **conflates two papers** — *Hummingbirds budget energy
  flexibly in response to changing resources* is **Funct. Ecol. 33:1904 (2019)**,
  `10.1111/1365-2435.13404`, while the *J. Avian Biol.* 51 (2020) paper is *Hummingbird torpor in
  context*, `10.1111/jav.02305`. "Hiebert 1993 *Physiol. Zool.*" is **The Auk 110:787–797**,
  `10.2307/4088634`. All four Crossref-verified 2026-09-05, `mailto=deciduusleaf@gmail.com`.

See [[C33-lolp-starvation]], [[G34-lolp-starvation-risk]], [[C6-damage-healing-ratio]].
