FALSIFIED — `C7_MUTANT_KILLED_ATTRIBUTED` is structurally 0/1: the attributed-marker `require` in `check_embedded_outputs.py` is unreachable dead code; the frozen mutant is killed (exit 1) by the earlier "drifted entry not caught" `require`, so the counter's `last` never ends with `drifted entry output accepted`. The C2 frozen predicate (claims.md:87–90) and `HOLDS_OK_V5` can never be satisfied by the landed gate bytes.

Scope: C2 claim semantics (corpus/check_embedded_outputs.py + C7 block of reports/round-67/measure.py). Every C7 conjunct except the attributed count verifies green; the defect is the ordering of two `require` calls in the gate's `_self_test`.

## Counterexample (the frozen mutant itself)

Counter: `measure.py:366–373` — `C7_CLAUSE = re.compile(r"problems \+= drift\(lines, stdout_set, lineno\)")`, `count=1` substitution → `problems += []  # mutant: verbatim comparison removed`. Gate site: `check_embedded_outputs.py:101`.

Replicated exactly (copy of `corpus/`, identical regex sub, `python3 -B corpus/check_embedded_outputs.py --self-test`, cwd = scratch tree):

- Unmutated (control): `SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired`, `BASE_EXIT=0`.
- Mutated: `self-test: drifted entry not caught`, `MUT_EXIT=1`.

`run()` (`measure.py:127–131`) returns `last = tail[-1]` of `stdout+stderr` ⇒ `last = "self-test: drifted entry not caught"`. Attribution (`measure.py:408`) requires `rc != 0 and last.endswith(C7_MARKER)` ⇒ `c7_mut_attributed += 0`. Predicted counter labels at any committed tip carrying these gate bytes: `C7_MUTANT_KILLED=1/1` but `C7_MUTANT_KILLED_ATTRIBUTED=0/1` ⇒ `c7_targets` false (`measure.py:452–453`) ⇒ `HOLDS_OK_V5=no` and predicate conjunct `C7_MUTANT_KILLED_ATTRIBUTED=1/1` failed. C2 FALSIFIED; the void condition "attributed calibration counts below target (C7 1/1)" (claims.md:129–131) is met at after-measurement.

## Mechanism — marker `require` is dead code under every input

`check_embedded_outputs.py:131–141` executes in order:

```
131  dproblems, dchecked = evaluate(drifted_entry, tmp)
132  require(dproblems is not None and dchecked == 1 and dproblems
133          and dproblems[0].startswith("drift entry:"),
134          "self-test: drifted entry not caught")      # exits 1 here for any empty/None dproblems
…
141  require(not ok(dproblems), MARKER)                # "drifted entry output accepted"
```

Direct inspection under the mutant (`evaluate()` on the same drifted entry): `dproblems = []`, `checked = 1` ⇒ line-132 condition `False` → `sys.exit(1)` printing the non-marker line; the marker `require` at :141 is never reached. It is unreachable unconditionally: if `dproblems` passes :132 it is a non-empty `drift entry:` list ⇒ `not ok(dproblems)` is `True` ⇒ :141 passes; if `dproblems` is empty/None, :132 exits first. The single literal `MARKER` print exists nowhere else (grep: only `MARKER = "…"` at gate:32 and doc strings); nothing in the file can ever end a failing run's last line with `drifted entry output accepted`. Also note the claims text (:86) paraphrases the control as `require(not ok(drift_case), '…')` — the landed code evaluates `dproblems` from the drifted entry, which is that variable; the defect is purely ordering, not naming.

## Attack angles, dispositioned

