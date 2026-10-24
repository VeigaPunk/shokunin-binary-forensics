FAIL — tier inflation found on two of the four rows: S038 is cited outside its declared scope and recorded anchors (`round-65-apk-axml-byte-evidence.md:71`, `:126`), and the DEX-header field semantics at `:103` rest on no registry row (S041, the only row whose scope touches item 9, is bounded by its own scope cell to "byte/oracle correspondence only"); S039 is clean, S040's `queued`/non-load-bearing status is contradicted by its own row text and by the oracle provenance.

Seat: R65ReviewSourcesTier (read-only leaf). Target: `corpus/SOURCES.md:52-55` (S038-S041) vs their citation sites in `corpus/knowledge/round-65-apk-axml-byte-evidence.md`. All paths below are absolute from `/home/vgpnk/Projects/shokunin/revenger-shokunin`; evidence is the working tree, not a committed archive (see Verification gaps).

## Method and grounding

Tooling: no `lsp` device is exposed in this seat's toolset, and no LSP server answers Markdown or the registry table, so every caller/citation check here is literal text search (`grep`/`sed`), never semantic proof. Absence claims are stated as grep-bounded, not as semantic absence.

```
$ sha256sum corpus/fixtures/apk-r65/* .ufo/waves/round-65/source-snapshots/*
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk
eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a  corpus/fixtures/apk-r65/generator.py
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  corpus/fixtures/apk-r65/truth.json
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  .ufo/waves/round-65/source-snapshots/ResourceTypes.h
412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c  .ufo/waves/round-65/source-snapshots/rea-android-applications.md
e7fe6715126a3be8e6ea7ca4d3dc2d8713b6c979bde13f8fa9d6c458a3c49c6a  .ufo/waves/round-65/source-snapshots/zipfile-docs.html
```

