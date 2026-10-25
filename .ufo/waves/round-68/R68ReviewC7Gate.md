CLEAN — the repaired gate is reachable and unshadowed on the frozen mutant path (exit 1, last line exactly `drifted entry output accepted`), the unmutated self-test exits 0, and `--entry` still detects the committed M39 drift (exit 1); one documentation defect outside the gate code: the registry row still asserts the marker "can never fire" (SKILL.md:268).

seat: L1Revenger68.R68ReviewC7Gate · role: independent reviewer (read-only) · round 68 · 2026-10-25
lane: /home/vgpnk/Projects/shokunin/revenger-shokunin · HEAD at review: `4232235` "round-68: build — C7 gate attribution repair (reachable marker as the killing line), AXML anchor derivation script + pinned snapshot copy, C05 v3 candidate (machine-derived anchors), S046 row"
artifact under review: `corpus/check_embedded_outputs.py` (172 lines, sha256 `b89183bec2fd3b94f5b0acc828a0d3fe16f6a98dde1d7752616da85d08a8e0ca`)
Nothing was edited. All runs were read-only over the lane tree; mutants were made in `/tmp/r68c7/` copies.

## 0. Provenance of the reviewed bytes

```
$ git log -1 --format='%H %s'          -> 4232235723cf8d4731a1e7e78ca098b8af953a57 round-68: build — ...
$ git status --porcelain corpus/check_embedded_outputs.py corpus/knowledge/ SKILL.md corpus/snapshots/
(empty)
```

The gate, the three knowledge entries and `corpus/snapshots/` are clean at HEAD `4232235`, so every run
below reads HEAD bytes. (The one counter run in §5 used a working-tree copy of `corpus/`; the C7 labels it
prints read only those clean paths — stated again there as a caveat.)

## 1. Q1 — is `drifted entry output accepted` reachable, and the LAST line, when the verbatim comparison is removed?

**Yes, on the frozen-mutant path; measured, exit 1.**

Control flow of `--self-test` (every line number verified against the file):

| line | code | taken under frozen mutant? |
|---|---|---|
| `:154` | `if args == ["--self-test"]:` | yes |
| `:155` | `with tempfile.TemporaryDirectory(...)` | yes |
| `:156` | `_self_test(Path(d))` | yes |
| `:133-134` | `require(problems is not None and checked == 1 and not problems, "self-test: clean entry not clean")` | **no** |
| `:135` | `dproblems, dchecked = evaluate(drifted_entry, tmp)` | yes |
| `:140-141` | `caught = (dproblems is not None and dchecked == 1 and dproblems and dproblems[0].startswith("drift entry:"))` | `caught = False` |
| `:142-145` | `if not caught: print("self-test: drifted entry not caught"); print(MARKER); sys.exit(1)` | **yes** |
| `:147-148` | `require(fproblems is not None and fchecked == 1 and not fproblems, "self-test: full-run entry not clean")` | not reached |

Why `caught` is False: the mutant replaces the only comparison site, `:105`
`problems += drift(lines, stdout_set, lineno)` (clause count in the file = 1, verified
`grep -c` = 1; the counter's regex `measure.py:385` `problems \+= drift\(lines, stdout_set, lineno\)`
matches the same single site). With no comparison, the drifted fixture's `evaluate()` returns
`problems == []`, `checked == 1` (`:106` still increments) ⇒ `dproblems` falsy ⇒ `caught` False.

`MARKER` is emitted from exactly one statement — `:144` — and the literal is defined once, at `:36`
(`grep -n 'MARKER'` → `36:MARKER = ...`, `144: print(MARKER)`). There is **no other emission site**.

Measured (frozen mutant == claims.md §C1 "Frozen mutant", applied to a byte-copy of the HEAD gate):

```
=== MUTANT: self-test ===
exit=1
self-test: drifted entry not caught$        <- cat -A
drifted entry output accepted$              <- cat -A, no trailing bytes
--- last line plain ---
drifted entry output accepted
```

