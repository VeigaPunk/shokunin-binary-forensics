RESULT: COMPLETE
# R62MutantJsNameSet — one bounded C04 saved-name forgery
Axes: detector discrimination; primary-byte traceability; exact restoration; isolation/scope fidelity.
Frozen revision (recorded extraction selector): `a3498e25ad87bf756288812d0ea7c474b09433c7`.
Read frozen claims:17–21,29–50; QUALITY:23–25; round-61-verifier-spotcheck:206–218. No admission decision made.
Scratch root: `/fast/scratch/hyaku/revenger-r62/R62MutantJsNameSet/`.

## Commands, artifacts and expected detector
Extraction, cwd `/`: `mkdir -p /fast/scratch/hyaku/revenger-r62/R62MutantJsNameSet/archive && git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive a3498e25ad87bf756288812d0ea7c474b09433c7 | tar -x -C /fast/scratch/hyaku/revenger-r62/R62MutantJsNameSet/archive` — successful, no stdout.
Probe, cwd `/`: `python3 -B /fast/scratch/hyaku/revenger-r62/R62MutantJsNameSet/mutation_probe.py` — exit 0.
Own stdlib reader: scratch `detect_names.py`; harness: `mutation_probe.py`; complete output: `probe-output.txt`; structured outcomes: `probe-results.json`.
Before/forged record artifacts: scratch `pristine-v2-analysis.json` and `mutated-v2-analysis.json`; archived record restored in `finally` before its last detector run.
Expected: derive shorthand source names independently from `corpus/fixtures/js-r7-v2/index.js:1`; compare their set against normalized named `imports` edges for that require specifier/source. Pristine/restored match (0); forged `imported_name` mismatches (1).
The same detector command/code ran on all three byte states; it did not consume truth.json, old verifier results or rejected-entry prose.

## Actual output
```text
frozen_revision_recorded=a3498e25ad87bf756288812d0ea7c474b09433c7
python=3.14.8 (main, Oct  2 2026, 10:23:31) [GCC 16.2.1 20260810]
detector_sha256=bb96801b51ecb5b25040f0e689e9da60b4ee3dc194d919cfb378d05f4fa20301
source_sha256=b53d96d432c120f6217a2da2ea3ed592308a3a23ef1a01745a22fd335ac4c42a
record_before_sha256=331ec252aefdc7715e49f039d7443736ff9560565f208f35b4c972bfe45d564e
record_mutated_sha256=360d92b4b0476a04e0e0137ee5b1c3b7bc06c9b26820cc12170b3da3520419bf
semantic_delta=[{"path":["normalized_result","graph","edges",9,"properties","imported_name"],"before":"rot13","after":"checksum"}]
byte_delta={"offset_zero_based":30558,"removed":"rot13","inserted":"checksum","before_bytes":171150,"mutated_bytes":171153,"unchanged_prefix_bytes":30558,"unchanged_suffix_bytes":140587}
PHASE=pristine COMMAND=/usr/bin/python3 -B /fast/scratch/hyaku/revenger-r62/R62MutantJsNameSet/detect_names.py /fast/scratch/hyaku/revenger-r62/R62MutantJsNameSet/archive
source=corpus/fixtures/js-r7-v2/index.js
record=corpus/live/runs/round-7/v2-analysis.json
source_line=1 const { rot13 } = require('./transform');
selected_named_require_edges=1
source_names=["rot13"] imported_names=["rot13"]
missing=[] unexpected=[]
NAME_SET=MATCH
EXIT=0
PHASE=mutated COMMAND=/usr/bin/python3 -B /fast/scratch/hyaku/revenger-r62/R62MutantJsNameSet/detect_names.py /fast/scratch/hyaku/revenger-r62/R62MutantJsNameSet/archive
source=corpus/fixtures/js-r7-v2/index.js
record=corpus/live/runs/round-7/v2-analysis.json
source_line=1 const { rot13 } = require('./transform');
selected_named_require_edges=1
source_names=["rot13"] imported_names=["checksum"]
missing=["rot13"] unexpected=["checksum"]
NAME_SET=MISMATCH
EXIT=1
PHASE=restored COMMAND=/usr/bin/python3 -B /fast/scratch/hyaku/revenger-r62/R62MutantJsNameSet/detect_names.py /fast/scratch/hyaku/revenger-r62/R62MutantJsNameSet/archive
source=corpus/fixtures/js-r7-v2/index.js
record=corpus/live/runs/round-7/v2-analysis.json
source_line=1 const { rot13 } = require('./transform');
selected_named_require_edges=1
source_names=["rot13"] imported_names=["rot13"]
missing=[] unexpected=[]
NAME_SET=MATCH
EXIT=0
record_after_sha256=331ec252aefdc7715e49f039d7443736ff9560565f208f35b4c972bfe45d564e
restoration={"record_exact_bytes":true,"source_exact_bytes":true,"readme_exact_bytes":true}
VERDICT=killed
```

## Verdict, exact delta and limits
**Killed by this independent reader**, not by an old verifier: exactly one parsed JSON leaf changed, `normalized_result.graph.edges[9].properties.imported_name`, `rot13` → `checksum`; five value bytes became eight, with every byte outside that replacement preserved. No clause was deleted.
Restoration evidence: before/after SHA-256 identical; exact byte equality true; pristine/restored stdout identical. Source and scratch README bytes also unchanged.
Only v2's selected imported-name value set was challenged. js-r3 was read, not mutation-tested. Duplicate multiplicity, imported_path/local_name, call spans, IDs/digest authenticity, producer behavior, runtime, Electron roles and general JavaScript parsing remain untested/unguarded here.
No old-verifier deletion coverage or Q13 deletion credit; no completeness, new gate, source-tier admission or C1 coverage increase claimed. Incorporating evidence into an entry still requires its own in-entry code/output and all unchanged admission criteria.
Production writes are confined to this assigned report; no production corpus/README, prior evidence, source rows, git/jj state or sibling files were edited. Frozen C04/C09 README rows remain uncovered; this probe confers no held status.
Proposed artifacts are confined to the named scratch reader/harness, outcome logs and paired record bytes; no production change proposed.
Installs or updates: none.
