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

## Round 62 — final measured coverage admission

One claim C1, coverage K (lowest criterion), frozen at
`a3498e25ad87bf756288812d0ea7c474b09433c7`; base
`5bd4a90fc1a34caa94496601b60537b3aab12301`. Target at least5/14,
4/14 falsifies. README stayed uncovered throughout drafting, fresh attacks
and correction reviews; held flips landed only at
`0651c7c683b4af3801b5ba63bc57ce99a46a7de0`.

| axis / criterion | before → after | counting command / independent condition | measured revisions | verdict |
|---|---|---|---|---|
| coverage — knowledge-map ground K | **4/14 → 6/14**, **2.9 → 4.3** | unchanged `python3 -B reports/round-61/measure.py TREE`, `K_HELD=K_HELD_BACKED`; separately, named fresh-seat Q01–Q13 admission decisions in `corpus/lessons/round-62.md` | base `5bd4a90f` → final measured `b0400f02c2790c5a6cdb8d51c8e8a276b895b926` | **improved**, C1 met |
| calibration — receipt-identity guard | 2/2 → 2/2 (10.0 → 10.0) | same probe, attributed command-mutant kills checked separately from HOLDS_OK | same | unchanged hold, not a new claim |
| calibration — selected runnability | calibration4/4, replay10/10 both ends | same probe, controls2/2, d2kills2/2, HOLDS_OK=yes, exit0 | same | unchanged hold |
| coverage — selected-family presence F | 4/8 → 4/8 (5.0 → 5.0) | existing F command; primary saved-input tree unchanged | same | unchanged |
| freshness — stored-assertion proxy | 18/18 → 18/18 (10.0 → 10.0) | existing grep, seed12 + readiness6; both files byte-identical | same | unchanged; no new current-host readiness claim |
| depth / operability / adjacency | no separate numeric claim | new manual derivations and bounded scope; PROVINCE/ADJ-06 unchanged | same | no harm demonstrated |

Final evidence: `reports/round-62/measure-after.log` and
`reports/round-62/final-verification.json`: two entry readouts exit0 and
match their embedded Provenance byte-for-byte (JS25 lines, EVM8 lines);
only C04/C09 change status among14 rows; all8 held knowledge paths resolve;
all611 preserved-input/old-evidence manifest files match; all64 original
fresh-report prefixes preserved; unchanged ten-verifier set and Q01–Q13;
source census exit0 (three disclosed W04s), rows27→31.

The K probe still measures existence/status only; it is not an admission
gate. New admitted files are `round-62-commonjs-require-name-evidence.md`
and `round-62-evm-dispatch-byte-evidence.md`. Original rejected candidates,
intermediate rejected revisions and counterexamples remain, uncredited.
The two within-round correction stages are not new claims or replacement
seats. M27/M28 record missing derivation and byte/hex-unit mistakes.

Capabilities: none added. No gate-registry conformity, new producer route,
runtime capability or promotion is claimed. Q01–Q13 were not weakened and
no Q14/lexical helper was adopted.

Planned future selection: coverage F on an authored local frontier artifact,
or the remaining receipt-clause calibration debt; keep SKILL/registry,
F03-versus-STALE and operator ADJ-06 debt explicit. This is a plan, not a
dispatch or claim for another round.

## Round 63 (hyaku) — final measured three-claim round

Pre-registration `reports/round-63/claims.md` at `54ab973c021cc62ca65dcbe2cbfabe3235d5ee38`;
do-nothing control red-before `reports/round-63/measure-before.log` (base
`55bcb6e1aeb4d42923a4e98db6580f67142b41ac`). Final measured revision
`f6ea293255d9263be24a8f100e8a5ad7490f26fa` (`reports/round-63/measure-after.log`,
committed with this section — round-62 routed defect (a) honored).

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| coverage — knowledge-map ground K | **6/14 → 7/14 (4.3 → 5.0)** | `python3 -B reports/round-63/measure.py TREE` (`K_HELD_BACKED`) | `55bcb6e` → `f6ea2932` | **improved, C1 met** |
| coverage — selected-family record presence F | **4/8 → 5/8 (5.0 → 6.2)** | same probe (`F_COVERAGE`) | same | **improved, C2 met** |
| calibration — receipt-clause attribution guard (new criterion C3) | **0/2 → 2/2 (0.0 → 10.0)** | same probe (`C3_RECEIPT_KILLED_ATTRIBUTED`) | same | **improved, C3 met** |
| calibration — receipt-identity mutation kill (C2) | 2/2 → 2/2 | same probe | same | unchanged hold |
| calibration — selected runnability | 4/4, replay 10/10 | same probe | same | unchanged hold |
| freshness — stored-assertion proxy | 18/18 → 18/18 | same probe (`FRESH_ROWS`) | same | unchanged hold |
| depth / operability / adjacency | — | — | — | unchanged (no claim; connector scan reported-not-absorbed) |

Claim separation verified by named seat `W2ReviewSeparability` (build) and
`W2VerifySeparabilityFinal` (falsify): three single-claim trees move only their
own counters. C1 admission condition: named fresh-seat Q decisions —
`W2AttackEntryQ01` PASS (exact-hash, re-review and transition confirm),
`W2AttackEntryQ11` PASS (same), `W2AttackEntryScope` CLEAN/Q10,
`W2AttackEntryIndependence` HOLDS/Q03, adversary `W2ClaimsAdmission`
NOT-FALSIFIED, discernment `W2SpotcheckDiscern` ADMIT-AGREE + REJECT-AGREE.
New admitted file: `corpus/knowledge/round-63-zip-central-directory-evidence.md`
(sha256 `b2660e60…e0086`); C06 flipped `partial → held` naming only it.

