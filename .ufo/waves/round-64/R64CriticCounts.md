# R64CriticCounts — byte-count and provenance attack

## Scope and axes

- **Coverage K:** C1's proposed C07 entry and its Q11 derivations.
- **Calibration:** do not call a compressed byte padding or a supplied offset a discovered offset.
- **Operability:** the documented command must reproduce correctly classified byte facts.

This is a critic's evidence report, not a gate decision, admission, integration, or round judgment. The frozen contract and counter were read; the round counter, canonical Rust judge, and orchestration runtimes were not invoked.

## Findings

### 1. Concrete counterexample: one compressed byte is printed as padding

Reviewed precursor: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/firmware-readout.py`, read snapshot `C3CE`, lines 20–32 and 60–63. Its `zero_spans(image)` enumerates *all* zero-byte runs and labels them `padding spans`. Byte **1098** is `00`, but lies inside the successfully decoded second zlib member **[1024,1114)**. The emitted **[1098,1099)** is therefore not padding.

Reproduction command, executed:

```sh
python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/firmware-readout.py
```

Observed relevant output:

```text
padding spans: maximal contiguous runs where every byte is 0x00;
  (0, 512) [half-open; end is first non-padding offset]
  (591, 1024) [half-open; end is first non-padding offset]
  (1098, 1099) [half-open; end is first non-padding offset]
  (1114, 2048) [half-open; end is first non-padding offset]
```

Independent byte check, executed:

```sh
od -An -t x1 -j1095 -N7 /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin
```

```text
2e c2 79 00 76 8c d5
```

Treating all four printed runs as padding double-counts byte 1098: their lengths plus the two compressed lengths total **2049**, not **2048**. The correct three padding intervals have sizes **512, 433, 934** and, with compressed sizes **79, 90**, partition the image exactly.

**Impacted axes:** calibration directly; coverage K's admission evidence if this output is incorporated; operability's correctness rather than command availability.

**Smallest safe correction:** derive complete zlib intervals first, take their complement within the image, and verify every complement byte is zero. Alternatively label all-zero runs literally and separately derive padding as the complement. Do not silently drop short runs by a minimum-length threshold: zero bytes inside compressed data are not padding regardless of run length. This is a fixable classification defect, not an axis tradeoff.

### 2. Offset validation is not offset derivation

The same readout snapshot, line 10, sets `EXPECTED_MEMBER_OFFSETS = (512, 1024)`; lines 65–70 iterate and print those supplied values. The decoder validates members at the supplied locations and correctly derives compressed lengths and payload hashes, but does not discover the locations from bytes. Its output honestly says `expected-offset scan`; an entry must not upgrade that into an independent byte-derived offset claim.

`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/QUALITY.md:23` explicitly says: “Constants such as header offsets are derived, not assumed.” The frozen round contract also requires each value to be derived from fixture bytes in-entry.

**Smallest safe correction:** scan byte positions for complete valid zlib streams and print discovered offsets, or carry an independent byte-scan command and its actual output in the entry. No change to truth, saved records, or the frozen counter is needed. This is a fixable provenance gap, not evidence that the literals were copied: their source cannot be established from this code.

### 3. Candidate-entry dependency was absent

The author supplied the intended scratch path `/tmp/revenger-r64-entry/candidate.md`. A direct read returned `Path ... not found`; the scratch directory had also been observed empty. Therefore this seat cannot attest to the candidate's in-entry command/output completeness or attack its exact final prose. No waiting or substitution of the saved record for the missing draft occurred. Findings 1–2 apply to the available readout precursor, not an unseen final entry.

The smallest safe handling is to keep this report's scope explicit and obtain the named fresh-seat entry review against the actual candidate before using it as admission evidence. This report supplies neither an admit nor a reject decision.

## Independent derivation and attack results

The byte derivation below ran **before** opening `truth.json`, `inspection.json`, the author's readout code, or the author's value message. It exhaustively tried zlib decoding at every byte offset; it did not seed member offsets from the contract or oracles. Only afterward were the oracle and saved observation opened for comparison.

The following executable command is equivalent to the Python evaluation performed; its displayed values are from the observed evaluation, not a claim that this exact shell wrapper was executed:

```sh
python3 -B - <<'PY'
from pathlib import Path
import hashlib, itertools, zlib
b = Path('/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin').read_bytes()
print('image', len(b), 'hex_chars', len(b.hex()), hashlib.sha256(b).hexdigest())
members = []
for start in range(len(b)):
    d = zlib.decompressobj()
    try:
        payload = d.decompress(b[start:]) + d.flush()
    except zlib.error:
        continue
    if not d.eof:
        continue
    end = len(b) - len(d.unused_data)
    members.append((start, end))
    print('member', start, end, end-start, len(payload), hashlib.sha256(payload).hexdigest())
