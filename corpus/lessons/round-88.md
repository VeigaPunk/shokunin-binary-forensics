# round-88 lesson — criterion R becomes a registry-wide gate; six legacy word-count receipts found false under the declared rule and closed by verified supersessions

Round shape: fresh-start (r71/r72/r73 rejected closures re-read and
spot-checked; freshstart probes re-run fresh 2026-11-02 with the registered
patterns pasted verbatim from the r87 receipt). Base
`48db9e0cee274250b2e14a03760759ee7e7375fd`; freeze `7fab03f` (claims +
instruments + reds, committed before any landing or after-run); landing
`87f80ce` (S474-S479 + the SKILL registry row; 2 files, 18 insertions);
correction `41322a3` (the landing's rows were appended at FILE END, outside
the Registry section — E12 x6 at the first round-end census draft; the
correction moved them inside the Registry directly after S473, move only,
row bytes sha-identical across the move `252a18f3…` both tips); final
measured revision = the adjudication commit carrying this lesson. ONE claim,
calibration, not exploratory, with counting commands. Non-author
verification: pending (the closure judge re-derives; this lesson records the
self-gate only).

## Gate

### The claim

C1 calibration: criterion R full extension — the receipt rule (r76: "a
receipt citing a counting command must be re-runnable to the same value per
leg, or name the leg it does not cover") becomes a registry-wide gate, and
the extension's first run finds six legacy word-count receipts false under
the declared rule (S454 10v11, S456 11v12, S459 16v14, S461 19v17, S462
11v10, S463 10v7), each closed by a verifying supersession (S474-S479).
Criterion R's machine check covered exactly TWO rows since r76 (S444 via
receipt_probe2 LEG4's standing negative control, S445 via LEG3); now every
row is scanned every run, every receipt token classified, every word-count
receipt rule-verified or machine-closed.

- The declared word-count rule: `len(quote.split())` — whitespace split;
  delimiters do not split. S459's recorded 16 is reachable only under
  hyphen-splitting, which the row never declared; S454's 10 and S462's 11
  are reachable under no obvious rule. The quotes themselves are faithful:
  each was verified verbatim in its own row's anchor AND in its bound
  source, re-opened 2026-11-02 (`preprobe-map-check.log`,
  MAP_CHECK_ALL_OK=True) — the drift is in the COUNTS, not the quotes.
- Instrument: `reports/round-88/receipt_sweep.py` (sha `57098ed5…71271`,
  17,664 bytes, frozen at the freeze commit `7fab03f`): declared
  receipt-token set (P1 word-count / P2 prints / P3 key=value
  version-excluding / P4 colon-count / P5 ORACLE OK) over every row's
  anchor cell; LEG_BOUND vs NON_COMMAND_NUMERIC classification; frozen
  WC_MAP channels (LIVE_PRODUCER rea help/llms, COMMITTED_GIT
  `git log 46c605c`, COMMITTED_FILE the r81 spotcheck, PRODUCER_PKG the
  installed 6.8.0 parser source); drift closes only through a superseding
  row that itself verifies; `--selftest` hermetic (synthetic tables, stub
  channels; five finding-ids + `SWEEP_SELFTEST=pass` exit 0); usage 64;
  malformed/missing registry 2; `--sources PATH` declared override. Named
  limitations declared in the instrument header and the registry row
  (tokens outside the anchor cell; wordings outside the set — "shows 7",
  "prints as"; P2-P5 registered, not re-derived).
- Counting instrument: `reports/round-88/sweep_probe.sh` (sha `9a2cb442…77cd0`,
  r87 shape). The mutant pair, both re-derived from the committed blob at
  the correction tip (`mutant-kill-after.log`): comparator-blind
  (`bceb9a33…e1c30`, one-line diff) dies exit 1 attributed
  `selftest: word-count comparator accepted a wrong count`; closure-blind
  (`6c65f6ddb7…7b7b0`, one-line diff) dies exit 1 attributed
  `selftest: closure accepted an unverified supersession`; counter
  conformance `1/1 · 2/2 · 1/1` exit 0 (`sweep-probe-after.log`), counter
  red form over a non-conforming target exit 1 (in the prelanding receipt).
- Red (`sweep-red-prelanding.log`, over base-state rows, exit 1):
  `SWEEP_ROWS_SCANNED=473`, receipt rows 18, tokens 27
  (P1=7 P2=1 P3=8 P4=4 P5=7), `SWEEP_WORDCOUNT_VERIFIED=1/7` (S457),
  `SWEEP_WORDCOUNT_CLOSED=0/6`, `SWEEP_WORDCOUNT_OPEN=6`.
- Prelanding green dry run (same receipt, exit 0): the STAGED registry
  (base rows + the six new rows, nothing landed) already showed
  `ROWS_SCANNED=479`, `CLOSED=6/6` with every closure resolved
  `by=S47x(corrected-count)`, `OPEN=0`.
- Green (after landing + correction, from the committed blobs at
  `41322a3`, `sweep-green.log`): `ROWS_SCANNED=479`,
  `SWEEP_WORDCOUNT_VERIFIED=1/7`, `SWEEP_WORDCOUNT_CLOSED=6/6`,
  `SWEEP_WORDCOUNT_OPEN=0`, `SWEEP_VERDICT=green`, exit 0 — over the
  committed SOURCES blob AND the live worktree.
- Registration: the SKILL.md §Gate registry gains the `receipt_sweep` row
  (8 → 9 rows, counting command
  `sed -n '/^## Gate registry/,/^## 7\./p' SKILL.md | grep -cE '^\| name \|'`).
  The declared scan contract + named limitations live in the row.
- Axis boundary (honest): the criterion-R score stays held at its r76
  value; the moved quantity is the criterion's registry-wide reach (2 rows
  machine-checked → 479/479 scanned per run) plus six false receipts
  superseded and closed — the same shape as the r87 registration move.
  Coverage, freshness, depth, operability, adjacency: unchanged (holds
  receipt over the correction tip: M 3/3 10.00, F4 10/11 9.09, A1v2 5/5
  10.00, A1 3/3 10.00, freshness 18/18, K 8/15 5.3 — all probe exits 0;
  PROVINCE byte-unchanged; no knowledge byte).
