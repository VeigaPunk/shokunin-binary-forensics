RESULT: COMPLETE
# R62CriticJsScope — attack on intended NEW C04 scope (destructured names + source/saved spans)
Leaf critic. Frozen `a3498e25ad87bf756288812d0ea7c474b09433c7` was extracted with `git archive` to
`/fast/scratch/hyaku/revenger-r62/R62CriticJsScope/frozen` ($S below is the parent directory); every
check ran there. No JS, REA producer or verifier was run. No C04 draft existed yet (the scratch
`mut-k2/3` copies are `# stub`), so this attacks the claimed scope in `reports/round-62/claims.md:20-23`.
README C04/C09 stay `uncovered` (`corpus/README.md:33,38`). No pre-credit, no admission claimed.

## Verdict: useful narrow knowledge remains, but "name ↔ span" is a trap

Run `cd $S/frozen && python3 -B $S/proposed_c04_oracle.py` (exit 0; output in `proposed_c04_oracle.out`,
sha256 `33e26dcf…ec2dc1`):

```text
v1 saved imports imported_name=checksum ... span=(1, 6, 1, 50) slice0="{ rot13, checksum } = require('./transform')"
v1 saved imports imported_name=rot13    ... span=(1, 6, 1, 50) slice0="{ rot13, checksum } = require('./transform')"
v1 saved semantic line1 bindings={'rot13': (1, 8, 1, 13), 'checksum': (1, 15, 1, 23)} call_sites=[(1, 28, 1, 50)]
v1 saved semantic unknown family=call-flow reason=dynamic-call span=(1, 28, 1, 35) slice0='require' detail='Unresolved call target require.'
v1 saved semantic unknown family=object-flow ... span=(1, 8, 1, 13) ... 'Static destructure property /rot13 has unknown-coverage presence; its receiver is unresolved ...'
v1 saved semantic reads-property by target module={'transform.js': 2}
v1 check names_equal=True local_equals_imported=True named_spans_distinct=1 named_span_is_declarator=True unnamed_span_is_call=[True] call_site_is_call=True binding_spans_equal_source_names=True
delta names removed=['checksum'] added=[] declarator_end 50->40 call_start 28->18 shift=10
```

The v2 check line is likewise all-True, with `named_spans_distinct=1`.

1. **Shared declarator span.** Each named `imports` edge carries the whole declarator span, and both
   v1 names share one span. The application graph holds no per-name span; only semantic `binding`
   nodes do. Any claim that an edge span locates "its" name is false (Q03/Q11). The entry must name
   the layer and field it reads, and state the four granularities: declarator, call, callee, binding.
2. **Column base is a derived constant**: 1-based line, 0-based column (only `slice0` gives exact
   token boundaries). On line 1 byte offset = column, so byte versus character columns are unknown.
3. **Layer contradiction.** Edges say `resolution_status=resolved`, `confidence=high`,
   `state=inferred`; the same record's semantic layer says the call target is unresolved and property
   presence unknown, with no `reads-property` into `index.js`. Scope "resolved" to `resolved_path`.
4. **Shorthand only** (`has_colon=False has_rest=False`): `imported_name == local_name` follows from
   the fixture form. Key versus binding is unknown; do not present it as a provider finding.

## Property read vs export binding (ECMA-262 "Draft ECMA-262 / October 16, 2026", opened 2026-10-21T18:01Z)

- statements-and-declarations (sha256 `a23fc93c…5fc8813e`): §14.3.3.1 `SingleNameBinding`: "Perform
  ? KeyedBindingInitialization … with arguments value, envRecord, and name."; §14.3.3.3: "Set value
  to ? GetV(value, propertyName)."
- scripts-and-modules (sha256 `a5444406…66b136d4`): "An ImportEntry Record is a Record that digests
  information about a single declarative import."; "[[ImportName]] … The name under which the
  desired binding is exported by the module identified by [[ModuleRequest]]."; "ModuleItem :
  ImportDeclaration ExportDeclaration StatementListItem".
- Oracle token counts, both `index.js`: `import_tokens=0 require_tokens=1`.

How to classify each point (full text in `$S/proposed_c04_inference_unknown.md`):

- **Inference:** each name is a `GetV` property read on the call result; no ImportEntry exists; the
  saved `imported_name`/`local_name` reuse ECMA vocabulary but are provider fields, not exports.
- **Unknown:** what the call returns and its own properties (the record says "unknown-coverage");
  any tie to `transform.js` exports or `exposes`; aliased, nested, rest, computed or default forms.
- **Cut:** drop old Node S020/S021/S023 inferences and `electron-main`/entrypoint text (out of frozen
  scope; the rejected entry is not citable). S029 and S030 suffice.

## Q13 bound (red-before)

Copied tree (removed afterwards), forged checksum edge span start 6→15, `imported_name`
rot13→rot14, checksum binding start 15→14: `v1 check names_equal=False local_equals_imported=False
named_spans_distinct=2 named_span_is_declarator=False ... binding_spans_equal_source_names=False`;
frozen copy stays all-True. Credit only those three clauses; state, confidence, unknown details
and delta are unguarded and must be named so.

## Impacted axes and smallest safe correction

Axes: coverage (C1) is admissible only if items 1–4 are adopted; calibration (blocks the "resolved"
overclaim); depth (span granularities are new narrow knowledge). Other rows are unharmed; no
corpus/live or corpus/fixtures byte was touched.

Correction: put `proposed_c04_oracle.py` (sha256 `0e83b226…87d95cc8`), or an equivalent block, in the
entry with its printed output. Adopt the wording in `proposed_c04_inference_unknown.md`. Label the
provider version and 2026-10-12 run context as recorded. The entry writer must re-open ECMA-262
independently. A peer note was delivered to `RevengerR61-2.R62JsEntry`.

Scratch: `$S/{proposed_c04_oracle.py,.out,proposed_c04_inference_unknown.md,probe_*.py,*.html}`.

Installs: none.
