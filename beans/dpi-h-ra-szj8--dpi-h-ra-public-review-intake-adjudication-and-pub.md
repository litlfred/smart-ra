---
# dpi-h-ra-szj8
title: 'DPI-H RA public review: intake, adjudication and publication of the revised guidance'
status: in-progress
type: epic
created_at: 2026-10-04T20:11:54Z
updated_at: 2026-10-04T20:11:54Z
---

The DPI-H Reference Architecture (draft v1.0) went out for public comment, closing 6 September 2026. This is the work of receiving, adjudicating and incorporating the comments in this folio. Platform: folio-assistant `public-comment` skill (bean folio-assistant-v26p, issue litlfred/folio-assistant#197).

## Done
- [x] smart-base harness installed (`dpi-h-ra.json` needs smart-base); folio scaffolded
- [x] review version frozen in `library/who-dpi-h-reference-architecture-draft-v1/` (PDF + .docx + extraction + page/line map)
- [x] document extracted to `folio/dpi-h-ra/` (11 chapters, 138 sections, 946 blocks, page/line provenance on each)
- [x] comment store, dashboard and per-block comment notes; staging previews; GitHub committee/editor tags

## To do
- [ ] owner: enable Issues on litlfred/smart-ra (committee discussion per comment), and list editor and committee GitHub logins in `review/public-comment/config.json`
- [ ] import each returned comment matrix: `bun run folio-assistant/folio-assistant-core/scripts/public-comment.ts import <file.xlsx>` (keep the files out of git)
- [ ] import the online-form export (.csv) and each narrative letter (`import-narrative`)
- [ ] triage every unplaced and low-confidence anchor
- [ ] committee recommendations; editor decisions; author edits on feature branches; incorporate on merge
- [ ] replace OpenHIE references in the DIIG with references to this document (downstream, after adoption)
