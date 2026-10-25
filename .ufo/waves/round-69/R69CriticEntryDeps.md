NOT NO-SILENT-DEPS — 2 values have no in-entry source (`UTF8_FLAG`/`SORTED_FLAG` semantics at entry:70; the EOCD record layout at entry:30) and 3 identity assertions carry no deriving command (entry:8 `c7b7cf98`, entry:11 "candidates keep every byte", entry:188 "round-65 corpus tree"). All three identity claims are TRUE when derived; every named hash reproduces. 4 findings: S-1 medium (C1/Q13 residual), S-2 low-medium (C1 scope), S-3 low (pointer), S-4 medium (C2/Q15).

# Silent-dependency audit — `corpus/knowledge/round-69-apk-axml-byte-evidence.md` (C05 v4)

seat: L1Revenger69.R69CriticEntryDeps · date 2026-10-25 · read-only (no edit, no mutation, no new source)
targets: entry (215 lines, sha256 `c1e7eaac9dba4c77e578c788755dec3e3499fd8795ad0e479c51b5be7deb11d5`, 35113 B), `corpus/snapshots/ResourceTypes.h`, S032/S034-derived payload offsets, item 11.

## What I actually ran and saw

| check | command | result |
|---|---|---|
| six named hashes | `sha256sum` on `fixture.apk truth.json generator.py readout.py derive_axml_anchors.py snapshots/ResourceTypes.h` | all six equal the entry's: `05d2280f…`, `27303bae…`, `eaa9444c…`, `92e347c3…`, `74d4c0d9…`, `56b88bc4…` |
| S047 derivation | `python3 -B corpus/derive_axml_anchors.py` | exit 0, **20 lines**, `diff` against entry:131-150 → identical (`DERIVE-MATCH`) |
| readout | `python3 -B corpus/fixtures/apk-r65/readout.py` | exit 0, **15 lines**, stdout sha256 = `507d79f8…dad247` (entry:9/:194) — exact |
| embedded stdout block | `diff <(sed -n 200,214p entry) readout.out` | identical (`STDOUT-BLOCK-MATCH`); all 15 per-item lines ⊆ fresh stdout |
| snapshot digests | `sha256sum` on `.ufo/waves/round-65/…ResourceTypes.h`, `.ufo/waves/round-67/…dex-format.html`, `.ufo/waves/round-65/…rea-android-applications.md` | `56b88bc4…`, `c0428612…` (281157 B), `412d9cb4…` — all match |
| cited readout lines | `awk` on `readout.py` | `:51-58` widths dict ✓, `:99-105` payload_off ✓, `:166` `flags & 0x100` ✓, `:22` `NO_INDEX = 0xFFFFFFFF` ✓, `:200-203` attr formula ✓ |
| S038 anchors | `awk` snapshot 236-266, 670-690, `grep UTF8_FLAG` | 237/239/241/244/245/246/247/248/253/263 ✓; struct 677 ✓; comment `attributeStart` 686 ✓, field 687 ✓; **`SORTED_FLAG=1<<0`:477, `UTF8_FLAG=1<<8`:480** |
| oracle key | `json.load(truth.json)` | `axml_declared.resource_ids` exists, 9 entries, two nonzero `0x0101021b`/`0x0101021c` ✓ |

## Value → source inventory (every value the entry states)

`src` = what the entry names; `vis` = is that source visible *inside the entry*.

### Header (lines 1-11)

