HOLES — the sha256 pin protects the pinned script's bytes and any path's content (P1, P2a, P2b), but pin presence (P5), pin-key spelling (P4), entry→script assignment (P3a/P3b) and `use`-path provenance (P2c) are protected only by convention; three named holes below, each with a minimal tightening that leaves the registered C7 line byte-identical.

Seat R70W1PinMut · 2026-10-25 · wave 1 (advisory; not kill-rule inputs).
Targets: `corpus/check_embedded_outputs.py` and `corpus/embedded_output_pins.json` at lane commit `aa1842fac199aa524930e5565ed3715de5f84c6d`. All probes ran on scratch copies (`git archive aa1842f | tar -x` → `/tmp/revenger-r70-R70W1PinMut/pristine`, one fresh `cp -a` copy per probe); no lane file was edited. Checker pointer lines below are `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin show aa1842fac199aa524930e5565ed3715de5f84c6d:corpus/check_embedded_outputs.py` line numbers; working-tree checker is byte-identical (sha256 `79cff2fa0ebdfe82ac6f66c5cb7027b29e1c8c2f620efc65a0eea4f1253fb57b`).

## Baseline (pristine)

```
$ cd /tmp/revenger-r70-R70W1PinMut/pristine
$ sha256sum corpus/derive_axml_anchors_r68.py corpus/derive_axml_anchors.py corpus/check_embedded_outputs.py corpus/embedded_output_pins.json
bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249  corpus/derive_axml_anchors_r68.py   (= pin digest, = claims.md C3 S046 row)
74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa  corpus/derive_axml_anchors.py       (current, r69-extended in place)
79cff2fa0ebdfe82ac6f66c5cb7027b29e1c8c2f620efc65a0eea4f1253fb57b  corpus/check_embedded_outputs.py
34c400c4721408a1ae485e8d6895ebb93e2744cdeeeefa0954c3c3176c0e4efd  corpus/embedded_output_pins.json
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md
checked_blocks=17 problems=0        exit=0
$ python3 -B corpus/check_embedded_outputs.py --self-test
SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired, pinned script verified by digest   exit=0
```

Shape of the r68 pin (`corpus/embedded_output_pins.json:2-6`): entry key `round-68-apk-axml-byte-evidence.md` → script-arg key `corpus/derive_axml_anchors.py` → `{"use": "corpus/derive_axml_anchors_r68.py", "sha256": "bce497d6…"}`. The r68 entry invokes the pinned script exactly once (entry line 128: `$ python3 -B corpus/derive_axml_anchors.py`); its other 16 blocks call `corpus/fixtures/apk-r65/readout.py` and are unpinned.

## Probes (each on a fresh copy; gate run as `python3 -B corpus/check_embedded_outputs.py --entry <entry>` from the scratch lane root)

### P1 — one-byte tamper of `corpus/derive_axml_anchors_r68.py` → KILLED, digest-protected
Byte 0 incremented (`bce497d6…` → `2227caa7…`).
```
exit=1  last: checked_blocks=16 problems=1
drift entry:128 pinned historical script digest mismatch: corpus/derive_axml_anchors_r68.py
```
Matches the registered C3 conjunct `EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1`: non-zero exit with the exact attributed text. Two good properties: the tampered bytes are never executed (`apply_pin` returns the problem and `evaluate` `continue`s before `run_cmd`, checker:129-133), and restoration to pristine bytes returns exit 0. The self-test guards this branch in-script (checker:190-195).

### P2 — `use` pointed elsewhere: relative escape, absolute path, out-of-repo symlink
- **P2a `use: "../README.md"`** (relative escape out of corpus/): `exit=1`, `drift entry:128 pinned historical script digest mismatch: ../README.md`. The escape is *attempted* (checker:106 joins `use` onto cwd with no confinement), but README's bytes don't hash to the pin → fail-closed. Content is digest-protected.
- **P2b absolute path `/tmp/revenger-r70-R70W1PinMut/ext-readme-abs.txt`**: `Path(cwd) / "/abs"` discards cwd (pathlib semantics), so the absolute path is honored; mismatch digest → `exit=1`, `pinned historical script digest mismatch: /tmp/…`. Content digest-protected; the checker accepts absolute `use` without complaint.
- **P2c symlink to a same-bytes copy OUTSIDE the lane tree (`/tmp/revenger-r70-R70W1PinMut/ext-alias.py` → scratch `corpus/derive_axml_anchors_r68.py`)**: **`exit=0, checked_blocks=17 problems=0` — pin applied, and the gate executed the "historical script" from `/tmp`, outside the repo.** `target.is_file()` follows symlinks and the digest only binds bytes, so any file anywhere with the pinned bytes passes. No integrity break (content-addressed), but the "historical revision in `corpus/`" property is convention-only.

