# R64ReviewEntryQ01 — Q01/Q02 admission review of the C07 candidate

Seat: fresh-seat reviewer (not the candidate author). Criteria under review: `corpus/QUALITY.md:13` (Q01)
and `corpus/QUALITY.md:14` (Q02), read verbatim:

- Q01 — "Each load-bearing claim rests on a `corpus/SOURCES.md` row that is tier A **for that claim's
  scope** and was opened in the round that wrote it. A tier-C row is never sole support."
- Q02 — "The entry opens with `source:` (its `S###` row, URL or path, exact anchor), `verified-at:`
  (date or commit) and `recheck:` (the command or citation that re-verifies it), and names the
  coverage-map row it fills (`corpus/README.md`)."

## Verdict

| criterion | verdict | basis |
|---|---|---|
| Q01 | **FAIL (not evaluable on the artifact; pre-conditions fail)** | candidate absent at both briefed paths; its two load-bearing rows S036/S037 do not exist in `corpus/SOURCES.md` |
| Q02 | **FAIL (not evaluable on the artifact; pre-conditions fail)** | no headers exist to inspect; any `source: S036 —` / `S037 —` written now cites an absent registry row, i.e. no real anchor |

This is a recommendation, not an admission. No entry was judged on quality; nothing existed to judge.

## Findings

### BLOCKER-1 — candidate absent at both briefed paths (blocks Q01 and Q02 entirely)

Brief: "/tmp/revenger-r64-entry/candidate.md or, if integrated,
corpus/knowledge/round-64-firmware-region-byte-evidence.md". Observed:

- `/tmp/revenger-r64-entry/` — `ls` → "No such file or directory".
- `/home/…/revenger-shokunin/corpus/knowledge/round-64-firmware-region-byte-evidence.md` — absent;
  `corpus/knowledge/` newest entry is still `round-63-zip-central-directory-evidence.md` (2026-10-24 00:24).
- Lane `git status --porcelain` shows only ` M corpus/verify_icon_languages.py`,
  ` M corpus/verify_multi_icon_states.py`, `?? .ufo/waves/round-64/R64EntryCommands.md` — no candidate file.
- Sibling author seat report `.ufo/waves/round-64/R64EntryCommands.md` independently records the same
  absence ("candidate … absent from both locations specified by the seat brief", `commands extracted: 0`).
- `.ufo/waves/round-64/R64EntryC07.md` (author seat report) was not present either.

Consequence: Q01 has no claim to test and Q02 has no header line to read. Both are recorded failed until a
candidate exists; neither can be re-scored from this report.

### BLOCKER-2 — S036 and S037 are not registry rows (Q01 fails by construction if the candidate lands first)

`corpus/SOURCES.md` holds **35** rows matching `^\| S[0-9]+ `, ending at `| S035 |` (`corpus/SOURCES.md:49`).
No `| S036 |` and no `| S037 |` row exists. The search log still says, verbatim:

> `- REA firmware guide (`docs/firmware-analysis.md`, Binwalk 3.1.x / Unblob 26.6.x requirement) — read by`
> `  the scout, not yet a row; open it when the firmware family is claimed.` (`corpus/SOURCES.md:82`)

The round contract already assigns this append to L1 ("append S036 + S037 only after opening",
`reports/round-64/claims.md` §Frontier and routed debt). Supporting artifacts are also absent:
`.ufo/waves/round-64/sources-rows-draft.md` does not exist and `.ufo/waves/round-64/R64SourcesRows.md`
was not written.

Why this is Q01/Q02 and not cosmetic: Q02 requires the `source:` header to carry "its `S###` row … exact
anchor"; an `S036`/`S037` reference is a dangling id until the rows are appended, so the header's anchor is
not verifiable and Q01's "rests on a `corpus/SOURCES.md` row" is false. Dependency, not a judgment on the
author's drafting: **the rows must be appended before any Q01/Q02 PASS can be issued**, and a re-review
must cite the appended row numbers.

### HIGH-1 — correspondence scope trap: the saved record corroborates 2 of the 5 truth regions only

