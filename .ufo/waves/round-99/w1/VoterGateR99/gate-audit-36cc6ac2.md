# VoterGateR99 gate audit — C14 candidate, digest 36cc6ac2cd37d6866fe4ce0ad06c20d67d19fd2c7f0da08a2b63d277b948fce5

Seat: VoterGateR99 (role reviewer). Candidate: `corpus/knowledge/round-98-rea-host-readiness.md`
at the round-99 claims freeze (lane commit 7e6edd4db649f99c425daa46a91edbbd18a6e27c).
Audit date: 2026-11-05. Criteria: Q01–Q17 of `corpus/QUALITY.md`. All commands were run
read-only from the lane root `/home/vgpnk/Projects/shokunin/revenger-shokunin`. This seat ran no
counter on any tree, built no landing tree, and did not touch `corpus/README.md` or the entry's
`admission-status` line.

## 0. Vote-binding digest

Command (v7 `digest()` rule, `reports/round-98/c1_k_admit_counter7.py`):

```
python3 -B -c "import sys;sys.path.insert(0,'reports/round-98');import c1_k_admit_counter7 as c;print(c.digest(open('corpus/knowledge/round-98-rea-host-readiness.md',encoding='utf-8').read()))"
```

Printed exactly: `36cc6ac2cd37d6866fe4ce0ad06c20d67d19fd2c7f0da08a2b63d277b948fce5` — equal to the
frozen vote-binding digest (and to `reports/round-99/controls/lint-candidate-freeze.log`). Vote
proceeds.

## 1. Per-criterion evidence

Every decision below carries at least one command this seat ran against the entry or its records,
with the observed output.

**Q01 — PASS.** Field dump of `corpus/SOURCES.md` rows S506/S507: S506 kind `docs`, tier `A`,
opened `2026-11-05`, used-by this entry; S507 kind `own-work`, tier `A`, opened `2026-11-05`,
used-by this entry. `reports/round-98/quote-receipts/S506.receipt.json`: `verdict verified`,
`http_status 200`, `fetched_at 2026-11-05`, `fetch_sha256 ce2d122b…e50`, `length 16650`.
`grep -cF` in `reports/round-98/quote-receipts/raw/S506.body`: each of the three quoted sentences
("Doctor checks registration; it cannot establish the current agent's connection.", "Static
JavaScript and ordinary ZIP inventory need neither Hopper nor Ghidra.", "Inspect the actual shell
PATH and launcher/runtime.") prints `1`; the two remedy-table anchors print `1` and `1`;
`sed -n 35,37p` prints "Native / decompilation, Android analysis and firmware extraction have their
own / bring-your-own prerequisites." — the paraphrase row's source, as the entry states.
`reports/round-99/quote-receipts/S506-reopen-r99.txt`: `http=200`, `bytes=16650`,
`sha256=ce2d122b…e50`, `cmp=identical`. Both rows are tier A for their claims' scopes and opened in
the round that wrote the entry (2026-11-05, round 98).

**Q02 — PASS.** `grep -nE '^(source|verified-at|recheck|coverage-map|admission-status):'` on the
entry prints six header lines (1–6): two `source:` lines (S506 with the pinned commit URL and
anchor "Choose the remedy from the observed failure" table + paragraph after it; S507 with the
record path), `verified-at: 2026-11-05` with body and fetch-log paths, `recheck:` naming re-open,
re-run and re-derive targets, `coverage-map: C14`. `grep -n '^| C14' corpus/README.md` → line 61
(row exists; status `partial` at the freeze, untouched by this seat). The S507 anchor is
byte-exact: `head -c 41` of `rea-doctor-r98.txt` is exactly `healthy: false\nenvironment_healthy:
false` (od verified), matching the SOURCES cell "lines 1-2 (1-based bytes 1-41)". No bare homepage
anchor.

**Q03 — PASS.** `cat corpus/fixtures/archive-r2/truth.json` prints `archive_sha256
857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e`, `archive_size 2964`, members
`bin/checksum` 16160 (sha `f5ba0697…`) and `README.txt` 84 (sha `7d8f6a8d…`) — fixed in round 2,
outside the record under test. `sha256sum corpus/fixtures/archive-r2/fixture.zip` prints the same
archive digest. The inspect record's `declared_size` lines print `2964` / `84` / `16160` against
`logical_path` `.` / `README.txt` / `bin/checksum` in record order (grep -nE verified). Expectations
are not copied from the record being checked.

**Q04 — PASS.** Record `rea-inspect-artifact-archive-r2.txt` lines 10–11: `id: rea-artifact-graph`,
`name: REA safe artifact graph provider`; derivation row `grep cli_package_version` →
`  cli_package_version: 6.7.0` (re-run OK). Transcript blocks: `$ rea --version` → `6.7.0`, `rc=0`;
`$ jadx --version` → `1.5.6`, `rc=0`. `12.1.4` occurs 0 times in the transcript and 17 times in the
doctor record; the entry scores ghidra-version 12.1.4 from the doctor row and labels it
configuration. No tool is credited with output it did not print; manual/session observations are
labelled.

**Q05 — PASS.** Derivation row `grep -m1 evidence_id` re-run prints
`evidence_id: ev_0ef6c8cdbfe9836f2daa149d17269e355f98424d59ecb55398dbe271c6a87382`; record lines
28–29 show `operation: inventory_artifact` immediately followed by `status: completed` — the entry's
substep claim. `grep -ciE '^rc=|exit code'` on the inspect record prints `0`, so the entry's
disclosure that the exit codes (doctor 1, inspect 0) were session-observed and "are not lines of any
record" is accurate. The route table marks exactly one row `capability` (command, date 2026-11-05,
Evidence ID, expected values fixed before the run); doctor and version rows are labelled
`configuration`; the transcript header carries `2026-11-05T17:46:13-03:00, host Linux
7.2.11-arch1-1 x86_64`.

