# W2VerifySourcesTable — `corpus/SOURCES.md` conformance after the S032/S033 append

Seat: `revenger-r63.W2VerifySourcesTable` · lane: `revenger-shokunin` ·
target: `/home/vgpnk/Projects/shokunin/revenger-shokunin` ·
lane tip attacked: **`db55bd6488e24e956df5818ae34c2a043d7ddc12`** (the
immediately-following integration commit after the build state `2a34e45562d965f9c8d32f6a27d2f2efa2e7d04e`).

Attacks: **C1 coverage K** — the `corpus/SOURCES.md` registry table as committed
after the S032/S033 append. Specifically the seven frozen census commands from
`CORPUS.md` §"Census", the maintained `scripts/sources-census.sh validate` CLI,
the claim "S032/S033 are the only new rows", the claim "S033's `used-by` names
the entry", and the claim "old rows are untouched except logged changes".

## Verdict

**Table is CONFORMANT as a table at both tips; two grounding defects were
located in the two new rows at the assigned tip `db55bd6`, and both were
repaired by the append-only follow-up commit `aaa0463` that landed while this
seat was running. The defects were visible only when the row text is compared
against the entry that cites it — the census itself cannot see them.**

**Read §11 first if judging the current tip:** at `aaa0463` the census is still
clean and validate still exits 0, but the warning set has grown to four W04s
while the frozen disclosure still says three.

- All seven frozen census commands: **clean**.
- `sources-census.sh validate --root … revenger`: **exit 0**, exactly the three
  disclosed W04s **S024 / S028 / S029**, nothing else.
- S032/S033 are the **only** new rows at the committed tip; every pre-existing
  line of `corpus/SOURCES.md` is **byte-identical** to the claim base.
- S033's `used-by` **does** name the entry.
- **D1 (blocking, C1/Q01):** the committed **S032** row's `scope` and `anchor`
  cells do **not** cover §4.3.7 (local file header record layout), which the
  committed entry uses load-bearingly and attributes to S032.
- **D2 (medium, C1/rule 1):** the committed **S033** row's `source` cell omits
  `corpus/live/runs/20261012T164246Z/LEDGER.md`, which the entry cites as S033
  and prints a digest for; and S033 has **no ≤25-word located quote** anywhere
  in the committed round lesson's `## Gate`, which contract v1 rule 1 requires
  for *every* new row.

D1 and D2 are **independently located here** and corroborate
`W2AttackEntryQ01` (which reported them from the entry side). The census is
nonetheless clean — that is the point: the census cannot detect a scope/anchor
gap or a missing source path, so "census exit 0" is not evidence that the rows
ground the entry.

---

## 1. The seven frozen census commands — re-run by me, on the committed bytes

Contract source: `/home/vgpnk/Projects/shokunin/CORPUS.md` §"Census — run from
the lane root (tested 2026-10-19 on a synthetic table)". The seven commands were
run **verbatim** from the frozen block, with `cwd` = the lane root, against the
**committed** file (`git show db55bd6:corpus/SOURCES.md`).

| # | command (frozen) | observed on committed `db55bd6` | expected | result |
|---|---|---|---|---|
| 1 | rows (spacing-tolerant) `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` | **33** | 31 base + 2 new | PASS |
| 2 | malformed rows `awk … NF!=13 … END{print n+0}` | **0** | 0 | PASS |
| 3 | tier histogram | **A=31 C=2** | no B/invalid | PASS |
| 4 | status histogram | **mined=28 queued=1 rejected=4** | enum only | PASS |
| 5 | duplicate ids (`… \| sort \| uniq -d`) | *(prints nothing)* | empty | PASS |
| 6 | enum violations + tier inflation | *(prints nothing)* | empty | PASS |
| 7 | mined rows whose `used-by` paths do not exist | *(prints nothing)* | empty | PASS |

Raw transcript (committed file, `cwd` = lane root):

