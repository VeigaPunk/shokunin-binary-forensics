# ExecR91Sm6V3 — C1 executor (SM6 v3, stated-cell rule)

**Status: C1 verified.** `C1_VERDICT=pass`, counter exit 0, `SM6_MISCLASS=0/22`,
`MUTANTS_KILLED=11/11`, `IMPL_SELFTEST exit=0`, `REAL_SELF_MISMATCH=0`.

## Files written

| path | change |
|---|---|
| `corpus/self_assessment_check3.py` | new (22395 B); v3 checker, SM6 replaced, SM1–SM5 byte-identical to v2 |
| `.ufo/waves/round-91/w1/ExecR91Sm6V3/counter.log` | full frozen-counter output, 39 lines, exit 0 |
| `.ufo/waves/round-91/w1/ExecR91Sm6V3.md` | this report |

`corpus/self_assessment_check2.py`: `git diff -- corpus/self_assessment_check2.py`
is empty (0 lines) — bytes untouched, as required.

## Rule → code (`claims.md` §C1, six steps)

`sm6(root)` in `corpus/self_assessment_check3.py`:

1. `last = [l for l in SCORECARD.splitlines() if "K_HELD_BACKED" in l]`; empty ⇒ 1.
2. `stated_region(line)` — stripped line, if it starts **and** ends with `|` and
   `line.split("|")` has ≥ 5 cells, region = `cells[2]` (the before→after cell);
   else the whole line. This is the frozen reference shape in
   `reports/round-91/mutants.py::region_of`.
3. `region.split("K_HELD_BACKED_STRICT")[0]`.
4. With the token present: `re.match(r"[^0-9]*" + PAIR + ARROW, region[m.end():])` —
   first `N/D` after the token, `ARROW` = `(?:\s*(?:\(\s*[\d.]+\s*\))?\s*(?:→|->)\s*(\d+)\s*/\s*(\d+))?`
   so a `(5.3)` score may sit between the sides and the **right** side wins when
   the group carries an arrow. Without the token: every `PAIR+ARROW` group in the
   region, take the **last** under the same right-side preference.
5. No group ⇒ `return 1` (row does not state the quantity).
6. `return 0 if got == (held, len(rows)) else 1`, with `held` = README rows
   matching `\|\s*held\s*\|\s*$` and `rows` = `^\| C[0-9]+ ` lines.

The pointer cell (cell 3: the counter/probe column) is never read — that is the
whole delta from v2, and the reason R04 (true stated cell, lying pointer) now
scores 0 while R03 (false stated cell, truthful pointer) now scores 1.

## Evidence

Frozen command, run from the lane root:

```
cd /home/vgpnk/Projects/shokunin/revenger-shokunin
PYTHONUTF8=1 python3 -B reports/round-91/c1_counter.py --impl corpus/self_assessment_check3.py --real . --lane .
```

`counter.log` tail (verbatim):

```
CASE REAL label=0 got=0 ok
SM6_MISCLASS=0/22
MUTANT M01 killed=yes misclass=5/21
MUTANT M02 killed=yes misclass=9/21
MUTANT M03 killed=yes misclass=9/21
MUTANT M04 killed=yes misclass=5/21
MUTANT M05 killed=yes misclass=5/21
MUTANT M06 killed=yes misclass=7/21
MUTANT M07 killed=yes misclass=6/21
MUTANT M08 killed=yes misclass=1/21
MUTANT M09 killed=yes misclass=1/21
MUTANT M10 killed=yes misclass=5/21
MUTANT M11 killed=yes misclass=7/21
MUTANTS_KILLED=11/11
IMPL_SELFTEST exit=0 last=SELFTEST OK: clean 0; six planted defects each scored exactly their class; twenty-four tightened-class probes (six v2 denominator legs, four v3 real-format legs where the stated cell and the pointer cell disagree) scored as declared; erratum excuses only a resolving, prefix-sharing correction
REAL_SELF_MISMATCH=0 exit=0
LEGS battery=pass mutants=pass selftest=pass real=pass
C1_VERDICT=pass
```

