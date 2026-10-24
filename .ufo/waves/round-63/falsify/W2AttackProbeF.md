# W2AttackProbeF — frozen F counter adversarial review

## Scope, axes, and result

Attacks **C2 coverage F**, specifically the distinction between selected-family record presence and the frozen claim's real-run/oracle requirements. Axes: **coverage F**, **producer provenance / Evidence-ID identity**, **byte-oracle agreement**, **negative-input filtering**, and **preservation of frozen holds**. This is a critic report, not an admission decision; no C1 Q-pass or C3 judgment is issued here.

**Counterexample confirmed:** a hand-written firmware record with a made-up Evidence ID and false region data produces `F_COVERAGE=5/8 score=6.2`, `HOLDS_OK=yes`, and exit 0. A receipt lacking `normalized_result` and malformed JSON do not count. The counter is not a C2 admission oracle. The frozen **claim remains defensible against this attack only as its explicit conjunction**, not from the numeric F result alone. I independently confirmed committed record/fixture byte agreement, but did not witness or repeat the original REA invocation.

## Committed inputs and execution

All lane paths below are relative to `/home/vgpnk/Projects/shokunin/revenger-shokunin` unless absolute. Reviewed committed tip **`db55bd6488e24e956df5818ae34c2a043d7ddc12`**, obtained with read-only `git rev-parse HEAD`, then extracted:

```sh
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive db55bd6488e24e956df5818ae34c2a043d7ddc12 corpus reports/round-63/claims.md reports/round-63/measure.py reports/round-63/measure-before.log | tar -x -C /tmp/revenger-r63-W2AttackProbeF-357Mkw
```

SHA-256 of committed frozen inputs:

- `reports/round-63/measure.py`: `3b7fba2d5243bbe0b723a99a53085130ff97010e23c8a59a8027f5f8992c5908`
- `reports/round-63/claims.md`: `aed53241c3e4445fab94e854e3185b235ab2ff45c921d6c95e6e60938c7d1e31`

Used existing `/usr/bin/python3` **3.14.8**; no tools installed or updated, no pacman transaction. Ran the **entire unchanged counter**, not a reimplementation of its F block, on all five trees. The exact invocation template was:

```sh
TMPDIR=/tmp/revenger-r63-W2AttackProbeF-357Mkw/mutants /usr/bin/python3 -B /tmp/revenger-r63-W2AttackProbeF-357Mkw/reports/round-63/measure.py TREE
```

All runs used cwd `/`. Two independent counter runs were allowed concurrently. A scratch harness cloned the committed `corpus/` for each negative/control tree, removed **only that scratch copy's** `corpus/live/runs/round-63/`, and inserted the specified file when applicable. The committed-tip tree was untouched. Every reported counter result below is from my own fresh execution. The `no_round63` tree is a local F negative control, **not** a rerun of the historical base commit or its C3 red-before.

## F1 — fabricated record attacks C2 provenance and oracle agreement

In `cases/fabricated_record/corpus/live/runs/round-63/inspection.json`, the only saved round-63 file was this hand-written JSON; there was no producer run, receipt, or saved stdout in this case:

```json
{"evidence_id":"ev_fabricated_W2AttackProbeF_no_real_run","operation":"inspect_firmware_regions","normalized_result":{"regions":[{"offset":0,"reported_size":1,"signature":"zlib"}]}}
```

The counter counts it. Root cause is the exact predicate in `reports/round-63/measure.py:38-44`: parsed dictionary, truthy `evidence_id`, and `normalized_result is not None`; it then counts the unvalidated `operation` string. Lines 45-53 map that operation to the firmware family. It reads no command, receipt, subject digest, regions, or oracle at this step.

Exact F output for **both the real committed-tip tree and the fabricated tree**:

```text
{'analyze_javascript_application': 6, 'compare_application_versions': 1, 'compare_javascript_export_shapes': 3, 'extract_artifact': 2, 'inspect_analysis_view': 1, 'inspect_artifact': 4, 'inspect_evm_interface': 7, 'inspect_firmware_regions': 1, 'inspect_pe_resources': 30, 'trace_application_feature': 2, 'trace_javascript_semantics': 2}
F_COVERAGE=5/8 score=6.2
F_FAMILIES=['native-static', 'javascript', 'archives', 'firmware', 'evm']
```

