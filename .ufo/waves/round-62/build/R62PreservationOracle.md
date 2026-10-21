RESULT: COMPLETE

# Preservation digest baseline — frozen a3498e25ad87bf756288812d0ea7c474b09433c7

Hash-only work: no measure.py, gate, verifier, fixture JS, EVM bytecode, REA producer,
network or chain call was run. No knowledge entry, README row or corpus file was edited.
Frozen point: `a3498e25ad87bf756288812d0ea7c474b09433c7`, tree
`f53a42f2eb5baa9fa999f8bcf2b7e8145d2309c7`, parent/claim base
`5bd4a90fc1a34caa94496601b60537b3aab12301` (`git cat-file -p a3498e25`). HEAD equals the
frozen revision.

Extraction (scratch, no repo mutation):
`git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive --format=tar a3498e25 | tar -x -C <scratch>/tree` → EXTRACT_OK.

## Scope counts — exact, from `find <paths> -type f | wc -l` and manifest rows

| Group | Path | Files | Bytes | Group SHA-256 |
|---|---|---:|---:|---|
| G1 | corpus/live | 345 | 3,632,126 | `7093b3b08ef4125050fb81592c27f5b6897bb065e71f5bb9e5f299acadeee881` |
| G2 | corpus/fixtures | 98 | 109,779 | `3b56a6392156e2510c47197c1ac2f36548c16207de06fb741ea31132ae458f32` |
| G3 | both rejected round-61 candidates | 2 | 26,620 | `eb0ab939f0d7233c307b6643a6a0f6c06a6014ffe96896814d8f2dcbcad97199` |
| G4 | .ufo/waves/round-61 (all) | 161 | 1,634,982 | `15e8ce3b5e27fb5a7cd33f1a7eb8d1a0233e5fe364a9aff541a31e4c4ec77f56` |
| G5 | corpus/lessons/round-61-verifier-spotcheck.md | 1 | 13,061 | `f600dc753989c72f83cedc085aa4fa410fbea7b1e4cd00480726300d834f21fb` |
| G6 | reports/round-61 (supplementary; claims.md:59-60 byte-preservation) | 4 | 26,503 | `62f6a9e59f5d6d6240e8eb46fe2fffddca317db32e3923edd63b79450d8c0915` |

TOTAL **611 files / 5,443,071 bytes**; manifest digest
`ba439cc085520324e35363e8474cd41583381f3f05cb00c35b9b6bc2fe2fed9c`
(SHA-256 over sorted `sha256␠␠bytes␠␠path\n` lines).

G4 internal breakdown (same manifest rows, no overlap): build 69 files/574,930 B;
falsify 2/35,420 B; falsify-w3 69/446,629 B; falsify-w3/counterexamples 5/11,845 B;
top-level 16/566,158 B — sums to 161/1,634,982 B.

Key preservation anchors (full table in manifest):
- `corpus/knowledge/commonjs-destructured-require-edges.md` 13,371 B
  `690db9f17ac2e64b35efeb90392fae3401ae8e14c843a1ac4eac6f240ef2a6f3` — line 5 `admission-status: rejected`.
- `corpus/knowledge/evm-saved-interface-candidates.md` 13,249 B
  `3e17b88fff8cfa1c98db72a212a134e1c56fcb8b84e75573a00041cc16969361` — line 5 `admission-status: rejected`.
- `corpus/lessons/round-61-verifier-spotcheck.md` 13,061 B
  `c83f2d29f7b0b72d5eb30c24d55aa6285128beda1b85fa7261cbc951444665d2`.
- `.ufo/waves/round-61/falsify-w3/adjudication.json` 21,103 B
  `9179e651f2eccb566196c5bf21f48264c19ed01f2b05729027e1450ecf5caa0f`;
  five counterexample files retained under `falsify-w3/counterexamples/`
  (e.g. `r24-scanner-rules.py` `73a63c4cd1d2f47c7034c48231f60cce3a79620e24f8b602fa04f49e404e32096`).
- Both rejected candidates are the pair the verifier lesson names at
  `corpus/lessons/round-61-verifier-spotcheck.md:62,144-145`; no other knowledge file has `admission-status`.

## Integrity and live-tree checks (hash-only, no admission meaning)

1. Independent identity per file: `git -C tree hash-object --no-filters -- <p>` compared to
   the `ls-tree` blob OID. Script exits 2 on any mismatch; run printed no mismatch for all 611.
2. Extracted set equals `git ls-tree -r a3498e25 -- <all six scoped paths>`: sorted
   listings `wc -l` = 611 and `diff` empty (0 lines).
3. Live working tree: re-hashed all 611 live files against manifest.tsv →
   `CHECKED 611 MISMATCHES 0`; `git status --porcelain -- <scoped paths>` → `STATUS_LINES 0`.
4. Round-62 candidate paths are absent at the frozen point:
   `git cat-file -e a3498e25:corpus/knowledge/round-62-evm-dispatch-byte-evidence.md` and
   `…round-62-commonjs-require-name-evidence.md` both `absent-at-frozen`; 0 tracked files
   under `.ufo/waves/round-62`. No pre-credit exists in the baseline.

## Unknowns / limits

- Covers frozen tracked bytes only. Untracked live workspace files outside the six scoped
  paths were not enumerated; scratch copies are not landed artifacts.
- Group digests depend on the generator's line format; reproduce only with
  `manifest.py` (3,689 B, SHA-256 `41b438067a12aaae113b1e4e96f6ca61faf2c3117953973199377b246f33837c`).
- This baseline makes no claim about entry quality, Q01–Q13, C1 admission or README
  status; rejected candidates remain rejected and C04/C09 remain as frozen.

## Proposed artifact (scratch, for L1 to land if wanted)

`/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62PreservationOracle/`:
`manifest.tsv` (612 lines = header + 611 rows, SHA-256
`d4d29d0a6eafa00f4cd82bd344fb6177eb61dd8c2c4d43ffe4eb27663f423031`),
`manifest.json` (SHA-256 `be35b0aa7b211486da914eb20ddb354e1744bd2e38a7884761ffae22ceae405e`),
`manifest.py`, `check_live.py`. Nothing under corpus/, README or .ufo/waves/round-61 changed.

Installs: none.
