# MutationR100 — scoped findings (round 100, wave w1)

Role: mutation-tester (leaf seat). Axes: calibration, coverage. Milestone: pre-register mutants for the v9
new legs and cap_apk_probe, run them after FROZEN, report kills and survivors per mutant.

FROZEN commit: `173abe91a80d79336ca9228643c63d41e0e7635c` (read from `.ufo/waves/round-100/w1/FROZEN`).
Instrument shas at that commit (verified in a git clone of it, see §0):

| path (lane-relative) | sha256 |
|---|---|
| `reports/round-100/c1_k_admit_counter9.py` | `8e2eafc80726789aafa2ee491123de8b46ac63945692edaed6c474540e9885e8` |
| `reports/round-100/cap_apk_probe.py` | `b2c9d189e75c582b06ce5636af17267869e70965c13d33ced10f501a03f2c71a` |
| `reports/round-100/forge_reach9.py` | `3acdd3a98b5dcdbdc3534f32c9be52f990da7f2994b498f6a107cc5678bdd362` |
| `reports/round-100/controls_c2.sh` | `479f690e6aeb4d43eab64edba2df4429ed2be9cb5dafc843ea1065c2f31ee408` |
| `reports/round-99/c1_k_admit_counter8.py` (v8 base) | `620dfca9959572449638cab203485555c5d45f5a8e89c5b68121ffc2d3023581` |

## 0. Pre-registration evidence (mtime and order)

- `.ufo/waves/round-100/w1/MutationR100/mutants.json` written before any mutant generation with detectors and before
  FROZEN. Stamp: `PRereg_STAMP=2026-11-05T23:13:58Z`, mtime epoch `1793920431`. FROZEN appeared at
  `2026-11-05T23:20:58Z` (loop `i=8`).
- Disclosed pre-FROZEN activity: one dry-run of mutant *generation only* (no detector, no score) on the then-unfrozen
  v9 bytes, to validate that every find-string and del-leg site resolves uniquely. Output discarded; the frozen run
  regenerated everything from the FROZEN clone.
- Byte drift disclosed: `mutants.json` records `sha256_at_prereg` = `5ea82db0…` for the v9 counter (the bytes at
  prereg time). ExecCounterV9 revised twice before FROZEN (`8e2eafc8…` final). The prereg lists leg names, not
  find-strings, for the counter, so its targets are unaffected; sites were re-derived from the FROZEN bytes.
  `mutants.json` was not edited. The probe `sha256_at_prereg` (`b2c9d189…`) matches FROZEN.

## 1. Tooling

Nothing installed, upgraded or removed. System `python3` only. Decoders used as already present on PATH:
androguard 4.1.4 (`~/.local/bin/androguard`), apktool 3.0.3 (`~/.local/bin/apktool`). No pacman. git used
read-only (`archive`, `rev-parse`, `status`) plus `git clone --shared` of the lane into scratch (not a lane mutation).
apktool wrote its framework cache under `~/.local/share/apktool` (allowed).

## 2. Harness problems found and fixed (disclosed, not hidden)

1. **Extract-tree run is void.** My first full run used a `git archive` extract of FROZEN. `build_fresh99.py`
   runs `git -C <lane> archive <rev>` and an extract has no `.git`, so the honest fixture was empty. forge_reach9
   fails closed (missing rows count as accepted) and printed `BASE_FORGE accepted=12/12`, `R100_CONTROL_*=control-bad`,
   self-test rc=1 for the **unmutated** counter. Those numbers say nothing about the counter. Archived as
   `receipts/run-extract-VOID/`. Re-run on a `git clone --shared` checked out at FROZEN (`TOPLEVEL` verified equal to
   the clone dir): baseline `R100_ACCEPTED=0/12`, controls `control-ok`, `R100_STUB_SELFTEST=ok`, `R100_VERDICT=met`.
   **Recommendation to L1:** forge_reach9 should refuse to count a builder failure as "accepted" silently in
   the summary, or at least print a builder-failure rc that is distinct from a counter accept. The current output
   looks like a counter failure.
2. **Disk.** `/fast` reached 100% host-wide (256K free) during my supplement run; my scratch was 5.6 GB, mostly
   forge work trees. I removed my own work trees (receipts kept), freed ~6.8 GB, and added per-run cleanup to the
   driver. `/fast` is now 55% used. Other seats may hit the same wall.

