"""C46 - reservoir audit negative control D.1: Betz-calibrated wind turbine.
Inputs are exactly the four numbers in audits/blind-brief-c46-2026-09-05.md.
Run: python vault/_scripts/c46_betz.py
"""
import math

D, U, RHO, P_E, CP = 90.0, 11.0, 1.225, 2.0e6, 0.44
TOL = 0.03  # assumed relative tolerance on the manufacturer's C_p (brief states none)

A_nom = math.pi * (D / 2) ** 2
P_avail = 0.5 * RHO * A_nom * U ** 3
betz = 16 / 27
F_req = P_E / U                      # generator form, Part C step 2
Aval = F_req * U / P_avail           # availability leg, step 7
sigma = P_E / (F_req * U)            # energy leg, step 8 (= 1 by construction here)

print(f"swept area A_nom      = {A_nom:.1f} m^2")
print(f"P_avail               = {P_avail/1e6:.4f} MW")
print(f"Betz ceiling 16/27    = {betz:.4f} -> {P_avail*betz/1e6:.4f} MW")
print(f"P_e / P_avail         = {P_E/P_avail:.4f}  (required C_p, electrical)")
print(f"  as fraction of Betz = {(P_E/P_avail)/betz:.4f}")
print(f"stated C_p aero power = {CP*P_avail/1e6:.4f} +/- {TOL*CP*P_avail/1e6:.4f} MW")
print(f"residual P_e - P_aero = {(P_E-CP*P_avail)/1e6:+.4f} MW  (implied drivetrain eta = {P_E/(CP*P_avail):.4f})")
print(f"F_req                 = {F_req:.0f} N")
print(f"A(nominal)            = {Aval:.4f}")
for k, lab in ((2.0, "2x"), (0.5, "0.5x")):
    print(f"A({lab} aperture, area {k*A_nom:.1f} m^2, P_avail linear in area) = {Aval/k:.4f}")
print(f"Sigma                 = {sigma:.4f}")
