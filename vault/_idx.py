#!/usr/bin/env python3
"""Generate the Gaps list in 00-index.md from gap-note frontmatter.

  python _idx.py           rewrite the block between the IDX:GAPS sentinels
  python _idx.py --check   exit 1 if the file would change (no write)

The block is generated: edit the notes, not the list. Idempotent; deduped by
frontmatter `name`; grouped by `standing` in the order live, narrowed,
withdrawn, overturned.
"""
import io, os, re, sys

HERE  = os.path.dirname(os.path.abspath(__file__))
GAPS  = os.path.join(HERE, "gaps")
INDEX = os.path.join(HERE, "00-index.md")

OPEN_S  = "<!-- IDX:GAPS -->"
CLOSE_S = "<!-- /IDX:GAPS -->"

STANDING_ORDER = ["live", "narrowed", "withdrawn", "overturned"]
EVIDENCE_ORDER = ["citation-intersection", "full-text-read", "string-protocol",
                  "single-review", "not-assessed"]


def front(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    d = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            d[k.strip()] = v.strip().strip('"')
    return d


def collect():
    by_name = {}
    for f in sorted(os.listdir(GAPS)):
        if not f.endswith(".md"):
            continue
        fm = front(io.open(os.path.join(GAPS, f), encoding="utf-8-sig").read())
        if fm.get("type") != "gap":
            continue
        name = fm.get("name") or os.path.splitext(f)[0]
        by_name[name] = fm          # dedupe by name; last file wins
    return by_name


def render(by_name):
    out = [OPEN_S, "", "<!-- generated from frontmatter by _idx.py; edit the notes, not this list -->"]
    for standing in STANDING_ORDER:
        rows = [(n, fm) for n, fm in by_name.items()
                if fm.get("standing") == standing]
        if not rows:
            continue

        def key(item):
            n, fm = item
            e = fm.get("evidence", "")
            rank = EVIDENCE_ORDER.index(e) if e in EVIDENCE_ORDER else len(EVIDENCE_ORDER)
            return (rank, n)

        out.append("")
        out.append("### " + standing.capitalize())
        for n, fm in sorted(rows, key=key):
            out.append("- [[%s]] — *%s* — %s"
                       % (n, fm.get("evidence", "not-assessed"), fm.get("note", "").strip()))
    out.append("")
    out.append(CLOSE_S)
    return "\n".join(out)


def apply(text, block):
    i = text.find(OPEN_S)
    j = text.find(CLOSE_S)
    if i == -1 or j == -1:
        raise SystemExit("00-index.md: missing %s / %s sentinels" % (OPEN_S, CLOSE_S))
    return text[:i] + block + text[j + len(CLOSE_S):]


def main(argv):
    check = "--check" in argv
    text = io.open(INDEX, encoding="utf-8").read()
    new = apply(text, render(collect()))
    if new == text:
        if not check:
            print("00-index.md: gaps block already up to date")
        return 0
    if check:
        print("ERROR  00-index.md: generated gaps block is stale — run `python _idx.py`")
        return 1
    io.open(INDEX, "w", encoding="utf-8", newline="").write(new)
    print("00-index.md: gaps block regenerated")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
