# Round 94 — C15 admission through the v3 gate (coverage K 10/15 → 11/15); the r93 critic's closes frozen as v3 legs and battery classes (calibration)

Base `9876cb38c5415fbc86336a26a68e05680c397fd5` (round-93 adjudication tip); freeze
`060a8e87d6de6b31f91b58524ab0fcad88ae5431` (claims, the v3 counter, the battery, the controls,
the entry re-grounding — committed before any wave seat ran; `reports/round-94/claims.md`);
wave `revenger-r94-w1` (13 seats, one v1 wave; results `.ufo/waves/round-94/w1-results.json`,
no dead seats); landing `60b5e8e36325b3decdc8ce46041216cdafd1166e`; adjudication = the commit
carrying this lesson, its LOG entry and its SCORECARD section.

**Authorship and non-author status (LEARNING.md).** All three gate votes (`ReviewerGate`,
`ReviewerBlind`, `CriticR94`) and the critic's attack pass were seats this lane dispatched. A
subagent the lane dispatched is still the lane. The C1 admission therefore rests on the frozen
counter's verdict over committed bytes, not on a non-author judgment, and it stays **pending the
non-author closure**. The same applies to C2's battery, whose findings below are the lane's own.

## Gate

### Admission of `corpus/knowledge/round-72-tool-landscape.md` (coverage-map row C15)

- **Candidate digest.** `01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3`,
  printed by `python3 -B reports/round-94/c1_k_admit_counter3.py --rev 060a8e8…` on the freeze
  tip (`.ufo/waves/round-94/w1/ExecFrozen/freeze-state-digest.txt`) and unchanged after the
  landing's single admission flip (`candidate` → `admitted` at line 11, the only status line;
  the counter normalises that line before hashing). The three votes bind this digest; the
  preflight on the working tree and the `--rev 60b5e8e3` run both read `C1_VOTES=… digest=01d51059…`.
- **Votes (lane-internal; see the authorship note).**
  `ReviewerGate` (reviewer): PASS 9 / n-a 8; `ReviewerBlind` (reviewer): PASS 9 / n-a 8;
  `CriticR94` (critic): PASS 8 / n-a 9. Each vote's artifact is a distinct wave file under
  `.ufo/waves/round-94/w1/<seat>/evidence.md` whose bytes contain the digest and whose sha256
  matches (`reports/round-94/votes/*.json`). Accepted: 3 of 3 under the v3 rules.
- **Source openings (CORPUS rule 1; access date 2026-11-05 for each row).**

