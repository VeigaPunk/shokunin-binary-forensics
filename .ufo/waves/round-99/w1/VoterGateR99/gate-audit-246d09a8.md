# VoterGateR99 gate audit — Amendment B candidate, digest 246d09a8cf6523ab380f88f7945f220338c27e31f8b43ba876bbd0a9a8d746da

Seat: VoterGateR99 (role reviewer). Candidate: `corpus/knowledge/round-98-rea-host-readiness.md` at
lane commit `9ddd38ac8baef67d689ac36fa233aaaef35b1703` (Amendment B; claims `reports/round-99/claims.md`
§Amendment B). Audit date: 2026-11-05. Supersedes this seat's
`gate-audit-36cc6ac2.md`, whose Q16 FAIL was upheld and fixed by this amendment. Criteria: Q01–Q17
of `corpus/QUALITY.md`. All commands read-only from the lane root. No counter was run on any tree;
`corpus/README.md` and the entry's `admission-status` line were not touched.

## 0. Vote-binding digest

v7 `digest()` on the amended entry prints exactly
`246d09a8cf6523ab380f88f7945f220338c27e31f8b43ba876bbd0a9a8d746da` — equal to the Amendment B
vote-binding digest. Vote proceeds on it.

## 1. What Amendment B changed (git diff 7e6edd4..9ddd38a, both files read in full)

- **Derivation table regenerated**: 21 rows → 29 rows. The preamble now states a cell rule: each
  output cell is the command's stdout verbatim, one code span per stdout line joined by ` / `; in the
  record-digest row the parenthesised file name is the rest of the same stdout line; text after an
  em dash is annotation. Padding and prefixes are removed inside the commands (`sed 's/^ *//'`,
  `cut -d' ' -f1`, `sed 's/^classification: //'`), never in the cells — the exact defect this seat
  reported against line 80 of the pre-amendment bytes.
- **New rows**: host identity; healthy and failing scope checks (the old combined row split);
  ghidra-named scope-check count (the old "(of 8" denominator now derived); ghidra-headless launcher
  path; installed skill identity; doctor binwalk/unblob count; inventory members and sizes; inventory
  root digest; truth.json archive digest; the substep-status row now ties `status: completed` to
  `operation: inventory_artifact` via `grep -A1`.
- **Route table**: the Native decompile row no longer states a cause for the `analyzeHeadless` exit
  ("because the headless launcher is not on PATH" deleted); the exit is credited to the probe
  transcript (true: `$ command -v analyzeHeadless` prints empty, `rc=1`), and the launcher path is
  credited to the doctor check via the derivation table.
- **§Q-map**: Q11 and Q16 rows restated for the new table, including the deriv_check instrument.
- **SOURCES**: S507's description cell drops "exit 1" as a record fact ("observed in the L1 session
  and is not a line of the record" — accurate: this seat counts 0 exit/rc lines in the doctor
  record). Side change: S505's `used-by` cell now points to `corpus/lessons/round-97.md`; S505 is
  not cited by this entry (census below), so it is outside this audit's object.

## 2. deriv_check run by this seat, both directions

- Amended entry: `python3 -B reports/round-99/controls/deriv_check.py --entry
  corpus/knowledge/round-98-rea-host-readiness.md --root .` → all 29 rows print `MATCH`;
  `DERIV_ROWS=29 DERIV_MISMATCH=0`, rc 0.
- Pre-amendment bytes (`git show 7e6edd4…:corpus/knowledge/…` to scratch):
  `DERIV_ROWS=21 DERIV_MISMATCH=7`, rc 1. The seven include exactly the `scope-check classes` row
  this seat flagged (got `10 classification: config_drift`…, want `10 config_drift`…), plus the
  split count row, flattened registration states, uniq -c padding, and the three digest rows whose
  stdout carries paths. The instrument demonstrably detects the defect class it is credited with.

## 3. Per-criterion evidence (command → observed output → decision)

Carry-over facts re-verified on the amended bytes; amendment-specific evidence marked (B).

