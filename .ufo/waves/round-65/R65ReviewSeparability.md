PASS — C1 and C2 are causally separable on the frozen counter: at the after-state, removing the full C1 slice moves only `K_HELD`/`K_ROW C05`/`K_HELD_BACKED`/`K_HELD_BACKED_STRICT`; removing the C2 patch moves only the `C5_*` labels and `HOLDS_OK_V3`; every other label is byte-identical (filtered-label set sha256 equal). Two low-severity notes on the claims.md separability sentence, no blocker.

Seat: R65ReviewSeparability (leaf, read-only). Measured revision: `8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0` (HEAD, `git status --short` empty). Runtime: `Python 3.14.8`, one interpreter (counter runs scripts via `sys.executable -B`, measure.py:118,310). No tool installs.

# Method

Seven scratch trees, all built from committed bytes (`git archive`, never the dirty worktree), counter run from `/` with `TMPDIR=/tmp/r65sep/tmp-<tree>`:

```
cd / && git -C <lane> archive 8214e4dd… corpus | tar -x -C /tmp/r65sep --one-top-level=<T>
cd / && TMPDIR=/tmp/r65sep/tmp-<T> python3 -B <lane>/reports/round-65/measure.py /tmp/r65sep/<T>
```

Scratch lives at `/tmp/r65sep` (outside the fleet root) because this seat may write only its report file; nothing under the lane was written, no git/jj mutation was run.

| tree | construction | K_HELD | K_ROW C05 | BACKED | STRICT | C5_PRESENT | C5_ATTR | V3 | exit |
|---|---|---|---|---|---|---|---|---|---|
| **B** | HEAD build state | 8/14 | frontier | 8/14 | 8/14 | 2/2 | 2/2 | yes | 0 |
| **B_noC1** | B − entry − `fixtures/apk-r65` − S038–S041 | 8/14 | frontier | 8/14 | 8/14 | 2/2 | 2/2 | yes | 0 |
| **B_noC2** | B − C2 patch (both scripts at `3eebcdd`) | 8/14 | frontier | 8/14 | 8/14 | 0/2 | 0/2 | no | 0 |
| **A** | B + C05 row flip (simulated L1 admission) | **9/14** | **held** | 9/14 | 9/14 | 2/2 | 2/2 | **yes** | 0 |
| **A_noC1** | A − entry file only (row left held) | 9/14 | held | **8/14** | **8/14** | 2/2 | 2/2 | yes | 0 |
| **A_noC1_full** | A − entry − fixtures − S038–S041 − row revert | 8/14 | frontier | 8/14 | 8/14 | 2/2 | 2/2 | yes | 0 |
| **A_noC2** | A − C2 patch | 9/14 | held | 9/14 | 9/14 | 0/2 | 0/2 | **no** | 0 |

`A` (flip only, on the real landed entry) reproduces the frozen after-state exactly: `K_HELD=9/14`, `K_ROW C05 status=held`, `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2`, `STRICT_REJECT_WINDOW_SELFTEST=pass`, `HOLDS_OK_V3=yes`, exit 0 — i.e. the flip is the only byte missing at HEAD.

# Separability receipts (exact diffs of the filtered label set)

`T.flt` = all `K_*`, `C2_*`–`C5_*`, `HOLD*`, `HOLDS_*`, `README_TOKEN*`, `F_*`, `FRESH_ROWS`, `SAVED_RECORDS`, `STRICT_*` lines.

```
c0b30da1d2768c1cb8ac78672b91ac73861ad4cff7387737cdcecad2a419f894  B.flt
c0b30da1d2768c1cb8ac78672b91ac73861ad4cff7387737cdcecad2a419f894  B_noC1.flt
c0b30da1d2768c1cb8ac78672b91ac73861ad4cff7387737cdcecad2a419f894  A_noC1_full.flt
5248842eeeedb9283a2fa7563963b37a3ec995e20b55f31450d17725aa184c27  A.flt
92b1224d52fccdb0cd850d1b579d5706a0505fec683ee3008419f5c401341502  A_noC1.flt
93fbada00d54afb0ef46ff71a0b74d9e52ce90ed131ee6c42da41178a851ceef  A_noC2.flt
790f2928e627eeaa760a19c9d1d9022b6d81974d91f09e50ac815515fa76a53c  B_noC2.flt
```

1. **`A` vs `A_noC1_full` (full C1 slice removed at the after-state)** — moves only C1's own labels, nothing else:

