# R63EntryC06 — C06 candidate entry draft (scribe seat)

Seat: `revenger-r63.R63EntryC06` (scribe, build wave, round 63).
Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Date: 2026-10-23.

## Result

The C06 candidate entry is drafted at **`/tmp/revenger-r63-entry/candidate.md`**,
intended for `corpus/knowledge/round-63-zip-central-directory-evidence.md` after
L1's build review. It was **not** written under `corpus/`.

| artifact | path | sha256 | bytes |
|---|---|---|---|
| candidate entry draft | `/tmp/revenger-r63-entry/candidate.md` | `630b974a51e0f6ab815a5806a0f415b3f07089df91923dde3a78b6fd49904c7e` | 74270 |
| readout script (embedded in the entry; same bytes) | `/tmp/revenger-r63-entry/readout.py` | `c6b54ccc2529dc7754eaf7ac7d71754d3d157805d050fe3fd5269c7452be829f` | 17595 |
| readout stdout (embedded in the entry) | `/tmp/revenger-r63-entry/readout.stdout.txt` | `e112d4092dfa8e3ed5398f07d1222457455ca06a94e01e988a0f58eab4c445ec` | 17 lines |

## Behavior

`.ufo/waves/round-63/build/zip-readout.out` **was absent** when this seat started,
so the values were derived from the fixture bytes directly, by a readout script
written for this entry. The peer pack `.ufo/waves/round-63/build/zip-readout.py` +
`zip-readout.out` (seat `R63ZipReadout`) landed later in the wave; its derived
values were compared against this seat's independent derivation and **agree on
every value** (archive size/digest, EOCD offset 2942, disk fields 0/0, counts
2/2, CD offset 2828, CD size 114, per-member name/local-header offset/compressed
size/uncompressed size/CRC-32, inflated SHA-256). This entry's own script is used
in the entry, not the peer's, so the entry's derivations are self-contained.

### The readout

One stdlib-only script (`struct`, `zlib`, `hashlib`, `json`, `binascii`) that
reads `corpus/fixtures/archive-r2/fixture.zip` as bytes, parses the
end-of-central-directory record and the central-directory file headers by
computed field offsets, follows each member's relative local-header offset, and
inflates the stored DEFLATE payload in memory. It extracts no file to disk,
executes no member, calls no producer, uses no network and reads no verifier
source. No third-party package was used and none was installed.

Each of the 17 emitted JSON objects carries a stable `fact` id, so **every value
in the entry names the one command that prints it**:

```
python3 -B readout.py <repo-root>                # all 17 facts
python3 -B readout.py <repo-root> --fact 'eocd'  # one fact
```

### Field offsets are derived, not assumed (Q11)

The script transcribes the field order and widths from S032's own §4.3.12 and
§4.3.16 field tables and **computes** the offsets by summing those widths:
central directory file header = 46 bytes fixed (`crc-32` @16, `compressed size`
@20, `uncompressed size` @24, `file name length` @28, `relative offset of local
header` @42); EOCD = 22 bytes fixed (both total-entries counts @8 and @10,
`size of the central directory` @12, `offset of start of central directory`
@16). The script then reads the fields at those computed offsets and checks
the resulting bytes against the values it parsed — the two readings agree for
every member, and the computed 22-byte EOCD length equals the observed 22 bytes
from the record's start to the end of file.

### Entry structure

`source:` (S032 spec row with URL + §-anchors + snapshot digest; S034 own-work
row with the three file paths and their digests) · `verified-at: 2026-10-23`
with the base commit · `recheck:` (the exact readout command, its exit, stdout
digest and line count, plus the per-value form) · `coverage-map: C06` with the
row's surface named and the two sibling archive fixtures named as **not**
covered · `admission-status: candidate`.

Body: **Observation** (items 1–17, each with its command and its printed
output) → **Inference** (18–21, each `[INFERENCE, scoped …]` with a basis) →
**Unknown** (22–26) → **Limitations** (27–35) → **Reproduce** (exact stdout +
script) → **Sources** → **Sentence-to-output inventory (Q11)** → **Q13** →
**QUALITY check**.

Named limitations: central-directory-only view of one archive (27); **no
trailing-bytes claim** — the byte accounting is explicitly scoped to this
fixture's 2964 bytes and no statement is made about trailing bytes, signing
blocks, comments or prepended data in archives generally (28); single fixture
(29); recorded-not-authenticated (30); manual analysis, no tool credited (31);
no execution / network / producer call (32); specification scope, incl. no
ZIP64 claim (33); no guard credit (34); C06's other two archive fixtures not
examined (35).

