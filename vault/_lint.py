#!/usr/bin/env python3
"""Vault lint. Run from the vault directory: python _lint.py

Checks:
  1. every note has type, and gaps have standing + evidence
  2. standing and evidence use the closed vocabularies
  3. no retired verdict vocabulary survives in a machine field
  4. every [[wikilink]] resolves to a real note
  5. every note is reachable from 00-index.md
  6. gap notes carry a STANDING line in the body
"""
import io, os, re, sys

STANDING = {"live", "narrowed", "withdrawn", "overturned"}
EVIDENCE = {"citation-intersection", "full-text-read", "string-protocol",
            "single-review", "not-assessed"}
RETIRED  = {"holds", "weakened", "collapsed"}
TYPES    = {"gap", "move", "method", "theorem", "computed", "index", "question"}
CROSSES  = {"nothing": 0, "word": 1, "metaphor": 2,
            "vocabulary": 3, "formalism": 4, "data": 5}
TOPOLOGY = {"disjoint", "direct", "mediated"}
EDGES    = ("borrows-from", "lends-to", "mutual-with",
            "computed-in", "uses-move", "rests-on")

def notes():
    for root, dirs, files in os.walk("."):
        # sources/ is an archive of primary documents, not knowledge notes — skip it
        if "sources" in dirs:
            dirs.remove("sources")
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(root, f)

def front(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m: return {}
    d = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            d[k.strip()] = v.strip().strip('"')
    return d

def main():
    errs, warns = [], []
    stems, index_links = set(), set()
    docs = {}

    for p in notes():
        stem = os.path.splitext(os.path.basename(p))[0]
        if stem.startswith("_"): continue
        stems.add(stem)
        text = io.open(p, encoding="utf-8").read()
        docs[p] = (stem, front(text), text)

    for p, (stem, fm, text) in docs.items():
        if text.startswith("﻿"):
            errs.append(f"{p}: UTF-8 BOM at start of file — breaks frontmatter parsing. "
                        f"Written by PowerShell Set-Content; rewrite without a BOM")
        t = fm.get("type")
        if not t:
            errs.append(f"{p}: no type")
        elif t not in TYPES:
            errs.append(f"{p}: type '{t}' not in {sorted(TYPES)}")

        if t == "gap":
            s, e = fm.get("standing"), fm.get("evidence")
            if s not in STANDING:
                errs.append(f"{p}: standing '{s}' not in {sorted(STANDING)}")
            if e not in EVIDENCE:
                errs.append(f"{p}: evidence '{e}' not in {sorted(EVIDENCE)}")
            if not re.search(r"^\*\*STANDING:", text, re.M):
                errs.append(f"{p}: no STANDING line in body")

            c = fm.get("crosses")
            if c not in CROSSES:
                errs.append(f"{p}: crosses '{c}' not in {sorted(CROSSES)}")
            elif fm.get("crosses-rank") != str(CROSSES[c]):
                errs.append(f"{p}: crosses-rank {fm.get('crosses-rank')} "
                            f"disagrees with crosses '{c}' (should be {CROSSES[c]})")

            if fm.get("topology") not in TOPOLOGY:
                errs.append(f"{p}: topology '{fm.get('topology')}' not in {sorted(TOPOLOGY)}")
            elif (fm.get("topology") == "mediated") != bool(fm.get("mediator")):
                errs.append(f"{p}: topology 'mediated' and mediator field must agree")

            cs = fm.get("contact-surface", "")
            if not re.fullmatch(r"\d+", cs):
                errs.append(f"{p}: contact-surface '{cs}' is not a bare integer")

            for k in EDGES:
                if k not in fm:
                    errs.append(f"{p}: missing edge field '{k}'")

        for k, v in fm.items():
            if k in ("standing", "evidence", "type") and v.lower() in RETIRED:
                errs.append(f"{p}: retired vocabulary '{v}' in machine field '{k}'")

        for link in re.findall(r"\[\[([^\]|#]+)", text):
            link = link.strip()
            if stem == "00-index": index_links.add(link)
            if link not in stems:
                errs.append(f"{p}: dead wikilink [[{link}]]")

    for s in sorted(stems - index_links - {"00-index"}):
        warns.append(f"not linked from 00-index: {s}")

    for e in errs:  print("ERROR  " + e)
    for w in warns: print("WARN   " + w)
    print(f"\n{len(stems)} notes | {len(errs)} errors | {len(warns)} warnings")
    return 1 if errs else 0

if __name__ == "__main__":
    sys.exit(main())
