# R68ReviewEntryQ04 — Q04 on `corpus/knowledge/round-68-apk-axml-byte-evidence.md`

FAIL — the manual-analysis leg and the output-scoring leg both pass, but item 11 credits `corpus/derive_axml_anchors.py` with printing **every** S038 line number the entry states (and says "no spec line number in this entry is transcribed by hand"), while `:237` and `:244` are stated and **not printed** by that script — Q04's reject clause "a tool is credited with a result it did not output". A second, same-class overstatement sits in item 5 (the struct widths are a hardcoded Python literal, never read from `ResourceTypes.h`, yet are presented as computed from S038's own struct definitions). Values themselves are correct; the credits are not.

Criterion under test: **Q04** — "A tool claim names the tool, version and function exercised, and scores the tool's own explicit output. Manual analysis is labeled as manual." Reject when "a tool is credited with a result it did not output, or one version/function is generalized to the product" (`corpus/QUALITY.md:20`).

Subject bytes: `corpus/knowledge/round-68-apk-axml-byte-evidence.md` (read in full; `admission-status: candidate`).
Frozen contract read first: `reports/round-68/claims.md` §C2 (candidate deltas 1-6, kill rule "Any Q FAIL on the v3 bytes … C2 is reported FALSIFIED").

---

## Evidence commands and their actual output (all run from `/home/vgpnk/Projects/shokunin/revenger-shokunin`)

### E1 — the derivation script's complete output (17 lines; no `:237`, no `:244`)

```
$ python3 -B corpus/derive_axml_anchors.py; echo EXIT=$?
sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f ResourceTypes.h
struct ResChunk_header : 218
struct Res_value : 287
struct ResStringPool_header : 461
struct ResXMLTree_header : 612
struct ResXMLTree_node : 621
struct ResXMLTree_attrExt : 677
struct ResXMLTree_attribute : 707
enum RES_STRING_POOL_TYPE : 239
enum RES_XML_TYPE : 241
enum RES_XML_START_NAMESPACE_TYPE : 245
enum RES_XML_END_NAMESPACE_TYPE : 246
enum RES_XML_START_ELEMENT_TYPE : 247
enum RES_XML_END_ELEMENT_TYPE : 248
enum RES_XML_RESOURCE_MAP_TYPE : 253
comment attributeStart : 686
field attributeStart : 687
EXIT=0
$ python3 -B corpus/derive_axml_anchors.py | wc -l
17
```

Filter for the two lines the entry states:

```
$ python3 -B corpus/derive_axml_anchors.py | awk 'NR<=2 || /: 237$|: 244$/'
sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f ResourceTypes.h
struct ResChunk_header : 218
```

**No `:237` line, no `:244` line.** The script's `ENUMS` tuple contains only the seven enum symbols the entry cites by name (`derive_axml_anchors.py:45-53`); `RES_XML_FIRST_CHUNK_TYPE` is not in it, and there is no block-extent derivation at all.

### E2 — the two stated line numbers, from the snapshot bytes (values are right)

```
$ sed -n '237p;238p;244p;245p;253p' corpus/snapshots/ResourceTypes.h
enum {
    RES_NULL_TYPE                     = 0x0000,
    RES_XML_FIRST_CHUNK_TYPE          = 0x0100,
    RES_XML_START_NAMESPACE_TYPE      = 0x0100,
    RES_XML_RESOURCE_MAP_TYPE         = 0x0180,
```

So `:237` = `enum {` and `:244` = `RES_XML_FIRST_CHUNK_TYPE` are **correct**, but the entry's recheck has never printed them. `grep -c RES_XML_FIRST_CHUNK_TYPE corpus/snapshots/ResourceTypes.h` = **2** (second hit at `:734`, `FIRST_CHUNK_CODE = RES_XML_FIRST_CHUNK_TYPE,`), so a naive "extend ENUMS" fix must disambiguate (the script's `find_unique` exits 2 on >1 hit; exercised below).

