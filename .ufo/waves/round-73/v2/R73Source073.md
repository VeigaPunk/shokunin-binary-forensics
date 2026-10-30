# R73Source073 — S073 source audit (round-73 frozen C10 wave, v2)

Seat: R73Source073 (reviewer, leaf; no subagent dispatch). Date: 2026-10-30.
Lane root: /home/vgpnk/Projects/shokunin/revenger-shokunin. Scope: SOURCES.md row S073 only.
Claim context: frozen C10 coverage admission (candidate corpus/knowledge/2026-10-29-rea-evidence-ledger-discipline.md, pin 7880b176…c7c4); this audit is source accuracy for inherited row S073, not a new admission.

## Assigned row (corpus/SOURCES.md line 87, verbatim)

`| S073 | ReAgent — https://github.com/Dryxio/reagent | tool | A | The project's declared C/C++ reconstruction pipeline and its explicit distinction between validation and equivalence proof | README.md "What it does", commit d12cea338c61898b06a86fe8adb25275fa9d5615, accessed 2026-10-27; "This is conservative verification, not a proof of semantic equivalence." | ReAgent describes compile/test/parity checks for reconstructed code but expressly does not treat them as semantic-equivalence proof; no installation, execution or correctness claim is made | mined | 2026-10-27 | on-release | corpus/knowledge/round-72-tool-landscape.md |`

Round-72 lesson row (corpus/lessons/round-72.md line 32): ADMIT, tier A; quote identical to the registry row.
Entry usage (corpus/knowledge/round-72-tool-landscape.md line 30): "ReAgent S073; REA feature spec S077" row — README described as "a reverser/checker, structural checks, candidate build/test gates and parity, while explicitly stating that this is not proof of semantic equivalence."

## Re-open evidence (this seat, 2026-10-30)

- URL reopened: https://raw.githubusercontent.com/Dryxio/reagent/d12cea338c61898b06a86fe8adb25275fa9d5615/README.md → HTTP 200, 20697 bytes.
- Pin check: GitHub API commit d12cea338c61898b06a86fe8adb25275fa9d5615 exists (committer date 2026-09-09T20:39:30Z, message "Document automatic environment adaptation for setup agents").
- Currency check: https://raw.githubusercontent.com/Dryxio/reagent/main/README.md → HTTP 200, byte-identical to the pinned file (cmp clean; sha256 ba66cef64fb57b9ab15e2ff1bee595f8a654059bf79cece400dec01a744e5929 for both). README at pin is still current at HEAD as of 2026-10-30.
- Located quote: line 55 of the pinned README, exact line content `This is conservative verification, not a proof of semantic equivalence.` — verbatim match to the registry row and the lesson row, no markup normalization needed. 10 words (≤25 limit satisfied).
- Anchor: heading `## What it does` at line 28; quote at line 55 falls inside that section, directly after the four numbered success conditions of the reversal pipeline.
- Scope support in README (lines 9–10, 33–45): "reconstruct and validate C/C++ functions from compiled binaries"; pipeline diagram shows "Reverser → checker → fix loop", "Conservative structural verifier", "Candidate overlay / configured build, test, and runtime gates", "Candidate parity gate (GREEN | YELLOW | RED)"; "The tool generates candidate C/C++ implementations; it does not patch the original source tree automatically."

## Comparison against row attributes

| Attribute | Row says | Observed | Result |
|---|---|---|---|
| located quote | "This is conservative verification, not a proof of semantic equivalence." | verbatim at line 55, sole occurrence | PASS |
| anchor | README.md "What it does" | heading `## What it does` line 28, quote inside section | PASS |
| pin | commit d12cea338c61898b06a86fe8adb25275fa9d5615 | exists (API 200), README served at that commit; current main byte-identical | PASS |
| scope / evidence col | declared C/C++ reconstruction pipeline; explicit validation-vs-equivalence distinction | README matches: C/C++ reconstruction, checker/verifier/parity gates, explicit non-proof statement | PASS |
| boundary col | compile/test/parity checks not treated as semantic-equivalence proof; no install/execution/correctness claim | quote and README support exactly this limit; nothing in row overclaims | PASS |
| tier | A (primary project README) | first-party project README at named commit | PASS |
| used-by | corpus/knowledge/round-72-tool-landscape.md | entry line 30 cites "ReAgent S073" with content matching the row | PASS |
| rejection flip | none (row is an admit) | no flip condition applicable | n/a |
| status/recheck | mined / on-release | content unchanged pin→main; on-release recheck policy fits | PASS |

## Located quote returned (≤25 words), access date, URL

- Quote: "This is conservative verification, not a proof of semantic equivalence." (10 words)
- Access date: 2026-10-30 (original lane open 2026-10-27; re-opened by this seat today).
- URL: https://github.com/Dryxio/reagent (README.md), pinned commit d12cea338c61898b06a86fe8adb25275fa9d5615.

## Disposition

AGREE with the round-72 disposition: ADMIT, tier A, for ReAgent's documented reconstruction/check loop and its explicit validation-vs-equivalence limit; not an installation or run claim. The registry row, lesson row, and entry wording are mutually consistent and verbatim-accurate. Unlike S071 (paraphrased registry quote) and S082 (misattributed quote) in round-72-verifier-spotcheck.md, S073 shows no quote defect, so no superseding row is proposed from this seat; S071/S082 supersession belongs to their assigned seats and is out of this seat's scope. No other source admission made.

## Classification

- Observation: quote verbatim at pinned README line 55; pin exists; main==pinned byte-identical; entry line 30 cites S073 as recorded.
- Inference: none required for the verdict; all checks are direct observations. (The lane's 2026-10-27 access cannot be re-observed; today's byte-identical re-fetch is consistent with but does not prove the README was unchanged on 2026-10-27.)
- Unknown: nothing material. ReAgent's actual tool behavior was not tested (correctly out of scope; static source read only).

## Network / source failures

None. Both fetches and the API call returned HTTP 200 on first attempt. No live-target requests; no tool installs or updates this seat (pacman pause honored; nothing installed via any channel).
