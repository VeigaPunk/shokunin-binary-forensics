GRADE: BROKEN — whole-entry Q11 audit, corpus/knowledge/round-62-evm-dispatch-byte-evidence.md @ d9776195

Frozen target d97761952be256d145d298022de03091de91d358 (claim base 5bd4a90fc1a34caa94496601b60537b3aab12301; pre-reg a3498e25ad87bf756288812d0ea7c474b09433c7). Candidate SHA-256 6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e (identical in worktree and archived tree). Scratch /fast/scratch/hyaku/revenger-r62/R62FEvmQ11Inventory (git archive of d9776195; TMPDIR=<seat>/tmp; cwd=/ for the run). Entry paths below are corpus/knowledge/round-62-evm-dispatch-byte-evidence.md.

FAILURES (severity order)

F1 (material) — r24 role claim contradicted by the entry's own instruction walk. :101-108 (Observation 6): "The dispatch-like pattern — derived from the files' own bytes, from a PUSH4 opcode through a JUMPI opcode inclusive — is 63deadbeef14601057 … Inside that occurrence the PUSH1 opcode byte is at offset 7 and its operand byte at offset 8 has value 16". In-entry output (## Provenance, r24 line): "instruction_opcode_counts":{"0x0":1,"0x50":1,"0x7f":1},"instructions":[[0,127,"63deadbeef146010570000000000000000000000000000000000000000000000"],[33,80,""],[34,0,""]],"jumpi_with_preceding_push1":[],"raw_0x5b_offsets":[]. OBSERVATION: r24 has instructions at 0, 33, 34 only; no 0x60 and no 0x57 opcode; offsets 7/8 are bytes 7/8 of the PUSH32 immediate. The value 7 comes from `po = s + pattern.index(P1)` (byte search in the 9-byte pattern), not from the walk. Frozen-tree corpus/fixtures/evm-r24/truth.json: "instruction_stream":["PUSH32 at 0 with immediate bytes 1..32","POP at 33","STOP at 34"],"executable_push4_count":0,"comparison_or_jump_instruction":false,"note":"All opcode-looking bytes lie inside PUSH32 immediate". The entry records no r24 structural fact; S028's scope is exactly "Distinguish a raw opcode-looking byte from an instruction" (corpus/SOURCES.md:42). Values 7/8/16 are true; the asserted opcode/operand ROLE is not.

F2 (material) — "derived from the files' own bytes" (plural) is false for 4 of 7 files. Code: `def derive_pattern(code): """The dispatch-like pattern, from the file's own PUSH4..JUMPI bytes."""` with the single call `pattern = derive_pattern(bytes.fromhex(r19[2:-1].decode("ascii")))`; each case then gets `pattern_block(code, pattern)` — the pattern is r19-derived and only searched elsewhere. In-entry output: r22.pattern.occurrence_count 0 (own PUSH4@7..JUMPI@15 bytes 63aaaaaaaa14601e57), r23 0 (PUSH4@0, no JUMPI), r24 0, r26 0 (own 63deadbeef14601157); only r21/r25 coincide with their own PUSH4..JUMPI run. Q03 row :192 repeats the claim.

F3 (material) — one prose claim has no in-entry derivation (correct value, underived). :147-148 (Unknown): "The `dispatch`, argument and state-mutability labels in the saved records are the provider's own recorded values, not interpreted here." The readout prints only selector+offset per function (`norm = [[f["selector"], f["bytecode_offset"]] …]`, `raw = [[f["selector"], f["bytecodeOffset"]] …]`); no such field appears in the printed stdout and no inventory row names one. True in the saved record (frozen tree: normalized functions carry "dispatch":"abi","inferred_arguments":"","inferred_state_mutability":"payable"; raw carries "arguments","stateMutability") but underived in-entry, and it falsifies the entry's own framing :23-25 ("Every value in the prose is a field of the printed output").

F4 (moderate) — the self-claim :200 ("`## Evidence inventory` names the field and the value for each claim") fails for: (a) :123-126 covers r19, r21, r22 but names only r19./r22. fields (r21 has no jumpi / valid_jumpdest / raw_0x5b row); (b) :131-135 "each record's own kind, deployment_authenticity and hardfork fields are unknown (`r19.recorded.bytecode.kind`)" names one of seven records; (c) :65-75 and :159-162 say "Each [record]" / "the saved files" while naming r19 fields only. All values verified true for all seven records at the frozen tree.

