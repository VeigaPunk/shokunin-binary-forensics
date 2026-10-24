---
round: 63
date: 2026-10-23
author: revenger-r63
claims: [C1, C2, C3]
lane: revenger-shokunin
claim_base: 55bcb6e1aeb4d42923a4e98db6580f67142b41ac
contract: reports/round-63/claims.md (frozen at lane commit 54ab973c021cc62ca65dcbe2cbfabe3235d5ee38)
counter: reports/round-63/measure.py (frozen; sha256 3b7fba2d5243bbe0b723a99a53085130ff97010e23c8a59a8027f5f8992c5908)
status: draft for L1 — build-wave evidence only; no admission is claimed by this file
---

# Round 63 — a fixture premise is a claim about the tool, not about the bytes (2026-10-23)

Three claims on distinct frozen criteria: **C1** coverage K (one independently
gated new entry on C06 archives, K 6/14 → ≥7/14, 6/14 falsifies), **C2**
coverage F (first saved `firmware`-family record from an authored inert
known-truth fixture, F 4/8 → 5/8, 4/8 falsifies), **C3** calibration
(attributed forged-receipt kill on the two remaining verifiers,
`C3_RECEIPT_KILLED_ATTRIBUTED` 0/2 → 2/2).

Red-before receipt, committed at the claim base: `reports/round-63/measure-before.log`
— `K_HELD=6/14 score=4.3`, `K_ROW C06 status=partial`, `K_HELD_BACKED=6/14`,
`F_COVERAGE=4/8 score=5.0`, `C3_CONTROLS_PASS=2/2`,
`C3_RECEIPT_KILLED_ATTRIBUTED=0/2`, `HOLD_CALIBRATION=4/4`,
`HOLD_REPLAY=10/10`, `HOLDS_OK=yes`, `PROBE_EXIT=0`. That log is the
do-nothing control: it contains no claimed work and therefore meets no target.

## Gate

### Sources opened in this round

Access date **2026-10-23** for every row below. Each located quote is at most
25 words and is verbatim against the pinned snapshot; whitespace in the
snapshot is normalized, no word is invented.

**S032** — PKWARE APPNOTE.TXT, `.ZIP` File Format Specification —
<https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT> — kind `spec`,
tier **A** for the scope "central directory file header and end-of-central-directory
record field layout of one authored, non-ZIP64 ZIP archive" — opened
**2026-10-23**, HTTP **200**, `text/plain`, 174585 bytes, spec version
**6.3.10** (Status `FINAL - replaces version 6.3.9`, Revised `Nov 01, 2022`).
Byte-exact snapshot `.ufo/waves/round-63/source-snapshots/appnote.txt`, sha256
`0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`; machine
sidecar `.ufo/waves/round-63/source-snapshots/appnote.provenance.json`. Opener
`R63SourceAppnote`; the row text it drafted is carried in
`.ufo/waves/round-63/build/R63SourceAppnote.md` §"Draft SOURCES.md row (S032)".
Located quotes (whitespace inside the snapshot's fixed-width field table is
normalized to single spaces; no word is changed or invented; every quote below
is a verbatim substring of the whitespace-normalized snapshot text):

- §4.3.12 (snapshot line 522): "central file header signature 4 bytes (0x02014b50)"
- §4.3.12 (lines 529–533): "crc-32 4 bytes compressed size 4 bytes uncompressed size 4 bytes file name length 2 bytes extra field length 2 bytes"
- §4.3.12 (line 538): "relative offset of local header 4 bytes"
- §4.3.16 (line 634): "end of central dir signature 4 bytes (0x06054b50)"
- §4.3.16 (lines 638–641): "total number of entries in the central directory on this disk 2 bytes total number of entries in the central directory 2 bytes"
- §4.4.16 (lines 983–985): "This is the offset from the start of the first disk on which this file appears, to where the local header SHOULD be found."
- §4.4.7 (lines 911–912): "If bit 3 of the general purpose flag is set, this field is set to zero in the local header and the correct"
- §4.4.7 (lines 913–914): "value is put in the data descriptor and in the central directory."
- §4.3.3 (lines 350–351): "All values MUST be stored in little-endian byte order unless otherwise specified in this document for a specific data element."

