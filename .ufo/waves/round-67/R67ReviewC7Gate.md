FAIL — the registered forged-drift control can never fire: `require(not ok(dproblems), MARKER)` at corpus/check_embedded_outputs.py:141 is unreachable because the descriptive require at :132-134 exits first whenever `dproblems` is empty (the frozen C7 mutant's own shape), so `C7_MUTANT_KILLED_ATTRIBUTED` can never be 1/1 — plus two verdict-map inaccuracies and a materially understated command surface vs the SKILL.md registry row.

Scope: read-only review of `corpus/check_embedded_outputs.py` (sha256 `19007bebeb4d60dafd826df108584933ebb3f2b1e6ab112925ea6c6cab3e697d`) against its registry row `SKILL.md:260-273` and frozen counter `reports/round-67/measure.py` (sha256 verified `7933c060db4d9b8db889830e2e0b6e1da1724d94854201aac9552e2a49cbc07e` = claims.md pin ✓). All runs in scratch copy `/tmp/r67c7gate-hzKefT` (`cp -a corpus/`); no lane bytes written. Tools installed: none.

## F1 — CRITICAL: mutant kills but is never attributed; `C7_MUTANT_KILLED_ATTRIBUTED` cannot be 1/1

Frozen mutant (claims.md §C2; measure.py:366-373, regex `problems \+= drift\(lines, stdout_set, lineno\)` → `problems += []`, matches exactly once at check_embedded_outputs.py:101). Empirical, exact frozen substitution:

```
hits: 1
$ python3 -B /tmp/c7-mutant.py --self-test
self-test: drifted entry not caught
mutant_rc=1
```

measure.py:408 attributes iff `rc != 0 and last.endswith("drifted entry output accepted")` where `last` = last line of stdout+stderr (measure.py:130-131). Under the mutant `dproblems == []`, so `require(dproblems ... and dproblems[0].startswith("drift entry:"), "self-test: drifted entry not caught")` at probe :132-134 fires at exit 1 *before* `require(not ok(dproblems), MARKER)` at :141. `MARKER` (:32, :141) is therefore dead code: it prints only if `ok(dproblems)` fails, which requires `dproblems` non-empty — but `dproblems` non-empty is exactly the state where the require never fires. Attribution condition is a constant false → `C7_MUTANT_KILLED_ATTRIBUTED=0/1` → C2 frozen predicate unsatisfiable → `HOLDS_OK_V5=no` → likely probe exit 1 (void condition "probe exit non-zero at final"). Also falsifies registry row SKILL.md:268 claim that the control "fires with attributed marker". Unmutated self-test passes (control half OK):

```
$ python3 -B corpus/check_embedded_outputs.py --self-test
SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
selftest_rc=0
```

Fix shape (recommendation only): the marker require must precede the descriptive require, or the drifted-case require itself must carry `MARKER` (one line: `require(dproblems and dproblems[0].startswith("drift entry:"), MARKER)`), so the frozen mutant's last line is the marker.

## F2 — HIGH: registry "read failure → exit 2" is wrong; four could-not-evaluate classes exit 1

- Missing/unreadable entry: `Path(entry_path).read_text` at :87 raises uncaught → traceback → exit **1**, not 2. Observed: `--entry /nonexistent.md` → `FileNotFoundError` traceback, `nofile_rc=1` (exit 1 is the drift/failed verdict in the map — a read failure is reported as "failed/drift").
- Malformed quotes in a declared command: `shlex.split` at :69 raises `ValueError` uncaught → exit 1. Observed: `unclosed_rc=1` (`ValueError: No closing quotation`).
- Command timeout: `subprocess.TimeoutExpired` at :74-75 uncaught → exit 1 (not evaluated; 120 s wait only).
- Command exits non-zero: reported as `drift entry:N command exited R: cmd` → exit 1. Observed `$ python3 -c "import sys; sys.exit(3)"` → `drift entry:2 command exited 3 … checked_blocks=0 problems=1`, rc=1. The registry's exit-1 description ("an embedded output line the entry's own command does not print") doesn't cover command crashes; a crashed command also leaves `checked` un-incremented, so `checked_blocks=0` under exit 1 is possible.
- True exit 2 observed only for: zero parsed blocks (`noblocks_rc=2`) and unsupported `argv[0]` (`$ ls -la` → `badcmd_rc=2`) — i.e. only the (None) returns at :71, :73, :90, :96.

## F3 — MEDIUM: command surface allows arbitrary code execution; write-scope row is conditional at best

`run_cmd` (:69-76) checks only `argv[0] in ("python3","python",sys.executable)` then runs `[sys.executable, "-B", *argv[1:]]` — every remaining token is passed verbatim. `$ python3 -c "<any python>"` executes arbitrary code as the invoking user. Observed: an entry whose sole block is `$ python3 -c "open('/tmp/c7-pwned.txt','w').write('arbitrary code ran')"` ran the payload and exited 0 clean (`inject_rc=0`, file contents `arbitrary code ran`). So registry SKILL.md:271 "writes nothing outside its own temp dirs" holds only for benign committed entries; as a security property the gate *is* the execution channel (also `-m`, `-S sitecustomize`, bare `python3` inheriting stdin — potential 120 s block, observed class not run). Registry wording "argv list, no shell, python3 first token only" is literally true; the implication of containment is not.

## F4 — LOW: parse/verdict gaps

- Vacuous clean: a block with zero output lines counts as `checked` (:101-102) and contributes nothing to `problems`; observed `vacuous_rc=0 checked_blocks=1`. An entry of only command-only fences exits 0 "clean" having compared zero lines.
- Unparseable blocks fail open as 2, not 1: `$ cmd` inside `~~~` fences, ```` (4-backtick) fences (line :49 toggles on any line starting with three backticks, so a ```` fence is parsed as an empty ``` fence immediately closed — contents unfenced), indented fences, or unfenced `$ ` lines are all invisible to the parser → if no ````-fenced `$ ` block survives, exit 2 "could-not-evaluate" rather than a failure. Rendering-equivalent drift in those blocks is unchecked.
- `errors="ignore"` (:87) hides entry-encoding problems only by later failing drift honestly; `text=True` (:75) can raise `UnicodeDecodeError` on non-UTF-8 command output → exit 1 (class noted, not run).
- Cosmetic: `checked_blocks=0` can appear under exit 1 (see F2); docstring/registry terminology split ("probe" in :5-9, claims.md, registry `kind=gate` :265, prompt "registered probe") — harmless but the seat brief itself mirrored the ambiguity.

## Verified-accurate registry facts

- Pinned-value path (SKILL.md:269): `--entry corpus/knowledge/round-65-apk-axml-byte-evidence.md` over sha256 `cf42cc2059e454027685a59a2a35a190f6ba981f95645f41e407c47c01c4d05a` (matches row) → exit 1, `drift entry:41 …` naming the M39 drifted hex `4d616e696673742d…`, `checked_blocks=15 problems=1` ✓.
- V2 clean: `--entry corpus/knowledge/round-67-apk-axml-byte-evidence.md` → exit 0, `checked_blocks=16 problems=0` ✓.
- Self-test hermeticity: `tempfile.TemporaryDirectory(prefix="rev-r67-c7-selftest-")` (:152-153), all fixtures/entries written inside tmp (:107-127), `evaluate` run with `cwd=tmp` (:128), no network, no lane-tree writes ✓.
- Mutant regex hits exactly once ✓; `run()`/attribution semantics in measure.py:127-131, 385-425 as analyzed ✓; measured-against sha256 ✓.

## Verdict for the C2 calibration claim

Gate present and functional for the happy paths; red-before and v2-clean receipts reproduce. But the frozen predicate's attributed-mutant leg is unsatisfiable by construction (F1) — recommend flagging C2 as failing on the landed bytes pending a one-line marker-order fix, and correcting SKILL.md:267-268,271 rows for F2/F3.
