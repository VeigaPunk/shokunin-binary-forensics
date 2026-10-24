# R64ScribeGate — report

Seat: scribe `revenger-r64.R64ScribeGate`, round 64 attempt 1 (hyaku).
Date: 2026-10-24. Bounds honored: no git/jj mutations, no commits/pushes, no
edits to wave spec/registry files, MANIFEST.json, fleet repo, sibling lanes, lane
jj state or Git index. Files written: the two paths this brief names (deliverable
and this report). No installs (no tool was fetched or upgraded).

## Deliverable

`.ufo/waves/round-64/gate-quotes.md` — 7264 bytes, sha256
`0228a73081f70335ac2dcd010162e1d45e9160993e5e9d5b0f136dff23990c7c`.

Contents:

- **S036 block** — 13 located quotes from the pinned-tag REA firmware-analysis
  guide, each verbatim against the whitespace-normalized snapshot, each ≤25 words
  (observed word counts 9–20), with snapshot line numbers, URL, access date
  2026-10-24, HTTP 200, 10695 bytes, sha256
  `e422b4816b1dbc912680afefb8e23acfd8ead4aea08c3d722d4ccb5207933609`, pinned tag
  commit and blob ids, scoped tier A (route-scope sentences only), and the
  recorded pinned-tag-vs-`main` divergence.
- **S037 block** — computed digests (this seat, `sha256sum`/`stat`, no provider
  rerun):
  `firmware-r63.bin` 2048 B `bdfe9f46…8510be`; `truth.json` 1933 B
  `9663f90b…a65e6`; `inspection.json` 3904 B `f6997835…aa71f9`; `receipt.json`
  492 B `e930a549…c6b94d`. Supplementary: `generator.py` 5532 B
  `4e5d5975…93db4`, `LEDGER.md` 22671 B `25a4a18b…1e1a6`, `stdout.raw` 3904 B
  `f6997835…aa71f9`.
- **Status flips** — README C07 observed `frontier` (not yet flipped); new state
  `held` on all-criteria admission (fallback `uncovered` if C1 falsifies).
  Registry rows S036/S037 observed absent (35 rows, last `S035`) → append
  `queued` → `mined` on landing with `used-by` citation; verification command
  included.

## Commands and outcomes (exact, in run order)

1. `read` of brief, `reports/round-64/claims.md`, `measure.py`,
   `measure-before.log` — contract loaded; red-before matches the brief
   (`K_HELD_BACKED=7/14`, `README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']`,
   `C4_RECEIPT_KILLED_ATTRIBUTED=0/2`, exit 0/`HOLDS_OK=yes`).
2. First existence check at 01:17:
   `ls -la .ufo/waves/round-64/source-snapshots/` →
   `No such file or directory`. Scratch scan found
   `/tmp/revenger-r64-src/rea-firmware-guide.md` (10695 B) +
   `headers.txt` (`HTTP/2 200`, `content-length: 10695`,
   `date: Sat, 24 Oct 2026 04:17:17 GMT`).
3. Recheck minutes later: `.ufo/waves/round-64/source-snapshots/` had been
   created by the source-opening seat with `rea-firmware-guide.md` (10695 B,
   sha256 `e422b481…93609`) and `rea-firmware-guide.provenance.json`
   (1919 B, sha256 `59b10f04…d7722`). `cmp` against the scratch copy →
   `BYTE_IDENTICAL_TO_QUOTED_COPY`; so the quotes were derived from a copy
   byte-identical to the canonical landed snapshot, and re-verified against the
   canonical path.
4. Provenance read: URL
   `https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/docs/firmware-analysis.md`,
   requested ref `rea-agents-6.5.0`, HTTP 200, `content-type: text/plain;
   charset=utf-8`, access date 2026-10-24, tag commit
   `3b79af28e80785afce9f5998d8f03289402a1847`, blob
   `152819177f8dce2124dea2a6a541e701cee227ed`, line count 213, tier "A for
   route-scope sentences only", `installs: none`.
5. Quote verification: a Python substring/word-count check over the landed
   snapshot printed `verbatim=True` and `OK` for all 13 quotes (max 20 words).
