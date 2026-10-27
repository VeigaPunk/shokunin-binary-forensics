VERDICT: C1 is correctly the lowest active criterion move; routed debts are only partly carried, with a key counter/control contradiction to surface.

## Evidence
- Frozen assignment: `reports/round-71/claims.md:7-9` calls C1 ground K the lowest criterion (5.7) and targets C05 sixth pass, 8/14→9/14; `SCORECARD.md:3-5` independently names coverage + calibration as active axes. C2 is a declared could-not-evaluate classification on an existing embedded-output gate (`claims.md:19-27`), not a general gate overhaul.
- The R70 spotcheck is `corpus/lessons/round-70-verifier-spotcheck.md`, not `reports/round-70/spotcheck.md` (that requested path does not exist). It records zero sampled disagreements and lists routed defects at lines 91-97. In particular, ten HOLD rows omitted from the after-receipt, Q16 omission, missing-entry exit 1, timeout exit 1/traceback, comparison asymmetry, env-override hybrid, PROVINCE version pin, SHONEN checks and open L0s.
- R70 lesson `corpus/lessons/round-70.md:139-147` explicitly routes C05 sixth pass (four prose repairs, Q16 map, literal names and SCORECARD companion), checker residuals, gate residuals, unmeasured self-assessment items, dex header-size oracle / ns_index limitation, L0s, and SHONEN verification.
- Current frozen receipt `reports/round-71/measure-before.log:1-15`: K=8/14; C1 no; missing-entry exit2 0/1 rc=1 with traceback; timeout exit2 0/1 rc=1 but stderr_traceback=no; gate self-test 0 named legs. Thus the R70 missing-entry residual is carried accurately, but the timeout's reported traceback is not reproduced in this receipt. This is a contradiction between R70 spotcheck (timeout traceback) and R71 measured baseline (none); do not collapse them into one status.
- `reports/round-71/pre-registration.txt:6-9` calls out counter exit contract and all ten HOLD lines; C1’s registered predicate requires both K mechanical labels and 16 assigned independent Q votes (`claims.md:11-13`), preventing control D's mechanical-only K 9/14 from counting (`claims.md:17`).

## Routed-debt ledger
| Debt | State | Evidence / note |
|---|---|---|
| C05 sixth pass / Q16-aware map and Q04/Q11b/Q13 repairs | Addressed as current target, not yet outcome | Frozen at `claims.md:7-17`; entry remains candidate-phase / no vote evidence yet in base receipt. |
| Counter's missing ten HOLD rows | Addressed in preregistration | `pre-registration.txt:9`; actual baseline prints all ten (`measure-before.log:33-42`). |
| C2 missing entry path exit-2 | Open target, observed unfixed | `measure-before.log:12`; preregistration explicitly registers this leg (`claims.md:23-25`). |
| C2 timeout classification | Open target, evidence conflict | Registered in `claims.md:23-27`; baseline rc=1 but no traceback (`measure-before.log:13`) conflicts with R70 spotcheck's traceback finding (`round-70-verifier-spotcheck.md:95`). Keep separate subclaims: exit mapping remains red; traceback is not confirmed by this receipt. |
| Gate one-directional compare / forged command residual | Deferred / explicitly outside C2 claim | R70 lesson lines 143, 154-155; C2 frozen scope limits it to classification and demands unchanged drift/pin/confinement behavior (`claims.md:21,25`). |
| Checker env-override hybrid / class refinements | Deferred | R70 lesson lines 142-144; not included in C1/C2 predicates. |
| SOURCES opening and census; assimilation/adoption | Deferred/planned separately | R71 claims lines 29-31 restrict source work and state no merge adoption; R70 quarantine/adoption gate remains closed. |
| L0 questions, PROVINCE tool-version pin, SHONEN external verification, fixture oracle limits | Open/deferred | R70 lesson lines 144-147; no basis in the frozen R71 predicates to count as addressed. |

## Axes and one bounded move
Axes: coverage (K), calibration (C2 registered exit-2 classification); adjacency is the seat judgment axis. C1 is indeed the lowest named active criterion (5.7), but no numeric calibration baseline appears in this lane scorecard excerpt as a comparable value; avoid claiming it is lower than calibration numerically.

Proposed move: in the final Gate/lesson, preserve a small provenance-linked routed-debt table with distinct states `addressed`, `open`, `deferred`, and represent the timeout contradiction as two fields (exit code and traceback observation), citing the R70 spotcheck and R71 receipt separately. This improves adjacency by making the carry-forward trace auditable and improves calibration evidence integrity without changing frozen predicates or bundling unrelated residuals into C2. Keep the existing claim boundaries intact.

Risks: accidental wording could make the deferred asymmetry, hybrid checker, or L0 items seem accepted as solved; timeout stderr behavior may vary by run. Use exact path:line and run-specific observations, not scalar closure claims. The report itself is pre-gate advice only.

Verification: compare the eventual Gate's routed rows against R70 lesson `:139-147`, R70 spotcheck `:91-97`, R71 preregistration `:6-9`, and R71 receipt `:12-15`; ensure the timeout row records rc=1 in this receipt while explicitly marking traceback as unobserved here. No code/test/build run performed; no source edits made. No installs.
