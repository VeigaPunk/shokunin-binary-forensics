PASS — the v4 entry's `## Comparison with the authored oracle` sentence is TRUE as written: all 45 shared fields re-derived from the readout's actual stdout match the `truth.json` oracle, 0 mismatches, and a second independent parse of the raw bytes (zipfile + a fresh struct walker, not `readout.py`) confirms every one of the oracle's declared values.

seat: L1Revenger69.R69OracleCorrespondence · round 69 · 2026-10-25 · read-only (no file edited, no git/jj write)

## Scope and commands

Lane root `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Everything below was run from there;
stdout captured to `/tmp/revenger-r69-oracle/` (scratch, deleted before return).

```
$ python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/revenger-r69-oracle/readout.jsonl
EXIT=0
  15 5099 /tmp/revenger-r69-oracle/readout.jsonl        # 15 lines, 5099 bytes, no stderr
$ sha256sum /tmp/revenger-r69-oracle/readout.jsonl
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247
```

That digest and line count are exactly the ones the entry pins at its `recheck:`
(`round-69-apk-axml-byte-evidence.md:6`) and §Reproduce — the claimed stdout SHA-256 is
re-derivable, not asserted.

Byte pins in the entry, all re-verified on the working tree:

```
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk   (947 bytes, stat)
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py
eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a  corpus/fixtures/apk-r65/generator.py
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  corpus/fixtures/apk-r65/truth.json
74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa  corpus/derive_axml_anchors.py
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
$ python3 -V        → Python 3.14.8   (= truth.json build_recipe.python_version)
```

## Shared-field correspondence (re-derived, one row per field)

Comparison program: parsed `truth.json` and the 15 stdout records, compared each oracle field against
the readout field that carries it, 45 comparisons. `attr[i].data` is carried under a type-dependent
key — `data_type_string` when dataType `0x03` (`readout.py:215`), `data_type_int_dec` otherwise — so the
comparison reads the key that matches the oracle's `data_type`.

| # | field | oracle | readout | verdict |
|---|---|---|---|---|
| 1 | image.sha256 | `05d2280f…afe7d03e` | `05d2280f…afe7d03e` | MATCH |
| 2 | image.size | 947 | 947 (`bytes`) | MATCH |
| 3 | AndroidManifest.xml.local_header_offset | 0 | 0 | MATCH |
| 4 | AndroidManifest.xml.compressed_size | 416 | 416 | MATCH |
| 5 | AndroidManifest.xml.uncompressed_size | 416 | 416 | MATCH |
| 6 | AndroidManifest.xml.crc32 | `962d075f` | `962d075f` | MATCH |
| 7 | AndroidManifest.xml payload sha256 | `73d1e0f2…afe9fae4` | `73d1e0f2…afe9fae4` | MATCH |
| 8 | classes.dex.local_header_offset | 465 | 465 | MATCH |
| 9 | classes.dex.compressed_size | 112 | 112 | MATCH |
| 10 | classes.dex.uncompressed_size | 112 | 112 | MATCH |
| 11 | classes.dex.crc32 | `2635c82a` | `2635c82a` | MATCH |
| 12 | classes.dex payload sha256 | `57cfe887…f8d548c2` | `57cfe887…f8d548c2` | MATCH |
| 13 | META-INF/MANIFEST.MF.local_header_offset | 618 | 618 | MATCH |
| 14 | META-INF/MANIFEST.MF.compressed_size | 69 | 69 | MATCH |
| 15 | META-INF/MANIFEST.MF.uncompressed_size | 69 | 69 | MATCH |
| 16 | META-INF/MANIFEST.MF.crc32 | `e948d738` | `e948d738` | MATCH |
| 17 | META-INF/MANIFEST.MF payload sha256 | `2e5da249…c403c0a49` | `2e5da249…c403c0a49` | MATCH |
| 18 | strings.count | 9 | 9 (`stringCount`) | MATCH |
| 19-27 | strings[0..8] | android · http://schemas.android.com/apk/res/android · manifest · package · com.example.r65 · versionCode · versionName · 1 · 1.0 | identical, in order | MATCH ×9 |
| 28-32 | attr[0] (package) name_idx / ns_idx / raw_value_idx / data_type / data | 3 / 4294967295 / 4 / 3 / 4 | 3 / 4294967295 / 4 / 3 / 4 | MATCH ×5 |
| 33-37 | attr[1] (versionCode) name_idx / ns_idx / raw_value_idx / data_type / data | 5 / 0 / 7 / 16 / 1 | 5 / 0 / 7 / 16 / 1 | MATCH ×5 |
| 38-42 | attr[2] (versionName) name_idx / ns_idx / raw_value_idx / data_type / data | 6 / 0 / 8 / 3 / 8 | 6 / 0 / 8 / 3 / 8 | MATCH ×5 |
| 43 | resource_ids length / full 9-entry array | 9 ids, all equal | 9 ids, all equal (`ids`) | MATCH |
| 44 | resource_ids[5] | `0x0101021b` | `0x0101021b` (and `nonzero.versionCode`) | MATCH |
| 45 | resource_ids[6] | `0x0101021c` | `0x0101021c` (and `nonzero.versionName`) | MATCH |

Result line: `fields compared: 45 mismatches: 0`.

The entry's parenthetical item pointers are correct: image → item 1, members → item 3, strings → item 6,
resource ids → item 7, attribute rows → item 8, so "items 6-8" is accurate
(`corpus/knowledge/round-69-apk-axml-byte-evidence.md:157`).

## Independent confirmation that the oracle itself is right (not just self-consistent)

Correspondence between two readers could be circular. Two checks exclude that.

1. **No shared input.** `grep -n "truth\|json.load" corpus/fixtures/apk-r65/readout.py` → no output:
   the readout never opens `truth.json`; it reads only `ROOT / "fixture.apk"` (`readout.py:20-21`) and
   `--fact` argv. The agreement is between two independent derivations, not a copy.
2. **Second implementation.** `zipfile` (a stdlib implementation unrelated to the readout's raw struct
   walk) plus a hand-written AXML walker re-derived every oracle field straight from the bytes:

```
independent zipfile parse:
 AndroidManifest.xml    offset=0 size=416/416 crc=962d075f sha=73d1e0f2e67c.. MATCH
 classes.dex            offset=465 size=112/112 crc=2635c82a sha=57cfe8878be7.. MATCH
 META-INF/MANIFEST.MF   offset=618 size=69/69 crc=e948d738 sha=2e5da2495f3d.. MATCH
