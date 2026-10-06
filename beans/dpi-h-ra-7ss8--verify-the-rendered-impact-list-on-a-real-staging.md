---
# dpi-h-ra-7ss8
title: Verify the rendered-impact list on a real staging preview
status: todo
type: task
created_at: 2026-10-06T17:21:55Z
updated_at: 2026-10-06T17:21:55Z
---

Issue: litlfred/smart-ra#23 (comment there on start and on every push).
Goal: first real staging run of the rendered-impact work in litlfred/folio-assistant (#2261, #2285, #2293, all merged): the PR comment lists the rendered pages a change alters, says what the build changed that the list missed, and the review page shows the list.
Needs network access to packages.fhir.org and packages2.fhir.org (SUSHI).

## Todo
- [ ] branch claude/rendered-impact-check from origin/main
- [ ] bump the folio-assistant submodule to current folio-assistant main: git -C folio-assistant fetch origin main && git -C folio-assistant checkout origin/main && git add folio-assistant
- [ ] one prose fix: folio/dpi-h-ra/ch1-introduction/p-1-5-1-3c0865.md, "as well as service coverage ." -> "as well as service coverage."
- [ ] OWNER RULE: SUSHI must run with 0 errors before committing: npx -y fsh-sushi . (stop and report on #23 if it errors)
- [ ] commit (this bean file too), push, open a DRAFT PR that references #23; do NOT merge
- [ ] wait for the "Staging preview" workflow (15-25 min incl. the gh-pages rate limit)
- [ ] report on #23: the bot comment's "Rendered pages to review" list (expect dpi-h-ra/index.html > prose:1-5-1-3c0865) and its "not known" line for the submodule bump; the "Measured against main" / "Missed by the list above" line; <preview>/rendered-impact.json and <preview>/rendered-measured.json; whether <preview>/review/ shows "Rendered pages this change alters"
- [ ] note anything wrong: a predicted page that did not change, a missing anchor, a missed page

## Done when
The PR comment and review page show the rendered list and the measurement for this change, and the findings are on #23.
