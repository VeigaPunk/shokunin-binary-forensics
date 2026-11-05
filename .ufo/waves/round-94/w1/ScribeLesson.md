# ScribeLesson — round 94, wave revenger-r94-w1, attempt 1

Seat: `ScribeLesson` (registry role `scribe`, axis `coverage`). Lane:
`/home/vgpnk/Projects/shokunin/revenger-shokunin` at freeze
`060a8e87d6de6b31f91b58524ab0fcad88ae5431`. Date: 2026-11-05. Read-only seat: no lane
file was written, no git/jj command was run against the lane, no network beyond the URLs
the task names, no host mutation.

## What I delivered (both in my wave dir only; the L1 lands them)

| artifact | path (relative to the lane root) |
|---|---|
| round-94 lesson draft | `.ufo/waves/round-94/w1/ScribeLesson/lesson-draft.md` |
| SOURCES append block (S498, S499) | `.ufo/waves/round-94/w1/ScribeLesson/sources-append.md` |
| this report | `.ufo/waves/round-94/w1/ScribeLesson.md` |

## Behavior

**lesson-draft.md** carries the round-94 lesson skeleton with the `## Gate` section the
task asked for:

- *Admission block* for `corpus/knowledge/round-72-tool-landscape.md` (C15): the
  candidate digest, the three vote seats, and the lint/embedded receipts are all marked
  `TODO-L1` for the L1 to fill from the landing tree. The digest slot records the
  freeze-tip value `01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3`
  and the fact — verified on the freeze bytes — that it is **invariant under the
  admission-status flip**, because the counter normalises every `admission-status:` line
  to `candidate` before hashing. The votes may therefore bind the freeze-tip digest
  provided the L1's only entry edit is that one status line; any other byte re-opens the
  digest and forces a full vote re-bind (the r93 M1 lesson).
- *Source-openings table* with rows S498 and S499: URL/path, access date 2026-11-05,
  the located ≤25-word quote, and the disposition line. Both quotes come from the
  `ScoutReopen` receipts (they were present, so no `TODO-scout` placeholder was
  needed): S498 — `README.md:65`, "REA connects your agent to tools for inspecting
  native binaries, JavaScript and Electron apps, .NET assemblies, and websites." (18
  words); S499 — `docs/installation.md:4`, "Setup previews configuration changes and
  asks for approval before applying them." (11 words).
- *`## Frontier and census`* skeleton: rows 497 → 499, C15 `uncovered` → `held`,
  K_HELD_BACKED 10/15 → 11/15, the census before/after driver command, and the
  S498/S499 §2b.4 sourcing note.
- Also drafted: `## Mistakes` (M1 = the r93 attack-script scratch reaping that broke the
  committed red re-run, fix disclosed in the battery source; M2 = wave-found defect, L1
  to word), `## Assimilation` (none; 155/155 collisions) and `## considerthese`
  (proposal-2 re-measurement, reported not adopted).

**sources-append.md** carries the two registry rows exactly as they should be appended to
`corpus/SOURCES.md`, with the append point named (inside `## Registry`, after the S497
row, before `## Paths`), a per-cell rationale table, and the **drifted variant of each
`teaches` cell written out and clearly marked as reference-only — do not append**.

## Gates I exercised (all on scratch copies; the lane was never written)

Every check below was run against the **exact bytes installed in my wave dir**, not
against a hand-retyped copy.

