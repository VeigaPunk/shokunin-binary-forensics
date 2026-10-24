# R64ReviewSources — S036 snapshot re-fetch + S036/S037 row conformance review

Axes: provenance integrity · contract-v1 conformance · zero mutation.
Seat: independent reviewer (no author, corrector, or integrator role). Read the
frozen contract, counter, red-before receipt, the S036 brief, `corpus/SOURCES.md`
and its fleet contract v1 before acting. Read-only git only; no git/jj mutation,
no commit, no index write.

## Verdict at a glance

| Item | Verdict |
|---|---|
| S036 source re-fetch, byte-identical vs the lane snapshot | **PASS** — sha256 `e422b481…93609` both sides, `cmp` byte-identical, git blob identity `1528191…227ed` matches GitHub contents API at tag `rea-agents-6.5.0` |
| S036 provenance sidecar (`source-snapshots/rea-firmware-guide.provenance.json`) | **PASS** — every asserted field independently reproduced (URL/status/bytes/sha/tag commit/blob/etag/main drift) |
| Located-quote set grounding the future S036 row | **PASS** — Q1–Q11 all found at the claimed line spans, all ≤25 words (max 21) |
| S036 registry row review | **PASS** (draft `sources-rows-draft.md`, sha256 `6e66fd3e078088fedcc0816fbf2e52262e0a644036014eaef3b7092387ba3d20`, 2 rows, NF=13 each) — conditional on the landing flip in §3.3 |
| S037 registry row review | **PASS** (same draft) — conditional on the landing flip in §3.3 |

The draft was absent when this seat started (three polls, 01:17Z–04:19Z) and
landed at 04:22Z; it was then graded in full (§3). Both verdicts are content
verdicts on the draft text, not on the landed registry.

## Findings, by severity

### RESOLVED (was BLOCKER)

