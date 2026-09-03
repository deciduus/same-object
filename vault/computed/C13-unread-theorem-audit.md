---
name: C13-unread-theorem-audit
type: computed
---

# The unread-theorem audit

> **Four of four survive citation intersection. None turned out in active use like
> [[kedem-caplan]].** The headline pattern — *the unifying theorem already exists, unread in an
> adjacent field* — is hardened, not damaged further. Load-bearing caveat: this is the
> citation-intersection standard, not the full-text re-read that caught kedem-caplan. A
> well-covered co-citation zero is what these four have; the deeper "is the concept used under
> another name" question was answered only for [[kirkwood-disposable-soma]] (via journal-field
> inspection of every citer) and remains formally open for the others.

Method: for each theorem, take a discrete anchor on each side, pull the citer set of each anchor,
and intersect the two sets — a work citing **both** anchors is a co-citer, the event whose absence
is the claim. OpenCitations COCI supplied citer sets (DOI-to-DOI); Crossref supplied reference
lists where a per-citer scan was run. Every count below carries the endpoint that produced it.
kedem-caplan's lesson is honoured: an intersection is inspected, not just counted.

All fetches 2026-09-03. Cross-source note: OpenCitations' `/citation-count/` endpoint returned a
constant bogus `1` all session and was **not** used; the `/citations/` list endpoint (parsed by
regex) and Crossref were used instead. Crossref `select=reference` returns HTTP 400 and was
dropped in favour of full-record pulls.

---

## [[kirkwood-disposable-soma]] — VERDICT: STILL-UNREAD (strong)

**Claim:** Kirkwood's disposable-soma theory (1977) is unread by self-healing-materials research.

- **Biology anchor:** Kirkwood, *Evolution of ageing*, Nature 270:301 (1977), **10.1038/270301a0**.
  A discrete, correctly-dated foundational paper — the ideal anchor shape.
- **Self-healing side:** citer union of four materials anchors, pulled from
  `opencitations.net/index/coci/api/v1/citations/<doi>`:
  White 2001 *Autonomic healing of polymer composites* (10.1038/35057232, 1990 citers),
  Blaiszik 2010 *Self-Healing Polymers and Composites* (10.1146/annurev-matsci-070909-104532,
  1364), Yang & Urban 2013 *Self-healing polymeric materials* (10.1039/c3cs60109a, 1362), plus
  10.1002/adma.200904102 (1003) — which on inspection is *Photoswitches: From Molecules to
  Materials*, **not** the self-healing review intended; it dilutes but cannot falsify a zero, and
  the other three (~4700 citers) are core self-healing. **Unique citers: 5075.**

**Intersection:** for each of the 5075 self-healing citers, its Crossref reference list was pulled
and scanned for the Kirkwood DOI (and for unstructured `Kirkwood` + 1977/79/97/99). Result:

    DONE total=5075  haveRefs=5042  noRefs=29  err=4  hitcount=0

- **Intersection size: 0.**
- **Coverage: 5042/5075 = 99.4%** of self-healing citers had DOI-bearing reference lists.
- **Reverse check:** the 1280 Europe PMC citers of Kirkwood
  (`/MED/593350/citations`, hitCount 1280) span **368 distinct journals; zero** are
  materials/polymer/composite/engineering/reliability venues. Every "heal" in their titles is
  *healthspan/healthy aging*, never material self-healing.

A well-covered zero from both directions. This is the strongest of the four, and it vindicates
[[C10-healing-curve-fit]]'s use of the disposable-soma frame: the frame is genuinely unimported.

---

## [[availability-formula]] — VERDICT: STILL-UNREAD (intersection 0; engineering anchor small)

**Claim:** reliability's availability A = MTBF/(MTBF+MTTR) is unread by the biology re-deriving it
as photosystem repair steady state k_rep/(k_rep+k_damage).

This theorem has **no discrete anchor on the biology side in the vault** — [[C1-availability-living-tissue]]
is the project's own computation, not a cited paper — so a proxy pair was built. "availability"
is in the homograph register (reliability engineering vs light/nutrient availability), so string
queries are invalid; only intersection is admissible.

- **Reliability-availability anchors:** IEEE Trans. Reliability, *Availability, MTBF and MTTR for
  Repairable M out of N System* (10.1109/tr.1981.5221134, **49** citers) + RAMS 2004
  *Steady-state availability estimation* (10.1109/rams.2004.1285427, 5). **Union 54.**
- **Photosystem-repair anchors:** Aro, Virgin & Andersson 1993, *Photoinhibition of Photosystem II:
  inactivation, protein damage and turnover*, BBA-Bioenergetics (10.1016/0005-2728(93)90134-2,
  **2155** citers) + Tikkanen 2013 *PSII photoinhibition-repair cycle protects PSI*
  (10.1016/j.bbabio.2013.10.001, 343).

**Intersection (OpenCitations set overlap): 0** for both biology anchors against the availability
union. No work cites both a reliability-availability paper and the canonical PSII repair papers.

- **Coverage:** biology side excellent (2155-citer anchor). **Engineering side is the weak point:**
  the availability formula is textbook, so no single heavily-cited anchor exists; 54 citers is a
  thin base. The zero is therefore "no PSII-repair paper reaches this availability paper, and none
  of its 54 citers reach PSII" — a genuine discrete-anchor zero, but a bigger reliability anchor
  would harden it. Discovery cross-check: Europe PMC `"mean time between failures" AND photosystem`
  = **0 hits**; the relaxed query returns only biological-sense "availability" (drought/nutrient),
  the homograph exactly as predicted.

