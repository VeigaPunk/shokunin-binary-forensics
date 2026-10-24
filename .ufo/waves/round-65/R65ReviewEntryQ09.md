# R65ReviewEntryQ09 — Q09 decision on round-65 C05 candidate entry

PASS — every digest-bearing sentence in `corpus/knowledge/round-65-apk-axml-byte-evidence.md` resolves to exactly the bytes claimed (16/16 instances re-derived), the one APK digest is explicitly "read from the file's bytes", and the dex checksum/signature are framed as declared-header self-consistency with validity explicitly disclaimed. Two stale template pointers are dangling (`### Code`, in-document `§Sources`) — low-severity reproduction-pointer defects, not digest overclaims.

Seat: fresh Q09 reviewer. Lane root `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Read-only: no lane file edited except this report. No tools installed or upgraded; no pacman/jj/git mutation. Read-only git reads used (`git show HEAD:`, `git status --porcelain`).

## Method

Target entry at HEAD `8214e4d` (working tree clean for every path I scored): `git status --porcelain corpus/fixtures/apk-r65 corpus/knowledge/round-65-apk-axml-byte-evidence.md corpus/SOURCES.md corpus/verify_icon_languages.py corpus/verify_multi_icon_states.py` printed nothing; `git show HEAD:<path> | sha256sum` equals the working-tree hashes below. Frozen contract read first: `reports/round-65/claims.md`.

Digest re-derivations (working tree and `git show HEAD:` agree):

```
$ sha256sum corpus/fixtures/apk-r65/{fixture.apk,truth.json,generator.py,readout.py}
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  fixture.apk   (947 bytes)
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  truth.json
eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a  generator.py
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  readout.py

$ python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/r65_q09_out.txt; echo exit=$?
exit=0
$ wc -l < /tmp/r65_q09_out.txt → 15
$ sha256sum /tmp/r65_q09_out.txt
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247

$ sha256sum .ufo/waves/round-65/source-snapshots/{ResourceTypes.h,rea-android-applications.md,zipfile-docs.html}
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  ResourceTypes.h (86255 bytes)
412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c  rea-android-applications.md (34 lines)
e7fe6715126a3be8e6ea7ca4d3dc2d8713b6c979bde13f8fa9d6c458a3c49c6a  zipfile-docs.html (S040; not cited by the entry)

