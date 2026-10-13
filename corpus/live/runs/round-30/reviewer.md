# Round 30 independent non-author review — PE name ID

**Decision:** admit the narrow, fixture-scoped calibration move, subject to the producer-receipt caveat below. No REA producer call or target execution was performed in this review. I read the r29/r30 fixtures, truths, saved inspections, r30 oracle/boundary/ledger and the Round 30 LOG declaration.

## Independent byte oracle

Both files are 1,024 bytes. Independently calculated SHA-256 is r29 `6cb7c33709d67f4f7e8c138d28451581c12d94af7e01afb345e97e5adb3853f5` and r30 `b94d840aa7eb952474b30260bc70e092fb1db832b0aa1bc393936d8dc4ce661a`. The exhaustive byte comparison finds **only** file offset 552, `01→02`; both truth manifests agree. Bytes `[600:615)` in both are `SEV-R27-PAYLOAD`, SHA-256 `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`.

Independent PE32 decode: DOS `e_lfanew=64`; PE machine `0x014c`, one section, optional header `0x010b`. Resource data directory at file 200 is RVA `0x2000`, size 103. The `.rsrc` section maps RVA `0x2000` to file 512. Directory headers at file 512, 536 and 560 each have zero named and one ID entry. Entries at 528, 552 and 576 decode respectively as `(ID 10, child directory relative 0x18)`, `(ID 1→2, child directory relative 0x30)`, `(ID 1036, data entry relative 0x48)`. The high bit marks only the first two targets as subdirectories. Thus targets are 536, 560 and 584 relative to base 512. At 584 the 16-byte data entry holds payload RVA `0x2058`, size 15, code page 0, reserved 0; RVA maps to file 600. The changed DWORD `[552:556)` is the **numeric name ID**; the pointer DWORD `[556:560)` remains `0x80000030`.

## Saved REA JSON comparison

The baseline saved Evidence ID is `ev_503af514d0af04c0d221c70948be240424911b1c27ef42e82a3c4a07c2c1bfcb`; new saved ID is `ev_178f0cb2ef7b5e4f61e73e19f71cba354c44a337b998da07ee559cb93ede53df`. Both JSON documents are parseable and have the same top-level field set and consistent `inspect_pe_resources` operation/provider (`rea-pe-resources` v1), parameters other than path, `raw_result: null`, metadata, limitations, and evidence links. Their `subject.digest.sha256` and normalized artifact SHA match the corresponding independently hashed files; subject, parameters, normalized artifact and location paths consistently refer to their respective fixtures. A full recursive comparison of **all** normalized fields finds exactly three changed leaves: `artifact.path`, `artifact.sha256`, and `resources[0].name.id` (1→2). Everything else, including format `pe32`, machine 332, resource directory/data-directory locations, three directory records and counts, type 10, language 1036, all entry and data-entry locations, code page/reserved, payload RVA/offset/length/SHA, empty icon groups, and coverage `{status: complete, examined_entries: 3, resources: 1}`, is equal. The full top-level record adds only the expected changed Evidence ID, subject digest/path, parameter path and artifact-path location. Normalized and top-level limitations match in both: static inventory; non-icon payload opaque; no language fallback, image decoding or shell/window loading observation; overlapping non-identical structures rejected.

## Eleven ledger checks

| Check | Independent disposition |
|---|---|
| `exit_zero` | **Producer receipt only, not independently verified.** The LEDGER says CLI exit 0, but saved JSON does not encode or authenticate process exit status, command execution or empty stderr. No producer call was allowed here. |
| `new_evidence_id` | **Verified in saved JSON:** distinct nonempty IDs above; distinctness does not independently authenticate how they were produced. |
| `source_sha` | **Verified:** independently hashed r29 file matches truth, saved subject and normalized artifact. |
| `new_sha` | **Verified:** independently hashed r30 file matches truth, saved subject and normalized artifact. |
| `sole_byte_552` | **Verified:** full file byte comparison gives only `552: 0x01→0x02`. |
| `baseline_resource_name` | **Verified:** r29 entry decodes ID 1; baseline normalized record reports ID 1. |
| `new_resource_name` | **Verified:** r30 entry decodes ID 2; new normalized record reports ID 2. |
| `type_and_language` | **Verified:** unchanged raw path ID 10 / ID 1036; both records agree. |
| `payload_identity` | **Verified:** unchanged data mapping and independently hashed `[600:615)` agree with both saved payload records. |
| `all_other_normalized_equal` | **Verified:** exhaustive recursive comparison has only artifact path/SHA and name ID changes. |
| `record_structure` | **Verified for both saved JSON records:** parseable, same keys/expected operation/provider, consistent artifact attribution, preserved limitation text. This does not verify producer invocation. |

Thus **10/11 are independently checkable and pass; `exit_zero` remains an unverified producer receipt**, not a falsified claim. The ledger's 11/11 describes its local checks, not eleven independently authenticated checks. The oracle and LOG's byte prediction agree with the actual fixture and inspection. Boundary.md has a labeling error in its *Data mapping* checklist: “Data-entry pointer at 556” is the **name entry's child-directory pointer**, not a data-entry pointer. Its `0x30→560` resolution is correct. The language entry pointer at 580 leads to the data entry at 584; that data entry's payload RVA field begins at 584. Boundary.md was not altered.

## Axis judgment and limits

- **Calibration: improved**, narrowly: changing only a verified numeric name ID changes only the saved parser's name ID and artifact identity, while payload attribution stays fixed. This adds name-field sensitivity beyond the r29 language-field control. The admission uses the saved-record comparison plus independent raw bytes, not independent proof of the CLI receipt.
- **Depth: unchanged:** no new payload semantics, runtime loader/caller behavior or native disassembly.
- **Coverage: unchanged:** same one-resource static PE inspection route; complete coverage is the saved parser's claim for this tiny fixture, not coverage of arbitrary PEs.

No axis is shown harmed. Saved JSON cannot by itself authenticate the producer's exit status, original invocation, or general parser correctness. The original Ghidra/IDA/Hopper provider refusal remains unresolved; no Windows loader behavior or PE execution is established.