Negative control (same mutant + `MARKER = "drifted entry output accepted (spoofed)"`, both clauses once each):

```
=== NEG CONTROL: mutant + spoofed marker, self-test ===
exit=1
self-test: drifted entry not caught
drifted entry output accepted (spoofed)
--- endswith real MARKER? --- 'drifted entry output accepted (spoofed)' False
```

⇒ killed `1/1`, attributed `0/1` — the attribution rule is not satisfiable by "any non-zero exit".

## 2. Q2 — can any other `require`/exit fire BEFORE the marker on that path?

**On the frozen-mutant path: no.** Exactly one `require` sits ahead of the marker, `:133-134`, and it is not
taken, because the frozen mutant leaves clean-entry evaluation intact (`problems == []`, `checked == 1` for
the clean fixture — the comparison it removes has nothing to report on a clean entry). This is measured, not
inferred: the mutant run in §1 does reach `:144`.

Complete exit inventory reachable from `--self-test` (nothing else can run on that path):

| site | line(s) | message / effect | marker last line? |
|---|---|---|---|
| `require()` body | `:39-42` (`print(msg); sys.exit(1)`) | generic exit used by the two requires | per call site |
| clean-entry require | `:133-134` → exit at `:42` | `self-test: clean entry not clean` | **no** |
| forged-control kill | `:142-145` (`print(MARKER); sys.exit(1)`) | `drifted entry output accepted` | **yes** |
| full-run require | `:147-148` → exit at `:42` | `self-test: full-run entry not clean` | **no** |
| success | `:157` `sys.exit(0)` | prints `SELFTEST OK: …` at `:149` | n/a |

`:161-162` (`exit 2`) and `:168` (`exit 64`) are `--entry`/usage paths, unreachable under `--self-test`.

So the marker is reachable and last on **1 of 3** `--self-test` failure exits. The round-67 M45 shape (a
require ahead of the marker) still exists at `:133-134`; the repair was to make the frozen mutant not trip
it, not to remove the ordering. Three probes prove the other two exits bypass the marker (each on a `/tmp`
copy, each reproducible):

```
probeA  drift() always reports (inverse mutant)        -> exit 1, last line: self-test: clean entry not clean
probeB  frozen mutant + reader.py raises SystemExit(1) -> exit 1, last line: self-test: clean entry not clean
probeC  real comparison kept, full-run fixture reports -> exit 1, last line: self-test: full-run entry not clean
```

This does **not** violate the C1 predicate, which attributes only the frozen removal mutant — but it makes
the module docstring's universal claim at `:20-23` literally false: "*the marker is the last output line of a
failed run*". It is the last line of the **drift-detection** failure run only. See F2.

## 3. Q3 — does the unmutated self-test still exit 0 and print SELFTEST OK?

**Yes.**

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && python3 -B corpus/check_embedded_outputs.py --self-test
SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
exit=0
```

(`:149` is the only printer of that line; `:157` exits 0.)

## 4. Q4 — does `--entry` mode still detect drift?

**Yes, exit 1 on the committed red snapshot.**

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && python3 -B corpus/check_embedded_outputs.py \
    --entry corpus/knowledge/round-65-apk-axml-byte-evidence.md
drift entry:41 embedded output line not in recheck stdout: {"cd_index": 2, ..., "fact": "member[META-INF/MANIFEST.MF]", ...}
checked_blocks=15 problems=1
exit=1
```

Last line `checked_blocks=15 problems=1` (by design — `:165` prints the summary after the problem lines, so
the marker is deliberately not the attribution surface of `--entry` mode; the counter reads `--entry` only
for `C7_RED_ON_R65_CANDIDATE`, `measure.py:429-431`, where it tests `rc != 0`). The named entry line `:41`
and the exit 1 match the registry's pinned expectation (`SKILL.md:269`), and the pinned snapshot hash
matches: `sha256sum` → `cf42cc2059e454027685a59a2a35a190f6ba981f95645f41e407c47c01c4d05a`.

