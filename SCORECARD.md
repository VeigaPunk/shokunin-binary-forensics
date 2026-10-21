# revenger scorecard — fleet round-1

Active mission axes: coverage + calibration. The imported record below had no
numeric rubric. These are newly declared, bounded 0–10 proxies, not mastery
scores or scalar round verdicts. Calibration was lowest before this move.

| axis / criterion | before → after score | evidence / command | measured commits | last change |
|---|---|---|---|---|
| calibration — selected saved-ledger runnability | 2.5 → 5.0 (`10 × 1/4 → 10 × 2/4`) | C below; `reports/round-1/measurements.json`; named r55–r57 verifier changes exit 1 → 0 | before `286033c5f2b1683fb538e86e15667709bb49b054`; after `7c3ce197341b0babe0046b1d9cbb59f1ba43f54e` | fleet round-1 |
| coverage — selected-family record presence | 5.0 → 5.0 (`10 × 4/8` both) | F below; same frozen measurements; existing native-static, JavaScript, archive, EVM records | same before/after commits | fleet round-1 initialization; unchanged |

**Verdicts:** calibration **improved** only for this saved-ledger repeatability
criterion; coverage **unchanged**. Historical depth is **unchanged**, not an
active scoring axis. No new producer, route, parser policy or runtime claim.
The two proxies tie after this move; that is not saturation.

**Rubric boundaries.** C counts the four existing cross-record PE state scripts
enumerated in its `names` set. Its broader 7/10 → 8/10 census overlaps that
subset, not a second independent competence gain. The language and numeric
multi-image verifiers still fail at their original artifact-path assertions.
F uses eight fixed selected families, including already-recorded EVM. The
inherited 3/7 = 4.29 omitted EVM; correcting the taxonomy is not coverage growth.
Record presence does not authenticate historical producer success/readiness.
Only the named ledger receives the additional relocation/tamper acceptance.

**Counting commands.** Both were executed from isolated corpus snapshots made
with `git archive --format=tar <measured-commit> corpus`; outputs and exact
command strings are committed in `reports/round-1/measurements.json` and
`reports/round-1/counting-commands.json`. The census probe exits 0 even when
constituent verifiers fail; inspect every printed exit code.

C — selected calibration and broader replay census:

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

F — selected-family saved-record presence:

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

planned: next move, calibration repeatability — isolate the existing
`verify_icon_languages.py` artifact-path failure with unchanged saved inputs;
declare its own falsifier before changing it. At the current 5.0/5.0 tie this
claim is more directly falsifiable than acquiring an unprobed producer family.
No additional verifier is changed in fleet round-1.

retired: historical depth scoring, wrong-fit for this dispatch's
coverage+calibration assignment, not saturation; findings remain below.
Calibration's historical r59 malformed-name validity/refusal criterion remains
**halted and falsified** (`LOG.md:707-721`). The newly declared repeatability
criterion neither resumes nor regrades it.

## Interactive continuation — fleet round-1 remains unadmitted

This section supersedes the earlier **planned** next move, not the imported
history or the bounded local improvement. The predecessor's nine-role batch
(`reports/round-1/batch-receipt.json`) is preserved historical dispatch evidence;
it does not satisfy the current operator's validated width-32 contract.
No completed round is added by this continuation.

| axis | current verdict | freshly exercised evidence and boundary |
|---|---|---|
| calibration — selected saved-ledger repeatability | **improved**, local behavior only; admission blocked | Baseline `286033c5f2b1683fb538e86e15667709bb49b054`: named verifier exit 1, `AssertionError: r55 artifact`. Work `7c3ce197341b0babe0046b1d9cbb59f1ba43f54e`: real CLI passes in 3/3 contexts and rejects 6/6 isolated forgeries; 9/9 original inputs byte-identical. `.ufo/waves/fleet-round-1-interactive/local-acceptance.json` contains full verdicts, commands, exits and revision hashes. The broader inherited 1/4 → 2/4 proxy is not re-counted here by retrying unrelated known failures. |
| coverage — fixed selected-family record presence | **unchanged** | Fresh isolated-archive runs at both commits: `COVERAGE 4 / 8 score= 5.0 families= ['native-static', 'javascript', 'archives', 'evm']`, exit 0 each. Exact command/output: `.ufo/waves/fleet-round-1-interactive/coverage-remeasurement.json`. Record presence is not producer authentication/readiness. |
| depth — historical guardrail, not active scoring | **unchanged** | No new REA producer, code semantics, image decode or PE runtime claim. Same r55–r57 evidence and independently pinned fixture hashes. |
| operability — not an assigned scoring axis | **unchanged** | Portable replay is counted only under the declared calibration criterion, not as a second gain. Missing contract files/registry remain named debt below. |
| freshness — not an assigned scoring axis | **unchanged** | Saved-record consistency rechecked; historical producer/native readiness not re-probed or refreshed. |
| adjacency — not an assigned scoring axis | **unchanged** | Scope remains saved PE evidence; route repair and shared-ledger integration are reported to their owners, not absorbed. |

