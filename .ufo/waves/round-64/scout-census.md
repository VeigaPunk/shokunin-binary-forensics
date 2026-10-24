# Round-64 SOURCES baseline census

Axes: validator exit status; source-row cardinality; disclosed-warning identity; complete output capture.

## Validator receipt

Command (executed exactly):

```text
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger
```

Working directory: `/home/vgpnk/Projects/shokunin/revenger-shokunin`

Exit code: **0**

Stdout, every line (tabs preserved):

```text
revenger	W04	S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes
revenger	W04	S028 duplicate url github.com/ethereum/execution-specs/tree/v2.20.0/src/ethereum/forks/osaka/vm across scopes
revenger	W04	S029 duplicate url tc39.es/ecma262 across scopes
revenger	W04	S034 duplicate url pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT across scopes
revenger	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
```

Stderr: empty (0 bytes).

## Row census

Specialized regex tool over `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md`:

```text
^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|
```

Matched rows: **35**. IDs: S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035. Matches occupy lines 15–49 in the observed SOURCES snapshot `C9EF`. Count obtained from the regex tool's starred matching lines, not its surrounding context lines.

Expression discrepancy in the seat brief: the printed pattern uses doubled braces:

```text
^\|[[:space:]]*S[0-9]{{3,}}[[:space:]]*\|
```

That literal pattern returned `No matches found` through the specialized regex tool. The 35-row result uses the normal three-or-more quantifier `{3,}`. Shell `grep -cE` was not invoked because the higher-priority tool policy requires the specialized grep device; no GNU-grep exit code is claimed.

## Findings

- Observed: validator exit 0 and exactly four W04 lines, for S024, S028, S029 and S034, matching the frozen baseline disclosure.
- Observed: all 35 baseline IDs S001–S035 appear once in the source-row matches. No S036/S037 row was present in this snapshot.
- Interpretation: the current baseline passes structural validation with the four disclosed cross-scope duplicate-URL warnings; exit 0 does not mean warning-free or certify source quality.
- Remaining gap: this receipt is the 35-row baseline, not the required future after-append census for S036/S037.

No source or production files changed. No installs or upgrades. No git/jj commands.
