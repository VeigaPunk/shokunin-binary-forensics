PASS — Q13: item 11's credit is bounded to the 20-line printed set; the 19 cited S038 line numbers equal the printed set exactly; and deletion is detected in every class the entry credits (missing symbol → exit 2; deleted script clause → gate exit 1 naming entry:147; corrupted embedded line → gate exit 1 naming entry:143).

seat: L1Revenger69.R69ReviewEntryQ13 (leaf, Q13 only) · date 2026-10-25
target: /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-69-apk-axml-byte-evidence.md (sha256 of the file is not pinned by the entry; bytes read as-is)
criterion: corpus/QUALITY.md:24 (Q13) — "A verifier or recheck command is credited in an entry only for the clauses whose deletion its own run is shown to detect; other clauses are named as unguarded."
role: fresh admission reviewer; no edits to any lane file; no subagents; no installs (no tool install/update performed).

## What Q13 tests on these bytes

The entry credits two commands: `corpus/derive_axml_anchors.py` (entry:6 S047 source row, entry:9 `recheck:`, entry:127 item 11, entry:194 §Reproduce) and `corpus/fixtures/apk-r65/readout.py` (entry:9 `recheck:`, entry:194, plus the per-item blocks). Item 11 is the clause under test: does its credit match what the command prints, and is a deletion in that credit set detected?

## Evidence 1 — the command's own stdout, re-derived, compared to the embedded block

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && python3 -B corpus/derive_axml_anchors.py; echo "EXIT=$?"
sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f ResourceTypes.h
struct ResChunk_header : 218
struct Res_value : 287
struct ResStringPool_header : 461
struct ResXMLTree_header : 612
struct ResXMLTree_node : 621
struct ResXMLTree_attrExt : 677
struct ResXMLTree_attribute : 707
enum block open : 237
enum RES_STRING_POOL_TYPE : 239 = 0x0001
enum RES_XML_TYPE : 241 = 0x0003
enum RES_XML_FIRST_CHUNK_TYPE : 244 = 0x0100
enum RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100
enum RES_XML_END_NAMESPACE_TYPE : 246 = 0x0101
enum RES_XML_START_ELEMENT_TYPE : 247 = 0x0102
enum RES_XML_END_ELEMENT_TYPE : 248 = 0x0103
enum RES_XML_RESOURCE_MAP_TYPE : 253 = 0x0180
enum block close : 263
comment attributeStart : 686
field attributeStart : 687
EXIT=0
```

`wc -l` = 20. Byte-for-byte diff of this stdout against the embedded block at entry:129-150 (the `$ python3 -B corpus/derive_axml_anchors.py` fence): **empty, DIFF_EXIT=0** — the embedded block is exactly the command's stdout, not a transcription.

Pins check out: `sha256sum corpus/derive_axml_anchors.py` = `74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa` (S047, entry:6), `corpus/snapshots/ResourceTypes.h` = `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f` (entry:6 and the derived digest line), `corpus/fixtures/apk-r65/readout.py` = `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976` (entry:9, entry:39). The readout recheck also holds: `python3 -B corpus/fixtures/apk-r65/readout.py` → exit 0, 15 lines, sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` exactly as entry:9/194 state, and the embedded "Full stdout" block (entry:199-215) is identical to the actual 15 lines (`identical: True`).

## Evidence 2 — the bound parses, and the cited set equals the printed set

Mechanical extraction of every `:NNN` / `line(s) NNN` S038 anchor from the prose (entry:1 header, entry:59 item 4, entry:84 item 8, entry:127/153 item 11) against the 20 printed lines:

```
PRINTED nums: [218, 237, 239, 241, 244, 245, 246, 247, 248, 253, 263, 287, 461, 612, 621, 677, 686, 687, 707]  (19 distinct + 1 digest line = 20 lines)
line 1:  unprinted=[]   line 59: unprinted=[]   line 153: unprinted=[]   line 162: unprinted=[]
line 84: unprinted=[200]   -> 200 is "readout.py:200-203", a readout.py code line, not an S038 line
printed-not-stated: [621]  -> stated on entry:1 as "`ResXMLTree_header`/`ResXMLTree_node` (lines 612, 621)"
stated-not-printed: []
block grouping 1+7+2+8+2 = 20, actual lines: 20
```

So the equality holds in both directions (19 cited line numbers = 19 printed line numbers), and item 11's parenthetical grouping (entry:127: "1 digest line + 7 struct lines + 2 enum-block bound lines + 8 enum lines + 2 attributeStart lines") parses to exactly the 20 output lines. `STRUCTS` has 7 names and `ENUMS` has 8 names in `corpus/derive_axml_anchors.py:44-63`, matching. The v3 defect (reports/round-68 summary: "the credit is bounded to 16 of 18 numbers") is closed: `:237` and `:244`, unprinted in v3, are printed here (lines "enum block open : 237", "enum RES_XML_FIRST_CHUNK_TYPE : 244 = 0x0100").

Item 11's own bound sentence (entry:127) reads: "The credit is bounded to exactly the numbers the command prints: the 20-line stdout below ... is the complete set of S038 line numbers this entry states" — this is the bounded form, not a universal "every line" overstatement.

