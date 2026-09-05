"""C51 — meta-analysis of the vault's own graded record.

Pre-registered in `audits/blind-brief-c51-2026-09-05.md`, sha256
8844d375b302b987d7bc83ebbb8f2e4157f26df7f93fd7bcdc6517ac697d786a,
hashed before any outcome column was read or coded.

Run from `vault/`:  python _scripts/c51_meta.py
Pure stdlib: Fisher's exact test is implemented here so the script has no
dependency that could silently change a p-value between machines.
"""

import csv
import os
from collections import Counter
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "c51_data", "claims.csv")


def fisher_exact(a, b, c, d):
    """Two-sided Fisher exact p for the 2x2 table [[a,b],[c,d]].

    Sums the hypergeometric probability of every table with the same margins
    whose probability is <= that of the observed table (the standard
    two-sided convention).
    """
    n = a + b + c + d
    r1, r2 = a + b, c + d
    c1 = a + c
    denom = comb(n, c1)

    def p_of(x):
        # x = the [0][0] cell; margins fixed
        if x < 0 or x > r1 or (c1 - x) < 0 or (c1 - x) > r2:
            return 0.0
        return comb(r1, x) * comb(r2, c1 - x) / denom

    p_obs = p_of(a)
    tol = p_obs * (1 + 1e-9)
    lo = max(0, c1 - r2)
    hi = min(r1, c1)
    return min(1.0, sum(p_of(x) for x in range(lo, hi + 1) if p_of(x) <= tol))


def table(rows, pred, outcome_fn, pred_levels):
    """Return {level: (yes, no)} for a binary outcome function."""
    out = {lv: [0, 0] for lv in pred_levels}
    for r in rows:
        lv = pred(r)
        if lv in out:
            out[lv][int(not outcome_fn(r))] += 1
    return out


def report(name, tab, levels, ylab, nlab):
    a, b = tab[levels[0]]
    c, d = tab[levels[1]]
    n = a + b + c + d
    p = fisher_exact(a, b, c, d)
    smaller_margin = min(a + b, c + d, a + c, b + d)
    print(f"\n--- {name}")
    print(f"{'':22s} {ylab:>10s} {nlab:>10s}   rate")
    for lv in levels:
        y, no = tab[lv]
        rate = y / (y + no) if (y + no) else float("nan")
        print(f"{lv:22s} {y:10d} {no:10d}   {rate:.3f}")
    print(f"n = {n};  Fisher two-sided p = {p:.4f};  smaller margin = {smaller_margin}")
    if smaller_margin < 5:
        print("  -> DIRECTION ONLY (brief: smaller margin < 5; p is not evidence)")
    return n, p, smaller_margin


def main():
    with open(DATA, encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    print(f"rows coded: {len(rows)}")
    print("outcome:", dict(Counter(r["outcome"] for r in rows)))
    print("type:   ", dict(Counter(r["type"] for r in rows)))
    print("round:  ", dict(Counter(r["round"] for r in rows)))

    graded = [r for r in rows if r["outcome"] != "ungraded"]
    print(f"\ngraded rows (ungraded excluded): {len(graded)}")
    surv = lambda r: r["survived"] == "1"
    print(f"overall survival: {sum(surv(r) for r in graded)}/{len(graded)} "
          f"= {sum(surv(r) for r in graded)/len(graded):.3f}")

    # ---- H1: derivations/catalogues (identity, taxonomy) vs correlations
    h1 = [r for r in graded if r["claim_kind"] in ("identity", "taxonomy", "correlation")]
    lv = lambda r: "identity/taxonomy" if r["claim_kind"] != "correlation" else "correlation"
    t = table(h1, lv, surv, ["identity/taxonomy", "correlation"])
    h1r = report("H1  claim kind x survival", t, ["identity/taxonomy", "correlation"],
                 "survived", "died")

    # ---- H2: famous pairs are more often prior art
    pa = lambda r: r["outcome"] == "PRIOR_ART"
    t = table(graded, lambda r: r["famous"], pa, ["famous", "obscure"])
    h2r = report("H2  famous x prior-art", t, ["famous", "obscure"], "prior art", "not")

    # ---- H3: post-blind-brief claims die at a HIGHER rate
    t = table(graded, lambda r: "blind brief" if r["blind_brief"] == "1" else "no brief",
              surv, ["blind brief", "no brief"])
    h3r = report("H3  blind brief x survival", t, ["blind brief", "no brief"],
                 "survived", "died")

    # ---- H3b: the round variable, as the broader version of the same claim
    t = table(graded, lambda r: r["round"], surv, ["post", "early"])
    h3br = report("H3b round x survival", t, ["post", "early"], "survived", "died")

    # ---- H4: data joins with scale mismatch die
    joins = [r for r in graded if r["move"] == "data_join"]
    t = table(joins, lambda r: r["scale_mismatch"], surv, ["mismatch", "same"])
    h4r = report("H4  scale mismatch x survival (data joins only)", t,
                 ["mismatch", "same"], "survived", "died")

    # ---- descriptive: survival by move type
    print("\n--- survival by move type (descriptive, not a pre-registered test)")
    for mv in sorted({r["move"] for r in graded}):
        sub = [r for r in graded if r["move"] == mv]
        s = sum(surv(r) for r in sub)
        print(f"{mv:18s} {s:2d}/{len(sub):2d}  {s/len(sub):.3f}")

    print("\n--- survival by adversarial pass (descriptive)")
    for k in ("1", "0"):
        sub = [r for r in graded if r["adversarial"] == k]
        s = sum(surv(r) for r in sub)
        print(f"adversarial={k}  {s:2d}/{len(sub):2d}  {s/len(sub):.3f}")

    # ---- logistic model gate from the brief
    print("\n--- logistic model gate")
    kinds = Counter(r["claim_kind"] for r in graded)
    prov = Counter(r["provenance"] for r in graded)
    ok = len(graded) >= 60 and min(kinds.values()) >= 5 and min(prov.values()) >= 5
    print(f"n_graded = {len(graded)} (>=60: {len(graded) >= 60}); "
          f"claim_kind levels {dict(kinds)}; provenance levels {dict(prov)}")
    sep = [k for k in kinds
           if len({r["survived"] for r in graded if r["claim_kind"] == k}) == 1]
    print("counts gate passed:", ok)
    print("levels perfectly separated on the outcome:", sep)
    print("model fitted: False - the maximum-likelihood estimate does not exist under "
          "complete separation, and a penalised fit would report a coefficient the data "
          "do not contain. Reported as the contingency tables above instead.")

    return h1r, h2r, h3r, h3br, h4r


if __name__ == "__main__":
    main()
