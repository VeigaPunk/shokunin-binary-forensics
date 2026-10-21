RESULT: COMPLETE

Scope: review only — README status conditions for C04/C09, an independent no-precredit checklist, and exact K-counter limits for the frozen C1. No repository edit; C04/C09 stay `uncovered` in `corpus/README.md`. Base a3498e25ad87bf756288812d0ea7c474b09433c7, extracted to scratch/tree via `git archive` (full revision recorded).

## 1. Conditions for a `held` C04/C09 (README-derived)

- `corpus/README.md:21-24`: `held` = "at least one admitted knowledge entry covers the ground"; `partial` = unsourced/pre-contract text only; `uncovered` = "a rejected candidate retained under `knowledge/` is clearly marked in the file and is not coverage".
- `corpus/README.md:11-13`: `knowledge/` holds admitted entries (the map names each) plus rejected candidates, each carrying `admission-status: rejected`.
- `corpus/QUALITY.md:29-32`: every criterion applied, none failing, decision recorded in the round lesson's `## Gate` (round-61 shape: `corpus/lessons/round-61.md:71-88`).
- H1 entry file `corpus/knowledge/round-62-*.md` exists with Q02 headers incl. `coverage-map: C04|C09` (`corpus/QUALITY.md:14`); H2 it carries no `admission-status: rejected`; H3 the round-62 lesson records an explicit admit with per-candidate Q01–Q13 verdicts; H4 the fresh falsify wave ran and every material finding was adjudicated; H5 the row's knowledge cell names that admitted path (`knowledge/[\w.-]+\.md`) while the rejected round-61 candidate stays in the work-evidence cell; H6 the status cell is exactly `held` and the row set is still 14 rows; H7 corpus/live, corpus/fixtures, prior rejected files, Q01–Q13 and the other twelve rows' statuses are byte-stable.

## 2. Exact K-counter limits (measured)

Probe `python3 -B reports/round-61/measure.py TREE` (cwd=/, TREE = extracted archive tree). Baseline `measure-base-a3498e2.log`: `K_HELD=4/14 score=2.9`, `K_ROW C04 status=uncovered`, `K_ROW C09 status=uncovered`, `K_HELD_BACKED=4/14`, `HOLDS_OK=yes`.
Denominator fixed at 14 (`corpus/README.md:45`); numerator = rows whose status cell is exactly `held` AND whose knowledge cell names ≥1 existing `knowledge/*.md` file. Reachable values only: **4/14 (2.9) = C1 falsified · 5/14 (3.6) = one admitted row · 6/14 (4.3) = both rows** (max; two rows on one axis are one claim). `partial`/`uncovered`/`frontier` score 0 on K.

| scratch variant (one probe run each; `probe-*.log` in my scratch) | C04 cell / status | K_HELD | K_HELD_BACKED |
|---|---|---|---|
| v1 bare text flip | unchanged / `held` | 5/14 (3.6) | **4/14** |
| v2 names a file that does not exist | new entry / `held` | 5/14 (3.6) | **4/14** |
| v3 names the retained REJECTED candidate | round-61 file / `held` | 5/14 (3.6) | **5/14** |
| v4 names an existing admitted entry | new entry / `held` | 5/14 (3.6) | **5/14** |
| v5 status cell `held (round-62)` | new entry / qualified | **4/14** (2.9) | 4/14 |
| v6 status cell `partial` | new entry / `partial` | **4/14** (2.9) | 4/14 |
| v7 one row added (denominator 15) | — | 4/15 (2.7) | 4/15 |

## 3. Findings

- **F1 high** — the probe's `score=` uses K_HELD while `SCORECARD.md:199` cites K_HELD_BACKED; v1/v2 print `score=3.6` with backed still 4/14 → cite K_HELD_BACKED and require K_HELD == K_HELD_BACKED in the final run.
- **F2 high** — backing is file-existence only: v3 names the rejected candidate and still reports 5/14 backed, against README's "not coverage". Known blind spot routed at `corpus/lessons/round-61-verifier-spotcheck.md` §Routed defects 3. The named path must carry a lesson admit decision and no `admission-status: rejected`.
- **F3 medium** — the status cell must be the bare word `held`; v5 proves `held (round-62)` scores 0 for the row.
- **F4 medium** — `partial` (v6) leaves K at 4/14 → C1 falsified; no partial credit on this axis.
- **F5 medium** — the denominator is part of the claim (v7 → 4/15, 2.7); `claims.md` voids admission on a changed denominator (14).
- **F6 low** — knowledge-cell paths must match `knowledge/[\w.-]+\.md`; a space or other character is silently unbacked (row does not count, no probe error).
- **F7 low** — ordering: the round-61 erratum retains "premature README admission" (`W3ClaimsAmendmentOrder.md`); a `held` cell before the falsify wave repeats that defect.

## 4. Independent no-precredit checklist (each item is a command L1 can run)

- P1 `grep -E '^\| C(04|09) ' corpus/README.md` shows status cell `uncovered` at candidate landing, before the falsify wave.
- P2 after admission: status cell exactly `held`; knowledge cell names the admitted `knowledge/round-62-*.md` file.
- P3 `grep -cE '^\| C[0-9]+ ' corpus/README.md` == 14.
- P4 status-column diff base vs final (`git show a3498e2:corpus/README.md`) touches C04/C09 only.
- P5 final probe prints `K_HELD=<n>/14` and `K_HELD_BACKED=<n>/14` with equal n in {5,6}; n=4 ⇒ falsified.
- P6 `git diff --name-only a3498e2 <final> -- corpus/live corpus/fixtures` empty.
- P7 sha256 unchanged: `knowledge/commonjs-destructured-require-edges.md` 690db9f1…2a6f3, `knowledge/evm-saved-interface-candidates.md` 3e17b88f…69361; both still `admission-status: rejected`.
- P8 `corpus/QUALITY.md` sha256 811ebf73…45d1 unchanged (Q01–Q13 not weakened; Q11 intact).
- P9 round-62 lesson `## Gate` gives per-candidate Q01–Q13 verdicts plus admit/reject, and S028–S031 carry located quotes and open dates only after being opened.
- P10 hold lines green: controls 2/2, attributed receipt-command kills 2/2, d2 2/2, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, `HOLDS_OK=yes`.
- P11 no text anywhere claims C04/C09 coverage before P1–P9 hold (README/LOG/SCORECARD).
- P12 knowledge cell names only `[\w.-]` paths; rejected candidates stay in the work-evidence cell.

## 5. Unknowns / residual risk

- The probe cannot distinguish an admitted entry from a rejected one (F2); only P9's lesson decision can, so the anti-precredit control is partly non-mechanical.
- Whether the two new entries satisfy Q11 is outside my scope (no prose/derivation review).
- S028–S031 are reserved, not yet written; I opened no source and wrote no source row.
- I modified no corpus file, README row/status, lesson or source row.

## 6. Proposed changes

None applied. Drafting vs post-admission row text and the probe-enforced invariants are in scratch: `/fast/scratch/hyaku/revenger-r62/R62ReviewReadmeScope/proposed-readme-rows.md`.

Installs / updates: none.
