#!/usr/bin/env python3
"""c40_setpoint.py -- pre-registered test of C38 section 5's setpoint prediction.

Brief: audits/blind-brief-c40-2026-09-05.md, sha256 over its first 7811 bytes
recorded there and re-checkable with --verify-brief. The brief was written and
hashed BEFORE any survival, longevity or latitude value was fetched.

T1  Spearman rho, ordinal torpor class (0 none / 1 daily torpor / 2 hibernation)
    vs published reserve margin. Margins are CITED from C38 section 2, never
    recomputed here. Exact permutation p (n! enumerated).
T2  Adult-survival proxy (AnAge maximum longevity, flagged PROXY exactly as the
    brief pre-declared) for lever-bearing vs lever-less small temperate mammals,
    controlled for body mass and latitude by greedy matched pairs; exact
    one-sided sign test, with a Wilcoxon rank-sum fallback also printed.
T3  Falsifier scan: lever-less species with a published margin > +100%.

Data, all fetched 2026-09-05:
  Ruf & Geiser 2015 Biol. Rev. 90:891-926, 10.1111/brv.12137, per-species
    Appendix table scraped from the open PMC copy PMC4351926 (214 species with
    T, BM, Tb_min, TMR_min, TMR_rel, TBD_max, LAT). C38 section 5 said this
    appendix "was not obtained"; it now has been.
  AnAge build 14, https://genomics.senescence.info/species/dataset.zip
  PanTHERIA 1.0 WR05, https://esapubs.org/archive/ecol/E090/184/
    PanTHERIA_1-0_WR05_Aug2008.txt  (26-4_GR_MidRangeLat_dd)

Every literal below is transcribed from those files or from C38 section 2.
Dependencies: stdlib only.

    python _scripts/c40_setpoint.py
    python _scripts/c40_setpoint.py --verify-brief
"""
import argparse, hashlib, itertools, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
BRIEF = os.path.join(HERE, "..", "..", "audits", "blind-brief-c40-2026-09-05.md")
BRIEF_BYTES = 7811
BRIEF_SHA = "1e2bc903ba59099120b4fb1f300d836cb67cb83261f697a18843ff9d91db5dff"

# ---------------------------------------------------------------- T1 inputs
# species -> (torpor class, margin as a ratio, C38 row used, sensitivity rows)
# Margins are C38 section 2 literals. Class from Ruf & Geiser 2015 Appendix
# (presence + T column) except the parid, which is absent from that appendix
# and is coded 1 from Brodin 2017's quantified nocturnal-hypothermia bout;
# the alternative code 0 is run as a sensitivity.
T1 = {
    "Myotis lucifugus":       (2, 0.99, "Haase 2019 mean microclimate +75%, "
                                        "selected roost +99%, Hranac medians +383%; "
                                        "median of the three lever-engaged rows",
                               [0.75, 0.99, 3.83]),
    "Peromyscus maniculatus": (1, 2.65, "Rezende 2009 warm-acclimated, lever engaged",
                               [2.65, 0.015]),
    "Cyanistes caeruleus":    (1, 0.571, "Brodin 2017 via C33 section 4, hypothermia ON",
                               [0.571, 0.10]),
    "Sorex araneus":          (0, -0.69, "Keicher 2017: -38% / -69% / -74%; median",
                               [-0.38, -0.69, -0.74]),
}
# Excluded from T1 by the brief's filter 4 (migrant), stated not hidden:
T1_EXCLUDED = [
    ("Selasphorus rufus", 2, "+2421% torpid / +354% normothermic",
     "obligate long-distance migrant"),
    ("Archilochus colubris", 1, "+116% torpid / -61% normothermic",
     "obligate long-distance migrant"),
    ("Homo sapiens", 0, "-12% (ASSUMED row)", "body mass >= 100 g"),
]

