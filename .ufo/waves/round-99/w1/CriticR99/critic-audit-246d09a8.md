# CriticR99 critic audit: C14 candidate, digest 246d09a8cf6523ab380f88f7945f220338c27e31f8b43ba876bbd0a9a8d746da

Seat: CriticR99 (role critic). Candidate: `corpus/knowledge/round-98-rea-host-readiness.md` at lane commit 9ddd38ac8baef67d689ac36fa233aaaef35b1703 (Amendment B, digest 246d09a8…). Scope: current bytes only; the earlier 36cc6ac2 digest is superseded for this seat's vote. No counter was run on any tree with C14 held. Checks ran on a `git archive` extract of 9ddd38ac (C14 `partial` in its README; not a landing tree).

## Method

1. Digest: sha256 of the entry text with every `admission-status` line normalised to `admission-status: candidate` (v7 `digest()` rule). Result: `246d09a8cf6523ab380f88f7945f220338c27e31f8b43ba876bbd0a9a8d746da`, equal to the amendment value.
2. Derivation table, mechanised: `verify_amend_b.py` (copied to the wave dir) runs every derivation command from the extract root and compares its stdout with the output cell's code spans (annotation after ` — ` dropped, one span per stdout line). Result: `ROWS 29`, every row `EXACT`, `BAD_ROWS 0`. Exit codes observed: 0 on 28 rows; 1 on the `doctor binwalk or unblob checks` row, which the row itself annotates (grep exits 1 on zero matches).
3. Probe transcript: `host-probes-r98.txt` has 13 `$` lines and 13 `rc=` lines, 0 unpaired. Version strings in the entry's transcript credit are present with their probe output: `rea --version` 6.7.0 (rc=0), `binwalk --version` 3.1.0 (rc=0), `unblob --version` 26.6.4 (rc=0), `jadx --version` 1.5.6 (rc=0), `java -version` `openjdk version "21.0.13"` (rc=0). `12.1.4` is not in the transcript and is credited to the doctor record, which prints it (`detail: 12.1.4`).
4. Doctor composition, re-derived: 13 failing scope checks (`ok: false`) = 3 `missing_analysis_engine` (hopper, ida-registration, kuna-installation) + 10 `config_drift` (`skill:identity` and nine registrations: antigravity, claude_code, copilot_cli, cursor, gemini_cli, kimi, omp, opencode, pi). The nine are the `missing`/`stale` states of the registration table (8 missing + omp stale). 11 healthy = 8 ghidra checks + jadx + node + host, each `classification: healthy`.
5. Quotes, S506 body (`reports/round-98/quote-receipts/raw/S506.body`, 16650 bytes, sha256 `ce2d122b…`): "Doctor checks registration; it cannot establish the current agent's connection." at line 22, "Static JavaScript and ordinary ZIP inventory need neither Hopper nor Ghidra." at line 34 (exact line), "Inspect the actual shell PATH and launcher/runtime." at line 26; the receipt span 7126–7202 satisfies `body[7126:7202] == quote`; receipt sha and length match the body; the paraphrased lines 35–37 contain the stated sentence. Receipt `fetched_at` 2026-11-05, host `raw.githubusercontent.com`.
6. Fixture: `corpus/fixtures/archive-r2/fixture.zip` sha256 `857989f5…` equals `truth.json` `archive_sha256` (verifier rows EXACT on both). Inspect record: `root_sha256` equals the same digest; `declared_size` 2964 (root `.`), 84 (`README.txt`), 16160 (`bin/checksum`) equal truth.json members.
7. Historical citation: the entry's "2026-10-19 re-probe row K05, which recorded the import as failing" is correct; line 40 of the checklist sits under `## Re-verification 2026-10-19` (line 29), and that row says `pwntools import fails`. The 2026-11-04 section (line 61) is a later re-probe and is not cited.
8. Registry and S507: the S507 `teaches` cell now says the doctor exit code 1 "is not a line of the record" (0 lines containing `exit` in the doctor record), consistent with the entry.
9. Lint: `corpus/lint_entry.py --entry corpus/knowledge/round-98-rea-host-readiness.md --lane .` prints `LINT_QMAP=0`, `LINT_Q14=0`, `LINT_Q15=0`, `LINT_HEADER=0`. The lint's own exit code was not captured (the run was piped to `tail`); the printed zero counts are the evidence.