```
-K_HELD=9/14 score=6.4              +K_HELD=8/14 score=5.7
-K_ROW C05 status=held              +K_ROW C05 status=frontier
 K_ROW C07 status=held
-K_HELD_BACKED=9/14                 +K_HELD_BACKED=8/14
-K_HELD_BACKED_STRICT=9/14          +K_HELD_BACKED_STRICT=8/14
 STRICT_REJECT_WINDOW_SELFTEST=pass old_window_miss=True
 SAVED_RECORDS=59
 README_TOKEN_LEGEND_MISMATCH=0 rows=[]
```
C2/C3/C4/HOLD/HOLDS_OK_V2/HOLDS_OK_V3/labels after those lines are byte-equal (implied by the sha256 identity with `B.flt`).

2. **`A` vs `A_noC2` (C2 patch removed at the after-state)** — moves only C2's own labels; K labels untouched:

```
-C5_CONTROL_PRESENT_verify_icon_languages.py=yes        +…=no
-C5_CONTROL_PRESENT_verify_multi_icon_states.py=yes     +…=no
-C5_CONTROL_PRESENT=2/2                                 +C5_CONTROL_PRESENT=0/2
 C5_CONTROLS_PASS=2/2
-C5_RECEIPT_KILLED=2/2                                  +C5_RECEIPT_KILLED=0/2
-C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2              +…=0/2
 HOLD_CALIBRATION=4/4
 HOLD_REPLAY=10/10
 HOLDS_OK=yes
 HOLDS_OK_V2=yes
-HOLDS_OK_V3=yes                                        +HOLDS_OK_V3=no
```

3. **`B` vs `B_noC1` (C1 stripped at the build state, pre-flip)** — *zero* label change; the three `.flt` files hash identically (`B_noC1.flt == B.flt == A_noC1_full.flt`). C1 contributes no counter label before the README flip. File-level proof of the strip:

```
Files B/corpus/SOURCES.md and B_noC1/corpus/SOURCES.md differ
Only in B/corpus/fixtures: apk-r65
Only in B/corpus/knowledge: round-65-apk-axml-byte-evidence.md
```
and the inverse for the C2 strip (`diff -rq B B_noC2`) lists exactly the two scripts.

4. **C1/C2 file sets are disjoint** (base `3eebcdd…` → HEAD):

```
corpus/SOURCES.md                                  |   4 +
corpus/fixtures/apk-r65/fixture.apk                | Bin 0 -> 947 bytes
corpus/fixtures/apk-r65/generator.py               | 234 +++++
corpus/fixtures/apk-r65/readout.py                 | 256 +++++
corpus/fixtures/apk-r65/truth.json                 | 103 +++
corpus/knowledge/round-65-apk-axml-byte-evidence.md| 162 ++++
corpus/lessons/round-65-verifier-spotcheck.md      |  76 ++++
corpus/lessons/round-65.md                         |  42 +++
corpus/verify_icon_languages.py                    |   3 +
corpus/verify_multi_icon_states.py                 |   3 +
```
No file is touched by both slices. `corpus/README.md` is **not** in the diff (0 lines) — C05 is still `frontier` and no other row changed.

# C2 fix-shape and attribution checks (all hold)

```
@@ -152,6 +152,9 @@ def check(r):                      # verify_icon_languages.py
+    forged_evidence=copy.deepcopy(receipt)
+    forged_evidence['evidence_id']='ev_6e055332…152dc3d'
+    require(not receipt_ok(forged_evidence,command,expected_hash,eid,raw_bytes),f'r{r}: forged receipt evidence accepted')
@@ -151,6 +151,9 @@ def check(round_id):               # verify_multi_icon_states.py
+    forged_evidence = copy.deepcopy(receipt)
+    forged_evidence['evidence_id'] = 'ev_8ed8898…8d4421'
+    require(not receipt_ok(…), f'r{round_id}: forged receipt evidence accepted')
```

