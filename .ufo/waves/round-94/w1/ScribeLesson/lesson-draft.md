# Round 94 — C15 admission for `corpus/knowledge/round-72-tool-landscape.md` (K 10/15 → 11/15)

Scribe draft for the L1 (`ScribeLesson`, wave `revenger-r94-w1`, seat 3 of 13). Drafted in
the wave dir only; the L1 lands `corpus/lessons/round-94.md`. Base `9876cb38c5415fbc86336a26a68e05680c397fd5`
(round-93 adjudication tip); freeze `060a8e87d6de6b31f91b58524ab0fcad88ae5431` (claims,
the v3 counter, the battery, the controls and the entry re-grounding — committed before any
seat ran). Claims: `reports/round-94/claims.md`, unchanged since the freeze.

This draft is a **draft**: every `TODO-…` marker below is a slot the L1 fills from the
landing tree. Nothing here is a verification claim — the frozen instruments are.

## Gate

### Admission of `corpus/knowledge/round-72-tool-landscape.md` (coverage-map row C15)

- **Candidate digest.** TODO-L1 — the final normalised digest must be read back from the
  landing tree, not from this draft. The freeze-tip value is
  `01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3`, printed by
  `PYTHONUTF8=1 python3 -B reports/round-94/c1_k_admit_counter3.py --rev 060a8e87d6de6b31f91b58524ab0fcad88ae5431`
  as `C1_VOTES=votes dir missing digest=01d51059…` and recorded byte-identically in
  `.ufo/waves/round-94/w1/ExecFrozen/freeze-state-digest.txt`. **The digest is invariant
  under the admission flip**: the counter normalises every `admission-status:` line to
  `candidate` before hashing, so flipping the entry's single status line to `admitted`
  leaves the digest unchanged (verified on the freeze bytes: candidate-tip and
  admitted-flip digests are equal). The three votes may therefore bind the freeze-tip
  digest **provided the L1's only edit to the entry is that one status line**; any other
  byte in `corpus/knowledge/round-72-tool-landscape.md` re-opens the digest and forces a
  full vote re-bind (the r93 M1 lesson).
- **Entry re-grounding already in the freeze bytes.** The freeze commit
  `060a8e8` already carries the entry's two new source header lines
  (`source: S498 — REA root README, …`, `source: S499 — REA setup documentation, …`) and
  the new `§Q-map` row `Q17`. `admission-status: candidate` sits at line 11 of the file
  (0-based index 10), inside the 15-line header window the `C1_ADMITTED` leg scans, and
  it is the only `admission-status:` line in the whole file. The r73 erratum section is
  byte-identical and is not touched this round.
- **Votes.** TODO-L1 — three lane-internal gate votes (reviewer ×2, critic ×1), each bound
  to the final digest, each carrying one distinct non-empty artifact inside
  `.ufo/waves/round-94/` whose bytes name that digest. Seat names, roles and the per-seat
  PASS/n-a counts come from the vote files the L1 lands in `reports/round-94/votes/`;
  the L1 fills the seat list and counts here. The frozen counter's `C1_VOTES` leg
  enforces the rules (≥2 accepted votes, pinned seat→role map, canonical seat
  uniqueness, role == pinned role and ∈ {reviewer, critic}, digest equality, Q01–Q17 with
  ≥1 PASS and every `n/a` reason ≥20 characters, one distinct artifact per vote,
  containment inside `.ufo/waves/round-94/`, artifact bytes naming the digest).
- **Lint and embedded-output gates.** TODO-L1 — paste the two receipts as they are read
  back from the landing tree. At the freeze tip, on the freeze bytes, the real
  `corpus/lint_entry.py` printed `LINT_QMAP=0 / LINT_Q14=0 / LINT_Q15=0 / LINT_HEADER=0`
  (exit 0) and the real `corpus/check_embedded_outputs.py` exited 2 with
  `could-not-evaluate: no `$ cmd` blocks or unsupported command` — the entry is
  documentation-only and carries no `$`-command block, so the counter's own
  no-`$`-block verification is what makes the embedded leg pass. Both instruments must be
  re-run on the landing bytes by the L1; these figures are the freeze-tip reading only.
- **Scope.** The entry stays scoped to named project sources: no tool execution, no host
  readiness, no accuracy or market-coverage claim (Q10). The C15 coverage row's `held`
  wording must keep that boundary clause.

### Source openings (CORPUS rule 1; access date 2026-11-05 for every row)

Quotes are the located ≤25-word quotes recorded in the receipts
`.ufo/waves/round-94/w1/ScoutReopen/receipts/S498.receipt.json` and `…/S499.receipt.json`
(fetched read-only, HTTP 200, body bytes committed under
`.ufo/waves/round-94/w1/ScoutReopen/receipts/raw/`). Both receipts carry
`verdict: verified`; `corpus/audit_source_quotes.py verify --sources corpus/SOURCES.md
--receipts reports/round-94/quote-receipts --sid S498 --sid S499` is the L1's check to
re-run on the landing receipts.

