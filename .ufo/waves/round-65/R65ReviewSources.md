FAIL — S038 PASS, S039 FAIL (anchor line wrong: quote at :7, cited :5), S040 FAIL (version misstated: sha256-bound snapshot is Python 3.15.1, row says 3.15.0), S041 PASS; plus one file-level contract-v1 violation (rule 5 search log has no round-65 note).

# R65ReviewSources — SOURCES.md rows S038–S041 vs SOURCES-CONTRACT-v1

Lane:/home/vgpnk/Projects/shokunin/revenger-shokunin. Contract read first:
/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/claims.md and
/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md.
Read-only: this seat wrote only this file; all git calls were `show`/`diff`/`status` (no mutation).

## Per-row verdicts

### S038 — PASS
`corpus/SOURCES.md:52`. 11 columns (NF=13), id next-unused after S037, no `|` in cells.

Snapshot bytes verified (`.ufo/waves/round-65/source-snapshots/ResourceTypes.h`):

```
$ sha256sum ResourceTypes.h   -> 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f
$ wc -c ResourceTypes.h       -> 86255
```
Both match the row's `snapshot sha256 56b88bc4…, 86255 bytes`.

Every cited line resolves to the named struct in that snapshot:

```
 218: struct ResChunk_header
 239:     RES_STRING_POOL_TYPE              = 0x0001,
 250:     RES_XML_LAST_CHUNK_TYPE           = 0x017f,
 287: struct Res_value
 461: struct ResStringPool_header
 612: struct ResXMLTree_header
 621: struct ResXMLTree_node
 677: struct ResXMLTree_attrExt
 707: struct ResXMLTree_attribute
```
(`sed -n '<n>p' ResourceTypes.h` for each.) The cited enum range `:239-250` is the real
AXML chunk-type body: `:238 RES_NULL_TYPE=0x0000`, `:241 RES_XML_TYPE=0x0003`,
`:244 RES_XML_FIRST_CHUNK_TYPE` through `:248 RES_XML_START_ELEMENT_TYPE=0x0102`,
`:250 RES_XML_LAST_CHUNK_TYPE=0x017f` (`sed -n '236,258p'`).

`teaches` is grounded in the same bytes: `UTF8_FLAG = 1<<8` at `:480`,
`attributeStart` `:687` and `attributeSize` `:690` in `ResXMLTree_attrExt`. The claimed
8/16/20/28-byte widths are derivable from the field widths in those structs
(`ResChunk_header` 2+2+4=8; `ResXMLTree_node` 8+4+4=16; `ResXMLTree_attrExt` 4+4+6×2=20;
`ResStringPool_header` 8+5×4=28 — fields at `:461-490`), so it is a derived-but-true
statement, not an unsourced one.

Tier A is scoped ("this tag only", field layout) — scoped, not global. Status `mined`;
`used-by corpus/knowledge/round-65-apk-axml-byte-evidence.md` exists and cites the row at
`corpus/knowledge/round-65-apk-axml-byte-evidence.md:1` (`source: S038 … (spec, tier A,
opened 2026-10-24)`). `opened` 2026-10-24 is the round date and matches the lesson gate
`corpus/lessons/round-65.md:12`.

