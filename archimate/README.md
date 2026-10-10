# ArchiMate models — one folder per version, named by SemVer

Each folder holds one `.archimate` model (Archi native XML or a zipped Archi
archive) and is named for the version of this IG it belongs to — the
`version:` in `sushi-config.yaml`. Nothing else says which one is current:
the folder whose name equals that `version:` is.

| folder | model | where it came from |
|---|---|---|
| `0.2.0/` | `WHO_RA` — 20 views, incl. Testing and Conformance | `v3/` (and its byte-identical copy `v2/`), 2026-07-09 |
| `0.2.0-draft.3/` | `WHO Models` | `v1/` |
| `0.2.0-draft.2/` | `WHO Reference Architecture` | `prev1/` |
| `0.2.0-draft.1/` | `WHO Models` | `prev2/` — "WHO Reference Architecture Draft v.2 - 6.2.2026" |

The `draft.N` order is the order the previous folder names gave
(`prev2` < `prev1` < `v1` < `v3`); the history before 2026-07-09 renames the
same files back and forth too often to recover a better one.

**Releasing a version:** when `sushi-config.yaml` moves to a new `version:`,
add `archimate/<that version>/` with its model. Until it exists the workflows
warn and publish no current model at `/archimate`.

## Published

Every staging build (each pull request, and every push to `main`) runs
cat-harness's `archimate` subgraph over the models `cat-archimate.config.json`
names — skill `archimate-models`, Tools `archimate-check` and
`archimate-pages`:

- `/en/dpi-h-ra/archimate/` — every model;
- `/en/dpi-h-ra/archimate/<version>/` — a model's views, and its elements by layer;
- `/en/dpi-h-ra/archimate/<version>/views/<id>/` — a view, drawn as SVG from the
  model (`/archimate/<version>/views/<id>.svg`), every box a link to its
  element;
- `/en/dpi-h-ra/archimate/<version>/elements/<id>/`, `…/relationships/<id>/` — one
  page per element and relationship, keyed by Archi's id, with its JSON-LD IRI
  at `/archimate/<version>/elements/<id>.jsonld` (and `…/relationships/`);
- `/en/mapper/` — the RA mapper (`.github/workflows/ra-mapper.yml`, after a
  successful build of `main`), current version first.

The pages are at the route of the visualiser `dpi-h-ra.json` declares for the
`archimate-pages` Tool, `/<locale>/<harness>/<visualiser>/` (owner, 2026-10-09;
folio-assistant#2527); the data they draw from — the SVG drawings and the
JSON-LD — keeps its address under `/archimate/`, so no IRI moves.

**No Java.** The Archi command-line report that `archimate.yml` used to run
(a JVM, a virtual display and a ~200 MB download per run) is gone (owner,
2026-10-09). Draw in Archi on your own machine; commit the `.archimate`; the
build does the rest. A pull request's preview is at
`STAGING/<branch>/en/dpi-h-ra/archimate/`.
