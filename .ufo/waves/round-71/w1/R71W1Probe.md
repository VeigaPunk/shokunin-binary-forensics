VERDICT: PASS with one pre-gate repair — both derivations reproduce byte-exactly at lane HEAD `18200a4`, v6 item 11/12 prose matches the real stdout (lines 16–18 of 20 = three APPNOTE layouts, 19–20 = fixed-part widths), and S052's quote is byte-exact and 12 words; but S052's anchor says the output is already "recorded in `corpus/lessons/round-71.md` `## Gate`", and that file does not exist in the lane.

## Axes

Operability and freshness: can a cold reader re-run the two commands and get the printed bytes; are the frozen Q04 repairs true of the actual stdout; does the round's one new source row carry a dated, located, ≤25-word quote at the recorded Gate path.

## Commands run (cwd `/home/vgpnk/Projects/shokunin/revenger-shokunin`, lane HEAD `18200a4b18e8dfce291a74028a9012ce4401ca10`)

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes
EXIT=0   (6 stdout lines, empty stderr)
     1	MATCH rea-android-applications.md: first line 7, folded phrase present=True: Start with `inspect_android_package` on the caller's APK path for package identity, manifest declarations, coverage, and inline Evidence.
     2	MATCH dex-format.html: first line 5949, folded phrase present=True: adler32 checksum of the rest of the file (everything but magic and this field)
     3	MATCH dex-format.html: first line 5956, folded phrase present=True: SHA-1 signature (hash) of the rest of the file (everything but magic, checksum, and this field)
     4	MATCH dex-format.html: first line 5981, folded phrase present=True: must be 0x70 (112) bytes (v40 or earlier)
     5	MATCH dex-format.html: first line 5035, folded phrase present=True: uint ENDIAN_CONSTANT = 0x12345678;
     6	MATCH ResourceTypes.h: first line 686, folded phrase present=True: Byte offset from the start of this structure where the attributes start
```

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout
EXIT=0   (20 stdout lines, empty stderr)
     1	local fixed part: 30 bytes (sum of the transcribed field widths)
     2	central fixed part: 46 bytes (sum of the transcribed field widths)
     3	eocd fixed part: 22 bytes (sum of the transcribed field widths)
     4	MATCH eocd.total_entries: spec offset 10, readout.py literal `u16(apk, eocd + 10)` present=True
     5	MATCH eocd.cd_size: spec offset 12, readout.py literal `u32(apk, eocd + 12)` present=True
     6	MATCH eocd.cd_offset: spec offset 16, readout.py literal `u32(apk, eocd + 16)` present=True
     7	MATCH central.name_length: spec offset 28, readout.py literal `u16(apk, cursor + 28)` present=True
     8	MATCH central.extra_length: spec offset 30, readout.py literal `u16(apk, cursor + 30)` present=True
     9	MATCH central.comment_length: spec offset 32, readout.py literal `u16(apk, cursor + 32)` present=True
    10	MATCH central.local_header_offset: spec offset 42, readout.py literal `u32(apk, cursor + 42)` present=True
    11	MATCH local.crc32: spec offset 14, readout.py literal `u32(apk, lh_off + 14)` present=True
    12	MATCH local.compressed_size: spec offset 18, readout.py literal `u32(apk, lh_off + 18)` present=True
    13	MATCH local.uncompressed_size: spec offset 22, readout.py literal `u32(apk, lh_off + 22)` present=True
    14	MATCH local.name_length: spec offset 26, readout.py literal `u16(apk, lh_off + 26)` present=True
    15	MATCH local.extra_length: spec offset 28, readout.py literal `u16(apk, lh_off + 28)` present=True
    16	MATCH APPNOTE 4.3.7: heading line 387, transcribed field lines 389-399
    17	MATCH APPNOTE 4.3.12: heading line 511, transcribed field lines 522-538
    18	MATCH APPNOTE 4.3.16: heading line 632, transcribed field lines 634-646
    19	MATCH central.fixed_part: spec width 46, readout.py literal `cursor + 46` present=True
    20	MATCH local.fixed_part: spec width 30, readout.py literal `lh_off + 30` present=True
```

