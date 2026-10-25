FAIL — Q08 (Q11 applied for Q08): the v3 defects are genuinely repaired (19/19 stated S038 line numbers + 8 enum values now print, 30/30 embedded output lines verbatim), but Q11 is still not satisfied at `entry:30`, where the signature value `504b0506` is stated inside a block the entry says is readout-produced while no command in the entry prints those four bytes — the same ordinary defect the round-68 Q11 seat asked to be fixed (`R68ReviewEntryQ11.md` §5 item 3) and the same value the **admitted** round-63 entry prints (`r63:55` `"eocd_signature_hex":"504b0506"`).

Seat: `L1Revenger69.R69ReviewEntryQ08` (fresh leaf, non-author). Subject: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-69-apk-axml-byte-evidence.md`, sha256 `a43fc907461e2d7939aa50950cbbd044a47ae4df08ca3d7aaf646032e9257656`, 215 newline-terminated lines (216 by `splitlines()`; final line unterminated), `admission-status: candidate`. Criterion only: **Q08 — superseded by Q11 — verify the entry applies Q11, not Q08** (`corpus/QUALITY.md` Q08 row + Q11 row: "Supersedes Q08. Each count, identifier, offset and digest in an entry carries, inside the entry, the command that derives it from the primary record (bytes, saved tool output) and that command's output. Constants such as header offsets are derived, not assumed. A value cited only to prose is labeled recorded, not re-derived."). Read-only seat: no file edited, no git/jj mutation, no installs (no tool needed; Python stdlib + coreutils only). Scratch removed.

## 1. Routing half — PASS (Q08 is not applied anywhere)

```
$ grep -c "^| Q08" corpus/knowledge/round-69-apk-axml-byte-evidence.md
0
$ sed -n '/^## §Q-map/,/^## Reproduce/p' corpus/knowledge/round-69-apk-axml-byte-evidence.md | grep -o '^| Q[0-9]*' | tr '\n' ' '
| Q01 | Q02 | Q04 | Q05 | Q07 | Q11 | Q13 | Q14 |
```
No Q08 row exists, so nothing is judged under the superseded row; the verdict below is Q11's text applied to these bytes (Q08's own test — "re-derived by command" without the in-entry command/output — is not what the entry argues).

## 2. What re-derives clean (Q11's core is genuinely repaired for the v3 fail class)

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin
$ python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/revenger-r69-q08-readout.txt; echo EXIT=$?
EXIT=0
$ wc -l < /tmp/revenger-r69-q08-readout.txt
15
$ sha256sum /tmp/revenger-r69-q08-readout.txt
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247   # == entry:9 and entry:194
$ python3 -B corpus/derive_axml_anchors.py > /tmp/revenger-r69-q08-derive.txt; echo EXIT=$?
EXIT=0
$ wc -l < /tmp/revenger-r69-q08-derive.txt
20
```
- **Embedded-output fidelity:** 30 embedded `{…}` line occurrences (15 distinct × per-item block + §Reproduce), all 30 exact-string matches against the fresh stdout (`Counter({'EXACT': 30})`, zero drift). The long `axml_start_element` line (890 B) is not truncated in the file.
- **Derivation completeness (the r68 FAIL basis):** the 20-line stdout prints every stated S038 line number and value — `218 237 239 241 244 245 246 247 248 253 263 287 461 612 621 677 686 687 707` plus 8 `= 0x…` enum values. My regex sweep of every `:N` / `line N` token in the entry's prose returns only pointers to other files (`readout.py:22/:51-58/:99-105/:166/:200-203`, `entry:41`, `l0-questions.md:42`) as not-in-derive — **no S038 line number is unprinted**, and the entry's item-11 credit ("complete set of S038 line numbers this entry states") is therefore true, not an overstatement.
- **Independent snapshot reads confirm the roles:** `237: enum {`, `263: };`, `244: RES_XML_FIRST_CHUNK_TYPE = 0x0100`, `245: RES_XML_START_NAMESPACE_TYPE = 0x0100`, `686: // Byte offset … attributes start.`, `687: uint16_t attributeStart;`, `677: struct ResXMLTree_attrExt`.
- **Pins:** `readout.py 92e347c3…3976`, `derive_axml_anchors.py 74d4c0d9…83aa`, `fixture.apk 05d2280f…d03e`, `truth.json 27303bae…8173`, `generator.py eaa9444c…7c1a`, `snapshots/ResourceTypes.h 56b88bc4…c56f` (== the round-65 source snapshot copy).
- **Registered gate:** `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-69-apk-axml-byte-evidence.md` → `checked_blocks=17 problems=0`, EXIT=0.
- **Item 5 complies with Q11's escape clause:** "manually transcribed in `readout.py:51-58` … labeled manual, not a runtime derivation" — the widths block is at `readout.py:51-59` (51 = `w8, w16, w32 = 1, 2, 4`; 52-58 the six rows), so the pointer resolves.

## 3. F1 — FAIL basis: `entry:30`, `504b0506` has no in-entry derivation

Exact line:

> `2. The end-of-central-directory signature `504b0506` is located at file offset **925**; its record states **3** …`

Evidence that no command in the entry prints it:

