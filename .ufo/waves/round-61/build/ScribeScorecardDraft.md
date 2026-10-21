# ScribeScorecardDraft — round-61 SCORECARD section (draft, report only)

Scope: draft only; no edit to `SCORECARD.md` or corpus. Probe not run by this seat; base values are pre-registered author-side output in `reports/round-61/measure-before.log`.

## Draft section (insert after `SCORECARD.md:144`)

```
## Round 61 — axes (attempt 1; claim base cf02419; pending non-author verification)

Pre-registration `reports/round-61/claims.md` (e0a4b0c). Predictions and falsifiers copied from it; no "after" value is measured yet.

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| coverage — knowledge-map ground (K), C1 | 2.9 → TBD (4/14 → TBD/14; 6/14 = 4.3 if both admit, 5/14 = 3.6 if one; 4/14 falsifies C1) | probe `K_HELD`, `K_ROW C04`, `K_ROW C09` | cf02419 → TBD | pending non-author verification |
| calibration — receipt-identity mutation kill (split, C2) | 0.0 → TBD (0/2 → TBD/2; 2/2 = 10.0) | probe `C2_RECEIPT_B_KILLED` | cf02419 → TBD | pending non-author verification |
| hold: calibration — saved-ledger runnability (C) | 10.0 → TBD (`HOLD_CALIBRATION` 4/4 → TBD; `HOLD_REPLAY` 10/10 → TBD) | probe `HOLD_*`; SCORECARD:32-43 | cf02419 → TBD | must stay 10.0 |
| hold: coverage — record presence (F) | 5.0 (at 35b2e8b, `:132`) → TBD (cf02419 not probed) | SCORECARD:45-57 (not in probe) | cf02419 → TBD | must stay 5.0 |

Split reasons (AXES.md §Working the axes; pattern of SCORECARD:138-140):
- K stays split from F: F counts saved REA record families and cannot see sourced knowledge; K counts map rows held by gated, sourced entries. Neither replaces the other.
- Receipt-identity kill is split from C: C counts exit 0 of `--self-test` over four named scripts; kaika mutant b survives at exit 0 (`.ufo/waves/kaika-r1/mutation-post.md:15,21`), so C cannot see a deleted receipt-identity clause. The kill criterion counts whether each script's own run rejects an in-memory forged receipt command. C remains a hold.

Counting (base, `reports/round-61/measure-before.log:1`):
  B=/tmp/revenger-r61-before; mkdir -p $B && git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive --format=tar cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97 corpus | tar -x -C $B && python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-61/measure.py $B
After: same with commit TBD, plus `git -C <lane> diff cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97 TBD -- corpus/live corpus/fixtures` (must be empty). Read probe exit code: 2 = could-not-evaluate.

Lowest-axis obligation: claims.md:15-17 names K (2.9). The receipt criterion at 0.0 is also lowest; C1 (K) and C2 are distinct, causally separable axes (claims.md:64-70), so the obligation holds under either reading.

Planned next round (SCORECARD:179-181; item 2 is this round's C2, C04/C09 part of item 3 is this round's C1):
1. coverage F — author inert known-truth firmware fixture; run REA `inspect_firmware_regions` (binwalk 3.1.0, unblob 26.6.4). Target F 4/8 → 5/8. Falsifier: record lacks `evidence_id` or `normalized_result`, or disagrees with byte oracle → F stays 4/8.
2. coverage K — re-gate `knowledge/seed.md` and `knowledge/2026-10-12-rea-readiness-checklist.md` against QUALITY Q01–Q11 (corpus/README.md:47-52: not re-gated). Falsifier: any failing Q id → recorded, not counted.

Saturation: unchanged — 7.0 line, window N = 3 (SCORECARD:173). Nudge does not apply (K 2.9 and receipt 0.0 sit below 7.0); no capability claim in claims.md. Retired: none.

Milestones (TBD): C04 sourced entry (base uncovered, corpus/README.md:30); C09 (uncovered, :35); receipt-command control in both scripts (base 0/2, mutation-post.md:15,21); sources census `revenger ok` exit 0 before (measure-before.log:29-30), after TBD.
First falsifiers: K_HELD after = 4/14 → C1 falsified. C2_RECEIPT_B_KILLED < 2/2, any hold ≠ base, or nonempty corpus/live|fixtures diff → C2 falsified or voided.
Learning trends: expansion TBD (C1); discernment TBD (C2); quality and freshness untouched.
```

## Findings

- F1 `reports/round-61/measure.py:18-26,84-100`: probe prints K, C2, HOLD values; it does not print F or the saved-record diff — run those separately.
- F2 `measure.py:65-68,99-100`: a could-not-evaluate mutant is skipped (not counted as killed) and `C2_RECEIPT_B_KILLED=k/2` still prints; exit 2 is the only signal. Cite exit code, not k/2 alone.
- F3 `claims.md:15-17`: "lowest criterion" predates the receipt criterion (see obligation above).
- F4 `SCORECARD.md:39`: both C2 scripts sit in C's `names` set; read `HOLD_CALIBRATION` with the C2 result.
- F5 `measure-before.log:2-25`: base matches pre-registration (K 4/14 = 2.9; C2 0/2, controls 2/2, d2 2/2; HOLD_CALIBRATION 4/4; HOLD_REPLAY 10/10).
- F6 arithmetic checked: 10×6/14 = 4.3; 10×5/14 = 3.6; 10×4/14 = 2.9; 10×2/2 = 10.0.
- F7 `corpus/README.md:9` says QUALITY Q01–Q10; `corpus/QUALITY.md:23` defines Q11 (supersedes Q08). Draft uses Q01–Q11; reconcile the README index in the integrated SCORECARD.
- F8 Installs/updates: none. Read `~/.omp/agent/RULES.md`; read-only `jj log` run.

VERDICT: draft section ready; all after-values TBD; pending non-author verification.