The record reports exactly two regions, both `signature` = `zlib` (offset 512 size 79; offset 1024 size 90),
`normalized_result.coverage` = `signature_scan`; keys are exactly `engine`, `input_size`, `regions`,
`coverage` (`corpus/live/runs/round-63/inspection.json`). The three padding spans exist only in
`truth.json` and in the bytes — the round-63 ledger says so itself: "The record's `coverage` is
`signature_scan` and it carries no padding region" (`corpus/live/runs/round-63/LEDGER.md:39`, O6), and
"the record … carries no per-member name and no decompressed digest" (`LEDGER.md:46`, I2).

A correspondence section claiming the record corroborates the five-region padding layout would exceed
S036's route-scope and S037's byte/record-correspondence scope → **Q01 fail**. PASS requires the
correspondence table to be two rows against the record (offset/size agree; decompressed size+sha256 agree
after a *checker-side* decompression, not as a record field) and padding stated as byte-derived only.

### HIGH-2 — staging-path trap in the record's raw layer

Inside `raw_result`, the subject appears as `/tmp/rea-firmware-7rPoLl/firmware.bin`
(`raw_result.report[0].Analysis.file_path`, and `raw_result.execution.args`), not as the lane fixture path.
The authoritative subject fields are `subject.local_path`, `parameters.path`, `subject.digest.sha256`
`bdfe9f46…10be`, `evidence_id` `ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259`, and
`receipt.json.fixture_sha256`. A `source:`/`Observation` anchor that quotes the `/tmp/rea-firmware-*` path
as the subject identity would be a false provenance claim (and a non-reproducible anchor) → Q02/Q01 hazard.

### MEDIUM-1 — provider UUIDs are not identities; `source_revision` is unknown, and that is supported

The pinned guide says "Binwalk signature UUIDs and Unblob blob IDs are producer-local identities; compare
content hashes and source ranges across runs" and "A matching version does not attest an installed build's
source revision, so that field remains unknown"
(`https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/docs/firmware-analysis.md:83-87`). The
record's `engine.source_revision` is `null`, consistent. An entry that treats `provider_id` values as
stable identities across runs, or that assigns a source revision, exceeds the row → Q01 fail.

### MEDIUM-2 — `recheck:` must be read-only; regeneration in place would break void condition 1

`truth.json` `build_recipe.command` is `python3 -B generator.py`, and I reproduced it: run inside a copy of
`corpus/fixtures/firmware-r63/` it rewrites `firmware-r63.bin` and `truth.json` in place with identical
bytes. Run in the lane fixture directory it would still count as touching frozen fixture paths, against
the contract's void condition "any changed `corpus/live` or `corpus/fixtures` byte outside new round-64
paths". The `recheck:` command should be a stdlib read-only readout (optionally regenerating into
`$TMPDIR` and byte-comparing), with its exact printed output and a stdout digest, as round 63 did.

### MEDIUM-3 — filename and column coupling with the frozen K probe

`reports/round-64/measure.py:33-34` counts a held row as backed only if the entry path matches
`knowledge/[\w.-]+\.md` in column index 3 (`l.split("|")[3]`) **and** the file exists under `TREE/corpus`.
The strict variant (`:46-48`) additionally drops entries carrying an `admission-status: rejected` marker.
So the integrated file must keep the exact name `corpus/knowledge/round-64-firmware-region-byte-evidence.md`,
the README row must cite it in the knowledge column (not the work-evidence column), and the row must still
end `| held |` — `K_HELD` matches `\| held \|$`. Any deviation leaves K at 7/14 while the claim says 8/14.

### MEDIUM-4 — the round-63 precedent already shows an M36-class token/evidence contradiction; do not copy it

`corpus/README.md:35` says C06 is `held`, while the cited entry's own header reads
`admission-status: candidate — drafted in the round-63 build wave for independent Q01–Q13 review; the
README C06 status flip is L1's and follows the fresh-seat decisions`
(`corpus/knowledge/round-63-zip-central-directory-evidence.md:8`). The new
`README_TOKEN_LEGEND_MISMATCH` label cannot catch this: `measure.py:72-75` tests only rows whose status is
`frontier`. If the C07 entry lands with the same candidate marker while C07 flips to `held`, the round
reproduces the exact defect M36 names (token contradicting its own evidence). The integrated entry should
carry an explicit admitted status naming the round-64 Gate decision (or the Gate must name the marker
change as the admission act), and the lesson should record the C06 instance alongside C07's.

### LOW-1 — `verified-at:` should pin the claim base, not the drafting time

