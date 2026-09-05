#!/usr/bin/env python3
"""c52_survival.py -- P-008 run against the pre-hashed brief
audits/blind-brief-c52-2026-09-05.md,
sha256 = bc2259e6984a3895a199f3585dc11ffad496162af7a50cb65c79948cac9f2547
over all 14,767 bytes. The brief was written and hashed BEFORE any adult
annual survival (phi) value was fetched. Check with --verify-brief.

What this script does, in the brief's own order:

L0  Build the lever coding under the brief's section 1.1 ASYMMETRIC rule --
    presence in the Ruf & Geiser 2015 appendix is sufficient for lever = 1,
    but lever = 0 requires an explicit negative (COMBINE hibernation_torpor
    = 0). Everything else is UNCODED and dropped. Written to
    c52_data/lever_codes.csv BEFORE any phi is read, and hashed.
L1  MAMMAL leg. Prior art: Turbill, Bieber & Ruf 2011, Proc R Soc B,
    10.1098/rspb.2011.0190 -- hibernators have ~15% higher annual survival
    than similar-sized non-hibernators, phylogenetic GLS. REDISCOVERED; this
    script only reports what a phi source would have to supply, and records
    that no open mammal phi source was obtained.
L2  BIRD leg -- the only new leg. BTO BirdFacts adult annual survival,
    scraped per species. Applies the brief's migrant rule and the asymmetric
    coding rule and reports the resulting n per arm.
L3  The banned-rules demonstration: what the same data yield if you use the
    two moves the brief forbids (code lever-less by absence, keep migrants).
    Reported as VOID BY CONSTRUCTION, in the C43 positive-control sense.
L4  P-072 falsifier scan.

All data are cached under c52_data/, all fetched 2026-09-05:
  Ruf & Geiser 2015 Biol. Rev. 90:891-926, 10.1111/brv.12137, per-species
    Appendix, open PMC copy PMC4351926 -> pmc4351926.html
  COMBINE, Soria et al. 2021 Ecology 102:e03344, 10.1002/ecy.3344,
    trait_data_reported.csv (NOT trait_data_imputed.csv -- forbidden by the
    brief section 3 positive-control clause)
    https://ndownloader.figshare.com/files/27703263
  PanTHERIA 1.0 WR05, 26-4_GR_MidRangeLat_dd
    https://esapubs.org/archive/ecol/E090/184/PanTHERIA_1-0_WR05_Aug2008.txt
  Amniote database, Myhrvold et al. 2015, 10.1890/15-0846R.1
    https://esapubs.org/archive/ecol/E096/269/Data_Files/Amniote_Database_Aug_2015.csv
  BTO BirdFacts, https://www.bto.org/understanding-birds/birdfacts/<slug>
    -> bto_<slug>.html, one file per species

Dependencies: stdlib only. Run from vault/:  python _scripts/c52_survival.py
"""
import argparse, csv, hashlib, html, math, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "c52_data")
BRIEF = os.path.join(HERE, "..", "..", "audits", "blind-brief-c52-2026-09-05.md")
BRIEF_SHA = "bc2259e6984a3895a199f3585dc11ffad496162af7a50cb65c79948cac9f2547"
BRIEF_BYTES = 14767
SEED = 20260905

# BTO slugs scraped, 2026-09-05. Chosen as: every British breeding species in
# the Ruf & Geiser avian appendix (swift, nightjar, house-martin) plus the
# small resident passerines BTO publishes adult survival for. "pied-wagtail"
# was requested and returned HTTP 404; recorded, not silently dropped.
BTO_SLUGS = ["swift", "nightjar", "house-martin", "blue-tit", "great-tit",
             "coal-tit", "wren", "robin", "dunnock", "goldcrest",
             "long-tailed-tit", "chaffinch", "greenfinch", "house-sparrow",
             "blackbird", "song-thrush", "treecreeper", "nuthatch",
             "willow-tit", "marsh-tit", "bullfinch", "reed-bunting",
             "yellowhammer", "skylark", "meadow-pipit", "starling", "linnet"]
BTO_404 = ["pied-wagtail"]

