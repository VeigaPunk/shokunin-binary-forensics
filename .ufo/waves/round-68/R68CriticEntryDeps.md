FAIL (silent-dep audit) — the v3 entry is NOT `NO-SILENT-DEPS`: 5 undeclared/underived sources (D1-D5) plus 3 minor (D6-D8). No stated *number* is wrong — every re-runnable value reproduces byte-exactly — so these are coverage/provenance gaps in the machine-derivation claim, not value defects. The sharpest one falsifies the entry's own universal claim (entry:125) and C2's predicate wording ("every spec line number derived").

## 0. What reproduces exactly (so the findings below are coverage, not arithmetic)

| check | command | result |
|---|---|---|
| readout recheck | `cd /home/vgpnk/Projects/shokunin/revenger-shokunin && python3 -B corpus/fixtures/apk-r65/readout.py` | exit 0, **15** lines, sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — matches entry:6/§Reproduce |
| derive recheck | `python3 -B corpus/derive_axml_anchors.py` | exit 0, **17** lines, identical to the entry:129-147 block |
| embedded vs actual | diff of the entry's 15 `{"…` lines and 17 derivation lines against live stdout | **byte-identical**, 0 diffs (no embedding drift of the M39 class) |
| counted tree | `git archive HEAD corpus \| tar -x -C /tmp/r68tree` then run both scripts from `/` | readout 15 lines + same sha256; derive 17 lines — scripts are `__file__`-relative, so the counting command's `git archive` tree replays |
| committed | `git ls-tree -r HEAD -- corpus/snapshots corpus/derive_axml_anchors.py corpus/knowledge/round-68…` | all three present in HEAD `4232235`; `git status --porcelain` clean for them |
| snapshot copy | `sha256sum corpus/snapshots/ResourceTypes.h .ufo/waves/round-65/source-snapshots/ResourceTypes.h` | both `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`, 86255 bytes — as claimed |
| S046 script pin | `sha256sum corpus/derive_axml_anchors.py` | `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249` — as claimed |
| S043 | `sha256sum .ufo/waves/round-65/source-snapshots/rea-android-applications.md` | `412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c` — as claimed |
| S045 | `sha256sum`/`wc -c` `.ufo/waves/round-67/source-snapshots/dex-format.html` | `c0428612…d9f4`, 281157 bytes — as claimed; all four quoted sentences present (`grep -c`: adler32 1, SHA-1 1, `must be 0x70` 1, `0x12345678` 1) |
| S032/S034 own anchor | `.ufo/waves/round-63/source-snapshots/appnote.txt` | `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`; sed 387-399 = §4.3.7 local-header field list, incl. "30-byte" widths — resolvable offline |
| "unchanged since `c7b7cf98`" | `git show c7b7cf98:<f> \| sha256sum` for fixture.apk / readout.py / truth.json / generator.py | all four identical to current (`05d2280f…`, `92e347c3…`, `27303bae…`, `eaa9444c…`) — claim holds |
| oracle correspondence | `truth.json` `axml_declared.resource_ids` / `.strings` / `.attributes` / `members` | exact match to items 6/7 and the three member rows |
| line citations in the entry | `readout.py:99-105`, `:200-203`, `:166`, `:22` | all resolve to the cited statements |

## 1. Undeclared / underived sources

**D1 — line `237` (enum-block start) has no derivation.** Stated four times: entry:1 ("chunk-type enum block **lines 237-253**"), entry:57 (item 4), entry:148 (item 11), entry:157 (§inference). The 17-line derivation output contains **no 237** (`grep -n "237" /tmp/r68deps_derive.txt` → only the sha line's `…958c56f`, no line-number hit; `RES_XML_FIRST_CHUNK_TYPE` is not in the script's `ENUMS`, `corpus/derive_axml_anchors.py:45-53`). This directly contradicts entry:125 ("**Every** S038 line number this entry states is printed by a committed derivation script") and entry:4 (S046 scope: "the machine derivation of **every** S038 line number this entry cites"), and it contradicts C2's frozen predicate as written in `reports/round-68/claims.md` ("with **every** spec line number derived by a committed script … instead of transcribed"). The value 237 is correct (`sed -n '237p'` = `enum {`), so the defect is the universal claim, not the number.

**D2 — line `244` (`RES_XML_FIRST_CHUNK_TYPE`) is stated and not derived.** entry:148: "line 244 is `RES_XML_FIRST_CHUNK_TYPE`". That symbol is absent from the derivation table; the sentence asserting it is hand-transcribed prose inside the item that declares the transcription class closed. Strongest counterexample available: change `244` to `243` in entry:148 and **no lane recheck fails** — the derivation never prints that symbol, and the registered gate only compares embedded command output. The value happens to be right (sed 237-255 confirms line 244 = `RES_XML_FIRST_CHUNK_TYPE`, line 245 = `RES_XML_START_NAMESPACE_TYPE`), so this is a live M40/M44 surface, not a wrong anchor.

**D3 — the chunk-type numeric *values* have no derivation and no named line.** entry:57 binds observed types to names: `0x0003` `RES_XML_TYPE`, `0x0001` string pool, `0x0180` resource map, `0x0100`/`0x0101` start/end namespace, `0x0102`/`0x0103` start/end element. The derivation prints symbol **lines only, never values** (`derive_axml_anchors.py:88,92` → `f"struct {name} : {line}"`, `f"enum {name} : {line}"`), so the value↔name binding is asserted, not printed; the same literals are hardcoded in the reader at `readout.py:129, 148, 171, 178, 187, 226`. A mis-transcribed value (say `0x0104` for start-element) would pass both rechecks. Values verified correct against `ResourceTypes.h:238-253`, but by me, not by the artifact.

