source: S003 — https://www.swgde.org/wp-content/uploads/2024/04/2024-03-07-SWGDE-Minimum-Requirements-for-Testing-Tools-Used-in-Digital-and-Multimedia-Forensics-18-Q-001-2.1.pdf — §§2, 4-6, Appendix A; 18-Q-001-2.1 (2024-03-07)
source: S004 — https://www.nist.gov/itl/csd/secure-systems-and-applications/computer-forensics-tool-testing-program-cftt/cftt-general-0 — "Methodology Overview" (page updated 2026-05-01)
source: S014 — `LOG.md` — round 7 and round 8 results (`:97-100`, `:105-109`) at `8bbcb4e`
verified-at: 2026-10-19
recheck: `python3` command C, `SCORECARD.md:32-43`, re-run from lane root (replay census over `corpus/verify_*.py --self-test`); confirm SWGDE 18-Q-001 current revision at https://www.swgde.org/documents (document cover advises checking for newer revisions)
coverage-map: C12

# Tool validation by function and version — C12

Falsifiable claims (each falsifiable: a single counterexample — a ledger claim missing a named field yet credited, or a version-generalized statement — defeats it).

1. A lane validation claim is well-formed only when it names the tool, its
   version, the exercised function, the input identity, the expected result,
   and the observed result. 18-Q-001 §6 lists the required documentation
   fields (purpose and scope "identify tool or technique", tester, date,
   procedure, datasets "including expected results", results and anomalies,
   identified limitations); the CFTT methodology overview structures testing
   around one tool category per specification.
2. The lane's fixture bench is the known-dataset method of 18-Q-001 Appendix
   A: "Lab created datasets can be targeted at the parameters most important
   to the functionality being tested." Each fixture's `truth.json` fixes
   expected values independently of the tool under test.
3. A validation result binds the named function in the named version, not the
   product. Round 7 (`LOG.md:97-100`) scores REA `compare_application_versions`
   in `rea-agents@6.4.0` at 0/1 on the removed `checksum` named-import claim:
   the comparison `items[]` "does not explicitly identify removed named
   `checksum` import", so the tool cannot be credited with that detection.
   Count from the saved tool output (L1 re-run 2026-10-19):
   `python3 -c "import json; it=json.load(open('corpus/live/runs/round-7/comparison.json'))['normalized_result']['items']; print(len(it), sum('checksum' in json.dumps(i) for i in it))"`
   → `15 0`: none of the 15 items names `checksum`, so explicit detection is
   0 of the 1 authored removal (fixture truth: `fixtures/js-r7-v2` drops
   `checksum` from the `index.js` import, `LOG.md:98`). The name appears only
   in the input graph's import relation, not in any comparison item.
   The round was not admitted and is preserved as bounded telemetry.
4. A function's validation outcome is a usage boundary, not a verdict on the
   tool. 18-Q-001 §4: "Testing is not necessarily pass/fail." The r7 outcome
   narrows how `compare_application_versions` output may be cited (manual
   graph difference separately labeled, `LOG.md:99`; analyst-side verifier
   scored 1/1 in r8, `LOG.md:108`); it does not invalidate the tool's other
   functions or other versions.

## Observation

- 18-Q-001-2.1 §4 General Discussion: "This document bases its testing
  baseline recommendations on the function of the tool, not on the tool
  origin" — testing scope is function- and category-oriented; §2 Scope adds
  that results "may be adopted from another competent organization".
- NIST CFTT methodology overview: "The testing methodology developed by NIST
  is functionality driven"; each category gets requirements/assertions/test
  cases, public comment, and a published report.
- 18-Q-001 §5.3.1/§5.3.2 frequency rows test a tool "[b]efore the tool is
  placed in service and after major update or revision"; the tester entry
  reads "Lab, CFTT or other 3rd party organization if the same major version".
