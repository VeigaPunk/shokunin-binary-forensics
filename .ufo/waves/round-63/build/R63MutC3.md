# R63MutC3 — Independent mutation confirmation of C3 (round 63)

**Seat:** `revenger-r63.R63MutC3` (mutation tester) · **Lane:** `/home/vgpnk/Projects/shokunin/revenger-shokunin`
**Date:** 2026-10-23 · **Scope:** C3 calibration claim only (`C3_RECEIPT_KILLED_ATTRIBUTED`).
**Method:** frozen-mutation replication in isolated `/tmp` copies. **No lane file was created, edited or deleted by this seat.**

---

## 1. Axes named (godspeed posture)

| # | Axis | Frozen criterion | Detector |
|---|---|---|---|
| A1 | Attributed kill — `verify_named_multi_icon_states.py` | C3 1/2 | `python3 -B <tree>/corpus/verify_named_multi_icon_states.py --self-test` (cwd `/`); kill = exit≠0 **and** last combined output line contains `forged receipt` |
| A2 | Attributed kill — `verify_icon_states.py` | C3 2/2 | `python3 -B <tree>/corpus/verify_icon_states.py --self-test` (cwd `/`); same kill rule |
| A3 | Residual debt (NOT in the frozen set) | — | delete the `stdout_sha256` conjunct; report survival only, **no claim extension** |
| A4 | Non-regression | — | pristine control on the same bytes, and preservation-manifest re-check |

Detector semantics are identical to the frozen counter `reports/round-63/measure.py` (`run()` uses
`[sys.executable, "-B", str(tree/"corpus"/script), "--self-test"]`, `cwd="/"`, `timeout=300`; attribution
test is `"forged receipt" in last.lower()`), so a green here is green for L1's counter.

## 2. Bytes under test

The two verifiers were already patched in the lane working tree when this seat started. The executor
(`revenger-r63.R63C3NamedPatch`) confirmed the bytes as final during the run
("final at corpus/verify_named_multi_icon_states.py sha256 a226bf73…; corpus/verify_icon_states.py sha256 7cbd931a…").

```
a226bf73eaba8f9162c763272b5eed4864fc202de23b8d99839c5e19d34cfffe  corpus/verify_named_multi_icon_states.py
7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a  corpus/verify_icon_states.py
```

These are **uncommitted** lane working-tree bytes (`git status`: ` M corpus/verify_icon_states.py`,
` M corpus/verify_named_multi_icon_states.py`). The frozen red-before at base commit
`55bcb6e1aeb4d42923a4e98db6580f67142b41ac` recorded both C3 mutants surviving (exit 0) —
`reports/round-63/measure-before.log`, `C3_RECEIPT_KILLED_ATTRIBUTED=0/2`.

**Mutant-text equivalence.** I did not trust my own hand-written mutant. I ran the frozen counter's own
`mutate_c3()` (copied verbatim out of `reports/round-63/measure.py`) against the final bytes and compared
the result to my literal deletion, byte for byte:

| script | frozen `mutate_c3()` output SHA-256 | my mutant SHA-256 | identical? |
|---|---|---|---|
| `verify_named_multi_icon_states.py` | `21b15fac7b2a5c2f50dff874f9d5be76f75a70742eda3d1a45527806b75cb12a` | `21b15fac7b2a5c2f50dff874f9d5be76f75a70742eda3d1a45527806b75cb12a` | **yes** (0 differing chars) |
| `verify_icon_states.py` | `6cf557650b13d753ef555cc0b3c1883fdecf903c9cb3cbc90e0ce707e7f1acd6` | `6cf557650b13d753ef555cc0b3c1883fdecf903c9cb3cbc90e0ce707e7f1acd6` | **yes** (0 differing chars) |

Frozen clause hit counts were exactly 1 in each file, so the frozen counter's `mutate_c3()` is
*evaluable* on the final bytes (it would have printed "could-not-evaluate" otherwise). The two mutants
exercised below are therefore the **same bytes** the frozen counter will mutate.

