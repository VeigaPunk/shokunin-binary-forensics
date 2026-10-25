# R70W2GateQ01 — Q01 admission review (round-70 C05 v5.1 candidate)

**PASS — every `source:` row the entry cites (S032, S034, S038, S041, S047, S048, S049) exists in `corpus/SOURCES.md` at lane commit 17ee7f87 with exactly the stated tier, scope, status and opened date; S048 supersedes S045 and S049 supersedes S043, both opened 2026-10-25; all seven cited rows are tier A, none is tier C, so no load-bearing claim rests on a tier-C row.**

Target: `corpus/knowledge/round-70-apk-axml-byte-evidence.md` at lane commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd`, `admission-status: candidate` (entry blob sha256 of the extracted file: `819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31`). Judged bytes extracted via `git show`/`git archive` at that commit; the working tree was not read for any judged value.

Note on method: no LSP device is present in this seat's tool inventory and no language server covers a markdown corpus, so every check below is a direct read of the landed commit bytes — the recorded fallback, not a semantic claim from grep.

## 1. Registry rows verified against the entry's header claims

All commands run against `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin show 17ee7f8…:corpus/SOURCES.md` (file extracted to scratch; row lines cited from that extraction, S0NN sits at file line NN+14).

| id | entry header claims (entry.md lines 1-7) | registry row (landed bytes) | verdict |
|---|---|---|---|
| S038 | spec, tier A; opened 2026-10-24, mined round 65; re-opened 2026-10-25; scope: struct layout + chunk-type enum values of the AXML chunk stream for one authored manifest | `SOURCES.md:52` — spec, **A**, scope "field layout of the compiled-XML (AXML) chunk, string-pool, node, attribute and value structures for one authored binary `AndroidManifest.xml`, this tag only", status `mined`, opened **2026-10-24**, `used-by` includes `corpus/knowledge/round-70-apk-axml-byte-evidence.md` | match |
| S032 | spec, tier A; opened 2026-10-23, mined round 63; re-opened 2026-10-25; scope: §4.3.12 central-directory file header + §4.3.16 EOCD record layouts | `SOURCES.md:46` — spec, **A**, scope "central directory file header and end-of-central-directory record field layout for one authored ZIP archive…", `mined`, **2026-10-23**, used-by includes the round-70 entry | match |
| S034 | spec, tier A; opened 2026-10-23, mined round 63; scoped re-open 2026-10-25; scope: §4.3.7 local file header only | `SOURCES.md:48` — spec, **A**, scope "local file header record field layout…: signature value, fixed 30-byte record part, file name length and extra field length offsets", `mined`, **2026-10-23**, used-by includes the round-70 entry | match |
| S041 | own-work, tier A; opened 2026-10-24, mined round 65 | `SOURCES.md:55` — own-work, **A**, scope "byte content of one authored 947-byte APK fixture… byte/oracle correspondence only…", `mined`, **2026-10-24**, used-by includes the round-70 entry | match |
| S047 | own-work, tier A; opened 2026-10-25 (round 69); **supersedes S046** | `SOURCES.md:61` — own-work, **A**, scope "machine derivation of every S038 line number and enum value the round-69 C05 v4 candidate cites…; the layout facts themselves rest on S038", teaches "**supersedes S046**…", `mined`, **2026-10-25**, used-by includes the round-70 entry | match |
| S048 | docs, tier A; opened 2026-10-25; **supersedes S045**; scope: declared `header_item` field semantics (checksum, signature, header_size, endian_tag) of one authored `classes.dex` | `SOURCES.md:62` — docs, **A**, scope "the declared `header_item` field semantics (checksum, signature, header_size, endian_tag) of one authored `classes.dex` member; not dex program validity", teaches "**supersedes S045** — corrects its located-quote locator…; the four quoted phrases are unchanged", `mined`, **2026-10-25**, used-by: the round-70 entry | match |
| S049 | docs, tier A; opened 2026-10-25; **supersedes S043**; scope: the route-scope sentence only | `SOURCES.md:63` — docs, **A**, scope "route-scope sentences only: what `inspect_android_package` is documented to take and return…; not provider execution on this host, not the authored fixture bytes", teaches "**supersedes S043** — adds the canonical URL…; the located sentence is unchanged", `mined`, **2026-10-25**, used-by: the round-70 entry | match |

Superseded predecessors exist and are correctly retired from support: S045 at `SOURCES.md:59` (opened 2026-10-24, used-by round-67 entry only) and S043 at `SOURCES.md:57` (opened 2026-10-24, status `queued`). The supersession convention matches the registry's precedent rows (S024 "supersedes S008", S044 "supersedes S040").

## 2. Tier-C clause

Tier-C rows in the landed registry: S012 (`community`, C, `rejected`, `SOURCES.md:23`) and S025 (`community`, C, `rejected`, `:36`). Neither is cited anywhere in the entry; no load-bearing claim rests on a tier-C row, and no cited row carries status `rejected` or `queued`.

## 3. Re-derivation (entry's own commands, run by me from `git archive 17ee7f8…` extraction)

Scratch extraction: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd corpus | tar -x -C <scratch>`.

