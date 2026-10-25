FAIL (advisory) — 11 located prose defects: 3 universal-quantifier overreaches that a wave-2 Q11/Q09/Q01 seat can cite with path:line, 4 unlabeled/unprinted assertions, 4 wording/count errors. No fabricated value: all 22 embedded command blocks reproduce byte-identically from the candidate tree.

seat: R70W1Prose · target: `corpus/knowledge/round-70-apk-axml-byte-evidence.md` at `aa1842fac199aa524930e5565ed3715de5f84c6d` (read via `git -C … show aa1842f:…`, extracted to `/tmp/revenger-r70-Prose` with `git archive`; the lane working tree was never read or written). Entry line numbers below are that blob's (`cat -n`). No file in the lane was edited; scratch deleted.

## 1. Reproduction — the OBSERVED class is sound

Method: parse every fenced block, run each `$ cmd` in the extracted tree, compare stdout line-for-line and require exit 0.

```
commands found: 22
bad: 0
```

So every printed value in items 1-15 is OBSERVED and paste-faithful (item 11's "complete set" = 20 lines, exact; item 12 = 14 MATCH; item 13 = 28 MATCH; item 14 = 9 pins; item 15 = `15 lines, sha256 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — all reproduced). The defects below are therefore *labeling and universal-quantifier* overreach, not data error.

Classification ledger (entry prose, non-block): OBSERVED 27 sentences · RECORDED 3 (item 3 ZIP widths line 39; item 12 line 152; item 5 line 63 — the last mislabeled in one word, F4) · INFERRED 5 (inference (a)-(d) line 234 + item 8's literal-16 sentence) · UNSUPPORTED/overreaching 11 (F1-F11).

## 2. Findings

### F1 — HIGH — entry:175 (item 13): "compared field by field" is false for 9 declared oracle fields
`truth.json` declares 7 keys per member (`["compressed_size","crc32","local_header_offset","method","name","sha256","uncompressed_size"]`) and 5 per attribute (`data`, `data_type`, `name_idx`, `ns_idx`, `raw_value_idx`). `entry_checks.py:134-140` compares 4 member fields; `:142-147` compares 4 attribute fields. Uncompared: `method` (truth.json:79, 88, 97), `uncompressed_size` (:82, 91, 100), attribute `data` (:5, 12, 19) — 9 fields.
Corrected sentence: "The readout's facts compared with the authored oracle `truth.json` on the four per-member fields (local_header_offset, compressed_size, crc32, sha256) and the four per-attribute fields (name_index, ns_index, raw_value_index, data_type); the oracle also declares each member's `method` and `uncompressed_size` and each attribute's `data`, which this block does not compare."
Note the coupling: `method` is exactly the field F3 asserts without derivation.

### F2 — HIGH — entry:209 (item 14): "every file this entry's claims rest on" omits the checker
The block's 9 lines are `entry_checks.py:34-43` `PINS` verbatim. `corpus/fixtures/apk-r65/entry_checks.py` (sha256 `68b1124fff206cc43c957cc3eb4e203c03a622ee4fd010075c884fe333e56049`) produces item 2's second command and items 12, 13, 14, 15 and is pinned nowhere. `corpus/QUALITY.md` (the Q08 row's basis) is likewise unpinned.
Corrected: "Digests and sizes of every fixture, snapshot and derivation-script file this entry's claims rest on …" — or, better, add `corpus/fixtures/apk-r65/entry_checks.py` (and `corpus/QUALITY.md`) to `PINS`.

### F3 — HIGH — entry:239 (Limitations): "The container is stored (method 0) with no data descriptors" is underivable in-entry
No command prints a ZIP compression method or general-purpose flag. `grep -n 'method' readout.py` → no hit; the only `flags` in the readout is the AXML string-pool flags (`readout.py:152, 166`). `entry_checks.py` transcribes `("flags", 2), ("method", 2)` (`:20-21`) but `--zip-layout` prints only the 14 offsets in `READOUT_USES` (`:41-54`) plus two fixed parts. The claim is true of the bytes (local header @0: flags `0x0000`, method `0x0000`; central @737: flags `0x0000`, method `0x0000`) yet nothing in the entry derives it — `QUALITY.md:23` Q11's fail condition is "a value is correct when re-derived but the entry carries no derivation". This also falsifies the §Q-map Q11 row (entry:259, "every count, offset, identifier and digest carries its deriving command").
Corrected: "The container is stored (method 0) and its local headers carry no data-descriptor flag, as the oracle's `build_recipe.container` and each member's `method` record (`truth.json`, digest item 14); the readout reads no compression method or general-purpose flag byte, so the walk does not exercise compression, split archives or spanned records."

### F4 — MEDIUM — entry:63 (item 5): "The fixed structure widths the readout **uses**" — it does not use them
`sizes` occurs only in the emit (`readout.py:65-68`). Every AXML read uses typed literals: `so + 8/12/16/20/24` (`:150-154`), `base + 8/16/20/24/26/28/30/32/34` (`:189-195`), `aoff` (`:203`), `aoff + 4/8/12/15/16` (`:206-210`). No command compares those literals with the sums — unlike the ZIP literals, which item 12 does compare (`entry_checks.py:132-149`). Only the literal 16 is tied to a sum (inference (b)).
Corrected: "The fixed structure widths the readout prints, and that its literal read offsets must match, are a manual transcription of S038's struct field lists (`readout.py:51-58`), labeled manual and not read from `ResourceTypes.h` at run time; the readout prints the constants and their sums."
Repair (stronger): a `--axml-layout` check comparing each AXML literal against the sums, mirroring item 12.

### F5 — MEDIUM — entry:101 (item 9): "Each declared field is compared with the field semantics S045 states (the four quoted phrases …)"
Four quoted phrases (dex-format.html:5949, 5956, 5981, 5035) cover checksum, signature, header_size, endian_tag. The block prints 9 fields/derived values; `magic_hex/magic_ascii`, `format_version`, `file_size`, `header_bytes` have no quoted phrase. The entry's own inference (d) (entry:234) names exactly four fields, so item 9's "Each" contradicts it.
Corrected: "The four declared fields S045's quoted phrases cover — checksum, signature, header_size, endian_tag — are compared with those phrases; `magic`, `format_version`, `file_size` and `header_bytes` are printed without a quoted S045 phrase and no semantics are claimed for them."

### F6 — MEDIUM — entry:61 (item 4): "the correspondence … is read by the reader from those two blocks" fails for `0x0100`
Item 11 prints `RES_XML_FIRST_CHUNK_TYPE : 244 = 0x0100` **and** `RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100` (entry block lines 134-135). Value matching alone therefore does not name the type-256 chunk at offset 248; the identification comes from item 8's `axml_start_namespace` fact (offset 248).
Corrected: "…; the `0x0100` value is shared by `RES_XML_FIRST_CHUNK_TYPE` and `RES_XML_START_NAMESPACE_TYPE` in that block, and the chunk at offset 248 is identified as the start-namespace chunk by the item-8 `axml_start_namespace` fact, not by its value alone."

### F7 — MEDIUM — entry:152 (item 12) and header line 4: the cited APPNOTE ranges do not contain the fields transcribed
Snapshot `corpus/snapshots/APPNOTE.TXT` (sha256 `0b993022…`, item 14): §4.3.7 field lines are **389-399** (`extra field length` is 399; entry cites 387-398). §4.3.12 field lines are **522-538** (`file name length` 532, `extra field length` 533, `file comment length` 534, `relative offset of local header` 538; entry cites 511-531, which stops at `uncompressed size` 531). So the four central fields item 12 derives offsets 28/30/32/42 from lie **outside** the cited range; lines 511-521 are section title/abbreviation, not field definitions. EOCD 632-646 is correct.
Corrected ranges: local `389-399`, central `522-538`, EOCD `634-646` (section opens at 387/511/632).

### F8 — LOW-MEDIUM — entry:79 (item 7): "The resource-map chunk holds one `uint32` per string"
An S038 array-layout fact, but item 11 prints only the enum line 253, no layout line; `readout.py:174` sizes the loop from `string_count`, so the chunk's own extent is never checked. It is derivable from printed values (44-byte chunk − 8-byte header = 36 = 9 × 4) but is stated unlabeled.
Corrected: "The resource-map chunk's printed size (44) less its printed header (8) is 36 bytes, 9 × 4 — one `uint32` per string (item 4's table); the array layout is S038's and its line is not among the lines item 11 prints."

### F9 — LOW — entry:273 (Reproduce): count/list mismatch
"The five derivation flags are `--pins`, `--eocd`, `--oracle`, `--zip-layout`, `--spec-quotes` and `--stdout-digest`" — five said, six listed; `entry_checks.py:176-177` dispatches six. (Entry:9's separate "five `entry_checks.py` flags named in items 11-15" is correct — those five exclude `--eocd`.)
Corrected: "The six derivation flags are …".

### F10 — LOW — entry:30 (item 2): "reads those four bytes back … at the printed offset"
`entry_checks.py:92-93` recomputes `pos = apk.rfind(b"PK\x05\x06")` and prints the bytes at its own offset; it never consumes the readout's 925. Output is right (925 = 925) but the provenance sentence describes a different command.
Corrected: "…the second command locates the same signature independently and prints the four bytes at the offset it finds (925, equal to the readout's)."

### F11 — LOW — entry:15 (Scope): "Nothing is … executed … at recheck time"
The recheck command runs `entry_checks.py`, which subprocess-executes `readout.py` (`entry_checks.py:99-100`, `:153-154`). `readout.py` itself executes no archive member and imports no network module, so the intent is right; the word is unscoped.
Corrected: "No archive member is extracted or executed and no producer is called at recheck time."

## 3. Focus items — the ones named in the brief

- **Item 4 (chunk `type` → enum name):** value arithmetic (`384 = 0x0180`, `256 = 0x0100`, `258 = 0x0102`, `259 = 0x0103`, `257 = 0x0101`, `1 = 0x0001`) is correct and each hex value is printed in item 11; the "walks from the root chunk's own `headerSize` by adding each chunk's `size`" sentence is OBSERVED-exact (`readout.py:144-148`: `off = u16(axml, 2)`, `off += csize`). Defect: F6 only.
- **Item 8 ("does not consult"):** HOLDS. `readout.py:211` resolves `ns` as `None if ans == NO_INDEX else strings[ans]`; the namespace chunk is emitted separately at `:182-184` and never feeds attribute resolution; no other path touches it. Resolvable by reading the cited source lines (OBSERVED-source, not command-printed — the entry's Observation bullet claims command-printed *values*, and this is not a value). Nit, not a finding: the printed `ns` value is the prefix string `"android"` (string 0), not the URI (string 1); "resolves each attribute's namespace" would be sharper as "resolves each attribute's namespace prefix string".
- **Item 9:** F5. Also verified true: `readout.py:233-248` is exactly the dex block (233 `magic = dex[:8]` … 248 `header_bytes=len(dex))`), and the recomputations are the S045-quoted ones (`zlib.adler32(dex[12:])`, `sha1(dex[32:])`).
- **Limitations:** F3 is the defect; the rest holds — "one manifest shape" (attributeCount 3, one start/end element), "UTF-8 string pool only" (flags `0x00000100`), "no styles" (styleCount 0), "no CDATA / no nested elements" (chunk table has one 0x0102/0x0103 pair and no 0x0104), "header only" (file_size 112 = header_bytes 112), "`readout.py:49-50` still comments … not assumed" (verbatim at those lines). "intentionally not a valid dex program" is supported by `generator.py:8` ("contains no classes and is not a valid dex program") but is not labeled RECORDED — cheap fix: append "(the generator's own docstring, `generator.py:8`)".
- **Quantifier words swept:** line 1 "every S038 line number and enum value … none is typed by hand" HOLDS (`derive_axml_anchors.py:108-124`: each symbol located by `find_unique`, each value parsed by `VALUE_RE` from the enum line). Line 19 "Every numbered item is produced by the command printed above its output" HOLDS (all 15 items have ≥1 command above the block; 22/22 reproduce). Line 119 "(the output below is the complete set)" HOLDS (20 lines, exact). Line 152 "each is compared with the literal in the readout source" HOLDS (14/14). Line 224 "complete stdout" HOLDS. Line 233 "every value in items 1-15 is printed by the command above it" HOLDS for values, but the *prose* source-line citations it shelters (F4's "uses") are not command-checked.

## 4. Axes impacted (wave-1 advisory; no mechanical conjunct moves)

| finding | axis / §Q-map row that would have to be repaired |
|---|---|
| F3 | Q11 (entry:259) — a stated value with no derivation; QUALITY.md:23 fail condition |
| F1 | Q03 (entry:251) / Q11 — oracle coverage narrower than "field by field" |
| F2 | Q09 (entry:257) — item 14's sentence is the only "completeness" guard; it is incomplete |
| F4 | Q04 (entry:252) / Q11 — "the widths are labeled manual" is fine; "the readout uses" is not |
| F7 | Q01 (entry:249) / S032 row scope — the cited range does not contain the transcribed fields |
| F5, F6, F8, F9, F10, F11 | prose precision; no row needs to change |

## 5. Smallest safe corrections

Zero-cost (prose only; every block stays byte-identical, item 15's digest unaffected): F4, F5, F6, F8, F9, F10, F11, plus the narrowing variants of F1 ("the four per-member / four per-attribute fields"), F2 ("every fixture, snapshot and derivation-script file"), F3 (recorded label) and F7 (range numbers).

Block-changing (requires re-running `check_embedded_outputs.py --entry` and re-pasting the affected block; `readout.py` stdout is untouched, so items 1-12 and item 15 stay valid):
1. `entry_checks.py --oracle`: add the 9 missing comparisons — `uncompressed_size` (readout prints it), attribute `data` (readout's `data_type_string` / `data_type_int_dec`), and `method` read at the transcribed local-header offset 8 (derived via `offsets(LOCAL_HEADER)`; do **not** add a `method` fact to `readout.py` — that would change all three member lines and item 15's sha256).
2. `PINS`: add `corpus/fixtures/apk-r65/entry_checks.py` (and `corpus/QUALITY.md`); item 14's block grows by 1-2 lines.
3. Optional: an `--axml-layout` check (F4) mirroring `--zip-layout`.

Order: F7/F3/F2/F1 first (they are the ones a wave-2 Q11/Q09/Q01 seat can falsify with a located defect); the rest are cheap.

## 6. Tooling

No install or upgrade was needed; nothing was installed, and no pacman transaction was attempted. Read-only git (`show`, `archive`) in the lane; all execution in `/tmp/revenger-r70-Prose` (deleted). Lane writes: this file only.