No universal clause and no provider-accuracy claim: the only "any/every/never"
words in the entry are inside negations or scope statements (e.g. "it is not a
claim that any ZIP implementation would read this file the same way", "no origin,
completeness or authenticity claim is made").

## Evidence exercised

**Byte-derived values (readout stdout, reproduced verbatim in the entry)**

| value | derived |
|---|---|
| archive | 2964 bytes, sha256 `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e` |
| EOCD | offset 2942 (22 bytes from end), sig `504b0506`, disk 0, cd-disk 0, entries-on-disk 2, total entries 2, cd size 114, cd offset 2828, comment length 0 |
| central directory | 2828–2942, `cd_offset+cd_size == eocd_offset`, 2 records parsed, both EOCD counts == 2 |
| byte accounting | segments `[0,2710,118,114,0,22,0]` sum to 2964 |
| `bin/checksum` | name len 12, lh offset 0, compressed 2668, uncompressed 16160, crc32 `b3df9ea7`, payload @42, inflated 16160 B, sha256 `f5ba0697…`, inflated crc32 == cd crc32 |
| `README.txt` | name len 10, lh offset 2710, compressed 78, uncompressed 84, crc32 `72a557b1`, payload @2750, inflated 84 B, sha256 `7d8f6a8d…`, inflated crc32 == cd crc32 |
| field offsets | 46 B / 22 B fixed parts; cd crc-32 @16, comp @20, uncomp @24, namelen @28, lh-offset @42; eocd 8/10/12/16; sigs `0x02014b50` and `0x06054b50` at computed offset 0 |

**Oracle comparison (`truth.json`)** — archive digest and size equal; both
members' size, compressed_size and sha256 equal (sha256 recomputed over the
inflated payload); member name sets equal (no member in one and not the other).
The oracle records no CRC-32, EOCD location, CD offset/size or local-header
offsets, so no oracle comparison is made for those — the entry says so.

**Saved-record correspondence (observation layer only)** — record 7692 B, sha256
`2fec924b…`, Evidence `ev_5cc39f35…`, operation `inspect_artifact`, provider
`rea-artifact-graph` v1, subject digest equal to the archive digest, 3
occurrences, nested inventory Evidence `ev_cc681c2a…`. Per member:
`logical_path` == derived name, `declared_size` == derived uncompressed size,
`compressed_size` == derived compressed size, node `sha256` == recomputed
inflated digest, node `size` == derived uncompressed size — all true for both
members. `executable` / `encrypted` / `hash_status` are labelled **recorded**
with no derived counterpart and are listed as unknown.

**Fixture premise** — the three files are byte-identical at base commit
`55bcb6e1aeb4d42923a4e98db6580f67142b41ac` and in the working tree (shown by
`git show <base>:<path> | sha256sum` in item 2). No `corpus/live` or
`corpus/fixtures` byte was modified; nothing under `corpus/` was written.

**Determinism / portability** — the readout was run three times on the lane
checkout and once on a clean `git archive 55bcb6e… corpus` extraction: identical
stdout sha256 `e112d409…` in every case (the stdout carries only repo-relative
paths, never the extraction root). The script embedded in the entry was
extracted back out of the draft and re-run: it exits 0 and reproduces
`e112d409…` exactly, and its bytes equal `readout.py`
(`c6b54ccc…`) — verified, not assumed.

**Entry self-verification** — a script re-checked the draft: all 17 embedded
`--fact` blocks are byte-identical to a fresh run (0 mismatches); the embedded
full stdout block matches a fresh full run; the stated script sha256/line count
match the file; and 39 prose assertions (every number, offset, size, CRC, digest
and boolean in the prose) were checked against the derived facts — 0 failures.

**Source quotes** — the six S032 quotes used in §Sources were verified as
verbatim substrings of the snapshot (whitespace-normalized) with word counts
7 / 21 / 8 / 23 / 24 / 20, each ≤ 25 words; the counts are printed in §Reproduce
via `printf … | wc -w`. Snapshot sha256 `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`
(174585 bytes, the served bytes), from seat `R63SourceAppnote`.

## Q01–Q13 self-check table (author's reading; not admission authority)

The table is also carried inside the entry (§QUALITY check). Independent
decisions are the falsify wave's, not this seat's.

