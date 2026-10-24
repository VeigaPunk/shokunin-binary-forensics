# R64EntryC07 — C07 candidate entry draft (scribe)

Report: .ufo/waves/round-64/R64EntryC07.md

## Deliverable

- **Candidate (deliverable):** `/tmp/revenger-r64-entry/candidate.md` — 48440 bytes, sha256 `0a3730a1a03b19ef134930a8eb180147be8b6e503fbd7040fdd7617eafed0a22`.
- **Integration target (not written by this seat):** `corpus/knowledge/round-64-firmware-region-byte-evidence.md` — L1 integrates after review. No file under `corpus/` was created or modified.
- **Readout script embedded in the entry §Reproduce:** `/tmp/revenger-r64-entry/readout.py` (also `extracted.py`, byte-identical extraction used for the parity check) — 10018 bytes, sha256 `2abe0c130ae29de27ae194511e3b4e5061364818cf94d8d8671c3019eafabae1`.
- Full stdout of the 7-fact run: `/tmp/revenger-r64-entry/all.txt` — 6978 bytes, sha256 `aa353251f7529a00c4336f9bf8cae6634838b8d10bd20e24b7340d94cf1314ae`.
- Scratch generator replay tree: `/tmp/revenger-r64-entry/gen/` (byte-identical fixture/oracle, see gate G4).

## Behavior

The entry drafts a manual, stdlib-only byte readout of the one authored fixture `corpus/fixtures/firmware-r63/firmware-r63.bin`, its correspondence to `corpus/fixtures/firmware-r63/truth.json` (25/25 compared fields match) and to the saved record `corpus/live/runs/round-63/inspection.json` (13/13 compared fields match), with observation/inference/unknown separation, six limitations, a Q01–Q13 map, and a verbatim `source:` header naming S036 (pinned tag `rea-agents-6.5.0`) and S037 (six file digests at claim base `666ea84b…`).

Derivation was independent: members were found by scanning every byte offset for a zlib stream reaching end-of-stream, never by reading `truth.json` first. Padding spans are the maximal all-zero runs of the **complement** of member ranges. Every value in §Observation carries its in-entry command and that command's printed output; the 7-line stdout is pinned by sha256 in the `recheck:` field.

## Gates exercised (this seat)

| Gate | Command | Outcome |
|---|---|---|
| G1 readout self-run | `python3 -B readout.py /home/vgpnk/Projects/shokunin/revenger-shokunin` | exit 0, 7 lines, sha256 `aa353251f7529a00c4336f9bf8cae6634838b8d10bd20e24b7340d94cf1314ae`; stderr 0 bytes |
| G2 entry-embedded script parity | extract §Reproduce code block → `python3 -B extracted.py <lane-root>` | exit 0, 7 lines, same sha256 `aa353251…` |
| G3 fixture/oracle/record identity at base | `git show 666ea84b…:<path> \| sha256sum` vs `sha256sum <path>` on six files | all six equal (fixture `bdfe9f46…510be`, generator `4e5d5975…3db4`, truth `9663f90b…65e6`, inspection `f6997835…71f9`, receipt `e930a549…b94d`, LEDGER `25a4a18b…1a6`) |
| G4 generator replay (scratch only) | `cp` generator to `/tmp/revenger-r64-entry/gen/`; `python3 -B generator.py`; `sha256sum` | exit 0; fixture `bdfe9f46…510be` (2048 B) and truth `9663f90b…65e6` reproduced byte-for-byte; host Python 3.14.8 / zlib 1.3.2 = recipe |
| G5 oracle correspondence | `--fact oracle` | 25 checks, 0 failures, `all_match: true` |
| G6 record correspondence | `--fact record` | 13 checks, 0 failures, `all_match: true`; record `coverage=signature_scan`, `extractions={}`, region kinds `{"zlib"}` |
| G7 cleanliness | scan candidate | 0 occurrences of the lane absolute root, 0 unreplaced markers; all paths in the entry are repo-relative |
| G8 base readout values (independent) | `--fact regions` / `--fact members` | regions `[0,512)pad`, `[512,591)zlib`, `[591,1024)pad`, `[1024,1114)zlib`, `[1114,2048)pad`, covered 2048, contiguous; members 79→78 B sha `a5718481…7b86`, 90→97 B sha `2d0d86aa…aba9`; both headers `78 da`, FLEVEL 3, FDICT 0, Adler-32 trailer matches |

