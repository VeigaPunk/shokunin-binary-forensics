NOT-FALSIFIED — the frozen admission order is being followed: candidate state landed with the README C05 row still `frontier` naming nothing, the entry carries `admission-status: candidate`, no committed flip exists at HEAD `8214e4dd`, and no pre-baked admit/reject record usurps the wave's fresh-seat decisions. Two fixable provenance findings below; neither is a deviation that flips or preempts the row.

Seat: R65CriticAdmissionOrder — attack on the admission order itself (claims.md §Admission order, lines 110–123).

## Step-by-step conformance check

Frozen order (claims.md:112–123):
1. Wave lands candidates **without** the README flip.
2. Fresh in-wave attacks: named fresh-seat Q01–Q13 pass decisions from non-author reviewers.
3. L1 adjudicates; only all-criteria pass flips C05 `frontier → held`; falsification flips `frontier → uncovered`.
4. Measure on a committed archive at the final tip.

**Step 1 — CONFORMANT.** Verified at HEAD `8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0` and in the working tree (identical bytes):

- `corpus/README.md:34`: `| C05 | Android packages (APK) | — | — | frontier |` — status cell still `frontier`, entry and fixture columns still `—`; the row names nothing. `git show HEAD:corpus/README.md` prints the same line, so no uncommitted flip hides in the working tree.
- `git diff 3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f HEAD -- corpus/README.md` is empty (zero hunks, empty `--stat`) — README untouched since claim base, so "no other README row changes" holds at this stage.
- `grep -c '| held |' corpus/README.md` = 8 — consistent with `K_HELD=8/14`; no phantom held row.
- `corpus/knowledge/round-65-apk-axml-byte-evidence.md:7`: `admission-status: candidate` — not `admitted`; the header itself states the flip "is L1's and follows the fresh-seat decisions recorded in corpus/lessons/round-65.md ## Gate".
- `corpus/lessons/round-65.md:22` (## Gate — admission decisions): records "CANDIDATE LANDED, admission pending … README C05 intentionally NOT flipped" — honest pending record, not a pre-decision.
- Candidate build artifacts present and committed (`git ls-tree HEAD`): `corpus/fixtures/apk-r65/{fixture.apk,generator.py,readout.py,truth.json}`, the entry, SOURCES S038–S041, the two verifier C5 patches, lesson draft — all landed without the flip, exactly as step 1 prescribes.
- Working tree: `git status --porcelain` shows only `?? .ufo/waves/round-65/R65ExecCensusProbe.md` (wave report traffic); no corpus drift.

**Step 2 — IN FLIGHT, not preempted.** This wave is the fresh-attack instrument. No committed file pre-records a Q01–Q13 verdict on the entry (see Finding 2 for the nearest miss, which correctly disclaims).

**Step 3 — NOT YET DUE; no premature adjudication.** Commit history since claim base (`git log --oneline 3eebcdd7..HEAD`):

```
8214e4d round-65 verifier spot-check (integrator, hyaku): non-author admit/reject
5b4d29e round-65: final measurement receipt (C5 2/2 attributed, holds green, exit 0; measured revision 6f1761a9)
6f1761a round-65: LOG + SCORECARD (C2 verified C5 2/2 attributed; C1 candidate pending dispatch; M38/M37 mined)
c7b7cf9 round-65: candidates — … (no README flip)
5a2e7a0 round-65: pre-registration — claims.md, frozen counter, red-before receipt
```

`c7b7cf9` explicitly lands candidates with "no README flip" per its own message, and the README diff confirms it. Neither `6f1761a` nor `5b4d29e` touches `corpus/README.md` (file-level stat: LOG.md/SCORECARD.md and reports/round-65/measure-after.log only). `SCORECARD.md:446` records C1 as "candidate … admission pending" and `:452` plans the flip only on the dispatched wave's adjudication — the deferral is documented, not smuggled.

**Step 4 — committed interim receipt is honest but mislabeled (Finding 1).**

## Finding 1 (fixable defect — provenance label, not order violation)

`reports/round-65/measure-after.log` (committed `5b4d29e`, message: "final measurement receipt") was measured on revision `6f1761a9` — a **pre-adjudication** tip. Its content is honest: line 1 `K_HELD=8/14`, line 2 `K_ROW C05 status=frontier`, line 45 `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2`, line 60 `HOLDS_OK_V3=yes`. It does **not** print the C1 after-state (9/14) because the row is not flipped — correct behavior, and the file cannot be mistaken for a forged green.

Risk: the name `measure-after.log` plus "final measurement receipt" can shadow the step-4 obligation — after this wave adjudicates and the row flips either way, the frozen contract requires a fresh measurement on the **committed final tip**. Smallest safe correction: when the flip lands, write the post-flip measurement to the same path (superseding this interim receipt) on the same revision as the flip commit, and ensure the report/SCORECARD cites that revision, not `6f1761a9`, as the measured final tip. If C1 falsifies, this file's 8/14 already matches the falsified K and only a `frontier → uncovered` re-measure is owed.

## Finding 2 (fixable defect — second authority, correctly disclaimed)

`corpus/lessons/round-65-verifier-spotcheck.md` (committed `8214e4d`, author `protocol-shokunin <protocol@shokunin.local>` — a **different lane's** closure integrator, not a seat of this wave) records `admitted=false, verdict rejected-honest-stop, lanes.revenger=ok` (line 76). Read strictly, a "rejected" verdict landed before the fresh-seat Q-decisions the frozen order names as the gate.

Weighing against deviation: the file does not touch README; line 37 explicitly states "**C1 not verified this round** … admission pending orchestrator dispatch"; routed defect D4 (line 72) correctly assigns the flip + Q01–Q13 admission to this dispatched wave. The verdict is a closure-protocol disposition on the *round report* (report admission under "every claim verifies"), not a Q-gate decision on the entry and not a falsification trigger. It does not authorize `frontier → uncovered`.

Residual hazard: at adjudication time this file must not be cited as a falsification record — its "rejected-honest-stop" is about report admission, not claim falsification. Smallest safe correction: L1's adjudication commit should cite only this wave's named fresh-seat Q01–Q13 decisions as the gate authority; if those seats pass, the prior `rejected-honest-stop` is superseded process history, not a contradiction.

## Counterexample tested

Strongest available: "the order was already violated because a verdict and a 'final' measurement are committed before adjudication." Falsified as stated — the verdict belongs to a report-admission protocol and disclaims the Q-gate (Finding 2), and the measurement honestly prints the pre-flip 8/14 frontier state rather than the 9/14 after-state (Finding 1). No committed byte flips, names, or pre-judges the C05 row. The order's remaining obligation — fresh-seat decisions → either-way flip → final-tip re-measure — is live and unexhausted, so no defect here is of the class the canonical judge must reject.

## Evidence index

- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/claims.md:110-123` — frozen admission order.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/README.md:34` — C05 row `— | — | frontier` (HEAD and working tree identical).
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-65-apk-axml-byte-evidence.md:7` — `admission-status: candidate`.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-65.md:22` — admission pending record.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/measure-after.log:1-2,60` — 8/14, frontier, HOLDS_OK_V3=yes @ measured revision `6f1761a9`.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-65-verifier-spotcheck.md:37,72,76` — disclaim + D4 routing + `rejected-honest-stop` line.
- Commands: `git diff 3eebcdd7..HEAD -- corpus/README.md` (empty); `git log --oneline 3eebcdd7..HEAD`; `git status --porcelain`; `git ls-tree -r HEAD corpus/fixtures/apk-r65`; `grep -c '| held |' corpus/README.md` = 8.

No tool installs this seat.
