# R64MutIcon — regression mutation sweep on the final patched tree

Status: **all six frozen prior mutants are killed with attribution on the final bytes**
(snapshot B). One **transient mid-edit regression** existed in a 77-second window
(01:17:08 → 01:18:25) and was repaired by the file's owner before the final bytes; it is
recorded as finding F1 for L1 adjudication, not as a final-tree failure.

## Tree identity (absolute paths)

Swept copy: `/tmp/revenger-r64-muticon/base2_corpus` = byte copy of
`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus` at 2026-10-24 01:18:25–01:19.

| file | sha256 (final bytes) |
|---|---|
| corpus/verify_icon_languages.py | `a2fd347e6379bee4d794d008aa0d1ea8b7823a1c0557775318a22a80f9239aa3` |
| corpus/verify_multi_icon_states.py | `9345cb8c91741e36d1d88805cbe1b2fef4a8c890f96a26dd7ea626909b6a0f7e` |
| corpus/verify_named_multi_icon_states.py | `a226bf73eaba8f9162c763272b5eed4864fc202de23b8d99839c5e19d34cfffe` |
| corpus/verify_icon_states.py | `7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a` |
| corpus/live/runs/round-47/producer-receipt.json | `3b5d3bdaad18cf7ab0c34643851e205353a979dff08133f48f54f0617e558ac5` |
| corpus/live/runs/round-42/producer-receipt.json | `05bf8bf6dd33719a3db6f6d9ff29a894d8191c627e14c7e746611f7c882119de` |

Pre-patch comparator bytes (`git show HEAD:…`, read-only): `verify_icon_languages.py`
`0f781c6a216bfdaa9cc1ab9b9fe8ae3ab9cb8a79d00ed56c4f94282c80a8efbd`,
`verify_multi_icon_states.py` `0179e93f8bec17d5f4b60047f167ad26aa803a84440e98329fd8a8f2ea7a176d`.

## Method

1. Frozen counter, run exactly as the contract states:
   `cd / && TMPDIR=/tmp/revenger-r64-muticon/tmp python3 -B
   /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure.py
   /tmp/revenger-r64-muticon/tree2` → **exit 0**.
2. Independent harness `/tmp/revenger-r64-muticon/sweep.py`: fresh `copytree` per case;
   **pristine run first** (baseline must pass), then the frozen mutation (regexes copied
   verbatim from `measure.py`; d2 rewrites the receipt with
   `json.dumps(data, indent=2) + "\n"` exactly as the counter), mutant run, **exact-byte
   restore**, restored run. Per-case sha256 of the mutated file (and for d2, script +
   receipt) before mutation, after mutation, and after restore; `restored_eq` compares the
   full 64-hex digests.
3. Lane files were never written by this seat. Post-sweep `sha256sum` of the four scripts
   and both receipts equals the table above (identical to pre-sweep values).

## Results — frozen prior mutants on final bytes

| # | mutant | expected detector (frozen attribution) | actual exit | last line | verdict |
|---|---|---|---|---|---|
| 1 | `verify_icon_languages.py` **b** — delete `receipt['command']==command` conjunct + connecting `and` | non-zero **and** last endswith `forged receipt command accepted` | **1** | `AssertionError: r47: forged receipt command accepted` | **KILLED, attributed** |
| 2 | `verify_multi_icon_states.py` **b** — same conjunct deletion | non-zero and endswith `forged receipt command accepted` | **1** | `AssertionError: r42: forged receipt command accepted` | **KILLED, attributed** |
| 3 | `verify_icon_languages.py` **d2** — round-47 receipt `command += ' --forged'` | non-zero (frozen class: raw kill; the attributed counter covers b only) | **1** | `AssertionError: r47: receipt` | **KILLED** |
| 4 | `verify_multi_icon_states.py` **d2** — round-42 receipt `command += ' --forged'` | non-zero (raw kill) | **1** | `AssertionError: r42: receipt` | **KILLED** |
| 5 | `verify_named_multi_icon_states.py` **c3** — delete `receipt['command']==command` conjunct + `and` | non-zero and `"forged receipt"` in last line | **1** | `AssertionError: r55: forged receipt accepted` | **KILLED, attributed** |
| 6 | `verify_icon_states.py` **c3** — delete `receipt['fixture_sha256'] == expected_hash` + `and` | non-zero and `"forged receipt"` in last line | **1** | `AssertionError: r36: forged receipt accepted` | **KILLED, attributed** |

