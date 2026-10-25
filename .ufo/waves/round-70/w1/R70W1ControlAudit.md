# R70W1ControlAudit — do-nothing control attack on the frozen r70 predicates

REACHED — all three mechanical predicates (`HOLDS_C1_V5`, `HOLDS_C2_V5`, `HOLDS_C3_V1`) print `yes` on
trees that perform **none** of the claimed work: C1 by a 17-echo entry with no source row, C2 by a 27-line
checker keyed to the counter's own fixture literals over unrepaired bytes, C3 by a `pins.json` pointing at a
stub that echoes the entry's own 17 lines while the S046-digest script sits unused. Wave-1 findings are
advisory (claims.md "Landing order" step 2); none is a kill-rule input. Every control below is built on a
`git archive 3f5edbc…` scratch tree under `/tmp/revenger-r70-R70W1ControlAudit/`; no lane file was written,
no git write was issued.

Axes named: **C1 reachability** (does the predicate bind to evidence or to block count), **C2 attribution**
(can the graded artifact grade itself), **C3 provenance** (is the digest conjunct about the same file the
derivation conjunct runs).

Counter used unchanged: `python3 -B reports/round-70/measure.py <tree>`, sha256
`488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76` (verified this seat).

## Control I — C1: tools overlay + README flip + 17 echo blocks, zero evidence

Builder: `control_i()` in `/tmp/revenger-r70-R70W1ControlAudit/build.py`; tree `/tmp/revenger-r70-R70W1ControlAudit/I`.
Entry = 68 lines: header keys present but `source: none — this control carries no source row`, a 15-row
§Q-map of `| Qnn | pass | x |`, and one fence containing 17 copies of

```
$ python3 -c "print('ok')"
ok
```

Counter output (actual):

```
K_HELD_BACKED=9/14 score=6.4
K_HELD_BACKED_STRICT=9/14
C05_STATUS=held
C05_KNOWLEDGE_COLUMN=knowledge/round-70-apk-axml-byte-evidence.md
C05_SINGLE_V5=yes
V5_ENTRY_PRESENT=yes
V5_ADMITTED_MARKED=yes
C1_GATE=checked_blocks=17 problems=0 exit=0 ok=yes
C1_LINT=LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0 exit=0
HOLDS_C1_V5=yes
...
EXIT=0
```

Why it reaches: `reports/round-70/measure.py:162` tests `(blocks or 0) >= 17`, a **count of `$ cmd` blocks**,
not of facts or distinct commands — 17 identical `print('ok')` blocks satisfy it. `corpus/lint_entry.py:87`
(`lint_header`) only requires the four *keys* to appear in the first 40 lines; the value `none` is never
resolved against `corpus/SOURCES.md`, and `lint_q15` (`lint_entry.py:80`) only resolves backticked hex tokens,
so a source-free entry lints clean. The author's pre-declared "known limit" (claims.md, C1 do-nothing
controls: "a v4 clone with a padded 15-row §Q-map") is therefore **not the cheapest** move: this control
carries no AXML byte, no fixture reference and no source row at all, and is strictly cheaper than cloning v4.

Impacted axis: C1 coverage. The non-mechanical wave-2 Q decisions are the only thing standing between this
entry and admission; Q01/Q11 would fail it, but a counter-only reading of C1 is green, which is exactly the
state claims.md says must not exist ("a counter-only pass is **not** admission").

Smallest safe correction (pick one, cheapest first):
1. In `measure.py:162`, require the 17 checked blocks to be **distinct commands** (`len({cmd}) >= 17`) and
   require at least 17 of them to invoke the entry's own readout/derivation scripts
   (`corpus/fixtures/apk-r65/readout.py`, `corpus/derive_axml_anchors*.py`) — both are one-line changes.
2. In `lint_entry.py:87`, resolve the `source:` line's `S0xx` tokens against `corpus/SOURCES.md` (the Q02
   class the claim already claims to enforce) so `source: none` is a lint finding.

