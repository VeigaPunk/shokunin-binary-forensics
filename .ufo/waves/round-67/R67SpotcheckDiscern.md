S045-ADMIT-AGREE + R65-REJECT-AGREE — every S045 anchor/quote is located and verbatim in the committed snapshot with honest tier/scope; the r65 entry:41 drift re-reproduces byte-exactly and the landed C7 gate goes red on it.

Seat: R67SpotcheckDiscern — outside-discernment spot-check of this round's recorded gate decisions (LEARNING.md shape: ≥1 admit + ≥1 reject re-verified by a non-author seat). Read-only; nothing installed or modified; no subagents.

## (a) ADMIT sample — registry row S045 (`corpus/SOURCES.md:59`)

Re-opened the committed snapshot `.ufo/waves/round-67/source-snapshots/dex-format.html` (the row's own bound bytes) and checked every anchored claim:

- Snapshot identity: `sha256sum` → `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4`; `wc -c` → `281157` bytes. Both match the row and `reports/round-67/claims.md` C1 item 4 verbatim.
- "File layout" section located: snapshot `:4825` `<h2 id="file-layout" data-text="File layout">`; its container table names `header_item` at `:4838`. The `header_item` field table the quotes come from is the dedicated section `<h3 id="header-item">` at `:5926` — reachable navigation, all quoted material verbatim there.
- checksum row quote `"adler32 checksum of the rest of the file (everything but magic and this field)"` — verbatim rendered text at snapshot `:5948-5951` (`magic` inside `<code>`; the row's rendering is faithful).
- header_size quote `"must be 0x70 (112) bytes (v40 or earlier)"` — verbatim at `:5981-5982`, and the qualifier is honestly carried: the doc also states `0x78 (120) bytes` for the v41+ layout (`:5984`); the row quotes only the v40-or-earlier branch, which is the branch the v2 entry's `dex\n035` member needs. Not overclaimed.
- `` `ENDIAN_CONSTANT = 0x12345678` `` — verbatim in the spec's code block at `:5035` (`uint ENDIAN_CONSTANT = 0x12345678;`).
- Remaining scope-listed fields present: `signature` = `ubyte[20]` "SHA-1 signature (hash) of the rest of the file…" at `:5954-5958`; `magic` covered by `DEX_FILE_MAGIC` "Embedded in header_item" (`:4966-4967`); `file_size` row at `:5962`; `endian_tag` at `:5990`.
- Tier/scope honesty: AOSP canonical DEX format spec → tier A docs is right; scope explicitly bounds itself to "the declared `header_item` field semantics … of one authored `classes.dex` member; not dex program validity and not general dex parsing" — matches what the source actually teaches and what the v2 entry consumes (entry line 106 cites only the checksum/signature/field-semantics rows).
- Registry bookkeeping: status `mined`, opened `2026-10-24`, used-by `corpus/knowledge/round-67-apk-axml-byte-evidence.md` (real: the v2 entry's `source:` line 3 and item 9 both cite S045); search-log line `SOURCES.md:89` records the fetch (281157 bytes, `curl -sL --max-redirs 15` after the fetch tool's redirect limit — consistent with the committed snapshot).
- Cosmetic nit (not a defect): the anchor phrase "File layout → `header_item` field table" is navigational — the field table is the `header_item` section at `:5926`, not literally inside the File layout table; `header_item` is however named inside that table at `:4838`. All quotes land verbatim either way.

Verdict: ADMIT was calibrated — anchors located, quotes verbatim, digest/size match, scope fenced. AGREE.

## (b) REJECT sample — retained round-65 candidate (`corpus/knowledge/round-65-apk-axml-byte-evidence.md`)

- `admission-status: rejected` intact at line 7 (adjudicated round-66: Q02/Q06/Q11 FAIL + R65SpotcheckDiscern REJECT); the file retains every byte including the drifted entry:41 — matching the void condition that prior rejected candidates stay byte-frozen as the C7 red-before surface.
- Re-ran the named command from the lane root:
  `python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[META-INF/MANIFEST.MF]'`
  → actual stdout carries `"payload_first16_hex": "4d616e69666573742d56657273696f6e"` — 16 bytes, ASCII `Manifest-Version` — sha256 `2e5da249…`, all other fields identical to the embedded line.
  → entry:41 still embeds `"payload_first16_hex": "4d616e696673742d56657273696f6e"` — 15 bytes (`4d 61 6e 69 66 73 74 2d…`, `Manifst-Version`): a dropped `65`/`e` byte after `66`/`f`. The embedded JSON line purports to be the verbatim output of its own `$` command and is not — the M39 transcription defect stands byte-for-byte.
- Reject still justified: a knowledge entry whose reproduced command output silently drops a byte fails the verbatim-evidence bar outright; the drift is in the load-bearing member record, not a cosmetic line.
- Corroboration (not required by the brief, run as an independent check): the landed C7 gate `corpus/check_embedded_outputs.py --entry` over this file exits 1 printing `drift entry:41 embedded output line not in recheck stdout` (checked_blocks=15 problems=1) — the C7_RED_ON_R65_CANDIDATE red-before is real and attributed to exactly this line; over the v2 candidate it exits 0 (checked_blocks=16 problems=0), consistent with C7_V2_CLEAN.

Verdict: REJECT remains calibrated — the falsifying evidence re-derives from the committed fixture bytes today. AGREE.

## Tooling

None installed or updated; existing `python3`/`sha256sum`/`wc` sufficed. Pacman untouched (host-wide pause).

## Bounds

Read-only review; the only write is this report at `.ufo/waves/round-67/R67SpotcheckDiscern.md`. No corpus/reports/git/jj mutations; no peer contact; no subagents.