| id | URL | located quote (≤25 words, receipt-verified: `body[span] == quote`) | disposition |
|---|---|---|---|
| S498 | https://raw.githubusercontent.com/morluto/rea/main/README.md (HTTP 200, 30064 B, sha256 `cb5b40c5…`; main `fe677f6c…`) | "REA connects your agent to tools for inspecting native binaries, JavaScript and Electron apps, .NET assemblies, and websites." (18 words) | admit, docs tier A; drift check of S054 — **no drift** on the scope sentence and the 38-row family table; one scope-neutral engine addition (`Kuna`) recorded in the row |
| S499 | https://raw.githubusercontent.com/morluto/rea/main/docs/installation.md (HTTP 200, 115812 B, sha256 `f05249e6…`) | "Setup previews configuration changes and asks for approval before applying them." (13 words) | admit, docs tier A; drift check of S075 — **no drift** on the approval statement; additional unattended/dry-run routes recorded, none bypassing the approval boundary |

  Two independent fetches (`ScoutReopen`, `ExecReceipts`) returned byte-identical bodies
  (`fetch-sha-compare.md`, `cmp` exit 0). The two new rows are `mined`, tier A, opened 2026-11-05,
  `used-by` the entry (repo-relative path `corpus/knowledge/round-72-tool-landscape.md`; the bare
  `knowledge/…` form produced 42 census E11 findings in the scribe's dry run and was not used).
- **Entry re-grounding in the freeze bytes.** Two source header lines (S498, S499), one new §Q-map
  row (Q17, n/a: no sentence credits a command or table with a set), and the admission flip. The
  r73 erratum section is byte-identical. The entry's own decision cells (Q01–Q16) are carried
  unchanged from the r72 candidate.
- **Lint and embedded gates on the landing tree.** `corpus/lint_entry.py` 0/0/0/0, exit 0;
  `corpus/check_embedded_outputs.py` exit 2 (`could-not-evaluate: no $ cmd blocks`), accepted by the
  counter only because the entry carries no `$` block (the leg's documented no-block clause).

## Mistakes (mined; class · evidence · captured-by · fix)

| # | class | evidence pointer | captured-by | fix (shown able to fail?) |
|---|---|---|---|---|
| **M1** | **reaped-scratch dependency in a committed instrument.** The committed r93 attack driver (`.ufo/waves/round-93/w1/CriticR93/attacks/attack.py`) hardcodes `/fast/scratch/hyaku/revenger-r93/CriticR93` (`S`, `HS`, `TREES`, `out/`). The reaper had swept that tree, so the frozen red-before re-run failed with `FileNotFoundError` before any verdict printed. | the reaped root is not citable; reproduction: `python3 -B .ufo/waves/round-93/w1/CriticR93/attacks/attacks.py A1` on a host where the r93 scratch is gone | the red stage itself (a missing verdict line) | `forge_battery3.py --stage red-v2` pre-creates the three bare dirs and copies every `*.py` of the attack folder; **able to fail:** the stage prints `MISSING` per vector until the dirs exist, and `V2_REACH_NEW` reads `0/8` before the fix (observed in the first run; that log lived in `/tmp` and is not cited). After the fix: `controls/battery3-red-v2.log` → `V2_REACH_NEW=8/8 runnable + 1 receipt-backed`, `RED_V2_VERDICT=pass` |
| **M2** | **helper-copy omission.** The first red-v2 stage copied only the three named attack scripts, dropping `attack.py`, the helper they import. Every vector printed no verdict line. | the same stage's `MISSING` lines (first run) | the stage's own reach count (`0/8`), which failed closed rather than passing | copy `sorted(CRITIC.glob("*.py"))`; **able to fail:** the `MISSING` → `pass` transition is the test (now `controls/battery3-red-v2.log`) |
| **M3** | **supersession depth.** The v3 SOURCES leg read supersessions one level deep. The honest fixture failed on S062, S068 and S094, which the r74 quote audit superseded with S431, S434 and S438 (`C1_SOURCES` failing). | `reports/round-94/controls/selftest-c1v3.log` (POS passes after the fix); the pre-fix run was in scratch and is not cited | the self-test POS leg (before freeze) | `check_sources` resolves supersession chains exactly as `audit_source_quotes.py` `resolve_terminal` does (depth 10); a `mined` terminal is required for every non-rejected cited sid. **Able to fail:** `F19` and the tree POS both flip on the rule. Fixed before the freeze, so no frozen predicate changed after data |
| **M4** | **anchor-width false green (open; critic H1).** `C1_ADMITTED` and the digest normaliser both anchor `admission-status:` at column 0. An indented second status line, `  admission-status: rejected` at line 3, with the real `admitted` at line 11, passes `C1_VERDICT=pass` (receipt `CriticR94/receipts/V14-indented-dup-status.rev.txt`). | `.ufo/waves/round-94/w1/CriticR94/findings.md` H1 | **none**: no v3 leg and no battery class covers indentation (the r93 battery F10 used column-0 only) | routed to r95 with the close: count `\s*admission-status\s*:` case-insensitively across the file and fail on any line containing `admission-status`. Not fixed this round — the frozen predicate names exactly one column-0 line, and a rule edit after data is not this claim's rule (kumitate r42) |
| **M5** | **gitignored residue from seat Python runs.** Sentinel F1: `corpus/__pycache__/audit_source_quotes.cpython-314.pyc` written ~1 min into the wave by a seat that ran a corpus tool without `-B`. Gitignored, so tracked bytes were unchanged, but it is a write into a lane file directory. | `.ufo/waves/round-94/w1/SentinelScope/audit.md` F1 | the sentinel audit (check 1c) | removed before landing; the wave context should carry `-B` for every corpus Python call (routed as a spec-template fix for r95). **Able to fail:** the sentinel's `find` is the failing state; the post-removal `find` is empty (the lane tree `__pycache__` removal is in the landing commit's working state). Same class as r93 M4 |
| **M6** | **a frozen leg name the counter does not have (wording overreach).** `claims.md` names a leg `C1_REGISTRY`; the counter has no such leg — the registry-equals-pinned check lives inside `C1_VOTES`. The registry-check mutant therefore has nothing to kill it by. | `MutationR94.md` (`C1_REGISTRY` — SURVIVED: the self-test is fully green when the registry gate is dropped); `CriticR94/findings.md` W1 | the mutation tester's per-leg run | recorded here as the erratum (the predicate `C1_VERDICT=pass` is unaffected: the check runs and its failure flips the verdict through `C1_VOTES`). **Able to fail:** the mutant survives, which is the finding. Routed to r95: split the registry check into its own leg with a red-before, and a battery class that drops the gate. Not an in-round edit: the frozen counter is not amended |
| **M7** | **a hand-written census count in the frozen claims.** `claims.md` states the round-start census as `21 W01 + 15 W04`; the measured round-start census is `21 W01 + 13 W04`, 0 E (`controls/census-round-start.log`). | `reports/round-94/controls/census-round-start.log`, `claims.md` §Frontier step | the census run at round start (exit 0 either way) | erratum here; the census driver's measured line is the authority. Not a predicate. **Able to fail:** the grep count (`grep -c` on W04) is 13 |

**Found-none sweep:** not needed — seven mined.

## Corrections (append-only; the filed bytes stay)

- **C-r93-1 — the round-93 "nine classes killed" sentence.** The r93 claim's "routed successor counters
  kill the routed forgery classes" held for the frozen nine as named (`V2_KILLS=9/9`); the r93 critic
  showed variants survive (findings 1–12). Round 94 freezes twelve classes against v3 and records the
  residual vectors as routed (see the Gate and M4/M6). The r93 filed bytes stay.
- **C-r94-1 — the claims.md leg list.** `C1_REGISTRY` is not a leg (M6). The predicate is the verdict.
- **C-r94-2 — the claims.md census count** (M7).

## Frontier and census

- Census round start (pre-freeze): `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`
  exit 0; 21 W01 + 13 W04, 0 E (`reports/round-94/controls/census-round-start.log`). Rows 497.
- Census round end: see the report's Sources & frontier section (`reports/round-94/controls/census-round-end.log`).
- Rows: 497 → 499 (S498, S499 appended after S497 inside the Registry section). Rows touched old→new:
  none (append-only; no status/recheck/used-by change in place).
- Tier histogram: A +2 (A=448 → 450); B and C unchanged.
- Frontier row advanced: C15 `uncovered` → `held`.
- Sourced claim: C1 rests on S498 and S499 (§2b.4), opened this round.

## Assimilation

**Assimilation: none.** `merge/revenger/` remains in mass id drift: the frozen collision check
(`.ufo/waves/round-94/w1/ExecCensus/collisions`) lists **155** staged ids that collide with the
registry, and the L0 question `revenger | round-91` is unanswered. Nothing adopted; the wave-4
quarantine-first duty is not re-run this round (it was performed in round 92 for all 26 rows).

## considerthese

`considerthese/2026-11-05.md` proposal 2 ("frozen-counter validity rate") was re-measured over the
r93 closure and the r94 state (`.ufo/waves/round-94/w1/ConnectorOverlap/measurement-r94.tsv`). Over
r90–r93, **0 of 8** frozen claims reached a clean verified verdict (all met-contested or
met-not-verified or failed). The r94 rows are pending and not counted. Recorded as the baseline;
**not adopted**: a criterion would need its own frozen predicate, and this lane's bar does not admit
a criterion from a measurement it has not frozen.

## Mistakes table note

M1–M7 are the mined set. M4 and M6 are open routed defects of the frozen counters (not fixed by
amendment); M1, M2, M3, M5 and M7 are closed by the artifacts named above.
- **C-r95-1 — S499 word count (round-94 spot-check defect C-b).** The `## Gate` row for S499 reads
  "(13 words)". Recount: "Setup previews configuration changes and asks for approval before applying them."
  is **11 words** (`awk '{print NF}'` on the quote). The quote itself is verbatim at the pinned body and
  within the 25-word limit; only the count was wrong. Corrected here, append-only; the filed Gate row stays.
