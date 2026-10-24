# R63ScoutArchive — C1 archive recon

Scout only. No files under `corpus/` changed. No tools installed. Fixture reads were `hashlib` + `zipfile.ZipFile.infolist` (central directory only; nothing executed).

Confidence: high on tables below (parsed JSON and on-disk bytes). `[INFERENCE]` marks the two judgments.

## Fixture truth (declared members)

On-disk SHA-256 matches each truth root. None of the three truths declare local-header offsets or EOCD fields. Byte CD columns are from this read, not from `truth.json`.

### `corpus/fixtures/archive-r2/truth.json`

Root `archive_sha256` `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e`, `archive_size` 2964. `source_binary_sha256` equals `bin/checksum`. Fields present: path, size, compressed_size, sha256. Absent: ordinal, crc32, local-header offset, EOCD.

| path | size | compressed | sha256 | byte local offset | byte CRC-32 |
|---|---:|---:|---|---:|---|
| bin/checksum | 16160 | 2668 | `f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0` | 0 | `b3df9ea7` |
| README.txt | 84 | 78 | `7d8f6a8de39432f4119f0139c5ef5970c84c23520cfe6b40d19a3653081804d3` | 2710 | `72a557b1` |

EOCD at 2942: disk entries 2, total entries 2, cd_size 114, cd_offset 2828, comment_len 0, no trailing bytes. Truth array order matches this CD order, but the file does not label an ordinal.

### `corpus/fixtures/nested-r11/truth.json`

`outer_sha256` `e1019438fe540d611b8f44207ae858d9347ac4a1784fde8aedf835760198481c`, size 3198. `inner_sha256` / `inner_size` equal archive-r2's archive hash and 2964. `marker_literal` is present. Member fields: path, size, compressed_size, sha256. Absent: ordinal, crc32, local-header offset, EOCD, and the inner leaves `bin/checksum` / `README.txt`.

| path | size | compressed | sha256 | byte local offset | byte CRC-32 |
|---|---:|---:|---|---:|---|
| payload/inner.zip | 2964 | 2905 | `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e` | 0 | `21e1d34d` |
| marker.txt | 68 | 65 | `b8437294700e7425956f92569127ebed5ac6b679be96fa52ee4b903711917095` | 2952 | `37107941` |

EOCD at 3176: entries 2/2, cd_size 119, cd_offset 3057, comment_len 0, no trailing bytes.

### `corpus/fixtures/duplicate-r15/truth.json`

`archive_sha256` `6cad12035be32a28223307744d4fd4b4998a275462821b70b5855528bb753ddf`, size 357. Richest of the three: ordinal, path, size, compressed_size, crc32, sha256. CRC values match the bytes. Absent: local-header offset, EOCD. Literals live in `README.md`, not in truth.

| ord | path | size | compressed | crc32 | sha256 | byte local offset |
|---:|---|---:|---:|---|---|---:|
| 0 | same.txt | 17 | 19 | `def64bf3` | `7cad0d5665be7b1f1c29e4c6e2ce70c57c03e32e3bee20c4d09eb3b8115520fa` | 0 |
| 1 | same.txt | 18 | 20 | `29e6da2f` | `0f2c2afb6ab1dc3fb6bb36fb58e520d2a3557a688e9cbbea82836b5d37c1097a` | 57 |
| 2 | marker.txt | 14 | 16 | `cbeb881c` | `764be4e93ae36094345b79dcea5fd2934487d63a541c311fce14f52408ee3420` | 115 |

EOCD at 335: entries 3/3, cd_size 164, cd_offset 171, comment_len 0, no trailing bytes.

## Saved records (`inspect_artifact` / `inventory_artifact`)

`rglob` under `corpus/live` for those two strings: 23 JSON files, all `json.loads` successfully. Only four files are archive inspections. One more is the duplicate-name failure. The other 18 only contain `inventory_artifact_id` inside JavaScript/trace/compare payloads (not archive operations).

`normalized_result parses` means the key is present and its value is a JSON object.

