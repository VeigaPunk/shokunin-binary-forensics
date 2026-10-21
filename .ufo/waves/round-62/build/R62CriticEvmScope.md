RESULT: COMPLETE — C09 scope attack on the intended round-62 EVM candidate (critic; no admission judged, README untouched)

Seat RevengerR61-2.R62CriticEvmScope · 2026-10-21 · frozen a3498e25ad87bf756288812d0ea7c474b09433c7 (tree f53a42f2eb5baa9fa999f8bcf2b7e8145d2309c7),
`git -C …/revenger-shokunin archive a3498e25… | tar -x -C /fast/scratch/hyaku/revenger-r62/R62CriticEvmScope/tree`.
Candidate `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md` did not exist in the tree or in R62EvmEntry scratch at review time,
so this attacks the scope frozen in `reports/round-62/claims.md:21-26`, not a draft. No bytecode, provider, REA, RPC or fixture JS run.

## Evidence
- Readout: `cd / && python3 -B …/R62CriticEvmScope/scope_probe.py …/tree …/src` → exit 0 (Python 3.14.8), full output `…/R62CriticEvmScope/scope_probe.out`.
  It ports S028 `get_valid_jump_destinations` literally (opcode set parsed from `__init__.py`: `ops_defined=149`) and asserts it equals the PUSH-skipping walk 7/7.
- Sources opened by this seat 2026-10-21T18:01:09Z, raw.githubusercontent.com/ethereum/execution-specs/v2.20.0/src/ethereum/forks/osaka/vm/:
  `runtime.py` a2801c41…aef8, `instructions/__init__.py` 49dd6155…3724 (both equal the round-61 pins), `instructions/control_flow.py` d82b9d3a…3f19.
- Key output lines (verbatim):
  - `fits_of_7 {'R': 4, 'W': 6, 'L': 7, 'C': 7, 'J': 7}`
  - r26 `shapes=[{'push4': 7, 'sel': 'deadbeef', 'jumpi': 15, 'push1_imm_off': 14, 'dest': 17}] s028_valid=[17] reachable_from_0=[0]` and `saved=[]`
  - r24 `raw/insn/in-imm 0x63=(1, 0, [1]) 0x5b=(0, 0, []) 0x57=(1, 0, [9]) 0x14=(1, 0, [6])`; `pattern_starts=[1] spans=[(1, 9)] d[8]=0x10 d[16]=0x00 insn_starts=[0, 33, 34]`
  - r19 `carrier=39B/294e6fd2e041 decoded=18B/d1086bce3214 subject_matches=['carrier'] bytecode_sha_is_decoded=True`
  - all 7: `undefined_starts=[]`, `flags=inferred/unknown/not-performed kind=unknown hardfork=unknown authenticity=unknown`, labels `('abi', 'payable', '')` where non-empty
  - scratch-only bytes (not lane fixtures, no provider run): `P_jump_over_stop W [('deadbeef', 17)] L [] C [('deadbeef', 17)]`; `P_skip_shape_before_stop W [('deadbeef', 12)] L [('deadbeef', 12)] C []`
  - `hashlib_sha3_256(b"") a7ffc6f8bf1ed766 != keccak256("") c5d2460186f7233c` (the Keccak value is a recorded constant, not computed)
- Record text (all seven `normalized_result.limitations`): [2] "Empty results do not prove the absence of callable dispatch."; [3] "Bytecode kind, hardfork and deployed-contract authenticity are unknown."; [4] "Original carrier and decoded bytecode SHA-256 are distinct identities; SHA-256 is not the Ethereum Keccak code hash."
- Spec text: runtime.py:26-30 defines validity as three conditions on the destination (in range, `JUMPDEST`, not PUSH data). Nothing about reachability.
  control_flow.py:83-84 pops `jump_dest` before `conditional_value`; :90-95 checks the valid set only when the condition is nonzero.

## Counterexamples to overreach (impacted axes: coverage via Q01/Q07/Q09/Q10/Q11; no harm axis touched)
1. Provider method or cause (Q07, Q04). Three rules fit all seven saved outputs: L (shape before the first STOP), C (reachable from pc 0) and J (raw bytes, ignores PUSH immediates).
   So no sentence may attribute PUSH-data exclusion, reachability or a STOP bound to evmole/REA. That includes r24: J ignores immediates and still fits r24.
   This repeats and strengthens round-61 W3EvmR24Confound (rule J) and W3EvmTwoRulesFit. Two scratch byte strings do separate L from C, but they are hypotheticals, not lane evidence, and no provider may run this round.
2. Dispatch validity (Q01, Q10). r26's destination 17 is in the S028 valid set, but reachable_from_0=[0].
   "Valid" can only mean set membership. "Valid dispatch", "statically valid dispatch pattern", or any reachability or branch-taken reading overreaches S028 (tier A for byte boundaries only, per assignment).
