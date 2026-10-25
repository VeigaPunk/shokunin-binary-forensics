MATCH — the archive fact is re-derived byte-identically on all four fields, independently confirmed by `sha256sum`/`wc -c` and by the committed tree; one adjacent low-severity prose truncation found in item 3 (not item 1).

# R68 item 1 — independent re-derivation: archive byte count + SHA-256

Seat: `L1Revenger68.R68Item1` (leaf, read-only). Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Subject: `corpus/knowledge/round-68-apk-axml-byte-evidence.md` (C05 v3 candidate, `admission-status: candidate`).
Nothing edited. No tool installs or upgrades were needed (tooling directive: none performed).

## 1. Commands run (actual, from the lane root)

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact archive; echo "EXIT=$?"
{"bytes": 947, "fact": "archive", "path": "corpus/fixtures/apk-r65/fixture.apk", "sha256": "05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e"}
EXIT=0
```

Members (each once, as instructed):

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[AndroidManifest.xml]'   # EXIT=0
{"cd_index": 0, "compressed_size": 416, "crc32": "962d075f", "crc32_matches": true, "crc32_recomputed": "962d075f", "fact": "member[AndroidManifest.xml]", "local_header_offset": 0, "payload_first16_hex": "03000800a001000001001c00c4000000", "payload_offset": 49, "sha256": "73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4", "uncompressed_size": 416}

$ python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[classes.dex]'           # EXIT=0
{"cd_index": 1, "compressed_size": 112, "crc32": "2635c82a", "crc32_matches": true, "crc32_recomputed": "2635c82a", "fact": "member[classes.dex]", "local_header_offset": 465, "payload_first16_hex": "6465780a30333500300c123da5fc7bea", "payload_offset": 506, "sha256": "57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2", "uncompressed_size": 112}

$ python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[META-INF/MANIFEST.MF]'  # EXIT=0
{"cd_index": 2, "compressed_size": 69, "crc32": "e948d738", "crc32_matches": true, "crc32_recomputed": "e948d738", "fact": "member[META-INF/MANIFEST.MF]", "local_header_offset": 618, "payload_first16_hex": "4d616e69666573742d56657273696f6e", "payload_offset": 668, "sha256": "2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49", "uncompressed_size": 69}
```

Independent cross-check that does not trust `readout.py`:

```
$ wc -c corpus/fixtures/apk-r65/fixture.apk
947 corpus/fixtures/apk-r65/fixture.apk
$ sha256sum corpus/fixtures/apk-r65/fixture.apk
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk
$ git cat-file -p HEAD:corpus/fixtures/apk-r65/fixture.apk | sha256sum
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  -
$ git cat-file -p HEAD:corpus/fixtures/apk-r65/fixture.apk | wc -c
947
$ git status --porcelain corpus/fixtures/apk-r65/ corpus/knowledge/round-68-apk-axml-byte-evidence.md   # (no output: clean)
```

The working-tree bytes I read are exactly the committed bytes, so the run is over the claim surface, not a local edit.

## 2. The entry's blocks that claim this fact

- `corpus/knowledge/round-68-apk-axml-byte-evidence.md:25` — the per-item block under observation item 1 (`:21` prose, `:24` command line):

```
{"bytes": 947, "fact": "archive", "path": "corpus/fixtures/apk-r65/fixture.apk", "sha256": "05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e"}
```

- `…:200` — the same line repeated in the §Reproduce full-stdout block (`:194`–`:215`).

Both blocks were compared byte-for-byte, not visually:

```
$ cmp -s /tmp/r68_item1_actual.txt <entry line 25>   -> IDENTICAL to actual stdout
$ cmp -s /tmp/r68_item1_actual.txt <entry line 200>  -> IDENTICAL to actual stdout
$ wc -c                                                159 / 159 / 159   (same length, trailing newline included)
```

## 3. Field-by-field verdict (item 1)

| field | actual stdout | entry:25 / entry:200 | verdict |
|---|---|---|---|
| `bytes` | `947` | `947` | MATCH |
| `fact` | `"archive"` | `"archive"` | MATCH |
| `path` | `"corpus/fixtures/apk-r65/fixture.apk"` | identical string | MATCH |
| `sha256` | `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` | identical string | MATCH |
| key order / separators / spacing | sorted keys, `", "` / `": "` | byte-identical (159 B both) | MATCH |
| exit code | `0` | entry states exit 0 for the readout (`:194`) | MATCH |

