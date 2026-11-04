# ReviewerR90C1 — attack on C1 (SM6 v2), round 90 w1

Freeze `c7767789fe9e96bcc0d50656ad4bdce69ba3a3a9`. Tree = `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive c7767789… corpus SHONEN.md SCORECARD.md SKILL.md`, extracted in scratch `/fast/scratch/hyaku/revenger-r90/ReviewerR90C1` (TMPDIR set there; deleted before yield). Receipts are in `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ReviewerR90C1/`. No tools were installed. No lane byte outside this dir was written.

Pins: `sha256sum` of `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/self_assessment_check.py` (82e59fce…), `corpus/self_assessment_check2.py` (0e73a90b…) and `reports/round-90/sm6_battery.py` (0f21a570…) all match `reports/round-90/instrument-pins.log`.

## Step 1: Re-runs (receipt `step1-rerun.log`)

| run | result |
|---|---|
| `sm6_battery.py --impl …/self_assessment_check.py --real TREE` | `SM6_MISCLASS=7/14` (B01 B02 B07 B10 B11 R1 R2), exit 1. This matches the red receipt and kill rule (c). |
| `sm6_battery.py --impl …/self_assessment_check2.py --real TREE` | `SM6_MISCLASS=0/14`, exit 0. R2 is flagged (got=1), so kill rule (d) holds. |
| v1 `--self-test` | `SELFTEST OK`, exit 0 |
| v2 `--self-test` | `SELFTEST OK` (twenty probes, six v2 legs), exit 0. Kill rule (a) holds. |
| v1 `--root TREE --lane LANE` | SM1=0 SM2=1 SM3=0 SM4=0 SM5=0 SM6=1, `SELF_MISMATCH=2` |
| v2 `--root TREE --lane LANE` | SM1=0 SM2=1 SM3=0 SM4=0 SM5=0 SM6=0, `SELF_MISMATCH=1` |

- SM1–SM5 are equal between v1 and v2. **Finding F0 (landing obligation, not a defect of v2 itself):** over the freeze tree, v2 prints `SELF_MISMATCH=1`, not 0. The cause is SM2=1: `corpus/README.md` at the freeze does not name `self_assessment_check2.py` (`step1-diagnose.log`). The lane worktree carries an uncommitted README line that names it.
- I simulated the landing as the freeze archive plus the current worktree `corpus/README.md` (sha256 af5bfb81…) and `SKILL.md` (`step1-sim-landing.log`):
  - v1: `SM1..SM5=0`, SM6=1.
  - v2: all six classes 0, `SELF_MISMATCH=0`, exit 0.
  - Battery: 0/14.
- Kill rule (b) therefore holds **only if that README line lands**.

## Step 2: Diff v1 → v2 (receipt `step2-v1-v2.diff`)

The diff touches four things only:
1. The docstring: header, rationale paragraph, SM6 definition and usage paths.
2. The `sm6()` regex and return logic, which now reads N/D and checks D against the map row count.
3. A new `_add_row` self-test helper.
4. Six new self-test probes and the `SELFTEST OK` text.

`sm1`–`sm5`, `evaluate`, `required` and `main` are untouched. Confirmed.

## Step 3: False-green hunt (probe `fg_probe.py`, receipt `step3-fg-probe.log`)

`fg_probe.py` builds trees with the frozen battery's own `build()` (rows `| Cnn | s | k | w | held/frontier |`). Multi-line cases get a raw SCORECARD body. The probe scores `sm6()` of v1 and v2.

Labels follow the claims.md predicate: 0 iff the current side states N = held AND D = map rows. All cases use 15 rows with 8 held.

Result: **`V2_FALSE_GREEN=8 V2_FALSE_RED=7 of 21`**.

False greens (v2 = 0, true label = 1):

