# ReviewerBlind — blind derivation for the frozen C1 admission (round 95, wave 1)

Seat: ReviewerBlind (reviewer). Candidate: `corpus/knowledge/round-95-evidence-ledger-discipline.md`.
Candidate digest (wave recipe: sha256 of entry bytes with every case-insensitive
`admission-status:` line replaced by `admission-status: candidate`):

```
476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9
```

## Blind method and byte binding

Files read (nothing else, no other seat's files, no gate/instrument bytes, no
receipt JSONs): `reports/round-95/quote-receipts/raw/S500.body`,
`reports/round-95/quote-receipts/raw/S501.body`,
`corpus/knowledge/2026-10-29-rea-evidence-ledger-discipline.md`,
`corpus/SOURCES.md` rows S096–S109 and S002, and the candidate entry.

- Working-tree entry bytes equal the freeze-commit bytes
  (6e0bf15fed58f357b7fa0c881371ac7616a116f7): `git show <rev>:<entry> | sha256sum`,
  the file's plain `sha256sum`, and the recipe digest are all
  `476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9`
  (normalization is identity here — the file's single `admission-status:` line
  is already `candidate`).
- Receipt bodies re-hash to the values frozen in claims.md:
  S500.body 17010 bytes sha256 `69fe22454e4dd4721aeba2c697dc8cf414f3be4630c3d41db491821f39465b8f`;
  S501.body 18784 bytes sha256 `f7add697322f37d7a7d69fde5e8e2c3d625344b67fb1ca32dc52dbe6bb103dac`.
  Every quote below is located in those committed bytes.

## Five-layer derivation table

| # | Layer | Candidate claim (compressed) | Source anchor | Located quote (≤25 words) | Mismatches |
|---|---|---|---|---|---|
| 1 | Evidence record schema | each record carries subject digest/format, provider, parameters, raw/normalized results, `confidence` ∈ {observed, derived, inferred}, `authority`, limitations, locations, and an `evidence_id` | S098/S500 → S500.body L139–153 | `confidence: z.enum(["observed", "derived", "inferred"]),` (L148); `evidence_id: prefixedDigestSchema("ev")` (L139) | 0 |
| 2 | Session ledger record/dedup/clear | session-owned in-memory set; idempotent `record`; dedups by Evidence ID; rejects conflicting content; clears when the owning session closes | S096/S501 → S501.body L53–77, L399–403 | `/** Record evidence idempotently; conflicting content is rejected. */` (L58); `/** Clear records when the owning session closes. */` (L399) | 0 |
| 3 | Residual-unknown verified qualification | revisioned unknowns with supporting/contradicting Evidence IDs, required authority/confidence/environment; `verified` only with qualifying evidence | S097/S100/S102 (rows; no new raw body this round) | S100 row quote: "Only qualifying observed evidence can verify a resolution."; S102 row quote: "Inference cannot satisfy observed authority." | 0 (row-consistency) |
| 4 | Verifier completion ledger | a separate `ecl_` ledger binds each `claim_id` to status ∈ {pass, fail, unsupported, truncated, unknown} and ≥1 Evidence ID | S108 (row; byte-level not re-derivable blind) | S108 row claim: "Each verifier claim binds a status to at least one Evidence ID in an `ecl_` ledger." | 0 (row-consistency) |
| 5 | Agent working rule | cite Evidence IDs; preserve limitations/coverage; do not treat a miss in partial Evidence as absence; export before session close | S100/S002 (rows) | S100 row claim: "Incomplete Evidence does not prove absence" | 0 (row-consistency) |

Total mismatches: 0.

## Drift-check verification (the two 2026-11-05 re-opens)

- S500 (re-open of S098): `evidenceAuthoritySchema = z.enum([` at body L122 with
  values `shipped-artifact`, `controlled-replay`, `historical-reference`,
  `external-service`, `analyst-inference` (L123–127); `confidence` L148,
  `authority` L149. The S098 row anchor ("evidenceAuthoritySchema L122–128;
  confidence/authority L148–149") matches the committed bytes line-for-line —
  the enum and the authority vocabulary are unchanged at the pinned commit.
- S501 (re-open of S096): class comment L53 `/** Session-owned set of immutable
  evidence records. */` over `#records`/`#unknownRevisions`/`#unknownHeads`
  Maps (L55–57); `record` L59–77 with dedup at L73 (`ok("duplicate")`) and
  conflict rejection at L74 (`err(new EvidenceIntegrityError("Conflicting
  evidence record"));`); `clear` L400–403 emptying all three Maps, comment at
  L399 and store-clears at L401–403. The S096 row anchor ("Class comment L53
  and `record` L58–77; `clear` L399–401") matches the committed bytes.

## Corroboration inside the blind bytes

- S501.body L380–396 (`verifyUnknownResolution`): `truthVerified:
  unknown.resolution?.disposition === "verified"` (L394) — resolution
  disposition semantics present in the same session-ledger bytes, consistent
  with layer 3.
- S501.body L139–140, L274 (`Conflicting evidence record` also on the import
  and atomic-record paths) — conflicting-content rejection is systemic, not a
  single-line accident.
- S500.body L138–153: the full `evidenceBaseSchema` block shows
  `raw_result: jsonValueSchema.nullable()` (L146), `normalized_result`
  (L147), `limitations: z.array(z.string())` (L151), `locations` (L152) —
  every field layer 1 names exists; `slash-command`-style extras the entry does
  not claim (analysis_profile, environment, relationship_coverage) are
  additional, not contradictory.

## Not re-derivable from the blind bytes (coverage gaps, not mismatches)

- Layers 3–5 byte-level: only S500/S501 were re-opened this round by design;
  S097/S099/S100/S102/S108/S002 primary bytes are not in the blind set. My
  check there is candidate-claim vs SOURCES-row claim/anchor/quote
  consistency, which holds with zero contradictions.
- S108's five-value status enum and S002's skill lines 313–314/350 are outside
  the blind set — unverified here, uncontradicted by anything read.

## Verdict

Zero mismatches across all five ledger layers; both drift-check rows verified
against the committed re-open bodies at their pinned line anchors. This blind
derivation SUPPORTS admission of the candidate at digest
`476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9`.
