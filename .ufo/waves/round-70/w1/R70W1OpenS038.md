# R70W1OpenS038 — S038 re-open + C05 items 11–12 quote location (freshness / coverage)

**VERDICT: OPENED-QUOTE-PRESENT** — live AOSP `ResourceTypes.h` at tag `android-15.0.0_r1` is byte-identical to the lane snapshot and the C05 item-11 quote is located at live line 686; 4 advisory findings (F1 APPNOTE cited line ranges under-cover transcribed fields; F2 REA row path 404s at the tag; F3 S038 registry anchor range excludes :253 used by the candidate; F4 live dex-format.html differs in 2 non-quote lines). Target reviewed: frozen candidate `aa1842fac199aa524930e5565ed3715de5f84c6d`.

## Method / evidence (commands)

```
$ curl -sSL 'https://android.googlesource.com/platform/frameworks/base/+/refs/tags/android-15.0.0_r1/libs/androidfw/include/androidfw/ResourceTypes.h?format=TEXT'   # base64 transport
$ base64 -d ... > live-ResourceTypes.dec.h
$ sha256sum live-ResourceTypes.dec.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  86255 bytes
$ sha256sum /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/snapshots/ResourceTypes.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  86255 bytes
$ cmp live-ResourceTypes.dec.h corpus/snapshots/ResourceTypes.h && echo IDENTICAL
IDENTICAL
```

Tag resolution: `refs/tags/android-15.0.0_r1` → commit `4e43ad12e1b211f15152e9c5b16b0fe88e6b93f3`; blob at that commit decoded sha256 `56b88bc4…` (same). Fetch time 2026-10-25T21:12:10Z (also re-fetched 21:32:30Z, same).

Plain URL (as written in the registry row, without `?format=TEXT`) serves an HTML page (874785 bytes, sha256 `8daf5ec3…`); the quote is still locatable there at HTML id=686 (file line 686). The snapshot bytes require `?format=TEXT` + base64 decode (as recorded in `corpus/lessons/round-65.md:12`).

**All four lane snapshots compared to live (2026-10-25):**

| snapshot | live sha256 (2026-10-25) | vs lane |
|---|---|---|
| `corpus/snapshots/ResourceTypes.h` (S038) | `56b88bc4…` 86255 B | BYTE-IDENTICAL |
| `corpus/snapshots/APPNOTE.TXT` (S032/S034) | `0b993022…` 174585 B | BYTE-IDENTICAL |
| `corpus/snapshots/rea-android-applications.md` (S043) | `412d9cb4…` 1992 B | BYTE-IDENTICAL (via npm tarball member and via repo path `.agents/skills/…`) |
| `corpus/snapshots/dex-format.html` (S045) | `12937cb8…` 281161 B | DIFFERS at lines 8946 & 8951 only (script nonce + JS feature-flag array); all four quoted phrases present at identical line numbers |

## The quote the C05 entry relies on — items 11–12

Item 11 (`--spec-quotes` MATCH lines) at candidate lines 144–149:

- `MATCH ResourceTypes.h: first line 686, folded phrase present=True: Byte offset from the start of this structure where the attributes start` — verified LIVE: line 686, under `struct ResXMLTree_attrExt` (line 677), field `uint16_t attributeStart;` at 687. PRESENT (12 words ≤ 25).
- `MATCH rea-android-applications.md: first line 7, folded phrase present=True: Start with `inspect_android_package` …` — verified LIVE at lines 7–8 of the REA file (npm tarball member `package/skills/reverse-engineer-anything/references/android-applications.md`; byte-identical).
- Four `MATCH dex-format.html: first line 5949 / 5956 / 5981 / 5035 …` — verified LIVE at identical line numbers (page differs only at 8946/8951).

Item 12 (candidate line 152) claims the APPNOTE layouts are at "snapshot lines 387-398, 511-531 and 632-646". LIVE APPNOTE (byte-identical to snapshot) shows the actual transcribed field lines:

```
   4.3.7 heading = 387; field list = 389–399 (399 = "extra field length 2 bytes" → OUTSIDE 387-398)
   4.3.12 heading = 511; "File header:" at 520; field list = 522–538 (532–538 = name/extra/comment/disk/internal/external/relative-offset → OUTSIDE 511-531)
   4.3.16 heading = 632; field list = 634–646 (within 632–646 ✓)
```