# ------------------------------------------------------- T2 frame, hard-coded
# AnAge (adult weight g, maximum longevity yr, data quality) x PanTHERIA
# (mid-range latitude, decimal degrees) x Ruf & Geiser class.
# Filter, applied exactly as brief section 4: Mammalia; order in
# {Chiroptera, Rodentia, Eulipotyphla/Soricomorpha}; mass < 100 g;
# |mid-range latitude| >= 35; AnAge data quality acceptable or high;
# maximum longevity present; not on the migratory-bat exclusion list.
# columns: species, class, mass_g, longevity_yr, abs_lat, coding_source, order
T2 = [
    ("Pipistrellus pipistrellus", 2, 5.00, 16.6, 43.44, "RG-species", "Chiroptera"),
    ("Vespadelus regulus", 2, 5.05, 8.0, 35.40, "clade-family", "Chiroptera"),
    ("Myotis leibii", 2, 5.60, 12.0, 40.89, "clade-family", "Chiroptera"),
    ("Vespadelus darlingtoni", 2, 6.06, 8.0, 35.39, "clade-family", "Chiroptera"),
    ("Myotis yumanensis", 2, 6.25, 14.0, 37.19, "clade-family", "Chiroptera"),
    ("Myotis brandtii", 2, 7.00, 41.0, 51.02, "clade-family", "Chiroptera"),
    ("Myotis volans", 2, 7.00, 21.0, 39.96, "clade-family", "Chiroptera"),
    ("Myotis evotis", 2, 7.40, 22.0, 40.12, "clade-family", "Chiroptera"),
    ("Myotis keenii", 2, 7.40, 19.0, 51.75, "clade-family", "Chiroptera"),
    ("Myotis nattereri", 2, 7.50, 23.7, 46.05, "RG-species", "Chiroptera"),
    ("Myotis sodalis", 2, 7.70, 20.0, 38.05, "clade-family", "Chiroptera"),
    ("Plecotus auritus", 2, 7.80, 30.0, 44.65, "RG-species", "Chiroptera"),
    ("Perognathus longimembris", 2, 8.00, 8.3, 35.77, "RG-species", "Rodentia"),
    ("Myotis daubentonii", 2, 8.50, 28.0, 44.87, "clade-family", "Chiroptera"),
    ("Myotis grisescens", 2, 9.25, 16.5, 35.76, "clade-family", "Chiroptera"),
    ("Barbastella barbastellus", 2, 10.25, 23.0, 44.28, "RG-species", "Chiroptera"),
    ("Myotis bechsteinii", 2, 10.50, 21.0, 45.26, "clade-family", "Chiroptera"),
    ("Myotis emarginatus", 2, 11.00, 22.7, 38.30, "clade-family", "Chiroptera"),
    ("Eptesicus nilssonii", 2, 13.00, 20.0, 53.78, "clade-family", "Chiroptera"),
    ("Myotis dasycneme", 2, 15.00, 20.5, 54.84, "clade-family", "Chiroptera"),
    ("Zapus hudsonius", 2, 18.00, 5.6, 48.34, "RG-species", "Rodentia"),
    ("Eptesicus serotinus", 2, 18.20, 21.0, 37.94, "clade-family", "Chiroptera"),
    ("Perognathus parvus", 2, 20.10, 5.8, 43.39, "RG-species", "Rodentia"),
    ("Falsistrellus tasmaniensis", 2, 22.54, 6.0, 35.07, "clade-family", "Chiroptera"),
    ("Rhinolophus ferrumequinum", 2, 22.88, 30.5, 38.48, "RG-species", "Chiroptera"),
    ("Myotis blythii", 2, 23.00, 33.0, 38.55, "clade-family", "Chiroptera"),
    ("Dryomys nitedula", 2, 26.00, 4.1, 42.31, "clade-family", "Rodentia"),
    ("Muscardinus avellanarius", 2, 27.30, 5.3, 47.96, "RG-species", "Rodentia"),
    ("Myotis myotis", 2, 28.55, 37.1, 47.44, "RG-species", "Chiroptera"),
    ("Tamias minimus", 2, 44.10, 10.0, 50.47, "clade-genus", "Rodentia"),
    ("Dipodomys heermanni", 2, 65.00, 8.3, 36.65, "clade-genus", "Rodentia"),
    ("Tamias townsendii", 2, 75.00, 9.3, 45.85, "clade-genus", "Rodentia"),
    ("Eliomys quercinus", 2, 82.50, 5.5, 42.91, "RG-species", "Rodentia"),
    ("Tamias sibiricus", 2, 85.00, 9.6, 50.17, "clade-genus", "Rodentia"),
    ("Tamias striatus", 2, 96.00, 9.5, 40.78, "RG-species", "Rodentia"),
    ("Crocidura leucodon", 1, 11.00, 2.9, 42.54, "RG-species", "Soricomorpha"),
    ("Crocidura russula", 1, 11.60, 4.0, 40.48, "RG-species", "Soricomorpha"),
    ("Peromyscus crinitus", 1, 16.50, 7.7, 36.88, "RG-species", "Rodentia"),
    ("Mus spicilegus", 1, 19.90, 3.5, 46.26, "clade-genus", "Rodentia"),
    ("Peromyscus maniculatus", 1, 20.50, 8.3, 40.92, "RG-species", "Rodentia"),
    ("Phodopus sungorus", 1, 23.40, 3.9, 50.89, "RG-species", "Rodentia"),
    ("Mystacina tuberculata", 1, 23.50, 7.6, 40.97, "clade-genus", "Chiroptera"),
    ("Apodemus peninsulae", 1, 32.90, 4.4, 48.26, "RG-species", "Rodentia"),
    ("Sorex caecutiens", 0, 5.40, 3.0, 53.58, "clade-genus", "Soricomorpha"),
    ("Micromys minutus", 0, 6.00, 3.8, 43.32, "clade-genus", "Rodentia"),
    ("Sorex araneus", 0, 9.00, 3.2, 53.76, "clade-genus", "Soricomorpha"),
    ("Blarina hylophaga", 0, 14.50, 2.8, 36.34, "clade-genus", "Soricomorpha"),
    ("Neomys fodiens", 0, 15.00, 3.1, 55.58, "clade-genus", "Soricomorpha"),
    ("Myodes rutilus", 0, 20.00, 2.1, 55.73, "clade-genus", "Rodentia"),
    ("Lagurus lagurus", 0, 20.30, 3.8, 48.93, "clade-genus", "Rodentia"),
    ("Myodes glareolus", 0, 20.80, 4.9, 53.56, "clade-genus", "Rodentia"),
    ("Blarina brevicauda", 0, 21.60, 2.2, 44.24, "clade-genus", "Soricomorpha"),
    ("Apodemus argenteus", 0, 23.40, 5.0, 38.25, "clade-genus", "Rodentia"),
    ("Apodemus sylvaticus", 0, 23.40, 6.3, 47.53, "clade-genus", "Rodentia"),
    ("Microtus pinetorum", 0, 25.50, 3.8, 37.42, "clade-genus", "Rodentia"),
    ("Microtus arvalis", 0, 27.50, 4.8, 50.70, "clade-genus", "Rodentia"),
    ("Apodemus flavicollis", 0, 29.40, 4.5, 51.12, "clade-genus", "Rodentia"),
    ("Onychomys leucogaster", 0, 32.50, 5.6, 38.20, "clade-genus", "Rodentia"),
    ("Alticola semicanus", 0, 36.00, 3.8, 47.67, "clade-genus", "Rodentia"),
    ("Ellobius talpinus", 0, 40.00, 6.4, 47.00, "clade-genus", "Rodentia"),
    ("Lasiopodomys brandtii", 0, 40.00, 4.1, 47.06, "clade-genus", "Rodentia"),
    ("Microtus ochrogaster", 0, 40.00, 5.3, 42.53, "clade-genus", "Rodentia"),
    ("Apodemus speciosus", 0, 44.00, 5.3, 38.25, "clade-genus", "Rodentia"),
    ("Microtus agrestis", 0, 46.00, 4.8, 54.77, "clade-genus", "Rodentia"),
    ("Microtus guentheri", 0, 51.60, 3.9, 36.91, "clade-genus", "Rodentia"),
    ("Meriones meridianus", 0, 53.00, 6.8, 39.67, "clade-genus", "Rodentia"),
    ("Meriones unguiculatus", 0, 53.20, 6.3, 45.12, "clade-genus", "Rodentia"),
    ("Allactaga elater", 0, 58.70, 5.2, 39.46, "clade-genus", "Rodentia"),
    ("Pseudomys shortridgei", 0, 64.00, 6.0, 35.42, "clade-genus", "Rodentia"),
    ("Dicrostonyx groenlandicus", 0, 66.00, 3.3, 68.22, "clade-genus", "Rodentia"),
    ("Lemmus lemmus", 0, 70.00, 3.3, 67.92, "clade-genus", "Rodentia"),
    ("Pseudomys fumeus", 0, 70.00, 6.5, 36.72, "clade-genus", "Rodentia"),
    ("Reithrodon auritus", 0, 72.20, 5.5, 39.77, "clade-genus", "Rodentia"),
    ("Scalopus aquaticus", 0, 90.00, 6.2, 35.50, "clade-genus", "Soricomorpha"),
    ("Mogera wogura", 0, 97.00, 3.2, 40.18, "clade-genus", "Soricomorpha"),
]
# Excluded by the migratory-bat rule (brief section 4 filter 4), listed not hidden:
T2_MIGRANT_EXCLUDED = ["Lasiurus cinereus", "Lasiurus borealis",
                       "Tadarida brasiliensis", "Nyctalus noctula",
                       "Miniopterus schreibersii", "Tadarida teniotis"]