```
rows: 33
malformed: 0
tier: A=31 C=2
status: mined=28 queued=1 rejected=4
dupids: []
enum: []
missing: (none)
```

Command 7 was run with `cwd` = lane root so that the repo-relative `used-by`
paths resolve; every path printed by the extractor exists on disk, including
both new rows' paths (`corpus/knowledge/round-63-zip-central-directory-evidence.md`,
`corpus/lessons/round-63.md`).

**Cross-check:** the same seven commands run against the **worktree** copy
(after the mid-wave drift described in §5) also print clean — 35 rows, 0
malformed, `A=33 C=2`, `mined=30 queued=1 rejected=4`, empty dup-ids, empty
enum, empty missing-path list.

## 2. Maintained CLI: `sources-census.sh validate`

```
$ cd /home/vgpnk/Projects/shokunin
$ ./scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger
revenger	W04	S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes
revenger	W04	S028 duplicate url github.com/ethereum/execution-specs/tree/v2.20.0/src/ethereum/forks/osaka/vm across scopes
revenger	W04	S029 duplicate url tc39.es/ecma262 across scopes
revenger	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
EXIT=0
```

**exit 0, exactly the three disclosed W04s S024/S028/S029, no E-code, no
unlisted warning.** This matches the frozen disclosure in
`reports/round-63/claims.md:125` ("census before (exit 0, 31 rows, three
disclosed W04s: S024/S028/S029) and after (exit 0 required)").

`census` mode on the same target: `rows 33 / tier.A 31 / tier.C 2 /
status.mined 28 / status.queued 1 / status.rejected 4 / FLEET.missing 0`,
exit 0.

The `--file` mode resolves `used-by` relative to the file's own directory, so
running it against a copy outside the lane reports spurious E11s for every row;
re-run with the copy placed at `<dir>/corpus/SOURCES.md` and the real
`corpus/` siblings symlinked in, the committed file validates as `ok` with the
same three W04s and exit 0. (Method note, not a defect.)

## 3. "S032/S033 are the only new rows"

```
$ git diff --numstat 2a34e45 db55bd6 -- corpus/SOURCES.md
4       0       corpus/SOURCES.md
$ git diff 2a34e45 db55bd6 -- corpus/SOURCES.md
@@ -43,6 +43,8 @@
+| S032 | PKWARE APPNOTE.TXT — .ZIP File Format Specification — …
+| S033 | Authored archive-r2 bytes and the saved archive inventory record — …
@@ -68,6 +70,8 @@
+- 2026-10-23, archive specification and firmware premise (rows C06/C2; S032, S033). …
+
```

Four insertions, zero deletions: the two new rows plus one search-log bullet
plus one blank line. **No existing row was modified, moved or removed.**
Row-id sequence at the tip is contiguous `S001 … S033` with no gap and no
reuse (`awk … print $2` → `S001 S002 … S033`); no `S034`/`S035` id is spent at
the committed tip, matching the lesson's "contiguous pair S032 + S033 with no id
skipped" (`corpus/lessons/round-63.md:135`).

**"Old rows untouched except logged changes" — confirmed, and stronger than
claimed:** no old row's `status`, `recheck` or `used-by` was edited at all in
this commit, so there is nothing unlogged. I verified byte-identity line by line
for every pre-existing line (sha256 of each of lines 1–45 at `2a34e45` vs at
`db55bd6`): **no line differs**. The only status change the round performed is
the *draft-time → land-time* flip of S032/S033 (`queued`/`—` → `mined`/
`used-by`), performed inside the same commit as the entry so that the E11
ordering holds; it is logged old→new in the lesson
(`corpus/lessons/round-63.md:139-147`). No `supersedes` row was needed.

## 4. "S033's `used-by` names the entry" — confirmed

Committed S033 row (line 47), cell by cell:

