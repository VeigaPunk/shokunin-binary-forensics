GRADE: PARTIAL — K_HELD_BACKED / Amendment A1 detector coverage
Axes: coverage (all four assigned mutations), calibration (pristine/mutated/restored controls and exact-byte restoration).
Scope: round 61 only; this is a counter-coverage finding, not a judgment of either entry's admission or of actual landed status drift.
Revision: ab580698212258a55e43e9bb9bf6ac78c91eae2a; Python 3.14.8, pre-existing.
Four independent full archives: D=/tmp/revenger-r61w3-W3KProbeMutant-{a,b,c,d}.
For each D, extraction executed from /: mkdir -p "$D" && git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive --format=tar ab580698212258a55e43e9bb9bf6ac78c91eae2a | tar -x -C "$D".
Detector for every phase: TMPDIR="$D" python3 -B "$D/reports/round-61/measure.py" "$D", subprocess cwd=/, timeout=300 seconds.
TMPDIR confines the probe's internal temporary mutants to the assigned scratch; no fixture JavaScript/bytecode or REA producer was executed.
Contract: reports/round-61/claims.md:90-93 requires backing files, fixed non-C04/C09 statuses, and 14 rows.

All four pristine controls: exit=0; exact lines `K_HELD=6/14 score=4.3`, `K_HELD_BACKED=6/14`.
Every one of the 12 invocations printed `K_ROW C04 status=held`, `K_ROW C09 status=held`, `HOLDS_OK=yes`; stderr was empty.
Every invocation also printed `C2_CONTROLS_PASS=2/2`, `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`.

| Mutant (one change per archive) | Expected detector | Actual relevant stdout; process exit | Verdict |
|---|---|---|---|
| a: corpus/README.md:29, C03 frontier -> held; knowledge cell remains `—` | No additional backed credit; raw/backed discrepancy exposes fake hold | `K_HELD=7/14 score=5.0`; `K_HELD_BACKED=6/14`; exit=0 | KILLED as a false-credit attack: zero backed credit. Raw count changes, not backed count; no exit 2. |
| b: delete corpus/knowledge/commonjs-destructured-require-edges.md; C04 remains held | Backed count falls or exit 2 | `K_HELD=6/14 score=4.3`; `K_HELD_BACKED=5/14`; exit=0 | KILLED by backed-count change. |
| c: insert README row 41, `| C15 | synthetic mutation row | — | — | frontier |` | Denominator change or exit 2 | `K_HELD=6/15 score=4.0`; `K_HELD_BACKED=6/15`; exit=0 | KILLED by printed-denominator change only; 14-row invariant is not an exit gate. |
| d: corpus/README.md:28, C02 partial -> frontier, all other bytes unchanged | Status drift visible through count change or exit 2 | `K_HELD=6/14 score=4.3`; `K_HELD_BACKED=6/14`; exit=0 | SURVIVED: complete stdout/stderr identical to pristine. |

Finding: d violates A1's fixed-status condition yet is invisible to this detector. measure.py:24-34 aggregates held/backed rows and prints only C04/C09 statuses; :111-113 gates exit on verifier holds/evaluability, not the other statuses.
Calibration: a's unchanged backed count is correct zero-credit behavior, not an erroneous admission; c is detectable by output comparison, not rejected by the process. No mutant exited 2.
This does not establish that the landed archive actually changed a forbidden status, nor that a knowledge entry fails Q01-Q11. It establishes an unguarded admission prerequisite; manual comparison remains necessary.

SHA-256 restoration evidence (command: sha256sum on each named target before mutation, while mutated, and after restoration):
R (README pristine/restored, a/c/d) = 9010c87374ac1b03b6a0165919825e0b14f1ab6b71999c24bee4658f448b1192
E (deleted entry pristine/restored, b) = 3382f1b3c56fbffb78f87735f353f5737b24e3ae102542cf98d3271946bc5629
| Archive/target | Before | Mutated | Restored |
|---|---|---|---|
| a/corpus/README.md | R | 06f8324ec8251d2683a2704b5359b9d6901b6db3eaa2cb9f3e3c316cc49a7eb4 | R |
| b/corpus/knowledge/commonjs-destructured-require-edges.md | E | ABSENT; sha256sum reported `No such file or directory (os error 2)`, exit=1 | E |
| c/corpus/README.md | R | 3cd7fe6474dc428a4acd251d0525ba32a133f1b811e55e3a0b21f4aa00b47309 | R |
| d/corpus/README.md | R | 24e104d19dbcbf04928a7427f4f4730f31b500b25c9cdf4b668df28a159ebab3 | R |
measure.py SHA-256, unchanged before/after in all four archives: ada7a9c97bba394f6539ce6f158ee81a8c342a42fa861d634933226bdd0b50d2.
Restoration: reversed the three README edits; recreated b's deleted entry from the untouched a archive. All target hashes match exactly; all four restored probe runs exited 0 with complete stdout/stderr identical to their pristine runs.
Evidence logs: /tmp/revenger-r61w3-W3KProbeMutant-{a,b,c,d}/probe-{pristine,mutated,restored}.log; complete commands/outputs/exits also in /tmp/revenger-r61w3-W3KProbeMutant-a/probe-results.json.
For d, all three complete log SHA-256 values are b7f50bbb42324f09e01ab629eb6861093abcce052952cbcd360504be7c0404b9 (each includes identical command, cwd, TMPDIR, stdout, stderr and exit).
Only scratch and this assigned report were written; no live lane source, Git index, jj state, saved record or fixture was changed.
VERDICT: Backing-file defenses hold; row-count drift is visible; non-C04/C09 non-held status drift survives without any output or exit distinction. Scoped A1 detector coverage is partial.
Installs/updates: none.