Divergence recorded, not smoothed: the fallback URL
`https://pkware.com/documents/casestudies/APPNOTE.TXT` returns HTTP 200 but
redirects to a **different revision** — `APPNOTE-6.3.9.TXT`, version 6.3.9
(revised Jul 15 2020), 173575 bytes, sha256
`c7cf1fecfbde36ebbfbac643e6183d5c76fac983c2066fb8e32c6e4058a87e80`. Every
section quoted above was compared line-for-line between the two revisions and
is byte-identical, so the quotes are stable across the redirect; the row pins
the primary URL and the 6.3.10 revision that was actually opened.

**Python `zipfile` documentation** (the source the contract calls "S033 if
used") — <https://docs.python.org/3/library/zipfile.html> — opened
**2026-10-23**, HTTP 200, no redirect, 139782 bytes; snapshot
`.ufo/waves/round-63/source-snapshots/zipfile.html`, sha256
`9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739`; page
`zipfile — Work with ZIP archives — Python 3.15.1 documentation`, footer
"Last updated on Oct 24, 2026 (00:13 UTC)."
**Screened and excluded: no registry row, and no S033 id is spent.** The C06
readout is a manual byte walk, not a `zipfile` behavior claim: neither readout
script imports `zipfile` (`grep -c 'import zipfile'` = 0 in
`.ufo/waves/round-63/build/zip-readout.py` and in the candidate
`/tmp/revenger-r63-entry/readout.py`; both use `struct`/`zlib`
directly), and every format claim the entry makes rests on S032. The page
defers to that same specification, so citing it would add no authority.
Located quote (19 words, module introduction): "Any advanced use of this module
will require an understanding of the format, as defined in PKZIP Application
Note." Deciding seat `R63SourceZipfileDocs` (`.ufo/waves/round-63/build/R63SourceZipfileDocs.md`
§6–§7) proposed this exclusion line, recorded verbatim:

> Excluded without a row: docs.python.org/3/library/zipfile.html (opened
> 2026-10-23, snapshot sha256 9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739) —
> the C06 readout is raw struct reads and every format claim rests on PKWARE
> APPNOTE 6.3.10 (S032), which the zipfile page itself names as the format
> authority; no entry sentence credits zipfile behavior.

Caveat recorded, with its resolution stated positively: `corpus/fixtures/archive-r2/truth.json`'s
`build` field names `zipfile.ZipFile(mode=w, compression=ZIP_DEFLATED,
compresslevel=9)` as the recipe that produced the fixture. **The candidate
prints that string as a recorded field** — the derived fact `truth_build_field`,
whose recorded note reads "recorded provenance string read from the oracle file;
this entry makes no claim about the behaviour of any library it names and does
not rely on it for any value" — and asserts no `zipfile` behavior, relying on
the string for no value. So no `zipfile` behavior enters the entry and **no docs
row is needed**; quoting the field as a recorded label is exactly the branch
that keeps the exclusion, whereas asserting module behavior would have required
the S033 docs row the deciding seat holds in reserve (§7, re-labelled and
not-needed). Revision trail, CORRECTED against preserved evidence (the first landing of this sentence misattributed rev2's content to rev1; `R63SourceZipfileDocs` §9c supplied six re-checkable points): the build string entered the candidate at revision `dcfe131c…`, printed as a recorded field carrying the note "recorded provenance string read from the oracle file; this entry makes no claim about the behaviour of any library it names and does not rely on it for any value". The earlier revision `630b974a…` (embedded stdout preserved, digest `e112d409…`) carried NO build-field line — that stdout has `compresslevel` count 0 and the recorded string necessarily contains `compresslevel`. The exclusion stands on every reading; no `zipfile` docs row is needed; `R63SourceZipfileDocs`'s rev1 observation stands as recorded.
**Registry ids are therefore S032 + S033 (own-work), with no id skipped** — see
the id paragraph below.

**S034** — scoped re-open of the same APPNOTE document beside S032, for the
local-header layout scope the falsify wave showed the entry needs (Q01 attack
`W2AttackEntryQ01`) —
<https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT> — kind `spec`,
tier **A** for the scope "local file header record field layout of one authored
ZIP archive". Opened 2026-10-23 (first fetch by `R63SourceAppnote`; scope
pinned this wave); the committed snapshot is byte-identical (sha256
`0b993022…`, `cmp` exit 0, `W2ReopenS032` re-fetch 2026-10-24). Located quote
(7 words, snapshot line 389, §4.3.7): "local file header signature 4 bytes
(0x04034b50)". Landed `mined` with used-by the C06 entry in the same revision
as the entry's corrected citations.

