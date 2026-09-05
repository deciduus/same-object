# Referee report

**Manuscript:** *Charnov's marginal value theorem is the Gittins index of the outside option, and its restless extension predicts giving-up density rises with patch regrowth*
**Referee:** 2
**Date:** 2026-09-05
**Basis:** `papers/charnov-gittins/paper.md` and `papers/charnov-gittins/refs.bib` only. No repository material, no vault notes, no scripts, no external sources were consulted. Every algebraic step and every number reported below was recomputed from the manuscript's own definitions.

---

## 1. Summary of the claims

The paper argues that Charnov's marginal value theorem is not analogous to, but literally is, an application of the Gittins index rule: if travel time is written into an "habitat arm" as a zero-reward prefix of length $\tau$ followed by the gain stream $g'$, then that arm's undiscounted index is $\sup_t g(t)/(\tau+t)=R^*$, while a deterministic concave patch has index $g'(t)$, so the index rule reproduces $g'(t^*)=R^*$; the identity is claimed to survive discounting (yielding a discounted MVT) and to fail in exactly three places the bandit literature already names — restlessness, switching costs, non-stationarity.

The restless case is then carried across: for a patch with active dynamics $\dot x=-\lambda x$, reward $\lambda x$, and passive regrowth $\dot x=r(1-x)$, the Whittle index is derived as $W(x)=\lambda x^2-r(1-x)^2$, the problem is shown indexable without parameter restriction, and implicit differentiation gives $d\mathrm{GUD}/dr>0$ — faster-regrowing patches should be abandoned at higher standing crop, a between-patch-type contrast that MVT predicts to be zero.

Finally the paper presents a bibliometric argument that the two literatures have not met (5 of 1,013 Gittins citers also cite Charnov, against 225 of 1,013 for a Gittins × Auer 2002 control, control ratio 62.5) and nominates Kadmon & Shmida (1992) with Kadmon (1992) as a system that parameterises but does not run the test.

---

## 2. Verification

I recomputed each item independently from the manuscript's stated definitions.

**2.1 Index of the current patch, $\nu_0(t)=g'(t)$ (Eq. 1).** **Correct.** The forward chord slope $(g(t+s)-g(t))/s$ is decreasing in $s$ for concave $g$, so the supremum sits at $s\to0^+$ and equals $g'(t)$ wherever $g$ is differentiable. The claim that $\delta$ drops out is also **correct**: for $\delta>0$ the ratio is $\int_0^s \delta e^{-\delta u}g'(t+u)\,du/(1-e^{-\delta s})$, a genuine probability-weighted average of $g'$ over $[t,t+s]$ with a strictly positive normalised weight, hence $\le g'(t)$ with equality only as $s\to0^+$. The dominated-convergence remark is correct but trivial, as the paper itself concedes.

**2.2 The MVT–Gittins identity (Theorem, Eq. 2).** **Correct as arithmetic, imprecise as a theorem.** For $\sigma=\tau+t$, $\int_\tau^{\tau+t}g'(u-\tau)\,du=g(t)-g(0)=g(t)$ and the denominator is $\tau+t$; stopping at $\sigma\le\tau$ gives ratio $0$, which is dominated whenever $g$ is non-trivial. So $\nu_0(\text{habitat})=\sup_{t\ge0}g(t)/(\tau+t)$. The deduction $\text{leave}\iff g'(t)\le R^*$ then follows from (1). Two gaps in the statement are recorded under Major issues (M1, M2): attainment of the supremum is asserted, not hypothesised, and the index rule invoked is the undiscounted one, whose validity is not the Gittins theorem the paper cites.

**2.3 The discounted index (Eq. 3).** **Correct.** With $\sigma=\tau+t$, $\mathbb{E}\int_0^\sigma e^{-\delta u}du=(1-e^{-\delta(\tau+t)})/\delta$ and the numerator is $\int_\tau^{\tau+t}e^{-\delta u}g'(u-\tau)du=e^{-\delta\tau}\int_0^t e^{-\delta v}g'(v)dv$. Their ratio is (3) exactly.

**2.4 The $\delta\to0$ limit of (3).** **Correct.** Numerator $\to \delta g(t)$, denominator $\to\delta(\tau+t)$ to first order; the ratio $\to g(t)/(\tau+t)$ uniformly on compacts. The renewal–reward route the paper prefers is also correct and is the better argument.

**2.5 "Stronger discounting makes the forager stay longer."** **Correct, verified numerically.** With $g(t)=1-e^{-\lambda t}$, $\lambda=1$, $\tau=1$: undiscounted $R^*=\max_t(1-e^{-t})/(1+t)=0.3162$ at $t^*\approx1.15$; at $\delta=1$, (3) maximises to $0.190$ near $t=2$. The outside index falls, so the departure threshold falls and residence rises. The claim that the *mechanism* is the $e^{-\delta\tau}$ prefactor is not established — the denominator $1-e^{-\delta(\tau+t)}<\delta(\tau+t)$ pushes the other way, and the net sign is a computation, not a factor you can read off. State it as a computed result or prove it.

**2.6 The three failure boundaries.** **Two correct, one over-claimed.** Restlessness: correct, Gittins' theorem assumes arms frozen when passive. Non-stationarity: correct as stated. Switching costs: the verdict "no optimal index policy of any kind exists" is stronger than Banks & Sundaram support and the manuscript's own footnote admits the primary paper was not obtained. Index policies under switching costs are known to be optimal in restricted settings; the correct claim is that no *Gittins-type* index policy is optimal in general. Downgrade the wording. **Partially cannot verify** — the primary source was not read by the authors and, under my instructions, not by me.

**2.7 The Whittle index $W(x)=\lambda x^2-r(1-x)^2$ (Eq. 4).** **Correct, and I reproduced it by the paper's own route.** With $A=\lambda a$, $B=r(1-a)$, the singular-arc active fraction is $u^*=B/(A+B)$ and $\rho(a)=u^*\lambda a+(1-u^*)\nu=A(B+\nu)/(A+B)$, as stated. Setting $\partial\rho/\partial a=0$ with $\nu$ held fixed and cancelling $r>0$ gives, after clearing denominators, $r+\nu-2ra-\lambda a^2+ra^2=0$, i.e. $\nu=\lambda a^2-r(1-a)^2$. That is (4) exactly.

