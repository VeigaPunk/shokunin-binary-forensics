# Round 63 — pre-registration (2026-10-23)

Claim base `55bcb6e1aeb4d42923a4e98db6580f67142b41ac` (main, clean and pushed;
lane `local=remote ahead=0`). No inherited uncommitted round-63 work
(`.ufo/waves/round-63/` does not exist; watchdog shows no
`lane-dead-no-report revenger round=63`). Parent admitted revenger=62 (closure
`corpus/lessons/round-62-verifier-spotcheck.md`); no other round is authorized.
L1 (revenger-r63) holds planner and sole integration ownership.

## Lowest axis

Coverage holds the two lowest scored criteria: K 4.3 (6/14) and F 5.0 (4/8);
calibration criteria 10.0; freshness 10.0. No stagnation waiver (saturation
7.0, window 3; a capability entered fleet round-1). Three claims, each on a
distinct recorded criterion (K and F are coverage sub-criteria split and
recorded in the fleet round-1 kaika continuation; a K move cannot move F and a
F move cannot move K — the counters share no input).

## C1 — coverage K: independently gated C06 (archives) entry

Target: **one newly admitted entry** covering C06, lifting K to at least 7/14
(5.0); **6/14 falsifies C1**. Candidate (NEW file):
`corpus/knowledge/round-63-zip-central-directory-evidence.md` — a manual,
byte-derived readout of the authored `corpus/fixtures/archive-r2/fixture.zip`
central directory (member names, local-header offsets, compressed/uncompressed
sizes, CRC-32, EOCD counts), each value derived in-entry by command from the
fixture bytes, compared against the independent oracle `truth.json` and the
saved REA record `corpus/live/runs/20261012T164246Z/artifact-inspection.json`
(observation layer only). Scope: authored-bytes ↔ spec-field ↔ saved-record
correspondence for this one fixture; no general ZIP parser claim, no trailing-
bytes claim, no provider-completeness claim, no authenticity claim.

Sources opened this round: S032 PKWARE APPNOTE (ZIP file format spec, tier A,
central directory / EOCD field layout) and, if used, S033 Python zipfile docs.
Each load-bearing claim rests on a tier-A row for its scope (Q01); the lesson
`## Gate` records located ≤25-word quotes, URLs and access dates.

Admission condition (same shape as round 62): named fresh-seat Q01–Q13 pass
decisions from reviewers other than the candidate author/corrector; README C06
flips `partial → held` only after those decisions land; the K probe measures
existence, never quality.

## C2 — coverage F: first firmware saved record from an authored known-truth fixture

Target: F **4/8 → 5/8** (`firmware` family present) **iff** a newly saved
record at `corpus/live/runs/round-63/` (a) carries `evidence_id` and
`normalized_result` with `operation == "inspect_firmware_regions"`, (b) is the
output of one real `npx -y rea-agents@6.5.0 inspect-firmware-regions <path>`
run (receipt committed with command, exit code, fixture SHA-256, stdout
SHA-256, Evidence ID), and (c) every region the record reports matches the
authored fixture's `truth.json` byte oracle (offset, size, and for
extractable members the decompressed content SHA-256). **4/8 falsifies C2.**
The fixture is authored, inert, synthetic, and never executed: raw image bytes
with compressed members at declared offsets (generator script + `truth.json`
committed under `corpus/fixtures/firmware-r63/`). L1 pre-probe (2026-10-23):
binwalk 3.1.0 does **not** detect a uImage header (85-signature scan, zero
findings on a 1056-byte header+payload image); zlib members at known offsets
are detected (`offset 512, size 55, name zlib`). The fixture must use members
from binwalk's actual signature list — this pre-probe is the red-before for
the fixture premise (see lesson M33). No execution of any firmware payload, no
real vendor image, no extraction beyond what the record itself performs.

## C3 — calibration: attributed forged-receipt kill on the two remaining verifiers

Debt from round 61 (SCORECARD planned; kaika `mutation-post.md`):
`verify_named_multi_icon_states.py` and `verify_icon_states.py` carry receipt
checks with no in-script forged-receipt control, so a clause-deletion mutant
survives their own run. Target: new criterion
`C3_RECEIPT_KILLED_ATTRIBUTED` **0/2 → 2/2**.

