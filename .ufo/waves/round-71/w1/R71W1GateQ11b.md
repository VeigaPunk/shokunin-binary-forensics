ACCURATE — the Observation paragraph's compared/locators-only literal naming is line- and content-exact against `readout.py` and against actual `--zip-layout`/`--axml-layout` stdout; zero locators-only literals appear in any compared output; one advisory wording nit exists outside the paragraph (item 5, see Residual).

Seat R71W1GateQ11b · revenger round 71 wave 1 (advisory pre-gate) · 2026-10-27 · read-only, no edits made to any lane file.

## Question

Does the v6 entry's Observation paragraph name the compared and locators-only literals accurately under Q11/Q16, checked against `corpus/fixtures/apk-r65/readout.py:22,76,166,211,233-248` and the actual `--zip-layout`/`--axml-layout` stdout?

## Evidence A — every locators-only citation is line- and content-exact

`grep -n` over `corpus/fixtures/apk-r65/readout.py` (256 lines; the `.ufo/waves/round-71/sources-s052/validate/` copy is byte-identical, `diff -q` exit 0):

- `readout.py:22` = `NO_INDEX = 0xFFFFFFFF` — matches Observation "`NO_INDEX = 0xFFFFFFFF`".
- `readout.py:76` = `    sig_eocd = b"PK\x05\x06"` — matches "the end-of-central-directory signature literal".
- `readout.py:166` = `         utf8=bool(flags & 0x100), sorted_flag=bool(flags & 0x1),` — both masks are on this single line, so "the UTF-8/sorted flag masks `flags & 0x100` and `flags & 0x1`" at `:166` is exact.
- `readout.py:211` = `            "ns_index": ans, "ns": None if ans == NO_INDEX else strings[ans],` — contains `strings[ans]`, exact.
- `readout.py:233-248` = `    magic = dex[:8]` (:233) through `         header_bytes=len(dex))` (:248) — the complete dex declared-header read block (reads at :233-236 plus `u32(dex, 32/36/40)` inside the :237-248 `emit`); the next emit (`jar_manifest`) starts at :250, outside the range. "The dex header reads" is exact.

Frozen contract (`reports/round-71/claims.md` line 11) requires the Observation to name exactly `:22` (`NO_INDEX`), `:76` (EOCD signature), `:166` (UTF-8/sorted masks), `:211` (`strings[ans]`), `:233-248` (dex header reads) as locators-only. The entry (`corpus/knowledge/round-71-apk-axml-byte-evidence.md:283`) names exactly these five, in order, with matching descriptions; none missing, none extra.

## Evidence B — actual stdout matches the "compared" half of the bound

Ran from the lane root (receipts embedded in §Receipts below):

- `python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout` → 20 lines. Lines 16–18 are the three APPNOTE layout MATCH lines (4.3.7 heading 387, 4.3.12 heading 511, 4.3.16 heading 632); lines 19–20 are `central.fixed_part` / `local.fixed_part`. Item 12's repaired sentence ("output lines 16-18 of 20 … last two lines compare the central and local fixed-part widths") is exact. The only readout.py source literals it prints are ZIP offset/fixed-part literals (`u16(apk, eocd + 10)`, `u32(apk, eocd + 12)`, `u32(apk, eocd + 16)`, `u16(apk, cursor + 28/30/32)`, `u32(apk, cursor + 42)`, `u32(apk, lh_off + 14/18/22/26/28)`, `cursor + 46`, `lh_off + 30`) — matching the Observation's "(ZIP offset/fixed-part literals)".
- `python3 -B corpus/fixtures/apk-r65/entry_checks.py --axml-layout` → 24 lines: 5 transcription-vs-readout-printed width MATCH lines, 1 node fixed-part line, and 18 MATCH lines whose readout.py source literals are all AXML layout literals (`u32(axml, so + 8/12/16/20/24)`, `u32(axml, base + 16/20/24/26/28/30/32)`, `u32(axml, aoff)`, `aoff + 4/8/12/15/16`) — matching "(AXML layout literals)".
- Grep of the whole entry for `readout.py literal`: hits only inside item 12's block (entry lines 160–176) and item 17's block (entry lines 261–278). No other item's command prints any readout source literal, so the Observation's "compared only where items 12 and 17 print them" is complete, not just sufficient.
- Locator-literal scan of both receipts for `sig_eocd|NO_INDEX|strings[ans]|flags &`: **zero matches**. None of the five locators-only literals is printed by any compared output. `--eocd` (item 2) prints the archive's bytes (`eocd signature bytes at offset 925: 504b0506 (4 bytes)`), not the readout.py:76 source literal, so `:76` staying locators-only is also correct.

