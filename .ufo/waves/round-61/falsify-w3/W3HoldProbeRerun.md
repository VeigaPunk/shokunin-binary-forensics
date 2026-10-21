GRADE: HOLDS — C1 coverage-K probe re-run on landed ab58069 vs base cf02419 (K_HELD_BACKED 6/14, exit 0)

# Scope
Re-run `reports/round-61/measure.py` (the live file, byte-identical to `ab58069:reports/round-61/measure.py`
— `git diff --stat ab58069 -- reports/round-61/measure.py` empty) on extracted archives of
`ab580698212258a55e43e9bb9bf6ac78c91eae2a` and `cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97`, `cwd=/`,
and compare every printed line against `reports/round-61/measure-after.log` (appended section) and
`reports/round-61/measure-before.log`. Live lane tree read-only; scratch only under
`/tmp/revenger-r61w3-W3HoldProbeRerun`.

# F1 (HOLDS) — after-tree probe output reproduces the appended after-log section line-for-line
Command: `cd / && python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-61/measure.py /tmp/revenger-r61w3-W3HoldProbeRerun/after` → `probe_exit=0`.
My output is byte-identical to `measure-after.log:52-79` for every probe-printed line:
`K_HELD=6/14 score=4.3`, `K_ROW C04 status=held`, `K_ROW C09 status=held`, `K_HELD_BACKED=6/14`,
all 6 `MUTANT` lines (b = `exit=1 killed :: AssertionError: r47/r42: forged receipt command accepted`,
d2 = `exit=1 killed :: ... receipt`), `C2_CONTROLS_PASS=2/2`, `C2_RECEIPT_B_KILLED=2/2`,
`C2_D2_KILLED=2/2`, `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2`, all 10 `HOLD` lines, `HOLD_CALIBRATION=4/4`,
`HOLD_REPLAY=10/10`, `HOLDS_OK=yes`. Log's `probe_exit=0` (:79) confirmed.
The appended section names `0597e5336fd67654c974fcb05f73353f44d868b9`; the landed `ab58069` adds only
`LOG.md`, `SCORECARD.md`, `measure-after.log` (`git diff --stat 0597e53..ab58069`), so corpus is
byte-identical — and my direct run on `ab58069` gives the same bytes as the log.
Also identical for the earlier `0b6ddf0` section (`measure-after.log:1-29`): my run on a `0b6ddf0`
archive is byte-identical to my `ab58069` run (`diff` empty).

# F2 (HOLDS) — base-tree probe output reproduces the amended before-log section
Command: `cd / && python3 -B .../measure.py /tmp/revenger-r61w3-W3HoldProbeRerun/before` → `probe_exit=0`.
Matches `measure-before.log:34-45` exactly: `K_HELD=4/14 score=2.9`, `K_ROW C04 status=uncovered`,
`K_ROW C09 status=uncovered`, `K_HELD_BACKED=4/14`, `C2_CONTROLS_PASS=2/2`, `C2_RECEIPT_B_KILLED=0/2`,
`C2_D2_KILLED=2/2`, `C2_RECEIPT_B_KILLED_ATTRIBUTED=0/2`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`,
`HOLDS_OK=yes`, `probe_exit=0` (:45).
The 16 `MUTANT`/`HOLD` lines elided from that section are byte-identical to the ones printed at
`measure-before.log:5-20` (verified line-by-line), so the parenthetical at `:46`
"(MUTANT and HOLD lines identical to the first run above.)" is TRUE.
Exit codes: after=0, before=0; both logs record `probe_exit=0`.

# F3 (PARTIAL, calibration limit of the K instrument) — K_HELD_BACKED tests file existence only
`measure.py:31-33` counts a held row as backed iff the file named in the knowledge cell
`exists`. An empty file with the right name passes. Mutation test (tree copy, corpus-only):
`corpus/knowledge/commonjs-destructured-require-edges.md` replaced by the 7-byte stub `# stub`
→ `K_HELD=6/14`, `K_HELD_BACKED=6/14`, exit 0 — the instrument cannot tell an admitted entry from
an empty placeholder.
Consequence: the score 4.3 rests on `K_HELD_BACKED`, but the pre-registered admission condition
(`claims.md:26-34`: pass Q01–Q11, cite a tier-A row opened in round 61, carry in-entry derivations,
survive the attacks) is evidenced only by each entry's own self-graded Q table, never by the probe.
`K_HELD_BACKED` is a necessary, not sufficient, condition for admission. Not a false statement in
the log; a coverage limit of the counting instrument.

