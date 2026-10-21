RESULT: COMPLETE

# R62 README admission plan — C04/C09 knowledge/work cells (proposal only, no admission)

Seat `RevengerR61-2.R62ReadmeAdmissionPlan` (leaf, no dispatch). Scope: propose the
`corpus/README.md` C04/C09 cells for the two new round-62 candidate paths; apply nothing.
Repo `/home/vgpnk/Projects/shokunin/revenger-shokunin`, frozen base
`a3498e25ad87bf756288812d0ea7c474b09433c7` (`git rev-parse` = same; `git status --short` shows
only the untracked `.ufo/waves/round-62/`). Scratch
`/fast/scratch/hyaku/revenger-r62/R62ReadmeAdmissionPlan/`.

## Behaviour
- Stage 0 (recommended now): **no README edit**; both rows stay byte-identical to base
  (`uncovered`). Naming a pending candidate buys no count and risks implying admission.
- Stage B (apply only after the fresh falsify wave **and** an all-criteria admit): replace the
  two base rows with the narrow-scope cells below and flip that row's status token to the
  existing `held`. Only rows whose entry actually passed are flipped (single-row variant allowed).
- Contingency on a reject decision: keep `uncovered`, add the rejected candidate to the
  work-evidence cell, mark both rounds' candidates rejected with their lesson pointers (exact
  rows: scratch `README-C04-C09-cell-proposal.md`, sections "Contingency"/"Stage 0").
- Retains old rejected references (`knowledge/commonjs-destructured-require-edges.md`,
  `knowledge/evm-saved-interface-candidates.md`) and the `lessons/round-61.md` pointer: Stage B
  moves that pointer from the knowledge cell into the work-evidence cell so nothing is dropped.
- Only existing status vocabulary (`held`/`partial`/`uncovered`/`frontier`); no new token, no row
  added, denominator 14 unchanged, no other row touched.

## Exact Stage-B replacements (apply only on admit)
```
| C04 | JavaScript/Electron packages | `knowledge/round-62-commonjs-require-name-evidence.md` (CommonJS destructured `require` names and call spans matched to saved import-name fields on `js-r3`/`js-r7-v2` only; manual, no Electron/ASAR/ESM/exports ground) | `fixtures/js-r3`, `js-r7-v2`, `shapes-r12`; `verify_js_graph_delta.py`, `verify_semantic_trace.py`, `verify_shape_evidence.py`; retained rejected candidate `knowledge/commonjs-destructured-require-edges.md` (rejected round 61, see `lessons/round-61.md`) | held |
```
```
| C09 | EVM bytecode interfaces | `knowledge/round-62-evm-dispatch-byte-evidence.md` (manual byte-boundary and dispatch observations on the authored EVM fixtures against saved candidate fields; no chain, provider-method or callable-interface-completeness claim) | `fixtures/evm-r19`, `evm-r21`…`evm-r26` (no `evm-r20`); `verify_evm_evidence.py`; retained rejected candidate `knowledge/evm-saved-interface-candidates.md` (rejected round 61, see `lessons/round-61.md`) | held |
```

## Evidence (frozen scratch only; cwd=/)
1. `git -C <repo> archive a3498e25ad87bf756288812d0ea7c474b09433c7 corpus | tar -x -C $S/base`
   → `cd / && python3 -B <repo>/reports/round-61/measure.py $S/base` → `K_HELD=4/14 score=2.9`,
   `K_ROW C04 status=uncovered`, `K_ROW C09 status=uncovered`, `K_HELD_BACKED=4/14`,
   `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`,
   `HOLDS_OK=yes`, exit 0 (log `probe-base.log`).
2. Stage-A sim (candidate paths in the knowledge cell, status kept `uncovered`):
   `K_HELD_BACKED=4/14` — naming a pending candidate changes no count.
3. Stage-B sim (both rows `held`, marker entry files present): `K_HELD=6/14 score=4.3`,
   `K_HELD_BACKED=6/14`.
4. Single-row sim (C04 `held`, C09 `uncovered`): `K_HELD=5/14 score=3.6`, `K_HELD_BACKED=5/14`
   — the C1 target count for one admitted row.
5. Ordering sim (C04 `held`, entry file absent): `K_HELD=6/14` but `K_HELD_BACKED=5/14` — a
   README flip without the file in the tree is not backed.
6. Row integrity: simulated README keeps 14 `| C` rows, each with 7 pipe-separated fields; diff
   vs base = 2 changed lines (`README-C04-C09-admit.patch`). Simulations 3–5 used one-line marker
   files in scratch copies only, never written into the repo.

## Findings
- F1. Ordering: the entry file must be committed in `corpus/` at the same revision as the README
  edit, else `K_HELD_BACKED` does not count the row (evidence 5). Land file → then row.
- F2. Probe blind spot kept separate from admission: `K_HELD_BACKED` counts held rows whose
  knowledge-cell files exist; it is not a quality verdict (claims.md; round-61 closure item 3).
  A row flip must follow an independent all-criteria admit, never the probe.
- F3. The parenthetical scope must be reconciled with the admitted entry's own `coverage-map:`
  header and `## Limitations`; if the entry's wording differs, the entry's wording wins verbatim.
  Neither candidate file exists at base, so the parentheticals are provisional.
- F4. The `knowledge/` index bullet claims rejected candidates carry an
  `admission-status: rejected` header; a pending or newly rejected round-62 candidate must carry
  such a header or the bullet is inaccurate (entry-owner / L1 item, not mine).
- F5. Prior rejected text is retained verbatim; nothing repairs the round-61 candidate bodies or lesson.

## Out of scope / unknowns
Not touched: `corpus/SCORECARD.md` K row and axis verdict; `corpus/lessons/round-62.md`;
`corpus/SOURCES.md` rows S028–S031; the candidate entry bodies; the gate decision and any
admission claim; `corpus/fixtures/**` and `corpus/live/**` bytes (only scratch copies edited).
Unknown: final titles/scopes of the two round-62 entries (files not yet landed) and whether one
or both pass the fresh wave — no admission is claimed by this report.

## Touched surfaces
This report `.ufo/waves/round-62/build/R62ReadmeAdmissionPlan.md`; scratch only
`/fast/scratch/hyaku/revenger-r62/R62ReadmeAdmissionPlan/` (`README-C04-C09-cell-proposal.md`,
`README-C04-C09-admit.patch`, `probe-base.log`, `base/`, `sim_uncovered/`, `sim_one_held/`,
`sim_held/`, `sim_held_nofile/`). No repository file modified, no jj/Git index or history
mutation, no fixture or live byte change.
Installs: none (stdlib Python only; no tool installed or updated).
