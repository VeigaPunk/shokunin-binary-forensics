# R63LessonDraft — corpus/lessons/round-63.md draft

Seat: `revenger-r63.R63LessonDraft` (scribe, build wave, round 63, attempt 1).
Date: 2026-10-23.
Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.

## Deliverable

| item | value |
|---|---|
| draft path (seat scratch; L1 lands it) | `/tmp/revenger-r63-lesson/round-63.md` |
| sha256 of the draft | `7dda3ff86ab9c06eef760b3f72a211a6f913a1095ce47a3861699a4a59bcbf8d` |
| size | 25798 bytes / 250 lines |
| target landing path | `corpus/lessons/round-63.md` (L1-only; this seat wrote nothing under `corpus/`) |

The draft is a **draft for L1**: it admits nothing, flips nothing, and edits no
`corpus/` file, `.ufo/waves` spec/registry file, `MANIFEST.json`, fleet repo
file, sibling lane, lane jj state or lane Git index.

## What the draft contains

1. **Frontmatter** — `round: 63`, `date: 2026-10-23`, `author: revenger-r63`,
   `claims: [C1, C2, C3]`, plus the claim base, the frozen contract commit and
   the frozen counter's sha256, and an explicit `status: draft for L1`.
2. **`## Gate`** —
   - *Sources opened*: **S032** (PKWARE APPNOTE.TXT 6.3.10) with URL, access
     date 2026-10-23, HTTP 200, byte-exact snapshot path + sha256
     `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`, and
     **nine located quotes, each ≤25 words, each verified verbatim against the
     whitespace-normalized snapshot** (my own re-verification, not a copy of
     the opener's assertion). The fallback URL's revision divergence (6.3.9,
     different sha256, byte-identical quoted sections) is recorded, not
     smoothed.
   - **S033** (Python `zipfile` docs) — recorded as **screened-and-excluded, no
     registry row**, with the reason: the C06 readout is raw `struct` reads
     (`grep -c 'import zipfile'` = 0 in both the build readout script and the
     candidate readout), so no entry sentence credits `zipfile` behavior.
   - *Candidate status* — **C06 candidate drafted in scratch, not landed and not
     admitted** (`/tmp/revenger-r63-entry/candidate.md`, sha256
     `630b974a51e0f6ab815a5806a0f415b3f07089df91923dde3a78b6fd49904c7e`, citing
     S032 + S034); README C06 stays `partial`; C2 and C3 carry build-stage green
     evidence with their receipts, and their admission remains L1's
     frozen-counter measurement.
   - *Id allocation flagged for L1* — the draft records that the contract's
     "S033 if used" resolves to **screened-and-excluded, no row**, with the
     deciding seat `R63SourceZipfileDocs` confirming that in-band (exclusion
     line recorded verbatim in the lesson, plus its 19-word located quote
     "Any advanced use of this module will require an understanding of the
     format, as defined in PKZIP Application Note."); that the C06 candidate
     names **S032** and a reserved **S034** (own-work bytes + saved record); and
     that this leaves **S033 unused** — whether to append contiguously is L1's
     decision, so the draft states the gap rather than hiding it. The seat's
     caveat is recorded with its resolution: `truth.json`'s `build` field names
     `zipfile.ZipFile(...)`, so quoting it as a recorded oracle label keeps the
     exclusion, while asserting module behavior would need the S033 row the
     seat holds in reserve (§7). The candidate as drafted asserts no module
     behavior and does not quote the `build` field.
   - *Admission order* — land without the flip → fresh falsify wave → adjudicate
     → flip C06 only on all-criteria pass → measure on a committed archive.
   - *Quality criteria* — Q01–Q13 unchanged, `corpus/QUALITY.md` byte-identical
     to the claim base, ten-verifier census stays 10.
3. **`## Mistakes`** — three rows:
   - **M33** `stale-premise` — evidence: the L1 pre-probe of 2026-10-23
     (binwalk 3.1.0 signature scan finds zero regions in a 1056-byte
     uImage-header image while finding an offset-512 zlib region), plus the
     located mechanism from `R63ScoutFirmware` (zlib signature is `short:
     true`, so the default scan misses a nonzero-offset member and
     `--search-all` finds it; `uimage` needs known enums **and** a valid header
     CRC **and** a matching data CRC) — captured-by **Q05/Q06** — fix:
     the fixture generator is restricted to binwalk-3.1-detectable members
     (`78 da` zlib at offsets 512 and 1024 of a 2048-byte inert image) with a
     byte oracle able to fail (offset shifted by one → `MISMATCH … expected
     512, got 513`; last region dropped → `MISMATCH … expected 2 reportable
     regions, got 1`; second physical image → `MISMATCH subject.digest.sha256`).
   - **M34** `counter-substitution` — the frozen counter can print all three
     targets without any of the claimed work (`R63CriticClaims`); the claim
     text, not the counter, is the gate.
   - **M35** residual unguarded clause — the `stdout_sha256` conjunct in
     `verify_icon_states.py` survives deletion (`R63MutC3` M3), so C3 is
     credited only for the two frozen conjuncts it demonstrably detects and the
     third is named as unguarded (debt, not a claim extension).
4. **`## Search log`** — two prose notes with the unit stated explicitly
   ("one proposed registry document set"): the archive-specification query
   (identified 3 / screened 3 / included 1 row / excluded 2, each exclusion
   with its reason) and the firmware-fixture-premise query (identified 3 /
   screened 3 / included 0 rows / excluded 3, each with its reason). Both name
   their openers.
5. **`## Routed debt`** — a table whose first row is the round-62 closure
   defect (a): the on-tip counter re-verification is committed **alongside the
   report claim** as `reports/round-63/measure-after.log` on the final tip, not
   only as a mid-round revision; `measure-before.log` stays the red-before
   receipt. Four further routed items are recorded as reported-not-absorbed:
   the counter's `HOLDS_OK` wording drift (`R63SimplifierProbe` D1), the
   unguarded `stdout_sha256` conjunct, the sibling scope on archives/firmware
   (ADJ-06 open, no province sentence edited), and the not-yet-performed
   outside spot-check.
6. **`## Tooling`** — none installed or upgraded; no pacman transaction; only
   the already-present `binwalk 3.1.0`, `python3 3.14.8` and read-only `curl`.

## Evidence I exercised myself (read-only, lane-local)

| command | observed |
|---|---|
| `sha256sum .ufo/waves/round-63/source-snapshots/{appnote.txt,zipfile.html,rea-firmware-guide.md}` | `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`, `9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739`, `d4a25c8569b37c3d030431333db08fc459af54a163af7815b4505cce2f16a898` |
| `curl -sS -L` on the primary APPNOTE URL (twice) | HTTP 200, 174585 bytes, sha256 `0b993022…` both times — snapshot == served bytes |
| `curl -sS -L` on the fallback APPNOTE URL | HTTP 200 → redirect to `APPNOTE-6.3.9.TXT`, 173575 bytes, sha256 `c7cf1fec…`, version 6.3.9 (Jul 15 2020) — different revision, recorded |
| Python: verify each drafted quote is a verbatim substring of the whitespace-normalized snapshot and ≤25 words | all nine quotes: `in_snapshot=True`, word counts 7/21/7/8/23/24/23/12/20 (all ≤25) |
| `binwalk --version` | `binwalk 3.1.0` |
| rebuilt a 1056-byte magic-only uImage (big-endian `0x27051956` + 992 zero payload) and ran `binwalk` and `binwalk -a` | both exit 0, **zero regions** — the M33 red-before reproduced |
| built a 1056-byte uImage with valid header CRC **and** known OS/CPU/type/compression enums, plus a sweep over 980 enum combinations | the CRC-valid variant **is** detected (`offset 0, size 1056, name uimage`); the magic-only variant is not — the premise defect is the unverified assumption, not a missing signature |
| built zlib streams at offset 512 with headers `78 da` / `78 9c` / `78 01` / raw deflate and scanned | `78 da` and `78 9c` at 512 are found **only** with `binwalk -a` (196 magic patterns); `78 01` and raw-deflate are not found at all; the default scan (187 patterns) reports nothing at a nonzero offset — the located mechanism behind M33 |
| `grep -c 'import zipfile'` on `.ufo/waves/round-63/build/zip-readout.py` and on the candidate `/tmp/revenger-r63-entry/readout.py` | 0 and 0 — the basis for screening S033 out with no row |
| `grep -n 'S032\|S033' corpus/SOURCES.md` | no match — the registry still ends at S031, so both rows are *drafted for L1*, not appended |
| `grep -n 'C06' corpus/README.md` | row 35 still `| partial |` — no premature flip |
| `git status --porcelain` (lane) | only the two C3 verifier edits plus the new `.ufo/waves/round-63/`, `corpus/fixtures/firmware-r63/`, `corpus/live/runs/round-63/` paths — no out-of-scope lane write |

## Sources of the draft's build-wave facts

Everything asserted about the build wave is cited to a committed build report
under `.ufo/waves/round-63/build/`: `R63SourceAppnote` (S032 row + Gate
record + snapshot provenance), `R63ScoutFirmware` (M33 red-before and the
signature mechanism, REA 6.5.0 envelope), `R63ScoutArchive` /
`R63ZipPremise` / `R63ZipReadout` (C06 premise and byte readout),
`R63FirmwareFixture` / `R63FirmwareRun` / `R63FirmwareOracle` /
`R63ReviewFirmware` (C2 fixture, real run, oracle, independent review),
`R63C3NamedPatch` / `R63C3IconPatch` / `R63MutC3` (C3 fix and attributed
kills), `R63CriticClaims` (M34), `R63ScoutRecordRecon` (F predicate),
`R63ReviewSeparability` (flip mechanics), `R63CriticHarms` (guard checks),
`R63SimplifierProbe` (counter drift D1), `R63ConnectorOverlap` (sibling
scope), `R63Preservation` (preservation manifest), `R63ReviewGateFinal`
(build-wave gate).

Where a seat's own report had not landed at draft time, the draft says so
rather than assuming: the S033 decision is recorded with its reason and names
the deciding seat's report path; the C06 candidate is recorded as pending with
the premise artifacts named.

## Out of scope / not done (deliberate)

- `corpus/lessons/round-63.md` was **not** written — L1 is the sole integrator
  of `corpus/`; the draft sits in seat scratch.
- `corpus/SOURCES.md` was **not** edited — no S032/S033 row appended, no
  existing row changed, no `status`/`recheck`/`used-by` in-place change logged
  (the S032 row arrives as `queued` and becomes `mined` only when the C06 entry
  lands; L1 logs that old→new change in this lesson).
- `corpus/README.md` was **not** touched — C06 stays `partial` until the fresh
  falsify wave's named Q01–Q13 decisions land.
- `corpus/QUALITY.md` was **not** touched — Q01–Q13 unchanged; M33 was captured
  by the existing Q05/Q06, so no new criterion row is proposed.
- No verifier was re-patched, no fixture or saved record was edited, no
  producer run was repeated, no target was executed.
- No `pacman`, `uv tool install`, npm global install or binary download; no
  `~/.omp/agent/config.yml` or routing-table edit; no model arguments set.

## Cleanup

Seat scratch `/tmp/revenger-r63-lesson/probe/` (the M33 reproduction binaries
and the two APPNOTE fetches) is removed after this report lands. The lesson
draft itself stays in scratch until L1 lands it as `corpus/lessons/round-63.md`;
if L1 prefers, the draft can be moved from
`/tmp/revenger-r63-lesson/round-63.md` into the lane tree at landing time, and
the sha256 above identifies the exact bytes this report describes.