C2: authored inert fixture `corpus/fixtures/firmware-r63/` (generator
reproduces the image byte-exact), one real
`npx -y rea-agents@6.5.0 inspect-firmware-regions` run saved at
`corpus/live/runs/round-63/` (Evidence `ev_aae7529f…`, receipt, oracle
`ORACLE OK` — regions 512/79 and 1024/90 with decompressed digests; seat
`W2VerifyC2Record` recomputed the Evidence ID from the shipped 6.5.0 package).
C3: `receipt_ok` refactor + one in-script forged-receipt control per script;
frozen mutants killed attributed (`r55:`/`r36: forged receipt accepted`);
build `R63MutC3` mutant bytes byte-identical to the frozen counter's own
`mutate_c3()` output; falsify `W2MutC3Final`/`W2VerifyC3Patches` reproduced.

Capabilities: none added (C2/C3 strengthen existing verifier/registry ground;
no new gate capability or promotion claimed). Sources: rows 31 → 35
(S032 APPNOTE, S033 own-work archive bytes/record, S034 scoped APPNOTE re-open
for §4.3.7 local-header layout, S035 own-work ledger); census exit 0 at both
ends; the S034 same-URL W04 is the disclosed scoped re-open. Mistakes mined:
M33 (stale fixture premise — uImage detectability assumed, not probed;
red-before is the L1 pre-probe), M34 (counter-substitution — the counter is
presence-only, the claim text is the gate; runnable falsifier
`W2AttackProbeK`), M35 (residual unguarded `stdout_sha256` conjuncts in BOTH
receipt scripts — routed, not claimed).

Residual/routed (full table `.ufo/waves/round-63/falsify/routed-debt.md` when
landed + report): frozen-counter semantics (K backed-regex prefix false
positive, F presence-only, C3 attribution-string weakness, HOLDS_OK drift D1 —
probe frozen, fixes route to a later registered counter); round-58/59 PASS-count
quotes (139) no longer reproduce after the C3 patch (142) — historical records
left unedited under void conditions, disclosed; C07 frontier-token legend
staleness (C2 record exists, no admitted knowledge — left per void conditions);
freshness hold proves byte survival, not current-host truth; oracle scope
(content+correspondence, not provenance — Q09 disclaimers carried).

Planned future selection: coverage K on C02/C06 re-gates or a managed-assembly
probe if a local SDK appears; calibration on the remaining receipt conjuncts
(M35) or a newly registered counter with the routed regex/attribution fixes.

## Round 64 (hyaku) — final measured two-claim round

Pre-registration `reports/round-64/claims.md` at `3bb430f9` (V2 diagnostic
wording amended at `671e3a18` before any after-measurement, recorded in the
lesson); do-nothing control `reports/round-64/measure-before.log` (base
`666ea84b`: K 7/14, STRICT 7/14, MISMATCH 1 [C07], C4 0/2, holds green). One
validated v2 wave, exactly 64 seats, dispatched as ONE task call (`.ufo/waves/
round-64/`); §3 planner seat held by L1. Final measured revision: see
`reports/round-64/measure-after.log` (committed with this section).

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| coverage — knowledge-map ground K | **7/14 → 8/14 (5.0 → 5.7)** | `python3 -B reports/round-64/measure.py TREE` (`K_HELD_BACKED`) on `git archive` trees | `666ea84b` → final tip | **improved, C1 met** |
| calibration — stdout_sha256 receipt guard (C4, new criterion) | **0/2 → 2/2 (0.0 → 10.0)** | same probe (`C4_RECEIPT_KILLED_ATTRIBUTED`, endswith-attributed) | same | **improved, C2 met** |
| calibration — receipt-identity (C2) and receipt-clause (C3) holds | 2/2 → 2/2 both | same probe | same | unchanged hold |
| calibration — selected runnability (C) | 4/4, replay 10/10 | same probe (`HOLD_*`) | same | unchanged hold |
| coverage — selected-family presence F | 5/8 → 5/8 | same probe (`F_COVERAGE`) | same | unchanged |
| freshness — stored-assertion proxy | 18/18 → 18/18 (byte-survival hold; not current-host truth — routed wording frozen) | same probe (`FRESH_ROWS`) | same | unchanged |
| v2 routed-counter diagnostics | K_HELD_BACKED_STRICT 7/14→8/14 (= BACKED both ends); README_TOKEN_LEGEND_MISMATCH **1 → 0** (M36 fix, shown able to fail); HOLDS_OK_V2 no → yes | same probe | same | registered, not scored |
| depth / operability / adjacency | no separate numeric claim | — | — | unchanged (ADJ-06 reported-not-absorbed; connector scan) |

C1 admission (distinct from the counter, per the round-61 M34 lesson): named
fresh-seat Q decisions on landed bytes — Q01+Q02 PASS (`R64ReviewEntryQ01`
re-review), Q03 PASS (`R64ReviewEntryScope` blind derivation), Q06 PASS
(`R64ReviewEntryQ06`), Q09 PASS ×6 criteria (`R64ReviewEntryQ09` re-review),
Q10 PASS (`R64ReviewEntryScope` delta, cross-lane fence), Q11 PASS
(`R64ReviewEntryQ11` re-review), remaining rows answered/n/a per the entry's
Q-map, 24/24 in-entry commands re-run MATCH (`R64EntryCommands`), recheck
mutation kill attributed (`R64MutEntry`). Admitted entry:
`corpus/knowledge/round-64-firmware-region-byte-evidence.md` (sha256
`9bf21e50…e0ebf`); README C07 flipped with the Gate decision in the same
revision. Also discharges the routed C07 legend staleness (frontier → held).

C2: one in-script forged-stdout control per script (6 insertions, 0 deletions;
existing controls retained) — `verify_icon_languages.py` `a2fd347e…`,
`verify_multi_icon_states.py` `9345cb8c…`. Verified by R64MutC4 (frozen mutants
byte-verical), R64ReviewC4Lang/Multi (PASS), R64MutIcon (C2/C3 regression
sweep), R64MutProbe (attribution integrity: loose messages rejected), 
R64SimplifierDrift (minimality). Red-before: both mutants exit 0 at base.

