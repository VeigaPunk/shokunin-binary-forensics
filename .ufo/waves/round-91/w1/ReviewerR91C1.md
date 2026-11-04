# ReviewerR91C1 — held-out SM6 probe vs landed v3 (round-91 C1 attack, calibration)

Verdict first: **the landed `corpus/self_assessment_check3.py` scores `HELDOUT_MISCLASS=0/22` (exit 0) on a
22-case held-out set that is disjoint from the frozen 21-case battery** — no false green, no false negative,
no divergence on either genuinely ambiguous case. The same set scores the red v2 gate **5/22**, so the probe
discriminates. Full output: `heldout-run.log` (v3, with per-case rule derivations),
`heldout-reference-check.log`, `heldout-v2-comparison.log`.

- Probe module: `.ufo/waves/round-91/w1/ReviewerR91C1/heldout_sm6_probe.py`
  (`python3 -B heldout_sm6_probe.py --impl <checker.py> [--fn <name>] [--derive]`; exit 0 iff 0 misclass,
  1 otherwise, 64 usage — verified: no-args exit 64, `--help` exit 0).
- Labels hand-derived from the frozen rule in `reports/round-91/claims.md` §C1, rule steps named per case
  (`S1` last-K-line, `S2/S2b` stated-region selection, `S3` STRICT truncation, `S4a` token-adjacent read,
  `S4b` last-N/D fallback, `S5` no-group → 1, `S6` N==held ∧ D==rows); printed by `--derive`.
- Read-only over the lane except the four seat files above; frozen battery/impl/counter bytes untouched;
  no git/jj mutation (only `rev-parse`/`status` reads); no tool installs (none needed).

## Score

| impl | HELDOUT_MISCLASS | exit | false greens (label 1, got 0) | false flags (label 0, got 1) |
|---|---|---|---|---|
| `corpus/self_assessment_check3.py` (landed v3) | **0/22** | 0 | none | none |
| `corpus/self_assessment_check2.py` (red gate, context only) | 5/22 | 1 | H13, H20 | H03, H05, H14 |
| frozen reference (`reports/round-91/mutants.py::reference`) | 0/22 | 0 | — | — |

Label fidelity: the corrected label set scores 0/22 against the frozen reference before the v3 result was
accepted, so "v3 passes" means "v3 agrees with the frozen rule as code, on cases the battery never asked".

## Case set (H01–H22) — mandated shapes

| required shape | cases | outcome under v3 |
|---|---|---|
| stated cell with two arrows | H01 (judged pair = middle, label 0), H02 (label 1) | ok / ok |
| token after the numbers | H03 (label 0, fallback branch), H04 (label 1) | ok / ok |
| axis label itself carries an `N/D` | H05 (axis token decoy), H06, H07 (plain axis `N/D`) | ok / ok / ok |
| `K_HELD_BACKED_STRICT` mention / escaped pipe | H08, H09 (STRICT in row format), H20, H21 (escaped `\|`) | ok ×4 |
| map has a `partial` status row | H10 (label 0), H11 (label 1), plus one trailing-space held row | ok / ok |
| `N/D` in fenced/code context in the stated cell | H12 (file-level fence above the row), H13 (inline code span inside the stated cell) | ok / ok |
| genuinely ambiguous | H19 (en-dash `–>` arrow), H20 (escaped pipe in axis cell) | ok / ok (literal labels) |

