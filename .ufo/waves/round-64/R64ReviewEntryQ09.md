# R64ReviewEntryQ09 — Q09/Q10/quality-bar review of the C07 candidate

Seat: `revenger-r64.R64ReviewEntryQ09` (independent leaf; no git/jj mutations run).
Round: 64 (hyaku), attempt 1. Reviewed: the C07 candidate draft routed by
`/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/briefs/R64ReviewEntryQ09.md`
against `reports/round-64/claims.md` and `corpus/QUALITY.md`.

**Verdict: NOT ADMISSIBLE AS-IS.** The Q09 digest-scope content, Q10 scoping, and every
quality-bar element named in my brief pass. The entry's own **Q01–Q13 application still
fails**: five of its thirteen rows answer a different criterion than the one they name, no
`n/a` reason is given anywhere, and two Q11 gaps remain. L1 must not flip C07 to `held` on
this revision; a table-only correction plus one fresh re-review should clear it.

## Reviewed artifact and pins

The target lane path does **not** exist at review time
(`corpus/knowledge/round-64-firmware-region-byte-evidence.md` absent); the draft is the
routed artifact. The draft was revised twice during this review, so both snapshots are
pinned:

| Artifact | Size | SHA-256 |
|---|---|---|
| `/tmp/revenger-r64-entry/candidate.md`, latest reviewed revision (459 lines) | 48440 B | `0a3730a1a03b19ef134930a8eb180147be8b6e503fbd7040fdd7617eafed0a22` |
| `/tmp/revenger-r64-q09-review/candidate.latest.md` (pinned copy of the above) | — | same |
| earlier revision reviewed in this seat (455 lines), superseded | 47161 B | `e86a5b1c9f382c186818fe55c78eed1537aa907151853e81f6aef80d4ff86cc9` |
| `/tmp/revenger-r64-q09-review/candidate.pinned.md` (pinned copy of the above) | — | same |
| `/tmp/revenger-r64-entry/readout.py` (embedded verbatim in §Reproduce `### Code`) | 10018 B | `2abe0c130ae29de27ae194511e3b4e5061364818cf94d8d8671c3019eafabae1` |

Delta between the two revisions (`diff`): a new `## Cross-lane scope note (Q10)` section and
a corrected Q06 row; nothing in §Observation, §Correspondence or §Limitations changed. The
remaining defects below are present in the latest revision. The embedded code block is
byte-identical to `readout.py` (`diff` empty).

## Method — what I re-derived independently

Every printed observation was re-derived, not read:

- Fixture bytes (`python3 -B`, stdlib): 2048 B, sha256 `bdfe9f46…510be`; whole-file
  maximal zero runs `(0,512) (591,433) (1098,1) (1114,934)`; zlib streams at 512 and 1024
  consume exactly 79 and 90 bytes (`decompressobj` eof, no unused tail), inflate to 78 and
  97 bytes with sha256 `a5718481…df7b86` and `2d0d86aa…eeaba9`, both matching `truth.json`.
- **The `1098` trap is handled correctly.** The candidate excludes the one-byte zero run at
  offset 1098 (inside member B `[1024,1114)`) from padding and says why (lines 17, 140;
  limitation 158). A naive "all zero runs are padding" readout would have contradicted
  `truth.json` — this entry does not.
- Readout rerun from the lane root: exit 0, 7 JSON lines, stdout sha256
  `aa353251f7529a00c4336f9bf8cae6634838b8d10bd20e24b7340d94cf1314ae` — equals the
  candidate's `recheck:` pin and the `### Stdout` block pin.
- S036 snapshot: `.ufo/waves/round-64/source-snapshots/rea-firmware-guide.md` 10695 B
  sha256 `e422b4816b1dbc912680afefb8e23acfd8ead4aea08c3d722d4ccb5207933609`, matching the
  header and the provenance sidecar (HTTP 200, tag commit `3b79af28…`, blob
  `152819177f…`). Quoted anchor lines 3, 56, 83-85, 91-96 are verbatim in the snapshot,
  each quote ≤25 words.