## Control J — C2: fixture-shaped checker only, no self-assessment repair

Builder: `control_j()`; tree `/tmp/revenger-r70-R70W1ControlAudit/J`; checker = 27 lines
(`/tmp/revenger-r70-R70W1ControlAudit/J_fixture_shaped.py`), README/SHONEN/SCORECARD left at base bytes.

Counter output (actual):

```
SM1=0
SM2=0
SM3=0
SM4=0
SM5=0
SM6=0
SELF_MISMATCH=0 exit=0
SELF_CLEAN_FIXTURE=0
SELF_MUTANTS_KILLED=6/6
SHONEN_BOX_COUNT=4
README_ROWS=14
HOLDS_C2_V5=yes
```

Counterfactual on the **same unrepaired bytes** with the lane's own checker
(`git show aa1842f:corpus/self_assessment_check.py` copied in place, counter re-run):

```
SM1=1
SM2=5
SM3=2
SM4=1
SM5=1
SM6=0
SELF_MISMATCH=10 exit=1
SELF_CLEAN_FIXTURE=0
SELF_MUTANTS_KILLED=6/6
HOLDS_C2_V5=no
```

So the tree J ships is stale by 10 mismatches; J's `0` is a **false clean**, and the only difference between
`yes` and `no` is which checker file the tree carries. The detectors that reach 6/6 are literal matches on the
counter's own fixture values: `"Q01–Q01" in readme`, `corpus/unnamed.py` exists, quoted size `< 1000`,
`len(shonen) < 500` + the r64 seat name, `` `deadbee0123` ``, `"8/14 → 9/14"`. Every one of those literals is
readable at `reports/round-70/measure.py:72-94` (`build_self_fixture`) in the frozen counter, and the fixture
is **static across runs** (`self_check`, `measure.py:99-128`, never randomizes a value).

This makes control E ("an always-0 checker reads SELF_MUTANTS_KILLED=0/6 → no", claims.md C2) the wrong
cheapest control: E is defeated, E′ = E + six fixture literals is not. The `SELF_MISMATCH` conjunct is
self-referential — `measure.py:178-186` runs the tree's own tool on the tree it grades — so a tool that
reports nothing costs nothing to write.

Impacted axis: C2 calibration. `SELF_MISMATCH=0` currently carries no information about the bytes it is
computed on.

