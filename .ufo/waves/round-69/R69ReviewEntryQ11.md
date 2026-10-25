FAIL — Q11 — the v3's headline defect (underived enum lines/values) is genuinely repaired, but four residual constructs still carry a value with no in-entry derivation and no "recorded" label: `504b0506` (entry:30), the `46-byte`/`30-byte` ZIP fixed widths (entry:37), the oracle-agreement sentence (entry:157) for which no comparison command exists, and four file digests that no command prints (entry:6-7, readout.py's repeated at :19/:194); the Q11 row's universal claim at entry:182 is therefore false on the entry's own bytes. Every value is numerically correct.

Reviewer: `L1Revenger69.R69ReviewEntryQ11` (fresh seat, not the author). Criterion only: Q11 (`corpus/QUALITY.md:24` — "Each count, identifier, offset and digest in an entry carries, inside the entry, the command that derives it from the primary record (bytes, saved tool output) and that command's output. Constants such as header offsets are derived, not assumed. A value cited only to prose is labeled recorded, not re-derived."). Subject bytes: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-69-apk-axml-byte-evidence.md` (216 lines, `admission-status: candidate`). No file edited; only this report and `/tmp/revenger-r69-*` scratch were written (scratch deleted).

## 1. What reproduces exactly (the bulk of Q11 is strong)

All commands run from `/home/vgpnk/Projects/shokunin/revenger-shokunin`.

```
$ python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/revenger-r69-q11-full.txt; echo exit=$?
exit=0
$ wc -l < /tmp/revenger-r69-q11-full.txt
15
$ sha256sum /tmp/revenger-r69-q11-full.txt
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  /tmp/revenger-r69-q11-full.txt
```
== entry:9 `recheck:` and entry:194 ("Exit 0; 15 stdout lines; … `507d79f8…`").

```
$ python3 -B corpus/derive_axml_anchors.py > /tmp/revenger-r69-q11-anchors.txt; echo exit=$?; wc -l < /tmp/revenger-r69-q11-anchors.txt
exit=0
20
$ sha256sum corpus/derive_axml_anchors.py corpus/snapshots/ResourceTypes.h corpus/fixtures/apk-r65/readout.py corpus/fixtures/apk-r65/fixture.apk corpus/fixtures/apk-r65/truth.json corpus/fixtures/apk-r65/generator.py
74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa  corpus/derive_axml_anchors.py
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  corpus/fixtures/apk-r65/truth.json
eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a  corpus/fixtures/apk-r65/generator.py
```
Every digest equals the entry's pin (entry:1-9; S041/S047 rows).

**Verbatim-embedding check, mechanical (not eyeballed):**

```
embedded per-item blocks vs `--fact <id>` stdout:  15/15 EXACT, 0 mismatch
embedded full-stdout block (entry:200-214) vs captured stdout: 15/15 EXACT, 0 mismatch
embedded item-11 derivation block (entry:131-150) vs captured stdout: 20/20 EXACT, 0 mismatch
```
So the entry's `verified-at` claim ("every output line below was captured from the named command's actual stdout at build time, never transcribed by hand") is true for all 50 embedded output lines. The registered M39 gate agrees and is clean on these bytes today:

```
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-69-apk-axml-byte-evidence.md
checked_blocks=17 problems=0
GATE_EXIT=0
```
17 blocks = 15 per-item + the full-stdout block + the derivation block, consistent with the 50 embedded lines counted above.

**Anchor derivation is a real derivation, not a hardcoded table** (this is the v3 repair that had to be checked, not trusted): `derive_axml_anchors.py:66` `VALUE_RE = re.compile(r"=\s*(0x[0-9a-fA-F]+)\s*,")`, applied at `:122-124` to `lines[line-1]` found by `find_unique` (`:74-80`, exit 2 on 0 or >1 hits, `:69-71`). The printed enum values are parsed out of the snapshot line. Independent confirmation of every printed anchor against the primary record:

```
$ sed -n '677p;686p;687p;218p;237p;263p;244p;245p;253p' corpus/snapshots/ResourceTypes.h   # sed prints in file order
struct ResChunk_header
enum {
    RES_XML_FIRST_CHUNK_TYPE          = 0x0100,
    RES_XML_START_NAMESPACE_TYPE      = 0x0100,
    RES_XML_RESOURCE_MAP_TYPE         = 0x0180,
};
struct ResXMLTree_attrExt
    // Byte offset from the start of this structure where the attributes start.
    uint16_t attributeStart;