- Six-file preservation at base `666ea84b…`: `git show <base>:<path> | sha256sum` equals
  the working tree for fixture `bdfe…`, generator `4e5d…`, truth `9663…`, inspection
  `f699…`, receipt `e930…`, ledger `25a4…`. `git status` shows only the two C2 verifier
  scripts modified; `corpus/live` and `corpus/fixtures` are byte-clean.
- Fixture premise: regenerating the committed generator in scratch
  (`/tmp/revenger-r64-entry/gen/`) reproduces fixture, generator and oracle byte-for-byte
  (all three digests identical). The premise is reproducible on this host.
- Record absences claimed by the entry are true: `normalized_result` keys are exactly
  `coverage/engine/input_size/regions`; `raw_result.report[0].Analysis.extractions` is
  `{}`; `grep -c unblob` on `inspection.json` = 0.
- Cross-lane scope note citations opened read-only and consistent: fleet
  `.ufo/l0-questions.md:42` is the ADJ-06 ownership/arbitration row;
  `tsukuroi-shokunin/PROVINCE.md:51` names "protocol integrator — kaidoku/revenger
  ownership unresolved" and lines 3-4/11-13 name the driver/firmware plane;
  `kaidoku-shokunin/PROVINCE.md:50,64-71,76-79,125` name its archive inventory,
  provider-pin registry, firmware surface and the ADJ-06 row. The note reports, does not
  absorb.

## Verdicts per deliverable criterion

| # | Criterion (brief) | Verdict | Evidence |
|---|---|---|---|
| 1 | Digest-scope disclaimers present — digests prove only the bytes hashed | **PASS** | lines 127, 159: "A SHA-256 match proves only that the bytes hashed are the bytes named"; "Matching digests prove only that the bytes hashed are the bytes named." |
| 2 | No origin / completeness / authenticity claim | **PASS** (one LOW wording fix) | line 127 disclaims authorship; line 159 authenticity; line 160 "makes no provider-completeness claim". Line 125's "they were produced independently — the record by Binwalk 3.1.0" states producer provenance as fact (finding F5). |
| 3 | Observation vs inference vs unknown separated | **PASS** | §Observation, inference and unknown lines 129–153: O1–O9, I1–I4, U1–U5; numbered Observation items separate from the tagged lists. |
| 4 | At least one limitation named | **PASS** | §Limitations lines 155–162: six named limitations (one fixture/no format claim; padding rule; digest≠authenticity; record is one signature scan; no extraction/execution; host-bounded replay). |
| 5 | Saved record used as observation layer only | **PASS** | lines 125–127 and 160: record's numbers compared against sizes measured from the compressed streams "rather than treating them as independent measurement"; private workspace copy `/tmp/rea-firmware-7rPoLl/firmware.bin` disclosed; ledger's Unblob probe explicitly not absorbed (line 125, U4). |
| 6 | Admission procedure Q01–Q13 applied, every `n/a` naming why | **FAIL** | §Q01–Q13 map (lines 168–184): rows Q04, Q05, Q07, Q10, Q12 answer a different criterion than the one named; Q08 omits "superseded by Q11"; no row names an `n/a` reason. See F1. |

## Reviewer's own Q01–Q13 application