Not exercised by this seat (main-agent / wave work): the frozen counter `reports/round-64/measure.py`, `K_HELD_BACKED`, README token flips, Q01–Q13 admission decisions, review of the sibling `firmware-readout.py`.

## Touched surfaces

Writes (all lane-owned scratch):
- `/tmp/revenger-r64-entry/candidate.md` (deliverable)
- `/tmp/revenger-r64-entry/readout.py`, `extracted.py`, `template.md`, `all.txt`, `err.txt`
- `/tmp/revenger-r64-entry/gen/{generator.py,firmware-r63.bin,truth.json}` (copy + replay)

Reads only (lane repo): the seat brief, `reports/round-64/claims.md`, `corpus/fixtures/firmware-r63/{firmware-r63.bin,generator.py,truth.json}`, `corpus/live/runs/round-63/{inspection.json,receipt.json,LEDGER.md}`, `corpus/knowledge/round-63-zip-central-directory-evidence.md` (format precedent), `corpus/README.md` (C07 row), `corpus/SOURCES.md`, `.ufo/waves/round-64/source-snapshots/rea-firmware-guide.md` + `.provenance.json`, `git show`/`git status` (read-only).

No git/jj mutations, no commit/push, no corpus writes, no edits to `.ufo/waves` spec/registry files, `MANIFEST.json`, fleet files or sibling lanes. No tool installs (nothing needed; Python 3.14.8 and zlib 1.3.2 already present).

## Provenance used in the entry

- **S036**: `.ufo/waves/round-64/source-snapshots/rea-firmware-guide.md`, 10695 bytes, sha256 `e422b4816b1dbc912680afefb8e23acfd8ead4aea08c3d722d4ccb5207933609`; URL `https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/docs/firmware-analysis.md`; sidecar records HTTP 200, tag commit `3b79af28…`, blob `152819177f…`; anchors quoted from lines 3, 56, 83-85, 91-96. **I did not re-fetch the URL**; the snapshot and its provenance sidecar are the cited artifact.
- **S037**: six files hashed at base `666ea84b6be2eec2b0359f556ba2429fc9044c36` (hashes in gate G3).
- Saved record is treated as observation layer only; per its own fields its coverage is `signature_scan` and both region sizes are `provider_reported_validation_unknown`.

## Findings