**S035** — saved round-2 archive ledger — `corpus/live/runs/20261012T164246Z/LEDGER.md`
(sha256 `05042a555f91511c9c191565d92f83527f54d1c9b14de331587f4cbffff9e6cb`,
3959 bytes) — kind `own-work`, tier **A** for the scope "the recorded
observation/inference/unknown layer of the saved archive inventory record,
cited for provenance only". Opened 2026-10-23; the entry cites it as the
recorded layer for the `rea-agents@6.4.0` attribution with no value derived
from it (Q01 attack item, medium). Located quote for this row (rule 1; from `corpus/live/runs/20261012T164246Z/LEDGER.md` line 1, 8 words): "Round 2 archive inventory — 20261012T164246Z". Landed `mined`, used-by the C06 entry.

**S033 (own-work) — the C06 entry's second source; id decision closed by L1.**
The C06 candidate names two rows: **S032** (the specification above) and
**S033**, the authored bytes and the saved record —
`corpus/fixtures/archive-r2/fixture.zip` (sha256
`857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e`, 2964 bytes),
`corpus/fixtures/archive-r2/truth.json` (sha256
`7df773bf46b7c1273f8c3402b7825e7dacbb7f990c7d7ef41f30917c94726e68`) and
`corpus/live/runs/20261012T164246Z/artifact-inspection.json` (sha256
`2fec924b5217885674149b6a516970f419a8e731c8e6e49eab178a4f065f3380`), all
byte-identical at the claim base `55bcb6e`. The row text is proposed by the
candidate seat in its §Sources and lands with the entry. Located quote for this row (rule 1; from the saved record's own ledger, `corpus/live/runs/20261012T164246Z/LEDGER.md` line 3, 19 words): "`npx -y rea-agents@6.4.0 inspect-artifact … fixture.zip --format json` returned exit 0".

**Id allocation — decided, not left open.** Contract v1's rule is "`S` + 3 or
more digits, the next unused; never reused"; with the `zipfile` documentation
screened out and no row written for it, **S033 is the next unused id**, so L1
closed the question in favour of option (a): the own-work row lands as
**S033**, the earlier S034 reservation is withdrawn, and the candidate is
renumbered to **S032 ×10 / S033 ×5 / S034 ×0** (verified on the current
candidate revision, sha256 `dcfe131cbf833c90ba956a54eeadbd46314f829e88f5528b52d7baad6c8ff193`).
The round's ids are therefore the contiguous pair **S032 + S033 with no id
skipped**; the zipfile documentation stays in the search log as
screened-and-excluded with no row. UPDATE (falsify wave, same round): two
further rows landed after this paragraph was drafted — **S034** (scoped re-open
of the same APPNOTE document beside S032, for the local-header layout the Q01
attack showed the entry needs) and **S035** (own-work ledger row); the registry
ids are now the contiguous block S032–S035, and this paragraph is retained
un-rewritten as the draft-time record with this marker appended. Decision trail: `R63SourceZipfileDocs`
§9a (the gap finding and its resolution).

**Registry state at draft time (verified, not assumed):** `corpus/SOURCES.md`
still ends at **S031**; `grep -n 'S032\|S033\|S034' corpus/SOURCES.md` returns
nothing. The rows above are therefore *drafted for L1*, not yet appended, and
C1's admission order forbids landing the C06 entry before the S032 row lands.
No existing row is edited by this round. Status/old→new, logged here per
contract rule 2: S032 and S033 were drafted `queued` / used-by `—` by the
build wave and landed `mined` /
used-by `corpus/knowledge/round-63-zip-central-directory-evidence.md,
corpus/lessons/round-63.md` in the SAME commit as the C06 entry (the E11
ordering: the flip happens in the same append as the entry lands, so the
mined used-by path exists at validation). A new row arrives as `queued` and
becomes `mined` only when the C06 entry names it, that in-place change
(`status`, `used-by`) being logged old→new in this lesson.

### Candidate status at draft time

| candidate | build-stage status | evidence | necessary next decision |
|---|---|---|---|
| C06 `knowledge/round-63-zip-central-directory-evidence.md` | **candidate drafted in seat scratch — not landed, not admitted** | full candidate at `/tmp/revenger-r63-entry/candidate.md` (current revision sha256 `dcfe131cbf833c90ba956a54eeadbd46314f829e88f5528b52d7baad6c8ff193`, renumbered to S032 + S033) carrying its own Q01–Q13 self-check; readout `readout.py` + `facts.json` produce every field value. Independent premise: `.ufo/waves/round-63/build/zip-readout.py` (sha256 `c4b9b9f7a9331c5273a2f7c61727598385885f4d51afda9b4d1f24e764886f22`) + `zip-readout.out` (sha256 `67e5ce626bdcd9caa02228000cc7ec3e51ddeacaa1a4ed926c53525028649203`) derive EOCD@2942 (2 entries on disk, 2 total), CD@2828 size 114, archive sha256 `857989f5…`, and both members' sizes/CRC-32/SHA-256, all matching `corpus/fixtures/archive-r2/truth.json` | the file must land in `corpus/knowledge/` with the S032 (+S033) rows; then a **fresh-seat** Q01–Q13 pass decision from a reviewer who is neither author nor corrector; only then may L1 flip README C06 `partial → held` |
| C2 firmware saved record `corpus/live/runs/round-63/` | **build evidence green; admission still L1's** | real `npx -y rea-agents@6.5.0 inspect-firmware-regions … --format json`, exit 0, Evidence ID `ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259`, fixture sha256 `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be`, stdout sha256 `f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9`, receipt `corpus/live/runs/round-63/receipt.json`; byte oracle `ORACLE OK` (zlib @512/79 and @1024/90, decompressed sha256 `a5718481…` / `2d0d86aa…`); independent review `R63ReviewFirmware` recomputed every digest and re-derived both members | L1's frozen counter on the committed archive must print `F_COVERAGE=5/8` with `F_FAMILIES` gaining `firmware`; the receipt, not the counter, is the evidence |
| C3 attributed receipt kills | **build evidence green; admission still L1's** | `receipt_ok(...)` refactor + one in-script forged-receipt control per script (`R63C3NamedPatch`, `R63C3IconPatch`); frozen mutants killed and attributed — named: `AssertionError: r55: forged receipt accepted`; icon_states: `AssertionError: r36: forged receipt accepted` (`R63MutC3`, mutant bytes byte-identical to the frozen counter's own `mutate_c3()` output); independent patch review `R63ReviewC3` returns **HOLDS** on both scripts, conjunct-by-conjunct, with the frozen clause matching exactly once in each final file | L1's frozen counter must print `C3_RECEIPT_KILLED_ATTRIBUTED=2/2` with `C3_CONTROLS_PASS=2/2` |

