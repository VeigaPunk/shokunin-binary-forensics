# CriticR94 — attack pass on round-94 C1 (K admit, C15) and C2 (calibration)

Scope: read-only attack on the frozen v3 counter `reports/round-94/c1_k_admit_counter3.py`
and the claims in `reports/round-94/claims.md`. Lane tip `060a8e8`. No lane file edited, no git
mutation in the lane. Candidate digest at the tip (printed by the counter):
`01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3`.

Method. Every attempt builds an honest admission-shaped fixture with the counter's own
`_fixture()` (freeze archive `9876cb3` + real entry bytes + synthetic wave/receipts), applies one
mutation, re-binds votes to the mutated digest where the mutation is an entry edit (an attacker can
always do this), and runs the counter two ways:

- `--rev`: the fixture is committed into a scratch git repo (objects borrowed read-only through
  `alternates` so `FREEZE_REV` resolves) and the counter runs `--rev <commit>`. This is the
  landing path.
- `--tree`: `--tree <dir>`, the path the frozen battery and self-test use.

Driver: `attacks/attacks.py` (copied into this wave dir). Per-attempt stdout: `receipts/<NAME>.<mode>.txt`.
Reproduce:

    mkdir -p /fast/scratch/hyaku/revenger-r94/CriticR94/work
    python3 -B .ufo/waves/round-94/w1/CriticR94/attacks/attacks.py          # V01-V27, C01, C02, H00
    python3 -B .ufo/waves/round-94/w1/CriticR94/attacks/attacks.py frozen   # frozen twelve, tree mode

## Verdict summary

- The frozen twelve (F10-F19, ONLY-C15) are reproduced: `FROZEN_KILLS_CRITICR94=12/12` (tree mode).
  The counter self-test passes (`SELFTEST_C1V3=pass legs=14`), the do-nothing base fails, the honest
  fixture passes with the real lint and the real embedded checker.
- C1 holds at the named vectors but its evidentiary legs are weaker than the claim text. Seventeen
  of the 27 forgeries pass v3; the ones that bear on the C1 move are H1-H3, M1, M3, M4 and M8.
- C2's "kills the routed forgery classes" is true for the named vectors. Variants of the same
  classes survive (H1, M5, M6, M7). The claim's own kill rule routes such survivors to r95, so this
  does not change the C2 predicate, but the sentence overstates it.

## Ranked findings

### HIGH

**H1. The dup-status close is anchored to column 0; an indented second status line passes (C2 + C1_ADMITTED).**
`C1_ADMITTED` counts `^admission-status:` (line start) and the digest normalises the same anchor.
Repro: header line 3 becomes `  admission-status: rejected` (two leading spaces); the real status on
line 11 stays `admitted`. Votes re-bound. Counter: `rc=0 verdict=pass failing=none`.
Receipt: `receipts/V14-indented-dup-status.rev.txt`. The r93 finding-1 shape (a second, contradicting
status line) survives in one form. Close: count `\s*admission-status\s*:` (case-insensitive) over the whole
file; fail on any line containing `admission-status`.

**H2. The C1 "opening evidence" is internal consistency, not a fetch (C1_QUOTES; claims wording W3/W12 reopened).**
`check_quotes` runs `audit_source_quotes.py verify`, which checks: the body's sha256 equals
`fetch_sha256`, the length matches, the quote appears in the body, and the span lies inside the
body. It does not check `fetched_at`, `http_status`, the `fetch_url` host, or whether the body
came from the network.
- V10: `fetched_at` set to `2026-10-01` on both new receipts, rows still say 2026-11-05 → `pass`.
  Receipt: `receipts/V10-receipt-stale-fetch.rev.txt`.
- V27: S498's body replaced by invented text ("REA is a cloud-hosted SaaS scanner …"), with
  `fetch_sha256`, length, quote and span recomputed → `pass`. Receipt: `receipts/V27-self-consistent-fabricated-body.rev.txt`.
