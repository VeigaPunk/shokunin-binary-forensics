# round-89 verifier spot-check — revenger (non-author closure)

author: hyaku closure (non-author integrator, @m_zfl)

Closed 2026-11-04 against lane head `c8cc585c3d25c8aa30ca7fde8b7b95c6d40c3893`
(= `git ls-remote origin refs/heads/main`; base `2b017fa3c616a84b7b491e3312029fa8a8c076e6`).
I did not author this round and did not improve it: everything below is a
re-derivation over committed bytes or a plain live probe I ran myself. Lane
repo `/home/vgpnk/Projects/shokunin/revenger-shokunin`; fleet root
`/home/vgpnk/Projects/shokunin`. No `jj` command was run in the lane except
through `scripts/hyaku/jj-lane.sh state` (read-only).

## Step-1 conformance — PASS (three status-neutral defects, below)

- **Report landed by the lane identity, last.** `git -C <fleet> log
  --format='%an %H' -- .ufo/reports/round-89/revenger.md` →
  `revenger-shokunin b95bafb51de5c3af50eb6fd5ecbd92ef6d572e3a` (note 4), and
  before it `90cc93c` (note 3), `81ed486` (erratum 2), `7ccdbe6` (erratum),
  `c96aedc` (report). Every commit that touches the report carries the lane
  identity; the report is a record plus append-only errata, never a rewrite.
- **Substantive report, not a marker.** 18,566 bytes; sections present in
  order: work performed, landed changes (each row tied to a `LOG.md` entry and
  a commit), before → after measurements, sources & frontier, trend verdicts,
  `## SHONEN`, round notes, three errata/notes.
- **`SHONEN` heading.** `grep -c '^## SHONEN'` = 1; four box lines, all `[~]`
  with pointers (`grep -cE '^- \[[ x~]\]'` = 4); the two `[x]` substrings in
  the file are prose stating that none was written (`:162`, `:267`), not marks.
  `SHONEN.md` itself is byte-unchanged base→tip.
- **Cited lane commits exist and are ancestors of the branch ref** (never
  `@{u}`; the repo is jj-colocated and HEAD is detached):
  `git merge-base --is-ancestor <hash> main` → `yes` for all ten cited hashes
  `2b017fa3`, `c84339c0`, `6ce41aab`, `bd575ca1`, `5f7ecce6`, `b90bf377`,
  `7f840eb6`, `e0fbf2ea`, `46c170d1`, `c8cc585c`.
- **Lane pushed, no uncommitted round work.**
  `jj-lane.sh state` → `branch=main local=c8cc585c… remote=c8cc585c… ahead=0
  behind=0 head=detached tracked=0 untracked=0`; `git status --porcelain`
  prints nothing.
- **Round range.** `git log 46c170d..c8cc585` = exactly one commit
  (`round-89 attempt 3: independent re-derivation …`), authored
  `revenger-shokunin <revenger@shokunin.local>`.
- **Prompt fidelity.** `.ufo/prompts/revenger-round-89.md` (84,496 B) is
  committed by the lane identity (`662f49a`, attempt 3) and carries the
  template contract: the report path and filename (`:101`, `:448-449`), the
  `SHONEN` heading requirement (`:118`, `:521-522`), the commit-hash citation
  rule (`:472`, `:493`), the write scope (`:448`), the L0 side channel
  (`:138`), commit-then-push (`:133`), push scope (`:135`), the L2 floor
  "at least 8 L2 subagents in ONE batched AgentSwarm call" (`:82`), the 8–16
  wave band (`:145`) and the 1–3-claims / lowest-axis binding (`:14-16`).
- **Dispatch/complete digest** (`.ufo/watchdog.log`, mutable; copied):
  `17:51:01-03 launch revenger round=89 pgid=3640955 attempt=1` ·
  `18:02:55 lane-dead-no-report` · `18:02:57 launch … attempt=2` ·
  `18:03:36 lane-dead-no-report` · `18:03:37 launch … attempt=3` ·
  `18:04:12 lane-dead-no-report` · `18:25:39 launch … attempt=1` ·
  `18:26:21 lane-dead-no-report` · `18:26:23 launch … attempt=2` ·
  `18:31:14 lane-dead-no-report` · `18:31:16 launch … attempt=3` ·
  `18:39:06 complete revenger round=89; hyaku-inline attempt=3`. All twelve
  lines match the closure contract verbatim.
