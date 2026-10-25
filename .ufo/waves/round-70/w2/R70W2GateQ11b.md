FAIL (Q11b) — every value in items 10-17 re-derives byte-exactly and every `readout.py:N`/snapshot-line citation resolves, but the region's own derivation summary (`:282`) asserts that the cited readout literals "are compared in items 12 and 17"; the UTF-8/SORTED masks at `readout.py:166` and the dex header offsets at `readout.py:234-247` are compared nowhere, so a recorded value is presented as re-derived (Q11 reject clause 2). Secondary (reported, Q13-flavoured): item 17's lead (`:250`) overstates its compared set.

# Seat R70W2GateQ11b — Q11 over items 10-17, Observation/inference/unknown, Limitations, cross-lane note, §Q-map, Reproduce

Bytes judged: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin show 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd:corpus/knowledge/round-70-apk-axml-byte-evidence.md`
sha256 `819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31`, 322 lines (the landed candidate,
`admission-status: candidate` at `:11`). Line numbers below are that file's lines.

All commands were run from a `git archive 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd` extraction in
`/tmp/revenger-r70-R70W2GateQ11b/tree` (deleted before return); every value below is from that extraction, and I
re-derived each one myself rather than accepting the entry's §Q-map row.

## 1. The nine command blocks of my region reproduce exactly (not the gate's verdict — my own replayer)

My replayer parsed each `$ ` line and its embedded lines, ran the command, and compared stdout line-for-line:

```
EXACT L113 rc=0 emb=1 act=1  readout.py --fact jar_manifest
EXACT L122 rc=0 emb=20 act=20  corpus/derive_axml_anchors.py
EXACT L143 rc=0 emb=6 act=6  entry_checks.py --spec-quotes
EXACT L155 rc=0 emb=20 act=20  entry_checks.py --zip-layout
EXACT L181 rc=0 emb=34 act=34  entry_checks.py --oracle
EXACT L221 rc=0 emb=10 act=10  entry_checks.py --pins
EXACT L237 rc=0 emb=1 act=1  entry_checks.py --stdout-digest
EXACT L244 rc=0 emb=3 act=3  entry_checks.py --container
EXACT L253 rc=0 emb=24 act=24  entry_checks.py --axml-layout
blocks=9 exact=9 diff=0
```

Independent of the blocks: `python3 -B corpus/fixtures/apk-r65/readout.py` → exit 0, `wc -l` = 15,
`sha256sum` = `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` = `:236`, matching Reproduce
(`:322`) "Exit 0 and 15 stdout lines". `entry_checks.py` dispatches exactly the eight flags Reproduce names
(`main(): cmds = {"--pins","--eocd","--oracle","--zip-layout","--stdout-digest","--spec-quotes","--container",
"--axml-layout"}`), so "The eight derivation flags" is correct.

## 2. Number/hex/identifier table for the region — every one has the output line that prints it

| entry lines | value(s) | printing output line |
|---|---|---|
| 110-115 (item 10) | `bytes 69`, `section_count 1`, first line | `:114` |
| 119-150 (item 11) | S038 lines 218/287/461/612/621/677/707; enum 237, 239=`0x0001`, 241=`0x0003`, 244=`0x0100`, 245=`0x0100`, 246=`0x0101`, 247=`0x0102`, 248=`0x0103`, 253=`0x0180`, 263; 686, 687 | `:123-142` |
| 119-150 (item 11) | spec-quote first lines 7, 5949, 5956, 5981, 5035, 686; "four S048 phrases" = 4 of 6 lines | `:144-149` |
| 152-176 (item 12) | 30, 46, 22; offsets 10, 12, 16, 28, 30, 32, 42, 14, 18, 22, 26, 28; widths 46, 30 | `:156-175` |
| 152-176 (item 12) | APPNOTE heading 387, fields 389-399; 511, 522-538; 632, 634-646 | `:171-173` |
| 178-216 (item 13) | 34 `MATCH` lines: 947, 416, 112, 69; offsets 0, 465, 618; indices 3, 4294967295, 4, 5, 0, 7, 16, 1, 6, 8; ids `0x0101021b`, `0x0101021c` | `:182-215` (34 embedded = 34 actual) |
| 218-232 (item 14) | ten digests + sizes 947, 2466, 9599, 11236, 15062, 4979, 86255, 174585, 281157, 1992 | `:222-231` |
| 234-239 (item 15) | 15 lines, sha256 `507d79f8…d247` | `:238` |
| 241-248 (item 16) | `flags=0x0000`, `method=0`, bit 3 clear ×3, oracle method 0 | `:245-247` |
| 250-278 (item 17) | widths [2,2,4]…; 16 bytes; offsets 8, 12, 16, 20, 24; `+16`; 0, 4, 8, 12, 15, 16 | `:254-277` |
| 282-284 (Obs/inf/unknown) | "items 3, 5, 12 and 17"; literal `16` in `readout.py:203` | `:270` (`u16(axml, base + 16)` present=True), `:58` (`headerSize: 16`) |
| 286-288 (Limitations) | "three attributes", "string 1", items 6/8, `generator.py:8`, `readout.py:49-50` | `:90` (attributeCount 3), `:76` (strings[1] = URI), `:8`/`:14` (§1), `readout.py:8` = `contains no classes and is not a valid dex program` |
| 290-292 (cross-lane) | fleet `.ufo/l0-questions.md:42`; `kaidoku-shokunin/corpus/README.md:27`, `:29` | `sed -n '42p' .ufo/l0-questions.md` → `tsukuroi | round-1 | …arbitrate the kaidoku/revenger shipped-artifact overlap before an ADJ-06 analysis is routed…`; kaidoku `:27` = "Archives & packages … APK content graph (120 deduplicated content nodes…)"; `:29` = "Android decode axis first-held on Godot APKs" |
| 294-312 (§Q-map) | "ten `corpus/` files" (Q09), "items 1-17" (Q11), "Exit 0" (Q05) | `:222-231` (10 lines), §1 above |
| 314-322 (Reproduce) | 15 stdout lines, Exit 0, eight flags, `--fact eocd` | §1 above; `:38` |

So the *table* test — every count/offset/identifier/digest in the region carries a command and that command's
output — passes.

## 3. Citation resolution (`cat -n` / `sed -n`, not the entry's §Q-map)

`readout.py:N` citations, all TRUE:

```
49|    # Every fixed offset the readout uses is computed here from the field
50|    # widths in ResourceTypes.h's own struct definitions, not assumed.
51|    w8, w16, w32 = 1, 2, 4            58|        "Res_value": [w16, w8, w8, w32],
76|    sig_eocd = b"PK\x05\x06"
105|        payload_off = lh_off + 30 + lh_name_len + lh_extra_len
155|    offsets = [u32(axml, so + sp["headerSize"] + 4 * i) for i in range(string_count)]
166|         utf8=bool(flags & 0x100), sorted_flag=bool(flags & 0x1),
168|         offsets=offsets, strings=strings)
203|        aoff = base + 16 + attribute_start + i * attribute_size
211|            "ns_index": ans, "ns": None if ans == NO_INDEX else strings[ans],
233|    magic = dex[:8]      234|    checksum = u32(dex, 8)      235|    signature = dex[12:32]
246|         file_size=u32(dex, 32), header_size=u32(dex, 36),
247|         endian_tag=f"0x{u32(dex, 40):08x}",      248|         header_bytes=len(dex))
```

Snapshot-line citations, all TRUE (my own `sed -n`, not `--spec-quotes`):
`ResourceTypes.h` 218 `struct ResChunk_header`, 237 `enum {`, 239 `RES_STRING_POOL_TYPE = 0x0001`, 241
`RES_XML_TYPE = 0x0003`, 244/245 `0x0100`, 246 `0x0101`, 247 `0x0102`, 248 `0x0103`, 253 `0x0180`, 263 `};`, 287
`struct Res_value`, 461 `struct ResStringPool_header`, 612/621/677/707 the four XML structs, 686
`// Byte offset from the start of this structure where the attributes start.`, 687 `uint16_t attributeStart;`.
`APPNOTE.TXT` 387 `4.3.7  Local file header:`, 389-399 the eleven 4.3.7 fields (sum 30), 511 `4.3.12`, 522-538
the seventeen 4.3.12 fields (sum 46), 632 `4.3.16`, 634-646 the 4.3.16 field lines (sum 22). `dex-format.html`
5035 `uint ENDIAN_CONSTANT = 0x12345678;`, 5949 adler32 phrase, 5956 SHA-1 phrase, 5981 `must be 0x70 (112) bytes`.
`rea-android-applications.md:7` = `Start with \`inspect_android_package\` on the caller's APK path…`.