- The honest fixture itself uses `https://fixture.invalid/` as `fetch_url` and passes; the counter
  never looks at the URL.
- The SOURCES `opened` cell that carries 2026-11-05 is a self-declared string.

The claim's sentence "the opening evidence is C1_QUOTES over the rows opened this round" is
therefore stronger than the leg reads. The counter cannot distinguish a fabricated receipt from a
fetched one. Close (r95): require `fetched_at == ROUND_DATE`, `http_status == 200`, `fetch_url` host
allowlisted to `github.com/morluto/rea`, and a committed fetch log that the counter re-hashes; a
non-author re-fetch remains the only real proof of opening.

**H3. The K move does not require the admitted entry to back C15 (C1_C15_CITES, C1_K_HELD_BACKED).**
`C1_C15_CITES` is `ENTRY_REL in c15[2]` (substring). `held_backed` counts every `knowledge/*.md` path
the cell names, provided each exists.
- V07: C15 cell `` `legacy/knowledge/round-72-tool-landscape.md` `` (a path that does not exist) →
  `pass`; the `findall` regex lands on the real entry file.
- V08: C15 cell `` `knowledge/seed.md` (census; `knowledge/round-72-tool-landscape.md` pending admission) ``
  → `pass`, `C1_K_HELD_BACKED=11/15`. The row is backed by `seed.md`; the entry is only named.
Receipts: `V07-c15-legacy-path.rev.txt`, `V08-c15-entry-pending.rev.txt`.
The "backed by the re-grounded entry" sentence is not enforced. Close: require the C15 file set
to equal exactly `[knowledge/round-72-tool-landscape.md]` and that path to resolve under `corpus/`.

### MEDIUM

**M1. The votes are self-attested by one writer; the registry leg the claim names does not exist (C1_VOTES; claims W).**
`claims.md` lists a leg `C1_REGISTRY`. The counter has no such leg (grep for `C1_REGISTRY` is empty);
the registry-equals-pinned check runs inside `C1_VOTES` only. Membership is now a constant in the
frozen counter (r93 finding 2 is closed for membership). Seat identity is not: any single writer
that produces two vote files with two pinned names and two distinct artifacts gets `C1_VOTES` `pass`.
My honest fixture is exactly that (one script writes all three votes) and passes
(`receipts/H00-honest-author-self-vote-residual.rev.txt`). Residual, named: membership is pinned,
per-seat provenance is not. Two accepted votes do not mean two seats.

**M2. Duplicate JSON keys are silently last-wins (C1_VOTES, registry).**
- V03: `registry.json` carries `"CriticR94": {"role": "reviewer"}` followed later by
  `"CriticR94": {"role": "critic"}` → `pass`.
- V04: `CriticR94.json` carries `"role": "reviewer", "role": "critic"` → `pass`.
A strict JSON reader rejects both; the counter accepts the last value. Close: `object_pairs_hook`
that rejects duplicate keys.

**M3. SOURCES parsing is last-wins, and "mined terminal" is a status string (C1_SOURCES).**
- V20: a second `S900` row (mined) re-declares an earlier rejected `S900`. `C1_SOURCES` passes; the
  whole run fails only because `audit_source_quotes.parse_rows` raises on duplicate ids, which kills
  `C1_QUOTES`. The kill is incidental and belongs to a different script. Receipt: `V20-dup-sources-row.rev.txt`.
- V21: `S901` (mined, no receipt) with `supersedes S900 — …` makes a rejected `S900` a "mined
  terminal" → `pass`. Receipt: `V21-fabricated-supersession.rev.txt`.
Claims' wording "every sid … reaches a mined supersession terminal" is status-text only. Close:
require every terminal row to carry a receipt or to be one of the two new rows.

