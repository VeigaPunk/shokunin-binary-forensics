# ExecR90SourceCheck — SOURCES.md dead repo-path instrument (r89 routed D1)

VERDICT: instrument built; red over the base-rev corpus archive names exactly one dead row, S481 `corpus/live/runs/round-89/receipt.json` (relocation target exists at `reports/round-89/rejected-android-record/receipt.json`); selftest 10/10 legs pass; no `/tmp` literal.

Base read: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-90/claims.md` (C1/C2 frozen at c7767789). This item is out of the C1/C2 counters; no frozen instrument or predicate touched.

## Files (all under /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ExecR90SourceCheck/)
| file | sha256 |
|---|---|
| `source_path_check.py` | 3cbd4329fc7096a64ff9a1efff8166a9ee2dbb738b1b449b04ed3424f02537a2 |
| `red.log` (corpus-only archive, as specified) | fd6985a770c940725e05408f375ced6e1486c52023a4760f42972fcd790600e1 |
| `red-fulltree.log` (full `git archive` of the same rev) | bb9e65b82d6c67ef0c34c3852923d9c75e40d9a1282e689718d50fa5f9683df0 |
| `selftest.log` | dbcbd2993c647081d845b44fd91ad23d8009b74c4b4265f1334a40528ec783a2 |
| `controls.log` (3 mutation controls on the real tree) | 25dcae95499466c21f179491a44331236d2e31e54471cdbaae5fb4a74a09e7b9 |

Also: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ExecR90SourceCheck.md` (Report trailer, same content).

## Tool behaviour (rules are in the docstring, declared before data)
- `--root TREE`: parses `TREE/corpus/SOURCES.md` `## Registry` rows (0-3 leading spaces before `|`, through blank lines, until the next `## `); splits on unescaped `|`; rows with ≠11 cells or a non-`S<digits>` id are printed as `MALFORMED` and counted (`SOURCE_PATH_MALFORMED`), not checked.
- Path spans = backticked tokens in the `source` cell; a span with whitespace contributes its first word (`corpus/.../entry_checks.py --spec-quotes` → the path). Skipped: `http://`, `https://`, `~/`, `/…`, drive `X:/`, `AppData/`, spans with `* ? { } [ ] $ < > …`.
- **Anchor rule (design decision, not in the item text):** a span counts as repo-relative only if its first `/`-segment is an existing entry at TREE root. The registry's source cells carry 78 backticked non-repo or shorthand spans in the full tree (commands such as `rea --llms`, commit ids, external-repo paths like `dist/domain/apple/appleArchiveFormat.js` (S463, relative to the AppData npm package) or `skills/reverse-engineer-anything/references/android-applications.md` (S039/S043, relative to morluto/rea), sibling shorthand `round-21`, `evm-r26`, `v4-prelanding-recon.log`). Without the anchor rule all of these would be false DEADs. They are counted in `SOURCE_PATH_UNANCHORED_SPANS`, never as dead.
- Resolution: file or directory under TREE after realpath; escaping TREE never resolves.
- Excuse: a dead S<id> is EXCUSED iff a later row's `teaches` or `source` cell matches `\bsupersedes\s+S<id>(?![0-9A-Za-z_])` AND that row has ≥1 anchored span and none dead.
- Output `DEAD <id> <path>`, `EXCUSED <id> by <id2>`, counters, `SOURCE_PATH_DEAD=<n>`; exit 0 iff n==0, 1 if n>0, 2 if SOURCES.md missing, 64 usage.
- Scratch: `tempfile.mkdtemp` (honours `TMPDIR`); `grep -c /tmp source_path_check.py` → 0.

