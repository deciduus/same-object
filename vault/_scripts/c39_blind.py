#!/usr/bin/env python3
"""c39_blind.py — blind governance re-code joined to the C36 Crow-AMSAA betas.

Turns C36 section 5's after-the-fact consistency observation into a (weak) test.
The coding rule, the ten-region list and the prediction were fixed in
`audits/blind-brief-c39-2026-09-05.md` and hashed BEFORE C36 was opened; the
governance scores below were coded from statute/regulation text only (URLs in
`vault/computed/C39-duane-governance-blind.md`).

Statistics: exact-permutation Spearman rank correlation (n = 8, so all 8! = 40320
score-vector permutations are enumerated -> exact two-sided p, no normal
approximation), plus a one-sided permutation test on the difference of group
mean betas (score 3 vs score <= 1).

    python c39_blind.py                 # the join and the statistics
    python c39_blind.py --verify-brief  # recompute the brief's sha256

Run 2026-09-05 for vault/computed/C39-duane-governance-blind.md.
Dependencies: stdlib only.
"""
import argparse, hashlib, itertools, os, sys

BRIEF = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "..", "..", "audits", "blind-brief-c39-2026-09-05.md")
BRIEF_BYTES = 4615          # bytes hashed = everything above the recorded hash block
BRIEF_SHA = "885ffef666798d784ec67260dbf7573a236e81007b893d6a24e3fa8f3d405d3d"

# region -> (score a, b, c) coded blind from governance sources
SCORES = {
    "US West Coast":            (1, 1, 1),
    "US East Coast":            (1, 1, 1),
    "US Southeast & Gulf":      (1, 1, 1),
    "US Alaska":                (1, 1, 1),
    "Canada East Coast":        (0, 1, 1),
    "Canada West Coast":        (0, 1, 1),
    "European Union":           (1, 1, 1),
    "Mediterranean-Black Sea":  (0, 0, 1),
    "Indian Ocean":             (0, 0, 0),
    "Southern Ocean (CCAMLR)":  (1, 0, 0),
}

# beta from C36 section 3, balanced 1990-2015 panel, failure = U/Umsy > 1.
# Regions coded but absent from C36's table carry None and drop out of the join.
BETA = {
    "US West Coast": 0.672, "US East Coast": 0.815, "US Southeast & Gulf": 0.861,
    "US Alaska": 0.942, "Canada East Coast": 0.881, "Canada West Coast": None,
    "European Union": 0.916, "Mediterranean-Black Sea": 1.105,
    "Indian Ocean": 1.362, "Southern Ocean (CCAMLR)": None,
}


def ranks(v):
    """Average ranks, ties shared."""
    order = sorted(range(len(v)), key=lambda i: v[i])
    r = [0.0] * len(v)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and v[order[j + 1]] == v[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1
        for k in range(i, j + 1):
            r[order[k]] = avg
        i = j + 1
    return r


def pearson(x, y):
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    sxx = sum((a - mx) ** 2 for a in x)
    syy = sum((b - my) ** 2 for b in y)
    return sxy / (sxx * syy) ** 0.5


def spearman_exact(s, b):
    """rho and EXACT two-sided permutation p over all n! relabelings."""
    rs, rb = ranks(s), ranks(b)
    rho = pearson(rs, rb)
    ge = tot = 0
    for perm in itertools.permutations(rs):
        tot += 1
        if abs(pearson(list(perm), rb)) >= abs(rho) - 1e-12:
            ge += 1
    return rho, ge / tot, tot


def perm_diff(hi, lo, reps=None):
    """One-sided permutation test: is mean(beta | score 3) < mean(beta | score<=1)?
    Enumerates all C(n, k) splits exactly."""
    obs = sum(hi) / len(hi) - sum(lo) / len(lo)
    pool = hi + lo
    k, n = len(hi), len(pool)
    le = tot = 0
    for idx in itertools.combinations(range(n), k):
        a = [pool[i] for i in idx]
        c = [pool[i] for i in range(n) if i not in idx]
        d = sum(a) / len(a) - sum(c) / len(c)
        tot += 1
        if d <= obs + 1e-12:
            le += 1
    return obs, le / tot, tot


def verify_brief():
    with open(os.path.normpath(BRIEF), "rb") as f:
        h = hashlib.sha256(f.read(BRIEF_BYTES)).hexdigest()
    print(f"brief first {BRIEF_BYTES} bytes sha256 = {h}")
    print("MATCHES recorded value" if h == BRIEF_SHA else "MISMATCH — brief altered")
    return 0 if h == BRIEF_SHA else 1


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify-brief", action="store_true")
    args = ap.parse_args(argv)
    if args.verify_brief:
        return verify_brief()

    print(f"{'region':26s} {'a':>2}{'b':>2}{'c':>2} {'score':>6} {'beta':>7}")
    joined = []
    for rg, (a, b, c) in SCORES.items():
        s, bt = a + b + c, BETA[rg]
        print(f"{rg:26s} {a:2d}{b:2d}{c:2d} {s:6d} "
              f"{('%7.3f' % bt) if bt is not None else '      -'}")
        if bt is not None:
            joined.append((rg, s, bt))

    s = [j[1] for j in joined]
    b = [j[2] for j in joined]
    n = len(joined)
    print(f"\njoined n = {n} of {len(SCORES)} coded regions")

    rho, p, tot = spearman_exact(s, b)
    print(f"Spearman rho = {rho:+.4f}   exact two-sided p = {p:.5f}  "
          f"({tot} permutations)")

    hi = [x for r, sc, x in joined if sc == 3]
    lo = [x for r, sc, x in joined if sc <= 1]
    print(f"score 3 : n={len(hi)} mean beta {sum(hi)/len(hi):.3f}  {hi}")
    print(f"score<=1: n={len(lo)} mean beta {sum(lo)/len(lo):.3f}  {lo}")
    d, pd, tt = perm_diff(hi, lo)
    print(f"difference of means = {d:+.4f}  one-sided permutation p = {pd:.5f} "
          f"({tt} splits)")

    print("\nPRE-DECLARED POWER CHECK (brief section 3):")
    print(f"  joined regions >= 8 : {n >= 8}")
    print(f"  each group >= 3     : {len(hi) >= 3 and len(lo) >= 3}")
    if not (n >= 8 and len(hi) >= 3 and len(lo) >= 3):
        print("  -> UNDERPOWERED by the brief's own rule; report DIRECTION ONLY.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
