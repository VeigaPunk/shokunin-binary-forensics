PASS — Q14 holds on the landed v5.1 bytes: no clause anywhere in the file pairs a hex run with a wrong byte count, no ellipsis-truncated run carries a length, and no ASCII rendering fails to decode from its run; lint Q14=0 and every value re-derived from a `git archive 17ee7f87` extraction matches the embedded lines.

Seat: R70W2GateQ14 (fresh wave-2 admission reviewer, criterion Q14 only) · 2026-10-25
Target: `corpus/knowledge/round-70-apk-axml-byte-evidence.md` at lane commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd` (`admission-status: candidate`), entry sha256 `819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31` (322 lines, 38186 bytes).
Basis read first: `reports/round-70/claims.md` §C1 (frozen predicate + kill rule), `corpus/QUALITY.md` Q14 row. I did not read `.ufo/waves/round-70/w1/`.

## Decision

**Q14: PASS** on these bytes. The three Q14 rules, judged over every clause of the whole file (header lines 1-11, items 1-17 prose and fenced output, Observation/inference/unknown, Limitations, cross-lane note, §Q-map, Reproduce):

1. **Hex + byte count in the same clause → 2×N hex characters.** No prose clause attaches a byte count to a hex run at all (independent sweep inventory: empty; the only backticked-hex+count clause in the file is none). The one fenced-output co-occurrence is consistent: entry line 36 `eocd signature bytes at offset 925: 504b0506 (4 bytes)` — `504b0506` is 8 hex chars = 4 bytes, and I re-derived it independently: `apk[925:929].hex()` → `504b0506` from the extracted `fixture.apk` (itself sha256 `05d2280f…`, 947 bytes, matching item 1).
2. **Ellipsis-truncated run carries no length.** The file contains zero U+2026 `…` characters (`grep -c …` → 0) and exactly one ASCII `...`, at line 288 (Limitations), inside a quoted readout comment — `readout.py:49-50` still comments that widths are "computed here ... not assumed" — with no hex run and no length in that clause. Vacuously satisfied.
3. **`ASCII \`…\`` rendering decodes from that same run.** The file contains zero `ASCII` renderings (`grep -n "ASCII"` → no matches). The only ASCII-ish renderings are tool-output fields, each verified against its sibling hex: `magic_ascii: "dex\n"` beside `magic_hex: "6465780a30333500"` (entry line 105) — `6465780a` decodes to `dex\n`; the readout renders `magic[:4].decode("ascii")` by construction (`readout.py:238`), and the entry's item 9 prose claims no semantics for `magic`. Item 2 prose's `b"PK\x05\x06"` decodes to `504b0506`, matching the output's `504b0506 (4 bytes)`.

## Evidence — commands and observed output

All commands run on a `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd | tar -x -C /tmp/revenger-r70-R70W2GateQ14-tree` extraction; no lane file written.

1. **Mechanical lint on the landed bytes** (`python3 -B corpus/lint_entry.py --entry <landed entry copy>`; worktree `corpus/lint_entry.py`, `corpus/QUALITY.md` and the entry are byte-identical to the landed commit — `git diff --stat 17ee7f87… -- <those paths>` empty):
   ```
   LINT_QMAP=0
   LINT_Q14=0
   LINT_Q15=0
   LINT_HEADER=0
   LINT_EXIT=0
   ```
