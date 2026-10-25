# R68CriticC7Claim — C1 predicate attack (calibration axis)

FALSIFIED — the frozen C1 predicate reads at target on **every** label while the gate performs **no verbatim comparison at all** (`C7_MUTANT_KILLED_ATTRIBUTED=1/1`, `HOLDS_OK_V5=yes`, `HOLDS_OK_V6=yes`, counter exit 0), and a second path passes every label with a one-operator weakening of `drift()` that behaviourally accepts appended drift text the landed gate rejects.

Scope note (matters for the verdict's meaning): the **landed** gate at `corpus/check_embedded_outputs.py` is a genuine repair — `drift()` is load-bearing at `:105`, the marker is emitted only from the failed-`caught` branch at `:140-144`, there is no self-integrity check, and it behaviourally rejects appended text (probe below). The defect is in the **predicate/instrument**: nothing in `measure.py` can distinguish that repair from a fake. That is precisely a calibration defect, so the verdict is FALSIFIED on the claim as stated ("the attribution rule must reject any other message"), not on the artifact.

## Instrument pins (verified, not trusted)

```
$ sha256sum reports/round-68/measure.py
0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766  reports/round-68/measure.py
```
matches `reports/round-68/claims.md:7` and `reports/round-68/measure-before.log:102` — the counter is the pinned, unedited instrument.

```
$ sha256sum corpus/check_embedded_outputs.py
b89183bec2fd3b94f5b0acc828a0d3fe16f6a98dde1d7752616da85d08a8e0ca  corpus/check_embedded_outputs.py
```

## How the labels are computed (the attack surface)

| label | code | what it actually measures |
|---|---|---|
| `C7_SELFTEST` | `measure.py:405-407` | exit code of `--self-test` |
| `C7_CONTROL_PASS` | `measure.py:408` | selftest exit 0 **and** the 30-byte marker string occurs anywhere in the gate file |
| `C7_MUTANT_KILLED_ATTRIBUTED` | `measure.py:385-392,421-428` | exit != 0 **and** `last.endswith(marker)`, where "mutant" is a **textual** regex substitution of one source line (`problems += drift(lines, stdout_set, lineno)` → `problems += []`) |
| `C7_NEG_SPOOF_KILLED(_ATTRIBUTED)` | `measure.py:460-492` | same, with the marker *literal* text edited |
| `C7_RED_ON_R65_CANDIDATE` | `measure.py:429-431` | exit != 0 of `--entry corpus/knowledge/round-65-apk-axml-byte-evidence.md` |
| `C7_V2_CLEAN` / `C7_V3_CLEAN` | `measure.py:432-446` | exit 0 of `--entry` on the r67 / r68 entry |
| `HOLDS_OK_V5/V6` | `measure.py:521-526` | the conjunction; no independent behavioural leg |

Consequence: the kill is established by **file bytes changing**, and clean-ness by **exit 0 on a named path**. Neither leg constrains *how* the gate decides. `C7_CONTROL_PASS` is a grep of the file text (`measure.py:408`), so even a marker in a comment satisfies its marker half.

## Attack matrix

All four gate variants were run through the **frozen** counter with the claims.md invocation, `TMPDIR` isolated, on a copy of the lane corpus (5.6 MB, `cp -a corpus <tree>/corpus`; only `corpus/check_embedded_outputs.py` differs per tree).

| # | attempt | counter output (C1 conjuncts) | predicate |
|---|---|---|---|
| A1 | **weakened comparison** inside an otherwise genuine gate: `drift()` accepts a line if some stdout line is a substring of it (`... if l not in stdout_set and not any(s in l for s in stdout_set)`) | `C7_SELFTEST=pass`, `C7_CONTROL_PASS=1/1`, `C7_MUTANT_KILLED=1/1`, `C7_MUTANT_KILLED_ATTRIBUTED=1/1`, `C7_NEG_SPOOF_KILLED=1/1`, `C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1`, `C7_RED_ON_R65_CANDIDATE=yes`, `C7_V2_CLEAN=yes`, `C7_V3_CLEAN=yes`, `HOLDS_OK_V5=yes`, `HOLDS_OK_V6=yes`, exit 0 | **PASSES** |
| A2 | **no comparison at all**: `--self-test` verifies the file's own sha256 (zeros-normalized on the digest line) and prints `MARKER` + exit 1 on mismatch; `--entry` exits 1 iff `"round-65"` is in the path, else 0; the mutant regex line kept once in an uncalled function | identical label block, incl. `HOLDS_OK_V5=yes` `HOLDS_OK_V6=yes`, exit 0 | **PASSES** |
| A3 | weaker superset: `drift()` accepts a line if it is a substring of a stdout line *or* contains one (`l in s or s in l`) | all labels green, `HOLDS_OK_V5/V6=yes`, exit 0 | **PASSES** |
| A4 | cosmetic marker print on **every** run (incl. the passing control): base f165908 gate + `print(MARKER)` as the first statement of `_self_test` | `C7_SELFTEST=pass`, `C7_CONTROL_PASS=1/1`, but `C7_MUTANT_KILLED_ATTRIBUTED=0/1`, `HOLDS_OK_V5=no`, `HOLDS_OK_V6=no` | blocked |
| A5 | unconditional `print(MARKER); sys.exit(1)` on `--self-test` | `C7_SELFTEST=fail`, `C7_CONTROL_PASS=0/1`, `HOLDS_OK_V5=no` | blocked |
| A6 | edit the counter instead of the gate | sha256 would differ from `claims.md:7` / `measure-before.log:102`; current file matches both | blocked (by external comparison only — `measure.py` does not self-verify its own pin) |

A1/A2/A3 raw output: `/tmp/r68critic-c1/tree-weak2.log:68-98`, `/tmp/r68critic-c1/fake-counter.log:68-98`, `/tmp/r68critic-c1/tree-weak.log:68-98`; baseline (landed gate) `/tmp/r68critic-c1/tree-base.log:68-74,97-98`. Reproduce with:

```sh
cd / && TMPDIR=/tmp/<iso> python3 -B \
  /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-68/measure.py <tree>
```

### A1 is not merely cosmetic — behavioural divergence, landed vs weakened

Probe dir `/tmp/r68critic-c1/probe`: `reader.py` prints `{"fact": "a", "v": 1}`; three entries, each a `$ python3 -B reader.py --fact a` block quoting respectively the true line, the true line **plus appended text** (`<<M39 appended drift text>>`), and an altered value.

```
LANDED/entry_verbatim  exit=0 :: checked_blocks=1 problems=0
LANDED/entry_appended  exit=1 :: checked_blocks=1 problems=1
LANDED/entry_altered   exit=1 :: checked_blocks=1 problems=1
WEAK2/entry_verbatim   exit=0 :: checked_blocks=1 problems=0
WEAK2/entry_appended   exit=0 :: checked_blocks=1 problems=0     <-- drift accepted
WEAK2/entry_altered    exit=1 :: checked_blocks=1 problems=1
```

One changed boolean in `drift()` (`corpus/check_embedded_outputs.py:83-86`) turns an entry whose quoted output is *wrong* into `problems=0`, and every C1 conjunct still reads at target. R65 stays red only because its drift line (`entry:41`, the long JSON member line) is textually unlike any stdout line — an accident of that fixture, not a property the predicate enforces.

### Why A2 is decisive on the attribution wording

The claim says the attribution rule must reject "any other message". `measure.py:428` checks only `rc != 0 and last.endswith(marker)`. A1/A2 show the kill may be caused by **anything that responds to file bytes** — a self-integrity hash in A2 kills both the textual mutant and the mode-f. `MARKER = "…"` spoof identically, and the spoof still reads `0/1` because the *printed* constant is spoofed. Every conjunct is satisfied by construction, with zero drift detection: `C7_V3_CLEAN` (exit 0 for any non-`round-65` path) and `C7_V2_CLEAN` are equally free.

The one genuine structural guard is narrow and worth recording: `caught` at `:140-142` is computed from the same `evaluate()` result, so a weakening that stops catching the **self-test's single synthetic drifted line** fails `C7_SELFTEST`/`CONTROL_PASS` and self-destructs (this is what blocks a tautological comparison, e.g. `drift(lines, {l for l,_ in lines}, …)`). It constrains exactly one 23-byte line differing in one field (`"v": 9` vs `"v": 1`); A1/A3 step around it, and A2 steps around it entirely.

## Impacted axes

- **calibration (C1)** — primary. The predicate is satisfied by A1/A2/A3; it measures "the file changed and the last line matches a string", not "the gate can attribute a drift-detection failure". Claim wording ("must reject any other message") is false of the instrument.
- **coverage (C2), collateral** — `C7_V3_CLEAN=yes` is a conjunct of C2's frozen predicate (`claims.md` C2 clause, `C7_V3_CLEAN`). Under A1/A2 the v3 candidate reads clean with **any** content. C2's admission therefore cannot rest on that label; it needs its own behavioural read of the v3 entry (other seats' Q-map work is the right home for that).
- **provenance / registry truth** — `SKILL.md:268` still states the marker "is structurally shadowed … and can never fire … reorder fix routed", and `:270` says "measured-against round-67 frozen counter". Commit `4232235` (message: "C7 gate attribution repair (reachable marker as the killing line)") does **not** touch `SKILL.md` (`git show --stat 4232235` — 6 files, no SKILL.md). The registered gate row contradicts the landed gate, which prints the marker at `corpus/check_embedded_outputs.py:144`. The registry is the lane's provenance surface; it is currently false at the tip.
- not impacted: `HOLD_REPLAY`/`HOLD_CALIBRATION`/`FRESH_ROWS` denominators (the gate stays outside `verify_*.py`); fixture/live bytes (all work done on copies).

## Smallest safe correction

1. **This round (no counter edit allowed):** C1 admission must carry one behavioural leg, executed by a seat, not by `measure.py`. In a temp tree: (a) a clean entry → exit 0; (b) an entry quoting a true line **plus appended text** → exit 1 with a `drift entry:` problem; (c) an entry with one field altered → exit 1. The landed gate passes all three (probe above); A1 and A3 fail (b). ~30 lines, no lane write.
2. **Registry:** correct `SKILL.md:268` to the measured truth (marker reachable at `corpus/check_embedded_outputs.py:144`; it is the last line of the failed `--self-test`, `measure.py:428` is the reader) and `:270` to the round-68 counter `0de4eb6f…`. Do not leave the r67 shadowing text in place once the repair is registered.
3. **Next counter (not this frozen one):** move the detection proof out of file-byte mutation. Have the counter generate the drifted entry itself from the entry's own declared command (a randomized wrong value in a correctly-shaped line), require exit 1 naming that line, and keep the textual mutant only for attribution. Byte-mutation probes are unconditionally gameable by any self-integrity check — this is structural, not an accident of this gate.
4. **Claim wording:** restate C1's scope to what the labels measure — "the marker is the last line of the textual-removal kill and not of the spoofed-marker kill" — and drop "the attribution rule must reject any other message"; the instrument rejects other *last lines*, not other kill causes.

## Tooling

No installs or upgrades were run (none needed); pacman guard respected.

Report: .ufo/waves/round-68/R68CriticC7Claim.md
