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
# (PMC5596050 fullTextXML) on 2026-09-05 and RE-READ 2026-09-05 for this
# revision (Table 1, Table 2, Results paragraph 1).
X_MAX = 148.0      # kJ, max fat deposits (= 4 g fat), Table 2
NSTEP = 100        # discrete reserve steps, Table 2
D_DAYS = 100       # days in winter, Table 2
PER_DAY = 288      # time periods per day (T = 288*100 + 96), Table 2 + text
DAYLIGHT = 96      # daylight periods = 8 h ("keep on foraging all daylight hours")
ALPHA1 = 80.0      # kJ/day, behaviour 1 "Forage 1", Table 1
ALPHA2 = 60.0      # kJ/day, behaviour 2 "Forage 2" (cautious), Table 1
C_RM = 45.0        # kJ/day resting metabolism, Table 1
LAMBDA = 0.8       # P(a foraging period is successful), Table 1
DELTA = 0.20       # gain reduction on an unsuccessful period, Table 2
GAMMA = 0.20       # expenditure increase in bad weather, Table 2
EPS = 0.30         # expenditure saving at maximum hypothermia, Table 2
X_START = 12.0     # kJ, fat at start of the forward iteration, Table 2
C_WU = 6.0         # kJ, extra warming-up cost, hypothermic bird, Table 2
                   # ("0 or 6 kJ" -- the paper reports BOTH; rev.1 silently used 0)
KJ_PER_G = X_MAX / 4.0        # 37 kJ/g, from Table 2's "148 kJ (4 g fat)"
GAIN_PAPER_G = 0.74           # g/day, the paper's own stated total daily fat gain
P_GG = 1 - 1 / (2 * D_DAYS)   # 0.9983 per period, text
P_BB = 1 - 1 / D_DAYS         # 0.9965 per period, text

DX = X_MAX / NSTEP            # 1.48 kJ per reserve step
C_STEP = C_RM / PER_DAY       # 0.15625 kJ/period
NIGHT = PER_DAY - DAYLIGHT    # 192 periods = 16 h
H_NIGHT = 16.0
REAL = LAMBDA + (1 - LAMBDA) * (1 - DELTA)   # 0.96 realised fraction of nominal gain

DAY_COST_G = C_STEP * DAYLIGHT                           # 15.0 kJ
NIGHT_HYP_G = C_STEP * NIGHT * (1 - EPS)                 # 21.0 kJ (C_WU = 0 branch)
NIGHT_HYP_B = C_STEP * NIGHT * (1 + GAMMA) * (1 - EPS)   # 25.2 kJ
NIGHT_NORMO_G = C_STEP * NIGHT                           # 30.0 kJ
NIGHT_NORMO_B = C_STEP * NIGHT * (1 + GAMMA)             # 36.0 kJ

GAIN_PAPER_KJ = GAIN_PAPER_G * KJ_PER_G                  # 27.38 kJ/day net


def alpha_for_net(net_kJ):
    """Nominal daily alpha whose realised daylight gain minus the daylight
    resting cost equals `net_kJ`.  Used only by the CALIBRATED policy."""
    return (net_kJ + DAY_COST_G) / REAL


def policies():
    """(label, realised gross daylight gain kJ, note)."""
    return [
        ("A  max foraging (C33 rev.1)", ALPHA1 * REAL,
         "behaviour 1 every daylight period; NOT the paper's policy"),
        ("B1 mixed policy, half b1 / half b2", (0.5 * ALPHA1 + 0.5 * ALPHA2) * REAL,
         "behaviour 1 to noon, behaviour 2 after noon"),
        ("B2 all-cautious bound (behaviour 2 only)", ALPHA2 * REAL,
         "lowest gain the paper's 'forage all daylight hours' text allows"),
        ("C  CALIBRATED to the paper's 0.74 g/day", alpha_for_net(GAIN_PAPER_KJ) * REAL,
         "alpha FITTED, not a paper parameter"),
    ]


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


