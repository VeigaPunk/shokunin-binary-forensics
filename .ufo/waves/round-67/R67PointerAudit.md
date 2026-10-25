FAIL — one misresolving pointer (off-by-one): `RES_XML_START_NAMESPACE_TYPE :244` cited twice (entry:1, entry:56); snapshot `:244` is `RES_XML_FIRST_CHUNK_TYPE = 0x0100`, the named constant is `:245` (same value, wrong symbol). Every other file:line pointer resolves.

# R67PointerAudit — pointer audit of `corpus/knowledge/round-67-apk-axml-byte-evidence.md` (C1 v2 candidate)

Scope: every file:line pointer the entry makes. All paths below are under
`/home/vgpnk/Projects/shokunin/revenger-shokunin` unless absolute. "entry:N" =
line N of the v2 candidate (187 lines total, sha256 of audited tree = working
tree at audit time; entry is the committed build state).

## THE MISRESOLVING POINTER

- **`.ufo/waves/round-65/source-snapshots/ResourceTypes.h:244` cited for
  `RES_XML_START_NAMESPACE_TYPE` — resolves to the wrong symbol.**
  Snapshot (verified by `read`):
  - `:244` = `RES_XML_FIRST_CHUNK_TYPE          = 0x0100,`
  - `:245` = `RES_XML_START_NAMESPACE_TYPE      = 0x0100,`
  - `:246` = `RES_XML_END_NAMESPACE_TYPE        = 0x0101,`
  Both aliases carry the cited value `0x0100`, so the *value* claim is
  unfalsified; but the named-symbol-to-line mapping is wrong by one line.
  Occurrences:
  1. entry:1 (S038 source header): "`RES_XML_START_NAMESPACE_TYPE` :244"
  2. entry:56 (item-4 prose): "start/end namespace :244/:246"
  Note the end-namespace pointer `:246` is correct; only start-namespace is off
  by one. If the gate reads a pointer as "the named text appears at the named
  line", this is a dangling/misresolving pointer. If it reads "a constant with
  the claimed value exists at the cited line", it is value-correct via the
  alias. Either way it is a factual line-number defect the routed repair did
  not fix (the repair extended the span to :253 for RESOURCE_MAP but did not
  re-check the :244 start-namespace pin; the round-65 draft cited the same
  span :239-250 which included the correct :245 only implicitly).

## RESOLVED — `corpus/fixtures/apk-r65/readout.py` (sha256 `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976`, 11236 B — verified)

