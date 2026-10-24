# W2VerifyFixture — C2 fixture attack

## Result

**Fixture SOUND at committed tip `db55bd6488e24e956df5818ae34c2a043d7ddc12`.** No fixture hole found in the assigned checks. This is a fixture finding, not a C2 provenance judgment, C1 admission, or canonical round decision.

Reviewer: `revenger-r63.W2VerifyFixture` (independent non-author).

Axes: **coverage F / fixture-oracle fidelity (Q06)**, **byte reproducibility**, **non-executable member content**, and **gzip/zlib signature-collision isolation**. No lane source, saved input, registry, index, or configuration was changed. Only this report and round-owned `/tmp` scratch were written.

## Committed-byte boundary and commands

The lane tip was identified with:

```sh
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin rev-parse HEAD
# db55bd6488e24e956df5818ae34c2a043d7ddc12
```

All executed fixture and record checks used this archive, not mutable lane files:

```sh
# S = /tmp/revenger-r63-fixture.JisGn5uw
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive \
  db55bd6488e24e956df5818ae34c2a043d7ddc12 corpus reports/round-63 \
  | tar -x -C /tmp/revenger-r63-fixture.JisGn5uw
```

Python `hashlib.sha256(path.read_bytes()).hexdigest()` on the archived files produced:

| File | SHA-256 |
|---|---|
| `corpus/fixtures/firmware-r63/generator.py` | `4e5d5975e3cf6362f6fd430f2147d42f75d011978f7d6b5ec86d224c77793db4` |
| `corpus/fixtures/firmware-r63/truth.json` | `9663f90b2b9f29c5beb621e554ed7584eedf5e77d4785f26a453e70dbd5a65e6` |
| `corpus/fixtures/firmware-r63/firmware-r63.bin` | `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be` |
| `reports/round-63/measure.py` | `3b7fba2d5243bbe0b723a99a53085130ff97010e23c8a59a8027f5f8992c5908` |
| `reports/round-63/claims.md` | `aed53241c3e4445fab94e854e3185b235ab2ff45c921d6c95e6e60938c7d1e31` |

## Attack 1 — C2 reproducibility

Counterexample sought: the generator overwrites intent-derived truth with a different image, or depends on hidden inputs.

After reviewing the generator, I copied only its committed source to a new scratch directory using `shutil.copyfile`, then ran:

```sh
python3 -B /tmp/revenger-r63-fixture.JisGn5uw/regenerated/generator.py
```

Observed exit `0`, empty stderr:

```text
wrote firmware-r63.bin sha256=bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be size=2048
region offset=0 size=512 kind=padding
region offset=512 size=79 kind=zlib
region offset=591 size=433 kind=padding
region offset=1024 size=90 kind=zlib
region offset=1114 size=934 kind=padding
```

Direct byte comparisons, not just digest comparisons: committed image == regenerated image **True**; committed `truth.json` == regenerated `truth.json` **True**. Python was `3.14.8`; compile/runtime zlib were both `1.3.2`, matching the recorded recipe. Reproducibility is bounded to these recorded versions.

**Impacted axes:** C2 coverage F, reproducibility. **Smallest correction:** none.

## Attack 2 — C2/Q06 oracle independently re-derived

Counterexample sought: declared offsets/sizes omit a member, include padding, overlap, or describe different decompressed bytes. I did not import the generator or call its `derive_regions`/`decode_member` functions. I discovered candidate starts by scanning the whole image, then decoded from each start to the decoder's EOF and measured consumed length from `unused_data`:

```python
# img = committed image bytes; this was executed in the Python tool cell.
zlib_hits = [i for i in range(len(img)-1)
             if (img[i] & 15) == 8 and (img[i] >> 4) <= 7
             and ((img[i] << 8) | img[i+1]) % 31 == 0]
gzip_hits = [i for i in range(len(img)-1)
             if img[i:i+2] == b'\x1f\x8b']
for off in zlib_hits:
    d = zlib.decompressobj()
    payload = d.decompress(img[off:]) + d.flush()
    assert d.eof and not d.unconsumed_tail
    size = len(img) - off - len(d.unused_data)
    compressed = img[off:off+size]
    assert int.from_bytes(compressed[-4:], 'big') == zlib.adler32(payload)
    # Compared offset, consumed size, len(payload), and SHA-256 to truth.json.
```

The zlib predicate covers valid RFC 1950 header pairs across all legal window sizes and flags, not just `78 da`. Results:

| Byte-derived region | Offset | Compressed/padding size | Decompressed size | Decompressed SHA-256 |
|---|---:|---:|---:|---|
| zero padding | 0 | 512 | — | — |
| zlib | 512 | 79 | 78 | `a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86` |
| zero padding | 591 | 433 | — | — |
| zlib | 1024 | 90 | 97 | `2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9` |
| zero padding | 1114 | 934 | — | — |

All five spans match `truth.json`, are contiguous, and cover all 2048 bytes. All 1879 padding bytes are zero. Both stream Adler-32 trailers validate. Decompressed bytes exactly match the two recorded recipe payload strings; recipe size, padding, offsets, Python and zlib versions also match. Member names are authored labels, not properties recoverable from the compressed format.

Compressed-slice SHA-256 values, also derived by `hashlib.sha256`:

- `[512:591]`: `bf3dd2e42d36324ae17e81c66cb5d699ac74b1a017628fcfb4302846b1c7c352`
- `[1024:1114]`: `8c32fdb048dc29f3f47dd1fb1c8fe53790d239309e340e03bd486d8722d424ff`

I also independently ran the committed record checker:

```sh
python3 -B /tmp/revenger-r63-fixture.JisGn5uw/corpus/live/runs/round-63/oracle_check.py
```

Observed five region lines: all padding `OK`; both reported member offsets, sizes, signatures and decompressed digests `OK`; final line **`ORACLE OK`**.

**Named decision:** W2VerifyFixture **PASS for Q06's current built-byte fixture premises** at this commit. This fresh check does not independently establish the historical ordering requirement “after every edit and before any producer call,” and is not a Q06 decision on C1's separate ZIP entry.

**Impacted axes:** C2 coverage F / Q06. **Smallest correction:** none to these bytes; retain the temporal/provenance limitation rather than claiming this later check witnessed the earlier producer call.

## Attack 3 — C2 inertness and strongest boundary collision

Counterexample sought: a generic `file` result on the padded image hides an executable member, or a second gzip/zlib prefix starts inside compressed bytes / straddles a padding boundary.

I wrote both consumed compressed slices, both complete decompressed payloads and all three padding spans under scratch. Existing **file 5.48** was invoked as `file --keep-going -- <each absolute path>` and `file --mime-type -- <each absolute path>`; both calls exited `0`, with no stderr from the first. Results:

| Object | `file --keep-going` | MIME |
|---|---|---|
| full image | data | application/octet-stream |
| member at 512, compressed | zlib compressed data; data | application/zlib |
| member at 1024, compressed | zlib compressed data; data | application/zlib |
| member at 512, decompressed | ASCII text | text/plain |
| member at 1024, decompressed | ASCII text | text/plain |
| each padding span | data | application/octet-stream |

Both complete payloads additionally pass `bytes.isascii()` and equal the expected inert diagnostic/inventory text. No member is identified as an executable image. No firmware bytes, extracted payload, REA producer, device or model were executed.

The exhaustive scan above covered **all 2047 two-byte windows**, at every start offset 0–2046, including unaligned positions and windows crossing region boundaries. Observed:

```text
zlib header offsets = [512, 1024]
gzip 1f8b offsets = []
unexpected internal-member prefix offsets = []
prefix windows intersecting any padding span = []
```

Both expected headers are `78da`. After excluding each intended header, all **165 wholly internal two-byte windows** of the compressed members are collision-free. Full-image scanning also checks windows starting at the final compressed byte and extending into padding, rather than scanning disjoint slices only.

Boundary byte windows `[max(0,b-2):min(image_size,b+3)]` were:

```text
b=0     000000
b=512   000078da15
b=591   1d2d000000
b=1024  000078da3d
b=1114  252c000000
b=2048  0000
```

Thus there is no gzip/zlib prefix in padding, at padding scan-window starts, across padding boundaries, or at a non-header position inside either compressed member. This is a bounded byte result, not proof about the scanner's internal search strategy or arbitrary other signature families.

**Impacted axes:** C2 fixture safety and coverage F interpretation. **Smallest correction:** none.

## Fresh counting receipts and scope limits

I reran the frozen counter myself, concurrently with the independent byte checks, from cwd `/`:

```sh
env TMPDIR=/tmp/revenger-r63-fixture.JisGn5uw python3 -B \
  /tmp/revenger-r63-fixture.JisGn5uw/reports/round-63/measure.py \
  /tmp/revenger-r63-fixture.JisGn5uw
```

Observed:

```text
K_HELD=6/14 score=4.3
K_ROW C06 status=partial
K_HELD_BACKED=6/14
F_COVERAGE=5/8 score=6.2
F_FAMILIES=['native-static', 'javascript', 'archives', 'firmware', 'evm']
FRESH_ROWS=18/18
C2_CONTROLS_PASS=2/2
C2_RECEIPT_B_KILLED=2/2
C2_D2_KILLED=2/2
C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
```

The two C3 mutants respectively ended with `AssertionError: r55: forged receipt accepted` and `AssertionError: r36: forged receipt accepted`, each exit `1`; controls exited `0`. C1 remains mechanically 6/14 while C06 is intentionally partial pending independent Q01–Q13 admission; this fixture review supplies no C1 gate decisions. C3 observations are the requested frozen-counter context, not a separate source review or canonical judgment.

For C2, I additionally rechecked internal envelope consistency: saved `stdout.raw` equals `inspection.json` byte-for-byte; its SHA-256 is `f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9`, matching the receipt. The image digest matches both receipt and record; Evidence IDs agree. Record windows are exactly `(512,79,zlib)` and `(1024,90,zlib)`.

**Not established by this seat:** real-run origin or historical pre-producer timing; image/record/receipt consistency cannot authenticate origin. No inference from this synthetic fixture to real firmware or general scanner completeness is warranted. Those are scope limits, not a located fixture defect.

## Tooling and cleanup

No tools were installed or updated; pacman was not invoked. Used existing Python 3.14.8, zlib 1.3.2 and file 5.48. Scratch was confined to `/tmp/revenger-r63-fixture.JisGn5uw` and is removed after this report lands. No correction to fixture bytes is requested.