**M4. Artifact binding is a substring of the digest; containment is round-level, not seat-level (C1_VOTES).**
- V17: `CriticR94` artifact is the digest alone; `ReviewerBlind` artifact is whitespace around it → `pass`.
- V25: `ReviewerBlind` artifact is the wave registry, with the digest in an ignored top-level key → `pass`.
- Containment is `is_relative_to(.ufo/waves/round-94)`. Seat A may point at seat B's file; only
  byte-identity (the sha distinctness check) stops it. V01 (symlink to a sibling's evidence) is killed
  by that distinctness check, not by containment.
Close: require the artifact to be inside the seat's own dir and to contain a line naming the seat plus
the digest.

**M5. `n/a` reasons are length-checked, not content-checked (C1_VOTES, F17 partial).**
- V18: twenty copies of `n` as the reason for every `n/a` → `pass` (length ≥20 and ≥10 alphanumerics).
  Receipt: `V18-na-twenty-letters.rev.txt`. Close: require a reference to a Q-map row or a minimum
  token count with a vocabulary check.

**M6. The S-id regex misses suffix and spaced forms (C1_SOURCES).**
- V19: body cites `S0999a` and `S 0999`. `\bS\d{3,}\b` matches neither, so neither is resolved →
  `pass`. Receipt: `V19-cite-suffix-unresolved.rev.txt`. Close: `\bS\s?\d{3,}[a-z]?\b`, or fail on any
  `S\s?\d` token that is not in the registry.

**M7. Embedded-output legs cover only the first line of a fence and only `$`-prompted blocks (C1_EMBED_NONVACUOUS, C1_EMBEDDED).**
- V22: a fence whose first line is `echo header`, followed by `$ python3 -B corpus/lint_entry.py --self-test`
  and no output → `pass`. The nonvacuous check looks only at the first line; the real checker treats a
  blank-output block as clean. Receipt: `V22-embed-prefix-vacuous.rev.txt`.
- V23: a fence with a `%` prompt and fabricated output (`LINT_QMAP=9 fabricated`) → `pass`; no `$`
  block exists, so no leg runs. Receipt: `V23-embed-unprompted-transcript.rev.txt`.
This re-opens r93 finding 7 in a new shape. Close: apply the non-blank check to every `$` line in any
fence, and treat any fence containing a command-looking line as a block.

**M8. Q-map decisions are not cross-checked against votes; the criterion list is tree-supplied (C1_LINT, C1_VOTES).**
- V06: entry Q-map says `Q02 | FAIL` while every vote says PASS → `pass`. Lint checks only that the
  decision cell is non-empty.
- V26: `Q05` removed from the tree's `corpus/QUALITY.md` and from the entry's Q-map → `pass`. `lint_qmap`
  reads its criterion list from the tree copy of QUALITY.md, which is not pinned.
Close: compare entry Q-map decisions with the vote decisions (equal sets, equal values) and pin QUALITY.md's sha.

**M9. The `--tree` harness dereferences symlinks; the landing path (`--rev`) does not (harness divergence).**
- V02 (symlink to a digest-bearing file outside the wave dir): `--rev` → `rc=1 failing=C1_VOTES` (the
  containment check fires); `--tree` → `rc=0 pass`. `shutil.copytree` dereferences the link.
- The frozen battery and self-test use `--tree`, so no battery class exercises a symlink artifact path.
The verdict of record is `--rev`, so this does not change the C1 predicate, but the battery's artifact
evidence does not cover symlinks. Close: `copytree(..., symlinks=True)` in `materialize`, and one
battery class run through `--rev`.

**M10. No author-independence check (residual; r93 finding 3, non-author half).**
- H00: a `reviewer`-role seat that authored the entry (no author field in the entry) is accepted.
- The battery's F13 class covers role mismatch on a pinned seat only. The A28 shape (author votes on
  its own entry) is not a battery class and survives v3 when the author's role is a voting role.
`claims.md` states no non-author requirement for votes, so the wording is accurate; the residual must be
named as open. Close: an `author:` field in the entry header, checked against the vote seats.

### LOW

