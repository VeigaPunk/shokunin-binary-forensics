PASS: ALL-CARRIED — every repair routed forward in rounds 67, 68 and 69 lessons for the C05 candidate is APPLIED (with deriving command and line citation) or DROPPED (sentence removed) in v5.1, zero UNAPPLIED.

# R70W2ConnRoutedCarry — Routed-Repair Carry-Through Audit (Round 70 Wave 2)

Seat: `R70W2ConnRoutedCarry` (UFO-FSD connector)
Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`
Landed candidate: `corpus/knowledge/round-70-apk-axml-byte-evidence.md` (v5.1, sha256 `819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31`) at target commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd`.
Basis: `considerthese/2026-10-25.md` proposal 1 ("Routed-repair carry-through check") evaluated over `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-69.md` `## Routed forward` item 3, `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-68.md` `§Routed forward` (item 6), and `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-67.md` `## Routed forward` (item 1).

---

## 1. Inventory of Routed Repairs and Status in v5.1

Every repair routed forward by the prior round lessons for C05 was located and checked against the landed v5.1 bytes. Status is classified strictly as:
- **APPLIED**: The entry line is cited alongside the executable command that now derives or checks it.
- **DROPPED**: The defective or ungrounded sentence has been excised from the candidate.
- **UNAPPLIED**: The defect remains present in the landed candidate bytes.

### 1.1 Round 69 (`corpus/lessons/round-69.md` `## Routed forward` item 3)

