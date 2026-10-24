# R64SkillChecklists — operability half of the SKILL candidate

Seat: scribe. Assignment: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/briefs/R64SkillChecklists.md`.
Round contract read first: `reports/round-64/claims.md`; frozen counter `reports/round-64/measure.py`; red-before `reports/round-64/measure-before.log`.

## Deliverable

`/tmp/revenger-r64-skill/checklists.md` — 227 lines, 13,506 bytes,
sha256 `07cdfdafd2ed557ed8f21b19c531e1f900284708e3302de10a6a443600f7b8db`.
Six sections, merge-ready for L1:

1. **Verifier census** — `SCORECARD.md:35-42` command C copied byte-identically; promise = one `<name> exit=<code> <last line>` per script, then `CALIBRATION <ok> / 4 score= <value>` and `REPLAY <ok> / <n>`; wrapper exit 0 is not the result (`SCORECARD.md:29-30`); recorded base `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10` (read from `measure-before.log`, not re-run).
2. **Firmware oracle** — `corpus/live/runs/round-63/LEDGER.md:110` copied byte-identically; promise = five `REGION` lines with per-region markers, final `ORACLE OK`, exit 0 (`LEDGER.md` O6, O10; spotcheck `corpus/lessons/round-63-verifier-spotcheck.md:31`); mismatch path `MISMATCH …` + `ORACLE MISMATCH` + exit 1.
3. **Frozen counter** — usage string from `claims.md:84` (`python3 -B reports/round-64/measure.py TREE`) with the archive/cwd=/TMPDIR contract, a byte-identical committed invocation shape (`W2FinalIndependent.md:148-149`), and a label→base-value table for every printed label plus the exit semantics (`measure.py:9-11`, `:273`) and the explicit rule that exit 0 ≠ claims met.
4. **SOURCES census** — 4a fleet `scripts/sources-census.sh validate`/`census` pair copied byte-identically from `W2FinalIndependent.md:151-152` with exit codes, W04 disclosure rule and recorded row counts; 4b the seven-command contract census copied byte-identically from `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:67-80` with each command's pass/fail promise.
5. **Evidence-ledger discipline** — observation/inference/unknown separation and Evidence-ID citation per `PROVINCE.md:6-7`, binding per `QUALITY.md:32-33`, shaped on the round-63 LEDGER exemplar, plus the five "never promote" rules (digest→origin Q09, recorded→re-derived Q11/Q03, tool presence→result Q04, counts→coverage README status legend, observation→universal Q10).
6. **Non-establishment boundary** — what a green run does not prove.

Provenance: every command in every fenced block was programmatically checked to
occur verbatim in the named source file (6 blocks, 0 mismatches). No command was
transcribed from memory; none was invented.

## Behavior and gates

- Executed **no** product command: the verifier census, oracle, counter and SOURCES
  census were not run by this seat. `R64ExecSkillRun` owns execution evidence; its
  transcript (`.ufo/waves/round-64/exec-skill-run.md`) records the SKILL.md-absent
  dependency at its deadline.
- All base values in the draft are **recorded** values quoted from
  `reports/round-64/measure-before.log` and committed artifacts, not observations
  of this seat.
- No tool installs (tooling directive not triggered). No git/jj command run. No
  file inside the repo created or modified except this report.
- No measurement, no claim, no README flip, no gate touched. Nothing here is
  evidence for C1 or C2.

## Touched surfaces

| path | action |
|---|---|
| `/tmp/revenger-r64-skill/checklists.md` | created (deliverable, outside the repo, lane-owned scratch) |
| `.ufo/waves/round-64/R64SkillChecklists.md` | created (this report) |

Read-only reads: `reports/round-64/{claims.md,measure.py,measure-before.log}`,
`SCORECARD.md`, `PROVINCE.md`, `corpus/{README.md,QUALITY.md,SOURCES.md}`,
`corpus/live/runs/round-63/{LEDGER.md,oracle_check.py}`,
`corpus/lessons/{round-63.md,round-63-verifier-spotcheck.md}`,
`.ufo/waves/round-63/falsify/{W2FinalIndependent.md,W2VerifySourcesTable.md}`,
`.ufo/waves/round-64/briefs/{R64SkillDraft.md,R64CriticSkill.md,R64ExecSkillRun.md}`,
`.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`,
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh` (header only), and the
sibling draft `/tmp/revenger-r64-skill/SKILL.md` (read-only).

## Findings — for L1 merge and the canonical judge

1. **Merge: duplicate block, identical bytes.** Sibling `SKILL.md` (23,390 B, present
   at end of run) §6.2 already carries the seven-command contract census. Programmatic
   comparison: `SKILL.md:168-183` block == `checklists.md` §4b block ==
   `SOURCES-CONTRACT-v1.md:67-80` (all three equal). Dedupe on merge; no textual conflict.
