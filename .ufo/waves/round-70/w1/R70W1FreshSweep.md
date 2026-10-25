PASS — every knowledge entry whose `$` blocks the gate can evaluate is green except r65 (explained M39); the r70 v5 candidate's 22 blocks all re-derive live and are mutation-killed. One pre-existing coverage gap flagged: 3 README-**held** entries carry 76 `$` blocks the gate can never evaluate (exit 2), and the exit-2 text misattributes the cause.

# R70W1FreshSweep — embedded-output gate sweep over every knowledge entry

Seat: leaf executor, round-70 wave 1 (pre-gate). Target bytes: lane commit `aa1842fac199aa524930e5565ed3715de5f84c6d`
(`git -C …/revenger-shokunin rev-parse --short HEAD` → `aa1842f`). No lane file was edited, no git write ran anywhere,
no package was installed (python3 3.14.8, stdlib only).

Scratch roots (all deleted before return):
`/tmp/revenger-r70-freshsweep` (candidate `git archive aa1842fa… | tar -x`), `…/base` (same for `3f5edbc2…`, `corpus/` only),
`…-mut` and `…-pinmut` (throwaway `cp -r` copies for the mutation and pin-tamper tests), `…-probe` (throwaway).

Command used for every row, run with cwd = the archive root:

```
python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/<file>
```

## Table — every `corpus/knowledge/*.md` at aa1842fa (17 files)

| entry | checked_blocks | problems | exit | pinned? |
|---|---|---|---|---|
| 2026-10-12-rea-readiness-checklist.md | — | — | 2 (0 `$` blocks, verified) | no |
| commonjs-destructured-require-edges.md | — | — | 2 (0 `$` blocks) | no |
| digest-scope-versus-provenance.md | — | — | 2 (0 `$` blocks) | no |
| evm-saved-interface-candidates.md | — | — | 2 (0 `$` blocks) | no |
| pe-resource-directory-layout.md | — | — | 2 (0 `$` blocks) | no |
| round-62-commonjs-require-name-evidence.md | — | — | **2 (11 `$` blocks present — see gap G1)** | no |
| round-62-evm-dispatch-byte-evidence.md | — | — | 2 (0 `$` blocks) | no |
| round-63-zip-central-directory-evidence.md | — | — | **2 (41 `$` blocks present — G1)** | no |
| round-64-firmware-region-byte-evidence.md | — | — | **2 (24 `$` blocks present — G1)** | no |
| round-65-apk-axml-byte-evidence.md | 15 | **1** | **1** | no |
| round-67-apk-axml-byte-evidence.md | 16 | 0 | 0 | no |
| round-68-apk-axml-byte-evidence.md | 17 | 0 | 0 | **yes** |
| round-69-apk-axml-byte-evidence.md | 17 | 0 | 0 | no |
| round-70-apk-axml-byte-evidence.md (the v5 candidate) | **22** | **0** | **0** | no |
| seed.md | — | — | 2 (0 `$` blocks) | no |
| tool-validation-by-function-and-version.md | — | — | 2 (0 `$` blocks) | no |
| utf16-unpaired-surrogates-in-resource-names.md | — | — | 2 (0 `$` blocks) | no |

`checked_blocks` equals the number of fenced `$ ` lines in each evaluable entry (15/16/17/17/22), i.e. **no block is
silently skipped**: independent count via `check_embedded_outputs.parse_blocks` + a raw `^\$ ` grep agree on all five
apk entries, and 0 of the 22 r70 blocks have an empty embedded-output list (a block with no quoted output would count
as "checked" while verifying nothing).

## Pin file — which entries it names

`corpus/embedded_output_pins.json` names exactly **one** entry:

```
{"round-68-apk-axml-byte-evidence.md": {"corpus/derive_axml_anchors.py":
  {"use": "corpus/derive_axml_anchors_r68.py",
   "sha256": "bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249"}}}
```

Pin target digest verified against the shipped file:

```
$ sha256sum corpus/derive_axml_anchors_r68.py corpus/derive_axml_anchors.py
bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249  corpus/derive_axml_anchors_r68.py
74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa  corpus/derive_axml_anchors.py
```

