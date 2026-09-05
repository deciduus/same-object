# Blind brief — C53: is the C49 exchange residual reachable by regolith adsorption?

Written and hashed **before** any isotherm, thermal or diffusion number was fetched.
Date: 2026-09-05. Follows the D.3a protocol as used by C49/C52 (single-agent blind).

## The quantity to compute

C49 leaves an `EXCHANGE REQUIRED` residual: a surface reservoir exchanging CH4 with the Mars
atmosphere in **both** directions at **>= 3,820 t/yr in each phase**, season-locked to the Gale
seasonal cycle 0.24 -> 0.65 ppbv, with tau_eff = 0.944 yr, i.e. 0.072 mg m^-2 day^-1 planet-wide.
C49 shows the *capacity* row survives by six orders. The open question is the **sign
alternation**: can adsorption/desorption on regolith, driven by Mars' actual surface temperature
and pressure swing, take up CH4 in one season and release it in the other at that magnitude?

Compute **Delta_M_ads**: the seasonal amplitude of the adsorbed CH4 inventory in the regolith
column that actually exchanges with the atmosphere, for a stated isotherm and a stated seasonal
temperature (and pressure) swing, over the diffusively accessible depth.

Delta_M_ads = A_aperture * integral_0^z_acc [ (dq/dT) * Delta_T(z) + (dq/dp) * Delta_p ] rho_reg dz

reported per m^2 first, then multiplied by the aperture.

## Pass condition, fixed now

**PASS iff Delta_M_ads >= 3,820 t per hemisphere-season within the diffusively accessible depth
over one season.** Report A_exchange = required / available = 3,820 t / Delta_M_ads, with the
mandatory step-5 aperture rows at 2x and 0.5x. A_exchange > 1 rules the mechanism out; an
exclusion that does not survive the 2x row is `NOT TESTED` per F7.

## Inputs I will fetch, and the fallback if unfetchable

1. **Isotherm.** Gough, Turner & Tolbert 2010, Icarus, "Methane adsorption on a martian soil
   analog: An abiogenic explanation for methane variability in the martian atmosphere",
   10.1016/j.icarus.2009.11.030 — JSC Mars-1 adsorption capacity at Mars-relevant T and p.
   Adverse counterpart: Meslin, Gough, Tolbert & Forget 2011, PSS, "Little variability of methane
   on Mars induced by adsorption in the regolith", 10.1016/j.pss.2010.09.022.
   Fallback if paywalled: verify by Crossref (DOI/title/author/journal/date) and derive a
   *bounding* isotherm from a Langmuir/Henry form pinned to any capacity number quoted in an
   open abstract or in secondary literature; label SECONDARY and carry the uncertainty forward.
2. **Nighttime near-surface enhancement mechanism.** Moores et al. 2019 GRL 10.1029/2019GL083800.
3. **Seasonal amplitude.** Webster et al. 2018 (0.24-0.65 ppbv), inherited from C49.
4. **Thermal swing.** Annual temperature amplitude at 0, 10, 50 cm for a mid-latitude site, from
   a standard Mars thermal model (Kieffer 2013 JGR-Planets, or Mellon/Kieffer thermal-inertia
   work). Fallback: compute the damping analytically from the annual skin depth,
   delta = sqrt(kappa * P / pi), with a stated thermal inertia and Delta_T(z) = Delta_T(0)
   exp(-z/delta) — clearly labelled a derivation, not a fetched profile.
5. **Accessible depth.** Knudsen/molecular diffusion of CH4 in Mars regolith over one season,
   Sizemore & Mellon 2008 Icarus 10.1016/j.icarus.2008.05.013. Fallback: compute
   z_acc = sqrt(D_eff * t_season) from a stated D_eff bracket with the bracket reported.
6. **Aperture.** Gale-like terrain area as nominal; **whole planet** and the Gale crater floor as
   the 2x / 0.5x style rows. Mars area 1.444e8 km^2 (C49).

Every number gets provider + date and a VERIFIED-PRIMARY / VERIFIED-SECONDARY / UNVERIFIED tag.

## Failure boundaries I expect, stated in advance

- **Isotherm measured at the wrong T.** Adsorption capacity is exponential in 1/T; a room- or
  200 K-measured isotherm extrapolated to a 150-250 K seasonal swing can be wrong by orders. If
  the fetched isotherm's T range does not bracket the swing, the row is `NOT TESTED`, not a pass.
- **Accessible depth set by diffusion, not by the thermal skin depth.** The annual skin depth
  (~1-2 m) and the seasonal diffusion length need not agree. The *smaller* of the two governs;
  using the larger is the way to manufacture a pass, and I state now that I will use the smaller.
- **Competition with H2O and CO2.** CH4 is a trace species at ~0.4 ppbv against a 95% CO2
  atmosphere and adsorbed H2O. Any single-component isotherm overstates CH4 loading; if the
  source gives only single-component data the result is an **upper bound** on Delta_M_ads, which
  makes a *failure* robust and a *pass* soft.
- **The aperture: whole planet vs Gale-like terrain.** C49's residual is stated planet-wide but
  the observable is one crater. Read locally, the required mass falls with the area; read
  globally, the available regolith rises with it. Both scale the same way, so the ratio is
  largely aperture-invariant — I expect this and will check it rather than assume it.
- **The C30 lesson.** Meslin 2011's published conclusion is adverse. I must not adopt their
  margin as if I computed it. Any agreement with Meslin must be an independent division of
  independently sourced numbers, or it is labelled tautological.

## What each outcome would mean

- **PASS** (Delta_M_ads >= 3,820 t): adsorption is a live candidate for the two-way reservoir and
  C49's residual is filled by a known abiotic process.
- **FAIL**: I reproduce Meslin 2011, and C49's `EXCHANGE REQUIRED` residual **tightens** — the
  seasonal signal needs a non-adsorptive two-way process (clathrate, microbial, subsurface
  transport) **or** the observable itself is a measurement artefact. The residual becomes a
  narrower specification, which is a result, not a null.
- **NOT TESTED**: named input missing; say which.