# F4 (PARTIAL, log fidelity) — the amended base transcript is filtered, not verbatim
`measure-before.log:34-45` is a condensation of the probe's actual print order
(`measure.py:29-46`: `K_HELD_BACKED` → 6 `MUTANT` → 4 `C2_*` → 10 `HOLD` → `HOLD_CALIBRATION` →
`HOLD_REPLAY` → `HOLDS_OK`). The elision is disclosed at `:46`, and every retained value is
correct, so no measured value is misreported — but the section is not a raw transcript and a
reader diffing stdout against it must apply the same filter.

# F5 (HOLDS) — probe sensitivity and side-effect checks (all executed on copies)
- README-only flip (C04 knowledge cell → `knowledge/does-not-exist-commonjs.md`): `K_HELD=6/14`,
  `K_HELD_BACKED=5/14` — the A1 "text flip alone counts 0" rule fires.
- Delete `corpus/knowledge/commonjs-destructured-require-edges.md`: `K_HELD=6/14`,
  `K_HELD_BACKED=5/14`.
- Flip C01 `held`→`partial`: `K_HELD=5/14`, `K_HELD_BACKED=5/14`.
- Break `verify_pe_resources.py`: `HOLD_REPLAY=9/10`, `HOLDS_OK=no`, **exit 1**.
- Duplicate the `receipt['command']` conjunct in `verify_icon_languages.py`: mutant site match
  count ≠ 1 → `could-not-evaluate`, **exit 2**. Both exit-code paths in `measure.py:109` behave as
  specified.
- Probe writes nothing in TREE: sha256 manifest of every file under the archive tree is identical
  before and after a run (`diff` of manifests empty).
- `cwd=` does not matter: run from `/tmp` gives output byte-identical to `cwd=/`.
- `git diff --stat cf02419 ab58069 -- corpus/live corpus/fixtures` → empty, rc 0 (matches
  `measure-after.log:81-82`).

# F6 (HOLDS) — the appended section's other recorded outputs reproduce
- Entry `## Reproduce` blocks re-run from the archive root: `evm-saved-interface-candidates.md`
  exit 0, stdout identical to its `## Provenance` block, 14 lines; `commonjs-destructured-require-edges.md`
  exit 0, identical, 29 lines — matches `measure-after.log:85-86` (`True 14` / `True 29`). Same at `0b6ddf0`.
- `R24_SPAN [[1, 9]]` (`measure-after.log:89`): recomputed from
  `corpus/fixtures/evm-r24/truth.json` `embedded_pattern_hex` = `63deadbeef14601057` (9 bytes);
  byte-search over `fixture.raw` (35 bytes) → occurrence at offset 1 → inclusive span `[1, 9]`.
  Matches. (The 18-byte r19 pattern does not occur in r24 at all; the span is well-defined only for
  the 9-byte `embedded_pattern_hex`, which is what the truth.json field and the M25 wording use.)
- Census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin revenger` → `revenger W04 S024 duplicate url
  www.rfc-editor.org/rfc/rfc3227.txt across scopes`, `revenger ok`, rc 0 — matches
  `measure-after.log:92-94`; the base log (`measure-before.log:29`) has no W04 line, consistent
  with S024 not existing at `cf02419`.

# Residual risk / verification gaps
- The probe cannot verify Q01–Q11 conformance, tier-A source use, or in-entry derivations (F3);
  those rest on the entries' self-graded Q tables and on peer seats, not on this measurement.
- `K_HELD_BACKED` inspects only the knowledge cell (README column 3); a row whose entry were named
  only in the evidence cell would read as unbacked. Not exercised by the current 14 rows.
- No independent check of the C09/C04 entries' substantive prose was performed here (other seats).
- No tools installed; no pacman/uv/npm installs were needed. Python 3 (stdlib only) used.

VERDICT: The landed probe reproduces every recorded value and exit code on both `ab58069` and
`cf02419` (K_HELD_BACKED 6/14 vs 4/14, exit 0/0) — the measurement record holds; the one substantive
limit is that `K_HELD_BACKED` attests only file existence (a 7-byte stub still scores 6/14), so the
counting probe is a necessary-but-not-sufficient witness for the pre-registered Q01–Q11 admission.