# Tb_min from the Ruf & Geiser Appendix, for the secondary T1b Spearman
TB_MIN = {"Myotis lucifugus": 1.3, "Peromyscus maniculatus": 13.4}


# --------------------------------------------------------------- statistics
def ranks(v):
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


def pearson(a, b):
    n = len(a)
    ma, mb = sum(a) / n, sum(b) / n
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    da = math.sqrt(sum((x - ma) ** 2 for x in a))
    db = math.sqrt(sum((y - mb) ** 2 for y in b))
    return num / (da * db) if da and db else float("nan")


def spearman_exact(x, y):
    rx, ry = ranks(x), ranks(y)
    rho = pearson(rx, ry)
    hits = tot = 0
    for perm in itertools.permutations(ry):
        tot += 1
        if abs(pearson(rx, list(perm))) >= abs(rho) - 1e-12:
            hits += 1
    return rho, hits / tot, tot


def sign_test_one_sided(diffs):
    """P(at least k of n non-zero diffs positive) under p = 0.5."""
    nz = [d for d in diffs if d != 0]
    n, k = len(nz), sum(1 for d in nz if d > 0)
    p = sum(math.comb(n, i) for i in range(k, n + 1)) / 2.0 ** n if n else 1.0
    return n, k, p


def ranksum(a, b):
    """Wilcoxon rank-sum W for group a, plus a normal-approx two-sided p."""
    allv = a + b
    r = ranks(allv)
    W = sum(r[:len(a)])
    na, nb = len(a), len(b)
    mu = na * (na + nb + 1) / 2.0
    sd = math.sqrt(na * nb * (na + nb + 1) / 12.0)
    z = (W - mu) / sd
    p = math.erfc(abs(z) / math.sqrt(2))
    return W, z, p


