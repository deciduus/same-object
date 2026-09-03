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

## If the core graph stops being enough

Obsidian itself is closed-source and cannot be modified. The plugin API is the only route, and
it is the one every impressive graph online is actually using.

| Plugin | What it adds that core cannot do |
|---|---|
| [Extended Graph](https://github.com/ElsaTam/obsidian-extended-graph) | **node size, shape and images bound to properties**; filter by property; saved views; SVG export |
| [Juggl](https://github.com/HEmile/juggl) | a separate interactive graph with per-node styling |
| [3D Graph](https://www.obsidianstats.com/plugins/3d-graph) | three dimensions. Mostly decorative |

**Extended Graph lifts the constraint that forced the colour ordering above.** With it,
`evidence` can drive **node size** and `standing` can drive colour, which is the honest
mapping: strength is a magnitude, standing is a category.

Nothing here is needed yet, and none of it is installed. The vault is plain markdown, so it
can also be read by a script or a custom dashboard if a gap ever demands one — Obsidian is one
reader of the data, not the format.

## What the layout should show

If the schema is honest, the graph clusters by literature and not by folder. The gaps with
`topology: disjoint` sit at the rim with few edges. That rim is the [[00-index]] open-work
queue, drawn rather than written.