def first_passage(alpha_gross, scale=1.0, days=D_DAYS, x0=None, c_wu=C_WU,
                  hypothermia=True):
    """P(reserve hits 0 within `days`).  Exact forward propagation of the joint
    (reserve bin, weather) distribution at the model's own 5-min resolution,
    0 absorbing.

    `alpha_gross` is the REALISED gross daylight gain in kJ/day, spread evenly
    over the 96 daylight periods.  `c_wu` is charged once, in the first daylight
    period of each day, when the preceding night was hypothermic (Table 2's
    "0 or 6 kJ"; rev.1 of this note silently used 0).  `scale` multiplies the
    foraging gain -- the paper's own food-availability knob (its Delta).
    """
    x0 = X_START if x0 is None else x0
    nb = NSTEP + 1
    g_step = alpha_gross / DAYLIGHT / REAL   # nominal per-period gain
    dist = [[0.0] * nb, [0.0] * nb]          # index 0 = good weather
    dist[0][min(nb - 1, int(round(x0 / DX)))] = 1.0
    dead = 0.0
    for _day in range(days):
        for period in range(PER_DAY):
            night = period >= DAYLIGHT
            new = [[0.0] * nb, [0.0] * nb]
            for w in (0, 1):
                src = dist[w]
                if sum(src) == 0.0:
                    continue
                cost = C_STEP * ((1 + GAMMA) if w else 1.0)
                if night:
                    if hypothermia:
                        cost *= (1 - EPS)
                    outs = [(1.0, -cost)]
                else:
                    g = g_step * scale
                    extra = c_wu if (period == 0 and hypothermia) else 0.0
                    outs = [(LAMBDA, g - cost - extra),
                            (1 - LAMBDA, g * (1 - DELTA) - cost - extra)]
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
    print("Brodin, Nilsson & Nord 2017 (10.1007/s00442-017-3923-3)")
    print("Europe PMC PMC5596050 full text, re-read 2026-09-05")

    print("\n== 0. POSITIVE CONTROL: does any stated policy reproduce 0.74 g/day? ==")
    print("   paper's own outcome: %.2f g/day = %.2f kJ/day at %.0f kJ/g"
          % (GAIN_PAPER_G, GAIN_PAPER_KJ, KJ_PER_G))
    print("   daylight resting cost, good weather = %.1f kJ" % DAY_COST_G)
    print("   %-42s %10s %10s %8s %8s"
          % ("policy", "gross kJ", "net kJ", "g/day", "x 0.74"))
    for label, gross, _n in policies():
        net = gross - DAY_COST_G
        print("   %-42s %10.2f %10.2f %8.2f %8.2f"
              % (label, gross, net, net / KJ_PER_G, (net / KJ_PER_G) / GAIN_PAPER_G))
    lo = ALPHA2 * REAL - DAY_COST_G
    print("   VERDICT -- POSITIVE CONTROL FAILS.")
    print("   The paper's stated daylight policy ('keep on foraging all daylight")
    print("   hours', behaviours 1 and 2 only) has a FLOOR of %.2f kJ = %.2f g/day,"
          % (lo, lo / KJ_PER_G))
    print("   which is %.2fx the paper's own 0.74 g. No mixture of behaviours 1 and 2"
          % ((lo / KJ_PER_G) / GAIN_PAPER_G))
    print("   can reach it. The trajectory is NOT reconstructible from Tables 1-2 plus")
    print("   the open text: the mass-dependent foraging metabolism (Table 1 fn a) and")
    print("   the mass-dependent gain ceiling ('up to 1 g of fat') are unparameterised.")
    print("   Policy C therefore FITS alpha to 0.74 g/day: alpha_eff = %.2f kJ/day"
          % alpha_for_net(GAIN_PAPER_KJ))
    print("   nominal (printed values are 80 and 60). LABELLED FIT, not a parameter.")

    print("\n== 1. Night draw, both C_WU treatments (Table 2: '0 or 6 kJ') ==")
    print("   hypothermic, C_WU=0 : %5.1f good / %5.1f cold" % (NIGHT_HYP_G, NIGHT_HYP_B))
    print("   hypothermic, C_WU=6 : %5.1f good / %5.1f cold"
          % (NIGHT_HYP_G + C_WU, NIGHT_HYP_B + C_WU))
    print("   normothermic        : %5.1f good / %5.1f cold"
          % (NIGHT_NORMO_G, NIGHT_NORMO_B))
    print("   hypothermia saving  : %.1f kJ at C_WU=0, %.1f kJ at C_WU=6"
          % (NIGHT_NORMO_G - NIGHT_HYP_G, NIGHT_NORMO_G - NIGHT_HYP_G - C_WU))
    print("   paper's stabilised cycle implies a night draw of %.1f kJ (= day gain)"
          % GAIN_PAPER_KJ)

    print("\n== 2. Energy margin over the critical period, x_dusk/R - 1 ==")
    x_dusk = X_START + NIGHT_HYP_G
    print("   x_dusk = x_start (12 kJ, Table 2) + C_WU=0 good-night draw = %.1f kJ"
          % x_dusk)
    m_hyp6 = 100.0 * (x_dusk - (NIGHT_HYP_G + C_WU)) / (NIGHT_HYP_G + C_WU)
    m_norm = 100.0 * (x_dusk - NIGHT_NORMO_G) / NIGHT_NORMO_G
    m_hyp0 = 100.0 * (x_dusk - NIGHT_HYP_G) / NIGHT_HYP_G
    for lbl, R in (("hypothermic night, C_WU=6", NIGHT_HYP_G + C_WU),
                   ("cold hypothermic night, C_WU=6", NIGHT_HYP_B + C_WU),
                   ("normothermic night", NIGHT_NORMO_G),
                   ("cold normothermic night", NIGHT_NORMO_B),
                   ("hypothermic night, C_WU=0 (rev.1)", NIGHT_HYP_G)):
        print("   %-36s R = %5.1f  margin = %+6.1f%%"
              % (lbl, R, 100.0 * (x_dusk - R) / R))
    print("   hypothermia lever: %+.1f points at C_WU=6 (rev.1 claimed %+.1f)"
          % (m_hyp6 - m_norm, m_hyp0 - m_norm))
    print("   ON THE PAPER'S OWN BUDGET (R = %.1f kJ): margin = x_start/R = %+.1f%%"
          % (GAIN_PAPER_KJ, 100.0 * X_START / GAIN_PAPER_KJ))

    print("\n== 3. First passage to x = 0 over a %d-night winter ==" % D_DAYS)
    print("   %-42s %16s %12s" % ("policy", "P(starve|winter)", "p/night"))
    for label, gross, _n in policies():
        P = first_passage(gross)
        pn = 1 - (1 - P) ** (1.0 / D_DAYS) if P < 1 else 1.0
        print("   %-42s %16.4g %12.4g" % (label, P, pn))

    gc = alpha_for_net(GAIN_PAPER_KJ) * REAL
    print("\n   CALIBRATED policy C against the paper's food knob Delta:")
    print("   %6s %18s %12s" % ("scale", "P(starve|winter)", "p/night"))
    for s in (1.10, 1.05, 1.00, 0.95, 0.90):
        P = first_passage(gc, scale=s)
        pn = 1 - (1 - P) ** (1.0 / D_DAYS) if P < 1 else 1.0
        print("   %6.2f %18.6g %12.4g" % (s, P, pn))

    P0 = first_passage(gc, hypothermia=False, c_wu=0.0)
    print("\n   Policy C, hypothermia REMOVED (no eps saving, no warm-up cost):")
    print("   P(starve|winter) = %.6g" % P0)

    print("\n== 4. The paper's OWN published survival, which bounds all of the above ==")
    print("   Brodin 2017 Results, sentence 1, verbatim: 'The probability of winter")
    print("   survival increased dramatically from 0.13 to 0.71 if birds used")
    print("   hypothermia to save 30 percent of the overnight energy expenditure.'")
    print("   So the model's own P(die over a winter), ALL causes incl. predation,")
    print("   is %.2f with hypothermia and %.2f without." % (1 - 0.71, 1 - 0.13))
    print("   P(starve) <= P(die) = 0.29 is therefore a HARD CEILING from the paper.")
    print("   Per night that ceiling is 1-(1-0.29)^(1/100) = %.2e."
          % (1 - (1 - 0.29) ** 0.01))
    print("   rev.1's 8.25e-8 sits 6.5 orders of magnitude below that ceiling;")
    print("   the calibrated open-loop policy C (%.4f) sits ABOVE it." % 0.9992)
    print("   Both bracket ends are open-loop artifacts: the paper's bird runs a")
    print("   STATE-DEPENDENT optimal policy from the backward DP, which forages")
    print("   harder when the reserve is low. No fixed-gain forward propagation")
    print("   can estimate its first-passage probability. C33's P(starve) is")
    print("   WITHDRAWN; the paper's own 0.29 / 0.87 are the quotable numbers.")
    print("   Hypothermia lever in the paper's own currency: survival 0.13 -> 0.71,")
    print("   a 58-point lever, and it is a PUBLISHED number, not this note's.")

    print("\n== 5. Grid side: what a like-for-like comparison would need ==")
    print("   LOLE 0.1 d/yr -> per-day OCCUPATION probability 0.1/365 = %.3e"
          % (0.1 / 365.0))
    print("   That is an occupation probability, not a first passage. The union bound")
    print("   gives P(first hit 0 within a year) <= LOLE = 0.1, which bounds the grid")
    print("   from ABOVE only and therefore cannot order the two systems.")
    print("   No published per-period first-passage probability for a")
    print("   storage-constrained adequacy study was found this session. Null, stated.")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "cites"
    sys.exit(cmd_cites() if cmd == "cites" else cmd_compute())
