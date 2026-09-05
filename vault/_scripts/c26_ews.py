#!/usr/bin/env python3
"""
c26_ews.py - put an ecological early-warning series and an engineering run-to-failure
dataset on ONE Weibull shape axis (beta).  Backs vault/computed/C26-ews-hazard-shape.md
and the gap vault/gaps/G29-early-warning-prognostics.md.

WHY THIS SCRIPT EXISTS
----------------------
Ecology reports critical slowing down as a *trend* in an indicator (rising lag-1
autocorrelation, rising variance).  Prognostics reports a *hazard*: a degradation model
run to a threshold, giving a remaining-useful-life distribution with a shape parameter.
Neither field has the other's object.  This computes the missing one: the Weibull shape
parameter beta implied by an ecological early-warning series, on the same axis as beta
fitted to engineering run-to-failure data.

ESTIMATORS (two, deliberately)
------------------------------
R1  Direct Weibull MLE on a SAMPLE OF FAILURE TIMES.  Engineering only - ecology has one
    transition per series, so R1 is not computable there.  That asymmetry is C18's
    finding ("everyone reports the mean; only one side reports the distribution")
    transplanted into ecology.
R2  Degradation-to-threshold.  Fit a Wiener process  D(t) = D0 + mu*t + sigma*W(t)  to a
    degradation / early-warning signal; its first-passage time to a threshold L is
    Inverse Gaussian IG(m = (L-D0)/mu, lam = (L-D0)^2/sigma^2); report the Weibull that
    best matches that IG over the 1%-99% quantile range (least squares on log(-log S)
    against log t).  R2 IS computable on a single ecological series, and is applied to
    BOTH sides, so the ecology and engineering numbers are one estimator, not two.

R2 is the Si (2011) EJOR review's own estimator family (Wiener degradation to a failure
threshold, first-passage RUL) applied to the Dakos/Scheffer early-warning indicator.
That composition is the object G29 says nobody has built.

DATA - all public; the script downloads to ./c26_data and caches (--offline reuses it)
--------------------------------------------------------------------------------------
  ECOLOGY      `YD2PB_grayscale`: Cariaco Basin greyscale, Younger Dryas -> Preboreal
               transition, 2,111 points.  Shipped with the `earlywarnings` R package;
               it is the series behind Dakos et al. 2008 PNAS 105:14308
               (doi 10.1073/pnas.0802430105).
               https://github.com/earlywarningtoolbox/earlywarnings-R -> data/*.rda
  ECOLOGY      `circulation`: a model thermohaline-circulation collapse series, 783
               points, same package.  MODEL OUTPUT, not field data - labelled as such
               in the result table and NOT used for the headline claim.
  ENGINEERING  NASA C-MAPSS turbofan degradation simulation, train_FD001 (100 units, one
               fault mode, one operating condition) and train_FD004 (249 units, two
               fault modes, six conditions).  NASA Prognostics Data Repository; fetched
               from the mirror at
               https://github.com/hankroark/Turbofan-Engine-Degradation/CMAPSSData

  NOT USED, and why:
   - IMS bearing run-to-failure set (NASA/Univ. Cincinnati): ~6 GB of raw vibration.
     Out of budget for a desk session.  Its published beta belongs in this table.
   - Carpenter et al. 2011 Science (doi 10.1126/science.1203672), the Peter Lake
     whole-ecosystem experiment: no machine-readable public archive of the chlorophyll
     series was reachable.  Numbers from that paper are therefore NOT in the table.

Stdlib + numpy only.  Usage:  python c26_ews.py [--offline] [--boot 400]
"""
import argparse
import gzip
import json
import math
import os
import struct
import urllib.request

import numpy as np

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "c26_data")
UA = {"User-Agent": "biomimicry-vault/1.0 (mailto:deciduusleaf@gmail.com)"}
EWS_RAW = "https://raw.githubusercontent.com/earlywarningtoolbox/earlywarnings-R/master/data/"
CMAPSS = "https://raw.githubusercontent.com/hankroark/Turbofan-Engine-Degradation/master/CMAPSSData/"


