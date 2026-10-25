# R67CensusReplay — round-67 census replay (current working tree)

PASS — all seven frozen census commands and the fleet validator are clean on the current tree: 45 rows (S001–S045 contiguous, S045 new), malformed=0, tier A=43 C=2, status mined=37 queued=4 rejected=4, duplicate-id/enum/used-by checks print nothing, `sources-census.sh validate` exit 0 (4 pre-existing W04 warnings, 0 E), and S045's used-by path exists and is tracked.

run: 2026-10-25T00:33:03Z (UTC) · seat R67CensusReplay · lane `/home/vgpnk/Projects/shokunin/revenger-shokunin`
lane HEAD: `7668510` (round-67 build tip; parent `d11f81d` pre-registration, base `fa0eb3eb`)
measured file: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md`
sha256 `fa70ee392db0d270201e6e7ee957ca5fe91f4dd528ff49297b056de9a30b5e64` · 48275 bytes · 96 lines · mtime 2026-10-24 21:02:07 -0300

## Measurement target is the current tree, and it equals the committed blob

- `git hash-object corpus/SOURCES.md` → `918f2c62a6cffe280917d05bd463409cb1a6fff7`
- `git rev-parse HEAD:corpus/SOURCES.md` → `918f2c62a6cffe280917d05bd463409cb1a6fff7` (equal)
- `git diff --stat HEAD -- corpus/` → no output, exit 0; `git status --porcelain -- corpus/` → only `?? corpus/lessons/round-67.md` (untracked, not the registry)

So this working-tree census is also a committed-tree census at `7668510`; there is no uncommitted registry drift for a seat to measure.

## Provenance of the seven commands (brief pointer is stale)

The item brief says "corpus/SOURCES.md §Census". **No such section exists**: `grep -nE 'Census|census' corpus/SOURCES.md` → no output, exit 1; SOURCES.md headings are `## Registry` (:11), `## Paths` (:61), `## Search log` (:72), `## Leads (unopened)` (:91). The canonical seven-command block lives in two byte-identical places, verified with `diff -u`: `/home/vgpnk/Projects/shokunin/CORPUS.md:133-147` and `/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:66-80` → `BLOCKS-IDENTICAL` (15 lines). I ran that exact text, verbatim, from the lane root. (Freshness finding only, not a registry defect: SOURCES.md:3 correctly names the contract file.)

## The seven commands — actual output, all from the lane root

| # | check | command shape | actual output | exit |
|---|---|---|---|---|
| 1 | rows | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | `45` | 0 |
| 2 | malformed (11 columns ⇒ NF=13) | contract awk `NF!=13` | `0` | 0 |
| 3 | tier histogram | contract awk col 5 | `A=43 C=2 ` | 0 |
| 4 | status histogram | contract awk col 9 | `mined=37 queued=4 rejected=4 ` | 0 |
| 5 | duplicate ids | contract awk col 2 \| sort \| uniq -d | *(prints nothing)* | 0 |
| 6 | enum violations + tier inflation | contract awk over NF==13 | *(prints nothing)* | 0 |
| 7 | mined used-by paths exist | contract awk col 12 \| `[ -e ]` | *(prints nothing)* | 0 |

- Row count **45** matches the brief's expectation after S045; columns sum correctly: 43+2 = 45 and 37+4+4 = 45.
- Independent id scan: `ids 45 first S001 last S045 contiguous True dupes 0` (Python range check on the extracted id column). Rows occupy `corpus/SOURCES.md:15-59`.
- Used-by scan (own loop over all 37 `mined` rows, every `,;`-separated cell resolved from the lane root): zero `MISSING`, zero `EMPTY` lines → every mined row names at least one existing used-by path. Command 7 agrees.

## S045 (new this round)

`corpus/SOURCES.md:59`:

`| S045 | DEX format specification (Android Open Source Project) — https://source.android.com/docs/core/runtime/dex-format | docs | A | … | mined | 2026-10-24 | 180d | corpus/knowledge/round-67-apk-axml-byte-evidence.md |`

- status `mined` (col 9), opened `2026-10-24`, recheck `180d`, used-by exactly `corpus/knowledge/round-67-apk-axml-byte-evidence.md`.
- `test -f corpus/knowledge/round-67-apk-axml-byte-evidence.md` → EXISTS; `git ls-files --error-unmatch` → TRACKED (`git ls-tree -r HEAD --name-only corpus/knowledge/` lists `corpus/knowledge/round-67-apk-axml-byte-evidence.md`).
- v2 entry sha256 `170df17d82452fef310749e43d7d11661a943e2185594ad1de8c8446d33d968a`.
- S045's own anchor snapshot exists and matches its stated digest/size: `.ufo/waves/round-67/source-snapshots/dex-format.html` sha256 `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4` (row text: same digest) and `281157` bytes (`wc -c`; row text: "281157 bytes"). The snapshot is tracked at HEAD (`git ls-files` lists it).
- Newness vs claim base: set diff of ids, `fa0eb3eb:corpus/SOURCES.md` → working tree, is exactly `44a45 > S045`; base has 44 rows and zero `S045` occurrences.

## Fleet validator — `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh` (sha256 `3fb7261569f46423dd80ecc23e0a23789a7926f667c7a3fc559d2439d4a64e30`)

`validate --root /home/vgpnk/Projects/shokunin revenger`, run with cwd `/home/vgpnk/Projects/shokunin`:

```
revenger	W04	S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes
revenger	W04	S028 duplicate url github.com/ethereum/execution-specs/tree/v2.20.0/src/ethereum/forks/osaka/vm across scopes
revenger	W04	S029 duplicate url tc39.es/ecma262 across scopes
revenger	W04	S034 duplicate url pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT across scopes
revenger	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
```

- **exit 0**; stderr empty; E-codes 0, W-codes 4 (all W04, all pre-existing rows, none naming S045). Per the script header W01–W04 are warnings that never change a clean lane's status; E01–E12 (malformed/id/dup/kind/tier/status/opened/recheck/community-A/used-by-missing/row-outside-Registry) produced nothing.
- `census revenger` independently agrees: `rows 45`, `tier.A 43`, `tier.C 2`, `status.mined 37`, `status.queued 4`, `status.rejected 4`, and FLEET roll-up `rows 45 / missing 0 / tier.invalid 0 / status.invalid 0`; exit 0.

## Build-state cross-observations (freshness, not a judgement)

- README C05 is **not** flipped: `corpus/README.md:34` still `| C05 | Android packages (APK) | — | fixtures/apk-r65; retained rejected candidate knowledge/round-65-apk-axml-byte-evidence.md … | uncovered |` and names no round-67 entry — consistent with the claims' admission order (candidate lands, flip only on all-pass).
- This seat judged registry shape only. It did **not** evaluate entry content, C7 gate behavior, Q01–Q13, or the counter; those are other seats' claims.

## Tooling

No installs or upgrades (bash/coreutils/gawk/python3/stdlib only). Pacman untouched.

## Risks / limits

- W04 duplicates (S024/S028/S029/S034) are pre-existing and warning-only; if the L1 intends a zero-warning census, they are outside the seven frozen checks and fail no frozen promise.
- The census validates registry structure, not claim content; a `mined` row with an existent-but-wrong used-by target passes command 7 by design (S045's target hash is recorded above for the content seats).
- The brief's "SOURCES.md §Census" pointer is stale (see Provenance); anyone replaying from that pointer alone will find no commands.
