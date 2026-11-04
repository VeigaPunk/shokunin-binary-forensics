# ReviewerR89C1 — C1 freshness attack (revenger round-89, attempt 1)

- Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`
- Base: `2b017fa3c616a84b7b491e3312029fa8a8c076e6`; freeze commit `c84339c`
- Instrument under attack: `corpus/census_reprobe.py`, sha256
  `c3127ffc18a54f85f01e2fb88f50b5db694484588e5b7467ae5567ffdd3b648a`
  (matches `reports/round-89/instrument-pins.log`)
- Host: linux 7.2.11-arch1-1, 2026-11-04. Nothing installed or upgraded (no
  tool/version/channel to record); no pacman transaction attempted.
- Scratch: `/fast/scratch/hyaku/revenger-r89/ReviewerR89C1` (deleted after
  receipts were copied here). Every command below was run with
  `TMPDIR=/fast/scratch/hyaku/revenger-r89/ReviewerR89C1`.
- I edited no instrument and no lane file. All trees under attack are copies in
  scratch; `corpus/census_reprobe.py` was read, never written.

Canonical invocation for every score in this report:

```
TMPDIR=/fast/scratch/hyaku/revenger-r89/ReviewerR89C1 PYTHONUTF8=1 \
  python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/census_reprobe.py --root <TREE>
```

Base tree extraction:

```
cd /home/vgpnk/Projects/shokunin/revenger-shokunin && \
  git archive 2b017fa3 corpus/knowledge | tar -x -C <scratch>/base
```

## Verdict summary

| # | Finding | Verdict | Severity |
|---|---|---|---|
| A1 | Red receipt reproduces byte-identically (10, exit 1, same 10 ids) | AGREE | — |
| A2 | Selftest receipt reproduces byte-identically (9 legs, pass, exit 0) | AGREE | — |
| A3 | Blind-token control reproduces (7; 15 if absence tokens are padded — still nonzero) | AGREE | — |
| A4 | Six of the ten mismatches re-derived by hand from the live host | AGREE | — |
| A5 | Exit semantics 0 / 1 / 2 / 64 | AGREE | — |
| D1 | K04 is unsatisfiable under the frozen rules on this host → target `0` is **unreachable**; floor is 1 | DISAGREE | blocker (claim MISS) |
| D2 | False green: a tree asserting the **opposite** of every fact scores byte-identically to a fully honest tree | DISAGREE | high |
| D3 | False green: rows are not attributed to their file (`ROWS[rid][0]` unused); corrected F rows in the checklist mask stale seed rows | DISAGREE | medium |
| D4 | False red + reproducibility: every live fact is PATH/HOME-dependent; the same tree scores 2 or 10 or 8 | DISAGREE | high |
| D5 | The counter counts probe findings, not rows, contradicting the frozen predicate sentence | DISAGREE | medium |
| D6 | An honest row without the literal token is rejected (`on PATH at /usr/bin/ghidra`) | declared rule, not an instrument defect | low / calibration |
| D7 | Kill rule (a) does not exercise the opposite rule at all; `--selftest` never touches the scored surface | DISAGREE | high |

## AGREE — reproductions

### A1. Red receipt

```
$ python3 -B corpus/census_reprobe.py --root base
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

`diff` against `reports/round-89/census-red.log`: empty (byte-identical). The
base claim of 10, the ten ids and exit 1 all hold. A do-nothing control fails,
as declared.

### A2. Selftest receipt

`--selftest` prints the same nine lines as `reports/round-89/census-selftest.log`
(`clean` + 8 plants, `CENSUS_SELFTEST=pass`, exit 0), byte-identical. The legs
run; what they cover is D7.

### A3. Blind-token control

Padded every row's last cell with every live positive token
(`HOST-CONTRACT.md SKILL.md 42 207` + the seven reference names + `present`
`rea-agents@6.7.0 24.21.0 11.19.0 imports 6.00 3.00`):

```
CENSUS_MISMATCH F01 ... names absent entries android-applications.md, ...
CENSUS_MISMATCH F03 ... names absent entries host-contract.md, skill.md
CENSUS_MISMATCH F08 ... states 'absent' against the live value
CENSUS_MISMATCH F12 ... states 'ModuleNotFound' against the live value
CENSUS_MISMATCH K04 presence:ghidra states 'absent' against the live value
CENSUS_MISMATCH K04 presence:ida states 'present' against the live value
CENSUS_MISMATCH K05 ... states 'fails' against the live value
CENSUS_STALE_UNFLAGGED=7   EXIT=1
```

