# ReplayScout — fleet round-1 reconnaissance

Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin` (git toplevel of the same name; `corpus/**` is tracked).
Measured baseline commit: `286033c5f2b1683fb538e86e15667709bb49b054`.
Method: source reading of the four cross-record PE state verifiers + saved-run JSON schema census.
**No verifier script, fixture or PE image was executed.** The only commands I ran were read-only JSON
parsing and `sha256sum` over corpus files (data-only census/hashing, no producer calls, no fixture execution).
All pass/fail diagnostics quoted below are quoted from `reports/round-1/baseline.txt` (observed), not re-produced.
All line pointers are coordinates in **baseline commit `286033c5…`** (`git show 286033c5:corpus/…`), because the
working tree's in-scope verifier diverged mid-flight while this reconnaissance ran (see §9).

---

## 1. The four cross-record PE state verifiers (inherited calibration denominator)

All four live at `<lane-root>/corpus/`, resolve their data root from their own file and read both frozen
fixture bytes and the saved REA record, then compare the saved record against a byte-derived decode.

| # | Path (lane-relative) | PE shape enforced | Rounds (`EXPECTED` keys) | Fixture bytes |
|---|---|---|---|---|
| 1 | `corpus/verify_icon_states.py` | **PE32** — `u16(opt)==0x10b and opt_size==224 and sections==1` (l.21) | 36, 37, 38, 39 (l.104-117) | 1024 B each |
| 2 | `corpus/verify_multi_icon_states.py` | **PE32+** — `u16(opt)==0x20b and u16(pe+20)>=240` (l.20) | 42, 43, 44, 45 (l.104-117) | 1536 B each |
| 3 | `corpus/verify_icon_languages.py` | **PE32+** (l.20) | 47, 48, 49 (l.104-114) | 1536 B each |
| 4 | `corpus/verify_named_multi_icon_states.py` | **PE32+** (l.19) | 55, 56, 57 (l.56) | 1536 B each |

Baseline diagnostics, `reports/round-1/baseline.txt` (ten-verifier `--self-test` census, lane root):

```
verify_icon_languages.py        exit=1  AssertionError: r47: artifact
verify_icon_states.py           exit=0  PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
verify_multi_icon_states.py     exit=1  AssertionError: r42: artifact
verify_named_multi_icon_states.py exit=1 AssertionError: r55 artifact
REPLAY 7 / 10
```

Calibration denominator is these four (`reports/round-1/brief.md`, "runnable existing cross-record PE state
ledgers / four existing scripts"); baseline **1/4** (only `verify_icon_states.py` passes), expected **2/4**
after the single in-scope fix, and **8/10** in the ten-verifier census.

The other six census scripts are not cross-record PE *state* ledgers: `verify_pe_resources.py` (l.9-13) is a
single-round (r27) saved-relation check whose `NEGATIVE REJECTED payload relation mismatch` line comes from its
`--self-test` mutation path (l.57-69); `verify_evm_evidence.py` is likewise single-round (r19, l.11-12);
`verify_js_graph_delta.py`, `verify_saved_evidence.py`, `verify_semantic_trace.py`, `verify_shape_evidence.py`
are bounded single-claim checks. Only `verify_pe_resources.py` (l.60) and `verify_evm_evidence.py` (l.66) parse
`sys.argv`; for all four PE-state verifiers `--self-test` is an inert argument (no `sys.argv` reference), so the
census exit codes are plain `main()` exit codes.

## 2. Path handling — why the three fail and the one does not

Current vs historical location (observed):

| role | value |
|---|---|
| historical producer corpus root (inside every saved record) | `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus` |
| current lane corpus root (`Path(__file__).resolve().parent`) | `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus` |
| resolved current fixture path, e.g. r55 | `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/pe-r55/fixture.exe` |
| path stored in that same record (`normalized_result.artifact.path`) | `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/pe-r55/fixture.exe` |

The relocation is byte-identical, not semantic: every one of the ten `corpus/verify_*.py` files and all fourteen
PE fixtures (`pe-r36..r39`, `pe-r42..r45`, `pe-r47..r49`, `pe-r55..r57`) hash equal between the current checkout
and the historical tree (sha256, checked). So every digest/Evidence-ID/payload assertion still holds, and the
**only** failing comparison class is "stored historical path vs. computed current path".

Per-verifier handling (line pointers are exact; `root`/`ROOT` = own-file directory):

| verifier | data root | fixture read | compared against computed path? |
|---|---|---|---|
| `verify_icon_states.py` | l.9 `root` | l.121 `root/'fixtures/pe-r{r}/fixture.exe'` | **NO** — only `artifact['sha256']` (l.131) and `artifact['bytes']` (l.132); the stored `artifact['path']` is never asserted → passes |
| `verify_multi_icon_states.py` | l.8 `root` | l.121 | **YES** — l.130 `report['normalized_result']['artifact']==dict(path=str(fixture),…)` |
| `verify_icon_languages.py` | l.8 `root` | l.118 | **YES** — l.127 `record['normalized_result']['artifact']==dict(path=str(fixture),…)` |
| `verify_named_multi_icon_states.py` | l.7 `ROOT` | l.65 `ROOT/f'fixtures/pe-r{r}/fixture.exe'` | **YES, twice** — l.67 artifact dict, and l.58 (`compare_normalized` embeds `artifact=dict(path=str(fixture),…)`) reached via l.68; plus **receipt command** l.69-70 `f'npx -y rea-agents@6.4.0 inspect-pe-resources {fixture} --format json'` |

The assertion texts fingerprint each baseline line unambiguously: `verify_icon_states` renders no artifact
message at all; `verify_multi_icon_states` (l.130) and `verify_icon_languages` (l.127) use `f'r{…}: artifact'`
(colon) → `r42: artifact` / `r47: artifact`; `verify_named_multi_icon_states` (l.67) uses `f'r{r} artifact'`
(no colon) → `r55 artifact`. Exactly the three observed failures, in the first-iterated key of each script's
`EXPECTED` dict (42, 47, 55).

Receipt file-name/schema differences across the four (relevant to any replay fix):

| verifier | receipt file read | receipt fields asserted |
|---|---|---|
| `verify_icon_states.py` | `producer-receipt.json` (l.142) | `exit_code`, `fixture_sha256`, `raw_output_sha256` **or** `stdout_sha256` (l.144); `evidence_id` skipped for r36 (l.145-146) |
| `verify_multi_icon_states.py` | `producer-receipt.json` (l.124) | `exit_code`, `fixture_sha256`, `evidence_id`, `stdout_sha256` (l.139-140); **no command check** |
| `verify_icon_languages.py` | `producer-receipt.json` (l.123) | same four (l.140-141); **no command check** |
| `verify_named_multi_icon_states.py` | **`receipt.json`** (l.65) | `command` equality, `exit_code`, `fixture_sha256`, `evidence_id`, `stdout_sha256`, `duration_seconds` numeric ≥0 (l.70) |

Observed receipt-schema heterogeneity in the frozen inputs: r36 carries `raw_output_sha256`/`raw_output_bytes`
and no `evidence_id`; r32 carries `stderr` + `duration_seconds`; r42-49 carry the four standard fields and no
`duration_seconds`; r55-57 (`receipt.json`) add `duration_seconds`. Only `verify_named_multi_icon_states.py`
reconstructs the receipt command string, and it reconstructs it from the **current** fixture path.

## 3. Why only `verify_named_multi_icon_states.py` is in scope

Observed from the brief, SCORECARD and the assertion sets:

1. The round's one claim names exactly this verifier and its records: "the existing named two-image PE
   saved-record verifier must replay…", scope r55-r57 (the UTF-16 named entries `A😀B!`).
2. Calibration arithmetic pins the count, not the choice: baseline 1/4, "expected after 2/4" — one of the three
   failing scripts is fixed, the other two keep failing by design. Fixing a different single script would also
   read 2/4, so the pin comes from the acceptance list, not the arithmetic.
3. The acceptance criteria enumerated in the brief map onto this script's assertion set only:
   - second-candidate claim → l.86-88 (r56 forgery, `candidate_resource_indices=[1]` at l.88)
   - size match → l.86/l.89 (r57 forgery, `size_matches=True` at l.89)
   - name location → l.72 exact named entry `{'name':'A😀B!','utf16le_hex':'41003dd800de42002100'}` at
     `{'offset':736,'bytes':12}`
   - ancestor location → `entry_locations` per resource inside the full normalized-result equality (l.28,
     l.37, l.58/68)
   - historic artifact path / receipt command → l.67 and l.69-70
   `verify_multi_icon_states.py` and `verify_icon_languages.py` assert neither a receipt command nor any named
   entry — both reject named keys outright (`require(not identifier & 0x80000000, 'this fixture must use
   numeric IDs')` at l.52 in each) — so they cannot exercise the name-location/ancestor-location criteria.
4. Historical pass record for this same script at the historical location: `SCORECARD.md` calibration row
   (r58: `python3 .shokunin/revenger/corpus/verify_named_multi_icon_states.py` exit0 → 3/3 normalized records,
   2/2 forged claims rejected) and the author-side `corpus/live/runs/round-58/reviewer.md`
   (`PASS: 139 positive checks; 2/2 forged claims rejected`). `round-58/` holds only `reviewer.md` + `LEDGER.md`
   (no `inspection.raw.json`). That r58 text also records the historical in-record offsets the current script
   still asserts: ancestor entry offsets `[536,592,664]`, name at offset 736 / 12 bytes, r56 delta
   `[(928,2,3)]`, r57 delta `[(924,48,47)]`.

## 4. Saved-run input schema the replay consumes

`corpus/live/runs/round-{r}/inspection.raw.json` (15 top-level keys, identical set for r42/r47/r55/r56/r57):
`evidence_id, subject{name,digest.sha256,local_path,format,architecture}, provider{id:'rea-pe-resources',
name,version:'1'}, analysis_profile, predicate_type:'rea.analysis', operation:'inspect_pe_resources',
parameters{path,max_file_bytes,max_entries}, raw_result (null for all five rounds), normalized_result, confidence:'observed',
authority:'shipped-artifact', environment (null), limitations, locations[{kind:'artifact-path',path}],
evidence_links`.
`normalized_result` keys: `artifact{path,sha256,bytes}, format:'pe32-plus', machine, directory{rva,location,
data_directory_location}, directories[], resources[], icon_groups[], coverage{status:'complete',
examined_entries,resources}, limitations[3]` — identical key sets for r42/r47/r55/r56/r57.

Four path-bearing fields exist inside one saved record; **only the first two are asserted by the in-scope
verifier**:
1. `normalized_result.artifact.path` — asserted (l.67, l.58); must equal the historical path, never `str(fixture)`.
2. receipt `command` — asserted (l.70); embeds the same historical fixture path.
3. `subject.local_path` — present, **not asserted** by any of the four.
4. `parameters.path`, `locations[0].path` — present, **not asserted** by any of the four.
Fixture-side inputs: `corpus/fixtures/pe-r{r}/fixture.exe` (bytes, frozen) and `corpus/fixtures/pe-r{r}/truth.json`
(present for all fourteen; **none of the four verifiers reads `truth.json`** — decoding is byte-derived).
Note `truth.json` itself references sibling fixtures relatively (`"source_fixture": "../pe-r42/fixture.exe"`),
i.e. it is location-independent.

## 5. Seven-family coverage proxy — presence only (confirmed)

Confirmed: the coverage number is **saved-record presence only**, computed by an inline command in
`reports/round-1/baseline.txt` — it is not checked-in code anywhere in the corpus. Its predicate is
"file under `corpus/live/runs/**/*.json` whose parsed object has `evidence_id` and non-null `normalized_result`,
counted by the `operation` string", intersected with a hand-written family→operation map:

- native-static ← `inspect_pe_resources`; managed ← `inspect_managed_artifact`; JavaScript ←
  `analyze_javascript_application`; Android ← `inspect_android_package`; archives ← `inventory_artifact`,
  `inspect_artifact`; firmware ← `inspect_firmware_regions`; browser-runtime ← `inspect_web_page`,
  `capture_browser_scenario`, `observe_web_session`.

Independent read-only reproduction (my own census, no verifier executed) — operation counts and 3/7 = 4.29 match
the baseline exactly:

```
analyze_javascript_application 6   compare_application_versions 1   compare_javascript_export_shapes 3
extract_artifact 2   inspect_analysis_view 1   inspect_artifact 4   inspect_evm_interface 7
inspect_pe_resources 30   trace_application_feature 2   trace_javascript_semantics 2      (total 58)
present = native-static, javascript, archives           0 parse failures
```

The seven-family taxonomy itself has a domain anchor in `PROVINCE.md` (Owns: native binaries, managed
assemblies, Electron/JavaScript packages, Android APKs, archives, firmware, browser/Electron runtime evidence);
`MISSION.md`/`AXES.md` in the fleet root do not enumerate families, so the brief is the working authority.

## 6. Omitted surfaces and limitations (not inflated)

Present in the saved corpus but **mapped to no family** (11 records): `inspect_evm_interface` **7**
(rounds 19-26; saved EVM records, `verify_evm_evidence.py` covers only the r19 one) — explicit in the brief as
out of the seven; `compare_application_versions` 1, `compare_javascript_export_shapes` 3,
`extract_artifact` 2, `inspect_analysis_view` 1, `trace_application_feature` 2, `trace_javascript_semantics` 2.
21 further files in `corpus/live/runs/**` carry an `evidence_id` but no `operation`/`normalized_result` and are
excluded by the predicate (all are receipts: 16 `producer-receipt.json` + 5 `receipt.json`, incl. both r59 ones).

Mis-attribution inside the map (observed, one record): `inspect_artifact` subjects include the **ELF** binary
`fixtures/checksum-r1/checksum` (`corpus/live/runs/20261012T163909Z/artifact-inspection.json`), plus three ZIPs.
The map files every `inspect_artifact` record under **archives**, so a native-binary evidence record is booked as
archives coverage. `extract_artifact` (2, both ZIP) is archives-flavoured but outside the map.

Proxy limitations by construction: presence is not authentication, not producer/runtime availability, not
receipt consistency, and not correctness — an operation string lives in the saved JSON (untrusted target
content) and is never cross-checked. Primary-key collisions/duplicates and per-family depth are not measured.
Underlying fixture breadth is thin: all 30 `inspect_pe_resources` records are authored 1 KB/1.5 KB synthetic PE
fixtures (rounds 27-59), so "native-static" presence does not represent general native-binary capability.

## 7. Inferred (not observed)

- **[INFERENCE, high confidence]** All three keys of each failing script fail identically, not just the
  first-iterated one: the comparator and the historical prefix are the same for every round and both sides carry
  the round number symmetrically (e.g. `…/pe-r56/fixture.exe` vs `…/pe-r56/fixture.exe`). Unverified because
  `main()` aborts on the first `AssertionError`. So r43-r45, r48-r49, r56-r57 per-record status is unknown.
- **[INFERENCE]** `verify_named_multi_icon_states.py`'s two forgery checks (baseline l.86-95) are currently
  unreachable: they run only after `{r: check(r) for r in EXPECT}` (l.75) succeeds, so the `2/2 forged claims
  rejected` line is dead until the path comparators are repaired. A repaired script must keep the rejection text
  exactly `f'r{r} normalized result'` (l.94) or its own forgery assertions break — brittle coupling to
  `compare_normalized`'s message.
- **[INFERENCE, design risk — not decided here]** The historical tree still exists on this machine and is
  byte-identical to the checkout, so an implementation that validates the "independently pinned historical path"
  by touching that directory would pass locally while depending on a tree that a standalone replay/copy is not
  obligated to have. The brief's acceptance ("copied corpus under a path with spaces and non-ASCII",
  "never accept a path by copying it out of the field under test") reads as requiring a declared pinned constant
  compared as string data, not a second filesystem read.

## 8. Remaining defects — explicitly NOT fixed in this lane

1. `corpus/verify_multi_icon_states.py:130` — identical defect (full artifact dict vs `str(fixture)`), still
   exits 1 at `r42: artifact`. Out of scope by the brief's one-claim pin.
2. `corpus/verify_icon_languages.py:127` — identical defect, still exits 1 at `r47: artifact`. Out of scope.
3. `corpus/verify_named_multi_icon_states.py` (baseline l.67, l.58 reached via l.68, and l.69-70) — the coupled
   path sites: the artifact dict compare, the artifact path embedded in `compare_normalized`'s expected tree, and
   the receipt command built from `str(fixture)`; relaxing only l.67 still fails at l.68/l.70. Not fixed by me
   (binding/implementation lane owns it); see §9 for the concurrent working-tree state I observed.
4. Named verifier covers only two forgeries (r56 candidate, r57 size). The brief's acceptance adds rejections for
   forged historic artifact path, forged receipt command, name location and ancestor location — those are
   currently only positive-checked (l.72, and full-equality via l.68), so they are a new-obligation gap, not a
   regression, and remain unimplemented.
5. No verifier covers the r59 / r59d saved records (`round-59/`, `round-59/devin-author/`, fixtures `pe-r59`,
   `pe-r59d`); the r59 malformed-name validity criterion stays halted per the brief.
6. `verify_icon_states.py:144-146` r36 special-case (receipt field name + missing `evidence_id`) remains a
   historical schema quirk left in place; receipts are heterogeneous across rounds (see §2).
7. The coverage proxy remains an inline command in `reports/round-1/baseline.txt` with the map in §5 — no
   checked-in counting script, so its reproducibility depends on quoting that command verbatim.

## 9. Concurrent working-tree divergence (observed, not my delta)

Between my first and second source read of `corpus/verify_named_multi_icon_states.py`, the working tree moved:
`git diff --stat 286033c5 -- corpus/` reports **exactly one** corpus file changed — that verifier, 9 insertions /
7 deletions; the other nine verifiers are byte-identical to the baseline commit. Observed in the working tree:

- new l.9 `HIST=Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')` — the historical path
  as a declared constant, matching the historical identity embedded in every saved record;
- `hist=HIST/f'fixtures/pe-r{r}/fixture.exe'` bound in `check` (working-tree l.67) and passed to
  `compare_normalized` in the forgery path (working-tree l.94).

I did not read that edit beyond these grep hits, did not run it, and make no correctness claim about it — it is
the binding lane's artifact and the parent's acceptance call. Two scout-side observations only:
(a) the observed `hist` binding is a pure path construction (`HIST/f'fixtures/pe-r{r}/fixture.exe'`), i.e. usable
as string data without reading the historical tree — the shape the brief's "independently pinned historical path"
implies; I did not read enough of the edit to claim whether the directory is touched elsewhere (only grep hits);
(b) the baseline coordinate map in §2-§3, §7 and §8 is now partially offset in the working tree (l.67/l.94), so
any future citation must name the tree it refers to.
My own write scope was `reports/round-1/scout.md` only; the inherited untracked
`reports/round-1/{brief.md,baseline.txt,dispatch.json}` are untouched.