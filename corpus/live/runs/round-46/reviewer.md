# Round 46 — non-author LEAF review

**PASS, narrowly:** the saved r42–r45 REA *normalized resource results* agree with independent decoding of these four static PE32+ fixtures. No PE or REA invocation was performed. This is not a pass for producer provenance, the full evidence envelope, or general PE parser correctness.

Read-only command (from any directory):

```sh
python -B /home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/verify_multi_icon_states.py
```

Exit **0**; exact stdout:

```text
PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
```

The verifier reads fixture bytes, saved `inspection.raw.json`, and `producer-receipt.json` for each round. It independently walks the PE32+ resource directory from the PE data-directory RVA via section mapping; compares the decoded format, machine, directory and its location, every reachable directory header, all three leaf type/name/language paths and entry locations, data-entry locations, code pages, payload RVA/offset/size/**SHA-256**, and both ordered group records against matching fields in the saved normalized result. Its derived reachable coverage is eight directory entries and three resources (six directory headers); it checks the normalized coverage claim is `complete` with those counts. It verifies fixture length 1536 and pinned fixture hashes; saved evidence IDs, operation, subject and artifact digests/locations; and receipt exit code, fixture hash, evidence ID, and SHA-256 of exact saved raw JSON bytes. These are internal consistency checks, not independent observation of production.

| Fixture against r42 | Exact changed byte | Second ordered image state (ID, declared size, candidates, same-language index, size match) |
|---|---|---|
| r42 baseline | — | `(2,48,(1,),1,true)` |
| r43 | 928: `02→03` | `(3,48,(),null,null)` |
| r44 | 924: `30→2f` | `(2,47,(1,),1,false)` |
| r45 | 640: `09→0c` | `(2,48,(1,),null,null)` |

The first ordered image is byte-decoded identically across all four reports: ID1, declared 48, candidate `[0]`, same-language `0`, size match `true`. Both RT_ICON payload hashes remain identical across fixtures. The four derived two-image state tuples are pairwise distinct. The verifier also copies the r45 saved report, forges the *second* `same_language_resource_index` to `1`, and requires a mismatch against independently decoded groups; the forged result is rejected by this in-memory equality test, not by a rerun of REA or the file-reading `check()` function.

**Bounds and remaining gaps:** Only these four pinned 1536-byte, numeric-ID, depth-three fixture trees are covered. `decode()` counts reachable entries, not all unreferenced bytes/possible alternative resource directories, and does not enforce PE section virtual-size bounds, section-table bounds, nonoverlapping mappings/structures or REA's general overlap policy; its `file_offset()` uses section raw size. These do not negate the pinned fixture comparison but cannot certify arbitrary or malformed PE inputs. The normalized-result `limitations` field and additional normalized fields, plus the evidence envelope's provider, parameters, confidence, authority, paths/locations, evidence links, raw_result and limitations, are **not** wholly compared/validated. The receipt command string, actual invocation, stdout origin, REA package/version, and history cannot be authenticated from matching saved hashes/IDs. Icon payloads are hashed but not decoded; Windows language fallback, OS icon selection/display, execution, and native-provider readiness are untested.