Learning trends: expansion **unchanged** (no knowledge entry admitted);
quality **improved** only for the re-verified saved-ledger replay;
discernment **unchanged** (no non-author admit-and-reject spot-check).
`corpus/lessons/round-1.md` records the gate decisions and missing outside check.

The canonical validator accepted exactly 32 distinct scopes, exit 0, and its
pure canonical renderer succeeded, exit 0. The executed operator-route
assessment exits 2 (`could-not-evaluate`): reviewer/sentinel → `@m_mid`,
critic → `@m_strong`, scribe → `@m_fast`, connector → `@m_mid`, rather than the
required audit `@m_grok`, content `@m_composer`, and connector
`@m_antigravity` with `@m_zfl` fallback. No seats were dispatched and no
registry was persisted. `.ufo/waves/fleet-round-1-interactive/routing-assessment-run.json`
and `routing-contract.json` carry exact commands, verdicts and bindings.

**planned:** keep fleet round-1 open. Operator-owned global route bindings must
first satisfy that matrix; a fresh interactive L1 continuation revalidates the
same 32-scope spec and dispatches its complete canonical payload once, without
overlays or model pins. Reuse landed work/evidence; do not advance to the
language-ledger move or loop rounds in this session. At-least-100 remains a
fresh-session objective, not a count established here.

**Named debt:** `SKILL.md`, `AGENTS.md`, `corpus/QUALITY.md`, and
`corpus/README.md` are absent in this lane (explicit read/glob sweep).
An authorized owned-file contract-restoration move must reconstruct sourced
instructions, register any permanent gate with its real verdict/self-test
interface, and obtain a non-author admit/reject spot-check. Do not promote or
call the local acceptance runner protocol-conformant while that registry/bar
is absent. This continuation admits no new knowledge under a nonexistent bar.
Inherited language/multi-image relocation failures remain separate future
claims; unchecked Evidence envelope path fields remain a bounded verifier
limitation (`reports/round-1/reviewer.md:39`), not silently repaired scope.


## Fleet round-1 kaika continuation — axes (2026-10-19, current)

Supersedes the "planned" and "named debt" lines above for the items it lands
(`QUALITY.md` and the corpus `README.md` now exist; `SKILL.md` and `AGENTS.md`
are still absent). Earlier rows stay as recorded history (`:9`, `:19-20`, `:63`
describe the 2026-10-15 state). Measured from isolated `git archive`
snapshots of `8bbcb4e` (before) and `35b2e8b` (after) unless noted.

| axis / criterion | before → after | counting command | measured commits | verdict (pending non-author verification) |
|---|---|---|---|---|
| calibration — selected saved-ledger runnability | 5.0 → **10.0** (`CALIBRATION 2/4 → 4/4`; `REPLAY 8/10 → 10/10`, descriptive only) | C (`:32-43`) | `8bbcb4e` → `35b2e8b` | improved |
| coverage — selected-family record presence (F) | 5.0 → 5.0 (`COVERAGE 4/8` both) | F (`:45-57`) | `8bbcb4e` → `35b2e8b` | unchanged |
| coverage — knowledge-map ground (K), split from coverage this round | 0.0 → **2.9** (held rows 0/14 → 4/14; admitted entries on rows frozen uncovered/partial at `a7acc20`: 0 → 4, split 2 uncovered + 2 partial) | `grep -cE '^\| C[0-9]+ .*\| held \|$' corpus/README.md` (at `a7acc20` via `git show`); expansion script in `LOG.md` kaika entry / report | `a7acc20` → `35b2e8b` | improved |
| freshness — knowledge re-verification currency (adopted this round) | previously unscored; base text vs the live host 4.4 (8 of 18 facts hold, 10 stale and unflagged) → **10.0** (18/18 hold or flagged with current value) | `grep -cE '^\| [FK][0-9]+ .*\| (holds\|STALE)' corpus/knowledge/{seed.md,2026-10-12-rea-readiness-checklist.md}`; probes in `.ufo/waves/kaika-r1/scout-freshness.md` | `8bbcb4e` → `35b2e8b` | improved |
| depth (historical guardrail, retired) | unchanged | — | — | unchanged |
| adjacency (not owned) | unchanged; the kaidoku/revenger overlap (tsukuroi ADJ-06) is reported, not absorbed | `.ufo/waves/kaika-r1/connector.md` | — | unchanged |

