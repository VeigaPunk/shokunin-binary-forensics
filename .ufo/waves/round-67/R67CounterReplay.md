MATCH — independent replay of the frozen counter over `git archive fa0eb3eb corpus` reproduces every key label in `measure-before.log`; the only textual diff is one trailing blank line.

## Instrument identity

| check | command | actual |
|---|---|---|
| worktree counter sha | `sha256sum reports/round-67/measure.py` | `7933c060db4d9b8db889830e2e0b6e1da1724d94854201aac9552e2a49cbc07e` |
| committed counter sha (HEAD `7668510`) | `git show 7668510:reports/round-67/measure.py \| sha256sum` | `7933c060…bc07e` (identical blob) |
| pinned value | `reports/round-67/measure-before.log:90` | `sha256 7933c060db4d9b8db889830e2e0b6e1da1724d94854201aac9552e2a49cbc07e` |

Pinned == worktree == committed. `claims.md:113` pins the sha by reference ("see `sha256sum reports/round-67/measure.py` in `measure-before.log`"), so the authority line is the log trailer at `measure-before.log:90`, which carries both the sha and the base commit — no ambiguity, but a reader must open the log to see the literal value.

## Replay

```
mkdir -p /tmp/revenger-r67-seat-counter
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive fa0eb3eb33f22f56ebf066dea5440121a30d55a2 corpus | tar -x -C /tmp/revenger-r67-seat-counter
cd / && TMPDIR=/tmp/revenger-r67-seat-counter python3 -B \
  /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-67/measure.py /tmp/revenger-r67-seat-counter
```

Exit code **0** (contract: 0 = holds), stderr empty, 88 stdout lines, ~1.3 s. Archived corpus at base: 498 files.

### Key labels (replayed vs receipt)

| label | replayed | `measure-before.log` |
|---|---|---|
| `K_HELD` | `8/14 score=5.7` | `8/14 score=5.7` |
| `K_ROW C05 status` | `uncovered` | `uncovered` |
| `K_ROW C07 status` | `held` | `held` |
| `K_HELD_BACKED` | `8/14` | `8/14` |
| `K_HELD_BACKED_STRICT` | `8/14` | `8/14` |
| `C05_REJECTED_MARKED` | `yes` | `yes` |
| `C05_KNOWLEDGE_COLUMN` | `-` | `-` |
| `C05_SINGLE_V2` | `no` | `no` |
| `C7_GATE_PRESENT` | `no` | `no` |
| `C7_SELFTEST` | `n/a` | `n/a` |
| `C7_RED_ON_R65_CANDIDATE` | `no` | `no` |
| `C7_V2_CLEAN` | `n/a (no gate)` | `n/a (no gate)` |
| `C7_CONTROL_PASS` | `0/1` | `0/1` |
| `C7_MUTANT_KILLED` | `0/1` | `0/1` |
| `C7_MUTANT_KILLED_ATTRIBUTED` | `0/1` | `0/1` |
| `C6_RECEIPT_KILLED_ATTRIBUTED` | `4/4` | `4/4` |
| `HOLD_CALIBRATION` | `4/4` | `4/4` |
| `HOLD_REPLAY` | `10/10` | `10/10` |
| `FRESH_ROWS` | `18/18` | `18/18` |
| `HOLDS_OK` / `_V2` / `_V3` / `_V4` | `yes` ×4 | `yes` ×4 |
| `HOLDS_OK_V5` | `no` | `no` |
| `STRICT_REJECT_WINDOW_SELFTEST` | `pass old_window_miss=True` | same |
| `SAVED_RECORDS` | `59` | `59` |
| `README_TOKEN_LEGEND_MISMATCH` | `0 rows=[]` | `0 rows=[]` |
| `F_COVERAGE` | `5/8 score=6.2`, families `native-static, javascript, archives, firmware, evm` | same |

Attributed calibration sub-labels also identical: `C2_CONTROLS_PASS=2/2`, `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2`, `C3_RECEIPT_KILLED_ATTRIBUTED=2/2`, `C4_RECEIPT_KILLED_ATTRIBUTED=2/2`, `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2`, `C6_RECEIPT_KILLED=4/4`, plus all 10 `HOLD <verifier> exit=0 …` lines byte-equal.

