# ExecBattery — round-95 battery4 end-to-end reproduction (attempt 1)

Date: 2026-11-05 (times -0300). Lane: /home/vgpnk/Projects/shokunin/revenger-shokunin.
Runs executed from the lane root with `python3 -B` and
`HYAKU_SCRATCH=/fast/scratch/hyaku/revenger-r95/ExecBattery`:

```
PYTHONUTF8=1 HYAKU_SCRATCH=/fast/scratch/hyaku/revenger-r95/ExecBattery \
  python3 -B reports/round-95/forge_battery4.py --stage red-v3   # 14:36:42-14:36:47
PYTHONUTF8=1 HYAKU_SCRATCH=/fast/scratch/hyaku/revenger-r95/ExecBattery \
  python3 -B reports/round-95/forge_battery4.py --stage full     # 14:37:08-14:37:41
```

## Freeze integrity (pre-run check)

- Lane HEAD = `6e0bf15fed58f357b7fa0c881371ac7616a116f7` (the freeze commit itself).
- Working-tree `corpus/knowledge/round-95-evidence-ledger-discipline.md` sha256
  `476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9` == `git show
  6e0bf15…:corpus/knowledge/round-95-evidence-ledger-discipline.md` blob sha256.
  Entry bytes identical to freeze.

## Result: no verdict-line drift — reproduction SUCCESS

### red-v3 (rc 0; control rc 0) — logs byte-identical except capture line

`diff controls/battery4-red-v3.log red-v3.log` → single hunk `14d13 < rc=0`: the frozen
control carries a trailing `rc=0` capture line that my tee'd battery-stdout log does not
(my rc was captured separately as `RED_RC=0`, equal to the control's `rc=0`). All 13
battery stdout lines — including every verdict line — are byte-identical.

| Token | Freeze | Repro | Match |
|---|---|---|---|
| V3_REACH_NEW | 10/10 | 10/10 | yes |
| MUTANT_V3_REGISTRY_SURVIVES | pass | pass | yes |
| RED_V3_VERDICT | pass | pass | yes |

Per-vector `v3 reach` lines: all 10 named TREE vectors, byte-identical, same order.

### full (rc 0; control rc 0) — logs byte-identical except capture line

`diff controls/battery4-full-at-freeze.log full.log` → single hunk `18d17 < rc=0` (same
trailing capture-line artifact; `FULL_RC=0` == control `rc=0`). All 17 battery stdout
lines byte-identical.

| Token | Freeze | Repro | Match |
|---|---|---|---|
| SELFTEST_C1V4 | pass | pass | yes |
| V4_KILLS | 10/10 | 10/10 | yes |
| MUTANT_V4_REGISTRY_KILLED | pass | pass | yes |
| POS_C1V4 | pass | pass | yes |
| DO_NOTHING_C1V4 | fail-as-required | fail-as-required | yes |
| HOLD_R94_BATTERY | pass | pass | yes |
| BATTERY4_VERDICT | pass | pass | yes |

All 10 per-vector `v4 KILLED on <leg>` lines match the frozen control exactly, same legs,
same order. No scratch path appears in any verdict line in either stage.

### Log receipts (retained in this wave dir)

- `red-v3.log` sha256 `54fd9885f242231b686bdebc64a1b4891114168705088613dc4c04cc5d45d3fd`
  (mtime 14:36:47).
- `full.log` sha256 `5b640281060356ddae6e326b21880cd3b3d0f3dcee938f415b8691c9d43f604a`
  (mtime 14:37:41).
- Controls: `battery4-red-v3.log`
  `21049ff614012264e09631207e52532e6c1972f698f16d1143b5936e70710d48`;
  `battery4-full-at-freeze.log`
  `7371cbc34654efad39b72c615720cc7b8ad9754d4376b5485bee5e553d376aff`.

## Environment notes

- Scratch nesting: `forge_battery4.py` appends `revenger-r95/battery4` to
  `HYAKU_SCRATCH`, so its work root was
  `/fast/scratch/hyaku/revenger-r95/ExecBattery/revenger-r95/battery4` (inside the seat
  scratch). The battery removes its own `b4-*` mkdtemp work dirs on exit; residual
  env-derived parent dirs (`revenger-r95/{battery4,c1v4}`, `revenger-r94/c1v3`,
  `revenger-r93/battery/{selftest,v1sim,v2sim}` from the HOLD re-run of the frozen r93
  simulators) contained **0 files** at end of run. Seat scratch tree deleted on exit.
- HOLD provisioning: `forge_battery4.py` pre-created
  `/fast/scratch/hyaku/revenger-r94/battery3` — `forge_battery3.py`'s hardcoded SCRATCH
  constant (line 22), disclosed provisioning per claims §C2. Left in place deliberately:
  r94 lesson M1 (a reaped scratch root breaks a direct frozen-battery3 run) and battery4
  re-pre-creates it (`mkdir(exist_ok=True)`) on every HOLD leg, so removal buys nothing
  and breaks direct runs.
- Python 3.14.8. Every seat Python invocation used `python3 -B`; `forge_battery4.py`
  spawns all counters/subprocesses with `-B` (run_counter, selftest_runner) and
  `forge_battery3.py` likewise (lines 73/117/129/138/147). My runs wrote no `__pycache__`
  anywhere and no default-path scratch.

## FINDING (pre-existing, not produced by this seat; reported, not remediated)

`reports/round-94/__pycache__/c1_k_admit_counter3.cpython-314.pyc` exists, mtime
2026-11-05 14:23:14 — **before** this seat's first battery invocation (14:36:42). It is
the r94 lesson M5 defect class (a Python import without `-B` writing bytecode under the
instrument tree). Corroborating scratch evidence: `/fast/scratch/hyaku/revenger-r94/c1v3`
mtime 14:27:56 sits at counter3's *default* `HYAKU_SCRATCH`-less path, which neither of
this seat's invocations could produce (both exported `HYAKU_SCRATCH`; counter3 SCRATCH is
env-aware — line 27). Attribution: some concurrent actor ran/imported counter3 bare
before ~14:28. Scope: `C1_PYCACHE` checks corpus/, reports/round-95/ and
.ufo/waves/round-95/ only, so this does **not** trip the frozen C1 leg, but the sentinel
should identify the actor. Per bounds this seat did not modify `reports/round-94/` (frozen
bytes).

## Verdict

Round-95 C2 instrument reproduces exactly at the freeze commit: red-before and full
battery both match the frozen controls on every verdict line with matching exit codes.
C2's `BATTERY4_VERDICT=pass` (exit 0) is independently reproduced.