- **Wave.** `.ufo/waves/round-89/w1-results.json` records `seats: 12`; twelve
  seat dirs exist under `w1/` (`ConnectorR89`, `CriticR89Claims`,
  `ExecR89Record`, `MutR89Census`, `MutR89Oracle`, `ReviewerR89C1`,
  `ReviewerR89C2`, `ScoutR89Host`, `ScribeR89Registry`, `ScribeR89Rows`,
  `ScribeR89Sources`, `SentinelR89`). 5 attack seats = 42 %, inside the
  8–16 band with one v1 wave; round total 12, no residual call.

Defects (status-neutral, routed below): D1 dead `source` path in S481 and in
`corpus/knowledge/2026-10-12-rea-readiness-checklist.md:67`; D2 the lesson's
`## Gate` asserts a source-opening table it does not carry; D3 the SM2 1 → 0
count has no committed receipt.

## C1 — freshness, host-readiness census re-probe — **MISS, verified**

Claim (frozen at `c84339c`, `reports/round-89/claims.md`): the 18-row census
is re-derived against the live host, target `CENSUS_STALE_UNFLAGGED=0`.
**Evidence-verified, not executed**: `census_reprobe.py` is the lane's own
gate and PROTOCOL §Gate standard (Closure consequence) forbids me running it.
What I verified instead:

1. **Instrument identity from committed bytes.**
   `git show c8cc585c:corpus/census_reprobe.py | sha256sum` →
   `c3127ffc18a54f85f01e2fb88f50b5db694484588e5b7467ae5567ffdd3b648a`
   = line 1 of `reports/round-89/instrument-pins.log` = the pin quoted in the
   claims file and the lesson.
2. **Self-test tally (committed evidence).** `reports/round-89/census-selftest.log`
   carries nine `CENSUS_SELFTEST_<leg>=ok` lines and `CENSUS_SELFTEST=pass`.
3. **Red / after receipts at named revisions.** `reports/round-89/census-red.log`
   = `CENSUS_ROWS=18`, ten `CENSUS_MISMATCH` lines (F01, F03, F04, F07, F08,
   F12, K01, K03, K04, K05), `CENSUS_STALE_UNFLAGGED=10`, exit 1.
   `reports/round-89/c1-after.log` = two findings, both `K04`,
   `CENSUS_STALE_UNFLAGGED=2`, `EXIT=1`. `reports/round-89/attempt3-verify.log`
   re-derives the same 2 at `46c170d`. The base value cannot have drifted:
   `git diff --numstat 2b017fa3 c8cc585c -- corpus/knowledge/seed.md
   corpus/knowledge/2026-10-12-rea-readiness-checklist.md` = `28 0` and `21 0`
   — append-only, zero deletions.
4. **The corrected values are true (my own plain probes, 2026-11-04).**
   `command -v rea; rea --version` → `/run/user/1000/fnm_multishells/…/bin/rea
   6.7.0`; `node --version; npm --version` → `v24.21.0`, `11.19.0`;
   `command -v ghidra` → `/usr/bin/ghidra`; `command -v ida` → rc=1 (absent);
   `jadx --version` → `1.5.6`; `binwalk --version` → `binwalk 3.1.0`;
   `unblob --version` → `26.6.4`; `python3 -c 'import pwn'` → imports;
   `ls ~/.agents/skills/reverse-engineer-anything/*.md` → 2 (`HOST-CONTRACT.md`,
   `SKILL.md`); `ls …/references/*.md` → 7; `sed -n 1,8p …/SKILL.md` →
   `version: "42"`, `tool_count: 207`; the `rea` entry in `~/.omp/agent/mcp.json`
   → args `["-y","rea-agents@6.7.0","mcp"]`; `npm view rea-agents version` →
   `6.8.0` (registry latest) against the skill's own pin `rea-agents@6.7.0`
   (three occurrences in `SKILL.md`), which is the fact the census row probes.
   Every corrected cell in the two `## Re-verification 2026-11-04` tables
   matches the live host.
