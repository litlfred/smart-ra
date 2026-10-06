# cat/dpi-h-ra/todos — the `todos` subgraph of dpi-h-ra

Orphan branch, never merged into `main`. A tip-keyed state branch: one live
copy of the `todos` subgraph of the `dpi-h-ra` folio instance, its paths
mirroring the checkout exactly (`todos/…` here is `todos/…` on `main`), with a root
`manifest.json` (`state-manifest/v1`, `keyedBy: "tip"`) that makes it a state
branch for `folio-assistant/cat-harness/scripts/branch-store.ts`.

**What it is for.** Owner decision 2026-10-06: smart-ra's `beans/` and
`todos/` are to be branch-mounted per the harness's subgraph-source mechanism
(`cat-harness/skills/kg/kg-core/directory-conventions.md` §"Where a subgraph
gets its content — `source`"). `dpi-h-ra.json` declares the `todos` directory
with `source: { "kind": "branch", "branch": "cat/dpi-h-ra/todos", "keyedBy": "tip" }`.

**Status: SEED, not authoritative.** `main` still tracks `todos/`, and removing
it from `main` is a separate owner decision. Until that cutover, `main` is the
source of truth and edits made here are read by nothing. See `manifest.json`.

**How it was generated.** 2026-10-06T17:08:28Z, by hand with git plumbing (no seeding command
creates a branch: `state-seed.ts` only refreshes an existing one): the tree is
`main@bcd7e92ab5b8`'s `todos/` subtree verbatim (tree `7793287e5665`, 4 file(s)), plus
this README and the manifest, committed with no parent.

**Keeping it current.** `bun run state:seed --id todos` refreshes it from the
ref the manifest records; `--authoritative` is the cutover's branch half and
is one-way. Writes splice onto the tip and never force-push.

**Name.** `cat/<instance>/<subgraph>`, mirroring `cat/cat-harness/todos`. To be
reconciled with the state-branch naming convention `folio_init` is adopting.