`claims.md` fixes base `666ea84b6be2eec2b0359f556ba2429fc9044c36`. The header should state that base and
record the S037 file digests at it (below), because the two modified `corpus/verify_*.py` files in the
working tree are unrelated C2 work and must not leak into the entry's pinning.

## Substrate verification (independent, non-author — all PASS)

I re-derived the layout blind: a stdlib-only script (`zlib` + `hashlib`) over the fixture bytes, no author
readout script, no `generator.py` import.

| fact | independently derived | `truth.json` | record |
|---|---|---|---|
| image | 2048 B, sha256 `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be` | same | `subject.digest.sha256`, `input_size` 2048, `locations` 0–2048 |
| padding | (0,512), (591,433), (1114,934); all-zero; 1879 B total; no nonzero byte outside the two streams | same, `fill_hex` `00` | not reported (expected) |
| zlib #1 | off 512, consumed 79, out 78, sha256 `a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86` | same | offset 512, `reported_size` 79 |
| zlib #2 | off 1024, consumed 90, out 97, sha256 `2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9` | same | offset 1024, `reported_size` 90 |
| regeneration | `python3 -B generator.py` in `/tmp/revenger-r64-review-q01` → image `bdfe9f46…`, `truth.json` `9663f90b2b9f29c5beb621e554ed7584eedf5e77d4785f26a453e70dbd5a65e6` (identical) | `build_recipe` pins Python `3.14.8`, zlib compile/runtime `1.3.2` | host is exactly Python 3.14.8 / zlib 1.3.2 / 1.3.2 |
| receipt | `stdout_sha256` `f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9` = sha256 of both `stdout.raw` and `inspection.json`; `fixture_sha256` matches the bytes | — | yes |

Three-way byte agreement (fixture, oracle, record) holds, and `truth.json` is byte-accurate on every field
I derived. This discharges the round-63 ledger's open item U5 ("a non-author seat would have to re-derive
the regions", `LEDGER.md:55`) **for the bytes**; it does not make the oracle third-party — image, oracle
and generator were authored by one seat, so the entry must keep U5's independence caveat.

## S036 route-scope evidence (the only route-scope text an entry may lean on)

Fetched and hashed at the pinned tag — `https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/docs/firmware-analysis.md`,
sha256 `e422b4816b1dbc912680afefb8e23acfd8ead4aea08c3d722d4ccb5207933609`, 10695 B; tag
`rea-agents-6.5.0` → commit `3b79af28e80785afce9f5998d8f03289402a1847`; snapshot kept at
`/tmp/revenger-r64-review-q01/guide.md`. Verified sentences (line numbers in the snapshot):

- `:3-5` "REA accepts **Binwalk 3.1.x** for region inspection and **Unblob 26.6.x** for explicit
  extraction. The report parsers are verified with Binwalk 3.1.0 and Unblob 26.6.4. Another build on those
  lines is accepted, the observed version is reported, and a limitation records that the parser was not
  verified against that build." → the record's `binwalk` 3.1.0 is the verified build; route scope is
  version-bound, so the row must pin the tag, not `main`.
- `:91-94` "Region offsets refer to bytes in the original firmware. `reported_size` preserves Binwalk's
  output; `size_basis=provider_reported_validation_unknown` reflects that Binwalk can replace unknown
  lengths with the next signature or EOF before serialization. Neither a signature nor its confidence byte
  proves a valid partition, encryption or runtime behavior." → supports the offset/size/`size_basis`
  claims and *forbids* any authenticity/partition-validity claim (also matches the record's
  `limitations[0]`).
- `:83-87` "Both return Evidence with the original path and SHA-256, raw producer reports, actual
  executable path/digest, version and limitations." → supports the record's `engine.executable_path` /
  `executable_sha256` / version fields and the subject digest; and the producer-UUID / source-revision
  limits above.
- `:50` "Normal REA builds and npm packages do not include or build these sources or engine binaries." →
  explains why the npm 6.5.0 package (checked: `/home/vgpnk/.npm/_npx/ad9a3fdbcad992c6/node_modules/rea-agents`,
  version `6.5.0`) contains no `docs/`; the row's anchor must be the repo file at the tag, and a package
  copy is not a substitute snapshot.

The guide's `## Verification` section additionally states fixtures are generated into ignored
`_reference/` and "No binary fixture is committed" (`:176-189`), and that SquashFS/UBIFS/proprietary
formats remain unverified — usable as the entry's limitation, not as support for any broader claim.

