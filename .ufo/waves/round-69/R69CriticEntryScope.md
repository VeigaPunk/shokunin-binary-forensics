SCOPE-CLEAN — Q10 PASS: every finding in the round-69 v4 entry is scoped to one authored APK fixture, one manual stdlib readout, the pinned spec versions and a named input; all seven bounds named in the brief are fenced in the entry and no fixture observation is stated as a universal. One generalising sentence exists (`:19`, instrument credit) but it is a Q04/Q11 defect, not a scope generalisation.

# R69CriticEntryScope — Q10 scope/limitation audit of `round-69-apk-axml-byte-evidence.md`

Seat `L1Revenger69.R69CriticEntryScope` · criterion **Q10 only** (`corpus/QUALITY.md:22`: "A finding is scoped to the observed family, operation, version and input. Cross-lane contested scope is reported, not absorbed." reject when "one family's observation is stated as a universal").
Record under test: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-69-apk-axml-byte-evidence.md` (215 lines, sha256 `c1e7eaac9dba4c77e578c788755dec3e3499fd8795ad0e479c51b5be7deb11d5`, `admission-status: candidate` at `:11`).
Sections read in full: `## Limitations` (`:165-167`), `## Cross-lane scope note (Q10)` (`:169-171`), `## Observation / inference / unknown` (`:159-163`); plus the whole body for the generalisation sweep. No file was edited; no git/jj mutation; no subagent; no tool installed.

## Verdict

**PASS / SCOPE-CLEAN.** No sentence states one fixture's behaviour as an APK / AXML / ZIP / dex universal. The only all-scoped sentences in the file are (a) restricted to this archive's three members (`:37`), or (b) explicit disclaimers (`:77`, `:91`, `:163`, `:167`). The ADJ-06 contest is reported upstream, not absorbed (`:171` → fleet `.ufo/l0-questions.md:42`, verified live below).

The brief's seven bounds, each tested against the bytes:

| bound | where fenced | my check |
|---|---|---|
| one authored fixture | `:15` "One authored APK, `corpus/fixtures/apk-r65/fixture.apk`"; `:167` "One authored fixture"; `:8` coverage-map "Not covered: … general AXML or ZIP-parser behavior beyond this fixture" | the readout opens exactly one path (`readout.py:21` `APK = ROOT / "fixture.apk"`, `:44` `APK.read_bytes()`); `truth.json` never occurs in the script |
| one manifest shape | `:167` "one manifest shape (a single element with three attributes)" | chunk table shows one start element `0x0102` and one end element `0x0103`, `attributeCount 3` (`:56`, `:88`) |
| UTF-8 string pool only | `:167` "UTF-8 string pool only"; `:70` flags `0x00000100`, `utf8: true` | `readout.py:151-166` decodes only the UTF-8 length-prefix path; branch is `flags & 0x100` |
| ZIP_STORED | `:167` "The container is ZIP_STORED with no data descriptors … does not exercise … compression" | true from bytes (see F6): method `0`, gp-flag `0x0` on all three local headers |
| dex header only | `:167` "The dex member is a header only and is intentionally not a valid dex program"; `:8` "Not covered: … dex validity or execution" | member is 112 bytes = `header_size` = `file_size` (`:109`) |
| manual standard-library analysis | `:15` "The analysis is **manual** … Python standard-library script"; `:161` | `readout.py:13-18` = hashlib, json, struct, sys, zlib, pathlib; `derive_axml_anchors.py:34-37` = hashlib, re, sys, pathlib; no `subprocess`/`socket`/`urllib`/`zipfile` in either |
| no provider call | `:15` "no producer is called, no network is used"; `:171` "this lane ran no provider and makes no readiness claim"; `:8` "Not covered: … provider (`inspect_android_package`) readiness or output" | no provider/JADX invocation anywhere; S043 is cited for documented scope only |

Cross-lane note (`:171`) resolves: `awk 'NR==42' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` prints the tsukuroi round-1 row asking to "arbitrate the kaidoku/revenger shipped-artifact overlap before an ADJ-06 analysis is routed" with no resolution recorded — so "reported-not-absorbed, unchanged from round 64" is accurate. The JADX-prerequisite half of that sentence is supported by the S043 snapshot (`.ufo/waves/round-65/source-snapshots/rea-android-applications.md:16-20`: "requires a separately supplied headless JADX MCP JAR 0.7.1 and Java 17 or newer").

## Named generalising sentence

