---
id: G12
name: G12-latch-fatigue
type: gap
standing: narrowed
evidence: full-text-read
contact-surface: 3
crosses: data
crosses-rank: 5
topology: direct
mediator: 
borrows-from: []
lends-to: []
mutual-with: []
computed-in: []
uses-move: ["[[M3-separate-timescales]]"]
rests-on: ["[[LaMSA-latch]]"]
tags: [node/gap, crosses/data, evidence/full-text-read, standing/narrowed]
last-checked: 2026-09-03
note: "Held on full-text read. The 2023 JEB LaMSA review names re-usability and defers it; the click-beetle latch paper measures one cycle on dried specimens."
---

# No cycles-to-failure number for a biological latch

**STANDING: NARROWED** · evidence: full-text-read · contact surface: 3 · last checked 2026-09-03

> Latch-mediated spring actuation beats muscle power density by orders of magnitude by
> decoupling slow loading from fast release. The springs and geometry are well modelled.
> **The latch is explicitly the least-characterized element in the field.**

## What happened to this entry

**Withdrawn, then restored and narrowed.** The withdrawal cited Dirks, Parle & Taylor,
*Fatigue of insect cuticle*, J. Exp. Biol. 216:1924 (2013), which publishes genuine S-N
curves — cycles to failure against applied cyclic stress — for locust hind tibiae and wings.
Tibiae failed at **100,000 cycles at 76% of ultimate strength**; wings at 46%.

**But a spring is not a latch.** The original claim was specifically about the latch — the
microsecond, low-friction, repeatably-releasing contact that the field itself names as its
least-characterized component. Fatigue data for the *material the leg is made of* does not
answer it.

The withdrawing agent flagged this itself: *"nobody has cycled a latch contact surface under
strike loading specifically."* That caveat was recorded and then overridden by the verdict
label — the failure mode that produced [[relationship-description]].

## Contact surface

Three relevant papers, all on cuticle as a **material**:

- Dirks, Parle & Taylor (2013) — S-N curves, locust hind tibiae and wings
- Parle et al. — wing cross-veins as a fatigue-mitigation strategy
- O'Neill et al. — repair of microdamage from cyclic loading in insect cuticle

The locust hind leg *is* the canonical latch system, so the material is right and the
component is wrong.

## What crosses

**Data, for the adjacent object.** Fatigue engineering's S-N methodology has reached insect
cuticle. It has not reached the latch contact.

## What is specifically absent

**Cycles-to-failure for a latch contact surface under strike loading.** Not the spring.
Not the cuticle. The interface that stores and releases.

Supporting: repeated trap-jaw ant strikes show **no decline in peak velocity** — fatigue
appears in the muscle motor, not in the spring or latch. So the latch outlasts the
measurement, and nobody has run it to failure.

## The full-text re-read: held, in the strongest available form

**The field names the property and explicitly defers it.** From the 2023 *J. Exp. Biol.* LaMSA
review ([jeb245262](https://journals.biologists.com/jeb/article/226/Suppl_1/jeb245262/306259/)),
read in full:

> "The intriguing distinctions among single-use, re-useable, re-settable LaMSA mechanisms are
> considered elsewhere"

Checked ABSENT in that review: cycles sustained before failure, wear patterns on latch contact
surfaces, latch fatigue, degradation over repeated use. **A named absence in a named source is
the strongest form this evidence can take** — better than a zero count, because it is the field
itself saying so.

**The most latch-specific paper measures one cycle.** The 2019 click-beetle latch paper
([jeb196683](https://journals.biologists.com/jeb/article/222/12/jeb196683/20388/)), read in
full, measures hinge morphology, mechanics and force during a **single** latching cycle on
**desiccated** specimens — a limitation the authors flag themselves. Checked ABSENT: wear,
damage, repeated use, cycle counts, durability.

A deliberate synonym hunt was run — wear, tribology, abrasion, contact fatigue, damage
accumulation, durability, reusability, resettability, end-of-life — precisely the failure mode
that damaged six of the previous eight entries. It found nothing on the biology side.

**And engineering has the formalism.** Mechanical-latch cycle life is routine; there is a US
patent titled *Method to detect end-of-life in latches*. So this is [[one-way-borrowing]]
waiting to happen: engineering has both the number and the method, biology has neither applied
to a latch contact.

### One live risk, not closed

Bolmin et al., *PNAS* 118:e2014569118 (2021) is reported in secondary sources to say click
beetles click repeatedly "without apparent external damage." **UNVERIFIED** — PNAS 403s and the
paper is not open access in Europe PMC. If that sentence is real it is a *qualitative* durability
statement, which would **soften but not overturn** the claim: "no apparent damage" is not a
cycles-to-failure number.

Also **UNVERIFIED**: the trap-jaw ant claim below carries no URL and was not re-checked.

## What would change it

A cyclic test rig on a latch geometry. This is the [[LaMSA-latch]] entry's practical arm and
one of the few things in this project reachable with a 3D printer and a high-speed camera.

## Homograph warning

`"LaMSA"` alone is contaminated — it returns CaMKII text and a **sociolinguistics** corpus
(Mary/merry mergers). `"click beetle"` returns **pheromone trap** literature. See
[[homographs]]. Use `"latch-mediated spring actuation"` in full.
