LIST — zero functions/imports are safely deletable (mutant clause + contract text freeze the oddities), but the forged-control statement at `corpus/check_embedded_outputs.py:141` is **dead code as ordered**: the frozen C7 mutant is killed one `require` earlier, so `C7_MUTANT_KILLED_ATTRIBUTED` prints `0/1`, not `1/1`. Minimal diff: reorder the drifted-case asserts so the marker require fires first.

File under review: `corpus/check_embedded_outputs.py` (169 lines, sha256 `19007bebeb4d60dafd826df108584933ebb3f2b1e6ab112925ea6c6cab3e697d`). Frozen contract: `reports/round-67/claims.md` §C2 (mutant regex at `claims.md:92`, control shape `require(not ok(drift_case), 'drifted entry output accepted')` at `claims.md:86`); counter clause `reports/round-67/measure.py:366` `re.compile(r"problems \+= drift\(lines, stdout_set, lineno\)")`, attribution test `measure.py:408` `rc != 0 and last.endswith(C7_MARKER)`, `last` = final line of `proc.stdout + proc.stderr` (`measure.py:130-131`).

## Caller surface

No `xd://lsp` device is mounted (`read xd://lsp` → "No such tool; mounted: ast_edit, debug") — semantic `references` unavailable; text grep is the fallback, recorded as such. It suffices here because the module is never imported: `grep 'import check_embedded_outputs|from check_embedded_outputs'` lane-wide → **no matches**; the only consumers run it as a subprocess — `measure.py:385,401,409,414` (`--self-test`, `--entry` ×2). Internal functions therefore have exactly the callers visible in the file.

## Verified behavior (this seat, lane root)

| command | observed | contract path |
|---|---|---|
| `--self-test` | exit 0, `SELFTEST OK: …` | pass |
| `--entry corpus/knowledge/round-65-apk-axml-byte-evidence.md` | exit 1, `drift entry:41 …`, `checked_blocks=15 problems=1` | red-before kill |
| `--entry corpus/knowledge/round-67-apk-axml-byte-evidence.md` | exit 0, `checked_blocks=16 problems=0` | C7_V2_CLEAN |
| `--entry corpus/QUALITY.md` (no `$ ` blocks) | exit 2 | could-not-evaluate |
| `--entry corpus/knowledge/round-63-zip-central-directory-evidence.md` (first block `$ git show…`) | exit 2 | unsupported command |
| `--entry /nonexistent-entry.md` | exit **1**, `FileNotFoundError` traceback | **contradicts** `:158` "or read failure" and `SKILL.md:267` verdict-map "2 … read failure" — that clause is unreachable |
| `--bogus` | exit 64 | usage path (undocumented in the 0/1/2 verdict map; distinct from evaluation verdicts — acceptable, noted) |

## Function-level dispositions (the three contracted axes)

| symbol (lines) | verdict | one-line justification |
|---|---|---|
| `require` (:35-38) | KEEP | 4 call sites (:129,:132,:136,:141); contract-shaped fail-and-print; `sys.exit(1)` (not `assert`, which `-O` strips) is what makes the marker a *printed last line* |
| `parse_blocks` (:41-65) | KEEP | sole caller `evaluate` :88; merging adds no axis gain; docstring nit — says "Yield", returns a list |
| `run_cmd` (:68-76) | KEEP | all three branches live: `not argv` (:70) guards `$ ` degenerate blocks against `IndexError` → exit 2; `argv[0] not in ("python3","python",sys.executable)` (:72) proven live (round-63 entry → exit 2); `return proc, proc.stdout, proc.returncode` (:76) — `proc` itself is only consumed via `is None` (:94), a simplifiable shape, not dead code |
| `drift` (:79-81) | KEEP — **frozen** | the single call `problems += drift(lines, stdout_set, lineno)` (:101) is the frozen mutant clause; matches exactly once (verified `re.findall` → 1); inlining or renaming breaks `mutate_c7` (match count ≠ 1 → `evaluable=False`) |
| `evaluate` (:84-103) | KEEP | every branch reached: `not blocks` → 2; `proc is None` → 2; `rc != 0` append → 1-path; `problems += drift` → frozen clause |
| `_self_test` (:106-142) | KEEP, **contains the dead control** | see below |
| `ok` (:145-146) | KEEP — contract-frozen | sole call :141; `claims.md:86` spells the control as `require(not ok(drift_case), …)`; could inline as `dproblems` but the name is contract-anchored |
| `main` (:149-165) | KEEP | all three exits observed: 0, 2, 64 |
| `MARKER` (:32) | KEEP — contract-frozen | `measure.py:388` requires the literal string in the gate text for `C7_CONTROL_PASS`; used :141 |
| imports (:25-30) | ALL USED | `json` :109+; `shlex` :69; `subprocess` :74; `sys` :38+; `tempfile` :152; `Path` :87,:152 — zero unused |

