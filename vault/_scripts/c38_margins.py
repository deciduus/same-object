#!/usr/bin/env python3
"""
c38_margins.py - the arithmetic behind vault/computed/C38-reserve-margin-across-species.md.

ONE QUANTITY, ONE AXIS

    margin  =  (reserve - expected draw) / expected draw       [x100 = %]
    ratio   =  reserve / expected draw                         [ = 1 + margin ]

C33 computed this for a single species - a 10-13 g parid, from Brodin, Nilsson & Nord
2017 (DOI 10.1007/s00442-017-3923-3) - and got +57.1% on a typical night, +31.0% on a
cold night, and +10.0% / -8.3% once the demand-side lever (nocturnal hypothermia) was
removed.  This script asks whether that 1.3-1.6x is a blue-tit artifact by recomputing
the SAME division for every other species and engineered system with published numbers.

NO NETWORK.  Every input is a literal transcribed from a named source whose page/table
location is recorded both here and in the note.  Nothing is fitted.  It is all division.
Rows are graded in the `grade` field:
    PRIMARY   - both numbers read off the source's own table/results text
    DERIVED   - both numbers primary, but the ratio is this script's, not the paper's
    PUBLISHED - the source itself prints the ratio (only Haase 2019 does)
    ASSUMED   - at least one input is a convention, not a measurement (human row only)

UNITS TRAP - the main place an error could hide
-----------------------------------------------
  fat        39.6 kJ/g  avian ecology convention (the family C33's source uses)
             37.0 kJ/g  whole adipose tissue, mammalian/nutrition convention
             Eberts et al. 2021 (eLife 10.7554/eLife.70062) use 37 for hummingbirds.
             The RATIO is untouched by the choice whenever reserve and draw are both
             in grams of fat - which is why the bat row is computed in grams.
  oxygen     20.1 J/mL O2   mixed diet     (used for the deer mouse, a granivore)
             19.8 J/mL O2   pure lipid     (used for the fasting hummingbird)
             The 1.5% spread between them moves no row's verdict.
  grid       PRM is capacity (MW) over peak demand, NOT energy (MWh) over energy.
             It is on this axis by analogy only.  See the note's Honesty section.

RUN
---
    python _scripts/c38_margins.py           # from vault/
"""

KJ_G_FAT_AVIAN = 39.6
KJ_G_FAT_MAMM  = 37.0
J_ML_O2_MIXED  = 20.1
J_ML_O2_LIPID  = 19.8

ROWS = []

def add(label, reserve, draw, worst, unit, lever, grade, where):
    ROWS.append(dict(label=label, reserve=reserve, draw=draw, worst=worst,
                     unit=unit, lever=lever, grade=grade, where=where))

def margin(reserve, draw):
    return (reserve - draw) / draw

# =========================================================================== #
# 1. PARID, one night - restated from C33, not recomputed.  C33 owns it.
#    Brodin, Nilsson & Nord 2017, Oecologia 185:43-54, Tables 1-2.
#    x_dusk = x_start (12 kJ, Table 2) + good-night draw (21.0 kJ) = 33.0 kJ.
# =========================================================================== #
add("Parid 10-13 g, night, hypothermia ON", 33.0, 21.0, 25.2, "kJ",
    "nocturnal hypothermia, eps=30%", "PRIMARY(C33)", "Brodin 2017 T1+T2 / C33 s4")
add("Parid 10-13 g, night, hypothermia OFF", 33.0, 30.0, 36.0, "kJ",
    "-- lever removed --", "PRIMARY(C33)", "same, C33 s4")

# =========================================================================== #
# 2. RUFOUS HUMMINGBIRD Selasphorus rufus, one autumn night.
#    Hiebert 1993, The Auk 110:787-797, DOI 10.2307/4088634.
#    "Body Mass and Torpor - Autumn": lean body mass ca. 3 g; autumn mass held
#    ~1.5 g ABOVE lean body mass.  "Seasonality of Torpor": a normothermic bird
#    consumes 661 mL O2 over a 12 h autumn night.
#    Torpor lever: Shankar et al. 2020, J. Avian Biol. 51:e02305,
#    DOI 10.1111/jav.02305 - mean hourly saving in torpor 82% of normothermic
#    cost (individual range 65-92%).
# =========================================================================== #
RUFOUS_FAT_G   = 1.5
RUFOUS_NIGHT_ML = 661.0
TORPOR_SAVE     = 0.82
TORPOR_SAVE_LO  = 0.65          # worst individual in Shankar's range
rufous_reserve = RUFOUS_FAT_G * KJ_G_FAT_AVIAN
rufous_draw    = RUFOUS_NIGHT_ML * J_ML_O2_LIPID / 1000.0
add("Rufous hummingbird, normothermic 12 h night", rufous_reserve, rufous_draw,
    rufous_draw, "kJ", "torpor available but not used", "DERIVED",
    "Hiebert 1993 Body Mass and Torpor + Seasonality of Torpor")
