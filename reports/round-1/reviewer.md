# Fleet round-1 — ReplayReviewer verdict

Scope: `corpus/verify_named_multi_icon_states.py` historical pin / local-read design and the landed replacement.
Revision inspected: baseline commit `286033c5f2b1683fb538e86e15667709bb49b054` plus the current uncommitted worktree edit (file snapshot tag `#6C93`, single-file diff `9 insertions(+), 7 deletions(-)`; `git status` shows no other tracked file modified). Reviewer executed no tests, no CLI runs, no HIST-path probe. L2 author-side evidence only; no independence, promotion, or outside-discernment claim.

## 1. Observed (directly checked)

### Saved records, unchanged (census via read + sha256)
- Fixture bytes at `corpus/fixtures/pe-r{55,56,57}/fixture.exe`: SHA-256 `41c0…572b`, `911f…e83b`, `71d1…494d` — equal to the in-code `EXPECT` pins, to each receipt `fixture_sha256`, to `subject.digest.sha256`, and to `normalized_result.artifact.sha256`.
- `sha256(inspection.raw.json)` equals each receipt `stdout_sha256` (3/3): r55 `54ffdeab…`, r56 `59a95f9d…`, r57 `5c915ebd…`.
- Evidence IDs in inspection == receipt == `EXPECT` (3/3); `operation` `inspect_pe_resources`.
- The historical absolute path `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/pe-r{r}/fixture.exe` appears in each saved record at FOUR sites: `normalized_result.artifact.path`, `receipt.command`, top-level `parameters.path`, top-level `locations[0].path`.
- r55–r57 `LEDGER.md` corroborate digests, evidence IDs, stdout SHAs, one-byte deltas (928, 924) and the stance "receipt hashes establish internal consistency only" — but reference fixtures only by relative `corpus/fixtures/...` paths. The absolute historical root is pinned only by parent authority (`brief.md:9`, `LOG.md:726`), i.e. independently of the data under test. Correct source of authority for the fix.

### Baseline defect (tag `#878F`, pre-fix)
Three coupled comparison sites used the current-checkout path as historical identity, all fed by `fixture=ROOT/...`:
- line 67 `r{r} artifact` equality — first failure, matches baseline.txt (`AssertionError: r55 artifact`);
- line 58 → 63 complete normalized-dictionary equality embeds the same local path in `expected`;
- line 69→70 receipt `command` built from local path.
A naive fix at only one site relocates the failure; all four sites plus the forged-claim call (line 92) had to be handled consistently.

## 2. Landed replacement — site-by-site verdict (tag `#6C93`)

| Site | Now | Verdict |
|---|---|---|
| lines 8–9 | `HIST=Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')` literal; comment "never read through it" | Correct. String is byte-identical (incl. historical spelling `prymeagnt`) to the saved prefix minus the fixed `/fixtures/pe-r{r}/fixture.exe` suffix; literal is absolute and canonical, so `Path()`/`str()` round-trip is identity. A wrong root would fail closed (AssertionError), never open. |
| 67 | `fixture=ROOT/...` + `d=fixture.read_bytes()`; `hist=HIST/f'fixtures/pe-r{r}/fixture.exe'` | Reads stay local; `fixture` now appears ONLY as a byte-read source. No open/read/join anywhere through `HIST`. |
| 69 | `artifact==dict(path=str(hist),…)` | Historical path pinned against independent constant, exact equality kept — no dual (hist-or-local) acceptance. |
| 59–65, 70 | `compare_normalized` param renamed `fixture→hist`, expected embeds `str(hist)`; complete-dictionary equality retained | No field dropped from `expected`; location entries (name offset 736/12 at line 74, directory/data-entry/payload locations from `decode`) still participate, so name-location and ancestor-location forgeries still break the byte-derived equality. |
| 71–72 | command from `{hist}` interpolation | Byte-for-byte template of saved commands (`npx -y rea-agents@6.4.0 inspect-pe-resources <path> --format json`, verified against all three receipts). Exit code, duration, fixture hash, evidence ID, `stdout_sha256==H(raw)` checks untouched. |
| 94 | forged-claim control passes `HIST/f'fixtures/pe-r{r}/fixture.exe'` | Consistent with line 67/70 expected construction; rejection attribution is sound because the positive check (line 70) passes first with the identical expected value. |
| argv / req sites | 21 static `req(` sites before and after; no argument parsing added | `--self-test` census command (baseline.txt:11–23) unaffected; PASS-line count is runtime-derived, unchanged in shape. |