def fetch(url, name, offline):
    os.makedirs(DATA, exist_ok=True)
    p = os.path.join(DATA, name)
    if os.path.exists(p):
        return p
    if offline:
        raise SystemExit("missing %s and --offline was given" % p)
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180) as r:
        open(p, "wb").write(r.read())
    return p


# ------------------------------------------------------------------ .rda reader
class _RDA:
    """Minimal XDR RData v2 reader - enough for a data.frame of numeric columns."""

    def __init__(self, b):
        self.b, self.i, self.refs = b, 0, []

    def i4(self):
        v = struct.unpack(">i", self.b[self.i:self.i + 4])[0]
        self.i += 4
        return v

    def rd(self):
        f = self.i4()
        t, ha, ht = f & 0xFF, (f >> 9) & 1, (f >> 10) & 1
        if t == 255:                                  # REFSXP, index in the high bits
            idx = f >> 8
            if idx == 0:
                idx = self.i4()
            return self.refs[idx - 1]
        if t == 254:                                  # NILVALUE
            return None
        if t == 1:                                    # SYMSXP
            v = self.rd()
            self.refs.append(v)
            return v
        if t in (2, 6, 17):                           # pairlist / language
            out = {}
            while True:
                tag = self.rd() if ht else None
                if ha:
                    self.rd()
                out[tag] = self.rd()
                f = self.i4()
                t2, ht, ha = f & 0xFF, (f >> 10) & 1, (f >> 9) & 1
                if t2 != 2:
                    break
            return out
        if t == 9:                                    # CHARSXP
            n = self.i4()
            if n == -1:
                return None
            v = self.b[self.i:self.i + n].decode("utf-8", "replace")
            self.i += n
            return v
        if t in (10, 13):                             # LGLSXP / INTSXP
            n = self.i4()
            v = [self.i4() for _ in range(n)]
        elif t == 14:                                 # REALSXP
            n = self.i4()
            v = list(struct.unpack(">%dd" % n, self.b[self.i:self.i + 8 * n]))
            self.i += 8 * n
        elif t in (16, 19):                           # STRSXP / VECSXP
            n = self.i4()
            v = [self.rd() for _ in range(n)]
        else:
            raise ValueError("unhandled SEXP type %d" % t)
        if ha:
            self.rd()                                 # attributes, discarded
        return v


def read_rda(path):
    b = open(path, "rb").read()
    raw = gzip.decompress(b) if b[:2] == b"\x1f\x8b" else b
    p = _RDA(raw[raw.index(b"X\n") + 2:])
    p.i4(); p.i4(); p.i4()                            # version / writer / reader
    out = {}
    while True:
        f = struct.unpack(">i", p.b[p.i:p.i + 4])[0]
        if (f & 0xFF) == 254:
            break
        p.i += 4
        tag = p.rd() if (f >> 10) & 1 else None
        out[tag] = p.rd()
    return out


# ------------------------------------------------------------------ estimators
def weibull_mle(t):
    """Newton solve for the two-parameter Weibull MLE.  Returns (beta, eta)."""
    t = np.asarray(t, float)
    t = t[t > 0]
    lt = np.log(t)
    b = 1.0
    for _ in range(500):
        tb = t ** b
        s0, s1, s2 = tb.sum(), (tb * lt).sum(), (tb * lt * lt).sum()
        g = s1 / s0 - 1.0 / b - lt.mean()
        dg = (s2 * s0 - s1 * s1) / s0 ** 2 + 1.0 / b ** 2
        step = g / dg
        b = max(b - step, 1e-6)
        if abs(step) < 1e-12:
            break
    eta = ((t ** b).mean()) ** (1.0 / b)
    return float(b), float(eta)


def _ig_cdf(x, m, lam):
    if x <= 0:
        return 0.0
    a = math.sqrt(lam / x)
    z1, z2 = a * (x / m - 1.0), a * (x / m + 1.0)
    phi = lambda z: 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))
    return phi(z1) + math.exp(min(2.0 * lam / m, 700.0)) * phi(-z2)