## 4. D1 — FAIL: `:282` presents uncompared literals as compared

Entry `:282` (the Observation bullet, the entry's own Q11 summary):

> "…the `readout.py:N` line citations are source locators checked by reading the file, and **the literals they
> concern are compared in items 12 and 17**."

Counterexample A — the string-pool masks at the cited `readout.py:166` (`flags & 0x100`, `flags & 0x1`). The
spec lines that would derive them exist and are never printed by any embedded command:

```
$ grep -n 'UTF8_FLAG\|SORTED_FLAG' corpus/snapshots/ResourceTypes.h
477:        SORTED_FLAG = 1<<0,
480:        UTF8_FLAG = 1<<8
$ python3 -B corpus/derive_axml_anchors.py | grep -c 'FLAG'
0
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout | grep -c '0x100'
0
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --axml-layout | grep -c '0x100'
0
```

Counterexample B — the dex header offsets the cited `readout.py:233-248` concerns (`dex, 8`, `dex[12:32]`,
`dex, 32`, `dex, 36`, `dex, 40`): no comparison in items 12 or 17 either.

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --axml-layout | grep -c 'dex, 8'   → 0
$ … --zip-layout | grep -c 'dex, 32'  → 0   (same for dex, 36 and dex, 40)
```

(Softer third case: the constant `b"PK\x05\x06"` at `readout.py:76` is compared by item 2's `--eocd` bytes, not
by items 12/17.)

Why this is Q11 and not merely a wording nit: `0x100` is stated as a value in item 6 (`:72`, "the UTF-8 flag
position tested is `flags & 0x100`") and is correct only because S038 `:480` says so; the entry carries no
command that derives it, and `:282` states that its literal *is* compared. That is Q11's reject clause "a
recorded value is presented as re-derived" (and clause 1: correct value, no derivation carried).

Smallest safe correction (one clause, no script change):

> "…the `readout.py:N` line citations are source locators checked by reading the file; the **offset** literals
> they concern are compared in items 12 and 17, while the UTF-8/SORTED masks `0x100`/`0x1` (`readout.py:166`) and
> the dex header field offsets (`readout.py:234-247`) are **recorded** from the readout source and not compared."

## 5. D2 — reported (Q13-flavoured, outside my decision): `:250` overstates the compared set

Entry `:250`: "17. The AXML field offsets the readout source uses, compared with sums of a second manual
transcription of S038's struct widths…". The `--axml-layout` block (`:254-277`) compares 18 literals; the readout
uses these AXML literals that appear in no comparison line:

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --axml-layout | grep -c 'base + 34'   → 0   (readout.py:197 styleIndex)
$ … | grep -c 'base + 8'   → 0   (readout.py:189 node lineNumber)
$ … | grep -c 'ch + 16'    → 0   (readout.py:180-181 namespace prefix/uri; also ch + 8, ch + 20)
```

(`rm["offset"] + 8`, `readout.py:172`, and the end-element `+8/+16/+20`, `readout.py:227-229`, likewise.) The
sentence credits item 17 with a set it does not cover; correction: "The AXML field offsets the readout source
uses **in the attrExt, attribute and string-pool-header records**…". Item 5 (`:63`) repeats the universal ("item
17's command checks that the literal read offsets in the readout source match sums of these widths") — that line
is outside my region, recorded here for the Q13 seat.

## 6. Alternative reading and what would flip me

If the L1 narrows `:282`'s quantifier to the ZIP/AXML *offset* literals only, then every value in my region
passes and Q11b is PASS on these bytes, with D2 routed to Q13. I did not adopt that reading because the sentence
as landed is unqualified, and the two counterexamples are literals the cited lines concern. Everything else in my
region — all 9 blocks, all 40+ numbers, all citations, the cross-lane pointers, the Limitations premises (no
ZIP flag/method read in `readout.py`; dex header-only at `generator.py:8`; `ns_index` 0 = prefix per item 6/8),
and the Reproduce numbers — I re-derived and found correct.

## 7. Tooling

No installs or upgrades (pacman paused host-wide; nothing needed): `python3` stdlib only, plus read-only
`git show`/`git archive`/`git log`. Scratch `/tmp/revenger-r70-R70W2GateQ11b` deleted before return. I did not
read `.ufo/waves/round-70/w1/` until after forming D1/D2 above; the cross-check showed the wave-1 seat on the
*previous* candidate (`aa1842f`, 273 lines) judged Reproduce "five derivation flags" and two APPNOTE ranges —
both repaired in the landed v5.1 — and did not audit the sentence I FAIL here (it did not exist at `aa1842f`;
`git show aa1842f:… | grep -n 'source locators'` → no match).
