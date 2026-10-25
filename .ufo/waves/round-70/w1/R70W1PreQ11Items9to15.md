# R70W1PreQ11Items9to15 — Q11 over items 9-15, Limitations, Cross-lane note, §Q-map, Reproduce

**FAIL (Q11)** — 22/22 embedded `$` blocks reproduce byte-exactly, but Q11's reject condition is met in four
places in my region: two wrong spec line ranges with no deriving command (item 12), a record value
(`method 0`) stated with no command while the oracle declares and the comparison drops it (Limitations),
a false universal ("every file", item 14 — the script that prints items 12-15 is unpinned), and a wrong count
("five derivation flags" listing six, Reproduce). The §Q-map Q11 row (`:259`) is therefore not supported and
must not stay `pass` on these bytes.

Bytes judged: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin show
aa1842fac199aa524930e5565ed3715de5f84c6d:corpus/knowledge/round-70-apk-axml-byte-evidence.md`
sha256 `0913f6515e93889a7a4204a613f52a3ff8d505742038dfa0d46443a79b088368`, 273 lines. The working tree equals
this commit for every file I attack (`git show <commit>:<path> | sha256sum` == `sha256sum <path>` for the entry,
`readout.py` `92e347c3…`, `entry_checks.py` `68b1124f…`, `derive_axml_anchors.py` `74d4c0d9…`,
`check_embedded_outputs.py` `79cff2fa…`, `lint_entry.py` `43364943…`, `truth.json` `27303bae…`,
`fixture.apk` `05d2280f…`). Commands were run both from the lane root and from a `git archive` extraction in
`/tmp/revenger-r70-R70W1PreQ11Items9to15`; every output below is from that extraction (identical bytes).

## Re-run of the entry's own commands (my independent parser, not the entry's gate)

```
22 blocks   ALL EXACT: True
OK  104 readout.py --fact dex_declared_header          rc 0 emb 1  act 1
OK  113 readout.py --fact jar_manifest                 rc 0 emb 1  act 1
OK  122 corpus/derive_axml_anchors.py                  rc 0 emb 20 act 20
OK  143 entry_checks.py --spec-quotes                  rc 0 emb 6  act 6
OK  155 entry_checks.py --zip-layout                   rc 0 emb 17 act 17
OK  178 entry_checks.py --oracle                       rc 0 emb 28 act 28
OK  212 entry_checks.py --pins                         rc 0 emb 9  act 9
OK  227 entry_checks.py --stdout-digest                rc 0 emb 1  act 1
```

`python3 -B corpus/fixtures/apk-r65/readout.py` → exit 0, `wc -l` = 15,
`sha256sum` = `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` = item 15's line.
Gate and lint on these bytes: `check_embedded_outputs.py --entry` → `checked_blocks=22 problems=0` exit 0;
`lint_entry.py --entry` → `LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0 LINT_HEADER=0` exit 0. **Neither mechanical label
sees D1-D5** — that is the whole value of this seat.

## Findings (each: entry line, wrong value, deriving output, exact correction)

### D1 — Reproduce `:273`: "The five derivation flags" lists six (FAIL, count + wrong number)

```
L273: … The five derivation flags are `--pins`, `--eocd`, `--oracle`, `--zip-layout`, `--spec-quotes` and
      `--stdout-digest` of `corpus/fixtures/apk-r65/entry_checks.py`.
```
Six flags named; `entry_checks.py:195-196` dispatches exactly six:
`cmds = {"--pins": pins, "--eocd": eocd, "--oracle": oracle, "--zip-layout": zip_layout, "--stdout-digest":
stdout_digest, "--spec-quotes": spec_quotes}`. The header's own `recheck:` (`:9`) says "the **five**
`entry_checks.py` flags named in items 11-15" and is correct (items 11-15 name `--spec-quotes`, `--zip-layout`,
`--oracle`, `--pins`, `--stdout-digest` = 5), which proves `:273` is the slip, not a deliberate scope.
Correction: `The six derivation flags are \`--pins\`, \`--eocd\`, \`--oracle\`, \`--zip-layout\`,
\`--spec-quotes\` and \`--stdout-digest\` of \`corpus/fixtures/apk-r65/entry_checks.py\`.`

