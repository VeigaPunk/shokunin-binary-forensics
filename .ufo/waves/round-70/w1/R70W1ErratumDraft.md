DRAFT-READY — SM5 reproduced (`SCORECARD.md:557` cites `e1d22caf`, which does not resolve; the round-69 pre-registration commit is `e1d22caaf9a2fdc4c1c13d1f4a8a6813e7b07968`), the exact appended erratum line is written and verified `SM5=1 -> 0` on the pinned candidate tree, the V3/V4 corrections are drafted as appended prose with their reproductions, and the 18-row claim hit-rate ledger for rounds 61-69 is derived by command (`met=10 falsified=2 honest-stop=5 pending=1`).

Seat: R70W1ErratumDraft (scribe / C2 repair draft). Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
All numbers below are computed from the **pinned** commit `aa1842fac199aa524930e5565ed3715de5f84c6d`
(`git archive aa1842fa corpus SHONEN.md SCORECARD.md SKILL.md`), never from the live working tree, because the
working tree changed under me during this wave (see Findings F1/F2). No lane file was edited. Tool installs: none.

---

## Part 1 — SM5 reproduction and the exact erratum line

### 1.1 Reproduce SM5=1 on the pinned candidate bytes

```
$ D=/tmp/revenger-r70-R70W1ErratumDraft-pin
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive aa1842fac199aa524930e5565ed3715de5f84c6d \
    corpus SHONEN.md SCORECARD.md SKILL.md | tar -x -C "$D"
$ cd "$D" && PYTHONDONTWRITEBYTECODE=1 python3 -B corpus/self_assessment_check.py --root . \
    --lane /home/vgpnk/Projects/shokunin/revenger-shokunin
SM1=1
SM2=7
SM3=2
SM4=1
SM5=1
SM6=0
SELF_MISMATCH=12
exit=1
```

Checker bytes under test (pinned, = `aa1842fa:corpus/self_assessment_check.py`):
`sha256 6a24baa158ec168e3d4315d91c8a9e35481976c065bb8323b5a61f4b665c90fb`.

