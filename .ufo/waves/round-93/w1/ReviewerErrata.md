# ReviewerErrata — round-93 w1 report (r92-routed corrections drafted as ready-to-land bytes)

Seat: ReviewerErrata · leaf member (no subagents, no swarm) · lane: revenger-shokunin.
Inputs read in full: `corpus/lessons/round-92-verifier-spotcheck.md` (routed defects 1–4),
`corpus/knowledge/round-92-managed-assembly-metadata-evidence.md`,
`.ufo/waves/round-92/w1/CriticR92Claims/findings.md` (finding 9),
`.ufo/waves/round-93/w1/ScoutS136/supersedes-draft.md` (arrived after 22 bounded polls of 30 s).
No frozen file modified; the living entry and SOURCES.md were never edited — all revisions made
on scratch copies; the L1 applies the bytes below.

## Deliverables (all under `.ufo/waves/round-93/w1/ReviewerErrata/`)

1. **entry-r92-revision.patch** — 113 lines, one mail-style revision header + a unified
   diff (built with `git diff --no-index` in scratch, header paths normalised to
   `a/corpus/knowledge/round-92-managed-assembly-metadata-evidence.md` / `b/...`), 7 hunks:
   - `recheck:` header line (defect 2): `"the three sibling commands in §8"` → `"in the
     unnumbered ## Reproduce section"`; no `§8` remains; remaining prose `§1`/`§5` pointers
     resolve to the entry's own numbered sections.
   - Defect 3 / critic finding 9, labels only, nothing deleted, Q-map table, embedded fenced
     blocks, scope and `admission-status` untouched:
     - :224-226 (item 5 lead) and :355-360 (item 12) and :260-263 (item 5 tail): the stream
       name-list and `#GUID`-spelling claims now labelled as resting on the §II.24.2.2 / §24.2.2
       section bodies (the anchor sections), not on a carried quote;
     - :404-409 (item 22): `rea` 6.8.0 / provider id / exit 0 / stderr 0 bytes / stdout digest
       labelled recorded fields per `receipt.json`, cited as saved, not re-derived;
     - :381-385 (item 17) and the Sources S491 bullet (:531-532): the "Standard CLI 2005"
       version-string quote labelled a partial sentence cut at the source PDF's line wrap,
       remainder not quoted.
   - Header lists the revision as the entry's NEXT REVISION OF RECORD with all four digests:
     previous normalised 2c96e633… / raw 4123a7d8… ; revision normalised
     faa872ebab84e11387aa2733eaea04f1e873a17aa16cb80f915f97757599460c / raw
     7d157de2c71c0a3c7aae5df30470f9ac652d0e877e457a2c9d28a884f0973be1. The digest difference is
     disclosed in the header: the r92 votes keep binding 2c96e633… (original bytes); the
     correction-of-record is logged by the L1 in the round-93 lesson, not a silent swap.

2. **relabel-correction.md** (defect 1) — two-sentence drop-in paragraph for the round-93
   lesson + LOG: the three r92 votes (CriticR92Claims, ReviewerR92Blind, ReviewerR92Gate) were
   lane-internal gate seats (LEARNING: "a subagent the lane dispatched is still the lane"), not
   non-author votes; the outside check was the non-author integrator spot-check
   (`corpus/lessons/round-92-verifier-spotcheck.md`).

3. **s136-row.txt** (defect 4) — the S497 supersedes row, byte-exact from ScoutS136's draft
   (sha256 22b7df7a612c8b764bdbb69a692893324c07472eae3438d7ff9af53be8d09b3c, 1 line, 1331 bytes
   + newline). Verified independently by me:
   - 11 columns (id, source, kind, tier, scope, anchor, teaches, status, opened, recheck,
     used-by); split gives exactly 13 parts; no embedded `|` in any cell; all cells non-empty.
   - `teaches` opens exactly `supersedes S136 — ` (em dash + space).
   - **Id check: S497 is the next free id.** Registry max today is S494; the living
     `corpus/SOURCES.md` contains no S495/S496/S497 rows; the frozen claims.md (`:34`,
     `:138`) reserves S495 (round-77 record) and S496 (Chrome DevTools Protocol) for
     ScoutRecord's rows with the C08 entry. Reservations verified in the frozen claims text,
     not taken from the peer's word alone.
   - Fetch facts re-verified against the scout's saved evidence:
     `.ufo/waves/round-93/w1/ScoutS136/Ecma-335-Augments.md` sha256
     `1e6e225aa41cd1ccf957b3c13ec4682fc6be2265327c3632f2e8fa01279b0828`, 69577 bytes — both
     match the row's anchor cell; the located quote is byte-slice `body[39:115]` verbatim,
     14 words, at line 3 of the saved body.
   - Lane's own auditor re-run by me on a scratch copy of SOURCES.md with this row appended:
     `audit_source_quotes.py verify` → `S497 terminal=S497 state=verified (ok)`,
     `SUMMARY rows=1 verified=1 unreachable=0 unresolved=0`, exit 0;
     `chains --range 130-140` → `S136 -> S497`, `TERMINALS=11/11`, exit 0 — i.e. the row's
     rule-2 form re-points S136's chain exactly as routed. The living SOURCES.md was not
     written.

4. **revision-checks.log** — gate outputs and digest derivation for the revision:
   - `corpus/lint_entry.py --entry <revised>` → `LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0
     LINT_HEADER=0`, exit 0; `corpus/check_embedded_outputs.py --entry <revised>` →
     `checked_blocks=11 problems=0`, exit 0.
   - Baseline control: the same two gates on the ORIGINAL bytes → exit 0 / exit 0, so the
     revision is gate-neutral (green before, green after).
   - Digests as in (1); recomputed with the frozen counters' exact normalisation
     (`admission-status:` line → `candidate` before hashing).

## ScoutS136's 404 correction (carried, verified-against-evidence by me)

The routing text said the r92 scout opened `github.com/dotnet/ecma-335/...` — that repo 404s;
the addendum lives in `dotnet/runtime` at `docs/design/specs/Ecma-335-Augments.md`, pinned at
commit `b22bfee2010118c58ae143c3b8a1aaee3d0c8c4c4`, blob `6a929a15f286e5c0f95e92050d7eece7e819fddf`.
The row correctly uses the `dotnet/runtime` raw URL (also what S136's own scope cell names).
I did not re-fetch from the network myself; the digest/blob/length facts above are re-derived
from the scout's saved body bytes, and the 404 finding is the scout's (I have not re-run the
fetch). Flagged so the L1 logs the URL correction with the row.

## L1 notes (from the draft, operative after landing)

- Copy `ScoutS136/quote-receipts/S497.receipt.json` (+ `raw/S497.body`) next to the row so any
  future S136-scoped quote audit resolves at the new chain terminal (S497).
- S497 lands `status: mined`, `used-by: —`; after the round-93 lesson exists the L1 may set
  `used-by` to `corpus/lessons/round-93.md` (in-place, log old→new) to keep the mined-with-
  used-by census clean.
- S136's cells stay byte-frozen (rule 2: only `status`/`recheck`/`used-by` change in place).

## No installs; scratch cleaned before yield

No tool installed or upgraded (none needed: git, python3, diff, cmp sufficed). Scratch
`/fast/scratch/hyaku/revenger-r93/ReviewerErrata/` (entry copies, diff intermediates, applytest
fixture with no commits, SOURCES-scratch with my row appended) is removed before this yield.
