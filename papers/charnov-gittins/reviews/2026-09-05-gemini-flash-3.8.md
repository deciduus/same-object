# External review — Gemini Flash 3.8, 2026-09-05

Reviewer had the paper only (no vault, no context). Recomputed by hand: the current-patch index, the habitat-arm index, the discounted MVT limit, W(x) = λx² − r(1−x)², W'(x) > 0, dGUD/dr, and Table 1 (r/λ = 1: GUD 0.5450, t* 0.607). All confirmed.

## Friction points to address
- **A. Asymptotic gap.** Weber & Weiss 1990 needs a fixed active fraction α = M/N; foraging has M = 1, α → 0. Add a remark or reference on bounded suboptimality in the sparse-activation limit (fluid limits, single-server polling).
- **B. Zero-delay paradox.** §3 derives W for zero switching delay; τ re-enters only through the anchor subsidy ν = λ·GUD²_MVT. Make explicit: transit time does not alter within-type ranks (W monotone in x), but scrambles ranks across patches with heterogeneous r and modifies the global ν across a mixed network.
- **C. GUD scope.** Brown's GUD is H = C + P + MOC. State that GUD here is Charnov's sense (residual density at departure under pure rate maximisation); predation P and cost C enter as shifts in the shadow price V'.

## Polish
- §2.1: note dominated convergence for δ → 0 (integrand bounded on compact [0, s]).
- Table 1 values verified.
- Griebling 2026 handling judged appropriately cautious.

(Full review text supplied by the owner; summarised here.)

## Orchestrator vetting (Fable 5.1, 2026-09-05)
Arithmetic independently re-run: GUD(r=1) = 0.5450, t* = 0.607, W'(0.545) = 2.0 > 0, dGUD/dr = 0.1035, HJB algebra residual 0. All confirmed. Points A, B, C judged valid and actionable; A's requested reference may not exist and must be reported honestly. The reviewer's "genuinely novel" is not an independent finding (it had no literature access) and is disregarded.
