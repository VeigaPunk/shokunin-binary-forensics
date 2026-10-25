MATCH — the entry's `jar_manifest` line (entry:120, and its duplicate in §Reproduce at entry:214) is byte-identical to the command's actual stdout: all four fields (`bytes`, `fact`, `first_line`, `section_count`) agree, exit 0. The item-10 prose sentence states nothing the output contradicts. Two low-severity prose/precision notes are recorded below; neither changes the fact.

# R68 Item 10 — independent re-derivation of the text-manifest fact

Seat: `L1Revenger68.R68Item10` (leaf, read-only). Entry reviewed: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-68-apk-axml-byte-evidence.md`
sha256 `107e2d7483e57e64476ead408f2eb793f41e3eea5e3c96407763eadca6dfea5b` (215 lines).
Lane root for every command: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.

## 1. Command actually run, actual stdout, exit code

Per the assignment, one run of the named command plus one run per member:

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact jar_manifest
{"bytes": 69, "fact": "jar_manifest", "first_line": "Manifest-Version: 1.0", "section_count": 1}
EXIT=0
```

stdout byte tail (`od -c`): `... r s i o n :   1 . 0 " ,   " s e c t i o n _ c o u n t " :   1 } \n` — a single line, single trailing LF, no stderr.

Members (assignment asks for these too):

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[AndroidManifest.xml]'
{"cd_index": 0, "compressed_size": 416, "crc32": "962d075f", "crc32_matches": true, "crc32_recomputed": "962d075f", "fact": "member[AndroidManifest.xml]", "local_header_offset": 0, "payload_first16_hex": "03000800a001000001001c00c4000000", "payload_offset": 49, "sha256": "73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4", "uncompressed_size": 416}
EXIT=0

$ python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[classes.dex]'
{"cd_index": 1, "compressed_size": 112, "crc32": "2635c82a", "crc32_matches": true, "crc32_recomputed": "2635c82a", "fact": "member[classes.dex]", "local_header_offset": 465, "payload_first16_hex": "6465780a30333500300c123da5fc7bea", "payload_offset": 506, "sha256": "57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2", "uncompressed_size": 112}
EXIT=0

