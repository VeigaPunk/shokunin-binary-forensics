# R63 ZIP readout findings

## Axes

- **Byte derivation:** EOCD and member metadata are parsed from raw ZIP bytes using `struct`; each payload SHA-256 is recomputed after raw-DEFLATE inflation from the local-header payload.
- **Oracle agreement:** all fields recorded in `truth.json` and compared below match.
- **Reproducibility:** script and its captured run output are saved beside this report.

## Run and evidence

Ran once from the lane repository:

```text
python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/build/zip-readout.py
```

- Script: `.ufo/waves/round-63/build/zip-readout.py` (stdlib only; no `zipfile` API)
- Full output: `.ufo/waves/round-63/build/zip-readout.out`
- Oracle: `corpus/fixtures/archive-r2/truth.json`

Readout: archive size `2964`, archive SHA-256 `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e`; EOCD byte offset `2942`; disk `0`, central-directory disk `0`, entries on disk `2`, total entries `2`; central directory offset `2828`, size `114` (records end at `2942`).

## Comparison table

`N/A` means `truth.json` does not record an oracle value for that field. For count fields, the expected count is the number of entries in `truth.json`.

| Field | Derived from fixture bytes | truth.json value | Match |
|---|---:|---:|:---:|
| archive_size | 2964 | 2964 | True |
| archive_sha256 | `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e` | `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e` | True |
| EOCD location | 2942 | N/A | N/A |
| EOCD disk number | 0 | N/A | N/A |
| EOCD central-directory disk | 0 | N/A | N/A |
| EOCD entries on this disk | 2 | 2 | True |
| EOCD total central-directory entries | 2 | 2 | True |
| EOCD central-directory size | 114 | N/A | N/A |
| EOCD central-directory offset | 2828 | N/A | N/A |
| `bin/checksum` name | `bin/checksum` | `bin/checksum` | True |
| `bin/checksum` local-header offset | 0 | N/A | N/A |
| `bin/checksum` compressed size | 2668 | 2668 | True |
| `bin/checksum` uncompressed size | 16160 | 16160 | True |
| `bin/checksum` CRC-32 (central-directory record) | `0xb3df9ea7` | N/A | N/A |
| `bin/checksum` inflated payload SHA-256 | `f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0` | `f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0` | True |
| `README.txt` name | `README.txt` | `README.txt` | True |
| `README.txt` local-header offset | 2710 | N/A | N/A |
| `README.txt` compressed size | 78 | 78 | True |
| `README.txt` uncompressed size | 84 | 84 | True |
| `README.txt` CRC-32 (central-directory record) | `0x72a557b1` | N/A | N/A |
| `README.txt` inflated payload SHA-256 | `7d8f6a8de39432f4119f0139c5ef5970c84c23520cfe6b40d19a3653081804d3` | `7d8f6a8de39432f4119f0139c5ef5970c84c23520cfe6b40d19a3653081804d3` | True |

## Mismatch and limitation

No mismatches among fields present in `truth.json`; every comparable field is `True`. `truth.json` contains no EOCD location/disk fields, central-directory offsets/size, local-header offsets, or CRC-32 values, so those byte-derived values are reported as `N/A` rather than claimed as oracle matches. No tool was installed or updated.