| value | line | src | vis |
|---|---|---|---|
| S038 URL + tag `android-15.0.0_r1` | 1 | S038 | declared (external, deliberately not re-fetched) |
| S038 struct lines 218/287/461/612/621/677/707; enum 239/241/244/245/246/247/248/253; bounds 237/263; comment 686; field 687 | 1,59,84,153 | item 11 derivation | **yes**, machine-derived, reproduced |
| S038 snapshot path + sha `56b88bc4…` | 1,6 | S038/S047 | yes, verified |
| `corpus/snapshots/ResourceTypes.h` = same sha as row snapshot | 127 | S047 | yes, verified both files |
| S043 path, lines 7-8, sha `412d9cb4…` | 2 | S043 | yes — quoted lines match snapshot bytes |
| `S039` ("supersedes") | 2 | **none** | no — resolvable only at `corpus/SOURCES.md:53` |
| S045 URL, 4 quoted fragments, snapshot sha `c0428612…`, 281157 B | 3,109 | S045 | yes, verified |
| S032 `§4.3.12` 46-byte CD header | 4,37 | S032 | yes |
| **S032 EOCD record layout (`§4.3.16`)** | **30,34** | **not named — :4 scopes S032 to §4.3.12** | **NO** (→ S-2) |
| S034 `§4.3.7` 30-byte, name@26, extra@28 | 5,37 | S034 | yes (`readout.py:99-100`) |
| S047 script sha `74d4c0d9…`, 20 lines | 6 | S047 | yes, verified |
| `S046` ("supersedes") | 6 | **none** | no — `SOURCES.md:60` |
| S041 four hashes (947 B etc.) | 7 | S041 | yes, verified |
| `c7b7cf98` "unchanged since" | 8 | **none (no command, no full hash)** | **NO** (→ S-4) |
| derive "exit 2 on missing/ambiguous" | 9 | script | yes (`fail()` path read) |
| readout 15 lines + sha `507d79f8…` | 9,194 | named command | yes, reproduced |
| **"every S038 line number and value this entry cites"** | **9** | derivation | **PARTIAL — false for `UTF8_FLAG`** (→ S-1) |
| C05 row ref / admission-status | 10,11 | `corpus/README.md`, claims.md | yes |
| "round-65/67/68 candidates keep every byte" | 11 | **none** | **NO** (→ S-4) |

### Body

| value | line | src | vis |
|---|---|---|---|
| 947 B, sha `05d2280f…` | 23 | readout `archive` | yes |
| EOCD sig `504b0506` @925; 3 entries; 188 B @737; 737+188==925 | 30 | readout `eocd` + **undeclared** APPNOTE §4.3.16 | values yes / layout **no** (S-2) |
| 3 members: cd_index, local_header_offset 0/465/618, sizes 416/112/69, CRC 962d075f/2635c82a/e948d738, payload sha, `payload_first16_hex` | 41-45 | readout | yes, all 15 lines reproduce |
| `payload_offset = lh_off+30+name_len+extra_len` | 37 | `readout.py:99-105` | yes, pointer resolves |
| CRC-32 over payload (IEEE/zlib) | 37 | unnamed algorithm | implicit; low |
| AXML header type 3, headerSize 8, total 416; 6-chunk table | 52-56 | readout | yes |
| chunk-type names ↔ 237-263 | 59 | item 11 | yes |
| headerSize column 28/8/16/16/16/16 | 52 | item 5 (manual) | yes, labeled manual |
| struct field widths → 8/28/20/20/16/8 | 61-65 | `readout.py:51-58` manual | yes, pointer resolves; labeled manual |
| 9 strings, 0 styles, flags `0x00000100`, stringsStart 64, offsets, strings, `utf8:true` | 70-74 | readout | values yes |
| **"bit `0x100` … the UTF-8 flag position"** | **70** | **nothing** — `UTF8_FLAG = 1<<8` at snapshot:480; derivation prints no flag line | **NO** (S-1) |
| `sorted_flag` = test of `0x1` | 74 (output field) | snapshot:477, unnamed | no, implicit |
| 9 resource ids; `0x0101021b`/`0x0101021c` = `truth.json axml_declared.resource_ids` | 77-81 | readout + oracle key | yes, key and values verified |
| element `manifest`, no ns, attributeStart 20, attributeSize 20, attributeCount 3 | 84-88 | readout + item 5 derived sizes | yes |
| attrExt @ `chunk_base+16` | 84 | item 5 node=16 + S038:677 | yes |
| quote "Appears header.headerSize bytes after a `ResXMLTree_node`" | 84 | "line **677**" | **pointer wrong line — text is snapshot:675**, and the derivation prints no comment text (S-3) |
| quote "Byte offset from the start of this structure…" | 84 | line 686 | line derived; **content** not machine-printed |
| `uint16_t attributeStart;` @687 | 84 | item 11 | yes |
| attr *i* = `chunk_base+16+attributeStart+i*attributeSize` | 84 | `readout.py:200-203` | yes |
| `0xffffffff` treated as null | 91 | `readout.py:22` | yes |
| start/end namespace prefix/uri, offsets 248/392 | 95,104 | readout | yes |
| dex magic 8 B, checksum `0x3d120c30` from offset 12, "20-byte signature", recompute from 32, file/header 112, endian `0x12345678` | 109-113 | readout + S045 semantics | values yes; widths/offsets trace to S045's declared `header_item` table (`readout.py:234-236`), arithmetic unshown — informational |
| 69 B, first line, section_count 1 | 118-122 | readout | yes; "section" concept = JAR manifest format, unnamed — low |
| 20-line derivation output + composition arithmetic | 127-151 | script | yes, identical |
| enum block 237-263; `:244` FIRST_CHUNK vs `:245` START_NAMESPACE | 153 | item 11 | yes |
| M40/M44/M49 class ids | 153 | lessons (file unnamed) | resolvable, low |
| oracle agreement on 8 fields | 157 | `truth.json` | yes (spot-checked ids, members, strings) |
| regeneration "was round-65 evidence, not re-run" | 157 | S041 | declared |
| **"with the round-65 corpus tree (bytes unchanged through round 69)"** | **188** | **none** | **NO** (→ S-4) |
| full stdout 15 lines | 199-214 | named command | yes, byte-identical |
| §Q-map decisions | 177-184 | n/a (decisions) | — |

