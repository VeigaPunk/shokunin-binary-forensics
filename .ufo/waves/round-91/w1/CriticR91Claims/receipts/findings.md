# CriticR91Claims — findings (round 91, attempt 1)

Seat: critic. Read-only over the lane. Every command below was run from
`/home/vgpnk/Projects/shokunin/revenger-shokunin` (the lane root) unless a
different `cd` is shown. Controls and their logs are in this directory
(`receipts/`), so each finding is reproducible after the seat scratch dir is
deleted. Nothing in the frozen set (`claims.md`, `sm6_battery_v3.py`,
`mutants.py`, `c1_counter.py`, `cap_probe.py`) was edited.

Scratch used: `$HYAKU_SCRATCH/revenger-r91/CriticR91Claims` (deleted at exit).
Fixture repos were created with `git clone`/`git init` under that scratch and
every later git call named `-C <fixture>`; no mutating git/jj command was run
in the lane.

Note on the assignment's "§9 of the round contract": no local document carries
a numbered §9 (checked `templates/round-prompt.md` — sections 1, 2, 2b, 3, 4, 5;
`MISSION.md` — 7 sections; `AXES.md`, `templates/agents/ufo-critic.md`,
`templates/agents/ADAPTATION.md` — unnumbered). I therefore attacked the four
criteria named in the assignment itself: control reachability, axis naming,
freeze order, fitting. This is a provenance gap in the assignment, not a lane
defect.

---

## C1 — calibration (SM6 v3 reads the stated cell)

### C1-1 [BLOCKING] The C1 target is reachable by a fitted implementation that never reads the stated cell

**Claim:** `claims.md` §C1 — `corpus/self_assessment_check3.py` must read the
K statement in the stated before→after cell; the predicate is
`SM6_MISCLASS=0/22` + `MUTANTS_KILLED=11/11` + self-test exit 0 +
`REAL_SELF_MISMATCH=0`, one command, exit 0 iff all four hold. The frozen
do-nothing control is "v2 itself"; claims.md adds "A control that meets the
target means the battery or target is wrong; then no data is collected."

**Control built:** `receipts/impl_fit_hardcoded.py` — a 21-entry table keyed on
`(map rows, held count, raw K line text)`, returning the frozen battery's own
hand label; no region split, no arrow handling, no token adjacency, no
`K_HELD_BACKED_STRICT` truncation. Its `--self-test` prints `SELFTEST OK` and
its run leg prints `SELF_MISMATCH=0` unconditionally. (An earlier import-based
variant, `impl_fit.py`, scored the same; the hard-coded one has no dependency
on the battery file.)

**Command:**
```
PYTHONUTF8=1 python3 -B reports/round-91/c1_counter.py \
  --impl .ufo/waves/round-91/w1/CriticR91Claims/receipts/impl_fit_hardcoded.py \
  --real . --lane .
```

**Observed output** (`receipts/c1-fit-hardcoded.log`, exit 0):
```
SM6_MISCLASS=0/22
MUTANTS_KILLED=11/11
IMPL_SELFTEST exit=0 last=SELFTEST OK
REAL_SELF_MISMATCH=0 exit=0
C1_VERDICT=pass
```

**Why this is a defect and not a trade:** the battery is a fixed 21-case lookup
surface; the counter never evaluates the impl on a case generated at run time.
The mutant leg is independent of `--impl` (`c1_counter.py` scores
`mutants.MUTANTS` against the battery, never against the impl), and the
self-test leg only checks an exit code. So the three legs that could have
discriminated an impl are not coupled to the impl at all; only the 21 fixed
cases are, and they are enumerable.

**Impacted axis:** calibration (the counter certifies conformance to a case
table, not that the gate reads the stated cell). The claim's own kill rule
("a control that meets the target means the battery or target is wrong") is
triggered by this control.

