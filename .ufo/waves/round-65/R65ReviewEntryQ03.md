PASS (Q03) — every expected value in the candidate is either byte-derived at check time (`readout.py` opens only `fixture.apk`) or a pin fixed outside the fixture (S038 struct field lists, generator declarations), and no saved path serves as both identity and locator; **admission blocker outside Q03**: `corpus/knowledge/round-65-apk-axml-byte-evidence.md:41` quotes a value no readout run produces (Q11 falsifier, F1 below).

Seat `revenger-r65.R65ReviewEntryQ03`, round 65 attempt 1 (hyaku), 2026-10-24. Lane `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Read-only: no production edit, no git/jj mutation, no subagents. Scratch: `/tmp/r65-q03/`.

## Record under review (identity, not path)

| record | identity | locator |
|---|---|---|
| candidate entry | sha256 `e173e6436e9b8cce2ddd9f318b914fde6fd9bdfaf18335f5a873ac60fa3cdfb7` (20754 B) | `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-65-apk-axml-byte-evidence.md` |
| fixture | sha256 `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` (947 B) | `corpus/fixtures/apk-r65/fixture.apk` |
| oracle | sha256 `27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173` | `corpus/fixtures/apk-r65/truth.json` |
| generator | sha256 `eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a` | `corpus/fixtures/apk-r65/generator.py` |
| readout | sha256 `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976` | `corpus/fixtures/apk-r65/readout.py` |

All five paths are tracked and clean at HEAD `8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0` (`git ls-files` lists all five; `git status --porcelain -- corpus/knowledge/ corpus/fixtures/apk-r65/` returned empty), so this review scores committed bytes.

## Criterion

`corpus/QUALITY.md:15` — **Q03**: *Expected values are derived independently: from bytes, a specification, or a pin fixed outside the record under test.* Fail when *the expected value is copied from the record being checked, or a saved path is used as both identity and locator* (mistakes M06/M14). Same rule at `SKILL.md:128`.

## Why Q03 holds — value-by-value origin audit

| expected value in the entry | origin | independent of the fixture? | evidence |
|---|---|---|---|
| item 1 size 947 / sha256 `05d2…` | readout stdout, recomputed from the file's bytes | yes — recomputed by me and by `R65BlindDerive` | E1, E3, E4 |
| item 2 EOCD 925 / CD 737+188 / 3 entries | byte walk only; `truth.json` carries no EOCD field | yes | E3; `truth.json` grep for `eocd`/`payload_offset` → no match |
| item 3 member offsets 0/465/618, sizes 416/112/69, CRC-32 | readout raw-struct walk (bytes); oracle values were measured by `zipfile` in `generator.py:175-192`, `:204`, so agreement is cross-parser | yes (two independent readers of the same bytes) | E3; F4 wording nit |
| item 4 six chunk types `0x0001/0x0180/0x0100/0x0102/0x0103/0x0101`, headerSizes 28/8/16/16/16/16 | S038 enum + struct widths, pinned in the snapshot | yes — verified line-by-line against the spec snapshot | E5, E6 |
| item 5 struct widths 8/28/16/20/20/8 | S038 field lists (snapshot lines listed in E5); only the sums are computed (`readout.py:51-60`) | yes — this is the "spec fixed outside the record" leg | E5 |
| items 6-8 nine strings, three attribute rows, resource ids `0x0101021b`/`0x0101021c` | readout byte walk; expectations from `generator.py:31-46` constants (`STRINGS`, `ATTRIBUTES`, `RESOURCE_IDS`) | declarations precede the bytes and the fixture cannot change them | E3, E5; residual F5 |
| item 9 dex checksum `0x3d120c30`, SHA-1 `a5fc7bea…`, 112/112, endian `0x12345678` | readout recomputes Adler-32/SHA-1 over the bytes | yes — self-verifying recomputation | E3 |
| item 10 jar 69 B, `Manifest-Version: 1.0`, 1 section | readout byte decode | yes | E3 |

**No expected value is copied from a saved producer record at check time.** Code-level proof: `readout.py:20-21` resolves `ROOT`/`APK` and `:44` is `apk = APK.read_bytes()`; a grep for `open(`, `read_text`, `truth`, `TRUTH` in the script returns nothing — `truth.json` is never read by the checker. The oracle is comparison-only in prose (§Comparison, `:119-121`), the same shape round 63 scored PASS (`reports/round-63/build/R63ReviewC06Q.md:23`).

**No saved path is both identity and locator.** Identity is a digest everywhere (`S041`, entry `:3-5`), paths are locators only, and the `recheck:` identity is the stdout digest `507d79f8…` (`:5`, `:162`) — a digest of what the path yields, not the path.

## Reproductions (commands and actual output)

**E1 — record digests** (scratch copy `/tmp/r65-q03/apk-r65`, `cp -a` from the lane):

```
$ sha256sum fixture.apk truth.json generator.py readout.py
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  fixture.apk
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  truth.json
eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a  generator.py
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  readout.py
```

**E2 — recheck**: `python3 -B readout.py` in the scratch copy → `exit=0`, 15 stdout lines, `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — byte-identical to the entry's `recheck:` pin (`:5`, `:162`) and to `R65EntryCommands`'s own recheck. Path-independence confirmed: the copy runs from `/tmp`, not the lane root.

**E3 — entry-quoted value vs actual stdout** (15 `$ python3 … --fact …` pairs parsed from the entry, each compared as parsed JSON against a fresh run):

```
pairs in entry: 15
MISMATCH 'member[META-INF/MANIFEST.MF]'
  differing: {'payload_first16_hex': ('4d616e696673742d56657273696f6e', '4d616e69666573742d56657273696f6e')}
exact-match 14/15  mismatched 1
```

**E4 — readout's only file access**: `grep -n "read_bytes\|open(\|read_text\|truth\|TRUTH\|Path(" corpus/fixtures/apk-r65/readout.py` → only `:20 ROOT = Path(...)`, `:44 apk = APK.read_bytes()`.

**E5 — spec-derived widths vs the S038 snapshot** (`/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-65/source-snapshots/ResourceTypes.h`, sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`):

| struct | readout table (`readout.py:52-59`) | snapshot field lines | sum | entry claim |
|---|---|---|---|---|
| `ResChunk_header` | `[2,2,4]` | `:222 uint16_t type`, `:227 uint16_t headerSize`, `:234 uint32_t size` | 8 | 8 ✓ |
| `ResStringPool_header` | `[2,2,4,4,4,4,4,4]` | header 8 + `:467/471/482/485/488` = 5×u32 | 28 | 28 ✓ |
| `ResXMLTree_node` | `[2,2,4,4,4]` | header 8 + `:626 uint32_t lineNumber` + `:629 ResStringPool_ref comment` | 16 | 16 ✓ |
| `ResXMLTree_attrExt` | `[4,4,2,2,2,2,2,2]` | ns+name (2×u32) + `:687/690/695/698/701/704` = 6×u16 | 20 | 20 ✓ |
| `ResXMLTree_attribute` | `[4,4,4,2,1,1,4]` | ns+name+rawValue (3×u32) + `Res_value` (`:707-719`) | 20 | 20 ✓ |
| `Res_value` | `[2,1,1,4]` | `:290 uint16_t size`, `:293 uint8_t res0`, `:351 uint8_t dataType`, `:408-409 data_type data` (`typedef uint32_t`) | 8 | 8 ✓ |

**E6 — chunk-type enum anchors** (`source-snapshots/ResourceTypes.h`): `RES_STRING_POOL_TYPE` `:239`, `RES_XML_TYPE` `:241`, `RES_XML_START_NAMESPACE_TYPE` `:245`, `0x0101` `:246`, `0x0102` `:247`, `0x0103` `:248`, `RES_XML_RESOURCE_MAP_TYPE` `:253`; `UTF8_FLAG = 1<<8` at `:480` (the readout's `flags & 0x100` test).

## Findings by severity

**F1 — blocker, adjacent criterion Q11 (not Q03). `entry:41` is false at pristine bytes.** The `member[META-INF/MANIFEST.MF]` record quotes `"payload_first16_hex": "4d616e696673742d56657273696f6e"`; the readout prints `4d616e69666573742d56657273696f6e`. Decoded: entry `b"Manifst-Version"` (15 B) vs fixture `b"Manifest-Version"` (16 B) — the value contradicts its own field name (first **16** bytes) and is one `65`/`e` short. `truth.json` does not carry `payload_first16_hex` at all (grep → no match), so only the readout arbitrates, and it contradicts the entry. The `recheck:` digest `507d79…` cannot catch this: it authenticates the readout's stdout, not the entry's transcription (the entry's own `:119-121` comparison is likewise unaffected). Corroborated independently by `R65MutEntry.md:75,85-88` (same pair, same call). One-field text fix in the entry; readout, fixture, oracle digests are unaffected.

**F2 — moderate, adjacent Q02/Q11. The promised embedded script block does not exist.** `entry:15` says *"the script is the `### Code` block of that section … and the same lines appear in the full 15-line stdout reproduced there"*, but `grep -c '^### ' <entry>` = **0** and §Reproduce (`:154-162`) holds only a ```sh command block. So the entry claims to be self-contained against its own script and is not; a reader must follow the path (identity is still pinned by the `92e347c3…` digest at `:162`, so this is a pointer defect, not an identity defect). Also found by `R65MutEntry.md` ("Secondary finding").

**F3 — low, Q02 pointer precision.** `entry:4` (item 4 text) cites S038's chunk-type enum at "lines 239-250", but `RES_XML_RESOURCE_MAP_TYPE = 0x0180` — one of the six values the entry uses — is at `:253`, outside the cited span. Anchor widened to 238-253 would be exact.

**F4 — low, Q03 wording.** The entry calls `truth.json` "the authored oracle" (`:119`) while `truth.json:74-101` (`members`) is measured from the finished APK by `generator.py:175-192` and written by `:204`, `:226`. The quality-gate substance is unharmed — the same sentence discloses "their **measured** offsets" and every quoted value is byte-derived (E3) — but a stricter Q03 reader could read "authored oracle" as an independent declaration. Suggested wording: "authored declarations for the AXML tables; container geometry measured from the built bytes by `zipfile`". Note also that `truth.json` carries no payload offsets and no AXML chunk table, so those facts have no oracle comparator at all (`R65BlindDerive.md` records the same limit).

**F5 — low, residual independence gap (correctly fenced).** The framework attribute ids `0x0101021b`/`0x0101021c` rest on `generator.py:44-46`'s comment alone; S038 (`ResourceTypes.h`) names no `android.R.attr` ids, and no registry row pins them. The entry already labels their identification **Inference** and attributes it to "the fixture generator declared" (`:124-127`), so no false claim is made — but "versionCode is `0x0101021b`" is not independently sourced in this lane.

**F6 — informational, peer-claim conflict for L1.** `R65EntryCommands.md:1` claims "16 commands executed; all 30 output lines matched; no mismatches", yet its own quoted `member[META-INF/MANIFEST.MF]` line (`:17`) carries the **correct** hex `4d616e69666573742d56657273696f6e`, which is not the entry's value at `:41`. That 30/30 claim is therefore falsified for that field regardless of which side is right; F1's ground truth is the fixture bytes plus the readout, both reproduced here.

## Cross-checks of peer seats

- `R65BlindDerive.md` (present, mtime 02:58:45): PASS — raw-byte walk (no `readout.py`, no entry) reproducing size/hash, EOCD, all three member rows and all six AXML chunk records. Its truth comparison agrees with mine on every shared field; its explicit note that `truth.json` "does not record payload offsets or the AXML chunk table" matches F4. No conflict with this verdict.
- `R65AxmlReprobe.md`: PASS — independent `struct` walk reproducing items 6-8 and the oracle's attribute rows. No conflict.
- `R65FixtureRegen.md`: regenerated `fixture.apk` and `truth.json` byte-identically at Python 3.14.8 (`cmp -s` exit 0, digests as E1), which removes the "oracle drifted from the artifact" risk for Q03.
- `R65MutEntry.md`: independently found F1 and F2; its mutant (b) detection is unaffected by F1.

## Residual risk / verification gaps

1. I verified the width table against the S038 snapshot transcription only; I did not re-open the pinned upstream URL (`refs/tags/android-15.0.0_r1`) — the snapshot digest ties my check to the lane's own copy.
2. Attr-id semantics (`0x0101021b` = `versionCode`) remain unsourced (F5); I did not fetch `android.R.attr`/`public.xml`, so I neither confirm nor deny the mapping beyond its declaredness.
3. `payload_first16_hex` has no oracle comparator, so F1 could only be caught by entry-vs-stdout comparison; I ran that for all 15 pairs (E3) and no other field differs.
4. Q03 does not police digest labeling of derived outputs; that is Q13's fence and the entry claims n/a there (`:152`).

## Harm / scope

No writes outside this report. The only commands touching lane files were reads (`sha256sum`, `sed`, `grep`, `git ls-files`, `git status --porcelain`, `git rev-parse`); all execution ran on a `cp -a` scratch copy at `/tmp/r65-q03/apk-r65`. No git/jj mutation, no file under `corpus/`, `reports/`, `LOG.md`, `SCORECARD.md`, `SHONEN.md` created or modified. **No tool installs or upgrades** were performed (nothing was needed; no pacman/uv action).
