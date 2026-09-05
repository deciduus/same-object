---
name: information-audit
type: method
---

# The information audit

> **The entropy sibling of the [[reservoir-audit]].** Where the reservoir audit does
> energy–momentum bookkeeping — a fuel-free device with `Σ > 1` has a misidentified
> *reservoir* — this one does entropy bookkeeping: a device that claims to compute, measure,
> sort or erase below the Landauer floor must **export the missing entropy somewhere**, and
> the audit specifies where and how much. It is built on the same four-step template of
> [[specification-instruments]] and validated the same way: on cases whose answer is already
> measured, before it is pointed at anything open.
>
> **It reproduces both calibration cases.** Run on Bérut et al.'s colloidal bit-erasure it
> returns the Landauer floor `kT ln2 ≈ 2.87×10⁻²¹ J` at 300 K and the measured heat saturates
> there. Run on Toyabe et al.'s single-molecule Maxwell demon it correctly names the sink that
> balances the books — **the demon's memory register**, an initially-unnamed entropy sink that
> closes the ledger exactly as Pioneer's onboard thermal photon field closed the reservoir
> ledger. It also recovers Koski et al.'s single-electron Szilard engine at 102 mK. Three for
> three, with the sink identified each time.

---

## 0. Why the analogy is exact

The reservoir audit rests on one identity, `P_total = −F·Δu`, and one move: name the reservoir
that supplies the coupling, or the device is misdescribed. The information audit rests on the
**second law counted with the information term**, and the same move: name the entropy sink that
absorbs the missing bits, or the sub-Landauer claim is misdescribed.

| | [[reservoir-audit]] | information audit |
|---|---|---|
| Conserved / bounded quantity | energy–momentum | entropy (incl. mutual information) |
| Exact identity | `P_total = −F·Δu` | `ΔS_tot = ΔS_bath + ΔS_mem + ΔS_corr ≥ 0` |
| Enumerated objects | reservoirs in contact | entropy **sinks** in contact |
| Exclusion leg | availability `A = F_req·Δu / P_avail > 1` rules a reservoir out | a sink that cannot absorb the required entropy is ruled out |
| The signature failure | a claim that supplies coupling from **no reservoir** (`Σ > 1`) | a claim that exports entropy to **no sink** (sub-Landauer with nothing debited) |
| Output | residual specification of the partner reservoir | residual specification of the missing sink: bits, DOF, rate |

The `Σ > 1` of the momentum ledger and "erasure below `kT ln2` with nothing else changed" are
the *same impossibility* in two conserved quantities. Neither is a verdict of "impossible" —
each is the flag that a partner (a reservoir; a sink) has been left unnamed.

---

## 1. The exact identity

Three forms, tightening from inequality to equality, all mechanism-free.

**(a) Landauer (1961).** Erasing one bit of information in contact with a bath at temperature
`T` dissipates at least

```
Q_erase ≥ kT ln2 = 0.693 kT
```

— the bit's entropy `k ln2` cannot vanish; it is exported to the bath as heat. At 300 K,
`kT ln2 = 2.87×10⁻²¹ J` (COMPUTED from `k = 1.380649×10⁻²³ J/K`; Bérut confirms `≈ 3×10⁻²¹ J`,
VERIFIED below).

**(b) Sagawa–Ueda generalized second law (with feedback / measurement).** If an operation
acquires mutual information `I` about the system by measurement, the second law is relaxed by
exactly that information:

```
⟨W_ext⟩ ≤ −ΔF + kT·I        equivalently   ⟨ΔF − W⟩ ≤ kT·I
```

Information is a resource worth `kT` per nat. This is the term the naive ledger omits, and it
is the whole reason a Maxwell demon appears to beat the second law: the books balance only when
`I` is counted. (Toyabe et al. eq. 1, VERIFIED below.)

**(c) Generalized Jarzynski equality (feedback efficacy form).** The inequality (b) is the
first cumulant of an exact equality:

```
⟨ exp[(ΔF − W)/kT] ⟩ = γ ,      0 ≤ γ ≤ m
```

where `γ` is the feedback efficacy — the sum over reverse trajectories of the probability the
control is undone — and `m` the number of measurement outcomes. `γ = 1` recovers the ordinary
Jarzynski equality (no usable information); `γ > 1` is the quantitative signature of a working
demon. (Toyabe et al. eq. 2, VERIFIED below.)

**The bookkeeping statement.** For any logically irreversible operation, any measurement of `I`
bits, any sorting/demon step: the total entropy change including the information term is `≥ 0`.
Missing dissipation at the system is not missing — it has been booked into a sink.

---

## 2. The finite enumeration of entropy sinks

Every partner the device is in entropy-contact with. The standing list, which the calibration
and open cases between them exercise:

1. **The thermal bath.** Absorbs heat `Q`; carries entropy `Q/T`. `k ln2` of entropy per erased
   bit, minimum. The default sink, and the one Landauer names.
2. **The memory register** that stores measurement outcomes. Each stored bit is `k ln2` of
   entropy *deferred*: not yet paid, but owed at the eventual erasure of the record. **This is
   the sink people forget, and it is the one that closes the Maxwell-demon books** — the exact
   analogue of the laboratory frame ("pushing on the Earth") in the reservoir audit.
3. **Correlations / mutual information** built with a feedback controller. Entropy can hide in
   the *joint* state of system+controller even when neither marginal shows it. `I` in identity
   (b) lives here.
4. **The physical carrier of the erased information** — the specific degrees of freedom the bit
   was encoded in (a colloidal position, a charge, a spin, a photon mode). Erasure randomizes
   *these*; the audit must be able to point at which.
5. **A non-thermal work/energy reservoir** (squeezed, coherent, or at a second temperature).
   This one can genuinely *shift* the apparent floor below `kT ln2` — and a claim that invokes
   it is admissible only if that reservoir is named and its entropy budget is drawn on. It is
   the sink most often smuggled in unlabelled.

---

## 3. Availability exclusion

For a claimed sub-Landauer operation, compute the entropy each candidate sink would have to
absorb, and whether it can.

- A claim that erases `N` bits and shows heat `< N·kT ln2` at the bath **and** writes nothing
  to memory **and** builds no correlation **and** invokes no non-thermal reservoir is
  **excluded** — it exports entropy to no sink. This is the `Σ > 1` of the information ledger:
  not "impossible physics," a misidentified sink.
- A claim that erases `N` bits with `< N·kT ln2` at the bath but *stores the outcomes* is not
  excluded — the deferred `N·k ln2` sits in sink 2, payable later. (This is precisely the
  reversible-computing loophole; see the open case.)
- A claim invoking sink 5 is admitted only with the reservoir's entropy budget written down,
  the same way the reservoir audit admits a photon reservoir only after `P_avail/c` is computed.

---

## 4. Residual specification

What survives is never a verdict. It is a description of the sink any real mechanism must use:
**how many bits, into which degrees of freedom, at what rate.** Prefix every negative with
*of the sinks considered* — the list is never provably complete (the Pioneer lesson: the real
partner sat unnamed for a decade).

---

## Part A — validation on measured cases

`VERIFIED` = fetched this session with the URL that produced it, per METHOD §4. `COMPUTED` =
arithmetic from a verified constant.