def ig_to_weibull(m, lam, qlo=0.01, qhi=0.99, n=300):
    """Weibull (beta, eta) matching an Inverse-Gaussian first-passage law over
    [qlo, qhi], by least squares on log(-log S) vs log t."""
    def inv(p):
        lo, hi = 1e-12, max(m, 1e-9)
        while _ig_cdf(hi, m, lam) < p and hi < 1e15:
            hi *= 2.0
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if _ig_cdf(mid, m, lam) < p:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)

    ps = np.linspace(qlo, qhi, n)
    xs = np.array([inv(p) for p in ps])
    ok = xs > 0
    if ok.sum() < 10:
        return None
    X, Y = np.log(xs[ok]), np.log(-np.log(1.0 - ps[ok]))
    beta, c = np.polyfit(X, Y, 1)
    return float(beta), float(math.exp(-c / beta))


def wiener_fpt_beta(sig, L, dt=1.0):
    """Fit D(t)=D0+mu t+sigma W(t) to `sig`; first-passage to L; Weibull-equivalent beta.
    Returns dict or None when the drift does not point at the threshold."""
    sig = np.asarray(sig, float)
    if len(sig) < 20:
        return None
    d = np.diff(sig)
    mu = d.mean() / dt
    sigma = d.std(ddof=1) / math.sqrt(dt)
    gap = L - sig[0]
    if mu <= 0 or gap <= 0 or sigma <= 0:
        return None
    m = gap / mu
    lam = gap * gap / (sigma * sigma)
    fit = ig_to_weibull(m, lam)
    if fit is None:
        return None
    return dict(beta=fit[0], eta=fit[1], mu=mu, sigma=sigma, m_fpt=m, lam=lam)


def ar1_indicator(x, win_frac=0.5, bw_frac=0.05):
    """Gaussian-kernel detrend, then rolling lag-1 autocorrelation - the standard
    critical-slowing-down indicator (Dakos et al. 2008; earlywarnings::generic_ews,
    default half-series window)."""
    x = np.asarray(x, float)
    n = len(x)
    bw = max(3.0, bw_frac * n)
    idx = np.arange(n)
    trend = np.array([(np.exp(-0.5 * ((idx - i) / bw) ** 2) * x).sum() /
                      np.exp(-0.5 * ((idx - i) / bw) ** 2).sum() for i in range(n)])
    r = x - trend
    win = max(20, int(win_frac * n))
    out = []
    for i in range(win, n + 1):
        seg = r[i - win:i]
        a, b = seg[:-1] - seg[:-1].mean(), seg[1:] - seg[1:].mean()
        den = math.sqrt((a * a).sum() * (b * b).sum())
        out.append((a * b).sum() / den if den > 0 else np.nan)
    return np.array(out), r


def block_boot_beta(sig, L, B=400, block=25, seed=7):
    """Moving-block bootstrap of the increment series -> percentile CI on beta."""
    rng = np.random.default_rng(seed)
    sig = np.asarray(sig, float)
    d = np.diff(sig)
    n = len(d)
    nb = max(1, n // block + 1)
    outs = []
    for _ in range(B):
        st = rng.integers(0, max(1, n - block), size=nb)
        dd = np.concatenate([d[s:s + block] for s in st])[:n]
        r = wiener_fpt_beta(np.concatenate([[sig[0]], sig[0] + np.cumsum(dd)]), L)
        if r and np.isfinite(r["beta"]):
            outs.append(r["beta"])
    if len(outs) < 20:
        return None
    return float(np.percentile(outs, 2.5)), float(np.percentile(outs, 97.5)), len(outs)


def boot_mle_beta(t, B=2000, seed=7):
    rng = np.random.default_rng(seed)
    t = np.asarray(t, float)
    bs = [weibull_mle(rng.choice(t, size=len(t), replace=True))[0] for _ in range(B)]
    return float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5)), B


# ------------------------------------------------------------------ data loaders
def load_ews(name, offline):
    d = read_rda(fetch(EWS_RAW + name + ".rda", name + ".rda", offline))
    df = list(d.values())[0]
    return np.array(df[0], float), np.array(df[1], float)


def load_cmapss(fname, offline):
    rows = np.loadtxt(fetch(CMAPSS + fname, fname, offline))
    units = rows[:, 0].astype(int)
    cyc = rows[:, 1].astype(int)
    life = np.array([cyc[units == u].max() for u in np.unique(units)], float)
    return rows, units, life


