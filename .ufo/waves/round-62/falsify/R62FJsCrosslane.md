GRADE: PARTIAL — corpus/knowledge/round-62-commonjs-require-name-evidence.md (C04 candidate; crosslane/ADJ-06 lens)

Frozen target: candidate state `d97761952be256d145d298022de03091de91d358`; claim base
`5bd4a90fc1a34caa94496601b60537b3aab12301`; pre-registration `a3498e25ad87bf756288812d0ea7c474b09433c7`.
Target blob sha256 `42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3`
(= worktree file). Lesson blob `corpus/lessons/round-62.md` sha256 `cf0339ebe9baa95124da3b7f4345f8c8abf8c5b35541d3b9ace1b22a0449d6ae`.
Scratch: /fast/scratch/hyaku/revenger-r62/R62FJsCrosslane (git archive of a3498e25 and d9776195; TMPDIR=…/tmp).

## Observation — the crosslane claim set HOLDS (primary evidence)

1. No sibling file, path or lane name is cited anywhere as support.
   `grep -nE 'kaidoku|kasegi|tsukuroi|chousa|PROVINCE\.md|l0-questions|adjacency-handoffs|/home/|shokunin/' <entry>` → rc=1, no hits.
   `grep -cE 'kaidoku|kasegi|tsukuroi' corpus/SOURCES.md` → 0. No guessed mutable line pointer exists to be wrong.
2. No ownership, priority or universality verb: `grep -nE '\bowns\b|prior art|holds the same|ground reported|exclusive owner|belongs to'` → no ownership hit (only "records' own `root_artifact_sha256`", "own-work bytes", "own round intake" = ordinary usage).
3. ADJ-06 preserved, no ruling declared: entry:68 quotes the lane's own routed disposition
   `corpus/lessons/round-62.md` — row 29 reads `| ADJ-06 sibling arbitration | Operator-owned and unresolved; new entries do not declare ownership or a ruling. |`
   (grep -n 'ADJ-06' corpus/lessons/round-62.md → 29). Entry:293 Q10 cell repeats "no ownership declared and no other lane's file cited as support".
4. No default-export claim, and no export-side claim at all: `grep -noE 'default[a-zA-Z]*'` → 0 hits; entry:54 item 19 "The export side of either module is **unknown and out of scope**".
   The round-61 rejected candidate's defect sentence ("a single exposed export named `default`", commonjs-destructured-require-edges.md:44) is NOT restated.
5. Not a duplicate of sibling ground (kaidoku read-only, HEAD `1e1bbef45ea0b92e443cdca04b814e74dfecbca1`):
   `grep -ri -- 'imported_name' kaidoku-shokunin/corpus/knowledge/ | wc -l` → 0; same for `destructur`, `source-range`, `local_name` → 0 each.
   kaidoku's nearest ground is a different representation (unresolved `require:` keys, `2026-10-13-r3-typora-signal.md:33`) and its held row is `Electron/ASAR/JS`
   (`kaidoku-shokunin/corpus/README.md:23`, status `held`) plus entrypoint NOT-FOUND (`2026-10-13-r3-renderer-asar.md:79-81`) — all outside this entry's scope and none cited as support.