### D2 — item 12 `:152`: two of three cited APPNOTE line ranges are wrong, and no command prints any of them (FAIL)

```
L152: … the layouts are APPNOTE snapshot lines 387-398, 511-531 and 632-646) …
```
Actual snapshot (`corpus/snapshots/APPNOTE.TXT`, digest `0b993022…`, the same file item 14 pins):
```
$ grep -n '4\.3\.7  Local file header\|4\.3\.12  Central directory\|4\.3\.16  End of central' corpus/snapshots/APPNOTE.TXT
387:   4.3.7  Local file header:
511:   4.3.12  Central directory structure:
632:   4.3.16  End of central directory record:
$ awk 'NR==398||NR==399||NR==531||NR==532||NR==534||NR==538||NR==646' corpus/snapshots/APPNOTE.TXT
398:      file name length                2 bytes
399:      extra field length              2 bytes
531:        uncompressed size               4 bytes
532:        file name length                2 bytes
534:        file comment length             2 bytes
538:        relative offset of local header 4 bytes
646:      .ZIP file comment length        2 bytes
```
- `387-398` stops one line before the local header's `extra field length` (399), which `LOCAL_HEADER`
  (`entry_checks.py:50`) transcribes. Correct range: **387-399**.
- `511-531` stops at `uncompressed size`; the seven central fields the entry transcribes at spec offsets 28/30/32/
  34/36/38/42 live at snapshot lines **532-538**. Correct range: **511-538**.
- `632-646` is correct (heading 632 → comment length 646).
Second half of the defect: no command in the entry prints these numbers, so all three are "cited to prose"
under Q11 — exactly the class item 12 exists to eliminate for offsets.
Correction (value + derivation in one): change the parenthetical to `APPNOTE snapshot lines 387-399, 511-538 and
632-646` and extend `--zip-layout` to print, per record, the section heading line and the last transcribed field
line it finds in the snapshot, e.g.
```
appnote 4.3.7  Local file header: heading 387, last transcribed field line 399
appnote 4.3.12 Central directory structure: heading 511, last transcribed field line 538
appnote 4.3.16 End of central directory record: heading 632, last transcribed field line 646
```
(paste the real stdout). The header's `source:` rows 4 and 5 carry the same wrong ranges and must be repaired in
the same pass, or the entry contradicts itself.

### D3 — Limitations `:239`: "stored (method 0) with no data descriptors" has no deriving command, and item 13 `:175` silently drops exactly that oracle field (FAIL)

```
L239: … The container is stored (method 0) with no data descriptors, so the walk does not exercise
      compression, split archives or spanned records. …
$ grep -n 'method\|descriptor' corpus/fixtures/apk-r65/readout.py      # (no output: the readout never reads it)
```
`method` is an oracle field — `truth.json` members carry `"method": 0` ×3 — but `entry_checks.py --oracle`
(`:132-147`) compares only `local_header_offset`, `compressed_size`, `crc32`, `sha256` per member, and
`--pins`/`--zip-layout` print no method. My leaf audit of `truth.json`:
```
leaves 3 (image) + 21 (members) + 2 + 15 (attributes) = 41 ; compared labels = 28 ; uncompared = 13
uncompared: image.path; 3x <member>.name; 3x <member>.method (=0); 3x <member>.uncompressed_size;
            3x axml.attribute[i].data (=4,1,8)
```
So `:175`'s "compared **field by field** with the authored oracle" is false as a coverage claim (28 of 41 oracle
leaf values), and the one record value Limitations states — `method 0` — is one of the 13 the comparison skips.
`no data descriptors` (general-purpose flag bit 3, local header +6) and the spanned-record claim (EOCD disk
numbers +4/+6) are likewise unprinted.
Correction, minimal and honest (one of two, either is acceptable):
(a) derive it: add a `--container-flags` flag printing, per member,
`<name>: method=u16(lh_off+8)=0 gp_flag=0x0000 data_descriptor_bit3=0` and `eocd: disk=0 cd_disk=0`, embed the
output under item 12 or 3, and change `:175` to `The readout's facts compared with the authored oracle
`truth.json` for the fields listed in this block (13 of its 41 leaf values are not compared: `image.path`,
each member's `name`, `method` and `uncompressed_size`, and each attribute's `data`)`;
(b) or narrow `:239` to `The authored generator declares method 0 and no data descriptors (`truth.json`
`members[].method`); neither is re-derived in this entry` and narrow `:175` to `the four member fields this block
lists`.
Either way `:259`'s Q11 universal must be restated (see D6).

