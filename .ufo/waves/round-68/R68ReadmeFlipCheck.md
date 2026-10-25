NOT-MET — 5 of the 9 §C2 conditions read the do-nothing control values right now (`K_HELD_BACKED=8/14`, `K_HELD_BACKED_STRICT=8/14`, `K_ROW C05 status=uncovered`, `C05_SINGLE_V3=no`, `HOLDS_C2_V3=no`) because all five are *computed from the README C05 status cell*, and 2 more (Q01–Q13 wave decisions, the outside-discernment spot-check) have **no artifact on disk yet** — the wave that owns them has not returned a single seat report. The flip-independent conditions (`C7_V3_CLEAN=yes`, `README_TOKEN_LEGEND_MISMATCH=0`, counter exit 0) all hold, and every byte-level assertion §C2 makes about the v3 entry re-derives exactly.

Seat: `L1Revenger68.R68ReadmeFlipCheck` · lane `/home/vgpnk/Projects/shokunin/revenger-shokunin` · measured tip `4232235` (`refs/heads/main`), counter `reports/round-68/measure.py` sha256 `0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766` (matches the frozen pin at `reports/round-68/claims.md:5`). Read-only seat: **no file in the lane was edited**, no git/jj mutation was run.

---

## 1. The README C05 row — exact text and status cell

`corpus/README.md:34` (byte-exact, single line):

```
| C05 | Android packages (APK) | — | `fixtures/apk-r65`; retained rejected candidate `knowledge/round-65-apk-axml-byte-evidence.md` (round-65 orchestrator-dispatched wave, falsified Q02/Q06/Q11, adjudicated round-66) | uncovered |
```

Cell split (`awk -F'|'` on the row, `NF=7`):

- **knowledge column** (`$4`, the cell the counter reads as `l.split("|")[3]`) = ` — ` — an em dash, **no `knowledge/*.md` path at all**
- work-evidence column (`$5`) = `` `fixtures/apk-r65`; retained rejected candidate `knowledge/round-65-apk-axml-byte-evidence.md` (round-65 orchestrator-dispatched wave, falsified Q02/Q06/Q11, adjudicated round-66) ``
- **status cell** (`$6`) = ` uncovered `

So the row is in the pre-flip state exactly as the milestone states: the v3 candidate is **not** named and the status is `uncovered`. `corpus/README.md` is byte-unchanged since the claim base (`git diff --name-only f165908 refs/heads/main -- corpus/README.md` → 0 files).

Legend the row is judged against, `corpus/README.md:21-25`: `held` = at least one admitted knowledge entry covers the ground; `uncovered` = work evidence exists but no admitted entry, and "a rejected candidate retained under `knowledge/` is clearly marked in the file and is not coverage".

## 2. §C2 precondition list, item by item, on the current bytes

Frozen predicate text: `reports/round-68/claims.md` §C2 ("Frozen predicate (pass branch)").