**Smallest safe correction:** add one case to the battery leg that is generated
from a run-time seed (random row/held counts and a randomly true-or-false
statement in the lane's row shape), or have the counter compare `--impl`'s
`sm6` against `mutants.reference` on randomized inputs. If the frozen files
cannot change, the round must report C1 as "conforms to the frozen 21-case
battery (which admits fitting)" and must not claim the rule is verified.

### C1-2 [non-blocking — claim survives] The hard-coded `8/15` control is killed

**Control built:** `receipts/impl_hard815.py` — reads the stated region's last
`N/D` but compares it to the constant `(8,15)` instead of the README counts.

**Command:** `c1_counter.py --impl receipts/impl_hard815.py --real . --lane .`
(`receipts/c1-hard815.log`, exit 1):
```
CASE B06 label=0 got=1 MISCLASS
CASE B07 label=1 got=0 MISCLASS
CASE B10 label=0 got=1 MISCLASS
CASE B12 label=1 got=0 MISCLASS
CASE R02 label=0 got=1 MISCLASS
CASE R09 label=0 got=1 MISCLASS
SM6_MISCLASS=6/22
C1_VERDICT=fail
```
The battery does discriminate against this specific hard-code (rows/held are
varied: 15/8, 14/8, 15/7, 16/9, 14/6). This attack does not reach the target.

### C1-3 [BLOCKING until landed; now unblocked by an undeclared edit] The real leg is a whole-tree property; the v3 file itself trips SM2

**Claim:** §C1 predicate requires `REAL_SELF_MISMATCH=0` from
`--root <TREE> --lane <LANE>`; `claims.md` declares no edit outside
`corpus/self_assessment_check3.py` ("v2 bytes stay unchanged").

**Probe built:** a fresh clone of HEAD with and without the untracked v3 file.

**Command/output** (`receipts/c1-real-leg-tree-dependence.log`, fixture
`git clone --no-hardlinks . $S/wt3`, toplevel asserted `$S/wt3`):
```
== clone of HEAD d509e98 (README at HEAD has no v3 index line; no untracked files)
SM5=0 / SM6=0 / SELF_MISMATCH=0
== same clone + untracked corpus/self_assessment_check3.py
SM5=0 / SM6=0 / SELF_MISMATCH=1
== v3 on the same clone (v3 present, README unindexed)
SM5=0 / SM6=0 / SELF_MISMATCH=1
== v3 on the same clone + README index line
SM5=0 / SM6=0 / SELF_MISMATCH=0
```
At 19:44 the live counter on v3 was red for exactly this reason
(`receipts/c1-v3-now.log`: `SM6_MISCLASS=0/22`, `REAL_SELF_MISMATCH=1`,
`C1_VERDICT=fail`) and v2's frozen red also flipped
(`receipts/c1-v2-now.log`: `SM6_MISCLASS=5/22`, `REAL_SELF_MISMATCH=1`,
`C1_VERDICT=fail`). A sibling has since edited `corpus/README.md` to index
`self_assessment_check3.py` (uncommitted at the time of writing:
`git status --porcelain corpus/README.md` → ` M corpus/README.md`; the diff adds
one bullet for `self_assessment_check3.py`), after which v3 passes
(`receipts/c1-v3-recheck.log`: `SM6_MISCLASS=0/22`, `REAL_SELF_MISMATCH=0`,
`C1_VERDICT=pass`) and v2's red reproduces (`receipts/c1-v2-recheck.log`:
`SM6_MISCLASS=5/22`, `REAL_SELF_MISMATCH=0`, `C1_VERDICT=fail`).

**Defect:** the C1 verdict is coupled to `corpus/README.md` indexing (SM2), a
file the claim never names; the pass depends on a lane edit outside the claim's
declared surface. The edit is legitimate and required, but it must be declared
in the round's landing (and it means C1's "what moves" is not only the SM6
rule).

**Impacted axis:** calibration (the real leg measures all six classes, not the
claimed SM6).

**Smallest safe correction:** declare the README index line as part of C1's
landing, and pin `--real` to the landing commit's `git archive` (the lane's own
r90 practice: "over `git archive <tip>`"), not the mutable worktree.

