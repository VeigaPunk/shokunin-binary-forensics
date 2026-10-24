# R63CriticCounts — C06 numeric derivation and scope review

## Result and axes

**The archive numbers are numerically SOUND; the candidate still has Q11 derivation holes and a frozen-scope conflict.** No byte-derived member/count/CRC disagreement and no oracle-to-derived-value copying was found. This is a scoped critic finding, not admission or a runtime judgment.

Affected axis: **coverage K / C06** through unchanged Q03, Q10 and Q11. Independence, reproducibility and bounded scope are the review dimensions, not new scored axes. Calibration C3 and firmware C2 were not reviewed.

The draft became available at the final prerequisite check, so this report reviews `/tmp/revenger-r63-entry/candidate.md`, SHA-256 `630b974a51e0f6ab815a5806a0f415b3f07089df91923dde3a78b6fd49904c7e`, reader snapshot `494C`, 672 lines. The intended production entry was still absent. Also reviewed `.ufo/waves/round-63/build/zip-readout.py` and `zip-readout.out`.

## Holes and smallest safe corrections

### H1 — local-header constants are assumed, contrary to “every field offset” (Q11)

Draft lines 63–69 say “every field offset used below” is computed from the specification. `CD_FIELDS` and `EOCD_FIELDS` at 308–323 derive only the central-directory and EOCD layouts. Local-header fixed length **30** and offsets **26**, **28** remain literal constants at 421–424 and 453–455; no local-header field-width table or computed-offset output exists. The payload offsets **42**, **2750**, and member-region lengths are numerically correct, but this does not satisfy Q11's explicit rule that header constants be derived rather than assumed.

**Correction:** add the APPNOTE §4.3.7 local-header width list, compute/print fixed size 30 and name/extra-length offsets 26/28, and use those computed values (or show their byte-read cross-check). Expand the source anchor to that actual scope. My independent width summation gives exactly 30/26/28.

### H2 — source and run metadata carry hashes/counts without their derivation commands (Q11)

- APPNOTE snapshot SHA-256 `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6` appears at lines 1 and 611; its **174585-byte** length appears at 611. No in-entry command hashes or measures that snapshot. The embedded script never reads it.
- Stdout SHA-256 `e112d4092dfa8e3ed5398f07d1222457455ca06a94e01e988a0f58eab4c445ec` and **17-line** count appear at 4 and 225. The producer command and its JSON are present, but no in-entry hashing/counting command produces those two metadata results. `sha256sum readout.py` and `wc -l readout.py` at 250–253 measure the script, not stdout.

These values independently match: they are not numeric errors. The sentence-to-output inventory's “every factual sentence” assertion at 624/670 does not supply the missing commands.

**Correction:** include the actual snapshot byte-count/hash and stdout byte-count/hash commands with their outputs, or explicitly label unsupported metadata as recorded rather than re-derived. Keep `331 readout.py` and script digest as-is; those have their own commands and matched.

### H3 — inclusive CD end offset 2941 is not in command output (Q11)

Lines 47 and 631 state **2828–2941 inclusive**. The cited `central_directory` output contains start 2828, size 114, and exclusive end 2942, but never prints 2941. The arithmetic is correct; Q11 rejects correctness without the in-entry derivation/output for the stated offset.

**Correction:** use the directly printed half-open range `[2828,2942)`, or emit `cd_last_byte_offset = cd_end_offset - 1` with output 2941.

### H4 — working-tree truth digest/byte-preservation claim lacks the working-tree side (Q11 / provenance)

Lines 3 and 26 claim all three inputs are byte-identical at base and in the working tree. Lines 29–34 hash only `git show <base>:<path>`. Current archive and saved-record hashes are computed elsewhere, but the current `truth.json` bytes are only decoded at 481; their hash is never printed or compared by the embedded script. Thus the displayed base hash is not evidence of current oracle byte identity.