$ git show HEAD:corpus/knowledge/round-65-apk-axml-byte-evidence.md | sha256sum
e173e6436e9b8cce2ddd9f318b914fde6fd9bdfaf18335f5a873ac60fa3cdfb7
```

Independent member/dex re-derivation (different code path from `readout.py`: `zipfile` + `zlib`):

```
$ python3 -B  # zipfile.ZipFile(fixture.apk)
AndroidManifest.xml 416  73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4  962d075f
classes.dex         112  57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2  2635c82a
META-INF/MANIFEST.MF 69  2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49  e948d738
dex adler32(payload[12:]) = 0x3d120c30  == declared 0x3d120c30
dex sha1(payload[32:])    = a5fc7bea8fa9ffaa52243540c8026066511b9fce == declared signature
dex file_size=112 header_size=112
axml first8 = 03000800a0010000  (payload len 416)
```

Independent container arithmetic (raw `struct`, not `readout.py`): EOCD at 925, entries 3, cd_off 737, cd_size 188, `737+188=925`, trailer 0; central-directory walk ends at 925; CRCs 962d075f / 2635c82a / e948d738; local header offsets 0 / 465 / 618.

Root-invariance of the stdout digest (tests the sentence at `:5`): copied only `fixture.apk` + `readout.py` to `/tmp/q09copy`, ran from `/`, output byte-identical to the lane-root run (`diff` empty, same `507d79f8…` hash). `readout.py` opens only `ROOT/fixture.apk` (`readout.py:20-21,44`; stdlib imports `hashlib,json,struct,sys,zlib,pathlib`), so "reads only `fixture.apk` beside it" (`:162`) is accurate.

Regeneration (tests `:4` and `:121`): `cp generator.py /tmp/q09gen && cd /tmp/q09gen && python3 -B generator.py` exited 0 and wrote `fixture.apk` sha256 `05d2280f…` (947 bytes) and `truth.json` sha256 `27303bae…` — both byte-identical to the committed files, including `python_version` "3.14.8". So "reproduced byte-for-byte" is true on this host/interpreter (see R2).

## Per-instance decisions (every digest-bearing sentence)

| # | entry line | claim | re-derived value | Q09 |
|---|---|---|---|---|
| 1 | `:1` | S038 snapshot `56b88bc4…`, 86255 bytes | equal; `wc -c` 86255 | PASS |
| 2 | `:2` | S039 snapshot `412d9cb4…`, 34 lines | equal; `wc -l` 34 | PASS |
| 3 | `:3` | fixture `05d2280f…`, 947 bytes | equal (tree + HEAD) | PASS |
| 4 | `:3` | `truth.json` `27303bae…` | equal (tree + HEAD) | PASS |
| 5 | `:3` | `generator.py` `eaa9444c…` | equal (tree + HEAD) | PASS |
| 6 | `:3` | `readout.py` `92e347c3…` | equal (tree + HEAD) | PASS |
| 7 | `:5` | 15-line stdout SHA-256 `507d79f8…` | equal; 15 lines; root-invariant | PASS |
| 8 | `:19`,`:23` | archive 947 bytes sha256 `05d2280f…` "read from the file's bytes" | equal; scope explicit | PASS |
| 9 | `:37` | `AndroidManifest.xml` payload sha256 `73d1e0f2…` | equal over payload | PASS (scope implicit — F4) |
| 10 | `:39` | `classes.dex` payload sha256 `57cfe887…` | equal over payload | PASS (scope implicit — F4) |
| 11 | `:41` | `META-INF/MANIFEST.MF` payload sha256 `2e5da249…` | equal over payload | PASS (scope implicit — F4) |
| 12 | `:37`,`:39`,`:41` | member CRC-32s over payload | equal (`zlib.crc32`) | PASS |
| 13 | `:103` | declared checksum `0x3d120c30` = Adler-32 "from offset 12 on" | equal (`adler32(dex[12:])`) | PASS |
| 14 | `:103`,`:107` | declared signature = SHA-1 "from offset 32 on" | equal (`sha1(dex[32:])`) | PASS |
| 15 | `:162` | `readout.py` sha256 `92e347c3…` | equal | PASS |
| 16 | `:121` | regeneration byte-for-byte | reproduced fixture + truth.json exactly | PASS |

Supporting (not digest) arithmetic also re-derived: six AXML chunks at 8/204/248/272/368/392 summing to 416 with headerSizes 28/8/16/16/16/16; EOCD `737+188=925`; 3 members, walk cursor 925. No contradiction found.

## Origin / completeness / authenticity framing

- `:19` — "read from the file's bytes": the only sentence introducing the archive digest; it makes no origin claim.
- `:121` — oracle comparison is stated as field agreement ("agree … on every shared field"), not as independent confirmation or authenticity; the oracle is authored by the same generator, and the entry does not call it independent.
- `:4`, `:121` — regeneration is a determinism replay of own-work, described as such; it is not presented as authenticating any third-party artifact.
- No sentence claims completeness: the walk is scoped to this archive's central directory (`:26`-`:41`), and `:129`-`:131` plus `:6` limit the claim to one authored fixture with one manifest shape.
- Task-relevant gap (not a violation): round-64 precedent carries an explicit disclaimer — `corpus/knowledge/round-64-firmware-region-byte-evidence.md:196` "Digest equality is not authenticity (Q09) … Matching digests prove only that the bytes hashed are the bytes named." Round-65 has no equivalent sentence; its fence is indirect (`:6` "Not covered: install/signature verification, dex validity or execution", `:127`, `:131`, and `corpus/SOURCES.md:55` "not install validity, dex validity, provider accuracy or completeness"). Q09 is satisfied because nothing overclaims, but adding the one sentence would match precedent and harden the entry.

## dex checksum/signature framing (criterion's third clause)

`:101` heading is "**dex declared header**"; `:103` says "Its **declared** checksum … equals the Adler-32 **recomputed over the bytes from offset 12 on**" and "its **declared** 20-byte signature equals the SHA-1 **recomputed over the bytes from offset 32 on**". Validity is disclaimed three times: `:6` coverage-map "Not covered: install/signature verification, dex validity or execution"; `:127` "nothing about install validity, **signature blocks**, dex program validity … is claimed; the fixture is inert"; `:131` "The dex member is a header only and is **intentionally not a valid dex program**." No sentence treats `checksum_matches`/`signature_matches` as proof of integrity, provenance, or dex validity. PASS.

## Findings (none falsifies Q09)

- **F1 — low, stale pointer at `:15`.** "the script is the `### Code` block of that section" — the entry contains no `### Code` heading or code fence (`grep -n '^### '` → no match; all 26 fences are output blocks; `## Reproduce` at `:154`-`:162` has only the shell command, exit/line-count/digest sentence, no code). Round-63's identical sentence (`corpus/knowledge/round-63-zip-central-directory-evidence.md:229-231`) does have the block below it; round-65 appears to have dropped it. Reproduction is still intact because `:162` pins `readout.py` by path + sha256 (verified), but the sentence as landed is false.
- **F2 — low, dangling cross-reference at `:3`.** S041 says "row text in §Sources", but the entry has no `## Sources` section (headings at `:9,:13,:119,:123,:129,:133,:137,:154`); round-63 has one at `:664`. `corpus/SOURCES.md:55` (S041) does exist and its four digests match the entry, so the anchor resolves via the registry; the in-document § pointer does not.
- **F3 — low, pointer wording at `:15`.** "the same lines appear in the full 15-line stdout reproduced there" — §Reproduce reproduces only the command and the digest, not the 15 lines. The 15 lines do appear in §Observation. I verified the set equality `sort(full-run stdout) == sort(per-fact outputs)` and that the full run is exactly 15 lines with `507d79f8…`. Note the full-run order differs from the entry's item order (full run emits `spec_derived_struct_widths` second), so "the same lines" is true as a set, not as a sequence.
- **F4 — info, digest scope not stated in prose.** The three member `sha256` values appear without an explicit "payload" qualifier in the prose sentence, unlike CRC-32 ("recomputed over its payload bytes"). They are exactly the payload hashes (`readout.py:106-117`: slice at `payload_offset` with `compressed_size`; ZIP_STORED, so equal to uncompressed size). No false claim; "payload sha256" would close the ambiguity.
- **F5 — info, dex recompute span is member-bounded.** `readout.py:241-245` hashes `dex[12:]`/`dex[32:]` of the 112-byte member, which coincides with the declared `file_size` 112. Exact for this fixture; the script is fixture-specific by design (`readout.py:20-21,44`), so this is not a claim defect, only a boundary to keep in mind if the readout is ever reused.

