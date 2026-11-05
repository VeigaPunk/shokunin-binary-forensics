# ReviewerGate — findings (revenger round 98, wave w1)

## Amendment C re-audit (binding vote, L1 commit `1b76b4d`, declared last amendment)

Diff inspected: `git diff 0146c0a 1b76b4d -- corpus/knowledge/round-98-rea-host-readiness.md`
(derivation-table preamble rescoped, 3 count rows added, §Q-map Q06 row
n/a→PASS; no other hunk).

- **New digest recomputed by me**: `6d27c129e6ec3bbd3699c84c0a06301d7aea88140e54a1ff8d8b34d5c0c5330f`
  — matches the L1-stated Amendment C digest.
- **CriticR98's Q11 defect repaired**: the three registration counts now have
  deriving rows, re-run by me, byte-equal: `grep -c '^    - client:'` → `14`;
  `awk … | sort | uniq -c` → `4 aligned / 1 manual / 8 missing / 1 stale`;
  `awk … | grep -cE '^(missing|stale)$'` → `9` (supports the Observation's
  "nine stale or missing client registrations").
- **CriticR98's Q16 defect repaired**: the preamble no longer credits the
  table with version strings and exit codes. Versions are sourced to
  `host-probes-r98.txt` (13 `$ …` commands each followed by output and an
  `rc=` line — re-verified); doctor exit 1 / inspect-artifact exit 0 are
  explicitly labeled session-observed, "not lines of any record" (true: no
  exit/rc lines in either record). The `\|` escape sentence is accurate (shell
  pipes and the `missing\|stale` alternation both unescape to the commands I
  ran).
- **Q06 n/a→PASS independently confirmed**: fixture digest
  `857989f5…be27e` (re-derived by sha256sum) equals truth.json
  `archive_sha256`; member sizes 84/16160 and archive size 2964 match the
  record's `declared_size` order; premise bytes fixed in round 2 (`5c9fb20`)
  and unchanged; no failed inputs. Nothing stated from intent.
- **Decision set**: 10 PASS (Q01–Q06, Q09–Q11, Q16) / 7 n-a (Q07, Q08, Q12,
  Q13, Q14, Q15, Q17) / 0 FAIL.
- **Vote**: `reports/round-98/votes/ReviewerGate.json` overwritten, bound to
  `6d27c129…`; `artifact_path =
  .ufo/waves/round-98/w1/ReviewerGate/gate-audit-amendment-c.md`;
  `artifact_sha256 =
  ea71f559963136d85b3ca8dbd1cae0e444d88b420c6320766fe88dfadcd9b1eb`
  (verified against the audit file bytes after writing; strict-JSON reload
  passes, 17 decisions, 0 FAIL). Prior votes (digests `1ea9260c…`,
  `73f1d7e0…`) superseded, kept by the L1.
- Exit codes: all re-run derivation commands exit 0; digest recompute matches.

## Amendment B round (superseded by Amendment C)

The L1 amended the candidate before any scoring (claims Amendment B):
`## §Q-map` appended, 3 derivation rows added, one route-table clause and one
observation clause reworded. Diff inspected via
`git diff cf8a9d4 0146c0a -- corpus/knowledge/round-98-rea-host-readiness.md`
(29 insertions, 4 deletions, no other file touched by that diff hunk set).

- **New digest recomputed by me** (v6 `digest()` rule; the file's only
  `admission-status` line already reads `candidate`):
  `73f1d7e044df04373a36c1f94f7e7216a7a513043ef769d5567a98cb53dd80e7` — matches
  the L1's stated Amendment B digest.
- **Three new derivation rows re-run, all byte-equal**: ghidra healthy count →
  `8`; installation-path greps → `1` and `1`; `wc -c` S506 body → `16650`.
- **Reworded clauses narrow the claims** (verified honest): "Hopper was absent
  during this run" → "Doctor reported Hopper missing the same day (record 1)"
  (record 1 = the doctor receipt, which reports `hopper`
  `missing_analysis_engine`; both records 2026-11-05); "at a time when" →
  "on the same day that" (saved records carry no sub-day ordering; the new
  sentence no longer claims it).
- **§Q-map cross-check**: the entry's own 17-row Q-map agreed with my
  independent audit on all 17 decisions at that commit.

Original (superseded) audit below.

---

## First audit (digest `1ea9260c…`, superseded by Amendment B)

Seat: ReviewerGate (reviewer). Candidate audited:
`corpus/knowledge/round-98-rea-host-readiness.md`, normalized digest
`1ea9260c812947d3e2c61161c22a1e143df432168e7b9b5bc4c1a90c0b1527b8` — recomputed
by me with the v6 `digest()` normalization rule (every `admission-status` line
normalized to `admission-status: candidate`) over the committed 10483-byte
file; equal to the frozen claims value, and the working-tree file is
byte-identical to the same path in the `git archive 9d49002a…` freeze
extraction.

## Q decisions with the command behind each

