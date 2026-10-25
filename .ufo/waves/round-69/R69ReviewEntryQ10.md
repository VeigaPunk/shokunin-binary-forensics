PASS — Q10: every finding in `corpus/knowledge/round-69-apk-axml-byte-evidence.md` is scoped to one authored APK fixture, one manual stdlib byte readout plus one pinned-snapshot anchor derivation, named spec versions (`android-15.0.0_r1`, APPNOTE 6.3.10, dex `035`) and named inputs; the §Limitations premises re-derive true from the built bytes, no fixture observation is stated as a universal, and the kaidoku/revenger ADJ-06 contest is reported (fleet `.ufo/l0-questions.md:42`, verified open) rather than absorbed.

# R69ReviewEntryQ10 — Q10 on the C05 v4 candidate

Seat: `L1Revenger69.R69ReviewEntryQ10` (leaf, read-only; no subagents, no edits to the entry or any repo file).
Entry under review: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-69-apk-axml-byte-evidence.md`
(`admission-status: candidate`, entry line 11).
Criterion: `corpus/QUALITY.md` row **Q10** — "A finding is scoped to the observed family, operation, version and input. Cross-lane contested scope is reported, not absorbed." reject trigger: "one family's observation is stated as a universal".
Contract read first: `reports/round-69/claims.md` §C1 (frozen predicate, admission order), then `corpus/QUALITY.md`.
Nothing was installed; no package manager was touched. Scratch `/tmp/revenger-r69-q10-*` deleted before return.

## 1. Re-derivation of every value this verdict relies on

I ran the entry's own commands from the lane root and compared actual stdout against the entry's embedded lines.

**Anchor derivation (entry item 11, lines 127-153; S047):**

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && python3 -B corpus/derive_axml_anchors.py
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

20 lines, exit 0 — exactly the count the entry and S047 claim. Machine check that no embedded line was transcribed:

```
actual readout lines: 15 missing verbatim from entry: 0
derivation exit 0 lines 20 missing from entry: []
```

**Byte readout (entry items 1-10, item 11's recheck):**

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/revenger-r69-q10-readout.txt
READOUT_EXIT=0
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  /tmp/revenger-r69-q10-readout.txt
15 /tmp/revenger-r69-q10-readout.txt
```

The digest equals the entry's `recheck:` value (`507d79f8…`, line 9) and the 15-line count equals §Reproduce (line 186+). All 15 actual lines appear verbatim in the entry (0 missing), so the §Observation JSON blocks are reproductions, not transcriptions.

**Pinned snapshot, read directly (input identity for the derivation):**

```
$ sed -n '237,265p' corpus/snapshots/ResourceTypes.h | cat -n
     1  enum {
     2      RES_NULL_TYPE                     = 0x0000,
     3      RES_STRING_POOL_TYPE              = 0x0001,
    ...
     8      RES_XML_FIRST_CHUNK_TYPE          = 0x0100,
     9      RES_XML_START_NAMESPACE_TYPE      = 0x0100,
    10      RES_XML_END_NAMESPACE_TYPE        = 0x0101,
    11      RES_XML_START_ELEMENT_TYPE        = 0x0102,
    12      RES_XML_END_ELEMENT_TYPE          = 0x0103,
    17      RES_XML_RESOURCE_MAP_TYPE         = 0x0180,
    27  };
$ sha256sum corpus/snapshots/ResourceTypes.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
```

237 + (n-1) gives `enum {` = 237, `};` = 263, `RES_XML_FIRST_CHUNK_TYPE` = 244, `RES_XML_RESOURCE_MAP_TYPE` = 253 — the entry's item-4 line claims (line 52) are the snapshot's bytes, and the snapshot digest equals the S038/S047 digest in the header.

## 2. Prong A — family / operation / version / input are named and bounded

Entry lines that carry the scoping (quoted from the file):

- **line 10** `coverage-map: C05 …` — "the container members, the binary-AXML `AndroidManifest.xml` and the `classes.dex` declared header **of one authored APK fixture** … Not covered: install/signature verification, dex validity or execution, provider (`inspect_android_package`) readiness or output, **general AXML or ZIP-parser behavior beyond this fixture**."
- **line 15** `Scope.` — "One authored APK, `corpus/fixtures/apk-r65/fixture.apk`, and the authored oracle … Nothing is extracted to disk, nothing is executed, no producer is called, no network is used, and no verifier source is read." (operation named)
- **line 1** S038 `source:` — "… for one authored binary `AndroidManifest.xml` … chunk-type enum block **lines 237-263**"; the URL pins `refs/tags/android-15.0.0_r1` (version).
- **line 4** S032 / **line 5** S034 — "central directory file header … for one authored ZIP archive: `§4.3.12`"; "local file header … `§4.3.7` … the `payload_offset` derivation in item 3 rests on these widths". The APPNOTE version the entry states, **6.3.10**, is the registry's own bound version: `corpus/SOURCES.md:46` and `:48` both read "version 6.3.10 (revised Nov 01, 2022)". Re-derived, not invented.
- **line 127** (item 11) — "The credit is bounded to exactly the numbers the command prints: the 20-line stdout below … is the complete set of S038 line numbers this entry states." Re-derived true: 1+7+1+8+1+1+1 = 20.
- **line 77** (item 7) — "… the all-zero entries are recorded as observed, and **no framework-wide semantics for a zero entry is claimed from this fixture**."
- **line 91** (item 8) — "… an observation of how this readout resolves **this fixture's** bytes, **not a prediction about any other parser**."
- **line 162** (§Inference bullet) — "Each inference cites its byte evidence and its registry anchor, and **each is scoped to this fixture**."

