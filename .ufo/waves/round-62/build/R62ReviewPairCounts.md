# R62ReviewPairCounts — independent recount of the C09 "three reported pairs" wording

RESULT: COMPLETE

Seat `RevengerR61-2.R62ReviewPairCounts` (reviewer, leaf, no dispatch). Scope: the count semantics behind the
old C09 phrase "three reported pairs" versus raw observations on `evm-r19`, `evm-r21`, `evm-r22` and the unique
selector+target pairs. No admission is claimed; `corpus/README.md:38` C09 stays `uncovered`.

## Method (frozen, read-only; only stdlib Python executed)

- Frozen `a3498e25ad87bf756288812d0ea7c474b09433c7` extracted read-only via `git -C
  /home/vgpnk/Projects/shokunin/revenger-shokunin archive a3498e25… | tar -x` into
  `/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62ReviewPairCounts/tree`; `diff -rq tree/corpus
  corpus` → empty (frozen corpus == working corpus).
- `python3` 3.14.8 stdlib only; no bytecode, fixture JS, provider, chain or RPC run; no
  `corpus/live`/`corpus/fixtures` byte touched (`git status --porcelain` → only `?? .ufo/waves/round-62/`).
- Command `cd tree && python3 -B ../proposed_block.py` → exit 0, byte-identical over two runs (`cmp out1.txt out2.txt`); code + full 51-line stdout in `…/RevengerR61-2.R62ReviewPairCounts/`.

## Exact counts, four separately named sets (`countset_output.txt:46-51`)

```
SET_A_records_reporting_at_least_one_pair=3 rounds=[19, 21, 22]
SET_B_candidate_observations_record_x_pair=4 [(19,'0xdeadbeef',16), (21,'0xdeadbeef',16), (22,'0xaaaaaaaa',30), (22,'0xbbbbbbbb',32)]
SET_C_distinct_selector_target_pairs=3 [('0xaaaaaaaa',30), ('0xbbbbbbbb',32), ('0xdeadbeef',16)]
SET_D_distinct_decoded_inputs_among_SET_A=2 ['94c1790f…1dbe2', 'd1086bce…e723']
SET_E_distinct_decoded_inputs_all_seven=6
SET_F_records_with_empty_functions=4 rounds=[23, 24, 25, 26]
```

## Resolution of "three reported pairs"

- **3 is correct** under two explicit readings — SET_A (records reporting ≥1 pair: r19, r21, r22)
  and SET_C (distinct `(selector, bytecode_offset)` pairs `0xdeadbeef@16`, `0xaaaaaaaa@30`, `0xbbbbbbbb@32`).
- **3 is wrong** under SET_B (candidate observations = record × pair) = **4**: r19 1 + r21 1 + r22 2.
  The defect is an **unnamed set**, not an arithmetic error: the round-61 falsify note
  (`.ufo/waves/round-61/falsify-w3/W3EvmQTable.md:20`, F5) — "a reader re-deriving it gets 4" — is
  true only for SET_B, so a new entry printing a number without naming its set fails Q11 again.
- SET_B > SET_C because **r19 ≡ r21 in decoded bytes** (both `d1086bce…e723`, 18 B), reported by
  two records with different carriers (`fixture.hex` 39 B text vs `fixture.raw` 18 B).

## Raw observations behind the counts (`countset_output.txt:4,10,16,6,12,18`)

- r19/r21: `raw_0x63=[6] raw_0x5b=[16] push4=[(6,'deadbeef')] jumpdest=[16]
  jumpi(at,dest,valid)=[(14,16,True)]`; r22: `raw_0x63=[7,17] raw_0x5b=[30,32]
  push4=[(7,'aaaaaaaa'),(17,'bbbbbbbb')] jumpdest=[30,32] jumpi=[(15,30,True),(25,32,True)]`.
- r19 `subject_eq_carrier=True subject_eq_decoded=False` (subject digest `294e6fd2…b827` is the
  39 B **hex carrier's** SHA-256, not the decoded 18-byte string); r21…r26 both true — "the record's
  subject digest equals the fixture bytes' SHA-256" is ambiguous for r19 unless carrier and decoded
  digests are printed separately, full and untruncated. Offsets 16/30/32 are JUMPDEST positions and
  the JUMPI destinations, matching `corpus/fixtures/evm-r22/truth.json` `branches[].destination_offset`;
  whether the provider *means* JUMPDEST is left unknown.

## Avoiding the records / candidates / distinct-inputs mix

Same bytes, six defensible numbers — name the set every time. Beyond SET_A…SET_F above: 7 saved EVM records
exist (`corpus/live/runs/round-*/inspection.json` with a `functions` field: rounds 19, 21–26; round-15 and 27–35
have none), and distinct **carrier** digests are 7 (all seven) and 3 (positive records only) — r19's carrier text
≠ its decoded bytes, so "distinct inputs" is 2 or 6 by decoded bytes and 3 or 7 by carrier.

Rules proposed for the new entry: (1) never write "pairs" without the set qualifier; (2) derive SET_C from the
tuple set, not per-record lists; (3) write "candidate observations (record × pair)" for SET_B; (4) count inputs by
**decoded** bytes and print carrier and decoded digests separately; (5) if 3 and 4 both appear, name both sets.

## Proposed artifact (scratch, not landed; integration is L1's)

`…/RevengerR61-2.R62ReviewPairCounts/proposed_block.py` — embeddable readout: per-fixture
carrier/decoded lengths and full SHA-256s, raw `0x63`/`0x5b` offsets, PUSH4 sites, JUMPDEST set, JUMPI
targets, saved-record SHA-256, full `evidence_id`, subject-digest equality to carrier vs decoded,
saved `functions`, flags, then the six named count sets; stdlib, read-only, deterministic, no
bytecode/provider execution. `paircount_recount.py` adds the record→input grouping exposing r19/r21.

## Unknowns (honest)

- Cause of the empty outputs (r23–r26) is unassigned; no fixture separates the competing rules and
  no provider was re-run this round.
- Whether `bytecode_offset` denotes the JUMPDEST destination, the PUSH1 operand or the PUSH4 site is consistent
  with the JUMPDEST reading on these bytes only; recomputability of the seven saved `evidence_id` values is untested
  (recorded identifiers); `dispatch: abi` / `payable` labels are provider inferences, not fixture truth.

Installs: none — `python3` 3.14.8, `git`, `tar`, `cmp`, `diff` were already present.