**D4 — `UTF8_FLAG = 1<<8` and `SORTED_FLAG = 1<<0` are never named.** entry:68 says flags `0x00000100` is "the UTF-8 flag position **the readout tests** (`flags & 0x100`, readout.py:166)" — the script is named as the source of a *spec* fact. The actual anchors, `ResourceTypes.h:480` (`UTF8_FLAG = 1<<8`) and `:477` (`SORTED_FLAG = 1<<0`), appear nowhere in the entry, are not in the derivation table, and `"sorted_flag": false` (entry:63, :201) is an interpretation of bit 0 with no resolvable source. This is the cleanest silent dependency: a layout claim loaded from S038 without an S038 pointer, under §Q-map Q01's "every load-bearing layout claim rests on S038".

**D5 — the struct field lists are hand-transcribed literals, presented as spec-derived.** entry:59: "The fixed structure widths used by the readout are **computed by summing the field widths of S038's own struct definitions** … **not assumed**". The summing is machine work (`readout.py:60`, `sum(w)`), but the field-width vectors are literal constants at `readout.py:52-59` (`"ResXMLTree_attrExt": [w32, w32, w16, w16, w16, w16, w16, w16]`, …). The script never opens `ResourceTypes.h`; `source_anchor` in the output is a string field, not a read. I verified all six vectors are correct against the snapshot (`ResChunk_header` 218-232, `ResStringPool_header` 461-480, `ResXMLTree_node` 621-631, `ResXMLTree_attrExt` 677-702 incl. `styleIndex` at :704, `ResXMLTree_attribute` 707-717, `Res_value` 287-300) — so no wrong number, but "not assumed" is unsupported: a transcribed field-list error is invisible to every recheck, and item 5's `attributeStart == 20` coincidence is reported as corroboration without an assertion in code (`readout.py` never compares `attribute_size`/`attribute_start` to the derived widths).

## 2. Minor

- **D6** — `generator.py` is inside S041's declared scope and §Comparison's regenerate-provenance rests on it, but the entry pins only fixture/truth/readout hashes; `generator.py` = `eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a` and is identical at `c7b7cf98`, so content is fine — the pin is missing. One hash closes it.
- **D7** — `NO_INDEX = 0xFFFFFFFF` (entry:82 cites `readout.py:22`) has no S038 anchor: the snapshot's only `0xFFFFFFFF` are `ResStringPool_span::END` (`:498`) and `ResTable::NO_ENTRY` (`:1456`), and `struct ResStringPool_ref` (`:430-436`) declares only `uint32_t index`. **Disclosed** ("treated as null by the readout"), so not silent — but the null-namespace rendering is a convention with no cited source.
- **D8** — `readout.py:11` names `corpus/knowledge/round-65-apk-axml-byte-evidence.md` as the consumer of its fact ids; that file still exists (21166 B) and is superseded twice. Stale docstring pointer, not load-bearing.

## 3. Impacted axes

- **Q11** (`entry:182`, "pass"): its stated basis — "the spec line numbers carry their deriving command … (item 11, machine-derived, not transcribed)" — is falsified for 237 and 244 by D1/D2. Q11 cannot stand as written.
- **Q01** (`§Q-map` Q01 row): wants every load-bearing layout claim to rest on S038; D4 (flag bit positions) and D3 (chunk-type values) load layout facts whose S038 pointers do not exist in the entry.
- **Q06/Q09**: unaffected — oracle and digest claims resolve exactly (see §0).
- **Predicate, not cosmetics**: `claims.md` §C2 frozen predicate requires "every spec line number derived". D1/D2 are within that predicate, so a wave PASS that ignores them would be a pass over an unmet predicate.

## 4. Smallest safe correction

Extend the *derivation*, not the claim — no value in the entry needs changing:

1. `corpus/derive_axml_anchors.py`: add `RES_XML_FIRST_CHUNK_TYPE` (and `RES_XML_CDATA_TYPE`/`RES_XML_LAST_CHUNK_TYPE` if the block citation is kept), emit the enum **values** (`enumv NAME : <line> = 0xNNNN`) for the seven cited symbols, print the enum block's first/last line (covers `237`), and add `const UTF8_FLAG : 480` / `const SORTED_FLAG : 477` (covers D4).
2. For D5, cheapest correct option: reword entry:59 to "field lists transcribed from S038:218-232 / 461-480 / 621-631 / 677-702 / 707-717 / 287-300, widths summed at `readout.py:52-61`", and cite those six ranges. Deriving the vectors from the snapshot is better but needs a field parser; the reword removes the false "not assumed" at zero risk.
3. Pin `generator.py` sha `eaa9444c…` in the S041 row (D6).
4. **Coupling — must move in one commit or the fix creates new false provenance**: the script change alters `derive_axml_anchors.py` sha (`bce497d6…` pinned in the S046 row and entry:4), the "17 output lines" count (entry:4, S046 row), and the entry:129-147 embedded block, and it changes what the C1 gate must re-check verbatim (register the new expectation in `corpus/check_embedded_outputs.py`'s registry). If only the script moves, the entry's sha pin and its embedded derivation become false — strictly worse than the current state.

## 5. Scope / tooling

Read-only seat: no production file was written; the only write is this report. Both rechecks were run (they write nothing) and one `git archive HEAD corpus` was extracted to `/tmp/r68tree` (outside the lane). No `git`/`jj` mutation, no sibling-repo or `shokuknow` access. No tool installed or upgraded, so nothing to record under the tooling directive.
