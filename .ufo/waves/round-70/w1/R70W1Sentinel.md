FINDINGS — the C3 gate executes code and reads files named by entry/pins content with no containment check, and the counter writes outside its temp dirs from a pins value; every other scope/safety conjunct holds.

Seat: R70W1Sentinel (wave 1, advisory). Scope: safety/scope review of `3f5edbc..aa1842f` (candidate) and `3f5edbc..dbacce2` (pre-registration). No lane file was edited; every attack ran on a `git archive aa1842f` extraction under `/tmp/revenger-r70-R70W1Sentinel-*` (deleted before return).

## 1. Scope of the diff — CONTAINED

```
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin diff --name-status 3f5edbc2 aa1842fa
M .ufo/waves/round-69/R69CounterReplay.md   A .ufo/waves/round-70/build-entry.py
A .ufo/waves/round-70/census-before.txt     A considerthese/2026-10-25.md
M corpus/check_embedded_outputs.py          A corpus/derive_axml_anchors_r68.py
A corpus/embedded_output_pins.json          A corpus/fixtures/apk-r65/entry_checks.py
A corpus/knowledge/round-70-apk-axml-byte-evidence.md  A corpus/lint_entry.py
A corpus/self_assessment_check.py           A corpus/snapshots/APPNOTE.TXT
A corpus/snapshots/dex-format.html          A corpus/snapshots/rea-android-applications.md
A reports/round-70/{before-treated-tools-on-base.log,build-controls.py,claims.md,measure-before.log,measure.py}
A reports/round-70/controls/{A..H}.log
```
27 paths, `+15019 -2`, all repo-relative, none absolute and none containing `..`; all land inside `/home/vgpnk/Projects/shokunin/revenger-shokunin`. `git diff --name-only 3f5edbc2 aa1842fa -- PROVINCE.md SKILL.md corpus/README.md` → empty: the C05 row is still `uncovered` and PROVINCE.md is byte-untouched at the candidate commit, as claims.md §C1 landing-order step (1) requires.

## 2. What holds (each re-derived here)

| conjunct | evidence |
|---|---|
| no network in any changed tool | `grep -nE "socket\|urllib\|http\|requests\|urlopen" corpus/check_embedded_outputs.py corpus/fixtures/apk-r65/entry_checks.py corpus/lint_entry.py corpus/self_assessment_check.py reports/round-70/measure.py` → no match. `readout.py` imports only `hashlib json struct sys zlib pathlib`; `derive_axml_anchors*.py` likewise, no `exec/eval/subprocess` (grep). |
| fixture bytes never executed | `entry_checks.py:130-136,180-185` run `readout.py` only; `generator.py` is never invoked by the entry (entry header S041 line says so). readout parses `struct` fields; no `exec/eval/marshal/pickle/importlib/zipfile.extract` anywhere in the recheck path. |
| normal runs leave the tree untouched | `find TREE -type f -printf '%p %s %T@\n' \| sort \| sha256sum` before/after gate `--self-test` + gate `--entry` on v5 (`checked_blocks=22 problems=0`) + lint `--self-test` + sm `--self-test` + `entry_checks --pins/--oracle` → `fc83369f0e0d…b99e` both times, `diff` → `IDENTICAL: no file created, modified or touched in the tree`. |
| counter exit-2 contract (M50) | `measure.py /tmp/…/empty-tree` (corpus/ but no README) → traceback + `COUNTER_ERROR=uncaught exception (exit 2)`, `exit=2`; `measure.py /nonexistent` → usage, `exit=2`. |
| entry's stated digests are the real bytes | `sha256sum` in the archive: `APPNOTE 0b993022…cd6 /174585`, `dex-format c0428612…d9f4 /281157`, `rea 412d9cb4…fa74c /1992`, `ResourceTypes.h 56b88bc4…c56f /86255`, `readout 92e347c3…3976`, `truth 27303bae…8173`, `generator eaa9444c…7c1a`, `fixture 05d2280f…d03e`, `derive_axml_anchors 74d4c0d9…83aa` — all nine equal entry item 14; `corpus/derive_axml_anchors_r68.py` = `bce497d6c0f5…e249` = pins `sha256` = the S046 row digest. No fabricated provenance found. |
| no secrets in changed bytes | grep for `api[_-]?key|secret|token|passwo?rd|BEGIN …PRIVATE|ghp_|AKIA|bearer` over the seven changed non-snapshot files → only the word "token" in lint/self-assessment docstrings. |
| lint takes no path from entry content | `lint_entry.py:88-91` passes only `[0-9a-f]{7,40}` as a separate argv element to `git -C lane cat-file -e`; no shell, no path. `entry_checks.py` paths are module constants (`PINS`, `SPEC_QUOTES`); no argv-supplied path. |
| build-entry.py provenance | `build-entry.py:25-30` raises `SystemExit` on `rc != 0` before pasting, so no failing command's output can be embedded; `OUT` (line 16) = `<lane>/corpus/knowledge/…` only. |

