#!/usr/bin/env python3
"""C30 - Venus phosphine reservoir audit: the arithmetic behind every A value.

All inputs are sourced in vault/computed/C30-venus-phosphine-audit.md, fetched
2026-09-05.  Nothing here is fitted; every line is a division.

Run:  python _scripts/c30_phosphine.py
"""

# ---------------------------------------------------------------- constants
M_PH3      = 33.998          # g/mol, PH3
SEC_YR     = 3.1557e7        # s per Julian year
VENUS_YR   = 0.6152          # Earth years per Venus year (224.7 d / 365.25 d)

# ------------------------------------------------- the required source flux
# Bains et al. 2021, Astrobiology, 10.1089/ast.2020.2352:
#   "a flux of ~10^8 phosphine molecules cm-2 s-1 (averaged across the whole
#    planet) is needed to reproduce the observed phosphine mixing ratio of
#    1 ppb above 55 km ... equivalent to ~26 kg/second or ~8x10^5 tonnes year-1"
S_REQ_CM2S = 1.0e8           # molecules cm^-2 s^-1
S_REQ_KG_S = 26.0            # kg/s of PH3
S_REQ_T_YR = 8.0e5           # tonnes/yr of PH3

S_REQ_MOL_YR = S_REQ_KG_S * 1e3 / M_PH3 * SEC_YR     # mol/yr, computed here

# Bains' own extremal-aperture lower bound (tau inflated ~10^3x by assuming
# destruction is transport-only from the surface to 98 km at K_z = 2200 cm2/s):
S_REQ_CONSERVATIVE = 1.3e5   # molecules cm^-2 s^-1

# ------------------------------------------------------- available fluxes
# Each value is the maximum the route can supply, in tonnes of PH3 per Earth
# year, taken from the paper named in the C30 table.
AVAIL_T_YR = {
    "volcanic (direct PH3, most reducing plausible crust)": 1.0e2,
    "lightning": 3.5 / VENUS_YR,       # "3.5 tonnes per Venusian year"
    "meteoritic delivery (100% hydrolysis of (Fe,Ni)3P)": 1.0e1,
}

# Routes Bains bounds only as an order-of-magnitude shortfall, not a flux.
SHORTFALL_ORDERS = {
    "atmospheric photochemistry": (5, None),      # "at least 5 orders"
    "surface / subsurface geochemistry": (8, 15),
    "tribochemical / mechanochemical": (2, None), # "at least two orders"
}

# ---------------------------------------------------------------- reporting
def main():
    print(f"S_req = {S_REQ_CM2S:.1e} molecules cm-2 s-1"
          f" = {S_REQ_KG_S} kg/s = {S_REQ_T_YR:.1e} t/yr"
          f" = {S_REQ_MOL_YR:.2e} mol/yr")
    print(f"Bains' extremal-aperture lower bound: {S_REQ_CONSERVATIVE:.1e}"
          f" cm-2 s-1  (ratio {S_REQ_CM2S/S_REQ_CONSERVATIVE:.0f}x)")
    print()
    print(f"{'route':<52} {'A':>10} {'A(2tau)':>10} {'A(0.5tau)':>11}")
    for name, avail in AVAIL_T_YR.items():
        A = S_REQ_T_YR / avail
        print(f"{name:<52} {A:>10.1e} {A/2:>10.1e} {2*A:>11.1e}")
    for name, (lo, hi) in SHORTFALL_ORDERS.items():
        lab = f">=1e{lo}" if hi is None else f"1e{lo}-1e{hi}"
        print(f"{name:<52} {lab:>10} {'/2':>10} {'x2':>11}")
    print()

    # Volcanic, by the independent phosphorus-outgassing route:
    #   Bains fig. 9: "few conditions require a total flux of less than
    #   10^9 grams of phosphorus per second"; Earth's volcanic P outgassing
    #   is "~143 kg/second".
    A_volc_P = 1.0e9 / (143.0 * 1e3)
    print(f"volcanic, via P outgassing: A = 1e9 g/s / 1.43e5 g/s = {A_volc_P:.1e}")

    # The aperture row that bites: at Bains' own extremal tau the volcanic
    # requirement falls to 800 t/yr of PH3.
    print(f"at tau x1e3: required = {S_REQ_T_YR/1e3:.0f} t/yr;"
          f" A(volcanic) = {S_REQ_T_YR/1e3/AVAIL_T_YR['volcanic (direct PH3, most reducing plausible crust)']:.1f}")

    # The 266.94 GHz degeneracy, in velocity units.
    C_KMS = 2.99792458e5
    nu_ph3, nu_so2 = 266.9445, 266.943329      # GHz
    dv = C_KMS * (nu_ph3 - nu_so2) / nu_ph3
    print(f"PH3 1-0 {nu_ph3} GHz vs SO2 {nu_so2} GHz:"
          f" separation {1e3*(nu_ph3-nu_so2):.2f} MHz = {dv:.2f} km/s")


if __name__ == "__main__":
    main()
