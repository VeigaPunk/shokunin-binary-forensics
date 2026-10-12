# pe-relation-check — round 27

Lane: pe-relation-check  
Evidence id: `ev_a524338e43a8a20a3fb0f018d46ef2fe06732e323bfb3ce98fd813bd223f50ef`  
Operation: `inspect_pe_resources`  
Claimed relation: the single reported resource identity maps to the authored payload bytes.

## Observation (recomputed)

- Fixture path: `.shokunin/revenger/corpus/fixtures/pe-r27/fixture.exe` (1024 bytes).
- Slice `fixture.exe[600:615]` (15 bytes):
  - hex: `5245562d5232372d5041594c4f4144`
  - ascii: `REV-R27-PAYLOAD`
  - sha256: `0346b578bdfe68866acea157268520567a5d6e96a28ab8a95835569921f088aa`

## Observation (Evidence normalized_result)

- Single resource in `resources[]` (index 0): type id 10, name id 1, language id 1033.
- Payload location: offset **600**, bytes **15**.
- Payload sha256: `0346b578bdfe68866acea157268520567a5d6e96a28ab8a95835569921f088aa`.

## Comparison

| field | recomputed slice | Evidence payload | match |
|-------|------------------|------------------|-------|
| offset | 600 (slice start) | 600 | yes |
| length | 15 | 15 | yes |
| sha256 | 0346b578…f088aa | 0346b578…f088aa | yes |

## Inference vs unknown

- **Observation:** byte identity of `fixture.exe[600:615]` equals Evidence payload location + sha256; only one resource is listed.
- **Inference (weak, structural):** that single resource identity (10 / 1 / 1033) is the one that owns this payload entry — consistent with Evidence tree + truth relation text; not independently re-parsed from PE directory here (no REA / no PE re-walk in this leaf).
- **Unknown:** runtime load behavior, language fallback, and any non-table mapping beyond the static inventory.

## Verdict

**PASS** — recomputed authored payload bytes at offset 600 length 15 match the single reported resource payload location and sha256 in Evidence.
