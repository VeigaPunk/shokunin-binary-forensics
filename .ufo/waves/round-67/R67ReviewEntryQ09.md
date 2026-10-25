Q09 PASS — every digest is claimed only for the exact bytes hashed; no origin/completeness/authenticity claim; dex checksum/signature explicitly framed as inert declared-header self-consistency, validity disclaimed.

Scope: `corpus/knowledge/round-67-apk-axml-byte-evidence.md` (LANDED v2 candidate) against `corpus/QUALITY.md:21` (Q09, M11/M13). Fresh-seat decision on the committed bytes; all commands run from `/home/vgpnk/Projects/shokunin/revenger-shokunin`.

## Digest claims — each verified over the exact bytes named

| entry claim | pointer | verification command → actual output |
|---|---|---|
| fixture sha256 `05d2280f…afe7d03e`, 947 bytes | entry:20,24 | `sha256sum corpus/fixtures/apk-r65/fixture.apk` → `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`; `wc -c` → `947` |
| truth.json sha256 `27303bae…f4b8173` | entry:4 | `sha256sum corpus/fixtures/apk-r65/truth.json` → `27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173` |
| readout.py sha256 `92e347c3…c13976` | entry:4,16,166 | `sha256sum corpus/fixtures/apk-r65/readout.py` → `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976` |
| readout stdout sha256 `507d79f8…dad247`, 15 lines | entry:6,166 | `python3 -B corpus/fixtures/apk-r65/readout.py \| sha256sum` → `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247`; `wc -l` → 15; exit 0 |
| member payload sha256s (AXML `73d1e0f2…`, dex `57cfe887…`, MANIFEST.MF `2e5da249…`) | entry:38,40,42 | recomputed inside the verified readout run above — each is a digest of the member's own payload bytes, nothing more |

## Q09 reject-condition sweep (a hash as proof of origin / completeness / valid interpretation)

- **No origin claim.** Hashes pin "the committed bytes" (entry:124,149); the fixture is described as "authored" by the oracle/build recipe (S041 own-work), never as authenticated-by-hash. No producer identity is derived from any digest.
- **No completeness claim.** Item 3 (entry:34) states the CD walk "selects three members" — positional enumeration from stated CD offsets, not hash-backed completeness; "no framework-wide semantics … is claimed" for zero resource-map entries (entry:74).
- **No authenticity/validity claim.** Item 9 (entry:106): "These are declared-header self-consistency facts about one inert member; dex validity is not claimed" — the declared checksum `0x3d120c30` and 20-byte signature are each reported only as equal to the Adler-32/SHA-1 recomputed over the specified byte ranges, per S045's field-table quotes. §Limitations (entry:134): "the dex member is a header only and is intentionally not a valid dex program." §Unknown (entry:130): "nothing about install validity, signature blocks, dex program validity … is claimed."
- **ZIP CRC-32s** (entry:34,38,40,42) are internal consistency only — "stated CRC-32 equals the CRC-32 recomputed over its payload bytes"; no integrity-provenance inference.
- **Saved records byte-preserved.** Entry:5 claims every embedded output line was captured from actual stdout. Check: extracted entry:172-186 (the embedded full-stdout block) → `diff` vs a fresh `python3 -B corpus/fixtures/apk-r65/readout.py` run → identical, 15/15 lines.

Verdict basis: no instance of the Q09 reject condition found anywhere in the entry; every positive requirement demonstrated on the committed bytes.

OFF- none observed within this read; non-Q09 criteria deferred to their named seats.