### Whole-log diff

```
diff <(grep -v '^# frozen instrument' measure-before.log) out.log
@@ -86,4 +86,3 @@
 HOLDS_OK_V4=yes
 HOLDS_OK_V5=no
-
```

Single hunk: the receipt contains one blank line between the last label and its `# frozen instrument:` trailer; the counter does not emit it. No label, value, ordering or wording difference. Diff exit 1 is attributable only to that blank line (verified by the hunk, not by assertion).

## Side-effect and determinism checks

- Second independent extraction (`/tmp/revenger-r67-seat-counter2`) re-run: `diff run2.log out.log` → **DETERMINISTIC_IDENTICAL**; exit 0 again.
- `diff <(find corpus -type f | sort | xargs sha256sum)` across the pre-run tree and the tree the counter ran in → **TREE_UNMUTATED_BY_COUNTER**: the instrument writes nothing into the measured tree.
- Both runs: 0 bytes on stderr.

## Do-nothing control — corroborated against the tree, not just labels

| control fact | command | observed |
|---|---|---|
| v2 candidate absent at base | `ls corpus/knowledge/round-67-apk-axml-byte-evidence.md` | No such file (as contract requires: C1 lands after base) |
| C7 gate absent at base | `ls corpus/check_embedded_outputs.py` | No such file → `C7_GATE_PRESENT=no` is structural, not a parse failure |
| README C05 not flipped | `corpus/README.md:34` | `\| C05 \| Android packages (APK) \| — \| …retained rejected candidate knowledge/round-65-apk-axml-byte-evidence.md… \| uncovered \|` |
| C7 red-before surface exists | `grep -o 'payload_first16_hex": "[^"]*"'` on r65 candidate | line 41 carries `4d616e696673742d56657273696f6e` (the drifted 15-byte manifest hex) alongside the other two members' correct hexes; `admission-status: rejected` at line 7 |

So the base receipt is a genuine do-nothing control: `8/14` held, C05 `uncovered` naming only the retained rejected r65 candidate, C7 all zero, `HOLDS_OK_V5=no`, exit 0 — exactly the values the contract's frozen predicates and do-nothing paragraphs predict.

## Findings / risks (non-blocking)

1. **Provenance nuance, not a mismatch.** `measure.py` does not exist at the claim base `fa0eb3eb` (`git show fa0eb3eb:reports/round-67/measure.py` yields the empty blob `e3b0c442…b855`); it is introduced in `d11f81d` and unchanged at HEAD `7668510`. The receipt therefore cannot be reproduced from a base checkout alone — it needs the committed counter from any commit ≥ `d11f81d`. I verified the HEAD blob is bit-identical to the pinned sha, and my replay with those bytes reproduces the receipt, so the freeze is intact; the only cost is that the reproducibility recipe must name the counter's own commit, not just the base.
2. **C2–C6 are baseline-invariant.** Every non-C7 attributed calibration count is already at target at the base tree (`2/2, 2/2, 2/2, 2/2, 4/4`), and `HOLD_CALIBRATION=4/4` / `HOLD_REPLAY=10/10` / `FRESH_ROWS=18/18` / `README_TOKEN_LEGEND_MISMATCH=0` already hold. Round-67's entire calibration delta is therefore `C7_*` plus the C05 flip; nothing else can move the calibration axis this round. This is consistent with claims.md C2 and confirms round-66's labels are purely regression surface.
3. `K_ROW C07 status=held` is unchanged at base and must stay `held` after — it is a no-touch baseline row, not part of the C1 either-way.
4. No tool installs or upgrades were needed or performed (no pacman/uv/npx/`~/.local/bin` writes).

## Scope

Read-only seat. Wrote exactly one file: this report (`/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67CounterReplay.md`). Scratch confined to `/tmp/revenger-r67-seat-counter{,2}` plus `/tmp/run2.log`, `/tmp/run2.err`. No git/jj mutations, no edits under `corpus/`, `reports/`, or the lane index. Did not read or copy any credential material. Network: unused.
