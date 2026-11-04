# ScribeR89Rows — round-89 census re-verification (freshness axis)

Seat: `ScribeR89Rows` (scribe, axis: freshness).
Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Scratch (deleted before yielding): `/fast/scratch/hyaku/revenger-r89/ScribeR89Rows`.
Receipt dir: `.ufo/waves/round-89/w1/ScribeR89Rows/`.

## Status

**My item was stood down mid-flight by the lane seat (`RevengerR89`, 2026-11-04):
"Do NOT write corpus/knowledge/* — the L1 is landing the appended re-verification
tables directly (K04 residual 2 accepted) … Do not touch lane files."** I did not
write any lane file. The L1 then landed the two `## Re-verification 2026-11-04`
tables itself (`6ce41aa`, adjudicated `bd575ca`).

I therefore delivered, in place of the landed edit:

1. an independent live re-probe of all 18 census facts (my own commands, not
   copied from the instrument),
2. a scratch prototype of both tables + the gate run over it,
3. an exhaustive proof that the frozen counter's `CENSUS_STALE_UNFLAGGED=0`
   target is unreachable on this host (K04), matching the L1's adjudication,
4. **one new post-landing truth defect the L1's own `holds.log` check cannot
   see** (F02 and F05 verdicts), with a gate-neutral patch — reported, not
   applied, because the lane files were explicitly out of my write scope at
   stand-down.

## Behaviour: what the host actually shows (my own probes)

All 18 facts re-probed on this Linux host, 2026-11-04, with the commands the
frozen instrument uses. Full log: `ScribeR89Rows/live-probes.log`.

| fact | live value observed by me |
|---|---|
| skill dir `*.md` | `HOST-CONTRACT.md`, `SKILL.md` (backups/recoveries excluded) |
| `references/*.md` | 7: android-applications, cli-command-map, connection-and-recovery, evidence-workflows, javascript-applications, native-and-artifacts, runtime-observation |
| SKILL.md frontmatter | `version: "42"`, `tool_count: 207` |
| `rea` | **present** on PATH, `rea --version` → 6.7.0 |
| `ghidra` | **present**, `/usr/bin/ghidra` |
| `jadx` / `binwalk` / `unblob` | present, 1.5.6 / 3.1.0 / 26.6.4 |
| `ida` | **absent** (no output, exit 1; no `ida*` binary anywhere on PATH or in `/usr/bin`, `/usr/local/bin`, `~/.local/bin`, `/opt`) |
| `import pwn` | **imports**, `/usr/lib/python3.14/site-packages/pwn/__init__.py` |
| node / npm | v24.21.0 / 11.19.0 |
| skill pin | `rea-agents@6.7.0` (SKILL.md lines 33, 37, 82, 83, 102-104) |
| `~/.omp/agent/mcp.json` `rea` args | `["-y", "rea-agents@6.7.0", "mcp"]` |
| unzip / zipinfo | UnZip 6.00 / ZipInfo 3.00 |

Every live value I derived independently matches the value the L1's landed
tables state in their observed columns. I found no disagreement between my
probes and the landed observations.

## Gate runs (both, over the lane tree)

Base — `git archive 2b017fa3 corpus/knowledge` extracted to scratch:
`ScribeR89Rows/gate-run-base.txt`

```
CENSUS_ROWS=18
CENSUS_MISMATCH F01 listing:skill_dir does not state live value 'HOST-CONTRACT.md'
CENSUS_MISMATCH F03 listing:references does not state live value 'android-applications.md'
CENSUS_MISMATCH F04 presence:rea does not state live value 'present'
CENSUS_MISMATCH F07 mcp:rea does not state live value 'rea-agents@6.7.0'
CENSUS_MISMATCH F08 presence:ghidra does not state live value 'present'
CENSUS_MISMATCH F12 import:pwn does not state live value 'imports'
CENSUS_MISMATCH K01 presence:rea does not state live value 'present'
CENSUS_MISMATCH K03 mcp:rea does not state live value 'rea-agents@6.7.0'
CENSUS_MISMATCH K04 presence:ghidra does not state live value 'present'
CENSUS_MISMATCH K05 import:pwn does not state live value 'imports'
CENSUS_STALE_UNFLAGGED=10
EXIT=1
```

Landed tree (working tree at `bd575ca`, the adjudication tip):
`ScribeR89Rows/gate-run-landed.txt`

```
CENSUS_ROWS=18
CENSUS_MISMATCH K04 presence:ghidra states 'absent' against the live value
CENSUS_MISMATCH K04 presence:ida states 'present' against the live value
CENSUS_STALE_UNFLAGGED=2
EXIT=1
```

`10 → 2`; the residual is exactly the K04 pair, and the frozen target `0` is
**not** reachable on this host. The target was already adjudicated MISS by the
L1 before my stand-down; I independently reproduce and confirm that verdict.

