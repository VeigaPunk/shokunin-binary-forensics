# ReviewerR92Gate — round 92 wave 1 — Q-gate vote on the C1 entry

Seat: ReviewerR92Gate (reviewer, leaf). Lane: revenger-shokunin.
Entry: `corpus/knowledge/round-92-managed-assembly-metadata-evidence.md`
READY: `.ufo/waves/round-92/w1/ScribeR92Entry/READY`, `sha256=2c96e633fc730d218560b9693b881ffdeb1244cad5ac77f5fb6626f494306fb6`
— equals this seat's recomputed sha256 of the entry bytes AND the
admission-status-normalised digest (the entry says `admission-status: candidate`;
normalisation is therefore the identity here, and the digest survives the L1's
admitted flip unchanged). Vote file: `reports/round-92/votes/ReviewerR92Gate.json`
(written only after READY existed), candidate_sha256 = `2c96e633…06fb6` (no prefix).

## Checks run (all evidence in `.ufo/waves/round-92/w1/ReviewerR92Gate/`)

1. **READY wait.** Three bounded polls (40×30 s, 40×30 s, 20×30 s ≈ 50 min);
   the first two timed out — the scribe seat produced nothing observable until
   10:33, then landed SOURCES.append.md and READY at 10:36. ReviewerR92Blind's
   bounded wait expired before READY and that seat did not vote; this seat's vote
   is therefore currently the only reviewer vote in `reports/round-92/votes/`
   (C1_VOTES needs ≥ 2 — the wave must land a second vote file or the leg fails).
2. **Sources re-opened (Q01/Q02).** All four URLs re-fetched by this seat
   (curl, HTTP 200, byte counts identical to ScoutR92Managed's snapshots):
   S491 ECMA-335 6th ed. PDF 4 982 145 B; S492 5th ed. PDF 7 238 968 B;
   S493 PE Format 281 747 B (ms.date 2026-09-10); S494 MetadataRootBuilder
   63 589 B (ms.date 2025-07-01). All 13 quoted clauses located verbatim:
   7 in S491, 3 in S492 (pdftotext, whitespace-normalised), 1 in S493
   ("208/224 8 CLR Runtime Header …", tag-stripped offset 27023), 2 in S494
   (stream-set sentence offset 3781; "The metadata version." for the
   MetadataVersion property). Edition markers verified ("6th Edition / June 2012",
   "5th Edition / December 2010"). All ≤ 25 words. → `quote-location.log`.
   SOURCES.append.md rows S491–S494: 11 cells each, tier A, status `mined`,
   opened 2026-11-05, used-by names the entry — the shape `C1_SOURCES` checks.
3. **Embedded commands (Q11/Q16).** All 11 fenced `$ cmd` blocks re-run from the
   lane root by this seat's own re-implementation (not only
   `corpus/check_embedded_outputs.py`): rc 0 × 11, every embedded output line
   present verbatim in stdout, zero drift; the four distinct stdout line counts
   are 11/21/48/40 exactly as the entry states. The corpus checker agrees:
   `checked_blocks=11 problems=0`, exit 0. → `recheck-blocks.log`, `recheck_blocks.py`.
4. **Fixtures (Q06).** Both committed generators re-run in this seat's scratch:
   self-check OK, regen byte-identical (r76 924 B `25ece37d…`, r85 1048 B
   `94429fa4…`). Both committed oracles re-run from the lane root: r76
   `ORACLE OK (10/10)`, r85 artifact `ORACLE OK (20/20)`, members 47/47,
   boundaries 39/39 (members/boundaries via ExecR92Producer's receipts and the
   entry's own embedded blocks, all re-derived here). → `regen-r76.log`, `regen-r85.log`.
5. **Git identity (Q15).** `git rev-parse 9402183a^{commit}` →
   `9402183a9492428fa0064d250746c62a0a2d9ca5`; `git diff --quiet 9402183a -- corpus`
   silent — both claims in `verified-at:` hold on the current tree.
6. **Mechanical gates.** `corpus/lint_entry.py` → LINT_QMAP=0 Q14=0 Q15=0
   HEADER=0, exit 0. Q-map carries a row for every criterion Q01–Q17 (Q08 marked
   superseded by Q11, per QUALITY.md).
7. **Scope / O-I-U (Q10).** Entry is fixture-scoped ("Nothing here is a claim
   about .NET, about the CLI format family at large"), separates Observation
   (items 1–9) / Inference (10–14) / Unknown (15–20) / Limitations (21–27); the
   v4.0.30319-vs-"Standard CLI 2005" divergence is reported as unknown, not
   explained; `#Guid`/`#GUID` casing preserved; no producer-readiness claim
   (rea 6.8.0 appears only as recorded receipt data). The entry avoids the
   cross-host byte-identity trap this wave exposed (ExecR92Producer D1: the
   r85 records' `evidence_id` covers host-specific absolute paths, so records
   are semantically identical, not byte-reproducible, across hosts).

## Defects

- **D-G1 (editorial, erratum per RevengerR92 ruling):** the `recheck:` header
  line cites "the three sibling commands in §8"; no §8 exists — the commands
  live in the unnumbered §Reproduce. The credit itself is true (this seat
  re-ran all three; they do re-derive the entry's numbers), so Q02/Q16 are
  PASS with the defect named in the vote notes. Bytes frozen as voted; fix
  routed to the entry's next revision, recorded in the round-92 lesson.
- **D-G2 (context, not an entry defect):** this host's `rea --version` is
  6.7.0 while the receipts record 6.8.0; ExecR92Producer correctly re-ran via
  `npx rea-agents@6.8.0`. The entry claims no current-host producer state, so
  this does not touch it.
- **D-G3 (wave risk):** only one reviewer/critic vote file exists at write time
  (this one). `C1_VOTES` requires ≥ 2 distinct seats; ReviewerR92Blind timed
  out pre-READY. If no second vote lands, C1 fails on votes regardless of this
  gate's verdict.

## Verdict

Q01–Q04, Q06, Q07, Q09–Q11, Q13–Q17 PASS; Q05, Q08, Q12 n/a (reasons in vote
notes); no FAIL. **ADMIT** — all criteria PASS or n/a on the voted bytes
(`2c96e633fc730d218560b9693b881ffdeb1244cad5ac77f5fb6626f494306fb6`).
Decision I would reject: none of the entry's 17 Q-map decisions; what I would
reject is silently repairing the §8 pointer post-vote (invalidates every vote
against the frozen digest) — erratum-and-next-revision is the right route.
No subagent spawned; no mutating git/jj command; no frozen file touched; no
tool installed (pacman pause respected). Scratch
`/fast/scratch/hyaku/revenger-r92/ReviewerR92Gate/` deleted before yielding.
