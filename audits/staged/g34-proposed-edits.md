---
name: PENDING-log-G34ADV
type: method
---

# PENDING log entries — G34 adversarial review, 2026-09-05

**Not applied. Not linked from `00-index.md`.** Proposed `vault/log.md` entries and the exact
edits they describe, produced by `audits/g34-adversarial.md`. An orchestrator that accepts them
should paste the log lines newest-first into `vault/log.md` and apply the edits to
`vault/gaps/G34-lolp-starvation-risk.md` and `vault/computed/C33-lolp-starvation.md`, then delete
this file. Full evidence, queries and hit tables live in the audit; only the verdict and the
replacement text are repeated here.

**Verdict carried over: NARROW, grade REPACKAGED.** The analogy is not prior art. The state
recursion and the shadow price are genuinely shared. The estimand is not, the citation anchors
are the wrong literature, and two of C33's headline numbers rest on undisclosed parameter and
policy choices that both point the same way.

---

## Proposed `vault/log.md` entries

```
## [2026-09-05] correction | G34: LOLE is not a first-passage quantity; title and thesis corrected
The gap was titled "...are the same first-passage problem". On the bird side 0 is absorbing and
P(starve) is a first-passage probability; on the grid side 0 is NOT absorbing — load is shed, the
shortfall ends, storage recharges — so LOLE = Sum_t P(x(t)<=0)*dt is an expected occupation time
counting repeated crossings. Those are different functionals of the same process. What the two
fields share is the state recursion and the shadow price, not the estimand. C33 sec 1's clause
"only the aggregation differs, and the aggregation is a reporting convention" is withdrawn. The
error was visible in C33's own sec 5.5 ("terminal vs restorable") and in table B's saturation for
Ireland, and was not carried into sec 1 or the title. Produced by adversarial review,
audits/g34-adversarial.md attack 3.

## [2026-09-05] correction | C33: simulated policy is not the paper's optimal policy; daily gain overshoots by 2.3x
C33 sec 3 computed P(starve) = 8.25e-8 "under the policy the paper reports as optimal under almost
all conditions — forage intensively every daylight period". Brodin et al. 2017 attaches that
qualifier to hypothermia alone; on foraging it reports a switch to cautious foraging (behaviour 2,
alpha = 60 kJ) after noon. The paper states its own outcome: total daily fat gain 0.74 g = 27.4 kJ
at the model's 37 kJ/g. C33's budget gives 76.80 - 15.0 = 61.8 kJ = 1.67 g, a 2.3x overshoot. The
five-order-of-magnitude LOLE separation in sec 3 is therefore substantially a policy artifact.
Source: Europe PMC PMC5596050 full text fetched 2026-09-05.

## [2026-09-05] correction | C33: warming-up cost C_WU omitted; hypothermia lever overstated ~4x
Brodin Table 2 gives C_WU = "0 or 6 kJ" and the paper reports both treatments (Fig. 3a, dashed vs
solid). C33's sec 2 parameter table omits C_WU and its 21.0 kJ hypothermic overnight draw is the
C_WU = 0 branch. Charging 6 kJ gives 27.0 kJ against 30.0 kJ normothermic — the hypothermia lever
saves 3 kJ, not 9. The paper's own stabilised cycle corroborates ~27.4 kJ (0.74 g/day). The
demand-side claim in sec 4 falls from a 47-point lever (57% -> 10%) to ~12 points (22% -> 10%).
The omitted branch was the one that flattered the note.

## [2026-09-05] correction | C33: +57% reserve margin compares an energy ratio against a capacity ratio
Planning reserve margin is (firm capacity - peak load)/peak load, MW/MW at one annual instant. The
bird's (x_dusk - R)/R is kJ/kJ over a 16-hour integral. The like-for-like grid quantity is the
energy margin over the critical period (stored energy entering the net-peak window over the energy
discharged across it); for 4-hour storage sized to a 4-hour net peak that is ~0-0.25. On the
paper's own budget the bird's margin is 12/27.4 = +43.8%, so the honest statement is ~0.44 against
~0-0.25, roughly 2x — and PRM should not be named. Note also that the margin is algebraically just
x_start / R: the whole sec 4 prediction is one ratio of two model parameters.

## [2026-09-05] method | G34's citation-intersection anchors measure a literature G34's own scope excludes
All four cross-domain pairings in G34 are anchored on Billinton & Allan 1996 and Billinton & Li
1994 — classic LOLP, a capacity-outage probability table convolved against a load-duration curve,
with no integrated state and therefore no reserve. G34's own "What survives" section says the
comparison must be to storage-constrained adequacy, not to that. The concession was never carried
into the measurement. The in-scope zero exists and is already measured — Denholm & Hand 2011 x
Houston & McNamara 1993, N_A 794, N_B 196, intersection 0, audits/scout-06-energy-systems.md
candidate #3 — but is imported rather than run inside G34 with its own decade bins.

## [2026-09-05] verification | G34's analogy is not prior art; bio-inspired power systems contact is word-level only
Europe PMC, 12 two-phrase conjunctions plus 3 calibration controls, and 4 WebSearch formulations,
all 2026-09-05. No source states the reserve-margin/fat or LOLP/starvation identity. The
prediction that bio-inspired power-systems work would prove to be swarm/metaheuristic is confirmed
by name: all 8 hits on '"loss of load probability" AND "bird"' are optimisation algorithms named
after birds (black-winged kite, honey badger); the 3 hits on '"loss of load expectation" AND
"foraging"' are metaheuristic sizing papers. Grade on the analogy: not REDISCOVERED, not merely
LOCATED. Instruments were degraded — Semantic Scholar returned HTTP 429 on 12 queries and OpenAlex
returned an exhausted daily budget — so the C5 sec 11 bar (>=8 formulations, >=2 working indices)
is NOT met on the engineering side and an IEEE-side sweep is still owed.

## [2026-09-05] method | Europe PMC FULL_TEXT: field prefix silently returns 0 — a fake-zero trap
The first prior-art pass used FULL_TEXT:"..." AND FULL_TEXT:"..." on
https://www.ebi.ac.uk/europepmc/webservices/rest/search and returned 0 on all ten queries,
including FULL_TEXT:"fat reserves" alone, which cannot be zero. The endpoint does not honour that
field prefix and returns 0 for everything. Bare-quoted phrases work ('"fat reserves"' -> 3,992).
This is failure-modes mode 1 (a field/punctuation artifact, not a synonym problem) and it would
have manufactured ten clean confident zeros. Candidate for the homographs/failure-modes register.

## [2026-09-05] correction | C33: the demand-side reading is borrowed grid -> bird, not bird -> grid
C33 sec 4 calls "the bird buys most of its adequacy on the demand side" the transferable claim.
Demand response counted as capacity toward resource adequacy is mature grid practice (MISO Demand
Response 101, 2024; PJM capacity auction; "negawatt" since Lovins 1989). The concept runs grid ->
bird. What is new is the quantity — no published figure exists for the demand-side share of an
animal's adequacy margin — and that quantity is currently uncertain by a factor of ~4 (see the
C_WU entry above).
```