## PASS checklist for the integrated entry (what a re-review will test)

1. `corpus/SOURCES.md` contains `| S036 |` and `| S037 |` with the anchors above (tag+section+sha256;
   six-file sha256 bundle) and both marked used by this entry.
2. Header lines 1–5: `source:` (S036 + S037, exact anchors), `verified-at:` (base `666ea84b…`), `recheck:`
   (stdlib-only, read-only, exact printed output + stdout digest), `coverage-map: C07`, `admission-status:`
   naming the round-64 Gate decision (not a stale `candidate` marker — MEDIUM-4).
3. Every load-bearing value carries its in-entry command and that command's output (Q11), and each printed
   value equals the independently derived table above.
4. Correspondence section: exactly two record regions; padding declared byte-derived; no record field
   invented (no per-member names, no decompressed digest as a record field).
5. Scope paragraph carries: one authored fixture only; no vendor image; no execution/extraction claim
   (record `extractions` = `{}`, `LEDGER.md:40`); no provider-completeness claim; no authenticity claim;
   binwalk-set-only statement (engine-dependent region set, `LEDGER.md:49` I5).
6. Observation / inference / unknown separation and at least one limitation (`QUALITY.md:32-33`).
7. No `/tmp/rea-firmware-*` path presented as subject identity; `evidence_id` + `subject.digest` +
   `receipt.fixture_sha256` are the identity handles.
8. No claim resting on `provider_id` as a cross-run identity, and no source revision asserted.
9. File name exactly `corpus/knowledge/round-64-firmware-region-byte-evidence.md`, cited in README column
   3, row still `| held |`, 14 rows unchanged (K probe `measure.py:33-34,46-48`).

## Residual risk

- **Author/oracle identity**: image, `truth.json` and `generator.py` share one author; my byte-level
  re-derivation removes transcription risk, not authorship risk. Q03 (blind independence) and Q09
  (digest-scope disclaimers) remain for other seats.
- **Engine dependence**: `unblob` 26.6.4 reports nothing on the whole image (`LEDGER.md:44` O11); any
  unqualified "the regions of this image" phrasing would be false. Not a Q01/Q02 defect by itself, but it
  is the most likely place a correct entry degrades into an over-claim.
- **`oracle_check.py` has no pinned digest** (it changed during round 63, `LEDGER.md:28`); if the entry
  cites it, the citation must be by path and behaviour, never by digest.
- **C2 scripts are dirty in the working tree** (`corpus/verify_icon_languages.py`,
  `corpus/verify_multi_icon_states.py`); an entry `verified-at:` that says "working tree" instead of base
  `666ea84b…` would be unpinnable.

## Verification gaps

- No candidate existed at either briefed path, so Q01/Q02 could not be scored on the artifact; the
  failures above are pre-conditions, and a later seat must re-run Q01/Q02 against the landed text.
- S036/S037 rows, `sources-rows-draft.md`, and the R64SourcesRows/R64EntryC07 reports were absent at
  review time; no dependency artifact was edited or created by this seat.
