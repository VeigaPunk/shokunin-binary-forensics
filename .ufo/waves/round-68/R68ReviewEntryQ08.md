FAIL (Q11, applied for Q08) — the v3 entry's derivation item 11 is not complete over the entry's own claims: two S038 line numbers the entry states (`entry:148` `line 244 is RES_XML_FIRST_CHUNK_TYPE`, and the enum-block start `237` used at `entry:1,57,148,157`) are absent from the derivation command's output while `entry:7`, `entry:156` and `entry:194` assert that every S038 line number the entry cites/states is printed there; the stated block extent `237-253` is also factually wrong (the `enum {` at 237 closes at `};` 263, so the block spans 237-263).

Seat: `L1Revenger68.R68ReviewEntryQ08` (fresh leaf, non-author). Entry under test: `corpus/knowledge/round-68-apk-axml-byte-evidence.md` (215 lines, tracked). Criterion: **Q08 — superseded by Q11 — apply Q11 and say so** — `corpus/QUALITY.md:20` (Q08 row) and `corpus/QUALITY.md:23` (Q11 row, "Supersedes Q08 … Each count, identifier, offset and digest in an entry carries, inside the entry, the command that derives it from the primary record … and that command's output. Constants such as header offsets are derived, not assumed. A value cited only to prose is labeled recorded, not re-derived."). Read-only seat: no edits, no git/jj mutation, no writes outside this report path, no tool installs.

## 0. Criterion routing (the "say so" half) — PASS

The entry's `§Q-map` Q08 row reads `superseded by Q11 | QUALITY.md:23 — Q08 is historical; this map applies Q11`. Verified: `QUALITY.md:20` is the Q08 row; `QUALITY.md:23` is the Q11 row whose first clause is `Supersedes Q08`. The pointer resolves to the supersession, and no Q08-shaped test is applied anywhere in the map. Routing is correct; the verdict below is Q11's text applied to these bytes.