The self-consistency cross-check is also **correct**: solving $\lambda x-V'[\lambda x+r(1-x)]=\lambda x^2-r(1-x)^2$ gives $V'=(1-x)[\lambda x+r(1-x)]/[\lambda x+r(1-x)]=1-x$. Note this is a fixed-point verification, not an independent derivation, and the manuscript should say so rather than present it as corroboration. I also verified that the HJB gain at the indifference state is $\rho=\lambda a-\lambda a(1-a)=\lambda a^2$, consistent with $\rho(a)=Aa$ above.

**2.8 Indexability.** **Correct.** $W'(x)=2\lambda x+2r(1-x)>0$ on $[0,1]$ for $\lambda,r>0$ (endpoints $2r$ and $2\lambda$), so $W:[0,1]\to[-r,\lambda]$ is a continuous strictly increasing bijection and $P(\nu)=[0,W^{-1}(\nu)]$ is nested and sweeps $\emptyset\to[0,1]$. Indexable unconditionally, as claimed.

**2.9 The two limits.** **Correct.** $r\to0$ with $V'=1-x$ retained gives $W=\lambda x^2\ne g'$; $r\to0$ with $V'\equiv0$ imposed gives $W=\lambda x=g'(t)$ and recovers (2). $r\to\infty$ gives $W(x)\to-\infty$ for $x<1$ and $W(1)=\lambda$. The numerical check reproduces: at $r/\lambda=10^6$ and $\nu=0.09$, $(1-x)^2=(x^2-0.09)/r$ solves to $x=0.999047$, matching the stated $0.99905$, and $t^*=\ln(1/0.999047)=9.53\times10^{-4}$, matching $9.5\times10^{-4}$.

The *justification* for the second limit is weak, however. Setting $V'\equiv0$ "by fiat" is not a limit of the model — it is a different model. See M3.

**2.10 GUD$(\rho)$ (Eq. 5).** **Correct.** $x^2-\rho(1-x)^2=u_0^2$ rearranges to $(1-\rho)x^2+2\rho x-(\rho+u_0^2)=0$, whose relevant root is $[-\rho+\sqrt{\rho^2+(1-\rho)(\rho+u_0^2)}]/(1-\rho)$, and the discriminant simplifies to $\rho+u_0^2(1-\rho)$ as printed. At $\rho=1$ the quadratic degenerates to $2x=1+u_0^2$, giving the stated removable-singularity value.

**2.11 $d\mathrm{GUD}/dr$ (Eq. 6).** **Correct.** $\partial W/\partial r=-(1-x)^2$ and $\partial W/\partial x=2\lambda x+2r(1-x)$, so implicit differentiation of $W(x)=\nu$ gives $dx/dr=(1-x)^2/[2(\lambda x+r(1-x))]>0$. The small-$r$ coefficient is $(1-u_0)^2/(2\lambda u_0)=0.49/0.6=0.8167$, matching the printed $0.817$.

**2.12 Table 1, all four rows including the corrected residence column.** **Correct in every cell.** Recomputed at $\lambda=1$, $\tau=1$, $u_0=0.30$, $\nu=0.09$, $t^*_{\mathrm{MVT}}=\ln(1/0.3)=1.20397$:

| $r\tau$ | GUD (mine) | ratio | $x_{\rm arr}$ | $t^*$ | $t^*/t^*_{\rm MVT}$ |
|---|---|---|---|---|---|
| 0.05 | 0.334845 | 1.1161 | 0.367286 | 0.092477 | 0.0768 |
| 0.20 | 0.401920 | 1.3397 | 0.510352 | 0.238913 | 0.1984 |
| 1.00 | 0.545000 | 1.8167 | 0.832615 | 0.423744 | 0.3520 |
| 10.00 | 0.774278 | 2.5809 | 0.999990 | 0.255840 | 0.2125 |

Every printed value agrees to the displayed precision. The non-monotonicity claim also checks out: at $r\tau=2$ I get GUD $=0.617973$, $x_{\rm arr}=0.948298$, $t^*=0.428183$, ratio $0.35564$ — the stated peak of $0.356$ near $r\tau=2$.

**One number in the surrounding prose is wrong.** The text says the old $x_{\rm arr}=1$ convention "overstated the ratio by up to a factor of 3.8". Factor 3.8 is the $r\tau=0.2$ row: $\ln(1/0.40192)/1.20397=0.75704$ against $0.19844$, ratio $3.815$. But the $r\tau=0.05$ row is far worse: $\ln(1/0.334845)/1.20397=0.90878$ against $0.07683$, a factor of **11.8**, and the factor diverges as $r\to0$ (old ratio $\to1$, new ratio $\to0$). "Up to a factor of 3.8" is therefore false over the table's own range. **Error.** Either say "by a factor of 3.8 at $r\tau=0.2$ and without bound as $r\to0$", or drop the number.

**2.13 The network-simulation range $[1.06,1.27]$.** **Cannot verify, and as reported it is not well defined.** The simulation is not described: the manuscript gives no number of patch types, no values of $r_{\rm fast}$ and $r_{\rm slow}$, no $\lambda$, no $\tau$, no visitation protocol, no horizon, no replication or Monte Carlo error. Worse, the quantity is ambiguous. Table 1's ratio column is GUD$(r)$/GUD$_{\rm MVT}$ — a single type against the MVT baseline — whereas the simulation reports a *fast/slow between-type* ratio. These are different quantities, but §3.6 sets them side by side ("the same anchor returns 1.271") as though the $1.271$ were commensurable with Table 1's $1.340$ at $r\tau=0.2$. Either they are the same quantity, in which case $1.271\ne1.340$ is an unexplained discrepancy requiring explanation, or they are not, in which case the sentence is misleading. Since the headline falsifiable statement is *powered on this interval*, this is not a presentational matter. See M5.

**2.14 The saturating-renewal restriction.** **The manuscript contradicts itself, and the Limitations version is the correct one.** §4 states: "The derivation runs the same way with linear renewal, but (4) changes. The *sign* of (6) survives; the coefficients in Table 1 do not." Limitations item 5 states: "under linear renewal the Whittle index degenerates to a step function and the regrowth effect vanishes or reverses". These cannot both be true, and the sign claim is what the paper's only falsifiable prediction rests on.

