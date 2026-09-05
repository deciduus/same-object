#!/usr/bin/env python3
"""C44 - the world soil-`Ha` ledger at site level. Programme item P-001, Track A.

Pre-registered in audits/blind-brief-c44-2026-09-05.md
sha256 724ae9034bbc61761dad85b1c32ea32479708f4098e51a76b9e94634e806ab6b
(hashed 2026-09-05 before any erosion value was joined to any site).

Run from vault/:   python _scripts/c44_world.py
Add --fetch to re-pull the remote sources (otherwise the c44_data/ cache is used).

Data, all open, all fetched 2026-09-05:

  P side  OCTOPUS v2.2, WFS http://geoserver.octopusdata.org/geoserver/wfs.
          GetCapabilities 200; it advertises four Be-10 basin/outlet pairs:
          crn_int_*, crn_aus_*, crn_xxl_*, crn_inprep_*. All four fetched,
          GLOBALLY, no bbox (C43 used a CONUS bbox). Field EBE_MMKYR =
          CAIRN-harmonised Be-10 denudation, mm/kyr. CC BY 4.0.
  E side  Borrelli et al. 2017, Nat. Commun. 8:2013, 10.1038/s41467-017-02142-7,
          gold OA, article HTML + all four Supplementary files read 2026-09-05.
          The 25 km GeoTIFF itself is behind an ESDAC registration form
          ("Registration is requested: Yes") and was NOT downloaded; the paper's
          Data Availability points only at the article and its SI, and neither
          SI file carries a country table (MOESM1 = notes/figures/C-factors,
          MOESM2 = peer-review file, MOESM3/4 = crop groups). So brief clause
          2(a) and 2(b) failed and clause 2(c), the continental rates, is used.
  E side  Panagos et al. 2015, Environ. Sci. Policy 54:438-447,
          10.1016/j.envsci.2015.08.012, Table 1, PDF read in full from the KU
          Leuven Lirias repository copy: a genuine PER-COUNTRY E for EU-28.
"""
import csv, json, math, os, random, re, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "c44_data")
os.makedirs(CACHE, exist_ok=True)
SEED = 20260905
RHO_B = 1300.0                     # kg/m3, fixed in the brief, not tuned
UA = {"User-Agent": "biomimicry-vault/1.0 (mailto:deciduusleaf@gmail.com)"}
WFS = "http://geoserver.octopusdata.org/geoserver/wfs"
ATTRS = "OBSID1,CNTRY,BASIN,AUTHOR,PUBYEAR,AREA,ELEV_AVE,SLP_AVE,EBE_MMKYR"

# --- E side, t/ha/yr ---------------------------------------------------------
# Borrelli 2017, printed continental means, baseline scenario, 2001.
BORRELLI_CONT = {"South America": 3.53, "Africa": 3.51, "Asia": 3.47,
                 "North America": 2.23, "Europe": 0.92, "Oceania": 0.90}
BORRELLI_GLOBAL = 2.8
# Borrelli 2017, printed land-use means (both periods, 2012 figures quoted).
BORRELLI_LC = {"cropland": 12.7, "other natural vegetation": 1.84,
               "forest": 0.16, "all land (global mean)": 2.8}
BORRELLI_T = 10.0                  # its "generic tolerable soil erosion threshold"
# Panagos 2015 Table 1: overall mean E, then mean E on arable land.
PANAGOS = {
    "AUT": (7.19, 3.97), "BEL": (1.22, 2.06), "BGR": (2.05, 2.47),
    "CYP": (2.89, 1.85), "CZE": (1.65, 2.52), "DEU": (1.25, 1.75),
    "DNK": (0.50, 0.61), "EST": (0.21, 0.70), "ESP": (3.94, 4.27),
    "FIN": (0.06, 0.46), "FRA": (2.25, 1.99), "GRC": (4.13, 2.77),
    "HRV": (3.16, 1.67), "HUN": (1.62, 2.10), "IRL": (0.96, 1.32),
    "ITA": (8.46, 8.38), "LTU": (0.52, 0.95), "LUX": (2.07, 4.54),
    "LVA": (0.32, 1.01), "MLT": (6.02, 15.93), "NLD": (0.27, 0.54),
    "POL": (0.96, 1.61), "PRT": (2.31, 2.94), "ROU": (2.84, 3.39),
    "SWE": (0.41, 1.12), "SVN": (7.43, 4.63), "SVK": (2.18, 3.54),
    "GBR": (2.38, 1.04)}