F1 (advisory): the frozen candidate's S032 source line (candidate:4) and item 12 (candidate:152) cite APPNOTE line ranges that do not contain the fields the entry's own transcription uses (`local.extra_length` at 399; `central.name_length/extra_length/comment_length/local_header_offset` at 532–538). The offsets asserted in item 12 (28/30/32/42) are correct, but the cited ranges do not cover them. The registry row S034 itself records the correct local range "snapshot lines 387-399", so the candidate's `387-398` contradicts its own cited row. (The working tree already repairs this by printing heading/field lines; this finding applies to the frozen aa1842f bytes.)

## F2 — REA registry row path does not resolve at the tag

`corpus/SOURCES.md` rows S039/S043 and candidate `source:` line 2 name path `skills/reverse-engineer-anything/references/android-applications.md` at `morluto/rea` tag `rea-agents-6.5.0`.

```
$ curl -sS -o /dev/null -w 'HTTP=%{http_code}\n' 'https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/skills/reverse-engineer-anything/references/android-applications.md'
HTTP=404
$ curl -sS -o /dev/null -w 'HTTP=%{http_code}\n' 'https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/.agents/skills/reverse-engineer-anything/references/android-applications.md'
HTTP=200   # sha256 412d9cb4… == snapshot
# npm member: package/skills/reverse-engineer-anything/references/android-applications.md (sha256 412d9cb4… == snapshot)
```

So the bytes are byte-identical via the repo's real path (`.agents/skills/…`) and the npm tarball member, but the literal path in the rows/candidate 404s at the tag. Advisory (registry/candidate locator repair).

## F3 — S038 registry anchor range excludes :253 the candidate uses

S038 row anchor says "chunk-type enum :239-250"; candidate item 11 prints `RES_XML_RESOURCE_MAP_TYPE : 253 = 0x0180` (used by item 4 for chunk type 384). This is the same class as the round-66 finding; the row is append-only so a correction needs a new/superseding row (S047 currently covers the enum-block derivation with `enum block open : 237` / `close : 263` printed). Advisory only; candidate quotes/derive are all grounded in the pinned bytes.

## F4 — live dex-format.html differs from snapshot

Two independent live fetches (281161 B / 281157 B) differ from the committed snapshot (281157 B, sha256 `c0428612…`) at exactly lines 8946 (`<script nonce=…>`) and 8951 (JS array) — per-request nonce/flags churn, no impact on the four quoted phrases or their line numbers. S045's snapshot is byte-identical to the round-67 snapshot (same digest). Verdict for S045: DIFFERS (boilerplate only), quotes present.

## Gate-block material (CORPUS rule 1)

- URL: https://android.googlesource.com/platform/frameworks/base/+/refs/tags/android-15.0.0_r1/libs/androidfw/include/androidfw/ResourceTypes.h (bytes via `?format=TEXT` + base64)
- Access date: 2026-10-25 (fetch 21:12:10Z; sha256 `56b88bc4…`, 86255 bytes; byte-identical to snapshot)
- ≤25-word located quote: "Byte offset from the start of this structure where the attributes start" (12 words) — ResourceTypes.h line 686, under `struct ResXMLTree_attrExt` (line 677), field `uint16_t attributeStart;` at 687.
- Round-70 lesson file `corpus/lessons/round-70.md` does not exist yet — Gate block is still to be written (dependency noted).

## Checksum / reproducibility notes

- `python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes` on frozen commit bytes → exit 0, all six MATCH lines identical to the candidate's embedded item-11 block.
- `python3 -B corpus/derive_axml_anchors.py` on frozen commit bytes → embedded item-11 derive block matches exactly (EMBEDDED==LIVE: True).
- Item-14 pins match the committed files (ResourceTypes.h `56b88bc4…`, APPNOTE `0b993022…`, dex `c0428612…`, REA `412d9cb4…`).

## Remaining unknowns

- None blocking: all four snapshot sources were re-opened today; S038 quote located; verdict OPENED-QUOTE-PRESENT with F1–F4 advisory findings (wave-1 repairs, not kill-rule inputs).
