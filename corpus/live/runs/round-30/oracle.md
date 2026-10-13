# Round 30 oracle — PE resource name-ID sensitivity

Independent raw-byte check of `corpus/fixtures/pe-r29/fixture.exe` against the existing fixture truth and round-30 truth/inspection records. No REA producer was called.

- Both fixtures are 1,024 bytes. SHA-256: r29 `6cb7c33709d67f4f7e8c138d28451581c12d94af7e01afb345e97e5adb3853f5`; expected r30 `b94d840aa7eb952474b30260bc70e092fb1db832b0aa1bc393936d8dc4ce661a` (matches the existing r30 truth and inspection artifact digest).
- Direct byte comparison confirms exactly one difference: file offset **552**, `0x01` → `0x02`. This is the first DWORD of the resource-name directory entry at file offset 552 (8-byte entry within the directory at 536). In an ID entry, that DWORD is the numeric resource name: r29 ID **1**, r30 ID **2**. The second DWORD `0x80000030` is unchanged and points to the next-level directory at file offset 560.
- Resource type entry at file offset 528 retains ID **10**; language entry at 576 retains ID **1036**. Data entry at file offset 584 specifies payload RVA `0x2058` (file offset **600**) and size **15** bytes; payload occupies `[600, 615)` (last byte offset 614). Payload bytes are `SEV-R27-PAYLOAD`; SHA-256 `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`, unchanged.
- The existing r29 and r30 truth records agree with these hashes, offset, before/after bytes, resource IDs, and payload boundaries/hash. The saved r30 normalized inspection likewise reports type 10, name 2, language 1036 and payload location 600/length 15 with the same payload hash.

**Oracle:** the controlled fixture change is exactly the one-byte numeric resource-name ID change at offset 552 from 1 to 2. No other file byte or payload byte changes. This is a static fixture-level conclusion, not a claim about Windows loader behavior.
