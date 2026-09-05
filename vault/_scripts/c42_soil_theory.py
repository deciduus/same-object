#!/usr/bin/env python3
"""
c42_soil_theory.py - the arithmetic behind vault/computed/C42-soil-ha-theory.md.

    python c42_soil_theory.py        # no network

WHAT THIS COMPUTES
------------------
The soil-depth balance

    dD/dt = P(D) - E ,        P(D) = P0 * exp(-D/Dstar)                       (1)

with E treated as exogenous (set by slope, rainfall erosivity and cover, not by D
except through the cover feedback of section 3c).

  * Steady state.  P(D_ss) = E  =>  D_ss = Dstar * ln(P0/E), which EXISTS ONLY IF
    E < P0.  d/dD [P(D)-E] = -(P0/Dstar) e^{-D/Dstar} < 0 everywhere, so whenever
    the fixed point exists it is globally asymptotically stable on D >= 0.
    If E >= P0 the RHS of (1) is negative for every D >= 0: no fixed point, and
    the profile runs monotonically to bedrock.

  * Time to bedrock, exact for (1), integrating dt = dD/(E - P(D)) from 0 to D0:

        t_bed = D0/E + (Dstar/E) * ln( (E - P0*exp(-D0/Dstar)) / (E - P0) )    (2)

    (differentiating (2) returns 1/(E - P0 e^{-D0/Dstar}); checked by check_t_bed()).
    Requires E > P0.  As Dstar -> 0 (or P0 -> 0) (2) collapses to D0/E.

  * Evans et al. 2020 soil lifespan, L = D0/(E - F) with F a CONSTANT formation
    rate.  This is (2)'s first-order cousin and the number policy actually quotes.

PARAMETERS AND THEIR PROVENANCE
-------------------------------
D0     = 300 mm      the 0.3 m surface horizon Evans et al. 2020 use, chosen for
                     nutrient/organic-matter enrichment; matches FAO/IPCC usage.
P0     = 0.077 mm/yr Heimsath et al. 1997, Nature 388:358, DOI 10.1038/41056,
                     Tennessee Valley CA: bare-bedrock soil production.
Dstar  = 434 mm      from the same study's reported decline 0.077 -> 0.0077 mm/yr
                     under 1 m of soil: Dstar = 1000/ln(10) = 434.3 mm.
                     VERIFIED-SECONDARY (Crossref-verified record; the two rate
                     endpoints are from secondary summaries, not the Nature PDF).
F_med  = 0.017 mm/yr Montgomery 2007 Table 1 soil-production median (n=188),
                     the k_r of C35.  NOTE it is ~2.3x SMALLER than P(300mm)
                     under Heimsath's parameters -- see section 4 of the note.
rho_b  = 1300 kg/m3  ASSUMED, inherited from C35 section 1.
"""
import sys

D0_MM   = 300.0
P0      = 0.077
DSTAR   = 1000.0 / __import__("math").log(10.0)   # 434.294 mm
F_MED   = 0.017          # Montgomery 2007 Table 1 median soil production
F_MEAN  = 0.036
RHO_B   = 1300.0
T_ACRE_TO_HA = 2.2417    # short ton/acre -> t/ha

import math


def depth_from_mass(t_per_ha_yr, rho_b=RHO_B):
    """t/ha/yr -> mm/yr (C35 section 1)."""
    return t_per_ha_yr * 100.0 / rho_b


def P(D, P0=P0, Dstar=DSTAR):
    """Heimsath exponential soil production function, mm/yr."""
    return P0 * math.exp(-D / Dstar)


def steady_state(E, P0=P0, Dstar=DSTAR):
    """D_ss solving P(D_ss)=E, or None if E >= P0 (no interior fixed point)."""
    if E >= P0:
        return None
    return Dstar * math.log(P0 / E)


def lifespan_evans(E, F, D0=D0_MM):
    """Evans et al. 2020 ERL 15:0940b2 lifespan L = D/(E-F), yr. None if E<=F."""
    return None if E <= F else D0 / (E - F)


