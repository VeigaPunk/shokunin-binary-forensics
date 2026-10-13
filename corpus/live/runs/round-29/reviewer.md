# Round 29 — independent non-author PE language review

**Verdict:** Accept the declared **fixture-scoped calibration improvement**. Depth and coverage are **unchanged**. This is a comparison of authored bytes and two saved static inspection records, not an authenticated execution trace or loader test. No producer call, fixture edit, or PE execution was made for this review.

## OBSERVATION — independent byte and identity checks

Sources: `../../../fixtures/pe-r28/{fixture.exe,truth.json}`, `../../../fixtures/pe-r29/{fixture.exe,truth.json}`, `../round-28/inspection.json`, `inspection.json`, `LEDGER.md`, and the round-29 declaration in `.shokunin/revenger/LOG.md` (paths to fixtures here are relative to this report's directory). The two fixture files are each 1024 bytes. SHA-256 computed directly from the files:

| | r28 baseline | r29 candidate |
|---|---|---|
| whole-file SHA-256 | `9e1815a37778fc4aaf828f6d22d8c5154e9126614dda2f445768bf35d6ad1034` | `6cb7c33709d67f4f7e8c138d28451581c12d94af7e01afb345e97e5adb3853f5` |
| entry bytes `[576:584]` | `09 04 00 00 48 00 00 00` | `0c 04 00 00 48 00 00 00` |
| little-endian entry ID | `0x0409` = 1033 | `0x040c` = 1036 |
| payload bytes `[600:615]` | `SEV-R27-PAYLOAD` | identical |
| payload SHA-256 | `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229` | identical |

The **only** byte difference in the entire files is `(offset 576, old 0x09, new 0x0c)`; file lengths match. An in-memory substitution of baseline byte 576 yields the exact candidate file and digest. Both truth manifests' applicable SHA-256, size, IDs, and payload fields agree with these calculations; r29's `baseline_sha256`, `changed_offset`, `before_byte`, and `after_byte` also agree. The r28 manifest's earlier r27-copy construction claim was not independently reverified against r27 in this review; it is not required for the r28/r29 comparison.

Independently decoding the fixture structures: PE signature at `0x40`, PE32 optional-header magic `0x010b`, i386 machine `0x014c`, resource data-directory entry at file offset 200 points to RVA 8192, size 103; `.rsrc` maps RVA `0x2000` to raw file offset 512. The type/name/language resource entries are at file offsets 528, 552, 576 (8 bytes apiece). Their raw IDs are respectively 10, 1, and 1033/1036. The unchanged last entry's target `0x48` resolves to data entry offset 584 (16 bytes), which contains payload RVA 8280, size 15, code page 0, reserved 0; the RVA maps to payload offset 600. This confirms that the changed byte is the resource language ID, not payload or target.

## OBSERVATION — saved inspection comparison

The saved baseline Evidence ID is `ev_bb5fb8cc540834401a018a1bc021a1cab989a7226d27e122ff51bc4387f86537`; candidate Evidence ID is distinct: `ev_503af514d0af04c0d221c70948be240424911b1c27ef42e82a3c4a07c2c1bfcb`. Both saved records state provider `rea-pe-resources` version `1`, predicate `rea.analysis`, operation `inspect_pe_resources`. Each `subject.digest.sha256` and `normalized_result.artifact.sha256` equals the independently computed SHA-256 for its respective fixture; subject, artifact, parameters and location paths refer to the corresponding r28/r29 fixture; normalized artifact sizes are both 1024.

Each normalized result contains **exactly one** resource, index 0, type `{kind:id,id:10}`, name `{kind:id,id:1}`, with language `{kind:id,id:1033}` (r28) or `{kind:id,id:1036}` (r29). Both give entry locations `(528,8), (552,8), (576,8)`, data-entry `(584,16)`, payload RVA 8280, location `(600,15)` and the identical computed payload SHA-256 above; code page and reserved are zero. Both report PE32, machine 332, directory RVA 8192, location `(512,103)`, data-directory location `(200,8)`, directories at `(512,24), (536,24), (560,24)`, each with one ID entry, and `coverage={status:complete,examined_entries:3,resources:1}`. Direct recursive JSON comparison found **no unreported changed normalized fields**: within `normalized_result`, differences are *only* `/artifact/path`, `/artifact/sha256`, and `/resources/0/language/id`. Outside it, differences are the Evidence ID, subject digest/path, parameters path, and artifact-location path. All other JSON values, including provider, operation, limitations, confidence, authority, raw-result null and coverage, compare equal.

The ledger's eleven listed checks agree with this independent comparison. All eight wave-1 reports were read: `oracle.md`, `entry-map.md`, `identity.md`, `prior.md`, `route.md`, `score.md`, `limits.md`, `history.md`. Their baseline/oracle claims agree where applicable. Their own scope limits matter: several assessed only r28 or an in-memory candidate and did **not** establish the final r29 fixture/producer outcome; the direct checks above establish the fixture and saved-result comparison instead.

## INFERENCE — axis decision

- **Calibration: improved narrowly; accept.** The exact one-byte language-ID input perturbation and the distinct saved inspection agree on 1033→1036 while preserving type/name and payload mapping/digest. This newly tests this field compared with r28's payload-byte control. The evidence supports sensitivity and attribution **for this fixture pair only**.
- **Depth: unchanged.** No additional semantic relationship, execution, loader decision, or language fallback behavior was observed.
- **Coverage: unchanged.** Both records use the existing `inspect_pe_resources` route on closely related authored PE32 fixtures; there is no new route or demonstrated broad parser completeness. No observed harm to these axes.

## UNKNOWN — provenance and external behavior

The saved JSON is not an independently authenticated producer transcript: `raw_result` is null, and the ledger's `npx -y rea-agents@6.4.0 inspect-pe-resources ... --format json`, exit-zero and combined-output claims cannot be verified from the two saved JSON files alone. A distinct recorded Evidence ID is not by itself cryptographic proof that the command ran or that outputs were generated independently; this review did not rerun the producer. The parser's stated `coverage.status=complete` applies only to its reported inspection, not all possible PE resources or variants. Windows loader language fallback/selection, whether the binary executes or requests/loads this resource, PE parser behavior on other files, and original native-provider readiness remain unknown. No claim here extends beyond static bytes and saved records.