---

## Exact replacement sentences

Reproduced verbatim from `audits/g34-adversarial.md` § *Proposed edits to G34 and C33*. Apply
there; nothing in this file is a vault edit.

### G34

**H1.** `# Loss-of-load probability and starvation risk are the same first-passage problem`
→ `# Loss-of-load probability and starvation risk are the same reserve recursion, read out by different functionals`

**Blockquote, first sentence.** Replace `Power-system reliability engineering asks *what is the
probability that a stored reserve hits zero before the horizon ends, given stochastic income and a
stochastic draw* and calls the answer **loss-of-load probability**.` with:

> Power-system reliability engineering propagates a stored reserve under stochastic income and a
> stochastic draw and reports **how much time the reserve spends at or below zero** — loss-of-load
> probability and its aggregate, loss-of-load expectation. Behavioural ecology propagates the same
> state under the same drivers and reports **whether an overwintering bird's fat reserve ever
> reaches zero** — starvation probability. **The state recursion is shared and the shadow price is
> shared; the estimand is not.** The grid's zero is a reflecting boundary and its statistic is an
> expected occupation time; the bird's zero is absorbing and its statistic is a first-passage
> probability.

**Frontmatter `note:`.** Replace with:

> `note: "Power-system adequacy and small-bird winter energetics propagate the same stochastic reserve recursion by backward SDP and read the same shadow price off the value function, but aggregate it into different functionals (occupation time vs first passage). Storage-constrained anchor pairing (Denholm & Hand 2011 x Houston & McNamara 1993) intersection 0 at 794 x 196; classic-LOLP anchors also 0 but are out of the claimed scope; same-side controls 25.2% and 12.8% of the smaller set."`

