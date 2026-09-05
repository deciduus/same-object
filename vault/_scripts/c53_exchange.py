#!/usr/bin/env python3
"""C53 - is C49's EXCHANGE REQUIRED residual reachable by regolith adsorption?

Blind brief audits/blind-brief-c53-2026-09-05.md
sha256 7529887e8233ede93ab66860c2d900ae37e41323f125f59d9f5890f837d5857f (hashed BEFORE this ran).

Route: Frenkel residence-time physisorption. Coverage N = gamma * Z * tau0 * exp(dH/RT).
Seasonal amplitude comes from d ln q / dT = -dH/(R T^2), damped with depth by the ANNUAL
thermal skin depth (which the brief pre-committed to as the smaller of thermal vs diffusive).
"""
import math

R, kB, NA = 8.314462, 1.380649e-23, 6.02214076e23
# --- observable + required, inherited from C49 (all its own arithmetic, not re-derived here)
REQ_T      = 3820.0          # t/yr per phase, planet-wide
CHI        = 0.41e-9         # ppbv -> mole fraction, Webster 2018 background
P_SURF     = 610.0           # Pa
A_MARS     = 1.444e14        # m^2
MARS_YR_S  = 687*86400.0
# --- adsorbate / regolith
M_CH4  = 0.016043            # kg/mol
m_CH4  = M_CH4/NA
TAU0   = 1e-13               # s, standard physisorption pre-exponential -- UNVERIFIED, linear
GAMMA  = 1.0                 # uptake/evaporation ratio; Smith+2019 LPSC best fit gamma/eta = 1
T_MEAN = 210.0               # K, Gale mean surface T -- UNVERIFIED
DT_PP  = 20.0                # K, peak-to-peak ANNUAL swing of daily-mean surface T -- DERIVED
RHO    = 1300.0              # kg/m^3 regolith bulk density -- UNVERIFIED
S_SPEC = 1.0e5               # m^2/kg (100 m^2/g, JSC Mars-1 palagonite high end) -- UNVERIFIED
SIGMA  = 0.16e-18            # m^2 per CH4, monolayer cross-section
# --- thermal
TI     = 300.0               # J m^-2 K^-1 s^-1/2 thermal inertia, Gale -- UNVERIFIED
C_SPEC = 800.0               # J/kg/K

def skin(period):
    kappa = TI**2/(RHO*C_SPEC)**2
    return math.sqrt(kappa*period/math.pi)

def coverage(dH_kJ, T):
    """molecules m^-2 at equilibrium with the CH4 partial pressure."""
    p = CHI*P_SURF
    Z = p/math.sqrt(2*math.pi*m_CH4*kB*T)          # Hertz-Knudsen collision flux
    tau = TAU0*math.exp(dH_kJ*1e3/(R*T))
    return GAMMA*Z*tau, Z, tau

def run(dH_kJ, label, dT=DT_PP, S=S_SPEC, delta=None):
    N, Z, tau = coverage(dH_kJ, T_MEAN)
    theta = N*SIGMA
    q = N/NA*M_CH4*S                                # kg CH4 per kg regolith
    coef = dH_kJ*1e3/(R*T_MEAN**2)                  # fractional dq/q per K
    d = delta if delta else skin(MARS_YR_S)
    dM_m2 = RHO*q*coef*dT*d                         # kg/m2, integral of exp(-z/delta) = delta
    tot_t = dM_m2*A_MARS/1000.0
    print(f"{label:38s} dH={dH_kJ:5.1f}  tau={tau:9.2e}s  theta={theta:9.2e}  "
          f"q={q:9.2e} kg/kg  dM={dM_m2:9.3e} kg/m2  total={tot_t:11.4g} t  "
          f"A_exch={REQ_T/tot_t:11.4g}")
    return dM_m2, tot_t

print("Mars annual thermal skin depth  = %.3f m" % skin(MARS_YR_S))
print("Mars diurnal thermal skin depth = %.4f m" % skin(88775.0))
for D in (1e-5, 1e-4, 8.4e-4):
    print("  diffusive depth over half a Mars yr at D_eff=%.1e m2/s : %.1f m"
          % (D, math.sqrt(D*MARS_YR_S/2)))
print("-> thermal skin depth is the SMALLER; it governs (brief's pre-commitment)\n")

lab  = run(18.0,  "Gough 2010 MEASURED dH")
fit  = run(31.5,  "Smith/Moores 2019 FITTED dH")
print()
print("ratio fitted/measured available = %.4g  (= exp(dH_gap/RT) x coef ratio)"
      % (fit[1]/lab[1]))
print("dH gap 13.5 kJ/mol == a factor %.4g in tau0" % math.exp(13.5e3/(R*T_MEAN)))
print()
print("--- step-5 aperture rows (available scales linearly with area) ---")
for name, area in (("2x planet", 2*A_MARS), ("planet (nominal)", A_MARS),
                   ("0.5x planet", 0.5*A_MARS), ("Gale-like 2.7e4 km2", 2.7e10)):
    for lbl, (dm, _) in (("measured dH=18", (lab[0], 0)), ("fitted dH=31.5", (fit[0], 0))):
        t = dm*area/1000.0
        print(f"  {name:22s} {lbl:16s} available {t:11.4g} t  A_exch {REQ_T/t:11.4g}")
print()
print("--- sensitivity on the two other soft inputs (measured-dH row) ---")
for dT in (10., 20., 30.):
    run(18.0, f"dT_pp={dT:.0f} K", dT=dT)
for S in (1.7e4, 1.0e5):
    run(18.0, f"S={S/1e3:.0f} m2/g", S=S)
print()
print("--- diurnal vs annual driving integral (K.m) ---")
print("  annual : %.2f   diurnal(90 K pp): %.2f  -> annual wins %.2fx despite smaller dT"
      % (DT_PP*skin(MARS_YR_S), 90*skin(88775.0),
         DT_PP*skin(MARS_YR_S)/(90*skin(88775.0))))
print()
print("C49 areal residual check: %.4g mg m^-2 day^-1"
      % (REQ_T*1e9/A_MARS/365.25))
