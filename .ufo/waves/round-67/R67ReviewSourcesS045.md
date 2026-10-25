# R67ReviewSourcesS045 — tier/scope review of the new S045 row

**PASS** — tier A is honest for the declared scope (vendor-published format spec, primary for declared `header_item` field semantics only), the anchor is an exact located span verified in the snapshot bytes, the snapshot sha256/size match, the Gate quote is verbatim and within the ≤25-word bound, and the census enum rules accept the row (validator exit 0).

Seat: reviewer, independent leaf. No installs (tools used: python3, sha256sum, grep, git read-only — all pre-existing). No writes outside this report file.

## Evidence

### 1. Row under review

`corpus/SOURCES.md:59` (read `:raw:59`) — `S045 | DEX format specification (Android Open Source Project) — https://source.android.com/docs/core/runtime/dex-format | docs | A | the declared header_item field semantics (magic, checksum, signature, file_size, header_size, endian_tag) of one authored classes.dex member; not dex program validity and not general dex parsing | "File layout" → header_item field table: … | mined | 2026-10-24 | 180d | corpus/knowledge/round-67-apk-axml-byte-evidence.md`.

### 2. Tier A honesty for the declared scope — PASS

- The scope cell explicitly fences to **declared** `header_item` field semantics of one authored member and **negates** both overreach directions: "not dex program validity and not general dex parsing" (SOURCES.md:59). A vendor format spec is primary for exactly this: what the format *declares* its fields to mean. It would not be primary for validity of real dex programs — the scope excludes that.
- Precedent consistency: sibling vendor-spec rows at tier A for layout/declared scope — S009 (Microsoft PE Format, `.rsrc` field layouts), S011/S019/S020/S044 (Python/Solidity/Node vendor docs). QUALITY.md "Signals of weak material" demotes only "vendor write-ups **without reproducible detail**" to tier C; the AOSP spec carries exact field tables (verified below), i.e. reproducible detail.
- No overreach in the citing entry: item 9 (`corpus/knowledge/round-67-apk-axml-byte-evidence.md:106`) cites S045 only for declared checksum/signature/header_size/endian semantics and ends "These are declared-header self-consistency facts about one inert member; dex validity is not claimed". Corroborated at :129 (Inference — "declared field semantics for this one member"), :130 (Unknown — "dex program validity … is claimed [not]"), :134 (Limitations — "intentionally not a valid dex program"), :152 (Q09 — "inert declared-header property, not validity"). Entry header :3 repeats the same bounded scope.

### 3. Anchor is an exact located span, not a bare homepage — PASS

Anchor = "File layout" → `header_item` field table → named rows with verbatim cell text, plus snapshot path + sha256 + size. All located in the snapshot (tag-stripped rendered text; raw-HTML grep misses are markup splitting, **not** drift — see §4):

