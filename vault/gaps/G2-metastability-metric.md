---
id: G2
name: G2-metastability-metric
type: gap
standing: narrowed
evidence: full-text-read
contact-surface: 0
crosses: nothing
crosses-rank: 0
topology: disjoint
mediator: 
borrows-from: []
lends-to: []
mutual-with: []
computed-in: []
uses-move: ["[[M6-vary-what-was-held-fixed]]"]
rests-on: []
tags: [node/gap, crosses/nothing, evidence/full-text-read, standing/narrowed]
last-checked: 2026-09-03
note: "Biology-side absence is false: seed ageing uses Arrhenius Ea ~55 kJ/mol and glassy-state trapping. Cross-class axis still missing; MOST work states both variables and cites no other class."
---

# No metastability figure of merit

**STANDING: NARROWED** · evidence: full-text-read · contact surface: 0 · last checked 2026-09-03

> Energetic materials, nuclear isomers, phase-change storage, molecular solar thermal and
> biological dormancy all quantify **stored energy against barrier-set lifetime.** Each has
> both numbers. **None plots against another.**

## One sentence was false and is struck

The note said the barrier vocabulary was "absent from the biology side entirely — 1 hit,
irrelevant." **That is a string artifact**, exactly the failure [[homographs]] and the synonym
trap describe. It anchored on the word *metastability*, which biology does not use, and
measured the word instead of the concept.

Biology uses barrier language, quantitatively.
[PMC6613187](https://pmc.ncbi.nlm.nih.gov/articles/PMC6613187/) (Fleming, Hill & Walters,
*Ann. Bot.* 2019), read in full, computes Arrhenius activation energies for seed ageing:

> "Ea = Arrhenius slope × R, R = 8.314 J mol⁻¹"

**≈55 kJ/mol** for germination loss and **≈57 kJ/mol** for RNA integrity, with P50 lifetimes
from **9.9 ± 0.3 years** (onion) to **51.9 ± 12.4 years** (pea).
[PMC1300301](https://pmc.ncbi.nlm.nih.gov/articles/PMC1300301/) adds the glassy-state half:
rotational activation energy ~25 kJ/mol above T_g against ~10 kJ/mol below it, with τ_R rising
from 10⁻¹¹ s wet to 10⁻⁴ s dry. That is kinetic trapping applied to dormancy, in numbers.

## The core claim survives, and got a sharper witness

No source read put two classes on one axis. The cleanest datum is a **verified negative**:
[PMC5956078](https://pmc.ncbi.nlm.nih.gov/articles/PMC5956078/), a molecular solar thermal
(MOST) photoswitch paper, has both variables in hand — **559 kJ/kg** measured density, **927
kJ/kg** calculated, storage lifetime **up to 48.5 days**, and an explicit stated target of
**>300 kJ/kg** — and compares itself to **no other metastable-storage class at all.** Not
phase-change, not latent heat. Only other photoswitches.

A field that states its own two-variable target and never looks sideways is the gap in one
document.

## A caution the re-read raised: the unification may itself fail

The note's governing arithmetic — lifetime ~ exp(ΔG/kT), so every ~6 kJ/mol buys 10× — is
**the proposed unifying object**, and it may not be universal.

- PCM crystallization is reported **non-Arrhenius** for fast glass formers. (UNVERIFIED —
  snippet only, no full text.) If so, the exponential axis is a linear-response special case.
- The seed numbers already strain it: **Ea ≈ 55 kJ/mol with P50 of decades**, where the rule
  of thumb predicts ~100 kJ/mol for a single year.

The mismatch sits in the **prefactor** — which is precisely the term a single-number figure of
merit would have to fix, and nobody has fixed it. This reframes the gap: the axis may be
missing because it is *hard*, not because it was overlooked. That is a better gap, not a
weaker one. See [[M6-vary-what-was-held-fixed]].

## Evidence, split honestly

The biology sub-claim is now `full-text-read` and **refuted**. The cross-class claim is still
effectively string-protocol: four papers is not a survey, and no full text was obtained on the
nuclear-isomer or PCM sides. All isomer figures are **UNVERIFIED** and none are used here.
