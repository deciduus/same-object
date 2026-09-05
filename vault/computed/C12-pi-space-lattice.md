---
name: C12-pi-space-lattice
type: computed
---

# The co-located Π-space is the integer kernel of one dimension matrix, and its crossovers are half-locked

> **The single Π-space that [[G21-dimensionless-regime-map]] says is absent is constructible in
> ten minutes of integer arithmetic.** Put organism-locomotion quantities (length, speed, gravity,
> mass, metabolic rate) and molecular-process quantities (diffusion, thermal diffusivity, kinematic
> viscosity, a reaction rate, a motor speed) into one 3×10 dimension matrix `D`. Its integer kernel
> is a rank-7 lattice, and **Froude, Reynolds, Péclet, Damköhler are all integer vectors in that one
> kernel**. Reading the crossovers against each other: the transport crossovers (Re=1, Pe=1, Pe_th=1)
> are **parallel lines** in the (log L, log v) plane, offset by material constants (Schmidt, Prandtl,
> Lewis). **The reason is elementary and should be said plainly: ν, D and α all have the dimension
> L²T⁻¹, so all three groups have the form `vL/(L²T⁻¹)` and all three crossover lines have slope −1.**
> No lattice machinery is needed to see it. The Froude family crosses them **transversally**. The
> parallelism can be *restated* in G22's constant-bound vocabulary (§5), but that restatement is a
> definition, not a derived criterion. And the one place a Froude and a Péclet transition coincide
> sits at L≈0.9 µm, v≈1.2 mm/s, where Re≈10⁻³ — a corner no organism occupies and where Froude is
> not a live boundary. So co-location closes the "space does not exist" half of G21 by construction,
> and its payload is the lock structure, not a coincident-transition organism.

