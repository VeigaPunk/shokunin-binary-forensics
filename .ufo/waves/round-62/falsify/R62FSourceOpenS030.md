GRADE: HOLDS — SOURCES.md row S030 + lessons/round-62.md sourceGate S030 (round 62, frozen candidate state)
Frozen revision: d97761952be256d145d298022de03091de91d358
  `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin rev-parse d97761952be256d145d298022de03091de91d358` -> `d97761952be256d145d298022de03091de91d358`
  `git -C … archive d977… | tar -x -C /fast/scratch/hyaku/revenger-r62/R62FSourceOpenS030/tree` -> exit 0
Candidate hashes (at d977):
  C04 corpus/knowledge/round-62-commonjs-require-name-evidence.md 42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3
  C09 corpus/knowledge/round-62-evm-dispatch-byte-evidence.md 6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e
Registry/lesson at d977: SOURCES.md 5c13831b8b64b1a2d715fc4031415750d92af4daf3ef8021c91a8912b5d66bbe;
  lessons/round-62.md cf0339ebe9baa95124da3b7f4345f8c8abf8c5b35541d3b9ace1b22a0449d6ae (worktree hashes equal to d977 blobs).

OBSERVATION — primary opens and exact outputs
O1 Shape: SOURCES.md:44 at d977 has 11 cells — S030 | own-work | A | scope |
   anchor | teaches | mined | 2026-10-21 | 90d | corpus/lessons/round-62.md,
   corpus/knowledge/round-62-commonjs-require-name-evidence.md. Used-by paths exist.
O2 Revision/bytes: `git cat-file -p a3498e25…:<path> | sha256sum` ->
   js-r3/index.js f7d8bf470bb37d5eacedd7d571705bc80cc365195069ce1b7c6d4a24ae869fd7 (274 B);
   js-r7-v2/index.js b53d96d432c120f6217a2da2ea3ed592308a3a23ef1a01745a22fd335ac4c42a (209 B);
   20261012T164357Z/analysis.json 7c3ba8c15673a7e48600bba3f42a6ca3935dbd75e30832569a631979e31ed452 (193573 B);
   round-7/v2-analysis.json 331ec252aefdc7715e49f039d7443736ff9560565f208f35b4c972bfe45d564e (171150 B).
   The two record values are exactly the row's two "record SHA-256" strings.
   `git diff a3498e25 d977 -- corpus/fixtures corpus/live` -> empty.
O3 Gate quote text: `git cat-file -p a3498e25:corpus/fixtures/js-r3/index.js | sed -n 1p` ->
   `const { rot13, checksum } = require('./transform');`
   and js-r7-v2 line 1 -> `const { rot13 } = require('./transform');`.
   Gate lines 76-77 cite the first exactly, at `corpus/fixtures/js-r3/index.js:1`, revision
   a3498e25. Quote is 7 whitespace-separated tokens (<=25). Access date is stated once for
   all new rows at lessons/round-62.md:59: "Access date **2026-10-21** for all new rows."
O4 Anchor path: in both records, `normalized_result.graph.edges` with `relation=imports`
   (js-r3 3 edges, js-r7-v2 2 edges) carry `properties` and `evidence.location.value`:
   js-r3 imported_name rot13/None/checksum at [line 1 col 6, col 50], [1,28-1,50], [1,6-1,50];
   js-r7-v2 None/rot13 at [1,18-1,40], [1,6-1,40]. `evidence.location` is an object with
   `available:true` and `value:{source:"index.js",start:{...},end:{...}}`, exactly the
   anchor's dotted path.
O5 Record pairing: subject.name is `js-r3` / `js-r7-v2`; operation
   `analyze_javascript_application`; provider `rea-javascript-application` v1; file SHA-256
   matches O2. Provider/operation/Evidence fields are recorded literal fields, not re-derived.
O6 Opened this round: `git show a3498e25:corpus/SOURCES.md | grep -c '^| S03'` -> 0;
   `git log --oneline -S'| S030 |' -- corpus/SOURCES.md` -> d977619 "round-62: new narrow
   C04/C09 candidates with in-entry derivations; 64-seat build, scoped sources, no admissions".
   Row opened 2026-10-21 equals the access date.
O7 Own-work boundary: the scope cell says "not provider accuracy or execution"; the teaches
   cell says "keeping literal record observations separate from runtime or export-binding
   claims". No provider-accuracy, completeness or runtime claim was found in the row.
O8 README at d977 still shows C04/C09 uncovered ("— (round-61 candidate rejected…)"), so
   S030 records provenance only and admits nothing.

INFERENCE
I1 All three checkable row strings — the two record hashes, the anchor path with relation
   filter, and the Gate quote with location/revision — match primary bytes at a3498e25
   (unchanged at d977). The row's declared narrow scope is narrower than the candidate's
   derivation and does not convert own-work bytes into producer-accuracy evidence.
I2 Gate line 78 says "saved import fields and full hashes were opened at the same revision
   (`R62SourceJsOwn.md:12-43`)". Lines 12-15 list all four opened files and 24-27 give the
   digest values truncated for display; the opener's referenced captured output
   `/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62SourceJsOwn/derive_s030.out` contains
   25 full 64-hex digests, and the row itself prints both full record digests. This is a
   display-truncation nuance in the report, not an actual misstatement of the frozen bytes.
I3 No actual misstatement found in S030's scope, anchor, quote text, kind/tier/status,
   opened date or used-by, nor in the mandatory Gate URL/path, access date, <=25-word quote
   or location fields.

UNKNOWN
U1 Whether other provider versions describe these fixtures the same way is outside S030's
   declared scope and is not claimed here.
U2 The provider's own root/directory digests (8eec9ffb…, 696c2496…) are recorded only; this
   review did not re-derive them.
U3 The C04 candidate's Q01-Q13 admission audit is a separate fresh attack; not adjudicated.

VERDICT: HOLDS. S030 and its Gate entry satisfy scope, anchor, quote-text, access-date,
opened-this-round and no-producer-accuracy checks against primary bytes. No correction
required; no admission is implied and README remains 4/14 with C04/C09 uncovered.
Installs: none.
