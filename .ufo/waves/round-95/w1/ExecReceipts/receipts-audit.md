# ExecReceipts — round-95 w1 — frozen receipts chain audit (S500/S501)

Seat: ExecReceipts (executor, read-only over the lane). Date: 2026-11-05.
Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Lane HEAD at audit time:
`6e0bf15fed58f357b7fa0c881371ac7616a116f7` (the freeze commit).
Scope: the frozen quote-receipt chain for the two 2026-11-05 drift-check rows S500/S501
claimed in `reports/round-95/claims.md` (C1 `C1_RECEIPTS` leg inputs). All reads; one
instrument run; one independent field-audit script run. No lane file touched.

## Command 1 — frozen instrument verify (from the lane root)

```
PYTHONUTF8=1 python3 -B corpus/audit_source_quotes.py verify --sources corpus/SOURCES.md \
  --receipts reports/round-95/quote-receipts --sid S500 --sid S501
```

rc = **0**. Full stdout:

```
S500 terminal=S500 state=verified (ok)
S501 terminal=S501 state=verified (ok)
SUMMARY rows=2 verified=2 unreachable=0 unresolved=0
```

Notes: `terminal==sid` for both rows — expected: the rows carry no `supersedes` chain
(the task pre-declares terminal==sid). The instrument's `check_verified` additionally
re-verified (both `ok`): body sha256 == `fetch_sha256`, body length == receipt `length`,
body is utf-8, normalized quote occurs in the normalized body, span in bounds, and
`norm(body[span]) == norm(quote)`. Registry linkage resolves (rows found; receipt sid ==
terminal sid).

## Command 2 — independent field audit (script in this wave dir)

Script: `.ufo/waves/round-95/w1/ExecReceipts/receipts_field_audit.py`
Run: `PYTHONUTF8=1 python3 -B .ufo/waves/round-95/w1/ExecReceipts/receipts_field_audit.py`
(from the lane root). rc = **0**, `FIELD_AUDIT_VERDICT=pass`. Full output:

### S500

| check | verdict | detail |
|---|---|---|
| fetched_at == 2026-11-05 | PASS | receipt='2026-11-05' |
| http_status == 200 | PASS | receipt=200 |
| fetch_url host allowed | PASS | host='raw.githubusercontent.com' |
| sha256(body) == fetch_sha256 | PASS | 69fe22454e4dd4721aeba2c697dc8cf414f3be4630c3d41db491821f39465b8f |
| length == len(body) | PASS | receipt=17010 actual=17010 |
| fetch-log line names sid + sha | PASS | `- S500 GET https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/src/domain/evidence.ts -> HTTP 200, 17010 bytes, sha256 69fe…` |
| [extra] strict JSON, no dup keys | PASS | strict JSON ok |
| [extra] receipt sid == requested sid | PASS | receipt='S500' |
| [extra] schema == revenger-quote-audit-v1 | PASS | receipt='revenger-quote-audit-v1' |
| [extra] verdict == verified | PASS | receipt='verified' |
| [extra] body sha == frozen claims sha | PASS | matches claims.md `69fe22…5b8f` |
| [extra] body length == frozen claims length | PASS | 17010 == 17010 |
| [extra] body non-empty and utf-8 decodable | PASS | bytes=17010 |

### S501

| check | verdict | detail |
|---|---|---|
| fetched_at == 2026-11-05 | PASS | receipt='2026-11-05' |
| http_status == 200 | PASS | receipt=200 |
| fetch_url host allowed | PASS | host='raw.githubusercontent.com' |
| sha256(body) == fetch_sha256 | PASS | f7add697322f37d7a7d69fde5e8e2c3d625344b67fb1ca32dc52dbe6bb103dac |
| length == len(body) | PASS | receipt=18784 actual=18784 |
| fetch-log line names sid + sha | PASS | `- S501 GET https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/src/application/investigation/EvidenceLedger.ts -> HTTP 200, 18784 bytes, sha256 f7ad…` |
| [extra] strict JSON, no dup keys | PASS | strict JSON ok |
| [extra] receipt sid == requested sid | PASS | receipt='S501' |
| [extra] schema == revenger-quote-audit-v1 | PASS | receipt='revenger-quote-audit-v1' |
| [extra] verdict == verified | PASS | receipt='verified' |
| [extra] body sha == frozen claims sha | PASS | matches claims.md `f7add6…3dac` |
| [extra] body length == frozen claims length | PASS | 18784 == 18784 |
| [extra] body non-empty and utf-8 decodable | PASS | bytes=18784 |

