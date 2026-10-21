# R61 reviewer: other verifiers, identity/receipt/digest deletion survey

Scope: corpus/verify_{evm_evidence,icon_states,js_graph_delta,named_multi_icon_states,pe_resources,saved_evidence,semantic_trace,shape_evidence}.py at base e0a4b0c (scratch copies sha256-identical to the live lane). Not claimed this round. C2 targets verify_icon_languages.py and verify_multi_icon_states.py not surveyed.

Method (executed in a /tmp copy only; live lane not written): each `and`-conjunct of every assert/require/req replaced by True (equal to deleting it from the chain), plus whole-statement and joint mutants; each run with the probe flag `--self-test` from cwd=/; killed = nonzero exit. Baselines 8/8 exit 0 (self-test and plain); ast.unparse round-trip identical 8/8. Runs: 295 single-clause, 147 statement-level, 6 joint.

Codes: K = killed by one deletion. M = falsified by its control but masked by a sibling (killed only jointly). U = no control falsifies it, so deletion is undetectable by the run.

| row | path:line | clause (ID identity, RCPT receipt, DIG digest) | n | code |
|---|---|---|---|---|
| E1 | verify_evm_evidence.py:26-29 | fixture identity: carrier/decoded sha, size, encoding | 4 | U |
| E2 | verify_evm_evidence.py:37-40 | saved Evidence: evidence_id, operation, subject digest, encoding | 4 | U |
| E3 | verify_evm_evidence.py:41-45 | artifact/bytecode sha256, bytes, hex | 5 | U |
| E4 | verify_evm_evidence.py:51-56 c2 | raw bytecodeOffset == target (control :67-68 falsifies c2,c3,c5,c6,c7) | 1 | M: rc=1 only if all five deleted |
| J1 | verify_js_graph_delta.py:31 | operation | 1 | U |
| J2 | verify_js_graph_delta.py:53-55 | saved parent evidence_id x2 | 2 | U |
| J3 | verify_js_graph_delta.py:58 c0 | left graph == source truth | 1 | U |
| J4 | verify_js_graph_delta.py:58 c1 | right graph == source truth (control :70-73) | 1 | K: "altered v2 graph was accepted" |
| I1 | verify_icon_states.py:126-132 | fixture sha, evidence_id, operation, subject, artifact sha/bytes | 6 | U |
| I2 | verify_icon_states.py:143-146 | RCPT exit_code, fixture_sha256, stdout_sha256, evidence_id | 4 | U (no receipt control) |
| N1 | verify_named_multi_icon_states.py:65 | normalized result == artifact dict + decoded tree (controls :89-97) | 1 | K: "r56 forged claim accepted" |
| N2 | verify_named_multi_icon_states.py:68-69 | len/H(d) digest, evidence_id, operation, subject, artifact dict | 6 | U |
| N3 | verify_named_multi_icon_states.py:72 | RCPT command c0, exit_code, fixture_sha256, evidence_id, stdout_sha256, duration x2 | 7 | U (no receipt control) |
| N4 | verify_named_multi_icon_states.py:74 | exact UTF-16 name bytes | 1 | U |
| P1 | verify_pe_resources.py:26-28 | fixture sha/size; authored payload bytes and sha | 4 | U |
| P2 | verify_pe_resources.py:31-35 | evidence_id, operation, subject, artifact sha/bytes/format/machine | 7 | U |
| P3 | verify_pe_resources.py:43-46 | resource type/name/language identity | 6 | U |
| P4 | verify_pe_resources.py:48-52 c2,c3 | payload sha == truth; payload sha == sha256(payload) (control :61-62) | 2 | M: each alone rc=0, pair rc=1 |
| Z1 | verify_saved_evidence.py:32,35,39,40 | ZIP operation, nested evidence_id, root format, root digest | 4 | U |
| Z2 | verify_saved_evidence.py:46 c0 | root format == zip | 1 | U |
| Z3 | verify_saved_evidence.py:46 c1 | root size == archive_size == len (control :131-132) | 1 | K: "ZIP: altered proof accepted" |
| Z4 | verify_saved_evidence.py:47,52,54,55 | root node sha; detached member; hash_status; duplicate path | 4 | U |
| Z5 | verify_saved_evidence.py:62,63,66,75-76 | member manifest, paths, per-member sha/size; ELF digest | 4 | U |
| Z6 | verify_saved_evidence.py:81-82 | JS operation, evidence_id | 2 | U |
| Z7 | verify_saved_evidence.py:95,97-98 | package main/type; asset digests | 3 | U |
| Z8 | verify_saved_evidence.py:114-116 c0 | declared_path == package main | 1 | U |
| Z9 | verify_saved_evidence.py:114-116 c1 | resolved_path == index.js (control :133-136) | 1 | K: "JS: altered proof accepted" |
| M1 | verify_semantic_trace.py:27-29 | parent/trace evidence_id, operation | 4 | U |
| M2 | verify_semantic_trace.py:30 c0, :32-34 | request-parent binding; source_evidence_id; evidence_links; source_graph_id | 4 | U |
| M3 | verify_semantic_trace.py:53-54 | node == parent node; module_path; artifact_sha256 | 3 | U |
| M4 | verify_semantic_trace.py:61-63 c1 | evidence context == parent context | 1 | U |
| M5 | verify_semantic_trace.py:68-71 c0 | relation == saved parent relation (control :90-91) | 1 | M: with M6 c2 (rc=1); alone rc=0 |
| M6 | verify_semantic_trace.py:75-77 c0, c2 | source == index.js (c0); token == name (c2) | 2 | c0 U; c2 M with M5 |
| H1 | verify_shape_evidence.py:41, 50-51 c1, 60 c1 | parent operation; parent artifact sha; saved fields == source truth | 3 | U |
| H2 | verify_shape_evidence.py:65-66, 71-73 | comparison operation/evidence_id; parent link ids; graph_id | 4 | U |
| H3 | verify_shape_evidence.py:74-77 c1,c4; 79-80 | requested module path; selected node ids | 4 | U |

