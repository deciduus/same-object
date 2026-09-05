#!/usr/bin/env python3
"""c31_ha.py — arithmetic behind computed/C31-remanufacturing-ha.md.

Run:  python _scripts/c31_ha.py     (from vault/)

Nothing here fetches anything. Every input is a literal taken from a source
named in C31 §Inputs; the script exists so the arithmetic in the note can be
re-run rather than trusted. Outputs are printed in the order the note's tables
use them.

The three objects computed:

  1. Ha = k_r/k_d for a repairable *product* population, where
        k_d = 1 / (mean in-service life L)        [exit rate per unit in service]
        k_r = 1 / (mean out-of-service time T)    [restore rate per unit out]
     so  Ha = L / T   exactly, as in C6 §3.3 (Ha = MTBF/MTTR).

  2. The r-corrected availability derived in C31 §3:
        A = Ha / (Ha + r)
     for a three-state chain S -> O (with probability r) / S -> Lost (1-r),
     O -> S (yield y) / O -> Lost (1-y), replenished by new production so the
     installed base is constant. Reduces to C6's A = Ha/(1+Ha) iff r = 1.

  3. The circular-fraction ceiling  A_circ = r*y <= r  (C31 §5, the prediction).
"""

def ha_from_times(L_years, T_years):
    """Ha = k_r/k_d = L/T. Both arguments in the same time unit."""
    k_d = 1.0 / L_years
    k_r = 1.0 / T_years
    return k_r / k_d, k_d, k_r


def A_c6(ha):
    """C6's availability: every exit re-enters the repairable pool (r = 1)."""
    return ha / (1.0 + ha)


def A_r(ha, r):
    """C31's availability for a fleet where only a fraction r of exits return."""
    return ha / (ha + r)


def rho(ha):
    """Erlang-B offered load. C6 s1.1: rho = 1/Ha, and 1 - A = B(rho, 1)."""
    return 1.0 / ha


def A_circ(r, y):
    """Fraction of unit-years of service supplied by remanufactured units."""
    return r * y


def line(name, L, T, r=1.0, note=""):
    ha, k_d, k_r = ha_from_times(L, T)
    return (f"{name:<46} L={L:>7.3f} yr  T={T:>7.4f} yr  "
            f"k_d={k_d:>8.4f}/yr  k_r={k_r:>9.3f}/yr  "
            f"Ha={ha:>9.2f}  A(C6)={A_c6(ha):.5f}  "
            f"A(r={r:g})={A_r(ha, r):.5f}  rho={rho(ha):.5f}  {note}")


if __name__ == "__main__":
    print("== 1. Rows computable from published inputs "
          "(sources in C31 section Inputs) ==")
    # Offshore wind turbine fleet. Carroll, McDonald & McMillan 2016,
    # Wind Energy 19:1107-1119, doi 10.1002/we.1887, Table 2, as read in
    # C1 section 3.2: lambda = 8.27 /turbine/yr, MTTR = 12.06 h.
    # L = MTBF = (8760 - 99.76)/8.27 h = 1047 h; T = MTTR = 12.06 h.
    print(line("offshore wind turbine fleet (repair, r=1)",
               1047.0 / 8760.0, 12.06 / 8760.0, 1.0, "[C1 3.2, VERIFIED-PRIMARY]"))

    # Human trabecular bone, the two C6 section 5 endpoints, for the axis.
    print(line("trabecular bone, full remodelling cycle down",
               (730 - 200) / 365.0, 200 / 365.0, 1.0, "[C6 5]"))
    print(line("trabecular bone, resorption phase only down",
               (730 - 35) / 365.0, 35 / 365.0, 1.0, "[C6 5]"))

    print()
    print("== 2. Sensitivity: a 10-year product fleet against core turnaround T ==")
    print("   L = 10 yr is Huster et al. 2023 (doi 10.1007/s13243-023-00130-3)")
    print("   central EV-battery lifetime. T is NOT PUBLISHED for any fleet found;")
    print("   these rows are a sensitivity, not data.")
    for T_months in (1, 3, 6, 12, 24):
        T = T_months / 12.0
        ha, _, _ = ha_from_times(10.0, T)
        print(f"   T = {T_months:>2} months  ->  Ha = {ha:>7.2f}   "
              f"A(C6, r=1) = {A_c6(ha):.4f}   "
              f"A(r=0.75) = {A_r(ha, 0.75):.4f}   "
              f"A(r=0.50) = {A_r(ha, 0.50):.4f}")

    print()
    print("== 3. The prediction: A_circ = r*y <= r, independent of yield ==")
    print("   r from Huster et al. 2023 section on return-rate assumptions.")
    for r, label in ((0.50, "RF50"), (0.75, "RD75/RF75 central"), (1.00, "RF100")):
        for y in (0.70, 0.85, 1.00):
            print(f"   r = {r:.2f} ({label:<18}) y = {y:.2f}  ->  "
                  f"A_circ = {A_circ(r, y):.4f}   ceiling r = {r:.2f}")

    print()
    print("== 4. Reciprocal check: Ha implied by an observed in-service fraction ==")
    print("   Ha = A*r/(1-A), the inverse of A = Ha/(Ha+r). Use this to read a")
    print("   published in-service fraction back onto C6's axis.")
    for A in (0.90, 0.95, 0.99):
        for r in (0.75, 1.00):
            print(f"   A = {A:.2f}, r = {r:.2f}  ->  Ha = {A * r / (1 - A):.2f}")
