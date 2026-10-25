SEPARABLE-WITH-NAMED-SHARED-LABEL — C2 is fully separable from C1 (its labels reach pass values on the *unrepaired* base gate, measured), but C1's frozen aggregate is not: `HOLDS_OK_V6` folds in `C7_V3_CLEAN`, so C1's pass predicate cannot be satisfied without C2's entry existing and being gate-clean. The coupling is one-directional, disclosed in both frozen predicates, and inert under C2's prescribed kill rule; it does not confound either verdict.

# Separability audit — round 68 (C1 calibration × C2 coverage)

scope: read-only. No file outside this report was written. No git/jj mutation, no pacman (no tool installs were needed).

frozen inputs reverified first:
- `reports/round-68/measure.py` sha256 `0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766` — matches `claims.md:7`.
- build tip `4232235` (gate sha256 `b89183bec2fd3b94f5b0acc828a0d3fe16f6a98dde1d7752616da85d08a8e0ca`), base `f165908` (gate sha256 `19007bebeb4d60dafd826df108584933ebb3f2b1e6ab112925ea6c6cab3e697d`).

## 1. Dependency graph read out of the counter (the whole question, statically)

C1's labels (all gate-local):
- `C7_GATE_PRESENT` `measure.py:397`; `C7_SELFTEST` `:405-407`; `C7_CONTROL_PASS` `:408`; `C7_MUTANT_KILLED`/`_ATTRIBUTED` `:412-428`; `C7_RED_ON_R65_CANDIDATE` `:429-431` (reads `knowledge/round-65-…`, frozen since r65); `C7_V2_CLEAN` `:433-437` (reads `knowledge/round-67-…`, frozen since r67); `C7_NEG_SPOOF_*` `:486-494`.
- `c7_targets` closes as `… and c7_mut_attributed == 1 and c7_red and c7_v2_clean)` at `measure.py:521-522`, and `holds_ok_v5 = (holds_ok_v4 and c7_targets)` at `:523` — **no v3 input**.
- `holds_ok_v6 = (holds_ok_v5 and c7_neg_killed == 1 and c7_neg_attributed == 0 and c7_v3_clean)` at `measure.py:525-526`, where `c7_v3_clean` is set by `gate --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md` (`:440-446`).

C2's labels (all README/knowledge-local):
- `K_HELD_BACKED` `:43`, `K_HELD_BACKED_STRICT` `:64`, `C05_KNOWLEDGE_COLUMN`/`C05_SINGLE_V3` `:68-76`, `README_TOKEN_LEGEND_MISMATCH` `:100-107`, `HOLDS_C2_V3` `:111-117` — no gate input.
- `C7_V3_CLEAN` is required by C2's frozen predicate (`claims.md:121`) but is not an input to `HOLDS_C2_V3`.

Answer to the two direct questions:
- **Does any C1 label depend on the v3 entry?** Yes, exactly one: `c7_v3_clean`, and through it the C1 aggregate `HOLDS_OK_V6` (`measure.py:526`), which C1's pass branch requires (`claims.md:57`). No *attribution* label of C1 does.
- **Does any C2 label depend on the gate's repair?** No. C2's counter labels never read the gate; and its one gate-derived predicate label, `C7_V3_CLEAN`, is provably identical on the unrepaired and repaired gate (§2, experiments A/B).

`claims.md:34-37` ("Neither counter reads the other's artifact") is therefore **factually false in both directions** — the counter reads the gate for `C7_V3_CLEAN` and the v3 entry for `HOLDS_OK_V6`. The predicates themselves disclose the shared label (`claims.md:57`, `:121`); only the justification sentence overstates. claims.md is frozen, so this belongs in the round report/lesson, not a claims edit.

## 2. Four measured cells (counterfactuals on committed trees, counter unmodified)

| tree | gate | v3 entry | C1 attribution core | C2 labels |
|---|---|---|---|---|
| base `f165908` | base | absent | 0/1 | 8/14, uncovered |
| **Exp C** = `4232235` corpus, v3 **removed** | repaired | absent | **1/1** | 8/14, `HOLDS_C2_V3=no` |
| **Exp D** = `f165908` corpus, v3 + README flip | **base** | present | **0/1** | **9/14, held, `HOLDS_C2_V3=yes`** |
| measured tip | repaired | present | 1/1 (target) | 9/14 (target) |

Exp A/B (the purity of `C7_V3_CLEAN`):
```
A: cd /tmp/sepA && gate --entry round-68-…md   -> checked_blocks=17 problems=0   exit 0
B: cd /tmp/sepB && gate --entry round-68-…md   -> checked_blocks=17 problems=0   exit 0
```
A = repaired gate (`4232235`), B = **base** gate (`f165908`, sha `19007be…`), same v3 bytes. Identical. `C7_V3_CLEAN` is invariant under the C1 delta; the diff between the gates is confined to the self-test path (`require(...MARKER)` shadowing vs the explicit `caught` branch), not entry mode.

