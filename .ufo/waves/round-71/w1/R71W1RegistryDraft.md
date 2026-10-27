# R71W1RegistryDraft — SKILL gate-registry wording for the exit-2 legs

DRAFT READY, row matches code on all four behavioral conjuncts; three registry gaps (stale citation, missing counter label, unstated unchanged-clauses) and three receipt conflicts reported below, not judged.

Scope: lane `/home/vgpnk/Projects/shokunin/revenger-shokunin` at working-tree tip `18200a4` (`round-71: build v6 candidate and gate exit-2 cases`). Read-only; no lane source edited, no commit, no counter run of my own except the gate's own CLI/self-test probes. Access date for every cited lane line: 2026-10-27. No new source row (S0xx) was opened this round, so no ≤25-word source quote is owed here; the quotes below are lane files.

## 1. Verdict basis — what the landed bytes actually do

All commands run from the lane root; `TMPDIR` pointed at my scratch so the gate's temp dirs stayed out of the lane.

| probe | command | observed |
|---|---|---|
| self-test | `python3 -B corpus/check_embedded_outputs.py --self-test` | `rc=0`, `elapsed_ms=1062`, stdout `SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired, pin and confinement checks passed, missing-entry and timeout legs passed`, stderr empty |
| missing entry | `--entry corpus/knowledge/round-71-missing-entry.md` | `rc=2`; stdout `could-not-evaluate: entry not found: corpus/knowledge/round-71-missing-entry.md`; stderr empty |
| path is a directory | `--entry corpus` | `rc=2`; stdout `could-not-evaluate: entry not found: corpus` |
| no `$ cmd` blocks | `--entry <scratch>/noblocks.md` | `rc=2`; stdout ``could-not-evaluate: no `$ cmd` blocks or unsupported command`` |
| refused command (`python3 -B -c print(1)`) | `--entry <scratch>/hostile.md` | `rc=2`; same combined message; stderr 0 bytes |
| usage | no arguments | `rc=64`, docstring printed |
| malformed pin file (out of the declared surface) | copied `corpus/`, `printf '{bad json' > corpus/embedded_output_pins.json`, `--entry corpus/knowledge/round-65-apk-axml-byte-evidence.md` | `rc=1`, stderr contains `Traceback` / `json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)` |
| unchanged functions | `git diff b7abcd8..18200a4 -- corpus/check_embedded_outputs.py \| grep '^@@'` | hunks only at `5,10` (docstring), `16,16` (docstring), `38,6` (`CannotEvaluate`), `95,7` + `103,8` (`run_cmd` timeout pass-through), `148,10` (`evaluate` guard), `168,7` (`run_cmd` call), `255,7` (self-test legs), `265,9` (`main`); `confined`/`inside`/`apply_pin`/`drift` have no hunk |
| base red-before | `git show b7abcd8:corpus/check_embedded_outputs.py` | `:154` `text = Path(entry_path).read_text(...)` with no existence guard (missing → `FileNotFoundError` traceback); `:106-107` `subprocess.run(..., timeout=120)` with no `except` (timeout → `TimeoutExpired` traceback); `:120` pin load unguarded |

Timeout CLI leg at the production 120 s limit was **not** run by me (12-minute seat box; `R71W1TimeoutProbe`/`R71W1GateReplay` own it). The exact string is fixed by f-string construction: `corpus/check_embedded_outputs.py:114` — `could-not-evaluate: command timed out after {timeout}s:` — with the default `timeout=120` threaded from `:158`/`:102` and the CLI calling `evaluate(args[1], Path.cwd())` at `:296`.

## 2. Exact SKILL registry wording (paste-ready; L1 owns the edit)

### 2a. `## Gate registry` row — replacement for current `SKILL.md:296`

```
| could-not-evaluate map (round 71) | Missing/unreadable entry and declared-command timeout are declared exit-2 classifications instead of uncaught exceptions. `corpus/check_embedded_outputs.py:161-166` refuses a path that is not a regular file as `could-not-evaluate: entry not found: <path-as-given>` and an unreadable file as `could-not-evaluate: entry not readable: <path>`; `:102-114` threads the 120-second limit into `run_cmd` and converts `subprocess.TimeoutExpired` into `could-not-evaluate: command timed out after 120s: <cmd>`; `:296-300` prints that message and exits 2, so no traceback reaches stderr. The self-test asserts both reasons hermetically (`:269-285`: a missing path, and an in-tree `sleeper.py` run under an injected `timeout=1` asserting `command timed out after 1s:`) and exits 0 printing `SELFTEST OK` with `missing-entry and timeout legs passed` (`:286`); measured 1.06 s on this host. The self-test asserts the raised reasons through `evaluate(...)`, not the CLI mapping — the CLI mapping is measured by the counter (`reports/round-71/measure.py:126,135` → `C2_MISSING_ENTRY_EXIT2`, `C2_TIMEOUT_EXIT2`; `:140-141` → `C2_GATE_SELFTEST`, `HOLDS_C2_V1`), frozen digest `d0d59b79…` (pre-registration). Unchanged from base `b7abcd8`, verified by `git diff`: the verbatim comparison line `problems += drift(lines, stdout_set, lineno)` (`:190`), the pin rule (`apply_pin`, `:130-151`), command confinement (`confined`/`inside`, `:79-99`, wiring leg `:263-270`) and the production 120-second limit. Exit 2 is claimed for exactly these two new classes plus the pre-existing no-`$ cmd`-blocks/unsupported/refused-command path (`:302-303`); a malformed `corpus/embedded_output_pins.json` is not classified (uncaught `json.JSONDecodeError`, exit 1 with traceback — observed 2026-10-27). |
```