1. `python3 -B corpus/fixtures/apk-r65/entry_checks.py --pins` — stdout is byte-identical to the entry's item-14 block, all ten lines, including the four snapshot digests the registry anchors cite: `ResourceTypes.h 56b88bc4…` (= S038/S047 anchor), `APPNOTE.TXT 0b993022…` (= S034 anchor "snapshot lines 387-399, sha256 0b993022…"), `dex-format.html c0428612…` (= S048/S045 anchor), `rea-android-applications.md 412d9cb4…` (= S049/S043 anchor), and `corpus/derive_axml_anchors.py 74d4c0d9…` (= S047's script digest). The entry's item-14 digest claims and the registry's anchor digests agree line for line.
2. `python3 -B corpus/derive_axml_anchors.py` — reproduced the entry's item-11 first block exactly (20 lines: sha256 line, 7 struct lines, enum block 237-263 with `RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100`, `comment attributeStart : 686`, `field attributeStart : 687`). S047's claimed re-open "by running it" is real on the landed bytes.
3. `python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes` — reproduced the entry's item-11 second block exactly (6 MATCH lines): the S049 sentence at snapshot first line 7 (raw snapshot lines 7-8 carry "Start with `inspect_android_package` on the caller's APK path…"), the four S048 phrases at dex-format.html lines 5949/5956/5981/5035, and S038's `attributeStart` comment at ResourceTypes.h:686. Every quoted phrase is present in the committed snapshot the cited row anchors.
4. Item-7 scope check (the one S038 claim the entry itself flags as not machine-anchored): ResourceTypes.h snapshot lines 252-253 read "This contains a uint32_t array mapping strings in the string pool back to resource identifiers." immediately above `RES_XML_RESOURCE_MAP_TYPE = 0x0180` (line 253, matching item 4's decimal 384). The cited text states the array layout, so item 7 does not exceed S038's registered scope.

## 4. "Opened in the round that wrote it"

S047/S048/S049 — the rows this round's repairs created — were opened 2026-10-25 (round 70's date), as required. S032/S034 (2026-10-23), S038/S041 (2026-10-24) are older rows; the entry discloses this in each header line and claims a re-open on 2026-10-25 by the entry's author from the committed snapshots whose digests item 14 re-derives (verified above). The frozen contract (`reports/round-70/claims.md` §Frontier step) declares exactly this: "re-opened this round". The stated opened dates match the registry in every case; no date, tier, scope or status claim in the entry's header is contradicted by the landed registry.

## 5. Residual observations (non-failing)

- `entry.md` item 9 says the undeclared-semantics dex fields are "printed without a quoted S045 phrase" — a leftover reference to the superseded id where S048 is meant. It explicitly claims no semantics from S045, so no load rests on the superseded row; prose residue only.
- `claims.md` §C1's admission sentence names S043/S045 while the landed entry cites S048/S049; `claims-amendment-A1.md` records the supersession as intended treatment ("S048/S049 rows supersede the S045/S043 locators") and `claims.md` is blob-frozen by design. Not an entry defect; the kill rule judges the entry bytes.
- A1's C1 conjunct ">= 5 `source:` S-ids that exist in `corpus/SOURCES.md` at tier A" is satisfied by this review's §1/§2 result: 7 ids, all present, all tier A.

## Verdict

**PASS** on Q01 for the landed candidate bytes at `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd`. Evidence: §1 table (all 7 rows), §2 (no tier-C support), §3 (item-14 and item-11 derivations reproduced exactly from the archive extraction), §4 (dates/supersessions verified).

Scratch (`/tmp/revenger-r70-R70W2GateQ01*`) deleted after this report was written. No lane file was edited.