**Q01 — PASS.** SOURCES field dump re-run: S506 `docs`/tier A/opened 2026-11-05, S507
`own-work`/tier A/opened 2026-11-05, both used-by this entry. `S506.receipt.json`: `verified`, http
200, fetched_at 2026-11-05, `ce2d122b…e50`, length 16650; the three quoted sentences and both
remedy-row anchors still `grep -cF` = 1 each in the committed body; r99 re-open receipt
`cmp=identical`. (B) The S507 cell now credits the doctor exit code to the session — consistent with
0 exit/rc lines counted in the record, so the registry row is now more accurate than at the freeze.

**Q02 — PASS.** Header grep prints the same six lines (1–6): two `source:`, `verified-at:
2026-11-05`, `recheck:`, `coverage-map: C14`, `admission-status: candidate`. README C14 row at line
61 (untouched, `partial`). S507 anchor byte-exact: `head -c 41` = `healthy:
false\nenvironment_healthy: false`.

**Q03 — PASS.** truth.json prints `archive_sha256 857989f5…e27e`, members 16160/84, root size 2964.
(B) The equality is now carried in-entry by three MATCHing rows: `inventory root digest`
(`root_sha256: 857989f5…`), `truth.json archive digest` (`"archive_sha256": "857989f5…"`), and
`inventory members and sizes` (`. 2964` / `README.txt 84` / `bin/checksum 16160`). Expectations
still originate in the round-2 fixture premise, not the record under test.

**Q04 — PASS.** Record lines 10–11: `id: rea-artifact-graph` / `name: REA safe artifact graph
provider`. (B) The CLI-version command now strips leading spaces and MATCHes at
`cli_package_version: 6.7.0`. `12.1.4`: 0 hits in the transcript, 17 in the doctor record; scored
from the doctor row, labelled configuration. Transcript version blocks unchanged (`rea --version`
6.7.0, `jadx --version` 1.5.6, both rc=0).

**Q05 — PASS.** ZIP row remains the only capability row: command, date, Evidence ID
(`ev_0ef6c8cd…87382`, MATCH), expected values fixed before the run. (B) The `analyzeHeadless` cause
clause is gone; the exit is credited to the transcript, which prints `rc=1` for it, and the launcher
path row MATCHes at `detail: /home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC/support/analyzeHeadless` —
genuinely under the Ghidra install directory. Doctor/inspect exit codes stay credited to the session
(0 exit lines in both records — doctor rechecked this pass, inspect previously).

**Q06 — PASS.** `sha256sum corpus/fixtures/archive-r2/fixture.zip` prints
`857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e` = truth.json `archive_sha256`;
(B) both digests now derived in-table. `git log --oneline -1 -- corpus/fixtures/archive-r2/fixture.zip`
still prints `5c9fb20 revenger r2`.

**Q07 — n/a.** Prediction scan on the amended bytes (`grep -inE 'predict|hypothes|we expect|caused
by'`) matches only the §Q-map row (now line 138). The removed cause clause was the only
cause-shaped sentence. See Q07 in corpus/QUALITY.md.

**Q08 — n/a.** QUALITY.md Q11 row: "Supersedes Q08."; Q11 re-applied in full (below). See Q08.

**Q09 — PASS.** Digest rows all MATCH: record digests `94eaa6ff…`/`fb9a4824…`/`c373f656…` (via the
new awk form), S506 body `ce2d122b…e50` and `16650`. Scope section still disclaims authenticity and
origin. Entry carries 64-hex digests, so Q09 applies and passes.

**Q10 — PASS.** (B) New `host identity` row MATCHes at `Linux 7.2.11-arch1-1 x86_64` from the
transcript header, agreeing with this seat's `uname -sr` / `uname -m`. Scope: one host, one date,
REA 6.7.0; per-shell PATH per S506; unprobed routes labelled; absent engines recorded absent.

**Q11 — PASS.** (B) Every count, identifier, digest, path and doctor-printed version in the scope
paragraph, route table and observation now has a derivation row, and this seat's deriv_check run
reports `DERIV_ROWS=29 DERIV_MISMATCH=0`, rc 0. Spot re-checks: client count 14; state split 4/1/8/1
(command strips padding); missing-or-stale 9; ghidra-named 8 and healthy 8 (denominator now
derived); skill identity stale; binwalk/unblob 0; installation paths 3 (raw `paths[3]:` line carries
exactly three comma-separated paths); installation state `state: multiple`.

