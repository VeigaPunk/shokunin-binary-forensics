# W2MutC3Final — frozen C3 mutants re-run against the COMMITTED verifiers at the lane tip

**Seat:** `revenger-r63.W2MutC3Final` (mutation-tester) · **Lane:** `/home/vgpnk/Projects/shokunin/revenger-shokunin`
**Date:** 2026-10-24 · **Axis:** calibration · **Claim attacked:** C3 (`C3_RECEIPT_KILLED_ATTRIBUTED` 2/2)
**Target attacked:** the two frozen C3 clause-deletion mutants re-run on the **committed** verifier bytes at the
lane tip, plus the two **non-frozen residual-debt** `stdout_sha256` mutants.
**Method:** isolated `/tmp` copies of `git archive HEAD corpus`. **No lane file was created, edited or deleted by
this seat** except this report. No target execution, no model arguments, no network, no pacman, no installs.

---

## 0. Verdict (one line per item)

| # | Item | Expected | Observed | Verdict |
|---|---|---|---|---|
| F1 | Frozen C3 mutant — `verify_named_multi_icon_states.py`: delete `receipt['command']==command and ` | exit≠0, last line contains `forged receipt` | exit **1**, last line `AssertionError: r55: forged receipt accepted` | **KILLED — ATTRIBUTED** |
| F2 | Frozen C3 mutant — `verify_icon_states.py`: delete ` and receipt['fixture_sha256'] == expected_hash` | exit≠0, last line contains `forged receipt` | exit **1**, last line `AssertionError: r36: forged receipt accepted` | **KILLED — ATTRIBUTED** |
| D1 | Residual debt (NOT frozen) — `verify_named_multi_icon_states.py`: delete ` and receipt['stdout_sha256']==H(raw)` | survive (routed debt, not claimed) | exit **0**, `PASS: 142 positive checks; …` | **SURVIVED — coverage finding, routed** |
| D2 | Residual debt (NOT frozen) — `verify_icon_states.py`: delete the `stdout_sha256` assert | survive (routed debt, not claimed) | exit **0**, `PASS: 4/4 source-decoded states, …` | **SURVIVED — coverage finding, routed** |

**C3 stands at 2/2 attributed on the committed bytes.** Neither frozen mutant was
rejected for an unrelated reason: the rejection message is the forged-receipt control's own
(`forged receipt accepted`), raised by the *in-script* control, not by an incidental assertion.

---

## 1. Bytes under test — committed at the lane tip, not the working tree

The lane tip is `db55bd6488e24e956df5818ae34c2a043d7ddc12`
(`round-63: C1 candidate entry (H1-H7/N1-N3 corrected), SOURCES S032+S033, round-63 lesson; README still partial pending falsify wave`).
The C3 patches landed in the preceding commit `2a34e45`. I exported the committed tree with
`git archive HEAD corpus` into `/tmp/revenger-r63-mutc3/base/` — never the working tree — so the bytes
attacked are exactly the committed bytes.

```
committed (git show HEAD:corpus/...)          ==  worktree  ==  base archive
a226bf73eaba8f9162c763272b5eed4864fc202de23b8d99839c5e19d34cfffe  corpus/verify_named_multi_icon_states.py
7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a  corpus/verify_icon_states.py
```

For reference, the red-before base commit `55bcb6e1aeb4d42923a4e98db6580f67142b41ac` carried different bytes
(`b62441d5…` / `acbf47bb…`) with **no** `receipt_ok(...)` helper and no in-script control — i.e. the
frozen mutant sites did not exist in the base shape.

**Clause-match count = exactly 1 in each final file** (required by the frozen fix shape, `claims.md` §C3):
`receipt['command']==command` → 1 occurrence in `verify_named_multi_icon_states.py`;
`receipt['fixture_sha256'] == expected_hash` → 1 occurrence in `verify_icon_states.py`.
The frozen counter's own `mutate_c3()` is therefore *evaluable* on these bytes.

