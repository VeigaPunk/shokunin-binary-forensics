FAIL — Q02 header completeness fails (load-bearing S032/S034 cited in the body, absent from `source:`), Q11 honesty fails narrowly (the "chunk-type enum block lines 237-253" range is transcribed and false on the bytes: the enum opens :237 and closes :263, repeated at entry:1,57,148,157), and S045 is misattributed ("opened … by this entry's author"); the C2 delta itself — the two `:244` → `:245` anchors — is verified correct and **no individual S038 symbol anchor is wrong** (all 17 derive lines reproduce byte-exactly).

Seat: R68HeaderCheck (Q02/Q11 entry-header check) · lane `/home/vgpnk/Projects/shokunin/revenger-shokunin` · review tree `4232235` (HEAD, 2026-10-24), entry sha256 `107e2d7483e57e64476ead408f2eb793f41e3eea5e3c96407763eadca6dfea5b`, 215 lines, five header lines + four trailer lines at :1-:9.

Read-only seat: no production edit, no git/jj mutation. No tool installed or upgraded (Python 3 stdlib only), so the tooling directive's install record is empty.

## Criteria in the entry's own terms

- **Q02** (`corpus/QUALITY.md:14`): "The entry opens with `source:` (its `S###` row, URL or path, exact anchor), `verified-at:` (date or commit) and `recheck:` … and names the coverage-map row it fills". Fail trigger: "any header is missing or the anchor is a bare homepage".
- **Q11** (`corpus/QUALITY.md:23`): "Each count, identifier, offset and digest in an entry carries, inside the entry, the command that derives it … and that command's output. Constants such as header offsets are derived, not assumed … a value is correct when re-derived but the entry carries no derivation, or a recorded value is presented as re-derived".

## Machine receipts I ran on the current bytes

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin
$ python3 -B corpus/derive_axml_anchors.py     # EXIT=0, 17 lines
sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f ResourceTypes.h
struct ResChunk_header : 218
struct Res_value : 287
struct ResStringPool_header : 461
struct ResXMLTree_header : 612
struct ResXMLTree_node : 621
struct ResXMLTree_attrExt : 677
struct ResXMLTree_attribute : 707
enum RES_STRING_POOL_TYPE : 239
enum RES_XML_TYPE : 241
enum RES_XML_START_NAMESPACE_TYPE : 245
enum RES_XML_END_NAMESPACE_TYPE : 246
enum RES_XML_START_ELEMENT_TYPE : 247
enum RES_XML_END_ELEMENT_TYPE : 248
enum RES_XML_RESOURCE_MAP_TYPE : 253
comment attributeStart : 686
field attributeStart : 687
$ python3 -B corpus/derive_axml_anchors.py | sha256sum
b02cfe54df5af9e8ca16c61c3d4c719ebb18ac3e9d1cf23b48686628bf3e0831  -

$ python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/r68hc_out.txt; echo EXIT=$?   # EXIT=0
$ wc -l /tmp/r68hc_out.txt; sha256sum /tmp/r68hc_out.txt
15 /tmp/r68hc_out.txt
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  /tmp/r68hc_out.txt
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact archive | wc -l    # 1 (single JSON line)

$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md
checked_blocks=17 problems=0            # GATE_EXIT=0

$ sha256sum corpus/derive_axml_anchors.py corpus/snapshots/ResourceTypes.h \
            corpus/fixtures/apk-r65/{readout.py,truth.json,fixture.apk,generator.py}
bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249  derive_axml_anchors.py
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  snapshots/ResourceTypes.h   (86255 bytes)
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  readout.py
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  truth.json
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  fixture.apk                 (947 bytes)
eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a  generator.py
$ sha256sum .ufo/waves/round-65/source-snapshots/ResourceTypes.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f    # copy is byte-exact
$ git rev-parse c7b7cf98:corpus/fixtures/apk-r65/{fixture.apk,truth.json,readout.py} ; git hash-object <same>
b62216a9… / d6b8c5cb… / 0fcb1d85…   ==   b62216a9… / d6b8c5cb… / 0fcb1d85…   # unchanged since c7b7cf98
$ git log --format='%h %ad %s' -1 c7b7cf98
c7b7cf9 2026-10-24 revenger-shokunin round-65: candidates — apk-r65 fixture+readout, C05 candidate entry …
```

Failure paths of the derive command (S046's "exit 2 on a missing or ambiguous symbol"), exercised on `/tmp` copies only, never on lane bytes: control tree exit `0`; symbol line removed → `derive_axml_anchors: enum RES_XML_START_NAMESPACE_TYPE: not found`, command exit `2`; symbol line duplicated → `derive_axml_anchors: enum RES_XML_END_ELEMENT_TYPE: ambiguous (2 hits at [248, 249])`, exit `2`; one appended byte → `snapshot digest 74ecef9a… != pinned 56b88bc4…`, exit `2`. Structural note: the digest pin is checked before symbol search, so a symbol-absence case on a *pinned* snapshot can only fire if the pin is also updated — the pin is a stronger guard, not a weaker one.

## Line 1 — `source: S038` (entry:1) — FAIL (range not honest; registry unreconciled)

**What it says.** AOSP `ResourceTypes.h` at tag `android-15.0.0_r1`, spec, tier A, "row mined round 65, **re-opened 2026-10-24 by this entry's author** from the committed snapshot"; scope "the field layout, chunk-type enum values and fixed struct sizes of the compiled-XML (AXML) chunk stream for one authored binary `AndroidManifest.xml`"; anchors `ResChunk_header` :218, "chunk-type enum block **lines 237-253**" with `RES_STRING_POOL_TYPE` :239, `RES_XML_TYPE` :241, `RES_XML_START_NAMESPACE_TYPE` **:245**, `RES_XML_END_NAMESPACE_TYPE` :246, `RES_XML_START_ELEMENT_TYPE` :247, `RES_XML_END_ELEMENT_TYPE` :248, `RES_XML_RESOURCE_MAP_TYPE` :253 "(0x0180 — inside the enum block, unlike the round-65 draft's :239-250)", `ResStringPool_header` :461, `ResXMLTree_header`/`ResXMLTree_node` :612/:621, `ResXMLTree_attrExt` :677 with comment :686 and field :687, `ResXMLTree_attribute` :707, `Res_value` :287; "every line number above is machine-derived"; snapshot sha256 `56b88bc4…`, 86255 bytes, committed byte-exact as `corpus/snapshots/ResourceTypes.h`.

**Does the row exist, at that tier and scope?** Yes. `corpus/SOURCES.md:52` is S038, kind `spec`, tier `A`, anchor column carries the same tag, `struct ResChunk_header` :218, a chunk-type enum range, `ResStringPool_header` :461, `ResXMLTree_header`/`ResXMLTree_node` :612/:621, `struct ResXMLTree_attrExt` :677, `struct ResXMLTree_attribute` :707, `Res_value` :287, and the identical snapshot sha/byte count. The row's scope ("field layout of the compiled-XML (AXML) chunk, string-pool, node, attribute and value structures for one authored binary `AndroidManifest.xml`, this tag only") is compatible with the header's wording, and its `teaches` column explicitly covers "The chunk-type values, the 8/16/20/28-byte fixed structure sizes" — so the header's scope addition ("chunk-type enum values and fixed struct sizes") is inside the registered scope, and the tag is named, so "this tag only" is preserved. Tier and scope: **honest**.

**Are the anchors true on the current bytes?** Every cited *symbol* line is exactly right. The derive output above matches 218/287/461/612/621/677/686/687/707/239/241/245/246/247/248/253, and the snapshot bytes confirm it directly: 686 `// Byte offset from the start of this structure where the attributes start.`, 687 `    uint16_t attributeStart;`, 707 `struct ResXMLTree_attribute`. The declared delta (`:244`→`:245` twice) is real: the r67 candidate has `:244` at its lines 1 and 56, and the v3's only two `:244` occurrences are narrative in `verified-at:` (entry:6) and `admission-status:` (entry:9), never anchors.

**Defect 1a (MEDIUM, Q11) — the block range is false at its end, in the header itself.** `awk 'NR==237…' corpus/snapshots/ResourceTypes.h` gives 237 `enum {` … 253 `RES_XML_RESOURCE_MAP_TYPE = 0x0180,` … 256 `RES_TABLE_PACKAGE_TYPE = 0x0200,` … 263 `};`. The enum that line 1 calls "the chunk-type enum block" therefore spans **237-263**, not 237-253; 253 is where the XML chunk-type sub-block ends, not where the block ends. The string `237-253` appears four times: entry:1 (header), entry:57 (item 4), entry:148 (item 11 prose), entry:157 (Observation/inference). Item 11 derives *symbols only* — nothing in the entry derives a block boundary — so this is a hand-transcribed range of exactly the M40/M44 class the entry claims to have eliminated, and it is wrong on the bytes. No cited anchor is off by one, so the repair stands; the range is the residue.

