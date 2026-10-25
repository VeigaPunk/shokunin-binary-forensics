DRAFT-READY — a gate-clean C07-deepening candidate entry exists at `.ufo/waves/round-70/w1/R70W1AssimDraft.draft-entry.md` (5/5 embedded blocks re-derive, lint 0/0/0/0), carrying only the package entry's claims 3-5, each re-fetched today from unblob's own `README.md` and each grounded in a printed command.

# R70W1AssimDraft — assimilation draft (addendum section 10)

Seat: leaf, no dispatch. Time-boxed. Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Writes made: this report and the draft entry only.

## 1. What was produced

| path | bytes | role |
|---|---|---|
| `.ufo/waves/round-70/w1/R70W1AssimDraft.draft-entry.md` | 16252 | candidate entry: header trio, `coverage-map: C07`, `admission-status: candidate`, observation/inference/unknown, limitation, full 15-row §Q-map, §Reproduce |
| `.ufo/waves/round-70/w1/R70W1AssimDraft.md` | this file | seat report, plus the draft SOURCES rows and Gate-block lines (§4) |

Nothing else in the lane was written. No git/jj mutation was issued anywhere; every git call this seat made was read-only `git show`/`cat-file` (via the two gate tools) in the lane.

## 2. The source, opened today

Command and exact output (this is the draft entry's item 1):

```
$ python3 -B -c "import hashlib,urllib.request as u;b=u.urlopen('https://raw.githubusercontent.com/onekey-sec/unblob/main/README.md').read();print('bytes',len(b));print('lines',b.count(b'\n'));print('sha256',hashlib.sha256(b).hexdigest())"
bytes 7580
lines 235
sha256 6544d60f22f7b521f8705b3bba5d47a50e428ccbd3359542708dbd009ccf3716
```

Fetched `2026-10-25T21:07:37Z` (`date -u`), HTTP 200, `curl -w` printed `bytes 7580`. The whole document (235 lines) was read, not only the quoted bullets. No SWGDE document was opened — its claims are out of scope for this lane (§6).

## 3. The three retained claims, each located under its heading

All four quotes below are printed with their 1-based line numbers by the draft entry's item 2:

```
sections [(20, '## Features'), (35, '## Installation'), (37, '### pip (recommended for most users)'), (91, '### From source')]
quotes [(22, '- **78+ supported formats** — archives, compression streams, and file systems including SquashFS, JFFS2, UBI/UBIFS, ext, CPIO, ZIP, 7-Zip, gzip, XZ, LZMA, LZ4, and many more. See the [full list](https://unblob.org/formats/).'), (100, 'Requires Python ≥ 3.10, [uv](https://docs.astral.sh/uv/), and a Rust toolchain (for the compiled extensions).'), (46, 'sudo apt install android-sdk-libsparse-utils e2fsprogs p7zip-full unar zlib1g-dev liblzo2-dev lzop lziprecover libhyperscan-dev zstd lz4'), (161, '  --show-external-dependencies    List required external tools and their status.')]
```

- **Package claim 3 (format count).** `## Features` line 20 → first bullet line 22: ≤25-word quote `78+ supported formats — archives, compression streams, and file systems including SquashFS, JFFS2, UBI/UBIFS, ext, CPIO, ZIP, 7-Zip, gzip, XZ, LZMA, LZ4` (22 words). The same figure recurs once in the lede at line 5. Derivation of the named-list size and the sibling figures (draft entry item 3):
  ```
  named_families 11
  named_list SquashFS JFFS2 UBI/UBIFS ext CPIO ZIP 7-Zip gzip XZ LZMA LZ4
  apt_packages 11
  flag_occurrences 3
  ```
  So the bullet names 11 families and ends `and many more`: the named list is not the count.
- **Package claim 4 (runtime).** `### From source` line 91 → last line 100: quote `Requires Python ≥ 3.10, uv, and a Rust toolchain (for the compiled extensions)` (14 words).
- **Package claim 5 (extractor set + verification command).** `### pip (recommended for most users)` line 37 → line 46, the 11-package apt line (quote `sudo apt install android-sdk-libsparse-utils e2fsprogs p7zip-full unar zlib1g-dev liblzo2-dev lzop lziprecover libhyperscan-dev zstd lz4`); `unblob --show-external-dependencies` occurs 3× (lines 59, 97, 161), described at line 161 as `List required external tools and their status`.

## 4. Draft SOURCES rows (11 columns, no `|` in any cell) and Gate-block lines

Two rows, because the probe is this seat's own run and must not be cited as the document's statement. **Both ids are PROVISIONAL** — the registry tail is S047, so S048/S049 are next-unused as of this seat's read; a sibling wave-1 draft may claim the same ids, and the L1 must reserve before appending (§7 F4).

```
| S048 | unblob upstream README — https://raw.githubusercontent.com/onekey-sec/unblob/main/README.md | docs | A | the project's own stated figures for its supported-format count, its runtime requirements and its Ubuntu/Debian external-extractor install line, on branch `main` as fetched 2026-10-25; not extraction capability, not handler correctness, not behavior on any image | `## Features` line 22, `### pip (recommended for most users)` line 46, `### From source` line 100, CLI reference line 161; branch `main`, fetched 2026-10-25, 7580 bytes, sha256 6544d60f22f7b521f8705b3bba5d47a50e428ccbd3359542708dbd009ccf3716 | unblob states 78+ supported formats (naming 11 families and `many more`), requires Python 3.10+ with uv plus a Rust toolchain for its compiled extensions, and names an 11-package apt install line with a command that reports external-tool presence | mined | 2026-10-25 | 90d | corpus/knowledge/round-70-unblob-upstream-figures.md |
| S049 | Own-work host probe of one installed unblob, run by `R70W1AssimDraft` on 2026-10-25 — commands in the citing entry's items 6 and 7 | own-work | A | the exit status and dependency rows that `unblob --show-external-dependencies` printed for unblob 26.6.4 on this host on 2026-10-25; not any other version, platform or earlier host state, and not extraction capability | the citing entry's items 6-7 print `unblob --version` = 26.6.4, exit 1, 15 rows, 5 found, 10 missing, and the 15 names; tool installed the same day by `uv tool install --force unblob` | the offered verification command runs and reports 15 required executables with 10 absent on this host, which is the observed state and not a capability statement | mined | 2026-10-25 | 90d | corpus/knowledge/round-70-unblob-upstream-figures.md |
```

Gate-block lines for `corpus/lessons/round-70.md` `## Gate` (round-69 §Gate shape; every quote ≤25 words, every number derived above):

```
### Source rows opened this round (CORPUS.md rule 1: URL or command, access date, located quote)

- **S048 (new row, docs, tier A; id provisional until appended).** What was opened:
  `https://raw.githubusercontent.com/onekey-sec/unblob/main/README.md`, branch `main`,
  fetched 2026-10-25 by `R70W1AssimDraft`: 7580 bytes, sha256
  `6544d60f22f7b521f8705b3bba5d47a50e428ccbd3359542708dbd009ccf3716` (entry item 1).
  Access date **2026-10-25**. Located quotes, each printed with its line number by entry
  item 2 — line 22 `78+ supported formats — archives, compression streams, and file
  systems including SquashFS, JFFS2, UBI/UBIFS, ext, CPIO, ZIP, 7-Zip, gzip, XZ, LZMA, LZ4`;
  line 100 `Requires Python ≥ 3.10, uv, and a Rust toolchain (for the compiled extensions)`;
  line 46 `sudo apt install android-sdk-libsparse-utils e2fsprogs p7zip-full unar zlib1g-dev
  liblzo2-dev lzop lziprecover libhyperscan-dev zstd lz4`.
- **S049 (new row, own-work, tier A; id provisional).** What was opened: this host's
  `unblob 26.6.4`, by `R70W1AssimDraft` on 2026-10-25. `unblob --show-external-dependencies`
  exits **1** and lists **15** executables, **5** found and **10** missing (entry items 6-7).
  The binary was installed by this seat the same day (`uv tool install --force unblob`); the
  pre-existing `~/.local/bin/unblob` symlink dated 13 October was dangling before that.

Registry changes (append-only fields, logged old → new):

| row | field | old | new | reason |
|---|---|---|---|---|
| S048 | (new row) | — | `mined`, opened `2026-10-25`, `90d`, used-by `corpus/knowledge/round-70-unblob-upstream-figures.md` | the entry cites it; row and entry must land in one commit or census W03 fires (reason recorded for S047 in `lessons/round-69.md` §Gate) |
| S049 | (new row) | — | `mined`, opened `2026-10-25`, `90d`, used-by `corpus/knowledge/round-70-unblob-upstream-figures.md` | the probe is own-work and must not be cited as the document's statement; same landing commit |
```

Landing note: `used-by` names `corpus/knowledge/round-70-unblob-upstream-figures.md` — the proposed landing path for this draft. If the L1 lands it under a different name, both `used-by` cells change with it.

## 5. Checks actually run on the draft (not on any lane file)

Both lane tools were run read-only against the draft path:

```
$ python3 -B corpus/lint_entry.py --entry .ufo/waves/round-70/w1/R70W1AssimDraft.draft-entry.md
LINT_QMAP=0
LINT_Q14=0
LINT_Q15=0
LINT_HEADER=0
lint_exit=0
$ python3 -B corpus/check_embedded_outputs.py --entry .ufo/waves/round-70/w1/R70W1AssimDraft.draft-entry.md
checked_blocks=5 problems=0
gate_exit=0
```

`checked_blocks=5` matters beyond the count: `check_embedded_outputs.py:71-73` refuses any block whose argv[0] is not a Python interpreter, so the draft's five blocks are all argv-safe `python3 -B -c` invocations. A block of the form `unblob --show-external-dependencies` would have made the gate exit 2; the probe is therefore wrapped in a Python `subprocess` call that prints the tool's exit status (1) while the Python process itself exits 0.

Column shape of the two SOURCES rows, checked by command on this report's own text. The pattern matches four lines: the two 11-column registry rows of §4 and the two 5-column rows of the §4 registry-change table, so the 11 is read off the first two lines only:

```
$ awk -F'|' '/^\| S04[89] /{print $2, NF-2}' .ufo/waves/round-70/w1/R70W1AssimDraft.md
 S048  11
 S049  11
 S048  5
 S049  5
$ grep -c '^| S04[89] ' .ufo/waves/round-70/w1/R70W1AssimDraft.md
4
```

`NF-2 = 11` on the registry rows is the column count *and* the no-`|`-inside-a-cell check: an embedded pipe would raise the field count above 11.

## 6. Provenance decisions (what I dropped and why)

- **Package claims 1-2 (SWGDE) dropped.** The package entry's `source:` line cites S096 (SWGDE 12-F-003-2.0) — an id from the shokuknow campaign, not from this lane's registry (`corpus/SOURCES.md` tail is S047; `grep -n 'S096\|S099' corpus/SOURCES.md` exits 1, no output). This lane holds no SWGDE row and none was opened, so the SWGDE half is out of scope exactly as the assignment states. Nothing in the draft asserts a SWGDE fact.
- **The "supersedes the FSTM 30+ and community 300+ figures" framing dropped.** Both superseded figures have no row in this lane's `corpus/SOURCES.md`:
  ```
  $ grep -n 'OWASP\|FSTM\|300+' corpus/SOURCES.md
  (no output, exit 1)
  $ grep -n 'unblob\|Unblob' corpus/SOURCES.md
  99:- REA firmware guide (`docs/firmware-analysis.md`, Binwalk 3.1.x / Unblob 26.6.x requirement) — read by the scout, not yet a row; open it when the firmware family is claimed.
  ```
  The only unblob mention is a lead note saying the REA firmware guide "is not yet a row" — so neither unblob nor the two superseded figures had a registry row before this draft. A supersede statement needs the superseded row to exist; the draft claims only the upstream figure and records the omission under Unknown.
- **Claim 5 narrowed, not repeated.** The package entry says the README's command lets one "verify the set". The probe shows what the command actually does — it reports 15 executables and their presence, and it does not map them back to the 11 apt packages. The draft states the narrower fact and puts the mapping under Unknown.

## 7. Findings for the L1 (advisory, wave 1 — no kill-rule input)

- **F1 — the frontier-step census command named in the frozen contract does not exist in the lane.** `reports/round-70/claims.md` §Frontier step says `SOURCES census before/after (scripts/sources-census.sh validate)`. Evidence:
  ```
  $ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && find . -maxdepth 4 -name '*census*'
  ./.ufo/waves/round-64/scout-census.md
  ./.ufo/waves/round-70/census-before.txt
  $ ls -d scripts
  ls: cannot access 'scripts': No such file or directory
  $ sed -n '1,60p' scripts/sources-census.sh
  sed: error opening input file 'scripts/sources-census.sh': No such file or directory (os error 2)
  ```
  Consequence for my slice: the two draft rows could not be validated by the named validator; the 11-column shape above is checked by `awk`, and the W03-consumer rule is honoured by landing the rows with the entry. Either the script lives elsewhere and the contract's path is stale, or the frontier step's "before/after" cannot be produced as written.
- **F2 — the package entry's recorded host state was stale on this host; reported verbatim.** `digest-scope-versus-provenance-amendment-2026-10-23.md` records "`unblob --version` reports `26.6.4`". Before this seat installed anything:
  ```
  $ command -v unblob
  (no output; "error: command not found: unblob")
  $ ls -l /home/vgpnk/.local/bin/unblob
  lrwxrwxrwx 1 vgpnk vgpnk 51 Oct 13 13:53 /home/vgpnk/.local/bin/unblob -> /home/vgpnk/.local/share/uv/tools/unblob/bin/unblob
  $ ls -d /home/vgpnk/.local/share/uv/tools/unblob*
  ls: cannot access '/home/vgpnk/.local/share/uv/tools/unblob*': No such file or directory
  ```
  i.e. a dangling symlink from 13 October: the recorded version was not obtainable from this host's `PATH` until this seat installed the tool. The draft's Limitation states the install provenance so no reader mistakes the probe for a pre-existing host fact.
- **F3 — "verify the set" is weaker than the package entry implies.** The tool's own report lists 15 executables; the README's apt line names 11 *packages*. Four reported executables — `jefferson`, `partclone.restore`, `ubireader_extract_files`, `ubireader_extract_images` — are not the name of anything in that line or in the README's separate sasquatch section (the remaining two of the 15-minus-5 missing set, `sasquatch` and `sasquatch-v4be`, are covered by that section). The mapping was not derived, so the draft records it as Unknown rather than as a defect of the README.
- **F4 — provisional S-ids.** S048/S049 are next-unused at this seat's read of the registry tail (S047). Wave-1 siblings drafting their own rows may claim the same ids; the L1 must reserve ids before appending, or two rows will collide in one append.
- **F5 — landing dependency.** The draft's items 2-3 fetch over the network. The gate passes today (`checked_blocks=5 problems=0`) but is not hermetic. Landing should commit `corpus/snapshots/unblob-README.md` at sha256 `6544d60f…` and re-point items 2-3 to the snapshot, mirroring the S032 snapshot pattern; the draft's §Reproduce says so.

## 8. Tool installs / updates made by this seat

- `uv tool install --force unblob` — uv `0.13.0` (`/home/vgpnk/.local/bin/uv`), channel: `uv tool` (PyPI, official project distribution), resolved `unblob==26.6.4`. Reason: run the document's own verification command as an *independent* derivation of the dependency set (Q03) and as the Q05 probe, instead of only restating the README's apt line. The first attempt failed with `error: Executable already exists: unblob` because of the dangling symlink in F2; `--force` replaced it. No pacman transaction was issued (all paused host-wide); no host service was restarted.

## 9. Out of scope / not done

- No lane corpus, reports, SKILL.md, SHONEN.md, SCORECARD.md or LOG.md file was written, edited, committed or pushed; no sibling lane or fleet path was written.
- No extraction, emulation or mount was run; no firmware fixture was touched.
- The package entry's SWGDE document was not fetched (out of scope).
- Not verified by this seat: whether the draft would survive wave-2 Q decisions (that is wave 2's job), and whether the `78+` figure matches the installed package's handler registry (not derived; a separate probe would be needed and is not claimed).
- `/tmp/revenger-r70-R70W1AssimDraft-unblob-README.md` (the fetched copy used while drafting) is deleted before return.
