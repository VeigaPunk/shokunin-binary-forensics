GRADE: PARTIAL — corpus/knowledge/round-62-evm-dispatch-byte-evidence.md (Unknown / Limitations / Inference)

Seat `RevengerR61-2.R62FEvmUnknowns` · critic · fresh falsify wave, revenger round62 attempt1. Not the author or corrector.
Frozen revision `d97761952be256d145d298022de03091de91d358` (`git rev-parse` ok); candidate blob `3e58a91fa8aee579aff7f873ce55061ae8f92cdf`,
file sha256 `6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e` (450 lines). Extracted with `git -C …/revenger-shokunin archive d977619…`
into `/fast/scratch/hyaku/revenger-r62/R62FEvmUnknowns/tree`. I ran one bounded check: the entry's own `## Reproduce` block
(cwd=/, TMPDIR under own scratch, Python 3.14.8). No bytecode or fixture-JS execution, no producer/REA/chain call, no edits. Installs: none.

## Primary checks (observation)
- `python3 -B readout.py <tree>` → `exit=0`, stderr 0 lines, 8 stdout lines; `cmp out.txt provenance.txt` → `IDENTICAL` to the entry's `## Provenance` block (:441-450).
- I parsed the per-case `recorded` objects from that output. All seven print `evmole@0.9.3`, `discovery_completeness=unknown`, and `kind`/`hardfork`/`deployment_authenticity` = `unknown`.
  `jumpi_with_preceding_push1`: r19 `[[14,16,True]]`, r21 `[[14,16,True]]`, r22 `[[15,30,True],[25,32,True]]`, r23 `[]`, r24 `[]`, r25 `[[15,16,False]]`, r26 `[[15,17,True]]`.
- The saved records (read-only) contain `limitations[2]` in all seven: "Recovered selectors, argument strings and mutability are upstream inferences, not verified ABI signatures or names. Empty results do not prove the absence of callable dispatch."
- `git diff --stat a3498e25…d977619 -- corpus/fixtures corpus/live corpus/knowledge` → only the two round-62 knowledge files (`2 files changed, 746 insertions(+)`). The Limitations line :171-173 (no fixture or live file modified) holds.
- `rg -n 'dispatch"|payable|mutability|inferred_arg|"arguments"|stateMutab' <entry>` → the only hit is `147:`. The readout never reads or prints these keys.

## Findings
F1 — r24 is missing from the "why no pair" Unknown, which leaves an unreproduced cause implied (Q07, Q10; nonfatal).
- Observation 5 (:92-95) names four empty records: r23, r24, r25, r26. Unknown :139-140 lists only "Why r23, r25 and r26 report no pair".
- Observation 6 (:97-112) puts two candidate explanations for r24 side by side, neither stated as a cause: the pattern sits inside the PUSH32 immediate (`r24.instruction_opcode_counts` `{"0x0":1,"0x50":1,"0x7f":1}`), and the embedded target byte at offset 16 is `0x00`, not `0x5b`.
- With r24 left out of the Unknown list, a reader takes r24's emptiness as explained. It is not: no producer ran, and a build critic shows rules that ignore immediates also fit r24.
  Evidence: `.ufo/waves/round-62/build/R62CriticEvmScope.md:14` `fits_of_7 {... 'J': 7}` and `:27` "That includes r24: J ignores immediates and still fits r24."
- The build oracle's Unknown covered all four: `R62EvmCandidatesOracle.md:73` "Why r23–r26 report no candidate is not answered here".
- The author's Q07 basis (:196, "No cause is stated for any empty pair list") is literally true, but the Unknown inventory does not match it.
- Counterexample: the same no-cause standard cannot exclude r24 and still include r23, since both rest on byte facts with no producer reproduction.
- Smallest correction: change :139 to "Why r23, r24, r25 and r26 report no pair".

F2 — the label bullet attributes origin and states field existence the entry never derives (Q09/Q04 wording; Q11 field-existence audit; nonfatal).
- Unknown :147-148: "The `dispatch`, argument and state-mutability labels in the saved records are the provider's own recorded values".
- (a) "the provider's own" assigns producer origin to saved-record content. That contradicts the entry's own statement at :73-75: "does not authenticate them and claims no origin, completeness or authenticity from them".
- (b) The existence and names of these fields appear only in prose. The block prints none of them, so they are recorded, not derived. The record's own text says "upstream inferences".
- A build-stage revision printed these labels (`R62SimplifyEntrySurface.md:45` "`payable` (3) is the recorded `dispatch`/`inferred_state_mutability` field values printed"). The frozen block dropped them; the prose kept the claim.
- Smallest correction: "The saved records also contain `dispatch`, argument and state-mutability fields (recorded, not printed, not interpreted here)."

F3 — the entry's self-claim that the inventory is complete is false; the values themselves are derived (nonfatal).
- The entry claims at :23-25, and in the Q11 row at :200, that the inventory "names the field and the value for each claim". Four counterexamples:
- (i) Inference :123-126 claims r19, r21 and r22 but cites only `r19`/`r22.jumpi_with_preceding_push1`. No `r21.jumpi_with_preceding_push1` row exists.
- (ii) :134-135 says "each record's own `kind`, `deployment_authenticity` and `hardfork` fields are `unknown`" but cites only `r19.recorded.bytecode.kind`. Inventory row :241 maps three fields to one path, with no hardfork, authenticity, or r21–r26 path.
- (iii) Unknown :142-143 says "every record carries `discovery_completeness=unknown`" and cites r19 only.
- (iv) Limitations :157 says "one recorded provider version". No summary field computes distinctness; the inventory has r19 only (:232).
- Every one of these values is in the printed output for all seven cases (checked above), so the Q11 derivation and output exist in-entry and the values are correct. The defect is citation precision.
- Smallest correction: add per-case rows (or a summary field) for r21 jumpi, `recorded.bytecode.hardfork`/`deployment_authenticity`, `recorded.discovery_completeness` and `recorded.provider_version` across the seven cases. Alternatively, narrow the :23-25 and :200 wording.

## Held under attack (observation)
- Empty is not absence (:141-143): this matches all seven records (`discovery_completeness=unknown`, limitation[2]). There is no hidden absence claim.
- `evidence_id` (:144-146): the entry abstains ("does not address, recompute or authenticate… claims no formula"). It does not claim the IDs cannot be recomputed, so the Unknown is not wrong.
- Compiled-bytecode/signature bullet (:150-153): a scope exclusion, not an absence finding. The signature non-claim matches limitation[2] "not verified ABI signatures or names".
- Inference :123-130 is a three-output correspondence, bounded as "not a definition of the field for any other carrier". Observation 7 shows r26 (operand 17 is a JUMPDEST, yet empty) against the converse rule, so the narrow byte-vs-record insight survives with no universal provider reading.
- Limitations :163-170 credit no verifier and call the block not deletion-sensitive (Q13). There is no present-tense capability claim (Q05). Lines :26-29 disclaim producer method, chain, and present capability.

## Inference / unknown
- [INFERENCE] F1 does not void admission on its own, because no cause is asserted. But it repeats the round-61 r24 rule-fit trap (W3EvmR24Confound) by implication, so L1 should require the one-word fix before any C09 flip.
- Unknown: whether L1 reads F2(a) as a Q09 violation (BROKEN) rather than wording. I grade it nonfatal because the fields carry no load-bearing value.

VERDICT: PARTIAL — no contradiction with bytes or records, and Q11 derivations are present. Three nonfatal defects: Q07/Q10 (F1), Q09/Q04 wording (F2), and the inventory self-claim (F3). Corrections above; no repair made. Installs: none.
