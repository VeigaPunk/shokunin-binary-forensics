# Round-71 counter amendment A2 — archive binding and vote JSON rejection

Date: 2026-10-27, before any wave-2 seat scored. This is a counter implementation hardening, not a change to the registered C1 target, vote assignment, PASS/n/a condition, or kill rule. Claims SHA remains `1febae1279fdeca323f5e8beffeb0a8ac2f26256158f7000bb0b2eff8321c3f5`.

Counter SHA after A2: `718daa96f34fa5c3435acdf031e2fe5099238e9092c36b845cb9258990fcca61` (`sha256sum reports/round-71/measure.py`). Deltas from A1 counter `fbd81050930657375f7314123ef468e66337b69adee12ce8416bb5dc98cff8f5`:

1. `q_votes` reads `.ufo/waves/round-71/w2-votes/` under the measured `TREE`, not the live lane path. The final archive command must include the committed vote directory. This makes the 16/16 evidence re-derivable from the measured commit.
2. JSON parsing uses `object_pairs_hook` to reject duplicate keys, and a valid non-object root returns 0/16 instead of raising and truncating the counter receipt. Per-seat filename/stem equality, exact assigned-Q key sets, unique Q ownership, and only `PASS`/`n/a` remain required.

Committed probe receipt `.ufo/waves/round-71/vote-parser-control.txt` shows a valid four-seat PASS set → 16, duplicate Q key → 0, and non-object root → 0. The per-seat files remain structural receipts, not cryptographic identity proof; `HOLDS_C1_V6` is not an admission verdict. The full C1 condition still requires the four fresh wave-2 reviewer seats' committed vote files plus their reports and independent final-seat evidence. The base red-before remains 0/16 because no committed round-71 vote files exist in the base archive; the A2 red-before receipt is re-run before wave-2 scoring.
## Corrected red-before after A2

`reports/round-71/measure-before.log` was re-run against the base `git archive` tree with the A2 counter. Exit 0; C1 remains red (`K_HELD_BACKED=8/14`, `C1_W2_Q_VOTES=0/16`, `HOLDS_C1_V6=no`); C2 remains red (`C2_MISSING_ENTRY_EXIT2=0/1`, `C2_TIMEOUT_EXIT2=0/1`, both with traceback on base); `HOLD_REPLAY=10/10`, `HOLDS_OK_V8=yes`, all ten individual HOLD rows retained. The A2 JSON parser change does not move any baseline label.