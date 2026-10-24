# W2VerifyLedger — LEDGER.md discipline verification (revenger-r63 falsify wave 2)

Seat: `revenger-r63.W2VerifyLedger` · 2026-10-24 · lane repo `/home/vgpnk/Projects/shokunin/revenger-shokunin`
Target: `corpus/live/runs/round-63/LEDGER.md` as committed at tip `2a34e45` (worktree `git status --porcelain` on `corpus/live/runs/round-63` + `corpus/fixtures/firmware-r63`: clean; both LEDGER.md and receipt.json last touched by `2a34e45`).
Method: every counting command re-run from scratch (python re-derivation + re-execution of the two cited checks); no repo bytes modified; all scratch under `/tmp/revenger-r63-ledger-*`, removed after this report.

## Verdict

**One leak located; all other assigned checks HOLD.**

- **LEAK L1 (Q09):** LEDGER.md "Fixture and route" table, Receipt row quotes `receipt.json` SHA-256 `e930a549db16a180d4ab05307e073cd71599a3317b9f3d15a0d97843d5c6b94b`, but the committed bytes hash to `e930a549db16a180d4ab05307e073cd71599a3317b9f3d15a0d97843d5c6b94d` (last hex char `b` vs `d`). The quoted digest is not the digest of the bytes it is attached to. Cause not determinable from the tree: no reconstructed earlier shape (compact/indent-2/sorted/no-duration/rounded-duration/newline-stripped variants) hashes to the quoted value → stale or transcription typo. Scope note: only the route-table file digest is wrong; the receipt's inner field bindings (O9) all verify (below), so the C2(b) receipt fields themselves are intact.
- **Residual wording (non-blocking):** LEDGER.md line 9 still reads "explicit zero padding" (no count/position). The corrected precise form is present at both load-bearing spots: O6 (three spans `offset 0 size 512`, `offset 591 size 433`, `offset 1114 size 934`, fill `00`, "all-zero at those spans") and U1 ("three all-zero padding spans"). Byte-verified: all three spans are all-zero and tile 0→2048. No factual error at line 9; recommend harmonizing to "three all-zero padding spans" at next edit.

## Check matrix

| # | Assigned check | Result | Evidence |
|---|---|---|---|
| 1 | O/I/U separation | **HOLDS** | Ledger table parses to 11 OBSERVATION + 6 INFERENCE + 6 UNKNOWN = 23 rows, zero malformed class labels. Spot-audit: O-rows state only saved bytes/fields (O9 says "internally consistent", not "authentic"); I-rows carry scope bounds (I1 "fixture-scoped", I5 "engine must always be named"); U-rows keep questions open. |
| 2 | Every named digest = exact bytes it hashed | **1 of 11 fails — L1 above** | Recomputed: generator.py `4e5d5975…93db4` ✓, truth.json `9663f90b…a65e6` ✓, firmware-r63.bin `bdfe9f46…510be` ✓, inspection.json = stdout.raw `f6997835…71f9` ✓ (3904 B each), stderr.txt `e3b0c442…855` ✓ (0 B), member0 `image[512:591]` `bf3dd2e4…c352` ✓, `/usr/bin/binwalk` `5fc19aac…40d6` ✓, `~/.local/bin/unblob` `0ce7b624…1d09` ✓. `oracle_check.py` current digest `d0dfd7a1…0512` equals the ledger's "at the time of the check" value; ledger cites it by path+behaviour (disclosed non-pin), so no violation. receipt.json ✗ = L1. |
| 3 | No origin/authenticity/completeness claim (Q09) | **HOLDS** | Keyword sweep (`authentic`, `genuine`, `proof of origin`, `complete record`, `trust`) hits only disclaimers: U4 ("does not authenticate that a producer ran at that time… no independent third-party witness") and the F-limits "Cannot see" list ("whether the Evidence ID is genuine"). No hash match is offered as origin/completeness/authenticity proof anywhere. U5 disclaims oracle independence; U2 keeps extraction completeness open. |
| 4 | "three all-zero padding spans" wording | **HOLDS** (residual at L9, see above) | O6 + U1 carry the corrected wording; truth.json declares exactly 3 padding regions; my byte check: `all(set(img[o:o+s])=={0})` = True for (0,512), (591,433), (1114,934). |
| 5 | F-limitation section matches frozen counter | **HOLDS** | Frozen `reports/round-63/measure.py` F block (read at source): `rglob("*.json")` under `corpus/live/runs`, skip unparsable, count top-level dicts with truthy `evidence_id` and `normalized_result is not None`, keyed by `operation` (default `"unknown"`), family = set intersection over 8 families. Ledger's definition sentence matches clause-for-clause. Replication on the real tree: counter `{'inspect_firmware_regions': 1, 'inspect_pe_resources': 30, 'inspect_evm_interface': 7, 'analyze_javascript_application': 6, 'inspect_artifact': 4, …}` → `F_COVERAGE=5/8`, `F_FAMILIES=['archives','evm','firmware','javascript','native-static']`, firmware file = exactly `corpus/live/runs/round-63/inspection.json`, `receipt.json` not counted (has `evidence_id`, no `normalized_result`) — identical to ledger I6 and the "Can see" list. "Cannot see" list verified true by mutation (below). Nuance (non-material): frozen code counts only the top-level JSON object (≤1 increment per file); ledger phrasing "for every dict" is compatible. |