## 3. Verdict summary

| # | Mutant | In frozen set? | Exit | Last line | Verdict |
|---|---|---|---|---|---|
| C0a | control — `verify_named_multi_icon_states.py` pristine | — | 0 | `PASS: 142 positive checks; …` | control pass (baseline green) |
| C0b | control — `verify_icon_states.py` pristine | — | 0 | `PASS: 4/4 source-decoded states, …` | control pass (baseline green) |
| M1 | `verify_named_multi_icon_states.py`: delete `receipt['command']==command and ` | **yes** | 1 | `AssertionError: r55: forged receipt accepted` | **KILLED — ATTRIBUTED** |
| M2 | `verify_icon_states.py`: delete ` and receipt['fixture_sha256'] == expected_hash` | **yes** | 1 | `AssertionError: r36: forged receipt accepted` | **KILLED — ATTRIBUTED** |
| M3 | `verify_icon_states.py`: delete the `stdout_sha256` conjunct | **no** (debt probe) | 0 | `PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED` | **SURVIVED** (coverage finding) |

**Both frozen C3 mutants are killed with an attributed `forged receipt` message.** The patches have landed;
the observed red state is the green one. C3 stands at **2/2** on the bytes tested.

## 4. Restoration evidence

Every mutant ran in its own fresh `/tmp` tree copy (`shutil.copytree` of the corpus, `symlinks=True`).
After each mutant run the pristine bytes were written back and the tree re-run:

| tree | file | SHA-256 pristine | SHA-256 mutated | SHA-256 after restore | bytes restored | restored re-run exit |
|---|---|---|---|---|---|---|
| `work/named_c3_frozen` | `verify_named_multi_icon_states.py` | `a226bf73eaba8f9162c763272b5eed4864fc202de23b8d99839c5e19d34cfffe` | `21b15fac7b2a5c2f50dff874f9d5be76f75a70742eda3d1a45527806b75cb12a` | `a226bf73eaba8f9162c763272b5eed4864fc202de23b8d99839c5e19d34cfffe` | yes | 0 (`PASS: 142 positive checks; …`) |
| `work/icon_c3_frozen` | `verify_icon_states.py` | `7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a` | `6cf557650b13d753ef555cc0b3c1883fdecf903c9cb3cbc90e0ce707e7f1acd6` | `7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a` | yes | 0 (`PASS: 4/4 source-decoded states, …`) |
| `work/icon_stdout_unfrozen` | `verify_icon_states.py` | `7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a` | `00744e55dacfccf7983ca45d59cf8001d894330351d782987854350a60620fe5` | `7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a` | yes | 0 (`PASS: 4/4 source-decoded states, …`) |

Lane bytes before and after this seat's whole run are identical:

```
before: 7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a  corpus/verify_icon_states.py
        a226bf73eaba8f9162c763272b5eed4864fc202de23b8d99839c5e19d34cfffe  corpus/verify_named_multi_icon_states.py
after:  7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a  corpus/verify_icon_states.py
        a226bf73eaba8f9162c763272b5eed4864fc202de23b8d99839c5e19d34cfffe  corpus/verify_named_multi_icon_states.py
```

Preservation manifest re-check (`.ufo/waves/round-63/build/preservation-base.sha256`, 455 entries):
**453 OK**, exactly 2 FAILED — and the two failures are the two C3 verifiers themselves, whose bytes the
executor deliberately changed. No `corpus/live` or `corpus/fixtures` byte outside the new round-63 paths
was touched.

## 5. Verbatim transcripts

Command form for every run below (cwd `/`):

```
python3 -B /tmp/revenger-r63-mutc3/work/<tree>/corpus/<script> --self-test
```

### 5.1 Control C0a — `verify_named_multi_icon_states.py`, pristine

```
exit=0
--- STDOUT ---
PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
--- STDERR ---
(empty)
```

### 5.2 Control C0b — `verify_icon_states.py`, pristine

