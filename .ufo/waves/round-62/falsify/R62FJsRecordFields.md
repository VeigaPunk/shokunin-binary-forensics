GRADE: PARTIAL — corpus/knowledge/round-62-commonjs-require-name-evidence.md (C04)

FROZEN: rev `d97761952be256d145d298022de03091de91d358`; extracted read-only with
`git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive d9776195… | tar -x -C tree-d977` (exit 0).
Candidate blob `git show d977…:corpus/knowledge/round-62-commonjs-require-name-evidence.md | sha256sum`
→ `42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3`, 296 lines; absent at
`a3498e25ad87bf756288812d0ea7c474b09433c7` (`git cat-file -e` → fatal, rc 128). README C04 still `uncovered`.

OBSERVATION (archived copies only, cwd=tree-d977):
- `stat -c %s corpus/live/runs/20261012T164357Z/analysis.json corpus/live/runs/round-7/v2-analysis.json`
  → `193573`, `171150`; `sha256sum` same → `7c3ba8c15673a7e48600bba3f42a6ca3935dbd75e30832569a631979e31ed452`,
  `331ec252aefdc7715e49f039d7443736ff9560565f208f35b4c972bfe45d564e`. Both records and all six fixture
  files are byte-identical at a3498e25 (`cmp` SAME ×8).
- JSON read (python stdlib): `evidence_id` `ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e`
  / `ev_66f5dc7e3e8a8d6033c17c400762521d815d77c5ac9a9c7e1b6a45232cd7987c`; `operation`
  `analyze_javascript_application` both; `provider` `{id:"rea-javascript-application", name:"REA JavaScript
  application analyzer", version:"1"}` both; `normalized_result.root_artifact_sha256`
  `8eec9ffb7f5856da96d9411dc0dc024f39d781842853dc78c59ddc431e929f32` /
  `696c24963ebaeb9f9d208a655d87c12bba322775bd95f8efabd914b49a78f655`, equal to `subject.digest.sha256`
  (True both). These match entry :29/:30 and stdout records at entry :226/:238 exactly.
- Each record file's own SHA-256 does not occur in its bytes (`own.encode() in b` → False both): the file
  digest is computed, not recorded in the record.
- Root-digest absence bound holds: `grep -rIl root_artifact_sha256 --include=*.py --include=*.sh
  --include=*.rs --include=*.go --include=*.ts --include=*.js .` → empty; outside corpus/live the tree
  hits are only .ufo build notes and this candidate. S029 (spec) and S030 (own-work) are `mined`, tier A,
  opened 2026-10-21 (SOURCES.md:43-44), scopes matching the entry's use.
- Entry code block reconstructed to readout.py → sha256 `31dac2113f1b78967a635fbf65125ecedc7a7ab4924debad8ba3c4be77ee02ac`
  (= claimed); `python3 -B readout.py tree-d977` → exit 0, 25 lines, stdout sha256
  `58b63dd9d7c7ae4a0311ff33f12317345f7e5b7c9e8f204cfb13d1d599f0c416`, `cmp` identical to the entry's
  §Exact stdout; rerun on tree-a349 gives the same 25 lines and digest.

INFERENCE:
- Every item 6 / item 7 value is correct and printed by the in-entry command. The provider root digest is
  read from `normalized_result` and labelled recorded; the absence sentence is bounded ("no opened source"),
  adds "this entry derives no digest over a directory", and asserts no non-recomputability (contrast the
  round-61 evidence_id caution). Q11's positive condition is met for these values.
- Q11 wording defect at entry :29 (item 6): "These are **recorded** fields of the saved files, not
  re-derived here" covers the byte counts and the two file SHA-256s, which the same entry's readout
  computes (`len(record_bytes)`, `sha(record_bytes)`, readout.py:84-85,101-102) and which item 17 (:49)
  calls "computed over". The saved JSON cannot carry its own digest (0 occurrences). The label is false
  for the derived byte hash/counts and true only for Evidence ID/operation/provider id/version.
- Minimal correction: split the sentence — bytes/SHA-256 derived by the readout's hashlib over the saved
  files; Evidence ID/operation/provider id/version read as recorded fields. No value or derivation is
  missing, so nonfatal to the record comparison; the provenance sentence is wrong → PARTIAL (Q11 wording).

UNKNOWN:
- S029's page digest and quote were not re-opened by this seat (outside this assigned item; the row and
  the round-62 Gate carry them).
- Whether the provider's directory-digest construction exists outside the opened sources was not tested;
  the entry makes no universal claim, so this does not affect its bounded sentence.

ADJACENT (unowned; span seat; not my grade basis):
- Entry :34/:35 say the edges "carry … `span_1based_inclusive` … `span_text_from_fixture`". The saved
  `evidence.location.value` has only `kind,source,start{line,column},end{line,column}`; both span fields
  are readout-computed (readout.py:62-64), so they are true of the readout's `imports_edge` record, not
  of the saved edge. If "carry" is read as saved-field provenance, items 8-9 and Q11 inventory rows 8-9
  (:264-265, "all saved fields") are referent errors; the values themselves are printed.

VERDICT: PARTIAL — record files/bytes/SHA-256, Evidence IDs, operation, provider id/version and both root
digests all verified against the saved records, with in-entry derivation and output; the only defect in
this item is item 6's blanket recorded/not-re-derived label for the derived file bytes and SHA-256 (Q11
wording-only). No admission recommendation; no repair made.

INSTALLS: none (git archive/cmp/stat/sha256sum and python3 stdlib only; no packages installed).