5. **The target really is unreachable truthfully.** `corpus/census_reprobe.py`
   `check_rows` (`:179-220`) scores one text per row (the last row carrying an
   id wins) and, per presence probe, requires its own literal and forbids the
   other's. `K04` carries two probes of opposite live state (ghidra present,
   ida absent), so a truthful single string yields two findings and a
   one-word string yields one — zero needs a faked `PATH` or edited bytes.
   Measured floor 1, truthful 2, reported 2.

**Verdict: MISS (10 → 2 against a frozen target of 0), and the residual is
honest, not a stale statement.** I agree with the lane's own ruling.

## C2 — coverage, F4 10/11 → 11/11 with the APK oracle — **KILLED, re-measured**

Claim (frozen): `reports/round-81/f_probe4.py` reads `F4_COVERAGE=11/11`
**and** `oracle_check.py` reads `ORACLE OK (19/19)` over the committed record.

1. **Counter re-measured by me over committed bytes, my own implementation of
   the frozen predicate** (records = `corpus/live/runs/**/*.json` with
   `evidence_id` and non-null `normalized_result`, family map copied from the
   frozen instrument): base `2b017fa3` → 134 JSON files, 21 record-shaped
   operations, `F4=10/11`; tip `c8cc585c` → identical 134 / 21 / `10/11`;
   `inspect_android_package` absent from the record-shaped set at both ends.
   This matches `f4-red.log`, `c2-after.log` (b) and `holds.log` exactly.
2. **The mapping did not move.** `git show <rev>:reports/round-81/f_probe4.py |
   sha256sum` → `4d871971fa49131f65e951bba1061a00b16c9eee8c3dc7df007fff434566a3c7`
   at base and at tip (byte-unchanged).
3. **The record is real, and it is outside the counted surface.** The landing
   `6ce41aa` did carry `corpus/live/runs/round-89/{inspection.json,receipt.json,LEDGER.md}`;
   the adjudication `bd575ca` relocated them; `git diff --name-only 2b017fa3
   c8cc585c -- corpus/live` = 0 lines, so the surface is net-unchanged.
   `git show c8cc585c:reports/round-89/rejected-android-record/inspection.json |
   sha256sum` → `01af3141d79027a3bae53b6482779d3e9c89446ab6ca09b408a6cb266f321c76`
   = run1 `stdout_sha256` in `reports/round-89/c2-after.log` (d) and in the
   producer receipt. The record does carry `operation:
   inspect_android_package`, an `evidence_id` and a non-null
   `normalized_result` (`package_name: com.example.r65`), so counting it would
   indeed print 11/11 — the report's "nominal" reading is accurate.
4. **Kill (a) and kill (c) hold.** Oracle green over the preserved record
   (`reports/round-89/oracle-design.log:20` → `ORACLE OK (19/19 checks)`) with
   the tamper control red (`oracle-tamper-control.log` → `ORACLE FAIL (18/19
   checks)`); and the two producer runs are not byte-identical: run1
   `01af3141…1c76` vs run2 `5bbdd189…ce00`, `cmp_verdict` "DIFFER … at char
   20, line 1 (per-run evidence_id)".

**Verdict: KILLED, no coverage move (10/11 → 10/11).** The round's own kill
rules fire; I re-measured the counters myself and agree.

## Discernment spot-check (non-author)

