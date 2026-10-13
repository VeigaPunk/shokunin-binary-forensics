# Round 28 oracle — PE resource byte delta

Independent baseline review of `corpus/fixtures/pe-r27/fixture.exe` and `truth.json` (no REA producer or target execution).

## Expected result

- Baseline file: 1,024 bytes; SHA-256 `523e6dc1b8cc2b48a636ce3cb93736ce46d4c8d58c594d8d8dd2ed72ca2640bb`.
- The sole intended change is file offset **600** (`0x258`): ASCII `R` (`0x52`) → `S` (`0x53`). No insertions, deletions, or other byte changes.
- Payload at offset 600, length 15: `REV-R27-PAYLOAD` → `SEV-R27-PAYLOAD`.
- Expected changed-file SHA-256: `9e1815a37778fc4aaf828f6d22d8c5154e9126614dda2f445768bf35d6ad1034`.
- Expected changed-payload SHA-256: `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`.
- Baseline payload SHA-256: `0346b578bdfe68866acea157268520567a5d6e96a28ab8a95835569921f088aa`.

## Static resource layout

The authored PE32 truth identifies the resource data-directory field at file offset 200, resource directory RVA `0x2000` at file offset 512 (103 bytes), and one RT_RCDATA (`type 10`) / name ID 1 / language 1033 resource. Its data entry is at file offset 584; it points to RVA `0x2058`, mapped in this fixture to payload file offset 600, size 15. The directory structures and payload length stay unchanged; only the first payload byte changes. `truth.json` describes this as a hand-built PE32 with one `.rsrc` section and no compiler or execution.

I verified the expected hashes by changing only baseline byte 600 in memory. The resulting byte comparison has exactly one difference: `(600, 0x52, 0x53)`. This is a byte-level oracle, not a claim about runtime loader behavior.