**Mutant-byte equivalence with the frozen counter.** I did not trust my own hand-written deletion. I
reimplemented the frozen counter's `mutate_c3()` verbatim from `reports/round-63/measure.py` (same two
regex forms, `r"\s*and\s+" + clause.pattern` then `clause.pattern + r"\s+and\s+"`) and compared the
produced bytes with my literal deletion:

| script | frozen `mutate_c3()` output SHA-256 | my literal-deletion SHA-256 | identical? |
|---|---|---|---|
| `verify_named_multi_icon_states.py` | `21b15fac7b2a5c2f50dff874f9d5be76f75a70742eda3d1a45527806b75cb12a` | `21b15fac7b2a5c2f50dff874f9d5be76f75a70742eda3d1a45527806b75cb12a` | **yes** |
| `verify_icon_states.py` | `6cf557650b13d753ef555cc0b3c1883fdecf903c9cb3cbc90e0ce707e7f1acd6` | `6cf557650b13d753ef555cc0b3c1883fdecf903c9cb3cbc90e0ce707e7f1acd6` | **yes** |

These two hashes are also byte-identical to the hashes recorded independently by the build seat
`.ufo/waves/round-63/build/R63MutC3.md` §2. Three independent replications agree on the same mutant bytes.

**Detector.** Identical to the frozen counter's `run()`: `[sys.executable, "-B", str(tree/"corpus"/script),
"--self-test"]`, `cwd="/"`, `timeout=300`; attribution test is `"forged receipt" in last.lower()` where
`last` is the last line of `(stdout + stderr).strip().splitlines()`. A green here is green for L1's counter.

---

## 2. Frozen C3 mutants — transcripts (verbatim)

### 2.1 F1 — `verify_named_multi_icon_states.py`, delete `receipt['command']==command and `

Mutation applied to the copy (diff against the committed file, verbatim):

```
17c17
<  return receipt['command']==command and receipt['exit_code']==0 and receipt['fixture_sha256']==digest and receipt['evidence_id']==eid and receipt['stdout_sha256']==H(raw) and isinstance(receipt['duration_seconds'],(float,int)) and receipt['duration_seconds']>=0
---
>  return receipt['exit_code']==0 and receipt['fixture_sha256']==digest and receipt['evidence_id']==eid and receipt['stdout_sha256']==H(raw) and isinstance(receipt['duration_seconds'],(float,int)) and receipt['duration_seconds']>=0
```

Control run (pristine committed bytes):

```
  file sha256 before = a226bf73eaba8f9162c763272b5eed4864fc202de23b8d99839c5e19d34cfffe
  file sha256 after  = a226bf73eaba8f9162c763272b5eed4864fc202de23b8d99839c5e19d34cfffe
  exit = 0   attributed(forged receipt in last line) = False
  ---- stdout (verbatim) ----
PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
  ---- stderr (verbatim) ----
  ---- last line ----
  PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
```

Mutant run:

```
SCENARIO verify_named_multi_icon_states.py :: c3-mutant :: ran clause_hits=1
  file sha256 before = a226bf73eaba8f9162c763272b5eed4864fc202de23b8d99839c5e19d34cfffe
  file sha256 after  = 21b15fac7b2a5c2f50dff874f9d5be76f75a70742eda3d1a45527806b75cb12a
  exit = 1   attributed(forged receipt in last line) = True
  stdout_has_forged=False stderr_has_forged=True
  ---- stdout (verbatim) ----
  ---- stderr (verbatim) ----
Traceback (most recent call last):
  File "/tmp/revenger-r63-mutc3/work/verify_named_multi_icon_states__c3-mutant/corpus/verify_named_multi_icon_states.py", line 106, in <module>
    if __name__=='__main__': main()
                             ~~~~^^
  File "/tmp/revenger-r63-mutc3/work/verify_named_multi_icon_states__c3-mutant/corpus/verify_named_multi_icon_states.py", line 84, in main
    rows={r:check(r) for r in EXPECT}; base=rows[55][0]
            ~~~~~^^^
  File "/tmp/revenger-r63-mutc3/work/verify_named_multi_icon_states__c3-mutant/corpus/verify_named_multi_icon_states.py", line 78, in check
    req(not receipt_ok(forged, command, digest, eid, raw), f'r{r}: forged receipt accepted')
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/revenger-r63-mutc3/work/verify_named_multi_icon_states__c3-mutant/corpus/verify_named_multi_icon_states.py", line 14, in req
    if not ok: raise AssertionError(msg)
               ^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: r55: forged receipt accepted
  ---- last line ----
  AssertionError: r55: forged receipt accepted
