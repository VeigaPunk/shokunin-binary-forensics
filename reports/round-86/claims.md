# round-86 claims — frozen before any landing or after-run

Base: `d7fd9d93c522ccc6f2b8f46a56cb90231926c43e` (r85 tip + non-author
spot-check, pushed clean). Round type: FRESH-START (r71/r72/r73 rejected
closures re-read; §gate below). Two claims, distinct axes, causally
separable, neither exploratory. Both reds were captured over the SAME
pre-fix tree at base before this freeze; the landings and after-runs come
only in later commits.

## Carry-in addressed first (status-neutral)

- r85 closure item 1 (mg_probe.py docstring prediction line vs the
  registered 0/3 red): `reports/round-85/corrections.md` correction 2 —
  the ruling recorded, the conditional fix trigger documented (r86 does
  not touch mg_probe.py; the verified sha pin
  `1840c30cf4f1cad0815c89ca80492053d4a43c5d752609a2edf33fa21a3ac03f`
  stays valid), the standing wording rule stated. No in-place rewrite.
- item 2 (census contract-literal form exit 2, operator-side r74–r85
  lineage): dual round-start receipts landed
  (`.ufo/waves/round-86/census-round-start-{sanctioned,literal}.log`;
  sanctioned exit 0, 21 W01 + 10 W04, zero E; literal exit 2, routed
  around, nothing assumed answered).
- item 4 (SHONEN non-author re-confirmation of the CURRENT SKILL.md
  bytes): stays operator-side routing; no box marked by the author.
- item 3 (per-revision-corpus basis movement): honored — every r86 sweep
  receipt cites its `SWEEP_CORPUS` basis line first.

## §gate — fresh-start (r71/r72/r73 re-read; what was ruled out and why)

All three rejected closures re-read this round at the fleet reports
(`.ufo/reports/round-7{1,2,3}/revenger.md`): r71 (C1 coverage/K C05
sixth pass — falsified on Q09/Q16 self-map overclaims; C2 verified), r72
(C1 coverage/C15 tool landscape — 18/18 row labels but no held row;
falsified, coverage denominator harmed), r73 (C1 coverage/C10 — wave
released un-settled; unresolved honest stop). Common thread: all three
are K-admission claims whose frozen predicate needs a wave Q-review
surface that has never settled on this host (r74 L0: no L2/AgentSwarm
dispatch surface; wave-Q admissions blocked — re-read this round,
`freshstart-probes.log` probe 3, unanswered). A do-nothing control
reaches each identically here: the predicate's deciding input does not
exist on this host, so landing the row work alone cannot move the
counter. Neither r86 claim routes through K, any wave vote file, or any
other operator-blocked surface.

Ruled out with fresh probes (`reports/round-86/freshstart-probes.log`,
2026-11-02):

- **coverage/K** — operator-blocked (probe 3; L0 r74 unanswered).
- **coverage/F android** — hard-gated (probe 1: `REA_JADX_MCP_JAR`
  UNSET, no jadx on PATH; S448 receipt stands; F4 honest exception stays
  10/11).
- **coverage/M, A1, A1v2** — saturated (3/3, 3/3, 5/5; the frozen holds
  re-run over the r86 landing archive at adjudication must stay green).
- **coverage/asset-catalog** — macOS-gated (probe 2: 7 unsupported_host
  groups printed this round, same count as r85).
- **ghidra-headless repeat** — no new measurement (r75 capability row
  holds; r85 non-author spot-check concurred).
- **criterion C repair / R full extension / N attribution pair** —
  §9-sizing and r75–r85 lineage stay routed; this round's calibration
  claim is the routed v7 vector the r84/r85 lessons named instead.
- **exploratory claim** — none declared (both claims carry counting
  commands).

Lowest-axis routing: the lowest-scoring non-retired axis is coverage (K
5.3 sits below the 7.0 saturation line, so the stagnation nudge does NOT
apply) — but every reachable coverage surface is saturated, hard-gated,
or operator-blocked at base (probe 6 enumeration). The obligation routes
this round on documented unreachability, not on the nudge; the receipts
above are the falsifiable form of that statement (re-probed fresh this
round, not inherited).

## C1 — calibration: orphan_sweep v7, per-source citation-sites accounting (the routed r84/r85 candidate vector 1), with the live used-by pointer-drift class surfaced and closed

- **Instrument**: `reports/round-86/orphan_sweep7.py`, sha256
  `f955cd7d634f8aa4f61c1734195dd32c959e8d5f347f5cd320484360c1948618`
  (frozen at this commit; change 10 = SOURCES.md used-by pointer
  accounting, non-gating; v6 stays byte-untouched, blob sha
  `b2db45b0…f12b7` re-verified this round).
