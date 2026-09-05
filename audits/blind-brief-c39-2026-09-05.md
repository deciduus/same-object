# Blind brief — C39 governance re-code of the Duane-β conservation regions

**Written 2026-09-05, BEFORE opening `vault/computed/C36-conservation-duane.md` or
`vault/_scripts/c36_duane.py`.** The purpose is to turn an after-the-fact consistency
observation ("regions with strong fisheries law seem to have lower β") into a test, by fixing
the coding rule, the region list, and the prediction in advance and hashing the file.

## 1. The coding rule

**Construct:** *formal statutory adaptive-management structure* — a legally binding
instrument (national statute, binding regulation, or a Commission conservation-and-management
measure with binding force on members) that closes the loop assess → trigger → respond.

Score three components, each **0 or 1**, from published governance/legal descriptions only
(statute text, regulation text, Commission basic texts, official programme descriptions).
Total score 0–3.

- **(a) Mandated assessment cycle.** The instrument requires stock assessments / scientific
  advice on a *fixed, recurring* cycle (annual, biennial, or an explicitly stated period) for
  the managed stocks. Score 0 if assessment is discretionary, ad hoc, or merely "as
  appropriate".
- **(b) Rebuilding requirement triggered by an assessment result.** The instrument states an
  objective threshold or status determination (e.g. "overfished", "below B_lim", "outside safe
  biological limits") that *obliges* the manager to adopt a rebuilding/recovery plan. Score 0
  if rebuilding is recommended, aspirational, or left to Commission discretion without a
  triggering criterion.
- **(c) Time-bound management response.** The instrument states a deadline for the response
  (e.g. "within 2 years", "as short a time as possible, not to exceed 10 years", "by 2020").
  Score 0 if no time limit is stated in the binding text.

**Coding discipline.** Each of (a)(b)(c) must be supported by a cited URL to the governing text
or an official description of it. Ambiguity is scored 0 (conservative). Outcome information —
stock status, biomass trends, recovery rates, β — is NOT admissible evidence for any component.

## 2. The ten regions/programmes to be coded

These are management regions/programmes of the kind carried in the RAM Legacy Stock Assessment
Database `region` / `management authority` fields. The list is fixed here in advance; regions
without a β in C36 will simply drop out of the join and that will be reported.

1. US West Coast (PFMC, Magnuson-Stevens Act)
2. US East Coast (NEFMC/MAFMC, Magnuson-Stevens Act)
3. US Southeast & Gulf of Mexico (SAFMC/GMFMC, Magnuson-Stevens Act)
4. US Alaska (NPFMC, Magnuson-Stevens Act)
5. Canada East Coast (Fisheries Act / Sustainable Fisheries Framework)
6. Canada West Coast (Fisheries Act / Sustainable Fisheries Framework)
7. European Union (Common Fisheries Policy, Reg. (EU) 1380/2013, ICES-advised)
8. Mediterranean–Black Sea (GFCM)
9. Indian Ocean (IOTC)
10. Southern Ocean (CCAMLR)

Reserve substitutes, used only if a listed region has no identifiable governing instrument:
Northwest Atlantic (NAFO), Atlantic tunas (ICCAT), New Zealand (Fisheries Act 1996 QMS).

## 3. The prediction

β is the Duane/recovery exponent computed in C36; **lower β = better** (faster/more complete
recovery relative to effort) as used there.

> **PREDICTION.** Regions scoring **3** on the governance rule have β further below 1 than
> regions scoring **≤1**. Operationally: (i) Spearman rank correlation between governance
> score and β is **negative**, and (ii) mean β of the score-3 group is **lower** than mean β of
> the score-≤1 group, with a one-sided permutation test.

**Pre-declared failure conditions.** The prediction FAILS if the Spearman ρ is positive, or if
the score-3 group mean β is not lower than the score-≤1 group mean. It is declared
UNDERPOWERED (direction reported only, no pass/fail claimed) if fewer than 8 coded regions have
a β in C36, or if either comparison group has fewer than 3 members.

No p-value threshold is used as a pass gate; the sign of the effect is the test, and p is
reported for honesty about how easily noise could produce it.

## 4. Order of operations (binding on the coder)

1. This file is written and its sha256 recorded below.
2. All ten regions are coded from governance sources with URLs, and the scores are written into
   `vault/computed/C39-duane-governance-blind.md`.
3. Only then is C36 opened and the join performed.

## sha256 of this file (bytes above this line)

Recorded by `vault/_scripts/c39_blind.py --hash-brief`; see C39 for the value carried forward.

`sha256(first 4615 bytes of this file) = 885ffef666798d784ec67260dbf7573a236e81007b893d6a24e3fa8f3d405d3d`

Recompute: `python vault/_scripts/c39_blind.py --verify-brief` (hashes the file's first
4615 bytes, i.e. everything above this block).
