#!/usr/bin/env python3
"""C47 - is `tfact` a depth label? Pre-registered mechanism test on independent sites.

Pre-registered in audits/blind-brief-c47-2026-09-05.md
sha256 13a3dad415f32d327eb9666111e0c5268d380cbdd543730ae5e5077cfe6daad6
hashed 2026-09-05 before any new site's tfact, restriction depth or erosion rate was fetched.

Run from vault/:   python _scripts/c47_tfact.py     (cache in _scripts/c47_data/)

Sources, both fetched 2026-09-05:
  P side  Portenga & Bierman 2011, GSA Today 21(8):4-10, 10.1130/G111A.1.
          GSA supplemental item 2011216 (Figshare 10.1130/2011216, CC BY-NC 4.0),
          Table DR2 "Bedrock Outcrop Data", CRONUS-recalculated erosion rate m/My.
  T side  USDA-NRCS Soil Data Access REST, same endpoint as C43:
          SDA_Get_Mukey_from_intersection_with_WktWgs84 -> component (tfact,
          slope_r, comppct_r), chorizon (dbthirdbar_r), corestrictions
          (resdept_r), muaggatt (brockdepmin).
  Rule    NSSH Part 618 Subpart B (Amended August 2024) Figure 618B-3.
"""
import json, math, os, random, re, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "c47_data")
os.makedirs(CACHE, exist_ok=True)
sys.path.insert(0, HERE)
from c43_soil_data import spearman, median, TON_AC_TO_T_HA, RHO_DEFAULT, UA  # noqa: E402

SDA = "https://sdmdataaccess.sc.egov.usda.gov/Tabular/post.rest"
PDF = os.path.join(CACHE, "portenga2011_2011216.pdf")
SEED = 20260905
BOX = (-125.0, -66.0, 24.0, 50.0)          # lon_min, lon_max, lat_min, lat_max
EXCL_DEG = 0.005                            # C43 independence radius

# NSSH Fig. 618B-3, depth (cm) -> T by renewability group
BINS = [(0, 25), (25, 50), (50, 100), (100, 150), (150, 1e9)]
GROUPS = {1: [1, 1, 2, 3, 5], 2: [1, 2, 3, 4, 5], 3: [3, 3, 4, 4, 5]}


def depth_bin(cm):
    for i, (lo, hi) in enumerate(BINS):
        if lo <= cm < hi:
            return i
    return 4


# ---------------------------------------------------------------- SDA
def sda(lon, lat):
    key = os.path.join(CACHE, "sda_%.5f_%.5f.json" % (lon, lat))
    if os.path.exists(key):
        return json.load(open(key))
    q = ("SELECT co.comppct_r, co.tfact, co.slope_r, "
         "(SELECT MIN(ch.dbthirdbar_r) FROM chorizon ch "
         " WHERE ch.cokey = co.cokey AND ch.hzdept_r = 0) AS rho, "
         "(SELECT MIN(cr.resdept_r) FROM corestrictions cr "
         " WHERE cr.cokey = co.cokey) AS resdept, mag.brockdepmin "
         "FROM SDA_Get_Mukey_from_intersection_with_WktWgs84('point(%.6f %.6f)') AS m "
         "INNER JOIN component co ON co.mukey = m.mukey "
         "LEFT OUTER JOIN muaggatt mag ON mag.mukey = m.mukey "
         "ORDER BY co.comppct_r DESC" % (lon, lat))
    body = json.dumps({"format": "JSON+COLUMNNAME", "query": q}).encode()
    req = urllib.request.Request(SDA, data=body,
                                 headers={"Content-Type": "application/json", **UA})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            out = json.loads(r.read().decode())
    except Exception as e:
        return {"error": str(e)}
    rows = out.get("Table") or []
    res = {"rows": rows[1:] if rows else []}
    json.dump(res, open(key, "w"))
    return res


def prefetch(points, workers=8):
    """Warm the per-point SDA cache concurrently. Order-independent: the cache
    file name is the coordinate, so results are identical to a serial run."""
    from concurrent.futures import ThreadPoolExecutor
    todo = [(lo, la) for lo, la in points
            if not os.path.exists(os.path.join(CACHE, "sda_%.5f_%.5f.json" % (lo, la)))]
    if not todo:
        return
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for i, _ in enumerate(ex.map(lambda p: sda(*p), todo), 1):
            if i % 100 == 0:
                print("   fetched %d/%d" % (i, len(todo)), flush=True)