p = 0
for value, group in itertools.groupby(b):
    n = sum(1 for _ in group)
    if value == 0:
        print('zero_run', p, p+n)
    p += n
p = 0
for start, end in members:
    if p < start:
        print('padding', p, start, start-p, all(x == 0 for x in b[p:start]))
    p = end
if p < len(b):
    print('padding', p, len(b), len(b)-p, all(x == 0 for x in b[p:]))
PY
```

Observed values from the independent evaluations:

```text
image 2048 hex_chars 4096 bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be
member 512 591 79 78 a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86
member 1024 1114 90 97 2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9
zero_run 0 512
zero_run 591 1024
zero_run 1098 1099
zero_run 1114 2048
padding 0 512 512 True
padding 591 1024 433 True
padding 1114 2048 934 True
```

| Attack | Observed result |
|---|---|
| Bytes versus hex characters | Image is 2048 bytes and 4096 hex characters. No unit error in the available readout's image length, compressed lengths, or inflated lengths. |
| Start offsets | Exhaustive independent decoding finds only 512 and 1024. Attempts at 511, 513, 1023 and 1025 each fail with `incorrect header check`. The numeric offsets are correct; their supplied-versus-derived provenance is finding 2. |
| Compressed-size boundary | At member ends 591 and 1114, exact slices reach zlib EOF; each slice shortened by one byte does not. Correct compressed sizes are 79 and 90 bytes. |
| Decompressed sizes and digests | Independently inflated payloads are 78 and 97 bytes, with the SHA-256 values above; all match the oracle. They are not derived from Binwalk's saved region list. |
| Padding off-by-one | Correct half-open intervals are [0,512), [591,1024), [1114,2048). Separate `od` boundary checks gave `0 0 120 218` at 510, `29 45 0 0` at 589, `0 0 120 218` at 1022, `37 44 0 0` at 1112, and only `0 0` from offset 2046 to EOF. |
| Padding versus compressed internal zero | Found a genuine counterexample: [1098,1099) overlaps the second complete compressed stream. See finding 1. |
| Copied expected values | No evidence of copying was established. The readout imports no oracle or saved record; hardcoded offsets remain assumptions. The missing entry prevents inspection of its value provenance. |
| Oracle comparison | `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/truth.json:28-71` matches the independently derived image, three padding spans, two member sizes, and inflated sizes/digests. |
| Saved-record comparison | `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/inspection.json` records input_size 2048 and regions (512,79), (1024,90), with `size_basis: provider_reported_validation_unknown`. It does not record padding classifications or inflated digests. Manual confirmation must not be attributed to Binwalk. |

Additional observed compressed-byte SHA-256 values, computed from the complete independently discovered intervals: first `bf3dd2e42d36324ae17e81c66cb5d699ac74b1a017628fcfb4302846b1c7c352`; second `8c32fdb048dc29f3f47dd1fb1c8fe53790d239309e340e03bd486d8722d424ff`. These were not needed to infer the interval boundaries.

The reviewed readout's separately observed SHA-256 was `d63cd25fc913ff338e40ae9dade4d928597d2c44a248efcf58e21df3f403d15e`. This is a working-tree observation, not a committed-revision claim. Both defects were sent directly to the readout executor and the concrete padding counterexample to the candidate author. No repaired version was reviewed here.

## Boundaries and tooling

No production file was edited, no git/jj mutation was run, no tool was installed or updated, and no scratch files were created by this seat. Only this assigned report was written. No final round measurement, counter edit, README flip, Q01–Q13 judgment, or admission is claimed.

Report: .ufo/waves/round-64/R64CriticCounts.md
