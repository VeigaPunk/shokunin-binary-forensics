GRADE: HOLDS — SOURCES.md row S028 + round-62 lesson Gate quote (C09 source-open slice)

Frozen target `d97761952be256d145d298022de03091de91d358` (HEAD; tree
`45c4c5da82aae8ca2e44f6e3ed874a33533f54b9`; `git diff --stat d9776195 -- corpus/` empty);
claimbase `5bd4a90fc1a34caa94496601b60537b3aab12301`; declaration
`a3498e25ad87bf756288812d0ea7c474b09433c7`. Candidate hashes at the frozen revision:
C09 `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md`
`6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e`;
C04 `round-62-commonjs-require-name-evidence.md`
`42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3`;
lesson `cf0339ebe9baa95124da3b7f4345f8c8abf8c5b35541d3b9ace1b22a0449d6ae`;
SOURCES `5c13831b8b64b1a2d715fc4031415750d92af4daf3ef8021c91a8912b5d66bbe`. Archive:
`/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62FSourceOpenS028/tree`.

## Observation (fresh read-only opens, 2026-10-21, official raw endpoints)

```
curl .../execution-specs/2004296f2ffcbcebcd00f41152d33e8dfda0922a/src/ethereum/forks/osaka/vm/instructions/__init__.py
  -> 10700 B sha256 49dd6155c7560811a8f546ea9c5a29678e3a3da859216e2ee48cfacaa5b63724 (367 lines)
curl .../2004296f.../src/ethereum/forks/osaka/vm/runtime.py
  -> 1971 B sha256 a2801c4169b806a9494707179a9df20170a37a1769596aac56013ddba509aef8 (69 lines)
curl .../v2.20.0/... for both files -> same SHA-256 as the commit fetch
git ls-remote --tags https://github.com/ethereum/execution-specs.git 'refs/tags/v2.20.0*'
  67f038c8c3fced0b388cfdcaed5c4a52d5fad2fd  refs/tags/v2.20.0
  2004296f2ffcbcebcd00f41152d33e8dfda0922a  refs/tags/v2.20.0^{}
GET git/tags/67f038c8... -> tag v2.20.0, object.type commit, tagger 2026-02-19T19:06:01Z,
  verification.verified=false (unsigned; row asserts no signature); tree URL HTTP 200
```

Anchor lines in the pinned bytes (`nl -ba`): `instructions/__init__.py` :55 `EQ = 0x14`,
:104 `STOP = 0x00`, :106 `JUMPI = 0x57`, :109 `JUMPDEST = 0x5B`, :118 `POP = 0x50`,
:121 `PUSH0 = 0x5F`, :122 `PUSH1 = 0x60`, :125 `PUSH4 = 0x63`, :153 `PUSH32 = 0x7F`;
`runtime.py` def L22, `return valid_jump_destinations` L69, `push_data_size` L64.
Gate quote at `runtime.py:29-30` is verbatim: "The jump destination shouldn't be part of
the data corresponding to `PUSH-N` opcodes." — 13 words (≤25), location cited at lesson
`:66`, access date 2026-10-21 at lesson `:59`.

## Manifest comparison

`.ufo/waves/round-62/source-snapshots/manifest.json` (sha256
`cd26810aeecf4ea7f0824f5ef88e16176541c439eedcde8fe2cf36f67c057c4b`, untracked build
artifact): instructions 10700 B / `49dd…`, runtime 1971 B / `a280…`, access 2026-10-21,
tag-ref raw URLs — identical digests/bytes/order to the S028 anchor cell ("respectively")
and to the Gate URL. Preservation manifest `frozen_tree` `f53a42f2…` equals
`git rev-parse a3498e25^{tree}`. `corpus/SOURCES.md` is byte-identical at `a3498e25` and
`5bd4a90` (`aa7b07e1…`, 27 rows, no S028); at the candidate it has 31 rows with S028.
Whole-row diff S001–S027 from claimbase to candidate: empty (no status/recheck/used-by
edits). Census on the frozen tree: 31 rows; S028 cell count 13 (no stray `|`); malformed
rows 0; duplicate ids none; both `used-by` paths exist.

## Requirement checks

- Row absent at claimbase and declaration, appended this round, `opened 2026-10-21`;
  Gate carries URL, revision and access date.
- Quote is 13 words, exact, at the cited lines; source is the pinned tag/commit.
- Scope excludes gas, stack, jump acceptance and provider behavior; `kind spec`, tier A
  only for byte assignments and the static scan; lesson `:68` "Enum assignments are not
  execution semantics".
- No own-work producer accuracy: the C09 entry keeps S028 spec facts in its
  `## Source facts (recorded)` block and S031 authored bytes separately; its recorded
  constants and runtime:28/29-30/64 quotes all match the pinned bytes exactly.
- No actual misstatement found in the row, the Gate quote, or the opener citations.

Non-fatal observations (not contradictions): (a) `recheck = on-release` was called weak
for a tag-pinned scope by build scout `R62SourceRevisions.md`; it is a contract-legal
cadence and the commit anchor makes a moved tag unable to change the quoted revision.
(b) The Gate URL uses the mutable `v2.20.0` ref while the row anchor pins commit
`2004296f`; both refs fetch identical bytes today. (c) The source-snapshots manifest is
not itself hash-pinned in the lesson/registry, so its content digests were independently
reproduced from the official bytes above.

Inference: none needed for this grade; every asserted value was re-read from the pinned
bytes or the frozen tree.

Unknowns: no post-v2.20.0 release state was queried (not required for a tag-pinned row);
no producer, fixture JS or EVM execution was used; C09 admission itself is not decided
by this slice.

VERDICT: HOLDS for S028 source row + Gate quote. No repair, no admission, no README
flip. Installs/updates: none.
