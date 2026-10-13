# Round 57 independent PE resource tree review

## Independent byte inspection (before REA comparison)
Commands run: Python read-only inspection via `Path.read_bytes()`, `hashlib.sha256`, and byte-difference enumeration on `.shokunin/revenger/corpus/fixtures/pe-r55/fixture.exe` and `pe-r57/fixture.exe`. No target execution.

Observed SHA-256: r55 `41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b`; r57 `71d11fba01d4daa040e04e649a70c39bcdb475ce2e0a2801f6171a325db0494d`. Both are 1536 bytes; exhaustive byte comparison found exactly one differing offset: 924, changing 48 (`0x30`) to 47 (`0x2f`). Resource directory at file offset 512, size 240. Entries: RT_ICON id 1/lang 1033 data entry 672, payload offset 768 size 48, SHA-256 `d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003`; RT_ICON id 2/lang 1033 data entry 688, payload offset 832 size 48, SHA-256 `2f503cace29956c75acd5356de2f8fa98485b01edd654daf0f81a739b44c82ae`; RT_GROUP_ICON name `A😀B!` (UTF-16LE bytes `41003dd800de42002100`), lang 1033, data entry 704, payload offset 896 size 34. The two payload hashes and bytes are unchanged between fixtures.

Group image entries begin at offsets 902 and 916. First: 1x1, declared bytes 48, ID 1. Second: 2x2, declared bytes 48 in r55 and 47 in r57, ID 2. Offset 924 is second entry declared-size field. Thus the sole byte mutation is exactly that field; IDs and icon candidates [resource entries 0 and 1] remain intact.

## REA comparison
After independent byte inspection, read saved `.shokunin/revenger/corpus/live/runs/round-57/inspection.raw.json` and `receipt.json`. Evidence ID: `ev_068eb9b682385b760251b6d23ba70680ec57b0e55b95ce242921a3f021e1cd07`. Receipt records command `npx -y rea-agents@6.4.0 inspect-pe-resources .../pe-r57/fixture.exe --format json`, exit 0. REA tree agrees on PE32+, directory offset/length, three resources, payload offsets/sizes/hashes, Unicode group name, both image IDs/candidate indexes, and declared sizes 48/47. It reports first size_matches true and only second false. `truth.json` matches the observed fixture hashes, single changed offset and expected image relations.

## Bounded assessment
- **OBSERVATION:** The two fixture files differ only at byte 924 (48→47); unchanged icon payloads retain their observed SHA-256 values. Saved REA output reports the same resource tree and the second-only size mismatch.
- **INFERENCE:** This supports the specific round-57 claim: the second image declaration under the Unicode-named two-image group was shortened by one byte without changing either image ID or candidate relationship; REA reflects that mutation accurately.
- **UNKNOWN:** This static inspection does not establish image decoding, language fallback, or actual shell/window loading. REA itself disclaims those behaviors.

Verdict: **SUPPORTED**, bounded to static resource-table/tree attribution and byte-level fixture comparison. No execution or claims about runtime rendering.
