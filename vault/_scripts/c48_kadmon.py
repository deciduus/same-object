"""C48 -- the Whittle patch rule under LINEAR nectar renewal (programme item P-068).

Pre-registered by audits/blind-brief-c48-2026-09-05.md, sha256
4e6fe72f283fe1eb074d8f2f3e8e7f17b1b4a35ad640751360df7422b2941572.

Verifies, numerically, the three analytical claims of that brief:
  A. singular-arc gain g(a) = lam*a*(c+nu)/(lam*a+c) has NO interior stationary point
     in a for any nu > -c  =>  Whittle index is flat on (0,1)  =>  dGUD/dc = 0.
  B. explicit-travel cycle rate R(a) = (x_arr-a)/(ln(x_arr/a)/lam + tau),
     x_arr = min(1, a+c*tau), is maximised at a* = max(a_MVT, 1-c*tau),
     where a_MVT solves f(a) = (1-a)/a + ln a = lam*tau.  => dGUD/dc <= 0.
  C. the contrast with C25's saturating law, where dGUD/dr > 0.

No data are read: both source papers are paywalled (see the note's access table).
Run: python _scripts/c48_kadmon.py   from vault/.
"""
import math

# ---------------------------------------------------------------- A
def g_arc(a, lam, c, nu):
    """Singular-arc long-run gain, linear renewal (brief eq. 2)."""
    A = lam * a
    return A * (c + nu) / (A + c)

def dg_da(a, lam, c, nu):
    """Brief eq. (3)."""
    A = lam * a
    return lam * c * (c + nu) / (A + c) ** 2

def g_arc_sat(a, lam, r, nu):
    """C25's saturating counterpart, for contrast: B = r(1-a)."""
    A, B = lam * a, r * (1.0 - a)
    return A * (B + nu) / (A + B)

# ---------------------------------------------------------------- B
def f(a):
    return (1.0 - a) / a + math.log(a)

def a_mvt(lam_tau):
    lo, hi = 1e-12, 1.0 - 1e-15
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) > lam_tau:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

def rate(a, lam, c, tau):
    x = min(1.0, a + c * tau)
    if x <= a:
        return 0.0
    return (x - a) / (math.log(x / a) / lam + tau)

def argmax_rate(lam, c, tau, n=2_000_001):
    best, ba = -1.0, None
    for i in range(1, n):
        a = i / n
        R = rate(a, lam, c, tau)
        if R > best:
            best, ba = R, a
    return ba, best

# ---------------------------------------------------------------- C25 saturating GUD
def gud_c25(rho, u0):
    if abs(rho - 1.0) < 1e-12:
        return 0.5 * (1.0 + u0 * u0)
    return (-rho + math.sqrt(rho + u0 * u0 * (1.0 - rho))) / (1.0 - rho)


if __name__ == "__main__":
    lam, tau = 1.0, 1.0

    print("A. singular-arc gain, linear renewal: is there an interior optimum?")
    print("   lam=1  c=0.5.  dg/da over a grid, for several subsidies nu:")
    for nu in (-1.0, -0.6, -0.5, -0.4, 0.0, 0.3, 1.0, 5.0):
        vals = [dg_da(i / 20, lam, 0.5, nu) for i in range(1, 20)]
        sgn = "all>0" if min(vals) > 0 else ("all<0" if max(vals) < 0 else "MIXED")
        roots = sum(1 for i in range(len(vals) - 1) if vals[i] * vals[i + 1] < 0)
        print(f"     nu={nu:+.2f}  sign={sgn:6s}  sign-changes={roots}  "
              f"argmax_a g = {max(((g_arc(i/2000, lam, 0.5, nu), i/2000) for i in range(1,2000)))[1]:.4f}")
    print("   => flat index W(x) = -c on (0,1); W(1) = lam.  dGUD/dc = 0.  [P1]\n")

    print("   contrast, C25 saturating B=r(1-a), lam=1 r=0.5 nu=0.09:")
    arg = max(((g_arc_sat(i / 2000, lam, 0.5, 0.09), i / 2000) for i in range(1, 2000)))[1]
    print(f"     argmax_a g = {arg:.4f}  (interior)  <= the term that linear renewal deletes\n")

    aM = a_mvt(lam * tau)
    print(f"B. a_MVT root of f(a)=lam*tau={lam*tau}:  a_MVT = {aM:.4f}   "
          f"(check f = {f(aM):.6f})")
    print(f"   kink of GUD*(c) at c*tau = 1 - a_MVT = {1-aM:.4f}\n")
    print("   c*tau | GUD* predicted | GUD* numeric argmax | dGUD/dc (fwd diff)")
    grid = [0.05, 0.10, 0.20, 0.50, 0.6821, 1.0, 2.0, 5.0]
    prev = None
    for ct in grid:
        c = ct / tau
        pred = max(aM, 1.0 - c * tau)
        num, _ = argmax_rate(lam, c, tau, 200001)
        d = "" if prev is None else f"{(pred-prev[0])/(c-prev[1]):+.3f}"
        print(f"   {ct:5.4f} | {pred:.4f}         | {num:.4f}              | {d}")
        prev = (pred, c)
    print("   => dGUD/dc = -tau below the kink, 0 above. NEVER positive. [P2]\n")

    print("C. the same axis under C25's saturating law (u0=0.30), for contrast:")
    print("   r*tau | GUD_C25(sat) | GUD_C48(linear, eq.8)")
    for rt in [0.05, 0.10, 0.20, 0.50, 1.0, 2.0, 5.0]:
        print(f"   {rt:5.2f} | {gud_c25(rt, 0.30):.4f}       | {max(aM, 1.0-rt):.4f}")
    print("   => the two laws disagree in SIGN across the whole usable window. [P3]")