Base-to-HEAD drift check for the fixture surface (so "stdout at lane base `b7abcd8…`" is also today's stdout):

```
$ git diff b7abcd8..HEAD -- corpus/fixtures/apk-r65/entry_checks.py corpus/fixtures/apk-r65/readout.py corpus/snapshots/
(no output; only .ufo/*, PROVINCE.md, SKILL.md, corpus/README.md, corpus/SOURCES.md, corpus/check_embedded_outputs.py, the v6 entry and reports/round-71/* changed)
```

## Item 11 — checked against actual stdout (freshness)

- `corpus/knowledge/round-71-apk-axml-byte-evidence.md:120` now says the second command "locates each quoted spec phrase … tags stripped and whitespace folded, and prints, for each phrase, the snapshot file, the line number its first words start on, and the searched phrase itself". Actual stdout lines 1–6 print exactly `MATCH <file>: first line <N>, folded phrase present=True: <phrase>` — file, line number, searched phrase; no raw snapshot line is claimed. The round-70 Q04 defect (`:119` "prints the raw line …") is repaired.
- Phrase inventory matches: 1 REA/S049 sentence + 4 dex-format/S048 phrases + 1 ResourceTypes/S038 `attributeStart` comment = 6 printed lines (`:120` says the same enumeration).
- Embedded block `:145-150` is byte-identical to live stdout (`diff` exit 0).
- Item 11's first command block `:124-143` (20 lines) is byte-identical to a live `python3 -B corpus/derive_axml_anchors.py` run (exit 0, `diff` exit 0), so "the output below is the complete set" holds for 20 lines.
- First-line numbers re-verified directly in the committed snapshots: `corpus/snapshots/rea-android-applications.md:7` starts `Start with \`inspect_android_package\`…`; `dex-format.html:5035` = `uint ENDIAN_CONSTANT = 0x12345678;`, `:5949` = `<td>adler32 checksum…`, `:5956` = `<td>SHA-1 signature…`, `:5981` = `<p>must be 0x70 (112) bytes`; `ResourceTypes.h:686` = `// Byte offset from the start of this structure where the attributes start.`
- Precision note (advisory, not a FAIL): location is computed from the phrase's **first three** words (`corpus/fixtures/apk-r65/entry_checks.py:289`, `first = " ".join(phrase.split()[:3])`). Saying "first three words" instead of "first words" would make the sentence exactly reproducible from the code; today's wording is still true.

## Item 12 — checked against actual stdout line ranges (the frozen Q04 repair)

- `:153` says "output lines 16-18 of 20 print where each record layout sits in the snapshot (heading line and the first and last transcribed field lines), while the last two lines compare the central and local fixed-part widths."
- Actual: 20 lines total; lines 16–18 are `MATCH APPNOTE 4.3.7: heading line 387, transcribed field lines 389-399`, `4.3.12: 511 / 522-538`, `4.3.16: 632 / 634-646`; lines 19–20 are `MATCH central.fixed_part: spec width 46 …` and `MATCH local.fixed_part: spec width 30 …`. The frozen repair is satisfied as written.
- Embedded block `:157-176` (20 lines) is byte-identical to live stdout (`diff` exit 0). Prose "summed here from the manually transcribed APPNOTE field widths" matches the code path (`entry_checks.py:181-196`, printed at `:185` and `:194-196`).

## S052 — quote, date, and the Gate anchor

- Row: `corpus/SOURCES.md:66`; entry row: `corpus/knowledge/round-71-apk-axml-byte-evidence.md:8`.
- Located quote `MATCH dex-format.html: first line 5035, folded phrase present=True: uint ENDIAN_CONSTANT = 0x12345678;` — byte-exact in the live stdout (grep -F hit count 1 in both SOURCES.md and the captured stdout), **12 words** (≤25), and it is stdout line 5.
- Access date present twice: "captured 2026-10-27" (census anchor) and "opened 2026-10-27" (entry row); re-opened by this seat 2026-10-27 at the committed snapshot bytes.
- Scope wording is accurate: it claims "output shape … file, first-line number, phrase-presence flag and phrase; not the raw source line or proof of all source text" — that is precisely what `entry_checks.py:284-292` prints.

**Repair required before the final candidate (operability).** `corpus/knowledge/round-71-apk-axml-byte-evidence.md:8` states the output is "recorded in `corpus/lessons/round-71.md` `## Gate`", but that file does not exist:

```
$ find . -name "round-71*" -not -path "./.git/*"
./corpus/knowledge/round-71-apk-axml-byte-evidence.md
./reports/round-71
./.ufo/waves/round-71
./.ufo/waves/round-71/sources-s052/validate/corpus/knowledge/round-71-apk-axml-byte-evidence.md
$ git ls-files corpus/lessons/ | tail -3
corpus/lessons/round-70-verifier-spotcheck.md
corpus/lessons/round-70.md
(no round-71.md)
```

Two acceptable fixes, either one before the final candidate: (a) write `corpus/lessons/round-71.md` with a `## Gate` section carrying the S052 access date (2026-10-27) and the 12-word located quote already used in the census row, or (b) reword the anchor to a path that exists at candidate time. Round-70's entry rows anchor to artifacts that existed at their candidate tip, so (a) keeps the convention. Note this is not one of the four frozen prose repairs, which are all satisfied above; it is an additional wave-1 repair recommendation.

## Risks

- The Gate draft is a wave-2/final artifact; if it is written after the final candidate, S052's anchor is true only post-adjudication. Writing the lesson file in the final candidate (or softening the anchor) removes the ordering hazard for a cold reviewer.
- The `--spec-quotes` "first line" value for dex-format.html 5949/5956/5981 lands on HTML table-cell lines (phrase starts after `<td>`); item 11's "line number its first words start on" is accurate for that, but a reader expecting the phrase to begin the line could misread it. No repair needed for Q04; the "folded" wording already signals tag stripping.
- Only `--spec-quotes` and `--zip-layout` plus their item-11 derive command were executed here; the full embedded-output gate was not run by this seat.

## Scope

Read-only: two derivation runs, one derive run, `git diff`/`git ls-files`/`grep`/`find`/`diff` inspections of the v6 entry, `corpus/SOURCES.md`, the federation snapshot bytes and the fixture scripts. No lane-source edit, no git/jj mutation, no campaign tool, no `/tmp` use, no install. Scratch `/fast/scratch/hyaku/revenger-r71/R71W1Probe/` held the captured stdout and diff inputs and was deleted after the receipts above were transcribed.

Report: .ufo/waves/round-71/w1/R71W1Probe.md