| cell | value |
|---|---|
| id | `S033` |
| source | Authored archive-r2 bytes and the saved archive inventory record — `corpus/fixtures/archive-r2/fixture.zip`, `corpus/fixtures/archive-r2/truth.json`, `corpus/live/runs/20261012T164246Z/artifact-inspection.json` |
| kind | `own-work` |
| tier | `A` |
| scope | byte content of one authored ZIP archive and the literal saved fields of one archive inventory record for it, at base commit `55bcb6e1aeb4d42923a4e98db6580f67142b41ac`; added scope is central-directory-to-oracle-to-saved-record correspondence, not provider accuracy or completeness |
| anchor | fixture sha256 `857989f5…`, truth.json sha256 `7df773bf…`, saved record sha256 `2fec924b…`, Evidence `ev_5cc39f35…`, nested `ev_cc681c2a…` |
| teaches | A byte readout of one archive's central directory can be checked field by field against an independent oracle and against one saved record's literal fields, without claiming the record is complete or authentic. |
| status | `mined` |
| opened | `2026-10-23` |
| recheck | `on-release` |
| **used-by** | **`corpus/knowledge/round-63-zip-central-directory-evidence.md, corpus/lessons/round-63.md`** |

`used-by` names the entry file explicitly, and the entry exists on disk. Both
`used-by` paths of S032 and S033 resolve (census command 7 silent). The
`Evidence` ids and the three digests in the anchor cell are **true**: I re-read
the saved record and found exactly those two evidence ids
(`ev_5cc39f356009773bb3d8a214ec39536a99f0799f6709f4cd7bb3badb33c6cf7d` top-level,
`ev_cc681c2a03da4e9901275c1425fb1f726cca78bbdbec3defb13b6a0ac8ad156b` nested),
and `sha256sum` on the three files reproduces the row's digests exactly.

S032's `teaches` cell is also factually checkable against the cited spec
tables and is **correct**: summing the §4.3.12 field widths gives a 46-byte
central-directory header with `crc-32` at offset 16 and `relative offset of local
header` at offset 42; the §4.3.16 table gives a 22-byte EOCD record with the two
total-entry counts at offsets 8 and 10. The archive's own bytes agree
(EOCD at 2942 with 2/2 at +8/+10; first CD header at 2828).

## 5. D1 — S032's committed scope/anchor do not cover §4.3.7 (blocking for C1/Q01)

Committed S032 row (line 46):

- `scope`: "central directory file header and end-of-central-directory record
  field layout for one authored ZIP archive: signature values, field order,
  length fields, CRC-32 and local-header offset"
- `anchor`: "§4.3.3, §4.3.12, §4.3.16, §4.4.7, §4.4.10-4.4.12, §4.4.16,
  §4.4.21-4.4.22; version 6.3.10 (revised Nov 01, 2022)"

**§4.3.7 (Local file header) appears in neither cell**, and the scope names two
records, not three. But the committed entry cites S032 for the local file
header load-bearingly:

- `corpus/knowledge/round-63-zip-central-directory-evidence.md:1` — "scope: **the
  local file header**, central directory file header and end-of-central-directory
  record field layout … anchors: **§4.3.7 (local file header, fixed field-width
  list)**, §4.3.12 …"
- `:67` (item 5) derives the **30-byte** local-header fixed part and the
  name/extra-length offsets **26 / 28** from §4.3.7;
- `:71` and `:254` (fact `spec_derived_field_offsets`) carry
  `"source_anchor": "APPNOTE 6.3.10 §4.3.7, §4.3.12 and §4.3.16 field tables (S032)"`
  and a `local_header_field_offsets` map;
- `:360` the readout bakes `LFH_FIELDS` in, commented "transcribed from the
  PKWARE APPNOTE field tables";
- `:645-646` two §4.3.7 quotes appear in the entry's `## Sources` bullet for S032.

The row's scope ("central directory file header and end-of-central-directory
record") does not license "the local file header". Per contract v1, `tier` is
"scoped to `scope`, never global", and Q01 requires each load-bearing claim to
rest on a row that is tier A **for that claim's scope** — so the row's declared
scope is narrower than the entry's use of it. The frozen contract
(`reports/round-63/claims.md:33-34`) also describes S032 as the
"central directory / EOCD field layout" row, i.e. the **contract agrees with
the row**, and the entry is the side that over-claims.

