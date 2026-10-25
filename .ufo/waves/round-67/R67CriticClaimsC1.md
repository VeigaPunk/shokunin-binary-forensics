NOT-FALSIFIED — the C1 claim shape survives all four attack lines: the pass-branch label set is not reachable from the base receipt without the v2 entry, the universal clauses enumerate their sets, and the kill rule names an exact observable trigger. Three minor hardening gaps recorded below (spot-check asymmetry, unpinned C05 non-status columns, unnamed incomplete-wave outcome); none is a reachability counterexample.

Scope: reports/round-67/claims.md §C1 (lines 31-72), counter reports/round-67/measure.py (sha256 7933c060… per measure-before.log:90), base receipt measure-before.log, landed v2 entry corpus/knowledge/round-67-apk-axml-byte-evidence.md, README C05 row corpus/README.md:34.

## (1) Universal clauses — enumeration check

- "carrying exactly the routed repairs and nothing else" (claims.md:34-36): the repair set IS fully enumerated as items 1-6 (claims.md:38-51); "nothing else" is checkable as a diff-closure claim against the retained r65 candidate corpus/knowledge/round-65-apk-axml-byte-evidence.md. Enumerable.
- "every applicable Q01–Q13 decision" (claims.md:60): full set enumerated — 13 criteria named in corpus/QUALITY.md:13-25; the entry's §Q-map (entry:142-156) decides all 13 rows with per-row basis, so "applicable" + "n/a only with the entry's named reason" is pinned to the entry's own named n/a reasons (Q12 entry:155 "no rejected source row is written"; Q13 entry:156 "n/a by construction"; Q08 entry:151 "superseded by Q11"). A seat marking any other Q n/a fails the predicate clause — closed, not open-ended.
- Kill side "any Q FAIL" (claims.md:64) quantifies over the same 13-name set. Enumerable.
- Void "a README status change other than C05 (either-way)" (claims.md:128) quantifies over the fixed 14-row set; enumerable by diff.

## (2) Do-nothing reachability — README label spoof tested

Strongest counterexample attempted: a one-line README C05 edit from base, no v2 work.

- Flip `| C05 | … | uncovered |` → `| … | held |`: prints `K_ROW C05 status=held` but `K_HELD_BACKED` stays 8/14 — `backed` requires col-3 (`l.split("|")[3]`) to contain `knowledge/[\w.-]+\.md` paths whose files exist (measure.py:35-36); current col-3 is `—` (README.md:34).
- Also name an existing un-rejected file in col-3 (e.g. `knowledge/seed.md`): now `K_HELD_BACKED=9/14`, `K_HELD_BACKED_STRICT=9/14`, `K_ROW C05 status=held`, `README_TOKEN_LEGEND_MISMATCH=0` — but the frozen predicate clause "the C05 row's knowledge column names only the round-67 entry" (claims.md:59) fails: counter prints `C05_SINGLE_V2=no` (measure.py:63-67). Three of the four mechanical labels are spoofable; the sole-name clause is not, without the actual v2 file.
- Name the retained r65 candidate in col-3 instead (file exists): `K_HELD_BACKED=9/14` prints, but `K_HELD_BACKED_STRICT` drops to 8/14 — `rejected_marked` scans the whole file for `admission-status: rejected` (measure.py:46-51,54-58) and the r65 candidate carries it. Same for a rejected-marked v2 file.
- Conclusion: the full pass-branch label set is NOT reachable without the v2 file present, sole-named in col-3, and free of the rejected marker. The residual non-mechanical surface is human: fabricated seat decisions. Defense is present and binding in the frozen text — named fresh-seat Q01–Q13 decisions (claims.md:54-55, admission order §2 claims.md:118-119, ≥1 blind AXML re-derivation), outside-discernment spot-check not-REJECT (claims.md:60-61), "the flip lands in the same revision as the Gate decision" (claims.md:61-62), and "every named decision is re-verified by the L1 against committed bytes before the flip" (claims.md:62-63). Confirmed: the claims text does pin same-revision and named seats. A bare README edit cannot satisfy these clauses without producing forged wave artifacts, which is outside the counter's scope by design.

## (3) Predicate-narrowing risk after landing — two real gaps

- **G1 (minor): spot-check asymmetry.** Pass branch requires every Q decision to be "PASS" but the spot-check only "not REJECT" (claims.md:60-61). An inconclusive spot-check verdict ("unable to determine") satisfies the predicate literally. Smallest safe correction: require the spot-check to return an affirmative verdict (admit/pass), not merely not-REJECT. Wave has a dispatched `R67SpotcheckDiscern` seat; adjudication can hold the bar higher than the frozen text without editing the contract.
- **G2 (minor): C05 row's non-status columns unpinned.** The void condition freezes every README status except C05 and the counter reads only col-3 + status; nothing pins C05's name/evidence columns in the flip revision. A flip could drop the "retained rejected candidate `knowledge/round-65-apk-axml-byte-evidence.md` (… falsified Q02/Q06/Q11 …)" provenance note (README.md:34) from col-4, erasing the map-level pointer to the red-before surface without tripping any label. The r65 file itself stays byte-frozen (claims.md:133-134), so this is false-provenance-by-omission at map level only. Smallest safe correction: flip diff touches only col-3 (insert v2 pointer) and the status cell.
- **G3 (minor): stale-byte decision window.** Seats decide "on the landed bytes" (claims.md:54); a v2 edit between decisions and flip would silently retarget. Closed in practice by same-revision flip (claims.md:61-62) + L1 re-verify against committed bytes (claims.md:62-63); worth one audit pointer: the flip commit should carry the seat-decision commit range.
- No counter-side narrowing: measure.py is sha256-pinned (claims.md:112-113), the 14-row denominator and "only the C05 row may change" are void conditions (claims.md:122-123), and `K_HELD_BACKED=9/14` forces the strict count over all held rows, so narrowing by dropping another row's backing collapses the numerator.

## (4) Kill rule falsifiability — exact observation

C1 is FALSIFIED by either observable (claims.md:64-66): (a) any named seat's published Q01–Q13 FAIL on the committed v2 bytes, or (b) the outside-discernment spot-check returning REJECT. Both land as committed wave artifacts with an attributed Q-id/verdict; consequences are spelled out (C05 stays `uncovered`, v2 gets `admission-status: rejected` retained as evidence, honest stop). Falsifiable as written — the trigger is a discrete published verdict, not a judgment call.

Residual gap (not a falsifier): the kill rule names only FAIL/REJECT. A wave with zero FAILs that fails to complete all applicable decisions (dead seats — wave contract: "dead seats stay dead", claims.md:144) leaves C1 neither FALSIFIED nor pass; the counter state is identical (C05 uncovered) but the claim's label is undecided rather than falsified. The contract does not name this third outcome; smallest safe correction: adjudicate incomplete-wave as not-achieved (FALSIFIED-by-incompleteness optional) at the L1 report.

## Verdict basis

No pass-branch reachability from base without the v2 entry plus the wave's all-pass (the col-3 sole-name clause is the load-bearing counter check; the human clauses are bound in the frozen text). Kill rule has an exact observable trigger. Verdict: **NOT-FALSIFIED**; G1-G3 are adjudication-time hardening notes, not counterexamples.

No tools installed or updated this run.
