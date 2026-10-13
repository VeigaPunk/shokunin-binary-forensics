# Round 30 boundary — proposed resource name-ID 1→2

## Scope and evidence reviewed

Read-only review of the saved round-29 inspection and the round-29 fixture; no REA invocation, execution, or fixture modification. Sources:

- `.shokunin/revenger/corpus/live/runs/round-29/inspection.json` — Evidence `ev_503af514d0af04c0d221c70948be240424911b1c27ef42e82a3c4a07c2c1bfcb`.
- `.shokunin/revenger/corpus/fixtures/pe-r29/fixture.exe` and adjacent `truth.json`.
- Round-30 declaration in `.shokunin/revenger/LOG.md` (the proposed name-ID mutation at file offset 552).

## Direct observations

- The fixture is 1024 bytes; computed SHA-256 is `6cb7c33709d67f4f7e8c138d28451581c12d94af7e01afb345e97e5adb3853f5`. It agrees with both saved inspection digest fields and the r29 truth manifest.
- At file offset 552 (`0x228`), the name-level 8-byte resource entry is `01 00 00 00 30 00 00 80`: its first DWORD is integer ID 1; its second DWORD points to a subdirectory at resource-relative offset `0x30`. The saved inspection locates this entry at offset 552 and reports resource name `{kind: "id", id: 1}`.
- The surrounding path is represented by entries at offsets 528 (type ID 10), 552 (name ID 1), and 576 (language ID 1036). The third entry remains `0c 04 00 00 48 00 00 00`; its target is the data entry at offset 584. The saved inspection reports one resource, this same path, and payload at offset 600, 15 bytes, SHA-256 `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`.
- The fixture bytes and inspection agree on the name entry's location, ID, and child-directory pointer. The inspection reports complete coverage (three entries examined, one resource), but this is the saved normalized parser result; `raw_result` is null and it does not independently authenticate the original invocation.

## Byte-level prediction (inference, not a new observation)

If the proposal means changing only the low byte at offset 552 from `0x01` to `0x02`, leaving every other byte fixed, the name entry becomes `02 00 00 00 30 00 00 80`. Its integer name ID is then 2; the pointer remains `0x80000030`. An in-memory candidate has sole delta `(552, 1, 2)`, length 1024, and expected SHA-256 `b94d840aa7eb952474b30260bc70e092fb1db832b0aa1bc393936d8dc4ce661a`. The unchanged structural path is predicted to be type ID 10 / name ID 2 / language ID 1036, with the same child directory and payload mapping/hash. These are byte-decode predictions, not a claim that a candidate artifact exists or that a parser reported it.

## Falsification checklist for a candidate and its saved inspection

| Check | Would falsify the one-byte name-ID claim if… |
|---|---|
| Input identity | Candidate is not 1024 bytes, does not have the predicted digest, or is not byte-identical to r29 except `(552, 0x01→0x02)`. |
| Field placement/encoding | Bytes `[552:560]` are not `02 00 00 00 30 00 00 80`; in particular, the child pointer changes, the ID is not integer 2, or the entry is no longer the name-level entry. |
| Neighbor integrity | Type entry at 528 or language entry at 576 changes, or the parent directory/counts/path topology differ from the r29 fixture without explanation. |
| Data mapping | Name entry's child-directory pointer at 556 still resolves to offset 560 (resource-relative `0x30`); the child language entry's pointer at 580 continues pointing to data entry 584. Correction after independent review: the original 'Data-entry pointer at 556' label was wrong; its numeric resolution was right. Any unintended pointer/directory changes falsify the single-field mutation. |
| Payload preservation | Bytes `[600:615]`, payload RVA/size, or payload digest differ from r29; expected payload digest is `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`. |
| Parser identity | A fresh static result for the candidate reports name ID other than 2, changes type/language or payload attribution, or fails to account for the expected resource (subject to an independently diagnosed parser error). |
| Evidence attribution | Candidate result's artifact digest/size do not bind to the candidate bytes, or evidence identity is reused in a way inconsistent with a new artifact/result. |

The first five checks are byte-level checks; the parser/evidence checks require a candidate inspection record. The saved r29 inspection is a baseline, not evidence about the proposed candidate.

## Limits: static observation vs unknown behavior

The available evidence supports a static mapping of resource directory entries and payload location for this small authored fixture. A byte-level name-ID substitution predicts a different numeric name key while preserving the existing child pointer. It does **not** prove that a Windows loader accepts the modified PE, that a caller requests/selects ID 2, or that any resource is loaded or displayed. No language/name fallback, application behavior, decoding of the opaque non-icon payload, or general parser correctness is established. A future parser result can establish only what that static parser reports for the exact candidate digest; it does not establish runtime semantics.