I recomputed the linear case. With passive $\dot x=c$ (constant, capped) and the same active dynamics, the singular-arc active fraction is $u^*=c/(\lambda a+c)$ and $\rho(a)=\lambda a(c+\nu)/(\lambda a+c)$. Then
$$\frac{\partial\rho}{\partial a}=\frac{\lambda c(c+\nu)}{(\lambda a+c)^2}>0$$
for all $a$ whenever $c>0$ and $c+\nu>0$: there is **no interior stationary point**, $\rho$ is monotone in $a$, and the singular-arc construction that produced (4) has no solution. The structure genuinely degenerates, exactly as Limitations item 5 says and exactly contrary to §4. **Error, and a load-bearing one** — §4 is the paragraph that tells the reader the *Anchusa* system still supports the sign prediction.

**2.15 The citation arithmetic.** Numerically **correct throughout**; the displayed identity is **written backwards**.

- $N$ floors: $1013+5424-5=6432$ ✓; $1013+3906-225=4694$ ✓.
- $E_{\rm gap}=1013\cdot5424/6432=854.2$ ✓; $E_{\rm ctrl}=1013\cdot3906/4694=842.9$ ✓.
- $O/E$: $5/854.2=0.00585$ ✓; $225/842.9=0.2669$ ✓.
- Percentages: $5/1013=0.494\%$ ✓; $225/1013=22.21\%$ ✓; ratio $45$ ✓.
- $N=10^6$: $E=5.494$, $O/E=0.910$ ✓.
- Control ratio $(225/3906)/(5/5424)=0.0576042/0.00092183=62.49$ ✓.

But the displayed equation asserts
$$\frac{(O/E)_{\rm gap}}{(O/E)_{\rm ctrl}}=\frac{O_{\rm ctrl}/|B_{\rm ctrl}|}{O_{\rm gap}/|B_{\rm gap}|}=62.5 .$$
Since $(O/E)_i=O_i N/(|A||B_i|)$, the left-hand side equals $(O_{\rm gap}/|B_{\rm gap}|)/(O_{\rm ctrl}/|B_{\rm ctrl}|)=1/62.5=0.016$. The middle expression is the *reciprocal* of the left-hand one. The intended object — an isolation factor of 62.5, control over gap — is fine; the equation as printed is false. **Error.** Fix by writing $(O/E)_{\rm ctrl}/(O/E)_{\rm gap}$ on the left.

---

## 3. Major issues

**M1. The theorem does not state the hypotheses it uses.** The Theorem asserts the supremum in (2) is "attained at Charnov's optimal residence time $t^*$". Attainment is a hypothesis, not a conclusion. For $g(t)=ct$ — concave, $g(0)=0$, everything else satisfied — $\sup_t ct/(\tau+t)=c$ is not attained at any finite $t$, and there is no $t^*$. The standard sufficient condition ($g$ strictly concave, increasing, $g'(0^+)>\lim_{t\to\infty}g(t)/(\tau+t)$, or $g$ bounded with $g'(\infty)=0$) must appear in the statement. Similarly, "concave" is used where "concave, increasing, differentiable on $(0,\infty)$, with $g'$ strictly decreasing" is what the argument needs — the last for the departure time to be unique. A theorem in *J. Appl. Prob.* will not pass in this form.

**M2. The zero-reward-prefix step: non-revisitability is sufficient but demonstrably not necessary, and the paper's central "licence" is therefore mis-identified.** The manuscript's boxed claim is that absorbing $\tau$ into the outside arm is legitimate *iff* a departed patch is never revisited, and §2.3 leans on this as the diagnosis of Kilpatrick et al.'s error. But in the standard bandit formulation a departed patch is *frozen*, not deleted, and its index remains $g'(t_{\rm dep})\le R^*$ for ever. Under concavity a frozen patch can therefore never re-attain top index, so revisits never occur on the optimal path regardless of whether they are permitted. The correct statement is weaker and cleaner: what is required is that $\tau$ is incurred **once per arm activation** and is a property of the arm's own reward stream, which holds whenever the forager never resumes a previously-suspended patch. Non-revisitability is one way to guarantee that; concavity plus frozen passive arms is another, and it is the one the model already has.

This matters twice over. First, the "iff" is false as written and should be "if". Second, and more seriously, it undercuts §3.5's second limit, where the paper *reinstates* $V'\ne0$ precisely because revisits are allowed — so the two sections use incompatible accounts of what revisitability does. Reconcile them explicitly.

There is a related structural point the paper misses and would be strengthened by. In steady state *every* patch is reached through a travel interval, so every arm has the same $\tau$-prefixed stream; the "current patch" is simply a habitat arm that has already been played for $\tau+t$, whose residual index is $\sup_s(g(t+s)-g(t))/s=g'(t)$. On that reading the identity is one arm type and one index computation rather than two, the asymmetry between "patch arm" and "habitat arm" disappears, and the zero-reward-prefix step needs no special pleading at all. I recommend restructuring §2 this way.

**M3. The reduction to MVT is achieved by imposing the answer.** §3.5's second limit sets $V'\equiv0$ "by fiat" and then observes that $W(x)=\lambda x$ recovers (2). But $V'\equiv0$ is not a limit of the restless model — it is the statement that resource left behind is worthless, which is the MVT assumption. So the "reduction passes" is close to circular: the paper assumes what distinguishes MVT from the restless model and then recovers MVT. The honest version derives $V'\to0$ as the terminal value of a patch that will never be revisited, from the dynamic programme with an absorbing departure, rather than asserting it. As written, the sentence "a stronger result than an unconditional pass would have been" is not earned.

**M4. The "no source states the identity" claim is not adequately supported by the paper's own evidence, because the control is not a control for what is being claimed.** Auer 2002 is a bandit paper sharing Gittins' field, venue culture, and vocabulary; Charnov 1976 is a behavioural-ecology paper. The gap/control contrast therefore confounds two effects — "these two *ideas* have not been connected" and "these two *fields* do not cite each other" — and only the first is the paper's thesis. A 62.5-fold ratio against a same-field control tells the reader mostly that Gittins' citers are operations researchers. The evidence would be far stronger with a *cross-field* control at comparable distance: e.g. Gittins × (a well-known ecology or animal-behaviour paper of similar citation volume that no one claims is connected to bandits), or the symmetric intersection Charnov × (some canonical OR paper). Without that, §5 establishes distance, not neglect. Since the title's "have not been connected" is a novelty claim and §5 is its only quantitative support, this must be addressed.