2. **Independent clause sweep (stronger than the lint).** I wrote a sweep that, unlike `lint_q14` (prose lines only, exactly one backticked run, counts ≤32 bytes, 40/64/128 excluded as digests), scans every clause of every line including fenced output, bare (unbackticked) hex, multi-run clauses, counts of any size, `\d+B` phrasings, and ASCII renderings. Result on the landed bytes: `0 findings`; the hex-run+count inventory is empty. Sensitivity check: planting `prints the four bytes \`504b0506\` (5 bytes)` into a scratch copy is caught (`line 30 [LEN-MISMATCH] hex 504b0506 = 8 chars = 4 bytes but clause says 5 bytes`).
3. **Full re-derivation of the entry's own commands.** All 24 embedded `$` command segments (readout facts, `entry_checks.py --eocd/--spec-quotes/--zip-layout/--oracle/--pins/--stdout-digest/--container/--axml-layout`, `derive_axml_anchors.py`) re-run from the extraction: **134/134 embedded output lines appear verbatim in actual stdout, and every segment's embedded line count equals the actual line count** (no unembedded stdout lines — stronger than the embedded-output gate's one-directional check). All ten item-14 pins digests re-verified against the extraction (e.g. `readout.py` `92e347c3…`, `entry_checks.py` `2d4f25f6…`, `ResourceTypes.h` `56b88bc4…`, `APPNOTE.TXT` `0b993022…`, `dex-format.html` `c0428612…`, `rea-android-applications.md` `412d9cb4…`).
4. **Byte-level cross-checks of every length-bearing hex value.** From the extracted `fixture.apk`: archive 947 bytes sha256 `05d2280f…` (item 1 ✓); EOCD signature at 925 = `504b0506` (item 2 ✓); each member's `payload_first16_hex` is exactly 32 hex chars = 16 bytes and equals my independently recomputed first 16 payload bytes for all three members (`03000800a001000001001c00c4000000`, `6465780a30333500300c123da5fc7bea`, `4d616e69666573742d56657273696f6e`) ✓; dex `magic_hex` 16 chars = 8 bytes, `magic_ascii` = its first 4 bytes ✓; dex signature field `a5fc7bea8fa9ffaa52243540c8026066511b9fce` = 40 hex = 20 bytes (SHA-1) ✓; the quoted S048 phrase's `0x70 (112) bytes` (entry line 147, command output quoting the snapshot verbatim) is a field-value notation, and `0x70 = 112` numerically ✓.
5. **Odd-length hex-like tokens:** the only ones in the file are decimal file sizes in item 14's pins output (`11236`, `15062`, `86255`) — not hex claims.

## Boundary decisions (stated, not hidden)

- **File digests beside file sizes** (item 14's `sha256 <64hex> N bytes <path>` lines, and JSON `"bytes": 947` beside a 64-hex `sha256` field): treated as digests, not byte runs — the same exclusion the frozen lint documents ("digest lengths (40, 64, 128) are file digests, not byte runs") and the only reading under which Q14's lesson (M39/M47: "nine bytes called 'the 16-byte prefix'") is coherent. A literal reading would condemn every sha256-with-size line, which cannot be the criterion's intent.
- **`0x70 (112) bytes`** (line 147): the spec's own value notation quoted verbatim for the S048 anchor; `0x70` is a field value equal to the count, not a byte-run quote; numerically consistent.
- **`0x0001`-style enum constants** (item 4 prose, line 54; `0xFFFFFFFF` at line 86): hex literals for values, no byte count attached to either — outside all three Q14 defect classes.

## Observation (not a Q14 defect; no action required for this criterion)

The entry's own §Q-map Q14 row (line 311) states "every hex string is printed inside a command block". Read literally that is imprecise: item 4's prose (line 54) quotes `0x0001`/`0x0180`/`0x0100`/`0x0102`/`0x0103`/`0x0101` and item 8's prose (line 86) has bare `0xFFFFFFFF` outside command blocks (their values are printed by commands — item 11's enum lines and item 8's decimal `ns_index: 4294967295` — so the provenance reading of the row holds). This is a wording nuance in the row's basis, not one of Q14's three defect classes (length mismatch / truncated-with-length / ASCII-not-decoding), so it does not change this decision; flagging it for the record only. Per the assignment I did not treat the §Q-map row as evidence — the decision above rests on the sweep, the lint, and the re-derivations.

## Residual risk / verification gaps

- My sweep's ASCII rule was initially written leniently (it would also accept a rendering longer than its run); since the file contains zero `ASCII \`…\`` renderings, lenient vs strict cannot change the outcome on these bytes. The planted-defect sensitivity test for the length rule passed.
- I judged Q14 only; Q01-Q13/Q15 decisions belong to their seats. The lint's Q15/HEADER/QMAP zeros are consistent with the C1 mechanical conjuncts but are not my criterion.
- Scratch (`/tmp/revenger-r70-R70W2GateQ14-*`) deleted before return; no lane file written; no mutating git/jj command run; no packages installed (stdlib only).
