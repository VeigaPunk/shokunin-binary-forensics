PASS — Q06: every fixture premise in the landed v5.1 entry re-derives from the built fixture's bytes (all ten item-14 digests match the committed files byte for byte, and an independent struct walk I wrote reproduces every container/AXML/dex value in items 1-9); the entry states honestly that it does not re-run `generator.py`, and a scratch re-run shows the pinned fixture and oracle *are* what the generator emits. No fixture premise is stated from intent.

Seat: R70W2GateQ06 · wave 2 (fresh; attacked nothing in wave 1) · lane `/home/vgpnk/Projects/shokunin/revenger-shokunin`
Target bytes: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin show 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd:corpus/knowledge/round-70-apk-axml-byte-evidence.md` (`admission-status: candidate`, 323 lines), extracted with
`git archive 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd corpus SHONEN.md SCORECARD.md SKILL.md | tar -x -C /tmp/revenger-r70-R70W2GateQ06-ZzSR`.
Contract read first: `reports/round-70/claims.md` §C1 (kill rule: a wave-2 Q FAIL carrying a located defect falsifies C1; a PASS never overrides a mechanical label) and `corpus/QUALITY.md` Q06. No lane file was written or edited; all runs happened in `/tmp/revenger-r70-R70W2GateQ06-ZzSR` and `/tmp/revenger-r70-R70W2GateQ06-gen`. No tool was installed (nothing was needed; Python 3.14.8 and coreutils sufficed).

## 1. Criterion under decision (Q06, quoted from `corpus/QUALITY.md:18`)

> Q06 | Fixture premises are byte-verified against the built fixture after every edit and before any producer call; failed inputs are retained. | reject when: an offset, operand, size or count is stated from intent rather than from the built bytes | M04, M05

The entry's own §Q-map row (`:303`) is **not** used as evidence anywhere below; each value is re-derived by command.

## 2. Item 14's ten digests against the committed files — exact match

Entry item 14 (`:218-232`) claims ten files with sha256 + byte size. The entry's command, run at the extracted target:

```
$ cd /tmp/revenger-r70-R70W2GateQ06-ZzSR && python3 -B corpus/fixtures/apk-r65/entry_checks.py --pins
sha256 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e 947 bytes corpus/fixtures/apk-r65/fixture.apk
sha256 27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173 2466 bytes corpus/fixtures/apk-r65/truth.json
sha256 eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a 9599 bytes corpus/fixtures/apk-r65/generator.py
sha256 92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976 11236 bytes corpus/fixtures/apk-r65/readout.py
sha256 2d4f25f6894ac86ced3c9986abd7cdbcf4c6d2aab477cda6dc515585c129b1f9 15062 bytes corpus/fixtures/apk-r65/entry_checks.py
sha256 74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa 4979 bytes corpus/derive_axml_anchors.py
sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f 86255 bytes corpus/snapshots/ResourceTypes.h
sha256 0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6 174585 bytes corpus/snapshots/APPNOTE.TXT
sha256 c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4 281157 bytes corpus/snapshots/dex-format.html
sha256 412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c 1992 bytes corpus/snapshots/rea-android-applications.md
EXIT=0
```

Independent hash, not through the entry's script (`sha256sum` + `stat -c '%s'` on the same ten paths): every digest and every size identical, line for line — `05d2280f…d03e/947`, `27303bae…8173/2466`, `eaa9444c…c1a/9599`, `92e347c3…3976/11236`, `2d4f25f6…b1f9/15062`, `74d4c0d9…83aa/4979`, `56b88bc4…c56f/86255`, `0b993022…0cd6/174585`, `c0428612…d9f4/281157`, `412d9cb4…a74c/1992`. Ten lines, ten files: the count "ten" is correct.

Completeness of the pin set: I enumerated every file the entry's commands actually open. `readout.py` reads only `fixture.apk`; `entry_checks.py` reads `fixture.apk`, `truth.json`, `readout.py`, `corpus/snapshots/APPNOTE.TXT` and the three spec snapshots (`entry_checks.py:111,117,124,169,182,221,253,254,287`); `derive_axml_anchors.py` reads only `ResourceTypes.h` (`derive_axml_anchors.py:102,105`). All ten opened files are pinned; the builder `.ufo/waves/round-70/build-entry.py` is named as outside `corpus/` and undigested (`:8`). No unpinned fixture input exists.

## 3. Every fixture premise re-derived from the built bytes by an independent walk

I wrote my own `struct` reader (not `readout.py`, not `entry_checks.py`) over `corpus/fixtures/apk-r65/fixture.apk` and compared with items 1-9, 16.

Container (`/tmp/revenger-r70-R70W2GateQ06-indep.py`, full stdout):

```
size 947 sha256 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e
eocd_off 925 sig 504b0506
total_entries 3 cd_size 188 cd_offset 737 cd_end==eocd True
member AndroidManifest.xml cd_index=0 lho=0 csz=416 usz=416 crc=962d075f payload_off=49 first16=03000800a001000001001c00c4000000 sha256=73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4 flags=0x0000/0x0000 method=0/0
member classes.dex cd_index=1 lho=465 csz=112 usz=112 crc=2635c82a payload_off=506 first16=6465780a30333500300c123da5fc7bea sha256=57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2 flags=0x0000/0x0000 method=0/0
member META-INF/MANIFEST.MF cd_index=2 lho=618 csz=69 usz=69 crc=e948d738 payload_off=668 first16=4d616e69666573742d56657273696f6e sha256=2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49 flags=0x0000/0x0000 method=0/0
```

Against the entry: item 1 `bytes 947`/`sha256 05d2280f…` (`:27`) ✓; item 2 `eocd_offset 925`, `offset_of_start_of_cd 737`, `size_of_central_directory 188`, `total_entries_cd 3`, `cd_end_equals_eocd_offset true` (`:34`) ✓ and the second command's `eocd signature bytes at offset 925: 504b0506 (4 bytes)` (`:36`) ✓; item 3 `local_header_offset` 0/465/618, `payload_offset` 49/506/668, `payload_first16_hex` for all three, `sha256`, `crc32` (`:43,45,47`) ✓ — the `payload_offset = local_header_offset + 30 + name_length + extra_length` formula (`:39`) is confirmed by my own arithmetic (0+30+19, 465+30+11, 618+30+20); item 16's `flags=0x0000 method=0` for every local and central record (`:245-247`) ✓. Independent CRC-32 recomputation over each payload: `962d075f`, `2635c82a`, `e948d738` — identical to the printed `crc32_recomputed`.

AXML and dex (`/tmp/revenger-r70-R70W2GateQ06-axml.py`, full stdout):

```
xml header type 3 headerSize 8 size 416 len 416
chunks [(8, 1, 28, 196), (204, 384, 8, 44), (248, 256, 16, 24), (272, 258, 16, 96), (368, 259, 16, 24), (392, 257, 16, 24)]
pool stringCount 9 styleCount 0 flags 0x100 stringsStart 64 stylesStart 0
offsets [0, 10, 55, 66, 76, 94, 108, 122, 126]
strings ['android', 'http://schemas.android.com/apk/res/android', 'manifest', 'package', 'com.example.r65', 'versionCode', 'versionName', '1', '1.0']
rm type 384 hs 8 size 44 ids ['0x0','0x0','0x0','0x0','0x0','0x101021b','0x101021c','0x0','0x0']
startelem type 0x102 hs 16 size 96
attrExt ns 4294967295 name 2 attributeStart 20 attributeSize 20 attributeCount 3 idIndex 0 classIndex 0
 attr 0 ns 4294967295 name 3 raw 4 vsize 8 res0 0 dtype 0x3 data 4
 attr 1 ns 0 name 5 raw 7 vsize 8 res0 0 dtype 0x10 data 1
 attr 2 ns 0 name 6 raw 8 vsize 8 res0 0 dtype 0x3 data 8