## Selftest (`selftest.log`, exit 0)
Legs: clean-resolves rc0; dead-row rc1; dead-superseded-by-resolving rc0 (EXCUSED); dead-superseded-by-dead rc1 (both DEAD); prefix-id `supersedes S48` does not excuse S481 rc1; 2-space indented row parsed rc1; URL source ignored rc0; `supersedes` in the source cell excuses rc0; an EARLIER superseding row does not excuse rc1; missing SOURCES.md rc2. Each fixture also carries a `| S999 | \`corpus/no\` |` row under a later `## Search log` heading that must not be parsed. `SOURCE_PATH_SELFTEST=pass`.

## Red (rev 77574c99845ab6662812bd6a88def1e72bf8d71b)
`red.log` — `git archive 77574c99 corpus` in scratch:
```
DEAD S481 corpus/live/runs/round-89/receipt.json
SOURCE_PATH_ROWS=482  SOURCE_PATH_ROWS_CHECKED=30  SOURCE_PATH_UNANCHORED_SPANS=98
SOURCE_PATH_MALFORMED=0  SOURCE_PATH_EXCUSED=0  SOURCE_PATH_DEAD=1   exit=1
```
`red-fulltree.log` — full archive of the same rev (repo-relative paths into `.ufo/`, `reports/`, `LOG.md` become checkable): identical verdict, `SOURCE_PATH_ROWS_CHECKED=38`, `UNANCHORED_SPANS=78`, `SOURCE_PATH_DEAD=1` (S481 only).

Caveat on the corpus-only tree: spans into `reports/`, `.ufo/`, `LOG.md` (e.g. S001, S014, S042, S448, S465-S473, S480, S482) are unanchored there because those roots are absent, so they are not checked. The full-tree run checks them and finds them all resolving. **Recommendation to L1:** gate on the full lane tree (or `git archive <rev>` with no pathspec), not the corpus-only archive.

### Every DEAD id, with relocation search (by filename `receipt.json`, 21 hits in the full tree)
| id | dead path | relocation target in tree? |
|---|---|---|
| S481 | `corpus/live/runs/round-89/receipt.json` | **yes**: `reports/round-89/rejected-android-record/receipt.json` (sha256 0afe9eea35bfc1b3cb7b82c8bd3a22de0f7cf26c1ec0f449ff7b7b49b6fada1f, byte-identical to the seat copy `.ufo/waves/round-89/w1/ExecR89Record/receipt.json`; its line 20 still carries the anchor `"stdout_sha256": "01af3141…6c76"` the row cites as `:20`). `corpus/live/runs/` has no `round-89` entry at this rev. `reports/round-89/rejected-android-record/LEDGER.md:145` records the move. |

## Controls on the real tree (`controls.log`; scratch copies of the full archive with one row inserted after S482)
- `good`: S900 cites `reports/round-89/rejected-android-record/receipt.json`, teaches `supersedes S481` → `EXCUSED S481 by S900`, DEAD=0, exit 0. This is the minimal registry fix shape.
- `prefix`: same row with `supersedes S48` → S481 still DEAD, exit 1.
- `deadsup`: superseder cites a non-existent `reports/round-89/receipt.json` → S481 and S900 both DEAD, exit 1.

## Risks / limits
- False-negative class (stated): a dead path whose top-level segment is itself gone or misspelt (e.g. `corpu/…`) is reported as unanchored, not dead. Shorthand sibling spans (`round-21`, `v4-prelanding-recon.log`) are not expanded. `CORPUS.md` (S472) is unanchored: no `CORPUS.md` exists anywhere in the tree, so it is prose naming, not a resolvable path.
- `anchor` cells (e.g. S481's `corpus/live/runs/round-89/receipt.json:20` in its anchor column) are not checked; the item scopes `source` only. Fixing S481 by a superseding row leaves the dead locator in S481's anchor text, which is append-only history.
- Only a row's own source paths decide whether it can excuse another row; superseder chains are not followed.

## Tooling
No installs or upgrades. Python 3.14.8 (host). Scratch `/fast/scratch/hyaku/revenger-r90/ExecR90SourceCheck` (TMPDIR set there) was deleted before yield. No lane byte outside this report dir and the trailer file was written; no git mutation.
