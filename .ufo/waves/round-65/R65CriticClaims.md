NOT-FALSIFIED — all four attacks resolved against committed bytes: freeze order is real, the do-nothing control re-derives byte-identically and meets no target, the C1 after-state is one-command re-derivable; two residual weaknesses recorded (probe exit code carries no claim signal; C1 has no counter-side anti-spoof twin of C5_CONTROL_PRESENT) plus one false-provenance hazard (a committed "final" after-log that predates admission).

# Attack 1 — Is the C5 kill rule frozen before any after-measurement? → YES, freeze order verified

Commit timeline (`git log --format='%h %cI %s'` in /home/vgpnk/Projects/shokunin/revenger-shokunin):

- `5a2e7a0` 2026-10-24T01:56:40-03:00 — "round-65: pre-registration" adds exactly `reports/round-65/claims.md`, `measure-before.log`, `measure.py` (3 files, +540). The kill rule (claims.md L43–49: delete `receipt['evidence_id']==evidence_id` conjunct; attributed iff mutant exit≠0 and last line ends `forged receipt evidence accepted`), the C5_CLAUSE regex and C5_MARKER (measure.py:261–263), and the do-nothing receipt all land in this one commit — nothing about C5 existed earlier to tune against.
- `c7b7cf9` 2026-10-24T02:46:11 — candidates land (C5 controls +3 lines/script, fixture, entry). AFTER the freeze.
- `5b4d29e` 2026-10-24T02:47:54 — `measure-after.log` committed. AFTER the freeze and after the controls.
- `git diff 5a2e7a0 HEAD -- reports/round-65/measure.py reports/round-65/claims.md` → empty. Frozen bytes never moved after the first after-run.

Causal order rule-frozen → control-landed → measured holds. claims.md L76–77 ("a rule changed after any seat has scored is not the claim's rule") is honored: no post-5a2e7a0 edit exists at all.

Sub-finding (procedural, not a rule violation): `5b4d29e` names its artifact "final measurement receipt" but was measured at `6f1761a` **before** the fresh-seat Q01–Q13 decisions and before the C05 flip — it prints `K_HELD=8/14`, `K_ROW C05 status=frontier` (git show 5b4d29e:reports/round-65/measure-after.log, lines 1–2). It is a valid C2 receipt (`C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2`) but it cannot be C1's after-state receipt. If the round closes citing 5b4d29e as "the" after-log, that is false provenance for C1; admission-order step 4 (claims.md L122–123) requires re-measurement at the true final tip.

# Attack 2 — Is the do-nothing control genuinely red? → YES, re-derived byte-identically

Executed the frozen command myself:

```
cd /home/vgpnk/Projects/shokunin/revenger-shokunin
git archive 3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f corpus | tar -x -C /tmp/r65-before.XXXX
TMPDIR=/tmp python3 -B reports/round-65/measure.py <tree>   → exit=0
diff reports/round-65/measure-before.log <my output> → IDENTICAL_TO_BEFORE_LOG
```

Red on every claimed line: `K_HELD=8/14` (C1 falsifier per claims.md L25), `K_ROW C05 status=frontier`, `C5_CONTROL_PRESENT=0/2`, `C5_RECEIPT_KILLED=0/2`, `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=0/2`, `HOLDS_OK_V3=no`. The before-log is not fabricated — the committed probe over the committed base archive reproduces it exactly.

# Attack 3 — Could a do-nothing control meet either target? → NO for both, but probe exit 0 is meaningless

- C2: base scripts contain no `forged receipt evidence accepted` string (`C5_CONTROL_PRESENT=0/2`, anti-spoof guard greps landed bytes — measure.py:280–282); the c5 mutant exits 0 at base (before-log MUTANT lines 38/41), so killed=0 → attributed=0. Unreachable without landing the control.
- C1: base prints `K_HELD=8/14`; target requires 9/14 and 8/14 is the declared falsifier. Unreachable without a README flip.
- **Finding (counter defect, frozen this round):** `sys.exit(2 if not evaluable else 0 if holds_ok else 1)` (measure.py:332) exits on `holds_ok` — the V1 formula, which contains neither `K_HELD` nor `c5_attributed`. The do-nothing base tree exits 0 (verified above). "probe exit 0" in the claimed after-state therefore carries zero information about either claim; an evaluator reading only the exit code cannot distinguish base from after. Only the explicit line values carry signal. Judge-facing note, not fixable under the frozen counter.

# Attack 4 — Is the C1 after-state one-command re-derivable? → YES in substance, with two structural notes

Demonstrated on the base side (byte-identical reproduction, above). The after-side differs only by `<commit>`: archive final tip → run probe. Notes:

- The derivation command runs `reports/round-65/measure.py` from the **checkout**, not from the archive — `reports/` is outside `git archive <commit> corpus`. Re-derivation trusts that the checked-out probe equals the frozen one; today it does (empty diff vs 5a2e7a0). Frozen-ness is enforced by git history, not by the command itself.
- `K_HELD` counts `| held |` text (measure.py:30–32); `K_HELD_BACKED`/`_STRICT` only check that named `knowledge/*.md` paths exist and lack an `admission-status: rejected` marker (measure.py:36–37,43–53). The candidate entry carries `admission-status: candidate` (corpus/knowledge/round-65-apk-axml-byte-evidence.md:7), so **a bare README flip naming the unadmitted candidate would print the entire C1 after-state** (9/14, backed, strict, C05 held) with zero admission. C2 got a counter-side anti-spoof guard (`C5_CONTROL_PRESENT`); C1 has none — its anti-spoof is purely the frozen admission order (fresh-seat Q01–Q13 → L1 flip, claims.md L110–123). Consistent with the contract's design, but the counter cannot distinguish admitted from premature flips; any reviewer validating C1 must check the Gate record, not the numbers alone.

# Verified mechanics of the landed C2 controls (context for attack 1–3)

- `verify_icon_languages.py:155–157`: `forged_evidence['evidence_id']='ev_6e055332b6fc…'` (the multi script's round-42 ID) placed immediately after the forged-stdout control, deep-copied, `require(not receipt_ok(...), 'r{r}: forged receipt evidence accepted')`.
- `verify_multi_icon_states.py:154–156`: transplants `ev_8ed889836291…` (the languages script's round-47 ID), same shape.
- Both IDs are real: `ev_6e05…` present in `corpus/live/runs/round-42/producer-receipt.json`; `ev_8ed8…` in `corpus/live/runs/round-47/producer-receipt.json` (grep -rl hits confirmed). Cross-foreign per claims.md L37–39. `receipt_ok` untouched — c7b7cf9 diff is +3 lines/script.
- Exactly one `receipt['evidence_id']` match per script (languages:120, multi:123) → `mutate_c5` cannot hit the `hits != 1` non-evaluable path (measure.py:266–274).
- After-log (5b4d29e) shows attributed kills on both mutants: `AssertionError: r47/r42: forged receipt evidence accepted` — `last.endswith(C5_MARKER)` satisfied.

# Impact summary

- Fixable defect: none found inside the frozen rule/predicate themselves.
- Tradeoffs for the canonical judge: (a) probe exit code is a holds-gate only — do not credit it as claim evidence; (b) C1's after-state lines are spoofable by a bare flip — validate against the Gate/admission record, and treat the committed `measure-after.log` as a C2-only receipt unless re-measured at the true final tip with C05 held.
- Smallest safe correction (procedural, in-scope of existing order): before closing C1, re-run the frozen command at the post-flip tip and commit that log; do not reuse 5b4d29e as the C1 after-receipt.

Report: .ufo/waves/round-65/R65CriticClaims.md
