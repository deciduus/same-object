#!/usr/bin/env python3
"""
c37_identity.py - provenance for C37 (LOLP = starvation probability, as a theorem).

One job: the ruin-theory parentage check.  C37 argues that grid loss-of-load
probability and small-bird starvation probability are both first-passage
(ruin) problems, and asks whether either literature cites the ruin-theory
parent.  This script intersects the citer set of the ruin-theory canon
(Asmussen & Albrecher, *Ruin Probabilities* 2nd ed., DOI 10.1142/7431) with
the citer sets of the two anchors C33/G34 already use.

    python c37_identity.py cites

Same blank-key discipline as c33_lolp.py: OpenCitations /citations/ records
with an empty or whitespace-only `citing` key are dropped BEFORE any set is
built, because the phantom "" member joins every set and inflates every
intersection by exactly 1.  The count dropped is reported.

Provider: https://api.opencitations.net/index/v1/citations/<doi>
DOIs verified against Crossref (api.crossref.org, mailto=deciduusleaf@gmail.com).
"""

import json, os, sys, time, urllib.request

MAILTO = os.environ.get("MAILTO", "deciduusleaf@gmail.com")
OC = "https://api.opencitations.net/index/v1"
UA = "biomimicry-vault/1.0 (mailto:%s)" % MAILTO
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".c37-cache")

ANCHORS = {
    "Asmussen & Albrecher 2010, Ruin Probabilities": "10.1142/7431",
    "Billinton & Allan 1996, Reliability Evaluation": "10.1007/978-1-4899-1860-4",
    "McNamara & Houston 1987, Ecology 68:1515": "10.2307/1939235",
    "Houston & McNamara 1993, Ornis Scand 24:205": "10.2307/3676736",
}


def _get(url, tries=4, timeout=300):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(3 * (i + 1))
    raise last


def citers(doi):
    os.makedirs(CACHE, exist_ok=True)
    fp = os.path.join(CACHE, doi.replace("/", "_") + ".json")
    if os.path.exists(fp):
        recs = json.load(open(fp))
    else:
        recs = json.loads(_get("%s/citations/%s" % (OC, doi)).decode("utf-8"))
        json.dump(recs, open(fp, "w"))
    blanks = sum(1 for r in recs if not str(r.get("citing", "")).strip())
    s = {str(r["citing"]).strip().lower() for r in recs if str(r.get("citing", "")).strip()}
    return s, blanks


def main():
    sets, drops = {}, 0
    for name, doi in ANCHORS.items():
        s, b = citers(doi)
        drops += b
        sets[name] = s
        print("%-46s N = %5d" % (name, len(s)))
    print("blank `citing` records dropped: %d" % drops)
    ruin = "Asmussen & Albrecher 2010, Ruin Probabilities"
    for name in ANCHORS:
        if name == ruin:
            continue
        o = sets[ruin] & sets[name]
        print("\nruin x %s -> O = %d" % (name, len(o)))
        for d in sorted(o)[:20]:
            print("   ", d)


if __name__ == "__main__":
    main()
