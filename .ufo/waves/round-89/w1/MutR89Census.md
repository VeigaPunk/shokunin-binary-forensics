# MutR89Census — mutation probe of the frozen census gate (round-89, w1)

Seat `MutR89Census`, lane `/home/vgpnk/Projects/shokunin/revenger-shokunin`,
base `2b017fa3c616a84b7b491e3312029fa8a8c076e6`. Read first:
`/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-89/claims.md`.

Instrument under test (byte-identical copy in scratch; lane file never edited):

```
c3127ffc18a54f85f01e2fb88f50b5db694484588e5b7467ae5567ffdd3b648a  corpus/census_reprobe.py
```

This equals the pin committed in
`/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-89/instrument-pins.log`.
337 lines, re-read in full before mutating.

## Control (pristine, same host, same base tree)

| detector | expected (frozen receipt) | observed |
|---|---|---|
| `--selftest` | 9 legs ok, `CENSUS_SELFTEST=pass`, exit 0 | identical (`reports/round-89/census-selftest.log`) |
| base red over `git archive 2b017fa3 corpus/knowledge` | 18 rows, 10 `CENSUS_MISMATCH`, `CENSUS_STALE_UNFLAGGED=10`, exit 1 | identical, same 10 ids F01 F03 F04 F07 F08 F12 K01 K03 K04 K05 (`reports/round-89/census-red.log`) |

Base tree sha256: `seed.md d1d31602…`, `2026-10-12-rea-readiness-checklist.md 561327fa…`.
The pristine run is the baseline every mutant is compared against; a mutant is
"killed" only when a detector output *changes* from this control.

## Six one-limb mutants (each: one line changed in a copy)

| # | limb (exact diff) | mutant sha256 | `--selftest` (last line) | base red | forbidden-branch tree (control 15) | verdict | leg that died |
|---|---|---|---|---|---|---|---|
| a | L216 `bad = [w for w in forbidden if w.lower() in text]` → `bad = []` (forbidden-opposite leg) | `479746b0 26b62094…` full: `479746b026b62094a79b2a395db02ec892f975d316a48a7acbc18abbb18949ff` | **pass** / `CENSUS_SELFTEST=pass` / exit 0 | 10 = control | **2** ≠ 15 | killed, but only by the forbidden branch | **none** — no selftest leg plants the forbidden-opposite branch |
| b | L204 `phantom = sorted(n for n in named if n not in live_l)` → `phantom = []` (listing phantom leg) | `d51573b3bef3e1c557557d647f3f254d673074cd520cd15e643fcd5b9db9f527` | **fail** / `CENSUS_SELFTEST=fail` / exit 1 | 10 = control | 13 ≠ 15 | killed | `CENSUS_SELFTEST_listing-phantom=FAIL`, findings `[]` |
| c | L143 `return (kind, arg, [m.group(0) if m else v], [])` → `return (kind, arg, [], [])` (version rule accepts any token) | `94b0416461e2672fdc0a38c78b9f669aee6338b526e3576dcdce7bd69a4a9e58` | **pass** / `CENSUS_SELFTEST=pass` / exit 0 | 10 = control | 15 = control | **SURVIVED all detectors** | **none** |
| d | L157 `return (kind, "rea", [f"rea-agents@{spec_v}"], [])` → `return (kind, "rea", ["rea"], [])` (mcp rule accepts a bare key name) | `93779bf5b95b521b7a90896a8d4168b898b3cf975c5a8f73bf5f478e44b41be1` | **pass** / `CENSUS_SELFTEST=pass` / exit 0 | **8** ≠ 10 | 15 = control | killed by base-red composition | **no selftest leg**; F07 + K03 (`mcp:rea`) flip green |
| e | L151 `return (kind, arg, ["imports"] if ok else ["fails"], ["fails", "ModuleNotFound"] if ok else ["imports"])` → `return (kind, arg, [], [])` (import rule accepts both states) | `18cc00ceebdd0c0d0f7f81ce357897345b91d09eb7187bdd4b13d6182a879887` | **pass** / `CENSUS_SELFTEST=pass` / exit 0 | **8** ≠ 10 | 13 ≠ 15 | killed by base-red composition | **no selftest leg**; F12 + K05 (`import:pwn`) flip green |
| f | L176 `return " | ".join(cells[-2:]) if len(cells) >= 2 else line` → `return " | ".join(cells)` (score the mint cell too) | `df662d717358293b47cb6bdae0c7e15e9fa57dfae871f0756e181dcfd950a472` | **fail** / `CENSUS_SELFTEST=fail` / exit 1 | **16** ≠ 10 | 15 = control | killed | `CENSUS_SELFTEST_clean=FAIL` — `CENSUS_MISMATCH K01 presence:jadx states 'absent' against the live value` (mint cell `mint ABSENT` now scored); base red also gains F09/F10/F11 + three K05 limbs |

Receipts: `receipts/mutants-selftest-and-red.log` (verbatim stdout+exit per
mutant), `receipts/mutant-pins.log`, `receipts/control.log`.

## Why the selftest is blind to four of six limbs — attributed

`selftest()` monkeypatches `live` with `fake_live` (L247–262) and swaps `ROWS`
for a synthetic 8-row table. Therefore the selftest exercises **only
`check_rows()`**, never any rule implementation inside `live()`. Replaying the
eight plants and classifying which branch produced the finding:

| plant | caught by |
|---|---|
| presence-opposite | **token-presence** |
| presence-unstated | token-presence |
| version-missing | token-presence |
| import-opposite | token-presence |
| mcp-missing | token-presence |
| listing-phantom | **listing-phantom** |
| skill-missing | token-presence |
| pin-missing | token-presence |

Receipt: `receipts/branch-attribution.log`. Two consequences, both measured:

1. **The forbidden-opposite branch is planted by zero legs.** The
   `presence-opposite` plant (`now absent`) is caught by token-presence
   (`'present'` missing) before the forbidden check runs, and `import-opposite`
   (`import fails`) likewise — `"imports"` is not a substring of `import fails`.
   That is exactly why mutant **a** passes `--selftest` and leaves the base red
   at 10.
2. **Mutants inside `live()` are invisible to `--selftest` by construction.**
   Proof: `attr_legs.py mut/mut_d.py` (mcp rule broken) prints a plant table
   byte-identical to pristine — every leg still `caught=1`.

`live()`-internal limbs c, d, e therefore had to be caught by a *count* change,
and only d and e produced one. c produced none.

## Survivor

**Mutant c survives every detector I could run** — `--selftest` (pass), base red
(10 = control), and both token-padding controls (15 and 8, both = control).

- **Exact rule weakened:** the `version` probe in `live()`. With the token list
  emptied, a row passes the version limb regardless of what version it states,
  and the forbidden list is empty in that branch anyway. The gate can no longer
  report a stale or wrong `node`/`npm`/`unzip`/`zipinfo` version at all.
- **Real blindness, not just a harness gap.** Three declared detectors, three
  misses: `--selftest` never calls `live()`; the base red has **zero** version
  mismatches (all version rows F06/K02/K06 state the live values, so breaking
  the rule cannot move 10); and the blind-token control pads the live version
  tokens (`24.21.0 11.19.0 6.00 3.00`) into every row, so its version limbs pass
  by construction. Nothing in the freeze would go red if the version rule were
  deleted.
- **Consistent with the committed control's own composition:** the 7 lines of
  `reports/round-89/junk-control.log` are 5 forbidden-opposite findings (F08,
  F12, K04 ×2, K05) + 2 listing-phantom (F01, F03) and **0 version findings** —
  so that control does not exercise the version leg either (the claims text's
  "forbidden-opposite and version legs bite" is only half true against its own
  receipt).

### Proposed next-round check (not applied)

1. **A hermetic `live()` leg in `--selftest`** — the structural fix. Build a
   temp dir holding a shim `node`/`npm` (3-line script echoing a fixed version),
   prepend it to `PATH` for the duration, and assert
   `live(("version", "node --version")) == ("version", "node --version",
   ["<shim version>"], [])`. This is the only way the selftest can reach any
   rule implementation, since it currently replaces `live()` wholesale. Do the
   same for `mcp` (a temp `mcp.json` via a `MCP_JSON` override) and `listing`
   (a temp `SKILL_DIR`).
2. **A version-opposite control tree** — base tree with one version row's scored
   cells rewritten to a non-live token (e.g. `24.0.0` where the live token is
   `24.21.0`); it must score `>= 1`, so the do-nothing control becomes
   `10 -> 11` and mutant c would score 10 instead of 11.

## Mutant a: killed, but only by a control that cannot be re-run

Mutant a survives both assigned detectors (`--selftest` pass, base red 10) and
is killed only by a tree whose scored cells state both the live value and its
opposite — my `junk` tree, where pristine scores 15 and mutant a scores 2
(the two listing-phantom findings only). That is the forbidden branch doing its
job.

**Calibration finding:** the committed blind-token control has **no generator in
the lane**. Two independent reconstructions of it do not reproduce the
committed 7 — all-token padding scores 15, value-kind-only padding scores 8 —
so the receipt is not re-derivable from the tree, and kill rule (b) of the
frozen claim cannot be re-run after a mutation. By composition the committed
receipt *would* kill mutant a (5 of its 7 lines are forbidden-branch findings,
which mutant a removes), but that is derived from the receipt text, not
executed. **Proposed next-round check:** commit the junk-control generator
(emitting the padding rule and the tree) beside `census_reprobe.py` so kill
rule (b) is re-runnable.

## Summary

- Six limbs, six attributions: b and f die on a named selftest leg; d and e die
  on the base-red count; a dies on the forbidden branch (not reachable from
  `--selftest`); **c survives everything**.
- The gate's rule *kinds* are not equally defended: the selftest plants eight
  rows but exercises two branches, and every `live()` rule implementation
  (version, mcp, import, skill, pin) is outside its reach.
- The frozen targets themselves are unaffected by this probe: C1's `0` is
  reached by the real landing, and no mutant was applied to the lane.

## Scope / restoration

- Lane writes: this file plus `receipts/` under
  `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-89/w1/MutR89Census/`.
  `corpus/census_reprobe.py` was **read only**; re-hashed after the probe:
  `c3127ffc…b648a`, still the pin.
- Scratch `/fast/scratch/hyaku/revenger-r89/MutR89Census` deleted after the
  receipts were copied out; `TMPDIR` was set to that path for every run.
- No git/jj mutation, no commit, no push, no `.ufo/state`, `.scratch`,
  `MANIFEST.json` or sibling-repo write.
- Tooling: nothing installed or upgraded (system `python3` sufficed); no pacman
  transaction attempted.
