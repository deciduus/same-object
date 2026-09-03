---
name: C15-metastability-metric
type: computed
---

# The metastability figure of merit does not exist as a single number. The prefactor kills it, exactly as C9 killed the moving-coupling advantage.

> **The candidate figure of merit `M = ρ_E · ln(τ/τ_op)` is built on `τ = τ₀ · exp(ΔG/kT)`, and that
> exponential is not shared across the classes [[G2-metastability-metric]] names. It fails in the
> PREFACTOR, and it fails there in two independent, fatal ways.**
>
> Backing out `τ₀` from real `(E_a, τ)` pairs — the whole crux — gives a spread of **~20 orders of
> magnitude** and, worse, two of the five classes do not live in the `exp(ΔG/kT)` form *at all*:
>
> | Class | governing barrier | backed-out / physical `τ₀` | does `exp(ΔG/kT)` apply? |
> |---|---|---|---|
> | MOST / chemistry (energetic materials) | `E_a ≈ 110–130 kJ/mol` | **~10⁻¹² – 10⁻¹³ s** (transition-state `h/kT`) | yes |
> | Biological dormancy (seeds) | `E_a ≈ 55 kJ/mol` | **~10⁻² – 10⁻¹ s** (backed out below) | approximately, but `τ₀` is macroscopic |
> | Phase-change material (PCM) | `E_a(T)`, **temperature-dependent** | undefined — no fixed point | **NO — non-Arrhenius / VFT** |
> | Nuclear isomers (Hf-178m2, Ta-180m) | spin / K-forbiddenness, **no `kT`** | **~10⁻²² s** (single-particle nuclear time) | **NO — no thermal `kT` in it** |
>
> The chemistry prefactor is a phonon/TST period; the seed prefactor is ~10¹¹× larger; the nuclear
> "prefactor" is ~10⁹× *smaller* and is not thermal at all; the PCM barrier is not even a constant.
> **A single `M` requires one shared exponential with one universal `τ₀`. There is none.** The barrier
> `ΔG` alone does not determine the lifetime, so no dimensionless number built on it can span the classes.
>
> **The honest object is at best a 2-D `(ΔG, ln τ₀)` map — and even that only holds the two
> thermally-activated classes (chemistry + biological dormancy).** Nuclear isomers and PCM do not embed
> in the plane: one has no `kT`, the other has no point (its `ΔG` is a curve in `T`). So the map is
> mildly informative *within* the Arrhenius subset — it separates chemistry (`τ₀ ~ 10⁻¹³ s`) from
> dormancy (`τ₀ ~ 10⁻² s`) cleanly by prefactor — and **uninformative as a five-class unifier.**
>
> This is a clean negative in the mould of [[C9-moving-coupling-point]]: the unifying arithmetic looked
> promising, and the apparent unification was a bookkeeping illusion that dies when the hidden term
> (`τ₀`, as `q'` there) is put back with real numbers. And it is the [[specification-instruments]]
> discipline applied honestly — the residual is a *specification of what a real shared axis would need*
> (one exponential, one prefactor physics), which the classes demonstrably do not satisfy.

Bears on [[G2-metastability-metric]], [[specification-instruments]], [[C9-moving-coupling-point]].

---

## 1. The candidate figure of merit, stated precisely

The natural object is two-dimensional: an **energy density** `ρ_E` and a **barrier-set lifetime** `τ`.

```
ρ_E   [J kg⁻¹]           extractable stored energy per unit mass
τ  =  τ₀ · exp(ΔG / kT)  [s]   Arrhenius/Kramers lifetime against the escape barrier ΔG
```

To collapse them to one dimensionless number one must pick an **operational timescale** `τ_op` (the
time the store must survive) and write, e.g.,

```
M  =  ρ_E · ln(τ / τ_op)  =  ρ_E · [ ΔG/kT + ln(τ₀/τ_op) ]                         (FoM-A)
```

or the equivalent "energy density at a fixed lifetime" form, `ρ_E` evaluated on the contour
`τ = τ_op`. Either way **the lifetime enters only through `ln τ = ΔG/kT + ln τ₀`.** The whole
construction rests on the claim that this logarithm is a shared, well-defined quantity across classes.
It is not. The `ΔG/kT` term is the one the note's "every ~6 kJ/mol buys 10×" arithmetic keeps
(`ln10·kT ≈ 5.9 kJ/mol` at 298 K — correct); the `ln τ₀` term is the one it silently drops. §2 shows
`ln τ₀` is where all the disagreement lives, and for two classes the whole form `exp(ΔG/kT)` is invalid.

