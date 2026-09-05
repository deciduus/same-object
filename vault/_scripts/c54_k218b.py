"""C54 - K2-18 b DMS reservoir audit, conditional arithmetic (downstream of a step-0(b) halt).

Every input is marked VERIFIED (fetched this session with the URL that produced it),
SECONDARY (quoted by a brief source about a non-brief source), UNVERIFIED (standard value),
or ASSUMED (chosen here; the free parameter).

Run: python vault/_scripts/c54_k218b.py
"""

# --- physical constants (UNVERIFIED: CODATA/IAU standard values) ---
G      = 6.67430e-11      # m^3 kg^-1 s^-2
M_E    = 5.9722e24        # kg
R_E    = 6.371e6          # m
N_A    = 6.02214076e23    # mol^-1
AMU    = 1.66053907e-27   # kg
YR     = 3.15576e7        # s (Julian year)
DAY    = 86400.0          # s

# --- planet (VERIFIED, ar5iv/2504.12267 = Madhusudhan et al. 2025 ApJL, quoting
#     Cloutier et al. 2019 / Benneke et al. 2019a): "a mass of 8.63 +/- 1.35 M_earth
#     and a radius of 2.61 +/- 0.09 R_earth" ---
M_p = 8.63 * M_E
R_p = 2.61 * R_E
g   = G * M_p / R_p**2
A_p = 4.0 * 3.141592653589793 * R_p**2

# --- atmosphere ---
MU_AMU = 2.3              # UNVERIFIED: solar-composition H2/He mean molecular weight
mbar   = MU_AMU * AMU     # kg per particle
T_phot = 422.0            # K, VERIFIED ar5iv/2504.12267: "422 (+141 -133) K at 1 mbar"
R_GAS  = 8.31446
H_scale = R_GAS * T_phot / (MU_AMU * 1e-3 * g)   # m

# --- observable (VERIFIED, ar5iv/2504.12267 abstract + sec IV):
#     "high abundance (>~10 ppmv) of at least one of the two molecules";
#     sec IV: "mixing ratios of ~10^-5 - 10^-3". Brief states 1-100 ppm. ---
F_DMS_NOM = 1e-5          # 10 ppmv
F_DMS_LO  = 1e-6
F_DMS_HI  = 1e-3

# --- the APERTURE (step 5). On a mass-budget input the aperture is the column, i.e.
#     the reference pressure to which the mixing ratio is taken to extend. ASSUMED. ---
P_REF_NOM = 1e5           # Pa = 1 bar

# --- the SINK timescale. VERIFIED-as-quoted, ar5iv/2504.12267 sec IV.2, of DMS/DMDS:
#     "very short lifetimes ... in the Earth's atmosphere (i.e., between a few hours to
#     ~1 day)". Nominal 1 day; short leg 3 h. This is NOT a K2-18 b number. ---
TAU_NOM   = 1.0 * DAY
TAU_SHORT = 3.0 * 3600.0

M_DMS = 62.13             # g/mol, UNVERIFIED (standard)

# --- Earth's marine DMS flux, for the ratio Madhusudhan/Tsai quote in "x Earth" units.
#     UNVERIFIED: 28 Tg S/yr, the mid of the commonly quoted 20-30 Tg S/yr. Flagged as
#     the weakest input in the note; the exponent of the answer does not turn on it. ---
F_EARTH_TgS = 28.0
F_EARTH_mol = F_EARTH_TgS * 1e12 / 32.06     # mol S/yr == mol DMS/yr (1 S per DMS)


def column(f_dms, p_ref):
    """DMS column number density [m^-2] for mixing ratio f_dms uniform above p_ref."""
    n_atm = p_ref / (mbar * g)                # total column, m^-2 (hydrostatic)
    return f_dms * n_atm, n_atm


def required_flux(f_dms, p_ref, tau):
    """F_req = N_col / tau, returned as (per-area m^-2 s^-1, global mol/yr, x Earth)."""
    n_col, _ = column(f_dms, p_ref)
    per_area = n_col / tau                            # m^-2 s^-1
    global_mol_yr = per_area * A_p / N_A * YR         # mol/yr
    return per_area, global_mol_yr, global_mol_yr / F_EARTH_mol


def tau_required(f_dms, p_ref, flux_mol_yr):
    """Invert: the photochemical lifetime that makes a given source flux sufficient."""
    n_col, _ = column(f_dms, p_ref)
    inventory_mol = n_col * A_p / N_A
    return inventory_mol / flux_mol_yr                # yr


if __name__ == "__main__":
    n_col, n_atm = column(F_DMS_NOM, P_REF_NOM)
    print("g            = %.3f m/s^2" % g)
    print("R_p          = %.4e m   A_p = %.4e m^2" % (R_p, A_p))
    print("H (422 K)    = %.1f km" % (H_scale / 1e3))
    print("N_atm(1 bar) = %.4e m^-2" % n_atm)
    print("N_DMS(10ppm) = %.4e m^-2" % n_col)
    inv = n_col * A_p / N_A
    print("inventory    = %.4e mol = %.4e t" % (inv, inv * M_DMS / 1e6))
    print()
    print("--- step 5 aperture rows: F_req (mol/yr) and A = F_req / F_Earth ---")
    for lbl, p in (("2x aperture (2 bar)", 2 * P_REF_NOM),
                   ("nominal   (1 bar)  ", P_REF_NOM),
                   ("0.5x aperture(0.5bar)", 0.5 * P_REF_NOM)):
        pa, mo, ax = required_flux(F_DMS_NOM, p, TAU_NOM)
        print("  %-22s F_req = %.3e mol/yr   A = %.3e" % (lbl, mo, ax))
    print()
    print("--- sink-timescale rows (tau is the second free parameter) ---")
    for lbl, tau in (("tau = 3 h ", TAU_SHORT), ("tau = 1 day", TAU_NOM),
                     ("tau = 1 yr ", YR), ("tau = 1 kyr", 1e3 * YR)):
        pa, mo, ax = required_flux(F_DMS_NOM, P_REF_NOM, tau)
        print("  %-11s F_req = %.3e mol/yr  (%.3e cm^-2 s^-1)  A = %.3e"
              % (lbl, mo, pa / 1e4, ax))
    print()
    print("--- mixing-ratio range rows, tau = 1 day, 1 bar ---")
    for lbl, f in (("1 ppm  ", F_DMS_LO), ("10 ppm ", F_DMS_NOM), ("1000 ppm", F_DMS_HI)):
        pa, mo, ax = required_flux(f, P_REF_NOM, TAU_NOM)
        print("  %-8s F_req = %.3e mol/yr   A = %.3e" % (lbl, mo, ax))
    print()
    print("--- the inversion: tau required for Tsai et al. 2024's >=20x Earth flux ---")
    for lbl, f in (("10 ppm ", F_DMS_NOM), ("1000 ppm", F_DMS_HI)):
        t = tau_required(f, P_REF_NOM, 20.0 * F_EARTH_mol)
        print("  %-8s tau_req = %.3e yr  = %.3e x (Earth's 1 day)" % (lbl, t, t * YR / TAU_NOM))
    print()
    print("--- Reed et al. 2024 lab ceiling vs required mixing ratio (aperture-free) ---")
    for lbl, ceil in (("no CO2 (0.81 ppmv)", 0.81e-6), ("with CO2 (0.06 ppmv)", 0.06e-6)):
        print("  %-22s A = f_req/f_ceiling = %.1f (at 10 ppmv)   %.1f (at 1000 ppmv)"
              % (lbl, F_DMS_NOM / ceil, F_DMS_HI / ceil))