`entry:19` — *"Every numbered item below is produced by the readout in §Reproduce. The script is saved verbatim as `corpus/fixtures/apk-r65/readout.py` (sha256 `92e347c3…`)"*. Item 11 is produced by `corpus/derive_axml_anchors.py`, whose command the entry itself prints at `:130` (`$ python3 -B corpus/derive_axml_anchors.py`); `:127` restricts its own credit to "items 4, 8 and 11" and `:161` names the same script. The universal is false as written.

Impacted axes: **operation** (instrument credit), not family/version/input. It is not SCOPE-BLEED under Q10 because it does not carry any fixture observation outside its observed scope — item 11's own block states its correct command, two paragraphs after the preamble. Q10 stays PASS; the sentence is a Q04 reject trigger ("a tool is credited with a result it did not output") and is finding **F2** below. This is the *same* finding the round-68 Q10 seat filed at v3:17 (`.ufo/waves/round-68/R68ReviewEntryQ10.md:137`, "medium · Q04/Q11") and the v4 kept the sentence verbatim (only its line number moved 17 → 19).

## Findings (adjacent criteria; none changes the Q10 verdict; ordered by severity)

**F1 · high · build-state / Q-map completeness.** The v4 §Q-map carries **8** rows (`:177-184`: Q01, Q02, Q04, Q05, Q07, Q11, Q13, Q14); the v3 candidate it is declared to be "the round-68 v3 candidate's bytes with exactly the deltas above" (`reports/round-69/claims.md` §C1) carried **13** (`round-68…md:172-184`). Silently dropped: **Q03, Q06, Q08 (superseded-by-Q11), Q09, Q10, Q12 (n/a)** — including Q10, the criterion this seat adjudicates, and Q03/Q06/Q09 which were PASS rows with substantive bases. `corpus/QUALITY.md:31` requires "Apply every criterion. A criterion marked `n/a` names why it cannot apply", and no n/a reason for the six appears anywhere in the entry. Row deletion is not among C1's enumerated deltas (items 1-9); the `diff -u` confirms the drop is a byte delta not accounted for. Smallest safe correction: restore the six rows at v4 line references (Q03/Q06/Q09 pass, Q08 "superseded by Q11", Q10 pass on this report's basis, Q12 n/a), or state in `reports/round-69/claims.md` that the map is intentionally narrowed — which would itself be a claims edit, not an entry edit.

**F2 · high · Q04/Q11 (unrepaired from r68).** `:19` universal; falsified by `:130`. Correction: "Every numbered item except item 11 is produced by the readout …; item 11 is produced by `corpus/derive_axml_anchors.py` (§Reproduce)."

**F3 · medium · Q11/Q13 credit boundary.** `:9` (`recheck:`) claims the derivation covers "every S038 line number **and value** this entry cites". Item 6 (`:70`) states "bit `0x100` set, the UTF-8 flag position" — that is S038's `UTF8_FLAG = 1<<8` at `corpus/snapshots/ResourceTypes.h:480`, and `corpus/derive_axml_anchors.py:52-61` (`ENUMS`) does not print it. The 20-line output therefore covers every *line number* (mechanically verified: stated set = derived set = {218,237,239,241,244,245,246,247,248,253,263,287,461,612,621,677,686,687,707}) but not every *value*; `:127` itself avoids the overstatement by bounding to "items 4, 8 and 11" while `:9` does not. This also exposes `reports/round-69/claims.md` §C1 item 1's own wording ("every S038 line number and value the entry states is printed by the derivation") — under the strict reading it is unsatisfied by one value. Correction: add `SORTED_FLAG`/`UTF8_FLAG` to `ENUMS` (20 → 22 output lines) and re-embed, or narrow `:9` to "every S038 line number and every enum value stated in items 4, 8 and 11".

**F4 · high/medium · Q15 (new criterion this round).** `:8` states *"the fixture, oracle and readout bytes are the round-65 claim-tree bytes, unchanged since `c7b7cf98`"* — a git object id plus a byte-identity sentence — and the entry names **no** deriving command (a scan of every 7-40-character hex token in the entry finds `c7b7cf98` as the only commit id; all others are sha256 digests or byte strings). Q15 (`corpus/QUALITY.md:27`) rejects exactly "an identity sentence … asserted without the deriving command". I verified the sentence is **true**, so this is a receipt gap, not a false identity:
```
$ git log --oneline -- corpus/fixtures/apk-r65/
c7b7cf9 round-65: candidates — apk-r65 fixture+readout, C05 candidate entry, S038-S041 rows, C5 forged-evidence controls, lesson+wave spec (no README flip)
$ git diff --stat c7b7cf98..HEAD -- corpus/fixtures/apk-r65/    # 0 lines of output
```
Correction: carry those two read-only commands (or the `git log` line) in `verified-at:`/`recheck:`; a Q15 seat applying the criterion mechanically will otherwise FAIL the v4 bytes, which under `claims.md` §C1's kill rule ("Any Q FAIL on the v4 bytes") falsifies C1.

