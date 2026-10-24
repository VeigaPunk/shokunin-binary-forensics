# W2VerifyC3Patches — committed-tip verification of the two C3 verifier patches

**Seat:** `revenger-r63.W2VerifyC3Patches` (reviewer, calibration) · **Lane:** `/home/vgpnk/Projects/shokunin/revenger-shokunin`
**Date:** 2026-10-24 (attempt 1) · **Scope:** C3 calibration only — the two patched verifiers and the frozen C3 counter.
**Frozen contract:** `reports/round-63/claims.md` §C3 (sha256 `aed53241…`) · **Frozen counter:** `reports/round-63/measure.py` (sha256 `3b7fba2d…`) · **Red-before:** `reports/round-63/measure-before.log` (sha256 `4c00f0f9…`).

**Verdict: HOLDS on both scripts.** All five assigned criteria reproduce on the committed tip; the frozen counter prints `C3_CONTROLS_PASS=2/2` and `C3_RECEIPT_KILLED_ATTRIBUTED=2/2` (probe exit 0), and both mutants are killed from the scripts' own designated controls. One **LOW** observability deviation (F1) is reported for L1 adjudication; no finding falsifies C3.

## Axes named

| # | Axis | Detector |
|---|---|---|
| A1 | Patch conformance — the five frozen criteria | `git show 55bcb6e:corpus/<script>` vs tip bytes; AST + full `SequenceMatcher` opcode audit |
| A2 | Frozen counter on committed bytes | `python3 -B reports/round-63/measure.py <git-archive HEAD corpus tree>` |
| A3 | Red-before truthfulness at base | apply the frozen `mutate_c3()` to `55bcb6e` bytes; mutants must exit 0 |
| A4 | Attribution genuineness | mutant traceback frames must name the new in-script controls, not an unrelated failure |

## Bytes attacked

- Lane tip `HEAD = db55bd6488e24e956df5818ae34c2a043d7ddc12` (build `2a34e45` + the integrating C1 candidate commit). Both scripts are committed; worktree blobs equal HEAD blobs (`git hash-object` = `git rev-parse HEAD:<path>`), and the emitted-file sha256s equal the bytes the build wave reviewed.
- `corpus/verify_icon_states.py`: base blob `29f5b272`, tip blob `1836c7cb`, file sha256 `7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a`.
- `corpus/verify_named_multi_icon_states.py`: base blob `9fc54331`, tip blob `6f0e3040`, file sha256 `a226bf73eaba8f9162c763272b5eed4864fc202de23b8d99839c5e19d34cfffe`.
- Frozen files untouched since pre-registration: `git diff --stat 54ab973 HEAD -- reports/round-63/{measure.py,measure-before.log,claims.md}` is empty; no worktree dirty state under `reports/round-63/`.
- Only corpus files modified base→tip: `corpus/SOURCES.md`, the two verifiers. All other corpus changes are additions under round-63 paths (`fixtures/firmware-r63/`, `live/runs/round-63/`, `knowledge/round-63-…`, `lessons/round-63.md`). No `corpus/live`/`corpus/fixtures` byte outside round-63 paths is modified — consistent with the frozen harm clause for this claim's surface.

**Tools:** Python 3.14.8, Git 2.56.0. No installs, no `pacman`, no network. **LSP unavailability recorded:** `xd://lsp` returns "No such tool" (mounted devices: `ast_edit`, `debug`), so caller/definition checks were done with `ast.parse` extraction of `FunctionDef` bodies plus a complete line-opcode audit rather than a language server; for a two-file fully-enumerated diff this is byte-complete proof, not grep inference.

## Criterion results — both scripts