**Counterexample from the code:** changing only the oracle's unused `build` string would leave every embedded comparison true and every displayed base-hash output unchanged while invalidating that byte-identity sentence. I did not modify the oracle. Its actual current SHA-256 independently matched the stated base hash.

**Correction:** include a working-tree `sha256sum corpus/fixtures/archive-r2/truth.json` command/output alongside the base command, or explicitly compute both hashes in the readout. Do not credit JSON field equality as byte preservation.

### H5 — ZIP64 absence is stated without an in-entry absence sweep (Q11 / scope precision)

Line 211 asserts “no ZIP64 record is present in the bytes this entry read.” The readout locates EOCD and walks the declared central directory; it has no ZIP64-record search or absence output. None of the listed facts establishes that negative claim.

**Correction:** remove that unnecessary parenthetical, retaining only that ZIP64 is outside the entry's claim. No new parser scope is needed.

### H6 — “every field the oracle records” exceeds the actual comparison (scope precision)

Line 179 says the central-directory view agrees with the oracle “on every field the oracle records.” The script checks archive size/hash, member names, member sizes/compressed sizes/hashes. `truth.json` also records `source_binary_sha256` and `build`; neither is compared or printed by the script. This is a local all-fields overclaim, not evidence of a universal claim about all ZIP implementations.

**Correction:** enumerate the exact checked fields instead of “every field.” Preserve the existing one-fixture limitation.

### H7 — correct byte accounting introduces a forbidden trailing-bytes claim (frozen scope)

Draft item 5 (55–59) and limitation 28 (201) explicitly observe **0 bytes after the EOCD**. Frozen `reports/round-63/claims.md:29–31` excludes “a trailing-bytes claim,” not merely a general trailing-bytes claim. The draft narrows that exclusion to “no general statement” in its output and prose. This is scope drift even though the reported zero is correct.

**Correction:** remove the trailing-byte/whole-file accounting claim and its extra fact, leaving the declared central-directory/EOCD/member correspondence. Do not resolve this by weakening the frozen scope. Admission interpretation remains with L1/canonical judge; no such decision was made here.

## Per-value findings

Common in-entry command: `python3 -B readout.py <repo-root> --fact '<id>'`; each fact below has its command and JSON output in the corresponding draft item. Independent numbers were obtained from fixture bytes **before opening truth.json or the saved record**. Byte intervals below are half-open; numeric field interpretation follows APPNOTE §4.3.7, §4.3.12 and §4.3.16.

