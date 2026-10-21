RESULT: COMPLETE

# R62JsEntry — C04 candidate, narrowed and corrected per the L1 integration decision (ready to land)

Scope: my seat only. Revised in scratch; no corpus write, no README flip, no admission claimed.
Candidate: `/fast/scratch/hyaku/revenger-r62/R62JsEntry/candidate.md` — 296 lines, sha256
`42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3`. Landing path: `corpus/knowledge/round-62-commonjs-require-name-evidence.md`
(candidate state; C04 stays `uncovered`).

## Final artifacts (scratch, lane-owned)

- `readout.py` — 129 code lines, sha256 `31dac2113f1b78967a635fbf65125ecedc7a7ab4924debad8ba3c4be77ee02ac`; one input (the
  extracted archive root), stdlib only, no live-corpus argument.
- `readout.stdout.txt` — 25 stdout lines, sha256 `58b63dd9d7c7ae4a0311ff33f12317345f7e5b7c9e8f204cfb13d1d599f0c416`. The stdout
  carries no path, so the same bytes give the same 25 lines from any extraction directory (verified against two paths).
- `tree/` — `git archive a3498e25ad87bf756288812d0ea7c474b09433c7` extraction (frozen base).

## L1 corrections applied

| Correction | How it is met |
|---|---|
| (1) stdout must be path-independent | `root_arg` removed from the header record; stdout sha256 identical from two different extraction roots |
| (2) no per-file digest-equality claim | inference 17 rewritten: each printed digest binds the bytes it was computed over; the provider's `root_artifact_sha256` is recorded, not re-derived, and no provider-vs-local digest equality is claimed. No code added |
| (3) drop the five grammar-flatten quotes | §Sources now quotes one text only — §14.3.3.3 "Set value to ? GetV(value, propertyName)." — and inference 16 uses it alone: the recorded agreement is of two literals, not an observed export binding and not an ECMAScript module import (S029's scope) |
| (4) scope the no-network claim | limitation 26: the readout touches no network/service/runtime/chain and reads local bytes and JSON only; the round's one network access is the read-only opening of the public ECMA-262 page for the S029 row |
| (5) reserved-row metadata is stale | header and §Sources cite S029 and S030 as existing `mined` rows (opened 2026-10-21), pending independent audit; Q01 row reworded to match |
| (6) cross-lane pointer | limitation 30 cites this lane's own intake `corpus/lessons/round-62.md` ("ADJ-06 sibling arbitration: operator-owned and unresolved; new entries do not declare ownership or a ruling"); no ownership claim, no sibling file cited |
| (7) keep source + call spans, no extra features | file lists and hashes, the require line and literal call text, both span bases, names, binding-assignment vs require-call spans, per-edge saved fields, recorded metadata, counts and the narrow name-value deltas all retained; the readout has no other feature |

Earlier narrowing (one stdlib readout, ≤130 code lines, ≤80 stdout lines of compact JSON, ≤450 entry lines, no verifier-source
introspection, no `maps_to`, no electron counts, no default-export surface, no semantic-unknown counters, no
`mutation_check.py`, no cross-lane script, package type only) holds: 129 code lines, 25 stdout lines, 296 entry lines.

## Command (frozen scratch copy only)

`git -C <repo> archive a3498e2… | tar -x -C tree` → exit 0; `python3 -B readout.py tree` → exit 0, 25 lines, stdout sha256
`58b63dd9…0c416`. No fixture JavaScript, bytecode, REA producer, runtime, service or chain touched; no verifier source read.

## Derived values (all in the 25 stdout lines)

- Files: js-r3 `index.js` 274 B `f7d8bf47…`, `package.json` 85 B `92ef8e3d…`, `transform.js` 379 B `cd9f3f63…`; js-r7-v2
  `index.js` 209 B `b53d96d4…`, `package.json` 85 B `92ef8e3d…`, `transform.js` 379 B `cd9f3f63…`. Package type `commonjs` both.
- Source line 1 of each `index.js`: `const { rot13, checksum } = require('./transform');` (names `rot13`,`checksum`) and
  `const { rot13 } = require('./transform');` (name `rot13`); specifier `"./transform"`.
- Spans (0-based end-exclusive / 1-based inclusive): require call `[28,50)` / `29-50` and `[18,40)` / `19-40`; binding assignment
  `[6,50)` / `7-50` and `[6,40)` / `7-40`; destructuring pattern `[6,25)` / `7-25` and `[6,15)` / `7-15`.
- Records: js-r3 193573 B `7c3ba8c1…` ev_4a93276c…; js-r7-v2 171150 B `331ec252…` ev_66f5dc7e…; both operation
  `analyze_javascript_application`, provider `rea-javascript-application` v1; root digests recorded, not re-derived.
- `imports` edges: 3 and 2; named targets `javascript-module`/`artifact-local-key`/`source-module`, unnamed targets
  `javascript-asset`/`content-digest`; every saved span's bytes read back as the expected text.
- Deltas: within fixture kept 2 / 1, removed 0, added 0; across records, over name values only, removed `["checksum"]`, added `[]`,
  kept `["rot13"]`.

## Unknowns (honest)

Runtime property presence (no execution); the export side (out of scope); the provider's root-digest construction (recorded, not
re-derived); every record field not named above; anything outside these two fixtures and two records.

## Decisions needed from L1

Land in candidate state (no held flip), then run the fresh falsify wave; `corpus/README.md` C04 stays `uncovered` until an
explicit all-criteria admission. S029/S030 rows already exist and are cited as existing rows pending independent audit, so no
`used-by` change is required of me.

Preservation: I wrote no corpus byte — the only repo file I wrote is this report. (Corpus changes visible in `git status` are
other seats' and the integrator's.) Installs: none (Python 3 standard library only; no pacman/uv/npm/cargo transaction).