## 3. Pre-registered mutants (`mutants.json`) — results

Driver: `.ufo/waves/round-100/w1/MutationR100/mutate_r100.py --tree <FROZEN clone> --scratch <dir>` (exit 0).
Receipts: `receipts/final-clean/results-prereg.json`, `run.out`, `run.err`, `ctl/<mutant>/control-{stub,flip}.log`.
Baseline (unmutated, FROZEN): `forge_rc=0`, `accepted=0/12`, `selftest_rc=0 selftest_ok=True`; probe
`rc=0 verdict=pass`; `controls_c2.sh` → `C2_CONTROLS=control-ok` (rc 0).

Kill rules, verbatim from `mutants.json`: v9 = `forge_reach9` shows the corresponding vector accepted OR the
mutant's `--self-test` fails; probe = `controls_c2.sh` control-bad OR genuine-fixture verdict changes.

### 3a. v9 del-leg (12 mutants, one per new leg; deletion operator from r99 `mutate8.build`)

| mutant | corresponding vector | forge rc | corresponding vector accepted | self-test rc | self-test | killed (prereg rule) |
|---|---|---|---|---|---|---|
| del-C1_PASS_NOTE_FLOOR | C02-N1 | 1 | no | 1 | FAIL | yes (self-test) |
| del-C1_VOTER_PRESENT | C02-N2 | 1 | no | 1 | FAIL | yes (self-test) |
| del-C1_QMAP_POINTER | C02-N3 | 1 | no | 1 | FAIL | yes (self-test) |
| del-C1_EVIDENCE_RESOLVES | C02-N4 | 1 | no | 1 | FAIL | yes (self-test) |
| del-C1_SECTIONS | C02-N5 | 1 | no | 1 | FAIL | yes (self-test) |
| del-C1_SURFACE_TEXT | C02-N6 | 1 | no | 1 | FAIL | yes (self-test) |
| del-C1_NA_SHARE | C14-N1 | 1 | no | 1 | FAIL | yes (self-test) |
| del-C1_ARTIFACT_COPY | C14-N2 | 1 | no | 1 | FAIL | yes (self-test) |
| del-C1_DERIV_RERUN | C14-N3 | 1 | no | 1 | FAIL | yes (self-test) |
| del-C1_RECORD_PINNED | C14-N4 | 1 | no | 1 | FAIL | yes (self-test) |
| del-C1_BODY_DIGEST | C14-N5 | 1 | no | 1 | FAIL | yes (self-test) |
| del-C1_ANCHOR_VERBATIM | C14-N6 | 1 | no | 1 | FAIL | yes (self-test) |

Self-test line for every one: `SELFTEST_C1V9=FAIL legs=128`; the first failure is the honest fixture, e.g.
`SELFTEST FAIL: c02:honest: expected pass; failing=C1_PASS_NOTE_FLOOR` (`receipts/dbg-selftest-mut/st.out`, mutant
del-C1_PASS_NOTE_FLOOR, rc 1).

**Reading (important for calibration).** The v9_legs `checks` dict entry is deleted, so `checks[name]` raises
`KeyError` at `c1_k_admit_counter9.py` v9_legs loop, which is caught (`except … KeyError …`) and recorded as
`(False, "unreadable: KeyError…")`. A deleted leg is therefore equivalent to a force-fail on every applicable profile.
The 12 "kills" show that the honest fixture still runs each leg (the self-test and honest control break), **not** that
any leg's vector is caught: **0/12 vector-specific kills**. The same operator's r99 kills (9/9 del-leg by self-test,
MutationR99 §3) carry the same caveat and should be read as overstated.

### 3b. Probe (4 mutants, exact find/replace on `cap_apk_probe.py`; each find verified unique)

| mutant | edit | controls_c2 (rc) | genuine rc / verdict | killed (prereg rule) |
|---|---|---|---|---|
| probe-drop-tamper-leg | tamper leg replaced by `(True,"")` | `control-bad` (1) | 0 / pass | **yes** (stub control: `CAP_TAMPER_DETECTED=pass`, `CAP_APK_VERDICT=pass`, rc 0) |
| probe-compare-only-package | `FIELDS = ("package",)` | `control-ok` (0) | 0 / pass | no — survived |
| probe-skip-fixture-sha | `sha_ok = True` | `control-ok` (0) | 0 / pass | no — survived |
| probe-swallow-decoder-failure | decoder failure path sets `ok = True` | `control-ok` (0) | 0 / pass | no — survived |

