GRADE: HOLDS — corpus/SOURCES.md row S031 and round-62 lesson sourceGate (S031 quote)

Target: frozen d97761952be256d145d298022de03091de91d358; claimbase 5bd4a90fc1a34caa94496601b60537b3aab12301; pre-registration a3498e25ad87bf756288812d0ea7c474b09433c7.
Candidate hash: corpus/knowledge/round-62-evm-dispatch-byte-evidence.md sha256 6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e at d977619.
SOURCES.md sha256 5c13831b8b64b1a2d715fc4031415750d92af4daf3ef8021c91a8912b5d66bbe; lesson sha256 cf0339ebe9baa95124da3b7f4345f8c8abf8c5b35541d3b9ace1b22a0449d6ae.

Method: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive d97761952be256d145d298022de03091de91d358 | tar -x -C .` in /fast/scratch/hyaku/revenger-r62/R62FSourceOpenS031 (11M); full hash recorded. All checks on archived copies with TMPDIR under the same scratch. No live edit, no producer/REA call, no JS/EVM execution, no chain/RPC, no git index/history mutation.

OBSERVATION (primary commands and output)

1. S031 row is corpus/SOURCES.md:45. Its sources exist: corpus/fixtures/evm-r19 contains fixture.hex (39 bytes) + truth.json; evm-r21..evm-r26 each contain fixture.raw (18/34/7/35/19/19 bytes) + truth.json; no evm-r20 fixture. corpus/live/runs/round-19 and round-21..round-26 each contain inspection.json. Command: `ls -la` per directory; sizes above.

2. Quote location and exact text. `jq -r '.limitations[4]' corpus/live/runs/round-19/inspection.json` ->
   "Original carrier and decoded bytecode SHA-256 are distinct identities; SHA-256 is not the Ethereum Keccak code hash."
   Python exact equality against the lesson's extracted quote: True. Word count `split()`: 17 (<=25). The file is single-line (1 newline, trailing) and its top-level array has 6 entries; index 4 is the quote. File sha256 e892dd18ff219f71ce2644a3f5a3e3ad3479d2ca46df9e2a7c260e7b33f15948 at both a3498e25 (`git show a3498e25:...`) and d977619. `json.loads(...)['limitations'][4]` at a3498e25 equals the lesson quote: True.

3. S031 anchor fields are present in each record 7/7. For every r in 19,21..26: `subject.digest` exists (sha256 object), `normalized_result.bytecode` exists, `normalized_result.functions` is a list (1,1,2,0,0,0,0 entries). `.limitations[4]` equals the same quote 7/7. Command/output: one `python3` loop printing `fields_ok`, `lim4_eq`.

4. Identity relation is the one the row teaches. 7/7:
   - `subject.digest.sha256` == sha256(fixture file bytes);
   - `normalized_result.bytecode.sha256` == sha256(decoded bytes);
   - `.bytes` == len(decoded); `.hex` == decoded.hex().
   r19: carrier 39 bytes sha256 294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827; decoded 18 bytes sha256 d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723; subject is the carrier, bytecode digest is decoded. r21 file bytes equal r19 decoded (18 bytes, same sha256). r22..r26 carrier == decoded.
   r24 pattern `63deadbeef14601057` has one occurrence, start 1, inclusive span [1,9]; its truth.json `embedded_pattern_hex` is a recorded/intent field, consistent with the row's "recorded intent only".

5. Row opened this round: S031 `opened` = 2026-10-21; lesson Gate access date = 2026-10-21. Diff `5bd4a90..d977619 -- corpus/SOURCES.md` shows S028-S031 added and no changes to S001-S027; the lesson states the same. S031 is tier A own-work, scope "fixture byte strings and identity relation to saved bytecode hex/size/digest and function candidate literals", explicitly "not provider semantics or completeness"; teaches keeps r19 carrier/decoded identities separate. No producer-accuracy claim from own work; the quoted sentence is a recorded limitation, and the lesson labels it as not producer provenance.

6. Blob identity across revisions: `git ls-tree -r` of the 42 paths (7 fixture dirs + 7 run dirs) at a3498e25 vs d977619, `diff` exit 0.

INFERENCE
- The S031 row's three load-bearing elements are true at the cited revision: fixture carriers and decoded bytecode are distinct for r19, subject and bytecode digests have different scopes, and the seven records contain the named fields. The row's teaching is narrow and consistent with the Gate quote.
- No actual misstatement found in S031 or in the S031 Gate paragraph. The quote is exact, 17 words, at limitations[4], with the round access date and row-open date; own-work is not used for producer accuracy.
- Adjacent entry-side note (not part of this grade, for the C09 Q01/Q11 seats): the candidate's Observation 3 and inventory also print `recorded.operation/provider_id/provider_version/evidence_id/authority/confidence/evidence_kind/discovery_completeness/runtime_execution`, which are outside S031's enumerated bytecode/function scope; the entry labels them recorded and disclaims authentication, so this is an attribution-scope question (S026 is the broader record row), not a false value or an S031 defect. I do not adjudicate the C09 entry here.

UNKNOWN
- None material to S031 or its Gate. I did not evaluate the candidate's full Q11 inventory or its other clauses; other seats own that decision. No provider was run; no success/failure of the producer is asserted.

VERDICT: HOLDS for S031 and the round-62 sourceGate quote. No repair, no admission, no coverage flip implied. Installs: none.
