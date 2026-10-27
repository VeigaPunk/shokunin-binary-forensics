**Verdict: `CONFORMANT-WITH-LOCATED-GAPS` — the lesson's structural shape, new-row Gate records, quarantine re-derivation and wave-1 seat numbers all re-derive from committed bytes, but nine located defects remain: four false quote word-counts, both `## Mistakes` rows use classes outside the frozen §5 vocabulary (M58 also lacks a criterion/rule `captured-by`), the proposal-1 ledger covers 11 of 14 proposable items and three of its "no adoption" cells carry no sweep, the provenance header names a superseded pre-repair commit, and the C1/C2 wave-2 adjudication, per-Q outcome table, candidate record and spot-check result are absent.**

# R71W2LessonReview — CORPUS conformance review of `corpus/lessons/round-71.md`

- Reviewed revision: lane HEAD `a16e6cb` (`corpus/lessons/round-71.md` sha256 `38f06c0323c51bf8be6f6a507131d6985eab73cd05ac25bb970f858b93c4fc86`; `corpus/SOURCES.md` sha256 `dc2e5b22d648587b3dbaf797aaabcec65792ac0655736b196e28726dc0a5ed99`). Entry under discussion `corpus/knowledge/round-71-apk-axml-byte-evidence.md`, 324 lines, sha256 `671f55fceb64af27f99c00106f58f9bc2c8b5dc9af6028382ff218655008f092`.
- Frozen inputs read: `reports/round-71/claims.md`, `pre-registration.txt`, `measure-amendment-A1.md`, `measure-amendment-A2.md`, `.ufo/waves/round-71/w1-attack-inventory.md`, fleet `CORPUS.md`, `LEARNING.md`, `.ufo/waves/kaika-w1/mistakes.md` §5.
- Read-only: no lane source, corpus, report or register edit was made by this seat. No packages installed, no `pacman`, no route/config change. No Q or C1/C2 verdict is asserted here; scoring belongs to the four Q reviewer seats and L1.
- Scratch `/fast/scratch/hyaku/revenger-r71/R71W2LessonReview/` created, used for one stdout capture, and deleted before return.

## Axes

1. **Contract conformance** — does the lesson satisfy `CORPUS.md` (row rule 1/2/5, `## Gate` layout, `## Mistakes` schema and §5 class vocabulary, "a count carries its command", "a negative claim carries its sweep", "a fix is shown able to fail") and `LEARNING.md` (spot-check result in the round lesson)?
2. **Artifact fidelity** — does every lesson claim re-derive from the committed commands, logs and registry bytes at the reviewed revision?
3. **Closure completeness** — are the round's decision surfaces present: C1 Q01–Q16 outcomes, C2 exit-2 legs, candidate/admitted/rejected record, wave-2 record, frontier/assimilation status?

## Receipts (commands run from the lane root unless stated)