Why the three survive, by reading the control recipe and the probe:
- **compare-only-package.** The stub decoders print the true manifest and the flip control changes `versionCode`
  inside the APK; for the flip the verdict is still `fail` because `CAP_FIXTURE_SHA=fail` (see gap below), so the
  per-decoder `versionCode` comparison is never the deciding leg in any control. Tamper checks only `versionName`.
- **skip-fixture-sha.** `controls_c2.sh` flip leg (lines ~175-186) does **not** require `CAP_FIXTURE_SHA=fail`; it
  appends `# CAP_FIXTURE_SHA=fail ABSENT` to the log and still prints `C2_CTRL_FLIP=refused` when rc=1 and
  `CAP_APK_VERDICT=fail`. The mutant's flip log reads `# CAP_FIXTURE_SHA=fail ABSENT` and the control is still
  `control-ok` (receipt `ctl/probe-skip-fixture-sha/control-flip.log`).
- **swallow-decoder-failure.** Decoders succeed on genuine and stub inputs, so the failure branch never runs in any
  control, and the genuine verdict is unchanged.

### 3c. Pre-registered totals

16 pre-registered mutants: **13 killed** (12 del-leg by self-test only, 1 probe by control), **3 survived**
(probe compare-only-package, skip-fixture-sha, swallow-decoder-failure). Vector-specific kills by the pre-registered
rule: **0/12** del-leg, **1/4** probe.

## 4. Post-FROZEN supplement (NOT part of the pre-registered table; labelled as attack re-runs)

Why: §3a shows the del-leg operator cannot test leg coverage. The pre-registration's own wording is "delete/negate the
leg's condition"; the negated form (condition replaced by `(True, "forced-pass")`) is the coverage test and is
reported here, separately, because I chose to add it after seeing §3a. Driver:
`.ufo/waves/round-100/w1/MutationR100/supplement_r100.py`, output `receipts/final-clean/supplement.json`,
`supp2.out`, `supp2.err` (rc 0). Kill rule unchanged (corresponding vector accepted, or self-test fails).

### 4a. Force-pass variants of each v9 leg (12)

| mutant | corresponding vector accepted | accepted vectors total | self-test | killed |
|---|---|---|---|---|
| fp-C1_PASS_NOTE_FLOOR | yes (C02-N1) | 1 | FAIL (rc 1) | yes, vector |
| fp-C1_VOTER_PRESENT | yes (C02-N2) | 1 | FAIL | yes, vector |
| fp-C1_QMAP_POINTER | yes (C02-N3) | 1 | FAIL | yes, vector |
| fp-C1_EVIDENCE_RESOLVES | yes (C02-N4) | 1 | FAIL | yes, vector |
| fp-C1_SECTIONS | yes (C02-N5) | 1 | FAIL | yes, vector |
| fp-C1_SURFACE_TEXT | yes (C02-N6) | 1 | FAIL | yes, vector |
| fp-C1_NA_SHARE | yes (C14-N1) | 1 | FAIL | yes, vector |
| fp-C1_ARTIFACT_COPY | yes (C14-N2) | 1 | FAIL | yes, vector |
| fp-C1_DERIV_RERUN | yes (C14-N3) | 1 | FAIL | yes, vector |
| fp-C1_RECORD_PINNED | yes (C14-N4) | 1 | FAIL | yes, vector |
| fp-C1_BODY_DIGEST | yes (C14-N5) | 1 | FAIL | yes, vector |
| fp-C1_ANCHOR_VERBATIM | yes (C14-N6) | 1 | FAIL | yes, vector |

**12/12 vector-specific kills.** Each leg is the only leg that refuses its vector: forcing any one leg open accepts
exactly its own vector and no other. The base `R100_VECTOR` lines show one failing leg per vector, so there is no
redundant refusal. Coverage of the 12 vectors is one-to-one. The self-test also fails on each force-pass, which is
correct.

### 4b. Probe attacks (inputs beyond the frozen controls; rc and verdict from `supplement.json`)