- **Red pair, same pre-fix tree (base `d7fd9d9`)**:
  - `sweep7-v6-blind-prelanding.log` — v6 over the tree: zero
    `SWEEP_SRC` lines (`grep -c` → 0): the class does not exist in v6;
    basis `SWEEP_CORPUS fleet-reports=26 lessons=52 log=1`; gating
    `CITED=1050 COMMITTED=988 LANDABLE_ORPHANS=0 ABSENT=62`, exit 0.
  - `sweep7-red-prelanding.log` — v7 over the SAME tree:
    `SWEEP_SRC registry=disk rows=451 sites=499 cited=493 mismatch=6
    absent=0` with the six exception lines
    (S448→reports/round-77/claims.md, S449→SKILL.md,
    S450→reports/round-78/province_probe3.sh,
    S451→reports/round-79/claims.md, S453→reports/round-79/claims.md,
    S456→reports/round-80/orphan-before.log); identical basis and
    gating, exit 0 (non-gating confirmed). The census existence check
    passes on all six pointers — the drift is invisible to every
    standing instrument by construction; the preprobe
    (`freshstart-probes.log` probes 4–5) cross-checks each pointer with
    `grep -cw` (all six CITES=0; each row's OTHER pointer cites, so
    `mined` stays valid per CORPUS.md's status contract).
- **Fix (SOURCES rule 2)**: drop exactly one non-citing pointer per row
  (six in-place used-by cell changes, old→new logged in
  `corpus/lessons/round-86.md`).
- **Green**: v7 over the fixed tree prints `mismatch=0` (adjudication
  receipt `sweep7-real-after.log`, run from the committed blob over the
  committed adjudication tip, basis line first; the landing-time state is
  additionally receipted).
- **Mutation check**: `sweep7-selftest-red.log` — selftest 25 legs + pass
  exit 0 from the pre-freeze bytes; ONE frozen one-substitution sed
  mutant (`USED_BY_ACCOUNTING = True` → `False`, exactly line 165,
  mutated sha `0bfe69a08d3d0491e55a6af5e2fa08a9438b732ea1a8eb7579f61b73db3028c3`)
  dies exit 1 attributed `selftest: used-by accounting drifted (used-by
  class)`. After-runs from the committed blob at adjudication
  (`sweep7-selftest-after.log`, `sweep7-mutant-kill-after.log`).
- **Counting command** (before → after, both paste-able, both on this
  host over committed bytes):
  `PYTHONUTF8=1 python -B reports/round-86/orphan_sweep7.py --lane <lane-dir> --fleet <fleet-root> --format summary | grep -E '^SWEEP_SRC '`
  → red `mismatch=6` (over base `d7fd9d9` tree, receipt
  `sweep7-red-prelanding.log`) → green `mismatch=0` (over the fixed
  tree, receipt `sweep7-real-after.log`); plus the blind leg
  `PYTHONUTF8=1 python -B reports/round-85/orphan_sweep6.py … | grep -c SWEEP_SRC`
  → `0` at both ends.
- **Axis moved**: calibration (citation attribution fidelity — a used-by
  pointer that names a document which never cites the row stops being
  invisible; the moved quantity is pointer-truth, not a criterion score).
  S472 (appended this round, inside the Registry directly after S471)
  grounds the claim: the drift evidence row.

## C2 — depth: SKILL.md gains the pointer-hygiene decision rows and the M42 named error signature

- **Red** (`skill-red-greps.log`, over base bytes): §4 error-pattern
  rows `grep -cE '^\| M[0-9]+ \|' SKILL.md` → 9 (M33–M41, no
  pointer-drift signature); `grep -c 'cite-back' SKILL.md` → 0 (no
  cite-back rule anywhere); `grep -c 'used-by' SKILL.md` → 4 (only the
  rule-2 logging mention + census rows).
- **Change**: §3 rule table gains two rows (cite-back rule: every listed
  used-by pointer names a document whose bytes cite the row id back,
  checked by the sweep's per-source accounting; placeholder semantics:
  em/en dash + ASCII hyphens mean no citation sites, machine parsers
  treat them as empty — the preprobe's own em-dash false-positive class
  is the named specimen). §4 gains M42 (pointer-drift: used-by written as
  evidence-location instead of citing-paths; six live r78–r80-vintage
  specimens; the check that catches it is the v7 accounting; fix is the
  rule-2 pointer drop logged old→new).
- **Counting command** (before → after):
  `grep -cE '^\| M[0-9]+ \|' SKILL.md` → 9 → 10; and
  `grep -c 'cite-back' SKILL.md` → 0 → 2 (the two new §3 rows). Measured
  over the landing archive at adjudication.
- **Axis moved**: depth (a reader can now act on SKILL.md alone when
  writing or auditing used-by pointers; before, the skill's rule-2 row
  permitted pointers with no cite-back property at all — the exact
  defect six live rows exhibit). Grounded in S472.
- **Separability**: C2's greps touch only SKILL.md; C1's instrument and
  fix never read SKILL.md §3/§4 rows (the accounting reads SOURCES.md
  plus the pointer-named files). Receipts `c1-only.log` / `c2-only.log`
  at adjudication (archive-of-base + claim files only, mirroring r85).

## Commit ordering

This freeze (claims + v7 + reds + probes + census receipts +
corrections.md correction 2) lands BEFORE any fix or after-run. The
landing (six used-by fixes + S472 + SKILL.md rows) lands before the
adjudication (scorecard/log/lesson + committed-blob after-runs + holds +
noharm + separability + round-end census). No measured value quoted here
is re-derivable only from uncommitted state.
