ROW-DEFECT — S046 is a legal 11-column row with a verified tier-A anchor, but its `mined` status is paired with `used-by: —` (fleet census W03 "S046 mined but unused", a repeat of round-67 routed defect D4) and the row is detached from the registry table by a blank line at `corpus/SOURCES.md:60`.

Scope of this seat: the S046 row at `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md:61` against the contract in that file's header (`:3-6`, `:9-35`) and the frozen fleet contract `/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` (`## Shape`, `## Rules`). Nothing edited. No tool installed or upgraded.

## Exact cell text (field-by-field, verbatim)

Split with `awk -F'|' 'NR==61{...}' corpus/SOURCES.md` → `NF=13` (11 columns + 2 outer pipes):

- id = `S046`
- source = `` AXML anchor derivation — `corpus/derive_axml_anchors.py` over `corpus/snapshots/ResourceTypes.h` ``
- kind = `own-work`
- tier = `A`
- scope = `` the machine derivation of every AOSP `ResourceTypes.h` line number the round-68 C05 candidate cites; the layout facts themselves rest on S038 ``
- anchor = `` script sha256 `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249`, 17 output lines; snapshot copy sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f` (86255 bytes, byte-exact copy of the S038 snapshot `.ufo/waves/round-65/source-snapshots/ResourceTypes.h`); located quote: `enum RES_XML_START_NAMESPACE_TYPE : 245` ``
- teaches = `` Turns the transcribed spec line numbers into a re-derivable command: every anchor is searched in the pinned bytes and a missing or ambiguous symbol is exit 2 — the capture for the M40/M44 anchor class ``
- status = `mined`
- opened = `2026-10-24`
- recheck = `on-release`
- used-by = `—`

## Per-field verdicts

| field | verdict | evidence |
|---|---|---|
| 11 columns | PASS | `awk -F'|' ... NF!=13` → `0` malformed rows; 46 registry rows total. |
| no literal/escaped `|` in any cell | PASS | `awk 'NR==61' corpus/SOURCES.md | grep -c '\\|'` → `0`; exactly 12 raw pipes = 11 cells; backtick count 14 (even). |
| id legal, unique, next-unused | PASS | `sort | uniq -d` over ids → empty; S046 follows S045 (S001–S046, 46 rows). Known cross-package collision with shokuknow's staged S046 space is disclosed at `corpus/SOURCES.md:99`; in-file uniqueness holds. |
| kind ∈ enum | PASS | `own-work` is in the contract enum. |
| tier A justified for an own-work row | PASS | Contract A includes "the lane's own re-runnable gate output". Re-ran it: `python3 -B corpus/derive_axml_anchors.py` → exit 0, `wc -l` = **17** (matches the anchor's "17 output lines"), first line pins `sha256 56b88bc4…c56f ResourceTypes.h`. Script is 102 lines, imports only `hashlib, sys, pathlib`, no `open(`/write/network/subprocess call; it refuses to print a line number it did not find (`fail()` → `sys.exit(2)`, exercised read-only: absent → `SystemExit code 2`, ambiguous → `SystemExit code 2`). |
| scope stated | PASS with LOW caveat | Scope is narrow and explicitly defers the layout facts to S038. Caveat under F3. |
| anchor locatable | PASS with LOW note | Both named files exist and hash exactly as stated: `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249  corpus/derive_axml_anchors.py`; `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h` == `…  .ufo/waves/round-65/source-snapshots/ResourceTypes.h`; both 86255 bytes. Note under F4. |
| teaches | PASS | One learner benefit; the exit-2 mechanism it names is the mechanism the script actually implements (verified above). |
| status token | FAIL (semantic) | `mined` is written "cited by ≥1 path in `used-by`" (`SOURCES.md:26`); the cell is `—`, and the citing entry exists (`corpus/knowledge/round-68-apk-axml-byte-evidence.md:4` `source: S046 — …`). F1. |
| used-by legal | FAIL (semantic) | `—` is a legal token but false for this row. F1. |
| opened legal / honest | PASS | ISO date `2026-10-24`, matches the search-log note `corpus/SOURCES.md:99` ("2026-10-24, round-68 AXML anchor derivation (S046)") and both artifact mtimes (2026-10-24). |
| recheck legal | PASS | `on-release` is a contract cadence and is consistent with S038 (the upstream it derives from), whose recheck cell is also `on-release`. |
| row shape (one registry table) | FAIL (structural) | Blank line at `:60` splits the table. F2. |

## Findings

### F1 — HIGH: `status: mined` with `used-by: —` (repeat of round-67 D4)

Evidence, three independent pointers:

1. Contract definition: `corpus/SOURCES.md:26` — "`mined` (cited by ≥1 path in `used-by`)".
2. Fleet census, run as the contract prescribes (`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`, exit 0):
   ```
   revenger	W03	S046 mined but unused
   revenger	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
   ```
   (the four `W04` duplicate-URL warnings on S024/S028/S029/S034 are pre-existing and disclosed in round-67's Gate.)
3. Lane precedent, one round old: `corpus/lessons/round-67.md:79` — "Status mined; used-by `corpus/knowledge/round-67-apk-axml-byte-evidence.md`." That row was opened by the same author pattern and pointed at the *then-candidate* entry; the entry is now `admission-status: rejected` (`corpus/knowledge/round-67-apk-axml-byte-evidence.md:8`) and the pointer is still correct. Same shape at S041 (`used-by: corpus/knowledge/round-65-apk-axml-byte-evidence.md`, that entry also rejected, `:7`). Round 68's `reports/round-68/claims.md:199-200` names "the S045 `used-by` re-point" as routed defect D4 — S046 reproduces the exact class.

Is `—` "honest" about the candidate state? No — it is under-claiming in a way that makes `mined` false, not cautious. `used-by` names entries that cite the row regardless of admission verdict (S041/S045 precedent), so naming the candidate leaks no admission claim and is stable if C2 is falsified this round (the pointer would still be right).

Fixes I would make (both are append-only-legal — `status`/`recheck`/`used-by` are the only mutable cells, `SOURCES.md:5-6`):
- **Primary:** set used-by to `corpus/knowledge/round-68-apk-axml-byte-evidence.md`, keep `mined`, and log old→new (`—` → that path) in the round-68 lesson Gate per rule 2.
- **Alternative (not recommended):** change status to `queued` and keep `—`, then re-point at admission. Rejected because it contradicts the S041/S045 precedent, would trip no census warning but would leave "cited by a committed entry" invisible, and needs a second in-place edit later.

### F2 — MEDIUM: the row is not in the registry table

`git diff HEAD~1..HEAD -- corpus/SOURCES.md` shows the added row surrounded by blank lines:
```
+| S046 | AXML anchor derivation — … | … | mined | 2026-10-24 | on-release | — |
+
```
`corpus/SOURCES.md:60` is an empty line between S045 (`:59`) and S046 (`:61`); blank lines inside the registry body occur only at `:12` (before the header) and `:60`. A deterministic pipe-table splitter over the `## Registry` slice reports `distinct pipe-tables: 2` — the real table (`:13`–`:59`, header + separator + 45 rows) and a detached one-row table (`:61`, S046 only). The contract's shape is "`## Registry` — the one table below" (`SOURCES-CONTRACT-v1.md` `## Shape`), so as rendered S046 is a header-less orphan row. The census regex tolerates it (hence `revenger ok`), so this will not be caught by any existing check.

Fix: delete the blank line at `:60`. No cell changes; no append-only violation (this is the row's own layout).

### F3 — LOW: scope over-broad on one cited line number

Scope says "every AOSP `ResourceTypes.h` line number the round-68 C05 candidate cites". The derivation emits 16 line numbers (7 structs: 218, 287, 461, 612, 621, 677, 707; 7 enum members: 239, 241, 245, 246, 247, 248, 253; comment 686; field 687) plus the sha256 line = 17 output lines. The entry cites one more line number that the script never derives: the block range `lines 237-253` (`corpus/knowledge/round-68-apk-axml-byte-evidence.md:57,148,157`), whose start `:237` is `enum {` (`sed -n '237p' corpus/snapshots/ResourceTypes.h`), not a derived symbol. Every load-bearing anchor is derived; only the range boundary is not.

Fix (cheap, no gate impact): reword scope to "every cited struct and enum-member line number". Fix (exact, higher cost): derive the `enum {` block start too — that changes 17 → 18 output lines and therefore the row's anchor count *and* the entry's `recheck:`/item-11 counts, so it must be done as one edit before the gate captures stdout.

### F4 — LOW/note: the "located quote" is derivation output, not snapshot bytes

`grep -cF "enum RES_XML_START_NAMESPACE_TYPE : 245" corpus/snapshots/ResourceTypes.h` → `0`; against the script's stdout → `1`. The byte line at `:245` is `    RES_XML_START_NAMESPACE_TYPE      = 0x0100,`. For an own-work row this is defensible (the source *is* the script, and `:` is its own output separator), and the row never presents the string as source bytes. Suggest labelling it `derivation output:` or quoting the `:245` byte line verbatim, so a later reviewer re-opening the snapshot cannot mistake the form for a source quote (the M40/M44 class this row captures is exactly that confusion).

### F5 — OBLIGATION, not yet a defect: rule 1 Gate record absent

Rule 1 (`SOURCES-CONTRACT-v1.md` `## Rules`) requires the round lesson's `## Gate` to record, for every new row, the URL/command, the access date and a ≤25-word quote with its location. `corpus/lessons/round-68.md` does not exist yet (`ls corpus/lessons/` stops at `round-67*.md`), so this row's rule-1 grounding is outstanding. It must land at round close, together with the F1 old→new log and the rows-45 → 46 census (round-67's equivalent is `corpus/lessons/round-67.md:79-82`). The row's own quote is 4 tokens, well inside the ≤25-word bound — that is not the round-67 D3 failure mode.

## Residual risk / verification gaps

- Rendering was checked with a deterministic pipe-table splitter, not a real GFM renderer; the claim is exactly "two contiguous pipe blocks in the `## Registry` slice", which that splitter proves.
- Other rows' `used-by` staleness is out of this seat's scope; I only used S038/S041/S045 as precedent and observed that S038/S045 do not list the round-68 entry although it cites them (consistent with "pointer = opening/mining entry", which supports F1's primary fix).
- The script's digest-mismatch branch (`snapshot digest … != pinned`) was read, not executed; the matching branch ran on every invocation. I did not fault-inject into `corpus/snapshots/` (read-only claim surface).
- The entry's substantive byte claims (items 1–13, readout 15-line digest, anchors at `:57/:134/:148`) were sampled for line-number membership (`:134 struct ResXMLTree_node : 621`, `:148 line 244 is RES_XML_FIRST_CHUNK_TYPE` → snapshot `:244` = `RES_XML_FIRST_CHUNK_TYPE      = 0x0100,` ✓) and are otherwise other seats' scope.