## 1. Derivation surfaces that re-derive clean (evidence runs)

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && python3 -B corpus/derive_axml_anchors.py ; echo EXIT=$?
sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f ResourceTypes.h
struct ResChunk_header : 218
struct Res_value : 287
struct ResStringPool_header : 461
struct ResXMLTree_header : 612
struct ResXMLTree_node : 621
struct ResXMLTree_attrExt : 677
struct ResXMLTree_attribute : 707
enum RES_STRING_POOL_TYPE : 239
enum RES_XML_TYPE : 241
enum RES_XML_START_NAMESPACE_TYPE : 245
enum RES_XML_END_NAMESPACE_TYPE : 246
enum RES_XML_START_ELEMENT_TYPE : 247
enum RES_XML_END_ELEMENT_TYPE : 248
enum RES_XML_RESOURCE_MAP_TYPE : 253
comment attributeStart : 686
field attributeStart : 687
EXIT=0
```
17 lines, exit 0 — byte-identical to the block embedded at `entry:127-146` (command `entry:128`, output `entry:129-145`), including the `:245` anchor and the 686/687 comment/field pair.

```
$ python3 -B corpus/fixtures/apk-r65/readout.py   → EXIT=0, 15 stdout lines
$ sha256sum /tmp/r68q08-readout.txt
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  /tmp/r68q08-readout.txt
```
Matches the pins at `entry:7` and `entry:194` exactly.

Programmatic comparison of every JSON line pasted in the entry against that fresh stdout:
- 30 embedded JSON-line occurrences in the entry, 15 distinct; all 30 `in_actual_exact=True` (zero drift).
- The full-stdout block at `entry:200-214` is 15 lines, `ORDER MATCH: True` against the live run (sequence `archive, spec_derived_struct_widths, eocd, member[AndroidManifest.xml], member[classes.dex], member[META-INF/MANIFEST.MF], axml_chunk_table, axml_string_pool, axml_resource_map, axml_start_namespace, axml_end_namespace, axml_start_element, axml_end_element, dex_declared_header, jar_manifest`).
- The long line at `entry:86` (`axml_start_element`, 890 bytes) is *not* truncated in the file; only the reader display truncated it. No M39-class drift anywhere (the r65 `Manifst-Version` defect does not recur; `payload_first16_hex: 4d616e69666573742d56657273696f6e` is the 16-byte `Manifest-` prefix the command prints).

Independent re-derivation of the item-5 constants against S038's struct bodies (`corpus/snapshots/ResourceTypes.h`):
- `ResChunk_header` (218): `uint16 type; uint16 headerSize; uint32 size` → `[2,2,4]` = 8 ✔
- `Res_value` (287): `uint16 size; uint8 res0; uint8 dataType; uint32 data` → `[2,1,1,4]` = 8 ✔
- `ResXMLTree_node` (621): header 8 + `uint32 lineNumber` + `ResStringPool_ref comment` → 16 ✔
- `ResXMLTree_attrExt` (677): `ns 4 + name 4 + six uint16` → 20, which is exactly the observed `attributeStart` 20 ✔ and consistent with `chunk_base + 16` (`readout.py:203` = `aoff = base + 16 + attribute_start + i * attribute_size`, matching the cited `readout.py:200-203`) ✔
- `ResXMLTree_attribute` (707): `ns 4 + name 4 + rawValue 4 + Res_value 8` → 20, exactly the observed `attributeSize` 20 ✔
- `attrExt` provenance quote "Appears header.headerSize bytes after a `ResXMLTree_node`" is at snapshot **675**, and the quoted `attributeStart` comment/declaration at **686/687** ✔ (the r67 range `685-687` was wrong because 685 is blank; the v3 686/687 pair is correct and derived).

Digests spot-verified on disk (values stated in the entry are correct):
```
bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249  corpus/derive_axml_anchors.py   (entry:4)
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h (entry:1,4; 86255 bytes ✔)
56b88bc4…  .ufo/waves/round-65/source-snapshots/ResourceTypes.h  (byte-exact copy ✔; 86255 bytes)
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py  (entry:5)
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  corpus/fixtures/apk-r65/truth.json   (entry:5)
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk  (entry:1)
412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c  .ufo/waves/round-65/source-snapshots/rea-android-applications.md (entry:2)
c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4  .ufo/waves/round-67/source-snapshots/dex-format.html (entry:3)
```
S043's quoted sentence really does straddle snapshot lines 7-8 ("Start with `inspect_android_package` on the caller's APK path for package / identity, manifest declarations, coverage, and inline Evidence."), and all four S045 quoted clauses ("adler32 checksum of the rest of the file", "SHA-1 signature", "must be 0x70 (112)", "ENDIAN_CONSTANT = 0x12345678") are present in the dex-format snapshot.

Registered gate re-run (context, not my criterion):
```
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md
checked_blocks=17 problems=0   (exit 0)
```

## 2. Finding F1 — HIGH, fails Q11: a stated S038 line number is not printed by the command the entry presents as deriving every such line

`entry:148` (item 11, the derivation item itself):

> The chunk-type enum block spans lines 237-253 and `RES_XML_START_NAMESPACE_TYPE` is line **245**; **line 244 is `RES_XML_FIRST_CHUNK_TYPE`**.

`244` does not appear in `python3 -B corpus/derive_axml_anchors.py`'s stdout (§1, full 17 lines above), and `RES_XML_FIRST_CHUNK_TYPE` is not one of the script's `ENUMS`/`STRUCTS` (`corpus/derive_axml_anchors.py:35-56`). The value itself is *correct* when re-derived independently:

```
$ awk 'NR==244||NR==245' corpus/snapshots/ResourceTypes.h
244:     RES_XML_FIRST_CHUNK_TYPE          = 0x0100,
245:     RES_XML_START_NAMESPACE_TYPE      = 0x0100,
```
(so the correct value is **244**, and the correct identifier at 245 is `RES_XML_START_NAMESPACE_TYPE`; note both are `0x0100` aliases).

This is Q11's reject clause verbatim — "a value is correct when re-derived but the entry carries no derivation" — and it is aggravated by four completeness assertions that the output contradicts:

- `entry:7` (`recheck:`) — "… (every S038 line number this entry cites; exits 2 if a cited symbol is missing or ambiguous)".
- `entry:156` (Observation) — "every spec line number in item 11, derived from the pinned snapshot bytes by a committed script that cannot print a line it did not find".
- `entry:194` (`## Reproduce`) — "Anchor derivation … exit 0, **17 lines, one per cited symbol** (item 11)".
- `entry:4` (S046 row) — "**17 output lines** over `corpus/snapshots/ResourceTypes.h`".