- Holds + no-harm: `holds-over-landing-archive.log` (over `41322a3`);
  `noharm-diff.txt` (freeze..correction: SKILL.md one appended registry
  block + SOURCES.md six rows appended and moved once inside the Registry;
  protected paths empty; frozen probes absent from the range).
  Separability: `c1-only.log` — base archive + the two instruments only,
  no SKILL row, no SOURCES rows: 473 base rows, red exit 1 with the
  disclosed marker difference (the COMMITTED_GIT leg reports
  CHANNEL_UNREACHABLE in a non-git tree — the channel needs the lane
  repository; the other six word-count legs identical to the base red);
  counter conformance green over the c1-only bytes.

### New source rows

- **S474-S479** (own-work, tier A, opened 2026-11-02, appended inside the
  Registry directly after S473; NF=13 checked at append and after the
  move — 0 malformed, 0 duplicates; rows 473 → 479): the corrected
  word-count receipts. Each re-opens its bound source (the four rea
  help/llms legs re-run per leg; `git log --format=%s -1 46c605c` re-run;
  the r81 spotcheck lesson re-read; the installed 6.8.0 NibArchive.js
  re-read), carries the byte-exact quote + the declared-rule count +
  `supersedes S45x`. C1 rests on them (Q01: tier A own-work for the
  claim's scope — the lane's own re-runnable receipts).
