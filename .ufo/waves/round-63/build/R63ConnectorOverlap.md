# R63ConnectorOverlap — sibling scan of C06, C07, and the two receipt verifiers

Read-only seat. Roster from `/home/vgpnk/Projects/shokunin/MANIFEST.json` (`roster` length 13). Provinces opened read-only. No sibling file written. Installs: none. Pacman not used.

Axes named for this round (frozen `reports/round-63/claims.md`): coverage K (C06), coverage F (firmware family), calibration C3, plus the unowned adjacency hold (SCORECARD `ADJ-06` reported, not absorbed). A move is kept only if it can lift K or F without closing that hold or touching the two verifiers' ownership.

## Verdict

Not "no overlap." Three contested-scope questions, each **report-not-absorb**. None of them is a reason to drop C1's authored ZIP field readout or C2's authored-fixture family record, and none of them authorizes a claim that revenger now exclusively owns archives or firmware.

Contradiction, left unsmoothed: `revenger-shokunin/PROVINCE.md:3-4` says this lane "Owns … archives, firmware." `kaidoku-shokunin/PROVINCE.md:3-5` names the same shipped-artifact domain including "archives and packages," and `:125` already holds firmware-region extraction as Core. `tsukuroi-shokunin/PROVINCE.md:51` (ADJ-06) still names the recipient "protocol integrator — kaidoku/revenger ownership unresolved." Those three sentences do not reduce to one owner.

## (1) C06 archives — who holds ZIP ground