Boundary extras: H14 (4-visible-column row with a `K_HELD_BACKED=9/15` pointer decoy), H15 (3-column row
with a verdict-column decoy), H16 (row not ending in `\|` → whole-line region), H17/H18 (two K rows, LAST
judged, both directions), H22 (2-column row → whole-line region). H01/H02 pin that S4a takes **one** arrow
step from the token (a last-pair reader false-greens H01's trailing `9/16`; a left-side reader fails both);
H03/H04 pin that the `S4b` fallback applies when the token-adjacent read yields no group.

Honest interpretation note on the "fenced code block inside the stated cell" requirement: a multi-line fence
cannot live inside a single table row, so it is realized two ways — H12 puts the fence (with a wrong token-
carrying pair) in the SCORECARD above the row (S1 must pick the row as the LAST K line), and H13 puts an
inline code span carrying `K_HELD_BACKED=9/16` inside the stated cell itself (S4a reads the FIRST token
occurrence). Both are disclosed in the module docstring.

## Mismatches found

- **v3: none.** Every case matches its hand-derived label; `AMBIGUOUS_DIVERGENCE=0`.
- **v2 (context, not the claim target): 5/22.**
  - H03, H05 (false flags): v2 reads the last token-adjacent group on the whole line, so a stated cell whose
    token carries no following digits (or a decoy token+pair in the axis cell) misroutes it — the round-90
    critic's pointer-cell defect, reproduced on held-out shapes.
  - H14 (false flag): same whole-line read lets the 4th-column pointer decoy `K_HELD_BACKED=9/15` decide.
  - H13 (false green): v2 takes the last token-adjacent group, so a stale code-span pair ahead of the real
    statement is skipped; the frozen rule reads the first token occurrence and flags it.
  - H20 (false green, ambiguous case): v2's whole-line scan finds the true pair in the stated cell; the
    literal rule reads cell index 2 of the naive split (' K map ') and flags. See ambiguity below.

## Ambiguity found

Two cases where the frozen rule does not decide the outcome; labels follow the literal reading, and both are
flagged `AMBIG` in the probe output:

1. **H19 — arrow class.** Stated cell uses `8/14 (5.7) –> 8/15 (5.3)` with an en dash. The rule names only
   `→`/`->`, so the literal read judges the left pair `(8,14)` → mismatch (label 1); a human reading `–>` as
   an arrow would judge the right side `(8,15)` → label 0. v3 implements the literal class (got 1 = label).
   Risk: a real lane row typed with a Unicode dash lookalike would be flagged as a mismatch by v3 even when
   its numbers are true.
2. **H20 — escaped pipes.** Axis cell contains `\|`. The rule says "cell index 2" of the `|`-delimited row
   without defining escape handling; a naive split makes cells[2] the tail of the axis cell (no token, no
   N/D → S5, label 1), a markdown-aware reader would judge the true stated cell (label 0). v3 implements the
   naive split (got 1 = label). Risk: any lane row containing `\|` left of the stated cell is judged on the
   wrong region — and per S5 that means **flagged as not stating the quantity** even when the stated cell is
   true. The lane's real rows currently contain no `\|`, so the frozen counter's real-tree leg is unaffected.

A third near-ambiguity is decidable but worth naming: H13 shows "the first `N/D` group that immediately
follows the token" means the first **token occurrence** (a stale inline-code pair ahead of the real
statement controls the verdict). The frozen reference decides it; v3 agrees; the frozen battery never tests it.

## Seat erratum (label provenance, disclosed)

The first derivation pass carried three seat errors, all caught by scoring my labels against the frozen
reference **before** accepting any implementation result: H10/H11 built 8 held rows where the labels assumed
7 (`["held"]*7 + ["held*"]`), and H15 misread the frozen "cell index 2" as the third visible column (index 2
of a naive `split("|")` is the second visible column — which is exactly why the rule's stated cell is the
before→after column on every row with ≥3 visible columns). Fixtures/labels were corrected per the frozen
rule's own semantics; the reference check then scored 0/22 (`heldout-reference-check.log`). The first-pass
reference log was overwritten by the corrected run's `tee`; the erratum is documented in the probe docstring.
The implementation was never the arbiter of a label.

## Residual risk / verification gaps

- The held-out set exercises `sm6` only; it says nothing about v3's SM1–SM5 classes, `--self-test`, or the
  real-tree leg (`REAL_SELF_MISMATCH`) — those remain the frozen counter's legs, not mine.
- Both ambiguity gaps (H19, H20) are real rule gaps: if the lane ever types a dash-arrow lookalike or an
  escaped pipe into its SCORECARD row, v3's verdict flips under a defensible alternative reading. A one-line
  rule clarification would close it; I did not edit claims.md (frozen).
- `reports/round-91/mutants.py::reference` was used as the rule-as-code arbiter for label fidelity; where
  prose and reference could diverge I re-derived from prose and found no divergence on this set.

Receipts (all under `.ufo/waves/round-91/w1/ReviewerR91C1/`): `heldout_sm6_probe.py`,
`heldout-run.log` (v3, 0/22, with derivations), `heldout-reference-check.log` (0/22),
`heldout-v2-comparison.log` (5/22).