| Criterion | `verify_icon_states.py` | `verify_named_multi_icon_states.py` |
|---|---|---|
| (1) frozen conjunct exactly once inside `receipt_ok` | **HOLDS** | **HOLDS** |
| (2) all pre-existing conjuncts byte-for-byte, incl. `round_id != 36` | **HOLDS** | **HOLDS** |
| (3) exactly one new forged-receipt control, message contains `forged receipt` | **HOLDS** | **HOLDS** |
| (4) no saved-input assertion / EXPECT / PASS *line* changed | **HOLDS** at source level; **F1 LOW** on the interpolated PASS count | **HOLDS** at source level; **F1 LOW** |
| (5) self-test exit 0 from lane root | **HOLDS** | **HOLDS** |

### (1) Frozen conjunct exactly once inside `receipt_ok`

AST extraction (`ast.parse`, `FunctionDef receipt_ok` span), tip bytes:

- `verify_icon_states.py`: helper lines 119–123; frozen clause `receipt['fixture_sha256'] == expected_hash` inside helper = **True**; whole-file literal count = **1**.
- `verify_named_multi_icon_states.py`: helper lines 16–17; frozen clause `receipt['command']==command` inside helper = **True**; whole-file literal count = **1**.

This is exactly the site the frozen `mutate_c3()` regexes target (`measure.py:125-128`); hit count 1 ⇒ the counter is evaluable (no `could-not-evaluate`).

### (2) Every pre-existing receipt conjunct survives byte-for-byte

Exact string equality, base `55bcb6e` vs tip:

- icon — the entire four-line receipt block is byte-identical inside the helper (same indentation):
  ```
      assert receipt['exit_code'] == 0 and receipt['fixture_sha256'] == expected_hash
      assert receipt.get('stdout_sha256', receipt.get('raw_output_sha256')) == sha(raw_bytes)
      if round_id != 36:
          assert receipt['evidence_id'] == evidence_id
  ```
  Equality result: `True`; `round_id != 36` occurrence count base/tip = 1/1. The real receipt check still runs through the helper (`receipt_ok(receipt, expected_hash, evidence_id, raw_bytes, round_id)`, line 150). The pre-existing forged-candidate control in `main()` is untouched (opcode audit).
- named — the 7-conjunct chain is byte-identical (string equality `True`), same order, from `receipt['command']==command` through `receipt['duration_seconds']>=0`; the real check remains `req(receipt_ok(receipt, command, digest, eid, raw),f'r{r} receipt')` with the original message literal `f'r{r} receipt'`.

Full `SequenceMatcher` opcode audit (base → tip): icon has exactly two non-equal regions — insert at base line 119 (helper) and replace of base lines 143–146 (the four receipt lines) — and **no other line differs**; named has exactly two — insert at line 15 (helper) and replace of line 72 (the inline receipt `req`) — with **no other line differs**. `EXPECTED` (icon) and `EXPECT` (named) blocks are byte-identical. Helper parameter order matches every call site (icon: `receipt, expected_hash, evidence_id, raw_bytes, round_id`; named: `receipt, command, digest, eid, raw`).

### (3) Exactly one new forged-receipt control per script

| script | `deepcopy(receipt)` | forge field | `forged receipt` message | base count of `forged receipt` |
|---|---|---|---|---|
| `verify_icon_states.py` | 1 | `forged['fixture_sha256'] = '0'*64` (line 152) | 1 (line 158) | 0 |
| `verify_named_multi_icon_states.py` | 1 | `forged['command'] += ' --forged'` (line 77) | 1 (line 78) | 0 |

Both controls sit in the saved-record path (`check_saved(r)` for r36–r39; `check(r)` for r55–r57) and run once per saved input. The forge fields are exactly the frozen ones; the named control's message is `f'r{r}: forged receipt accepted'`, the icon control's is `f'r{round_id}: forged receipt accepted'`. One control site each — no duplicate or shadow control was added. No other new diagnostic contains `forged receipt`.

### (4) No saved-input assertion / EXPECT / PASS line changed

The opcode audit lists every removed line; they are only the pre-existing receipt lines moved into the helper:

- icon removed: the four receipt block lines (quoted in (2)); nothing else.
- named removed: the single inline `req(receipt['command']==… >=0,f'r{r} receipt')`; nothing else.