# slug -> (binomial, obligate long-distance migrant?, adult mass g)
# Migrant status by the brief's section 3 (vi) rule. Masses: BTO BirdFacts /
# standard field values, used only for the L3 matching demonstration.
BTO_META = {
    "swift": ("Apus apus", True, 44), "nightjar": ("Caprimulgus europaeus", True, 83),
    "house-martin": ("Delichon urbicum", True, 19),
    "blue-tit": ("Cyanistes caeruleus", False, 11),
    "great-tit": ("Parus major", False, 18), "coal-tit": ("Periparus ater", False, 9),
    "wren": ("Troglodytes troglodytes", False, 10),
    "robin": ("Erithacus rubecula", False, 18),
    "dunnock": ("Prunella modularis", False, 21),
    "goldcrest": ("Regulus regulus", False, 6),
    "long-tailed-tit": ("Aegithalos caudatus", False, 8),
    "chaffinch": ("Fringilla coelebs", False, 24),
    "greenfinch": ("Chloris chloris", False, 28),
    "house-sparrow": ("Passer domesticus", False, 30),
    "blackbird": ("Turdus merula", False, 100),
    "song-thrush": ("Turdus philomelos", False, 70),
    "treecreeper": ("Certhia familiaris", False, 10),
    "nuthatch": ("Sitta europaea", False, 23),
    "willow-tit": ("Poecile montanus", False, 11),
    "marsh-tit": ("Poecile palustris", False, 12),
    "bullfinch": ("Pyrrhula pyrrhula", False, 21),
    "reed-bunting": ("Emberiza schoeniclus", False, 19),
    "yellowhammer": ("Emberiza citrinella", False, 27),
    "skylark": ("Alauda arvensis", False, 38),
    "meadow-pipit": ("Anthus pratensis", False, 19),
    "starling": ("Sturnus vulgaris", False, 78),
    "linnet": ("Linaria cannabina", False, 19),
}


