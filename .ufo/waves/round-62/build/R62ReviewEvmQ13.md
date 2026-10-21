RESULT: PARTIAL

Seat RevengerR61-2.R62ReviewEvmQ13 (reviewer). Scope: no-credit boundary for the new C09
EVM manual readout; why diffing printed output is manual evidence, not an automatic
deletion-sensitive guard; necessary n/a explanations vs false passes. Frozen
a3498e25ad87bf756288812d0ea7c474b09433c7 extracted to
/fast/scratch/hyaku/revenger-r62/R62ReviewEvmQ13/frozen. No live production edit; corpus
byte-preserved (`git status --porcelain corpus/` and `git diff --stat a3498e2 -- corpus/`
both empty). README C04/C09 remain `uncovered`; no admission claimed. Full proposal
(three-tier scheme, 9-clause table with reasons, per-clause detail, all dispositions,
probe commands): /fast/scratch/hyaku/revenger-r62/R62ReviewEvmQ13/proposed-no-credit-boundary.md

EVIDENCE READ
- `round-61/falsify-w3/W3EvmQTable.md` — GRADE BROKEN on the rejected C09 entry: F1 (:6) r24
span premise not re-derived in-entry; F2 (:10) the `## Reproduce` block credited for every
value while 2 of 7 clause deletions leave stdout byte-identical at exit 0, no clause named
unguarded; F5 "three reported pairs" contradicts the block's own 4 tuples; VERDICT (:31).
- `round-61/falsify-w3/W3EvmVerifierCredit.md` — GRADE HOLDS: KILLED 0/37, SURVIVED 37/37
(:59), verifier sha256 8265a22f…0b49 unchanged (:11), r19-only scope.

REPRODUCTION (independent, frozen tree, all probes in scratch)
- Prior C09 block: pristine exit 0, stdout byte-identical to its `## Provenance` (PROV==OUT
True); 8 AST-targeted literal clause deletions -> 6 detected, 2 survived (P4
`ins[k-1][1]==0x60`, P8 subject-digest binding) — the same two clauses W3EvmQTable:10 names.
probe/prior-deletion-results.json
- Saved verifier `corpus/verify_evm_evidence.py` in-tree: 37 require-conjuncts by AST, each
deleted -> 0/37 killed, 37/37 survived; file sha256 identical before/after (8265a22f…0b49).
Confirms W3EvmVerifierCredit:59. probe/vtree, restored byte-equal.
- NEW candidate readout `R62EvmEntry/readout.py` sha256 0a08dbd1…d40834f (pristine stdout
37762 B, exit 0, stderr empty): 22 AST-targeted single-clause deletions -> **13 detected, 9
survive**: N04 PUSH1-precedes-JUMPI, N06 candidate offset in JUMPDEST set, N08 candidate
offset equals some JUMPI target, N09 subject digest==sha256(carrier), N12 bytecode
digest==sha256(decoded), N13 recorded bytecode hex==decoded hex, N19 raw 0x5B set coincides
with instruction JUMPDEST set, N20 r19 decoded == r21 raw, N22 truth.json
push4_opcode_offset matches the walk. probe/new/deletion-results-final.json

F1 (decisive) — A stdout diff is blind to a clause whose printed value is constant across the
corpus, so "diff the printed output" is manual evidence, not an automatic deletion-sensitive
guard. Every survivor prints a constant here: `subject==carrier:True` 7/7; `bytecode==decoded:
True` 7/7; `recorded_bytecode_hex==decoded:True` 7/7; `in_jumpdest_set=True` 4/4;
`equals_some_jumpi_target=True` 4/4; `coincide=True` 7/7; `is_push4_opcode_offset:False` 4/4;
`r19_decoded_equals_r21_raw:True`; `match=True`. Deleting such a clause leaves stdout
byte-identical, so no diff of printed output can see it. Contrast N05 `target in jd`, which
varies (r25 prints False) and IS detected. Blindness 9 of 22 = 41%. Corroboration: with a
synthetic fixture whose JUMPI is preceded by PUSH2, N04 becomes detected — the clause is real,
the corpus simply cannot exercise it.

F2 — Exit status carries no signal, so "run and diff" is an operator comparison. The readout
asserts nothing on any compared value (only `assert text.startswith("0x")`). Corrupting the r19
fixture byte AND the r19 record's `bytecode_offset` 16->17 leaves **exit 0** with 38 differing
stdout lines (probe/corrupt2). A guard needs a nonzero exit.