$ python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[META-INF/MANIFEST.MF]'
{"cd_index": 2, "compressed_size": 69, "crc32": "e948d738", "crc32_matches": true, "crc32_recomputed": "e948d738", "fact": "member[META-INF/MANIFEST.MF]", "local_header_offset": 618, "payload_first16_hex": "4d616e69666573742d56657273696f6e", "payload_offset": 668, "sha256": "2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49", "uncompressed_size": 69}
EXIT=0
```

## 2. The entry's claiming block

- Prose sentence, item 10 — `corpus/knowledge/round-68-apk-axml-byte-evidence.md:116`:
  > `10. The `META-INF/MANIFEST.MF` payload is 69 bytes of ASCII whose first line is `Manifest-Version: 1.0` with one blank-line-separated section:`
- Command line — entry:119: `$ python3 -B corpus/fixtures/apk-r65/readout.py --fact jar_manifest`
- Embedded output line — **entry:120**:
  `{"bytes": 69, "fact": "jar_manifest", "first_line": "Manifest-Version: 1.0", "section_count": 1}`
- Second occurrence (full-run stdout in §Reproduce) — **entry:214**: same string.
- Supporting member line — entry:43 (`member[META-INF/MANIFEST.MF]`, the parent block at entry:46).

## 3. Field-by-field verdict

Byte comparison (`[ "$ACTUAL" = "$(sed -n '120p' …)" ]`, then `214p`): `BYTE_EQUAL_L120=yes`, `BYTE_EQUAL_L214=yes`.

| field | actual | entry:120 / entry:214 | verdict |
|---|---|---|---|
| `bytes` | `69` | `69` | MATCH |
| `fact` | `"jar_manifest"` | `"jar_manifest"` | MATCH |
| `first_line` | `"Manifest-Version: 1.0"` | `"Manifest-Version: 1.0"` | MATCH |
| `section_count` | `1` | `1` | MATCH |

No field differs; no field is missing or extra on either side. Key order also matches, so the line is a verbatim capture, not a re-serialisation.

Cross-fact consistency: `bytes: 69` equals `uncompressed_size: 69` from `member[META-INF/MANIFEST.MF]` (entry:43) and equals `build_recipe.members[…].bytes` for `META-INF/MANIFEST.MF` in `corpus/fixtures/apk-r65/truth.json`.

Whole-run cross-check (the recheck the entry's header claims):
```
$ python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/r68_item10_run.txt ; echo EXIT=$?
EXIT=0
$ wc -l < /tmp/r68_item10_run.txt     -> 15
$ sha256sum /tmp/r68_item10_run.txt   -> 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247
$ grep -n jar_manifest /tmp/r68_item10_run.txt
15:{"bytes": 69, "fact": "jar_manifest", "first_line": "Manifest-Version: 1.0", "section_count": 1}
```
15 lines and `507d79f8…dad247` match the entry's header `recheck:` claim exactly; the manifest fact is stdout line 15 and equals entry:214.

Script/fixture pins re-derived (so the printed line demonstrably comes from the pinned reader over the pinned fixture):
```
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py   (= entry hygiene pin)
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk   (= entry S041 / item 1)
```
Exhaustive embedded-output check I also ran (same script, all `--fact` blocks in the entry): **15 embedded blocks, 0 diffs** (L24, 31, 38, 40, 42, 53, 62, 71, 78, 85, 92, 99, 101, 110, 119).

## 4. Prose judgement — does entry:116 state anything the output does not support?

Sentence decomposed against the printed fields and against the bytes (raw member read, read-only, via `zipfile`):

1. "is 69 bytes" — supported: `bytes: 69` (and `uncompressed_size: 69`).
2. "of ASCII" — **true, but not fully printed by this block**. The reader only proves the first line ASCII (`readout.py:251` `jar.split(b"\r\n")[0].decode("ascii")`) plus the first 16 bytes via `member[...]`'s `payload_first16_hex`. The raw member is `b'Manifest-Version: 1.0\r\nCreated-By: revenger-r65 fixture generator\r\n\r\n'`, `all(c<128) == True` over all 69 bytes. So the qualifier is correct on the artifact; it is an evidence-scope gap, not a false statement. Note only — Q11 counts/offsets/identifiers/digests are all printed.
3. "whose first line is `Manifest-Version: 1.0`" — supported exactly (`first_line`).
4. "with one blank-line-separated section" — supported against the bytes (one `\r\n\r\n`, i.e. one main section terminated by a blank line). Caveat for a third party porting the fact: `section_count` is **not** a section count — `readout.py:252` computes `section_count=jar.count(b"\r\n\r\n")`, a blank-line *separator* count. Here both readings yield 1, so the prose is not contradicted; for any manifest with entry sections the field would report separators, not sections. This is an interpretive hazard in the field name, not a defect in this entry's sentence.
5. Omission, not overreach: the section's only other content is `Created-By: revenger-r65 fixture generator`. The prose says "whose first line is …" (true) and does not claim the manifest is one line, so nothing unsupported is asserted; a reader just learns less about the section than the bytes contain.

Verdict on the prose: **MATCH** — no statement in entry:116 exceeds the printed output; item 4's note is about the field's implementation semantics, item 2's about where the ASCII claim is evidenced.

## 5. Secondary findings (adjacent prose, same fact surface; not part of the field comparison)

- **F1 (prose precision, low).** entry:46 (inherited verbatim from `corpus/knowledge/round-67-apk-axml-byte-evidence.md:45`): "The `META-INF/MANIFEST.MF` payload begins `4d616e69666573742d` — ASCII `Manifest-`, the 16-byte prefix of `Manifest-Version: 1.0`". The quoted hex is a **9-byte** prefix (`bytes.fromhex('4d616e69666573742d').decode() == 'Manifest-'`, len 9); the 16-byte prefix is `4d616e69666573742d56657273696f6e` = `Manifest-Version` (len 16), which is exactly the `payload_first16_hex` printed at entry:43. The appositive therefore attaches the 16-byte length to a 9-byte string. The correct 16-byte value is present in the block above it and is what "the value above" refers to, so no wrong bytes are asserted — it is a dangling appositive an adjudicator should note. Fix is editorial (drop "the 16-byte prefix of `Manifest-Version: 1.0`" or move it to the 16-byte string).
- **F2 (verified-correct, recorded so it is not mistaken for a defect).** The same parenthetical's "the round-65 draft recorded a 15-byte `4d616e696673742d…` pair at its entry:41" is accurate: `corpus/knowledge/round-65-apk-axml-byte-evidence.md:41` prints `payload_first16_hex": "4d616e696673742d56657273696f6e"`, which is 30 hex chars = **15 bytes**, decoding to `Manifst-Version` (the 'e' of "Manifest" dropped). The r68 entry's "15-byte" label is correct and its own value is the correct 16-byte `Manifest-Version`.

## 6. Bounds compliance / retained evidence

- Wrote only this file. No repo file edited; the entry, `readout.py`, `truth.json`, `fixture.apk` all read-only; no git/jj command run; no writes outside `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-68/`.
- No tool installed or upgraded this seat (nothing needed; Python 3 stdlib sufficed) — nothing to record under the tooling directive.
- Retained evidence: the four command/stdout pairs in §1 (all exit 0), the byte-equality results `BYTE_EQUAL_L120=yes` / `BYTE_EQUAL_L214=yes`, the 15-block/0-diff sweep, the 15-line `507d79f8…dad247` whole-run hash, and the two script/fixture sha256 pins in §3. Entry sha256 `107e2d74…dfea5b` anchors the reviewed revision.