## Cited checks re-executed (O10/O11)

- `oracle_check.py` (cwd=`corpus/live/runs/round-63`): exit 0, last line `ORACLE OK`; five REGION lines — 3× `record=not-expected padding=OK`, 2× zlib `offset=OK size=OK signature=OK decompressed_sha256=OK` with `a5718481…` (78 B) and `2d0d86aa…` (97 B) — matches O10(b) and O6 verbatim.
- Independent recomputation (O10(a) route): `zlib.decompressobj` over `img[512:591]` → 78 B sha `a5718481…` = truth; over `img[1024:1114]` → 97 B sha `2d0d86aa…` = truth. 2/2.
- unblob 26.6.4 (digest-verified binary) re-run in `/tmp` (O11): whole 2048-byte image → exit 0, **0** `ChunkReport`, 0 extracted files; isolated 79-byte member → **1** `ChunkReport`, extracts `zlib.uncompressed` 78 B sha `a5718481…` = truth digest. Matches O11 exactly.
- O9 five cross-checks all True: `stdout_sha256` == sha(stdout.raw) == sha(inspection.json); `fixture_sha256` == sha(image) == subject digest; receipt `evidence_id` == record `evidence_id`; exit_code 0; stderr 0 B. O1/O2/O3/O7 field statements all reproduced (incl. top-level `locations` = one `file-offset-range` 0–2048; `grep -c unblob inspection.json` = 0).

## Forged-evidence scenario (executed, `/tmp` only)

Forged a hand-written `forged_record.json` — fabricated `evidence_id` (`ev_fff…`), `operation=inspect_firmware_regions`, plausible regions, no producer — into a copy of the runs tree: **the frozen F counter counts it** (firmware tick stands, `inspect_firmware_regions: 2`). Confirms the ledger's own admission that F alone is not evidence. Stopping artifacts that prevent credit, in order:

1. **receipt.json stdout binding (O9 / C2(b)):** any forged record's bytes ≠ pinned `stdout_sha256 f6997835…`. Demonstrated: tampering region offset 512→513 gives record sha `8b4c4cac…` ≠ `f699…` → receipt equality chain breaks.
2. **truth.json byte oracle (O10 / C2(c)):** offset 513 → `zlib: incorrect header check`; even a fully self-consistent forged pair (record + receipt with recomputed mutual hashes, which F counts identically) still fails the oracle, because truth values are derived from fixture bytes — a pin outside the record under test (Q03).
3. **claims.md C2(b) real-run requirement + frozen void condition:** the record must be the output of one real `npx -y rea-agents@6.5.0` run with a committed receipt (command/exit/fixture sha/stdout sha/Evidence ID); a fabricated file has no such run, and "any changed `corpus/live` byte outside new round-63 paths" is a frozen void — the counter itself runs on a committed `git archive` tree, so uncommitted forgeries do not exist for it.

## Notes and costs

- No tool installs; used stock `python3` and the pre-existing digest-verified `~/.local/bin/unblob` 26.6.4. No pacman (paused). No repo file modified; no target executed (decompression only).
- Time-box honored; every assigned axis closed on committed bytes.
