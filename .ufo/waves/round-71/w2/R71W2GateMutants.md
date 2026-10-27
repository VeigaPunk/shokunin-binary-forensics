# R71W2GateMutants — fresh scratch-mutation probe of the patched embedded-output gate (wave 2)

**VERDICT: GATE HOLDS — 5/5 valid mutants killed, 0 survivors, baseline and restored bytes green on every leg; the CLI legs (not `--self-test`) are the sole killers of both main-handler mutants, now observed directly on the exact production-120s timeout path (closes W1's `R71W1GateMut` attribution-4 `[INFERENCE]`).**

Scope: `corpus/check_embedded_outputs.py` at final candidate `4c1eeaee88fd07e442f1bd546faf77be3957d390` — bytes identical to HEAD and to the working tree (sha256 `05afff8b9f4a47d6705b6de17b7b4e38f28927ac7139dfb2748420a31cf938f8`, 313 lines). All mutation in scratch `/fast/scratch/hyaku/revenger-r71/R71W2GateMutants/`; zero lane writes; read-only seats respected; no installs, no pacman, no subagents, no route/config changes.

## Detector (bounded, frozen before scoring)

Three legs per config, mirroring the counter's C2 legs (`reports/round-71/measure.py:100-121`):

1. `--self-test` (hermetic, includes the injected-1s timeout leg) — `python3 -B <gate> --self-test`, cwd=scratch work dir.
2. CLI missing-entry leg — `python3 -B <gate> --entry <scratch>/work/corpus/knowledge/round-71-missing-entry.md` (nonexistent path, counter shape), stderr captured.
3. Production timeout CLI leg — counter fixture shape (`measure.py:107-117`): fixture copies the lane `corpus/`, writes `corpus/sleeper_r71.py` = `import time; time.sleep(300)` and `corpus/knowledge/round-71-timeout-probe.md` with a `$ python3 -B corpus/sleeper_r71.py` fenced block; gate executed from the fixture with the gate's own production `timeout=120` — no injected value. One fixture per config, all legs run concurrently; wall time confirms the real 120 s limit fired.

## Baseline — pristine `05afff8b…`

```
[self-test] rc=0
  SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired, pin and confinement checks passed, missing-entry and timeout legs passed
[cli-missing-entry] rc=2
  could-not-evaluate: entry not found: …/work/corpus/knowledge/round-71-missing-entry.md
  stderr: (empty)
[timeout-leg pristine wall=120.1s rc=2]
  could-not-evaluate: command timed out after 120s: python3 -B corpus/sleeper_r71.py
  stderr: (empty)
```

Baseline green on all three legs before any mutation; detector run again identically on mutated and restored bytes.

## Mutants (smallest behavior-bearing point each; one mutant per fresh pristine copy)

| # | Mutant | Edited point | sha256 (mutated) | self-test | CLI missing-entry | Production-120s timeout leg | Verdict | Killed by |
|---|--------|--------------|------------------|-----------|-------------------|------------------------------|---------|-----------|
| M1b | reason-text drift only | `evaluate`: `entry not found:` → `entry not located:` | `98a87168e74d0c4cdd5d2567959410805ba58cdd1831ca121501c1c89bc12255` | rc=1 `self-test: missing-entry reason was not declared` | rc=2, `could-not-evaluate: entry not located: …`, no traceback | not run (already killed) | KILLED | self-test exact-reason require; counter's exact-text check kills it on the CLI too |
| M5 | missing-entry handler deleted | `evaluate`: remove `if not path.is_file(): raise CannotEvaluate("…entry not found…")` | `6f8f8ca6da2cb95eb61be16ace22b330814284d4bc7ec206f684185dce692e76` | rc=1 `self-test: missing-entry reason was not declared` | rc=2, `could-not-evaluate: entry not readable: …` (falls to OSError branch), no traceback | not run (already killed) | KILLED | self-test reason check |
| M2v2 | timeout catch removed | `run_cmd`: bare `subprocess.run(..., timeout=timeout)`, try/except dropped | `568d0bbe81758f2070df8f4543c87316565d4d83ff51b367955c2f9816144f44` | rc=1, raw `subprocess.TimeoutExpired: Command '['/usr/bin/python', '-B', '-B', 'sleeper.py']' timed out after 1 seconds` traceback | rc=2 declared line, no traceback (unaffected control path) | **rc=1, wall=120.2s, raw `subprocess.TimeoutExpired: … timed out after 120 seconds` traceback on stderr** | KILLED | self-test timeout leg AND the exact production CLI leg (directly observed; W1 held this as inference) |
| M3 | main traceback restored | `main` handler body `print(str(exc))` → `raise` | `1d0e03a7e353a88411982a592b3792571cd1dde907a32d730632c32300f257c7` | **rc=0 `SELFTEST OK` (blind)** | **rc=1**, stdout empty, `CannotEvaluate: could-not-evaluate: entry not found: …` traceback on stderr | not run | KILLED | **CLI leg only** |
| M4 | exit mapping 2→1 only | `main` handler `sys.exit(2)` → `sys.exit(1)` | `e9721b472cebe99124df294659a9e9b6807ad8a5f771e3e1f8e90edb20e27889` | **rc=0 `SELFTEST OK` (blind)** | **rc=1**, declared line intact, no traceback | **rc=1, wall=120.1s**, declared `…timed out after 120s:` line intact on stdout, no traceback | KILLED | **CLI leg only — now confirmed on both exit-2 paths** |

Invalid-mutant note: a first M2 edit removed only the `except` clause, leaving a bare `try:` → `SyntaxError: expected 'except' or 'finally' block`, rc=1 on every leg (`04ea9c2592674d8ed7c5613d2eb1f2fea54f3480ba8d4b1f0cd2d6f0032e7f93`). Discarded as not behavior-bearing (compile failure kills trivially) and superseded by M2v2. M5's and M4's shas equal W1's M1/M4 shas — the same minimal points were independently re-derived from the committed bytes.

## Attribution findings (coverage, not contract change)

1. **`_self_test` is structurally blind to `main()`.** It calls `evaluate()` directly and catches `CannotEvaluate` itself, so M3 (traceback restored) and M4 (exit 2→1) both print `SELFTEST OK`. Only the CLI legs kill them — on the missing-entry leg and, newly this wave, on the production-120s timeout leg (M4 rc=1 with the declared timeout text still printed; M2v2 would reach `main` uncaught). The frozen "exits 2 / no traceback" predicate is therefore carried entirely by real-CLI execution; `--self-test` alone would admit both main-handler mutants as survivors.
2. **W1's only `[INFERENCE]` is closed.** W1 `R71W1GateMut` finding 4 deferred the production-120s CLI leg; this wave ran it for pristine (rc=2, declared line, clean stderr), M2v2 (rc=1, raw 120-second `TimeoutExpired` traceback) and M4 (rc=1, declared line, clean stderr) — all exactly as inferred, at wall 120.1–120.2 s.
3. **Registered do-nothing controls are independently reachable in scratch:** control E (declared text, exit 1) is exactly M4; control F (missing-entry only, timeout still raises) is exactly M2v2. Both are killed by this detector, matching their frozen `HOLDS_C2_V1=no`.
4. **M1b partial-mask nuance reconfirmed on fresh bytes:** against exit-code/no-traceback alone the text-drift mutant survives the CLI leg structurally (rc=2, `could-not-evaluate:` line, clean stderr); it dies only on the exact-reason contract (self-test require; the counter's `'could-not-evaluate: entry not found:' in stdout` check kills it at CLI level too).

## Restoration evidence

```
cp gate.pristine.py → work/corpus/check_embedded_outputs.py and timeout-restored fixture
sha256 restored gate = 05afff8b9f4a47d6705b6de17b7b4e38f28927ac7139dfb2748420a31cf938f8  (== pristine)
[self-test] rc=0 SELFTEST OK … missing-entry and timeout legs passed
[cli-missing-entry] rc=2, could-not-evaluate: entry not found: …, stderr empty
[timeout-leg restored wall=120.2s rc=2] could-not-evaluate: command timed out after 120s: python3 -B corpus/sleeper_r71.py, stderr empty
lane corpus/check_embedded_outputs.py sha256 = 05afff8b9f4a47d6705b6de17b7b4e38f28927ac7139dfb2748420a31cf938f8 (unchanged)
git status --porcelain corpus/check_embedded_outputs.py → empty (clean)
```

Commands: `git -C <lane> show 4c1eeae…:corpus/check_embedded_outputs.py > gate.pristine.py` (extraction, read-only); drivers `drive_fast.py` / `drive_slow.py` / `m2slow.py` in scratch (subprocess legs, no env or config changes). All five mutant files were byte-exact single-substring replacements asserted `count==1` against pristine before writing.

Scratch `/fast/scratch/hyaku/revenger-r71/R71W2GateMutants/` deleted after this report was written. No L0 question answered here; no source edits; wave-2 findings only.

Report trailer: `.ufo/waves/round-71/w2/R71W2GateMutants.md`