All four snapshot/fixture digests equal the digests stated in the registry rows (`SOURCES.md:52-55`) and in `round-65-apk-axml-byte-evidence.md:3`. The entry's recheck reproduces:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/r65_readout.txt; echo "exit=$?"; wc -l < /tmp/r65_readout.txt; sha256sum /tmp/r65_readout.txt
exit=0
15
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  /tmp/r65_readout.txt
```

That matches entry:156-158 (15 lines, sha256 `507d79f8…`) exactly. README C05 is still unflipped: `corpus/README.md:34` = `| C05 | Android packages (APK) | — | — | frontier |`.

## Findings, by severity

### S1 — DEX declared-header field semantics rest on no registry row; S041 is used outside its declared scope
- Citing sentence: `corpus/knowledge/round-65-apk-axml-byte-evidence.md:103` — "Its declared checksum **`0x3d120c30`** equals the Adler-32 recomputed over the bytes from offset 12 on, and its declared 20-byte signature equals the SHA-1 recomputed over the bytes from offset 32 on. The header's `file_size` and `header_size` are both 112 and the endian tag is `0x12345678`."
- The entry's own basis claim: `:141` (Q01) — "every load-bearing layout claim rests on S038 … for AXML scope; container offsets rest on S032/S034 … and the fixture's own bytes (S041 …)". Item 9's field layout is in none of those three scopes: S038 is AXML-only (`SOURCES.md:52` scope cell: "field layout of the compiled-XML (AXML) chunk, string-pool, node, attribute and value structures"), S032/S034 are ZIP container records, and the fixture's bytes cannot certify what offset 12/32/40 *mean* — the same author wrote `generator.py`, `readout.py` and `truth.json`.
- No DEX-format source exists in the registry: `grep -in dex corpus/SOURCES.md` returns only incidental hits (`index`) plus S041; `grep -rln 'dex format\|dex-format\|dalvik' corpus/` returns nothing. The fixture scripts also cite no DEX documentation: `grep -n 'https\?://' corpus/fixtures/apk-r65/{generator,readout}.py` yields only the `schemas.android.com` namespace URI in `generator.py:39`.
- S041's declared scope cell (`SOURCES.md:55`) is "byte content of one authored 947-byte APK fixture … **byte/oracle correspondence only**, not install validity, dex validity, provider accuracy or completeness". Using it as the authority for third-party format field names/semantics is exactly the tier-A-outside-scope shape: the row can support "these bytes are what the oracle declares", not "offset 12 is the Adler-32 field".
- Consequence for the judged axis (coverage): Q01's pass basis at `:141` is incomplete as written — one of ten numbered observations (item 9, the dex member) has no tier-A source. Fix is a registered DEX-format row (or relabel item 9's field names as fixture-authored inference and drop them from the "load-bearing layout claim" set). The round's own M38 class is the same shape: "layout constants stated from intent, not built bytes" (`corpus/lessons/round-65.md:29`).

### S1 — `getAttributeNameResID` semantics attributed to S038, outside its scope and its recorded anchors
- Citing sentence: `corpus/knowledge/round-65-apk-axml-byte-evidence.md:71` — "Seven entries are `0x00000000` — S038's `ResXMLTree::getAttributeNameResID` semantics make 0 \"no resource id\" — and the entries for `versionCode` and `versionName` are **`0x0101021b`** and **`0x0101021c`**".
- S038's declared scope is field layout only (`SOURCES.md:52`), and its `teaches` cell enumerates "the chunk-type values, the 8/16/20/28-byte fixed structure sizes, the UTF8 flag bit and the attributeStart/attributeSize semantics" — method return semantics are not in the row.
- The anchor does not contain the claim: the snapshot's sole `getAttributeNameResID` occurrence is a bare declaration with no comment —

```
$ grep -n 'getAttributeNameResID' .ufo/waves/round-65/source-snapshots/ResourceTypes.h
792:    uint32_t getAttributeNameResID(size_t idx) const;
```

  and S038's recorded anchors are `:218, :239-250, :461, :612, :621, :677, :707, :287` (`SOURCES.md:52`) — `:792` is not among them. The nearby "0 means…" prose in the snapshot belongs to other structures (`:914` base package, `:1405`/`:1461` "resource identifier … 0 is invalid"), never to this method or to the resource-map array.
- The sentence also names the wrong API for the thing described: item 7 is reading the `RES_XML_RESOURCE_MAP_TYPE` chunk (a plain `uint32_t` array; snapshot `:250-254` says only "mapping strings in the string pool back to resource identifiers. It is optional"), not an attribute accessor.
- Not labeled as inference (`:126` lists a different inference set), so it reads as spec-backed. Either drop the gloss, or state it as "the fixture declares these ids; a 0 entry carries no id in this authored map" (fixture-scoped, S041-safe).

### S2 — S040 is not "honestly non-load-bearing" as registered
- Row state: `SOURCES.md:54` has `status = queued`, `used-by = —`, yet its `teaches` cell says "Documents the module-level reader scope **used only as a cross-check in this round's container walk**". A `queued` row with an asserted use is internally inconsistent under the file's own contract ("only `status`, `recheck` and `used-by` change in place; every row below was opened … by the round that wrote it").
- The stated use is real and one-directional, not a symmetric cross-check: `corpus/fixtures/apk-r65/generator.py:172-187` (`parse_members()`) opens the finished APK with `zipfile.ZipFile(...).infolist()/.read()` and writes `local_header_offset`, `compressed_size`, `crc32`, `sha256` into `truth.json` `members[]` (verified in `truth.json`, e.g. `classes.dex`: `local_header_offset 465`, `crc32 2635c82a`, `compressed_size 112`). The entry then compares the struct walk against exactly those fields: `round-65-apk-axml-byte-evidence.md:121` — "The readout values agree with it on every shared field: … the three members' local-header offsets, payload sizes and CRC-32 values (item 3)".
- So the oracle's member fields are a second parser's output (zipfile), not authored intent; `truth.json` mixes both (authored `axml_declared`, measured `members`). The entry's Q03 sentence (`:143`, "expected values come from the authored oracle and from S038-derived struct widths fixed outside the record under test") therefore omits that one expected-value family was produced by a tool parse of the same bytes.
- Honesty verdict: the row's *tier* A is correct (primary module docs), but its status is not. Either S040 becomes `mined` with `used-by corpus/knowledge/round-65-apk-axml-byte-evidence.md` and the oracle provenance is declared in the entry, or the row must stop asserting a use and the member expected values must come from the authored layout rather than zipfile. `corpus/lessons/round-65.md:14`'s "honestly non-load-bearing" is contradicted by `SOURCES.md:54`'s own sentence. Note the entry never cites S040 and `readout.py` imports no zipfile (`readout.py:13-18`: hashlib, json, struct, sys, zlib, pathlib), so no entry sentence is void — the defect is registry/oracle honesty, not a false readout.

### S3 — `0xffffffff` null-index inference promises an S038 anchor the snapshot does not contain
- `round-65-apk-axml-byte-evidence.md:126` — "Each inference cites its byte evidence **and its S038 anchor**" — but the `0xffffffff` null string-pool index has no S038 anchor: `ResStringPool_ref`'s struct comment (`ResourceTypes.h:430-436`) is silent on any null value, and the only `0xFFFFFFFF` constants are `ResStringPool_span::END` (`:498`, with its own comment at `:502`) and `NO_ENTRY` (`:1456`) — both unrelated structures.
- Also double-labeled: stated flat in §Observation at `:85` ("is the `ResStringPool_ref` null index") and again as inference at `:126`. Keep it in one place, as inference, without the S038-anchor promise.

### S3 — Dangling header pointer for S041
- `:3` — "registry id assigned by L1 at the round-65 append — **row text in §Sources**". There is no `## Sources` section in the entry (headings at `:9,13,119,123,129,133,137,154`); the row text is `corpus/SOURCES.md:55`. Q02 asks for resolvable provenance pointers; this one does not resolve.

