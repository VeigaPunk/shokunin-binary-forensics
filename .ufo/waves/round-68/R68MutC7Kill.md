KILLED-ATTRIBUTED — frozen mutant `problems += []` kills the repaired gate (exit 1) with `drifted entry output accepted` as the LAST output line; unmutated control exits 0 with a different last line; scratch bytes restored to the lane sha256.

seat: `L1Revenger68.R68MutC7Kill` · round 68 · lane `/home/vgpnk/Projects/shokunin/revenger-shokunin` · 2026-10-25
assignment: the C1 kill-rule probe (frozen mutant, `reports/round-68/claims.md` §C1) — leaf, no subagents, production tree read-only.

## 1. Scratch tree (copy made before any mutation)

```
SCRATCH=$(mktemp -d /tmp/r68-c7kill-XXXXXX)      # -> /tmp/r68-c7kill-LIfsdC
cp -a /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus "$SCRATCH/corpus"
```

```
b89183bec2fd3b94f5b0acc828a0d3fe16f6a98dde1d7752616da85d08a8e0ca  /tmp/r68-c7kill-LIfsdC/corpus/check_embedded_outputs.py
b89183bec2fd3b94f5b0acc828a0d3fe16f6a98dde1d7752616da85d08a8e0ca  /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/check_embedded_outputs.py
6791 /tmp/r68-c7kill-LIfsdC/corpus/check_embedded_outputs.py
```

## 2. Unmutated control, run in the same scratch tree (before the mutation)

```
cd /tmp/r68-c7kill-LIfsdC && python3 -B corpus/check_embedded_outputs.py --self-test
EXIT=0
SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
```

stderr: 0 bytes. `last.endswith("drifted entry output accepted")` → **False**. The detector's green branch is distinct from the marker branch, so a marker-ending last line in the mutant run cannot be the control's own output.

## 3. Frozen mutant applied exactly once (single-match assertion)

```
pat = re.compile(r"problems \+= drift\(lines, stdout_set, lineno\)")
regex_matches= 1                        # asserts len == 1 before substituting
mutated_sha256= d67d9b121389e922f7a64fafb9bad08ba530691dc68ddb5759ae0d9535f5c2ba
mutated_bytes= 6800
```

`diff -u` lane↔scratch after substitution — exactly one hunk, the frozen replacement, nothing else:

```
@@ -102,7 +102,7 @@
             problems.append(f"drift entry:{lineno} command exited {rc}: {cmd}")
             continue
         stdout_set = set(stdout.splitlines())
-        problems += drift(lines, stdout_set, lineno)
+        problems += []  # mutant: verbatim comparison removed
         checked += 1
     return problems, checked
```

This is byte-for-byte the counter's own `C7_CLAUSE` / `mutate_c7` protocol
(`reports/round-68/measure.py:386-393`, counter sha256 `0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766`), applied by hand to the copy rather than by the counter.

## 4. Mutated self-test — exit code, FULL output, last-line test

```
cd /tmp/r68-c7kill-LIfsdC && python3 -B corpus/check_embedded_outputs.py --self-test
EXIT=1
=== STDOUT (complete, 2 lines) ===
self-test: drifted entry not caught
drifted entry output accepted
=== STDERR (complete) ===
<empty, 0 bytes>
```

```
line_count= 2
last_repr= 'drifted entry output accepted'
endswith_marker= True
```

Both attributed conjuncts of the frozen predicate hold: `rc != 0` **and** `last.endswith("drifted entry output accepted")`.

## 5. Why the kill is attributable (not merely non-zero)

The mutation makes `evaluate(drifted_entry)` return `problems == []` with `checked == 1`; `caught` is falsy because of the empty list, not because of an exception or an earlier `require`:

- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/check_embedded_outputs.py:140-145` — `caught = (dproblems is not None and dchecked == 1 and dproblems and dproblems[0].startswith("drift entry:"))`; on False it prints `self-test: drifted entry not caught`, then `print(MARKER)` (:144), then `sys.exit(1)` (:145).
- The clean-entry `require` (:134-135 region: `"self-test: clean entry not clean"`) and the full-run `require` (`"self-test: full-run entry not clean"`) **did not** fire — neither message appears in the captured stdout. So the only executed exit is :145, the repaired forged-drift control, and the marker is the last thing printed before it.
- The marker literal occurs twice in the gate (`:21` docstring prose, `:36` `MARKER = …`); neither is an output path. In the mutant run the marker reaches stdout only through `print(MARKER)` at :144, i.e. through the r67-shadowing repair.
- Counter-side semantics agree: `measure.py:146-150` `run()` returns `(returncode, last non-blank line of stdout+stderr)`; stderr is empty here, so the counter's `last.endswith(C7_MARKER)` at `:428` reads the same string I measured.

## 6. Restoration evidence (no scratch drift left behind)

```
restored_sha256= b89183bec2fd3b94f5b0acc828a0d3fe16f6a98dde1d7752616da85d08a8e0ca
restored_bytes= 6791
identical_to_lane= True
diff -r <lane>/corpus /tmp/r68-c7kill-LIfsdC/corpus ; tree_diff_exit=0
```

Control re-run after restore: `EXIT=0`, last line `SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired`, stderr 0 bytes.

Lane tree never written: gate sha256 unchanged (`b89183be…8e0ca`, identical to the pre-copy value) and `git status --porcelain corpus/check_embedded_outputs.py` → empty. All scratch work stayed under `/tmp/r68-c7kill-LIfsdC`; the mutation existed only for the one run in §4.

## 7. Calibration findings on the C1 surface (reported, not fixed; this seat is read-only)

1. **The registry row still states the defect the repair removed.** `SKILL.md:268` (`## Gate registry`, `self-test` field) still reads: *"**correction 2026-10-24 (r67 adjudication):** the trailing forged-drift control's marker `drifted entry output accepted` is structurally shadowed by that earlier require and can never fire … recorded limitation, reorder fix routed"*. My §4 measurement falsifies "can never fire": the marker is the last line of a killed mutant run. The registry is the *registered* attribution C1 is scored on, so as landed it contradicts the bytes it registers. `claims.md` §C1's "correct the registry row to state the measured truth" is written as a fail-branch action; on the pass branch the same staleness remains and should be corrected in the same revision as the flip decision.
2. **`C7_CONTROL_PASS` is not a reachability test.** `measure.py:408` computes it as `c7_selftest_ok and C7_MARKER in c7_gate.read_text(...)`, and the gate's own docstring (`check_embedded_outputs.py:21`) plus the constant definition (`:36`) contain the literal. So the conjunct is satisfied by text presence, not by the marker ever being printable — empirically confirmed: `reports/round-68/measure-before.log:75` reads `C7_CONTROL_PASS=1/1` on base `f165908` while `:77` reads `C7_MUTANT_KILLED_ATTRIBUTED=0/1`, on the file whose marker is dead code. The attribution conjunct (§4) is the load-bearing one; `C7_CONTROL_PASS=1/1` should not be cited as evidence that the marker is reachable.
3. **Registry `measured-against` is stale**: `SKILL.md` still names `reports/round-67/measure.py` and its `7933c060…bc07e` digest, not the round-68 counter `0de4eb6f…f7766` the claims freeze. Cosmetic for scoring, but it is the field a later seat reads to find the instrument.
4. **Mutant scope note (survival surface, not a coverage failure here):** the mutant only removes the verdict-bearing comparison, so the clean and full-run branches still pass (`problems == []` is exactly what they require). The single detector for this mutant is the drifted-case branch — which is the branch the repair made attributable. No additional detector is claimed.

## Tooling

No installs or upgrades were needed (python3 only, already present). Nothing recorded against the operator tooling directive.

## Bounds compliance

Wrote exactly one file — this report, `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-68/R68MutC7Kill.md`. No writes to `corpus/`, `reports/`, `LOG.md`, `SCORECARD.md`, `SHONEN.md`, `.git`, jj state, or any sibling lane. No git/jj mutations, no `agent://` messages to other seats, no subagents. Scratch copy is disposable and now byte-identical to the lane corpus.