- `checksum uint adler32 checksum of the rest of the file (everything but magic and this field); used to detect file corruption` — present, preceded by `…ubyte[8] = DEX_FILE_MAGIC magic value…`, followed by `signature ubyte[20] SHA-1 signature (hash) of the rest of the file (everything but magic, checksum, and this field); used to uniquely identify files` (field widths `ubyte[8]`/`uint`/`ubyte[20]` are in the same table, so the entry's offset-12/offset-32 derivation surfaces are in the anchored span).
- `must be 0x70 (112) bytes (v40 or earlier)` — present (raw grep also 1 hit at byte level).
- `uint ENDIAN_CONSTANT = 0x12345678;` — present (raw grep: `ENDIAN_CONSTANT` 9 hits, `0x12345678` 1 hit).
- `"File layout"` — present (1 hit); `header_item` — 7 hits. Raw-HTML hit counts: `adler32 checksum…` 0, `SHA-1 signature…` 0 — solely because tags split the cells; tag-stripped search hits both verbatim.

This satisfies the Q02 bar ("anchor … not a bare homepage") and matches the located-span precedent (S002 frontmatter, S038 enum lines 237-253, S009 named sections).

### 4. Snapshot sha256 and size — PASS

- `sha256sum .ufo/waves/round-67/source-snapshots/dex-format.html` → `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4`; `wc -c` → `281157`. Both byte-match SOURCES.md:59, the lesson (`corpus/lessons/round-67.md`, `## Gate — source rows opened this round`), and the frozen claim (`reports/round-67/claims.md` C1 item 4).
- Commit state: `git ls-files -- .ufo/waves/round-67/source-snapshots/ corpus/knowledge/round-67-apk-axml-byte-evidence.md` lists both; `git status --porcelain` on snapshot + SOURCES.md + v2 entry is empty (tracked, clean, no uncommitted mutation).

### 5. ≤25-word Gate quote — PASS (quote verbatim; one word-count label nit)

`corpus/lessons/round-67.md` HAS landed (6359 bytes, 21:08 — my first `ls | grep -i round-67` returned nothing in a compound command; re-listed and confirmed present), so the lesson Gate path applies, with the entry-header quotes cross-checked as the brief's fallback:

- Lesson quote: "adler32 checksum of the rest of the file (everything but magic and this field); used to detect file corruption" — **verbatim** in the snapshot's rendered header_item checksum row (see §3 context).
- Length: programmatic `len(q.split())` → **19** words; lesson parenthetical says "(18 words)". The bound is ≤25 and holds either way; the label is off by one. LOW finding, no admission impact (the contract requires the quote + location, both present).
- Entry-header quotes (round-67 entry :3) all verbatim in the snapshot: checksum sentence, signature sentence "SHA-1 signature (hash) of the rest of the file (everything but magic, checksum, and this field)", header_size sentence, `ENDIAN_CONSTANT = 0x12345678`. Entry item 9 (:106) quotes the same four spans verbatim.

### 6. Census enum rules accept the row — PASS

Validator: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh` (enum lines 655-658: kind `^(spec|docs|paper|code|tool|dataset|talk|book|community|own-work)$`, tier `^[ABC]$`, status `^(queued|mined|rejected)$`; E10 = community-at-A only; E11 = used-by path on disk).

- `validate --root /home/vgpnk/Projects/shokunin revenger` → exit 0, `revenger ok`; only warnings are pre-existing W04 URL-scope duplicates (S024/S028/S029/S034 — none is S045). So for S045: kind=docs ∈ enum, tier=A legal (not community), status=mined legal, opened 2026-10-24 valid, recheck `180d` valid cadence, used-by `corpus/knowledge/round-67-apk-axml-byte-evidence.md` exists (E11 clean).
- `census` → `revenger rows 45`, `tier.A 43`, `tier.C 2`, `status.mined 37`, `queued 4`, `rejected 4` — 44 round-start rows + S045 = 45, consistent with claims.md "census exit 0 at round start (44 rows)".
- Search-log note for the S045 opening present at `corpus/SOURCES.md:89` (registered item satisfied).

## Findings by severity

- **LOW (F1):** `corpus/lessons/round-67.md` labels the S045 Gate quote "(18 words)"; the quoted span is 19 words (`python3` count above). Bound ≤25 not threatened; label only. Fix would be a one-token lesson edit, but lessons are append-only and the admission order gives that to the L1 — recorded, not acted on.
- **INFO (F2):** raw-HTML `grep -F` for the two long quotes returns 0 hits (HTML tag splitting inside the table cells). Later seats re-verifying by raw byte grep must strip tags or they will false-report drift. Quote verbatimity holds in rendered text.

## Residual risk and verification gaps

- I verified the snapshot's rendered text contains the anchored spans; I did not re-fetch source.android.com (network fetch authorized for the quarS seats, not needed for byte-consistency review). If the live page changed after 2026-10-24 the sha256 pin still binds this round's evidence — that is the row's stated recheck model (`180d`).
- The S045 row itself is reviewed; whether every *other* Q01–Q13 criterion passes on the v2 entry is the named per-Q seats' surface (my §2 check covers only S045's tier/scope honesty and its citation sites :3, :106, :129, :130, :134, :144, :152).
- Census warnings W04 are pre-existing rows outside this seat's scope; lane still validates exit 0.

Verdict stands: **PASS**.