## 3. PROVINCE refusals and cross-lane absorption — CONTAINED

- `PROVINCE.md` unmodified in the diff (§1). The candidate does no live-target execution: the only artifact read is the authored `corpus/fixtures/apk-r65/fixture.apk` and the committed snapshots; entry item 3/§Unknown state no provider was called and the fixture is inert.
- No DRM/piracy content and no reversed code published: the entry publishes only spec quotations located by `--spec-quotes` (six `MATCH` lines) and digests of the authored fixture.
- ADJ-06: the only cross-lane reference is `corpus/knowledge/round-70-apk-axml-byte-evidence.md:243` — "The kaidoku/revenger ADJ-06 overlap and the fleet `l0-questions.md` entry for it stay reported, not absorbed." No sibling-lane knowledge file is cited as a source (`grep -nE "kaidoku|harness-integrity|game-dev|lore|art-east|rlm-dispatch|gate-evidence|shokuknow"` → that one line only). Not absorbed.

## 4. FINDINGS

### F1 — HIGH — the gate executes arbitrary code named by entry text; the allowlist is argv[0] only
`corpus/check_embedded_outputs.py:75-83` (`run_cmd`): only `argv[0]` is checked (`if argv[0] not in ("python3","python",sys.executable)`), then `subprocess.run([sys.executable,"-B",*argv[1:]], cwd=str(cwd))`. `evaluate` (`:118-140`) feeds it every fenced `$ …` line of the entry verbatim. So `-c`, `-m`, absolute script paths and `../` paths all pass.

```
$ cat evil_entry.md → ``` $ python3 -B /tmp/revenger-r70-R70W1Sentinel-sb/abs_escapee.py / abs escapee ran ```
$ cd TREE && python3 -B corpus/check_embedded_outputs.py --entry /tmp/…/evil_entry.md
checked_blocks=1 problems=0          # exit 0
marker: executed from absolute path outside the tree

$ cat inline_entry.md → ``` $ python3 -B -c "import pathlib;pathlib.Path('/tmp/…-MARKER-C').write_text('inline code ran');print('inline ok')" / inline ok ```
$ cd TREE && python3 -B corpus/check_embedded_outputs.py --entry /tmp/…/inline_entry.md
checked_blocks=1 problems=0          # exit 0
marker: inline code ran
```
Impact: a knowledge entry is review input; here review input is executable with the gate's privileges, and the gate reports it clean (`problems=0`). `-c`/`-m` also reach the stdlib network modules, so "no network at recheck time" is a property of today's corpus commands, not of the gate. The header claim at `corpus/check_embedded_outputs.py:25-27` ("it writes nothing outside its own temp dirs") is false as a property of the tool — see F7.
Smallest remediation: in `run_cmd`, reject any argv[1:] containing `-c`/`-m`, and require `Path(cwd, argv[idx]).resolve()` to be a regular file whose `realpath` is inside `Path(cwd,"corpus")`; report a `could-not-evaluate`/problem otherwise.