```
exit=0
--- STDOUT ---
PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
--- STDERR ---
(empty)
```

### 5.3 M1 (FROZEN) — `verify_named_multi_icon_states.py`, delete `receipt['command']==command and `

Mutated SHA-256 `21b15fac7b2a5c2f50dff874f9d5be76f75a70742eda3d1a45527806b75cb12a`; literal occurrences = 1.

```
exit=1
--- STDOUT ---
(empty)
--- STDERR ---
Traceback (most recent call last):
  File "/tmp/revenger-r63-mutc3/work/named_c3_frozen/corpus/verify_named_multi_icon_states.py", line 106, in <module>
    if __name__=='__main__': main()
                             ~~~~^^
  File "/tmp/revenger-r63-mutc3/work/named_c3_frozen/corpus/verify_named_multi_icon_states.py", line 84, in main
    rows={r:check(r) for r in EXPECT}; base=rows[55][0]
            ~~~~~^^^
  File "/tmp/revenger-r63-mutc3/work/named_c3_frozen/corpus/verify_named_multi_icon_states.py", line 78, in check
    req(not receipt_ok(forged, command, digest, eid, raw), f'r{r}: forged receipt accepted')
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/revenger-r63-mutc3/work/named_c3_frozen/corpus/verify_named_multi_icon_states.py", line 14, in req
    if not ok: raise AssertionError(msg)
               ^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: r55: forged receipt accepted
--- RESTORED RERUN exit=0 | PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
```

Attribution: the failure is raised by the script's **own** in-script forged-receipt control
(`req(not receipt_ok(forged, …), f'r{r}: forged receipt accepted')`) — the mutant deleted the very conjunct
the control exercises, so the forged receipt is no longer rejected and the control fires. Last line
contains `forged receipt` → **attributed kill**.

### 5.4 M2 (FROZEN) — `verify_icon_states.py`, delete ` and receipt['fixture_sha256'] == expected_hash`

Mutated SHA-256 `6cf557650b13d753ef555cc0b3c1883fdecf903c9cb3cbc90e0ce707e7f1acd6`; literal occurrences = 1.

```
exit=1
--- STDOUT ---
(empty)
--- STDERR ---
Traceback (most recent call last):
  File "/tmp/revenger-r63-mutc3/work/icon_c3_frozen/corpus/verify_icon_states.py", line 181, in <module>
    main()
    ~~~~^^
  File "/tmp/revenger-r63-mutc3/work/icon_c3_frozen/corpus/verify_icon_states.py", line 162, in main
    rows = {r: check_saved(r) for r in EXPECTED}
               ~~~~~~~~~~~^^^
  File "/tmp/revenger-r63-mutc3/work/icon_c3_frozen/corpus/verify_icon_states.py", line 158, in check_saved
    raise AssertionError(f'r{round_id}: forged receipt accepted')
AssertionError: r36: forged receipt accepted
--- RESTORED RERUN exit=0 | PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
```

Attribution: same shape — the script's own forged-receipt control (`forged['fixture_sha256'] = '0'*64`)
is what rejects, and the mutant removed the conjunct it depends on. Last line contains `forged receipt`
→ **attributed kill**.

### 5.5 M3 (NOT IN THE FROZEN SET — residual debt probe) — `verify_icon_states.py`, delete the `stdout_sha256` conjunct

Mutated SHA-256 `00744e55dacfccf7983ca45d59cf8001d894330351d782987854350a60620fe5`; literal occurrences = 1.

```
exit=0
--- STDOUT ---
PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
--- STDERR ---
(empty)
--- RESTORED RERUN exit=0 | PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
```

**The mutant survives.** The `stdout_sha256` conjunct of `receipt_ok()` in `verify_icon_states.py` is still
unguarded by an in-script forged-receipt control: the script forges `fixture_sha256` only, so deleting the
`stdout_sha256` conjunct is invisible to the script's own run.

