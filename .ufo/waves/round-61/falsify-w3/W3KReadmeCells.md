GRADE: PARTIAL — corpus/README.md rows C04/C09 knowledge cells and `held` status vs the README's own status definitions (landed ab58069)

Seat RevengerR61-2.W3KReadmeCells. Archive: `git archive ab580698212258a55e43e9bb9bf6ac78c91eae2a | tar -x -C /tmp/revenger-r61w3-W3KReadmeCells` (rev-parse printed ab580698212258a55e43e9bb9bf6ac78c91eae2a). Read-only; nothing executed except greps, `ls` and `git diff`/`show`.

## Definition under test (observation)
- README:19 `held` — "at least one admitted knowledge entry covers the ground"; README:20 `partial` — "covered only by unsourced or pre-contract text"; `uncovered` — "work evidence exists but no knowledge entry".
- So `partial` is about source quality, not breadth. A gated, sourced entry that covers only part of a row's surface cannot be `partial` or `uncovered` under this text. `held` is the only status the definition allows for C04 and C09. Two near-precedents point the same way. C06 (README:32) is `partial` with "(archive-tool row only)" because its entry is pre-contract, not because it is narrow. C13 (README:39) is `held` with a narrowing qualifier on its seed.md citation.
- Diff cf02419..ab58069 on README: only C04/C09 changed, from `uncovered` to `held`, plus index/footer text. The other 12 statuses are unchanged and there are still 14 rows. Probe: `measure-after.log:5` `K_HELD_BACKED=6/14`, and both cited slugs exist.

## C09 — "EVM bytecode interfaces" (README:36) — HOLDS
- The cell qualifier "(saved records on seven authored fixtures)" matches the entry. The entry covers seven records, r19 and r21–r26, at evm-saved-interface-candidates.md:20-45. Its scope statement is at :9-14: "not a statement about deployed contracts…". Its limitations are at :80-81.
- The README work evidence `evm-r19`, `evm-r21`…`evm-r26` (no r20) is the same set as the entry's `CASES` (:107-108). The cell has no scope gap.
- The entry stays inside the surface: opcode and selector definitions come from S016–S019, and it carries its own negatives. The surface label claims nothing the cell or entry contradicts.
- Nit (non-voiding): the entry header at :4 is a bare `coverage-map: C09`, while the C04 header at commonjs…:4 carries its scope limit. Q02 only requires naming the row, so it passes.

## C04 — "JavaScript/Electron packages" (README:30) — PARTIAL
1. Internal tension in one line (README:30). The cell says the entry covers "CommonJS destructured `require` only; no Electron/ASAR ground", yet the row is `held`, and README:19 says held means the entry "covers the ground". Read literally, the row's ground includes Electron packages and the cell disclaims that part. The entry agrees with the cell: commonjs…:13-14 says "Despite the coverage row's label, nothing here is Electron evidence."
   - This is not BROKEN. README:20 gives no other status that fits. The limit is disclosed in the same cell, in the entry header (:4), and in the lesson's principle (lessons/round-61.md:12-18): "the surface name is not evidence".
   - It is a definitional gap, though: under this scheme K counts rows by label, not by breadth. One fixture pair with three named edges flips a row whose label covers JavaScript and Electron packages.
2. The cell understates the entry (README:30). "`require` only" leaves out three things the entry observes:
   - the package-entrypoint `maps_to` edge (commonjs…:34-36)
   - the `electron-main` label (:37-38)
   - the `default`-only export (:38-40)
   The cell's exclusions ("no Electron/ASAR") are also shorter than the entry header's list (:4), which adds "ESM, bundler or `exports`". This is an understatement, not an overstatement, so it is not harm under claims.md:68-70.
3. The `held` status hides work evidence in the same row that has no knowledge entry. README:30 lists `shapes-r12`, `verify_semantic_trace.py` and `verify_shape_evidence.py` as C04 work evidence. `grep -rln "shapes-r12\|semantic_trace\|verify_shape" corpus/knowledge/` found no files (exit=1). `verify_semantic_trace.py:10-12` reads round-14 records and `js-r3/index.js`, none of which the entry covers. Before round 61 these items made C04 `uncovered`. Now the row shows `held` and no README text marks them as still lacking knowledge. That is consistent with README:19's "at least one", but the signal is lost.
4. Duplicate-authority check: not broken. Kaidoku also holds a row named "Electron/ASAR/JS" (kaidoku-shokunin/corpus/README.md, the row of that name). The revenger entry disclaims that ground (commonjs…:80-86) and leaves ADJ-06 with the operator. The README:30 cell itself does not name kaidoku; the entry does.

## Strongest counterexample tried
The premise: `held` for C04 overstates the evidence, which would void C1. It fails against README:19-20. Under those lines, the only alternative status, `partial`, requires unsourced or pre-contract text, and that is not the case here. The overstatement risk sits in the row label and the status scheme, not in the entry. The cell discloses the limit in the same line.

## Smallest safe corrections (no change to any count)
- README:30 cell: "(CommonJS destructured `require` and package `main` edge only; no Electron, ASAR, ESM, bundler or `exports` ground; `shapes-r12`/semantic-trace work evidence has no entry)".
- Optional: evm-saved-interface-candidates.md:4 → `coverage-map: C09 (saved records on seven authored fixtures)`, to mirror the C04 header.
- Definitional: add a breadth note to README:19-20, for example "held rows may cover a sub-ground named in the cell". K would then read as rows touched, not surfaces covered. Better as a future amendment than a change to this round's count.

## Impacted axes
- coverage K: the count is unaffected, 6/14 still stands under the README text. Interpretation: K tracks row labels, not breadth.
- No harm under claims.md:68-70: no saved record or fixture changed, no hold lost, the entry does not overstate, and source rows are outside this seat.

VERDICT: `held` is the only status README:19-20 allows for both rows. C09 is clean. C04 is PARTIAL because of an internal tension, an understatement and masked work evidence, all on README:30; none of these voids C1. Installs: none.
