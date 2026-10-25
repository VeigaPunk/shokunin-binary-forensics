BYTE-IDENTICAL — regenerating `corpus/fixtures/apk-r65` reproduces `fixture.apk` and `truth.json` with zero byte difference on this host (both sha256 unchanged), and the committed `fixture.apk` sha256 equals the v2 entry header's claim.

Seat: R67FixtureHold (leaf, read-only on the lane). Item: fixture immutability hold, void-condition surface for round 67.

Axes named: (1) artifact-byte reproducibility of the frozen claim surface; (2) interpreter-version provenance (the only field that can legitimately move); (3) claim-surface agreement (entry header vs committed bytes); (4) environment insensitivity (TZ/locale/hash seed); (5) absence of write side effects on the lane.

## Environment

- `python3 --version` → `Python 3.14.8`
- Host: `linux 7.2.11-arch1-1`, x64. Date at measurement: `2026-10-24T21:33-03:00`.
- Committed baseline: lane HEAD `7668510ffc49733daf023e40ff3300ef387ebde5` (read via `git rev-parse HEAD`).
- Scratch: `/tmp/revenger-r67-seat-fixture` (the one named scratch dir). A second sibling scratch (`/tmp/revenger-r67-seat-fixture-b`) was created only for the environment-varied run below and deleted after its hashes were recorded; it no longer exists (`ls -d /tmp/revenger-r67-seat-fixture*` → only the named dir).

## Committed baseline (before any regeneration)

`sha256sum` over the working tree, which `git status --porcelain -- corpus/fixtures` reports clean (empty output) and `git diff --stat -- corpus/fixtures/apk-r65` reports empty (exit 0):

```
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk
eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a  corpus/fixtures/apk-r65/generator.py
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  corpus/fixtures/apk-r65/truth.json
```

Committed blobs at HEAD (`git show HEAD:corpus/fixtures/apk-r65/<f> | sha256sum`) are byte-identical to the four lines above — same four digests, no working-tree-only drift.

Whole-directory receipt (sorted `sha256sum` lines over the four files, hashed): `61f737d236e99035676d7cbdbb88a12967170a969577aadd8967ac61dfb9c667`. This is the value the L1 can re-derive for the void-condition check "Changed `corpus/live` or `corpus/fixtures` bytes".

Unchanged-since-round-65 proof: `git log --oneline -- corpus/fixtures/apk-r65` returns exactly one commit, `c7b7cf9` (round 65), and `git diff --stat c7b7cf9..HEAD -- corpus/fixtures/apk-r65` is empty (exit 0). This matches the entry's "bytes unchanged since `c7b7cf98`" claim at `corpus/knowledge/round-67-apk-axml-byte-evidence.md:5`.

Wave-window evidence: mtimes are `fixture.apk 2026-10-24 02:37:29`, `generator.py 02:36:56`, `readout.py 02:39:41`, `truth.json 02:37:29` (-0300), i.e. ~19 h before this wave's activity — no seat in this wave touched the directory. `git status --porcelain -- corpus/fixtures` was empty again after all of my runs.

## Regeneration (the assigned command, verbatim)

```
$ cp -a /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65 /tmp/revenger-r67-seat-fixture
$ cd /tmp/revenger-r67-seat-fixture && python3 -B generator.py
fixture.apk 947 bytes sha256 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e
member AndroidManifest.xml offset=0 size=416 crc32=962d075f
member classes.dex offset=465 size=112 crc32=2635c82a
member META-INF/MANIFEST.MF offset=618 size=69 crc32=e948d738
gen_exit=0
```

Post-run hashes in the scratch tree:

```
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  fixture.apk      (947 B)
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  truth.json      (2466 B)
eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a  generator.py
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  readout.py
```

## Byte comparison (before/after)

`cmp` of each regenerated file against the committed original — all four exit 0:

```
CMP_APK=identical        (947 B: 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e, before == after)
CMP_TRUTH=identical      (2466 B: 27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173, before == after)
CMP_GEN=identical
CMP_READOUT=identical
```

`truth.json` difference: **none at all on this host** — zero bytes differ, and the before/after sha256 are the same string (`27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173`). No normalization was needed or applied.

## Claim-surface agreement (entry header)

