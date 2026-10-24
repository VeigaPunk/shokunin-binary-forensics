# W2ReopenS033 — S033 own-work row vs committed bytes

**Verdict: CONFIRMS.** No mismatch. Lane tip `db55bd6488e24e956df5818ae34c2a043d7ddc12` (integration after build `2a34e45562d965f9c8d32f6a27d2f2efa2e7d04e`). The S033 line in `corpus/SOURCES.md` is byte-identical in the worktree and at `HEAD` (1261 chars, 11 cells). The three anchored files have the same git blob at base `55bcb6e1aeb4d42923a4e98db6580f67142b41ac`, at `2a34e455…`, at `HEAD`, and in the worktree.

Axes checked: anchor digest/id fidelity; both member digests from a raw central-directory walk; teaches sentence against those bytes.

No tools installed.

## Row under attack

`corpus/SOURCES.md` S033 (own-work, tier A, mined, opened 2026-10-23, recheck on-release).

- **source:** `corpus/fixtures/archive-r2/fixture.zip`, `corpus/fixtures/archive-r2/truth.json`, `corpus/live/runs/20261012T164246Z/artifact-inspection.json`
- **scope:** those bytes at base `55bcb6e1aeb4d42923a4e98db6580f67142b41ac`; correspondence only, not provider accuracy or completeness
- **anchor:** fixture sha256 `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e`; truth.json sha256 `7df773bf46b7c1273f8c3402b7825e7dacbb7f990c7d7ef41f30917c94726e68`; saved record sha256 `2fec924b5217885674149b6a516970f419a8e731c8e6e49eab178a4f065f3380`; Evidence `ev_5cc39f356009773bb3d8a214ec39536a99f0799f6709f4cd7bb3badb33c6cf7d`; nested `ev_cc681c2a03da4e9901275c1425fb1f726cca78bbdbec3defb13b6a0ac8ad156b`
- **teaches:** "A byte readout of one archive's central directory can be checked field by field against an independent oracle and against one saved record's literal fields, without claiming the record is complete or authentic."

## Recomputed (raw `struct` + `zlib.decompress(..., -15)`, not `zipfile`)

| claim | row / task | bytes | result |
|---|---|---|---|
| fixture sha256 | anchor | `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e` | match |
| fixture size | task (not an anchor cell) | 2964 | match to file and to `truth.json` `archive_size` |
| truth.json sha256 | anchor | `7df773bf46b7c1273f8c3402b7825e7dacbb7f990c7d7ef41f30917c94726e68` (728 bytes) | match |
| saved-record sha256 | anchor | `2fec924b5217885674149b6a516970f419a8e731c8e6e49eab178a4f065f3380` (7692 bytes) | match |
| evidence_id | anchor | top-level `evidence_id` `ev_5cc39f356009773bb3d8a214ec39536a99f0799f6709f4cd7bb3badb33c6cf7d` | match |
| nested evidence_id | anchor | `normalized_result.substeps[0].evidence_id` `ev_cc681c2a03da4e9901275c1425fb1f726cca78bbdbec3defb13b6a0ac8ad156b` | match |
| root sha256 | task (not a separate anchor token) | occurrence `logical_path` `.` → node `art_8307324c337aaa39634e6d004da5c50e9420e95504f68c6d70b36dfb274e90e0` sha256 `857989f5…be27e`, size 2964; same value at `subject.digest.sha256` | equals recomputed fixture digest |

Central directory: EOCD at offset 2942, signature `0x06054b50`, 2 entries, CD at 2828 size 114, comment length 0. Both members, method 8, GP bit 3 clear:

| member | local header | inflated sha256 | size | compressed | crc32 |
|---|---|---|---|---|---|
| `bin/checksum` | 0 | `f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0` | 16160 | 2668 | `b3df9ea7` |
| `README.txt` | 2710 | `7d8f6a8de39432f4119f0139c5ef5970c84c23520cfe6b40d19a3653081804d3` | 84 | 78 | `72a557b1` |

Local-header name equals the central-directory name for both. Inflated length equals the central-directory uncompressed size. Recomputed CRC-32 equals the central-directory CRC-32. `truth.json` `members[]` (`path`, `size`, `compressed_size`, `sha256`) equals those values; name-set delta is empty. Saved occurrences `bin/checksum` and `README.txt`: `logical_path`, `declared_size`, `compressed_size`, and the pointed node's `sha256`/`size` equal the same values. The only saved path that is not a member is `.` (the root).

Git blobs (base = build commit = HEAD = worktree): fixture `91935330bc627690f8696c76a743c4d02bf5554c`; truth `5619a978a3203e22ac77058bc0697d713e98c517`; record `7d5e9d0ac5dce31f00e181e859d6f813920bdd59`.

## Teaches sentence

The sentence is what those bytes show, not a stronger claim:

- Shared fields check: central-directory name, uncompressed size, and compressed size match the oracle and the saved record's literal fields; the oracle's and the node's sha256 match the digest recomputed over each inflated local-header payload.
- The disclaimer holds: the record's own `limitations` say the inspection does not execute the artifact or claim format-specific semantics, and that the ZIP inventory lists central-directory entries only. The row's scope cell already excludes provider accuracy and completeness. CRC-32 is a central-directory field and matches the inflated bytes, and it is absent from both the oracle and the saved occurrences — the sentence does not claim those documents store every central-directory field.

## Not a mismatch

- The anchor does not print fixture size or the two member digests; both were recomputed and agree with `truth.json` and the saved nodes.
- `LEDGER.md` is not in the S033 source cell. This reopen did not treat the knowledge entry's extra ledger citation as part of the registry row.

## Unknowns

None for the assigned check. Provider accuracy and completeness stay outside the row's scope and were not tested.
