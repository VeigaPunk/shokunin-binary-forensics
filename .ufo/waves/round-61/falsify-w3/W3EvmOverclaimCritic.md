GRADE: PARTIAL — corpus/knowledge/evm-saved-interface-candidates.md (C09), whole-entry overclaim sweep vs Q05/Q07/Q10

Seat RevengerR61-2.W3EvmOverclaimCritic · 2026-10-21 · archive of ab580698212258a55e43e9bb9bf6ac78c91eae2a in /tmp/revenger-r61w3-W3EvmOverclaimCritic.
The entry is byte-identical in the archive and the live tree (sha256 `ab9c48da93cc…387b`, both). Its `## Reproduce` block, run in the archive, exits 0 and prints exactly the `## Provenance` lines (all 14 lines equal).

## Method
- Ran rg `(never|always|every|all|any|none|only|deployed|general|rate|%)` over the entry, which hit lines 3,11,34,37,38,52,55,65,68,72,81,85,87,98,171,180-189. Every narrative sentence (lines 9-99) was then compared with the seven saved records (full field dump of `corpus/live/runs/round-{19,21..26}/inspection.json`) and with the fixture bytes.
- Tested both post-hoc rules at lines 64-65 against all seven bytestreams with an instruction walk. No fixture contains an executable JUMP (0x56). In r22 the first STOP is at 26, after both JUMPIs at 15 and 25. Both rules fit all seven, and no fixture separates them. HOLDS.
- Re-opened S016 at https://raw.githubusercontent.com/ethereum/execution-specs/v2.20.0/src/ethereum/forks/osaka/vm/runtime.py (accessed 2026-10-21). The docstring reads verbatim: "The jump destination shouldn't be part of the data corresponding to `PUSH-N` opcodes." The walk is equivalent to `get_valid_jump_destinations`. HOLDS.

## Generalisation, provider-method, rate, 'every'/'never' — sentences that HOLD
- No sentence generalises to deployed code. Lines 11, 70-72 and 99 disclaim deployed contracts, compiled bytecode and kasegi's layer. Q10 passes on scope.
- No rate is quoted (line 81). rg finds no `%` and no "rate" except that disclaimer.
- No provider-method claim. Lines 12-13 and 63-66 leave the method and the cause unknown and call the rules "post-hoc… neither is validated". Q07 passes. The r25 ledger (`round-25/LEDGER.md:5`) also says "**cause is unknown**".
- The 'every' at line 55 is used only to refute a universal with the r26 counterexample. r26 has a valid JUMPI→JUMPDEST at 15→17 and `functions=[]` (Reproduce output). It is a valid single-counterexample falsification.
- Line 68 matches the record's own limitation[2], verbatim: "Empty results do not prove the absence of callable dispatch."
- Line 52 "observed on three more authored records only" is scoped. Kaidoku's basis is a different 81-byte carrier (`kaidoku…/2026-10-13-r3-evm-interface.md:151-153`, `PROVINCE.md:54`).
- Lines 30-31: the PUSH4 sites (6/7/17) appear in no record field; `bytecode_offset` is the only positional field (field dump).
- Lines 85-90: `verify_evm_evidence.py:10-11` reads r19 only. `MutantEvmVerifier.md:6` gives "mutants 37/37 exit 0". `LOG.md:289` gives "immediate offsets 1–9". All three HOLD.
- Line 74 "four seats": `ExecEvmOracleR19.md:29` (2 forms), `R21.md:29` (4), `R22.md:12` (3) and `R23.md:23` (8) make 4 EVM seats. The count HOLDS, but the entry cites none of these reports (see P5).
- Line 82 "run 2026-10-12": `LOG.md:233-310` dates every round 19-26 result 2026-10-12. HOLDS, but the line is uncited.
- Line 12: `~/.agents/skills/reverse-engineer-anything/SKILL.md:37` names `rea-agents@6.7.0` today. HOLDS.

## Overclaims found (none contradicted by evidence; all PARTIAL)
- P1, lines 97-98, Q01/Q10. "Kasegi owns deployed-code identity and claimability (`kasegi-shokunin/PROVINCE.md:25`)" overstates its cite. Line 25 is only "**Refuses:** anything outside this domain; report cross-domain evidence back to the orchestrator rather than absorbing it." `rg -i 'deploy|claimab|EVM|bytecode' kasegi-shokunin/PROVINCE.md` prints 0 lines. The real support is `kasegi…/corpus/knowledge/operator-queue.md:58` ("Deployed-code check required… bytecode drift = re-verify") plus `PROVINCE.md:3` (domain "claim packages").
- P2, lines 82-83, Q01/Q04. "`authority: shipped-artifact` label describes a file class, not origin" asserts REA's label semantics without a source. rg finds no definition in `corpus/SOURCES.md` or in any build report; the only other hit is this entry's own Q09 row. The Q09 row at line 185 already uses the safe form, "not read as origin".
- P3, lines 9 and 82, Q11 (Q04 adjacent). "provider … `evmole@0.9.3` inside the records" and "One provider version" are claims about all seven records, but the Reproduce block never prints `provider.version`. Line 170 itself says the string "is read from the r19 record". The claim is TRUE by observation (all seven records: `provider.version = "evmole@0.9.3"`, `authority = "shipped-artifact"`), but it is not derived in the entry.
- P4, lines 59-60, Q06/Q11. The r24 premises "embedded JUMPI target (0x10)" and "the file has no 0x5B byte" are not printed by the block, which prints `raw_0x63` only and `jumpdest=[]` from the instruction walk. Both are TRUE (bytes `7f63deadbeef146010570000…5000`: offset 8 is `0x10` and there is no `5b`). The Q06 row at line 182 ("every fixture premise re-derived") and the Q11 row at line 187 ("every count … carries the command") therefore overclaim slightly.
- P5, line 74, Q11. The count "four seats" carries neither a command nor a path; it is not labeled "recorded" with a cite.
- P6, lines 54-57 vs line 181, Q05. "…is therefore false for this provider version on this input" is in present tense and attributes the result to evmole@0.9.3 alone. The evidence is one 2026-10-12 run through `rea-agents@6.4.0`: the record's `provider.name` is "REA EVM interface adapter", and the run was not re-probed in round 61. The Q05 row says "no current capability claim". A past-tense, adapter-pinned wording removes the tension.
- P7, line 33, wording nit. "immediate contains the r19 pattern" means only r19's 9-byte subsequence `63deadbeef14601057` (r19 offsets 6-14), not r19's 18 bytes; r24 has no `5b`. Lines 59-60 already imply this.

## Impacted axes
C1 coverage K (admission of C09): no Q05, Q07 or Q10 failure. Every gap is a citation or in-entry-derivation gap (Q01/Q11), and each underlying fact is true on the bytes and records. No saved record or fixture was touched; reads only.

## Smallest safe correction
- Line 98: cite `kasegi-shokunin/corpus/knowledge/operator-queue.md:58` and `PROVINCE.md:3`.
- Line 83: replace with "is not read as origin".
- Reproduce: add `rec['provider']['version']`, `rec['authority']`, `[i for i,b in enumerate(d) if b==0x5b]` and r24 `d[8]` to the print.
- Line 74: cite the four ExecEvmOracle reports.
- Line 56: change to "was false for rea-agents@6.4.0/evmole@0.9.3 on r26 (run 2026-10-12)".

VERDICT: PARTIAL — no sentence generalises past the seven records and fixtures, and nothing is contradicted. One cross-lane cite (line 98) and one unsourced label semantics (line 83) overstate their basis, and four in-entry derivation gaps make the Q06/Q11 table rows slightly overclaim. Installs: none.