**Q12 — n/a.** S-id census on the amended bytes: only `S506` (18) and `S507` (5); neither rejected.
See Q12.

**Q13 — n/a.** (B) The §Q-map now credits `deriv_check.py` with re-running every row and comparing
it with its output cell, and with reporting 0 mismatches. This seat verified both claims directly
(0 mismatches amended; 7 on the pre-amendment bytes), so the credit is bounded to exactly what the
run detects — no unbounded deletion-guard claim, and the recheck header still names re-derivation
targets only. The criterion's reject condition (a verifier credited as guarding a value whose check
survives deletion) is not met; with the credit bounded and demonstrated, no FAIL either way. See Q13.

**Q14 — n/a.** No clause pairs a hex run with a byte count; the record-digest row keeps 8-hex
ellipsis prefixes with file names and carries no length; own lint run prints `LINT_Q14=0`. See Q14.

**Q15 — n/a.** The only commit token remains the upstream REA pin
`12f6e0974cc0db0b3a9b86246accc76556837222` inside the S506 URL; no lane-tree identity sentence; own
lint run prints `LINT_Q15=0`. See Q15.

**Q16 — PASS.** (B) The pre-amendment defect is fixed at the source: the scope-check-classes command
now strips the prefix (`sed 's/^classification: //'`) and padding (`sed 's/^ *//'`), and every cell
is verbatim stdout under the stated rule — `DERIV_ROWS=29 DERIV_MISMATCH=0` on the amended bytes vs
`DERIV_MISMATCH=7` on the freeze bytes, both runs by this seat. Em-dash annotations are accurate
("grep exits 1 on zero matches" — observed; "the record prints the three comma-separated paths on
one line" — observed on the raw `paths[3]:` line). Version attribution unchanged and correct;
"Doctor has no binwalk or unblob check" still true of the record bytes (0 hits) and now derived by
row.

**Q17 — n/a.** No adjudication relocated a cited artifact. `test -f` resolves the three round-98
records, fixture.zip, truth.json, S506 body, fetch log, the 2026-10-12 checklist and the round-96
session. (The amendment's S505 `used-by` retarget concerns a row this entry does not cite.) See Q17.

### Transcript and record spot-checks (carry-over)

13 `$` blocks / 13 `rc=` lines, pairing `pending=0 bad=0`; `python3 -c 'import pwn'` rc=0;
`command -v hopper`/`idat64`/`analyzeHeadless` rc=1; doctor record has 0 exit/rc lines; inspect
record provider id `rea-artifact-graph`. Lint (own run, amended bytes): `LINT_QMAP=0 LINT_Q14=0
LINT_Q15=0 LINT_HEADER=0`, rc 0.

## 4. Decisions

| Q | decision | change vs previous vote |
|---|---|---|
| Q01 | PASS | same |
| Q02 | PASS | same |
| Q03 | PASS | same |
| Q04 | PASS | same |
| Q05 | PASS | same |
| Q06 | PASS | same |
| Q07 | n/a | same |
| Q08 | n/a | same |
| Q09 | PASS | same |
| Q10 | PASS | same |
| Q11 | PASS | same |
| Q12 | n/a | same |
| Q13 | n/a | same, with the new deriv_check credit examined and found bounded |
| Q14 | n/a | same |
| Q15 | n/a | same |
| Q16 | PASS | was FAIL — fixed by Amendment B and verified by this seat's own deriv_check runs |
| Q17 | n/a | same |

## 5. Agreement with the entry's §Q-map

17 of 17 decisions agree on digest `246d09a8…`.

## 6. Not run by this seat

No counter (v7 or v8) on any tree; no landing tree; no edits outside this seat's write scope; no
peer messages. The superseded audit `gate-audit-36cc6ac2.md` and the superseded vote remain in place
as evidence under `.ufo/waves/round-99/w1/` and `superseded-votes-digest-36cc6ac2/`.
