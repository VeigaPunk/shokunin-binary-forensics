# ScoutReopen — round 95 w1 — independent re-fetch + drift check (C1's two sources)

Seat: `ScoutReopen` (scout). Role in this wave: non-author re-fetch of the two source
rows C1 rests on (S500, S501), plus a drift check of the scope cells they re-verify
(S098, S096). Read-only with respect to every lane file; nothing under `corpus/`,
`reports/`, or any lane index was created, edited, or deleted by this seat.

Fetch date: 2026-11-05 (UTC clock read `2026-11-05T17:35:37Z`).
Host: Linux 7.2.11-arch1-1 x86_64. Method: `curl -sf` with `%{http_code}` captured;
no retry — both fetches succeeded on the first attempt.

## 1. Re-fetch verdicts

| sid | url | HTTP | bytes | observed sha256 | pinned sha256 (claims.md) | committed receipt body sha256 | verdict |
|---|---|---|---|---|---|---|---|
| S500 | `https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/src/domain/evidence.ts` | 200 | 17010 | `69fe22454e4dd4721aeba2c697dc8cf414f3be4630c3d41db491821f39465b8f` | `69fe22454e4dd4721aeba2c697dc8cf414f3be4630c3d41db491821f39465b8f` | `69fe22454e4dd4721aeba2c697dc8cf414f3be4630c3d41db491821f39465b8f` | **match** |
| S501 | `https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/src/application/investigation/EvidenceLedger.ts` | 200 | 18784 | `f7add697322f37d7a7d69fde5e8e2c3d625344b67fb1ca32dc52dbe6bb103dac` | `f7add697322f37d7a7d69fde5e8e2c3d625344b67fb1ca32dc52dbe6bb103dac` | `f7add697322f37d7a7d69fde5e8e2c3d625344b67fb1ca32dc52dbe6bb103dac` | **match** |

`cmp` of the refetched bytes against the committed
`reports/round-95/quote-receipts/raw/S{500,501}.body`: **byte-identical** for both.
No drift, therefore no repair is required and none was attempted (drift is reported,
never repaired — this seat holds no lane write authority).

Fetched bodies live in this wave dir:
`receipts/raw/S500.body`, `receipts/raw/S501.body`.
Fetch log with HTTP status: `receipts/fetch-log.md`.

### Receipt-field cross-check (independent, against the refetched bytes)

| sid | receipt `length` == refetched byte count | receipt `fetch_sha256` == refetched sha256 | receipt `span` bytes == receipt `quote` |
|---|---|---|---|
| S500 | yes (17010) | yes | yes — bytes [3149, 3223) are exactly `Source authority vocabulary owned by Evidence and reused by its consumers.` |
| S501 | yes (18784) | yes | yes — bytes [2136, 2198) are exactly `Record evidence idempotently; conflicting content is rejected.` |

Receipt JSON fields observed and consistent with the frozen claims: `http_status: 200`,
`fetched_at: 2026-11-05`, `fetch_url` host `raw.githubusercontent.com`, `verdict: verified`,
`schema: revenger-quote-audit-v1`. The committed `reports/round-95/quote-receipts/fetch-log.md`
names both sids with both shas, as the frozen `C1_RECEIPTS` leg requires.

## 2. Drift verdicts vs the S098 / S096 scope cells (`corpus/SOURCES.md`, read-only)

### Row S098 — scope cell "Evidence v2 confidence and authority vocabulary at commit 12f6e09";
anchors `evidenceAuthoritySchema` L122–128; `confidence`/`authority` L148–149

**Verdict: `no-drift`.**