Both `print('PASS: …')` statements are byte-identical to base (print-line count 1/1 each, equality `True`). `EXPECTED`/`EXPECT` dict text identical. All other saved-input assertions untouched.

**F1 (LOW)** qualifies this at output level for the named script — see Findings.

### (5) Self-test exit 0 from the lane root

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin
$ python3 -B corpus/verify_icon_states.py --self-test
exit=0  PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
$ python3 -B corpus/verify_named_multi_icon_states.py --self-test
exit=0  PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
```

Same results from the `git archive HEAD corpus` tree (cwd `/`), so the pass does not depend on the worktree.

## Frozen counter receipt (my own run, committed bytes)

`git archive HEAD corpus` → `/tmp`; `TMPDIR` under lane-owned scratch; cwd lane root:

```
$ python3 -B reports/round-63/measure.py /tmp/revenger-r63-c3/tip-tree
MUTANT verify_named_multi_icon_states.py control exit=0 pass :: PASS: 142 positive checks; …
MUTANT verify_named_multi_icon_states.py c3 exit=1 killed :: AssertionError: r55: forged receipt accepted
MUTANT verify_icon_states.py control exit=0 pass :: PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
MUTANT verify_icon_states.py c3 exit=1 killed :: AssertionError: r36: forged receipt accepted
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
PROBE_EXIT=0
```

Incidental counters on the same tip (not admission decisions here): `K_HELD=6/14`, `K_ROW C06 status=partial`, `K_HELD_BACKED=6/14`, `F_COVERAGE=5/8`, `FRESH_ROWS=18/18`. The C2 calibration lines were green too.

## Red-before reproduced at base bytes (A3)

Applying the frozen `mutate_c3()` to the `55bcb6e` scripts on an isolated copy, cwd `/`:

```
BASE-RED verify_named_multi_icon_states.py mutant exit=0 last=PASS: 139 positive checks; …        (survived)
BASE-RED verify_icon_states.py           mutant exit=0 last=PASS: 4/4 source-decoded states, …    (survived)
```

This independently reproduces `measure-before.log`'s `C3_RECEIPT_KILLED_ATTRIBUTED=0/2` — the red baseline is real, and the tip's 2/2 is not a comparison against a fabricated baseline.

## Attribution genuineness (A4)

Both mutants compile (`py_compile` OK — the frozen deletions leave valid syntax), exit 1, and the traceback frames name the new controls, not an unrelated assertion:

- named: frame at `verify_named_multi_icon_states.py:78`,
  `req(not receipt_ok(forged, command, digest, eid, raw), f'r{r}: forged receipt accepted')` → `AssertionError: r55: forged receipt accepted`.
- icon: frame at `verify_icon_states.py:158`,
  `raise AssertionError(f'r{round_id}: forged receipt accepted')` → `AssertionError: r36: forged receipt accepted`.

Both are the first saved round (r55 / r36), i.e. the control fires before any later data could mask it. Under the mutant the genuine-receipt check still passes (deleting a conjunct only makes `receipt_ok` more permissive), so the failure is attributable strictly to the forged-receipt control. A mutant of the same clause at base survives (previous section), proving the control is the delta that buys the kill.

## Findings

### F1 — LOW (observability; L1 decision): named PASS count moved 139 → 142, and a saved `corpus/live` observation no longer reproduces
- **What it attacks:** criterion (4) read at the emitted-output level, and Q09's spirit for reproducible saved observations.
- **Evidence:** base named self-test emits `PASS: 139 positive checks; …`; tip emits `PASS: 142 positive checks; …`. Cause: the new control is counted through the shared `req()` counter (`req(not receipt_ok(forged,…), …)` at line 78), so +1 per round × 3 rounds, and the three negative controls are now counted as "positive checks". `corpus/live/runs/round-58/LEDGER.md:4` and `reviewer.md:13` quote the exact base string `PASS: 139 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size)…`; that saved record is byte-preserved but its quoted observation is no longer reproducible against the current verifier. The print statement source line itself is byte-identical, so criterion (4) holds at source level; the icon PASS line is unaffected.
- **Why not a falsifier:** the frozen harm clause protects corpus bytes (unchanged), Q09 requires saved records stay byte-preserved (they do), and no frozen count or gate consumes the 139/142 field. The C3 target is the attributed kill, which holds.
- **Recommendation (no edit by this seat):** if L1 wants criterion (4) at output level, move the forged check off the `req()` counter (bare `if`/`try` like the icon control, or exclude it from `N`) — one-line change, restores 139 with identical kill behaviour.

### F2 — INFO (residual debt, outside the frozen mutant set): the `stdout_sha256` conjuncts remain unguarded
- **What it attacks:** the calibrative *coverage* of the new controls, not the frozen claim.
- Independently reproduced in isolated copies: deleting ` and receipt['stdout_sha256']==H(raw)` (named) and the `assert receipt.get('stdout_sha256', …) == sha(raw_bytes)` line (icon) both leave exit 0 and a full PASS — the control forges `command` / `fixture_sha256`, so a clause-deletion mutant on the stdout digest survives both scripts' own runs. Matches the build-wave M3/P3 debt; routed for a future round, no claim expansion here.

### F3 — INFO (probe semantics, not a patch defect): attribution is string-based and `C3_CONTROLS_PASS` does not prove a control exists
- **What it attacks:** the strength of the counter as a regression detector.
- `measure.py` attributes on `"forged receipt" in last.lower()` only, and its control counter only checks that the untouched scripts exit 0. Consequently (independently observed by the sibling attack seat and consistent with the frozen text at `measure.py:142-164`) a keyword-bearing crash before the designated control would also score, and a tree with the controls deleted but scripts green would still print `C3_CONTROLS_PASS=2/2`. For the **committed** scripts this is not a live weakness: the kills' traceback frames land on lines 78 / 158, i.e. the designated controls, not an unrelated path. The frozen attribution rule was pre-registered in `claims.md`; this seat does not re-target it.

### F4 — INFO (pre-existing, unchanged by the patch): external absolute-path dependency
- `verify_named_multi_icon_states.py` reads `HIST=/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus` (byte-identical to base). The probe's control run therefore depends on a sibling tree existing on this host; it does here (controls green), but the verifier is not self-contained in a fresh tree. Not introduced by the C3 patch and not a frozen-harms issue.

## Residual risk and verification gaps

- No LSP server/device in this seat; semantic checks are AST + full byte/opcode diffs over the two files, which enumerate every changed line, so no grep-inference is presented as proof. No C3 source rows exist to re-open (S032/S033 belong to C1 and are out of scope).
- The mutant attribution predicate is the frozen string rule (F3); evidence that today's kills are genuine rests on the traceback frames cited above.
- Named verifier's PASS count drift (F1) is the only observable regression found; it is cosmetic and recoverable in one line, but L1 should decide before quoting the counter receipt in an entry.
- C1/C2 adjudication and the incidental `K_*`/`F_*` numbers printed by the counter are outside this leaf; they are reported only as observed output. Concurrent uncommitted edits by other seats were visible in `git status corpus/` during this run (`corpus/lessons/round-63.md`, later also `corpus/SOURCES.md`); they are not mine, not committed, and do not touch the two C3 blobs — the worktree blob hashes of both verifiers still equal HEAD at my final check (`1836c7cb…`, `6f0e3040…`).
- Scratch `/tmp/revenger-r63-c3/` (extracted trees, mutants, counter log) was removed after this report landed; all quoted outputs are reproduced above.

## Bounds compliance

Wrote only this report path and `/tmp/revenger-r63-c3/` scratch; no commit, no git/jj mutation, no index change, no lane file edit, no spec/registry/manifest edit, no sibling-lane access, no target execution (verifier self-tests and the frozen counter only), no tool installs (Python 3.14.8 / Git 2.56.0 existing), no `pacman`.
