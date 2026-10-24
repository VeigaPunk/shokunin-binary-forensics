# R63 firmware fixture

## Result

Authored the inert raw fixture under `corpus/fixtures/firmware-r63/`:

- `generator.py` — fixed text payloads, offsets, zero padding, zlib level 9; writes the image and derives region sizes and decompressed hashes by reading the completed image bytes.
- `firmware-r63.bin` — 2048 bytes. SHA-256: `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be`.
- `truth.json` — image path/hash/size, a contiguous five-region table, decompressed member hashes/sizes, and recipe/runtime metadata.

Members: offset 512, compressed size 79, decompressed size 78, SHA-256 `a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86`; offset 1024, compressed size 90, decompressed size 97, SHA-256 `2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9`. Padding regions are `[0,512)`, `[591,1024)`, and `[1114,2048)`, all byte `00`.

Artifact hashes:

```text
4e5d5975e3cf6362f6fd430f2147d42f75d011978f7d6b5ec86d224c77793db4  generator.py
9663f90b2b9f29c5beb621e554ed7584eedf5e77d4785f26a453e70dbd5a65e6  truth.json
bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be  firmware-r63.bin
```

The recipe records Python `3.14.8`, zlib compile/runtime `1.3.2`; generation is byte-for-byte reproducible with those recorded Python/zlib versions and has no timestamps or random input. The compressed payloads are inert ASCII records; no payload was executed.

## Commands and retained evidence

The required signature inventory was run before selecting the format:

```text
$ binwalk --list
Zlib compressed file            zlib                               Built-in
Total signatures: 85
Extractable signatures: 57

$ binwalk --version
binwalk 3.1.0
```

Only the listed `zlib` signature was used. Build command and output:

```text
$ python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/generator.py
wrote firmware-r63.bin sha256=bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be size=2048
region offset=0 size=512 kind=padding
region offset=512 size=79 kind=zlib
region offset=591 size=433 kind=padding
region offset=1024 size=90 kind=zlib
region offset=1114 size=934 kind=padding
```

Binwalk exact scan command and output:

```text
$ binwalk /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin --search-all --include zlib
512                                0x200                              Zlib compressed file, total size: 79 bytes
1024                               0x400                              Zlib compressed file, total size: 90 bytes
Analyzed 1 file for 1 file signatures (3 magic patterns) in 1.0 milliseconds
```

### Explicit byte verification

This command reads the built image and `truth.json`; verifies image size/hash, each contiguous region's offset/size/kind, all declared padding bytes, exact zlib stream boundaries, decompressed size/hash and recipe payload bytes, and the recorded Python/zlib versions. It also scans every image byte for binwalk 3.1.0's three zlib magic prefixes, every RFC 1950-valid CMF/FLG header, and gzip magic.

```sh
python3 -B -c 'import hashlib, json, pathlib, platform, sys, zlib
image_path, truth_path = map(pathlib.Path, sys.argv[1:3])
data = image_path.read_bytes()
truth = json.loads(truth_path.read_text(encoding="utf-8"))
assert truth["image"]["path"] == image_path.name
assert len(data) == truth["image"]["size"] == truth["build_recipe"]["image_size"]
digest = hashlib.sha256(data).hexdigest()
assert digest == truth["image"]["sha256"]
recipe = truth["build_recipe"]
assert recipe["command"] == "python3 -B generator.py"
assert recipe["python_version"] == platform.python_version()
assert recipe["compression"]["compile_version"] == zlib.ZLIB_VERSION
assert recipe["compression"]["runtime_version"] == zlib.ZLIB_RUNTIME_VERSION
assert recipe["compression"]["format"] == "RFC 1950 zlib-wrapped DEFLATE"
assert recipe["compression"]["implementation"] == "zlib.compress(payload, level=9)"
assert recipe["compression"]["level"] == 9
assert recipe["padding_byte_hex"] == "00"
member_specs = {m["name"]: m for m in recipe["members"]}
zlib_offsets = []
cursor = 0
for region in truth["regions"]:
    offset, size, kind = region["offset"], region["size"], region["kind"]
    assert offset == cursor and size > 0 and offset + size <= len(data)
    chunk = data[offset:offset + size]
    assert len(chunk) == size
    if kind == "padding":
        fill = bytes.fromhex(region["fill_hex"])
        assert len(fill) == 1 and region["fill_hex"] == recipe["padding_byte_hex"]
        assert chunk == fill * size
    elif kind == "zlib":
        zlib_offsets.append(offset)
        decoder = zlib.decompressobj()
        payload = decoder.decompress(chunk) + decoder.flush()
        assert decoder.eof and not decoder.unused_data and not decoder.unconsumed_tail
        member = region["decompressed_member"]
        assert len(payload) == member["size"]
        assert hashlib.sha256(payload).hexdigest() == member["sha256"]
        spec = member_specs[region["name"]]
        assert spec["offset"] == offset
        assert payload == spec["payload_utf8"].encode("utf-8")
        print("PASS region offset={} size={} kind=zlib name={} decompressed_size={} decompressed_sha256={}".format(offset, size, region["name"], len(payload), member["sha256"]))
    else:
        raise AssertionError("unknown region kind: {}".format(kind))
    if kind == "padding":
        print("PASS region offset={} size={} kind=padding fill_hex={}".format(offset, size, region["fill_hex"]))
    cursor = offset + size
assert cursor == len(data)
assert zlib_offsets == [m["offset"] for m in recipe["members"]]
assert len(zlib_offsets) >= 2
print("PASS image size={} sha256={} regions={}".format(len(data), digest, len(truth["regions"])))
def offsets_for(magic):
    return [i for i in range(len(data) - len(magic) + 1) if data.startswith(magic, i)]
for magic in (bytes.fromhex("789c"), bytes.fromhex("78da"), bytes.fromhex("785e")):
    found = offsets_for(magic)
    expected = [off for off in zlib_offsets if data[off:off + 2] == magic]
    assert found == expected
    print("PASS binwalk_zlib_magic {} offsets={}".format(magic.hex(), found))
valid_zlib_headers = []
for i in range(len(data) - 1):
    cmf, flg = data[i], data[i + 1]
    if cmf & 0x0f == 8 and cmf >> 4 <= 7 and ((cmf << 8) | flg) % 31 == 0:
        valid_zlib_headers.append(i)
assert valid_zlib_headers == zlib_offsets
print("PASS RFC1950_header_offsets={}".format(valid_zlib_headers))
gzip_offsets = offsets_for(bytes.fromhex("1f8b"))
assert not gzip_offsets
print("PASS gzip_magic_1f8b offsets={}".format(gzip_offsets))' /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/truth.json
```

