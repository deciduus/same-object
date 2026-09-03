---
name: C20-release-the-constant
type: computed
---

# Release the constant: M6 as an integer operation on the dimension matrix

> **[[M6-vary-what-was-held-fixed]] is now a computable operator, not a slogan.** Give me a
> dimension matrix with some quantities marked *fixed constant* (appears alone) and some marked
> *free parameter*, and there is a finite, integer-linear-algebra procedure that (i) decides which
> Π-groups are constant-bound, and (ii) for each, **enumerates the dimensional signature a new
> quantity would need to release it** — the discrete search over "which held-fixed thing to attack."
> Run on the gecko it **re-derives contact splitting**: "release the surface-energy constant `w` by
> adding a length scale independent of the pad — the sub-contact radius." Run on a `kT` noise floor
> it points at **active/driven operation** (effective `T_eff`). This is the actionable form of
> [[G22-scale-transfer-triage]]'s triage, which G22 says nobody had built. The operator emits a
> *signature*, never a guarantee a physical quantity with that signature exists — a lead, not a
> result.

Instrument in the sense of [[specification-instruments]]: conserved object = the integer kernel of a
dimension matrix; finite enumeration = the columns of `D` plus the finite family of releasing
signatures; deliverable = for each lone constant, the exact dimension a new quantity must carry.
Discrete-math core: augmenting a matrix with a column and re-reading its kernel over ℤ.

---

## 1. The operator, stated as integer linear algebra

Base dimensions `[M, L, T]` (thermal carried as diffusivities/energies, no Θ row, per
[[C12-pi-space-lattice]]). A dimension matrix `D` has one column per quantity; entries are integer
powers. Partition the columns:

- **free parameters** `F` — quantities you can co-vary (lengths, speeds, geometry);
- **fixed constants** `K` — material/universal constants that appear *alone*, un-co-varyable
  (`kT`, `g`, `c`, `λ`, `ν`, surface energy `w`);
- one distinguished **scaling parameter** `s ∈ F` — the thing you push when you scale the design
  (body size, pad area), and possibly an **output** column you solve for.

A dimensionless (Π) group is an integer vector `x ∈ ker(D)` (Buckingham = linear algebra over ℤ;
the kernel is a free ℤ-module of rank `n − rank(D)`, Smith-normal-form guarantee, C12 §3.3).

**Constant-bound criterion (made precise).** Let `Π*` be the governing group of the target
capability, and let `c ∈ K` be a fixed constant with nonzero entry in `Π*`. Form the dimension
vector `d_c` of `c`. Let `d_c = p + r`, where `p` is the projection of `d_c` onto the column space
of the **free non-scale** submatrix `F \ {s}` and `r` is the residual. Then:

> `c` is **constant-bound** in `Π*` iff the only quantities carrying the dimension `c` must pair
> with (to enter `Π*`) are `c` itself, other fixed constants, and the scaling parameter `s`. In
> lattice terms (C12): the target vector has support on `c` with **no compensating free-parameter
> support** other than `s`. So as `s` varies, `Π*` is *forced* — the capability anti-scales.

This is exactly C12's reading — "two crossovers are locked iff their Π-difference vector is
supported only on non-tunable constants" — generalised from a *pair of crossovers* to *one target
group under scaling*. "Appears alone" = "the only length (or time, or energy) the constant can
combine with is the scale itself."

**The M6 operation — RELEASE THE CONSTANT.** Add one new column `q` (a new physical quantity) to
`D` with dimension `d_q` chosen so that the dimension `c` was "stuck to" is now supplied by a
**free quantity independent of `s`**:

```
   D  →  D_aug = [ D | d_q ]      with d_q ∈ span_ℤ( {the dimension c needs} ),  d_q ⟂ s
```

Concretely: `c` enters `Π*` by pairing with some dimension `δ` (a length, a time, an energy). If the
sole carrier of `δ` is `s`, add `q` with a `δ`-component, decoupled from `s`. Re-read `ker(D_aug)`:
it gains exactly one new Π-group `q/s` (the ratio of the new quantity to the scale), and `Π*`
becomes a **function of that ratio** instead of a fixed number. The constant `c` now sits in a
**compensable ratio** `c / (free δ-carrier)` — off the "appears-alone" diagonal. The capability is
no longer forced by `s`.