## Finding — dead code: the forged control can never print MARKER

`_self_test` order (verified against committed bytes):

```python
132  require(dproblems is not None and dchecked == 1 and dproblems
133          and dproblems[0].startswith("drift entry:"),
134          "self-test: drifted entry not caught")
…
141  require(not ok(dproblems), MARKER)
```

`not ok(p)` ≡ `bool(p)`. The point at which :141 is reached, `dproblems` is already guaranteed truthy by :132 — so `not ok(dproblems)` is always `False` and `MARKER` can never print. Every state that would fire :141 (empty/`None` `dproblems`) exits at :132 first. `:141` + the `MARKER` string there are dead as a *control* (the constant itself must stay for `measure.py:388`).

Empirical receipt — counter-identical mutant on a temp copy (`/tmp/revenger-r67-simplifier/gate-mutant.py`; substitution text equivalent to `measure.py:372`'s `problems += []  # mutant: verbatim comparison removed`):

```
subs = 1
MUTANT_EXIT=1
last line: "self-test: drifted entry not caught"
```

So under the real counter the mutant is **killed but not attributed**: `last.endswith(C7_MARKER)` at `measure.py:408` is `False` → `C7_MUTANT_KILLED_ATTRIBUTED=0/1` → the frozen C2 predicate cannot pass on these bytes. (Sibling `R67MutC7Kill` is running the counter's own mutant flow; this receipt is the same substitution with the same observed kill line.)

## Minimal diff (proposed, NOT applied — restores the control, preserves all three axes)

In `_self_test`, fire the forged control before the descriptive assert (splits :132-134 into an evaluation sanity + the marker + the format check; +1 line):

```python
    dproblems, dchecked = evaluate(drifted_entry, tmp)
    require(dproblems is not None and dchecked == 1,
            "self-test: drifted entry not evaluated")
    # In-script forged control: the drifted case MUST be caught. If the
    # verbatim comparison is removed (or weakened), this fires with the
    # attributed marker as the last output line.
    require(not ok(dproblems), MARKER)
    require(dproblems[0].startswith("drift entry:"),
            "self-test: drifted entry not caught")
```

Preserves: frozen clause at :101 byte-identical (mutant still applies, count 1); `MARKER` literal still in file (`C7_CONTROL_PASS` intact); `ok`/`require` names intact (claims.md:86 shape); all exit codes unchanged on every observed path; entry-mode verbatim check untouched. Under the mutant: `dproblems == []` → marker prints → exit 1, last line ends `drifted entry output accepted` → attributed. Side effect to weigh: an unevaluated drifted entry (None/None) now reports "not evaluated" exit 1 instead of "not caught" — a clearer self-test failure, no contract impact.

## Tradeoffs / not proposed

- `drift`'s `lineno` parameter (:79) is unused in the body — *looks* dead, but the frozen regex pins the call signature `drift(lines, stdout_set, lineno)`; deleting the parameter and updating the call would leave the frozen regex matching zero times → `evaluable=False`. Frozen, not dead.
- `run_cmd` could return `(bool_or_None, stdout, rc)` instead of the `CompletedProcess`; only `proc is None` is consumed — cosmetic churn, no axis gain.
- `evaluate` discards partial `problems` on `(None, None)` return — matches verdict map (2 = could-not-evaluate dominates 1); contract-shaped.
- `parse_blocks` "Yield" docstring vs list return; `fence` toggle treats ```` ```lang ```` as plain fences — cosmetic / accepted-surface notes, not minimality items.
- No installs or upgrades performed this seat (none needed); pacman untouched.
