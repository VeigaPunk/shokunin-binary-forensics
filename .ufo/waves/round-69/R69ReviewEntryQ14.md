FAIL — Q14: entry line 48 puts a byte count on an ellipsis-truncated hex run ("a 15-byte `4d616e696673742d…` pair": 16 hex chars shown, not 2×15=30) and labels the command's 32-hex-character (16-byte) `payload_first16_hex` as "the correct 9-byte pair"; the leading `(9 bytes)`/ASCII `Manifest-` clause is correct and every other hex/count clause in the entry passes.

# Q14 review — round-69 C05 v4 candidate

- criterion: **Q14** (`corpus/QUALITY.md:31`) — a hex string quoted with a byte count in the same clause carries `2 × N` hex characters; an ellipsis-truncated run carries no length; an `ASCII \`…\`` rendering decodes from that same run.
- object under test: `corpus/knowledge/round-69-apk-axml-byte-evidence.md`, 215 lines, sha256 `c1e7eaac9dba4c77e578c788755dec3e3499fd8795ad0e479c51b5be7deb11d5`, `admission-status: candidate`.
- scope: Q14 only, sweep of every hex/count clause in the entry, including the `MANIFEST.MF` clause (line 48) and item 11's hex values (item-11 block, lines 131-150).
- lane writes: this file only. Scratch under `/tmp/revenger-r69-q14-*`, deleted before return. No tool installed; no package touched.

## Verdict

**FAIL**, on line 48 only. One unambiguous violation (a byte count on an ellipsis-truncated run, defect 1) plus a second count in the same sentence that is wrong under the entry's own use of "pair" (defect 2, contestable on a charitable reading); every other hex/count clause in the entry passes.

### Entry line 48, verbatim

```
The `META-INF/MANIFEST.MF` payload begins `4d616e69666573742d` — ASCII `Manifest-` (9 bytes), the first nine bytes of `Manifest-Version: 1.0` (the round-65 draft recorded a 15-byte `4d616e696673742d…` pair at its entry:41; the deriving command prints the correct 9-byte pair above).
```

### Defect 1 — length attached to an ellipsis-truncated run

Text: ``a 15-byte `4d616e696673742d…` pair``.

- The run as quoted is `4d616e696673742d` + `…` = 16 hex characters = 8 bytes. `2 × 15 = 30` hex characters are not present; Q14's second limb is explicit that an ellipsis-truncated run **carries no length**, so the `15-byte` label is forbidden independently of arithmetic.
- The `15` is a true byte count only for the *untruncated* draft value `4d616e696673742d56657273696f6e` (30 hex chars = 15 bytes), which the entry does not quote in this clause. That is the smallest safe correction (below) — either quote that run in full and keep 15, or drop the length and keep the truncation.