### F2 — HIGH — the pin rule's `use` value escapes the tree, and is executed
`corpus/check_embedded_outputs.py:98-111` (`apply_pin`): `target = Path(cwd) / pin["use"]` with no containment check; absolute values discard `cwd` entirely and `..` walks out. The sha256 check is self-consistent — it only proves the file the pins file named is the file the pins file hashed.

```
# pins.json: use = "../escapee.py", sha256 = sha256(escapee.py)   (escapee.py sits outside TREE)
$ cd TREE && python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md
checked_blocks=17 problems=17        # exit 1 (drift only — the pin was accepted)
marker: executed from outside the tree

# pins.json: use = "/tmp/revenger-r70-R70W1Sentinel-sb/abs_escapee.py", sha256 = sha256(that file)
$ cd TREE && python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-…md ; echo exit=$?
exit=1
marker: executed from absolute path outside the tree
```
Entry *name* is not a vector (`load_pins:86-96` uses only `Path(entry_path).name` as a JSON key, never a path), so the escape is entirely through the pins value. Impact: the C3 gate's trust root — "digest-pinned historical script" — can be pointed at any Python file on the host, executed. Symlinks inside `corpus/` are the same class (no `is_symlink`/realpath check).
Smallest remediation: require `pin["use"]` to be relative, reject any `..` component, resolve it and require `is_relative_to(<tree>/corpus)` and `not is_symlink()` before hashing/executing.

### F3 — MEDIUM — the counter writes outside its temp dirs from a pins value
`reports/round-70/measure.py:231-234`:
```
for pin in spec.values():
    target = d / pin["use"]                 # absolute / ".." escapes d
    if target.is_file():
        target.write_bytes(target.read_bytes() + b"\n# tampered\n")
```
```
$ printf 'outside-tree victim\n' > /tmp/revenger-r70-R70W1Sentinel-VICTIM.txt
# pins.json (in the tree under test): use = "/tmp/revenger-r70-R70W1Sentinel-VICTIM.txt"
$ python3 -B reports/round-70/measure.py TREE   → counter exit=0
$ cat /tmp/revenger-r70-R70W1Sentinel-VICTIM.txt
outside-tree victim

# tampered
```
Impact: the counter is run against candidate/control trees (`build-controls.py` runs it over scratch trees); a tree's `embedded_output_pins.json` therefore steers an arbitrary-file append by the scoring instrument, contradicting `measure.py:7` ("writes only inside its own temp directories") and claims.md §C3's control premise.
Smallest remediation: same containment check as F2 in the mutant loop (`target.resolve().is_relative_to((d/"corpus").resolve())`), skip otherwise.

