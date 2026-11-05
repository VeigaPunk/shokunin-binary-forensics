# CriticR98 critic audit: C14 candidate, digest 73f1d7e044df04373a36c1f94f7e7216a7a513043ef769d5567a98cb53dd80e7

Seat: CriticR98 (role critic). Candidate: `corpus/knowledge/round-98-rea-host-readiness.md` at lane commit 0146c0a (Amendment B). Supersedes my audit `critic-audit.md` (digest 1ea9260c…), which stays as recorded.

Digest recomputed by this seat: `73f1d7e044df04373a36c1f94f7e7216a7a513043ef769d5567a98cb53dd80e7` (normalized sha256, admission-status lines set to `admission-status: candidate`). Equal to the amendment value.

Method: re-audit of the bytes changed between cf8a9d4 and 0146c0a (`git diff cf8a9d4 0146c0a -- corpus/knowledge/round-98-rea-host-readiness.md`), then the full entry against Q01 to Q17. Read-only commands on the lane's saved records. Lint run on a `git archive` extract of 0146c0a, whose README still has C14 `partial`; no counter run on any tree with C14 held.

## Changed bytes

| Change (diff hunk) | Re-derivation | Result |
|---|---|---|
| Route table, ZIP row: "Hopper was absent during this run" → "Doctor reported Hopper missing the same day (record 1)" | `hopper` is `ok: false`, `missing_analysis_engine` in the doctor scope list. The record files carry no date line; "same day" rests on the S507 prose that the three records were produced on 2026-11-05. | Accurate. Dating is prose-supported, not record-supported. Not a Q05 issue (the ZIP row's date is in its command line of the entry). |
| Observation sentence: "at a time when doctor reported Hopper missing" → "on the same day that doctor reported Hopper missing" | same as above | Accurate, same basis. |
| Derivation row added: "ghidra scope checks healthy" with `grep -A1 '^  - name: ghidra' ... grep -c '    ok: true'` → `8` | run on `corpus/live/runs/round-98/rea-doctor-r98.txt` | output `8`. Matches. |
| Derivation row added: "installation paths" with `grep -c '^    paths\[3\]: '` and `grep -c '^    state: multiple'` → `1` and `1` | run | outputs `1` and `1`. Matches. |
| Derivation row added: "S506 body length" `wc -c < .../S506.body` → `16650` | run | `16650`. Matches. The S506 digest row lost its byte count from the same clause (Q14 hygiene). |
| `## §Q-map` appended, 17 rows | lint on 0146c0a extract | `LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0 LINT_HEADER=0`, rc 0. The blocking lint defect from my first audit (F1) is resolved. |

## Still open

**Q11 (FAIL).** The new rows derive the ghidra count and the installation-path lines. The route table still states "Of 14 client registrations, doctor reports 4 `aligned` ..., 8 `missing`, 1 `manual` ... and 1 `stale`" (entry line 58), and the Observation still says "nine stale or missing client registrations" (line 88). No derivation row counts these. The registration derivation row prints the listing only. I re-derived the values by hand (14; aligned 4; missing 8; manual 1; stale 1; nine = 8 + 1); the values are right, the derivation is absent. QUALITY Q11 rejects a count without its deriving command.

**Q16 (FAIL).** Line 64 still reads "Every value above was derived from the saved record by the command shown. The outputs are the commands' actual stdout." The credit covers the registration counts and the nine-sum, which no printed command output compares. The credit reaches past what the commands print.

The entry's own Q-map marks Q11 and Q16 PASS. This seat does not accept those self-assessments for the reasons above.

## Q-map decisions in the entry, checked

- Q06 is marked n/a ("no fixture was authored or edited this round"). That is the wrong reason: Q06 applies to premises verified before a producer call, and the ZIP route is a producer call on this fixture. The premise does hold (archive sha256 857989f5… equals `truth.json` archive_sha256; members match). This seat votes PASS on Q06 and records the mis-stated n/a here.
- Q15 is marked n/a. This seat votes PASS: the only pinned identity is REA `12f6e09`, the seven-hex prefix of `12f6e0974cc0db0b3a9b86246accc76556837222` in the S506 receipt's fetch_url. Lint Q15 is 0.
- Q13 is marked n/a. This seat votes PASS for the same reason (recheck lines name re-derivation targets and credit no verifier).

## Full decision table (this seat)

| Q | Decision | Evidence |
|---|---|---|
| Q01 | PASS | S506 body unchanged, ce2d122b…, 16650 bytes; span 7126–7202 equals the quote; receipt fetched_at 2026-11-05 at the SOURCES URL |
| Q02 | PASS | head lines carry S506, S507, verified-at, recheck, coverage-map C14, admission-status; the amendment moved no header |
| Q03 | PASS | `truth.json` members 84 (7d8f6a8d…) and 16160 (f5ba0697…) and archive 857989f5… equal the record; the comparison is this seat's, not the table's |
| Q04 | PASS | rea 6.7.0 = doctor cli_package_version; jadx 1.5.6, openjdk 21.0.13, binwalk 3.1.0, unblob 26.6.4 = host-probes rc=0 lines; Ghidra 12.1.4 is configuration, not re-run |
| Q05 | PASS | ZIP row carries command, date, exit and Evidence ID ev_0ef6c8cd…, present in the saved inspect record; doctor and version rows labelled configuration |
| Q06 | PASS | archive-r2 fixture sha256 857989f5… re-derived; see Q06 note above on the entry's n/a |
| Q07 | n/a | no parser prediction or cause is offered; route results are recorded observations |
| Q08 | n/a | superseded by Q11 per QUALITY.md |
| Q09 | PASS | digests bind exact bytes (fixture, record files, S506 body); origin and authenticity disclaimed |
| Q10 | PASS | one host, one date, one ZIP route; other routes marked configured, unprobed or absent |
| Q11 | FAIL | see Still open |
| Q12 | n/a | no rejected source row is cited or load-bearing |
| Q13 | PASS | recheck names re-derivation targets; no verifier credited as guarding a clause |
| Q14 | PASS | no hex run quoted with a byte count in one clause; the S506 digest clause no longer carries a count; lint Q14=0 on the 0146c0a extract |
| Q15 | PASS | only pinned id is REA 12f6e09, a prefix of the S506 fetch_url id; lint Q15=0 |
| Q16 | FAIL | see Still open |
| Q17 | n/a | no adjudication relocated a cited path |

## Vote

Decisions are in `reports/round-98/votes/CriticR98.json`, bound to 73f1d7e0…, artifact this file. Two FAIL decisions (Q11, Q16) fail `C1_VOTES`, and therefore C1, per the claims. They are recorded as they stand.

Not run by this seat: any counter on a tree with C14 held; the v7 counter; the non-author closure that admission still needs (LEARNING.md).