- **F1 (dependency absent).** No `R64FirmwareReadout` artifact was present when drafting in `/tmp/revenger-r64-*` (no such directory at discovery), so the brief's fallback applied: values were derived independently and the brief's "still re-run each command" condition is moot. L1 should re-run the `recheck` command on the integrated tree before admission.
- **F2 (partition counterexample, sibling script).** `R64CriticCounts` reports that a sibling `firmware-readout.py` labels a one-byte span at offset 1098 as padding. My measurement confirms byte 1098 is `0x00` and lies inside member B's range `[1024,1114)`; taking whole-file maximal zero runs yields `(0,512)`, `(591,433)`, `(1098,1)`, `(1114,934)`. This draft's complement-first rule yields exactly `[0,512)`, `[591,1024)`, `[1114,2048)` and covers 2048 bytes contiguously — the counterexample does not apply to this draft, and the rule is stated in-entry so reviewers can falsify it. Critic follow-up: the finding concerned an earlier readout snapshot (`C3CE`/hash `d63cd25f…`), and the critic states it claims no gate decision or re-review of this final draft; its described complement plus all-offset scan rules match this draft.
- **F3 (recipe is not oracle-checked).** `R64CriticFixture` reports `oracle_check.py` never validates `build_recipe`, so recipe payload/name edits and padding splits leave the checked inputs identical. The draft therefore frames agreement as byte/record correspondence, not canonical or unique truth; `build_recipe` is labelled oracle-stated metadata, and generator replay (G4) is the only support for it, explicitly host-bounded.
- **F4 (member names are not byte-derived).** A zlib stream carries no name; `diagnostic-note`/`component-note` are generator/oracle labels. The entry states this in item 6 and in unknown U1, after the critic's correction.
- **F4c (L1 correction round).** Added `## Cross-lane scope note (Q10)` after §Limitations: reported-not-absorbed fence for ADJ-06 (fleet `.ufo/l0-questions.md:42` open; tsukuroi `PROVINCE.md:51` recipient unresolved), kaidoku Core live firmware surface/archive inventory/provider-pin registry, and tsukuroi driver/firmware health plane — no evidence IDs and no README host pins. Q06 row replaced with fixture-premises-byte-verified (items 1–5 derived by command from the built bytes); Q12 and Q13 rows left as-is per L1 confirmation. No derived value, command or output changed; recheck digest unchanged (`aa353251…`).
- **F4b (reviewer wording fixes applied).** `R64CriticFixture` flagged four spots in the reviewed draft; all applied: coverage-map no longer attributes `extract_firmware`/families to the C07 row (the row says only "firmware images"); truth correspondence now says the 25 selected comparisons match, not "complete for every field"; Q12 now says the authored oracle shares one author with the image and that only the readout is independent of the saved record; record-origin wording now attributes the run to the record's own envelope/`raw_result` rather than asserting producer origin from consistency. Recheck digest unchanged (`aa353251…`), no markers or absolute-path leaks.
- **F5 (record is narrower than the oracle).** The saved record has no padding regions, no names, no decompressed digests, `extractions` `{}`, and no Unblob appearance; the ledger's `O11` author-side Unblob probe is outside the record and is explicitly not used as evidence.
- **F6 (receipt hash).** `receipt.json` current bytes hash `e930a549…b94d` at base and in the working tree, matching the ledger's corrected pin; the ledger's note records a prior one-hex-char pin defect. No conflict with this entry.
- **F7 (claim status).** This is a candidate only. Admission is fresh-seat Q01–Q13 work; the K counter was not run by this seat, and no K movement, README token flip or `SOURCES.md` append is claimed or performed.

## Conflicts (verbatim)

- `R64CriticCounts`: "Counts counterexample in current firmware-readout.py: zero_spans emits (1098,1099) labelled padding, but byte1098=00 lies INSIDE valid second compressed stream [1024,1114). Correct padding exactly [0,512),[591,1024),[1114,2048); partition2048, not2049. Executor notified. Hardcoded EXPECTED_MEMBER_OFFSETS also provenance concern; my blind all-offset scan independently found512,1024."
- `R64CriticFixture`: "Oracle review finding: oracle_check.py never validates build_recipe; changing recipe payload/name leaves checked inputs identical. Padding splits also preserve all checks. Please say agreement is on byte/record fields, not unique/canonical truth or authenticated recipe. Attribute only two zlib hits to saved Binwalk 3.1.0 --search-all scan; padding, names and inflated hashes are manual, and 'firmware' is route/coverage label, not vendor/device format."
- `R64CriticFixture` (correction): "diagnostic-note/component-note are oracle/generator-authored labels, not manual byte-derived names; zlib carries no member name."

All three are reflected in the draft's wording (F2–F4). No unresolved conflict: my independent measurement agrees with the critics on the two zlib offsets/sizes, the manual status of padding/names/inflated digests, and the record-only attribution of the Binwalk hits.

## Known limits

- Single authored fixture; the entry claims no vendor image, format family, extraction, execution, provider-completeness or authenticity.
- The padding partition is this readout's stated rule; alternatives give different spans.
- Digest matches prove only the bytes hashed (Q09 disclaimer in-entry).
- S036 was cited from the saved snapshot and its provenance sidecar, not re-fetched.
- Generator replay byte-identity holds only for Python 3.14.8 / zlib 1.3.2.
- The review rows Q01–Q13 are drafted as a map, not pass decisions; admission remains with fresh seats.
