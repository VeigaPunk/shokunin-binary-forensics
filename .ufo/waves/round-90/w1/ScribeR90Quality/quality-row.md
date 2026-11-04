# Draft — `corpus/QUALITY.md` criterion Q17 (ScribeR90Quality, round 90)

Target: append one row after Q16 (`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/QUALITY.md:28`)
in the `## Criteria` table (`| id | criterion | reject when | lesson |`). Highest existing id
is Q16 (`grep -n '^| *Q[0-9]' corpus/QUALITY.md` → last hit `:28 | Q16`); `grep -n 'Q1[7-9]'`
over QUALITY.md prints nothing, so Q17 is free. Append only; rows Q01–Q16 stay byte-unchanged
(claims.md no-harm statement, `reports/round-90/claims.md:108`).

## Row (paste verbatim)

```
| Q17 | When an adjudication relocates a cited artifact, every citation of the old path — `corpus/SOURCES.md` `source` and `anchor` cells, `corpus/knowledge/` entries, `LOG.md`, `corpus/lessons/` — is swept in the same commit. A filed entry gains an appended dated correction naming the old and the new path; a SOURCES row whose `source` cannot change in place (only `status`, `recheck`, `used-by` are mutable) is closed by a new row whose `teaches` opens `supersedes S### —` and cites the relocated path. Machine check: `reports/round-90/source_path_check.py` prints `SOURCE_PATH_DEAD=0` over the landing tree. | a `source` or `anchor` cell, or an entry pointer, names a path that does not resolve at closure while the bytes live at a relocated path (S481 cites `corpus/live/runs/round-89/receipt.json` after `bd575ca` moved it to `reports/round-89/rejected-android-record/receipt.json`; `corpus/knowledge/2026-10-12-rea-readiness-checklist.md:67` still names `corpus/live/runs/round-89/`) | D1 (`lessons/round-89-verifier-spotcheck.md:65-66,168,211-218`); Mistakes row "relocation not swept" (round-90 lesson) |
```

## Grounding (each clause → evidence)

| clause | evidence (absolute path:line) |
|---|---|
| relocation left a dead `source` cell | `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md:498` (S481 `source` and anchor both `corpus/live/runs/round-89/receipt.json`) |
| relocation left a dead knowledge pointer | `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/2026-10-12-rea-readiness-checklist.md:67` |
| `source` not mutable in place | `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md:6` ("only `status`, `recheck` and `used-by` change in place") |
| fix shape = superseding row + appended correction | `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-89-verifier-spotcheck.md:211-218` |
| relocated bytes exist and carry the quoted anchors | `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-89/rejected-android-record/receipt.json` :6 `"rea_version": "6.7.0"`, :20 `"stdout_sha256": "01af3141…1c76"`, :31 `"cmp_verdict": "DIFFER: …"` (re-read 2026-11-04 with `sed -n '20p;6p;31p'`) |
| failure grade: discernment held at `unchanged` because of this | `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-89-verifier-spotcheck.md:200-207` |

## Red-before (scratch probe, not the named instrument)

`reports/round-90/source_path_check.py` is **absent** at the freeze `c7767789fe9e96bcc0d50656ad4bdce69ba3a3a9`
(`ls reports/round-90/` lists no such file). Q17 names it as the machine check; the lane must land it
before the row is admitted, else the row's "Machine check" clause is a pointer that does not resolve
(the very class Q17 rejects). My stand-in probe over the lane working tree at the freeze
(`d1-dead-path-probe.log`, this dir) printed:

```
DEAD line=498 S481 source corpus/live/runs/round-89/receipt.json
DEAD line=498 S481 anchor corpus/live/runs/round-89/receipt.json
PATH_TOKENS_CHECKED=83
SOURCE_PATH_DEAD_PROBE=2
```

Probe limits (named unguarded, Q16): it checks only backticked tokens starting `corpus/` or
`reports/` inside the `source` and `anchor` cells of `S###` rows; it does not read knowledge
entries, `LOG.md` or lessons, unbackticked paths, or `.ufo/` paths. The knowledge pointer at
`2026-10-12-rea-readiness-checklist.md:67` was found by `grep -rn 'corpus/live/runs/round-89'`
(hits: SOURCES.md:498, the checklist :67, the r89 spot-check lesson :135,:168,:212,:214 — the
lesson hits are historical narration of the move, not live pointers — plus `reports/round-89/`
claims/logs/the relocated LEDGER/receipt, which are frozen r89 records).

Proposed check contract (proposal only; I do not write instruments): exit 0 and
`SOURCE_PATH_DEAD=0` iff every repo-relative path in S-row `source`/`anchor` cells and in
non-superseded knowledge-entry pointers resolves, where a row superseded by a later
`supersedes S### —` row and an entry with an appended `Correction (round N):` naming the new path
are exempt; a self-test must show the S481 tree at `c7767789` red (2) and a superseded tree green.