F3 — Two recheck-command defects the entry must resolve. (a) stdout is path-dependent: line 2
prints `root: <resolved path>`; the same tree at two paths differs on that line alone, so a
byte-for-byte diff against a stored transcript fails for a reason unrelated to any clause.
(b) `spec_anchor:` lines print only when argv[2] supplies `osaka_v220_instructions___init__.py`
+ `osaka_v220_runtime.py` (0 lines without, 11 with); those copies are not committed (repo
`find` returns none), so the spec anchors are not re-verifiable from the repo alone.

F4 — Necessary n/a explanations rather than false passes (proposed, not applied).
- Q13 is NOT n/a if the entry's `recheck:` header names the readout: QUALITY.md:27 scopes Q13
to "a verifier **or recheck** command". Then the honest cell is limited credit (13 of 22)
**plus naming the 9 unguarded**. Writing "Q13 n/a — no verifier cited" while the header names
the block whose 9 clauses are unguarded is a false pass wearing an n/a.
- Q13 n/a is unavailable on the alternative route: no deletion-sensitive command exists here
for r21-r26 (`verify_evm_evidence.py` reads r19 only, 0/37).
- Q12 n/a is legitimate only if the entry does NOT cite the rejected round-61 entry or its
Reproduce output as factual support (claims.md forbids it); citing it makes Q12 applicable and
it fails.
- Q05 n/a only if no present-tense capability claim: the readout prints recorded
operation/provider/evidence_id, plus `producer_version_strings_in_record_bytes: rea-agents=0
6.4.0=0 evmole=2 0.9.3=1` and a per-round `round_ledger_line_with_producer_command` naming
`rea-agents@6.4.0`. That is ledger prose, so any `6.4.0` claim must be labelled recorded with
its source row, not presented as re-derived.
- Q07 n/a only if the entry asserts no cause for any empty candidate list.
- Q04: the readout is a manual byte walk and must be labelled manual.

F5 — The new readout already fixes what F1/F5 of the prior review flagged: the r24 `[1, 9]`
inclusive span IS derived in-entry (`r24_pattern_occurrence_starts: [1] count=1`,
`r24_pattern_inclusive_spans: [[1, 9]]`), matching `truth.json` `embedded_pattern_offsets [1,9]`
and my independent byte search (pattern `63deadbeef14601057`, len 9, one occurrence at 1);
counts are disambiguated (`candidate_observations_total: 4` vs `distinct_selector_offset_pairs:
3`); no truncated digests (every `sha256=` and `sha256_field` value 64 hex chars;
`recorded_evidence_id` the full 70-char id).

RESIDUAL RISK / UNKNOWNS
1. Snapshot drift: the executor's readout changed twice while this review ran (0a08dbd1… is the
measured snapshot). Any further change voids the clause list and requires re-running
`probe/new/delmut2.py`. 13/22 and 9/22 are a lower bound on detection, upper bound on blindness.
2. I measured the executable `readout.py`, not the written `candidate.md` (100400 B, sha256
e1542232…). Every Q-row disposition is a proposal; the entry's wording decides whether Q13 is a
limited credit or a false pass.
3. N04's unguardedness is corpus-vacuous, not code-vacuous; whether such a fixture may be
authored is outside my scope and would change the count. My 22-clause enumeration is my own AST
selection, not a proof of completeness.
4. Cross-tree: N06/N08 detected only on a mutated record; N09/N12/N13 only on mutated
fixture/record trees; N19/N20/N22 constant on every tree I built.
5. I did not open S028-S031 source rows (L1 owns source rows); I read the executor's fetched spec
copies only to confirm anchor lines exist and print. Whether those copies are the committed
tier-A artifact is unverified here. I did not evaluate the C04 candidate.

PROPOSED CHANGES (none applied): the scratch proposal above only. No repo file created or edited
except this report.

Installs / updates: none. Toolchain as found: python3 3.14.8 (/usr/bin/python3), git, coreutils
diff. No pacman/uv/cargo/npm action, no service restart.

VERDICT: the new EVM readout is materially better than the rejected C09 entry (F5), but its
`## Reproduce` block cannot be credited as an automatic guard: 9 of 22 check clauses survive
deletion with byte-identical stdout at exit 0, and exit status is 0 even under fixture and record
corruption. Bind Tier 1 derivation / Tier 2 guard for the 13 detected clauses / Tier 3
named-unguarded for N04, N06, N08, N09, N12, N13, N19, N20, N22 — Q13 as a limited credit, not
n/a and not a false pass, unless the `recheck:` header is changed to cite something else AND that
something is shown deletion-sensitive (no such command exists for r21-r26). README C04/C09 remain
uncovered; no admission claimed.
