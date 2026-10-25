PASS (Q02) — the entry opens with seven `source:` rows (S038/S043/S045/S032/S034/S047/S041), then `verified-at:` 2026-10-25 and a runnable `recheck:`, names coverage row C05 against `corpus/README.md`, and every header source row resolves: all seven ids exist in `corpus/SOURCES.md`, every digest/path/anchor in those rows re-derives from the cited bytes (I ran each command), and no anchor is a bare homepage.

criterion: Q02 only (`corpus/QUALITY.md:14` — `source:` with its `S###` row / URL or path / exact anchor, `verified-at:` date or commit, `recheck:` command or citation, and the `corpus/README.md` coverage row it fills; reject when any header is missing or an anchor is a bare homepage; ticket clause: every header source row must resolve).
seat: `L1Revenger69.R69ReviewEntryQ02` (fresh, non-author review of the landed build) · witness: this seat.
target bytes: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-69-apk-axml-byte-evidence.md`
identity (my command, cwd = lane root):

```
$ sha256sum corpus/knowledge/round-69-apk-axml-byte-evidence.md
c1e7eaac9dba4c77e578c788755dec3e3499fd8795ad0e479c51b5be7deb11d5  corpus/knowledge/round-69-apk-axml-byte-evidence.md
$ wc -l -c corpus/knowledge/round-69-apk-axml-byte-evidence.md
    215   35113 corpus/knowledge/round-69-apk-axml-byte-evidence.md