## Finding 1 — K04 is structurally unsatisfiable (confirms the L1's MISS)

`K04` scores **one shared text** (its observed + verdict cells) against two
mutually exclusive presence probes:

* `presence:ghidra` — ghidra is on PATH → token `present` required, `absent` **forbidden**;
* `presence:ida` — ida is off PATH → token `absent` required, `present` **forbidden**.

One string cannot both contain and not contain the same token. Enumerated
exhaustively over every truth-relevant combination
(`ScribeR89Rows/k04-floor-proof.log`, `k04-phrasing-matrix.log`):

| K04 cell text | findings |
|---|---|
| `ghidra present at /usr/bin/ghidra; ida absent` (the landed, truthful-literal row) | **2** |
| `ghidra present at /usr/bin/ghidra; ida not on PATH` | 1 (ida leg: does-not-state) |
| `ghidra installed at /usr/bin/ghidra; ida absent` | 1 (ghidra leg: does-not-state) |
| `ghidra is installed; ida is not installed` | 2 |
| `ghidra present at /usr/bin/ghidra` (ida dropped) | 1 |
| `ida absent` (ghidra dropped) | 1 |
| `present absent present absent` (junk-control style) | 2 |

**Floor is 1, and reaching 1 requires dropping or rewording one of the two
truths** — the instrument's literal-token rules cannot credit a row that
truthfully states a mixed state. The truthful-literal row costs 2. This matches
the L1's adjudication wording ("floor 1 only by non-literal wording, truthful-
literal 2") and the independent observations of `RevengerR89` and
`CriticR89Claims`. The K04 row as landed states both truths; I did not touch it
and do not recommend touching it.

## Finding 2 — NEW: F02 and F05 verdicts contradict their own recorded cell

This is a **post-landing** defect, not present in the base tree. It is a truth
defect on my axis and it is invisible to the frozen counter, which is why the
L1's `reports/round-89/holds.log` check did not catch it: that receipt only
`grep -c`s how many rows carry a `holds`/`STALE` marker, it never checks that
a `holds` verdict is **true**.

The landed `## Re-verification 2026-11-04` preamble defines its own rule:

> the observed column is its output on this host, and the verdict states the
> current value. `holds` means the recorded value still matches.

Two rows violate that rule:

```
| F02 | SKILL.md version 37, tool_count 170 (`:5`) | `sed -n 1,8p …/SKILL.md` | version 42, tool_count 207 | holds |
| F05 | acquisition pin `npx -y rea-agents@6.4.0` (`:8`) | `grep -n 'rea-agents@' …/SKILL.md` | `rea-agents@6.7.0` | holds |
```

* **F02** — recorded cell: version 37 / tool_count 170. Live: 42 / 207. The
  recorded value does **not** still match, so the verdict must be
  `STALE -> 42 / 207`, not `holds`.
* **F05** — recorded cell: acquisition pin `rea-agents@6.4.0`. Live pin:
  `rea-agents@6.7.0`. Same conclusion: `STALE -> 6.7.0`, not `holds`.

Two independent cross-checks confirm the recorded cell really is the *mint*
record, not the previous table's observation:

1. **The `:N` citations resolve into the 2026-10-12 mint census block.**
   `:5` → seed.md line 10 (`SKILL.md (version 37, tool_count 170 declared) + references/`);
   `:8` → seed.md line 13 (`- NO `rea` CLI on PATH; acquisition path per skill: `npx -y rea-agents@6.4.0``).
   Full map: `ScribeR89Rows/f02-f05-citation-map.log`.
2. **The file contradicts itself.** The 2026-10-19 table, for the *same*
   recorded cell and the *same* live values, already ruled these two facts
   STALE — `F02 … STALE → 42 / 207` and `F05 … STALE → 6.7.0` — while every
   other mint-vs-live divergence in the new table (F01, F03, F04, F06–F12,
   K01–K05) is marked STALE. F02 and F05 are the only two rows marked `holds`
   whose recorded value the host contradicts.

The alternative reading — "recorded" = the 2026-10-19 table's observation —
does not survive contact with the same file: under it F06 (2026-10-19 observed
`v24.21.0, 11.19.0`, live identical) would have to be `holds`, and the landed
table marks it `STALE`. So the mint-record reading is the file's convention,
and F02/F05 are the anomalies.

**Detector** (`ScribeR89Rows/detect_false_holds.py`, re-derives the live value
with the frozen instrument's own `live()` and compares it to the recorded cell
literally): on the landed tree it reports exactly **2** false-holds rows
(F02, F05); on the corrected copy it reports **0**
(`detect_false_holds.log`, `detect_false_holds_after_fix.log`). The checklist
file is clean — K06's `holds` is correct (mint said "archive tools present",
live confirms UnZip 6.00 / ZipInfo 3.00).

