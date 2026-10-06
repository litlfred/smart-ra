---
$schema: folio-fsh-guts/v1
title: "todos/ of dpi-h-ra, as removed from main by its cutover"
kind: cutover-snapshot
movedOn: 2026-10-06
movedFrom: "todos/"
reason: cutover
instance: "dpi-h-ra"
directory: "todos"
sourceCommit: 6d996432245c53f15fc8de2efdb8c5f183d6f1f3
tree: 7793287e56652fbce7ce7c8e29242b6629f4b7b1
authoritativeBranch: "cat/dpi-h-ra/todos"
archive: "cutover-dpi-h-ra-todos-7793287e5665.tar.gz"
files: 4
bytes: 1012
summary: >-
  todos/ as main tracked it at 6d996432245c (tree 7793287e5665, 4 file(s),
  1012 bytes), packed beside this file as cutover-dpi-h-ra-todos-7793287e5665.tar.gz by git archive. It was removed from
  main by state:seed --cutover after cat/dpi-h-ra/todos was verified authoritative and
  byte-identical; that branch is the live store, and this is the copy main last held.
---

# todos/ of dpi-h-ra, at its cutover

`cutover-dpi-h-ra-todos-7793287e5665.tar.gz` beside this file holds `todos/` exactly as `main` tracked it at
`6d996432245c53f15fc8de2efdb8c5f183d6f1f3` — list it with `tar -tzf cutover-dpi-h-ra-todos-7793287e5665.tar.gz`. Extracted and added to a
fresh index it writes tree `7793287e56652fbce7ce7c8e29242b6629f4b7b1`, which is how the cutover verified it before
removing anything.

The live content is on `cat/dpi-h-ra/todos`, mounted at `todos/` by `state:mount`.
Do not unpack this back onto `main`: edit the branch.