## Decisions (this seat)

| Q | Decision | Evidence |
|---|---|---|
| Q01 | PASS | S506 body re-read; receipt span equals the quote; sha256 and length match; SOURCES rows S506 and S507 are tier A and opened 2026-11-05. |
| Q02 | PASS | Header lines carry source S506 and S507 with URL/path and anchor, verified-at 2026-11-05, recheck naming the S506 re-open, `coverage-map: C14`, and `admission-status: candidate`. |
| Q03 | PASS | Expected values come from `truth.json` (round 2): archive sha 857989f5…, members 84 and 16160; compared by this seat after the fact, not used to set the record. |
| Q04 | PASS | Tool, version and function named; each version line printed by its probe with rc=0 in the transcript; doctor 12.1.4 and 21.0.13 credited to the doctor record and derived by row. |
| Q05 | PASS | Only the ZIP row is capability (command, date, exit 0 disclosed, Evidence ID `ev_0ef6c8cd…` present in the inspect record); doctor and version rows labelled configuration; absence rows labelled absent. |
| Q06 | PASS | `sha256sum` of the fixture equals the truth.json archive digest; the producer call premise matches the bytes; no fixture authored this round. |
| Q07 | n/a | Q07 applies only to parser predictions; the entry states none (grep for predict, expect, hypothesis, pre-registered finds only table prose). |
| Q08 | n/a | Q08 is superseded by Q11 in QUALITY.md; the entry applies Q11. |
| Q09 | PASS | Digests bind exact bytes; the entry's scope sentence disclaims origin and authenticity, and this seat treats no digest as provenance. |
| Q10 | PASS | Scope limited to one host (`Linux 7.2.11-arch1-1 x86_64`, transcript line 1), one date, REA 6.7.0, the routes named; firmware and Android are marked capability unprobed. |
| Q11 | PASS | All 29 derivation rows re-run EXACT; the route-table counts (11, 13, 14, 4/1/8/1, nine, eight, three engines, three paths) each have a row. |
| Q12 | n/a | The entry cites no rejected registry row; its load-bearing rows S506 and S507 are mined, not rejected. |
| Q13 | n/a | The entry credits no verifier with guarding any clause; the recheck line names re-derivation targets only. |
| Q14 | PASS | `grep -nE '[0-9a-f]{8,}'` with `byte` finds one line (Q06 row, line 137): the hex run `857989f5…` is ellipsis-truncated and carries no byte count. |
| Q15 | PASS | `grep -o 'rea/12f6e0[0-9a-f]*' reports/round-98/quote-receipts/S506.receipt.json` prints `rea/12f6e0974cc0db0b3a9b86246accc76556837222`, so the pinned revision `12f6e09` is a prefix of that identity. |
| Q16 | PASS | Each output cell matches its command's stdout (29 EXACT); route sentences match transcript lines (`jadx` 1.5.6 at lines 20–22; `binwalk` 3.1.0 at lines 14–16; `unblob` 26.6.4 at 17–19). `reports/round-99/controls/deriv_check.py` exists in the tree. |
| Q17 | n/a | No adjudication relocated a cited artifact in this commit; cited paths resolve in the extract. |

## Findings (none blocks the vote)

- Minor: the S506 SOURCES row anchor states "body bytes 7126-7202" without a base convention; the receipt uses 0-based half-open slicing, which is what the bytes satisfy. Not an entry defect; a one-word convention note would remove the ambiguity.
- Minor: `reports/round-99/controls/deriv_check.py` and `amendB-deriv-check.log` were added after the claims-freeze commit. They sit in the post-freeze controls directory and are cited by Q16; they are not run by any counter, so no score depends on them.
- Process: the amendment's rows were checked by this seat on the extract, not on any landing tree.

## Vote

Decisions are in `reports/round-99/votes/CriticR99.json`, bound to `246d09a8cf6523ab380f88f7945f220338c27e31f8b43ba876bbd0a9a8d746da`, artifact this file. No FAIL decision: C1_VOTES is not failed by this seat on the current bytes.

Not run by this seat: any counter on a tree with C14 held; v8 bytes; the landing tree.
