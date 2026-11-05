# ExecSession — round-96 session-leg reproduction

Host: ebxnouf (linux 7.2.11-arch1-1, x86_64). REA CLI 6.7.0. Ghidra 12.1.4 PUBLIC.
Scratch: /fast/scratch/hyaku/revenger-r96/ExecSession/ (deleted after copy).
Frozen record under test (untouched, read-only): corpus/live/runs/round-96/.
All Python invocations use python3 -B.

## Leg 1 — Fixture regen: PASS (byte-identical)
- cmd: python3 -B corpus/fixtures/pe-r75-headless-smoke/gen_pe_r75.py regen.exe → rc=0, wrote 1024 bytes
- cmp regen.exe vs committed fixture.exe: IDENTICAL
- sha256 regen.exe: fe060de1bc5106f30dec532270fc634426484e4e2ef186e5b7617443950afd72
- sha256 fixture.exe: fe060de1bc5106f30dec532270fc634426484e4e2ef186e5b7617443950afd72
- Verdict: fixture is deterministically regenerable; matches the subject digest seen in Leg 3.

## Leg 2 — Ghidra headless: PASS (output byte-identical)
- analyzeHeadless ghidra-proj rev96repro -import fixture.exe -postScript rev75_dump.java -deleteProject → rc=0
- INFO REPORT lines (repro): Processing input files / Analysis succeeded / Execute script: rev75_dump.java /
  Post-analysis succeeded / Save succeeded (/fixture.exe, rev96repro) / Import succeeded — same 6 REPORT lines
  as the frozen ghidra-headless-r96.log (only the project name differs: rev96repro vs rev96cap).
- Script line: REV75_DUMP wrote codeable-decompiled.c: 1 functions, 1 decompiled (frozen log: identical counts).
- Output file: function_count=1; `// ==== FUNC entry @ 140001000 ====`; undefined8 entry(void){ return 0x2a; }
  decompiled_ok=1 of 1.
- diff codeable-decompiled.c vs corpus/live/runs/round-96/codeable-decompiled.c: IDENTICAL (rc=0).
- Verdict: headless route reproduces the frozen session output exactly.

## Leg 3 — REA `decompile` @ 140001000: PASS (evidence_id EQUAL, bytes identical)
- cmd: timeout 120 rea decompile fixture.exe 140001000 → rc=0, stderr empty.
- Printed evidence_id: ev_cc0b9d88200afef1e7bf90e77f4d52faa20a049f85f1db1a7bf4a531282ffefe
- EQUALS the entry's frozen ev_cc0b9d88200afef1e7bf90e77f4d52faa20a049f85f1db1a7bf4a531282ffefe: YES (observed, exact string match).
- diff rea-decompile-repro.txt vs rea-decompile.raw.txt (frozen): IDENTICAL (rc=0, 0 diff lines).
  Includes subject sha256 fe060de1… (= Leg 1 fixture), provider ghidra 12.1.4.
- Verdict: stronger than the stability floor the task requires — full byte identity with the frozen record,
  not just a matching evidence_id. No identity claimed beyond what was observed.

## Leg 4 — `rea doctor`: SAME HEALTHY SET (ghidra scope identical; rc=1 both runs)
- cmd: timeout 120 rea doctor → rc=1. healthy: false / environment_healthy: false — but the frozen
  rea-doctor-r96.txt carries the same healthy:false, i.e. rc=1 is the frozen baseline, not a regression.
- ghidra-scope scope_check lines: identical between repro and frozen (ghidra, ghidra-platform,
  ghidra-architecture, ghidra-installation, ghidra-version, ghidra-headless, ghidra-native_decompiler,
  ghidra-java; detail: /home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC[/support/analyzeHeadless]).
  GHIDRA_INSTALL_DIR entry identical (installation/headless/native_decompiler all true).
  22× classification: healthy, 0× unhealthy/degraded/error/unavailable. 9× state: missing — these are
  absent-optional MCP client installs (environment-wide, outside the ghidra scope), same class as frozen.
- Full-file diff repro vs frozen: exactly ONE differing line — paths[3] carries the live fnm_multishells
  PID prefix of the current shell (3146096_… vs frozen 1372562_…), a per-invocation process path,
  not a health finding. All scope_check content is otherwise identical.
- Frozen-record rc not stored in the file; the saved healthy:false matches the repro's verdict, so the
  exit-1 behavior is consistent with the frozen capture.
- Verdict: same healthy set as frozen; the only diff is the shell PID path.

## Summary
4/4 legs reproduce. Fixture byte-identical; Ghidra output byte-identical; REA evidence_id equal AND full
output byte-identical; doctor ghidra-scope identical with healthy:false matching the frozen baseline
(rc=1 both). No lane files touched; no pyc written (all python3 -B); nothing installed.

## Blockers / risks
None. One cosmetic delta noted in Leg 4 (live shell PID in paths[3]) — not a health difference.
