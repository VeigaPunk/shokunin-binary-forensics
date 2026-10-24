# revenger round-67 claims — pre-registration (frozen before any after-measurement)

date: 2026-10-24 · author: L1 revenger-r67 (attempt 1, Kimi fresh L1) · claim base:
`fa0eb3eb33f22f56ebf066dea5440121a30d55a2` (r66 tip `8362a235` + operator considerthese sweep
`d4657ee` + non-author r66 spot-check `fa0eb3eb`; both read-only for this lane)
counter: `reports/round-67/measure.py` sha256 pinned below · red-before receipt:
`reports/round-67/measure-before.log` (committed in this same revision, run before any after-run)

## Assimilation posture (operator item 10, wave-4 quarantine-first)

This lane's first round under the 2026-10-24 assimilation directive adopts **nothing** from
`/home/vgpnk/Projects/shokuknow/merge/revenger/`. The lane's full data-row quarantine slice is
re-derived this round and every row hand-checked to a verdict; package adoption starts a later
round. Slice derivation (executed 2026-10-24, output committed at
`.ufo/waves/round-67/assimilation/quarantine-slice`):

```sh
awk -F'|' -v l='revenger' '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {print $4, $5}' \
  /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md
```

Re-derived count: **26 rows** (24 `payload-absent`, 2 fetch-failure prose rows S054/S099 — the
register's unchecked family, verdict `unverifiable-unreachable`, which is not fabrication);
every line carries an S-id. Id-collision evidence (pre-append, committed):
`reg-ids` 44 (S001–S044) · `staged-ids` 146 (S045–S190) · `collisions` 0. This round's own new
registry row takes **S045** (the lane's next unused id); that collides with the package's staged
S045 space, so any later adoption round renumbers the package **by document** (URL/anchor is the
evidence; the id follows it), never arithmetically. Nothing from `SOURCES.append.md` and no
`knowledge/` file from the package is appended or copied this round.

## C1 — coverage, knowledge-map ground K (lowest non-retired criterion, 5.7)

The round-66 routed C05 re-gate: the falsified round-65 candidate's repairs are all text-level.
One **new** candidate entry lands this round —
`corpus/knowledge/round-67-apk-axml-byte-evidence.md` — carrying exactly the routed repairs and
nothing else:

1. item 3's `member[META-INF/MANIFEST.MF]` block carries the readout's actual 16-byte
   `payload_first16_hex` `4d616e69666573742d56657273696f6e` (the r65 entry transcribed the 15-byte
   `4d616e696673742d…` at its entry:41 — M39);
2. the S038 anchor states the chunk-type enum span **including** `RES_XML_RESOURCE_MAP_TYPE` at
   snapshot line 253 (r65 cited :239-250), re-opened this round from the committed snapshot;
3. the route-scope source anchor is snapshot lines 7-8 (S043's corrected anchor, not r65's line 5);
4. the dex declared-header facts (item 9) rest on a **new tier-A row opened this round** — S045,
   the AOSP DEX format spec (`source.android.com/docs/core/runtime/dex-format`, fetched
   2026-10-24, snapshot `.ufo/waves/round-67/source-snapshots/dex-format.html` sha256
   `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4`) — instead of no registry row;
5. item 8's derivation sentence names the attrExt-relative provenance of `attributeStart` and the
   readout's derivation of local payload offsets (the two silent value dependencies);
6. the entry carries a Q08 row (`superseded by Q11`, QUALITY.md) and no dangling `### Code`
   pointer — `## Reproduce` names the saved script path directly.

The candidate lands with `admission-status: candidate`; **the README C05 row is NOT flipped at
build time**. The dispatched round-67 wave carries named fresh-seat Q01–Q13 decisions on the
landed bytes plus an outside-discernment spot-check.

- **Frozen predicate (pass branch):** `K_HELD_BACKED=9/14` **and** `K_ROW C05 status=held` **and**
  `K_HELD_BACKED_STRICT=9/14` **and** `README_TOKEN_LEGEND_MISMATCH=0` **and** the C05 row's
  knowledge column names only the round-67 entry, **and** every applicable Q01–Q13 decision on the
  landed v2 bytes is PASS (n/a only with the entry's named reason) **and** the wave's
  outside-discernment spot-check is not REJECT — the flip lands in the same revision as the Gate
  decision, and every named decision is re-verified by the L1 against committed bytes before the
  flip.
- **Kill rule (fail branch):** any Q FAIL on the v2 bytes, or a spot-check REJECT → C05 stays
  `uncovered`, the v2 entry is marked `admission-status: rejected` (retained, evidence), and C1 is
  reported **FALSIFIED** — honest stop, no re-target, no repaired acceptance condition.
- **Do-nothing control (red-before):** base `fa0eb3eb` — no v2 file exists, `K_HELD_BACKED=8/14`,
  `K_ROW C05 status=uncovered`; the control cannot reach 9/14 without the new entry plus the
  wave's all-pass.
- Measured commits: before `fa0eb3eb…` (`measure-before.log`), after = the final measured tip
  (`measure-after.log`). Causally separable from C2: C1 touches corpus knowledge/SOURCES/README
  bytes only; C2 adds one new `corpus/check_embedded_outputs.py` file and touches no existing byte.

## C2 — calibration, new criterion C7: embedded-output verbatim gate (the M39 fix shape)

Round-66 routed debt and considerthese/2026-10-24.md proposal 1 converge: a cheap pre-gate check
that re-runs an entry's own declared commands and diffs every embedded output line verbatim. The
new file is `corpus/check_embedded_outputs.py` — deliberately **outside** the `verify_*` replay
family so the frozen ten-verifier census and `HOLD_REPLAY=10/10` denominator stay untouched.

- **Modes.** `--entry <path>` (cwd = lane root): parse the entry's fenced blocks whose first line
  is `$ <command>`; run each command; every following output line must appear verbatim in that
  command's stdout; exit 0 clean (≥1 block checked), 1 with `drift entry:<line> …` findings, 2
  could-not-evaluate. `--self-test`: hermetic temp-tree cases (clean entry exit 0; drifted entry
  exit 1 naming the drift) plus the in-script forged control
  `require(not ok(drift_case), 'drifted entry output accepted')` with the attributed marker.
- **Frozen predicate:** `C7_GATE_PRESENT=yes` **and** `C7_SELFTEST=pass` **and**
  `C7_CONTROL_PASS=1/1` **and** `C7_MUTANT_KILLED_ATTRIBUTED=1/1` **and**
  `C7_RED_ON_R65_CANDIDATE=yes` **and** `C7_V2_CLEAN=yes` **and** `HOLDS_OK_V5=yes` **and** probe
  exit 0 at the final measured tip.
- **Mutant (frozen):** delete the single comparison call — regex
  `problems \+= drift\(lines, stdout_set, lineno\)` (must match exactly once) → the gate's own
  self-test must exit non-zero with last line ending `drifted entry output accepted`; attributed
  iff both hold. Unmutated self-test green is the control half.
- **Red-before is committed history, not a constructed state:** the retained round-65 candidate
  still carries the drifted hex at its entry:41, so `--entry` over the committed base tree must
  exit 1 naming that drift (`C7_RED_ON_R65_CANDIDATE=yes` in the after tree; at base the gate does
  not exist and the label prints `no`).
- **Do-nothing control:** base `fa0eb3eb` prints `C7_GATE_PRESENT=no`, `C7_SELFTEST=n/a`,
  `C7_CONTROL_PASS=0/1`, `C7_MUTANT_KILLED_ATTRIBUTED=0/1`, `C7_RED_ON_R65_CANDIDATE=no`,
  `HOLDS_OK_V5=no`.
- Registry: the gate registers in `SKILL.md` (this lane's registry home) as a **probe** with
  verdict map 0/1/2 and self-test spelling `--self-test`, owner revenger.

## Frozen counter

`python3 -B reports/round-67/measure.py TREE` — invocation contract identical to round-66
(`git archive <commit> corpus | tar -x -C <tree>`; from `/`;
`TMPDIR=/tmp/revenger-r67-counter-XXXX python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-67/measure.py <tree>`).
All round-66 labels carry byte-identical semantics; additions: the C7 labels above and
`HOLDS_OK_V5 = HOLDS_OK_V4 ∧ C7 targets`. Exit semantics unchanged (2 not-evaluable / 0 holds /
1 hold failed). Counter sha256 at pre-registration (pinned, never edited after):
see `sha256sum reports/round-67/measure.py` in `measure-before.log`.

## Admission order (unchanged, binding)

1. Land candidates with **no** README status flip. 2. Fresh in-wave attacks; every Q01–Q13
decision from a named seat that is not the author; blind independence = at least one seat derives
the AXML layout without the author's readout. 3. Adjudicate; flip the affected coverage row only
on an all-criteria pass; a falsified claim stops honestly. 4. Calibration needs red-before below
target and attributed counts at target at the final measured commit. 5. Only the C05 row may
change; the 14-row denominator, the ten-verifier replay set, FRESH_ROWS 18, and Q01–Q13 stay
fixed.

## Void conditions

Changed `corpus/live` or `corpus/fixtures` bytes (this round registers **no** new fixture/live
paths — the round-65 fixture bytes are the claim surface and stay frozen); a lost baseline held
row; a README status change other than C05 (either-way); a changed denominator; weakened
Q01–Q13; attributed calibration counts below target (C2 2/2, C3 2/2, C4 2/2, C5 2/2, C6 4/4,
C7 1/1); `HOLD_CALIBRATION` < 4/4; `HOLD_REPLAY` < 10/10; `STRICT_REJECT_WINDOW_SELFTEST` not
pass; `HOLDS_OK_V4`/`HOLDS_OK_V5` not yes; probe exit non-zero at final; prior rejected
candidates altered (the r65 candidate keeps every byte, including its drifted entry:41 — it is
the red-before surface); any write outside the lane repo + this round's report path.

## Wave contract (registered, not a claim)

ONE v2 wave of exactly 64 seats under `scripts/hyaku/ufo-wave-policy-v2.json` (band 64–128,
maxLanes 256), validated (`plan` exit 0) and dispatched as exactly ONE batched call; ≥25% attack
roles; build items (quarantine hand-checks, counter/census re-runs) and attack items (Q01–Q13,
spot-check, gate mutant review, separability, claims critics) together; §3 planner seat held by
the L1 (a bounded planning data-walk rides scout/connector items). Slot acquired via
`scripts/hyaku/wave-slot.sh acquire` immediately before dispatch, released when settled. Dead
seats stay dead and are reported; no replacement seats.

## Registered (not claims)

S045 row + search-log note; the 26 quarantine verdicts (lesson `## Gate`, ≥1 admit + ≥1 reject
recorded for the non-author closure to spot-check); SKILL.md gate registry row; considerthese
mining (proposal 1 = C2's fix shape; read-only, never edited); census before→after; one mistake
mined in `corpus/lessons/round-67.md` `## Mistakes`.