**After the provenance table.** Insert:

> **Anchor scope, stated against this note's own restriction.** The four Billinton pairings above
> measure the **classic-LOLP** literature, which *"What survives"* below explicitly places outside
> this note's scope. They are retained as an out-of-scope control. **The in-scope measurement is
> the storage-constrained pairing, Denholm & Hand 2011 × Houston & McNamara 1993, `N_A` 794,
> `N_B` 196, ∩ = 0** (`audits/scout-06-energy-systems.md` candidate #3, OpenCitations 2026-09-05).
> Until that pairing is re-run inside this note with its own decade bins, the in-scope zero is
> imported, not measured here.

**End of "What survives".** Append:

> **A second scope restriction, from `audits/g34-adversarial.md`.** Even under storage-constrained
> scoping, **LOLE is not a first-passage quantity**: unserved load is shed and the reserve
> recovers, so the grid's zero is not absorbing and LOLE counts repeated crossings. The bird's
> `P(starve)` is a first-passage probability on an absorbing boundary. **What the two fields share
> is the state recursion and the shadow price, not the estimand.** The claim is corrected to that,
> and the word "first-passage" is removed from the grid side throughout.

### C33

**§1.** Replace `Same functional equation, same absorbing boundary, same backward sweep — only the
aggregation differs, and the aggregation is a reporting convention.` with:

> Same state recursion, same backward sweep — **and there the identity stops.** The bird's zero is
> absorbing and `P(starve)` is a first-passage probability. **The grid's zero is not absorbing**:
> load is shed, the shortfall ends, and storage recharges, so `LOLE` is an expected **occupation
> time** of a non-absorbing process, counting repeated crossings. First-passage probability and
> expected occupation time are different functionals of the same process and they diverge exactly
> where the risk is interesting — a system that dips below zero ten times for an hour each has
> LOLE 10 h and would have died at the first dip. **The aggregation is not a reporting
> convention; it is the difference between the two estimands.**

**§1, displayed recursion.** `0 absorbing` → `0 absorbing on the bird side only; reflecting on the
grid side`.

**§2, parameter table.** Add row:

> `| C_WU | extra warming-up cost, hypothermic bird | **0 or 6 kJ** — the paper reports both | Table 2, Eq. 10 |`

**§2, derived budget.** Replace `Overnight draw \`45 × 16/24 × 0.7\` = **21.0 kJ** hypothermic
(25.2 cold)` with:

> Overnight draw, `C_WU = 0`: `45 × 16/24 × 0.7` = **21.0 kJ** hypothermic (25.2 cold). **With the
> paper's other treatment, `C_WU = 6 kJ`: 27.0 kJ hypothermic (31.2 cold)** — against 30.0 kJ
> normothermic, so the hypothermia lever saves **3 kJ, not 9**. **The paper's own stabilised cycle
> independently puts the overnight draw at ≈27.4 kJ**: it reports a total daily fat gain of
> **0.74 g**, which at the model's 37 kJ/g is 27.4 kJ, and in a stabilised cycle the night's draw
> equals the day's gain. **Every number below that uses 21.0 kJ is the low-draw branch, and it is
> the branch that flatters this note.**

**§3, policy sentence.** Replace `under the policy the paper reports as optimal under almost all
conditions — forage intensively every daylight period, maximum hypothermia every night` with:

> under **maximum foraging** — forage intensively every daylight period, maximum hypothermia every
> night. **This is not the paper's optimal policy and the note previously mis-described it as
> such.** The paper's "under almost all conditions" qualifier attaches to hypothermia alone; on
> foraging it reports the bird switching to cautious foraging (behaviour 2, α = 60 kJ) after noon
> once dusk fat is within reach. **The consequence is measurable: this note's budget gives 61.8 kJ
> (1.67 g) of net daily fat gain against the paper's own reported 0.74 g — a 2.3× overshoot. The
> `8.25 × 10⁻⁸` is therefore an upper bound on safety, and the five-decade separation in §3 is
> substantially an artifact of the policy, not a property of the bird.** Re-running under the
> mixed behaviour-1/behaviour-2 policy is the outstanding fix.

**§3, table B heading.** `### B. Grid criterion → bird units` →
`### B. Grid criterion → bird units — illustrative only, not a result`, and prepend:

> **This direction converts an expected occupation time into a first-passage probability, and
> those are different functionals (§1).** The saturation for Ireland is the symptom, not a
> curiosity. The table is retained to show the scale, and **no claim in this note rests on it.**

**§4, comparator.** Replace `roughly **two to four times** the 15–20% grid convention (ESIG 2024:
WECC-CAMX PRM ≥ 15%, mainland Spain ≥ 10%)` with:

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

**§4, headline claim.** Replace `**The bird meets a far stricter adequacy standard than any grid
while carrying a supply-side margin that is only modestly larger, because it buys most of its
adequacy on the demand side.** That is the transferable claim.` with:

> **The demand-side reading is the grid's own, not a transfer from the bird.** Demand response
> counted as capacity toward resource adequacy is mature grid practice — MISO's *Demand Response
> 101* (2024), PJM's capacity auction, and "negawatt" as a term since Lovins 1989. **The borrowing
> here runs grid → bird.** What is new is not the concept but the **quantity**: no published
> figure exists for the demand-side share of an animal's adequacy margin. **On the low-draw branch
> that share is large (57% → 10% when hypothermia is removed); on the paper's own budget, with the
> 6 kJ warming cost charged, it is 22% → 10% — a 12-point lever, not a 47-point one.** The claim
> is the existence and rough size of the quantity, and its size is currently uncertain by a factor
> of four.

**§4, falsifier.** Append:

> **The second falsifier is not yet tested even in-model.** The normothermic rows above are a
> counterfactual inside one parameterisation — `x_dusk` held at its `ε = 30%` optimum with `ε`
> switched off. A bird that genuinely cannot use hypothermia would **re-optimise `x_dusk` upward**,
> which is what the DP exists to compute. Re-running Brodin's DP at `ε = 0` and reading the new
> optimal dusk reserve is a small job and is the minimum before the demand-side mechanism is
> claimed.

**§5.** Append items 8 and 9:

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

## Not proposed, and why

- **No `standing:` change.** The gap survives as a narrowed claim; `live` is still correct and
  nothing here meets the bar in `failure-modes` for `overturned`.
- **No `crosses:` change.** `formalism` (rank 4) still holds: the shared object is the state
  recursion plus the shadow price, which is a formalism-level correspondence. The estimand
  difference narrows what is shared; it does not drop it to `vocabulary`.
- **No edit to `vault/_scripts/c33_lolp.py`.** The policy and `C_WU` faults are in the script, but
  fixing them is a recomputation, not a text edit, and the recomputed numbers should land in C33
  in one motion rather than as a sequence of partial corrections.