**Defect 1b (MEDIUM, registry) — the header contradicts the row it cites and nothing routes the conflict.** Line 1 says `:253` is "inside the enum block, **unlike the round-65 draft's :239-250**" — and `corpus/SOURCES.md:52` still reads `chunk-type enum :239-250`. The entry asserts the registered range is wrong while the registry keeps it unchanged; per `corpus/SOURCES.md:3-6` only `status`, `recheck` and `used-by` are mutable in place, so the anchor divergence needed a routed correction (report/lesson), not a silent disagreement. Byte truth is 237-263, i.e. both strings are wrong and differently wrong (registry excludes :253 that the entry needs; entry understates the close).

**Defect 1c (LOW-MEDIUM, attribution) — "re-opened … by this entry's author" does not hold for this file's author.** The lane's recorded re-open is round-67's (`corpus/lessons/round-67.md:80` "Re-opened from committed snapshots (no new fetch), for the v2 candidate's headers: S038"), by `L1 revenger-r67` (`reports/round-67/claims.md:3`); this round's author is `L1 revenger-r68 (attempt 1, Kimi fresh L1)` (`reports/round-68/claims.md:3`). A round-68 re-read is traceable only indirectly, in the S046 opening unit (`corpus/SOURCES.md:99`: "the bytes are the S038 snapshot re-opened from the repository"), and no registry field changed: S038 is still `status=mined`, `used-by=corpus/knowledge/round-65-apk-axml-byte-evidence.md` (`SOURCES.md:52`, cols read directly). Fix: name the round ("re-opened round 67 by its author; re-read round 68 for the anchor derivation").

## Line 2 — `source: S043` (entry:2) — PASS (two LOW notes)

**What it says.** "S043 — supersedes S039 — REA … 'Android application artifacts' (docs, tier A; row mined round 66) — route-scope sentences only … not provider execution and not the fixture bytes — anchor: snapshot `.ufo/waves/round-65/source-snapshots/rea-android-applications.md` **lines 7-8** (…), sha256 `412d9cb4…` — the round-65 draft cited 'line 5', which is `older server.`"

**Truth.** `SOURCES.md:57` exists: docs, tier A, scope wording matches the header nearly verbatim, `teaches` starts "supersedes S039 — same scope and tier". The snapshot exists at that path with sha256 `412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c` (verified) and `sed -n '5p;7,8p'` prints `older server.` / `Start with \`inspect_android_package\` on the caller's APK path for package` / `identity, manifest declarations, coverage, and inline Evidence. Use` — the two-line anchor and the "line 5 is `older server.`" correction are both exact. Round attribution: `SOURCES.md:90` records S042–S044 under round-66. **Honest and complete.**

LOW: the registry's status token for S043 is `queued` (`SOURCES.md:57` col 9), not `mined`, so "row mined round 66" uses a status word the row does not carry. LOW: `used-by` is `—` although the v3 cites it.

## Line 3 — `source: S045` (entry:3) — FAIL (misattributed opening); row/tier/scope/digest otherwise verified

**What it says.** Android DEX spec (source.android.com), docs, tier A, "**opened 2026-10-24 by this entry's author**"; scope "the declared `header_item` field semantics of one authored `classes.dex` member (magic, checksum, signature, file_size, header_size, endian_tag); not dex program validity"; anchor = the "File layout" → `header_item` table with four quoted strings; snapshot `.ufo/waves/round-67/source-snapshots/dex-format.html` sha256 `c0428612…`, 281157 bytes.

**Truth.** `SOURCES.md:59` exists: docs, tier A; the registered scope is the same sentence plus "and not general dex parsing" — the entry's omission only narrows, so scope is honest. Snapshot sha256 verified `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4`.

**Defect 3a (MEDIUM, attribution) — the opening is not this entry's author's.** `corpus/SOURCES.md:91` records the opening under round 67 ("round-67 C05 re-gate source opening (S045). Unit: one fetched document — the AOSP DEX format spec …"), and round-67's author is `L1 revenger-r67` (`reports/round-67/claims.md:3`) — not this file's `L1 revenger-r68` (`reports/round-68/claims.md:3`). The phrase was true in the r67 candidate (whose line 1/8 read identically for its own author) and became false when inherited into the r68 file. Given this round's calibration axis is *attribution* (C7), a false "by this entry's author" in the header is the same defect class as the one C1 repairs. Fix: "opened 2026-10-24 by the round-67 author".