```

**Attribution isolation (why this is the frozen conjunct's kill, not an incidental failure).**
The traceback frame is `verify_named_multi_icon_states.py:78`, i.e. the in-script forged-receipt control
`req(not receipt_ok(forged, command, digest, eid, raw), f'r{r}: forged receipt accepted')`. The forged copy
differs from the real receipt in exactly one field (`command += ' --forged'`); the real receipt passed every
conjunct earlier in the same run; therefore the only conjunct that can reject the forgery is the deleted
`receipt['command']==command`. The rejection is the control's own message, not a crash and not an unrelated
assertion.

### 2.2 F2 — `verify_icon_states.py`, delete ` and receipt['fixture_sha256'] == expected_hash`

Mutation applied to the copy (diff against the committed file, verbatim):

```
120c120
<     assert receipt['exit_code'] == 0 and receipt['fixture_sha256'] == expected_hash
---
>     assert receipt['exit_code'] == 0
```

Control run (pristine committed bytes):

```
  file sha256 before = 7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a
  file sha256 after  = 7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a
  exit = 0   attributed(forged receipt in last line) = False
  ---- stdout (verbatim) ----
PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
  ---- stderr (verbatim) ----
  ---- last line ----
  PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
```

Mutant run:

```
SCENARIO verify_icon_states.py :: c3-mutant :: ran clause_hits=1
  file sha256 before = 7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a
  file sha256 after  = 6cf557650b13d753ef555cc0b3c1883fdecf903c9cb3cbc90e0ce707e7f1acd6
  exit = 1   attributed(forged receipt in last line) = True
  stdout_has_forged=False stderr_has_forged=True
  ---- stdout (verbatim) ----
  ---- stderr (verbatim) ----
Traceback (most recent call last):
  File "/tmp/revenger-r63-mutc3/work/verify_icon_states__c3-mutant/corpus/verify_icon_states.py", line 181, in <module>
    main()
    ~~~~^^
  File "/tmp/revenger-r63-mutc3/work/verify_icon_states__c3-mutant/corpus/verify_icon_states.py", line 162, in main
    rows = {r: check_saved(r) for r in EXPECTED}
               ~~~~~~~~~~~^^^
  File "/tmp/revenger-r63-mutc3/work/verify_icon_states__c3-mutant/corpus/verify_icon_states.py", line 158, in check_saved
    raise AssertionError(f'r{round_id}: forged receipt accepted')
AssertionError: r36: forged receipt accepted
  ---- last line ----
  AssertionError: r36: forged receipt accepted
```

**Attribution isolation.** The frame is `verify_icon_states.py:158`, the `else:` branch of the in-script
forged-receipt control — i.e. the forged receipt was *accepted* by `receipt_ok(...)` and the control
explicitly raised. With `fixture_sha256` deleted from `receipt_ok`, the forged `fixture_sha256 = '0'*64`
no longer trips any conjunct; the `round_id != 36` evidence-ID exemption is untouched by this mutation and
plays no part in the kill (round 36 is the row that fired).

---

## 3. Residual debt mutants (NOT in the frozen set) — still survive

### 3.1 D1 — `verify_named_multi_icon_states.py`: delete ` and receipt['stdout_sha256']==H(raw)`

```
### DEBT MUTANT 1 verify_named_multi_icon_states.py: delete ` and receipt['stdout_sha256']==H(raw)` (hits=1) ###
  before sha256 = a226bf73eaba8f9162c763272b5eed4864fc202de23b8d99839c5e19d34cfffe
  after  sha256 = 3735a6f34d6f85d6f59007882e78f1f97332004c33a42e08137b36783bcc078a
  exit=0  SURVIVED=True  last_line='PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.'
  ---- stdout ----
PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
  ---- stderr ----
```

Diff (verbatim), showing the `stdout_sha256` conjunct removed and **nothing else** changed:

```
17c17
<  return receipt['command']==command and receipt['exit_code']==0 and receipt['fixture_sha256']==digest and receipt['evidence_id']==eid and receipt['stdout_sha256']==H(raw) and isinstance(receipt['duration_seconds'],(float,int)) and receipt['duration_seconds']>=0
---
>  return receipt['command']==command and receipt['exit_code']==0 and receipt['fixture_sha256']==digest and receipt['evidence_id']==eid and isinstance(receipt['duration_seconds'],(float,int)) and receipt['duration_seconds']>=0
```

### 3.2 D2 — `verify_icon_states.py`: delete the `stdout_sha256` conjunct

```
### DEBT MUTANT 2 verify_icon_states.py: delete the stdout_sha256 assert line (removed 1 line(s)) ###
  before sha256 = 7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a
  after  sha256 = 00744e55dacfccf7983ca45d59cf8001d894330351d782987854350a60620fe5
  exit=0  SURVIVED=True  last_line='PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED'
  ---- stdout ----
PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
  ---- stderr ----
```

Diff (verbatim):

```
121d120
<     assert receipt.get('stdout_sha256', receipt.get('raw_output_sha256')) == sha(raw_bytes)
```

**Reading of D1/D2.** Both survive because the frozen in-script controls forge exactly one field each
(`command` for named, `fixture_sha256` for icon_states). A deletion of the `stdout_sha256` conjunct removes
a check that no in-script control exercises, so the self-test stays green. This is a **detector-coverage
finding, not a falsification of C3** — C3's frozen sentence names one conjunct per script and claims
exactly those two kills, both of which are observed. This debt is routed (lesson M35 / §Routed debt), and
this seat does not extend the claim or change the contract.

---

## 4. Supplementary coverage census — every other receipt conjunct in the two committed verifiers

Not part of the frozen claim; run to scope the residual debt honestly. Each conjunct was deleted alone
(and, where the conjunct was first in its chain, the deletion form `clause and` was used so the mutation
is a real semantic deletion, not a syntax error). Every mutant ran on a fresh copy of the committed tree.

```
SWEEP verify_named_multi_icon_states.py
  CONTROL exit=0 last='PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.'
  command          hits=0 exit=1 KILLED  before=a226bf73eaba8f91 after=21b15fac7b2a5c2f
      last='AssertionError: r55: forged receipt accepted'
  exit_code        hits=1 exit=0 SURVIVED(no in-script control)  before=a226bf73eaba8f91 after=d7a7294584f58049
      last='PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.'
  fixture_sha256   hits=1 exit=0 SURVIVED(no in-script control)  before=a226bf73eaba8f91 after=2bb816d260c83521
      last='PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.'
  evidence_id      hits=1 exit=0 SURVIVED(no in-script control)  before=a226bf73eaba8f91 after=747a2a0ecaf277fb
      last='PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.'
  stdout_sha256    hits=1 exit=0 SURVIVED(no in-script control)  before=a226bf73eaba8f91 after=3735a6f34d6f85d6
      last='PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.'
SWEEP verify_icon_states.py
  CONTROL exit=0 last='PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED'
  exit_code        hits=0 exit=0 SURVIVED(no in-script control)  before=7cbd931a3a8ef639 after=2df00b9d7d4c02f2
      last='PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED'
  fixture_sha256   hits=1 exit=1 KILLED  before=7cbd931a3a8ef639 after=6cf557650b13d753
      last='AssertionError: r36: forged receipt accepted'
```

Two further named conjuncts of `verify_named_multi_icon_states.py` (`isinstance(receipt['duration_seconds'],(float,int))`
and `receipt['duration_seconds']>=0`) and the `evidence_id` conjunct of `verify_icon_states.py` were also tested:

```
  duration_isinstance    exit=0 SURVIVED(no in-script control)
      after =080d3a8cf799a0eaee3f51d31ae95c429525bc26f8cd8711f35c34f1914917a6
      last='PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.'
  duration_nonneg        exit=0 SURVIVED(no in-script control)
      after =a22575d577b88205e8f8248fce7768a24fa39b563556eaf3e1bbc7c2a73df41f
      last='PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.'