### F4 — MEDIUM-LOW — `self_assessment_check.py` SM3 reads files outside TREE named by SHONEN content
`corpus/self_assessment_check.py:90-99`: `for tok in re.findall(r"`([\w./-]+\.(?:md|py|json))`", text): for cand in (root/tok, root/"corpus"/tok)` — `[\w./-]` admits `..`, and `root` is a `git archive` extraction that is supposed to be self-contained.
```
SHONEN box: "- [x] Landed `SKILL.md` (100 bytes) and `../sentinel-victim.py` (123 bytes)."
A: victim present at <scratch>/sentinel-victim.py (123 bytes) → SM1..SM6=0, SELF_MISMATCH=0, exit=0
B: same tree, victim renamed away            → SM3=1, SELF_MISMATCH=1, exit=1
```
Impact: the calibration count (C2's `SELF_MISMATCH=0`) can be satisfied by bytes outside the tree under test; a self-assessment may "quote" an out-of-tree digest/size and still score clean. Read-only, no execution.
Smallest remediation: `p = (root/tok).resolve()` and skip unless `p.is_relative_to(root.resolve())`.

### F5 — LOW — the pin rule is opt-out by command spelling (fails closed today)
`corpus/check_embedded_outputs.py:102-104`: `idx = first non-flag arg; if idx is None or argv[idx] not in pins: return cmd, None` — an entry that spells the script `./corpus/derive_axml_anchors.py` is silently re-derived against the **current** script, with no `PIN_MARKER` and no diagnostic that a pin existed and was skipped.
```
$ sed -i 's|^$ python3 -B corpus/derive_axml_anchors.py$|$ python3 -B ./corpus/derive_axml_anchors.py|' r68-copy.md
$ cd BYPASS && python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-…md
gate exit=1 ; grep -c "pinned historical script digest mismatch" → 0 ; checked_blocks=17 problems=7
```
Impact: C3's guarantee ("re-derives against the pinned earlier script revision") holds only for the exact spelling; today the bypass surfaces as drift (fail-closed), but the failure is mislabeled as content drift, and an entry whose lines happen to match the current script would pass as pinned though it never was.
Smallest remediation: match on the *resolved* script path (normalize `./`, `//`) and emit a problem when an entry named in pins has a block that runs the pinned script's basename without the pin applying.

### F6 — LOW (calibration) — `EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1` is satisfiable by a pre-broken pin
`reports/round-70/measure.py:225-237` tampers the pinned file, then scores `killed_pin = int(rc != 0 and PIN_MARKER in out)`. With `sha256` set to `"0"*64` from the start (no tamper semantics), the run still printed `EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1`. The label does not attribute the kill to the intended one-byte tamper. Not exploitable alone (C3 also requires `EMB_R68 problems=0` and `EMB_PINNED_SCRIPT_IS_S046=yes`), but the receipt overstates what it measured.
Smallest remediation: require the untampered run to be clean first, then tamper, then assert the marker.

### F7 — LOW — false self-description in the gate's header
`corpus/check_embedded_outputs.py:25-27` states "…it writes nothing outside its own temp dirs." Entry mode can rewrite tracked files in the lane tree through a declared command:
```
$ cat gen_entry.md → ``` $ python3 -B corpus/fixtures/apk-r65/generator.py ```
$ cd TREE && python3 -B corpus/check_embedded_outputs.py --entry /tmp/…/gen_entry.md
checked_blocks=1 problems=0          # exit 0
fixture.apk  mtime 1792962121 → 1792962851   truth.json  mtime 1792962121 → 1792962851
(sha256 unchanged: 05d2280f…d03e / 27303bae…8173)
```
`generator.py:197,226` writes `fixture.apk` and `truth.json` in place. Impact: a readiness/provenance statement in the tool's own docstring that the tool does not enforce (the same claim is inherited by claims.md §C3's "the gate … verifies by sha256 before use" framing). Smallest remediation: state the real contract (commands run with the gate's privileges) or enforce F1's containment; either way, make the header match the code.

### F8 — INFO — a malformed pin exits 1, not 2
`corpus/check_embedded_outputs.py:106` `pin["sha256"]` — a pins object without `sha256` raises `KeyError`:
```
KeyError: 'sha256'
exit=1                                # no checked_blocks line
```
Fails closed (the counter's regex then yields `C1_GATE=n/a`), but exit 1 is the tool's "drift found" code; a could-not-evaluate should be 2. One-line fix: validate the pin shape and `sys.exit(2)` / emit a `PIN_MARKER` problem.

## 5. Adjudication note for the L1
F1/F2 are not repairs to prose: they are the trust boundary of the instrument that C3 is built on. Wave-1 findings are advisory, so no kill rule is triggered; the smallest safe repair before the candidate is declared final is a containment helper used by both `apply_pin` and `measure.py`'s mutant loop, plus the `-c`/`-m`/absolute-path rejection in `run_cmd`. F4 is independent (C2's instrument). F5-F8 are label/doc fixes that do not change any frozen predicate.

Tooling: nothing installed or upgraded (pacman paused host-wide); Python 3 stdlib and read-only `git` only.