Both complete counter executions also returned `HOLDS_OK=yes`, exit 0. Thus the complete counter's success status does not distinguish this fabricated record from the real candidate.

**Smallest safe correction:** do not alter the frozen counter or treat it as a provenance checker. Any final C2 conclusion must separately bind the actual committed record to its real producer receipt and byte-oracle agreement. A hand-written JSON passing this presence predicate is not C2 evidence.

## F2 — receipt-only input attacks C2's negative-input filtering

In `cases/receipt_only/corpus/live/runs/round-63/receipt.json`:

```json
{"evidence_id":"ev_fabricated_W2AttackProbeF_receipt_only","operation":"inspect_firmware_regions"}
```

This deliberately includes the matching operation as well as the Evidence ID, isolating absence of `normalized_result` as the rejection condition. It is **not counted**: no `inspect_firmware_regions` key is printed, and F remains 4/8. The actual committed receipt also lacks `normalized_result` and is not an additional firmware observation. No correction indicated by this control.

## F3 — malformed JSON attacks C2's parser-skip behavior

In `cases/unparseable_json/corpus/live/runs/round-63/inspection.json`, exact bytes (no closing value/object):

```text
{"evidence_id":"ev_invalid","operation":"inspect_firmware_regions","normalized_result":
```

It is **skipped**, not counted, and does not crash the complete probe. This matches `measure.py:39-42` catching JSON `ValueError` and Unicode decoding errors. No correction indicated by this control.

Exact F output shared by **no_round63**, **receipt_only**, and **unparseable_json**:

```text
{'analyze_javascript_application': 6, 'compare_application_versions': 1, 'compare_javascript_export_shapes': 3, 'extract_artifact': 2, 'inspect_analysis_view': 1, 'inspect_artifact': 4, 'inspect_evm_interface': 7, 'inspect_pe_resources': 30, 'trace_application_feature': 2, 'trace_javascript_semantics': 2}
F_COVERAGE=4/8 score=5.0
F_FAMILIES=['native-static', 'javascript', 'archives', 'evm']
```

## F4 — frozen claim, not the counter, excludes the fabrication

Reopened the committed `reports/round-63/claims.md:45-52` verbatim:

> Target: F **4/8 → 5/8** (`firmware` family present) **iff** a newly saved
> record at `corpus/live/runs/round-63/` (a) carries `evidence_id` and
> `normalized_result` with `operation == "inspect_firmware_regions"`, (b) is the
> output of one real `npx -y rea-agents@6.5.0 inspect-firmware-regions <path>`
> run (receipt committed with command, exit code, fixture SHA-256, stdout
> SHA-256, Evidence ID), and (c) every region the record reports matches the
> authored fixture's `truth.json` byte oracle (offset, size, and for
> extractable members the decompressed content SHA-256). **4/8 falsifies C2.**

The additional admission sentence at lines 105-108 says:

> Admission order (same as round 62): land candidates without README flip →
> fresh falsify wave → adjudicate → flip C06 only on all-criteria pass; C2 F
> count requires the byte-oracle agreement receipt; C3 requires red-before 0/2
> and attributed 2/2 at final.

The fabricated record satisfies (a) only. Condition (b) is false by construction: I wrote it without invoking REA. Condition (c) is also false: it claims a zlib region at offset 0 / size 1, while the authored reportable members are at 512 / 79 and 1024 / 90. I ran the committed checker explicitly against it:

```sh
python3 -B /tmp/revenger-r63-W2AttackProbeF-357Mkw/corpus/live/runs/round-63/oracle_check.py --record /tmp/revenger-r63-W2AttackProbeF-357Mkw/cases/fabricated_record/corpus/live/runs/round-63/inspection.json --truth /tmp/revenger-r63-W2AttackProbeF-357Mkw/corpus/fixtures/firmware-r63/truth.json
```

Observed rejection, exit **1** (mismatch lines and final verdict):

```text
MISMATCH subject.digest.sha256: missing or not a string
MISMATCH subject.digest.sha256: expected bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be, got None
MISMATCH normalized_result.input_size: expected 2048, got None
MISMATCH normalized_result.regions: expected 2 reportable regions, got 1
MISMATCH normalized_result.regions[0].offset: expected 512, got 0
MISMATCH normalized_result.regions[0].reported_size: expected 79, got 1
MISMATCH normalized_result.regions[1]: missing reported region
ORACLE MISMATCH
```