**Fields that differ: none.** Verdict for item 1: **MATCH**.

## 4. Prose judgment on item 1 (`:21`)

> `1. The archive is **947 bytes** with SHA-256 `05d2280f…d03e`, read from the file's bytes.`

Every clause is supported by the output:

- "947 bytes" — the `bytes` field (and `wc -c` independently).
- the SHA-256 literal — the `sha256` field, character-exact (and `sha256sum` independently).
- "read from the file's bytes" — a methodological claim about the counter, and it is true of the implementation, not merely plausible: `corpus/fixtures/apk-r65/readout.py:44-46` does `apk = APK.read_bytes()`, then `bytes=len(apk)` and `sha256=hashlib.sha256(apk).hexdigest()`. Nothing is hardcoded, so the value cannot be a transcribed constant. This is exactly the property the entry's `verified-at` (`:6`) asserts and that the M39 drift class violated.

No prose sentence about item 1 states anything the output does not support. Corroborating consistency checks, same fact: `readout.py` sha256 in the entry (`92e347c3…3976`) equals `sha256sum corpus/fixtures/apk-r65/readout.py`; the full-run recheck claim at `:194` also holds — `python3 -B corpus/fixtures/apk-r65/readout.py` → exit 0, 15 stdout lines, stdout sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247`, matching the entry's stated hash.

## 5. Adjacent finding (out of item-1 scope, same entry — actionable)

**F1 (LOW, prose verbatim quote) — `corpus/knowledge/round-68-apk-axml-byte-evidence.md:46`.**

> `The `META-INF/MANIFEST.MF` payload begins `4d616e69666573742d` — ASCII `Manifest-`, the 16-byte prefix of `Manifest-Version: 1.0` …`

Evidence:

```
entry:46 quoted             4d616e69666573742d                    ->  9 bytes -> b'Manifest-'
actual payload_first16_hex  4d616e69666573742d56657273696f6e    -> 16 bytes -> b'Manifest-Version'
r65:41 value                4d616e696673742d56657273696f6e      -> 15 bytes -> b'Manifst-Version'
```

The quoted literal is a 9-byte prefix, but the same sentence calls it "the 16-byte prefix"; the entry's own output block at `:43`/`:205` prints the full 16-byte value `4d616e69666573742d56657273696f6e`. The quote is truncated with no ellipsis, so a reader who lifts `4d616e69666573742d` as "the 16-byte prefix" gets a mismatch against the output — the same hand-truncation failure mode as M39, at lower stakes (prose, not an output block). The two claims about the round-65 draft in the same sentence are accurate: r65 `:41` really does carry `4d616e696673742d56657273696f6e` (dropped `65`, hence 15 bytes), so "15-byte" and the ellipsis-marked r65 quote are correct.

Suggested fix (author's call, not applied): quote the full 32 hex chars at `:46`, or write `4d616e69666573742d…`. This does not touch item 1 and does not change my verdict; flagging it for the Q13/verbatim-quoting seat so it is adjudicated once, not twice.

All three member blocks are otherwise clean — `entry:39`, `entry:41`, `entry:43` compare `exact_equal=True` against fresh stdout at 365/360/367 chars respectively, exit 0 each.

## 6. Residual risk / verification gaps

- The `--fact` invocation was exercised from the lane root only; the absolute-path form was not run. Low risk: the script embeds the repo-relative `path` string as a constant (`readout.py:45`) and reads `fixture.apk` beside itself, so CWD cannot change the printed `path`.
- This seat verified item 1 and the member lines it was asked to capture. It did not re-derive the AXML chunk/string-pool items (items 4-10) or item 11's anchor table; those are other seats' items.
- Semantic (LSP) callers were not consulted: the surfaces here are a JSON-emitting script and Markdown, with no language server answering the lane, so evidence is direct execution plus independent hashing rather than semantic proof — recorded here as instructed rather than presented as stronger than it is.