```
$ git rev-parse HEAD                                  -> a16e6cb
$ git log --oneline -6
  a16e6cb round-71: curate sources and record frontier mistakes
  c6e284c round-71: freeze fresh falsification wave
  4c1eeae round-71: integrate W1 repairs and harden frozen counter
  620849e round-71: integrate W1 repairs, sources and controls
  da4f1ee round-71: correct timeout probe fixture path
  18200a4 round-71: build v6 candidate and gate exit-2 cases

$ git diff --numstat b7abcd8..HEAD -- corpus/SOURCES.md          -> 4  0
$ git diff b7abcd8..HEAD -- corpus/SOURCES.md | grep -E '^[+-]\| S'
  + S052   + S053                                                 (no '-' row line)
$ git show b7abcd8:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'   -> 51
$ grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md                      -> 53
$ git show b7abcd8:corpus/SOURCES.md | grep -c "C05 authored APK"                            -> 0
$ grep -c "C05 authored APK" corpus/SOURCES.md                                               -> 1
$ git show b7abcd8:corpus/SOURCES.md | grep -cE '^- 2026-'                                   -> 17
$ grep -cE '^- 2026-' corpus/SOURCES.md                                                      -> 18

$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes
  6 × MATCH lines, exit 0; includes
  MATCH dex-format.html: first line 5035, folded phrase present=True: uint ENDIAN_CONSTANT = 0x12345678;
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout | wc -l                   -> 20
  lines 16-18 MATCH APPNOTE 4.3.7/4.3.12/4.3.16; 19 central.fixed_part 46; 20 local.fixed_part 30

$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md
  checked_blocks=24 problems=0   (exit 0)
$ python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md | tail -4
  LINT_QMAP=0 / LINT_Q14=0 / LINT_Q15=0 / LINT_HEADER=0   (exit 0)
  (QUALITY.md exposes 16 Q rows: Q01..Q16 — `grep -cE '^\|[[:space:]]*Q[0-9]{2}' corpus/QUALITY.md` -> 16)

$ python3 (fenced-block compare, round-70 vs round-71 entries)
  r70 blocks 18 / r71 blocks 18 / identical pairs 18 of 18

$ python3 -c "import json,collections;w=json.load(open('.ufo/waves/round-71/w1-results.json'));print(w['seats'],len(w['results']),collections.Counter(r['agent'] for r in w['results']))"
  40 40 Counter({'reviewer': 9, 'executor': 7, 'scout': 7, 'scribe': 5, 'critic': 4,
  'mutation-tester': 3, 'connector': 2, 'sentinel': 1, 'revenger': 1, 'simplifier': 1})
  attacker roles 9+4+3+1+1 = 18  (matches "18/40"); no empty seat outputs (0 dead)
$ python3 -c "...len(json.load(open('.ufo/waves/round-71/w2-spec.json'))['items'])"          -> 34

$ grep -c 'HOLD ' reports/round-70/measure-after.log                                        -> 0
$ grep -c 'HOLD ' reports/round-71/measure-before.log                                       -> 10
   rows at :33-:42; :43 is HOLD_REPLAY=10/10
$ sed -n '24,26p;91,92p' corpus/lessons/round-70-verifier-spotcheck.md
  confirms the ten missing HOLD rows and routed defect #1 ("print them in the next receipt")
$ sed -n '5,7p' .ufo/waves/round-71/w1/R71W1Quarantine.md
  confirms the searched path /home/vgpnk/Projects/shokuknow/lanes/revenger and the un-run query

$ awk -F'|' -v l='revenger' '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {print $4, $5}' \
    /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md | wc -l   -> 26
  same query with `{print $3}` histogram: round1=9 round2=4 round3=9 round4=4   (all r1-r4)

$ python3 (word counts of the exact quoted strings, split())
  S052 "MATCH dex-format.html: … uint ENDIAN_CONSTANT = 0x12345678;"  -> 12 (lesson: 12) OK
  S053 "This module provides tools to create, read, write, append, and list a ZIP file." -> 14 (lesson: 14) OK
  S048 checksum "adler32 checksum of the rest of the file (everything but magic and this field)" -> 14 (lesson: 18) DRIFT
  S048 header_size "must be 0x70 (112) bytes (v40 or earlier)" -> 8 (lesson: 12) DRIFT
  S032 "end of central dir signature 4 bytes (0x06054b50)" -> 8 (lesson: 13) DRIFT
  S049 "Start with inspect_android_package on the caller's APK path … inline Evidence." -> 17 (lesson: 20) DRIFT

$ ls .ufo/waves/round-71/w2-votes/   -> No such file or directory (at review time)
$ ls .ufo/waves/round-71/w2/         -> swarm-registry.json only
```

## Findings (located defects)

**D1 — number-drift in four Gate quote word-counts (`round-71.md:15,16,17`).** Measured counts are 14/8 (S048), 8 (S032), 17 (S049); the lesson prints 18/12, 13, 20. Every count remains under the ≤25-word cap, so no rule-1 limit is broken; the numbers themselves are false. The same wrong counts are inherited verbatim from `.ufo/waves/round-71/w1/R71W1OpenS048.md`, `R71W1OpenS032.md`, `R71W1OpenS049.md`, so the lesson is faithful to its seats but not to the text.
Draft replacement (S048): "Located quote (14 words) … `(8 words)`"; (S032): "Located quote at §4.3.16 line 634 (8 words)"; (S049): "Located route quote at line 7 (17 words)".

