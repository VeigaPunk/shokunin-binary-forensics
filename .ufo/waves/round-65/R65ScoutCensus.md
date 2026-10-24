PASS — maintained census exits 0 and all seven frozen census commands match expected after-state (rows 41, malformed 0, no duplicates/enums/missing used-by).

Seat `R65ScoutCensus`, round 65 attempt 1 (hyaku). Read-only census run on the
live working tree of `/home/vgpnk/Projects/shokunin/revenger-shokunin` at
2026-10-24T05:58:03Z (not a committed archive — census commands are specified
"from the lane root" by CORPUS.md §Census, so they measure the working tree).
Expected per seat brief: rows 41, malformed 0, no duplicates, no enum
violations, no missing used-by paths, maintained census exit 0. All matched.

## Maintained census (fleet root)

Command (cwd `/home/vgpnk/Projects/shokunin`):

```sh
./scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger
```

Exit code: **0**. Full output:

```
revenger	W04	S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes
revenger	W04	S028 duplicate url github.com/ethereum/execution-specs/tree/v2.20.0/src/ethereum/forks/osaka/vm across scopes
revenger	W04	S029 duplicate url tc39.es/ecma262 across scopes
revenger	W04	S034 duplicate url pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT across scopes
revenger	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
EXIT=0
```

The four W04 duplicate-URL warnings are the pre-disclosed set named in
`reports/round-65/claims.md` ("four disclosed W04s S024/S028/S029/S034" —
claims.md:128): same IDs, same URLs, none new. `ok` line confirms validator
accepts the file.

## Frozen manual census (lane root, CORPUS.md §Census lines 134–147)

All commands run with cwd `/home/vgpnk/Projects/shokunin/revenger-shokunin`
against `corpus/SOURCES.md` (88 lines). Each exited **0**.

| # | command (abbrev.) | expected | observed |
|---|---|---|---|
| 1 | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | 41 | **41** |
| 2 | malformed `NF!=13` awk | 0 | **0** |
| 3 | tier histogram | — | **A=39 C=2** |
| 4 | status histogram | — | **mined=35 queued=2 rejected=4** |
| 5 | duplicate ids (`sort \| uniq -d`) | empty | **(no output)** |
| 6 | enum violations + tier inflation | empty | **(no output)** |
| 7 | mined used-by missing paths | empty | **(no output)** |

Row IDs are contiguous S001–S041 with tail `S036 S037 S038 S039 S040 S041`
(verified by the same id-extraction awk piped to `tail -6`), consistent with
claims.md admission-order step 1's "source rows S038+ (+S039…)" plus one
additional appended row S041 beyond the S038–S040 named in the contract
(claims.md:114 names "S038+"; the contract's wording allows ≥1 more row).
Status histogram: 35 mined + 2 queued + 4 rejected = 41 ✓. Tier histogram:
39 A + 2 C = 41 ✓.

## Findings and residual notes

- All expected post-conditions hold: maintained validate exit 0, rows 37→41
  (claims.md:128 requires "rows 37 → 38+"), zero malformed, zero duplicates,
  zero enum violations, zero missing used-by paths.
- [INFERENCE] S041 is the "+S039 if the zipfile-docs opener lands it"-style
  extra row allowance playing out; claims.md:114 already anticipated S038+
  rows plural, so 41 rows is inside the contract envelope, not a violation.
- Census measures the working tree only; committed-tree equivalence at final
  tip is the L1 measure step's job (claims.md:122–123), not this seat's.
- No missing used-by paths means every `mined` row's used-by targets —
  including the new C1 entry `corpus/knowledge/round-65-apk-axml-byte-evidence.md`
  cited by the new rows — resolve on disk in the working tree.
- Installs: none. No git/jj mutations; no writes outside this report.

Report: .ufo/waves/round-65/R65ScoutCensus.md
