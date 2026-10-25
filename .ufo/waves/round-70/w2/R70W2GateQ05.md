# R70W2GateQ05 — Q05 readiness/capability gate on the landed C05 v5.1 candidate

PASS — the one exit-status claim (Reproduce: `Exit 0` and 15 stdout lines) carries its probe (item 15) and re-derives exactly on the landed bytes; the provider surface carries an explicit no-claim fence in three places; the v4 exit-2 refusal clause is dropped, not re-asserted; no readiness, capability or refusal-path sentence in the entry lacks a probe or states a wrong value.

Seat: R70W2GateQ05 (fresh wave-2 revenger seat; no wave-1 files read before this verdict). Target: `corpus/knowledge/round-70-apk-axml-byte-evidence.md` at lane commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd`, `admission-status: candidate` (line 11). Criterion: `corpus/QUALITY.md` Q05 — "A readiness or capability claim carries a probe against the real surface: its command, date and observed exit, output or Evidence ID. Presence, configuration or acquisition is not capability." Reject when: "the claim rests on a configured value, an install, or an unrechecked older probe."

## Method

All commands were run by me on a `git archive 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd` extraction at `/tmp/revenger-r70-R70W2GateQ05/` (deleted after this report). Probe-byte tie-in — the scripts I probed are the item-14 pinned bytes:

```
$ sha256sum corpus/fixtures/apk-r65/readout.py corpus/fixtures/apk-r65/entry_checks.py corpus/fixtures/apk-r65/fixture.apk
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  readout.py      (= entry item 14 line 4)
2d4f25f6894ac86ced3c9986abd7cdbcf4c6d2aab477cda6dc515585c129b1f9  entry_checks.py (= entry item 14 line 5)
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  fixture.apk     (= entry item 14 line 1)
```

Line numbers below are the landed entry's own lines (file is 322 lines; `git show 17ee7f87…:<path>` equals the extraction).

## Q05-relevant sentence inventory (complete sweep)

Grep sweeps over the landed bytes for `exit|ready|readiness|refus|capab|install|provider|check=True|degrades|shows|proves|demonstrat|ensures|guarantee|detects|guards|non-zero|fail|mismatch|superset` produced every candidate sentence. Results:

### 1. Exit-status claim — probed, re-derives (sound)

- Entry line 322 (Reproduce): "Exit 0 and 15 stdout lines; item 15's command prints their count and digest and runs the readout with `check=True`."
- In-entry probe: item 15, lines 237-238 — command `$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --stdout-digest`, embedded line `readout stdout: 15 lines, sha256 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247`.
- My re-derivation: `python3 -B corpus/fixtures/apk-r65/readout.py` → `exit=0`, `wc -l` = 15, `sha256sum` = `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — identical to the embedded item-15 line. `entry_checks.py --stdout-digest` re-run prints the same line, exit 0.
- The `check=True` mechanism claim is in the digest-pinned source: `entry_checks.py:274-275` — `out = subprocess.run([sys.executable, "-B", str(HERE / "readout.py")], capture_output=True, text=True, cwd=str(CORPUS.parent), check=True).stdout` (inside `def stdout_digest():`, line 273). No try/except wraps it.

### 2. Provider readiness — fenced, no claim exists (nothing to probe)

- Line 10 (coverage-map): "Not covered: install/signature verification, dex validity or execution, provider (`inspect_android_package`) readiness or output, general AXML or ZIP-parser behavior beyond this fixture."
- Line 292 (cross-lane note): "this lane ran no provider and makes no readiness claim (Q05 fence)".
- Line 284 (Unknown): "nothing about install validity, signature blocks, dex program validity or any provider's behavior is claimed; the fixture is inert and no producer was called."
- S049's scope (line 2) is bounded to "the route-scope sentence only … not provider execution". No sentence in the entry asserts provider readiness, capability or a refusal path, so Q05 has no unprobed provider claim to locate. The S049 quote itself is located by the item-11 `--spec-quotes` command (embedded `MATCH rea-android-applications.md: first line 7 … present=True`).

### 3. v4's rejected Q05 defect — repaired by drop

The round-69 v4 entry (`3f5edbc206351232a3d2d801334dd930499ccaf5:corpus/knowledge/round-69-apk-axml-byte-evidence.md`, line 6, `admission-status: rejected` at its line 11) carried the exit-2 refusal clause "(exit 2 on a missing or ambiguous symbol)" for `derive_axml_anchors.py`, credited with no probe — the routed repair was "probe-or-drop the exit-2 clause (Q05)" (claims.md §C1). In the v5 bytes the clause is gone: line 6 (S047 row) reads "anchor: `corpus/derive_axml_anchors.py` and `corpus/snapshots/ResourceTypes.h`, digests printed in item 14" with no exit/refusal claim, and grep finds no `exit 2`, `refuse` or `ambiguous` sentence anywhere in the 322 landed lines. Dropped, not re-asserted — the repair class is satisfied.

