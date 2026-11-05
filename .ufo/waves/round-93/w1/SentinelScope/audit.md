# Round 93 w1 — write-scope and safety audit (SentinelScope)

Lane: /home/vgpnk/Projects/shokunin/revenger-shokunin
Freeze commit: 02050cb2a6758e3bd9cec696ff0e42df6f23511a (HEAD at audit time, unchanged)
Snapshot: wave dir polled 20 times (bounded, 60 s apart; 11 seat dirs and 106 files at the final poll). Audit sweep at ~12:10 -0300 saw 109 files. The wave was NOT complete: ReviewerGate and MutationR93 have no wave dir yet, and ReviewerBlind and ScribeEntry have no seat report yet.

## Verdicts

| # | Check | Verdict |
|---|-------|---------|
| 1 | Lane-tree integrity | PASS |
| 2 | Wave-dir credential scan + out-of-wave write scan | VIOLATION (out-of-wave write, scratch leftover); credential scan PASS |
| 3 | Frozen-file hash check (11 paths) | PASS |
| 4 | Seat-report sweep | VIOLATION (CriticR93 cleanup claim false; ScoutRecord undisclosed write); no installs, no sudo, no pacman, no sysctl |

## 1. Lane-tree integrity — PASS

- `git status --porcelain` → `?? .ufo/waves/round-93/` only. No tracked path is modified or staged.
- `git diff --stat 02050cb2a6758e3bd9cec696ff0e42df6f23511a` → empty (exit 0).
- `git diff --name-only` (working tree vs HEAD) → empty. HEAD = 02050cb.
- `git ls-files --others --exclude-standard` outside `.ufo/waves/round-93/` → empty.
- `reports/round-92/**` has no tracked diff against the freeze.

Note: `reports/round-93/__pycache__/` is gitignored (`.gitignore:2`), so it does not appear in `git status`. It is caught under check 2, not here.

## 2. Wave-dir audit

### 2a. Credential material — PASS (no hits)
Strict pattern set (generic key=value secrets, bearer tokens, AKIA/ASIA, gh[pousr]_, xox*, AIza, PEM private-key header, `op://`, JWT, DB URIs with inline password, session/CSRF cookies): 0 hits across the wave dir (`grep -rPn`, exit 1).

Broad token/cookie/secret word sweep (`grep -rPnic`) hit 13 files. All are non-credential prose:
- `ScoutS136/quote-receipts/raw/S497.body` (12), `ScoutS136/Ecma-335-Augments.md` (12): ECMA-335 "metadata token" spec text.
- `CriticR93/findings.md`, `evidence.md`, `attacks/attacks.py`, `CriticR93.md` (2 each): "token-level" check wording.
- `ExecBattery/canfail.log` (1): "token leg" wording.
- `ConnectorOverlap/measurement.tsv` (1): "coverage token" wording.
No secret values, tokens, cookies, or `op://` references.

### 2b. Out-of-wave writes — VIOLATION (one lane-tree write, one scratch leftover)