### Admission order (unchanged from the frozen contract)

1. Land the candidates **without** the README flip — S032 row, the C06 entry,
   the firmware fixture/record/receipt/oracle, the two verifier patches.
2. Fresh falsify wave: named fresh-seat Q01–Q13 pass decisions for the C06
   entry, from reviewers other than its author or corrector.
3. Adjudicate. Only on an all-criteria pass does L1 flip README C06
   `partial → held`; the flip must end the row with `| held |` and name
   `knowledge/round-63-zip-central-directory-evidence.md` in the
   knowledge-entries cell, in the same commit as the entry file, or the
   counter's `K_HELD_BACKED` check cannot back the row
   (`R63ReviewSeparability` §Findings 2).
4. Measure on a committed archive: `python3 -B reports/round-63/measure.py TREE`
   over `git archive <commit> corpus`, cwd `/`, `TMPDIR` under lane scratch.
   The on-tip run is committed as `reports/round-63/measure-after.log` — see
   §Routed debt.

Nothing in this section admits anything. A printed counter value is not an
admission: `R63CriticClaims` showed that a status-only C06 flip, one
hand-written firmware JSON, and two source-text canaries can print
`K_HELD=7/14`, `F_COVERAGE=5/8` and `C3_RECEIPT_KILLED_ATTRIBUTED=2/2` without
any of the claimed work. The frozen claim text — a newly admitted entry, a
real producer run with a receipt and byte-oracle agreement, and the exact
`receipt_ok` fix shape — is the gate, and the counter is only its presence half.

