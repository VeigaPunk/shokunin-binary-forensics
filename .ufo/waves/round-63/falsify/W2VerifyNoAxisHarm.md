# W2 — No-axis-harm verification (round 63 falsify)

**Verdict: PASS — no axis lost ground at lane tip `db55bd6488e24e956df5818ae34c2a043d7ddc12`.**
K held-set is identical to base (6/14, same six rows, denominator 14), F families are a strict
superset of the four base families, freshness is 18/18, calibration is 4/4 runnable and 10/10
replay, and `SCORECARD.md`/`LOG.md` are byte-identical to `55bcb6e` (round-63 append absent at
tip, as the dispatch note predicts). No HARM located. Two low-severity notes and one inherent
dependency are recorded below; neither is a score regression.

Axes named: **coverage K**, **coverage F**, **freshness hold**, **calibration runnability +
replay**, **frozen score-file custody**.

## Method (committed bytes only)

```sh
cd /home/vgpnk/Projects/shokunin/revenger-shokunin
git rev-parse HEAD                     # db55bd6488e24e956df5818ae34c2a043d7ddc12
git archive 55bcb6e corpus | tar -x -C /tmp/revenger-r63-noharm/base
git archive HEAD    corpus | tar -x -C /tmp/revenger-r63-noharm/tip
cd / && TMPDIR=/tmp/revenger-r63-noharm python3 -B \
  /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-63/measure.py \
  /tmp/revenger-r63-noharm/{base,tip}
```

The probe used is the **frozen** one: worktree `git hash-object` = `HEAD:reports/round-63/measure.py`
= `fc6fcbeb714d70fdf0a0e7b43e212ca842dea17d` (sha256 `3b7fba2d5243bbe0b723a99a53085130ff97010e23c8a59a8027f5f8992c5908`),
single-touch history at `54ab973`; `claims.md` blob `485f5a8f…` identical at `54ab973` and tip.
Python 3.14.8 (`/usr/bin/python3`), cwd `/`. No tool installed/updated, no pacman transaction.
No `lsp` device is exposed in this seat's toolset, so caller inspection used literal `grep`
(recorded here as the fallback, not as semantic proof).

## Measured: base `55bcb6e` → tip `db55bd6` (my own reruns)

| Label | base | tip | Delta |
|---|---|---|---|
| `K_HELD` | `6/14 score=4.3` | `6/14 score=4.3` | none |
| held row ids | C01,C04,C09,C11,C12,C13 | C01,C04,C09,C11,C12,C13 | none (superset trivially holds) |
| `K_ROW C06 status` | `partial` | `partial` | none (flip is post-wave) |
| `K_HELD_BACKED` | `6/14` | `6/14` | none |
| row denominator | 14 | 14 | none |
| `F_COVERAGE` | `4/8 score=5.0` | `5/8 score=6.2` | +firmware |
| `F_FAMILIES` | native-static, javascript, archives, evm | native-static, javascript, archives, **firmware**, evm | base ⊂ tip |
| per-operation counts | 10 keys | same 10 keys, identical values, +`inspect_firmware_regions: 1` | no count decreased |
| `FRESH_ROWS` | `18/18` | `18/18` | none |
| `C3_RECEIPT_KILLED_ATTRIBUTED` | `0/2` | `2/2` | improvement |
| `HOLD_CALIBRATION` | `4/4` | `4/4` | none |
| `HOLD_REPLAY` | `10/10` | `10/10` | none |
| `HOLDS_OK` / process exit | `yes` / 0 | `yes` / 0 | none |

My base run reproduces `reports/round-63/measure-before.log` **line for line** (including
`C3 … c3 exit=0 pass` and `PASS: 139 positive checks`), so the red-before is independently
reproducible and the tip is measured by the same code path.

Independent recount (not the probe) of the K/F/freshness predicates on the same two trees gave
the identical sets: held ids `{C01,C04,C09,C11,C12,C13}` on both; families base
`{archives,evm,javascript,native-static}`, tip those four + `firmware`; freshness 18 on both.

## Axis-by-axis evidence

### 1. SCORECARD.md — prior rows byte-identical; round-63 section absent (expected)

```
git diff 55bcb6e..HEAD -- SCORECARD.md | wc -l        # 0
git rev-parse 55bcb6e:SCORECARD.md HEAD:SCORECARD.md  # 4b45d8fd… both
sha256(55bcb6e:SCORECARD.md) = sha256(HEAD:SCORECARD.md) = 34f130b46c0fbfb8e3df905b58dc226b7722b0913f9a422187feebf04e4c775a
git diff --stat HEAD -- SCORECARD.md                  # empty (worktree clean)
grep -nE '^## ' SCORECARD.md | tail -1                # "## Round 62 — final measured coverage admission"
grep -c 'round-63\|round 63' SCORECARD.md              # 0
```