**V2-1. Frozen-directory write, gitignored.**
- Path: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-93/__pycache__/c1_k_admit_counter2.cpython-314.pyc` (35538 bytes, mtime 2026-11-05 11:55:15).
- Also created: directory `reports/round-93/__pycache__/` (mtime 11:55:15).
- Why it is a violation: the seat contract allows writes only at named paths. `reports/round-93/**` is frozen. A bytecode cache from importing or running the frozen counter without `-B` is a write into that tree.
- Who wrote it: UNVERIFIED. Attribution is by timestamp only. 11:55:15 falls inside ScoutRecord's window (its wave dir mtime 11:55, scout run ~11:50–11:56). ScoutRecord's report (`ScoutRecord.md`) says it ran the counter only in scratch and does not mention this file. Other seats active at 11:55 (ExecBattery 11:56, CriticR93 11:58) are also possible.
- Impact: gitignored and content-free, so it does not alter any frozen byte (check 3 still matches). It must be deleted before the L1 lands so the landing tree is clean.
- Remediation (for the L1, not this seat): `rm -rf reports/round-93/__pycache__` before landing; run every counter with `python3 -B`.

**V2-2. Scratch not removed (CriticR93).**
- Path: `/fast/scratch/hyaku/revenger-r93/CriticR93` — 28,199 files, 288,600,499 bytes (≈ 275 MiB), last modified 11:56:49.
- Violation: the contract requires scratch deletion before yield. `CriticR93.md` (lines 7–8) says "scratch removed before yield". `CriticR93.md` was written at 11:58:33, so the seat yielded with the scratch still present. The claim is false.
- Remediation: the owning seat (or L1) must `rm -rf` that directory. This seat did not touch it.

**Not a violation — `.jj/` mtimes.** 36 files under `.jj/` are newer than `claims.md`. All stamped 11:42:03–11:42:04, the same second as `freeze-base.txt` and `controls/oracle-opening.log`, which points to the freeze-time jj snapshot. No seat wrote there. Note: there is no mutating-jj violation evidence, but jj-internal mtimes cannot be attributed to a seat from stat alone.

**Not a violation — tracked files newer than claims.md.** `reports/round-93/freeze-base.txt` and `reports/round-93/controls/oracle-opening.log` have mtime 11:42:03, newer than `claims.md` (11:41:50). Both are tracked and byte-identical to the freeze (`git diff` empty; check 3 matches).

**Scan: files written under `$W` only.** The find for lane files newer than `claims.md` excluding `.git`, `.ufo/waves/round-93/`, and `reports/round-93/controls/` returned only the items above (`freeze-base.txt` and the `.jj` store). The find for `corpus/`, `reports/`, `SKILL.md`, `SCORECARD.md`, `LOG.md`, `MANIFEST.json` newer than claims returned only `reports/round-93/**` items already named.

## 3. Frozen-file check — PASS

Freeze-commit bytes (`git show 02050cb:<path>`) compared with working-tree bytes, sha256:

| Path | Result |
|------|--------|
| reports/round-93/claims.md | MATCH 2e980194… |
| reports/round-93/c1_k_admit_counter2.py | MATCH 2a5132d0… |
| reports/round-93/c2_legend_counter2.py | MATCH fba5a58a… |
| reports/round-93/forge_battery.py | MATCH d6e70e52… |
| reports/round-93/controls/battery-full.log | MATCH 91c2ac5d… |
| reports/round-93/controls/battery-v1-only.log | MATCH a2dfe506… |
| reports/round-93/controls/c1v2-do-nothing.log | MATCH 737a531c… |
| reports/round-93/controls/c2v2-do-nothing.log | MATCH d704d90b… |
| reports/round-93/controls/oracle-opening.log | MATCH f68249d4… |
| reports/round-93/controls/selftest-c1v2.log | MATCH 8cc09dfe… |
| reports/round-93/controls/selftest-c2v2.log | MATCH 28361c3f… |

checked=11, drift=0. The `controls/` set is 7 files, as frozen (`git ls-tree`).

The `__pycache__` bytecode (V2-1) is not a frozen path and does not change any frozen byte.

## 4. Seat-report sweep

Seat reports present (8): ConnectorOverlap.md, CriticR93.md, ExecBattery.md, ExecCensus.md, ExecOracle.md, ReviewerErrata.md, ScoutRecord.md, ScoutS136.md.
Not yet present: ReviewerBlind (dir, no .md), ScribeEntry (dir, no .md). Wave dir absent: ReviewerGate, MutationR93 (their scratch dirs exist, so they are presumably still running). This seat: SentinelScope (this file).

| Seat | Installs | sudo/pacman/sysctl | Write-path claim | Scratch cleanup | Finding |
|------|----------|--------------------|------------------|-----------------|---------|
| ConnectorOverlap | none | none | wave dir only | scratch absent | OK |
| CriticR93 | none | none | says "frozen not edited" | **scratch present (275 MiB), claim "removed before yield" false** | VIOLATION V2-2 |
| ExecBattery | none ("installed nothing") | none | wave dir | scratch name absent | OK |
| ExecCensus | none | none | wave dir | own scratch deleted | OK |
| ExecOracle | none | none | wave dir only | scratch absent | OK |
| ReviewerErrata | none | none | wave dir | scratch absent | OK |
| ScoutRecord | none ("no pacman action") | none | says lane file untouched; "reports/round-93 copied to scratch" | scratch absent | **undisclosed write: pyc (V2-1) not in report** |
| ScoutS136 | none | none | "nothing outside my wave dir" | scratch absent | OK (V2-1 not attributable to it by report) |

Grep over all seat reports for `pacman|sysctl|sudo|pip install|uv tool|npm -g|cargo install|apt|brew|curl…|sh` found only "no pacman", "installed nothing", "no tools installed" disclaimers. No seat admits an install, sudo, pacman, or sysctl action.

Scratch root `/fast/scratch/hyaku/revenger-r93/` at audit time: CriticR93 (275 MiB, violation), MutationR93, ReviewerBlind, ReviewerGate, ScribeEntry (active), battery, c1v2, c2v2, l1 (not matched to a wave seat name; L1 or unidentified — not attributable here), SentinelScope (this seat, removed at yield).

## Non-audit observations (for the main agent, out of scope)
- ScoutS136 notes `c1_k_admit_counter2.py` reads receipts from `reports/round-93/quote-receipts/`, which does not yet exist in the lane. The L1 must copy them there. Not a write violation.
- A peer message (S66ReviewerDesign) about `souji-shokunin` round-66 arrived during the poll. It is another repo and another wave. Not acted on, not in scope.

## Required follow-up
1. Before landing: delete `reports/round-93/__pycache__/`; the L1 must not commit it.
2. Delete `/fast/scratch/hyaku/revenger-r93/CriticR93` (or have CriticR93 do it).
3. Re-run checks 1–3 after the L1 lands, and complete check 4 for ReviewerGate, MutationR93, ReviewerBlind, ScribeEntry once they yield (not present at audit time).
