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

On every successful build of `main` (`.github/workflows/archimate.yml`, after
the staging preview):

- `/archimate/<version>/` — Archi's HTML report for each folder;
- `/archimate/` — the current version's report again;
- `/mapper/` — the RA mapper (`.github/workflows/ra-mapper.yml`), current
  version first.
