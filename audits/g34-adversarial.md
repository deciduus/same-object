# G34 adversarial review

Run 2026-09-05. Target: [[G34-lolp-starvation-risk]] and [[C33-lolp-starvation]]. Brief: kill it
if it can be killed. Instruments available this session: WebSearch, Europe PMC REST search,
Europe PMC full text (Brodin et al. 2017, `PMC5596050`). **Semantic Scholar
`graph/v1/paper/search` returned HTTP 429 on every attempt** (12 queries, two passes with 2 s and
8 s backoff) and **OpenAlex returned `Rate limit exceeded / Insufficient budget, resets at
midnight UTC`** on the first call — the daily budget was already spent by a parallel agent. The
prior-art leg below is therefore **WebSearch + Europe PMC only**, which is one instrument short
of the C5 §11 standard it was asked to match. Stated, not hidden.

---

## Verdict

**NARROW — grade REPACKAGED.** The analogy is not prior art (attack 1 clean, no source states
it), but two load-bearing claims are false as written: **(a) LOLE is not a first-passage
functional** — the grid's zero boundary is *not* absorbing, so the estimand on the grid side is
an expected occupation count and on the bird side a hitting probability (attack 3, fatal to the
note's title); and **(b) the citation-intersection anchors are the classic-LOLP literature that
G34's own scope paragraph excludes** (attack 2). Two further numerical faults: **C33's forward
simulation runs a policy the paper does not report as optimal and overshoots the paper's own
stated daily fat gain by 2.3×** (attack 4a), and **the `+57%` reserve margin is an energy ratio
compared against a capacity ratio** (attack 4b). The structural correspondence at the level of
the *state equation* survives; the headline numbers do not.

---

## Attacks

### 1. Prior art on the analogy — **FAILS TO KILL (G34 is not REDISCOVERED)**

Europe PMC, `https://www.ebi.ac.uk/europepmc/webservices/rest/search`, `format=json`,
**2026-09-05**. Queries are the exact strings sent.

**Syntax calibration first, and it caught a fake zero.** The first pass used
`FULL_TEXT:"..." AND FULL_TEXT:"..."`. Every one of ten queries returned **0** — including
`FULL_TEXT:"fat reserves"` alone, which cannot be zero. **The `FULL_TEXT:` field prefix is not
honoured by this endpoint and silently returns 0 for everything** (failure-modes mode 1: a
punctuation/field artifact, not a synonym problem). All ten were re-run bare-quoted. The
calibration controls below fire, so the zeros that follow are real.

| # | Query (verbatim) | Hits | Read of the hits |
|---|---|---|---|
| C1 | `"fat reserves"` | **3,992** | calibration — bird/ecology side findable |
| C2 | `"loss of load probability"` | **63** | calibration — grid side findable |
| C3 | `"resource adequacy" AND "foraging"` | **1** | calibration — the AND operator works |
| 1 | `"loss of load probability" AND "fat reserves"` | **0** | — |
| 2 | `"loss of load" AND "starvation risk"` | **0** | — |
| 3 | `"reserve margin" AND "fat reserves"` | **0** | — |
| 4 | `"loss of load expectation" AND "foraging"` | **3** | all metaheuristic sizing papers (honey badger algorithm; storage optimisation reviews). *"Foraging"* is the optimiser's name, not an animal. **Word-level only.** |
| 5 | `"value of lost load" AND "starvation"` | **0** | — |
| 6 | `"planning reserve margin" AND "animal"` | **1** | *Critical Risk Indicators for the electric power grid* (2021) — "animal" is a physical-contact outage cause. Homograph. |
| 7 | `"torpor" AND "demand response"` | **0** | — |
| 8 | `"loss of load probability" AND "bird"` | **8** | **all eight are bio-inspired *metaheuristics*** — black-winged kite algorithm, honey badger algorithm, graph-theoretic solar interconnection. Optimiser names, zero biological content. |
| 9 | `"loss of load probability" AND "ecology"` | **1** | stand-alone PV/wind sizing review; "ecology" in a boilerplate sustainability sentence. |
| 10 | `"hibernation" AND "energy storage sizing"` | **0** | — |
| 11 | `"gambler's ruin" AND "fat reserves"` | **0** | — |
| 12 | `"ruin probability" AND "starvation"` | **0** | — |

WebSearch, 2026-09-05, four formulations: `"loss of load probability" "starvation" bird "fat
reserve" analogy`; `"reserve margin" analogy "fat reserves" animal power system reliability
bio-inspired`; `"stochastic dynamic programming" "energy reserves" birds "state of charge"
battery storage same formalism`; `ecology-inspired resource adequacy "first passage" reserve
depletion probability grid biology same mathematics`. Every one returns the two literatures
**separately** and nothing joining them. The nearest miss is
[*Asymptotic Analysis of First Passage Time Problems Inspired by Ecology*](https://link.springer.com/article/10.1007/s11538-014-0053-5)
(Bull. Math. Biol. 2014) — first-passage, ecology, but predator search in a 2-D landscape, no
grid content.

**Outcome.** The prediction in the brief — that bio-inspired power systems would turn out to be
swarm/metaheuristic and not this mapping — is **confirmed literally and by name**: the eight
`"loss of load probability" AND "bird"` hits are algorithms named after birds. **No source
states the reserve-margin↔fat or LOLP↔starvation identity.** G34 is not REDISCOVERED and is not
merely LOCATED at word level either. **This attack fails; the analogy is the note's own.**
Caveat carried: this rests on one full-text index (Europe PMC, biomedical-skewed, thin on IEEE
power engineering) plus WebSearch. An IEEE-side full-text sweep and a working Semantic Scholar
key are still owed.

### 2. Metaphor test — the anchors are the wrong literature. **HIT**

Billinton & Allan's LOLP is confirmed static: *"The LOLP is obtained by combining each capacity
part's availability with the load duration curve"* — a capacity-outage probability table
convolved against a load-duration curve
([ScienceDirect topic page](https://www.sciencedirect.com/topics/engineering/loss-of-load-probability);
[Wikipedia, *Loss of load*](https://en.wikipedia.org/wiki/Loss_of_load); WebSearch 2026-09-05).
**There is no integrated state, no reserve trajectory, and therefore no first-passage problem in
the anchor.**

Both notes already concede this in prose — G34 *"What survives"* and scout-06's own
metaphor-risk paragraph both say the comparison must be to **storage-constrained adequacy**, not
to classic LOLP. **The defect is that the concession was never carried into the measurement.**
All four cross-domain pairings in G34's provenance table are anchored on **Billinton & Allan
1996** and **Billinton & Li 1994** — i.e. on exactly the classic-convolution canon the note says
is out of scope. The measured zero is a true zero **about a literature the note disclaims**.

The correct grid anchor for the claimed scope is the storage-adequacy / ELCC-of-storage lineage —
**Denholm & Hand 2011** is the obvious one, and the project has already measured it: scout-06
candidate **#3** reports Denholm & Hand 2011 × Houston & McNamara 1993, `N_A` 794, `N_B` 196,
**∩ = 0**. That measurement, not the Billinton ones, is the evidence G34's scope actually needs,
and it is not in G34's table.

**Outcome.** Not fatal to the gap — the right-anchor zero exists — but G34's evidence table does
not measure what G34 claims. Fix by promoting candidate #3 to a fifth row and demoting the
Billinton rows to "classic-scope control, out of claimed scope".

### 3. Units, horizons, absorbing boundary — **HIT, and this one reaches the title**

C33 §1 writes one recursion with *"0 absorbing"* and asserts *"Same functional equation, same
absorbing boundary, same backward sweep — only the aggregation differs, and the aggregation is a
reporting convention."* **The last clause is false, and it is false in the direction that matters.**

- For the bird, 0 **is** absorbing. `P(starve) = 1 − S(x₀,0)` is a **first-passage probability**:
  the probability the process ever hits 0.
- For the grid, 0 is **not** absorbing. Load is shed, the shortfall ends, storage recharges, and
  the process continues. `LOLE = Σ_t P(x(t) ≤ 0)·Δt` is an **expected occupation time** — a
  functional of the *stationary* (or cyclo-stationary) law of a reflected/non-absorbing process,
  which counts repeated crossings.

First-passage probability and expected occupation time are **different functionals of the same
process**, and they diverge exactly where the risk is interesting: a system that dips below zero
ten times for one hour each has LOLE 10 h and, run as an absorbing problem, would have died at
the first dip. So:

- **G34's title — *"are the same first-passage problem"* — is wrong for the grid side.** LOLE is
  not a first-passage quantity, under classic *or* storage-constrained scoping. What the two
  fields genuinely share is the **state recursion** and the **shadow price**, not the estimand.
- **The two-way table in C33 §3 is a conversion between non-commensurable functionals**, not a
  unit conversion. "Hours of lost load" and "nights of death" are not the same object, and the
  8-hour charge does not make them one. C33 §5.2 calls the 8 h an assumption and §5.5 concedes
  "terminal vs restorable" — but §3 then prints table B as a result anyway, and §5.5 treats the
  Ireland saturation as a curiosity rather than as the symptom it is. **The mapping saturates
  for Ireland because the functionals differ, not because the number is large.**

**Outcome.** Table B (grid → bird) should be withdrawn as a result and retained only as an
illustration with the non-commensurability stated in-table. Table A (bird → grid) survives only
if relabelled: the bird's number is a first-passage probability and its "LOLE" is a *notional*
LOLE for a system that is switched off at the first shortfall — a lower bound on the LOLE of the
same process run non-absorbing.

### 4. The reserve-margin number — **TWO HITS**

Full text of Brodin, Nilsson & Nord 2017 fetched from Europe PMC `PMC5596050/fullTextXML`,
2026-09-05, 186,809 bytes, and grepped.

**4a. The simulated policy is not the paper's optimal policy, and the budget does not
reconcile. (fatal to §3's headline)**

C33 §3 says `P(starve)` was computed *"under the policy the paper reports as optimal under
almost all conditions — forage intensively every daylight period, maximum hypothermia every
night"*. **The paper attaches "under almost all conditions" to hypothermia only**, verbatim:
*"Under almost all conditions (except for a narrow window when 1.22 < ∆ < 1.25), the birds
should always enter maximum hypothermia at dusk"*. On foraging it says the opposite of what C33
assumed: *"After noon … as the probability that the birds will reach the optimal fat level at
dusk increases, they will start to use the second foraging strategy, cautious foraging with less
gain (behaviour 2). Depending on the foraging success in the afternoon, the birds will switch
between behaviours 1 and 2."* Table 1 gives behaviour 2 as **α = 60 kJ**, not 80.

The arithmetic check is decisive. The paper states its own outcome: **"The total fat gain over
the whole day will be 0.74 g"**. At the model's own 37 kJ/g (`X_max` 148 kJ = 4 g) that is
**27.4 kJ of net daily fat gain**. C33 §2's derived budget gives realised gain 76.80 kJ minus
daylight cost 15.0 kJ = **61.8 kJ = 1.67 g**. **C33's simulated bird gains 2.3× more fat per day
than the paper's own reported trajectory.** A starvation probability of `8.25 × 10⁻⁸` is what
you get from a bird with 2.3× the paper's daily surplus, which is why it lands five orders of
magnitude from any grid criterion. The five-decade headline is substantially an artifact of the
wrong policy.

**4b. The warm-up cost was silently set to zero, and it is the paper's own alternative
treatment.** Table 2 gives `C_WU` = *"Extra warming up cost hypothermic birds, **0 or 6 kJ**"* —
two treatments, both reported (Fig. 3a, dashed vs solid). C33 §2's parameter table omits `C_WU`
entirely and its overnight draw `45 × 16/24 × 0.7 = 21.0 kJ` is the `C_WU = 0` branch. The
paper's other branch is explicit about the consequence: *"If there is such a cost, the birds
would carry 0.1 g extra fat already at dusk to buffer for this expense."* Charging the 6 kJ makes
the hypothermic night ≈ **27.0 kJ** against a normothermic 30.0 kJ — **the hypothermia lever
saves 3 kJ, not 9.** The §4 demand-side story collapses from *57% → 10%* (a 47-point lever) to
*≈22% → 10%* (a 12-point lever). The undisclosed choice is the one that maximises the headline.

Independent corroboration: in a stabilised cycle the night's draw must equal the day's gain, and
the paper's own 0.74 g/day puts the overnight draw at **≈27.4 kJ** — within 2% of the
warm-up-inclusive figure and 30% above C33's 21.0 kJ.

**What holds.** `x_start = 12 kJ` **is** defensible as a dawn reserve: the paper says the forward
iteration simulated *"1000 birds with a morning body mass of 11.2 g on day 1 (which was the
preferred level when the iteration had stabilized after a few days)"*. C33 §5.7's description is
accurate. Note also that the margin is algebraically just `x_start / R` — 12/21 = 57.1% — so the
whole prediction is one ratio of two model parameters, and it moves to **12/27.4 = +43.8%** on
the paper's own budget.

**4c. Capacity vs energy — the comparator is wrong.** Planning reserve margin is
`(firm capacity − peak load)/peak load`, **MW/MW**, evaluated at a single annual instant. The
bird's `(x_dusk − R)/R` is **kJ/kJ**, evaluated over a 16-hour integral. Both are dimensionless;
they are not the same dimensionless number, and the 15–20% convention was never a statement
about energy. The like-for-like grid quantity for an energy-limited resource is the **energy
margin over the critical period**: stored energy at the start of the net-peak window divided by
the energy discharged across it, i.e. residual state-of-charge at the end of the critical period
as a fraction of the critical-period energy. For the 4-hour lithium fleets that dominate current
storage adequacy accreditation, sized to a 4-hour net peak, that ratio is **≈0–0.25**. Against
that comparator the bird's 0.44–0.57 is roughly **2×**, not "two to four times the 15–20%
convention" — and the sentence should not name PRM at all.

### 5. Cherry-pick check — **PARTIAL HIT**

Not a species cherry-pick: *"Our model animal is, thus, a non-hoarding parid with a body mass of
10–13 g, such as a blue tit"* is the paper's own label, so C33 reports it correctly. Three
qualifications the notes should carry:

- **The parameters are willow-tit data, not blue-tit data**: *"The parameter values are taken
  from data on willow tits (Tables 1, 2)"*, and the paper flags the mismatch itself — *"We are
  aware that blue tits may not be as cold-adapted as, for example, a willow tit."*
- **The willow tit is a large-scale hoarder** and the model deliberately drops caching: *"we did
  not include food-storing in our model."* Caches are a second reserve. A hoarding parid's true
  adequacy margin is larger than any fat-only number, in a way the fat-only formalism cannot see
  — the bird has an off-book resource, and the grid analogue (contracted firm imports) is exactly
  the thing PRM accounting fights about.
- **The "species with no hypothermia" row is not a species.** C33 §4's normothermic rows (+10%,
  −8.3%) are a counterfactual *inside one parameterisation* — the same `x_dusk = 33.0 kJ` with
  `ε` switched off. That is not evidence about a bird that does not use hypothermia; such a bird
  would re-optimise `x_dusk` upward, which is what the DP is for. **C33's own falsifier asks for a
  cross-species comparison and C33's table does not supply one.** Re-running the DP with `ε = 0`
  is a few lines and would supply it; until then the demand-side claim is untested even
  in-model.

### 6. Direction of borrowing — **HIT**

Demand response counted as capacity toward resource adequacy is **standard, mature grid
practice**, not a transfer from biology. WebSearch 2026-09-05: MISO's own
[*Demand Response 101*](https://cdn.misoenergy.org/20240510%20Demand%20Response%20101%20Workshop%20Presentation632828.pdf)
workshop; CRS [*PJM's Electric Capacity Market*](https://www.congress.gov/crs-product/R48553)
(demand-side resources bid into the capacity auction); the term **"negawatt"** for demand
reduction as negative capacity dates to Lovins 1989–90. Resource adequacy is routinely defined
*"inclusive of the capability to reduce customer load through demand response"*.

So C33 §4's headline sentence — *"it buys most of its adequacy on the demand side"* — is **a
grid concept applied to a bird**. The borrowing runs **grid → bird**, and the note frames it as
"the transferable claim", i.e. bird → grid. What is genuinely new in that sentence is not the
concept but the **quantity**: nobody has published the demand-side share of an animal's adequacy
margin. That is the claim worth keeping, and it is smaller than the one written — and, per
attack 4b, currently mis-sized.

---

## Proposed edits to G34 and C33

Text only. **Not applied.** Also mirrored in `vault/PENDING-log-G34ADV.md`.

### G34 — title and thesis

Replace the H1 `# Loss-of-load probability and starvation risk are the same first-passage
problem` with:

> `# Loss-of-load probability and starvation risk are the same reserve recursion, read out by different functionals`

Replace, in the blockquote, `Power-system reliability engineering asks *what is the probability
that a stored reserve hits zero before the horizon ends, given stochastic income and a stochastic
draw* and calls the answer **loss-of-load probability**.` with:

> Power-system reliability engineering propagates a stored reserve under stochastic income and a
> stochastic draw and reports **how much time the reserve spends at or below zero** — loss-of-load
> probability and its aggregate, loss-of-load expectation. Behavioural ecology propagates the same
> state under the same drivers and reports **whether an overwintering bird's fat reserve ever
> reaches zero** — starvation probability. **The state recursion is shared and the shadow price is
> shared; the estimand is not.** The grid's zero is a reflecting boundary and its statistic is an
> expected occupation time; the bird's zero is absorbing and its statistic is a first-passage
> probability.

### G34 — frontmatter and evidence table

Replace the frontmatter `note:` first sentence with:

> `note: "Power-system adequacy and small-bird winter energetics propagate the same stochastic reserve recursion by backward SDP and read the same shadow price off the value function, but aggregate it into different functionals (occupation time vs first passage). Storage-constrained anchor pairing (Denholm & Hand 2011 x Houston & McNamara 1993) intersection 0 at 794 x 196; classic-LOLP anchors also 0 but are out of the claimed scope; same-side controls 25.2% and 12.8% of the smaller set."`

Add a fifth row to the provenance table, and relabel the four Billinton rows. Add after the
table:

> **Anchor scope, stated against this note's own restriction.** The four Billinton pairings above
> measure the **classic-LOLP** literature, which *"What survives"* below explicitly places outside
> this note's scope. They are retained as an out-of-scope control. **The in-scope measurement is
> the storage-constrained pairing, Denholm & Hand 2011 × Houston & McNamara 1993, `N_A` 794,
> `N_B` 196, ∩ = 0** (`audits/scout-06-energy-systems.md` candidate #3, OpenCitations 2026-09-05).
> Until that pairing is re-run inside this note with its own decade bins, the in-scope zero is
> imported, not measured here.

### G34 — "What survives"

Append:

> **A second scope restriction, from `audits/g34-adversarial.md`.** Even under storage-constrained
> scoping, **LOLE is not a first-passage quantity**: unserved load is shed and the reserve
> recovers, so the grid's zero is not absorbing and LOLE counts repeated crossings. The bird's
> `P(starve)` is a first-passage probability on an absorbing boundary. **What the two fields share
> is the state recursion and the shadow price, not the estimand.** The claim is corrected to that,
> and the word "first-passage" is removed from the grid side throughout.

### C33 — §1, the false clause

Replace `Same functional equation, same absorbing boundary, same backward sweep — only the
aggregation differs, and the aggregation is a reporting convention.` with:

> Same state recursion, same backward sweep — **and there the identity stops.** The bird's zero is
> absorbing and `P(starve)` is a first-passage probability. **The grid's zero is not absorbing**:
> load is shed, the shortfall ends, and storage recharges, so `LOLE` is an expected **occupation
> time** of a non-absorbing process, counting repeated crossings. First-passage probability and
> expected occupation time are different functionals of the same process and they diverge exactly
> where the risk is interesting — a system that dips below zero ten times for an hour each has
> LOLE 10 h and would have died at the first dip. **The aggregation is not a reporting
> convention; it is the difference between the two estimands.**

Replace the `0 absorbing` annotation on the displayed recursion with `0 absorbing on the bird
side only; reflecting on the grid side`.

### C33 — §2, the missing parameter and the wrong policy

Add a row to the §2 parameter table:

> `| C_WU | extra warming-up cost, hypothermic bird | **0 or 6 kJ** — the paper reports both | Table 2, Eq. 10 |`

Replace the derived-budget sentence `Overnight draw \`45 × 16/24 × 0.7\` = **21.0 kJ**
hypothermic (25.2 cold)` with:

> Overnight draw, `C_WU = 0`: `45 × 16/24 × 0.7` = **21.0 kJ** hypothermic (25.2 cold). **With the
> paper's other treatment, `C_WU = 6 kJ`: 27.0 kJ hypothermic (31.2 cold)** — against 30.0 kJ
> normothermic, so the hypothermia lever saves **3 kJ, not 9**. **The paper's own stabilised cycle
> independently puts the overnight draw at ≈27.4 kJ**: it reports a total daily fat gain of
> **0.74 g**, which at the model's 37 kJ/g is 27.4 kJ, and in a stabilised cycle the night's draw
> equals the day's gain. **Every number below that uses 21.0 kJ is the low-draw branch, and it is
> the branch that flatters this note.**

### C33 — §3, the policy correction

Replace `under the policy the paper reports as optimal under almost all conditions — forage
intensively every daylight period, maximum hypothermia every night` with:

> under **maximum foraging** — forage intensively every daylight period, maximum hypothermia every
> night. **This is not the paper's optimal policy and the note previously mis-described it as
> such.** The paper's "under almost all conditions" qualifier attaches to hypothermia alone; on
> foraging it reports the bird switching to cautious foraging (behaviour 2, α = 60 kJ) after noon
> once dusk fat is within reach. **The consequence is measurable: this note's budget gives 61.8 kJ
> (1.67 g) of net daily fat gain against the paper's own reported 0.74 g — a 2.3× overshoot. The
> `8.25 × 10⁻⁸` is therefore an upper bound on safety, and the five-decade separation in §3 is
> substantially an artifact of the policy, not a property of the bird.** Re-running under the
> mixed behaviour-1/behaviour-2 policy is the outstanding fix.

### C33 — §3, table B

Retitle `### B. Grid criterion → bird units` to:

> `### B. Grid criterion → bird units — illustrative only, not a result`

and prepend:

> **This direction converts an expected occupation time into a first-passage probability, and
> those are different functionals (§1).** The saturation for Ireland is the symptom, not a
> curiosity. The table is retained to show the scale, and **no claim in this note rests on it.**

### C33 — §4, the comparator and the headline

Replace `roughly **two to four times** the 15–20% grid convention (ESIG 2024: WECC-CAMX PRM ≥
15%, mainland Spain ≥ 10%)` with:

> **and the grid's planning reserve margin is the wrong comparator for it.** PRM is
> `(firm capacity − peak load)/peak load`, **MW/MW at a single annual instant**; the bird's ratio
> is **kJ/kJ over a 16-hour integral**. Both are dimensionless and they are not the same
> dimensionless number. **The like-for-like quantity is the energy margin over the critical
> period** — stored energy entering the net-peak window over the energy discharged across it,
> equivalently residual state of charge at the end of the critical period as a fraction of that
> period's energy. For the 4-hour storage fleets that dominate current accreditation, sized to a
> 4-hour net peak, that margin is **≈0–0.25**. On the paper's own budget the bird's margin is
> `12 / 27.4` = **+43.8%** on a typical night (not +57.1%). **The honest statement is: ≈0.44
> against ≈0–0.25, roughly 2×** — and PRM should not be named.

Replace `**The bird meets a far stricter adequacy standard than any grid while carrying a
supply-side margin that is only modestly larger, because it buys most of its adequacy on the
demand side.** That is the transferable claim.` with:

> **The demand-side reading is the grid's own, not a transfer from the bird.** Demand response
> counted as capacity toward resource adequacy is mature grid practice — MISO's *Demand Response
> 101* (2024), PJM's capacity auction, and "negawatt" as a term since Lovins 1989. **The borrowing
> here runs grid → bird.** What is new is not the concept but the **quantity**: no published
> figure exists for the demand-side share of an animal's adequacy margin. **On the low-draw branch
> that share is large (57% → 10% when hypothermia is removed); on the paper's own budget, with the
> 6 kJ warming cost charged, it is 22% → 10% — a 12-point lever, not a 47-point one.** The claim
> is the existence and rough size of the quantity, and its size is currently uncertain by a factor
> of four.

### C33 — §4, the falsifier

Append:

> **The second falsifier is not yet tested even in-model.** The normothermic rows above are a
> counterfactual inside one parameterisation — `x_dusk` held at its `ε = 30%` optimum with `ε`
> switched off. A bird that genuinely cannot use hypothermia would **re-optimise `x_dusk` upward**,
> which is what the DP exists to compute. Re-running Brodin's DP at `ε = 0` and reading the new
> optimal dusk reserve is a small job and is the minimum before the demand-side mechanism is
> claimed.

### C33 — §5, two new honesty items

> 8. **Species label vs parameter source.** The paper labels its animal a non-hoarding parid,
>    "such as a blue tit", but states that **"the parameter values are taken from data on willow
>    tits"** and flags that blue tits "may not be as cold-adapted". The willow tit is additionally
>    **a large-scale hoarder**, and the model deliberately excludes caching. A cache is a second
>    reserve invisible to a fat-only formalism, so the margins here are a **lower bound** for any
>    hoarding species — and the grid analogue, off-book contracted firm imports, is exactly what
>    PRM accounting argues about.
> 9. **Prior-art instruments were degraded on 2026-09-05.** The adversarial prior-art sweep behind
>    these corrections ran on **Europe PMC + WebSearch only**: Semantic Scholar returned HTTP 429
>    on 12 queries and OpenAlex returned an exhausted daily budget. No source states the analogy in
>    what was reachable, but the C5 §11 bar (≥8 formulations across ≥2 working indices) is **not**
>    met on the engineering side.

---

## What would settle it

1. **Re-run the intersection on the in-scope anchor, inside G34, with decade bins.** Denholm &
   Hand 2011 × Houston & McNamara 1993 (and × McNamara & Houston 1987), OpenCitations, same
   blank-key filter, same mode-6 binning as the Billinton rows. That is the measurement G34's own
   scope paragraph demands and currently borrows from a scout report. **Cost: hours.**
2. **Re-run Brodin's forward propagation under the paper's actual mixed policy, with `C_WU = 6
   kJ`, and check the output against the paper's own 0.74 g/day.** If the recomputed daily gain
   lands at 0.74 g the simulation is validated and every number in §3 and §4 can be reissued with
   a stated tolerance. If it does not, `c33_lolp.py` has a second fault. **This is the single
   highest-value item: it is a positive control the note never ran, and it decides whether the
   five-decade separation is real or a policy artifact.**
3. **Re-run the DP at `ε = 0` and read the re-optimised `x_dusk`.** Turns C33's demand-side claim
   from an in-model counterfactual into an in-model result, and is the only version of the second
   falsifier that the formalism can actually answer.
4. **Settle the estimand question by computing both functionals on one trace.** Take one
   state-of-charge trajectory; compute (a) `P(first hit 0 within T)` and (b)
   `Σ_t P(x(t) ≤ 0)·Δt` on the non-absorbing version. **The ratio of those two numbers is the
   honest exchange rate between starvation probability and LOLE**, it is computable from the bird
   model alone, and it would replace the invented 8-hour convention in §3 with a derived one. If
   that ratio is stable across parameterisations, the two-way table becomes a result; if it swings
   by orders of magnitude, table B should go.
5. **Repeat attack 1 on a power-engineering index.** IEEE Xplore or a working Semantic Scholar
   key, ≥8 formulations, tabulated to the C5 §11 standard. Europe PMC's coverage of power
   systems is thin and the current NOVEL-on-the-analogy finding rests on it.
6. **Get the grid-side energy-margin number properly.** The ≈0–0.25 figure above is reasoned from
   4-hour storage sized to a 4-hour net peak, not fetched. A cited accreditation study (ELCC of
   storage, duration-dependent) would make the like-for-like comparison quotable.