add("Rufous hummingbird, torpid all night (82%)", rufous_reserve,
    rufous_draw * (1 - TORPOR_SAVE), rufous_draw * (1 - TORPOR_SAVE_LO), "kJ",
    "torpor engaged", "DERIVED", "Hiebert 1993 x Shankar 2020")

# =========================================================================== #
# 3. RUBY-THROATED HUMMINGBIRD Archilochus colubris - crop reserve only.
#    Eberts, Powers & Welch 2019, Diversity 11(1):9, DOI 10.3390/d11010009.
#    Table 2 footnote: average energy content of the evening meal 2651 +- 313 J.
#    Results + Table 1: total nighttime energy expenditure over an 11 h night,
#    fed 6806 +- 405 J, fasted 7640 +- 481 J, both normothermic (video confirmed
#    no torpor on any trial).  NOTE: Table 1's column header reads "kJ" but its
#    own footnote and the Results text give J.  J is correct; kJ is a typo in
#    the published table and this script uses J.
#    This row is the CROP alone - endogenous fat was not measured - so it is a
#    strict LOWER bound on the dusk reserve, and is labelled as one.
# =========================================================================== #
HUMM_CROP_J, HUMM_FED_J, HUMM_FASTED_J = 2651.0, 6806.0, 7640.0
add("Ruby-throated hummingbird, CROP ONLY vs normothermic night",
    HUMM_CROP_J / 1000, HUMM_FED_J / 1000, HUMM_FASTED_J / 1000, "kJ",
    "torpor not used in these trials", "PRIMARY",
    "Eberts 2019 Table 1 + Table 2 footnote")
add("Ruby-throated hummingbird, CROP ONLY vs torpid night",
    HUMM_CROP_J / 1000, HUMM_FED_J * (1 - TORPOR_SAVE) / 1000,
    HUMM_FASTED_J * (1 - TORPOR_SAVE_LO) / 1000, "kJ",
    "torpor engaged", "DERIVED", "Eberts 2019 x Shankar 2020")

# =========================================================================== #
# 4. DEER MOUSE Peromyscus maniculatus.
#    Rezende, Gomes, Hayes et al. 2009, J. Exp. Biol. 212:2795-2802,
#    DOI 10.1242/jeb.032789, Table 1 - fat mass and mean VO2 measured on the
#    SAME animals in the same table, which is exactly what this axis needs and
#    almost no other pairing in this note has.
#      warm-acclimated female: fat 3.077 g, VO2mean 2.155 mL/min
#      cold-acclimated  male : fat 1.683 g, VO2mean 4.241 mL/min
#    Draw horizon = a 12 h night.
# =========================================================================== #
def mouse(fat_g, vo2_ml_min, label, lever, worst_vo2=None):
    reserve = fat_g * KJ_G_FAT_MAMM
    night   = vo2_ml_min * 60 * 12 * J_ML_O2_MIXED / 1000.0
    worst   = (worst_vo2 or vo2_ml_min) * 60 * 12 * J_ML_O2_MIXED / 1000.0
    add(label, reserve, night, worst, "kJ", lever, "DERIVED",
        "Rezende 2009 Table 1")
mouse(3.077, 2.155, "Deer mouse, warm-acclimated female, 12 h night",
      "daily torpor (facultative)", worst_vo2=4.241)
mouse(1.683, 4.241, "Deer mouse, cold-acclimated male, 12 h night",
      "daily torpor (facultative)")