dex magic 6465780a30333500 checksum 0x3d120c30 sig a5fc7bea8fa9ffaa52243540c8026066511b9fce filesize 112 hdrsize 112 endian 0x12345678
checksum recomputed 0x3d120c30 sig recomputed a5fc7bea8fa9ffaa52243540c8026066511b9fce
```

Against the entry: item 4's chunk table (`:58`) is identical in every offset/type/headerSize/size, and the walk origin is right — the root chunk's declared `headerSize` is 8, so the first child sits at 8, not 28 (`:54`); item 5's summed widths are consistent with the declared headerSizes (string pool 28, node 16, attrExt 20, attribute 20 — `:67`); item 6 (`:76`) matches field for field (flags `0x00000100` → `utf8 true`, `sorted_flag false`, `stringsStart 64` = 28 + 9×4, `styleCount 0`, `stylesStart 0`, the nine offsets and nine strings); item 7 (`:83`) matches (44−8 = 36 = 9×4, the two non-zero ids `0x0101021b`/`0x0101021c`, seven zeros); item 8 (`:90`) matches (attributeStart 20, attributeSize 20, attributeCount 3, classIndex 0, and each attribute's ns/name/raw/vsize 8/data type/data); item 9 (`:105`) matches (magic, checksum and its adler32 recomputation over bytes 12+, signature and its SHA-1 recomputation over bytes 32+, file_size 112, header_size 112, endian_tag `0x12345678`); item 10 (`:114`) matches (`bytes 69`, `first_line "Manifest-Version: 1.0"`, `section_count 1` — payload is `Manifest-Version: 1.0\r\nCreated-By: …\r\n\r\n`).

Item 2's "the second command locates the same signature on its own … which equals the readout's offset" (`:30`) is confirmed by two independent finds at 925. Items 12 and 17 compare the readout's *source literals* with sums of the manual transcriptions and pass (I re-ran both; 20 and 25 `MATCH` lines, no `MISMATCH`). The snapshot line numbers those blocks print are also true against the snapshot bytes — `ResourceTypes.h:218 struct ResChunk_header`, `:287 struct Res_value`, `:461 struct ResStringPool_header`, `:612 struct ResXMLTree_header`, `:621 struct ResXMLTree_node`, `:677 struct ResXMLTree_attrExt`, `:707 struct ResXMLTree_attribute`, `:237 enum {`, `:239/:241/:244/:245/:246/:247/:248/:253` the eight enum values, `:263 };`, `:686` the `attributeStart` comment, `:687 uint16_t attributeStart;` — all read from the pinned snapshot.

No offset, operand, size or count in items 1-10 and 16 is stated from intent: each is printed by a command, and each printed value survives an independent re-derivation.

## 4. The generator premise — the entry's honesty, and the fact behind it

The entry says, in the S041 header line (`:7`): "…anchors: the four digests printed in item 14, which also prints the digest of `entry_checks.py`; **this entry does not re-run `generator.py`**". That is honest: none of the entry's 25 `$` commands names `generator.py` (`grep -n '^\$ '` lists only `readout.py`, `entry_checks.py`, `derive_axml_anchors.py`; `generator.py` occurs only in prose and in the item-14 listing at `:224`). The Scope paragraph (`:15`) makes the same claim about producer calls ("no producer is called at recheck time"), and it is true of the committed recheck commands.

The premise the entry *relies* on without demonstrating — that the pinned `truth.json` is the generator's output for the pinned `fixture.apk` — I tested myself in a scratch copy of the generator, nothing else present:

```
$ mkdir -p /tmp/revenger-r70-R70W2GateQ06-gen && cp <target>/corpus/fixtures/apk-r65/generator.py /tmp/revenger-r70-R70W2GateQ06-gen/
$ cd /tmp/revenger-r70-R70W2GateQ06-gen && python3 -B generator.py; echo GEN_EXIT=$?
fixture.apk 947 bytes sha256 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e
member AndroidManifest.xml offset=0 size=416 crc32=962d075f
member classes.dex offset=465 size=112 crc32=2635c82a
member META-INF/MANIFEST.MF offset=618 size=69 crc32=e948d738
GEN_EXIT=0
$ sha256sum fixture.apk truth.json
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  fixture.apk
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  truth.json
$ cmp fixture.apk <target>/corpus/fixtures/apk-r65/fixture.apk && echo FIXTURE_IDENTICAL
FIXTURE_IDENTICAL
$ cmp truth.json  <target>/corpus/fixtures/apk-r65/truth.json  && echo TRUTH_IDENTICAL
TRUTH_IDENTICAL
```

So the pinned bytes *are* the built fixture and the built oracle: the premise is true even though the entry does not demonstrate it (origin is Q09's axis, and item 14's own disclaimer at `:218` — "a digest … does not establish who produced them, that a copy was faithfully fetched" — is correct and is not contradicted by any claim the entry makes about the fixture's *bytes*).

Item 13's oracle labelling is also accurate, which matters for Q06 because it decides what the "expected value" is: `truth.json`'s member measurements come from `parse_members(apk)` over the finished ZIP bytes via `zipfile` (`generator.py:175-190`, called at `:196-197`), while `axml_declared` comes from the build declarations `STRINGS`/`ATTRIBUTES`/`RESOURCE_IDS` (`generator.py:206-216`). The entry states exactly this split (`:178`: "The oracle's AXML values are the generator's own build declaration, so agreement shows the readout parses what the generator wrote; it does not show that a declared value … is the Android framework's value for its name"). Checked against the regenerated `truth.json`: `image.size 947`, `image.sha256 05d2280f…`, members `AndroidManifest.xml/classes.dex/META-INF/MANIFEST.MF`, 9 declared strings, 3 declared attributes, 9 declared resource ids — matching item 13's 34 `MATCH` lines one for one.

## 5. "after every edit" — the mechanism and the post-edit re-derivation

`build-entry.py:33-39` builds each fenced block by *running* the command (`run(c)` → `subprocess.run(...)` at `:27`) and pasting `p.stdout`; `:28-29` aborts with `SystemExit` on a non-zero exit, and `main()` writes the entry only after all blocks are substituted (`:196-199`). An edit therefore cannot leave a stale output block: the next build regenerates every line from bytes, and the gate then re-checks every embedded line against fresh stdout.

That this happened for v5.1 (the landed bytes) is visible in git, not in prose:

```
$ git -C <lane> diff --stat aa1842f 17ee7f87 -- corpus/fixtures corpus/snapshots corpus/derive_axml_anchors.py corpus/knowledge/round-70-apk-axml-byte-evidence.md
 corpus/fixtures/apk-r65/entry_checks.py            | 107 ++++++++++++++++++-
 .../knowledge/round-70-apk-axml-byte-evidence.md   | 115 +++++++++++++++------
 2 files changed, 187 insertions(+), 35 deletions(-)
