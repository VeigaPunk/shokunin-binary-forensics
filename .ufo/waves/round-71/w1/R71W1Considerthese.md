PROPOSAL-ONLY — ledgering proposal 1 is useful; round-71 next-gate checks are not yet available, so do not label any adoption held.

## Evidence and bounded ledger

Read-only basis: `considerthese/2026-10-24.md`, `considerthese/2026-10-25.md`, `considerthese/2026-10-26.md`, `reports/round-71/claims.md`, and `reports/round-71/pre-registration.txt`. Proposal 1 in the Oct 26 note asks to track each considerthese proposal through later adoption and the next gate. The note explicitly reports four round-70 adoptions (Oct 26, lines 27–28); the ledger below is limited to those examples and this proposed ledger itself. “Checked” means evidence of execution at adoption is recorded; “next-gate check” remains pending absent round-71 final-gate evidence.

| Proposal (origin) | Proposed → acted evidence | Checked at adoption | Checked at next gate |
|---|---|---|---|
| Oct 24 #3, claim hit-rate ledger | Adopted in round 70 per Oct 26, lines 27–28. Oct 24 describes the proposal at line 35; Oct 26 says the ledger reads 11/18 by stricter per-predicate reading and 10/18 by SCORECARD-cell reading (line 27). | Yes: presence and two reported readings; they are distinct measures, not a single settled score. | Pending: round-71 gate outcome not in the read evidence. |
| Oct 25 #1, routed-repair carry-through | Adopted as `R70W2ConnRoutedCarry` per Oct 26, line 27; originating proposal is Oct 25, line 32. | Yes: adoption is named; no outcome for whether it caught or prevented missed repairs is established in these notes. | Pending. |
| Oct 25 #2, consecutive-falsification streak / deliberate approach change | Adopted as stdout-built entry per Oct 26, line 27; originating proposal is Oct 25, line 33. | Partial: round 70 entry is built from command outputs and 24 embedded blocks re-derive (`checked_blocks=24 problems=0`), Oct 26 line 26. This is evidence of the implementation form, not proof the C05 gate passed: the same line records C05 failed for the fifth pass on prose claims. | Pending. |
| Oct 25 #4, candidate Q-map completeness check | Adopted as `lint_entry.py` QMAP per Oct 26, line 27; originating proposal is Oct 25, line 35. | Yes: adoption is named. The cited notes do not provide a specific round-70 detection/hold outcome for the QMAP check. | Pending. |
| Oct 26 #1, proposal-adoption ledger (this proposal) | Proposed in Oct 26, lines 27–28; this report records prior adoptions and separates evidence at adoption from next-gate status. | Yes: this bounded ledger is drafted; do not infer an operational recurring process from one report. | Pending: check after the round-71 final gate, then update only from recorded gate evidence. |

## Interpretation / limits

The lesson window supports adopting a ledger that distinguishes adoption from demonstrated effect: round 70's generated-output work had measurable derivation evidence but did not prevent prose-driven C05 failures (Oct 26, line 26). The Oct 26 note itself identifies instruments/lint checks versus reporting tweaks as a hypothesis for learning, not a proven ranking (lines 27–28); this small, selectively reported ledger cannot establish comparative effectiveness. Round 71 remains pre-gate under the frozen contract, so no next-gate result is claimed. No source row was opened or added, no input was edited, and no source tree/campaign tool was used.

## Commands and touched surfaces

- Read frozen inputs: `claims.md` and `pre-registration.txt` (tool reads; no execution claim).
- Read lessons: `considerthese/2026-10-24.md`, `2026-10-25.md`, `2026-10-26.md` (tool reads; line references above).
- `mkdir -p /fast/scratch/hyaku/revenger-r71/R71W1Considerthese` → `scratch_ready=/fast/scratch/hyaku/revenger-r71/R71W1Considerthese`.
- Wrote only `.ufo/waves/round-71/w1/R71W1Considerthese.md` in the lane repo. No tests, gate, counter, or verifier were run. No installs.
- Scratch cleanup is performed before handoff.

Report: `.ufo/waves/round-71/w1/R71W1Considerthese.md`