Census run by me: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh
validate --root /home/vgpnk/Projects/shokunin revenger` → exit 0, 21 `W01` +
10 `W04`, zero `E` (same lineage as round 88; the three new rows added no
warning). Row counts: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md` = **482** at the tip vs **479** at base (the report's
479 → 482), malformed rows 0, duplicate ids 0, mined `used-by` paths missing 0.

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S480 admit (C1 red receipt) | admit, own-work, tier A | `reports/round-89/census-red.log:12` re-read | agree | `CENSUS_STALE_UNFLAGGED=10` is byte-verbatim at the cited line; the ten mismatch ids at `:2-11` are exactly the ten named; a tier-A own-work receipt is the right class for the lane's own re-runnable output; `used-by` resolves |
| S482 admit (oracle green receipt) | admit, own-work, tier A | `reports/round-89/oracle-design.log:20` re-read | agree | `ORACLE OK (19/19 checks)` verbatim; nineteen `check ok:` lines at `:1-19`; `teaches` states the fixture-vs-record boundary, which is what the receipt actually shows |
| S481 admit (producer receipt) | admit, own-work, tier A | cited path `corpus/live/runs/round-89/receipt.json` | **disagree** (row as written) / agree on the source | the cited path does not exist at the tip — the adjudication relocated the record to `reports/round-89/rejected-android-record/receipt.json`, where the quoted `stdout_sha256` at `:20`, `rea_version` at `:6`, provider at `:8-10` and `cmp_verdict` at `:31` are byte-verbatim. The source and the judgment are right; the row's citation fails CORPUS rule 1 ("a row is a claim … canonical path") and PROTOCOL §Evidence standard ("a pointer must resolve at closure time") |
| C2 android record — reject (preserved, not counted) | reject | my own F4 re-derivation at base and tip, plus the record's shape and digests | agree | rejecting an authentic-but-forgeable record is the right call: the counters would move on a fabricated record, so counting it would credit a criterion the round cannot defend; preserving the bytes outside the counted surface keeps the evidence and the honesty |
| C1 claim — self-ruled MISS at 2 findings | claim not admitted | live host probes of all twelve corrected facts + the frozen predicate's `check_rows` | agree | target 0 is unreachable without faking `PATH`; 2 findings is the truthful floor for the mixed-state `K04` row; no re-scoping was attempted |
| the eight corrected census rows | re-verify (stale → live) | the twelve live probes listed under C1 | agree | every corrected cell states the value I measured; the earlier tables are byte-identical (append-only, 0 deletions) |
| two false `holds` (F02, F05) corrected at `5f7ecce` | correction landed | `git show 5f7ecce -- corpus/knowledge/seed.md` | agree | exactly the two verdict cells change (`holds` → `STALE -> 42 / 207`, `STALE -> 6.7.0`); the live values are the ones I measured; the detector's own K06 prose-cell false positives are disclosed, not applied |

## Per-axis verdicts (closure)

| axis | verdict | evidence |
|---|---|---|
| freshness | **improved** | the census surface moved 10 findings / 10 rows → 2 findings / 1 row (`census-red.log` vs `c1-after.log`, both evidence-verified at their named revisions); eight stale rows now state values I re-measured on the live host; append-only (0 deletions). The claim's frozen target 0 was not met — the axis moved, the claim did not verify |
| coverage | unchanged | C2 killed; F4 10/11 → 10/11 re-measured by me at both ends; `corpus/live` net-unchanged; K untouched (r74 L0 still unanswered) |
| calibration | improved | base SCORECARD asserted `freshness — stored-assertion proxy 18/18 → 18/18` in every historical section; the appended r89 section corrects that proxy in committed bytes, the two false `holds` in the round's own new table were caught and corrected (`5f7ecce`), both claims are recorded as MISS/KILLED instead of re-scoped, and the gate's five blind spots are registered as limits rather than claimed as capability |
| depth | unchanged | no knowledge entry admitted and no new decision threshold; `SKILL.md` gains M43 plus two registry rows that record *limits* (`census_reprobe` "experimental and NOT admitted", `apk_identity_oracle` "probe, no self-test") |
| operability | unchanged | no admitted runnable checklist or gate; the census is registered probe-as-gate and the oracle a probe, both with named blind spots |
| adjacency | unchanged | `PROVINCE.md` and `corpus/QUALITY.md` byte-unchanged base→tip (`git diff --stat` empty); the `rea` 6.7.0-vs-6.8.0 and Windows-ghidra-path drift inside `PROVINCE.md` is reported, not absorbed |

No axis is harmed.

## Trend verdicts (closure)