Required derivation, then re-embed: add `RES_XML_FIRST_CHUNK_TYPE` (and the enum-bound symbols of F2) to `corpus/derive_axml_anchors.py`, re-run, paste the new stdout, and update every "17" count (`entry:4`, `entry:194`, item 11's `17` if restated) plus S046's output-line count in `corpus/SOURCES.md`. No numeric anchor changes are required by F1 — only the missing derivation.

## 3. Finding F2 — HIGH, fails Q11: the "chunk-type enum block lines 237-253" span is neither derived nor correct as an extent

Stated four times: `entry:1` ("chunk-type enum block **lines 237-253**"), `entry:57` ("S038's chunk-type enum block names at **lines 237-253**"), `entry:148` ("The chunk-type enum block spans lines 237-253"), `entry:157` ("S038's enum block (lines 237-253)").

- The start **237** is not printed by the derivation command (the first printed enum line is 239). It is correct (`237: enum {`), but un-derived — same reject clause as F1.
- As an *extent* the range is wrong. The enum that opens at 237 continues past 253 into the `RES_TABLE_*` chunk types and closes later:
```
$ python3 - <<'EOF'   # walk from the first `enum {`
enum opens at 237 closes at 263
EOF
$ awk 'NR==237||NR==255||NR==256||NR==263' corpus/snapshots/ResourceTypes.h
237: enum {
255:     // Chunk types in RES_TABLE_TYPE
256:     RES_TABLE_PACKAGE_TYPE            = 0x0200,
263: };
```
So the block spans **237-263**. Correct value: either "the enum block, lines 237-263" (with both bounds derived by the script) or, if only the cited XML chunk-type entries are meant, "the cited entries at lines 239-253" — in which case the phrase "the chunk-type enum block" must not carry `237`/`253` as its bounds. Either way the range endpoints must appear in the derivation output; today `253` appears only incidentally as the `RES_XML_RESOURCE_MAP_TYPE` anchor, and `237`/`263` appear nowhere.

(For the record: `entry:1`'s contrast claim about the round-65 draft — "unlike the round-65 draft's :239-250" — is accurate about those bytes, `grep -c ':239-250' corpus/knowledge/round-65-apk-axml-byte-evidence.md` → 1.)

## 4. Findings that are LOW under Q11 and are NOT the fail basis (recorded so the next pass does not re-litigate them)

- **L1 — header/source digests carry no in-entry `sha256sum` command + output.** `readout.py` (`entry:5,17,194`), `truth.json` (`entry:5`), the S043 snapshot digest (`entry:2`), the S045 snapshot digest (`entry:3`), and the derive-script digest (`entry:4`, `entry:17`) are stated as anchors of source rows; only the snapshot digest (`entry:129`) and the fixture digest (item 1, `entry:25`) are printed by a command inside the entry. I verified all of them on disk (§1) — values correct, presentation gap only, the same LOW category `.ufo/waves/round-65/R65ReviewEntryQ11.md` Finding 3 and `.ufo/waves/round-67/R67ReviewEntryQ11.md` §5 treated as non-failing.
- **L2 — the EOCD signature hex `504b0506` (`entry:28`) is not printed.** The `eocd` fact prints `eocd_offset: 925` only; the literal lives in `readout.py:76`. Unchanged from r65 Q11 Finding 2.
- **L3 — the ZIP fixed-part constants 46 and 30 (`entry:35`) are literals in `readout.py:96` and `readout.py:105` with a prose pointer to S032 §4.3.12 / S034 §4.3.7, not a printed derivation.** Same category as L1/L2 (the payload offsets that *use* them are printed, so the arithmetic is auditable).
- **L4 — item 5's `bytes_per_field` is a transcribed table that is then summed, not read from the snapshot.** `readout.py:52-59` hardcodes `[w16,w16,w32]` etc.; the printed addends make the sums auditable, and I re-derived every one against S038's bodies (§1) with no mismatch — so the constants are correct and the addends are shown, but the "computed … not assumed" wording at `entry:59` oversells the mechanism slightly. Not a Q11 fail given the printed addends.

## 5. OFF-criterion observations (owners: Q03/Q06/Q10; not scored here)

- `entry:75` and `entry:152` claim agreement with the authored oracle (`truth.json` `axml_declared.resource_ids`, "agree with it on every shared field") with no comparison command/output shown. I reproduced it independently: `truth.json` ids = `["0x00000000"×5, "0x0101021b", "0x0101021c", "0x00000000"×2]`, identical to the readout's `ids` array — the claim is true, the evidence is absent (same INFO as r65 Q11 Finding 4).
- Item 8's `ns_index: 4294967295` is labeled "recorded as observed and treated as null" (`entry:89`) — that is the labeling Q11's last sentence wants; correct, and the `NO_INDEX = 0xFFFFFFFF` it points to is `readout.py:22` as cited.
- Untracked `corpus/__pycache__/` exists in the lane working tree (`git status --porcelain corpus/` → `?? corpus/__pycache__/`). Not mine (every command of mine ran `python3 -B` or stdin scripts); it is a sibling-seat artifact or pre-existing. The build files themselves are tracked: `git ls-files` returns all three of `corpus/derive_axml_anchors.py`, `corpus/snapshots/ResourceTypes.h`, `corpus/knowledge/round-68-apk-axml-byte-evidence.md`.

## 6. Residual risk and verification gaps

- **The registered gate cannot catch F1/F2.** `check_embedded_outputs.py` re-checks that each embedded output line appears in its command's stdout; a *missing* output line (a stated anchor the command never prints) is invisible to it — hence `17 blocks, 0 problems` coexists with F1/F2. `C7_V3_CLEAN=yes` therefore does not carry the completeness claim at `entry:7/156/194`. (Q13-adjacent; reported, not absorbed.)
- I did not run the round-68 counter or the census; I did not read `corpus/README.md`'s C05 row or the `K_HELD_BACKED` machinery; I did not re-audit Q01-Q07/Q09/Q10/Q12/Q13. Those are other seats' surfaces.
- My verdict is on derivation *coverage* and one wrong span endpoint. No embedded output line drifts, no fixture/oracle/dex value is wrong, and every individual spec anchor cited as a point (218, 239, 241, 245, 246, 247, 248, 253, 287, 461, 612, 621, 677, 686, 687) is correct.
- **Adjudication note (explicit, so Main can weigh it):** F1 and F2 are mechanical — the values are correct and the fix is a two/three-symbol extension of a committed script plus a re-embed and a count update. If the adjudicator applies the *lenient* Q11 reading used by the r67 seat (which passed a v2 entry carrying the wrong `:244` anchor and never tested derivation coverage), F1/F2 would downgrade to LOW. Under this round's seat rule ("a value that the command does not print is a FAIL for Q11") and Q11's reject clause ("a value is correct when re-derived but the entry carries no derivation"), the v3 bytes fail Q11 as they stand. I record FAIL.

Tooling: no installs or upgrades this seat (system `python3`, `awk`, `sha256sum`, `grep` sufficed).

Report: `.ufo/waves/round-68/R68ReviewEntryQ08.md`
