# CriticR93 attack receipts

Each row is one attempt built in scratch from the freeze base and run through the frozen v2
counter with `--tree`. Raw outputs: `receipts/<NAME>.txt`. Driver: `attacks/attack.py`,
`attacks/attacks.py`, `attacks/attacks2.py`, `attacks/attacks3.py`.

| attempt | what it does | counter | verdict | failing legs / note |
|---|---|---|---|---|
| A0 | honest control, stubbed lint/embedded | C1 | pass | control |
| A0 | honest control | C2 | pass | control |
| A1 | two seats, one shared artifact file and sha | C1 | pass | not caught |
| A2 | artifact path traversal to corpus/SOURCES.md and opens.json | C1 | pass | not caught |
| A3 | fabricated seats in registry, bound junk artifacts | C1 | pass | not caught (self-attested registry) |
| A3b | battery F1 shape, no artifact fields | C1 | fail | C1_VOTES (control) |
| A4 | zero-byte artifacts | C1 | pass | not caught |
| A5 | artifact = swarm-registry.json | C1 | pass | not caught |
| A6 | oracle_check.py replaced by a printer | C1 | pass | not caught (oracle unpinned) |
| A6b | truth.json rewritten | C1 | pass | not caught (unpinned input) |
| A7 | opens.json stale fixture sha, record sha correct | C1 | fail | C1_OPENS |
| A8 | S495 opened 2026-11-04 in SOURCES | C1 | fail | C1_SOURCES |
| A9 | body-only S901 rejected row, beyond line 15 | C1 | pass | not caught |
| A10 | header rejected, body admission-status: admitted | C1 | pass | not caught (ADMITTED scans whole file) |
| A11 | rejected entry named in C08 | C1 | fail | C1_ADMITTED; K line printed 10/15 |
| A12 | no entry file, C08 held citing knowledge/seed.md | C1 | fail | many legs; C1_K_HELD_BACKED=pass, K line 10/15 |
| A13 | lowercase seats vs registry case | C1 | fail | C1_VOTES |
| A14 | tilde-only fabricated output, real checker | C1 | fail | C1_EMBEDDED (real checker exit 2, fail-closed) |
| A14b | mixed fence: honest ``` plus fabricated ~~~ | C1 | pass | not caught |
| A15 | C08 held plus C02 moved to held (backed) | C2 | fail | C2_ONLY_C08 (sole failing leg) |
| A16 | zero-byte entry file, C08 held citing it | C2 | pass | not caught (token-level) |
| A17 | one PASS plus 16 n/a reason "-" | C1 | pass | not caught |
| A18 | honest-shaped entry, real lint/embedded | C1 | fail | C1_LINT, C1_EMBEDDED (thin entry, not a forgery) |
| A19 | registry deleted on honest tree | C1 | fail | C1_VOTES (intended) |
| A19 | registry deleted on honest tree | C2 | pass | C2 unaffected |
| A20 | lowercase registry key added, honest votes | C1 | pass | benign control |
| A21a | one real seat cast as ReviewerGate and reviewergate | C1 | pass | not caught |
| A21b | one real seat cast as ReviewerGate and "ReviewerGate " | C1 | pass | not caught |
| A23 | external header row, no receipt | C1 | fail | C1_QUOTES (control) |
| A27 | block whose only output line is whitespace | C1 | pass | not caught |
| A28 | entry author ScribeEntry votes as reviewer | C1 | pass | not caught |
| A29 | executor-role seat ExecOracle votes as critic | C1 | pass | not caught |
| H0 | honest lint-clean entry, real lint/embedded (control) | C1 | pass | control |
| H0 | honest lint-clean entry (control) | C2 | pass | control |
| R1 | real tools: header rejected, duplicate admitted line | C1 | pass | not caught |
| R2 | real tools: body-only S901 rejected | C1 | pass | not caught |
| R3 | real tools: case-variant duplicate seat | C1 | pass | not caught |
| R4 | real tools: mixed fence | C1 | pass | not caught |
| R5 | real tools: whitespace-only output | C1 | pass | not caught |
| R6 | real tools: forged oracle_check.py | C1 | pass | not caught |
| R7 | real tools: artifact traversal to corpus | C1 | pass | not caught |
| R8 | real tools: 1 PASS + 16 n/a "-" | C1 | pass | not caught |
| R9 | real tools: every bypass at once, header rejected, K line 10/15 | C1 | pass | C1_VERDICT=pass with ADMITTED=pass |
| R9 | same tree | C2 | pass | C2 token/record legs pass |

Counter kills in total: A3b, A7, A8, A11, A12, A13, A14, A15, A19 (C1), A23, A18 (not a forgery).
Counter passes on forgeries: A1, A2, A3, A4, A5, A6, A6b, A9, A10, A14b, A16 (C2), A17, A21a, A21b,
A27, A28, A29, R1-R9 (C1 R9 also C2). A20 and H0 are controls.

Frozen-control receipts (scratch runs, read-only): `c1 --self-test` SELFTEST_C1V2=pass; `c2 --self-test`
SELFTEST_C2V2=pass; `battery --stage full` BATTERY_VERDICT=pass (V1_REACH_C2=5/5, V2_KILLS=9/9,
POS_C1V2=pass, POS_C2V2=pass, DO_NOTHING_C2=fail); `battery --stage v1-only` BATTERY_VERDICT=pass.
Receipts: `receipts/c1_selftest.txt`, `receipts/c2_selftest.txt`, `receipts/battery_full.txt`,
`receipts/battery_v1only.txt`.

## Q-gate receipts (critic vote on ScribeEntry/entry-draft.md)

Candidate digest, admission-status normalised: `0db16a56fb0c2346d7109999dd6d98123403a52fa67d189112ba5597860593da`
(recomputed from the draft bytes; the status line is `admission-status: candidate`, so raw and normalised bytes agree).

Re-runs (read-only; `python3 -B`, cwd the lane root; nothing written in the lane; no scratch created):
- Seven `transcript` one-liners (draft lines 65, 83, 104, 120, 136, 154, 170): rc 0, stdout equal to the printed block lines in every case (6, 11, 5, 6, 9, 7, 4 lines).
- Oracle block (`$ python3 -B corpus/fixtures/browser-r77/oracle_check.py ...`): rc 0, 18 of 18 printed lines equal; last line `ORACLE OK (17/17 checks)`.
- `git rev-parse 02050cb2a6758e3bd9cec696ff0e42df6f23511a^{commit}` prints the same id; `git diff --quiet 02050cb2a6758e3bd9cec696ff0e42df6f23511a -- corpus` exits 0.
- `corpus/fixtures/browser-r77/oracle_check.py` exits 1 on any failing check (lines 14-16, 201), so the draft's item 26 exit claim holds.

Not verifiable at vote time:
- `corpus/SOURCES.md` at 02050cb has no S495 or S496 row; `reports/round-93/quote-receipts/` does not exist; the S496 quote was not re-fetched here.

Q11 gaps (counts without a derivation command in the entry):
- `(15 words)` for the S496 quote (draft line 340; the count is correct, 15 words).
- `The stdout line count of the oracle block is 18` (draft line 375; the count is correct, 18 lines).
All other counts in the entry re-derived by the re-runs above and matched.

Limit noted: `corpus/check_embedded_outputs.py` replays only `$ ` blocks; the seven transcript blocks are replayed by hand here only (the draft's item 26 says so).

## Q-gate second pass (entry normalised digest 53083246d5528eab8682f5938e4f1b0967683ae883499d15d702d9f671bd1fb1)

Re-checked against the working tree (read-only runs, `python3 -B`; no lane writes; scratch created and removed):
- Digest: recomputed on the landed entry; status line is `admitted` in the file and normalises to `candidate`; digest equals 53083246….
- Q01 (sources): `corpus/SOURCES.md` S495 and S496 rows: status `mined`, opened `2026-11-05`, used-by the entry path. `audit_source_quotes.py verify --sid S496`: `state=verified (ok)` against `reports/round-93/quote-receipts/S496.receipt.json`. S495 is own-work with no quote receipt (the verifier reports it unresolved; the counter's C1_QUOTES checks only http rows, and it passes). The S496 anchor's HTTP Last-Modified `Wed, 04 Nov 2026 04:38:14 GMT` and etag `6aeab6b6-8a86` are recorded verbatim in that receipt (line 11).
- Q11 (counts): the two earlier counts without derivation (`(15 words)`, `line count ... 18`) are gone from the entry; a pattern search for `words`, `line count` and `N lines` finds nothing. Re-run: all seven transcripts equal their printed lines; the oracle block equals its 18 printed lines.
- Q15 (git identity): `git rev-parse 02050cb2…^{commit}` still prints 02050cb2…. But `git diff --quiet 02050cb2… -- corpus` now exits 1: `corpus/README.md`, `corpus/SOURCES.md` and `corpus/knowledge/round-92-managed-assembly-metadata-evidence.md` differ from 02050cb2…. The entry's verified-at sentence says that command is silent and that the whole corpus tree is byte-identical, so the sentence is false as written. The narrower subtree the entry reads (`corpus/live` and `corpus/fixtures`) is identical: `git diff --quiet 02050cb2… -- corpus/live corpus/fixtures` exits 0.
- Frozen C1 counter on the working tree (`--tree`): `C1_K_HELD_BACKED=10/15`, `C1_ADMITTED=pass`, `C1_SOURCES=pass`, `C1_QUOTES=pass`, `C1_OPENS=pass`, `C1_LINT=pass`, `C1_EMBEDDED=pass`, `C1_VOTES=fail` (no landed votes yet in `reports/round-93/votes/` at the time of the run). `C1_VERDICT=fail` is therefore expected before votes land.

## Q-gate third pass (entry normalised digest 1304008c5a0aff9dbb9af09967e12caeef028b1ca52e14dac7b8fe0247e43647)

Re-checked against the working tree (read-only, `python3 -B`, no lane writes, no scratch):
- Digest recomputed on the landed entry (status line `admitted`, normalises to `candidate`): 1304008c….
- Q15: `git rev-parse 02050cb2…^{commit}` prints 02050cb2…. The entry's scoped sentence names `git diff --quiet 02050cb2… -- corpus/live corpus/fixtures`, which exits 0 (silent), matching its claim that the records and fixtures are byte-identical. The sentence no longer claims whole-corpus identity; it says the index and registry files changed at landing and are not claimed identical. Note, not a defect: `corpus/knowledge/round-92-managed-assembly-metadata-evidence.md` also differs from 02050cb2…, and the sentence does not name it; it makes no claim about it.
- Q11: no new counts; pattern search for `words`, `line count`, `N lines`, `N bytes` finds none; all seven transcripts and the 18-line oracle block re-run equal to their printed lines.
- Q01: S495 and S496 rows unchanged in substance (mined, opened 2026-11-05, used-by the entry); S496 quote receipt verified previously.
