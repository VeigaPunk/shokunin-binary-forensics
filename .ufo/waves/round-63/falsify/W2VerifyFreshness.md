# W2 — Freshness hold attack (C1 supporting hold, `FRESH_ROWS`)

**Verdict: HOLDS — 18/18 rows present, `holds|STALE`; zero drift vs `55bcb6e`. Not BROKEN.**

Scope: the freshness assertion rows the frozen probe counts for C1 admission
(`claims.md` "Counting and admission order", `HOLDS_OK` conjunct `fresh == 18`).
Nothing below edits or re-adjudicates C1's Q01–Q13 decisions or the C2/C3 counts.

## Target state

| Item | Value |
|---|---|
| Lane repo | `/home/vgpnk/Projects/shokunin/revenger-shokunin` |
| Lane tip | `db55bd6488e24e956df5818ae34c2a043d7ddc12` (2026-10-23 23:54:16 -0300) |
| Claim base | `55bcb6e1aeb4d42923a4e98db6580f67142b41ac` — ancestor of tip, `git rev-list --count 55bcb6e..HEAD` = 3 |
| Round commits | `54ab973` freeze probe → `2a34e45` build state → `db55bd6` C1 candidate + SOURCES + lesson |
| Frozen probe | `reports/round-63/measure.py` sha256 `3b7fba2d5243bbe0b723a99a53085130ff97010e23c8a59a8027f5f8992c5908` (single-touch history at `54ab973`) |

## Byte identity (`55bcb6e` → tip → worktree → archive)

| File | Base blob | Tip blob | Worktree SHA-256 | Archive-tree SHA-256 | `git diff 55bcb6e` |
|---|---|---|---|---|---|
| `corpus/knowledge/seed.md` | `27bb6a89…` (100644) | `27bb6a89…` (100644) | `d1d31602f2b667d6c9406743f06dd2f14030cf1fdf477b1da251f2682d7d7534` | same | empty (0 bytes, exit 0) |
| `corpus/knowledge/2026-10-12-rea-readiness-checklist.md` | `2c32a77d…` (100644) | `2c32a77d…` (100644) | `561327faf39fdc9221c3ebc1b2f9e5175a466ca39fb2c37d119be594f085b6e0` | same | empty (0 bytes, exit 0) |

Both forms of the required check were run: worktree (`git diff 55bcb6e -- <two paths>`,
exit 0, 0 bytes) and commit-to-commit (`git diff 55bcb6e HEAD -- <two paths>`,
exit 0, 0 bytes). `git status --porcelain` for both paths: empty.

## Row count by hand (frozen regex, replicated)

Regex `^\| [FK][0-9]+ .*\| (holds|STALE)` run over the worktree files:

```
corpus/knowledge/seed.md                                total_lines=71  FRESH=12
corpus/knowledge/2026-10-12-rea-readiness-checklist.md  total_lines=46  FRESH=6
FRESH_ROWS=18/18
```

ID set is exactly `F01–F12 ∪ K01–K06`: 18 IDs, 18 unique, **no duplicates**, verdict
mix 8 `holds` / 10 `STALE`. Every match carries its verdict in the **final cell**:
seed lines 56–67 (`F01`…`F12`), checklist lines 36–41 (`K01`…`K06`). The only
non-matching pipe lines in those two tables are the headers (`| fact |`) and
separators (`|---|`) at seed 54/55 and checklist 34/35 — no renamed, re-spaced, or
hidden F/K row exists.

Label source: `reports/round-63/measure-before.log:10` already reads `FRESH_ROWS=18/18`
at the base — freshness is a **hold**, not a claimed target; the only failure mode
in scope is drift, and there is none.

## Frozen probe on the committed tip (one counting command, re-run)

```
git archive db55bd6 corpus | tar -x -C /tmp/revenger-r63-w2fresh/tree
TMPDIR=/tmp/revenger-r63-w2fresh python3 -B reports/round-63/measure.py <tree>   # exit 0
…
FRESH_ROWS=18/18
…
HOLDS_OK=yes
PROBE_EXIT=0
```

Incidental tip labels (reported, **not** my adjudication): `K_HELD=6/14`,
`K_ROW C06 status=partial`, `K_HELD_BACKED=6/14`, `F_COVERAGE=5/8`
(`native-static, javascript, archives, firmware, evm`), `C3_CONTROLS_PASS=2/2`,
`C3_RECEIPT_KILLED_ATTRIBUTED=2/2`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`.
C06 still `partial` is the contract-mandated pre-flip state; the K target is not
mine to certify and is unaffected by anything in this report.

## Attack log (each names what it attacks)

| # | Attack | Result |
|---|---|---|
| A1 | Probe-regex fidelity — hand-rolled regex must reproduce the probe's count | 18/18 both sides |
| A2 | Uncommitted row injection — forged extra row only in the worktree | worktree hash == committed blob hash; status clean |
| A3 | Base drift — rows edited since `55bcb6e` and hidden by a path filter | both diff forms empty (0 bytes) |
| A4 | Row-shape evasion — a row edited to dodge `^\| [FK][0-9]+ ` and drop from count | every F/K table row matches; only headers/separators do not |
| A5 | Count-preserving swap — delete one row, add another to keep 18 | ID set exactly 18 unique `F01–K06`; zero duplicates |
| A6 | Archive/worktree divergence — clean filter or checkout rewrite changes probe input | hash identical across worktree, tip blob, base blob, archive tree |
| A7 | Type/mode substitution — symlink or exec bit hides content | `100644` regular blob at base and tip |
| A8 | Counter tampering — `measure.py` rewritten to hardcode 18 | hash matches frozen hash from `54ab973`; hand regex agrees independently |
| A9 | Silent repair elsewhere — freshness rows duplicated in another knowledge file | `git diff --stat 55bcb6e HEAD -- corpus/knowledge/` shows only the new `round-63-zip-central-directory-evidence.md` (+709); the two freshness files are untouched |

**Severity: none.** No drift, no missing row, no shape evasion, no probe tamper.
**Smallest remediation: none** — preserve these bytes through admission.

## Residual risk

- The hold proves the assertion rows survive byte-identically; it does not prove
  the 2026-10-19 observations are still true today (host versions are time-sensitive).
  That is outside the frozen probe's definition and inside Q05 ("presence is not
  capability"); no host-version re-probe was in my assignment and none was run.
- The regex's greedy `.*` would count a verdict token occurring mid-line. At the
  tip every matched row has its verdict as the final cell, so the laxity is unrealized,
  but a future edit could satisfy the counter with prose.

## Verification gaps

- Did not run `jj` (lane jj state off-limits per lane bounds); git is the lane's
  committed store and is what the probe consumes (`git archive`).
- Did not re-open `corpus/README.md` C06 beyond the probe's `status=partial` line;
  the flip decision belongs to the adjudication seat, not this one.
- Ignored one out-of-lane IRC from `kotodama-r64.RevVerifyO2` (kotodama round-64
  mutant `m5`): different lane/round, no bearing on R63 freshness; no action taken.
- Tool installs: none (pacman paused; no uv/npx/binary install needed). Heavy scratch
  `/tmp/revenger-r63-w2fresh` removed after this report landed.
