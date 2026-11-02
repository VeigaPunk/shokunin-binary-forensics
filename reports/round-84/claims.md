# round-84 claims (frozen before any committed after-run)

Base `54a36bca7bc52d528026ca28beb51f4cab98fa69` (r83 tip + the r83
verifier spot-check). Carry-in landing
`67e1470e5b2492df7b86632c5b3bafabfdd3e023` (the r83 non-author closure's
three routed status-neutral defects, addressed BEFORE any claim work:
`reports/round-83/v4-postlanding-recon.log` regenerated from committed
bytes and landed with a full-provenance header; `corrections.md` — the
full-sha pin correction for the five `f520f8d6…9701` drift sites and the
census `census-round-start-sanctioned2.log` pointer resolution; the r84
round-start census receipts). This file, the sha-pinned v5 instrument
(`orphan_sweep5.py`), the sha-pinned A1v2 mapping (`ag_probe2.py`), the
red-befores (`v4-invisible-red.log`, `v5-red-unmatched-absent.log`,
`ag2-red.log`), the preprobe (`preprobe-arc-shape.log`) and the §7 gate
(`freshstart-probes.log`) freeze BEFORE the landing (fixture + producer
records) and BEFORE any after-run. Two claims, distinct axes (coverage,
calibration), causally separable, neither exploratory.

## C1 — coverage: the artifact-graph family's archive-side pair moves through real producer records (criterion A1v2, 3/5 → 5/5)

Registered criterion A1v2 (`reports/round-84/ag_probe2.py`, sha pinned
below; the r82 A1 mapping `ag_probe.py` stays byte-untouched and
frozen): the rea-artifact-graph provider's FULL available-operation set
counts RECORDED iff some `corpus/live/runs/round-*/` carries both an
`inspection.json` whose `operation` equals the operation AND a
`receipt.json` with `exit_code == 0` and an `oracle.result` starting
`ORACLE OK`. Denominator disclosure (pre-run): the r82 registration
counted the no-effects triple only; the provider declares FIVE available
operations (`rea capabilities` 2026-11-02, S466: the triple +
`extract_artifact` + `inspect_artifact`; `inspect_asset_catalog` is
`available: false` / `unsupported_host` — excluded). The r81/r82
scorecards name the archive-side pair "available-but-unrecorded". On the
round base A1v2 prints 3/5 (6.00); only real current-producer records on
the pair move it to 5/5 (10.00). The v1 instrument holds 3/3 (10.00)
throughout (the pair does not move the r82 criterion — same disclosure
shape as r81's F3→F4 and r82's A1 registration).

- BEFORE (red, committed `ag2-red.log`): over the round-base archive
  `54a36bca`: `A1V2_RECORDED=3/5 score=6.00` with `extract_artifact`
  and `inspect_artifact` unrecorded; frozen holds on the same base:
  `A1_RECORDED=3/3 score=10.00` (r82 instrument), `F4_COVERAGE=10/11
  score=9.09` (r81 instrument).
- WORK: author the inert zip fixture (`corpus/fixtures/arc-r84/`:
  `build_zip.py` — 17-check SELFCHECK that re-opens the built bytes
  with the stdlib reader and re-derives every checked fact (entry
  order, names, sizes, CRC32s, content sha256s, fixture sha); no
  byte-size constants anywhere; regen byte-identical across scratch and
  worktree builds; `truth.json` written by the generator's derive()
  from the built bytes, with the Q07 hypotheses frozen BEFORE the
  committed runs; `oracle_check.py` — 36 BYTE+HYP checks for the
  inspect record, 31 for the extract record, each BYTE check
  re-deriving its expected value from the fixture bytes (Q03),
  producer-internal ids checked for FORM only), run TWO bounded
  producer runs on the committed-path bytes from the lane root
  (`rea inspect-artifact corpus/fixtures/arc-r84/R84Sample.zip --format
  json` and `rea extract-artifact corpus/fixtures/arc-r84/R84Sample.zip
  --format json`, exact stdout saved per record, exit 0, stderr 0
  bytes, receipts with fixture shas and Evidence IDs), oracles
  `ORACLE OK (36/36 checks)` and `ORACLE OK (31/31 checks)`.
- AFTER (green, `ag2-after.log`, landing archive): `A1V2_RECORDED=5/5
  score=10.00` with both archive-side operations recorded; oracle
  re-runs over the landing-archive bytes reproduce both OK lines; the
  frozen holds re-print 3/3 and 10/11 over the same archive.

