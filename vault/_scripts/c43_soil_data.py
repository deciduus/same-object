#!/usr/bin/env python3
"""C43 — paired test of the C35 T-vs-measured-formation prediction.

Pre-registered in audits/blind-brief-c43-2026-09-05.md
sha256 dbae0496666126c4070f518f16d1bf997f6c6b9165469284f940440b5e7ef727

Run from vault/:   python _scripts/c43_soil_data.py
Add --fetch to re-pull the two remote sources (otherwise the cache is used).

Data, both open, both fetched 2026-09-05:

  P side  OCTOPUS v2.2 CRN International, be10-denude:crn_int_basins /
          crn_int_outlets, WFS at http://geoserver.octopusdata.org/geoserver/wfs
          (GetCapabilities 200; GetFeature outputFormat=csv 200). Field
          EBE_MMKYR = CAIRN-harmonised Be-10 denudation rate, mm/kyr.
          Codilean & Munack 2024, DOI 10.25900/57H4-VM77, CC BY 4.0.
  T side  USDA-NRCS Soil Data Access REST, POST to
          https://sdmdataaccess.sc.egov.usda.gov/Tabular/post.rest,
          SDA_Get_Mukey_from_intersection_with_WktWgs84 joined to component
          (tfact, comppct_r) and chorizon (dbthirdbar_r at hzdept_r = 0).

Unit chain, fixed in the brief:
  T [mm/yr] = tfact [short ton/ac/yr] * 2.2417 [t/ha per ton/ac] * 100 / rho_b
  where rho_b is in kg/m3 (dbthirdbar_r is g/cm3, so * 1000).
"""
import csv, json, math, os, random, re, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "c43_data")
os.makedirs(CACHE, exist_ok=True)
SEED = 20260905
TON_AC_TO_T_HA = 2.2417
RHO_DEFAULT = 1300.0          # kg/m3, C35 assumption, used only when SSURGO has none
UA = {"User-Agent": "biomimicry-vault/1.0 (mailto:deciduusleaf@gmail.com)"}

WFS = "http://geoserver.octopusdata.org/geoserver/wfs"
OUTLETS = (WFS + "?service=WFS&version=1.1.0&request=GetFeature"
           "&typeName=be10-denude:crn_int_outlets&outputFormat=csv"
           "&srsName=EPSG:4326&bbox=-125,24,-66,50,EPSG:4326")
BASINS = (WFS + "?service=WFS&version=1.1.0&request=GetFeature"
          "&typeName=be10-denude:crn_int_basins&outputFormat=csv&propertyName="
          "OBSID1,CNTRY,BASIN,AUTHOR,PUBYEAR,REFDOI,AREA,ELEV_AVE,SLP_AVE,"
          "EBE_MMKYR,EBE_ERR,MATERIAL")
SDA = "https://sdmdataaccess.sc.egov.usda.gov/Tabular/post.rest"


def get(url, path):
    if not os.path.exists(path) or "--fetch" in sys.argv:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=300) as r:
            open(path, "wb").write(r.read())
    return open(path, encoding="utf-8-sig").read()


