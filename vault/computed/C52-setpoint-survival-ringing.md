---
name: C52-setpoint-survival-ringing
type: computed
exit: prediction
extends-to: [ecology, conservation]
next-step-cost: L
---

# The setpoint→survival test on real `phi` — pre-registered, and it does not run

> **HONEST NULL, and the new leg is the bird leg.** The mammal leg of H1 is **prior art**:
> Turbill, Bieber & Ruf 2011 (`10.1098/rspb.2011.0190`, Crossref-verified, 283 citations)
> already reports that hibernators have **~15% higher annual survival than similar-sized
> non-hibernators** under phylogenetic GLS. That was established **before the outcome was
> fetched** and written into the hashed brief. The only new leg — **torpid vs non-torpid
> birds** — is **structurally unrunnable**: of the 27 British species with BTO ring-recovery
> adult survival, exactly **3** are in the Ruf & Geiser appendix (*Apus apus*, *Caprimulgus
> europaeus*, *Delichon urbicum*) and **all 3 are obligate long-distance migrants**, excluded
> by a rule fixed in advance — so the lever-bearing arm is **n = 0**. **In temperate avifauna
> the metabolic lever and long-distance migration are alternative solutions to the same winter
> energy problem, so any migrant-controlled test of the lever on birds has an empty treatment
> arm.** No `phi` was substituted with longevity. **H1 is NOT TESTED, not supported and not
> refuted.**

Programme item **P-008**, with **P-072** as a rider. Brief:
`audits/blind-brief-c52-2026-09-05.md`,
`sha256 = bc2259e6984a3895a199f3585dc11ffad496162af7a50cb65c79948cac9f2547` over all **14,767**
bytes, written and hashed **before any adult-annual-survival value was fetched**. Verify:
`python _scripts/c52_survival.py --verify-brief`. Arithmetic:
`python _scripts/c52_survival.py` from `vault/`. All fetches **2026-09-05**.

## 1. Which leg is new — decided before the join, not after

The brief's §4 ran the prior-art check **before** any outcome data, precisely because
`audits/c43-adversarial.md` killed C43's mechanism clause on prior art discovered afterwards.

| leg | verdict, fixed in the hashed brief |
|---|---|
| **mammals, hibernation → annual survival** | **REDISCOVERED.** Turbill, Bieber & Ruf 2011, *Proc. R. Soc. B*, `10.1098/rspb.2011.0190` — Crossref 2026-09-05: title, venue, authors Turbill/Bieber/Ruf, issued 2011-03-30, `is-referenced-by-count` = **283**. Abstract via Europe PMC `resultType=core`, PMID 21450735: phylogenetic GLS; monthly survival higher during hibernation; *"Hibernators also have approximately 15 per cent higher annual survival than similar sized non-hibernating species"*. **That is H1.** |
| **birds, torpor → annual survival** | **NEW.** 10 Europe PMC formulations + WebSearch return no comparative test of adult annual survival in torpid vs non-torpid birds. The avian literature is single-species torpor energetics. |
| **cross-taxon (same sign, same magnitude in birds as in mammals?)** | **NEW.** |
| **daily torpor separated from hibernation** | **weakly new** — Turbill's contrast is hibernators vs non-hibernators. Gate not reached here. |

Also recorded before the join: **Geiser & Turbill 2009**, *Naturwissenschaften*
`10.1007/s00114-009-0583-0` (93.5% of 61 recently extinct mammals homeothermic).
**Semantic Scholar `graph/v1/paper/search` returned HTTP 429 on every attempt** — the same rate
limit `c43-adversarial.md`, `g34-adversarial.md` and `g36-adversarial.md` hit. The prior-art leg
is Crossref + Europe PMC + web and **does not meet the C5 §11 bar**. Stated, not hidden.

## 2. The coding rule that fixes C40's worst joint, and what it costs

C40 §5.2 had to amend its lever coding **mid-run, with the longevity column on screen**, because
absence from the Ruf & Geiser appendix is *"not measured"*, not *"no lever"*. Under the strict
rule C40's `p` went from `0.00014` to `0.240`. The brief's §1.1 therefore fixed an **asymmetric**
rule in advance: presence in the appendix alone gives **lever = 1**; **lever = 0** requires an
explicit negative in a second source (COMBINE `hibernation_torpor` = 0); everything else is
**UNCODED and dropped**; conflicts are dropped too.

Frame: COMBINE `trait_data_reported.csv` × PanTHERIA mid-range latitude, orders Chiroptera /
Rodentia / Eulipotyphla, adult mass < 100 g, |lat| ≥ 35°. **n = 671 species.**