## Evidence C — embedded blocks equal actual stdout (Q16's stdout check)

Mechanical extraction of the fenced blocks following each `$ python3 -B corpus/fixtures/apk-r65/entry_checks.py …` line in the entry, diffed against the fresh receipts: `--zip-layout` 20/20 lines identical (embedded==actual=True); `--axml-layout` 24/24 lines identical (embedded==actual=True). Q16 (`corpus/QUALITY.md:28`: "a sentence that says what a command prints is checked against that command's stdout") is satisfied for the two repaired descriptions.

## Evidence D — Q11/Q16 mapping

- Q11 (`QUALITY.md:23`) requires each count/identifier/offset/digest to carry its deriving command and output, and prose-only values to be labeled recorded. The Observation labels all `readout.py:N` citations "source locators checked by the file" (recorded-class) and does not present any of the five as re-derived. The entry's Q11 row (`:309`: "`readout.py:N` citations are labeled source locators") is true of the paragraph.
- Q16 (`QUALITY.md:28`) requires set-credits to stop at printed members. The paragraph's credit ("compared only where items 12 and 17 print them") stops exactly at the printed sets (Evidence B), and the five-item locators-only list is exactly the complement among the entry's load-bearing citations. No unguarded literal is credited by the paragraph.

## Residual (advisory, outside the checked paragraph; no edit made)

- Item 5 (`entry:130`) says item 17's command "checks that the literal read offsets in the readout source match sums of these widths". Actual `--axml-layout` prints no MATCH for `u16(axml, base + 34)` (`readout.py:197`, `style_index`, attrExt offset 18, the eighth field of `[4,4,2,2,2,2,2,2]`) nor for `u32(axml, base + 8)` (`readout.py:189`, chunk `lineNumber`). A strict Q16 reader could call item 5's credit one field past the printed set; the Observation paragraph itself does not repeat that breadth, and the frozen repair list (items 11/12, Observation, Q13) did not name item 5. Wave-2 Q16 voters may weigh this wording; it does not falsify the checked Observation naming.

## Receipts (copied from scratch `/fast/scratch/hyaku/revenger-r71/R71W1GateQ11b/` before its deletion)

`--zip-layout` (20 lines, verbatim):
```
local fixed part: 30 bytes (sum of the transcribed field widths)
central fixed part: 46 bytes (sum of the transcribed field widths)
eocd fixed part: 22 bytes (sum of the transcribed field widths)
MATCH eocd.total_entries: spec offset 10, readout.py literal `u16(apk, eocd + 10)` present=True
MATCH eocd.cd_size: spec offset 12, readout.py literal `u32(apk, eocd + 12)` present=True
MATCH eocd.cd_offset: spec offset 16, readout.py literal `u32(apk, eocd + 16)` present=True
MATCH central.name_length: spec offset 28, readout.py literal `u16(apk, cursor + 28)` present=True
MATCH central.extra_length: spec offset 30, readout.py literal `u16(apk, cursor + 30)` present=True
MATCH central.comment_length: spec offset 32, readout.py literal `u16(apk, cursor + 32)` present=True
MATCH central.local_header_offset: spec offset 42, readout.py literal `u32(apk, cursor + 42)` present=True
MATCH local.crc32: spec offset 14, readout.py literal `u32(apk, lh_off + 14)` present=True
MATCH local.compressed_size: spec offset 18, readout.py literal `u32(apk, lh_off + 18)` present=True
MATCH local.uncompressed_size: spec offset 22, readout.py literal `u32(apk, lh_off + 22)` present=True
MATCH local.name_length: spec offset 26, readout.py literal `u16(apk, lh_off + 26)` present=True
MATCH local.extra_length: spec offset 28, readout.py literal `u16(apk, lh_off + 28)` present=True
MATCH APPNOTE 4.3.7: heading line 387, transcribed field lines 389-399
MATCH APPNOTE 4.3.12: heading line 511, transcribed field lines 522-538
MATCH APPNOTE 4.3.16: heading line 632, transcribed field lines 634-646
MATCH central.fixed_part: spec width 46, readout.py literal `cursor + 46` present=True
MATCH local.fixed_part: spec width 30, readout.py literal `lh_off + 30` present=True
```

