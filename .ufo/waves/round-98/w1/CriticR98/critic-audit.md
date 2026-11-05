# CriticR98 critic audit: C14 candidate

Seat: CriticR98 (role critic). Candidate: `corpus/knowledge/round-98-rea-host-readiness.md` at claims freeze 9d49002a3804de48d365b7d32849ada06745d64f.
Candidate digest (v6 `digest()` rule, recomputed by this seat): 1ea9260c812947d3e2c61161c22a1e143df432168e7b9b5bc4c1a90c0b1527b8. Equal to the claims value.

Method: read-only. The freeze archive was extracted to scratch and checked there; saved records were read in the lane. The entry lint (`corpus/lint_entry.py`) and the quote tool (`corpus/audit_source_quotes.py verify --sid S506`) were run on the freeze copy, which has C14 `partial`. No counter was run on any tree with C14 held. Checks I could not run are named below.

## Evidence re-derived

| Check | Command or method | Result |
|---|---|---|
| Candidate digest | normalized sha256 of the entry text (admission-status lines set to `admission-status: candidate`) | 1ea9260c812947d3e2c61161c22a1e143df432168e7b9b5bc4c1a90c0b1527b8 |
| S506 body | sha256 of `reports/round-98/quote-receipts/raw/S506.body` | ce2d122b873fb84d98cdb56afd84a34ee8de362b65760855838dfb29c2282e50, 16650 bytes |
| S506 quote span | `body[7126:7202] == quote` | True; quote is the 76-byte sentence "Static JavaScript and ordinary ZIP inventory need neither Hopper nor Ghidra." |
| S506 remedy-table quotes | byte search in the body | "Doctor checks registration; it cannot establish the current agent's connection." at 3644; "Inspect the actual shell PATH and launcher/runtime." at 6166; row labels at 3548 and 6100 |
| S506 paraphrase anchor | body lines 35-37 | "Native decompilation, Android analysis and firmware extraction have their own bring-your-own prerequisites." (the entry marks it a paraphrase; accurate) |
| S506 receipt | `reports/round-98/quote-receipts/S506.receipt.json` | fetched_at 2026-11-05, http_status 200, fetch_url equal to the SOURCES S506 URL |
| Quote tool | `python3 -B corpus/audit_source_quotes.py verify --sources corpus/SOURCES.md --receipts reports/round-98/quote-receipts --sid S506` | `SUMMARY rows=1 verified=1 unreachable=0 unresolved=0`, rc 0 |
| Doctor verdict | `sed -n 1,2p corpus/live/runs/round-98/rea-doctor-r98.txt` | `healthy: false` / `environment_healthy: false`; bytes 1-41 (the entry's range) |
| Scope checks | the entry's sed/grep derivation | 11 `ok: true`, 13 `ok: false`; classes 10 config_drift, 11 healthy, 3 missing_analysis_engine (all printed) |
| Registrations | awk derivation in the entry | listing reproduced exactly; counts by reading: 14 total, aligned 4 (codex, devin, grok_build, zcode), missing 8, manual 1 (grok_bot), stale 1 (omp) |
| Ghidra healthy | scope rows | eight ghidra scope checks each `ok: true`, classification healthy |
| CLI and paths | `cli_package_version: 6.7.0`; `installations paths[3]`, `state: multiple`; `skill` `state: stale` | as the entry states |
| Probes | `corpus/live/runs/round-98/host-probes-r98.txt` | rea 6.7.0 rc=0; `command -v analyzeHeadless` empty rc=1; idat64 rc=1; hopper rc=1; `python3 -c 'import pwn'` rc=0; binwalk 3.1.0; unblob 26.6.4; jadx 1.5.6; openjdk 21.0.13 |
| Record digests | `sha256sum corpus/live/runs/round-98/*` | 94eaa6ff1137d0dd… host-probes, fb9a48249a225013… doctor, c373f656932a9c07… inspect; match the entry |
| ZIP inventory | `rea-inspect-artifact-archive-r2.txt` | evidence_id ev_0ef6c8cdbfe9836f2daa149d17269e355f98424d59ecb55398dbe271c6a87382; root sha 857989f5…; declared sizes 2964 / 84 / 16160; `hash_status: verified` on each member; `status: completed` on inventory_artifact |
| Fixture digest | `sha256sum corpus/fixtures/archive-r2/fixture.zip` | 857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e |
| Pinned expected values | `corpus/fixtures/archive-r2/truth.json` (round-2 pin, outside the record) | archive_size 2964; members bin/checksum 16160 sha f5ba0697…, README.txt 84 sha 7d8f6a8d…; all equal the record |
| K05 claim | `corpus/knowledge/2026-10-12-rea-readiness-checklist.md`, `## Re-verification 2026-10-19` (lines 29-47), row K05 "pwntools import fails" | the entry's "corrects the 2026-10-19 re-probe row K05" is accurate. Omitted: the later `## Re-verification 2026-11-04` section (line 61) already records pwntools importing. Not a false claim. |
| Frozen lint | `python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-98-rea-host-readiness.md --lane <freeze>` | `LINT_QMAP=17 [Q01..Q17]`, `LINT_Q14=0`, `LINT_Q15=0`, `LINT_HEADER=0`, rc=1 |
| Frozen lint, control | same command on `corpus/knowledge/round-96-native-analysis-sessions.md` | `LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0 LINT_HEADER=0`, rc=0 |
| Check-embedded | `python3 -B corpus/check_embedded_outputs.py --entry <candidate>` | rc=2 `could-not-evaluate: no $ cmd blocks` (the entry has no fenced command blocks) |

## Blocking defect (C1_LINT)

D1. The candidate has no `## §Q-map` section. The frozen lint reports `LINT_QMAP=17` and exits 1. The round-96 entry has the section and passes. `reports/round-97/c1_k_admit_counter6.py` requires lint rc 0 (leg `C1_LINT`), and the claims keep every v6 leg in the c14 profile. On the entry bytes the claims freeze (digest 1ea9…), C1_LINT fails, so C14 cannot be held. Adding the section changes the digest; the claims bind the digest and say any edit other than the admission-status line invalidates the votes. The claims therefore cannot be met as frozen, and the L1 must decide the amendment.

## Defects (Q criteria)

D2 (Q11). Counts without a derivation command: "eight ghidra scope checks" healthy; "Of 14 client registrations ... 4 aligned ... 8 missing ... 1 manual ... 1 stale"; and "nine stale or missing client registrations" (a sum of those counts). The values are correct on re-derivation (14, 4, 8, 1, 1, eight ghidra rows ok). The derivation table prints the registration listing and the scope classes but no counting command for these counts. QUALITY Q11 rejects a count without its derivation.

D3 (Q16). The entry states "Every value above was derived from the saved record by the command shown." The table's commands print the values they are cited for, but the counts in D2 have no printed output behind them, so the credit reaches past what the commands print.

## Non-blocking notes

N1. The ZIP member comparison with `truth.json` is asserted in prose. The expected side (truth.json values) has no command in the table. Values match on re-derivation (above).
N2. The exit codes of `rea doctor` (1) and `rea inspect-artifact` (0) are stated in prose, not in the saved records. The ZIP capability claim is carried by the Evidence ID and the saved output, so Q05 holds. Doctor is configuration only.
N3. Admission procedure step 1-2: the entry carries no per-criterion decision table, so no per-criterion record exists in the entry itself (see D1).

## Attacks run on the holdout (development set, disclosed)

Frozen v6 on the new c02 holdout (`.ufo/waves/round-98/w1/CriticR98/fresh/`, run 2026-11-05, log `results-c02-fixture.json`): honest control accepted (K 13/15). Five new forgery classes accepted: a FAIL vote saved under `ReviewerBlind.JSON`, a n/a reason made of Q ids, a `recheck: none` header, a Q14 count error in a two-run clause, a coverage-map header naming C05. The held C06 row backed by a candidate entry is refused, incidentally, by `C1_ONLY_C02` and `C1_ADMITTED_UNION`.

## Vote

Decisions are in `reports/round-98/votes/CriticR98.json`. Two FAIL decisions (Q11, Q16) fail `C1_VOTES` and therefore C1, per the claims. The FAILs stand as recorded; they are not narrowed for the counter.

Not run: the v7 counter (not in my scope), any landing-tree counter run, and the non-author closure. The candidate's admission needs that closure (LEARNING.md), which this vote does not provide.