| attack input | unmutated probe | compare-only-package | skip-fixture-sha | swallow-decoder-failure | drop-tamper |
|---|---|---|---|---|---|
| A1 androguard shim rewrites `versionCode="1"`→`"2"` in its real output (package/versionName correct) | rc 1 `fail` (ANDROGUARD=fail) | **rc 0 `pass`** (ANDROGUARD=pass) | rc 1 | rc 1 | rc 1 |
| A2 fixture copy with `truth.json` image.sha256 = 64 zeros, decoders untouched | rc 1 `fail` (FIXSHA=fail) | rc 1 | **rc 0 `pass`** (FIXSHA=pass) | rc 1 | rc 1 |
| A3 androguard shim exits 1 on every input | rc 1 `fail` (ANDROGUARD=fail) | rc 1 | rc 1 | rc 1 verdict, **ANDROGUARD=pass** printed | rc 1 |

Readings:
- **compare-only-package: killed by A1** (unmutated refuses a decoder that lies about `versionCode`; the mutant accepts,
  rc 0). This is the attack the frozen controls did not contain.
- **skip-fixture-sha: killed by A2** (a wrong digest with correct decoders is accepted, rc 0). The frozen controls did
  not contain it; the frozen flip control's refusal came from the decoder leg.
- **swallow-decoder-failure: killed on the output contract only.** A3's verdict stays `fail`/rc 1 because the
  tamper leg also fails when the decoder fails, so the verdict-level kill rule does not catch it. The mutant prints
  `CAP_ANDROGUARD=pass` for a decoder that failed. That is a broken per-decoder line, not a wrong verdict. I count
  it as a survivor under the frozen rule and as a line-level kill here.
- **drop-tamper: killed** (stub control, §3b).

## 5. Gaps for the L1 (findings; I did not edit any frozen or sibling file)

1. **`reports/round-100/controls_c2.sh` does not enforce claims §C2(iii).** Claims say the byte-flipped fixture
   "must make the probe print `CAP_FIXTURE_SHA=fail` and `CAP_APK_VERDICT=fail`". The script's flip leg requires only
   rc 1 and `CAP_APK_VERDICT=fail`; `CAP_FIXTURE_SHA=fail` is appended as an annotation (`ABSENT` is logged, not
   refused). Consequence: §3b skip-fixture-sha survives the frozen controls. The claims-level predicate is unaffected
   because the frozen C2 predicate is the probe's verdict on the genuine fixture, but the control text is weaker than
   the claim. This is the L1's call; I have not changed it.
2. **C2 controls do not exercise the per-decoder versionCode/versionName legs or the digest leg** (§3b). The
   attacks A1 and A2 are not in claims.md; they are attack re-runs. Consider adding them as controls before the next
   round.
3. **The del-leg operator is a coverage artifact** (§3a). Recommend a force-pass (negate) operator in mutate8 for
   future rounds, and a re-read of MutationR99 §3's 9/9 del-leg kills.
4. **forge_reach9 counts builder failure as "accepted"** (§2.1). The extract-tree baseline reported 12/12 for an
   unmutated counter. Suggest a distinct builder-failure outcome.

## 6. Scratch and hygiene

- Receipts (wave dir): `.ufo/waves/round-100/w1/MutationR100/receipts/` — `run-clone/` (prereg run, ctl logs,
  mutant sources), `final-clean/` (results-prereg.json, supplement.json, run/supp outputs, `shas.txt` with 32
  entries), `dbg-selftest-mut/` (honest self-test FAIL lines for del-C1_PASS_NOTE_FLOOR, forge run output),
  `run-extract-VOID/` (void extract-tree run, see §2.1), `supp-partial/` (first supplement attempt, stopped by disk
  full at fp-C1_EVIDENCE_RESOLVES; its three completed force-pass results are identical to the final run).
- Scripts (wave dir): `mutants.json` (prereg, unedited), `mutate_r100.py`, `supplement_r100.py`.
- No lane file written. No git mutation. No commit. No `corpus/`, `reports/round-[0-9]*/` (except read), `SCORECARD.md`
  or sibling file touched. No message to other seats beyond the two builder interface questions (answered).
- Scratch `/fast/scratch/hyaku/revenger-r100/MutationR100/` deleted before yield (see final yield).

## 7. Open items

1. L1 decides §5.1 (controls_c2.sh enforcement of §C2(iii)) before the C2 target is scored.
2. L1 decides whether to add the attacks A1/A2 as frozen controls for round 101 (or report them as the attacks they are).
3. Whether the force-pass operator is adopted in mutate8 going forward (I have not changed mutate8 or any r99 file).
