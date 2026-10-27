# R71W1Reproduce — v6 `## Reproduce` replay (wave 1, pre-gate)

**VERDICT: HOLDS — all 24 embedded `$` commands of `corpus/knowledge/round-71-apk-axml-byte-evidence.md` run from the lane root with exit 0, empty stderr, and stdout byte-identical to each embedded output block; no misleading text found in the Reproduce-reachable prose; the round-70 four prose repairs are confirmed accurate against actual output.**

Seat: R71W1Reproduce (leaf, reviewer) · 2026-10-27 · read-only, no lane source edits.
Tree state tested: lane `revenger-shokunin`, git HEAD `18200a4b18e8dfce291a74028a9012ce4401ca10`, working tree with `reports/round-71/claims.md` and `reports/round-71/measure.py` modified (siblings' live edits); the v6 entry file itself clean. Entry sha256 `778af93bac4cca16f8ad38e2af3cb4fd984a2054c65ad4dcba513f1f392ea3bf`; `readout.py` `92e347c3…`, `entry_checks.py` `2d4f25f6…`, `derive_axml_anchors.py` `74d4c0d9…` — the last three equal the digests item 14 prints.

## Method

Harness in scratch (`/fast/scratch/hyaku/revenger-r71/R71W1Reproduce/repro_harness.py`, deleted after this report): parses every fenced block containing `$ ` lines from the entry, runs each command with `subprocess.run(cwd=<lane root>)`, byte-compares stdout lines and stderr against the block's embedded output. Independently re-hashed the ten pinned files with `sha256sum`, printed the cited `readout.py` locator lines, and diffed all command/output pairs against the round-70 v5.1 entry (`corpus/knowledge/round-70-apk-axml-byte-evidence.md`).

## Results

### 1. Every embedded command reproduces its block (exit 0, 24/24)

```
TOTAL=24 PASS=24 FAIL=0
```

All 24 lines printed `PASS l<line> exit=0 lines=<n>`. Blocks and line counts: items 1–10 single-fact readout calls (1 line each), `derive_axml_anchors.py` 20 lines, `--spec-quotes` 6, `--zip-layout` 20, `--oracle` 34, `--pins` 10, `--stdout-digest` 1, `--container` 3, `--axml-layout` 24. Zero diffs, zero stderr on every run. Representative receipts:

```
PASS l26 exit=0 lines=1 :: python3 -B corpus/fixtures/apk-r65/readout.py --fact archive
PASS l122 exit=0 lines=20 :: python3 -B corpus/derive_axml_anchors.py
PASS l181 exit=0 lines=34 :: python3 -B corpus/fixtures/apk-r65/entry_checks.py --oracle
```

### 2. Reproduce-section claims verified as written

- `python3 -B corpus/fixtures/apk-r65/readout.py` → exit 0, 15 stdout lines, sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — equals item 15's printed count and digest exactly ("Exit 0 and 15 stdout lines" holds).
- Single-fact form `--fact eocd` → exit 0, matches item 2's block.
- "The eight derivation flags of `entry_checks.py`" is complete and accurate: `entry_checks.py:297-300` `cmds` dict contains exactly `--pins, --eocd, --oracle, --zip-layout, --stdout-digest, --spec-quotes, --container, --axml-layout`; all eight ran exit 0; unknown flag prints docstring and exits 64 (`entry_checks.py:301-303`).

### 3. Item 14 pins are true, not just self-consistent

`diff` of `sha256sum` over the ten files vs `--pins` output digests: identical (and the ten byte sizes 947/2466/9599/11236/15062/4979/86255/174585/281157/1992 match). `PINS_DIGESTS_MATCH_INDEPENDENTLY`.

### 4. Round-70 prose repairs confirmed against actual output (misleading-text audit)

- Item 11 (`--spec-quotes`): output lines are `MATCH <snapshot file>: first line <n>, folded phrase present=True: <phrase>` — file, first-line number, searched phrase, exactly as the repaired description claims; the S049 header anchor "first line 7" matches `MATCH rea-android-applications.md: first line 7, …`.
- Item 12: numbered actual output — lines 16–18 of 20 are the three `MATCH APPNOTE 4.3.7/4.3.12/4.3.16` layout lines; lines 19–20 are `central.fixed_part`/`local.fixed_part` width comparisons. The repaired sentence ("output lines 16-18 of 20 … while the last two lines compare central/local fixed-part widths") is literally true.
- Observation/Q13 locators-only bounds: `readout.py:22`, `:76`, `:166`, `:211`, `:233-248` are cited as locators and no item compares their literals — checked: no command output contains a comparison of those source literals; consistent with the Q16 bound.
- Locator citations point at the claimed content: `:76` `sig_eocd = b"PK\x05\x06"`; `:105` `payload_off = lh_off + 30 + lh_name_len + lh_extra_len`; `:51-58` widths dict; `:155-168` string-pool decode with `:166` `utf8=bool(flags & 0x100), sorted_flag=bool(flags & 0x1)`; `:203` `aoff = base + 16 + attribute_start + i * attribute_size`; `:211` `… else strings[ans]`; `:233-248` dex header reads. `entry_checks.py:126` `check=True` backs item 15/Q05's "non-zero readout exit prints no line" clause.
- Q13's named surviving forged-block case (a different in-tree script printing fabricated lines passes the gate) is stated as unguarded and the entry credits no verifier for it — the gate run below confirms it still only checks declared-command stdout.

### 5. Freshness axis

All 24 command/output pairs are byte-identical with the round-70 v5.1 entry: `R70_CMDS=24 R71_CMDS=24 RETAINED_IDENTICAL=24/24`, no DRIFT and no NEW-in-v6 lines. This supports the `verified-at` retention claim ("output blocks below are retained byte-for-byte from the round-70 v5.1 entry"), and no fixture/script digest moved since the round-70 bytes (item 14 digests re-confirmed from disk today, 2026-10-27).

### 6. Advisory gate observation (recheck clause, current tree)

`python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md` → exit 0, `checked_blocks=24 problems=0`. `check_embedded_outputs.py` is unmodified in this tree; the registered counter/wave-2 gate run is not mine — this is the pre-gate replay only.

## Not run / out of scope

- `reports/round-71/measure.py` counter and C2 exit-2 classification (C2 repair not yet landed in this tree; gate exit-2 review is a separate seat).
- No `--self-test`, no producer/REA calls, no network, no fixture writes; nothing outside the lane root read except fleet-level contract files named by my task.

## Residual risk

- Replay proves stdout-equality at today's bytes, not provenance of the committed snapshot/script bytes (item 14's own caveat).
- The one-directional comparison clause Q13 names is real (verified by reading `check_embedded_outputs.py` behavior claims, not by injecting a mutant — mutant work belongs to the K68 seats).

## Verification gaps

None in scope: every Reproduce-reachable claim was exercised; no FAIL found, so no repair recommendation.