I verified the §4.3.7 content is present and that the entry's numbers are right
— so the fix is to widen the row (or add a scoped companion row), not to change
the entry's arithmetic. In the pinned snapshot
`.ufo/waves/round-63/source-snapshots/appnote.txt` (sha256
`0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`):

```
387:    4.3.7  Local file header:
389:        local file header signature     4 bytes  (0x04034b50)
...
398:        file name length                2 bytes
399:        extra field length              2 bytes
```

Summing those widths: `sig 4 + ver 2 + gpb 2 + cm 2 + t 2 + d 2 + crc 4 + cs 4 +
us 4 + fn 2 + ex 2 = 30`; `file name length` at offset **26**, `extra field
length` at offset **28** — exactly what the entry asserts. The defect is the
row's scope/anchor coverage, not the arithmetic.

Corroborating: the **committed** round lesson mentions §4.3.7 **zero** times
(`git show db55bd6:corpus/lessons/round-63.md | grep -c '4\.3\.7'` → `0`), so
the Gate's located-quote list for S032 (nine quotes, lines 52–60 of the lesson)
does not include a §4.3.7 quote either.

## 6. D2 — S033's `source` cell omits LEDGER.md, and S033 has no located Gate quote

**(a) Missing source path.** The committed S033 `source` cell lists three files
(`fixture.zip`, `truth.json`, `artifact-inspection.json`). The committed entry
treats `corpus/live/runs/20261012T164246Z/LEDGER.md` as part of S033:

- entry `:2` — "S033 — Authored archive-r2 bytes, the authored oracle and the
  saved archive inventory record — … `artifact-inspection.json`,
  `corpus/live/runs/20261012T164246Z/LEDGER.md` (own-work, tier A …)";
- entry `:44` prints the ledger digest
  `05042a555f91511c9c191565d92f83527f54d1c9b14de331587f4cbffff9e6cb`
  (I re-ran `sha256sum` on that file — the digest is correct);
- entry `:700` (Q04) rests on it: "the `rea-agents@6.4.0` run that produced the
  saved record, **as recorded in the run's own `LEDGER.md`**, is credited with …".

The entry's own proposed row text for S033 (entry `:656`) **does** include
`LEDGER.md` in the source list and the ledger digest in the anchor — the
committed row dropped both when L1 pasted it. So the committed row is narrower
than both the entry's citation and the entry's own draft of the row.

