#!/usr/bin/env python3
"""
c33_lolp.py - provenance + arithmetic for G34 / C33 (LOLP <-> starvation risk).

Two independent jobs, selected by argv[1]:

    python c33_lolp.py cites     # OpenCitations citer-set intersections, decade-binned
    python c33_lolp.py compute   # the LOLE <-> per-night starvation conversion

WHY ITS OWN FETCHER.  vault/_scripts/intersect.py is under repair for the
blank-key trap and must not be used for this note.  The fetch below is
self-contained and drops every record whose `citing` key is empty or
whitespace-only BEFORE any set is built, and reports how many it dropped.  An
unfiltered set carries a phantom "" member which is shared by every set and so
inflates every intersection by exactly 1.

Decade binning (failure-modes mode 6).  OpenCitations /citations/ records carry
a `creation` field = the citing work's date.  Both citer sets are binned by
that decade and the intersection is reported PER DECADE, because a pooled zero
across a 40-year window is forty years of separate measurements reported as one.

Provider: https://api.opencitations.net/index/v1/citations/<doi>
DOIs resolved through Crossref (api.crossref.org, mailto=deciduusleaf@gmail.com).
"""

import json, os, sys, time, urllib.parse, urllib.request
from collections import defaultdict

MAILTO = os.environ.get("MAILTO", "deciduusleaf@gmail.com")
OC = "https://api.opencitations.net/index/v1"
UA = "biomimicry-vault/1.0 (mailto:%s)" % MAILTO
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".c33-cache")


def _get(url, tries=5, timeout=300):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(3 * (i + 1))
    raise last


def _cached(url, key):
    os.makedirs(CACHE, exist_ok=True)
    p = os.path.join(CACHE, key + ".json")
    if os.path.exists(p):
        return json.loads(open(p, "rb").read().decode("utf-8"))
    raw = _get(url)
    open(p, "wb").write(raw)
    return json.loads(raw.decode("utf-8"))