The operator's **output** is the signature `d_q` — a short integer `[M, L, T]` vector (up to
combination with existing free columns, a finite family). *Which* `δ` to attack is read off `Π*`;
the algebra returns the exact dimension a releasing quantity must carry. That finite list is the
discrete search M6 describes in prose.

---

## 2. Gecko adhesion — does the operator re-derive contact splitting?

**The bound.** Gecko adhesive strength scales as **A^(−1/4)** in pad area `A` — a *negative*
exponent, intrinsically anti-scaling (carried from [[G22-scale-transfer-triage]] and METHOD §9,
`evidence: full-text-read`; synthetic tape fails beyond ~1 cm², human-scale ~200 cm² unrealized).

**The matrix.** Fracture/JKR pull-off stress of a single contact of radius `R` is
`σ_c = C·(E w / R)^{1/2}` — elastic modulus `E`, work of adhesion (surface energy) `w`, contact
radius `R`. Quantities `[σ, w, E, R]`, rows `[M, L, T]`:

```
        σ    w    E    R
  M  [  1    1    1    0 ]
  L  [ -1    0   -1    1 ]
  T  [ -2   -2   -2    0 ]
```

**Kernel by integer elimination.** Rows `M` and `L` are independent; row `T = 2·(row M)`, so
`rank(D) = 2` ⇒ `4 − 2 = 2` Π-groups. Solving `M: s+b+e=0`, `L: −s−e+r=0` over `[σ,w,E,R]`:

| Basis | set | vector `(σ,w,E,R)` | Π-group | dimensionless check |
|---|---|---|---|---|
| Π_a | σ=1,E=0 | `(1,−1,0,1)` | `σR / w` | `(M L⁻¹T⁻²)(L)/(M T⁻²) = 1` ✓ |
| Π_b | σ=0,E=1 | `(0,−1,1,1)` | `E R / w` | `(M L⁻¹T⁻²)(L)/(M T⁻²) = 1` ✓ |

The law is `Π_a = f(Π_b)`, i.e. `σR/w = f(ER/w)`; fracture mechanics fixes `f(x)=C x^{1/2}`,
recovering `σ_c = C(Ew/R)^{1/2}`.

**Why it is constant-bound.** The surface-energy constant `w` (dimension `M T⁻²`, VERIFIED:
JKR pull-off `F_c = (3/2)π w R`, linear in `R`, independent of `E` — arXiv:2407.00378, fetched this
session) appears in **both** kernel vectors, always paired with the length `R`. When the pad is one
contact, `R ∝ A^{1/2}` — **`R` is locked to the scaling parameter.** So

```
   σ_c = C(Ew)^{1/2} · R^{-1/2}   and   R ∝ A^{1/2}   ⇒   σ_c ∝ A^{-1/4}.
```

There it is: the **−1/4 is `R^{−1/2}` composed with `R ∝ A^{1/2}`.** `w` is "alone" — its only
length companion is the scale itself. No free co-variation holds `σ_c` fixed as `A` grows.

**Apply RELEASE.** The dimension `w` is stuck to is a **length** (`R`), and the sole carrier of that
length is the scale. Operator output: *add a quantity of dimension `L`, independent of `A`.* Add the
**sub-contact radius `a`**:

```
        σ    w    E    R    a
  M  [  1    1    1    0    0 ]
  L  [ -1    0   -1    1    1 ]
  T  [ -2   -2   -2    0    0 ]
```

`a` is dimension `L`, already in the row space, so `rank = 2` still and now `5 − 2 = 3` Π-groups —
the new one is `Π_c = a/R`. The law generalises to `σR/w = f(ER/w, a/R)`. Contact-splitting
geometry supplies the form: split the pad into `n = (R/a)²` self-similar subcontacts; each has its
**own** pull-off stress `σ = C(Ew/a)^{1/2}`, set by `a`, **not** by the pad `R`. Equivalently the
total force gains `√n` at fixed pad area:

```
   F_tot = n · (3/2)π w a = (3/2)π w R² / a = √n · (3/2)π w R.
```

The constant `w` now sits in the **compensable ratio `w/(E a)`** with `a` free and independent of
scale. **The constant is released.** Make `a` small (sub-µm setal tips) and strength is recovered at
any body size.

