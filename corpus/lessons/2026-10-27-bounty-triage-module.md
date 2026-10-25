# 2026-10-27 — bounty-triage training module (interactive dispatch, not a steered round)

This is a dated lane lesson for an interactive dispatch, not a round entry: no round number
is claimed, no coverage row moves, and no claim is declared. Precedent for the naming:
`2026-10-12-r1-provider-gap.md`.

Demand: train the lane on authorized bounty-hunting triage using the public Claude-Red
library and the linked guide/corpus. Delivered as one instruction module
(`corpus/training/bounty-triage/MODULE.md`), one exercise validator, two offline packages,
and index/registry updates. `PROVINCE.md` is narrowed, not widened: the module's first gate
is written scope, and every live/dynamic method is refused.

## Gate

### Source rows opened this dispatch

Access date: **2026-10-27**. Both documents were fetched to byte-preserved snapshots in
`corpus/snapshots/`; the live URL and the snapshot digest are both in the row.

- **S050 (new).** https://raw.githubusercontent.com/SnailSploit/Claude-Red/main/SECURITY.md
  → `corpus/snapshots/claude-red-security.md`, 3182 bytes, sha256
  `b153d16ad517bb30087103c5a920760b927d5ace2b0bcaa4d6802b5824814131`.
  Located quotes: `## Intended Use` (heading line 5) bullet line 10 — "Bug bounty
  programs with explicit written permission for the techniques described" (11 words);
  `## Reporting a Vulnerability Found Using This Library` (heading line 31) sentence
  line 40 — "Allow at least 90 days before public disclosure unless the
  vulnerability is being actively exploited" (15 words).
  Tier A **only for this row's scope** (the repository's own stated intended use and
  disclosure policy — a maintainer statement), not for any offensive method.
- **S051 (new).** https://raw.githubusercontent.com/SnailSploit/Claude-Red/main/Skills/utility/offensive-reporting/SKILL.md
  → `corpus/snapshots/claude-red-offensive-reporting.md`, 14720 bytes, sha256
  `b9a8bf71828399c75c6c877e0768e4f916adbea352010e2fed06e57f06786200`.
  Located quotes: intro line 8 — "A great finding lost in a bad report is a wasted
  finding." (12 words); "Treat the report with the same rigor as the exploit." (10
  words); section headings `## Quick Workflow` line 10 and `## Report Structure
  (Standard)` line 20.
  Tier C (curated community methodology): corroboration only; no load-bearing claim rests
  on it. The module's report rules rest on this lane's own Q01–Q16 and the exercise
  validator, not on S051.

### Attempted but unopened

