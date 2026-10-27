# R71W2SpotcheckDraft — source-decision sample for the non-author closure spotcheck

**Verdict.** Draft table agrees with the round-71 sample: **ADMIT S052** (own-work `--spec-quotes` stdout, tier A, scope = output shape only) and **REJECT S053** (CPython `zipfile` docs, tier A, not load-bearing for this C05 entry) — both reproduced at lane HEAD; two scope caveats recorded below, neither reverses a decision.

**Role.** I am a lane-dispatched scribe in round-71 wave 2 (`R71W2SpotcheckDraft`). I am **not** the outside/non-author verifier, and this draft is **not** discernment evidence: it neither claims non-author agreement nor replaces the closure's independent re-open. It edits no lesson, no `SOURCES.md` row, no entry, no counter, and writes no vote file (not a reviewer seat). The canonical decisions remain the frozen `reports/round-71/claims.md` and the wave-2 Q01–Q16 votes.

## State

- Lane `/home/vgpnk/Projects/shokunin/revenger-shokunin`; HEAD `c6e284c6583fa3502754361f411b66646880ba02`, TREE `cfae4cfc2cc8348f86df9de2662e27afeca8f055`. Named candidate/build commit in my assignment is `4c1eeaee88fd07e442f1bd546faf77be3957d390`; `c6e284c` is the later freeze commit on the same line (`git log b7abcd8..HEAD`: 18200a4 build v6 → da4f1ee timeout fixture path → 620849e integrate sources/controls → 4c1eeae integrate W1 repairs/counter → c6e284c freeze wave).
- Base `b7abcd875c84f4e1d6c8df966b6bd20f4154c53f` (pre-registration). Command inputs are unchanged base→HEAD: `git diff --stat b7abcd8 HEAD -- corpus/fixtures/apk-r65 corpus/snapshots corpus/derive_axml_anchors.py` prints nothing (exit 0), so the reproduced stdout is the same at both points.
- No source/lesson file was modified by this seat; the only write is this untracked report.
- **Working-tree delta in my sampled rows is not mine.** At report time `git status` shows `M corpus/SOURCES.md`, and `git diff --word-diff=porcelain corpus/SOURCES.md` prints exactly: S052 `used-by` `-corpus/knowledge/round-71-apk-axml-byte-evidence.md` / `+…, corpus/lessons/round-71.md`; S053 teaches `-format-layout` / `+format/layout`; S053 `used-by` `-—` / `+corpus/lessons/round-71.md`. My table and quotes describe the **committed HEAD** state (`c6e284c`), where S053 `used-by=—`; the uncommitted edit is another seat's in-flight write, reported verbatim for L1, not adjudicated and not applied by me.

## Decisions

| Source | Decision | Exact anchor | Quote (words) | Reason |
|---|---|---|---|---|
| **S052** — `entry_checks.py --spec-quotes` stdout, `kind=own-work`, `tier=A`, `status=mined`, `recheck=90d`, `used-by=corpus/knowledge/round-71-apk-axml-byte-evidence.md` — `corpus/SOURCES.md:66` | **ADMIT** | `corpus/fixtures/apk-r65/entry_checks.py --spec-quotes`, exit 0, six `MATCH` lines; revision = lane base `b7abcd8…`; representative line `MATCH dex-format.html: first line 5035, …` at stdout line 5 of 6 | `MATCH dex-format.html: first line 5035, folded phrase present=True: uint ENDIAN_CONSTANT = 0x12345678;` (12) | Contract tier-A explicitly covers “the lane's own re-runnable gate output”. Scope is bounded to what the command actually prints — snapshot file, first-word line number, folded-presence flag, and the queried phrase — and the entry uses it only for that shape (item 11, Q01). Reproduced byte-identically by this seat, so the row is re-runnable, not an author assertion. |
| **S053** — `zipfile` docs, CPython 3.15.2 — https://docs.python.org/3/library/zipfile.html, `kind=docs`, `tier=A`, `status=rejected`, `recheck=on-release`, `used-by=—` — `corpus/SOURCES.md:67` | **REJECT** (as support for this C05 entry) | Page title `zipfile — Work with ZIP archives — Python 3.15.2 documentation`; intro under `<h1>`/`# zipfile — Work with ZIP archives` (`id="module-zipfile"`, live HTML span `id="zipfile-work-with-zip-archives"`) | `This module provides tools to create, read, write, append, and list a ZIP file.` (14) | The entry makes no Python `zipfile` API claim: `grep -c zipfile corpus/knowledge/round-71-apk-axml-byte-evidence.md` → **0**, and the readout does not import it (`corpus/fixtures/apk-r65/readout.py:13-18` imports `hashlib, json, struct, sys, zlib` only). Its ZIP layout claims rest on APPNOTE S032/S034 plus fixture bytes (entry `source:` line 4; item 12). Row is formatted per contract (`REJECTED: <reason>; flip: <what would change the verdict>`) and carries the flip condition. |

