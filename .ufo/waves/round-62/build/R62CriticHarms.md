RESULT: COMPLETE

# R62CriticHarms — attack on frozen holds (claims.md:53-61), revision a3498e25ad87bf756288812d0ea7c474b09433c7

Scope: harms/holds only. No claim, no admission, README untouched. Nothing from the tree was executed
(no verifier, measure.py mutant run, fixture JS or bytecode); only git/sha256/stdlib regex readouts on
scratch extractions `/fast/scratch/hyaku/revenger-r62/R62CriticHarms/work/{base5bd,frozen,neg}`.

## Frozen state (all holds intact at freeze)
- `git diff --name-status 5bd4a90 a3498e25` → `M LOG.md`, `A reports/round-62/claims.md`, `A reports/round-62/measure-before.log` only.
- `git diff --name-only cf024192 a3498e25 -- corpus/live corpus/fixtures | wc -l` → `0`.
- C2 code at a3498e25: `0f781c6a…8efbd` (icon_languages), `0179e93f…a176d` (multi_icon_states) = spotcheck lesson :125-128.
- `reports/round-61/measure.py` sha256 `ada7a9c97bba394f6539ce6f158ee81a8c342a42fa861d634933226bdd0b50d2` at 45faeae, 5bd4a90, a3498e25 and live worktree.
- `work/hold_check.py base5bd frozen` → every line PASS, `HOLD_CHECK ok`, exit 0 (live 345 files, fixtures 98, .ufo/waves/round-61 161, reports/round-61 4, map ids C01..C14, Q01-Q13 rows + non-row text identical, SOURCES ids unchanged).

## Counterexamples (probe output ≠ hold satisfaction)
1. **Non-target flip meets the K target.** measure.py:27-29 prints status only for C04/C09; :32-34 counts any held row.
   `work/k_blindspots.py` (measure.py:10-34 copied verbatim to `k_only.py`) on README variants:
   `C02_partial_to_held: K_HELD=5/14 … C04 status=uncovered C09 status=uncovered K_HELD_BACKED=5/14`.
   5/14 reached with both target rows uncovered; HOLDS_OK never looks at map rows. Axis: coverage (false K credit).
2. **Existence ≠ admission.** `C04_held_names_old_rejected: K_HELD=5/14 … C04 status=held … K_HELD_BACKED=5/14` —
   the round-61 rejected file satisfies `is_file()` (measure.py:33). Axis: coverage / false provenance.
3. **Lost baseline held row hides behind a gain.** `C04_held_plus_C01_lost: K_HELD=4/14 … C04 status=held`. Reported as
   "C1 falsified" rather than "harm: lost C01"; the probe cannot name which.
4. **Denominator floats.** `dup_C01_row` and `C15_held_added` → `K_HELD_BACKED=5/15 score=3.3`. Rows counted from any
   `^\| C[0-9]+ ` line (measure.py:24); 14 is never asserted. (Note: a dict-keyed status diff also misses the duplicate;
   ordered-list equality is required — my first scratch diff showed `changed=[]` for it.)
5. **HOLD_REPLAY 10/10 is not what HOLDS_OK checks.** measure.py:99,109-111: `replay == len(results)` over a glob, so
   deleting or adding a `verify_*.py` keeps `HOLDS_OK=yes` at 9/9 or 11/11. [INFERENCE from source; not executed.]
   Any new round-62 verifier would itself break the literal 10/10 hold.
6. **C2 attributed kills are outside HOLDS_OK.** measure.py:111 omits `attributed_b`; d2 kills (:91-92) count any nonzero
   exit, unattributed (base log :9,:12 last lines end `: receipt`, but the probe does not require it).
7. **Q01-Q13 can be weakened without a byte change.** QUALITY.md:4-6 makes "new rows that name the row they replace"
   the legal supersession path (Q11 already "Supersedes Q08", :23). claims.md:33-34 allows a narrow new criterion.
   A Q14 "Supersedes Q11…" leaves Q11's row byte-identical — the round-61 closure's own test (spotcheck :60-62) passes it.
8. **Preservation is invisible to the probe.** It reads only the `corpus` archive (measure-before.log:1); reports/round-61
   and `.ufo/waves/round-61` counterexamples are never compared. measure-before.log:2 runs the probe from the live
   worktree path, not the archive; its sha equals the committed blob today, but the after-log must record it.

## Red/green of the proposed check
`cd / && python3 -B work/hold_check.py work/frozen work/neg` on a copy mutated with C02 held, C04 held naming old file,
Q14 "Supersedes Q11", `verify_shape_evidence.py` removed, one `\n` appended to the old EVM file → exit 1:
```
FAIL preserved corpus/knowledge/evm-saved-interface-candidates.md (1 files)
FAIL verifier set 10 :: base=10 final=9
FAIL non-C04/C09 rows byte-identical :: C02
FAIL C04 held names only knowledge/round-62-commonjs-require-name-evidence.md :: ['knowledge/commonjs-destructured-require-edges.md']
FAIL C04 entry present and not marked rejected
FAIL added rows ['Q14'] do not supersede/exempt Q01-Q13 :: Q14
```
Same `neg` tree through the unchanged K section: `K_HELD=6/14 … K_ROW C04 status=held … K_HELD_BACKED=6/14`.
Green: `hold_check.py work/base5bd work/frozen` → `HOLD_CHECK ok`, exit 0. Python 3.14.8.

## Smallest safe correction (proposals only; scratch files, not live edits)
- Keep measure.py unchanged (claims.md:38). Add as an independent harm check, run by L1 on final vs 5bd4a90 archives:
  `/fast/scratch/hyaku/revenger-r62/R62CriticHarms/work/hold_check.py` sha256 `b590a00f79db98689f2c9312587658d83e87ee00432d76720fcb9df241192d61`.
- Read probe lines literally, not HOLDS_OK: `C2_CONTROLS_PASS=2/2`, `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2`, `C2_D2_KILLED=2/2`
  with both d2 last lines ending `: receipt`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10` (denominator 10), `HOLDS_OK=yes`,
  plus measure.py sha `ada7a9c9…50d2` in the after-log.
- `K_HELD_BACKED≥5/14` is necessary, never sufficient: C1 also needs the per-candidate Q01-Q13 Gate rows by a non-author
  seat (claims.md:41-43). hold_check deliberately judges no quality; a PASS admits nothing.
- Any Q14 must be additive only: no "supersedes/replaces/n/a/exempt" referencing Q01-Q13 (checked heuristically).
- Tradeoff, not defect: hold_check requires non-target rows byte-identical (stricter than "status"); a deliberate
  pointer edit to another row would need an explicit logged exception rather than a silent pass.
- Not auto-judged: SOURCES old-row changes are listed for the old→new log; S028-S031 are the only allowed new ids.

## Unknowns
- No final candidate state exists yet; C04/C09 audit lines show `INFO … uncovered` at frozen.
- Counterexample 5's runtime behaviour is inferred from source; verifiers were not run by this seat.

Installs: none.
