# Revenger — kaika continuation plan

Planning only; no claim is scored, admitted, integrated, or completed here. The worktree HEAD was `8bbcb4e3267d155525c1ef1258ee327b49e53ec4` (`git rev-parse HEAD`). `dispatch.md:22-23` records that L1 wrote the map, quality bar, and lesson before dispatch; the map is a pre-admission snapshot. L1 owns canonical source-row integration, post-admission map updates, and the seed/readiness headers.

**Proposed round axes:** calibration (C1), coverage (C2), and freshness (C3). `SCORECARD.md:79-86` has coverage/calibration scores but currently labels freshness non-assigned; the L1-authored `ufo-round-plan-v1` must explicitly add freshness for C3, without inventing a baseline score. `sources-curation` is a capability claim, not a fourth axis. These are distinct axes under fleet `AXES.md:25-35`.

## Map audit

### Census evidence

The current map has fourteen rows and these status counts; command run from the lane root:

```sh
python3 -B -c 'from pathlib import Path
from collections import Counter
rows=[line for line in Path("corpus/README.md").read_text().splitlines() if line.startswith("| C")]
c=Counter(line.split("|")[-2].strip() for line in rows)
print("rows",len(rows)); print("statuses", " ".join(f"{k}={c[k]}" for k in sorted(c)))'
```

```text
rows 14
statuses frontier=4 partial=6 uncovered=4
```