def site_record(lon, lat):
    """Dominant component: tfact, slope, rho_b, restriction depth + its source."""
    res = sda(lon, lat)
    rows = [r for r in res.get("rows", []) if r[1] is not None]
    if not rows:
        return None
    c = rows[0]
    tfact = float(c[1])
    slope = float(c[2]) if c[2] is not None else None
    rho = float(c[3]) * 1000.0 if c[3] is not None else RHO_DEFAULT
    if c[4] is not None:
        depth, src = float(c[4]), "resdept_r"
    elif c[5] is not None:
        depth, src = float(c[5]), "brockdepmin"
    else:
        depth, src = 200.0, "none-assumed>150"
    return dict(lon=lon, lat=lat, tfact=tfact, slope=slope, rho=rho, depth=depth,
                depth_src=src, bin=depth_bin(depth),
                T=tfact * TON_AC_TO_T_HA * 100.0 / rho)


# ---------------------------------------------------------------- DR2 parse
NUM = re.compile(r"-?\d+(?:\.\d+)?")


def parse_dr2():
    """Table DR2 rows (PDF pp. 22-24, 0-based) with lat/lon and a CRONUS rate."""
    import pypdf
    r = pypdf.PdfReader(PDF)
    out = []
    for pg in (22, 23, 24):
        for line in (r.pages[pg].extract_text() or "").split("\n"):
            if "Table DR" in line or "decimal degrees" in line:
                continue
            toks = NUM.findall(line)
            if len(toks) < 6:
                continue
            # locate the AMS standard token; the rate columns follow it
            m = re.search(r"\b(\d*KNSTD\w*|NIST[_\w]*|LLNL\w*|S555\w*|07KNSTD|BEST\w*)\b", line)
            if not m:
                continue
            tail = NUM.findall(line[m.end():])
            head = NUM.findall(line[:m.start()])
            if len(tail) < 2 or len(head) < 2:
                continue
            # lat, lon are the first two decimal numbers of the row after the sample id
            latlon = [t for t in head if "." in t]
            if len(latlon) < 2:
                continue
            lat, lon = float(latlon[0]), float(latlon[1])
            # CRONUS rate: last token integer => it is % difference
            cron = float(tail[-3]) if "." not in tail[-1] else float(tail[-2])
            if not (BOX[0] <= lon <= BOX[1] and BOX[2] <= lat <= BOX[3]):
                continue
            if cron <= 0:
                continue
            out.append((lon, lat, cron / 1000.0))       # m/My -> mm/yr
    # de-duplicate identical coordinates (replicate analyses of one outcrop)
    seen, uniq = set(), []
    for lon, lat, p in out:
        k = (round(lon, 3), round(lat, 3))
        if k in seen:
            continue
        seen.add(k)
        uniq.append((lon, lat, p))
    return uniq


# ---------------------------------------------------------------- stats
def partial_spearman(x, y, z):
    """Spearman of x,y controlling z, by residualising ranks on ranks."""
    from c43_soil_data import ranks
    rx, ry, rz = ranks(x), ranks(y), ranks(z)

    def resid(a):
        mz, ma = sum(rz) / len(rz), sum(a) / len(a)
        b = (sum((p - mz) * (q - ma) for p, q in zip(rz, a))
             / sum((p - mz) ** 2 for p in rz))
        return [q - (ma + b * (p - mz)) for p, q in zip(rz, a)]
    ex, ey = resid(rx), resid(ry)
    n = len(ex)
    mx, my = sum(ex) / n, sum(ey) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(ex, ey))
    sxx = sum((a - mx) ** 2 for a in ex)
    syy = sum((b - my) ** 2 for b in ey)
    return sxy / math.sqrt(sxx * syy)


def h1(recs, label):
    g2 = sum(1 for s in recs if s["tfact"] == GROUPS[2][s["bin"]])
    band = sum(1 for s in recs
               if min(GROUPS[g][s["bin"]] for g in GROUPS) <= s["tfact"]
               <= max(GROUPS[g][s["bin"]] for g in GROUPS))
    n = len(recs)
    print("H1 %s: n=%d  Group-2 agreement %.1f%%   band agreement %.1f%%"
          % (label, n, 100.0 * g2 / n, 100.0 * band / n))
    print("   depth source: " + ", ".join(
        "%s %d" % (k, sum(1 for s in recs if s["depth_src"] == k))
        for k in ("resdept_r", "brockdepmin", "none-assumed>150")))
    print("   observed tfact x depth bin (rows = bin 0-25/25-50/50-100/100-150/>150):")
    for b in range(5):
        row = [sum(1 for s in recs if s["bin"] == b and s["tfact"] == t)
               for t in (1, 2, 3, 4, 5)]
        print("     bin %d  %-28s  predicted G1/G2/G3 = %d/%d/%d"
              % (b, row, GROUPS[1][b], GROUPS[2][b], GROUPS[3][b]))
    return 100.0 * g2 / n, 100.0 * band / n


