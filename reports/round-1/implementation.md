# Round-1 implementation receipt — ReplayImplementation

Target: `corpus/verify_named_multi_icon_states.py` (sole code write). Baseline commit 286033c5f2b1683fb538e86e15667709bb49b054. Snapshot after edit: tag #6C93.

## Exact changes (4 surgical edits, line numbers post-edit)

1. L8-9 (added): `HIST=Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')` with comment marking it historical-identity-only, never read through. `ROOT` (L7) unchanged and still sole source of all file reads.
2. L59-60 (`compare_normalized`): parameter `fixture`→`hist`; expected artifact still `dict(path=str(hist),sha256=digest,bytes=length)` — same exact-equality semantics, now fed the historical identity. Internal rename only; all callers positional, no API surface change.
3. L67-71 (`check`): added `hist=HIST/f'fixtures/pe-r{r}/fixture.exe'` beside the unchanged `fixture=ROOT/...` (used only for `read_bytes`); `r{r} artifact` equality, full `compare_normalized` replay, and receipt `command` expectation (`npx -y rea-agents@6.4.0 inspect-pe-resources {hist} --format json`) now use `hist`.
4. L94 (`main` forged controls): `compare_normalized(...,HIST/f'fixtures/pe-r{r}/fixture.exe',...)` replaces the ROOT-derived path, so r56 candidate and r57 size rejections stay attributed to forged content (`r{r} normalized result`), not an incidental path mismatch.

Expected historical path is derived solely from the pinned constant; no expectation is ever copied from a saved field under test.

## Preserved untouched

Fixture digests and Evidence IDs (`EXPECT`), byte decoder, complete `compare_normalized` dict equality incl. three limitation strings, digest/subject/Evidence-ID/receipt-hash checks, exact UTF-16 name + location assertion, states tuples, one-byte deltas, both negative controls, `req` counter and PASS line. No saved JSON, receipt, or fixture byte was modified. No fallbacks, no new abstractions, no formatting churn.

## Observed vs inferred vs unknown

- Observed: saved r55-r57 `artifact.path` strings and receipt `command` strings equal `str(HIST/f'fixtures/pe-r{r}/fixture.exe')` and the formatted command for all three rounds (data-only census, matches EXPECT digests/IDs and baseline.txt cause line).
- Inferred from code (not executed): verifier now replays from any local checkout path (reads via ROOT); a saved artifact path or receipt command rewritten to the new checkout fails at `r{r} artifact` / `r{r} receipt`; forged second-candidate and size-match claims fail at `r{r} normalized result`.
- Unknown: actual CLI acceptance result — per instructions no build/test/CLI run was performed; parent executes after integration.

## Limits

- Authored r55-r57 fixtures only; not general PE validation.
- `HIST` is the immutable recorded identity of these exact saved r55-r57 Evidence records; it MUST NOT be edited on any future relocation of this corpus. Only `ROOT` follows a local checkout move. The historical directory need not exist locally; `HIST` is never read through. An intentional change of the recorded producer identity would require re-production of the saved Evidence, not editing this constant.
- Same failure mode exists in `verify_multi_icon_states.py` (r42) and `verify_icon_languages.py` (r47); left untouched — out of this lane's scope.
- Reviewer/critic notified for static review only; their replies are author-side evidence, not independent promotion verification.
