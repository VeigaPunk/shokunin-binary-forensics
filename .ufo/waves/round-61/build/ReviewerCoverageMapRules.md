# ReviewerCoverageMapRules — round 61 (read-only)

Seat: CloseChousa26.ReviewerCoverageMapRules-10 · claims base cf02419 · HEAD e0a4b0c · `corpus/README.md` and `corpus/QUALITY.md` blobs identical at both (482ea714…, 521bd603…).
Method: git show/ls-tree/grep and in-memory regex tests. No probe, census, or lane write was run. O = observed, I = inference.

## 1. When a row may flip uncovered → held (C04, C09 only)
1. Meaning: `held` = at least one admitted knowledge entry covers the ground. Fixtures, live runs and verifiers are work evidence, not knowledge (README:19-23, O).
2. Admission: Q01–Q11 pass (n/a needs a reason), recorded in `corpus/lessons/round-61.md` `## Gate`; a reject names its Q-id (QUALITY.md:25-31, O).
3. Header (Q02, QUALITY.md:14): `source:` lines lead with an S-id, plus `verified-at:`, `recheck:`, and one `coverage-map: C04` line (regexes in §2).
4. Sources: new Registry rows, id S016+ (kimi CORPUS.md:89; S001–S015 at SOURCES.md:15-29), `opened` 2026-10-21, tier A for scope, kind not `community`. No existing row can serve: all 15 are opened 2026-10-19 (O); claims.md:31-32 needs a round-61 opening (I).
5. `status` = `mined` only once `used-by` lists `corpus/knowledge/<slug>.md`. The counter checks the listing (revenger.md:122); census E11 checks the path exists and W03 warns on `mined` with `—` (sources-census.sh:29,32; O).
6. Gate records URL, access date, ≤25-word verbatim quote with location (kimi CORPUS.md:112-115); search log prose with counts (:126-128); each status change logged old→new (contract rule 2).
7. README: C04 (README:30) / C09 (README:35) knowledge cell `—` → `knowledge/<slug>.md`; status `uncovered` → `held` (exact token). No other row changes.
8. Census `validate` before and after (claims.md:72-75).
Harm voids admission: a changed saved record or fixture, a lost hold (the other 12 rows stay byte-identical), an overstated entry, or an unopened source (claims.md:68-70).
Not sufficient: work evidence; "survives the wave-2 attacks" (claims.md:33), which has no Q-id, so map each attack to Q01–Q11 or it cannot reject (QUALITY.md:28-29); lane-dispatched subagents, this seat included, are still the lane (LEARNING.md:46).
The flip need not wait for the outside check (kaika admitted first: round-1.md:90-111, O). Discernment "improved" does need ≥1 admit and ≥1 reject sampled non-author (LEARNING.md:42-45); a round with zero recorded rejects cannot be sampled.

## 2. How K and the expansion trend are counted
- K (SCORECARD.md:133; measure.py:24-29): K_HELD = rows matching `^\| C[0-9]+ ` whose last cell is exactly `held`, over all such rows (14). Score = 10·K_HELD/14, 1 dp. Base 4/14 = 2.9 (measure-before.log:2; my `grep -cE` gives 4 and 14 on cf02419, O). Rows count once.
- Expansion (LEARNING.md:33; kimi CORPUS.md:123-125): admitted knowledge entries that are new vs base, whose `coverage-map` row was uncovered/partial at the frozen base, and whose `source:` cites a `mined` row listing that entry. Executable form: fleet `.ufo/reports/round-1/revenger.md:104-125`.
- Counter regexes (in-memory, O): `^coverage-map: C<n>$` only ("coverage-map: C04 (JavaScript)" fails; revenger.md:119). `^source: S<n>` must lead the line ("source: https://… S016" fails; :120). `used-by` splits on `,` only ("a.md; b.md" drops b; census splits `[,;]`, sources-census.sh:147).
- Constants are hard-coded: `mapc="a7acc20"; base="8bbcb4e"` (revenger.md:106). For round 61 set both to cf02419. Unchanged, the four kaika entries (absent at 8bbcb4e; uncovered/partial at a7acc20) count again, so the run reads `total=4` before any new entry (I; same code path that printed revenger.md:133).
- Reads the working tree (revenger.md:112,116), not a commit: run it on a clean checkout of the landing commit.
- Frozen set = {uncovered, partial} (:122,:124). LEARNING.md:33's "ground the map did not hold" also covers frontier; no frontier entry is planned, so record the chosen set in the Gate.
- Predicted: expansion +2 (both admit), +1 (one), 0 (none). Trend: improved iff ≥1 counted; harmed iff an admitted entry fails its bar (LEARNING.md:31-35).
- K and expansion can split: a row can flip while its source is `queued` (K +1, expansion 0). Report both (SCORECARD.md:138-139).

