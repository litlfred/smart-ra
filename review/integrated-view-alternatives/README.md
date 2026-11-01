# Integrated View: the two naming alternatives not merged

Option A (merged with tools/archimate-dth/dpi_h_integrated.py) renames the 15 elements that are the same thing as a figure box, and adds new elements for the 12 that are narrower or of another type. This folder keeps the two alternatives for the discussion in the linked issue:

- `view-B-rename-all.svg`, `dpi_h_integrated_B.py`: rename all 27 near-match elements.
- `view-C-keep-as-is.svg`, `dpi_h_integrated_C.py`: rename nothing; 23 new elements carry candidateMatch.
- `view-A-merged.svg`: what was merged, for comparison.

The drawings are made by `pretty.py model.xml "<view name>" out.svg --marks` from the model alone. ● = an existing element renamed (formerName kept), ○ = a new element next to a similar older one (candidateMatch).
To rebuild B or C: `python3 -I tools/archimate-dth/add_views.py review/integrated-view-alternatives/dpi_h_integrated_B.py archimate/0.3.0-draft.1/WHOBaseFile.archimate /tmp/B.archimate` on the model *before* the merge.