**The fix is gate-neutral** — it changes no scored token, so
`CENSUS_STALE_UNFLAGGED` stays 2 and the K04 residual is untouched:

`ScribeR89Rows/false-holds-fix.patch`

```diff
-| F02 | SKILL.md version 37, tool_count 170 (`:5`) | `sed -n 1,8p …/SKILL.md` | version 42, tool_count 207 | holds |
+| F02 | SKILL.md version 37, tool_count 170 (`:5`) | `sed -n 1,8p …/SKILL.md` | version 42, tool_count 207 | STALE -> 42 / 207 |
-| F05 | acquisition pin `npx -y rea-agents@6.4.0` (`:8`) | `grep -n 'rea-agents@' …/SKILL.md` | `rea-agents@6.7.0` | holds |
+| F05 | acquisition pin `npx -y rea-agents@6.4.0` (`:8`) | `grep -n 'rea-agents@' …/SKILL.md` | `rea-agents@6.7.0` | STALE -> 6.7.0 |
```

**Status: reported, NOT applied.** At stand-down the lane seat forbade me from
writing `corpus/knowledge/*` and the lane was already adjudicated
(`bd575ca`). This is a decision for the L1: land the two-line verdict
correction (it is gate-neutral and restores the table's own stated rule), or
record it as a known residual. I did not apply it unilaterally.

## Gates and checks I ran

| check | result |
|---|---|
| frozen gate over base archive | `CENSUS_STALE_UNFLAGGED=10`, exit 1 — reproduces `reports/round-89/census-red.log` exactly (same 10 ids) |
| frozen gate over landed tree | `CENSUS_STALE_UNFLAGGED=2`, exit 1 (K04 only) |
| frozen gate over my scratch prototype | `CENSUS_STALE_UNFLAGGED=2`, exit 1 (K04 only) — my tables scored identically to the L1's |
| gate over F02/F05-corrected copy | `CENSUS_STALE_UNFLAGGED=2`, exit 1 — fix is gate-neutral |
| `git diff --stat c84339c` on the two census files | `21 +++` / `28 +++`, **0 deletions** — earlier tables byte-identical, additions only |
| `git diff 2b017fa3 c84339c -- corpus/knowledge` | empty — earlier tables byte-identical across the freeze |
| false-holds detector, landed tree | 2 rows (F02, F05) |
| false-holds detector, corrected copy | 0 rows |

## Touched surfaces

**Written by me — only my own wave dir and this report:**

* `.ufo/waves/round-89/w1/ScribeR89Rows.md` (this file)
* `.ufo/waves/round-89/w1/ScribeR89Rows/` — `live-probes.log`,
  `gate-run-base.txt`, `gate-run-landed.txt`, `prototype-gate-run.txt`,
  `prototype-seed.md`, `prototype-checklist.md`, `build.py`,
  `k04_proof.py`, `k04-floor-proof.log`, `k04-phrasing-matrix.log`,
  `holds-convention-audit.log`, `f02-f05-citation-map.log`,
  `detect_false_holds.py`, `detect_false_holds.log`,
  `detect_false_holds_after_fix.log`, `false-holds-fix.patch`

**Not touched by me:** `corpus/knowledge/*` (stood down before any write),
`reports/round-89/claims.md`, `corpus/census_reprobe.py`, `MANIFEST.json`,
`.ufo/state/`, `.scratch/`, any sibling repo, any `.ufo/` file outside my own
wave dir. No commit, no push, no mutating git/jj command, no service restart.

## Out of scope (not touched, not claimed)

* C2 coverage (android family record, F4, ORACLE) — another seat's axis.
* The frozen counter's K04 design — a frozen predicate; I did not edit it and
  do not recommend editing it for this round.
* `corpus/live/runs/round-89/**` and the adjudication's rejection of the
  android record.
* Every claim, knowledge admission and map row — untouched.

## Tooling

**No installs, no upgrades, no tool changes were performed this round.** Every
command used was already present (`python3` 3.14, coreutils `ls`/`grep`/`sed`,
`node` v24.21.0, `npm` 11.19.0). `/home/vgpnk/.omp/agent/RULES.md` was read
first; its pacman guard was never invoked because no install was needed. No
`uv tool`/`npx`/`~/.local/bin` writes.

## Known limits of this report

* The `holds` convention for F02/F05 is my reading of the table's own
  preamble plus the `:N` citation map; the alternative reading is disproved by
  F06 (shown above), but the L1 may hold that a `holds` verdict there was
  intended to mean "unchanged since 2026-10-19". If so, the defect is
  *wording*, not truth — but as landed, the two tables give the same
  (recorded, observed) pair opposite verdicts, which is inconsistent under any
  reading.
* I could not observe whether the L1 will land the patch; I did not apply it.
* K04 reachability is proven over the token alphabet that matters
  (`present`/`absent`); a row that avoided both literals would score 2, not 0,
  so 0 remains unreachable regardless of wording.