Exactly the frozen 7 and the same ids. A stronger variant that also pads the
absence token `absent` scores 15 (F04/F09/F10/F11/K01 additionally bite on the
forbidden word) — nonzero either way, so the rule's intent survives.

### A4. Hand re-derivation (six of the ten)

```
$ command -v rea            -> /run/user/1000/fnm_multishells/1981588_1793727763382/bin/rea (rc=0)
$ rea --version             -> 6.7.0
$ command -v ghidra         -> /usr/bin/ghidra (rc=0);  command -v ida -> (none), rc=1
$ python3 -c 'import pwn'   -> imports ok /usr/lib/python3.14/site-packages/pwn/__init__.py (rc=0)
$ jq .mcpServers.rea.args ~/.omp/agent/mcp.json -> ["-y","rea-agents@6.7.0","mcp"]
$ ls ~/.agents/skills/reverse-engineer-anything/*.md -> HOST-CONTRACT.md, SKILL.md
$ ls .../references/*.md    -> 7 names (android-applications.md, cli-command-map.md,
                               connection-and-recovery.md, evidence-workflows.md,
                               javascript-applications.md, native-and-artifacts.md,
                               runtime-observation.md)
$ node --version; npm --version -> v24.21.0 / 11.19.0
$ sed -n 1,8p .../SKILL.md  -> metadata.version "42", tool_count 207
$ unzip -v | head -1        -> UnZip 6.00 ...;  zipinfo -v | head -1 -> ZipInfo 3.00 ...
```

F04/K01 (rea present, 6.7.0), F07/K03 (`rea-agents@6.7.0`), F08/K04 (ghidra
present), F12/K05 (pwn imports), F01 (`HOST-CONTRACT.md` is a live entry), F03
(seven reference names, not six) all contradict the stored rows as the gate
says. The red is real; the stored census is genuinely stale.

### A5. Exit semantics

`--root` absent → exit 64 with the usage line; `--root <nonexistent>` →
`missing …/seed.md`, `CENSUS_STALE_UNFLAGGED=could-not-evaluate`, exit 2;
0 findings → 0; >0 → 1. As declared.

### A6. Lane worktree state at review time

`corpus/knowledge/seed.md` and `…/2026-10-12-rea-readiness-checklist.md` are
byte-identical to the `2b017fa3` archive (`sha256 d1d31602…` / `561327fa…`),
no `## Re-verification 2026-11-04` section exists, and `git status --porcelain
-- corpus/knowledge corpus/census_reprobe.py` is empty. The rows had not landed
when I polled, so the lane scores the **base state**:

```
$ python3 -B corpus/census_reprobe.py --root /home/vgpnk/Projects/shokunin/revenger-shokunin
CENSUS_STALE_UNFLAGGED=10   EXIT=1
```

## DISAGREE — findings

### D1 (blocker). K04 is unsatisfiable: the frozen target `0` cannot be reached

`ROWS["K04"] = [("presence","ghidra"), ("presence","ida")]`. Both probes are
scored against **one** `scored_text(line)` (the last two cells). On this host
`live(("presence","ghidra"))` is `tokens=['present'], forbidden=['absent']` and
`live(("presence","ida"))` is `tokens=['absent'], forbidden=['present']`. A row
must therefore contain `present` and not `absent` (ghidra) **and** contain
`absent` and not `present` (ida). No string satisfies both. The contradiction
is structural, not a wording problem: it holds for any mixed-state pair and
flips with the host (if ghidra were absent and ida present, the same
exclusivity applies).

Empirical floor, on an otherwise fully corrected tree (all 18 rows rewritten
with the live values, appended as a `## Re-verification 2026-11-04` table):

| K04 wording | score | findings |
|---|---|---|
| both halves literal: `ghidra present at /usr/bin/ghidra; ida absent (…)` | `CENSUS_STALE_UNFLAGGED=2` exit 1 | K04 ghidra, K04 ida |
| ghidra literal, ida in prose: `… ida: command -v ida prints nothing (no entry)` | `CENSUS_STALE_UNFLAGGED=1` exit 1 | K04 ida |
| ida literal, ghidra in prose: `ghidra: /usr/bin/ghidra exists; ida absent (…)` | `CENSUS_STALE_UNFLAGGED=1` exit 1 | K04 ghidra |
| both halves in prose | `CENSUS_STALE_UNFLAGGED=2` exit 1 | both |

