# Independent byte oracle — round 57

## Procedure and byte observations
Commands: Python `Path.read_bytes()` for both fixtures; SHA-256 with `hashlib.sha256`; PE/resource offsets decoded with `struct` and direct byte slicing. No execution or producer rerun.

- r55 SHA-256 `41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b`; r57 SHA-256 `71d11fba01d4daa040e04e649a70c39bcdb475ce2e0a2801f6171a325db0494d`; each 1536 bytes.
- Bytewise comparison output: `[(924, 48, 47)]` (offset, r55 byte, r57 byte). Thus the only changed byte is offset 924, from 0x30 to 0x2f.
- Resource bytes at 896 in r57 decode as group header reserved=0, type=1, count=2, then two 14-byte entries. First entry resource ID 1, declared size 48; second entry resource ID 2, declared size 47. Entry offsets 902 and 916; size field of second entry is offset 924.
- UTF-16 name record at 736: length prefix 5, code units bytes `41003dd800de42002100`, decoding to `A😀B!` (surrogate pair D83D DE00); the named group payload is offset 896, 34 bytes. Three payloads: RT_ICON ID1 offset768/48 bytes SHA-256 `d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003`; RT_ICON ID2 offset832/48 bytes SHA-256 `2f503cace29956c75acd5356de2f8fa98485b01edd654daf0f81a739b44c82ae`; RT_GROUP_ICON offset896/34 bytes. Icon payload byte ranges are unchanged between fixtures.

## Comparison with saved REA result
Evidence ID: `ev_068eb9b682385b760251b6d23ba70680ec57b0e55b95ce242921a3f021e1cd07` (saved inspection.raw.json; receipt command `npx -y rea-agents@6.4.0 inspect-pe-resources ...pe-r57/fixture.exe --format json`, exit 0). Its normalized output reports group name `A😀B!`, two image entries in order, IDs 1 then 2, candidates `[0]` then `[1]`, same-language indices 0 then 1, declared sizes 48 then 47, and `size_matches` true then false. These agree with the direct byte observations and payload lengths above. Receipt target SHA-256 matches independently computed r57 hash.

## Bounded conclusion
**OBSERVATION:** These two files differ only at offset 924, where the second group image declared size changes 48→47. The Unicode-named two-image group and both ordered IDs/candidates remain present; the underlying two icon payloads are each 48 bytes and unchanged. Saved REA result reports only the second image as `size_matches:false`.

**INFERENCE:** The one-byte mutation accounts for the reported mismatch; it does not remove or alter either icon resource candidate.

**UNKNOWN:** This byte-level review does not establish how Windows or any application renders/uses these resources, nor behavior outside this fixture pair. No target execution was performed.