| Q | decision | basis |
|---|---|---|
| Q01 | author-proposed pass; final decisions in the round-63 lesson | S032 is a `spec` row opened this round, tier A for the scope used (the two fixed records' field layout), quoted with section anchors and its snapshot digest; S034 is the own-work row for the archive bytes, oracle and saved record, with digests and base commit. No claim rests on a row outside those two. |
| Q02 | pass | header carries `source:` (two rows — S032 with URL/§-anchors/snapshot digest, S034 with paths and digests), `verified-at:` 2026-10-23 + base commit, `recheck:` (one runnable command with stdout digest and line count, plus the per-value form), `coverage-map: C06`; anchors are section numbers, not a bare homepage. |
| Q03 | pass | expected values come from the archive's bytes and the spec's field tables; the oracle and the record supply the compared side only and never feed a derived value (digests are recomputed in items 9–10 before the comparisons in 11–12). |
| Q04 | pass | analysis labelled manual; no tool credited with a result it did not output; the `rea-agents@6.4.0` run that produced the saved record is credited with the record's existence and literal fields only. |
| Q05 | n/a | no readiness, capability or host-state claim; the saved record is read as a saved file, in the past tense. |
| Q06 | pass | the fixture premise is byte-verified here (archive length/digest from bytes vs oracle; base-commit vs working-tree digests). |
| Q07 | n/a | no predicted parser behaviour; the offsets are arithmetic on the spec's own field lists, not a prediction about an implementation. |
| Q08 | superseded by Q11 | — |
| Q09 | pass | each digest binds exactly the bytes it hashed; no origin/completeness/authenticity claim; saved-record bytes unchanged at base commit. |
| Q10 | pass | scope is one archive, one oracle, one saved record, one provider id/version, one operation; sibling-lane overlap left with the operator; no ownership declared, no other lane's file cited as support. |
| Q11 | pass | the sentence-to-output inventory maps every factual sentence — including header, source and run-metadata rows — to a command and a printed field; each observation item shows its command and its output. |
| Q12 | n/a | no rejected source row is cited; the Python `zipfile` documentation was screened and excluded without a row, so no reject reason is owed. |
| Q13 | n/a by construction — no guard credit | no verifier, recheck command, comparison tool or automatic checker is credited or introduced; no value is presented as covered by any check. |

## Registry rows for L1 (not written by this seat)

- **S032** (spec, tier A) — drafted by seat `R63SourceAppnote`; row text and Gate
  quotes in `.ufo/waves/round-63/build/R63SourceAppnote.md`. This entry cites it
  for the two fixed records' field layout only.
- **S034** (own-work, tier A) — the own-work bundle row for this entry's inputs,
  proposed row text carried inline in the entry's §Sources. Validated for
  contract-v1 shape: 11 data cells, `NF=13` under `awk -F'|'`, no `|` inside any
  cell, kind `own-work`, tier `A`, status `queued`, `used-by` `—` (flip to
  `mined` with `corpus/knowledge/round-63-zip-central-directory-evidence.md`
  when the entry lands, logged old→new in the round lesson). The id was
  confirmed by seat `R63SourcesRows` as collision-free: claims.md reserves S032
  and "S033 if used" (Python zipfile docs), so S033 stays free for that
  possible outcome and S034 carries the own-work row either way.
- The Python `zipfile` documentation is **not** cited: the readout is raw
  `struct` reads plus `zlib` inflate and credits no `zipfile` behavior.

## Out of scope / not done (deliberate)

- `corpus/knowledge/round-63-zip-central-directory-evidence.md` was **not**
  created — L1 integrates the draft after build review.
- `corpus/SOURCES.md`, `corpus/README.md`, `corpus/QUALITY.md` were **not**
  edited. The README C06 flip (`partial → held`) is L1's and happens only after
  fresh falsify-wave Q01–Q13 pass decisions land.
- No `corpus/live` or `corpus/fixtures` byte was read-modified; no fixture,
  oracle, record or ledger byte was changed. The preservation manifest
  (seat `R63Preservation`) covers that independently.
- No target execution: the archive was read as bytes and member payloads were
  inflated in memory; nothing was extracted to disk or run.
- No model arguments were set; `~/.omp/agent/config.yml` was not touched; the
  host routing table was not edited.
- No git or jj mutation, no commit, no push, no publish, no deploy.

## Tooling

No tool was installed or upgraded. No `pacman`, `uv`, `npm` or binary install was
performed or needed; the operator's tooling directive was not triggered by this
seat's work. The only network access in this wave was seat `R63SourceAppnote`'s
two `curl` GETs of the APPNOTE URL (recorded in its report); this seat made no
network request.

## Artifacts

| path | what |
|---|---|
| `/tmp/revenger-r63-entry/candidate.md` | the C06 candidate entry draft (sha256 `630b974a51e0f6ab815a5806a0f415b3f07089df91923dde3a78b6fd49904c7e`) |
| `/tmp/revenger-r63-entry/readout.py` | the readout script, embedded verbatim in the entry (sha256 `c6b54ccc2529dc7754eaf7ac7d71754d3d157805d050fe3fd5269c7452be829f`) |
| `/tmp/revenger-r63-entry/readout.stdout.txt` | its exact stdout, embedded verbatim in the entry (sha256 `e112d4092dfa8e3ed5398f07d1222457455ca06a94e01e988a0f58eab4c445ec`) |
| `/tmp/revenger-r63-entry/template.md` | the entry template the draft was generated from (placeholders substituted with the exact command outputs) |
| `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/build/R63EntryC06.md` | this report |