| Q | My verdict | Basis |
|---|---|---|
| Q01 | **FAIL (blocked)** | S036 quote/tier/scope matches claims and the snapshot (verified). S037's frozen scope in claims is "authored fixture bytes + truth.json + saved record + LEDGER"; the entry adds `generator.py` and `receipt.json` (header line 2) and leans on the receipt in the Q10 row. Neither S036 nor S037 exists in `corpus/SOURCES.md` yet (`grep -c "S036\|S037"` = 0), so no registered row is tier A for the claim's scope at review time. |
| Q02 | **FAIL (blocked), header otherwise complete** | `source:`, `verified-at:`, `recheck:`, `coverage-map: C07`, `admission-status: candidate` present; S036 anchors and S037 digests verified. Blocked on the same absent registry rows. |
| Q03 | **PASS** | Values scanned from offset 0 with no oracle input (lines 15–17); oracle is a comparison target; independent blind derivation is the admission test and is another seat's deliverable. |
| Q04 | **PASS (content); entry row wrong** | Readout labeled manual/standard-library (line 10); Binwalk 3.1.0 named only as the record's recorded provider, credited only with its own explicit region output; no tool credited with a derived value. The entry's Q04 row (175) answers "falsifiability" instead. |
| Q05 | **n/a** | No readiness or capability claim; no probe owed. The entry's Q05 row (176) gives a scope answer instead of naming `n/a`. |
| Q06 | **PASS** | Premises re-derived from built bytes (items 1–5) and the generator replay (item 3) before any comparison; no producer call; no failed input. The latest revision corrected this row (the earlier snapshot answered "no verifier credited"). |
| Q07 | **n/a** | No predicted parser behaviour and no cause is asserted; the member scan is a procedure, not a prediction. The entry's Q07 row (178) says "never executed". |
| Q08 | **superseded by Q11** | Not marked as superseded. |
| Q09 | **PASS** | Findings 1–2 of my brief; lines 127, 159. |
| Q10 | **PASS** | One fixture/family/operation/version; no vendor image or general format claim (lines 10, 157); §Cross-lane scope note (164–166) reports-not-absorbs ADJ-06 and the kaidoku/tsukuroi surfaces, with citations I verified; the ledger's Unblob probe is reported-not-absorbed (line 125, U4). The entry's Q10 row (181) still answers provenance digests instead. |
| Q11 | **FAIL (narrow)** | See F2/F3/F4/F7: six of the "13 compared fields" are constant echoes, the record-absence sentences are unprinted, and the host Python/zlib versions are asserted with no command/output. |
| Q12 | **n/a** | No rejected source row is cited, so no reject reason/flip is owed. The entry's Q12 row (183) answers oracle agreement. |
| Q13 | **PASS** | No verifier/checker is credited as coverage; recheck is labeled a reproducibility aid (line 184). |

## Findings by severity

**F1 — HIGH — the Q01–Q13 map answers the wrong criteria (five rows), and no `n/a` reason is
named.** Latest revision, Q-map lines 168–184:
- Q04 ("tool claim names tool, version, function; manual analysis labeled") is answered with
  readout falsifiability/`aa353251…` (175).
- Q05 (readiness/capability probe) is answered with the scope paragraph (176).
- Q07 (predicted parser behaviour) is answered with "never executed/extracted" (178).
- Q10 (family/operation/version/input scope; contested scope reported) is answered with the
  record's provenance digests (181), despite a correct §Cross-lane scope note elsewhere.