**D2 — `## Mistakes` classes outside the frozen vocabulary (`round-71.md:37,38`).** `CORPUS.md` ("Rules added from the kaika campaign") requires classes from `mistakes.md` §5: `vacuous · survivor · stale-premise · reference-drift · number-drift · scope · attribution · landing · provider`. The cells read `measurement-receipt omission` and `recon path omission`, which are sub-descriptions, not vocabulary tokens.
Draft: keep the token first — `scope (measurement-receipt omission: an aggregate replay label hides per-verifier outcomes)` and `reference-drift (recon path omission: the seat searched an unprovided, incorrect lane subdirectory …)`.

**D3 — M58 `captured-by` is neither a `QUALITY.md` criterion nor a protocol rule (`round-71.md:37`).** The cell reads "prior non-author spot-check's routed defect #1". The schema allows a criterion, a protocol rule, or `none`.
Draft: `none — no QUALITY.md criterion required per-verifier receipt rows; routed by the round-70 spot-check as defect #1 (`corpus/lessons/round-70-verifier-spotcheck.md:91`)`.

**D4 — M59 fix has no red-before for the fix itself.** M58's fix is demonstrated (r70 receipt `grep -c 'HOLD ' reports/round-70/measure-after.log` → 0 vs r71 → 10, so it "is shown able to fail"). M59's fix ("include the exact absolute register path and command") has a red-before only for the seat's *search*, not for the register query: `R71W1Quarantine.md:5-7` never ran that query, so no state exists where the same command exits non-clean for the named reason.
Draft red-before to commit: run the lesson's `awk` against the unprovided path — `awk … /home/vgpnk/Projects/shokuknow/lanes/revenger/absent-defect-register.md` → no such file (one row, 0 data), then against the contract path → 26 rows; cite both in the fix cell.

**D5 — proposal-1 ledger incomplete (`round-71.md:45-59`).** The ledger's own mandate (2026-10-26 #1) is "every considerthese proposal"; it carries 11 rows against 14 proposals in the three in-scope files (5 + 5 + 4). Missing: **2026-10-24 #4 undispatched-wave backlog**, **2026-10-24 #5 burst-aware reporting**, **2026-10-25 #3 "Did the instrument run" line**. Verified absent: `grep -n "undispatched\|burst-aware\|Did the instrument run\|instrument run" corpus/lessons/round-71.md corpus/lessons/round-70.md` → no output (2026-10-27).
Draft rows:

```
| 2026-10-24 #4 undispatched-wave backlog | No observed adoption | sweep 2026-10-27: `grep -n "undispatched\|backlog" corpus/lessons/round-70.md corpus/lessons/round-71.md` → no match | — |
| 2026-10-24 #5 burst-aware reporting | No observed adoption | sweep 2026-10-27: `grep -ni "burst" corpus/lessons/round-70.md corpus/lessons/round-71.md` → no match | — |
| 2026-10-25 #3 "Did the instrument run" line | No observed adoption | sweep 2026-10-27: `grep -rni "instrument run" corpus/lessons/round-70.md corpus/lessons/round-71.md` → no match | — |
```

**D6 — three existing "No observed adoption" cells are negative claims with no sweep.** `CORPUS.md`: "A negative claim carries its sweep … need the search command that produced the absence." Affected: 2026-10-24 #1, 2026-10-24 #2, 2026-10-25 #5.
Draft evidence text (each already run by this seat, 2026-10-27):
- #1: `grep -rniE 'ascii|hex.*decode' corpus/lint_entry.py` → only the two self-test fixture strings (`:118`, `:149`); no entry-wide hex→ASCII checker. (`grep -rniE 'hex.*ascii|ascii.*hex' corpus/lint_entry.py` → no match.)
- #2: `grep -rniE 'refusal|provider-refus' corpus/lessons/round-70.md LOG.md` → no per-round refusal-line field; LOG hits are route/history prose.
- 2026-10-25 #5: `grep -rli "cross-pass\|disagreement ledger" corpus/lessons/` → `round-69.md`, `round-69-verifier-spotcheck.md`, `round-71.md` (this proposal's own text) only; no ledger file.

