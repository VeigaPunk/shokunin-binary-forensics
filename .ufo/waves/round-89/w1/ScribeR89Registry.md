# ScribeR89Registry — gate registration and mined decision ground (round 89, wave 1)

**Seat:** `ScribeR89Registry` (scribe) · **Lane:** `/home/vgpnk/Projects/shokunin/revenger-shokunin`
**Base:** `2b017fa3c616a84b7b491e3312029fa8a8c076e6` · **Freeze:** `c84339c`
**Axis served:** freshness (C1). **Judged on:** depth, operability.

---

## 0. What this seat did, and what it did not

**Lane writes performed by this seat: none.** After prototyping the registry row,
the M-row and the README index bullets, the L1 (`RevengerR89`) instructed this seat
to stand down ("do NOT write SKILL.md or corpus/README.md … paste it in your wave
report only"), because the L1 was landing both items itself in an honest-stop round
(C1 **MISS**, C2 **KILLED**). The L1's landed bytes are therefore what carries the
registration; this report supplies the **measured limits** that make that
registration honest, plus the receipts behind them.

**Read-only work performed by this seat (all in scratch, all now copied out):**

- re-derived every live census fact independently with the host's own commands;
- measured the frozen gate's four exit legs (0 / 1 / 2 / 64) and its `--selftest`;
- measured the **K04 mixed-state floor** and the **PATH/HOME environment spread**;
- reproduced the **negated-wording false green** (an inverted census scoring
  byte-identically to an honest one);
- reproduced the **cross-file row-key masking** (a row appended to the wrong file
  changes that id's verdict);
- audited the landed `SKILL.md` registry row and the landed `corpus/README.md`
  index against every required field and against the self-assessment checker.

**No package was installed or upgraded.** No pacman transaction was attempted
(the host-wide pacman guard is paused). Tooling used: the system `python3`
(`/usr/bin/python3`, CPython 3.14.8, `PYTHONUTF8=1`, `-B` so no bytecode is written)
and `git` **read-only** (`git diff` / `git status` / `git log` only — no mutating
git or jj command was run, no commit, no push).

---

## 1. Behaviour registered

`corpus/census_reprobe.py` is registered in `SKILL.md` `## Gate registry` as a
**probe-as-gate, experimental and NOT admitted** (landed by the L1 at
`SKILL.md:393–401`). Verbatim field map of the landed row:

| field | value (landed) |
|---|---|
| name | `census_reprobe` (round-89 host-readiness census re-probe, **experimental and NOT admitted** …) |
| kind | probe-as-gate (returns 0/1 and can fail, but is **not** admitted as a gate: `--selftest` never calls `main`; mutants a/c/d/e survive `--selftest`) |
| entry command | `PYTHONUTF8=1 python3 -B corpus/census_reprobe.py --root TREE` (cwd = lane root; `--json` machine form; `--selftest` hermetic legs) |
| verdict map | `0` clean · `1` findings (**one per probe spec, NOT per row** — `CENSUS_STALE_UNFLAGGED = len(findings)`) · `2` could-not-evaluate (census file missing) · `64` usage |
| self-test | `PYTHONUTF8=1 python3 -B corpus/census_reprobe.py --selftest` (spelling `--selftest`) — nine legs, last line `CENSUS_SELFTEST=pass`, exit 0 |
| declared scan contract | last two cells (observed, verdict) of the **last** row carrying each id, across **both** census files; the mint cell is never scored — plus five named measured limitations |
| pinned-value path | instrument sha256 `c3127ffc18a54f85f01e2fb88f50b5db694484588e5b7467ae5567ffdd3b648a` (matches `reports/round-89/instrument-pins.log`); red `reports/round-89/census-red.log` (10 findings, exit 1); after `reports/round-89/c1-after.log` (**2 findings, K04 only — the frozen target 0 was NOT reached**); blind-token control `reports/round-89/junk-control.log` (7); environment `reports/round-89/environment.log` |
| write scope | read-only over the lane tree **and the live host** (PATH lookups, four fixed version commands, `import pwn`, `~/.agents/skills/reverse-engineer-anything`, `~/.omp/agent/mcp.json` — only the `rea` entry's `args`, never `env`); writes nothing, creates no temp tree |
| owner | revenger |

Every required field of the seat contract is present: name, kind, entry command,
verdict map **0/1/2/64**, self-test spelling, pinned-value path, write scope,
owner — plus the extra `declared scan contract` field the sibling
`receipt_sweep` row already uses for named limitations.

## 2. The mined decision ground (§4 error-pattern row)

**`M43`** appended to `SKILL.md` §4 (`SKILL.md:149`); the section heading was
updated `M33–M41 → M33–M43` (one byte-deleted, one byte-added line — the only
non-additive edit in the whole diff). `M43` is the next free M-number: `M42` was
the last row in §4 and `M43` was unused lane-wide (the only prior occurrence is a
wave-draft aside in `.ufo/waves/round-67/adjudication-drafts.md:39`, not a landed
mistake row).

Landed row, verbatim:

> **M43** | marker-vs-truth (a marker count is not a re-verification) | a census
> table whose eighteen rows all read `holds` while ten state host facts this host
> contradicts: the freshness proxy counted the markers (18/18) and never the facts
> | a live re-probe gate over the rows (`corpus/census_reprobe.py`, round 89), and
> any count it prints must name the invoking PATH/HOME — the same tree scores
> 2/8/10 across shells; a lexical re-probe is itself a wording check, so a negated
> census can pass it (round-89 D2) | `reports/round-89/census-red.log`,
> `corpus/lessons/round-89.md`

## 3. README index fix (SM2)

`corpus/README.md` `## Index` now names both unindexed corpus scripts:

- `audit_source_quotes.py` — committed fetch-receipt quote audit
  (`verify` / `chains` / `self-test`); read-only over committed bytes, no network.
- `census_reprobe.py` — host-readiness census re-probe (round 89, experimental,
  NOT admitted: see `SKILL.md` §Gate registry for its measured limits); re-derives
  the 18 census rows from the live host and prints `CENSUS_STALE_UNFLAGGED`.

The **coverage map table was not touched** — the whole README diff is `+5 −0`
lines, all inside the `## Index` bullet list (`git diff 2b017fa3 -- corpus/README.md`).

**Checker result (read-only run of the frozen checker, cwd = lane root):**

```
$ PYTHONUTF8=1 python3 -B corpus/self_assessment_check.py --root . --lane .
SM1=0
SM2=0      <-- was 2 at base
SM3=0
SM4=0
SM5=0
SM6=1      <-- disclosed, not repaired (hardcoded /14 denominator against the 15-row map)
SELF_MISMATCH=1
EXIT=1
```

SM2 dropped **2 → 0**; SM6 stays **1**, as the round declares it (the instrument is
denominator-blind; the fix is routed to a future calibration claim, not made here).

---

## 4. Gates measured (this seat's own runs, frozen bytes untouched)

Instrument bytes re-hashed at measurement time:
`c3127ffc18a54f85f01e2fb88f50b5db694484588e5b7467ae5567ffdd3b648a` — equal to
the pin in `reports/round-89/instrument-pins.log`. `corpus/census_reprobe.py` was
read, never written.

| leg | command | exit | observed |
|---|---|---|---|
| L1 plain, landing tree (this shell: mise-first PATH, node v26.12.0) | `--root <lane>` | 1 | `CENSUS_ROWS=18`, 6 findings, `CENSUS_STALE_UNFLAGGED=6` |
| L2 selftest | `--selftest` | 0 | 9 legs `CENSUS_SELFTEST_*=ok`, last line `CENSUS_SELFTEST=pass` |
| L3 missing tree | `--root <nonexistent>` | 2 | `missing …/corpus/knowledge/seed.md`, `CENSUS_STALE_UNFLAGGED=could-not-evaluate` |
| L4 usage | no args | 64 | usage line on **stderr** |
| L5 plain, landing tree, fnm-first PATH (node v24.21.0) | `--root <lane>` | 1 | `CENSUS_STALE_UNFLAGGED=2` (K04 only) — the L1's `c1-after.log` count |
| L6 plain, **same tree**, mise-first PATH | `--root <lane>` | 1 | `CENSUS_STALE_UNFLAGGED=6` — four extra findings (F06/K02 node+npm) |

**The verdict map is therefore exactly 0/1/2/64 and the `CENSUS_SELFTEST=pass`
spelling is exact** (reproduced byte-for-byte against
`reports/round-89/census-selftest.log`).

## 5. Findings — the limits that make the registration a limit, not a capability

All measured by this seat on scratch copies of the tree; the frozen instrument was
never edited.

1. **K04 mixed-state floor (the reason the frozen target 0 is unreachable).**
   K04 carries two probes over **one** scored string: `ghidra` is on PATH
   (`/usr/bin/ghidra`) while `ida` is absent. The gate requires the string to
   contain `present` and forbid `absent` for the first, and contain `absent` and
   forbid `present` for the second — mutually exclusive on one string.
   Measured over the landing tree with only the K04 row varied:
   * `ghidra present; ida absent` (truthful, both halves) → **2 findings**;
   * `ghidra present; ida not installed` → **1 finding** (ida half unsatisfiable);
   * `ghidra found at /usr/bin/ghidra; ida absent` → **1 finding** (ghidra half
     unsatisfiable — honest synonym wording is rejected, rule 5);
   * base row (`both absent`) → **1 finding**.
   Floor is **1**, reachable only by dropping a true half of the row. Reaching 0
   requires editing the frozen instrument or faking `PATH` — neither is done here.

2. **The count is `len(findings)`, not distinct rows.** One row with two probe
   specs contributes two findings (K04 above). `CENSUS_STALE_UNFLAGGED=2` means
   **one row**, not two. Any prose that calls it a "row count" is wrong; the
   landed registry row says so explicitly.

3. **Negated wording is a false green (D2 class), reproduced.** With only the F08
   row changed, an **honest** row (`present`) and a **lying** row
   (`ghidra not present`) produce **byte-identical stdout**
   (`sha256` of both stdout streams equal; both exit 1 with the same other
   findings). Substring matching cannot see the negation.

4. **Environment-bound verdict (PATH/HOME).** The *same* landing tree scores
   **2** under the fnm-multishell PATH and **6** under the mise-first PATH
   (node v26.12.0 / npm 11.20.0 instead of v24.21.0 / 11.19.0). A count without
   its environment is not a count; the landed row requires `reports/round-89/environment.log`
   to be named with any quoted count.

5. **Cross-file row-key masking (D3 class), reproduced.** The gate keys rows by
   id across **both** census files and takes the **last** occurrence. Appending a
   **stale** F01 row to the *checklist* file (the wrong file for an F id) makes
   F01 mismatch again and moves the tree from 6 → **7** findings. A correction
   placed in the wrong file silently masks the corrected row in the right one.

6. **Honest synonym wording is rejected.** `ghidra found at /usr/bin/ghidra`
   fails the presence rule (the rule wants the literal `present`); the landed
   `## Re-verification 2026-11-04` rows had to use the literal to score.

## 6. Gates and surfaces touched

- **Product bytes written by this seat:** none.
- **Product bytes written by the L1 for this seat's item** (read-only verified by
  `git diff 2b017fa3 -- SKILL.md corpus/README.md`):
  * `SKILL.md` — `+25 −1` in total for the round. This seat's item accounts for:
    one §4 row (M43), the §4 heading range (`M33–M41` → `M33–M43`, the single
    deleted line), and one new `## Gate registry` table block — the
    `census_reprobe` row, 9 field lines plus its table header and separators.
    The remaining `+`-lines in the same diff are the L1's **C2** item
    (`apk_identity_oracle`, a second registry block, 9 field lines) — not this
    seat's byte, reported here only so the diff total is not mis-attributed.
    No other §-byte touched.
  * `corpus/README.md` — `+5 −0`: two index bullets only; the coverage map
    table, the legend, the row-count line and every other byte are unchanged.
- **Files this seat read but did not modify:** `corpus/census_reprobe.py`
  (sha256 re-checked), `corpus/knowledge/seed.md`,
  `corpus/knowledge/2026-10-12-rea-readiness-checklist.md`,
  `corpus/self_assessment_check.py`, `corpus/audit_source_quotes.py`,
  `reports/round-89/*`, `corpus/lessons/round-89.md`.
- **Untracked byte present in the tree at hand-off, not this seat's:** `corpus/__pycache__/census_reprobe.cpython-314.pyc` (untracked in `git status`; this seat ran every invocation with `python3 -B`, so it did not write it). Left in place — deleting another seat's byte is outside this seat's scope; flagged for the L1's cleanup.
- **Scratch:** `/fast/scratch/hyaku/revenger-r89/ScribeR89Registry` — every run
  carried `TMPDIR=` that path; deleted before this report was written, after the
  receipts were copied into the wave report directory.

## 7. Out of scope (not done, deliberately)

- The frozen instrument `corpus/census_reprobe.py` was **not** edited, weakened or
  re-pinned (no post-score instrument repair).
- `corpus/knowledge/seed.md` and `…/2026-10-12-rea-readiness-checklist.md` were
  **not** edited (owned by `ScribeR89Rows`; the L1 landed the append).
- The `corpus/README.md` **coverage map** was not touched.
- No claim of green for C1: the landed tree scores **2 findings** (K04 only) and
  the frozen target was **0** — a **MISS**, recorded as such in
  `corpus/lessons/round-89.md` `## Final measurements`.
- No C2 work: the oracle / F4 / producer-byte-identity question belongs to
  `ExecR89Record`, `ReviewerR89C2` and `CriticR89Claims` (C2 is recorded
  **KILLED** — forged record passes both counters; two producer runs differ at
  byte 20).
- No commit, no push, no mutating git/jj command, no `.ufo/state`, `.scratch`,
  `MANIFEST.json` or sibling-repo write, no `agent://all` message, no pacman
  transaction.

## 8. Artifact paths (all absolute)

Wave report: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-89/w1/ScribeR89Registry.md`

Receipts (this seat's own runs):
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-89/w1/ScribeR89Registry/gate-measurements.log` — the four exit legs + the two PATH variants (L1–L6), with the instrument sha256 line
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-89/w1/ScribeR89Registry/k04-isolation.log` — the four K04 wordings with their finding counts
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-89/w1/ScribeR89Registry/negation-experiment.log` — honest vs lying F08, byte-identity of stdout
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-89/w1/ScribeR89Registry/cross-file-masking.log` — stale row in the wrong file moves the count 6 → 7
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-89/w1/ScribeR89Registry/limits-probe.log` — the first K04 / negation probe pass
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-89/w1/ScribeR89Registry/environment.log` — PATH/HOME/node/npm/rea/ghidra/ida of this measurement environment

Landed product surfaces (L1's bytes, verified read-only by this seat):
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/SKILL.md` — `## Gate registry` row `census_reprobe` (lines 393–401) and §4 row `M43` (line 149)
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/README.md` — `## Index` bullets for `audit_source_quotes.py` and `census_reprobe.py` (lines 19–23)

## 9. Verdict summary

| acceptance item | state |
|---|---|
| one `census_reprobe` registry row with every required field (name, kind, entry command, verdict map 0/1/2/64, self-test spelling, pinned-value path, write scope, owner) | **met** (landed by the L1; every field independently re-derived here) |
| one §4 error-pattern row (M43) | **met** (landed by the L1; M43 is the next free number) |
| README index names `audit_source_quotes.py` and `census_reprobe.py` | **met** (landed by the L1) |
| `self_assessment_check.py` SM2 → 0, SM6 stays 1 | **met** (SM2=0, SM6=1, measured) |
| no other README byte changed | **met** (`+5 −0`, index list only) |
| frozen instrument untouched | **met** (sha256 re-checked equal to the pin) |
| green claim for C1 | **not made** — C1 is a MISS (2 findings, K04 only, target 0) |