Located evidence lines in the refetched `S500.body` (line numbers are the body's own
1-based lines, and they agree exactly with the scope cell's anchors):

```
122  export const evidenceAuthoritySchema = z.enum([
123    "shipped-artifact",
124    "controlled-replay",
125    "historical-reference",
126    "external-service",
127    "analyst-inference",
128  ]);
...
148      confidence: z.enum(["observed", "derived", "inferred"]),
149      authority: evidenceAuthoritySchema,
```

The confidence enum is still exactly the three members the cell claims
(`observed`/`derived`/`inferred`), the authority field is still bound to
`evidenceAuthoritySchema`, and the named-authority vocabulary still carries the same
five members. The cell's claim — "Evidence records distinguish observed/derived/inferred
confidence and named authorities" — holds in the current bytes.

### Row S096 — scope cell "Session-owned EvidenceLedger record/import/clear contract at commit 12f6e09 only";
anchors Class comment L53, `record` L58–77, `clear` L399–401

**Verdict: `no-drift`.**

Located evidence lines in the refetched `S501.body`:

```
53  /** Session-owned set of immutable evidence records. */
54  export class EvidenceLedger {
...
58    /** Record evidence idempotently; conflicting content is rejected. */
59    record(input: Evidence): RecordResult {
...
71        if (existing === evidence) return ok("duplicate");
72        return recordsAgree(existing, evidence)
73          ? ok("duplicate")
74          : err(new EvidenceIntegrityError("Conflicting evidence record"));
75      }
76      this.#records.set(evidence.evidence_id, evidence);
77      return ok("added");
78    }
...
399   /** Clear records when the owning session closes. */
400   clear(): void {
401     this.#records.clear();
```

The class comment is at L53 as the cell states; `record` carries its doc comment at L58
and its body through L77 (closing brace L78), so the cell's L58–77 span still names the
whole record contract; `clear` is at L399–401 as the cell states. The record semantics the
cell claims are intact: dedupe by `evidence_id` (L66, L71–73), conflicting content rejected
with `EvidenceIntegrityError` (L74), added on success (L76–77), and clearing tied to the
owning session (L399–401). The cell's "import" wording is still backed elsewhere in the
file — the bundle merge path at L80+ (`/** Validate an entire bundle before atomically
merging its records. */`).

### Anchor-precision observation (NOT drift)

`clear()`'s body clears three maps — `this.#records.clear()` (L401),
`this.#unknownRevisions.clear()` (L402), `this.#unknownHeads.clear()` (L403) — while the
S096 anchor range names only L399–401. The row's *teaches* text ("clears with the owning
session") remains true and is not contradicted by the bytes, and the anchor range
L399–401 does point at the `clear` method and its doc comment. This is an anchor-range
precision nit for the L1 to note when S500/S501 are appended at landing — **not** a drift
verdict, and this seat does not edit `corpus/SOURCES.md`.

## 3. Entry-side cross-check (read-only)

The superseding entry `corpus/knowledge/round-95-evidence-ledger-discipline.md` makes
two claims that the refetched bytes must support:

- line 37 — "S500 … confirms the confidence enum and the source-authority vocabulary are
  unchanged in the current bytes": supported by S500.body L122–128 and L148–149.
- line 38 — "S501 … confirms `record` stays idempotent with conflicting-content rejection
  in the current bytes": supported by S501.body L58–78 (doc comment L58, dedupe L71–73,
  conflict rejection L74).

Additional phrases located verbatim in the refetched bodies:
`confidence: z.enum(["observed", "derived", "inferred"])`, `authority: evidenceAuthoritySchema`,
`export const evidenceAuthoritySchema = z.enum([` (all S500);
`/** Session-owned set of immutable evidence records. */`,
`Record evidence idempotently; conflicting content is rejected.`,
`err(new EvidenceIntegrityError("Conflicting evidence record"))`,
`/** Clear records when the owning session closes. */` (all S501).

## 4. Freeze-commit byte check (read-only)

`git -C <lane> show 6e0bf15fed58f357b7fa0c881371ac7616a116f7:corpus/knowledge/round-95-evidence-ledger-discipline.md | sha256sum`
and `sha256sum corpus/knowledge/round-95-evidence-ledger-discipline.md` both give
`476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9` — the working-tree
entry bytes equal the freeze commit's bytes. That value is also the digest the votes
bind (the digest normalizer over `^\s*admission-status\s*:.*$` → `admission-status: candidate`,
case-insensitive, recomputed independently here). `HEAD` is the freeze commit
`6e0bf15fed58f357b7fa0c881371ac7616a116f7`; `git status --porcelain` shows only the
untracked `.ufo/waves/round-95/` tree. No git write command was run.

## 5. Open observations for the L1 (no action taken by this seat)

- `corpus/SOURCES.md` currently ends at `S499`; the S500/S501 rows are **not yet present**
  in the file. The frozen claims describe them as appended **at landing** ("Frontier step"),
  so their absence pre-landing is the expected state, not a defect. Confirmed by reading
  the file rather than assuming.
- `corpus/lessons/round-95.md` does not exist yet (the L1 writes it at landing), so the
  `## Gate` quotes the claim text references are not yet locatable in the lane. The two
  receipt quotes above are locatable in the committed bodies and are the bytes any such
  Gate quote must agree with.
- The `clear()` anchor-precision nit in §2.

## 6. Summary

| check | result |
|---|---|
| S500 re-fetch vs pinned sha | **match** (HTTP 200, 17010 bytes) |
| S501 re-fetch vs pinned sha | **match** (HTTP 200, 18784 bytes) |
| S500/S501 refetch vs committed receipt bodies | **byte-identical** (cmp) |
| S098 scope cell vs current `evidence.ts` | **no-drift** |
| S096 scope cell vs current `EvidenceLedger.ts` | **no-drift** |
| Receipt quote spans vs refetched bytes | **exact match** for both |
| Entry bytes vs freeze commit 6e0bf15 | **identical** (`476edc36…479fb9`) |
| Lane files edited by this seat | **none** |
| Drift requiring repair | **none found** |
