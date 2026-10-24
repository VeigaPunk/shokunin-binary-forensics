source: S032 — PKWARE APPNOTE.TXT, `.ZIP` File Format Specification — https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT (spec, tier A, opened 2026-10-23) — scope: the central directory file header and end-of-central-directory record field layout for one authored ZIP archive — anchors: §4.3.12 (central directory structure, fixed file-header field table), §4.3.16 (end of central directory record), §4.3.3 (byte order), §4.4.7 (CRC-32), §4.4.10–4.4.12 (name/extra/comment length fields), §4.4.16 (relative offset of local header), §4.4.21–4.4.22 (total entry counts); version 6.3.10, FINAL, revised Nov 01 2022; snapshot `.ufo/waves/round-63/source-snapshots/appnote.txt` sha256 `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`, 174585 bytes
source: S034 — PKWARE APPNOTE.TXT, `.ZIP` File Format Specification — https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT (spec, tier A; registry id assigned by L1 at the round-63 append, superseding S032's narrower scope — row text in §Sources) — scope: the local file header record field layout for one authored ZIP archive — anchor: §4.3.7 (local file header, fixed field-width list); version 6.3.10, FINAL, revised Nov 01 2022; same snapshot `.ufo/waves/round-63/source-snapshots/appnote.txt` sha256 `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`, 174585 bytes
source: S033 — Authored archive-r2 bytes, the authored oracle and the saved archive inventory record — `corpus/fixtures/archive-r2/fixture.zip`, `corpus/fixtures/archive-r2/truth.json`, `corpus/live/runs/20261012T164246Z/artifact-inspection.json` (own-work, tier A; registry id assigned by L1 at the round-63 append — row text in §Sources) — scope: the byte content of that one fixture, that one authored oracle and the literal saved fields of that one record at base commit `55bcb6e1aeb4d42923a4e98db6580f67142b41ac`; anchors: fixture sha256 `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e` (2964 bytes), `truth.json` sha256 `7df773bf46b7c1273f8c3402b7825e7dacbb7f990c7d7ef41f30917c94726e68`, saved record sha256 `2fec924b5217885674149b6a516970f419a8e731c8e6e49eab178a4f065f3380`
source: S035 — The run's own ledger — `corpus/live/runs/20261012T164246Z/LEDGER.md` (own-work, tier A; registry id assigned by L1 at the round-63 append — row text in §Sources) — scope: the recorded layer for the producer invocation that produced the saved record named above, at base commit `55bcb6e1aeb4d42923a4e98db6580f67142b41ac`; anchor: file sha256 `05042a555f91511c9c191565d92f83527f54d1c9b14de331587f4cbffff9e6cb`, 3959 bytes
verified-at: 2026-10-23 (round-63 work commit pending; the fixture, oracle, saved-record and ledger bytes read here are byte-identical at base commit `55bcb6e1aeb4d42923a4e98db6580f67142b41ac`, verified by `git show <base>:<path> | sha256sum` and `sha256sum <path>`)
recheck: `python3 -B readout.py <repo-root>` — the script is the `### Code` block in §Reproduce, saved verbatim as `readout.py`; run from the lane root it exits 0 and prints 17 stdout lines whose SHA-256 is `ccaffa322c49d1850fb7da86dc9221ea3bd73c8e3db81cc2ce9be6a1e5b40dc5`; the per-value form `python3 -B readout.py <repo-root> --fact '<id>'` prints the single JSON line for one named fact. The stdout carries only repo-relative paths, never the extraction root, so the same bytes give the same 17 lines from any checkout of the same commit.
coverage-map: C06 (`corpus/README.md`, archives (ZIP inventory)) — the local header, central directory and end-of-central-directory records of one authored ZIP fixture, compared against one authored oracle and one saved archive-inventory record. Not covered: nested-archive (`fixtures/nested-r11`) and duplicate-entry (`fixtures/duplicate-r15`) archive ground, which the C06 row also lists and which this entry does not examine.
admission-status: admitted — README C06 flipped to held naming this entry in the round-63 admission revision; the stale `candidate` header was repaired round-66 (R65ScoutReadme §C; admission on record in `corpus/lessons/round-63.md`)

# ZIP local header, central directory and end-of-central-directory records of one authored archive, compared with an authored oracle and a saved inventory record — C06

Scope. One authored archive, `corpus/fixtures/archive-r2/fixture.zip`, and two documents that describe it: the authored oracle `corpus/fixtures/archive-r2/truth.json` and the saved inspection record `corpus/live/runs/20261012T164246Z/artifact-inspection.json`. The analysis is **manual**: a Python standard-library script that reads the archive's bytes with `struct` and inflates the stored DEFLATE payload with `zlib`. Nothing is extracted to disk, no member is executed, no producer is called, no network is used, and no verifier source is read. The comparison is **one fixture's central-directory view**: the member names, local-header offsets, compressed and uncompressed sizes and CRC-32 values the central directory states, against an independent oracle, against the literal fields of one saved record. It is not a ZIP parser, not an archive inventory tool, and not a statement about any provider's accuracy.

## Observation

Every numbered item below is produced by the readout in §Reproduce. The command is given with the output it printed; the script is the `### Code` block of that section, and the same lines appear in the full 17-line stdout reproduced there. Item numbers are the entry's own; they are not identifiers in any file.

**Archive bytes**

1. The archive is **2964 bytes** with SHA-256 `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e`, read from the file's bytes.

```
$ python3 -B readout.py <repo-root> --fact 'archive'
{"fact":"archive","path":"corpus/fixtures/archive-r2/fixture.zip","bytes":2964,"sha256":"857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e"}
```


2. The four files this entry reads — the fixture, the oracle and the saved record (S033), and the run's ledger `corpus/live/runs/20261012T164246Z/LEDGER.md` (S035) — are byte-identical at the base commit `55bcb6e1aeb4d42923a4e98db6580f67142b41ac` and in the working tree:

```
$ git show 55bcb6e1aeb4d42923a4e98db6580f67142b41ac:corpus/fixtures/archive-r2/fixture.zip | sha256sum
857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e  -
$ git show 55bcb6e1aeb4d42923a4e98db6580f67142b41ac:corpus/fixtures/archive-r2/truth.json | sha256sum
7df773bf46b7c1273f8c3402b7825e7dacbb7f990c7d7ef41f30917c94726e68  -
$ git show 55bcb6e1aeb4d42923a4e98db6580f67142b41ac:corpus/live/runs/20261012T164246Z/artifact-inspection.json | sha256sum
2fec924b5217885674149b6a516970f419a8e731c8e6e49eab178a4f065f3380  -
$ git show 55bcb6e1aeb4d42923a4e98db6580f67142b41ac:corpus/live/runs/20261012T164246Z/LEDGER.md | sha256sum
05042a555f91511c9c191565d92f83527f54d1c9b14de331587f4cbffff9e6cb  -
```

```
$ sha256sum corpus/fixtures/archive-r2/fixture.zip corpus/fixtures/archive-r2/truth.json corpus/live/runs/20261012T164246Z/artifact-inspection.json corpus/live/runs/20261012T164246Z/LEDGER.md
857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e  corpus/fixtures/archive-r2/fixture.zip
7df773bf46b7c1273f8c3402b7825e7dacbb7f990c7d7ef41f30917c94726e68  corpus/fixtures/archive-r2/truth.json
2fec924b5217885674149b6a516970f419a8e731c8e6e49eab178a4f065f3380  corpus/live/runs/20261012T164246Z/artifact-inspection.json
05042a555f91511c9c191565d92f83527f54d1c9b14de331587f4cbffff9e6cb  corpus/live/runs/20261012T164246Z/LEDGER.md
```

**End of central directory record**

3. The end-of-central-directory record starts at byte offset **2942** of the 2964-byte file — 22 bytes from the end — and its four signature bytes are `504b0506`, the little-endian form of `0x06054b50`. The record's disk fields are `number of this disk` **0** and `number of the disk with the start of the central directory` **0**; its two entry counts are **2** on this disk and **2** in the central directory; its `size of the central directory` is **114** and its `offset of start of central directory` is **2828**; its `.ZIP file comment length` is **0** and the comment bytes are empty.

```
$ python3 -B readout.py <repo-root> --fact 'eocd'
{"fact":"eocd","eocd_offset":2942,"eocd_offset_from_end":22,"eocd_signature_hex":"504b0506","number_of_this_disk":0,"number_of_disk_with_start_of_cd":0,"total_entries_in_cd_on_this_disk":2,"total_entries_in_cd":2,"size_of_central_directory":114,"offset_of_start_of_cd":2828,"zip_file_comment_length":0,"zip_file_comment_hex":""}
```


4. The central directory therefore occupies the byte range **[2828, 2942)** — 114 bytes — and the record that follows it begins immediately at 2942: `cd_offset + cd_size == eocd_offset`. Two central-directory file headers were parsed from those 114 bytes, and both of the end-of-central-directory record's own counts equal that parsed number.

```
$ python3 -B readout.py <repo-root> --fact 'central_directory'
{"fact":"central_directory","cd_offset":2828,"cd_size":114,"cd_end_offset":2942,"cd_byte_range_half_open":[2828,2942],"cd_byte_range_inclusive":[2828,2941],"cd_end_equals_eocd_offset":true,"eocd_total_entries_matches_parsed_entries":true,"eocd_entries_on_this_disk_matches_parsed_entries":true,"parsed_entries":2}
```


**Field offsets, derived from the specification's own field lists**

5. The three fixed records this entry reads have fixed lengths of **30** bytes (local file header), **46** bytes (central directory file header) and **22** bytes (end-of-central-directory record). Those three lengths, and every field offset used below, are **computed by summing the byte widths the specification's own field tables list** — the local file header's widths from S034 §4.3.7, the central directory file header's and the end-of-central-directory record's widths from S032 §4.3.12 and §4.3.16 — not assumed and not taken from any implementation. The computed offsets are: local file header `file name length` at **26** and `extra field length` at **28**; central directory `crc-32` at **16**, `compressed size` at **20**, `uncompressed size` at **24**, `file name length` at **28**, `relative offset of local header` at **42**; end-of-central-directory `total number of entries in the central directory on this disk` at **8**, `total number of entries in the central directory` at **10**, `size of the central directory` at **12**, `offset of start of central directory` at **16**. The computed 22-byte end-of-central-directory length equals the observed 22 bytes from the record's start to the end of the file, and the two signatures read at the computed offset 0 are `0x02014b50` and `0x06054b50`.

```
$ python3 -B readout.py <repo-root> --fact 'spec_derived_field_offsets'
{"fact":"spec_derived_field_offsets","source_anchor":"APPNOTE 6.3.10 \u00a74.3.7 local file header field table (S034); \u00a74.3.12 and \u00a74.3.16 field tables (S032)","local_header_fixed_part_bytes":30,"local_header_field_offsets":{"local file header signature":{"offset":0,"width":4},"version needed to extract":{"offset":4,"width":2},"general purpose bit flag":{"offset":6,"width":2},"compression method":{"offset":8,"width":2},"last mod file time":{"offset":10,"width":2},"last mod file date":{"offset":12,"width":2},"crc-32":{"offset":14,"width":4},"compressed size":{"offset":18,"width":4},"uncompressed size":{"offset":22,"width":4},"file name length":{"offset":26,"width":2},"extra field length":{"offset":28,"width":2}},"central_directory_fixed_part_bytes":46,"central_directory_field_offsets":{"central file header signature":{"offset":0,"width":4},"version made by":{"offset":4,"width":2},"version needed to extract":{"offset":6,"width":2},"general purpose bit flag":{"offset":8,"width":2},"compression method":{"offset":10,"width":2},"last mod file time":{"offset":12,"width":2},"last mod file date":{"offset":14,"width":2},"crc-32":{"offset":16,"width":4},"compressed size":{"offset":20,"width":4},"uncompressed size":{"offset":24,"width":4},"file name length":{"offset":28,"width":2},"extra field length":{"offset":30,"width":2},"file comment length":{"offset":32,"width":2},"disk number start":{"offset":34,"width":2},"internal file attributes":{"offset":36,"width":2},"external file attributes":{"offset":38,"width":4},"relative offset of local header":{"offset":42,"width":4}},"eocd_fixed_part_bytes":22,"eocd_field_offsets":{"end of central dir signature":{"offset":0,"width":4},"number of this disk":{"offset":4,"width":2},"number of the disk with the start of the central directory":{"offset":6,"width":2},"total number of entries in the central directory on this disk":{"offset":8,"width":2},"total number of entries in the central directory":{"offset":10,"width":2},"size of the central directory":{"offset":12,"width":4},"offset of start of central directory with respect to the starting disk number":{"offset":16,"width":4},".ZIP file comment length":{"offset":20,"width":2}},"eocd_fixed_part_equals_observed_record_length":true,"central_directory_signature_at_computed_offset":33639248,"central_directory_signature_is_0x02014b50":true,"eocd_signature_at_computed_offset":101010256,"eocd_signature_is_0x06054b50":true,"per_member_offset_checks":[{"file_name":"bin/checksum","crc32_offset":16,"crc32_value_at_computed_offset":3017776807,"crc32_equals_record_crc32":true,"compressed_size_offset":20,"compressed_size_value_at_computed_offset":2668,"uncompressed_size_offset":24,"uncompressed_size_value_at_computed_offset":16160,"file_name_length_offset":28,"file_name_length_value_at_computed_offset":12,"file_name_length_equals_record":true,"relative_offset_of_local_header_offset":42,"relative_offset_of_local_header_value_at_computed_offset":0,"relative_offset_equals_record":true},{"file_name":"README.txt","crc32_offset":16,"crc32_value_at_computed_offset":1923438513,"crc32_equals_record_crc32":true,"compressed_size_offset":20,"compressed_size_value_at_computed_offset":78,"uncompressed_size_offset":24,"uncompressed_size_value_at_computed_offset":84,"file_name_length_offset":28,"file_name_length_value_at_computed_offset":10,"file_name_length_equals_record":true,"relative_offset_of_local_header_offset":42,"relative_offset_of_local_header_value_at_computed_offset":2710,"relative_offset_equals_record":true}]}
```


**Member records (central directory)**

6. The first central-directory record, at file offset **2828**, names the member **`bin/checksum`** (`62696e2f636865636b73756d`), with `relative offset of local header` **0**, `compressed size` **2668**, `uncompressed size` **16160** and `crc-32` **`b3df9ea7`** (decimal 3017776807). Its `file name length` is 12, `extra field length` 0, `file comment length` 0, `compression method` 8, `general purpose bit flag` 0, and its extra-field and comment bytes are empty. Reading the same fields at the specification-derived offsets of item 5 selects the same bytes.

```
$ python3 -B readout.py <repo-root> --fact 'member_cd[bin/checksum]'
{"fact":"member_cd[bin/checksum]","index":0,"cd_header_offset":2828,"cd_header_signature_hex":"504b0102","version_made_by":788,"version_needed_to_extract":20,"general_purpose_bit_flag":0,"compression_method":8,"last_mod_file_time":27855,"last_mod_file_date":23884,"crc32":3017776807,"crc32_hex":"b3df9ea7","compressed_size":2668,"uncompressed_size":16160,"file_name_length":12,"extra_field_length":0,"file_comment_length":0,"disk_number_start":0,"internal_file_attributes":0,"external_file_attributes":2179792896,"relative_offset_of_local_header":0,"file_name":"bin/checksum","file_name_bytes_hex":"62696e2f636865636b73756d","extra_field_hex":"","file_comment_hex":""}
```


7. The second central-directory record, at file offset **2886**, names the member **`README.txt`** (`524541444d452e747874`), with `relative offset of local header` **2710**, `compressed size` **78**, `uncompressed size` **84** and `crc-32` **`72a557b1`** (decimal 1923438513). Its `file name length` is 10, `extra field length` 0, `file comment length` 0, `compression method` 8, `general purpose bit flag` 0, and its extra-field and comment bytes are empty. Reading the same fields at the specification-derived offsets of item 5 selects the same bytes.

```
$ python3 -B readout.py <repo-root> --fact 'member_cd[README.txt]'
{"fact":"member_cd[README.txt]","index":1,"cd_header_offset":2886,"cd_header_signature_hex":"504b0102","version_made_by":788,"version_needed_to_extract":20,"general_purpose_bit_flag":0,"compression_method":8,"last_mod_file_time":27987,"last_mod_file_date":23884,"crc32":1923438513,"crc32_hex":"72a557b1","compressed_size":78,"uncompressed_size":84,"file_name_length":10,"extra_field_length":0,"file_comment_length":0,"disk_number_start":0,"internal_file_attributes":0,"external_file_attributes":25165824,"relative_offset_of_local_header":2710,"file_name":"README.txt","file_name_bytes_hex":"524541444d452e747874","extra_field_hex":"","file_comment_hex":""}
```


**Member payloads (local header, inflated)**

8. At the local-header offset the first member's record states, byte 0 of the file, the four bytes `504b0304` — the little-endian form of the local file header signature `0x04034b50`. The local header names the same member, `bin/checksum`, and its `file name length` is 12, matching the central directory's. Its payload starts at byte **42** — the local header's 30-byte fixed part, computed from S034 §4.3.7's field widths, plus its 12-byte name — and is **2668** bytes long, matching the central directory's compressed size; inflating it with `zlib` (raw DEFLATE) yields **16160** bytes, matching the central directory's uncompressed size, with SHA-256 `f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0` and CRC-32 `b3df9ea7` — the same CRC-32 the central directory states for this member.

```
$ python3 -B readout.py <repo-root> --fact 'member_local[bin/checksum]'
{"fact":"member_local[bin/checksum]","file_name":"bin/checksum","local_header_offset":0,"local_header_signature_hex":"504b0304","local_header_signature_is_lfh":true,"local_header_file_name":"bin/checksum","local_header_name_equals_cd_name":true,"local_header_file_name_length":12,"local_header_extra_field_length":0,"local_header_name_length_equals_cd_name_length":true,"payload_offset":42,"payload_bytes_read":2668,"payload_bytes_equal_cd_compressed_size":true,"inflated_bytes":16160,"inflated_bytes_equal_cd_uncompressed_size":true,"inflated_sha256":"f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0","inflated_crc32":3017776807,"inflated_crc32_hex":"b3df9ea7","inflated_crc32_equals_cd_crc32":true}
```


9. At the local-header offset the second member's record states, byte **2710**, the four bytes `504b0304`. The local header names the same member, `README.txt`, and its `file name length` is 10. Its payload starts at byte **2750** — the local header's 30-byte fixed part, computed from S034 §4.3.7's field widths, plus its 10-byte name — and is **78** bytes long, matching the central directory's compressed size; inflating it yields **84** bytes, matching the central directory's uncompressed size, with SHA-256 `7d8f6a8de39432f4119f0139c5ef5970c84c23520cfe6b40d19a3653081804d3` and CRC-32 `72a557b1` — again the CRC-32 the central directory states.

```
$ python3 -B readout.py <repo-root> --fact 'member_local[README.txt]'
{"fact":"member_local[README.txt]","file_name":"README.txt","local_header_offset":2710,"local_header_signature_hex":"504b0304","local_header_signature_is_lfh":true,"local_header_file_name":"README.txt","local_header_name_equals_cd_name":true,"local_header_file_name_length":10,"local_header_extra_field_length":0,"local_header_name_length_equals_cd_name_length":true,"payload_offset":2750,"payload_bytes_read":78,"payload_bytes_equal_cd_compressed_size":true,"inflated_bytes":84,"inflated_bytes_equal_cd_uncompressed_size":true,"inflated_sha256":"7d8f6a8de39432f4119f0139c5ef5970c84c23520cfe6b40d19a3653081804d3","inflated_crc32":1923438513,"inflated_crc32_hex":"72a557b1","inflated_crc32_equals_cd_crc32":true}
```


**Comparison with the authored oracle `truth.json`**

10. At the archive level, the bytes give SHA-256 `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e` and length 2964, and both equal the oracle's `archive_sha256` and `archive_size`.

```
$ python3 -B readout.py <repo-root> --fact 'truth_archive_level'
{"fact":"truth_archive_level","archive_sha256_equals_truth":true,"archive_size_equals_truth":true}
```


11. For `bin/checksum` the oracle's `size` 16160, `compressed_size` 2668 and `sha256` `f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0` equal the values derived from the bytes: the uncompressed size and compressed size from the central-directory record, and the digest recomputed over the inflated local-header payload. For `README.txt` the oracle's `size` 84, `compressed_size` 78 and `sha256` `7d8f6a8de39432f4119f0139c5ef5970c84c23520cfe6b40d19a3653081804d3` equal the derived values in the same way. The oracle records no CRC-32, no EOCD location, no central-directory offset or size and no local-header offsets, so no oracle comparison is made for those values.

```
$ python3 -B readout.py <repo-root> --fact 'truth_member[bin/checksum]'
{"fact":"truth_member[bin/checksum]","file_name":"bin/checksum","present_in_truth":true,"size_equals_truth":true,"compressed_size_equals_truth":true,"sha256_equals_truth":true,"sha256_source":"recomputed sha256 over the inflated local-header payload"}
```


```
$ python3 -B readout.py <repo-root> --fact 'truth_member[README.txt]'
{"fact":"truth_member[README.txt]","file_name":"README.txt","present_in_truth":true,"size_equals_truth":true,"compressed_size_equals_truth":true,"sha256_equals_truth":true,"sha256_source":"recomputed sha256 over the inflated local-header payload"}
```


12. The member **name sets** agree exactly: no member name appears in the archive and not in the oracle, and no oracle member name is absent from the archive.

```
$ python3 -B readout.py <repo-root> --fact 'truth_member_set_delta'
{"fact":"truth_member_set_delta","in_zip_not_in_truth":[],"in_truth_not_in_zip":[]}
```


**Recorded provenance in the oracle file (not an observation of the archive's bytes)**

*Recorded-provenance note, unnumbered and outside the observation sequence above.* The oracle file also carries a `build` string, printed here as a **recorded** field of that file. This entry records it and relies on it for no value: it makes no claim about what any library named in that string does, and no field, count or digest in this entry is derived from it.

```
$ python3 -B readout.py <repo-root> --fact 'truth_build_field'
{"fact":"truth_build_field","recorded_build_string":"Python zipfile.ZipFile(mode=w, compression=ZIP_DEFLATED, compresslevel=9); write checksum as bin/checksum; writestr README.txt as stated","note":"recorded provenance string read from the oracle file; this entry makes no claim about the behaviour of any library it names and does not rely on it for any value"}
```


**Correspondence with the saved record `corpus/live/runs/20261012T164246Z/artifact-inspection.json`**

13. The saved record is **7692** bytes with SHA-256 `2fec924b5217885674149b6a516970f419a8e731c8e6e49eab178a4f065f3380`. Its recorded fields — read from the file, not re-derived — are top-level Evidence ID `ev_5cc39f356009773bb3d8a214ec39536a99f0799f6709f4cd7bb3badb33c6cf7d`, operation `inspect_artifact`, provider id `rea-artifact-graph`, provider version `1`, subject digest `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e` (equal to the archive digest derived in item 1), 3 occurrences, and nested inventory Evidence ID `ev_cc681c2a03da4e9901275c1425fb1f726cca78bbdbec3defb13b6a0ac8ad156b`. These are **recorded** fields of a saved file: their presence is observed here, but this entry does not establish who produced the record, that it is complete, or that it is authentic. The run's own ledger, `corpus/live/runs/20261012T164246Z/LEDGER.md` (S035; sha256 `05042a555f91511c9c191565d92f83527f54d1c9b14de331587f4cbffff9e6cb`), is the **recorded layer** for the attribution: it records the producer invocation (`npx -y rea-agents@6.4.0 inspect-artifact …`, exit 0), the Evidence IDs quoted above, and the fixture digest. This entry credits the ledger with that recorded attribution only; it derives no value from the ledger.

```
$ python3 -B readout.py <repo-root> --fact 'saved_record'
{"fact":"saved_record","path":"corpus/live/runs/20261012T164246Z/artifact-inspection.json","bytes":7692,"sha256":"2fec924b5217885674149b6a516970f419a8e731c8e6e49eab178a4f065f3380","evidence_id":"ev_5cc39f356009773bb3d8a214ec39536a99f0799f6709f4cd7bb3badb33c6cf7d","operation":"inspect_artifact","provider_id":"rea-artifact-graph","provider_version":"1","subject_sha256":"857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e","occurrences":3,"nested_inventory_evidence_id":"ev_cc681c2a03da4e9901275c1425fb1f726cca78bbdbec3defb13b6a0ac8ad156b"}
```


14. The saved record's occurrence for `bin/checksum` carries `logical_path` `bin/checksum` (equal to the name derived in item 6), `declared_size` 16160 (equal to the central directory's uncompressed size for that member), `compressed_size` 2668 (equal to the central directory's compressed size), and the node it points at carries `sha256` `f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0` and `size` 16160 — the node digest equals the digest recomputed over the inflated payload in item 8. The occurrence also records `executable` true, `encrypted` false and `hash_status` `verified`; these three are **recorded** fields with no derived counterpart in this entry, and no claim is made about what they mean.

```
$ python3 -B readout.py <repo-root> --fact 'saved_occurrence[bin/checksum]'
{"fact":"saved_occurrence[bin/checksum]","file_name":"bin/checksum","present_in_saved_record":true,"saved_logical_path":"bin/checksum","saved_logical_path_equals_derived_name":true,"saved_declared_size":16160,"saved_declared_size_equals_cd_uncompressed_size":true,"saved_compressed_size":2668,"saved_compressed_size_equals_cd_compressed_size":true,"saved_node_sha256":"f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0","saved_node_sha256_equals_recomputed_inflated_sha256":true,"saved_node_size":16160,"saved_node_size_equals_cd_uncompressed_size":true,"saved_executable":true,"saved_encrypted":false,"saved_hash_status":"verified"}
```


15. The saved record's occurrence for `README.txt` carries `logical_path` `README.txt` (equal to the name derived in item 7), `declared_size` 84 (equal to the central directory's uncompressed size), `compressed_size` 78 (equal to the central directory's compressed size), and the node it points at carries `sha256` `7d8f6a8de39432f4119f0139c5ef5970c84c23520cfe6b40d19a3653081804d3` and `size` 84 — the node digest equals the digest recomputed over the inflated payload in item 9. The occurrence also records `executable` false, `encrypted` false and `hash_status` `verified`, again recorded fields with no derived counterpart here.

```
$ python3 -B readout.py <repo-root> --fact 'saved_occurrence[README.txt]'
{"fact":"saved_occurrence[README.txt]","file_name":"README.txt","present_in_saved_record":true,"saved_logical_path":"README.txt","saved_logical_path_equals_derived_name":true,"saved_declared_size":84,"saved_declared_size_equals_cd_uncompressed_size":true,"saved_compressed_size":78,"saved_compressed_size_equals_cd_compressed_size":true,"saved_node_sha256":"7d8f6a8de39432f4119f0139c5ef5970c84c23520cfe6b40d19a3653081804d3","saved_node_sha256_equals_recomputed_inflated_sha256":true,"saved_node_size":84,"saved_node_size_equals_cd_uncompressed_size":true,"saved_executable":false,"saved_encrypted":false,"saved_hash_status":"verified"}
```


16. The saved record's three occurrence paths are `.`, `README.txt` and `bin/checksum`. Both member names derived from the bytes appear there; the third path, `.`, is the archive root itself, not a member, so it is the one path present in the record and not among the archive's members.

```
$ python3 -B readout.py <repo-root> --fact 'saved_occurrence_set_delta'
{"fact":"saved_occurrence_set_delta","saved_occurrence_paths":[".","README.txt","bin/checksum"],"in_zip_not_in_saved_record":[],"in_saved_record_not_in_zip":["."],"note":"the saved record's '.' occurrence is the archive root itself, not a member"}
```


## Inference

17. [INFERENCE, scoped to this one archive, this one oracle and this one saved record] The values the central directory states for each member — its name, uncompressed size, compressed size and CRC-32 — describe the member bytes that the same archive's local header points at. Basis: for both members the local-header name equals the central-directory name (item 8, item 9), the payload length equals the central directory's compressed size (item 8, item 9), the inflated length equals the central directory's uncompressed size (item 8, item 9), and the CRC-32 recomputed over the inflated payload equals the central directory's CRC-32 field (item 8, item 9). This is an agreement between two record types inside one file, not a general property of ZIP archives.

18. [INFERENCE, scoped to this one archive and this one oracle] The central directory's view of this archive agrees with the authored oracle on each field this entry checked: the archive's size and SHA-256, and, for each of the two members, its name, uncompressed size, compressed size and SHA-256. Basis: item 10 (archive digest and size) and item 11 (both members' names, sizes, compressed sizes and digests). This is agreement of two descriptions of one fixture; it says nothing about how the oracle was produced or whether it would hold for another archive.

19. [INFERENCE, scoped to this one archive and this one saved record] The saved record's occurrence fields that have a derived counterpart — `logical_path`, `declared_size`, `compressed_size` and the node's `sha256` and `size` — equal the values this entry derived from the archive's bytes, for both members. Basis: item 14 and item 15 against items 6–9. This is a correspondence between one record's literal fields and one archive's bytes; it is **not** a claim that the record is complete, correct in general, or authentic, and the record's own stated limitation — that its ZIP inventory lists central-directory entries only — is not tested here.

20. [INFERENCE] Each digest printed in this entry binds exactly the bytes it was computed over: the archive digest covers the 2964 archive bytes, the two inflated-payload digests cover the inflated bytes of their own members, and the saved record's digest covers the 7692 bytes of that saved file. A digest match is not evidence of origin, completeness or authenticity. Basis: item 1, item 8, item 9, item 13.

## Unknown

21. Whether the saved record's `executable`, `encrypted` and `hash_status` fields are correct is **unknown**. They are recorded fields with no derived counterpart in this entry, and this entry does not test them.

22. Whether the saved record is complete — whether an archive member, a nested archive, or any byte is missing from it — is **unknown**. Its own limitations text states that the ZIP inventory lists central-directory entries only and that bytes after the central directory are not occurrences; this entry neither confirms nor denies that boundary, and it does not read the record's completeness beyond the fields named in items 13–16.

23. Whether the archive's `bin/checksum` member is a valid executable, and what it does if run, is **unknown**. No member was executed and no member was disassembled. The member's bytes were inflated and hashed; nothing more.

24. Whether the central directory is complete for this archive — whether an archive could carry members this view does not show — is **unknown**. This entry reads what one file's central directory states.

25. Whether the CRC-32 values the central directory states would be reproduced by any other implementation, or whether other archives' central directories would agree with their own oracles in the same way, is **unknown**. Two members of one fixture were checked.

## Limitations

26. This is a **central-directory-only view of one archive**. The entry reports what one file's end-of-central-directory record and central-directory records state, plus an independent recomputation over that same file's local-header payloads. It is not a ZIP parser, and it is not a claim that any ZIP implementation would read this file the same way. The scope is the records and members this entry names; nothing is claimed about any region of an archive that these records do not describe.

27. **Single fixture.** One archive, one oracle, one saved record. Nothing here is generalized to another archive, another archive family, another provider or another provider version.

28. **Recorded, not authenticated.** The saved record's Evidence IDs, provider id and version, operation name and `hash_status` values are read from a saved file (S033), and the producer invocation that this entry attributes to the run is recorded in the run's own ledger (S035). This entry establishes no producer origin, no acquisition completeness and no authenticity for them, and the digest comparisons establish only that the bytes agree.

29. **Manual analysis.** The readout is a Python standard-library script (`struct`, `zlib`, `hashlib`, `json`, `binascii`); no third-party package was used, none was installed, and no tool is credited with a result it did not output. The one recorded tool invocation in the sources of this lane — the `rea-agents@6.4.0` run that produced the saved record, recorded in `corpus/live/runs/20261012T164246Z/LEDGER.md` (S035) — is credited with nothing here beyond the record's existence and its literal fields. The oracle's recorded `build` string is printed as a recorded field and is relied on for no value; no claim is made about what any library it names does.

30. **No execution, no network, no producer call.** The archive was read as bytes; member payloads were inflated in memory and never written to disk or executed; no producer was invoked; no network request was made; no verifier source was read.

31. **Specification scope.** S032's anchor is the central directory file header and end-of-central-directory record field layout, and S034's is the local file header record field layout, with the field meanings quoted in §Sources. It does not license a general ZIP-parser claim, a ZIP64 claim, a compression-method-semantics claim, or a provider-completeness or authenticity claim; ZIP64 is outside this entry's scope and none of its records is read here.

32. **No guard credit.** No verifier, recheck command, comparison tool or automatic checker is credited as guarding any value in this entry, and none is introduced. The recheck command reproduces the observations; it does not detect the deletion of any clause. See §Q13.

33. **Scope of the coverage row.** This entry covers the `fixtures/archive-r2` ground of C06 only. The C06 row also lists `fixtures/nested-r11` and `fixtures/duplicate-r15`; neither is examined here.

## Reproduce

One command, run once from the lane root on the base-commit tree. The script is the `### Code` block below, saved verbatim as `readout.py`. Python 3 standard library only; no third-party package, no install, no network.

```
$ python3 -B readout.py .
```

exit 0, 17 stdout lines, stdout SHA-256 `ccaffa322c49d1850fb7da86dc9221ea3bd73c8e3db81cc2ce9be6a1e5b40dc5`:

```
{"fact":"archive","path":"corpus/fixtures/archive-r2/fixture.zip","bytes":2964,"sha256":"857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e"}
{"fact":"eocd","eocd_offset":2942,"eocd_offset_from_end":22,"eocd_signature_hex":"504b0506","number_of_this_disk":0,"number_of_disk_with_start_of_cd":0,"total_entries_in_cd_on_this_disk":2,"total_entries_in_cd":2,"size_of_central_directory":114,"offset_of_start_of_cd":2828,"zip_file_comment_length":0,"zip_file_comment_hex":""}
{"fact":"central_directory","cd_offset":2828,"cd_size":114,"cd_end_offset":2942,"cd_byte_range_half_open":[2828,2942],"cd_byte_range_inclusive":[2828,2941],"cd_end_equals_eocd_offset":true,"eocd_total_entries_matches_parsed_entries":true,"eocd_entries_on_this_disk_matches_parsed_entries":true,"parsed_entries":2}
{"fact":"member_cd[bin/checksum]","index":0,"cd_header_offset":2828,"cd_header_signature_hex":"504b0102","version_made_by":788,"version_needed_to_extract":20,"general_purpose_bit_flag":0,"compression_method":8,"last_mod_file_time":27855,"last_mod_file_date":23884,"crc32":3017776807,"crc32_hex":"b3df9ea7","compressed_size":2668,"uncompressed_size":16160,"file_name_length":12,"extra_field_length":0,"file_comment_length":0,"disk_number_start":0,"internal_file_attributes":0,"external_file_attributes":2179792896,"relative_offset_of_local_header":0,"file_name":"bin/checksum","file_name_bytes_hex":"62696e2f636865636b73756d","extra_field_hex":"","file_comment_hex":""}
{"fact":"member_cd[README.txt]","index":1,"cd_header_offset":2886,"cd_header_signature_hex":"504b0102","version_made_by":788,"version_needed_to_extract":20,"general_purpose_bit_flag":0,"compression_method":8,"last_mod_file_time":27987,"last_mod_file_date":23884,"crc32":1923438513,"crc32_hex":"72a557b1","compressed_size":78,"uncompressed_size":84,"file_name_length":10,"extra_field_length":0,"file_comment_length":0,"disk_number_start":0,"internal_file_attributes":0,"external_file_attributes":25165824,"relative_offset_of_local_header":2710,"file_name":"README.txt","file_name_bytes_hex":"524541444d452e747874","extra_field_hex":"","file_comment_hex":""}
{"fact":"member_local[bin/checksum]","file_name":"bin/checksum","local_header_offset":0,"local_header_signature_hex":"504b0304","local_header_signature_is_lfh":true,"local_header_file_name":"bin/checksum","local_header_name_equals_cd_name":true,"local_header_file_name_length":12,"local_header_extra_field_length":0,"local_header_name_length_equals_cd_name_length":true,"payload_offset":42,"payload_bytes_read":2668,"payload_bytes_equal_cd_compressed_size":true,"inflated_bytes":16160,"inflated_bytes_equal_cd_uncompressed_size":true,"inflated_sha256":"f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0","inflated_crc32":3017776807,"inflated_crc32_hex":"b3df9ea7","inflated_crc32_equals_cd_crc32":true}
{"fact":"member_local[README.txt]","file_name":"README.txt","local_header_offset":2710,"local_header_signature_hex":"504b0304","local_header_signature_is_lfh":true,"local_header_file_name":"README.txt","local_header_name_equals_cd_name":true,"local_header_file_name_length":10,"local_header_extra_field_length":0,"local_header_name_length_equals_cd_name_length":true,"payload_offset":2750,"payload_bytes_read":78,"payload_bytes_equal_cd_compressed_size":true,"inflated_bytes":84,"inflated_bytes_equal_cd_uncompressed_size":true,"inflated_sha256":"7d8f6a8de39432f4119f0139c5ef5970c84c23520cfe6b40d19a3653081804d3","inflated_crc32":1923438513,"inflated_crc32_hex":"72a557b1","inflated_crc32_equals_cd_crc32":true}
{"fact":"truth_archive_level","archive_sha256_equals_truth":true,"archive_size_equals_truth":true}
{"fact":"truth_member[bin/checksum]","file_name":"bin/checksum","present_in_truth":true,"size_equals_truth":true,"compressed_size_equals_truth":true,"sha256_equals_truth":true,"sha256_source":"recomputed sha256 over the inflated local-header payload"}
{"fact":"truth_member[README.txt]","file_name":"README.txt","present_in_truth":true,"size_equals_truth":true,"compressed_size_equals_truth":true,"sha256_equals_truth":true,"sha256_source":"recomputed sha256 over the inflated local-header payload"}
{"fact":"truth_member_set_delta","in_zip_not_in_truth":[],"in_truth_not_in_zip":[]}
{"fact":"truth_build_field","recorded_build_string":"Python zipfile.ZipFile(mode=w, compression=ZIP_DEFLATED, compresslevel=9); write checksum as bin/checksum; writestr README.txt as stated","note":"recorded provenance string read from the oracle file; this entry makes no claim about the behaviour of any library it names and does not rely on it for any value"}
{"fact":"saved_record","path":"corpus/live/runs/20261012T164246Z/artifact-inspection.json","bytes":7692,"sha256":"2fec924b5217885674149b6a516970f419a8e731c8e6e49eab178a4f065f3380","evidence_id":"ev_5cc39f356009773bb3d8a214ec39536a99f0799f6709f4cd7bb3badb33c6cf7d","operation":"inspect_artifact","provider_id":"rea-artifact-graph","provider_version":"1","subject_sha256":"857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e","occurrences":3,"nested_inventory_evidence_id":"ev_cc681c2a03da4e9901275c1425fb1f726cca78bbdbec3defb13b6a0ac8ad156b"}
{"fact":"saved_occurrence[bin/checksum]","file_name":"bin/checksum","present_in_saved_record":true,"saved_logical_path":"bin/checksum","saved_logical_path_equals_derived_name":true,"saved_declared_size":16160,"saved_declared_size_equals_cd_uncompressed_size":true,"saved_compressed_size":2668,"saved_compressed_size_equals_cd_compressed_size":true,"saved_node_sha256":"f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0","saved_node_sha256_equals_recomputed_inflated_sha256":true,"saved_node_size":16160,"saved_node_size_equals_cd_uncompressed_size":true,"saved_executable":true,"saved_encrypted":false,"saved_hash_status":"verified"}
{"fact":"saved_occurrence[README.txt]","file_name":"README.txt","present_in_saved_record":true,"saved_logical_path":"README.txt","saved_logical_path_equals_derived_name":true,"saved_declared_size":84,"saved_declared_size_equals_cd_uncompressed_size":true,"saved_compressed_size":78,"saved_compressed_size_equals_cd_compressed_size":true,"saved_node_sha256":"7d8f6a8de39432f4119f0139c5ef5970c84c23520cfe6b40d19a3653081804d3","saved_node_sha256_equals_recomputed_inflated_sha256":true,"saved_node_size":84,"saved_node_size_equals_cd_uncompressed_size":true,"saved_executable":false,"saved_encrypted":false,"saved_hash_status":"verified"}
{"fact":"saved_occurrence_set_delta","saved_occurrence_paths":[".","README.txt","bin/checksum"],"in_zip_not_in_saved_record":[],"in_saved_record_not_in_zip":["."],"note":"the saved record's '.' occurrence is the archive root itself, not a member"}
{"fact":"spec_derived_field_offsets","source_anchor":"APPNOTE 6.3.10 \u00a74.3.7 local file header field table (S034); \u00a74.3.12 and \u00a74.3.16 field tables (S032)","local_header_fixed_part_bytes":30,"local_header_field_offsets":{"local file header signature":{"offset":0,"width":4},"version needed to extract":{"offset":4,"width":2},"general purpose bit flag":{"offset":6,"width":2},"compression method":{"offset":8,"width":2},"last mod file time":{"offset":10,"width":2},"last mod file date":{"offset":12,"width":2},"crc-32":{"offset":14,"width":4},"compressed size":{"offset":18,"width":4},"uncompressed size":{"offset":22,"width":4},"file name length":{"offset":26,"width":2},"extra field length":{"offset":28,"width":2}},"central_directory_fixed_part_bytes":46,"central_directory_field_offsets":{"central file header signature":{"offset":0,"width":4},"version made by":{"offset":4,"width":2},"version needed to extract":{"offset":6,"width":2},"general purpose bit flag":{"offset":8,"width":2},"compression method":{"offset":10,"width":2},"last mod file time":{"offset":12,"width":2},"last mod file date":{"offset":14,"width":2},"crc-32":{"offset":16,"width":4},"compressed size":{"offset":20,"width":4},"uncompressed size":{"offset":24,"width":4},"file name length":{"offset":28,"width":2},"extra field length":{"offset":30,"width":2},"file comment length":{"offset":32,"width":2},"disk number start":{"offset":34,"width":2},"internal file attributes":{"offset":36,"width":2},"external file attributes":{"offset":38,"width":4},"relative offset of local header":{"offset":42,"width":4}},"eocd_fixed_part_bytes":22,"eocd_field_offsets":{"end of central dir signature":{"offset":0,"width":4},"number of this disk":{"offset":4,"width":2},"number of the disk with the start of the central directory":{"offset":6,"width":2},"total number of entries in the central directory on this disk":{"offset":8,"width":2},"total number of entries in the central directory":{"offset":10,"width":2},"size of the central directory":{"offset":12,"width":4},"offset of start of central directory with respect to the starting disk number":{"offset":16,"width":4},".ZIP file comment length":{"offset":20,"width":2}},"eocd_fixed_part_equals_observed_record_length":true,"central_directory_signature_at_computed_offset":33639248,"central_directory_signature_is_0x02014b50":true,"eocd_signature_at_computed_offset":101010256,"eocd_signature_is_0x06054b50":true,"per_member_offset_checks":[{"file_name":"bin/checksum","crc32_offset":16,"crc32_value_at_computed_offset":3017776807,"crc32_equals_record_crc32":true,"compressed_size_offset":20,"compressed_size_value_at_computed_offset":2668,"uncompressed_size_offset":24,"uncompressed_size_value_at_computed_offset":16160,"file_name_length_offset":28,"file_name_length_value_at_computed_offset":12,"file_name_length_equals_record":true,"relative_offset_of_local_header_offset":42,"relative_offset_of_local_header_value_at_computed_offset":0,"relative_offset_equals_record":true},{"file_name":"README.txt","crc32_offset":16,"crc32_value_at_computed_offset":1923438513,"crc32_equals_record_crc32":true,"compressed_size_offset":20,"compressed_size_value_at_computed_offset":78,"uncompressed_size_offset":24,"uncompressed_size_value_at_computed_offset":84,"file_name_length_offset":28,"file_name_length_value_at_computed_offset":10,"file_name_length_equals_record":true,"relative_offset_of_local_header_offset":42,"relative_offset_of_local_header_value_at_computed_offset":2710,"relative_offset_equals_record":true}]}
```

**The readout stdout's own measurement** (command and exact output; the same bytes the block above shows):

```
$ python3 -B readout.py . > readout.stdout.txt && wc -l readout.stdout.txt && sha256sum readout.stdout.txt
17 readout.stdout.txt
ccaffa322c49d1850fb7da86dc9221ea3bd73c8e3db81cc2ce9be6a1e5b40dc5  readout.stdout.txt
```

**The script's own measurement** (command and exact output):

```
$ sha256sum readout.py
8dbefe4dae2fd170d4bd658c4d1111e66a15b266687fe586e385d9aab74c367f  readout.py
$ wc -l readout.py
329 readout.py
```

**The APPNOTE snapshot's own measurement** (command and exact output; the snapshot the §Sources quotes are taken from):

```
$ wc -c .ufo/waves/round-63/source-snapshots/appnote.txt
174585 .ufo/waves/round-63/source-snapshots/appnote.txt
$ sha256sum .ufo/waves/round-63/source-snapshots/appnote.txt
0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6  .ufo/waves/round-63/source-snapshots/appnote.txt
```

**The excluded zipfile snapshot's own measurement** (command and exact output; the snapshot of the page screened out in this round — see §Sources):

```
$ wc -c .ufo/waves/round-63/source-snapshots/zipfile.html
139782 .ufo/waves/round-63/source-snapshots/zipfile.html
$ sha256sum .ufo/waves/round-63/source-snapshots/zipfile.html
9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739  .ufo/waves/round-63/source-snapshots/zipfile.html
```

**The APPNOTE revision facts** (command and exact output; the version, status and revision date this entry states are read from the snapshot's own header lines):

```
$ tr -d '\r' < .ufo/waves/round-63/source-snapshots/appnote.txt | head -5
File:    APPNOTE.TXT - .ZIP File Format Specification
Version: 6.3.10 
Status: FINAL - replaces version 6.3.9
Revised: Nov 01, 2022
Copyright (c) 1989 - 2014, 2018, 2019, 2020, 2022 PKWARE Inc., All Rights Reserved.
```

**The quoted text's word counts** (command and exact output; every quote used in §Sources is 25 whitespace-separated words or fewer):

```
$ printf '%s\n' "central file header signature 4 bytes (0x02014b50)" | wc -w
7
$ printf '%s\n' "crc-32 4 bytes compressed size 4 bytes uncompressed size 4 bytes file name length 2 bytes extra field length 2 bytes" | wc -w
21
$ printf '%s\n' "local file header signature 4 bytes (0x04034b50)" | wc -w
7
$ printf '%s\n' "file name length 2 bytes extra field length 2 bytes" | wc -w
10
$ printf '%s\n' "end of central dir signature 4 bytes (0x06054b50)" | wc -w
8
$ printf '%s\n' "total number of entries in the central directory on this disk 2 bytes total number of entries in the central directory 2 bytes" | wc -w
23
$ printf '%s\n' "This is the offset from the start of the first disk on which this file appears, to where the local header SHOULD be found." | wc -w
24
$ printf '%s\n' "All values MUST be stored in little-endian byte order unless otherwise specified in this document for a specific data element." | wc -w
20
$ printf '%s\n' "If bit 3 of the general purpose flag is set, this field is set to zero in the local header and the correct" | wc -w
23
$ printf '%s\n' "value is put in the data descriptor and in the central directory." | wc -w
12
```

### Code — `readout.py` (complete)

```python
#!/usr/bin/env python3
"""Manual central-directory readout for the round-63 C06 candidate entry.

Usage:  python3 -B readout.py <repo-root> [--fact ID]

Reads local bytes and JSON only: no ZIP is extracted to disk, no member is
executed, no producer is called, no network is used, no verifier source is
read. Every value is derived from the fixture bytes by struct reads; the
comparisons against truth.json and against the saved record are printed
after the derivation, so the oracle never feeds a derived value.

Each stdout line is one JSON object carrying a stable "fact" id, so a citing
entry can name the single command that prints any one value.
"""
import binascii
import hashlib
import json
import os
import struct
import sys
import zlib

ROOT = sys.argv[1]
ONLY = sys.argv[3] if len(sys.argv) > 3 and sys.argv[2] == "--fact" else None
ZIP_REL = "corpus/fixtures/archive-r2/fixture.zip"
TRUTH_REL = "corpus/fixtures/archive-r2/truth.json"
RECORD_REL = "corpus/live/runs/20261012T164246Z/artifact-inspection.json"
EOCD_SIG, CDH_SIG, LFH_SIG = 0x06054B50, 0x02014B50, 0x04034B50

# Field order and widths transcribed from the PKWARE APPNOTE field tables
# (S032: §4.3.12 central directory file header, §4.3.16 end of central
# directory record; S034: §4.3.7 local file header). The offsets below are COMPUTED by summing those widths.
CD_FIELDS = [("central file header signature", 4), ("version made by", 2),
             ("version needed to extract", 2), ("general purpose bit flag", 2),
             ("compression method", 2), ("last mod file time", 2),
             ("last mod file date", 2), ("crc-32", 4), ("compressed size", 4),
             ("uncompressed size", 4), ("file name length", 2),
             ("extra field length", 2), ("file comment length", 2),
             ("disk number start", 2), ("internal file attributes", 2),
             ("external file attributes", 4),
             ("relative offset of local header", 4)]
EOCD_FIELDS = [("end of central dir signature", 4), ("number of this disk", 2),
               ("number of the disk with the start of the central directory", 2),
               ("total number of entries in the central directory on this disk", 2),
               ("total number of entries in the central directory", 2),
               ("size of the central directory", 4),
               ("offset of start of central directory with respect to the starting disk number", 4),
               (".ZIP file comment length", 2)]
LFH_FIELDS = [("local file header signature", 4), ("version needed to extract", 2),
              ("general purpose bit flag", 2), ("compression method", 2),
              ("last mod file time", 2), ("last mod file date", 2), ("crc-32", 4),
              ("compressed size", 4), ("uncompressed size", 4),
              ("file name length", 2), ("extra field length", 2)]


def read(rel):
    with open(os.path.join(ROOT, rel), "rb") as handle:
        return handle.read()


def u16(buf, off):
    return struct.unpack_from("<H", buf, off)[0]


def u32(buf, off):
    return struct.unpack_from("<I", buf, off)[0]


def offsets(fields):
    out, pos = {}, 0
    for name, width in fields:
        out[name] = {"offset": pos, "width": width}
        pos += width
    return out, pos


def crc32(data):
    return binascii.crc32(data) & 0xFFFFFFFF


facts = []


def fact(fid, obj):
    facts.append((fid, obj))


zip_bytes = read(ZIP_REL)
fact("archive", {"fact": "archive", "path": ZIP_REL, "bytes": len(zip_bytes),
                  "sha256": hashlib.sha256(zip_bytes).hexdigest()})

# ---- end of central directory record (APPNOTE §4.3.16) ----
eocd_off = zip_bytes.rfind(struct.pack("<I", EOCD_SIG))
if eocd_off < 0:
    raise SystemExit("no end-of-central-directory signature found")
eocd = {"eocd_offset": eocd_off, "eocd_offset_from_end": len(zip_bytes) - eocd_off,
        "eocd_signature_hex": zip_bytes[eocd_off:eocd_off + 4].hex(),
        "number_of_this_disk": u16(zip_bytes, eocd_off + 4),
        "number_of_disk_with_start_of_cd": u16(zip_bytes, eocd_off + 6),
        "total_entries_in_cd_on_this_disk": u16(zip_bytes, eocd_off + 8),
        "total_entries_in_cd": u16(zip_bytes, eocd_off + 10),
        "size_of_central_directory": u32(zip_bytes, eocd_off + 12),
        "offset_of_start_of_cd": u32(zip_bytes, eocd_off + 16),
        "zip_file_comment_length": u16(zip_bytes, eocd_off + 20)}
eocd["zip_file_comment_hex"] = zip_bytes[eocd_off + 22:
                                         eocd_off + 22 + eocd["zip_file_comment_length"]].hex()
fact("eocd", dict({"fact": "eocd"}, **eocd))

# ---- central directory (APPNOTE §4.3.12) ----
cd_off, cd_size = eocd["offset_of_start_of_cd"], eocd["size_of_central_directory"]
cd_end = cd_off + cd_size
members, pos, index = [], cd_off, 0
while pos < cd_end:
    if u32(zip_bytes, pos) != CDH_SIG:
        raise SystemExit("bad central directory signature at %d" % pos)
    name_len, extra_len, comment_len = u16(zip_bytes, pos + 28), u16(zip_bytes, pos + 30), u16(zip_bytes, pos + 32)
    members.append({
        "index": index, "cd_header_offset": pos,
        "cd_header_signature_hex": zip_bytes[pos:pos + 4].hex(),
        "version_made_by": u16(zip_bytes, pos + 4),
        "version_needed_to_extract": u16(zip_bytes, pos + 6),
        "general_purpose_bit_flag": u16(zip_bytes, pos + 8),
        "compression_method": u16(zip_bytes, pos + 10),
        "last_mod_file_time": u16(zip_bytes, pos + 12),
        "last_mod_file_date": u16(zip_bytes, pos + 14),
        "crc32": u32(zip_bytes, pos + 16), "crc32_hex": "%08x" % u32(zip_bytes, pos + 16),
        "compressed_size": u32(zip_bytes, pos + 20),
        "uncompressed_size": u32(zip_bytes, pos + 24),
        "file_name_length": name_len, "extra_field_length": extra_len,
        "file_comment_length": comment_len, "disk_number_start": u16(zip_bytes, pos + 34),
        "internal_file_attributes": u16(zip_bytes, pos + 36),
        "external_file_attributes": u32(zip_bytes, pos + 38),
        "relative_offset_of_local_header": u32(zip_bytes, pos + 42),
        "file_name": zip_bytes[pos + 46:pos + 46 + name_len].decode("utf-8"),
        "file_name_bytes_hex": zip_bytes[pos + 46:pos + 46 + name_len].hex(),
        "extra_field_hex": zip_bytes[pos + 46 + name_len:pos + 46 + name_len + extra_len].hex(),
        "file_comment_hex": zip_bytes[pos + 46 + name_len + extra_len:
                                      pos + 46 + name_len + extra_len + comment_len].hex()})
    pos += 46 + name_len + extra_len + comment_len
    index += 1
fact("central_directory", {
    "fact": "central_directory", "cd_offset": cd_off, "cd_size": cd_size,
    "cd_end_offset": cd_end,
    "cd_byte_range_half_open": [cd_off, cd_end],
    "cd_byte_range_inclusive": [cd_off, cd_end - 1],
    "cd_end_equals_eocd_offset": cd_end == eocd_off,
    "eocd_total_entries_matches_parsed_entries": eocd["total_entries_in_cd"] == len(members),
    "eocd_entries_on_this_disk_matches_parsed_entries":
        eocd["total_entries_in_cd_on_this_disk"] == len(members),
    "parsed_entries": len(members)})

for member in members:
    fid = "member_cd[%s]" % member["file_name"]
    fact(fid, dict({"fact": fid}, **member))

# ---- local header + inflated payload ----
lfh_offsets, lfh_fixed = offsets(LFH_FIELDS)
for member in members:
    lfh_off = member["relative_offset_of_local_header"]
    # name/extra lengths read at the offsets COMPUTED from the §4.3.7 widths
    lfh_name_len = u16(zip_bytes, lfh_off + lfh_offsets["file name length"]["offset"])
    lfh_extra_len = u16(zip_bytes, lfh_off + lfh_offsets["extra field length"]["offset"])
    data_off = lfh_off + lfh_fixed + lfh_name_len + lfh_extra_len
    lfh_name = zip_bytes[lfh_off + lfh_fixed:lfh_off + lfh_fixed + lfh_name_len].decode("utf-8")
    raw = zip_bytes[data_off:data_off + member["compressed_size"]]
    if member["compression_method"] == 8:
        plain = zlib.decompress(raw, -15)
    elif member["compression_method"] == 0:
        plain = raw
    else:
        raise SystemExit("unhandled compression method %d" % member["compression_method"])
    crc = crc32(plain)
    fid = "member_local[%s]" % member["file_name"]
    fact(fid, {"fact": fid, "file_name": member["file_name"], "local_header_offset": lfh_off,
               "local_header_signature_hex": zip_bytes[lfh_off:lfh_off + 4].hex(),
               "local_header_signature_is_lfh": u32(zip_bytes, lfh_off) == LFH_SIG,
               "local_header_file_name": lfh_name,
               "local_header_name_equals_cd_name": lfh_name == member["file_name"],
               "local_header_file_name_length": lfh_name_len,
               "local_header_extra_field_length": lfh_extra_len,
               "local_header_name_length_equals_cd_name_length":
                   lfh_name_len == member["file_name_length"],
               "payload_offset": data_off,
               "payload_bytes_read": len(raw),
               "payload_bytes_equal_cd_compressed_size": len(raw) == member["compressed_size"],
               "inflated_bytes": len(plain),
               "inflated_bytes_equal_cd_uncompressed_size":
                   len(plain) == member["uncompressed_size"],
               "inflated_sha256": hashlib.sha256(plain).hexdigest(),
               "inflated_crc32": crc, "inflated_crc32_hex": "%08x" % crc,
               "inflated_crc32_equals_cd_crc32": crc == member["crc32"]})

# ---- truth.json comparison ----
truth = json.loads(read(TRUTH_REL).decode("utf-8"))
truth_by_path = {m["path"]: m for m in truth["members"]}
inflated_sha = {o["file_name"]: o["inflated_sha256"]
                for f, o in facts if f.startswith("member_local[")}
fact("truth_archive_level", {
    "fact": "truth_archive_level",
    "archive_sha256_equals_truth":
        hashlib.sha256(zip_bytes).hexdigest() == truth["archive_sha256"],
    "archive_size_equals_truth": len(zip_bytes) == truth["archive_size"]})
for member in members:
    t = truth_by_path.get(member["file_name"])
    fid = "truth_member[%s]" % member["file_name"]
    if t is None:
        fact(fid, {"fact": fid, "file_name": member["file_name"], "present_in_truth": False})
        continue
    fact(fid, {"fact": fid, "file_name": member["file_name"], "present_in_truth": True,
               "size_equals_truth": member["uncompressed_size"] == t["size"],
               "compressed_size_equals_truth": member["compressed_size"] == t["compressed_size"],
               "sha256_equals_truth": inflated_sha[member["file_name"]] == t["sha256"],
               "sha256_source": "recomputed sha256 over the inflated local-header payload"})
fact("truth_member_set_delta", {
    "fact": "truth_member_set_delta",
    "in_zip_not_in_truth": sorted(set(m["file_name"] for m in members) - set(truth_by_path)),
    "in_truth_not_in_zip": sorted(set(truth_by_path) - set(m["file_name"] for m in members))})
fact("truth_build_field", {
    "fact": "truth_build_field",
    "recorded_build_string": truth.get("build"),
    "note": "recorded provenance string read from the oracle file; this entry makes no "
            "claim about the behaviour of any library it names and does not rely on it "
            "for any value"})

# ---- saved record correspondence (observation layer only) ----
record_bytes = read(RECORD_REL)
record = json.loads(record_bytes.decode("utf-8"))
substep = record["normalized_result"]["substeps"][0]["evidence"]["normalized_result"]
occurrences, nodes = substep["occurrences"], substep["nodes"]
sha_by_artifact = {n["artifact_id"]: n["sha256"] for n in nodes}
size_by_artifact = {n["artifact_id"]: n["size"] for n in nodes}
by_path = {occ["logical_path"]: occ for occ in occurrences}
fact("saved_record", {
    "fact": "saved_record", "path": RECORD_REL, "bytes": len(record_bytes),
    "sha256": hashlib.sha256(record_bytes).hexdigest(),
    "evidence_id": record.get("evidence_id"), "operation": record.get("operation"),
    "provider_id": record.get("provider", {}).get("id"),
    "provider_version": record.get("provider", {}).get("version"),
    "subject_sha256": record.get("subject", {}).get("digest", {}).get("sha256"),
    "occurrences": len(occurrences),
    "nested_inventory_evidence_id":
        record["normalized_result"]["substeps"][0].get("evidence_id")})
for member in members:
    occ = by_path.get(member["file_name"])
    fid = "saved_occurrence[%s]" % member["file_name"]
    if occ is None:
        fact(fid, {"fact": fid, "file_name": member["file_name"],
                   "present_in_saved_record": False})
        continue
    fact(fid, {"fact": fid, "file_name": member["file_name"],
               "present_in_saved_record": True, "saved_logical_path": occ["logical_path"],
               "saved_logical_path_equals_derived_name": occ["logical_path"] == member["file_name"],
               "saved_declared_size": occ["declared_size"],
               "saved_declared_size_equals_cd_uncompressed_size":
                   occ["declared_size"] == member["uncompressed_size"],
               "saved_compressed_size": occ["compressed_size"],
               "saved_compressed_size_equals_cd_compressed_size":
                   occ["compressed_size"] == member["compressed_size"],
               "saved_node_sha256": sha_by_artifact.get(occ["artifact_id"]),
               "saved_node_sha256_equals_recomputed_inflated_sha256":
                   sha_by_artifact.get(occ["artifact_id"]) == inflated_sha[member["file_name"]],
               "saved_node_size": size_by_artifact.get(occ["artifact_id"]),
               "saved_node_size_equals_cd_uncompressed_size":
                   size_by_artifact.get(occ["artifact_id"]) == member["uncompressed_size"],
               "saved_executable": occ["executable"], "saved_encrypted": occ["encrypted"],
               "saved_hash_status": occ["hash_status"]})
fact("saved_occurrence_set_delta", {
    "fact": "saved_occurrence_set_delta", "saved_occurrence_paths": sorted(by_path),
    "in_zip_not_in_saved_record": sorted(set(m["file_name"] for m in members) - set(by_path)),
    "in_saved_record_not_in_zip": sorted(set(by_path) - set(m["file_name"] for m in members)),
    "note": "the saved record's '.' occurrence is the archive root itself, not a member"})

# ---- spec-derived field offsets (constants derived, not assumed) ----
cd_offsets, cd_fixed = offsets(CD_FIELDS)
eocd_offsets, eocd_fixed = offsets(EOCD_FIELDS)
lfh_offsets_all, lfh_fixed_all = offsets(LFH_FIELDS)
cd_checks = []
for member in members:
    base = member["cd_header_offset"]
    cd_checks.append({
        "file_name": member["file_name"],
        "crc32_offset": cd_offsets["crc-32"]["offset"],
        "crc32_value_at_computed_offset": u32(zip_bytes, base + cd_offsets["crc-32"]["offset"]),
        "crc32_equals_record_crc32":
            u32(zip_bytes, base + cd_offsets["crc-32"]["offset"]) == member["crc32"],
        "compressed_size_offset": cd_offsets["compressed size"]["offset"],
        "compressed_size_value_at_computed_offset":
            u32(zip_bytes, base + cd_offsets["compressed size"]["offset"]),
        "uncompressed_size_offset": cd_offsets["uncompressed size"]["offset"],
        "uncompressed_size_value_at_computed_offset":
            u32(zip_bytes, base + cd_offsets["uncompressed size"]["offset"]),
        "file_name_length_offset": cd_offsets["file name length"]["offset"],
        "file_name_length_value_at_computed_offset":
            u16(zip_bytes, base + cd_offsets["file name length"]["offset"]),
        "file_name_length_equals_record":
            u16(zip_bytes, base + cd_offsets["file name length"]["offset"]) == member["file_name_length"],
        "relative_offset_of_local_header_offset": cd_offsets["relative offset of local header"]["offset"],
        "relative_offset_of_local_header_value_at_computed_offset":
            u32(zip_bytes, base + cd_offsets["relative offset of local header"]["offset"]),
        "relative_offset_equals_record":
            u32(zip_bytes, base + cd_offsets["relative offset of local header"]["offset"])
            == member["relative_offset_of_local_header"]})
fact("spec_derived_field_offsets", {
    "fact": "spec_derived_field_offsets",
    "source_anchor": "APPNOTE 6.3.10 §4.3.7 local file header field table (S034); "
                      "§4.3.12 and §4.3.16 field tables (S032)",
    "local_header_fixed_part_bytes": lfh_fixed_all,
    "local_header_field_offsets": lfh_offsets_all,
    "central_directory_fixed_part_bytes": cd_fixed,
    "central_directory_field_offsets": cd_offsets, "eocd_fixed_part_bytes": eocd_fixed,
    "eocd_field_offsets": eocd_offsets,
    "eocd_fixed_part_equals_observed_record_length":
        eocd_fixed == eocd["eocd_offset_from_end"] - eocd["zip_file_comment_length"],
    "central_directory_signature_at_computed_offset": u32(zip_bytes, cd_off),
    "central_directory_signature_is_0x02014b50": u32(zip_bytes, cd_off) == CDH_SIG,
    "eocd_signature_at_computed_offset": u32(zip_bytes, eocd_off),
    "eocd_signature_is_0x06054b50": u32(zip_bytes, eocd_off) == EOCD_SIG,
    "per_member_offset_checks": cd_checks})

if ONLY is not None:
    for fid, obj in facts:
        if fid == ONLY:
            print(json.dumps(obj, separators=(",", ":"), sort_keys=False))
            break
    else:
        raise SystemExit("unknown fact id: %s" % ONLY)
else:
    for fid, obj in facts:
        print(json.dumps(obj, separators=(",", ":"), sort_keys=False))
```

## Sources

- **S032** (spec, tier A, opened 2026-10-23) — PKWARE APPNOTE.TXT, `.ZIP` File Format Specification, <https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT>. Version 6.3.10, status FINAL, revised Nov 01 2022 (the revision facts are read from the snapshot's own header lines; the command and its output are in §Reproduce). Snapshot: `.ufo/waves/round-63/source-snapshots/appnote.txt`, sha256 `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6` (174585 bytes, the served bytes; measured by `wc -c` and `sha256sum` in §Reproduce). Located quotes used here, each verbatim in the snapshot and 25 words or fewer:
  - §4.3.12: "central file header signature 4 bytes (0x02014b50)"
  - §4.3.12: "crc-32 4 bytes compressed size 4 bytes uncompressed size 4 bytes file name length 2 bytes extra field length 2 bytes"
  - §4.3.16: "end of central dir signature 4 bytes (0x06054b50)"
  - §4.3.16: "total number of entries in the central directory on this disk 2 bytes total number of entries in the central directory 2 bytes"
  - §4.4.7: "If bit 3 of the general purpose flag is set, this field is set to zero in the local header and the correct"
  - §4.4.7: "value is put in the data descriptor and in the central directory."
  - §4.4.16: "This is the offset from the start of the first disk on which this file appears, to where the local header SHOULD be found."
  - §4.3.3: "All values MUST be stored in little-endian byte order unless otherwise specified in this document for a specific data element."
  The row's scope is the central directory file header and end-of-central-directory record field layout and the field meanings above. It is not cited for archive semantics beyond those fields, for the local file header layout (that is S034), for ZIP64, or for any provider's behavior.
- **S033** (own-work, tier A; registry id assigned by L1 at the round-63 append) — the authored archive bytes, the authored oracle and the saved record: `corpus/fixtures/archive-r2/fixture.zip` (sha256 `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e`, 2964 bytes), `corpus/fixtures/archive-r2/truth.json` (sha256 `7df773bf46b7c1273f8c3402b7825e7dacbb7f990c7d7ef41f30917c94726e68`), `corpus/live/runs/20261012T164246Z/artifact-inspection.json` (sha256 `2fec924b5217885674149b6a516970f419a8e731c8e6e49eab178a4f065f3380`), all byte-identical at base commit `55bcb6e1aeb4d42923a4e98db6580f67142b41ac`. The oracle's and the record's literal field values are items 10–16 and the recorded-provenance note above; the byte-derived values are item 1, items 3–9. Proposed registry row text for L1 (contract v1, 11 columns): `| S033 | Authored archive-r2 bytes and the saved archive inventory record — `corpus/fixtures/archive-r2/fixture.zip`, `corpus/fixtures/archive-r2/truth.json`, `corpus/live/runs/20261012T164246Z/artifact-inspection.json` | own-work | A | byte content of one authored ZIP archive and the literal saved fields of one archive inventory record for it, at base commit 55bcb6e1aeb4d42923a4e98db6580f67142b41ac; added scope is central-directory-to-oracle-to-saved-record correspondence, not provider accuracy or completeness | fixture sha256 857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e; truth.json sha256 7df773bf46b7c1273f8c3402b7825e7dacbb7f990c7d7ef41f30917c94726e68; saved record sha256 2fec924b5217885674149b6a516970f419a8e731c8e6e49eab178a4f065f3380, Evidence ev_5cc39f356009773bb3d8a214ec39536a99f0799f6709f4cd7bb3badb33c6cf7d, nested ev_cc681c2a03da4e9901275c1425fb1f726cca78bbdbec3defb13b6a0ac8ad156b | A byte readout of one archive's central directory can be checked field by field against an independent oracle and against one saved record's literal fields, without claiming the record is complete or authentic. | mined | 2026-10-23 | on-release | corpus/knowledge/round-63-zip-central-directory-evidence.md |` (landed `mined` with this used-by at the round-63 append; flip logged old→new in the round lesson).
- **S034** (spec, tier A; registry id assigned by L1 at the round-63 append, superseding S032's narrower scope) — the same PKWARE APPNOTE.TXT document, <https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT>, same snapshot `.ufo/waves/round-63/source-snapshots/appnote.txt` (sha256 `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`, 174585 bytes). Scope: the local file header record field layout. Anchor: §4.3.7. Located quotes used here, each verbatim in the snapshot and 25 words or fewer:
  - §4.3.7: "local file header signature 4 bytes (0x04034b50)"
  - §4.3.7: "file name length 2 bytes extra field length 2 bytes"
  These two quotes are the only source this entry rests on for the local-header layout claims (the `spec_derived_field_offsets` fact and the two `member_local` member facts, items 8 and 9). Registry row as landed at the round-63 append (`corpus/SOURCES.md` S034; contract v1, 11 columns): `| S034 | PKWARE APPNOTE.TXT — .ZIP File Format Specification — https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT | spec | A | local file header record field layout for one authored ZIP archive: signature value, field order, length fields and the fixed header size | §4.3.7; version 6.3.10 (revised Nov 01, 2022) | The local file header is a fixed 30-byte record whose file name length sits at offset 26 and whose extra field length sits at offset 28, so a byte readout can locate each member payload from the header's own field widths. | mined | 2026-10-23 | on-release | corpus/knowledge/round-63-zip-central-directory-evidence.md |` (landed `mined` with this used-by at the round-63 append; flip logged old→new in the round lesson).
- **S035** (own-work, tier A; registry id assigned by L1 at the round-63 append) — the run's own ledger: `corpus/live/runs/20261012T164246Z/LEDGER.md` (sha256 `05042a555f91511c9c191565d92f83527f54d1c9b14de331587f4cbffff9e6cb`, 3959 bytes — derived by `$ wc -c < corpus/live/runs/20261012T164246Z/LEDGER.md` → `3959` and `$ sha256sum corpus/live/runs/20261012T164246Z/LEDGER.md` → `05042a555f91511c9c191565d92f83527f54d1c9b14de331587f4cbffff9e6cb`, run 2026-10-24 at the aaa0463 tip), byte-identical at base commit `55bcb6e1aeb4d42923a4e98db6580f67142b41ac`. Scope: the recorded layer for the producer invocation that produced the saved record named under S033 — the `npx -y rea-agents@6.4.0 inspect-artifact …` command and its exit 0, the Evidence IDs, and the fixture digest. This entry credits the ledger with that recorded attribution only and derives no value from it. Proposed registry row text for L1 (contract v1, 11 columns): `| S035 | Run ledger for the saved archive inventory record — `corpus/live/runs/20261012T164246Z/LEDGER.md` | own-work | A | the recorded layer for the producer invocation that produced the saved archive inventory record named under S033, at base commit 55bcb6e1aeb4d42923a4e98db6580f67142b41ac | file sha256 05042a555f91511c9c191565d92f83527f54d1c9b14de331587f4cbffff9e6cb, 3959 bytes; the recorded command, its exit status and the Evidence IDs it lists | Which recorded run produced the saved archive inventory record, as the run's own ledger states it, without that attribution establishing origin or authenticity of the record's contents. | mined | 2026-10-23 | on-release | corpus/knowledge/round-63-zip-central-directory-evidence.md |` (landed `mined` with this used-by at the round-63 append; flip logged old→new in the round lesson).
- No fifth source is cited: S032, S033, S034 and S035 above are this entry's complete registry basis. The Python `zipfile` documentation was **screened and excluded** in this round: the readout reads the archive's bytes with `struct` and inflates with `zlib`, imports no `zipfile`, and credits no `zipfile` behavior. The one place a library name appears is the oracle's recorded `build` string, printed above as a recorded field and relied on for no value — this entry makes no claim about what any library named there does, so the exclusion stands and no docs row is needed. The excluded page's own snapshot is `.ufo/waves/round-63/source-snapshots/zipfile.html` (sha256 `9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739`, accessed 2026-10-23); it is not cited as support for any claim.

## Sentence-to-output inventory (Q11)

Every factual sentence above is of one of two kinds, and the split is stated exactly here rather than claimed universally. **Derived** — the value is produced by a command whose output is printed in the entry: the readout's own `--fact` command form `python3 -B readout.py <repo-root> --fact '<id>'`, run from the lane root with the script of §Reproduce, where each id's line is reproduced verbatim in that item's block and again in the full stdout above; and the file-measurement commands (`sha256sum`, `wc -c`, `wc -l`, `head`) whose outputs are printed in §Reproduce for the script, the stdout, the APPNOTE snapshot, the zipfile snapshot and the fixture/oracle/record/ledger files. The pointer is the `fact` id and the field path inside its JSON object, or the named measurement command and its printed output. **Recorded** — the value is read from a named file and is not re-derived: the saved record's Evidence IDs, operation, provider id and version, subject digest and `executable`/`encrypted`/`hash_status` values (S033), the run ledger's recorded producer invocation (S035), the oracle's recorded values including its `build` string (S033), and the APPNOTE document's own version/status/revision-date header lines, which are read from the snapshot by the printed `tr -d '\r' … | head -5` command and are **recorded** from that document rather than derived from the archive. No other kind of value is asserted, and the sentence above makes no claim beyond these two kinds.

| # | Sentence (short form) | command | fact id / field |
|---|---|---|---|
| 1 | archive byte length and SHA-256 | `--fact 'archive'` | `archive` → `bytes`, `sha256` |
| 2 | the four files are byte-identical at base commit and in the tree | `git show <base>:<path> \| sha256sum` (four invocations) and `sha256sum <path> …` (one invocation, four paths) | command output in item 2 |
| 3 | EOCD offset, distance from end, signature, disk fields, counts, CD size/offset, comment | `--fact 'eocd'` | `eocd` → `eocd_offset`, `eocd_offset_from_end`, `eocd_signature_hex`, `number_of_this_disk`, `number_of_disk_with_start_of_cd`, `total_entries_in_cd_on_this_disk`, `total_entries_in_cd`, `size_of_central_directory`, `offset_of_start_of_cd`, `zip_file_comment_length`, `zip_file_comment_hex` |
| 4 | CD spans [2828, 2942), ends where the EOCD starts, 2 records parsed, counts agree | `--fact 'central_directory'` | `central_directory` → `cd_offset`, `cd_size`, `cd_end_offset`, `cd_byte_range_half_open`, `cd_byte_range_inclusive`, `cd_end_equals_eocd_offset`, `parsed_entries`, `eocd_total_entries_matches_parsed_entries`, `eocd_entries_on_this_disk_matches_parsed_entries` |
| 5 | fixed 30/46/22-byte records, computed field offsets, signatures at offset 0 | `--fact 'spec_derived_field_offsets'` | `spec_derived_field_offsets` → `local_header_fixed_part_bytes`, `local_header_field_offsets`, `central_directory_fixed_part_bytes`, `central_directory_field_offsets`, `eocd_fixed_part_bytes`, `eocd_field_offsets`, `eocd_fixed_part_equals_observed_record_length`, `central_directory_signature_is_0x02014b50`, `eocd_signature_is_0x06054b50`, `per_member_offset_checks` |
| 6 | first central-directory record: name, offsets, sizes, CRC-32, lengths, method, flags | `--fact 'member_cd[bin/checksum]'` | `member_cd[bin/checksum]` → `file_name`, `file_name_bytes_hex`, `cd_header_offset`, `relative_offset_of_local_header`, `compressed_size`, `uncompressed_size`, `crc32`, `crc32_hex`, `file_name_length`, `extra_field_length`, `file_comment_length`, `compression_method`, `general_purpose_bit_flag`, `extra_field_hex`, `file_comment_hex` |
| 7 | second central-directory record: name, offsets, sizes, CRC-32, lengths, method, flags | `--fact 'member_cd[README.txt]'` | `member_cd[README.txt]` → same field names as item 6 |
| 8 | first local header: signature, name, name length, payload offset/length, inflated length/digest/CRC-32 | `--fact 'member_local[bin/checksum]'` | `member_local[bin/checksum]` → `local_header_signature_hex`, `local_header_signature_is_lfh`, `local_header_file_name`, `local_header_name_equals_cd_name`, `local_header_file_name_length`, `local_header_name_length_equals_cd_name_length`, `payload_offset`, `payload_bytes_read`, `payload_bytes_equal_cd_compressed_size`, `inflated_bytes`, `inflated_bytes_equal_cd_uncompressed_size`, `inflated_sha256`, `inflated_crc32`, `inflated_crc32_equals_cd_crc32` |
| 9 | second local header: signature, name, name length, payload offset/length, inflated length/digest/CRC-32 | `--fact 'member_local[README.txt]'` | `member_local[README.txt]` → same field names as item 8 |
| 10 | archive digest and size equal the oracle's | `--fact 'truth_archive_level'` | `truth_archive_level` → `archive_sha256_equals_truth`, `archive_size_equals_truth` |
| 11 | both members' names, sizes, compressed sizes and digests equal the oracle's | `--fact 'truth_member[bin/checksum]'`, `--fact 'truth_member[README.txt]'` | `truth_member[…]` → `size_equals_truth`, `compressed_size_equals_truth`, `sha256_equals_truth`, `sha256_source` |
| 12 | the member name sets agree exactly | `--fact 'truth_member_set_delta'` | `truth_member_set_delta` → `in_zip_not_in_truth`, `in_truth_not_in_zip` |
| RP | the oracle's recorded `build` string (recorded-provenance note, not an observation) | `--fact 'truth_build_field'` | `truth_build_field` → `recorded_build_string`, `note` |
| 13 | saved record bytes, digest, Evidence IDs, operation, provider, subject digest, occurrence count | `--fact 'saved_record'` | `saved_record` → `bytes`, `sha256`, `evidence_id`, `operation`, `provider_id`, `provider_version`, `subject_sha256`, `occurrences`, `nested_inventory_evidence_id` |
| 14 | saved occurrence for `bin/checksum` and its node | `--fact 'saved_occurrence[bin/checksum]'` | `saved_occurrence[bin/checksum]` → `saved_logical_path`, `saved_logical_path_equals_derived_name`, `saved_declared_size`, `saved_declared_size_equals_cd_uncompressed_size`, `saved_compressed_size`, `saved_compressed_size_equals_cd_compressed_size`, `saved_node_sha256`, `saved_node_sha256_equals_recomputed_inflated_sha256`, `saved_node_size`, `saved_node_size_equals_cd_uncompressed_size`, `saved_executable`, `saved_encrypted`, `saved_hash_status` |
| 15 | saved occurrence for `README.txt` and its node | `--fact 'saved_occurrence[README.txt]'` | `saved_occurrence[README.txt]` → same field names as item 14 |
| 16 | the three saved occurrence paths, `.` being the root | `--fact 'saved_occurrence_set_delta'` | `saved_occurrence_set_delta` → `saved_occurrence_paths`, `in_zip_not_in_saved_record`, `in_saved_record_not_in_zip` |
| 17–20 | the four inferences | the observations above | as cited in each item |
| 21–25 | the unknowns | no output claimed | — |
| 26–33 | the limitations | no output claimed | — |
| S1 | the ten §Sources quotes and their word counts | `printf '%s\n' "<quote>" \| wc -w` (ten invocations) | the `wc -w` outputs in §Reproduce |

## Q13 — no deletion-sensitive guard credit

No verifier, recheck command, comparison tool or automatic checker is credited as a guard of any value in this entry, and none is introduced. The values stated here are of two kinds. The **derived** kind — the archive length and digest, the end-of-central-directory location and counts, the central-directory offset and size, the per-member names, offsets, sizes and CRC-32 values, the local-header names and name lengths, the inflated payload lengths, digests and CRC-32 values, the field offsets computed from the specification's field lists — comes from the command in §Reproduce and the output it printed. The **recorded** kind — the saved record's Evidence IDs, operation, provider id and version, subject digest, and its `executable`, `encrypted` and `hash_status` values, the oracle's recorded values, and the run ledger's recorded producer invocation — is read from the named files, not re-derived, and is labelled as such where it appears. No claim is made that any check detects, verifies or guards any value; the recheck command reproduces the observations, and nothing here is credited to it.

## QUALITY check — decisions, not admission

The table below records the author's reading of unchanged `corpus/QUALITY.md` Q01–Q13, not independent admission authority. The final round-63 Gate in `corpus/lessons/round-63.md` records the named fresh-seat recommendations and L1 admission after any correction; the readout and its recorded output are unchanged by that status transition.

| Q | decision | basis |
|---|---|---|
| Q01 | author-proposed pass; final independent decisions in the round-63 lesson | S032 is a `spec` row opened this round, tier A for the scope used (the central directory file header and end-of-central-directory record field layout), quoted in §Sources with its section anchors and its snapshot digest; S034 is the `spec` row for the local file header record field layout (anchor §4.3.7), quoted there with the same snapshot digest; S033 is the own-work row for the archive bytes, the oracle and the saved record; S035 is the own-work row for the run's ledger. Each load-bearing claim rests on the row whose scope covers it: no local-header-layout claim cites S032, and no central-directory or end-of-central-directory claim cites S034. No claim in this entry rests on a row outside those four. |
| Q02 | pass | the header carries `source:` (four rows — S032 and S034 with the URL, section anchors and snapshot digest, S033 with the fixture/oracle/record paths and their digests, and S035 with the ledger path and its digest), `verified-at:` 2026-10-23 with the base commit, `recheck:` (one runnable command with its stdout digest and line count, plus the per-value form) and `coverage-map: C06`; the anchors are section numbers, not a bare homepage. |
| Q03 | pass | the expected values are derived from the archive's bytes and the specification's field tables; the oracle and the saved record supply the compared side only and never feed a derived value (item 8 and item 9 derive the digests before item 10 and item 11 compare them). |
| Q04 | pass | the analysis is labelled manual (item 29); no tool is credited with a result it did not output; the `rea-agents@6.4.0` run that produced the saved record, as recorded in the run's own `LEDGER.md` (S035), is credited with the record's existence and its literal fields only (item 29, item 13). |
| Q05 | n/a (no readiness or capability claim) | the entry claims no readiness, no producer capability and no current-host state; the saved record is read as a saved file, in the past tense, at its recorded digests. |
| Q06 | pass | the fixture premise is byte-verified here: the archive's length and SHA-256 are derived from its bytes and compared with the oracle (item 1, item 10), and the bytes are shown to be identical at the base commit (item 2). |
| Q07 | n/a (no predicted parser behaviour) | the entry predicts nothing about any parser or provider; the spec-derived offsets are an arithmetic property of the specification's own field lists (item 5), not a prediction about how any implementation reads the file. |
| Q08 | superseded by Q11 | — |
| Q09 | pass | each printed digest binds the bytes it was computed over (item 1, item 8, item 9, item 13 and item 20); no origin, completeness or authenticity claim is made (item 28, item 20); the saved record's bytes are unchanged at the base commit (item 2). |
| Q10 | pass | the scope is this one archive, this one oracle and this one saved record, with one provider id and version and one operation (item 13, items 17–19, item 27); sibling-lane overlap is left with the operator, this entry declares no ownership and cites no other lane's file as support. |
| Q11 | pass | the §Sentence-to-output inventory maps every factual sentence, including the header, source and run-metadata rows, to a command and a printed field or to the recorded file named beside it; each item's block shows the command and its output, and the script, stdout and snapshot measurements are shown with their commands in §Reproduce. |
| Q12 | n/a (no rejected source row cited) | the entry cites no rejected row; the Python `zipfile` documentation was screened and excluded without a registry row, so no reject reason is owed. The oracle's recorded `build` string is printed as a recorded field and relied on for no value, so no claim about any library's behaviour is made and the exclusion stands. |
| Q13 | n/a by construction — no guard credit | no verifier, recheck command, comparison tool or automatic checker is credited or introduced, and no value is presented as covered by any check (§Q13). |