### Quality criteria

Q01–Q13 are unchanged; `corpus/QUALITY.md` is byte-identical to the claim base
(`git diff 55bcb6e -- corpus/QUALITY.md` returns nothing, `R63CriticHarms`
guard 3). No Q14 row is adopted, no criterion is weakened, and the ten-verifier
census stays 10.

## Mistakes

| id | class | evidence | captured-by | fix / falsifiable demonstration |
|---|---|---|---|---|
| M33 | stale-premise: a fixture's detectability was assumed from the format's name instead of probed against the tool's actual signature list, so the fixture premise and the producer call were mismatched before any bytes were produced | L1 pre-probe 2026-10-23 — binwalk 3.1.0 signature scan finds **zero regions** in a 1056-byte uImage-header image while finding an **offset-512 zlib region**; red-before for the whole C2 fixture premise (`reports/round-63/claims.md` §C2). Independent reproduction by `R63ScoutFirmware` §2a–2c pins the mechanism: the zero-finding image is the magic-only 1056-byte one (sha256 `b4e9f53c…`), and the positive control (zlib at offset 512, reported size 55, name `zlib`) needs binwalk's `--search-all`, because upstream `src/magic.rs` marks the zlib signature `short: true` — the default scan (187 magic patterns) reports nothing at a nonzero offset, `--search-all` (196 patterns) reports it. Upstream `src/structures/uimage.rs` requires a known OS/CPU/type/compression **and** a valid header CRC32, and `src/extractors/uimage.rs` additionally requires the data CRC32 to match — so "uImage" is in the signature list but a header-shaped image is not a uImage region. Reproduced again here: magic-only 1056-byte uImage → zero findings under both the default and `--search-all` scans; a CRC-valid, known-enum variant of the same length → one `uimage` hit at offset 0, size 1056 | **Q05** (a readiness/capability claim needs a probe against the real surface — the producer's own command, date and observed output, never a configured value or an unrechecked older probe) and **Q06** (fixture premises are byte-verified against the built fixture before any producer call) — Q05 and Q06 caught it only after the premise was written down and re-probed, not before | the fixture generator is restricted to **binwalk-3.1-detectable** members — here two RFC 1950 zlib streams with headers `78 da`, at offsets 512 and 1024 of a 2048-byte inert image (`corpus/fixtures/firmware-r63/generator.py`, `truth.json` records the recipe and the compressed member digests) — and the byte oracle is able to **fail**: `corpus/live/runs/round-63/oracle_check.py` returns 0/`ORACLE OK` on the saved record and returns 1 with `MISMATCH normalized_result.regions[0].offset: expected 512, got 513` when the first reported offset is shifted by one, and 1 with `MISMATCH normalized_result.regions: expected 2 reportable regions, got 1` when the last region is dropped. The same generator+oracle pair also rejects a second physical image: swapping the first 512 padding bytes for `ff` while keeping both compressed members and every offset yields `MISMATCH subject.digest.sha256` (`R63CriticFixture` §1), which is why the oracle binds the actual image digest to the record's `subject.digest.sha256` and length to `normalized_result.input_size` |
| M34 | counter-substitution: the frozen counter's printed numbers were treated as the gate, although a counter-only tree can print all three targets without any of the claimed work | `R63CriticClaims` §1: (a) README C06 already names the existing `knowledge/2026-10-12-rea-readiness-checklist.md`, so flipping only the status cell satisfies `K_HELD_BACKED` with no new entry; (b) `{"evidence_id":"invented","operation":"inspect_firmware_regions","normalized_result":{}}` satisfies the F presence predicate and prints `F_COVERAGE=5/8` with no fixture, no producer call and no receipt; (c) a top-level `assert "receipt['command']==command" in Path(__file__).read_text(), 'forged receipt'` in each original verifier makes both frozen mutants die with an attributed message while testing source text instead of receipt data | Q11/Q13 in the entry sense, but the counter shape itself is governed by the frozen claim sentences — the claim text ("one newly admitted entry", "the output of one real `npx -y rea-agents@6.5.0 inspect-firmware-regions <path>` run", the exact `receipt_ok` fix shape) is the barrier the counter cannot replace | keep the two gates separate in the report: the printed counter value is reported next to the substantive evidence (entry + fresh Q01–Q13 decisions; receipt + fixture + byte oracle; frozen diff of the `receipt_ok` refactor), and L1 reviews the committed diff against the frozen fix sentences as well as reading the attributed tally. The frozen counter and the round-61 probe stay untouched  Falsifiable demonstration (executed this round): `W2AttackProbeK`'s six do-nothing-tree runs print `K_HELD_BACKED=7/14` with no new entry, `F_COVERAGE=5/8` from one fabricated JSON, and C3 targets from canary strings — the counter is presence-only and the claim text is the gate (`.ufo/waves/round-63/falsify/W2AttackProbeK.md`).|
| M35 | residual unguarded clause: a receipt conjunct with no in-script forged-receipt control survives clause deletion, so the two verifiers are not uniformly deletion-sensitive | `R63MutC3` §3, mutant M3 (outside the frozen C3 set, reported as coverage, not as a claim extension): deleting the `stdout_sha256` conjunct from `corpus/verify_icon_states.py` leaves the self-test **green** — exit 0, `PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED`. The frozen C3 sentence forges `command` (named) and `fixture_sha256` (icon_states) only, so the `stdout_sha256` conjunct is unguarded by the new controls. Correction (W2MutC3Final): the debt is one conjunct WIDER than first stated — the `stdout_sha256` conjunct in `verify_named_multi_icon_states.py` also survives deletion (exit 0, green PASS); a full census shows the in-script controls detect 2 of 10 deletable receipt conjuncts, exactly the two the frozen sentence names, so C3 is true as written but must not be read as 'the receipt checks are deletion-sensitive' | Q13 (a verifier may be credited only for the clauses whose deletion its own run is shown to detect) — it constrains *credit*, not the file; no criterion forbids an unguarded conjunct, so this is captured-but-not-enforced | keep the claim honest: C3 is credited for the two frozen conjuncts it shows to detect, and the `stdout_sha256` conjunct is named as unguarded rather than counted. Widening the control to that conjunct is a **debt item for a later round**, not a silent extension of this round's target; `R63SimplifierProbe` D1 records the related point that the frozen counter's `HOLDS_OK` is stricter than the round-61 definition it claims to inherit (it adds `killed_b == 2`, `c3_controls == 2`, `fresh == 18`), so a green hold already requires the C3 controls to pass |

## Search log

Unit for both queries below: **one proposed registry document set** (a
document plus its revision/anchors counts once; the lane's own authored
fixture/record sets count once each; failed URL attempts are excluded before
the count). The two counts are not comparable with the historical
external-document totals recorded in round 61/62 notes.

- **2026-10-23, archive specification (C1, ZIP central-directory field layout).**
  Query: the primary specification that fixes the central-directory file
  header and end-of-central-directory record layouts — signature values, field
  order, length fields, CRC-32 and the relative offset of the local header —
  for a byte-derived readout of one authored archive. Where: the PKWARE
  APPNOTE URL and its documented fallback; the Python `zipfile` documentation
  as the candidate implementation-behaviour source. Identified **3**,
  screened **3**, included **1** row (S032), excluded **2**.
  Excluded with reasons: (1) the fallback URL's target — it resolves to a
  **different revision** (6.3.9) of the same document, so it corroborates the
  quotes (byte-identical sections) but is not a second proposed row, and the
  row pins the 6.3.10 revision actually opened; (2) the Python `zipfile`
  documentation — the readout is raw `struct` reads and credits no `zipfile`
  behavior, so the page is screened-and-excluded with **no row** rather than a
  rejected row that would need a grounded reject reason.
  Stop: one tier-A specification covers every load-bearing
  field the entry states, and the fixture's own bytes plus `truth.json` cover
  the values. Openers: `R63SourceAppnote` (APPNOTE), `R63SourceZipfileDocs`
  (zipfile docs), `R63ScoutArchive` (fixture/record inventory), `R63ZipPremise`
  (fixture premise re-verification), `R63ZipReadout` (byte readout).
  **Reconciliation, append-only:** this note is the one L1 uses. UPDATE (falsify wave, same round): two further rows, S034 and S035, were appended after the Q01 attack showed the entry needs a local-header-layout scope and a ledger provenance row; the round's registry total is four rows (S032, S033, S034, S035) — logged here per the append-only rule rather than rewriting the counts above.
  `R63SourceZipfileDocs` §6 separately proposed a SOURCES.md-style block that
  counts the own-work row as an included row (2 included / 1 excluded) and omits
  the fallback-revision exclusion; it recommends L1 land this note and drop that
  block, because this note is later *and* reconciles the fallback revision, and
  the zipfile snapshot digest it adds is already carried above and in the Gate.
  **Divergence recorded verbatim, not smoothed:** `R63SourcesRows` judged the
  seat's §6 counts (3 identified / 3 screened / 2 included / 1 excluded, the
  own-work bundle counted as a document set) the correct ones and told L1 to
  paste that block verbatim, while this note counts 3 / 3 / 1 / 2 (the APPNOTE
  6.3.9 fallback revision as the second exclusion; the own-work bundle not
  counted as an "included" external document). Neither arithmetic is wrong — the
  conventions differ — and L1 resolved in favour of **this** note, dropping the
  §6 block and keeping only its snapshot digest for the Gate record. The seat
  records the disagreement and its resolution in its report §9b so the canonical
  judge sees a decision rather than a silently dropped block. Nothing on disk
  conflicts — neither seat edits `corpus/SOURCES.md`.