`--axml-layout` (24 lines, verbatim):
```
MATCH ResChunk_header: transcription [2, 2, 4] readout-printed [2, 2, 4]
MATCH ResStringPool_header: transcription [2, 2, 4, 4, 4, 4, 4, 4] readout-printed [2, 2, 4, 4, 4, 4, 4, 4]
MATCH ResXMLTree_node: transcription [2, 2, 4, 4, 4] readout-printed [2, 2, 4, 4, 4]
MATCH ResXMLTree_attrExt: transcription [4, 4, 2, 2, 2, 2, 2, 2] readout-printed [4, 4, 2, 2, 2, 2, 2, 2]
MATCH ResXMLTree_attribute: transcription [4, 4, 4, 2, 1, 1, 4] readout-printed [4, 4, 4, 2, 1, 1, 4]
ResXMLTree_node fixed part: 16 bytes; attrExt begins at chunk offset + 16
MATCH ResStringPool_header.stringCount: spec offset 8 (+0), readout.py literal `u32(axml, so + 8)` present=True
MATCH ResStringPool_header.styleCount: spec offset 12 (+0), readout.py literal `u32(axml, so + 12)` present=True
MATCH ResStringPool_header.flags: spec offset 16 (+0), readout.py literal `u32(axml, so + 16)` present=True
MATCH ResStringPool_header.stringsStart: spec offset 20 (+0), readout.py literal `u32(axml, so + 20)` present=True
MATCH ResStringPool_header.stylesStart: spec offset 24 (+0), readout.py literal `u32(axml, so + 24)` present=True
MATCH ResXMLTree_attrExt.ns: spec offset 0 (+16), readout.py literal `u32(axml, base + 16)` present=True
MATCH ResXMLTree_attrExt.name: spec offset 4 (+16), readout.py literal `u32(axml, base + 20)` present=True
MATCH ResXMLTree_attrExt.attributeStart: spec offset 8 (+16), readout.py literal `u16(axml, base + 24)` present=True
MATCH ResXMLTree_attrExt.attributeSize: spec offset 10 (+16), readout.py literal `u16(axml, base + 26)` present=True
MATCH ResXMLTree_attrExt.attributeCount: spec offset 12 (+16), readout.py literal `u16(axml, base + 28)` present=True
MATCH ResXMLTree_attrExt.idIndex: spec offset 14 (+16), readout.py literal `u16(axml, base + 30)` present=True
MATCH ResXMLTree_attrExt.classIndex: spec offset 16 (+16), readout.py literal `u16(axml, base + 32)` present=True
MATCH ResXMLTree_attribute.ns: spec offset 0, readout.py literal `u32(axml, aoff)` present=True
MATCH ResXMLTree_attribute.name: spec offset 4, readout.py literal `u32(axml, aoff + 4)` present=True
MATCH ResXMLTree_attribute.rawValue: spec offset 8, readout.py literal `u32(axml, aoff + 8)` present=True
MATCH ResXMLTree_attribute.valueSize: spec offset 12, readout.py literal `u16(axml, aoff + 12)` present=True
MATCH ResXMLTree_attribute.valueDataType: spec offset 15, readout.py literal `axml[aoff + 15]` present=True
MATCH ResXMLTree_attribute.valueData: spec offset 16, readout.py literal `u32(axml, aoff + 16)` present=True
```

`--eocd` (1 line, verbatim): `eocd signature bytes at offset 925: 504b0506 (4 bytes)`

Report trailer: `.ufo/waves/round-71/w1/R71W1GateQ11b.md`
