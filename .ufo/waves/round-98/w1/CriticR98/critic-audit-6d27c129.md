# CriticR98 critic audit: C14 candidate, digest 6d27c129e6ec3bbd3699c84c0a06301d7aea88140e54a1ff8d8b34d5c0c5330f

Seat: CriticR98 (role critic). Candidate: `corpus/knowledge/round-98-rea-host-readiness.md` at lane commit 1b76b4d (Amendment C). Supersedes `critic-audit-73f1d7e0.md` (digest 73f1d7e0…), which stays as recorded.

Digest recomputed by this seat: `6d27c129e6ec3bbd3699c84c0a06301d7aea88140e54a1ff8d8b34d5c0c5330f` (normalized sha256). Equal to the amendment value.

Method: re-audit of the bytes changed between 0146c0a and 1b76b4d (`git diff 0146c0a 1b76b4d -- corpus/knowledge/round-98-rea-host-readiness.md`), then the entry's counts, attributions and Q decisions. Read-only commands on the lane's saved records and on the 1b76b4d `corpus/` extract. No counter run on any tree with C14 held.

## Changed bytes

| Change | Re-derivation | Result |
|---|---|---|
| Derivation preamble replaces "Every value above was derived…" with "Every count, identifier and digest stated above is derived below …" | see the two open items below | Still over-broad. See Q11 and Q16. |
| Preamble: "Version strings and exit codes are not derived here. Each comes from the probe transcript `host-probes-r98.txt`, where every command line is followed by its printed output and an `rc=` line." | `$ ` lines = 13, `rc=` lines = 13, and each `$` is followed by output then `rc=` before the next `$` (checked by awk: 0 unpaired). Version strings: `12.1.4` occurs 0 times in the transcript and 17 times in the doctor record; `21.0.13`, `6.7.0`, `1.5.6`, `3.1.0`, `26.6.4` occur in the transcript. | The structure claim holds. The attribution does not for `ghidra-version 12.1.4`, which the entry states as a version string and which is not in the transcript. |
| Preamble: doctor exit code 1 and inspect exit code 0 "were observed in the L1 session and are not lines of any record" | the doctor and inspect records carry no exit line | Accurate and honest. Q05 holds: the ZIP capability row is carried by its Evidence ID. |
| New row: client registration count `grep -c '^    - client:'` → `14` | run → `14` | Matches. |
| New row: registration state split `awk … \| uniq -c` → `4 aligned / 1 manual / 8 missing / 1 stale` | run → `4 aligned`, `1 manual`, `8 missing`, `1 stale` | Matches. |
| New row: "missing-or-stale registrations" → `9` | run → `9` | Matches. |
| Q06 changed to PASS with the truth.json cross-check | `sha256sum` 857989f5…, equal to truth.json `archive_sha256` | Agreed: PASS. |

## Open items

**Q11 (FAIL, narrow).** The route table states "Doctor lists three such installation paths (`state: multiple`)". The row that should derive it is `grep -c '^    paths\[3\]: ' … ` and `grep -c '^    state: multiple' …`, which print `1` and `1`. Neither prints 3. The `paths[3]` label is doctor's own count field, but the entry neither derives the 3 nor labels it recorded. A command that derives it, checked here: `grep '^    paths\[3\]: ' corpus/live/runs/round-98/rea-doctor-r98.txt | cut -d: -f2 | tr ',' '\n' | grep -c .` → `3`. QUALITY Q11 rejects a count without its deriving command. Every other count in the route table (14; 4/8/1/1; nine; eight ghidra; eleven and thirteen; 24; three missing engines) is now derived.

**Q16 (FAIL).** The preamble credits the probe transcript with the version strings ("Each comes from the probe transcript"). `ghidra-version 12.1.4` is stated in the Native decompile row and is not printed by the transcript; it is printed by the doctor record. The credit reaches past what the transcript prints. The same preamble's "every count, identifier and digest … is derived below" is the Q16 credit that the three-installation-paths count (Q11 above) does not meet.

## Decisions (this seat)

| Q | Decision | Evidence |
|---|---|---|
| Q01 | PASS | S506 body unchanged, ce2d122b…, 16650 bytes; span 7126–7202 equals the quote; receipt fetched_at 2026-11-05 at the SOURCES URL |
| Q02 | PASS | head lines carry S506, S507, verified-at, recheck, coverage-map C14, admission-status; no header moved |
| Q03 | PASS | `truth.json` members 84 and 16160 and archive 857989f5… equal the record values; comparison by this seat |
| Q04 | PASS | rea 6.7.0 = transcript `rea --version` and doctor cli_package_version; jadx 1.5.6, openjdk 21.0.13, binwalk 3.1.0, unblob 26.6.4 = transcript rc=0 lines; ghidra 12.1.4 is scored from the doctor output that prints it, labelled configuration |
| Q05 | PASS | ZIP row carries command, date, Evidence ID ev_0ef6c8cd…, present in the saved inspect record; the exit 0 is disclosed as session-observed |
| Q06 | PASS | archive-r2 fixture sha256 857989f5… equals truth.json archive_sha256; the producer call ran on these bytes |
| Q07 | n/a | no parser prediction or cause is offered |
| Q08 | n/a | superseded by Q11 per QUALITY.md |
| Q09 | PASS | digests bind exact bytes; origin and authenticity disclaimed |
| Q10 | PASS | one host, one date, one ZIP route; other routes marked configured, unprobed or absent |
| Q11 | FAIL | the "three such installation paths" count is not derived by its row (the row prints 1 and 1); see Open items |
| Q12 | n/a | no rejected source row is cited or load-bearing |
| Q13 | PASS | recheck names re-derivation procedures; no verifier credited as guarding a clause |
| Q14 | PASS | no hex run quoted with a byte count in one clause; the lint Q14 count on 1b76b4d is 0 |
| Q15 | PASS | only pinned identity is REA 12f6e09, a prefix of the S506 fetch_url id; lint Q15 on 1b76b4d is 0 |
| Q16 | FAIL | the preamble's transcript attribution does not cover `ghidra-version 12.1.4`; see Open items |
| Q17 | n/a | no adjudication relocated a cited path |

## Checks run on 1b76b4d (corpus extract, C14 `partial` in its README)

`LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0 LINT_HEADER=0`, `lint rc=0`. README C14 row at 1b76b4d: `partial`.

## Vote

Decisions are in `reports/round-98/votes/CriticR98.json`, bound to 6d27c129…, artifact this file. FAIL on Q11 and Q16 fails `C1_VOTES`, and therefore C1, per the claims. Both FAILs are recorded as they stand. The fix for Q11 is the one command above (or a `recorded` label on the 3); the fix for Q16 is to drop `ghidra-version 12.1.4` from the transcript credit or cite the doctor record for it.

Not run by this seat: any counter on a tree with C14 held; the v7 counter; the non-author closure admission still needs (LEARNING.md).
