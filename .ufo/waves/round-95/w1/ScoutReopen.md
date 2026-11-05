# ScoutReopen — round 95 w1 — scoped findings

Seat: `ScoutReopen` (scout). Scope: independent non-author re-fetch and drift check of
the two source rows C1 rests on (S500, S501), and the drift verdicts against the S098 /
S096 scope cells in `corpus/SOURCES.md`.

Read-only with respect to every lane file. Nothing under `corpus/`, `reports/`, or any
lane index was created, edited, or deleted by this seat; no git write command was run.
All writes are confined to this seat's wave dir `.ufo/waves/round-95/w1/ScoutReopen/`
and this report file. Scratch was created and then deleted.

## Verdicts (one line each)

- **S500 re-fetch: `match`** — HTTP 200, 17010 bytes, sha256 `69fe22454e4dd4721aeba2c697dc8cf414f3be4630c3d41db491821f39465b8f`, equal to the pinned sha in `reports/round-95/claims.md` and byte-identical (`cmp`) to the committed `reports/round-95/quote-receipts/raw/S500.body`.
- **S501 re-fetch: `match`** — HTTP 200, 18784 bytes, sha256 `f7add697322f37d7a7d69fde5e8e2c3d625344b67fb1ca32dc52dbe6bb103dac`, equal to the pinned sha and byte-identical (`cmp`) to the committed `reports/round-95/quote-receipts/raw/S501.body`.
- **S098 scope cell vs current `evidence.ts`: `no-drift`** — `evidenceAuthoritySchema` still at L122–128 with the same five named authorities; `confidence: z.enum(["observed","derived","inferred"])` and `authority: evidenceAuthoritySchema` still at L148–149.
- **S096 scope cell vs current `EvidenceLedger.ts`: `no-drift`** — class comment still at L53; `record` doc comment at L58 with body through L77 (dedupe L71–73, `EvidenceIntegrityError` on conflict L74, add L76–77); `clear` still at L399–401.
- **No drift found; no repair needed and none attempted** (drift is reported, never repaired).

Full detail with located evidence lines: `.ufo/waves/round-95/w1/ScoutReopen/reopens.md`.
Fetched bodies: `.ufo/waves/round-95/w1/ScoutReopen/receipts/raw/S500.body` and `S501.body`.
Fetch log with HTTP status: `.ufo/waves/round-95/w1/ScoutReopen/receipts/fetch-log.md`.

## Cross-checks (read-only)

- Both receipt JSONs (`http_status: 200`, `fetched_at: 2026-11-05`, host
  `raw.githubusercontent.com`, `verdict: verified`) are consistent with the refetched bytes;
  each receipt's `length` and `fetch_sha256` re-verify against the refetch, and each
  receipt's `span` bytes are exactly its `quote` (S500 `[3149,3223)`, S501 `[2136,2198)`).
- The committed `reports/round-95/quote-receipts/fetch-log.md` names both sids with both
  shas, satisfying the frozen `C1_RECEIPTS` leg's log-naming requirement.
- The superseding entry's two S500/S501 claims are supported by the refetched bytes
  (entry L37 ← S500 L122–128/L148–149; entry L38 ← S501 L58–78).
- The entry's working-tree bytes equal the freeze commit's bytes
  (`6e0bf15fed58f357b7fa0c881371ac7616a116f7:corpus/knowledge/round-95-evidence-ledger-discipline.md`),
  both sha256 `476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9` — which is
  also the digest the votes bind under the `admission-status: candidate` normalizer.
- `HEAD` is the freeze commit; `git status --porcelain` shows only the untracked
  `.ufo/waves/round-95/` tree.

## Notes for the L1 (observations, no action taken here)

- `corpus/SOURCES.md` currently ends at `S499`; the S500/S501 rows are **not yet in the
  file**. The frozen claims place their append at **landing**, so the absence pre-landing
  is the expected state, not a defect — verified by reading the file, not assumed.
- `corpus/lessons/round-95.md` does not exist yet (L1 writes it at landing), so the
  `## Gate` quotes the claim text points at are not yet locatable in the lane. The two
  receipt quotes are locatable in the committed bodies and are the bytes any Gate quote
  must agree with.
- Anchor-precision nit (not drift): S096's `clear` anchor range is L399–401, while
  `clear()`'s body clears three maps (`#records` L401, `#unknownRevisions` L402,
  `#unknownHeads` L403). The row's "teaches" text stays true; the anchor range points at
  the method and its doc comment. Worth noting when S500/S501 are appended at landing.

## Housekeeping

- Scratch `/fast/scratch/hyaku/revenger-r95/ScoutReopen/` was created and **deleted**
  before this report; the receipts were copied into the wave dir first.
- Every Python invocation used `python3 -B`; no `__pycache__` was produced under
  `corpus/`, `reports/round-95/`, or `.ufo/waves/round-95/`.
- No tools installed, no sudo, no host sysctl touched, no `agent://all`, no subagent
  dispatch (leaf seat).
- Network use limited to the two URLs named in this task's spec
  (`raw.githubusercontent.com/morluto/rea` at the pinned revision).
