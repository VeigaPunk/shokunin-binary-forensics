# R64ConnectorOverlap — sibling scan of C07 and the C4 receipt scripts

Read-only seat. No sibling file written. No git/jj mutation. Installs: none. Pacman not used. The planned entry `corpus/knowledge/round-64-firmware-region-byte-evidence.md` is not in the tree yet; `SKILL.md` is absent (glob of that path skipped as missing; `SCORECARD.md:124` still records it absent). This report names the sentence; it does not draft either file.

Axes named from frozen `reports/round-64/claims.md`: coverage K (C1, C07), calibration (C2, `C4_RECEIPT_KILLED_ATTRIBUTED`), and the unowned adjacency hold (ADJ-06 reported, not absorbed). A move is kept only if K can still rise on admission and C4 can still go 0/2 → 2/2 without closing that hold or moving any other README row. Red-before (`reports/round-64/measure-before.log`): `K_HELD_BACKED=7/14`, `K_ROW C07 status=frontier`, `README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']`, `F_FAMILIES` already includes `archives` and `firmware`, `C4_RECEIPT_KILLED_ATTRIBUTED=0/2`.

## Verdict

Not "no overlap." ADJ-06 is still open, and this round's new ground is the first knowledge token on the contested firmware verb. Kotodama and chousa do not hold that ground. C4 does not touch a sibling. Do not wait for an integrator ruling before C1 or C2.

Contradiction, left unsmoothed. These four sentences do not reduce to one owner:

1. `revenger-shokunin/PROVINCE.md:3-4` — "Owns: reverse engineering of shipped artifacts — … archives, firmware".
2. `kaidoku-shokunin/PROVINCE.md:3-5` — same shipped-artifact domain, "archives and packages"; `:76-79` pruned firmware out of Frontier because it is already Core; `:125` holds `inspect-firmware-regions` and `extract-firmware` on real blobs (GSP 56/156, `ev_0388cb9a…`, `ev_4009f834…`; binwalk 3.1.0 / unblob 26.6.4). `:242` and `:274-275` still say kaidoku/revenger arbitration is open.
3. `tsukuroi-shokunin/PROVINCE.md:51` (ADJ-06) — recipient is "protocol integrator — kaidoku/revenger ownership unresolved"; tsukuroi keeps driver/firmware health and "no binary-internals inference". `:79-80` and `:150-152` repeat that this is not a grant. Fleet `.ufo/l0-questions.md:42` is still the open question that asks to arbitrate the overlap before an ADJ-06 analysis is routed.
4. `MANIFEST.json` `roster` (13 ids, array ends at `:110`) lists both lanes with near-duplicate domains: revenger "reverse engineering of shipped artifacts, evidence-ledger discipline" (`:95-100`); kaidoku "reverse engineering of shipped artifacts with REA on this host" (`:103-108`). Tsukuroi, the lane that filed ADJ-06, is not in that array. Kotodama and chousa are not in it either. The roster duplicates the contested domain and omits the filer, so a roster read cannot settle ADJ-06.

## What this round adds, and why the round-63 fence is not enough

Round 63 saved `inspect_firmware_regions` on the authored fixture and did not admit a C07 entry. `corpus/README.md:36` is still `frontier` with knowledge `—`. The legend (`corpus/README.md:21-24`) defines `frontier` as "no knowledge and no saved record" and `held` as "at least one admitted knowledge entry covers the ground." The saved record exists (`corpus/live/runs/round-63/inspection.json`: `operation` `inspect_firmware_regions`, provider Binwalk 3.1.0, subject `corpus/fixtures/firmware-r63/firmware-r63.bin`). That is why `README_TOKEN_LEGEND_MISMATCH=1` at base. C1, if admitted, flips that token to `held`.

