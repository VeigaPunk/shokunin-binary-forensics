VERDICT: Contested boundary only — v6's explicit C05 scope fence does not absorb Kaidoku's APK content-graph or Android decode claims; keep ADJ-06 open and report, not resolve.

## Axes
Adjacency and coverage. The v6 candidate addresses frozen C1 coverage only on C05; this scan found no cross-lane boundary expansion to trade against that gain.

## Evidence
- `revenger-shokunin/corpus/knowledge/round-71-apk-axml-byte-evidence.md:11` scopes coverage to container members, binary-AXML manifest, and declared dex header of **one authored APK fixture**; it explicitly excludes provider readiness/output and general parser behavior beyond the fixture.
- `.../round-71-apk-axml-byte-evidence.md:285` expressly disclaims install validity, signature blocks, dex program validity, and any provider behavior.
- `.../round-71-apk-axml-byte-evidence.md:291-293` itself states ADJ-06 remains open and the Kaidoku APK content-graph inventory / Android decode axis are not restated or claimed.
- `kaidoku-shokunin/corpus/README.md:27` identifies its held APK content graph as 120 deduplicated content nodes and all 130 occurrences hash-verified; `:29` identifies its Android decode axis (manifest/class census and resource decode). These are distinct propositions from the candidate's byte walk and authored oracle comparison.
- `revenger-shokunin/PROVINCE.md:3-7` broadly includes Android APKs in Revenger's domain, while `kaidoku-shokunin/PROVINCE.md:3-6` broadly includes shipped artifacts and archives/packages. This is a real governance contradiction, not resolved by the narrower v6 evidence scope.
- Fleet `.ufo/l0-questions.md:42` records the kaidoku/revenger shipped-artifact overlap question; this remains an ownership arbitration, not a technical conclusion that either lane exclusively owns APKs.
- Frozen `reports/round-71/claims.md:9-13` makes the sole C1 surface change C05 and constrains its claim to the authored APK fixture. C1's scope is consistent with the v6 boundary above.

## Proposed move
No candidate repair indicated. Preserve the current narrow C05 fixture-level wording; retain the explicit non-absorption statement at v6 `:291-293`; route the broader Android/APK ownership contradiction to the integrator under still-open ADJ-06. Do not claim Kaidoku's graph inventory, decode behavior, or provider capability as Revenger evidence. This bounded move protects adjacency without shrinking or changing the frozen C05 coverage predicate.

## Risks / contradiction
The provinces' broad domain declarations overlap on shipped APKs (Revenger `PROVINCE.md:3-5`; Kaidoku `PROVINCE.md:3-6`) despite the candidate's distinct artifact-level proposition and explicit fence. This cannot be collapsed into a scalar score or settled by this leaf report. No source/fixture/parser assertion was independently re-run; findings are scoped document comparisons.

## Verification
Read-only review of the cited lane candidate, frozen claims, both province declarations, Kaidoku corpus index, and fleet L0 question. No source tree or campaign tool invoked; no lane-source changes.

Report: .ufo/waves/round-71/w1/R71W1ConnOverlap.md