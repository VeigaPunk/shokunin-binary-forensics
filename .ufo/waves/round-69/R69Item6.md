MATCH — `axml_string_pool` re-derivation exits 0 and is byte-identical to both embedded copies (entry:74, entry:207); every field agrees, and the entry:70 prose states nothing this output does not support (one value, "size 196", is sourced from the sibling chunk-table fact, not from this fact's own output).

# R69Item6 — per-item re-derivation: `axml_string_pool`

Scope: one frozen fact, re-derived from the lane repo only. No writes outside this report and `/tmp/revenger-r69-i6-*` (scratch deleted). No package installs, no mutating git, no subagents.

Axes. (a) fidelity — actual stdout vs the embedded line, byte level; (b) prose support — does entry:70 overstate; (c) instrument integrity — is the readout the pinned one. All three moved; no axis harmed.

## 1. Command and actual output

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_string_pool
{"fact": "axml_string_pool", "flags": "0x00000100", "offset": 8, "offsets": [0, 10, 55, 66, 76, 94, 108, 122, 126], "sorted_flag": false, "stringCount": 9, "strings": ["android", "http://schemas.android.com/apk/res/android", "manifest", "package", "com.example.r65", "versionCode", "versionName", "1", "1.0"], "stringsStart": 64, "styleCount": 0, "stylesStart": 0, "utf8": true}
exit=0
```

One stdout line, 379 bytes (with trailing newline), sha256 `541ea73e08660e503347a50b59b8a3309cf11ee04115368149cf6797ef32b802`. No stderr.

## 2. Embedded lines and byte diff

The entry carries this fact twice:

- `corpus/knowledge/round-69-apk-axml-byte-evidence.md:74` — the item 6 block; its command line is `entry:73` (`$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_string_pool`), exactly the command run.
- `corpus/knowledge/round-69-apk-axml-byte-evidence.md:207` — the same line again inside the §Reproduce full-stdout block (entry:201-211).

```
$ diff <actual stdout> <entry:74>  ->  (empty)  IDENTICAL
$ diff <actual stdout> <entry:207> ->  (empty)  IDENTICAL
```

Field-by-field (actual vs entry:74, entry:207 — all three strings are the same bytes):

| # | field | actual | entry:74 / :207 | verdict |
|---|---|---|---|---|
| 1 | `fact` | `"axml_string_pool"` | same | MATCH |
| 2 | `flags` | `"0x00000100"` | same | MATCH |
| 3 | `offset` | `8` | same | MATCH |
| 4 | `offsets` | `[0, 10, 55, 66, 76, 94, 108, 122, 126]` | same | MATCH |
| 5 | `sorted_flag` | `false` | same | MATCH |
| 6 | `stringCount` | `9` | same | MATCH |
| 7 | `strings` | 9-element list, `android` … `1.0` in that order | same | MATCH |
| 8 | `stringsStart` | `64` | same | MATCH |
| 9 | `styleCount` | `0` | same | MATCH |
| 10 | `stylesStart` | `0` | same | MATCH |
| 11 | `utf8` | `true` | same | MATCH |

Fields that differ: **none** (0 of 11). No whitespace, key-order or value-formatting drift either — the diff is empty, not just field-equal.

## 3. Prose judgement — entry:70

Full sentence: "The string-pool chunk (offset 8, size 196) declares **9** strings, **0** styles, flags **`0x00000100`** — bit `0x100` set, the UTF-8 flag position the readout tests (`flags & 0x100`, readout.py:166) — with string data starting 64 bytes into the chunk. The nine strings, decoded as length-prefixed UTF-8 from the offsets the pool states, are:"

Claim-by-claim against what the output (and the bytes) support:

| claim | support | verdict |
|---|---|---|
| chunk at offset 8 | `offset: 8` | supported |
| size 196 | **not in this fact's output**; from the `axml_chunk_table` fact, entry:54-56 (`{"headerSize": 28, "offset": 8, "size": 196, "type": 1}`), which I also reproduced in the full run | supported by cross-fact citation, not by this output |
| 9 strings | `stringCount: 9`, `strings` length 9 | supported |
| 0 styles | `styleCount: 0` (`stylesStart: 0` consistent) | supported |
| flags `0x00000100` | `flags: "0x00000100"` | supported |
| bit `0x100` set / UTF-8 flag position | `utf8: true`; readout.py:166 is `utf8=bool(flags & 0x100), sorted_flag=bool(flags & 0x1),` (exact line, exact expression); S038 defines `UTF8_FLAG = 1<<8` at `corpus/snapshots/ResourceTypes.h:480` | supported |
| "readout.py:166" pointer | line 166 verified verbatim | supported |
| string data starting 64 bytes into the chunk | `stringsStart: 64`; S038 field doc `// Index from header of the string data.` (ResourceTypes.h:484-485); chunk header starts at the chunk offset, so 64 from the header is 64 into the chunk; readout.py:154 computes `base = so + strings_start + rel` | supported |
| nine strings as length-prefixed UTF-8 from the stated offsets | `strings`/`offsets` in output; readout.py:155-161 reads a 2-byte prefix then decodes UTF-8; independently decoded from fixture bytes (below): prefixes `07 07` before `android`, u16len == u8len for all nine, 0x00 terminator each | supported |

Unsupported statements: **none**. Two scope notes, neither an overstatement:

1. "size 196" is the only number in the sentence not carried by this fact's own JSON; it is carried by the sibling `axml_chunk_table` block (entry:55-56) and by internal arithmetic: headerSize 28 + 4×stringCount 36 = 64 = `stringsStart`; and `stringsStart` 64 + last-string extent 132 (rel 126 + 2 prefix + 3 bytes + 1 terminator) = 196 = chunk size. Both equalities hold from the measured fields.
2. "length-prefixed UTF-8" describes the readout's code path (readout.py:157-161), which is what the sentence says it does; S038's struct comment documents the UTF-16 branch only (ResourceTypes.h:449-457), so the UTF-8 prefix layout is code-described, not spec-anchored — the sentence attributes it to the readout, so it is scoped correctly.

## 4. Independent byte check (not from the script's output)

Read `fixture.apk` directly (payload at file offset 49, AXML chunk at 8): `stringsStart` 64 → data at AXML 72 = file 121; first bytes `0707616e64726f696400` = `07 07 "android" 00`. All nine offsets decode to the same nine strings, each with `u16len == u8len` (ASCII), each terminated by `0x00`. `truth.json` `axml_declared.strings` is exactly the same nine-string list, so the oracle agrees (the entry's §Oracle claim at entry:157 holds for this fact).

## 5. Instrument integrity

- `corpus/fixtures/apk-r65/readout.py` sha256 `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976` — equals the S041 pin at entry:7 and the §Reproduce pin.
- `fixture.apk` `05d2280f…7d03e`, `truth.json` `27303bae…b4f8173`, `generator.py` `eaa9444c…930c27c1a` — all equal the entry:7 pins.
- `corpus/snapshots/ResourceTypes.h` sha256 `56b88bc4…8957c56f` — equals the S047/S038 pin (entry:1, entry:6); `UTF8_FLAG = 1<<8` at :480.
- Full run reproduced: `python3 -B corpus/fixtures/apk-r65/readout.py` → exit 0, 15 lines, sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — exactly the entry:9 `recheck:` digest, so the embedded full-stdout block is consistent with today's bytes, not just this one line.
- `git status --porcelain -- corpus/fixtures/apk-r65 corpus/knowledge/round-69-apk-axml-byte-evidence.md` → empty; HEAD `35e1258`; entry sha256 `c1e7eaac…deb11d5` equals `git show HEAD:…` byte-for-byte. Nothing in this tree is dirty.
- The readout opens only `Path(__file__).resolve().parent / "fixture.apk"` (readout.py:20-21) — no network, no extraction, no producer call in the fact path.

## 6. Q-map interaction

The entry's Q11 row (entry:182) says every count/offset/digest carries its deriving command and output. For this fact that holds: the JSON is embedded with its command at entry:73-74, and the only external number in the prose (196) is embedded with its own command at entry:54-56. Q04's "manual" label concerns item 5's struct widths and is untouched by this fact. No Q-map row is contradicted by this re-derivation.

## 7. Residual risk and verification gaps

- **Residual (low):** readout.py:157-159 reads a *single* byte for each of `u16len`/`u8len` and asserts `len(s) == u16len` (readout.py:161). That is valid only when the UTF-16 length equals the UTF-8 byte length and both are < 0x80 — true for all nine strings here (verified: every `u16len == u8len`, max 42), but it would mis-decode or assert on non-ASCII or ≥128-byte strings. The entry's §Limitations (entry:167) says "UTF-8 string pool only" but does not name this decoder restriction. The prose at entry:70 makes no generality claim, so this is an instrument-scope gap, not an unsupported statement.
- **Gap:** I did not perturb the fixture/README/entry to test that the fact would fail on drift (mutation is another seat's lane), and did not re-run `corpus/derive_axml_anchors.py` (outside this fact's scope; its sha matches the S047 pin, checked statically only).
- **Tooling note:** no `lsp` device is mounted in this seat, so caller/definition checks used `read`/`grep` as the literal fallback. This item is byte-level (a JSON line vs file bytes), so no symbol graph exists to resolve; grep was not used as semantic proof of anything but line presence in a markdown file.
- No tools installed or upgraded; pacman untouched.

Verdict: **MATCH** — 11/11 fields identical, both embedded copies byte-identical, prose fully supported with one cross-fact value correctly traceable to its own embedded command.
