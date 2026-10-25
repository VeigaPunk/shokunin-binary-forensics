FINDINGS — confinement refuses every hostile spelling I could build (no escape, no false clean) and changes no live entry verdict, but its wiring has **zero red-before**, one live block class was downgraded from *checked* to *could-not-evaluate*, the accepted command set depends on which interpreter launches the gate, and the registry/docstring still describe the pre-round-70 command set.

Seat: R70W2GateConfinement · wave 2 (falsify) · target bytes: lane commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd`
Target file sha256 (landed == working tree): `5f42415bd4124cf916ecfd9b745d030254a29d299afbe8061a89b784e0d9e879` `corpus/check_embedded_outputs.py`
All work on `git archive` extraction in `/tmp/revenger-r70-R70W2GateConfinement/` (scratch deleted at end); no lane file written.

## 1. What was asked and what I measured

Question: did the round-70 command confinement (`confined` :75-85 / `inside` :87-95, wired at `corpus/check_embedded_outputs.py:104-105`) break or weaken anything?

Axes measured: (a) live-corpus regression — every declared command in all 17 `corpus/knowledge/*.md`; (b) hostile spellings — symlink out of tree, in-tree symlink, dir-symlink, trailing slash (file and directory), `./corpus/../../x.py`, `corpus/../../x.py`, mixed case, `python3.14`, absolute interpreter, `-c`, `-m`, absolute script path, symlink loops (self and two-node), symlink into an unreadable directory, broken symlink; (c) verdict code for each refusal; (d) red-before — mutation of the predicate and of the wiring against `--self-test` and the frozen counter; (e) determinism — same entry bytes under two launchers.

## 2. Live corpus: no verdict regresses, one block class is downgraded

Block accounting over all 17 entries at the landed commit (`parse_blocks` + the exact two `run_cmd` checks):

```
{'total': 165, 'accepted': 118, 'refused_argv0': 43, 'refused_confinement': 2, 'badsplit': 2}
```

* 118 blocks accepted and executed — **all of them the `python3 -B <relative script> ...` shape**, i.e. the shape the ticket names: not one such block is refused. Every entry built only from that shape still exits 0.
* 43 blocks refused by the **pre-existing** `argv[0]` allow-list (`:102`, unchanged from base `3f5edbc`): `sha256sum`/`wc`/`cp`/`printf`/`mv`/`grep`/`git`/`tr`/`cd`. Same at base — not a round-70 effect.
* **2** blocks refused by the **new** confinement, both in `corpus/knowledge/round-64-firmware-region-byte-evidence.md`:
  * `:74 $ python3 -V`
  * `:76 $ python3 -c 'import zlib; print(zlib.ZLIB_VERSION, zlib.ZLIB_RUNTIME_VERSION)'`

Per-entry verdict, landed vs base (`--entry`, cwd = tree root; format `landed/base`):

```
2/2 2026-10-12-rea-readiness-checklist.md        2/2 round-62-commonjs-require-name-evidence.md
2/2 commonjs-destructured-require-edges.md       2/2 round-62-evm-dispatch-byte-evidence.md
2/2 digest-scope-versus-provenance.md            2/2 round-63-zip-central-directory-evidence.md
2/2 evm-saved-interface-candidates.md            2/2 round-64-firmware-region-byte-evidence.md
2/2 pe-resource-directory-layout.md              1/1 round-65-apk-axml-byte-evidence.md
0/0 round-67-apk-axml-byte-evidence.md           0/1 round-68-apk-axml-byte-evidence.md
0/0 round-69-apk-axml-byte-evidence.md           0/0 round-70-apk-axml-byte-evidence.md
2/2 seed.md  2/2 tool-validation-by-function-and-version.md  2/2 utf16-unpaired-surrogates-in-resource-names.md
```

No entry flips 0→2. The only verdict change is round-68 `1→0`, which is the **pin** mechanism (`apply_pin` :123-143), not the confinement; it is C3's claim surface, not mine, and I did not score it.

**C05 / C1 input (my seat's gate contribution):** the landed candidate `corpus/knowledge/round-70-apk-axml-byte-evidence.md` declares 24 blocks (`grep -c '^\$ '` = 24) and the landed gate reports

```
checked_blocks=24 problems=0   (exit 0)
```

so the confinement drops nothing from the C05 candidate's coverage: 24 declared = 24 checked. On the confinement axis alone I have no FAIL for C1.

## 3. Hostile spelling matrix (exit code, landed gate, hostile entry in scratch, cwd = tree root)

| # | declared command | exit | first output line |
|---|---|---|---|
| T0 | `python3 -B corpus/fixtures/apk-r65/readout.py --fact eocd` | **0** | `checked_blocks=1 problems=0` |
| A | `python3 -B corpus/evil.py` (→ `/etc/hostname`) | **2** | could-not-evaluate |
| B | `python3 -B corpus/inlink2.py --fact eocd` (symlink → in-tree readout) | **2** | could-not-evaluate |
| C | `python3 -B corpus/outdir/x.py` (`outdir` → `/tmp/.../outside`) | **2** | could-not-evaluate |
| D | `python3 -B corpus/fixtures/apk-r65/readout.py/ --fact eocd` (trailing slash, file) | **1** | `drift entry:2 command exited 2: ...` |
| E | `python3 -B corpus/fixtures/` (trailing slash, directory) | **1** | `drift entry:2 command exited 1: ...` |
| F | `python3 -B ./corpus/../../x.py` | **2** | could-not-evaluate |
| G | `python3 -B corpus/../../x.py` | **2** | could-not-evaluate |
| H | `PYTHON3 -B corpus/.../readout.py --fact eocd` | **2** | could-not-evaluate |
| I | `Python3 -B corpus/.../readout.py --fact eocd` | **2** | could-not-evaluate |
| J | `python3.14 -B corpus/.../readout.py --fact eocd` | **2** | could-not-evaluate |
| K | `/usr/bin/python3 -B corpus/.../readout.py --fact eocd` | **0** (launched by `/usr/bin/python3`) | `checked_blocks=1 problems=0` |
| L | `python -B corpus/.../readout.py --fact eocd` | **0** | `checked_blocks=1 problems=0` |
| M | `python3 -B -c 'print(1)'` | **2** | could-not-evaluate |
| N | `python3 -B -m json.tool` | **2** | could-not-evaluate |
| O | `python3 -B corpus/../corpus/fixtures/apk-r65/readout.py --fact eocd` | **2** | could-not-evaluate |
| P | `python3 -B /tmp/.../outside/x.py` | **2** | could-not-evaluate |
| Q | `python3 -B corpus/evil.py/` (trailing slash on symlink) | **2** | could-not-evaluate |
| R | `python3 -B .` | **1** | `drift entry:2 command exited 1: python3 -B .` |
| S | `python3 -V` | **2** | could-not-evaluate |
| — | `python3 -B corpus/loop.py` (self symlink loop) | **2** | could-not-evaluate |
| — | `python3 -B corpus/loopy1.py` (two-node loop) | **2** | could-not-evaluate |
| — | `python3 -B corpus/rootlink.py` (→ `/root/secret/x.py`) | **2** | could-not-evaluate |
| — | `python3 -B corpus/broken.py` (→ `/nonexistent/deep/x.py`) | **2** | could-not-evaluate |

**No hostile spelling yields exit 0.** Every refusal is exit 2 (`evaluate` :172-173 → `main` :261-264), not exit 0; the trailing-slash spellings (D, E) are *accepted by `inside`* (Path strips the trailing slash) but the interpreter then fails, so they land on the documented `drift entry:N command exited RC` finding (exit 1) — a failing verdict, not a clean one. `inside`'s `except ValueError` (:94) also absorbs symlink loops and unreadable targets without a traceback (measured above), which is stronger than I expected: `resolve()` never raised here.

## 4. Findings

**F1 (red-before absent — the material one). The confinement has no failing test.** `_self_test` asserts only the predicate's booleans (`:244-249`, `confined([...])` called directly); it never asserts that `run_cmd`/`evaluate` *honours* them. Mutant: delete the two wiring lines `if not confined(argv, cwd): return None, "", 2` (`:104-105`), keep everything else.

```
$ python3 -B c2.py --self-test
SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired, pinned script verified by digest and named by the entry, commands confined to relative scripts inside the tree
MUT2_SELFTEST_RC=0
$ python3 -B c2.py --entry ../outside_entry.md     # $ python3 -B corpus/outside.py, outside.py -> /tmp/.../outside/run.py
checked_blocks=1 problems=0
MUT2_ENTRY_RC=0
$ python3 -B corpus/check_embedded_outputs.py --entry ../outside_entry.md   # landed bytes
could-not-evaluate: no `$ cmd` blocks, unsupported command, or read failure
LANDED_ENTRY_RC=2
```

The mutant is **unkilled** (self-test green) and the unconfined gate **executes out-of-tree code and returns a false clean (0)**. The frozen counters contain no confinement mutant at all: `grep -n "confin\|CONFIN\|symlink\|inside(" reports/round-70/measure.py reports/round-70/measure-a1.py` → no match. So the round-70 hardening is behaviourally present in the landed bytes but is not defended by any red-before at self-test or counter level — the same class as round-67 M45 / round-68 M46 (an instrument whose claimed property has no attributable failing control).
*Smallest safe correction:* in `_self_test`, after the predicate block, write a temp entry whose script is a symlink leaving the temp tree and `require(evaluate(that_entry, tmp) == (None, None), "self-test: an out-of-tree symlink script was evaluated")`; add one counter mutant that deletes `:104-105` and expect exit 2.

**F2 (secondary red-before gap). The `is_symlink` clause (`:93`) is load-bearing and untested.** The self-test's `link.py` targets `/etc/hostname`, i.e. *outside* the tree, so the `resolve()/relative_to` half alone rejects it. Mutant dropping `and not (root / p).is_symlink()`:

```
$ python3 -B c1.py --self-test
SELFTEST OK: ... commands confined to relative scripts inside the tree
MUT_SELFTEST_RC=0
$ python3 -B c1.py --entry ../b2.md     # $ python3 -B corpus/inlink2.py, symlink -> in-tree readout.py
checked_blocks=1 problems=0
MUTANT_inlink2_RC=0
$ python3 -B corpus/check_embedded_outputs.py --entry ../b2.md   # landed
LANDED_inlink2_RC=2
```

Note the clause is *stricter than its own docstring* (`:76-77` says "no symlink **leaving the tree**"), and stricter than amendment A1's wording (`claims-amendment-A1.md:37` "commands confined to relative scripts inside the tree"): an in-tree symlink is refused although it stays in the tree. Either the clause or the wording should move.

**F3 (live coverage downgrade, no live verdict change).** `round-64:74` and `:76` were *evaluated* at base and are *refused* now. Synthetic reproduction of the class (block 1 `python3 -c`, block 2 drifted):

```
$ python3 -B corpus/check_embedded_outputs.py --entry ../mask.md
could-not-evaluate: no `$ cmd` blocks, unsupported command, or read failure     LANDED_mask_RC=2
$ python3 -B base_checker.py --entry ../mask.md
drift entry:8 embedded output line not in recheck stdout: {"eocd_offset": 999}
checked_blocks=2 problems=1                                                    BASE_mask_RC=1
```

So the confinement can turn a **named drift finding (exit 1)** into **could-not-evaluate (exit 2)** — the ticket's regression class. It is not a false clean, and on the 17 live entries it changes no verdict (§2 table), but `python3 -V` is a legitimate deterministic readout that a knowledge entry may legitimately declare (round-64 does) and it is now uncheckable. Also note the perverse incentive: on this host `/usr/bin/python3 -> python3.14` (`ls -l`), so an entry that pins its interpreter (`python3.14`) is refused while the unpinned spelling passes.

**F4 (determinism). The accepted command set depends on the launcher, not on the entry.** `run_cmd:102` allows `sys.executable` as an `argv[0]` spelling, and `:106` then runs *that* interpreter. Same entry bytes, two launchers:

```
$ /tmp/.../venv/bin/python3 -B corpus/check_embedded_outputs.py --entry ../k.md   # $ /usr/bin/python3 -B corpus/.../readout.py
could-not-evaluate: ...                                                        venv-launched K exit=2
$ python3 -B corpus/check_embedded_outputs.py --entry ../k.md
checked_blocks=1 problems=0                                                    system-launched K exit=0
```

Inherited from base (the tuple predates round 70), but round 70 is the commit that claims a *closed* command set, and `:106` also means every declared `python3` is silently re-pointed at the launcher's interpreter, so a re-derivation's interpreter version is a property of the runner. No live entry uses an absolute interpreter, so no live impact.

**F5 (confinement is applied after pin substitution, so a pin can launder a refused spelling).** `evaluate` order: `apply_pin` (`:167`) then `run_cmd` (`:171`). A pin keyed on the *declared* argument rewrites the command before the confinement ever sees it:

```
# entry: $ python3 -B ../../evil.py --fact eocd   + entry text naming the pinned digest
$ python3 -B corpus/check_embedded_outputs.py --entry ../launder.md     # pin "../../evil.py" -> corpus/fixtures/apk-r65/readout.py
checked_blocks=1 problems=0        LANDED_launder_RC=0
$ ... same entry, pin key removed                                        LANDED_launder_nopin_RC=2
```

No out-of-tree code executes (the `use` path is itself confined, `:135-136`), so this is not an escape — but "commands confined to relative scripts inside the tree" is then a property of *what runs*, not of *what the entry declares*, and exit 0 certifies a command the entry does not contain. The entry must name the pinned digest in its own text (`:137-138`), which limits it to an author who is already editing both files.

**F6 (registry/docstring stale against the landed bytes — freshness).**
* `corpus/check_embedded_outputs.py:15-17` still says the gate "Re-parses every fenced block whose first line is `$ <command>`, runs that exact command (argv list, no shell)"; `:25-27` "runs the entry's declared commands". Neither mentions confinement.
* `SKILL.md:279` verdict map: "`2` could-not-evaluate (no `$ cmd` blocks / unsupported command)" — a confinement refusal is reported under "unsupported command", and `SKILL.md:283` write scope still says "runs the entry's declared commands (argv list, no shell, `python3` first token only)". The confinement rule (`no -c/-m`, no absolute/`..`/symlink script) is stated **only** in `reports/round-70/claims-amendment-A1.md:37`, not in the registry home.
* The refusal message names nothing: `could-not-evaluate: no `$ cmd` blocks, unsupported command, or read failure` gives no entry line and no command, so an author cannot tell *which* block was refused or why (contrast the drift findings, which carry `entry:N`).
* Inherited, not round-70: a multi-line `$ python3 -c '...` block is parsed one line at a time, so `shlex.split` raises uncaught at `:163` → traceback, **exit 1 with no verdict line** (measured: `LANDED_unbal_RC=1`, `BASE_unbal_RC=1`). Live bytes contain two such blocks (`round-64:147`, `round-62:95`); both are currently masked because an earlier block in the same entry returns exit 2 first. Fixing F3 (allowing `python3 -V`) would not unmask it, but a future entry with an unclosed quote as its *first* block would crash the gate as a "failed" verdict.

## 5. What this does NOT establish

* No statement about C1's Q01-Q15 decisions (other seats), about C2's `SELF_MISMATCH` counter, or about C3's pin digest provenance. I only used the pin mechanism as an input to F5.
* No claim that the confinement is bypassable by an entry: every escape spelling I built is refused, and the only exit-0 paths run an in-tree regular file (T0, K, L) or a pin-substituted in-tree file (F5). The confinement constrains the *script argument only* — arguments, the child's inherited environment (`PYTHONPATH`/`PYTHONHOME` are not scrubbed) and the script's own syscalls are outside it, as at base.
* I did not read `.ufo/waves/round-70/w1/` before forming this verdict; the verdict above stands on the landed bytes and base comparison alone.

## 6. Tooling / hygiene

No packages installed or updated (pacman paused; nothing needed — stdlib `python3` 3.14.8 and `python3 -m venv` only). All mutations and hostile trees lived in `/tmp/revenger-r70-R70W2GateConfinement/` (copy of the `git archive` extraction); scratch directory deleted. No mutating git command was run in the lane or the fleet (`git show` / `git archive` / `git log` only). No lane file written except this report.