**Q06 — PASS.** `sha256sum corpus/fixtures/archive-r2/fixture.zip` → `857989f5…e27e`, byte-equal to
truth.json `archive_sha256` (equality checked by this seat; `grep -c` prints 1). Member premises
(84 / 16160 / 2964) match both truth.json and the record. The producer call ran on these bytes; no
fixture was authored or edited this round (`git log --oneline -1 -- corpus/fixtures/archive-r2/`
shows the fixture last touched at the round-2 commit, read-only git).

**Q07 — n/a.** `grep -inE 'predict|hypothes|we expect|caused by'` on the entry matches only line
128 — the §Q-map row itself. No parser accept, refuse or cause prediction is offered; see Q07 in
corpus/QUALITY.md.

**Q08 — n/a.** `corpus/QUALITY.md` Q11 row opens "Supersedes Q08."; Q08 has no independent object;
Q11 applied in full below. See Q08 in corpus/QUALITY.md.

**Q09 — PASS.** `sha256sum corpus/live/runs/round-98/*` reproduces all three record digests
(`94eaa6ff…`, `fb9a4824…`, `c373f656…` — derivation rows re-run OK); `sha256sum` + `wc -c` on the
S506 body give `ce2d122b…e50` and `16650`, as the entry states. The scope section states "it treats
no digest as authenticity or origin (Q09)"; every digest binds exact committed bytes only. The
entry contains 64-hex digests, so Q09 is applicable and decided on the merits.

**Q10 — PASS.** `uname -sr` → `Linux 7.2.11-arch1-1`; `uname -m` → `x86_64`; both match the entry's
scope line and the transcript header. Scope restricts every claim to one host, one date (2026-11-05)
and REA 6.7.0; `command -v rea` resolves to a per-shell `fnm_multishells` path (transcript), and the
entry treats it as per-shell per S506; unprobed routes are labelled unprobed; absent engines are
recorded absent (state-split `4 aligned / 1 manual / 8 missing / 1 stale` re-run OK).