F5 (minor) — inventory row "r19 artifact bytes and encoding | `r19.recorded.artifact.bytes` | 39": the named field carries bytes only; the encoding value ("hex", printed at r19.recorded.artifact.encoding) is neither named nor valued.

F6 (minor) — internal inconsistency: :92 "The four records that report no pair. r23, r24, r25 and r26" vs :139 "Why r23, r25 and r26 report no pair" (r24 omitted, unexplained).

F7 (nit) — Q04 row :193 "The only tool named is the provider" vs the same entry naming python3 3.14.8, `git archive` and corpus/verify_evm_evidence.py (:164).

VERIFIED CLEAN (audit coverage)
- 67/67 inventory rows: each cited field resolves in the printed stdout and its value matches exactly (scripted check over a fresh run's JSON).
- The entry's own Reproduce block, extracted verbatim from the frozen file, re-run against the git-archived d9776195 tree, cwd=/, TMPDIR set: exit 0, stderr 0 bytes, 8 stdout lines, byte-identical to the ## Provenance block (diff empty). "exact, complete and untruncated" holds; Python 3.14.8 as recorded.
- S028 side fully verified: all nine opcode constants and runtime.py :22/:28/:29-30/:64 match exactly; tag v2.20.0 dereferences to commit 2004296f2ffcbcebcd00f41152d33e8dfda0922a (matches header and SOURCES.md:42); file digests 49dd6155…/a2801c41… match SOURCES.md:42 and the lane's own source-snapshots.
- r19 fixture.hex is literally "0x"+36 hex+"\n" (39 bytes) → the "0x-prefixed ASCII hex" role holds.
- corpus/fixtures and corpus/live untouched between a3498e25 and d9776195 → the recorded lane-base run equals the frozen-state run.
- Cross-lane citations exist and quote verbatim: corpus/lessons/round-62.md:29 (ADJ-06 row) and .ufo/waves/round-62/build/R62DebtExistingFiles.md:33 (§4 ADJ-06).
- No rejected round-61 row cited; S028/S031 exist in corpus/SOURCES.md:42,45 (mined).

INFERENCE
- F1–F3 are the Q11 failures: two role/derivation-scope misstatements and one correct-but-underived claim. The entry's own Q11 "pass" (:200) is not supportable as written. No numeric, byte, count, offset or digest value was found wrong, so the failures are role labels, derivation scope and inventory completeness — locally repairable, not a wholesale rejection. No repair made by me.

UNKNOWN
- Whether "the PUSH1 opcode byte" was meant as pure byte-value naming; either way no r24 structural fact is recorded, so the referent stays unrecorded and the contradiction with the entry's own walk stands.
- I did not adjudicate Q01–Q13 beyond the Q11/Q03/Q06/Q07 referent checks in scope.
- No bytecode execution, chain/RPC call, producer call or fixture-JS run was performed; the readout only reads bytes and JSON.

MINIMAL CORRECTION (named only; not applied)
1. Observation 6: state the pattern is derived once from r19's PUSH4..JUMPI bytes and searched as a raw byte string elsewhere; state that in r24 the occurrence (1-9) lies inside the PUSH32 immediate (no executable PUSH4/JUMPI; walk = 0, 33, 34) and that 7/8 are pattern-byte positions, not instruction offsets.
2. Print or cite the dispatch/argument/state-mutability fields, or drop :147-148.
3. Add inventory rows for the fields the claims span (r21 jumpi/valid_jumpdest/raw_0x5b; the other six records' kind/deployment_authenticity/hardfork) or scope those claims to r19.
4. Fix the "r19 artifact bytes and encoding" row; reconcile :139 with :92.

VERDICT: BROKEN for the whole-entry Q11 criterion on this frozen target (F1–F3 material; F4–F7 minor). Do not admit as-is; a focused correction plus re-review by a fresh-wave seat on the corrected bytes is the narrow path. No live production edits, no Git index/history mutation, no subagents, no writes outside this report path and the seat scratch.
Installs: none — no package installed; python3 3.14.8 (pre-existing) used read-only; no pacman/uv/cargo/npm action.