Baseline controls (pristine bytes, same harness): 4/4 **exit 0** —
`PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained,
forged selection REJECTED`;
`PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second
match REJECTED`;
`PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits:
authored r55-r57 fixtures, not general PE validation.`;
`PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED`.
Every restored run returned to exit 0 with the same PASS line.

Expected-vs-actual for each mutant therefore matches the frozen attribution, including the
round-64 endswith form for b; no crash or unrelated assertion was counted as attribution.

## Frozen-counter receipt (final bytes, full label set)

```
K_HELD=7/14 score=5.0
K_ROW C07 status=frontier
K_HELD_BACKED=7/14
K_HELD_BACKED_STRICT=7/14
README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']
C2_CONTROLS_PASS=2/2
C2_RECEIPT_B_KILLED=2/2
C2_D2_KILLED=2/2
C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
MUTANT verify_icon_languages.py b exit=1 killed :: AssertionError: r47: forged receipt command accepted
MUTANT verify_multi_icon_states.py b exit=1 killed :: AssertionError: r42: forged receipt command accepted
MUTANT verify_icon_languages.py d2 exit=1 killed :: AssertionError: r47: receipt
MUTANT verify_multi_icon_states.py d2 exit=1 killed :: AssertionError: r42: receipt
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
MUTANT verify_named_multi_icon_states.py c3 exit=1 killed :: AssertionError: r55: forged receipt accepted
MUTANT verify_icon_states.py c3 exit=1 killed :: AssertionError: r36: forged receipt accepted
C4_CONTROLS_PASS=2/2
C4_RECEIPT_KILLED_ATTRIBUTED=2/2
MUTANT verify_icon_languages.py c4 exit=1 killed :: AssertionError: r47: forged receipt stdout accepted
MUTANT verify_multi_icon_states.py c4 exit=1 killed :: AssertionError: r42: forged receipt stdout accepted
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
HOLDS_OK_V2=no
```

Counter exit **0**. `HOLDS_OK_V2=no` is **not** a calibration failure at this snapshot: its
frozen formula is
`controls==2 and killed_d2==2 and c3_controls==2 and attributed_b==2 and c3_attributed==2
and c4_attributed==2 and ok==4 and replay==total and fresh==18 and len(mismatch)==0`
(`reports/round-64/measure.py:262-268`); every calibration term is at target (2/2 each,
4/4, 10/10, 18/18) and the sole false term is `len(mismatch)==1` — C1's C07
`frontier→held` README flip, which the contract lands only on C1 admission. C1 is outside
this seat's sweep.

## Restoration evidence (before / after hashes, full restore)

Pristine digests are the table above; mutated-file digests are 16-hex prefixes as printed
by the harness; `restored_eq=True` means the restored full digest equals the pristine full
digest.

| case | pristine (prefix) | mutated (prefix) | restored (prefix) | restored_eq | restored run |
|---|---|---|---|---|---|
| control ×4 | as table | unchanged | unchanged | True | exit 0 PASS |
| b `verify_icon_languages.py` | `a2fd347e6379bee4` | `b00bde88e10dca28` | `a2fd347e6379bee4` | **True** | exit 0 PASS |
| b `verify_multi_icon_states.py` | `9345cb8c91741e36` | `2c34e1c8f02ba116` | `9345cb8c91741e36` | **True** | exit 0 PASS |
| d2 r47 (script+receipt) | `256033f206b20456` | `84a85c6e09038eb8` | `256033f206b20456` | **True** | exit 0 PASS |
| d2 r42 (script+receipt) | `4d8722111cabff9b` | `8dc3649262349abc` | `4d8722111cabff9b` | **True** | exit 0 PASS |
| c3 `verify_named_multi_icon_states.py` | `a226bf73eaba8f91` | `21b15fac7b2a5c2f` | `a226bf73eaba8f91` | **True** | exit 0 PASS |
| c3 `verify_icon_states.py` | `7cbd931a3a8ef639` | `6cf557650b13d753` | `7cbd931a3a8ef639` | **True** | exit 0 PASS |