# Published national/supra-national tolerable-loss numbers, t/ha/yr. H2c only.
NATIONAL_T = {
    "EU": (0.3, 1.4, "Verheijen et al. 2009 proposed range for Europe; the "
                     "1.4 upper bound is quoted by Panagos 2015 as the European "
                     "mean soil formation rate"),
    "USA": (2.24, 11.21, "USDA tfact 1-5 short ton/ac/yr converted at 2.2417"),
    "GLOBAL": (10.0, 10.0, "Borrelli et al. 2017's generic T-value")}

CONTINENT = {
    "Africa": "DZA EGY KEN MAR MDG NAM NGA SDN SWZ UGA ZAF ZMB ZWE CMR COD",
    "Asia": ("AZE BGD BDG BTN CHN GEO IDN IND IRN ISR JPN KAZ KGZ KOR LKA MMR "
             "NPL PAK PHL RUS THA TJK TUR TWN VNM"),
    "Europe": ("AUT BEL BGR CHE CZE DEU DNK ESP EST FIN FRA GBR GRC HRV HUN IRL "
               "ISL ITA LTU LUX LVA MKD MLT NLD NOR POL PRT ROU SRB SVK SVN SWE"),
    "North America": "CAN CRI CUB DMA GTM HND JAM MEX NIC PAN PRI SLV TTO USA",
    "Oceania": "AUS NZL PNG",
    "South America": "ARG BOL BRA CHL COL ECU GUY PER SUR URY VEN"}
C2C = {c: k for k, v in CONTINENT.items() for c in v.split()}


def get(url, name):
    p = os.path.join(CACHE, name)
    if not os.path.exists(p) or "--fetch" in sys.argv:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA),
                                    timeout=900) as r:
            open(p, "wb").write(r.read())
    return open(p, encoding="utf-8-sig").read()


# --- statistics (same implementations as C43) --------------------------------
def median(xs):
    xs = sorted(xs); n = len(xs)
    return xs[n // 2] if n % 2 else 0.5 * (xs[n // 2 - 1] + xs[n // 2])


def boot_ci(xs, n=10000, seed=SEED):
    rnd = random.Random(seed); k = len(xs)
    ms = sorted(median([xs[rnd.randrange(k)] for _ in range(k)]) for _ in range(n))
    return ms[int(0.025 * n)], ms[int(0.975 * n)]


def binom_two_sided(k, n):
    lg = lambda i: (math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1)
                    - n * math.log(2.0))
    lk = lg(k)
    return min(1.0, sum(math.exp(lg(i)) for i in range(n + 1) if lg(i) <= lk + 1e-12))


def ranks(xs):
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs); i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        for k in range(i, j + 1):
            r[order[k]] = (i + j) / 2.0 + 1
        i = j + 1
    return r


def _cf(a, b, x):
    tiny = 1e-30; c, d = 1.0, 1 - (a + b) * x / (a + 1)
    d = tiny if abs(d) < tiny else d; d = 1 / d; h = d
    for m in range(1, 300):
        m2 = 2 * m
        for num in (m * (b - m) * x / ((a + m2 - 1) * (a + m2)),
                    -(a + m) * (a + b + m) * x / ((a + m2) * (a + m2 + 1))):
            d = 1 + num * d; d = tiny if abs(d) < tiny else d; d = 1 / d
            c = 1 + num / c; c = tiny if abs(c) < tiny else c
            h *= d * c
        if abs(d * c - 1) < 1e-12:
            break
    return h


def betainc(a, b, x):
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    lb = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    if x < (a + 1) / (a + b + 2):
        return math.exp(lb + a * math.log(x) + b * math.log(1 - x)) * _cf(a, b, x) / a
    return 1 - math.exp(lb + b * math.log(1 - x) + a * math.log(x)) * _cf(b, a, 1 - x) / b


def spearman(x, y):
    rx, ry = ranks(x), ranks(y); n = len(x)
    mx, my = sum(rx) / n, sum(ry) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    sxx = sum((a - mx) ** 2 for a in rx); syy = sum((b - my) ** 2 for b in ry)
    rho = sxy / math.sqrt(sxx * syy)
    if n < 4 or abs(rho) >= 1:
        return rho, float("nan")
    t = rho * math.sqrt((n - 2) / (1 - rho * rho))
    return rho, betainc(0.5 * (n - 2), 0.5, (n - 2) / ((n - 2) + t * t))