Second, the base of 1,013 is used for every percentage yet the paper itself reports that Crossref (986), OpenCitations (1,026) and OpenAlex (1,544) disagree, that the provider for the 1,013 enumeration "was not recorded", and that OpenAlex is 52% larger. An enumeration whose provider is unknown cannot anchor a headline number. Either re-run the enumeration with the provider recorded, or report the control ratio across all three bases and show it is stable.

**M5. The falsifiable prediction is powered on an interval that the paper does not derive, describe, or reconcile.** §3.6 asks a field test to be powered for a between-type GUD ratio in $[1.06,1.27]$ at $r\tau=0.2$. That interval comes entirely from an undescribed 20-patch simulation (see 2.13), its endpoints are two different choices of a free parameter $\nu$ rather than a confidence interval, and its upper endpoint disagrees with Table 1's $1.340$ at the same $r\tau$ and the same nominal anchor without comment. An experimentalist reading this cannot compute a sample size. Either specify the simulation completely (parameters, protocol, replicate count, dispersion) and explain the $1.271$ vs $1.340$ gap, or drop the interval and state the prediction as a closed-form function of $(r_{\rm fast},r_{\rm slow},\lambda,\tau,\nu)$ that a reader can evaluate for their own system.

**M6. §4 and Limitations item 5 contradict each other on whether the sign survives linear renewal, and §4 is wrong.** See 2.14 for the computation. The consequence is not cosmetic: §4 is the section that names a real biological system, and it currently tells the reader that the sign prediction transfers to *Anchusa* while Limitations tells the reader it does not. Resolve in favour of Limitations, move the degeneracy result into the main text with the derivation, and rewrite §4's caveat. A reader who stops before Limitations will otherwise carry away a false claim about the one empirical system the paper names.

**M7. The restless extension's negative simulation result is disclosed only in Limitations, and the paper's framing does not survive contact with it.** The Whittle policy loses 13.3% of intake at the pre-registered anchor and 0.5% under each policy's own optimal threshold, "in every cell of the sweep". This is not fatal to the extension's interest — a signed comparative static can be worth publishing even from a policy that does not out-earn the incumbent, and Whittle indices carry no optimality guarantee in the $M=1$, $\alpha\to0$ regime anyway (Limitations item 3, which is well done and honest). But it *is* fatal to reading the extension as a normative claim about foragers, and the abstract currently invites exactly that reading: "Faster-regrowing patches should be abandoned at a *higher* giving-up density" is a normative sentence for a policy that earns less. The result belongs in §3, adjacent to the prediction, with the word "should" replaced or qualified. A referee should not learn the central negative result on page 12.

Relatedly, the 0.5% figure is the informative one and deserves more than a clause: if two policies differ by 0.5% under their own optimal thresholds, the empirical contest between them is essentially unpowered in any realistic field study, which bears directly on whether the proposed experiment is worth running.

**M8. Is §5 a legitimate part of a theory paper?** Partly. A short novelty statement with the intersection count and the named near-misses (Kilpatrick et al., Lejarraga & Hertwig, Griebling et al.) is legitimate and useful. A full bibliometric null model with expected counts, denominator sensitivity, and a derived control-ratio statistic is a different paper in a different genre, and in a theory venue it reads as advocacy for the paper's own novelty — an argument the authors cannot make disinterestedly. Compress §5 to roughly a third of its length in the main text, keeping the numbers and the five inspected works, and move the null model, the $N$-sensitivity argument, and the control-ratio derivation to an appendix. This also removes the awkwardness of a Theorem section and a scientometrics section carrying equal weight.

**M9. Under-hedging in the abstract, over-hedging in Limitations, and they do not agree.** The abstract asserts "We show they are the same object" flatly; Limitations concludes "The claim is 'appears unwritten', not 'is unwritten'" and lists four unread full texts including the one document known to co-cite all three sources. The abstract also omits both the negative simulation and the linear-renewal restriction. The title's declarative "is the Gittins index" is defensible for the mathematics; the *novelty* half needs the same hedge in the abstract that it gets on page 12.

---

## 4. Minor issues

1. **Undiscounted index undefined.** $\nu_0$ is used throughout but never defined; §1.2 defines only $\nu_\delta$. Add one line defining $\nu_0$ as the $\delta=0$ ratio (equivalently the renewal–reward ratio), and note that the "index theorem" invoked at $\delta=0$ is the average-reward statement, not Gittins' discounted theorem.
2. **Three orphan bibliography entries.** `green1984`, `srivastava2013` and `scully2025` appear in `refs.bib` with full verification notes but are cited nowhere in the manuscript. `scully2025` in particular (240 occurrences of "Gittins", zero of "Charnov") is direct evidence for the novelty claim and should be cited in §5, not left dangling.
3. **Two works cited in prose with no bibliography entry.** "Bhat, Bénichou & Redner (2018, *Phys. Rev. E*)" and "Lejarraga & Hertwig (2016)" are named in §5 as read-in-full evidence but have no `refs.bib` entries and no DOIs. These carry evidential weight; they need entries at the same verification standard as the rest.
4. **Markdown table breakage.** The §5 table header `| | $|A|$ | $|B|$ | ...` contains unescaped pipes inside math, which will not render as a table. Use `\lvert A\rvert` or escape.
5. **Table 1 caption is too thin for reproducibility.** It gives $\lambda$, $\lambda\tau$, $G_{\max}$, $u_0$ and names a script, but not $\nu=0.09$ explicitly, and not the fact that $x_{\rm arr}$ assumes round-robin symmetric visitation (which is buried in Limitations item 6). Both belong in the caption.
6. **Abstract length.** Roughly 230 words, and it carries a bibliometric statistic ("62.5", "run-time enumeration 2026-09-03") that no abstract needs. *J. Appl. Prob.* will want it under 150. Cut the citation numbers from the abstract entirely.
7. **Notation collisions.** $r$ is the regrowth rate in §3 and the reward-rate function $r(u)$ in the Theorem statement in §2.2. $\rho$ is the average-reward gain in §3.3 and the ratio $r/\lambda$ in §3.6. $\nu$ is both the generic Whittle subsidy and the specific anchored equilibrium value. All three should be disambiguated.
8. **$V$ never defined as a relative value function** before use, and the average-reward HJB is written down without stating the ergodicity conditions under which $(\rho,V)$ exists.
9. **Limitations item 6 contains main-text material.** "The discrete-time index may differ at $O(\Delta t)$, and this was not checked" is a statement about whether (4) is the right object, not a modelling caveat; it belongs with the derivation in §3.3. Conversely, Limitations item 1 (the homogeneous-habitat degeneracy) is already fully stated in §3.6 and can be reduced to a cross-reference.
10. **The Acknowledgements cite an unnamed language model's review as corroboration** ("independently recomputed the index, its derivative, and Table 1, and confirmed them"). Confirmation by an unnamed model is not evidence and should not be offered as such; keep the acknowledgement, drop the claim of independent verification.
11. **"Two remarks are load-bearing" (§2.1)** — the concave-hull remark is genuinely load-bearing and deserves its own short lemma, since it is reused in §2.6 (non-concave gain curves) and §2.5 (delayed-reward patches under discounting). At present the reader must reconstruct it three times.
12. **The exploration-bonus inequality** $\nu(x)\ge\mathbb{E}[\text{immediate rate}]$ is stated in §2.6 as though established and then disclosed as unproved on page 12. Flag it as a conjecture at the point of first use.
13. `kilpatrick2020` is a preprint with a well-documented note explaining that no journal version exists; the in-text treatment should say "preprint" once so the reader is not left wondering about the venue of the paper the argument leans on hardest.

