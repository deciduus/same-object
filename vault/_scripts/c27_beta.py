#!/usr/bin/env python3
"""C27 — product-lifespan Weibull fits placed on C18's beta axis.

Run:  python _scripts/c27_beta.py        (from vault/)

Inputs are PUBLISHED fitted parameters only; nothing here is re-fitted from raw
data. Every row names its source and its verification grade. The script does
three things and no more:

  1. re-derives median and mean from (beta, eta, theta) so the published median/
     mean can be checked against the published shape/scale (an internal
     consistency test on the source, not a new measurement);
  2. computes the hazard-fold statistic  H = h(2M)/h(M/2) = 4^(beta-1),
     the dimensionless "how much does the hazard climb over one factor of four
     in age" number that makes beta legible without a plot;
  3. prints the citation-intersection arithmetic for G30 at the union floor,
     and states that the concept-scoped denominator is MISSING.

No network calls. Provenance for every number is in C27-product-lifespan-beta.md.
"""
from math import gamma, log

# (label, beta, eta_scale_years, theta_delay_years, published_median, published_mean, grade)
# LBNL: Lutz et al. 2011, LBNL-5093E, Tables 2-12, delayed two-parameter Weibull.
LBNL = [
    ("Gas boiler",            1.000, 25.31, 0.000, 17.54, 25.31, "VERIFIED-fetched"),
    ("RAC, surveys >2000",    1.080, 10.27, 0.000,  8.36, 11.27, "VERIFIED-fetched"),
    ("RAC, surveys <2000",    1.067,  6.92, 8.000, 12.91, 14.75, "VERIFIED-fetched"),
    ("Electric water heater", 1.174, 13.19, 0.000,  9.65, 12.48, "VERIFIED-fetched"),
    ("Refrigerator",          1.272, 11.75, 8.874, 17.68, 19.77, "VERIFIED-fetched"),
    ("Gas water heater",      1.307, 11.64, 3.196, 11.99, 13.93, "VERIFIED-fetched"),
    ("Room air-conditioner",  1.442, 14.29, 0.000, 11.08, 12.96, "VERIFIED-fetched"),
    ("Heat pump",             1.525, 18.62, 0.000, 14.64, 16.77, "VERIFIED-fetched"),
    ("Freezer",               1.885, 17.92, 6.459, 21.21, 22.36, "VERIFIED-fetched"),
    ("Central air-cond.",     2.094, 21.49, 0.000, 18.04, 19.03, "VERIFIED-fetched"),
    ("Gas furnace",           2.218, 26.68, 0.000, 22.61, 23.63, "VERIFIED-fetched"),
]

# Held et al. 2021, Eur. Transp. Res. Rev. 13:9, Table 1 (subset read via PMC7829067).
CARS = [
    ("Car, Luxembourg",  2.0,  8.0), ("Car, Belgium", 2.0, 11.7),
    ("Car, Germany",     2.4, 14.8), ("Car, Italy",   2.7, 19.6),
    ("Car, Spain",       3.2, 19.4), ("Car, Austria", 3.4, 15.9),
    ("Car, Switzerland", 3.6, 15.4), ("Car, Greece",  4.2, 33.9),
    ("Car, Netherlands", 4.4, 17.2), ("Car, Poland",  6.0, 35.1),
]

# C18 rows, for the comparison axis.
C18 = [
    ("Enzyme, suicide inactivation", 1.0,  "C18 sec.2.1  (geometric, p = 1/r)"),
    ("Enzyme, thermal denaturation", 1.0,  "C18 sec.2.1  (<1 if biphasic)"),
    ("Organic flow-battery reactant", 1.0, "C18 sec.2.3  (calendar-time decay)"),
    ("Li-ion NCR18650GA",           12.7,  "C18 sec.2.2  VERIFIED-via-search only"),
]


def med(beta, eta, theta=0.0):
    return theta + eta * log(2.0) ** (1.0 / beta)


def mean(beta, eta, theta=0.0):
    return theta + eta * gamma(1.0 + 1.0 / beta)


def hazard_fold(beta):
    """h(2M)/h(M/2) for a pure Weibull: (2M/M/2)^(beta-1) = 4^(beta-1)."""
    return 4.0 ** (beta - 1.0)


def main():
    print("=" * 78)
    print("C27  product-lifespan Weibull fits on the C18 beta axis")
    print("=" * 78)

    print("\n[1] LBNL residential appliances (Lutz et al. 2011) — internal check")
    print(f"{'class':<24}{'beta':>7}{'eta':>8}{'theta':>7}"
          f"{'med(calc)':>11}{'med(pub)':>10}{'mean(calc)':>12}{'mean(pub)':>11}")
    for lab, b, e, th, pm, pmean, _g in LBNL:
        print(f"{lab:<24}{b:>7.3f}{e:>8.2f}{th:>7.2f}"
              f"{med(b, e, th):>11.2f}{pm:>10.2f}{mean(b, e, th):>12.2f}{pmean:>11.2f}")

    print("\n[2] hazard-fold H = 4^(beta-1)  (H = 1 memoryless; H > 1 wear-out)")
    rows = ([(l, b) for l, b, *_ in LBNL]
            + [(l, b) for l, b, _e in CARS]
            + [(l, b) for l, b, _s in C18])
    for lab, b in sorted(rows, key=lambda r: r[1]):
        print(f"  {lab:<32} beta={b:<6.3f}  H={hazard_fold(b):>10.2f}")

    print("\n[3] G30 citation-intersection arithmetic (union floor only)")
    for lab, na, nb, o in [("Weibull1951 x Oguchi2015", 11512, 103, 0),
                           ("Weibull1951 x Murakami2010-I", 11512, 185, 1),
                           ("Weibull1951 x Bakker2014", 11512, 717, 0),
                           ("CONTROL Mueller2006 x Oguchi2015", 511, 103, 15)]:
        n = na + nb - o
        exp = na * nb / n
        print(f"  {lab:<34} |A|={na:<6} |B|={nb:<5} O={o:<3} "
              f"N_floor={n:<6} E={exp:8.2f}  O/E={o / exp:6.4f}")
    print("  concept-scoped N_universe: NOT OBTAINED — OpenAlex daily budget")
    print("  exhausted 2026-09-05 (HTTP 429, 'Insufficient budget'). Every E")
    print("  above is a FLOOR and flatters the gap claim by construction.")
    print("\n  denominator-invariant control ratio, shared B = Oguchi 2015:")
    print("    (O_gap/|B|) / (O_ctl/|B|) = (0/103)/(15/103) = 0  -> isolation infinite")


if __name__ == "__main__":
    main()