No reject-trigger occurrence found: I found no sentence that lifts a fixture observation to a family/format universal. The two places where a weaker entry would universalize (zero resource-map entries; `0xffffffff` ns-index resolution) each carry an explicit in-line refusal, quoted above.

## 3. Prong B — §Limitations premises re-derive true from the built bytes

Entry line 167: "One authored fixture, one manifest shape (a single element with three attributes), UTF-8 string pool only, no CDATA, no nested elements, no styles. The container is ZIP_STORED with no data descriptors … The dex member is a header only and is intentionally not a valid dex program. Generalization to other APKs, other AXML producers or the `inspect_android_package` provider would need its own evidence."

Checked each premise against bytes/actual stdout:

| premise | evidence |
|---|---|
| one element, three attributes | `axml_chunk_table` prints exactly one `type 258` (start element, offset 272) and one `type 259` (end element, offset 368), no `0x0104` CDATA chunk; `axml_start_element` prints `"element_name": "manifest"`, `"attributeCount": 3` |
| UTF-8 pool only | `axml_string_pool` prints `"flags": "0x00000100", "utf8": true, "styleCount": 0` |
| no nested elements | chunk walk is a flat 6-chunk list ending at `xml_total_size 416` with `"xml_total_size_equals_member": true`; single start/end element pair |
| no styles | `"styleCount": 0, "stylesStart": 0` |
| ZIP_STORED, no data descriptors | independent struct read of the three local headers (below) |
| header-only dex | `dex_declared_header` prints `"file_size": 112, "header_size": 112, "header_bytes": 112` |