**F5 · low · Q10-section pointer precision.** `:171` writes "fleet `l0-questions.md:42`"; the fleet root has no `l0-questions.md` (it is `.ufo/l0-questions.md` — `find /home/vgpnk/Projects/shokunin -maxdepth 3 -name 'l0-questions*'`). The r68 entry and `.ufo/reports/round-1/revenger.md:84` both use the prefixed form `.ufo/l0-questions.md:42`. Correction: restore the `.ufo/` prefix.

**F6 · low · Q11 · §Limitations bound asserted without a printed receipt.** `:167` states "The container is ZIP_STORED with no data descriptors". `readout.py:99-106` reads name/extra length, `compressed_size`, CRC and the local-header name only — neither the compression-method field (local header +8) nor general-purpose-flag bit 3 (+6) is read or emitted, and `compressed_size == uncompressed_size` is consistent with but not proof of STORED. Direct byte read confirms the sentence is true (`method 0`, `gp_flag 0x0` at offsets 0, 465, 618), so this is a missing receipt, not a false statement. Correction: emit `method` and `gp_flag` in the `member[...]` fact (one readout edit, no fixture change).

## Evidence (commands actually run, output as printed)

- Digests vs the entry's pins — all equal: `sha256sum corpus/fixtures/apk-r65/{readout.py,fixture.apk,truth.json,generator.py} corpus/snapshots/ResourceTypes.h corpus/derive_axml_anchors.py` → `92e347c3…`, `05d2280f…`, `27303bae…`, `eaa9444c…`, `56b88bc4…`, `74d4c0d9…` (= `:1`, `:3`, `:6`, `:7`).
- Instruments reproduce at this tree: `python3 -B corpus/derive_axml_anchors.py` → exit 0, **20** lines; `python3 -B corpus/fixtures/apk-r65/readout.py` → exit 0, **15** lines, sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — the pinned `recheck:` value (`:9`, `:194`).
- Anchor completeness: a script extracted every `:NNN` and `line NNN` token from the entry and every `: NNN` from the derivation output; stated set == derived set (19 numbers), `stated not derived: []`.
- Cross-lane: `awk 'NR==42' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` → the tsukuroi ADJ-06 row (kaidoku/revenger shipped-artifact overlap), no resolution text.
- Provider fence: `grep -in 'jadx|prerequisit|inspect_android_package' .ufo/waves/round-65/source-snapshots/rea-android-applications.md` → lines 7, 16-20, 27 (JAR 0.7.1 + Java 17 prerequisites are documented, so `:171` does not overstate S043's row).
- ZIP container bounds: `struct.unpack` of local headers at offsets 0/465/618 → `gp_flag 0x0`, `method 0` for all three members.
- Build state: `grep -n '| C05 ' corpus/README.md` → `:34` still `uncovered` — not flipped, as `:11` claims and `claims.md` §C1 admission order requires.
- Q-map delta: `diff -u` v3→v4 shows the six-row deletion and the Q14 addition (`round-68…md:172-184`, 13 rows → `round-69…md:177-184`, 8 rows).
- Registry: `corpus/SOURCES.md:61` carries S047 (extended derivation, supersedes S046 at `:60`), matching `:6`.

## Residual risk and gaps

- **Tag-content identity is not re-verified.** I proved the committed snapshot equals its pin (sha256 `56b88bc4…`, 86255 bytes) but did not re-fetch `android-15.0.0_r1`; origin is outside Q09's scope and no network was used. Version scoping therefore rests on the pin the entry states (correct posture).
- **Q10 is not a licence to pass F1/F3/F4.** The scope verdict is clean; the entry's admission still turns on the Q03/Q06/Q09/Q11/Q13/Q15 seats, and F3/F4 are mechanical FAILs for two of them if read strictly.
- **Not my assignment, not run:** the frozen counter, the C7 gate, the census, and the lesson/SCORECARD paths.
- No tool was installed or upgraded for this seat. Scratch files under `/tmp/revenger-r69-scope-*` were deleted before returning; `git status --porcelain` shows no `corpus/` change and no `__pycache__` from my runs (both scripts ran with `-B`).
