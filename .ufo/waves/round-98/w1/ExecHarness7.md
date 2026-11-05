# ExecHarness7 findings — round 98 w1 (forge_reach7)

Seat: ExecHarness7 (executor). Lane: revenger-shokunin. Freeze: 9d49002a3804de48d365b7d32849ada06745d64f.

## Files written

1. `reports/round-98/forge_reach7.py` — NEW (sha256 9d1f668f44e909d92b975f6fb3650a6940de877a3ab1d20d47f334e1ae6245ac, size 10593).
   CLI: `python3 -B reports/round-98/forge_reach7.py --counter <path> [--profile c02] --work <scratch>`; `--profile` forwarded to the counter only when given (v6: no profile). Honours TMPDIR/HYAKU_SCRATCH/--work (never hardcodes /tmp; scratch routed under --work; exports TMPDIR/HYAKU_SCRATCH/PYTHONUTF8 into counter subprocess). Does NOT reuse `build_fresh.main()` (its COUNTER defaults to the frozen v5 counter); it drives the `--counter` argument with `--work/--tree` (and `--profile` when given).
2. `reports/round-98/forgeries7/__init__.py` — vendored r97 mutators (sha256 553736b3ac7b646ea08499cf6ed39b103404e59d352d2213cc24676eab811c22, size 10034).
3. `reports/round-98/forgeries7/MANIFEST.sha256` — source manifest (sha256 1979f8ffcf0ae99ef4591f95c54d7ee5d05985133c9d44a5f48c2fecad072131).
4. `reports/round-98/controls/v7-dev/harness-v6.log` — red-before (sha256 a595d3e994cebe053fc6c80c2caf468bc1fa5843b68490accea801959b9db315).
5. `.ufo/waves/round-98/w1/ExecHarness7.md` — this file.

Frozen bytes (`reports/round-9[0-7]/`, `corpus/`, `reports/round-97/forge_reach6.py`, `.ufo/waves/round-97/w1/CriticR97/fresh/build_fresh.py`) are byte-unchanged.

## Vectored mutators (manifest)

`forgeries7/__init__.py` is a verbatim copy of `build_fresh.py` lines `def rd(p):` through the end of the `VECTORS` block's last mutator, with header/runtime shim: imports `hashlib,json,re,shutil,sys`, `Path`; `mod=None` + `set_mod(m)` (the r97 functions reference global `mod`; caller binds the frozen v5 counter module); `MUTATORS` registry for the 8 harness vectors. Verbatim subset verified programmatically (`block in vendored == True`).

Copied-mutator manifest (`forgeries7/MANIFEST.sha256` contents):
```
56762e34f52b38b61ac53ededacda7cf6b6e4569f08ec61a4ed6a1f4ccb9cd80  .ufo/waves/round-97/w1/CriticR97/fresh/build_fresh.py
805ffb8aabbdbd451781dd831afce7ab41258979489d29ae789ae9fc1a23ad19  reports/round-96/c1_k_admit_counter5.py
80c1f10b93ac9c3688c4dbd45286da7f08730b17b50930f5cb1d82dc4df3f2f4  reports/round-97/c1_k_admit_counter6.py
```

Vectors: FR00=`m_none`, FR02=`m_entry_bom`, FR06=`m_row_dup_held_over_held`, FR07=`m_row_dup_target_over_held`, FR08=`m_headers_in_fence`, FR09=`m_verified_at_stale`, FR10=`m_na_boilerplate_on_pass`, FR12=`m_own_work_dangling`. Direct import of `build_fresh.py` is impossible (it runs `argparse.parse_args()` at import time), hence vendoring per the spec's alternative.

Honest fixture: frozen v5 `_fixture()` (`reports/round-96/c1_k_admit_counter5.py` sha 805ffb8...). Verified v5 and v6 fixtures produce identical file sets/hashes and each counter passes the other's honest fixture; a v5-built tree is therefore faithful for a v6/v7 `c02` counter. Stub self-test trees are built from this same full fixture (so every delta applies; no `builder note … No such file` class).

FR00b (Amendment A / ReviewerClaims F4/F5): FR00 plus one new file `reports/round-98/benign-r98.txt` with the sentence `This extra file is benign and changes nothing about admission.`; prints `C2_POSITIVE2=<pass|fail>` immediately after `C2_POSITIVE`; `C2_VERDICT=met` requires both positives pass.

## Red-before (harness-v6.log), exit 0

Command:
`PYTHONUTF8=1 python3 -B reports/round-98/forge_reach7.py --counter reports/round-97/c1_k_admit_counter6.py --work <scratch>` (no `--profile`; TMPDIR=`/fast/scratch/hyaku/revenger-r98/ExecHarness7/tmp`, HYAKU_SCRATCH=`/fast/scratch/hyaku/revenger-r98/ExecHarness7/hyaku`)

Exact output lines:
```
VECTOR FR00 rc=0 verdict=pass failing=none
VECTOR FR00b rc=0 verdict=pass failing=none
VECTOR FR02 rc=0 verdict=pass failing=none
VECTOR FR06 rc=1 verdict=fail failing=C1_ADMITTED_UNION,C1_VERDICT
VECTOR FR07 rc=1 verdict=fail failing=C1_ADMITTED_UNION,C1_VERDICT
VECTOR FR08 rc=0 verdict=pass failing=none
VECTOR FR09 rc=0 verdict=pass failing=none
VECTOR FR10 rc=0 verdict=pass failing=none
VECTOR FR12 rc=0 verdict=pass failing=none
C2_ACCEPTED=5/5
C2_POSITIVE=pass
C2_POSITIVE2=pass
C2_STUB_SELFTEST=ok
C2_ROWSET_FR06=C1_ADMITTED_UNION,C1_VERDICT
C2_ROWSET_FR07=C1_ADMITTED_UNION,C1_VERDICT
C2_VERDICT=not-met
rc=0
```

Exit code observed: 0. This matches the spec's red-before acceptance (C2_ACCEPTED=5/5, C2_POSITIVE=pass, C2_STUB_SELFTEST=ok, row-set lines without C1_ROWSET, C2_VERDICT=not-met).

## Verdict

Harness complete and meets the acceptance predicates against frozen v6. Calibration target (v7 `c02` 0/5) is not yet demonstrated — v7 does not exist in the working tree; the L1 records the frozen run after the v7 freeze. No v7/c14/lading-tree counter was run (none exists).

## Risks / notes

- `build_fresh.py` also writes overlay artifacts beside itself; this harness does not invoke it and therefore does not pollute frozen paths.
- FR06/FR07 fail v6 incidentally via `C1_ADMITTED_UNION` (undecorated `admitted` scan); the row-set acceptance for v7 must be via the named leg `C1_ROWSET` (checked by `C2_VERDICT`).
- Stubs print only `C1_VERDICT=fail`/`C1_ADMITTED=fail` (r96 battery convention); `failing_legs` therefore counts them as expected.

## Open questions

None. Interface question answered in the harness docstring: `--profile` is passed through only when explicitly given.

## Tooling recorded

None — system python3 only (stdlib `argparse/importlib/subprocess/shutil/hashlib`). No installs.