Exp C (C1's artifact alone) — `/tmp/sepC` = `4232235` corpus with the v3 file deleted:
```
C7_SELFTEST=pass :: SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
C7_RED_ON_R65_CANDIDATE=yes exit=1 :: checked_blocks=15 problems=1
C7_V2_CLEAN=yes exit=0 :: checked_blocks=16 problems=0
C7_V3_CLEAN=n/a (no v3 file)
C7_CONTROL_PASS=1/1   C7_MUTANT_KILLED=1/1   C7_MUTANT_KILLED_ATTRIBUTED=1/1
C7_NEG_SPOOF_KILLED=1/1   C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1
HOLDS_OK_V2=yes  HOLDS_OK_V3=yes  HOLDS_OK_V4=yes  HOLDS_OK_V5=yes  HOLDS_OK_V6=no
K_HELD_BACKED=8/14  C05_STATUS=uncovered  C05_SINGLE_V3=no  HOLDS_C2_V3=no
counter exit 0
```
→ The complete C1 attribution target is reached with C2's artifact absent, yet **C1 still cannot pass** because `HOLDS_OK_V6=no` (`c7_v3_clean=False`). This is the named coupling, measured, and the smallest counterexample that exhibits it: target attribution, no v3, C1 aggregate red.

Exp D (C2's artifact alone) — `/tmp/sepD` = base `f165908` corpus + v3 + `derive_axml_anchors.py` + `snapshots/ResourceTypes.h` + the C05 README row flip, **base gate untouched**:
```
K_HELD_BACKED=9/14  K_HELD_BACKED_STRICT=9/14  C05_SINGLE_V3=yes  C05_STATUS=held
README_TOKEN_LEGEND_MISMATCH=0 rows=[]  HOLDS_C2_V3=yes
C7_V3_CLEAN=yes exit=0 :: checked_blocks=17 problems=0
C7_MUTANT_KILLED=1/1   C7_MUTANT_KILLED_ATTRIBUTED=0/1   HOLDS_OK_V5=no   HOLDS_OK_V6=no
counter exit 0
```
→ Every C2 label reaches its pass value **without C1's repair**. Coverage is independent of calibration.

## 3. Does the shared label `C7_V3_CLEAN` break separability? How to read it

It does not break either verdict, and it must be read as a **joint label, not a C1 label or a C2 label**:

- It is a function of *(gate presence, v3 presence, v3 bytes)*. Its value is `rc==0` from `gate --entry v3`; the gate does not read `admission-status` (no hit in `corpus/check_embedded_outputs.py`), so C2's kill rule — retain the file, mark it `admission-status: rejected`, keep every byte (`claims.md` §C2 kill rule) — leaves `C7_V3_CLEAN` unchanged. **A C2 falsification therefore cannot false-fail C1**, and an out-of-contract deletion would already violate the void conditions (`claims.md:180` prior rejected candidates altered / fixture freeze).
- Its v3-independence of the repair (A vs B) is why C2's pass does not consume C1's change: the gate that satisfied `C7_V3_CLEAN` in Exp D is the *unrepaired* one. C2 depends on the round-67 gate's *existence*, not on this round's repair.
- Its inclusion in `HOLDS_OK_V6` is redundant for C1's purpose. C1 already carries an anti-over-kill guard that uses a frozen, non-C2 artifact: `C7_V2_CLEAN` (`measure.py:433-437`, `:522`). Adding v3 as a second clean sample inside V6 buys no additional C1 protection (different bytes, same property) and is the sole cross-artifact edge in the graph.

Reading rule for adjudication this round (frozen predicates, no edit): C1's verdict is the attribution core (`C7_MUTANT_KILLED_ATTRIBUTED`, `C7_NEG_SPOOF_*`, `C7_SELFTEST`, `C7_CONTROL_PASS`, `C7_RED`, `C7_V2_CLEAN`, `HOLDS_OK_V5`) **and** `HOLDS_OK_V6`, where the v3 conjunct is only satisfiable because C2's artifact is in the measured tree. If the two claims ever separate in outcome (C2 fails and its file is removed/renamed), C1's V6 reads `no` for a reason that has nothing to do with attribution — report that explicitly rather than as a calibration failure.

## 4. Impacted axes and smallest safe correction

impacted: **calibration (C1) aggregate only**. Coverage's labels are unaffected in both directions.

Smallest safe correction, for the *next* counter revision (claims.md is frozen; never retro-edit a rule a seat has scored):
```
- holds_ok_v6 = (holds_ok_v5 and c7_neg_killed == 1 and c7_neg_attributed == 0
-                and c7_v3_clean)
+ holds_ok_v6 = (holds_ok_v5 and c7_neg_killed == 1 and c7_neg_attributed == 0)
```
i.e. drop `c7_v3_clean` from `measure.py:526` and keep the label as a standalone joint readout cited by C2's predicate only (`claims.md:121`), where it is already the natural place for it. This removes the only cross-artifact edge, loses no C1 power (`C7_V2_CLEAN` retains the anti-over-kill guard), and leaves C2's enforcement of v3's presence to `C05_SINGLE_V3` + `K_HELD_BACKED`. Alternative (`c7_v3_clean = (not v3.is_file()) or rc == 0`) also restores C1's independence but silently weakens C2's cited label — prefer the removal.

## 5. Two ancillary findings the flip depends on (both measured, both cheap traps)

1. **The C05 flip must move the knowledge ref into field 3, not just flip the status.** `C05_SINGLE_V3`/`C05_KNOWLEDGE_COLUMN` read `c05_line.split("|")[3]` (`measure.py:68-76`), and `K_HELD_BACKED` reads `l.split("|")[3]` (`:43`). The current row `corpus/README.md:34` carries `— ` in field 3 and the evidence prose in field 4. Exp E (`/tmp/sepE`, base + v3 + status-only flip):
```
K_HELD=9/14 score=6.4    K_HELD_BACKED=8/14    K_HELD_BACKED_STRICT=8/14
C05_KNOWLEDGE_COLUMN=-   C05_SINGLE_V3=no      C05_STATUS=held   HOLDS_C2_V3=no
```
A status-only flip inflates the headline `K_HELD` to 9/14 (`score=6.4`) while the backed count stays 8 — a spoof surface. Quote `K_HELD_BACKED`, never `K_HELD`, as this row's coverage number; Exp D is the correct shape (`K_HELD_BACKED=9/14` with the knowledge ref in field 3 and `| held |` last).

2. **`README_TOKEN_LEGEND_MISMATCH` is inert to the C05 flip — the nominal shared README read in C1's chain is harmless.** `holds_ok_v2` includes `len(mismatch) == 0` (`measure.py:512-515`), i.e. C1 reads the same file C2 flips. But `mismatch` only flags rows whose *last* column is `frontier` (`:100-104`, `ROW_OPS`), and C05's last column is its status. Measured in both directions: `README_TOKEN_LEGEND_MISMATCH=0 rows=[]` with C05 `uncovered` (base receipt `:13`) and with C05 `held` (Exp D, Exp E). No perturbation path from C2's flip to C1's chain.

Entry provenance check while testing purity: v3's item-11 command is **repo-relative** — `corpus/knowledge/round-68-apk-axml-byte-evidence.md:128` `$ python3 -B corpus/derive_axml_anchors.py`; `grep home/vgpnk` over the entry returns no hits. So `C7_V3_CLEAN` is a pure function of (gate, measured tree), with no leak to the lane working tree. (The wave brief describes that command as an absolute path; the landed bytes are relative — the landed form is the safer one, and any seat asserting the absolute form is describing a version that is not in the tree.)

Block-count consistency across the three candidate generations, from the same labels: r65 `15` blocks `1` problem (red, `C7_RED_ON_R65_CANDIDATE=yes`), r67 `16` blocks `0` (clean), r68 `17` blocks `0` (clean) = r67 + item 11. No block was dropped by the anchor repair.

## 6. Commands replayed (exact)

```sh
git -C $R archive 4232235 corpus | tar -x -C /tmp/sepA
git -C $R archive f165908 corpus | tar -x -C /tmp/sepB ; cp v3 + derive + snapshots into /tmp/sepB
cd /tmp/sepA && python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md
cd /tmp/sepB && python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md
git -C $R archive 4232235 corpus | tar -x -C /tmp/sepC && rm /tmp/sepC/corpus/knowledge/round-68-apk-axml-byte-evidence.md
cd / && TMPDIR=/tmp/revenger-r68-sepC python3 -B $R/reports/round-68/measure.py /tmp/sepC
# /tmp/sepD, /tmp/sepE: f165908 corpus + v3 + README row variants; same counter invocation
```

verdict restated: the two claims do not confound each other's outcomes — C2 admits on its own bytes over the base gate (Exp D), C1's attribution reaches target with C2's bytes absent (Exp C) — but C1's frozen aggregate carries one disclosed, one-directional, kill-rule-inert edge to C2's artifact via `C7_V3_CLEAN`. Name it in the settlement, quote `K_HELD_BACKED` for coverage, and drop the v3 conjunct from `HOLDS_OK_V6` in the next counter revision.
