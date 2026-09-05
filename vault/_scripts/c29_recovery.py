#!/usr/bin/env python3
"""
c29_recovery.py - Weibull hazard shape of ECOLOGICAL RECOVERY, with right-censoring.

WHAT THIS COMPUTES
------------------
[[C18-durability-axis]] established that the shared durability coordinate is the Weibull
SHAPE parameter `beta`, not a mean count, and that ecology-adjacent fields publish means
while reliability publishes distributions.  [[G32-recovery-time-hazard-shape]] claims the
same asymmetry for disturbance ecology: ecology reports a MEAN return time (Pimm 1984),
reliability reports (beta, eta).

This script computes the missing object: `beta` for ecological recovery times, fitted as a
right-censored survival problem.

DATA
----
Jones, H.P. & Schmitz, O.J. (2009) "Rapid Recovery of Damaged Ecosystems", PLoS ONE 4(5):
e5653, doi 10.1371/journal.pone.0005653.  Table S1 (open supplement, .xls) tabulates 240
recovery studies with columns:

    Habitat | Disturbance | Response Variable(s) | Recovered? | Return Time | Control | Citation

Rows 1-240 are data; rows 241+ of the same sheet are the reference list and are discarded.

SURVIVAL CODING (the whole methodological content of this script)
-----------------------------------------------------------------
    "Recovered? = Yes*"  -> EVENT   at the stated Return Time  (recovery observed)
    "Recovered? = No*"   -> RIGHT-CENSORED at the stated time  (study ended, no recovery)

Ecology's own "mean return time" is the mean of the EVENT rows only; that estimator throws
away every censored row, which is exactly the population that carries the recovery debt.

The Weibull survival is  S(t) = exp(-(t/eta)^beta),  hazard h(t) = (beta/eta)(t/eta)^(beta-1):

    beta > 1  hazard RISES with time since disturbance -> recovery "accelerates" (memory)
    beta = 1  memoryless: a constant per-year chance of recovering, no matter how long
    beta < 1  hazard FALLS: recover early or effectively never  ("recovery debt")

MLE with right-censoring (eta profiled out analytically):

    logL(beta) = d*log(beta) - d*beta*log(eta_hat(beta))
                 + (beta-1)*sum_{events} log t_i - sum_{all} (t_i/eta_hat)^beta
    eta_hat(beta) = ( sum_{all} t_i^beta / d )^(1/beta),   d = number of events

CI on beta by PROFILE LIKELIHOOD (chi2_1 at 95%: drop of 1.921 in logL), not by a normal
approximation - beta is bounded below by 0 and the profile is asymmetric.

DEPENDENCIES
------------
    numpy, scipy, xlrd   (xlrd >= 2.0 reads the legacy .xls this supplement is served as;
                          openpyxl cannot read .xls)

USAGE
-----
    python c29_recovery.py                # downloads the supplement, fits, prints tables
    python c29_recovery.py --xls FILE     # use an already-downloaded copy
    python c29_recovery.py --range low    # sensitivity: use the low end of "3-4 years"
                                          # (default 'mid'; also 'high')
"""

import argparse
import collections
import re
import sys
import urllib.request

import numpy as np
from scipy.optimize import brentq, minimize_scalar

SUPPLEMENT_URL = (
    "https://journals.plos.org/plosone/article/file"
    "?type=supplementary&id=info:doi/10.1371/journal.pone.0005653.s001"
)
N_DATA_ROWS = 240  # rows 1..240 of Sheet1; 241+ is the appended reference list

# ---------------------------------------------------------------- time parsing

_UNIT_YEARS = {
    "day": 1.0 / 365.25,
    "week": 7.0 / 365.25,
    "month": 1.0 / 12.0,
    "year": 1.0,
    "yr": 1.0,
    "decade": 10.0,
    "century": 100.0,
    "centurie": 100.0,  # "centuries" after the trailing-s strip
}

_UNITS = ("day|days|week|weeks|month|months|year|years|yr|yrs"
          "|decade|decades|century|centuries")

_TIME_RE = re.compile(
    r"(\d+(?:\.\d+)?)\s*(?:-|to|–)\s*(\d+(?:\.\d+)?)\s*(" + _UNITS + r")"
    r"|(\d+(?:\.\d+)?)\s*(" + _UNITS + r")",
    re.I,
)


def _unit_years(tok):
    return _UNIT_YEARS[tok.lower().rstrip("s") if tok.lower() != "yrs" else "yr"]


def parse_time_years(text, range_mode="mid"):
    """First time expression in a free-text Return Time cell, in years, or None.

    Ranges ('3-4 years', '50 - 70 years') are collapsed by `range_mode`.
    Qualifiers ('~', '>', 'at least') are ignored: the number is taken at face value,
    which for a '>50 years' NOT-RECOVERED row is the correct censoring time anyway.
    """
    m = _TIME_RE.search(text)
    if not m:
        return None
    if m.group(3):
        lo, hi = float(m.group(1)), float(m.group(2))
        v = {"mid": (lo + hi) / 2.0, "low": lo, "high": hi}[range_mode]
        return v * _unit_years(m.group(3))
    return float(m.group(4)) * _unit_years(m.group(5))


def habitat_group(h):
    for g in ("Forest", "Marine", "Freshwater", "Brackish", "Terrestrial"):
        if h.startswith(g):
            return g
    return None


# ---------------------------------------------------------------- Weibull MLE