```
$ grep -c "504b0506" /tmp/revenger-r69-q08-readout.txt
0
$ sed -n '76,86p' corpus/fixtures/apk-r65/readout.py
   76	    sig_eocd = b"PK\x05\x06"
   77	    eocd = apk.rfind(sig_eocd)
   ...
   81	    emit("eocd", eocd_offset=eocd,
   82	         total_entries_cd=total_entries,
   83	         size_of_central_directory=cd_size,
   84	         offset_of_start_of_cd=cd_off,
   85	         cd_end_equals_eocd_offset=(cd_off + cd_size == eocd),
   86	         parsed_entries=total_entries)
```
The eocd fact prints the **offset** (925) and the record's counts, but never the four signature bytes. The bytes are nonetheless correct:

```
$ dd if=corpus/fixtures/apk-r65/fixture.apk bs=1 skip=925 count=4 2>/dev/null | xxd -p
504b0506
```
Why this is a Q11 reject, not a nit:
1. Q11 requires the value to carry the command **and that command's output**; here the output does not contain the value (reject clause: "a value is correct when re-derived but the entry carries no derivation").
2. The entry's §Observation opens "Every numbered item below is produced by the readout in §Reproduce", and `entry:182` (Q-map Q11) asserts "every count, offset, identifier and digest carries its deriving command and output in §Observation (items 1-10)" — both claims are false at this value.
3. It is not a prose-cited constant either: the entry's own S032 row is scoped to "central directory file header field layout … `§4.3.12` (46-byte fixed part)" — the end-of-central-directory record is outside that scope, so the "labeled recorded" escape is unavailable as written.
4. The lane's admitted precedent for the identical value prints it: `corpus/knowledge/round-63-zip-central-directory-evidence.md:55` shows `{"fact":"eocd", …, "eocd_signature_hex":"504b0506", …}` (admission-status: admitted). The v4 is below the lane's own admitted bar on the same record.
5. `reports/round-68/` `.ufo/waves/round-68/R68ReviewEntryQ11.md` §5 item 3 named this exact repair — "`504b0506` → emit `signature_hex` in the `eocd` fact (the bytes are already at `readout.py:76-77`)" — and the v4 did not apply it.

Correct value: `504b0506` (verified above); the defect is the missing derivation. Smallest fix: add `signature_hex=sig_eocd.hex()` to the `eocd` emit (`readout.py:81-86`), re-capture the 15-line stdout and its SHA-256 pin (`entry:9`, `entry:194`), and the item-2 sentence then carries its own output.

## 4. F2 — same class, recorded as LOW (not the fail basis)

`entry:109`: "Its declared checksum **`0x3d120c30`** equals the Adler-32 recomputed over the bytes **from offset 12 on** … and its declared 20-byte signature equals the SHA-1 recomputed over the bytes **from offset 32 on**". Both offsets are stated; neither is printed (the `dex_declared_header` fact at `readout.py:237-248` emits no offset field; the slices are `dex[12:]` at `readout.py:241` and `body_after_sig = dex[32:]` at `readout.py:236`). Both values are correct (8-byte magic + 4-byte checksum = 12; + 20-byte signature = 32), and the sentence quotes S045's field semantics in place, so this reads as recorded-from-spec rather than derived. I do **not** fail on it: the round-68 Q11 seat's §5 correction list did not name these offsets, so elevating them here would exceed the lane's own established bar. It remains a named residual of the same shape as F1.

## 5. LOW items already settled by precedent (recorded so the next pass does not re-litigate)

- Source-row anchors without in-entry commands: snapshot sizes `86255`/`281157` (`entry:1`, `entry:3`) and the S043/S045/S041 header digests. Verified correct on disk; presentation gap only — the exact category `.ufo/waves/round-68/R68ReviewEntryQ08.md` §4 L1 and the round-65/67 Q11 reports treat as non-failing.
- S032/S034 fixed widths `46`/`30` (`entry:37`): hard-coded in `readout.py` but attributed "per S032 §4.3.12" / "per S034 §4.3.7", which is the labelling alternative the round-68 Q11 seat's §5 item 3 itself prescribed. Compliant.
- `0xffffffff` (`entry:91`) is printed as decimal `4294967295` with the `NO_INDEX` literal at `readout.py:22`; `0x100` is printed inside `flags:"0x00000100"` with `utf8:true`. Value present.
- Item 11's line-count arithmetic is exact: 1 digest + 7 struct + 2 bounds + 8 enum + 2 attributeStart = 20 = `wc -l`.

## 6. Adjacent observations (outside my criterion, for the owning seats)

- `entry:184` (Q14) says "`0300 0800 a001 0000`/`6465780a30333500`/`504b0506` carry byte counts from their own clauses"; `entry:30`'s clause states no byte count for `504b0506`. That is a Q14 question, not mine.
- The v4 did not add a truth.json comparison command, so the §Comparison sentence ("The readout values agree with it on every shared field") is asserted without embedded compare output — the round-68 Q11 seat's §5 item 3 fourth bullet. Q03/Q11 territory; I verified the oracle's `resource_ids` array matches the printed `axml_resource_map` ids, so the assertion is factually true.

## 7. Residual risk / verification gaps

- No LSP server is applicable to a Markdown corpus entry; all checks were command-execution and byte reads (stated as the literal fallback).
- I could not test whether the adjudicator treats prose-cited constants as failing under Q11 generally; my verdict follows the assignment's rule ("a value that the command does not print is a FAIL for Q11") at the one locus where the lane's own admitted entry prints the same value and its own round-68 Q11 seat demanded the fix.
- Everything else in the v4's Q11 surface (embedded fidelity, derivation completeness, bounded credit, manual labelling, digest pins) reproduces byte-for-byte and is not in doubt.

Tooling: none installed or updated (no need; pacman guard respected).