## Residual risk

- **R1 — digest anchors survive only while the bytes are untouched.** All values were checked at committed HEAD `8214e4d` with a clean tree for the scored paths, so `:1-:5`, `:19-:41`, `:121`, `:162` and `SOURCES.md:55` are true of a committed tree, not only of the working tree. Any later re-encode of `fixture.apk`/`truth.json`/`generator.py`/`readout.py` (or snapshot replacement) without updating digests falsifies those sentences; the round-end tip must be re-hashed if any of those five paths changes.
- **R2 — cross-interpreter reproducibility.** Byte-for-byte regeneration holds on Python 3.14.8 / zlib 1.3.2 (tested); `truth.json` embeds `python_version`, and the entry hedges exactly that field at `:121`. Fixture byte-reproduction across other CPython/zlib builds is not established (same class of caveat round-64 records at `corpus/knowledge/round-64-firmware-region-byte-evidence.md:200`). The entry claims reproduction only "on this host" (`:4`), so no overclaim.
- **R3 — oracle circularity.** The artifact and oracle share one author; agreement is internal consistency, not independent confirmation. Q09 does not forbid it and the entry does not call it independent, but Q03/Q06 owners may want it stated (round-64 states it at `corpus/knowledge/round-64-firmware-region-byte-evidence.md:190`).
- **R4 — adjacent, unscored.** `corpus/SOURCES.md:55` S040's rationale says zipfile docs were "used only as a cross-check in this round's container walk", but the entry never cites S040 and its walk uses `struct` only. Whether that cross-check exists elsewhere in the round is outside this seat; flagged only because it sits in the same registry block as the S041 digests.

## Verification gaps

- **No `lsp` device in this seat's tool inventory**, so caller/definition/diagnostics checks were text-based (`read`, `grep`, `git show`); nothing here is presented as semantic LSP proof. This seat exposes only read/bash/edit/eval/glob/grep/task/wait/web_search/write/yield.
- Measurements cover HEAD `8214e4d` / working tree, not the round-end final tip (README C05 is still `frontier` at `corpus/README.md:34`, as required pre-admission). Per contract, measurements belong to committed trees; HEAD is committed, but a later amendment needs re-hashing.
- I did not run `reports/round-65/measure.py` or the C2 mutation/self-tests (other seats own those); no statement here about `K_HELD`, `C5_*` or `HOLDS_OK_V3`.
- No tools were installed or upgraded; no package manager commands were run.