def mm(t_ha):
    """t/ha/yr -> mm/yr at rho_b = 1300 kg/m3."""
    return t_ha * 100.0 / RHO_B


# --- assemble the sites ------------------------------------------------------
def load():
    pts = {}
    for lyr in ("crn_int_outlets", "crn_aus_outlets", "crn_xxl_outlets",
                "crn_inprep_outlets"):
        txt = get(WFS + "?service=WFS&version=1.1.0&request=GetFeature&outputFormat=csv"
                  "&srsName=EPSG:4326&typeName=be10-denude:" + lyr, lyr + ".csv")
        for r in csv.DictReader(txt.splitlines()):
            m = re.search(r"POINT \(([-\d.]+) ([-\d.]+)\)", r.get("the_geom") or "")
            if m:
                pts.setdefault(r["OBSID1"], (float(m.group(1)), float(m.group(2))))

    rows = {}
    srcs = [("crn_int_basins", os.path.join(HERE, "c43_data", "octopus_basins.csv"))]
    for lyr in ("crn_aus_basins", "crn_xxl_basins", "crn_inprep_basins"):
        get(WFS + "?service=WFS&version=1.1.0&request=GetFeature&outputFormat=csv"
            "&propertyName=" + ATTRS + "&typeName=be10-denude:" + lyr, lyr + ".csv")
        srcs.append((lyr, os.path.join(CACHE, lyr + ".csv")))
    for lyr, path in srcs:
        for r in csv.DictReader(open(path, encoding="utf-8-sig")):
            r["_layer"] = lyr
            rows.setdefault(r["OBSID1"], r)      # precedence: int > aus > xxl > inprep

    sites = []
    for oid, r in sorted(rows.items()):
        try:
            p = float(r["EBE_MMKYR"]) / 1000.0
        except (TypeError, ValueError):
            continue
        cn = (r.get("CNTRY") or "").strip()
        if p <= 0 or not cn:
            continue
        cont = C2C.get(cn)
        if cont is None:
            continue
        lon, lat = pts.get(oid, (None, None))
        e_cont = mm(BORRELLI_CONT[cont])
        s = dict(obsid=oid, cntry=cn, cont=cont, layer=r["_layer"], lon=lon, lat=lat,
                 author=r.get("AUTHOR"), year=r.get("PUBYEAR"), slope=r.get("SLP_AVE"),
                 area=r.get("AREA"), P=p, E_cont=e_cont, Ha_cont=p / e_cont)
        if cn in PANAGOS:
            s["E_ctry"] = mm(PANAGOS[cn][0]); s["Ha_ctry"] = p / s["E_ctry"]
            s["E_arab"] = mm(PANAGOS[cn][1]); s["Ha_arab"] = p / s["E_arab"]
        sites.append(s)
    return sites


def cell(label, xs, floor=12):
    n = len(xs)
    if n < 5:
        return "%-26s n=%4d   not reported (n < 5)" % (label, n)
    med = median(xs); below = sum(1 for v in xs if v < 1)
    if n < floor:
        return ("%-26s n=%4d   median %.4f   %d/%d below 1   DIRECTION ONLY"
                % (label, n, med, below, n))
    lo, hi = boot_ci(xs)
    return ("%-26s n=%4d   median %.4f  CI [%.4f, %.4f]   %d/%d below 1"
            % (label, n, med, lo, hi, below, n))