```
`grep -n '^struct …'` likewise returns 218, 287, 461, 612, 621, 677, 707. The 20-line composition claim (1 digest + 7 struct + 2 block bounds + 8 enum + 2 attributeStart = 20) matches the actual stdout line-for-line.

`readout.py` file:line pointers cited by the entry also verify exactly: `:22` = `NO_INDEX = 0xFFFFFFFF`; `:51-58` = the six `widths` lists (the entry labels this **manual**, entry:60-62 — correct and honest); `:99-105` = `lh_name_len`/`lh_extra_len` and `payload_off = lh_off + 30 + lh_name_len + lh_extra_len`; `:166` = `utf8=bool(flags & 0x100)`. S043's snapshot checks out too: line 5 = `older server.`, lines 7-8 = the quoted `inspect_android_package` sentence, sha256 `412d9cb4…`, and r65 entry:41 does record `4d616e696673742d56657273696f6e`, so entry:48's historical *record* claim is accurate. Length check (so this does not collide with the Q14 seat's separate FAIL on line 48): the r65:41 run is 30 hex chars = 15 bytes = `b'Manifst-Version'`; the v4 printed `payload_first16_hex` is 32 hex chars = 16 bytes = `b'Manifest-Version'` — the draft's prefix is one byte short of the printed 16, and Q14's objection (a "15-byte" label on an ellipsis-truncated run, plus "9-byte pair" for a 32-hex-char field) is a length-attribution defect, not a derivation defect, so it is not Q11's ground.

## 2. The Q11 failure — four residual underived constructs

All four are **numerically correct**; each is exactly Q11's reject shape ("a value is correct when re-derived but the entry carries no derivation, or a recorded value is presented as re-derived"), and none is labeled `recorded`. They are not new: `diff -u` of v3 vs v4 (9 hunks, lines 1-12, 43-49, 54-62, 72-78, 86-92, 122-128, 134-151, 153-160, 169-197) shows entry:30, entry:37 and entry:157 fall **outside every changed hunk** — the v4 repair set did not touch them; the digest leg (e) survives the same way at :19 (lines 15-44 are in no hunk) and reappears in the reworked :7/:194 text.

**(a) entry:30 — `504b0506` has no deriving output.**

> `2. The end-of-central-directory signature \`504b0506\` is located at file offset **925**; …`

The named command prints the offset and counts, never the signature bytes:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact eocd
{"cd_end_equals_eocd_offset": true, "eocd_offset": 925, "fact": "eocd", "offset_of_start_of_cd": 737, "parsed_entries": 3, "size_of_central_directory": 188, "total_entries_cd": 3}
```
No `signature_hex`/`payload_first*` field exists in that fact; `readout.py:76-77` holds the literal `sig_eocd = b"PK\x05\x06"` and `eocd = apk.rfind(sig_eocd)`, i.e. the constant is the *search key*, not a derived value. Correct value (independently checked): `504b0506` —
```
$ python3 -c "d=open('corpus/fixtures/apk-r65/fixture.apk','rb').read(); print(d[925:929].hex())"
504b0506
```
but the reader cannot obtain it from the entry. This is the same sentence the round-68 Q11 seat scored (`.ufo/waves/round-68/R68ReviewEntryQ11.md` §3, entry:28 there); it is unchanged.

**(b) entry:37 — `46-byte` / `30-byte` fixed widths have no deriving output and no label.**

> `3. Walking the three central-directory records (46-byte fixed part per S032 §4.3.12) and their local headers (30-byte fixed part per S034 §4.3.7) selects three members; …`

No embedded output prints 46 or 30 (the member facts print `local_header_offset`, `payload_offset`, sizes, CRCs — never the fixed widths). The numbers are hardcoded literals in the reader, not derived: `readout.py:72-73` (comment), `:92` (`cursor + 30`), `:95-96` (`cursor + 46`), `:105` (`lh_off + 30`). The clause cites the spec sections but carries no "recorded" label, so Q11's "constants such as header offsets are derived, not assumed" is unmet. Values are correct (the walks land exactly: `cd_end_equals_eocd_offset: true`, `cursor == eocd` at `readout.py:119`). Same sentence as r68 §3 (entry:35 there), unchanged.

**(c) entry:157 — the oracle-agreement sentence has no command at all.**

> `The readout values agree with it on every shared field: image sha256 and size (item 1), the three members' local-header offsets, payload sizes and CRC-32 values (item 3), the nine strings, the three attribute rows and the two non-zero resource ids (items 6-8).`

