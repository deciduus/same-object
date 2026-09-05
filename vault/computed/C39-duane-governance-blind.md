---
name: C39-duane-governance-blind
type: computed
last-checked: 2026-09-05
result: "Blind re-code of fishery governance (3-point statutory adaptive-management rule, coded from statute text before C36 was opened) joined to C36's Crow-AMSAA beta: Spearman rho = -0.709, exact two-sided p = 0.0596, n = 8. Direction as predicted; UNDERPOWERED by the brief's own pre-declared rule (the score<=1 group has n = 2, needed 3)."
exit: computation
extends-to: [conservation]
next-step-cost: M
---

# The governance ordering in C36 §5, re-coded blind

> **RESULT — the direction survives a blind re-code, the test does not.** Ten management
> programmes were scored 0–3 on a statutory adaptive-management rule fixed and sha256-hashed
> *before* [[C36-conservation-duane]] was opened. Eight of the ten have a β. Spearman
> **ρ = −0.709, exact two-sided p = 0.0596** (all 40,320 permutations enumerated); score-3
> mean β **0.841** vs score-≤1 mean β **1.234**, difference **−0.392**, one-sided permutation
> **p = 0.0476** over all 21 splits. **But the brief pre-declared that either group falling
> below 3 members makes the comparison underpowered, and the score-≤1 group has 2 members. So
> the pre-registered verdict is UNDERPOWERED — direction only, no pass claimed.** C36 §5's
> grouping was not an artefact of having seen the βs; it is also not yet a test.

Script: `vault/_scripts/c39_blind.py` (stdlib only). Brief:
`audits/blind-brief-c39-2026-09-05.md`,
`sha256 = 885ffef666798d784ec67260dbf7573a236e81007b893d6a24e3fa8f3d405d3d`
over its first 4,615 bytes; recompute with `python _scripts/c39_blind.py --verify-brief`.

## 1. What was fixed in advance

The brief fixed three things before any outcome was seen: the coding rule, the ten regions, and
the prediction. **Construct:** a binding instrument that closes assess → trigger → respond.
Three components, 0/1 each, coded from legal text only; outcome information (stock status,
biomass, β) inadmissible; ambiguity scored 0.

- **(a)** assessments/advice required on a *fixed recurring cycle*;
- **(b)** a rebuilding obligation *triggered* by an objective status determination;
- **(c)** a *stated deadline* for the response.

The prediction: score-3 regions have β further below 1 than score-≤1 regions, tested as a
negative Spearman ρ plus a lower score-3 group mean. Pre-declared failure: ρ positive, or the
score-3 mean not lower. Pre-declared underpowering: fewer than 8 joined regions, **or either
group with fewer than 3 members**.

## 2. The coding table (governance sources only)

| Region / programme | instrument | a | b | c | **score** | key evidence |
|---|---|:-:|:-:|:-:|:-:|---|
| US West Coast (PFMC) | Magnuson-Stevens Act, 16 U.S.C. §1854(e) | 1 | 1 | 1 | **3** | §1854(e)(1) annual report to Congress identifying overfished stocks; (e)(3) Council "shall prepare and implement" a plan **within two years** of notification; (e)(4) rebuilding "not exceed 10 years" |
| US East Coast (NEFMC/MAFMC) | same | 1 | 1 | 1 | **3** | same statute |
| US Southeast & Gulf (SAFMC/GMFMC) | same | 1 | 1 | 1 | **3** | same statute |
| US Alaska (NPFMC) | same | 1 | 1 | 1 | **3** | same statute |
| European Union | Reg. (EU) 1380/2013 (CFP) | 1 | 1 | 1 | **3** | Art. 6(2) measures on scientific advice incl. STECF; Art. 16(4) TACs fixed annually in accordance with the plan; Art. 10(1)(g) safeguards and **remedial action** tied to plan targets and reference points; Art. 2(2) MSY exploitation rate **by 2015, at the latest 2020** |
| Canada East Coast | Fisheries Act ss. 6.1–6.2 + Fishery (General) Regs Sch. IX | 0 | 1 | 1 | **2** | rebuilding plan obliged when a prescribed major stock is at or below its LRP, **within 24 months** (extendable by 12); no fixed statutory assessment cycle → (a)=0 |
| Canada West Coast | same | 0 | 1 | 1 | **2** | same |
| Mediterranean–Black Sea | GFCM binding recommendations / multiannual plans | 0 | 0 | 1 | **1** | plans are binding recommendations with dated phases (transitional ~3 yr, long-term ~5 yr) → (c)=1; no binding fixed assessment cycle and no threshold-triggered rebuilding obligation in the binding text → (a)(b)=0 |
| Indian Ocean (IOTC) | IOTC Res. 15/10, 21/01 | 0 | 0 | 0 | **0** | 15/10 sets B_lim = 0.2·B0 and a decision *framework*, but HCR adoption and assessment scheduling remain Commission/SC discretion; rebuilding plans (e.g. yellowfin) adopted ad hoc, no general trigger, no stated response deadline |
| Southern Ocean (CCAMLR) | CM 21-01/21-02 + annual catch-limit measures | 1 | 0 | 0 | **1** | catch limits and decision rules (depletion probability, 50–60% escapement over 35 yr) reviewed each season → (a)=1; no threshold-triggered rebuilding obligation, no deadline → (b)(c)=0 |

