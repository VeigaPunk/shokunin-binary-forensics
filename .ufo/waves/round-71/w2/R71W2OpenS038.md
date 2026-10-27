PASS (fresh re-open, W2) — S038 live raw bytes are base64 wire bytes and are NOT line-addressable as served; only the pinned snapshot (now proven byte-identical to the decoded live body) supports the entry's line locators.

Seat: R71W2OpenS038 (scout), wave-2 fresh falsification of attack-inventory item 39. Lane: revenger-shokunin. Date/access: 2026-10-27, ~16:10–16:19 UTC (host `date -u`). Read-only; no source edits, no votes written (not a Q01–Q16 reviewer seat).

## Commands and output

```
$ date -u
2026-10-27T16:10:40Z

$ curl -sS -D - -o s038-page.body \
  "https://android.googlesource.com/platform/frameworks/base/+/refs/tags/android-15.0.0_r1/libs/androidfw/include/androidfw/ResourceTypes.h"
HTTP/2 200 · content-type: text/html; charset=utf-8 · content-length: 874785
(Gitiles rendered page; 2366 FileContents-lineContents rows; footer offers "?format=TEXT" as the "txt" format link)

$ curl -sS -D - -o s038-text.b64 \
  ".../ResourceTypes.h?format=TEXT"
HTTP/2 200 · content-type: text/plain; charset=utf-8 · content-disposition: attachment
115008 bytes, body begins "LyoKICogQ29weXJpZ2h0..." — base64, not raw source

$ base64 -d s038-text.b64 > s038-live.h
$ wc -c s038-live.h; sha256sum s038-live.h corpus/snapshots/ResourceTypes.h
86255 s038-live.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  s038-live.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
$ diff -q s038-live.h corpus/snapshots/ResourceTypes.h
BYTE-IDENTICAL

$ grep -n "attributeStart\|RES_XML_START_NAMESPACE_TYPE" s038-live.h
245:    RES_XML_START_NAMESPACE_TYPE      = 0x0100,
687:    uint16_t attributeStart;
736:        START_NAMESPACE = RES_XML_START_NAMESPACE_TYPE,
   (comment :686 = "// Byte offset from the start of this structure where the attributes start.")
```

## Findings

1. **Raw live bytes are not line-addressable.** The registered URL serves two live forms: (a) the default response is HTML (`text/html`, 874,785 bytes) whose markup carries per-line `<td id="N">` anchors — line-addressable only as rendered HTML, not as raw source bytes; (b) the raw-bytes form, `?format=TEXT` (the page's own "txt" format link), returns `text/plain` + `content-disposition: attachment` whose 115,008-byte body is a single base64 blob — no line structure on the wire. The W1 report's "base64-encoded body" observation is confirmed; a plain-text reader of the registered URL cannot line-address the response.

2. **Decoded live body is byte-identical to the pinned snapshot.** `?format=TEXT` decoded = 86,255 bytes, sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`, matching `corpus/snapshots/ResourceTypes.h` (the S038 registry digest at `corpus/SOURCES.md:52`). W1's "exact live-vs-snapshot identity is unresolved" limitation is now closed for the decoded content — the snapshot bytes are current as of 2026-10-27.

3. **Line locators resolve identically on both copies.** In the decoded live bytes: line 245 `RES_XML_START_NAMESPACE_TYPE = 0x0100` (matches the S047-derived `enum RES_XML_START_NAMESPACE_TYPE : 245` cited by the v6 entry's item 11); line 686 comment + line 687 `uint16_t attributeStart;` (matches `comment attributeStart : 686` / `field attributeStart : 687` in the same output). The HTML view's `id="245"`/`id="686"`/`id="687"` anchors agree.

4. **Verbatim ≤25-word quote** (decoded live bytes, line 686, 15 words): "Byte offset from the start of this structure where the attributes start."

5. **Answer to the scoped question:** the raw live bytes served for S038 are not line-addressable (base64 blob for the raw form; HTML anchors for the default view are markup ids, not source lines). The line-number locators in the registry row and the v6 entry are supported by the pinned snapshot; because the decoded live body is now verified byte-identical to that snapshot, the locators transfer to today's live content.

## Evidence limits

- Byte-identity was established against `?format=TEXT` decoded output, not against the default HTML page's embedded text; the HTML was verified only for line-anchor presence (`id="245"` etc.), not diffed to source.
- Currency is a point-in-time fetch (2026-10-27); the pinned tag `android-15.0.0_r1` could move upstream, and later mutation would not be caught by this report.
- No claim is made about the reader transport used in W1; both live fetches here used `curl` over HTTP/2 200.
- No census, counter run, fixture regeneration, or Q01–Q16 scoring was performed by this seat; no tools were installed; no pacman transaction run. Scratch `/fast/scratch/hyaku/revenger-r71/R71W2OpenS038/` deleted after copying evidence lines above.
