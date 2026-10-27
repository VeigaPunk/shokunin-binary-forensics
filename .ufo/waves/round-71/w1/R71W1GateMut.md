# R71W1GateMut — scratch-mutant probe of the patched embedded-output gate

**Verdict: GATE HOLDS — 4/4 mutants killed, 0 survivors; attribution split shows the exit-2/no-traceback mapping is enforced only by the CLI leg (`--self-test` alone cannot see `main()`'s handler).**

Scope: `corpus/check_embedded_outputs.py` (lane sha256 `05afff8b9f4a47d6705b6de17b7b4e38f28927ac7139dfb2748420a31cf938f8`, 313 lines). All mutation in scratch `/fast/scratch/hyaku/revenger-r71/R71W1GateMut/`; zero lane writes. C2-relevant behavior points per frozen claims (§C2): missing-entry handler (`evaluate`, raises `CannotEvaluate("could-not-evaluate: entry not found: …")`), timeout catch (`run_cmd`, `except subprocess.TimeoutExpired → CannotEvaluate("…command timed out after {timeout}s…")`), traceback suppression + exit mapping (`main`, `except CannotEvaluate: print(str(exc)); sys.exit(2)`).

## Detector (bounded)

`--self-test` (hermetic, includes injected-1s timeout leg) + CLI missing-entry leg `--entry /nonexistent/missing-entry.md`, run from scratch with stderr captured. Pristine baseline green:

```
=== BASELINE pristine 05afff8b ===
--- self-test
SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired, pin and confinement checks passed, missing-entry and timeout legs passed
selftest_exit=0
--- cli missing entry
could-not-evaluate: entry not found: /nonexistent/missing-entry.md
cli_exit=2
--- cli stderr: (empty)
```

## Mutants (each applied to a fresh pristine copy; smallest behavior-bearing point)

| # | Mutant | Edited point | sha256 (mutated) | self-test | CLI missing-entry | Verdict | Killed by |
|---|--------|--------------|------------------|-----------|-------------------|---------|-----------|
| M1 | remove missing-entry handler | `evaluate`: delete `if not path.is_file(): raise CannotEvaluate("…entry not found…")` | `6f8f8ca6da2cb95eb61be16ace22b330814284d4bc7ec206f684185dce692e76` | exit 1 `self-test: missing-entry reason was not declared` | exit 2, `could-not-evaluate: entry not readable: …`, no traceback | KILLED | self-test (reason check) |
| M2 | remove timeout catch | `run_cmd`: bare `subprocess.run(..., timeout=timeout)`, drop try/except | `568d0bbe81758f2070df8f4543c87316565d4d83ff51b367955c2f9816144f44` | exit 1, raw `subprocess.TimeoutExpired: … timed out after 1 seconds` traceback on stderr | exit 2 clean (control; unaffected path) | KILLED | self-test (timeout leg) |
| M3 | restore traceback | `main`: handler body → `raise` | `79965469e130fd7cbb4a69fa2aea8f4d85ae309bb2ded14a3bbec08b754df648` | exit 0 `SELFTEST OK` | exit 1, empty stdout, `CannotEvaluate: could-not-evaluate: entry not found: …` traceback on stderr | KILLED | CLI leg only |
| M4 | alter only exit mapping | `main`: handler `sys.exit(2)` → `sys.exit(1)` | `e9721b472cebe99124df294659a9e9b6807ad8a5f771e3e1f8e90edb20e27889` | exit 0 `SELFTEST OK` | exit 1, declared line intact, no traceback | KILLED | CLI leg only |

Raw receipts (verbatim):

- M1 self-test: `self-test: missing-entry reason was not declared` / `selftest_exit=1`. M1 CLI: `could-not-evaluate: entry not readable: /nonexistent/missing-entry.md` / `cli_exit=2` / stderr empty. Falling through to the `OSError` catch changes only the reason text; exit code and no-traceback survive this mutant.
- M2 self-test stderr tail: `subprocess.TimeoutExpired: Command '['/usr/bin/python3', '-B', '-B', 'sleeper.py']' timed out after 1 seconds` / `selftest_exit=1`.
- M3 self-test: `SELFTEST OK: … missing-entry and timeout legs passed` / `selftest_exit=0`. M3 CLI: `cli_exit=1`, stdout empty, stderr tail `CannotEvaluate: could-not-evaluate: entry not found: /nonexistent/missing-entry.md`.
- M4 self-test: `SELFTEST OK: …` / `selftest_exit=0`. M4 CLI: `could-not-evaluate: entry not found: /nonexistent/missing-entry.md` / `cli_exit=1` / stderr empty.

## Attribution / survivor findings (coverage, not contract change)

1. **Self-test blind spot at `main()`.** `_self_test` calls `evaluate()` directly and catches `CannotEvaluate` itself, so it never exercises `main()`'s handler: M3 (traceback restored) and M4 (exit 2→1) both print `SELFTEST OK`. Only the CLI missing-entry leg kills them. The frozen predicate's "exits 2 / emits no traceback" legs are therefore carried entirely by the counter's CLI leg; `--self-test` alone would let both mutants pass as survivors. (A shell-out leg inside the self-test would close this, but per mutation protocol this is recorded as a finding, not changed.)
2. **M1 partial-mask nuance.** Against the CLI leg alone M1 survives structurally (still exit 2, still a `could-not-evaluate:` line, no traceback — only the reason drifts to `entry not readable` via the OSError branch). It is killed by the self-test's `require("entry not found:" in str(exc))` and would also be killed by the counter's exact-text check `could-not-evaluate: entry not found:`.
3. **Registered do-nothing controls are reachable.** Control E ("declared text, exit 1") is exactly M4; control F ("missing-entry only, timeout still raises") is exactly M2. Both are independently killed by this detector, matching `HOLDS_C2_V1=no` for E/F.
4. **Production 120s CLI timeout leg not exercised in scratch** (bounded box; would need >120 s). M2's kill is attributed via the gate's own injected-1s timeout leg, which shares `run_cmd`'s sole code path; the traceback propagation through `main` (no other handler exists) is [INFERENCE] from the M2/M3 CLI stderr evidence, not a 120 s observation.

## Restoration evidence

```
cp pristine → work; sha256 work/check_embedded_outputs.py
05afff8b9f4a47d6705b6de17b7b4e38f28927ac7139dfb2748420a31cf938f8  (== pristine)
detector on restored bytes: SELFTEST OK … selftest_exit=0; cli_exit=2, declared line, stderr empty
lane source: 05afff8b9f4a47d6705b6de17b7b4e38f28927ac7139dfb2748420a31cf938f8 (unchanged)
git status --porcelain corpus/check_embedded_outputs.py → empty (clean)
```

Baseline green before any mutation; mutated and restored bytes hashed at every step; scratch deleted after this report was written.

No installs performed; no pacman transactions; no lane source edits; no subagents; no route/config changes.

Report trailer: `.ufo/waves/round-71/w1/R71W1GateMut.md`