### E3 — the script's refused/ambiguous behavior is as the entry describes (this leg holds)

In-memory exercise of the committed `find_unique` (no file written):

```
$ python3 -B - <<'EOF'   # import corpus/derive_axml_anchors.py, feed it line lists
ENUMS: ('RES_STRING_POOL_TYPE', 'RES_XML_TYPE', 'RES_XML_START_NAMESPACE_TYPE', 'RES_XML_END_NAMESPACE_TYPE', 'RES_XML_START_ELEMENT_TYPE', 'RES_XML_END_ELEMENT_TYPE', 'RES_XML_RESOURCE_MAP_TYPE')
find_unique on RES_XML_FIRST_CHUNK_TYPE -> 244
derive_axml_anchors: X: ambiguous (2 hits at [1, 2])
ambiguous SystemExit 2
EOF
```

Confirms the entry's sentence "a missing or ambiguous symbol is exit 2" (`round-68-…:125`) — the mechanism exists; it just is not applied to `:237`/`:244`.

### E4 — the readout's own output is scored and reproduces exactly

```
$ python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/q04-readout.out; echo EXIT=$?
EXIT=0
$ wc -l /tmp/q04-readout.out
15
$ sha256sum /tmp/q04-readout.out
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247
```

Entry `recheck:` (`:7`) and §Reproduce (`:194`) state 15 lines with SHA-256 `507d79f8…dad247`. **Match, byte for byte.** Every per-item block (items 1-10) is the readout's own stdout, not prose paraphrase — spot-checked against `/tmp/q04-readout.out` for `archive`, `eocd`, the three `member[…]` rows, `axml_chunk_table`, `axml_string_pool`, `axml_resource_map`, `axml_start_element`, the two namespace facts, `axml_end_element`, `dex_declared_header`, `jar_manifest`.

### E5 — artifacts are the hashed bytes

```
$ sha256sum corpus/fixtures/apk-r65/readout.py corpus/fixtures/apk-r65/fixture.apk \
            corpus/snapshots/ResourceTypes.h corpus/derive_axml_anchors.py
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249  corpus/derive_axml_anchors.py
```

All four match the entry's header/§Reproduce pins.

### E6 — the width block is a hardcoded literal, and the "source anchor" in the output is a string literal

```
$ awk 'NR>=48 && NR<=63{printf "%d: %s\n", NR, $0}' corpus/fixtures/apk-r65/readout.py
48:     # --- Spec-derived structure widths (S038 field lists) --------------------
49:     # Every fixed offset the readout uses is computed here from the field
50:     # widths in ResourceTypes.h's own struct definitions, not assumed.
51:     w8, w16, w32 = 1, 2, 4
52:     widths = {
53:         "ResChunk_header": [w16, w16, w32],
54:         "ResStringPool_header": [w16, w16, w32, w32, w32, w32, w32, w32],
55:         "ResXMLTree_node": [w16, w16, w32, w32, w32],
56:         "ResXMLTree_attrExt": [w32, w32, w16, w16, w16, w16, w16, w16],
57:         "ResXMLTree_attribute": [w32, w32, w32, w16, w8, w8, w32],
58:         "Res_value": [w16, w8, w8, w32],
59:     }
60:     sizes = {name: sum(w) for name, w in widths.items()}
61:     emit("spec_derived_struct_widths",
62:          source_anchor="S038 ResourceTypes.h struct field lists",
63:          bytes_per_field={k: v for k, v in widths.items()},
...
$ grep -n "ResourceTypes\|snapshots" corpus/fixtures/apk-r65/readout.py
50:    # widths in ResourceTypes.h's own struct definitions, not assumed.
62:         source_anchor="S038 ResourceTypes.h struct field lists",
126:    # (S038 ResourceTypes.h struct ResChunk_header field list). The root
```