Net: **~60 stated values; 5 lack an in-entry source or deriving command.** Everything else is fully backed, and no stated hash, offset or count is contradicted by the bytes.

## Findings

### S-1 (medium — C1 gate / Q13 residual): the `recheck:` line still carries the universal credit the v4 claims to have repaired
- entry:9 — "`python3 -B corpus/derive_axml_anchors.py` from the lane root (**every S038 line number and value this entry cites**; exits 2 …)".
- entry:70 (item 6) labels flag bit `0x100` **"the UTF-8 flag position"**. That is S038's `UTF8_FLAG = 1<<8` at `corpus/snapshots/ResourceTypes.h:480` (`SORTED_FLAG = 1<<0` at :477). `grep -n "FLAG\|flags" corpus/derive_axml_anchors.py` → **no match**: the derivation prints no flag line, so the header's universal quantifier is false as written.
- This is precisely the v3 defect `claims.md` §C1 item 2 and entry:183 (Q13 row: "the v3 FAIL was a universal credit; the v4 sentence names the 20-line set") say was removed. Item 11 (:127) *is* correctly bounded to "items 4, 8 and 11" — so item 11 is honest and the residual is the header line plus the uncited constant at :70.
- Smallest safe correction (no value changes): at :70 cite `` `UTF8_FLAG = 1<<8` (corpus/snapshots/ResourceTypes.h:480) `` and `:477`; narrow :9 to "every S038 line number and enum value stated in items 4 and 8". (Adding the flags to the derivation would change S047's sha256 and its 20-line count — avoid.)

### S-2 (low-medium — C1 scope): the EOCD record's layout is used but not declared
- entry:30 (item 2) states what the EOCD *record states*: 3 entries, CD size 188 at +12, CD offset 737 at +16, signature `504b0506`. `readout.py:76-80` reads `eocd+10`, `+12`, `+16` — that mapping is APPNOTE **§4.3.16**, not §4.3.12.
- entry:4 scopes S032 to "central directory file header field layout … `§4.3.12` (46-byte fixed part)" and entry:15's Scope repeats only "S032 (central directory header) and S034 (local file header)". The entry says 6.3.10 (§4 does not name a revision either; `SOURCES.md:46` does).
- The source is **not fabricated**: `corpus/SOURCES.md:46` covers "central directory file header **and end-of-central-directory record** field layout … §4.3.3, §4.3.12, **§4.3.16** … fixed 22-byte record whose two total-entries counts sit at offsets 8 and 10". But that row's claim text names only offsets 8/10 — the `+12`/`+16` fields item 2 relies on are stated **nowhere** in entry or registry (only section-level §4.3.16 exists).
- Smallest safe correction: add "and §4.3.16 (22-byte EOCD record; total entries @+10, CD size @+12, CD offset @+16)" to entry:4, and name EOCD in entry:15.

### S-3 (low — pointer): the quoted attrExt comment is pinned to 677 but sits at 675
- entry:84 attributes "Appears header.headerSize bytes after a `ResXMLTree_node`" to "S038's `struct ResXMLTree_attrExt` (line 677)". Snapshot: `675: * Appears header.headerSize bytes after a ResXMLTree_node.`; 677 is the struct declaration; 686/687 are the *other* quote (correctly derived).
- entry:11's "no spec line number in this entry is transcribed by hand" holds for 677 (printed) but the sentence's own line (675) is neither cited nor printed, and no derivation prints quoted comment **text** — so both quoted sentences are unverified prose over verified line numbers.
- Smallest safe correction: cite 675 for the sentence (keep 677 for the struct), or add the two comment lines to the derivation's printed set.

### S-4 (medium — C2 calibration): Q15's instrument cannot fail on this entry, while C1's gate requires Q15 PASS on it
Three identity assertions in the v4 bytes, none carrying a deriving command:
1. entry:8 — "unchanged since `c7b7cf98`".
2. entry:11 — "The round-65, round-67 and round-68 candidates keep every byte."
3. entry:188 — "with the round-65 corpus tree (bytes unchanged through round 69)".

Derived (all **true**, so this is missing derivation, not false provenance):
```
git cat-file -t c7b7cf98 → commit ; git rev-parse c7b7cf98 → c7b7cf98ddeecbd5464e47396f224e6384b78905
git ls-tree c7b7cf98 -- corpus/fixtures/apk-r65/ → b62216a9 fixture.apk / aea5de72 generator.py / 0fcb1d85 readout.py / d6b8c5cb truth.json
git hash-object <same four files now>     → b62216a9 / d6b8c5cb / 0fcb1d85 / aea5de72   (identical set)
git diff --stat 222a7a7 -- corpus/knowledge/round-6{5,7,8}-apk-axml-byte-evidence.md → (empty)
```
- `corpus/QUALITY.md:27` (Q15) is lane-wide: "A stated git object id or tree identity is re-derived with the command that names it". None of the three does. `claims.md` §C1's gate is "every applicable Q01–Q15 decision … PASS (n/a only with the entry's named reason)" — no such reason is recorded for Q15-in-entry.
- `corpus/q15_tree_id_check.py:33` matches only ``` `<hex>:corpus` = `<40hex>` ``` and `scan()` (:80-95) only inspects lines beginning `tree-identity restatement:` / `tree-identity false-sentence:`. It therefore cannot flag entry:8/:11/:188, so `Q15_PRESENT=yes` / `Q15_SELFTEST=pass` do not imply the v4 entry is Q15-clean. The criterion's text is broader than its mechanical form.
- Smallest safe correction, either one: (a) append the two commands+output to entry:8/188 (I have them above; also drop `c7b7cf98` or give the full 40-hex id), or (b) write Q15's scope as the lesson's `tree-identity` lines in `QUALITY.md:27` and have the wave record Q15 `n/a` for the entry with that named reason.

