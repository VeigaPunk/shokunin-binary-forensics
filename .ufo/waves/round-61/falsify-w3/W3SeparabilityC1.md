GRADE: HOLDS — C1 separability: K reaches 6/14 with C2 absent; holds stay ok (seat RevengerR61-2.W3SeparabilityC1)

## Trees (scratch /tmp/revenger-r61w3-W3SeparabilityC1, read-only git archive/show on the lane)
- base = `git archive cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97`; landed = `git archive ab580698212258a55e43e9bb9bf6ac78c91eae2a`.
- cf = base + exactly these 5 files via `git show ab58069:<f>` (sha256 prefix, equal to landed):
  `corpus/knowledge/evm-saved-interface-candidates.md` ab9c48da93cc83da; `corpus/knowledge/commonjs-destructured-require-edges.md` 3382f1b3c56fbffb;
  `corpus/README.md` 9010c87374ac1b03; `corpus/SOURCES.md` aa7b07e12107ab9e; `corpus/lessons/round-61.md` dd5511584a346b0d.
- `diff -rq cf/corpus landed/corpus` → only `QUALITY.md`, `verify_icon_languages.py`, `verify_multi_icon_states.py` differ, so C2 is absent.
  The C2 scripts in cf equal base (ed0ad166…, 5b75339c…).
- cfq = cf + landed `corpus/QUALITY.md` (Q12/Q13 rows), a control for the one landed corpus file outside both the C1 and C2 sets.
- Probe: `python3 -B landed/reports/round-61/measure.py <tree>`, with measure.py sha256 ada7a9c9…d50d2 (= live file).

## Observations (command output)
| tree | K_HELD | K_HELD_BACKED | C2_B_KILLED_ATTRIBUTED | C2_CONTROLS / D2 | HOLD_CAL | HOLD_REPLAY | HOLDS_OK | exit |
|---|---|---|---|---|---|---|---|---|
| base | 4/14 | 4/14 | 0/2 | 2/2 / 2/2 | 4/4 | 10/10 | yes | 0 |
| cf | 6/14 | 6/14 | 0/2 | 2/2 / 2/2 | 4/4 | 10/10 | yes | 0 |
| cfq | 6/14 | 6/14 | 0/2 | 2/2 / 2/2 | 4/4 | 10/10 | yes | 0 |
| landed | 6/14 | 6/14 | 2/2 | 2/2 / 2/2 | 4/4 | 10/10 | yes | 0 |
- Outside the MUTANT and C2_* lines, the cf probe log is identical to landed (`diff` empty). Every HOLD line matches.
- In cf, mutant b still survives 2/2 (`MUTANT verify_icon_languages.py b exit=0 pass`, and the same for multi_icon). This confirms the cf tree is C2-free, and that K does not depend on C2.
- README rows base→cf: 14→14. Only the C04 and C09 rows change (`uncovered`→`held`, knowledge cell now names the entry). The other 12 rows are byte-identical (`diff` of the `^| C[0-9]+ ` lines).
- The backing gate is live in cf. Removing evm-saved-interface-candidates.md gives `K_HELD_BACKED=5/14`, removing commonjs-destructured-require-edges.md gives `5/14`, and removing both gives `4/14`. HOLDS_OK=yes in all three.
- `corpus/live` and `corpus/fixtures`: `diff -r` cf==base==landed. `git diff --stat cf02419 ab58069 -- corpus/live corpus/fixtures` printed nothing, rc 0.
- Entry Reproduce blocks: python extracted from `## Reproduce` and run with cwd = tree root. They only read bytes and JSON and execute no fixture JS or bytecode. Results:
  - EVM: exit 0, 14 lines; cf == landed == the `## Provenance (Q11)` text block, byte-identical.
  - CJS: exit 0, 29 lines; cf == landed == recorded.
- Census `scripts/sources-census.sh validate --root /tmp/revenger-r61w3-W3SeparabilityC1 <tree>`:
  - cf and landed both print `W04 S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes` then `ok`, rc 0.
  - base prints `ok`, rc 0. The W04 warning comes from C1's SOURCES.md and is identical with or without C2.
- Pre-existing C13 entry precondition: `grep -c "receipt\['command'\]"` gives 1/1/1 in base, cf and landed (digest-scope-versus-provenance.md:151-156 still holds).

## Finding (calibration note, not a C1 defect on landed)
- The declared partition (claims.md:66-67: "C1 touches only corpus/knowledge/, corpus/README.md, corpus/SOURCES.md and the round lesson; C2 touches only the two verifier scripts") does not cover the landed corpus diff.
  - `corpus/QUALITY.md` (+Q12/Q13, landed QUALITY.md:24-25) belongs to neither claim. Its source is the frontier "mined mistake" step (lesson round-61.md:43, "captured by a criterion 2 (Q12, Q13)").
- So the C1-only tree is not textually self-consistent:
  - cf `corpus/README.md:9` says "admission criteria Q01–Q13", but cf QUALITY.md holds only Q01–Q11.
  - Both entries' QUALITY tables score rows that don't exist in cf: evm-saved-interface-candidates.md:188-189 and commonjs-destructured-require-edges.md:201-202 (Q12 n/a, Q13 pass).
- Impact: none on the count or the holds. The cfq control equals cf on every value. C1 admission is pre-registered on Q01–Q11 (claims.md:30-31), so Q12/Q13 rows are extra, not required. On landed ab58069, README:9 is true.
- Impacted axes: calibration (claim-boundary wording) only. Coverage K is unaffected.
- Smallest safe correction: a future claims amendment naming `corpus/QUALITY.md` (Q12/Q13) as a frontier-step file outside C1 and C2. No entry, README or probe change is needed.

## Inference / unknown
- [INFERENCE] The live census run in measure-after.log reads the live working-copy SOURCES.md. Here it was re-run on the archived cf and landed trees instead (same SOURCES sha256 aa7b07e1…), so this report doesn't depend on the live tree's state.
- Not attacked here (other seats): Q01–Q11 content, tier-A status of S016–S027, entry overstatement.

VERDICT: HOLDS. The C1-only tree (base + 5 files) gives K_HELD_BACKED=6/14 with C2 absent (mutant b 0/2), HOLDS_OK=yes, probe exit 0, fixtures/records identical, Reproduce outputs identical, and the gate drops to 5 and 4 when entries are removed. One calibration note: QUALITY.md Q12/Q13 sits outside the declared C1/C2 partition, and in a C1-only tree README:9 and the entries' Q12/Q13 rows reference criteria that aren't there.
Installs: none.