Byte-verification transcript (exit 0):

```text
PASS region offset=0 size=512 kind=padding fill_hex=00
PASS region offset=512 size=79 kind=zlib name=diagnostic-note decompressed_size=78 decompressed_sha256=a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86
PASS region offset=591 size=433 kind=padding fill_hex=00
PASS region offset=1024 size=90 kind=zlib name=component-note decompressed_size=97 decompressed_sha256=2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9
PASS region offset=1114 size=934 kind=padding fill_hex=00
PASS image size=2048 sha256=bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be regions=5
PASS binwalk_zlib_magic 789c offsets=[]
PASS binwalk_zlib_magic 78da offsets=[512, 1024]
PASS binwalk_zlib_magic 785e offsets=[]
PASS RFC1950_header_offsets=[512, 1024]
PASS gzip_magic_1f8b offsets=[]
BYTE_VERIFICATION_EXIT=0
```

### Unblob cross-check

```text
$ unblob --version
26.6.4
```

For a known-offset member extraction, exact image bytes `[512:591)` were copied to scratch, then passed to unblob. Copy command and output:

```text
$ python3 -B -c 'from pathlib import Path; import hashlib; image=Path("/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin").read_bytes(); chunk=image[512:591]; out=Path("/tmp/revenger-r63-firmware-member0-confirmed.zlib"); out.write_bytes(chunk); print("member_offset=512 compressed_size={} sha256={}".format(len(chunk), hashlib.sha256(chunk).hexdigest()))'
member_offset=512 compressed_size=79 sha256=bf3dd2e42d36324ae17e81c66cb5d699ac74b1a017628fcfb4302846b1c7c352

$ unblob --process-num 1 --extract-dir /tmp/revenger-r63-firmware-unblob-confirmed --report /tmp/revenger-r63-firmware-unblob-confirmed-report.json --log /tmp/revenger-r63-firmware-unblob-confirmed.log /tmp/revenger-r63-firmware-member0-confirmed.zlib
╭────────────────────────────── unblob (26.6.4) ──────────────────────────────╮
│ Extracted files: 2                                                           │
│ Extracted directories: 1                                                     │
│ Extracted links: 0                                                           │
│ Extraction directory size: 157.00 B                                          │
╰─────────────────────────────────────────────────────────────────────────────╯
       Chunks distribution
│ ZLIB       │ 79.00 B │ 100.00% │
│ UNKNOWN    │ 0.00 B  │  0.00%  │
```

The emitted `zlib.uncompressed` file was 78 bytes; `sha256sum` returned `a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86`, matching `truth.json`.
The whole padded image scan was also attempted; it does not establish embedded-member discovery by unblob:

```text
$ unblob -vvv --process-num 1 --force --extract-dir /tmp/revenger-r63-firmware-unblob --report /tmp/revenger-r63-firmware-unblob-report.json --log /tmp/revenger-r63-firmware-unblob.log /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin
log result (timestamp/pid omitted): Ended searching for chunks all_chunks=[]
```


## Risks and scope

Unblob 26.6.4 did not discover either embedded stream when scanning the full padded raw image (`all_chunks=[]`); its zlib handler patterns are anchored at stream start. The exact declared first member is extractable when supplied as a standalone stream, as shown above. Binwalk and the fixture's independent byte sweep find only the two declared streams in the full image. This fixture seat did not execute payloads or install/update tools; no packages were installed.