---

## 5. Recommendation

**Major revision.**

The mathematical core is sound. I recomputed every derivation and every number I could reach from the manuscript alone, and with three exceptions they are right: the chord-slope index, the habitat-arm index, the discounted index and its limit, the Whittle index by the singular-arc route, its self-consistency check, unconditional indexability, the closed-form GUD, the sign of $d\mathrm{GUD}/dr$, the small-$r$ coefficient, all sixteen non-trivial cells of the corrected Table 1, the non-monotone peak at $r\tau\approx2$, and the entire citation arithmetic. That is an unusually clean set of numbers, and the corrected residence column in particular is right where a naive treatment would be wrong. The central observation — that MVT's apparent self-reference is the index's, and dissolves once $R^*$ is recognised as a property of a different arm — is worth publishing, and the failure-boundary argument (the correspondence breaks precisely where the bandit literature already knows the index theorem breaks) is the strongest structural evidence in the paper.

But three errors and one framing failure block acceptance in the present form. The linear-renewal contradiction (M6) is the worst: §4 tells the reader the sign survives, my own computation says the singular arc has no interior stationary point under constant renewal, and the paper's own Limitations agrees with me — so the manuscript currently makes a false claim about the one biological system it names. The control-ratio identity (2.15) is printed as its own reciprocal. The "factor of 3.8" (2.12) is wrong over the table's own range. And the novelty argument (M4) rests on a same-field control that measures field distance rather than conceptual neglect, on a citer base whose provider was not recorded and which three providers put between 986 and 1,544. Add to these the theorem's missing hypotheses (M1), the mis-identified licence for the zero-reward prefix (M2), and the fact that the negative simulation result appears only in Limitations (M7), and the revision required is substantial rather than editorial. None of it, however, threatens the identity itself, which is why this is major revision and not rejection. I would want to see the revised manuscript.

---

## 6. Questions for the author

1. **On M2.** In the standard formulation a departed patch is frozen, not removed, and its index stays at $g'(t_{\rm dep})\le R^*$ for ever — so under concavity no optimal path ever revisits, whether or not revisiting is permitted. Why, then, is non-revisitability necessary rather than merely sufficient for the zero-reward-prefix step? And if it is only sufficient, how do you reconcile that with §3.5, where revisitability is what makes $V'\ne0$ and breaks the MVT reduction?

2. **On M6 / 2.14.** I find that under linear renewal $\dot x=c$ the singular-arc gain is $\rho(a)=\lambda a(c+\nu)/(\lambda a+c)$ with $\partial\rho/\partial a=\lambda c(c+\nu)/(\lambda a+c)^2>0$ everywhere, so no interior stationary point exists and (4) has no linear-renewal analogue. This contradicts §4's "the sign of (6) survives" and agrees with Limitations item 5. Which is the paper's position, and what is the derivation behind whichever one you keep? Given that *Anchusa* is the only real system named, what remains testable there?

3. **On M4 / M5.** Two parts. (a) What does the control ratio become against a *cross-field* control — a canonical ecology paper of comparable citation volume that no one claims is connected to bandit theory — and does the 62.5 survive? Without that comparison, how do you separate "these ideas have not met" from "these fields do not cite each other"? (b) For the 20-patch simulation: what are $r_{\rm fast}$, $r_{\rm slow}$, $\lambda$, $\tau$, the visitation protocol and the replicate count, and why does the same-anchor between-type ratio come out at $1.271$ when the closed form at $r\tau=0.2$ gives $1.340$?

---

## Author response

**Date:** 2026-09-05. **Revision:** referee 2, round 1.

We thank the referee for recomputing every derivation and every number reachable from the
manuscript alone. Three errors were found and all three are corrected. **No number in Table 1
changed** — the referee's independent recomputation of all sixteen non-trivial cells agrees
with ours, and we have left the table exactly as printed. Below, each item names the change
and quotes the sentence now in the manuscript.

### 1. ERROR 1 — linear renewal (§2.14, M6, Question 2)

**Accepted in full. The referee is right and §4 was wrong.** We reproduce the referee's
computation and it is C48's, which the vault has carried since 2026-09-05: with passive
`ẋ = c` the singular-arc active fraction is `u* = c/(λa + c)`, the gain is
`ρ(a) = λa(c+ν)/(λa+c)`, and `∂ρ/∂a = λc(c+ν)/(λa+c)² > 0` for every `a` whenever `c > 0` and
`ν > −c`. The `a`-dependence of the forgone regrowth — `r(1−a)` in the saturating model — is
what supplied the competing term that produced an interior stationary point; under linear
renewal the forgone regrowth is `c` regardless of standing crop, that term does not exist, and
the maximiser is the boundary `a = 1`.

