HOLD verified; M58 is repaired at the counter and captured in red-before, not a remaining defect.

## Evidence

- `reports/round-70/measure-after.log` is the received after-receipt. In `corpus/lessons/round-70-verifier-spotcheck.md:24-26`, the verifier records that after omitted individual `HOLD` lines while `HOLD_REPLAY=10/10` remained; its rerun printed all ten, exit 0 each. The routed defect is explicitly repeated at `:91-94`.
- Round-71 frozen `reports/round-71/pre-registration.txt:6,9` declares red-before `HOLD_REPLAY 10/10`, counter printing ten individual HOLD lines, and exit contract. `reports/round-71/measure-before.log:33-42` contains precisely ten `HOLD <verify_*.py> exit=0 ...` lines; `:43` says `HOLD_REPLAY=10/10`, `:47-48` records `HOLDS_OK_V8=yes`, `MEASURE_EXIT=0`. This confirms current print/captured behavior on the receipt.
- Source cause/repair locator: `reports/round-71/measure.py:144-148` explicitly retains all ten rows, loops sorted `verify_*.py`, runs `--self-test`, and prints each `HOLD` line before the replay total. Frozen counter hash is recorded at `pre-registration.txt:4`; this check is observational, not a new counter validation.

## M58 draft — receipt omission

- **Class:** operability / evidence-receipt omission (status-neutral; not a verifier failure).
- **Evidence:** Round-70 after receipt omitted the ten per-script HOLD rows, although it retained aggregate `HOLD_REPLAY=10/10`; verifier rerun reported all ten exited 0 (`corpus/lessons/round-70-verifier-spotcheck.md:24-26`, routed defect `:91-94`). Round-71 red-before receipt now prints all ten (`reports/round-71/measure-before.log:33-43`).
- **Captured by:** `reports/round-71/measure-before.log` (counter output captured before gate), with printer at `reports/round-71/measure.py:144-148`; a final after-receipt should preserve this complete output. Frozen red-before pointer: `reports/round-71/measure-before.log` (`pre-registration.txt:6`).
- **Fix:** Add/retain one output row per verifier in the captured measure receipt, not only `HOLD_REPLAY`; round-71 counter already implements this. No behavioral repair or re-gating is indicated by this check.

**Boundary:** Only read-only spotcheck/receipt evidence examined. No source or lane files edited. The missing `reports/round-71/controls/C2-missing-before.log` path was attempted but does not exist in the current listing; it is unrelated to M58. No seat-level round verdict.