| # | check | command | result |
|---|---|---|---|
| 1 | cell count of the two new rows | `awk -F'|' 'NF!=13 {print NR}'` over the extracted rows | prints **nothing**; each row is 11 cells → `NF=13` under the census's parser (which counts the leading and trailing empty fields) |
| 2 | no literal/escaped `\|` in any cell | per-cell scan of both rows | **no pipe inside any cell** |
| 3 | ≤25-word located quotes | word count of the two quotes | S498 = **18 words**, S499 = **11 words** |
| 4 | receipts verify over the committed bodies | `corpus/audit_source_quotes.py` semantics re-run by hand: body sha256 == `fetch_sha256`, `len(body)` == `length`, `body[span] == quote`, quote present in body | **both sids verified** (this is also `ScoutReopen`'s own `verified` verdict, independently re-fetched byte-identically by `ExecReceipts`) |
| 5 | fleet census on the appended rows | `scripts/sources-census.sh validate --file <scratch root>/corpus/SOURCES.md` (symlink farm over the real lane tree so `E11` path resolution is real) | **exit 0, 21 W01 + 13 W04, 0 E, 499 rows**; no finding on S498 or S499; W/E counts identical to the freeze tip |
| 6 | frozen C1 counter on a simulated landing | `PYTHONUTF8=1 python3 -B reports/round-94/c1_k_admit_counter3.py --tree <scratch tree>` with the two rows appended, C15 flipped to `held`, the entry status line flipped to `admitted` | `C1_SOURCES=pass`, `C1_QUOTES=pass`, `C1_C15_HELD=pass`, `C1_C15_CITES=pass`, `C1_ONLY_C15=pass`, `C1_ADMITTED=pass`, `C1_TRIO=pass`, `C1_ROWS_TOTAL=pass`, `C1_LINT=pass`, `C1_EMBEDDED=pass`, `C1_EMBED_NONVACUOUS=pass`, `C1_K_HELD_BACKED=pass` (11/15). **`C1_VOTES=fail`** — needs ≥2 accepted vote files in `reports/round-94/votes/`, which is the L1's landing step, not this row set's |
| 7 | real lint on the freeze entry | `python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-72-tool-landscape.md --lane .` | `LINT_QMAP=0 / LINT_Q14=0 / LINT_Q15=0 / LINT_HEADER=0`, exit 0 |
| 8 | real embedded-output checker | `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-72-tool-landscape.md` | exit 2, `could-not-evaluate: no `$ cmd` blocks or unsupported command` — the entry is documentation-only with no `$`-block; the counter's own no-`$`-block verification is what makes that leg pass |
| 9 | digest value | `PYTHONUTF8=1 python3 -B reports/round-94/c1_k_admit_counter3.py --rev 060a8e87d6de6b31f91b58524ab0fcad88ae5431` | `C1_VOTES=votes dir missing digest=01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3`; byte-identical to `.ufo/waves/round-94/w1/ExecFrozen/freeze-state-digest.txt` |

Check 6 is the decisive one: it runs the **frozen** instrument unmodified, over the
**exact** rows I am shipping, and every leg except the vote leg passes. The vote leg is
structurally outside my deliverable (the L1 lands the vote files).

## Touched surfaces

Written (my wave dir only):

- `.ufo/waves/round-94/w1/ScribeLesson/lesson-draft.md` (new)
- `.ufo/waves/round-94/w1/ScribeLesson/sources-append.md` (new)
- `.ufo/waves/round-94/w1/ScribeLesson.md` (this report, new)

Scratch: `/fast/scratch/hyaku/revenger-r94/ScribeLesson/` — created, used, and **deleted
before this yield** (no tree left behind). The lane working tree is unchanged apart from
the untracked `.ufo/waves/round-94/` wave dir that the whole wave owns.

Not touched: any lane file (`corpus/`, `reports/`, `SCORECARD.md`, `LOG.md`, `SKILL.md`,
`README.md`, `PROVINCE.md`, `QUALITY.md`), `.ufo/state`, `.ufo/watchdog.log`, the fleet
repo, sibling lanes, `shokuknow`. No git/jj write command was run anywhere. No sudo, no
sysctl, no pacman, no `~/.local/bin` or PATH-directory write, no tool install.

Network: exactly the URLs the task names — the two `raw.githubusercontent.com/morluto/rea`
README/installation files, read-only, for byte-identity confirmation against the
scout's receipts (HTTP 200; sha256 `cb5b40c5…` / `f05249e6…`, identical to the receipts).
Nothing else was fetched.

## Out of scope (deliberately not done)

- Landing. The L1 owns `corpus/SOURCES.md`, `corpus/lessons/round-94.md`,
  `corpus/README.md`, the entry's admission-status flip, `reports/round-94/votes/`, the
  receipts under `reports/round-94/quote-receipts/`, `SCORECARD.md` and `LOG.md`. I did
  not touch any of them.
- Verifying the claim. I did not run the claim's own predicate as a verdict; I exercised
  the frozen instruments against my own deliverable. The claims are frozen bytes and I
  did not edit them.
- The `## Mistakes` wording, the assimilation and considerthese paragraphs, and the
  after-census figures in the lesson draft are drafted from evidence but are the L1's to
  confirm and land; each carries an explicit `TODO-L1` where it needs a landing-tree
  reading.

## Findings for the canonical judge

1. **The census W04 discrepancy is a claim-vs-evidence conflict, reported verbatim.**
   `reports/round-94/claims.md` (§Frontier step) states: *"Census round start (pre-freeze):
   exit 0, 21 W01 + 15 W04, 0 E (`controls/census-round-start.log`)"*. The log it cites
   contains **21 W01 + 13 W04** and 0 E — the two W04 counts differ by 2. `ExecCensus`
   measured the same 13 against the same claim figure and recorded it as a real number
   rather than adjusting to the expectation. The claims file is frozen and was not
   edited. My lesson draft carries the measured 13 and flags the discrepancy; the L1
   should land the measured number, not the claimed one.
2. **The digest is flip-invariant, so the three votes can bind the freeze-tip digest.**
   Verified on the freeze bytes: normalising `admission-status: candidate` and
   `admission-status: admitted` to the same canonical line yields the same sha256
   (`01d51059…`). This means the r93 M1 failure mode (stale vote binding) is avoidable
   *without* a re-bind **provided** the L1's only entry edit is that one status line. Any
   other byte in the entry re-opens the digest and all three votes must be re-bound. The
   lesson draft states this precondition explicitly rather than assuming it.
3. **The located quotes are byte-identical to the older rows' anchor quotes.** S498's
   quote equals S054's anchor quote byte-for-byte and S499's equals S075's, at the same
   spans. That is the evidentiary basis of the `no-drift` verdicts, and it is why the two
   new rows are **not** supersessions: no older scope cell is corrected, so contract
   rule 2's `supersedes S0NN —` form does not apply and S054/S075 keep their own
   `mined` status and anchors. Both variants of the `teaches` cell are written out in
   `sources-append.md`; only the no-drift variant is in the append block.
4. **The drift checks are scope-neutral but not change-free.** Two adjacent changes were
   found and recorded rather than hidden: the README's native-binary family gained the
   engine name `Kuna` (a provider addition inside an unchanged family, 38/38 `Target`
   rows byte-identical), and the installation docs added an unattended `--yes` approval
   route, a pre-approval macOS-version check, a dry-run approval path and a
   readiness-check table (all approval statements, none bypassing the approval
   boundary). Neither changes the cited scope cell.
5. **The row's `used-by` must be the repo-relative path.** I initially tried the bare
   `knowledge/round-72-tool-landscape.md`; it satisfies the counter's cite-back
   substring check but produces **42 `E11` findings** in the census (path does not
   resolve on disk) and a non-zero census exit. The shipped rows use
   `corpus/knowledge/round-72-tool-landscape.md`, which is what the frozen counter's
   `C1_SOURCES` leg and the census both accept — check 5 above is the evidence.

## Artifact paths

- `.ufo/waves/round-94/w1/ScribeLesson/lesson-draft.md`
- `.ufo/waves/round-94/w1/ScribeLesson/sources-append.md`
- `.ufo/waves/round-94/w1/ScribeLesson.md` (this report)

Scratch `/fast/scratch/hyaku/revenger-r94/ScribeLesson` was removed before this yield.