# =========================================================================== #
# 5. COMMON SHREW Sorex araneus - the no-lever control.
#    Sorex is one of the few small mammals in which torpor is not part of the
#    repertoire; its winter strategy is Dehnel's phenomenon (shrinking the
#    organ, not lowering the setpoint).
#    Keicher, Voigt et al. 2017, J. Exp. Biol. 220:2834-2841,
#    DOI 10.1242/jeb.159947, Results: "the survival time of S. araneus without
#    food is 5-10 h" (attributed to Hanski 1994).  Discussion: winter subadult
#    fat turnover t50 = 2.1 h, so the animal "would have burned all fat reserves
#    within 4.2 h" - the authors' own inference, flagged as such.
#    Draw horizon = a 16 h midwinter night, the same night C33's parid faces.
# =========================================================================== #
SHREW_NIGHT_H = 16.0
for hrs, tag in ((10.0, "fasting endurance 10 h (best case)"),
                 (5.0,  "fasting endurance 5 h (worst case)"),
                 (4.2,  "all fat gone in 4.2 h (authors' inference)")):
    add(f"Common shrew, {tag}", hrs, SHREW_NIGHT_H, SHREW_NIGHT_H, "h",
        "NONE - Sorex does not use torpor", "PRIMARY", "Keicher 2017 Results/Discussion")

# =========================================================================== #
# 6. LITTLE BROWN BAT Myotis lucifugus - the extreme, and the only PUBLISHED ratio.
#    Haase, Fuller, Hranac et al. 2019, PLoS ONE 14(10):e0222311,
#    DOI 10.1371/journal.pone.0222311, open access.
#    Table 2: autumn body mass 7.61 +- 1.08 g, fat mass 2.11 +- 0.82 g (N=46).
#    Results: central-Montana winter duration 181 days.  Fig 3A: mean time to
#    total fat exhaustion in healthy bats 317.5 +- 105.5 days; >360 days in the
#    microclimate the bats actually select (4.8 C, 100% RH); 176 days at the
#    warmest/driest microclimate available.  Infected with P. destructans:
#    131.23 +- 38.40 days.
#    Cross-check: Hranac et al. 2021, Ecol. Evol. 11:11604-11614,
#    DOI 10.1002/ece3.7641, Results - pre-hibernation fat median 2.32 g against
#    a median 0.48 g required, residual 1.85 g at emergence.
# =========================================================================== #
BAT_WINTER_D = 181.0
add("Little brown bat, healthy, mean microclimate", 317.5, BAT_WINTER_D, BAT_WINTER_D,
    "d", "hibernation (TMR ~4% of BMR)", "PUBLISHED", "Haase 2019 Fig 3A")
add("Little brown bat, healthy, SELECTED roost", 360.0, BAT_WINTER_D, BAT_WINTER_D,
    "d", "hibernation + microclimate choice", "PUBLISHED", "Haase 2019 Results")
add("Little brown bat, worst microclimate available", 176.0, BAT_WINTER_D, BAT_WINTER_D,
    "d", "hibernation", "PUBLISHED", "Haase 2019 Fig 3A")
add("Little brown bat, WNS-infected", 131.23, BAT_WINTER_D, BAT_WINTER_D,
    "d", "hibernation, lever degraded by pathogen", "PUBLISHED", "Haase 2019 Fig 3A")
# independent second instrument, same species, different paper
add("Little brown bat (Hranac 2021 medians)", 2.32, 0.48, 0.48 + 1.21, "g fat",
    "hibernation", "PUBLISHED", "Hranac 2021 Results")

# =========================================================================== #
# 7. HUMAN - the sanity row, and the only ASSUMED one.
#    Reserve: a 70 kg adult carrying ~15 kg fat.  15000 g x 37 kJ/g = 555 MJ.
#    BOTH the 70 kg and the 15 kg are conventions, not a measurement from a
#    named table, which is why this row is graded ASSUMED and is not used in
#    any conclusion.  Draw: total fasting expenditure ~7 MJ/day.
#    The horizon is the argument.  Against ONE DAY the margin is absurd (+7800%)
#    and that is the point: a human is not sized to one night.  Against a 90-day
#    seasonal famine it goes negative.
#    Documented ceiling, VERIFIED at title level via Crossref 2026-09-05:
#    Stewart & Fleming 1973, Postgrad. Med. J. 49:203-209,
#    DOI 10.1136/pgmj.49.569.203, "Features of a successful therapeutic fast of
#    382 days' duration".  Full text NOT read - PMC scan blocked.
# =========================================================================== #
HUMAN_FAT_KG, HUMAN_MJ_DAY = 15.0, 7.0
human_reserve_mj = HUMAN_FAT_KG * 1000 * KJ_G_FAT_MAMM / 1000.0
add("Human adult, horizon = 1 day", human_reserve_mj, HUMAN_MJ_DAY, HUMAN_MJ_DAY,
    "MJ", "no acute lever; slow BMR downregulation", "ASSUMED", "convention")