### Does the comparison now trust data under test?
No. Observed: no expected value is derived from `report` fields (`str(fixture)` fully removed from comparison sites; grep confirms only `fixture.read_bytes()` remains), and no path is copied out of `receipt.command` or `normalized_result.artifact.path`. Historical identity binds via independently pinned constants (`EXPECT` digests/evidence IDs, `HIST` root) plus byte hashes of the present corpus; the historical root itself is pinned by parent dispatch docs, not by the saved records.

## 3. Findings by severity

1. Medium (residual, baseline-inherited — NOT a regression, NOT in the single claim): `parameters.path` and `locations[0].path` also carry the historical absolute path but are unchecked, before and after the fix. A forgery editing only those fields still replays. If the parent's "rejection of forged historic artifact path" probe targets `normalized_result.artifact.path`, it fails closed (message `r55 artifact`) as required; if it targets `parameters`/`locations`, the current verifier will not reject. Recommend the fleet report state this limit (or add pins as a separate future claim), rather than silently widening this move.
2. Low: line 94 re-constructs `HIST/f'fixtures/pe-r{r}/fixture.exe'` inline instead of reusing the `hist` value produced by `check()`; currently value-identical, but a future divergence would silently weaken forged-claim attribution while both checks still pass for the wrong reason.
3. Low: identical rejection message `r{r} normalized result` for every dictionary mismatch means the forged-claim probe (lines 93–97) cannot, in isolation, prove the rejection was caused by the intended mutation; soundness rests on the positive check passing with the same expected constructor — satisfied in this revision.
4. Cosmetic: `PASS: {N} …` text unchanged; no new `req` sites, so the relocated ledger's N should equal the historical passing count — parent should record the value, not assume it.

## 4. Verdict

ACCEPT (conditional on parent CLI acceptance) for the inspected revision (baseline + worktree edit tag `#6C93`). The design separates local byte reads from independently pinned historical path/command identity, keeps complete normalized-dictionary equality, receipt stdout-hash/command checks, and both forged-claim rejections intact, and does not make any comparison trust the field under test. No blocking defect found. No independence or promotion is claimed by this review.

## 5. Exact acceptance conditions for the parent (run once after integration)

- A1 lane root `python3 -B corpus/verify_named_multi_icon_states.py` → exit 0, `PASS:` line, record N; A2 unrelated CWD via absolute script path → identical stdout; A3 copied corpus under a path with spaces and non-ASCII → identical stdout (expected safe because no comparison consumes a local path).
- A4 unchanged historical inputs: before/after sha256 of all `corpus/fixtures/pe-r5{5,6,7}/*` and `corpus/live/runs/round-5{5,6,7}/{inspection.raw.json,receipt.json}` match the values in §1 (r55 raw `54ffdeab…`, r56 `59a95f9d…`, r57 `5c915ebd…`).
- A5 isolated-copy forgeries, each expected nonzero with the cited check: `normalized_result.artifact.path` → `r55 artifact`; `receipt.command` path token → `r55 receipt`; r56 saved `images[1].candidate_resource_indices` → `r56 normalized result`; r57 `images[1].size_matches` → `r57 normalized result`; saved `resources[2].name.location` → `r{r} normalized result`; saved `directories[*]`/entry location → same. Known pass-through (finding 1): `parameters.path`/`locations[0].path`-only forgery — do not count this verifier as rejecting it.
- A6 static guard: `grep -n 'str(fixture)' corpus/verify_named_multi_icon_states.py` empty; no `read_bytes`/`open` under `HIST`; `HIST` literal matches `brief.md:9` root exactly.
- A7 baseline census re-run (baseline.txt command) → `verify_named_multi_icon_states.py exit=0`, `REPLAY 8/10`; siblings `verify_icon_states`/`verify_multi_icon_states`/`verify_icon_languages` outcomes unchanged.

Observed: §1 facts, diff, line cites. Inferred: A1–A5 runtime outcomes follow deterministically from the static semantics above (tests not executed here). Unknown: actual acceptance results, current existence of the historical root path (never probed, deliberately), producer authentication (explicitly out of claim).