**D7 — provenance header names a superseded pre-repair build (`round-71.md:3`).** The lesson says "current pre-gate build `18200a4…`", but the entry was rewritten at `620849e` (entry sha256 `778af93…` → `671f55f…`, 14 changed lines) — the very repairs the Gate then describes at `:25` (item 5, Observation, Q16, Q14, Q08/Q12). Verified: `git diff --stat 18200a4..HEAD -- corpus/knowledge/round-71-apk-axml-byte-evidence.md` → 1 file, 14 insertions, 14 deletions; `git diff --stat 4c1eeae..HEAD -- <entry>` → empty. The frozen final candidate per the assignment is `4c1eeae`; the lesson never names it.
Draft: `author: RevengerR71 · base `b7abcd8…` · frozen claims `reports/round-71/claims.md` · final candidate `4c1eeae…` (entry 324 lines, sha256 `671f55f…`; lane HEAD `a16e6cb`) · no package installation.`

**D8 — no C1 wave-2 Q outcome record; seven Qs are unmentioned.** `grep -oE 'Q[0-9]{2}' corpus/lessons/round-71.md` → Q01, Q04(1), Q08, Q11(2), Q12, Q13(2), Q14(2), Q15, Q16(5); no Q02, Q03, Q05, Q06, Q07, Q09, Q10 and no per-Q table. At review time `.ufo/waves/round-71/w2-votes/` does not exist, so no wave-2 decision could honestly be recorded — the gap is the missing section, not a missing verdict. Wave-1 seat outputs exist for Q01/Q02, Q03/Q06, Q04, Q05/Q09/Q10, Q11b, Q13/Q16 and Q14/Q15 (`w1-results.json`), and the Gate cites only some of them.
Draft section (no outcome asserted; bind to the frozen predicate at `claims.md:11-13`):

```
### Wave-2 C1 adjudication (Q01–Q16 on the final candidate)
Final candidate `corpus/knowledge/round-71-apk-axml-byte-evidence.md` at `<commit>`, sha256 `<sha>`.
| Q | vote file `.ufo/waves/round-71/w2-votes/…` | decision | seat report |
| Q01 | R71W2Q01Q04.json | <PASS|n/a|FAIL> | .ufo/waves/round-71/w2/R71W2Q01Q04.md |
| Q02 | R71W2Q01Q04.json | … | … |
| Q05 | R71W2Q05Q08.json | … | … |      (Q05–Q08)
| Q09 | R71W2Q09Q12.json | … | … |      (Q09–Q12)
| Q13 | R71W2Q13Q16.json | … | … |      (Q13–Q16)
Counter `reports/round-71/measure.py` (sha256 `718daa96…`, amendment A2): C1_W2_Q_VOTES=<n>/16, C1_GATE=<n>/0 problems, C1_LINT=0/0/0/0, HOLDS_C1_V6=<yes|no>.
All PASS/n-a → one adjudication revision: v6 header `admitted`, C05 → held with `knowledge/round-71-apk-axml-byte-evidence.md`, SCORECARD row `K_HELD_BACKED 8/14 → 9/14`. Any FAIL with a located defect → README stays uncovered, only the v6 `admission-status` line rejected, C1 falsified/honest stop (`claims.md:13`).
```

**D9 — C2 has no record anywhere in the lesson.** No mention of the exit-2 predicate, the A1 fixture-path correction, the A2 archive/vote-parser hardening, the red-before legs (`controls/C2-missing-before.log`, `C2-timeout-before.log`) or controls E/F. This is a frozen claim of the round and needs its own adjudication record.
Draft section:

```
### Wave-2 C2 adjudication (registered gate exit-2 legs)
| leg | command | observed | predicate |
| missing entry | `python3 -B corpus/check_embedded_outputs.py --entry <nonexistent>` | exit <n>, text `<…>`, traceback <yes|no> | exit 2, `could-not-evaluate: entry not found:`, no traceback |
| 120s timeout | `<valid entry whose declared command runs corpus/sleeper_r71.py>` | exit <n>, text `<…>`, traceback <yes|no> | exit 2, `could-not-evaluate: command timed out after 120s:`, no traceback |
| self-test | `python3 -B corpus/check_embedded_outputs.py --self-test` | exit <n> | exit 0, both hermetic cases |
Counter labels C2_MISSING_ENTRY_EXIT2=<n>/1, C2_TIMEOUT_EXIT2=<n>/1, HOLDS_C2_V1=<yes|no>. Amendment A1 changed only the sleeper path (`fbd81050…`); A2 moved vote reads into the measured TREE and rejects duplicate keys / non-object roots (`718daa96…`); neither moved a target. Controls E/F as pre-registered (`claims.md:27`). SKILL.md row names both mappings.
```

