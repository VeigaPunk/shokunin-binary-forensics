# ReviewerProbeAudit — round-61 counting probe (read-only audit)

Subject: `reports/round-61/measure.py` @ e0a4b0c (sha256 7879ec49…; live copy identical), `claims.md`, `measure-before.log`, corpus @ e0a4b0c. Corpus e0a4 == cf02419 (`git diff --stat cf02419 e0a4 -- corpus` empty), so the before log applies to e0a4.
Commands: `git -C <lane> archive --format=tar e0a4… corpus reports/round-61 SCORECARD.md | tar -x -C <scratch>/e0a4`, then `python3 -B <scratch>/e0a4/reports/round-61/measure.py <scratch>/e0a4`.
Scratch only: `/tmp/revenger-r61-ReviewerProbeAudit-scratch/{e0a4,cf02,crash-tree,cne-tree,prefix-tree}`. Files written: this report only. Disclosed: `git diff --stat` on the live lane may refresh the `.git/index` stat cache; no content change. Installs: none (python3 3.14.8, git 2.56.0 used as found).

## 1. Before-log confirmation (observed)
- Probe on e0a4 corpus: rc 0, stderr empty; stdout lines 2–25 equal `measure-before.log:2–25` (programmatic equality: True); log line 26 `probe_exit=0`. cf02419 tree: identical output.
- Corpus digest (466 files) before == after. Verifiers contain no write/open/mkdir/unlink/subprocess calls (grep), so the HOLD runs in TREE do not write.
- `/tmp/rev-r61-mut-*` leftovers after 5 runs: 0. Census `revenger ok …/SOURCES.md`, rc 0 (= log :29–30).

## 2. Audit answers
- Exact deletion at base: YES in both files. icon removes `and receipt['command']==f'npx…json'` (verify_icon_languages.py:145), leaving line 144 ending `H(raw_bytes),f'r{r}: receipt')`. multi removes `receipt['command']==command and ` (verify_multi_icon_states.py:143). Both mutants compile; clause hits = 1 each.
- could-not-evaluate: returns None for 0 or 2+ hits and for a sole conjunct (E3). Real run on a 2-hit tree: rc 2, but summary `C2_RECEIPT_B_KILLED=0/2` (D3).
- cwd='/': mutants and controls pass at '/' (2/2); HOLD at TREE 10/10; verifiers resolve paths from `__file__`; TREE is `.resolve()`d (measure.py:18). No cwd dependence observed.
- Temp cleanup: `TemporaryDirectory` context (measure.py:59) cleans up. The caller tree `/tmp/revenger-r61-before` is never removed (D9).
- killed = nonzero exit: NO, crashes count as kills (D1).
- K vs SCORECARD.md:133: identical on LF UTF-8 (base 4=4, rows 14=14; label flip 5=5). Diverges on CRLF and line separators (D8). Both count status labels, not entries (D5).

## 3. Defects
D1 HIGH — kill = any nonzero exit: measure.py:76, :81, :83; pre-registered at claims.md:56–57. Not triggered at base (0/2 is correct today).
- Crash tree (SyntaxError appended to icon verifier): control `exit=1 killed`, b `exit=1 killed`; `C2_CONTROLS_PASS=1/2`, `C2_RECEIPT_B_KILLED=1/2`, `HOLD_CALIBRATION=3/4`, probe rc 0.
- Prefix tree (icon conjunct renamed `receipt['command']==command_expected`, no receipt control added): `b exit=1 killed :: SyntaxError: invalid syntax. Perhaps you forgot a comma?` gives `C2_RECEIPT_B_KILLED=1/2`, while `C2_CONTROLS_PASS=2/2`, `C2_D2_KILLED=2/2`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`. Every hold is green; the credit is not receipt identity.
- [INFERENCE] The after-run would be credited with collateral failures unless fixed. Fix: compile() the mutant (else could-not-evaluate); killed only if exit==1 AND last line equals the control's own message; amend claims.md before the after-run, with a dated note.
D2 MEDIUM — no identifier boundary: CLAUSE (measure.py:33) matches the prefix of `command_expected`. Synthetic `require(A and receipt['command']==command_ok)` becomes `require(A_ok)`, which compiles and fails at runtime (a kill). Closed by D1's message check; fix the regex too: `command\b`, and remove the BoolOp operand via ast.
D3 MEDIUM — could-not-evaluate printed as a number: measure.py:66–67, :85. Cne tree (second clause text in a comment): `MUTANT verify_multi_icon_states.py b could-not-evaluate`, `C2_RECEIPT_B_KILLED=0/2` (identical to "survived"), rc 2. Fix: print `=could-not-evaluate`.
D4 MEDIUM — exit 0 with failed holds: measure.py:100. Crash tree: holds 1/2, 3/4, 9/10 and rc 0. The void rule (claims.md:60–62) is not encoded. Fix: nonzero exit unless the four holds pass.
D5 MEDIUM — K counts status labels, not entries: measure.py:25–26. SCORECARD.md:133 has the same regex, while SCORECARD.md:139 says "held by gated, sourced entries". Flipping C04 to held with no entry gives `K_HELD=5/14 score=3.6` (grep 5). Base is sound: held rows C01/C11/C12/C13 (README:27,37,38,39) cite existing entries with source/verified-at/recheck/coverage-map headers (knowledge files, lines 1–7). Fix: print `K_ENTRY_BACKED=n/14`.
D6 MEDIUM — claimed holds not measured: claims.md:52 (byte-identical records) and :62 (`git diff <base> <after> -- corpus/live corpus/fixtures` empty). The probe takes one TREE and prints neither. Fix: `--base TREE`, print `SAVED_DIFF=0`.
D7 LOW — measure.py:76 labels a failing control `killed` (crash tree).
D8 LOW — K parity breaks on non-LF input: measure.py:23 (universal newlines), :24 (splitlines). CRLF: probe 4/14, grep 0 held. U+2028 in a held C04: probe 4/14, grep 5 (row dropped). U+2028 in C04 surface: `K_ROW C04 status=C04`. Trailing-space held row: K_ROW reports `held`, K_HELD excludes it. Base has 0 CR and 0 separator chars: latent.
D9 LOW — fixed caller path: measure-before.log:1 uses `/tmp/revenger-r61-before` with `tar -x` overlay, never cleaned. Currently identical to cf02 corpus (`diff -rq` 0). Use mktemp.

## 4. Verified OK / notes
- Deletion is exact for both files; `A and C or B` → `A or B` is the intended semantics.
- `--self-test` gates a negative branch in six verifiers (sys.argv, e.g. verify_pe_resources.py:60); the two C2 targets ignore it, so self-test == plain for them.
- Hold set matches SCORECARD C (names: SCORECARD.md:39 == measure.py:92–93; 10 verifiers).
- Post-change: the in-script control must route through the same conjunct (refactor check to take a receipt). A duplicated expression leaves b surviving (0/2), which the probe would show.

VERDICT: the probe reproduces the before log and deletes the intended conjunct, but kill = any nonzero exit and exit 0 on failed holds let collateral failures count as calibration; fix D1, D4, D6 before the C2 after-run and D5 before C1 admission.
INSTALLS: none.