6. Reproduce re-run by me on the frozen extract (independent of the entry's own claim):
   extracted readout.py from entry:85-213 → sha256 `31dac2113f1b78967a635fbf65125ecedc7a7ab4924debad8ba3c4be77ee02ac` (entry:80 claim — MATCH);
   `python3 -B readout.py tree_prereg` → exit 0, 25 stdout lines, stdout sha256 `58b63dd9d7c7ae4a0311ff33f12317345f7e5b7c9e8f204cfb13d1d599f0c416` (entry:80 claim — MATCH);
   same digest from the d9776195 tree; the entry's embedded stdout block (entry:219-243) is byte-identical to my run's stdout (EQUAL: True, 25/25 lines).

## Observation — nonfatal defects found (do not touch the crosslane substance)

D1 (entry:80, in-entry contradiction): "The stdout carries no path, so the same bytes give the same 25 lines from any extraction directory."
   The entry's own stdout block contains path fields: `"dir":"corpus/fixtures/js-r3"`, `"source_file":"corpus/fixtures/js-r3/index.js"`,
   `"files":[{"path":"index.js",…}]`, `"record":{"path":"corpus/live/runs/20261012T164357Z/analysis.json",…}`.
   The operative conclusion is TRUE and verified (same stdout digest from two different extraction roots); only the stated reason is false (the stdout carries RELATIVE paths, not none).
   Minimal correction: "carries no absolute path" / "paths are repo-relative". Q11-adjacent count/scope wording — nonfatal.
D2 (entry:248, unsourced count): the ECMA quote is labelled "— 8 words"; the lane's own source-open log records the same quote as
   "6 words (whitespace split)" (.ufo/waves/round-62/build/R62SourceEcma.md:36). No in-entry command derives a word count. Both values are ≤25, so the Gate quote budget holds; the number is nonetheless unsupported and disagrees with the recorded derivation. Nonfatal.
D3 (entry:68, pointer/revision): the ADJ-06 quote cites `corpus/lessons/round-62.md`, which does NOT exist at the frozen revision the entry pins for its own readout —
   `git cat-file -e a3498e25…:corpus/lessons/round-62.md` → "fatal: path 'corpus/lessons/round-62.md' exists on disk, but not in 'a3498e25…'"; the file first appears at d9776195.
   The pointer is therefore resolvable only at the entry's landing revision, not inside the tree `recheck:` materialises. Also note the entry renders the lesson row as
   `"ADJ-06 sibling arbitration: operator-owned and unresolved; …"` ("| " → ": ", lowercased "Operator-owned"); semantically identical, not a verbatim line. Nonfatal wording.

## Inference

- The load-bearing crosslane posture is sound: the entry declares no ownership, no ruling, cites no sibling file, absorbs no same-family ground, and makes no
  export-side/`default`/Electron-role/package-`main` claim (entry:10 Scope explicitly excludes "package `main`, entrypoint resolution, any role label, any export binding").
  Round-62 lesson:29 ("Operator-owned and unresolved; new entries do not declare ownership or a ruling") is satisfied in substance.
- Coverage-axis caveat for L1 only (not an entry defect): the entry's coverage-map header names the README row surface "JavaScript/Electron packages"
  while the entry covers two authored CommonJS directories, names and call spans only. If C04 is flipped to held, the row needs a scope annotation in the knowledge cell
  as the C06 precedent does ("(archive-tool row only)", corpus/README.md:35). README:33 is still `uncovered` with the round-61 rejected candidate named — no premature flip.
- D1/D2/D3 are wording/derivation defects, not scope defects: none of them changes a claim's truth, and none is material to the ADJ-06 preservation or the no-absorption property.

## Unknown

- Whether L1 will amend D1–D3 before admission; I did not repair, admit or alter anything.
- Whether the sibling surface that ADJ-06 refers to (kaidoku's held Electron/ASAR/JS row) will be arbitrated; operator-owned and unresolved at this revision.
- I did not evaluate the C09 candidate (separate lane) and did not run any repository verifier, REA producer, fixture JS, or network fetch.

## VERDICT

Crosslane/ADJ-06 dimension: HOLDS (no sibling citation, no ownership/ruling, no absorption, no default-export claim, sibling ground verified non-duplicative at kaidoku 1e1bbef4).
Entry as a whole: PARTIAL — three nonfatal wording/derivation defects (D1 stdout-paths statement, D2 unsupported 8-word count, D3 lesson pointer absent from the frozen tree).
Q cited: Q11 (D2 unsourced count; D3 pointer resolution) and Q02 wording precision (D1) — none rises to BROKEN; no material finding requiring repair.
Installs/updates: none. No file outside .ufo/waves/round-62/falsify/ was written; no live corpus, README, SOURCES or git state touched.