## Missing sections required by `CORPUS.md`/`LEARNING.md` (drafts only, nothing edited)

**M1 — candidate / admitted / rejected record (`## Gate` layout).** The Gate has source-row admits/rejects and a C05 pre-gate note, but no explicit knowledge-entry record. Draft:

```
### Candidate record
- Candidate: `corpus/knowledge/round-71-apk-axml-byte-evidence.md` — `admission-status: candidate`; README C05 unflipped; wave-2 Q01–Q16 pending (claims.md:13).
- Admitted: none yet this round.
- Rejected: none this round; the round-70 predecessor `corpus/knowledge/round-70-apk-axml-byte-evidence.md` stays byte-preserved and unmarked.
```

**M2 — spot-check result (`LEARNING.md`: at least one admit and one reject, `agree`/`disagree` with reason).** `round-71.md:29-31` records only "pending"; no non-author verdict text exists. Draft shell to be filled by the non-author closure:

```
### Spot-check result (non-author)
Sample: S052 (admit) and S053 (reject). Reviewer `<seat>`; `<agree|disagree>`; reason: `<…>`; pointer `<report path>`. No self-attestation counted.
```

**M3 — wave-2 record (parallel to `## Wave-1 record`).** Missing entirely. Draft:

```
## Wave-2 record
Validated v1 wave 2: 34 seats, <n> dead. Roles: <histogram>. Attacks: <n>/34. Votes bind at `.ufo/waves/round-71/w2-votes/<seat>.json` (4 files, 16 Q). W2 results: `.ufo/waves/round-71/w2-results.json`. No tools installed or updated.
```

**M4 — counts without their command (`CORPUS.md`: `<number> — <command> <date>`).** Present numbers whose command is only in a seat report or receipt file: `24/24` embedded blocks (`:23`; add `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md` → `checked_blocks=24 problems=0`, 2026-10-27), `51`/`53` rows (`:19`; add the frozen `grep -cE` command), `40 seats`, role histogram and `18/40` (`:63`; add the `w1-results.json` one-liner above), `ten HOLD rows` (`:37`; add `grep -c 'HOLD ' reports/round-71/measure-before.log` → 10; the rows are `:33-:42`), `174585 bytes` / `1992 bytes` (`:16,17`; add the `sha256sum`/`wc -c` pair from the seat reports). The `26` quarantine rows already carry their command in `M59`, so that one conforms.

**M5 — M58 pointer precision.** `reports/round-71/measure-before.log:33-43` spans the ten HOLD rows (`:33-:42`) plus `HOLD_REPLAY=10/10` (`:43`). Acceptable as written, but `:33-42` is the exact evidence range.

**M6 — SOURCES additions not logged.** The round added one `## Paths` line (C05 sequence now ends `… S049 → S052`) and one `## Search log` entry (`:80`, `:103`). Row rule 2 is satisfied (no in-place pre-existing row change: `git diff b7abcd8..HEAD -- corpus/SOURCES.md` shows only `+` lines, ids `S052`/`S053`), but the Gate's one-line summary speaks only of rows. Draft addition: "SOURCES also gained one C05 Paths line (S049 → S052) and one 2026-10-27 search-log entry (6 identified / 6 screened / 5 included / 1 rejected)."

## Verified as conformant (no action)

