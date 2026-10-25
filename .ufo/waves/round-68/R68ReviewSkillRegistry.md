ROW-DEFECT — four of the ten registry cells are clean (`name`, `kind`, entry command, `owner`) and six carry defects, four of them introduced or left stale by the round-68 repair (verdict map omits the measured `64` usage code and misclassifies read failure; self-test cell still asserts the marker "can never fire"; measured-against still names the round-67 counter; pinned-value path presents a digest-pinned baseline the gate does not enforce), plus a `probe`/`gate` self-contradiction left over from r67 routed defect D2.

Seat: `L1Revenger68.R68ReviewSkillRegistry` · leaf, read-only · measured tree: lane HEAD `4232235` (`git status --porcelain` empty for `SKILL.md`, `corpus/check_embedded_outputs.py`, `corpus/knowledge/round-68-*`, `corpus/snapshots/`) · nothing written outside this file · no tools installed or upgraded (no install channel was needed).

Row under review: `/home/vgpnk/Projects/shokunin/revenger-shokunin/SKILL.md:260-273`.
Gate: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/check_embedded_outputs.py` (tracked: `git ls-files` → `corpus/check_embedded_outputs.py`).
Standard: `/home/vgpnk/Projects/shokunin/PROTOCOL.md:375-420` §Gate standard (Verdict, Self-test, Two evidences, Registry, Scope).

---

## 1 · Measurements (commands and actual output)

### 1.1 The pinned-value path — snapshot exists, exits exactly as claimed

```sh
sha256sum corpus/knowledge/round-65-apk-axml-byte-evidence.md
→ cf42cc2059e454027685a59a2a35a190f6ba981f95645f41e407c47c01c4d05a  corpus/knowledge/round-65-apk-axml-byte-evidence.md

python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-65-apk-axml-byte-evidence.md
→ drift entry:41 embedded output line not in recheck stdout: {"cd_index": 2, ... "uncompressed_size": 69}
→ checked_blocks=15 problems=1
EXIT=1
```

Row claims sha256 `cf42cc20…` and "exit 1 naming entry:41". **Both hold, byte-identically.**

`git log --oneline -- corpus/knowledge/round-65-apk-axml-byte-evidence.md` → last touched `a4c712a` (round-66 commit).
Row claims "the bytes are the round-66-tip bytes, unchanged since". **Holds.**

### 1.2 Self-test — green, and cwd-independent (contra a lane-root-only reading)

```sh
python3 -B corpus/check_embedded_outputs.py --self-test      # cwd = lane root
→ SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
SELFTEST_EXIT=0