def sda(lon, lat):
    """tfact + surface bulk density of the dominant component at a point."""
    key = os.path.join(CACHE, "sda_%.5f_%.5f.json" % (lon, lat))
    if os.path.exists(key):
        return json.load(open(key))
    q = ("SELECT co.comppct_r, co.tfact, ch.dbthirdbar_r "
         "FROM SDA_Get_Mukey_from_intersection_with_WktWgs84('point(%.6f %.6f)') AS m "
         "INNER JOIN component co ON co.mukey = m.mukey "
         "LEFT OUTER JOIN chorizon ch ON ch.cokey = co.cokey AND ch.hzdept_r = 0 "
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


def median(xs):
    xs = sorted(xs); n = len(xs)
    return xs[n // 2] if n % 2 else 0.5 * (xs[n // 2 - 1] + xs[n // 2])


def boot_ci(xs, n=10000, seed=SEED):
    rnd = random.Random(seed); k = len(xs)
    ms = sorted(median([xs[rnd.randrange(k)] for _ in range(k)]) for _ in range(n))
    return ms[int(0.025 * n)], ms[int(0.975 * n)]


def binom_two_sided(k, n):
    """Exact two-sided binomial p at p0 = 0.5."""
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
        avg = (i + j) / 2.0 + 1
        for k in range(i, j + 1):
            r[order[k]] = avg
        i = j + 1
    return r


def spearman(x, y):
    rx, ry = ranks(x), ranks(y); n = len(x)
    mx, my = sum(rx) / n, sum(ry) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    sxx = sum((a - mx) ** 2 for a in rx); syy = sum((b - my) ** 2 for b in ry)
    rho = sxy / math.sqrt(sxx * syy)
    if n < 4 or abs(rho) >= 1:
        return rho, float("nan")
    t = rho * math.sqrt((n - 2) / (1 - rho * rho))
    # two-sided p from Student t, series-free normal-ish approximation via incomplete beta
    x_ = (n - 2) / ((n - 2) + t * t)
    return rho, betainc(0.5 * (n - 2), 0.5, x_)


def betainc(a, b, x):
    """Regularised incomplete beta, continued fraction (NR 6.4)."""
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    lbeta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    front = math.exp(lbeta + a * math.log(x) + b * math.log(1 - x))
    if x < (a + 1) / (a + b + 2):
        return front * _cf(a, b, x) / a
    return 1 - math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
                        + b * math.log(1 - x) + a * math.log(x)) * _cf(b, a, 1 - x) / b


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


def main():
    out_txt = get(OUTLETS, os.path.join(CACHE, "octopus_us_outlets.csv"))
    bas_txt = get(BASINS, os.path.join(CACHE, "octopus_basins.csv"))
    pts = {}
    for r in csv.DictReader(out_txt.splitlines()):
        m = re.search(r"POINT \(([-\d.]+) ([-\d.]+)\)", r["the_geom"] or "")
        if m:
            pts[r["OBSID1"]] = (float(m.group(1)), float(m.group(2)))
    bas = {r["OBSID1"]: r for r in csv.DictReader(bas_txt.splitlines())}

    sites, no_t = [], 0
    for oid, (lon, lat) in sorted(pts.items()):
        b = bas.get(oid)
        if not b or b.get("CNTRY") != "USA":
            continue
        try:
            p = float(b["EBE_MMKYR"]) / 1000.0          # mm/kyr -> mm/yr
        except (TypeError, ValueError):
            continue
        if p <= 0:
            continue
        res = sda(lon, lat)
        rows = [r for r in res.get("rows", []) if r[1] is not None]
        if not rows:
            no_t += 1
            continue
        top = rows[0]
        tfact = float(top[1])
        rho = float(top[2]) * 1000.0 if top[2] is not None else RHO_DEFAULT
        rho_assumed = top[2] is None
        t_mm = tfact * TON_AC_TO_T_HA * 100.0 / rho
        sites.append(dict(obsid=oid, lon=lon, lat=lat, basin=b.get("BASIN"),
                          author=b.get("AUTHOR"), year=b.get("PUBYEAR"),
                          doi=b.get("REFDOI"), slope=b.get("SLP_AVE"),
                          elev=b.get("ELEV_AVE"), P=p, tfact=tfact, rho=rho,
                          rho_assumed=rho_assumed, T=t_mm, ratio=t_mm / p,
                          Ha_T=p / t_mm))

    json.dump(sites, open(os.path.join(CACHE, "sites.json"), "w"), indent=1)
    n = len(sites)
    print("US OCTOPUS Be-10 sites with a coordinate: %d" % sum(
        1 for o in pts if bas.get(o, {}).get("CNTRY") == "USA"))
    print("matched to an SSURGO tfact: %d   (no tfact at point: %d)" % (n, no_t))
    if n < 5:
        print("BELOW n=5: honest null on data availability (brief section 5)")
        return
    ratios = [s["ratio"] for s in sites]
    med = median(ratios)
    lo, hi = boot_ci(ratios)
    k = sum(1 for r in ratios if r > 2)
    print("median T/P = %.3f   bootstrap 95%% CI [%.3f, %.3f]" % (med, lo, hi))
    print("sign test vs 2: %d of %d above, p = %.3g" % (k, n, binom_two_sided(k, n)))
    rho_s, p_s = spearman([s["T"] for s in sites], [s["P"] for s in sites])
    print("Spearman rho(T, P) = %.3f  p = %.3g" % (rho_s, p_s))
    print("median Ha_T = %.3f" % median([s["Ha_T"] for s in sites]))
    print("\nby tfact class:")
    for t in sorted({s["tfact"] for s in sites}):
        g = [s["ratio"] for s in sites if s["tfact"] == t]
        print("  tfact %.0f  n=%3d  median T/P = %.3f  median P = %.4f mm/yr"
              % (t, len(g), median(g),
                 median([s["P"] for s in sites if s["tfact"] == t])))
    lowrel = [s for s in sites if s["slope"] not in (None, "")
              and float(s["slope"]) < 100]           # SLP_AVE is in per-mille-ish units
    if len(lowrel) >= 5:
        print("\nEXPLORATORY (not pre-registered) low-gradient subset n=%d: "
              "median T/P = %.3f" % (len(lowrel),
                                     median([s["ratio"] for s in lowrel])))
    print("\nrho_b assumed (no SSURGO dbthirdbar_r): %d of %d"
          % (sum(1 for s in sites if s["rho_assumed"]), n))
    regional()


EU = {"AUT", "BEL", "BGR", "HRV", "CZE", "DNK", "EST", "FIN", "FRA", "DEU",
      "GRC", "HUN", "IRL", "ITA", "LVA", "LTU", "LUX", "MLT", "NLD", "POL",
      "PRT", "ROU", "SVK", "SVN", "ESP", "SWE", "CHE", "NOR", "GBR"}
# area-specific erosion, Mg/ha/yr, both full-text-read 2026-09-05
EROSION = {"Europe (Panagos 2015 RUSLE2015, erosion-prone land)": 2.46,
           "Europe (Borrelli 2017, 2001)": 0.92,
           "Oceania (Borrelli 2017, 2001)": 0.90,
           "Asia (Borrelli 2017, 2001)": 3.47,
           "North America (Borrelli 2017, 2001)": 2.23}


def regional():
    """Section 5 replication: regional Be-10 formation vs regional erosion."""
    bas = list(csv.DictReader(open(os.path.join(CACHE, "octopus_basins.csv"),
                                   encoding="utf-8-sig")))
    aus = os.path.join(CACHE, "octopus_aus_basins.csv")
    if not os.path.exists(aus):
        get(WFS + "?service=WFS&version=1.1.0&request=GetFeature&typeName="
            "be10-denude:crn_aus_basins&outputFormat=csv&propertyName="
            "OBSID1,CNTRY,EBE_MMKYR,SLP_AVE", aus)
    bas += list(csv.DictReader(open(aus, encoding="utf-8-sig")))

    def rates(sel, slope_cut=None):
        out = []
        for r in bas:
            if r.get("CNTRY") not in sel:
                continue
            try:
                v = float(r["EBE_MMKYR"])
                s = float(r["SLP_AVE"])
            except (TypeError, ValueError):
                continue
            if v > 0 and (slope_cut is None or s < slope_cut):
                out.append(v / 1000.0)
        return out

    print("\nregional Be-10 denudation medians (OCTOPUS, mm/yr):")
    reg = {}
    for lab, sel in (("Europe", EU), ("Australia", {"AUS"}),
                     ("China", {"CHN"}), ("USA", {"USA"})):
        for cut, tag in ((None, "all"), (150, "low-gradient")):
            v = rates(sel, cut)
            if v:
                reg[(lab, tag)] = median(v)
                print("  %-10s %-13s n=%4d  P = %.4f" % (lab, tag, len(v), median(v)))
    print("\nHa = P / erosion-depth, rho_b = %.0f kg/m3:" % RHO_DEFAULT)
    for name, e in EROSION.items():
        d = e * 100.0 / RHO_DEFAULT
        key = ("Europe" if "Europe" in name else
               "Australia" if "Oceania" in name else
               "China" if "Asia" in name else "USA")
        for tag in ("all", "low-gradient"):
            p = reg.get((key, tag))
            if p:
                print("  %-52s %-12s E = %.4f mm/yr  P = %.4f  Ha = %.3f"
                      % (name, tag, d, p, p / d))


if __name__ == "__main__":
    main()