**(b) Missing rule-1 quote.** Contract v1 rule 1: "The round lesson's `## Gate`
records, for every new row, the URL, the access date, and a ≤25-word quote with
its location grounding `teaches`." For S032 the committed lesson has nine
located quotes (lines 52–60). For **S033** the committed lesson's block
(lines 116–126) gives paths, digests and the base commit, but **no located
quote** of any kind — I grepped the committed lesson for quoted literals
≥10 chars: every hit is an S032/§-quote, the zipfile-page footer, or prose in
the Mistakes/debt tables. Round-62 sets the precedent that own-work rows do get
a located quote in the lesson (`corpus/lessons/round-62.md:76-85`: S030 →
`corpus/fixtures/js-r3/index.js:1` → "const { rot13, checksum } = require('./transform');";
S031 → `limitations[4]` → "Original carrier and decoded bytecode SHA-256 are
distinct identities; …").

S033's `teaches` ("…can be checked field by field against an independent oracle
and against one saved record's literal fields, without claiming the record is
complete or authentic") is therefore ungrounded by any located quote in the
committed lesson.

## 7. Adjacent defect found while grounding §4.3.7 (entry-side, corroborating)

The entry's `§Reproduce` block (entry `:291-292`) claims:

```
$ printf '%s\n' "local file header signature 4 bytes (0x04034b50)" | wc -w
8
```

The actual output is **7** (I re-ran it; `wc -w` counts whitespace-separated
tokens: "local file header signature 4 bytes (0x04034b50)" = 7). This is the
same "a count carries its command" class as `W2AttackEntryScope`'s finding; I
reproduce it independently. It is a claim whose stated output is wrong, and it
sits inside the §Sources quote block that grounds S032.

Also note the committed lesson's §4.4.7 quote locator is off by one line: the
lesson cites "§4.4.7 (lines 912–913)" for the quote "value is put in the data
descriptor and in the central directory." — that text actually spans snapshot
lines **913–914** (line 912 ends "…and the correct"). The quote text itself is
verbatim in the snapshot; only the line locator is wrong.

## 8. Non-defects checked and cleared

- **`## Paths` section.** S032/S033 appear in no Paths sequence. **Not a
  defect**: contract rule 4 says "There is no row quota", the Paths section is
  an ordered study-sequence list with no per-row coverage requirement, and the
  precedent is a `mined` row with no Paths entry (S015 — `mined`, used-by
  `corpus/knowledge/digest-scope-versus-provenance.md`, absent from Paths).
- **Tier/scope sanity.** S032 `spec`/A is appropriate (a specification read at
  its pinned revision is primary for field layout); S033 `own-work`/A matches
  the lane's own re-runnable gate output; `community` never appears at tier A
  (census command 6 silent); no `B` or invalid tier exists.
- **Enum conformance.** All kinds are in the contract's ten-value enum; all
  statuses in {queued, mined, rejected}; `recheck` values are ISO/`Nd`/symbolic
  cadences (`on-release` is a legal symbolic cadence) — the CLI reports no
  E08/E09.
- **Duplicate id / duplicate URL+scope.** No duplicate id. No duplicate URL+scope
  pair (S032's URL is unique in the committed table), so no E04.
- **Row-shaped source outside `## Registry`** (E12): none.
- **Re-open of the new row's source (independent of `W2ReopenS032`).** I
  re-fetched the row's URL myself: `https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT`
  → HTTP **200**, `Content-Length` **174585**, sha256
  `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`, byte-identical
  (`diff -q` silent) to the committed snapshot, version line `6.3.10` /
  `Status: FINAL - replaces version 6.3.9` / `Revised: Nov 01, 2022`. The
  fallback `https://pkware.com/documents/casestudies/APPNOTE.TXT` redirects to
  `APPNOTE-6.3.9.TXT` (173575 bytes, sha256 `c7cf1fec…`) — the different
  revision the row's opener recorded. All section anchors named in S032's
  `anchor` cell exist in the snapshot: §4.3.3 (line 348), §4.3.12 (511),
  §4.3.16 (632), §4.4.7 (900), §4.4.10–4.4.12 (937–939), §4.4.16 (981),
  §4.4.21–4.4.22 (1032, 1041).

## 9. Worktree drift observed mid-verification (dependency to record, not a defect at the tip)

While this seat was running, the **worktree** changed under me (files modified
at 00:05–00:07 local, after my first census pass at ~00:00):

```
$ git status --porcelain corpus/
 M corpus/SOURCES.md
 M corpus/lessons/round-63.md
 M corpus/live/runs/round-63/LEDGER.md
$ git diff corpus/SOURCES.md   →  +| S034 | … +| S035 | …
```

The uncommitted state adds **two further rows** (S034 = APPNOTE §4.3.7 scoped
re-open; S035 = the saved round-2 archive ledger) and rewrites the lesson's
Gate accordingly. This is an in-flight L1 repair aimed at D1/D2, not part of the
committed tip I was asked to attack, and it is **not committed** — my verdict
above is against `db55bd6` as instructed.

I verified the drift separately so the integrator can use it: on the worktree
file all seven census commands are still clean (35 rows, 0 malformed,
`A=33 C=2`, `mined=30 queued=1 rejected=4`, empty dup-ids / enum / missing-path
lists) and `sources-census.sh validate --root … revenger` still exits **0** —
but the warning set grows to **four** W04s (S024, S028, S029 **and S034**,
"duplicate url pkware.cachefly.net … across scopes", because S034 reuses S032's
URL at a different scope). Two consequences for the judge:

1. The frozen disclosure "three disclosed W04s: S024/S028/S029"
   (`reports/round-63/claims.md:125`) becomes **stale** the moment S034 lands.
   S034's same-URL/different-scope shape matches the existing S028/S029/S030/S031
   precedent (a scoped re-open beside, not a `supersedes` correction), so W04 —
   not E04 — is the right code and exit 0 is preserved; the *disclosure text*,
   not the row, needs the update.
2. On the worktree state the S032/S033 rows are **no longer** the only new rows
   (S034/S035 exist), so the "only new rows" claim is true at `db55bd6` and
   false in the worktree. Whichever commit L1 lands, that claim must be
   re-stated against the new tip.

Also worth L1's attention while the repair is open: the worktree S035 row has
no located Gate quote either, and the S034 row's `used-by` names only the entry
(not the lesson), which is allowed (mined requires ≥1 path).

## 10. Scope, method, and limits

- **What I ran:** the seven frozen census commands (verbatim from `CORPUS.md`),
  `scripts/sources-census.sh validate` and `census`, `git diff`/`git show`
  (read-only) against `2a34e45` → `db55bd6`, `sha256sum`, `awk` field-width
  summation against the pinned APPNOTE snapshot, one read-only `curl` re-fetch
  of the row's URL and of its documented fallback, and a byte read of
  `corpus/fixtures/archive-r2/fixture.zip`.
- **What I did NOT do:** no target execution (no verifier, no producer, no
  `npx rea-agents`), no model arguments, no git/jj mutation, no commit, no edit
  to any product file, `corpus/SOURCES.md`, `MANIFEST.json`, fleet files or
  sibling lanes. The only file I wrote is this report. `~/.omp/agent/config.yml`
  untouched.
- **Tooling:** none installed or upgraded. No `pacman` (host-wide pacman gate
  is paused). No `uv tool install`, no global npm install, no binary download.
  Only pre-existing tools: `bash`, `git`, `awk`, `sha256sum`, `grep`, `sed`,
  `python3` (3.x, stdlib `struct`/`json`/`re`/`hashlib`), `curl`, `cmp`/`diff`.
  `gawk` is required by `sources-census.sh` and was present.
- **Scratch:** `/tmp/revenger-r63-sourcestable/` (committed SOURCES.md copy plus
  a `corpus/` mirror for `--file` mode) and `/tmp/r63-appnote.txt`,
  `/tmp/r63-pkware-com.txt` (the two fetches). All removed after this report
  lands.
- **Not re-derived here (other seats' scope):** the frozen counter values
  (`K_HELD`, `F_COVERAGE`, `C3_RECEIPT_KILLED_ATTRIBUTED`), the README C06 flip,
  the C2 firmware record envelope, and the C3 verifier patches. My verdict is
  confined to the registry table.
- **One dependency I could not fully close:** the census's `used-by` existence
  check is path-relative and the CLI's `--file` mode resolves paths relative to
  the file's directory, so a straight `--file` run outside the lane reports
  spurious E11 for every row. I re-ran with a `corpus/` mirror so the paths
  resolved truthfully; the committed file validates clean either way.

## 11. Re-verification at the new tip `aaa0463` (the drift landed mid-seat)

The uncommitted drift described in §9 was committed while this seat was still
running, as:

```
aaa0463 round-63: corrected C1 entry (wc-w fix, S034/S035 citations, derived
         metadata), S034+S035 registry rows, LEDGER receipt-pin fix,
         lesson Gate+M35 updates
```

I re-ran the whole verification against that tip. The repair **is** an
append-only repair: `git diff --numstat db55bd6 aaa0463 -- corpus/SOURCES.md`
= `2  0` (two inserted rows, **zero deletions**), and `diff` of the S032 row and
the S033 row between the two commits reports **identical**. S032 and S033 were
not edited in place; two new rows were added.

Re-run census at `aaa0463` (all seven frozen commands, `cwd` = lane root):

| # | command | observed at `aaa0463` | result |
|---|---|---|---|
| 1 | rows | **35** | PASS |
| 2 | malformed (NF≠13) | **0** | PASS |
| 3 | tier histogram | **A=33 C=2** | PASS |
| 4 | status histogram | **mined=30 queued=1 rejected=4** | PASS |
| 5 | duplicate ids | *(empty)* | PASS |
| 6 | enum / tier-inflation | *(empty)* | PASS |
| 7 | missing `used-by` paths | *(empty)* | PASS |

CLI at the new tip:

```
revenger	W04	S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes
revenger	W04	S028 duplicate url github.com/ethereum/execution-specs/tree/v2.20.0/src/ethereum/forks/osaka/vm across scopes
revenger	W04	S029 duplicate url tc39.es/ecma262 across scopes
revenger	W04	S034 duplicate url pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT across scopes
revenger	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
EXIT=0
```

**Still exit 0, still census-clean — but now FOUR W04s, and the frozen
disclosure at `reports/round-63/claims.md:125` still reads "three disclosed W04s:
S024/S028/S029"** (`git diff db55bd6 aaa0463 -- reports/round-63/claims.md` is
empty: the claim file was not updated). S034 reuses S032's URL at a different
scope, which is the same shape as the existing S028/S029/S030/S031 re-opens, so
W04 (not E04) is the correct code and exit 0 is preserved — but the *disclosure
sentence* is now stale. That sentence is the wave's own frozen text and I do not
edit it; I record it as a live discrepancy for the judge/L1.

**What the repair fixed (verified at `aaa0463`):**

- **D1 is repaired.** New row **S034** (spec, tier A) carries the §4.3.7
  local-file-header scope, with anchor "§4.3.7; version 6.3.10 (revised Nov 01,
  2022); snapshot lines 387-399, sha256 `0b993022…`" and `teaches` "Local-header
  layout scope beside S032 — the local file header is a fixed 30-byte record
  whose file name length sits at offset 26 and extra field length at offset 28…".
  The entry now has a **separate `source:` line for S034**, its §Sources S032
  bullet **no longer lists §4.3.7** (grep for `4.3.7` inside the S032 bullet
  returns 0), and the two §4.3.7 quotes moved under the S034 bullet. The row
  S032 itself was left byte-identical — the append-only discipline held. The
  §4.3.7 offsets in S034's `teaches` are correct: summing the §4.3.7 field
  widths gives 30 bytes with `file name length` at 26 and `extra field length`
  at 28, which I recomputed from the snapshot table myself.
- **D2(a) is repaired.** New row **S035** (own-work, tier A) carries
  `corpus/live/runs/20261012T164246Z/LEDGER.md` (sha256 `05042a55…`, 3959 bytes)
  as a provenance-only scope with `teaches` "The saved record's own ledger names
  the recorded layer for the rea-agents@6.4.0 archive-route attribution; it
  supports no derived value in the entry". The entry now has a **separate
  `source:` line for S035**, and S033's source line no longer names the ledger.
  The ledger's `used-by` path resolves and the digest reproduces.
- **The `wc -w` defect is repaired** at `aaa0463`: the §Reproduce block now
  prints `7` for the §4.3.7 signature quote, which is what the command actually
  outputs (I re-ran it: 7).

**Residual defects still present at `aaa0463` (small, located):**

1. **§4.4.7 quote locator still off by one line.** The lesson still reads
   "§4.4.7 (lines 912–913): 'value is put in the data descriptor and in the
   central directory.'" — that text spans snapshot lines **913–914** (line 912
   ends "…and the correct"). The quote text is verbatim; only the locator is
   wrong. `corpus/lessons/round-63.md:59`.
