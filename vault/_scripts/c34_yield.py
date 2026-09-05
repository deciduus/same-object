#!/usr/bin/env python3
"""
c34_yield.py - the clustering parameter `alpha` for genetic load, and the
Poisson-vs-negative-binomial mean-fitness comparison.  Stdlib only.

    python c34_yield.py

WHAT THIS COMPUTES
------------------
Semiconductor yield engineering writes die yield two ways:

    Poisson (Murphy 1964 limit) :  Y = exp(-A*D0)
    Stapper 1983 (clustered)    :  Y = (1 + A*D0/alpha)^(-alpha)     -> Poisson as alpha -> inf

`alpha` is the negative-binomial clustering parameter: small alpha = defects
strongly clustered on the wafer, and clustering RAISES yield above the Poisson
prediction at the same mean defect count.  Fitted alpha for real wafer lines is
of order 0.3-5 (Stapper 1983; Cunningham 1990).

Population genetics writes the Haldane-Muller principle as

    W_bar = exp(-U)

with `U` the genomic deleterious mutation rate, and has no alpha.  The genetic
analogue of defect clustering is OVERDISPERSION of the per-individual mutation
count: mutations are Poisson within an individual but the Poisson mean varies
BETWEEN individuals (here: with parental age), so the marginal count is a
Poisson mixture and therefore negative binomial with

    alpha = E[lambda]^2 / Var[lambda]

ROUTE (and why it is the defensible one)
----------------------------------------
Per-individual de novo mutation (DNM) counts are modelled, in the source
literature itself, as Poisson with a mean linear in parental age:

    lambda(f, m) = c + b_f*f + b_m*m

so Var[lambda] across a cohort is fixed by the published regression slopes and
the cohort's parental-age variances:

    Var[lambda] = b_f^2 s_f^2 + b_m^2 s_m^2 + 2*b_f*b_m*rho*s_f*s_m

No per-trio table is needed.  Uncertainty is propagated by Monte Carlo over the
inputs, each drawn from its published (or, where marked, ASSUMED) interval.

THINNING INVARIANCE - the step that makes this transferable
-----------------------------------------------------------
Only a small fraction p of DNMs are deleterious, so U = p * mu.  If the total
count is NB(mu, alpha) and each mutation is independently deleterious with
probability p, the deleterious count is NB(p*mu, alpha) -- SAME alpha.
(NB is a gamma-Poisson mixture; thinning Poisson(lambda) gives Poisson(p*lambda),
and p*Gamma(alpha, theta) = Gamma(alpha, p*theta), whose shape is still alpha.)
So an alpha fitted on *total* DNM counts is the alpha that belongs in the load
formula, and the unknown p cancels.  This is checked numerically below.

INPUTS - every one with its source
----------------------------------
  b_f = 1.51 mutations per year of father's age   Jonsson et al. 2017, Nature 549:519,
  b_m = 0.37 mutations per year of mother's age   doi 10.1038/nature24018 (1,548 Icelandic
  mu  = 70.0 mean DNMs per proband                trios).  Crossref-verified 2026-09-05.
  (cross-check: Kong et al. 2012, doi 10.1038/nature11396, 78 trios, mean 63.2,
   ~2.0 per paternal year -- same order, run as a sensitivity case below.)

  s_f = 6.0 y, s_m = 5.0 y, rho = 0.7   ASSUMED / UNSOURCED.  The parental-age
  standard deviations and their correlation are NOT tabulated in the source
  papers' main text.  They are the dominant uncertainty and are swept, not
  asserted: alpha is reported as a function of s_f as well as a point estimate.

  U   = 1.2 deleterious mutations per diploid genome per generation, with 0.5-2.2
  swept.  Human U_del estimates span roughly this range; treated as a swept input,
  not a fetched number.  UNVERIFIED as a point value.

  alpha_wafer = 0.3-5   Stapper 1983 / Cunningham 1990 fitted range, as reported
  in the yield-model literature.  Used only as a contrast case.  UNVERIFIED
  (secondary-source range, not read off a table in this run).
"""

import math
import random

# ---------------------------------------------------------------- inputs
MU_J, BF_J, BM_J = 70.0, 1.51, 0.37      # Jonsson 2017
MU_K, BF_K, BM_K = 63.2, 2.01, 0.37      # Kong 2012 (b_m not separately reported; reused)
SF, SM, RHO = 6.0, 5.0, 0.7              # ASSUMED
N_MC = 200000
random.seed(20260905)


def alpha_from_mixture(mu, bf, bm, sf, sm, rho):
    """alpha = E[lambda]^2 / Var[lambda] for lambda linear in parental ages."""
    var = (bf * sf) ** 2 + (bm * sm) ** 2 + 2.0 * bf * bm * rho * sf * sm
    return mu * mu / var, var


def w_poisson(u):
    return math.exp(-u)


def w_nb(u, a):
    return (1.0 + u / a) ** (-a)


