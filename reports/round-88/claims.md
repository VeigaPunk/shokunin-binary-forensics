# round-88 claims — frozen before any landing or after-run

Base: `48db9e0cee274250b2e14a03760759ee7e7375fd` (r87 adjudication tip + the
non-author verifier spot-check, pushed clean). Round type: FRESH-START
(r71/r72/r73 rejected closures re-read; §gate below). ONE claim, calibration,
not exploratory, with counting commands. Reds were captured over the base-state
tree before this freeze; the landing and after-runs come only in later commits.

## Carry-in addressed first (status-neutral; r87 closure — clean, four operator-side notes only)

- r87 closure item 1 (SHONEN boxes 2-3 non-author-checkable, operator-side):
  routing re-recorded; SKILL.md changes this round (the registry row), so the
  standing need names the r88 bytes at round end; no box marked by the author.
- r87 closure item 2 (plain-mode git-checkout dependency): the class is
  inherited and DISCLOSED in the new registry row's write-scope field (the
  sweep's COMMITTED_GIT channel runs `git log`; same class as receipt_probe2's
  LEG4 `git show`). No frozen v2 byte changed; the operator-side disclosure
  stands.
- r87 closure item 3 (census literal form, operator-side lineage L0 r79):
  dual round-start receipts landed
  (`.ufo/waves/round-88/census-round-start-{sanctioned,literal}.log`;
  sanctioned exit 0, 21 W01 + 10 W04, zero E; literal exit 2, routed around,
  nothing assumed answered).
- r87 closure item 4 (S473 quote word-count precision): ADDRESSED BY THIS
  ROUND'S CLAIM — the word-count receipt class is the claim's target; the
  lesson-level erratum (the r87 lesson's recorded "13 words" for the
  SCORECARD quote: whitespace-rule count 12, slash-split count 13; the quote
  itself verbatim, both counts ≤ 25) is mined in `corpus/lessons/round-88.md`
  as the same class the six registry drifts instantiate. S473's own registry
  row carries no word-count token (checked), so no registry closure row is
  needed for it.

## §gate — fresh-start (r71/r72/r73 re-read; what was ruled out and why)

All three rejected closures re-read this round at the fleet reports
(`.ufo/reports/round-7{1,2,3}/revenger.md` exist; verdict lines match the
dispatch digests): r71 (C1 coverage/K C05 sixth pass — falsified on
Q09/Q16 self-map overclaims at `dac9590`), r72 (C1 coverage/C15 tool
landscape — `C15_TOOL_ROWS=18/18` but `C15_HELD_BACKED=0/1` at `d6475ee`;
row labels are not admission), r73 (C1 coverage/C10 — wave released
un-settled, 0 vote files, unresolved honest stop). Common thread: all three
are K-admission claims whose frozen predicate needs a wave Q-review surface
that has never settled on this host (L0 r74 re-read this round,
`freshstart-probes.log` probe 6b, unanswered). A do-nothing control reaches
each identically here: the predicate's deciding input does not exist on this
host, so landing row work alone cannot move the counter. The r88 claim routes
through none of that.

Ruled out with fresh probes (`reports/round-88/freshstart-probes.log`,
2026-11-02, registered patterns pasted verbatim from the r87 receipt):

