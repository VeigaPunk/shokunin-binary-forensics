RESULT: COMPLETE

# R62JsEntry — C04 candidate, corrected per the fresh falsify wave (candidate pending; ready to land)

Scope: my seat only. Fixed in scratch, no live corpus edit, no README flip, no admission claimed.
Candidate: `/fast/scratch/hyaku/revenger-r62/R62JsEntry/candidate.md` — 351 lines, sha256
`d4544c7012a52c0b877022009de6056d6beeda53cd78c2054361e732dce5cafe`. Landing path:
`corpus/knowledge/round-62-commonjs-require-name-evidence.md` (candidate state; C04 stays `uncovered`).

## Final artifacts (scratch, lane-owned)

- `readout.py` — 142 code lines, sha256 `78a51a73959c36248a63407eef4b90c212a9077e4f34c5fff6d75e0486176d14`; one input
  (the extracted archive root), stdlib only, no live-corpus argument, no network.
- `readout.stdout.txt` — 25 lines, sha256 `3c62d57c25bb10e3f0114dadb9525cda1e44c695e5a5cc50c2b674777c7a8bcf`; repo-relative
  paths only, never the extraction root; identical from two different extraction roots.
- `tree/` — `git archive a3498e25ad87bf756288812d0ea7c474b09433c7` extraction (frozen base).

## Falsify-wave corrections applied

| Required | How it is met |
|---|---|
| physical source line from unfiltered `splitlines()`, non-empty count separate | `physical_lines_total` 7, `non_empty_lines` 7, `physical_line_number_1based` 1, from `text.splitlines()`; the non-empty count is a separate field |
| span text read at the SAVED start/end lines, not the regex line | each edge record carries `saved_line_text` read at the record's own `start_line`, plus `saved_line_equals_physical_source_line`, `saved_start_line_equals_physical_source_line`, `text_at_saved_columns`, `text_at_saved_equals_manual_require_call_text`, `text_at_saved_equals_manual_binding_assignment_text` |
| physical-source / saved-line and column / text equality printed explicitly | the five flags above are printed per edge; item 11 states the reading the compared texts establish |
| mutating the saved line / prepending a blank line must show disagreement (stdout comparison, not a gate) | §Reproduce "Saved-line sensitivity": prepending one blank line moves the physical require line to 2 while the saved location still names line 1; the stdout then shows `physical_line_number_1based` 2 and the three js-r3 `saved_line_equals_physical_source_line` flags false (5 true → 3 false, 2 true). Exact commands and output are embedded; it is a stdout difference, not a gate, and nothing is credited to it |
| source ASCII status printed to bound char-vs-byte conventions | `source_ascii_only` true, `source_chars` = `source_bytes` (274/274, 209/209) |
| infer the 0-based convention by compared texts, not assertion | item 11: the reading is established by the text-equality flags; the 1-based inclusive form is the display form |
| in-entry `sha256sum`/`wc` with exact output for own script/stdout digest and line count | §Reproduce "This entry's own metadata": `sha256sum readout.py readout.stdout.txt` and `wc -l readout.py readout.stdout.txt` with the exact output |
| ECMA pin/date/anchor labelled RECORDED from S029 | the `source:` header says "**recorded from the S029 row, not derived by the readout**"; §Sources repeats it |
| quote word count false "8" → derived 6, or omit; drop the false spaced-parentheses rendering claim | the count is now derived in §Reproduce (`printf '%s\n' "Set value to ? GetV(value, propertyName)." \| wc -w` → `6`); the spaced-parentheses rendering sentence is deleted |
| full `SingleNameBinding : BindingIdentifier Initializer opt` case label | inference 16 and §Sources name that case explicitly |
| delete "one network access this round"; readout no network; source opens recorded separately | limitation 26: the readout uses no network; the ECMA-262 page opening is "recorded in the source ledger, not in this entry's readout"; no round count |
| "stdout carries no path" → relative paths / no extract root | the `recheck:` header says the stdout carries only repo-relative paths, never the extraction root |
| unknown export side → "not examined here"; required module object → value of the call | unknown item 19 is "not examined here"; unknown item 18 and inference 16 speak of the value of the `require(...)` call |
| cross-lane paraphrase, not verbatim quote | limitation 30 paraphrases the round-62 intake and cites `corpus/lessons/round-62.md`; no verbatim quote, no ownership claim |
| no Q13 guard credit; avoid overbroad "every value above derived" | §Q13 splits the values into the derived kind (command + printed output) and the recorded kind (S029's date/anchors/digest; each record's Evidence ID, operation, provider id/version, root digest) and claims no coverage by any check |
| inventory covers headers / source / run metadata too | inventory rows H1-H3 (header, verified-at, recheck), row S1 (the quote and its derived word count), plus the recorded run-metadata fields in rows 6-7 |
| no new features, producer calls or helper gate | the only code added is what the corrections above require; no producer call, no gate, no helper script |

The readout grew from 129 to 142 code lines (the delta is exactly the required physical-line, saved-line, equality-flag and
ASCII-status work); the entry is 351 lines and the stdout 25 lines.

## Command (frozen scratch copy only)

`git -C <repo> archive a3498e2… | tar -x -C tree` → exit 0; `python3 -B readout.py tree` → exit 0, 25 lines, stdout sha256
`3c62d57c…8bcf`. No fixture JavaScript, bytecode, REA producer, runtime, service or chain touched; no verifier source read.

## Derived values (all in the 25 stdout lines)

- Files: js-r3 `index.js` 274 B `f7d8bf47…`, `package.json` 85 B `92ef8e3d…`, `transform.js` 379 B `cd9f3f63…`; js-r7-v2
  `index.js` 209 B `b53d96d4…`, same other two. Package type `commonjs` both. Sources pure ASCII, 7 physical lines each.
- Physical line 1 of each `index.js`: `const { rot13, checksum } = require('./transform');` (names `rot13`,`checksum`) and
  `const { rot13 } = require('./transform');` (name `rot13`); specifier `"./transform"`.
- Spans (0-based end-exclusive / 1-based inclusive): require call `[28,50)` / `29-50` and `[18,40)` / `19-40`; binding assignment
  `[6,50)` / `7-50` and `[6,40)` / `7-40`; destructuring pattern `[6,25)` / `7-25` and `[6,15)` / `7-15`.
- Records (recorded fields): js-r3 193573 B `7c3ba8c1…` ev_4a93276c…; js-r7-v2 171150 B `331ec252…` ev_66f5dc7e…; both
  `analyze_javascript_application`, provider `rea-javascript-application` v1; root digests recorded, not re-derived.
- `imports` edges: 3 and 2; every saved span's text at the saved line equals the manual span text; named targets
  `javascript-module`/`artifact-local-key`/`source-module`, unnamed targets `javascript-asset`/`content-digest`.
- Deltas: within fixture kept 2 / 1, removed 0, added 0; across records, over name values only, removed `["checksum"]`, added `[]`,
  kept `["rot13"]`.

## Unknowns (honest)

Whether the value of the call carries the named properties (no execution); the export side (not examined here); the provider's
root-digest construction (recorded, not re-derived); every record field not named above; anything outside these two fixtures and
two records.

## For L1

Land in candidate state (no held flip), then the fresh falsify wave; C04 stays `uncovered` until an explicit all-criteria
admission. S029/S030 exist and are cited as existing rows pending independent audit.

Preservation: I wrote no corpus byte — the only repo file I wrote is this report. Installs: none (Python 3 standard library
only; no pacman/uv/npm/cargo transaction).