| Value / role | Independent result and byte derivation | In-entry evidence / finding |
|---|---|---|
| Archive length | 2964 = `len(bytes)` | `archive`, lines 18–23: matches |
| Archive SHA-256 | `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e` | `archive`: matches; not copied from truth |
| EOCD location | 2942 = last `PK\x05\x06` signature offset | `eocd`, 39–43: matches |
| EOCD distance from file end | 22 = 2964 − 2942 | `eocd`: matches |
| EOCD signature | `504b0506` at [2942,2946) | `eocd`: matches |
| Current disk | 0, [2946,2948), `0000` | `eocd`: matches |
| CD-start disk | 0, [2948,2950), `0000` | `eocd`: matches |
| Entries on this disk | 2, [2950,2952), `0200` | `eocd`: matches; independently walked 2 |
| Total entries | 2, [2952,2954), `0200` | `eocd`: matches; independently walked 2 |
| CD size | 114, [2954,2958), `72000000` | `eocd` / `central_directory`: matches |
| CD start | 2828, [2958,2962), `0c0b0000` | `eocd` / `central_directory`: matches |
| EOCD comment length | 0, [2962,2964), `0000`; empty comment bytes | `eocd`: matches |
| CD exclusive end | 2942 = 2828 + 114 | `central_directory`, 47–51: matches |
| CD inclusive last byte | 2941 = 2942 − 1 | Correct but not printed: H3 |
| Parsed member count | 2 from walk of [2828,2942) | `central_directory`: matches both EOCD counts |
| First CD record start/length | 2828 / 58 = 46 + 12 + 0 + 0 | `member_cd[bin/checksum]`: start and component lengths match |
| First name | `bin/checksum`, hex `62696e2f636865636b73756d` | Name bytes, not truth/record, supply derived side |
| First name/extra/comment lengths | 12 / 0 / 0 from [2856,2862) | `member_cd[bin/checksum]`, 75–79: matches |
| First local-header offset | 0, [2870,2874), `00000000` | Same fact: matches |
| First compressed size | 2668, [2848,2852), `6c0a0000` | Same fact: matches truth and saved occurrence |
| First uncompressed size | 16160, [2852,2856), `203f0000`; inflated length independently 16160 | Same fact / `member_local[bin/checksum]`: matches |
| First CRC-32 | `b3df9ea7` = 3017776807, [2844,2848), `a79edfb3`; recomputed from inflated payload | Both CD and local facts match; absent from truth and saved record |
| First method/flags | 8 / 0 from CD [2838,2840) / [2836,2838) | Same fact: matches |
| First payload start/end | 42 / 2710; 0 + 30 + 12 + 0, then +2668 | `member_local[bin/checksum]`: start/length match; local constants need H1 correction |
| First inflated SHA-256 | `f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0` | `member_local[bin/checksum]`: recomputed; matches truth and saved node |
| Second CD record start/length | 2886 / 56 = 46 + 10 + 0 + 0 | `member_cd[README.txt]`, 83–87: matches |
| Second name | `README.txt`, hex `524541444d452e747874` | Name bytes supply derived side |
| Second name/extra/comment lengths | 10 / 0 / 0 from [2914,2920) | Same fact: matches |
| Second local-header offset | 2710, [2928,2932), `960a0000` | Same fact: matches |
| Second compressed size | 78, [2906,2910), `4e000000` | Same fact: matches truth and saved occurrence |
| Second uncompressed size | 84, [2910,2914), `54000000`; inflated length independently 84 | Same fact / `member_local[README.txt]`: matches |
| Second CRC-32 | `72a557b1` = 1923438513, [2902,2906), `b157a572`; recomputed from inflated payload | Both CD and local facts match; absent from truth and saved record |
| Second method/flags | 8 / 0 from CD [2896,2898) / [2894,2896) | Same fact: matches |
| Second payload start/end | 2750 / 2828; 2710 + 30 + 10 + 0, then +78 | `member_local[README.txt]`: start/length match; H1 applies |
| Second inflated SHA-256 | `7d8f6a8de39432f4119f0139c5ef5970c84c23520cfe6b40d19a3653081804d3` | Same fact: recomputed; matches truth and saved node |
| CD fixed header size/field offsets | 46; CRC16, compressed20, uncompressed24, name-length28, local-offset42 | Width-summed `spec_derived_field_offsets`: matches APPNOTE |
| EOCD fixed header size/field offsets | 22; counts8/10, CD-size12, CD-offset16, comment-length20 | Same fact: matches APPNOTE |
| Local fixed size/field offsets | 30; name-length26, extra-length28 | Numerically correct; not derived in-entry: H1 |
| Seven layout lengths | `[0,2710,118,114,0,22,0]`, sum2964 | Correct for these bytes; frozen scope issue H7 |
| Saved-record byte length/hash | 7692 / `2fec924b5217885674149b6a516970f419a8e731c8e6e49eab178a4f065f3380` | `saved_record`, 143–147: independently matches |
| Saved occurrence count | 3; paths `.`, `README.txt`, `bin/checksum`; non-root members2 | `saved_record` / `saved_occurrence_set_delta`: correctly distinguishes root from member |
| Truth archive/member comparisons | Archive size/hash and both members' name/size/compressed-size/hash all agree | `truth_*`, 111–137: no derived value is sourced from these comparison values |
| Saved size/digest comparisons | Both declared sizes, compressed sizes, node sizes and payload hashes agree | `saved_occurrence[*]`, 151–171: recorded side labeled; derived side independent |
| Script length/hash | 331 lines / `c6b54ccc2529dc7754eaf7ac7d71754d3d157805d050fe3fd5269c7452be829f` | Commands/output at 250–253; matches |
| Stdout length/hash | 17 lines / `e112d4092dfa8e3ed5398f07d1222457455ca06a94e01e988a0f58eab4c445ec` | Independently matches; metadata command hole H2 |
| APPNOTE snapshot length/hash | 174585 / `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6` | Independently matches; metadata command hole H2 |
| Oracle current hash | `7df773bf46b7c1273f8c3402b7825e7dacbb7f990c7d7ef41f30917c94726e68` | Actual match, but current-side derivation absent in-entry: H4 |

