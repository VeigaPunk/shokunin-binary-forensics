# R71W1PinRegression — pin/confinement/verbatim regression probe (wave 1, advisory)

**VERDICT: NO REGRESSION.** The patched gate (`corpus/check_embedded_outputs.py`, sha256 `05afff8b9f4a47d6705b6de17b7b4e38f28927ac7139dfb2748420a31cf938f8`) reproduces every round-70/71 retained-entry `EMB_*` label byte-for-byte, and all four pin legs (script digest, `use`-path escape ×2, entry-text digest naming), command confinement, and the verbatim comparison held under tamper. Zero surviving mutants; two inconclusive-by-design items noted (120s CLI timeout wall-clock not exercised; M3 first probe collided with a real entry anchor — resolved, see M3).

Environment: Python 3.14.8. All runs in scratch `/fast/scratch/hyaku/revenger-r71/R71W1PinRegression/` (byte-identical `cp -a` of lane `corpus/`, proven by `diff -r` → `SCRATCH_PRISTINE_MATCH` before any probe). The lane tree was never written; every tamper was applied to scratch copies only. No installs; no pacman transactions.

## 1. Baseline: r65/r67/r68/r69 through the patched gate (cwd = scratch root)

Command: `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-NN-apk-axml-byte-evidence.md`

| label | round-70 `measure-after.log` / round-71 `measure-before.log` | patched-gate scratch run | match |
|---|---|---|---|
| EMB_R65 | checked_blocks=15 problems=1 exit=1 | checked_blocks=15 problems=1 exit=1 | YES |
| EMB_R67 | checked_blocks=16 problems=0 exit=0 | checked_blocks=16 problems=0 exit=0 | YES |
| EMB_R68 | checked_blocks=17 problems=0 exit=0 | checked_blocks=17 problems=0 exit=0 | YES |
| EMB_R69 | checked_blocks=17 problems=0 exit=0 | checked_blocks=17 problems=0 exit=0 | YES |

R65's single retained problem is the known round-65 transcription drift, still caught verbatim:
`drift entry:41 embedded output line not in recheck stdout: {"cd_index": 2, ... "payload_first16_hex": "4d616e696673742d56657273696f6e" ...}` (entry says `…4d616e69 6673…`; real stdout prints `…4d616e69 6653…`, cf. r67 entry line 42 which has the corrected hex). Exit contract unchanged.

`--self-test` → `exit=0`, `SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired, pin and confinement checks passed, missing-entry and timeout legs passed`.
Missing-entry CLI → `could-not-evaluate: entry not found: corpus/knowledge/no-such-entry.md`, `exit=2`, no traceback (C2 declared mapping present).

Pin wiring on the baseline: pins sha256 `34c400c4721408a1ae485e8d6895ebb93e2744cdeeeefa0954c3c3176c0e4efd`; pinned target `corpus/derive_axml_anchors_r68.py` sha256 `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249` (= pins.json value; = digest named by the r68 entry itself, entry line 4) — `EMB_PINNED_SCRIPT_IS_S046=yes` equivalent intact; R68 clean run proves the digest-verified substitution path still executes 17 checked blocks.

## 2. Mutants (scratch copies only; all reruns of the r68 entry)

- **M1 — tamper pinned r68 script** (inserted `print("tampered-r71-pin-probe")` into `corpus/derive_axml_anchors_r68.py`): `drift entry:128 pinned historical script digest mismatch: corpus/derive_axml_anchors_r68.py` / `checked_blocks=16 problems=1` / `exit=1`. **killed** — digest verified *before* substitution; the tampered script never executed; block not counted as checked; kill attributed to `PIN_MARKER`.
- **M2 — pin path relative escape** (`"use": "../outside-r68.py"`): `drift entry:128 pinned historical script digest mismatch: ../outside-r68.py (path escapes the tree)` / `exit=1`. **killed**.
- **M2b — pin path absolute escape** (`"use": "/etc/hostname"`): `… /etc/hostname (path escapes the tree)` / `exit=1`. **killed**.
- **M3 — pin to a script whose digest the entry names** (`use: corpus/pin-alt.py`, a readout.py copy, sha `92e347c3…`): pin was substituted and the substituted command ran (`drift entry:128 command exited 1: python3 -B corpus/pin-alt.py`, `exit=1`). **killed, and initially looked like a naming-leg miss — it is not**: the r68 entry text genuinely names `92e347c3…` as its readout.py anchor (entry lines 5, 17, 194), so substitution was authorized under the frozen digest-in-text rule. The kill came from the substituted command's own exit 1. Documents that the naming check binds the digest, not the script name.
- **M3b — pin to a truly unnamed digest** (`use: corpus/pin-alt3.py`, sha `f79fab0781269ec0078001756a1947c5a9bd6e95e896922a04522227ab86b096`, absent from entry text): `drift entry:128 pinned historical script digest mismatch: corpus/pin-alt3.py (entry text does not name the pinned digest)` / `exit=1`. **killed** — entry-text naming leg fires.
- **M4 — confinement, `python3 -B -c print(1)`** (probe entry): `could-not-evaluate: no \`$ cmd\` blocks or unsupported command` / `exit=2`, nothing evaluated. **killed** (refused via the patched could-not-evaluate path).
- **M4b — confinement, symlink `corpus/link.py` → `/etc/hostname`**: `could-not-evaluate: no \`$ cmd\` blocks or unsupported command` / `exit=2`. **killed**.
- **M5 — verbatim comparison** (probe entry, real stdout line with `947`→`948`): `drift entry:3 embedded output line not in recheck stdout: {"bytes": 948, …}` / `exit=1`. **killed** — verbatim line unchanged on the patched gate.

## 3. Inconclusive-by-design / not exercised

- The **CLI leg at the declared production 120s timeout** was not exercised wall-clock (would spend 120s of the 12-minute box; and is the C2 falsify seats' registered leg). The timeout mapping is proven here only via `--self-test` (1s injected leg, exit 0) — same `run_cmd` → `TimeoutExpired` → `CannotEvaluate` path.
- M3 as first built is **inconclusive as a naming-leg test** (authorized substitution); superseded by M3b which is the valid probe.

## 4. Restoration evidence

- After the M1 restore and again after the M3b restore, the pristine r68 run returned `checked_blocks=17 problems=0` / `exit=0` (recovery receipt).
- Final scratch hashes after all restores: `embedded_output_pins.json` → `34c400c4…` (= lane), `derive_axml_anchors_r68.py` → `bce497d6…` (= lane).
- Final `diff -r lane-corpus scratch-corpus` residue: `Only in corpus: link.py`, `Only in corpus: pin-alt.py` (probe-added files; `pin-alt3.py` added after that diff) — no lane file differs. Lane `check_embedded_outputs.py` sha256 unchanged at `05afff8b…`.
- Scratch root deleted before return: `rm -rf /fast/scratch/hyaku/revenger-r71/R71W1PinRegression`.

## 5. Scope notes

Leaf seat; no edits to lane source; no campaign tools; no subagents; no installs (nothing needed); pacman untouched per host-wide pause. Findings above cite actual command output captured this round.
