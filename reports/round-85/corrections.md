# round-85 corrections (r84 non-author closure carry-in; append-only, status-neutral)

## Correction 1 — D1: the r84 report prose's bare-class imprecision, stated exactly

The r84 fleet report's C2 bullet says v4 shows "ZERO instrument rows name
the bare-cited `v4-postlanding-recon.log`". The committed red receipt
contradicts that absolute: `reports/round-84/v4-invisible-red.log` line
637 records the token's PATH-form twin (`SWEEP absent
reports/round-83/v4-postlanding-recon.log`, cited by the r83 verifier
lesson's path-form citation). Zero holds ONLY of the bare-token class —
`reports/round-84/claims.md` states this exactly ("its PATH-form twin …
WAS recorded, as an absent row"). Substance unaffected; the red/green
contrast verifies.

The fleet report is orchestrator-owned and is not rewritten (no in-place
edit of any r84 surface, including the report). The correction is this
file plus a standing wording rule, effective for every r85-and-later
prose this lane writes:

- A bare-class claim is quoted as exactly that: "ZERO bare-token rows"
  or "the bare-token class recorded nothing", never a bare absolute
  about "instrument rows".
- When precision matters, cite `reports/round-84/claims.md` §C2 change 7
  wording instead of paraphrasing.

The r85 claims.md, lesson, LOG entry, SCORECARD section and fleet report
follow this rule (their v4/v5 contrast sentences name the bare-token
class explicitly).

Carry-in provenance: routed defect D1 of the r84 non-author closure
(`corpus/lessons/round-84-verifier-spotcheck.md` §6, routed for next
round); addressed FIRST this round, before any claim work. D2 is
addressed by `.ufo/waves/round-85/postadjudication-sweep.log` (the
committed receipt); D3 stays operator-side routing (dual census receipts
landed, nothing assumed answered).

## Correction 2 — r85 closure routed item 1: the mg_probe.py docstring prediction line vs the registered 0/3 red

The r85 non-author spot-check routed (status-neutral,
`corpus/lessons/round-85-verifier-spotcheck.md` §7 item 1): mg_probe.py's pre-run
denominator paragraph says "on the round base only inspect_managed_artifact is
recorded, so M prints 1/3 (3.33)", while the frozen red (`mg-red.log`) prints 0/3
under the registered oracle-receipt definition — the r76 artifact record predates
the oracle-receipt gate, its receipt carries no `oracle` field, so it does not
count. The 0/3-not-1/3 shape was disclosed at the freeze, in claims.md, in the
LEDGER and in the report; substance was never affected.

Ruling recorded (the spot-check's own condition): a one-line docstring correction
in a NEW committed version of mg_probe.py is owed "next round the lane touches
this file". Round 86 does NOT touch mg_probe.py — the file is executed (the
frozen M hold re-run) but no byte changes, so the verified sha pin
`1840c30cf4f1cad0815c89ca80492053d4a43c5d752609a2edf33fa21a3ac03f`
(round-85 spot-check §2) stays valid and the conditional fix is not triggered.
The correction is this entry plus the standing wording rule:

- An instrument docstring's pre-run prediction line states the registration
  RULE, not an expected count; where a predicted count and the registered red
  differ, the registered red receipt governs and every prose citation names the
  red receipt's number (0/3 here).
- When the lane next touches mg_probe.py, the prediction line is corrected in
  the same commit (rule stated in the docstring: "on the round base only
  inspect_managed_artifact carries any record; under the registered
  oracle-receipt gate (receipt.json oracle.result starting ORACLE OK) it does
  not count, so M prints 0/3 (0.00)").

Carry-in provenance: routed item 1 of the r85 non-author closure; addressed
FIRST this round, before any claim work, status-neutral. Items 2 (census
literal-form exit 2, operator-side lineage — dual round-start receipts landed
again in `.ufo/waves/round-86/`) and 4 (SHONEN non-author re-confirmation of
the CURRENT SKILL.md bytes — operator-side, unchanged) stay routed; item 3
(per-revision-corpus basis movement) is honored: every r86 receipt cites its
`SWEEP_CORPUS` basis line first.