Frozen mutation (same sentence in plan, probe code and receipt): for each
script, delete exactly one receipt-identity conjunct and its connecting
`and`, then run `--self-test` on a fresh tree copy:
- `verify_named_multi_icon_states.py`: delete `receipt['command']==command`.
- `verify_icon_states.py`: delete `receipt['fixture_sha256'] == expected_hash`.

Frozen fix shape (executor applies; the probe's mutant must match exactly one
site in the final files): refactor each script's receipt block into a
`receipt_ok(...)` helper preserving every existing conjunct byte-for-byte
(including the `round_id != 36` evidence-ID exemption in
`verify_icon_states.py`), and add one in-script control per script:
deep-copy the receipt, forge one field (`command += ' --forged'` for named,
`fixture_sha256 = '0'*64` for icon_states), require rejection with a message
containing `forged receipt`. A kill is **attributed** iff the mutant run exits
non-zero and its last output line contains `forged receipt`; a crash or an
unrelated assertion is not attributed. Red-before at base: both mutants exit 0
(committed in `measure-before.log`). Unchanged scripts otherwise; the
ten-verifier census count stays 10; all existing saved-input assertions stay.

## Counting and admission order

Frozen counter: `python3 -B reports/round-63/measure.py TREE` (this directory,
frozen at the pre-registration commit) on a committed `git archive <commit>
corpus` tree, cwd=/, TMPDIR under lane-owned scratch. Labels it prints:
`K_HELD`, `K_HELD_BACKED`, `K_ROW C06`, `F_COVERAGE`/`F_FAMILIES`,
`C3_CONTROLS_PASS`, `C3_RECEIPT_KILLED_ATTRIBUTED`, existing
`C2_*`/`HOLD_*`/`HOLDS_OK` (same definitions as the round-61 probe), and
freshness `FRESH_ROWS`. The round-61 probe and its pinned SHA are untouched.

Do-nothing control (committed with pre-registration): the frozen counter run
on the base archive must print K_HELD_BACKED 6/14, F_COVERAGE 4/8,
C3_RECEIPT_KILLED_ATTRIBUTED 0/2 — a control that skips all claimed work does
not meet any target (`measure-before.log`).

Admission order (same as round 62): land candidates without README flip →
fresh falsify wave → adjudicate → flip C06 only on all-criteria pass; C2 F
count requires the byte-oracle agreement receipt; C3 requires red-before 0/2
and attributed 2/2 at final. A falsified claim is reported honestly, not
re-targeted.

## Harms and frozen holds

Void conditions: any changed `corpus/live` or `corpus/fixtures` byte outside
new round-63 paths; any lost baseline held row; any README status change other
than C06; changed denominator (14 rows / 8 families); weakened Q01–Q13;
C2 attributed kills below 2/2 or d2 below 2/2; HOLD_CALIBRATION below 4/4;
HOLD_REPLAY below 10/10; probe exit non-zero at final. Prior rejected
candidates, counterexamples, verifier lesson and round-62 evidence remain
byte-preserved. No new gate capability, registry conformity or promotion is
claimed.

## Frontier and routed debt

Sources: append S032 (+S033 if used) only after opening; log Gate quotes;
census before (exit 0, 31 rows, three disclosed W04s: S024/S028/S029) and
after (exit 0 required). Mistake: mine M33 (stale fixture premise — L1 assumed
uImage detectability without checking binwalk 3.1's signature list; red-before
is the 2026-10-23 pre-probe) into `corpus/lessons/round-63.md` `## Mistakes`.
Routed debt honored: the round-62 closure defect (a) — any on-tip probe
re-verification is committed alongside the report claim
(`reports/round-63/measure-after.log` on the final tip, not only mid-round
revisions). C1 is the sourced claim: it rests on S032 opened this round.

Two validated v1 waves (build 32, falsify 32), total 64 ≤ 128; no per-lane
model pins; host routing table binds routes. Seats never mutate the fleet
repo, sibling lanes, lane jj state or lane Git index; lane absolute paths in
every prompt; every `Report:` trailer path is relative to
/home/vgpnk/Projects/shokunin/revenger-shokunin — write it at
/home/vgpnk/Projects/shokunin/revenger-shokunin/<that path>. Pacman is paused
host-wide: no pacman transactions; install only via `uv tool` / `npx` /
official binaries if truly needed (none anticipated). Heavy scratch is
lane/round-owned under `/tmp/revenger-r63-*` and removed on landing.