**Minimum residual = 1** (one row, K04), and that minimum is only reachable by
phrasing one half of the row without the literal token — i.e. by taking the
honest-wording rejection of D6. Literal honesty costs 2. **0 is unreachable**
while the host has ghidra present and ida absent, without editing the
instrument (forbidden by the no-harm statement) or mutating the host
(installing `ida` or removing `ghidra` — out of scope for a census round).

Consequence for the frozen claim: C1's target `CENSUS_STALE_UNFLAGGED=0` is a
**MISS** as frozen. The correct disposition is to record the named limit (the
K04 rule pair is mutually exclusive; floor 1) rather than to reach 0 by any
text trick. I did not repair the instrument and I did not attempt a homoglyph
or zero-width escape; both would be text gaming.

### D2 (high). False green: an inverted census scores identically to an honest one

Built `opposite/` from the same base archive: every one of the 18 rows contains
every live token, and every row's scored cells assert the **opposite** state
using negation that avoids the single forbidden literal:

```
| F04 | … | not present - `command -v` prints nothing | nothing found 2026-11-04 |
| F08 | … | not present - prints nothing | nothing found 2026-11-04 |
| F12 | … | imports? no - raises ImportError | does not import 2026-11-04 |
| K05 | … | jadx, binwalk, unblob not present; imports? no - ImportError | nothing found |
| F03 | … | none of android-applications.md, … exists | directory empty 2026-11-04 |
| F02 | … | not version 42 and not tool_count 207 - SKILL.md declares 37 / 170 | wrong |
| F07 | … | `rea-agents@6.7.0` is the published package, not this host entry; no `rea` key | not registered |
```

```
$ diff score-honest.log score-opposite.log   ->  (empty)
HONEST  : CENSUS_STALE_UNFLAGGED=2  exit 1  ids=[K04, K04]
OPPOSITE: CENSUS_STALE_UNFLAGGED=2  exit 1  ids=[K04, K04]
```

Byte-identical stdout. Fourteen of eighteen rows are inverted with **zero**
effect on the counter. Cause: `forbidden` is at most one literal word per probe
(`absent` for a present tool, `fails`/`ModuleNotFound` for a working import),
and the check is a substring test; `not present`, `imports? no`, `raises
ImportError`, `not found`, `not registered`, `not 24.21.0` all pass. The frozen
predicate says a row mismatches iff it "fail[s] to state the live value … (or
state[s] its opposite)" — the implementation only detects the opposite when it
is spelled with the one forbidden word. **The gate is not the predicate.**

This is the answer to the false-green question: yes, the frozen rules admit a
false green, and it is not a corner case — it is the whole row population.

### D3 (medium). False green: a row is accepted from the wrong document

`check_rows` builds one `lines` dict keyed by row id from both files, and
`key` from `ROWS[rid][0]` is never used; the checklist is read after the seed,
so a checklist line wins any collision. Appending the **corrected F rows to
`2026-10-12-rea-readiness-checklist.md`** while `seed.md` keeps its stale text:

```
$ python3 -B corpus/census_reprobe.py --root frows-in-check
CENSUS_MISMATCH K01 … / K03 … / K04 … / K05 …
CENSUS_STALE_UNFLAGGED=4   EXIT=1
```

versus 10 for the same tree under a copy that enforces per-file attribution
(`lines[(key, rid)]`). So `seed.md` can still read "NO `rea` CLI on PATH",
"Host engines ABSENT … ghidra", "pwntools import fails" — the human-facing
census — while the counter reports 4. The reverse placement (K rows in the
seed) does not mask, because the checklist is read last
(`score-misplaced: CENSUS_STALE_UNFLAGGED=10`).

The docstring does not declare this, so it is not a declared rule; it is an
unimplemented constraint. It matters for the landing only in that a correction
written into the wrong file would be silently accepted.

### D4 (high). False red and non-reproducibility: every live fact is environment-relative