### C1-4 [non-blocking, material] The real leg is unpinned; the "before" receipt is environment-dependent

**Command/output** (`receipts/c1-red-on-archive.log`; a `git archive f6356ff`
tree, no `.git`, no untracked files):
```
SM1=0 SM2=0 SM3=0 SM4=0 SM5=34 SM6=0
SELF_MISMATCH=34
```
SM5 resolves cited commit ids with `git -C <lane> cat-file` (`sm5` in
`corpus/self_assessment_check2.py:39-64`), so on an archive without `.git` it
reports 34. Conversely, in the live worktree the same v2 run reported
`REAL_SELF_MISMATCH=0` at the freeze, `1` while v3 was untracked, and `0` again
after the README edit (`receipts/c1-v2-now.log`, `c1-v2-recheck.log`); v1 moved
`1` (frozen log) → `2` in the same window. The frozen receipt
`reports/round-91/c1-red-v2.log` line `REAL_SELF_MISMATCH=0 exit=0` is therefore
a property of the tree state, not of v2.

**Impacted axis:** calibration / freshness of the measurement. **Correction:**
pin the tree for the real leg and state which tree the red receipt used.

### C1-5 [non-blocking] R01/R02 are not "verbatim SCORECARD lines"

**Claim:** `sm6_battery_v3.py` docstring — "R01 and R02 are the verbatim
SCORECARD lines 693 and 667 of the freeze base".

**Command/output** (`receipts/battery-r01-r02-provenance.log`):
```
R01 byte-identical-to-SCORECARD:693/667 = False
R02 byte-identical-to-SCORECARD:693/667 = False
```
R01 drops the verdict-cell tail `; the round-73 C10 claim is now
falsified-closed, not carried`; R02 truncates the **stated cell** after
`` `C15_HELD_BACKED` 0/1 → 0/1 `` and omits `` `C15_TOOL_ROWS` 0/18 → 18/18; C15
`uncovered` → `uncovered` ``. The battery is a paraphrase of the lane's row
shape, not the row. The stated-cell truncation is exactly where a second `N/D`
group lives, so the case does not test the frozen rule on the lane's real
stated cell. **Correction:** quote byte-exactly or label the cases "truncated".

### C1-6 [non-blocking, disclosed] Axis name: calibration is contested and the round says so

**Evidence:** `SCORECARD.md:1659` (round-90 C1 row) is labelled
"calibration — SM6 gate fidelity" and records "**MET on the frozen counter;
admission contested.** CriticR90Claims: … the move is gate fidelity rather than
self-assessment accuracy (operability or a calibration sub-axis)". The r90
counterexample receipt the claim cites is
`.ufo/waves/round-90/w1/CriticR90Claims/receipts/c1-realformat-counterexample.log`
and it demonstrates the defect only on **mutated** rows (`CX
stated-after-cell-false-9/15`, `CX stated-after-cell-false-8/14`); on the
committed row (line 693) v2 reads `SM6=0`, i.e. correctly
(`receipts/c1-v2-recheck.log`: `REAL_SELF_MISMATCH=0`, `SM6=0`). `AXES.md`
defines calibration as "SHONEN.md/SCORECARD entries match observed repo state",
which fits SM6 by definition, so the label is defensible — but the claimed
defect has no real committed instance; it is a constructed counterexample.
`claims.md` discloses the contested-label caveat, so this is a disclosed
tradeoff, not a hidden one. **Correction:** say in the row that the defect is
demonstrated on authored variants, and that the committed row is read
correctly by v2.

### C1-7 [minor, frozen-artifact inconsistency] Counter docstring vs behaviour

`reports/round-91/c1_counter.py:13` documents leg 1 as `SM6_MISCLASS=0/21`,
while the frozen claims and the actual output are `0/22` (21 battery cases + the
real-tree leg). Doc/behaviour mismatch inside a frozen artifact; no data
depends on it.