def main():
    sites = load()
    json.dump(sites, open(os.path.join(CACHE, "sites.json"), "w"), indent=1)
    n = len(sites)
    print("=== C44 world soil-Ha ledger, site level ===")
    print("brief sha256 724ae9034bbc61761dad85b1c32ea32479708f4098e51a76b9e94634e806ab6b")
    print("OCTOPUS Be-10 sites, global, positive rate, mapped country: %d" % n)
    print("with an outlet coordinate: %d" % sum(1 for s in sites if s["lon"] is not None))
    print("distinct countries: %d" % len({s["cntry"] for s in sites}))

    ha = [s["Ha_cont"] for s in sites]
    med = median(ha); lo, hi = boot_ci(ha)
    k = sum(1 for v in ha if v < 1)
    print("\n-- H1, all sites, E = Borrelli 2017 continental mean --")
    print("median Ha = %.4f   bootstrap 95%% CI [%.4f, %.4f]" % (med, lo, hi))
    print("sign test vs 1: %d of %d below, p = %.3g" % (k, n, binom_two_sided(k, n)))
    nus = [s for s in sites if s["cntry"] != "USA"]
    hnu = [s["Ha_cont"] for s in nus]
    print("non-US only: n=%d  median Ha = %.4f  CI %s  %d below 1  p = %.3g"
          % (len(hnu), median(hnu), "[%.4f, %.4f]" % boot_ci(hnu),
             sum(1 for v in hnu if v < 1), binom_two_sided(sum(1 for v in hnu if v < 1),
                                                           len(hnu))))

    print("\n-- P vs E, Spearman across sites --")
    rho, p = spearman([s["P"] for s in sites], [s["E_cont"] for s in sites])
    print("continental E (6 distinct values): rho = %.3f  p = %.3g" % (rho, p))
    eu = [s for s in sites if "E_ctry" in s]
    if len(eu) >= 12:
        r2, p2 = spearman([s["P"] for s in eu], [s["E_ctry"] for s in eu])
        print("EU-28 country E (Panagos 2015, %d distinct countries): "
              "n=%d  rho = %.3f  p = %.3g"
              % (len({s["cntry"] for s in eu}), len(eu), r2, p2))

    print("\n-- Ha by continent (E = that continent's Borrelli mean) --")
    for c in sorted({s["cont"] for s in sites}):
        g = [s["Ha_cont"] for s in sites if s["cont"] == c]
        print("  " + cell("%s (E=%.2f t/ha)" % (c, BORRELLI_CONT[c]), g))

    print("\n-- Ha by country, n >= 10 (brief section 4.1) --")
    print("  %-4s %-14s %5s %9s %9s %20s %7s" %
          ("ISO", "continent", "n", "med P", "E mm/yr", "median Ha [95% CI]", "<1"))
    for cn in sorted({s["cntry"] for s in sites}):
        g = [s for s in sites if s["cntry"] == cn]
        if len(g) < 10:
            continue
        use_ctry = "E_ctry" in g[0]
        h = [s["Ha_ctry"] if use_ctry else s["Ha_cont"] for s in g]
        e = g[0]["E_ctry"] if use_ctry else g[0]["E_cont"]
        lo, hi = boot_ci(h)
        print("  %-4s %-14s %5d %9.4f %9.4f  %8.4f [%.4f, %.4f] %4d %s"
              % (cn, g[0]["cont"], len(g), median([s["P"] for s in g]), e,
                 median(h), lo, hi, sum(1 for v in h if v < 1),
                 "*" if use_ctry else ""))
    print("  * E is Panagos 2015 country mean; unmarked rows use the "
          "continental Borrelli mean, so Ha varies only through P.")

    print("\n-- Ha by land-cover class (Borrelli 2017's own strata; the sites "
          "themselves are NOT land-cover classified: no raster reader) --")
    for lab, e in sorted(BORRELLI_LC.items(), key=lambda kv: -kv[1]):
        d = mm(e)
        print("  %-26s E = %6.2f t/ha = %.4f mm/yr   global median Ha = %.4f"
              % (lab, e, d, median([s["P"] for s in sites]) / d))

    print("\n-- H2c, T/P where a published national tolerable-loss number exists --")
    for key, (tlo, thi, note) in NATIONAL_T.items():
        if key == "EU":
            g = [s for s in sites if s["cntry"] in PANAGOS]
        elif key == "USA":
            g = [s for s in sites if s["cntry"] == "USA"]
        else:
            g = sites
        if len(g) < 12:
            print("  %-7s n=%d  below the n=12 floor" % (key, len(g)))
            continue
        for t, tag in ((tlo, "low"), (thi, "high")):
            r = [mm(t) / s["P"] for s in g]
            lo, hi = boot_ci(r)
            print("  %-7s T=%5.2f t/ha (%-4s) n=%4d  median T/P = %8.2f  "
                  "CI [%.2f, %.2f]  %d/%d above 2"
                  % (key, t, tag, len(g), median(r), lo, hi,
                     sum(1 for v in r if v > 2), len(g)))
        print("          %s" % note)

    print("\n-- comparison rows --")
    print("  C43 US median T/P (USDA tfact, per site)          22.322")
    print("  C43 section 5 regional Ha: EU 0.187/0.499, AUS 0.120, "
          "ASIA 0.077, N.AM 0.096")
    for c in ("Europe", "Oceania", "Asia", "North America"):
        g = [s["Ha_cont"] for s in sites if s["cont"] == c]
        print("  C44 site-level median Ha, %-14s %.4f   (C43 used a regional "
              "median P, not a site median)" % (c, median(g)))


if __name__ == "__main__":
    main()
