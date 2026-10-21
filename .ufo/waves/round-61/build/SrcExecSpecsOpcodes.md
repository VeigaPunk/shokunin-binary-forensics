# C09 source opening — ethereum/execution-specs v2.20.0 (Osaka VM)

Opened 2026-10-21. Scope: opcode byte values and semantics of EQ 0x14, JUMPI 0x57,
JUMPDEST 0x5B, PUSH4 0x63. Read-only; no execution, no RPC, no REA producer calls.

## Opened (curl -sS, all HTTP 200, 2026-10-21)
- Tag list: https://api.github.com/repos/ethereum/execution-specs/tags?per_page=30 → v2.20.0
- Release page: https://github.com/ethereum/execution-specs/releases/tag/v2.20.0 — title
  "v2.20.0 - BPO2 · ethereum/execution-specs", `datetime="2026-02-19T19:07:08Z"`.
- Tag resolves to commit `2004296f2ffcbcebcd00f41152d33e8dfda0922a` (author date
  2026-02-19T19:01:27Z, "chore(specs): bump version (#2239)").
- Raw files at that tag, HTTP 200 each: `.../v2.20.0/src/ethereum/forks/osaka/vm/`
  `instructions/__init__.py` (367 lines), `instructions/comparison.py` (177),
  `instructions/control_flow.py` (171), `instructions/stack.py` (208), `vm/runtime.py`,
  `vm/interpreter.py`. Section anchor: module docstrings are the only headings, so the
  anchor is the file path plus line range at the tag.

## Verbatim quotes (<=25 words; whitespace normalized across wrapped lines)
1. "Alter the program counter to the specified location if and only if a condition is
   true." — `control_flow.py:72-73` (`jumpi` docstring).
2. "The jump destination should have the `JUMPDEST` opcode (0x5B)." — `runtime.py:28`.
3. "The jump destination shouldn't be part of the data corresponding to `PUSH-N`
   opcodes." — `runtime.py:29-30`.

## Observed facts (path:line at v2.20.0)
- `Ops` enum: `EQ = 0x14` (`instructions/__init__.py:55`), `JUMPI = 0x57` (:106),
  `JUMPDEST = 0x5B` (:109), `PUSH4 = 0x63` (:125).
- Dispatch table: `Ops.EQ: comparison_instructions.equal` (:234), `Ops.JUMPI: ...jumpi`
  (:283), `Ops.JUMPDEST: ...jumpdest` (:286), `Ops.PUSH4: stack_instructions.push4` (:292).
- PUSH4 is `partial(push_n, num_bytes=4)` (`stack.py:146`). `push_n`: GAS_VERY_LOW (:68),
  reads 4 code bytes from `pc+1` as big-endian into U256 (:71-74), `pc += 5` (:77).
- EQ: pops left then right (:139-140), GAS_VERY_LOW (:143), pushes `U256(left == right)`
  (:146), `pc += 1` (:151).
- JUMPI: pops `jump_dest` then `conditional_value` (:83-84; dest is top of stack),
  GAS_HIGH (:87); condition 0 → `pc+1` (:90-91); else dest not in
  `evm.valid_jump_destinations` → `InvalidJumpDestError` (:92-93); else `pc = dest` (:95).
- JUMPDEST: no-op (:167-168), charges GAS_JUMPDEST (:165), `pc += 1` (:171).
- `valid_jump_destinations` is built once per message call from code before the loop
  (`interpreter.py:242,249`) by `get_valid_jump_destinations` (`runtime.py:22-69`): linear
  scan, adds `pc` where opcode == JUMPDEST (:58-59), skips PUSH1..PUSH32 data (:60-65),
  unknown bytes advance 1 (:51-56).

## Inference for the C09 entry (labeled inference, never spec-stated)
- A PUSH4 immediate is only a 4-byte big-endian U256; calling it a selector candidate is
  the ABI/compiler dispatcher convention, which these files do not state.
- The dispatcher shape (PUSH4 immediate, EQ, JUMPI to a JUMPDEST) is recoverable
  statically, but selector→destination pairing is an analyst inference over adjacent
  code, not a relationship the spec defines.
- A static JUMPDEST census must apply the PUSH-data skip (`runtime.py:60-65`): a 0x5B byte
  inside a PUSH4 immediate is not a valid destination; a naive byte scan overstates.

## What the source does NOT state
- That 0x63 immediates are function selectors, or how a selector is derived (ABI
  encoding is outside these files).
- Any static-analysis method for recovering selectors or dispatcher targets; the scan in
  runtime.py exists only to validate jumps during execution.
- Numeric gas costs (only the names GAS_VERY_LOW/GAS_HIGH/GAS_JUMPDEST appear; values are
  in gas.py, not opened).
- Behavior of any fork other than Osaka at v2.20.0, or of deployed binaries of any client.

## Proposed SOURCES.md row (id TBD; append after S015)
| S016 (TBD) | execution-specs v2.20.0, Osaka fork EVM opcode table and instructions — https://github.com/ethereum/execution-specs/blob/v2.20.0/src/ethereum/forks/osaka/vm/ | spec | A | opcode byte values and execution semantics of EQ (0x14), JUMPI (0x57), JUMPDEST (0x5B), PUSH4 (0x63) at commit 2004296f2ffcbcebcd00f41152d33e8dfda0922a | instructions/__init__.py:55,106,109,125,234,283,286,292; comparison.py:127-151; control_flow.py:70-98,149-171; stack.py:47-77,146; runtime.py:22-69 | Opcode values, stack/gas/pc effects, and that JUMPDEST bytes inside PUSH data are not valid jump destinations. | queued | 2026-10-21 | on-release | pending C09 entry (flip to mined at admission) |

## Gaps
- Gas numeric values unopened; the ABI selector-derivation clause needs a separate source
  if the C09 entry claims it — this row cannot support that clause.
- Single revision checked; recheck is on next execution-specs release.
- No installs; only curl and python3 (stdlib) were used.