The deleted sentence was: *"The derivation runs the same way with linear renewal, but (4)
changes. The sign of (6) survives; the coefficients in Table 1 do not."* §4 now reads, in
part:

> **The derivation does not run the same way, and the prediction does not transfer.** [...]
> There is **no interior stationary point** [...] The maximiser is the boundary `a = 1`, and
> the index degenerates to a step function, `W(x) = −c` on `(0,1)`, `W(1) = λ`, flat on the
> interior and carrying neither state nor `c` information. There is therefore **no analogue of
> (4), no analogue of (6), and no regrowth effect**: `dGUD/dc = 0` from the index alone, and
> with travel made explicit the self-consistent cycle gives
> `GUD*(c) = max{a_MVT(λτ), 1 − cτ}`, whose derivative is `−τ` below the kink and `0` above —
> never positive, where (6) requires strictly positive. [...] This is Limitations item 5; an
> earlier draft of this section claimed that the sign of (6) survives linear renewal, and that
> claim was wrong.

The full derivation is now in the main text with the caveat, not only in Limitations, so a
reader who stops before page 12 cannot carry away the false claim. The contradiction the
referee identified is resolved in favour of Limitations, as recommended.

**On the vault.** `C25-whittle-foraging` §5 already carried the boundary condition correctly
(*"the comparative static reverses sign: `dGUD/dc ≤ 0`, against `dGUD/dr > 0` here"*), and
`C48-kadmon-regrowth-test` is the derivation. The bug existed in `paper.md` only, so no vault
note required editing for this item. That is recorded in the README.

### 2. ERROR 2 — the control-ratio identity (§2.15)

**Accepted. The equation was printed as its own reciprocal.** The algebra, in full. With
`E_i = |A|·|B_i|/N`,

```
(O/E)_i = O_i / ( |A|·|B_i| / N ) = O_i · N / ( |A|·|B_i| ).
```

Forming the ratio of the control's `O/E` to the gap's, the common factors `N` and `|A|` cancel:

```
(O/E)_ctrl     O_ctrl·N/(|A|·|B_ctrl|)     O_ctrl / |B_ctrl|     225/3,906     0.0576042
---------- =  ------------------------  =  -----------------  =  ---------  =  ---------  =  62.49
(O/E)_gap      O_gap ·N/(|A|·|B_gap| )     O_gap  / |B_gap|      5/5,424       0.00092183
```

The manuscript had printed `(O/E)_gap / (O/E)_ctrl` on the left of that same right-hand side,
which equals `1/62.5 = 0.016`. The intended object — an isolation factor of 62.5, control over
gap — was never in doubt and no number changes. The display now reads:

> Since `(O/E)_i = O_i·N/(|A||B_i|)`, the isolation factor is the control's `O/E` divided by
> the gap's: `(O/E)_ctrl / (O/E)_gap = (O_ctrl/|B_ctrl|)/(O_gap/|B_gap|) = (225/3,906)/(5/5,424)
> = 0.0576/0.000922 = 62.5.` (Written the other way up,
> `(O/E)_gap/(O/E)_ctrl = 1/62.5 = 0.016`; an earlier draft printed the left-hand side in that
> orientation against the right-hand side in this one.)

### 3. ERROR 3 — "up to a factor of 3.8" (§2.12)

**Accepted; the referee's 11.8 reproduces.** `ln(1/0.334845)/1.20397 = 0.90878` against the
corrected `0.07683` is a factor of 11.8 at `rτ = 0.05`, and as `r → 0` the old convention's
ratio tends to 1 while the corrected one tends to 0, so the factor is unbounded. "Up to a
factor of 3.8" was false over the table's own range. The sentence now reads:

> The resulting overstatement is row-dependent, not bounded by a single factor: it is $3.8$ at
> $r\tau=0.2$, $11.8$ at $r\tau=0.05$, and diverges as $r\to0$, since the old convention's
> ratio tends to $1$ while the corrected one tends to $0$.

### 4. The simulation (§2.13, M5, Question 3b)

**Accepted.** A new subsection of §3, *"The simulation behind that interval"*, states the
setup completely: complete graph, `N = 20` (10 fast, 10 slow), one forager, uniform
`τ = 1/λ`, `λ = 1`, `G_max = 1`, baseline `r_fast·τ = 0.2` and `r_slow·τ = 0.02`, `dt = 0.01`
with exact exponential flow per step, burn-in 200 time units discarded and 1,000 scored, 20
seeds none dropped, Student-`t` 95% intervals across seeds, destination chosen by `argmax` of
the policy's own criterion at the arrival state `x_j^arr = 1 − (1−x_j)e^{−r_j τ}`, one habitat
scalar per forager. Endpoints: `ν = λu₀² = 0.09` gives `1.2708 ± 0.0002`; `ν` learned by a
damped fixed point on the realised long-run intake rate converges to `0.273` and gives
`1.0600 ± 0.0002`. The manuscript now says plainly that `[1.06, 1.27]` is **a calibration
range, not a confidence interval**, with Monte Carlo error `±0.0002` on each endpoint, and
names the usable design window `r_fast·τ ∈ [0.2, 1]` — at `r_fast·τ = 10` the simulated
forager never visits the slow type and the ratio is undefined. Script:
`vault/_scripts/c45_whittle_sim.py`.

**Why 1.271 and not 1.340.** The referee is right that the two quantities were set side by
side without being commensurable, and the explanation is in the denominator, not in the
network. Table 1's 1.340 is `GUD(rτ=0.2)/GUD_MVT` with `GUD_MVT = u₀ = 0.300`, an `r = 0`
baseline. The simulation's 1.271 is a *between-type* ratio whose slow type regrows at
`r_slow·τ = 0.02`, not 0, and therefore departs at `GUD_slow = 0.3138` — within 0.8% of the
closed form's own small-`r` expansion `0.300 + 0.817×0.02 = 0.3163`. The fast type departs at
`0.3987` against the closed form's `0.4019`, again 0.8%. Against the same `r = 0` baseline the
simulated fast value gives `0.3987/0.300 = 1.329` against Table 1's `1.340`. So the closed form
survives the network; what changes is the baseline the ratio is taken against. That paragraph
is now in the manuscript.

We flag the limit of this answer, since the referee asked for an explanation and not a
plausible one. The residual 0.8% at each level is attributed **in the source note** (C45 §5,
§8) to two causes: the `dt` overshoot — every threshold fires at the first step past the
crossing, worth ≤ 0.5% on any GUD here — and the finite-`N` visit imbalance, 87% of departures
being from fast patches at the baseline. Neither was isolated, and a `dt`-halving check is
named there as not run and is still not run. We state the attribution as the note's and mark
it as not separately verified rather than presenting it as established.

### 5. Theorem hypotheses (M1)

**Accepted.** The hypotheses now appear in the statement, and the failure case is named:

> **Theorem.** *Let patches be statistically identical, with deterministic gain function $g$
> satisfying $g(0)=0$, increasing, differentiable on $(0,\infty)$, and strictly concave, so
> that $g'$ is strictly decreasing; let travel time be $\tau>0$ at zero reward in a stationary
> habitat; and assume the supremum in (2) below is attained at some finite $t^{*}$.*

followed immediately by:

> Attainment is a hypothesis, not a conclusion. It is implied by either of two standard
> conditions: $g$ bounded with $g'(t)\to0$ as $t\to\infty$, or, more generally, $g$ concave and
> increasing with $g'(0^{+})>\lim_{t\to\infty} g(t)/(\tau+t)$. Both fail for $g(t)=ct$, which
> is concave with $g(0)=0$ and for which $\sup_{t}ct/(\tau+t)=c$ is approached but never
> attained: there is then no $t^{*}$ and the forager never leaves. Strict decrease of $g'$ is
> what makes the departure time unique.

The clause *"the supremum being attained at Charnov's optimal residence time"* is replaced by
*"attained at Charnov's optimal residence time"*, so the conclusion no longer asserts what the
hypothesis now supplies. The referee's minor point that "concave" was doing more work than it
states is taken with it: strict concavity is now hypothesised, and its role — uniqueness of the
departure time — is named.

### 6. Non-revisitability (M2, Question 1) — restructuring adopted, and it verifies

**We adopt option (a), the referee's restructuring, and we have done the check the brief
asked for. It goes through.** The argument, as we verified it:

- Every patch is reached through travel, so in steady state every arm carries the same
  `τ`-prefixed stream. A **fresh** arm's index is `R*` by (2). The **occupied** patch is such
  an arm already played for `τ + t`, whose residual index is `sup_s [g(t+s) − g(t)]/s = g'(t)`
  by (1). One arm type, one index computation; the patch-arm/habitat-arm asymmetry disappears.
