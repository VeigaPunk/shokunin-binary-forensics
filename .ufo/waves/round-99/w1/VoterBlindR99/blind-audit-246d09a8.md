# Blind audit (Amendment B) — VoterBlindR99 (reviewer) — candidate 246d09a8

- Seat: VoterBlindR99 (reviewer, pinned). This is the full re-vote after Amendment B
  (lane commit 9ddd38a); my earlier vote on 36cc6ac2 is superseded and was not consulted.
- Entry audited: `corpus/knowledge/round-98-rea-host-readiness.md` (current worktree)
- Vote-binding digest: `246d09a8cf6523ab380f88f7945f220338c27e31f8b43ba876bbd0a9a8d746da`
- Blindness: no vote file (including my superseded one), no other seat's audit, no round-98
  critic/reviewer audit, and no claims.md amendment FAIL text was read. Inputs: the entry,
  `corpus/QUALITY.md`, `corpus/SOURCES.md` rows S506/S507, `corpus/README.md` C14 row, the S506
  committed body + fetch log, the three S507 records, `corpus/fixtures/archive-r2/truth.json`,
  the 2026-10-12 checklist, the probe transcript, and frozen v7's digest/check_vote_notes source.
  I read the entry's own diff since 7e6edd4 (its bytes, not any seat's prose) to scope the re-audit.
- Receipts beside this file: `derivations-rerun-amended.txt`
  (sha256 `e99af3f3b10b749423bd4eecf08aa7307ee8dff7fd5c6530df7f3c4448bb91f1`), produced by my
  scratch runner with all 29 amended derivation rows verbatim plus prose checks.

## 1. Digest recompute (frozen v7 digest(), reports/round-98/c1_k_admit_counter7.py:109-111)

```
DIGEST_AMENDED = 246d09a8cf6523ab380f88f7945f220338c27e31f8b43ba876bbd0a9a8d746da
MATCHES_246d09a8 = True
ADMISSION_STATUS_LINES = ['admission-status: candidate']
```

## 2. What Amendment B changed (from the entry's own bytes)

Rendered derivation-table output cells to a stated rule (one code span per stdout line joined by
` / `, annotation only after ` — `, digest-prefix plus file-name rule for the record-digest row);
split the scope-check count into healthy/failing rows; added rows for host identity, ghidra-named
scope checks, ghidra-headless launcher path, installed skill identity, doctor binwalk/unblob
absence, inventory members+sizes as `logical_path declared_size` pairs, inventory root digest,
truth.json archive digest; anchored the substep-status row to `operation: inventory_artifact`;
tightened the ghidra route-row attributions; Q11/Q16 map rows now cite
`reports/round-99/controls/deriv_check.py`.

## 3. All 29 derivation rows re-run — byte-identical

My runner (independent of the entry-cited control) re-ran every row from the lane root; every
output matched its cell under the stated rule. Highlights: host identity
`Linux 7.2.11-arch1-1 x86_64`; healthy `11` / failing `13`; classes `10 config_drift / 11 healthy /
3 missing_analysis_engine`; 14 registration pairs (4 aligned / 1 manual / 8 missing / 1 stale);
missing-or-stale `9`; ghidra-named `8`, ghidra healthy `8`; headless launcher
`detail: /home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC/support/analyzeHeadless`; doctor versions
`detail: 12.1.4` and `detail: 21.0.13; 64-bit; JDK; …`; engine/jadx four pairs; skill identity
four lines ending `detail: Installed REA skill identity is stale.`; binwalk/unblob count `0`
(grep rc=1 on zero matches, exactly as the cell's em-dash annotation says); paths `3`;
`state: multiple`; `cli_package_version: 6.7.0`; evidence ID `ev_0ef6c8cd…`;
`operation: inventory_artifact` / `status: completed`; members `. 2964 / README.txt 84 /
bin/checksum 16160`; root digest, truth.json digest, fixture digest all `857989f5…`; record
digests `94eaa6ff… (host-probes-r98.txt)` / `fb9a4824… (rea-doctor-r98.txt)` /
`c373f656… (rea-inspect-artifact-archive-r2.txt)`; S506 body `ce2d122b…`, length `16650`.

## 4. The entry-cited control, independently exercised

- `python3 -B reports/round-99/controls/deriv_check.py --entry <entry> --root .` on the worktree:
  29 × `DERIV … MATCH`, `DERIV_ROWS=29 DERIV_MISMATCH=0`, exit 0 — the Q11/Q16 credit
  ("re-runs every row", "reports 0 mismatches") is true.
- Deletion-detection demonstration (scratch copies only, lane untouched):
  - mutant 1, one output cell's code span deleted → `DERIV healthy scope checks MISMATCH
    got=['11'] want=[]`, `DERIV_MISMATCH=1`, rc=1;
  - mutant 2, one command's record path corrupted → `DERIV client registration count MISMATCH
    got=[] want=['14']`, `DERIV_MISMATCH=1`, rc=1.
  Its own run therefore detects deletion or corruption of exactly the clauses it is credited with.

## 5. Quotes and prose re-verified

- S506 quotes byte-exact in the committed body: line 22 (doctor-registration), line 34
  (static-JS/ZIP), line 26 (shell PATH); paraphrase matches body lines 35-37 verbatim.
- jadx detail quotation byte-exact in the doctor record (lines 65, 161, 236).
- K05 correction accurate: the `## Re-verification 2026-10-19` row records
  "pwntools import fails" (checklist line 40); the round-98 probe rc=0 corrects it.
- Exit codes 1/0: `grep -c 'rc='` on both records → 0 matches; the preamble credits them to the
  session, not to a record — honest.
- Probe transcript prints every credited version (rea 6.7.0, jadx 1.5.6, java "21.0.13",
  binwalk 3.1.0, unblob 26.6.4) with its own command and rc= line; header prints the host and
  `2026-11-05T17:46:13-03:00`.
- truth.json: `archive_sha256` equals the fixture digest and the evidence root digest; members
  16160/84 match; evidence member sha256s equal truth.json's (corroboration).
- SOURCES rows S506/S507: docs tier A / own-work tier A, opened 2026-11-05 (the writing round).
  Observation: the S507 row's prose differs slightly from the claims-freeze text (amendment
  commit touched the registry row); tier, scope and open date are unchanged, so Q01/Q02 are
  unaffected.
