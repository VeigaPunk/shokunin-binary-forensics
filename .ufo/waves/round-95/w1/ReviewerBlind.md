# ReviewerBlind — round 95 wave-1 scoped findings

Blind-derivation seat for the frozen C1 admission. Full derivation in
`.ufo/waves/round-95/w1/ReviewerBlind/derivation.md`; vote in
`.ufo/waves/round-95/w1/ReviewerBlind/vote.json`.

## Result: supports admission (zero mismatches)

- Candidate digest (wave recipe): `476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9`.
  Working-tree entry bytes == freeze-commit bytes (6e0bf15f) — all three
  hashes (recipe digest, file sha256, `git show` blob sha256) identical.
- Five ledger layers re-derived only from S500.body, S501.body, the superseded
  2026-10-29 candidate, SOURCES rows S096–S109/S002 and the candidate:
  **0 mismatches** on all five layers.
- Receipt bodies re-hash to the claims.md-frozen values byte-for-byte
  (S500 17010 B / `69fe2245…`; S501 18784 B / `f7add697…`).
- Drift-check rows verified at their pinned anchors: S098 row's
  `evidenceAuthoritySchema L122–128` / `confidence/authority L148–149` and
  S096 row's class-comment L53 / `record` L58–77 / `clear` L399–401 all match
  the committed bodies exactly — the observed/derived/inferred enum and the
  five-value authority vocabulary are unchanged at REA `12f6e09`, and
  `record` idempotency plus conflicting-content rejection and session-close
  `clear()` are all present in today's bytes.
- Corroborating bytes inside the blind set: `verifyUnknownResolution`
  (`truthVerified: unknown.resolution?.disposition === "verified"`, L394 of
  S501.body) backs the resolution layer; conflicting-content rejection appears
  on the record (L74), import (L112/L140) and atomic (L274) paths.

## Voting decisions

PASS: Q01, Q02, Q04, Q09, Q10, Q11, Q16. n/a (with ≥6-token Q-referenced
notes in vote.json): Q03, Q05, Q06, Q07, Q08, Q12, Q13, Q14, Q15, Q17.

## Coverage gaps (not defects)

- S097/S099/S100/S102/S108/S002 primary bytes were not re-opened this round by
  design (only S500/S501); layers 3–5 were checked for candidate-vs-row
  consistency only. S108's status enum values and S002's cited skill lines are
  unverified in the blind set, uncontradicted.
- Residual risk: none actionable in the blind scope; full cross-checking of
  receipts/votes/registry belongs to the gate legs, not this seat.
