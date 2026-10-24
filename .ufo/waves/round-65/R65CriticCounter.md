FAIL — the counter is label-spoofable on both claims: a one-line README edit prints the full C1 after-state with zero C1 work, and a self-source-grep trap prints `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2` while exercising zero forged receipts (`C5_CONTROL_PRESENT` binds the marker string only, not the control mechanism). Guards that did fire are named per attack below.

Seat: R65CriticCounter. Probe: `reports/round-65/measure.py` (frozen, `#9836`). All trees built as `git archive 8214e4d corpus | tar -x -C /tmp/r65critic/tmp/<t>/` — committed tree `8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0` (README C05 still `frontier`, C5 controls landed at `verify_icon_languages.py:155-157`, `verify_multi_icon_states.py:154-156`, entry `admission-status: candidate`). Measurements ran `cd / && TMPDIR=/tmp/r65critic/... python3 -B reports/round-65/measure.py <tree>`.

## Baseline T0 (unmodified HEAD archive)

`K_HELD=8/14`, `K_ROW C05 status=frontier`, `K_HELD_BACKED=8/14`, `K_HELD_BACKED_STRICT=8/14`, `C5_CONTROL_PRESENT=2/2`, `C5_CONTROLS_PASS=2/2`, `C5_RECEIPT_KILLED=2/2`, `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2`, `HOLDS_OK{,_V2,_V3}=yes`, exit 0. Landed controls are real (deep-copy + transplant of the two frozen foreign IDs at the lines cited above; mutants killed attributed in the T0 log).

## ATTACK 1 — README flip with no C1 work: FULL LABEL SPOOF (demonstrated twice)

**T1** — one-line README diff only: `| C05 | Android packages (APK) | — | — | frontier |` → `| C05 | Android packages (APK) | \`knowledge/seed.md\` | — | held |`. Result: `K_HELD=9/14 score=6.4`, `K_ROW C05 status=held`, `K_HELD_BACKED=9/14`, `K_HELD_BACKED_STRICT=9/14`, `HOLDS_OK_V3=yes`, exit 0 — the complete C1 after-state, byte-identical labels to a legitimate admission. The "knowledge" is `seed.md`, a pre-contract file with zero APK content, already serving rows C02/C10/C12 (path reuse across rows is unpenalized).

**T5** — flip + a two-line fabricated `knowledge/round-65-stub.md` (`admission-status: admitted — nothing reviewed`): identical labels, `K_HELD_BACKED_STRICT=9/14`.

Guards that did NOT fire and why: `held` counting is `re.search(r"\| held \|$", l)` on the status cell alone (measure.py:31); `K_HELD_BACKED` requires only `(TREE/"corpus"/p).is_file()` (measure.py:36-37); `K_HELD_BACKED_STRICT` adds only the absence of the substring `admission-status: rejected` anywhere in the file (measure.py:43-53) — a file bearing `admission-status: admitted` or no marker at all passes. `README_TOKEN_LEGEND_MISMATCH` scans only rows whose last cell is `frontier` (measure.py:80-83), so flipping C05→held *removes* it from the legend guard instead of triggering it. `K_ROW C05` reads the same flipped cell (measure.py:33-35). Nothing in the probe verifies admission provenance (Q01–Q13 fresh-seat decisions, L1 flip order), fixture existence, or entry content — all procedural/out-of-band. This is the same gap class as round-64: the probe counts bytes; admission is provenance.

## ATTACK 2 — C5 kill attribution without the landed control: FULL LABEL SPOOF (demonstrated)

claims.md:88-90 asserts `C5_CONTROL_PRESENT` "greps the landed script bytes for the control's attribution string, so a tree printing kills without landing the control cannot satisfy the after-state." Counterexample (**T2**): in each script I replaced the three landed control lines with a single self-inspection trap — `require("receipt['evidence_"+"id']==evidence_id" in open(__file__).read(), f'...: forged receipt evidence accepted')` (string concatenated so it does not collide with `C5_CLAUSE`; clause count stays 1 per script). No receipt is deep-copied, no foreign ID transplanted, `receipt_ok` never called on a forgery.

Measured T2: `C5_CONTROL_PRESENT=2/2`, `C5_CONTROLS_PASS=2/2`, mutant lines `MUTANT verify_icon_languages.py c5 exit=1 killed :: AssertionError: r47: forged receipt evidence accepted` (and r42 for multi), `C5_RECEIPT_KILLED=2/2`, `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2`, `HOLDS_OK_V3=yes`, exit 0. The mutant "kill" fires because the mutant's own source text changed, not because any forged receipt was rejected — the attribution message lies (no forgery was attempted or accepted). The trap also false-kills innocuous rewrites of the conjunct and false-passes a semantically-void `receipt_ok` that retains the literal conjunct text (e.g. `...==evidence_id or True`, where the regex still matches and the subn still deletes). So `C5_CONTROL_PRESENT` is a string-presence guard, not an anti-spoof guard for the control mechanism; the after-state can be satisfied without landing the claimed control. Whether label-satisfaction counts as claim satisfaction is judge-side; mechanism-wise this is a spoof.