def mc_alpha(mu, bf, bm, n=N_MC):
    """Monte Carlo interval for alpha over the uncertain inputs."""
    out = []
    for _ in range(n):
        f = bf * random.uniform(0.93, 1.07)          # +-7% on the published slope
        m = bm * random.uniform(0.80, 1.20)
        sf = random.uniform(4.0, 8.0)                # the ASSUMED input, swept wide
        sm = random.uniform(3.5, 6.5)
        rho = random.uniform(0.45, 0.90)
        mm = mu * random.uniform(0.95, 1.05)
        a, _ = alpha_from_mixture(mm, f, m, sf, sm, rho)
        out.append(a)
    out.sort()
    return out[int(0.5 * n)], out[int(0.025 * n)], out[int(0.975 * n)]


def check_thinning(alpha, mu, p=0.017, n=400000):
    """Numerically confirm alpha survives Poisson thinning (gamma-Poisson route)."""
    theta = mu / alpha
    tot = dl = tot2 = dl2 = 0.0
    for _ in range(n):
        lam = random.gammavariate(alpha, theta)
        k = _pois(lam)
        d = sum(1 for _ in range(k) if random.random() < p)
        tot += k; tot2 += k * k
        dl += d; dl2 += d * d
    mt, vt = tot / n, tot2 / n - (tot / n) ** 2
    md, vd = dl / n, dl2 / n - (dl / n) ** 2
    at = mt * mt / (vt - mt) if vt > mt else float("inf")
    ad = md * md / (vd - md) if vd > md else float("inf")
    return (mt, at), (md, ad)


def _pois(lam):
    """Knuth for small lam, normal approx above 30 (adequate for a moment check)."""
    if lam < 30:
        L, k, p = math.exp(-lam), 0, 1.0
        while True:
            k += 1
            p *= random.random()
            if p <= L:
                return k - 1
    return max(0, int(round(random.gauss(lam, math.sqrt(lam)))))


def main():
    print("=" * 74)
    print("C34 - clustering parameter alpha for genetic load")
    print("=" * 74)

    a_j, var_j = alpha_from_mixture(MU_J, BF_J, BM_J, SF, SM, RHO)
    a_k, var_k = alpha_from_mixture(MU_K, BF_K, BM_K, SF, SM, RHO)
    print("\n[1] Point estimates (Var[lambda] from published age slopes)")
    print("  Jonsson 2017 : mu=%.1f  Var[lambda]=%.1f  ->  alpha = %.1f"
          % (MU_J, var_j, a_j))
    print("  Kong 2012    : mu=%.1f  Var[lambda]=%.1f  ->  alpha = %.1f"
          % (MU_K, var_k, a_k))

    med, lo, hi = mc_alpha(MU_J, BF_J, BM_J)
    print("\n[2] Monte Carlo over the uncertain inputs (n=%d)" % N_MC)
    print("  alpha = %.1f   95%% interval [%.1f, %.1f]" % (med, lo, hi))
    print("  (the interval is dominated by s_f, which is ASSUMED, not fetched)")

    print("\n[3] alpha as a function of the assumed paternal-age SD")
    print("  s_f (y) |  Var[lambda] |  alpha")
    for sf in (3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 10.0):
        a, v = alpha_from_mixture(MU_J, BF_J, BM_J, sf, SM, RHO)
        print("   %5.1f  |    %7.1f  | %6.1f" % (sf, v, a))

    print("\n[4] Thinning invariance check (simulation)")
    (mt, at), (md, ad) = check_thinning(a_j, MU_J, p=1.2 / MU_J)
    print("  total       : mean %.2f  alpha_hat %.1f  (target %.1f)" % (mt, at, a_j))
    print("  deleterious : mean %.3f  alpha_hat %.1f  (target %.1f)" % (md, ad, a_j))
    print("  -> alpha is preserved under thinning; p cancels, as proved above.")

    print("\n[5] Mean fitness: Haldane-Muller exp(-U) vs Stapper (1+U/alpha)^(-alpha)")
    print("     U   alpha |  exp(-U)  |   NB      | NB/Poisson | excess")
    for u in (0.5, 1.2, 2.2):
        for a in (a_j, lo, hi, 5.0, 3.0, 0.3):
            wp, wn = w_poisson(u), w_nb(u, a)
            print("  %4.1f  %6.1f | %8.5f  | %8.5f  |  %7.4f   | %+6.2f%%"
                  % (u, a, wp, wn, wn / wp, 100.0 * (wn / wp - 1.0)))
        print("  " + "-" * 66)

    print("\n[6] Small-U expansion (why the excess is ~U^2/2alpha)")
    for u, a in ((1.2, a_j), (2.2, a_j), (1.2, 3.0)):
        print("  U=%.1f alpha=%.1f : exact %+.4f%%   approx exp(U^2/2a)-1 = %+.4f%%"
              % (u, a, 100.0 * (w_nb(u, a) / w_poisson(u) - 1.0),
                 100.0 * (math.exp(u * u / (2 * a)) - 1.0)))

    print("\n[7] What alpha would have to be to matter at the 10%% level, per U")
    for u in (0.5, 1.2, 2.2, 5.0):
        # solve exp(U^2/2a) = 1.10
        a = u * u / (2.0 * math.log(1.10))
        print("  U=%.1f  ->  alpha <= %.2f" % (u, a))


if __name__ == "__main__":
    main()
