HOLD — Frozen base leaves C1/C2 red; syntactically valid fake vote files remain a provenance counterexample.

## Evidence

- Read frozen contract `reports/round-71/claims.md:7-27` and receipt `reports/round-71/pre-registration.txt:1-9`. C1 requires 9/14 held/strict, exact C05 v6 path, admitted marker, gate/lint, and precisely 16 valid Q votes; C2 requires both real CLI failure modes exit 2 without traceback plus self-test. These are conjunctive.
- Reproduced frozen baseline from the base archive under `/fast/scratch/hyaku/revenger-r71/R71W1ClaimsCritic/base` with `HYAKU_SCRATCH=/fast/scratch/hyaku/revenger-r71/R71W1ClaimsCritic python3 /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-71/measure.py /fast/scratch/hyaku/revenger-r71/R71W1ClaimsCritic/base` (exit 0). Actual output: `K_HELD_BACKED=8/14`, `C1_W2_Q_VOTES=0/16`, `HOLDS_C1_V6=no`, missing-entry `rc=1 stderr_traceback=yes`, timeout `rc=1 stderr_traceback=no`, `HOLDS_C2_V1=no`. The no-trace timeout indicator alone does not satisfy exit-2 classification.
- Frozen control D output `reports/round-71/controls/D-C1-v5-copy-with-q16.log:1-11`: copied v5 material reaches K 9/14, clean 24-block gate and lint but `C1_W2_Q_VOTES=0/16` and `HOLDS_C1_V6=no`. This is the strongest skip-work counterexample: target metrics/gate can be met without the registered vote conjunct.
- `reports/round-71/measure.py:49-62` accepts JSON based on seat string, expected Q key set, and PASS/n-a values; unique Q ownership is checked, but no signature or independent reviewer provenance is checked. Thus a forged file with a valid seat identity and assigned decisions can satisfy the syntactic predicate if placed in the expected directory. Claims wording “committed per-seat JSON vote files” (`claims.md:11-13`) establishes location/shape, not authorship.
- `reports/round-71/build-controls.py:10-23,35-43` specifies README flip, stub, and v5-copy controls; it writes fixtures only in configured controls scratch. I did not mutate lane or invoke the builder. Frozen control outputs show no target reached HOLDS=yes.

## Counterexample and safe correction

The strongest observed local counterexample is D: every C1 structural metric except votes is green, while admitted v5 copy plus Q16 row still fails because votes are 0/16. This validates resistance to simple skip-work. More adversarially, `q_votes()` parses ordinary JSON and does not bind seat claims to authenticated artifacts, so fabricated PASS records could meet the predicate if expected seats/Qs are covered. Smallest safe correction: preserve this round's frozen predicate; before a future round, bind vote files to immutable reviewer-produced receipts or independently validate provenance. Do not narrow targets or rewrite this round's counter.

Impacted axes: C1 coverage target resists simple README/stub/v5-copy controls; calibration/integrity confidence is weaker for unauthenticated votes. C2 remains the registered exit-2 behavior; baseline is not an exit-text-only control (`claims.md:23-27`).

## Boundary

No lane-source edits, no seat judgment, no vote/admission decision. Frozen counter run only against archived base fixture. Scratch removed before return.