---

## [[stress-strength-interference]] — VERDICT: STILL-UNREAD (and two vault numbers corrected)

**Claim:** stress-strength interference (reliability) is unread by the biology that re-derived it,
Alexander 1997.

- **Biology anchor:** Alexander, *A theory of mixed chains applied to safety factors in biological
  systems*, J. Theor. Biol. (1997), **10.1006/jtbi.1996.0270**.
- **Engineering anchors:** four discrete stress-strength-interference reliability papers —
  10.1109/24.589940, 10.1109/tr.2008.2006289, 10.1109/24.488933 (IEEE Trans. Reliability),
  10.1016/0026-2714(96)00011-x (Microelectronics Reliability). **Union of citers: 84.**

**Intersection (OpenCitations set overlap): 0.** None of Alexander's citers cite any of the four
interference anchors.

- **Coverage / reverse direction:** Alexander's **39** citers (OpenCitations) were listed in full;
  every one is a comparative-biomechanics / evolutionary-physiology venue (J. Exp. Biol., J.
  Physiol., PNAS, eLife, ICB, Evolution, TREE, Oikos). **Zero reliability-engineering citers.** So
  neither literature cites the other. Consistent with [[G19-safety-factor-derived-twice]], which
  individually inspected the citing set.

**Vault-number corrections (both were string-based):**
- "**46 citations, every one comparative biomechanics**" — the *all-biomechanics* half holds, but
  the count is wrong. Real counts: Crossref `is-referenced-by-count` **36**; OpenCitations **39**;
  Europe PMC **28**. There is no source returning 46. Treat 46 as stale.
- "**753 works** [in interference theory], not one biological" — unverifiable and almost certainly a
  Boolean-relaxation artifact per METHOD §11. `query.bibliographic="stress-strength interference
  reliability"` on Crossref returns **1,806,063** (relaxed matching). There is no discrete
  753-work interference corpus; the *directional* claim (interference literature does not cite
  Alexander) is what the intersection actually supports.

---

## [[hill-number-multifunctionality]] — VERDICT: STILL-UNREAD (used as pipeline positive control)

Run as the brief's positive control: [[G6-multifunctionality]] already intersected to 0, so if my
pipeline reported this as *well-connected*, my pipeline would be wrong.

- **Ecology anchor:** Byrnes et al. 2014, *Investigating the relationship between biodiversity and
  ecosystem multifunctionality*, Methods Ecol. Evol. (10.1111/2041-210x.12143, **844** citers).
- **Engineering anchors:** 10.1088/2399-7532/ab8e95 (*Multifunctional Materials* residual-performance
  paper, 18 citers), 10.1016/j.compstruct.2011.06.008 (45), 10.1177/0021998311410497 (J. Composite
  Materials, 55).

| Intersection (OpenCitations set overlap) | Result |
|---|---|
| Byrnes 2014 × residual-performance metric | **0** |
| Byrnes 2014 × Composite Structures | **0** |
| Byrnes 2014 × J. Composite Materials | **0** |
| **Positive control:** Byrnes 2014 × Jost 2006 (diversity formalism, 10.1111/j.2006.0030-1299.14714.x) | **7** |

The pipeline returns **nonzero** where genuine metric-import contact exists (Byrnes×Jost — G6
reports 17 via a reference-list scan; the 7 here is the COCI set-overlap floor, same sign) and
**zero** where G6 claims a gap. **Pipeline validated.** Hill-number stays STILL-UNREAD.

---

## What this does to the headline pattern

[[kedem-caplan]] remains the one entry that collapsed — and the reason it collapsed is instructive:
it was catalogued on a bare **2-co-citer** count, the weakest possible instrument, and a full-text
re-read found the *result* in structural use. The four theorems audited here were never resting on
a 2-co-citer count; they now rest on **citation intersection with inspected sets**, the same
standard that [[G25-proofreading-coding]] and [[G6-multifunctionality]] survived. On that standard,
**all four hold**:

- Kirkwood: a 99.4%-covered zero across 5075 self-healing citers, corroborated by 368 citing
  journals containing no materials venue. As strong as this project's evidence gets.
- Availability and stress-strength: discrete-anchor intersections of 0, with excellent coverage on
  the biology side and thin (but real) anchors on the engineering side.
- Hill-number: 0, and it doubled as proof the instrument still fires on true contact.

**So the pattern is hardened.** kedem-caplan was a genuine wound, but it was a wound to a *counting*
claim; re-testing its four neighbours on the *intersection* standard did not reproduce the failure.
**The honest residual:** none of these four has yet had the [[reading-not-counting|full-text
re-read]] that caught kedem-caplan — the step that distinguishes "literatures do not touch" from
"the concept is used under another name." Citation intersection cannot see a Morrison-&-Osterle-style
parallel derivation that never cites the anchor. Kirkwood's journal-field sweep is the closest
approximation and it too came back clean. The four are hardened to the level of G6/G25, not beyond
it. The next move on any of them is a full-text pass over the near-miss papers, not another count.
