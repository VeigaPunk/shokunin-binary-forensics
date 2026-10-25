DEFECT — the gate's own behaviour is clean on all four checks, but the C7 *hold* is unmeasurable at the round-69 tip: the frozen counter dies at `reports/round-69/measure.py:158` (`run()` called before `def run` at `:187`) on any tree containing `corpus/q15_tree_id_check.py`, printing zero `C7_*` labels and exiting 1.

seat: `L1Revenger69.R69ReviewC7Gate` · round-69 (hyaku 6) · read-only review, nothing edited
target: `corpus/check_embedded_outputs.py` sha256 `b89183bec2fd3b94f5b0acc828a0d3fe16f6a98dde1d7752616da85d08a8e0ca`
gate unchanged since the round-69 base: `git log --oneline 222a7a7..HEAD -- corpus/check_embedded_outputs.py` → empty
(only commit touching it: `4232235` round-68 attribution repair)

---

## Answers to the four asked checks

### (1) Is the marker reachable on every `--self-test` failure path as the last line? — **NO**

The marker is printed on exactly one path, the forged-control branch
`corpus/check_embedded_outputs.py:142-145`:

```python
142:     if not caught:
143:         print("self-test: drifted entry not caught")
144:         print(MARKER)
145:         sys.exit(1)
```

The other self-test failure paths exit 1 with their own message and **no marker**:

- `:133-134` — `require(..., "self-test: clean entry not clean")`
- `:147-148` — `require(..., "self-test: full-run entry not clean")`

and any uncaught exception (see F2 below; `:78-79` timeout, `:91` unguarded read) also
exits 1 with no marker and no `drift entry:` finding.