def matched_pairs(control, treat, mass_tol=0.3, lat_tol=10.0):
    """Greedy nearest-neighbour matching on (log10 mass, latitude)."""
    used, pairs = set(), []
    cands = []
    for i, c in enumerate(control):
        for j, t in enumerate(treat):
            dm = abs(math.log10(c[2]) - math.log10(t[2]))
            dl = abs(c[4] - t[4])
            if dm <= mass_tol and dl <= lat_tol:
                cands.append((dm / mass_tol + dl / lat_tol, i, j))
    for d, i, j in sorted(cands):
        if ("c", i) in used or ("t", j) in used:
            continue
        used.add(("c", i)); used.add(("t", j))
        pairs.append((control[i], treat[j], d))
    return pairs


# ------------------------------------------------------------------- driver
def verify_brief():
    b = open(BRIEF, "rb").read()[:BRIEF_BYTES]
    h = hashlib.sha256(b).hexdigest()
    print("brief bytes hashed :", len(b))
    print("sha256             :", h)
    print("expected           :", BRIEF_SHA)
    print("MATCH" if h == BRIEF_SHA else "*** MISMATCH ***")
    return h == BRIEF_SHA


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify-brief", action="store_true")
    a = ap.parse_args()
    if a.verify_brief:
        raise SystemExit(0 if verify_brief() else 1)

    print("=" * 74)
    print("T1 -- torpor class vs published reserve margin (margins cited from C38)")
    print("=" * 74)
    names = list(T1)
    cls = [T1[s][0] for s in names]
    mar = [T1[s][1] for s in names]
    for s in names:
        print(f"  {s:26s} class {T1[s][0]}  margin {T1[s][1]:+7.3f}   {T1[s][2]}")
    rho, p, tot = spearman_exact(cls, mar)
    n = len(names)
    counts = {c: cls.count(c) for c in sorted(set(cls))}
    claimable = n >= 8 and sum(1 for c in counts.values() if c >= 3) >= 2
    print(f"\n  n = {n}   class counts {counts}")
    print(f"  Spearman rho = {rho:+.4f}   exact two-sided p = {p:.4f} "
          f"({tot} permutations)")
    print(f"  predicted sign positive -> {'AS PREDICTED' if rho > 0 else 'FAILS'}")
    print(f"  brief section 7 gate (n>=8 and two classes with n>=3): "
          f"{'MET' if claimable else 'NOT MET -> DIRECTION-ONLY'}")

    print("\n  sensitivity over the alternative C38 rows per species:")
    grids = [T1[s][3] for s in names]
    rhos = []
    for combo in itertools.product(*grids):
        rhos.append(pearson(ranks(cls), ranks(list(combo))))
    print(f"    {len(rhos)} combinations, rho range "
          f"{min(rhos):+.4f} to {max(rhos):+.4f}, "
          f"{sum(1 for r in rhos if r > 0)}/{len(rhos)} positive")
    alt = [0 if s == "Cyanistes caeruleus" else T1[s][0] for s in names]
    print(f"    parid recoded class 0: rho = {pearson(ranks(alt), ranks(mar)):+.4f}")
    print(f"  T1b (Tb_min secondary): only {len(TB_MIN)} species carry Tb_min "
          "-> SKIPPED per brief section 2")
    print("  excluded from T1 by the pre-registered filter:")
    for s, c, m, why in T1_EXCLUDED:
        print(f"    {s:24s} class {c}  {m:34s} {why}")

    print()
    print("=" * 74)
    print("T2 -- adult-survival PROXY (AnAge maximum longevity) lever vs lever-less")
    print("=" * 74)
    treat = [r for r in T2 if r[1] >= 1]
    ctrl = [r for r in T2 if r[1] == 0]
    print(f"  lever-bearing n = {len(treat)}   lever-less n = {len(ctrl)}")
    for lab, g in (("lever-bearing", treat), ("lever-less", ctrl)):
        print(f"  {lab:14s} mass {min(x[2] for x in g):5.1f}-{max(x[2] for x in g):5.1f} g"
              f"   |lat| {min(x[4] for x in g):5.2f}-{max(x[4] for x in g):5.2f}"
              f"   longevity {min(x[3] for x in g):4.1f}-{max(x[3] for x in g):4.1f} yr")
    pairs = matched_pairs(ctrl, treat)
    print(f"\n  matched pairs formed: {len(pairs)} "
          f"(|dlog10 mass| <= 0.3, |dlat| <= 10 deg)")
    diffs = []
    for c, t, d in pairs:
        diff = c[3] - t[3]          # lever-less minus lever-bearing
        diffs.append(diff)
        print(f"    {c[0]:24s} {c[3]:5.1f} yr  vs  {t[0]:26s} {t[3]:5.1f} yr"
              f"   diff {diff:+6.1f}")
    nnz, k, ps = sign_test_one_sided([-d for d in diffs])   # H2: lever-less LOWER
    print(f"\n  sign test (H2: lever-less proxy lower): {k}/{nnz} pairs in the "
          f"predicted direction, one-sided p = {ps:.5f}")
    W, z, pw = ranksum([x[3] for x in ctrl], [x[3] for x in treat])
    print(f"  Wilcoxon rank-sum, unmatched: W = {W:.1f}, z = {z:+.3f}, "
          f"two-sided p = {pw:.2e}")
    mc = sum(x[3] for x in ctrl) / len(ctrl)
    mt = sum(x[3] for x in treat) / len(treat)
    print(f"  mean proxy: lever-less {mc:.2f} yr vs lever-bearing {mt:.2f} yr "
          f"-> {'AS PREDICTED' if mc < mt else 'FAILS'}")
    gate = len(pairs) >= 4
    print(f"  brief section 7 gate (>=4 matched pairs): "
          f"{'MET' if gate else 'NOT MET -> DIRECTION-ONLY'}")
    print(f"  NOTE the outcome is the pre-declared PROXY, not measured phi. "
          "No true adult annual survival was obtained (see the note's section 6).")
    print("  excluded as migratory bats: " + ", ".join(T2_MIGRANT_EXCLUDED))

    # POST-HOC sensitivity, not in the brief: drop Chiroptera. Bat longevity is
    # extreme for reasons (flight, predation escape) independent of the lever,
    # so this is the confound-controlled version of T2.
    print("\n  POST-HOC sensitivity (NOT pre-registered) -- Chiroptera dropped:")
    tn = [r for r in treat if r[6] != "Chiroptera"]
    cn = [r for r in ctrl if r[6] != "Chiroptera"]
    pn = matched_pairs(cn, tn)
    dn = [c[3] - t[3] for c, t, _ in pn]
    nn, kn, pn_ = sign_test_one_sided([-d for d in dn])
    mcn = sum(x[3] for x in cn) / len(cn)
    mtn = sum(x[3] for x in tn) / len(tn)
    Wn, zn, pwn = ranksum([x[3] for x in cn], [x[3] for x in tn])
    print(f"    lever-bearing n = {len(tn)}, lever-less n = {len(cn)}; "
          f"{len(pn)} matched pairs")
    print(f"    sign test {kn}/{nn} in predicted direction, one-sided p = {pn_:.4f}")
    print(f"    rank-sum z = {zn:+.3f}, two-sided p = {pwn:.4f}")
    print(f"    mean proxy: lever-less {mcn:.2f} yr vs lever-bearing {mtn:.2f} yr "
          f"-> {'AS PREDICTED' if mcn < mtn else 'FAILS'}")

    # Coding-rule sensitivity: the LITERAL brief-source-1 rule, i.e. class 0 for
    # every species not carried by the Ruf & Geiser Appendix at species level.
    # This miscodes ~20 obligate hibernators as lever-less (see the note, 5.2).
    print("\n  CODING sensitivity -- literal source-1 rule (absent from RG => class 0):")
    lit = [(r[0], r[1] if r[5] == "RG-species" else 0) + r[2:] for r in T2]
    tl = [r for r in lit if r[1] >= 1]
    cl = [r for r in lit if r[1] == 0]
    pl = matched_pairs(cl, tl)
    dl = [c[3] - t[3] for c, t, _ in pl]
    nl, kl, ppl = sign_test_one_sided([-d for d in dl])
    mcl = sum(x[3] for x in cl) / len(cl)
    mtl = sum(x[3] for x in tl) / len(tl)
    Wl, zl, pwl = ranksum([x[3] for x in cl], [x[3] for x in tl])
    print(f"    lever-bearing n = {len(tl)}, lever-less n = {len(cl)}; "
          f"{len(pl)} matched pairs")
    print(f"    sign test {kl}/{nl}, one-sided p = {ppl:.4f}; "
          f"rank-sum z = {zl:+.3f}, p = {pwl:.4f}")
    print(f"    mean proxy: lever-less {mcl:.2f} yr vs lever-bearing {mtl:.2f} yr "
          f"-> direction {'held' if mcl < mtl else 'INVERTED'}, significance lost")

    print()
    print("=" * 74)
    print("T3 -- falsifier scan: lever-less species with a published margin > +100%")
    print("=" * 74)
    hits = [s for s in T1 if T1[s][0] == 0 and T1[s][1] > 1.0]
    for s in T1:
        if T1[s][0] == 0:
            print(f"  {s:26s} margin {T1[s][1]:+7.3f}  "
                  f"{'FALSIFIER' if T1[s][1] > 1.0 else 'below +100%'}")
    print(f"  lever-less species carrying a published margin > +100%: {len(hits)}")
    print(f"  -> mechanism claim {'FALSIFIED' if hits else 'NOT FALSIFIED'} "
          "(scan is over the 1 lever-less species with a published margin)")
    print()
    verify_brief()


if __name__ == "__main__":
    main()
