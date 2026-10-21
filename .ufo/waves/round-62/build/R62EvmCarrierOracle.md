RESULT: COMPLETE
# R62EvmCarrierOracle — archived evm-r19 / evm-r21 carrier↔decoded digest binding oracle
Seat `RevengerR61-2.R62EvmCarrierOracle` (round-62 build, leaf). Lane scope: archived
`corpus/fixtures/evm-r19` + `evm-r21` only — carrier bytes, decoded bytes, and every
saved-record `subject`/`artifact`/`bytecode` SHA field with the byte set it binds. No
opcode/dispatch reading (other seat), no entry text, no admission, no README/hold or
map change, no production edit.

## Inputs (frozen, read-only)

- Frozen `a3498e25ad87bf756288812d0ea7c474b09433c7` extracted read-only:
  `git -C …/revenger-shokunin archive a3498e25… | tar -x -C /fast/scratch/hyaku/revenger-r62/R62EvmCarrierOracle/archive` → `EXTRACTED`.
- `diff -r --brief …/archive/corpus corpus` → no output (exit 0): corpus bytes identical
  to the frozen revision; nothing mutated.
- Scratch `/fast/scratch/hyaku/revenger-r62/R62EvmCarrierOracle/`: `carrier_oracle.py`
  (stdlib only, sha256 `6a5cb20e8ebb416fdb2a699c51a069ba03a9fa6d3a2f105e20b442285ac39d1d`),
  `carrier_oracle.stdout.txt` (123 lines, sha256 `2e848cbb2bbc7056b03e2eed61523ab3f9431a3edf8d5318ef5d3e0aa345d2b7`,
  stderr empty), `proposed_readout_block.py` + `.stdout.txt`,
  `proposed-evm-carrier-readout.md`, `other_evm_records_appendix.txt`.
- Run `python3 -B carrier_oracle.py …/archive --selftest` → exit 0. No bytecode, no
  fixture JS, no REA producer, no chain/RPC, no network, no third-party target.

## Derived findings (citations = stdout line numbers)

1. **r19 has two identities.** Carrier `fixture.hex` 39 bytes, sha256 `294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827` (`:7`);
   decoded 18 bytes, sha256 `d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723` (`:9`);
   the 36-byte lowercase hex text is a third byte string, `87167114f90266d04a0fa4f7ea87e192684a8079b0365cf6bfd97c6873c8f43b` (`:8`),
   carried by **no** saved record field (`:103`, mention_count=0).
2. **r19 bindings** (`corpus/live/runs/round-19/inspection.json`, `ev_0ad0097eb137ff9196b29ac3fb6109d8f72ee0761e2655fa1fca594295cf6f42`):
   `subject.digest.sha256` → carrier file (`:28`); `artifact.sha256` → carrier file (`:29`);
   `bytecode.sha256` → decoded bytes (`:31`); `artifact.bytes=39`, `encoding=hex`,
   `bytecode.bytes=18` (`:30`,`:32`); `bytecode.hex` equals the decoded bytes (`:34`).
3. **r21 bindings** (`round-21/inspection.json`, `ev_4810eda7b540fbf2d4265c0f9deb3886dc009945cb77276b980f5502112cfc85`):
   all three fields (`subject.digest` `:62`, `artifact` `:63`, `bytecode` `:65`) bind the
   **same** 18-byte set, because r21's raw carrier *is* the decoded byte string; a digest
   match on r21 is not evidence of a recovered carrier/decoded split.
4. **Cross-fixture**: r21 carrier bytes are byte-identical to r19 decoded bytes (`:78`);
   r21 lowercase hex text equals r19 hex payload text (`:79`).
5. **Sweep completeness**: recursive walk of each record for `sha` keys yields exactly
   three fields per record (`:37-39`, `:71-73`); `unmatched_record_sha_fields=none`
   (`:41`,`:75`).
6. **Locator paths**: both `subject.local_path` values point into an older checkout
   (`/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/…`); the
   path exists on this host and its bytes equal the archived fixture (`:27`,`:61`) —
   identity is by digest (Q09), not by path.
7. **Corpus-wide mention map** (archived `corpus/` only, `:93-119`): `294e6fd2…` 9
   mentions, `d1086bce…` 12, `87167114…` 0.
8. **Detection check (Q13-relevant)**: baseline resolves; mutated record `artifact.sha256`
   → `UNMATCHED` (`:121`); one changed carrier payload byte → both `artifact.sha256` and
   `bytecode.sha256` → `UNMATCHED` (`:122-123`).

## Proposed artifact (scratch only — no production file written)

- `…/R62EvmCarrierOracle/proposed-evm-carrier-readout.md` — drop-in `## Reproduce` block
  + observed output + binding table, for the C09 entry writer
  (`round-62-evm-dispatch-byte-evidence.md`). The block derives every digest it prints,
  avoiding round 61's Q11 failure mode (correct but underived values,
  `corpus/lessons/round-61.md:106`) for the r19/r21 carrier scope; the entry writer must
  still run and print it **inside the entry**. `other_evm_records_appendix.txt` — recorded
  field equality for r22–r26 (`subject=artifact=bytecode=True` for all five raw
  carriers): handoff only, out of scope.

## Unknowns / limits

- `evidence_id` values are recorded identifiers; not recomputed here, so labeled recorded,
  not derived. No claim about provider method, deployed authenticity, hardfork, discovery
  completeness or runtime behavior; digests bind bytes only. Whether the 36-byte hex-text
  digest belongs in the entry is the entry writer's scoping call.

## Preservation / no-claim statements

- No corpus, fixture, report, lesson, README or source file written or modified by this
  seat; only this report and the scratch files above (`git status --porcelain` shows only
  the pre-existing untracked `.ufo/waves/round-62/`). No gate, admission, promotion,
  registry, README row, C04/C09 map or hold change; README stays uncovered and nothing
  here is claimed as admitted.

## Installs

None. Stdlib Python 3 only (`python3 -B`; hashlib/json/pathlib/sys).