```

The fixture, the oracle, the generator, the readout, the snapshots and the derivation script are unchanged between v5 and v5.1; only the checker and the entry changed — and item 14's digest for the changed checker is the changed file's digest (`2d4f25f6…` = the committed `entry_checks.py`, §2), i.e. the pin set was re-derived after the edit rather than carried over.

Re-running the entry's own recheck commands on the landed bytes (extraction, nothing else touched):

```
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md
checked_blocks=24 problems=0
GATE_EXIT=0
$ python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md
LINT_QMAP=0
LINT_Q14=0
LINT_Q15=0
LINT_HEADER=0
LINT_EXIT=0
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --stdout-digest
readout stdout: 15 lines, sha256 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247
```

24 blocks (25 commands, because item 2's block carries two) with 0 problems, and item 15's printed `15 lines / 507d79f8…` reproduces exactly — so the entry's embedded lines are the current built output, not an earlier pass.

## 6. "failed inputs are retained"

There is no failed fixture input in this entry to retain: all 25 embedded commands exit 0 (gate `problems=0`, and each block's command exits 0 when run by hand), and the fixture rebuilds deterministically (§4). I also checked that no block was *dropped* between candidate v5 and the landed v5.1 rather than repaired:

```
$ diff <(git show aa1842f:corpus/knowledge/round-70-apk-axml-byte-evidence.md | grep '^\$ ') \
       <(git show 17ee7f87:corpus/knowledge/round-70-apk-axml-byte-evidence.md | grep '^\$ ')