VERIFY conditions (all five must hold): (a) A1v2 prints 5/5 over the
landing archive; (b) both records carry `operation ==
inspect_artifact` / `extract_artifact`, provider `rea-artifact-graph`,
exit 0, stderr 0 bytes, `evidence_id` form `ev_<64hex>`; (c) both
oracles reproduce OK over the archive bytes (HYP checks against the
pre-registered `truth.json` — recorded whichever way they fall); (d)
the frozen holds: r82 A1 3/3 and r81 F4 10/11 unchanged over the same
archive (the pair does not move them); (e) fixture regen byte-identical
from the committed generator. KILL RULE: any condition fails → the
candidate records are retained rejected (`admission-status` note in the
LEDGERs), README byte-unchanged, A1v2 prints 3/5 — recorded honestly as
falsified.

Boundary: operation-record presence on the provider's full available
set; the records demonstrate the built-in provider's zip inventory and
extraction of one authored inert 508-byte archive (Q10 scope note in
the LEDGERs: no general archive-format claim; `extract_artifact`'s
`launches_process,may_write_filesystem` effects are the producer's own
extraction output under the host temp area — nothing executed, nothing
written inside the lane repo). No knowledge admission (K untouched,
8/15); no README byte changes; PROVINCE byte-unchanged.

## C2 — calibration: orphan_sweep v5 — the unmatched-bare-citation and LOG-corpus gaps close inside the standing instrument

v5 supersession of the r83 instrument (`reports/round-84/
orphan_sweep5.py`, sha256 pinned below; v4 `reports/round-83/
orphan_sweep4.py`, v3, v2, v1 stay byte-untouched). Two named changes,
both routed by the r83 non-author closure:

7. Unmatched extension-bearing bare tokens are RECORDED, not skipped.
   The routed defect live: `v4-postlanding-recon.log` was cited BARE by
   the r83 report (×2), `corpus/lessons/round-83.md`, SCORECARD and
   LOG, matched NOTHING under HEAD or the working tree, and v4's
   classify_bare returned None — the pointer invisible to the
   instrument by construction (its PATH-form twin in the r83
   verifier-spotcheck lesson WAS recorded, as an absent row). v5
   records an unmatched bare token as an absent row iff it looks like a
   filename (tail extension, no `..`, not all digits+dots); known
   disclosed noise: dotted JSON field paths print as absent rows
   (recorded, not gating, dispositioned in the round lesson). The v4
   selftest leg BARE_UNMATCHED_SKIPPED is re-pinned to the prose class;
   the extension class moves to its own recorded-absent leg.
   BEFORE (red, committed): `v4-invisible-red.log` — v4 over the real
   pre-landing tree: ZERO instrument rows name the token (only the
   header's own prose mentions it; `SWEEP_BARE_TOKENS matched=302
   unmatched_skipped=1408`); `v5-red-unmatched-absent.log` — v5 over
   the SAME tree: row 973 `SWEEP absent v4-postlanding-recon.log |
   bare-token unmatched: no file named v4-postlanding-recon.log under
   HEAD or the working tree`, `unmatched_recorded_absent=47`.
   AFTER (green): the carry-in landing commits the receipt; v5 over the
   post-landing tree classifies the bare token `committed` (bare-token
   normalized) and the absent row is gone — `sweep5-real-after.log`
   (adjudication) must show `SWEEP committed v4-postlanding-recon.log`
   and zero `SWEEP absent v4-postlanding-recon.log` rows.

8. LOG.md joins the citation corpus (the routed "future registered
   change with its own red/green"). v4 normalized bare tokens found in
   fleet reports + lessons only; the lane's own LOG.md cites the same
   receipts and was a standing corpus blind spot. v5 appends LOG.md as
   a citation source; `SWEEP_CORPUS` gains a `log=` term (printed
   always, so the basis line's shape is grep-stable). Red/green: the
   hermetic selftest vector collects a synthetic LOG body's bare +
   path tokens under the log source name, and the log-disabled twin
   must collect nothing (mutant leg); on the real tree, `SWEEP_CORPUS
   fleet-reports=24 lessons=48 log=1` and CITED moves 705 (v4 red,
   log excluded) → 987 (v5 red, log included) on the same tree.

Selftest: v4's thirteen legs (one re-pinned to the prose class) + six
new vectors (unmatched recorded-absent / range+version skipped /
unmatched-absent mutant / log-corpus collected / log-corpus mutant) =
18 legs + `SWEEP_SELFTEST=pass`, exit 0. THREE frozen sed mutants (one
substitution each, recipes pinned below), each dying exit 1 attributed:
`BARE_TOKEN_CLASSIFICATION` → `selftest: bare-filename classification
drifted (bare-token class)` (the r83 recipe, unchanged);
`UNMATCHED_BARE_ABSENT` → `selftest: unmatched-absent recording drifted
(unmatched-absent class)`; `LOG_CORPUS` → `selftest: log-corpus
collection drifted (log-corpus class)`.

VERIFY conditions (all five must hold): (a) v5 selftest 18 legs + pass,
exit 0, from the committed blob; (b) all three sed-mutated copies die
exit 1 with their attributed last lines, each exactly one changed line;
(c) red receipts: v4-invisible-red.log shows zero instrument rows for
the token over the pre-landing tree, v5-red-unmatched-absent.log shows
the recorded absent row over the same tree; (d) the post-landing
real-tree receipt shows the token committed and names it in no absent
row, with the `SWEEP_CORPUS log=1` basis line present; (e) v4 bytes and
the r83 receipts unchanged (no rewrite of r83 evidence). KILL RULE: any
condition fails → v5 retained as a rejected candidate in
`reports/round-84/`, the carry-in landing stays (it is the closure
duty, not claim-consequent), and C2 records falsified honestly.

Boundary: v5 moves no criterion score; the moved quantity is the
standing capability's citation visibility (an unresolvable bare-cited
pointer stops being invisible; the lane's own LOG joins the count
basis). Counts remain per-revision-corpus (basis lines cited first):
the red receipts ran over the pre-carry-in tree, the green receipt over
the post-adjudication worktree; disclosed in each receipt header. The
recorded absent rows carry dispositions in the round lesson, not
re-litigation of historical rounds. Exit codes 0/1/64 unchanged
(absent never gates; only LANDABLE_ORPHANS does).

## Frozen sha256 pins

- `reports/round-84/orphan_sweep5.py` =
  `d9a7ba174ce3c30a4414fcebe8e074ea00d58bfce4cfbf2c2cdb76f888ca46cb`
- `reports/round-84/ag_probe2.py` =
  `6e1c07b568d982331c8ce17e9bdb659178066a68d2f44fa1e1e51fec8a71d1e1`
- `reports/round-83/orphan_sweep4.py` (frozen r83, unchanged) =
  `f520f8d69875d1ca83eb8daeddbffecb5f471bf5f5e6aba43bd97029fc2ea701`
  (the FULL sha — see `corrections.md` correction 1)
- fixture bytes (`corpus/fixtures/arc-r84/`):
  `R84Sample.zip` = 508 bytes,
  `f1f983eff6823a4ba23d714b25b69ca8e64484ddc00ec24043210311d729bc59`;
  `truth.json` = 1445 bytes,
  `0dcdf82cf58f4112a590ee1118a6648b86f81f55388aaafdc06adaa13964b703`;
  `build_zip.py` = 6637 bytes, sha
  `03ddcbdc5bd02393dde1f7b4993b9c2198a5651f6f21939e149f9e96d988230f`;
  `oracle_check.py` sha
  `230c359c53582ed30a8bfc0d1d449d12084c4e65ccbfa1fbd23a76ee2b545969`
- frozen sed mutant recipes (C2, one substitution each, verified by
  diff at demonstration):
  `sed 's/^BARE_TOKEN_CLASSIFICATION = True$/BARE_TOKEN_CLASSIFICATION = False/'`
  → dies `selftest: bare-filename classification drifted (bare-token class)`
  `sed 's/^UNMATCHED_BARE_ABSENT = True$/UNMATCHED_BARE_ABSENT = False/'`
  → dies `selftest: unmatched-absent recording drifted (unmatched-absent class)`
  `sed 's/^LOG_CORPUS = True$/LOG_CORPUS = False/'`
  → dies `selftest: log-corpus collection drifted (log-corpus class)`
  demonstration receipt `sweep5-mutant-kill.log` at the freeze;
  re-run over the committed blob at adjudication
  (`sweep5-mutant-kill-after.log`).

## §7 fresh-start gate (r71/r72/r73 rejected closures re-read; fresh probes 2026-11-02)

All three closures are K-admission claims whose wave Q-review surface
never settled on this host (r71: Q09/Q16 FAIL at the wave; r72: wave
unconfirmed, no worker outcomes; r73: 34/64 spawned, 0 settled, no vote
files) — a do-nothing control reaches each identically here; neither
r84 claim routes through K. Ruled out with fresh probes (receipt
`freshstart-probes.log`):

- **F android** (the only unrecorded F4 family): `REA_JADX_MCP_JAR`
  UNSET; no jadx on PATH — S448 stands; F4's honest exception stays
  10/11.
- **macho/signature families**: `rea capabilities` → `unsupported_host`
  (8 groups) — S453 stands.
- **K admissions**: the r74 L0 unanswered (re-read this round) — routed
  around, never treated as answered.
- **criterion C repair**: standing §9 disposition (r78–r83).
- **criterion R full extension / N attribution pair**: stay routed —
  this round's calibration claim is the v5 classes the r83 closure
  routed as instrument gaps instead.
- **A1 extension**: AVAILABLE and CLAIMED this round (C1) — the
  archive-side pair is the one route every standing ruling-out map left
  open ("available-but-unrecorded", r81/r82 scorecards).

## Carry-in dispositions (r83 non-author closure; addressed first, before any claim work)

1. **Unlanded cited receipt** — `reports/round-83/v4-postlanding-recon.log`
   regenerated from committed bytes only (recon recipe + instrument blob
   sha + basis movement disclosed in the receipt header; 7/7
   reconstruction-receipt byte-verify) and landed FIRST as
   `67e1470e5b2492df7b86632c5b3bafabfdd3e023`; the five citing surfaces'
   load-bearing values (`LANDABLE_ORPHANS=0`, exit 0) reproduce.
2. **Short-form sha pin drift** — `corrections.md` correction 1 (the
   five `f520f8d6…9701` sites named; the claims.md full sha governs;
   append-only, no in-place rewrite).
3. **Census pointer** — `corrections.md` correction 2 (the sanctioned2
   receipt is gone with the r83 scratch; the value is settled three
   ways: the committed killed-run output body, the verifier's
   independent re-run, and this round's exit-0 re-run receipt landed in
   the same commit).

## Sources opened this round (rows appended inside the Registry at the landing)

| row | path/command | decision |
|---|---|---|
| S466 | `PYTHONUTF8=1 rea capabilities` (provider `rea-artifact-graph`: the triple + `extract_artifact,inspect_artifact` `available: true`, `inspect_asset_catalog` `unsupported_host`) + `rea inspect-artifact --help` / `rea extract-artifact --help` + `preprobe-arc-shape.log`, opened 2026-11-02 | ADMIT (tier A, own-work environment) |
| S467 | `corpus/live/runs/round-84/inspect-artifact/` + `corpus/live/runs/round-84/extract-artifact/` (records, receipts, LEDGERs) + `corpus/fixtures/arc-r84/` (fixture, generator, truth, oracle), opened 2026-11-02 | ADMIT (tier A, own-work) |
| S468 | the r84 C2 class evidence — `reports/round-84/v4-invisible-red.log` (v4: zero instrument rows name the bare-cited token) + `v5-red-unmatched-absent.log` (v5: the recorded absent row) + the r83 closure's routed-defect note (`corpus/lessons/round-83-verifier-spotcheck.md`), opened 2026-11-02 | ADMIT (tier A, own-work) |

C1 is sourced by S466 + S467; C2 is sourced by S468.

## ERRATUM (appended 2026-11-02, pre-after-run instrument correction — no in-place rewrite of the frozen text above)

The freeze-time pin for `reports/round-84/ag_probe2.py` above
(`6e1c07b568d982331c8ce17e9bdb659178066a68d2f44fa1e1e51fec8a71d1e1`,
v2.0) is superseded by
`f9772ab1428ebe6e420ef285f2d9a02b26372c5556e8404ba825349f04721990`
(v2.1). v2.0 scanned `corpus/live/runs/round-*/` one level deep and
could never see the landed record layout
`runs/round-84/<operation>/inspection.json` — the c1-only separability
dry-run exposed this (it printed 3/5 against landed records) BEFORE any
after-run receipt existed. v2.1 matches `inspection.json` by name at
any depth under `runs/` (rglob); the round-1-era
`artifact-inspection.json` files remain unmatched. The red was re-run
with v2.1 over the same base archive: `ag2-red-v21.log`, values
unchanged (`A1V2_RECORDED=3/5 score=6.00`, the pair unrecorded). The
green after-runs all use v2.1. The c1-only dry-run mismatch is mined in
`corpus/lessons/round-84.md` (record-layout vs scan-shape class).