| code | n | % |
|---|---:|---:|
| lever = 1 (Ruf & Geiser appendix) | **24** | 3.6 |
| lever = 0 (COMBINE `hibernation_torpor` = 0) | **216** | 32.2 |
| **UNCODED — dropped** | **425** | **63.3** |
| CONFLICT — dropped | 6 | 0.9 |

By order: Chiroptera 9 / 1 / 94 / 1; Rodentia 12 / 151 / 241 / 4; Eulipotyphla 3 / 64 / 90 / 1.
`_scripts/c52_data/lever_codes.csv`,
`sha256 = e6554ce84043db91d1a996d0e54626be8126f31150948bbda68284f76e7be0e2`, written **before**
any `phi` was read.

**The number to quote: a rule that refuses to infer "lever-less" from absence can code only
35.8% of the frame.** C40's 75-species table was reachable only by inferring the other 64%.

## 3. The outcome — `phi` was not obtainable, and longevity was not substituted

Brief §2's source ladder, tried in order:

| # | source | outcome |
|---|---|---|
| 1 | **BTO BirdFacts** per-species survival pages | **WORKED** — real ring-recovery adult annual survival for **27 of 27** slugs requested (`pied-wagtail` returned HTTP 404, recorded). Birds only, Britain only. |
| 2 | EURING / Robinson compilations | no machine-readable open table obtained |
| 3 | **Amniote database**, Myhrvold et al. 2015, `10.1890/15-0846R.1` | **NEGATIVE RESULT, asserted in code**: the 36-column header contains **no field matching `surv`**. There is no `adult_survival` field. |
| 4 | mammal survival compilations (Sibly et al., long-term-studies compendia) | none reachable as open data this run |
| 5 | COMBINE `max_longevity_d` as a downgraded PROXY | **NOT USED.** This is the point of the brief. |

**Brief §2's pre-committed gate — ≥ 10 lever-less species carrying `phi` — is not met for
mammals (n = 0) and not met for birds (n = 0).** Both legs report **DIRECTION ONLY**, and for
both the direction is undefined because an arm is empty.

## 4. The bird leg, and why it is empty

Ruf & Geiser's avian appendix carries **43 species**. Intersected with the 27 BTO species that
publish adult survival: **3** — *Apus apus* (`phi` 0.808), *Caprimulgus europaeus*
(0.700 ± 0.05), *Delichon urbicum* (0.410). **All three are obligate Afro-Palaearctic
migrants and are removed by the brief's §3 (vi) migrant rule. Lever-bearing arm: n = 0.**

The lever-**less** arm is empty for a second, independent reason: the asymmetric rule requires an
explicit negative from a second source, **COMBINE covers mammals only**, and **no avian
compilation states homeothermy per species** — the avian heterothermy literature (McKechnie &
Lovegrove-type reviews) is positive-record, exactly like Ruf & Geiser. So **no bird can be coded
lever = 0 at all** under a rule that refuses to infer absence.

**This is the substantive result of the run, and it is a design fact, not a data shortage.**
Temperate small birds facing a winter energy deficit have two solutions — lower the setpoint, or
leave — and the species that take the first are largely the species that also take the second
(swift, nightjar, house martin, and in the wider appendix the hummingbirds C40 §6.4 already lost
to the same rule). **Any test of the lever on birds that controls for migration removes its own
treatment group.** A design that escapes this must go to resident heterotherms outside Britain —
*Calypte anna*, *Phalaenoptilus nuttallii* — for which no ring-recovery `phi` was found.

## 5. The banned-rules demonstration — VOID BY CONSTRUCTION

C43 died partly on a comparison clause that was a positive control by construction. This run
therefore computes, and labels as **void**, what the same BTO data give under the two moves the
brief forbids: code lever-less by **absence**, and **keep the migrants**.

- Unmatched: lever-bearing n = 3, mean `phi` = **0.639**; lever-less n = 24, mean = **0.493**; **naive Δ`phi` = +0.147**.
- Matched within 2× mass (brief §3 ii), 3 pairs: *Delichon urbicum* 0.410 vs *Emberiza schoeniclus* 0.542 (−0.132); *Apus apus* 0.808 vs *Alauda arvensis* 0.513 (+0.295); *Caprimulgus europaeus* 0.700 vs *Sturnus vulgaris* 0.687 (+0.013).
- **Mean Δ`phi` = +0.059, bootstrap 95% CI [−0.132, +0.295]** (10,000 resamples over pairs, seed 20260905). One-sided sign test **2/3, p = 0.500**. Gate (≥ 8 non-tied pairs): **NOT MET, n = 3.**