**L1. Header trio can be inside an HTML comment (C1_TRIO, LINT HEADER).** V24: `source:`, `verified-at:`,
`recheck:`, `coverage-map:` inside `<!-- … -->` → `pass` (presence check only). Receipt: `V24-trio-in-html-comment.rev.txt`.

**L2. The K line prints `11/15` on a failing verdict.** V15 and C01/C02 print `C1_K_HELD_BACKED`
independent of admission. The predicate is the verdict, so this is not a verdict defect; it is the r93
finding-10 shape reappearing. Do not quote the K line alone.

**L3. Process: the C2 red stage writes into another round's scratch.** `forge_battery3.py --stage red-v2`
runs `mkdir` on `/fast/scratch/hyaku/revenger-r93/CriticR93/{out,hs,trees}`. I did not run that stage
(it touches `revenger-r93`, which is off-limits to this seat), so `V2_REACH_NEW=8/8` is taken from the
committed `controls/battery3-red-v2.log`, not re-observed here. `--stage full` writes into the shared
`/fast/scratch/hyaku/revenger-r94/battery3`.

**L4. `C1_LINT` passes `--lane <live lane>`, so the Q15 `cat-file` reads the live object store, not the tree.**
No false result today (the objects are the same), but it is not the tree under test.

## Wording audit (claims.md vs. counter reads)

- **W1 (C1, legs).** Claims name `C1_REGISTRY`; the counter has no such leg. The registry check is folded
  into `C1_VOTES`. Fix the claim text or split the leg. (M1)
- **W2 (C1, ADMITTED).** "Exactly ONE `admission-status:` line in the whole file" is true for column-0 lines
  only. State the anchor. (H1)
- **W3 (C1, opening evidence).** "C1_QUOTES over the rows opened this round" verifies internal consistency;
  dates, URL and status are not read. (H2)
- **W4 (C1, backing).** "C15 backed by the entry" is a substring check, and any named file that exists counts toward K. (H3)
- **W5 (C1, terminal).** "Every sid … reaches a mined supersession terminal" reads status text. (M3)
- **W6 (C1, base).** `C1_ONLY_C15` re-derives the base rows from `git archive FREEZE_REV corpus/README.md`
  on every run; there is no stored baseline. The claim's question is answered: yes, it re-derives. Its scope
  is the README coverage rows only, which is what the claim says. Accurate.
- **W7 (C1, votes).** "Seats against the PINNED wave registry" is true; "three lane-internal gate votes"
  is true of who wrote them, and nothing else. (M1, M10)
- **W8 (C2, classes).** "The v3 counter kills the routed forgery classes" holds for named vectors. Variants
  survive (H1, M5, M6, M7). Route them to r95 as the kill rule already does; say "named vectors" in the claim.
- **W9 (C2, F13).** Receipt-backed reach is disclosed exactly as the claim says. The F13 battery class tests
  role mismatch only; A28 author self-vote is not in the battery. The verdict does not count F13. Honest as
  written.
- **W10 (C2, red-v2).** `RED_V2_VERDICT=pass` is a committed-log fact I did not re-observe (L3).

## Frozen-kill cross-check (tree mode, my run)

```
FROZEN-F10-dup-status:       KILLED   failing=C1_ADMITTED,C1_VOTES
FROZEN-F11-forged-registry:  KILLED   failing=C1_VOTES
FROZEN-F12-case-dup-seat:    KILLED   failing=C1_VOTES
FROZEN-F13-role-mismatch:    KILLED   failing=C1_VOTES
FROZEN-F14-empty-artifact:   KILLED   failing=C1_VOTES
FROZEN-F15-traversal:        KILLED   failing=C1_VOTES
FROZEN-F16-body-rejected-sid:KILLED   failing=C1_VOTES,C1_SOURCES
FROZEN-F17-vacuous-na:       KILLED   failing=C1_VOTES
FROZEN-F18-ws-output:        KILLED   failing=C1_VOTES,C1_EMBEDDED,C1_EMBED_NONVACUOUS
FROZEN-F18b-tilde-fence:     KILLED   failing=C1_VOTES,C1_EMBEDDED,C1_EMBED_NONVACUOUS
FROZEN-F19-stale-new-row:    KILLED   failing=C1_SOURCES
FROZEN-ONLY-C15-second-row:  KILLED   failing=C1_ONLY_C15,C1_K_HELD_BACKED
FROZEN_KILLS_CRITICR94=12/12
```

