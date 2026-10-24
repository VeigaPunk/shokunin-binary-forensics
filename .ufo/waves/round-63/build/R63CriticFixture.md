# R63 C2 fixture critic

**Design verdict: SOUND for the exact bytes, saved observation, and version-bounded recipe reviewed.** This is a scoped design review, not a claim-admission or canonical-judge decision.

## Axes and reviewed identities

Axes: byte-oracle ambiguity/identity; scanner continuation and carve boundaries; inertness; reproducibility. Frozen authority: `reports/round-63/claims.md:43-61` and `reports/round-63/measure.py:36-53`; no criterion was changed.

Read-only byte analysis observed:

- `corpus/fixtures/firmware-r63/firmware-r63.bin`: 2048 bytes, SHA-256 `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be`.
- `generator.py`: SHA-256 `4e5d5975e3cf6362f6fd430f2147d42f75d011978f7d6b5ec86d224c77793db4` at byte inspection.
- `truth.json`: SHA-256 `9663f90b2b9f29c5beb621e554ed7584eedf5e77d4785f26a453e70dbd5a65e6` at byte inspection.
- Saved `corpus/live/runs/round-63/inspection.json`: Evidence ID `ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259`; subject digest equals the image digest above. `receipt.json` records the single producer invocation and exit 0. I did not repeat it.

## 1. Strongest ambiguity counterexample: a second physical image

A region-only comparison has two authorities: the record can describe one image while the truth validates another image with identical compressed member tuples. The initial oracle source read did not compare its actual image hash with the saved record's subject digest. I reported this to the oracle author. The smallest safe correction was to bind the actual image SHA-256 to `record.subject.digest.sha256`, and the actual length to `normalized_result.input_size`; those checks were present by the time the attack below executed.

Tested the actual comparison source, SHA-256 `d0dfd7a1cd105485e47bf52446056a2636fb803c05a404ce56da597f36ce0512`, in the existing Python interpreter:

1. Original truth + original saved record: return **0**, last line `ORACLE OK`.
2. Alternate image: replace exactly the first 512 zero padding bytes with `ff`; leave both compressed members and every offset/size unchanged. Update the alternate truth's first `fill_hex`, image path and image SHA-256 accordingly. Alternate image SHA-256: `4653a32ea6b08b886501951bdea492e17a8058d5634e8aa2162eed588b1e9422`.
3. Same original saved record + alternate truth: return **1**. All padding, member hashes and region tuples independently matched, but identity rejected the second state:

```text
MISMATCH subject.digest.sha256: expected 4653a32ea6b08b886501951bdea492e17a8058d5634e8aa2162eed588b1e9422, got 'bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be'
ORACLE MISMATCH
```

**Impacted axes:** oracle uniqueness and provenance/calibration. **Correction status:** the fixable identity defect is closed in the exercised source; no pre-fix accepted mutation run is claimed. The oracle also checks contiguous image coverage, actual filler bytes, exact compressed-stream EOF, decompressed size/hash, and bijective non-padding region alignment. Equivalent padding spellings, labels or recipe prose can still differ; they are not different physical byte truths. This is not a guarantee of unique JSON serialization or general firmware validation.

## 2. Compression magic and scan continuation

All positions below were derived from the finished image, not generator intent. Intervals are half-open.

| Bytes | Kind | Byte evidence |
|---|---|---|
| `[0,512)` | padding | every byte `00` |
| `[512,591)` | zlib | 79 bytes; prefix `78 da`; Adler-32 trailer `7b3b1d2d` |
| `[591,1024)` | padding | 433 bytes, every byte `00` |
| `[1024,1114)` | zlib | 90 bytes; prefix `78 da`; Adler-32 trailer `11bf252c` |
| `[1114,2048)` | padding | 934 bytes, every byte `00` |

An exhaustive adjacent-byte sweep over the **whole** image checked every RFC 1950-valid CMF/FLG pair: compression method 8, CINFO ≤7, and `(CMF*256+FLG) % 31 == 0`. It found **only** `(512,78da)` and `(1024,78da)`. Consequently, neither stream contains the other's compression prefix; there is no such prefix in padding, trailers, or straddling a region boundary. Gzip prefix `1f8b` was absent globally; therefore `1f8b08` was absent too.