- Cited-path sweep: 14/14 paths resolve, including the amendment's
  `reports/round-99/controls/deriv_check.py`; README C14 still `partial` (pre-landing, expected).

## 6. Per-Q decisions (command + output evidence)

- **Q01 PASS** — `sed -n '523,524p' corpus/SOURCES.md` → S506 `docs | A`, S507 `own-work | A`,
  both opened 2026-11-05; S506 table credits exactly what the reference states (§5 quote check);
  host facts cite the lane's own S507 records.
- **Q02 PASS** — entry opens with both `source:` lines (pinned commit URL + named anchor; corpus
  path), `verified-at: 2026-11-05`, concrete `recheck:`, `coverage-map: C14`; `grep -n 'C14'
  corpus/README.md` → line 61.
- **Q03 PASS** — `grep -oE '"archive_sha256": *"[0-9a-f]+"' corpus/fixtures/archive-r2/truth.json`
  → `"archive_sha256": "857989f5…"`; round-2 expectation, independent of the record under test.
- **Q04 PASS** — `grep -nE 'provider|operation'` on the inspect record → provider
  `rea-artifact-graph`, operations `inspect_artifact`/`inventory_artifact`; each version claim
  carries its own probe command and rc= line.
- **Q05 PASS** — the single capability row carries command, date, Evidence ID and (disclosed)
  exit 0; all other rows labeled configuration or absent; presence never called capability.
- **Q06 PASS** — `sha256sum corpus/fixtures/archive-r2/fixture.zip | cut -d' ' -f1` →
  `857989f5…` = truth.json `archive_sha256`; sizes 2964/84/16160 match the manifest; no fixture
  authored or edited this round.
- **Q07 n/a** — trigger grep hits only the entry's own Q07 map row; nothing predicts parser
  accept/refuse/cause.
- **Q08 n/a** — `corpus/QUALITY.md:23` "Q11 | Supersedes Q08"; Q11 applied instead.
- **Q09 PASS** — re-derived fixture, three record-file, and S506-body digests; each binds exact
  committed bytes; scope paragraph disclaims authenticity/origin; evidence_id used as receipt only.
- **Q10 PASS** — scope paragraph limits claims to this host, 2026-11-05, REA 6.7.0, named routes;
  unprobed routes labeled unprobed.
- **Q11 PASS** — all 29 rows byte-identical on my independent re-run (§3); every count,
  identifier, digest, path and doctor-printed version in the scope paragraph, route table and
  observation now has an in-entry derivation; session-only exit codes are labeled as such.
- **Q12 n/a** — reject-grep hits only the entry's own Q12 map row; nothing rests on a rejected row.
- **Q13 PASS** — a verifier (deriv_check.py) is now credited, and the credit equals its own run's
  coverage: I re-ran it (29 MATCH, 0 mismatches, exit 0) and demonstrated by scratch mutants that
  its run detects both a deleted output cell and a corrupted command (§4); transcript-sourced
  values and session exit codes are named as outside the derivation table. The entry's Q13 map
  row still says "no verifier is credited" — stale rationale wording, but the criterion's reject
  condition (crediting a guard whose check survives deletion) is nowhere met.
- **Q14 n/a** — 64-hex strings appear only in the source URL, evidence_id and digest rows, none
  paired with a byte count; the record-digest cell's `…` is the command's own awk output.
- **Q15 n/a** — 40-hex occurrences are the pinned REA revision inside the fetched URL and
  substrings of digests; no lane-tree identity sentence exists.
- **Q16 PASS** — every output cell matched its command's stdout under the stated cell rule (my
  run and deriv_check agree, 29/29); the absence sentence is derived in-table (count 0, annotation
  explains grep rc=1); the substep status is anchored to `inventory_artifact`; exit codes credited
  to the session.
- **Q17 n/a** — 14/14 cited paths resolve; no relocation occurred.

Decision: 11 PASS (Q01-Q06, Q09-Q11, Q13, Q16), 6 n/a (Q07, Q08, Q12, Q14, Q15, Q17), 0 FAIL.