| record | operation | evidence_id | root sha256 | normalized_result |
|---|---|---|---|---|
| `corpus/live/runs/20261012T164246Z/artifact-inspection.json` | `inspect_artifact`; substep `inventory_artifact` status `completed`, evidence `ev_cc681c2a03da4e9901275c1425fb1f726cca78bbdbec3defb13b6a0ac8ad156b` | `ev_5cc39f356009773bb3d8a214ec39536a99f0799f6709f4cd7bb3badb33c6cf7d` | `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e` (zip, 2964) | yes |
| `corpus/live/runs/round-11/outer-inspection.json` | `inspect_artifact`; substep `inventory_artifact` `completed`, evidence `ev_7bf3ed12dd6277e10be323db9b11fb89194a5fbae7a9887b98b5de95d9ceff3c` | `ev_4ed00a76eb549fde378cae6197a96b608cc6173db63144270912fad850953313` | `e1019438fe540d611b8f44207ae858d9347ac4a1784fde8aedf835760198481c` (zip, 3198) | yes |
| `corpus/live/runs/round-11/inner-inspection.json` | `inspect_artifact`; substep `inventory_artifact` `completed`, **same** inventory evidence `ev_cc681c2a…ad156b` and graph sha `52ec1a7c00c4b8d00f2196c45d9728f7b9ca0a2b5875c87a0530f9b8f6d30028` as the archive-r2 record | `ev_e622426d9def5309f4f5dd273d01424b7b50c9598e4c78248fbd00d82e6ac9fd` | `857989f5…933be27e` (zip, 2964) | yes |
| `corpus/live/runs/20261012T163909Z/artifact-inspection.json` | `inspect_artifact`; substep `inventory_artifact` `completed`, evidence `ev_ad931089830ba05c0b3d7b1b3b9021826963bd5e66bd5638cfd23c50489309a8` | `ev_dd509246a007f8e57b150678116da8895e0bea842093bb56aca525f1b886ab2c` | `f5ba0697…84897d0` (**elf**, 16160; checksum-r1, not a zip) | yes |
| `corpus/live/runs/round-15/inspection.json` | no top-level operation; `details.operation` = `inspect_artifact` | none | none | **no** (key absent; error object) |

Archive-r2 and inner inventories agree with archive-r2 truth on both leaves: `README.txt` 84/78/`7d8f6a8d…`, `bin/checksum` 16160/2668/`f5ba0697…`, `hash_status` `verified`. Outer agrees with nested truth: `marker.txt` 68/65/`b8437294…`, `payload/inner.zip` 2964/2905/`857989f5…`, format zip, not expanded. All three zip inventories set `source_location` null (no offset) and do not record CRC-32. Stated limit: central-directory entries only; trailing bytes are not occurrences. `coverage.status` is `complete-within-substeps`.

REA `edges[].ordinal` is not CD order. Archive-r2 record: README.txt = 0, bin/checksum = 1; bytes are the reverse (checksum at 0, README at 2710). Outer record: marker.txt = 0, payload/inner.zip = 1; bytes are the reverse.

Round-15 body: `artifact_operation_failed` / `execution_failure`, message `Artifact path collision: same.txt`, `retryable` false. No Evidence ID, no inventory.

Non-archive rglob hits (do not ground C06): `20261012T164357Z/analysis.json`, `round-6/view-request.json`, `round-7/comparison.json`, `round-7/comparison-request.json`, `round-7/v2-analysis.json`, `round-9/trace.json`, `round-9/trace-request.json`, `round-9/trace-exact.json`, `round-9/trace-exact-request.json`, `round-12/v1-analysis.json`, `round-12/v1-direct-analysis.json`, `round-12/v2-analysis.json`, `round-12/v2-direct-analysis.json`, `round-12/comparison-request.json`, `round-12/comparison-default-request.json`, `round-12/comparison-direct-request.json`, `round-14/trace-request.json`, `round-18/trace-request.json`. Top operations, where present, are `analyze_javascript_application`, `compare_application_versions`, or `trace_application_feature`. Request payloads have no `evidence_id` and no `normalized_result`. `round-11/outer-extraction.json` is not in this hit set.

## Recommendation

Rest C06 on **archive-r2 `fixture.zip` + `truth.json` + `corpus/live/runs/20261012T164246Z/artifact-inspection.json`** (`ev_5cc39f35…`, inventory `ev_cc681c2a…`).

Not because that truth is the most complete. duplicate-r15 declares more CD fields (crc32 and ordinal). archive-r2 is the only fixture whose root sha and both leaf sha256/size/compressed_size agree with a completed `inspect_artifact`/`inventory_artifact` whose subject path is the fixture itself. The frozen C1 sentence already names this pair. Name, size, compressed size, and sha256 can be checked against both truth and the record. CRC-32, local-header offset, and EOCD are in the bytes only — neither truth nor the record carries them — and REA edge ordinal must not be cited as CD order.

## Gaps that block a later nested or duplicate entry

**nested-r11.** Outer name/size/compressed_size/sha256 could support a shallow entry against `outer-inspection.json`. A C1-shaped CD entry cannot: truth has no crc32, local offset, or EOCD, and the saved record has none of those either (`source_location` null; edge ordinal opposes CD order). Inner leaves are not in nested truth. `inner-inspection.json` is not a second observation: same inventory evidence id and same graph sha as the archive-r2 record, and its subject path is `corpus/live/runs/round-11/materialized/payload/inner.zip`, not a fixture file.

**duplicate-r15.** Truth is sufficient for names, ordinals, sizes, CRC-32, and sha256 (those CRCs match the bytes) but still has no offsets or EOCD. The blocker is the saved record: `round-15/inspection.json` has no `evidence_id` and no `normalized_result`. There is no archive observation to correspond to. `[INFERENCE]` A future entry stays blocked until some other saved run actually inventories this zip; this file cannot be that run.
