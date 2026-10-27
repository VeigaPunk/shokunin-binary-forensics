PASS — v6 has no embedded-output drift; all 24 blocks match v5.1.

## Evidence

- Gate command from the lane root: `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md` → `checked_blocks=24 problems=0`, exit 0. This agrees with the gate's documented clean/ drift/ could-not-evaluate exit contract (`corpus/check_embedded_outputs.py:10-19`).
- Independent comparison used a separate fenced-block parser and ran each declared argv command with captured stdout. v6: 24 blocks, 134 embedded output lines checked; v5.1 (`corpus/knowledge/round-70-apk-axml-byte-evidence.md`): 24 blocks, 134 output lines checked; missing lines/nonzero command exits: 0 problems for both.
- Independent byte comparison of each command and its ordered embedded output lines: `blocks identical (cmd+output bytes): True`; all 24 block pairs matched. v6 blocks begin at entry lines 27, 34, 36, 43, 45, 47, 58, 67, 76, 83, 90, 92, 94, 96, 105, 114, 123, 144, 156, 182, 222, 238, 245, 254.
- Source entry identifies the gate recheck at `corpus/knowledge/round-71-apk-axml-byte-evidence.md:10` and describes retained v5.1 blocks at `:9`; the command/output blocks occupy `:27-277`.

checked_blocks=24; problems=0; gate_exit=0; independent problems=0; v6 blocks match v5.1: yes.
