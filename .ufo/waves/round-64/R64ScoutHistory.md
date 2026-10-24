# R64ScoutHistory — findings

Axes: reproducibility, attribution accuracy, historical-evidence preservation.

## Observed

- The `139 positive checks` quotation is at `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-58/reviewer.md:13`, repeated in `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-58/LEDGER.md:4`.
- Literal searches found no `139` in `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-59/`; its reviewer records direct byte checks. Do not claim both historical reviewers contain the quotation.
- Ran each assigned check once, concurrently, from `/`; both tool invocations completed successfully:

  ```sh
  python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_named_multi_icon_states.py --self-test
  ```
  ```text
  PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
  ```
  ```sh
  python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_icon_states.py --self-test
  ```
  ```text
  PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
  ```

The commands did not print numeric exit-code lines. The saved red-before receipt independently records control exit 0 and identical summaries at `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure-before.log:22-27`.

## Inference and limits

[INFERENCE] The named-multi +3 is consistent with its current C3 forged-receipt `req` at `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_named_multi_icon_states.py:76-78`, once per round 55/56/57 (lines 62, 84); `req` increments `N` (lines 10–14). A historical version/diff was not reconstructed. Icon states has no 142-check output; preserve its actual state/delta summary.

LSP unavailable: `read xd://lsp` returned `No such tool`, with only ast_edit/debug mounted. Source findings are literal evidence, not semantic-reference proof. Confidence: high for current outputs and quote locations; medium for historical causality. Remaining unknown: intended round-59 citation and precise patch lineage.

## Preservation and deliverable

Historical evidence remains untouched under `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/claims.md:115-122,147-150`. The complete non-reproduction receipt, including commands, outputs, scope, source accounting and preservation rationale, is `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/scout-history.md`.

Only the two assigned receipt/report files were written. No production/history/fixture edits, Git/JJ commands, tool installs/updates or scratch artifacts. No additional verification requested or performed.

Report: .ufo/waves/round-64/R64ScoutHistory.md