- **Gate rule 1 for new rows.** S052: own-work command, access date 2026-10-27, 12-word stdout quote, scope limited to the printed output shape — command re-run reproduces all six MATCH lines byte-for-byte. S053: URL, access date, 14-word quote located under the `# zipfile` heading, `rejected`/`on-release`/flip clause present; `supersedes S044` opens `teaches`; S044 row untouched.
- **Row status changes.** Base 51 → HEAD 53 rows; the only changed row ids are `+ S052`, `+ S053`; no in-place status/recheck/used-by edit of a pre-existing row.
- **used-by and validate receipts (fixed in `a16e6cb` during this review).** At `c6e284c` S052 listed only the entry and S053 listed `—` while this lesson cites both; `a16e6cb` sets `S052 → corpus/knowledge/round-71-apk-axml-byte-evidence.md, corpus/lessons/round-71.md` and `S053 → corpus/lessons/round-71.md`, and logs the old→new values in `round-71.md:19`, satisfying rule 2. The same commit replaced the removed `sources-s053/validate/` mirror path with the two surviving `validate.log` receipts (`sources-s052` and `sources-s053`, both `EXIT=0`, W04/W01 warnings disclosed).
- **Quarantine.** The lesson's exact `awk` query re-derives 26 rows; the round histogram is round1=9, round2=4, round3=9, round4=4, so "all are historical r1-r4 entries" holds. The round-70 verdict counts (4 PRESENT / 19 ABSENT / 1 UNREACHABLE / 2 UNVERIFIED-REACHABLE) sum to 26 and are attributed second-hand to the round-70 lesson, not re-derived here.
- **M58 fix red-before.** `grep -c 'HOLD ' reports/round-70/measure-after.log` → 0 versus `reports/round-71/measure-before.log` → 10 rows; the pointer to `round-70-verifier-spotcheck.md:24-26,91-92` resolves to the routed defect.
- **Pre-gate technical claims.** Gate 24 blocks/0 problems and lint 0/0/0/0 reproduce; 18/18 fenced blocks byte-identical between round-70 and round-71 entries; `--zip-layout` is exactly 20 stdout lines with APPNOTE locators at 16-18 and width comparisons at 19-20 (so the lesson's line at `:25` is right, and the wave-1 Prose seat's "21 lines" count was a fenced-block artifact, not an entry defect); item 5's `readout.py:189/:197` locators-only wording, the Observation bounds, the Q14 row, the Q08 `superseded` row, the Q12 `n/a` row and the Q16 locator list are all present at `:64`, `:283`, `:312`, `:306`, `:310`, `:314`.
- **Wave-1 record numbers.** 40 seats / 0 dead / role histogram / 18 attacker seats match `w1-results.json`; wave-2 spec has 34 items, consistent with the 40 + 34 = 74-seat plan.
- **Proposal ledger arithmetic and cited artifacts.** 11 recorded rows each point at an artifact that exists (`R70W2ConnRoutedCarry.md`, `.ufo/waves/round-70/build-entry.py`, `corpus/lint_entry.py`, `R71W1Prose.md`), and the 11/18-versus-2/18 hit-rate sentence matches `corpus/lessons/round-70.md:131-136`.

## Concurrent-state disclosure

During this review the lane moved twice: `c6e284c` (wave-2 freeze) → `a16e6cb` (sources + lesson curation). The lesson I first read was sha256 `8ea8f355…`; findings D1–D9 were re-checked against the current `38f06c03…` and all still hold, except the used-by/validate-path gap, which `a16e6cb` closed (recorded above). `.ufo/waves/round-71/w2-votes/` and `w2-results.json` were absent throughout; `w2/` contained only `swarm-registry.json`. Separate peer report files appeared in `w2/` while I worked (`R71W2Census.md`, `R71W2Sentinel.md`, `R71W2SpotcheckDraft.md`) — untouched by me.

## Out of scope / not claimed

- No Q01–Q16 decision, no C1/C2 verdict, no C05 flip, no SCORECARD/LOG/README edit, no source repair, no re-gate after scoring.
- The round-70 verdict counts, the APPNOTE/DEX live-page contents and the provider route were not re-fetched here; they are reported as recorded by the cited seats.
- `PENDING` items that are legitimately future work are flagged as missing sections, not as falsifications: wave-2 Q table, C2 legs, candidate/spot-check records, wave-2 seat record, final census sentence.

Artifact: `.ufo/waves/round-71/w2/R71W2LessonReview.md` (this file). Scratch removed.
