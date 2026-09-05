"""
C25 - Whittle index for a regrowing (restless) foraging patch.
Stdlib only.  Run:  python c25_whittle.py
Companion to vault/computed/C25-whittle-foraging.md.

MODEL (G_max normalised to 1, so x = standing crop = GUD when left behind):
  state x in [0,1]
  ACTIVE  (forager in patch):  xdot = -lam*x   ; intake rate = lam*x
                               => g(t) = 1 - exp(-lam t), Charnov's concave gain
  PASSIVE (patch unoccupied):  xdot =  r*(1-x) ; intake rate 0 (+ Whittle subsidy nu)
  travel time tau; discount -> 0 (average reward).

DERIVED IN THE NOTE (relative value V(x) = x - x^2/2, so V'(x) = 1-x):
  WHITTLE INDEX        W(x) = lam*x**2 - r*(1-x)**2
  MVT / C5 baseline    nu(x) = lam*x            (valid only when patches are
                                                 non-revisitable, i.e. V' == 0)
"""
import math

LAM = 1.0        # sets the time unit; all rates are in units of lam
LTAU = 1.0       # lam*tau, so that r*tau == r/lam numerically


def W(x, r, lam=LAM):
    """Whittle index of a patch at standing crop x with regrowth rate r."""
    return lam * x * x - r * (1.0 - x) ** 2


def dW(x, r, lam=LAM):
    return 2.0 * lam * x + 2.0 * r * (1.0 - x)


def gud_whittle(rho, u0):
    """Departure standing crop prescribed by the Whittle rule in a patch with
    rho = r/lam, in a habitat whose indifference index nu is anchored so that
    the rule agrees with MVT at r = 0:  nu = lam*u0**2, u0 = GUD_MVT.
    Closed form:  x = (-rho + sqrt(rho + u0**2*(1-rho))) / (1-rho)."""
    if abs(1.0 - rho) < 1e-9:
        return 0.5 * (1.0 + u0 * u0)
    return (-rho + math.sqrt(rho + u0 * u0 * (1.0 - rho))) / (1.0 - rho)


def dgud_dr(x, rho, lam=LAM):
    """dGUD/d(r/lam) at fixed habitat index:  (1-x)^2 / (2[x + rho(1-x)])."""
    return (1.0 - x) ** 2 / (2.0 * (x + rho * (1.0 - x)))


def residence(x_arr, x_dep, lam=LAM):
    """Residence time to deplete from x_arr to x_dep under xdot = -lam x."""
    if x_dep <= 0 or x_dep >= x_arr:
        return 0.0
    return math.log(x_arr / x_dep) / lam


# --------------------------------------------------------------------------
def section_indexability():
    print("A. INDEXABILITY  (W must be strictly increasing in x on [0,1])")
    print("   W'(x) = 2*lam*x + 2*r*(1-x) > 0 for all x in (0,1), lam,r > 0.")
    bad = 0
    for rho in (0.0, 0.01, 0.1, 1.0, 10.0, 1e3):
        prev = -1e18
        for i in range(1001):
            x = i / 1000.0
            w = W(x, rho)
            if w < prev - 1e-15:
                bad += 1
            prev = w
    print("   numeric check over 6 values of r/lam x 1001 states:"
          " monotonicity violations = %d" % bad)
    print("   => passive set {x : W(x) <= nu} = [0, W^-1(nu)] grows with nu."
          "  INDEXABLE, unconditionally.\n")


def section_degeneracy():
    print("B. HOMOGENEOUS-HABITAT DEGENERACY")
    print("   W is strictly increasing in x, so argmax_i W(x_i) = argmax_i x_i")
    print("   whenever all patches share (lam, r). The r-dependence cancels out")
    print("   of the priority rule: 'go to the fullest patch'. The index carries")
    print("   NO testable signal in a homogeneous habitat.  It bites only across")
    print("   patch types that differ in r (or lam).  Table C is that case.\n")


def section_prediction(u0=0.30):
    print("C. PREDICTION TABLE   (lam=1, lam*tau=%.1f so r*tau = r/lam;"
          " G_max=1)" % LTAU)
    print("   Habitat indifference index nu anchored at the MVT baseline:")
    print("   GUD_MVT = u0 = %.2f, nu = lam*u0^2 = %.4f\n" % (u0, u0 * u0))
    hdr = ("   r*tau |   GUD_W  |  dGUD   | GUD_W/GUD_MVT | t* (arr=1) |"
           " t*_W/t*_MVT")
    print(hdr)
    print("   " + "-" * (len(hdr) - 3))
    t_mvt = residence(1.0, u0)
    for rho in (0.0, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0):
        x = gud_whittle(rho, u0)
        t = residence(1.0, x)
        print("   %6.2f | %7.4f  | %+7.4f | %11.3f   | %8.3f   | %9.3f"
              % (rho * LTAU, x, x - u0, x / u0, t, t / t_mvt))
    print()
    print("   dGUD/d(r/lam) at r->0+ = (1-u0)^2 / (2*u0) = %.4f"
          % dgud_dr(u0, 0.0))
    print("   => small-r expansion:  GUD(r) ~ u0 + (1-u0)^2/(2 u0) * (r/lam)\n")


def section_limits(u0=0.30):
    print("D. LIMITS")
    print("   r -> 0, patches REVISITABLE   : W(x) -> lam*x^2  (NOT MVT).")
    print("     The residual lam*x^2 vs lam*x is the value of resource left in")
    print("     a patch you can return to - C5 row 6, now quantified.")
    print("   r -> 0, patches NON-REVISITABLE: V' == 0 by fiat, W(x) = lam*x =")
    print("     g'(t); rule g'(t*) = R* = max_t g(t)/(tau+t).  C5 eq.(4). EXACT.")
    print("   r -> infinity                 : W(x) -> -inf for x<1, W(1)=lam.")
    print("     GUD -> G_max, t* -> 0: skim the top of an always-full patch.")
    for rho in (1e2, 1e4, 1e6):
        print("     r/lam = %-8.0e  GUD = %.6f  t* = %.6f"
              % (rho, gud_whittle(rho, u0), residence(1.0, gud_whittle(rho, u0))))
    print()


if __name__ == '__main__':
    print(__doc__)
    section_indexability()
    section_degeneracy()
    section_prediction()
    section_limits()