Split reason (AXES.md §Working the axes): F counts saved REA record families
and cannot see sourced knowledge; K counts map rows held by gated, sourced
entries. Neither replaces the other. Freshness is adopted because 10 of 18
recorded host facts had silently drifted (`MISSION.md:49-51`, evidence-backed
axis addition). Correction to `:135`: "evidence_id confirmed path-sensitive
(content+path+params)" holds only for this lane's `inspect-pe-resources`
family. It is not a universal rule (fleet `MANIFEST.json:2782`; `LOG.md` kaika entry).

## Imported scorecard — historical, not current

The following unmeasured table and planned/retired statements describe imported
training history; the current rubric, plan and retirement decisions are above.

Owned axes: depth, coverage, calibration. Scores remain unassigned without a
quality rubric; a row count is a measurement, not a score or verdict.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | r52: `python3 .shokunin/revenger/corpus/live/runs/round-52/reviewer-verify.py` exit0 -> Unicode named group A😀B!→icon ID1 candidate0/lang1033/size48, two leaves; Evidence `ev_b9b5ec033d76da151ad5ce0c052e821130fe4aec6613fc6c2fbdcc48dec03c66`, non-author `corpus/live/runs/round-52/reviewer.md`; r47: `python3 .shokunin/revenger/corpus/live/runs/round-47/reviewer-verify.py` exit0 -> same-ID two-language candidates [0,1], matching-language index1, 3/3 leaves; Evidence `ev_8ed889836291b900a28c7e3816167392cc5042301e069cb2a647b6a98e8d4421`, non-author `corpus/live/runs/round-47/reviewer.md`; r42: `python3 .shokunin/revenger/corpus/live/runs/round-42/reviewer-verify.py` exit 0 -> 2/2 ordered group references, 3/3 leaves, independent bytes; Evidence `ev_6e055332b6fc4cb1a047db769eb5896c73aff9d1ce1bad18105e6559b152dc3d`, non-author `corpus/live/runs/round-42/reviewer.md`; r36: `corpus/live/runs/round-36/inspection.raw.json` Evidence `ev_71a46cb021e0f657859b13c2e95e4bb39508ec441851dcc0b91bea490d0b5922` -> 2/2 independently byte-decoded PE resource rows, one group-to-icon relation with 3/3 candidate/language/size checks, zero false/missed links; non-author `corpus/live/runs/round-36/reviewer.md`; r27: `corpus/live/runs/round-27/inspection.json` Evidence `ev_a524338e43a8a20a3fb0f018d46ef2fe06732e323bfb3ce98fd813bd223f50ef` -> 1/1 RT_RCDATA name 1 language 1033 maps to authored payload; `python3 .shokunin/revenger/corpus/verify_pe_resources.py --self-test` -> 1 positive + 1 rejected mutation; non-author `corpus/live/runs/round-27/reviewer.md`; r22: `corpus/live/runs/round-22/inspection.json` Evidence `ev_24fe0001...` -> 2/2 authored EVM selector/destination pairs, no extra reported candidate; non-author `corpus/live/runs/round-22/reviewer.md`; r18: `corpus/live/runs/round-18/trace.json` Evidence `ev_03c9f793...` -> 1 exact argument seed/2 nodes/1 source-backed alias relation, partial coverage; non-author `corpus/live/runs/round-18/reviewer.md`; r14: `corpus/live/runs/round-14/trace.json` Evidence `ev_53329396...` -> 1 exact seed/4 nodes/3 source-backed capture relations, partial coverage; non-author `corpus/live/runs/round-14/reviewer.md`; r12: exact `index.js:default` static shape comparison `ev_bb7e1c...` identified 2/2 presence deltas and 2/2 stable names in inventories, `corpus/live/runs/round-12/reviewer.md`; r9: exact-seed trace `corpus/live/runs/round-9/trace-exact.json` -> 1 seed, 5 nodes/6 edges, 2/2 named imports; non-author `corpus/live/runs/round-9/reviewer.md`; r3: `corpus/live/runs/20261012T164357Z/LEDGER.md` verifies three static relationships, command -> `True`; Evidence `ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e`; commit in r3 report | r52 Unicode named icon-group relation |
| coverage | unmeasured | r55: `python3 -c "import json,pathlib; p=pathlib.Path('.shokunin/revenger/corpus/live/runs/round-55/inspection.raw.json'); n=json.loads(p.read_text())['normalized_result']; print(len(n['resources']),len(n['icon_groups'][0]['images']))"` -> 3 2; Evidence `ev_db785aec4caaa20630a96a8a3b250ff3aae9c0fa454ff36abe4415725fa22e79`, independent `corpus/live/runs/round-55/byte-oracle.md` + `result-review.md`; r51: `python3 .shokunin/revenger/corpus/live/runs/round-51/reviewer-verify.py` exit0 -> PE32+ supplementary-plane Unicode name A😀B! and numeric ID3, 2/2 leaves independently decoded; Evidence `ev_fac73cc2e5da6d7580e6e2aead6dac8248e826b9dbb78fefd3105294d3d02d8b`, non-author `corpus/live/runs/round-51/reviewer.md`; r41: `python3 .shokunin/revenger/corpus/live/runs/round-41/reviewer-verify.py` exit 0 -> PE32+ AMD64, 2/2 leaves, 1/1 icon relation vs raw bytes; Evidence `ev_ed0685e5757066b3e76effd01579ff0dcacbbb3a430a39e2f8c3d4d987162973`, non-author `corpus/live/runs/round-41/reviewer.md`; r35: `python3 .shokunin/revenger/corpus/live/runs/round-35/reviewer-verify.py` exit 0 -> saved `ev_10659f4a57562678720db1effbc9cc9f9c0bd30e0944194d4429a15f0793191a` 3/3 precision/recall for same-name two-language resource and independent numeric entry; reviewer `corpus/live/runs/round-35/reviewer.md`; work commit recorded in r35 report; r34: `corpus/live/runs/round-34/inspection.json` Evidence `ev_93770df76abe2cec23c8c0708cda054d3ad2a3fb6bb495d267703d0afd136bd3` -> supplementary-plane PE name + numeric resource, independent source-byte precision 2/2 recall 2/2 zero extras; `python3 .shokunin/revenger/corpus/live/runs/round-34/verify_review.py` exit 0, non-author reviewer at `corpus/live/runs/round-34/reviewer.md`; r33: `corpus/live/runs/round-33/inspection.json` Evidence `ev_50a1273217e51aa8f8f1c204f759582b840dfb8a455e8758ca2f1ba413db90bc` -> 2/2 independently decoded non-ASCII/numeric PE resources, precision 2/2 recall 2/2, no extras; `corpus/live/runs/round-33/reviewer.md` reproducer rerun exit 0 (work commit recorded in r33 report); r32: `corpus/live/runs/round-32/inspection.json` Evidence `ev_dcc2411a94ff88169c18f1db3d70ad0792bbccb059dec89bec0df3a578ef653d` -> 2/2 independently byte-decoded named/numeric PE resources, precision 2/2 recall 2/2; `corpus/live/runs/round-32/reviewer.md` reproducer exit 0; r31: `corpus/live/runs/round-31/inspection.json` Evidence `ev_dd2627a0bc00b597eeecd066ada29a6b20e86d8d2dc19b7bf2aa517465595a24` -> 2/2 independently decoded PE resource tuples, 2/2 precision/recall, no extra; `corpus/live/runs/round-31/reviewer.md` non-author byte oracle; r27: first saved `inspect_pe_resources` route, distinct from EVM/ZIP/ELF/JS; verifier absent at `f27b5f1a92af4f05081e7992925e30d621fff1c0`; r21: `corpus/live/runs/round-21/inspection.json` Evidence `ev_4810eda7...` -> raw carrier/decoded SHA parity and 1/1 expected candidate, independent `corpus/live/runs/round-21/reviewer.md`; r19: `corpus/live/runs/round-19/inspection.json` Evidence `ev_0ad0097e...` -> 1/1 authored EVM selector candidate, both carrier/decoded digests checked by `corpus/live/runs/round-19/reviewer.md`; r17: JS recovery refused without Wakaru (`corpus/live/runs/round-17/recovery.json`), no Evidence/output and no gain, independently reviewed; r15: duplicate-name ZIP inspection refused (`corpus/live/runs/round-15/inspection.json`); 3/3 REA occurrences unmeasured, non-author `corpus/live/runs/round-15/reviewer.md`, no gain; r11: outer extraction 2/2 + separate inner inventory 2/2, `corpus/live/runs/round-11/reviewer.md`, outer `ev_fdd504ec...`, inner `ev_e622426d...`; r10: REA extraction `ev_cdab230843b4c92582316077f5092a2f4ea4813b34a55c25463250ee7fdd2671` materialized 2/2 fixture members, independently hashed in `corpus/live/runs/round-10/reviewer.md`; r2: archive identity precision/recall 3/3; `corpus/live/runs/20261012T164246Z/LEDGER.md` independent Python comparison -> `True True`; r1 behavioral recall 0/6, precision N/A; `python3 -c "import json; d=json.load(open('.shokunin/revenger/corpus/live/runs/20261012T163909Z/artifact-inspection.json')); print(d['operation'],d['evidence_id'])"` -> `inspect_artifact ev_dd509246...`; native `provider_unavailable`; commit recorded in r1 report | r51 PE32+ supplementary Unicode name |
| calibration | unmeasured | r58: `python3 .shokunin/revenger/corpus/verify_named_multi_icon_states.py` exit0 → 3/3 full byte-derived normalized records, 2/2 exact one-byte deltas, 2/2 forged claims rejected; independent `corpus/live/runs/round-58/reviewer.md` additionally rejects forged name/entry location; Evidence r55–r57 in LOG; work commit recorded in r58 report; r57: `python3 -c "import json,pathlib; n=json.loads(pathlib.Path('.shokunin/revenger/corpus/live/runs/round-57/inspection.raw.json').read_text())['normalized_result']; print(len(n['resources']),[(i['candidate_resource_indices'],i['size_matches']) for i in n['icon_groups'][0]['images']])"` → 3 [([0], True), ([1], False)]; Evidence `ev_068eb9b682385b760251b6d23ba70680ec57b0e55b95ce242921a3f021e1cd07`, 8 non-author reports `corpus/live/runs/round-57/`; work commit recorded in r57 report; r56: `python3 -c "import json,pathlib; p=pathlib.Path('.shokunin/revenger/corpus/live/runs/round-56/inspection.raw.json'); n=json.loads(p.read_text())['normalized_result']; print(len(n['resources']),len(n['icon_groups'][0]['images']))"` → 3 2; one-byte missing-second control under named Unicode group, Evidence `ev_44be7fd71ca9e8028e71b2714bea44597bd8b25ee83922003747e03fd231342a`, 8 non-author reviews `corpus/live/runs/round-56/`; work commit recorded in r56 report; r54: named Unicode icon group 47-byte declared versus 48-byte payload, candidate[0]/same-language0 retained and size flag false, 2/2 leaves and 1/1 link independently byte-reviewed `corpus/live/runs/round-54/{byte-oracle,result-review}.md`, Evidence `ev_f015502b774219fa3491150c7c2ac1c592c0c099227642d43b4962e555920d24`; r53: `python3 -B .shokunin/revenger/corpus/live/runs/round-53/reviewer-verify.py` exit0 -> Unicode named group unchanged, icon ID2 missing without false link, one-byte control; Evidence `ev_a95668fb8f673de9356fb95e0327f1da81593f468496f44a9803a5cc35d23347`, non-author `corpus/live/runs/round-53/reviewer.md`; r50: `python3 .shokunin/revenger/corpus/verify_icon_languages.py` exit0 -> group language selection 1/none/0 across three byte-derived states, two exact deltas, one forged field rejected; Evidence r47–r49, non-author `corpus/live/runs/round-50/reviewer.md`; r49: `python3 .shokunin/revenger/corpus/live/runs/round-49/reviewer-verify.py` exit0 -> two candidates [0,1] and first-language selection index0, exact byte delta; Evidence `ev_01789c2e316115394bcd7e13f90471766eeac4f108e9ff939390995f952a2ec0`, non-author `corpus/live/runs/round-49/reviewer.md`; r48: `python3 .shokunin/revenger/corpus/live/runs/round-48/reviewer-verify.py` exit0 -> two icon candidates [0,1], group-language no match, null same/size; Evidence `ev_6fbaf25df632a32d7264905eeb0e2ecc64adcdd23e5ddf08e377145e68150f4b`, non-author `corpus/live/runs/round-48/reviewer.md`; r46: `python3 .shokunin/revenger/corpus/verify_multi_icon_states.py` exit 0 -> four byte-derived two-image states, three one-byte deltas, forged second match rejected; Evidence r42–r45, non-author `corpus/live/runs/round-46/reviewer.md`; r45: `python3 .shokunin/revenger/corpus/live/runs/round-45/reviewer-verify.py` exit 0 -> second icon cross-language candidate [1] with null resolved/size, first link intact; Evidence `ev_4949e51a450f63160d8e81c8b3bde0957479419a5594bc30a91571579cc1f3c4`, non-author `corpus/live/runs/round-45/reviewer.md`; r44: `python3 .shokunin/revenger/corpus/live/runs/round-44/reviewer-verify.py` exit 0 -> selective second-image size mismatch, both candidates preserved, one-byte delta; Evidence `ev_7915751e9f33b07a866efadfa65263e967a3d00f186e094ed1532c6d34007dd2`, non-author `corpus/live/runs/round-44/reviewer.md`; r43: `python3 .shokunin/revenger/corpus/live/runs/round-43/reviewer-verify.py` exit 0 -> multi-image first link valid/second missing, exact one-byte control; Evidence `ev_c9f9127a4617806bc1d133354dc7a70de0089d6c67ec4b895ae4903fbfbff60f`, non-author `corpus/live/runs/round-43/reviewer.md`; r40: `python3 .shokunin/revenger/corpus/verify_icon_states.py` exit 0 -> four byte-derived states, three exact deltas, one rejected forged candidate; Evidence r36–r39, non-author `corpus/live/runs/round-40/reviewer.md`; r39: `python3 .shokunin/revenger/corpus/live/runs/round-39/reviewer-verify.py` exit 0 -> cross-language candidate [0], null same-language and size match; Evidence `ev_f7ce61a5f70a94527373f4385ca8f0172e90daaa27367a48b8d4e3d4632b1910`, non-author `corpus/live/runs/round-39/reviewer.md`; r38: `python3 .shokunin/revenger/corpus/live/runs/round-38/reviewer-verify.py` exit 0 -> one candidate [0], same-language 0, false size match on declared 47 vs actual 48 bytes; Evidence `ev_e1d4ee6634880000941c45f3b0c86afc649d8b8bcdd57b01e0c98e141275374c`, non-author `corpus/live/runs/round-38/reviewer.md`; r37: `python3 .shokunin/revenger/corpus/live/runs/round-37/reviewer-verify.py` exit 0 -> controlled missing icon ID 2, 0 false candidate/same-language/size matches, 2/2 leaf identities; Evidence `ev_f4a84eba2ceb19f9af6de5c061c6b147e1023136fdf21960851219e23e90ba50`; non-author `corpus/live/runs/round-37/reviewer.md`; r30: `corpus/live/runs/round-30/inspection.json` Evidence `ev_178f0cb2ef7b5e4f61e73e19f71cba354c44a337b998da07ee559cb93ede53df` vs r29 `ev_503af514d0af04c0d221c70948be240424911b1c27ef42e82a3c4a07c2c1bfcb` -> sole byte offset 552 name ID 1→2; 10/11 checks independently verified, producer exit receipt unverified by saved JSON; `corpus/live/runs/round-30/reviewer.md`; r29: controlled one-byte PE language ID 1033→1036, `ev_bb5fb8cc...`→`ev_503af514...`, eleven local checks and independent `corpus/live/runs/round-29/reviewer.md` confirm unchanged payload mapping; r28: controlled one-byte PE payload change, distinct `ev_a524338e...`→`ev_bb5fb8cc...`, ten local checks, independent `corpus/live/runs/round-28/reviewer.md` confirms changed hash and fixed resource mapping; r26: r25→r26 one-byte valid-target control, both empty Evidence, `corpus/live/runs/round-26/reviewer.md`, narrow calibration; r25: entry-STOP fixture confounded by stale jump operand, `corpus/live/runs/round-25/reviewer.md`, no gain; r24: `corpus/live/runs/round-24/inspection.json` Evidence `ev_50d5ffb1...` -> 0 false reported candidates for one PUSH32 immediate decoy; independent `corpus/live/runs/round-24/reviewer.md`; r23: `corpus/live/runs/round-23/inspection.json` Evidence `ev_296e7ed7...` -> 0 false selector promotions on one bare PUSH4 control; independent `corpus/live/runs/round-23/reviewer.md`; r20: `python3 .shokunin/revenger/corpus/verify_evm_evidence.py --self-test` -> 1/1 selector plus two digests/operand-destination checked, one rejected offset mutation; independent `corpus/live/runs/round-20/reviewer.md`; r16: `python3 .shokunin/revenger/corpus/verify_semantic_trace.py --self-test` -> 3/3 returned captures source/parent-consistent plus one rejected forged location; independent `corpus/live/runs/round-16/reviewer.md`; r13: `python3 .shokunin/revenger/corpus/verify_shape_evidence.py --self-test` -> 2/2 source-matched saved presence deltas, 2/2 stable names, one rejected mutation, `corpus/live/runs/round-13/LEDGER.md` and independent review; r8: `python3 .shokunin/revenger/corpus/verify_js_graph_delta.py --self-test` -> 1/1 saved-parent import delta + rejected mutation; non-author `corpus/live/runs/round-8/reviewer.md`; r7 comparison tool remains 0/1; r6: `corpus/live/runs/round-6/LEDGER.md` comparison -> five `True`, non-author `corpus/live/runs/round-6/reviewer.md` confirms 1/1 parent projection, IDs `ev_4a93276c...` → `ev_f315c466...`; r5: independent `corpus/live/runs/round-5-review.md` rebuilt ELF and ZIP byte-identically; `python3 .shokunin/revenger/corpus/verify_saved_evidence.py --self-test` -> 2 positives + 2 rejection controls; r4: `python3 .shokunin/revenger/corpus/verify_saved_evidence.py --self-test` -> 2 positive + 2 negative rejection, `corpus/live/runs/round-4-verification.md`; r1: independent `truth-score.md` defines six truth atoms; `python3 -c "from pathlib import Path; p=Path('.shokunin/revenger/corpus/live/runs/round-1/wave/truth-score.md'); print(sum(x.startswith('| T') for x in p.read_text().splitlines()))"` -> 6; artifact-only precision separated from behavioral precision N/A; commit recorded in r1 report | r54 named-group size mismatch control |