## Independence attack and Q10

The embedded script creates archive/CD/local-payload facts at lines 358–478. It first loads the oracle at 481, and first loads the saved record at 507–508. Its size and CRC fields come from raw integer reads, while the payload digest and CRC are recomputed after DEFLATE inflation. The `zip-readout.py` pack also derives its actual values from archive bytes and uses truth only for the expected-side table. No claimed re-derived archive number was traced to a copied oracle or saved-record value.

No universal claim about all ZIP archives or all providers was located in the observed findings: lines 177–181 and 199–205 repeatedly restrict the result to one fixture, one oracle and one saved record; the saved provider/version/IDs are explicitly recorded. H6 is a narrower overstatement of compared fields, and H7 is an explicit frozen-scope conflict. Those should not be confused with a failed CRC or a generic parser counterexample.

## Executed evidence

A bytes-only decoder first ran in the Python evaluation session before the oracle/record were opened; it used little-endian integer reads, walked the CD by declared record lengths (not by oracle member count), inflated both local payloads and recomputed CRC-32/SHA-256. After opening the comparison files, a second bytes-only command used ordered APPNOTE field layouts with `struct.calcsize` prefix widths to reproduce those independently obtained values. That command, `python3 -B -c <independent decoder>`, exited 0 and printed:

```text
fixed_sizes {"central": 46, "eocd": 22, "local": 30}
archive 2964 857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e
eocd_offset 2942
eocd {"cd_disk": 0, "cd_offset": 2828, "cd_size": 114, "comment_size": 0, "disk": 0, "entries_on_disk": 2, "entries_total": 2}
member {"central_offset": 2828, "comment_len": 0, "compressed_size": 2668, "crc32": "b3df9ea7", "crc32_from_payload": "b3df9ea7", "extra_len": 0, "flags": 0, "local_offset": 0, "method": 8, "name": "bin/checksum", "name_len": 12, "payload_end": 2710, "payload_offset": 42, "sha256": "f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0", "uncompressed_size": 16160}
member {"central_offset": 2886, "comment_len": 0, "compressed_size": 78, "crc32": "72a557b1", "crc32_from_payload": "72a557b1", "extra_len": 0, "flags": 0, "local_offset": 2710, "method": 8, "name": "README.txt", "name_len": 10, "payload_end": 2828, "payload_offset": 2750, "sha256": "7d8f6a8de39432f4119f0139c5ef5970c84c23520cfe6b40d19a3653081804d3", "uncompressed_size": 84}
walked_count 2 central_end 2942
```

The complete embedded candidate code was then executed in memory with `python3 -B -c <embedded code> /home/vgpnk/Projects/shokunin/revenger-shokunin`, without creating a script or changing any input. Observed exit 0; stderr empty; 17 stdout lines; stdout digest and 331-line script digest matched the draft. Comparing its member facts against my independently derived CD offsets, local offsets, sizes, name/extra/comment lengths, methods/flags, payload offsets, inflated sizes, CRCs and hashes produced `candidate_member_value_mismatches []`. This was a readout reproduction, not a deletion-sensitive verifier or admission gate.

No production files or existing fixtures/records were edited. No target/member was executed, no runtime judge was invoked, no tools were installed or updated, and no scratch files were created by this critic. Only this assigned report was written. All listed defects are correctable without weakening Q01–Q13 or changing the frozen counting contract.