**Q11 — PASS.** This seat re-ran all 23 derivation-table rows from a scratch script (receipt
`derive_check.out` beside this file): 22 rows reproduce the recorded outputs — doctor verdict lines,
scope counts `11`/`13`, client count `14`, state split `4/1/8/1`, missing-or-stale `9`, ghidra
healthy `8`, ghidra names (exact one-line match), doctor-printed versions (`detail: 12.1.4`,
`detail: 21.0.13; 64-bit; JDK; …`), engine/jadx classification pairs, installation paths `3` (the
raw record line `    paths[3]: /run/user/1000/fnm_multishells/3146096_…/bin/rea,……` carries exactly
three comma-separated paths, so the r98 count-by-lines defect is fixed; `controls/q11-paths-old-vs-new.log`
shows old `1` vs new `3`), installation state `1`, CLI version, Evidence ID, substep status, member
sizes, fixture digest, three record digests, S506 body digest and length. The single exception is a
rendered-output inaccuracy on the `scope-check classes` row, which is an output-description defect
decided at Q16, not a Q11 reject: the value is correct when re-derived and the derivation (command
that derives it from the primary record) is carried in-entry.

**Q12 — n/a.** `grep -oE 'S[0-9]{3}'` on the entry yields only `S506` (18 hits) and `S507`
(5 hits); neither row is rejected or superseded; no rejected registry row is load-bearing; see Q12
in corpus/QUALITY.md.

**Q13 — n/a.** The `recheck:` header (entry line 4) names re-open, re-run and re-derivation targets
only; no verifier or recheck command is credited with guarding any clause against deletion; see Q13
in corpus/QUALITY.md.

**Q14 — n/a.** `grep -nE '[0-9a-f]{16}'` piped to `grep -i byte` finds no clause pairing a hex run
with a byte count; the record-digest row uses 8-hex ellipsis prefixes with no length claim; this
seat's own lint run prints `LINT_Q14=0`; see Q14 in corpus/QUALITY.md.

**Q15 — n/a.** The only commit-shaped token is upstream REA revision
`12f6e0974cc0db0b3a9b86246accc76556837222` inside the S506 fetch URL — a source pin, not a lane-tree
identity sentence; no `rev-parse`/`X:corpus` claim exists; this seat's lint run prints
`LINT_Q15=0`; see Q15 in corpus/QUALITY.md.

**Q16 — FAIL (narrow; new this round).** Evidence in §2 below.

**Q17 — n/a.** No adjudication relocated a cited artifact for this entry. `test -f` resolves every
cited path: the three `corpus/live/runs/round-98/` records, `corpus/fixtures/archive-r2/fixture.zip`,
`corpus/fixtures/archive-r2/truth.json`, `reports/round-98/quote-receipts/raw/S506.body`,
`reports/round-98/quote-receipts/fetch-log.md`, `corpus/knowledge/2026-10-12-rea-readiness-checklist.md`,
`corpus/knowledge/round-96-native-analysis-sessions.md`, plus the round-99 controls the claims cite.
See Q17 in corpus/QUALITY.md.

### Transcript completeness (supports Q04/Q05/Q16)

`host-probes-r98.txt` read in full: 13 `$` blocks, 13 `rc=` lines; `awk` pairing shows
`pending=0 bad=0` (every command block is closed by an `rc=` line). Every value the entry credits to
the transcript is printed by it: `rea --version` → `6.7.0`; `command -v rea` → a
`fnm_multishells` path; `binwalk --version` → `binwalk 3.1.0`; `unblob --version` → `26.6.4`;
`jadx --version` → `1.5.6`; `java -version` → first line `openjdk version "21.0.13" 2026-10-20`
(the entry quotes a leading substring of this printed line); `command -v analyzeHeadless`,
`command -v idat64`, `command -v hopper` each print empty with `rc=1`; `python3 -c 'import pwn'`
prints empty with `rc=0`. `grep -ciE 'binwalk|unblob'` on the doctor record prints `0` — the entry's
"Doctor has no binwalk or unblob check" is true of the record bytes. `controls/q16-version-attribution.log`
concurs: `6.7.0 host-probes=1 doctor=11`, `1.5.6 probes=1 doctor=0`, `21.0.13 probes=3 doctor=3`,
`3.1.0 probes=1 doctor=0`, `26.6.4 probes=1 doctor=0`, `12.1.4 probes=0 doctor=17`.

## 2. Open item — Q16 FAIL, entry line 80

The derivation table's `scope-check classes` row (entry line 80) shows:

- Command: `sed -n '/^scope_checks/,/^informational_checks/p' corpus/live/runs/round-98/rea-doctor-r98.txt | grep -oE 'classification: [a-z_]+' | sort | uniq -c`
- Recorded output cell: `` `10 config_drift` / `11 healthy` / `3 missing_analysis_engine` ``