**Verdict: the operator reproduces contact splitting.** "Release the surface-energy constant by
adding a length scale independent of the pad" *is* the sub-contact radius, and it is exactly the
Arzt–Gorb–Spolenak solution: *"splitting up the contact into finer subcontacts increases adhesion,"*
with flies/beetles at µm terminal elements and geckos (larger) forced to **sub-µm** ones — the
finer contact is the smaller independent length `a` (Arzt, Gorb, Spolenak, *PNAS* 100(19):10603–6,
2003; abstract VERIFIED via EuropePMC, fetched this session). The M6 operator, run blind on the
dimension matrix, points at the known biomimetic fix. That is the validation.

---

## 3. A `kT`-bound case — does it point at active drive?

**The bound.** A sensor's noise floor is `kT` (thermal energy, `M L² T⁻²`). Detecting signal
energy `E_sig` requires beating it; the statolith / hair-cell margin and Landauer's `k ln2` sit in
this family (C4/G11).

**The matrix.** Two energies `[E_sig, kT]`, rows `[M, L, T]`:

```
        E_sig   kT
  M  [    1      1 ]
  L  [    2      2 ]
  T  [   -2     -2 ]
```

`rank = 1` (identical columns) ⇒ `2 − 1 = 1` Π-group: `Π* = E_sig / kT`. The **only** way to move
`Π*` is to raise `E_sig` (a magnitude move — the thing M6 says is usually not the lever). `kT`
appears alone: `T` is the fixed ambient temperature, a constant of the environment, paired with
nothing free.

**Apply RELEASE.** The dimension `kT` is is an **energy**; the sole carrier of an *independent,
tunable* energy is absent. Operator output: *add a quantity carrying an independent energy (or, via
`E = k·T_eff`, an independent temperature / drive amplitude), or an independent time to average
over.* Add a controllable drive energy `U_drive` (`M L² T⁻²`, free):

```
        E_sig   kT    U_drive
  M  [    1      1       1    ]
  L  [    2      2       2    ]
  T  [   -2     -2      -2    ]
```

`rank = 1` still; now `3 − 1 = 2` Π-groups: `E_sig/kT` **and** `U_drive/kT`. The effective floor
becomes `kT · g(U_drive/kT) ≡ k T_eff`, with `T_eff` a **free parameter**. The equilibrium constant
`kT` now enters a compensable ratio with a driven energy scale — released.

**Verdict: the operator points at active/driven operation.** Moving from equilibrium `kT` to an
effective `k T_eff` set by an out-of-equilibrium drive is exactly the **active-bath trick** (G11):
raise (or reshape) the noise temperature deliberately, or — the dual reading, adding a *time* `τ_c`
rather than an energy — average the floor down by `1/√(B τ_c)` over a coherence time. Both are the
same discrete move: add an independent carrier of the dimension `kT` is stuck to, so the constant
leaves the diagonal. The operator names the escape hatch the driven-sensor literature already uses.

---

## 4. The screening procedure (the actionable form of G22's triage)

For a candidate capability:

1. **List** the governing quantities; build the dimension matrix `D` over `[M, L, T]`.
2. **Partition** columns into free parameters `F`, fixed constants `K`, output, and the scaling
   parameter `s`.
3. **Kernel.** Compute `rank(D)` by integer elimination; read off the Π-groups
   (`n − rank(D)` of them, integer basis via SNF). Identify the target group `Π*`.
4. **Constant-bound test.** For each `c ∈ K` appearing in `Π*`: is the dimension `c` must pair with
   (to enter `Π*`) carried by any free quantity **other than `s`**? If none — `c` is constant-bound
   (equivalently: `Π*`'s support on `c` has no compensating free-parameter support; C12's lattice
   criterion). The capability then anti-scales in `s`.
5. **Emit the signature.** For each bound `c`, output the residual dimension `r` — the `[M,L,T]`
   vector a new quantity must carry to supply, independent of `s`, the dimension `c` is stuck to.
   Up to combination with existing free columns this is a **finite family** of signatures.
6. **Enumerate candidates.** List physical quantities matching each signature that are realisable
   and independent of `s`. Each is a lead: *add this and `c` is released.* (Gecko: `L` ⟶ sub-contact
   size. `kT`: energy/time ⟶ active drive / coherence time.)
7. **Decide.** If no signature can release `c` — because `Π*` is a ratio of fixed constants with no
   free direction at all (e.g. `Sc = ν/D`, C12 §5, locked forever) — the capability is
   **unconditionally constant-bound**: a real impossibility, stop. Otherwise the emitted signatures
   are the ranked search space for what to change.

