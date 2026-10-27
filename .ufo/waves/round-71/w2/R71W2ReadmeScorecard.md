PENDING — C1 is not adjudicated at this tree: C05 remains `uncovered`, the v6 entry remains `candidate`, and the committed W2 vote directory is absent.

## Independent README coverage derivation

Command: `grep -n '^| *C[0-9][0-9]' corpus/README.md`
Output: 14 rows, C01–C14. Held rows with extant knowledge paths: C01, C04, C06, C07, C09, C11, C12, C13 = **K_HELD_BACKED 8/14**. Other statuses: C02/C10/C14 partial; C03/C08 frontier; C05 uncovered. This applies the counter's rule (`reports/round-71/measure.py:25-32`): count held rows only when each knowledge-column path resolves to a file.

Command: `git diff b7abcd875c84f4e1d6c8df966b6bd20f4154c53f..HEAD -- corpus/README.md`
Output: only the corpus README lessons-directory inventory line and C05 row differ. C05 remains `uncovered`; its knowledge column is `—`; the v6 candidate path appears only in the evidence column. No coverage status has been flipped. The sole coverage-map row changed is C05 (the other README edit is inventory wording).

Command: `git diff 4c1eeaee88fd07e442f1bd546faf77be3957d390..HEAD -- corpus/README.md` and `git ls-tree -r --name-only HEAD -- .ufo/waves/round-71/w2-votes/`
Output: README diff is empty; no committed `w2-votes/` files at HEAD. The checked-out candidate file `corpus/knowledge/round-71-apk-axml-byte-evidence.md` says `admission-status: candidate` and explicitly says votes pending. Thus no premature admission/flip is present. The required exact knowledge-column value on admission is `knowledge/round-71-apk-axml-byte-evidence.md` (counter constant `V6` at `measure.py:10`); it is not yet in that column.

## Counter / SCORECARD evidence

`reports/round-71/measure.py` SHA-256 is `718daa96f34fa5c3435acdf031e2fe5099238e9092c36b845cb9258990fcca61` in both the worktree and HEAD. The counter reads votes from the measured TREE (`measure.py:56-70`), and C1 requires nine backed/strict rows, C05 held, exactly the v6 knowledge path, admitted entry, gate/lint success and 16 valid votes (`:79-101`). No vote directory is in HEAD, so the scorecard cannot yet claim final C1 results. The existing `SCORECARD.md` ends with round 70; there is no round-71 row/evidence line to validate yet.

**Draft only, if all frozen C1 conditions pass:**

`| coverage — knowledge-map ground K (C05 sixth pass) | K_HELD_BACKED 8/14 → 9/14 (5.7 → 6.4); C05 uncovered → held | python3 -B reports/round-71/measure.py <committed git-archive TREE including .ufo/waves/round-71/w2-votes/> (K_HELD_BACKED, K_HELD_BACKED_STRICT, C05_STATUS, C05_KNOWLEDGE_COLUMN, V6_ADMITTED_MARKED, C1_GATE, C1_LINT, C1_W2_Q_VOTES, HOLDS_C1_V6) | <frozen base> → <final measured commit> | C1 met only after all 16 Q votes pass/n-a and L1's adjudication revision |`

Do not publish that admission row until L1 has the committed vote files, an actual final-counter receipt at SHA `718daa96…`, and its adjudication revision. If any Q fails, use the frozen honest-stop wording and preserve C05 uncovered; do not use the draft admission line.

## Evidence commands / outputs

- `git rev-parse HEAD` → `c6e284c6583fa3502754361f411b66646880ba02` (freeze/fresh-wave tip; distinct from candidate `4c1eeaee88fd07e442f1bd546faf77be3957d390`).
- `sha256sum reports/round-71/measure.py` → `718daa96f34fa5c3435acdf031e2fe5099238e9092c36b845cb9258990fcca61`.
- `grep -n '^| *C[0-9][0-9]' corpus/README.md` → exactly 14 coverage rows; statuses as enumerated above.
- `head -40 corpus/knowledge/round-71-apk-axml-byte-evidence.md` → candidate header, C05 coverage-map declaration, and pending W2 decisions.

Report: `.ufo/waves/round-71/w2/R71W2ReadmeScorecard.md`
