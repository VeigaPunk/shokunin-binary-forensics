RESULT: COMPLETE
# R62MutantEvmRawVsInsn — bounded r24 counterexample
Axes: coverage (C1); calibration guardrail: manual structural readout only. No other axis measured.
Frozen revision: `a3498e25ad87bf756288812d0ea7c474b09433c7`.
Scratch root: `/fast/scratch/hyaku/revenger-r62/R62MutantEvmRawVsInsn/` (all artifact paths below are relative to this root).
Read mandatory RULES, godspeed/shokunin skills, frozen claims, QUALITY, and round-61 verifier spotcheck.

## Mutant and expected detector
One scratch-only byte changed: `archive/corpus/fixtures/evm-r24/fixture.raw`, zero-based offset 10, `0x00 -> 0x5b`.
The byte is inside PUSH32 immediate [1,32]; byte length remains 35. No opcode boundary changes.
Plausible defect challenged: using raw `0x5b` count as a substitute for instruction-boundary JUMPDEST count.
Expectations saved BEFORE running in `expected-probe.json`: pristine exit 0, mutant exit 1 with `RAW_INSTRUCTION_DIVERGENCE`, restored exit 0 and original stdout.
The own detector walks instruction boundaries, skips PUSH1..PUSH32 immediate widths, separately enumerates every raw `0x5b`, and rejects unequal offset lists.
“Valid JUMPDEST” below means an instruction-boundary JUMPDEST only, not execution, reachability or callability.
No archived script, fixture JavaScript, EVM bytecode, REA producer, network target, service or runtime provider was executed.

## Commands and actual output
Extraction (cwd `/`, exit 0, no output):
```sh
mkdir -p /fast/scratch/hyaku/revenger-r62/R62MutantEvmRawVsInsn/archive && git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive --format=tar a3498e25ad87bf756288812d0ea7c474b09433c7 | tar -x -C /fast/scratch/hyaku/revenger-r62/R62MutantEvmRawVsInsn/archive
```
Run (cwd `/`, exit 0):
```sh
python3 -B /fast/scratch/hyaku/revenger-r62/R62MutantEvmRawVsInsn/r24_probe.py
```
Same detector command invoked on pristine, mutated, restored bytes, each cwd `/`:
```sh
/usr/bin/python3 -B /fast/scratch/hyaku/revenger-r62/R62MutantEvmRawVsInsn/r24_probe.py --detect /fast/scratch/hyaku/revenger-r62/R62MutantEvmRawVsInsn/archive/corpus/fixtures/evm-r24/fixture.raw
```
Python version from actual initial readout: `3.14.8`. Detector source: `r24_probe.py`; saved complete output: `probe.stdout`; machine-readable observations: `probe-result.json`.
Observed output fields (all phases have empty stderr):
| Phase | Raw offsets | Raw count / present | Valid-JUMPDEST offsets / count | Detector output / exit |
|---|---|---|---|---|
| pristine | `[]` | `0 / false` | `[] / 0` | `RAW_INSTRUCTION_COINCIDENCE / 0` |
| mutated | `[10]` | `1 / true` | `[] / 0` | `RAW_INSTRUCTION_DIVERGENCE / 1` |
| restored | `[]` | `0 / false` | `[] / 0` | `RAW_INSTRUCTION_COINCIDENCE / 0` |
Every phase also printed `FIXTURE_BYTES=35`, `INSTRUCTION_STARTS=[0,33,34]`, `INSTRUCTION_OPCODES=["0x7f","0x50","0x00"]`, `INSTRUCTION_COUNT=3`.
Every phase printed `PUSH_IMMEDIATE_SPANS=[{"pc":0,"opcode":"0x7f","start":1,"end_inclusive":32,"byte_count":32}]`.
The emitted delta has `changed_byte_count=1`, `length_before=35`, `length_after=35`, `inside_first_push32_immediate=true`.

## Hashes, saved delta and restoration
Actual SHA-256 (raw fixture bytes, not text or saved-record identity):
- pristine: `b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93`
- mutated: `d1e7a919e61e6f2af02ae897bcfd6d03d1190659d099133befcdffaae3538370`
- restored: `b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93`
Saved `r24-byte-delta.json` contains both full hex strings, the single-byte delta, before/mutant hashes and frozen revision.
Saved bytes: `r24.pristine.raw`, `r24.mutant.raw`; saved phase output: `pristine.stdout`, `mutated.stdout`, `restored.stdout` (and corresponding empty `.stderr` files).
The probe restores exact original bytes in `finally`, then runs the same detector; actual output: `RESTORED_BYTE_EQUAL=true`, `PRISTINE_RESTORED_STDOUT_EQUAL=true`, `VERDICT=KILLED`.

## Verdict and proposed entry requirement
KILLED by this authored bounded divergence detector, with a passing pristine baseline and passing restored control. No existing verifier/producer coverage is claimed or tested.
Observed counterexample: raw `0x5b` presence changes while the instruction-boundary JUMPDEST set stays empty. The two counts are distinct facts.
The NEW C09 entry must carry its own code AND output for both raw-byte offsets/count and instruction-boundary offsets/count; one derivation cannot stand in for the other (unchanged Q11).
The local structural definition does not establish completeness, authenticity, a general parser method, current producer behavior or all-criteria admission. Existing-verifier kill/survival is unknown.
Only the isolated r24 fixture was mutated and restored; production writes are limited to this report. Prior rejected evidence and README were not written. No source rows, gate or promotion added; no held/admission flip.
This counterexample is evidence for frozen C1, not an admission decision or a claim that K increased.
Installs/updates: none.