- **2026-10-23, firmware fixture premise and the tool's actual signature list
  (C2 and M33).** Query: what the firmware-inspection path actually detects,
  so that the authored fixture's members are detectable at all and the
  premise is probed rather than assumed. Where: the REA firmware-analysis
  guide (opened as a lead); the upstream Binwalk v3.1.0 source that defines the
  signature registry and the zlib/uimage signatures; the locally installed
  `binwalk 3.1.0` binary's own signature list and scan behaviour.
  Identified **3**, screened **3**, included **0** registry rows, excluded **3**
  with reasons: (1) the REA guide is a lead, not a row — its `main` revision is
  newer than the pinned `rea-agents@6.5.0` package whose schema this round's
  record is parsed against, so it cannot be the row a 6.5.0 record rests on;
  (2) the upstream Binwalk source was read to establish *which* signatures
  exist and *why* the default scan misses a nonzero-offset zlib — it is
  recorded here as the M33 mechanism, while this round's registry rows are
  frozen to S032 (+S033 if used) by the claim text, so it gets no row; (3) the
  local `binwalk 3.1.0` probe is own-work evidence — its outputs (85 file
  signatures; 187 magic patterns by default, 196 with `--search-all`; the
  `gzip`/`uimage`/`zlib` built-in list) are recorded as evidence and in the
  fixture's `truth.json` recipe, not as a registry row. Stop: the fixture's
  members are now chosen from the tool's actual detectable set and the
  producer run's own receipt carries the command, exit code, fixture digest,
  stdout digest and Evidence ID — the byte oracle, not a document, is what
  settles the agreement. Openers: `R63ScoutFirmware` (guide, signature list,
  M33 red-before), `R63FirmwareFixture`, `R63FirmwareRun`, `R63FirmwareOracle`,
  `R63ReviewFirmware`, `R63CriticFixture`.