**Impact / boundary:** this falsifies the interpretation “5/8 plus exit 0 proves C2,” not the stronger preregistered conjunction. A presence counter intentionally lacking provenance validation is a disclosed measurement limitation, not permission to weaken real-run or oracle requirements. A receipt and matching hashes establish internal byte consistency, not an independently authenticated historical execution; the ledger itself acknowledges this at `corpus/live/runs/round-63/LEDGER.md:54,77-100`. Canonical admission must not promote that consistency into proof of origin. No new authentication requirement or alternate judge is introduced by this review.

## F5 — actual committed candidate versus the same byte gates

Reopened the committed `inspection.json`, `receipt.json`, `truth.json`, and `oracle_check.py`. Receipt command is the pinned `npx -y rea-agents@6.5.0 inspect-firmware-regions ... --format json`; receipt exit code is 0. Receipt and record carry the same Evidence ID:

`ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259`.

My fresh `sha256sum` and `cmp -s stdout.raw inspection.json` checks establish:

- Fixture SHA-256: `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be`, equal to receipt `fixture_sha256`, truth image digest, and record subject digest.
- `stdout.raw` and `inspection.json`: byte-identical, both SHA-256 `f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9`, equal to receipt `stdout_sha256`.
- Receipt SHA-256: `e930a549db16a180d4ab05307e073cd71599a3317b9f3d15a0d97843d5c6b94d`.

Fresh command, cwd `/`:

```sh
python3 -B /tmp/revenger-r63-W2AttackProbeF-357Mkw/corpus/live/runs/round-63/oracle_check.py
```

Observed output, exit 0:

```text
REGION name=padding kind=padding offset=0 size=512 record=not-expected padding=OK
REGION name=diagnostic-note kind=zlib offset=512 size=79 offset=OK size=OK signature=OK decompressed_sha256=OK (a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86)
REGION name=padding kind=padding offset=591 size=433 record=not-expected padding=OK
REGION name=component-note kind=zlib offset=1024 size=90 offset=OK size=OK signature=OK decompressed_sha256=OK (2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9)
REGION name=padding kind=padding offset=1114 size=934 record=not-expected padding=OK
ORACLE OK
```

This is positive evidence for byte agreement and saved-envelope consistency. It is not a claim that I witnessed the original shell invocation, authenticated the Evidence ID externally, or executed firmware; none of those occurred.

## Full-counter control receipts and limits

All five full runs printed the following unchanged accompanying results:

```text
K_HELD=6/14 score=4.3
K_ROW C06 status=partial
K_HELD_BACKED=6/14
FRESH_ROWS=18/18
C2_CONTROLS_PASS=2/2
C2_RECEIPT_B_KILLED=2/2
C2_D2_KILLED=2/2
C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
```

Every run exited 0 with empty stderr. `C2_*` here are the probe's **legacy calibration holds** (`measure.py:72-122`), not a real-run or byte-oracle gate for the round-63 firmware C2 claim. C06 remaining partial is expected before independent Q decisions; these incidental outputs do not provide those decisions.

| TREE suffix | Firmware operation count | F_COVERAGE / printed score | Exit | HOLDS_OK |
|---|---:|---|---:|---|
| root (committed tip) | 1 | `5/8 score=6.2` | 0 | yes |
| `cases/no_round63` | absent | `4/8 score=5.0` | 0 | yes |
| `cases/fabricated_record` | 1 | `5/8 score=6.2` | 0 | yes |
| `cases/receipt_only` | absent | `4/8 score=5.0` | 0 | yes |
| `cases/unparseable_json` | absent | `4/8 score=5.0` | 0 | yes |

Only this assigned report was written in the lane. All mutations were confined to `/tmp/revenger-r63-W2AttackProbeF-357Mkw`; no target or firmware payload execution, repository/index/jj mutation, frozen-counter edit, source-row edit, config edit, or cross-lane write. No external source rows support the F parser predicate; this scoped review opens the committed code, frozen claim, and local evidence directly. Scratch is removed after the report lands.