add("Human adult, horizon = 90 d famine", human_reserve_mj, 90 * HUMAN_MJ_DAY,
    90 * HUMAN_MJ_DAY, "MJ", "BMR falls ~15-20% over weeks", "ASSUMED", "convention")

# =========================================================================== #
# 8. ENGINEERED ROWS.  NERC, 2025 Long-Term Reliability Assessment (January
#    2026), "Summary of Planning Reserve Margins and Reference Margin Levels by
#    Assessment Area", pp. 175-176.  PDF fetched from
#    https://www.nerc.com/globalassets/our-work/assessments/nerc_ltra_2025.pdf
#    on 2026-09-05 and text-extracted.  These are Reference Margin Levels: the
#    margin the area is planned TO, i.e. the design rule, not an outcome.
#    Stored as percentages directly, not as a reserve/draw pair.
# =========================================================================== #
GRID_RML = [
    ("WECC-Mexico",              7.0, 9.1),
    ("MISO, summer 2025-26",     8.1, 8.1),
    ("NPCC-Quebec",             11.9, 12.2),
    ("MRO-Manitoba Hydro",      12.0, 12.0),
    ("NPCC-New England (ICR)",  13.0, 13.4),
    ("Texas RE-ERCOT",          13.75, 13.75),
    ("MRO-SaskPower",           15.0, 15.0),
    ("SERC-East / -SE / -Central", 15.0, 15.0),
    ("NPCC-New York (RML)",     15.0, 15.0),
    ("MISO, winter 2025-26",    19.1, 19.1),
    ("MRO-SPP",                 19.0, 19.0),
    ("WECC-California",         19.2, 20.3),
    ("NPCC-Maritimes",          20.0, 20.0),
    ("NYSRC IRM 2025/26",       24.4, 24.4),
    ("PJM (IRM)",               18.6, 26.3),
]
# Battery duration convention.  4 h is the planning default for utility-scale
# Li-ion (NREL Annual Technology Baseline 2024, Utility-Scale Battery Storage:
# 4 h is the default duration).  Sized against a ~4 h evening net-peak window it
# carries no margin at all by construction.  SECONDARY - the ATB page was read
# via search summary, not fetched in full.
BATTERY_H, NETPEAK_H = 4.0, 4.0
add("Li-ion storage, 4 h duration vs 4 h net-peak window", BATTERY_H, NETPEAK_H,
    5.0, "h", "demand response (external to the asset)", "SECONDARY",
    "NREL ATB 2024, utility-scale battery storage")

# =========================================================================== #
def main():
    print(f"{'row':<58}{'reserve':>9}{'draw':>9}{'margin%':>10}{'worst%':>10}  grade")
    print("-" * 110)
    for r in ROWS:
        m = margin(r["reserve"], r["draw"]) * 100
        w = margin(r["reserve"], r["worst"]) * 100
        print(f"{r['label']:<58}{r['reserve']:>9.4g}{r['draw']:>9.4g}"
              f"{m:>+10.1f}{w:>+10.1f}  {r['grade']}")

    print("\nNERC 2025 LTRA Reference Margin Levels (design rule, pp.175-176):")
    lo = min(a for _, a, _ in GRID_RML)
    hi = max(b for _, _, b in GRID_RML)
    for name, a, b in GRID_RML:
        s = f"{a:.4g}%" if a == b else f"{a:.4g}-{b:.4g}%"
        print(f"  {name:<32}{s:>14}")
    print(f"  {'RANGE ACROSS ALL AREAS':<32}{f'{lo:.4g}-{hi:.4g}%':>14}")

    print("\nconversions actually used:")
    print(f"  rufous reserve {RUFOUS_FAT_G} g x {KJ_G_FAT_AVIAN} = "
          f"{rufous_reserve:.1f} kJ; draw {RUFOUS_NIGHT_ML} mL O2 x "
          f"{J_ML_O2_LIPID} J/mL = {rufous_draw:.2f} kJ")
    print(f"  deer mouse: VO2 x 60 x 12 h x {J_ML_O2_MIXED} J/mL")
    print(f"  human: {HUMAN_FAT_KG} kg x {KJ_G_FAT_MAMM} kJ/g = "
          f"{human_reserve_mj:.0f} MJ  [ASSUMED]")
    print(f"  bat rows are days/days and grams/grams - unit-free, no conversion")

if __name__ == "__main__":
    main()