| Lane | What it actually holds | Pointer |
|---|---|---|
| revenger | Named owner of archives under the evidence ledger. Map row C06 is still `partial` (archive-tool row only). Work evidence is this lane's own `fixtures/archive-r2`, `nested-r11`, `duplicate-r15`. | `revenger-shokunin/PROVINCE.md:3-7`; `corpus/README.md:35` |
| kaidoku | Core "Archive/package inventory": `inspect_artifact` / `extract_artifact` on the pacman `.pkg.tar.zst` cache and `.MTREE` hashes. Not a PKWARE central-directory field layout. | `kaidoku-shokunin/PROVINCE.md:5`, `:50` |
| kaidoku | APK inventory already records REA's limitation, verbatim: "ZIP inventory lists central-directory entries only. Bytes after the central directory, including an APK Signing Block or a ZIP comment, are not occurrences." | `kaidoku-shokunin/corpus/knowledge/2026-10-13-r3-apk-inventory.md:53-60` |
| game-dev-3d | Authored ZIP used only as a GLB carrier. Lesson observes REA central-directory occurrences `triangle.glb` + `truth.json`, and that inventory omits bytes after the central directory. Province refuses reverse engineering as an end and names revenger as the contested lane. | `game-dev-3d-shokunin/corpus/lessons/r10-rea-zip-carrier.md:1-14`; `PROVINCE.md:8-12`, `:38-41`, `:65`, `:70`, `:78` |
| kasegi | No ZIP format and no firmware. Domain is bounty scopes and claim packages. "Claim packages" is submission packaging, not an archive format. | `kasegi-shokunin/PROVINCE.md:3-4`, `:24-25`, `:35-38` |
| tsukuroi | ADJ-06 hands driver/firmware/**package** mechanism that needs shipped-artifact RE to the integrator, not to this lane. | `tsukuroi-shokunin/PROVINCE.md:51` |

Homonyms, not ZIP ground: kake's GitHub Actions upload archives (`kake-shokunin/PROVINCE.md:245-248`); kengaku's relocated `~/archive/bench-arena` path; kama's llama release tarball. No other province names PKWARE APPNOTE fields, EOCD counts, or local-header offsets.

**Is a ZIP central-directory byte-readout inside revenger's shipped-artifact province?** Yes, for this lane's authored `corpus/fixtures/archive-r2/fixture.zip` only: member names, local-header offsets, compressed/uncompressed sizes, CRC-32, and EOCD counts, each derived from those bytes and compared to this lane's `truth.json` and the saved record `corpus/live/runs/20261012T164246Z/artifact-inspection.json`. That subject is the frozen C1 scope (`reports/round-63/claims.md:19-31`) and is not stated by any sibling.

**Contested item (report, do not absorb):** the sentence both siblings already hold — ZIP inventory lists central-directory entries only, and bytes after the central directory are not occurrences. C1's frozen "no trailing-bytes claim" is the fence. The new entry must not restate that limitation as revenger knowledge, must not cite kaidoku's APK evidence or game-dev-3d's `ev_3f68dd30…` / `ev_289ef677…` carrier ids, and must not treat kaidoku's pacman archive inventory as this lane's ground. ADJ-06 stays open (`revenger-shokunin/SCORECARD.md:136`).

## (2) C07 firmware — does any sibling own it?

Yes, in two different senses. Neither is an authored inert image with a `truth.json` byte oracle.

| Lane | Sense of "firmware" | Pointer |
|---|---|---|
| kaidoku | **Core, shipped-artifact.** `inspect-firmware-regions` and `extract-firmware` on real blobs: GSP 56/156 regions (`ev_0388cb9a…`, `ev_4009f834…`), nvidia ucode stubs, `pkg.tar.zst` carve. Binwalk 3.1.0 / unblob 26.6.4. Firmware was pruned out of Frontier because it is already held. | `kaidoku-shokunin/PROVINCE.md:76-79`, `:125` |
| tsukuroi | **Host health inventory, not internals.** Driver/firmware plane (kernel modules, nvidia driver + GSP presence, `nvidia-smi` shape). ADJ-06 keeps "no binary-internals inference" and forbids invoking a target. Firmware updates stay operator-owned. | `tsukuroi-shokunin/PROVINCE.md:3-4`, `:11-13`, `:51`, `:150-152`, `:167-174` |
| mori | Refuses driver/firmware and routes it to tsukuroi. Not an RE owner. | `mori-shokunin/PROVINCE.md:12-14`, `:66` |
| revenger | Province names firmware, but map row C07 is still `frontier` with no knowledge entry. | `revenger-shokunin/PROVINCE.md:4`; `corpus/README.md:36`, `:63-66` |
| kasegi | Does not own firmware. | `kasegi-shokunin/PROVINCE.md:3-4`, `:35-38` |

**Contested item (report, do not absorb):** the verb `inspect-firmware-regions` plus the binwalk 3.1.0 / unblob 26.6.4 pins. Kaidoku already holds that probe on vendor GSP/nvidia blobs. C2 may still add this lane's first saved `firmware` family record (`claims.md:43-61`) only while the subject is the new inert fixture under `corpus/fixtures/firmware-r63/` and the new run under `corpus/live/runs/round-63/`. The entry must not restate kaidoku's GSP region counts or evidence ids, must not claim nvidia/host firmware health (tsukuroi's plane), must not run `extract-firmware` or any payload, and must not say revenger now owns firmware. ADJ-06 remains the integrator's question.

## (3) The two patched verifiers

Lane-internal. Fleet filename search returns only:

- `revenger-shokunin/corpus/verify_named_multi_icon_states.py`
- `revenger-shokunin/corpus/verify_icon_states.py`

`tameshi-shokunin/PROVINCE.md` does not name either script. Tsukuroi ADJ-07 gives tameshi the reusable mutation *method* and leaves each lane's gate with that lane (`tsukuroi-shokunin/PROVINCE.md:52`). C3's frozen conjunct deletions and `receipt_ok` controls (`claims.md:63-88`) stay inside these two files. No sibling pointer. Not contested.

## Proposed move

Keep the subject split; do not ask the integrator to rule ADJ-06 before C1 or C2.

- C1 (K): admit the central-directory field correspondence for `archive-r2/fixture.zip` only. One sentence in the entry: trailing bytes after the central directory, APK Signing Blocks, and other lanes' ZIP carriers are not this claim (pointers above). That is the non-absorption, and it matches the frozen "no trailing-bytes claim."
- C2 (F): save one real `inspect-firmware-regions` record of the authored inert fixture with byte-oracle agreement. One sentence in the entry: kaidoku's GSP/nvidia region map and tsukuroi's host firmware plane are not this claim. Do not flip a province ownership sentence.
- C3: patch only the two scripts named above. No sibling citation.

Affected axes: K and F can move; adjacency stays "reported, not absorbed" (no harm); C3 stays lane-internal (no harm). Holds: no sibling corpus byte is an input to these claims, so the preservation manifest is untouched by this scan.

## Risks

- Restating kaidoku's or game-dev-3d's "bytes after the central directory" limitation inside the C06 entry would absorb their ground and is the C1 failure mode even if the field table is correct.
- Citing `ev_0388cb9a…` / `ev_4009f834…`, or treating binwalk's signature list as a firmware-ownership proof, would absorb kaidoku Core and would not by itself satisfy F (F moves only on a new saved record with oracle agreement).
- Editing `PROVINCE.md:4` to "exclusively owns firmware/archives" would contradict ADJ-06 and is out of scope.
- A README C06 flip before fresh Q01–Q13 decisions is still L1's gate, not this seat's (`claims.md:38-41`).

## Verification

Re-read, do not re-run producers:

- `test -f revenger-shokunin/corpus/fixtures/archive-r2/fixture.zip` and the saved record path in `claims.md:28-29` still resolve; the new knowledge file does not cite `kaidoku-shokunin/` or `game-dev-3d-shokunin/` evidence ids.
- The C2 receipt's fixture path is under `corpus/fixtures/firmware-r63/` and its operation is `inspect_firmware_regions`; it does not name GSP, nvidia ucode, or tsukuroi.
- `find` of the two verifier basenames still returns only the two revenger paths after the C3 patch.
- SCORECARD adjacency row stays the ADJ-06 "reported, not absorbed" sentence (`SCORECARD.md:136`).

Files written: this report only.
