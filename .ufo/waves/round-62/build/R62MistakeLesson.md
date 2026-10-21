# R62MistakeLesson — round-62 `## Mistakes` row for the M26/Q11 class

RESULT: COMPLETE

Axis: coverage (C1). Draft the round-62 lesson `## Mistakes` row for the
round-61 M26 / Q11-incompleteness class, with a red-before missing-derivation
exemplar and the bounded command that shows it. **No corpus file edited, no
README row touched, C04/C09 stay `uncovered`, no admission claimed.** Frozen
base `a3498e25ad87bf756288812d0ea7c474b09433c7`, extracted read-only to
`/fast/scratch/hyaku/revenger-r62/R62MistakeLesson/` (cwd = that dir). Scratch:
`proposed-round-62-mistakes-row.md` (five-cell row, evidence paths, checker
algorithm), `evidence_transcript.txt` (run log), `q11_red_before.py` (command),
`q11_inventory_check.py` + specs, three controls, mutant.

## 1. Bounded command — no spans in old C04 `## Reproduce` while prose says carried

`python3 -B q11_red_before.py corpus/knowledge/commonjs-destructured-require-edges.md` on frozen bytes (sha256 `690db9f1…2a6f3`, identical to the git object):

```text
entry=corpus/knowledge/commonjs-destructured-require-edges.md
reproduce_block_lines=53 printed_extent_derivations_in_block=0 (ast print-call scope)
prose_extent_claims_attributed_to_entry=1
  prose L80: - `corpus/verify_js_graph_delta.py` and `verify_saved_evidence.py` guard the names and the entry mapping but not the v2 digests, edge spans or the unnamed edge
VERDICT=RED  prose attributes extent values to the entry's own block; the block derives none
EXIT=1
```

Closure-form count over the extracted Python block only, same bytes:
`block_lines=53 count(location|start|span|column)=0`. The prose at entry lines
80–83 (unmodified) says the opposite: "…not the v2 digests, **edge spans** or
the unnamed edge …; **this entry's block carries those values**". C09 matches:
block 110–143 has 0 pattern-search hits, output 151–165 prints no
`0x5b`/`0x10` (prose 65, 94–95 assert the target and `[1, 9]`).

## 2. How the same inventory succeeds on a complete candidate — mechanism only

Three conditions must coincide: prose attributes the value to the entry's own
block; the `## Reproduce` block derives it; the `## Provenance` block prints
it. Round-61's C04 satisfied only the first. The check discriminates: RED (0
printed derivations) on both frozen rejected candidates, GREEN (4) on the
admitted `pe-resource-directory-layout.md`, GREEN (1) on a synthetic complete
control, RED (0) on a synthetic red-before mutant and on a comment-only mutant
(AST scope: a comment is not a derivation).

**Not claimed.** At `a3498e25…b09433c7` the corpus holds neither round-62
candidate file (`ls corpus/knowledge/ | grep round-62` → exit 1). The round-62
candidates are **not yet shown green**; the green outcome rests on the admitted
C01 entry and synthetic controls only, and whether they reach GREEN must be
established by running the same command on the landed files. Until then they
are drafts; C04/C09 stay `uncovered`, no admission claimed.

## 3. Proposed lesson row (append-only; L1 lands it)

`corpus/lessons/round-1.md` holds M01–M20 and `corpus/lessons/round-61.md`
holds M21–M26 (M26 at `round-61.md:128`), so the round-62 lesson continues at
**M27** (census: `awk -F'|' '/^\| M[0-9]+ /'`). Proposed id `M27`; class:
successful recheck output mistaken for complete derivation coverage (the
round-61 M26 class, re-confirmed on the frozen bytes); captured-by: Q11
(existing, unchanged; admission failed to enforce it). Row text: scratch.

## 4. Boundaries, installs, unknowns

- `corpus/` untouched (`git diff --stat -- corpus/` empty): no QUALITY edit, no
  SOURCES row, no README row, no map-status change, no new gate, no promotion,
  no admission. Prior rejected candidates and the round-61 lesson stay
  byte-identical (sha256 above matches the git objects). Routed debt #1
  (`round-61-verifier-spotcheck.md:208-210`) is answered by §1–§2: the missing
  spans/counts/targets are still to be derived or labelled recorded, and this
  seat's byte checks are **not** in-entry derivations. Debt #2–#4 stay with
  their owners (Q12: `RevengerR61-2.R62DebtQ12Flip`).
- Advisory stdlib check, not a gate or corpus verifier; no new capability; its
  vocabulary catches the C04/C09 shape, not every unlinked assertion; the
  non-author Q11 audit remains the necessary admission condition. No fixture
  byte, saved record, ledger or prior lesson text modified; no fixture JS,
  bytecode, producer, RPC or live-target run; no jj/Git history mutation.
  **Installs: none** (Python 3 stdlib only).
- Unknowns: whether the round-62 candidates land green is unobserved; the
  check is lexical and coarse, pointing at sentences to read rather than
  certifying; the `print(...)` scope assumes printed values, so a file-written
  value reads RED (a limit, not a pass).
