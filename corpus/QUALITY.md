# QUALITY — revenger's admission bar

What a `corpus/knowledge/` entry must show before it is admitted. Each criterion
cites the mistake class that produced it (`corpus/lessons/round-1.md`
`## Mistakes — kaika continuation`). Criteria are superseded by new rows that
name the row they replace, never rewritten (`LEARNING.md` §Files the path
writes). Source tiers are defined in `corpus/SOURCES.md` and are not restated here.

## Criteria

| id | criterion | reject when | lesson |
|---|---|---|---|
| Q01 | Each load-bearing claim rests on a `corpus/SOURCES.md` row that is tier A **for that claim's scope** and was opened in the round that wrote it. A tier-C row is never sole support. | the claim exceeds what the cited text states (for example a catalog abstract cited for clause-level requirements) | M17 |
| Q02 | The entry opens with `source:` (its `S###` row, URL or path, exact anchor), `verified-at:` (date or commit) and `recheck:` (the command or citation that re-verifies it), and names the coverage-map row it fills (`corpus/README.md`). | any header is missing or the anchor is a bare homepage | M18 |
| Q03 | Expected values are derived independently: from bytes, a specification, or a pin fixed outside the record under test. | the expected value is copied from the record being checked, or a saved path is used as both identity and locator | M06, M14 |
| Q04 | A tool claim names the tool, version and function exercised, and scores the tool's own explicit output. Manual analysis is labeled as manual. | a tool is credited with a result it did not output, or one version/function is generalized to the product | M02 |
| Q05 | A readiness or capability claim carries a probe against the real surface: its command, date and observed exit, output or Evidence ID. Presence, configuration or acquisition is not capability. | the claim rests on a configured value, an install, or an unrechecked older probe | M01, M19 |
| Q06 | Fixture premises are byte-verified against the built fixture after every edit and before any producer call; failed inputs are retained. | an offset, operand, size or count is stated from intent rather than from the built bytes | M04, M05 |
| Q07 | A predicted parser behavior (accept, refuse, cause) is a pre-registered hypothesis with spec-derived ground truth and is recorded whichever way it falls. A cause is stated only once independently reproduced. | a prediction is written as fact, or an unreproduced cause is used as support | M07, M12 |
| Q08 | Every count, identifier and offset role is re-derived by command from its source record; a non-author byte-derived value supersedes author prose. | a count lacks its command, or an identifier or role label comes from memory | M08, M09, M10 |
| Q09 | A digest or receipt is claimed only for the exact bytes it hashed. It does not establish producer origin, acquisition completeness or authenticity. Saved records stay byte-preserved. | a hash match is offered as proof of origin, completeness or a valid interpretation | M11, M13 |
| Q10 | A finding is scoped to the observed family, operation, version and input. Cross-lane contested scope is reported, not absorbed. | one family's observation is stated as a universal | M15 |

## Admission procedure

1. Apply every criterion. A criterion marked `n/a` names why it cannot apply.
2. Admit only when no criterion fails. Record the decision in the round lesson's
   `## Gate` with the criteria checked; a reject names the failing `Q` id.
3. Each entry separates observation, inference and unknown, and names at least
   one limitation (`PROVINCE.md:5-7`).

## Signals of weak material

- Catalog pages, abstracts and landing pages: primary only for what they state.
- A single tool-test report: scoped to that tool version, function and data set.
- Vendor or community write-ups without reproducible detail: leads (tier C).
- Older guidance used as current procedure without a revision check.