**Two things follow.** First, the banned rules do produce a headline-shaped number — `+0.147` —
and it is the *unmatched* one; **the mass matching the brief pre-registered destroys it on its
own**, dropping the effect to `+0.059` with a CI four times its own width. Second, even the
`+0.147` is a positive control: swifts and nightjars are long-lived aerial insectivores because
of flight, roost inaccessibility and predation escape, not because of torpor — the same confound
C40 §6.2 identified for bats, reappearing in birds.

## 6. P-072 — the falsifier, still a formality

**Zero.** Eight Europe PMC formulations run 2026-09-05 (`"fat reserves" AND "overnight" AND
"energy expenditure" AND "small bird"`; `"dusk" AND "fat" AND "overnight energy expenditure"`;
`"body fat" AND "starvation" AND "overnight" AND "passerine"`; `"winter fattening" AND "energy
reserves" AND "survival" AND "shrew"` → 0 hits; `"energy reserves" AND "overnight" AND "vole"`;
`"fat load" AND "overnight fast" AND "bird"`; `"reserve" AND "overwinter" AND "homeothermic" AND
"small mammal"` → 0 hits; `"pre-roost" AND "fat" AND "overnight"` → 0 hits) returned **no new
published dusk-reserve / overnight-cost pair for any lever-less species.**

Lever-less small endotherms with a published margin: **1** (*Sorex araneus*, −69%, Keicher 2017
via C38 §2). Of those above +100%: **0**. **NOT FALSIFIED — over a reach of n = 1.** C40 §5.1
called that a formality rather than a test; **this run tried to widen it and failed, so it is
still a formality.** P-072's own success condition ("a ≥10-candidate scan still zero ⇒ quotable")
is **not met**: the candidate count is 1, not 10.

## 7. Confounds — what each pre-empted control actually returned

| # | control | result |
|---|---|---|
| i | phylogenetic pseudoreplication; family level; with/without Chiroptera | **not reached** — no leg had a runnable arm. The bat problem is untouched. |
| ii | mass matched within 2× | **run, in §5 only.** It removed most of the void effect on its own. |
| iii | latitude \|lat\| ≥ 35°, Δlat ≤ 10° | applied to the mammal frame (§2); not reached on any test |
| iv | flight — legs stratified, never pooled | **honoured**: no bird+mammal number appears anywhere in this note |
| v | source-study clustering | **not reached.** BTO values share one provider; had a leg run, every British `phi` would have been one cluster — a C43-shaped kill waiting for a future run |
| vi | migrant exclusion | **decisive**: removed 3 of 3 lever-bearing birds |
| vii | effect size with CI, not only p | honoured — §5 leads with Δ`phi` and its CI |
| — | positive-control check | `trait_data_imputed.csv` was **not** used; the lever source (Ruf & Geiser HTML) and the `phi` source (BTO HTML) share no provenance |

## 8. Honesty

1. **Nothing here supports C38 §5's survival clause and nothing here refutes it.** The clause remains untested on real `phi`. Anyone quoting C40's `p = 0.00014` should read C40 §6.1 first; this run adds a second reason to discount it — its lever coding covered only ~36% of the frame under a rule that does not infer absence.
2. **The mammal leg was never ours.** Turbill 2011 published it in 2011 with 283 citations. This vault's contribution to the mammal cell is zero, and P-008's framing ("Join the 214-species appendix to EURING/BTO adult φ") did not know that. **P-008 should be rewritten to name Turbill 2011 as its baseline.**
3. **The prior-art reach is bounded.** Semantic Scholar was down (429). Ten Europe PMC formulations plus WebSearch found no avian comparative survival test; that is not proof one does not exist.
4. **The bird `phi` values are one provider, one country, one ringing scheme.** Had the bird leg run, §7 (v) would likely have killed it the way source clustering killed C43. The design escaped that attack only by not producing a result.
5. **The migrant rule is doing enormous work and was fixed in advance.** It is defensible — migration and torpor are not exchangeable — but it is also the entire reason the leg is empty, and a different reviewer could reasonably pre-register a design that stratifies on migration instead of excluding it. **That design is the obvious next run, and it is not this one.**
6. **§5's numbers must never be quoted as a result.** They exist to show what the forbidden rules manufacture. Extracting `+0.147` from this note would reproduce exactly the error the brief was written to prevent.
7. **The blind held.** No `phi` value was fetched before the brief was hashed, and no coding rule was amended after an outcome was seen — the two failures C40 §5.2 and §6.7 disclose. The brief's §7 wrote down, in advance, the suspicion that fewer than three lever-bearing British birds would survive the filters. **It was right, and that is the only prediction this run risked.**

See [[C40-setpoint-survival-test]], [[C38-reserve-margin-across-species]],
[[C33-lolp-starvation]], [[program]].