No false positives on the two later candidates (read-only runs): r67 candidate `checked_blocks=16 problems=0`
exit 0; r68 v3 candidate `checked_blocks=17 problems=0` exit 0 — matching the C2 claim's stated `17 blocks,
0 problems`.

## 5. Counter labels on the reviewed bytes

`reports/round-68/measure.py` (sha256 pinned `0de4eb6f…f7766`; not re-hashed here beyond the contract's
claim) run against a copy of the clean-at-HEAD `corpus/` (`/tmp/r68tree/corpus`), reproducing the counter's
own C7 block, `TMPDIR` isolated:

```
C7_GATE_PRESENT=yes
C7_SELFTEST=pass :: SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
MUTANT check_embedded_outputs.py control exit=0 pass :: SELFTEST OK: ...
MUTANT check_embedded_outputs.py c7 exit=1 killed :: drifted entry output accepted
C7_RED_ON_R65_CANDIDATE=yes exit=1 :: checked_blocks=15 problems=1
C7_V2_CLEAN=yes exit=0 :: checked_blocks=16 problems=0
C7_V3_CLEAN=yes exit=0 :: checked_blocks=17 problems=0
C7_CONTROL_PASS=1/1
C7_MUTANT_KILLED=1/1
C7_MUTANT_KILLED_ATTRIBUTED=1/1
MUTANT check_embedded_outputs.py c7neg exit=1 killed :: drifted entry output accepted (spoofed)
C7_NEG_SPOOF_KILLED=1/1
C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1
counter_exit=0
```

Every C7 conjunct of claims.md §C1 reads at target on these bytes, and `HOLDS_OK_V5`/`HOLDS_OK_V6` are not
mine to adjudicate. **Caveat (honesty):** this is a working-tree-copy run, not the frozen
`git archive <commit> corpus | tar -x` invocation; it is valid for the C7 block only because the sole paths
that block reads (the gate and the three knowledge entries) are clean at HEAD `4232235` (§0). The other ~50
labels in the run are not reported and are not evidence.

## Findings (severity order)

**F1 — MEDIUM. The forged control cannot detect a *weakening* of the comparison, though the in-script
comment claims it can.** `:136-139` says "*If the verbatim comparison is removed (or weakened) the branch
below is taken*". Measured counter-example: replacing `:105` with
`problems += drift(lines[:1], stdout_set, lineno)` (checks only the first embedded line) passes the
self-test untouched —

```
=== probeD (comparison weakened to first line only) ===
SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
exit=0
```

— and the same weakened gate silently accepts a drifted **second** embedded line
(`checked_blocks=1 problems=0`, exit 0) where the real gate reports
`drift entry:4 embedded output line not in recheck stdout: {"fact": "b", "v": 9}`, exit 1. Cause: every
drifted fixture in `_self_test` embeds exactly one output line (`:126-127`), so a first-line-only comparison
is indistinguishable. The frozen mutant (removal) is still killed and attributed — the C1 predicate is
unaffected — but the comment overstates the control and a whole weakening class survives it. Fix shape: add a
two-line fixture whose *second* embedded line is wrong, and require it caught.

**F2 — MEDIUM. The marker covers 1 of 3 `--self-test` failure exits; the docstring states it universally.**
See §2 for the inventory and probes A/B/C. `:20-23` must be narrowed to "the last output line of a
drift-detection failure"; otherwise a reader will over-read the attribution guarantee exactly as round 67
over-read it in the other direction. No claim-level violation.

**F3 — MEDIUM. The registry row contradicts the repaired gate.** `SKILL.md:268` (self-test field) still
states the round-67 truth as current: the marker "*is structurally shadowed by that earlier require and can
never fire — … recorded limitation, reorder fix routed*". Measured at HEAD `4232235`: it fires and is
attributed `1/1`. The row is the gate's registered contract (PROTOCOL §Gate standard) and the C1 claim
counts the registry row as part of the landed build; leaving it stale means the registration says the defect
is still open. This is a one-line correction, not a code change; it is the only defect I find in the
delivered C1 artifact set. Note the row's other fields are accurate: entry command, verdict map `0/1/2`, the
pinned red snapshot (`cf42cc…`, entry:41, exit 1 — re-verified in §4) and the family note.

**F4 — LOW. `caught` does not specifically prove the comparison ran.** `:140-141` accepts
`dproblems[0].startswith("drift entry:")`, and `:102` also emits `drift entry:{lineno} command exited {rc}:
{cmd}` — so a command failure would satisfy "drifted caught". Latent, not exploitable on this path: the clean
fixture runs the identical command first (`:132`), so any command failure aborts at `:133` before `:135`
(probeB demonstrates exactly this). Recorded so a future fixture reorder does not silently widen it.

**F5 — INFO. Non-`require` failure paths carry no marker.** `shlex.split` ValueError (`:73`),
`subprocess.run` `TimeoutExpired` (`:78-79`, `timeout=120`), and `Path.read_text` (`:91`) propagate as
tracebacks whose last line is not the marker. Same class as F2, no action implied beyond wording.

## Positive verification (what holds, with the check that holds it)

- Marker reachable and last on the frozen mutant: §1, `cat -A` shows no trailing bytes; `:144` is the only
  emission statement; `:145` exits 1.
- Single, exact mutant site: `grep -c 'problems += drift(lines, stdout_set, lineno)'` → 1; the counter's
  `C7_CLAUSE` (`measure.py:385`) is the same literal, so the counter's mutation and mine are the same edit.
- Attribution rule is falsifiable: spoof control kills with a last line that does not `endswith` the marker
  (§1), and `measure.py:428` / `:492` implement exactly `rc != 0 and last.endswith(C7_MARKER)` over
  `(stdout + stderr).strip().splitlines()[-1]` (`:146-150`).
- Clean run and drift detection both intact after the repair: §3, §4.
- No collateral: `--entry` on r67 and r68-v3 candidates is clean (§4), so the repair did not make the gate
  vacuous in entry mode.

## Residual risk

1. A weakening-class mutant (F1) is not attested by any label; `C7_MUTANT_KILLED=1/1` therefore means "the
   removal mutant is killed", not "the comparison is intact".
2. `C7_MUTANT_KILLED_ATTRIBUTED` is satisfiable only because the frozen mutant happens not to touch the
   clean/full fixtures; a two-clause mutant would land on F2's non-attributable exits and read
   `killed=1/1, attributed=0/1`. The predicate is narrow by design — that narrowness should be stated where
   the gate is registered (F3 is the same defect, in prose).
3. The registry row lagging its artifact is the same failure mode round 67 closed as M45 at the counter
   level; here it survives at the prose level.

## Verification gaps (declared, not hidden)

- I did not run the frozen invocation (`git archive <measured-tip> corpus | tar -x`) — the measured tip does
  not exist yet at review time; §5 is a working-tree-copy run of the C7 block only, justified by §0.
- I did not adjudicate Q01-Q13 on the v3 entry, the anchor derivations, the census or the verifier replay —
  other seats' scope.
- No `lsp` server is applicable to a standalone stdlib script with no callers in this repo (the gate is
  invoked as a subprocess from `measure.py` at `:405` (`C7_SELFTEST`), `:420` (frozen mutant) and `:488`
  (negative control), each through `run()` at `:146-150`, which I read directly); all cross-file
  claims above are from those read sites, not from grep inference.

## Tooling record

No installs, upgrades or package-manager transactions were performed for this review (per the 2026-10-19
directive's recording requirement: nothing to record). Mutants and probe copies were created only under
`/tmp/r68c7/`; the lane tree, `corpus/`, `reports/`, `SKILL.md`, the Git index and the jj state were not
modified.