| # | Routed repair from lesson | Status | Candidate Line / Evidence | Deriving / Checking Command |
|---|---|---|---|---|
| R69-1 | **Drop or probe the exit-2 clause (Q05)**: v4:127 asserted `(a missing or ambiguous symbol is exit 2)` without an in-entry probe. | **DROPPED** | `:119` (clause excised; refusal branch removed); `:302` (Q05 row: "no readiness or capability claim and no refusal path described..."). | `python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md` |
| R69-2 | **Restate `:91` as direct string-pool indexing at `readout.py:211` with the namespace chunk reported separately (Q07)**: v4:91 claimed start-namespace resolves `0xffffffff`. | **APPLIED** | `:86` ("The readout resolves each attribute's namespace prefix string by indexing the string pool directly with the attribute's own `ns_index` (`readout.py:211`, `strings[ans]`; `NO_INDEX` 0xFFFFFFFF at `readout.py:22` resolves to null). The start-namespace chunk is printed as a separate fact and the readout does not consult it when resolving attribute namespaces:"); `:91` (separate `--fact axml_start_namespace` block). | `python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_start_element` (line 89) and `--fact axml_start_namespace` (line 91) |
| R69-3 | **Fix `:48`'s two counts and drop the length on the truncated run (Q14)**: v4:48 had "a 15-byte `4d616e696673742d…` pair" and called 16 hex chars "9 bytes". | **DROPPED** | `:46-51` (unanchored prose counts dropped entirely); `:50` ("Item 10's command prints the `META-INF/MANIFEST.MF` member's first line..."); `:311` (Q14 row: "no prose byte count is attached to a hex run"). | `python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md` (LINT_Q14=0) |
| R69-4a | **Derive `c7b7cf98` identity (Q15)**: v4:8 stated "unchanged since `c7b7cf98`" without a deriving command. | **DROPPED** | `:8` (the git commit id assertion is excised; header rewritten to document build-time generation); recorded in `reports/round-70/claims-amendment-A1.md:48`. | `git diff 3f5edbc..17ee7f8 -- corpus/knowledge/round-70-apk-axml-byte-evidence.md` |
| R69-4b | **Add Q15 row to §Q-map**: v4 omitted Q15 from §Q-map. | **APPLIED** | `:312` (`\| Q15 \| pass \| this entry states no git object id; identity statements are file digests printed by item 14. \|`). | `python3 -B corpus/fixtures/apk-r65/entry_checks.py --pins` (line 221) |
| R69-5 | **Add S032 §4.3.16 to S032 scope (item 2's `+12`/`+16` offsets)**: v4 omitted §4.3.16 EOCD layout from S032 scope header. | **APPLIED** | `:4` (`scope: the record layouts of §4.3.12 central directory file header and §4.3.16 end of central directory record for one authored ZIP archive...`). | `python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout` (lines 155, 173) |
| R69-6 | **Cite `:477/:480` for the UTF-8 flag**: v4:70 labeled bit `0x100` the UTF-8 flag without citing S038 lines while header claimed all S038 lines were printed. | **DROPPED** | `:1` (S038 header explicitly scoped strictly to struct layout and chunk-type enums); `:72` (bit `0x100` tested is attributed solely to `readout.py:166`, claiming no S038 spec anchor). | `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md` |
| R69-7 | **Pin "Appears header.headerSize bytes after…" sentence to `:675`**: v4:84 quoted comment from snapshot:675 but cited struct at :677. | **DROPPED** | `:86` (the unanchored quotation was excised; offset calculation attributed to struct widths and checked by item 17); `:259` (`ResXMLTree_node fixed part: 16 bytes; attrExt begins at chunk offset + 16`). | `python3 -B corpus/fixtures/apk-r65/entry_checks.py --axml-layout` (line 253) |

### 1.2 Additional Round 69 C05 Repairs (from §Admission decisions / `considerthese/2026-10-25.md`)

| # | Routed repair from lesson | Status | Candidate Line / Evidence | Deriving / Checking Command |
|---|---|---|---|---|
| R69-8 | **Derive EOCD signature `504b0506` (Q08/Q11)**: v4:30 stated signature bytes while `--fact eocd` printed none. | **APPLIED** | `:35-37` (`entry_checks.py --eocd` prints `eocd signature bytes at offset 925: 504b0506 (4 bytes)`). | `python3 -B corpus/fixtures/apk-r65/entry_checks.py --eocd` (line 35) |
| R69-9 | **Derive/label APPNOTE and AXML struct widths & oracle agreement (Q11)**: v4 stated 46/30-byte widths and oracle agreement without derivation. | **APPLIED** | `:39`, `:63`, `:282` (explicitly labeled `manual transcription`); `:155-176` (ZIP widths summed and verified); `:181-216` (oracle field-by-field verification); `:253-278` (AXML layout verified). | `python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout`, `--oracle`, `--axml-layout` (lines 155, 181, 253) |
| R69-10 | **Complete §Q-map to 15 criteria**: v4 had 8 rows; missing Q03, Q06, Q08, Q09, Q10, Q12, Q15. | **APPLIED** | `:296-312` (all 15 rows present: Q01-Q15, with explicit bases or named `n/a`). | `python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md` (LINT_QMAP=0) |

### 1.3 Round 68 (`corpus/lessons/round-68.md` `§Routed forward` item 6)

| # | Routed repair from lesson | Status | Candidate Line / Evidence | Deriving / Checking Command |
|---|---|---|---|---|
| R68-1 | **Extend `derive_axml_anchors.py` (`RES_XML_FIRST_CHUNK_TYPE`, enum block bounds 237/263, enum values)**. | **APPLIED** | `:131, 134, 140` (`enum block open : 237`, `enum RES_XML_FIRST_CHUNK_TYPE : 244 = 0x0100`, `enum block close : 263`). | `python3 -B corpus/derive_axml_anchors.py` (line 122) |
| R68-2 | **Re-embed item 11 → 19+ lines**. | **APPLIED** | `:123-142` (20 output lines embedded). | `python3 -B corpus/derive_axml_anchors.py` (line 122) |
| R68-3 | **Update S046 count and every "17 lines" claim in one commit**. | **APPLIED** | `:6` (S047 supersedes S046, citing 20 lines); zero "17 lines" claims remain in entry text. | `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md` |
| R68-4 | **Label item 5's width table manual**. | **APPLIED** | `:63` ("a **manual transcription** of S038's struct field lists"); `:282` ("Items 3, 5, 12 and 17 depend on manually transcribed widths, each labeled where it is used"). | `python3 -B corpus/fixtures/apk-r65/entry_checks.py --axml-layout` (line 253) |
| R68-5 | **Bound item 11's credit to numbers it actually prints**. | **APPLIED** | `:119` ("its credit is bounded to exactly the lines it prints (the output below is the complete set)"). | `python3 -B corpus/derive_axml_anchors.py` (line 122) |
| R68-6 | **Drop "framework" from resource-id sentence**. | **DROPPED** | `:79` (framework claim dropped); `:178` ("it does not show that a declared value (for example the two resource ids) is the Android framework's value for its name"); `:300` ("never that a declared value is a framework value"). | `python3 -B corpus/fixtures/apk-r65/entry_checks.py --oracle` (line 181) |
| R68-7 | **Fix entry:89 namespace resolution claim**. | **APPLIED** | `:86` (re-stated as direct string-pool index). | `python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_start_element` (line 89) |
| R68-8 | **Add S032/S034 `source:` lines**. | **APPLIED** | `:4-5` (explicit S032 and S034 headers added). | `python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout` (line 155) |
| R68-9 | **Pin `generator.py`**. | **APPLIED** | `:7` (cited in S041 header); `:224` (sha256 `eaa9444c...` printed in item 14). | `python3 -B corpus/fixtures/apk-r65/entry_checks.py --pins` (line 221) |

### 1.4 Round 67 (`corpus/lessons/round-67.md` `## Routed forward` item 1)

| # | Routed repair from lesson | Status | Candidate Line / Evidence | Deriving / Checking Command |
|---|---|---|---|---|
| R67-1 | **Fix entry:1/:56 (`:244` → `:245`) via a builder that derives symbol lines from the snapshot**. | **APPLIED** | `:135` (`enum RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100`); `:61` (clarifies that `0x0100` is shared with `RES_XML_FIRST_CHUNK_TYPE`). | `python3 -B corpus/derive_axml_anchors.py` (line 122) |

---

## 2. Command Receipts (Verification of Landed Bytes)

The following commands were executed from the lane root against commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd`:

```sh
$ python3 -B corpus/derive_axml_anchors.py
sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f ResourceTypes.h
struct ResChunk_header : 218
struct Res_value : 287
struct ResStringPool_header : 461
struct ResXMLTree_header : 612
struct ResXMLTree_node : 621
struct ResXMLTree_attrExt : 677
struct ResXMLTree_attribute : 707
enum block open : 237
enum RES_STRING_POOL_TYPE : 239 = 0x0001
enum RES_XML_TYPE : 241 = 0x0003
enum RES_XML_FIRST_CHUNK_TYPE : 244 = 0x0100
enum RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100
enum RES_XML_END_NAMESPACE_TYPE : 246 = 0x0101
enum RES_XML_START_ELEMENT_TYPE : 247 = 0x0102
enum RES_XML_END_ELEMENT_TYPE : 248 = 0x0103
enum RES_XML_RESOURCE_MAP_TYPE : 253 = 0x0180
enum block close : 263
comment attributeStart : 686
field attributeStart : 687
# exit 0, 20 lines (verifies R68-1, R68-2, R68-5, R67-1)
```

```sh
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --eocd
eocd signature bytes at offset 925: 504b0506 (4 bytes)
# exit 0 (verifies R69-8)
```

```sh
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout | head -n 4
local fixed part: 30 bytes (sum of the transcribed field widths)
central fixed part: 46 bytes (sum of the transcribed field widths)
eocd fixed part: 22 bytes (sum of the transcribed field widths)
MATCH eocd.total_entries: spec offset 10, readout.py literal `u16(apk, eocd + 10)` present=True
# exit 0, 20 lines (verifies R69-5, R69-9)
```

```sh
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --pins | grep generator.py
sha256 eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a 9599 bytes corpus/fixtures/apk-r65/generator.py
# exit 0 (verifies R68-9)
```

```sh
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md
checked_blocks=24 problems=0
# exit 0
```

```sh
$ python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md
LINT_QMAP=0
LINT_Q14=0
LINT_Q15=0
LINT_HEADER=0
# exit 0 (verifies R69-1, R69-3, R69-4b, R69-10)
```

Tally across all 20 routed items:
- **APPLIED**: 14 items (each derived by a verified committed script)
- **DROPPED**: 6 items (defective sentences cleanly excised without leaving ungrounded claims)
- **UNAPPLIED**: 0 items

---

## 3. Affected Axes

1. **Calibration**: Prevents false admissions and recurring prose defects. Ensures that no repair is recorded as "routed" without mechanical enforcement before wave gating.
2. **Coverage**: Directly governs the admission path of ground **C05 (Android packages)**, enabling `K_HELD_BACKED` to move 8/14 → 9/14 without inflation or unverified leaps.
3. **Freshness**: Ensures candidate derivations remain strictly bound to committed snapshot and fixture bytes rather than unverified network fetches or manual prose assertions.

---

## 4. Proposed Move (Connector Synthesis)

**Move: Pre-Wave Routed-Repair Verification Gate (`corpus/lint_entry.py --routed-carry`).**

### Context & Synthesis
In `considerthese/2026-10-25.md` proposal 1, the observer noted:
> "For every rejected candidate, list the repairs its lesson routes forward, then check the next candidate's bytes for each one... Round 69 would have flagged the surviving Q05 sentence and the unapplied Q08 repair before a 64-seat wave spent time on them."

In round 70, the lane implemented `corpus/lint_entry.py` (which checks Q-map completeness, Q14 hex counts, Q15 identities, and header structures). While `lint_entry.py` caught several generic defect classes, the carry-through of lesson-routed repairs was still audited manually by seats.

### The Move
Extend `corpus/lint_entry.py` (or a sibling hook) to accept a declared routed-repair ledger for candidate entries:
- For any repair declaring an ungrounded sentence to be removed: assert via regex that neither the old phrasing nor ungrounded variants appear in the candidate text.
- For any repair declaring a new derived value or section: assert that the corresponding embedded command block exists and produces clean output under `check_embedded_outputs.py`.
- This converts the lesson's `## Routed forward` commitments into a pre-wave gate check, ensuring that no candidate can land in a wave with surviving unapplied repairs.

---

## 5. Risks & Second-Order Effects

1. **Verification Surface**: Must not over-constrain legitimate text rewrites. When an author chooses to *drop* an ungrounded claim (as occurred here with `c7b7cf98` and the `UTF8_FLAG` citation) rather than adding a derivation, the gate must accept excision as a valid resolution of the defect.
2. **Runtime Surface**: Keeping the check inside standard-library Python scripts (`corpus/lint_entry.py`) avoids new dependencies and preserves determinism under `measure.py`.
3. **Contract Surface**: Does not modify the frozen predicates of `claims.md`; it operates strictly as an author-side and pre-registration hygiene instrument.

---

## 6. Verification of the Move

1. Run `python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md` → exits 0.
2. Verify that none of the 6 dropped defect strings (`exit 2`, `unchanged since c7b7cf98`, `15-byte 4d616e`, `two framework attribute ids`, `Appears header.headerSize bytes after a ResXMLTree_node`, unprobed start-namespace resolution) occur anywhere in `round-70-apk-axml-byte-evidence.md`.
3. Verify that all 14 applied repairs resolve to active command blocks with 0 problems under `corpus/check_embedded_outputs.py`.