planned: r60 (devin) named resource-type key `REVTEST` fixture verified non-author — coverage improved; evidence_id confirmed path-sensitive (content+path+params); r36 static icon-group relation independently reviewed; r35 same-name two-language static resource independently reviewed; r34 valid surrogate-pair PE name independently reviewed; r33 non-ASCII PE name identity independently reviewed; r32 named-resource PE identity independently reviewed; r31 two-resource PE identity independently reviewed; r30 PE name-ID control independently reviewed; r29 PE language-ID control independently reviewed; r28 PE one-byte payload control independently reviewed; r27 PE resource route reviewed; paused by operator after r26 (that pause line remains in LOG; this dispatch superseded it for round 27 only); r25 entry-STOP control rejected as confounded; r24 immediate-decoy negative reviewed; r23 bare-PUSH4 negative control reviewed; r22 two-branch EVM fixture reviewed; r21 raw carrier route reviewed; r20 EVM saved-proof reviewed; r19 EVM fixture route reviewed; r18 bounded alias trace reviewed; source recovery halted after r17 Wakaru requirement; r16 semantic saved-proof reviewed; duplicate-name occurrence coverage halted after r15 path collision; r14 bounded semantic capture trace reviewed; r13 saved-shape verifier independently reviewed (`corpus/live/runs/round-13/reviewer.md`); native session blocked until caller-supplied provider. Next claim must specify a distinct route and truth oracle.
retired: none.

