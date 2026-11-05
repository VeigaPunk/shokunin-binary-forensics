# CriticR93 — round-93 attack report

Scoped findings for the attack seat. Full ranked findings with repro commands:
`.ufo/waves/round-93/w1/CriticR93/findings.md`. Attempt receipts: `.ufo/waves/round-93/w1/CriticR93/evidence.md`
(raw outputs under `.ufo/waves/round-93/w1/CriticR93/receipts/`; driver scripts under `.../CriticR93/attacks/`).

Tooling: no install. Read-only use of the frozen counters and the lane tree; all trees built in scratch
from `git archive 281a5bad66e844190a570cb35d257c6974749993`; scratch removed before yield. No frozen file edited.

Headline numbers (attempts run: 40+; each counter verdict and failing legs recorded):
- C1 counter passes 25 forgery attempts: 16 with stubbed lint/embedded (A1-A6b, A9, A10, A14b, A17, A21a/b, A27-A29) and 9 with real lint and real embedded checker (R1-R9, including R9, which carries every bypass with the header `admission-status: rejected`: `C1_VERDICT=pass`, `C1_K_HELD_BACKED=10/15`).
- C1 counter kills 9 attempts (A3b, A7, A8, A11, A12, A13, A14, A19 C1-side, A23) for the reasons in findings.md.
- C2 counter: kills A15 (second row moved, `C2_ONLY_C08`); passes A16 (zero-byte entry, token-level).
- Battery: green in scratch (`BATTERY_VERDICT=pass`, `V2_KILLS=9/9`, `POS_C1V2=pass`, `POS_C2V2=pass`).

Top findings (ranked in findings.md):
1. C1_ADMITTED scans the whole file: a rejected entry with a duplicate `admission-status: admitted` passes the verdict.
2. The vote registry is self-attested; the battery F1 kill is incidental (killed by missing artifact fields).
3. One real seat counted as several (case and trailing-space variants); author self-votes and role mismatches pass.
4. Artifact binding is sha equality only: shared, empty, registry-as-artifact, and path-traversal artifacts all pass.
5. The oracle script and truth.json are unpinned; a forged oracle passes C1_OPENS.
6. Source citations in the body (after line 15) are never checked.
7. Whitespace-only output and mixed fences defeat the embedded-output legs.
8. C2_ONLY_C08 has no committed control; the C2 positive accepts an empty entry (token-level only).
9. Q-gate n/a reasons are unconstrained (1 PASS + 16 "-" passes).
10. The K line is not admission-gated; only the verdict is.
11. Real-tools positive control is absent from POS_C1V2 (lint and embedded stubbed).
12. Process: the wave registry is untracked at lane HEAD; the L1 must commit the wave bytes for C1 --rev.

Answers to the brief: (a) 10/15 without an admitted entry: verdict pass (R9). (b) second row moved while
passing POS: rejected (A15), but no committed control exercises that leg. (c) deleting the registry does
not kill POS_C1V2 (self-test uses its own fixture); C2 unaffected; C1 refusal is intended.

Vote: CAST on the draft `.ufo/waves/round-93/w1/ScribeEntry/entry-draft.md` (candidate_sha256 `0db16a56fb0c2346d7109999dd6d98123403a52fa67d189112ba5597860593da`). Vote file `.ufo/waves/round-93/w1/CriticR93/vote.json`; artifact `.ufo/waves/round-93/w1/CriticR93/evidence.md` (sha256 `86138e9f0ed6aa017e8a33cf30bcc2b7c5798b8cc89938f4552507fd8298fa49`). 11 PASS; 6 n/a with reasons, including Q01 and Q11 marked n/a as "NOT PASSED" because the schema has no FAIL value (see the notes in vote.json).
