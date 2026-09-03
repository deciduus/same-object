---
name: graph-view
type: method
---

# Reading the graph

Zero plugins. Everything here is Obsidian core.

## Turn on

Graph view → **Display → Arrows.** The edge fields are genuinely directional
(`borrows-from` is not `lends-to`), so arrows carry real information rather than decoration.

## Colour groups

Settings live in the graph view's **Groups** panel. **Order matters: the last matching group
wins.** So declare the coarse thing first and the sharp thing last.

Paste these queries in this order:

| Order | Query | Meaning |
|---|---|---|
| 1 | `["type":"gap"]` | every catalogue entry, base colour |
| 2 | `["type":"theorem"]` | the unread results |
| 3 | `["type":"move"]` | the six structural patterns |
| 4 | `["type":"computed"]` | numbers this project produced |
| 5 | `["standing":"withdrawn"]` | dimmed — do not cite |
| 6 | `["standing":"overturned"]` | dimmed — do not cite |
| 7 | `["evidence":"citation-intersection"]` | **declared last, so it wins** |

Group 7 is last on purpose. Node size cannot be bound to a property in Obsidian, so
**evidence strength has to be carried by colour**, and it only survives if nothing repaints
over it.

## What the layout should show

If the schema is honest, the graph clusters by literature and not by folder. The gaps with
`topology: disjoint` sit at the rim with few edges. That rim is the [[00-index]] open-work
queue, drawn rather than written.
