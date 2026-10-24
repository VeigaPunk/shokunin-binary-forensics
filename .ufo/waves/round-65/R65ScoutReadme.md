FAIL — every coverage-map name resolves to a real file and the C05 planned filename matches the landed candidate exactly, but two `held` rows name entries whose headers still say `admission-status: candidate` (C06 round-63 zip, C07 round-64 firmware); six pre-contract entries carry no `admission-status:` header at all (a documented convention, not a count-breaker).

Seat: R65ScoutReadme — README-index audit, read-only. Scope: `corpus/README.md` coverage map ↔ `corpus/knowledge/` files and admission markers. All paths absolute under `/home/vgpnk/Projects/shokunin/revenger-shokunin/`.

## A. File-existence audit — PASS (13/13 named files exist, no orphans)

Every `knowledge/…md` token in the coverage-map table (`corpus/README.md:30-43`) resolves:

| row | status | named entry(ies) | on disk | header `admission-status:` |
|---|---|---|---|---|
| C01 | held | `pe-resource-directory-layout.md` | yes (14755 B) | **none** (pre-contract) |
| C02 | partial | `seed.md`, `2026-10-12-rea-readiness-checklist.md` | yes, yes | **none**, **none** (pre-contract) |
| C03 | frontier | — | n/a | n/a |
| C04 | held | `round-62-commonjs-require-name-evidence.md`; retained rejected `commonjs-destructured-require-edges.md` | yes, yes | `admitted` (:6); `rejected` (:5) |
| C05 | frontier | — | n/a | n/a |
| C06 | held | `round-63-zip-central-directory-evidence.md` | yes | **`candidate`** (:8) — mismatch, §C |
| C07 | held | `round-64-firmware-region-byte-evidence.md` | yes | **`candidate`** (:6) — mismatch, §C |
| C08 | frontier | — | n/a | n/a |
| C09 | held | `round-62-evm-dispatch-byte-evidence.md`; retained rejected `evm-saved-interface-candidates.md` | yes, yes | `admitted` (:21); `rejected` (:5) |
| C10 | partial | `seed.md` §Verification discipline | yes | none (pre-contract) |
| C11 | held | `utf16-unpaired-surrogates-in-resource-names.md` | yes | none (pre-contract) |
| C12 | held | `tool-validation-by-function-and-version.md`; `seed.md` §Calibration strategy | yes, yes | none, none (pre-contract) |
| C13 | held | `digest-scope-versus-provenance.md`; `seed.md` §Calibration strategy | yes, yes | none, none (pre-contract) |
| C14 | partial | `2026-10-12-rea-readiness-checklist.md` | yes | none (pre-contract) |

Directory listing `corpus/knowledge/` contains exactly 13 `.md` files; every one is named in the map (no unnamed entries, no missing names). Empty knowledge cells (C03/C05/C08) match their `frontier` status.

## B. C05 filename check — PASS

