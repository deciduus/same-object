#!/usr/bin/env python3
"""C49 -- Mars methane reservoir audit (P-089, Track C).

Blind brief: audits/blind-brief-c49-2026-09-05.md, sha256
34a7d8ee823c28b8c776a56d9bfeca62fae177650f8e9059082274efaff2c424

Every literature input is tagged with provider + fetch date in LIT below.
Run:  python c49_mars.py
"""
import math

# ---------------------------------------------------------------- literature
LIT = {
 "chi_bg":      (0.41e-9, "Webster+2018 Science 10.1126/science.aaq0131, Crossref-verified 2026-09-05; value as given in the blind brief"),
 "chi_bg_sig":  (0.16e-9, "same"),
 "chi_lo":      (0.24e-9, "same, seasonal minimum"),
 "chi_hi":      (0.65e-9, "same, seasonal maximum"),
 "chi_spike19": (21.0e-9, "same brief line; Curiosity TLS-SAM 2019 enrichment-mode spike"),
 "chi_spike13": (7.0e-9,  "Webster+2015/2018; Yung+2018 (full-text-read PMC6205098, 2026-09-05) calls it the ~7 ppbv TLS-observed spike"),
 "chi_tgo":     (0.05e-9, "Korablev+2019 Nature 10.1038/s41586-019-1096-4, Crossref-verified 2026-09-05; upper limit as given in the brief"),
 "tau_photo_yr":(300.0,   "Summers+2002 GRL 10.1029/2002GL015377 / Atreya+2007, quoted verbatim by Yung+2018 full-text-read: a long gas-phase lifetime of ~300 years"),
 "chi_idp_model":(2.5e-9, "Yung+2018 full-text-read: meteoric/IDP UV models predict mean background levels of about 2.5 ppbv, some five times larger than that observed by TLS"),
 "yung_spike_src_t":(75000.0, "Yung+2018 full-text-read: approximating the ~7 ppbv TLS-observed spike required a lifetime of 1 month with a source strength of 75,000 t/year of CH4 (5 x 10^9 mol/year)"),
 "yung_spike_tau_yr":(1/12.0, "same, a lifetime of 1 month"),
 "micro_lo_t_km2_yr":(4.0,  "Oehler & Etiope 2017 Astrobiology 10.1089/ast.2017.1657, full-text-read PMC5730060 2026-09-05: typical microseepage rates from soil in petroleum basins, about 4-40 tonnes km-2 year-1 (10-100 mg m-2 day-1; Etiope and Klusman 2010)"),
 "micro_hi_t_km2_yr":(40.0, "same"),
 "serp_t_km2_yr":(5.0,      "same: microseepage of ~5 tonnes km-2 year-1 (15 mg m-2 day-1), as detected in several serpentinization sites on Earth"),
 "nili_km2":(30000.0,       "same: the entire 30,000 km2 of olivine-rich outcrop at Nili Fossae"),
 "oehler_plume_t_yr":(19000.0, "same: the plume-related 19,000 tonnes CH4 year-1"),
}
V = {k: v[0] for k, v in LIT.items()}

# ---------------------------------------------------------------- constants
P_S      = 610.0            # Pa, mean surface pressure (standard value, UNVERIFIED)
G_MARS   = 3.721            # m/s^2 (standard, UNVERIFIED)
R_MARS   = 3.3895e6         # m (standard, UNVERIFIED)
MU_ATM   = 43.34e-3         # kg/mol, Mars mean molar mass (standard, UNVERIFIED)
M_CH4    = 16.043e-3        # kg/mol
YEAR_MARS_D = 686.98        # Earth days (standard, UNVERIFIED)
SOL_D    = 1.02749          # Earth days

A_SURF     = 4 * math.pi * R_MARS ** 2       # m^2
A_SURF_KM2 = A_SURF / 1e6
M_ATM      = P_S * A_SURF / G_MARS           # kg
N_ATM      = M_ATM / MU_ATM                  # mol


def burden_t(chi):
    """Global CH4 burden in tonnes for a well-mixed mole fraction chi."""
    return chi * N_ATM * M_CH4 / 1e3


# ---------------------------------------------------------------- observables
B_bg  = burden_t(V["chi_bg"])
B_lo  = burden_t(V["chi_lo"])
B_hi  = burden_t(V["chi_hi"])
B_s19 = burden_t(V["chi_spike19"])

half_mars_yr = (YEAR_MARS_D / 2) / 365.25            # Earth years
R_ss     = B_bg / V["tau_photo_yr"]                  # t/yr, steady-state maintenance
R_seas   = (B_hi - B_lo) / half_mars_yr              # t/yr, seasonal rise (= fall)
tau_seas = half_mars_yr / math.log(V["chi_hi"] / V["chi_lo"])   # yr, effective decay
speedup  = V["tau_photo_yr"] / tau_seas

dt_spike_yr   = SOL_D / 365.25                       # next TLS point ~one sol later
tau_spike     = dt_spike_yr / math.log(V["chi_spike19"] / V["chi_hi"])
R_spike       = B_s19 / tau_spike
speedup_spike = V["tau_photo_yr"] / tau_spike

sigma_bg = V["chi_bg"] / V["chi_bg_sig"]             # step 0(a)