def citers(doi):
    """{doi -> decade} for works citing `doi`.  Blank `citing` keys dropped."""
    url = "%s/citations/%s" % (OC, urllib.parse.quote(doi))
    rows = _cached(url, doi.replace("/", "_").replace(".", "-"))
    out, dropped = {}, 0
    for r in rows:
        c = (r.get("citing") or "").strip().lower()
        if c.startswith("coci =>"):
            c = c.split("=>", 1)[1].strip()
        if not c:
            dropped += 1
            continue
        yr = (r.get("creation") or "")[:4]
        out[c] = (int(yr) // 10 * 10) if yr.isdigit() else None
    print("  %s -> %d records, %d blank `citing` dropped, %d unique"
          % (doi, len(rows), dropped, len(out)), file=sys.stderr)
    return out, dropped


PAIRS = [
    ("GAP 1  Billinton&Allan 1996 x McNamara&Houston 1987",
     "10.1007/978-1-4899-1860-4", "10.2307/1939235"),
    ("GAP 2  Billinton&Li 1994 x Houston&McNamara 1993",
     "10.1007/978-1-4899-1346-3", "10.2307/3676736"),
    ("GAP 3  Billinton&Allan 1996 x Houston&McNamara 1993",
     "10.1007/978-1-4899-1860-4", "10.2307/3676736"),
    ("GAP 4  Billinton&Li 1994 x McNamara&Houston 1987",
     "10.1007/978-1-4899-1346-3", "10.2307/1939235"),
    ("CTRL-A power x power  Billinton&Allan 1996 x Billinton&Li 1994",
     "10.1007/978-1-4899-1860-4", "10.1007/978-1-4899-1346-3"),
    ("CTRL-B eco x eco      McNamara&Houston 1987 x Houston&McNamara 1993",
     "10.2307/1939235", "10.2307/3676736"),
]


def cmd_cites():
    blanks = 0
    for label, a, b in PAIRS:
        A, da = citers(a)
        B, db = citers(b)
        blanks += da + db
        inter = sorted(set(A) & set(B))
        n = len(A) + len(B) - len(inter)
        E = len(A) * len(B) / float(n) if n else 0.0
        print("\n%s" % label)
        print("  N_A=%d  N_B=%d  O=%d  N_floor=%d  E=%.1f  O/E=%.3f"
              % (len(A), len(B), len(inter), n, E,
                 (len(inter) / E) if E else float("nan")))
        print("  O as %% of smaller set: %.2f%%"
              % (100.0 * len(inter) / min(len(A), len(B))))
        # mode 6: decade bins across the whole citer window
        da_, db_, di = defaultdict(int), defaultdict(int), defaultdict(int)
        for d, dec in A.items():
            da_[dec] += 1
        for d, dec in B.items():
            db_[dec] += 1
        for d in inter:
            di[A[d]] += 1
        decs = sorted([x for x in set(da_) | set(db_) if x is not None])
        print("  decade | N_A | N_B | O")
        for dec in decs:
            print("   %ss | %4d | %4d | %d" % (dec, da_[dec], db_[dec], di[dec]))
        if None in da_ or None in db_:
            print("   undated | %4d | %4d | %d" % (da_[None], db_[None], di[None]))
        for d in inter:
            print("   HIT %s" % d)
    print("\nTOTAL blank `citing` records dropped across all fetches: %d" % blanks)


# ---------------------------------------------------------------- compute ----
#
# Parameters, ALL from Brodin, Nilsson & Nord, "Adaptive temperature regulation
# in the little bird in winter: predictions from a stochastic dynamic
# programming model", Oecologia 185:43-54 (2017), DOI 10.1007/s00442-017-3923-3,
# Tables 1-2 and text.  Open-access full text fetched from Europe PMC
# (PMC5596050 fullTextXML) on 2026-09-05.
X_MAX = 148.0      # kJ, max fat deposits (= 4 g fat), Table 2
NSTEP = 100        # discrete reserve steps, Table 2
D_DAYS = 100       # days in winter, Table 2
PER_DAY = 288      # time periods per day (T = 288*100 + 96), Table 2 + text
DAYLIGHT = 96      # daylight periods = 8 h, text ("all eight daylight hours")
ALPHA = 80.0       # kJ gain over a full day of intensive foraging (behaviour 1)
C_RM = 45.0        # kJ/day resting metabolism, Table 1
LAMBDA = 0.8       # P(a foraging period is successful), Table 1
DELTA = 0.20       # gain reduction on an unsuccessful period, Table 2
GAMMA = 0.20       # expenditure increase in bad weather, Table 2
EPS = 0.30         # expenditure saving at maximum hypothermia, Table 2
X_START = 12.0     # kJ, fat at start of the forward iteration, Table 2
P_GG = 1 - 1 / (2 * D_DAYS)   # 0.9983 per period, text
P_BB = 1 - 1 / D_DAYS         # 0.9965 per period, text

DX = X_MAX / NSTEP            # 1.48 kJ per reserve step
C_STEP = C_RM / PER_DAY       # 0.15625 kJ/period
G_STEP = ALPHA / DAYLIGHT     # 0.83333 kJ nominal gain/period
NIGHT = PER_DAY - DAYLIGHT    # 192 periods = 16 h
H_NIGHT = 16.0


def budget():
    """Deterministic daily budget in both weather states, and the night draw."""
    gain = DAYLIGHT * G_STEP * (LAMBDA + (1 - LAMBDA) * (1 - DELTA))
    return dict(
        gain=gain,
        day_G=C_STEP * DAYLIGHT,
        day_B=C_STEP * DAYLIGHT * (1 + GAMMA),
        night_G=C_STEP * NIGHT * (1 - EPS),
        night_B=C_STEP * NIGHT * (1 + GAMMA) * (1 - EPS),
        night_normo=C_STEP * NIGHT,
        night_normoB=C_STEP * NIGHT * (1 + GAMMA),
    )


def _shift(vec, kJ, nb):
    """Drift a reserve distribution by kJ (may be negative), linear split."""
    out = [0.0] * nb
    k = kJ / DX
    lo = int(k // 1)
    frac = k - lo
    for i, p in enumerate(vec):
        if p == 0.0:
            continue
        for j, w in ((i + lo, 1.0 - frac), (i + lo + 1, frac)):
            if w == 0.0:
                continue
            if j >= nb:
                j = nb - 1
            if j < 0:
                j = 0
            out[j] += p * w
    return out


def first_passage(scale=1.0, days=D_DAYS, x0=None):
    """P(reserve hits 0 within `days`) under the policy the paper reports as
    optimal under almost all conditions: forage intensively in every daylight
    period, enter maximum hypothermia every night.  `scale` multiplies the
    foraging gain -- the paper's own food-availability knob (its Delta).

    Exact forward propagation of the joint (reserve bin, weather) distribution
    at the model's own 5-minute resolution, with 0 absorbing.
    """
    x0 = X_START if x0 is None else x0
    nb = NSTEP + 1
    dist = [[0.0] * nb, [0.0] * nb]          # index 0 = good weather
    dist[0][min(nb - 1, int(round(x0 / DX)))] = 1.0
    dead = 0.0
    for _day in range(days):
        for period in range(PER_DAY):
            night = period >= DAYLIGHT
            new = [[0.0] * nb, [0.0] * nb]
            for w in (0, 1):
                src = dist[w]
                tot = sum(src)
                if tot == 0.0:
                    continue
                cost = C_STEP * ((1 + GAMMA) if w else 1.0)
                if night:
                    cost *= (1 - EPS)
                    outs = [(1.0, -cost)]
                else:
                    g = G_STEP * scale
                    outs = [(LAMBDA, g - cost),
                            (1 - LAMBDA, g * (1 - DELTA) - cost)]
                p_to_good = P_GG if w == 0 else 1 - P_BB
                for prob, dxk in outs:
                    v = _shift([p * prob for p in src], dxk, nb)
                    for w2, pw in ((0, p_to_good), (1, 1 - p_to_good)):
                        row = new[w2]
                        for i, p in enumerate(v):
                            if p:
                                row[i] += p * pw
            for w in (0, 1):
                dead += new[w][0]
                new[w][0] = 0.0
            dist = new
    return dead


def cmd_compute():
    b = budget()
    print("Brodin, Nilsson & Nord 2017 (10.1007/s00442-017-3923-3) energy budget, kJ")
    for k in ("gain", "day_G", "day_B", "night_G", "night_B",
              "night_normo", "night_normoB"):
        print("  %-12s %8.3f" % (k, b[k]))
    print("  net/day good weather = %+.3f   net/day bad weather = %+.3f"
          % (b["gain"] - b["day_G"] - b["night_G"],
             b["gain"] - b["day_B"] - b["night_B"]))

    mean_s = G_STEP * (LAMBDA + (1 - LAMBDA) * (1 - DELTA))
    var_s = LAMBDA * (1 - LAMBDA) * (G_STEP * DELTA) ** 2
    sd_day = (DAYLIGHT * var_s) ** 0.5
    print("  per-period gain: mean %.5f kJ, variance %.6f kJ^2" % (mean_s, var_s))
    print("  daily gain: mean %.3f kJ, sd %.4f kJ, CV %.4f"
          % (DAYLIGHT * mean_s, sd_day, sd_day / (DAYLIGHT * mean_s)))

    print("\nReserve margin: dusk reserve against the overnight draw")
    x_dusk = X_START + b["night_G"]
    print("  x_dusk = x_start (12 kJ, Table 2) + good-night draw = %.2f kJ" % x_dusk)
    for label, R in (("good night, max hypothermia", b["night_G"]),
                     ("cold night, max hypothermia", b["night_B"]),
                     ("good night, normothermic", b["night_normo"]),
                     ("cold night, normothermic", b["night_normoB"])):
        print("  %-30s R = %6.2f kJ   margin = %+7.1f%%"
              % (label, R, 100.0 * (x_dusk - R) / R))

    print("\nFirst passage to x = 0 over a %d-day winter, vs foraging-gain scale"
          % D_DAYS)
    print("  scale | P(starve | winter) |   p/night | LOLE h/winter")
    for s in (1.00, 0.80, 0.70, 0.65, 0.62, 0.60, 0.58, 0.56, 0.54, 0.50):
        P = first_passage(scale=s)
        pn = 1 - (1 - P) ** (1.0 / D_DAYS) if P < 1 else 1.0
        print("  %4.2f  | %18.6g | %9.3g | %13.5f"
              % (s, P, pn, P * (H_NIGHT / 2.0)))

    print("\nGrid criteria read as a %d-night starvation risk" % D_DAYS)
    print("  (an unserved event is charged the mean remaining night, %.0f h)"
          % (H_NIGHT / 2.0))
    for name, lolh in (
            ("North America LOLE 0.1 d/yr, charged 8 unserved h/event", 0.8),
            ("GB / France / Belgium / Poland  LOLH 3 h/yr", 3.0),
            ("Netherlands  LOLH 4 h/yr", 4.0),
            ("Ireland  LOLH 8 h/yr", 8.0)):
        Pw = lolh / (H_NIGHT / 2.0)
        pn = 1 - (1 - Pw) ** (1.0 / D_DAYS)
        print("  %-56s P(winter) = %.4f   p/night = %.3e" % (name, Pw, pn))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "cites"
    sys.exit(cmd_cites() if cmd == "cites" else cmd_compute())