**Defect 3b (LOW, Q02 "exact anchor") — the quoted strings are de-tagged renderings, not the snapshot's bytes.** Literal search on the pinned file returns zero hits for two of the four quotes:
```
$ grep -c -F 'SHA-1 signature (hash) of the rest of the file (everything but magic, checksum, and this field)' …/dex-format.html   → 0
$ grep -c -F 'adler32 checksum of the rest of the file (everything but magic and this field)' …/dex-format.html                    → 0
$ grep -c -F 'must be 0x70 (112) bytes (v40 or earlier)' …/dex-format.html                                                          → 0
```
The raw rows interleave ` <code translate="no" dir="ltr">magic</code>` etc. (`tr '\n' ' '` confirms: "…(everything but     <code …>magic</code>, <code …>checksum</code>, and this field); used …"; "must be 0x70 (112) bytes       <span style="float:right">(v40 or earlier)</span>"). The quotations are faithful renderings, but a rechecker cannot reproduce them by literal match, and the entry records no de-tag rule. Say "rendered text; raw HTML carries `<code>`/`<span>` markup" or quote a literal substring.

## Line 4 — `source: S046` (entry:4) — PASS (one LOW note)

**What it says.** Own-work, tier A, "row opened round 68 by this entry's author"; scope "the machine derivation of every S038 line number this entry cites … not the layout facts themselves"; anchor `corpus/derive_axml_anchors.py` sha256 `bce497d6…`, 17 output lines over `corpus/snapshots/ResourceTypes.h` sha256 `56b88bc4…` (exit 2 on a missing or ambiguous symbol); source snapshot same sha.

**Truth.** `SOURCES.md:61` exists with the same kind/tier/date/script sha/line count/snapshot sha, and `SOURCES.md:99` logs the round-68 opening unit. File sha256 `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249` verified; stdout 17 lines verified; the exit-2 contract exercised on `/tmp` copies (missing symbol, ambiguous symbol, digest mismatch — all exit 2, receipts above). **Honest and complete.**

LOW: `used-by` on S046 is `—` (`SOURCES.md:61` col 12) while `reports/round-68/claims.md` §Registered calls it "the frontier step's sourced row for C2" and the v3 header cites it — the back-pointer the row exists for is absent. Same pattern for S038/S041 (name only the round-65 entry), S045 (names only the r67 candidate), S043 (`—`).

## Line 5 — `source: S041` (entry:5) — PASS (two LOW notes)

**What it says.** Own-work, tier A, "row mined round 65"; the authored bundle (`fixture.apk`, `truth.json`, `generator.py`, `readout.py`); "byte content … at the round-65 claim tree (bytes unchanged since)"; anchors fixture sha256 `05d2280f…` (947 bytes), truth.json `27303bae…`, readout.py `92e347c3…`.

**Truth.** `SOURCES.md:55` exists, own-work, tier A; fixture sha + `stat -c %s` = 947 bytes ✓, truth.json sha ✓, readout.py sha ✓. "Unchanged since" is grounded: the three blobs at `c7b7cf98` (the round-65 candidates commit) are identical to HEAD (`git rev-parse` vs `git hash-object`), and `generator.py` still hashes to the registry's `eaa9444c…`. **Honest.**

LOW: `generator.py` is named as part of the source bundle but carries no digest in the header while the other three do (the registry has it) — an anchor set that is silently incomplete. LOW: `used-by` names only the round-65 entry.

## Line 6 — `verified-at:` (entry:6) — PASS

**What it says.** "2026-10-24 (round-68 re-derivation; the fixture, oracle and readout bytes are the round-65 claim-tree bytes, unchanged since `c7b7cf98`; every output line below was captured from the named command's actual stdout at build time, never transcribed by hand — the round-65 draft's entry:41 transcription drift is the M39 class this entry repairs, and the round-67 draft's `:244` anchor is the M40/M44 class this entry repairs by deriving every spec line number from the pinned snapshot)".

**Round match.** 2026-10-24 is this round's declared date (`reports/round-68/claims.md:3`) and the build commit's date (`4232235 2026-10-24`, HEAD). It does **not** claim to be today's review date, and it re-reproduces today, so it is not stale. ✔

**Provenance honesty.** `c7b7cf98` resolves to `c7b7cf9 2026-10-24 … round-65: candidates — apk-r65 fixture+readout, C05 candidate entry…` and the three blobs at that commit equal HEAD (receipts above), so "unchanged since `c7b7cf98`" is exact rather than asserted. "Every output line captured from actual stdout" is independently confirmed on the **current** bytes: the repaired gate re-ran all 17 `$ <command>` blocks and found `problems=0` (exit 0). ✔

