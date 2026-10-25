FAIL — Q11 — the entry's own universal claim "no spec line number in this entry is transcribed by hand" is false on its own bytes: it states snapshot line numbers **237** and **244** that `corpus/derive_axml_anchors.py` never prints, and the enum *values* it attributes to S038 are never emitted by any command; every value is numerically correct, but the derivations are absent while presented as present.

Reviewer: `L1Revenger68.R68ReviewEntryQ11` (fresh, not the author). Criterion only: Q11 (`corpus/QUALITY.md:24`, "Supersedes Q08 … carries, inside the entry, the command that derives it from the primary record … and that command's output. Constants such as header offsets are derived, not assumed. A value cited only to prose is labeled recorded, not re-derived"). Subject bytes: `corpus/knowledge/round-68-apk-axml-byte-evidence.md` (215 lines, `admission-status: candidate`). No file was edited; nothing outside this report was written.

## 1. The entry's commands reproduce (this part of Q11 is strong)

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin
$ python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/q11_readout.txt; echo EXIT=$?
EXIT=0
$ wc -l < /tmp/q11_readout.txt
15
$ sha256sum /tmp/q11_readout.txt
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  /tmp/q11_readout.txt   # == entry:7 recheck claim
$ python3 -B corpus/derive_axml_anchors.py > /tmp/q11_anchor.txt; echo EXIT=$?
EXIT=0
$ wc -l < /tmp/q11_anchor.txt
17
```

Pinned digests all match: `fixture.apk 05d2280f…d03e` (947 B), `truth.json 27303bae…8173`, `readout.py 92e347c3…3976`, `corpus/snapshots/ResourceTypes.h 56b88bc4…c56f` (86255 B) == `.ufo/waves/round-65/source-snapshots/ResourceTypes.h 56b88bc4…c56f`, `derive_axml_anchors.py bce497d6…e249`.

Every one of the 15 distinct readout fact lines is embedded **verbatim**: I extracted all 30 `{…}` lines from the entry (15 in the per-item blocks + the same 15 in §Reproduce) and matched them as exact strings against the captured stdout — 30/30 EXACT, 0 divergence. The item-11 anchor block (entry:129-146) is likewise byte-for-byte equal to `/tmp/q11_anchor.txt`. So the readout side has **zero transcription drift**; the M39 class this entry says it repairs is genuinely repaired there.

## 2. The Q11 failure — two stated S038 line numbers have no derivation, and the entry says they do

Mechanical sweep of every line-number token in the entry against what the script actually prints:

```
$ python3 -c '…regex sweep…'
script prints line numbers: 218 239 241 245 246 247 248 253 287 461 612 621 677 686 687 707
entry line-number tokens:   218 237 239 241 244 245 246 247 248 253 287 461 612 677 686 687 707
NOT printed by script:      237 244
```

The structural reason (so this is not a transcription slip but an unguarded gap): the script iterates two **fixed whitelists**, `derive_axml_anchors.py:35-43` (`STRUCTS`) and `:45-53` (`ENUMS`), and its enum predicate is `l.strip().startswith(n + " ")` (`:93-95`) emitting only `f"enum {name} : {line}"` (`:96`). It has no probe for the `enum {` block-opening line and no `RES_XML_FIRST_CHUNK_TYPE` entry, and it never emits the `= 0x…` value. It cannot print 237, cannot print 244, and cannot print any enum value — whatever the entry says.

Exact entry lines at issue (all values are **correct** when re-derived — I checked the snapshot bytes — the defect is that the derivation is absent while the entry asserts it is present):

- **entry:148** — "The chunk-type enum block spans lines **237-253** and `RES_XML_START_NAMESPACE_TYPE` is line **245**; **line 244 is `RES_XML_FIRST_CHUNK_TYPE`**." Neither 237 nor 244 is in the printed output. Correct values: snapshot line 237 is `enum {`; line 244 is `    RES_XML_FIRST_CHUNK_TYPE          = 0x0100,` (verified below). The correct 245 and 253 are printed.
- **entry:125** — "**Every S038 line number this entry states is printed by a committed derivation script** … **no spec line number in this entry is transcribed by hand**." This sentence is false on its own bytes: 237 and 244 are transcribed. This is the reject clause "a recorded value is presented as re-derived", stated as a universal.
- **entry:1** (`source:` S038) — "chunk-type enum block **lines 237-253**" and closing "**every line number above is machine-derived** by `corpus/derive_axml_anchors.py` … item 11". Same false universal; 237 is not printed.
- **entry:4** (`source:` S046) — "the machine derivation of **every** S038 line number this entry cites". Overstated for 237/244 (a source-row defect for the S046 seat; recorded here, not scored by me).

Snapshot bytes proving the two values are right but underived:

```
$ sed -n '235,256p' corpus/snapshots/ResourceTypes.h | cat -n
     1  };
     2
     3  enum {                                            <- line 237
     4      RES_NULL_TYPE                     = 0x0000,   <- 238
     5      RES_STRING_POOL_TYPE              = 0x0001,   <- 239 (script prints 239)
     …
    10      RES_XML_FIRST_CHUNK_TYPE          = 0x0100,   <- line 244 (script does NOT print)
    11      RES_XML_START_NAMESPACE_TYPE      = 0x0100,   <- line 245 (script prints 245)
    12      RES_XML_END_NAMESPACE_TYPE        = 0x0101,   <- 246
    13      RES_XML_START_ELEMENT_TYPE        = 0x0102,   <- 247
    14      RES_XML_END_ELEMENT_TYPE          = 0x0103,   <- 248
    19      RES_XML_RESOURCE_MAP_TYPE         = 0x0180,   <- 253
```

## 3. Same class, lower stakes — constants asserted with no in-entry command (Q11 "constants … derived, not assumed")

All five are **numerically correct**; each carries neither a command output in the entry nor a "recorded" label. Each is an independent instance of the reject clause, so fixing only §2 would still leave Q11 short.

- **entry:57** (item 4) — "The six chunk types … `0x0001` … `0x0180` … `0x0100` … `0x0102` … `0x0103` … `0x0101` — **are the values S038's chunk-type enum block names**". The six numbers appear in the chunk table as ints (`type: 1/384/256/258/259/257`), so the fixture side is derived; the *name↔value join* is not — the script prints names and line numbers only, never `= 0x…`. Correct per snapshot (239=0x0001, 245=0x0100, 246=0x0101, 247=0x0102, 248=0x0103, 253=0x0180), underived.
- **entry:59** (item 5) — "computed by summing the field widths of **S038's own struct definitions** … **not assumed**". No command reads S038's struct definitions: `readout.py:56-60` hard-codes `"ResXMLTree_attrExt": [w32, w32, w16, w16, w16, w16, w16, w16]`, and the emitted `bytes_per_field` table is a sum over hand-entered lists. The sum is printed (`spec_derived_struct_widths`); the field list is transcribed. (Widths themselves check out: 8/28/20/20/16/8 == the sums of the printed lists and the observed `headerSize` column 28,8,16,16,16,16.)
- **entry:35** (item 3) — "**46-byte** fixed part per S032 §4.3.12" and "**30-byte** fixed part per S034 §4.3.7": cited to registry rows, with no in-entry command/output and no "recorded" label. Correct from the bytes:
  ```
  $ xxd -s 765 -l 2 corpus/fixtures/apk-r65/fixture.apk    # CD name_len at 737+28
  000002fd: 1300                                            # 0x0013 = 19
  $ xxd -s 783 -l 19 corpus/fixtures/apk-r65/fixture.apk   # name at 737+46
  0000030f: 416e 6472 6f69 644d 616e 6966 6573 742e  AndroidManifest.
  0000031f: 786d 6c                                  xml
  $ xxd -s 26 -l 2 corpus/fixtures/apk-r65/fixture.apk     # LH name_len at 0+26
  0000001a: 1300                                            # 19
  $ xxd -s 30 -l 19 corpus/fixtures/apk-r65/fixture.apk    # name at 0+30
  0000001e: 416e 6472 6f69 644d 616e 6966 6573 742e  AndroidManifest.
  ```
  (46 and 30 are also only in a code comment, `readout.py:72-73`, and as literals at `:92`, `:95-96`, `:105`.)
- **entry:28** (item 2) — "The end-of-central-directory signature **`504b0506`**". The `eocd` fact prints offsets/counts but not the signature bytes (`readout.py:76-77` has `PK\x05\x06` but emits no `signature_hex`). Correct: `$ xxd -s 925 -l 4 fixture.apk → 504b 0506`.
- **entry:68** (item 6) — "bit **`0x100`** set, the **UTF-8 flag** position the readout tests (`flags & 0x100`, readout.py:166)". `readout.py:166` is exactly `utf8=bool(flags & 0x100),` (verified), but the *spec* basis for the bit is not cited or printed: `corpus/snapshots/ResourceTypes.h:480` `UTF8_FLAG = 1<<8`. The reader's constant is assumed, not derived — and all nine decoded strings hang on it.
- **entry:152** (§Comparison) — "The readout values **agree with it on every shared field**". No command shows `truth.json`'s values or a diff; `readout.py` has no oracle mode (`grep -n "truth\|oracle\|json.load" readout.py` → no hits). The oracle's own content (e.g. `resource_ids` = the same nine ids including `0x0101021b`/`0x0101021c`) is correct, but the agreement is prose-only.

## 4. What is *not* wrong

No incorrect value found. Every derived number, digest, offset, string and hex byte I re-derived matches: archive 947/`05d2280f…`, EOCD 925 / CD 737+188==925 / 3 entries, member offsets 0/465/618, payload offsets 49/506/668, sizes 416/112/69, CRCs `962d075f`/`2635c82a`/`e948d738` with `crc32_matches true`, chunk walk 8→204→248→272→368→392→416, string pool 9/0/`0x00000100`/stringsStart 64, resource map ids, `attributeStart` 20 / `attributeSize` 20 / `attributeCount` 3, ns indices, dex checksum `0x3d120c30`, SHA-1 `a5fc7bea8fa9ffaa52243540c8026066511b9fce`, file/header size 112, endian `0x12345678`, jar manifest 69/1 section. The referenced `readout.py` line numbers I spot-checked are accurate (`:22` = `NO_INDEX = 0xFFFFFFFF`, `:99-105` = the payload-offset derivation, `:166` = `flags & 0x100`, `:200-203` = the attrExt-relative comment). The entry's stated `headerSize` column equals the derived struct widths, and `attrExt`=20/`attribute`=20 equal the observed `attributeStart`/`attributeSize`.

The script's own guard is real: digest mismatch exits 2 (`derive_axml_anchors: snapshot digest 443bf2f0… != pinned 56b88bc4…`, exit 2), and `find_unique` (`:62-70`) fails on 0 hits and on >1 hits. So the exit-2 claim at entry:125 is trustworthy — the gap is its *coverage*, not its guard.

## 5. Impact and the smallest safe correction

Consequence under the frozen contract: a Q FAIL on the v3 bytes does not admit. Per `reports/round-68/claims.md` §C2 kill rule — "Any Q FAIL on the v3 bytes … the C05 row stays `uncovered`, the v3 entry is marked `admission-status: rejected` (retained as evidence, every other byte kept), and C2 is reported **FALSIFIED** — honest stop, no re-target". I do not flip anything; this is a reviewer finding for adjudication.

This is a **fixable defect, not a tradeoff** — no fact is in doubt, and the repair is mechanical, confined to the two scripts' coverage plus one re-capture:

1. Extend `corpus/derive_axml_anchors.py` so its output covers exactly what the entry states: add a block-open probe emitting the `enum {` line of the chunk-type block (237), add `RES_XML_FIRST_CHUNK_TYPE` to `ENUMS` (244), and extend the enum emit to carry the value (`enum RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100`) so entry:57's six name↔value pairs are printed. Optionally emit each struct's field lines so entry:59's field lists are derived rather than transcribed.
2. Re-capture entry:125-146 verbatim from the new stdout (17 → ~19-21 lines), and update `source:` S046's "17 output lines" (`entry:4`) and `verified-at`/`recheck` accordingly; re-run `corpus/check_embedded_outputs.py` after the edit (the entry's blocks must stay gate-clean).
3. Either derive or relabel the remaining constants: `504b0506` → emit `signature_hex` in the `eocd` fact (the bytes are already at `readout.py:76-77`); 46/30 → emit the two fixed widths from a decoded record (or label "recorded from S032 §4.3.12 / S034 §4.3.7"); `0x100` → cite `snapshots/ResourceTypes.h:480` (`UTF8_FLAG = 1<<8`) and print it in a fact; §Comparison (entry:152) → embed a `truth.json` dump/compare output, since `readout.py` currently has no oracle mode.

Tooling: none installed or updated this seat (no installs were needed; pacman guard respected).

Report: .ufo/waves/round-68/R68ReviewEntryQ11.md
