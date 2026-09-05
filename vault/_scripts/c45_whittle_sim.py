"""
C45 - the C25 Whittle patch index RUN FORWARD as a policy in a mixed-r network.
Programme item P-053.  stdlib only (no numpy needed: N = 20 is small enough that
plain Python lists beat array dispatch).

Pre-registered by audits/blind-brief-c45-2026-09-05.md
sha256 fbc48359b5215f6a3f2c4f6cefee4ce7a73257c7c8121c33ef8615f0d49714a7

MODEL (C25 section 1, G_max = 1, lam = 1 sets the time unit)
  ACTIVE  (forager present):  xdot = -lam x, intake rate lam x
  PASSIVE (unoccupied)     :  xdot =  r (1 - x)
  NETWORK: complete graph, N patches, uniform travel time tau.
  WHITTLE INDEX  W(x) = lam x^2 - r (1-x)^2      (C25 eq. 3)

POLICIES  (leave-rules use ONE habitat scalar learned by a damped fixed point on
           the realised long-run intake rate; see brief section 1)
  whittle : leave when W(x_cur) < nu ; go to argmax_j W_j(x_j^arr)
  mvt     : leave when lam*x_cur < R*; go to argmax_j x_j^arr
  fullest : leave when x_cur < max_j x_j (current, not arrival) ; go to
            argmax_j x_j^arr
  random  : residence ~ U(0, 2 t*_MVT) ; destination uniform over the others
  where x_j^arr = 1 - (1 - x_j) exp(-r_j tau) is the state patch j will be in on
  arrival -- this is what "net of travel" means here.
"""
import math
import random
import statistics

LAM = 1.0
DT = 0.01
BURN = 200.0      # time units discarded
RUN = 1000.0       # time units scored
SEEDS = 20
NFAST = 10
NSLOW = 10
GUD_MVT = 0.30    # C25 section 5 anchor u0


def W(x, r):
    return LAM * x * x - r * (1.0 - x) ** 2


def simulate(policy, r_fast, r_slow, tau, nu, seed, nfast=NFAST, nslow=NSLOW,
             burn=BURN, run=RUN, dt=DT):
    """One trajectory.  Returns a dict of stationary statistics."""
    rng = random.Random(seed)
    N = nfast + nslow
    rr = [r_fast] * nfast + [r_slow] * nslow
    typ = [0] * nfast + [1] * nslow          # 0 = fast, 1 = slow
    x = [rng.random() for _ in range(N)]
    da = math.exp(-LAM * dt)
    gf = [math.exp(-rr[i] * dt) for i in range(N)]
    ga = [math.exp(-rr[i] * tau) for i in range(N)]   # regrowth over one transit
    t_mvt = math.log(1.0 / GUD_MVT) / LAM

    cur = rng.randrange(N)
    transit = 0.0
    dest = -1
    t = 0.0
    t_in = 0.0                       # arrival time at the current patch
    rand_target = rng.uniform(0.0, 2.0 * t_mvt) if policy == "random" else 0.0

    intake = 0.0
    gud = ([], [])
    res = ([], [])
    flips = [0, 0]                   # [type-flipped, total transits]
    dest_agree = [0, 0]              # whittle destination == fullest destination
    others = [[j for j in range(N) if j != i] for i in range(N)]

    while t < burn + run:
        scoring = t >= burn
        # ---- flow over dt -------------------------------------------------
        if dest >= 0:                                   # in transit
            for j in range(N):
                x[j] = 1.0 - (1.0 - x[j]) * gf[j]
            transit -= dt
            if transit <= 1e-12:
                cur, dest = dest, -1
                t_in = t + dt
                if policy == "random":
                    rand_target = rng.uniform(0.0, 2.0 * t_mvt)
        else:                                           # in patch cur
            xn = x[cur] * da
            if scoring:
                intake += x[cur] - xn
            x[cur] = xn
            for j in others[cur]:
                x[j] = 1.0 - (1.0 - x[j]) * gf[j]
        t += dt
        if dest >= 0:
            continue

        # ---- leave? -------------------------------------------------------
        # The leave test is evaluated every step; the destination scan and the
        # transit-reordering statistic are computed ONLY on a departure, which
        # is where the cost is.  This is an optimisation, not a rule change.
        oth = others[cur]
        if policy == "whittle":
            leave = W(x[cur], rr[cur]) < nu
        elif policy == "mvt":
            leave = LAM * x[cur] < nu
        elif policy == "fullest":
            leave = x[cur] < max(x[j] for j in oth)
        else:
            leave = (t - t_in) >= rand_target

        if leave:
            xa = {j: 1.0 - (1.0 - x[j]) * ga[j] for j in oth}
            best_other = max(oth, key=lambda j: W(xa[j], rr[j]))
            fullest_other = max(oth, key=lambda j: xa[j])
            if policy == "whittle":
                go = best_other
            elif policy == "random":
                go = rng.choice(oth)
            else:
                go = fullest_other
            if scoring:
                gud[typ[cur]].append(x[cur])
                res[typ[cur]].append(t - t_in)
                # type-reordering across transit: the best-indexed patch NOW
                # vs the best-indexed patch at the state it will be in on arrival
                now_best = max(oth, key=lambda j: W(x[j], rr[j]))
                flips[1] += 1
                if typ[now_best] != typ[best_other]:
                    flips[0] += 1
                dest_agree[1] += 1
                if best_other == fullest_other:
                    dest_agree[0] += 1
            dest = go
            transit = tau

    def m(a):
        return statistics.fmean(a) if a else float("nan")
    return dict(rate=intake / run,
                gud_fast=m(gud[0]), gud_slow=m(gud[1]),
                res_fast=m(res[0]), res_slow=m(res[1]),
                n_fast=len(gud[0]), n_slow=len(gud[1]),
                flip=flips[0] / flips[1] if flips[1] else float("nan"),
                agree=dest_agree[0] / dest_agree[1] if dest_agree[1] else float("nan"))


