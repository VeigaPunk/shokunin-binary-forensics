# CriticCalibrationClaim — round 61, C2 (receipt-identity mutation kill), read-only
Base observed: lane HEAD `e0a4b0c` (`git log --oneline -1`). The three ExecReceiptControl{Lang,Multi,Both} clones are at e0a4b0c with an empty `git status`, so no C2 draft existed to attack. These findings target the claim (`reports/round-61/claims.md:42-62`) and the probe (`reports/round-61/measure.py`).

## Q1: calibration move or operability tautology?
- OBS: forgery discrimination on real inputs is already 2/2 at base. `measure-before.log:7,10` shows d2 (on-disk forged `command`) giving `AssertionError: r47: receipt` / `r42: receipt`, exit 1. C2 does not change the verdict on any genuine or forged artifact.
- OBS: what C2 changes is self-test adequacy against one known code mutant. Mutant b = conjunct deleted (`mutation-post.md:15,21`). The control is designed against that exact mutant, so 2/2 follows if the control is coded correctly. Only the implementation is at risk, not the property.
- INFERENCE: this is a regression guard for an existing calibration control (forgery discrimination that holds in-script), not new discrimination. It is calibration-adjacent, not a pure operability tautology. Precedent: `SCORECARD.md:81` counts isolated forgery rejection under calibration. But the new criterion is defined by the gap it closes. 0.0→10.0 on n=2 with one mutant operator is premature saturation. Impacted axis: calibration (score inflation risk), not correctness.
- INFERENCE (sibling peer MutationReceiptConjuncts is measuring this): the receipt `require` has 5 conjuncts (`verify_icon_languages.py:143-145`, `verify_multi_icon_states.py:143-144`). A command-only forgery cannot kill deletion of `exit_code`, `fixture_sha256`, `evidence_id` or `stdout_sha256`: those fields stay identical in the forged copy. So the name "receipt-identity" overstates scope; it covers 1 of 5 receipt conjuncts.

## Q2: vacuous kills / rejection for the wrong reason
1. PROBE SCORES CRASHES AS KILLS. `measure.py:81` counts `killed_b += rc != 0`, and `:51-52` keeps only the last output line. Nothing checks that the failure is the control.
2. THE MUTANT-SITE REGEX HAS NO RIGHT BOUNDARY. `measure.py:33` `(?:command|f'[^']*')` matches a prefix. I ran `mutate_b` copied verbatim on plausible refactor text (python3 stdin; no lane writes):
   `...==0 and receipt['command']==commands[r], 'r1: receipt')` → `...==0s[r], ...` | `SyntaxError: invalid decimal literal`
   `ok and receipt['command']==command_for(hist)` → `ok_for(hist)` | compiles, then NameError at run time
   `ok and receipt['command']==command.strip()` → `ok.strip()` | compiles, then AttributeError
   `ok and receipt['command']==f'npx {hist}' + ' --format json'` → `ok + ' --format json'` | compiles, then TypeError
   Each run exits 1 and is counted as "killed" even if no control exists. That gives a false 2/2.
3. COULD-NOT-EVALUATE TRAPS (exit 2, which voids the count rather than faking it):
   - Control text containing `forged_receipt['command']==command`: the regex has no left boundary, so the count is 2.
   - Renaming to `expected_command`: count 0.
   - Making the clause its own `require(receipt['command']==command, ...)`, or wrapping it in parentheses: no adjacent `and`, so the result is `CNE-noand`.
4. AMBIGUOUS REJECTION MESSAGE. All 5 conjuncts share one message, `r{r}: receipt`. Matching that message alone cannot show the command conjunct rejected the forgery. Broken forgeries would also yield `r47: receipt`: a fresh dict, a changed `stdout_sha256`, or a modified `HIST`/path that breaks `artifact` first. Soundness comes from a key-diff argument instead: the real receipt passed every conjunct earlier in the same run, and the forged copy differs only in `command`. Then the only conjunct that can flip is the command one.
5. BROAD CATCH. A control written as `except Exception`/`except AssertionError` with no message check also counts KeyError or other assertion messages as "rejected". Under b, the probe exposes this as a survivor, not a false kill. It still makes the PASS line dishonest.
6. DUPLICATE AUTHORITY. A control that re-implements the comparison (e.g. `forged['command']!=command`) tests its own copy, not the production conjunct. The validator must be the same code path that `check()` uses.

## Acceptance evidence the integrator MUST show (per file, on the after commit)
A. The probe's b line ends exactly with the control's unique message, e.g. `MUTANT verify_icon_languages.py b exit=1 killed :: AssertionError: r47: forged receipt command accepted` (and r42 for multi). Not `r47: receipt`, and not SyntaxError, NameError, TypeError, AttributeError or KeyError. Treat any other b tail as NOT killed.
B. Full stderr of one hand-run mutant b per file, in a /tmp copy with cwd=/. Its innermost traceback frame must be the control's `raise` line (`File ".../verify_X.py", line N, in main/check` with N cited in the after file).
C. Control (unmutated) line: exit 0, and the PASS text names the forged receipt command as REJECTED.
D. d2 is unchanged: exit 1 with `AssertionError: r47: receipt` / `r42: receipt`. The on-disk check fires before the control.
E. In-script asserts:
   - The forged receipt equals `copy.deepcopy(real)` with the same key set, and the differing keys are exactly `{'command'}`.
   - The forgery is applied after the real receipt passed in the same run.
   - The rejection is an `AssertionError` with `str(e)==f'r{r}: receipt'`; any other exception propagates.
F. Site shape:
   - `grep -cE "receipt\[['\"]command['\"]\]\s*==" corpus/verify_<X>.py` gives 1.
   - The matched RHS is exactly `command` or a single f-string, followed by whitespace, `,` or `)`.
   - It is adjacent to an `and` in the receipt `require`.
   - `mutate_b(text)` output passes `compile()`.
G. The holds still pass: `C2_CONTROLS_PASS=2/2`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, and `git diff <base> <after> -- corpus/live corpus/fixtures` is empty.

## Smallest safe corrections (no change to the pre-registered probe)
- Add one in-memory control per file that reuses `check`'s own receipt validation: deepcopy the real receipt, change only `command` (realistic forgery: `rea-agents@6.4.1`), require exactly `r{r}: receipt`, and raise a unique `forged receipt command accepted` message otherwise. Run it unconditionally, after `rows` are computed.
- The judge should reject a 2/2 that lacks evidence A/B, because the probe cannot tell a kill from a crash. This is a fixable evidence gap, not a tradeoff.
- Tradeoff for the canonical judge: report C2 as "receipt-command self-test adequacy, 1 operator, 1 of 5 receipt conjuncts". Do not report a calibration jump in discrimination, since d2 was 2/2 before. Residual risk that stays: deleting the control itself (exit 0) is unguarded.

VERDICT: C2 is a legitimate but narrow regression-guard move. The probe can score crash kills (regex prefix match plus rc!=0), so 2/2 is admissible only with evidence A, B, E and F.
Installs: none. Files written: this report only.
