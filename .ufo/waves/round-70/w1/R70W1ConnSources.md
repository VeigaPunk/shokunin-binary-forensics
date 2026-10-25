# R70W1ConnSources — cross-source pattern scan (seat report)

Verdict: **PATTERNS-REMAIN** — the v5 candidate carries two of the four recurring defect patterns (folded-HTML quote locating; source rows opened by the entry's author) and has repaired the other two (hand-typed line numbers; digests pinned outside corpus/). ADJ-06 kaidoku/revenger overlap: the entry absorbs nothing (Q10 fence only).

Scope: C05 v5 candidate at lane commit `aa1842fac199aa524930e5565ed3715de5f84c6d` (file `corpus/knowledge/round-70-apk-axml-byte-evidence.md`, `admission-status: candidate`), items 11-12 + source block; rejected candidates round-65/67/68/69; `PROVINCE.md`; fleet `.ufo/l0-questions.md` row 42 (ADJ-06). All commands ran in a sandbox `git archive aa1842f` extraction at `/tmp/revenger-r70-R70W1ConnSources-D3My` (scratch, deleted before return).

## Pattern 1 — line numbers typed by hand (M40 class; r65 Q02 `:244` vs `:245`, r67 Q02 recurrence) → REPAIRED

`corpus/derive_axml_anchors.py` (v5) is search-based: `find_unique` (lines 74-80) + `enum_block_bounds` (lines 83-98) + `VALUE_RE` (line 66); exits 2 on missing/ambiguous symbol or digest mismatch (lines 28-30, 69-71). I ran it in the sandbox; output is byte-identical to the embedded item-11 block and prints every S038 ref the entry body states:

```
$ python3 -B corpus/derive_axml_anchors.py   (rc=0)
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
```

Cross-check (script over the entry bytes): the set of S038 line refs in the entry body `{218,237,239,241,244,245,246,247,248,253,263,287,461,612,621,677,686,687,707}` ⊆ derive output. The r68 Q04 FAIL (`:237`/`:244` stated, never printed) and r67 Q02 FAIL (`:244` twice) cannot recur: the script now prints both and exits 2 on absence. The `--spec-quotes` "first line N" values are also machine-located (first three words per raw line, `entry_checks.py:187-188`).

## Pattern 2 — quotes from folded HTML → REMAINS (mechanism; disclosed; low-risk content)

`entry_checks.py:178-179`: `fold(text) = re.sub(r"\s+"," ", re.sub(r"<[^>]+>","",text)).strip()`; `spec_quotes()` (lines 182-191) matches each phrase only in this folded text. Verified against the committed snapshot `corpus/snapshots/dex-format.html`:

```
# raw substring counts (no tag strip):  checksum phrase=0, signature phrase=0, header_size phrase=0, ENDIAN phrase=1
# tag-stripped newline-preserved counts: checksum=0, signature=0, header_size=0, ENDIAN=1
```

Three of the four S045 quotes exist **nowhere verbatim** — not in raw HTML, not even after tag-stripping with newlines preserved; they exist only after whitespace collapse. Raw context (`dex-format.html:5948-5956`):

```
|   <td>adler32 checksum of the rest of the file (everything but
|     <code translate="no" dir="ltr">magic</code> and this field); used to detect file corruption
|   <td>SHA-1 signature (hash) of the rest of the file (everything but
|     <code translate="no" dir="ltr">magic</code>, <code ...>checksum</code>, and this field); used
```

Folded-context check: `adler32 checksum of the rest of the file (everything but magic and this field); used to detect file corruption signature ubyte[20] SHA-1 signature …` — each phrase is a faithful segment of the rendered table cell (inline `<code>` spans, intra-cell line wraps); no fabricated cross-cell joins were found. The tool discloses the folding ("folded phrase present=True") and the reported "first line" (5949/5956/5981) locates only the phrase's first three words, which span source lines. So: pattern persists by construction, but each quote is honest rendered text, labeled, and single-cell. The S043 quote (`rea-android-applications.md:7`) and S038 comment (`ResourceTypes.h:686`) ARE verbatim in their snapshots — confirmed by `sed -n '7p'` / `sed -n '686p'`.

## Pattern 3 — digest pinned to a path outside corpus/ → REPAIRED for the entry

v5 item 14 (`--pins`) prints digests for corpus-relative paths only; all four spec snapshots are now committed copies under `corpus/snapshots/`, byte-exact to the lane's earlier outside-corpus pins (digests match the old stores): `ResourceTypes.h` 56b88bc4…, `APPNOTE.TXT` 0b993022…, `dex-format.html` c042861…, `rea-android-applications.md` 412d9cb…. The old outside-corpus paths (`.ufo/waves/round-65|67/source-snapshots/…`) still appear in SOURCES rows S038/S045/S046/S047 as provenance history — not in the entry. No v5 digest references a path outside `corpus/`.

## Pattern 4 — rows opened by the same author who writes the entry → REMAINS (explicit, admitted)

The v5 source block declares every cited row re-opened 2026-10-25 "by this entry's author": S038, S043, S045, S032, S034, S047 (S041 is own-work); only S047/S041 are lane-authored rows, but the re-opening record is single-author. SOURCES currently lags the build: `S043 status=queued, used-by=—`; `S045 used-by=round-67…`; `S038/S041 used-by=round-65…`; `S047 used-by=round-69…` — i.e., none re-pointed to the v5 candidate yet (claims.md re-points S045 used-by old→new at admission). This is the designed independence caveat: wave-2 fresh seats (Q01-Q15) are the mitigation, and the mechanical lint/gate already pass on the candidate bytes (below).

## ADJ-06 (kaidoku/revenger shipped-artifact overlap) — absorbs nothing

- Fleet `.ufo/l0-questions.md` row 42 (tsukuroi, round-1): "arbitrate the kaidoku/revenger shipped-artifact overlap before an ADJ-06 analysis is routed? Evidence: tsukuroi-shokunin/corpus/knowledge/adjacency-handoffs-fleet-r1.md sections 1-2 and its JSON source pins."
- v5 entry: the only kaidoku mention is the Q10 fence note — "The kaidoku/revenger ADJ-06 overlap and the fleet `l0-questions.md` entry for it stay reported, not absorbed."
- Entry URLs are exactly the three tier-A sources: AOSP `ResourceTypes.h`, PKWARE APPNOTE.TXT, source.android.com dex-format (plus the `http://schemas.android.com/…` URI inside a command-output block, which is data). Scope is the authored `apk-r65` fixture (own-work S041), not a shipped artifact; nothing from kaidoku's corpus (which does host APK/REA knowledge, e.g. `2026-10-13-r3-apk-inventory.md`) is cited or copied.
- Province note: `PROVINCE.md` owns reverse engineering of shipped artifacts generally, so the province-level overlap question stands open (ADJ-06); the C05 candidate itself is not the overlap — it is fixture/own-work and says so.

## Mechanical state of the candidate bytes (all in sandbox, rc=0)

```
$ python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md
LINT_QMAP=0 / LINT_Q14=0 / LINT_Q15=0 / LINT_HEADER=0
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md
checked_blocks=22 problems=0
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes   # 6 MATCH lines, matches embedded block
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout    # 3 sums + 15 MATCH lines
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --oracle        # 28 MATCH lines
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --eocd          # eocd signature bytes at offset 925: 504b0506 (4 bytes)
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --stdout-digest # readout stdout: 15 lines, sha256 507d79f8…
$ python3 -B corpus/fixtures/apk-r65/readout.py | wc -l              # 15
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --pins          # 9 corpus-relative digest lines
q14: no `…` ellipsis run anywhere in the entry (grep: 0 hits); the only prose byte-count on a hex run is the item-3 "32-hex-character run, which is 16 bytes" (verbatim correct).
README C05 row at aa1842f still `uncovered`; entry header `admission-status: candidate` — landing-order step 1 state.
```

## Where v5 still carries the patterns (list)

1. Folded-HTML quote locating (P2) — `entry_checks.py:178-188`, S045 quotes only exist post-folding (3/4); disclosed but mechanical.
2. Same-author source-row re-opening (P4) — source block lines of the entry ("re-opened 2026-10-25 by this entry's author"); SOURCES rows not yet re-pointed (S043 queued; S045 used-by stale).
3. (Borderline) SOURCES row anchors still name outside-corpus snapshot stores for provenance — not an entry defect; admission-time re-point expected.

Repaired in v5: all hand-typed spec line numbers (P1, incl. r68 Q04 class), outside-corpus digest pins (P3), Q08 (`504b0506` now printed by `--eocd`), Q11 (recorded label + item-12 sums), Q14 (no ellipsis runs), Q15 (no git object id stated).