2. **Merge: cwd wording differs from the contract.** `SKILL.md` §6.1 says
   "Invoke from the lane root exactly as frozen: `python3 -B reports/round-64/measure.py TREE`";
   `claims.md:84-85` says "on a committed `git archive <commit> corpus` tree, **cwd=/**,
   TMPDIR under lane-owned scratch". `measure.py` resolves TREE absolutely (`:21`) and
   runs each verifier with `cwd=TREE` (`:253`), so both orders execute; the frozen
   condition is cwd=/. My §3 states cwd=/ and keeps the lane-root requirement where it
   actually binds (the census-C glob, §1). Reported, not resolved — I did not edit the
   sibling or the SKILL candidate.
3. **Merge: SKILL.md lacks four items this half supplies.** No census-C block, no
   firmware-oracle command, no fleet `sources-census.sh` pair, no O/I/U ledger section
   (grep-verified absent). Nothing in SKILL.md contradicts them.
4. **Operability trap (new).** Command C globs `pathlib.Path("corpus")` relative:
   from any cwd other than the lane root it censuses zero scripts, prints a
   silently green `REPLAY 0 / 0` and exits 0. `SKILL.md` §6.4 points at "Census C"
   without the block; §1 of the draft supplies the block and the cwd requirement.
5. **Staleness parameter.** The committed fleet-census line carries `--today 2026-10-24`.
   `--today` is optional; `sources-census.sh` defaults to UTC today
   (`TODAY=${TODAY:-$(date -u +%F)}`). The draft says so instead of freezing the date.
6. **Provenance outside the lane.** The seven-command census exists verbatim only in
   the fleet contract `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`, which the lane's own
   `corpus/SOURCES.md:3` names as governing; the lane holds an in-lane exercise record
   at `.ufo/waves/round-63/falsify/W2VerifySourcesTable.md:52`. If the merged SKILL must
   be self-contained in-repo, L1 needs a lane-owned copy; creating one is outside this
   seat's write scope.
7. **No round-64 committed counter invocation exists.** The only committed invocation
   shape is round-63's (`W2FinalIndependent.md:148-149`, which names
   `reports/round-63/measure.py` and commit `db55bd6`). The draft quotes it byte-identical
   and warns to change commit and path; it must not be quoted as a round-64 run.
8. **Census counts at different tree states — both recorded.** Round-64 base: exit 0,
   35 rows, four W04s S024/S028/S029/S034 (`claims.md:127-129`). Round-63 tip: exit 0,
   33 rows, three W04s S024/S028/S029 (`W2FinalIndependent.md:139-143`). Appends between
   rounds; no contradiction, and W04 does not fail a clean lane.
9. **Exit 0 is not claim satisfaction (M34).** `measure-before.log` prints
   `HOLDS_OK=yes` together with `C4_RECEIPT_KILLED_ATTRIBUTED=0/2` and `HOLDS_OK_V2=no`;
   by `measure.py:273` (`0 if holds_ok`) that run exits 0. The exit code of that recorded
   run is **derived**, not observed — the receipt prints no exit line. The draft's §3
   states the rule explicitly.
10. **Sibling instrument digest matches.** SKILL.md §7 pins
    `measure.py` sha256 `b8e68d32…b9168`; the working-tree file hashes identically.
    No conflict.

## Known limits

- Promised-outcome text for the counter's labels is derived from `measure.py`'s print
  statements plus `measure-before.log`; it holds for this frozen counter only.
- The oracle promise (five `REGION` lines, `ORACLE OK`, exit 0) is a recorded observation
  from round 63, not a run of this seat.
- The ledger-discipline section adds no rule; every sentence cites `PROVINCE.md`,
  `QUALITY.md`, `corpus/README.md` or the round-63 LEDGER.
- No non-author review of `checklists.md` yet; `R64ReviewSkill*` / `R64CriticSkill` own
  that pass, and the SHONEN box stays unflipped on my output alone.
- `checklists.md` lives in `/tmp/revenger-r64-skill/`; if wave scratch is cleared before
  L1 merges, the draft is lost. Its section map, checksum and every source citation are
  reproduced above so the content is recoverable from the repo.

## Artifact paths

- `/tmp/revenger-r64-skill/checklists.md` — sha256 `07cdfdafd2ed557ed8f21b19c531e1f900284708e3302de10a6a443600f7b8db`
- `.ufo/waves/round-64/R64SkillChecklists.md` — this report
- `/tmp/revenger-r64-skill/SKILL.md` — sibling draft, read only (23,390 B)

Report: .ufo/waves/round-64/R64SkillChecklists.md
