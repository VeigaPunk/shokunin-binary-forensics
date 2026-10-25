NO-REGRESSION — the landed gate reproduces every base label that must hold (`EMB_R68` 7→0, `EMB_R65` 1 retained, `EMB_R67/R69` 0, new `EMB_R70` 24/0), the registered comparison line is byte-identical and present exactly once, and the frozen round-68 counter's C7 section on the landed tree is label-for-label identical to `measure-after.log` (`C7_MUTANT_KILLED_ATTRIBUTED=1/1`, `C7_SELFTEST=pass`, counter exit 0); two exit-contract defects found are **base-identical retained**, not introduced by this wave.

seat: R70W2GateReplay (fresh wave-2 seat; `.ufo/waves/round-70/w1/` was NOT read before this verdict and was not read at all)
target: lane commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd` (`admission-status: candidate`, README C05 `uncovered`); base `3f5edbc206351232a3d2d801334dd930499ccaf5`
date: 2026-10-25

## Identity of what was replayed

| artifact | landed `17ee7f8` | base `3f5edbc` |
|---|---|---|
| `corpus/check_embedded_outputs.py` blob sha256 | `5f42415bd4124cf916ecfd9b745d030254a29d299afbe8061a89b784e0d9e879` | `b89183bec2fd3b94f5b0acc828a0d3fe16f6a98dde1d7752616da85d08a8e0ca` |
| registered line `problems += drift(lines, stdout_set, lineno)` | line **178**, 1 occurrence | line **105**, 1 occurrence |
| `corpus/derive_axml_anchors_r68.py` sha256 | `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249` (= S046 row digest) | absent |
| `reports/round-70/measure.py` / `measure-a1.py` / `reports/round-68/measure.py` sha256 | `488f95aa…c88c76` / `96feeaa0…e87191` / `0de4eb6f…93f7766` (all as frozen) | — |

Trees: `git archive <commit> corpus | tar -x -C /tmp/revenger-r70-GateReplay/{landed,base}`; full trees likewise at `{full-landed,full-base}`. Every gate call below ran with **cwd = the archived tree root** and the tree's own gate.

## (1) `--entry` over EVERY `corpus/knowledge/*.md` — both trees

Landed (17 files):

```
2026-10-12-rea-readiness-checklist.md        rc=2  could-not-evaluate: no `$ cmd` blocks…
commonjs-destructured-require-edges.md       rc=2  could-not-evaluate…
digest-scope-versus-provenance.md            rc=2  could-not-evaluate…
evm-saved-interface-candidates.md            rc=2  could-not-evaluate…
pe-resource-directory-layout.md              rc=2  could-not-evaluate…
round-62-commonjs-require-name-evidence.md   rc=2  could-not-evaluate…
round-62-evm-dispatch-byte-evidence.md       rc=2  could-not-evaluate…
round-63-zip-central-directory-evidence.md   rc=2  could-not-evaluate…
round-64-firmware-region-byte-evidence.md    rc=2  could-not-evaluate…
round-65-apk-axml-byte-evidence.md           rc=1  checked_blocks=15 problems=1
round-67-apk-axml-byte-evidence.md           rc=0  checked_blocks=16 problems=0
round-68-apk-axml-byte-evidence.md           rc=0  checked_blocks=17 problems=0
round-69-apk-axml-byte-evidence.md           rc=0  checked_blocks=17 problems=0
round-70-apk-axml-byte-evidence.md           rc=0  checked_blocks=24 problems=0
seed.md                                      rc=2  could-not-evaluate…
tool-validation-by-function-and-version.md   rc=2  could-not-evaluate…
utf16-unpaired-surrogates-in-resource-names.md rc=2  could-not-evaluate…
```

Base (16 files): the same 12 `rc=2` entries, and `r65 rc=1 15/1`, `r67 rc=0 16/0`, **`r68 rc=1 17/7`**, `r69 rc=0 17/0` — `round-70-…md` absent.

Every delta, explained:

| entry | base | landed | explanation |
|---|---|---|---|
| r68 | 17 blocks, **7 problems**, rc=1 | 17 blocks, **0 problems**, rc=0 | C3's pin: `embedded_output_pins.json` rebinds the block's script argument `corpus/derive_axml_anchors.py` to `corpus/derive_axml_anchors_r68.py` (sha256 verified before use). Command: `rm corpus/embedded_output_pins.json` in a copy → the same entry reads **7 problems** again (mutation E below), so the 7→0 is the pin and nothing else. |
| r65 | 15/1 rc=1 | 15/1 rc=1 | retained M39 transcription drift, unchanged bytes (`cf42cc20…` both sides). Located: entry:41 quotes `payload_first16_hex":"4d616e696673742d…"` while `python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[META-INF/MANIFEST.MF]'` prints `4d616e69666573742d…` (`6e69 6673` vs `6e69 6665 7374` — characters dropped). |
| r67 / r69 | 16/0, 17/0 | same | untouched, bytes identical (`057a1826…`, `f869340b…`). |
| r70 | absent | 24/0 rc=0 | new candidate; 24 blocks, 0 vacuous (measured: every one of the 24 has ≥1 embedded output line). |
| other 12 | rc=2 | rc=2 | no `$ cmd` block at all — documented exit 2, identical on both sides, no change. |

Knowledge-dir delta base→landed is exactly one added file (`819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31  round-70-apk-axml-byte-evidence.md`); `diff` of the two sha256 census files shows no other line.

Gate `--self-test`: landed `SELFTEST OK: … pinned script verified by digest and named by the entry, commands confined to relative scripts inside the tree`, **exit 0**; base `SELFTEST OK: … forged control fired`, **exit 0**. No-args → exit 64 on landed.

## (2) `git diff 3f5edbc 17ee7f8 -- corpus/check_embedded_outputs.py`

`1 file changed, 103 insertions(+), 1 deletion(-)`.

**Registered comparison line**: unchanged and present exactly once.
`git show 17ee7f8:corpus/check_embedded_outputs.py | grep -c 'problems += drift(lines, stdout_set, lineno)'` → `1` (line 178). No `-` line in the diff touches it; the only hunk that edits the enclosing `evaluate()` loop *adds* pin lines before/around it (`@@ -96,0 +160,2 @@`, `@@ -97,0 +163,8 @@`, `@@ -106,0 +180,3 @@`). The frozen counter's own regex agrees: `C7_CLAUSE.findall` → 1 hit, `C7_MUTANT_KILLED=1/1`.

**Removed lines — exactly one** (base `corpus/check_embedded_outputs.py:149`):
```
    print("SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired")
```
replaced by the extended self-test summary (added line 103 below).

**Added lines — all 103**, in diff order (`git diff -U0 … | grep '^+'`):
```
 1  import hashlib
 2  PIN_MARKER = "pinned historical script digest mismatch"
 3  PINS_REL = "embedded_output_pins.json"
 4  def confined(argv, cwd):
 5      """Round-70 hardening (sentinel F1): the declared command may only be
 6      `python3 [-B] <relative script inside cwd> [args]` — no `-c`/`-m`, no absolute or
 7      `..` script path, no symlink leaving the tree."""
 8      rest = argv[1:]
 9      while rest and rest[0] == "-B":
10          rest = rest[1:]
11      if not rest or rest[0].startswith("-"):
12          return False
13      return inside(rest[0], cwd)
14
15
16  def inside(rel, cwd):
17      p = Path(rel)
18      if p.is_absolute() or ".." in p.parts:
19          return False
20      root = Path(cwd).resolve()
21      try:
22          return (root / p).resolve().relative_to(root) is not None and not (root / p).is_symlink()
23      except ValueError:
24          return False
25
26
27      if not confined(argv, cwd):
28          return None, "", 2
29  def load_pins(entry_path):
30      """Round-70 C3 (freshness): a retained entry whose embedded output was printed
31      by an earlier revision of a script re-derives against that revision, pinned by
32      sha256 in corpus/embedded_output_pins.json, never against the current script.
33      Shape: {"<entry file name>": {"<script arg as written in the command>":
34      {"use": "<repo-relative path of the pinned copy>", "sha256": "<hex>"}}}."""
35      p = Path(__file__).resolve().parent / PINS_REL
36      if not p.is_file():
37          return {}
38      return json.loads(p.read_text(encoding="utf-8")).get(Path(entry_path).name, {})
39
40
41  def apply_pin(cmd, pins, cwd, entry_text=None):
42      """Return (command, problem). A pinned script is verified by digest before it
43      replaces the script argument; a digest mismatch is a problem, not a fallback.
44      Round-70 tightening (R70W1PinMut/PinCritic): the `use` path must stay inside cwd (no
45      absolute path, no `..`, no symlink) and, when entry_text is given, the entry's own text
46      must name the pinned digest in full — a pin is the entry declaring which script revision
47      printed its output, never a free assignment."""
48      argv = shlex.split(cmd)
49      idx = next((i for i, a in enumerate(argv[1:], 1) if not a.startswith("-")), None)
50      if idx is None or argv[idx] not in pins:
51          return cmd, None
52      pin = pins[argv[idx]]
53      if not inside(pin["use"], cwd):
54          return cmd, f"{PIN_MARKER}: {pin['use']} (path escapes the tree)"
55      if entry_text is not None and pin["sha256"] not in entry_text:
56          return cmd, f"{PIN_MARKER}: {pin['use']} (entry text does not name the pinned digest)"
57      target = Path(cwd) / pin["use"]
58      if not target.is_file() or hashlib.sha256(target.read_bytes()).hexdigest() != pin["sha256"]:
59          return cmd, f"{PIN_MARKER}: {pin['use']}"
60      argv[idx] = pin["use"]
61      return shlex.join(argv), None
62
63
64      pins = load_pins(entry_path)
65      used = set()
66          pargv = shlex.split(cmd)
67          pidx = next((i for i, a in enumerate(pargv[1:], 1) if not a.startswith("-")), None)
68          if pidx is not None and pargv[pidx] in pins:
69              used.add(pargv[pidx])
70          cmd, pin_problem = apply_pin(cmd, pins, cwd, text)
71          if pin_problem:
72              problems.append(f"drift entry:{lineno} {pin_problem}")
73              continue
74      for key in pins:
75          if key not in used:
76              problems.append(f"drift entry:0 unused pin for script argument {key}: no block of this entry runs it")
77      old = tmp / "old_reader.py"
78      old.write_text("print('old')\n", encoding="utf-8")
79      pins = {"reader.py": {"use": "old_reader.py", "sha256": hashlib.sha256(old.read_bytes()).hexdigest()}}
80      pinned_cmd, pin_problem = apply_pin("python3 -B reader.py --fact a", pins, tmp)
81      require(pin_problem is None and pinned_cmd.split()[2] == "old_reader.py",
82              "self-test: a digest-verified pin did not replace the script argument")
83      old.write_text("print('tampered')\n", encoding="utf-8")
84      _, pin_problem = apply_pin("python3 -B reader.py --fact a", pins, tmp)
85      if not (pin_problem and pin_problem.startswith(PIN_MARKER)):
86          print("self-test: a tampered pinned script was accepted")
87          print(PIN_MARKER + " not raised")
88          sys.exit(1)
89      old.write_text("print('old')\n", encoding="utf-8")
90      require(apply_pin("python3 -B reader.py --fact a", pins, tmp, "text naming " + pins["reader.py"]["sha256"])[1] is None,
91              "self-test: a pin whose digest the entry text names was refused")
92      _, pin_problem = apply_pin("python3 -B reader.py --fact a", pins, tmp, "text that names no digest")
93      require(pin_problem is not None and pin_problem.startswith(PIN_MARKER),
94              "self-test: a pin the entry text does not name was accepted")
95      (tmp / "link.py").symlink_to("/etc/hostname")
96      require(confined(["python3", "-B", "reader.py", "--fact", "a"], tmp)
97              and not confined(["python3", "-c", "print(1)"], tmp)
98              and not confined(["python3", "-B", "-m", "json.tool"], tmp)
99              and not confined(["python3", "-B", "/etc/passwd.py"], tmp)
100             and not confined(["python3", "-B", "../x.py"], tmp)
101             and not confined(["python3", "-B", "link.py"], tmp),
102             "self-test: command confinement accepted or refused the wrong spelling")
103     print("SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired, pinned script verified by digest and named by the entry, commands confined to relative scripts inside the tree")
```
Nothing in the added set weakens the comparison: `drift()` itself, `parse_blocks()` and `main()`'s exit contract are untouched; the only behavioural change inside `evaluate()` is that a block may be rewritten (pin) or short-circuited (pin problem) **before** the unchanged comparison runs.

## (3) Frozen round-68 counter's C7 section on the landed tree

`python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-68/measure.py /tmp/…/full-landed` → **exit 0**. C7 region (lines 68-80), side-by-side against `reports/round-68/measure-after.log` (same lines, `::` suffix stripped) — all 13 rows `SAME`:

```
SAME C7_GATE_PRESENT=yes
SAME C7_SELFTEST=pass
SAME MUTANT check_embedded_outputs.py control exit=0 pass
SAME MUTANT check_embedded_outputs.py c7 exit=1 killed
SAME C7_RED_ON_R65_CANDIDATE=yes exit=1
SAME C7_V2_CLEAN=yes exit=0
SAME C7_V3_CLEAN=yes exit=0
SAME C7_CONTROL_PASS=1/1
SAME C7_MUTANT_KILLED=1/1
SAME C7_MUTANT_KILLED_ATTRIBUTED=1/1
SAME MUTANT check_embedded_outputs.py c7neg exit=1 killed
SAME C7_NEG_SPOOF_KILLED=1/1
SAME C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1
```
The attributed kill still reads **1/1**; `C7_SELFTEST` is `pass` (exit 0) — its printed text is the extended summary, truncated by the counter at 160 chars, the label is unchanged. Whole-log label diff (after stripping `:: …`) is empty over counter lines 1-98; the only `diff` output is the after-log's appended human receipt prose (its lines 99-112), which is not counter output. `HOLDS_OK`, `_V2`, `_V3`, `_V4`, `_V5`, `_V6` all `yes`.

Independent replay of the same registered mutant (my copy, not the counter's): clause replaced with `problems += []` → `--self-test` exit **1**, last line exactly `drifted entry output accepted` (attribution holds).

Round-70 counter on the same tree (corroboration, exit 0): `C1_GATE=checked_blocks=24 problems=0 exit=0 ok=yes`, `C1_LINT=… exit=0`, `EMB_R65=15/1`, `EMB_R67=16/0`, `EMB_R68=17/0`, `EMB_R69=17/0`, `EMB_PINNED_SCRIPT_IS_S046=yes`, `EMB_R68_BYTES_UNCHANGED=yes`, `EMB_R65_BYTES_UNCHANGED=yes`, `EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1`, `HOLDS_C3_V1=yes`, `HOLDS_OK_V7=yes`. `measure-a1.py` on the same tree: `A1_C1=yes A1_C2=yes A1_C3=yes`, with `A1_C3_DETAIL=binds_s046=yes script_digest=yes script_prints_17_lines=yes`.

## Mutation matrix (all on `cp -r` copies in scratch; the lane was never written)

| # | mutation | result |
|---|---|---|
| A | append `TAMPERED_SUFFIX` to the first quoted output line of the r70 entry | `drift entry:27 … TAMPERED_SUFFIX`, `checked_blocks=24 problems=1`, exit 1 — the 24-block pass is not vacuous |
| B | independent re-derivation: `python3 -B corpus/derive_axml_anchors_r68.py \| wc -l` | `17` lines; extended `derive_axml_anchors.py` → `20` lines (diff shows the 7 quoted enum lines are r68-only, the extended one adds `= 0x…` and block bounds) |
| C | append one byte to the pinned script | `drift entry:128 pinned historical script digest mismatch: corpus/derive_axml_anchors_r68.py`, exit 1; restore → `17/0` exit 0 |
| D | redact the pinned digest from the r68 entry text | `… (entry text does not name the pinned digest)`, exit 1 |
| E | delete `embedded_output_pins.json` | r68 falls back to the current script: **7** problems at entry:137-143, exit 1 — proves 7→0 is the pin, not a weakened comparison |
| F | add a pin for a script no block runs | `drift entry:0 unused pin for script argument …`, exit 1 |
| G | pin `use` = `../outside.py` | `… (path escapes the tree)`, exit 1 |
| H | `$ python3 -B -X utf8 /abs/outside.py` in an entry | exit **2**, refused (`confined` rejects a leading non-`-B` flag); `-c`, `-m`, absolute, `..` and inside-tree symlink spellings all refused (also asserted by the gate's own self-test) |

## Findings — located, none of them introduced by this wave

**F1 (retained, base-identical) — missing entry file exits 1, not the documented 2.**
`corpus/check_embedded_outputs.py:154` (landed; base `:91`):
`text = Path(entry_path).read_text(encoding="utf-8", errors="ignore")` is uncaught, while the module docstring promises exit 2 for "read failure".
```
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/does-not-exist.md
FileNotFoundError: [Errno 2] No such file or directory: 'corpus/knowledge/does-not-exist.md'
exit=1
```
Base behaves identically (exit 1, same traceback shape). Operability risk: a caller who mistypes an entry path (e.g. runs from the fleet root) gets the "drift found" code, which is the code a reader treats as a finding.

**F2 (retained, base-identical) — a command timeout exits 1 with a traceback and no marker.**
`corpus/check_embedded_outputs.py:106-107` (`subprocess.run(..., timeout=120)`) has no `except subprocess.TimeoutExpired`. Reproduced on a copy with `timeout=1` and a 5 s sleeper:
```
subprocess.TimeoutExpired: Command '['/usr/bin/python3', '-B', '-B', 'corpus/slow.py']' timed out after 1 seconds
exit=1
```
Base `:79` is the same construct with the same gap. Same consequence as F1 (exit 1 = "drift", contract says 2 = could-not-evaluate), plus no attributed text.

**F3 (coverage limit, pre-existing) — a fence without a `$ ` first line is invisible.**
`parse_blocks` only starts a block at `$ `; 8 output-shaped fences across 7 entries are therefore never checked (none in r65/r67/r68/r69/r70, so today's tabulation is unaffected):
`pe-resource-directory-layout.md:232-234`, `round-62-commonjs-require-name-evidence.md:122-265` and `:269-295`, `round-62-evm-dispatch-byte-evidence.md:578-587`, `round-63-zip-central-directory-evidence.md:239-257`, `round-64-firmware-region-byte-evidence.md:229-481`, `tool-validation-by-function-and-version.md:171-173`, `utf16-unpaired-surrogates-in-resource-names.md:180-184`. `checked_blocks` is a count of *parsed* blocks, not of the entry's quoted-output surface.

**F4 (limit, frozen) — the comparison is set-membership.** `stdout_set = set(stdout.splitlines())` means order and duplicates are not compared, and a quoted line that appears anywhere in stdout passes. This is the registered line's semantics; the line is byte-identical to base and must stay so (round-68 C7 L0), so this is recorded, not scored.

**F5 (scope observation on C3, not a predicate failure) — the pin restores the block, not the entry's prose.** The r68 retained (and `admission-status: rejected`) entry still asserts at line 148 "The chunk-type enum block spans lines **237-253**", while the current derivation prints `enum block open : 237` / `enum block close : 263` (snapshot `corpus/snapshots/ResourceTypes.h`: `enum {` at 237, `};` at 263 — read at `:237` and `:263`). The pin makes the *quoted block* re-derive (which is exactly C3's predicate) and C3 additionally freezes the r68 bytes (`EMB_R68_BYTES_UNCHANGED=yes`), so this cannot and should not be repaired inside C3 — but a reader must not take `EMB_R68 problems=0` as "the r68 entry's prose is now true". The admitted r70 candidate is not affected: it quotes `enum block open : 237` / `enum block close : 263` (entry lines 131, 140) and has no `237-253` span claim (`grep -n '237' round-70-…md` → line 131 only).

## Limits of this replay

- I did not consult `.ufo/waves/round-70/w1/` at any point, before or after forming the verdict; the only wave-1 artifact I touched is `claims-amendment-A1.md` (a frozen-contract document, not a w1 report).
- I did not judge Q01-Q15 on the C05 candidate, C1's admission flip, C2's checker bytes, or separability — those are other seats' kill-rule inputs. My scope is the gate/lint replay above.
- F1/F2 are behaviour defects against the gate's own docstring, reachable today, but they are present byte-for-byte in base, so they are **not regressions** and do not falsify any frozen label. Recording them for the round's lesson/backlog, not as a C1/C3 kill.
- No tool was installed or upgraded; no pacman transaction was attempted; no mutating git/jj command was run in the lane or the fleet. Scratch lived at `/tmp/revenger-r70-GateReplay*` and was deleted before returning.