| Q | decision | command / evidence |
|---|---|---|
| Q01 | PASS | `sed -n '523,524p' corpus/SOURCES.md` (both rows tier A, opened 2026-11-05, used-by this entry); `python3 corpus/audit_source_quotes.py verify --sources corpus/SOURCES.md --receipts reports/round-98/quote-receipts --sid S506` → `state=verified`, exit 0; fresh 2026-11-05 `curl` of the pinned S506 URL → HTTP 200, 16650 bytes, sha256 `ce2d122b…` byte-identical to `raw/S506.body` |
| Q02 | PASS | entry lines 1–6 read raw (dual `source:` with pinned URL + located anchor `## Choose the remedy from the observed failure` at body line 16; `verified-at: 2026-11-05` naming revision `12f6e09`; `recheck:` names re-open/re-run/re-derive; `coverage-map: C14` = README line 61 "host readiness for REA routes"; `admission-status: candidate`) |
| Q03 | PASS | `git log --oneline -- corpus/fixtures/archive-r2/` → `5c9fb20` (truth fixed in round 2, outside this round's record); `truth.json` member sizes 16160/84, archive digest/size 857989…/2964 cross-checked against `sha256sum corpus/fixtures/archive-r2/fixture.zip` → `857989f5…be27e`; identity (digest) held separately from locator (path) |
| Q04 | PASS | `grep cli_package_version …rea-doctor-r98.txt` → `  cli_package_version: 6.7.0` (matches entry); `$ rea --version` probe transcript `6.7.0`; provider `rea-artifact-graph`, operation `inspect_artifact` in the inspect record header; binwalk/unblob/jadx/java versions appear only as printed probe outputs |
| Q05 | PASS | capability row backed by real probe: `grep -m1 evidence_id …rea-inspect-artifact-archive-r2.txt` → `ev_0ef6c8…`, `grep -m1 'status: completed'` → present, exit 0 stated, values matched against round-2 truth; ghidra → "configured. Not re-run this round", android/firmware → "capability unprobed", native engines → "not ready" (no presence-as-capability) |
| Q06 | n/a | no fixture authored/edited this round; round-2 premise bytes verified in place (sizes/digest cross-check above). n/a reason recorded in the vote note |
| Q07 | n/a | no parser accept/refuse/cause prediction exists anywhere in the entry |
| Q08 | n/a | superseded by Q11; applied in full there |
| Q09 | PASS | scope sentence "treats no digest as authenticity or origin (Q09)"; fixture digest derived by `sha256sum` and used as value comparison only; record digests `94eaa6ff…`/`fb9a4824…`/`c373f656…` re-run byte-equal; Evidence-ID chain never claimed as origin |
| Q10 | PASS | scope limits "one host … 2026-11-05 … routes this lane uses" + explicit no-other-host/date/version/route sentences; S507 scope cell "not other hosts, dates or routes"; pwntools correction scoped to the 2026-10-19 re-probe |
| Q11 | PASS | all 15 derivation rows re-run from the lane root: 1,2p → `healthy: false`/`environment_healthy: false`; scope ok-true/false → 11/13; classifications → 10 config_drift / 11 healthy / 3 missing_analysis_engine (parsed per-block: healthy = node, host, 8 ghidra checks, jadx); awk registration pairs → all 14 match entry order/values; cli 6.7.0; ev id byte-equal; `status: completed`; sizes 2964/84/16160 in record order; fixture digest `8579…be27e`; three record digests; S506 body `ce2d122b…` 16650 bytes — all match |
| Q12 | n/a | no rejected row load-bearing; S506/S507 tier A, status mined, no flip cited |
| Q13 | n/a | no verifier credited as mutation-guarding any clause; `recheck:` names re-executable procedures only |
| Q14 | n/a | no hex-with-length clause, no truncation, no ASCII rendering (grep over entry bytes) |
| Q15 | n/a | no `X:path` tree identity sentence; revision `12f6e09…` asserted inside a fetched-and-byte-verified URL, not a tree identity |
| Q16 | PASS | awk output enumerates 14 registrations → 4 aligned + 8 missing + 1 manual + 1 stale = count and members match the entry sentence; scope_checks per-block parse → exactly the eight ghidra names healthy (of 11); `grep -ci 'binwalk\|unblob' …rea-doctor-r98.txt` → 0, so "doctor has no binwalk or unblob check" is true against the record bytes |
| Q17 | n/a | no relocation adjudication; every cited path resolves in the `git archive` freeze extraction (4488 files listed) |

## Exit codes observed

- Every derivation command: exit 0, outputs byte-equal to the entry.
- `audit_source_quotes.py verify --sid S506`: exit 0.
- Fresh S506 URL fetch: HTTP 200.
- No command in this audit failed.

## Vote

`reports/round-98/votes/ReviewerGate.json` (strict JSON, verified by reload):
12 PASS, 5 n/a, 0 FAIL; `candidate_sha256` = the digest above;
`artifact_path = .ufo/waves/round-98/w1/ReviewerGate/gate-audit.md`;
`artifact_sha256 = 00b6a9935c0e52024fbd4453d81cf69e7744e685a9d4ebb2dd6139334fb3b4cc`
(sha256 of the audit file's committed bytes, matching).

## Tooling record

No tools installed or upgraded (nothing needed; host python3/curl/git/coreutils
sufficed). No writes outside the seat's wave dir, vote file, this findings file
and scratch `/fast/scratch/hyaku/revenger-r98/ReviewerGate/` (deleted on exit).