Sources, fetched 2026-09-05: 16 U.S.C. §1854 <https://www.law.cornell.edu/uscode/text/16/1854>;
50 CFR 600.310 <https://www.law.cornell.edu/cfr/text/50/600.310>; NOAA MSA overview
<https://www.fisheries.noaa.gov/topic/laws-policies/magnuson-stevens-act>; Reg. (EU) 1380/2013
<https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32013R1380>; DFO fish-stocks
provisions guidelines
<https://www.dfo-mpo.gc.ca/reports-rapports/regs/sff-cpd/guidelines-lignes-directrices-eng.htm>
and Canada Gazette II 156(8) SOR/2022-73
<https://gazette.gc.ca/rp-pr/p2/2022/2022-04-13/html/sor-dors73-eng.html>; GFCM management plans
<https://www.fao.org/gfcm/activities/fisheries/management-measures/management-plans/en/>; IOTC
Res. 15/10
<https://iotc.org/cmm/resolution-1510-target-and-limit-reference-points-and-decision-framework>
and the active-CMM compendium
<https://iotc.org/sites/default/files/documents/compliance/cmm/IOTC_-_Compendium_of_ACTIVE_CMMs_01_January_2026.pdf>;
CCAMLR conservation measures
<https://www.ccamlr.org/en/conservation-and-management/conservation-measures>.

## 3. The join

β is C36 §3, balanced 1990–2015 panel, failure = `U/Umsy > 1`. Two coded regions (Canada West
Coast, Southern Ocean) have no row in C36 and drop out — they were listed in the brief and are
reported dropped, not swapped.

| Region | score | β |
|---|:-:|---|
| US West Coast | 3 | 0.672 |
| US East Coast | 3 | 0.815 |
| US Southeast & Gulf | 3 | 0.861 |
| Canada East Coast | 2 | 0.881 |
| European Union | 3 | 0.916 |
| US Alaska | 3 | 0.942 |
| Mediterranean–Black Sea | 1 | 1.105 |
| Indian Ocean | 0 | 1.362 |
| Canada West Coast | 2 | — (not in C36) |
| Southern Ocean (CCAMLR) | 1 | — (not in C36) |

## 4. The statistic

```
n = 8
Spearman rho              = -0.7092
exact two-sided p         =  0.0596   (all 8! = 40,320 relabelings enumerated)
score 3   n=5  mean beta  =  0.841
score <=1 n=2  mean beta  =  1.234
difference of means       = -0.3923
one-sided permutation p   =  0.0476   (all C(7,5) = 21 splits enumerated)
```

The p-values are exact enumerations, not normal approximations — at n = 8 the asymptotic
Spearman p would be meaningless.

**Verdict against the pre-declared rule.** ρ is negative and the score-3 mean is lower, so the
*direction* passes both clauses. But the score-≤1 group has **2** members against the
pre-declared minimum of 3. **The brief says that is UNDERPOWERED and that only the direction may
be reported. That is the verdict: DIRECTION CONFIRMED, TEST UNDERPOWERED — not a pass.** With
only three distinct scores among 8 points, the smallest attainable two-sided Spearman p is
bounded well away from anything decisive; 0.0596 is near the floor this design can reach.

Reporting it as a pass would be exactly the move the exercise was built to prevent.

## 5. Honesty

**The coder is an AI with prior knowledge of which regions did well.** This is the deepest
problem and hashing the brief does not fix it. I knew before writing a line that US federal
fisheries are the standard success story and the Mediterranean the standard failure; that
knowledge could have steered which three components the rule uses and how ambiguity was
resolved. The hash proves the rule preceded *reading C36*, not that it preceded *knowing the
answer*. Worse, the orchestrating instruction that commissioned this work quoted six of C36's β
values in its own text, so those numbers were in view before the brief was written — **the blind
is broken at the source**, and only the *coding* (which region gets which 0/1) was done from
legal text without consulting the table. What would fix it: a human coder who has not seen C36,
or a pre-registered external index.

**Governance descriptions are outcomes-adjacent.** A statute is not independent of the fishery it
governs: the Sustainable Fisheries Act 1996 rebuilding mandate was *written because* US stocks
had collapsed, and the CFP's 2020 MSY deadline was written because EU stocks had. Formal
structure is partly a response to past failure, so score and β can share a cause with no causal
arrow between them. The rule cannot separate "law caused recovery" from "collapse caused law".

**n = 8, three distinct scores, and one instrument doing most of the work.** Five of the eight
joined regions share a single statute (MSA), so the effective sample is closer to four
independent governance regimes than eight. The score-≤1 group is two rows. Nothing here would
survive a demand for independence of observations.

**The external index was checked and is not usable as coded.** Melnychuk, Peterson, Elliott &
Hilborn, *Fisheries management impacts on target species status*, PNAS 114(1) 178–183,
**DOI [10.1073/pnas.1609915114](https://doi.org/10.1073/pnas.1609915114) — verified at Crossref,
2026-09-05** (its title is not "Fisheries Management Index"; the FMI is the index constructed in
that programme of work). Its per-region/per-fishery FMI attribute scores were **not obtainable in
this session**: `pnas.org` returns HTTP 403 to the fetcher and no open per-region score table was
located. So the second, external code was **not** run and only the AI code is reported. Obtaining
the FMI scores — from the PNAS SI, from the authors, or from the 2023 *Fish and Fisheries*
state-fisheries release — and re-running §4 against them is the single cheapest thing that would
convert this from a direction into a test.

**What would count as falsification, restated.** A blind human or FMI-based coding of ≥10
programmes with ≥3 per group in which ρ ≥ 0, or in which the score-3 mean β is not below the
score-≤1 mean. [[C36-conservation-duane]] §5 stands where it stood: consistent, and still not
tested.