1. **Draft artifact arrived late; now graded.** `sources-rows-draft.md` was
   absent at 01:17Z, 01:19Z and 04:19Z (`R64SourcesRows` still "reading the
   brief"), then written at 04:22Z. File sha256
   `6e66fd3e078088fedcc0816fbf2e52262e0a644036014eaef3b7092387ba3d20`, 3873 bytes,
   two registry data rows. It was graded in full in §3 (both rows PASS). No
   verdict in this report rests on the author's self-report: every digest, line
   span and census value below was recomputed by this seat.

### HIGH

2. **Anchor identity trap: the committed round-63 guide snapshot is `main`, not
   the pinned tag; it must never be reused as the S036 anchor.** Independently
   re-fetched, same minute:
   - tag `rea-agents-6.5.0` → HTTP 200, `content-length: 10695`, sha256
     `e422b4816b1dbc912680afefb8e23acfd8ead4aea08c3d722d4ccb5207933609`;
   - `main` → HTTP 200, 15474 bytes, sha256
     `d4a25c8569b37c3d030431333db08fc459af54a163af7815b4505cce2f16a898`.
   `.ufo/waves/round-63/source-snapshots/rea-firmware-guide.md` is byte-identical
   to my `main` fetch (`cmp` clean) and therefore is **not** the tag document.
   A row whose anchor carries `d4a25c85…` or "main" cites bytes the 6.5.0
   producer never shipped → FAIL. Required anchor token: tag name +
   commit `3b79af28e80785afce9f5998d8f03289402a1847` + sha256 `e422b481…93609`.

3. **Status ↔ used-by coupling can break the frozen census.** Contract v1 census
   (contract §Census, last check) prints `missing: <path>` for every `used-by`
   path of a `mined` row that does not exist. The claims' fallback is explicit:
   if C1 falsifies, C07 flips `frontier → uncovered` and the new entry may not
   land. A row landed as `mined` while naming
   `corpus/knowledge/round-64-firmware-region-byte-evidence.md` would then print
   a `missing:` line (census must print nothing). Two conforming exits:
   - entry admitted and lands in the same commit → `mined`, used-by names the
     entry path (and optionally the round-64 lesson);
   - entry not admitted → `queued`, `used-by —`, **or** `mined` citing
     `corpus/lessons/round-64.md` only if that lesson actually contains the
     literal id (precedent verified: `corpus/lessons/round-62.md` contains
     S026/S028/S030/S031; `corpus/lessons/round-63.md` contains
     S031/S033/S035, matching those rows' `used-by` cells).
   The invariant to enforce at landing: every path named in a `mined` row's
   `used-by` exists **and** contains that row's id.
   **Draft state as received:** both rows are `queued` while `used-by` names
   `corpus/knowledge/round-64-firmware-region-byte-evidence.md` (both rows) and
   `corpus/lessons/round-64.md` (S037 only); both paths were absent at 04:23Z.
   The frozen census does not flag this (it checks only `mined` rows), so no
   census failure arises today, and the draft header explicitly commits L1 to
   setting `mined` at integration. Contract v1 defines `used-by` as paths "citing
   the row", so a row landed with `queued` **and** these paths would name
   citations that do not exist — the landing flip is mandatory, not cosmetic.

4. **No entropy claim may rest on S036.** `grep -c -i entropy` over the pinned
   snapshot = 0. The record's `normalized_result.coverage` token is
   `signature_scan`, which the guide does not define verbatim. S036 can support
   only: Evidence returns input path + SHA-256, raw producer reports, executable
   path/digest, version, limitations (Q4, lines 83–84); offsets are bytes in the
   original firmware (Q7, line 91); producer may infer lengths (Q8, lines 93–94);
   a signature/confidence byte proves no partition, encryption or runtime
   behavior (Q9, lines 94–95); inspection needs a separately configured Binwalk
   (Q10, lines 123–124). Any `teaches`/scope sentence about entropy scanning,
   extraction behavior, or provider accuracy is out of tier-A scope → FAIL.
   *Draft check:* both scope and `teaches` cells of S036 stay inside these
   sentences; no entropy token appears — compliant.

### MEDIUM

5. **Tier-A scope must be written into the `scope` cell, not implied.** Contract
   v1: tier is "scoped to `scope`, never global"; Q01 grades the row "tier A for
   that claim's scope". For S036 the scope cell must bound to route sentences at
   tag 6.5.0 and exclude (a) local execution on this host, (b) fixture bytes,
   (c) binwalk internals, (d) provider accuracy/completeness. For S037 the scope
   cell must bound to authored-bytes ↔ saved-record correspondence at base
   `666ea84b…` and exclude provider accuracy, completeness, real vendor images,
   extraction/execution and authenticity (same shape as S033's accepted scope).
   *Draft check:* both scope cells state their exclusions explicitly — compliant.

6. **Cell hygiene: no `|` inside any cell, 11 columns, enums enforced.** A pipe
   inside a cell makes NF≠13 and the census prints a malformed-row count >0;
   anchors that list several files/digests must separate them with commas or
   semicolons. Enums: kind ∈ {spec, docs, paper, code, tool, dataset, talk, book,
   community, own-work}; tier ∈ {A,B,C} and `community` is never A;
   status ∈ {queued, mined, rejected}; `opened` ISO date; `recheck` ISO date,
   `90d`/`180d` cadence, or `on-release`.
   *Draft check:* 2 rows, NF=13 on every table line (no in-cell pipe), enums
   clean, `opened` `2026-10-24`, `recheck` `on-release` — compliant.

### LOW

7. **The snapshot is still untracked.** `git ls-files --error-unmatch` fails and
   `git status --porcelain` shows `??` for `.ufo/waves/round-64/**`; the
   "committed snapshot" in the brief is at review time the working-tree file L1
   will integrate. Byte identity is proven against that file; commit-level
   immutability arrives only at L1's integration.
8. **`snapshot-manifest.json` correctly omits the source snapshot.** Its brief
   scopes it to the frozen inputs (claims/counter/red-before, `firmware-r63/*`,
   `round-63/{inspection,stdout,receipt,LEDGER,oracle_check}`, the two C4
   verifiers). Not a defect; a landing-time tamper check for the new snapshot
   would need a separate line and no brief asks for one (recorded, not routed).

### INFO

9. Quote spans were re-derived mechanically (`split`/`find` over the pinned
   snapshot with `**`/backticks stripped), not trusted from the opening report:
   Q1 3–4/13w · Q2 4–5/11w · Q3 26–27/12w · Q4 83–84/18w · Q5 84–86/18w ·
   Q6 86–87/16w · Q7 91/9w · Q8 93–94/13w · Q9 94–95/15w · Q10 123–124/18w ·
   Q11 149–151/21w. All found, all ≤25 words; partial-line end points match the
   hard-wrapped source.
10. Registry id space is clean for S036/S037: 35 rows, contiguous to S035, no
    duplicates, no enum violations, no missing `used-by` paths — so S036 is the
    next unused id by first actual use (round-63's "future zipfile-docs row takes
    S036" note is a lead note, and contract v1 gives leads no reservation).
11. **S036 anchor lists two headings the row's sentences do not use**
    ("Resource and lifecycle policy", "Verification"). Contract v1 asks for an
    exact, revisioned location, not a minimal one, and the load-bearing headings
    ("CLI and MCP" with "### Interpret the results", "Caller-supplied tools",
    lines 56–124) are all present, so this is breadth, not inaccuracy — INFO
    only, no action required.

## 1. Independent re-fetch receipts (S036)

Fetch at 2026-10-24T04:17:23Z from a lane-owned scratch dir
(`/tmp/revenger-r64-review-sources/`), `curl -sS -L`, cwd outside the lane:

| Observation | Value |
|---|---|
| URL | `https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/docs/firmware-analysis.md` |
| HTTP status | 200 (no redirect; `final_url` identical) |
| `content-length` / downloaded | 10695 / 10695 |
| sha256 | `e422b4816b1dbc912680afefb8e23acfd8ead4aea08c3d722d4ccb5207933609` |
| etag | `"323070c5e18148df7792662d81a23b57e47e668f1c1ecaa7f240d644797bab98"` |
| server `date` | `Sat, 24 Oct 2026 04:17:23 GMT` |
| git blob sha of fetched bytes | `152819177f8dce2124dea2a6a541e701cee227ed` |
| GitHub contents API `?ref=rea-agents-6.5.0` | size 10695, blob sha `152819177f8dce2124dea2a6a541e701cee227ed` |
| `git/ref/tags/rea-agents-6.5.0` | `refs/tags/rea-agents-6.5.0` → commit `3b79af28e80785afce9f5998d8f03289402a1847` |

Byte-identical comparison (required condition):

```
sha256sum  lane snapshot …/round-64/source-snapshots/rea-firmware-guide.md
           = e422b4816b1dbc912680afefb8e23acfd8ead4aea08c3d722d4ccb5207933609
cmp        lane snapshot  vs  my independent fetch  → CMP_TAG_BYTE_IDENTICAL
wc -l -c   lane snapshot  → 213 10695
```

Cache-independent identity: my fetched bytes hash to the same **git blob sha**
that the GitHub contents API returns for the path at ref `rea-agents-6.5.0`,
so the snapshot is the tag's blob, not a CDN artifact. My `main` fetch
reproduces the round-63 snapshot byte-for-byte (`CMP_MAIN_R63_BYTE_IDENTICAL`,
sha `d4a25c85…`), which independently confirms the opening seat's drift claim.

Tag choice is grounded in the record, not inferred: `corpus/live/runs/round-63/
receipt.json` `command` = `npx -y rea-agents@6.5.0 inspect-firmware-regions …`
and `LEDGER.md:22` states the CLI version comes from the command line, not the
record envelope (the envelope names the binwalk provider 3.1.0). So "the version
that produced the record" is `rea-agents@6.5.0` — the pinned tag is correct.

## 2. Provenance sidecar review (`rea-firmware-guide.provenance.json`)

Every field was reproduced independently and agrees: `url` (tag, not main),
`access_date` 2026-10-24, `http_status` 200, `content_length_bytes` 10695,
`sha256` `e422b481…93609`, `line_count` 213, `content_type`, `etag`, tag ref/
commit `3b79af28…`, blob `152819177…`/10695, `capture_command`, integrity check,
`pinned_vs_main` (main 15474 / `d4a25c85…` — matches my fetch),
`tier` note ("A for route-scope sentences only …") and `installs: none`.
The `access_time_utc_offset_note` (host 01:17 −03:00) is consistent with the
server `date` returned to me (04:17Z). No unsupported claim found; **PASS**.

## 3. Row review — S036/S037 draft as received (PASS, one landing condition)

Artifact: `.ufo/waves/round-64/sources-rows-draft.md`, sha256
`6e66fd3e078088fedcc0816fbf2e52262e0a644036014eaef3b7092387ba3d20`, 3873 bytes,
written 2026-10-24T04:22Z. Two data rows; all four table lines NF=13; no `|`
inside any cell.

### 3.1 S036 — PASS

| Contract v1 cell | Draft | Verdict |
|---|---|---|
| id | `S036` (next unused: 35 rows, max S035, no dupes) | PASS |
| source | "Firmware analysis — REA documentation at tag rea-agents-6.5.0 — <tag URL>" (title + canonical URL) | PASS |
| kind | `docs` (enum member) | PASS |
| tier + scope | `A`, scope cell bounds to "route-scope sentences only … not provider execution on this host, not the authored fixture bytes, not extraction or completeness" | PASS — Q01 scope respected |
| anchor | tag `rea-agents-6.5.0`, `refs/tags/… → commit 3b79af28…1847`, `blob 152819177…227ed`, named headings, "route text lines 56-124", "snapshot 213 lines, 10695 bytes, sha256 e422b481…93609" | PASS — exact location **plus revision**; pins the tag snapshot, not `main` |
| teaches | one sentence: Evidence with original path + SHA-256, raw producer reports, executable path/digest, version, limitations; offsets are bytes in the original firmware; sizes stay provider-reported; "so a saved region list can be read without claiming partition validity" | PASS — each clause maps to Q4/Q7/Q8/Q9 (INFO 9); no entropy, execution, extraction or validity claim |
| status / opened / recheck / used-by | `queued` / `2026-10-24` / `on-release` / entry path | PASS for the draft; landing flip required (landing condition, §3.3) |

No sentence in the row cites `main`, no entropy statement, and nothing from the
row's text exceeds the pinned tag's words.

### 3.2 S037 — PASS

| Contract v1 cell | Draft | Verdict |
|---|---|---|
| id | `S037` | PASS |
| source | own-work title + the six repo-relative paths (command/repo-path form allowed for `own-work`) | PASS |
| kind | `own-work` | PASS |
| tier + scope | `A`, "byte/record correspondence only, not provider accuracy, extraction, authenticity or completeness", pinned at base `666ea84b…` | PASS — matches the claims' own-work scope shape (S033 precedent) |
| anchor | base `666ea84b…` + all six sha256s with sizes | PASS — every digest recomputed here and confirmed identical at base and in the working tree (§4 table) |
| teaches | "the image is 2048 bytes and its sha256 appears in receipt.fixture_sha256, truth.json image and inspection subject digest, while receipt.stdout_sha256 equals the saved inspection.json sha256…" | PASS — all four bindings re-verified: `truth.json.image.sha256` = `bdfe9f46…`, `receipt.fixture_sha256` = `bdfe9f46…`, `inspection.subject.digest.sha256` = `bdfe9f46…`, `receipt.stdout_sha256` = `f6997835…` = sha256(`inspection.json`) |
| status / opened / recheck / used-by | `queued` / `2026-10-24` / `on-release` / entry path + lesson path | PASS for the draft; landing flip required (§3.3) |

### 3.3 The single landing condition (not a draft defect)

Both rows are `queued` while `used-by` names
`corpus/knowledge/round-64-firmware-region-byte-evidence.md` (both) and
`corpus/lessons/round-64.md` (S037). Neither path existed at 04:23Z. The draft
header states L1 will set `mined` at integration. Therefore L1 **must**, in the
same commit that appends the rows:

1. set both rows to `mined`;
2. have both named paths present, with the entry actually citing S036 and S037
   and the lesson containing the literal `S036`/`S037` mentions;
3. re-run the contract census from §4 — otherwise the frozen census prints
   `missing: <path>` and the append is non-conformant.

If C1 falsifies and the entry never lands, the alternative exit of HIGH finding 3
applies instead (`queued` + `used-by —`, or lesson-only citation). The draft's
choice is a forward reference that the census does not currently flag; it must
not be landed verbatim as `queued` with these paths.

## 4. Row-review gate for landing (contract v1, self-tested)

Contract v1 cells: id · source · kind · tier · scope · anchor · teaches · status ·
opened · recheck · used-by. Mechanical checks and their expected results on the
landed `corpus/SOURCES.md` (run from the lane root):

```sh
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md        # 37 (was 35)
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md   # 0
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {i=$2;gsub(/[[:space:]]/,"",i);print i}' corpus/SOURCES.md | sort | uniq -d   # nothing
# enum + tier-inflation: contract snippet must print nothing
# mined used-by path existence: contract snippet must print nothing (the HIGH-finding-3 trap)
```

A checker implementing the same rules was self-tested: **0 problems across the
35 live rows**, and an injected-defect fixture was flagged on exactly the three
injected faults (tier `D`, recheck `soon`, nonexistent `used-by` path). Run on
the received draft it reports only the two documented forward references
(`used-by` named on `queued` rows) — the §3.3 landing condition and nothing
else. The script lives at `/tmp/revenger-r64-review-sources/rowcheck.py`
(scratch, removed on landing) — the census commands above are the portable
equivalent.

Canonical values for the landed rows (all independently computed here; the
received draft matches every one):

| Field | S036 | S037 |
|---|---|---|
| id | S036 (next unused, verified) | S037 |
| kind | `docs` | `own-work` |
| tier | A, route-scope sentences only | A, byte/record correspondence scope only |
| anchor revision | tag `rea-agents-6.5.0`, commit `3b79af28e80785afce9f5998d8f03289402a1847`, snapshot sha256 `e422b4816b1dbc912680afefb8e23acfd8ead4aea08c3d722d4ccb5207933609`, sections "CLI and MCP" (:53) and "Interpret the results" (:89) | base `666ea84b6be2eec2b0359f556ba2429fc9044c36` + the six file sha256s below |
| opened | 2026-10-24 | 2026-10-24 |
| recheck | `on-release` (S002/S016/S018 precedent) or `180d` | `on-release` (S026/S030/S031/S033/S035 precedent) |
| status | `mined` only if its `used-by` path exists in the same commit, else `queued` | same rule |

S037 anchor digests, verified to exist **at base `666ea84b`** via
`git ls-tree` and to equal the working-tree blobs (no drift):

| File | Bytes | sha256 |
|---|---|---|
| `corpus/fixtures/firmware-r63/firmware-r63.bin` | 2048 | `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be` |
| `corpus/fixtures/firmware-r63/truth.json` | 1933 | `9663f90b2b9f29c5beb621e554ed7584eedf5e77d4785f26a453e70dbd5a65e6` |
| `corpus/fixtures/firmware-r63/generator.py` | 5532 | `4e5d5975e3cf6362f6fd430f2147d42f75d011978f7d6b5ec86d224c77793db4` |
| `corpus/live/runs/round-63/inspection.json` | 3904 | `f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9` |
| `corpus/live/runs/round-63/receipt.json` | 492 | `e930a549db16a180d4ab05307e073cd71599a3317b9f3d15a0d97843d5c6b94d` |
| `corpus/live/runs/round-63/LEDGER.md` | 22671 | `25a4a18b76a2a55f3b7ea397ee23bba948be3f1c1a3e13a3194c0f057bb1e1a6` |

Cross-check: the independent `R64LessonDraft` seat published the same six
digests, so two seats agree. `inspection.json` and `stdout.raw` are the same
bytes (`f69978…` both), and `receipt.json` binds
`evidence_id ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259`
and `fixture_sha256 = bdfe9f46…` — so a row that quotes either identity cannot
silently mix layers.

## 5. Residual risk

- **Tag re-pointing.** `raw.githubusercontent.com/<tag>/…` resolves to
  `3b79af28…` today; if upstream force-moves the tag, the blob sha check (not
  the URL) is what detects it. Rows pin the sha256, so the citation survives.
- **Shared CDN.** My fetch and the lane fetch share Fastly. The GitHub contents
  API blob identity is the independent server-side object check; a poisoned
  edge cache would have to spoof both the served bytes and the blob sha.
- **Time skew.** My fetch and the seat's fetch were ~1h apart on the same tag;
  identical sha across both, so content drift in that window is excluded.
- **Landing transform risk.** The draft passed as drafted; the remaining risk is
  the integration step itself — a `queued` append with two named-but-absent
  `used-by` paths, or a flip to `mined` without the entry/lesson containing the
  ids. §3.3 and the §4 census are the check to run on the landed tree.
- **Late-arriving draft order.** The draft was graded at sha256 `6e66fd3e…`; if
  the file is edited before landing, this verdict does not carry over — re-run
  §4 against the new sha.
- **Snapshot not yet committed.** Integration can still drop, rename or re-fetch
  it; the sha256 in the sidecar is the invariant to preserve.

## 6. Verification gaps

- **No language-server surface.** The review targets Markdown rows and JSON
  provenance; no LSP server answers `.md`/`.json` in this lane, so
  `references`/`definition`/`diagnostics` are inapplicable. Byte identity, git
  blob identity, and census/awk checks are the literal checks used, and they are
  sufficient for these artifact types — recorded explicitly rather than
  presented as semantic proof.
- **Draft arrived only at 04:22Z.** The three earlier absence polls are
  recorded; the review then proceeded on the received file and its sha256. No
  part of the verdict relies on the author's self-report.
- **No producer re-run.** The record is observation-layer evidence only; this
  seat neither re-executed `rea inspect-firmware-regions` nor validated fixture
  bytes against truth (other seats own that).
- **S037 bundled `oracle_check.py` was not given a digest row here.** It is in
  the run directory (`d0dfd7a1cd105485e47bf52446056a2636fb803c05a404ce56da597f36ce0512`,
  11034 B) but is outside the claims' named bundle; include it only if the draft
  broadens the anchor to "the round-63 run directory".

## 7. Tooling and touched surfaces

- Installs/upgrades: **none**. No pacman transaction (host-wide pause honored),
  no `uv tool`, no npm, no binary download.
- Read: frozen contract, counter, red-before receipt, briefs, `corpus/SOURCES.md`
  and fleet contract v1, the round-64 snapshot + provenance sidecar, the
  round-63 record/receipt/LEDGER/fixtures, `R64SourceReaGuide.md`,
  `R64LessonDraft.md`, `scout-sources.md`, `snapshot-manifest.json`, and the
  draft `sources-rows-draft.md` (sha256 `6e66fd3e…`).
- Written: this report only. Scratch: `/tmp/revenger-r64-review-sources/`
  (curl bodies/headers, `rowcheck.py`, `selftest.md`) — removable on landing.
- Read-only git used: `ls-tree`, `hash-object`, `ls-files`, `status`,
  `check-ignore`; no mutation, no index write, no commit.
- No `corpus/**`, `.ufo/waves` spec/registry, `MANIFEST.json`, fleet or sibling
  lane, jj state or Git index touched.

Report: .ufo/waves/round-64/R64ReviewSources.md