### D4 — item 14 `:209`: "every file this entry's claims rest on" is false — `entry_checks.py` is unpinned (FAIL)

```
L209: 14. Digests and sizes of every file this entry's claims rest on, recomputed from bytes …
$ grep -c '68b1124f' corpus/knowledge/round-70-apk-axml-byte-evidence.md
0
```
Items 12-15 (and item 2's second command) are produced by `corpus/fixtures/apk-r65/entry_checks.py`
(`sha256sum` → `68b1124fff206cc43c957cc3eb4e203c03a622ee4fd010075c884fe333e56049`, `wc -c` → `9092` bytes), and
its digest appears nowhere in the entry. `PINS` (`entry_checks.py:34-44`) lists 9 files, none of them the derivation script itself; `--pins`
prints 9 lines, all exact against `sha256sum`. The `verified-at:` line also names `check_embedded_outputs.py`
and `lint_entry.py` (recheck instruments, arguably outside "claims rest on").
Correction: add `"corpus/fixtures/apk-r65/entry_checks.py"` to `PINS` and re-paste `--pins` (10 lines); the
sentence then becomes true. If the author prefers to keep 9 pins, narrow it to `Digests and sizes of every
record file this entry's claims rest on (the derivation script `corpus/fixtures/apk-r65/entry_checks.py` is the
one load-bearing file not pinned here)`.

### D5 — item 9: the dex header offsets the derivation rests on are assumed, not derived (FAIL against Q11's "constants such as header offsets are derived")

Item 9 (`:101`) credits `readout.py:233-248` (verified: that range is exactly the dex block, `magic = dex[:8]` at
233 … `header_bytes=len(dex)` at 248) and S045's four quoted phrases (item 11 prints them at dex-format.html
5949/5956/5981/5035). But the field *offsets* the readout uses — checksum 8, signature 12..32, file_size 32,
header_size 36, endian_tag 40 — are literals in `readout.py` and **no command in the entry prints or sums them**,
while the ZIP offsets get exactly that treatment in item 12. The S045 snapshot carries the widths needed
(`grep -n 'ubyte\[8\] = DEX_FILE_MAGIC\|ubyte\[20\]\|uint = ENDIAN_CONSTANT' corpus/snapshots/dex-format.html`
→ 5941, 5955, 5991), so the repair is a direct analogue of `--zip-layout`:
Correction: add `entry_checks.py --dex-layout` printing
`magic offset 0 width 8 / checksum offset 8 width 4 / signature offset 12 width 20 / file_size offset 32 width 4 /
header_size offset 36 width 4 / endian_tag offset 40 width 4` with each literal present in `readout.py`, and
embed it under item 9 with the sentence `the field offsets are summed here from S045's header_item widths and
each is compared with the literal in the readout source`. Without it, item 9's values are correct
(I re-derived them from `payload_first16_hex` `6465780a30333500 300c123d a5fc7bea…`: bytes 8-11 LE =
`0x3d120c30` = `declared_checksum`; bytes 12-31 = `a5fc7bea8fa9ffaa52243540c8026066511b9fce`) but underived.

### D6 — §Q-map `:259`: the Q11 row asserts a universal the bytes do not satisfy (FAIL as written)

```
L259: | Q11 | pass | every count, offset, identifier and digest carries its deriving command and output in
      items 1-15; the recorded values (APPNOTE widths) are labeled recorded where used; no value is cited only
      to prose. |
```
Falsified by D1 (count), D2 (line ranges, both wrong and underived), D3 (`method 0`), D4 (unpinned script),
D5 (dex offsets). The row must not read `pass` until D1-D5 are repaired. Proposed replacement text once repaired:
`| Q11 | pass | every count, offset, identifier and digest in items 1-15 carries its deriving command and output
(1-2 archive/eocd, 3-8 members and AXML chunks, 9 dex layout via --dex-layout, 11 S038/S043/S045 anchors,
12 APPNOTE layouts and section lines, 13 oracle comparison, 14 pins incl. the derivation script, 15 stdout
digest); the APPNOTE widths are labeled recorded where used. |`
Also note the row's scope word `items 1-15` does not cover Limitations/Reproduce, where D1 and D3 live — after
repair the row should say `in this entry` or name those sections.

