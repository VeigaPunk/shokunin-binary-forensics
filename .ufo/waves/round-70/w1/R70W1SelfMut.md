# R70W1SelfMut — C2 checker mutation probe (wave 1, advisory)

ALL-SIX-KILLED — all six SM-class neutralization mutants are detected by the frozen counter's own fixtures (printed `SELF_MUTANTS_KILLED` drops 6/6 → 5/6 per mutant, each loss attributable to the neutralized class), and the clean-path always-1 mutant is caught by `SELF_CLEAN_FIXTURE=nonzero`. The checker is shown able to fail (pristine: each planted defect scores exactly its class, exit 1) and able to pass (clean fixture 0, exit 0). No lane file was edited by this seat; /tmp scratch deleted at return.

## Setup — attack target = candidate-commit bytes, scratch only

- Scratch: `/tmp/revenger-r70-R70W1SelfMut` (tree, per-run copies, mutants, logs). Every read/write absolute.
- Tree built exactly as tasked: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive --format=tar -o $S/cand.tar aa1842fac199aa524930e5565ed3715de5f84c6d corpus SHONEN.md SCORECARD.md SKILL.md` → extracted 6.4 MB.
- Frozen counter verified: `sha256sum reports/round-70/measure.py` → `488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76` (matches claims.md).
- Blob identity of the attack target: `git -C <lane> show aa1842f…:corpus/self_assessment_check.py | sha256sum` → `6a24baa158ec168e3d4315d91c8a9e35481976c065bb8323b5a61f4b665c90fb`, identical to the checker inside the scratch tree.
- Mutants (scratch-only, each compile()-checked): the class function's entire body replaced by `return 0` — `sm1` checker:55, `sm2` :64, `sm3` :90, `sm4` :109, `sm5` :114, `sm6` :137; CLEAN mutant replaces checker:242 `n = sum(got.values())` → `n = 1` (clean-fixture path neutralized: always prints `SELF_MISMATCH=1`, exit 1). Mutant sha256: SM1 `0fd924a5…eed71`, SM2 `c6393fe6…a2e1`, SM3 `92682768…ad74c`, SM4 `1f4d3244…eed9`, SM5 `c358e90f…5cc7`, SM6 `3d60cecd…89f7e`, CLEAN `66c4cbcd…c1d76`.

SM1 mutant diff (all six class mutants have this same shape):

```diff
 def sm1(root):
-    readme, quality = txt(root / "corpus/README.md"), txt(root / "corpus/QUALITY.md")
-    ids = [int(x) for x in re.findall(r"^\| Q(\d+) \|", quality, re.M)]
-    m = re.search(r"`QUALITY\.md` — admission criteria Q01[–-]Q(\d+)", readme)
-    if not ids or not m:
-        return 1
-    return 0 if int(m.group(1)) == max(ids) else 1
+    return 0  # MUTANT: class neutralized
```

CLEAN mutant diff:

```diff
         got = evaluate(root, lane)
         for k in CLASSES:
             print(f"{k}={got[k]}")