### 4. Two behavioral sentences inside §Q-map rows — unprobed in-entry, verified TRUE by my probes, not Q05 defects

These are the closest calls; recorded with evidence so other seats and L1 can weigh them:

- Line 302 (§Q-map Q05 row): "…whose `--stdout-digest` runs the readout with `check=True`, so a non-zero readout exit prints no line." — a counterfactual refusal-path claim about the gate, with no in-entry probe. Tamper test on a scratch COPY (`cp -r`, then appended `sys.exit(1)` to the copy's `readout.py`; lane file untouched): `entry_checks.py --stdout-digest` → `exit=1`, **0 bytes on stdout**, stderr traceback ending `subprocess.CalledProcessError: … returned non-zero exit status 1.` The sentence is TRUE; no wrong value exists to locate.
- Line 310 (§Q-map Q13 row): "…a command whose flag is corrupted still passes if its output is a superset of the embedded lines (the readout degrades an unknown flag to its full dump)…" — a non-refusal behavior claim about the readout, with no in-entry probe. My probe: `python3 -B corpus/fixtures/apk-r65/readout.py --bogus-flag` → `exit=0`, 15 stdout lines (the full dump), 0 bytes stderr. TRUE; no wrong value exists to locate.

Why these do not fail Q05: (a) both sit inside §Q-map rows, not in the observation items 1-17 that carry the entry's load-bearing values — no value in items 1-17 rests on either sentence; (b) line 310 is the unguarded-clause disclosure Q13 itself mandates ("other clauses are named as unguarded") — a limitation statement about the entry's own committed tooling, the opposite of a capability credit, and the entry explicitly "credits no verifier for either"; (c) line 302 is the probe-soundness argument for the very claim Q05 requires to be probed, its mechanism (`check=True`) resolves in the digest-pinned source at `entry_checks.py:274-275`; (d) both statements are true by direct probe, so Q05's reject conditions (configured value / install / unrechecked older probe producing a wrong or stale claim) are not met — there is no defect value a corrected sentence would fix. I note for the record that line 310's parenthetical is the only behavioral sentence in the entry carrying neither a command nor a source-line citation; if a future round reclassifies it as a capability claim, the one-line fix is a probe (`readout.py --bogus-flag` → exit 0, 15 lines) or a source citation.

### 5. verified-at past-execution claim — re-derives

Line 8: "the embedded-output gate `corpus/check_embedded_outputs.py --entry` and the lint `corpus/lint_entry.py --entry` both ran on the built bytes" — both commands are named in the header's `recheck:` (line 9) and re-run clean on the landed bytes: gate `checked_blocks=24 problems=0`, exit 0; lint `LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0 LINT_HEADER=0`, exit 0. The claim is re-derivable by its named command (M19's requirement); its digest-scope limits are already declared in item 14.

### 6. Configuration claims — not capability, and each is exercised by its own item

Line 322's "eight derivation flags" and the single-fact form are configuration claims; each flag is exercised by an item command with embedded output (items 2, 11-14, 16-17 use `--eocd`, `--spec-quotes`, `--oracle`, `--pins`, `--container`, `--stdout-digest`, `--zip-layout`, `--axml-layout`), and item 2 uses exactly the advertised single-fact form. Under Q05 ("presence, configuration or acquisition is not capability") these carry no capability assertion.

## Decision

**PASS.** The entry's only exit-status claim carries its probe and re-derives byte-for-byte; the provider surface is fenced with no readiness/capability claim anywhere; the previously rejected exit-2 clause is dropped; the two unprobed behavioral sentences in the §Q-map rows are true limitation/probe-mechanism disclosures about the entry's own tooling, verified by my independent probes, with no wrong value to locate and no observed value resting on them. No sentence implying a refusal path, exit status, provider readiness or capability lacks a probe while stating anything false.

## Residual risk and verification gaps

- Line 310's parenthetical ("the readout degrades an unknown flag to its full dump") and line 302's counterfactual ("a non-zero readout exit prints no line") carry no in-entry probe; both verified true by my probes (outputs above), but a stricter classification of either as a "capability claim" would demand an in-entry probe line or source citation. This is the single judgment call in this verdict; everything else is mechanical.
- I did not re-derive items 1-14 and 16-17's APK byte values (outside Q05 scope; the embedded-output gate's clean run mechanically confirms every embedded line appears in its command's stdout, and other seats own those criteria).
- Wave-1 records (`.ufo/waves/round-70/w1/`) were not read before this verdict, per seat discipline; this report is an independent record, available for post-hoc cross-check only.