### 1.2 Which token, which line

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && grep -n "e1d22caf" SCORECARD.md
557:Pre-registration `e1d22caf` (claims + frozen counter `reports/round-69/measure.py` sha256
$ grep -c "e1d22caf" SCORECARD.md
1
$ git cat-file -e e1d22caf^{commit}
fatal: Not a valid object name e1d22caf^{commit}      (exit 128)
```

One cited token, one mismatch: `SCORECARD.md:557`, inside `## Round 69 (hyaku run 6)` (section starts at
`SCORECARD.md:555`, i.e. after the checker's `## Round 61` scan start at `:187`).

### 1.3 The correct full hash, and why it is that commit

```
$ git log --format='%H %ad %s' --date=short --diff-filter=A -- reports/round-69/claims.md
e1d22caaf9a2fdc4c1c13d1f4a8a6813e7b07968 2026-10-25 round-69: pre-registration — claims (C1 C05 v4 re-gate with full routed repair bundle, C2 Q15 tree-identity criterion), frozen counter measure.py, Q15 checker, red-before receipt
$ git show --stat --oneline e1d22caaf9a2fdc4c1c13d1f4a8a6813e7b07968
e1d22ca round-69: pre-registration — claims … frozen counter measure.py, Q15 checker, red-before receipt
 corpus/q15_tree_id_check.py   | 129 ++++++++
 reports/round-69/claims.md    | 231 ++++++++++++++
 reports/round-69/d1-false-sentence.md |  12 +
 reports/round-69/measure-before.log   | 105 +++++++
 reports/round-69/measure.py   | 577 ++++++++++++++++++++++
$ git show e1d22caaf9a2fdc4c1c13d1f4a8a6813e7b07968:reports/round-69/measure.py | sha256sum
bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377  -
$ git cat-file -e e1d22caaf9a2fdc4c1c13d1f4a8a6813e7b07968^{commit} && echo full_resolves=yes
full_resolves=yes
```

The identity is not just "the 8-char prefix resolves to something": `e1d22caa` is the commit that adds
`reports/round-69/claims.md` **and** carries the round-69 counter whose sha256 (`bca74e6d…`) is exactly the digest
`SCORECARD.md:558` states for it, plus the red-before log `:559` names. The citation's referent is therefore the
full hash above, not any other commit sharing the prefix. (`git rev-parse e1d22ca` resolves; `e1d22caf` does not —
the SCORECARD token is an 8-char truncation of a hash whose 8th char is `a`, not `f`.)

### 1.4 The erratum line to append (exact bytes, column 0)

Append to `SCORECARD.md` as its own line, **at column 0**, no indent, ASCII `->` with one space each side,
each hash backticked:

```
erratum: `e1d22caf` -> `e1d22caaf9a2fdc4c1c13d1f4a8a6813e7b07968`
```

Byte check (`od -c`): `e r r a t u m :   ` e 1 d 2 2 c a f `   - >   ` e 1 d 2 2 c a a f 9 a 2 f d c 4 c 1
c 1 3 d 1 f 4 a 8 a 6 8 1 3 e 7 b 0 7 9 6 8 ` \n`.

### 1.5 Verification of the erratum (three variants, scratch copies only)

```
$ for v in good note wronggood; do  # each = fresh copy of the pinned tree + one appended line
    good      : erratum: `e1d22caf` -> `e1d22caaf9a2fdc4c1c13d1f4a8a6813e7b07968`
    note      : erratum: `e1d22caf` -> `e1d22caaf9a2fdc4c1c13d1f4a8a6813e7b07968` (round-69 pre-registration commit; V2)
    wronggood : erratum: `e1d22caf` -> `deadbeef`
  done
good      :: SM5=0 SELF_MISMATCH=11
note      :: SM5=0 SELF_MISMATCH=11
wronggood :: SM5=1 SELF_MISMATCH=12
```

So the repair moves SM5 `1 -> 0` and total `12 -> 11` on the candidate bytes, a trailing parenthetical after the
good hash is tolerated (the checker's regex is `^erratum: \`([0-9a-f]{7,40})\` -> \`([0-9a-f]{7,40})\`` with no
end anchor), and a non-resolving `good` does **not** excuse the bad token — the erratum cannot be gamed.

Placement safety (why EOF is safe):
- `corpus/self_assessment_check.py:114-135` (`sm5`) builds the `excused` map from every line of the file
  (`:122`) and `continue`s on any line starting `erratum:` (`:127`), so the appended line cannot itself be
  counted as a citation.
- The tool's own self-test already exercises exactly this shape (`:208-209`, "an appended erratum with a resolving
  correction excuses SM5; a bad one does not"), which is why §1.5's `wronggood` variant is a meaningful control
  rather than an accident of the regex.
- `sm6` (`:137-143`) reads the **last** line containing `K_HELD_BACKED`; the erratum line does not contain it.
- `grep -ln SCORECARD corpus/*.py` → `corpus/self_assessment_check.py` only; `reports/round-70/measure.py` mentions
  `SCORECARD.md` only when writing its synthetic fixture (`measure.py:95`). No other parser reads the file.

### 1.6 What the erratum does *not* fix (state this in the lesson, do not overclaim)

After the erratum, the pinned candidate tree still reads `SELF_MISMATCH=11`: `SM1=1`, `SM2=7`, `SM3=2`, `SM4=1`.
SM1 and the seven SM2 units are exactly the repairs the working tree already carries (`QUALITY.md` index
`Q01–Q13` → `Q01–Q15`; the seven names added are, by command on the pinned tree,
`['check_embedded_outputs.py', 'derive_axml_anchors.py', 'derive_axml_anchors_r68.py', 'lint_entry.py',
'q15_tree_id_check.py', 'self_assessment_check.py', 'snapshots/']`). The remaining `SM3=2` + `SM4=1` are the
SHONEN box-1 items (SKILL.md `39098 bytes`/`bfd92057…` vs current `51809`/`a12fb8e2…`, and the lane-seat
`revenger-r64.R64ReviewSkill` `[x]`). The erratum is the **SM5 unit only** — one of the four remaining units after
the README repairs.

---

## Part 2 — Round-69 spot-check V3 and V4 corrections (appended prose, text only)

Both drafts are grounded in my own reproductions below, not in the spot-check's word.

### 2.1 V3 — the C1 table cell

Reproduction (round-69 tip tree `db956ec`, round-69 counter, absolute path, no pipe so the exit is real):

```
$ git -C …/revenger-shokunin archive db956eca73bf810db9bdf2c98dc843a528f5d789 corpus | tar -x -C $T
$ PYTHONDONTWRITEBYTECODE=1 python3 -B …/reports/round-69/measure.py $T > log 2>&1; echo exit=$?
exit=1
$ grep -n "K_HELD_BACKED=" log | head -1
4:K_HELD_BACKED=8/14
$ tail -3 log
Traceback (most recent call last):
  File "…/reports/round-69/measure.py", line 158, in <module>
    rc, last = run(TREE, "q15_tree_id_check.py", "--self-test")
NameError: name 'run' is not defined
```

Draft prose to append (e.g. to `corpus/lessons/round-69-verifier-spotcheck.md` §6 V3 or the round-70 lesson):

> **V3 correction (erratum to the round-69 C1 table cell).** The C1 row's `K_HELD_BACKED` cell reads "not
> printed — the counter crashes before the hold block". That cell is wrong on the second half: the counter prints
> `K_HELD_BACKED=8/14` (and `K_HELD_BACKED_STRICT=8/14`) at line 4 of its stdout, *before* the `NameError` at
> `reports/round-69/measure.py:158`; only the hold block (`HOLDS_OK_V6` and later labels) is unprinted. The
> section's trend sentence "8/14" is right and the cell must not be read as "K unmeasured". Reproduced on the
> round-69 tip tree `db956ec` with the absolute-path invocation; exit 1 (not 2), which is itself the V5 defect.

### 2.2 V4 — the printed counting command

Reproduction (relative form, from the fleet root, which is where the printed form resolves to a non-existent path):

```
$ cd /home/vgpnk/Projects/shokunin && python3 -B reports/round-69/measure.py /tmp/…-r69tip
python3: can't open file '/home/vgpnk/Projects/shokunin/reports/round-69/measure.py': [Errno 2] No such file or directory
```

and the absolute form (the one `reports/round-69/claims.md:156-160` prints) does execute — it produced the V3 log
above and exits 1 on the V5 `NameError`. Note the two documents disagree: `claims.md:154` advertises
`python3 -B reports/round-69/measure.py TREE` (relative) while `claims.md:156-160` gives the absolute form.

Draft prose to append:

> **V4 correction (counting-command restatement).** The round-69 C1 counting command as printed in the round table
> (`python3 -B reports/round-69/measure.py TREE` over a `git archive` tree) does not execute from any cwd but the
> lane root; run from the fleet root it fails with
> `can't open file '/home/vgpnk/Projects/shokunin/reports/round-69/measure.py'`. The command that executes is the
> absolute-path form already printed in `reports/round-69/claims.md:156-160`:
> `cd / && TMPDIR=<scratch> python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-69/measure.py <tree>`.
> Read every round-69 table command as that form; the relative form is a typographic residue, not a second
> invocation contract.

---

## Part 3 — Claim hit-rate ledger, lane rounds 61-69 (considerthese `2026-10-24.md` proposal 3)

### 3.1 Derivation (command)

The ledger is produced mechanically: claim ids and axes are read from each round's pre-registration headings
(`^## C<n> — ` or `^**C<n> — ` in `reports/round-6*/claims.md`); each verdict is read from the **last cell** of the
matching table row inside that round's `SCORECARD.md` section(s) (`^## Round <n>` up to the next `^## `), matched by
an explicit `C<n>` token in the verdict cell, else by the claim's axis word when exactly one non-`unchanged` row of
that axis exists; normalized by `\bC\d (met|improved)\b` → `met`, `falsified` + `honest stop` →
`falsified/honest-stop`, `pending` → `pending`.

```
$ python3 -B /tmp/revenger-r70-R70W1ErratumDraft-ledger.py
61	C1	coverage	247	falsified	C1 falsified: neither candidate survives the fresh attacks
61	C2	calibration	248	met	C2 improved independently
62	C1	coverage	272	met	**improved**, C1 met
63	C1	coverage	313	met	**improved, C1 met**
63	C2	coverage	314	met	**improved, C2 met**
63	C3	calibration	315	met	**improved, C3 met**
64	C1	coverage	379	met	**improved, C1 met**
64	C2	calibration	380	met	**improved, C2 met**
65	C1	coverage	436	pending	**pending — candidate landed, flip deferred to dispatched wave**
65	C2	calibration	435	met	**improved, C2 met**
66	C1	coverage	462	falsified	**falsified C05 candidate, order executed — verdict recorded**
66	C2	calibration	463	met	**improved, C2 met**
67	C1	coverage	492	falsified/honest-stop	**C1 falsified — honest stop** (5/6 routed repairs verified good by fresh seats; fix routed)
67	C2	calibration	493	falsified/honest-stop	**C2 falsified — honest stop** (gate's drift detection + red-before real and verified; reorder fix routed)
68	C1	calibration	520	met	**improved, C1 met** — with the named instrument caveat: two critics show the predicate is satisfiable by a non-detecting gate
68	C2	coverage	521	falsified/honest-stop	**C2 FALSIFIED — honest stop**: wave decisions Q04, Q05, Q07, Q08 (returned FAIL under Q11), Q11, Q13 FAIL on the landed v3 bytes
69	C1	coverage	565	falsified/honest-stop	**C1 FALSIFIED — honest stop** (wave Q FAILs at Q05, Q07, Q11, Q14, Q15 on the landed v4 bytes; kill rule executed)
69	C2	calibration	566	falsified/honest-stop	**C2 FALSIFIED — honest stop, instrument defect.** The frozen counter dies `NameError` at `measure.py:158` …
CLAIMS=18
```

Columns: round · claim · axis · `SCORECARD.md` line the verdict was read from · normalized verdict · raw verdict
(truncated at 120 chars for display; the script prints the full cell).

Claim inventory cross-check (independent command, from the pre-registrations alone):

```
$ for r in 61 62 63 64 65 66 67 68 69; do grep -cE "^## C[0-9]+ — |^\*\*C[0-9]+ — " reports/round-$r/claims.md; done | awk '{s+=$1} END {print "sum="s}'
2 1 3 2 2 2 2 2 2
sum=18
```

### 3.2 Totals

```
$ awk -F'\t' 'NF>=5 {c[$5]++} END {for (k in c) printf "%s=%d\n", k, c[k]}' ledger.tsv | sort
falsified=2
falsified/honest-stop=5
met=10
pending=1
$ awk -F'\t' 'NF>=5' ledger.tsv | wc -l
18
```

**met = 10 · falsified = 2 (not labelled honest-stop: r61 C1, r66 C1) · falsified/honest-stop = 5 (r67 C1, r67 C2,
r68 C2, r69 C1, r69 C2) · pending = 1 (r65 C1) · total = 18.** 10 + 2 + 5 + 1 = 18.

Two cross-checks that make the ledger falsifiable in the other direction:
- rounds 67-69 alone: `awk -F'\t' '$1>=67 && NF>=5' ledger.tsv | wc -l` = **6** claims, `… && $5=="met"` = **1**
  (r68 C1). This is exactly the sentence the round-70 pre-registration asserts at `reports/round-70/claims.md`
  ("1 met (r68 C1) of 6"), now derived rather than quoted.
- the two `falsified`-without-honest-stop rows are genuinely different in kind and should not be folded into the
  honest-stop count: r61 C1 is a fresh-wave rejection of both candidates (`SCORECARD.md:247`), and r66 C1 is an
  **either-way** claim (execute the frozen order) whose executed outcome was candidate falsification — the claim
  was executed as specified while the axis did not move (`SCORECARD.md:462`, `:471`).

### 3.3 Ledger as a table (paste-ready for `corpus/lessons/round-70.md`)

| round | claim | axis | verdict | source |
|---|---|---|---|---|
| 61 | C1 | coverage | falsified | `SCORECARD.md:247` |
| 61 | C2 | calibration | met | `SCORECARD.md:248` |
| 62 | C1 | coverage | met | `SCORECARD.md:272` |
| 63 | C1 | coverage | met | `SCORECARD.md:313` |
| 63 | C2 | coverage | met | `SCORECARD.md:314` |
| 63 | C3 | calibration | met | `SCORECARD.md:315` |
| 64 | C1 | coverage | met | `SCORECARD.md:379` |
| 64 | C2 | calibration | met | `SCORECARD.md:380` |
| 65 | C1 | coverage | pending | `SCORECARD.md:436` |
| 65 | C2 | calibration | met | `SCORECARD.md:435` |
| 66 | C1 | coverage | falsified (order executed) | `SCORECARD.md:462`, `:471` |
| 66 | C2 | calibration | met | `SCORECARD.md:463` |
| 67 | C1 | coverage | falsified — honest stop | `SCORECARD.md:492` |
| 67 | C2 | calibration | falsified — honest stop | `SCORECARD.md:493` |
| 68 | C1 | calibration | met (instrument caveat) | `SCORECARD.md:520` |
| 68 | C2 | coverage | falsified — honest stop | `SCORECARD.md:521` |
| 69 | C1 | coverage | falsified — honest stop | `SCORECARD.md:565` |
| 69 | C2 | calibration | falsified — honest stop (instrument defect) | `SCORECARD.md:566` |

**totals: 10 met / 2 falsified / 5 falsified-honest-stop / 1 pending (18 claims).** Reading: the lane's problem is
not coverage ambition but calibration — every falsification from r67 on is a wave-seat text or instrument defect on
an entry the lane had already labelled improved, and the two `met` rows on the calibration axis (r63 C3, r64 C2,
r65 C2, r66 C2, r68 C1) are all *guard added* claims, not *guard held under attack* claims.

---

## Findings (advisory, wave 1)

- **F1 — the C2 tool's bytes moved in the working tree during this wave.** `git -C … status --porcelain` shows
  `M corpus/self_assessment_check.py`; `git diff` is one line, `sm3`: `re.findall(r"(\d[\d,]*) bytes", text)` →
  `re.findall(r"(?<![\w-])(\d[\d,]*) bytes", text)`. Working-tree sha256 `ae1c62aa…` vs pinned/HEAD
  `6a24baa1…`. The frozen C2 predicate is defined over the checker **as shipped at the tip**, and
  `reports/round-70/claims.md` (C2 kill rule) says SM-class corrections are made by editing the stale
  self-assessment, not the checker. Whoever lands the final bytes must either commit that sm3 change as a
  declared checker revision (with a re-run of `SELF_CLEAN_FIXTURE` / `SELF_MUTANTS_KILLED=6/6`) or revert it. All
  numbers in this report use the pinned `6a24baa1…` bytes and are unaffected.
- **F2 — the working tree's README/SHONEN/SKILL edits are in flight; do not score the tree mid-repair.** At
  18:06 my first checker run over `.` read `SM1=1 SM2=7 … SELF_MISMATCH=12`; by 18:08 the same command read a
  different SM2 because sibling seats had rewritten `corpus/README.md` (`Q01–Q13` → `Q01–Q15`, seven index lines
  added). Every judged number here was therefore re-derived from `git archive aa1842fa`, per the wave's
  stable-target rule.
- **F3 — transient artifact I created and removed.** An exploratory `import self_assessment_check` without `-B`
  wrote `corpus/__pycache__/self_assessment_check.cpython-314.pyc` at 18:08:15; I deleted the directory at
  18:08:37 (`git status --porcelain corpus/` no longer lists it; `ls corpus/__pycache__` → No such file). All
  subsequent runs used `python3 -B` + `PYTHONDONTWRITEBYTECODE=1`. Flagged for the pycache-provenance seat so it
  does not attribute that directory to anyone else.
- **F4 — SM5 repair is still owed at the tip.** `grep -c '^erratum:' SCORECARD.md` = 0 and `SCORECARD.md` mtime
  is `2026-10-25 07:20:56` (untouched while README/SHONEN/SKILL were being repaired), so `SELF_MISMATCH` cannot
  reach 0 until §1.4's line is appended.
- **F5 — not derivable by command, marked `recorded`:** none of the 18 rows fell through to `UNMAPPED`; the only
  vocabulary outlier is r61 C2's cell text "C2 improved independently" (`SCORECARD.md:248`), which the
  normalization rule maps to `met` on the strength of the same row's `0/2 → 2/2`. Raw text is quoted in §3.1 so a
  reviewer can overrule the mapping without re-running anything.

## Scope / out-of-scope

- Wrote only this report and `/tmp/revenger-r70-R70W1ErratumDraft*` scratch (script, pinned trees, variant copies);
  scratch deleted before returning. No lane file edited, no git mutation anywhere.
- Out of scope by assignment: applying the erratum or the V3/V4 prose to the lane, scoring C1/C3, wave-2 decisions.
- Artifacts: this file; scratch script `/tmp/revenger-r70-R70W1ErratumDraft-ledger.py` (deleted; reproduced in full
  in §3.1 by its output), TSV `/tmp/revenger-r70-R70W1ErratumDraft-ledger.tsv` (deleted; full contents in §3.1).
