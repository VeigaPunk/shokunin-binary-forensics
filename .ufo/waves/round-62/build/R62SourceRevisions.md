RESULT: COMPLETE
Scope: metadata only for reserved S028/S029 at frozen `a3498e25ad87bf756288812d0ea7c474b09433c7`,
extracted via `git archive` to `/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62SourceRevisions/tree`.
No entry/README/registry/map edit, no producer/fixture/EVM/JS/RPC/service run; the named
round-62 candidate files are absent (`find`: none).

## S028 — execution-specs v2.20.0

```text
$ git ls-remote --tags https://github.com/ethereum/execution-specs.git 'refs/tags/v2.20.0*'
67f038c8c3fced0b388cfdcaed5c4a52d5fad2fd  refs/tags/v2.20.0
2004296f2ffcbcebcd00f41152d33e8dfda0922a  refs/tags/v2.20.0^{}
$ GET /repos/ethereum/execution-specs/git/tags/67f038c8… -> tag v2.20.0, tagger 2026-02-19T19:06:01Z, object commit 2004296f…, verified=false reason=unsigned
$ GET /repos/ethereum/execution-specs/releases/tags/v2.20.0 -> published_at=2026-02-19T19:07:08Z
$ GET /repos/ethereum/execution-specs/commits/2004296f… -> committer 2026-02-19T19:01:27Z, verified=true reason=valid
sha256 commit=tag: 49dd6155c7560811a8f546ea9c5a29678e3a3da859216e2ee48cfacaa5b63724 instructions/__init__.py; a2801c4169b806a9494707179a9df20170a37a1769596aac56013ddba509aef8 runtime.py
grep -n: 55 EQ=0x14; 106 JUMPI=0x57; 109 JUMPDEST=0x5B; 125 PUSH4=0x63; runtime def L22, return L69
```
Annotated tag; peeled commit `2004296f…` is the commit S016 already names. Access
2026-10-21 is a fourth distinct timestamp. The tag is unsigned; the commit-signature
result is an observation, not authenticity. `tree/v2.20.0` is mutable; the commit URL
is content-addressed. S016's tag-tree source plus `on-release` cannot detect a moved tag.

## S029 — ECMA-262 draft of 2026-10-16

```text
$ curl -sSIL https://tc39.es/ecma262/
HTTP/2 200; last-modified Mon, 19 Oct 2026 16:26:55 GMT; etag "6ad644cf-7469d7"; date Wed, 21 Oct 2026 18:00:13 GMT
page: ECMAScript® 2027; text "Draft ECMA-262 / October 16, 2026"; sha256 06db92a8331aa452b0d4de8c8938f4b7559b72417769b57d0032002398f27d7f (7629271 bytes); no 40-hex commit marker
/2027/ -> HTTP 404; git ls-remote --tags tc39/ecma262 | grep -c es2027 -> 0
```
Access 2026-10-21, draft 2026-10-16 and Last-Modified 2026-10-19 are distinct;
the URL is the moving latest draft. No frozen 2027 edition anchor exists.

```text
es2026: tag f7db29f16c5175a93f0d6e8fb27a8e3cb9b97a9e -> commit 0248456c758431e4bb8e5d26333ff1865123c9cd, tagger 2026-07-02T16:33:40Z, verified true
es2026-errata: tag 5ebd9700730a7d3b833af8f10793d76443803c0c -> commit d89c03f2db8a597bc915b363a6518d0cc8acdbc0, tagger 2026-07-28T00:04:11Z
spec.html@0248456c sha256 ce7bc30174061fd8d212270b81cf6511661180c1e174f6911d10ced0581527b0; L21738 id=sec-runtime-semantics-keyedbindinginitialization, L29079 id=sec-imports
spec.html@d89c03f2 sha256 032ecc740356b38f6846338d8c44536291a134a6ce60e651f935befb239cfc1a; same ids at L21739/L29080
/2026/: "Draft ECMA-262 / March 31, 2026", last-modified 16:26:45Z, sha256 0119d5a26afb504f4a7aba84d9d8288912044cc459c0552ea5f22f911cb87f40
```
Line numbers move between revisions; clause ids survive; `/2026/` was redeployed after both tags with no build link, so page↔tag equality is unproven.

Numbering drift affecting the entry citation:
- 2027 draft: 14.3.1.2 Evaluation calls BindingEvaluation; 14.3.1.3 `id=sec-bindingevaluation`; 14.3.3.3 keyed; 16.2.2 imports.
- ES2026: no 14.3.1.3 and no `sec-bindingevaluation`; 14.3.1.2 Evaluation directly
  contains "BindingInitialization of BindingPattern"; 14.3.3.3 keyed; 16.2.2 imports.
- So `§14.3.1.3` can only mean the 2027 draft; an ES2026-pinned row must cite
  `§14.3.1.2` + `§14.3.3.3`. The keyed argument is `environment` in ES2026 and
  `envRecord` in the draft; both carry the undefined/PutValue note (naming only).

## Recommendations

1. S028 anchor: label v2.20.0, identity commit `2004296f…`; use commit tree/raw URL
   (or tag URL only with the peel in the anchor) plus both digests. **Recheck `180d`**
   with `git ls-remote --tags https://github.com/ethereum/execution-specs.git 'refs/tags/v2.20.0*'`,
   requiring `67f038c8…` → `2004296f…`; `on-release` is wrong for a tag-pinned scope,
   and `on-tag-move` is validator-legal (`^[A-Za-z][A-Za-z0-9 _-]*$`) but new.
2. S029 primary: approved `es2026` tag commit `0248456c758431e4bb8e5d26333ff1865123c9cd` (GitHub reports its tag
   signature valid, 2026-07-02) with clause ids; use ES2026 numbering and recheck `180d`
   against tag peel plus the `es2026-errata` tag state (`on-release` alone never becomes due).
3. S029 alternate: if draft-only `§14.3.1.3` is required, anchor the live draft with
   draft date 2026-10-16, Last-Modified 2026-10-19T16:26:55Z and page digest
   `06db92a8331aa452b0d4de8c8938f4b7559b72417769b57d0032002398f27d7f`; recheck `90d` against the draft-date string and the three clause
   ids. Do not present commit `4feb0272…` as the page's build (same ids at
   L22077/L22289/L29704, sha256 `1f7935840bf249dbbfb32cc4d083114cea48bab4c513b7d7bed00387a3ebe89e`, no provenance).
4. Entry headers: `verified-at` = access 2026-10-21; tag/draft dates go in
   `source:`/anchor; Q02 `recheck` names the comparison. Proposed rows (not applied):
   `/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62SourceRevisions/proposed-S028-S029-rows.md`,
   `used-by` `—` until L1 logs the entry.
## Unknowns

- No build-provenance link ties a tc39.es page to a commit; page↔tag equality is
  unproven, including `/2026/` vs `es2026` or `es2026-errata`.
- GitHub tag refs are mutable by repository owners; observed refs are not an
  immutability guarantee. v2.20.0's tag object is unsigned.
- Candidate entries are absent at the frozen revision, so no header or line anchor
  about them is asserted.

No installs or updates. No admission; README held rows and prior evidence untouched.