`bce497d6…` is the digest the claims' C3 names for the S046 row (`claims.md` §C3, `S046_SCRIPT_SHA` in
`reports/round-70/measure.py`) → `EMB_PINNED_SCRIPT_IS_S046=yes` holds from bytes. r68 is the only entry that names
`corpus/derive_axml_anchors.py` (1 block, `round-68-apk-axml-byte-evidence.md` `$` line), so the pin has exactly the
intended single hit. The r70 candidate also names `corpus/derive_axml_anchors.py` (1 block, entry line 122) and is
correctly **unpinned** — it is a new entry that must re-derive against the current script, and its own item-14 digest
row prints the current script's real digest (`corpus/knowledge/round-70-apk-axml-byte-evidence.md:217`:
`74d4c0d9… 4979 bytes corpus/derive_axml_anchors.py`, equal to the `sha256sum` above).

## r65's one red is the explained M39 drift, not a new one

```
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-65-apk-axml-byte-evidence.md
drift entry:41 embedded output line not in recheck stdout: {"cd_index": 2, … "payload_first16_hex": "4d616e696673742d56657273696f6e", …}
checked_blocks=15 problems=1          # rc=1
```

`4d616e696673742d…` is the 15-byte mis-transcription of `Manifest-Version`; the repaired value is
`4d616e69666573742d56657273696f6e` (16 bytes). Provenance is already recorded in this lane:
`.ufo/waves/round-67/R67RevengerLedger.md:41` ("retained r65 candidate still carries drifted `4d616e696673742d` at its
:41 with `admission-status: rejected`") and `.ufo/waves/round-67/R67MutC7Surface.md:148` ("the r65 red is exactly the
committed M39 surface (`entry:41`, 15-byte `4d616e696673742d…`)"). The r65 entry is `admission-status: rejected`
(line 7) and named by no README row as backing. **Explained — not a finding.**

No other entry shows drift. **No unexplained drift exists at aa1842fa.**

## G1 (flag) — three README-**held** entries are unevaluable, and the exit-2 text says the wrong thing

`corpus/README.md` names these three as the knowledge column of **held** rows:

- `:33` `| C04 | … | knowledge/round-62-commonjs-require-name-evidence.md … | held |`
- `:35` `| C06 | … | knowledge/round-63-zip-central-directory-evidence.md … | held |`
- `:36` `| C07 | … | knowledge/round-64-firmware-region-byte-evidence.md … | held |`

All three exit 2 — but not because they lack blocks:

```
round-62-… blocks=11  argv0={'sha256sum':1,'wc':1,'cp':1,'printf':1,'mv':1,'python3':2,'grep':3, '<shlex error>':1}
round-63-… blocks=41  argv0={'python3':19,'git':4,'sha256sum':4,'wc':3,'tr':1,'printf':10}
round-64-… blocks=24  argv0={'python3':10,'git':6,'sha256sum':4,'cp':1,'cd':1,'wc':1,'<shlex error>':1}
```

Mechanism, located: `corpus/check_embedded_outputs.py:79` (`if argv[0] not in ("python3","python",sys.executable): return
None,"",2`) → `:134-135` (`if proc is None: return None, None`, which **discards problems already collected**) → `:208`
prints `could-not-evaluate: no `$ cmd` blocks, unsupported command, or read failure`. The first non-python block aborts
the whole entry, so the 2/19/10 `python3` blocks in those three entries are **never run** — 31 of the 76 blocks. The
printed reason names "no `$ cmd` blocks", which is false for all three; anyone logging only the message records "no
blocks" for entries that carry 76.

Two of the three also embed commands that cannot execute as printed: 17 `<repo-root>` placeholder blocks in r63 (e.g.
`round-63-zip-central-directory-evidence.md:23` `$ python3 -B readout.py <repo-root> --fact 'archive'`) and 8 in r64
(`:24`, `:85`, `:94`, `:101`, …). One block in each of r62/r64 is not even shlex-parseable
(`round-62-…:95` `printf '%s`, `round-64-…:147` `python3 -c 'import json`) — so a future pin-style repair cannot
simply enable shell blocks; those entries need their `$` lines rewritten to the lane-root form the apk entries use.

**Attribution — pre-existing, not caused by aa1842fa.** The same three exit 2 identically at the claim base:

```
$ cd <base 3f5edbc2 archive>; python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-6{2,3,4}…
round-62-commonjs-require-name-evidence rc=2 :: could-not-evaluate: …
round-63-zip-central-directory-evidence rc=2 :: could-not-evaluate: …
round-64-firmware-region-byte-evidence rc=2 :: could-not-evaluate: …
```

The candidate's gate diff against base is pin-only (adds `hashlib`, `PIN_MARKER`, `PINS_REL`, `load_pins`, `apply_pin`,
one call site in `evaluate`, three self-test assertions) — no change to `run_cmd` or the exit-2 path
(`diff -u base/corpus/check_embedded_outputs.py corpus/check_embedded_outputs.py`). So G1 is an inherited limit, and it
is **not** a C1/C2/C3 predicate input: the C3 predicate names r68/r65/r67/r69 only, and the C1 gate reads the r70 entry
only. It is advisory for the freshness axis, not a kill.