def main():
    # ---- H1 on the pre-registered 1,500 random CONUS points
    rnd = random.Random(SEED)
    pts = [(rnd.uniform(BOX[0], BOX[1]), rnd.uniform(BOX[2], BOX[3]))
           for _ in range(1500)]
    prefetch(pts)
    rand = [r for r in (site_record(lo, la) for lo, la in pts) if r]
    print("random CONUS points drawn 1500, answered with a tfact: %d\n" % len(rand))
    h1(rand, "random CONUS points")

    # ---- the independent erosion-rate sites
    dr2 = parse_dr2()
    prefetch([(lo, la) for lo, la, _ in dr2])
    c43 = json.load(open(os.path.join(HERE, "c43_data", "sites.json")))
    dropped = 0
    sites = []
    for lon, lat, p in dr2:
        if any(abs(lon - s["lon"]) < EXCL_DEG and abs(lat - s["lat"]) < EXCL_DEG
               for s in c43):
            dropped += 1
            continue
        r = site_record(lon, lat)
        if r:
            r["P"] = p
            r["ratio"] = r["T"] / p
            sites.append(r)
    print("\nDR2 CONUS outcrop points with a CRONUS rate: %d" % len(dr2))
    print("dropped within %.3f deg of a C43 site: %d" % (EXCL_DEG, dropped))
    print("joined to an SSURGO tfact: %d" % len(sites))
    json.dump(sites, open(os.path.join(CACHE, "sites.json"), "w"), indent=1)
    if len(sites) < 30:
        print("\nBELOW the pre-registered n=30 gate: H2 and H3 are an honest null "
              "on data availability.")
        return
    print()
    h1(sites, "DR2 outcrop sites")

    P = [s["P"] for s in sites]
    print("\nH2: rho(P, depth bin) = %.3f  p = %.3g" % spearman(P, [s["bin"] for s in sites]))
    print("    rho(P, resdept cm) = %.3f  p = %.3g" % spearman(P, [s["depth"] for s in sites]))
    print("    rho(tfact, P)      = %.3f  p = %.3g" % spearman([s["tfact"] for s in sites], P))
    print("    rho(T, P)          = %.3f  p = %.3g" % spearman([s["T"] for s in sites], P))
    print("\n    by tfact class:")
    for t in sorted({s["tfact"] for s in sites}):
        g = [s for s in sites if s["tfact"] == t]
        print("      tfact %.0f  n=%3d  median P = %.4f mm/yr  median T/P = %.2f"
              % (t, len(g), median([s["P"] for s in g]),
                 median([s["ratio"] for s in g])))

    print("\nH3 (within-class rho(T, P), classes with n >= 25):")
    worst = 0.0
    for t in sorted({s["tfact"] for s in sites}):
        g = [s for s in sites if s["tfact"] == t]
        if len(g) < 25:
            continue
        rho, p = spearman([s["T"] for s in g], [s["P"] for s in g])
        # T is constant within a tfact class unless rho_b varies; report both
        rho_d, p_d = spearman([s["depth"] for s in g], [s["P"] for s in g])
        print("   tfact %.0f  n=%3d  rho(T,P) = %.3f p=%.3g   rho(depth,P) = %.3f p=%.3g"
              % (t, len(g), rho, p, rho_d, p_d))
        worst = max(worst, abs(rho))
    print("   largest |rho| among qualifying classes: %.3f" % worst)

    sl = [s for s in sites if s["slope"] is not None]
    if len(sl) >= 30:
        rho_raw, p_raw = spearman([s["tfact"] for s in sl], [s["P"] for s in sl])
        rho_sl, p_sl = spearman([s["slope"] for s in sl], [s["P"] for s in sl])
        pr = partial_spearman([s["tfact"] for s in sl], [s["P"] for s in sl],
                              [s["slope"] for s in sl])
        print("\nslope covariate, n=%d:" % len(sl))
        print("   rho(tfact, P)            = %.3f  p = %.3g" % (rho_raw, p_raw))
        print("   rho(slope_r, P)          = %.3f  p = %.3g" % (rho_sl, p_sl))
        print("   partial rho(tfact, P | slope_r) = %.3f" % pr)


if __name__ == "__main__":
    main()
