GRADE: PARTIAL — C04 candidate `corpus/knowledge/round-62-commonjs-require-name-evidence.md` at frozen rev d97761952be256d145d298022de03091de91d358

# Falsify report — R62FJsImportsNames (C04 CommonJS imports/names fields)

## Frozen target

- Entry file: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-62-commonjs-require-name-evidence.md`
- File SHA-256 `42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3`; identical to `git show d9776195:…` (working copy clean).
- Frozen rev `d97761952be256d145d298022de03091de91d358` (candidate state); claim base `5bd4a90fc1a34caa94496601b60537b3aab12301`; pre-registration `a3498e25ad87bf756288812d0ea7c474b09433c7`.
- Archive digests (`git archive | sha256sum`): d9776195 `4b52df49bbd6349d6ac8c45c4f7d73d9e7125c7f719950e89818cad21dc8cebc`; a3498e25 `269874834fd6a2b0289e9103e1c0166c9ac744aefbc55c897b103816c430e58d`.
- Scratch only: `/fast/scratch/hyaku/revenger-r62/R62FJsImportsNames/` (tree, readout.py, out.txt). TMPDIR=`…/tmp`. No repo mutation, no fixture-JS/VM execution, no producer/RPC call.

## Attack axis (as assigned) — normalized_result.graph `imports` field values

**Observation — reproduction is byte-exact.** Code block extracted from the entry (lines 85–213) hashes to `31dac2113f1b78967a635fbf65125ecedc7a7ab4924debad8ba3c4be77ee02ac` = the `readout.py` digest claimed in §Reproduce. Run on the frozen archive:

```
python3 -B readout.py tree   # exit 0, 25 stdout lines
sha256sum out.txt → 58b63dd9d7c7ae4a0311ff33f12317345f7e5b7c9e8f204cfb13d1d599f0c416
```

matches the claimed stdout digest; the entry's printed stdout block hashes to the same value. Identical output on the `a3498e25` tree (`cmp` equal). Zero-match and two-match mutants of `js-r3/index.js` both exit 1 with "expected exactly one destructured require line" — the fail-closed bound the entry claims is real.

**Observation — the two confusions the axis warned about are avoided.** The readout reads `normalized["graph"]`, filters `relation == "imports"`; `normalized_result.semantic_graph` has **0** edges and its relations are `aliases/defines/reads/captures/reads-property/coerces/writes` — no `imports` relation in either record, and `raw_result` is `None` in both. No count here can be confused with a semantic-graph set. Conversely, items 14/15/25 explicitly confine both deltas to `imported_name` **name values** and disclaim any edge-set delta. The S030 anchor names the exact path (`normalized_result.graph.edges` where `relation=imports`).

**Observation — every derived value re-verified against the primary records** (independent of the entry's own script):

| claim | independent check | result |
|---|---|---|
| js-r3 imports edges 3 (named 2, unnamed 1); js-r7-v2 2 (named 1, unnamed 1) | raw `graph.edges` where `relation=='imports'` | exact |
| named values js-r3 {rot13, checksum}, js-r7-v2 {rot13} | `properties.imported_name` of those edges | exact |
| `specifier` "./transform", `resolved_path` "transform.js", `state` "inferred" | all 5 imports edges | exact |
| location 6→50 / 28→50 (js-r3), 6→40 / 18→40 (js-r7-v2) | `evidence.location.value` | exact |
| `span_text_from_fixture` | independent slicing of `index.js` line 1 | `[6:50]`=`{ rot13, checksum } = require('./transform')`, `[28:50]`=`require('./transform')`, `[6:25]`/`[6:15]` exact |
| end-column is end-exclusive | `len("require('./transform')")`=22, 28+22=50 | exact |
| record 193573 B / 171150 B, digests, Evidence IDs, `analyze_javascript_application`, provider `rea-javascript-application` v1 | file bytes + JSON | exact |
| `root_artifact_sha256` 8eec9ffb… / 696c2496… | `normalized_result.root_artifact_sha256` | exact (correctly labelled recorded) |
| S029 page digest 06db92a8…, draft "October 16, 2026", §14.3.3.3 quote | re-fetched https://tc39.es/ecma262/ | digest identical; colophon "Draft ECMA-262 / October 16, 2026"; clause text is "Set value to ? GetV ( value , propertyName )." as the entry says |
| Q13 stance, README C04 still `uncovered`, admission-status `candidate` | README row + entry front matter | exact |

## Findings (severity order)

**F1 — the one factual misstatement: `imported_name` is ABSENT on the unnamed edge, not `null` (entry:34 and :35).** Entry item 8: "The third edge carries `imported_name` `null` (no name)"; item 9: "the unnamed one carries `imported_name` `null`". Primary record:

```
js-r3  edges[9].properties keys = ['expression','kind','resolved_path','specifier']   # 'imported_name' key ABSENT
js-r3  edges[1]/edges[3] (exposes) properties = [... 'imported_name' …] → imported_name = None   # key PRESENT, null
js-r7-v2 edges[2].properties keys = ['expression','kind','resolved_path','specifier']   # ABSENT
```

The readout prints `props.get("imported_name")`, so an absent key and an explicit null are indistinguishable in its stdout — the printed `null` does not derive the claim "carries". Within one record the two states are distinguishable and meaningful, so the conflation is not harmless. **No count, name set, span, digest, or inference changes** — the semantic conclusion ("this edge has no import name") is right, and the Q11 letter is satisfied (a command and its output are in the entry). Minimal correction, named only: in items 8 and 9 say the unnamed edge's `properties` object has **no** `imported_name` key (the readout renders absent as `null`); if the distinction is to be carried in the output, have `readout.py` print key presence (e.g. `imported_name_present: false`) so the stdout itself shows it.

**F2 — dangling cross-reference `§A` (entry:18,19,23,24,25,29,30,34,35,36,37,41,42 and the QUALITY rows at :289,:292).** `§A` occurs 15 times and is defined nowhere: no heading contains it, and `grep -c '§A'` over every other file in `corpus/knowledge/` and `corpus/` returns 0. The intended referent is the stdout block (§Reproduce → "Exact stdout"), but the label as written resolves to nothing, so every Observation pointer and the Q06/Q09 bases are unresolvable as written. The Q11 inventory table does independently map each sentence to a stdout record + field, so no value is left underived. Minimal correction: define `§A` once (e.g. "§A — the stdout records in §Reproduce/Exact stdout") or re-point each pointer at that anchor.

**F3 — the quoted-text word count is not reproducible under the corpus's own convention (entry:248).** Entry: `"Set value to ? GetV(value, propertyName)." — 8 words`. The corpus precedent for an explicit count is `corpus/lessons/round-61-verifier-spotcheck.md:150` ("…to the less volatile." (13 words, ≤25.)), where 13 = whitespace tokens of the quoted sentence. Whitespace tokens of the S029 quote = **6**; HTML-normalized ("Set value to ? GetV ( value , propertyName ) .") = 11. No convention I can derive yields 8, and unlike every other value in the entry this count carries no in-entry derivation command. Both 6 and 8 are ≤25, so the corpus quote-length limit is unaffected. Minimal correction: align to the precedent (6) or drop the number and keep only the ≤25 assertion.

## Inference (separate from observation)

- The entry is substantively reproducible: I could not break any count, name set, span, digest, specifier/resolved_path/state value, target identity, or the reproduce digest; no criterion hard-fails. The three findings are a record-field-presence misstatement (F1) plus two labeling/citation imprecisions (F2, F3).
- F1 is the only one a reader could act on wrongly: a consumer wanting to know whether the provider stores `imported_name: null` or omits the key gets the wrong answer from entry:34/:35.
- Scope note: the S029 quote is not unique to the `SingleNameBinding : BindingIdentifier` case — the same step text also appears in the `BindingElement : BindingPattern` case of the same clause 14.3.3.3 (and in 14.3.1.3). Entry:16's use is still supported, so this is a non-material note, not a defect.

## Coverage (judged axis)

- Covered and verified: js-r3 and js-r7-v2 fixture bytes; both saved records; every `imports`-edge field the entry names; the reproduce command and its stdout digest; S029's page digest/date/quote; S030's record digests; the graph-vs-semantic_graph and name-set-vs-edge-set boundaries; the Q13 no-guard-credit stance; README C04 still `uncovered`.
- Not covered by this entry (recorded for L1, not a defect): the C04 row's third fixture family `shapes-r12` (v1/v2) is untouched; no Electron-role evidence is offered (correctly — round-61 rejected that claim); no `verify_js_graph_delta.py` / `verify_semantic_trace.py` / `verify_shape_evidence.py` clause is credited (correctly — Q13). If L1 admits this entry as the C04 knowledge cell, the row surface "JavaScript/Electron packages" would rest on CommonJS require-name correspondence only, with no Electron and no shapes-r12 evidence.

## Unknown / verification gaps

- The `imported_name` key-presence distinction on the unnamed edge is asserted nowhere in the entry, so I cannot tell whether the author intended "absent" or believed it stored null; only the record can decide, and it says absent.
- I did not re-derive `root_artifact_sha256`'s construction (the entry correctly labels it recorded and out of scope); I confirmed only that the record's own field carries that value.
- Whether L1 treats F1 as a §Observation wording fix or as an admission-blocking Q11 issue is L1's call, not mine.

## VERDICT

PARTIAL, not BROKEN. The C04 candidate's central correspondence — graph `imports` field values, named/unnamed counts, name-set equality, exact call spans, digests, and the byte-exact reproduce — reproduces and independently verifies against the primary records at d9776195, and no Q01–Q13 criterion hard-fails on the substance. The grade is PARTIAL solely because entry:34/:35 assert that the unnamed edge "carries `imported_name` `null`" when the record omits the key (F1, with the printed `null` unable to show the difference), because `§A` is an undefined pointer used 15 times (F2), and because the "8 words" count is not reproducible under the corpus's precedent convention (F3). No repairs made; no admission assumed.

Material finding reported to L1 (RevengerR61-2) by message. Nothing installed (no tool install/update performed this seat).