3. Callability or interface (Q05, Q09). Runtime is not performed and completeness is unknown 7/7, and limitation[2] disclaims absence.
   "Callable", "dispatches to", "interface present/absent" have no support. Only "the saved record lists N functions" survives.
4. JUMPI operand role (Q01 scope). The fact that the PUSH1 value is the destination operand comes from control_flow.py:83-84, not from the reserved S028 scope "opcode source + runtime boundary scan".
   The entry must either include control_flow.py in the S028 row when it is opened, or use the byte-only phrase "PUSH1 immediate value immediately before the JUMPI byte".
5. Selector semantics (Q01). S018 is not among the reserved round-62 sources, so "not Keccak-derived" or "test constants" lacks a round-opened tier-A row. Label authorship as recorded (LOG.md:234, 267, 278) or omit it.
   Stdlib `hashlib.sha3_256` is not Keccak-256, so any in-entry "check" built on it would be false.
6. r24 "embedded JUMPI target" (Q11 wording). Offsets 1–32 are data (`insn_starts=[0, 33, 34]`). Safe wording: "byte 8 inside the immediate is 0x10".
   The four r24 values that round-61 lacked (count, span, raw 0x5B, byte 8) are all printable by one line each (A2 in the proposal).
7. Digest scope (Q09). r19's subject digest is the carrier digest, not the decoded-bytes digest. A disjunctive `subject_eq_bytes` check hides this (round-61 W3EvmFlagsDigest). Print which digest matched.
8. Generality (Q10). Equivalence of the walk with S028 is shown only on these seven files (`undefined_starts=[]`, no PUSH0 or truncated push), and the records say `hardfork=unknown`.
   Scope the claim to "S028 osaka v2.20.0 on these seven files"; do not claim it holds across forks.
9. Registered falsification (Q07). The round-62 claims pre-register no provider prediction, and round-61's "every valid pattern" wording was untraceable (W3EvmR25R26Targets F5).
   r26 can be stated only as an observation pair, not as a falsified registered hypothesis.
10. Output equality is not completeness (Q11, Q13). Provenance equality guards printed tokens only. Each prose value needs a mapped printed token or a "recorded" label.
    Keep: three reported pairs ≠ three records ≠ two distinct positive byte strings; r24 raw 0x63 = 1 ≠ PUSH4 instructions = 0; occurrence count 1 ≠ span length 9 ≠ `embedded_pattern_offsets` length 2.

11. Kasegi cross-lane cite (Q01/Q10; round-61 routed defect 2). R62ConnectKasegi's note, which I checked read-only at kasegi HEAD 8bf980721554d2d24bcc83e2e0996e0c27684a06:
    - `PROVINCE.md:25` is only the "**Refuses:**" line; grep -ciE 'deploy|identit|claimab|bytecode|EVM' finds 0 lines in that file.
    - `:3` is the domain line and `:42` reads "Sibling lanes are reported, not absorbed:".
    - `operator-queue.md:58` is one per-program "Deployed-code check required" row; kasegi's own `lessons/round-10.md:26` calls it "checklist-level".
    - `claim-gates.md` has 0 deploy/bytecode/pin hits.
    Recommendation (rev. after R62ConnectKasegi rev.2 withdrew its fallback): omit kasegi from the C09 entry, with no fallback citation. Never cite `:58` as support.
    Also delete any blanket negative such as "no sibling lane's ground is claimed": kaidoku `corpus/README.md:38` is an EVM row with status `held` (kaidoku HEAD 69e82c48), so that negative is unverified.
    The Q10 cell credits no sibling source. "Seven" and "one provider version" are counts that must appear in the entry's printed output or be labelled recorded.
    Rechecked: kasegi `PROVINCE.md` has 0 hits for "revenger" and 0 for "deployed"; `:44-47` lists chousa, kagi, kake and kengaku only.

## Fixable vs tradeoff
All ten are fixable by narrowing the wording or adding a printed token. None needs a fixture or record change. The one tradeoff the judge must reject outright is any provider-method or cause sentence (item 1): it cannot be fixed this round, because separating L, C and J requires a new fixture plus a provider run, both outside round-62 bounds.

## Proposed artifact (scratch, not an entry)
`/fast/scratch/hyaku/revenger-r62/R62CriticEvmScope/evm-scope-delimitation.md` contains:
- table A: seven surviving narrow claims, each with the printed token it requires;
- table B: eleven overreach patterns, each with its counterexample and safe wording;
- section C: count conflations to avoid.
`scope_probe.py` can serve as an independent oracle for the entry's token map. It is not a substitute for the entry's own in-entry derivation (Q11).

## Preservation
I read only the prior rejected entry, the round-61 counterexamples and the verifier lesson; none was edited. Rejected `evm-saved-interface-candidates.md` is not cited as factual support.
README C09 stays uncovered; nothing here claims admission. Live tree: no edits (only this report written).

Installs: none (pre-present python3 3.14.8, curl, git).