independent AXML: stringCount=9 styles=0 flags=0x00000100
 stringCount=9 strings==oracle: True
 resource_ids==oracle: True
 attributeStart=20 attributeSize=20 attributeCount=3
  attr[0] oracle={data:4,data_type:3,name_idx:3,ns_idx:4294967295,raw_value_idx:4} raw=identical MATCH
  attr[1] oracle={data:1,data_type:16,name_idx:5,ns_idx:0,raw_value_idx:7}   raw=identical MATCH
  attr[2] oracle={data:8,data_type:3,name_idx:6,ns_idx:0,raw_value_idx:8}    raw=identical MATCH
```

   (First run of this walker used a wrong `attributeStart` offset and mismatched; corrected offsets are
   `base+24`/`base+26`/`base+28`, `readout.py:200-203` — recorded here so the reader sees the fix, not a
   silent green.)

## Embedded-output fidelity (transcription-drift check, M39/M40 class)

The entry claims every embedded line was captured from the actual stdout. Checked mechanically: every
line in the entry starting `{"` (30 of them: 15 in the per-item blocks + the 15-line §Reproduce block)
was matched against the fresh 15-line run.

```
embedded JSON lines in entry: 30
exact matches: 30 | visibly truncated (…): 0 | problems: 0
```

The 891-byte `axml_start_element` line is stored in full in the file (the `…` seen in a `read` preview is
the reader's 768-char display truncation, not the file's bytes). The item 11 anchor block is likewise
byte-identical to a fresh `python3 -B corpus/derive_axml_anchors.py`: `entry block lines: 20 | actual: 20
| byte-identical: True`, exit 0.

## Findings

**No HIGH or MEDIUM finding.** The comparison sentence holds on every shared field, and the shared-field
enumeration it carries is complete for what the readout prints.

- **LOW/INFO — `members[].method` is an oracle field the readout never prints.** `truth.json` declares
  `method: 0` for all three members and `build_recipe.container` "ZIP_STORED"; `readout.py` has no
  `method`/compression field in its member records, so that oracle field is un-cross-checked by readout
  stdout and can only be inferred from `compressed_size == uncompressed_size`. Independent
  `zipfile` check closes it: `compress_type per member (0=STORED): [('AndroidManifest.xml', 0),
  ('classes.dex', 0), ('META-INF/MANIFEST.MF', 0)]`. Not a contradiction and not a "shared field"
  (no readout counterpart), so the entry's wording is not false — but a reader cannot re-derive it from
  the stated command alone. Optional hardening only; no edit made.
- **INFO — `data` is not a raw printed field.** The readout emits the attribute `data` word under
  `data_type_string` (dataType `0x03`) or `data_type_int_dec` (everything else) — `readout.py:215`. The
  three-row agreement is demonstrable only to a checker that knows that mapping; the term "attribute
  rows" in the entry could be read as a raw field-by-field print. Value correspondence is exact.
- **INFO — `build_recipe.python_version` is a precondition, not a shared field.** It appears in the
  comparison's scope sentence but has no readout counterpart; the readout prints no interpreter version.
  It happens to be satisfied on this host (`python3 -V` → 3.14.8), and the entry explicitly discloses
  that regeneration from `generator.py` was not re-run (S041/round-65 evidence), so this is disclosed,
  not hidden.
- **INFO — the compressed/uncompressed split is non-discriminating for this fixture.** All three pairs
  are equal (ZIP_STORED), so a readout that swapped the two would still match — already covered by the
  entry's own Limitations ("ZIP_STORED with no data descriptors"). No new gap.

## Residual risk

- *Latent, not active:* the correspondence is exact for this fixture's value set but does not exercise a
  non-STORED member, a non-UTF-8 pool, a `dataType` other than `0x03`/`0x10`, or a null `raw_value`
  (`0xffffffff`). All are named in the entry's Limitations; none is claimed.
- The oracle and the readout share the same *fixture*, so a systematic misreading of the ZIP/AXML byte
  layout could in principle fool both — excluded here by the independent `zipfile`/fresh-walker parse,
  which uses different code and different field offsets to reach the same values.

## Verification gaps (what this seat did not do)

- Did not re-run `generator.py` to reproduce the fixture byte-for-byte (round-65/S041 evidence; the
  entry says so explicitly). Reproducibility of 947 bytes from `generator.py` under 3.14.8 is therefore
  unverified *in this round*, and the oracle's determinism claim rests on the round-65 record.
- Did not execute the Q01–Q15 decision seats or the counter; those are other seats' assignments. This
  report answers only the oracle-correspondence question for the v4 candidate.
- Did not check `corpus/README.md` C05 status or admission (out of seat scope; claims.md §C1 sets the
  admission order). The entry correctly reads `admission-status: candidate`
  (`round-69-apk-axml-byte-evidence.md:9`).
- Generic role bullets about one canonical runtime, same-identity rerouting, `resume_continuity_v1`
  and saturation claims are **n/a** for this lane: no runtime, rerouting, resume path or saturation
  assertion exists in the reviewed artifact.

## Tooling log

No install or upgrade was performed. Tools used: host `python3` 3.14.8 (stdlib `zipfile`, `struct`,
`hashlib`, `json`), `sha256sum`, `stat`, `grep` — all pre-existing binaries. Scratch:
`/tmp/revenger-r69-oracle/` (removed before return).