## Evidence 3 — deletion is detected (the Q13 leg that v3 failed)

(a) Delete a cited symbol from the snapshot (`/tmp` copy, pin re-aimed to the mutant digest):

```
$ python3 -B derive_axml_anchors.py
derive_axml_anchors: enum RES_XML_RESOURCE_MAP_TYPE: not found
MUTANT_EXIT=2
```

(b) Delete one enum clause from the verifier script (`ENUMS` entry removed, `/tmp` tree) and run the registered gate against a copy of the entry:

```
$ python3 -B corpus/check_embedded_outputs.py --entry entry.md
drift entry:147 embedded output line not in recheck stdout: enum RES_XML_RESOURCE_MAP_TYPE : 253 = 0x0180
checked_blocks=1 problems=17        (exit 1; 16 other problems are the readout commands absent from the stub tree)
```

(c) Corrupt one embedded output line (`:245` → `:244`, the exact M40/M44 error) and run the gate on the real entry copy:

```
$ python3 -B corpus/check_embedded_outputs.py --entry /tmp/revenger-r69-q13-drift.md
drift entry:143 embedded output line not in recheck stdout: enum RES_XML_START_NAMESPACE_TYPE : 244 = 0x0100
checked_blocks=17 problems=1
DRIFT_EXIT=1
```

(d) The registered gate on the actual bytes is clean:

```
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-69-apk-axml-byte-evidence.md
checked_blocks=17 problems=0
GATE_EXIT=0
```

Each printed value therefore has a check whose deletion the credited run detects: `find_unique` (symbol absent/ambiguous → exit 2), the `VALUE_RE` extraction (a broken value prints `?`, which the gate reports as drift), and the verbatim block comparison for the printed set itself.

## Evidence 4 — the unguarded clauses are named

The only S038-derived material the derivation does not print is item 5's struct field widths. Item 5 names it unguarded at entry:61: "**manually transcribed** in `readout.py:51-58` from S038's own struct field lists ... a manual transcription, labeled manual, not a runtime derivation; the readout merely prints the constants and the sums". S047's scope sentence repeats the exclusion at entry:6: "not the layout facts themselves, which rest on S038". Item 11's bound is worded "S038 line number and enum value" (entry:127), so the width table is outside the credit. Verified pointers: `readout.py:52-58` is the `widths` dict (6 structs), `readout.py:166` is `utf8=bool(flags & 0x100)`, `readout.py:22` is `NO_INDEX = 0xFFFFFFFF`, `readout.py:99-105` ends at `payload_off = lh_off + 30 + lh_name_len + lh_extra_len`, `readout.py:200-203` ends at `aoff = base + 16 + attribute_start + i * attribute_size` — every line the entry cites for the readout is the line it says it is.

## Residual risks (recorded; none reaches the Q13 reject trigger on these bytes)

1. **entry:9 (`recheck:`) and entry:194 (§Reproduce) drop the word "enum".** They say "every S038 line number and value this entry cites", while item 11 (entry:127) bounds the same credit to "items 4, 8 and 11" and to "enum value". Read as coverage, the derivation prints 19 line numbers and 8 enum values and nothing else, so if "value" is read to include item 5's struct field widths (S038 field-list values the script does not print) the sentence is broader than the printed set. This does not fail Q13 because the widths are named manual in item 5 and excluded by S047's scope, i.e. "other clauses are named as unguarded"; the smallest correction is to write "every S038 line number and enum value this entry cites" (or "the 19 line-number and 8 enum-value lines the command prints") in both places.
2. **The registered gate's comparison is one-way** (`corpus/check_embedded_outputs.py` `drift()`: `l not in stdout_set`). Removing one embedded output line from the entry still passes: `$ python3 -B corpus/check_embedded_outputs.py --entry /tmp/revenger-r69-q13-omit.md` → `checked_blocks=17 problems=0`, `OMIT_EXIT=0`. On these bytes the block is complete (20/20 identical to stdout, Evidence 1), so no credited value is false; but an entry-side omission of a printed line is not deletion-detected. This belongs to the open D5 counter/gate ground, not to this entry's Q13 verdict.
3. The retained round-68 v3 entry now drifts under the extended script (`--entry corpus/knowledge/round-68-apk-axml-byte-evidence.md` → 7 drift lines, exit 1). It is byte-preserved as evidence (Q09) and was not edited, which is what C1 requires; noted only so the Gate does not read that drift as a v4 defect.

## Verdict

**Q13 = PASS** on `corpus/knowledge/round-69-apk-axml-byte-evidence.md` as read: the credit is bounded to the printed 20-line set (item 11, entry:127), every cited S038 line number and enum value is printed by the named command with its actual stdout embedded verbatim, deletion in each credited class is detected by the command's own run or the registered gate, and the one unguarded class (struct field widths) is explicitly labeled manual at entry:61 with the S047 scope fence at entry:6.

No file in the lane repo was written; `/tmp/revenger-r69-q13-*` scratch was used and removed. No tool install or update was performed.
