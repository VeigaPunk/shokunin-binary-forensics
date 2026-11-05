# ReviewerGate — round-95 gate vote (C1 admission)

Vote: **PASS-bound** — `vote.json` written with candidate_sha256
`476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9`, decisions
PASS on Q01, Q02, Q04, Q09, Q10, Q11, Q15, Q16; n/a on Q03, Q05, Q06, Q07, Q08,
Q12, Q13, Q14, Q17 (each n/a carries a ≥6-token note with a Q cross-reference).
Artifact: `.ufo/waves/round-95/w1/ReviewerGate/evidence.md`, sha256
`ce1f94eb3d037cc2555f265c6c1e37f8a25b600c59c9918c290cfe5a57133890` (see vote.json
for the authoritative value; the artifact names both the seat and the digest).

Identity ground: working-tree entry bytes == freeze commit `6e0bf15…` bytes
(sha256sum equal); digest recomputed from the wave-context recipe by me.

Non-author verification performed before voting (read-only beyond my wave dir):
receipt bodies re-hash to their frozen `fetch_sha256` values, receipt spans decode
byte-exactly to the ≤25-word quotes, and an independent refetch of both
raw.githubusercontent.com pinned URLs (S500/S501, REA `12f6e09…`) reproduced
lengths 17010/18784 and both digest values. Corner anchors checked line-for-line
in refetched sources: `evidence.ts:148` confidence enum, `:121–128` authority
vocabulary; `EvidenceLedger.ts:58/74` idempotent record + conflict rejection;
`evidenceBundle.ts:444–464/543–569` qualification incl. rank `{inferred:1,
derived:2, observed:3}`; `residualUnknown.ts:65–70` verified branch;
`evidenceCompletionLedger.ts:15–27` ECL statuses; issue pages #21/#50/#73 carry
the credited contract sentences ("Secrets and arbitrary environment values never
enter evidence.", "…typed truncation/limit errors rather than evicting evidence
silently.", "Inference cannot satisfy observed authority."). Adjacent-methodology
phrases located on the arXiv/Richards/Frontiers/ED sources at their stated dates.

Gate instrument state at vote time: v4 counter self-test run by me —
`SELFTEST_C1V4=pass legs=24` rc 0; frozen controls match claims.md (do-nothing rc
1; red-v3 10/10 with the r94 M6 mutant surviving v3; full battery 10/10 kills,
mutant dies on v4, `BATTERY4_VERDICT=pass`). Entry mechanics: lint rc 0; embedded
checker rc 2 `could-not-evaluate: no $ cmd blocks` (the frozen C1_EMBEDDED leg
reads exactly this shape as clean); `audit_source_quotes.py verify` →
`rows=2 verified=2` rc 0; README C10 knowledge-file set parses to exactly the one
admitted entry with status `held`; only one `admission-status: candidate` line in
the frozen head window; superseded r74 candidate byte-preserved at `rejected`
(not re-fetched this round beyond S500/S501, as `verified-at` states).

Frozen-instrument residuals carried honestly (deny none, fix none): the receipt
legs attest committed-byte honesty; real opening proof remains the non-author
closure (my refetch above exercises it for S500/S501 at the pinned revision); the
entry is documentation-only with no C1_OPENS leg, so C1_QUOTES+C1_RECEIPTS carry
the opening evidence per the frozen claim wording. No causes were needed beyond
the frozen tables; no scratch predicates hardcode /tmp; every seat Python call
here used `python3 -B`; no lane file, no git/jj write, no subagent, no
`agent://all`.

Scratch `/fast/scratch/hyaku/revenger-r95/ReviewerGate/` deleted on exit
(receipt-relevant pointers now live in this report and the artifact).

## Report

- verdict: gate vote filed (see above).
- findings: none — no post-freeze byte drift encountered in any frozen surface I
  checked; the constraints-of-record all reproduce.
