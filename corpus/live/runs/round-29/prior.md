# Round 29 prior: independent read of saved round-28 inspection

Scope: read-only baseline parse; no REA call and no fixture changes. Paths below are repository-relative to `/home/vgpnk/Projects/prymeagnt/revenger`.

## OBSERVATION

- Saved record: `.shokunin/revenger/corpus/live/runs/round-28/inspection.json`, JSON `evidence_id` `ev_bb5fb8cc540834401a018a1bc021a1cab989a7226d27e122ff51bc4387f86537`.
- Its `subject.digest.sha256` and `normalized_result.artifact.sha256` both equal `9e1815a37778fc4aaf828f6d22d8c5154e9126614dda2f445768bf35d6ad1034`; `subject.format` is `pe`, provider is `rea-pe-resources` version `1`, operation is `inspect_pe_resources`, and `confidence` is `observed`. Saved record says `raw_result: null`.
- `normalized_result` describes a 1024-byte PE32 (machine 332), resource directory RVA 8192 at file offset 512. It records one resource: type ID 10, name ID 1, language ID 1033; resource entry locations are offsets 528, 552, and 576; data-entry location is 584; payload location is offset 600, length 15, SHA-256 `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`. Coverage says complete, three entries examined, one resource.
- Raw-byte cross-check of the referenced artifact `.shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe`: size 1024; whole-file SHA-256 matches the record. At offset 576, the 8-byte entry is `09 04 00 00 48 00 00 00`: little-endian ID `0x0409` (1033), followed by relative directory offset `0x48`. The actual 15 payload bytes at offset 600 are `SEV-R27-PAYLOAD`; their digest matches the saved record.
- Reproducible read-only checks (from repository root):
  ```sh
  sha256sum .shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe
  wc -c < .shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe
  od -An -tx1 -j 576 -N 8 .shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe
  dd if=.shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe bs=1 skip=600 count=15 status=none | sha256sum
  ```
  Expected outputs: whole-file digest above; 1024; `09 04 00 00 48 00 00 00`; payload digest above. JSON claims can be checked with `jq '{evidence_id,subject,provider,operation,raw_result,normalized_result}' .shokunin/revenger/corpus/live/runs/round-28/inspection.json`.

## INFERENCE

- The saved inspection and its referenced bytes consistently identify the baseline language as 0x0409 / 1033. For the declared r29 mutation, changing only the language ID's low byte at file offset 576 from `0x09` to `0x0c` would encode 0x040c / 1036 while leaving the second DWORD (relative offset 0x48) unchanged. This is a byte-level expectation, not evidence that such a mutation was made or inspected.
- The normalized output supports a static inventory claim for this one saved artifact. Its `confidence: observed` and shipped-artifact authority are fields in the saved record; this independent read does not authenticate how the producer invocation was performed.

## UNKNOWN

- No observation here establishes the r29 fixture's bytes, digest, new Evidence ID, REA output, or whether payload identity/mapping remains unchanged after a language mutation.
- No PE loader behavior, language fallback/selection, execution, Windows resource API behavior, or parser correctness beyond the saved static record is established. The record itself explicitly limits language fallback and actual loading as unobserved; payloads other than RT_GROUP_ICON are opaque.