def learn_nu(policy, r_fast, r_slow, tau, iters=8, nfast=NFAST, nslow=NSLOW):
    """Damped fixed point nu <- (nu + realised long-run rate)/2 on short runs,
    one seed.  The converged nu is then FROZEN for the production seeds."""
    nu = 0.3
    for _ in range(iters):
        s = simulate(policy, r_fast, r_slow, tau, nu, 12345,
                     nfast=nfast, nslow=nslow, burn=60.0, run=200.0)
        nu = 0.5 * nu + 0.5 * s["rate"]
    return nu


def ci(vals):
    """Student-t 95% CI, two-sided, df = n-1."""
    v = [q for q in vals if q == q]
    n = len(v)
    if not n:
        return float("nan"), float("nan")
    mu = statistics.fmean(v)
    if n < 2:
        return mu, 0.0
    se = statistics.stdev(v) / math.sqrt(n)
    tcrit = {2: 12.706, 3: 4.303, 5: 2.776, 10: 2.262, 20: 2.093}.get(n, 2.093)
    return mu, tcrit * se


NU_GRID = [0.0, 0.01, 0.02, 0.03, 0.05, 0.07, 0.10, 0.15, 0.20, 0.25,
           0.30, 0.35, 0.40, 0.50, 0.60]


def best_nu(policy, r_fast, r_slow, tau, nfast=NFAST, nslow=NSLOW):
    """NOT pre-registered.  Post-hoc grid search for the threshold that
    MAXIMISES long-run intake, so that 'the index is a poor policy' can be told
    apart from 'the pre-registered calibration of nu is a poor calibration'."""
    best, bn = -1.0, NU_GRID[0]
    for nu in NU_GRID:
        rt = statistics.fmean(
            [simulate(policy, r_fast, r_slow, tau, nu, 500 + k, nfast=nfast,
                      nslow=nslow, burn=60.0, run=200.0)["rate"] for k in range(3)])
        if rt > best:
            best, bn = rt, nu
    return bn


def run_cell(policy, r_fast, r_slow, tau):
    nu = (0.0 if policy in ("fullest", "random")
          else learn_nu(policy, r_fast, r_slow, tau))
    out = [simulate(policy, r_fast, r_slow, tau, nu, 1000 + s) for s in range(SEEDS)]
    ratio = [o["gud_fast"] / o["gud_slow"] for o in out]
    agg = {k: ci([o[k] for o in out]) for k in
           ("rate", "gud_fast", "gud_slow", "res_fast", "res_slow", "flip", "agree")}
    agg["ratio"] = ci(ratio)
    agg["nu"] = (nu, 0.0)
    agg["_raw"] = out
    return agg


