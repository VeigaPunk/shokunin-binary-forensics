# Round 29 — independent falsification matrix (no producer)

Scope: define checks for the declared language-ID perturbation; do not run REA or score the new saved REA output. Target claim and constants: `.shokunin/revenger/LOG.md`, “Round 29 declaration” (offset 576, `09→0c`, language 1033→1036, payload expected unchanged). Source manifest: `.shokunin/revenger/corpus/fixtures/pe-r28/truth.json`. Baseline saved record: `.shokunin/revenger/corpus/live/runs/round-28/inspection.json`, Evidence `ev_bb5fb8cc540834401a018a1bc021a1cab989a7226d27e122ff51bc4387f86537`; its resource `entry_locations` identify language entry at file offset 576, 8 bytes, and payload at offset 600, 15 bytes. Candidate source bytes: `.shokunin/revenger/corpus/fixtures/pe-r29/fixture.exe`; candidate manifest: `.shokunin/revenger/corpus/fixtures/pe-r29/truth.json`. Candidate result pointer only (not assessed here): `.shokunin/revenger/corpus/live/runs/round-29/inspection.json`; run ledger: `.shokunin/revenger/corpus/live/runs/round-29/LEDGER.md` (author claims are not independent verification).

## Raw-byte verification commands

From repository root (`/home/vgpnk/Projects/prymeagnt/revenger`), these read files only and verify the authored byte oracle; they do not invoke REA:

```sh
sha256sum .shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe .shokunin/revenger/corpus/fixtures/pe-r29/fixture.exe
python -c 'from pathlib import Path; import hashlib; a=Path(".shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe").read_bytes(); b=Path(".shokunin/revenger/corpus/fixtures/pe-r29/fixture.exe").read_bytes(); d=[i for i,(x,y) in enumerate(zip(a,b)) if x!=y]; print("sizes",len(a),len(b),"deltas",[(i,a[i],b[i]) for i in d]); print("language-entry-bytes",a[576:584].hex(),b[576:584].hex()); print("payload",a[600:615].hex(),b[600:615].hex()); print("payload-sha256",hashlib.sha256(a[600:615]).hexdigest(),hashlib.sha256(b[600:615]).hexdigest())'
```

Expected oracle from the manifest: both files 1024 bytes; sole difference `(576, 9, 12)`; entry bytes `0904000048000000` → `0c04000048000000` (language ID is low 16-bit value, little-endian); payload bytes/digests remain identical, digest `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`. Whole-file hashes expected: r28 `9e1815a37778fc4aaf828f6d22d8c5154e9126614dda2f445768bf35d6ad1034`; r29 `6cb7c33709d67f4f7e8c138d28451581c12d94af7e01afb345e97e5adb3853f5`.

## Falsification matrix

| Test | Evidence / exact comparison | Falsifies the narrow claim if… |
|---|---|---|
| Source delta | r28 and r29 fixture raw bytes; above command; truth manifests’ `changed_offset`, `before_byte`, `after_byte` | size differs, changed offsets are not exactly `[576]`, or values are not `09→0c` |
| Mutation interpretation | r28 saved inspection `resources[0].entry_locations[2]` (offset 576); raw bytes `[576:578]`; r28/r29 truth `resource_language_id` | offset is not the declared language ID field or little-endian value does not change `1033 (0x0409)`→`1036 (0x040c)` |
| Input identity | SHA-256 command and each manifest `sha256`, `baseline_sha256`, `size` | computed identities/sizes disagree with manifests or expected values above |
| Payload control | raw bytes `[600:615]`, SHA-256; r28/r29 truth `payload_file_offset`, `payload_bytes`, `payload_sha256`; baseline inspection resource payload location/hash | payload bytes or digest change, or source offset/length is not 600/15 |
| Baseline parser anchor | r28 inspection `evidence_id`, `subject.digest.sha256`, `normalized_result.resources` | baseline does not bind the r28 input digest and report one type 10/name 1/language 1033 resource with language-entry offset 576 and payload offset/length 600/15 |
| Candidate parser response (not evaluated) | candidate saved inspection path above; compare `evidence_id`, `subject.digest.sha256`, `normalized_result.resources[0]` against baseline and raw-byte oracle | no distinct Evidence ID; wrong file digest; resource count/type/name/language differs from exactly 1 / 10 / 1 / 1036; or payload offset/length/hash differs from 600/15/the baseline payload digest |
| Attribution and scope | both records’ provider/operation and normalized resource fields; ledger is author narrative only | records are not comparable same static operation, or any required identity/location relationship cannot be independently reproduced |

## Classification

**OBSERVATION:** The round-29 declaration specifies a single language-field byte change and names the expected unchanged resource payload. The baseline saved record reports a resource language-entry location at offset 576 and payload location at offset 600, length 15. These are pointers to static metadata and a saved parser record, not loader behavior.

**INFERENCE:** If each matrix condition passes, the paired static records would support only fixture-scoped sensitivity to this language-ID change while preserving reported payload attribution. A changed reported language alone is insufficient absent byte identity, distinct Evidence ID, same resource mapping, and unchanged payload checks.

**UNKNOWN:** This report does not run the producer or validate the candidate inspection/Evidence ID, candidate hashes, author invocation, or exit status. It makes no claim about Windows language fallback, loading, execution, general PE correctness, or native-provider readiness. Any unverified matrix item remains unknown, not passed.