```

```
  evidence_id_assert_line        hits=1 exit=1 KILLED
      last="IndentationError: expected an indented block after 'if' statement on line 122"
  stdout_sha256_assert_line        hits=1 exit=0 SURVIVED(no in-script control)
      after =b9ba88d559711bee977fb334e8b6a55487cdd3f0de259ef588c77d07a2cf906b
      last='PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED'
```

The `evidence_id` "KILLED" above is a **syntax artifact, not a kill** — deleting the `assert` line inside
`if round_id != 36:` leaves an empty block and the file does not parse. Re-run with the conjunct
*neutralized* (`pass` in place of the assert, semantics preserved, file still parses):

```
neutralize hits=1  before=7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a
  after =75111ff62264ef350075d8891d8b56768c08045dfbcd2216c8ee8e453ffe0e77
  exit=0  SURVIVED(no in-script control)
  last='PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED'
```

**Census result.** Of the 10 deletable receipt-identity conjuncts across the two committed verifiers, the
in-script forged-receipt controls detect exactly **2** — the two the frozen C3 sentence names. The other
**8** (`exit_code` ×2, `fixture_sha256` in named, `evidence_id` ×2, `stdout_sha256` ×2, `duration_seconds` ×2
in named) survive clause deletion. The label `C3_RECEIPT_KILLED_ATTRIBUTED` therefore covers 2 of 10
conjuncts; this is the same scope-honesty observation the round-61 critic raised for C2, and it is a
**coverage finding for the routed debt**, not grounds to weaken or widen C3.

---

## 5. Restoration evidence

Every mutant ran in its own fresh `/tmp` copy (`shutil.copytree` of the committed `corpus`, `symlinks=True`);
the lane was never a mutation target. For each frozen mutant and each debt mutant I mutated → ran → wrote
the **exact pristine bytes** back → re-ran the same detector on the restored copy:

```
RESTORE verify_named_multi_icon_states.py (frozen C3 mutant, clause_hits=1)
  pristine sha256   = a226bf73eaba8f9162c763272b5eed4864fc202de23b8d99839c5e19d34cfffe
  mutated  sha256   = 21b15fac7b2a5c2f50dff874f9d5be76f75a70742eda3d1a45527806b75cb12a
  restored sha256   = a226bf73eaba8f9162c763272b5eed4864fc202de23b8d99839c5e19d34cfffe   identical_to_pristine=True
  control run : exit=0 last='PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.'
  mutant  run : exit=1 last='AssertionError: r55: forged receipt accepted'
  restored run: exit=0 last='PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.'  back_to_control=True
RESTORE verify_icon_states.py (frozen C3 mutant, clause_hits=1)
  pristine sha256   = 7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a
  mutated  sha256   = 6cf557650b13d753ef555cc0b3c1883fdecf903c9cb3cbc90e0ce707e7f1acd6
  restored sha256   = 7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a   identical_to_pristine=True
  control run : exit=0 last='PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED'
  mutant  run : exit=1 last='AssertionError: r36: forged receipt accepted'
  restored run: exit=0 last='PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED'  back_to_control=True
RESTORE verify_named_multi_icon_states.py (residual stdout_sha256 debt mutant, n=1)
  pristine sha256   = a226bf73eaba8f9162c763272b5eed4864fc202de23b8d99839c5e19d34cfffe
  mutated  sha256   = 3735a6f34d6f85d6f59007882e78f1f97332004c33a42e08137b36783bcc078a
  restored sha256   = a226bf73eaba8f9162c763272b5eed4864fc202de23b8d99839c5e19d34cfffe   identical_to_pristine=True
  control run : exit=0 last='PASS: 142 positive checks; …'
  mutant  run : exit=0 last='PASS: 142 positive checks; …'  SURVIVED=True
  restored run: exit=0 last='PASS: 142 positive checks; …'  back_to_control=True