-        n = sum(got.values())
+        n = 1  # MUTANT: clean path neutralized, always print 1
```

## Detector

Frozen counter, its own usage: `python3 -B reports/round-70/measure.py TREE`. Kill semantics at measure.py:115 — a class mutant counts killed iff `rc == 1 and n == 1 and per.get(cls) == "1"` on the counter's own `build_self_fixture` defect fixture; the clean leg requires `rc == 0 and SELF_MISMATCH == 0` (measure.py:108-109). Nine parallel runs (BASELINE, SM1..SM6, CLEAN, RESTORED), each on its own copy of the archive tree with its checker overlaid; the source tree copy was never mutated.

## Per-mutant results (printed by the frozen counter)

| run | counter exit | SELF_CLEAN_FIXTURE | SELF_MUTANTS_KILLED | HOLDS_C2_V5 | tree SELF_MISMATCH | mutant detected |
|---|---|---|---|---|---|---|
| BASELINE | 0 | 0 | 6/6 | no | 12 exit=1 | — |
| SM1 | 0 | 0 | 5/6 | no | 11 (−1) | yes |
| SM2 | 0 | 0 | 5/6 | no | 5 (−7) | yes |
| SM3 | 0 | 0 | 5/6 | no | 10 (−2) | yes |
| SM4 | 0 | 0 | 5/6 | no | 11 (−1) | yes |
| SM5 | 0 | 0 | 5/6 | no | 11 (−1) | yes |
| SM6 | 0 | 0 | 5/6 | no | 12 (−0; SM6=0 on this tree) | yes |
| CLEAN | 0 | nonzero | 6/6 | no | 1 exit=1 | yes (clean conjunct) |
| RESTORED | 0 | 0 | 6/6 | no | 12 exit=1 | restore byte-exact |

Verbatim RUN lines (all runs also printed `K_HELD_BACKED=8/14 score=5.7`, `HOLDS_C1_V5=no`, `HOLDS_C3_V1=yes`, `HOLDS_OK_V7=yes`):

```
RUN BASELINE exit=0 K_HELD_BACKED=8/14 score=5.7 SELF_MISMATCH=12 exit=1 SELF_CLEAN_FIXTURE=0 SELF_MUTANTS_KILLED=6/6 HOLDS_C2_V5=no HOLDS_C1_V5=no HOLDS_C3_V1=yes HOLDS_OK_V7=yes
RUN SM1 exit=0 ... SELF_MISMATCH=11 exit=1 SELF_CLEAN_FIXTURE=0 SELF_MUTANTS_KILLED=5/6 HOLDS_C2_V5=no ...
RUN SM2 exit=0 ... SELF_MISMATCH=5 exit=1 SELF_CLEAN_FIXTURE=0 SELF_MUTANTS_KILLED=5/6 HOLDS_C2_V5=no ...
RUN SM3 exit=0 ... SELF_MISMATCH=10 exit=1 SELF_CLEAN_FIXTURE=0 SELF_MUTANTS_KILLED=5/6 HOLDS_C2_V5=no ...
RUN SM4 exit=0 ... SELF_MISMATCH=11 exit=1 SELF_CLEAN_FIXTURE=0 SELF_MUTANTS_KILLED=5/6 HOLDS_C2_V5=no ...
RUN SM5 exit=0 ... SELF_MISMATCH=11 exit=1 SELF_CLEAN_FIXTURE=0 SELF_MUTANTS_KILLED=5/6 HOLDS_C2_V5=no ...
RUN SM6 exit=0 ... SELF_MISMATCH=12 exit=1 SELF_CLEAN_FIXTURE=0 SELF_MUTANTS_KILLED=5/6 HOLDS_C2_V5=no ...
RUN CLEAN exit=0 ... SELF_MISMATCH=1 exit=1 SELF_CLEAN_FIXTURE=nonzero SELF_MUTANTS_KILLED=6/6 HOLDS_C2_V5=no ...
RUN RESTORED exit=0 ... SELF_MISMATCH=12 exit=1 SELF_CLEAN_FIXTURE=0 SELF_MUTANTS_KILLED=6/6 HOLDS_C2_V5=no ...
```

(`...` = identical context fields; full lines captured in the run transcript.)

## Attribution — mutated checker on the counter's own fixtures

The counter itself does not print a class name for a lost mutant; its attribution condition is `per.get(cls) == "1"` (measure.py:115). Verified externally by running each mutated checker directly on the counter's own `build_self_fixture(SMk=True)` fixture (`--root <fixture> --lane <lane>`), replicating the counter's exact invocation:

```
SM1 defect=SM1 exit=0 SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=0 SELF_MISMATCH=0
SM2 defect=SM2 exit=0 SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=0 SELF_MISMATCH=0
SM3 defect=SM3 exit=0 SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=0 SELF_MISMATCH=0
SM4 defect=SM4 exit=0 SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=0 SELF_MISMATCH=0
SM5 defect=SM5 exit=0 SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=0 SELF_MISMATCH=0
SM6 defect=SM6 exit=0 SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=0 SELF_MISMATCH=0
SM1_onclean defect=clean exit=0 ... SELF_MISMATCH=0   (same all-zero shape for SM2..SM6 _onclean)
CLEAN_onclean defect=clean exit=1 SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=0 SELF_MISMATCH=1
CLEAN_onSM1 defect=SM1 exit=1 SM1=1 SM2=0 SM3=0 SM4=0 SM5=0 SM6=0 SELF_MISMATCH=1
```

Each neutralized class no longer fires on its own planted defect (exit 0, all-zero) — exactly why measure.py:115 counts it not-killed; the loss is attributable to that class. Neutralizations create no false positives (all `_onclean` runs score 0).

Pristine instrument sanity (same fixtures, unmutated checker):

```
PRISTINE_clean defect=clean exit=0 SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=0 SELF_MISMATCH=0
PRISTINE_SM1 defect=SM1 exit=1 SM1=1 SM2=0 SM3=0 SM4=0 SM5=0 SM6=0 SELF_MISMATCH=1
PRISTINE_SM2 defect=SM2 exit=1 SM1=0 SM2=1 ... SELF_MISMATCH=1
PRISTINE_SM3 defect=SM3 exit=1 ... SM3=1 ... SELF_MISMATCH=1
PRISTINE_SM4 defect=SM4 exit=1 ... SM4=1 ... SELF_MISMATCH=1
PRISTINE_SM5 defect=SM5 exit=1 ... SM5=1 ... SELF_MISMATCH=1
PRISTINE_SM6 defect=SM6 exit=1 ... SM6=1 ... SELF_MISMATCH=1
```

The checker is shown able to fail (each planted defect scores exactly its class, total 1, exit 1) and able to pass (clean 0, exit 0).

## Restoration evidence

- RESTORED run: checker first overwritten with the SM1 mutant bytes (hash ≠ pristine verified), then restored to exact pristine bytes (sha256 re-verified `6a24baa1…` before its counter run) → `SELF_MUTANTS_KILLED=6/6` again, `SELF_CLEAN_FIXTURE=0`.
- Scratch tree checker final sha256 = `6a24baa1…` — the source tree copy was never mutated; every mutant lived in a per-run copy (`run_<tag>/`).
- Lane file untouched by this seat: all writes were scratch + this report.

## Advisory findings (wave 1, not kill-rule inputs)

1. **Mid-wave lane drift (stability).** The lane working tree's `corpus/self_assessment_check.py` changed during this wave: session-start sha `6a24baa1…` (= candidate blob) → now `ae1c62aa9879f9de426beb20a09dbf2973ec841a501d364cb3e83eb119bbe282`; `git status --porcelain` → ` M corpus/self_assessment_check.py`; the diff is one line in `sm3` (:99): `for size in re.findall(r"(\d[\d,]*) bytes", text):` → `for size in re.findall(r"(?<![\w-])(\d[\d,]*) bytes", text):`. The tasking said the checker would not change this wave; this probe attacked the candidate-commit bytes (correct per the stable-targets rule), but wave-2 mutation seats must re-pin the exact bytes they attack.
2. **Candidate-tree SM2=7 (claims' base Before said 4).** Unnamed on the candidate tree: `check_embedded_outputs.py`, `derive_axml_anchors.py`, `derive_axml_anchors_r68.py`, `lint_entry.py`, `q15_tree_id_check.py`, `self_assessment_check.py`, `snapshots/`. The base-unnamed four plus exactly three new ones; the C1/C2/C3 README repairs must add `lint_entry.py` (C1), `self_assessment_check.py` (C2), `derive_axml_anchors_r68.py` (C3) for SM2 to reach 0.
3. **Counter structure: both C2 conjuncts are load-bearing.** The mutant leg alone does NOT catch an always-1 checker (CLEAN run printed `SELF_MUTANTS_KILLED=6/6`); only the `SELF_CLEAN_FIXTURE` conjunct does. Conversely the clean leg alone would not catch class neutralizations. Keep both in `HOLDS_C2_V5`.
4. **Baseline context on the candidate tree** (out_BASELINE.log, counter exit 0): `SM1=1 SM2=7 SM3=2 SM4=1 SM5=1 SM6=0`, `SELF_MISMATCH=12 exit=1`, `HOLDS_C2_V5=no` — expected pre-repair state; `C1_GATE=checked_blocks=22 problems=0 exit=0 ok=yes`, `C1_LINT=LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0 exit=0`, `HOLDS_C3_V1=yes` (`EMB_R68=checked_blocks=17 problems=0`, `EMB_R65=… problems=1`, `EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1`), `HOLDS_OK_V7=yes`, `HOLD_REPLAY=10/10`, `GATE_SELFTEST=exit 0`.

## Tooling record

No installs or upgrades (pacman paused host-wide; used python3 3.14.8 stdlib, git, diff, tar only).