| Case | Known answer | What the audit returns | Sink identified | Status |
|---|---|---|---|---|
| **Bérut et al. 2012** — colloidal double-well bit erasure, `T = 300 K` | mean dissipated heat saturates at `kT ln2 ≈ 3×10⁻²¹ J` for long protocols | `Q_erase ≥ kT ln2`; the erased bit's `k ln2` is exported as heat; floor `= 2.87×10⁻²¹ J` | **the thermal bath** (sink 1) | ✔ reproduced |
| **Toyabe et al. 2010** — single-molecule feedback demon, `T = 300 K` | extracts `⟨ΔF−W⟩ = 0.062 kT` using `I = 0.22`; efficiency 28%; `γ > 1` | work is paid for by information written to the demon's **memory**, redeemable only at an erasure cost `≥ kT·I` | **the memory register** (sink 2) | ✔ reproduced, sink correct |
| **Koski et al. 2014** — single-electron Szilard engine, `T = 102 mK` | extracts `⟨−W⟩ ≈ 0.75 × kT ln2 ≈ 7.3×10⁻²⁵ J` per bit | extracted heat balanced by the **information created** about electron position; erasure regenerates `≥ kT ln2` | **created information / memory** (sinks 2–4) | ✔ reproduced |

### A.1 Bérut — the bath (sink 1) ✔

- "in the limit of long erasure cycles the mean dissipated heat **saturates at the Landauer
  bound**," and the long-time fit gives a constant `A = 0.72 kT`, "close to `kT ln2 ≈ 0.693 kT`";
  Landauer bound `≈ 3×10⁻²¹ J` at room temperature (300 K) — all **VERIFIED**,
  [ar5iv/1503.06537](https://ar5iv.labs.arxiv.org/html/1503.06537) (Bérut/Ciliberto review of
  the Nature 483, 187 (2012) experiment).
- Audit input: one bit erased, no memory kept, no feedback. Sinks 2–5 are empty by construction.
  The entropy `k ln2` has exactly one place to go — the bath — so the audit predicts
  `Q ≥ kT ln2 = 2.87×10⁻²¹ J` (COMPUTED). **The measurement lands on the prediction.** This is
  the information audit's Part-A anchor: a case where only one sink is available and the floor
  is hit.

### A.2 Toyabe — the memory register (sink 2) ✔ *the decisive test*

This is the exact analogue of Pioneer: an initially-unnamed sink that closes the balance.