Named-field score: 6/6 per sid; overall 26/26 rows PASS (6 named + 7 extra context rows × 2).

## Command 3 — freeze-integrity: receipt chain bytes vs freeze commit

`git show 6e0bf15fed58f357b7fa0c881371ac7616a116f7:<path> | sha256sum` vs
`sha256sum <worktree path>` (read-only git):

| path | verdict | sha256 (identical both sides) |
|---|---|---|
| reports/round-95/quote-receipts/S500.receipt.json | FREEZE-EQ | 9a0320e16cba51e8bb00df61943d3820beda4ead5cbe54ac700544d6cb81b412 |
| reports/round-95/quote-receipts/S501.receipt.json | FREEZE-EQ | c359e26e57c2affc2f46811fbe7a0f6b834017f5f2506eb963c756130dca362e |
| reports/round-95/quote-receipts/raw/S500.body | FREEZE-EQ | 69fe22454e4dd4721aeba2c697dc8cf414f3be4630c3d41db491821f39465b8f |
| reports/round-95/quote-receipts/raw/S501.body | FREEZE-EQ | f7add697322f37d7a7d69fde5e8e2c3d625344b67fb1ca32dc52dbe6bb103dac |
| reports/round-95/quote-receipts/fetch-log.md | FREEZE-EQ | 61f12cc8b0896cf5b8516f18194ff71578d395222901f6b7a2604d37add98f9b |

All five receipt-chain files are byte-identical to the freeze commit: the receipts are
unmodified frozen bytes, and the raw bodies hash to exactly the shas pinned in the frozen
claims.md.

## Command 4 — registry-row state (context, factual)

- `git show 6e0bf15…:corpus/SOURCES.md | grep -cE '\bS50[01]\b'` → `0`: the freeze commit
  does not contain the S500/S501 rows.
- `git status --porcelain -- corpus/SOURCES.md` → ` M corpus/SOURCES.md`: the working tree
  carries L1-staged S500 (line 517) / S501 (line 518) rows not yet committed.
- `git status --porcelain -- reports/round-95/quote-receipts` → empty (clean, matches HEAD).

Consistent with claims.md wording "appended at landing": HEAD is still the freeze commit;
the L1 owns SOURCES.md staging. Not a receipts-chain defect; recorded as observation only.
No repair performed (seat is read-only).

## Verdict

- Instrument leg (C1_QUOTES shape over the new rows): **PASS** (rc 0, 2/2 verified,
  terminal==sid as pre-declared).
- Independent field audit: **PASS** (13/13 rows per sid; every named predicate holds).
- Freeze integrity: **PASS** (5/5 files byte-identical to 6e0bf15; body hashes equal the
  frozen-claims-pinned shas; lengths equal).

**Findings against the frozen claims: NONE.** No mismatch found; nothing repaired.

## Artifacts

- This report: `.ufo/waves/round-95/w1/ExecReceipts/receipts-audit.md`
- Audit script: `.ufo/waves/round-95/w1/ExecReceipts/receipts_field_audit.py`
- Findings copy: `.ufo/waves/round-95/w1/ExecReceipts.md`

Scratch `/fast/scratch/hyaku/revenger-r95/ExecReceipts` was created per spec, unused (no
scratch-side writes needed), and deleted on exit. Every seat Python invocation used
`python3 -B` with `PYTHONUTF8=1`; no `__pycache__` created by this seat. No installs; no
network beyond reads of committed bytes; no git/jj write commands (read-only
`rev-parse`/`show`/`status`/`sha256sum` only).