### 5.6 Supplementary probes naming the same debt precisely (not part of the frozen claim)

| probe | construction | exit | last line |
|---|---|---|---|
| P1 | code intact, receipt `stdout_sha256` forged to `0`*64 in `live/runs/round-37/producer-receipt.json` (receipt SHA `2d8771a1…` → `1f813905…`) | 1 | `AssertionError` (bare, from `receipt_ok`'s stdout conjunct) |
| P2 | code conjunct deleted **and** receipt `stdout_sha256` forged | **0** | `PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED` |
| P3 | same double mutant on the named verifier (delete ` and receipt['stdout_sha256']==H(raw)`, occurrences = 1; forge `live/runs/round-55/receipt.json` `stdout_sha256`) | **0** | `PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.` |

P1 shows the stdout conjunct *is* load-bearing against a forged receipt; P2/P3 show it has **no in-script
control**, so a clause deletion is undetectable from the script's own run. Code restored to the pristine
SHA-256 in both probe trees after the run.

**This is a coverage finding about residual debt, not a change to the C3 contract.** The frozen C3 claim
names exactly two mutants (M1, M2); both are killed. The `stdout_sha256` conjuncts in both files remain
unguarded and are routed debt for a future round — no claim is expanded here.

## 6. Frozen-counter corroboration (read-only, on a `/tmp` tree copy)

I ran the frozen probe `python3 -B reports/round-63/measure.py <tree>` against a `/tmp` copy of the lane
corpus (no lane file was written; the probe copies the corpus into its own temp dirs for each mutant):

```
K_HELD=6/14 score=4.3
K_ROW C06 status=partial
K_HELD_BACKED=6/14
F_COVERAGE=5/8 score=6.2
F_FAMILIES=['native-static', 'javascript', 'archives', 'firmware', 'evm']
FRESH_ROWS=18/18
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py b exit=1 killed :: AssertionError: r47: forged receipt command accepted
MUTANT verify_icon_languages.py d2 exit=1 killed :: AssertionError: r47: receipt
MUTANT verify_multi_icon_states.py control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py b exit=1 killed :: AssertionError: r42: forged receipt command accepted
MUTANT verify_multi_icon_states.py d2 exit=1 killed :: AssertionError: r42: receipt
C2_CONTROLS_PASS=2/2
C2_RECEIPT_B_KILLED=2/2
C2_D2_KILLED=2/2
C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
MUTANT verify_named_multi_icon_states.py control exit=0 pass :: PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
MUTANT verify_named_multi_icon_states.py c3 exit=1 killed :: AssertionError: r55: forged receipt accepted
MUTANT verify_icon_states.py control exit=0 pass :: PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
MUTANT verify_icon_states.py c3 exit=1 killed :: AssertionError: r36: forged receipt accepted
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
HOLD verify_evm_evidence.py exit=0 NEGATIVE REJECTED candidate destination mismatch
HOLD verify_icon_languages.py exit=0 PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
HOLD verify_icon_states.py exit=0 PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
HOLD verify_js_graph_delta.py exit=0 NEGATIVE REJECTED saved graph disagrees with source truth
HOLD verify_multi_icon_states.py exit=0 PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
HOLD verify_named_multi_icon_states.py exit=0 PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
HOLD verify_pe_resources.py exit=0 NEGATIVE REJECTED payload relation mismatch
HOLD verify_saved_evidence.py exit=0 NEGATIVE JS REJECTED: JS: wrong package-main mapping
HOLD verify_semantic_trace.py exit=0 NEGATIVE REJECTED relation differs from source parent
HOLD verify_shape_evidence.py exit=0 NEGATIVE REJECTED changed-property evidence mismatch
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
```

The counter's own C3 lines agree with this seat's independent runs: `C3_CONTROLS_PASS=2/2`,
`C3_RECEIPT_KILLED_ATTRIBUTED=2/2` (was `0/2` in `measure-before.log`). The counter's `HOLD_REPLAY=10/10`
also confirms the ten-verifier census count is unchanged, as the frozen fix shape requires.

## 7. Frozen-fix-shape conformance (byte-level, read-only)

The frozen fix shape requires each script's receipt block to be refactored into a `receipt_ok(...)` helper
**preserving every existing conjunct byte-for-byte**, including the `round_id != 36` evidence-ID exemption in
`verify_icon_states.py`. I diffed `HEAD` against the working tree and counted each original conjunct
literal in both texts:

| conjunct literal | HEAD count | worktree count |
|---|---|---|
| `receipt['command']==command` (named) | 1 | 1 |
| `receipt['exit_code']==0` (named) | 1 | 1 |
| `receipt['fixture_sha256']==digest` (named) | 1 | 1 |
| `receipt['evidence_id']==eid` (named) | 1 | 1 |
| `receipt['stdout_sha256']==H(raw)` (named) | 1 | 1 |
| `isinstance(receipt['duration_seconds'],(float,int))` (named) | 1 | 1 |
| `receipt['duration_seconds']>=0` (named) | 1 | 1 |
| `receipt['exit_code'] == 0` (icon) | 1 | 1 |
| `receipt['fixture_sha256'] == expected_hash` (icon) | 1 | 1 |
| `receipt.get('stdout_sha256', receipt.get('raw_output_sha256')) == sha(raw_bytes)` (icon) | 1 | 1 |
| `receipt['evidence_id'] == evidence_id` (icon) | 1 | 1 |
| `round_id != 36` (icon exemption) | 1 | 1 |

No conjunct was weakened, dropped or reordered; the `round_id != 36` exemption survived the refactor
verbatim. The fix shape is met.

## 8. Harms check

| harm class | result |
|---|---|
| lane file edited by this seat | **none** — all writes were under `/tmp/revenger-r63-mutc3/`; lane SHA-256s identical before/after |
| `corpus/live` / `corpus/fixtures` bytes outside new round-63 paths | **unchanged** — 453/455 manifest entries OK; the 2 mismatches are the two C3 verifiers (executor change, not mine) |
| ten-verifier census count | unchanged — `HOLD_REPLAY=10/10`, `HOLD_CALIBRATION=4/4` |
| existing saved-input assertions | preserved — every conjunct literal present (table in §7); controls exit 0 on both scripts |
| README / QUALITY / registry / MANIFEST / spec files | **not touched** by this seat |
| target execution | none — no firmware payload or vendor image was executed; only Python verifiers over authored bytes |
| claim expansion | none — the surviving M3 mutant is reported as residual debt only; the C3 criterion is unchanged |
| tooling install | **none** — no package, binary or `npx` fetch was needed or performed; Python 3 stdlib only (`hashlib`, `json`, `pathlib`, `re`, `shutil`, `subprocess`) |
| scratch | `/tmp/revenger-r63-mutc3/` — removed after this report lands (transcripts retained in §5) |

## 9. Bottom line for L1

- The two **frozen** C3 mutants are both **killed with an attributed `forged receipt` message**
  (`r55: forged receipt accepted` / `r36: forged receipt accepted`) on the current lane bytes.
  C3 is green at **2/2**, independently confirmed and corroborated by the frozen counter
  (`C3_RECEIPT_KILLED_ATTRIBUTED=2/2`, `C3_CONTROLS_PASS=2/2`, `HOLDS_OK=yes`).
- One **non-frozen** mutant (delete the `stdout_sha256` conjunct) **survives** in
  `verify_icon_states.py`, and the same debt exists in `verify_named_multi_icon_states.py`
  (probes P2/P3). That is residual unguarded debt, routed for a future round — it does not
  affect the frozen C3 criterion and no contract change is implied.
- Nothing in the lane was modified by this seat; all bytes were restored and re-verified green.

---

*Scratch:* `/tmp/revenger-r63-mutc3/` (mutate.py, equiv.py, transcripts.json, equiv.json, tree copies) — removed on completion of this report.
