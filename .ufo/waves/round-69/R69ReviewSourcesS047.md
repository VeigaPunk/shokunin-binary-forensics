ROW-CLEAN — S047 is a legal 11-column append whose pinned script+snapshot anchors reproduce byte-for-byte (exit 0, 20 lines), and whose `supersedes S046` is a verified strict superset (old 17 ⊂ new 20, no enum value changed) that repairs a real S046 gap (:237, :244 cited by the round-68 entry but absent from S046's 17-line output).

# R69ReviewSourcesS047 — registry-row review (S047)

Scope: the S047 row only, in /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md:61, read against the registry contract in that file's header (contract source: /home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md, frozen 2026-10-19). Nothing edited.

## A. Structural checks (contract "Census", run from lane root)

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin
$ grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
47
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md
0
$ awk -F'|' '/^\| S047 /{print "NF="NF}' corpus/SOURCES.md
NF=13
$ awk 'NR==61' corpus/SOURCES.md | grep -o '\\|' | wc -l
0
$ awk 'NR==61{print gsub(/\|/,"|")}' corpus/SOURCES.md
12
$ <duplicate-id census from the contract>
(no output)
$ <enum-violation / tier-inflation census from the contract>
(no output)
```

- 11 columns: PASS. NF=13 for a `|`-delimited table row = 12 separators = exactly 11 cells.
- No literal `|` inside a cell: PASS. The row line carries exactly 12 `|` characters (the 12 delimiters) and zero escaped `\|`; the escaped-pipe scan prints `0`. No HTML-entity pipe appears in the row text.
- id uniqueness / never-reused: PASS. 47 rows, duplicate-id census silent; S047 sits as the last registry row (line 61) immediately after S046 (line 60) and before `## Paths` (line 63) — append-only order holds.
- id cross-tree note (not a defect): the round-69 search log discloses the shokuknow staged-space collision rather than hiding it — `corpus/SOURCES.md:92`: "Id note: S047 collides with the shokuknow package's staged S047 space; adoption stays closed (wave-4), and a later adoption round renumbers the package by doc…". Within this lane's registry the id is the next unused, which is what the contract requires.

## B. Field-by-field verdicts (exact cell text)

| # | field | cell text (verbatim) | verdict |
|---|---|---|---|
| 1 | `id` | `S047` | CLEAN — `S`+3 digits, next unused, never reused, last row in append order. |
| 2 | `source` | `AXML anchor derivation (extended) — `corpus/derive_axml_anchors.py` over `corpus/snapshots/ResourceTypes.h`` | CLEAN — title — repo path(s), the form the contract prescribes for `own-work` ("a repo path or command"). The "(extended)" qualifier keeps the row's identity distinct from S046's. |
| 3 | `kind` | `own-work` | CLEAN — in the contract enum. |
| 4 | `tier` | `A` | CLEAN — the contract's tier-A definition explicitly includes "the lane's own re-runnable gate output"; this is a re-runnable command over committed bytes with a pinned digest. Not `community`, so no tier inflation. |
| 5 | `scope` | `the machine derivation of every S038 line number and enum value the round-69 C05 v4 candidate cites, including the enum-block bounds; the layout facts themselves rest on S038` | CLEAN — scope is stated, bounded, and carries the boundary clause that stops tier A from being read as tier A for the layout facts (those stay on S038). Scope is *true* of the artifact: every S038 line number the entry cites is in the 20-line stdout (check C below). |
| 6 | `anchor` | `script sha256 `74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa`, 20 output lines; snapshot copy sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f` (86255 bytes, byte-exact copy of the S038 snapshot `.ufo/waves/round-65/source-snapshots/ResourceTypes.h`); located quote from stdout: `enum RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100`` | CLEAN — locatable and reproduced (check C). Revision is named by content digest of both the command and its input, which is a tighter binding than a commit id for own-work. |
| 7 | `teaches` | `supersedes S046 — turns the transcribed spec line numbers, the enum-block bounds and the enum values into a re-derivable command: every cited symbol is searched in the pinned bytes and a missing or ambiguous symbol exits 2` | CLEAN — contract rule 2 requires a correction's `teaches` to open `supersedes S0NN —`; it does, verbatim. One grounded learner benefit (the defect class + the command that captures it). The exit-2 claim is real: `corpus/derive_axml_anchors.py:32,71` ("Read-only: … writes nothing", `sys.exit(2)`), and it fires — I triggered it by running the script with the snapshot absent (`exit=2`, `derive_axml_anchors: snapshot missing: …`). |
| 8 | `status` | `mined` | CLEAN by the contract's definition — `mined` = "cited by ≥1 path in `used-by`", and `used-by` is a real file that does cite it (`corpus/knowledge/round-69-apk-axml-byte-evidence.md:6` and `:177`). Consistent with precedent: S046, S043 and S039 are all `mined` off candidate/later-rejected entries. See residual risk R1 (`mined` here does not mean admitted). |
| 9 | `opened` | `2026-10-25` | CLEAN — ISO date, equal to the round that wrote the row (script-extension commit `da022615b052977f3b0c1b4c501564d977bf7b0d`, authored `2026-10-25 07:05:29 -0300`). |
| 10 | `recheck` | `on-release` | CLEAN (legal cadence per the contract's "ISO date or cadence (`90d`, `180d`, `on-release`)") and precedented for own-work rows (S013, S026, S030, S033). See residual risk R2 — for own-work over a frozen snapshot an `on-release` trigger has no upstream release event to fire on. |
| 11 | `used-by` | `corpus/knowledge/round-69-apk-axml-byte-evidence.md` | CLEAN — repo-relative, comma-separated form, file exists (35113 bytes), and it is the *only* row citing that entry (`awk … $12 ~ /round-69-apk-axml/` → `S047` only). Consistent with the entry's state: the entry declares `admission-status: candidate` (entry line 13), the README C05 row is still `uncovered` (`corpus/README.md:34`), and `reports/round-69/claims.md:80-82` keeps the flip contingent on the Q01–Q15 wave — so the row cites a candidate, and nothing in the registry or corpus advertises an admitted C05. |

## C. Anchor reproduction (the row's own numbers, re-derived)

```
$ sha256sum corpus/derive_axml_anchors.py
74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa  corpus/derive_axml_anchors.py
$ sha256sum corpus/snapshots/ResourceTypes.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
$ wc -c corpus/snapshots/ResourceTypes.h
86255 corpus/snapshots/ResourceTypes.h
$ cmp -s .ufo/waves/round-65/source-snapshots/ResourceTypes.h corpus/snapshots/ResourceTypes.h && echo byte-exact
byte-exact
$ python3 corpus/derive_axml_anchors.py > out; echo exit=$?
exit=0
$ wc -l out
20 out
$ grep -c 'enum RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100' out
1
```

Both pinned digests match the cells exactly; the size matches (86255); the copy is byte-exact against the S038 snapshot named in the cell; the run is exit 0 with exactly 20 lines; the "located quote from stdout" is present verbatim. Full 20-line stdout:

```
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
```

Composition matches the entry's own breakdown (`20 = 1 digest + 7 struct + 2 bounds + 8 enum + 2 attributeStart`).

Scope truth test — every S038 line number the cited entry states is in that stdout:

```
$ python3 -c "... extract ':'/'line N' integers 210..720 from corpus/knowledge/round-69-apk-axml-byte-evidence.md, subtract stdout set ..."
stdout line numbers: [218, 237, 239, 241, 244, 245, 246, 247, 248, 253, 263, 287, 461, 612, 621, 677, 686, 687, 707]
corpus/knowledge/round-69-apk-axml-byte-evidence.md | cited 210..720 not in stdout: []
```

All seven enum values the entry states (`0x0001`, `0x0003`, `0x0100`, `0x0101`, `0x0102`, `0x0103`, `0x0180`) are printed. Non-S038 numbers the entry carries (`readout.py:22/:166/:200`, `entry:41`, `l0-questions.md:42`) are readout/lesson/ledger references, not spec anchors, and fall outside the row's scope.

## D. `supersedes S046` correctness

Rule form: `teaches` opens `supersedes S046 —` (row cell 7). ✓

Substance — re-ran the superseded script from its pinned commit against the pinned snapshot and set-diffed:

```
$ git show 4232235:corpus/derive_axml_anchors.py > old.py
$ sha256sum old.py
bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249  old.py      # == S046's pinned sha
$ python3 old.py     # with corpus/snapshots/ResourceTypes.h beside it
exit=0 ; 17 lines
OLD-NOT-IN-NEW: []
NEW-ONLY: ['enum RES_XML_FIRST_CHUNK_TYPE : 244', 'enum block open : 237', 'enum block close : 263']
value-changed: {}          # every enum value present in both is identical
```

- Strict superset: PASS. 17 ⊆ 20; the three added lines are exactly the round-69 extension the row's `teaches` names ("the enum-block bounds and the enum values"). No value was silently changed.
- The supersede repairs a real overclaim, not a cosmetic edit: the round-68 entry cites `:237` (enum `{`) and `:244` (`RES_XML_FIRST_CHUNK_TYPE`) — `corpus/knowledge/round-68-apk-axml-byte-evidence.md` ("… `:237` (enum `{`) and `:244` (`RES_XML_FIRST_CHUNK_TYPE`)") — and neither number appears in S046's 17-line output. S046's scope sentence ("every … line number the round-68 C05 candidate cites") was therefore not true of its own artifact; S047's 20-line output covers both. The direction and necessity of the supersede are correct.
- S046 left `mined` in place: contract-legal. Rule 2 allows only `status`/`recheck`/`used-by` to change in place and does not require flipping the superseded row; precedent is S043→S039 (S039 still `mined`). See residual risk R3 for the reader-facing consequence.

## E. Residual risks and verification gaps (none is a row defect)

- R1 — `mined` is citation-based, not admission-based. S047's only `used-by` is a file carrying `admission-status: candidate`. This is exactly the contract's definition and matches S046/S043/S039, but if the C1 wave falsifies C05 the row's `mined` will keep pointing at a `rejected` entry (as S046's already does for round-68). Any later "mined ⇒ admitted" reading of the registry would be wrong; that reading is not in the contract.
- R2 — `recheck: on-release` has no trigger for the actual change vector of an own-work derivation. A pinned snapshot cannot "release"; the thing that can change is the script itself, and `on-release` will not fire on that. S046 used an ISO date instead. Legal either way (the contract enumerates the cadence and does not constrain it per kind); an ISO date would be the tighter choice if the wave wants one convention for own-work rows.
- R3 — after the supersede, two `mined` rows pin the same path with different digests. S046's pinned `bce497d6…` is no longer the working-tree `corpus/derive_axml_anchors.py` (`74d4c0d9…`); it resolves only via `git show 4232235:corpus/derive_axml_anchors.py` (verified — that blob hashes to S046's pin). Contract-legal (append-only, supersede marker present), but a reader resolving S046's anchor from the corpus tree alone hits a mismatch with no in-row pointer. A round-lesson old→new note would close it without editing S046.
- R4 — verification gap: the contract's rule 1 requires the round lesson's `## Gate` to record, for every new row, the access date and a ≤25-word quote with its location. `corpus/lessons/round-69.md` does not exist yet (`ls corpus/lessons/` ends at `round-68.md`), and no `## Gate` record for round 69 exists under `reports/round-69/` or `.ufo/waves/round-69/` (`grep -rln "## Gate"` → empty). `reports/round-69/claims.md:85-86,219-231` records the row's existence, sha and supersede, and the row itself carries the ≤25-word located quote, so the substance is on disk — the Gate duty is pending at round close, not satisfied at build time. I cannot verify it from this seat.

## F. Tooling

No tool installed or upgraded for this review; all checks used existing binaries (`awk`, `grep`, `cmp`, `sha256sum`, `git show`, `python3` stdlib). Scratch under `/tmp/revenger-r69-*` and the `/tmp/snapshots/` copy were removed before returning; all evidence above is reproducible from the lane tree with the commands as written.