Totals: 110 clauses in 36 rows. K 4 (J4, N1, Z3, Z9); M 5 (E4, P4 x2, M5, M6-c2); U 101, including all 11 receipt clauses (I2, N3) and every fixture digest. Statement-level kills (8): evm :51-56, icon :161, js :58, named :65, pe :48-52, saved :46 and :114-116, shape :96-97. Semantic :68-77 is masked across two statements (0 alone, rc=1 jointly).

Notes:
- Own-run gating: six scripts run their only negative control under --self-test (evm :66, js :69, pe :60, saved :130, semantic :89, shape :112); plain runs print no NEGATIVE. icon_states (inline :157-165) and named_multi (inline :89-97) have no flag.
- Every control mutates a deep copy of a saved record only (evm :67-68, js :70-73, pe :61-62, saved :131-136, semantic :90-91, shape :113-114, icon :157-158, named :89-91). None touches fixture bytes, receipt.json or truth constants, so no receipt or fixture-digest clause has a kill path in any of the 8 scripts.
- Non-identity kills, outside the table: icon :161 (candidate relation) and shape :96-97 (presence).
- Masking is the calibration risk: E4 needs five deletions (four leaves rc=0); P4 and M5/M6 need pairs. Single-clause probes alone undercount kills.
- C2 scope: named_multi :72 c0 (receipt command, row N3) is unkilled in its own run; its only kill is external N2 (reports/round-1/replay_scenarios.py:341-344, forger :196-204, runner :297-300), checked by grep only, not executed. icon_states :143-146 (I2) is the same receipt gap and is not in C2. Rule implied for the C2 control: the forged command must leave every sibling conjunct True, or mutant b survives (cf. P4, E4).
- Identity classification is mine: identity binds the record to Evidence ID, operation, subject, artifact, parent/graph, source truth or resource key; RCPT = receipt field; DIG = hash equality. Counts, offsets, semantic values, shapes and provenance are excluded. Clause-level TSV (295 rows with codes): /tmp/revenger-r61-ReviewerOtherVerifiersGap-clauses.tsv.

Confidence: high on executed outcomes for these eight scripts at e0a4b0c; medium on the identity boundary (rule above; TSV allows a re-cut). Falsification sets were derived from reading before the statement and joint runs; the runs matched every one.
Gaps: probe d2 forgeries and N2 not executed; C2 scripts not surveyed; no lane writes.

VERDICT: 110 identity/receipt/digest clauses across the eight verifiers: 4 killed by their own run, 5 only jointly, 101 with no kill path, including all 11 receipt clauses and every fixture digest; the receipt gap is also unclaimed in verify_icon_states.py and verify_named_multi_icon_states.py.
Installs: none (python3 3.14.8 already present; no pacman, uv or npm transactions).
