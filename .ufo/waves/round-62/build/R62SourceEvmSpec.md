RESULT: COMPLETE

Seat `RevengerR61-2.R62SourceEvmSpec`, leaf. Scope: open execution-specs v2.20.0
opcode source and runtime at official raw endpoints; propose a narrow S028 row. No
live registry/corpus edit, no fixture byte changed, no EVM bytecode run, no
producer, no admission claimed. Frozen archive `a3498e25ad87bf756288812d0ea7c474b09433c7`
extracted to `/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62SourceEvmSpec/tree`.

## Opens (2026-10-21, HTTP 200, official endpoints)

- ref/tags/v2.20.0 -> 392 B, `object.type=tag sha=67f038c8c3fced0b388cfdcaed5c4a52d5fad2fd`
- git/tags/67f038c8... -> tag v2.20.0, tagger 2026-02-19T19:06:01Z, `object.type=commit sha=2004296f2ffcbcebcd00f41152d33e8dfda0922a` ('Release v2.20.0')
- commits/2004296f... -> committed 2026-02-19T19:01:27Z, subject 'chore(specs): bump version (#2239)'
- raw .../2004296f.../src/ethereum/forks/osaka/vm/instructions/__init__.py -> 10700 B, 367 lines, sha256 `49dd6155c7560811a8f546ea9c5a29678e3a3da859216e2ee48cfacaa5b63724`
- raw .../vm/runtime.py -> 1971 B, 69 lines, sha256 `a2801c4169b806a9494707179a9df20170a37a1769596aac56013ddba509aef8`
- both files re-fetched at ref v2.20.0 -> identical bytes and SHA-256
- raw .../vm/instructions/control_flow.py (scope check) -> 3124 B, sha256 `d82b9d3a0d8dc770528c202fe2ecb5f518654522a3f9c630408c6fe5c2f13f19`
- saved at `.../R62SourceEvmSpec/`: both sources at commit and tag ref, both JSON API replies, `readout.py`, `readout.out`, `S028-proposed-row.md`

## Anchors in the pinned bytes

instructions/__init__.py:32  class Ops(enum.Enum):
instructions/__init__.py:55  EQ = 0x14
instructions/__init__.py:106 JUMPI = 0x57
instructions/__init__.py:109 JUMPDEST = 0x5B
instructions/__init__.py:125 PUSH4 = 0x63
runtime.py:22                def get_valid_jump_destinations(code: Bytes) -> Set[Uint]:
runtime.py:26-30             dest < len(code); JUMPDEST 0x5B; not inside PUSH-N data
runtime.py:60-65             PUSH1..PUSH32 branch advances pc past immediate data

Gate quote, `runtime.py:29-30`, 13 words, opened 2026-10-21: "The jump destination
shouldn't be part of the data corresponding to `PUSH-N` opcodes."

## Proposed S028 row (proposal only, not applied)

Row plus provenance table: `.../R62SourceEvmSpec/S028-proposed-row.md`. Scope: byte
assignments EQ/JUMPI/JUMPDEST/PUSH4 and the stated definition plus implementation of
the static destination scan, this tag only; excludes execution effects, gas, stack
behavior, jump acceptance. Teaches 0x14/0x57/0x5B/0x63 and that the scan omits 0x5B
offsets inside PUSH-N immediate data. `used-by`: `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md`.

## Semantics discipline

The enum states numeric assignments only; it says nothing about what PUSH4 or EQ does
when executed, its gas or stack effect, so the row credits none of that. `runtime.py`
is a static scan; alone it does not establish that JUMP/JUMPI to a non-member offset
is refused - that test is at `control_flow.py:63,92`, observed for calibration but
outside this row's credit. No semantics from the enum alone.

## Duplicate risk and decision for L1

Frozen `corpus/SOURCES.md` has 27 rows, no S028. S016 already cites the same URL, tag,
commit, four lines and `runtime.py:22-69` with a broader "semantics" scope, `mined`,
used-by the rejected r61 entry; appending S028 is a second row on one URL and should
raise the known scoped-duplicate warning class (W04 for S024).

1. Preferred: keep S016 and log an in-place `used-by` old->new adding the round-62
   entry, plus this open and quote in the round-62 lesson; the contract permits it.
2. If a this-round pinned row is mandated: append S028 and prefix `teaches` with
   "narrower re-open of S016, byte boundaries only"; do not call S016 rejected.
Either way the entry must open the bytes and carry its own command + output; my quote
and anchors cannot serve as its Q11 derivation.

## Fixture cross-check (own-work domain, not S028 credit)

`python3 -B readout.py`, static only, all seven authored fixtures: evm-r19(hex)
decoded and evm-r21 share sha256 `d1086bce32141782...`, i.e. seven records, six
distinct byte arrays. evm-r24 is 35 bytes `7f` + PUSH32 immediate [1,32] (9 pattern
bytes + 23 zeros) + `50 00`; raw 0x5B count 0, valid destinations 0. In these seven
records the raw 0x5B count equals the scan count (no 0x5B inside PUSH data), so they
do not exercise the exclusion; an entry must still state which count it means.

## Unknowns

- The round-62 EVM entry is absent from the frozen archive and the live tree, so its
  in-entry coverage of its own prose is not yet checkable; gate work remains.
- S028 versus the S016 `used-by` route is L1's integration decision; live registry untouched.
- No census validator run; the duplicate statement rests on S016 row text, not a validator run.

Installs or updates: none.
