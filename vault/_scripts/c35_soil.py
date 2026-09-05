#!/usr/bin/env python3
"""
c35_soil.py - the arithmetic behind vault/computed/C35-soil-ha.md, and the
citer-set intersection behind vault/gaps/G36-wear-erosion-damage.md.

Two independent jobs, one file, because they share the anchor list:

  python c35_soil.py            # soil Ha table only (no network)
  python c35_soil.py --fetch    # also re-run OpenCitations + Crossref

OPENCITATIONS BLANK-KEY TRAP
----------------------------
    https://api.opencitations.net/index/v1/citations/<doi>
returns some records with an **empty `citing`** field.  Building the citer set
without filtering adds a phantom "" element which inflates |A|, |B| and -- because
the phantom is in every set -- every intersection by exactly 1.  `citers()` below
drops blank/whitespace `citing` values and reports how many it dropped.  On the
2026-09-05 run the drop counts were: Archard 21, Miner 13, Paris 15, Meng 2,
Amezketa 1, and 0 for Nearing / Le Bissonnais / Denef / RUSLE.

UNITS
-----
Erosion is published two ways.  Mass: t ha^-1 yr^-1.  Depth: mm yr^-1.  They are
the same quantity only through a bulk density, which is itself a soil property
that erosion changes:

    depth [mm/yr] = mass [t/ha/yr] * 100 / rho_b [kg/m^3]

    (1 t/ha = 1000 kg / 1e4 m^2 = 0.1 kg/m^2; / rho_b -> m; * 1000 -> mm)

rho_b = 1300 kg/m^3 is an ASSUMPTION here, not a measurement; the plausible
range 1100-1600 moves every mass-derived depth by -15%/+18%.  Depth-native rows
(Montgomery 2007 Table 1) never pass through it, and are preferred for that reason.
"""
import sys

RHO_B = 1300.0          # kg/m^3, assumed; see UNITS above
T_ACRE_TO_HA = 2.2417   # short ton/acre -> t/ha (1 short ton = 0.90718 t; 1 ac = 0.40469 ha)


def depth_from_mass(t_per_ha_yr, rho_b=RHO_B):
    """t/ha/yr -> mm/yr."""
    return t_per_ha_yr * 100.0 / rho_b


def ha_and_a(k_r, k_d):
    """C6's healing Damkohler number and its availability. k_r, k_d in the same units."""
    Ha = k_r / k_d
    return Ha, Ha / (1.0 + Ha)


# --- Inputs -----------------------------------------------------------------
# Montgomery 2007, PNAS 104:13268-13272, DOI 10.1073/pnas.0611508104, Table 1,
# read from the author-hosted PDF (mssoy.org/sites/default/files/documents/
# montgomery-2007.pdf), fetched 2026-09-05. VERIFIED-PRIMARY. All mm/yr.
MONTGOMERY_T1 = {
    # label:                  (n,   median, mean,  s.e.)
    "Conventional agriculture": (448, 1.537, 3.939, 0.321),
    "Conservation agriculture": (47,  0.082, 0.124, 0.022),
    "Native vegetation":        (65,  0.013, 0.053, 0.016),
    "Soil production":          (188, 0.017, 0.036, 0.004),
    "Geological":               (925, 0.029, 0.173, 0.029),
}
# Borrelli et al. 2017, Nat. Commun. 8:2013, DOI 10.1038/s41467-017-02142-7.
# 35.0 Pg/yr (2001), 35.9 Pg/yr (2012, +2.5%), area-specific mean 2.8 Mg/ha/yr.
# VERIFIED-SECONDARY: DOI, title and authors from Crossref 2026-09-05; the
# numbers are from search snippets -- nature.com 303-redirects to an IdP and the
# full text was not obtained this session.
BORRELLI_MEAN_T_HA = 2.8
# USDA soil loss tolerance "T", 1-5 short tons/acre/yr (fragile -> deep soils).
T_VALUE_ACRE = (1.0, 5.0)


