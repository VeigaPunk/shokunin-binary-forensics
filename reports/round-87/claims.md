# round-87 claims — frozen before any landing or after-run

Base: `1306ec9ac32a4d4477cc15049c1d09e326ecac5a` (r86 tip + non-author
spot-check, pushed clean). Round type: FRESH-START (r71/r72/r73 rejected
closures re-read; §gate below). ONE claim, not exploratory, with a counting
command; the round's second routed axis obligation is addressed in §gate
(documented unreachability). Reds were captured over the pre-landing tree
before this freeze; the landing and after-runs come only in later commits.

## Carry-in addressed first (status-neutral; r86 closure — clean, no defects routed)

- r86 closure item 1 (census contract-literal form exit 2, operator-side
  r74–r86 lineage): dual round-start receipts landed
  (`.ufo/waves/round-87/census-round-start-{sanctioned,literal}.log`;
  sanctioned exit 0, 21 W01 + 10 W04, zero E; literal exit 2, routed
  around, nothing assumed answered; L0 r79 still unanswered).
- r86 closure item 2 (SHONEN box 1 non-author re-confirmation,
  operator-side): routing re-recorded; SKILL.md changes this round, so the
  standing need names the r87 bytes at round end; no box marked by the
  author. The r86 verifier's box-3 substance confirmation is cited in
  SHONEN.md's standing pointer, not promoted to `[x]` by the author.
- r86 closure item 3 (coverage unreachability routing must be re-probed
  fresh each round): re-probed fresh 2026-11-02 — see §gate.

## §gate — fresh-start (r71/r72/r73 re-read; what was ruled out and why)

All three rejected closures re-read this round at the fleet reports
(`.ufo/reports/round-7{1,2,3}/revenger.md` exist; verdict lines match the
dispatch digests): r71 (C1 coverage/K C05 sixth pass — falsified on
Q09/Q16 self-map overclaims at `dac9590`), r72 (C1 coverage/C15 tool
landscape — `C15_TOOL_ROWS=18/18` but `C15_HELD_BACKED=0/1` at
`d6475ee`; row labels are not admission), r73 (C1 coverage/C10 — wave
released un-settled, 0 vote files, unresolved honest stop). Common
thread: all three are K-admission claims whose frozen predicate needs a
wave Q-review surface that has never settled on this host (L0 r74
re-read this round, `freshstart-probes.log` probe 6b, unanswered). A
do-nothing control reaches each identically here: the predicate's
deciding input does not exist on this host, so landing row work alone
cannot move the counter. The r87 claim routes through none of that.

Ruled out with fresh probes (`reports/round-87/freshstart-probes.log`,
2026-11-02):

- **coverage/K** — operator-blocked (probe 6b; L0 r74 unanswered).
- **coverage/F android** — hard-gated (probe 1: `REA_JADX_MCP_JAR`
  UNSET, no jadx on PATH; S448 stands; F4's honest exception stays
  10/11).
- **coverage/M, A1, A1v2** — saturated (3/3, 3/3, 5/5; the frozen holds
  re-run over the landing archive at adjudication must stay green).
- **coverage/asset-catalog** — macOS-gated (probe 6: 7
  `availability_code: unsupported_host` groups printed 2026-11-02, same
  count as r85/r86 — the sentinel did not move; probe 3's first loose
  pattern `grep -ciE unsupported` printed 31 by counting limitation-text
  lines — disclosed in the receipt, mined as the loose-pattern class).
- **depth — the r86 planned "registry-edit reader checklist if the
  drift class recurs"** — trigger unmet: the v7 `SWEEP_SRC mismatch=0`
  state stands and no recurrence happened; declaring the conditioned row
  with its trigger false would be manufacturing need.
- **considerthese 2026-10-28 lesson-1 proposal** (a checker comparing an
  entry's claimed coverage sets against the command's actual compared
  set) — considered, NOT adopted this round: its natural consumers are
  the operator-blocked C05 re-gate surface, and it is a larger
  instrument than one bounded round; routed stays.