`readout.py` **never opens** `ResourceTypes.h` (its three hits are a comment, a literal `source_anchor` value, and a comment). The field-width lists are transcribed by hand; only `sum()` is executed.

### E7 — no interpreter version anywhere in the entry

```
$ grep -n "Python 3\|python3\.[0-9]\|CPython\|3\.14" corpus/knowledge/round-68-apk-axml-byte-evidence.md
(no match)
$ python3 --version
Python 3.14.8
```

Every digest/checksum in items 1-10 comes from `hashlib.sha256` / `hashlib.sha1` / `zlib.crc32` / `zlib.adler32` (`readout.py:46,115-117,241-245`) under `python3`, whose version the entry never names.

### E8 — cited function-level line references are accurate (this leg passes)

```
$ grep -n "0x100\|NO_INDEX\|payload_off = lh_off" corpus/fixtures/apk-r65/readout.py
22:NO_INDEX = 0xFFFFFFFF
105:        payload_off = lh_off + 30 + lh_name_len + lh_extra_len
166:         utf8=bool(flags & 0x100), sorted_flag=bool(flags & 0x1),
```

Entry cites `readout.py:99-105` for the payload-offset derivation, `readout.py:166` for `flags & 0x100`, `readout.py:22` for the `0xffffffff` → null treatment — each resolves to the named function.

---

## Findings, by severity

### F1 (blocking, Q04) — item 11 credits the derivation script with printing line numbers it does not print

Entry line **`:125`** (item 11 opening sentence), verbatim:

> "11. Every S038 line number this entry states is printed by a committed derivation script that searches the pinned snapshot bytes for each cited symbol — no spec line number in this entry is transcribed by hand."

Stated S038 line numbers in the entry and whether E1 prints them:

| stated | where stated | printed by `derive_axml_anchors.py`? |
|---|---|---|
| `:218` | `:1`, `:148` | yes (line 2) |
| **`:237`** | `:1` ("lines 237-253"), `:57`, `:148`, `:157` | **no** |
| `:239` `:241` `:245` `:246` `:247` `:248` `:253` | `:1`, `:57`, `:148` | yes |
| **`:244`** | `:148` ("line 244 is `RES_XML_FIRST_CHUNK_TYPE`") | **no** |
| `:677` `:686` `:687` | `:8` | yes |

The values of `:237` and `:244` are correct (E2), so this is not a wrong number; it is the **credit** that is false — exactly Q04's reject trigger, and precisely the M40/M44 failure mode the entry claims to have made "mechanical" (`:148`). The one line that discriminates the r67 off-by-one (`:244`) is the one the "capture" does not print, so a future snapshot shift would leave `:244` unguarded while `:245` stays symbol-derived.

Correct value / fix (either, both are two-line changes):
- (a) extend `corpus/derive_axml_anchors.py` to also emit `enum RES_XML_FIRST_CHUNK_TYPE : 244` (disambiguated — the token occurs twice, E2/E3) and an `enum-block-open RES_NULL_TYPE : 238`/`enum {` derivation, and update the expected count from **17 → 19 lines** in `:125`, `:191-194` and the S046 row; or
- (b) narrow `:125` to "every cited *symbol*'s line number" and mark `:237`/`:244` as **recorded from the snapshot** (manual), deleting "no spec line number in this entry is transcribed by hand". Then `:1`, `:57`, `:148`, `:157` need the same qualifier.

### F2 (blocking, same class, Q04) — item 5 presents hand-transcribed struct widths as computed from S038 by the command

Entry line **`:59`** (item 5 sentence, block at `:61-63`) says the widths are "computed by summing the field widths of S038's own struct definitions … not assumed", followed by the `spec_derived_struct_widths` block whose `source_anchor` field reads `"S038 ResourceTypes.h struct field lists"`. E6: the lists are a Python literal (`readout.py:52-59`), the `source_anchor` value is a string literal (`:62`), and the readout never reads `ResourceTypes.h`. The S038→width mapping is **manual transcription and is not labeled manual**, while the tool's output is credited with establishing it. Q04's clause "manual analysis is labeled as manual" is violated for this step.