def t_bedrock(E, D0=D0_MM, P0=P0, Dstar=DSTAR):
    """Exact time to strip D0 to bedrock under (1). None if E <= P0."""
    if E <= P0:
        return None
    num = E - P0 * math.exp(-D0 / Dstar)
    return D0 / E + (Dstar / E) * math.log(num / (E - P0))


def check_t_bed(E=1.537, D0=D0_MM, h=1e-4):
    """Numerical check that d(t_bed)/dD0 = 1/(E - P(D0))."""
    d = (t_bedrock(E, D0 + h) - t_bedrock(E, D0 - h)) / (2 * h)
    return d, 1.0 / (E - P(D0))


ROWS = [
    # label,                              E mm/yr,          F for Evans lifespan
    ("Conventional agriculture (median)", 1.537,            F_MED),
    ("Conventional agriculture, 1.5 rnd", 1.5,              F_MED),
    ("Conventional agriculture (mean)",   3.939,            F_MEAN),
    ("Global mean (Borrelli 2.8 t/ha/yr)", depth_from_mass(2.8), F_MED),
    ("USDA T = 5 short ton/ac/yr",        depth_from_mass(5 * T_ACRE_TO_HA), F_MED),
    ("USDA T = 1 short ton/ac/yr",        depth_from_mass(1 * T_ACRE_TO_HA), F_MED),
    ("No-till / conservation (median)",   0.082,            F_MED),
    ("Native vegetation (median)",        0.013,            F_MED),
]


def rho_sensitivity(rho_lo=1100.0, rho_hi=1600.0):
    """Ha for the T-rows scales linearly with rho_b (mass-derived k_d only)."""
    out = []
    for tons in (1, 5):
        for rho in (rho_lo, RHO_B, rho_hi):
            kd = depth_from_mass(tons * T_ACRE_TO_HA, rho)
            out.append((tons, rho, kd, F_MED / kd, kd / F_MED))
    return out


def main(argv=()):
    print("c42_soil_theory.py -- soil as a stock, not a repairable unit\n")
    print(f"P0 = {P0} mm/yr, Dstar = {DSTAR:.1f} mm, D0 = {D0_MM:.0f} mm")
    print(f"P(D0) = {P(D0_MM):.4f} mm/yr   vs Montgomery median F = {F_MED} mm/yr"
          f"   (ratio {P(D0_MM)/F_MED:.2f})\n")

    d, a = check_t_bed()
    print(f"check dt/dD0: numeric {d:.6f}  analytic {a:.6f}  "
          f"(agree to {abs(d-a):.2e})\n")

    hdr = (f"{'system':38s} {'E mm/yr':>9s} {'Ha=F/E':>8s} {'A=Ha/(1+Ha)':>12s} "
           f"{'D_ss mm':>9s} {'L Evans yr':>11s} {'t_bed yr':>10s}")
    print(hdr)
    print("-" * len(hdr))
    for label, E, F in ROWS:
        Ha = F / E
        A = Ha / (1.0 + Ha)
        dss = steady_state(E)
        L = lifespan_evans(E, F)
        tb = t_bedrock(E)
        print(f"{label:38s} {E:9.4f} {Ha:8.4f} {A:12.4f} "
              f"{('--' if dss is None else f'{dss:9.0f}'):>9s} "
              f"{('thicken' if L is None else f'{L:11.0f}'):>11s} "
              f"{('none' if tb is None else f'{tb:10.0f}'):>10s}")

    print("\nD_ss '--' means E >= P0: no steady state, the profile runs to bedrock.")
    print("t_bed 'none' means E <= P0: bedrock is never reached.\n")

    print("Bulk-density sensitivity on the T rows (Ha and T/k_r scale with rho_b):")
    print(f"{'T ton/ac':>9s} {'rho_b':>7s} {'k_d mm/yr':>10s} {'Ha':>8s} {'T/k_r':>8s}")
    for tons, rho, kd, Ha, ratio in rho_sensitivity():
        print(f"{tons:9d} {rho:7.0f} {kd:10.4f} {Ha:8.4f} {ratio:8.1f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