Instrument in the sense of [[specification-instruments]]: the conserved object is the **integer kernel
of a dimension matrix** (Buckingham's theorem *is* linear algebra over ℤ), the finite enumeration is
the chosen quantity set, and the deliverable is a lattice with named sublattices. Discrete-math core:
integer row reduction; the Smith normal form is computed in §3.3 and is diag(1,1,1) — a certificate
of integrality, not the engine of any result here.

---

## 1. The quantities — deliberately mixing both worlds

Base dimensions M (mass), L (length), T (time). Thermal effects are carried as diffusivities
(L²T⁻¹) so no Θ row is needed. Ten quantities, five organism-scale and five process-scale:

| # | Symbol | Quantity | World | Dimension |
|---|---|---|---|---|
| 1 | `L` | body length | organism | L |
| 2 | `v` | locomotion speed | organism | L T⁻¹ |
| 3 | `g` | gravitational acceleration | organism | L T⁻² |
| 4 | `ν` | kinematic viscosity | shared/fluid | L² T⁻¹ |
| 5 | `D` | molecular diffusion coefficient | process | L² T⁻¹ |
| 6 | `k` | first-order reaction/transport rate | process | T⁻¹ |
| 7 | `u` | molecular-motor speed | process | L T⁻¹ |
| 8 | `α` | thermal diffusivity | process | L² T⁻¹ |
| 9 | `m` | body mass | organism | M |
| 10 | `B` | metabolic rate (power) | organism | M L² T⁻³ |

## 2. The dimension matrix

Columns in the order `[L, v, g, ν, D, k, u, α, m, B]`; rows `[M, L, T]`. Entry = integer power.

```
        L   v   g   ν   D   k   u   α   m   B
  M  [  0   0   0   0   0   0   0   0   1   1 ]
  L  [  1   1   1   2   2   0   1   2   0   2 ]
  T  [  0  -1  -2  -1  -1  -1  -1  -1   0  -3 ]
```

**Buckingham count.** 10 quantities − rank(D) independent Π-groups. Rank is computed below and is 3,
so there are **10 − 3 = 7** independent dimensionless groups.

## 3. Integer row reduction — the kernel, with the arithmetic

Reorder the rows to `[L, T, M]` and reduce with **integer (±1) elementary operations only** — that is
what makes the kernel a ℤ-lattice rather than a ℚ-space (Smith-normal-form guarantee, §3.3).

**3.1 Pivots.**

Start:
```
R_L = [ 1  1  1  2  2  0  1  2  0  2 ]
R_T = [ 0 -1 -2 -1 -1 -1 -1 -1  0 -3 ]
R_M = [ 0  0  0  0  0  0  0  0  1  1 ]
```
Column 1 (`L`): `R_L` already has pivot 1; `R_T`, `R_M` are 0 there. Keep.

Column 2 (`v`): scale `R_T` by −1 → `R_T' = [0 1 2 1 1 1 1 1 0 3]` (unimodular, −1). Clear column 2
from `R_L`:  `R_L ← R_L − 1·R_T'`:
```
R_L' = [ 1  0  -1  1  1  -1  0  1  0  -1 ]
```
Column 9 (`m`): `R_M` has pivot 1; `R_L'`, `R_T'` are 0 there. Keep.

**Reduced rows (pivots in columns 1, 2, 9, all equal to +1):**
```
  (L) [ 1  0  -1   1   1  -1   0   1   0  -1 ]
  (v) [ 0  1   2   1   1   1   1   1   0   3 ]
  (m) [ 0  0   0   0   0   0   0   0   1   1 ]
```
Three nonzero pivot rows ⇒ **rank(D) = 3**, confirming 7 Π-groups.

**3.2 Kernel basis.** Pivot columns `{L, v, m}`; free columns `{g, ν, D, k, u, α, B}` (seven — the
Π-count). For a kernel vector `x` over `[L,v,g,ν,D,k,u,α,m,B]`, the three rows read:

```
(L):  L  =  g − ν − D + k − α + B
(v):  v  = −2g − ν − D − k − u − α − 3B
(m):  m  = −B
```

Set each free variable to 1 in turn (others 0) and solve the pivots. The seven basis vectors, written
as the dimensionless groups they name (with repeating variables L, v, m):

| Basis | free var =1 | (L, v, m) solve | Π-group | Named number |
|---|---|---|---|---|
| Π₁ | g | (1, −2, 0) | `gL / v²` | **1/Froude** |
| Π₂ | ν | (−1, −1, 0) | `ν / (vL)` | **1/Reynolds** |
| Π₃ | D | (−1, −1, 0) | `D / (vL)` | **1/Péclet** |
| Π₄ | α | (−1, −1, 0) | `α / (vL)` | **1/Péclet (thermal)** |
| Π₅ | k | (1, −1, 0) | `kL / v` | **Damköhler** (Da_I) |
| Π₆ | u | (0, −1, 0) | `u / v` | motor/locomotion speed ratio |
| Π₇ | B | (1, −3, −1) | `BL / (m v³)` | metabolic power coefficient |

Each row's group is dimensionless by construction; e.g. Π₇ = `BL/(mv³)`: `BL = M L³T⁻³`,
`m v³ = M L³T⁻³`. ✓

**3.3 Smith normal form — now actually computed.** *(Previously this section asserted the SNF
without computing it; see Corrections 2026-09-05.)*

Computed this session (Python 3, stdlib `fractions`/integer arithmetic, no library SNF routine):
the standard SNF algorithm applied to `D` (rows `[M, L, T]`, columns `[L, v, g, ν, D, k, u, α, m, B]`)
returns

```
SNF(D) = diag(1, 1, 1) | 0_{3x7}         invariant factors (1, 1, 1),  rank 3
```

with unimodular `U` (3×3) and `V` (10×10) satisfying `U·D·V = SNF(D)` — verified by explicit matrix
multiplication in the same script; `U = ((1,0,0), (0,1,0), (0,−1,−1))`, `det U = −1`.

Two consequences: (i) the kernel is a **free ℤ-module of rank 7**, so a canonical basis exists with
**integer** entries (no fractional exponents anywhere above); (ii) *any* dimensionless group is an
integer combination of Π₁…Π₇.

**How much this buys — honestly: very little.** The invariant factors being all 1 is the generic
case for a dimension matrix whose entries are small integers with a ±1 pivot available; it certifies
integrality, nothing more. It does **not** produce the parallel-crossover result of §5, which follows
from ν, D and α sharing the dimension L²T⁻¹ and needs no normal form at all. The SNF is retained
here as a computed footnote, not as the load-bearing apparatus the first draft implied.

## 4. The known groups are integer vectors in this one kernel — the key check

Writing each named number as its exponent vector over `[L,v,g,ν,D,k,u,α,m,B]` and matching against §3.2:

| Number | Definition | Exponent vector | In kernel as |
|---|---|---|---|
| **Froude** | `v²/(gL)` | (−1, 2, −1, 0,…) | −Π₁ |
| **Reynolds** | `vL/ν` | (1, 1, 0, −1, 0,…) | −Π₂ |
| **Péclet** | `vL/D` | (1, 1, 0, 0, −1, 0,…) | −Π₃ |
| **Damköhler** | `kL/v` | (−1, 1, 0,0,0, 1, 0,…) | +Π₅ |

Negation preserves integrality, so each is a legitimate integer kernel vector. **Froude and Péclet are
both integer vectors in the kernel of the same matrix.** That is the literal statement G21 says does
not exist: organisms (Froude, via g, L, v) and processes (Péclet, via D) co-located on shared
dimensionless axes. The space is not missing — it was simply never written down as the kernel it is.

Derived material numbers fall out as **differences** of basis vectors (no free-parameter support):

- **Schmidt** `Sc = ν/D = Pe/Re = Π₃ − Π₂`
- **Prandtl** `Pr = ν/α = Π₄ − Π₂`
- **Lewis** `Le = α/D = Π₃ − Π₄`

Hold that thought — those three differences are the whole story of §5.

## 5. Lattice-dependence: which crossovers are locked, which are free

Fix the material constants (g, ν, D, α, k) and use the (log L, log v) plane as the organism/process
map. Each crossover surface is a straight line there:

| Crossover | Equation | Line in (log L, log v) | Slope |
|---|---|---|---|
| Re = 1 | `vL/ν = 1` | log v = −log L + log ν | **−1** |
| Pe = 1 | `vL/D = 1` | log v = −log L + log D | **−1** |
| Pe_th = 1 | `vL/α = 1` | log v = −log L + log α | **−1** |
| Fr = Fr_c | `v²/(gL)=Fr_c` | log v = ½log L + ½log(Fr_c g) | **+½** |
| Da = 1 | `kL/v = 1` | log v = log L + log k | **+1** |

**Parallel (cannot intersect) — and the reason is one line.** Re=1, Pe=1, Pe_th=1 all have slope −1
**because ν, D and α all carry the dimension L²T⁻¹.** Each group is `vL` divided by one of them, so
each crossover reads `log v = −log L + log(that constant)`. Same dimension ⇒ same slope ⇒ parallel;
the offsets are `log ν`, `log D`, `log α`, pure material constants. So `Pe=1` sits a fixed distance
`log(ν/D) = log Sc` from `Re=1` **everywhere**, independent of the organism's L and v. An organism
cannot cross the diffusion boundary without crossing the viscous boundary displaced by exactly
`log Sc`; the two transitions are one transition shifted by a constant.

That is the whole content. It is visible directly from the dimensions table in §1 and requires
neither the kernel nor a Smith normal form.

> **Restating it in [[G22-scale-transfer-triage]]'s vocabulary — a definition, not a derived
> criterion.** G22 says a capability is *constant-bound* when the governing group "contains a fixed
> constant appearing **alone** — kT, λ, g, c — rather than in a compensable ratio." The Π-space
> phrasing is: **two crossovers are parallel iff the integer difference of their Π-vectors has
> support only on non-tunable constants** (here `Π₃ − Π₂ = Sc`, supported only on ν and D, with zero
> entries on every free parameter L, v, g, m, B). This is a *translation* of "appears alone" into
> exponent-vector language — the two phrasings are definitionally equivalent, and nothing is derived
> in passing between them. It is useful because it makes the check mechanical, not because it proves
> anything G22 did not already say.

**Free (transversal, intersect in a point).** Froude (slope +½) and Damköhler (slope +1) cross the
transport family at single points — because g (L T⁻²) and k (T⁻¹) are *not* of dimension L²T⁻¹, so
their groups do not have the `vL/(L²T⁻¹)` form. Transversal intersection means an organism *can* be
moved across one without the other — the Froude and Péclet crossovers are **independent** in a way
the Re/Pe pair is not.

## 6. Reading the crossovers against each other

Empirical transition values, provenance stated per `METHOD.md` §4:

- **Froude 0.16** (hull-speed / stern-wave crossover), **0.5–0.6** (surface-wave amplitude max),
  **2–4** (trot→gallop): carried from [[G21-dimensionless-regime-map]], Vogel *Comparative
  Biomechanics* read in full text (`evidence: full-text-read`, quoted verbatim in the gap note).
- **Pe = 1 at ~10 µm** (motor transport beats diffusion; diffusion time x²/D, motors ~1 µm/s): carried
  from G21 and `METHOD.md` §9 worked crossovers, same full-text provenance.
- No transition value is invented here; the geometry below uses only these plus textbook constants.

**Where do a Froude and a Péclet transition coincide?** Solve Fr = Fr_c together with Pe = 1:

```
Pe = 1        ⇒  v = D / L
Fr = v²/(gL)  ⇒  (D/L)² /(gL) = Fr_c  ⇒  L³ = D² /(g·Fr_c)
             ⇒  L* = ( D² / (g Fr_c) )^{1/3}
```

With D = 1×10⁻⁹ m²/s (small solute in water, order of magnitude), g = 9.81, Fr_c = 0.16
(VERIFIED arithmetic, this session): **L\* ≈ 0.86 µm, v\* ≈ 1.2 mm/s.** At that point Re = v\*L\*/ν ≈
**10⁻³** (ν = 10⁻⁶). For a cytoplasmic-protein D ≈ 10⁻¹¹ the coincidence moves to L\* ≈ 40 nm,
v\* ≈ 250 µm/s.

**Interpretation — the new object.** The Froude and Péclet crossover lines *do* meet, but the meeting
point sits at Re ≈ 10⁻³, deep in the Stokes world, where **Froude is not a live regime boundary at all**
— a micron object's weight is negligible against viscosity and thermal forcing, so "gravity vs inertia"
names nothing. Froude only becomes an operative transition at Re ≳ 0.1–1, i.e. L ≳ 0.1–1 mm; and there
`Pe = Re·Sc` with Sc ≈ 10³ in water, so Pe ≈ 10²–10³ — nowhere near its own crossover. **The
Froude-family transitions and the Péclet/Damköhler transitions occupy disjoint operative regions of the
shared plane, connected only through a corner no organism inhabits.** Co-locating them does not
manufacture an organism size at which two transitions coincide; it proves, quantitatively, that none
exists in the physically live region.

## 7. Prior art

| Source | What it did | Provenance |
|---|---|---|
| Buckingham Π as kernel of the dimension matrix | Textbook; **rank m, n−m groups, homogeneous integer system** stated explicitly across the standard references | VERIFIED (WebSearch, ScienceDirect/lecture notes, this session) |
| Kitano, *Mathematical structure of unit systems*, arXiv:1305.1291 | Π-groups **explicitly as ker T**; "standard decomposition" of the transfer matrix into `[I_M \| 0]` — i.e. Smith-normal-form reasoning. **Physics/EM only; no biology.** | VERIFIED (ar5iv full text) |
| "Dynamic duos: building blocks of dimensional mechanics", arXiv:2401.15101 | 2-D table of mechanical quantities by (length, time) exponents; ratios give scales. **Not an integer-kernel/SNF construction; not a shared Π regime map; biology is one domain among many** | VERIFIED (ar5iv full text) |
| "A Foraging Mandala for Aquatic Microorganisms", *ISME J* 2018 (Stocker group) | Co-locates dimensionless numbers (Péclet, Reynolds-class) for **aquatic microbes** on shared axes — a genuine regime map | UNVERIFIED (search summary only; Nature paywall/redirect this session) |
| Data-driven dimensionless-number discovery (e.g. arXiv:2111.03583, BuckiNet-type) | ML extraction of Π-groups from data; not a comparative-biology co-location | VERIFIED (search listing) |

**Verdict on novelty.** The integer-kernel / Smith-normal-form framing of Buckingham is **classical**
(Kitano makes it explicit; it is textbook otherwise) — claim nothing there. Co-locating transport
dimensionless numbers as a **regime map** already exists for aquatic microbes (the Foraging Mandala),
so the micro-scale Pe/Re half of the picture has been drawn. What appears **absent** in the searched
literature: (a) one dimension matrix co-locating organism-**locomotion** quantities (Froude, via g/L/v)
with molecular-**process** quantities (Péclet/Damköhler, via D/k) across scales, and (b) the
**restatement** of G22's constant-bound criterion as "the Π-difference vector is supported only on
non-tunable constants" — a notational convenience, not a derived criterion. Those two are the
candidate new pieces; both rest on ~a dozen
searches, not a systematic review, so state them as *underexplored*, not *first*.

## 8. Closes / buys — the verdict

**Closes the surviving half of G21? Yes, by construction.** G21's restated claim was that "no single
Π-space co-locates organisms and processes." Froude and Péclet are integer vectors in the kernel of one
3×10 matrix (§4). The object the gap calls absent is built. This is a *closure by construction* rather
than by discovering an unread theorem — the machinery (kernel of the dimension matrix) is 111 years old
and textbook, which is why the honest framing is: **the space was never missing, only unwritten.** That
matches [[what-closes-a-gap]]: closing needed a theorem, and Buckingham *is* the theorem; the gap
survived only as long as nobody actually formed the mixed matrix.

**What it buys, beyond closing the wording:**

1. **G22's constant-bound criterion gets a mechanical restatement — a definition, not a new result.**
   "A fixed constant appearing alone" is *by definition* "a crossover pair whose Π-difference vector
   has support only on material constants." Sc = Pe/Re is the worked case: the Re and Pe crossovers
   are parallel and offset by `log Sc` forever — **because ν and D share the dimension L²T⁻¹**, which
   is readable off §1 without any lattice. The restatement makes the triage check mechanical; it does
   not derive the criterion, and it is not what the SNF (computed in §3.3, invariant factors 1,1,1)
   buys. Claim it as a convenience of notation, not as a theorem.

2. **A negative structural result the single-group view could not see.** Because Fr and Pe live on lines
   of different slope, they *can* be independent — but the actual coincidence point (§6) lands at
   Re ≈ 10⁻³, where Froude is inert. So the shared space reveals that the Froude and Péclet transitions
   are **operatively disjoint**: no organism sits where both switch. The missing Π-space was partly
   missing because, for the Froude↔Péclet pair, **it carries no coincident-transition prediction** —
   which is itself worth knowing, and only visible once both families share a plane.

**Net:** the co-located Π-space exists and is constructible (Froude and Péclet in one kernel); the
transport family (Re, Pe, Pe_th) has parallel crossovers **because ν, D and α share the dimension
L²T⁻¹**, while the Froude/Damköhler family is transversal to them; and that parallelism can be
restated as [[G22-scale-transfer-triage]]'s constant-bound criterion in exponent-vector form — a
definitional translation, not a derivation. The Smith normal form is computed (§3.3) and is
diag(1,1,1); it certifies integrality and nothing else. Prior art covers the linear-algebra framing
and the micro-scale transport mandala, but not this organism⊕process co-location.

See [[specification-instruments]]: conserved object = integer kernel; enumeration = the quantity set;
deliverable = the lattice with its locked and free sublattices.

---

## Corrections 2026-09-05

Backlog A18; `audits/01-math-physics.md` C12 items; `audits/03-method-epistemics.md` 18.

1. **SNF asserted → SNF computed.** Old: §3.3 asserted "every pivot is ±1, so `D` is unimodularly
   equivalent to `[I₃ | 0]`" and the note leaned on "Smith normal form" as its discrete-math core,
   but **no normal form was ever computed**. New: the SNF is computed this session in Python
   (integer arithmetic, standard SNF algorithm, no library routine) from the 3×10 matrix of §2:
   **SNF(D) = diag(1, 1, 1) with a 3×7 zero block; invariant factors (1, 1, 1); rank 3**, verified
   by explicit multiplication `U·D·V = SNF(D)` with `U = ((1,0,0), (0,1,0), (0,−1,−1))`, `det U = −1`.
   The claim is therefore now backed — and correspondingly **demoted**, because all-ones invariant
   factors certify only that the kernel basis is integral.
2. **"Lattice-locked" → "parallel because ν, D and α share dimension L²T⁻¹."** Old: §5 and the
   pull-quote presented the parallelism of the Re = 1, Pe = 1, Pe_th = 1 crossovers as a "lattice
   lock", a structural fact read off the kernel. New: all three groups have the form
   `vL / (L²T⁻¹)` (inputs: §1 dimensions ν = D = α = L²T⁻¹), so all three lines are
   `log v = −log L + log(constant)` with slope −1. Parallelism follows from the dimensions table
   alone; no kernel and no normal form is involved.
3. **G22 constant-bound restatement kept, relabelled a definition.** Old: §5 and §8 called it
   G22's criterion "recovered as a kernel property" and said "the triage rule graduates from prose
   to a check on the SNF basis." New: "constant appears alone" and "the Π-difference vector has
   support only on non-tunable constants" are two phrasings of the same condition — a definitional
   translation that makes the check mechanical, deriving nothing. Kept, relabelled.