- Generalized second law `⟨ΔF − W⟩ ≤ kT·I` (their eq. 1) and generalized Jarzynski
  `⟨exp[(ΔF−W)/kT]⟩ = γ`, `0 ≤ γ ≤ 2` (their eq. 2) — **VERIFIED**,
  [arXiv:1009.5287](https://arxiv.org/abs/1009.5287) (full text read this session).
- For the shortest feedback delay `ε = 1.1 ms`: `p = 0.059`, `I = 0.22`, `⟨ΔF−W⟩ = 0.062 kT`,
  giving "the efficiency of the information-energy conversion as `⟨ΔF−W⟩/kT·I = 28%`" —
  **VERIFIED**, same source. The demon extracts free energy exceeding the work done on the
  particle; naively the second law is violated.
- **Where does the entropy go?** The paper answers it in exactly the audit's language:
  "since the energy converted from information is compensated for by the **demon's energy cost
  to manipulate information**, the second law of thermodynamics is not violated when the total
  system including both the particle and demon is considered" — **VERIFIED**, same source. The
  demon's Fig. S1 shows `kT ln2` debited in the macroscopic memory per bit converted.
- **The audit's report:** the extracted `0.062 kT` is not free; it is a loan against the
  measurement record. The information `I = 0.22` written into the demon's memory is `kT·I` of
  deferred entropy in sink 2, redeemed when that memory is erased (sink 2 → sink 1, at the
  Landauer cost of A.1). The books balance in the memory, which no term in the *particle's*
  ledger contains — precisely as Pioneer's coupling balanced in a photon field no term in the
  *external* reservoir ledger contained. **The audit names the sink the naive ledger omits.**

### A.3 Koski — created information (sinks 2–4) ✔

- "extraction of `kT ln2` of heat from the reservoir at temperature `T` per one bit of created
  information," measured `⟨−W⟩ ≈ 0.75 × kT ln2` at bath temperature `T = 102 ± 3 mK`;
  "According to the Landauer principle, erasure of this information generates at least the
  extracted amount of heat, `kT ln2` per bit, restoring the agreement with the second law" —
  **VERIFIED**, [ar5iv/1402.5907](https://ar5iv.labs.arxiv.org/html/1402.5907) (PNAS 111,
  13786 (2014)). Floor at 102 mK: `kT ln2 = 9.76×10⁻²⁵ J`, so `0.75×` is `7.3×10⁻²⁵ J` (COMPUTED).
- Audit report: identical structure to Toyabe at a different substrate (single charge, sink 4)
  and three orders of magnitude colder. The extracted heat is booked against information created
  about the electron's position; the erasure debt closes it. **Sink correctly identified; the
  instrument is substrate- and scale-independent, as a bookkeeping identity must be.**

### Part A verdict

**Three for three, and the sink is named correctly each time.** Bérut hits the floor with only
the bath available; Toyabe and Koski appear to beat it and are closed by the memory sink the
naive ledger omits. The instrument reproduces the calibration cases and may be pointed at an
open one.

---

## Part B — the open case: the real floor of reversible / adiabatic computing

**The claim.** Logically reversible (adiabatic) computation can be run with energy dissipation
per operation `→ 0`, arbitrarily far below `kT ln2`.

Run the audit rather than adjudicating the claim.

**Step 1 — the identity.** A *logically reversible* gate erases no bits: `ΔI = 0`, the Landauer
term is zero, and identity (a) places **no floor at all**. So the headline claim is *not
excluded* — quasi-static reversible logic can in principle dissipate `→ 0`. The audit agrees
with the proponents this far, and this is the honest part of the claim.

**Step 2 — enumerate what the computation actually does.** A useful computation is not purely
reversible end-to-end. It must, per operation:
- **initialize** input/ancilla registers to a known state (`I_in` bits pushed to a definite
  value — logically irreversible);
- **clear garbage / ancilla** bits to re-read a definite output (`G` bits — logically
  irreversible);
- run at **finite rate** `R`, not quasi-statically.

**Step 3 — availability exclusion.** Each irreversible bit in Step 2 carries `k ln2` that must
land in a sink:
- Sent to the **bath** → dissipation `≥ (I_in + G)·kT ln2` per operation. Not zero. The claim
  of zero total dissipation is **excluded** for any computation that resets a register it reads.
- Kept in **memory** (Bennett's construction: retain the full reversible history tape, never
  clear the garbage) → dissipation at the bath genuinely `→ 0`, but the entropy is now booked
  into sink 2, a history tape **growing at `(I_in + G)·k ln2` per operation**. The tape is the
  sink. Zero dissipation is bought with unbounded memory, not with no entropy.
- Sent to a **non-thermal reservoir** (sink 5) → admissible only if that reservoir is named and
  its finite entropy budget is drawn down; it is exhausted after a finite number of operations.

**Step 4 — the residual specification.**

> **Of the sinks considered**, a reversible-computing scheme that reads a definite output and
> resets its registers must deposit at least `(I_in + G)·k ln2` of entropy per operation — into
> the thermal bath as `(I_in + G)·kT ln2` of heat at throughput rate `(I_in + G)·R·k ln2` W/K,
> **or** into a monotonically growing history-tape memory at `(I_in + G)·k ln2` per operation,
> **or** into a named non-thermal reservoir whose entropy budget bounds the total number of
> operations. A scheme claiming zero dissipation, bounded memory, and no non-thermal reservoir
> simultaneously has an unnamed sink and is excluded — the entropy signature of a misidentified
> partner, the `Σ > 1` of the information ledger.

The finite-rate correction is separable and additive: the Landauer value is the quasi-static
floor, and running in finite time `t` adds a dissipation `∝ 1/t` on top (Bérut's own `B/τ` term
is this same overhead measured — VERIFIED above). "Sub-Landauer" and "at finite speed" cannot
both be claimed without a sink for the excess.

This is a specification, not a verdict: it tells an experimentalist exactly what to measure —
heat at the bath, growth rate of any retained memory, or the depletion of a claimed non-thermal
reservoir — to locate where a given adiabatic scheme actually books its entropy. Compare the
project's own [[C3-energy-error-axis]]: real CMOS sits at `~10⁶ × kT ln2` per operation, six
orders *above* the floor, so the contest is entirely about the quasi-static limit, not about
any device yet built.

---

## The link to biological proofreading — [[G25-proofreading-coding]]

The same bookkeeping, with biology paying the information cost in ATP rather than in electrical
erasure. Kinetic proofreading spends `≥ kT` per decade of error suppression — `ln10 = 2.303 kT`
per decade in [[C3-energy-error-axis]]. That is identity (b) run backwards: a proofreading step
is a **measurement-and-discard** — the enzyme reads substrate identity and irreversibly ejects
the wrong substrate — and the discarded bit's entropy must be exported to a sink. Biology's sink
is the phosphate released into solution: one ATP hydrolysis carries `≈ 20–28 kT` (C3: ATP at
`27.6 × kT ln2`), more than enough to pay the `k ln2` per rejected bit with the rest as the
irreversibility margin that makes the discard effectively one-way. **The information audit and
kinetic proofreading are one instrument in two vocabularies** — the demon's memory-erasure cost
of Toyabe and the ATP cost of a proofreading cycle are the *same* entry in the *same* ledger,
which is exactly the unread bridge G25 measures at a 3.8% citation intersection.

---

## Part C — negative controls (design; NOT RUN) — *added 2026-09-05 from `audits/staged`*

The 3/3 of Part A is a positive-only control set, and it is not blind: all three cases
(Bérut 2012, Toyabe 2010, Koski 2014) are textbook results whose entropy sink is stated in the
source the audit quotes, and Bérut has only one sink available by construction, so it cannot
discriminate. **The audit has never been shown to return "no unnamed sink."** Mirrors
[[reservoir-audit]] Part D.

**C.1 — A device whose entropy books already close.** Feed a system with a fully accounted
entropy budget and no unnamed sink: a measured, near-quasistatic isothermal gas expansion, or a
Carnot-cycle heat engine at published efficiency, where `ΔS_total` is accounted to within
measurement uncertainty by the named reservoirs alone. **What counts as returning nothing:** the
sink enumeration terminates with the *already-named* sinks supplying the full balance,
`ΔS_residual` reported as an interval containing zero, and **no new sink specified.** If the
audit names an additional sink here, the Toyabe result — where naming the demon's memory register
as the unnamed sink is the audit's headline success — is an artefact of the procedure.

**C.2 — A blind case.** Compute the sink for one case *before* reading the source's conclusion,
and record the pre-registration in the note with a date, the source withheld until after. The
three existing cases cannot be un-read, so this needs a fourth. **What counts as passing:** the
pre-registered sink matches the published one, and the pre-registration is timestamped ahead of
the read.

**C.3 — An adversarial case.** A published claim whose sink attribution was **later corrected**.
The audit passes if it reproduces the correction, not the original attribution.

**Until C.1 and C.2 are run, "validated 3/3" should be read as *validated against positives only,
non-blind*.**

---

## Standing

Part A: **passed, three for three**, with the entropy sink correctly identified in every case —
the bath for pure erasure (Bérut), the memory register for the two Maxwell demons (Toyabe,
Koski). The Toyabe case is the information audit's Pioneer: an apparent violation closed by a
sink no term in the naive ledger contains. Part B returns a residual specification for
reversible computing rather than a verdict: `(I_in + G)·k ln2` of entropy per operation, into
the bath, a growing memory, or a named non-thermal reservoir — one of the three, or the claim is
excluded.

The instrument inherits the reservoir audit's discipline verbatim: enumerate the finite sink
list, exclude by availability, and **prefix every negative with *of the sinks considered***. It
is a [[specification-instruments]] construction in the entropy channel, sibling to the
[[reservoir-audit]] in the momentum channel.

See [[specification-instruments]], [[reservoir-audit]], [[C3-energy-error-axis]],
[[G25-proofreading-coding]].