Several frozen kills are incidental: the entry or vote edit also changes the digest, so `C1_VOTES` fails
alongside the named leg. The named leg does fire in every case, so the frozen predicate holds.

## Attempt table (rc / verdict / failing; `rev` unless noted)

| Attempt | Vector | rc | verdict | failing | Reads as |
|---|---|---|---|---|---|
| V01 | vote artifact = symlink to sibling's file | 1 | fail | C1_VOTES | killed (distinctness) |
| V02 | symlink to digest file outside wave dir | 1 | fail | C1_VOTES | killed in rev; **tree passes (M9)** |
| V03 | registry duplicate seat key | 0 | pass | none | survives (M2) |
| V04 | vote duplicate role key | 0 | pass | none | survives (M2) |
| V05 | Q-map decision cell empty | 1 | fail | C1_LINT | killed |
| V06 | Q-map FAIL vs votes PASS | 0 | pass | none | survives (M8) |
| V07 | C15 cell `legacy/knowledge/…` (nonexistent) | 0 | pass | none | survives (H3) |
| V08 | C15 cell backed by seed.md, entry "pending" | 0 | pass | none | survives (H3) |
| V09 | receipt span end < start | 1 | fail | C1_QUOTES | killed |
| V10 | receipt fetched_at 2026-10-01 | 0 | pass | none | survives (H2) |
| V11 | vote seat ScoutReopen role scout | 1 | fail | C1_VOTES | killed |
| V12 | two votes, same exact seat, two files | 1 | fail | C1_VOTES | killed (collision) |
| V13 | seat `reviewergate` (case variant) | 1 | fail | C1_VOTES | killed (exact pin) |
| V14 | indented duplicate status (`  admission-status: rejected`) | 0 | pass | none | survives (H1) |
| V15 | admitted status on line 16 | 1 | fail | C1_ADMITTED | killed |
| V16 | S427 (REJECTED_OK) renamed mined | 1 | fail | C1_SOURCES | killed |
| V17 | artifact = digest only / whitespace+digest | 0 | pass | none | survives (M4) |
| V18 | n/a reason = 20 × `n` | 0 | pass | none | survives (M5) |
| V19 | cites `S0999a`, `S 0999` | 0 | pass | none | survives (M6) |
| V20 | duplicate S900 row (rejected then mined) | 1 | fail | C1_QUOTES | C1_SOURCES passes; incidental kill (M3) |
| V21 | fabricated mined terminal S901 supersedes S900 | 0 | pass | none | survives (M3) |
| V22 | `$` line not first in fence, no output | 0 | pass | none | survives (M7) |
| V23 | `%`-prompt transcript, fabricated output | 0 | pass | none | survives (M7) |
| V24 | trio keys inside HTML comment | 0 | pass | none | survives (L1) |
| V25 | registry as artifact, digest in extra key | 0 | pass | none | survives (M4) |
| V26 | Q05 removed from tree QUALITY.md + Q-map | 0 | pass | none | survives (M8) |
| V27 | S498 body invented, receipt recomputed | 0 | pass | none | survives (H2) |
| C01 | control: second coverage row moved (C07) | 1 | fail | C1_ONLY_C15 | killed |
| C02 | control: duplicate C15 row | 1 | fail | C1_ROWS_TOTAL | killed |
| H00 | honest fixture, one writer, author = reviewer seat | 0 | pass | none | control; residual (M1, M10) |