- `https://x.com/sammy_capital/status/2113733817596834151?s=20` — the fetch failed with
  `x-unavailable` (the provider refused the endpoint). No bytes were read, so **no registry
  row is opened** (the registry's own rule: every row was opened on its `opened` date) and
  no claim cites the thread. It stays an unopened lead; a retry needs a channel that can
  return the page.
- The Claude-Red README index and the `offensive-fast-checking` skill were read while
  screening but not registered: the index states category counts only, and the fast-checking
  checklist is procedure this module deliberately does not import. The SECURITY.md row and
  the reporting row cover the only two things used (intended-use boundary, report quality).

### Registry changes (append-only fields, old → new)

| row | field | old | new | reason |
|---|---|---|---|---|
| S050 | (new row) | — | `mined`, opened `2026-10-27`, `180d`, used-by `corpus/training/bounty-triage/MODULE.md` | maintainer statement of authorized use and disclosure window |
| S051 | (new row) | — | `mined`, opened `2026-10-27`, `on-release`, used-by `corpus/training/bounty-triage/MODULE.md` | corroborating report-structure discipline; tier C, never sole support |
| S001–S049 | — | unchanged | unchanged | no in-place edit was needed |

Census before → after (same seven commands as `SKILL.md` §6.2, run from the lane root;
the before count is the round-70 gate record, the after count was measured this dispatch):

```
before: rows 49 (round-70 gate)
after:  rows 51 (measured)
malformed 0; duplicates none; enum violations none; missing used-by paths none; tier A=48 C=3
```

## Authored

- `corpus/training/bounty-triage/MODULE.md` — five-stage module: written-scope gate,
  artifact-first triage, evidence preservation, nine-section report quality, stop/escalation
  matrix. Decision tables, required fields, and the validator code map are inline.
- `corpus/training/bounty-triage/check_package.py` — package validator. Exit codes 0/1/2/64;
  `--self-test` builds synthetic packages and asserts each of 26 detectors fires on a case
  built for it, plus a clean control; `--json` for machine use. **Not an admission gate** and
  not registered in the SKILL gate registry: it checks structure and binding, not truth.
- `corpus/training/bounty-triage/fixtures/build_exercise.py` — deterministic builder
  (ZIP_STORED, fixed timestamps, sorted members) with `--verify` binding both packages to
  one digest. `truth.json` records artifact and member digests.
- `fixtures/exercise-r1/package/` — clean package (scope, ledger, report, artifact).
- `fixtures/exercise-r1-defective/package/` — same bytes with four planted defects
  (expired scope, unevidenced impact line, overclaim, missing stop decision).

## Smoke run (offline exercise, run this dispatch)

```
$ python3 -B corpus/training/bounty-triage/fixtures/build_exercise.py --verify
verified: 2 packages bind 3fb10d3f474914e2a1f1b5c097572b5dedc90939e9373a37b2a95e4f930af2b3
$ python3 -B corpus/training/bounty-triage/check_package.py --self-test
self-test: 26/26 detectors fired as expected
self-test: clean package PASS
VERDICT=PASS
$ python3 -B corpus/training/bounty-triage/check_package.py \
    --package corpus/training/bounty-triage/fixtures/exercise-r1/package --as-of 2026-10-27
package: /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/training/bounty-triage/fixtures/exercise-r1/package
as-of: 2026-10-27
artifacts: 1 digest-bound
ledger: 5 rows (observation=3 inference=1 unknown=1)
report: 9/9 sections
findings: 0
VERDICT=PASS
$ python3 -B corpus/training/bounty-triage/check_package.py \
    --package corpus/training/bounty-triage/fixtures/exercise-r1-defective/package --as-of 2026-10-27
package: /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/training/bounty-triage/fixtures/exercise-r1-defective/package
as-of: 2026-10-27
artifacts: 1 digest-bound
ledger: 5 rows (observation=3 inference=1 unknown=1)
report: 9/9 sections
findings: 4
  B05 scope expired 2026-10-01 before as-of 2026-10-27
  R04 Impact line lacks evidence/unknown: 'The telemetry endpoint accepts unauthenticated writes from any client.'
  R05 overclaim phrase present: 'full compromise'
  R08 Stop conditions section records no decision ('none triggered' or 'STOP:')
VERDICT=FAIL
```

Exit codes observed: builder 0, self-test 0, clean 0, defective 1.

## Mistakes

| class | evidence | captured-by | fix |
|---|---|---|---|
| M54 — instrument declared before its control ran | the first `--self-test` draft crashed partway through a synthetic case (`ValueError: too many values to unpack`) because one mutation returned a 4-tuple; the run aborted before printing a single detector result, while both exercise packages already printed PASS/FAIL | running `--self-test` immediately after the two exercise runs | the mutation was reduced to a 3-tuple; the self-test now runs before the exercise is cited, and the module's §6 lists it first |
| M55 — a detector can pass for the wrong reason | the defective package's overclaim line also cited `E4`, so `R04` fired only on the *unevidenced* line; a learner could read "R04 present" as "the overclaim was caught" | reading the four findings by code against the planted defects | recorded here: each expected code is named in the exercise, and the lesson states exactly which line produced R04 |
| M56 — located-quote pointer from draft (M40 recurrence) | S051's first anchor said `"Quick Workflow" line 8`; line 8 is the intro sentence and the heading is line 10, while S050's anchor conflated heading and quoted-bullet lines | re-reading both snapshots with `grep -n '^#'` and `sed -n '5,13p'` before leaving the quotes in place | both anchors now name the heading line and the quote line separately: S050 heading 5 / quote 10 and heading 31 / quote 40; S051 intro 8, headings 10 and 20 |
| M57 — set-coverage claim from draft (Q16 class) | the first self-test covered 19 codes while the module and this lesson said it fired "every detector"; B01, B09, L01, L02, L04, L06 and R02 had no case | enumerating the module's code map against the self-test case list before restating the claim | seven cases added; the self-test now reports 26/26, and the sentence was made true by adding coverage, not by weakening it |

All four are authoring mistakes, not domain claims; none is used as support for a knowledge
entry.

## Limits and routed notes

- The module is instruction. It does not move any coverage row, is not an admitted knowledge
  entry, and does not appear in the coverage map; `corpus/README.md` lists it under Index.
- No REA producer was run for this exercise: the artifact is an authored ZIP and the
  observations are stdlib reads. The module says how an REA route enters (stage 2, step 4,
  Q04) but claims no provider behavior.
- `check_package.py` cannot tell whether a scope is genuine, whether a statement is true, or
  whether a report is publishable; §6 of the module states this. Its rules are structural.
- The X thread remains unopened (see above). If a later dispatch reads it, that is a new
  source row, not a retroactive one.
- Tool installs: none. No build/lint/test gate was run; only the authored module's smoke
  commands above.
