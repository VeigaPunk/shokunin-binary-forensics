MATCH — `member[AndroidManifest.xml]` re-derives byte-identically: the command's actual stdout is 365 bytes, sha256 `d475f62a5988bc19e648255b745fbc8e5c4b6042dfde70a42fd5578ce1dd5907`, and the entry's embedded line at `corpus/knowledge/round-69-apk-axml-byte-evidence.md:41` (duplicated verbatim at `:203`) is the same 365 bytes with all 11 fields equal; the prose around the fact states nothing the output does not support.

Seat: L1Revenger69.R69Item3 (leaf, per-item re-derivation of the AndroidManifest member fact). Read-only: nothing edited, no git write, no package install (pacman is paused host-wide; no tool was needed — `python3 -B` stdlib only).

## 1. Command and actual output

From the lane root `/home/vgpnk/Projects/shokunin/revenger-shokunin`:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[AndroidManifest.xml]'
{"cd_index": 0, "compressed_size": 416, "crc32": "962d075f", "crc32_matches": true, "crc32_recomputed": "962d075f", "fact": "member[AndroidManifest.xml]", "local_header_offset": 0, "payload_first16_hex": "03000800a001000001001c00c4000000", "payload_offset": 49, "sha256": "73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4", "uncompressed_size": 416}
EXIT=0
```

Captured stdout: 366 bytes on disk including the trailing `\n`; 365 bytes excluding it. sha256 of the 365-byte line: `d475f62a5988bc19e648255b745fbc8e5c4b6042dfde70a42fd5578ce1dd5907`. Interpreter: the host's `python3` (stdlib `struct`/`zlib`/`hashlib` only; no site-packages needed).

## 2. The entry's embedded line and its location

- `corpus/knowledge/round-69-apk-axml-byte-evidence.md:40` — the `$ python3 -B … --fact member[AndroidManifest.xml]` command line
- `corpus/knowledge/round-69-apk-axml-byte-evidence.md:41` — the embedded output line (inside item 3, the "Walking the three central-directory records…" block)
- `corpus/knowledge/round-69-apk-axml-byte-evidence.md:203` — the same line again inside the §Reproduce full-stdout block

Byte checks (`diff` of each embedded line against the captured stdout file):

```
$ sed -n '41p'  corpus/knowledge/round-69-apk-axml-byte-evidence.md | diff - /tmp/revenger-r69-item3/actual.json && echo LINE41_IDENTICAL_BYTES
LINE41_IDENTICAL_BYTES
$ sed -n '203p' corpus/knowledge/round-69-apk-axml-byte-evidence.md | diff - /tmp/revenger-r69-item3/actual.json && echo LINE203_IDENTICAL_BYTES
LINE203_IDENTICAL_BYTES
```

Both embedded occurrences: `len(line) == 365`, `line == actual` → True, sha256 `d475f62a5988bc19e648255b745fbc8e5c4b6042dfde70a42fd5578ce1dd5907`. Key order, separators (`, ` / `": "`), spacing and number formatting are identical to the JSON the readout prints (`json.dumps(..., sort_keys=True)` shape); nothing was reflowed.

## 3. Field-by-field verdict

Parsed both sides (`json.loads`) and compared the union of keys:

| field | actual | embedded (:41/:203) | verdict |
|---|---|---|---|
| `cd_index` | `0` | `0` | equal |
| `compressed_size` | `416` | `416` | equal |
| `crc32` | `"962d075f"` | `"962d075f"` | equal |
| `crc32_matches` | `true` | `true` | equal |
| `crc32_recomputed` | `"962d075f"` | `"962d075f"` | equal |
| `fact` | `"member[AndroidManifest.xml]"` | `"member[AndroidManifest.xml]"` | equal |
| `local_header_offset` | `0` | `0` | equal |
| `payload_first16_hex` | `"03000800a001000001001c00c4000000"` | same | equal |
| `payload_offset` | `49` | `49` | equal |
| `sha256` | `"73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4"` | same | equal |
| `uncompressed_size` | `416` | `416` | equal |

Key sets equal (`11 == 11`), no extra key on either side, no absent key, no type mismatch (ints stay ints, booleans stay booleans). **Fields that differ: none.**

Independent re-derivation from the fixture bytes, so the match is not just "the same script twice" (`python3` inline, reading only `corpus/fixtures/apk-r65/fixture.apk`):

```
signature at 0: 504b0304 PK\x03\x04
local name_length 19 extra_length 0 name AndroidManifest.xml
derived payload_offset 49
compressed_size 416 uncompressed_size 416
crc32 stated 962d075f recomputed 962d075f match True
sha256 payload 73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4
first16 03000800a001000001001c00c4000000
payload len 416
```

and `compression_method 0 (0=stored)`, flags `0x0`, version-needed 20 — i.e. the stored/no-descriptor shape the entry's Limitations section claims. Ancillary replay of the entry's own recheck at `:16`/§Reproduce: `python3 -B corpus/fixtures/apk-r65/readout.py` → exit 0, 15 stdout lines, sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — exactly the digest the entry states, and the member line is one of those 15.

Oracle cross-check, `corpus/fixtures/apk-r65/truth.json` (`members[0]`): `compressed_size 416`, `crc32 "962d075f"`, `local_header_offset 0`, `method 0`, `name "AndroidManifest.xml"`, `sha256 "73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4"`, `uncompressed_size 416` — every shared field agrees with the actual output, including `method 0`, which the fact line does not print.

## 4. Prose judgment (does the sentence state anything the output does not support?)

Two prose sentences bear on this fact.

**Item 3, `:37`** — "Walking the three central-directory records (46-byte fixed part per S032 §4.3.12) and their local headers (30-byte fixed part per S034 §4.3.7) selects three members; every member's stated CRC-32 equals the CRC-32 recomputed over its payload bytes, and the walk's end cursor equals the end-of-central-directory offset. Each member's `payload_offset` is derived by the readout as `local_header_offset + 30 + name_length + extra_length` from the S034 §4.3.7 field list (readout.py:99-105), not assumed."

- "selects three members": supported by the `eocd` fact (`"parsed_entries": 3`, `"total_entries_cd": 3`) and the three `member[...]` facts (`cd_index` 0/1/2).
- "every member's stated CRC-32 equals the CRC-32 recomputed over its payload bytes": supported literally by this line (`crc32_matches: true`, `crc32 == crc32_recomputed == "962d075f"`) and by the two sibling member lines at `:43` and `:45`.
- "the walk's end cursor equals the end-of-central-directory offset": supported by `cd_end_equals_eocd_offset: true` (`:35`-block fact), not by this line — correctly attributed to the item-2/3 block as a whole.
- "`payload_offset` is derived as `local_header_offset + 30 + name_length + extra_length` from the S034 §4.3.7 field list (readout.py:99-105), not assumed": the cited range is accurate — `readout.py:99` `lh_name_len = u16(apk, lh_off + 26)`, `:100` `lh_extra_len = u16(apk, lh_off + 28)`, `:105` `payload_off = lh_off + 30 + lh_name_len + lh_extra_len`. The prose attributes the formula to the script, and the script is where those two operands come from; I confirmed them on the bytes (`name_length 19`, `extra_length 0` → `0+30+19+0 = 49`, matching `payload_offset: 49`). **Residual, not a defect:** the fact line prints only the endpoints (`local_header_offset`, `payload_offset`), not `name_length`/`extra_length`, so the 49 cannot be recomputed from that one line alone without the script or the bytes. The sentence does not claim otherwise — it names `readout.py:99-105` as the source of the derivation — so no unsupported statement is made.
- The 46-byte / 30-byte fixed widths are the walk's own cursor arithmetic (`readout.py:96` `cursor += 46 + name_len + extra_len + comment_len`, `:105` `+ 30`) and are cited to S032 §4.3.12 / S034 §4.3.7, both present in the entry's `source:` header. They are spec citations, not claims about the output; the bytes agree (local-header fixed part 30, central-directory fixed part 46).

**Item 4, `:52`** — "The `AndroidManifest.xml` payload begins `0300 0800 a001 0000` — chunk type `0x0003` (`RES_XML_TYPE`), headerSize 8, total size **416**, equal to the member's uncompressed size."

- "begins `0300 0800 a001 0000`": this is the first 8 bytes of `payload_first16_hex` (`03000800a001000001001c00c4000000`), re-derived from the bytes as well. The spaced 4-group form is a faithful rendering; the hex string carries no stated byte-count clause, so Q14's `2 × N` shape rule does not apply to it (consistent with the entry's own Q14 row at `:184`, which enumerates only counted hex).
- "chunk type `0x0003` (`RES_XML_TYPE`)" / "total size **416**": supported by the `axml_chunk_table` fact — `"xml_header_type": 3`, `"xml_total_size": 416`, and `"xml_total_size_equals_member": true` (the "equal to the member's uncompressed size" clause; the member's `uncompressed_size` is 416 in this very line).
- "headerSize 8": read from bytes 2-3 of the quoted hex (`08 00` → 8); the XML header chunk itself is not a row of the chunk table (which starts at offset 8), so this is the one number in the sentence that the two facts support only through the hex, not through a named field. It is still directly present in the printed bytes — not an unsupported statement.

**Verdict on the prose: nothing stated that the output (plus the named script lines and the sibling facts it cites) does not support.** The only looseness is presentational, and it is the safe direction: two intermediate operands are attributed to the script rather than claimed as printed fields.

## 5. Build state (does this re-derivation support C1's predicate as it stands?)

- The entry is committed and its worktree copy is clean: `git rev-parse HEAD:corpus/knowledge/round-69-apk-axml-byte-evidence.md` → `00402958f673fc55ed738664d60f2e543eb73129`; `git diff --stat HEAD -- corpus/knowledge/round-69-apk-axml-byte-evidence.md corpus/fixtures/apk-r65/` → empty. HEAD at read time `35e1258`.
- Claim surface frozen as declared: `corpus/fixtures/apk-r65/fixture.apk` sha256 `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` and `corpus/fixtures/apk-r65/readout.py` sha256 `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976` — both equal to the S041 header line's pins.
- Admission is still build state, not a flip: `corpus/README.md:34` keeps C05 at `uncovered` with the knowledge column `—` (only the retained rejected round-65 candidate is listed), and the entry declares `admission-status: candidate` at `:11`. So the C1 predicate's `K_ROW C05 status=held` / `C05_SINGLE_V4=yes` legs are still `no`, exactly as `reports/round-69/measure-before.log` records.

This item's evidence bears on the entry's item-3/item-4 derivation honesty (the ground Q11 and Q14 read), and it is a positive input to the C1 wave; it is not by itself an adjudication of those criteria and does not move the README row.

## 6. Risks / blockers

- **None blocking.** No missing artifact; the fixture, oracle, readout and entry were all present and hash-clean.
- Risk (informational, same class as the carried D5 drift items): the fact line's `payload_offset` is not recomputable from its own JSON alone (`name_length`/`extra_length` unprinted), so a future reader checking only the embedded line must open `readout.py:99-105`. No claim depends on the line being self-sufficient.
- Tool installs/updates this item: **none** (no `pacman`, no `uv`, no fetch; host pacman transactions remain paused, untouched).
- Scratch `/tmp/revenger-r69-item3/` removed before returning.