Rationale for each clause vs the currently landed row: the landed row already names both exact message prefixes and "no traceback", but (i) it does not say the drift/pin/confinement behavior and the 120 s limit are unchanged — a conjunct the frozen C2 claim requires the row to carry, (ii) it names two of the counter's three labels, omitting `C2_GATE_SELFTEST`, and (iii) "the live CLI returns exit 2 … and no traceback" is unscoped, while a malformed pin file demonstrably still tracebacks.

### 2b. `verdict map` row — replacement for current `SKILL.md:288` (already accurate; this is the optional exact-text tightening)

```
| verdict map | `0` clean (≥1 block checked, every embedded output line verbatim) · `1` failed (an embedded line absent from its command's stdout, a declared command exits non-zero, or a pin finding `pinned historical script digest mismatch`) · `2` could-not-evaluate, printing one `could-not-evaluate:` line and no traceback, for exactly these reasons: `entry not found: <path>` (missing path, or a path that is not a regular file), `entry not readable: <path>`, `command timed out after 120s: <cmd>` (the production limit; the self-test injects 1s), or `no `$ cmd` blocks or unsupported command` (also printed for a command refused by confinement) · `64` usage (no arguments or an unrecognised form; PROTOCOL §Gate standard requires it declared) |
```

The landed `:288` text ("no `$ cmd` blocks, unsupported command, unreadable/missing entry, or declared command times out after 120s; each prints the applicable `could-not-evaluate:` reason") is true as written; use this only if L1 wants the exact strings in the registry.

### 2c. `self-test` row — one citation must be repaired in current `SKILL.md:289`

Current text cites the drifted-case branch as `corpus/check_embedded_outputs.py:140-146`. The block is at `:228-233` on this tip (`:228-229` `caught = (…)`, `:230` `if not caught:`, `:231` `self-test: drifted entry not caught`, `:232` `print(MARKER)`, `:233` `sys.exit(1)`), and was already at `:218-220` at base `b7abcd8` — the citation was stale before round 71 and this round's `+12` lines moved it further. Draft replacement clause:

```
**Rewritten 2026-10-25 from the after-run (r68 adjudication, repair D2/M46); citation refreshed 2026-10-27:** the drifted case is an `if not caught:` branch (`corpus/check_embedded_outputs.py:228-233`) that prints `self-test: drifted entry not caught`, then the marker `drifted entry output accepted` **as the last line**, then exits 1 …
```

The row's round-71 legs are covered by 2a; do not duplicate them in `:289`.

## 3. Row-vs-code match table (claim conjunct → site → observed)

| frozen C2 conjunct | code site | match |
|---|---|---|
| CLI on nonexistent entry exits 2 | `:161-162`, `:295-300` | yes, observed `rc=2` |
| prints `could-not-evaluate: entry not found:` | `:162` | yes, byte-exact prefix |
| no traceback | `main` catches `CannotEvaluate` at `:296-300` | yes, stderr empty |
| valid entry, in-tree command over 120 s → exit 2 | `:102-114` + `:158` default → `:296` call | code-level yes; CLI leg deferred to executor seats |
| prints `could-not-evaluate: command timed out after 120s:` | `:114` f-string with `timeout=120` | yes by construction |
| `--self-test` exits 0 with both fast hermetic cases | `:269-285`, `:286`, `:291-294` | yes, observed `rc=0` in 1.06 s |
| registered row names these exact mappings | `SKILL.md:296` | partially — prefixes yes, but see 2a gaps |
| drift unchanged | `drift` `:153-155`, call `:190` | yes, no diff hunk |
| pin unchanged | `load_pins` `:118-127`, `apply_pin` `:130-151` | yes, no diff hunk |
| confinement unchanged | `confined` `:79-89`, `inside` `:91-99`, wiring `:263-270` | yes, no diff hunk |
| 120 s limit unchanged | `:102` `timeout=120` | yes; the self-test's 1 s is an argument, not a changed default |

## 4. Findings (verbatim conflicts and registry gaps)