def _neg_logL(beta, t, e):
    """Negative profile log-likelihood in beta (eta concentrated out)."""
    d = float(e.sum())
    with np.errstate(over="ignore"):  # the bracket search probes absurd beta
        eta = ((t ** beta).sum() / d) ** (1.0 / beta)
        if not np.isfinite(eta) or eta <= 0:
            return 1e12
        return -(d * np.log(beta) - d * beta * np.log(eta)
                 + (beta - 1.0) * np.log(t[e == 1]).sum()
                 - ((t / eta) ** beta).sum())


def fit_weibull(pairs, level=1.920729):
    """(n, n_events, n_censored, beta, lo, hi, eta) for [(time, event), ...]."""
    t = np.asarray([p[0] for p in pairs], float)
    e = np.asarray([p[1] for p in pairs], int)
    if e.sum() < 3:
        return None
    r = minimize_scalar(_neg_logL, bounds=(0.02, 25.0), args=(t, e), method="bounded")
    beta, l0 = r.x, r.fun

    def gap(b):
        return _neg_logL(b, t, e) - l0 - level

    lo = brentq(gap, 1e-3, beta) if gap(1e-3) > 0 else float("nan")
    hi = brentq(gap, beta, 60.0) if gap(60.0) > 0 else float("nan")
    eta = ((t ** beta).sum() / e.sum()) ** (1.0 / beta)
    return (len(t), int(e.sum()), len(t) - int(e.sum()), beta, lo, hi, eta)


# ---------------------------------------------------------------- data loading

def load_rows(xls_path=None):
    import xlrd
    if xls_path:
        book = xlrd.open_workbook(xls_path)
    else:
        req = urllib.request.Request(
            SUPPLEMENT_URL,
            headers={"User-Agent": "biomimicry-vault/1.0 (mailto:deciduusleaf@gmail.com)"},
        )
        book = xlrd.open_workbook(file_contents=urllib.request.urlopen(req, timeout=120).read())
    sh = book.sheet_by_index(0)
    return [[str(sh.cell_value(r, c)).strip() for c in range(7)]
            for r in range(1, min(N_DATA_ROWS + 1, sh.nrows))]


def build(rows, range_mode="mid"):
    by_habitat = collections.defaultdict(list)
    by_disturbance = collections.defaultdict(list)
    dropped = collections.Counter()
    for r in rows:
        g = habitat_group(r[0])
        if g is None:
            dropped["habitat not one of the five groups"] += 1
            continue
        t = parse_time_years(r[4], range_mode)
        if t is None or t <= 0:
            dropped["Return Time carries no parseable duration"] += 1
            continue
        s = r[3].strip().lower()
        if s.startswith("yes"):
            ev = 1
        elif s.startswith("no"):
            ev = 0
        else:
            dropped["Recovered? neither yes nor no"] += 1
            continue
        by_habitat[g].append((t, ev))
        by_disturbance[r[1].strip()].append((t, ev))
    return by_habitat, by_disturbance, dropped


# ---------------------------------------------------------------- report

def _line(label, f):
    if f is None:
        return f"{label:<22s}  (too few events to fit)"
    n, ev, cn, b, lo, hi, eta = f
    star = "*" if hi < 1.0 else (" " if lo < 1.0 < hi else "+")
    return (f"{label:<22s} {n:4d} {ev:4d} {cn:4d}   {b:5.3f}  [{lo:5.3f}, {hi:5.3f}] "
            f"{eta:8.2f}  {star}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--xls", default=None)
    ap.add_argument("--range", dest="range_mode", default="mid",
                    choices=["mid", "low", "high"])
    args = ap.parse_args()

    rows = load_rows(args.xls)
    by_hab, by_dist, dropped = build(rows, args.range_mode)
    pooled = [x for v in by_hab.values() for x in v]

    print(f"Jones & Schmitz 2009 Table S1 (doi 10.1371/journal.pone.0005653.s001)")
    print(f"data rows read: {len(rows)}   usable: {len(pooled)}   range coding: {args.range_mode}")
    for k, v in dropped.most_common():
        print(f"  dropped {v:3d}: {k}")
    print()
    hdr = f"{'group':<22s} {'N':>4s} {'ev':>4s} {'cens':>4s}   {'beta':>5s}  {'95% profile CI':>16s} {'eta(yr)':>8s}"
    print(hdr); print("-" * len(hdr))
    for k in ("Forest", "Marine", "Freshwater", "Brackish", "Terrestrial"):
        print(_line(k, fit_weibull(by_hab[k])))
    print(_line("ALL POOLED", fit_weibull(pooled)))
    print("  * = CI entirely below 1 (decreasing hazard); + = entirely above 1")
    print()
    print("by disturbance type (N >= 10 only):")
    print(hdr); print("-" * len(hdr))
    for k, v in sorted(by_dist.items(), key=lambda kv: -len(kv[1])):
        if len(v) >= 10:
            print(_line(k, fit_weibull(v)))
    print()
    print("sensitivity:")
    print(_line("events only (no cens.)", fit_weibull([(t, 1) for t, e in pooled if e == 1])))
    for mode in ("low", "high"):
        h, _, _ = build(rows, mode)
        print(_line(f"pooled, range={mode}", fit_weibull([x for v in h.values() for x in v])))
    print()
    print("ecology's own estimator, for contrast:")
    ev_t = [t for t, e in pooled if e == 1]
    print(f"  mean return time over RECOVERED rows only = {np.mean(ev_t):.2f} yr "
          f"(n = {len(ev_t)}); it cannot see the {sum(1 for _, e in pooled if e == 0)} "
          f"censored rows at all.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
