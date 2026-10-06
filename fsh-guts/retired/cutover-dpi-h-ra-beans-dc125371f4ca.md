---
$schema: folio-fsh-guts/v1
title: "beans/ of dpi-h-ra, as removed from main by its cutover"
kind: cutover-snapshot
movedOn: 2026-10-06
movedFrom: "beans/"
reason: cutover
instance: "dpi-h-ra"
directory: "beans"
sourceCommit: b166ab75ffbae6a0f98d4340b9f28c3b862bb4bb
tree: dc125371f4ca4f3eddb9a7d8048ac92c845a9be0
authoritativeBranch: "cat/dpi-h-ra/beans"
archive: "cutover-dpi-h-ra-beans-dc125371f4ca.tar.gz"
files: 3
bytes: 3552
summary: >-
  beans/ as main tracked it at b166ab75ffba (tree dc125371f4ca, 3 file(s),
  3552 bytes), packed beside this file as cutover-dpi-h-ra-beans-dc125371f4ca.tar.gz by git archive. It was removed from
  main by state:seed --cutover after cat/dpi-h-ra/beans was verified authoritative and
  byte-identical; that branch is the live store, and this is the copy main last held.
---

# beans/ of dpi-h-ra, at its cutover

`cutover-dpi-h-ra-beans-dc125371f4ca.tar.gz` beside this file holds `beans/` exactly as `main` tracked it at
`b166ab75ffbae6a0f98d4340b9f28c3b862bb4bb` — list it with `tar -tzf cutover-dpi-h-ra-beans-dc125371f4ca.tar.gz`. Extracted and added to a
fresh index it writes tree `dc125371f4ca4f3eddb9a7d8048ac92c845a9be0`, which is how the cutover verified it before
removing anything.

The live content is on `cat/dpi-h-ra/beans`, mounted at `beans/` by `state:mount`.
Do not unpack this back onto `main`: edit the branch.