Whole-file identity is stronger than the required row-level check: **every prior row is
byte-identical**. `LOG.md` likewise unchanged (sha256 `092f99ff…` on both sides,
`git diff --stat 55bcb6e..HEAD -- LOG.md` empty). The round-63 append has not landed —
that is L1's post-wave act, not a delta I can certify; whenever it lands it must remain a pure
append (dependency recorded, not a failure).

### 2. Coverage K — no row lost

- README is byte-identical: sha256 `7ccd8d4484db710800a34a0b3718c8f73523e5c5666359e81e2f44ddbaca7ab6`
  at `55bcb6e` and at tip; `git diff 55bcb6e..HEAD -- corpus/README.md` empty. So all 14 rows,
  not only the six held rows, are byte-identical — no status change other than the none that
  occurred, and no denominator change (14 → 14).
- Held-set at tip `{C01,C04,C09,C11,C12,C13}` equals the base held-set → superset condition met
  with zero loss; every held row's cited `knowledge/*.md` still exists (`K_HELD_BACKED=6/14`,
  unchanged from base).
- `C06` remains `partial` at tip; the 7/14 target is not banked and therefore cannot be a
  "harm"; it stays pending on the post-wave flip.

### 3. Coverage F — all four base families retained

- Probe family sets: base `['native-static','javascript','archives','evm']` ⊂ tip
  `['native-static','javascript','archives','firmware','evm']`.
- Operation census is identical for every pre-existing key (`analyze_javascript_application` 6,
  `compare_application_versions` 1, `compare_javascript_export_shapes` 3, `extract_artifact` 2,
  `inspect_analysis_view` 1, `inspect_artifact` 4, `inspect_evm_interface` 7,
  `inspect_pe_resources` 30, `trace_application_feature` 2, `trace_javascript_semantics` 2);
  the only new key is `inspect_firmware_regions: 1`. No record was lost, replaced or re-typed.
- Run-file set base→tip differs by exactly two additions:
  `corpus/live/runs/round-63/inspection.json`, `corpus/live/runs/round-63/receipt.json`
  (104 → 106 JSON files under `corpus/live/runs`). `receipt.json` is not counted by the probe
  (it requires truthy `evidence_id` + non-null `normalized_result`), so there is no count
  inflation from the receipt.
- Byte identity outside round-63 paths: all **443** files under `corpus/live` + `corpus/fixtures`
  outside `corpus/live/runs/round-63/` and `corpus/fixtures/firmware-r63/` have identical
  sha256 base→tip (`diff` empty); `git diff --diff-filter=MDR 55bcb6e..HEAD -- corpus/live
  corpus/fixtures` prints nothing. `corpus/fixtures/archive-r2/{fixture.zip,truth.json}` and
  `corpus/live/runs/20261012T164246Z/artifact-inspection.json` still hash
  `857989f5…`, `7df773bf…`, `2fec924b…` — matching the S033 row's cited digests exactly.
- `corpus/knowledge/` gains exactly one file (`round-63-zip-central-directory-evidence.md`);
  every pre-existing knowledge file is byte-identical.

### 4. Freshness — 18/18

`FRESH_ROWS=18/18` at both base and tip; the two assertion sources
(`corpus/knowledge/seed.md`, `corpus/knowledge/2026-10-12-rea-readiness-checklist.md`) are
byte-identical base→tip. Corpus-wide, non-round-63 bytes are unchanged (see §3), so no
assertion row could have been quietly retired.

### 5. Calibration — runnability 4/4, replay 10/10, attribution 2/2

- `HOLD_CALIBRATION=4/4` and `HOLD_REPLAY=10/10` at tip (same at base). The ten-verifier census
  is unchanged: `corpus/verify_*.py` count is 10 at both commits; the new
  `corpus/live/runs/round-63/oracle_check.py` is outside that glob and does not enter the
  denominator.
- `C2_CONTROLS_PASS=2/2`, `C2_RECEIPT_B_KILLED=2/2`, `C2_D2_KILLED=2/2`,
  `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2` — unchanged from base and from `measure-before.log`.
