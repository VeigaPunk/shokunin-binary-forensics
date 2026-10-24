# R63 firmware byte-oracle checker

## Changed file and behavior

- `corpus/live/runs/round-63/oracle_check.py` is the only implementation file changed by this seat.
- Default inputs are `corpus/live/runs/round-63/inspection.json` and `corpus/fixtures/firmware-r63/truth.json`; `--record` and `--truth` allow alternate inputs for reuse.
- Prints one `REGION` line for each declared truth region. Padding ranges are identified as not expected REA detections and checked against the authored fill bytes. Each zlib/gzip region is matched one-to-one against the record's normalized reported regions by `signature`, `offset`, and `reported_size`; missing, extra, duplicate/shifted rows fail with the field named. The checker also verifies image size/SHA-256, binds those values to the record's `subject.digest.sha256` and `normalized_result.input_size`, checks contiguous truth ranges, and compares decompressed member size/SHA-256 against truth.
- The saved REA result reports `normalized_result.regions` but has an empty raw `extractions` map and no decompressed hashes. Therefore member hashes in the checker are independently computed by decompressing the inert fixture bytes and compared with `truth.json`; they are not attributed to REA output.

## Evidence

The real record is `corpus/live/runs/round-63/inspection.json`, evidence ID `ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259`. It reports zlib regions at offset/size 512/79 and 1024/90. The oracle image is `corpus/fixtures/firmware-r63/firmware-r63.bin`, SHA-256 `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be`, size 2048. `corpus/live/runs/round-63/receipt.json` retains the real `npx -y rea-agents@6.5.0 inspect-firmware-regions ... --format json` command, exit 0, fixture and stdout hashes, and Evidence ID. A separate firmware-run seat performed the invocation; this seat did not install or update tools.

## Required transcripts

### Green: real saved record

Command: `python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/oracle_check.py`

```text
REGION name=padding kind=padding offset=0 size=512 record=not-expected padding=OK
REGION name=diagnostic-note kind=zlib offset=512 size=79 offset=OK size=OK signature=OK decompressed_sha256=OK (a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86)
REGION name=padding kind=padding offset=591 size=433 record=not-expected padding=OK
REGION name=component-note kind=zlib offset=1024 size=90 offset=OK size=OK signature=OK decompressed_sha256=OK (2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9)
REGION name=padding kind=padding offset=1114 size=934 record=not-expected padding=OK
ORACLE OK
EXIT=0
```

### Red: first reported offset shifted by 1

Command: `python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/oracle_check.py --record /tmp/revenger-r63-oracle-shift.json`

```text
REGION name=padding kind=padding offset=0 size=512 record=not-expected padding=OK
REGION name=diagnostic-note kind=zlib offset=512 size=79 offset=MISMATCH size=OK signature=OK decompressed_sha256=OK (a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86)
REGION name=padding kind=padding offset=591 size=433 record=not-expected padding=OK
REGION name=component-note kind=zlib offset=1024 size=90 offset=OK size=OK signature=OK decompressed_sha256=OK (2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9)
REGION name=padding kind=padding offset=1114 size=934 record=not-expected padding=OK
MISMATCH normalized_result.regions[0].offset: expected 512, got 513
ORACLE MISMATCH
EXIT=1
```

### Red: last reported region dropped

Command: `python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/oracle_check.py --record /tmp/revenger-r63-oracle-drop.json`

```text
REGION name=padding kind=padding offset=0 size=512 record=not-expected padding=OK
REGION name=diagnostic-note kind=zlib offset=512 size=79 offset=OK size=OK signature=OK decompressed_sha256=OK (a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86)
REGION name=padding kind=padding offset=591 size=433 record=not-expected padding=OK
REGION name=component-note kind=zlib offset=1024 size=90 record=MISSING offset=MISSING size=MISSING decompressed_sha256=OK (2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9)
REGION name=padding kind=padding offset=1114 size=934 record=not-expected padding=OK
MISMATCH normalized_result.regions: expected 2 reportable regions, got 1
MISMATCH normalized_result.regions[1]: missing reported region
ORACLE MISMATCH
EXIT=1
```

## Risks and blockers

- The checker validates content against the authored fixture oracle and validates region correspondence, but does not establish provenance/authenticity of either JSON file or the REA invocation; consult the saved run receipt for command and hash custody.
- It treats declared `padding` regions as image filler, not expected Binwalk detections. Current real output contains exactly the two declared zlib detections.
- No blockers. No tools were installed or updated by this seat.