# Round 93 — C08 admission on the saved round-77 CDP record (K 9/15 → 10/15); successor counters and forgery battery frozen

Base `281a5bad66e844190a570cb35d257c6974749993`; freeze `02050cb2a6758e3bd9cec696ff0e42df6f23511a`
(claims, both v2 counters, the battery, controls — committed before any seat ran). Wave
`revenger-r93-w1` (13 seats, one v1 wave; results `.ufo/waves/round-93/w1-results.json`). Claims:
`reports/round-93/claims.md`, unchanged since the freeze. This lesson is the lane's own evidence;
a seat this lane dispatched is still the lane (LEARNING.md). The outside check is the integrator's
spot-check, not any seat in this wave.

## Gate

### Admission of `corpus/knowledge/round-93-browser-cdp-runtime-evidence.md` (C08)

- Scribe draft `ScribeEntry` (READY digest `0db16a56…`, admission line normalised). Three corrections
  after the first votes moved the normalised digest: (a) one underived count sentence removed and one
  "(15 words)" parenthetical removed (critic Q11) -> `53083246…`; (b) the verified-at byte-identity
  clause scoped to `corpus/live corpus/fixtures`, because the registry changed at landing (critic Q15)
  -> final digest `1304008c5a0aff9dbb9af09967e12caeef028b1ca52e14dac7b8fe0247e43647`. All three votes
  were re-bound to the final digest (see Mistakes M1).
- Votes (reviewer|critic, digest-bound, artifact-bound to wave bytes; files in `reports/round-93/votes/`):
  `ReviewerGate` (reviewer), `ReviewerBlind` (reviewer; blind derivation from fixture and record bytes
  before reading the entry), `CriticR93` (critic). Per-vote PASS/n-a counts are in the vote files.
- Lint (`corpus/lint_entry.py`) 0/0/0/0 and embedded-output gate `checked_blocks=2 problems=0`, both on
  the corrected draft.

### Source openings (CORPUS rule 1; access date 2026-11-05 for every row; quotes located in the wave dirs)

| id | URL / path | located quote or location | disposition |
|---|---|---|---|
| S495 | `corpus/live/runs/round-77/inspection.json` (own-work) | oracle last line `ORACLE OK (17/17 checks)` (`oracle_check.py` stdout); stdout sha256 `b045a4ee…` | admit, own-work tier A, scoped to the authored fixture and that one record |
| S496 | https://chromedevtools.github.io/devtools-protocol/ (HTTP 200; body sha256 `ba8018bb…`, 35462 B; no `ms.date`; Last-Modified 2026-11-04) | landing-hero intro, 2nd sentence: "It allows tools to instrument, inspect, debug, and profile Chromium, Chrome, and other Blink-based browsers." | admit, docs tier A, scope = the protocol's own self-description only |
| S497 | https://raw.githubusercontent.com/dotnet/runtime/b22bfee2010118c58ae143c3b8a1aaee3d0c8c4c4/docs/design/specs/Ecma-335-Augments.md (HTTP 200; body sha256 `1e6e225a…`, 69577 B) | line 3: "This is a list of additions and edits to be made in ECMA-335 specifications." | admit, docs tier A for the addendum's own scope; supersedes S136's "unopened — see LEADS" state (rule 2) |

S497's `used-by` is set to this lesson (a `mined` row must be cited). Receipts:
`reports/round-93/quote-receipts/{S496,S497}.receipt.json` + `raw/`, verified by
`corpus/audit_source_quotes.py verify` at the landing tree.

### C2 battery and successor counters

Frozen predicate and kill rule are in `claims.md`. Result: `BATTERY_VERDICT=pass`, `V2_KILLS=9/9`,
`V1_REACH_C2=5/5` (red-before), `POS_C1V2=pass`, `POS_C2V2=pass`, `DO_NOTHING_C2=fail`,
`R92_RECEIPTS=4/4`. The controls are in `reports/round-93/controls/`.

## Mistakes