- **expansion: unchanged** — no `knowledge/` entry was admitted and no
  coverage-map row changed (`git diff --numstat 2b017fa3 c8cc585c --
  corpus/knowledge` = the two census files, append-only; `grep -cE
  '^\| C[0-9]+ .*\| held \|$' corpus/README.md` = 8, unchanged). The three new
  `SOURCES.md` rows are own-work evidence for this round's receipts, not new
  ground, and the report says so.
- **quality: improved** — eight stale entries re-verified with dated live
  values I re-measured; two false `holds` in the round's own table corrected by
  a new commit rather than an amend; the rejected record preserved
  byte-identically (`cmp`-equivalent digests above) instead of deleted; no
  admitted entry found false and left unmarked.
- **discernment: unchanged** — of five sampled gate decisions, four agree with
  my re-open and one does not: S481 was admitted with a `source` path that no
  longer resolves. The substance of that row is sound, so this is a citation
  defect, not a taste failure — but LEARNING.md's `improved` test is agreement
  on admits *and* rejects, or a disagreement that becomes a lesson adding a
  grounded `QUALITY.md` criterion, and neither holds at this closure (the
  round pre-declared `QUALITY.md` unchanged). Routed as D1 with the exact fix;
  had the row pointed at the relocated receipt I would have graded `improved`.

## Routed defects (status-neutral; lane to fix in r90)

1. **D1 — the record relocation was not swept across every mention.** S481's
   `source` cell names `corpus/live/runs/round-89/receipt.json`, which the
   adjudication moved; `corpus/knowledge/2026-10-12-rea-readiness-checklist.md:67`
   still points at `corpus/live/runs/round-89/` too. `source` is not in
   `SOURCES.md`'s mutable set (only `status`, `recheck`, `used-by`), so the fix
   is a new row whose `teaches` opens `supersedes S481 —` pointing at
   `reports/round-89/rejected-android-record/receipt.json`, plus an appended
   correction line in the checklist (never a rewrite of the filed bytes).
2. **D2 — the lesson's `## Gate` lacks the required source-opening table.**
   CORPUS rule 1 requires the round lesson's `## Gate` to record, for every new
   row, the URL/path, the access date and a ≤25-word quote with its location.
   The section asserts "The final source-opening table records …" but the table
   lives only in `.ufo/waves/round-89/w1/ScribeR89Sources.md`. Next round: carry
   it in the lesson.
3. **D3 — an un-receipted count.** The report's "`self_assessment_check.py` SM2
   drops 1 → 0 (SM6 still hardcodes a `/14` denominator against the 15-row
   map)" carries no counting command or receipt file. I re-derived the SM6
   half from committed bytes (`corpus/self_assessment_check.py:183`:
   `K_HELD_BACKED[^0-9]*(\d+)/14…`), so the fact holds; the SM2 delta needs a
   committed receipt like every other number this lane quotes.
4. **D4 — the census gate's frozen-run baseline pins inputs, not host state.**
   `census-red.log` is a run over the committed `2b017fa3` census archive, but
   the verdict also depends on the live host (`PATH`, four version commands,
   `import pwn`, `~/.omp/agent/mcp.json`). A later host change silently
   invalidates the expected verdict. The lane discloses this (registry row
   limit 4, `environment.log`); r90 should pin the environment (`which` paths,
   versions) inside the baseline, as the lane's own routed item (1) already
   says.
5. **Residual, not routed as a defect** — the superseded
   `freshness — stored-assertion proxy 18/18` rows still stand in eight
   historical SCORECARD sections without an in-row forward pointer; the r89
   section supersedes the proxy class explicitly and the rows are per-round
   records, so this is noted, not charged.

## Admission

Neither declared claim verifies: C1 missed its frozen target (2 findings vs 0,
the residual truthful and the target unreachable under the frozen predicate),
C2 was killed by its own kill rules and moved no coverage counter. No axis is
harmed. **Round not admitted — honest stop, lane status `ok`.** The `SHONEN`
boxes stay `[~]`: boxes 1–4 are checkable in principle by a non-author, but the
promotion decision (and the standing re-confirmation of the current `SKILL.md`
bytes) is operator-owned and nothing here writes `[x]`.