6. S037 digests + cross-checks (Python, `json`/`hashlib`, stdlib only):
   `receipt.fixture_sha256 == image == truth.image.sha256 ==
   inspection.subject.digest.sha256` (True);
   `receipt.stdout_sha256 == sha256(inspection.json)` (True);
   `cmp inspection.json stdout.raw` → identical;
   `receipt.evidence_id == inspection.evidence_id` (True,
   `ev_aae7529f…0ed259`); `inspection.operation` = `inspect_firmware_regions`;
   `inspection.provider` = Binwalk 3.1.0; `truth.image.size` = 2048;
   `truth.regions` = 5 entries / 2 zlib members; `receipt.command` names
   `rea-agents@6.5.0`.
7. Registry/README state: `grep -cE '^\| S[0-9]{3,}' corpus/SOURCES.md` → 35;
   last rows `S034`, `S035`; no `S036`/`S037`. `corpus/README.md:36` →
   `| C07 | firmware images | — | — | frontier |`.
8. `stat`/`sha256sum` on the deliverable; `git status --porcelain` on
   `gate-quotes.md`, `corpus/README.md`, `corpus/SOURCES.md` → only
   `?? .ufo/waves/round-64/gate-quotes.md` (README/SOURCES untouched).

## Gates

- Quote gate (contract v1 rule 1): 13/13 quotes are verbatim substrings of the
  whitespace-normalized snapshot; 13/13 ≤25 words; every quote carries a line
  number; URL, access date, HTTP status, byte count and sha256 recorded. PASS.
- Provenance gate: canonical snapshot present; sha256 recomputed and equal to
  the provenance sidecar and to the quoted copy; `cmp` byte-identical. PASS.
- S037 digest gate: 4/4 required files hashed by this seat; 7/7 correspondence
  checks True. PASS (observation layer only; no rerun).
- Bounds gate: two writes, both brief-named; no mutations detected. PASS.

## Findings

1. **Snapshot timing (resolved).** The canonical S036 snapshot was absent at my
   first check and landed during the run (same minute window). The brief's
   "record the dependency and return" branch was therefore not needed: the
   landed snapshot is byte-identical to the copy on which the quotes were
   located. No dependency remains.
2. **Revision collision worth carrying to L1.** `.ufo/waves/round-63/source-snapshots/rea-firmware-guide.md`
   and `.ufo/waves/round-64/source-snapshots/rea-firmware-guide.md` share a
   basename but are **different revisions**: round-63 holds `main`
   (15474 B, sha256 `d4a25c85…f16a898`, lead only); round-64 holds the pinned
   `rea-agents-6.5.0` tag (10695 B, `e422b481…93609`). The round-64 provenance
   file states this explicitly; the Gate block repeats it so the lesson cannot
   silently cite `main`.
3. **`inspection.json` is `stdout.raw` verbatim** (3904 B, identical bytes), and
   `receipt.stdout_sha256` binds it. This is stronger than "the record was
   saved": the receipt's stdout conjunct is satisfied by the file actually on
   disk. It remains internal consistency, not producer-origin proof (S036 lines
   86–87; ledger discipline applies).
4. **C07 token and registry rows are still old-state at scribe time.** The
   flips in `gate-quotes.md` are prospective, as the contract intends
   (admission-then-flip). If C1 falsifies, the fallback token is `uncovered`,
   not `held`.
5. **Binwalk version alignment is observed, not attested.** `inspection.json`
   reports Binwalk 3.1.0, matching the S036 sentence that parsers were verified
   with Binwalk 3.1.0; the snapshot also states a matching version does not
   attest the build's source revision. The Gate block carries both quotes so the
   lesson does not over-read the match.

## Known limits / out of scope

- This seat did not author, correct, admit or judge the C07 candidate; no
  Q01–Q13 decision is made or implied here.
- The S036 quotes are route-scope evidence only; they say nothing about the
  fixture bytes, and the S037 digests prove only that the observed files are
  the ones hashed at scribe time.
- The lesson `corpus/lessons/round-64.md` does not exist yet (L1 lands it); this
  deliverable is its Gate input, including the required old→new status log.
- No counter run, no provider invocation, no build/test/lint was performed by
  this seat (none is its assignment).

## Artifact paths

- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/gate-quotes.md`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/source-snapshots/rea-firmware-guide.md` (read-only, landed by sibling)
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/source-snapshots/rea-firmware-guide.provenance.json` (read-only)
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/R64ScribeGate.md` (this report)
