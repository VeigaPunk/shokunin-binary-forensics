RESULT: COMPLETE — M25 attribution and capture settled from frozen evidence; append-only addendum drafted in scratch, no round-61 text edited, no admission claim.

Seat RevengerR61-2.R62DebtM25Capture, leaf. Frozen revision `a3498e25ad87bf756288812d0ea7c474b09433c7` (verified as repo HEAD; `git archive` → `/fast/scratch/hyaku/revenger-r62/R62DebtM25Capture`). Reads only frozen bytes, `git show` of in-repo ancestors, and stdlib Python. Wrote: this report and one scratch addendum. No lane corpus write, no README change, no fixture/producer/EVM/JS execution, no installs.

## 1. What the old entry actually wrote (0b6ddf0, ancestor of frozen)

- `git show 0b6ddf0:corpus/knowledge/evm-saved-interface-candidates.md:88-89` verbatim: "`corpus/fixtures/evm-r24/truth.json` lists embedded-pattern offsets `[1, 9]`; the bytes contain the pattern only at 1 (fixture left unchanged)."
- Phrase counts on that blob: `inconsistent`, `two occurrences`, `defect` and `inclusive` each return 0 (`for s in inconsistent 'two occurrences' defect inclusive; do git show 0b6ddf0:corpus/knowledge/evm-saved-interface-candidates.md | grep -c "$s"; done` → four lines, each `0`). The entry never wrote the quoted claim; it juxtaposes `[1, 9]` with the single start at 1 and leaves the span unstated (implied discrepancy only).
- Its Q06 row at `0b6ddf0` entry:181 says "every fixture premise re-derived from the built bytes by the block above", but its `## Reproduce` prints only `raw_0x63=[1]` — no pattern search, no span.

## 2. What ScribeEntryEvm actually wrote

- Findings item 6, `ScribeEntryEvm.md:30-32`: "Byte search finds the 9-byte pattern once, at 1; byte 9 is 0x57 inside it. The second entry is inconsistent with the bytes (finding for the lane; not edited)."
- Its own draft entry did not say that; it left the field as "Why `truth.json` for r24 lists embedded-pattern offset 9 (author error or intent)" (`ScribeEntryEvm.md:99`).
- `ExecSelectorKeccak.md:26`: "Truth defect; not edited here."
- Settlement: the explicit false proposition is a build-seat finding (ScribeEntryEvm:31; ExecSelectorKeccak:26), not entry text. The frozen M25 row's joint attribution "the build seats and the C09 entry (at `0b6ddf0`) stated that … names two occurrences 'inconsistent with the bytes'" overstates the entry. Independently flagged by `falsify-w3/W3LessonMistakes.md:25` (FINDING 3) and `W3EvmR24SpanFix.md` F3; the quoted phrase traces to the seats and to the pre-correction row's own class cell ("fixture premise inconsistent with bytes", `0b6ddf0:corpus/lessons/round-61.md:41`).

## 3. The two M25 rows

- Original (`0b6ddf0:corpus/lessons/round-61.md:41`): class "fixture premise inconsistent with bytes … the pattern occurs only at 1"; captured-by "Q06 (existing)"; census `:43` "captured by a criterion 3 (Q12, Q13, Q06); `none` 2 (M23, M24 — process)".
- Rewrite (`0597e53`, frozen `corpus/lessons/round-61.md:41`): class attributes the two-occurrence quote to seats plus entry; captured-by "none — Q06 checks premises against bytes, not a reader's semantics for a truth field"; census `:43` "captured … 2 (Q12, Q13); `none` 3 (… M25)".
- So "Q06 vs none" is exactly the delta introduced by the 0597e53 correction, not an unresolved ambiguity in the evidence.

## 4. Capture settled: Q06, not none

- Q06 reject condition (`corpus/QUALITY.md:18`): "an offset, operand, size or count is stated from intent rather than from the built bytes." The disputed proposition — that `[1, 9]` names a second pattern occurrence at 9 — is a count/offset claim about the built bytes, and a byte search refutes it (section 5).
- The "reader's semantics for a truth field" rationale covers only the irreducibly intentional question ("why did the author write a span"), which stays recorded-only (`LOG.md:289`; `round-24/LEDGER.md:3`). It does not cover the knowable occurrence count; the row's own fix is a byte check (`[start, start+len-1]` comparison).
- The round's own Q06 PASS-IF required the span statement: `ReviewerEvmQuality.md:14` — "State that r24 `embedded_pattern_offsets: [1, 9]` is an inclusive span (… 'offsets 1–9'), not two occurrences." The entry passed Q06 anyway (`0b6ddf0` entry:181; frozen entry:188), and the Gate row records the basis as "Q03/Q06/Q11 `## Reproduce` re-run by L1, output identical" (`round-61.md:77`) — output equality, not the PASS-IF span statement. Correct form: "Q06 (existing; admission failed to enforce it)", the same convention as the M26/Q11 row (`round-61.md:128`).
- Census consequence for the new lesson only: captured 3 (Q12, Q13, Q06) / none 2 (M23, M24) — the original `0b6ddf0:43` count; the 0597e53 2/3 is not adopted. `round-61.md` stays byte-identical history; no row is rewritten here.

## 5. Bounded byte check (frozen scratch copy, stdlib, bytecode not executed)

`python3 -B` over `corpus/fixtures/evm-r24/fixture.raw`:

```text
len 35 sha256 b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93
pattern_len 9 occurrence_starts [1] span [[1, 9]]
byte_at_9 0x57 byte_at_1 0x63 raw_0x63_positions [1]
```

Corroboration (recorded): `LOG.md:289` "occur only inside immediate offsets 1–9"; `round-24/LEDGER.md:3` "occupy offsets 1–9 within that immediate"; `reports/round-61/measure-after.log:89` `R24_SPAN [[1, 9]]`.

## 6. Preserved evidence and non-claims

- README untouched; C04/C09 still uncovered; the C09 entry keeps `admission-status: rejected`; K not recounted; no prior report, counterexample, or fixture changed.
- The frozen entry's missing in-entry span derivation and its Q06/Q11 "pass" rows (`entry:188,193`) remain open debt; this seat does not repair them and does not treat the corrected wording as Q11 coverage.
- "First doubted by `AuditR24Truth`" is recorded-only: `dead-seats.json:514-521` shows `report_in_lane: false`, `session_output_bytes: 0`, `last_error: "Request was aborted"`; `LOG.md:805` asserts the transcript doubt, but no transcript exists in the frozen archive (`find` → none). Unverified.
- Unknown: whether the 0597e53 "reader's semantics" rationale was a deliberate scope argument or post-hoc wording (the file records the conclusion only). `embedded_pattern_offsets` author intent remains prose-only (`LOG.md:289`).

## 7. Proposed artifact (scratch, not applied)

- `/fast/scratch/hyaku/revenger-r62/R62DebtM25Capture/R62-lesson-M25-attribution-addendum.md` — append-only section for the new `corpus/lessons/round-62.md`: entry verbatim vs seats, Q06 capture with Q06 text + PASS-IF + failed enforcement, census 3/2, explicit no-edit of round-61.md, and the non-claims above. L1 owns the lesson; nothing was written under `corpus/`.

Installs: none. Scratch: `/fast/scratch/hyaku/revenger-r62/R62DebtM25Capture/`.
