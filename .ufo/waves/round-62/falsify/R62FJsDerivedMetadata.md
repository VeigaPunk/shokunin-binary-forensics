GRADE: PARTIAL — corpus/knowledge/round-62-commonjs-require-name-evidence.md (C04 candidate), computed vs recorded metadata labelling (Q11 labelling wording; Q09/Q10 unaffected)

## Target identity
- Frozen revision: d97761952be256d145d298022de03091de91d358 (`git cat-file -t` -> commit); derivation revision a3498e25ad87bf756288812d0ea7c474b09433c7 (commit).
- Candidate blob 480f62c490b43d7c21248caf8905357d1bb67726; file SHA-256 42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3.
- Extract: `git -C <repo> archive d977…d358 | tar -x -C /fast/scratch/hyaku/revenger-r62/R62FJsDerivedMetadata/tree`, cwd=/, TMPDIR under own scratch.
- `git diff --stat a3498e25… d977… -- corpus/fixtures/js-r3 corpus/fixtures/js-r7-v2 <both records>` -> empty, rc 0. The inputs are byte-identical across the two revisions.
- Method: independent jq/sha256sum/stat reads of the archived records. readout.py was NOT executed (that is the reproduce seat's job). No JS, no EVM, no provider, no network.

## Observation (primary evidence)
O1. Computed record metadata matches. `stat -c %s` gives 193573 and 171150. `sha256sum` gives 7c3ba8c15673a7e48600bba3f42a6ca3935dbd75e30832569a631979e31ed452 and 331ec252aefdc7715e49f039d7443736ff9560565f208f35b4c972bfe45d564e. In readout.py these come from `len(record_bytes)` and `sha(record_bytes)` (entry lines 185-186), so they are computed, not stored in the records.
O2. Stored fields match. `jq '{evidence_id,operation,provider,root:.normalized_result.root_artifact_sha256}'` returns:
  - ev_4a93276c…1c7e / ev_66f5dc7e…987c
  - operation `analyze_javascript_application`
  - provider `{"id":"rea-javascript-application","name":…,"version":"1"}`
  - root 8eec9ffb7f5856da96d9411dc0dc024f39d781842853dc78c59ddc431e929f32 / 696c24963ebaeb9f9d208a655d87c12bba322775bd95f8efabd914b49a78f655.
  readout.py reads all of these with `record.get(...)`, which is a stored-field read. Item 6 and the S030 bullet label them recorded, which is correct.
O3. The directory-root digest is correctly labelled recorded: items 7 and 20 say "recorded, not re-derived". No digest over a directory is computed anywhere in readout.py.
O4. Every prose alias is a prefix of the full value printed in stdout. Checked: 92ef8e3d…, cd9f3f63…, 8eec9ffb…(:transform.js), 696c2496…(:transform.js), a3498e25…. Full digests appear in the header, item 1 and item 6.
O5. Identity claims about the entry's own blocks hold.
  - The extracted ```python block -> `sha256sum` 31dac2113f1b78967a635fbf65125ecedc7a7ab4924debad8ba3c4be77ee02ac (claimed 31dac211…02ac).
  - The extracted stdout block -> 58b63dd9d7c7ae4a0311ff33f12317345f7e5b7c9e8f204cfb13d1d599f0c416, `wc -l` 25 (claimed 58b63dd9…c416, 25 lines).
O6. DEFECT A: computed facts are labelled recorded.
  - Item 6 (entry line 29) lists bytes and file SHA-256 alongside the Evidence ID, operation and provider, then says: "These are **recorded** fields of the saved files, not re-derived here."
  - Bytes and file SHA-256 are not fields of the saved files (see O1). They are computed in-entry.
  - This contradicts the entry's own header line 2 ("record SHA-256"), item 17 ("the two record digests cover those saved record files"), the Q09 row ("each printed digest binds the bytes it was computed over (§A items 1, 6)") and the S030 bullet, which correctly limits "recorded" to provider, operation, Evidence ID and root.
O7. DEFECT B: the Q11 inventory overclaims what the edge rows carry.
  - Rows 8 and 9 (lines 264-265) read "js-r3's three `imports` edges, all saved fields" and "same".
  - The records carry fields that `import_edges()` never projects. On the target nodes: `identity.sha256`, `identity.artifact_sha256`, `identity.stability`. In the edge properties: `module_link_kind`, `imported_path`, `local_name`, `exported_name`, `resolution_status`, `target_file_kind`, `target_json_status`, `kind`, `expression`, and `evidence.location.available`.
  - Primary evidence: `jq '.normalized_result.graph.nodes[]|select(target ids)'` and `jq '.normalized_result.graph.edges[]|select(.relation=="imports")|{p:.properties,loc:.evidence.location}'`.
  - The overclaim contradicts the entry's own item 21 ("only the fields named in items 1-13 were read") and item 24 ("other properties … were not compared").
O8. DEFECT C: the record-to-fixture pairing has no derivation and no recorded label.
  - The Scope sentence (line 10) says the records "describe them (… for js-r3, … for js-r7-v2)".
  - The only in-entry source of that pairing is the hard-coded `FIXTURES` tuple (lines 101-104). Nothing printed supports it.
  - The records themselves carry `subject.name` "js-r3"/"js-r7-v2", `subject.digest.sha256` (equal to root) and `normalized_result.input_path`/`subject.local_path`. Those paths are `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/js-r3` (and `/js-r7-v2`), a different directory from the archived `corpus/fixtures/…`. None of these fields is printed or cited.
O9. No unsupported per-file graph binding.
  - The `javascript-asset` target carries `identity.sha256` cd9f3f63…a345, and the `javascript-module` target carries `identity.artifact_sha256` cd9f3f63…a345. Both equal the computed `transform.js` digest (item 1).
  - The entry neither prints nor claims that equality. Item 17 says "no equality between a provider digest and a local file digest is claimed", and item 8's "no namespace or key" is literally true for those two keys.
O10. No recorded value is presented as re-derived. Evidence ID, operation, provider id/version and root are all labelled recorded (items 6, 7, 20; S030 bullet), consistent with claims.md:27 ("A saved identifier is recorded, not authenticated.").

## Inference
I1. [INFERENCE] Defects A-C are labelling and wording defects. No printed value is wrong, and every computed value has its in-entry derivation and output (O1, O5). That is why the grade is PARTIAL, not BROKEN.
  - Q11's reject conditions ("correct value without derivation"; "recorded value presented as re-derived") are not triggered.
  - Defect A is the reverse mislabel: it understates derivation, which misleads a Q11 auditor about which values are re-derived.
  - Defect B is a false "carries all fields" claim of the kind lessons/round-62.md:99-101 asks reviewers to audit ("Audit claims that the block 'carries' a field").
I2. [INFERENCE] Defect C is an identity premise of the comparison. Item 14's within-fixture agreement depends on the pairing.
  - The printed span readback constrains it indirectly. A swapped pairing would slice js-r3's line at [6,40) and [18,40), giving text that is visibly not the binding or call text, and the name delta would become non-empty.
  - So the pairing is consistency-supported, but no printed field derives it and it is not labelled recorded. The differing `local_path` means "describe the archived directory" is a premise, not an observation.

## Unknown
U1. Whether the producer's input directory at `/home/vgpnk/Projects/prymeagnt/…/fixtures/js-r3` was byte-identical to the archived fixture is unknown. The root construction was not re-derived, and this seat derives none.
U2. Whether L1 treats defect B (a short-form inventory cell) as a Q11-fatal contradiction rather than wording is L1's judgment.

## Out-of-scope note (not graded here)
N1. `line_number_1based` is computed as an ordinal over non-empty lines (line 162), not as a physical line number. Here it coincides: `awk END{NR}` = 7 and `grep -c .` = 7 for both `index.js` files, and both files begin with `const`. I leave this to the span/source seats.

## Smallest safe correction (do not apply; for L1)
- Defect A: item 6. Split the sentence: "Byte count and file SHA-256 are computed by §Reproduce. Evidence ID, operation, provider id and version are recorded fields of the saved files, not re-derived."
- Defect B: inventory rows 8 and 9. Replace "all saved fields" with "the projected fields listed (other saved edge/identity fields not read)".
- Defect C: Scope. Label the pairing "paired by this entry (`FIXTURES`); not derived". Optionally print `subject.name`/`input_path` as recorded, noting that `local_path` differs from the archived path and the root is not re-derived. Claim no per-file binding.

VERDICT: PARTIAL. Item 6 labels computed record facts as recorded (A). The inventory says the edge rows carry "all saved fields" (B). The record-to-fixture pairing has no derivation and no recorded label (C). Hashes, aliases, recorded-field labels and root-digest handling hold, and no per-file graph binding is claimed.
Installs: none. Tools used: /usr/bin/python3 (Python 3.14.8) not invoked on any fixture; /home/vgpnk/.local/bin/jq, coreutils sha256sum/stat/wc, awk, git archive/diff/cat-file (read-only).
Scratch: /fast/scratch/hyaku/revenger-r62/R62FJsDerivedMetadata/{tree,readout.py,stdout.txt,tmp}.