1. **Do-nothing control** — CONFIRMED unreachable for prose/builds without the file. All C7 labels gated on `c7_present = (TREE/"corpus"/"check_embedded_outputs.py").is_file()` (`measure.py:376–377`); else-branch prints `no`/`n/a`/`0` (`measure.py:419–425`). Receipt `measure-before.log:65–71,88`: `C7_GATE_PRESENT=no`, `C7_SELFTEST=n/a`, `C7_RED_ON_R65_CANDIDATE=no`, `C7_V2_CLEAN=n/a`, `C7_CONTROL_PASS=0/1`, `C7_MUTANT_KILLED=0/1`, `C7_MUTANT_KILLED_ATTRIBUTED=0/1`, `HOLDS_OK_V5=no`, probe exit 0.
2. **Mutant clause uniqueness** — CONFIRMED. `grep` over the lane: the clause pattern occurs once, at `check_embedded_outputs.py:101` (the `measure.py:366` occurrence is the counter's own regex literal, not a second call site). `mutate_c7` (`measure.py:369–373`) refuses on `len(hits) != 1`; in-tree `findall` = 1 ⇒ mutant applies, `evaluable` stays `True`.
3. **Marker attribution gameability** — CONFIRMED closed, and doubly so by accident: unmutated `--self-test` exits 0 with `SELFTEST OK:…` last line (no marker); every failing self-test path exits at a `require` whose message is never `MARKER` because the marker `require` is dead. `require` (`gate:35–38`) does `print(msg); sys.exit(1)` — the marker cannot print while exiting 0. But this "closedness" is exactly the defect: attribution is impossible for *any* mutant, including the frozen one.
4. **`verify_*` placement / HOLD_REPLAY** — CONFIRMED preserved. Replay set `sorted((TREE/"corpus").glob("verify_*.py"))` (`measure.py:427`); `check_embedded_outputs.py` does not match; `HOLD_REPLAY=10/10` and `HOLD_CALIBRATION=4/4` stand in `measure-before.log:72–83`.
5. **Counter substitution (M34)** — CONFIRMED no flip from prose alone. `C7_GATE_PRESENT` is `is_file()` on the counter-hardcoded rel path; absent the gate file every C7 label is forced to `no`/`n/a`/`0`. (A *sham gate file* could flip the labels, but that is the generic "attacker commits anything" model every C2–C6 criterion already shares, not a new C7-specific hole; the registered SKILL.md verdict-map row plus this wave's mutant review is the intended mitigation.)

## Impacted axes

- **C2 frozen predicate**: `C7_MUTANT_KILLED_ATTRIBUTED=1/1` unsatisfiable ⇒ C2 FALSIFIED at after-measurement regardless of everything else.
- **Void**: "attributed calibration counts below target (C7 1/1)" (claims.md:130).
- **C1**: untouched (separable per claims.md:72 — C2 adds one file, no existing byte).
- **Design note**: the mutation kills `problems += drift(…)`; a sham mutation at `drift()`'s definition (e.g., `return []`) would likewise exit at :132 un-attributed — the attribution channel is dead for the whole class, not just this mutant.

## Smallest safe correction (gate file only; counter stays pinned)

Move the attributed marker `require` *before* the detailed drifted-entry `require` in `_self_test`, keeping the none-safety in the detailed one:

```python
    dproblems, dchecked = evaluate(drifted_entry, tmp)
    require(dproblems is not None and not ok(dproblems), MARKER)      # attributed kill channel
    require(dchecked == 1 and dproblems and dproblems[0].startswith("drift entry:"),
            "self-test: drifted entry not caught")
```

Under the frozen mutant: `dproblems == []` ⇒ first `require` fails → last line = `drifted entry output accepted`, exit 1 ⇒ `C7_MUTANT_KILLED_ATTRIBUTED=1/1`. Unmutated control unchanged (non-empty `dproblems` ⇒ `not ok` True ⇒ passes to the detailed check). This is a one-statement reorder + conjunct swap inside `check_embedded_outputs.py` — the only byte-level fix available; the frozen counter's regex and label formulas need no change.

## Evidence hashes / pointers

- `reports/round-67/measure.py` sha256 `7933c060db4d9b8db889830e2e0b6e1da1724d94854201aac9552e2a49cbc07e` (matches pin, measure-before.log:90).
- `corpus/check_embedded_outputs.py` sha256 `19007bebeb4d60dafd826df108584933ebb3f2b1e6ab112925ea6c6cab3e697d`.
- `--entry` sanity on scratch copy: r65 candidate → `drift entry:41 … 4d616e696673742d…` `checked_blocks=15 problems=1` exit 1 (red path works); v2 → `checked_blocks=16 problems=0` exit 0 (clean path works). The gate *functions*; only its attribution marker is dead.
- Mutant/self-test runs replicated in `/tmp` scratch on byte-copies of `corpus/`; lane tree untouched.

Report: .ufo/waves/round-67/R67CriticC7Claim.md
