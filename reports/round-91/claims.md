# Round 91 — frozen claims (revenger, hyaku run 15, attempt 1)

Frozen before any build or scoring seat ran. Base = lane branch tip at freeze
(`jj-lane.sh state` → `local=`; see `freeze-base.txt`). Nothing in this file
changes after the freeze; a miss is an honest stop, never a narrowed target.

Two claims, distinct axes. Coverage — the lowest non-retired axis (K 8/15 =
5.3; C05 uncovered, C10 partial, C15 uncovered) — carries **no claim** this
round; it is routed on documented unreachability with fresh receipts
(`SCORECARD.md` round-91 row, `reports/round-91/holds.log`) and a named next
move. Reason, fixed here: K's denominator moves only by admitting a
`corpus/knowledge/` entry through the Q01–Q17 gate with per-source openings
(C10 cites 14 sources, C15 cites 50); C05's last six candidates were rejected
and its r90 record's counter is itself the routed defect (spot-check item 1,
reachable without a producer run); new map rows are operator-blocked (L0 r74).

## C1 — calibration: the self-assessment gate reads the K statement where the lane states it

**Claim type:** axis move (calibration). **Target axis:** calibration.

**What moves.** `corpus/self_assessment_check3.py` supersedes
`corpus/self_assessment_check2.py` (whose bytes stay unchanged): SM6 must read
the **stated before→after cell** of the lane's own SCORECARD row — the cell the
lane writes its numbers in — instead of the last token-adjacent `N/D` anywhere
on the line. Round 90's critic showed v2 reads the evidence-pointer cell in the
lane's real row format (`c1-realformat-counterexample.log`), so v2 both
false-flags a true row and passes a false one.

**Frozen rule (v3), stated once:**
1. Take the **last** SCORECARD line containing `K_HELD_BACKED`.
2. If that line is a `|`-delimited table row with at least 5 cells, the
   **stated region** is cell index 2 (the cell the lane writes its before→after
   numbers in); otherwise the whole line.
3. Truncate the stated region at the first `K_HELD_BACKED_STRICT` (a different
   metric).
4. If the region contains `K_HELD_BACKED`, read the **first** `N/D` group that
   immediately follows the token (skipping non-digits, an optional parenthesised
   score such as `(5.3)`, and taking the right side of `→`/`->` when the group
   carries one). Otherwise read the **last** `N/D` group in the region under the
   same right-side preference.
5. If neither yields a group, SM6 = 1: the row does not state the quantity it is
   judged on.
6. SM6 = 0 iff N = README rows whose status is `held` and D = README
   coverage-map rows (`^\| C<n> `).

**Counter (frozen):**
`python3 -B reports/round-91/c1_counter.py --impl <checker.py> --real <TREE> --lane <LANE>`
prints `SM6_MISCLASS=n/22` over the frozen battery
`reports/round-91/sm6_battery_v3.py` (N = 21 cases: 12 bare-line cases
retained from round 90 B01–B12, 9 real-format table-row cases R01–R09 whose
text is the lane's own row shape), `MUTANT <id> killed=yes|no` for the 11
frozen rule mutants in `reports/round-91/mutants.py`, `MUTANTS_KILLED=k/11`,
the impl's `--self-test` exit, and `REAL_SELF_MISMATCH=<n>` from a full run over
`<TREE>`.

**Predicate (frozen):** `SM6_MISCLASS=0/22` (21 labelled battery cases + the real-tree leg) **and** `MUTANTS_KILLED=11/11`
**and** impl `--self-test` exit 0 **and** `REAL_SELF_MISMATCH=0`. One counter,
one command, exit 0 iff all four hold.

**Before → after.** before = `corpus/self_assessment_check2.py` as `--impl`
(measured red: `SM6_MISCLASS=5/22`, all five in real-format cases R03–R06 and
R08; `reports/round-91/c1-red-v2.log`, exit 1); v1 red: `11/22`
(`c1-red-v1.log`). after = `corpus/self_assessment_check3.py` as `--impl`.

**Kill rule.** Any nonzero battery mismatch, any surviving mutant, a failing
self-test, or a nonzero real-tree mismatch ⇒ **not verified**, reported as such.

**Do-nothing control (must fail).** The cheapest control that skips the claimed
work is v2 itself: it is the current gate, and the same frozen command scores it
`MISCLASS>0` (real-format cases R03/R04/R05/R06). A control that meets the
target means the battery or target is wrong; then no data is collected.
Second control: `corpus/self_assessment_check.py` (v1) over the same battery.

**Separability.** C1 verifies with no `message_tree_check.py` on disk and no
`SKILL.md` edit; nothing in C2 is read by the C1 counter.

**Measured axis value.** `SM6_MISCLASS` is a count of mismatches between the
lane's self-assessment statement and observed repo state — calibration's own
signal (the round-90 spot-check admitted exactly this quantity as calibration).
Axis verdict recorded per the frozen counter; the r90 contested-label caveat
(gate fidelity vs assessment accuracy) is disclosed, not hidden.

## C2 — operability (capability acquisition): commit-message ↔ tree conformance is measurable over the lane's own history

**Claim type:** capability acquisition (enters the `capabilities:` table this
round on a demonstrated run). **Target axis:** operability.
**Grounded in** `considerthese/2026-11-04.md` proposal 4 (mined, not edited) and
the lane's recurring commit-hygiene class (seven of nine rounds r80–r88 landed a
commit whose message cites paths its tree does not carry).

