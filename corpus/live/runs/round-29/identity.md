# Round 29 identity and mutation oracle (independent LEAF)

## Scope

Read-only computation from `.shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe`, its `truth.json`, and the round-28 saved inspection. No fixture was changed or created; no REA call or execution was made.

## OBSERVATION

- `fixture.exe` is 1024 bytes; raw SHA-256: `9e1815a37778fc4aaf828f6d22d8c5154e9126614dda2f445768bf35d6ad1034`.
- Baseline payload is file bytes `[600:615]` (15 bytes), ASCII `SEV-R27-PAYLOAD`; SHA-256 `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`.
- At file offset 576, the raw language ID bytes are `09 04`, i.e. little-endian `0x0409` / decimal 1033. The full four bytes at `[576:580]` are `09 04 00 00`. Offset 576 is the third resource directory entry location in the saved r28 record (see below).
- Applying the declared mutation in memory only—replace byte at offset 576 from `0x09` to `0x0c`—produces `0c 04 00 00` there, i.e. language ID `0x040c` / decimal 1036. All other bytes remain identical. Expected 1024-byte mutated-file SHA-256: `6cb7c33709d67f4f7e8c138d28451581c12d94af7e01afb345e97e5adb3853f5`.
- The mutation leaves bytes `[600:615]` identical; expected payload SHA-256 remains `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`.

## Evidence pointers

- Round claim and constants: `.shokunin/revenger/LOG.md`, “Round 29 declaration — calibration (2026-10-13)”. It specifies offset 576 `0x09→0x0c`, expected type 10/name 1/language 1036 and unchanged payload offset 600/length 15/digest.
- Source bytes and authored baseline identity: `.shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe`; companion `.shokunin/revenger/corpus/fixtures/pe-r28/truth.json` records whole-file SHA, size, payload identity and prior change at offset 600.
- Saved baseline inspection: `.shokunin/revenger/corpus/live/runs/round-28/inspection.json`, Evidence `ev_bb5fb8cc540834401a018a1bc021a1cab989a7226d27e122ff51bc4387f86537`. Its normalized result reports artifact digest/size, one resource type ID 10/name ID 1/language ID 1033, `entry_locations` offsets 528/552/576, and payload location offset 600 length 15 plus digest. This is a saved result, not independent proof of invocation.

## Reproduction (read-only; performs mutation only in memory)

From repository root:

```sh
python3 -c 'from pathlib import Path; import hashlib; p=Path(".shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe"); b=p.read_bytes(); assert len(b)==1024 and hashlib.sha256(b).hexdigest()=="9e1815a37778fc4aaf828f6d22d8c5154e9126614dda2f445768bf35d6ad1034"; assert b[576:580]==bytes.fromhex("09 04 00 00"); assert b[600:615]==b"SEV-R27-PAYLOAD"; m=bytearray(b); m[576]=0x0c; assert [(i,x,y) for i,(x,y) in enumerate(zip(b,m)) if x!=y]==[(576,0x09,0x0c)]; print("mutated_sha256",hashlib.sha256(m).hexdigest()); print("payload_sha256",hashlib.sha256(m[600:615]).hexdigest()); print("language_bytes",m[576:580].hex(" "))'
```

## INFERENCE

If the claimed single-byte mutation is used, the expected static resource-language identity changes from 1033 to 1036 while the file identity changes and payload bytes/digest stay fixed. This is an exact raw-byte oracle for the declared mutation, not an observed r29 fixture or parser result.

## UNKNOWN

No r29 fixture, r29 Evidence record, or parser outcome was examined or generated here. Whether a later result has a new Evidence ID, recognizes exactly the expected resource tuple, preserves payload mapping/digest, or faithfully attributes the producer invocation remains unverified. No loader, language fallback, or runtime behavior is established.