Capabilities: none added (C2 strengthens existing verifiers; the entry is
knowledge). SHONEN box 1: SKILL.md landed (39098 bytes, `bfd92057…`),
non-author verifier `R64ReviewSkill` re-stated `[x]`-ready = YES on the final
bytes — box flips `[x]` with that named verifier. Mistake mined: M36
(token-vs-legend drift; fix = registered `README_TOKEN_LEGEND_MISMATCH`,
shown able to fail with value 1 at base). Sources: rows 35 → 37 (+S036 pinned
REA firmware guide, +S037 own-work bundle), census exit 0 both ends; C1 is the
sourced claim.

Routed forward (full detail in `corpus/lessons/round-64.md`): counter spoof
surface (decoy trees meet numeric targets — the Q-gate is the defense; an
AST-bound mutation counter is future-counter debt); STRICT rejected-marker
scan window (first 2000 bytes — this entry's marker sits at 4155, recorded by
R64ReviewSeparability); entry recheck scope items 10–11 outside the stdout pin
(R64MutEntry); Q01 two LOW line-anchoring nits; `## Frontier` C07 prose staleness;
transplant corollary owner named (R64RevengerLedger 6-prong check).

Planned future selection: coverage K on C02/C05/C08 re-gates or a managed-assembly
probe if a local SDK appears; calibration on the remaining receipt conjuncts
(`evidence_id`/`exit_code` still lack in-script forged controls — named by
R64ReviewSeparability) or the registered AST-bound counter.

## Round 65 (hyaku) — verified calibration guard, coverage candidate pending dispatch

Pre-registration inherited from the dead prior attempt and re-verified before use: `reports/round-65/claims.md` at `5a2e7a0`; base `3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f`; do-nothing control re-run reproduced exactly (`measure-before.log`: K 8/14, C5 0/2, HOLDS_OK_V3=no, exit 0). Candidate commit `c7b7cf98ddeecbd5464e47396f224e6384b78905` (fixture + entry + S038-S041 + C5 patches + lesson + wave spec; README NOT flipped). Round shape: ONE v2 wave of exactly 64 seats prepared and validated (`plan` exit 0, counts 64, dispatch.calls 1) at `.ufo/waves/round-65/wave-spec.json`; dispatch is the orchestrator's between-round act per the accepted host mapping (2026-10-23) — zero seats dispatched in-seat, reported as the mapping, not a defect. §3 planner seat held by the L1.

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| calibration — evidence-id transplant guard (C5, new criterion) | **0/2 → 2/2 (0.0 → 10.0)** | `python3 -B reports/round-65/measure.py TREE` (`C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED`, endswith-attributed) | `3eebcdd7` → `c7b7cf98` | **improved, C2 met** |
| coverage — knowledge-map ground K | 8/14 → 8/14 (5.7 → 5.7); admission pending | same probe (`K_HELD_BACKED`) | `3eebcdd7` → `c7b7cf98` | **pending — candidate landed, flip deferred to dispatched wave** |
| calibration — C2/C3/C4 holds | 2/2 → 2/2 each | same probe | same | unchanged hold |
| calibration — selected runnability (C) | 4/4, replay 10/10 | same probe (`HOLD_*`) | same | unchanged hold |
| coverage — selected-family presence F | 5/8 → 5/8 | same probe (`F_COVERAGE`) | same | unchanged |
| freshness — stored-assertion proxy | 18/18 → 18/18 (byte-survival hold) | same probe (`FRESH_ROWS`) | same | unchanged |
| diagnostics — STRICT rejected-marker scan | `[:2000]` window → whole-file scan + `STRICT_REJECT_WINDOW_SELFTEST=pass` (registered, not scored) | same probe | same | registered repair (M37) |
| depth / operability / adjacency | — | — | — | unchanged (ADJ-06 reported-not-absorbed) |

