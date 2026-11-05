# ExecReceipts — round-95 w1 — findings (receipts chain audit)

**Verdict: receipts chain consistent with the frozen claims. Findings: NONE.**

Seat ExecReceipts, 2026-11-05, lane HEAD = freeze commit `6e0bf15fed58f357b7fa0c881371ac7616a116f7`.

Evidence (full record: `.ufo/waves/round-95/w1/ExecReceipts/receipts-audit.md`):

1. Frozen instrument, from lane root: `PYTHONUTF8=1 python3 -B corpus/audit_source_quotes.py verify --sources corpus/SOURCES.md --receipts reports/round-95/quote-receipts --sid S500 --sid S501` → rc 0; `S500 terminal=S500 state=verified (ok)`; `S501 terminal=S501 state=verified (ok)`; `SUMMARY rows=2 verified=2 unreachable=0 unresolved=0`. terminal==sid as pre-declared (no supersession chain).
2. Independent field audit (`python3 -B` script `.ufo/waves/round-95/w1/ExecReceipts/receipts_field_audit.py`): rc 0, `FIELD_AUDIT_VERDICT=pass`, 13/13 rows PASS per sid — fetched_at==2026-11-05, http_status==200, fetch_url host `raw.githubusercontent.com` (allowed set), sha256(committed raw body)==fetch_sha256 (S500 `69fe22…5b8f` @17010 B; S501 `f7add6…3dac` @18784 B), length==byte length, and `fetch-log.md` lines naming each sid + its sha. Extras all PASS: strict JSON (no dup keys), sid/schema/verdict sanity, body sha+length equal the values pinned in frozen claims.md.
3. Freeze integrity: all 5 receipt-chain files (2 receipts, 2 raw bodies, fetch-log.md) byte-identical to freeze commit 6e0bf15 (`git show … | sha256sum` == worktree sha256sum); raw bodies hash to exactly the claims-pinned shas.
4. Observation (not a finding): working-tree `corpus/SOURCES.md` is `M` vs HEAD with L1-staged S500/S501 rows (lines 517–518, 0 hits at the freeze commit) — consistent with claims.md "appended at landing"; L1-owned file, untouched by this seat.

Per-field pass/fail tables, exact commands, rc values and sha evidence are in
`.ufo/waves/round-95/w1/ExecReceipts/receipts-audit.md`. Nothing repaired; read-only seat.