| id | URL / path | access date | located quote (≤25 words) | disposition |
|---|---|---|---|---|
| S498 | `https://raw.githubusercontent.com/morluto/rea/main/README.md` (REA root README, main at commit `fe677f6cf9853fb12490dfb8ef23ccae3a551049`; 30064 bytes, sha256 `cb5b40c5752a403fbe20be9af2c08b5ca915c033af142f6f57af227cbaa2b6ba`; identical bytes at the pinned commit URL) | 2026-11-05 | `README.md:65` — "REA connects your agent to tools for inspecting native binaries, JavaScript and Electron apps, .NET assemblies, and websites." (18 words) | admit, docs tier A — drift-check re-open of S054's source; **verdict `no-drift`** (S054's scope cell still describes the current README) |
| S499 | `https://raw.githubusercontent.com/morluto/rea/main/docs/installation.md` (REA installation and setup docs, main at commit `fe677f6cf9853fb12490dfb8ef23ccae3a551049`; 115812 bytes, sha256 `f05249e642a40562e8f2f1eee8ec23d56401f4b5884ba665c02f9730d8de2267`; identical bytes at the pinned commit URL) | 2026-11-05 | `docs/installation.md:4` — "Setup previews configuration changes and asks for approval before applying them." (11 words) | admit, docs tier A — drift-check re-open of S075's source; **verdict `no-drift`** (S075's scope cell still describes the current installation docs) |

Both re-opens are recorded as **new independent rows, not supersessions**: the drift
check found no drift, so S054's and S075's scope cells are not corrected and rule 2's
`supersedes S0NN —` form does not apply. Neither S498 nor S499 supersedes anything, and
the older rows keep their `mined` status and their own anchors. The drift-check verdicts
and the adjacent-but-scope-neutral changes (the added `Kuna` native-analysis engine name
in the README's native-binary family; the added unattended `--yes` approval route,
pre-approval macOS-version check, dry-run approval path and readiness-check table in the
installation docs) are recorded in the rows' `teaches` cells and in the scout's
`drift-verdicts.md`; they do not change either scope cell.

The L1 also lands the two receipts under `reports/round-94/quote-receipts/` (with the
`raw/` bodies) — the counter's `C1_QUOTES` leg reads them from there, not from the wave
dir.

### Registry append

The two rows to append to `corpus/SOURCES.md` are in
`.ufo/waves/round-94/w1/ScribeLesson/sources-append.md`, with the exact append point
named there. Append-only: no existing row's bytes change, and no `status`, `recheck` or
`used-by` cell is edited in place this round.

## Frontier and census

- Census before: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`
  → exit 0, 21 W01 + 13 W04, 0 E; 497 registry rows. The committed pre-freeze receipt is
  `reports/round-94/controls/census-round-start.log`.
  **Discrepancy to carry, verbatim:** `reports/round-94/claims.md` (§Frontier step) states
  the round-start census as "exit 0, 21 W01 + 15 W04, 0 E (`controls/census-round-start.log`)";
  the log it cites contains **21 W01 + 13 W04** and 0 E — the two W04 counts differ by 2.
  `ExecCensus` measured and recorded the same 13 W04 against the same claim figure
  (`ExecCensus/census-driver.log`, `.ufo/waves/round-94/w1/ExecCensus.md` §2). The claims
  file is frozen and is not edited; the L1 records the measured number, not the claimed
  one.
- Census after: TODO-L1 — the L1 re-runs the same driver command on the landing tree and
  records the exit code and the W/E counts here. With the two rows appended as drafted
  (source URLs are the receipts' own raw `main` URLs, distinct from S054's and S075's
  canonical URLs), the expected after-state is **499 rows, 21 W01 + 13 W04, 0 E, exit 0**
  — the new rows add no W04 and no E-code. Re-run and record the actual numbers.
- Rows: 497 → 499 (S498, S499 appended; no old row touched).
- Frontier row advanced: coverage-map row **C15 `uncovered` → `held`**. K_HELD_BACKED
  10/15 → 11/15 (6.7 → 7.3). Every other coverage row stays byte-identical — the
  counter's `C1_ONLY_C15` leg compares the other 14 rows against the frozen base archive.
- Sourced claim: C1 rests on S498/S499 (§2b.4).
- Tally receipt for the L1: TODO-L1 — the census driver's exit code and the row count,
  read back from the landing run.

## Mistakes

- **M1 (candidate, from the frozen battery source — L1 to confirm and word).** The r93
  attack-script scratch tree was reaped between rounds, so the committed red re-run broke:
  the r93 attack driver hardcodes its r93 scratch root and output directory. The fix is
  pre-creating the bare directories before the re-run, disclosed in the battery source
  itself (`reports/round-94/forge_battery3.py`, the `r93s`/`mkdir` block). **Able to
  fail:** the red-before is committed at freeze as
  `reports/round-94/controls/battery3-red-v2.log`; the missing-directory failure is the
  state that receipt reproduces.
- **M2 (candidate — L1 to confirm and word).** Any wave-found defect the L1 accepts.
  TODO-L1.

## Assimilation

**Assimilation: none.** The `merge/revenger/` package stays blocked on the id-collision
guard: 155 staged ids, 155 collisions, registry 497 ids — re-verified fresh this round by
`ExecCensus` (`ExecCensus/collision-run.log`, `ExecCensus/collisions`). The L0 question
`revenger | round-91` is still unanswered (`.ufo/l0-questions.md`). Nothing from the
package is adopted this round.

## considerthese

`considerthese/2026-11-05.md` proposal 2 ("frozen-counter validity rate") was re-measured
by `ConnectorOverlap` over the r93→r94 window on committed bytes
(`.ufo/waves/round-94/w1/ConnectorOverlap/measurement-r94.tsv`): **10 of 10 frozen claims
over r89–r93 are invalid** (failed, killed, met-contested or met-not-verified), a running
rate of 100%; the r94 rows are counted 0 (pending, no committed verdict at the freeze).
Reported, not adopted: a QUALITY criterion needs its own frozen predicate.