Pinned upstream [Binwalk v3.1.0 zlib signature](https://raw.githubusercontent.com/ReFirmLabs/binwalk/v3.1.0/src/signatures/zlib.rs) recognizes `789c`, `78da`, `785e`, **not** `7801`. Its [signature registry](https://raw.githubusercontent.com/ReFirmLabs/binwalk/v3.1.0/src/magic.rs) marks zlib short; default scanning can therefore miss nonzero-offset zlib. The saved record's actual execution uses `--quiet --search-all --threads 1 --log …`, so this default-mode counterexample does not apply here.

The saved record reports exactly `(offset=512, reported_size=79, signature=zlib)` and `(1024,90,zlib)`. Thus scanning demonstrably reached the second member; it did not stop after the first or carve the first through padding. The [pinned scanner](https://raw.githubusercontent.com/ReFirmLabs/binwalk/v3.1.0/src/binwalk.rs) resumes at the end of a validated known-size hit and skips its interior. This is compatible with these non-overlapping streams, not proof of nested-member completeness. The installed executable's retained source revision is null; upstream source reasoning is corroborated by, not substituted for, the saved observation.

Each exact compressed slice decoded with `eof=True`, zero unused data and zero unconsumed tail. Decoding from its start through the image suffix consumed exactly 79/90 bytes, respectively. This rejects the usual `decompress()`-ignores-trailing-padding boundary ambiguity. Adler values independently computed from the decoded bytes matched both trailers. The oracle's exact-EOF check is important: Binwalk's upstream [zlib extractor](https://raw.githubusercontent.com/ReFirmLabs/binwalk/v3.1.0/src/extractors/zlib.rs) inflates the inner stream and adds wrapper lengths; its reported size alone is not an independent wrapper-checksum guarantee.

## 3. Inertness

Decoded content was read in memory only:

- `diagnostic-note`: 78 ASCII bytes, SHA-256 `a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86`; diagnostic sensor/units/state text.
- `component-note`: 97 ASCII bytes, SHA-256 `2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9`; component/revision/execution-label text.

Both begin with ASCII `R63 inert synthetic`, not an executable header. Explicit prefix checks rejected ELF, MZ/PE, shebang, 32-bit Mach-O in both byte orders, WebAssembly, DEX and Java class headers. The complete decoded strings are the generator's short literal records, not code or nested archives. This is byte-level evidence, not reliance on the words `inert` or `execution=disabled`.

The saved inspection used no extraction/recursive-extraction flag; `raw_result.report[0].Analysis.extractions` is `{}`. Nothing in this review executed a payload, and no additional firmware extraction or vendor input was used. No executable-format member was found in this fixture.

## 4. Determinism and fixed stamps

`generator.py` uses fixed literal payloads, offsets 512/1024, image length 2048 and zero filler. Zlib wrappers have **no timestamp field**; no gzip member or filesystem timestamp is embedded. There is no clock, random source or filename metadata in member construction.

Compression is `zlib.compress(payload, level=9)`, so bit identity is **version-bounded**, not an assertion about all compressor versions. `truth.json` explicitly records Python **3.14.8**, zlib compile/runtime **1.3.2**, and says reproducible with those recorded versions. This disclosure is sound; a different compressor must not be silently treated as the same build. The generator does not enforce the recorded environment. If an unqualified cross-version guarantee is later wanted, the smallest correction is to pin/reject mismatched compressor versions or specify fixed DEFLATE bytes/framing, retaining a Binwalk-recognized zlib header. That stronger guarantee is not demonstrated here and is not silently assumed.

## Reproduction of the exercised identity attack

The following is equivalent to the in-process Python test used; it writes only owned temporary test data and removes it before returning. It executes the comparison helper, never the firmware bytes.

```sh
python3 -B - <<'PY'
from pathlib import Path
import contextlib, copy, hashlib, io, json, sys, tempfile
lane = Path('/home/vgpnk/Projects/shokunin/revenger-shokunin')
fixture = lane / 'corpus/fixtures/firmware-r63'
run = lane / 'corpus/live/runs/round-63'
check = run / 'oracle_check.py'
source = check.read_text()
print('ORACLE_SOURCE_SHA256', hashlib.sha256(source.encode()).hexdigest())
ns = {'__name__': '_r63_critic_fixture_review', '__file__': str(check)}
exec(compile(source, str(check), 'exec'), ns)
image = (fixture / 'firmware-r63.bin').read_bytes()
truth = json.loads((fixture / 'truth.json').read_bytes())
old_argv = sys.argv[:]
def exercise(label, truth_path):
    sys.argv = [str(check), '--record', str(run/'inspection.json'), '--truth', str(truth_path)]
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        rc = ns['main']()
    print(label, 'return', rc)
    print(out.getvalue(), end='')
try:
    exercise('BASE', fixture/'truth.json')
    with tempfile.TemporaryDirectory(prefix='revenger-r63-critic-fixture-', dir='/tmp') as tmp:
        tmp = Path(tmp)
        alternate = b'\xff'*512 + image[512:]
        forged = copy.deepcopy(truth)
        (tmp/'alternate.bin').write_bytes(alternate)
        forged['image']['path'] = str(tmp/'alternate.bin')
        forged['image']['sha256'] = hashlib.sha256(alternate).hexdigest()
        forged['regions'][0]['fill_hex'] = 'ff'
        (tmp/'truth.json').write_text(json.dumps(forged))
        exercise('ALTERNATE', tmp/'truth.json')
finally:
    sys.argv = old_argv
PY
```

Whole-image prefix sweep, matching the independently executed byte computation:

```sh
python3 -B - <<'PY'
from pathlib import Path
p = Path('/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin')
b = p.read_bytes()
print([(i, b[i:i+2].hex()) for i in range(len(b)-1)
       if b[i] & 15 == 8 and b[i] >> 4 <= 7 and (b[i]*256+b[i+1]) % 31 == 0])
print([i for i in range(len(b)-1) if b[i:i+2] == b'\x1f\x8b'])
PY
```

Observed: `[(512, '78da'), (1024, '78da')]`, then `[]`.

## Scope and disposition

The strongest false-provenance counterexample was fixable and is rejected by the exercised correction; it is not a coverage-for-calibration trade. The reviewed layout has no compression-prefix collisions, no early-stop observation, exact stream boundaries, and inert text members. Keep the explicit version limitation and `signature_scan` / `provider_reported_validation_unknown` qualifications. No scanner-completeness, general firmware, extraction-capability or round-admission verdict is made.

Only this assigned report was written in the lane by this critic. No production edits, git/jj mutations, package installations/updates, runtime launches, or duplicated REA producer calls were made. Temporary counterexample data under `/tmp/revenger-r63-critic-fixture-*` was removed (observed `SCRATCH_REMOVED True`).