```

read-only seat: no file edited; this report is the only write. Lane HEAD at review time `35e1258` (build commit `da02261`). No tool installed or upgraded (no pacman/uv/npx/cargo/npm transaction).

## 1. Header presence and precedence (clause 1)

The first bytes of the file are `source:` — not merely present, first:

```
$ head -c 40 corpus/knowledge/round-69-apk-axml-byte-evidence.md | od -c
0000000   s   o   u   r   c   e   :       S   0   3   8     342 200 224
```

Numbered head (`awk 'NR<=10'`), first 150 chars per line:

```
1: source: S038 — AOSP `ResourceTypes.h` (binary resource/XML format structures) — https://android.googlesource.com/platform/frameworks/base/+/refs/tags/
2: source: S043 — supersedes S039 — REA reverse-engineer-anything skill reference, "Android application artifacts" (docs, tier A; row mined round 66) — r
3: source: S045 — Android DEX format specification (AOSP, source.android.com) — https://source.android.com/docs/core/runtime/dex-format (docs, tier A, **
4: source: S032 — PKWARE APPNOTE.TXT — .ZIP File Format Specification — https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT (spec, tier A; row mi
5: source: S034 — PKWARE APPNOTE.TXT — .ZIP File Format Specification — https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT (spec, tier A; row mi
6: source: S047 — supersedes S046 — AXML anchor derivation (own-work, tier A; row opened round 69 by this entry's author) — scope: the machine derivation
7: source: S041 — Authored apk-r65 bundle — `corpus/fixtures/apk-r65/fixture.apk`, `corpus/fixtures/apk-r65/truth.json`, `corpus/fixtures/apk-r65/generat
8: verified-at: 2026-10-25 (round-69 re-derivation; the fixture, oracle and readout bytes are the round-65 claim-tree bytes, unchanged since `c7b7cf98`; 
9: recheck: `python3 -B corpus/derive_axml_anchors.py` from the lane root (every S038 line number and value this entry cites; exits 2 if a cited symbol i
10: coverage-map: C05 (`corpus/README.md`, Android packages (APK)) — the container members, the binary-AXML `AndroidManifest.xml` and the `classes.dex` de
```

- `source:` is line 1; all seven source rows precede `verified-at:`/`recheck:`/`coverage-map:`. PASS.
- `verified-at:` carries an exact date, `2026-10-25`, plus commit `c7b7cf98`. PASS (date and commit both present, both re-derived in §3).
- `recheck:` carries two runnable commands (not a citation alone) and a claimed stdout digest; both re-ran clean in §4. PASS.
- `coverage-map:` is the tenth line and names `C05` plus `corpus/README.md` plus the README's surface label `Android packages (APK)`. PASS (§5).
- No anchor is a bare homepage: S038 is a tag-pinned googlesource file URL with per-symbol line anchors; S045 is the AOSP dex-format page with a field-table anchor and a pinned snapshot digest; S032/S034 are the APPNOTE document with section anchors (`§4.3.12`, `§4.3.7`); S043/S047/S041 are repo paths with line spans and sha256s.

## 2. Every header source row resolves (ticket clause)

Ids extracted from the entry's own bytes, each looked up in the registry:

```
$ for s in $(grep "^source:" corpus/knowledge/round-69-apk-axml-byte-evidence.md | grep -oE "^source: S[0-9]+" | grep -oE "S[0-9]+"); do grep -qE "^\| *$s " corpus/SOURCES.md && echo "$s RESOLVES" || echo "$s MISSING"; done
S038 RESOLVES
S043 RESOLVES
S045 RESOLVES
S032 RESOLVES
S034 RESOLVES
S047 RESOLVES
S041 RESOLVES
```

Registry columns read directly (`awk -F'|'` over `corpus/SOURCES.md`; kind/tier/status/opened):

```
S032 type= spec  tier= A  status= mined  opened= 2026-10-23
S034 type= spec  tier= A  status= mined  opened= 2026-10-23
S038 type= spec  tier= A  status= mined  opened= 2026-10-24
S041 type= own-work tier= A  status= mined  opened= 2026-10-24
S043 type= docs  tier= A  status= queued opened= 2026-10-24
S045 type= docs  tier= A  status= mined  opened= 2026-10-24
S047 type= own-work tier= A  status= mined  opened= 2026-10-25
```

Both rows the entry names as superseded also exist, so the supersession statements resolve: `S039` at `SOURCES.md:53`, `S046` at `SOURCES.md:60`. S047's `used-by` already names this very entry (`corpus/knowledge/round-69-apk-axml-byte-evidence.md`); S046's `used-by` names the round-68 entry. No dangling `S###` in the header.

### 2a. Digest and path re-derivation for every row

```
$ sha256sum corpus/derive_axml_anchors.py corpus/snapshots/ResourceTypes.h \
    corpus/fixtures/apk-r65/fixture.apk corpus/fixtures/apk-r65/truth.json \
    corpus/fixtures/apk-r65/generator.py corpus/fixtures/apk-r65/readout.py
74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa  corpus/derive_axml_anchors.py
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  corpus/fixtures/apk-r65/truth.json
eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a  corpus/fixtures/apk-r65/generator.py
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py
$ sha256sum .ufo/waves/round-65/source-snapshots/ResourceTypes.h .ufo/waves/round-65/source-snapshots/rea-android-applications.md
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  .ufo/waves/round-65/source-snapshots/ResourceTypes.h
412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c  .ufo/waves/round-65/source-snapshots/rea-android-applications.md
$ sha256sum .ufo/waves/round-67/source-snapshots/dex-format.html && stat -c '%s bytes' .ufo/waves/round-67/source-snapshots/dex-format.html
c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4  .ufo/waves/round-67/source-snapshots/dex-format.html
281157 bytes
```

Every digest in header lines 1-7 equals the file it names, including the two copies of the S038 snapshot (entry:1's `56b88bc4…` appears identically for `.ufo/…/round-65/source-snapshots/ResourceTypes.h` and `corpus/snapshots/ResourceTypes.h`, so the header's "committed byte-exact as `corpus/snapshots/ResourceTypes.h` (same sha256)" resolves).

### 2b. Anchor re-derivation, row by row

**S038 (entry:1).** Header states 19 distinct `ResourceTypes.h` line numbers (`:237/:239/:241/:244/:245/:246/:247/:248/:253/:263`, `line 218`, `line 287`, `line 461`, `lines 612, 621`, `line 677`, `line 686`, `line 687`, `line 707`). My run of the cited derivation prints exactly that set plus the digest line (see §4 for the full stdout). Independent byte check of the envelope lines and the disputed `:244`/`:245` pair:

```
$ awk 'NR==237||NR==239||NR==241||NR==244||NR==245||NR==246||NR==247||NR==248||NR==253||NR==263 {printf "%d: %s\n", NR, $0}' corpus/snapshots/ResourceTypes.h
237: enum {
239:     RES_STRING_POOL_TYPE              = 0x0001,
241:     RES_XML_TYPE                      = 0x0003,
244:     RES_XML_FIRST_CHUNK_TYPE          = 0x0100,
245:     RES_XML_START_NAMESPACE_TYPE      = 0x0100,
246:     RES_XML_END_NAMESPACE_TYPE        = 0x0101,
247:     RES_XML_START_ELEMENT_TYPE        = 0x0102,
248:     RES_XML_END_ELEMENT_TYPE          = 0x0103,
253:     RES_XML_RESOURCE_MAP_TYPE         = 0x0180,
263: };
$ awk 'NR==218||NR==287||NR==461||NR==612||NR==621||NR==677||NR==686||NR==687||NR==707 {printf "%d: %s\n", NR, $0}' corpus/snapshots/ResourceTypes.h
218: struct ResChunk_header
287: struct Res_value
461: struct ResStringPool_header
612: struct ResXMLTree_header
621: struct ResXMLTree_node
677: struct ResXMLTree_attrExt
686:     // Byte offset from the start of this structure where the attributes start.
687:     uint16_t attributeStart;
707: struct ResXMLTree_attribute
```

The header's range claim "chunk-type enum block **lines 237-263** (`enum {` :237, `};` :263)" is byte-true, and `RES_XML_START_NAMESPACE_TYPE` is genuinely at `:245` (value `0x0100`), with `:244` = `RES_XML_FIRST_CHUNK_TYPE` — the M40/M44 off-by-one the header says it repairs is repaired. The header's own "every line number above is machine-derived … item 11" claim is true of all 19 numbers (set difference empty, §4).

**S043 (entry:2).** Anchor `lines 7-8` plus the counter-claim that "line 5" is `older server.`:

```
$ awk 'NR==5||NR==7||NR==8 {printf "%d: %s\n", NR, $0}' .ufo/waves/round-65/source-snapshots/rea-android-applications.md
5: older server.
7: Start with `inspect_android_package` on the caller's APK path for package
8: identity, manifest declarations, coverage, and inline Evidence. Use
```

The quoted sentence in entry:2 — "Start with `inspect_android_package` on the caller's APK path for package identity, manifest declarations, coverage, and inline Evidence." — spans :7-:8, and `:5` is `older server.`. Both resolve; snapshot sha `412d9cb4…` matches.

**S045 (entry:3).** Snapshot pin `c0428612…`, 281157 bytes matches. Anchor strings in the pinned HTML:

```
$ grep -c "must be 0x70 (112) bytes" .ufo/waves/round-67/source-snapshots/dex-format.html      → 1
$ grep -c "0x12345678" …/dex-format.html                                                       → 1
$ grep -c "SHA-1 signature" …/dex-format.html                                                  → 1
$ grep -o ".\{0,80\}SHA-1 signature.\{0,200\}" …/dex-format.html
  <td>SHA-1 signature (hash) of the rest of the file (everything but
$ grep -o ".\{0,60\}adler32.\{0,180\}" …/dex-format.html
  <td>adler32 checksum of the rest of the file (everything but
```

The checksum and signature quotes are HTML-wrapped across a `<code>`-split line, so a literal single-line `grep -c` of the whole sentence returns 0 — but the words are present in the pinned snapshot and resolve to that document under its pinned digest. That is an anchor-resolvability note (LOW, §7 F6), not a missing row and not a bare homepage.

**S032/S034 (entries 4-5).** `corpus/SOURCES.md:46` records S032 anchor `§4.3.3, §4.3.12, §4.3.16, …` and teaches the "fixed 46-byte record"; `:48` records S034 `§4.3.7` with "file name length sits at offset 26 and extra field length at offset 28" in a "fixed 30-byte record". Entry:4 cites `§4.3.12` (46-byte fixed part), entry:5 cites `§4.3.7` (30-byte fixed part), name length offset 26, extra length offset 28 — the header's anchors are the registry's anchors.

**S047 (entry:6).** `corpus/SOURCES.md:61` records script sha256 `74d4c0d9…`, 20 output lines, snapshot `56b88bc4…` (86255 bytes). My run prints 20 lines, exit 0, and the row's located quote `enum RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100` appears verbatim in the stdout.

**S041 (entry:7).** All four member digests and the 947-byte size match (§2a; `stat`/`ls` shows `-rw-r--r-- 947 … fixture.apk`).

## 3. `verified-at:` — the `c7b7cf98` clause re-derives

Entry:8 asserts the fixture/oracle/readout bytes are the round-65 claim-tree bytes "unchanged since `c7b7cf98`". Read-only git check against that commit's tree:

```
$ git log -1 --format='%H %s' c7b7cf98
c7b7cf98ddeecbd5464e47396f224e6384b78905 round-65: candidates — apk-r65 fixture+readout, C05 candidate entry, S038-S041 rows, C5 forged-evidence controls, lesson+wave spec (no README flip)
$ for f in fixture.apk truth.json generator.py readout.py; do git cat-file -p c7b7cf98:corpus/fixtures/apk-r65/$f | sha256sum; done
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  -
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  -
eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a  -
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  -
```

All four equal the header's S041 digests, so the `verified-at:` clause resolves to a real commit whose blobs are the cited bytes. PASS.

## 4. `recheck:` re-run — both commands exit 0 and reproduce the entry byte-for-byte

The `recheck:` half claimed for the readout: exit 0, 15 stdout lines, SHA-256 `507d79f8…`.

```
$ python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/revenger-r69-q02-readout.txt; echo "EXIT=$?"; wc -l < /tmp/revenger-r69-q02-readout.txt; sha256sum /tmp/revenger-r69-q02-readout.txt
EXIT=0
15
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  /tmp/revenger-r69-q02-readout.txt
$ (stderr empty)
```

The header's second half claims `derive_axml_anchors.py` prints every S038 line number and value the entry cites and exits 2 on a missing/ambiguous symbol. Both properties demonstrated:

```
$ python3 -B corpus/derive_axml_anchors.py; echo "EXIT=$?"
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

Byte-level comparison of the entry's embedded blocks with the live stdout (Python, `re`-extracted fenced blocks, blank lines dropped):

```
live lines: 20   embedded lines: 20   IDENTICAL: True
readout block: lines=15 sha256_of_joined=507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247
live   lines: 15 sha256=507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247
last block identical to live: True
header-stated S038 line numbers: [218, 237, 239, 241, 244, 245, 246, 247, 248, 253, 263, 287, 461, 677, 686, 687, 707]
unprinted in header: []
```

(the script's `(?::|line )(\d{3})` pattern does not capture the plural token `lines 612, 621`; both were verified in the struct block above, giving the full 19-number set.)

Exit-2 contract, probed on a **scratch copy only** (`/tmp/revenger-r69-q02-x2`, corpus untouched): (a) deleting `struct Res_value` and re-pinning the copy's digest makes the run print `derive_axml_anchors: struct Res_value: not found` and `EXIT=2`; (b) leaving the pin stale against a mutated snapshot prints `derive_axml_anchors: snapshot digest 79a39055… != pinned 56b88bc4…` and `EXIT=2`. So the `recheck:` command is not a citation dressed as a check: it fails loudly on the two cases the header names.

## 5. Coverage-map row named and extant (clause 4)

```
$ grep -cE '^\| C[0-9]+ ' corpus/README.md
14
$ grep -nE '^\| C05 ' corpus/README.md
34:| C05 | Android packages (APK) | — | `fixtures/apk-r65`; retained rejected candidate `knowledge/round-65-apk-axml-byte-evidence.md` (round-65 orchestrator-dispatched wave, falsified Q02/Q06/Q11, adjudicated round-66) | uncovered |
```

Entry:10 names `C05`, `corpus/README.md`, and the README's exact surface words `Android packages (APK)`. The row exists, the denominator is 14, and the status is still `uncovered` — consistent with `admission-status: candidate` (entry:11), which is the build-state the claims require before an all-pass flip. Naming the row is Q02's requirement; the unflipped status is C1's design, not a Q02 defect.

## 6. Why this is PASS and not FAIL on Q02's own reject test

Q02's reject condition is "any header is missing or the anchor is a bare homepage". Observed: (a) all four header elements exist and the `source:` block is first; (b) seven rows, seven registry hits, zero dangling ids; (c) every anchor in those rows is a document/section/symbol/line span or a repo path with a digest — none is a homepage; (d) every digest the header states equals the artifact it names, and the `c7b7cf98` blob claim re-derives; (e) the recheck commands run and their actual stdout equals the entry's embedded stdout byte-for-byte; (f) the coverage row is named and extant. Nothing in the reject clause is met.

## 7. Off-criterion findings (routed, not Q02 grounds — do not read these as a Q02 FAIL)

These are real and should be fixed before any flip; all are text-level, none removes a header element or breaks an anchor. The in-wave Q01 seat (`R69ReviewEntryQ01.md`) already logged F1-F5 as off-Q01 findings and the round-68 header check (`R68HeaderCheck.md`) logged F1/F2/F6, so they are recorded here for the adjudicator rather than re-litigated.

- **F1 (M) — S043 status token.** Entry:2 says "row mined round 66"; `corpus/SOURCES.md:57` col 9 reads `queued`, `used-by: —` (confirmed by `corpus/lessons/round-66.md:16` "+S043 queued supersedes S039"). Correct value: "row opened round 66, status `queued`" (or omit the status word). Q02-class adjacent, Q01/Q12 territory; already `R69ReviewEntryQ01.md:51` M2, `R68HeaderCheck.md:84`.
- **F2 (M) — S045 opener attribution.** Entry:3 says "opened 2026-10-24 by this entry's author"; `corpus/SOURCES.md:91` records "round-67 C05 re-gate source opening (S045) … Opener: L1 revenger-r67", and this entry's author is `L1 revenger-r69` (`reports/round-69/claims.md:3`). Correct value: "opened 2026-10-24 by the round-67 author". Carried from `R68HeaderCheck.md` Defect 3a; not in claims §C1's nine-item repair list.
- **F3 (L) — S038 "re-opened 2026-10-25".** The only trace is `corpus/SOURCES.md:92`'s S047 unit ("the bytes are the S038 snapshot re-opened from the repository"); the S038 row itself is unchanged (`opened 2026-10-24`, `used-by` the round-65 entry), and `corpus/lessons/round-69.md` does not exist yet (`ls` → No such file), so the old→new log the SOURCES contract requires is a settlement-time obligation.
- **F4 (M) — S038 registry anchor is stale against the bound bytes.** `corpus/SOURCES.md:52` still says "chunk-type enum :239-250"; the snapshot the row pins has the block at 237-263 with `:253` inside it. The entry's 237-263 is the byte-true value (verified §2b); the registry row, not the entry, needs the routed correction.
- **F5 (L) — body quote placement (item 8, not the header).** Entry:84 attributes "Appears header.headerSize bytes after a `ResXMLTree_node`" to `struct ResXMLTree_attrExt` (line 677); that sentence is the doc-comment at snapshot `:675`, the struct opens at `:677`. Q11/Q08 class, out of Q02's header scope; same as `R69ReviewEntryQ01.md` finding 4.
- **F6 (L) — S045 quoted sentences are de-tagged renderings.** In the pinned HTML the checksum/signature sentences are split by `<code>` markup, so a literal whole-sentence `grep -F` returns 0. The anchor still resolves to the pinned snapshot (`c0428612…`), but a rechecker cannot reproduce the quotes by literal match without a stated de-tag rule.

## 8. Residual risk

- My verdict is bound to entry sha256 `c1e7eaac9dba4c77e578c788755dec3e3499fd8795ad0e479c51b5be7deb11d5` (35113 bytes, 215 lines). Any edit to the entry, `corpus/derive_axml_anchors.py`, `corpus/snapshots/ResourceTypes.h`, or the four apk-r65 files voids it and the two recheck commands must be re-run.
- S032/S034 were checked against the registry's recorded anchors (`§4.3.12`/`§4.3.7`, 46/30-byte widths, offsets 26/28) and the readout's arithmetic; the APPNOTE document itself was not re-fetched (no APPNOTE snapshot exists under `.ufo/waves/*/source-snapshots/`). This is a resolution check at registry strength, not a re-read of PKWARE's bytes.
- Exit-2 probes ran on a scratch copy under `/tmp/revenger-r69-q02-x2`; the lane corpus was never written. Scratch removed after the run.

Tooling: none installed, none upgraded — no pacman/uv/npx/cargo/npm transaction; only `read`, `grep`, `awk`, `head`, `od`, `sha256sum`, `stat`, `wc`, `python3 -B` and read-only `git log`/`git cat-file` were used.