No command compares the readout to the oracle, and the oracle side of every shared field is never printed:
```
$ grep -n 'truth\|oracle\|json.load\|compare' corpus/fixtures/apk-r65/readout.py
(no hits)
```
`truth.json`'s `axml_declared.resource_ids` do equal the readout's ids (checked directly), so the sentence is true — it is just not derived in the entry. Same sentence as r68 §3 (entry:152 there), unchanged.

**(d) Residual, weaker — entry:70, bit `0x100`.** `flags & 0x100` is cited to `readout.py:166` (verified) and the output prints `"flags": "0x00000100"` with `"utf8": true`, so the reader-side value is derivable; what is absent is the spec basis (`corpus/snapshots/ResourceTypes.h:480`, `UTF8_FLAG = 1<<8`), on which all nine decoded strings depend. The v4 wording ("the UTF-8 flag position the readout tests") is honest about provenance, so I do not rest the FAIL on this — it is named so the repair pass can close it in the same edit.

**(e) entry:6-7, :19, :194 — four file digests with no deriving command and no output.** Surfaced independently by the Q09 seat (`.ufo/waves/round-69/R69ReviewEntryQ09.md` §4 F2) and re-derived here for Q11's own text, which names "digest" explicitly.

| digest | file | entry line(s) |
|---|---|---|
| `74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa` | `corpus/derive_axml_anchors.py` | 6 |
| `27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173` | `corpus/fixtures/apk-r65/truth.json` | 7 |
| `eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a` | `corpus/fixtures/apk-r65/generator.py` | 7 |
| `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976` | `corpus/fixtures/apk-r65/readout.py` | 7, 19, 194 |

No embedded output prints any of the four. The two commands named in `recheck:` print other files' digests: the derivation prints `sha256 56b88bc4… ResourceTypes.h` (entry:131) and the readout prints the fixture's own `05d2280f…` (entry:27 and entry:200). Mechanical locator sweep:

```
truth.json             27303bae lines=[7] inside_output_lines=[]
generator.py           eaa9444c lines=[7] inside_output_lines=[]
readout.py             92e347c3 lines=[7, 19, 194] inside_output_lines=[]
derive_axml_anchors.py 74d4c0d9 lines=[6] inside_output_lines=[]
fixture.apk            05d2280f lines=[7, 23, 27, 200] inside_output_lines=[27, 200]
ResourceTypes.h        56b88bc4 lines=[1, 6, 131] inside_output_lines=[131]
```

All four values are correct (see the `sha256sum` capture in §1), which is precisely Q11's reject clause: correct when re-derived, derivation absent from the entry. This is a gap rather than a house exception — the entry already shows the pattern for two other files, printing the fixture digest at entry:27 and the snapshot digest at entry:131.

**Consequence for the entry's own Q-map:** entry:182 states "every count, offset, identifier and digest carries its deriving command and output in §Observation (items 1-10)". On (a), (b) and (e) that is false, and (e) is the sharp end because the row names "digest" explicitly. I did not use the Q-map row as evidence for this verdict; it is recorded because a false universal is itself the reject shape ("recorded value presented as re-derived"), exactly the defect that failed the v3's item-11 sentence.

## 3. Impact and the smallest safe correction

Under `reports/round-69/claims.md` §C1 kill rule — "Any Q FAIL on the v4 bytes … the C05 row stays `uncovered`, the v4 entry is marked `admission-status: rejected` … and C1 is reported **FALSIFIED**" — a Q11 FAIL blocks admission. I flip nothing; this is a reviewer finding for adjudication.

This is a **fixable defect, not a tradeoff**: no value is in doubt, and the remaining repair is confined to the entry's prose. Note the constraint that decides *which* repair is admissible: §Void conditions of `claims.md` (`reports/round-69/claims.md:185`) include "Changed `corpus/live` or `corpus/fixtures` bytes (… the round-65 fixture bytes are the claim surface and stay frozen)". `readout.py` lives under `corpus/fixtures/apk-r65/`, so **the derivation-emitting repair (adding `signature_hex` to `eocd`, adding a widths fact, adding an oracle-compare mode) is void this round** — it would also move the pinned stdout digest `507d79f8…` and the `15 stdout lines` count that entry:9/:194/claims.md repeat. The admissible minimal repair is therefore the Q11 "label recorded" branch, entry-only:

1. entry:30 — append provenance, e.g. "signature bytes `504b0506` recorded from S032 §4.3.8 (the reader searches for this literal, `readout.py:76-77`; the location is the derived value)". Do not present the four bytes as re-derived.
2. entry:37 — append "(46/30 recorded from S032 §4.3.12 / S034 §4.3.7; the walk's landing at 925 and the printed `payload_offset` values are the derived checks)". The `payload_offset` sentence already carries its `readout.py:99-105` derivation and is fine as written.
3. entry:157 — bound the sentence to what is printed, or name the oracle keys as recorded and state that the comparison is not re-run here (the entry already uses exactly this "not re-run by this entry" idiom for `generator.py` regeneration, so it is in-house style).
4. entry:70 — add `corpus/snapshots/ResourceTypes.h:480` (`UTF8_FLAG = 1<<8`) as the bit's anchor.
5. entry:6-7/:19/:194 — derive or label the four digests. **Constraint on the derivation route, verified:** the entry's embedded-output gate runs today as `checked_blocks=17 problems=0`, exit 0 (17 = 15 per-item blocks + the full-stdout block + the derivation block), so any repair must keep it clean. `check_embedded_outputs.py` executes only `python3`/`python`/`sys.executable` argv — `run_cmd:76-77` returns `(None, "", 2)` otherwise — and `evaluate:99-100` turns that into `(None, None)` → `main:160-162` exits 2 with "could-not-evaluate". A fenced `$ sha256sum …` block is therefore **inadmissible**: it would flip `C7_V4_CLEAN` from 0 to 2. Gate-safe options: (i) a `python3 -B -c "…"` hashing block — `parse_blocks:57` opens any block starting `$ `, and `drift` tests set membership (`:83-85,104-105`), so each printed line must match an embedded line as an exact string; (ii) the Q11 "recorded" label in prose or in a fence with no `$ ` line — invisible to `parse_blocks:57`, so it cannot disturb the 15-line/`507d79f8…` pin.
6. entry:182 — after 1-5, the Q11 row's universal is true; if only 1-3 are fixed, reword the row to the bounded set.

If the adjudicator prefers derivation over labeling, the readout change must be registered in a round that does not freeze `corpus/fixtures` (i.e. not this one).

**Cross-seat coordination (Q14).** The Q14 seat's FAIL (`.ufo/waves/round-69/R69ReviewEntryQ14.md`, entry:48) and this Q11 FAIL occupy disjoint legs, and both are entry-prose-only under `claims.md:185`: the Q14 repair rewrites the entry:48 sentence (facts preserved, count attribution moved), while this report's legs are entry:30, :37, :70, :157, :6-7/:19/:194 and the :182 row. Neither repair re-emits a tool output or touches `corpus/fixtures`, so a single edit pass closes both without moving the `507d79f8…` stdout pin or the 15-line count.

**Cross-seat confirmation (Q09).** `.ufo/waves/round-69/R69ReviewEntryQ09.md` §4 F2 surfaces the same four header digests under Q09's lens and reaches the same value verdict (all correct by `sha256sum`). Leg (e) here is that finding scored under Q11's text, which names "digest" in its own clause, so repair item 5 serves both reports; note the gate constraint in item 5 — the M39 gate re-runs only `python3` blocks, so the digest repair must be a python3 hashing block or a "recorded" label, never `$ sha256sum`.


## 4. Not wrong (so the repair pass does not churn)

No incorrect value found anywhere in items 1-11: 947/`05d2280f…`; EOCD 925, CD 737+188==925, 3 entries; members 0/465/618, payload offsets 49/506/668, sizes 416/112/69, CRCs `962d075f`/`2635c82a`/`e948d738` all `crc32_matches: true`; chunk walk 8→204→248→272→368→392→416; string pool 9/0/`0x00000100`/stringsStart 64 and all nine strings; resource map 9 ids with `0x0101021b`/`0x0101021c` at 5/6 and seven zeros; `attributeStart` 20 / `attributeSize` 20 / `attributeCount` 3; ns index `0xffffffff` on `package`/element; dex magic `6465780a30333500`, checksum `0x3d120c30` (declared == recomputed), SHA-1 `a5fc7bea8fa9ffaa52243540c8026066511b9fce`, file/header size 112, endian `0x12345678`; jar manifest 69 bytes/1 section; S038 lines 218/237/239/241/244/245/246/247/248/253/263/677/686/687/707/287/461/612/621; S043 line 5 and 7-8; r65:41 and the r67 `:244` attribution.

Tooling: nothing installed or updated this seat (no install needed; pacman guard respected; uv/npx not used).

Report: .ufo/waves/round-69/R69ReviewEntryQ11.md
