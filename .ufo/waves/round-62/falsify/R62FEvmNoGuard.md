GRADE: HOLDS — corpus/knowledge/round-62-evm-dispatch-byte-evidence.md, Q13 / no-guard boundary

Seat R62FEvmNoGuard (fresh falsify, critic; not author/corrector). Frozen revision
`d97761952be256d145d298022de03091de91d358` (rev-parse ^{commit} confirmed), extracted with
`git -C …/revenger-shokunin archive` into `/fast/scratch/hyaku/revenger-r62/R62FEvmNoGuard/tree`.
Candidate blob `3e58a91fa8aee579aff7f873ce55061ae8f92cdf`, file sha256
`6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e`. Claimbase 5bd4a90f…, pre-reg a3498e25… (read, not re-audited).

## Criterion under attack
`corpus/QUALITY.md:25` Q13: "A verifier or recheck command is credited in an entry only for the clauses whose
deletion its own run is shown to detect; other clauses are named as unguarded." Deletion sense per M22
(`lessons/round-61.md:38`): a verifier clause deleted, invisible to "the script's own run".

## Observation — every guard-relevant statement in the entry (rg -i guard|deletion|detect|verif|recheck|compar|admi)
- :10-13 `recheck:` header: names the readout and says Provenance "is the exact stdout"; it claims no detection.
- :163 "**No verifier is credited as a guard for any value in this entry.**"
- :164-168: `verify_evm_evidence.py` "is not cited as support, and every clause of this entry is unguarded by it",
  with an enumerated list (digests and scopes, walk, JUMPDEST set, raw 0x63/0x5b offsets, r24 pattern/spans/
  embedded operand/target byte, both candidate counts, "every inventory row").
- :168-170: the Reproduce block "is a manual comparison against the saved records; it is **not** claimed to be
  deletion-sensitive."
- :202 Q13 row: "No verifier is credited as a guard for any clause, and this entry's own block is not claimed to be deletion-sensitive".
- No other match for guard/detect/catch/fail/assert in the entry. Q03/Q06/Q11 rows ("re-derived … by the block",
  "field of the printed output") are derivation claims, not guard credit.
Result: the entry contains **zero guard-coverage claims**, so it credits no clause to either the verifier or the recheck command.

## Observation — the boundary is true, not merely asserted (archived copies, cwd=/, TMPDIR=<scratch>/tmp, Python 3.14.8)
1. Readout extracted from the entry's ```python block (sha256 740f321e…eb, 131 lines). `rg 'assert|raise|exit\('`
   shows only `:131 sys.exit(main())`, and `main` always returns 0. The script has no check clause and reads only
   `corpus/fixtures/` and `corpus/live/runs/` (entry :303-304), never the entry itself.
2. Baseline run `python3 -B readout.py <tree>`: exit 0, stderr 0 bytes; `cmp` stdout vs the extracted Provenance
   block → byte-identical (both sha256 aff3efda2691cb95ed7146292f602ba5dc5c40794e5c64efda3aaa7275f235bf).
3. One deletion mutant (`mutant_del_raw5b.py`: the `"raw_0x5b_offsets"` line removed): **exit 0, stderr 0**. Its
   stdout differs from Provenance, and `raw_0x5b_offsets` is absent from every line. The deletion survives the
   script's own run and is visible only through a manual diff against Provenance. That matches the entry's
   "manual comparison … not claimed to be deletion-sensitive", so crediting the block would have been an overcredit, and the entry does not credit it.
4. `corpus/verify_evm_evidence.py` (read, not run): it reads r19 only (:10-12), and its sole negative (:66-74) alters one
   saved offset to 6, which several conjuncts in :51-56 reject. No single-conjunct deletion is shown to be detected.
   Its non-credit is therefore correct under Q13 (the entry needs no demonstration to withhold credit).
5. Frozen `LOG.md:828` says "no verifier guard credit". `corpus/README.md:38` keeps C09 "uncovered". The README does
   not reference the new entry, so no guard or admission is implied for it outside the entry.

## Observation — recorded source facts vs defining authority labels; count validation vs admission
- `## Source facts (recorded)` (:31-42) says these are "recorded source facts, not values this entry re-derives",
  and the readout comment (:308-310) says "RECORDED from S028". The S028 constants are labelled as recorded, not as
  values derived in-entry, and are not credited as guards.
- The saved `authority`/`provider`/`evidence_id` fields are labelled recorded and "**not read** as origin, custody or
  authenticity" (:159-162, :131-135). A label is not used as a defining authority.
- `summary.*` counts (7 / 4 / 3) are printed readout fields. Admission is disclaimed at :15-17 (`admission-status: candidate`)
  and :186, :204-206. No probe/K count or count equality is offered as quality admission.

## Inference
- [INFERENCE] Q02's `recheck:` "re-verifies" only via a human diff of stdout against Provenance. The entry states this as manual, so it does not conflict with Q13.
- [INFERENCE] Non-material wording only, not a Q13 defect: the explicit per-clause "unguarded" list at :164-168 is attached
  to the verifier. For the recheck command, the zero credit is stated as a blanket sentence at :169-170 rather than
  per clause. Because zero clauses are credited, the blanket statement already names every clause as uncredited.

## Unknown / not audited here (other seats)
- Q11 per-value derivation completeness (for example, the Inference bullet :124-127 names r21 without citing an
  `r21.jumpi_with_preceding_push1` field), S028 line-anchor accuracy (code comment `runtime.py:22-69` versus quoted
  :22/:28/:29-30/:64), and other Q rows. None of these bear on the guard boundary.
- [INFERENCE] If C09 is later flipped, README:38 still lists `verify_evm_evidence.py` in the row. L1 should make sure
  the flipped row does not read as guard credit for the new entry. This is not a defect of the frozen candidate.

## Counterexample sought, not found
Any sentence crediting the verifier, the readout, its exit code, an output equality or a count as detecting a clause:
none. The strongest test (deleting a readout clause) shows the block can't act as a guard by itself, and the entry
never claims it does.

VERDICT: HOLDS for Q13/no-guard boundary on blob 3e58a91f… at d9776195…. No correction required.
Installs: none. Scratch: /fast/scratch/hyaku/revenger-r62/R62FEvmNoGuard/ (tree/, readout.py, mutant_del_raw5b.py,
provenance.txt, base.out, mut.out, tmp/). No repo, index or production edits.