## Capabilities

| Capability | What it can now do | Evidence pointer | First-working round |
|---|---|---|---|
| sources-curation | Keep a contract-v1 `corpus/SOURCES.md` registry of opened sources (scoped tiers, append-only rows, study paths, a search log, kept rejects) whose seven census commands all run clean | `corpus/SOURCES.md` at `35b2e8b`; census: 15 rows, malformed 0, `A=14 C=1`, `mined=12 queued=1 rejected=2`, duplicate/enum/missing-path checks print nothing (fleet `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` §Census) | fleet round-1 (kaika continuation) |

Rows enter only through a round that demonstrates the capability running (`AXES.md` §Capabilities).

## Saturation

Saturation line **7.0** on every owned axis/criterion; stagnation window **N = 3** rounds (declared fleet round-1 kaika continuation; proposal `.ufo/waves/kaika-r1/planner.md` §Saturation). The nudge does not apply now: coverage criteria sit at 5.0 and 2.9, and a capability entered this round.

## Planned

Next round (declared fleet round-1 kaika continuation):

1. **coverage — record families (F)**: author an inert known-truth firmware fixture and run REA `inspect_firmware_regions` on it (host binwalk 3.1.0 and unblob 26.6.4 match REA's stated 3.1.x/26.6.x). F goes 4/8 → 5/8 only if the saved record carries `evidence_id` and `normalized_result` and agrees with the byte oracle.
2. **calibration**: add an in-script forged-receipt-command rejection to `verify_icon_languages.py` and `verify_multi_icon_states.py`, so the surviving mutant `b` (`.ufo/waves/kaika-r1/mutation-post.md`) is killed by the script's own run.
3. **coverage — knowledge map (K)**, alternative to 1: re-gate `seed.md` and the readiness checklist against `QUALITY.md` Q01–Q11, or admit a sourced entry on C04/C09 (uncovered).

## Retired

- none retired; record with justification when an axis is retired.

## Round 61 (hyaku) — axes, current

Supersedes the `Planned` list above for the items it consumes (planned item 2,
and item 3's C04/C09 alternative). Pre-registration `reports/round-61/claims.md`
at `e0a4b0c4348ef1fade46539f520e94fa140c4d8a`, amendments A1/A2 before any
after-run. Measured from isolated `git archive <commit> corpus` snapshots with
`python3 -B reports/round-61/measure.py TREE`: before `cf02419`
(`reports/round-61/measure-before.log`), after the work landing
`0b6ddf07f33184baf901dd807ddc72a95f4010c1` (`reports/round-61/measure-after.log`).

| axis / criterion | before → after | counting command | measured commits | verdict (pending non-author verification) |
|---|---|---|---|---|
| coverage — knowledge-map ground (K) | 2.9 → **4.3** (`K_HELD_BACKED` 4/14 → 6/14; C04 and C09 uncovered → held, each backed by an admitted entry) | probe `K_HELD_BACKED` (regex as `:133` plus entry-file existence) | `cf02419` → `0b6ddf0` | improved |
| calibration — receipt-identity mutation kill (new, split this round) | 0.0 → **10.0** (`C2_RECEIPT_B_KILLED_ATTRIBUTED` 0/2 → 2/2) | probe C2 lines | `cf02419` → `0b6ddf0` | improved (narrow regression guard) |
| calibration — selected saved-ledger runnability (C) | 10.0 → 10.0 (`HOLD_CALIBRATION` 4/4, `HOLD_REPLAY` 10/10 both) | C (`:32-43`), via the probe | same | unchanged (hold) |
| coverage — selected-family record presence (F) | 5.0 → 5.0 (`COVERAGE 4/8` both) | F (`:45-57`) | same | unchanged |
| freshness — stored assertions re-verified | 10.0 → 10.0 (18/18 rows still present) | `:134` grep | same | unchanged |
| depth, operability, adjacency | — | — | — | unchanged (no claim; cross-lane ground reported in each entry, not absorbed) |

Split reason (AXES.md §Working the axes): the runnability criterion C counts
exit 0 only and was already at 10.0, so it cannot see whether a verifier's own
run would notice a deleted identity check. The new criterion counts exactly the
two kaika survivors (`.ufo/waves/kaika-r1/mutation-post.md:15,21`); its 10.0 is
a regression guard on two scripts, not a general calibration level. The other
four receipt conjuncts in both scripts (8 survivors,
`.ufo/waves/round-61/build/MutationReceiptConjuncts.md`) and the receipt clauses
in `verify_named_multi_icon_states.py` and `verify_icon_states.py` stay outside
the claim. Holds: saved records and fixtures byte-identical
(`git diff --stat cf02419 0b6ddf0 -- corpus/live corpus/fixtures` empty).

Re-measured by the session-3 replacement L1 on
`0597e5336fd67654c974fcb05f73353f44d868b9` (C09 entry and lesson M25
corrected): values identical (`reports/round-61/measure-after.log`, appended
section). C1's pre-registered "survives the wave-2 attacks" conjunct is unmet:
the falsify wave's 65 seats died with the host session before reporting
(`.ufo/waves/round-61/falsify/dead-seats.json`); the K row's verdict rests on
the non-author closure.

Capabilities: none added (C2 strengthens existing verifiers; the entries are
knowledge, not a new capability).

**planned:** next round, pick from (1) coverage F: an authored firmware fixture
through REA `inspect_firmware_regions` (unchanged from `:179`); (2) calibration:
in-script controls for the remaining receipt conjuncts and for the
`verify_named_multi_icon_states.py`/`verify_icon_states.py` receipt clauses
(Q13); (3) coverage K: re-gate `seed.md` and the readiness checklist against
Q01–Q13, or an authored discriminator for C04's `main` vs fallback (non-index
`main`) through a fresh producer run.

## Round 61 final adjudication — supersedes provisional K row

Fresh validated 66-seat wave over `ab580698`:
`.ufo/waves/round-61/falsify-w3/`. C04 and C09 both failed Q11 as written;
the admission decisions and original pass tables are superseded by
`corpus/lessons/round-61.md` `## Gate — fresh-wave rejection erratum`.
The candidates are retained, clearly marked rejected, with no repaired or
weakened acceptance conditions. README C04/C09 return to `uncovered`.

| axis / criterion | before → final | counting command | verdict |
|---|---|---|---|
| coverage — K | 4/14 → 4/14 (2.9 → 2.9); provisional 6/14 withdrawn | `python3 -B reports/round-61/measure.py TREE` (`K_HELD_BACKED`, after both rollbacks) | C1 falsified: neither candidate survives the fresh attacks |
| calibration — receipt-identity mutation kill | 0/2 → 2/2 (0.0 → 10.0) | same probe, `C2_RECEIPT_B_KILLED_ATTRIBUTED` | C2 improved independently |
| calibration runnability, F, freshness | holds unchanged | probe holds; F and freshness commands above, independently repeated by `W3HoldFandFreshness.md` | unchanged |

The earlier K score was provisional status text, not proof of admission.
The probe checks existence only; the quality gate is the separate necessary
condition that rejected these candidates. Final command output and measured
revision are appended to `reports/round-61/measure-after.log`.

Final measured revision: `7a66d224ef671c086c6e48fa0fc27dff4381281f`.
Probe exit 0, `K_HELD_BACKED=4/14`,
`C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2`, `HOLDS_OK=yes`; census exit 0,
saved-input diff empty (`reports/round-61/measure-after.log:96-136`).