## Positive evidence for the candidate's freshness (mutation test, on a copy)

The r70 entry's `problems=0` is a live measurement, not a vacuous pass. One extra token appended to the first embedded
output line of a `cp -r` copy of the archive root:

```
mutating first output line, entry line 27: '{"bytes": 947, "fact": "archive", … "sha256": "05d2280f…"}\n'
mutated rc= 1
drift entry:27 embedded output line not in recheck stdout: {… "sha256": "05d2280f…"}MUTATED
checked_blocks=22 problems=1
```

Same method kills the pin: flipping the first byte of `corpus/derive_axml_anchors_r68.py` in a throwaway copy yields

```
drift entry:128 pinned historical script digest mismatch: corpus/derive_axml_anchors_r68.py
checked_blocks=16 problems=1          # rc=1
```

→ `EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1` and the marker is the attributed text the claims require.

## C3 conjuncts I re-derived from bytes (side observation, not my claim to score)

| conjunct | my command's output | holds |
|---|---|---|
| `EMB_R68 checked_blocks=17 problems=0` | `checked_blocks=17 problems=0` (rc=0) | yes |
| before: base r68 = 7 problems | base archive: `checked_blocks=17 problems=7`, rc=1, drifting lines `entry:137-143` (`enum RES_STRING_POOL_TYPE : 239` …) | yes, matches `claims.md` §C3 Before |
| `EMB_R65 problems=1` | `checked_blocks=15 problems=1` (M39, above) | yes |
| `EMB_R67 problems=0` / `EMB_R69 problems=0` | `16/0` / `17/0` | yes |
| `GATE_SELFTEST` exit 0 | `SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired, pinned script verified by digest` rc=0 | yes |
| pin target digest = S046 | `bce497d6…` | yes |

The base also **lacks** both `corpus/embedded_output_pins.json` and `corpus/derive_axml_anchors_r68.py` (`ls` → "No such
file or directory"), so the C3 surface is genuinely new at aa1842fa rather than a re-labelled pre-existing file.

## Risks / advisories for wave 2 (no action taken by me)

1. **G1 is the freshness axis's open wound.** 3 of 14 README rows are `held` on entries the gate cannot evaluate; 31
   python3 blocks in them have never been compared to their quoted stdout. If any wave-2 seat or the L1 wants the
   freshness story to cover `held` (not just `retained candidates`), the repair is per-entry `$`-line normalisation to
   the lane-root form (as r67-r70 already use), not a gate widening — widening `run_cmd` to shell would import
   `cp`/`mv`/`cd` side effects into a read-only gate.
2. **Forward drift risk on r70, identical in shape to the r68 wound.** The r70 entry re-derives against the mutable
   `corpus/derive_axml_anchors.py` and is unpinned. The next in-place extension of that script will make r70 read
   `problems>0`. That is the gate working (it will be *seen*, unlike r68's silent drift), but if r70 lands as the C05
   backing, a pin row for it should be added at that same in-place-extension revision — otherwise the C05 held row goes
   red on a future round's script edit, not on a defect in the entry.
3. The exit-2 message (`:208`) should distinguish "no blocks" from "unsupported command"; as written it will keep
   reporting "no `$ cmd` blocks" for entries that carry dozens. Cheap, one-line, but it is the gate's bytes and the
   gate is frozen for this wave — recorded, not edited.

## Tooling

No installs or upgrades. python3 3.14.8 (system), `git` read-only (`show`, `archive`, `rev-parse`), `sha256sum`, `diff`,
`cp`/`rm` in `/tmp` scratch only. All four scratch roots (`/tmp/revenger-r70-freshsweep{,-mut,-pinmut,-probe}`) removed
before this report was written.