- Entry frontmatter row `corpus/knowledge/round-67-apk-axml-byte-evidence.md:4` declares fixture sha256 `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` (947 bytes) → **matches the committed file exactly**.
- Entry body `…:20` repeats the same digest → matches.
- Entry `…:16` declares `readout.py` sha256 `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976` → matches the committed script.
- Entry `…:166` (and frontmatter `…:6`) declares the `readout.py` stdout contract "Exit 0; 15 stdout lines; SHA-256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247`". Executed over the frozen bytes from the lane root:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py   # exit=0 stdout_bytes=5099 stderr_bytes=0 stdout_lines=15
stdout_sha256=507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247
```

  Exact match. Stdout contains no absolute paths (`grep -c '/home/\|/tmp/'` → `0`), consistent with the entry's "carries only repo-relative paths, never the extraction root" (`…:6`).
- `readout.py` reads its own directory (`corpus/fixtures/apk-r65/readout.py:20-21` `ROOT = Path(__file__).resolve().parent`; `APK = ROOT / "fixture.apk"`; `:44` `apk = APK.read_bytes()`), so this run read the committed fixture, not the scratch copy.

## Environment-varied determinism

Second scratch copy, generator run under a scrubbed environment (`env -i PATH=/usr/bin:/bin TZ=UTC LC_ALL=C PYTHONHASHSEED=0 HOME=/tmp python3 -B generator.py`), exit 0, printed the same four lines including `fixture.apk 947 bytes sha256 05d2280f…7d03e`. `cmp` results: first-run vs second-run `fixture.apk` identical, `truth.json` identical; second-run vs committed `fixture.apk` identical, `truth.json` identical. So the output is insensitive to TZ, locale, hash seed, HOME and cwd — as `generator.py:30` (`DOS_DATE_TIME = (2026, 10, 24, 12, 0, 0)`) and the `ZIP_STORED` in-memory container (`generator.py:166-171`) predict. Scratch dir removed after recording.

## Oracle coherence under the frozen bytes (independent re-derivation)

Independent `zipfile` walk of the frozen `fixture.apk` (not using `readout.py`), compared against `truth.json`:

```
AndroidManifest.xml: bytes=416 sha256=73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4 matches_oracle=True
classes.dex:         bytes=112 sha256=57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2 matches_oracle=True
META-INF/MANIFEST.MF: bytes=69 sha256=2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49 matches_oracle=True
all_members_match_oracle= True
image_sha256= 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e size= 947
central_dir_order= ['AndroidManifest.xml', 'classes.dex', 'META-INF/MANIFEST.MF']
```

Each row matched on sha256, uncompressed size and CRC-32 simultaneously (`truth.json:73-108`). The oracle therefore describes the frozen bytes; a byte-preserved fixture cannot be paired with a drifted oracle here.

## Side-effect audit

- `readout.py` performs no writes: no `open(`, `write(`, `ZipFile(` or temp-file call anywhere in the script (grep over the whole file returns nothing); the only I/O is `read_bytes()` at `:44` plus `print`. Confirmed by the zero-byte stderr above and by `git status --porcelain -- corpus/fixtures` staying empty.
- `generator.py` writes only two files, both relative to its own directory (`HERE`): `APK_PATH.write_bytes(apk)` at `:197` and `TRUTH_PATH.write_text(...)` at `:226` (`APK_PATH`/`TRUTH_PATH` defined `:28-29`). It never wrote to the lane: it ran only in `/tmp`, and the lane's fixture bytes are unchanged after the run (same four digests, empty `git status`/`git diff` for the path).
- No file outside `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67FixtureHold.md` and the named scratch dir was written by this seat. No git/jj mutation was run (only `rev-parse`, `show`, `log`, `diff`, `status`, `grep` — all read-only).

## Tooling

No tool was installed or upgraded by this seat. `python3` 3.14.8 and coreutils `sha256sum`/`cmp` were already present; no pacman transaction was attempted (host-wide pacman pause respected).

## Risks / caveats (calibration)

1. **`truth.json` byte-identity is interpreter-version-conditional by construction.** `generator.py:219` embeds `platform.python_version()` into `build_recipe.python_version`, and `truth.json:67` records `"3.14.8"`. On this host the runtime is exactly `3.14.8`, so the field reproduces and `truth.json` is byte-identical. On any other interpreter patch/minor, `truth.json` would legitimately differ in that one string while `fixture.apk` would still be expected identical (fixed DOS date-time, `ZIP_STORED`, authored member bytes). The hold as specified ("truth.json may differ ONLY in nothing at all on this host") is satisfied — the qualifier is doing real work and the match is not accidental: the recorded version equals the runtime version exactly.
2. **`fixture.apk` identity is demonstrated only on this host/this interpreter.** I did not and cannot test other Python versions here; the byte-level argument (no timestamps inside members, fixed DOS date-time `:30`, `ZIP_STORED` `:166`) is inspected, not exhaustively proven across interpreters.
3. **Frozen bytes are a live shared surface.** This report certifies the directory at `2026-10-24T21:33-03:00` (tree digest `61f737d2…c667`). Any later write by another seat would invalidate it; the L1 should re-derive the four digests (or the tree digest) at the final measured commit for the void-condition check.
4. Not in scope here and deliberately not judged: the entry's item-level claims (hex capture, S038/S043/S045 anchors, Q08 row) belong to the C1 critics; the C7 gate belongs to the mutant/separability seats. This seat asserts only the fixture-byte surface.

## Pointers

- `corpus/fixtures/apk-r65/fixture.apk` — 947 B, sha256 `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`.
- `corpus/fixtures/apk-r65/truth.json` — 2466 B, sha256 `27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173`; recipe at `:49-67` (`python_version` `:67`), image digest `:69-72`, members `:73-108`.
- `corpus/fixtures/apk-r65/generator.py:28-30` (paths, fixed DOS date-time), `:166-171` (in-memory `ZIP_STORED`), `:197` (`APK_PATH.write_bytes`), `:219` (`platform.python_version()`), `:226` (`TRUTH_PATH.write_text`).
- `corpus/fixtures/apk-r65/readout.py:20-21,44` (self-relative read), no write sites.
- `corpus/knowledge/round-67-apk-axml-byte-evidence.md:4,6,16,20,166` (the verified claims).
- Evidence artifacts in the named scratch dir: `readout.stdout`/`readout.stderr` (first run, stderr 48 B = an xtrace line only, not script output), `readout3.stdout`/`readout3.stderr` (clean re-run, stderr 0 B).