### Informational (no correction required for gate)
- S039 / S046 predecessor ids appear in "supersedes" clauses with no source line; both resolve (`SOURCES.md:53`, `:60`) — dangling but reachable.
- item 10's "blank-line-separated section" is a JAR-manifest-format concept with no declared source; only observed counts are claimed.
- item 9's `12`/`32` are arithmetic over S045's declared `header_item` table; the declared table is named, the arithmetic is unshown.
- M40/M44/M49 (entry:8, :153) are lesson class ids; the lesson file is not named in-entry.

## Counterexample test (strongest available)
The strongest attack I could build from local evidence was **"the entry asserts a git object id, and this round's new criterion demands exactly that be re-derived"** — proven above (S-4): the entry does state one, the criterion does demand it, the checker cannot see it, and the claim happens to be true. It is a **duplicate-authority / gate-scope defect, not a false-provenance kill**: no stated value resolves to something else, so it does not by itself falsify C1 — it makes the Q15 leg of C1 either `n/a`-with-reason or a one-clause edit, and it narrows C2's claimed instrument coverage.

## Impacted axes
- **C1 (coverage)**: S-1 puts a Q13-adjacent universal credit on the v4 bytes that a strict Q13 seat can FAIL; S-2 is a scoping clause on item 2; S-3 is a pointer a strict Q11/Q15 seat can FAIL; S-4 makes "Q15 applicable to the entry" an unresolved gate question.
- **C2 (calibration)**: S-4 — `QUALITY.md:27`'s text exceeds `q15_tree_id_check.py`'s coverage; `Q15_PRESENT=yes` alone does not establish that a bare object id is caught.
- Not impacted: item 11's derivation credit (reproduced byte-identically), every hash/digest, the fixture bytes, the oracle correspondence, the Q01/Q02/Q04/Q05/Q07/Q14 rows I re-read.

## Hygiene
Read-only throughout: no file in the lane, corpus, fixtures, sibling lane or `/home/vgpnk/Projects/shokuknow` was written; no git/jj mutating command; no package installed or upgraded (used the host `python3`/`sha256sum`/`git` only). Scratch `/tmp/revenger-r69-deps-*` deleted before return.