`live()` reads `shutil.which`, `subprocess` PATH lookups, `Path.home()`-rooted
`SKILL.md`/`mcp.json`. The census facts are therefore facts about *the
invoking shell*, and the claim declares no runner environment.

```
$ env -i HOME=$HOME PATH=/usr/local/bin:/usr/bin:/bin python3 -B corpus/census_reprobe.py --root base
CENSUS_STALE_UNFLAGGED=16   EXIT=1
   (F04/K01 rea absent, F06/K02 node 26.12.0 npm 12.2.1, F11/K05 unblob absent, plus the 10)
$ env -i HOME=$HOME PATH=/usr/local/bin:/usr/bin:/bin python3 -B corpus/census_reprobe.py --root honest
CENSUS_STALE_UNFLAGGED=10   EXIT=1
$ env -i HOME=<empty> PATH="$PATH" python3 -B corpus/census_reprobe.py --root honest
CENSUS_STALE_UNFLAGGED=8    EXIT=1
```

Provenance of the lane's live values:

```
rea    -> /run/user/1000/fnm_multishells/1981588_1793727763382/bin/rea   (fnm per-shell shim)
node   -> same fnm multishell dir      npm -> same
unblob -> /home/vgpnk/.local/bin/unblob
ghidra -> /usr/bin/ghidra   jadx -> /usr/bin/jadx   binwalk -> /usr/bin/binwalk   ida -> (none)
```

So the red `10` and the target `0` are both conditional on the lane's
interactive PATH: a fully honest corrected tree scores **10** under a clean
PATH — the same number the stale base scores under the lane PATH. The counter
cannot be quoted without the environment, and a landing verified in one shell
is not verified in another. `fnm_multishells/<pid>_<ts>` is per-session, so the
`rea` presence fact is not even stable across shells of the same host. This is
the freshness axis biting the instrument itself: it re-derives host facts
without pinning which host view it re-derives them from.

### D5 (medium). The counter counts probe findings, not rows

`CENSUS_STALE_UNFLAGGED = len(findings)`, and findings are appended per probe
spec, not per row. Measured:

| tree | findings | distinct mismatching rows |
|---|---|---|
| base (lane PATH) | 10 | 10 |
| honest (all 18 corrected) | 2 | 1 (K04) |
| base (clean PATH) | 16 | 14 |
| junk control | 7 | 5 |

The frozen predicate sentence says "`CENSUS_STALE_UNFLAGGED` is the count of
such rows". For the base it coincides; for the target it cannot, and D1's floor
of 1 row is 2 findings if the row is written literally. A closure that quotes
"CENSUS_STALE_UNFLAGGED=0 rows" is quoting a quantity that is not a row count.

### D6 (low / calibration). Honest wording is rejected — declared, but it is a second divergence from the predicate

```
$ … --root honest-wording      # F08: "on PATH at /usr/bin/ghidra | current 2026-11-04"
CENSUS_MISMATCH F08 presence:ghidra does not state live value 'present'
CENSUS_STALE_UNFLAGGED=3   EXIT=1     (F08 + the two K04 probes)
```

`on PATH at /usr/bin/ghidra` **does** state the live value, so under the frozen
predicate sentence it should not mismatch; the gate rejects it because the
docstring declares "presence live on PATH -> must contain `present`". Verdict:
**declared rule, not an instrument defect** — the gate is a literal-token
checker by design, and the landing must use the literal words
`present` / `absent` / `imports`. But the claim's one-sentence predicate
("fail to state the live value … or state its opposite") is not what the code
measures in either direction: it is too permissive about negation (D2) and too
strict about synonymy (D6). Any closure text should quote the token rule, not
the predicate sentence.

### D7 (high). Selftest: the opposite rule has no leg, and the scored surface is untested

Mutation battery on scratch copies (`mut-*.py`); each mutation is applied to a
copy, the real instrument is untouched. "caught" = a leg turns `=FAIL`.

