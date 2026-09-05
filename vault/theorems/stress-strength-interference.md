---
name: stress-strength-interference
type: theorem
era: 1967
---

# Stress-strength interference

> Load distribution, strength distribution, probability of interference in a weakest-link series system. **Biology re-derived it from scratch in 1997, thirty years late.**

Alexander's *A Theory of Mixed Chains Applied to Safety Factors in Biological Systems* (1997,
*J. Theor. Biol.*, `10.1006/jtbi.1996.0270`) has **36–46 citations depending on provider, every
one comparative biomechanics.** Zero crossings either way. See
[[G19-safety-factor-derived-twice]], which carries the full provider table.

| Provider | N | Date |
|---|---|---|
| OpenAlex (`cited_by_count`, W2144457609) | **46** | 2026-09-05 |
| OpenCitations (`/index/v1/citations/`, counted) | **40** | 2026-09-05 |
| Crossref (`is-referenced-by-count`) | **36** | 2026-09-05 |
| Europe PMC | 28 | 2026-09-03 |

**Citation-tested and confirmed still-unread: [[C13-unread-theorem-audit]].** Alexander 1997
citers intersected against four IEEE / *Microelectronics Reliability* interference papers (84
citers): **0 overlap.**

> **One number here was wrong; the other correction was itself wrong, and is reversed.**
> The "753 works" figure for the engineering literature was a **string artifact** — relaxed
> matching returns ~1.8M — and stays withdrawn.
> **But "46 citations" was not stale.** It is simply the **OpenAlex** count, which still returns
> **46** on 2026-09-05, alongside OpenCitations 40 and Crossref 36. Calling it stale mistook a
> provider disagreement for an error. Neither changes the finding: the intersection is a
> measured, inspected zero, and all providers agree the citing set is comparative biomechanics.

**And biology stated the logic verbatim without the citation.** Diamond (2002, *J Physiol*):

> Safety factors serve to minimize the overlap zone between the low tail of capacity
> distributions and the high tail of load distributions.

He also lists *safety factors of series systems* as unsolved — which reliability engineering
solved decades earlier.

Computed out in [[C2-probabilistic-safety-factors]], where the **remodeling objection
inverted the trade**: engineering's fixed-at-manufacture assumption is the zero-gain limit of
a control loop biology runs with feedback.