def main():
    tau0 = 1.0 / LAM
    r_slow = 0.02 / tau0
    print(__doc__)
    print("dt = %.3g   burn-in = %g   scored run = %g   seeds = %d   N = %d\n"
          % (DT, BURN, RUN, SEEDS, NFAST + NSLOW))

    print("TABLE 1 - baseline  r_fast*tau = 0.2, r_slow*tau = 0.02, tau = 1/lam")
    print("%-9s %8s %9s %9s %9s %9s %9s %9s"
          % ("policy", "nu/R*", "rate", "GUD_f", "GUD_s", "res_f", "res_s", "flip"))
    base = {}
    for pol in ("whittle", "mvt", "fullest", "random"):
        a = run_cell(pol, 0.2, r_slow, tau0)
        base[pol] = a
        print("%-9s %8.4f %9.4f %9.4f %9.4f %9.4f %9.4f %9.4f"
              % (pol, a["nu"][0], a["rate"][0], a["gud_fast"][0], a["gud_slow"][0],
                 a["res_fast"][0], a["res_slow"][0], a["flip"][0]))
    print()
    for pol in ("whittle", "mvt", "fullest", "random"):
        a = base[pol]
        print("  %-9s fast/slow GUD ratio = %.4f +/- %.4f   rate = %.4f +/- %.4f"
              % (pol, a["ratio"][0], a["ratio"][1], a["rate"][0], a["rate"][1]))

    # P4 - value of the index, paired across seeds
    marg = [100.0 * (w["rate"] / m["rate"] - 1.0)
            for w, m in zip(base["whittle"]["_raw"], base["mvt"]["_raw"])]
    mm, mh = ci(marg)
    print("\nP4  VALUE OF THE INDEX (whittle vs mvt, paired by seed):"
          " %+.2f%% +/- %.2f%%" % (mm, mh))
    for other in ("fullest", "random"):
        m2, h2 = ci([100.0 * (w["rate"] / g["rate"] - 1.0)
                     for w, g in zip(base["whittle"]["_raw"], base[other]["_raw"])])
        print("    (whittle vs %-8s %+.2f%% +/- %.2f%%)" % (other + ":", m2, h2))

    print("\nTABLE 2 - sweep  r_fast*tau in {0.05, 0.2, 1, 10} x tau in {0.5, 1, 2}/lam")
    print("   r_slow held FIXED in absolute units at %.4f*lam\n" % r_slow)
    print("%6s %6s %8s %9s %9s %9s %9s %9s %9s"
          % ("tau", "rf*tau", "policy", "GUD_f", "GUD_s", "ratio", "+/-", "flip", "rate"))
    sweep = {}
    for tau in (0.5, 1.0, 2.0):
        for rt in (0.05, 0.2, 1.0, 10.0):
            rf = rt / tau
            for pol in ("whittle", "mvt"):
                a = run_cell(pol, rf, r_slow, tau)
                sweep[(tau, rt, pol)] = a
                print("%6.1f %6.2f %8s %9.4f %9.4f %9.4f %9.4f %9.4f %9.4f"
                      % (tau, rt, pol, a["gud_fast"][0], a["gud_slow"][0],
                         a["ratio"][0], a["ratio"][1], a["flip"][0], a["rate"][0]))

    print("\n    value of the index across the sweep (whittle rate / mvt rate - 1):")
    for tau in (0.5, 1.0, 2.0):
        for rt in (0.05, 0.2, 1.0, 10.0):
            w = sweep[(tau, rt, "whittle")]["_raw"]
            v = sweep[(tau, rt, "mvt")]["_raw"]
            mu, h = ci([100.0 * (a["rate"] / b["rate"] - 1.0) for a, b in zip(w, v)])
            print("      tau=%.1f rf*tau=%5.2f : %+7.2f%% +/- %.2f%%" % (tau, rt, mu, h))

    print("\nP3  transit type-flip fraction vs tau at r_fast*tau = 0.2 (whittle):")
    for tau in (0.5, 1.0, 2.0):
        a = sweep[(tau, 0.2, "whittle")]
        print("    tau = %.1f : flip = %.4f +/- %.4f" % (tau, a["flip"][0], a["flip"][1]))

    print("\n    slow-patch visit counts per scored run (whittle), by cell:")
    for tau in (0.5, 1.0, 2.0):
        row = " ".join("rf*tau=%-5.2f n_slow=%-6.1f" %
                       (rt, statistics.fmean([o["n_slow"] for o in
                                              sweep[(tau, rt, "whittle")]["_raw"]]))
                       for rt in (0.05, 0.2, 1.0, 10.0))
        print("      tau=%.1f : %s" % (tau, row))

    print("\nTABLE 3 - POST-HOC rate-optimal thresholds (NOT pre-registered),")
    print("   baseline cell; grid = %s" % NU_GRID)
    print("%-9s %9s %9s %9s %9s %9s" %
          ("policy", "nu*", "rate", "GUD_f", "GUD_s", "ratio"))
    opt = {}
    for pol in ("whittle", "mvt"):
        nu = best_nu(pol, 0.2, r_slow, tau0)
        out = [simulate(pol, 0.2, r_slow, tau0, nu, 1000 + s) for s in range(SEEDS)]
        opt[pol] = out
        r_, _ = ci([o["rate"] for o in out])
        gf, _ = ci([o["gud_fast"] for o in out])
        gs, _ = ci([o["gud_slow"] for o in out])
        rr_, rh = ci([o["gud_fast"] / o["gud_slow"] for o in out])
        print("%-9s %9.3f %9.4f %9.4f %9.4f %9.4f +/- %.4f"
              % (pol, nu, r_, gf, gs, rr_, rh))
    mu, h = ci([100.0 * (a["rate"] / b["rate"] - 1.0)
                for a, b in zip(opt["whittle"], opt["mvt"])])
    print("   VALUE OF THE INDEX at each policy's own best threshold:"
          " %+.2f%% +/- %.2f%%" % (mu, h))

    print("\nTABLE 4 - the C25 ANCHOR nu = lam*GUD_MVT^2 = %.4f, baseline cell."
          % (GUD_MVT ** 2))
    print("   C25 section 5 anchors nu at the MVT baseline, NOT at the learned")
    print("   network rate.  This is the reconciliation cell.")
    nu_a = GUD_MVT ** 2
    out = [simulate("whittle", 0.2, r_slow, tau0, nu_a, 1000 + s) for s in range(SEEDS)]
    for k in ("rate", "gud_fast", "gud_slow", "res_fast", "res_slow", "flip"):
        mu, h = ci([o[k] for o in out])
        print("   %-9s %.4f +/- %.4f" % (k, mu, h))
    mu, h = ci([o["gud_fast"] / o["gud_slow"] for o in out])
    print("   %-9s %.4f +/- %.4f" % ("ratio", mu, h))
    mu, h = ci([100.0 * (a["rate"] / b["rate"] - 1.0)
                for a, b in zip(out, base["mvt"]["_raw"])])
    print("   value of the index at the C25 anchor: %+.2f%% +/- %.2f%%" % (mu, h))

    print("\nP5  HOMOGENEOUS DEGENERACY (all 20 patches identical, 5 seeds)")
    print("%8s %9s %9s %9s %11s" % ("r*tau", "nu", "GUD", "rate", "destagree"))
    for r in (0.05, 0.2, 1.0, 10.0):
        nu = learn_nu("whittle", r, r, tau0, nfast=20, nslow=0)
        out = [simulate("whittle", r, r, tau0, nu, 1000 + s, nfast=20, nslow=0)
               for s in range(5)]
        g, _ = ci([o["gud_fast"] for o in out])
        rt_, _ = ci([o["rate"] for o in out])
        ag, _ = ci([o["agree"] for o in out])
        print("%8.2f %9.4f %9.4f %9.4f %11.4f" % (r, nu, g, rt_, ag))


if __name__ == "__main__":
    main()
