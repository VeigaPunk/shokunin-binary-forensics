PASS — Q04: the readout is labeled manual where its constants are hand-transcribed (entry:11, entry:61), and the derivation script's credit is bounded to exactly the 20 stdout lines it prints (entry:153), a set that contains every S038 line number the entry states and nothing the command does not print.

# Q04 — fresh admission review of `corpus/knowledge/round-69-apk-axml-byte-evidence.md`

- criterion: **Q04** — "a tool claim names the tool, version and function exercised, and scores the tool's own explicit output; manual analysis is labeled manual; reject when a tool is credited with a result it did not output".
- entry under review: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-69-apk-axml-byte-evidence.md` (215 lines, `admission-status: candidate`)
- scoped to this criterion only; no file edited; no subagent dispatch; no package installed.

## 1. The manual label is present and is true against the code it points at

Entry:11 (Scope): "The analysis is **manual**: a Python standard-library script reads the archive's bytes with `struct` and walks the ZIP central directory…"

Entry:61 (item 5) states the widths are "**manually transcribed** in `readout.py:51-58` from S038's own struct field lists … — a manual transcription, labeled manual, not a runtime derivation; the readout merely prints the constants and the sums".

Pointer check, actual source:

```
$ python3 - … (repr of corpus/fixtures/apk-r65/readout.py:48-60)
48 '    # --- Spec-derived structure widths (S038 field lists) --------------------'
49 '    # Every fixed offset the readout uses is computed here from the field'
50 "    # widths in ResourceTypes.h's own struct definitions, not assumed."
51 '    w8, w16, w32 = 1, 2, 4'
52 '    widths = {'
53 '        "ResChunk_header": [w16, w16, w32],'
54 '        "ResStringPool_header": [w16, w16, w32, w32, w32, w32, w32, w32],'
55 '        "ResXMLTree_node": [w16, w16, w32, w32, w32],'
56 '        "ResXMLTree_attrExt": [w32, w32, w16, w16, w16, w16, w16, w16],'
57 '        "ResXMLTree_attribute": [w32, w32, w32, w16, w8, w8, w32],'
58 '        "Res_value": [w16, w8, w8, w32],'
59 '    }'
60 '    sizes = {name: sum(w) for name, w in widths.items()}'
```

The widths are integer literals in the script; nothing reads `ResourceTypes.h` at run time for them. The entry's "manual / not a runtime derivation" label is correct, and `51-58` is exactly the transcription block (width constants + six per-struct field lists; `}` at 59 and the `sizes` sum at 60 are not transcription). The readout does "merely print the constants and the sums" for this fact — `emit("spec_derived_struct_widths", …)` passes the literal dict and the sums.

The other cited script pointers also resolve exactly (all checked, not sampled):

| entry pointer | claim | actual line(s) |
|---|---|---|
| entry:37 `readout.py:99-105` | `payload_offset = local_header_offset + 30 + name_length + extra_length` | 99 `lh_name_len = u16(apk, lh_off + 26)`, 100 `lh_extra_len = u16(apk, lh_off + 28)`, 105 `payload_off = lh_off + 30 + lh_name_len + lh_extra_len` |
| entry:70 `readout.py:166` | UTF-8 test `flags & 0x100` | 166 `utf8=bool(flags & 0x100), sorted_flag=bool(flags & 0x1),` |
| entry:84 `readout.py:200-203` | attribute at `chunk_base + 16 + attributeStart + i*attributeSize` | 203 `aoff = base + 16 + attribute_start + i * attribute_size` (200-202 the S038 comment) |
| entry:91 `readout.py:22` | `0xffffffff` treated as null | 22 `NO_INDEX = 0xFFFFFFFF` |

## 2. The tool's own explicit output is what the entry scores — every embedded block re-runs verbatim

Independent re-run (my own extraction of every fenced block, one command segment per `$ ` line, `argv` list, no shell):

```
$ python3 -B corpus/derive_axml_anchors.py ; echo EXIT=$?
sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f ResourceTypes.h
struct ResChunk_header : 218
struct Res_value : 287
struct ResStringPool_header : 461
struct ResXMLTree_header : 612
struct ResXMLTree_node : 621
struct ResXMLTree_attrExt : 677
struct ResXMLTree_attribute : 707
enum block open : 237
enum RES_STRING_POOL_TYPE : 239 = 0x0001
enum RES_XML_TYPE : 241 = 0x0003
enum RES_XML_FIRST_CHUNK_TYPE : 244 = 0x0100
enum RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100
enum RES_XML_END_NAMESPACE_TYPE : 246 = 0x0101
enum RES_XML_START_ELEMENT_TYPE : 247 = 0x0102
enum RES_XML_END_ELEMENT_TYPE : 248 = 0x0103
enum RES_XML_RESOURCE_MAP_TYPE : 253 = 0x0180
enum block close : 263
comment attributeStart : 686
field attributeStart : 687
EXIT=0
```

```
$ python3 -B corpus/fixtures/apk-r65/readout.py > out ; echo EXIT=$?; wc -l out; sha256sum out
EXIT=0
15 out
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  out
```

Both match the entry's stated counts and digest (entry:9 `recheck:`; entry:190-196 §Reproduce: "Exit 0; 15 stdout lines; their SHA-256 is `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247`").

Block-by-block verbatim diff of the entry's embedded outputs against actual stdout:

```
command-segments=17 ok=17 bad=0
full-run block lines: 15 actual lines: 15 exact_equal: True
derivation block lines: 20 actual: 20 exact_equal: True
```

Cross-check with the registered embedded-output gate (independent implementation, self-test first):

```
$ python3 -B corpus/check_embedded_outputs.py --self-test
SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-69-apk-axml-byte-evidence.md
checked_blocks=17 problems=0
EXIT=0
```

Embedded-JSON census: 30 embedded JSON lines = 15 unique facts, each appearing twice (per-item block + §Reproduce full-stdout block) — no value appears only in prose. The entry's line 8 sentence "every output line below was captured from the named command's actual stdout at build time, never transcribed by hand" holds for all 17 segments.

Byte pins in the entry that I re-derived on the tree:

```
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py
74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa  corpus/derive_axml_anchors.py
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  corpus/fixtures/apk-r65/truth.json
```

## 3. The derivation credit is bounded to exactly the numbers its stdout prints (the v3 defect is gone)

Entry:153 (item 11): "The credit is bounded to exactly the numbers the command prints: the 20-line stdout below (1 digest line + 7 struct lines + 2 enum-block bound lines + 8 enum lines + 2 attributeStart lines) is the complete set of S038 line numbers this entry states".

Arithmetic and observed composition agree: 1+7+2+8+2 = 20, `wc -l` = 20, and the 20 lines have exactly that shape (1 `sha256`, 7 `struct`, `enum block open`/`enum block close`, 8 `enum … = 0x…`, `comment attributeStart`/`field attributeStart`).

Attack that would falsify the bound: any S038 line number stated in the entry but absent from those 20 lines. Enumeration of every line-number citation in the entry (grep for `line N`, `lines N`, `:NNN`):

```
1:line 218   1:line 287   1:line 461   1:line 612   1:lines 612   1:line 621   1:line 677
1:line 686   1:line 687   1:line 707   1:lines 237   1::237 1::239 1::241 1::244 1::245
1::246 1::247 1::248 1::253 1::263
8::244  59::237 59::239 59::241 59::244 59::245 59::246 59::247 59::248 59::253 59::263
59:lines 237   84:line 677   84:snapshot line 686   84:line 687   153::237 153::244 153::263 153:lines 237 162:lines 237
```

Distinct S038 numbers stated anywhere in the entry (header line 1, items 4, 8, 11): **218, 237, 239, 241, 244, 245, 246, 247, 248, 253, 263, 287, 461, 612, 621, 677, 686, 687, 707** — 19 numbers. Every one of them is a line of the printed stdout above; the 20th line is the snapshot digest. No S038 number is stated outside the printed set. (`:41`, `:42`, `:48` in the grep are the entry's own self-references to earlier drafts/entry lines, not S038 anchors.) So the v3 universal "every line" credit is replaced by a set that is provably equal to what the entry states and to what the command prints.

The set is also correct against the pinned snapshot bytes (not just self-consistent): snapshot lines 237-263 are the enum block `enum {` … `};` with `RES_STRING_POOL_TYPE` 239 = 0x0001, `RES_XML_TYPE` 241 = 0x0003, `RES_XML_FIRST_CHUNK_TYPE` 244 = 0x0100, `RES_XML_START_NAMESPACE_TYPE` 245 = 0x0100, `RES_XML_END_NAMESPACE_TYPE` 246 = 0x0101, `RES_XML_START_ELEMENT_TYPE` 247 = 0x0102, `RES_XML_END_ELEMENT_TYPE` 248 = 0x0103, `RES_XML_RESOURCE_MAP_TYPE` 253 = 0x0180; snapshot 686/687 are the `attributeStart` comment and `uint16_t attributeStart;`; 677/707 are the two attribute structs.

Guard claim in item 11 — "The script refuses to print a line it did not find (a missing or ambiguous symbol is exit 2)" — probed hermetically on a `/tmp` copy (the pinned digest patched in the copy so the symbol path is reached):

```
symbol-removed:   rc=2 stdout_lines=1 last='derive_axml_anchors: enum RES_XML_FIRST_CHUNK_TYPE: not found'
symbol-ambiguous: rc=2 stdout_lines=1 last='derive_axml_anchors: enum RES_XML_TYPE: ambiguous (2 hits at [241, 242])'
```

No anchor line is printed before the exit (`print("\n".join(out))` happens only after every `find_unique` has passed), so "refuses to print a line it did not find" is literally true. My scratch tree `/tmp/revenger-r69-q04-sym2` was removed.

## 4. Entry lines at issue (and why none fails Q04)

- **entry:11** — "The analysis is **manual**": present; true (manual `struct` walk, no producer, no network, no extraction).
- **entry:61** — item 5 manual label + `readout.py:51-58` locator: present, locator exact, code confirms literals.
- **entry:70, entry:37, entry:84, entry:91** — script-internal locators: exact.
- **entry:153** — bounded-credit sentence and the 20-line composition: exact match to observed stdout; no S038 number outside it.
- **entry:196** — "every line also appears in the per-item blocks above": verified; 15 unique facts, each twice.
- **entry:8** — "every output line below was captured from the named command's actual stdout … never transcribed by hand": verified by the 17/17 verbatim re-run.

Nothing in the entry credits a tool with a result it did not print, and no version/function is generalized to a product (the readout is scoped to one fixture; the derivation to one snapshot).

## 5. Residual observations (no Q04 fail; handed to the owning criteria)

1. **No interpreter version is named** — commands say `python3 -B`, and the two instruments are identified by script SHA-256 (`92e347…`, `74d4c0d9…`) rather than a version string. I read Q04's "version" clause at instrument-identity level, which the pins satisfy more strongly than a version number; a seat scoring Q05/Q13 should not assume the pins cover interpreter-version drift.
2. **The `= ?` sentinel is unguarded on the value column.** With an enum *value* stripped from the pinned snapshot copy, the script still exits 0 and prints 20 lines (probe `value-missing: rc=0 stdout_lines=20`). The entry's exit-2 sentence is scoped to symbols/lines, so this is not an over-claim; but a Q13 seat should note that the derivation's *value* guard is not demonstrated by the embedded run. In the real run the sentinel never appears: `derive_axml_anchors.py | grep -c '='` = 8, `grep -c '?'` = 0.
3. The embedded `axml_start_element` line is 890 characters and complete (no truncation ellipsis in the file: `len=890`, tail `…"offset": 272, "styleIndex": 0}`); any apparent `…` in a terminal read is the reader's 768-byte cut, not the entry's bytes.

## 6. Tooling

No install or upgrade was needed; every check used the pre-existing `python3` standard library. No mutating git/jj command was run. Scratch: `/tmp/revenger-r69-q04-*` (created and deleted; `sym`/`sym2` trees removed).
