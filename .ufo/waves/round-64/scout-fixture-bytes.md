# R64ScoutFixtureBytes — independent byte census

Axes: census completeness; digest-to-ledger agreement; preservation of existing evidence.

## Observed

Recursive file inventory (hidden files included, gitignore disabled) found **9 files**: 3 fixture files and 6 saved-run files. Two `sha256sum --` commands hashed every listed file directly, without running the generator, checker, REA, or frozen counter. Exact full-digest searches were then made against `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/LEDGER.md` for every distinct computed SHA-256; the two saved output files share one digest. Ledger lines 15–28 were read to establish which file each matching string describes.

**Result: 8 matching files, 0 conflicting recorded digests, 1 unrecorded file (the ledger itself).**

Ledger references below are line numbers in `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/LEDGER.md`.

| File | Computed SHA-256 | Ledger cross-check |
|---|---|---|
| `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin` | `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be` | MATCH, line 15 (also line 35) |
| `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/generator.py` | `4e5d5975e3cf6362f6fd430f2147d42f75d011978f7d6b5ec86d224c77793db4` | MATCH, line 16 |
| `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/truth.json` | `9663f90b2b9f29c5beb621e554ed7584eedf5e77d4785f26a453e70dbd5a65e6` | MATCH, line 18 |
| `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/LEDGER.md` | `25a4a18b76a2a55f3b7ea397ee23bba948be3f1c1a3e13a3194c0f057bb1e1a6` | UNRECORDED: exact full digest has no match in the ledger |
| `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/oracle_check.py` | `d0dfd7a1cd105485e47bf52446056a2636fb803c05a404ce56da597f36ce0512` | MATCH, line 28; explicitly a historical check-time digest, not an immutable pin |
| `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/receipt.json` | `e930a549db16a180d4ab05307e073cd71599a3317b9f3d15a0d97843d5c6b94d` | MATCH, line 26; matches the corrected pin ending `5c6b94d` |
| `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/inspection.json` | `f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9` | MATCH, line 27 explicitly assigns the saved-stdout digest to this file too |
| `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/stdout.raw` | `f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9` | MATCH, line 27 (also receipt stdout digest at line 26) |
| `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/stderr.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | MATCH, line 27 |

## Commands exercised

These two commands produced the nine computed values above:

```sh
sha256sum -- /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/generator.py /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/truth.json
sha256sum -- /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/LEDGER.md /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/oracle_check.py /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/receipt.json /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/inspection.json /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/stdout.raw /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/stderr.txt
```

## Inference, confidence, and remaining unknowns

- High confidence in this point-in-time working-tree census and literal ledger correspondence. The ledger self-digest gap is disclosed, not counted as a conflicting digest.
- [INFERENCE] The missing self-digest alone does not establish payload drift or forgery.
- No baseline/archive comparison was performed; historical byte preservation, authenticity, semantic correctness, and later concurrent changes are not established by this census.
- No exported code contract was investigated; LSP tracing is not applicable to this file-digest question. The checker was hashed, not executed.
- No source/evidence files were changed. No git/jj operations, tool installs, scratch files, builds, tests, or verifier runs were performed. Only the two assigned report files were written.

Report: .ufo/waves/round-64/scout-fixture-bytes.md
