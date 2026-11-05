# ExecCensus — round-94 w1 census, collision, no-harm receipts

Seat: ExecCensus (leaf executor). Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin` at HEAD `060a8e87d6de6b31f91b58524ab0fcad88ae5431` (the freeze tip). Run: 2026-11-05T13:16:45-03:00. Read-only seat: no lane files, no git writes, no host mutations.

## 1. Seven census commands (SKILL.md §6.2, verbatim, from lane root)

Receipt: `.ufo/waves/round-94/w1/ExecCensus/census-seven.log` (sha256 `e1e920c5e76f6665dbc4d3ae40c2a410a19c20fff3387c43ff8684faa7c594f6`).

| # | check | result | verdict |
|---|-------|--------|---------|
| 1 | rows (spacing-tolerant) | 497 | consistent with registry census below |
| 2 | malformed rows (NF!=13) | 0 | clean |
| 3 | tier histogram | `A=448 B=21 C=28` | sums to 497 |
| 4 | status histogram | `mined=461 queued=16 rejected=20` | sums to 497 |
| 5 | duplicate ids | none printed | clean |
| 6 | enum violations / tier inflation | none printed | clean |
| 7 | mined used-by missing paths | none printed | clean |

All seven green at the freeze tip.

## 2. Fleet census driver

`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`

Receipt: `.ufo/waves/round-94/w1/ExecCensus/census-driver.log` (sha256 `f0f8c6a7f0fc69ba68c07aae15862e12baac7fceae986e6fc5bb970561c551e2`).

- Exit code: **0**; final verdict line `ok` for `corpus/SOURCES.md`; zero E-codes.
- Warnings: **W01=21, W04=13** (grep-verified over tab-delimited codes). Expected per seat spec was 21 W01 + 15 W04: **W01 matches, W04 is 13, a delta of −2 vs the expected 15.** Exit 0 and 0 E are unaffected; this is a warnings-only drift, recorded as the real number, not adjusted to the expectation.
- W04 rows (13): S024, S028, S029, S034, S048, S053, S427, S428, S429, S430, S491, S493, S496 — all "duplicate url … across scopes".
- W01 rows (21): S051, S087, S088, S169, S170, S180, S197, S198, S199, S200, S203, S311, S332, S351, S352, S384, S388, S394, S399, S400, S437 — all "tierC mined used-by=…" (includes the C1 counter-evidence rows S087/S088 → `corpus/knowledge/round-72-tool-landscape.md`, consistent with the frozen claim's re-grounded entry).

## 3. Assimilation id-collision check

Commands run exactly as specified; redirect targets resolved inside the seat dir (`cd "$A"` first, so the relative `reg-ids staged-ids collisions` names land in-bounds). No writes outside the wave dir; `shokuknow` touched only at `merge/revenger/SOURCES.append.md` via read-only grep.

Receipts in `.ufo/waves/round-94/w1/ExecCensus/`:
- `reg-ids` — 497 lines, sha256 `3a0973dc3f9f38d18650be067523696823eb9d21aa14e61e06479a348d50c7af`
- `staged-ids` — 155 lines, sha256 `18ff151052c7aa13e03cd0e12e48f42158d31b79d1bd4e6fb62f9b95404e2631`
- `collisions` — sha256 `18ff151052c7aa13e03cd0e12e48f42158d31b79d1bd4e6fb62f9b95404e2631` (byte-identical to staged-ids: **every staged id collides**)
- `collision-run.log` — run header + counts, sha256 `b756d0b4e91d913f01b44698ca9c88648d9245edad9e5e611863c129bf982a39`

**Collision count: 155 (matches the expected 155).** reg-ids 497 == census row count 497.

## 4. No-harm receipts (read-only `git diff --stat`)

Receipt: `.ufo/waves/round-94/w1/ExecCensus/no-harm.txt` (sha256 `6df5ffff3e4573ee1aae94b7e499541d4552348b51466276594d0deaf95e2b04`).

- `060a8e8…..refs/heads/main -- PROVINCE.md corpus/QUALITY.md` → empty diff (exit 0). Frozen lane governance bytes untouched.
- `9876cb3…..refs/heads/main -- corpus/live corpus/fixtures` → empty diff (exit 0). Live corpus and fixtures untouched.

## Verdict

Census green: 497 rows, 0 malformed, 0 duplicates, 0 enum/tier violations, 0 missing used-by paths, driver exit 0 with 0 E. Collisions 155/155 as expected. No-harm clean on both pinned ranges. One delta to carry to the L1: **driver W04 = 13, not the expected 15** (W01 and E counts exact); does not affect exit status or any kill rule.

## Provenance / bounds

- Files written: the six receipts + this report path `.ufo/waves/round-94/w1/ExecCensus.md` (named by the seat spec) + seat-dir files. Nothing else touched.
- Scratch `/fast/scratch/hyaku/revenger-r94/ExecCensus` (census runner script only; outputs all live in the wave dir) — deleted on exit.
- No installs performed; no network used; no spawns.
