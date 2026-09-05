#!/usr/bin/env python3
"""c41_parents.py -- is the C37 "double rediscovery" pattern general?

For each confirmed same-object pair (A, B) in the project, name a candidate
PARENT theory P and measure all THREE pairwise citer-set intersections
A x B, A x P, B x P on two independent providers.

Classification per row:
    (i)   both cite parent      -- not a rediscovery
    (ii)  one cites parent
    (iii) neither cites parent  -- double rediscovery (the C37 pattern)
    (iv)  parent not indexable

Usage:  python c41_parents.py [--providers=opencitations,semanticscholar]
Output: a TSV-ish table on stdout; --json FILE for the raw record.

E is the UNION FLOOR only:  E = N_A*N_B/(N_A+N_B-O).  It is the smallest
defensible denominator and therefore the largest E and the smallest O/E; it
flatters every gap claim and is never quotable alone (see citation-intersection).
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import providers  # noqa: E402

# doi -> short label
ROWS = [
    # (id, label, A, B, P, parent name)
    ("1", "LOLP x starvation",
     ("Billinton & Allan 1996", "10.1007/978-1-4899-1860-4"),
     ("McNamara & Houston 1987", "10.2307/1939235"),
     ("Asmussen & Albrecher 2010, Ruin Probabilities", "10.1142/7431"),
     "ruin theory (Lundberg 1903 / Cramer 1930)"),
    ("2", "Charnov MVT x Gittins",
     ("Charnov 1976", "10.1016/0040-5809(76)90040-x"),
     ("Gittins 1979", "10.1111/j.2517-6161.1979.tb01068.x"),
     ("Wald 1945, Sequential Tests", "10.1214/aoms/1177731118"),
     "optimal stopping / sequential analysis"),
    ("3", "healing Ha x Erlang-B",
     ("White et al. 2001", "10.1038/35057232"),
     ("Kendall 1953", "10.1214/aoms/1177728975"),
     ("Bolch et al., Queueing Networks and Markov Chains", "10.1002/0471200581"),
     "queueing theory (Erlang 1917 / Kleinrock 1975)"),
    ("4", "availability A x PSII repair",
     ("Billinton & Allan 1996", "10.1007/978-1-4899-1860-4"),
     ("Aro, Virgin & Andersson 1993", "10.1016/0005-2728(93)90134-2"),
     ("Barlow & Proschan, Math. Theory of Reliability", "10.1137/1.9781611971194"),
     "renewal theory / two-state Markov chain"),
    ("5", "Weibull beta products x recovery hazard",
     ("Oguchi et al. 2015", "10.1021/es505245q"),
     ("Jones & Schmitz 2009", "10.1371/journal.pone.0005653"),
     ("Kaplan & Meier 1958", "10.1080/01621459.1958.10501452"),
     "survival analysis (Kaplan-Meier 1958 / Cox 1972)"),
    ("6", "genetic load x die yield",
     ("Kimura, Maruyama & Crow 1963", "10.1093/genetics/48.10.1303"),
     ("Murphy 1964", "10.1109/proc.1964.3442"),
     ("Greenwood & Yule 1920", "10.2307/2341080"),
     "Poisson mixture / compound-Poisson counting"),
    ("7", "early warning x prognostics",
     ("Scheffer et al. 2009", "10.1038/nature08227"),
     ("Si et al. 2011", "10.1016/j.ejor.2010.11.018"),
     ("Kramers 1940", "10.1016/S0031-8914(40)90098-2"),
     "first-passage / escape over a barrier"),
    ("8", "adaptive management x Duane",
     ("Walters & Holling 1990", "10.2307/1938620"),
     ("Duane 1964", "10.1109/TA.1964.4319640"),
     ("Wright 1936", "10.2514/8.155"),
     "learning curves / NHPP reliability growth"),
]

CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".oc-cache")


def efloor(na, nb, o):
    u = na + nb - o
    return (na * nb / u) if u else 0.0


def main(argv):
    names = ["opencitations", "semanticscholar"]
    for a in argv:
        if a.startswith("--providers="):
            names = a.split("=", 1)[1].split(",")
    mods = [providers.BY_NAME[n] for n in names]

    sets = {}   # (provider, doi) -> set or None
    stats = {}

    def get(mod, doi):
        k = (mod.NAME, doi.lower())
        if k not in sets:
            try:
                sets[k] = mod.citers(doi, CACHE, stats)
            except Exception as e:            # noqa: BLE001
                sets[k] = None
                sys.stderr.write("  [%s] %s FAILED: %s\n" % (mod.NAME, doi, e))
        return sets[k]

    out = []
    for rid, label, A, B, P, pname in ROWS:
        rec = {"id": rid, "label": label, "A": A, "B": B, "P": P,
               "parent": pname, "providers": {}}
        for mod in mods:
            sa, sb, sp = get(mod, A[1]), get(mod, B[1]), get(mod, P[1])
            pr = {}
            for tag, (x, xd), (y, yd) in (("AxB", A, B), ("AxP", A, P), ("BxP", B, P)):
                sx = sets[(mod.NAME, xd.lower())]
                sy = sets[(mod.NAME, yd.lower())]
                if sx is None or sy is None:
                    pr[tag] = {"err": "provider could not enumerate one side"}
                    continue
                inter = sorted(sx & sy)
                pr[tag] = {"n_a": len(sx), "n_b": len(sy), "o": len(inter),
                           "E_floor": round(efloor(len(sx), len(sy), len(inter)), 1),
                           "hits": inter[:3]}
            rec["providers"][mod.NAME] = pr
        out.append(rec)
        print("\n=== %s. %s   [parent: %s]" % (rid, label, pname))
        for mod in mods:
            for tag in ("AxB", "AxP", "BxP"):
                c = rec["providers"][mod.NAME][tag]
                if "err" in c:
                    print("  %-16s %-4s  ERR %s" % (mod.NAME, tag, c["err"]))
                else:
                    print("  %-16s %-4s  N_A=%-7d N_B=%-7d O=%-4d E_floor=%-9.1f hits=%s"
                          % (mod.NAME, tag, c["n_a"], c["n_b"], c["o"],
                             c["E_floor"], ",".join(c["hits"]) or "-"))
    for f in argv:
        if f.startswith("--json="):
            with open(f.split("=", 1)[1], "w", encoding="utf-8") as fh:
                json.dump(out, fh, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