## Commands and observed output

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes    # EXIT=0
MATCH rea-android-applications.md: first line 7, folded phrase present=True: Start with `inspect_android_package` on the caller's APK path for package identity, manifest declarations, coverage, and inline Evidence.
MATCH dex-format.html: first line 5949, folded phrase present=True: adler32 checksum of the rest of the file (everything but magic and this field)
MATCH dex-format.html: first line 5956, folded phrase present=True: SHA-1 signature (hash) of the rest of the file (everything but magic, checksum, and this field)
MATCH dex-format.html: first line 5981, folded phrase present=True: must be 0x70 (112) bytes (v40 or earlier)
MATCH dex-format.html: first line 5035, folded phrase present=True: uint ENDIAN_CONSTANT = 0x12345678;
MATCH ResourceTypes.h: first line 686, folded phrase present=True: Byte offset from the start of this structure where the attributes start
```
- Entry block vs live: extracted the fenced block under `corpus/knowledge/round-71-apk-axml-byte-evidence.md:144` and compared with fresh stdout → `entry_lines 6 live_lines 6 identical True`; the S052 quote occurs exactly once in the entry (`occurrences_of_quote_in_entry 1`) and is 12 tokens.
- Live S053 fetch: `curl -sL --max-redirs 10 https://docs.python.org/3/library/zipfile.html` → `HTTP=200 BYTES=139782`, `sha256 e5eaebbea4ebde68e4759d94d54add4241968068f28996367cd07fb0d8ef9378`, `<title>zipfile — Work with ZIP archives &#8212; Python 3.15.2 documentation</title>`; rendered intro text contains the quoted sentence verbatim in that order.
- Registry/row checks: `corpus/SOURCES.md` S052 line 66 (`mined`, `2026-10-27`, `90d`, used-by the v6 entry) and S053 line 67 (`rejected`, `2026-10-27`, `on-release`, `used-by=—`); row count 53 (`grep -c "^| S0"`), matching `census-after.txt` (51→53; A 48→50; rejected 4→5; 0 malformed, tier-inflation empty, mined used-by empty).
- Source validation mirrors: `.ufo/waves/round-71/sources-s052/validate.log` and `sources-s053/validate.log` each end `ok …/corpus/SOURCES.md` with EXIT=0; warnings disclosed are W04 duplicate-URL rows plus W01 S051. `scripts/sources-census.sh:33` documents W04 as a warning that does not affect a clean lane; S053's W04 is the expected same-URL-as-S044 case (`corpus/SOURCES.md:58`, supersedes S044). The `validate/` mirrors are now empty dirs (the temporary mirror was removed after validation, as the logs state), so the logs are receipts, not re-runnable trees.

## Caveats the closure should weigh (no decision reverses)

1. **S052 prints the query, not the file's bytes.** The printed phrase is the author-supplied search argument echoed with a folded-presence flag and the first-word line number; for one-line phrases it happens to equal the raw source line (the 5035 case). The row's “not the raw source line” is epistemically right, and entry item 11 words it correctly (“the searched phrase itself”), but a reader could over-read the echoed text as extracted file content. Credit stays: presence + first-line number only.
2. **S053 has no committed snapshot.** Only the live fetch above grounds it (`e5ea…`, 139782 bytes). S044's row (`corpus/SOURCES.md:58`) cites snapshot `sha256 e7fe6715…, 139782 bytes` titled 3.15.1, yet `corpus/snapshots/` contains no zipfile file, so S044's snapshot pointer is not re-checkable from the lane. Same byte count but different digest here means the version string, not the body, moved 3.15.1→3.15.2; no byte-identity claim is made, and `recheck=on-release` is the right cadence for this moving unversioned URL. Recorded as an adjacent observation, not a verdict on S044.
3. **S052 tier-A narrowness.** It is defensible only because the claim scope is the command's own stdout and the run is reproducible from committed inputs; it can never support spec content. Entry Q01 (`corpus/knowledge/round-71-apk-axml-byte-evidence.md:299`) states exactly that limit.

## Scope and non-evidence

- Read-only for sources: no `SOURCES.md`, lesson, entry, counter or vote-file edit; scratch `/fast/scratch/hyaku/revenger-r71/R71W2SpotcheckDraft/` used only for the live fetch and removed after the run.
- This seat does not adjudicate C1, C2, Q01–Q16, or any hold; it answers no L0 question, spawns nothing, and does not stand in for the outside verifier's independent re-open or for the fresh wave-2 votes.
- Tooling: none installed or updated; no pacman transaction; `curl`/`python3` from the host as-is.

Report: .ufo/waves/round-71/w2/R71W2SpotcheckDraft.md