def main(argv=()):
    kr_med = MONTGOMERY_T1["Soil production"][1]     # 0.017 mm/yr
    kr_mean = MONTGOMERY_T1["Soil production"][2]    # 0.036 mm/yr

    print(f"rho_b = {RHO_B:.0f} kg/m3 ; 1 t/ha/yr = {depth_from_mass(1.0):.4f} mm/yr")
    t_lo, t_hi = (a * T_ACRE_TO_HA for a in T_VALUE_ACRE)
    print(f"USDA T = {T_VALUE_ACRE[0]:.0f}-{T_VALUE_ACRE[1]:.0f} ton/ac/yr "
          f"= {t_lo:.2f}-{t_hi:.2f} t/ha/yr = {depth_from_mass(t_lo):.3f}-"
          f"{depth_from_mass(t_hi):.3f} mm/yr")
    print(f"Borrelli global mean {BORRELLI_MEAN_T_HA} t/ha/yr "
          f"= {depth_from_mass(BORRELLI_MEAN_T_HA):.4f} mm/yr\n")

    rows = []
    for lab in ("Conventional agriculture", "Conservation agriculture", "Native vegetation"):
        n, med, mean, _ = MONTGOMERY_T1[lab]
        rows.append((f"{lab} (median, n={n})", kr_med, med))
        rows.append((f"{lab} (mean, n={n})", kr_mean, mean))
    rows.append(("Global cropland+ mean, Borrelli 2017", kr_med,
                 depth_from_mass(BORRELLI_MEAN_T_HA)))
    rows.append((f"USDA T policy point, T={T_VALUE_ACRE[0]:.0f} ton/ac (k_r := k_d)",
                 depth_from_mass(t_lo), depth_from_mass(t_lo)))
    rows.append((f"USDA T policy point, T={T_VALUE_ACRE[1]:.0f} ton/ac (k_r := k_d)",
                 depth_from_mass(t_hi), depth_from_mass(t_hi)))
    rows.append(("USDA T=1 ton/ac erosion vs MEASURED k_r", kr_med, depth_from_mass(t_lo)))
    rows.append(("USDA T=5 ton/ac erosion vs MEASURED k_r", kr_med, depth_from_mass(t_hi)))

    print(f"{'row':52s} {'k_r mm/yr':>10s} {'k_d mm/yr':>10s} {'Ha':>9s} {'A':>8s}")
    for lab, k_r, k_d in rows:
        Ha, A = ha_and_a(k_r, k_d)
        print(f"{lab:52s} {k_r:10.4f} {k_d:10.4f} {Ha:9.4f} {A:8.4f}")

    print("\nT-value overstatement of soil formation "
          f"(T in depth / measured k_r median): "
          f"{depth_from_mass(t_lo)/kr_med:.1f}x to {depth_from_mass(t_hi)/kr_med:.1f}x")

    if "--fetch" in argv:
        fetch()
    else:
        print("\n(pass --fetch to re-run the citation intersection)")
    return 0


# --- The G36 intersection ---------------------------------------------------
ANCHORS = {
    "archard1953":      "10.1063/1.1721448",
    "meng1995":         "10.1016/0043-1648(95)90158-2",
    "miner1945":        "10.1115/1.4009458",
    "paris1963":        "10.1115/1.3656900",
    "nearing1989":      "10.13031/2013.31195",
    "lebissonnais1996": "10.1111/j.1365-2389.1996.tb01843.x",
    "denef2001":        "10.1016/s0038-0717(01)00076-1",
    "amezketa1999":     "10.1300/j064v14n02_08",
    "rusle1991":        "10.1080/00224561.1991.12456571",
}
PAIRS = [
    # leg 1 -- wear <-> erosion detachment
    ("archard1953", "nearing1989"), ("archard1953", "lebissonnais1996"),
    ("meng1995", "nearing1989"), ("meng1995", "lebissonnais1996"),
    # leg 2 -- fatigue <-> aggregate breakdown
    ("miner1945", "lebissonnais1996"), ("miner1945", "denef2001"),
    ("miner1945", "amezketa1999"), ("paris1963", "lebissonnais1996"),
    ("paris1963", "denef2001"), ("paris1963", "amezketa1999"),
    ("meng1995", "denef2001"), ("archard1953", "denef2001"),
    ("archard1953", "amezketa1999"),
    # controls
    ("miner1945", "paris1963"), ("meng1995", "archard1953"),
    ("denef2001", "lebissonnais1996"), ("rusle1991", "nearing1989"),
    ("amezketa1999", "lebissonnais1996"),
]
MAILTO = "deciduusleaf@gmail.com"


def fetch():
    import json, urllib.parse, urllib.request
    def get(url):
        req = urllib.request.Request(
            url, headers={"User-Agent": f"biomimicry-vault/1.0 (mailto:{MAILTO})"})
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read().decode("utf-8"))

    def citers(doi):
        recs = get(f"https://api.opencitations.net/index/v1/citations/{doi}")
        raw = [r.get("citing", "") for r in recs]
        dropped = sum(1 for c in raw if not c.strip())      # the blank-key trap
        return {c.strip().lower() for c in raw if c.strip()}, len(recs), dropped

    print("\n=== Crossref (mailto=%s) ===" % MAILTO)
    for k, d in ANCHORS.items():
        m = get(f"https://api.crossref.org/works/{urllib.parse.quote(d)}"
                f"?mailto={MAILTO}")["message"]
        print(f"{k:18s} {m['DOI']:38s} refby={m.get('is-referenced-by-count')}"
              f"  {(m.get('title') or [''])[0][:60]}")

    print("\n=== OpenCitations citer sets ===")
    sets = {}
    for k, d in ANCHORS.items():
        s, n, drop = citers(d)
        sets[k] = s
        print(f"{k:18s} records={n:6d} dropped_empty={drop:3d} unique={len(s):6d}")

    print("\n=== pairings (E is the UNION FLOOR: |A||B|/(|A|+|B|-O)) ===")
    for a, b in PAIRS:
        A, B = sets[a], sets[b]
        O = A & B
        E = len(A) * len(B) / (len(A) + len(B) - len(O))
        print(f"{a:16s} x {b:18s} |A|={len(A):6d} |B|={len(B):6d} O={len(O):4d} "
              f"E_floor={E:8.1f} |A||B|={len(A)*len(B):.3e}")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
