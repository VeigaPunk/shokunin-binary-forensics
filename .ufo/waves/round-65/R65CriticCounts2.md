NOT-FALSIFIED — independent recount of corpus/SOURCES.md reproduces the maintained census exactly: 41 rows, A=39 C=2, mined=35 queued=2 rejected=4, zero malformed/dups/missing-paths, four disclosed W04s; 37→41 delta at claim base verified cell-for-cell.

# Seat: R65CriticCounts2 — second independent count attack

## Method

Three counting paths, mutually independent implementations:

1. **Maintained census output** — `scripts/sources-census.sh` (fleet census tool, sha256 `3fb7261569f46423dd80ecc23e0a23789a7926f667c7a3fc559d2439d4a64e30`).
2. **Frozen contract commands** — the seven §Census commands in `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:64-81` run verbatim from the lane root.
3. **Own parser** — Python, different parse method: `|`-split per line, strip empty edge cells, require exactly 11 cells, counter-histogram on cells 3 (tier) and 7 (status); run on both the working tree and `git show 3eebcdd7…:corpus/SOURCES.md` (frozen claim base, piped stdin — no writes).

Counted file: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md` sha256 `ef839dcbe2e3aeb64820adfd6b3b8db569a9d3b0eea716c51a48fcb8ea70d38e` (88 lines).

## Evidence — maintained output

`bash scripts/sources-census.sh census revenger-shokunin` (from `/home/vgpnk/Projects/shokunin`), exit 0:

```
revenger-shokunin	rows	41
revenger-shokunin	tier.A	39
revenger-shokunin	tier.C	2
revenger-shokunin	status.mined	35
revenger-shokunin	status.queued	2
revenger-shokunin	status.rejected	4
FLEET	rows	41 · tier.A 39 · tier.B 0 · tier.C 2 · tier.invalid 0
FLEET	status.queued 2 · status.mined 35 · status.rejected 4 · invalid 0 · missing 0
```

`bash scripts/sources-census.sh validate revenger-shokunin` → exit 0, `ok`, with exactly the four disclosed W04s:

```
W04	S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes
W04	S028 duplicate url github.com/ethereum/execution-specs/tree/v2.20.0/src/ethereum/forks/osaka/vm across scopes
W04	S029 duplicate url tc39.es/ecma262 across scopes
W04	S034 duplicate url pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT across scopes
```

## Evidence — seven contract commands (working tree, run verbatim)

```
rows: 41            malformed: 0
tier: A=39 C=2      status: mined=35 queued=2 rejected=4
dup ids: (none)     enum/tier-inflation: (none)   missing used-by: (none)
```

## Evidence — own parser

Working tree:
```
ROWS: 41   MALFORMED: 0   ENUM_OK: True
TIER:   {A: 39, C: 2}          (tier.B = 0)
STATUS: {mined: 35, queued: 2, rejected: 4}
KIND:   {spec: 16, docs: 11, own-work: 12, community: 2}
DUP_IDS: none
ID_RANGE: S001..S041 contiguous=True, file order monotonic
LAST_ROW: S041 (SOURCES.md:55) tier A, kind own-work, status mined
W04_DUP_URLS (independent URL extraction, scheme-normalized):
  rfc-editor.org/rfc/rfc3227.txt                     → S008, S024
  github.com/ethereum/execution-specs/…/osaka/vm     → S016, S028
  tc39.es/ecma262/                                   → S022, S029
  pkware.cachefly.net/…/APPNOTE.TXT                  → S032, S034
MISSING_USEDBY (mined rows, path existence check): none
NEW ROWS: S038 A spec mined · S039 A docs mined · S040 A docs queued · S041 A own-work mined
```

Frozen claim base `3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f` (`git show …:corpus/SOURCES.md` piped to the same parser):
```
BEFORE rows: 37  last: S037
BEFORE tier:   {A: 35, C: 2}
BEFORE status: {mined: 32, queued: 1, rejected: 4}
```

## Delta check against recorded claims

- `claims.md:127-128` — "Census before: exit 0 (37 rows ending S037; four disclosed W04s S024/S028/S029/S034). Census after must exit 0 with rows 37 → 38+." ✓ 37→41, exit 0, same four W04s (no new W04 — S038/S039/S040 introduce no duplicate URL; S041 is own-work with no URL).
- `corpus/lessons/round-65.md:17` — "rows 37 → 41 (+S038, +S039, +S040 queued, +S041)" ✓ exact.
- `LOG.md:901` — "rows 37 → 41, +S038/S039 mined, +S040 queued, +S041 own-work" ✓.
- `SCORECARD.md:450` — "Sources: rows 37 → 41 … seven manual census commands and `scripts/sources-census.sh validate` both exit 0" ✓.
- Implied before-histogram at 37 rows (A35 C2 / mined32 queued1 rejected4) is consistent with the recorded round-62 end-state in `LOG.md:854` (31 rows A29 C2, mined26 queued1 rejected4) plus round-63 (+S032–S035: 4 mined) and round-64 (+S036/S037: 2 mined): 31+6=37, mined 26+6=32, A 29+6=35. Chain reconciles with no unexplained row churn.

## Drift hunt — checks beyond the required histograms

- **Row placement (regression on round-64 E12 defect):** all 41 S-rows sit inside `## Registry` (SOURCES.md:13-55); no row-shaped lines elsewhere in the file. No E12 recurrence.
- **Append-only discipline:** my before/after parse shows all pre-existing S001–S037 ids still present in order; status changes confined to appends (+4 rows). Lesson claims "No pre-existing row's status/recheck/used-by changed" (`lessons/round-65.md:17`) — consistent with status histogram delta being exactly the four new rows.
- **S040 queued row:** used-by `—`, correct for queued status (W03/W01 silent).
- **Opened dates:** S038–S041 `opened=2026-10-24` (today) — valid ISO, not future (E08 clean). Note, outside census scope: S036/S037 rows also carry `opened=2026-10-24` though appended in round 64 (git log `c7b7cf9`/`782bd02`); E08 validates date well-formedness only, not opener-round truth. Not a census drift — recorded here as an observation for the sources reviewer, not a FAIL under my brief.

## Result

No drift on any axis: rows, tier histogram, status histogram, kind histogram, id contiguity/order, malformed rows, enum violations, duplicate URLs, used-by path existence, or recorded before/after deltas. The count attack fails to falsify — census is consistent across three independent counters and every recorded claim.

Tool installs: none (bash/gawk/python3 only).