| class | evidence pointer | captured-by | fix (shown able to fail?) |
|---|---|---|---|
| **M1 — stale vote binding (and two further digest moves).** The entry changed after one reviewer had read it; that reviewer's vote bound the earlier digest `6dc0c74a…`. The vote could not count against the final bytes. | `.ufo/waves/round-93/w1/ReviewerBlind/vote.json` at first read (`candidate_sha256` `6dc0c74a…`) vs READY `0db16a56…`; re-bound votes `reports/round-93/votes/*.json` | the frozen C1 counter's candidate-digest leg (`candidate_sha256 == want`) rejects a stale vote; the L1 saw the mismatch by reading the READY and vote digests before landing | fix = freeze the draft before votes are read, and re-bind every vote to the final digest. **Able to fail:** the stale vote's digest is a non-match under the frozen leg, observed before re-binding |
| **M2 — a background URL in the brief was wrong.** The r92 brief pointed at `github.com/dotnet/ecma-335/blob/main/docs/Ecma-335-Augments.md`; that repository returns 404. The blob sha and commit belong to `dotnet/runtime`. | `.ufo/waves/round-93/w1/ScoutS136.md` ("Defects", item 1); 404 on the repo and API | `ScoutS136` fetched and checked the URL and the commit before writing S497 | fix = S497 cites the verified `dotnet/runtime` URL with the pinned commit; the r92 scout's URL is noted here, not silently re-pointed. **Able to fail:** the 404 is the failing state; the pinned raw URL returns 200 with the matching blob |
| **M3 — the r92 successor counters are still reachable by named forgeries outside the nine frozen classes.** Critic R1: a rejected entry with a second `admission-status: admitted` line in a fenced block passes C1 (`C1_ADMITTED` scans the whole file). A3: a self-attested registry plus votes from fabricated seats passes C1_VOTES. A21/A21b/R3: a case- or space-variant seat counted as a second distinct seat. A28/A29: an author self-vote and a role mismatch pass. A1/A4: a shared or empty artifact passes. Several more in `.ufo/waves/round-93/w1/CriticR93/findings.md`. | `.ufo/waves/round-93/w1/CriticR93/findings.md` ranked findings 1–12, receipts under `CriticR93/receipts/` | none in the frozen counters: the battery froze the nine routed classes only; the critic was the first attack seat run against the v2 counters | routed to round 94 as successor predicates (each finding has a close written in its own text); the frozen v2 counters are NOT edited (kumitate r42 rule). **Able to fail:** each listed attack is a receipt that flips a verdict on a committed tree, so the gap is shown, not asserted |
| **M4 — a round-scratch tree and a gitignored cache were written where they do not belong.** A 275 MiB seat scratch dir was left after yield; a `__pycache__` appeared inside the frozen `reports/round-93/` tree when a counter was imported without `-B`. | `.ufo/waves/round-93/w1/SentinelScope/audit.md` V2-1 and V2-2 | `SentinelScope` audit (check 2b) | fix = both removed before landing; every counter runs with `python3 -B`; the cache is gitignored, so the frozen bytes were never altered (the sentinel's check 3 matches). **Able to fail:** the sentinel's `find -newer` sweep names the path |
| **M5 — appended-row cell arithmetic.** The landing appended S497 with the used-by cell set by string surgery that left the old dash in front of the path (`— corpus/lessons/round-93.md`), so the census read a non-existent used-by path. | `reports/round-93/census-round-end.log` (before the fix: `E11 S497 missing used-by — corpus/lessons/round-93.md`, exit 1 with the lesson present on disk) | the round-end census (E11) | fix = the stray dash removed from the cell (used-by is a mutable cell); exit 0 and 0 E after the fix. **Able to fail:** the E11 line is the failing state reproduced on the landing tree |

## Corrections (append-only; the filed bytes stay)

- **C-r92-1 — the round-92 votes were lane-internal, not non-author.** The round-92 spot-check's
  defect 1 stands: `ReviewerR92Gate`, `ReviewerR92Blind` and `CriticR92Claims` were seats this lane
  dispatched. LEARNING.md: a subagent the lane dispatched is still the lane. The round-92 record
  keeps its filed bytes; this entry is the correction of record. The round-92 admission rests on the
  integrator's independent re-derivation (spot-check §2–§3), not on those votes.
- **C-r92-2 — the round-92 entry revision (spot-check defects 2 and 3).** Applied as the next
  revision of `corpus/knowledge/round-92-managed-assembly-metadata-evidence.md` from
  `.ufo/waves/round-93/w1/ReviewerErrata/entry-r92-revision.patch` (`git apply --check` clean; the
  patch header records both normalized digests). The round-92 votes are not re-bound: they bind the
  original bytes, as their record states. The `recheck:` pointer now names the unnumbered `## Reproduce`
  section; note-level beyond-quote statements are labelled.
- **C-r92-3 — S136 "see LEADS" dangling pointer (spot-check defect 4).** S136's scope cell is frozen
  (rule 2 allows only `status`, `recheck`, `used-by` to change). The correction is the new row S497,
  whose `teaches` opens `supersedes S136 —`; the S136 `chains` output now resolves S136 → S497.

## Frontier and census

- Census round start: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`
  exit 0 (21 W01 + 12 W04, 0 E) — `.ufo/waves/round-93/w1/ExecCensus/census-mid.log`; rows 494 at start.
- Census round end: `reports/round-93/census-round-end.log` (exit 0 after the M5 fix; 0 E, 34 W: 21 W01 + 13 W04).
- Rows: 494 → 497 (S495, S496, S497). Rows touched old→new: none (append-only; S497's `used-by` set
  to this lesson at landing, `—` → `corpus/lessons/round-93.md`).
- Frontier row advanced: C08 `uncovered` → `held`. Sourced claim: C1 rests on S495/S496 (§2b.4).

## Assimilation

**Assimilation: none.** The `merge/revenger/` package remains in mass id drift: 155 staged ids all
collide with the registry (S047–S201; `ExecCensus/collisions.txt`), and the L0 question
`revenger | round-91` is unanswered. Nothing was adopted from the package this round. (The
wave-4 quarantine-first duty was not re-run this round; it was performed in round 92 for all 26
rows. Assimilation work waits for the operator's ruling.)

## considerthese

`considerthese/2026-11-05.md` proposal 2 ("frozen-counter validity rate") was mined by
`ConnectorOverlap`: measured on committed bytes, r89–r92 give 8/8 claims contested or not verified
(`ConnectorOverlap/measurement.tsv`). Mined, not adopted: a QUALITY criterion would need its own
frozen predicate. It is recorded here as the baseline for round 94 to re-measure.