Smallest safe correction:
1. **Base-tree attribution leg** (strongest, ~8 lines): run the tree's tool against `git archive
   <BASE_COMMIT>` and require the exact before-vector `SM1=1 SM2=4 SM3=2 SM4=1 SM5=1 SM6=0` /
   `SELF_MISMATCH=9`. A checker that cannot reproduce the documented before-count has not been shown able to
   fail on real bytes. This is the same "shown able to fail" standard C2 claims in its own title.
2. **De-literalize the mutant fixture** (~4 lines): draw each defect value from `secrets.token_hex` (commit
   hex, file name, byte size ≥ 4096 so the `<1000` shape dies, SHONEN length ≥ 500) and add one second
   variant per class. A literal-matching detector then scores 0/6 while a real detector still scores 6/6.

## Control K — C3: pin → echo stub printing the entry's own 17 lines

Builder: `control_k()`; tree `/tmp/revenger-r70-R70W1ControlAudit/K`. The stub
`corpus/echo_r68.py` (19 lines) prints the 17 lines **extracted from the r68 entry's own block**, and
`pins.json` is:

```
{
  "round-68-apk-axml-byte-evidence.md": {
    "corpus/derive_axml_anchors.py": {
      "use": "corpus/echo_r68.py",
      "sha256": "1db07373e409aa4ca7bd2110a807c2e200843a759ba1a79235003ebe666e6cb1"
    }
  }
}
```

`corpus/derive_axml_anchors_r68.py` (sha256 `bce497d6…`, the S046 digest) is copied in but **never executed**:
`grep -c derive_axml_anchors_r68 corpus/check_embedded_outputs.py` → `0`.

Counter output (actual):

```
EMB_R65=checked_blocks=15 problems=1 exit=1
EMB_R67=checked_blocks=16 problems=0 exit=0
EMB_R68=checked_blocks=17 problems=0 exit=0
EMB_R69=checked_blocks=17 problems=0 exit=0
EMB_PINNED_SCRIPT_IS_S046=yes
EMB_R68_BYTES_UNCHANGED=yes
EMB_R65_BYTES_UNCHANGED=yes
EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1
HOLDS_C3_V1=yes
```

Attribution control K′ (same tree, `embedded_output_pins.json` emptied): `EMB_R68=… problems=7`,
`EMB_PIN_MUTANT_KILLED_ATTRIBUTED=0/1`, `HOLDS_C3_V1=no` — so the pin *is* load-bearing, but load-bearing
for an echo, not for a derivation.

Why it reaches: `corpus/check_embedded_outputs.py:98-114` (`apply_pin`) verifies only
`sha256(target) == pin["sha256"]` — the digest the pin file itself asserts — and never binds `pin["use"]` to
the S046 row. The counter's separate conjunct `measure.py:220-221` (`pinned_ok`) hashes the *fixed* path
`corpus/derive_axml_anchors_r68.py`, a different file from the one the gate executes. Two authorities for one
claim: the digest conjunct and the derivation conjunct do not talk about the same bytes. `drift` is a
subset test (`check_embedded_outputs.py:116-118`), so a script that prints exactly the entry's recorded lines
is a perfect forger — `problems=0` proves only that the entry agrees with *something*, not that it agrees
with the historical script.

Impacted axis: C3 freshness / provenance. `EMB_PINNED_SCRIPT_IS_S046=yes` is true and irrelevant;
`EMB_R68 problems=0` is true and forged.

Smallest safe correction (one line in the counter, one in the gate):
1. `measure.py:220-221`: read `corpus/embedded_output_pins.json`, take the r68 entry's single pin's `use`
   path, and require `sha(use_target) == S046_SCRIPT_SHA`. K then reads `EMB_PINNED_SCRIPT_IS_S046=no`.
2. `check_embedded_outputs.py:98-114`: after the digest check, require the pin's `sha256` to appear in the
   cited source row (`S046`) of `corpus/SOURCES.md`, so a pin cannot be self-certified by the file it names.

## Duplicate-authority note (C1 vs C3 tool overlap)

Control C and D in `reports/round-70/controls/` already read `HOLDS_C3_V1=yes` on trees that change nothing
about C3 (`C-stub-entry-flip.log`, `D-v4-clone-flip.log`), because `overlay_tools()` copies the whole treated
tool set. That is consistent with C3's change *being* the tools, but it means the eight committed receipts do
not isolate C3 from a C1 tree; the wave-2 separability seats will need the C3-only tree to carry the pin file
and the r68 script and nothing else, otherwise "C3 yes" is a property of any tree that copies `corpus/`.

## What holds

- Control A (base) reproduces exactly: `K_HELD_BACKED=8/14`, `HOLDS_C1_V5=no`, `HOLDS_C2_V5=no`,
  `HOLDS_C3_V1=no`, `EXIT=0` — the do-nothing baseline is intact.
- Control E is defeated as claimed (`SELF_MUTANTS_KILLED=0/6`), but it is not the cheapest gaming control.
- `GATE_SELFTEST=exit 0`, `HOLD_REPLAY=10/10`, `FRESH_ROWS=18/18`, `F_COVERAGE=5/8` on every tree above,
  including the forged ones — the holds are indifferent to the three claims, as designed.

## Tooling

No install or upgrade was performed (pacman paused host-wide; no `uv`/binary install needed). Python 3 stdlib
only. Scratch: `/tmp/revenger-r70-R70W1ControlAudit/` (builder `build.py`, trees `I`, `J`, `J_fixture_shaped.py`,
`K`, `Kpinless`), deleted after this report was written.