Correct value / fix: state it as "the field-width lists are transcribed from S038 (manual; `readout.py:52-59`); the command sums them", or drop `source_anchor` from being evidence and label the mapping manual. Note the genuinely machine-independent corroboration that already exists and should carry the claim: the derived sizes are compared to the observed `headerSize` column from the fixture bytes (`:57`; `28, 8, 16, 16, 16, 16`), which is a real two-source agreement.

### F3 (minor, Q04) — no interpreter version is named for the tool whose output every digest rests on

The only interpreter named is `python3` (`:7`, `:13`, `:191`), and "runs with the Python standard library only" (`:156`) is a tool-scope claim with no version (E7). Q04's first clause asks a tool claim to name "the tool, version and function exercised". Weakest of the three findings — the corpus's admitted precedents (`round-64-firmware-region-byte-evidence.md:212`, `round-62-evm-dispatch-byte-evidence.md:220`) pass Q04 with a stdlib reader and no Python version — so on precedent alone this would not force a FAIL, but the v3 bytes are the place to fix it: record `CPython 3.14.8` (E7, the interpreter that reproduced the pinned stdout hash) in `verified-at:` and name the exercised functions (`struct.unpack_from`, `hashlib.sha256/sha1`, `zlib.crc32/adler32`).

### F4 (Q-map accuracy, supports F1) — the entry's own Q04 row misdescribes its tool surface

Entry **`:175`**: "| Q04 | pass | no tool claim: the readout is manual standard-library byte analysis, labeled manual; the only tool named is Python itself, used as the reader, not credited with a result. |". Not evidence for my decision (per brief), but it is contradicted by the entry's own bytes: item 11 does make a tool claim about `derive_axml_anchors.py`, and items 1-10 credit the readout with every value in the entry. The row must be rewritten to name both scripts and the credit scope, not to assert "no tool claim".

---

## What passes on Q04 and should not be disturbed

- **Manual labeling is explicit and repeated**: `:13` "The analysis is **manual**: a Python standard-library script reads the archive's bytes with `struct` …"; `:156` "every value in items 1-10: read directly from the committed bytes by the §Reproduce script, which runs with the Python standard library only"; `readout.py:2` docstring "Manual byte-derived readout of the round-65 APK fixture."
- **The tool's own explicit output is scored, and the score reproduces** (E4): 15 lines, exit 0, stdout SHA-256 `507d79f8…dad247` — identical to `:7`/`:194`, and every embedded block is that stdout.
- **No third-party tool is credited** anywhere (no `inspect_android_package`, no jadx, no apktool, no provider record); the §Cross-lane scope note (`:164-166`) fences the provider route to S043 documentation scope.
- **No generalization of one version/function to the product**: `:160-162` (§Limitations) scopes everything to this one fixture and declares the dex member "intentionally not a valid dex program".
- **Function-level citations resolve** (E8): `readout.py:22`, `:99-105`, `:166`.

## Residual risk and verification gaps

- I did not mutate `corpus/derive_axml_anchors.py` or the snapshot (lane bounds); F1's fix is described, not applied. The `:237`/`:244` derivations were only tested **in memory** (E3) via the committed `find_unique`, which is why I can say the fix is small and the ambiguity rule already fires.
- `truth.json` was not opened for this criterion (it is the oracle under Q03/Q06); nothing in Q04 turns on it.
- Only one interpreter (`Python 3.14.8`) was exercised; the pinned stdout hash could in principle be interpreter-specific, which is exactly F3's gap — the entry does not record which interpreter it used.
- No writes outside this report; no git/jj mutation; no tool installs or upgrades were needed, so there is nothing to record under the tooling directive.

Report path: `.ufo/waves/round-68/R68ReviewEntryQ04.md` (this file).
