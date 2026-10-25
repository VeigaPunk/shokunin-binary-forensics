# R70W2ErratumCheck — SCORECARD round-69 errata verification

Verdict: **ERRATA-TRUE** — all three corrections in the appended "Errata to the round-69 section" (`SCORECARD.md:603-615`) verify true against source evidence.

## 1. Erratum (hash resolution) — TRUE

- `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin rev-parse e1d22ca` → `e1d22caaf9a2fdc4c1c13d1f4a8a6813e7b07968` (resolves; exit 0).
- `git -C ... rev-parse e1d22caaf9a2fdc4c1c13d1f4a8a6813e7b07968` → same full hash (resolves; exit 0).
- `git -C ... rev-parse e1d22caf` → `fatal: ambiguous argument 'e1d22caf': unknown revision or path not in the working tree.` exit 128 (fails). ✓
- Commit adds round-69 pre-registration files (`git show --stat e1d22ca…`):
  ```
  corpus/q15_tree_id_check.py           | 129 ++++++++
  reports/round-69/claims.md            | 231 ++++++++++++++
  reports/round-69/d1-false-sentence.md |  12 +
  reports/round-69/measure-before.log   | 105 +++++++
  reports/round-69/measure.py           | 577 ++++++++++++++++++++++++++
  ```
  → includes `reports/round-69/claims.md`. ✓
- Printed token on the Round-69 "Pre-registration" line (`SCORECARD.md:557`) is `` `e1d22caf` `` = 8 chars, last char `f`; real hash prefix is `e1d22ca` (8 chars, last char `a`) — matches the errata description "8-character truncation whose last character is wrong". ✓
- Also consistent: the pinned counter hash given in that same line, `bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377`, equals `sha256sum reports/round-69/measure.py` in the working tree (bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377). ✓

## 2. V3 — counter prints K_HELD_BACKED=8/14 before the NameError; exit 1 — TRUE

Setup: `D=$(mktemp -d /tmp/revenger-r70-erratumcheck-BTcR)`; `git -C <lane> archive db956eca73bf810db9bdf2c98dc843a528f5d789 corpus | tar -x -C "$D"` (EXTRACT_OK; tree contains `corpus/q15_tree_id_check.py`).

Run (absolute counter path, correct `TREE` arg per usage `measure.py TREE (TREE/corpus must exist)`):
```
$ python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-69/measure.py /tmp/revenger-r70-erratumcheck-BTcR
K_HELD=8/14 score=5.7
K_ROW C05 status=uncovered
K_ROW C07 status=held
K_HELD_BACKED=8/14
C05_REJECTED_MARKED=yes
K_HELD_BACKED_STRICT=8/14
...
Q15_PRESENT=yes
Traceback (most recent call last):
  File "/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-69/measure.py", line 158, in <module>
    rc, last = run(TREE, "q15_tree_id_check.py", "--self-test")
               ^^^
NameError: name 'run' is not defined
EXIT=1
```
- `K_HELD_BACKED=8/14` and `K_HELD_BACKED_STRICT=8/14` print **before** the traceback; only the hold block (`HOLDS_OK_V6` etc.) is unprinted. ✓
- `NameError` at `measure.py:158` (`def run` is at `:187`, matching the scorecard C2 cell), exit code 1. ✓
- This reproduces the registered receipt exactly (`reports/round-69/measure-after.log:16-44`: stdout 22 lines with `K_HELD_BACKED=8/14` at line 20 and `K_HELD_BACKED_STRICT=8/14` at line 22, then the same traceback; `counter exit code: 1`). ✓

## 3. V4 — printed relative form fails from fleet root; absolute form runs — TRUE

- Printed relative form from the fleet root `/home/vgpnk/Projects/shokunin`:
  ```
  $ cd /home/vgpnk/Projects/shokunin && python3 -B reports/round-69/measure.py /tmp/revenger-r70-erratumcheck-BTcR/corpus
  python3: can't open file '/home/vgpnk/Projects/shokunin/reports/round-69/measure.py': [Errno 2] No such file or directory
  EXIT=2
  ```
  → fails (relative path does not resolve from fleet root). ✓
- Absolute form from `/`:
  ```
  $ cd / && python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-69/measure.py /tmp/revenger-r70-erratumcheck-BTcR
  K_HELD=8/14 score=5.7
  ... (identical output, including K_HELD_BACKED=8/14 and K_HELD_BACKED_STRICT=8/14)
  NameError: name 'run' is not defined
  EXIT=1
  ```
  → runs (same behavior as V3). ✓
- The absolute form is indeed the one printed in `reports/round-69/claims.md:156-160` (`/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-69/measure.py <tree>`), and the registered run in `measure-after.log:6-8` uses `cd / && … measure.py "$T"`. ✓

## Notes / cross-checks

- Source of V3/V4: `corpus/lessons/round-69-verifier-spotcheck.md` §6 (`:135-140`) documents the same two corrections (counter printed `K_HELD_BACKED=8/14` before the `NameError` at `:158`; printed counting command does not run), corroborating the erratum.
- The exact original cell string "not printed — the counter crashes before the hold block" is not present verbatim in the current tree outside the erratum/spotcheck/w1-draft, so the quote is corroborated by the committed spotcheck §6 rather than by a surviving original cell.
- No tools installed/updated (used existing `git` and `python3`); no pacman transactions; no writes outside the report path; scratch at `/tmp/revenger-r70-erratumcheck-BTcR` deleted.

## Evidence pointer list

- `SCORECARD.md:603-615` — errata section under test
- `SCORECARD.md:557` — pre-registration token `e1d22caf` (8 chars, wrong last char)
- `git rev-parse` triple — outputs in §1
- `git show --stat e1d22caaf9a2fdc4c1c13d1f4a8a6813e7b07968` — adds `reports/round-69/claims.md` (+counter, red-before, Q15 checker)
- `reports/round-69/measure.py` sha256 `bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377` (matches pinned value in scorecard line 557 and claims.md line 6)
- `reports/round-69/measure-after.log:16-44` — registered run: `K_HELD_BACKED=8/14` / `K_HELD_BACKED_STRICT=8/14` before NameError at `:158`, exit 1
- `reports/round-69/claims.md:156-160` — absolute counter command printed in claims
- `corpus/lessons/round-69-verifier-spotcheck.md:135-140` — V3/V4 source corrections
- Archive tree: `git archive db956eca73bf810db9bdf2c98dc843a528f5d789 corpus`