Exit 0. All 21 labelled cases (`B01`–`B12`, `R01`–`R09`) plus `CASE REAL`
scored `ok`; no battery case disagreed with the rule, so no case is reported as
unsatisfiable.

Self-test, separately: `PYTHONUTF8=1 python3 -B corpus/self_assessment_check3.py --self-test`
→ `SELFTEST OK …`, exit 0.

SM1–SM5 identity, checked by comparing `ast.get_source_segment` of each function
between v2 and v3: `txt`, `sm1`, `sm2`, `boxes`, `sm3`, `sm4`, `sm5`,
`commonprefix`, `evaluate`, `required` — all **IDENTICAL**; `sm6` differs. Import
block identical. CLI preserved verbatim: `--root TREE --lane LANE` prints
`SM1..SM6` + `SELF_MISMATCH=<n>` (exit 0 iff 0, 1 if >0, 2 on a missing file),
`--self-test`, usage → 64.

### Self-test legs added this round (v3)

Four SM6 probes in the lane's own five-cell row shape, via a new
`_table_row(root, row)` helper (adds the fifteenth map row and makes `row` the
whole SCORECARD statement):

| probe | want |
|---|---|
| stated cell true, pointer agrees | 0 |
| **stated cell false while the pointer cell agrees** (`→ 9/15` vs 8 held, pointer `=8/15`) | 1 |
| **stated cell true while the pointer cell disagrees** (`→ 8/15`, pointer `=9/15`) | 0 |
| stated cell carries scores only (`2.9 → **4.3**`), pointer carries the N/D | 1 |

The last two are the round-90 counterexample pair: a v2-shaped rule passes the
second and fails the third, so the self-test proves SM6 can fail — and can pass
— in the lane's own row format. v2's own twenty probes are retained and still
score as declared (they are bare-line / `_add_row` legs, unaffected by the cell
cut). Probe count 20 → 24; the summary line was updated to say so.

## Integration dependency (not written by me)

The counter's real leg runs `--impl … --root .`, and v2's SM2 (byte-identical,
unchangeable) requires every top-level `corpus/*.py` to be named in
`corpus/README.md`. Adding `corpus/self_assessment_check3.py` therefore made the
tree fail its own index class (`SM2=1`, `SELF_MISMATCH=1`) until the index row
existed — a landing/integration write outside my assigned paths. The L1 landed
it at `corpus/README.md:30` (the r90 precedent: commit `abd1394`, "SM v2
index"), and the counter was re-run after that. I did not edit `README.md` or any
other lane file; the only lane files I created are the two listed above.

Pre-landing proof that SM2 was the sole cause: in `$HYAKU_SCRATCH` (since
deleted) I copied `corpus/ SHONEN.md SCORECARD.md SKILL.md` to a scratch tree,
added only that one index line, and ran
`python3 -B corpus/self_assessment_check3.py --root <scratch> --lane .` →
`SM1..SM6 = 0`, `SELF_MISMATCH=0`, exit 0.

## Risks / disclosures

- **Row-shape dependence.** Cell index 2 is taken from `line.split("|")`, so the
  stated region is correct for the canonical row (`| a | b | c | d | e |`).
  A line with a leading pipe but no trailing pipe falls back to the whole line —
  this mirrors the frozen reference (`mutants.py::region_of`) exactly and no
  battery case exercises the difference.
- **A truthful pointer no longer rescues a row.** Per rule step 5, a row whose
  stated cell carries no `N/D` scores 1 even if its probe cell quotes the
  correct counter (R06). That is the frozen rule, not a defect.
- **SM2 coupling is now a landing rule:** any future top-level `corpus/*.py`
  must get its `corpus/README.md` index line in the same landing commit, or the
  self-assessment gate scores `SELF_MISMATCH≥1` for the whole tree.
- No tools were installed or upgraded this seat; nothing ran outside
  read-only git and the two named writers.

## Blockers

None remaining. `counter.log` carries `C1_VERDICT=pass` at exit 0.