- A **frozen** (departed) arm's index is `g'(t_dep)`, and `g'(t_dep) ≤ R*` **by construction of
  departure** — the forager left precisely when the index fell to the outside index. Freezing
  holds it there for ever.
- A fresh arm's index is `R*`. So the fresh arm always weakly wins. Because `g'` is strictly
  decreasing, resuming the frozen arm for any positive duration `s > 0` returns
  `[g(t_dep+s) − g(t_dep)]/s < g'(t_dep) ≤ R*`, strictly, where the fresh arm returns exactly
  `R*`. Revisiting is therefore never strictly optimal.

**The one gap, stated rather than hidden.** At the departure instant `g'(t_dep) = R*` exactly,
so the frozen arm and a fresh arm tie at that point. The conclusion is "never *strictly*
better to revisit", not "strictly worse to revisit". Nothing downstream uses the strict form.
A second, milder point in the same direction: the model as written charges no travel to resume
a frozen arm, whereas a physical forager would pay `τ` again — that only widens the margin, so
the argument is conservative.

Consequently the boxed claim is weakened from "iff" to "if", and the licence is restated as the
condition actually used:

> Absorbing travel time into the outside arm is legitimate **if $\tau$ is incurred once per
> activation of an arm and is a property of that arm's own reward stream.** Never revisiting a
> departed patch is one sufficient condition. It is not necessary, and in the present model it
> is not an assumption at all: it is a consequence.

**Reconciliation with §3.5, which the referee asked for explicitly.** The correct diagnosis of
the switching-cost break is not "revisits are permitted" but "**the arm you return to is not
frozen at its departure index**". That distinction is exactly what separates §2 from §3. With
`r = 0` the arm is frozen and the argument above applies. With any `r > 0` the arm is restless:
a departed patch regrows, its index recovers, it can re-attain the top, and revisits genuinely
occur — which is why `V' = 1 − x ≠ 0` there. The manuscript now says so in both places, and
§3.5 makes the non-commutation explicit: `lim_{r→0⁺} W(x) = λx²` differs from the frozen-arm
value `λx`, and the gap `λx(1−x)` is precisely the value of a revisit that the restless model
permits and the frozen model forbids. The two sections no longer use incompatible accounts of
revisitability; they use one account and differ in whether the arm is frozen.

The §2 preamble's assumption list and the abstract are updated to match ("a departed patch is
frozen rather than deleted, in the standard bandit sense"). This is recorded in the vault as
`C5-charnov-gittins` **§13, "Referee-2 restatement"**; the proof in C5 §2–§4 is untouched, per
the principle that a restatement is not a re-derivation.

### 7. `V' ≡ 0` "by fiat" (M3)