- C3 attribution is real, not a crash: tip c3 mutants exit 1 with last lines
  `AssertionError: r55: forged receipt accepted` and `AssertionError: r36: forged receipt accepted`;
  the probe's attribution predicate is `rc != 0 and "forged receipt" in last.lower()`, and no
  `could-not-evaluate` line appeared, so `mutate_c3` matched **exactly one** site in each final
  file (regex `receipt['command']==command`, `receipt['fixture_sha256']\s*==\s*expected_hash`).
- The verifier diffs are additive: `verify_icon_states.py` extracts the existing conjuncts
  verbatim into `receipt_ok(...)` **including** the `if round_id != 36` evidence-ID exemption,
  then adds the forged-`fixture_sha256` control; `verify_named_multi_icon_states.py` does the
  same for the command conjunct and adds the `' --forged'` control. No conjunct, no
  `req(...)` count and no saved-input assertion was removed — the named verifier's positive
  count rises 139 → 142 (the three added control checks). Both controls pass on the unmutated
  tree, so the control is not vacuous.

## Findings by severity

1. **LOW (custody, not axis harm) — dirty worktree under `corpus/` at tip.**
   `git status --porcelain` shows ` M corpus/lessons/round-63.md` (committed blob `e32fd37`,
   worktree `2601cdf`; it is L1's in-flight lesson correction, task "Locating the incorrect
   lesson sentence"). My numbers are taken from `git archive HEAD`, so they describe committed
   bytes only. Any later gate that runs on the worktree instead of a commit archive will measure
   uncommitted bytes; the lesson file is not read by the probe, so no axis number changes.
2. **LOW (documentation drift, inherent to the frozen C3 fix shape).**
   `corpus/live/runs/round-58/LEDGER.md` and `…/round-58/reviewer.md` quote
   `PASS: 139 positive checks; …`; the patched verifier now prints `142` because each of the
   three saved rounds adds one forged-receipt control check. Those records are byte-preserved
   (as required) and were true when written; no script or gate pins `139` (grep found only that
   prose), so nothing fails. Residual: a reader diffing historical quoted output against a
   current run sees a 139/142 mismatch.
3. **INFO (dependency, not a regression). — F 5/8 is an existence count.**
   The frozen F predicate counts a parsed dict with truthy `evidence_id` and non-null
   `normalized_result` and does not verify provenance or the byte oracle; peer
   `W2AttackProbeF` demonstrated a hand-written record also yields 5/8. The tip's F gain is
   therefore contingent on C2's real `npx rea-agents@6.5.0` run plus oracle agreement (other
   seats' receipts), not on the counter value. Nothing in this check can or should upgrade that
   existence count into an admission.
4. **INFO — K 6/14 at tip.** The C1 target (7/14) is not yet banked because C06 is still
   `partial`; that is the expected pre-flip state, and the falsify wave's Q-decisions gate the
   flip. No held row was traded away to prepare it.

## Residual risk

- This seat certifies **non-regression at `db55bd6`**, not any post-wave state. When L1 appends
  the round-63 SCORECARD section and flips C06, the append must be verified again for purity
  (prior rows byte-identical) and for K 7/14 — a different commit than the one measured here.
- The C3 patch protects the two frozen conjuncts only. Peer `R63MutC3` M3 (recorded as M35 in
  `corpus/lessons/round-63.md`) shows `stdout_sha256` in `verify_icon_states.py` remains
  deletion-tolerant; that is disclosed coverage debt, not lost ground, and this check does not
  credit beyond 2/2.
- `S033`'s cited digests were re-verified here by sha256 and match the committed bytes; S032's
  quote fidelity is out of this seat's scope (W2ReopenS032/S033 own it).

## Verification gaps

- No language-server semantic check was possible in this seat (no `lsp` device in toolset);
  caller/definition checks for the two patched verifiers used `grep` over `corpus/`, `SCORECARD.md`,
  `LOG.md`, and `reports/` — the only consumers found are prose records and the frozen probe,
  both covered above.
- I did not re-execute the REA producer or any firmware payload (out of scope, and the wave
  forbids target execution). The C2 real-run claim is untouched by this report.
- Heavy scratch `/tmp/revenger-r63-noharm/*` is removed after this report lands.

## Tooling record

No installs or updates. `/usr/bin/python3` 3.14.8 and coreutils only; no pacman transaction
(pacman is paused host-wide). No files outside this report path and `/tmp/revenger-r63-noharm/`
were written; no git mutation was performed (read-only `git rev-parse/archive/diff/show/status/
ls-tree/hash-object` only).