d2 receipt bytes: round-47 `3b5d3bda…` → `689683675644aea8…` (command + ` --forged`) →
restored `3b5d3bda…`; round-42 `05bf8bf6…` → `cd7dd1ea801864be…` → restored `05bf8bf6…`.

Mutant application was confirmed by the removed-line text, not only by exit codes:
`REMOVED(and): return (receipt['command']==command and receipt['exit_code']==0 and
receipt['fixture_sha256']==expected_hash and` (b, both scripts);
`REMOVED(and): return receipt['command']==command and receipt['exit_code']==0 and
receipt['fixture_sha256']==digest and receipt['evidence_id']==eid and receipt['stdo…`
(c3 named); `REMOVED(and): assert receipt['exit_code'] == 0 and
receipt['fixture_sha256'] == expected_hash` (c3 icon_states).

## Finding F1 — transient regression window in `corpus/verify_icon_languages.py`

At mtime **01:17:08** the lane file had sha256
`2e9e56e8bd8d55ba56c91c87454c0768a66ac87cbe4ee02943cf1916a26d7d15` and its C4 patch
**replaced** the existing forged-command control instead of adding after it:

```diff
     forged=copy.deepcopy(receipt)
     forged['command']+=' --forged'
-    require(not receipt_ok(forged,command,expected_hash,eid,raw_bytes),f'r{r}: forged receipt command accepted')
+    forged_stdout=copy.deepcopy(receipt)
+    forged_stdout['stdout_sha256']=H(b'')
+    require(not receipt_ok(forged_stdout,command,expected_hash,eid,raw_bytes),f'r{r}: forged receipt stdout accepted')
```

`forged` became dead code. Measured on those bytes:

```
MUTANT verify_icon_languages.py b exit=0 pass :: PASS: 3/3 group-language states, …
C2_RECEIPT_B_KILLED=1/2
C2_RECEIPT_B_KILLED_ATTRIBUTED=1/2
HOLDS_OK=no
HOLDS_OK_V2=no
```

counter exit **1**. The independent harness reproduced it (b: control exit 0, mutant
exit 0 PASS, restored exit 0) while the **same mutation on the pre-patch HEAD bytes**
(`0f781c6a…`, control exit 0) was killed with `AssertionError: r47: forged receipt command
accepted` (`attributed=True`), and d2/C4 stayed killed on both — i.e. the mutation and the
detector were sound; only the deleted `require` line differed.

At mtime **01:18:25** the owner restored the line (sha256
`a2fd347e6379bee4…`, current bytes). This sequence is a real claim-voiding state while it
existed (claims.md: "the existing forged-command controls stay"; void condition "C2
attributed kills below 2/2"), and it shows the frozen counter catches the regression
(`C2_RECEIPT_B_KILLED=1/2`, exit 1). The owner was notified; the final sweep above is bound
to `a2fd347e6379bee4…`. If `verify_icon_languages.py` changes again, re-run the counter:
any re-drop of line 151 (`require(not receipt_ok(forged,…), 'forged receipt command
accepted')`) prints 1/2 and fails the probe.

## Limits, dependencies, tooling

- C1 (new C07 knowledge entry + README flip) had **not** landed when this sweep ran:
  `K_HELD_BACKED=7/14`, `README_TOKEN_LEGEND_MISMATCH=1` (C07) — expected mid-wave; this
  seat makes no C1 statement.
- d2's frozen attribution class is raw `exit != 0`; its last lines (`…: receipt`) are
  recorded verbatim rather than upgraded to an endswith claim.
- Scratch is lane-owned `/tmp/revenger-r64-muticon/` (≈60 MB, disposable at landing);
  evidence transcripts `measure-frozen.out`, `measure-frozen2.out`, `sweep.out`,
  `sweep3.out`, `sweep4.out`, harnesses `sweep.py`/`sweep_d2.py`.
- No tool installs, upgrades, pacman transactions, git/jj mutations, commits, or pushes.
  Lane working-tree hashes unchanged after the sweep.