RESTORE verify_icon_states.py (residual stdout_sha256 debt mutant, n=1)
  pristine sha256   = 7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a
  mutated  sha256   = 00744e55dacfccf7983ca45d59cf8001d894330351d782987854350a60620fe5
  restored sha256   = 7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a   identical_to_pristine=True
  control run : exit=0 last='PASS: 4/4 source-decoded states, …'
  mutant  run : exit=0 last='PASS: 4/4 source-decoded states, …'  SURVIVED=True
  restored run: exit=0 last='PASS: 4/4 source-decoded states, …'  back_to_control=True
```

**Lane bytes before and after this seat's entire run are identical** (`sha256sum` on the lane paths):

```
before: a226bf73eaba8f9162c763272b5eed4864fc202de23b8d99839c5e19d34cfffe  corpus/verify_named_multi_icon_states.py
        7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a  corpus/verify_icon_states.py
after:  a226bf73eaba8f9162c763272b5eed4864fc202de23b8d99839c5e19d34cfffe  corpus/verify_named_multi_icon_states.py
        7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a  corpus/verify_icon_states.py
```

`git status --porcelain corpus/live corpus/fixtures` → empty (no saved record or fixture byte touched).
`git rev-parse HEAD` → `db55bd6488e24e956df5818ae34c2a043d7ddc12` (unchanged; no git/jj mutation by this seat).
The only working-tree change under `corpus/` is ` M corpus/lessons/round-63.md` — **not mine**: it is another
seat's in-flight lesson edit (mtime 2026-10-24 00:01:02, after this seat started); I did not touch it, and I
am flagging it only so the integrator does not attribute it to this seat.

---

## 6. Independent counter re-run on the committed tree (cross-check, not a substitute)

I re-ran the **frozen** counter myself on a `git archive HEAD corpus` tree (never on the working tree),
`TMPDIR` under lane-owned scratch:

```
K_HELD=6/14 score=4.3
K_ROW C06 status=partial
K_HELD_BACKED=6/14
F_COVERAGE=5/8 score=6.2
F_FAMILIES=['native-static', 'javascript', 'archives', 'firmware', 'evm']
FRESH_ROWS=18/18
MUTANT verify_named_multi_icon_states.py control exit=0 pass :: PASS: 142 positive checks; …
MUTANT verify_named_multi_icon_states.py c3 exit=1 killed :: AssertionError: r55: forged receipt accepted
MUTANT verify_icon_states.py control exit=0 pass :: PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
MUTANT verify_icon_states.py c3 exit=1 killed :: AssertionError: r36: forged receipt accepted
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
```

(`C2_CONTROLS_PASS=2/2`, `C2_RECEIPT_B_KILLED=2/2`, `C2_D2_KILLED=2/2`,
`C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2` were also printed and green.)

Red-before cross-check on the base commit `55bcb6e` corpus (same counter, same command):

```
K_HELD=6/14 score=4.3
K_HELD_BACKED=6/14
F_COVERAGE=4/8 score=5.0
MUTANT verify_named_multi_icon_states.py control exit=0 pass :: PASS: 139 positive checks; …
MUTANT verify_named_multi_icon_states.py c3 exit=0 pass :: PASS: 139 positive checks; …
MUTANT verify_icon_states.py control exit=0 pass :: PASS: 4/4 source-decoded states, …
MUTANT verify_icon_states.py c3 exit=0 pass :: PASS: 4/4 source-decoded states, …
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=0/2
```

This reproduces `reports/round-63/measure-before.log` (`C3_RECEIPT_KILLED_ATTRIBUTED=0/2`) from the base
bytes, independently. The red→green transition for C3 is therefore observed end-to-end on committed bytes:
**0/2 at base → 2/2 at the lane tip.**

Note for the integrator: at the committed tip the counter prints `K_HELD_BACKED=6/14` with
`K_ROW C06 status=partial` and `F_COVERAGE=5/8`. The C1 admission (README C06 `partial → held`, needed for
K 7/14) is L1's and the falsify wave's business, gated on the fresh-seat Q01–Q13 pass decisions; this seat
did not attempt it. F 5/8 is already met by the committed tree. This seat's calibration verdict is
unaffected by the C1 status.

---

## 7. Findings for the integrator

1. **C3 is not falsified.** Both frozen mutants are killed *and* attributed on the committed bytes at
   `db55bd6`: `AssertionError: r55: forged receipt accepted` and `AssertionError: r36: forged receipt
   accepted`, exit 1 both, last line contains `forged receipt`. The frozen counter agrees:
   `C3_RECEIPT_KILLED_ATTRIBUTED=2/2`, `C3_CONTROLS_PASS=2/2`, `HOLDS_OK=yes`.
2. **The kills are attributable, not incidental.** Each rejection comes from the in-script forged-receipt
   control itself (`verify_named_multi_icon_states.py:78`, `verify_icon_states.py:158`), on a receipt copy
   that differs in exactly one field, after the real receipt already passed every conjunct in the same run.
3. **Residual debt survives as expected (routed, not claimed).** The `stdout_sha256` conjunct deletion
   survives in **both** scripts. The round-63 lesson's M35 mistake row and the §Routed-debt row name only the
   `verify_icon_states.py` conjunct (`stdout_sha256` in `verify_icon_states.py`); the
   `verify_named_multi_icon_states.py` `stdout_sha256` conjunct is **also** unguarded — my D1 is a
   single-variable clause deletion with the receipt untouched (`3735a6f3…`, exit 0,
   `PASS: 142 positive checks; …`), so it isolates the clause rather than a receipt change. The build seat's
   own probe P3 (`.ufo/waves/round-63/build/R63MutC3.md` §5.6) reached the same verdict for the named
   script but coupled it with a forged receipt; my D1 shows the clause deletion alone is already
   undetectable, i.e. the debt is one conjunct wider than the routed-debt row states. This is a coverage
   finding for L1 to route, not a contract change — C3's frozen sentence names one conjunct per script and
   both named kills are observed.
4. **Scope honesty, quantified.** 2 of 10 deletable receipt-identity conjuncts across the two committed
   verifiers are detected by the in-script controls; 8 survive. The two detected ones are exactly the two the
   frozen sentence names, so the criterion is true as written — but the label
   `C3_RECEIPT_KILLED_ATTRIBUTED` should not be read as "the receipt checks are deletion-sensitive".
   Same shape as the round-61 C2 scope-honesty finding.
5. **A "kill" that is a syntax error is not a kill.** Deleting the `assert receipt['evidence_id'] == ...`
   line from `verify_icon_states.py` yields `IndentationError` (exit 1) — a crash, not an attributed kill.
   Neutralizing the conjunct instead shows it genuinely survives. Recorded so the integrator does not count
   the crash as coverage.

---

## 8. Tooling, scratch, and hygiene

- **No installs.** No tool was missing; nothing was installed, so no tool/version/channel row is required.
- **No pacman** (host-wide pause honored). No network, no target execution, no model arguments.
- **Scratch:** all work under `/tmp/revenger-r63-mutc3/` (base archive, per-scenario copies, driver scripts,
  transcript files). **Removed after this report landed** (see §5 for the hashes that make the removal
  auditable — the transcripts are reproduced verbatim above).
- **Lane bounds honored:** no subagent dispatch; no edit to `.ufo/waves/round-63/` spec/registry files, no
  `MANIFEST.json`, no fleet-repo file, no sibling lane, no lane jj state, no lane Git index. The only file
  this seat wrote in the lane is this report:
  `.ufo/waves/round-63/falsify/W2MutC3Final.md`.
- **Reusable artifacts** (all under the removed scratch root; regenerate with the commands in §2–§4):
  `base/` (committed archive), `basecommit/` (base-commit archive), `work*/` (per-scenario copies),
  `driver.py` … `driver7.py`, `driver*-out.txt`, `measure-on-committed.txt`, `measure-on-base.txt`.