## Routed debt

| routed item | source | round-63 disposition |
|---|---|---|
| **(a) on-tip re-verification output was not committed alongside the report claim in round 62** | `corpus/lessons/round-62-verifier-spotcheck.md:63` — "commit the resume re-verification output alongside the report claim when a resumed attempt re-runs the probe on the final tip (this round's on-tip re-run is closure-verified but was not itself committed)" | **Honored.** The binding measurement for round 63 is a frozen-counter run on the **final tip** — `python3 -B reports/round-63/measure.py TREE` over `git archive <final-commit> corpus`, cwd `/`, `TMPDIR` under lane-owned scratch — and its complete output is committed as `reports/round-63/measure-after.log` **in the same commit as the report claim**, not only as a mid-round revision. `measure-before.log` remains the red-before receipt at the claim base and is not replaced by it. Any probe re-run that is not on the final tip is labelled as such in the report and is not presented as the claim's measurement |
| counter-contract wording drift: `HOLDS_OK` in the frozen probe is not the round-61 definition it claims to inherit (it adds `killed_b == 2`, `c3_controls == 2`, `fresh == 18`) | `R63SimplifierProbe` D1 — direction strictly conservative, base outcome identical, so the red-before receipt is unaffected | Recorded, not fixed: both files are frozen. L1 adjudicates; the probe is **not** edited this round. The gate is unchanged — the final committed `measure-after.log` must show the C3 controls passing and the C3 attributed tally at 2/2 as separate printed lines, because `HOLDS_OK` alone does not prove C3 |
| residual unguarded receipt conjunct (`stdout_sha256` in `verify_icon_states.py`) survives deletion | `R63MutC3` M3 | Routed as M35 coverage debt. C3 is credited only for the two frozen conjuncts it is shown to detect; the `stdout_sha256` conjuncts in BOTH scripts are named as unguarded (W2MutC3Final corrected the count from one to two). Widening the control is a later-round item and no extension of this round's target is claimed |
| sibling scope on archives and firmware | `R63ConnectorOverlap` — `kaidoku-shokunin` holds Core archive/package inventory and already holds firmware-region inspection on vendor blobs; `tsukuroi-shokunin` ADJ-06 keeps "protocol integrator — kaidoku/revenger ownership unresolved" open | Reported, **not absorbed**. The C06 entry rests on this lane's authored `archive-r2/fixture.zip` only and must not restate the sibling limitation that ZIP inventory lists central-directory entries only; the C2 record rests on the new inert fixture only and must not cite sibling evidence ids or host firmware health. ADJ-06 stays open; no province sentence is edited |
| outside spot-check for round 63 | not yet performed — the round's gate seats are this lane | Deferred to independent closure, as in round 62. This lesson records no outside discernment verdict |

## Tooling

No tool was installed or upgraded in this seat. No `pacman` transaction (the
host's pacman gate is paused), no `uv tool install`, no global npm install, no
binary download. The lesson's M33 row was re-probed with the already-present
`binwalk 3.1.0` (`/usr/bin/binwalk`) and `python3 3.14.8`; the APPNOTE URLs
were fetched read-only with `curl` (primary, fallback, and re-fetch for digest
agreement). Scratch used by this seat: `/tmp/revenger-r63-lesson/` (removed
after this report lands).