This seat ran that exact command; its stdout (cat -A) is:

```
     10 classification: config_drift$
     11 classification: healthy$
      3 classification: missing_analysis_engine$
```

The printed token `classification:` is missing from the recorded cell three times, so the recorded
output is not that command's stdout. Two in-entry sentences are therefore false for this row:

1. Line 65 (preamble): "…and the outputs are those commands' actual stdout."
2. Line 137 (§Q-map Q16): "Each sentence that credits a command or record with output was checked
   against that command's stdout, row by row in the derivation table."

The entry's own convention does not license the drop: the `engine and jadx classifications` row
strips its prefixes inside the command (`sed -E 's/^ *- name: //; …'`), the `registration state
split` row differs from stdout by leading whitespace only (uniq -c padding), and markdown cells
cannot be the excuse — a whole token is absent, not spacing. The counts and labels (10/11/3) are
correct when re-derived, so this is an output-description defect (Q16), not a wrong value.

The r98-routed Q16 defect itself (version attribution) is fixed and verified: see the transcript
completeness section. This FAIL is a different, previously unflagged sentence on the same criterion.

Fix within the amendment budget (for the L1 to decide; not applied by this seat): record the actual
stdout (`10 classification: config_drift` / `11 classification: healthy` /
`3 classification: missing_analysis_engine`), or make the command's stdout the cell, e.g. append
`| sed -E 's/^ +//; s/classification: //'`.

## 3. Decisions

| Q | decision | one-line basis |
|---|---|---|
| Q01 | PASS | S506/S507 tier A, opened 2026-11-05, receipt verified, all quotes located once in the committed body |
| Q02 | PASS | six header lines present, anchors are table+paragraph (not a homepage), C14 row exists, S507 anchor byte-exact (41 bytes) |
| Q03 | PASS | truth.json (round 2) archive digest and member sizes match fixture bytes and record |
| Q04 | PASS | tool/version/function named; `rea-artifact-graph` id in record; versions traced to printing records |
| Q05 | PASS | one capability row with command/date/Evidence ID; exit codes honestly disclosed as session observations (0 exit lines in records) |
| Q06 | PASS | fixture sha256 equals truth.json archive_sha256; premises byte-verified |
| Q07 | n/a | no parser prediction or cause claim exists |
| Q08 | n/a | superseded by Q11 per QUALITY.md |
| Q09 | PASS | digests bind exact committed bytes; origin/authenticity disclaimed; all re-hashed by this seat |
| Q10 | PASS | one host/date/version scope, matches uname and transcript header; per-shell PATH treated per-shell |
| Q11 | PASS | 22/23 derivation rows reproduce exactly incl. the fixed install-paths row printing `3`; the one output inaccuracy is decided at Q16 |
| Q12 | n/a | only S506/S507 cited; no rejected row load-bearing |
| Q13 | n/a | recheck names re-derivation only; no verifier credited as guarding a clause |
| Q14 | n/a | no hex+byte-count clause; no truncated run with length; LINT_Q14=0 |
| Q15 | n/a | no lane-tree git identity sentence; upstream pin lives in a URL; LINT_Q15=0 |
| Q16 | FAIL | line 80 recorded output is not the command's stdout (`classification:` prefix dropped), falsifying line 65 and line 137 claims |
| Q17 | n/a | no relocation adjudicated; all cited paths resolve |

Lint (this seat's own run): `LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0 LINT_HEADER=0`, rc 0.

## 4. Agreement with the entry's §Q-map

16 of 17 decisions agree. Disagreement: Q16 — entry line 137 says PASS; this seat says FAIL on the
row-by-row stdout comparison that line itself claims.

## 5. Not run by this seat

No counter (v7 or v8) on any tree; no landing tree; no fixture or corpus edits; no v7/r98-builder
runs (not needed); no peer messages. Frozen controls read: `q11-paths-old-vs-new.log`,
`q16-version-attribution.log`, `lint-candidate-freeze.log`, `c1-base-rowstatus.log`,
`S506-reopen-r99.txt`, `s507-reopen-r99.txt`.