- Located quotes grounding the corrections (≤25 words each, whitespace
  rule, in each row's anchor): e.g. S474 "Inspect SQLite schema and
  optional ordinary-table rows from a local snapshot" (11 words);
  S479 "throw new TypeError(`Unsupported NIBArchive format version
  ${formatVersion}`)" (7 words; the quote omits the line trailing
  semicolon). All seven recorded-vs-derived values are in
  `preprobe-map-check.log` / `sweep-red-prelanding.log`.
- Erratum (carry-in addressed): the r87 lesson's "(verbatim; 13 words)"
  for the SCORECARD r75 quote — the quote IS verbatim (checked this round
  against the committed SCORECARD bytes); under the rule now declared its
  whitespace count is 12 (13 requires splitting `retire/split`). The
  precision class is the same one the six registry rows instantiate;
  S473's own registry row carries no word-count token (checked), so no
  registry closure row is needed. Both counts are ≤ 25; no substantive
  violation.

### Criteria mapping (self-gate, pending non-author verification)

Q01 pass (S474-S479, tier A own-work, opened this round); Q02 n/a (no
knowledge entry; the new rows carry the full header contract); Q03 pass
(the expected drift values were derived mechanically from the quotes and
pinned in claims.md BEFORE the landing; the closure counts were frozen in
claims.md too); Q04 pass (the producer legs name rea 6.8.0 and the exact
subcommands); Q05 n/a (no readiness claim; plain-mode host dependencies
are disclosed in the registry row, not claimed); Q06 n/a (no fixture);
Q07 pass (the mutants' deaths and the six drifts were pre-registered as
expected behavior in claims.md before the landing); Q08/Q11 pass (every
count carries its command — the WC_MAP channels, the registry grep, the
sweep's own printed value lines); Q09 pass (receipts claim only the bytes
they hashed — blob shas re-derived in the receipts); Q10 pass (scoped to
this registry's word-count receipt class; no cross-family
generalization); Q13 pass (each verdict switch is credited only for the
clause its mutant shows it detects — comparator and closure both killed
attributed); Q14/Q15/Q16 pass (no hex runs; the named revisions are
derived by the git commands in the receipts; the sweep's printed output
is quoted, not described).

Spot-check: the non-author closure re-derives the red/green pair, both
mutant deaths, the registration count, and at least one word-count
verification (e.g. re-run `rea inspect-sqlite-database --help` and count
the header description words). No wave surface was used or needed (this
claim verifies from committed bytes on this host).

### Census

Round start: sanctioned explicit-lane-dir form exit 0 (21 W01 + 10 W04,
zero E — `.ufo/waves/round-88/census-round-start-sanctioned.log`);
contract-literal form exit 2 (`.ufo/waves/round-88/census-round-start-literal.log`;
operator-side lineage, L0 r79 stands). Round end: FIRST draft of the
sanctioned census caught the landing defect (E12 row-outside-Registry ×6,
exit 1 — the receipt was superseded by the corrected run); the SECOND
draft caught the E11 sequencing class (the rows' used-by names this
lesson, which did not exist until the adjudication landed — the round-end
census must run AFTER the lesson lands); the FINAL sanctioned census over
the adjudication state exits 0 with the standing 21 W01 + 10 W04 and zero
E (`.ufo/waves/round-88/census-round-end-sanctioned.log`); literal form
exit 2, routed around. Sources 473 → 479.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| Registry-append placement (rows outside the Registry section): the landing appended S474-S479 at FILE END — after `## Leads (unopened)` — instead of inside the Registry table after S473 (the r87 placement rule, whose wording was in the r87 lesson read this round); the round-end census flagged E12 row-outside-Registry ×6, sanctioned exit 1 | `.ufo/waves/round-88/census-round-end-sanctioned.log` first draft (superseded); `git diff 87f80ce..41322a3 --stat` = 6 insertions 6 deletions, SOURCES.md only | the round-end census gate, run before the adjudication landed | correction `41322a3` moves the six rows inside the Registry directly after S473; the move is byte-preserving (the six rows extracted from both tips sort to the same sha `252a18f3…`); rule: new Registry rows append directly after the last Registry row (S473 at :490, `## Paths` at :498), never at file end; mined |
| Synthetic-id grammar mismatch: the selftest's first synthetic row ids (S_A, S_B) do not match the registry row grammar (`S` + 3+ digits), so `parse_rows` scanned 0 rows and ST1 failed at the very first prelanding selftest run | scratch preprobe1 (consolidated into `reports/round-88/preprobe-history.log`, catch 1) | the preprobe habit (run every frozen recipe by hand BEFORE the freeze) | synthetic ids renamed S701/S702/S703; the selftest passes over synthetic tables that satisfy the same grammar the real parser applies; mined |
| Pinned-marker reachability (mutant dies at the wrong stage): ST1's first assertion gated on `SWEEP_WORDCOUNT_VERIFIED=1/2`, which the blinded comparator ALSO falsifies (2/2), so mutant A died with the wrong last line (`rejected a matching count`) and the pinned marker (`accepted a wrong count`) was unreachable | scratch preprobe3 (consolidated into `preprobe-history.log`, catch 2); the r87 deterministic-ordering rule was the reference | hand-running both mutants at the preprobe, comparing each death line against its pin | first ST1 assertion checks only the correct-receipt leg; the drift assertion is mutant A's deterministic death point (ST1 before ST2); both mutants now die with their pinned lines; mined |
| grep-piped exit attribution, recurrence (the r87 mined class, new signature) + an unpinned temp-tree construction: the first prelanding receipt draft recorded `MUTA_EXIT=0`/`MUTB_EXIT=0` although both mutants die exit 1 (the echo captured `tail`'s exit after a pipe); separately, the first committed-blob green receipt draft never copied the script into the temp tree, so python failed to open it and the sweep never ran (exit 2 with a python error, not a sweep verdict) | scratch preprobe receipts (consolidated into `preprobe-history.log`, catch 3); the first `sweep-green.log` draft's python error line | reading the receipts before citing (the mandated pin-vs-receipt check) | exits captured into variables before any pipe; every temp-tree construction step (mkdir, git show redirect, script copy) made explicit in the receipt; the regenerated receipts carry truthful exits (`MUTA_EXIT=1`, `MUTB_EXIT=1`, `SWEEP_GREEN_EXIT=0`); mined |
| P3 detector truncated version strings: the first inventory regex counted `application.version=12.1.4` as the receipt token `version=12` and `revision.ghidra=8b6bbb…` as `ghidra=8` — S443 would have entered the register on token fragments that are not receipts | the inventory scan draft (S443 flagged P3-keyval[version=12]) vs the row text (version strings, not counts) | the preprobe cross-check habit (hits read against the row text before the pattern set is frozen) | the declared P3 excludes values immediately followed by a word char or dot (`(?![\w.])`), so version- and sha-shaped values are not tokens; frozen in the instrument and the registry row's contract; mined |

## Routed forward

- Criterion R is CLOSED as a routed debt this round (the full extension
  landed); the sweep is the criterion's standing gate: a future round
  appending a word-count receipt must either declare-rule its count in
  the row or register it via a frozen WC_MAP/CLOSURE revision with its own
  red-before — that maintenance duty is routed with the registry row.
- Criterion C repair (§9-ruled-out twice; needs the operator to rule the
  fixture-chain re-authoring in scope); criterion N closed r87.
- F android gate (`REA_JADX_MCP_JAR` + jadx PATH — re-probed fresh
  2026-11-02, still gated); K L0 r74 (re-read, unanswered) — coverage
  stays routed on documented unreachability, sentinel = the 7
  unsupported_host groups (unchanged 2026-11-02).
- Census literal form (operator-side, lineage L0 r79); SHONEN box 1
  non-author re-confirmation (operator-side, now naming the r88 SKILL.md
  bytes — the registry row changed SKILL.md again).
- The criterion-instrument class question (whether every criterion probe
  of P's class takes a registry row) stays routed (r78 registry note).
- The census-ordering class: the round-end census must run after the
  adjudication's lesson lands (E11 sequencing, mined above); the
  round-end receipts land with the adjudication (the r87 pattern,
  followed).
- considerthese 2026-10-28 lesson-1 proposal (the claimed-coverage-set vs
  actual-compared-set checker) — considered again, not adopted (consumers
  are the operator-blocked C05 surface); stays open.
- Plain-mode host dependencies of the sweep (rea on PATH, git, the
  installed producer package file) are disclosed in the registry row's
  write-scope field; the selftest runs none of them (PATH-stripped
  counter receipt).
- treecommit repo-relative + file-exists + numstat rule (held: 9/9
  freeze, 2/2 landing, 1/1 correction).