| # | §C2 condition | Required | Measured now | Met? | Evidence |
|---|---|---|---|---|---|
| 1 | `K_HELD_BACKED` | `9/14` | **`8/14`** | **NO** | counter stdout (below); flip-gated |
| 2 | `K_HELD_BACKED_STRICT` | `9/14` | **`8/14`** | **NO** | counter stdout; flip-gated |
| 3 | `K_ROW C05 status` | `held` | **`uncovered`** | **NO** | `corpus/README.md:34`; flip-gated |
| 4 | `C05_SINGLE_V3` | `yes` | **`no`** (`C05_KNOWLEDGE_COLUMN=-`) | **NO** | counter stdout; flip-gated |
| 5 | `README_TOKEN_LEGEND_MISMATCH` | `0` | **`0`** (`rows=[]`) | **YES** | counter stdout |
| 6 | `HOLDS_C2_V3` | `yes` | **`no`** | **NO** | counter stdout; flip-gated |
| 7 | `C7_V3_CLEAN` | `yes`, 17 blocks / 0 problems | **`yes` exit=0 :: checked_blocks=17 problems=0** | **YES** | counter stdout **and** independent run: `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md` → `checked_blocks=17 problems=0`, `ENTRY_EXIT=0` |
| 8 | wave Q01–Q13 decisions on the v3 bytes all PASS | 13/13 (n/a with named reason) | **ABSENT — no artifact exists** | **NO** | `.ufo/waves/round-68/` contains only `build-r68.py`, `build-wave-spec.py`, `wave-spec.json`; `find .ufo/waves/round-68 -name '*.md'` → **empty**; `grep -rl Q01 .ufo/waves/round-68/` hits only the two builder/spec files (no decision record) |
| 9 | outside-discernment spot-check not REJECT | not REJECT | **ABSENT — no artifact exists** | **NO** | same: zero seat reports in `.ufo/waves/round-68/` |
| 10 | counter exit code | `0` | **`0`** | **YES** | `EXIT=0` (below) |

Void-condition guards that §C2/§Void also fence, checked and **all clean**:

- `git diff --stat f165908 refs/heads/main` → 9 files: `build-r68.py`, `corpus/SOURCES.md`, `corpus/check_embedded_outputs.py`, `corpus/derive_axml_anchors.py`, `corpus/knowledge/round-68-apk-axml-byte-evidence.md`, `corpus/snapshots/ResourceTypes.h`, `reports/round-68/{claims.md,measure-before.log,measure.py}` — nothing else.
- `corpus/live/` + `corpus/fixtures/` touched since base: **0 files**.
- round-65 and round-67 rejected candidates touched since base: **0 files** (the r67 `:244` anchor survives verbatim: `RES_XML_START_NAMESPACE_TYPE` :244` → still present, `corpus/knowledge/round-67-apk-axml-byte-evidence.md:1`).
- denominator unchanged: `K_HELD=8/14` over `rows=14`; `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, `FRESH_ROWS=18/18`, `HOLDS_OK_V4/V5/V6=yes`, `STRICT_REJECT_WINDOW_SELFTEST=pass`.

## 3. The counter, run over a scratch tree from `refs/heads/main`

```sh
TREE=$(mktemp -d /tmp/r68-flipcheck-XXXX)
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive refs/heads/main corpus | tar -x -C "$TREE"
cd / && TMPDIR=/tmp/revenger-r68-counter-flip python3 -B \
  /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-68/measure.py "$TREE"
```

Tree: `/tmp/r68-flipcheck-LsrX`. Labels quoted verbatim (the decisive ones):

```
K_HELD=8/14 score=5.7
K_ROW C05 status=uncovered
K_ROW C07 status=held
K_HELD_BACKED=8/14
C05_REJECTED_MARKED=yes
K_HELD_BACKED_STRICT=8/14
C05_KNOWLEDGE_COLUMN=-
C05_SINGLE_V2=no
C05_SINGLE_V3=no
STRICT_REJECT_WINDOW_SELFTEST=pass old_window_miss=True
README_TOKEN_LEGEND_MISMATCH=0 rows=[]
C05_STATUS=uncovered
HOLDS_C2_V3=no
C7_GATE_PRESENT=yes
C7_SELFTEST=pass :: SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
MUTANT check_embedded_outputs.py c7 exit=1 killed :: drifted entry output accepted
C7_RED_ON_R65_CANDIDATE=yes exit=1 :: checked_blocks=15 problems=1
C7_V2_CLEAN=yes exit=0 :: checked_blocks=16 problems=0
C7_V3_CLEAN=yes exit=0 :: checked_blocks=17 problems=0
C7_CONTROL_PASS=1/1
C7_MUTANT_KILLED=1/1
C7_MUTANT_KILLED_ATTRIBUTED=1/1
C7_NEG_SPOOF_KILLED=1/1
C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK_V4=yes
HOLDS_OK_V5=yes
HOLDS_OK_V6=yes
EXIT=0
```

This is the red-before receipt's C7 half inverted (base `f165908` read `C7_MUTANT_KILLED_ATTRIBUTED=0/1`, `HOLDS_OK_V5=no`, `HOLDS_OK_V6=no`), and the C2/README half **unchanged** (`measure-before.log`: `K_HELD_BACKED=8/14`, `C05_STATUS=uncovered`, `C05_SINGLE_V3=no`, `HOLDS_C2_V3=no`) — i.e. C1's axis moved and C2's coverage axis has not, which is correct for a build that must not flip.

## 4. The structural finding: five §C2 conditions cannot be satisfied before the flip

`reports/round-68/measure.py:36-81` derives every README-dependent label from the row's own status cell:

- `:36` `held = [l for l in rows if re.search(r"\| held \|$", l)]` — a row is only counted if it *ends* `| held |`
- `:43` `K_HELD_BACKED` = `held` rows whose **knowledge column** (`l.split("|")[3]`) names existing `knowledge/*.md` files
- `:64` `K_HELD_BACKED_STRICT` = the same minus any row naming a file marked `admission-status: rejected`
- `:76` `C05_SINGLE_V3` = the C05 row's knowledge column holds **exactly one** path, equal to `knowledge/round-68-apk-axml-byte-evidence.md`
- `:116-117` `C05_STATUS` = the row's last-but-one cell; `HOLDS_C2_V3` = `len(backed)==9 and len(strict)==9 and c05_single_v3 and c05_status=="held" and len(mismatch)==0`

Consequence, stated exactly: **items 1–4 and 6 of §2 are post-flip observables, not pre-flip gates.** They read 8/14 / 8/14 / uncovered / no / no on *any* tree where C05 is not yet flipped, including a tree whose entry is perfect. Taken literally as a precondition list, §C2 is circular: nothing can satisfy them without the flip, and the flip (admission order item 3, `claims.md` "flip the affected coverage row only on an all-criteria pass") must not happen without them.

The only coherent reading, and the one I report against, is the one the claims file itself encodes: item 5 (`README_TOKEN_LEGEND_MISMATCH`), item 7 (`C7_V3_CLEAN`), item 10 (exit 0) plus the entry's own byte assertions and the void conditions are the **pre-flip gates**; items 1–4 and 6 are **the flip's own receipt**, to be re-measured at the same final commit that carries the flip. The genuinely outstanding pre-flip gates right now are items **8 (Q01–Q13)** and **9 (spot-check)**, and neither has an artifact on disk.

## 5. What the README row MUST read — only if all preconditions hold

Counter-load-bearing cells are exactly two: the **knowledge column** (`measure.py:76`, `:43`, `:64`) and the **status cell** (`measure.py:36`, `:116`). Minimal exact requirement:

- knowledge column = `` `knowledge/round-68-apk-axml-byte-evidence.md` `` — **exactly one** path, no second `knowledge/*.md` (two paths → `C05_SINGLE_V3=no`), no trailing prose containing another `knowledge/...md` token
- status cell = `held` (the row must still *end* `| held |`; `measure.py:36` anchors on `\| held \|$`)
- the path must go in the **knowledge** column (index 3), not the work-evidence column: `split("|")[3]` only, so a path appended to the fixtures cell reads `C05_SINGLE_V3=no` while *looking* flipped — the one flip error that would silently score 8/14 again

Recommended full row (keeps the r65 precedent, keeps `fixtures/apk-r65`, and names the r67 rejected candidate that the current row omits — column 4 is read by no label, so this is honesty, not scoring):

```
| C05 | Android packages (APK) | `knowledge/round-68-apk-axml-byte-evidence.md` | `fixtures/apk-r65`; retained rejected candidate `knowledge/round-65-apk-axml-byte-evidence.md` (round-65 orchestrator-dispatched wave, falsified Q02/Q06/Q11, adjudicated round-66); retained rejected candidate `knowledge/round-67-apk-axml-byte-evidence.md` (round-67 orchestrator-dispatched wave, Q02 FAIL: `RES_XML_START_NAMESPACE_TYPE` `:244` vs `:245`, adjudicated round-67) | held |
```

After that row lands, the same counter invocation must read `K_HELD_BACKED=9/14`, `K_HELD_BACKED_STRICT=9/14`, `K_ROW C05 status=held`, `C05_SINGLE_V3=yes`, `HOLDS_C2_V3=yes`, `C05_STATUS=held`, `K_HELD=9/14 score=6.4`. Also required in the **same revision**, though no counter label reads it: the entry's `admission-status:` line must move off `candidate` — `corpus/knowledge/round-68-apk-axml-byte-evidence.md:9` currently reads "`admission-status: candidate — … It is NOT admitted: the README C05 row stays uncovered …`", which after a flip would be a README entry that says `held` over a file that says "NOT admitted". The admitted-entry precedent is `corpus/knowledge/round-64-firmware-region-byte-evidence.md:7` (`admission-status: admitted — README C07 flipped to held naming this entry in the round-64 admission revision`).

## 6. §C2's own byte assertions about the v3 entry — all re-derived, all true

§C2 lists six deltas; I checked each against the references (not against the entry's prose):

1. **`:245` in both places** — `RES_XML_START_NAMESPACE_TYPE` is `:245` at `…round-68…md:1` (source header) and `:57` (the chunk-type table, "start/end namespace :245/:246"). The only two surviving `:244` tokens are `:6` (`the round-67 draft's \`:244\` anchor is the M40/M44 class this entry repairs`) and `:9` (the admission-status narration of the repair) — meta-references to the defect, not cited anchors. The r67 candidate still carries the defect verbatim, as the red-before surface must (`…round-67….md:1`, `RES_XML_START_NAMESPACE_TYPE` :244`).
2. **attrExt 686 comment / 687 field** — my own run of the derivation prints `comment attributeStart : 686`, `field attributeStart : 687` (not the r67 range `685-687`).
3. **item 11 embeds the derivation** — `…round-68….md:128` `$ python3 -B corpus/derive_axml_anchors.py`; the command resolves from the tree root and prints **17 lines, exit 0**, first line `sha256 56b88bc4… ResourceTypes.h`, then `struct ResChunk_header : 218` … `enum RES_XML_START_NAMESPACE_TYPE : 245` … `field attributeStart : 687`. Script digest matches S046's pin exactly: `sha256sum corpus/derive_axml_anchors.py` → `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249` = `corpus/SOURCES.md:61`.
4. **snapshot copy byte-exact** — `corpus/snapshots/ResourceTypes.h` sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`, `86255 bytes` — both match `claims.md` §C2 delta 4 and S046.
5. **`admission-status: candidate`** — `…round-68….md:9`, as claimed (see §5 for what the flip must then change).
6. **fixture/oracle/readout unchanged** — `corpus/fixtures/` shows 0 files changed since `f165908`; the entry's `recheck:` digest `507d79f8…` is the round-65 value it claims to preserve.

Also present and matching: `S046` row at `corpus/SOURCES.md:61` (own-work, tier A, `2026-10-24`, registered in the append log at `:99`), and a 13-row `## §Q-map` at `…round-68….md:168` covering Q01–Q13 (Q08 = "superseded by Q11" and Q13 = "n/a by construction" both carry named reasons; Q12 = n/a, no rejected source row). That map is the entry's **claim**, not a decision — §C2 item 8 requires the wave's seats to rule on it, and no seat has ruled.

## 7. Findings outside this seat's claim (for C1's owner and the adjudicator)

- **`SKILL.md` gate-registry row is stale against the landed repair.** `SKILL.md:268` still states, as current truth, "**correction 2026-10-24 (r67 adjudication):** the trailing forged-drift control's marker `drifted entry output accepted` is structurally shadowed by that earlier require and **can never fire** … recorded limitation, reorder fix routed". The repaired gate contradicts this in the same tree: `--self-test` prints `SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired` (exit 0) and the counter reads `C7_MUTANT_KILLED_ATTRIBUTED=1/1` with the marker as the killed run's last line. `SKILL.md` is in **no** round-68 commit (`git log -1 -- SKILL.md` → `712ef61`, the round-67 adjudication; `git status --porcelain SKILL.md` → clean). No counter label reads `SKILL.md`, so this cannot fail C1's predicate — but it is precisely the round-67 M45 class (a registered statement that no longer matches the measured behaviour) recurring on the registry surface, and it is the one place a reader is told the marker is dead.
- `SKILL.md:269` `measured-against` still pins the gate to the round-67 counter `7933c060…`; the round-68 counter is the measuring instrument now.
- Non-blocking observation: invoking the gate with no arguments exits `64` (usage), while the documented verdict map at `SKILL.md:267` lists only `0/1/2`. `64` is a usage error rather than an evaluation verdict, so this is a doc-completeness nit, not a contract breach.

## 8. Verdict and what would change it

**NOT-MET**, unmet items: K_HELD_BACKED (8/14 vs 9/14), K_HELD_BACKED_STRICT (8/14 vs 9/14), C05 status (uncovered vs held), C05_SINGLE_V3 (no vs yes), HOLDS_C2_V3 (no vs yes) — all five flip-gated by construction — plus the two wave-produced conditions with no artifact yet: the Q01–Q13 decisions on the v3 bytes and the outside-discernment spot-check.

Pre-flip gates that are green and need no rework: `README_TOKEN_LEGEND_MISMATCH=0`, `C7_V3_CLEAN=yes (17 blocks, 0 problems)`, counter exit `0`, all retain-holds (`HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, `FRESH_ROWS=18/18`, `HOLDS_OK_V4/V5/V6=yes`), all void guards (no live/fixtures delta, prior rejected candidates byte-unchanged, denominator 14), and every byte assertion §C2 makes about the v3 entry.

The flip becomes legal only when (a) the wave returns PASS on all applicable Q01–Q13 with a non-REJECT spot-check — the only two pre-flip items still missing — and (b) the flip revision writes the knowledge cell exactly as §5 specifies and moves the entry's `admission-status:` off `candidate`. Until then the row must stay exactly as it is at `corpus/README.md:34`.

## 9. Bounds honoured, tooling

No production file was created or modified; the only write is this report. No `git`/`jj` mutation (only read-only `git log/diff/status/archive/rev-parse`), no writes to `corpus/`, `reports/`, `SKILL.md`, `.git`, the fixture/**live** trees, or `shokuknow`. Tool installs: **none** (no pacman/uv/npm/cargo transaction was run this seat).

One observation I did **not** clean up, because it is another seat's artifact and `corpus/` is read-only for me: `git status --porcelain corpus/ reports/ SKILL.md` reports exactly one line, `?? corpus/__pycache__/` — `corpus/__pycache__/check_embedded_outputs.cpython-314.pyc`, mtime `2026-10-25 03:29:00`. It is **not** from this seat: every python invocation I made ran with `-B`, my two in-tree runs (`--entry`, `derive_axml_anchors.py`) ran inside `/tmp/r68-flipcheck-LsrX` (which has no `__pycache__`), and the counter runs from the scratch tree. It means at least one concurrent seat is importing or spawning the gate from the **lane working tree** rather than a scratch tree. It cannot affect any measurement in this report: the counting contract exports `git archive <commit> corpus` (tracked bytes only), and untracked bytecode is not in any commit. Left in place for its owner to remove.

Report: .ufo/waves/round-68/R68ReadmeFlipCheck.md