## What holds in my region (with the line that proves it)

| criterion / value | decision | evidence |
|---|---|---|
| Q11 items 9-10, 11, 13, 15 blocks | PASS | 22/22 blocks exact; `--spec-quotes` 6 lines exact; `--oracle` 28 lines exact; `--stdout-digest` `15 lines, sha256 507d79f8…` exact and independently reproduced |
| Q11 item 11 derivation honesty | PASS | `derive_axml_anchors.py:74-129` searches the snapshot lines for each symbol and `fail()`s (exit 2) on absent/ambiguous; snapshot digest re-checked at `:106-108` against pin `56b88bc4…`; 20 lines, all exact |
| Q11 item 12 offsets (values) | PASS | `--zip-layout`: `local fixed part: 30`, `central fixed part: 46`, `eocd fixed part: 22`, 14 `MATCH … present=True`; my own sums from the snapshot field lists reproduce 30/46/22 and offsets 10/12/16 (eocd), 28/30/32/42 (central), 14/18/22/26/28 (local) |
| Q11 item 14 digests/sizes | PASS (values) | `--pins` 9 lines; independent `sha256sum` of the same 9 files matches every hex and every byte count |
| Q11 `:239` `readout.py:49-50` | PASS | `awk 'NR>=49&&NR<=50'` → `# Every fixed offset the readout uses is computed here from the field widths … not assumed` — the "computed here … not assumed" quote is verbatim |
| Q11 `:239` three attributes / UTF-8 / no CDATA / no nesting / header-only dex | PASS | item 8 `"attributeCount": 3`; item 6 `"utf8": true, "styleCount": 0`; item 4 chunk table has one start (272) + one end (368) element and no type 260 (`0x0104`); item 9 `"file_size": 112, "header_size": 112` |
| Q14 (`:262` row) | PASS | `4d616e69666573742d56657273696f6e` = 32 hex = 16 bytes = `b'Manifest-Version'`; `6465780a30333500` = 16 hex = 8 bytes, no prose count; the 64-hex digests carry no prose count; no other prose byte count attaches to a hex run |
| Q15 (`:263` row) | PASS | no git object id in the entry; the only 40-hex run is the dex `signature_sha1` printed by item 9 (`a5fc7bea…`), not a git id; identity statements are item 14's file digests |
| Q13 (`:261` row) | PASS | gate detection is set membership (`check_embedded_outputs.py:113-115,139-140`), which is exactly the clause the entry credits ("every embedded line appears in its command's stdout"); run on these bytes: `checked_blocks=22 problems=0` exit 0 |
| Q09 (`:257` row / item 14 sentence) | PASS | `:209` sentence disclaims origin/completeness in the same clause that prints the digests |
| Q05 / Q10 (Cross-lane note `:243`) | PASS | no provider run, no readiness or exit-status claim; `ADJ-06` resolves: `grep -n 'ADJ-06' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` → `42:` (tsukuroi r1, "arbitrate the kaidoku/revenger shipped-artifact overlap"); lane `SHONEN.md:27` cites the same `:42`. Reported, not absorbed ✓. Repair suggestion (not a FAIL): cite `.ufo/l0-questions.md:42` in the note as SHONEN.md does. |
| Q02 (`:250` row) | PASS | `source:` present for S038/S043/S045/S032/S034/S047/S041 (`:1-7`), `verified-at:` `:8`, `recheck:` `:9`, `coverage-map:` `:10` naming C05 |

## Q11 token table for my region (every count / hex / identifier / offset, and where it is printed)

