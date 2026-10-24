**FAIL** — Q06: one quoted fixture premise does not reproduce (`corpus/knowledge/round-65-apk-axml-byte-evidence.md:41`, MANIFEST.MF `payload_first16_hex`); all measured premises, the oracle-vs-byte walk and the scratch regen pass.

# R65ReviewEntryQ06 — criterion Q06 on the C05 candidate + apk-r65 fixture

One quoted fixture premise does not reproduce: `corpus/knowledge/round-65-apk-axml-byte-evidence.md:41` (MANIFEST.MF `payload_first16_hex`) states `4d616e696673742d56657273696f6e` ("Manifst-Version", 15 bytes) where the fixture bytes and the readout print `4d616e69666573742d56657273696f6e` ("Manifest-Version", 16 bytes). Every *measurement* premise, the oracle-vs-byte walk and the scratch regeneration pass; the repair is a single hex-pair insertion (`65` after `66`).

Seat: R65ReviewEntryQ06 (leaf, read-only). Tree reviewed: lane working tree at HEAD `8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0`; entry blob `f02952af…` at HEAD equals the working file. No production edits made; no subagents; no installs/upgrades (stdlib Python 3.14.8 only).

## Findings

### F1 — blocking (Q06): a quoted byte premise was not byte-verified

- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-65-apk-axml-byte-evidence.md:41` (also at HEAD, same line):

```json
{"cd_index": 2, …, "payload_first16_hex": "4d616e696673742d56657273696f6e", "payload_offset": 668, "sha256": "2e5da249…", "uncompressed_size": 69}
```

- Actual payload bytes (`fixture.apk[668:668+16]`):

```
4d616e69666573742d56657273696f6e  ->  "Manifest-Version"
```

- The readout never prints the recorded value: running the quoted command verbatim (`shlex`-tokens) yields the 367-char line with `…69666573742d…`, the entry records 365 chars with `…696673742d…`. Decoding both: claimed = `Manifst-Version` (missing `0x65`), actual = `Manifest-Version`.
- Internal contradiction in the same entry: item 10 (`…:116`) prints `"first_line": "Manifest-Version: 1.0"`, which cannot be the first line of a payload whose first 16 bytes are `…69667374…`; and the entry's own `recheck` fingerprint (`…:5`, `…:162`) `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` is the SHA-256 of stdout containing the *correct* hex.
- Effect on Q06 as written ("every fixture premise was byte-verified against the built fixture"): falsified for this premise. Q11 fidelity also at risk (a recorded output is not the output of its stated command). Load-bearing values are unaffected (same `sha256`, `crc32`, size and offset), so this is a transcription defect, not a fabricated result — but the criterion text does not admit an unverified premise.
- Fix: insert `65` between `66` and `73` on line 41; then `python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[META-INF/MANIFEST.MF]'` reproduces the line verbatim.

### F2 — low (evidence-pointer accuracy)

- `…byte-evidence.md:15`: "the script is the `### Code` block of that section … and the same lines appear in the full 15-line stdout reproduced there". There is no `### Code` block and no full stdout block anywhere in the entry (`grep -n '^### '` → no match; headings are `## Observation` … `## Reproduce`, entry is 162 lines vs a 256-line/11 236-byte script). §Reproduce (`…:154-162`) carries the command, the 15-line/sha256 claim and the single-fact form only. The script itself is the real file and is byte-accurate (`readout.py` sha256 `92e347c3…f8c13976`, entry `…:162`), so this is a dangling pointer, not a false measurement.

### F3 — low (source-file description inherited by S041)

- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65/generator.py:11-14`: "All truth.json measurements (offsets, sizes, digests, the AXML chunk table) are derived from the finished bytes". `truth.json` has no chunk table (`top-level keys: ['axml_declared','build_recipe','image','members']`; no key contains "chunk"), and its `axml_declared` block mirrors the generator constants `STRINGS`/`ATTRIBUTES`/`RESOURCE_IDS`. The oracle labels that block `axml_declared` and the entry's §Comparison (`…:119-121`) correctly calls it "declares … the declared AXML string table", so no entry claim depends on the docstring; the S041 row (`corpus/SOURCES.md:55`) inherits the imprecise description of the shipped file.

## Verified (fresh evidence, independent of readout.py)

1. **Fixture identity** — `sha256sum corpus/fixtures/apk-r65/*`:
   `fixture.apk 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` (947 B), `truth.json 27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173`, `generator.py eaa9444c…c27c1a`, `readout.py 92e347c3…f8c13976` — all four equal the entry's `source:`/S041 hashes and the §Reproduce script hash.
2. **truth.json member measurements vs an independent byte walk** (my own `struct` EOCD → central-directory → local-header walk; CRCs recomputed with `zlib.crc32`, hashes with `hashlib`): **34/34 field checks pass, 0 fails.** All 7 keys of all 3 members — `name`, `local_header_offset` (0 / 465 / 618), `compressed_size` = `uncompressed_size` (416 / 112 / 69), `crc32` (`962d075f` / `2635c82a` / `e948d738`), `method` 0, `sha256` (`73d1e0f2…`, `57cfe887…`, `2e5da249…`) — equal the walk; `image.size` 947 and `image.sha256` match; `build_recipe.members` byte counts (416/112/69) match; the EOCD arithmetic holds (`925 = 737 + 188`, 3 entries, walk cursor ends at 925).
3. **Declared AXML table vs bytes** — string pool: `stringCount` 9, `styleCount` 0, `flags` `0x00000100`, `stringsStart` 64, `stylesStart` 0, offsets `[0,10,55,66,76,94,108,122,126]`, strings equal `truth.json axml_declared.strings` in order; resource map: 9 ids equal `axml_declared.resource_ids`, non-zero `16843291`/`16843292` (`0x0101021b`/`0x0101021c`); start-element: name `manifest`, `attributeStart` 20, `attributeSize` 20, `attributeCount` 3, and the three decoded attribute rows equal `axml_declared.attributes` exactly (`name_idx/ns_idx/raw_value_idx/data_type/data`). Chunk table equals entry item 4 byte-for-byte (`28/8/16/16/16/16` header sizes at `8/204/248/272/368/392`, sizes `196/44/24/96/24/24`, walk ends at 416 = member size). Namespace pair resolves to `android` / `http://schemas.android.com/apk/res/android`, `lineNumber` 1.
4. **dex declared header** — magic `dex\n035\0`; Adler-32 over `[12:]` equals declared `0x3d120c30`; SHA-1 over `[32:]` equals declared signature `a5fc7bea…`; `file_size` 112, `header_size` 112, `endian_tag` `0x12345678` — item 9 values exact.
5. **Text manifest** — 69 bytes, first line `Manifest-Version: 1.0`, `section_count` 1.
6. **Reproduce claim** — from the lane root: `python3 -B corpus/fixtures/apk-r65/readout.py` → `rc 0`, **15 stdout lines**, stdout sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — exactly the entry's `recheck` (`…:5`) and §Reproduce (`…:162`) values. **Path independence** also holds: the same 15 lines and the same sha256 from a foreign scratch tree `/tmp/r65q06tree` (entry's "same bytes give the same 15 lines from any checkout" claim).
7. **Quoted-output fidelity** — 15 quoted command blocks; **14/15 reproduce byte-for-byte**; the only mismatch is F1. All 15 quoted JSON lines parse.
8. **Scratch-only regeneration and byte compare** — copied only `generator.py` to `/tmp/r65q06`, ran `python3 -B generator.py` under **Python 3.14.8** (equal to `truth.json build_recipe.python_version`): produced `fixture.apk` sha256 `05d2280f…d03e` and `truth.json` sha256 `27303bae…8173`; `cmp` says `FIXTURE_IDENTICAL` and `TRUTH_IDENTICAL` — the entry's "reproduced byte-for-byte … up to its embedded python_version field" is satisfied, and in fact the bytes are fully identical. HEAD blobs equal the working bytes for all four files (`fixture.apk`, `truth.json`, `generator.py`, `readout.py`), so what I regenerated is the committed tree's content.
9. **Container premises** — all three members: local flags `0x0000` (no data-descriptor bit), DOS date-time `2026-10-24 12:00:00`, method 0 → §Limitations' "ZIP_STORED with no data descriptors" and `build_recipe.container` verified. `corpus/fixtures/apk-r65/` holds exactly the four declared files; no scratch artifact or stray `.apk`/`truth.json` anywhere under the lane's `corpus/fixtures` beyond the per-round fixture dirs.

## Axis read (coverage / calibration)

Q06 coverage of the *fixture* is strong and independently reproducible: the oracle's member measurements are exactly a fresh byte walk, and regeneration is deterministic at the recorded interpreter. Q06's calibration is the failure: the entry's Q06 row asserts "every fixture premise was byte-verified", yet one quoted premise is provably not the bytes. Under `reports/round-65/claims.md` §Admission order step 3, an all-criteria Q01–Q13 pass is required before the README C05 flip, so this decision is a blocker on the candidate as it stands — narrowly repairable at `…:41` (and the dangling pointers F2 should be corrected in the same edit since they are the same evidence-trail paragraph family).

## Residual risk and verification gaps

- **"Generator run only in scratch" is not observable post hoc.** The generator is deterministic and writes only `fixture.apk`/`truth.json` beside itself; an in-place run would have produced byte-identical output, leaving no trace. What I can and did verify is the property that matters: fresh scratch regeneration reproduces the committed bytes exactly, the fixture dir has no extra artifacts, and HEAD bytes equal working bytes. Treated as verified-by-effect, not verified-by-absence-of-evidence.
- **S038 anchors not re-opened.** I did not fetch `ResourceTypes.h` (network) to confirm the cited struct field lists or line numbers (218, 239-250, 461, 612, 621); Q06 is fixture-scoped. Note the derived widths are nevertheless confirmed *empirically* inside this fixture: `attributeStart=20`, `attributeSize=20`, `headerSize` 28/16, and the chunk walk summing exactly to 416 are mutually consistent, so a wrong S038 derivation could not produce these bytes by accident — but the source anchors themselves remain a Q01/Q11 obligation.
- **Scope.** I assessed Q06 only; C2/C5 verifier patches, the census, README state and the counter labels are outside this seat and untouched.
- **Artefacts left behind:** none in the lane; my scratch trees are `/tmp/r65q06`, `/tmp/r65q06tree`, `/tmp/r65head` (outside every repo).

Report: `.ufo/waves/round-65/R65ReviewEntryQ06.md`