A second, deeper problem sits in the numerator and is worth stating once: **the five classes do not even
share `ρ_E`.** Nuclear isomers store ~10⁹ J g⁻¹ (nuclear), chemistry stores ~10² – 10³ J g⁻¹
(molecular bonds), and seeds store *no extractable energy at all* — the conserved quantity there is
viability / genome integrity, not work. So `ρ_E` is not one axis either; the premise "each class has both
numbers" is already strained. But the lifetime axis is the sharper kill, so the rest of this note lives there.

## 2. The prefactor cross-class check — the crux, with real numbers

`τ = τ₀ exp(ΔG/kT)` has two parameters. The note's arithmetic assumes `τ₀ ≈` a phonon period
`~10⁻¹³ s` universally. Back it out class by class.

### 2.1 Biological dormancy (seeds) — `τ₀ ~ 10⁻² s`, ELEVEN orders above a phonon

From [[G2-metastability-metric]] / **PMC6613187** (Fleming, Hill & Walters, *Ann. Bot.* 2019,
read in full in the vault; [https://pmc.ncbi.nlm.nih.gov/articles/PMC6613187/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6613187/)):
`E_a ≈ 55 kJ/mol` for germination loss, P50 lifetimes **9.9 yr (onion) to 51.9 yr (pea)**. Invert
`τ₀ = τ / exp(E_a/RT)` (computed this session):

```
onion, E_a=55 kJ/mol, τ=9.9 yr:   τ₀ = 1.4×10⁻² s (278K) … 4.9×10⁻² s (293K) … 2.1×10⁻¹ s (313K)
pea,   E_a=55 kJ/mol, τ=51.9 yr:  τ₀ = 2.6×10⁻¹ s (293K)
```

**The seed prefactor is `~10⁻² – 10⁻¹ s` — macroscopic, ~10¹¹ times a phonon period.** Equivalently,
if you *impose* the phonon `τ₀ = 10⁻¹³ s`, a 9.9-yr lifetime demands `E_a = 120.6 kJ/mol`, not 55.
That is exactly the "rule predicts ~100 kJ/mol for a year, biology reports ~55" mismatch the note
flagged — and it is now located: **it lives entirely in a `τ₀` that is 11 orders of magnitude off.**
Physically this large effective prefactor is the signature of a *cooperative* escape (relaxation of the
whole cytoplasmic glass, not one bond vibrating) — which ties dormancy to the PCM glass physics below.
`VERIFIED` (E_a, P50 from PMC6613187, in vault full-text; `τ₀` arithmetic this session).

### 2.2 Chemistry — MOST / energetic materials — `τ₀ ~ 10⁻¹³ s` (a real phonon/TST period)

Norbornadiene→quadricyclane (QC) MOST pair: QC half-life **587 h at 371 K**, storage
**≈ 65 kJ/mol**
([https://pubs.rsc.org/en/content/articlelanding/2022/cp/d2cp03032b](https://pubs.rsc.org/en/content/articlelanding/2022/cp/d2cp03032b),
search-snippet `VERIFIED`; note the [[G2-metastability-metric]] photoswitch **559 kJ/kg / 48.5 d** is the same class).
The back-reaction barrier for QC systems is `E_a ≈ 110–130 kJ/mol`. Back out `τ₀`:

```
τ = 587 h = 2.11×10⁶ s at 371 K:
  E_a=110 kJ/mol → τ₀ = 6.9×10⁻¹⁰ s
  E_a=120 kJ/mol → τ₀ = 2.7×10⁻¹¹ s
  E_a=130 kJ/mol → τ₀ = 1.0×10⁻¹² s
transition-state theory universal prefactor h/kT = 1.3×10⁻¹³ s (371K),  1.6×10⁻¹³ s (298K)
```

**Chemistry sits at `τ₀ ≈ 10⁻¹² – 10⁻¹³ s`, i.e. the TST `h/kT` period** — the *only* class where the
note's phonon assumption is roughly right, because it is derivable there (Eyring). This is the class the
naive rule was implicitly built for. `E_a` value `UNVERIFIED` (typical NBD/QC range; the half-life and
storage energy are `VERIFIED`); the point is insensitive to which value in 110–130 — all give `τ₀`
within ~3 orders of a phonon, versus 11 for seeds.

### 2.3 Phase-change material (PCM) — the barrier is not a constant, so `exp(ΔG/kT)` is ill-posed

Fragile glass-forming PCMs crystallise **non-Arrhenius**; the standard description is
**Vogel–Fulcher–Tammann (VFT)**, `η ∝ exp[B/(T−T₀)]`, with a viscosity that diverges at a finite
Vogel temperature `T₀ ≈ 0.77 T_g`. Crucially, "for fragile liquids the temperature-dependent activation
energy barrier can **increase several-fold as the temperature is lowered**"
([https://pubs.rsc.org/en/content/articlelanding/2015/... VFT crystallisation kinetics] and the
fragility literature, e.g. [https://arxiv.org/abs/2009.07742](https://arxiv.org/abs/2009.07742);
search-snippet `VERIFIED`, primary PDFs are binary-encoded and not extractable this session — marked
accordingly). **There is no single `ΔG` to put in `M`.** The lifetime is a VFT curve, not a point on an
Arrhenius line; forcing an "effective `E_a`" makes `τ₀` a fitting artefact that changes with the
temperature window. The exponential the whole FoM rests on does not exist for this class.

### 2.4 Nuclear isomers — no `kT` at all; `τ₀ ~ 10⁻²² s`, set by nuclear matrix elements

Two real long-lived isomers:

- **Hf-178m2**: `Kπ = 16⁺`, excitation **2.446 MeV**, half-life **31 yr** (≈ 9.8×10⁸ s), specific energy
  **~1.3 GJ/g** ([search snippets from OSTI / arXiv nucl-th/0405051]; `VERIFIED` via search).
- **Ta-180m**: spin 9⁻, excitation **~75 keV**, half-life **> 10¹⁵ yr** (decay never observed; the only
  naturally-occurring nuclear isomer) ([https://arxiv.org/abs/2205.10534](https://arxiv.org/abs/2205.10534),
  [https://arxiv.org/abs/2111.11497](https://arxiv.org/abs/2111.11497); `VERIFIED` via search).

The lifetime here is **not** `τ₀ exp(ΔG/kT)`. There is no `kT`: isomer decay is essentially
temperature-independent. The "barrier" is a **selection rule** — K-forbiddenness (`ΔK` large) and
angular-momentum mismatch (`ΔI = 8`) — and the suppression is a *hindrance factor* on a nuclear
transition whose unhindered rate is `~10⁻²² s` (a single-particle/Weisskopf time; the field's own phrasing
is that an allowed transition "would take place in ~10⁻²² s" while K-conservation stretches Hf to ~10⁹ s).
So the nuclear "prefactor" is ~10²² times *smaller* than a phonon, and the exponent is not thermal.
**This class cannot be placed on any `ΔG/kT` axis.** `VERIFIED` (energies, spins, half-lives via search).

### 2.5 The spread, tabulated

```
class                τ₀ (backed out / physical)   exponent physics            embeds in exp(ΔG/kT)?
nuclear isomer       ~10⁻²² s                     K-/spin-forbiddenness, no kT   NO
chemistry / MOST     ~10⁻¹³ s (TST h/kT)          bond rearrangement, thermal    YES
biological dormancy  ~10⁻² s                      cooperative glass relaxation   ~ (τ₀ anomalous)
PCM (fragile)        undefined (E_a is E_a(T))    VFT, super-Arrhenius           NO
```

`τ₀` spans **~20 orders of magnitude** among the classes that *do* have one, and it is not derivable
from a shared physics — TST fixes it for chemistry, a nuclear matrix element fixes it for isomers, a
cooperative length-scale inflates it for the glassy classes. **The barrier `ΔG` therefore does not
determine `τ`, and no single number built on `exp(ΔG/kT)` can span the classes.** Single FoM: dead.

## 3. The escape — is there an honest 2-D object?

Following [[C12-pi-space-lattice]]'s pattern (when a 1-D number fails, look for a region/lattice), plot
each class in the `(ΔG, ln τ₀)` plane instead of collapsing to one axis. With the real numbers:

```
ln τ₀ (s)
  +0   ┤                                   ● seeds/dormancy  (E_a≈55 kJ/mol, τ₀~10⁻¹·⁵)
       │
 -10   ┤
       │
 -30   ┤              ● chemistry/MOST      (E_a≈110–130 kJ/mol, τ₀~10⁻¹³, the TST line)
       │
 -50   ┤  ● nuclear   (only if forced; there is no kT axis — placed for contrast only)
       └───────────────────────────────────────────────────  ΔG →
```

Two facts decide whether this 2-D map is the honest shared object:

1. **The thermally-activated subset does separate cleanly.** Chemistry clusters on the TST line
   `ln τ₀ ≈ −30` (`10⁻¹³ s`); biological dormancy sits ~25 natural-log units higher
   (`τ₀ ~ 10⁻² s`) because its escape is cooperative. That vertical separation *is* a real, computable
   statement: **the prefactor, not the barrier, is what distinguishes a decades-stable seed
   (`E_a` only 55 kJ/mol) from a chemistry store needing 110–130 kJ/mol for far shorter lifetimes.**
   Within {chemistry, dormancy} the `(ΔG, ln τ₀)` map is the honest object, and it carries the finding.

2. **Nuclear isomers and PCM do not embed.** The nuclear point has no `kT`, so its abscissa `ΔG/kT`
   is meaningless — its lifetime is set on a different physical axis (forbiddenness) entirely. PCM has
   no single point at all — it is a VFT *curve*, `ΔG = ΔG(T)`. Placing either on the plane is a category
   error, the same kind [[C9-moving-coupling-point]] caught when the Schur-complement "gain" turned out
   to be advected heat counted twice.

So the 2-D map is **not** a five-class unifier. It is a two-class prefactor diagram. That is genuinely
informative — it names the prefactor as the missing coordinate the note suspected — but it does not
close G2 as posed.

## 4. Verdict

**A single figure of merit does NOT close G2. It fails, and it fails in the prefactor, exactly where
[[G2-metastability-metric]] predicted.** The escape to a 2-D `(ΔG, ln τ₀)` map is only *partially*
successful: it is the honest shared object for the two thermally-activated classes (chemistry and
biological dormancy), where it cleanly attributes their lifetime difference to a `~10¹¹×` prefactor gap
rather than to the barrier — but it is **uninformative across all five**, because nuclear isomers carry
no `kT` and PCMs carry no fixed `ΔG`, so neither embeds in the plane.

Restating against the note's three offered outcomes: the naive exponential FoM **fails** (outcome:
2-D map); the 2-D map is **informative only within the Arrhenius subset**. The deep reason is the one
[[specification-instruments]] would extract as the residual specification: *a shared axis would require
one exponential law with one prefactor physics*, and the five classes demonstrably instantiate three
different physics for `τ₀` (nuclear matrix element `10⁻²²` s, TST `10⁻¹³` s, cooperative-glass `10⁻²` s)
plus one class (PCM) with no constant barrier. The axis is missing **because it is not constructible from
a shared exponential**, not because anyone overlooked it — a better gap, and a clean negative in the
[[C9-moving-coupling-point]] mould.

**What survives as worth something.** One computable statement: *for thermally-activated metastable
stores, the prefactor `τ₀` — not the barrier `ΔG` — is the discriminating coordinate, and it separates
chemistry (`τ₀ ≈ h/kT ≈ 10⁻¹³ s`, derivable) from biological dormancy (`τ₀ ≈ 10⁻² s`, cooperative) by
~11 orders of magnitude.* That is why a 55-kJ/mol seed outlives a 120-kJ/mol chemical store: biology
buys lifetime in the prefactor, chemistry in the barrier. Everything else in G2's premise — one `ρ_E`,
one `τ`, one `M` — does not hold.

## 5. Status

- **§2.1 seed `τ₀` arithmetic:** `E_a`, P50 `VERIFIED` (PMC6613187, vault full-text); inversion this session.
- **§2.2 MOST:** half-life 587 h @ 371 K and 65 kJ/mol storage `VERIFIED` (RSC d2cp03032b snippet);
  back-reaction `E_a` 110–130 kJ/mol `UNVERIFIED` (typical range) — conclusion insensitive within it.
- **§2.3 PCM non-Arrhenius / VFT:** `VERIFIED` via search snippets; primary arXiv PDFs (2009.07742) were
  binary-encoded and not text-extractable this session — no number is quoted from them beyond the
  qualitative non-Arrhenius statement.
- **§2.4 nuclear isomers:** Hf-178m2 (2.446 MeV, 31 yr, Kπ16⁺, ~1.3 GJ/g) and Ta-180m (~75 keV, >10¹⁵ yr)
  `VERIFIED` via search (OSTI, arXiv 2205.10534, 2111.11497). The `~10⁻²²` s unhindered time is the
  field's own Weisskopf statement, `VERIFIED` via snippet.
- **What would overturn this.** A single physical law deriving `τ₀` for all classes from one quantity
  (there is none: TST, nuclear matrix elements, and cooperative-glass length scales are unrelated), or a
  reformulation of nuclear-isomer lifetime and PCM crystallisation as genuine `exp(ΔG/kT)` processes with
  a constant barrier (both are explicitly not — no `kT`, and `ΔG(T)` respectively).

See [[G2-metastability-metric]], [[specification-instruments]], [[C9-moving-coupling-point]].
