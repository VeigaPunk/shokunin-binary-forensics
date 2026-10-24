# Round 64 — pre-registration (2026-10-24)

Claim base `666ea84b6be2eec2b0359f556ba2429fc9044c36` (main, clean and pushed;
lane `local=remote ahead=0`). No inherited uncommitted round-64 work
(`.ufo/waves/round-64/` does not exist; watchdog shows no
`lane-dead-no-report revenger round=64`). Parent round 63 reported at
`a6f5c42145200d4c12510c5b0a6927c0111340b6`; its closure routed inputs are
honored by this round (see Routed inputs). L1 (revenger-r64) holds planner and
sole integration ownership.

## Lowest axis

Coverage K is the lowest scored criterion: **5.0 (7/14)**; coverage F 6.2
(5/8); calibration criteria C2/C3 10.0; freshness 10.0. No stagnation waiver
(saturation 7.0, window 3; capability entered fleet round-1). Two claims, each
on a distinct axis: C1 coverage, C2 calibration.

## C1 — coverage K: independently gated C07 (firmware) entry

Target: **one newly admitted entry** covering C07, lifting K to at least 8/14
(5.7); **7/14 falsifies C1**. Candidate (NEW file):
`corpus/knowledge/round-64-firmware-region-byte-evidence.md` — a manual,
byte-derived readout of the authored `corpus/fixtures/firmware-r63/firmware-r63.bin`
(2048 bytes; padding spans, two zlib members at 512 and 1024 with compressed
sizes and decompressed content digests), each value derived in-entry by
command from the fixture bytes, compared against the independent oracle
`corpus/fixtures/firmware-r63/truth.json` and the saved REA record
`corpus/live/runs/round-63/inspection.json` (observation layer only). Scope:
authored-bytes ↔ saved-record correspondence for this one fixture; no real
vendor image, no extraction/execution claim, no provider-completeness claim,
no authenticity claim, no general firmware-format claim.

The C07 coverage-map token is **stale at base by the legend's own definition**
(legend: `frontier` = "no knowledge and no saved record"; a saved
`inspect_firmware_regions` record exists since round 63 — routed input). This
round repairs it: on C1 admission C07 flips `frontier → held` naming only the
new entry; **if C1 falsifies, L1 flips C07 `frontier → uncovered`** (work
evidence exists, no admitted knowledge). Either flip lands; K moves only on
admission. No other README row changes.

Sources opened this round: **S036** (REA firmware-analysis guide at the pinned
`rea-agents-6.5.0` tag — the registry lead explicitly holds this row for "when
the firmware family is claimed"; scope: what the `inspect-firmware-regions`
route does per the version that produced the record, tier A for route-scope
sentences only) and **S037** (own-work bundle: authored fixture bytes +
`truth.json` + saved record + LEDGER, tier A for byte/record correspondence).
Each load-bearing claim rests on a tier-A row for its scope (Q01); the lesson
`## Gate` records located ≤25-word quotes, URLs, access dates. **C1 is the
round's sourced claim.**

Admission condition (same shape as rounds 62–63): named fresh-seat Q01–Q13
pass decisions from reviewers other than the candidate author/corrector; the
K probe measures existence, never quality. Blind independence (Q03): at least
one seat derives the expected layout without the author's readout script and
compares blind.

## C2 — calibration (M35 routed debt): attributed forged-receipt kill on the stdout_sha256 conjunct

Debt from round 63 (lesson M35, falsify wave): the
`receipt['stdout_sha256']==H(raw_bytes)` conjunct of `receipt_ok()` in
`verify_icon_languages.py` and `verify_multi_icon_states.py` is covered by no
in-script forged-receipt control, so deleting it leaves the self-test green.
Target: new criterion `C4_RECEIPT_KILLED_ATTRIBUTED` **0/2 → 2/2**.

Frozen mutation (same sentence in plan, probe code and receipt): for each
script, delete exactly `receipt['stdout_sha256']==H(raw_bytes)` and its
connecting `and` inside `receipt_ok`, then run `--self-test` on a fresh tree
copy.

Frozen fix shape: in each script, after the existing forged-command control,
add one in-script control: deep-copy the receipt, set
`forged['stdout_sha256'] = H(b'')`, require rejection with a message ending
`forged receipt stdout accepted`. A kill is **attributed** iff the mutant run
exits non-zero and its last output line ends with `forged receipt stdout
accepted` (registered endswith attribution — fixes the round-63 routed
substring weakness for this criterion); a crash or an unrelated assertion is
not attributed. Red-before at base: both mutants exit 0 (committed in
`measure-before.log`). Unchanged scripts otherwise; the ten-verifier census
count stays 10; all existing saved-input assertions stay; the existing
forged-command controls stay.

## Counting and admission order