### S3 — header `source:` set omits S032/S034 although item 3 rests on them
- `:33` cites "46-byte fixed part per S032 §4.3.12" and "30-byte fixed part per S034 §4.3.7", but the header's `source:` lines list only S038, S039, S041 (`:1-3`), and `:142` (Q02) describes the header as carrying "S038, S039, S041". Not inflation — S032/S034 are `mined` tier-A rows (`SOURCES.md:47-48`) with the cited sections in their anchor cells — but the header is incomplete against the entry's own citations.

## Clean results (checked, no inflation)

- **S039 is used strictly inside its route-scope-only scope.** Exactly four occurrences: `:2` (header source line restating "route-scope sentences only"), `:135` ("The provider route (`inspect_android_package`, JADX prerequisites) is documented scope from S039 only; this lane ran no provider and makes no readiness claim"), `:142` (Q02 provenance), `:145` (Q05 fence). No entry sentence takes an AXML/ZIP/DEX format fact from S039. The snapshot confirms the cited material is route/prerequisite prose: `rea-android-applications.md:7-8` (what `inspect_android_package` takes and returns) and `:16-20` ("The provider requires a separately supplied headless JADX MCP JAR 0.7.1 and Java 17 or newer" … "REA setup does not install or configure that JAR"). `SOURCES.md:53`'s "route-scope sentences only … not provider execution on this host, not the authored fixture bytes" is honored.
- **S038's format items are in scope and accurate.** Chunk-type enum verified at `ResourceTypes.h:237-254` (`RES_STRING_POOL_TYPE 0x0001`, `RES_XML_RESOURCE_MAP_TYPE 0x0180`, `RES_XML_START_NAMESPACE_TYPE 0x0100`, `:0x0102`, `:0x0103`, `RES_XML_END_NAMESPACE_TYPE 0x0101`) matching entry `:53`; `UTF8_FLAG = 1<<8` at `:477-480` matching entry `:64`; struct widths 8/28/16/20/20/8 derivable from `:461-490` (`ResChunk_header` + five `uint32_t`), `:612-621`, `:677`, `:707`, `:287` matching entry `:55-59`; `attributeStart 20`/`attributeSize 20` matching entry `:80`. All are inside S038's declared scope and its `teaches` cell.
- **S041's fixture/oracle/script bytes check out inside its byte scope.** All four digests match both `SOURCES.md:55` and entry `:3` (sha256 table above), and the readout reproduces exit 0 with the claimed 15-line stdout digest. The entry's negatives stay inside the row's exclusions: `:127` "nothing about install validity, signature blocks, dex program validity or any provider's behavior is claimed".
- **No premature admission.** C05 remains `frontier` (`corpus/README.md:34`); the entry's `admission-status: candidate` and `corpus/lessons/round-65.md:20-22` both say the Q-map is draft, not the admission.

## Residual risk

- The two S1 findings are *bounded*: the AXML core (items 2-8) is correctly sourced and byte-verified, and the readout reproduces. If L1 wants C1 admitted this round, the smallest honest repair is (i) a registered DEX-format row covering item 9's field layout, or item 9 relabeled as fixture-authored layout inference with the "load-bearing layout claim" wording in `:141` narrowed; (ii) delete or inference-label the `getAttributeNameResID` gloss at `:71`. Neither repair changes any measured value.
- S040's status fix is bookkeeping, but it changes a claim the lesson already made in print (`corpus/lessons/round-65.md:14`), so it needs an L1 adjudication line rather than a silent edit.
- I did not audit C2, the frozen counter, README/SHONEN flips, or the lesson's M37/M38 receipts — other seats' lanes.

## Verification gaps

- **No `lsp`**: this seat's toolset exposes no `lsp` device and no LSP server answers Markdown/registry tables; all caller/citation checks are literal text search. The one absence claim that matters ("no DEX-format source row exists") is bounded by two independent greps (`grep -in dex corpus/SOURCES.md`; `grep -rln 'dex format\|dex-format\|dalvik' corpus/`) over the working tree, not a semantic reference search.
- **Working tree, not a committed archive**: the brief says measurements belong to committed trees; I read the working tree (per the seat's read-only bounds I do not run `git archive` or any repo mutation). Every digest I cite was cross-checked against the frozen registry and entry text, so a later commit that changes these bytes will invalidate the pointers — re-run this audit on the final tip's archive.
- Time-box: single pass, no second reviewer corroboration of the S038 `:792` reading; the snapshot is the only S038 artifact available (no network re-open in-seat).

## Tooling record

No installs or upgrades were performed (nothing needed; no pacman transaction attempted, per the host-wide pacman pause).