- Frozen contract names the entry `corpus/knowledge/round-65-apk-axml-byte-evidence.md` (`reports/round-65/claims.md:20`).
- Actual file: `corpus/knowledge/round-65-apk-axml-byte-evidence.md`, 20754 B, sha256 `e173e6436e9b8cce2ddd9f318b914fde6fd9bdfaf18335f5a873ac60fa3cdfb7` — exact filename match, zero divergence.
- Entry header self-identifies the row: `coverage-map: C05 (… Android packages (APK))` (:6) and `admission-status: candidate — … the README C05 status flip is L1's and follows the fresh-seat decisions recorded in corpus/lessons/round-65.md ## Gate` (:7) — consistent with the frozen admission order (`claims.md:112-121`: candidates land **without** the README flip; flip is L1's on all-criteria pass).
- README C05 row is still `| C05 | Android packages (APK) | — | — | frontier |` (`corpus/README.md:34`); no `round-65-` token appears anywhere in `corpus/README.md` — correct un-flipped build state.
- Red-before corroborates: `reports/round-65/measure-before.log` prints `K_HELD=8/14`, `K_ROW C05 status=frontier`, `K_ROW C07 status=held`, `README_TOKEN_LEGEND_MISMATCH=0 rows=[]`.

## C. Status mismatches found (the audit's positive findings)

1. **C06**: README `held` (`corpus/README.md:35`) but `corpus/knowledge/round-63-zip-central-directory-evidence.md:8` reads `admission-status: candidate — drafted in the round-63 build wave for independent Q01–Q13 review; the README C06 status flip is L1's and follows the fresh-seat decisions`. Single occurrence in file; never updated to `admitted` after the round-63 flip landed. `corpus/lessons/round-63.md:188-192` records the planned flip `partial → held` naming this file; `measure-before.log` `K_HELD=8/14` shows the flip did land.
2. **C07**: README `held` (`corpus/README.md:36`) but `corpus/knowledge/round-64-firmware-region-byte-evidence.md:6` reads `admission-status: candidate — drafted in the round-64 build wave …`. Single occurrence. `corpus/lessons/round-64.md:258-266` records the all-criteria Q01–Q13 pass and `README C07 flips frontier → held … naming only this entry` — admission is on record; the header is stale.
3. **Pre-contract header absence (documented, not a defect)**: `seed.md`, `2026-10-12-rea-readiness-checklist.md`, `digest-scope-versus-provenance.md`, `pe-resource-directory-layout.md`, `tool-validation-by-function-and-version.md`, `utf16-unpaired-surrogates-in-resource-names.md` carry `source:`/`verified-at:`/`recheck:`/`coverage-map:` headers but no `admission-status:` line. `corpus/README.md:55-56` names this exactly ("neither entry has been re-gated against QUALITY.md" for the two pre-contract entries; contract-era convention). Their README statuses (held/partial) are by-map-convention, not by in-file marker — flagged so a future strict header audit doesn't double-count.

## D. Counter-relevance of the mismatches (why they don't break the after-state)

`reports/round-65/measure.py:31` counts `held` rows by the trailing `| held |` token only; `:36-37` (K_HELD_BACKED) checks file existence; `:50-53` (K_HELD_BACKED_STRICT) additionally requires the named files not to contain `admission-status: rejected` anywhere (whole-file scan, `:43-46`). The stale `candidate` headers on C06/C07 entries therefore do **not** disturb `K_HELD_BACKED`/`K_HELD_BACKED_STRICT` — the counter is README-token-bound, exactly the gap `corpus/lessons/round-63.md:199-205` documents ("a status-only flip … can print the targets"). Mismatch class: in-file admission marker vs README status, not counter-visible.

Consistency check on the strict scan: retained rejected candidates mark at byte 859 (`commonjs-destructured-require-edges.md`) and 712 (`evm-saved-interface-candidates.md`) — matches `claims.md:61-63` (859/712, before byte 2000), so the whole-file scan change is count-neutral at base. The C05 candidate's `admission-status: candidate` does not contain the `rejected` string, so an admission-time C05 flip stays K_HELD_BACKED_STRICT-backed. Caveat for L1: any edit to the C06/C07 headers (e.g. to `admitted`) is counter-neutral, but inserting the literal string `admission-status: rejected` anywhere in a `held`-named file would un-back its row.

## E. Commands and outputs

- `ls corpus/knowledge/` → 13 `.md` files, list in §A (all named in map).
- `grep admission-status corpus/knowledge/` → hit lines quoted verbatim in §A/§C; six files with zero hits (pre-contract set).
- `grep -bo 'admission-status: rejected' corpus/knowledge/*.md` → `commonjs-destructured-require-edges.md:859`, `evm-saved-interface-candidates.md:712`.
- `grep 'Gate|admit|held|candidate' corpus/lessons/round-63.md, round-64.md` → admission-order and adjudication lines cited in §C.
- `grep 'admission-status|held|K_HELD|rejected|candidate' reports/round-65/measure.py` → counting logic lines 31-53 cited in §D.
- `grep 'K_HELD|K_ROW|README_TOKEN' reports/round-65/measure-before.log` → quoted in §B.

## F. Remaining unknowns / non-goals

- Whether L1 intends to update the C06/C07 entry headers to `admitted` — outside this audit's bounds (entries are seat-read-only).
- The r65 candidate's `admission-status: candidate` is correct by contract at this stage; whether Q01–Q13 fresh seats pass it is other seats' scope.
- No git/jj mutation performed; all findings from working-tree bytes (build state as landed).