### P3 — pin added for the r67 entry mapping to the extended script → accepted while VACUOUS, convention-only
The r67 entry never invokes `corpus/derive_axml_anchors.py` at all (all 16 of its blocks call `readout.py`), which makes the mis-assignment visible end to end:
- **P3a** `round-67-apk-axml-byte-evidence.md` → `corpus/derive_axml_anchors.py` → `use: corpus/derive_axml_anchors_r68.py`, true digest `bce497d6…`: **`exit=0, checked_blocks=16 problems=0`.** The pin is silently never applied; nothing reports an unused pin.
- **P3b** same key but self-pinned to the *current extended* script (`use: corpus/derive_axml_anchors.py`, its own current digest `74d4c0d9…` — the exact re-derivation-against-later-revision C3 exists to prevent): **`exit=0, checked_blocks=16 problems=0`.** A self-consistent digest can never flag a wrong assignment. The digest authenticates bytes, not history: which entry maps to which script revision is recorded only by convention in `pins.json`, and an entry that doesn't run the script at all is indistinguishable from a correct pin. (For the r68 entry itself the assignment is separately claim-pinned — `EMB_PINNED_SCRIPT_IS_S046=yes` — but the pins file admits any assignment for any future entry.)

### P4 — script argument respelled `./corpus/derive_axml_anchors.py` in the entry → pin silently bypassed, convention-only
One command line rewritten in the scratch r68 entry (`$ python3 -B ./corpus/derive_axml_anchors.py`, entry line 128), pins untouched.
```
exit=1  last: checked_blocks=17 problems=7
drift entry:137 embedded output line not in recheck stdout: enum RES_STRING_POOL_TYPE : 239
drift entry:138 … enum RES_XML_TYPE : 241
drift entry:139 … enum RES_XML_START_NAMESPACE_TYPE : 245
drift entry:140 … enum RES_XML_END_NAMESPACE_TYPE : 246
… (+3 more drift lines)
```
The pin is looked up by exact string (checker:103 `argv[idx] not in pins`), so `./corpus/…` misses the key `corpus/…` and the gate re-derives against the **current r69-extended script** with zero pin-related output. It fails closed *only by accident* — because the extension changed this script's output. Had the in-place extension been output-neutral for these facts, the gate would stay green with freshness silently lost. Note the output is byte-for-byte the pre-C3 baseline: `checked_blocks=17 problems=7` = the `measure-before.log` value `EMB_R68=checked_blocks=17 problems=7`.

### P5 — delete `corpus/embedded_output_pins.json` → pinning silently disabled, convention-only
```
exit=1  last: checked_blocks=17 problems=7   (identical to P4: generic drift lines, no pins-related message)
```
`load_pins` returns `{}` on a missing pins file (checker:92-94 `if not p.is_file(): return {}`), with no named error, no exit-2 "could-not-evaluate". The freshness rule silently vanishes; the gate stays red only because the current script's output drifted (same accidental fail-closed profile as P4).

## Digest-protected vs convention-only

| Surface | Protection |
|---|---|
| Pinned script bytes tampered (P1) | **digest** — killed with attributed marker |
| `use` pointing at wrong-content file, any path shape (P2a/P2b) | **digest** (content) — killed |
| `use` escaping corpus/, absolute paths, out-of-repo symlinks with pinned bytes (P2c) | **convention only** — accepted green |
| Which entry maps to which script (P3a/P3b), incl. entries that never run the script | **convention only** — accepted green |
| Pin key spelling / pin applied at all (P4) | **convention only** — silent bypass, accidental fail-closed |
| Pins file present at all (P5) | **convention only** — silent `{}`, accidental fail-closed |

## Proposed minimal tightenings (each leaves the registered C7 line `problems += drift(lines, stdout_set, lineno)` at checker:140 byte-identical)

- **H1 (P5), counter-side, zero checker change:** pin `corpus/embedded_output_pins.json` bytes in `reports/round-70/measure.py` exactly like `EMB_R68_BYTES_UNCHANGED` (pristine sha256 `34c400c4…`), conjunct `EMB_PINS_UNCHANGED=yes`. Deletion or edit flips the C3 predicate.
- **H2 (P4 and P3 both), checker-side, one rule:** in `evaluate()`, track which pin keys were consumed; after the block loop, append `drift entry:<lineno> pin declared but never applied: <keys>` for any unconsumed key. Kills the spelling bypass (P4) and the vacuous/wrong assignment (P3) with a single "declared pins must be applied" invariant.
- **H3 (P2c), checker-side, one condition:** in `apply_pin`, require `(Path(cwd) / pin["use"]).resolve().is_relative_to(Path(cwd).resolve())`, else return the pin problem. Rejects `..` escapes and absolute paths; in-repo symlinks stay allowed and the digest still binds content.
- **H4 (optional second step for P3's assignment half):** have the entry bytes state the historical script's digest (the r68 entry already cites the S046 digest `bce497d6…`) and have `apply_pin` cross-check `pin["sha256"]` against the digest named in the entry — wrong assignment becomes fail-closed and self-describing. Larger change; flag for wave-2 discussion, not required to close H1-H3.

## Restoration and hygiene evidence

- P1 scratch bytes restored to pristine before moving on (`restored==pristine: True`; hash back to `bce497d6…`).
- Lane untouched by this seat: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin status --porcelain -- corpus/` shows only sibling wave-1 edits (`M corpus/README.md`, `M corpus/self_assessment_check.py` — neither is a target of my probes); my three attack-target files in the lane hash identically to the pinned commit: `bce497d6…` (derive_axml_anchors_r68.py), `79cff2fa…` (check_embedded_outputs.py), `34c400c4…` (embedded_output_pins.json).
- Scratch removed: `ls -d /tmp/revenger-r70-R70W1PinMut*` → `No such file or directory`.
- No packages installed or upgraded; Python 3 stdlib + git archive only.