- Insertions only, 3 lines per script; `receipt_ok` unchanged (`verify_icon_languages.py:118-120`) and the existing forged-command/forged-stdout controls retained — matches the frozen fix shape.
- Exactly one mutant-clause match per script: `grep -c "receipt\['evidence_id'\]==evidence_id"` → `1`, `1` (base and landed). Marker absent at base: `grep -c 'forged receipt evidence accepted' <base script>` → `0`.
- Both transplanted IDs are genuinely foreign **and real**, read from the receipts themselves: round-42 `inspection.raw.json`/`producer-receipt.json` `evidence_id=ev_6e0553…dc3d`, round-47 `…ev_8ed88…4421` (the languages script gets the multi script's r42 id and vice versa, as claimed).
- Attributed kills on the landed tree (`A.log`, identical in `B.log`):
```
MUTANT verify_icon_languages.py c5 exit=1 killed :: AssertionError: r47: forged receipt evidence accepted
MUTANT verify_multi_icon_states.py c5 exit=1 killed :: AssertionError: r42: forged receipt evidence accepted
C5_CONTROLS_PASS=2/2  C5_RECEIPT_KILLED=2/2  C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2
```
Red-before counterpart (`reports/round-65/measure-before.log`): `C5_CONTROL_PRESENT=0/2`, both `c5` mutants `exit=0 pass`, `…ATTRIBUTED=0/2`. Red→green is a clean, attributable transition on the frozen mutant.
- Fixture identity confirmed: `fixture.apk` 947 bytes, sha256 `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` (tree copy and lane copy agree). Entry carries `admission-status: candidate` (line 7) and no `admission-status: rejected` (0 matches), so the STRICT scan is not evaded.

# Findings

**F1 — LOW (wording).** claims.md separability sentence: “C1 touches corpus knowledge/registry/README only; C2 touches two verifier scripts only”. C1's actual footprint also includes `corpus/fixtures/apk-r65/` (4 files) and `corpus/lessons/round-65.md` — both named by the C1 claim paragraph itself but omitted from the separability sentence. Separability is unaffected (no shared file with C2, and both extras are unscored by the counter); the sentence simply understates C1's footprint. Evidence: diffstat above; `diff -rq B B_noC2` shows only the two scripts.

**F2 — LOW (latent coupling, not exercised).** `README_TOKEN_LEGEND_MISMATCH` (an input to `HOLDS_OK_V2`, hence to C2's `HOLDS_OK_V3`) exempts only rows whose status is `held` and keys `ROW_OPS["C05"] = {"inspect_android_package"}` (measure.py, ROW_OPS block + mismatch loop). If any C1 artifact had saved an `inspect_android_package` record while C05 is still `frontier`, V2 would read `no` and C2's V3 target would be unreachable until L1's flip — i.e. C1 would gate C2's label. Currently dormant and provably unexercised: `grep -rl 'inspect_android_package' corpus/live/runs` → 0 files, `F_FAMILIES` in every run lacks `android`, `README_TOKEN_LEGEND_MISMATCH=0` in all seven trees. Recommendation for the final measure: flip first, then measure (that ordering also removes the frontier row from the mismatch set).

**F3 — INFO (asymmetry that makes the backed guard load-bearing).** `K_HELD` is text-only. `A_noC1` (entry deleted, row left `held`) prints `K_HELD=9/14` while `K_HELD_BACKED=8/14` and `K_HELD_BACKED_STRICT=8/14` — so the frozen clause “`K_HELD_BACKED` and `K_HELD_BACKED_STRICT` equal at both ends” is what forces the entry's bytes to exist at the referenced path, and it works. Consequence: the round-end receipt must never be quoted on `K_HELD` alone.

**F4 — INFO (do not cite exit code as a C2 witness).** The probe's exit status is C2-invariant: `sys.exit(2 if not evaluable else 0 if holds_ok else 1)` and `holds_ok` (V1) does not include C5. `B_noC2` and `A_noC2` both exit **0** with `HOLDS_OK_V3=no`. The round-end condition correctly requires `HOLDS_OK_V3=yes` *and* exit 0, so this is a caution for readers, not a defect.

No finding rises above LOW. I found no path by which the C2 patch moves a K label, or by which the C1 slice moves a C5/HOLD label, on the landed tree.

# Residual risk

- Tree `A` is my **simulation** of L1's flip (my own row prose), not an admission. Only the knowledge-column path token and the trailing `held` are read by the counter, so prose beyond those is label-inert; but the actual wording L1 lands is unverified here.
- Pre-flip, C1 is invisible to the counter (`B ≡ B_noC1`, identical label-set sha256). The “moves only its own labels” property is therefore only demonstrable at the after-state, and the round's C1 payload is 100% carried by a hand-written README row plus the backed/strict guards. This is consistent with the frozen admission order (“K moves only on admission”), but it means the counter cannot independently witness C1's *content* — that rests entirely on the fresh-seat Q01–Q13 decisions.
- Final-tip measurement does not exist yet; all numbers here are on committed `8214e4d` and derived scratch trees.

# Verification gaps

- Q01–Q13 admission of the entry: out of scope for this seat (other reviewers).
- No `lsp` device is exposed to this seat; `receipt_ok` callsites and the clause/marker counts were checked by literal `read`/`grep` on committed bytes and are not presented as semantic proof. The decisive instrument here was executing the frozen counter over seven derived trees.
- `C5_CONTROL_PRESENT` alone can be spoofed by putting the marker string in a comment, but it cannot carry the claim alone: `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED` and `HOLDS_OK_V3` still require the live mutant kill, so the spoof surface is bounded (noted, not filed as a defect).