- Q12 (rejected source row's reject reason/flip) is answered with oracle agreement counts
  (183).
- Q08 (179) omits "superseded by Q11"; no row in the map names `n/a`, although Q05, Q07 and
  Q12 cannot apply to this entry.

Consequence: a gate reader following this table would record passes for Q04, Q05, Q07, Q10
and Q12 without any answer to those criteria, and the entry violates `QUALITY.md`
"Admission procedure" step 1 ("Apply every criterion. A criterion marked `n/a` names why it
cannot apply."). The round-63 and round-62 entries use the correct convention (`Q05 n/a`,
`Q07 n/a`, `Q12 n/a`, `Q08 superseded by Q11`). Fix is table-only: Q04 pass (manual label +
Binwalk 3.1.0 credited only with its own output), Q05 `n/a` (no capability claim), Q06 pass
(now correct), Q07 `n/a` (no prediction), Q08 "superseded by Q11", Q09 pass, Q10 pass
(scope paragraph/limitations + §Cross-lane scope note), Q11 pass after F2/F3, Q12 `n/a` (no
rejected row), Q13 pass. No observation needs to change.

**F2 — MEDIUM — "All 13 compared fields match" overstates derivation; six are constant
echoes.** Line 107 plus `readout.py:177-215`: `operation` and `provider.version` are
hardcoded literals compared to the record; per member, `signature` is hardcoded `"zlib"` and
`size_basis` hardcoded `"provider_reported_validation_unknown"`. Only 7 of the 13 are
derived-vs-stated (subject digest, `input_size`, region count, presence ×2, `reported_size`
×2). Q11 requires a value cited only to the saved record to be labeled recorded, not
re-derived. The load-bearing agreement (offset 512/1024, size 79/90) is unaffected, but the
count/framing must be corrected — e.g. "7 derived comparisons plus 6 recorded-field echoes
(operation, provider version, signature, size_basis)", with the recorded ones labeled as
such (or derive `signature` from the detected member kind and drop
`operation`/`provider.version` from the comparison count).

**F3 — MEDIUM — record-absence sentences have no in-entry command/output.** Lines 125 ("It
contains no padding regions …, no member names, no decompressed sizes or digests, and
`extractions` is `{}`; … Unblob appears nowhere") and O8 line 139. I verified all of these
true directly (key set exactly `coverage/engine/input_size/regions`; raw `extractions` `{}`;
`grep -c unblob` = 0), but the readout's `fact_record` prints only `coverage`, `confidence`,
`authority`, `region_kinds` and the checks — not `extractions` and not any absence set.
Under Q11 these are prose-recorded values, not re-derived ones. Fix: add a
`record_absences` fact that prints `extractions: {}`, the normalized key set and an
`unblob_mentions: 0`, or label the sentence "recorded".

**F4 — MEDIUM — S037's frozen scope is narrower than the files the entry leans on.**
`reports/round-64/claims.md` S037: "own-work bundle: authored fixture bytes + `truth.json`
+ saved record + LEDGER". Header line 2 names six files, adding `generator.py` and
`receipt.json`; the Q10 row (181) cites the receipt's command and exit 0. Q01 requires a row
tier A for the claim's scope. Either L1's registry append must include `generator.py` and
`receipt.json` in S037's text, or item 3's generator replay and the receipt-based provenance
sentence exceed the frozen row. The command line is already in the LEDGER (which S037 does
name), so the receipt citation is avoidable; the generator replay needs an explicit S037
mention.

**F5 — LOW — Q09 wording tension at line 125.** "they were produced independently — the
record by Binwalk 3.1.0 `--search-all`, the readout by inflating the bytes" asserts producer
provenance as fact, while line 127 correctly says a digest match establishes "not who
authored them". The producer statement rests on the record's provider fields, the receipt
command and the ledger (recorded provenance), not on any hash. Reword to recorded
provenance ("the record's saved provenance names binwalk 3.1.0; the readout's values come
from in-memory zlib; this entry authenticates neither producer").

**F6 — LOW — oracle independence is not in `## Unknown`.** Item 3 and Scope line 10 disclose
that one generator wrote both fixture and oracle, the Q12 row notes the shared author, and
line 127 disclaims canonicity; but the U1–U5 list lacks the round-63 U5-style statement that
oracle agreement is internal consistency, not third-party validation. Add one
Unknown/limitation line.

**F7 — LOW — host version assertion lacks its command (Q11).** Line 55 claims the host's
Python/zlib versions equal the recipe's (`Python 3.14.8`, `zlib 1.3.2` compile and runtime),
and I4/limitation 162 rely on that equality, but item 3 shows no version command/output. Add
`python3 -c "import sys,zlib;print(sys.version.split()[0], zlib.ZLIB_VERSION, zlib.ZLIB_RUNTIME_VERSION)"`
with its printed line.

**Confirmed strengths (no action).** The 1098 one-byte zero run is explicitly excluded with
the correct reason; the private-workspace copy path is disclosed and distinguished from the
fixture link; the record's `size_basis` is used as a caution ("compares the record's numbers
to sizes measured directly … rather than treating them as independent measurement"); the
ledger's Unblob probe is reported-not-absorbed; the new §Cross-lane scope note reports ADJ-06
and the kaidoku/tsukuroi surfaces without absorbing them, and its citations
(`.ufo/l0-questions.md:42`, `tsukuroi-shokunin/PROVINCE.md:3-4,11-13,51`,
`kaidoku-shokunin/PROVINCE.md:50,64-71,76-79,125`) check out; all six base-commit digests,
the S036 snapshot hash and every quoted anchor line re-verify; the stdout pin reproduces.

## Residual risk and verification gaps

- **The reviewed artifact is the scratch draft, not a lane file.** The report-path target
  `corpus/knowledge/round-64-firmware-region-byte-evidence.md` is absent; the draft was
  still being edited at review end (two pinned revisions). L1 must integrate the corrected
  revision and re-pin the stdout hash; my line citations are to the pinned latest copy only.
- **Q01/Q02 remain conditional on the registry append.** `corpus/SOURCES.md` has no S036 or
  S037 row at review time. A draftsman's S036 row exists in scratch
  (`/tmp/revenger-r64-review-sources/selftest.md:3`) with the same tier/scope/snapshot
  anchor; I did not treat it as registered. If L1 appends S036 without `generator.py`/
  `receipt.json` in S037, F4 stands.
- **Blind Q03 derivation is another seat's deliverable** and is not covered here.
- **Counter risk for L1:** `reports/round-64/measure.py:37-48` counts any cited entry that
  exists and is not marked `admission-status: rejected` as backing. The candidate marker is
  `admission-status: candidate`, so flipping README C07 to `held` naming this draft would
  lift `K_HELD_BACKED` to 8/14 even though the Q map and Q11 are defective. Do not flip
  until F1/F2 and, if S037 is not widened, F4 are fixed and a fresh seat re-reviews. The K
  probe measures existence, never quality — as the contract says.
- **No LSP application:** this artifact is prose/data with no callers or definitions, and
  the `lsp` device is not present in this seat's tool set; literal `grep` was used only for
  two in-tree absence checks (S036/S037 row count, `unblob` mention count), each backed by
  direct reads for content. No semantic claim rests on grep output.
- Installs: **none** (no uv/npx/binary install; no pacman transaction). Scratch:
  `/tmp/revenger-r64-q09-review/` (pinned copies only), removable on landing.

## Re-review — landed text (final bytes)

Same identity, same criteria. Reviewed the landed lane file
`corpus/knowledge/round-64-firmware-region-byte-evidence.md`: 53098 B, 496 lines, sha256
`9bf21e5057b77f17a8406af9d006fb4594dd2da54c6d0920f4ca842cfa3e0ebf` (matches the routed
hash). This replaces the scratch review bound to `0a3730a1…` (the delivered revision);
HEAD `671e3a1` still contains `0a3730a1…`, so the corrected bytes are a **working-tree
modification** (`git status`: ` M corpus/knowledge/round-64-firmware-region-byte-evidence.md`).

**Verdict: PASS on every criterion in my brief; no actionable finding remains in scope.**
The candidate is admissible on Q01–Q13 as reviewed; the README C07 flip is L1's.

### Re-run evidence

- Embedded `### Code` block is byte-identical to the previously pinned readout
  (`2abe0c13…fabae1`); running it from the lane root exits 0 and prints 7 JSON lines with
  stdout sha256 `aa353251f7529a00c4336f9bf8cae6634838b8d10bd20e24b7340d94cf1314ae` — the
  header `recheck:` pin holds. The script reads only `corpus/` paths (fixture, oracle,
  record, ledger), so the pin reproduces from a corpus-only archive; item 10's snapshot
  line is a separate shell command and is explicitly flagged as outside `corpus/`.
- Item 11's command was replayed verbatim; its output on this tree is identical
  (`region_count` 2, `names_present` False, `decompressed_digest_present` False,
  `extractions` {}, `unblob_lower` 0, `unblob_upper` 1).
- Item 10's sizes and digests re-verified: generator 5532 B `4e5d…`, receipt 492 B
  `e930…`, S036 snapshot 10695 B `e422b481…7933609`.
- S036 and S037 rows now exist in `corpus/SOURCES.md` (lines 83–84); S037 names all six
  files including `generator.py` and `receipt.json`, tier A for byte/record
  correspondence, at base `666ea84b…` — F4 resolved and Q01/Q02 unblocked. S036 keeps the
  route-scope-only tier A wording.
- `README.md` C07 is still `frontier` and the two C2 verifier scripts are the only other
  modified paths; `corpus/live` and `corpus/fixtures` remain byte-clean.

### Resolution of prior findings

| Prior | Status | Evidence in landed text |
|---|---|---|
| F1 Q-map mislabels (Q04/Q05/Q07/Q10/Q12), no `n/a` | **RESOLVED** | Map lines 209–221: Q04 answers tool/version/manual-label; Q05 `n/a (no readiness or capability claim)`; Q07 `n/a (no predicted parser behaviour)`; Q08 "Superseded by Q11"; Q10 scopes family/operation/version/input and points to §Cross-lane scope note; Q12 `n/a (no rejected source row cited)`. Every row now answers its named criterion. |
| F2 "13 compared fields" overstated derivation | **RESOLVED** | Item 7 splits 16 derived / 9 recorded constants; item 8 splits 5 derived / 8 recorded; Q11 row (219) states the `derived` key convention and labels the constant rows recorded, not re-derived. Counts re-checked against the readout's 25/13 checks — correct. |
| F3 record-absence sentences had no command/output | **RESOLVED** | Item 11 (144–152) adds a `python3 -c` command and prints region keys, name/digest absence flags, `extractions` `{}`, and both `Unblob` counts. Output reproduced exactly. |
| F4 S037 scope vs six files | **RESOLVED** | Landed S037 row names `firmware-r63.bin`, `truth.json`, `generator.py`, `inspection.json`, `receipt.json`, `LEDGER.md`, tier A for byte content and literal saved fields (E satisfied). |
| F5 "produced independently" provenance assertion | **RESOLVED** | The sentence now reads "the record's provenance is **recorded provenance**: Binwalk 3.1.0 `--search-all` as the record's own envelope and `raw_result` name it, and no digest establishes that…"; the Q09 disclaimer (line 163) is unchanged. |
| F6 oracle independence absent from Unknown | **RESOLVED** | U6 (190): "whether the oracle is an independent expectation: it is not… 25 comparisons show internal consistency… not independent confirmation". |
| F7 host version asserted without command | **RESOLVED** | Item 3 adds `python3 -V` → `Python 3.14.8` and `zlib.ZLIB_VERSION/ ZLIB_RUNTIME_VERSION` → `1.3.2 1.3.2`. |

### Residual notes (non-blocking)

1. Nit: item 8 counts the two per-offset presence checks among the "8 recorded fields";
   presence is a membership test over the record's region list against byte-derived
   offsets, so the label under-claims rather than over-claims. No Q11 impact; optional
   rewording only.
2. **Commit before measuring.** The reviewed bytes are uncommitted (HEAD `671e3a1` holds
   `0a3730a1…`). The frozen counter runs on a committed `git archive <commit> corpus`
   tree; commit the corrected entry before the final measurement so the measured bytes are
   the reviewed bytes. Until the README flip, `K_HELD_BACKED` stays 7/14 and
   `README_TOKEN_LEGEND_MISMATCH` stays 1.
3. The flip must name only this entry per the contract; the entry's own scope text already
   disclaims extraction/vendor/other-fixture ground and reports ADJ-06 without absorbing
   it.
4. No LSP application (prose/data artifact; no callers/definitions; device absent from this
   seat's tool set). Installs: none. No git/jj mutation was run (status/log/show reads only).

