GRADE: HOLDS — round-62 preservation manifest vs frozen attack bytes d9776195 (no old bytes changed, no label reinterpretation, no removed attack)

## Frozen inputs

- Attack revision `d97761952be256d145d298022de03091de91d358` (full), claim base
  `5bd4a90fc1a34caa94496601b60537b3aab12301`, pre-registration
  `a3498e25ad87bf756288812d0ea7c474b09433c7` (tree `f53a42f2eb5baa9fa999f8bcf2b7e8145d2309c7`).
- Archive: `git -C …/revenger-shokunin archive d9776195… | tar -x -C scratch/tree` → `EXTRACT_OK`;
  `rev-parse HEAD` = `d9776195…` at extraction time.
- Manifest bytes (live == archived): `manifest.json` sha256
  `be35b0aa7b211486da914eb20ddb354e1744bd2e38a7884761ffae22ceae405e`, `manifest.tsv` sha256
  `d4d29d0a6eafa00f4cd82bd344fb6177eb61dd8c2c4d43ffe4eb27663f423031`; both committed at d9776195.
- Candidate hashes at the attack rev: C04 `42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3`,
  C09 `6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e`; both `admission-status: candidate`.

## Observation (primary commands and exact output)

1. Manifest inventory: 611 TSV rows / 611 JSON entries = 611 bytes-5,443,071, matching
   `summary.total_files` and `total_bytes`; JSON/TSV sets equal. Declared
   `manifest_sha256=ba439cc0…` reproduces exactly as SHA-256 over the path-sorted
   `sha256␠␠bytes␠␠path\n` lines (scratch `verify.py`); all six oracle group digests reproduce
   (`G1 7093b3b0…`, `G2 3b56a639…`, `G3 eb0ab939…`, `G4 15e8ce3b…`, `G5 f600dc75…`, `G6 62f6a9e5…`).
2. Per-file check of every manifest row against the extracted d9776195 tree (sha256, byte count,
   `git hash-object` blob, git mode, JSON parity): `MISMATCHES 0` (611/611).
3. `git ls-tree -r a3498e25 -- corpus/live corpus/fixtures <both rejected candidates>
   .ufo/waves/round-61 corpus/lessons/round-61-verifier-spotcheck.md reports/round-61`
   = 611 paths; manifest `git_blob`/mode mismatches: **0**; manifest set minus git set: empty.
4. `git diff --name-status a3498e25 d9776195 -- <same six paths>` → empty; file sets and every blob
   OID identical at both revisions (611 = 611, `oid diffs: []`).
   `git diff --numstat a3498e25 d9776195 | awk '$2!=0'` → no output: the entire commit-to-commit diff
   contains zero deleted lines (91 files changed, 20,086 insertions only).
5. Old rejected candidates now: `690db9f17ac2…` (`commonjs-destructured-require-edges.md`:13,371 B) and
   `3e17b88fff8c…` (`evm-saved-interface-candidates.md`:13,249 B) — equal to manifest rows 261-262;
   line 5 of each still reads `admission-status: rejected — round-61 fresh falsify wave on ab58069`.
6. Old attack evidence retained: `falsify-w3/adjudication.json` `9179e651…` (manifest:152) and five
   `falsify-w3/counterexamples/` files (manifest:153-157), e.g. `r24-scanner-rules.py
   73a63c4cd1d2f47c7034c48231f60cce3a79620e24f8b602fa04f49e404e32096`; G4 breakdown 16+69+2+69+5
   = 161 files / 1,634,982 B matches the oracle table.
7. Label surface unchanged: `git diff a3498e25 d9776195 -- README.md corpus/README.md` → empty;
   `corpus/README.md:33,38` C04/C09 still `| uncovered |`; held-row count `grep -cE '^\| C[0-9]+ .*\| held \|$'`
   = 4. Lesson bytes: `corpus/lessons/round-61.md` sha256 `da59f8d9…` and verifier lesson `c83f2d29…`
   identical at `5bd4a90`, `a3498e25`, `d9776195`.
8. Live tree `git status --porcelain` over the six scoped paths and both READMEs → empty.

## Inference

- The manifest was generated at the pre-registration revision but every one of its 611 entries has the
  same blob OID at d9776195, so it remains a valid byte baseline for the frozen attack commit.
- Zero deletions in the whole diff, plus unchanged README statuses and unchanged rejected-candidate
  headers, establishes that no old label was reinterpreted and no round-61 attack artifact was removed.

## Unknown

- `corpus/lessons/round-61.md` is outside the manifest's declared six groups; it is byte-preserved by
  direct blob identity at the three revisions, not by manifest membership. Scope note only, no claim defect.
- Untracked workspace files outside the six paths were not enumerated (same limitation the oracle states).
  This seat makes no entry-quality, Q11, admission or coverage-K judgement.

VERDICT: HOLDS. No correction, no admission. Installs: none.