Expectations recorded before the run matched every row; V02-tree and V20 are the two that differ from a
naive reading (harness divergence; incidental kill).

## Construction notes (per attempt, short)

- V01: `ReviewerBlind/evidence.md` replaced by a symlink to `ReviewerGate/evidence.md`; the vote's
  `artifact_sha256` copied from the target so the sha check passes; distinctness must then catch it.
- V02: symlink to `work/outside-evidence.md` (outside the wave dir, digest inside). Committed with
  `shutil.copytree(symlinks=True)` into a scratch repo; `--rev` reads the link.
- V03: registry text built by hand with a duplicate key first (reviewer) and the pinned value last (critic).
- V04: `json.dumps` of the vote with `"role": "critic"` replaced by `"role": "reviewer", "role": "critic"`.
- V05/V06: one entry Q-map cell edited; votes re-bound by `resign()`; only the Q-map leg differs.
- V07/V08: the README C15 cell rewritten by cell index (cells 2); the row otherwise byte-identical.
- V09/V10: receipts rewritten with span reversed / `fetched_at` stale.
- V11/V12/V13: extra vote files (`ScoutReopen.json`, `ReviewerGate.b.json`, `reviewergate.json`) with their own artifacts.
- V14: `  admission-status: rejected` inserted at header line 3; votes re-bound.
- V15: admitted status moved to line 16; votes re-bound.
- V16: S427 row `rejected` → `mined` in place.
- V17: CriticR94 artifact = digest + newline; ReviewerBlind = whitespace around digest.
- V18: every `n/a` note in ReviewerGate set to twenty `n`.
- V19: body sentence with `S0999a` and `S 0999`; votes re-bound.
- V20: SOURCES rows appended: S900 rejected, then S900 mined; body cites S900.
- V21: SOURCES rows appended: S900 rejected, S901 mined with `supersedes S900 — …` in the 7th column; body cites S900.
- V22: fence `sh` with `echo header`, then `$ python3 -B corpus/lint_entry.py --self-test`, blank line.
- V23: fence `text` with `% python3 …` and fabricated `LINT_QMAP=9`.
- V24: `<!--` before the verified-at line and `-->` after the coverage-map line.
- V25: registry gets top-level `candidate: <digest>`; ReviewerBlind's artifact = registry.
- V26: `| Q05 |` removed from tree QUALITY.md and from the entry Q-map.
- V27: S498 body replaced; `fetch_sha256`, `length`, `quote`, `span` recomputed.
- C01/C02/H00: controls as named.

Harness note: on re-read before the first run, I found the SOURCES column index wrong for the supersession
row (the `supersedes` text belongs in the 7th column, unquoted); it was fixed before any reported run. Every
reported V20/V21 row comes from the corrected builder.

## What I did not run (honest scope)

- `forge_battery3.py --stage red-v2` (writes into `revenger-r93`; not mine). The committed log is cited, not re-observed.
- `forge_battery3.py --stage full` (writes into the shared `revenger-r94/battery3`). The frozen-kill cross-check
  above reproduces its V3 kill loop in my own scratch, tree mode; `HOLD_R93_BATTERY` was not re-run.
- Network: none. `quote-receipts/` and the S498/S499 rows do not exist at `060a8e8`, so C1_QUOTES cannot be
  judged at the tip; the vote treats them as the L1 landing will supply them (see evidence.md).

## Next (for r95, routed with receipts; no predicate change)

H1 (indent-proof status count), H2 (receipt fetched_at / host / status), H3 (C15 file-set equality),
M2 (duplicate-key rejection), M3 (per-terminal receipts), M4 (seat-scoped artifact + seat name in body),
M6 (S-id grammar), M7 (non-blank check on every `$` line; any fenced command-looking line), M8 (Q-map ↔ vote equality;
pinned QUALITY sha), M9 (`symlinks=True` in `materialize`; one symlink class through `--rev`), M10 (author field).