### C1-8 [non-blocking] Freeze order holds for the C1 artefacts (as committed)

`git log --oneline b13aac7..HEAD -- reports/round-91/` and
`git diff --stat b13aac7 HEAD -- reports/round-91/` are both empty: the frozen
battery/mutants/counter/claims bytes are unchanged since the freeze commit.
`stat`: battery 19:36:23, freeze commit 19:37:23, v3 19:42:09 — labels precede
the implementation. The only post-freeze change to C1's measurement surface is
the README index edit (C1-3), which is not in the claim.

### C1-9 [BLOCKING for the freeze invariant] The frozen claims file was edited after data existed

**Claim:** `claims.md` header — "Nothing in this file changes after the freeze;
a miss is an honest stop, never a narrowed target."

**Observed** (`git status --porcelain reports/round-91/claims.md` → ` M`;
`git diff reports/round-91/claims.md`, uncommitted at review time): an appended
section `## Erratum (appended after data, 2026-11-04; predicate, counter, kill
rule and target unchanged)` with two bullets. The first re-reads C2 after the
data ("The claim is read as 'the lane can measure commit-message↔tree
conformance'") and says a closure that reads the frozen description as binding
"will find the claim not verified"; the second records that a SCORECARD prose
line won SM6's last-line slot and "scored SM6=1 until it was reworded".

The predicate *text* is unchanged, but the frozen file itself now carries a
post-data reinterpretation of the claim and a disclosure that the measured data
was reworded. That is a change to the frozen artifact the round declared
immutable; the lane's own r89 precedent appends errata to `LOG.md`/`SCORECARD.md`,
not to the frozen claims file. As of review the edit is uncommitted, so it is
also undeclared to any committed receipt.

**Impacted axis:** calibration / freeze order. **Smallest safe correction:**
move the erratum to `SCORECARD.md`/`LOG.md` (append-only, as r89 did) and leave
`reports/round-91/claims.md` byte-identical to `b13aac7`; state the C2
description defect in the round report with the `cited=8` measurement.

### C1-10 [material, disclosed in the erratum] The real-tree SM6=0 depends on rewording the lane's own SCORECARD text to fit the gate

The erratum states that a round-91 SCORECARD prose sentence naming
`K_HELD_BACKED` occupied the rule's "last line" slot and scored SM6=1 "until it
was reworded"; the current section instead writes "K (8 of 15)" in prose and
keeps `K_HELD_BACKED` only in the table row (`SCORECARD.md:1695`, which the rule
reads as cell 2). So the green real leg was obtained by editing the measured
text, not by the gate handling the lane's writing; the gate's blind spot is
named and routed to r92. This is data-fitting in the weak sense — disclosed,
but it means the `REAL_SELF_MISMATCH=0` receipt is a property of a reworded
tree. **Correction:** keep the truthful prose and route the gate fix, or pin
the real leg to the freeze-base archive (where the row is the only K line) and
report the landing tree's SM6 separately.

---

## C2 — operability / capability acquisition (message↔tree conformance)

### C2-1 [BLOCKING] The frozen extraction rule cannot satisfy the frozen probe

**Claim:** §C2 — the instrument "extracts every **backticked** repo-relative
path and every `.log` filename cited in each commit message"; the counter's
leg 4 requires a real run with `commits≥20` and `cited≥20`.

**Control built:** `receipts/spec_extract.py` — the frozen rule implemented
literally (backticked tokens that look like paths + every `.log` token; bare
names resolve by unique suffix), with a `--selftest` pass line added in the
probe copy.

**Command:**
```
python3 -B receipts/spec_extract.py . 7fab03f..refs/heads/main
```
**Observed** (`receipts/spec-extract-real.log`, exit 1):
```
MESSAGE_TREE commits=23 cited=8 misses=1
```
`receipts/probe-spec-conformant.log` (same file installed as
`message_tree_check.py` in a copy of the probe dir):
```
CAP_SELFTEST=pass exit=0
CAP_PLANTED_MISS=pass clean_exit=0 dirty_exit=1
CAP_REAL=fail commits=23 cited=8 misses=1 exit=1
LEGS present=pass selftest=pass planted=pass real=fail
CAP_MESSAGE_TREE=fail
```
There are **zero backticked tokens in any of the 23 commit messages**
(`git log --format=%B 7fab03f..main | grep -c '`'` → 0); the 8 spec-visible
citations are all `.log` names in three commits (5f7ecce, 6ce41aa, 45b2713).
`cited=8 < 20` ⇒ leg 4 fails by construction.

The landed instrument passes (`receipts/probe-landed.log`:
`CAP_REAL=pass commits=23 cited=25 misses=9 exit=1`) only because it extracts
**prose** paths as well as backticked ones — an extraction rule the claim never
froze. Its own docstring states the broader rule. Note also that the claim's
grounding (`considerthese/2026-11-04.md` proposal 4) says "extract file paths
and `.log` names", not "backticked file paths"; the claim narrowed its own
grounding, and the narrowed rule is the one that cannot pass.

**Impacted axis:** operability (the frozen predicate's meaning changed after
the freeze: the claim text and the passing instrument disagree).

**Smallest safe correction:** restate the extraction rule in the claim to the
one the instrument implements (prose + backticked paths, `path:line` stripped,
explicit directories), and record that the frozen backticked-only rule scores
`cited=8`, i.e. below the probe's own floor. Without that, C2's pass is a
predicate change made after the freeze.

### C2-2 [BLOCKING] The probe is satisfiable with no commit-tree membership check at all

**Claim:** §C2 leg 3 — "the instrument must exit 1 on the two-commit range and
name `missing/r91.txt`"; the claim's do-nothing control says a stub that
"prints `MSG_TREE_SELFTEST=pass` and a plausible summary line" dies at leg 3.

**Control built:** `receipts/stubD.py` — reuses the landed instrument's
tokenizer but performs **no tree lookup and no filesystem lookup**. It flags a
cited path only when the literal substring `missing` appears in it (the probe's
own spelling), and on any range longer than 3 commits it prints `misses=99`
and exits 1.

**Command:**
```
cd <probe-copy with stubD as message_tree_check.py>
HYAKU_SCRATCH=$S python3 -B cap_probe.py --lane <LANE> --range 7fab03f..refs/heads/main
```
**Observed** (`receipts/probe-stubD.log`, exit 0):
```
CAP_SELFTEST=pass exit=0
CAP_PLANTED_MISS=pass clean_exit=0 dirty_exit=1
CAP_REAL=pass commits=23 cited=25 misses=99 exit=1
LEGS present=pass selftest=pass planted=pass real=pass
CAP_MESSAGE_TREE=pass
```
Two holes combine: (a) the planted path is self-identifying (`missing/r91.txt`
— the same literal the instrument's own selftest plants at
`reports/round-91/message_tree_check.py:231,248`), so a name check passes legs
2 and 3; (b) leg 4 ignores the real run's exit code and its `misses` value, so
a control that reports `misses=99 exit=1` still passes. A control that always
passes (`receipts/stubA.py`) *is* killed — `CAP_PLANTED_MISS=fail`
(`receipts/probe-stubA.log`) — but that is the weakest possible stub.

**Impacted axis:** operability (control reachability).

**Smallest safe correction:** plant an ordinary-looking absent path (e.g.
`reports/round-91/absent-receipt.log`), and require leg 4 to be self-consistent
(exit 0 iff `misses==0`) and to cross-check `commits` against
`git rev-list --count`.

### C2-3 [BLOCKING] The probe cannot distinguish commit-tree checking from worktree checking

**Claim:** §C2 — each citation is checked "against that commit's own tree
(`git cat-file -e <c>:<path>`)".

**Control built:** `receipts/stubE.py` — same tokenizer, but resolution is
`Path(lane, path).exists()` plus a `git ls-files --cached --others` suffix
search; no `cat-file -e <c>:<path>` anywhere.

**Command:** same probe invocation with `stubE.py` installed.
**Observed** (`receipts/probe-stubE.log`, exit 0):
```
CAP_PLANTED_MISS=pass clean_exit=0 dirty_exit=1
CAP_REAL=pass commits=23 cited=25 misses=1 exit=1
CAP_MESSAGE_TREE=pass
```
The worktree checker reports `misses=1`, the landed instrument `misses=9`. The
probe's fixture has no history where the worktree and a commit tree differ
(all three commits are the fixture tip), so both pass; the measured quantity is
not identified by the probe.

**Impacted axis:** operability. **Smallest safe correction:** make the planted
fixture contain a commit whose cited path exists in the worktree but not in
that commit (add the file after the citing commit), and require the instrument
to flag it.

### C2-4 [BLOCKING for the predicate as written] Leg 4 ignores exit code and K; the lane's own history is non-conformant

**Command/output** (`receipts/probe-landed.log` and
`receipts/msg-tree-real.log`):
```
MESSAGE_TREE commits=23 cited=25 misses=9        (instrument exit 1)
CAP_REAL=pass commits=23 cited=25 misses=9 exit=1
CAP_MESSAGE_TREE=pass
```
`claims.md` §C2 says the instrument exits 0 iff K=0; the probe's leg 4 only
requires `commits≥20` and `cited≥20`, so `CAP_MESSAGE_TREE=pass` is printed
while the instrument reports 9 misses and exit 1. The capability claim is
"measurable", which the numbers do support, but the predicate as written cannot
distinguish a working instrument from one that always fails, and the round does
not disclose K=9 for the declared range.

**Correction:** require the real leg's exit code to be consistent with K
(exit 0 iff K==0), or print and pin K in the claim. Do not report "pass" as if
the lane's history conforms.

### C2-5 [material] 8 of 9 measured misses are ambiguity false positives; the multi-match rule was chosen after the freeze

**Control built:** `receipts/classify_misses.py` — for each miss printed by the
instrument, count suffix matches of that name in the commit's own tree.

**Command/output** (`receipts/miss-classification-real.log`):
```
b13aac7 claims.md suffix_matches=30 AMBIGUOUS
b280719 w1-results.json suffix_matches=4 AMBIGUOUS
e0fbf2e truth.json suffix_matches=53 AMBIGUOUS
6ce41aa inspection.json suffix_matches=31 AMBIGUOUS
6ce41aa receipt.json suffix_matches=21 AMBIGUOUS
6ce41aa LEDGER.md suffix_matches=72 AMBIGUOUS
45b2713 c1-only.log suffix_matches=11 AMBIGUOUS
45b2713 noharm-diff.txt suffix_matches=13 AMBIGUOUS
d509e98 ufo-wave-policy.json suffix_matches=0 TRUE-MISS
CLASSIFY ambiguous=8 true_miss=1 total=9
```
Concrete false positive: `b13aac7` cites `claims.md` in the message and adds
`reports/round-91/claims.md` in that same commit (`git cat-file -e
b13aac7:reports/round-91/claims.md` succeeds), yet the instrument reports it
missing because 30 files share the name. The frozen claim says only that bare
filenames "resolve by suffix match"; the multi-match → `miss` decision is an
implementation choice made after the freeze, and it is what moves K from 1 to
9. The same pattern dominates the r80–r88 window
(`receipts/miss-classification-r80-88.log`: `ambiguous=14 true_miss=5`).

**Correction:** declare multi-match semantics (ambiguous ⇒ `bare`, not `miss`),
or resolve against the cited round's directory; report K=1 (the true miss) and
name it.

### C2-6 [material] The claim's grounding "seven of nine rounds r80–r88" is not reproduced

**Command:** instrument over `f21e0d5..45b2713` (round-80 freeze through
round-88 adjudication), then group by round in the subject:
```
MESSAGE_TREE commits=48 cited=66 misses=19
80 commits 4 with_miss 0
81 commits 5 with_miss 0
82 commits 5 with_miss 0
83 commits 5 with_miss 1
84 commits 7 with_miss 1
85 commits 8 with_miss 4
86 commits 6 with_miss 2
87 commits 4 with_miss 3
88 commits 4 with_miss 1
```
6 of 9 rounds, not 7; and 14 of the 19 misses are ambiguity false positives
(C2-5). `considerthese/2026-11-04.md:36` itself says the number is "read off
prose"; the round repeats it as grounding without reproducing it with the
instrument it builds. **Correction:** cite the reproduced count (6/9, or 1/9
true misses) or drop the number.

### C2-7 [non-blocking] Axis name: operability is valid by `AXES.md`, but not a scoring axis in this lane's SCORECARD

`AXES.md` defines operability as "Runnable artifacts: checklists that are
executable, commands that exist, scripts that run … produces the stated
outcome", which fits a new instrument; the claim declares capability
acquisition, which `AXES.md` allows with a per-axis verdict. But
`SCORECARD.md:3` says "Active mission axes: coverage + calibration" and
`SCORECARD.md:84` still records "operability — not an assigned scoring axis";
later round tables track "depth / operability / adjacency … unchanged". The
round should therefore enter a `capabilities:` row (claims says it will) and not
an operability score. No defect if that is what lands.

---

## Disclosure update (read after the findings above)

While this seat ran, the landing seats wrote an uncommitted `SCORECARD.md`
round-91 section and the `claims.md` erratum. Their disclosures overlap some
findings and must be scored honestly:

| finding | status after the landing drafts |
|---|---|
| C1-1 fitted table | **undisclosed**; the SCORECARD row discloses only "6 of 17 attributed implementation mutants survive … eight rule elements have no discriminating case" (MutR91Sm6), which is a different defect |
| C1-3 README index | **disclosed** in the SCORECARD row: "`REAL_SELF_MISMATCH` 1 → 0 (the 1 was the new file's missing `corpus/README.md` index line, fixed in the same landing)" |
| C1-10 SCORECARD rewording | **disclosed** in the claims erratum and routed to r92 |
| C1-9 claims.md edit | **not disclosed as a freeze violation**; the SCORECARD says claims are "unchanged since the freeze except one appended `## Erratum`" |
| C2-1 backticked rule | **disclosed** in the erratum (attributed to `ReviewerR91C2.md` H1) — but the disclosure is itself the post-freeze edit of C1-9 |
| C2-5 ambiguity | **disclosed** in the SCORECARD row ("1 genuine mismatch, 8 ambiguous bare names") and routed to r92 |
| C2-2/C2-3/C2-4 probe holes | **undisclosed** |
| C1-4 unpinned real leg, C1-5 "verbatim" rows | **undisclosed** |

## Summary

- Findings: **17** (C1: 10; C2: 7).
- Blocking as written: **C1-1, C1-9, C2-1, C2-2, C2-3, C2-4**. C1-3 was
  blocking until the README index edit landed (now disclosed); C2-1 is
  disclosed only by the post-freeze erratum that C1-9 objects to.
- Material but not blocking: C1-4, C1-5, C1-10, C2-5, C2-6.
  Disclosed/minor: C1-6, C1-7, C1-8, C2-7.
- Two strongest:
  1. **C1-1** — a 21-entry lookup table passes the frozen C1 counter
     (`C1_VERDICT=pass`), so the predicate cannot certify that the gate reads
     the stated cell; the claim's own do-nothing rule is triggered.
  2. **C2-2** — a stub with no tree check and no filesystem check passes
     `CAP_MESSAGE_TREE=pass` (planted miss caught by the literal `missing`,
     real range reported as `misses=99 exit=1`), so the probe certifies
     neither tree membership nor the real range's conformance.
- Findings I could not reproduce: none of the above; the claim's "seven of nine
  rounds" figure and the "verbatim" battery rows are the two claims that did
  not reproduce (C2-6, C1-5), and the §9 numbering itself (see header).