**What moves.** `reports/round-91/message_tree_check.py` does not exist at base.
After: it reads a commit range in a git repo, extracts every backticked
repo-relative path and every `.log` filename cited in each commit message, and
checks each against that commit's own tree (`git cat-file -e <c>:<path>`;
bare filenames resolve by suffix match and are reported as `bare`). It prints
per commit `COMMIT <hash> cited=<n> misses=<k> [missing=<path>,…]` and the
summary `MESSAGE_TREE commits=<N> cited=<M> misses=<K>`; exit 0 iff K = 0,
1 if K > 0, 2 on usage error.

**Counter (frozen):**
`python3 -B reports/round-91/cap_probe.py --lane <LANE> --range <A>..<B>` — four
legs, all required:
1. the instrument exists;
2. `--selftest` exits 0 and prints `MSG_TREE_SELFTEST=pass` (its own fixture
   repo: a clean commit, a planted missing-path commit, and a `.log` leg);
3. **planted-miss kill** — the probe builds its own throwaway repo (mktemp under
   `$HYAKU_SCRATCH`/`TMPDIR`, `git -C "$D"` named on every call) with one commit
   citing an existing path and one citing `missing/r91.txt`; the instrument must
   exit 1 on the two-commit range and name `missing/r91.txt`, and exit 0 on the
   clean single-commit range;
4. a real run over the declared lane range printing
   `MESSAGE_TREE commits=N cited=M misses=K` with N ≥ 20 and M ≥ 20.
Prints `CAP_PRESENT=`, `CAP_SELFTEST=`, `CAP_PLANTED_MISS=`, `CAP_REAL=`, and
`CAP_MESSAGE_TREE=pass|fail`; exit 0 iff pass.

**Predicate (frozen):** `CAP_MESSAGE_TREE=pass`, exit 0. Declared lane range for the receipt: `7fab03f..refs/heads/main` (21 commits at the freeze).

**Before → after.** before = instrument absent (`CAP_PRESENT=0`,
`CAP_MESSAGE_TREE=fail`, exit 1; `reports/round-91/c2-red-absent.log`); after = `CAP_MESSAGE_TREE=pass`, exit 0. Declared lane range for the receipt: `7fab03f..refs/heads/main` (21 commits at the freeze).

**Kill rule.** An absent instrument, a self-test that does not print the pass
line, a planted miss that is not caught (or a clean range that is flagged), or a
real range under 20 commits ⇒ **not verified**.

**Do-nothing control (must fail).** The cheapest skip is a stub file that prints
`MSG_TREE_SELFTEST=pass` and a plausible summary line: leg 3 kills it (the stub
does not catch `missing/r91.txt`, so the probe's planted-miss leg fails). An
empty file fails legs 2–4. A target reachable by a stub means the probe is
wrong; then no data is collected.

**Separability.** C2 verifies with `self_assessment_check3.py` absent; the C1
counter never reads `message_tree_check.py`.

## Frozen artefacts at the freeze commit

- `reports/round-91/sm6_battery_v3.py` — 21 labelled cases (labels written by
  hand from the frozen rule before any implementation existed).
- `reports/round-91/mutants.py` — 11 rule mutants, each with the case that must
  kill it (declared in the module docstring).
- `reports/round-91/c1_counter.py`, `reports/round-91/cap_probe.py` — the two
  counters above.
- Red-before receipts: `reports/round-91/c1-red-v2.log`,
  `reports/round-91/c1-red-v1.log`, `reports/round-91/c2-red-absent.log`.

## Round shape (fixed here)

One v1 wave, 12 seats (`ufo-wave-policy.json`, band 8–16), ≥25 % attack:
executor ×4 (v3 impl, rule-mutant battery cross-check, message-tree instrument,
real-range receipt), scribe ×2 (SOURCES rows + SKILL/QUALITY prose; lesson),
scout ×1 (per-surface recon), connector ×1 (sibling-overlap scan), reviewer ×1,
critic ×1, mutation-tester ×1, sentinel ×1 = 4 attack seats (33 %). The L1 holds
the canonical planner seat; no planner seat is dispatched (validator rejects it).