Fixture inventory command and output (includes gaps hidden by the map's `…` shorthand):

```sh
python3 -B -c 'from pathlib import Path
root=Path("corpus/fixtures")
dirs=sorted(p.name for p in root.iterdir() if p.is_dir())
with_truth=sorted(p.name for p in root.iterdir() if p.is_dir() and (p/"truth.json").is_file())
without_truth=sorted(p.name for p in root.iterdir() if p.is_dir() and not (p/"truth.json").is_file())
pe=[x for x in dirs if x.startswith("pe-r")]
evm=[x for x in dirs if x.startswith("evm-r")]
print("DIRS",len(dirs),"TRUTH",len(with_truth),"WITHOUT_TRUTH",len(without_truth),without_truth)
print("PE",len(pe),pe)
print("EVM",len(evm),evm)'
```

```text
DIRS 44 TRUTH 40 WITHOUT_TRUTH 4 ['checksum-r1', 'js-r3', 'js-r7-v2', 'shapes-r12']
PE 30 ['pe-r27', 'pe-r28', 'pe-r29', 'pe-r30', 'pe-r31', 'pe-r32', 'pe-r33', 'pe-r34', 'pe-r35', 'pe-r36', 'pe-r37', 'pe-r38', 'pe-r39', 'pe-r41', 'pe-r42', 'pe-r43', 'pe-r44', 'pe-r45', 'pe-r47', 'pe-r48', 'pe-r49', 'pe-r51', 'pe-r52', 'pe-r53', 'pe-r54', 'pe-r55', 'pe-r56', 'pe-r57', 'pe-r59', 'pe-r59d']
EVM 7 ['evm-r19', 'evm-r21', 'evm-r22', 'evm-r23', 'evm-r24', 'evm-r25', 'evm-r26']
```

Saved-record census F was run at base `8bbcb4e`; its exact counting command is `SCORECARD.md:48-56`:

```sh
python3 -B -c 'import collections,json,pathlib
c=collections.Counter()
for p in sorted(pathlib.Path("corpus/live/runs").rglob("*.json")):
 try: x=json.loads(p.read_bytes())
 except (ValueError,UnicodeError): continue
 if isinstance(x,dict) and x.get("evidence_id") and x.get("normalized_result") is not None: c[x.get("operation","unknown")]+=1
families={"native-static":{"inspect_pe_resources"},"managed":{"inspect_managed_artifact"},"javascript":{"analyze_javascript_application"},"android":{"inspect_android_package"},"archives":{"inventory_artifact","inspect_artifact"},"firmware":{"inspect_firmware_regions"},"browser-runtime":{"inspect_web_page","capture_browser_scenario","observe_web_session"},"evm":{"inspect_evm_interface"}}
present=[k for k,v in families.items() if v.intersection(c)]
print(json.dumps(c,sort_keys=True)); print("COVERAGE",len(present),"/",len(families),"score=",10*len(present)/len(families),"families=",present)'
```

```text
{"analyze_javascript_application": 6, "compare_application_versions": 1, "compare_javascript_export_shapes": 3, "extract_artifact": 2, "inspect_analysis_view": 1, "inspect_artifact": 4, "inspect_evm_interface": 7, "inspect_pe_resources": 30, "trace_application_feature": 2, "trace_javascript_semantics": 2}
COVERAGE 4 / 8 score= 5.0 families= ['native-static', 'javascript', 'archives', 'evm']
```

### Row-by-row check

`README.md:18-22` defines the status vocabulary and keeps fixture/run evidence distinct from knowledge. The statuses below match the **frozen pre-admission map**; current knowledge drafts are not admitted until L1 integrates the canonical registry and runs the Q gate.

| Row | Status check | Work-evidence check |
|---|---|---|
| C01 | `uncovered` is the frozen pre-admission value; no admitted C01 entry at freeze. The new PE-layout draft is not yet admitted. | Fixture/verifier evidence exists. `pe-r27…pe-r59d` is sparse shorthand; exact present set is in the inventory output above. |
| C02 | `partial` matches the pre-contract seed/checklist entries. | **Wrong/incomplete pointer:** the cell names a lesson, not the saved provider run. Corrected value: `live/runs/20261012T163909Z/native-analyze.json`, `live/runs/20261012T163909Z/LEDGER.md`; retain the lesson only as context. The run is `provider_unavailable` (`LOG.md:26-30`). |
| C03 | `frontier` matches no managed fixture/family record in the fixture inventory and F output. | `—` is correct; `dotnet` on PATH alone is not a saved managed record or capability. |
| C04 | `uncovered` matches work evidence without an admitted C04 entry. | The listed JS fixtures/verifiers exist; F has JavaScript records. `verify_saved_evidence.py` also checks the r3 JS parent (`verify_saved_evidence.py:2,15-19`), a useful additional pointer if this cell is meant to be exhaustive. |
| C05 | `frontier` matches no APK fixture or Android family record. | `—` is correct; `jadx` presence is not an APK record. |
| C06 | `partial` matches the checklist's archive-tool-only pre-contract knowledge. | The three named archive fixtures exist; F has archive inventory/extraction records. The shared `verify_saved_evidence.py` also covers r2 ZIP evidence (`:2,13-18`); optional completeness pointer, not a false current value. |
| C07 | `frontier` matches no firmware fixture/family record. | `—` is correct despite the current `binwalk`/`unblob` paths; F has no firmware operation. |
| C08 | `frontier` matches no saved browser-runtime family record. | `—` is correct; no browser-runtime operation appears in F. |
| C09 | `uncovered` matches EVM work without an admitted entry. | `evm-r19…evm-r26` is sparse shorthand: actual folders are `evm-r19`, `evm-r21`–`evm-r26` (no `evm-r20` fixture); the verifier exists. |
| C10 | `partial` matches pre-contract seed text. | `verify_saved_evidence.py` exists; saved-ledger evidence is present. |
| C11 | `uncovered` is the frozen pre-admission value; the UTF-16 draft is not yet admitted. | The `pe-r51…pe-r59` shorthand skips `pe-r58`; exact relevant folders in the inventory are `pe-r34`, `pe-r51`–`pe-r57`, `pe-r59`, and `pe-r59d`. |
| C12 | `partial` matches the pre-contract calibration-strategy text. | `truth.json` is a qualified subset, not every fixture directory: the inventory command reports the source-only exceptions. The new tool-validation draft is not yet admitted. |
| C13 | `partial` matches the pre-contract fixture-provenance text. | The lesson gate and `reports/round-1/` exist; the new digest-scope draft is not yet admitted. |
| C14 | `partial` matches the pre-contract readiness checklist. | `—` is correct for `corpus/live/runs/`; the current round's recheck report is under `.ufo/waves/`, not a saved REA run record. |

The C02 correction is directly shown by this executed command/output:

```sh
for p in corpus/live/runs/20261012T163909Z/native-analyze.json corpus/live/runs/20261012T163909Z/LEDGER.md; do test -e "$p" && printf 'present %s\n' "$p" || printf 'absent %s\n' "$p"; done
```

```text
present corpus/live/runs/20261012T163909Z/native-analyze.json
present corpus/live/runs/20261012T163909Z/LEDGER.md
```

At planning time, `corpus/SOURCES.md` is absent, while the new PE-layout, UTF-16, tool-validation, and digest-scope files are present. Their source notes use temporary `T3-*`/`T4-*` identifiers (and the freshness edits refer to `S001`/`S002`); they remain pre-admission drafts until L1 creates the canonical `S###` rows. This state was checked with the following command:

```sh
for p in corpus/SOURCES.md corpus/knowledge/pe-resource-directory-layout.md corpus/knowledge/utf16-unpaired-surrogates-in-resource-names.md corpus/knowledge/tool-validation-by-function-and-version.md corpus/knowledge/digest-scope-versus-provenance.md; do test -e "$p" && printf 'present %s\n' "$p" || printf 'absent %s\n' "$p"; done
```

```text
absent corpus/SOURCES.md
present corpus/knowledge/pe-resource-directory-layout.md
present corpus/knowledge/utf16-unpaired-surrogates-in-resource-names.md
present corpus/knowledge/tool-validation-by-function-and-version.md
present corpus/knowledge/digest-scope-versus-provenance.md
```

## Claim acceptance

### C1 — saved-ledger runnability (calibration)

**Before at base.** `git rev-parse HEAD` returned `8bbcb4e3267d155525c1ef1258ee327b49e53ec4`. Ran SCORECARD command C (`SCORECARD.md:35-42`) from the lane root:

```sh
python3 -B -c 'import pathlib,subprocess,sys
ps=sorted(pathlib.Path("corpus").glob("verify_*.py"))
rows=[(p.name,subprocess.run([sys.executable,"-B",str(p),"--self-test"],capture_output=True,text=True)) for p in ps]
for name,r in rows: print(name,"exit="+str(r.returncode),(r.stdout+r.stderr).splitlines()[-1])
names={"verify_icon_states.py","verify_multi_icon_states.py","verify_icon_languages.py","verify_named_multi_icon_states.py"}
ok=sum(r.returncode==0 for name,r in rows if name in names)
print("CALIBRATION",ok,"/",len(names),"score=",10*ok/len(names))
print("REPLAY",sum(r.returncode==0 for _,r in rows),"/",len(rows))'
```

```text
verify_evm_evidence.py exit=0 NEGATIVE REJECTED candidate destination mismatch
verify_icon_languages.py exit=1 AssertionError: r47: artifact
verify_icon_states.py exit=0 PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
verify_js_graph_delta.py exit=0 NEGATIVE REJECTED saved graph disagrees with source truth
verify_multi_icon_states.py exit=1 AssertionError: r42: artifact
verify_named_multi_icon_states.py exit=0 PASS: 139 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
verify_pe_resources.py exit=0 NEGATIVE REJECTED payload relation mismatch
verify_saved_evidence.py exit=0 NEGATIVE JS REJECTED: JS: wrong package-main mapping
verify_semantic_trace.py exit=0 NEGATIVE REJECTED relation differs from source parent
verify_shape_evidence.py exit=0 NEGATIVE REJECTED changed-property evidence mismatch
CALIBRATION 2 / 4 score= 5.0
REPLAY 8 / 10
```

**After gate:** the same C command prints `CALIBRATION 4 / 4`; both repaired scripts exit zero with their existing forged-claim rejection intact; the other selected negative controls remain rejected; and byte comparisons against base show no fixture or `corpus/live/runs/` record changed. Keep the known-good split from `verify_named_multi_icon_states.py`: current `ROOT` supplies bytes, independently pinned historical `HIST` supplies expected artifact/receipt identity (`verify_named_multi_icon_states.py:7-9,59-72`; fix commit `7c3ce19`).

**Falsifiers:** (1) C remains below `4 / 4` or either target self-test exits nonzero. (2) Any existing forged input is accepted, or any fixture/saved-run bytes differ from the base snapshot.

### C2 — coverage plus `sources-curation` capability

**Before at base.** Ran the base tree inventory:

```sh
git ls-tree -r --name-only 8bbcb4e -- corpus/SOURCES.md corpus/knowledge
```

```text
corpus/knowledge/2026-10-12-rea-readiness-checklist.md
corpus/knowledge/seed.md
```

No canonical `SOURCES.md` existed; the current source-note drafts and new knowledge entries are listed in the Map audit, but their `T3-*`/`T4-*` IDs are not canonical registry IDs.

**After gate:** L1 integrates a `corpus/SOURCES.md` with the frozen contract's Registry, Paths, Search log, and Leads sections; maps temporary IDs to unique `S###` rows; records every new row's opened date, exact anchor, scoped tier, grounded `teaches`, status/recheck/used-by; and runs all census commands in `SOURCES-CONTRACT-v1.md:64-80`. Every in-scope knowledge entry must cite a real tier-A `S###` row opened this round, have `source:`, `verified-at:`, `recheck:`, and `coverage-map:` headers, separate observation/inference/unknown, name a limitation, and pass Q01–Q10 (`QUALITY.md:13-30`). The source contract's non-author sample reopens a row. Representative vertical slice: C01 PE-layout source → `pe-resource-directory-layout.md` → byte-derived command → full Q gate → admitted row; apply the same gate to every other in-scope entry. Only after admission should README rows/statuses and the `sources-curation` capability row be updated. F remains `4 / 8` unless a qualifying saved-record family is added; knowledge curation alone does not change F.

**Falsifiers:** (1) Any in-scope entry lacks a canonical source row, fails a Q criterion, or relies on a tier/source not opened for that scope this round. (2) Any SOURCES census fails, the source sample cannot be reopened, or an unadmitted draft is counted as held/capability.

### C3 — freshness of pre-contract knowledge

**Before at base.** Ran `git show 8bbcb4e:corpus/knowledge/seed.md`; relevant exact output: `## REA toolset census (probed 2026-10-12, commands + outputs on record)` and `- Host engines ABSENT at mint: ghidra, jadx, binwalk, unblob, pwntools` (`seed.md:3,12-14`). Ran `git show 8bbcb4e:corpus/knowledge/2026-10-12-rea-readiness-checklist.md`; relevant exact output: `# REA readiness checklist — 2026-10-12 (mint)` and the row `| jadx / binwalk / unblob / pwntools | ... | ABSENT |` (`2026-10-12-rea-readiness-checklist.md:1,12`). Both base files lacked the current `verified-at:`/`recheck:` headers; the base tree command above lists exactly these two knowledge files.

**Live host observation for this continuation:**

```sh
for x in dotnet jadx binwalk unblob; do printf '%s: ' "$x"; command -v "$x" || true; done
```

```text
dotnet: /usr/bin/dotnet
jadx: /usr/bin/jadx
binwalk: /usr/bin/binwalk
unblob: /home/vgpnk/.local/bin/unblob
```

The current seed and readiness documents append dated 2026-10-19 re-verification tables pointing to `.ufo/waves/kaika-r1/scout-freshness.md`; this is existing author evidence, not a probe independently rerun by this planner. **After gate:** both original entries preserve their 2026-10-12 snapshot and carry dated live re-probe commands/results; every changed fact is explicitly `STALE → current`, holds are recorded, and inaccessible/unprobed capability remains UNKNOWN. C3 measures freshness of these two entries only, not REA route readiness. L1 owns the source/header integration.

**Falsifiers:** (1) Either entry lacks a dated live recheck, or a known-stale 2026-10-12 fact remains stated as current. (2) A PATH/version observation is presented as an exercised REA capability, or a fact without a live probe is silently upgraded instead of marked UNKNOWN/stale.

## Execution order

1. **Freeze baseline and axes.** Preserve the command/output blocks above; keep coverage's fixed-family F proxy distinct from knowledge-map coverage, and declare freshness explicitly. Evidence: C, F, map census, fixture inventory, base tree listing.
2. **Land C1 alone.** Apply the ROOT/HIST relocation pattern to the two failed verifiers; run both self-tests and C; compare fixture/run bytes to base. Evidence: C output, negative-control lines, unchanged-byte result.
3. **Curate C2.** Use the opened-source notes as inputs, normalize IDs into L1's canonical `SOURCES.md`, check every entry against Q01–Q10, reopen a non-author sample, and update map statuses only after admission. Evidence: source rows/anchors, census outputs, per-entry Q table, sample review, resulting map rows.
4. **Close C3 independently.** Retain both old snapshots; check the two live recheck records and explicitly flag stale/unknown facts. Evidence: exact commands/outputs and date in `scout-freshness.md` and the two knowledge entries; no REA producer call is needed for this freshness-only claim.
5. **L1 gate.** Record before→after and every verdict in the canonical round plan/SCORECARD/LOG; only add `sources-curation` to capabilities if the round demonstrates the complete source-to-admitted-entry route. No integration or admission is claimed by this planner.

## Saturation

- **Proposed saturation line: 7.0/10.** Policy choice, not a measured result: both current proxies are `5.0` by C/F, so this leaves headroom and does not call the present tie saturated.
- **Proposed stagnation window: N=3 rounds.** Policy choice: wait for three full rounds without a demonstrated capability before the nudge can force a frontier move; the current capability table is empty (`SCORECARD.md:140-144`), while C2 can establish the first capability and reset that window.

## Planned

**Next-round claim set (one claim):** coverage/capability acquisition on the missing firmware family. Author one inert, byte-oracle firmware fixture; re-probe `binwalk --version` and `unblob --version` against `PROVINCE.md:56-57`; run REA `inspect_firmware_regions` and `extract_firmware` only on that fixture; compare reported regions and extracted bytes to the independently authored manifest; save full Evidence and a non-author review. The F family key is `inspect_firmware_regions` (`SCORECARD.md:54-56`), so the future F result should move from the observed `4 / 8` to `5 / 8` only if that saved operation record has both `evidence_id` and `normalized_result` and the byte oracle agrees. `[INFERENCE]` This is the best immediate frontier candidate among the four missing F families because the required Binwalk/Unblob tools are currently on PATH and `PROVINCE.md` names their compatible version families; PATH presence still does not prove REA capability. Managed is deferred until a usable .NET SDK is verified; Android needs a known-truth APK fixture; browser-runtime needs a declared local page/CDP target. Do not combine those same-axis coverage candidates into this single claim.

**Hard blockers:** none to this plan. C2 is intentionally pending L1's canonical SOURCES/map integration after admission; C3's dated recheck artifacts are present but await that integration/review; C1 still requires its post-change run and immutable-input gate. No producer calls, installs, or live-target execution were made for this planning assignment.
