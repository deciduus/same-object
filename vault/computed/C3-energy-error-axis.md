---
name: C3-energy-error-axis
type: computed
---

# The energy-per-error axis

> Every substrate that stores, transmits or checks information, on one kT-normalized axis.

## The identity

- Landauer (1961): E >= kT ln2 per bit erased = **0.693 kT**
- Shannon (1948): E_b >= N_0 ln2, and for thermal noise N_0 = kT -> **0.693 kT**
- Error correction (2015): dW >= kT ln(eta_eq/eta) -> **2.303 kT per decade**

**Stated honestly:** each half is sourced but no single source states the composition. It is
our derivation. Caveat: N_0 = kT is the *matched* noise density of a passive resistor; real
receivers carry a noise figure F >= 1.

## Selected values

| Substrate | x Landauer |
|---|---|
| LDPC code vs the Shannon limit | **1.001** |
| one ATP hydrolysis | 27.6 |
| DNA replication, per bit | 165 |
| superconducting logic incl. cooling | 1.4e3 |
| **cortical synapse** | **6.6e5** |
| **CMOS 32-bit add, 45 nm** | **1.09e6** |
| neuromorphic, per synaptic event | 9.1e9 |

**Two clusters, 2.7 unoccupied orders between.** What separates them is not chemistry:
near-floor systems are single-molecule, slow and local; far systems are fast and move charge
across structures thousands of times larger than the bit. A neuron and a transistor are on the
same side of that line, within a factor of 1.7.

**Reliability does not explain the gap.** kT ln(1/eps) at eps = 1e-15 gives ~50x. The observed
gap is 1e6 — under a third of it in log terms.

## Correction carried

An earlier version claimed no cross-substrate energy-per-bit axis existed. **False** — see
[[G8-energy-per-bit-axis]]. The combination here may still be novel; the absence claim was
not.