Scope note (not a defect here, already reported under 3b): that guarantee covers gate-recognised `$ <command>` blocks only; the de-tagged S045 prose quotes sit outside it.

## Line 7 — `recheck:` (entry:7) — PASS on runnability; LOW-MEDIUM completeness gap

**What it says.** `python3 -B corpus/derive_axml_anchors.py` from the lane root (every S038 line number cited; exits 2 on a missing/ambiguous symbol) and `python3 -B corpus/fixtures/apk-r65/readout.py` from the lane root — "exits 0 and prints 15 stdout lines whose SHA-256 is `507d79f8…`"; the per-value form `--fact '<id>'` prints one JSON line.

**Truth.** Both commands exist and run exactly as written: derive exit 0 / 17 lines; readout exit 0 / 15 lines / stdout sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` (byte-identical to the claim, stderr empty); `--fact archive` prints one JSON line. The exit-2 clauses hold (receipts above). **Runnable and honest.**

**Gap.** The receipt is asymmetric: the readout half is pinned by stdout digest, the derive half — the entire C2 story — is pinned only by exit status. If a future snapshot edit shifted a printed line number, the derive command would still exit 0. The missing receipt, computed on the current bytes: **derive stdout = 17 lines, sha256 `b02cfe54df5af9e8ca16c61c3d4c719ebb18ac3e9d1cf23b48686628bf3e0831`**. Add it to the `recheck:` line (cheap, and it makes the anchor derivation as re-checkable as the readout).

## Line 8 — `coverage-map:` (entry:8) — PASS

**What it says.** "C05 (`corpus/README.md`, Android packages (APK)) — the container members, the binary-AXML `AndroidManifest.xml` and the `classes.dex` declared header of one authored APK fixture, read out byte by byte against the authored oracle. Not covered: install/signature verification, dex validity or execution, provider (`inspect_android_package`) readiness or output, general AXML or ZIP-parser behavior beyond this fixture."

**Truth.** `corpus/README.md:34` is the C05 row and its surface string is exactly `Android packages (APK)`; the row's other columns are `—` (knowledge) and `fixtures/apk-r65` + the retained r65 rejected candidate (work evidence). The map is complete (row named by file and by its own surface title) and honest (the not-covered list matches what the entry actually does, and the fixture-scoped bound matches the README's legend at `README.md:21-24`, where a retained rejected candidate "is not coverage"). ✔

## Line 9 — `admission-status:` (entry:9) — PASS on admission state; OVER-CLAIMED on derivation

**What it says.** "candidate — the round-68 third-pass candidate: the round-67 v2 candidate's two `:244` anchors are corrected to `:245` … the spec line numbers are now derived by `corpus/derive_axml_anchors.py` rather than transcribed, and the readout bytes, oracle and fixture are unchanged since round 65. It is NOT admitted: the README C05 row stays `uncovered` until the dispatched wave's fresh seats return an all-criteria pass … on a fail the row stays `uncovered` and this file is marked `rejected`."

**True state.** Verified: `corpus/README.md:34` C05 status column = **`uncovered`**, knowledge column = `—` (the v3 is *not* named anywhere in the row), so the entry does not claim coverage it lacks. This matches `reports/round-68/claims.md` admission order step 1 ("Land the build with **no** README status flip") and the still-unsatisfied `C05_SINGLE_V3=yes` target. The two `:244` → `:245` corrections are real (r67 candidate `:244` at its lines 1 and 56; v3 has `:245` in both places, `:244` only as narrative). **The admission state is described truthfully and completely.**

**Over-claim (MEDIUM, ties to 1a).** "the spec line numbers are now derived … rather than transcribed" is too strong: every *symbol* line is derived, but the block range (237-253 ×4) is transcribed, undriven by any command, and false on the bytes (enum closes :263). Either derive the boundaries too (add `enum open` / `enum close` lines to `derive_axml_anchors.py`, which would then print 19 lines and force the S046 row's "17 output lines" to be updated) or narrow the sentence to "the cited symbol lines".

## Cross-cutting: header completeness (Q02 letter) — FAIL

1. **Two load-bearing body sources have no `source:` line.** entry:13 states the container analysis rests on "the APPNOTE 6.3.10 fixed record widths already mined as S032 (central directory header) and S034 (local file header)", and entry:35 restates it ("46-byte fixed part per S032 §4.3.12", "30-byte fixed part per S034 §4.3.7", with `payload_offset` derived "from the S034 §4.3.7 field list (readout.py:99-105), not assumed"). Body mention counts: `S032` ×3, `S034` ×4. Header `source:` lines: S038, S043, S045, S046, S041 — no S032, no S034. Both rows exist and are tier A (`SOURCES.md:47` tier=A, `SOURCES.md:48` tier=A), so this is an omission, not a missing source; but Q02 requires each header's `S###` row for the sources the entry stands on, and the container walk is one third of the entry's evidence.
2. **The lane's own convention is the opposite.** The admitted sibling `corpus/knowledge/round-63-zip-central-directory-evidence.md` has body source counts S032×12, S033×11, S034×16, S035×11 and header lines exactly `source: S032/S034/S033/S035` (:1-:4) — header set == body set. The v3 is the first C05 candidate whose body cites a source the header withholds.
3. **Its own §Q-map Q02 row is stale against its header.** entry:173 claims pass while enumerating the header as "(`source:` (S038, S043, S045, S041 with URLs/paths, pinned anchors and snapshot digests) …)" — it omits **S046**, which is present at entry:4, and is silent on S032/S034, so the self-check was not re-read after the header was extended. That is a self-audit defect independent of the substantive omission.