The round-63 connector told C2 not to say revenger owns firmware (`.ufo/waves/round-63/build/R63ConnectorOverlap.md:42`). The landed C06 entry then used a generic Q10 line: "sibling-lane overlap is left with the operator, this entry declares no ownership and cites no other lane's file as support" (`corpus/knowledge/round-63-zip-central-directory-evidence.md:731`). That line is unauditable: it does not name the contested item. Copying it onto C07 fails for a second reason. A `held` cell whose row label is "firmware images" is what a later handoff will quote. Tsukuroi OUT-009 (`PROVINCE.md:129`) already paraphrases this lane as owning firmware; R20 (`:150`) says that paraphrase is not a grant. The `held` token is the first coverage-map sentence that agrees with the paraphrase. The generic deferral sits inside the entry, where the map reader does not look.

Second-order, same verb and same pin. README frontier note `:63-66` already says the host has binwalk 3.1.0 and unblob 26.6.4 and names both `inspect_firmware_regions` and `extract_firmware`. Kaidoku Core `:125` holds those versions and both verbs. Claims (`reports/round-64/claims.md:29-31,41-48`) allow S036 only as route-scope for the pinned producer version, and forbid a provider-completeness claim. Promoting `:63-66` into the admitted entry or into the new SKILL would absorb kaidoku's pin registry (`PROVINCE.md:64-71`: that registry never stands for a sibling's runtime capability; the converse holds here). Recording Binwalk 3.1.0 as a field of this one saved record is correspondence, not that claim.

Archives stay contested and are not this claim. Kaidoku `:50` holds archive/package inventory. F already counts `archives` (`measure-before.log`). C06 is already `held` on one authored ZIP (`corpus/README.md:35`). A C07 admission must not be worded as closing the archives half of ADJ-06, and must not reopen C06.

## Sibling scan of the four named provinces

| Lane | On roster? | Overlap with C07 / C4 | Disposition |
|---|---|---|---|
| kaidoku | yes (`MANIFEST.json:103-108`) | Core firmware regions + extract on vendor blobs; Core archive/package inventory. Live PE via Ghidra (`:51`) is not these receipt scripts. | Report, do not absorb. Do not cite `ev_0388cb9a…` / `ev_4009f834…` or GSP counts. |
| tsukuroi | no | ADJ-06 filer. Owns driver/firmware health, not internals (`:3-4`, `:11-13`, `:51`). Firmware updates stay operator-owned (`:167-174`). | Report, do not absorb. Do not ask this lane to pick the RE owner. |
| kotodama | no | Domain is linguistic-cultural worldbuilding (`PROVINCE.md:3-7`). Refuses canon, game mechanics, general source-research, web publishing, prompt craft (`:16-20`). No firmware, no PE receipt verifier. | No sentence. Null overlap. |
| chousa | no | Domain is deep-research method (`PROVINCE.md:3-4`): framing, source hierarchy, citation chaining. Refuses bounty packages, model-quality claims, orchestration (`:10-15`). | No sentence, with one fence: do not cite chousa's verify-claims/verify-chain gates as this lane's Q01 procedure. Admission stays `corpus/QUALITY.md`. |

C4 scripts are lane-internal. Among revenger, kaidoku, tsukuroi, chousa, and kotodama, `verify_icon_languages.py` and `verify_multi_icon_states.py` exist only at `revenger-shokunin/corpus/`. Tsukuroi ADJ-07 (`PROVINCE.md:52`) gives tameshi the mutation method and leaves each lane's gate with that lane. The frozen conjunct deletion and the `forged receipt stdout accepted` control (`claims.md:65-80`) stay inside those two files. No sibling citation on the C4 patch.

## Proposed move

One sentence, carried in two places. Do not edit `PROVINCE.md`. Do not add a `SOURCES.md` row for a sibling. Do not rule ADJ-06.

