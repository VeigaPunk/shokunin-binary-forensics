SIMPLER-FORM — the C7 repair is semantically correct (mutant killed *and* attributed, spoof killed *not* attributed, passing run byte-identical), but the rewritten block kept a single-use boolean plus two lines of redundant prose: 11 lines → 8, −1 name, behaviour proven identical on all four legs; `ok()` was removed correctly and nothing else in the file is dead.

seat: R68SimplifierGate (leaf, read-only) · surface: `corpus/check_embedded_outputs.py` sha256 `b89183bec2fd3b94f5b0acc828a0d3fe16f6a98dde1d7752616da85d08a8e0ca` (6791 B, 172 lines) · r67 comparison base `git show 7668510:corpus/check_embedded_outputs.py` (written only to `/tmp/r67gate.py`) · no production edits.

## Axes (godspeed)
1. **calibration** — does the repair actually make the registered marker the killing line (the C1 predicate)?
2. **dead weight** — is any name/branch now unreachable or single-use?
3. **contract surface** — is anything a *live* contract document still asserting the old defect?

## (1) Smallest correct form of the rewritten block

Landed block, `corpus/check_embedded_outputs.py:135-145` (11 lines):

```python
    dproblems, dchecked = evaluate(drifted_entry, tmp)
    # Forged control (round-68 repair of M45): the drifted case MUST be
    # caught. If the verbatim comparison is removed (or weakened) the branch
    # below is taken, and the attributed marker is the LAST output line, so
    # the kill is attributable to the marker and not to some earlier require.
    caught = (dproblems is not None and dchecked == 1 and dproblems
              and dproblems[0].startswith("drift entry:"))
    if not caught:
        print("self-test: drifted entry not caught")
        print(MARKER)
        sys.exit(1)
```

Smallest correct form (8 lines; `caught` folded, prose 4→3 lines, `dproblems is not None` dropped because `dproblems` truthiness already covers `None`):

```python
    dproblems, dchecked = evaluate(drifted_entry, tmp)
    # Forged control (r68/M45): the drifted case must be caught; if the verbatim
    # comparison is removed this prints MARKER as the LAST line, so the kill is
    # attributable to the marker and not to an earlier require.
    if not (dchecked == 1 and dproblems and dproblems[0].startswith("drift entry:")):
        print("self-test: drifted entry not caught")
        print(MARKER)
        sys.exit(1)
```

Equivalence proven, not asserted — built as `/tmp/min.py` and run on four legs:

| leg | landed file | minimal form |
|---|---|---|
| `--self-test` | rc 0, `SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired` | rc 0, stdout **byte-identical** (`cmp` clean; both `bcd32f26ad4ec7e9683b3512d305a57fc69d3419b98f72d126d1bc5925cccf1d`) |
| frozen mutant (`problems += drift(...)` → `problems += []`) | rc 1, last = `drifted entry output accepted` | rc 1, last = same |
| mutant + `MARKER` spoof | rc 1, last = `…(spoofed)` → attributed **False** | rc 1, last = `…(spoofed)` → attributed **False** |
| `--entry corpus/knowledge/round-68-apk-axml-byte-evidence.md` | `checked_blocks=17 problems=0`, rc 0 | `checked_blocks=17 problems=0`, rc 0 |

Landed-file leg transcript (`/tmp/mut.py`, `/tmp/spoof.py`, both derived from the landed bytes with the frozen clauses asserted to match exactly once):

```
=== mut rc=1 last=drifted entry output accepted      → killed True  attributed True
=== spoof rc=1 last=drifted entry output accepted (spoofed) → killed True  attributed False
```

This matches the frozen counter's rule exactly: `reports/round-68/measure.py:428` `c7_mut_attributed += rc != 0 and last.endswith(C7_MARKER)`, `:492` the same for the spoof leg, `C7_MARKER` at `:384`, spoof clause `:460`.

### What must NOT be simplified away (each proven load-bearing)

