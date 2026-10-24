PASS — independent struct byte walk confirms the requested AXML fields match the authored oracle and candidate entry items 6–8.

## Evidence

Probe: executed a Python standard-library byte walk directly on `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65/fixture.apk`. ZIP EOCD, central-directory and local-header fields, and AXML chunk/string-pool/resource-map/node/attribute fields were unpacked with `struct`; member selection was by walking the archive records, not `zipfile` or the candidate `readout.py`. The observed output:

```text
ZIP eocd_offset=925 entries=3 cd_offset=737 cd_size=188 archive_bytes=947
AndroidManifest.xml local_offset=0 payload_offset=49 payload_bytes=416 crc32=962d075f
AXML type=0x0003 header_size=8 total_size=416 child_chunks=[(1, 8, 28, 196), (384, 204, 8, 44), (256, 248, 16, 24), (258, 272, 16, 96), (259, 368, 16, 24), (257, 392, 16, 24)]
STRING_POOL count=9 flags=0x00000100 strings=['android', 'http://schemas.android.com/apk/res/android', 'manifest', 'package', 'com.example.r65', 'versionCode', 'versionName', '1', '1.0']
RESOURCE_MAP entries=9 nonzero=[(5, '0x0101021b'), (6, '0x0101021c')]
START_ELEMENT offset=272 name='manifest' ns=None attributeStart=20 attributeSize=20 attributeCount=3
ATTRIBUTES (name, namespace, raw value, typed dataType, typed data, resource id, Res_value size):
  ('package', None, 'com.example.r65', 3, 4, 0, 8)
  ('versionCode', 'android', '1', 16, 1, 16843291, 8)
  ('versionName', 'android', '1.0', 3, 8, 16843292, 8)
```

Comparison:
- Oracle `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65/truth.json:37-47` declares the same nine strings in the same order; `:26-35` declares resource IDs `0x0101021b` / `0x0101021c` at indices 5 / 6. The independently parsed values match.
- Oracle `truth.json:3-25` declares attribute rows `(name_idx, ns_idx, raw_value_idx, data_type, data)` as `(3, 0xffffffff, 4, 3, 4)`, `(5, 0, 7, 16, 1)`, `(6, 0, 8, 3, 8)`. The walk resolves these to `package` → typed string `com.example.r65`, `android:versionCode` → typed int `1`, and `android:versionName` → typed string `1.0`; resource IDs match the map.
- Candidate `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-65-apk-axml-byte-evidence.md:64-83` items 6–8 state the same string pool, map, start-element fields, and three attributes. The direct extraction also agrees with oracle member size/CRC and local offset in `truth.json:74-83`.

This PASS is limited to the assigned AXML-byte reprobe; it is not an overall Q01–Q13 admission decision. The one-fixture/manual-readout scope and generalization limits remain as stated in the candidate entry (`:129-132`).