# C-MAPSS column layout: 0 unit, 1 cycle, 2-4 operating settings, 5..25 = sensors s1..s21.
# s4 (col 8, LPT outlet temp), s11 (col 15, static pressure HPC outlet) and s15 (col 19,
# bypass ratio) are the standard monotone degradation sensors.
HEALTH_COLS = (8, 15, 19)


def cmapss_health(rows, mask, colstat):
    sub = rows[mask]
    z = []
    for c in HEALTH_COLS:
        mean, sd, sign = colstat[c]
        if sd == 0:
            continue
        z.append(sign * (sub[:, c] - mean) / sd)
    return np.mean(z, axis=0)


def cmapss_colstats(rows, units):
    """Fleet mean/sd per sensor, plus the sign that makes the index increase with age."""
    out = {}
    for c in HEALTH_COLS:
        v = rows[:, c]
        mean, sd = float(v.mean()), float(v.std())
        sign = 1.0
        if sd > 0:
            sl = np.polyfit(rows[:, 1], (v - mean) / sd, 1)[0]
            sign = -1.0 if sl < 0 else 1.0
        out[c] = (mean, sd, sign)
    return out


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    ap.add_argument("--boot", type=int, default=400)
    a = ap.parse_args()
    res = []

    # ---------- ecology: R2 only (one transition per series, so R1 does not exist) ----
    for tag, name, note in [
        ("ECO Cariaco YD->Preboreal greyscale (field)", "YD2PB_grayscale",
         "Dakos 2008 PNAS dataset; AR(1) -> 1 as the bifurcation threshold"),
        ("ECO thermohaline collapse (MODEL output)", "circulation",
         "model series, not field data - context row only"),
    ]:
        _, x = load_ews(name, a.offline)
        ar1, _ = ar1_indicator(x)
        sig = ar1[np.isfinite(ar1)]
        r = wiener_fpt_beta(sig, L=1.0)
        if r is None:
            res.append((tag + " [R2]", None, None,
                        dict(n=len(x), n_ind=int(len(sig)),
                             ar1_start=float(sig[0]), ar1_end=float(sig[-1])),
                        note + "; indicator drift is not toward the threshold"))
            continue
        ci = block_boot_beta(sig, 1.0, B=a.boot)
        res.append((tag + " [R2]", r["beta"], ci,
                    dict(n=len(x), n_ind=int(len(sig)), mu=r["mu"], sigma=r["sigma"],
                         m_fpt=r["m_fpt"], lam=r["lam"],
                         ar1_start=float(sig[0]), ar1_end=float(sig[-1])), note))

    # ---------- controls for the ecology row -----------------------------------------
    # CTRL-A: a STATIONARY AR(1) surrogate - noise-driven, no approaching bifurcation,
    # phi and sd matched to the Cariaco residual.  This instantiates the "beta ~ 1 /
    # no passage" arm of the discriminator.  If it also returns beta >> 1 the estimator
    # is measuring smoothness, not proximity to a threshold.
    _, xc = load_ews("YD2PB_grayscale", a.offline)
    _, resid = ar1_indicator(xc)
    seg = resid
    phi = float(np.corrcoef(seg[:-1], seg[1:])[0, 1])
    sd = float(seg.std())
    rng = np.random.default_rng(11)
    sb, nopass, snr = [], 0, []
    for _ in range(200):
        y = np.empty(len(xc))
        y[0] = 0.0
        e = rng.normal(0, sd * math.sqrt(max(1 - phi ** 2, 1e-6)), len(xc))
        for i in range(1, len(xc)):
            y[i] = phi * y[i - 1] + e[i]
        ind, _ = ar1_indicator(y)
        ind = ind[np.isfinite(ind)]
        d = np.diff(ind)
        snr.append(d.mean() / d.std(ddof=1))
        r = wiener_fpt_beta(ind, 1.0)
        if r is None:
            nopass += 1
        else:
            sb.append(r["beta"])
    # one-sided surrogate tests for the OBSERVED Cariaco statistics
    ind_obs, _ = ar1_indicator(xc)
    ind_obs = ind_obs[np.isfinite(ind_obs)]
    d_obs = np.diff(ind_obs)
    snr_obs = d_obs.mean() / d_obs.std(ddof=1)
    r_obs = wiener_fpt_beta(ind_obs, 1.0)
    snr = np.array(snr)
    p_snr = float((snr >= snr_obs).mean())
    p_beta = float((np.array(sb) >= r_obs["beta"]).mean()) if sb and r_obs else None
    res.append(("CTRL stationary AR(1) surrogate (no bifurcation)",
                float(np.median(sb)) if sb else None,
                (float(np.percentile(sb, 2.5)), float(np.percentile(sb, 97.5)), len(sb)) if sb else None,
                dict(phi=phi, sd=sd, n_reps=200, n_no_passage=nopass,
                     frac_no_passage=round(nopass / 200.0, 3),
                     drift_to_noise_observed=round(float(snr_obs), 5),
                     drift_to_noise_surrogate_median=round(float(np.median(snr)), 5),
                     p_one_sided_drift_to_noise=p_snr,
                     p_one_sided_beta=p_beta),
                "null arm: an indicator with no trend toward the threshold"))

    # CTRL-B: the FIRST HALF of the Cariaco record only - far from the transition.
    ind_h, _ = ar1_indicator(xc[:len(xc) // 2])
    ind_h = ind_h[np.isfinite(ind_h)]
    rh = wiener_fpt_beta(ind_h, 1.0)
    res.append(("CTRL Cariaco first half only (far from transition)",
                rh["beta"] if rh else None,
                block_boot_beta(ind_h, 1.0, B=a.boot) if rh else None,
                dict(n=len(xc) // 2, n_ind=int(len(ind_h)),
                     ar1_start=float(ind_h[0]), ar1_end=float(ind_h[-1])),
                "placebo arm: same series, transition removed"))

    # ---------- engineering: R1 and R2 -----------------------------------------------
    for fn, lab in [("train_FD001.txt", "ENG C-MAPSS FD001 (1 mode, 1 condition)"),
                    ("train_FD004.txt", "ENG C-MAPSS FD004 (2 modes, 6 conditions)")]:
        rows, units, life = load_cmapss(fn, a.offline)
        b, eta = weibull_mle(life)
        res.append((lab + " [R1 direct MLE]", b, boot_mle_beta(life),
                    dict(N_units=len(life), eta=eta, mean_life=float(life.mean()),
                         min=float(life.min()), max=float(life.max())),
                    "run-to-failure lifetimes; the estimator ecology cannot run"))
        cs = cmapss_colstats(rows, units)
        us = np.unique(units)
        ends = np.array([cmapss_health(rows, units == u, cs)[-1] for u in us])
        L = float(np.median(ends))
        betas = []
        for u in us:
            r = wiener_fpt_beta(cmapss_health(rows, units == u, cs), L)
            if r and np.isfinite(r["beta"]) and 0 < r["beta"] < 100:
                betas.append(r["beta"])
        if betas:
            betas = np.array(betas)
            res.append((lab + " [R2 degradation->FPT]", float(np.median(betas)),
                        (float(np.percentile(betas, 2.5)),
                         float(np.percentile(betas, 97.5)), len(betas)),
                        dict(n_units_fitted=len(betas), n_units_total=len(us),
                             threshold_L=L),
                        "same estimator as the ecology rows; spread is across units"))

    # ---------- report ----------------------------------------------------------------
    print("\nC26 - Weibull shape parameter beta, ecology and engineering on one axis")
    print("=" * 86)
    for tag, beta, ci, det, note in res:
        if beta is None:
            print("%-52s  beta = n/a" % tag)
        else:
            cis = "[%.2f, %.2f]" % (ci[0], ci[1]) if ci else "n/a"
            print("%-52s  beta = %6.2f   95%% %s" % (tag, beta, cis))
        print("%-52s  %s" % ("", note))
        print("%-52s  %s" % ("", json.dumps(
            {k: (round(v, 4) if isinstance(v, float) else v) for k, v in det.items()})))
    print("=" * 86)
    print("Discriminator:  beta > 1  -> wear-out / bifurcation-driven (hazard rises with age)")
    print("                beta ~ 1  -> memoryless / noise-induced (constant hazard)")


if __name__ == "__main__":
    main()