Adjacent note for calibration: `--self-test` is decorative — neither script reads `argv`; `main()` runs unconditionally (`verify_icon_languages.py:177-178`, `verify_multi_icon_states.py:177-178`). The flag's semantics are never enforced.

## ATTACK 3 — clause-count fragility: denial, not spoof (demonstrated)

Appending one doc comment quoting the conjunct (`# doc note: the conjunct receipt['evidence_id']==evidence_id must stay in receipt_ok`) to both scripts (**T3**) gives regex count 2 → `mutate_c5` returns None → output `MUTANT ... c5 could-not-evaluate (clause match count != 1)`, `C5_RECEIPT_KILLED=0/2`, `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=0/2`, `HOLDS_OK_V3=no`, probe exit **2** (not-evaluable). The frozen fix shape is "insertions only" — a well-meaning comment documenting the landed control would silently break the round; likewise any reformat that introduces whitespace inside `receipt[` yields count 0 → exit 2. The same fragility exists in `mutate_b`/`mutate_c3`/`mutate_c4` (identical `len(hits)!=1` pattern, measure.py:131-138, 183-191, 224-232). Guard that fires: `evaluable=False` → exit 2 (visible, not a silent pass). Fixable defect, not a canonical-reject tradeoff: the kill rule could locate the conjunct inside `receipt_ok` rather than the whole file, or count only non-comment matches.

## ATTACK 4 — denominator/decoy-row inflation: partial spoof, caught (demonstrated)

**T4**: appended `| C15 | adversarial row (denominator inflation) | \`knowledge/seed.md\` | — | held |` → `K_HELD=9/15 score=6.0`, `K_ROW C05 status=frontier`. Guards that fire: `K_ROW C05` (measure.py:33-35) and the score column (6.0 ≠ 6.4); the "Rows 14" prose line is not counter-checked but is diff-visible. Corollary: because `K_ROW C05` must read `held`, no denominator game alone can fake the after-state — C05's own status cell must flip, i.e. Attack 1 is the only complete C1 spoof. Row deletion is a harsher DoS: removing one frontier row yields `8/13`.

## Other surfaces probed (analytic, counter-evidence in probe source)

- **Legend-mismatch asymmetry (wave footgun, currently clean):** any `corpus/live/runs/**.json` record with `"operation": "inspect_android_package"` lands `README_TOKEN_LEGEND_MISMATCH=1` while C05 remains `frontier` (`ROW_OPS` map, measure.py:63-83). `grep -rl inspect_android_package corpus/live/runs/` → no hits at 8214e4d, so the before/after logs stay clean — but a wave seat that records an APK readout under `live/runs/` with that operation string before L1's flip would fail `HOLDS_OK_V2`. After the flip the same record is silent (the check exempts non-frontier rows).
- **`HOLDS_OK_V3`/exit are C1-blind:** formula at measure.py:321-331 contains no K label. Exit 0 + `HOLDS_OK_V3=yes` is identical at 8/14-frontier and 9/14-held (both measured). Consistent with claims.md's "exit 0 required at round end" + L1-decided flip, but no seat should read exit 0 as C1 verification.
- **Symlinked knowledge paths:** `is_file()` follows symlinks and `copytree(symlinks=True)` preserves them (measure.py:36-37, 147) — a knowledge cell could point at a symlink to an out-of-tree file; byte-count spoof, same class as Attack 1, subsumed by the provenance gap.
- **Strict-scan over-fire (suppression, not spoof):** a legitimately admitted entry quoting the literal `admission-status: rejected` string (e.g. in a discussion of prior candidates) would be excluded from `K_HELD_BACKED_STRICT` while `K_HELD_BACKED` stays — a self-inconsistency pair. Current candidate contains only `admission-status: candidate` (line 7), safe.

## Summary

| Attack | Labels achieved | Counter guard that stopped it |
|---|---|---|
| T1/T5 README flip, no C1 work | full C1 after-state (9/14, C05=held, STRICT=9, V3, exit 0) | none — admission is unverified provenance |
| T2 source-grep trap | full C5 2/2 attributed + V3 + exit 0 | none — `C5_CONTROL_PRESENT` binds the string only |
| T3 doc comment quoting conjunct | — | `evaluable=False` → exit 2 (denial, not spoof) |
| T4 extra held row | 9/15 only | `K_ROW C05` label + score column |

Impacted axes: calibration (C5 anti-spoof claim at claims.md:88-90 is weaker than asserted — string presence ≠ mechanism; demonstrated) and coverage-K integrity (counter cannot detect flip-without-admission; the frozen admission order + git provenance remain the only real guard — a process property the canonical judge must enforce outside the probe). Smallest safe corrections for a future counter revision (not in-scope edits this round): (a) require `admission-status: admitted` (positive marker) in every knowledge path named by a `held` row, not merely the absence of `rejected`; (b) make `C5_CONTROL_PRESENT` grep the *shaped* control (a `forged_evidence['evidence_id']=` assignment adjacent to `require(not receipt_ok(forged_evidence` + marker) rather than the marker alone; (c) scope `mutate_*` conjunct search to `receipt_ok`'s body to remove the whole-file count landmine. None of these changes the landed work's verdicts — T0 green and the real controls remain compliant under all three tightenings.