Command and output (re-derived from the lane's own bytes):

```
$ python3 - <<'EOF'
for h in ["4d616e69666573742d","4d616e696673742d","4d616e696673742d56657273696f6e","4d616e69666573742d56657273696f6e"]:
    b=bytes.fromhex(h); print(f"{h!r:40} hexchars={len(h):3} bytes={len(b):3} ascii={b!r}")
EOF
'4d616e69666573742d'                     hexchars= 18 bytes=  9 ascii=b'Manifest-'
'4d616e696673742d'                       hexchars= 16 bytes=  8 ascii=b'Manifst-'
'4d616e696673742d56657273696f6e'         hexchars= 30 bytes= 15 ascii=b'Manifst-Version'
'4d616e69666573742d56657273696f6e'       hexchars= 32 bytes= 16 ascii=b'Manifest-Version'
```

Retained round-65 draft bytes the sentence refers to (`corpus/knowledge/round-65-apk-axml-byte-evidence.md:41`, read-only, byte-preserved):

```
$ sed -n '41p' corpus/knowledge/round-65-apk-axml-byte-evidence.md | python3 -c "..."
draft run: 4d616e696673742d56657273696f6e hexchars= 30 bytes= 15 ascii= b'Manifst-Version'
```

So the historical byte count 15 is correct for the *full* draft run and 8 is correct for the *truncated* run quoted in line 48; the clause states one against the other.

### Defect 2 — `9-byte` stated for the 16-byte printed run

Text: ``the deriving command prints the correct 9-byte pair above``.

The value "above" is the printed `payload_first16_hex` of the `member[META-INF/MANIFEST.MF]` fact, `4d616e69666573742d56657273696f6e` — 32 hex characters = **16 bytes**, `b'Manifest-Version'`. `9 bytes` is the length of the 18-hex-character prefix only, not of the run the command prints. The round-67/round-68 v3 wording this line descends from said "the 16-byte pair" (`corpus/knowledge/round-68-apk-axml-byte-evidence.md:46`); the v4 edit replaced the correct count with an incorrect one, so the Q14 repair of this clause is not complete — the leading `(9 bytes)` was fixed and the trailing count was newly broken.

Honest caveat on this second defect: a charitable reading takes "the 9-byte pair" to name the `4d616e69666573742d` run quoted at the start of the same line (18 hex = 9 bytes, correct), of which the printed value is the 16-byte continuation. Under the entry's own prior usage ("the deriving command prints the 16-byte pair, which is the value above", r68 line 46) "pair" denotes the printed `payload_first16_hex`, so the count is wrong as written and the sentence needs the same fix either way. The FAIL does **not** rest on this leg: defect 1 above is unambiguous under Q14's truncation limb and stands alone. If an adjudicator reads "9-byte pair" charitably, it still fails on defect 1 and must still be reworded so no count sits beside a truncated run.

Command and output (the entry's own command):

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[META-INF/MANIFEST.MF]'
{"cd_index": 2, "compressed_size": 69, "crc32": "e948d738", "crc32_matches": true, "crc32_recomputed": "e948d738", "fact": "member[META-INF/MANIFEST.MF]", "local_header_offset": 618, "payload_first16_hex": "4d616e69666573742d56657273696f6e", "payload_offset": 668, "sha256": "2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49", "uncompressed_size": 69}
exit=0
```

Fixture bytes at that offset (independent of the script):

```
$ python3 -c "d=open('corpus/fixtures/apk-r65/fixture.apk','rb').read(); print(d[668:684].hex(), d[668:684])"
4d616e69666573742d56657273696f6e b'Manifest-Version'
```

No command in the entry prints `9 bytes` or `15-byte`; both are hand-written, and the `Readout.py --fact` form prints only `payload_first16_hex` (16 bytes). Under the assignment's rule that a value the named command does not print fails the criterion that carries it, line 48 fails Q14 on both counts.

### What does pass in line 48

The leading clause is Q14-correct and I re-derived it: `4d616e69666573742d` = 18 hex chars = 9 bytes, ASCII `Manifest-` decodes from that same run, and it is the first nine bytes of `Manifest-Version: 1.0` (`python3 -c "print(bytes.fromhex('4d616e69666573742d')[:9])"` → `b'Manifest-'`).

## Rest of the entry — sweep result

Every other hex/count clause is Q14-consistent, checked by re-running the entry's own commands and by hex arithmetic:

| entry line | clause | hex chars | bytes | verdict |
|---|---|---|---|---|
| 7, 23 | `947 bytes` + sha256 (the count binds the file's size, not the digest's length) | 64 | file 947 | pass |
| 30 | `` `504b0506` `` at offset 925 — no byte count in clause | 8 | 4 | pass (exempt: no count stated) |
| 52 | `` `0300 0800 a001 0000` `` — no count on the run (`headerSize 8` is the field) | 16 | 8 | pass |
| 109 | `` first eight bytes are `6465780a30333500` ``, ASCII `dex\n035\0` | 16 | 8 | pass (decodes: `b'dex\n035\x00'`) |
| 109 / 113 | 20-byte signature, printed `a5fc7bea…9fce` | 40 | 20 | pass |
| 131-150 (item 11) | enum values `0x0001 0x0003 0x0100 0x0101 0x0102 0x0103 0x0180`, line numbers, one sha256 | — | — | pass (no count clause attached to a hex run) |
| 3, 109 | `0x70 (112) bytes` (S045 quote) | — | — | pass (`0x70` = 112, decimal equivalence, not a run length) |

Item 11's hex values are consistent with the fixture: chunk types printed decimal at line 56 (`1, 384, 256, 258, 259, 257`) equal the enum hex in item 11 (`0x0001, 0x0180, 0x0100, 0x0102, 0x0103, 0x0101`). The embedded item-11 block is byte-identical to live stdout:

```
$ python3 -B corpus/derive_axml_anchors.py | wc -l
20
$ diff <(sed -n '131,150p' corpus/knowledge/round-69-apk-axml-byte-evidence.md) <(python3 -B corpus/derive_axml_anchors.py)
(no differences; exit 0)
```

Hashes re-derived at review time, all matching the entry's header:

```
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py
74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa  corpus/derive_axml_anchors.py
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
$ python3 -B corpus/fixtures/apk-r65/readout.py | sha256sum
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  -
exit=0, 15 stdout lines (entry line 9's recheck value reproduces)
```

## Note on the entry's own Q-map (not used as evidence)

`corpus/knowledge/round-69-apk-axml-byte-evidence.md:184` says Q14 pass and asserts "the ellipsis-truncated run `4d616e696673742d…` carries no length" — line 48 in the same file gives that run a length (`15-byte`). The row describes a property the entry's bytes lack; it is a false self-report about Q14 and should be corrected together with line 48. (Flagged for the Q11 seat as a possible `presented-as-derived` issue; not my verdict, and I did not score from the row.)

## Impacted axes

- **coverage (C1)** — direct. `reports/round-69/claims.md` §C1 pass branch requires that *every applicable Q01–Q15 decision of the wave on the landed v4 bytes is PASS*; the §C1 kill rule reads "Any Q FAIL on the v4 bytes … → the C05 row stays `uncovered`, the v4 entry is marked `admission-status: rejected` …, and C1 is reported FALSIFIED". This FAIL is on the landed v4 bytes, so if sustained at adjudication C1 cannot reach `K_HELD_BACKED=9/14`.
- **calibration (C2)** — none. Q14 is a coverage criterion; Q15 and its restatement are untouched by this finding.
- No claim/void-condition effect beyond §C1: no fixture, live, README, denominator or Q01–Q15 weakening is involved in the correction.

## Smallest safe correction (line 48 only)

Replace the parenthetical so every count is the bytes of the run it sits beside, and no truncated run carries a length:

```
The `META-INF/MANIFEST.MF` payload begins `4d616e69666573742d` — ASCII `Manifest-` (9 bytes), the first nine bytes of `Manifest-Version: 1.0` (the round-65 draft recorded `4d616e696673742d56657273696f6e` — 30 hex characters, 15 bytes, ASCII `Manifst-Version` — at its entry:41; the deriving command prints `4d616e69666573742d56657273696f6e`, 32 hex characters, 16 bytes, ASCII `Manifest-Version`, the value above).
```

This keeps the M39 provenance point (the draft's run was one byte short, `b'Manifst-Version'`), removes the length from the truncated run, and states 16 bytes for the printed run. It changes no other sentence and no value in items 1-11.

### Constraint confirmed with the Q11 seat — prose only, no fixture/readout change

`reports/round-69/claims.md:185` voids the round on "Changed `corpus/live` or `corpus/fixtures` bytes", and `corpus/fixtures/apk-r65/readout.py` lives under that path: no `--fact` output may be re-emitted, no fact field added, and the pinned stdout digest `507d79f8…` / 15-line count must not move. Both Q14 repairs above are entry prose only — they quote values already present in the entry (line 45's printed run) or in the retained round-65 record (`corpus/knowledge/round-65-apk-axml-byte-evidence.md:41`, re-readable with `sed -n '41p'`), and touch no tool. A stricter, hex-free variant that creates no new derivation obligation is also Q14-clean and is the preferred wording if the sentence should quote no historical run at all:

```
The `META-INF/MANIFEST.MF` payload begins `4d616e69666573742d` — ASCII `Manifest-` (9 bytes), the first nine bytes of `Manifest-Version: 1.0`; the round-65 draft's recorded prefix at its entry:41 was one byte short of the 16 bytes (32 hex characters) that `payload_first16_hex` prints above.
```

Here no hex run carries a count: the only byte counts (`9 bytes`, `16 bytes`) sit beside the run whose hex is quoted in the same sentence and beside the printed run identified by field name and character count, and the truncation disappears entirely. It deletes the `9-byte pair` phrase as well, so defect 2 is repaired by the same edit.

## Counterexample test performed

The strongest available counterexample to this FAIL is "the count describes the historical draft, not the quoted run". It does not survive: (a) Q14's text forbids a length on any ellipsis-truncated run unconditionally, so the clause is non-compliant however the number was intended; (b) `corpus/knowledge/round-68-apk-axml-byte-evidence.md:46` was rejected on this same clause by this same criterion (`QUALITY.md:31` reject example cites "r68 v3 entry line 46"), so the class is settled and v4 re-opens it with a truncated run carrying a count; (c) the printed value the clause points at, `payload_first16_hex` at line 45, is 32 hex characters, so the historical count cannot be read off the quoted characters either (`2 × 15 = 30 ≠ 16`).

Converged fact with the Q11 seat: r65 entry:41 does decode to exactly 15 bytes (`b'Manifst-Version'`), so `15` is a true statement about the draft's record and my Q14 objection is **not** that the number is false — it is that Q14's truncation limb tests the shape of the clause, not the truth of the underlying fact, and a truncated run cannot evidence 15. That is why the repair keeps the 15-byte fact and moves the count onto an untruncated run or a hex-free sentence. Q11 does not rest on line 48 and my FAIL does not rest on Q11's legs (entry:30, entry:37, entry:157); the two findings are disjoint and one prose edit pass on the entry absorbs both without touching `corpus/fixtures`.