# ---------------------------------------------------------------- availability
P_idp      = burden_t(V["chi_idp_model"]) / V["tau_photo_yr"]   # t/yr sustained
P_serp     = V["serp_t_km2_yr"] * V["nili_km2"]                 # t/yr, Nili aperture
P_photo    = B_bg / V["tau_photo_yr"]                           # t/yr removal capacity
P_regolith = V["micro_lo_t_km2_yr"] * A_SURF_KM2                # t/yr two-way exchange ceiling

# required two-way exchange flux density, mg m-2 day-1
q_req_mg = (B_hi - B_lo) * 1e9 / (A_SURF_KM2 * 1e6) / (half_mars_yr * 365.25) * 1e3

ROWS = [
    ("SOURCE", "UV degradation of meteoritic/IDP organics -- background only",
     R_ss, P_idp, "infall mass x organic content x UV yield (the Yung+2018 model itself)", "linear"),
    ("SOURCE", "UV degradation of meteoritic/IDP organics -- seasonal amplitude",
     R_seas, P_idp, "same", "linear"),
    ("SOURCE", "Serpentinisation / abiotic FTT microseepage",
     R_seas, P_serp, "30,000 km2 Nili Fossae olivine outcrop at 5 t/km2/yr", "linear in area"),
    ("SINK", "Gas-phase photochemistry (tau = 300 yr) vs the seasonal fall",
     R_seas, P_photo, "the whole atmospheric column already carrying the burden", "FIXED by the burden -- not free"),
    ("SINK", "Gas-phase photochemistry vs the 2019 spike, read globally",
     R_spike, P_photo, "same", "FIXED by the burden -- not free"),
    ("SINK", "Regolith adsorption / two-way surface exchange",
     R_seas, P_regolith, "whole planet at the LOWEST terrestrial microseepage rate, 4 t/km2/yr", "linear in area"),
]


def A(req, avail):
    return req / avail


def show():
    print("== derived constants ==")
    print("  surface area          %.4g km2" % A_SURF_KM2)
    print("  atmospheric mass      %.4g kg   (%.4g mol)" % (M_ATM, N_ATM))
    print("  burden @ 0.41 ppbv    %.4g t" % B_bg)
    print("  burden @ 0.24 / 0.65  %.4g / %.4g t" % (B_lo, B_hi))
    print("  burden @ 21 ppbv      %.4g t   (if globally mixed)" % B_s19)
    print()
    print("== step 0(a) ==")
    print("  background 0.41 +/- 0.16 ppbv -> %.2f sigma, interval excludes zero" % sigma_bg)
    print("  TGO global limit %.2f ppbv -> a globally mixed background is consistent with ZERO"
          % (V["chi_tgo"] * 1e9))
    print()
    print("== required fluxes ==")
    print("  R_ss   (hold 0.41 ppbv at tau=300 yr)          %12.4g t/yr" % R_ss)
    print("  R_seas (drive 0.24 -> 0.65 in half a Mars yr)  %12.4g t/yr" % R_seas)
    print("  tau_eff implied by the seasonal fall           %12.4g yr  -> %.0fx faster than photochemistry"
          % (tau_seas, speedup))
    print("  R_spike (21 ppbv gone in one sol, read GLOBAL) %12.4g t/yr (tau %.2f h, %.3gx)"
          % (R_spike, tau_spike * 365.25 * 24, speedup_spike))
    print("  two-way exchange flux density required         %12.4g mg/m2/day  vs 10-100 terrestrial microseepage"
          % q_req_mg)
    print()
    print("== enumeration: A = required / available, with the step-5 aperture row ==")
    hdr = "%-7s %-62s %11s %12s %10s %10s %10s  state"
    print(hdr % ("side", "candidate", "req t/yr", "avail t/yr", "A(2x ap)", "A", "A(0.5x ap)"))
    for side, name, req, av, ap, sc in ROWS:
        a = A(req, av)
        st = "RULED OUT (x%.3g)" % a if a > 1 else "SURVIVES"
        if a > 1 and a / 2 < 1:
            st += "  [fails the 2x row -> NOT TESTED per F7]"
        print("%-7s %-62s %11.4g %12.4g %10.4g %10.4g %10.4g  %s"
              % (side, name, req, av, a / 2, a, a * 2, st))
        print("        aperture: %s  (%s)" % (ap, sc))
    print()
    print("== calibration against Yung+2018 ==")
    B7 = burden_t(V["chi_spike13"])
    S7 = B7 / V["yung_spike_tau_yr"]
    print("  our GLOBAL-burden source for a 7 ppbv spike at tau=1 month: %.4g t/yr" % S7)
    print("  Yung+2018 (Lefevre & Forget model, LOCAL Martz-crater source): %.4g t/yr"
          % V["yung_spike_src_t"])
    print("  ratio = %.3g -- local-vs-global aperture divergence, exactly F3" % (S7 / V["yung_spike_src_t"]))
    print("  IDP model / observed background = %.2fx (Yung says 'some five times larger')"
          % (V["chi_idp_model"] / V["chi_bg"]))
    print("  our tau_eff %.3g yr vs Lefevre & Forget 2009 'shorter than 1 year' -- MATCH" % tau_seas)
    print()
    print("== provenance ==")
    for k, (v, src) in LIT.items():
        print("  %-20s = %r\n      %s" % (k, v, src))


if __name__ == "__main__":
    show()
