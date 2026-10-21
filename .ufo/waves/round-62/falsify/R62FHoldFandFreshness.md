GRADE: HOLDS — F/freshness readouts preserved on frozen candidate d97761952be256d145d298022de03091de91d358 vs claim base 5bd4a90fc1a34caa94496601b60537b3aab12301

## Target (full hashes)
- Frozen revision `d97761952be256d145d298022de03091de91d358` (rev-parse, full); tree `45c4c5da82aae8ca2e44f6e3ed874a33533f54b9`; extracted with `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive d977619… | tar -x -C /fast/scratch/hyaku/revenger-r62/R62FHoldFandFreshness/arch`. Extraction 783 files = `git ls-tree -r --name-only d977619… | wc -l` 783 (complete).
- Claim base `5bd4a90fc1a34caa94496601b60537b3aab12301`, same extraction to `…/base`. Pre-registration `a3498e25ad87bf756288812d0ea7c474b09433c7` is the entries' lane base, not this attack's tree.
- cwd = each extracted tree root (the scored commands use relative `corpus/…`; cwd=/ is not usable without rewriting them). `TMPDIR=/fast/scratch/hyaku/revenger-r62/R62FHoldFandFreshness/tmp`.

## Observation — F command, SCORECARD.md:45-57
Command block extracted verbatim from `arch/SCORECARD.md:45-57` to `cmd_f.sh` (`awk 'NR>=45 && /^```sh/{flag=1;next} flag && /^```/{exit} flag{print}'`; 9 lines, ends with the COVERAGE print), run as `bash ../cmd_f.sh` in each tree.
- base exit=0: `COVERAGE 4 / 8 score= 5.0 families= ['native-static', 'javascript', 'archives', 'evm']`
- arch exit=0: identical; `diff out_f_base.txt out_f_arch.txt` → no output, `F-OUTPUTS-IDENTICAL`.
- Full counters, both trees, identical: `{"analyze_javascript_application": 6, "compare_application_versions": 1, "compare_javascript_export_shapes": 3, "extract_artifact": 2, "inspect_analysis_view": 1, "inspect_artifact": 4, "inspect_evm_interface": 7, "inspect_pe_resources": 30, "trace_application_feature": 2, "trace_javascript_semantics": 2}`.
- No lost family: the four present families and their record counts are unchanged base→frozen; managed/android/firmware/browser-runtime were absent in both.

## Observation — freshness command, SCORECARD.md:134
- Command as intended (`grep -cE '^\| [FK][0-9]+ .*\| (holds|STALE)' corpus/knowledge/{seed.md,2026-10-12-rea-readiness-checklist.md}`), in both trees: `seed.md:12`, `2026-10-12-rea-readiness-checklist.md:6` → 18 total. All-table rows also 18 in both (no un-flagged row added or removed).
- Frozen statuses: 8 rows `holds`, 10 rows `STALE`, and all 10 STALE rows carry `→` current values (`STALE-with-arrow: 10`).
- Byte identity base↔frozen: `seed.md` `d1d31602f2b667d6c9406743f06dd2f14030cf1fdf477b1da251f2682d7d7534`; checklist `561327faf39fdc9221c3ebc1b2f9e5175a466ca39fb2c37d119be594f085b6e0`. No fact row was edited or added.
- Verbatim markdown cell: the recorded regex shows `(holds\|STALE)`. GNU grep ERE treats `\|` as a literal pipe, so the literal cell text prints `seed.md:0`, `checklist:0`, exit=1 on BOTH trees. De-escaping the table cell's alternation pipe reproduces 12+6. This is a pre-existing authoring/table-escaping nuance, byte-identical at base and frozen, not a candidate delta and not a lost fact.

## Observation — surrounding held state (no flip)
- `corpus/README.md` sha256 `2c8606d3de51014c83f5be1e2b1309a8f42c343a5c2b006cc73ed0ee96e8e23f` identical base↔frozen; `grep -cE '^\| C[0-9]+ .*\| held \|$'` = 4 in base and frozen; 14 C-rows in both.
- `corpus/README.md:33` C04 and `:38` C09 both still `uncovered` in the frozen tree, citing only the round-61 rejected candidates; neither new entry is named in a held row. `corpus/live/runs`: 344 files both, combined digest `1b1d9344249ead062b917abda696fd097abe10ffd2d54dbd9010571995680997` both (`LIVE-RUNS-IDENTICAL`).
- `git diff --name-only 5bd4a90… d977619…` changes nothing under `corpus/live`, `corpus/knowledge/seed.md`, the checklist, `corpus/README.md` or `SCORECARD.md` (0 matches). The two new files are `corpus/knowledge/round-62-{commonjs-require-name,evm-dispatch-byte}-evidence.md`, both `admission-status: candidate (not admitted)`.

## Inference
- Because `corpus/live/runs` and the two freshness files are byte-identical base↔frozen, the 4/8 family coverage and the 18 hold/STALE-with-current-value rows are preserved in this exact frozen state; the candidate adds knowledge drafts only.
- This is a readout-preservation check, not a live-host freshness or producer-readiness claim. The entries themselves make no such claim (`round-62-evm-dispatch-byte-evidence.md:194`: "No current capability is claimed; the records were not re-run."; `round-62-commonjs-require-name-evidence.md:288`: "n/a (no readiness or capability claim)").

## Unknown
- Live-host truth of the 18 facts was not re-probed (prohibited live probing; outside this bounded check); `holds`/`STALE→value` are recorded statuses, not a new verification.
- C04/C09 admission and K 4/14 → ≥5/14 remain other seats'/L1's decisions; this lane made no admission.

VERDICT: HOLDS for the assigned F/freshness preservation check. No repair or admission indicated. Installs: none.