## 3. README index lines that must change on landing
- :9 "admission criteria Q01–Q10" → "Q01–Q11 (Q11 supersedes Q08)". Base drift: QUALITY.md:23 defines Q11; SCORECARD.md:181 already says Q01–Q11 (O).
- :11 "`knowledge/` — admitted domain entries" → only gated entries are admitted; `seed.md` and the readiness checklist are pre-contract (README:49-52, O; ScoutReadmeDrift.md D5 agrees).
- :12 lessons list omits `round-1-verifier-spotcheck.md` (exists; integrator-written per its line 3, O). Add it. On landing add `round-61.md` (`## Gate`, one `## Mistakes` row) and any integrator check as `round-61-verifier-spotcheck.md` (new file; kimi CORPUS.md:53-60).
- :42-43 footer "statuses … frozen at `a7acc20`" is stale for round 61. Reading it gives K before 0/14 (score 0.0), so a 6/14 landing reads +4.3 instead of the true +1.4 (a7acc20 held=0; ScoutCensusBaseline.md:60). Add a round-61 pointer, `git show cf02419:corpus/README.md`; keep the kaika line as history.
- :30, :35 cells as in §1.7. :13–:15 are unchanged by C1; "Rows 14" stays.
- Path forms differ on purpose: README cells use `knowledge/<slug>.md`; `used-by` and the counter need `corpus/knowledge/<slug>.md`.

## 4. Counting pitfalls in the probe's K regex (measure.py:22-29)
- P1 exact token: only a literal `held` then ` |` at EOL counts. In-memory (O): plain → grep 1 / probe 1; `**held**`, `held (partial)`, trailing space → 0 / 0; CR residue → grep 0 / probe 1 (universal newlines); `|C04|…|held|` → row dropped from the denominator. Read K_ROW together with K_HELD.
- P2 denominator = every line starting `| C<digits> `; a reformatted row drops out (14→13) and the score rises. Check K_HELD prints /14.
- P3 total only: a swap (C04 held while another row loses held) reads +1 (CriticSeparability.md:26, O). Require the other 12 rows byte-identical and K_ROW C04/C09 = `held`.
- P4 string, not admission: a README-only flip passes. Pair with a path-exists check on the cell, the Gate, and census.
- P5 committed tree only (`git archive <commit> corpus`; measure.py:4-8, claims.md:10-12): uncommitted flips are invisible.
- P6 CRLF: the probe matches SCORECARD.md:133 on LF text and diverges on CR. Base has 0 CR and 0 trailing-space lines (`grep -cP '\r$'`, `grep -cE ' +$'`, O).
- Any change to measure.py after pre-registration is a new registered version (claims.md:10-13), not an edit.

## 5. Facts that change C1 scope
- F1 (O): C09 has saved REA records: 7 `inspection.json` files (rounds 19, 21–26) with `"operation":"inspect_evm_interface"`; round-19 names `evmole@0.9.3`. Peer ScoutReadmeDrift.md:47 ("no inspect_evm_interface record") is wrong; SCORECARD.md:82 lists `evm`.
- F2 (O): C04 saved JS: 2 files with `"operation": "analyze_javascript_application"` (round-14, round-18 `trace-request.json`).
- F3 Q03/M06: C09 PUSH4/JUMPDEST values come from fixture bytes via an in-entry command, not from the record under test (QUALITY.md:15; round-1.md:43). Q04: name `evmole@0.9.3` and the function if its output is scored (QUALITY.md:16).
- F4 Q01 risk: "destructured require edges" (C04) and "PUSH4 selector candidates" (C09) are not stated by any S001–S015 row (O); label them inference and cite only what a row states (QUALITY.md:13).
- F5 Q10: PROVINCE.md:3-4 owns Electron/JavaScript packages, but kaidoku/revenger ADJ-06 is unresolved (connector.md:64-79; SCORECARD.md:136). C04 scopes to byte-level structure, reports ADJ-06, and claims no REA provider operations.

Installs: none (git, grep and Python stdlib only).
VERDICT: C1 flips only on an admitted, census-clean entry plus a `held` token; K base 4/14; re-base the expansion counter to cf02419 (revenger.md:106) and change README :9, :11, :12, :42-43 on landing.
