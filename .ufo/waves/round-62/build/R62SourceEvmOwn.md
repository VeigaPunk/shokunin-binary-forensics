RESULT: COMPLETE

Scope: propose S031 (own-work, tier A) for the seven authored EVM fixture byte strings and
the literal saved bytecode/function fields at frozen `a3498e25ad87bf756288812d0ea7c474b09433c7`,
`used-by=corpus/knowledge/round-62-evm-dispatch-byte-evidence.md`. No corpus/README/QUALITY/live
edit, no source row applied, no admission, no K or provider-capability claim; prior rejected entries untouched.

Frozen base
- `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin rev-parse a3498e25…` -> `a3498e25ad87bf756288812d0ea7c474b09433c7`;
  extracted with `git archive` to `/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62SourceEvmOwn/tree`.
- Opened there: `corpus/fixtures/evm-r19/fixture.hex` and `evm-r21`…`evm-r26/fixture.raw` with each `truth.json`;
  `corpus/live/runs/round-19/inspection.json` and `round-21`…`round-26/inspection.json` (no `evm-r20`).

Derivation (command + output; full log `derive_s031.out`, script `derive_s031.py`, cwd scratch root, exit 0)
- Fixture file bytes / SHA-256 / decoded bytes: r19 39 `294e6fd2…b827` -> 18 `d1086bce…e723` (hex carrier);
  r21 18 `d1086bce…e723`; r22 34 `94c1790f…dbe2`; r23 7 `8047ddff…2f5a`; r24 35 `b69834e0…5d93`;
  r25 19 `2d87a4e2…e8f7`; r26 19 `ebe2d675…e97d`.
- `normalized_result.bytecode.hex` equals each decoded fixture string 7/7; `bytecode.sha256` equals
  `sha256(decoded)` 7/7; `bytecode.bytes` equals decoded length 7/7; `subject_eq_carrier` 7/7;
  `artifact_eq_carrier` 7/7. `subject_eq_decoded` is 6/7: false only r19 (39-byte hex carrier vs 18 decoded).
- Literal `functions`: r19/r21 `0xdeadbeef`/`16`; r22 `0xaaaaaaaa`/`30` and `0xbbbbbbbb`/`32`; r23–r26 `[]`.
- r24: 35 bytes, `0x7f` at 0, immediate [1,32]; byte search of `63deadbeef14601057` gives starts `[1]`,
  inclusive span `[1,9]`; raw 0x5b offsets `[]`; offsets 33/34 = 0x50/0x00.
- r25/r26: 19 bytes each, differing only at offset 14 (0x10 vs 0x11); offset 17 = 0x5b in both;
  r19 decoded equals r21 file bytes (6/7 distinct decoded arrays).
- Record bytes contain `rea-agents` 0 times; every record's literal `provider.version` is `evmole@0.9.3`.
  The row does not repeat S026's `rea-agents@6.4.0` attribution (that string is LEDGER prose only,
  e.g. `corpus/live/runs/round-19/LEDGER.md:5`).

Gate quote (opened 2026-10-21, 17 words by `split()`, exact string equality `True`):
`corpus/live/runs/round-19/inspection.json` `$.limitations[4]` (single-line file, `:1`): "Original carrier
and decoded bytecode SHA-256 are distinct identities; SHA-256 is not the Ethereum Keccak code hash."
Additional located anchor (not the Gate quote), 9 words, `corpus/fixtures/evm-r24/truth.json:16` `$.note`:
"All opcode-looking bytes lie inside PUSH32 immediate; no execution/chain." The record is data, not a
producer receipt; `truth.json` fields are recorded intent, never the oracle.

Proposed row (proposal only, not applied)
| S031 | Authored EVM byte fixtures and saved bytecode records — `corpus/fixtures/evm-r19`, `evm-r21` to `evm-r26`; `corpus/live/runs/round-19`, `round-21` to `round-26` | own-work | A | added scope beside S026 — exact authored fixture byte strings at a3498e25ad87bf756288812d0ea7c474b09433c7 and their byte-identity relation to the saved records' literal bytecode strings, sizes and digests, plus literal functions selector and bytecode_offset integers; truth.json intent fields recorded only; provider behavior, field meaning and completeness excluded | `corpus/fixtures/evm-r19/fixture.hex` and `evm-r21` to `evm-r26/fixture.raw` plus `truth.json` at `a3498e2`; `inspection.json` `$.normalized_result.bytecode.hex`/`.sha256`/`.bytes` and `$.normalized_result.functions[]` in `corpus/live/runs/round-19`, `round-21` to `round-26` | Which exact bytes each saved EVM record's bytecode string and digest covers, including r19's 39-byte hex carrier versus 18 decoded bytes, so an oracle comparison names its referent. | mined | 2026-10-21 | 90d | corpus/knowledge/round-62-evm-dispatch-byte-evidence.md |

Full row, Gate note, provenance tables and boundaries: `/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62SourceEvmOwn/S031-row-proposal.md`.

Relation to S026 (duplicate authority)
- S026 stays the sole row for what the provider reported, including empty `functions` lists and any field
  meaning (`dispatch`, `payable`, `inferred`, `kind`, `hardfork`). S031 adds the authored fixture byte
  strings and their identity relation to the saved `bytecode` fields, which S026 does not credit.
- If L1 judges the record-literal half too duplicative, the non-overlapping core is the seven fixture
  byte arrays plus the identity equalities.

Row-shape validation (scratch copy, no live edit)
- Inserted this exact row after S027 in a scratch `corpus/SOURCES.md`, copied `corpus/knowledge/` beside
  it and added a zero-byte stub at the used-by path; `sources-census.sh validate --file
  <scratch>/corpus/SOURCES.md --today 2026-10-21` -> exit 0, `0` E-codes, no S031 finding, NF=13 (11 cells);
  census rows `27 -> 28`. Only the pre-existing `W04 S024` warning.
- E11 sequencing for L1: `used-by` must resolve when the row is validated, so insert it with the landed
  entry, or insert as `queued` and log the queued->mined flip old->new.

Honest limits / unknowns
- No record carries a creation timestamp; `opened` 2026-10-21 is the row's open date, not a run date.
- `subject.local_path` denotes an older checkout; correspondence rests on per-file digest equality, not path.
- Tier A covers exact bytes, lengths, SHA-256 of those bytes and the listed record literals only; no
  authenticity, origin, completeness, ABI, runtime, reachability, hardfork, chain or general-method claim.
- This readout is row provenance, not an entry derivation: the C09 entry must still carry its own Q11
  command and output for every value it states.
- No other seat is claimed to have opened these bytes; no producer was run.

Installs: none.
