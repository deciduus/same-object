#!/usr/bin/env python3
"""c28_roc.py — the O2 biosignature detection as a diagnostic test.

Backs vault/computed/C28-biosignature-roc.md. Pure arithmetic on Bayes' rule; the
only inputs are sensitivity, specificity and prevalence, and the point of the note
is that the astrobiology literature publishes NO value for any of the three.

    "disease"  = life present on the observed planet
    "test +"   = O2 detected above the instrument's stated threshold
    sens       = P(O2 detected | life)          = 1 - false-negative rate
    spec       = P(no O2 detected | no life)    = 1 - false-positive rate
    prev       = P(life) over the observed sample  (the base rate; UNKNOWN)

Run:  python c28_roc.py        (from vault/_scripts/)
"""

# ILLUSTRATIVE INPUTS, NOT MEASURED ONES.  No specificity for the O2 test is
# published, and the note's abiotic-source section shows that none is currently
# estimable from the literature: the enumeration of false-positive mechanisms is a
# list, not a rate over a reference population.  The SPECS grid below is a span
# chosen to display the arithmetic, and every number this script prints inherits
# that status.  The note's real OUTPUT is the inversion in spec_required(): given
# an assumed prevalence, what specificity would a believable detection need.
# The callout was corrected 2026-09-05 (audit 06) for describing this grid as a
# range "the field's own false-positive enumeration can plausibly support".
PREVS = [1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3, 0.5]
SPECS = [0.900, 0.950, 0.990, 0.999]


def ppv(prev, sens, spec):
    """Positive predictive value = P(life | O2 detected)."""
    tp = sens * prev
    fp = (1.0 - spec) * (1.0 - prev)
    return tp / (tp + fp)


def npv(prev, sens, spec):
    """Negative predictive value = P(no life | no O2)."""
    tn = spec * (1.0 - prev)
    fn = (1.0 - sens) * prev
    return tn / (tn + fn)


def lr_pos(sens, spec):
    """Positive likelihood ratio; the Bayes factor the field already computes."""
    return sens / (1.0 - spec)


def prev_breakeven(sens, spec):
    """Prevalence at which PPV = 0.5 — detection as likely true as false."""
    return (1.0 - spec) / (sens + 1.0 - spec)


def spec_required(prev, sens, target=0.5):
    """Specificity needed to reach PPV = target at a given prevalence."""
    # target = sens*prev / (sens*prev + (1-spec)(1-prev))
    return 1.0 - (sens * prev * (1.0 - target)) / (target * (1.0 - prev))


def table(sens):
    print(f"\n## PPV table, sensitivity = {sens:.2f}")
    print("| prevalence | " + " | ".join(f"spec={s:.3f}" for s in SPECS) + " |")
    print("|---|" + "---|" * len(SPECS))
    for p in PREVS:
        row = " | ".join(f"{ppv(p, sens, s):.3f}" for s in SPECS)
        print(f"| {p:g} | {row} |")


def main():
    print("# C28 — O2 detection as a diagnostic test")
    print("\nLR+ (= sens/(1-spec)), the Bayes factor the field already reports:")
    for s in SPECS:
        print(f"  spec={s:.3f}: LR+ = {lr_pos(1.0, s):8.1f} (sens=1.0)"
              f" | {lr_pos(0.5, s):8.1f} (sens=0.5)")

    for sens in (1.0, 0.5):
        table(sens)

    print("\n## Break-even prevalence (PPV = 0.5)")
    print("| specificity | sens=1.0 | sens=0.5 |")
    print("|---|---|---|")
    for s in SPECS:
        print(f"| {s:.3f} | {prev_breakeven(1.0, s):.5f} | "
              f"{prev_breakeven(0.5, s):.5f} |")

    print("\n## Specificity required for PPV = 0.5 and PPV = 0.9 (sens = 1.0)")
    print("| prevalence | spec for PPV=0.5 | spec for PPV=0.9 |")
    print("|---|---|---|")
    for p in PREVS:
        print(f"| {p:g} | {spec_required(p, 1.0, 0.5):.6f} | "
              f"{spec_required(p, 1.0, 0.9):.6f} |")

    print("\n## NPV, for the false-negative leg Meadows 2018 also enumerates")
    print("| prevalence | sens=0.5, spec=0.99 | sens=0.1, spec=0.99 |")
    print("|---|---|---|")
    for p in PREVS:
        print(f"| {p:g} | {npv(p, 0.5, 0.99):.4f} | {npv(p, 0.1, 0.99):.4f} |")


if __name__ == "__main__":
    main()