C2: one in-script forged-evidence control per script (`verify_icon_languages.py` ← transplants the round-42 saved evidence id; `verify_multi_icon_states.py` ← round-47's; both ids verified present in `corpus/live/runs/` saved bytes pre-patch). Frozen mutant (delete the `evidence_id` conjunct, one regex match per script) exits non-zero with last line ending `forged receipt evidence accepted` on both; unmutated self-tests green; patches 3 insertions / 0 deletions each, `receipt_ok` untouched. Seeds routed prong (c) of the round-63/64 Evidence-ID transplant check; prongs (a),(b) and the injectivity registry remain future-round debt (owner named in `corpus/lessons/round-65.md`).

C1 (disposition): candidate entry `corpus/knowledge/round-65-apk-axml-byte-evidence.md` over authored fixture `corpus/fixtures/apk-r65/` (947 bytes sha256 `05d2280f…`, regen byte-identical in scratch) covers README C05 with a manual byte-derived readout (15 facts, stdout sha256 `507d79f8…`, every embedded output byte-matched). Admission requires named fresh-seat Q01–Q13 decisions per the frozen order; the validated 64-seat wave (attack roles 38/64 = 59%) carries those seats plus the C5 attribution/regression/separability attacks and will be dispatched by the orchestrator. L1 dry-run with the flip applied on a scratch copy prints K_HELD=K_HELD_BACKED=STRICT=9/14 (6.4), MISMATCH=0, HOLDS_OK_V3=yes, exit 0 — the after-state is one command away once the wave rules.

Capabilities: none added (C2 strengthens existing verifiers; the entry is a pending candidate, not an admitted capability).

Sources: rows 37 → 41 (+S038 mined, +S039 mined, +S040 queued, +S041 own-work); seven manual census commands and `scripts/sources-census.sh validate` both exit 0 at round end. Mistakes mined: M38 (layout-from-intent; red-before `.ufo/waves/round-65/m38-red-before.log`), M37 (pre-registered STRICT window; fix registered with self-test). Tool installs: none (curl/npm-pack/python3 only; no package installed or updated).

**planned:** next round — adjudicate the dispatched round-65 wave: on all-criteria pass flip C05 `frontier → held` naming only the round-65 entry (same revision as the Gate decision), re-measure on the committed tip, and record C1's verdict; on falsification flip `frontier → uncovered` per the frozen order. Then calibration on the remaining receipt conjuncts (`exit_code`/`fixture_sha256` still lack in-script forged controls) or coverage K on C02/C08 re-gates.

Routed forward: AST-bound mutation counter (owner: future registering round); recheck-pin scope holes H1–H3; SHONEN box 1 `[x]` re-confirmation by a non-lane reviewer (r64 routing 1, unchanged); evidence-id prongs (a)/(b) + injectivity registry; `## Frontier` C05 prose refresh at admission time (with the row flip, same revision).

## Round 66 (hyaku) — frozen-order adjudication: C05 falsified→uncovered, C6 calibration guard verified

Pre-registration `16b9387b` (claims.md + counter `measure.py` sha256 `a59914e9…1da` + red-before on base `8214e4dd`). Claims: C1 coverage — execute the round-65 frozen admission order on the C05 row (either-way flip + candidate disposition), C2 calibration — new criterion C6 (forged `exit_code`/`fixture_sha256` receipt controls, 0/4 → 4/4 attributed). The orchestrator-dispatched 64-seat r65 wave (all 64 reports under `.ufo/waves/round-65/`, committed as evidence this round) falsified the C05 candidate at Q02/Q06/Q11 (one transcription byte-pair at entry:41); every named decision re-verified by this L1 against committed bytes before the flip.

| axis / criterion | before -> after | counting command | measured commits | verdict |
|---|---|---|---|---|
| coverage — C05 adjudicated disposition (frozen order) | `frontier` → `uncovered` (8/14 → 8/14, 5.7 → 5.7 — honest: falsified candidate ground, not held) | `python3 -B reports/round-66/measure.py TREE` (`K_ROW C05`, `C05_REJECTED_MARKED`, `K_HELD_BACKED`) | `8214e4dd` → `a4c712a0` | **falsified C05 candidate, order executed — verdict recorded** |
| calibration — C6 exit_code/fixture_sha256 guards | **0/4 → 4/4 attributed** | same probe (`C6_RECEIPT_KILLED_ATTRIBUTED`, controls/pass 4/4) | `8214e4dd` → `a4c712a0` | **improved, C2 met** |
| calibration — C2/C3/C4/C5 holds | 2/2 each → 2/2 each | same probe | same | unchanged hold |
| calibration — selected runnability (C) | 4/4, replay 10/10 | same probe (`HOLD_*`) | same | unchanged hold |
| coverage — selected-family presence F | 5/8 → 5/8 | same probe (`F_COVERAGE`) | same | unchanged |
| freshness — stored-assertion proxy | 18/18 → 18/18 | same probe (`FRESH_ROWS`) | same | unchanged |
| diagnostics — STRICT scan + legend token | `STRICT_REJECT_WINDOW_SELFTEST=pass`; `README_TOKEN_LEGEND_MISMATCH` 0 → 0 (`uncovered` is a legend row) | same probe | same | unchanged diagnostics |
| depth / operability / adjacency | — | — | — | unchanged (ADJ-06 reported-not-absorbed) |

C1 verdict (frozen `reports/round-65/claims.md:110-123` order, step 3): **FALSIFIED**. Fresh-seat decisions Q02, Q06, Q11 FAIL — item 3's MANIFEST `payload_first16_hex` at `corpus/knowledge/round-65-apk-axml-byte-evidence.md:41` records `4d616e696673742d…` where the entry's own deriving command prints `4d616e69666573742d…` (15-byte `Manifst-Version` vs 16-byte `Manifest-Version`), plus the S039 anchor at line 5 and the ResourceTypes.h:239-250 range; corroborated by R65MutEntry, R65CriticEntryDeps, R65EntryQmapDraft, R65ReviewSourcesTier, and `R65SpotcheckDiscern` = REJECT at current bytes. The candidate is retained rejected (evidence, never cited as held); all repairs are text-level and routed to a next coverage round (lesson §Routed forward item 6).

C2: one in-script forged control per conjunct per script (`verify_icon_languages.py:158-163`, `verify_multi_icon_states.py:157-162`; `receipt_ok` untouched; 6 insertions/0 deletions each). Frozen mutants (delete each conjunct, one regex match) exit non-zero with the attributed marker on both scripts — with this landing, every `receipt_ok` conjunct on both ledgers carries a mutation-covered forgery guard (C3–C6 complete).

Registered dispositions landed in the same revision: S042–S044 rows (+3 → 44 total; S043/S044 correct S039/S040 by new row), stale `candidate` headers on the two admitted entries → `admitted`, SOURCES `## Search log` retro+current notes, SKILL.md round-66 refresh (header source/verified-at, M37–M41 rows, §6 counter/checklists repoint, apk-r65 regen warning, §6.5 gate, §7 pointer rows). Census exit 0 both ends.

Round shape: L1-seat adjudication + build under the accepted host mapping; one v2-band verification spec prepared and validated at `.ufo/waves/round-66/` (64 seats, `ufo-swarm-wave.mjs plan` exit 0 under `scripts/hyaku/ufo-wave-policy-v2.json`) — prepared-but-undispatched; zero in-seat dispatch. §3 planner seat held by the L1. Tool installs: none. No confirmed misroot.

**planned:** next round — the C05 re-gate needs a v2 candidate whose repairs are all text-level (entry:41 hex pair, dex-header spec row + S043 as route-scope source, item-8 provenance, item-9 dex semantics row, Q-map pointers); or calibration/coverage elsewhere on C02/C08; the dispatched r66 verification wave's findings adjudicate this round's work honestly.

Routed forward: verbatim-output-diff gate for embedded entry outputs (M39 fix shape, owner: future registering round); AST-bound mutation counter + label-spoof surface; generator conditional-symlink note; evidence-ID prongs (a)/(b)/(d) + injectivity registry; endswith-attribution asymmetry; recheck-pin H1–H3; SHONEN box 1 `[x]` non-lane re-confirmation (carried); r58/59 PASS-count quotes.

## Round 67 (hyaku) — quarantine-first: both claims honestly falsified, holds green

Pre-registration `d11f81df` (claims.md + frozen counter sha256 `7933c060…` + red-before on base
`fa0eb3eb`); build `7668510f`; ONE v2 wave of 64 seats dispatched in-seat (attempt 1 aborted by
the dispatcher exit — 0 seat work; attempt 2 same taskCall, 64/64 reports, 0 dead); adjudicated
fail branch on both claims; final measured tip = the adjudication commit (measure-after.log).

| axis / criterion | before → after | counting command | verdict |
|---|---|---|---|
| coverage — C05 re-gate (K, lowest criterion) | 8/14 → 8/14 (5.7 → 5.7) — honest: the v2 candidate was rejected (wave Q02 FAIL: START_NAMESPACE anchor :244 vs actual :245, twice) and retained; C05 stays uncovered | `python3 -B reports/round-67/measure.py TREE` (K_HELD_BACKED 8/14, K_ROW C05 uncovered, C05_SINGLE_V2 no) | **C1 falsified — honest stop** (5/6 routed repairs verified good by fresh seats; fix routed) |
| calibration — C7 embedded-output verbatim gate | 0 → present but unattributed: killed 1/1, attributed **0/1** (the forged-control marker is shadowed dead code — seats R67MutC7Kill/R67CriticC7Claim/R67ReviewC7Gate) | same probe (C7_* labels; HOLDS_OK_V5=no is the honest signal) | **C2 falsified — honest stop** (gate's drift detection + red-before real and verified; reorder fix routed) |
| calibration — C2–C6 prior holds | 2/2·2/2·2/2·2/2·4/4 → same | same probe | unchanged hold |
| calibration — selected runnability C + replay | 4/4, 10/10 → same | same probe (HOLD_*) | unchanged hold |
| coverage — selected-family presence F | 5/8 → 5/8 | same probe | unchanged |
| freshness — stored-assertion proxy | 18/18 → 18/18 | same probe | unchanged hold |
| diagnostics | C05_REJECTED_MARKED yes (r65 candidate); MISMATCH 0; STRICT window pass | same probe | unchanged |
| depth / operability / adjacency | no claim | connector CONTEST-NAMED (kaidoku; reported-not-absorbed) | unchanged |

Neither claim is exploratory; no `unprovable-but-better` ruling sought. Capabilities: none added
(the C7 gate registered as a probe in SKILL.md, with its registry row corrected at adjudication).
Sources: 44 → 45 (+S045 mined, dex-format spec, snapshot committed); census exit 0 both ends.
Mistakes: M44 (anchor off-by-one from intent — M40 recurring; builder must derive symbol lines),
M45 (registered attribution claim false — marker shadowed; registry corrected, fix routed).
Quarantine (item 10, wave-4): 26/26 verdicts — 4 PRESENT (register wrong), 19 ABSENT
(fabrication-class confirms), 1 UNREACHABLE, 2 UNVERIFIED-REACHABLE; adoption closed; 0 package
rows/entries appended or copied.

## Round 68 (hyaku, attempt 2) — C1 verified, C2 falsified on five wave criteria

Pre-registration `f505526f7ecf4ac1ad51d99aa2d1dd5c57c0bae0` (claims, frozen counter
`reports/round-68/measure.py` sha256 `0de4eb6f…93f7766`, red-before receipt on base
`f165908aaffcf14798de53405fe788986bd33ff9`); build `4232235723cf8d4731a1e7e78ca098b8af953a57`;
ONE validated v2 wave of exactly 64 seats (attack 46/64 = 71.9 %), dispatched in one call; final
measured tip in `reports/round-68/measure-after.log`.

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| calibration — C7 attribution (C8) | `C7_MUTANT_KILLED_ATTRIBUTED` **0/1 → 1/1**; `HOLDS_OK_V5`/`V6` **no → yes**; negative spoof pair `1/1` / `0/1` at both ends; counter exit 0 | `python3 -B reports/round-68/measure.py TREE` over `git archive <commit> corpus` | `f165908` → final tip | **improved, C1 met** — with the named instrument caveat: two critics show the predicate is satisfiable by a non-detecting gate (`R68CriticC7Claim`, `R68CriticClaimsC1`); behavioural legs on the landed gate were run by `R68MutC7Entry`/`R68MutC7Kill`/`R68MutC7Spoof`, and counter-side behavioural legs are routed |
| coverage — knowledge-map ground K | `K_HELD_BACKED` 8/14 → 8/14; `K_ROW C05` `uncovered` → `uncovered`; `C05_SINGLE_V3` no → no; `HOLDS_C2_V3` no → no | same probe | same | **C2 FALSIFIED — honest stop**: wave decisions Q04, Q05, Q07, Q08 (returned FAIL under Q11), Q11, Q13 FAIL on the landed v3 bytes; kill rule executed (row unchanged, entry `admission-status: rejected`, every other byte kept) |
| coverage — selected-family presence F | 5/8 → 5/8 (`6.2`) | same probe (`F_COVERAGE`) | same | unchanged |
| calibration — C2–C6 receipt guards | 2/2 · 2/2 · 2/2 · 2/2 · 4/4 → same | same probe | same | unchanged hold |
| calibration — selected runnability + replay | 4/4, 10/10 → same | same probe (`HOLD_*`) | same | unchanged hold |
| freshness — stored-assertion proxy | 18/18 → 18/18 | same probe (`FRESH_ROWS`) | same | unchanged hold |
| diagnostics | `README_TOKEN_LEGEND_MISMATCH` 0; STRICT window selftest pass; `C05_REJECTED_MARKED=yes` | same probe | same | unchanged |
| depth / operability / adjacency | no claim | `R68ConnectorOverlap`, `R68SentinelScope` | — | unchanged (ADJ-06 contest named, reported-not-absorbed) |

The v3 candidate passes Q01, Q02, Q03, Q06, Q09, Q10, Q12 and fails Q04/Q05/Q07/Q11/Q13, all on one
root: item 11's claim that the derivation script prints *every* stated S038 line number, while `:237`
and `:244` are stated and never printed, item 5's widths are a Python literal presented as derived,
and item 9's namespace-resolution sentence is ungrounded. The C05 row therefore stays `uncovered`,
`corpus/README.md` is byte-unchanged, and the repair set is routed as one bundle
(`corpus/lessons/round-68.md` §Routed forward item 6).

Capabilities: none added (the gate repair strengthens an existing registered gate; Q14 is an
admission criterion, not a capability). SHONEN box 1 keeps its `[~]`-with-outside-verifier state —
`R68ReviewSkillRefresh` is lane-dispatched and says so. Mistakes mined: **M46** (landing/registry
drift — the SKILL gate row asserted the r67 limitation after the r68 repair; fixed from the
after-run, shown able to fail against `C7_MUTANT_KILLED_ATTRIBUTED=1/1`), **M47** (prose hex/ASCII
length drift at entry:46; fix = new criterion Q14, shown to flag that line and pass the admitted
round-63 line 97). Sources: rows 45 → 46 (S046), `S046 used-by` `—` → the round-68 entry; census
exit 0 both ends, the round-start `W03` gone at round end. Quarantine (item 10): `Assimilation:
none` — frozen-claim round; the re-derived slice is still 26 rows and stays closed. considerthese:
`2026-10-24.md` proposal 1 landed as Q14.

**planned:** the next coverage round re-gates C05 with the routed repair bundle: extend
`derive_axml_anchors.py` (`RES_XML_FIRST_CHUNK_TYPE`, enum block bounds, enum values) and re-embed
item 11 to 19+ lines, label item 5's widths manual, bound item 11's credit, drop "framework", fix
item 9's namespace sentence, add S032/S034 `source:` lines and pin `generator.py` — all in one
commit, then re-gate. Calibration side: give the frozen counter a behavioural (non-marker) C7 leg,
drop `c7_v3_clean` from `HOLDS_OK_V6`, and close the kill rules over every mechanical conjunct.


## Round 69 (hyaku run 6) — both claims honestly falsified; instrument defect reported, not repaired

Pre-registration `e1d22caf` (claims + frozen counter `reports/round-69/measure.py` sha256
`bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377` + red-before
`reports/round-69/measure-before.log` on base `222a7a70`); build `da02261` (C05 v4 candidate + extended
derivation + S047 + QUALITY Q15); ONE validated v2 wave of exactly 64 seats, dispatched in one call
(attack 45/64 = 70.3 % lane predicate, 41/64 = 64.1 % prompt §3 floor list), 64/64 reports, 0 dead seats.

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| coverage — coverage aggregate on the C05 row (`HOLDS_C2_V4`) | `no` → `no`; `K_HELD_BACKED` 8/14 → 8/14; `C05_STATUS` `uncovered` → `uncovered`; `C05_SINGLE_V4` no → no | `python3 -B reports/round-69/measure.py TREE` over `git archive <commit> corpus` | `222a7a7` → adjudicated tip | **C1 FALSIFIED — honest stop** (wave Q FAILs at Q05, Q07, Q11, Q14, Q15 on the landed v4 bytes; kill rule executed: README unflipped, v4 entry `admission-status: rejected`, every other byte kept) |
| calibration — Q15 tree-identity criterion + D1 restatement | criterion row present (`QUALITY.md:27`), checker behaves as specified on every leg run by hand (`--self-test` exit 0; D1 fixture scan exit 1; true restatement scan exit 0), restatement + false-sentence lines committed in `corpus/lessons/round-69.md` | checker: `python3 -B corpus/q15_tree_id_check.py --self-test` / `--scan <file> --lane <lane>`; counter label `Q15_PRESENT` (+ `Q15_SELFTEST`/`Q15_FALSE_KILLED`/`Q15_RESTATE_OK`, all **unevaluable** — see below) | `222a7a7` → adjudicated tip | **C2 FALSIFIED — honest stop, instrument defect.** The frozen counter dies `NameError` at `measure.py:158` on every tree carrying the Q15 checker (`def run` is at `:187`), so no `Q15_*`, `C7_*` or `HOLDS_OK*` label is printable with the pinned sha256; the D1 fixture also sits outside the `corpus`-only archive. Not repaired after scoring (kumitate r42) |
| calibration — C7 gate and C2–C6 receipt guards | gate behaved as specified under four independent reviews; labels unprintable for the reason above | same probe | same | **unchanged hold, unmeasured this round** — the C7 L0 (marker-presence vs behavioural legs) stays open and was not pre-empted |
| calibration — selected runnability + replay | `HOLD_CALIBRATION` 4/4, `HOLD_REPLAY` 10/10 — every `verify_*.py --self-test` exits 0 when run directly (`R69HoldSweep`) | ten verifier self-tests | same | unchanged |
| coverage — selected-family presence F | 5/8 → 5/8 (`6.2`) | same probe (`F_COVERAGE`) | same | unchanged |
| freshness — stored-assertion proxy | 18/18 → 18/18 | same probe (`FRESH_ROWS`) | same | unchanged hold (byte survival only) |
| diagnostics | `README_TOKEN_LEGEND_MISMATCH=0`; STRICT window selftest pass | same probe | same | unchanged |
| depth / operability / adjacency | no claim | `R69ConnectorOverlap` (CONTEST-NAMED, ADJ-06 still open), `R69SentinelScope` (CONTAINED) | — | unchanged (reported, not absorbed) |

**Round void conditions fired, recorded not hidden** (`reports/round-69/claims.md:187-194`): counter exit
non-zero at final; `HOLDS_OK_V6` not yes. The V6 cause is independent of C2: extending
`corpus/derive_axml_anchors.py` in place reformatted seven enum lines the retained round-68 candidate
embeds verbatim, so `C7_V3_CLEAN` went `yes → no` while that candidate's own bytes are unchanged
(`R69HoldSweep`, `R69CriticClaimsC1`). No target was narrowed; no acceptance condition was repaired.

Capabilities: none added. The Q15 criterion + checker are admission-bar and instrument work, not a new
capability (the checker's kill leg is `rc != 0` and a non-demonstrating fixture also satisfies it —
`R69CriticClaimsC2`). SHONEN box 1: **D4 reconciled by append** — committed `SHONEN.md:4-9` reads `[x]`
with named verifier `revenger-r64.R64ReviewSkill`; the round-68 paragraph's `[~]` sentence is superseded
as a *state* statement and survives only as a *scope* statement (the `[x]` covers the r64 bytes,
39098 B / `bfd92057…`; current bytes are 51809 B / `a12fb8e2…` and have no non-lane re-confirmation;
seven live defects listed in `R69ShonenBox1`). Mistakes: **M48** (identity-without-derivation — the r68
D1 class, found three more times inside this round's own claims text), **M49** (enum-block bound stated
as 237-253 where the block closes at 263), **M50** (frozen-counter regression: new block calls a helper
defined below it; the red-before could not see it because the branch does not exist on the base tree).
Sources: rows 46 → 47 (+S047 supersedes S046), census exit 0 at both ends, same four disclosed W04s.
Quarantine (item 10): `Assimilation: none` for adoption — the full 26-row slice hand-checked, verdicts
per seat in `corpus/lessons/round-69.md` §Item-10; adoption closed; zero package rows or entries copied.
considerthese: `2026-10-24.md` proposal 2 (provider-refusal seats on their own line) landed as a zero line
in the wave record — no seat was lost to a provider refusal.

**planned:** the next coverage round re-gates C05 a fifth time with the routed set: probe-or-drop the
exit-2 clause (Q05), restate `:91` as direct string-pool indexing (Q07), label the recorded ZIP widths and
the `504b0506` key (Q11), fix `:48`'s two counts (Q14), add the `c7b7cf98` derivation and a Q15 row
(Q15). Calibration: hoist `def run` in a NEW counter revision with a fresh red-before *before* any
after-run, map uncaught exceptions to exit 2, move the D1 fixture under `corpus/`, and make the
derivation extension additive (a flag or a second script) so the retained round-68 candidate stays clean.

## Errata to the round-69 section (appended 2026-10-25, round 70 — the rows above stay as written)

erratum: `e1d22caf` -> `e1d22caaf9a2fdc4c1c13d1f4a8a6813e7b07968`

The first line is the machine-read form (`corpus/self_assessment_check.py` SM5): the round-69 pre-registration
commit is `e1d22caaf9a2fdc4c1c13d1f4a8a6813e7b07968` (`git rev-parse e1d22ca`), and the token printed at the
Round 69 section's "Pre-registration" line is an 8-character truncation whose last character is wrong. Two more
corrections from `corpus/lessons/round-69-verifier-spotcheck.md` §6: **V3** — the round-69 C1 table cell that reads
"not printed — the counter crashes before the hold block" is wrong on its second half: the frozen counter printed
`K_HELD_BACKED=8/14` (and `K_HELD_BACKED_STRICT=8/14`) before the `NameError`, and only the hold block was
unprinted; **V4** — the round-69 counting command printed in that table does not run from the fleet root; the
executable form is `cd / && python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-69/measure.py <tree>`
(the absolute-path form already printed in `reports/round-69/claims.md`).

**Round-63 section seat name (found by the round-70 named-unmeasured sweep, `R70W1SM5Sweep` F1).** The Round 63 section's
"`W2ReviewSeparability` (build)" names no seat that ever existed; the build-side separability seat is
`R63ReviewSeparability` (`.ufo/waves/round-63/build/R63ReviewSeparability.md`), and `W2VerifySeparabilityFinal`
(`.ufo/waves/round-63/falsify/W2VerifySeparabilityFinal.md`) is correct as written.

## Round 70 (hyaku run 7, fresh-start round) — C1 falsified (honest stop); C2 and C3 verified as declared

Pre-registration `dbacce212d798d1ec5bb59e03ff91d577eed0283` (claims + frozen counter `reports/round-70/measure.py` sha256
`488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76` + red-before + eight controls on base `3f5edbc206351232a3d2d801334dd930499ccaf5`);
tighten-only amendment A1 (`reports/round-70/claims-amendment-A1.md`, `measure-a1.py` sha256 `96feeaa048f0f2b8ab0f3bb183c714a57ff41e951d4221c09806b6acf2e87191`)
declared before any wave-2 seat scored. Two v1 waves, 40 + 45 = 85 seats, 0 dead seats.

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| coverage — knowledge-map ground K (C05 fifth pass) | `K_HELD_BACKED` 8/14 → 8/14 (5.7 → 5.7); `C05_STATUS` `uncovered` → `uncovered` | `python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-70/measure.py <git archive tree>` | `3f5edbc` → final tip | **C1 FALSIFIED — honest stop**: wave-2 FAIL Q04, Q11b, Q13 on four prose sentences (`:119`, `:152`, `:282`, `:310`); 13 of 16 decisions PASS/n-a; entry marked `rejected`, README unflipped |
| calibration — self-assessment mismatches (new tool `corpus/self_assessment_check.py`) | `SELF_MISMATCH` 9 → 0 (`SM1=1 SM2=4 SM3=2 SM4=1 SM5=1 SM6=0` → all 0); `SELF_MUTANTS_KILLED` n/a → 6/6; `A1_C2` no → yes | same counter (`HOLDS_C2_V5`) and `measure-a1.py` | `3f5edbc` → final tip | **verified as declared**; limits: classes are bounded detectors (`R70W2CheckerClasses`), SM3/SM4 are 0 because overstatement was removed, an env-override hybrid survives both counters (`R70W2CheckerMut`) |
| freshness — retained entries re-derive (digest-pinned historical script) | `EMB_R68` problems 7 → 0 (checked_blocks 17 both); `EMB_R65` 1 → 1 (retained M39 drift still seen); `EMB_PIN_MUTANT_KILLED_ATTRIBUTED` n/a → 1/1; `A1_C3` no → yes | same counter (`HOLDS_C3_V1`) | `3f5edbc` → final tip | **verified as declared** (`R70W2GateReplay` NO-REGRESSION incl. frozen r68 C7 labels; `R70W2PinMutants` 17/17 probes protected) |
| holds | `HOLD_REPLAY` 10/10, `GATE_SELFTEST` exit 0, `F_COVERAGE` 5/8, `FRESH_ROWS` 18/18 both ends | same counter (`HOLDS_OK_V7=yes`) | same | unchanged |
| depth / operability / adjacency | no separate claim | `R70W2SentinelFinal` CONTAINED; ADJ-06 reported-not-absorbed | — | unchanged |

Capabilities: three registered instruments entered the repertoire as tooling, not as a new analysis family — `corpus/self_assessment_check.py` (gate), `corpus/lint_entry.py`
(pre-flight, not a gate), the gate's digest-pin rule and command confinement; their registry rows are in `SKILL.md` §Gate registry. Mistakes mined: M51 (reference drift, captured by SM5),
M52 (frozen predicate reachable by a cheaper control; fixed by A1), M53 (prose credits beyond a command's output; new criterion Q16). Sources: rows 47 → 49 (S048 supersedes S045's locator,
S049 supersedes S043's repo path), census exit 0 at both ends. Assimilation: nothing adopted (two REJECT, one scope ADMIT without an entry), see `corpus/lessons/round-70.md`.

K_HELD_BACKED 8/14 → 8/14

**planned:** the C05 sixth pass is a repair of four sentences of `knowledge/round-70-apk-axml-byte-evidence.md` against the printed outputs (and the same-revision SCORECARD K line);
checker residuals and the env-canary control; the gate's exit-2 contract (`R70W2GateReplay` F1/F2).
## Round 71 (hyaku run 10, attempt 1) — C1 falsified; C2 verified

Supersedes only the round-70 **planned** C05 sixth pass; the earlier round-70 record remains unchanged. Pre-registration `63b560bec2405228797405ec06a818ee343e61f0`, base `b7abcd875c84f4e1d6c8df966b6bd20f4154c53f`, frozen candidate `4c1eeaee88fd07e442f1bd546faf77be3957d390`, and final vote/adjudication measurement commit `dac9590236f0d3e7213c30ccdb343f0891a36644`. Counter `reports/round-71/measure.py` SHA-256 `82c817e1c2f7181cae759328fc884b8c38defbdba80dde4aad535d9c1f5f91b2` (A3).

| axis / criterion | before → final | counting command / evidence | measured commits | verdict |
|---|---|---|---|---|
| coverage — knowledge-map ground K (C05 sixth pass) | `K_HELD_BACKED` 8/14 → 8/14 (5.7 → 5.7); C05 `uncovered` → `uncovered`; frozen 9/14 target unmet | counter below; `C1_W2_Q_VOTES=0/16`, `C1_GATE=24 blocks / 0 problems`, lint `0/0/0/0`, `HOLDS_C1_V6=no`; Q09/Q16 FAILs in `corpus/lessons/round-71.md` | `b7abcd8` → `dac9590` | **C1 FALSIFIED — honest stop;** no entry admitted |
| calibration — declared gate exit-2 outcomes | `C2_MISSING_ENTRY_EXIT2` 0/1 → 1/1 and `C2_TIMEOUT_EXIT2` 0/1 → 1/1 (score 0.0 → 10.0); `HOLDS_C2_V1` no → yes | same counter; missing-entry and production 120s timeout both exit 2 without traceback; self-test exit 0 with both named legs | `b7abcd8` → `dac9590` | **C2 verified as declared** |
| retained holds | `HOLD_REPLAY` 10/10, `F_COVERAGE` 5/8, `FRESH_ROWS` 18/18, `HOLDS_OK_V8=yes` | same counter; all ten `HOLD <name> exit=0` lines captured in `reports/round-71/measure-after.log`; retained `EMB_R65` red label unchanged | `b7abcd8` → `dac9590` | unchanged; no harm observed |

Counting command: `python3 -B reports/round-71/measure.py TREE`; `TREE` was an isolated archive of `dac9590236f0d3e7213c30ccdb343f0891a36644` containing `corpus`, `SKILL.md`, `SCORECARD.md`, `SHONEN.md` and `.ufo/waves/round-71/w2-votes/`. Exact output is `reports/round-71/measure-after.log` (exit 0). The frozen C1 vote rule accepts only PASS/n/a: the 16 decisions include two FAILs, so 0/16 is the correct counter result, not a missing vote receipt.

Learning trends: expansion **unchanged** (no C05 flip, no admitted entry); quality **unchanged** (no existing admitted entry failed re-check and none was strengthened); discernment **unchanged** (the S052/S053 outside spot-check remains pending; no lane seat is counted as outside). No capability added. The counter's live round-70 self-check import limitation is disclosed in `corpus/lessons/round-71.md` and is not claimed as hermetic.