2. **S033 and S035 still have no ≤25-word located quote in the lesson's
   `## Gate`.** The Gate's located-quote list (lines 52–60) is still entirely
   S032 sections; S034 got one (7 words, snapshot line 389, §4.3.7), but S033
   and S035 got only paths, digests and scope sentences. Contract v1 rule 1 asks
   for a located quote for *every* new row; the round-62 own-work precedent
   (S030/S031) supplied them.
3. **"S032/S033 are the only new rows" is now false at the tip** — it was true
   at `db55bd6` (which is what this seat was asked to attack) and is false at
   `aaa0463`, where S034 and S035 also landed. Any claim text that asserts
   "the only new rows" must now name four rows, or be restated against the
   specific commit it describes.

## 12. Bottom line for the canonical judge

1. **Table conformance: CONFIRMED at both tips.** At the assigned tip
   `db55bd6`: seven census commands clean, CLI validate exit 0 with exactly the
   three disclosed W04s (S024/S028/S029), S032/S033 the only new rows, every
   old row byte-identical to the base, S033's `used-by` names the entry,
   S032's `teaches` and S033's digests/Evidence ids factually true against the
   sources. At the later tip `aaa0463` (the repair landed mid-seat): still
   census-clean (35 rows / 0 malformed / A=33 C=2 / mined=30 queued=1
   rejected=4 / no dup ids / no enum violations / no missing `used-by` paths)
   and validate still exits 0.