Frozen counter: `python3 -B reports/round-64/measure.py TREE` (this directory,
frozen at the pre-registration commit) on a committed `git archive <commit>
corpus` tree, cwd=/, TMPDIR under lane-owned scratch. Labels it prints:
`K_HELD`, `K_HELD_BACKED` (same regex as the round-63 probe), `K_ROW C07`,
`K_HELD_BACKED_STRICT` (routed-counter fix: cited entries carrying an
`admission-status: rejected` marker do not count as backing — diagnostic,
must equal K_HELD_BACKED at both ends or the discrepancy is reported),
`README_TOKEN_LEGEND_MISMATCH` (routed-counter fix: a row at `frontier`
contradicts the legend's own definition — "no knowledge and no saved record" —
iff at least one saved record exists for that row's own surface operations per
the probe's frozen ROW_OPS map; 1 at base (`C07`), 0 at round end), `F_COVERAGE`/`F_FAMILIES` (presence semantics unchanged),
`C4_CONTROLS_PASS`, `C4_RECEIPT_KILLED_ATTRIBUTED`, existing
`C2_*`/`C3_*`/`HOLD_*` (same definitions as the round-63 probe), `FRESH_ROWS`
(byte-survival hold; it does not certify current-host truth — routed wording),
`HOLDS_OK` (round-63 semantics, continuity hold) and `HOLDS_OK_V2`
(routed-counter fix: `holds_ok` with the attributed counts
`C2_RECEIPT_B_KILLED_ATTRIBUTED`/`C3_RECEIPT_KILLED_ATTRIBUTED`/
`C4_RECEIPT_KILLED_ATTRIBUTED` substituted for the raw kills, PLUS the
registered legend fix `README_TOKEN_LEGEND_MISMATCH == 0`; a diagnostic
label, not a claim target). The round-63 probe and its pinned SHA are untouched.

Do-nothing control (committed with pre-registration): the frozen counter run
on the base archive must print K_HELD_BACKED 7/14, K_HELD_BACKED_STRICT 7/14,
README_TOKEN_LEGEND_MISMATCH 1, C4_RECEIPT_KILLED_ATTRIBUTED 0/2 — a control
that skips all claimed work meets no target (`measure-before.log`).

Admission order (same as rounds 62–63): land candidates without README flip →
fresh in-wave attacks → adjudicate → flip C07 only on all-criteria pass; C2
requires red-before 0/2 and attributed 2/2 at final. A falsified claim is
reported honestly, not re-targeted.

## Harms and frozen holds

Void conditions: any changed `corpus/live` or `corpus/fixtures` byte outside
new round-64 paths; any lost baseline held row; any README status change other
than C07; changed denominator (14 rows / 8 families); weakened Q01–Q13;
C2 attributed kills below 2/2 or d2 below 2/2; C3 attributed below 2/2;
C4 attributed below 2/2 after landing; HOLD_CALIBRATION below 4/4;
HOLD_REPLAY below 10/10; probe exit non-zero at final. Prior rejected
candidates, counterexamples, verifier lesson and round-63 evidence remain
byte-preserved. No new gate capability, registry conformity or promotion is
claimed (SKILL.md is checklist work, not a claim).

## Frontier and routed debt

Sources: append S036 + S037 only after opening; log Gate quotes; census before
(exit 0, 35 rows, four disclosed W04s: S024/S028/S029/S034) and after
(exit 0 required). Mistake: mine M36 (coverage-map token drifted from the
legend's definition for a full round because no committed check compared
tokens to evidence — fix = the registered `README_TOKEN_LEGEND_MISMATCH`
counter label, shown able to fail at base with value 1) into
`corpus/lessons/round-64.md` `## Mistakes`.

Routed inputs from the round-63 closure, dispositioned here:

1. **Frozen-counter semantics → later registered counter** — this round's
   probe IS the later counter: it registers `K_HELD_BACKED_STRICT`,
   `README_TOKEN_LEGEND_MISMATCH` and `HOLDS_OK_V2` (above). F stays
   presence-only by definition; per-family counts are already printed. Any
   remaining semantic gap is re-routed with reasons.
2. **M35 both stdout_sha256 conjuncts** — claimed as C2.
3. **C07 legend staleness** — repaired inside C1 (flip either way).
4. **Evidence-ID transplant corollary** — owner named this round: a future
   calibration round that registers a receipt/Evidence-ID binding check;
   this round records the mechanism in the lesson (Q09 disclaimers carried).
5. **r58/59 139→142 PASS-count quotes** — stay unedited (historical records
   under void conditions); the round-64 lesson records the non-reproduction
   and names the owner: the next round that touches those verifiers
   re-derives current pass counts in its receipts.
6. **Freshness-hold wording** — frozen in this contract (label semantics
   above); SCORECARD wording updated at round end.
7. **SHONEN box 1 (SKILL.md absent)** — checklist work this round: a named
   scribe drafts, a named non-author reviewer verifies; box flips only on a
   named verifier, else stays `[~]`/`[ ]`.

One validated v2 wave (exactly 64 seats under policy v2, ≥25% attack roles:
reviewer/critic/mutation-tester/scout), dispatched as exactly ONE task call;
total 64 ≤ 128; no per-lane model pins; host routing table binds routes. L1
holds the §3 planner seat (validator rejects planner as a swarm role). Seats
never mutate the fleet repo, sibling lanes, lane jj state or lane Git index;
lane absolute paths in every prompt; every `Report:` trailer path is relative
to /home/vgpnk/Projects/shokunin/revenger-shokunin — write it at
/home/vgpnk/Projects/shokunin/revenger-shokunin/<that path>. Pacman is paused
host-wide: no pacman transactions; install only via `uv tool` / `npx` /
official binaries if truly needed (none anticipated). Heavy scratch is
lane/round-owned under `/tmp/revenger-r64-*` and removed on landing.