| id | last K line(s) | why v2 passes it |
|---|---|---|
| P03 | `K_HELD_BACKED 8/15 → 9 / 15` | A spaced current side fails the optional arrow group, so v2 falls back to the left side, 8/15. |
| P04 | `K_HELD_BACKED 8/15 (5.3%) → 9/15 (6.0%)` | The score slot only allows `[0-9.]`, so `%` breaks the arrow group. |
| P05 | `K_HELD_BACKED 8/15 => 9/15` | `=>` is not an accepted arrow. |
| P06 | `K_HELD_BACKED 8/15 ⇒ 9/15` | `⇒` is not an accepted arrow. |
| P07 | `K_HELD_BACKED was 8/15, now 9/15` | The first fraction after the token is taken. |
| P11 | `K_HELD_BACKED 9/15` then a fenced block holding `K_HELD_BACKED 8/15` | The last line naming the token is inside the fence; fences are not skipped. |
| **P15** | `\| coverage — K \| 8/15 (5.3) → 9/15 (6.0) \| \`measure.py TREE\` (\`K_HELD_BACKED=8/15\`) \| same \|` | **This is the lane's own SCORECARD row shape.** The before→after claim cell comes *before* the token, so v2 reads only the counter citation `K_HELD_BACKED=8/15`. A false after-score passes whenever the cited counter output is true. |
| P20 | `K_HELD_BACKED 8/16`, README with an extra `\| C99 \|` line inside a fenced example | D counts every `^\| C<n> ` line anywhere in the README, not just map rows. |

The requested shapes, with their outcomes:

| shape | outcome |
|---|---|
| trailing text `8/15 (5.3)` (P01) | ok |
| spaced `8 / 15` (P02) | false **red** |
| several statements on the last line (P09, P10) | ok |
| K line inside a fence (P11) | false green |
| `K_HELD_BACKED_STRICT`-only last line (P12) | false **red**: it masks a true earlier K. P13 is ok. |

Other false reds: P08 (chained `→ … → 8/15`), P14 (STRICT before K on one line: the `split` drops the K), P17 (`in round 89:` digits before the fraction), P18 (a numberless last K line masks a true one) and P21 (the fenced C99 row inflates D). v1 gets every probe red (always 1), so none of this is a v2 regression against v1 on greens. These are blind spots outside the frozen 14 cases.

Real tree: the last K line (SCORECARD line 693 of the archive, the R1 case) has exactly the P15 shape. The claim cell reads `8/15 (5.3) → 8/15 (5.3)` and the citation reads `` (`K_HELD_BACKED=8/15`) ``. R1 = 0 is correct, but v2 reaches it by checking the citation, not the claimed after-side. (`step3-real-k-lines.log` is a rough scan only: its row-667 "v2-reads 8/14" column comes from my simplified regex, which lacks the backtick handling. B08 shows v2 reads 8/15 there.)

## Step 4: Battery labels vs. the predicate sentence

I checked every case against "0 iff current side states N = held AND D = map rows". All 14 labels agree:

- **True statements (label 0):** B01, B04, B06, B08 and B10 state the current side correctly. For B11, the STRICT metric is a different statement, and the K side is 8/15.
- **False or missing statements (label 1):**
  - B02, B03 and B12: wrong N or D.
  - B05: the current side is 8/14.
  - B07: 8/15 over a 14-row map.
  - B09: no statement.
  - R2: the appended 8/14 is the last K line over 15 rows.
- **R1:** I re-derived 15 rows, 8 held and current side 8/15 independently, agreeing with `reports/round-90/c1-real-label.log`.

Residual risk: R1's label is not fixed in the file. It comes from `--real-label`, default 0. If a landing tree changed the K statement and the caller omitted `--real-label`, R1 would be scored against a stale 0.

## Proposals (report only; frozen instruments untouched)

- A v3 SM6 should anchor on the claim cell (`N/D (s) → N/D (s)` in the row that names the token), not on the first fraction after the token.
- It should accept `=>`, `⇒` and spaced fractions, skip fenced blocks, and count D only inside the coverage-map table.
- Freeze P03–P07, P11, P15 and P20 as new battery cases before any v3 score.

VERDICT: C1 holds on its frozen predicate: v2 `SM6_MISCLASS=0/14`, self-test OK, SM1–SM5 equal to v1, R2 flagged, v1 control 7/14. Kill rule (b) `SELF_MISMATCH=0` holds only once the uncommitted `corpus/README.md` line naming `self_assessment_check2.py` lands (the freeze tree gives SM2=1). Non-blocking defect outside the battery: 8/21 probe shapes are false greens, including P15, the lane's own SCORECARD row shape, where v2 checks the counter citation and not the claimed after-side.