This turns G22's one-line criterion ("scale-transferable iff the governing group can be held fixed
by co-varying free parameters; constant-bound iff a constant appears alone") into a **decision
procedure over a finite set** — the thing G22's closing sentence and Perricone et al. 2021 both say
is missing.

---

## 5. The honesty limit — signature, not solution

The operator returns the **dimensional signature** a releasing quantity must have. It does **not**
tell you whether a physical quantity with that signature exists or is realisable. Two sharply
different outcomes, and they must not be confused:

- **No releasing signature is dimensionally possible** — `Π*` is a ratio of fixed constants with no
  free direction (the Schmidt-locked case). This is a **real impossibility**: no added quantity can
  unlock it, because the lock is in the constants' arithmetic. A genuine result.
- **A releasing signature exists but may have no physical realisation** — the algebra says "add a
  length independent of scale" or "add an independent energy," but whether such a quantity *exists
  and can be built* is outside the matrix. The gecko happens to have one (sub-contact size is a real,
  manufacturable, scale-free length). Another capability's required signature might correspond to no
  realisable quantity. This is a **lead, not a result.**

So the operator **narrows** the search — from "vary something" to "add a quantity of exactly this
dimension, decoupled from the scale" — and it **cannot guarantee** the quantity is out there. That
is precisely M6's posture (§8 of METHOD): it tells you *which held-fixed thing to attack*, not that
attacking it will succeed. The win is the same as every specification instrument here — it returns
a tighter description of what a solution must be, never the solution itself.

---

## 6. Prior art

| Source | What it does | Is it the release operator? | Provenance |
|---|---|---|---|
| Buckingham Π as kernel of the dimension matrix; Kitano, arXiv:1305.1291 | Π-groups as `ker T`, SNF decomposition `[I\|0]` | No — the *checking* machinery, not a directed search for what to add | VERIFIED (carried from C12; Kitano ar5iv full text) |
| Szirtes, *Applied Dimensional Analysis and Modeling* | Adds / suppresses / combines variables and dimensions to handle **singular** dimension matrices | No — a computational device for tractability (make `A` square), not a search for a quantity to unlock scale transfer | VERIFIED (WebSearch this session: Google Books, PSU thesis) |
| Dimensional analysis + Quality-by-Design (pharma), PMC12301016 | Organises a design space with Π-groups | No — uses fixed Π structure; does not add a column to release a lone constant | VERIFIED (WebSearch listing this session) |
| "Inverse dimensional analysis" / dimensional synthesis (four-bar kinematics, arXiv:2507.08269) | Solves for parameter **values** from a target motion | No — "inverse" = fit values within a fixed Π structure, not add a new dimension-carrier | VERIFIED (WebSearch this session) |
| Contact splitting: Arzt, Gorb, Spolenak, *PNAS* 100(19):10603 (2003) | The biomimetic fix the operator **reproduces** | It is the *answer*, not the operator | VERIFIED (EuropePMC abstract, fetched this session) |
| JKR pull-off `F_c = (3/2)π w R` | The physics the gecko matrix encodes | — | VERIFIED (arXiv:2407.00378, fetched this session) |

**Verdict on novelty.** The mechanical step — augmenting a dimension matrix with a column and
re-reading its kernel — is **textbook** (Szirtes does exactly this augmentation, for a different
purpose). Claim nothing there. What appears **absent** in the searched literature: using that
augmentation as a **directed, computable operator** that (a) decides constant-boundedness of a
target group under scaling, (b) emits the finite set of dimensional signatures that would release
each lone constant, and (c) is validated by **re-deriving a known biomimetic solution** (contact
splitting) blind. That combination is the genuinely new piece. It rests on ~a dozen searches, not a
systematic review, so state it as **underexplored, not first** — and note it is not a discovery but
*methodology packaging on 111-year-old machinery*, exactly the honest framing G22 §"Status" demands.

---

See [[specification-instruments]]: conserved object = integer kernel of the dimension matrix;
enumeration = the finite family of releasing signatures; deliverable = for each lone constant, the
exact dimension a new quantity must carry to unlock it. Ties [[M6-vary-what-was-held-fixed]] (the
prose move), [[C12-pi-space-lattice]] (the lattice-lock reading), and
[[G22-scale-transfer-triage]] (the triage) through one operator.