cd / && python3 -B …/corpus/check_embedded_outputs.py --self-test
→ SELFTEST OK: … forged control fired          CWD_ROOT_EXIT=0
```

### 1.3 The frozen mutant — **attributed kill is now real** (this is what falsifies the row's text)

```sh
# copy to /tmp, replace the single comparison call exactly as claims.md freezes it
mutation_sites= 1                      # regex `problems \+= drift\(lines, stdout_set, lineno\)`
python3 -B corpus/check_embedded_outputs.py --self-test
→ last line: drifted entry output accepted
MUT_EXIT=1   attributed= True
```

### 1.4 The negative control (spoofed marker) — killed but **not** attributable

```sh
MARKER = "drifted entry output accepted (spoofed)"    # sed matched exactly once
→ last line: drifted entry output accepted (spoofed)
SPOOF_EXIT=1   spoof_attributed= False
```

Marker literal appears as a single assignment (`check_embedded_outputs.py:36`) plus one docstring mention (`:21`) — `grep -n "drifted entry output accepted"` → only `:21`, `:36`. That is why the spoof moves the emitted last line off the registered marker. The same literal is hardcoded as the counter's spoof regex at `reports/round-68/measure.py:460` (`re.compile(r'MARKER = "drifted entry output accepted"')`) — an undocumented freeze coupling the row does not record.

### 1.5 Verdict-map probes — `64` undeclared, and "read failure" is **not** exit 2

```sh
python3 -B corpus/check_embedded_outputs.py                     → NOARG_EXIT=64
python3 -B corpus/check_embedded_outputs.py --entry a.md b.md   → EXTRA_EXIT=64
python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/does-not-exist.md
→ FileNotFoundError: [Errno 2] No such file or directory: 'corpus/knowledge/does-not-exist.md'
MISSING_EXIT=1
python3 -B corpus/check_embedded_outputs.py --entry /tmp/r68reg-unsup.md   # first token `echo`
→ could-not-evaluate: no `$ cmd` blocks, unsupported command, or read failure
UNSUP_EXIT=2
python3 -B corpus/check_embedded_outputs.py --entry corpus/README.md
→ could-not-evaluate: …          READMEEXIT=2
```

So: `0` clean, `1` failed, `2` could-not-evaluate-for-no-blocks/unsupported/argv0 — all as declared. But **`64` is reachable and undeclared**, and **read failure is a false `failed`**: PROTOCOL.md:380-382 names `64` explicitly ("every other code a gate exits (`2`, `3`, `64`, …) is declared in its registry entry and mapped onto clean | failed | could-not-evaluate"), and `grep -n "except " corpus/check_embedded_outputs.py` → only the `timeout=120` line matched, i.e. **no try/except anywhere**: `Path.read_text` (`:91`) and `subprocess.run(..., timeout=120)` (`:78-79`) both escape as an uncaught traceback → exit 1, which the row's map classes as `failed (drift)`.

### 1.6 The gate still separates real candidates

```sh
--entry corpus/knowledge/round-68-apk-axml-byte-evidence.md → checked_blocks=17 problems=0  V3_EXIT=0
--entry corpus/knowledge/round-67-apk-axml-byte-evidence.md → checked_blocks=16 problems=0  R67_EXIT=0
```

Consistent with `reports/round-68/measure-before.log:72-73` (`C7_RED_ON_R65_CANDIDATE=yes exit=1 :: checked_blocks=15 problems=1`, `C7_V2_CLEAN=yes exit=0 :: checked_blocks=16 problems=0`).

### 1.7 Instruments and their digests

```sh
sha256sum reports/round-67/measure.py → 7933c060db4d9b8db889830e2e0b6e1da1724d94854201aac9552e2a49cbc07e   (row cites 7933c060…bc07e: correct)
sha256sum reports/round-68/measure.py → 0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766   (not cited anywhere in the row)
```

### 1.8 Digest enforcement: absent

```sh
grep -n "hashlib\|sha256\|snapshot_tampered\|expected.json" corpus/check_embedded_outputs.py
→ NONE (no digest verification in gate)
find corpus -maxdepth 2 -name expected.json → (nothing); ls -d .ufo/waves/*/frozen → no frozen dirs
```

### 1.9 The registry-home pointer does not resolve inside this repo

```sh
ls PROTOCOL.md → ls: cannot access 'PROTOCOL.md': No such file or directory
ls -la /home/vgpnk/Projects/shokunin/PROTOCOL.md → 46627 bytes (fleet root only)
```

`SKILL.md:260` heads the registry `(registry home; PROTOCOL.md §Gate standard)` — a bare filename that a reader standing in the lane repo cannot open.

---

## 2 · Field-by-field verdicts (exact cell text quoted)

PROTOCOL.md:401-403 fixes the field set: *name, `gate|probe`, entry command, verdict map (code → class), self-test command and spelling, pinned-value path, write scope, owner*. The row carries all eight plus a `family note`, in order — **field set complete, no missing mandatory field.**

| # | field (`SKILL.md` line) | exact cell text | verdict |
|---|---|---|---|
| 1 | name (`:264`) | `` `check_embedded_outputs` `` | **OK** — module stem of `corpus/check_embedded_outputs.py`; unique in `corpus/` (`glob` shows no sibling); the file is tracked and committed. |
| 2 | kind (`:265`) | `gate (committed, re-runnable verdict script this lane owns)` | **OK, and it qualifies.** PROTOCOL.md:377-379: a gate "reads surfaces, compares them against expected values persisted in its own repo, and returns a verdict. A tool that cannot fail is a probe." Measured: exits `1` on real drift (§1.1), `0` on clean candidates (§1.6), `2` not-evaluable (§1.5) — it can fail, so `gate` is right. This is also the r67-settled direction (`corpus/lessons/round-67-verifier-spotcheck.md:230-235` routed D2: "The landed row is the authoritative registry"). |
| 3 | entry command (`:266`) | `` `python3 -B corpus/check_embedded_outputs.py --entry <knowledge.md>` (cwd = lane root) `` | **OK** — identical to the usage contract at gate `:14`; `--entry` requires exactly 2 argv (`:158`), so the placeholder is the only argument shape accepted; cwd = lane root is genuinely required (entry path is lane-root-relative). |
| 4 | verdict map (`:267`) | `` `0` clean (≥1 block checked, every embedded output line verbatim) · `1` failed (drift: an embedded output line the entry's own command does not print) · `2` could-not-evaluate (no `$ cmd` blocks / unsupported command / read failure) `` | **DEFECT (S1).** Three faults, all measured in §1.5: (a) **`64` undeclared** though reachable on no-args and on any argv that is not `--self-test` / `--entry <path>` (`:167-168`), and PROTOCOL.md:380-382 names `64` as a code that must be declared and mapped; (b) **"read failure" is false for class `2`** — a missing entry exits `1` with a `FileNotFoundError` traceback (`:91` has no try/except), i.e. it reads as a **false `failed`/drift** verdict instead of could-not-evaluate; (c) the `1` description omits its second finding kind — `drift entry:N command exited RC: cmd` (`:102`), which is a command non-zero exit, not output drift. |
| 5 | self-test (`:268`) | `` `python3 -B corpus/check_embedded_outputs.py --self-test` (spelling `--self-test`; hermetic temp trees; asserts clean+full-run exit 0 and drifted-caught — the drifted-case `require` at `_self_test` carries the frozen-mutant kill; **correction 2026-10-24 (r67 adjudication):** the trailing forged-drift control's marker `drifted entry output accepted` is structurally shadowed by that earlier require and can never fire — seats `R67ReviewC7Gate`/`R67MutC7Kill`/`R67CriticC7Claim`; recorded limitation, reorder fix routed) `` | **DEFECT (S1) — stale and now measurably false.** The command and spelling are correct and green (§1.2). But the bolded correction states the marker "is structurally shadowed … and **can never fire**" — after the round-68 repair the mutated run's last line **is** `drifted entry output accepted` (§1.3, `attributed=True`), and the spoof control shows the attribution rule is discriminating rather than exit-code-only (§1.4). The clause "the drifted-case `require` at `_self_test`" also names a construct that no longer exists as a require: the drifted case is an explicit `if not caught:` branch at `:140-145` that prints `self-test: drifted entry not caught` then `MARKER` and exits 1. A registry field asserting a newly-false limitation is the exact dishonesty class C1 exists to remove. |
| 6 | pinned-value path (`:269`) | `` red snapshot `corpus/knowledge/round-65-apk-axml-byte-evidence.md` sha256 `cf42cc20…4d05a` — expected verdict over these committed bytes: exit 1 naming entry:41 (the M39 drift); the bytes are the round-66-tip bytes, unchanged since `` | **DEFECT (S2) — the facts hold, the conformance claim overstates.** Every stated fact reproduces (§1.1: hash, exit 1, `entry:41`, round-66 provenance). But PROTOCOL.md:390-397 requires the second evidence to be a committed snapshot **with digest verification by the gate**, "an edited snapshot is `snapshot_tampered` (could-not-evaluate) … and a baseline without digests is reported `unpinned (legacy)`". The gate has no `hashlib`, no `expected.json`, no `snapshot_tampered` path (§1.8); `evaluate()` reads the entry unchecked (`:91`). So the sha256 is registry **prose the instrument does not enforce** — the cell must carry the `unpinned (legacy)` label or the gate must gain the digest check. |
| 7 | measured-against (`:270`) | `` round-67 frozen counter `reports/round-67/measure.py` labels `C7_*` (sha256 `7933c060…bc07e`, pinned in `reports/round-67/claims.md`) `` | **DEFECT (S2) — stale.** The sha256 is correct for the r67 counter (§1.7), but that counter does not print the labels this row's own self-test claim now depends on: the attributed kill and the negative control are round-68 additions (`reports/round-68/measure.py:453` `C7_MUTANT_KILLED_ATTRIBUTED`, `:490-491` `C7_NEG_SPOOF_KILLED` / `C7_NEG_SPOOF_KILLED_ATTRIBUTED`, folded into `HOLDS_OK_V5`/`HOLDS_OK_V6` at `:524,:527`). As written, a reader following the cell lands on an instrument that cannot measure the row's stated property. |
| 8 | write scope (`:271`) | `` read-only over the lane tree; runs the entry's declared commands (argv list, no shell, `python3` first token only); writes nothing outside its own temp dirs `` | **DEFECT (S3) — scope conflation (low).** True of the gate's own code: it opens only the named entry, runs `-B`, and its only write is inside `tempfile.TemporaryDirectory` (`:155`). False as an unconditional claim about the run: the executed command is arbitrary Python — `run_cmd` gates only `argv[0] ∈ ("python3","python",sys.executable)` (`:76`), so `python3 -c 'open(...,"w")'` passes. The cell must distinguish gate writes (temp-only) from entry-command writes (unconstrained, entry is trusted input). |
| 9 | owner (`:272`) | `revenger` | **OK** — lane owns the file (tracked in this repo) and the registry home is this `SKILL.md`. |
| 10 | family note (`:273`) | `deliberately OUTSIDE the `verify_*.py` replay family: the ten-verifier census and `HOLD_REPLAY=10/10` denominator are frozen and this probe does not join them (claims.md §C2)` | **DEFECT (S3) — two faults.** (a) It calls the instrument "**this probe**" while its own `kind` cell (the r67-authoritative one) says `gate` — the residual of routed defect D2, now *inside* the row rather than only in prose (`corpus/lessons/round-67-verifier-spotcheck.md:230-235`). (b) `claims.md §C2` is unversioned; the sentence it means lives at `reports/round-67/claims.md:78-79` ("deliberately **outside** the `verify_*` replay family so the frozen ten-verifier census and `HOLD_REPLAY=10/10` denominator stay untouched"); the round-68 claims state the freeze in Admission-order step 5 and Void conditions, not in a §C2. Substantively true: the filename does not match `verify_*.py`. |

**Header (not a field):** `SKILL.md:260` `## Gate registry (registry home; PROTOCOL.md §Gate standard)` — **DEFECT (S3, pointer)**: no `PROTOCOL.md` exists in this repo (§1.9); the pointer needs the fleet-root path. This matters more than usual: the row's own `:398` cite (`corpus/SOURCES.md:3`) does name a fleet contract, so the lane already has the pattern for out-of-repo pointers.

---

## 3 · Exact edits I would make (not applied — read-only seat)

**E1 — verdict map (`SKILL.md:267`), replace the whole cell:**

```
| verdict map | `0` clean (≥1 block checked, every embedded output line verbatim) · `1` failed (two finding kinds: `drift entry:N embedded output line not in recheck stdout: …` — output the entry's own command does not print; and `drift entry:N command exited RC: …` — a declared command exited non-zero) · `2` could-not-evaluate (no `$ cmd` blocks / unsupported first token / `argv[0]` not `python3`/`python`/`sys.executable` / unreadable entry / command timeout >120 s) · `64` could-not-evaluate (usage: no args, or argv that is not exactly `--self-test` or `--entry <path>`; prints the module docstring) |
```

This is only honest if the gate is repaired in the same revision: wrap `Path(entry_path).read_text(...)` (`:91`) and the `subprocess.run(..., timeout=120)` call (`:78-79`) in `try/except (OSError, subprocess.TimeoutExpired): return None, None` so the existing `problems is None → exit 2` path (`:160-162`) covers them. Without that repair, the `2` clause must instead read "…/ no `$ cmd` blocks / unsupported first token / non-`python3` argv" and a separate line must state the measured truth: "an unreadable entry or a command timeout escapes as an uncaught traceback and exits 1 — i.e. reads as `failed`, a known misclassification." I would take the repair, not the confession.

**E2 — self-test (`SKILL.md:268`), replace the parenthetical:**

```
| self-test | `python3 -B corpus/check_embedded_outputs.py --self-test` (spelling `--self-test`; hermetic temp trees, no network, cwd-independent; asserts clean exit 0, full-run exit 0, and drifted-caught; the drifted case is an explicit `if not caught:` branch at `_self_test` gate:140-145 that prints `self-test: drifted entry not caught` then the registered marker `drifted entry output accepted` as the **last** line and exits 1 — so the frozen mutant `problems += drift(lines, stdout_set, lineno)` → `problems += []` (gate:105, exactly one occurrence) dies **attributably**; round-68 repair of the r67 shadowing defect M45, superseding the 2026-10-24 correction, which is no longer true; the marker literal at gate:36 is frozen because `reports/round-68/measure.py:460`'s spoof-control regex hardcodes it verbatim — a marker edit must move both) |
```

**E3 — measured-against (`SKILL.md:270`), replace the cell:**

```
| measured-against | `reports/round-68/measure.py` sha256 `0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766` labels `C7_GATE_PRESENT` `C7_SELFTEST` `C7_CONTROL_PASS` `C7_MUTANT_KILLED` `C7_MUTANT_KILLED_ATTRIBUTED` `C7_NEG_SPOOF_KILLED` `C7_NEG_SPOOF_KILLED_ATTRIBUTED` `C7_RED_ON_R65_CANDIDATE` `C7_V2_CLEAN` `C7_V3_CLEAN`, folded into `HOLDS_OK_V5`/`HOLDS_OK_V6`; supersedes the round-67 counter (`reports/round-67/measure.py` sha256 `7933c060…bc07e`), which prints neither the attributed nor the negative-control label |
```

**E4 — pinned-value path (`SKILL.md:269`), append one clause (keep every stated fact):**

```
… the bytes are the round-66-tip bytes, unchanged since (`a4c712a`) — **baseline status `unpinned (legacy)`** per PROTOCOL §Gate standard: no `expected.json`, and the gate does not verify this digest (`evaluate()` reads the entry with no hashlib check), so an edited snapshot yields a compared verdict rather than `snapshot_tampered`; the sha256 above is registry prose, not gate-enforced |
```

**E5 — family note (`SKILL.md:273`), replace the cell:**

```
| family note | deliberately OUTSIDE the `verify_*.py` replay family — the filename does not match the `verify_*.py` glob, so the ten-verifier census and the `HOLD_REPLAY=10/10` denominator stay untouched (`reports/round-67/claims.md:78-79`; restated as a freeze in `reports/round-68/claims.md` Admission order step 5 and Void conditions) |
```

This drops the word "probe", completing routed defect D2 in the row it was routed against. Direction matters: reconcile **prose → `kind | gate`**, never the reverse.

**E6 — write scope (`SKILL.md:271`), replace the cell:**

```
| write scope | read-only **for the gate itself**: it reads only the named entry, runs with `-B` (no bytecode), and its only write is inside `tempfile.TemporaryDirectory` (self-test). It runs the entry's declared commands as argv lists, no shell, `argv[0]` restricted to `python3`/`python`/`sys.executable`, cwd = lane root, 120 s timeout — **the executed command's own writes are not constrained by the gate**, so an entry is trusted input and the gate is not a sandbox |
```

**E7 — header (`SKILL.md:260`):**

```
## Gate registry (registry home; fleet `../../PROTOCOL.md:375-420` §Gate standard — no PROTOCOL.md exists in this repo)
```

**E8 (nit, gate not row):** the self-test temp prefix is still `rev-r67-c7-selftest-` (`:155`); cosmetic only, but it is the kind of leftover a reader uses to date the code.

---

## 4 · Residual risk

- **The row's `kind` and its own prose disagree, and the prose is the more quotable.** `family note` says "this probe"; a future seat reconciling *toward* the prose would flip the classification and retro-invalidate C1's scoring basis. Only E5 is acceptable; the row must lead.
- **`C7_CONTROL_PASS` in the counter is a static-grep, not a behavioural control.** `reports/round-68/measure.py:408` computes it as `c7_selftest_ok and C7_MARKER in c7_gate.read_text(...)` — a substring test on the source, not a run. The row's self-test cell (E2) is therefore the only behavioural record that the marker is reachable; if the marker moves to a docstring only, this control stays green while attribution dies. Flagged for `R68CounterIntegrity`, outside the row.
- **`64`'s class:** PROTOCOL.md:381-382 makes an undeclared nonzero code read as could-not-evaluate by default, so the row's omission currently degrades gracefully in interpretation but still violates the declaration duty ("every other code a gate exits … **is declared** in its registry entry"). Do not treat the default as conformance.
- **Self-test fixture independence:** the self-test's expected values are two independently transcribed literals (the reader's `facts` dict in the generated `reader.py` vs `json.dumps({"fact": "a", "v": 1})` at `:118`), which satisfies "independent of the recomputation" (PROTOCOL.md:385-389), but they live in-script rather than in a committed data file. Acceptable; recorded so no seat later claims a committed expectation file exists.
- **C1 interaction (positive):** my independent runs reproduce both behavioural conjuncts of the frozen C1 predicate on the committed HEAD bytes — attributed kill `1/1` (§1.3) and spoof killed `1/1` with attributed `0/1` (§1.4) — matching the repaired gate, not the `measure-before.log:77` red value `0/1`. I measured the gate directly, **not** through the round-68 counter; the counter's own `1/1` reading is `R68CounterIntegrity`'s to establish.

## 5 · Verification gaps (not covered by this seat)

1. **Command-timeout path not executed** — asserting `TimeoutExpired → exit 1` would need a declared `time python3`-style sleeper; my evidence is the code path at gate `:78-79` plus `grep -n "except "` finding no handler (a read, not a run). The `FileNotFoundError → exit 1` sibling of that class **was** executed (§1.5).
2. **Round-68 counter not run** — measured-against staleness is established by reading the label definitions and print sites (`reports/round-68/measure.py:383-460, 490-491, 524-527`) and the red-before receipt, not by a counter execution. Counter execution belongs to `R68CounterIntegrity` / `R68CounterReplay`.
3. **Did not adjudicate C05 or any entry content** — anchors, Q01–Q13 and the README flip are other seats' scope; I ran only the gate's `--entry` verdict over the candidates (§1.6) to confirm the instrument can still separate red from clean.
4. **Admission effect: none.** This is a registry-row review; a ROW-DEFECT is a conformance defect routed to the lane (PROTOCOL.md:412-417), status-neutral — it does not by itself touch C1's or C2's frozen predicates, and E1-E7 change no instrument on the claim surface.