- Lane evidence: `LOG.md:97-100` (r7, tool claim unmet, round not admitted);
  `LOG.md:107-108` (r8, `verify_js_graph_delta.py --self-test` exit 0,
  labeled analyst-side, not repair of the tool); `SCORECARD.md:32-43`
  (command C replays the saved-ledger verifiers against current fixture
  bytes); `corpus/README.md:37` (row C12 marked partial at base: only the
  pre-contract `seed.md` §Calibration strategy held this ground).

## Inference

- [INFERENCE] Mapping the lane's REA probe functions onto 18-Q-001 §5.3
  "Forensic Analysis Tools" is a judgment call: REA's `inspect_*`/`analyze_*`
  functions extract and aggregate artifact data rather than search or recover
  deleted files, so §5.3.3 "Aggregation and Summary" (with Appendix A
  known-dataset testing) is the closest category, not a stated one.
- [INFERENCE] The lane's byte-oracle fixtures satisfy the "expected results"
  documentation field of §6 better than truth copied from tool output;
  deriving expectations from authored bytes matches the known-dataset method
  (Appendix A) rather than empirical testing.

## Unknown

- Whether a CFTT or third-party report exists covering any REA function on
  PE resources; the CFTT report index (opened 2026-10-19) is organized "by
  tool category" and "by publication date" but no individual report was
  opened for this entry.
- Which SWGDE tool category a static-analysis provider (decompile/
  disassemble) belongs to; no lane probe exists for such providers, so this
  is untested, not merely unscoped.
- Whether `rea-agents` versions later than 6.4.0 change the r7 comparison
  behavior; version claims bind 6.4.0 only.

## Limitations

- SWGDE guidance is consensus best practice for forensic labs, not a binding
  standard; §3 notes it does not address processing speed, ease of use, or
  personnel training. The lane adopts it as a claim shape, not as authority.
- The r7 evidence is one fixture pair (js-r3 / js-r7-v2) and one comparison
  operation; it does not bound `compare_application_versions` on other
  language families or artifact types.
- No negative-control fixture exists yet that a validated REA function is
  *expected* to refuse (r59's predicted refusal was falsified, `LOG.md:711-716`,
  lesson M07); the falsifiability of the claims above rests on forged-record
  rejections inside the ledger verifiers, not on tool refusals.

## QUALITY check

| id | verdict | basis |
|---|---|---|
| Q01 | pass | Load-bearing claims cite tier-A rows opened this round (SWGDE 18-Q-001-2.1 full PDF; NIST CFTT methodology overview); lane records cited by path. |
| Q02 | pass | `source:` (URL + §/revision anchors), `verified-at:`, `recheck:` (command C + SWGDE revision-check citation) and `coverage-map: C12` present. |
| Q03 | pass | Expected values come from authored fixture bytes and `truth.json`, and from the tool's own saved output when scoring it; never from the claim under test. |
| Q04 | pass | r7 claim names `compare_application_versions` in `rea-agents@6.4.0` and scores its explicit `items[]` output (0/1); the manual difference is labeled manual (`LOG.md:99`). |
| Q05 | n/a | Entry asserts no readiness/capability claim; it describes validation practice only. |
| Q06 | n/a | Entry edits no fixture and states no offset/operand premises; fixtures are cited as existing records. |
| Q07 | pass | The r7 outcome is recorded as an observed falsification of a declared claim, not a predicted behavior; the falsified r59 refusal prediction is cited only as an existing recorded outcome. |
| Q08 | pass | r7 0/1 carries its command over the saved `comparison.json` (15 items, 0 naming `checksum`); r8 1/1 carries `python3 -B corpus/verify_js_graph_delta.py --self-test` → `POSITIVE saved parent graphs: removed checksum 1/1; …` then `NEGATIVE REJECTED …`, exit 0 (L1 re-run 2026-10-19) |
| Q09 | n/a | Entry makes no digest or receipt claim; that surface is C13. |
| Q10 | pass | Every claim is scoped to named function + version + fixture family; product-wide and cross-version generalization is explicitly rejected (claim 3, Unknown). |