Independent check of the container premise (the entry's readout prints only sizes, so I read the fields myself):

```
$ python3 -B - <<'EOF'   # struct read of fixture.apk local headers
print: AndroidManifest.xml sig 504b0304 ver 20 flaghex 0x0 method 0 nlen 19 elen 0 bit3 False
       classes.dex         sig 504b0304 ver 20 flaghex 0x0 method 0 nlen 11 elen 0 bit3 False
       META-INF/MANIFEST.MF sig 504b0304 ver 20 flaghex 0x0 method 0 nlen 20 elen 0 bit3 False
       eocd sig at 925: 504b0506
```

All three members: compression method `0` (stored), general-purpose flags `0x0000` (bit 3 clear → no data descriptor), and the name lengths reproduce the readout's payload offsets (`0+30+19=49`, `465+30+11=506`, `618+30+20=668`). Every §Limitations premise is true of the built bytes.

## 4. Prong C — cross-lane contested scope reported, not absorbed

Entry line 171 (§Cross-lane scope note (Q10), heading line 169): "The provider route (`inspect_android_package`, JADX prerequisites) is documented scope from S043 only; this lane ran no provider and makes no readiness claim (Q05 fence). The kaidoku/revenger ADJ-06 overlap and fleet `l0-questions.md:42` remain reported-not-absorbed, unchanged from round 64."

Pointers resolved:

```
$ grep -n "^tsukuroi" /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md
42:tsukuroi | round-1 | Ratify the explicitly steered fleet round-1 namespace after the historical lane-r11/training-r10 closeout, and arbitrate the kaidoku/revenger shipped-artifact overlap before an ADJ-06 analysis is routed? …
```

Line 42 is the open ADJ-06 kaidoku/revenger arbitration question (no `L0 ANSWER` marker on that line, unlike the answered line 53). So the cited L0 pointer is real and still open — the contest is *reported* at a resolvable line, not absorbed.

The "documented scope from S043 only" clause is accurate, not an absorption: `S043` (`corpus/SOURCES.md:57`) scopes itself to "route-scope sentences only … not provider execution on this host, not the authored fixture bytes", and the S043 snapshot really does carry the JADX prerequisite the entry names:

```
$ grep -n -i jadx .ufo/waves/round-65/source-snapshots/rea-android-applications.md
16:The provider requires a separately supplied headless JADX MCP JAR 0.7.1 and
17:Java 17 or newer. `REA_JADX_MCP_JAR` selects the absolute JAR path; `JAVA_HOME`
```

Non-absorption is also declared in the coverage line (10): "Not covered: … provider (`inspect_android_package`) readiness or output". The lane's own map row `corpus/README.md:34` is `C05 | Android packages (APK) … uncovered`, so the entry claims no sibling ground.

**Scope-prose delta vs the v3 candidate is nil.** Programmatic section compare against `corpus/knowledge/round-68-apk-axml-byte-evidence.md`:

```
## Limitations IDENTICAL
## Cross-lane scope note (Q10) IDENTICAL
```

The v4 repair bundle therefore neither widened nor narrowed the Q10-carrying prose; it is the same text that the round-68 Q10 seat passed (`.ufo/waves/round-68/R68ReviewEntryQ10.md:1`: "PASS — Q10: every finding … is scoped to one authored APK fixture, one manual stdlib readout … no single-fixture observation is stated as a universal").

## 5. Residual risks (reported, outside this criterion / not a Q10 FAIL)

These do not satisfy Q10's reject trigger; they are handed to the seats that own them rather than absorbed into this verdict.

- **R1 — registry row anchor range contradicts the entry's (Q01/Q02 surface).** `corpus/SOURCES.md:52` (S038) lists "chunk-type enum **:239-250**", while entry line 1 and item 4 (line 52) state the block runs **237-263** with `RES_XML_RESOURCE_MAP_TYPE` at **:253**, and the derivation prints `enum block close : 263` / `enum RES_XML_RESOURCE_MAP_TYPE : 253`. The entry's numbers are the snapshot's bytes (verified in §1); the registry row's range cannot contain :253 and is stale. The same row's state/date columns still read `mined | 2026-10-24`, while entry line 1 says the row was "**re-opened 2026-10-25** by this entry's author". Correct value for the row's anchor would be the derived `:237-263` (open/close) plus `:253` for the resource-map enum; the Q01/Q02 seats should decide whether the header's re-open claim is required to land in `SOURCES.md`.
- **R2 — v4 §Q-map dropped the Q10 row the v3 carried (self-map surface).** `round-69` §Q-map (lines 173-184) has 8 rows: Q01, Q02, Q04, Q05, Q07, Q11, Q13, Q14. The round-68 v3 map carried 13 rows including `| Q10 | pass | scope is one fixture, one operation (manual readout), one artifact version …` (`round-68-apk-axml-byte-evidence.md:181`). Q03, Q06, Q08, Q09, Q10 and Q12 are absent from the v4 map. The criterion still holds on the bytes, and this seat must not treat a map row as evidence, but the entry no longer self-declares Q10 while `claims.md` §C1's predicate reads "every applicable Q01–Q15 decision of the dispatched wave on the landed v4 bytes is PASS". Adjudicator should record Q10 from this seat's report, not from the entry.
- **R3 — cross-lane note is thinner than the round-64 accepted note (depth).** `round-64-firmware-region-byte-evidence.md:203` names kaidoku's live surface and tsukuroi's plane with `file:line` pointers. The v4 note names ADJ-06 + `l0-questions.md:42` and fences the S043 provider route, but does not name kaidoku's live APK surface, which exists: `kaidoku-shokunin/PROVINCE.md:56` — "APK surface (full) | `rea inspect-artifact` content graph; `inspect-android-package` (jadx-headless-mcp 0.7.1); `decode-android-resources` (apktool 3.0.3); `search-android-classes`…". The entry does not absorb it (coverage line 10 excludes provider readiness/output), so Q10 holds; naming that surface would strengthen the report.
- **R4 — `ZIP_STORED` premise has no in-entry derivation (Q06/Q11 surface).** The readout prints only sizes (`416/416`, `112/112`, `69/69`), never the compression method; a reader cannot re-derive "ZIP_STORED with no data descriptors" from the embedded output. I verified it true independently (method `0` ×3, flags `0x0000`, bit 3 clear), so the statement is correct — the gap is that no embedded command prints it. Q06 ("an offset, operand, size or count is stated from intent rather than from the built bytes") owns this, not Q10.

## 6. Verification gaps

- I did not run `reports/round-69/measure.py`, the wave, or the C7 gate; I read no `corpus/README.md` flip state beyond `:34` (which still reads `uncovered`, consistent with `admission-status: candidate`).
- I did not re-audit Q01-Q09/Q11-Q15. I used `SOURCES.md` only for the rows' own scope/version text (S032/S034/S038/S041/S043/S047) and for R1's registry-range comparison.
- No LSP server answers Markdown corpus files here, so pointer resolution was done with `read`/`grep`/`sed` and direct byte reads; every number above is from a command whose output is quoted.

## Verdict

**PASS (Q10).** Scoping prongs A (family/operation/version/input), B (§Limitations truthful on the built bytes) and C (ADJ-06 / `l0-questions.md:42` reported, provider route fenced, coverage row not flipped) all hold on the v4 bytes. Nothing in the entry states a single-fixture observation as a universal. R1-R4 are reported for other criteria and do not move this decision.