def sha256_file(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def verify_brief():
    b = open(BRIEF, "rb").read()
    ok = len(b) == BRIEF_BYTES and hashlib.sha256(b).hexdigest() == BRIEF_SHA
    print("brief bytes  = %d (expected %d)" % (len(b), BRIEF_BYTES))
    print("brief sha256 = %s" % hashlib.sha256(b).hexdigest())
    print("MATCH" if ok else "MISMATCH -- the brief has been edited since hashing")
    return 0 if ok else 1


# ------------------------------------------------------------------ sources
def ruf_geiser():
    """Per-species appendix -> {binomial: (AVES|MAMMALIA, class DT/HIB, lat)}."""
    s = open(os.path.join(DATA, "pmc4351926.html"), encoding="utf-8",
             errors="replace").read()
    tab = re.findall(r"<table.*?</table>", s, re.S)[0]
    out, grp = {}, None
    for r in re.findall(r"<tr.*?</tr>", tab, re.S):
        cells = [" ".join(html.unescape(re.sub(r"<[^>]+>", " ", c)).split())
                 for c in re.findall(r"<t[dh].*?</t[dh]>", r, re.S)]
        if len(cells) != 11 or cells[0] == "Taxon":
            continue
        if not cells[1]:
            if cells[0].isupper():
                grp = cells[0]
            continue
        out[cells[0].split(" (")[0]] = (grp, cells[1], cells[9])
    return out


def pantheria_lat():
    out = {}
    with open(os.path.join(DATA, "pantheria.txt")) as f:
        for r in csv.DictReader(f, delimiter="\t"):
            v = r["26-4_GR_MidRangeLat_dd"]
            if v not in ("-999", ""):
                out[r["MSW05_Binomial"]] = float(v)
    return out


def combine_rows():
    with open(os.path.join(DATA, "combine_reported.csv"), encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def bto_phi(slug):
    """Adult annual survival scraped from a cached BTO BirdFacts page."""
    p = os.path.join(DATA, "bto_%s.html" % slug)
    h = open(p, encoding="utf-8", errors="replace").read()
    i = h.find("Survival of adults")
    if i < 0:
        return None, None
    txt = " ".join(html.unescape(re.sub(r"<[^>]+>", " ", h[i:i + 900])).split())
    m = re.search(r"All adults\s+(0\.\d+)(?:\s*±\s*(0\.\d+))?", txt)
    if not m:
        return None, None
    return float(m.group(1)), (float(m.group(2)) if m.group(2) else None)


# ------------------------------------------------------------------ stats
def boot_ci(vals, n=10000, seed=SEED):
    if not vals:
        return (float("nan"), float("nan"))
    rng = random.Random(seed)
    k = len(vals)
    means = sorted(sum(rng.choice(vals) for _ in range(k)) / k for _ in range(n))
    return means[int(0.025 * n)], means[int(0.975 * n)]


def sign_test_one_sided(pos, nontied):
    """P(X >= pos) under Binomial(nontied, 0.5)."""
    return sum(math.comb(nontied, k) for k in range(pos, nontied + 1)) / 2 ** nontied


# ------------------------------------------------------------------ legs
def build_lever_codes():
    """Brief section 1.1. Written before any phi is read."""
    ruf = ruf_geiser()
    lat = pantheria_lat()
    rows, counts = [], {"lever1": 0, "lever0": 0, "UNCODED": 0, "CONFLICT": 0}
    for r in combine_rows():
        sp = (r["genus"] + " " + r["species"]).strip()
        if r["order"] not in ("Chiroptera", "Rodentia", "Eulipotyphla"):
            continue
        try:
            m = float(r["adult_mass_g"])
        except ValueError:
            continue
        if m >= 100:
            continue
        la = lat.get(sp)
        if la is None or abs(la) < 35:
            continue
        ht = r["hibernation_torpor"].strip()
        in_ruf = sp in ruf
        if in_ruf and ht == "0":
            code = "CONFLICT"
        elif in_ruf:
            code = "lever1"
        elif ht == "0":
            code = "lever0"
        else:
            code = "UNCODED"
        counts[code] += 1
        rows.append({"binomial": sp, "order": r["order"], "family": r["family"],
                     "adult_mass_g": "%.4g" % m, "midrange_lat_dd": "%.3f" % la,
                     "combine_hibernation_torpor": ht or "NA",
                     "in_ruf_geiser_appendix": "1" if in_ruf else "0",
                     "ruf_geiser_class": ruf[sp][1] if in_ruf else "",
                     "lever_code": code})
    rows.sort(key=lambda d: d["binomial"])
    path = os.path.join(DATA, "lever_codes.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    return rows, counts, path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify-brief", action="store_true")
    a = ap.parse_args()
    if a.verify_brief:
        return verify_brief()

    print("=" * 74)
    print("C52 -- P-008, setpoint lever vs adult annual survival")
    print("brief sha256 %s (%d bytes)" % (BRIEF_SHA, BRIEF_BYTES))
    print("=" * 74)

    # -- L0 -----------------------------------------------------------------
    print("\n[L0] lever coding, brief section 1.1 asymmetric rule")
    rows, counts, path = build_lever_codes()
    tot = len(rows)
    print("  small (<100 g) temperate (|lat|>=35) Chiroptera/Rodentia/"
          "Eulipotyphla in COMBINE x PanTHERIA: n = %d" % tot)
    for k in ("lever1", "lever0", "UNCODED", "CONFLICT"):
        print("    %-9s %4d  (%.1f%%)" % (k, counts[k], 100.0 * counts[k] / tot))
    print("  lever_codes.csv sha256 = %s" % sha256_file(path))
    print("  -> the asymmetric rule codes %d of %d species (%.1f%%); it refuses"
          % (counts["lever1"] + counts["lever0"], tot,
             100.0 * (counts["lever1"] + counts["lever0"]) / tot))
    print("     to infer 'lever-less' from absence, which is what C40 had to do.")
    by_order = {}
    for r in rows:
        by_order.setdefault((r["order"], r["lever_code"]), 0)
        by_order[(r["order"], r["lever_code"])] += 1
    for k in sorted(by_order):
        print("      %-14s %-8s %4d" % (k[0], k[1], by_order[k]))

    # -- L1 -----------------------------------------------------------------
    print("\n[L1] MAMMAL leg -- REDISCOVERED, and no open phi source")
    print("  Prior art: Turbill, Bieber & Ruf 2011, Proc R Soc B,")
    print("    10.1098/rspb.2011.0190 (Crossref-verified 2026-09-05, 283 cites):")
    print("    hibernators have ~15% higher annual survival than similar-sized")
    print("    non-hibernators, phylogenetic GLS. That IS H1 for mammals.")
    hdr = open(os.path.join(DATA, "amniote.csv"), encoding="utf-8",
               errors="replace").readline().strip().split(",")
    surv = [h for h in hdr if "surv" in h.lower()]
    print("  Amniote database (Myhrvold 2015) survival-bearing fields: %r" % surv)
    print("  brief section 2 source 3 -> NEGATIVE RESULT: the field does not exist.")
    print("  brief section 2 sources 2 and 4 -> no machine-readable open mammal")
    print("    phi compilation obtained this run.")
    print("  brief section 2 gate: >=10 lever-less species WITH phi. n = 0.")
    print("  VERDICT: MAMMAL LEG NOT RUN ON phi. Longevity NOT substituted.")

    # -- L2 -----------------------------------------------------------------
    print("\n[L2] BIRD leg -- the only new leg")
    ruf = ruf_geiser()
    aves = {k: v for k, v in ruf.items() if v[0] == "AVES"}
    print("  Ruf & Geiser avian appendix: %d species" % len(aves))
    phi = {}
    for s in BTO_SLUGS:
        p, se = bto_phi(s)
        phi[s] = (p, se)
    got = [s for s in BTO_SLUGS if phi[s][0] is not None]
    print("  BTO BirdFacts adult annual survival obtained for %d/%d slugs "
          "(404: %r)" % (len(got), len(BTO_SLUGS), BTO_404))
    lever_bearing = [s for s in got if BTO_META[s][0] in aves]
    print("  of those, in the Ruf & Geiser appendix (lever = 1): %d -> %s"
          % (len(lever_bearing), [BTO_META[s][0] for s in lever_bearing]))
    kept = [s for s in lever_bearing if not BTO_META[s][1]]
    print("  after the brief's migrant-exclusion rule (section 3 vi): %d" % len(kept))
    print("    excluded as obligate long-distance migrants: %s"
          % [BTO_META[s][0] for s in lever_bearing if BTO_META[s][1]])
    print("  lever-less arm under the asymmetric rule: COMBINE is MAMMALS ONLY,")
    print("    and no avian compilation states homeothermy per species, so no")
    print("    bird can be coded lever = 0 from a second source. n = 0.")
    print("  VERDICT: BIRD LEG UNRUNNABLE. Both arms empty, by the two rules")
    print("    the brief fixed in advance. Brief section 7 predicted this.")

    # -- L3 -----------------------------------------------------------------
    print("\n[L3] the banned-rules demonstration -- VOID BY CONSTRUCTION")
    print("  What the same BTO data give if you use the two moves the brief")
    print("  forbids: (a) code lever-less by ABSENCE from Ruf & Geiser (C40's")
    print("  amended rule), (b) keep the migrants.")
    lv = [(BTO_META[s][0], phi[s][0], BTO_META[s][2]) for s in got
          if BTO_META[s][0] in aves]
    ll = [(BTO_META[s][0], phi[s][0], BTO_META[s][2]) for s in got
          if BTO_META[s][0] not in aves]
    mlv = sum(x[1] for x in lv) / len(lv)
    mll = sum(x[1] for x in ll) / len(ll)
    print("    lever-bearing n=%d mean phi = %.3f  %s"
          % (len(lv), mlv, [(x[0], x[1]) for x in lv]))
    print("    lever-less    n=%d mean phi = %.3f" % (len(ll), mll))
    print("    naive delta phi = %+.3f" % (mlv - mll))
    # matched pairs within 2x mass, greedy, seedless (deterministic order)
    used, pairs = set(), []
    for name, p, m in sorted(lv, key=lambda x: x[2]):
        best = None
        for nm2, p2, m2 in sorted(ll, key=lambda x: x[2]):
            if nm2 in used:
                continue
            if abs(math.log10(m) - math.log10(m2)) <= 0.301:
                if best is None or abs(math.log10(m) - math.log10(m2)) < best[3]:
                    best = (nm2, p2, m2, abs(math.log10(m) - math.log10(m2)))
        if best:
            used.add(best[0])
            pairs.append((name, p, best[0], best[1]))
    d = [a - b for _, a, _, b in pairs]
    lo, hi = boot_ci(d)
    pos = sum(1 for x in d if x > 0)
    nontied = sum(1 for x in d if x != 0)
    print("    matched pairs within 2x mass: %d" % len(pairs))
    for nm, a, nm2, b in pairs:
        print("      %-24s %.3f  vs %-24s %.3f  d=%+.3f" % (nm, a, nm2, b, a - b))
    if d:
        print("    mean delta phi = %+.3f, bootstrap 95%% CI [%+.3f, %+.3f], "
              "seed %d" % (sum(d) / len(d), lo, hi, SEED))
        print("    one-sided sign test %d/%d, p = %.4f"
              % (pos, nontied, sign_test_one_sided(pos, nontied)))
    print("    GATE (>=8 non-tied pairs): %s -- %d"
          % ("MET" if nontied >= 8 else "NOT MET", nontied))
    print("  This is reported ONLY to show that the banned rules manufacture a")
    print("  positive result from data the pre-registered rules call empty.")
    print("  It is not evidence for H1. In C43's language it is a positive")
    print("  control by construction: swifts and nightjars are aerial")
    print("  insectivores with long adult lifespans for reasons -- flight,")
    print("  predation escape, migration -- that have nothing to do with torpor.")

    # -- L4 -----------------------------------------------------------------
    print("\n[L4] P-072 falsifier scan")
    print("  8 Europe PMC formulations run 2026-09-05 (listed in the C52 note).")
    print("  Lever-less small endotherms carrying a PUBLISHED reserve margin: 1")
    print("    (Sorex araneus, -69%, Keicher 2017 via C38 section 2)")
    print("  Of those with margin > +100%: 0")
    print("  NOT FALSIFIED -- over a reach of n = 1. Still a formality, not a")
    print("  test. C40's reach was also 1; this run did not widen it.")

    print("\n" + "=" * 74)
    print("OVERALL: H1 NOT TESTED on phi. Mammal leg REDISCOVERED (Turbill 2011)")
    print("and unrunnable for lack of an open phi source; bird leg -- the only")
    print("new leg -- structurally unrunnable because in temperate avifauna the")
    print("lever and long-distance migration are alternative solutions to the")
    print("same winter energy problem, so the migrant rule empties the lever arm.")
    print("=" * 74)
    return 0


if __name__ == "__main__":
    sys.exit(main())