- **exploratory claim** — none declared (the claim carries counting
  commands).

Lowest-axis routing: the lowest-scoring non-retired axis is coverage
(K 5.3 sits below the 7.0 saturation line, so the stagnation nudge does
NOT apply) — but every reachable coverage surface is saturated,
hard-gated, or operator-blocked at base. The obligation routes this
round on documented unreachability, not on the nudge; the receipts above
are the falsifiable form of that statement (re-probed fresh this round,
not inherited — the r86 closure's standing condition).

## C1 — calibration: criterion N's mutation-killed attribution pair lands on the negctl harness itself (instrument v2), and the criterion-N instrument gets its registry row

The routed r75-planned-(b) item, carried through r86 ("criterion N
attribution pair" in every Routed-forward list since r75): the v1
negctl harness (`reports/round-75/probe_negctl.sh`, sha256
`eb5d1b54fa20421c09cd55e15d6a849af1379a822887b5a6ef60e0935c013fad`,
frozen bytes, never touched this round) passes its four legs but exposes
NO self-test mode, NO declared usage exit, and NO mutation-checked
verdict logic — a verdict-instrument drift in the harness itself would
be invisible. Twelve rounds of routed debt; the r79 v2 precedent
(`receipt_probe2`/`gate_probe2`, supersedes-v1 + `--selftest` + frozen
sed mutant + usage exit 64) is the fix shape.

- **Instrument**: `reports/round-87/probe_negctl2.sh`, sha256
  `d70271464a437a6c0de598237a603cc50498458a14c94e37f8df2edf7e03070d`
  (frozen at this commit). Plain mode (no arguments): v1-identical legs,
  value lines and verdict contract over the same frozen P1/P2 fixtures
  (v1's logic refactored into named verdict functions;
  `plain-equal-prelanding.log`: v1/v2 plain outputs byte-identical,
  diff empty, both exit 0; the official `plain-equal.log` re-derives
  from the committed blobs at receipt-completion). `--selftest`:
  hermetic — synthetic verdict vectors only, no fixture build, no probe
  run, no producer call; expected finding-ids
  `NEGCTL_SELFTEST_FALSEPASS_LOGIC=ok`,
  `NEGCTL_SELFTEST_ATTRIBUTION_GUARD=ok`,
  `NEGCTL_SELFTEST_STALE_LOGIC=ok`,
  `NEGCTL_SELFTEST_UNRECORDED_LOGIC=ok`, last line
  `NEGCTL_V2_SELFTEST=pass`, exit 0. Unrecognized invocation: usage line
  on stderr, exit 64.
- **The pair (two frozen one-substitution sed mutants, each killed with
  its own attributed last line, from the committed bytes)**:
  - mutant A (verdict blind):
    `s|^stale_flag_ok() {.*|stale_flag_ok() { return 0; }|` — exactly
    one line (35); mutated-copy sha256
    `f70c0e9aceb72323550b4d3732edaa39013498fc2607b286f0adeddf49c79a99`;
    dies exit 1, last line `selftest: stale-record verdict accepted a
    false-pass`.
  - mutant B (attribution pattern relaxed to `.*`):
    `s|'\^engine-ghidra \.\*STALE-RECORD'|'.*'|` — exactly one line
    (35); mutated-copy sha256
    `ec29099cf02b9d10b4a9f15368e22d0ed0977d667b0e83969eedf1ffdce439cb`;
    dies exit 1, last line `selftest: attribution guard accepted an
    unattributed kill`. Deterministic attribution ordering: ST1
    (false-pass rejection) precedes ST2 (attribution guard), so mutant A
    dies at ST1 and mutant B — whose `[ "$1" = "1" ]` guard still
    rejects exit-0 inputs — dies at ST2 with its own message.
- **Counting instrument**: `reports/round-87/selftest_probe.sh`, sha256
  `ed0b328279133579a100d99f331ba752267782cd9b6764899c2082bfad4d87ed`
  (frozen at this commit; r79 shape: PATH stripped of the producer
  directory, sed-must-change-bytes guard, mktemp copies removed on
  exit). The SAME command measures both ends.
- **Red** (`negctl-red.log`, over the v1 bytes = base bytes):
  `NEG_SELFTEST_MODE_PRESENT=0/1`,
  `NEG_SELFTEST_MUTANTS_KILLED_ATTRIBUTED=0/2`, `NEG_USAGE_EXIT64=0/1`,
  exit 1; v1 blindness markers `usage:`/`NEGCTL_V2_SELFTEST`/
  `stale_flag_ok`/`attribution guard` all grep 0; v1 baseline (plain
  legs green, exit 0 — the harness works but cannot show it can fail)
  receipted at `negctl-v1-baseline.log`.
- **Green** (after landing, from the committed blob):
  `NEG_SELFTEST_MODE_PRESENT=1/1`,
  `NEG_SELFTEST_MUTANTS_KILLED_ATTRIBUTED=2/2`, `NEG_USAGE_EXIT64=1/1`,
  exit 0 (`negctl-green.log`, receipt-completion commit, landing tip
  named; `negctl-mutant-kill-after.log` carries both attributed deaths
  with the one-line diffs and mutated-copy shas).
- **Registration**: the criterion-N instrument gets its
  SKILL.md §Gate-registry row (first registration — v1 was never
  registered, the same gap the round-78 registration closed for R/G;
  probe bytes sha pinned; §Gate-standard verdict map with declared
  0/1/2/64; self-test clause satisfied with the two-evidences pair
  `negctl-red.log` vs `negctl-green.log` over committed input snapshots).
- **Counting commands** (both paste-able on this host):
  1. `bash reports/round-87/selftest_probe.sh reports/round-87/probe_negctl2.sh; echo $?`
     → red-over-v1 form `bash reports/round-87/selftest_probe.sh reports/round-75/probe_negctl.sh; echo $?`
     = `0/1 · 0/2 · 0/1`, exit 1 (`negctl-red.log`) → `1/1 · 2/2 · 1/1`,
     exit 0 (`negctl-green.log`).
  2. `sed -n '/^## Gate registry/,/^## 7\./p' SKILL.md | grep -cE '^\| name \|'`
     → 7 → 8 (the criterion-N row).
- **Axis moved**: calibration (verdict-instrument self-conformance — the
  moved quantity is the criterion-N instrument's ability to show it can
  fail, plus registry visibility of the criterion's instrument; the
  criterion-N score itself stays 10.0 held, exactly like the r79
  receipt_probe2 registration moved no criterion score). S473 (appended
  this round, inside the Registry directly after S472) grounds the
  claim: the routed-debt evidence row.
- **No-harm**: no verifier byte, no corpus/live, no fixtures, no
  knowledge byte, no README byte, no PROVINCE byte; SKILL.md changes are
  the one appended registry row (additions only); SOURCES.md changes are
  the one appended S473 row. Receipt `noharm-diff.txt` at adjudication.
- **Separability**: single claim — the C1-only tree (archive of base +
  `probe_negctl2.sh` + `selftest_probe.sh` only, no SKILL row, no
  SOURCES row) must run green identically (`c1-only.log`), because the
  instruments read nothing outside their own bytes and the v1 fixture
  inputs.

## Commit ordering

This freeze (claims + probe_negctl2 + selftest_probe + negctl-red +
negctl-v1-baseline + freshstart-probes + preprobe receipts + census
receipts) lands BEFORE any landing or after-run. The landing (SKILL.md
registry row + S473) lands before the adjudication (scorecard/log/lesson
+ holds + noharm + separability + round-end census); the official
green/mutant/plain-equal receipts are re-derived from the committed
blobs at the landing tip and land in the receipt-completion commit. No
measured value quoted here is re-derivable only from uncommitted state.