22a23,24
> $ python3 -B corpus/fixtures/apk-r65/entry_checks.py --container
> $ python3 -B corpus/fixtures/apk-r65/entry_checks.py --axml-layout
```

Two commands added, none removed: no failing check was hidden by deletion.

Mechanism limit, stated so it is not mistaken for a clean bill: `build-entry.py` aborts *before* writing on a non-zero exit (`:28-29`, write at `:199`), so a failed command's stdout is never pasted into the entry and is not retained in any committed artifact of this entry — the retention clause is satisfied vacuously here (nothing failed), but the builder does not record a failure when one occurs. This is a property of an undigested builder outside `corpus/`; it is not a located defect in the landed bytes and no fixture premise rests on it.

## 7. Adjacent findings — located, but **not** Q06 decisions (handoff to the Q04/Q09/Q11 seats)

These are real prose defects in the same entry. They are not Q06 rejects: none of them makes a *fixture premise* (offset, operand, size, count of the built fixture) wrong, and Q06's reject clause is about those premises. I record them so they are not lost, and I do not decide them.

1. **`:152` (item 12), positional claim is false.** "…the last three lines print where each record layout sits in the snapshot (heading line and the first and last transcribed field lines)." The command's output is 20 lines; the three APPNOTE locator lines are lines 16-18, and the last three are `MATCH APPNOTE 4.3.16` + `MATCH central.fixed_part` + `MATCH local.fixed_part`:
   ```
   $ python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout | nl -ba | tail -5
       16	MATCH APPNOTE 4.3.7: heading line 387, transcribed field lines 389-399
       17	MATCH APPNOTE 4.3.12: heading line 511, transcribed field lines 522-538
       18	MATCH APPNOTE 4.3.16: heading line 632, transcribed field lines 634-646
       19	MATCH central.fixed_part: spec width 46, readout.py literal `cursor + 46` present=True
       20	MATCH local.fixed_part: spec width 30, readout.py literal `lh_off + 30` present=True
   ```
   The printed values themselves (387/389-399, 511/522-538, 632/634-646) are correct. Smallest safe correction: replace "the last three lines print where each record layout sits in the snapshot" with "the three `MATCH APPNOTE` lines print where each record layout sits in the snapshot, followed by the two fixed-part width checks".
2. **`:218` (item 14), scope of "the commands above".** "Digests and sizes of the ten files under `corpus/` that the commands above read" — `generator.py` is read by none of items 1-13; it is hashed only by item 14's own `--pins` (`entry_checks.py:40-51` lists it; `readout.py` never opens it). Nine of the ten are read above; the tenth is the producer script. The count (10) and every digest are correct. Smallest safe correction: "the ten files under `corpus/` the commands read — nine by items 1-13, and `generator.py` by this item's own command".
3. **`:19` "saved verbatim" vs `:218`'s disclaimer.** `:19` says the readout "is saved verbatim; its digest is item 14's", while `:218` correctly says a digest "does not establish who produced them, that a copy was faithfully fetched". There is no second copy of `readout.py` in the tree against which "verbatim" could be checked, so the phrase is unsupported by the entry's own evidence (it is not falsified either). Q09 territory; smallest safe correction: "its digest is item 14's, which identifies exactly these bytes".

None of the three changes a Q06 outcome, and none is a FAIL input for C1 from this seat.

## 8. Decision

**Q06 = PASS**, on the landed candidate bytes at `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd`.

Basis, all re-derived above: (i) all ten item-14 digests and sizes equal the committed files, hashed both by the entry's command and by `sha256sum`/`stat`; (ii) every fixture premise in items 1-10 and 16 reproduces from an independent struct walk of `fixture.apk`, including the four payload offsets, the six-chunk AXML table, the string-pool offsets, the three attributes and the dex header; (iii) the entry is honest that it does not re-run `generator.py`, and a scratch re-run proves the pinned fixture and oracle are byte-identical to the generator's output, so the premise it relies on is true; (iv) the post-edit pin refresh is visible in git (only the checker and entry changed; the checker's new digest is the changed file's digest) and the gate re-checks 24 blocks with 0 problems; (v) no failed input exists and none was dropped between v5 and v5.1 (two commands added, none removed).

Per the frozen kill rule (`reports/round-70/claims.md` §C1), this is one PASS decision for the non-mechanical conjunct of C1; it does not override any mechanical label, and it is scoped to Q06 only.

## 9. Reproduce

```sh
D=$(mktemp -d /tmp/revenger-r70-rerun-XXXX)
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd corpus SHONEN.md SCORECARD.md SKILL.md | tar -x -C "$D"
cd "$D"
python3 -B corpus/fixtures/apk-r65/entry_checks.py --pins          # ten digests, §2
python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout    # 20 lines, §7.1
python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md
G=$(mktemp -d /tmp/revenger-r70-rerun-gen-XXXX); cp corpus/fixtures/apk-r65/generator.py "$G/"
(cd "$G" && python3 -B generator.py && cmp fixture.apk "$D/corpus/fixtures/apk-r65/fixture.apk" && cmp truth.json "$D/corpus/fixtures/apk-r65/truth.json")
```

Tooling: nothing installed or upgraded (pacman paused; no `uv`/`npx` needed). Scratch deleted before returning.