## Per-line verdict table

| entry line | header | verdict |
|---|---|---|
| :1 | `source: S038` | **FAIL** — row/tier/scope honest and all 17 symbol anchors reproduce; but "enum block lines 237-253" is false on bytes (237-263) at 4 sites, contradicts the cited row's `:239-250` (`SOURCES.md:52`) with no routed correction, and "re-opened … by this entry's author" is the round-67 author's act |
| :2 | `source: S043` | **PASS** — row docs/tier A, scope matches, lines 7-8 + sha + "line 5 is `older server.`" all exact (LOW: registry status is `queued`, not "mined"; used-by `—`) |
| :3 | `source: S045` | **FAIL** — "opened 2026-10-24 by this entry's author" is false (`SOURCES.md:91` = round-67 opening; `L1 revenger-r67`); quotes are de-tagged renderings, 0 literal hits on the pinned HTML (LOW) |
| :4 | `source: S046` | **PASS** — row own-work/tier A/opened 2026-10-24, script sha, 17 lines, exit-2 paths all verified (LOW: `used-by` is `—`) |
| :5 | `source: S041` | **PASS** — row own-work/tier A, all three digests + 947 bytes verified, "unchanged since `c7b7cf98`" blob-proven (LOW: `generator.py` named without a digest; used-by names only r65) |
| :6 | `verified-at:` | **PASS** — 2026-10-24 = round-68 declared date and build-commit date; `c7b7cf98` provenance exact; "captured from actual stdout" independently confirmed by the repaired gate (17 blocks, 0 problems) on current bytes |
| :7 | `recheck:` | **PASS (runnable)** — both commands exit 0 with the claimed 15-line/`507d79f8…` readout stdout and `--fact` single-line form; **gap**: derive half has no pinned stdout digest → supply `b02cfe54…` / 17 lines |
| :8 | `coverage-map:` | **PASS** — C05 named by file and exact README surface title (`README.md:34`); not-covered list honest and fixture-bounded |
| :9 | `admission-status:` | **PASS on state** — README C05 = `uncovered`, knowledge `—`, no flip, fail path stated; **over-claims** "line numbers now derived rather than transcribed" against the residual 237-253 range |

## Residual risk / verification gaps

- **Not falsified, but adjacent to item 5 (another seat's lane):** `spec_derived_struct_widths` prints `bytes_per_field` as literal dicts inside `readout.py`; the widths are cited to S038's field lists rather than parsed from the snapshot. Q11's "constants … are derived, not assumed" therefore rests on the citation, not on a derivation command. I record it as risk, not as a header finding.
- My `:244` residue check counts narrative mentions; a reviewer searching the v3 for the token will find two hits (entry:6, entry:9) and must read them as narrative, not anchors.
- I did not test the gate's `--self-test` or the C1 mutant/negative-control paths (C1 surface, other seats); my gate use was `--entry` only, exit 0.
- The nine header lines re-reproduce today (2026-10-25) from HEAD `4232235`; if the wave later edits this entry, re-run `derive_axml_anchors.py` + `readout.py` + the gate before adjudicating, because every verdict above is bound to entry sha256 `107e2d7483e57e64476ead408f2eb793f41e3eea5e3c96407763eadca6dfea5b`.