- I did not run `measure.py` (it is evaluation, not this seat's criterion) and did not invoke binwalk; the
  record-vs-bytes claims were checked from saved bytes and saved record only.

## Provenance

- Read-only on the lane: no git/jj mutation, no commit/push, no corpus file created or modified; the only
  lane write is this report. Scratch confined to `/tmp/revenger-r64-review-q01/` (fixture copy, regenerated
  image + oracle, pinned guide snapshot `guide.md`).
- No tool installed or upgraded (pacman untouched per the paused-host rule).
- Report path per contract: `.ufo/waves/round-64/R64ReviewEntryQ01.md`, relative to
  `/home/vgpnk/Projects/shokunin/revenger-shokunin`.

## Re-review — landed bytes, same identity (2026-10-24)

Scope: the landed entry `corpus/knowledge/round-64-firmware-region-byte-evidence.md`, sha256
`9bf21e5057b77f17a8406af9d006fb4594dd2da54c6d0920f4ca842cfa3e0ebf` (matches the announced corrected
digest), and the appended rows `corpus/SOURCES.md:83` (S036) and `:84` (S037). Both blockers from the first
pass are cleared: the candidate exists, and both rows are present (11 columns each, `status=mined`,
`date=2026-10-24`, `refresh=on-release`, `used-by` naming this entry; S037 also names
`corpus/lessons/round-64.md`). The registry now holds 37 `S###` rows.

### Verdict after re-review

| criterion | verdict | basis |
|---|---|---|
| Q01 | **PASS** | every load-bearing claim maps to S036 (route scope) or S037 (byte/record correspondence), both tier A for the scope used; no dangling S-id, no other row cited |
| Q02 | **PASS** | two `source:` headers with verified anchors, `verified-at:`, `recheck:` that reproduces exactly, `coverage-map: C07`; two LOW precision nits below, neither defeating the criterion |

Recommendation to L1: **admit**, optionally after the two LOW corrections. Admission authority stays with L1.

### Q01 — criterion evidence

| claim class (entry location) | row | scope fit, anchor verified |
|---|---|---|
| route identity and invocation (`rea inspect-firmware-regions <path>`) | S036 | guide line 56, quoted verbatim in the snapshot; row scope is "what `inspect-firmware-regions` returns and bounds per rea-agents-6.5.0" |
| accepted/verified engine version (Binwalk 3.1.x, parser verified with 3.1.0) | S036 | guide lines 3-5, verified verbatim; matches the record's provider `3.1.0` |
| region offsets are original-firmware bytes; `reported_size` is provider output; `size_basis=provider_reported_validation_unknown`; a signature/confidence byte does not prove a partition | S036 | guide lines 91-94, verified verbatim (citation range `91-96` overshoots by two lines — LOW-1) |
| Evidence envelope fields (original path + SHA-256, executable path/digest, version, limitations) | S036 | guide lines 83-85, verified verbatim |
| fixture, generator, oracle, record, receipt, ledger bytes at base `666ea84b…` | S037 | I recomputed all six with `git show <base>:<path> \| sha256sum` **and** `sha256sum <path>`: `bdfe9f46…`(2048), `4e5d5975…`, `9663f90b…`, `f6997835…`, `e930a549…`, `25a4a18b…` — all six equal the entry's item 2 output and the row's anchors |
| record-only facts (operation, provider version, two `zlib` regions, `coverage=signature_scan`, `size_basis`, empty `extractions`, no names/decompressed digests, one `Unblob` mention in `limitations[2]`) | S037 | reproduced by command; `region_count` 2, `names_present` False, `decompressed_digest_present` False, `extractions` `{}`, `unblob_lower` 0 / `unblob_upper` 1 — matches item 11 exactly |

Dangling-id check: the entry references only `S036` (9 occurrences) and `S037` (6); every other identifier is a
file path or a `Q` id. The cross-lane note disclaims source support explicitly ("no other lane's file is cited
as support for a value here"), and that holds: the fleet/sibling pointers support only the scope disclaimer,
and the one verbatim quote in it ("protocol integrator — kaidoku/revenger ownership unresolved") is present at
`tsukuroi-shokunin/PROVINCE.md:51` as claimed (the `l0-questions.md:42` pointer is loose — LOW-2).

Scope containment (the HIGH-1 hazard from the first pass) is now handled correctly: the record is matched on
exactly its two regions and its literal fields; the three padding spans and both decompressed digests are
presented as byte-derived only; the oracle's member labels are explicitly *not* byte-derived (item 6), and U6
states the oracle is not independent because one generator wrote both. No extraction, authenticity,
provider-completeness or general-format claim appears; limitation 4 restates S036's bounds.

### Q02 — criterion evidence

- Header lines 1-6 carry `source:` ×2, `verified-at:`, `recheck:`, `coverage-map: C07`, `admission-status:`.
  Each header is on one line; nothing is a bare homepage.
- **S036 anchor is real and independently reproducible.** `refs/tags/rea-agents-6.5.0` → commit
  `3b79af28e80785afce9f5998d8f03289402a1847` (re-checked with `git ls-remote`); file blob
  `152819177f8dce2124dea2a6a541e701cee227ed` re-derived offline with `git hash-object` on the in-repo
  snapshot `.ufo/waves/round-64/source-snapshots/rea-firmware-guide.md` — exact match; that snapshot's
  sha256 is `e422b4816b1dbc912680afefb8e23acfd8ead4aea08c3d722d4ccb5207933609` (10695 B), identical to the
  bytes I fetched from the tag URL. Quoted line numbers 3, 56, 83-85 all verified in that snapshot.
- **S037 anchor is real**: six digests at base `666ea84b…` (table above).
- **`recheck:` reproduces.** I extracted the `### Code` block verbatim to `/tmp/revenger-r64-review-q01/readout.py`
  and ran `python3 -B readout.py <lane-root>` from the lane root: exit 0, **7** JSON lines, stdout sha256
  `aa353251f7529a00c4336f9bf8cae6634838b8d10bd20e24b7340d94cf1314ae` — exactly the header's value, and
  identical on a second run (deterministic; the script prints with `sort_keys=True`). `--fact image` emits
  exactly one line. The script imports only `hashlib`, `json`, `sys`, `zlib`; its only file access is
  `open(..., "rb")`; it writes nothing.
- **Published values reproduce independently.** My own stdlib derivation (no author script) gives the same
  image digest/size, the same five-region partition, and for both members `78 da`, mod-31 check true,
  `FLEVEL` 3, `FDICT` 0, end-of-stream clean, Adler-32 trailers `7b3b1d2d` / `11bf252c` matching recomputation,
  inflated sizes 78 / 97 with digests `a5718481…` / `2d0d86aa…`, and plaintext equal to the oracle's
  `payload_utf8` strings. The entry's own disclosure that a whole-file zero-run rule would add a one-byte run
  at offset 1098 is accurate (byte 1098 is `0x00` between `0x79` and `0x76`).
- **Derived-vs-recorded splits are honest.** The readout prints 25 oracle checks and 13 record checks; I
  enumerated every row and confirmed the entry's 16/9 and 5/8 splits exactly, and that the script's left
  sides are genuinely byte-derived where the entry says so (`record region_count` derived = `len(members)`,
  `reported_size` derived = `compressed_size`), so the "constant rows are recorded, not re-derived" disclosure
  (Q11) is accurate rather than decorative.
- Coverage-map row named: `coverage-map: C07` (line 5), matching `corpus/README.md:36`. README C07 is still
  `frontier`, so the admission-order rule (flip only after all-criteria pass) is being respected.

### Findings (LOW only; no criterion failure)

- **LOW-1 — anchor range overshoots by two lines.** Entry line 197 and the Q02 row cite "S036 lines 91-96"
  for two sentences that sit entirely in 91-94; line 95 is a blank line and 96 opens a different bullet
  ("- Extraction returns regular file paths…"). The quoted content is inside the stated range, so the anchor
  still locates it; narrowing to `91-94` would make it exact.
- **LOW-2 — `l0-questions.md:42` is the question that references ADJ-06, not ADJ-06 itself.** Entry line 205
  reads "ADJ-06 (fleet `.ufo/l0-questions.md:42` remains open; …)". Line 42 is the open tsukuroi round-1
  question ending "…before an ADJ-06 analysis is routed"; the ADJ-06 row is
  `tsukuroi-shokunin/PROVINCE.md:51`, which the entry also cites, and the quoted phrase there is verbatim.
  Suggested wording if corrected: "the open question at `:42` references ADJ-06". Neither pointer supports a
  value in this entry, so Q01 is unaffected.

### Residual risk and gaps after re-review

- `admission-status: candidate` (entry line 6) is still the marker; the Q02 header obligation is met, but the
  C07 flip must land together with a `## Gate` decision that names this admission (prior MEDIUM-4), or the
  round reproduces the C06-style token/evidence mismatch (`corpus/README.md:35` says `held` while
  `round-63-zip-central-directory-evidence.md:8` still says `candidate`).
- Author-oracle identity is disclosed (U6) and not fixed by this review; my byte-level re-derivation removes
  transcription and readout risk only.
- Host-bounded generator replay is disclosed (limitation 6) and held on this host (Python 3.14.8 / zlib
  1.3.2, both digests reproduced twice).
- Not my criterion, not evaluated here: the core six-check invariant of `reports/round-64/measure.py` on a
  committed archive tree, the sources census after the append (37 rows), and Q03–Q13 decisions by other
  seats. This re-review scores Q01 and Q02 only.

### Re-review provenance

Read-only on the lane: no git/jj mutation (only `git show`, `git hash-object`, `git ls-remote`, all
read-only), no commit/push, no corpus or README edit; the only lane write is this appended section. Scratch
confined to `/tmp/revenger-r64-review-q01/` (`readout.py` extracted from the entry, fixture/oracle
regeneration copy, pinned guide snapshot). No tool installed or upgraded.
