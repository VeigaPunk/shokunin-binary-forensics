# Round-91 C1 — SM6 v3 mutant table (attack seat MutR91Sm6)

- impl: `corpus/self_assessment_check3.py` sha256 `7f2b8e836cbd7fcb47de2d36343c339d7dbdb1787ae924fe5a15287914630791`
- frozen detector: `reports/round-91/sm6_battery_v3.py` (21 labelled cases), baseline mismatches: **0** (none), real-tree sm6: **0**
- optional detector: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-91/w1/ReviewerR91C1/heldout_sm6_probe.py` — baseline `HELDOUT_MISCLASS=0/22` exit 0
- supplementary probes (attack-seat, NOT frozen truth): S01–S11; baseline values `{'S01': 1, 'S02': 1, 'S03': 0, 'S04': 'EXC:FileNotFoundError', 'S05': 'EXC:FileNotFoundError', 'S06': 0, 'S07': 1, 'S08': 0, 'S09': 1, 'S10': 1, 'S11': 1}`
- **SURVIVORS=6** ['M03', 'M04', 'M06', 'M07', 'M09', 'M17']

| id | textual transformation (exact replaced text → replacement) | rule element broken | battery | killing case ids | held-out | held-out case ids | SUP probe kills |
|---|---|---|---|---|---|---|---|
| M01 | `return cells[2]` → `return cells[3]` | rule 2: stated region = cell index 2 | **KILLED** | R02, R03, R04, R05, R06, R07, R08 | HELDOUT_MISCLASS=12/22 | H01, H03, H05, H06, H08, H10, H12, H14, H15, H18, H20, H21 | — |
| M02 | `return cells[2]` → `return cells[1]` | rule 2: stated region = cell index 2 | **KILLED** | R01, R02, R04, R07, R09 | HELDOUT_MISCLASS=12/22 | H01, H03, H05, H06, H07, H08, H10, H12, H14, H15, H18, H21 | S08, S09 |
| M03 | `if len(cells) >= 5:` → `if len(cells) >= 6:` | rule 2: table row iff at least 5 cells | **SURVIVED** | — | HELDOUT_MISCLASS=0/22 | — | S08, S09 |
| M04 | `region = stated_region(last[-1]).split("K_HELD_BACKED_STRICT")[0]` → `region = stated_region(last[-1])` | rule 3: truncate the stated region at the first K_HELD_BACKED_STRICT | **SURVIVED** | — | HELDOUT_MISCLASS=0/22 | — | S02 |
| M05 | `if len(cells) >= 5:⏎            return cells[2]` → `if len(cells) >= 5:⏎            return s` | rule 2: table row => stated region is cell index 2 | **KILLED** | R06 | HELDOUT_MISCLASS=2/22 | H05, H20 | S08, S09 |
| M06 | `last[-1]` → `last[0]` | rule 1: the LAST SCORECARD line containing K_HELD_BACKED | **SURVIVED** | — | HELDOUT_MISCLASS=3/22 | H12, H17, H18 | S01 |
| M07 | `re.match(r"^\\| C[0-9]+ ", l)]` → `re.match(r"^\\| C[0-9]+ ", l) and "partial" not in l]` | rule 6: D = every `^| C<n> ` map row | **SURVIVED** | — | HELDOUT_MISCLASS=1/22 | H10 | S03, S11 |
| M08 | `if re.search(r"\\|\s*held\s*\\|\s*$", l)` → `if l.split("\|")[4].strip() == "held"` | rule 6: N = README rows whose status is held | **KILLED** | B01, B04, B06, B08, B10, B11, R01, R02, R04, R07, R09 | HELDOUT_MISCLASS=13/22 | H01, H03, H05, H06, H08, H10, H12, H14, H15, H16, H18, H21, H22 | S03, S08 |
| M09 | `readme = txt(root / "corpus/README.md")⏎    rows = [l for l in readme.splitlines()` → `readme = txt(root / "corpus/README.md") if (root / "corpus/README.md").is_file() else ""⏎    rows = [l for l in readme.splitlines()` | rule 6: N/D are read from the README (absence must fail closed) | **SURVIVED** | — | HELDOUT_MISCLASS=0/22 | — | S04 |
| M10 | `return 0 if got == (held, len(rows)) else 1` → `return 0 if got[0] >= held and got[1] == len(rows) else 1` | rule 6: SM6 = 0 iff N equals the held rows | **KILLED** | B03, B12, R03, R08 | HELDOUT_MISCLASS=5/22 | H04, H07, H09, H11, H17 | S01, S09, S10 |
| M11 | `return 0 if got == (held, len(rows)) else 1` → `return 0 if got == (held, len(rows) + 1) else 1` | rule 6: D = the number of map rows | **KILLED** | B01, B04, B06, B07, B08, B10, B11, R01, R02, R04, R07, R09 | HELDOUT_MISCLASS=13/22 | H01, H03, H05, H06, H08, H10, H12, H14, H15, H16, H18, H21, H22 | S03, S06, S08 |
| M12 | `if mm:⏎            got = (int(mm.group(3)` → `if False:⏎            got = (int(mm.group(3)` | rule 4: the FIRST N/D group immediately following the token | **KILLED** | R02 | HELDOUT_MISCLASS=4/22 | H01, H02, H13, H19 | — |
| M13 | `got = (int(mm.group(3) or mm.group(1)), int(mm.group(4) or mm.group(2)))` → `got = (int(mm.group(1)), int(mm.group(2)))` | rule 4: prefer the right side of -> when the group carries one | **KILLED** | B04, B05, B07, B08, R02, R03, R05, R07, R09 | HELDOUT_MISCLASS=8/22 | H01, H06, H10, H11, H14, H17, H18, H22 | — |
| M14 | `(?:\s*(?:\(\s*[\d.]+\s*\))?\s*(?:→\|->)\s*(\d+)\s*/\s*(\d+))?` → `(?:\s*(?:→\|->)\s*(\d+)\s*/\s*(\d+))?` | rule 4: skip an optional parenthesised score such as (5.7) | **KILLED** | B07, B08, R02, R03, R05, R07, R09 | HELDOUT_MISCLASS=8/22 | H01, H06, H10, H11, H14, H17, H18, H22 | — |
| M15 | `if not nums:⏎            return 1` → `if not nums:⏎            return 0` | rule 5: no group => SM6 = 1 | **KILLED** | R06 | HELDOUT_MISCLASS=1/22 | H20 | S02 |
| M16 | `if "K_HELD_BACKED" in l]` → `if "K_HELD_BACKED" in l and "K_HELD_BACKED_STRICT" in l]` | rule 1: any SCORECARD line containing K_HELD_BACKED | **KILLED** | B01, B04, B06, B08, B10, R01, R02, R04, R07, R09 | HELDOUT_MISCLASS=12/22 | H01, H03, H05, H06, H10, H12, H14, H15, H16, H18, H21, H22 | S03, S06, S08 |
| M17 | `if re.search(r"\\|\s*held\s*\\|\s*$", l)` → `if "held" in l` | rule 6: N = rows whose status is held (status column only) | **SURVIVED** | — | HELDOUT_MISCLASS=0/22 | — | S06, S10 |

Every mutant changes exactly one contiguous source region (hunk counts: all 1).

## Supplementary probe definitions (rule-derived; not part of the frozen battery)

| probe | scenario | expected SM6 | rule step |
|---|---|---|---|
| S01 | two K lines; last is false (9/15), first true | 1 | rule 1: last K line is the statement |
| S02 | `K_HELD_BACKED_STRICT 8/15 · K_HELD_BACKED 9/15` | 1 | rule 3: truncate at STRICT ⇒ region empty ⇒ no N/D |
| S03 | README has a `partial` row; statement 8/15 | 0 | rule 6: D counts every map row |
| S04 | no `corpus/README.md` at all; statement 0/0 | 1 | rule 6: undefined without README ⇒ fail closed |
| S05 | no `SCORECARD.md` | 1 | rule 1: no K line |
| S06 | a NOTE cell contains `held`; status cell `frontier`; statement 0/15 | 0 | rule 6: only the status column counts |
| S07 | SCORECARD row with 3 content cells (differential only, no label) | — | threshold boundary |
| S08 | 3 visible columns, token in the axis cell, stated cell true 8/15 | 0 | rule 2 (naive-split convention, as in held-out H15) |
| S09 | 3 visible columns, token in the axis cell, stated cell false 9/15 | 1 | rule 2 (false-green direction) |
| S10 | note-cell `held`, statement 1/15 (false) | 1 | rule 6 (false-green direction) |
| S11 | `partial` row, statement 8/14 (false) | 1 | rule 6 (false-green direction) |

## Reproduce

```
cd /home/vgpnk/Projects/shokunin/revenger-shokunin
TMPDIR=$HYAKU_SCRATCH/revenger-r91/MutR91Sm6/tmp PYTHONUTF8=1 python3 -B \
  .ufo/waves/round-91/w1/MutR91Sm6/mutate_sm6.py \
  --impl corpus/self_assessment_check3.py \
  --battery reports/round-91/sm6_battery_v3.py \
  --out .ufo/waves/round-91/w1/MutR91Sm6 \
  --real . \
  --heldout .ufo/waves/round-91/w1/ReviewerR91C1/heldout_sm6_probe.py
```

Two runs produced byte-identical `mutants.json` (sha256 `60a583853e243ad7da912a60f2da73d1f53732a9112a03761567df0855f12679`).