### S039 — FAIL (one-line anchor defect; rest of row sound)
`corpus/SOURCES.md:53`. Cells, id, tier scoping ("route-scope sentences only … not provider
execution on this host, not the authored fixture bytes"), status `mined`, and used-by are
all correct; snapshot digest and line count check out:

```
$ sha256sum rea-android-applications.md -> 412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c
$ wc -l rea-android-applications.md     -> 34
```

Defect: the row's anchor says `line 5`, and the lesson gate repeats it —
`corpus/lessons/round-65.md:13` "Located quote, line 5: \"Start with `inspect_android_package`
on the caller's APK path for package identity, manifest declarations, coverage, and inline
Evidence.\" (17 words)." At the landed snapshot, line 5 is `older server.` and the quoted
sentence starts at line 7:

```
$ nl -ba .ufo/waves/round-65/source-snapshots/rea-android-applications.md | sed -n '5,8p'
     5  older server.
     7  Start with `inspect_android_package` on the caller's APK path for package
     8  identity, manifest declarations, coverage, and inline Evidence. Use
```
(`nl` on the whole file: `:1 "# Android application artifacts"`, `:3-5` the "Use the
connected server's advertised Android tools…" paragraph.)

The row's second anchor component, the `"The provider requires"` paragraph, is correct —
that paragraph begins at `:16` ("The provider requires a separately supplied headless JADX
MCP JAR 0.7.1 and Java 17 or newer.").

Contract v1 requires the anchor be exact (`anchor` = "exact section / heading / page / line
plus revision"). A wrong line number on the load-bearing row that `claims.md` §Frontier step
conformance names as one of C1's two sourced supports is not exact. Fix: `:7-8` (and the
matching gate line `corpus/lessons/round-65.md:13`) — the quote text itself is verbatim and
present, so this is a citation correction, not a new open.

### S040 — FAIL (version claim contradicted by the row's own byte binding)
`corpus/SOURCES.md:54`. Cells, id, kind/tier, `status queued`, `used-by —`, `opened
2026-10-24` are all legal; quote grounding is real (the sentence appears in the module
description body, line-wrapped: `<p>The ZIP file format is a common archive and compression
standard. This module\nprovides tools to create, read, write, append, and list a ZIP file.`).

Defect: the row titles the source "CPython **3.15.0** documentation" and scopes it "this
release only", but the snapshot the row binds by sha256 is **3.15.1**:

```
$ grep -o '<title>[^<]*' .ufo/waves/round-65/source-snapshots/zipfile-docs.html
<title>zipfile — Work with ZIP archives &#8212; Python 3.15.1 documentation
$ grep -o 'Python 3\.1[0-9]\.[0-9]*' … | sort -u
Python 3.15.1
$ sha256sum zipfile-docs.html -> e7fe6715126a3be8e6ea7ca4d3dc2d8713b6c979bde13f8fa9d6c458a3c49c6a   (139782 bytes)
```
The sha256 and byte count match the row, so the row asserts 3.15.0 over bytes that are
3.15.1 — a version-scoped row whose version is wrong, self-contradictory within one row.
Same misstatement in `corpus/lessons/round-65.md:14` ("CPython 3.15.0 `zipfile`
documentation … sha256 `e7fe6715…`"). Fix: retitle to 3.15.1 (keep the digest) or re-fetch
the 3.15.0 page and re-pin; either way the gate line follows. Low blast radius: the row is
`queued`/not load-bearing — the entry's format claims rest on S032/S034, and the entry does
not cite S040 (`grep -n 'S040' corpus/knowledge/round-65-apk-axml-byte-evidence.md` → only
S038/S039/S041 in the `source:` header).

### S041 — PASS
`corpus/SOURCES.md:55`. All four digests and the byte count reproduce from the working tree:

```
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  corpus/fixtures/apk-r65/truth.json
eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a  corpus/fixtures/apk-r65/generator.py
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py
947 corpus/fixtures/apk-r65/fixture.apk
```
All four paths exist, `used-by` exists and cites the row at
`corpus/knowledge/round-65-apk-axml-byte-evidence.md:3`. The `teaches` process claim
("regeneration … reproduced the fixture byte-for-byte on Python 3.14.8") is corroborated by
a wave receipt, not just asserted: `.ufo/waves/round-65/R65FixtureRegen.md:15-17` records
`cmp -s` exit 0 for `fixture.apk` and `truth.json` and runtime `Python 3.14.8`.

Minor (not a FAIL): the anchor pins content by sha256 but names no commit revision
("at the round-65 claim tree"), unlike S037's "at base 666ea84b…". Content addressing pins
the bytes, so exactness is satisfied in substance; naming the landing commit (`c7b7cf9`,
`git log --oneline -1 -- corpus/SOURCES.md`) would match the row's own convention.

## File-level contract checks (all rows)

```
rows                                 41
malformed NF!=13                     0
duplicate ids                        (none)
enum/tier/community-A violations     (none)
tier histogram                       A=39 C=2
status histogram                     mined=35 queued=2 rejected=4
mined rows with missing used-by      (none)
```
`bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate
/home/vgpnk/Projects/shokunin/revenger-shokunin` → `revenger-shokunin ok`, exit 0
(warnings only, the four disclosed W04s S024/S028/S029/S034).

- **Append-only (rule 2): satisfied.** `git diff --stat 3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f
  -- corpus/SOURCES.md` → `1 file changed, 4 insertions(+)`, zero deletions; base archive has
  exactly 37 rows ending `S037`. No pre-existing row's `status`/`recheck`/`used-by` moved.
- **Ids never reused: satisfied.** ids are contiguous 001–041 (max 041 over 41 rows, no
  gaps/dups); S038–S041 are the next-unused block.

## Findings (severity order)

1. **F1 — S039 anchor line wrong (:5 vs :7).** Evidence above; contract v1 `anchor` exactness
   + `claims.md` §Frontier step conformance names S039 as one of C1's sourced supports.
   One-line fix in `corpus/SOURCES.md:53` and `corpus/lessons/round-65.md:13`.
2. **F2 — S040 version misstated (3.15.0 claimed, 3.15.1 bound by digest).** Evidence above;
   fix row title/scope and `corpus/lessons/round-65.md:14`. Queued row, not load-bearing, so
   no effect on C1/C2 counting, but it is a false revision in a version-scoped row.
3. **F3 — contract v1 rule 5 not satisfied for round 65.** No `## Search log` note for the
   round's bounded search: `grep -c '^- 2026-10-24,' corpus/SOURCES.md` → `0`; the
   base→HEAD diff for the file is insertion-only 4 rows, so no note was added anywhere; the
   last note is `corpus/SOURCES.md:81` (2026-10-23). Rule 5 requires question/query, where
   searched, identified/screened/included/excluded counts with exclusion reasons and a stop
   rationale for each bounded search — the round opened three external documents
   (S038–S040) and one own-work bundle (S041) without one. Fix in the lesson/round-close
   bookkeeping: append the 2026-10-24 note.
4. **F4 (minor) — lesson census path points at a non-existent lane path.**
   `corpus/lessons/round-65.md:17` cites `scripts/sources-census.sh validate`, but the lane
   has no `scripts/` dir (`ls scripts` → No such file or directory); the script is the fleet
   one at `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh` (one level up). The
   claim's substance is true (validate exits 0), the path is not resolvable from the lane.

## Residual risk / verification gaps
- S039 and S040 provenance upstream (npm `rea-agents@6.5.0` extraction; live
  docs.python.org fetch) was not re-fetched by this seat — only the landed snapshots were
  checked; their digests match the registry, so the rows bind what they claim to bind except
  for the two revision strings above.
- No LSP server applies to a Markdown registry; the census above is the contract's own
  textual instrument (contract v1 §Census), and `sources-census.sh validate` (E01–E12,
  W01–W04) was used as the maintained semantic checker alongside the manual commands.
- Regeneration of the APK was not re-run by this seat (outside seat bounds); it is
  corroborated by the wave receipt R65FixtureRegen.md, not independently reproduced here.
- Tooling: no installs or upgrades were needed or performed (python3 3.14.8, coreutils
  sha256sum, gawk already present); pacman untouched.