**F1 — frozen counter and claims are being rewritten in the working tree, and their digests no longer match the pre-registration receipt.** `reports/round-71/pre-registration.txt` records `Counter SHA-256: d0d59b79652dae9d65796493f703470dc4d4998ec607cb25a41aed939f38d06c` and `Claims SHA-256: 1febae1279fdeca323f5e8beffeb0a8ac2f26256158f7000bb0b2eff8321c3f5`; those values match the **committed** files at `63b560b`/`18200a4`. Working-tree bytes at 2026-10-27T12:22:55-03:00 hash `a86c6a95efab754c39d2c9f9b04e9927456392defdef6acafac7ee7ef3c5a544` (`measure.py`, had been `44c0e384…` at ~12:21:56, mtime 12:22:16) and `5b95d343b7f2e5c228d22f7de4dd4d43cb9b1844e4709969d07129c6acc1d19b` (`claims.md`, mtime 12:21:41). `git status --porcelain` → ` M reports/round-71/claims.md`, ` M reports/round-71/measure.py`. The uncommitted counter diff (`git diff -- reports/round-71/measure.py`, one hunk `@@ -46,20 +46,48 @@`) replaces `q_votes()`'s committed per-seat `.ufo/waves/round-71/w2-votes/*.json` parsing with an orchestrator `.ufo/waves/round-71/w2-results.json` parser; the uncommitted claims diff changes the C1 vote-mechanism sentences to match (e.g. committed: "The counter parses committed per-seat JSON vote files under `.ufo/waves/round-71/w2-votes/`"). The C2 legs themselves are untouched by that hunk (`C2_MISSING_ENTRY_EXIT2` at `:126`, `C2_TIMEOUT_EXIT2` `:135`, `C2_GATE_SELFTEST` `:140`, `HOLDS_C2_V1` `:141` in the working tree). I neither judge nor repair this; it is reported for the canonical judge with both digests.

**F2 — a receipt named by the frozen claims does not exist.** `reports/round-71/claims.md` §C2: "Red-before receipts are `controls/C2-missing-before.log` and `controls/C2-timeout-before.log`." `ls -l reports/round-71/controls/` lists only `A-do-nothing-base.log`, `B-C1-readme-flip-only.log`, `C-C1-admitted-stub.log`, `C2-timeout-before.log`, `D-C1-v5-copy-with-q16.log`; `C2-missing-before.log` is absent. The missing-entry red is instead in `reports/round-71/measure-before.log:12`.

**F3 — the red-before label disagrees with the claim's own before-text for the timeout leg.** `reports/round-71/measure-before.log:13` prints `C2_TIMEOUT_EXIT2=0/1 rc=1 stderr_traceback=no`, while `claims.md` §C2 Before says the timeout case "produces `TimeoutExpired` traceback and exit 1". The separate control does show that traceback — `reports/round-71/controls/C2-timeout-before.log:1` `Traceback (most recent call last):`, last lines `subprocess.TimeoutExpired: Command '['/usr/bin/python3', '-B', '-B', 'sleeper.py']' timed out after 120 seconds`, `RC=1` — but that control runs a different fixture (`sleeper.py`, double `-B`) from the counter's leg (`corpus/sleeper_r71.py`, `time.sleep(300)`, `reports/round-71/measure.py:129-135`). Both agree the leg scores 0/1; the stderr field and the fixture identity do not agree with each other. Diagnosing the cause is out of my seat; [INFERENCE] a gate run that exits 1 on a non-timed-out command (`drift entry:N command exited RC`) would produce exactly `rc=1`, empty stderr.

**F4 — registry line-number drift (M46 class).** `SKILL.md:289` cites `corpus/check_embedded_outputs.py:140-146`; actual block is `:228-233` (tip) and `:218-220` (base `b7abcd8`). This round's `+12` lines in `_self_test` widened the gap. Repair text in §2c.

**F5 — the landed round-71 row is under-specified.** `SKILL.md:296` omits `C2_GATE_SELFTEST` (`reports/round-71/measure.py:140`) and never states that drift/pin/confinement and the 120 s limit are unchanged, although the frozen C2 claim makes "without changing its drift, pin, or confinement behavior" and "No change is made to … the gate's 120-second runtime limit" part of the predicate. Draft §2a carries both.

**F6 — scope boundary the row must not overclaim.** A malformed `corpus/embedded_output_pins.json` still raises an uncaught `json.JSONDecodeError` (exit 1, traceback observed). Also `:161` classifies a directory path as `entry not found`, not `entry not readable`. The draft scopes the no-traceback/exit-2 claim to the two named classes; the landed row's unqualified "the live CLI returns exit 2 … and no traceback" reads broader than the code.

## 5. Out of scope / limits

- No SKILL.md, `corpus/`, counter, claims, or control file was edited; no commit, push, jj/git mutation, or subagent dispatch.
- `HOLDS_C2_V1` itself, the 120 s CLI timeout leg, and the v6 entry gate/lint were not measured here; the frozen counter and wave-2 scoring are other seats'.
- The frozen counter mutated while this seat ran (F1); line numbers cited for `reports/round-71/measure.py` are the working-tree ones at 12:22:55, digest `a86c6a95…`, and the labels are the same names in the frozen `d0d59b79…` bytes.
- Scratch `/fast/scratch/hyaku/revenger-r71/R71W1RegistryDraft/` (selftest/missing/badpins/hostile receipts) deleted before returning; evidence is inlined above.

Report trailer: `.ufo/waves/round-71/w1/R71W1RegistryDraft.md`