2. **D1 (located at `db55bd6`, repaired at `aaa0463`):** committed S032
   `scope`/`anchor` omit §4.3.7 / the local file header record layout that the
   committed entry uses load-bearingly and attributes to S032 (entry `:1`,
   `:67`, `:71`, `:254`, `:360`, `:645-646`); the frozen contract itself scopes
   S032 to central-directory/EOCD. The entry's 30/26/28 arithmetic was right;
   the row's declared scope did not cover it, and the committed lesson had no
   §4.3.7 quote. **Repair at `aaa0463`**: new append-only row **S034** carries
   the §4.3.7 scope with a 7-word located quote; the entry cites S034 for the
   §4.3.7 quotes; the S032 row was left byte-identical.
3. **D2 (located at `db55bd6`, repaired at `aaa0463`):** committed S033 `source`
   omitted the archive `LEDGER.md` that the entry cited as S033 and printed a
   digest for, and S033 had no ≤25-word located quote in the committed lesson's
   `## Gate` (rule 1), unlike S032 and unlike the round-62 own-work precedent.
   **Repair at `aaa0463`**: new append-only row **S035** carries the ledger as
   a provenance-only scope and the entry cites S035 for it.
4. **Still open at `aaa0463` (small, located):** (a) the lesson's §4.4.7 quote
   locator (lines 912–913) should be 913–914; (b) S033 and S035 still carry no
   ≤25-word located quote in the lesson's `## Gate`; (c) the entry's `wc -w`
   claim of 8 was wrong (actual 7) — **fixed at `aaa0463`**.
5. **Live discrepancy to carry forward:** the new tip raises the warning set to
   **four** W04s (S024, S028, S029 **and** S034, the last because S034 reuses
   S032's URL at a different scope — the same shape as the existing S028/S029/
   S030/S031 re-opens, so W04 not E04 and exit 0 is preserved), while the
   frozen disclosure at `reports/round-63/claims.md:125` still says "three
   disclosed W04s: S024/S028/S029" and that file was not updated. Likewise the
   phrase "S032/S033 are the only new rows" is true at `db55bd6` and false at
   `aaa0463`. Neither file is mine to edit; both are recorded here.
6. **Method limit:** the census cannot see a scope/anchor gap or a missing
   source path — that is why a clean census plus exit 0 did not by itself make
   C1 pass at `db55bd6`. The row-vs-citing-entry comparison, not the census, is
   what located D1 and D2.