- `:99-105` payload_offset derivation (entry:34) — `:99` `lh_name_len = u16(apk, lh_off + 26)`, `:100` `lh_extra_len`, `:105` `payload_off = lh_off + 30 + lh_name_len + lh_extra_len`. RESOLVES.
- `:166` UTF-8 flag test (entry:66 cites `flags & 0x100`, readout.py:166) — `:166` `utf8=bool(flags & 0x100)`. RESOLVES.
- `:200-203` attribute location comment + computation (entry:81) — `:200-202` comment "attributeStart is 'Byte offset from the start of this structure' … relative to the attrExt at base + 16, not to the chunk", `:203` `aoff = base + 16 + attribute_start + i * attribute_size`. RESOLVES.
- `:22` `0xffffffff` null treatment (entry:88) — `:22` `NO_INDEX = 0xFFFFFFFF`. RESOLVES (the definition line; the null-test itself is `:211` `None if ans == NO_INDEX` — :22 is the constant's seat, acceptable).

## RESOLVED — `.ufo/waves/round-65/source-snapshots/ResourceTypes.h` (sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`, 86255 B — verified)

- `:218` `struct ResChunk_header` ✓
- `:237` `enum {` opener ✓ (block runs to `};` at :263; all seven cited chunk types sit inside :237-253 as claimed)
- `:239` `RES_STRING_POOL_TYPE = 0x0001` ✓ · `:241` `RES_XML_TYPE = 0x0003` ✓
- **`:244` `RES_XML_FIRST_CHUNK_TYPE = 0x0100` — NOT `RES_XML_START_NAMESPACE_TYPE` (see above; named constant is :245)**
- `:246` `RES_XML_END_NAMESPACE_TYPE = 0x0101` ✓ · `:247` `RES_XML_START_ELEMENT_TYPE = 0x0102` ✓ · `:248` `RES_XML_END_ELEMENT_TYPE = 0x0103` ✓ · `:253` `RES_XML_RESOURCE_MAP_TYPE = 0x0180` ✓
- `:287` `struct Res_value` ✓ · `:461` `struct ResStringPool_header` ✓ · `:612` `struct ResXMLTree_header` ✓ · `:621` `struct ResXMLTree_node` ✓ · `:677` `struct ResXMLTree_attrExt` ✓ · `:707` `struct ResXMLTree_attribute` ✓
- `:685-687` attributeStart field text (entry:81) — `:686` "Byte offset from the start of this structure where the attributes start.", `:687` `uint16_t attributeStart;`. RESOLVES (entry drops the final period; text otherwise verbatim).
- attrExt doc comment (entry:81 quote "Appears header.headerSize bytes after a `ResXMLTree_node`") — verbatim at `:675` in the doc block above `:677`. RESOLVES.
- Supporting: `UTF8_FLAG = 1<<8` at `:480` (consistent with readout `flags & 0x100`; entry cites no line for it).

## RESOLVED — `.ufo/waves/round-65/source-snapshots/rea-android-applications.md` (sha256 `412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c`, 1992 B — verified)

- `:7-8` route-scope quote (entry:2): `:7` "Start with `inspect_android_package` on the caller's APK path for package", `:8` "identity, manifest declarations, coverage, and inline Evidence." — the quoted sentence is verbatim across the wrap. RESOLVES.
- `:5` = `older server.` — byte-exact; the entry's contrast note ("the round-65 draft cited 'line 5', which is `older server.`") is accurate. RESOLVES.

## RESOLVED — `.ufo/waves/round-67/source-snapshots/dex-format.html` (sha256 `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4`, 281157 B — verified)

Three quoted field texts (whitespace/markup-normalized, all found by grep):
1. checksum — `:5949-5951` "adler32 checksum of the rest of the file (everything but `magic` and this field); used to detect file corruption". Quote is a verbatim span of this cell. ✓
2. signature — `:5956-5958` "SHA-1 signature (hash) of the rest of the file (everything but `magic`, `checksum`, and this field); used to uniquely identify files". ✓
3. header_size — `:5981-5982` "must be 0x70 (112) bytes (v40 or earlier)" (the parenthetical is an inline `<span>`). ✓
- `ENDIAN_CONSTANT = 0x12345678` — verbatim at `:5035` ("uint ENDIAN_CONSTANT = 0x12345678;"). ✓
- Anchor text "File layout → header_item field table": `<h2 id="file-layout">` at `:4825` exists and its layout table rows `header`→`header_item` at `:4837-4838`; the field table itself is `<h3 id="header-item">` at `:5926` with the Name/Format/Description table opening `:5930`. RESOLVES (minor phrasing: the field table is under the "Items and related structures" h2 at `:5921`, not literally nested under the "File layout" h2 — the anchor's arrow reads as spec-navigation shorthand and both endpoints exist).
- `file_size` row is present in the same table (entry:106 claims declared file_size 112 = member length; the field exists in the table — verified via the table span :5930-5996).

## Fenced-block and `$ ` command count

- `grep '^\`\`\`'` → 28 fence lines = **14 fenced blocks** (open/close pairs at lines 22-25, 29-32, 36-43, 51-54, 60-63, 69-72, 76-79, 83-86, 90-93, 97-102, 108-111, 117-120, 162-164, 170-187).
- `grep '^\$ '` → **16 `$ ` command lines**: one per block for 12 blocks; the member block (36-43) carries three (`--fact member[AndroidManifest.xml]`, `--fact member[classes.dex]`, `--fact member[META-INF/MANIFEST.MF]`), the end-node block (97-102) carries two (`axml_end_element`, `axml_end_namespace`), and the full-stdout block (170-187) carries one.
- **Brief premise check:** the item brief says "16 fenced blocks each carry a `$ ` command line" — the factual count is **14 fenced blocks, 16 `$ ` command lines**. The `\`\`\`sh` block at :162-164 has **no** `$ ` prefix (first line `python3 -B corpus/fixtures/apk-r65/readout.py`). Under the C2 gate's declared parse rule (fenced blocks whose first line is `$ <command>`), that sh block is skipped — flagging for the gate reviewers in case the gate instead keys on every fenced block.
- Reproduce block fidelity: the 15 output lines at entry:172-186 are **byte-identical** to a fresh run (`diff` clean; the closing fence :187 was the only extra line in my slice).

## Other pointers verified

- **All six sha256 pins match** (`sha256sum`): fixture.apk `05d2280f…` (947 B ✓), truth.json `27303bae…`, readout.py `92e347c3…`, ResourceTypes.h `56b88bc4…` (86255 B ✓), rea-android-applications.md `412d9cb4…`, dex-format.html `c0428612…` (281157 B ✓).
- **recheck pointer** (`python3 -B corpus/fixtures/apk-r65/readout.py` from lane root): ran — exit 0, **15 stdout lines**, stdout sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — matches the entry's pinned digest exactly.
- `truth.json` `axml_declared.resource_ids` (entry:74) — `:26-36` array holds `0x0101021b` / `0x0101021c` at the positions aligning with strings `versionCode`/`versionName` (`:43-44`). RESOLVES.
- r65 candidate `entry:41` (entry:5, entry:45) — `corpus/knowledge/round-65-apk-axml-byte-evidence.md:41` does carry the drifted 15-byte `4d616e696673742d56657273696f6e` (readout prints the 16-byte `4d616e69666573742d…`). RESOLVES; v2's repair claim is accurate.
- `QUALITY.md:23` (entry:151) — the Q11 row, text begins "Supersedes Q08." RESOLVES.
- `corpus/README.md` C05 row (entry:7) — `README.md:34`, label "Android packages (APK)", status `uncovered`, knowledge column `—`, names only the retained rejected r65 candidate. RESOLVES.
- Registry rows (`corpus/SOURCES.md`): S032 `:46` (§4.3.12 anchor ✓), S034 `:48` (§4.3.7 ✓), S038 `:52`, S043 `:57` ("supersedes S039" consistent with entry:2), S045 `:59` (dex-format row ✓). (S038's registry row still shows the old `enum :239-250` anchor — that's the registry's text, not an entry defect.)
- `l0-questions.md:42` (entry:138, fleet path `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`) — the tsukuroi round-1 row asking to "arbitrate the kaidoku/revenger shipped-artifact overlap before an ADJ-06 analysis is routed". RESOLVES.
- Commit `c7b7cf98` (entry:5) — exists (`git cat-file -t` → commit, subject "round-65: candidates — apk-r65 fixture+readout, C05 candidate entry, S038-S041 rows…"). RESOLVES.
- Heading inventory: `#` ×1, `##` ×7 (Observation, Comparison with the authored oracle, Observation/inference/unknown, Limitations, Cross-lane scope note (Q10), §Q-map, Reproduce) — **no `### Code` pointer**, consistent with the admission-status note "dangling `### Code` pointer removed".
- Q08 row present in §Q-map (entry:151) as "superseded by Q11" ✓.

## Verdict detail

- Dangling/misresolving pointers: **1 distinct defect** — `RES_XML_START_NAMESPACE_TYPE :244` (twice: entry:1, entry:56); correct line is `:245`. Value-equivalent via the `:244` alias `RES_XML_FIRST_CHUNK_TYPE = 0x0100`.
- All other file:line pointers, line ranges, quotes, digests, commit ids and registry/oracle references resolve.
- Fenced-block count correction: 14 blocks (13 `$ `-led + 1 bare `\`\`\`sh`), 16 `$ ` command lines — not "16 blocks each with `$ `".

No tools installed; all checks used existing binaries (`grep`, `sha256sum`, `awk`, `diff`, `git cat-file`, `python3`).
Report: `.ufo/waves/round-67/R67PointerAudit.md`
