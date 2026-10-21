GRADE: HOLDS — round-62-commonjs-require-name-evidence.md (C04) whole-line regex / readout coordinate attack

Frozen revision: d97761952be256d145d298022de03091de91d358 (full SHA, `git rev-parse` confirmed). Claimbase 5bd4a90fc1a34caa94496601b60537b3aab12301; pre-registration a3498e25ad87bf756288812d0ea7c474b09433c7.
Candidate under attack: corpus/knowledge/round-62-commonjs-require-name-evidence.md, SHA-256 42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3 (archived copy; byte-equal to worktree, `cmp` clean).
Method: git archive of d977619 extracted to /fast/scratch/hyaku/revenger-r62/R62FJsRegexBoundary/tree; all checks ran there, TMPDIR=/fast/scratch/hyaku/revenger-r62/R62FJsRegexBoundary/tmp. No fixture JS or EVM execution, no producer/REA calls.

## Primary evidence

E1 Reproduce chain (cwd=/fast/scratch/hyaku/revenger-r62/R62FJsRegexBoundary):
- readout.py extracted verbatim from the entry's §Reproduce fence → SHA-256 `31dac2113f1b78967a635fbf65125ecedc7a7ab4924debad8ba3c4be77ee02ac` — equals the entry's claimed script digest.
- `TMPDIR=$S/tmp python3 -B readout.py tree` → exit=0, 25 lines, stdout SHA-256 `58b63dd9d7c7ae4a0311ff33f12317345f7e5b7c9e8f204cfb13d1d599f0c416` — equals the entry's claimed stdout digest, and `diff` vs the entry's fenced stdout: STDOUT_BYTE_IDENTICAL. The entry's §Reproduce is honest; the a3498e25 pin is valid at d977619 because all 8 fixture/record paths compare `same` under `cmp` across both revisions (verified individually).

E2 Coordinate attack — semicolon (entry:24-25 vs saved records):
- js-r3 line 1 is 51 chars, js-r7-v2 line 1 is 41 chars; the char at column 50 / 40 is `;` (sliced from raw bytes: `";"`). LINE_RE requires `;$` line-final and fixture line 1 ends `');` with no trailing whitespace, so the match bound is the whole line.
- Manual call span [28,50)/[18,40) and binding span [6,50)/[6,40) all end exclusive of the `;`; the saved `end.column` 50/40 is end-exclusive and also excludes it. Semicolon is outside the call span, outside the binding span, and outside every saved span — entry items 4/5/8/9/11 are mutually consistent with the bytes.

E3 Coordinate attack — source span vs saved span (entry:37, item 11):
- Saved locations read from the archived records: js-r3 named edges (6,50) and (6,50), unnamed (28,50); js-r7-v2 named (6,40), unnamed (18,40); all start.line=end.line=1, kind `source-range`, source `index.js`.
- Slicing fixture line 1 at those saved columns reproduces exactly the claimed texts: `{ rot13, checksum } = require('./transform')`, `require('./transform')`, `{ rot13 } = require('./transform')`. Manual spans equal saved spans for all five edges. Item 11's "the bytes read back at the saved columns are the texts above" is independently reproduced from raw bytes, not from the entry's own tool.

E4 Coordinate attack — empty-line filtering before enumeration (readout.py:161-162 in entry):
- Code: `lines = [line for line in text.split("\n") if line.strip()]` then `enumerate(lines, 1)` — YES, empty/whitespace-only lines are filtered BEFORE enumeration, so `line_number_1based` is an index over non-empty lines, not physical file lines. This convention is not stated in §Limitations.
- On the frozen bytes it produces no false value: both index.js files split into 8 parts (trailing newline), all 7 physical lines non-empty, and the require line IS physical line 1, so printed `line_number_1based` 1 and `non_empty_lines` 7 are true under both readings (verified per-line with repr from raw bytes).

E5 Recorded-vs-derived labeling (entry:34-35, items 8/9):
- Saved `location` object keys are exactly {end, kind, source, start} — the saved record does NOT contain `span_1based_inclusive` or `span_text_from_fixture`; both are computed by readout.py (the latter by slicing the matched line at saved columns).
- Items 8/9 list these two derived fields inside the location's field list ("a `source-range` location ... with ... `span_1based_inclusive` ..., `span_text_from_fixture` ...") without a derived/recorded label. Nonfatal: the Observation preamble (entry:13) states every item is "produced by the `readout.py` block ... the pointer names the stdout record and its field", and both ARE stdout `imports_edge` fields mapped in the Q11 inventory (entry rows 8/9, `location.*`); item 11 gives the derivation by readback; `span_text_from_fixture`'s own name flags fixture slicing; items 6/7 label the genuinely recorded provider fields explicitly. Every value has true in-entry derivation+output; Q11's letter is met.

E6 Corroborated side values (all match my independent reads of archived bytes): six fixture digests + record digests 7c3ba8c1…/331ec252…, record bytes 193573/171150, evidence_ids ev_4a93276c…/ev_66f5dc7e…, operation analyze_javascript_application, provider rea-javascript-application v1, root digests 8eec9ffb…/696c2496…, identity keys `8eec9ffb…:transform.js`/`696c2496…:transform.js` (strategy artifact-local-key, namespace source-module), unnamed edges strategy content-digest with null namespace/key, counts 3/2/1 and 2/1/1, exactly three files per fixture dir, `"type":"commonjs"` in both package.json.

## Observation
1. Attack axes answered: empty lines ARE filtered before enumeration (harmless on these bytes, value true, convention undisclosed — cosmetic); semicolon is outside call/binding/saved spans consistently; source spans match saved spans for both selected files with the column base demonstrated by readback; the one-match fail-closed bound is real (SystemExit unless exactly one LINE_RE match).
2. Items 8/9 could be read as attributing `span_1based_inclusive`/`span_text_from_fixture` to the saved record; preamble+inventory+item 11 make provenance recoverable, no value is false. Minimal correction if L1 wants it: mark those two fields "derived by readout" in items 8/9. I made no repair.

## Inference
- [INFERENCE] The entry's §Reproduce is a faithful instrument: script digest and stdout digest both match, and every span/count/name value I re-derived from raw bytes equals the printed output. No contradiction with any claimed value was found; no Q01–Q13 ground for rejection surfaced on this seat's axes (Q11 derivation mapping verified for items 3-5, 8-11).

## Unknown
- Whether `line_number_1based`'s non-empty-line convention should be disclosed as a limitation is an L1 wording-judgment; on the frozen bytes it changes nothing (require line is physical line 1 in both files).
- Broader-than-two-fixture regex behavior (other syntactic shapes) is out of the entry's declared scope and was not tested.

VERDICT: HOLDS — no contradiction, no missing requirement on the assigned regex/readout-coordinate axes; reproducible end-to-end at SHA level. Candidate stays admission-pending with L1; no flip claimed here.
Installs: none (stock python3 only; no tool installed or updated).