Entry `corpus/knowledge/round-64-firmware-region-byte-evidence.md`, a `## Cross-lane scope note (Q10)` that names the contested lines (unlike C06's generic Q10):

> Reported, not absorbed: this entry covers only authored `corpus/fixtures/firmware-r63/firmware-r63.bin` bytes against the saved `inspect_firmware_regions` record `corpus/live/runs/round-63/inspection.json`; a C07 `held` token does not settle ADJ-06 (fleet `.ufo/l0-questions.md:42` open; `tsukuroi-shokunin/PROVINCE.md:51` still names the recipient "protocol integrator — kaidoku/revenger ownership unresolved"), does not absorb kaidoku Core live `inspect-firmware-regions` / `extract-firmware` or its archive inventory (`kaidoku-shokunin/PROVINCE.md:50,76-79,125`) or its provider-pin registry (`:64-71`), and does not absorb tsukuroi's driver/firmware health plane (`tsukuroi-shokunin/PROVINCE.md:3-4,11-13`).

README C07 knowledge cell, only if every admission criterion passes (claims: flip `frontier → held` naming only the new entry; if C1 falsifies, `frontier → uncovered` and no other row changes). Match the C06 cell's parenthetical, which is the fence a map reader actually sees:

> `knowledge/round-64-firmware-region-byte-evidence.md` (authored `firmware-r63.bin` bytes ↔ one saved `inspect_firmware_regions` record only; not kaidoku live firmware or archive Core, not tsukuroi host firmware health, not an ADJ-06 ruling)

SKILL.md, checklist work this round whether or not C1 admits (`claims.md:122`, SHONEN box 1). The draft sources committed province bytes and will otherwise copy "Owns: … archives, firmware". One line, not a province rewrite:

> Firmware and archives stay reported, not absorbed: ADJ-06 is unresolved (`.ufo/l0-questions.md:42`); this skill does not grant firmware or archive ownership.

If C1 falsifies and a rejected candidate is retained, that file still carries the entry sentence. A rejected file without it can be quoted as ownership, and a rejected file is not coverage (`corpus/README.md:23-24`).

Affected axes: K can move on admission and does not move if the sentence is the only addition; calibration C4 is untouched and stays lane-internal; adjacency stays "reported, not absorbed" (`SCORECARD.md:136`) and becomes auditable (no harm, the hold is not closed); F, freshness, denominators, and `HOLDS_OK` / `HOLDS_OK_V2` are not inputs to this scan.

## Risks

- Citing `ev_0388cb9a…`, `ev_4009f834…`, GSP region counts, or README `:63-66` as host readiness inside the entry or the skill absorbs kaidoku `:125` and exceeds the contract's "no provider-completeness" limit. The saved record's Binwalk 3.1.0 field may be quoted only as a recorded field of that one file.
- A `SOURCES.md` row pointing at kaidoku, tsukuroi, chousa, or kotodama would turn a contest note into a source. Q10 (`corpus/QUALITY.md:22`) wants the contest reported, not sourced.
- Editing `PROVINCE.md:3-7` to "exclusively owns" would contradict ADJ-06 and is out of this round's void conditions.
- Reusing C06's "cites no other lane's file" would hide the `held`-token vector this round actually creates.
- Blocking C1 or C2 on an integrator ruling of ADJ-06 would spend an unowned question against a claim that the contract already scoped to one fixture and one saved record.

## Verification

For L1, re-read; do not re-run producers for this scan:

- The entry contains the sentence above; `grep` of the entry finds no `ev_0388cb9a`, no `ev_4009f834`, no `GSP`, and no `SOURCES.md` row whose path is a sibling corpus file.
- On admission, the README diff touches only the C07 row, and that cell includes the parenthetical. On falsification, C07 becomes `uncovered` and no other status cell changes.
- Landed `SKILL.md`, if any, contains the one non-ownership line and does not say this lane exclusively owns firmware or archives.
- The C4 diff is only `corpus/verify_icon_languages.py` and `corpus/verify_multi_icon_states.py`. A filename search of kaidoku, tsukuroi, chousa, and kotodama still returns neither basename.
- `SCORECARD.md:136` stays the ADJ-06 "reported, not absorbed" sentence. `PROVINCE.md` is byte-unchanged.

Files written: this report only.