**Accepted; the circularity is removed.** §3.5's second limit no longer asserts `V' ≡ 0`. It
derives it from the item-6 argument:

> **$r=0$, arms frozen.** At $r=0$ a departed patch neither regrows nor recovers its index, so
> the frozen-arm argument of Section 2.3 applies verbatim: its index stays at
> $g'(t_{\mathrm{dep}})\le R^{*}$ for ever, no optimal path resumes it, and the resource left
> behind is never harvested by this forager. Its shadow price is therefore $0$ as an *output*
> of the dynamic programme with an absorbing departure --- $V'\equiv0$ is derived from the
> departure structure, not imposed.

The claim that this is "a stronger result than an unconditional pass would have been" is
deleted; the sentence now says only that the reduction passes because of the structural
condition of §2.3, and that the first limit shows what happens when that condition is removed.

### 8. The Auer control (M4)

**Accepted as a limitation; the number is kept and its interpretation is marked.** §5 now
carries, immediately after the control's citation record:

> This is a **same-field** control: Auer et al. is a bandit paper sharing Gittins' venue
> culture and vocabulary, whereas Charnov 1976 is behavioural ecology, so the ratio below
> measures field distance as well as conceptual neglect, and should be read as an upper bound
> on the latter. No cross-field control of comparable citation volume has been run; we keep
> the number and mark its interpretation.

We have not run the cross-field control in this round (see Question 3a below).

### 9. Abstract (M7, M9)

**Accepted.** The abstract previously carried the normative "should" with no mention of the
negative simulation. It now states the result in the abstract itself:

> ...indexable unconditionally, and $dGUD/dr>0$: faster-regrowing patches are predicted to be
> left at a *higher* giving-up density. The claim is a signed comparative static and not one of
> superiority --- run forward in a 20-patch network the Whittle policy *loses* intake to
> MVT-with-regrowth, by $13.3\%$ at the pre-registered anchor and $0.5\%$ when each policy is
> given its own rate-optimal threshold --- and it is specific to saturating renewal: under
> linear renewal the index degenerates to a step function and the effect does not survive.

"should be abandoned" becomes "are predicted to be left", and the saturating-renewal
restriction is now in the abstract as well as in Limitations. The referee's point that the
0.5% figure is the informative one is taken: it is now the second number in the abstract's
clause rather than a subordinate clause on page 12.

### 10. The referee's three questions

**Q1 (on M2): why is non-revisitability necessary rather than merely sufficient, and how is
that reconciled with §3.5?**

It is not necessary, and we no longer claim it is. See item 6: we adopt the referee's frozen-arm
formulation, verify it, and state its one gap (the tie at the departure instant). The
reconciliation with §3.5 is that freezing, not deletion, is the operative condition — and
freezing is exactly what the restless model removes. At `r = 0` the arm is frozen and revisits
are never strictly optimal, so `V' = 0`; at any `r > 0` the arm's index recovers, revisits do
occur, and `V' = 1 − x`. The two `r → 0` branches do not commute, and the manuscript now says
so, with the gap `λx(1−x)` identified as the value of the revisit.

**Q2 (on M6): which is the paper's position, what is the derivation, and what remains testable
in *Anchusa*?**

Limitations item 5 is the paper's position; §4 was wrong and is corrected. The derivation is
the referee's own and is now printed in §4 (see item 1). On *Anchusa*: **nothing of this
prediction remains testable there.** Kadmon (1992) measured linear renewal; under linear
renewal `dGUD/dc ≤ 0` while (6) requires `> 0`, so the system cannot confirm the prediction
whichever way the data fall — a null there is uninformative rather than a falsification. What
the Kadmon pair still does, and it is the only thing §4 now claims for it, is **parameterise**:
it is the rare case where renewal rate and the departure decision are measured on one
plant–pollinator system, which is what makes it a template for the design. The test itself
requires an array with saturating refill by construction; a linear-refill arm in the same
array then makes a negative control, so that a null on the linear arm checks the apparatus
while a null on the saturating arm is a real falsification. §4 says this.

**Q3a (on M4): what does the control ratio become against a cross-field control, and does 62.5
survive?**

**We do not know, and we have not run it.** We regard this as the referee's strongest
unaddressed point and we decline to guess at the answer. What we have done is stop the
manuscript from claiming more than the measurement supports: §5 now states that Auer is a
same-field control, that the ratio therefore measures field distance as well as conceptual
neglect, and that 62.5 should be read as an **upper bound** on isolation rather than a measure
of it. The cross-field control the referee specifies — Gittins × a canonical ecology paper of
comparable citation volume that nobody claims is bandit-related, or the symmetric Charnov ×
canonical-OR intersection — is the right design and it is recorded as open work in
`vault/PENDING-log-REV2.md`. We would rather report the ratio with its interpretation marked
than report a cross-field number we have not fetched.

The referee's second point under M4 is likewise recorded and likewise not closed in this round:
the provider of the 1,013 enumeration was not recorded, and Crossref (986), OpenCitations
(1,026) and OpenAlex (1,544) disagree for the same DOI. Re-running the enumeration with the
provider recorded, or reporting the control ratio across all three bases, is staged as open
work. The manuscript already discloses all four figures and says the percentages are not
recomputed against the other three; we have not extended that disclosure into a claim of
stability we cannot yet support.

**Q3b (on M5): the simulation's parameters and protocol, and why 1.271 against 1.340?**

Answered in full at item 4 above. Parameters and protocol are now in the manuscript; the
1.271/1.340 difference is a difference of denominator — the simulation's slow type regrows at
`r_slow·τ = 0.02` rather than 0, so its GUD is 0.3138 and not 0.300 — and against a common
`r = 0` baseline the simulated fast value gives 1.329 against Table 1's 1.340, an 0.8%
agreement. The residual 0.8% is attributed by the source note to `dt` overshoot and finite-`N`
visit imbalance; we report that attribution as the note's and mark it as not separately
verified.

### Items accepted but not acted on in this round

We record these as accepted rather than argued, so the referee can see they are not
overlooked. They are staged in `vault/PENDING-log-REV2.md`: downgrading the Banks & Sundaram
switching-cost verdict to "no *Gittins-type* index policy is optimal in general" (§2.6);
defining `ν₀` explicitly and noting that the `δ = 0` index theorem is the average-reward
statement (Minor 1); citing `scully2025` in §5 and adding `refs.bib` entries for Bhat et al.
(2018) and Lejarraga & Hertwig (2016) (Minor 2, 3); escaping the pipes in the §5 table
(Minor 4); putting `ν = 0.09` and the round-robin visitation assumption in the Table 1 caption
(Minor 5); shortening the abstract and removing its bibliometric statistics (Minor 6);
disambiguating `r`, `ρ` and `ν` (Minor 7); stating the ergodicity conditions for `(ρ, V)`
(Minor 8); moving the `O(Δt)` remark from Limitations into §3.3 (Minor 9); dropping the
independent-verification claim from the Acknowledgements (Minor 10); giving the concave-hull
remark its own lemma (Minor 11); flagging the exploration-bonus inequality as a conjecture at
first use (Minor 12); saying "preprint" once for Kilpatrick et al. (Minor 13); and compressing
§5 with the null model moved to an appendix (M8). None of these changes a number or a result.