- **coverage/K** — operator-blocked (probe 6b; L0 r74 unanswered).
- **coverage/F android** — hard-gated (probe 1: `REA_JADX_MCP_JAR` UNSET, no
  jadx on PATH; S448 stands; F4's honest exception stays 10/11).
- **coverage/M, A1, A1v2, F4** — saturated (3/3, 3/3, 5/5, 10/11; the frozen
  holds re-run over the landing archive at adjudication must stay green).
- **coverage/asset-catalog** — macOS-gated (probe 6 registered metric: 7
  `availability_code: unsupported_host` groups printed 2026-11-02, same
  sentinel as r85/r86/r87; probe 3's loose noise pattern printed 31,
  disclosed as noise per the r87 mined class).
- **calibration criterion N** — CLOSED r87 (the routed pair landed; the
  criterion score stays 10.0 held). criterion C repair — §9-ruled-out twice
  (needs the operator to rule the fixture-chain re-authoring in scope).
- **depth — the r86/r87 planned registry-edit reader checklist** — trigger
  unmet: no drift recurrence since v7 (`mismatch=0` stands); declaring the
  conditioned row with its trigger false would be manufacturing need.
- **considerthese 2026-10-28 Q16 self-map checker proposal** — considered,
  NOT adopted (re-read this round): its natural consumers are the
  operator-blocked C05 re-gate surface; routed stays (third consecutive
  round).
- **exploratory claim** — none declared (the claim carries counting
  commands).

Lowest-axis routing: the lowest-scoring non-retired axis is coverage (K 5.3
< 7.0 — the stagnation nudge does NOT apply) — but every reachable coverage
surface is saturated, hard-gated, or operator-blocked at base. The
obligation routes this round on documented unreachability (fresh probes
receipted 2026-11-02), not on the nudge.

## C1 — calibration: criterion R full extension — the receipt rule becomes a registry-wide machine check; six legacy word-count receipts found false under the declared rule and closed by verified supersessions

The routed r76 item, carried through every Routed-forward list since r76
("criterion R full extension to the legacy receipt-quoting rows"): criterion
R's machine check covered exactly TWO rows (S444 via receipt_probe2 LEG4's
standing negative control, S445 via LEG3's exact tokens) out of 473. This
round the criterion becomes a registry-wide gate, and the extension's first
run finds REAL drift: six of the seven legacy word-count receipts record
counts that are false under any declared rule.

- **The declared word-count rule**: a word count is `len(quote.split())` —
  whitespace split; delimiters do not split words. A receipt recording a
  word count without declaring a rule is not re-runnable (the criterion-R
  violation r76 named); one that declares no rule AND records a value no
  rule reaches (S454's 10 vs 11; S462's 11 vs 10) is false, not merely
  underspecified. S459's recorded 16 is reachable only under
  hyphen-splitting, which the row never declared.
- **Instrument**: `reports/round-88/receipt_sweep.py`, sha256
  `57098ed5b8f427ae331da87a1ed68ed4efe909196686db4953612ab643771271`
  (17,664 bytes, LF, frozen at this commit). Plain mode sweeps EVERY
  `| S### |` row's anchor cell (column 7 of 11) over the declared
  receipt-token set (P1 word-count / P2 prints / P3 key=value / P4
  colon-count / P5 ORACLE OK), classifies every receipt row (LEG_BOUND
  when the cell cites a backticked command, NON_COMMAND_NUMERIC
  otherwise), verifies every P1 receipt against its bound source under the
  declared rule (the frozen WC_MAP carries the byte-exact quotes and the
  deriving channels: LIVE_PRODUCER for the four rea help/llms legs,
  COMMITTED_GIT for the r78 subject, COMMITTED_FILE for the r81 spotcheck
  quote, PRODUCER_PKG for the installed 6.8.0 parser source), and closes a
  drift only through a superseding row that itself verifies (present,
  declares `supersedes S<id>`, carries the same quote, records the
  rule-derived count). `--sources PATH`: declared registry override (the
  prelanding dry run uses it over a staged copy; the channel legs still
  resolve from the lane root, so `git log` and the committed-file leg read
  the lane tree, not the staged copy). `--selftest`: hermetic (synthetic tables, stub
  channels; no producer call, no git, no file reads). Usage exit 64;
  malformed row or missing registry exit 2. Named limitations declared in
  the instrument header and the registry row: tokens outside the anchor
  cell, receipt wordings outside the declared set ("shows 7", "prints as"),
  and P2-P5 values (registered, not re-derived — the census pair stays
  with receipt_probe2's standing legs).
- **The six drifts (red, over base-state rows,
  `sweep-red-prelanding.log`, exit 1)**: S454 recorded 10, whitespace count
  11; S456 recorded 11, count 12; S459 recorded 16, count 14; S461 recorded
  19, count 17; S462 recorded 11, count 10; S463 recorded 10, count 7.
  S457 verifies (9 = 9). Every quote verified verbatim in its own row's
  anchor AND in its bound source at the preprobe
  (`preprobe-map-check.log`, MAP_CHECK_ALL_OK=True — the sources were
  re-opened 2026-11-02, so the drifts are not transcription artifacts: the
  quotes are faithful, the COUNTS are false).
- **Counting instrument**: `reports/round-88/sweep_probe.sh`, sha256
  `9a2cb44251619e8bedfc71862a507550d944fbbb4f58948dd63d4ea385e77cd0`
  (frozen at this commit; r87 shape: PATH stripped of the producer
  directory, sed-must-change-bytes guard, mktemp copies removed on exit).
- **The mutant pair (two frozen one-substitution sed mutants, each killed
  with its own attributed last line, exactly one line each — 2 diff lines
  including the diff header pair)**:
  - mutant A (comparator blind):
    `s|def counts_match(recorded, derived): return recorded == derived|def counts_match(recorded, derived): return True|`
    — mutated-copy sha256
    `bceb9a338ce76bcb3fd25d3649ded3fde13ddc6734ef6fce1ed52d8fb0de1c30`;
    dies exit 1, last line `selftest: word-count comparator accepted a
    wrong count` (dies at ST1's drift assertion; ST1 precedes ST2).
  - mutant B (closure blind):
    `s|def closure_ok(closure_recorded, quote_ws, quote_in_row, supersedes_ok): return quote_in_row and supersedes_ok and counts_match(closure_recorded, quote_ws)|def closure_ok(closure_recorded, quote_ws, quote_in_row, supersedes_ok): return True|`
    — mutated-copy sha256
    `6c65f6ddb7d8cc021a616339d7e7f6548272661498344b8714bad450107ba7b0`;
    dies exit 1, last line `selftest: closure accepted an unverified
    supersession` (its comparator intact, it passes ST1 and dies at ST2's
    wrong-count-closure rejection).
  - Counter red form receipted (`sweep-red-prelanding.log`:
    `PROBE_RED_EXIT=1` over a non-conforming target — the counter can fail).
- **Fix (the landing)**: six superseding SOURCES rows appended inside the
  Registry directly after S473 — S474 (supersedes S454, records 11), S475
  (supersedes S456, records 12), S476 (supersedes S459, records 14), S477
  (supersedes S461, records 17), S478 (supersedes S462, records 10), S479
  (supersedes S463, records 7) — each re-opening its source 2026-11-02,
  each carrying the byte-exact quote + the declared-rule count + the
  supersedes declaration. Append-only discipline held: no existing row is
  edited in place (the supersession discipline is the same shape as
  S445-supersedes-S444). Plus the SKILL.md §Gate registry row for
  `receipt_sweep` (8 → 9 rows) so the extension is a REGISTERED gate, not a
  loose script.
- **Prelanding green dry run** (`sweep-red-prelanding.log`, same receipt:
  `SWEEP_GREEN_DRYRUN_EXIT=0`): the sweep over the STAGED registry (base
  rows + the six new rows, staged copy only — nothing landed) already
  prints `SWEEP_ROWS_SCANNED=479`, `CLOSED=6/6`, `OPEN=0`, green exit 0,
  with every closure resolved `by=S47x(corrected-count)` — the landing's
  expected state, captured before the landing.
- **Green (after landing, from the committed blobs over the landing tip)**:
  the sweep over the landing tree prints `SWEEP_ROWS_SCANNED=479`,
  `SWEEP_WORDCOUNT_VERIFIED=1/7`, `SWEEP_WORDCOUNT_CLOSED=6/6`,
  `SWEEP_WORDCOUNT_OPEN=0`, `SWEEP_VERDICT=green`, exit 0
  (`sweep-green.log`); the mutant kills and the counter conformance re-derive
  from the committed blobs (`mutant-kill-after.log`,
  `sweep-probe-after.log`).
- **Counting commands** (all paste-able on this host, from the lane root):
  1. `PYTHONUTF8=1 python -B reports/round-88/receipt_sweep.py; echo $?`
     → red over base state: `SWEEP_WORDCOUNT_OPEN=6`, exit 1
     (`sweep-red-prelanding.log`) → green over the landing:
     `SWEEP_WORDCOUNT_OPEN=0`, exit 0 (`sweep-green.log`).
  2. `bash reports/round-88/sweep_probe.sh reports/round-88/receipt_sweep.py; echo $?`
     → `1/1 · 2/2 · 1/1`, exit 0 (both ends; the frozen bytes do not
     change between freeze and landing).
  3. `sed -n '/^## Gate registry/,/^## 7\./p' SKILL.md | grep -cE '^\| name \|'`
     → 8 → 9 (the receipt_sweep row).
- **Axis moved**: calibration (the criterion-R machine check's coverage:
  2 rows machine-checked since r76 → every row scanned every run, every
  receipt token classified, every word-count receipt rule-verified or
  machine-closed; six false legacy receipts superseded and closed). The
  criterion-R score stays held at its r76 value — the moved quantity is the
  criterion's registry-wide reach and the six receipts' correction, the
  same shape as r87's registration move. Coverage, freshness, depth,
  operability, adjacency: unchanged (the frozen holds re-run over the
  landing archive must stay green at adjudication; PROVINCE byte-unchanged;
  no knowledge byte).
- **Sourcing**: C1 rests on the six rows opened this round (S474-S479,
  appended by the landing) plus the drift evidence they carry; each was
  opened by re-running or re-reading its bound source on 2026-11-02 (the
  preprobe receipt records both containment checks per row).
- **No-harm**: no verifier byte, no corpus/live, no fixture, no knowledge
  byte, no README byte, no PROVINCE byte, no QUALITY byte; SKILL.md changes
  are the one appended registry row (additions only); SOURCES.md changes
  are the six appended rows. Receipt `noharm-diff.txt` at adjudication.
- **Separability**: single claim — the c1-only tree (archive of base +
  the two instruments only, no SKILL row, no SOURCES rows) must reproduce
  the red (`c1-only.log`); the disclosed marker difference (the
  COMMITTED_GIT leg reports CHANNEL_UNREACHABLE in a non-git tree — the
  channel needs the lane repository) is itself the proof the instruments
  read nothing outside their bytes, the registry, and the named channels.

## Commit ordering

This freeze (claims + receipt_sweep.py + sweep_probe.sh +
sweep-red-prelanding.log + preprobe-map-check.log + preprobe-history.log +
freshstart-probes.log + census round-start receipts) lands BEFORE any
landing or after-run. The landing (SOURCES.md S474-S479 + the SKILL.md
registry row) lands before the adjudication (scorecard/log/lesson + holds +
noharm + separability + round-end census); the official green/mutant/probe
receipts are re-derived from the committed blobs at the landing tip and land
in the receipt-completion commit. No measured value quoted here is
re-derivable only from uncommitted state.
