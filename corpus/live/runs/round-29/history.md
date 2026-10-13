# Round 29 history cross-check — scope of round 28 one-byte control

Scope: independent raw-byte cross-check of the prior round only. No fixture was changed and no REA command was run.

## Evidence pointers

- Round 28 declaration/result and scope: `.shokunin/revenger/LOG.md`, “Round 28 declaration” and “Round 28 result”.
- Prior comparison: `.shokunin/revenger/corpus/live/runs/round-28/LEDGER.md`.
- Baseline fixture: `.shokunin/revenger/corpus/fixtures/pe-r27/fixture.exe` (SHA-256 `523e6dc1b8cc2b48a636ce3cb93736ce46d4c8d58c594d8d8dd2ed72ca2640bb`).
- Altered fixture and truth: `.shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe`, `.shokunin/revenger/corpus/fixtures/pe-r28/truth.json` (SHA-256 `9e1815a37778fc4aaf828f6d22d8c5154e9126614dda2f445768bf35d6ad1034`).
- Saved r27 REA record: `.shokunin/revenger/corpus/live/runs/round-27/inspection.json`, Evidence `ev_a524338e43a8a20a3fb0f018d46ef2fe06732e323bfb3ce98fd813bd223f50ef`.
- Saved r28 REA record: `.shokunin/revenger/corpus/live/runs/round-28/inspection.json`, Evidence `ev_bb5fb8cc540834401a018a1bc021a1cab989a7226d27e122ff51bc4387f86537`.

## Raw-byte checks

Reproducible read-only commands from the repository root (Python standard library; they do not invoke REA):

```sh
python3 - <<'PY'
from pathlib import Path
from hashlib import sha256
p = Path('.shokunin/revenger/corpus/fixtures')
a = (p/'pe-r27/fixture.exe').read_bytes()
b = (p/'pe-r28/fixture.exe').read_bytes()
print(len(a), sha256(a).hexdigest())
print(len(b), sha256(b).hexdigest())
print([(i, x, y) for i, (x, y) in enumerate(zip(a, b)) if x != y])
print('r27 payload', a[600:615], sha256(a[600:615]).hexdigest())
print('r28 payload', b[600:615], sha256(b[600:615]).hexdigest())
print('language entry @576', b[576:584].hex(' '), int.from_bytes(b[576:580], 'little'))
PY
```

Observed from that check: both files are 1024 bytes; the only differing `(offset, old byte, new byte)` tuple is `(600, 82, 83)` (`0x52→0x53`). Payload bytes at `[600:615]` are `b'REV-R27-PAYLOAD'` and `b'SEV-R27-PAYLOAD'`, respectively; SHA-256 values are `0346b578bdfe68866acea157268520567a5d6e96a28ab8a95835569921f088aa` and `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`.

The saved r28 record identifies the resource entry locations as offsets 528 (type), 552 (name), and 576 (language); at offset 576 its 4-byte ID field is `09 04 00 00`, i.e. language ID `0x0409` / 1033. The same record reports type ID 10, name ID 1, language ID 1033, payload offset 600, length 15, and the r28 payload hash above. Its matching artifact digest is the r28 whole-file SHA above. The r27 ledger reports the corresponding one-resource mapping and baseline payload hash.

## OBSERVATION / INFERENCE / UNKNOWN

**OBSERVATION:** Round 28's controlled byte change is in the payload at offset 600, not the language ID field at offset 576. The two saved inspection records and r28 ledger report the same type/name/language mapping and payload offset/length, with the respective payload digests matching the two authored byte slices. The r28 ledger describes ten local comparisons of the saved records to the authored files; the independent review is cited there. This is the prior saved-record comparison, not an independent authentication of producer invocation.

**INFERENCE:** Round 28 supports a narrow payload-byte calibration claim: for that fixture pair, a one-byte payload change was reflected in the reported payload digest while the reported resource mapping stayed the same. It does not test changing the language ID, the parser's response to such a change, or whether a resource remains associated with the same payload after language metadata changes. Round 29's proposed one-byte edit at offset 576 is therefore a distinct control axis/field, not a repeat already covered by r28.

**UNKNOWN:** Whether a parser correctly handles arbitrary language IDs, language fallback or loader selection; whether this saved-output pattern generalizes; and authenticity of saved REA records beyond the recorded local comparison and review. Neither round establishes executable/loader behavior or general parser correctness.