| mutation | selftest | caught |
|---|---|---|
| M1 `len(hit) >= 1` → `== 1` | pass | no (each plant does yield exactly one finding — the docstring's "exactly one" holds today, the assertion is only weaker) |
| M2 `main` prints `CENSUS_STALE_UNFLAGGED=0` and returns 0 | pass | **no** — and the base tree then prints `CENSUS_STALE_UNFLAGGED=0`, exit 0 |
| M3 presence `forbidden` emptied | pass | **no** |
| M3b `bad = []` (the whole forbidden branch dead) | pass | **no** |
| M4 phantom check removed | FAIL `listing-phantom` | yes |
| M5 missing-token check dead | FAIL 5 legs | yes |
| M6 `scored_text` returns the whole line | FAIL `clean` | yes (K01's `mint ABSENT` canary) |
| M6b `scored_text` returns the last 3 cells | FAIL `clean` | yes |
| M7 per-file attribution enforced | pass | **no** |

Code-path census of the 8 plants: `presence-unstated`, `version-missing`,
`mcp-missing`, `skill-missing`, `pin-missing` → 5 legs on the **missing-token**
path. `listing-phantom` → 1 leg on the phantom path. `presence-opposite`
(`now absent`) and `import-opposite` (`import fails`) are *named* opposite but
both fire on the missing-token path first (`present` / `imports` is absent from
their scored text), so **zero legs exercise the forbidden branch**. M3 and M3b
prove it: the rule the docstring calls "must not state its opposite" — the only
rule that could have caught D2 — is unverified by kill rule (a). Two legs also
share one code path by construction (the five missing-token legs).

M2 shows the stronger gap: `--selftest` never calls `main`, so the printed
count and the exit code — the entire scored surface of C1 — are unconstrained
by the hermetic leg set. Only the separate receipts (base must be 10, junk must
be 7) constrain them, and those are re-runs of the same file rather than
assertions inside it.

## False greens and false reds the frozen rules admit

- **False green (admitted, demonstrated):** a census whose scored cells assert
  the opposite of every live fact, phrased with negation that avoids the one
  forbidden literal (`not present`, `imports? no`, `raises ImportError`, `not
  found`, `not registered`), scores byte-identically to the honest correction
  (`=2`, K04 only).
- **False green (admitted, demonstrated):** a corrected row placed in the
  *other* census file is accepted; the stale row in its own file is never read.
- **False red (admitted, demonstrated):** an honest row stating the live value
  without the literal token (`on PATH at /usr/bin/ghidra`) is rejected — by
  declared rule.
- **False red (admitted, demonstrated):** the same honest tree scores 2, 8 or
  10 depending on the invoking PATH and HOME; a correct row becomes a mismatch
  under a clean PATH.
- **Not admitted:** inserting every live token (7 / 15), doing nothing (10),
  moving rows between files in the K→seed direction (10).

## Residual risk and verification gaps

- The headline is D1: **C1 cannot reach 0**. Unless the closure edits the
  instrument or mutates the host, the landing will score ≥1 on K04 alone, and
  the honest-literal landing will score 2. The claim should be recorded as a
  MISS with the K04 exclusivity as the named limit.
- D4 means any quoted number must name the environment. I verified two PATHs
  and two HOMEs; I did not verify Windows-layout behaviour (the claim calls it
  historical) or a host where `ida` is present (which would flip the K04 pair
  but not remove the exclusivity).
- I did not exercise C2 (`f_probe4.py`, `oracle_check.py`); out of scope here.
- I did not test `--json` consumers beyond confirming its shape and exit code.
- The scratch trees (`honest`, `opposite`, `honest-wording`, `frows-in-check`,
  `misplaced`, `junk*`, `mut-*.py`) are reproducible from `build.py` and
  `selftest-attack.py`, both copied into this directory.
- Lane hygiene (observed, not mine, not touched): `corpus/__pycache__/
  census_reprobe.cpython-314.pyc` appeared at 18:00:33 during the wave. Every
  invocation of mine used `python3 -B`, and a control run confirms `-B`
  suppresses the write, so another seat imported the instrument without it. A
  stray byte under `corpus/` should not reach the landing.
- Final poll before this report was closed: `corpus/knowledge/{seed.md,
  2026-10-12-rea-readiness-checklist.md}` still hash `d1d31602…` / `561327fa…`
  (identical to `2b017fa3`) and contain no `## Re-verification 2026-11-04`
  section, so A6's base-state scoring is what this review scored. If the rows
  land later, re-score with the canonical invocation above and expect ≥1
  (K04) — a `0` would mean the landed text gamed the K04 pair.

Report: .ufo/waves/round-89/w1/ReviewerR89C1.md