- `dchecked == 1` — **not** redundant with `dproblems`. If the declared command dies (`rc != 0`) the drift list is never consulted, `checked` stays 0, and `evaluate` returns `["drift entry:NNN command exited …"]`, which *does* start with `drift entry:`. Witness `/tmp/nodc_falsepass.py` (minimal form minus `dchecked`, plus the mutant, plus a drifted fixture whose command exits 1) prints `SELFTEST OK …` and exits **0** with the verbatim comparison removed — i.e. dropping that conjunct restores a false pass of exactly the M45 class. Keep it.
- `dproblems[0].startswith("drift entry:")` — keeps the self-test from counting a command-failure problem as a caught drift.
- `print(MARKER)` (the constant, not a literal) — this is what makes the negative control read `C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1`; a literal would pin the marker and the spoof would be unattributable-by-construction only if it were also unspoofable, so hard-coding would silently weaken the control. Also `MARKER` has exactly one assignment (`:36`) and one use (`:144`), so `C7_SPOOF_CLAUSE` (`measure.py:460`) still matches exactly once.
- `print("self-test: drifted entry not caught")` before the marker — causal diagnostic; verified it does not displace the marker from the last line.

## (2) `ok()` removal — correct, and nothing else is dead

r67 had `def ok(problems): return not problems` at `:145` with exactly one caller, `require(not ok(dproblems), MARKER)` at `:141` — the line the round-67 adjudication proved unreachable. Both the caller and the definition are gone in r68 (diff hunk `@@ -129,21 +133,20 @@` deletes the three-line caller and the four-line helper).

No reference survives: `grep -nw ok corpus/check_embedded_outputs.py` → exit 1 (no match); AST body functions are `['require','parse_blocks','run_cmd','drift','evaluate','_self_test','main']`, every one of which has a resolving `Load` reference; `reports/round-68/measure.py` contains no `ok(` call.

Nothing else became dead: all six imports are used (`json` `_self_test:118-121`, `shlex` `run_cmd:73`, `subprocess` `run_cmd:78`, `sys` `require:42`, `run_cmd:76-78`, `main:153-168`, `tempfile` `main:155`, `Path` `evaluate:91`); `require` still has two live callers (`:133`, `:147`); `drift` still has its `evaluate:105` caller; `lineno` is still consumed by the `drift` f-string (`:84-85`). The only shift is that `require` went from three callers to two — that is a use-count change for a helper that is still the file's failure idiom, not dead weight.

## (3) Passing-run public behaviour identical

- `--self-test`: rc **0**, stdout **byte-identical** to r67 (`sha256 bcd32f26…` for both `/tmp/o67.txt` and `/tmp/o68.txt`, `cmp` clean).
- `--entry` mode is untouched by the diff (changes are confined to the module docstring, the drifted block, and the `ok()` deletion); measured live on the v3 candidate: `checked_blocks=17 problems=0`, rc **0** — consistent with `C7_V3_CLEAN=yes` in the C2 predicate.
- The docstring edit (`:3-8`, `:18-20`) is provenance, not dead weight: it now states the "registered gate / marker is the last output line" fact that the code enforces.

## Finding (not mine to edit) — live contract row is now stale

`SKILL.md:268` (Gate registry, `self-test` cell) still asserts the round-67 defect as current truth: *"the trailing forged-drift control's marker `drifted entry output accepted` is structurally shadowed by that earlier require and can never fire — … recorded limitation, reorder fix routed"*. That sentence is false against the landed bytes (mutant leg: marker is the last line, above) and contradicts the gate's own docstring at `:18-20`. A registry row is a live contract document, not historical provenance, so the round that repairs the behaviour must carry the corrected cell — otherwise C1's "the registered attribution" surface still points at a row that calls itself broken. No other file regressed: the r67 lesson's shadowing statement is historical and stays.

## Tradeoff
The residual win is small (−3 lines, −1 name in a 172-line file); the value is that the minimal guard is also the one with the fewest places to reintroduce the shadowing class, and that `dchecked` and the `startswith` conjunct are now documented as load-bearing rather than looking like removable belt-and-braces. Leaving the landed form in place harms no axis; taking the 8-line form costs one no-op review.

## Bounds / tooling
Wrote only this file. Scratch copies (`/tmp/r67gate.py`, `r67run.py`, `r68run.py`, `mut.py`, `spoof.py`, `min.py`, `minmut.py`, `minspoof2.py`, `nodc.py`, `nodc_falsepass.py`, `*.out/.txt`) live outside the lane; `corpus/` hash unchanged (`b89183be…`). No installs or upgrades; no tooling changes.
