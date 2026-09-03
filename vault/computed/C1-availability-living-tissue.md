---
name: C1-availability-living-tissue
type: computed
---

# Availability of living tissue

> **Photosystem II = 0.883. Cortical bone = 0.984. A leaf is less available than a power grid.**

First availability figures ever computed for biological tissue, using
[[availability-formula]].

| System | A |
|---|---|
| Data centre, five nines | 0.99999 |
| US power grid, normal operations | 0.9998 |
| Commercial aviation dispatch | 0.995 |
| **Cortical bone** | **0.984** |
| **Trabecular bone** | **0.939** |
| **Photosystem II, 20 C** | **0.883** |
| Photosystem II, 35 C heat stress | 0.56-0.71 |
| Photosystem II, 5 C cold stress | 0.45-0.48 |

## The caveats are load-bearing

1. **Population, not unit.** A leaf holds ~1e8 photosystems; a *fraction* is down, never the
   whole. So biological A is an **expected functional fraction**, which coincides with a
   probability only when units fail **independently**. The 35 C row shows what correlated
   damage does — heat hits every unit at once and A collapses to 0.56.
2. **Down-while-repaired holds for PSII, not bone.** A resorption cavity degrades stiffness
   rather than eliminating it, so bone's 0.984 reads properly as *"1.6% of tissue volume is
   in the remodeling space"* and is a lower bound.
3. **Gut epithelium was left blank deliberately.** A 3-5 day turnover is **scheduled
   replacement before failure** — preventive maintenance, not availability. Forcing the
   formula onto it would be the merely-cute failure mode.
