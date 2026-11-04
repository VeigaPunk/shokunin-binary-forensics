# ScoutR89Host — independent per-surface reconnaissance of the 18-row host-readiness census

Seat: `ScoutR89Host` (wave 1, revenger round 89 attempt 1).
Lane repo: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Frozen claims read first: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-89/claims.md`.
Scratch (deleted after receipts copied): `/fast/scratch/hyaku/revenger-r89/ScoutR89Host`.

## 0. Method and discipline

- I wrote and ran **my own** probe for each of the 18 facts first, and saved the raw
  output (`receipts-raw.txt`, `receipts-canon.txt`, `receipts-fix.txt`,
  `receipts-probes.txt`) **before** opening `corpus/census_reprobe.py`. The
  instrument was read only afterwards, to cross-check my own rule set — my
  findings were not copied from it.
- The instrument's own rule set (read afterwards) is a **literal-token** rule:
  the scored text is the row's last two cells (observed + verdict); a presence
  probe requires the literal word `present` (on PATH) or `absent` (off PATH)
  **and forbids the opposite word anywhere in that same scored text**; a
  listing probe requires every live `*.md` name to be named and forbids
  phantom names; an import probe requires `imports`/`fails`.
- Environment is pinned by `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-89/environment.log`
  (this lane shell: `HOME=/home/vgpnk`, fnm-multishell PATH). **Every presence
  and version value below is relative to that PATH** — see Finding 3.
- Tooling: **nothing installed or upgraded**. No pacman transaction, no
  service restart, no `~/.local/bin` write. The rule set in
  `/home/vgpnk/.omp/agent/RULES.md` was read first; no tool install was needed
  for reconnaissance, so no install record exists.
- I wrote **only** this report (plus the sibling copy at
  `.ufo/waves/round-89/w1/ScoutR89Host.md` named by my `Report:` trailer) and
  the receipts in `.ufo/waves/round-89/w1/ScoutR89Host/`. No lane byte else was
  touched; no git/jj mutation, no commit, no push; `.ufo/state`, `.scratch`,
  `MANIFEST.json` and sibling repos untouched.

## 1. The 18-row probe table (my own commands, this host, 2026-11-04)

Paths: `S=~/.agents/skills/reverse-engineer-anything`.

| id | exact command | exit | observed value |
|---|---|---|---|
| F01 | `ls -1 ~/.agents/skills/reverse-engineer-anything/*.md` | 0 | `HOST-CONTRACT.md`, `SKILL.md` — exactly **two** `*.md` files. Top level also holds `references/` (dir) and three non-`*.md` copies: `SKILL.md.rea.backup` + two `….recovery` |
| F02 | `sed -n 1,8p ~/.agents/skills/reverse-engineer-anything/SKILL.md` | 0 | frontmatter `version: "42"`, `tool_count: 207`. (`SKILL.md.rea.backup` frontmatter: `version: "37"`, `tool_count: 170`; both `.recovery` copies carry 42/207) |
| F03 | `ls -1 ~/.agents/skills/reverse-engineer-anything/references/*.md` | 0 | **seven** names: `android-applications.md`, `cli-command-map.md`, `connection-and-recovery.md`, `evidence-workflows.md`, `javascript-applications.md`, `native-and-artifacts.md`, `runtime-observation.md` (plus 5 `.rea.backup` and 2 `.recovery` non-`*.md` copies) |
| F04 | `command -v rea` | 0 | `/run/user/1000/fnm_multishells/1981588_1793727763382/bin/rea`; `rea --version` → `6.7.0`; symlink → `…/fnm/node-versions/v24.21.0/installation/lib/node_modules/rea-agents/scripts/rea.mjs` |
| F05 | `grep -n 'rea-agents@' ~/.agents/skills/reverse-engineer-anything/SKILL.md` | 0 | skill's own pin is `rea-agents@6.7.0` (lines 33, 37, 82, 83, 102–104) |
| F05b | `npm view rea-agents version` | 0 | **`6.8.0`** (registry `latest`); `npm view rea-agents@6.4.0 version` → `6.4.0` (still published), `…@6.7.0` → `6.7.0` |
| F06a | `node --version` | 0 | `v24.21.0` (fnm multishell node is first on PATH; `/usr/bin/node` and mise `latest` are `v26.12.0`) |
| F06b | `npm --version` | 0 | `11.19.0` (`/usr/bin/npm` and mise `latest` are `12.2.1`) |
| F07 | `python3 -c "import json;d=json.load(open('/home/vgpnk/.omp/agent/mcp.json'));e=d['mcpServers']['rea'];print(list(d.keys()));print(list(e.keys()));print([a for a in e['args'] if 'rea-agents@' in a][0]);print(list(e['env'].keys()))"` | 0 | top keys `['$schema','disabledServers','mcpServers']`; `rea` entry keys `['type','command','args','env']`; its own spec **`rea-agents@6.7.0`**; `disabledServers: ['rea']`; env **key names only** (never values): `GHIDRA_INSTALL_DIR`, `JAVA_HOME`, `REA_JADX_MCP_JAR` |
| F08 | `command -v ghidra` | 0 | `/usr/bin/ghidra` → `/opt/ghidra/ghidraRun` (real install; `/opt/ghidra/support/analyzeHeadless` present). `ghidra --version` exits 0 printing nothing |
| F09 | `jadx --version` | 0 | `1.5.6` (`/usr/bin/jadx`) |
| F10 | `binwalk --version` | 0 | `binwalk 3.1.0` (`/usr/bin/binwalk`) |
| F11 | `unblob --version` | 0 | `26.6.4` (`/home/vgpnk/.local/bin/unblob` — a **user** PATH dir, not a system dir) |
| F12 | `python3 -c 'import pwn'` | 0 | **succeeds**, exit 0 → `/usr/lib/python3.14/site-packages/pwn/__init__.py` (python 3.14.8) |
| K01 | `which rea` | 0 | `/run/user/1000/fnm_multishells/1981588_1793727763382/bin/rea` |
| K02a | `node --version` | 0 | `v24.21.0` |
| K02b | `npm --version` | 0 | `11.19.0` |
| K03 | same `mcp.json` read as F07 | 0 | server key `rea` exists, own spec `rea-agents@6.7.0`, `disabledServers: ['rea']` |
| K04a | `command -v ghidra` | 0 | `/usr/bin/ghidra` — **present** |
| K04b | `command -v ida` | 1 | **no output** — absent. Also absent: `ida64`, `idaq`, `idaPro`, `idat` |
| K05a | `jadx --version` | 0 | `1.5.6` |
| K05b | `binwalk --version` | 0 | `binwalk 3.1.0` |
| K05c | `unblob --version` | 0 | `26.6.4` |
| K05d | `python3 -c 'import pwn'` | 0 | imports OK (exit 0), repeatable ×3 |
| K06a | `unzip -v` | 0 | `UnZip 6.00 of 20 April 2009` |
| K06b | `zipinfo -v` | 0 | `ZipInfo 3.00 of 20 April 2009` |

## 2. Agreement table — does the row's observed+verdict text state the observed value?

Scored text = the row's last two cells, exactly as the gate reads them.
"base" = frozen census at `2b017fa3` (the tree C1's red was measured over);
"landed" = current worktree at HEAD `b90bf37` (the appended
`## Re-verification 2026-11-04` tables, which the gate reads as the last
occurrence per id; F02/F05 verdicts were corrected post-landing by `5f7ecce`,
token-neutral — the gate reads the same 2 findings either way).

| id | base observed+verdict states the live value? | contradicting words (base) | landed states the live value? | contradicting words (landed) |
|---|---|---|---|---|
| F01 | **no** | lists only `SKILL.md`; live listing has **two** `*.md` — `HOST-CONTRACT.md` unnamed; verdict `holds` is false | yes | — |
| F02 | **yes** | — (`42` / `207` live; backup 37/170 also true) | yes | — (verdict corrected post-landing to `STALE -> 42 / 207` by commit `5f7ecce`; token-neutral) |
| F03 | **no** | `same six names` — live has **seven** `*.md` (`cli-command-map.md` added 2026-10-22); `holds (names)` false | yes | — |
| F04 | **no** | `no output, exit 1` / `holds` — `rea` **is** on PATH | yes | — |
| F05 | **no** (partial) | `latest 6.7.0` — registry latest is now **6.8.0** (the pin `rea-agents@6.7.0` and `6.4.0 still published` remain true) | yes | row now states only the pin `rea-agents@6.7.0`; the stale registry-latest claim was dropped rather than corrected (verdict since corrected to `STALE -> 6.7.0` by `5f7ecce`; token-neutral) |
| F06 | **yes** | — (`v24.21.0` / `11.19.0` under the pinned PATH) | yes | — |
| F07 | **no** | `package rea-agents@6.5.0` — live spec is `rea-agents@6.7.0`; and `registered for the omp host` is false at runtime (see Finding 4) | yes (config fact) | verdict `registered` overstates: entry exists but the server is in `disabledServers` |
| F08 | **no** | `absent` / `holds` — ghidra **is** present | yes | — |
| F09 | **yes** | — (`1.5.6`, present) | yes | — |
| F10 | **yes** | — (`binwalk 3.1.0`, present) | yes | — |
| F11 | **yes** | — (`26.6.4`, present) | yes | — |
| F12 | **no** | `ModuleNotFoundError: No module named 'pwn'` / `holds` — import now **succeeds** | yes | — |
| K01 | **no** | `command -v rea → no output` / `holds` — `rea` **is** present | yes | — |
| K02 | **no** (partial) | `npm view rea-agents version → 6.7.0` — now **6.8.0** (the node/npm versions are still true) | yes (versions + pin) | registry-latest dimension dropped, not corrected |
| K03 | **no** | `package rea-agents@6.5.0` — live `rea-agents@6.7.0`; `registered for the omp host` false at runtime | yes (config fact) | verdict `registered` overstates (disabled at runtime) |
| K04 | **no** | `both absent` / `holds` — ghidra **present** (ida absent is correct) | **yes** (truthful: `ghidra present at /usr/bin/ghidra; ida absent`) | none — yet the gate flags it twice (Finding 2) |
| K05 | **no** | `pwntools import fails` / `3 of 4 present` — pwntools **imports**; live is 4 of 4 | yes | — |
| K06 | **yes** | — (`UnZip 6.00`, `ZipInfo 3.00`) | yes | — |

### Count of rows that contradict this host

| tree | rows contradicting this host (my independent reading) | rows the frozen gate flags |
|---|---|---|
| base census (`2b017fa3`, the tree C1's red=10 was measured over) | **12** — F01, F03, F04, F05, F07, F08, F12, K01, K02, K03, K04, K05 | **10** — F01, F03, F04, F07, F08, F12, K01, K03, K04, K05 (F05 and K02 missed: Finding 1) |
| landed tree (current worktree, appended `## Re-verification 2026-11-04`) | **1** — K04 only (and it is *truthful*, not wrong) | **2 findings, 1 row** — both on K04 |

The 10 base findings I reproduce independently match the frozen red receipt
`reports/round-89/census-red.log` exactly, row for row.

## 3. Independent findings the frozen gate does not see

**Finding 1 — the gate under-scores the base census by two rows (12, not 10).**
F05 and K02 both assert the npm **registry latest** (`rea-agents`): the base
text says `latest 6.7.0` / `npm view rea-agents version → 6.7.0`. The registry
now publishes `latest = 6.8.0` (verified: `npm view rea-agents version` →
`6.8.0`; `dist-tags { latest: '6.8.0' }`; versions list ends `…, 6.5.0,
6.7.0, 6.8.0`). The gate's `pin` rule reads only the **skill's own** pin
(6.7.0, still true) and its `version` rule reads only `node --version` /
`npm --version` — so neither row is flagged even though each states a host fact
this host contradicts. A census whose claim is "re-derived from the live host"
should treat the registry-latest dimension as a fact too; the landed rows
sidestepped it by dropping the phrase rather than correcting it to 6.8.0.

**Finding 2 — K04 is structurally unsatisfiable under the frozen rule set
(2 findings, 1 row, unavoidable without faking the host).**
K04 carries two presence probes over the **same** scored text: `ghidra` (live:
present → requires the literal `present`, forbids `absent`) and `ida` (live:
absent → requires the literal `absent`, forbids `present`). The two constraints
are mutually exclusive on one string: any text containing both `present` and
`absent` trips ghidra's forbidden-`absent` and ida's forbidden-`present` (2
findings); any text containing only one of them fails the other probe's token
requirement (1 finding). I brute-forced the rule over 2704 candidate wordings
using the instrument's own live-value functions: **minimum 1 mismatch, and 1
is reachable only by omitting one of the two live facts** — i.e. by writing a
row that states `ghidra present` but silently drops `ida`. The truthful row
("ghidra present at /usr/bin/ghidra; ida absent") scores **2**, which is what
the landed tree and `reports/round-89/c1-after.log` show.
Consequence: with the frozen bytes and a host where ghidra and ida differ in
presence, `CENSUS_STALE_UNFLAGGED=0` is **unreachable**. The only ways to 0 are
(a) make the two probes agree in polarity on the host — i.e. install an `ida`
binary or remove ghidra (faking the host, and ghidra is a real 2026-06-29
install), (b) edit the frozen instrument (forbidden by the no-harm statement),
or (c) change HOME/PATH so `shutil.which` sees a different world (also faking).
The landed K04 row is factually correct on both tools; the miss is the
instrument's literal-token exclusivity, not a wrong census.

**Finding 3 — the census is PATH-conditional, so "the live host" is
shell-relative.** Under a restricted PATH (`env -i PATH=/usr/local/bin:/usr/bin:/bin`)
the very same tree scores **16** findings instead of 2: `rea` becomes absent
(it resolves only through the session-scoped fnm multishell dir
`/run/user/1000/fnm_multishells/1981588_…/bin/rea`, never `~/.local/bin/rea`),
`unblob` becomes absent (it lives in `~/.local/bin/unblob`), and node/npm flip
to `v26.12.0` / `12.2.1`. The landed rows are valid only under the PATH pinned
in `reports/round-89/environment.log`; a different shell (CI, cron, another
user) re-derives different "live" values. Any claim resting on "the live host"
must carry the PATH with it.

**Finding 4 — F07/K03 verdict "registered" is imprecise; the server is
disabled at runtime.** `~/.omp/agent/mcp.json` lists `rea` under `mcpServers`
with its own spec `rea-agents@6.7.0` **and** lists `rea` in
`disabledServers`. `~/.agents/AGENTS.md` and the skill's own SKILL.md both say
the REA MCP server is deliberately disabled and that REA is CLI-first
("A session has zero REA MCP tools"); this session's tool inventory confirms
no `rea` MCP server is mounted. So the config entry exists, but "registered for
the omp host" overstates it — the entry is present and *disabled*. The gate's
`mcp` rule cannot tell the two apart (it only checks that the `rea` key exists
and that the row contains the live spec); I verified that a row worded "not
registered for the runtime" **also passes** the rule. The landed rows chose the
looser wording.

## 4. Cross-checks performed (read-only)

- `PYTHONUTF8=1 python3 -B corpus/census_reprobe.py --root <base archive of 2b017fa3 corpus/knowledge>` → `CENSUS_ROWS=18`, 10 `CENSUS_MISMATCH` lines, `CENSUS_STALE_UNFLAGGED=10`, exit 1 — reproduces the frozen red byte-for-byte.
- Same gate over the current worktree → 2 findings (K04 only), exit 1, idempotent over two runs.
- `--selftest` → 9 legs, `CENSUS_SELFTEST=pass`, exit 0.
- `sha256sum corpus/census_reprobe.py` → `c3127ffc…648a`, matching `reports/round-89/instrument-pins.log`; the instrument was not modified by me.
- `git diff --stat 2b017fa3 c84339c -- corpus/knowledge` → empty (the freeze did not pre-edit the census files).
- Blind-token control `reports/round-89/junk-control.log` → 7, consistent with the forbidden-opposite and version legs biting.
- Claims' routing evidence re-verified independently: `jadx` 1.5.6 on PATH, and `/home/vgpnk/.local/opt/jadx-headless-mcp/jadx-headless-mcp-0.7.1-all.jar` present (42,619,858 bytes, 2026-10-13). K stays operator-blocked (r74 L0 unanswered) — untouched by this seat.
- No REA call was made: presence is not capability (`corpus/QUALITY.md` Q05).

## 5. Receipts

Copied into `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-89/w1/ScoutR89Host/`:

- `receipts-raw.txt` — first-pass probe output (all 18 facts).
- `receipts-canon.txt` — canonical per-fact command/exit/output table (three rows needed re-running as script files after shell quoting mangled the inline `python3 -c`; see `receipts-fix.txt`).
- `receipts-fix.txt` — corrected F07/K03 (`mcp.json` key names + own spec + env key names only) and F12/K05d (`import pwn`) runs.
- `receipts-probes.txt` — the numbered 27-probe script used for the table in §1.
- `k04_brute.py` — brute-force proof of the K04 floor over the instrument's own live-value functions.
- `floor-tree/`, `k04-test/`, `k04-a…k04k/`, `k04c-*/`, `mcp-test/` — scratch trees used to measure the reachable floor (not lane files).

Scratch `/fast/scratch/hyaku/revenger-r89/ScoutR89Host` deleted before yield.
