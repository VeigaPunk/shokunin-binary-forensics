# pe-byte-oracle — round 27

**lane:** pe-byte-oracle  
**result:** PASS  
**evidence_id:** ev_a524338e43a8a20a3fb0f018d46ef2fe06732e323bfb3ce98fd813bd223f50ef  
**operation:** inspect_pe_resources  
**fixture:** `.shokunin/revenger/corpus/fixtures/pe-r27/fixture.exe`  
**method:** independent `struct` decode of on-disk bytes (truth.json not used as source of truth)

## Recomputed

| Field | Value |
|-------|-------|
| file size | 1024 |
| file SHA-256 | `523e6dc1b8cc2b48a636ce3cb93736ce46d4c8d58c594d8d8dd2ed72ca2640bb` |
| DOS magic | `MZ` (0x5A4D) |
| e_lfanew | 0x40 (64) |
| PE signature | `PE\0\0` |
| machine | 0x14C (i386) |
| optional magic | 0x10B (PE32) |
| NumberOfSections | 1 |
| SizeOfOptionalHeader | 224 |
| resource DATA_DIRECTORY file offset | 200 |
| resource DD RVA | 0x2000 (8192) |
| resource DD size | 103 |
| section `.rsrc` VA/raw | VA 0x2000, PointerToRawData 512, SizeOfRawData 512, VirtualSize 103 |
| resource root file offset | 512 |
| type / name / language | 10 (0xA) / 1 / 0x0409 (1033) |
| IMAGE_RESOURCE_DATA_ENTRY file off | 584 |
| payload RVA | 0x2058 |
| payload file offset | 600 |
| payload length | 15 |
| payload ASCII | `REV-R27-PAYLOAD` |
| payload SHA-256 | `0346b578bdfe68866acea157268520567a5d6e96a28ab8a95835569921f088aa` |

## Checks

- [x] MZ present
- [x] PE32 magic 0x10B
- [x] machine 0x14C
- [x] resource DD at file offset 200, RVA 0x2000, size 103
- [x] one type/name/language chain (10, 1, 0x0409)
- [x] payload @ 600 len 15 == `REV-R27-PAYLOAD`
- [x] whole-file and payload SHA-256 as above

## Verdict

**PASS** — all required PE resource geometry and payload bytes match the round-27 contract.
