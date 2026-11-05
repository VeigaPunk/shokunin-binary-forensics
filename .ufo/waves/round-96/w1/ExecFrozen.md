# ExecFrozen — round-96 hold legs (executor)

Digest pin: `.ufo/waves/round-96/w1/ExecFrozen/digest.txt` line 1 = `2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923` with the exact re-derivation command, its output, and the sha256 comparison (working-tree bytes == freeze commit `ff767436feed32cf2f4074f05f938f8cea98e69a` entry bytes == digest).

Hold legs (all `python3 -B`, exact commands in `holds.log`):
- `PYTHONUTF8=1 python3 -B reports/round-95/c1_k_admit_counter4.py --self-test` → `SELFTEST_C1V4=pass legs=24` rc=0 (frozen r95 instrument green on freeze tree).
- `PYTHONUTF8=1 python3 -B reports/round-95/forge_battery4.py --stage full` → `BATTERY4_VERDICT=pass`, `HOLD_R94_BATTERY=pass` rc=0 (r95 battery holds; full delta/mutant/positive/do-nothing lines in holds.log).
- Held probes over freeze archive (`git archive ff767436... corpus | tar -x` into scratch `arch/`; run from `arch/` with `corpus` arg): `f_probe4.py corpus` → `F4_COVERAGE=11/11`; `mg_probe.py corpus` → `M_RECORDED=3/3`; `ag_probe2.py corpus` → `A1V2_RECORDED=5/5`. Probe usage headers confirm `<corpus-dir>` / `<tree>/corpus` arg shape; no adaptation needed.

Note per task: frozen counter4 `--rev` runs were NOT run against anything but their own self-test/battery.

Checks: all Python via `python3 -B`; scratch deleted after copying receipts into the wave dir; no lane files edited; no git writes; no tools installed.

Risks: none observed. Held probes match expected values exactly.

Report: `Report: .ufo/waves/round-96/w1/ExecFrozen.md` + `.ufo/waves/round-96/w1/ExecFrozen/digest.txt` + `.ufo/waves/round-96/w1/ExecFrozen/holds.log`