| entry line | token | printed by | verdict |
|---|---|---|---|
| 101 | `readout.py:233-248` | `awk 'NR>=233&&NR<=248' readout.py` = dex block, 233 `magic = dex[:8]` … 248 `header_bytes=len(dex)` | PASS |
| 101 | "four quoted phrases" (S045) | item 11: 4 `MATCH dex-format.html` lines (5949, 5956, 5981, 5035) | PASS |
| 101 | `0x3d120c30`, `0x12345678`, `6465780a30333500`, `a5fc7bea…`, `112`, `035` | item 9 block (exact) | PASS |
| 119 | "second command", "four S045 phrases" | block has 2 commands; 4 dex MATCH lines | PASS |
| 152 | `387-398` | **no command**; snapshot has `4.3.7` at 387 and `extra field length` at 399 | **FAIL (D2)** |
| 152 | `511-531` | **no command**; `4.3.12` at 511, transcribed fields run to 538 | **FAIL (D2)** |
| 152 | `632-646` | no command; value correct (632 heading, 646 comment length) | value PASS / derivation FAIL (D2) |
| 152 | `30`, `46`, `22` | `--zip-layout` lines 1-3 (exact) | PASS |
| 152 | `LOCAL_HEADER`, `CENTRAL_HEADER`, `EOCD` | `entry_checks.py:48,51,56` | PASS (resolvable) |
| 152 | spec offsets 10/12/16/28/30/32/42/14/18/22/26/28 | `--zip-layout` 12 `MATCH … spec offset N` lines (exact) | PASS |
| 175 | "One line per compared field" | 28 `cmp` calls / 28 lines (exact) | PASS as written; "field by field" overstates 28/41 → **D3** |
| 209 | "every file" | `--pins` 9 lines; `grep -c 68b1124f` = 0 | **FAIL (D4)** |
| 239 | "three attributes" | item 8 `"attributeCount": 3` | PASS |
| 239 | `method 0`, "no data descriptors" | nothing (readout has no `method`/`descriptor` code) | **FAIL (D3)** |
| 239 | `readout.py:49-50` | `awk` 49-50 = "computed here … not assumed" | PASS |
| 243 | `ADJ-06` | fleet `.ufo/l0-questions.md:42` (no in-entry command; reported scope) | PASS (note) |
| 259 | Q11 universal | falsified by D1-D5 | **FAIL (D6)** |
| 262 | "16-byte … 32-hex-character" | `python3 -c` on the printed run: 32 hex / 16 bytes | PASS |
| 263 | "no git object id" | `grep -nE '\b[0-9a-f]{7,40}\b'` → only the dex sha1/crc32 runs | PASS |
| 273 | "Exit 0" | not printed; derivable only because `--stdout-digest` runs the readout with `check=True` (`entry_checks.py:172-173`) | partial — see note N1 |
| 273 | "15 stdout lines" | item 15 (exact) + my run (`wc -l` 15) | PASS |
| 273 | "five derivation flags" | six names in the same sentence; dispatch dict has six keys | **FAIL (D1)** |

## Notes (not defects, worth a repair line)

- **N1** Reproduce `:273` "Exit 0" is asserted, not shown. Tighten to `Exit 0 — item 15's command runs the
  readout with `check=True`, so a non-zero exit fails that block — and 15 stdout lines`.
- **N2** The Reproduce block is fenced ```` ```sh ```` without a `$ ` first line, so the registered gate does not
  cover it (that is why `checked_blocks=22`, not 23). Prefixing the command with `$ ` would put the entry's own
  headline command under the gate without changing any value.
- **N3** `--zip-layout`'s fixed-part check has a vacuous conjunct: `f"{want}" in literal` (`entry_checks.py:165`)
  is always true for the two hard-coded literals `cursor + 46` / `lh_off + 30`. The entry's credit ("compared
  with the literal in the readout source") is still honest because `literal in src` is the real test, but the
  flag would be stronger summing `offsets(...)` against the readout's literal in one expression.
- **N4** Item 11's block is the only place the S038 struct lines appear; the entry states no S038 line number in
  prose outside it, so "every S038 line number … is printed by the item-11 command" holds as written.

## Scope discipline

Read-only: no file in the lane, the fleet repo, `corpus/`, `reports/` or `shokuknow` was written; every mutation
test was a copy in `/tmp/revenger-r70-R70W1PreQ11Items9to15` (deleted before return). No subagents, no
`agent://all`, no git write, no jj. Tooling: none installed — `pacman` transactions are paused host-wide and
existing `python3` (stdlib only) covered every check; no upgrade was needed or attempted.