This is **not** a defect against the registered contract: `SKILL.md:279-280` scopes the
claim correctly ("the drifted case is an `if not caught:` branch … prints … then the
marker as the last line"), and `corpus/lessons/round-68-verifier-spotcheck.md:85-90`
states "reachable only through the drift branch" as the intended shape. What *is*
inaccurate is the gate docstring at `:20-23`, which universalises it — see F1.

### (2) Does any require/exit fire before it on the frozen-mutant path? — **NO**

Reproduced the frozen mutant (`measure.py:426-434`, regex must match exactly once) on a
copy of the gate:

```console
$ python3 -B /tmp/revenger-r69-c7gate/corpus/check_embedded_outputs.py --self-test; echo RC=$?
self-test: drifted entry not caught
drifted entry output accepted
RC=1
```

`clause_hits= 1`; last line `'drifted entry output accepted'`, `ATTRIBUTED= True`.

The clean-case `require` at `:133-134` executes first and **passes** (the mutant only
empties the drifted problem list, `problems += []`), and the full-run `require` at
`:147-148` is never reached (exit at `:145`). The round-67 M45 shadowing is repaired for
this path.

### (3) Does the unmutated self-test still exit 0? — **YES**

```console
$ python3 -B corpus/check_embedded_outputs.py --self-test; echo RC=$?
SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
RC=0
```

Negative control (frozen mutant + spoofed marker text) behaves as registered — killed but
unattributed:

```console
$ python3 -B corpus/check_embedded_outputs.py --self-test   # spoofed copy
self-test: drifted entry not caught
drifted entry output accepted (spoofed)
SPOOF_RC=1            # last.endswith(registered marker) == False
```

### (4) Does `--entry` still detect drift on the r65 candidate (exit 1, entry:41) and read clean on v4? — **YES / YES**

```console
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-65-apk-axml-byte-evidence.md; echo RC=$?
drift entry:41 embedded output line not in recheck stdout: {"cd_index": 2, "compressed_size": 69, ..., "payload_first16_hex": "4d616e696673742d56657273696f6e", ...}
checked_blocks=15 problems=1
RC=1

$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-69-apk-axml-byte-evidence.md; echo RC=$?
checked_blocks=17 problems=0
RC=0
```

The r65 `entry:41` drift is genuine, not a gate artifact — exactly one field differs from
the live readout:

```
payload_first16_hex: entry='4d616e696673742d56657273696f6e' actual='4d616e69666573742d56657273696f6e'
```

(transposed `s`/`f`: `...6e69667374...` vs `...6e69666573...`). The v4 candidate
(`corpus/knowledge/round-69-apk-axml-byte-evidence.md`, sha256
`c1e7eaac9dba4c77e578c788755dec3e3499fd8795ad0e479c51b5be7deb11d5`,
`admission-status: candidate` at `:11` — README not flipped, as §C1 requires) is clean
over all 17 embedded blocks, including `python3 -B corpus/derive_axml_anchors.py` at
`:130` and the full-run readout at `:199`.

Exit-2 paths sampled: no `$ cmd` blocks → `2`; non-`python3` command → `2`. Consistent
with `SKILL.md:279`.

---

## Findings by severity

### F0 — BLOCKING (instrument): the frozen counter cannot reach the C7 block at the round-69 tip

`reports/round-69/measure.py` (sha256 `bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377`,
identical at claims commit `e1d22ca` and at HEAD `35e1258`) executes its Q15 block at
module level at `:151-182`, calling `run(...)` at `:158`, `:163`, `:172`. `def run` is
only at `:187`. Python resolves at call time in a flat script, so the call at `:158`
raises before the definition exists.

Reproduced on a clean archive per the registered invocation contract:

```console
$ git archive HEAD corpus | tar -x -C /tmp/revenger-r69-c7gate/headtree
$ cd / && TMPDIR=/tmp/revenger-r69-c7gate timeout 240 python3 -B \
    /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-69/measure.py /tmp/revenger-r69-c7gate/headtree
HEAD_COUNTER_RC=1
stdout lines: 22
stderr: NameError: name 'run' is not defined   (measure.py:158)
```

Consequences:

- **No `C7_*` label is ever printed at the final tree** — `C7_SELFTEST`,
  `C7_MUTANT_KILLED_ATTRIBUTED`, `C7_V4_CLEAN`, `HOLDS_OK_V5/V6` are all unmeasurable.
  The frozen predicate `C7_V4_CLEAN=yes` (claims §C1) and "the counter's exit code is 0"
  (claims §C1, §C2) cannot hold while the checker ships.
- **No `Q15_*` label except `Q15_PRESENT`** — C2's `Q15_SELFTEST`/`Q15_FALSE_KILLED`/
  `Q15_RESTATE_OK` are likewise unmeasurable.
- The committed red-before receipt is complete (`reports/round-69/measure-before.log`,
  105 lines, `HOLDS_OK_V6=yes`) **only because** `corpus/q15_tree_id_check.py` does not
  exist in the base tree: `git cat-file -e 222a7a7:corpus/q15_tree_id_check.py` → fatal,
  and the receipt itself prints `Q15_SELFTEST=n/a (no checker)` at `:23`. The checker was
  added in the claims commit `e1d22ca` (`git log -- corpus/q15_tree_id_check.py`).
  So the base passes through the HOLD lines and the final tree cannot.

This is not counter drift — the pinned sha matches the defective bytes, so the frozen
artifact itself carries the defect, and it is not repairable without editing the frozen
counter (which claims §"Frozen counter" forbids). Immediate consequence for this seat:
the C7 hold's labels must be verified **directly** through the gate (done above), not
through the counter; and any adjudication that reads `measure-after.log` will find the
run truncated at 22 lines with exit 1.

Notified `L1Revenger69.R69CounterReplay` with the repro.

### F1 — LOW (Q15/D1-class prose): the gate docstring universalises the marker

`corpus/check_embedded_outputs.py:20-23` says the marker "is the last output line of a
failed run". Contradicted by `:133-134` and `:147-148`, which fail without it (Q1 above).
The registry row `SKILL.md:280` states the scoped truth; the docstring does not. Same
class as the round-68 D1 defect (a sentence about the bytes that the named command
contradicts). Fix: scope the sentence to the forged control.

### F2 — LOW (exit contract): an unreadable entry exits 1 with no finding, and a timeout does the same

`evaluate` at `:91` reads the entry with no guard; `main` at `:158-162` only maps
`problems is None` to exit 2:

```console
$ python3 -B corpus/check_embedded_outputs.py --entry /tmp/revenger-r69-c7gate/does-not-exist.md
Traceback (most recent call last):
  ...
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/revenger-r69-c7gate/does-not-exist.md'
MISSING_RC=1
```

Exit 1 with **empty stdout** matches neither registered finding kind at `SKILL.md:279`
("1 = failed (two finding kinds: `drift entry:N …` and `drift entry:N command exited
RC`)"), and the gate's own exit-2 message at `:161` advertises a "read failure" cause that
can never reach that branch. `subprocess.run(..., timeout=120)` at `:78-79` is likewise
uncaught → `TimeoutExpired` → exit 1.

Counter consequence (currently latent behind F0): `measure.py:470-472` computes
`C7_RED_ON_R65_CANDIDATE = rc != 0` with no existence guard on the r65 candidate, so a
tree missing that file would read `yes` from a traceback — a false red, a concrete
instance of the open D5 "counter C7 gameability" item.

### F3 — LOW (pointer): the registry's branch pointer overruns by one line

`SKILL.md:280` cites `corpus/check_embedded_outputs.py:140-146`. The drift branch is
`:140-145`; `:146` is `fproblems, fchecked = evaluate(full_entry, tmp)`, the next statement
outside the branch. D1/M46-class pointer drift; fix to `:140-145`.

### F4 — OPEN D5 confirmed (not a new defect): the two-line partial-drift fixture still does not exist

The self-test's three fixtures are all **single-output-line** blocks (`:122-130`), so a
weakening that compares only the first quoted line survives the self-test. Demonstrated:

- weakened copy (`drift()` → `lines[:1]`): `--self-test` → `SELFTEST OK …`, exit **0**;
- weakened copy against a two-line block whose first line is genuine stdout and second
  line is `BOGUS SECOND LINE`: `checked_blocks=1 problems=0`, exit **0** (drift accepted);
- the committed gate against the same block: `drift entry:4 … BOGUS SECOND LINE`,
  exit **1**.

This is exactly the D5 "two-line partial-drift fixture" gap; claims §Registered leave D5
open and not pre-empted, so it is recorded, not scored against this round.

---

## Residual risk (accepted, documented by the gate)

- The gate executes entry-declared argv as `python3` with no sandbox (`:76-79`); only the
  first token is whitelisted, so `$ python3 -c "…"` in an entry runs arbitrary code.
  Documented as intended ("it runs the entry's declared commands", `:25-27`), and
  candidates are lane-authored/reviewed — low.
- Presence-only semantics: an entry may quote a *subset* of a command's stdout. Documented
  (`:16-18`); partial drift **within** quoted lines is caught (F4 real-gate leg).
- `drift(lines, stdout_set, lineno)` at `:87` takes `lineno` and never uses it — dead
  parameter, cosmetic.

## Verification gaps

- Did not run the counter to completion: impossible at the round-69 tip because of F0
  (reproduced on a clean HEAD archive; exit 1, 22 stdout lines).
- Did not score the C05/Q15 predicates themselves (other seats own those); this seat verified
  only the gate-level facts they rest on — v4 clean (17/17 blocks), r65 red at `entry:41`,
  attribution 1/1 and spoof 0/1.
- Registry pin re-derived: `sha256sum corpus/knowledge/round-65-apk-axml-byte-evidence.md`
  → `cf42cc2059e454027685a59a2a35a190f6ba981f95645f41e407c47c01c4d05a`, matching
  `SKILL.md:281`; expected verdict `exit 1 naming entry:41` holds.

## Tooling

No installs or upgrades were made; all work used the existing `python3` (3.14) and
read-only git. Scratch under `/tmp/revenger-r69-c7gate/` was removed after the review.

---

## Addendum — cross-check with `R69CounterReplay` (post-report)

`R69CounterReplay` independently reproduced F0 and added F5/F6 on the frozen counter.
Re-derived here from the bytes, not taken on report:

**F5 — the D1 fixture is unreachable under the registered invocation.** `measure.py:161`
reads `TREE / "reports/round-69/d1-false-sentence.md"`, but the frozen invocation archives
`corpus` only (`claims.md` §Frozen counter: `git archive <commit> corpus | tar -x`). In a
corpus-only tree `d1.is_file()` is False → `:169` prints `Q15_FALSE_KILLED=n/a (no d1
fixture)` and sets the flag False. C2's predicate `Q15_FALSE_KILLED=yes` therefore cannot
be produced by the invocation that names it. Confirmed statically at `:161-169`.

**F6 — the exit status does not depend on either claim.** `measure.py:577` is
`sys.exit(2 if not evaluable else 0 if holds_ok else 1)`, and `holds_ok` (`:557-559`) is
built only from the C2–C7 fixture controls, `HOLD_REPLAY` and `FRESH_ROWS`. No
`q15_*`, `c05_single_v4`, `c05_status`, `holds_c2_v4` or `c7_v4_clean` term reaches it;
`holds_ok_v6` (`:574-575`) adds the C7 *v3* leg, not v4. Exit 0 is therefore compatible
with every claim label reading `no`/`n/a` — the "counter's exit code is 0" conjunct is
vacuous (D5 kill-rule-closure class). Confirmed statically at `:557-577`.

Ordering: F0 fires first on any checker-present tree, so F5/F6 are only reachable after a
block move. Together: with the pinned counter, C1/C2 are **not evaluable** (not
falsified) — I concur with `R69CounterReplay`'s status.

**Block-count question (v3 = 17, v4 = 17) — consistent, no claim.** The two candidates'
embedded `$ cmd` lists are byte-identical (diff empty; 17 blocks each). The repair bundle
grew output *lines inside* the existing derivation block, not the block count:

| candidate | `derive_axml_anchors.py` block output lines | blocks |
|---|---|---|
| v3 (`round-68-…md`, block at `:128`) | 17 | 17 |
| v4 (`round-69-…md`, block at `:130`) | 20 (= live `python3 -B corpus/derive_axml_anchors.py` output, 20 lines) | 17 |

Matches claims §C1 item 1 ("20 lines") and item 11 (re-embed), with item 8's
`S032`/`S034` source lines landing in the header, not a fence. So `checked_blocks=17` on
both is expected and the gate's clean v4 verdict is unaffected.

### F6 sharpened — the exit status is a function of V1 only, so *every* claim leg is exit-invisible

`R69CounterReplay` reported C1's `C7_V4_CLEAN` as label-only (V6 chains on `c7_v3_clean`
at `:484`, never on `c7_v4_clean` at `:492-493`). Re-derived line by line, the gap is one
level wider: `:577` is `sys.exit(2 if not evaluable else 0 if holds_ok else 1)`, and it
references **`holds_ok` (V1, `:557-559`) only** — `holds_ok_v2`…`holds_ok_v6`
(`:561-575`) are printed and never read by the exit expression. So no V-leg, and a
fortiori no claim label, can change the exit status.

Label → exit wiring, every occurrence of each variable:

| claim label | defined | read by | reaches `:577`? |
|---|---|---|---|
| `C05_SINGLE_V4` | `:79` | `c2_v4_ok` `:123` → print `HOLDS_C2_V4` `:125` | no |
| `C05_STATUS` | `:118` | `c2_v3_ok`/`c2_v4_ok` `:120`,`:124` | no |
| `HOLDS_C2_V4` | `:125` | nothing | no |
| `C7_V4_CLEAN` (`c7_v4_clean`) | `:492` | print `:493` only | no |
| `C7_V3_CLEAN` (`c7_v3_clean`) | `:484` | `holds_ok_v6` `:574` | no (V6 not in `:577`) |
| `Q15_PRESENT` (`q15_present`) | `:153` | print `:155` only | no |
| `Q15_SELFTEST` (`q15_selftest`) | `:159` | print `:160` only | no |
| `Q15_FALSE_KILLED` (`q15_false_killed`) | `:165` | print `:166` / else `:168` | no |
| `Q15_RESTATE_OK` (`q15_restate`) | `:174` | print `:175` / else `:177` | no |

`evaluable = False` is set only in the C2–C7 mutation could-not-evaluate branches
(`:221`, `:272`, `:311`, `:355`, `:407`, `:459`, `:529`, `:534`), so exit 2 is
unreachable for any claim-leg condition as well. The one claim-adjacent leg that *is*
wired — `mismatch` (README token legend) into `holds_ok_v2` `:564` — terminates in V2,
which is itself not read at `:577`.

Empirical witness (base archive `222a7a7`, checker absent so F0 does not fire, with only
`corpus/knowledge/round-68-apk-axml-byte-evidence.md` removed):

```console
$ git archive 222a7a7 corpus | tar -x -C /tmp/r69c7-base
$ rm /tmp/r69c7-base/corpus/knowledge/round-68-apk-axml-byte-evidence.md
$ cd / && TMPDIR=/tmp/r69c7-base python3 -B reports/round-69/measure.py /tmp/r69c7-base; echo RC=$?
C7_V3_CLEAN=n/a (no v3 file)
C7_MUTANT_KILLED_ATTRIBUTED=1/1
HOLD_REPLAY=10/10
HOLDS_OK=yes
HOLDS_OK_V2=yes
HOLDS_OK_V3=yes
HOLDS_OK_V4=yes
HOLDS_OK_V5=yes
HOLDS_OK_V6=no
RC=0
```

A failing V6/C7 leg still exits 0. Combined with F0/F5 this makes the claims' "the
counter's exit code is 0" conjunct vacuous three ways over: the block never executes
(F0), the fixture is unarchived (F5), and the exit expression ignores every claim and
V2–V6 term (F6). Repair order must be block-move → archive widening → exit-chain wiring,
then re-verified on a checker-present tree; the registration-time red-before on that same
tree is the control that catches all three.

### F6 inheritance — the unwired exit is not a round-69 regression

The same V1-only exit expression exists in every prior round of this counter, so the C7
gate has never moved the exit status since it was registered:

| round | counter | exit line | aggregate wired |
|---|---|---|---|
| 67 | `reports/round-67/measure.py` @ `d00f779` | `:455` `sys.exit(2 if not evaluable else 0 if holds_ok else 1)` | `holds_ok` `:439` |
| 68 | `reports/round-68/measure.py` @ `d00f779`, sha256 `0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766` (matches its claims pin) | `:528` same expression | `holds_ok` `:508`; `holds_ok_v5` `:523`; `holds_ok_v6` `:525` — C7 v3/neg legs unwired |
| 69 | `reports/round-69/measure.py`, sha256 `bca74e6d…` | `:577` same expression | `holds_ok` `:557-559`; `holds_ok_v6` `:574-575` |

**The round-68 receipt's prose.** `reports/round-68/measure-after.log:108` reads:

> `counter exit code: 0 (the V1 holds hold; every V-label is yes)`

Precision, since the difference matters for the finding's severity: the parenthetical's
*observation* is true of that run — `:93-98` show `HOLDS_OK` through `HOLDS_OK_V6` all
`yes`. What the code refutes is the **entailment** the receipt line presents: exit 0 does
not carry the V-labels, because exit 0 is emitted with `HOLDS_OK_V6=no` (witness in §F6
sharpened). Read as certification — which is how a receipt line is read — it is a meaning
asserted against contradicting bytes, the D1 class; Q15 does not reach it because Q15
verifies git object ids, not the semantics of a mechanical signal.

**Repair consequence.** `R69CounterReplay`'s F7 item 3 is the right shape:
`sys.exit(2 if not evaluable else 0 if holds_ok_v7 else 1)`. Two conditions on it:

1. The exit expression itself must name the terminal hold — a `holds_ok_v7` that `:577`
   does not read would simply become the seventh unread label.
2. The wiring needs its own falsification control, or it is itself unverified: a temp tree
   in which one claim label is forced to its failing value (e.g. `C05_SINGLE_V4=no` by a
   README C05 row naming two entries, with `HOLDS_OK`/`HOLD_REPLAY`/`FRESH_ROWS` left
   green) must exit non-zero. Without that leg the repaired chain is a label with a new
   name.

Because the v7 leg must include `c7_v4_clean`, C1's `C7_V4_CLEAN=yes` becomes
exit-relevant for the first time; the round-69 gate facts verified in this report (v4
clean, 17/17 blocks) are therefore directly usable as that leg's expected value once the
counter is repinned.
