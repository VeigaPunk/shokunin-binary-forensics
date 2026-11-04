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
| ghidra-headless-recon | Import a PE into the local Ghidra 12.1.4 headless, run auto-analysis, and export per-function decompiled C via a committed Java postScript (Ghidra 12.x Python scripts require PyGhidra, so the postScript is Java) | `reports/round-75/ghidra-headless-recon.log`; fixture `corpus/fixtures/pe-r75-headless-smoke/` (generator + truth pin; regen byte-identical); run: exit 0, `1 functions, 1 decompiled`, `entry @ 140001000` → `return 0x2a;` | round-75 |
| cited-evidence orphan sweep | Enumerate every lane-repo path cited by the closed round reports and lessons, classify each against HEAD and the working tree (committed / orphan / orphan-dir / absent-fleet / absent), and exit 1 naming any landable orphan (on-disk, never committed); hermetic `--selftest` (no git/network/live-tree write) with a planted-orphan vector and an attributed mutant kill | `PYTHONUTF8=1 python -B reports/round-80/orphan_sweep.py --lane <lane> --fleet <fleet-root>` → `CITED=344 COMMITTED=330 LANDABLE_ORPHANS=0 ABSENT=14`, exit 0 (`reports/round-80/sweep-real-after.log`); `--selftest` → `SWEEP_SELFTEST=pass`, exit 0 (`reports/round-80/selftest-after.log`); red-before `reports/round-80/orphan-before.log` | round-80 |

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
## Round 72 (hyaku run 10) — C1 falsified; C15 remains uncovered

Pre-registration and frozen predicate: `reports/round-72/claims.md` + `measure.py`, committed at freeze `1c5b748e86b217d957b1ea6553ed4e71432df7b6`; source/entry candidate and validated wave payload committed at `99911e808a25f8d9ba26e1c00fbb18e755daf820`. C1 was the sole coverage claim. C15 remains `uncovered`; the knowledge file remains a candidate and is not admitted.

| axis / criterion | before → measured candidate | counting command / evidence | measured commits | verdict |
|---|---|---|---|---|
| coverage — knowledge-map ground K / C15 tool landscape | `K_HELD_BACKED` 8/14 (5.7) → 8/15 (5.3); `C15_HELD_BACKED` 0/1 → 0/1; `C15_TOOL_ROWS` 0/18 → 18/18; C15 `uncovered` → `uncovered` | `reports/round-72/measure.py TREE`; exact output and coverage-map count in `reports/round-72/measure-after.log` | prior `dac9590236f0d3e7213c30ccdb343f0891a36644` → candidate `99911e808a25f8d9ba26e1c00fbb18e755daf820` | **C1 FALSIFIED — honest stop:** source rows/entry exist, but README is not held and frozen predicate is 0/1 |
| calibration | no claim; no calibration gate changed | no calibration work was claimed or scored | — | unchanged; no calibration credit |
| retained holds | no hold was flipped; C15 is deliberately not admitted | frozen controls at `reports/round-72/controls/`; final candidate count in `measure-after.log` | freeze → candidate | unchanged |

The counter ran on a `git archive` of candidate `99911e808a25f8d9ba26e1c00fbb18e755daf820`, exited 0, and printed `C15_HELD_BACKED=0/1`, `C15_TOOL_ROWS=18/18`, `HOLDS_C15=no`. Its status-only control also remained 0/1 and 0/18. The coverage-map K count follows the same `held`-row predicate as the round-71 counter; the new uncovered C15 row expands the denominator but not the numerator. The selected v2 wave validated at 64 distinct items (18 reviewer, 22 critic, 8 mutation-tester, 6 executor, 4 scribe, 3 scout, 3 connector; L1 held the planner seat), and `w1.ready` was written. No `WAVE-DONE`/results handoff had arrived when the operator-directed closure interruption occurred; the parent reported explicit five-hour quota 429s and dispatcher ceiling zero. Thus no seat results or non-author verification are credited; dispatch/settlement is unconfirmed. No residual wave or replacement seats were issued.

Sources: `corpus/SOURCES.md` 53 → 95 (42 additions: tier A 37, tier C 5; mined 37, rejected 5), census exit 0; no existing row changed in place. No tool was installed or updated. Do not promote C15 until an independent source review and the unchanged frozen counter both pass.

## Round 73 (hyaku run 12, attempt 2) — C1 unresolved (honest stop); no axis moved

Frozen claim C1 (`reports/round-73/claims.md`, counter `measure.py`, pin `candidate-pin.json`, frozen at `606548a`) was not measured after: the wave that carries its 16 Q votes was validated and handed off (`.ufo/waves/round-73/v2.ready`) but was released un-settled at the operator wrap-up. Counter at `74e1c3e`: `K_HELD_BACKED=8/15` (5.3, unchanged), `C10_HELD_BACKED=0/1`, `C10_Q_VOTES=0/16`. No axis score, capability or retirement changed. The claim neither verifies nor is falsified; the next round carries it unchanged under the frozen rule.
## Round 74 (hyaku run 13, fresh start, new Windows host) — C1 verified (new coverage criterion P); C2 verified (inherited QA criterion 51/51); carried C10 disposed by the frozen kill rule

Fresh-start round per the operator ruling: the last three closures were rejected honest-stops
whose declared claims a do-nothing control could reach (wave never settled). The inherited r74
freeze `85db6ab` (instruments sha-verified unchanged) supplied C2; its carried C10 admission was
ruled out as a claim (required 4-seat Q review cannot exist on this host — no `.ufo/state/`
dispatcher, `/home/vgpnk` absent) and its frozen kill rule was executed instead: counter over
base `85db6ab` → `C10_Q_VOTES=0/16`, `C10_HELD_BACKED=0/1` (`C10_CANDIDATE_PIN=1/1`,
`C10_SOURCES=1/1`, exit 0); candidate `admission-status:` `candidate` → `rejected` (single
line, this round); README C10 stays `partial`; K unchanged. No repair-and-revote under that claim.

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| coverage — province surface accuracy (new bounded criterion P, split recorded here; instrument-level only) | `PROVINCE_SURFACES_RESOLVED=4/11 UNRECORDED_ABSENT=7 P_SCORE=3.6` exit 1 → `11/11 / 0 / 10.0` exit 0 | `bash reports/round-74/province_probe.sh` (before `province-before.log`, after `province-after.log`) | `85db6ab` → this round's tip | **verified as declared**; boundary: K 8/15 (5.3) and F 5/8 unchanged — no coverage-map row moved, no admission claimed |
| calibration — source-registry quote fidelity (inherited frozen QA criterion) | `QA_VERIFIED_TOTAL=0/51 QA_UNRESOLVED=51/51 QA_TARGET=no` (frozen `measure-before.log`) → `QA_VERIFIED=42/42 QA_MANUAL_VERIFIED=9/9 QA_VERIFIED_TOTAL=51/51 QA_UNRESOLVED=0/51 QA_NEGCTRL=pass QA_TARGET=yes`, counter exit 0 | `python -B reports/round-74/measure.py TREE` over `git archive <tip> corpus .ufo/waves/round-74` (host invocation `PYTHONUTF8=1`; sha-pinned counter unchanged) | `85db6ab` → this round's tip (`reports/round-74/measure-after.log`) | **verified as declared**; 10 registry quotes were not verbatim (2 misquotes S062/S068, 1 insertion S094, 2 early ends S063/S080, 5 representation-only) — corrected only via superseding rows S429–S442 opened this round; 3 rejected flips (S062, S068, S094) carry located-quote reasons (Q12) |
| coverage — knowledge-map ground K (C05, C10, C15) | 8/15 (5.3) → 8/15 (5.3); C05 uncovered, C10 partial (candidate rejected this round), C15 uncovered | `reports/round-73/measure.py TREE` (`K_HELD_BACKED=8/15`) | same | **unchanged** (honest: no admission; the round-73 C10 claim is now falsified-closed, not carried) |
| calibration — C2–C8 receipt guards, exit-2 gate, runnability holds | untouched this round; no gate, fixture, admitted entry or Q01–Q16 byte changed | `git diff 85db6ab..<tip> -- corpus/knowledge corpus/live corpus/fixtures corpus/README.md` → only the candidate's one status line | same | unchanged (no harm observed; diff receipt `reports/round-74/no-harm-diff.txt`) |
| freshness | instrument bytes and registry rows re-verified on the new host: 51/51 sources re-fetched with status evidence; verifiers run under `PYTHONUTF8=1` (locale decode defect mined) | same archive counter + instrument self-test exit 0 (7/7 legs) | same | hold, exercised on a new host |
| depth / operability / adjacency | no claim | PROVINCE corrections are coverage P work; no engine claimed (`rea` CLI 6.8.0 probed, presence not readiness, Q05) | — | unchanged (ADJ-06 unchanged) |

Capabilities: none added (the probe is a counting instrument for criterion P, not a new
analysis family). SHONEN unchanged (`[~]` states stand; no outside verifier this round).
Sources: rows 428 → 442 (+S429–S442 mined this round; S062/S068/S094 rejected; no other
in-place change). Census exit 0 at both ends (W01/W04 warnings only). Mistakes mined:
environment-drift freeze defect, locale decode, rendered-vs-fetchable quote drift,
probe summary arithmetic (self-caught) — `corpus/lessons/round-74.md`.

**planned:** next round — (a) outside re-derivation of the 51 receipts is the closure judge's;
if confirmed, QA is a candidate for saturation or sub-axis split; (b) coverage K remains the
lowest criterion: C05/C10/C15 admission all require the wave Q-review surface — on this host
that surface must first exist (L0 filed), so a K move stays blocked and should not be declared
again until the operator rules; (c) P's absent surfaces (engines) may become freshness moves if
the operator installs any.

## Round 75 (hyaku run 14) — P2: the r74 province probe's blind spot fixed with its own red-before; calibration criterion N; first local headless decompilation

Base `f29dc92b3adb4202195bc7fc25b4aa6a5b7a2563`. Two claims, neither exploratory. The r74
carry-in items are addressed in `corpus/lessons/round-75.md` `## Mistakes` (mode-correction
note; treecommit file-args discipline — this round's commit lists explicit files only and is
verified by the mandated diff-stat). Full gate, receipts and mistake mining:
`corpus/lessons/round-75.md`.

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| coverage — province surface accuracy (criterion P revision, instrument P2; split unchanged from r74) | red `P2_SURFACES_RESOLVED=10/11 UNRECORDED_ABSENT=0 STALE_RECORDS=1 P2_SCORE=9.1` exit 1 (`p2-before.log`, base PROVINCE bytes in a fixture; `engine-ghidra STALE-RECORD`) → green `11/11 0 0 10.0` exit 0 (`p2-after.log`) after the dated present-record lands | red: `bash reports/round-75/province_probe2.sh <fixture-with-base-PROVINCE.md>`; green: `bash reports/round-75/province_probe2.sh` | `f29dc92` → this round's tip | **improved, C1 met** — ghidra 12.1.4 (off-PATH install of 2026-10-26, `rea doctor` healthy, S443) was recorded absent on 2026-10-31 by a PATH-only probe; the record is now true and the probe can see the mismatch class. Boundary: K 8/15 (5.3), F 5/8 unchanged; no coverage-map row moved; no admission claimed. v1 on the fixed bytes exits 1 by construction (no PRESENT-record grammar) — disclosed supersession, `negctl-run.log` leg 4 |
| calibration — record-vs-reality mismatch detection (new bounded criterion N) | `NEGCTL_V1_STALE_RECORD_FLAGGED=0/1` (v1 false-pass: exit 0 on a record contradicting the host) → `NEGCTL_V2_STALE_RECORD_FLAGGED=1/1` (exit 1, attributed `engine-ghidra … STALE-RECORD`), `NEGCTL_V2_UNRECORDED_ABSENT_FLAGGED=1/1`, `NEGCTL_V2_POSITIVE_CONTROL=pass`, `NEGCTL_SELFTEST=pass` (0.0 → 10.0) | `bash reports/round-75/probe_negctl.sh` (`negctl-run.log`, exit 0) | same | **improved, C2 met** — the kill leg requires the specific line + token, not merely a non-zero exit |
| coverage — knowledge-map ground K | 8/15 (5.3) → 8/15 at base re-run; untouched by this round (C05 uncovered, C10 partial, C15 uncovered) | `PYTHONUTF8=1 python -B reports/round-73/measure.py <git-archive TREE>` (`holds.log`, exit 0; K operator-blocked per r74 planned (b) — ruled out again, not declared) | `f29dc92` (tip re-run in `tip-verification.log`) | unchanged (operator-blocked route, not attempted) |
| coverage — selected-family presence F | 5/8 (6.25) → 5/8 | SCORECARD F command, cwd=lane (`holds.log`, exit 0); producer route ruled out on S444 (`rea --llms`: zero `inspect_*` operations in 6.8.0 — a 6.5-era-named record would be fabricated) | same | unchanged (blocked route documented, not attempted) |
| freshness — stored-assertion proxy | 18/18 → 18/18 (seed 12 + readiness 6; knowledge files untouched) | `grep -cE '^\| [FK][0-9]+ .*\| (holds\|STALE)' corpus/knowledge/seed.md corpus/knowledge/2026-10-12-rea-readiness-checklist.md` (`holds.log`) | same | unchanged hold |
| calibration — C2–C8 receipt guards, exit-2 gate, runnability | untouched this round; no verifier, gate, fixture (except the new pe-r75-headless-smoke addition), README byte or knowledge byte changed | no-harm diff receipt `reports/round-75/tip-verification.log` (protected paths: corpus/knowledge, corpus/live, corpus/README.md, all pre-r75 fixtures → additions only, the new fixture dir) | same | unchanged (no harm observed) |
| freshness — engine-record currency (re-verification, not a scored criterion) | ida, jadx, binwalk/unblob, pwntools re-probed 2026-11-01 with the wider probe (PATH + `~/tools` + `/c/Program Files` + python imports): all absent, records stand; ghidra record corrected (C1) | P2 run itself (`p2-after.log`) | same | exercised; recorded in lesson Gate |
| depth / operability / adjacency | no claim; no engine readiness claimed (Q05: presence is not readiness) | — | — | unchanged (ADJ-06 unchanged) |

Capabilities: `ghidra-headless-recon` enters the table above on this round's demonstration
(authored fixture, committed generator + Java postScript; `entry @ 140001000` →
`return 0x2a;` against the authored bytes `B82A000000C3`; pe-r53 pipeline leg exit 0 with
Ghidra's own `function_count=0` — no decompile claim from that leg).

Sources: rows 442 → 444 (+S443 own-host Ghidra install, +S444 own-host rea manifest; both
mined, opened this round; C1 is the sourced claim). Census exit 0 at both ends, warning
count 31 → 31 (same disclosed W01/W04 classes; no new warning).
`reports/round-75/census-before.log`, `census-after.log`.

Mistakes mined (full table `corpus/lessons/round-75.md`): PATH-only presence probe
(inherited r74 defect — the round's central find), restored-instrument mode drift (r74
carry-in, closed by the note treecommit cannot avoid), frozen-counter/producer
operation-name drift (S444; routed), shared absent-marker genericity in the first P2
draft (self-caught at the red-before), generator assert-offset defects (self-caught, Q06
held).

Routed forward: F counter revision for current-producer operation names (needs a frozen
mapping table, owner: a future registering round); `rea doctor` node gate
(24.21.0 < required 24.22.1, `environment_healthy: false`) recorded, substrate remediation
refused per PROVINCE; r74 P row's 10.0 stays historical under v1.

**planned:** next round — if the operator installs/registers any engine or the node gate
clears, a readiness move on the newly workable surface (F-family producer route once the F
counter revision exists); otherwise calibration: give criterion N a mutation-killed
attribution pair on the negctl harness itself, or retire/split P2 at saturation. K stays
blocked until the operator rules on the filed L0.

## Round 76 (hyaku run 15) — the routed F-counter revision was premised on a false record; managed family moves through a real 6.8.0 run; criterion R receipt correction

Freeze `68feeca6b625dc94d31de3954cac75391cc22146` (claims + frozen probes sha-pinned
in `reports/round-76/claims.md` + red-befores; `c21e5a4` immediately before it is an
empty-path commit, mined M-r76.3). Landing `9116ddd662b56b8a93232359e63525c53909b4ff`;
final measured revision = the adjudication commit carrying this section. Both claims
causally separable, neither exploratory. Carry-in dispositions (non-author r75 closure):
S444 per-leg correction landed (S445, machine-checked); the sanctioned F-counter
amendment was **not executed — its premise is refuted by producer evidence** (manifest
kebab-case equivalents for every F family; provider-gate payloads carrying snake_case
`details.operation`; a real 6.8.0 record writing `operation: inspect_managed_artifact`),
so the frozen counter bytes stay unchanged (`reports/round-76/claims.md` §carry-in;
`corpus/lessons/round-76.md`).

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| coverage — selected-family record presence (F) | **5/8 → 6/8 (6.25 → 7.50)**, families += `managed` | `PYTHONUTF8=1 python -B reports/round-76/f_probe.py <git-archive tree>/corpus` (predicate byte-equal to the r71 counter's F block; before `f-before.log`, after `f-after.log`) | `6f3a646c` → `9116ddd6` | **improved, C1 met** — one real `rea inspect-managed-artifact` (6.8.0, built-in `rea-dotnet-static`) record on an authored inert managed PE/CLI (`corpus/fixtures/managed-r76/`, generator self-check, regen byte-identical, sha256 `25ece37d…5733c`); identity oracle `ORACLE OK (10/10)` (`corpus/live/runs/round-76/`); boundary: F presence-only, the record+oracle is the gate; no K row moved (K stays 8/15, 5.3) |
| calibration — SOURCES-row receipt fidelity (new bounded criterion R) | red (`receipt-before.log` exit 1: LEG3 FAIL, LEG4 `S444_MISMATCH_FLAGGED`) → **green (`receipt-after.log` exit 0: LEG1/2/3 pass, LEG4 fires) (0.0 → 10.0)** | `bash reports/round-76/receipt_probe.sh` | same | **improved, C2 met** — carries the r75 non-author carry-in: S444's aggregated "prints 0" is false on the `--llms` leg (actual 2: `inspect_macho`, `inspect_signature`; doctor leg 0); superseding row S445 records exact per-leg values; the negative control keeps flagging the base row |
| calibration — carry-in premise re-derivation (not scored; protocol work) | r75 routed premise "F names no longer exist in the producer" → refuted on three independent surfaces (manifest, provider-gate payloads, saved record) | S445 row; `reports/round-76/claims.md` §carry-in | same | routed revision resolved by evidence; no frozen byte changed |
| coverage — knowledge-map ground K | 8/15 (5.3) → 8/15; C05 uncovered, C10 partial, C15 uncovered | `PYTHONUTF8=1 python -B reports/round-73/measure.py <tree>` not re-run this round — no README/knowledge byte changed (no-harm diff below); operator-blocked route (r74 L0 unanswered, re-checked) | same | unchanged (blocked route, not attempted) |
| freshness — stored-assertion proxy | 18/18 → 18/18 (seed 12 + readiness 6) | `grep -cE '^\| [FK][0-9]+ .*\| (holds\|STALE)' corpus/knowledge/seed.md corpus/knowledge/2026-10-12-rea-readiness-checklist.md` | same | unchanged hold |
| calibration — C2–C8 guards, exit-2 gate, runnability | untouched; no verifier/gate/README/knowledge byte changed | `git diff 6f3a646c..9116ddd6 --stat -- corpus/knowledge corpus/README.md corpus/verify_*.py …` → empty on protected paths (`reports/round-76/noharm-diff.txt`: additions only, fixture+run dirs) | same | unchanged (no harm observed) |
| separability | C1-only tree (landing archive, SOURCES reverted to base) still 6/8; C2's before-run executed with zero C1 bytes in the tree | `reports/round-76/f-separability.log`, `r-separability.log` | same | claims separable as frozen |
| depth / operability / adjacency | no claim; no engine readiness claimed (provider presence, not readiness — Q05) | — | — | unchanged (ADJ-06 unchanged) |

Capabilities: none added (the fixture and probes are instruments/evidence, not a new
analysis family). Sources: rows 444 → 446 (+S445 correction supersedes S444, +S446
own-work; both mined, opened this round; C1 and C2 are sourced claims). Census exit 0
at both ends, 31 W → 31 W (same disclosed W01/W04 classes); 444 → 446 rows.
`reports/round-76/census-after.log`. Mistakes mined (full table
`corpus/lessons/round-76.md`): aggregated per-leg receipts (the carry-in class);
routing on an un-re-derived premise; treecommit absolute-path empty commit
(`c21e5a4`, caught by the mandated diff check); generator metadata-layout asserts
(self-caught, Q06 held).

**planned:** next round — if the operator supplies a provider surface (jadx
`REA_JADX_MCP_JAR`, Linux binwalk, or a CDP endpoint), the android/firmware/browser
F families are one bounded producer run each; otherwise calibration: extend criterion
R across the 444 legacy registry rows that quote counting commands (S444 was the
flagged instance), or give criterion N's negctl harness the mutation-killed
attribution pair (r75 planned (b), still open). K stays blocked until the operator
rules on the filed L0.

## Round 77 (hyaku run 16) — browser-runtime moves through a real CDP producer run on the host's own browser; the r76 gate-payload refutation leg becomes committed, machine-checked receipts (criterion G)

(The r76 **planned** paragraph above is superseded below for the items this
round consumed — the CDP endpoint turned out to be supplier-immediate (the
lane itself, r76 spotcheck routed-premise class); the browser family moved,
and the gate-receipt work became criterion G. Android's jadx gate and the
criterion-R/N calibration items stand as written there.)

Freeze `5acef36fe6cd473308bd57ec103372a2cc17ac4a` (claims + probes + red-befores);
landing `071de56028ed32180b210c1559eda9ece99ec132`; final measured revision = the
adjudication commit carrying this section. Both claims causally separable, neither
exploratory. Carry-in dispositions (r76 non-author closure, all status-neutral):
census sanctioned form recorded next to the literal (`SKILL.md` §4a); the
scratch-probe leg committed and machine-checked (C2's substance); the two cosmetic
wording notes applied in `corpus/lessons/round-77.md` §Carry-in (S445 left
byte-untouched). Full gate, receipts and mistake mining: `corpus/lessons/round-77.md`.

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| coverage — selected-family record presence (F) | **6/8 → 7/8 (7.50 → 8.75)**, families += `browser-runtime` | `PYTHONUTF8=1 python -B reports/round-76/f_probe.py <git-archive tree>/corpus` (frozen r76 instrument, sha256 `e15a43af…f39ed` unchanged; before `f-red.log`, after `f-after.log`) | `3e980481` → this round's tip | **improved, C1 met** — one real `rea inspect-web-page` (6.8.0, built-in `rea-cdp-browser`) passive record of an authored inert local page (`corpus/fixtures/browser-r77/`, committed-files-as-truth; regen n/a — no generator) served from the committed bytes on loopback `http://127.0.0.1:8477`, CDP `http://127.0.0.1:9333` (host Chrome/156.0.8078.74 headless, scratch profile, caller-supplied surface — nothing installed); identity oracle `ORACLE OK (17/17 checks)` (`corpus/live/runs/round-77/`), including both `cdp_hash == sha256(authored script text)` bindings. Disclosed histogram delta: `inspect_web_page: 1` + `list_browser_targets: 1` (discovery aux; in no family set). Note (r76 spotcheck item 3a): f_probe prints two decimals; the r71 counter prints `8.8` — representation-only, mapping AST-verified equal. Boundary: F presence-only (r63); android stays uncovered — caller-supplied `REA_JADX_MCP_JAR` absent (committed gate receipt, S448) |
| calibration — provider-gate payload receipt fidelity (new bounded criterion G) | red (`gate-red.log` exit 1: `GATE_LEG0_RECEIPTS_PRESENT=no` over the base archive) → **green (`gate-after.log` exit 0: LEG0 yes, LEG1=1, LEG2=1, LEG3 negctl flagged) (0.0 → 10.0)** | `bash reports/round-77/gate_probe.sh` (sha256 `a594b57f…e84a`, pinned at freeze) | same | **improved, C2 met** — carries r76 spotcheck routed item 2: the producer's own gate payloads (`details.operation` snake_case) are now committed receipts (`corpus/live/runs/round-77/provider-gates/`, S448), re-run live per leg and machine-checked, with a mutated-copy negative control that is flagged (a blind comparator would fail LEG3). The three-surface r76 refutation is fully durable from committed bytes: S445 aliases + S448 payloads + S446/S447 real records |
| coverage — knowledge-map ground K | 8/15 (5.3) → 8/15; C05 uncovered, C10 partial, C15 uncovered | not re-run this round — no README/knowledge byte changed (no-harm diff below); operator-blocked route (r74 L0 unanswered, re-checked) | same | unchanged (blocked route, not attempted) |
| coverage — province surface accuracy (P2 hold) | 11/11 / 0 / 0 / 10.0 exit 0 → same after the dated browser-surface record landed | `bash reports/round-75/province_probe2.sh` (`p2-rerun.log`) | same | unchanged hold — the frozen probe's fixed token list does not see the new record by construction (routed: wiring it into a future P revision is a future registering round's call) |
| freshness — stored-assertion proxy | 18/18 → 18/18 (seed 12 + readiness 6) | `grep -cE '^\| [FK][0-9]+ .*\| (holds\|STALE)' corpus/knowledge/seed.md corpus/knowledge/2026-10-12-rea-readiness-checklist.md` (exit 0) | same | unchanged hold |
| calibration — C2–C8 guards, exit-2 gate, runnability; C/R criteria | untouched; no verifier, gate, README or knowledge byte changed | no-harm diff: protected paths (knowledge, README, verifiers, SHONEN, LOG, SCORECARD, r71 counter, r76 f_probe) empty on 3e980481..071de560 (`reports/round-77/noharm-diff.txt`); `reports/round-76/f_probe.py` blob unchanged | same | unchanged (no harm observed) |
| separability | C1-only tree (provider-gates + gate_probe removed) still 7/8; C2-only tree (all browser-r77 bytes removed; probe references 0 browser-r77 paths) still green | `f-separability.log`, `g-separability.log` | same | claims separable as frozen |
| depth / operability / adjacency | no claim; no engine readiness claimed beyond the demonstrated run (Q05: the PROVINCE browser record cites the run receipt, not presence) | — | — | unchanged (ADJ-06 unchanged) |

Capabilities: none added (the fixture, oracle and probe are instruments/evidence;
the CDP observation route is REA's built-in provider, exercised once — not a new
analysis capability owned by this lane).

Sources: rows 446 → 448 (+S447 the recorded browser record, +S448 the committed
gate receipts; both mined, opened this round; C1 and C2 are sourced claims).
Census exit 0 at both ends, warning count 31 → 31 (same disclosed W01/W04
classes); the literal contract form exits 2 and the sanctioned explicit-lane-dir
form exits 0 — both recorded with real outputs in `SKILL.md` §4a and the lesson
`## Census` (r76 spotcheck routed item 1). `reports/round-77/census-after.log`.
Mistakes mined (full table `corpus/lessons/round-77.md` `## Mistakes`): assumed
observation (script-source retention under late attach — caught by reading the
producer record before pinning expectations), incomplete red tree (instrument
bytes missing from the first red extraction — self-caught), surface-reachability
premise inherited unexamined ("caller-supplied" read as operator-supplied —
re-derived before any fixture was authored).

**planned:** next round — F's last family (android) is hard-gated on the
caller-supplied `REA_JADX_MCP_JAR` (jadx-headless-mcp 0.7.1, absent; committed
receipt): it moves only if that surface appears; otherwise calibration (criterion
R extension to the legacy receipt-quoting rows, or criterion N's mutation-killed
attribution pair — r75 planned (b), still open). K stays blocked until the
operator rules on the filed L0.

## Round 78 (hyaku run 17; watchdog driver label `zcode run14` is the driver's process label, not a run counter) — the province probe learns the browser surface (criterion P3); criterion G/R instruments registered per the §Gate standard

Base `9676f52f627cacbcf1eeab8093c212743ec4a2bd`. Freeze
`f042b2959a257644782405f295272486389fc908` (claims + sha-pinned instruments +
red-befores). Landing `7f303c3d53b148c82d1296f66f40e924d18b2af5` (SKILL registry
rows, S449/S450, lesson). Correction `b7fee90ff4308498a696ebec1fb0911f0cc67f12`
(disclosed post-freeze p3_negctl LEG4 tree-resolution fix + lesson mistake row 3) —
final measured revision = the adjudication commit carrying this section. Both claims
causally separable, neither exploratory. Carry-in dispositions (r77 non-author
closure, all status-neutral): the two gate registrations landed (C2), the sanctioned
census form stays documented in SKILL.md §4a (re-run both forms this round), and the
report-title/driver-label alignment is applied. Full gate, receipts and mistake
mining: `corpus/lessons/round-78.md`.

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| coverage — province surface accuracy (criterion P revision, instrument P3; supersedes the r75 P2 as the criterion's instrument) | score held **10.0 → 10.0** at **11 → 12 surfaces**; the moved quantity is the caught defect class: `P2_NEGCTL_STALE_BROWSER_FLAGGED=0/1` (frozen v2 exits 0 on a stale browser record — `p3-before.log`, committed at freeze) → `P3_NEGCTL_STALE_BROWSER_FLAGGED=1/1` (exit 1, attributed to `cdp-browser STALE-RECORD`; `P3_NEGCTL_VERDICT=green` from the b7fee90f archive bytes, `p3-negctl-run.log`; standalone `p3-after.log`: fixture exit 1, lane exit 0 12/12) | red: `bash reports/round-75/province_probe2.sh <fixture-with-stale-browser-record>` → exit 0; after: `bash reports/round-78/province_probe3.sh <same-fixture>` → exit 1, and `bash reports/round-78/province_probe3.sh <lane-dir>` → exit 0 `P3_SCORE=10.0` | `f042b295` (red) → `b7fee90f` | **improved, C1 met** — the r77-routed blind spot (P2's fixed surface list predates the browser record, S450) is closed with its own red-before; no PROVINCE.md byte changed (blob `bd7cd320` identical base↔tip); boundary: a PRESENT surface with no record is green by design and the UNRECORDED-ABSENT state is not manufacturable for cdp-browser in a fixture — disclosed, not claimed (`P3_NEGCTL_UNRECORDED_ABSENT_LEG=not-claimable`) |
| calibration — gate-registry registration (r77 carry-in item 1; criterion R unregistered since r76) | registered instruments in the SKILL.md Gate registry **3 → 5**; probe-path rows **0 → 2** | `sed -n '/^## Gate registry/,/^## [^G]/p' SKILL.md \| grep -cE '^\| name \|'` (before `registry-before.log` = 3, after `registry-after.log` = 5) and `grep -cE 'reports/round-7[67]/(gate\|receipt)_probe' SKILL.md` (0 → 2) | `f042b295` (red) → `b7fee90f` | **improved, C2 met** — criterion G's `gate_probe.sh` and criterion R's `receipt_probe.sh` are registered with the PROTOCOL §Gate-standard row fields (S449: "closure grades no gate conformant until its registry row exists at the lane's registry home"), including the honest disposition that neither exposes a self-test mode (routed debt, not claimed); no criterion score moved (C 5.0, N 10.0, R 10.0, G 10.0 all held) — the closed gap is that two in-use verdict instruments were invisible to gate-conformance checking |
| coverage — knowledge-map ground K | 8/15 (5.3) → 8/15; C05 uncovered, C10 partial, C15 uncovered | not re-run — no README/knowledge byte changed (no-harm diff below); operator-blocked route (r74 L0 unanswered, re-checked in the fleet `.ufo/l0-questions.md` this round) | same | unchanged (blocked route, not attempted) |
| coverage — selected-family record presence F | 7/8 (8.75) → 7/8; android hard-gated on the caller-supplied `REA_JADX_MCP_JAR` (env unset, no jadx on PATH, no `~/tools/jadx*` — re-probed this round; S448 receipt stands) | `PYTHONUTF8=1 python -B reports/round-76/f_probe.py <archive-tree>/corpus` (`holds.log`, exit 0) | same | unchanged (gated route, not attempted) |
| freshness — stored-assertion proxy | 18/18 → 18/18 (seed 12 + readiness 6; knowledge files untouched) | `grep -cE '^\| [FK][0-9]+ .*\| (holds\|STALE)' corpus/knowledge/seed.md corpus/knowledge/2026-10-12-rea-readiness-checklist.md` (`holds.log`) | same | unchanged hold |
| calibration — C2–C8 guards, exit-2 gate, runnability; C/R/G criteria bytes | untouched; no verifier, gate, README or knowledge byte changed | no-harm diff: protected paths (knowledge, README, verifiers, SHONEN, P2, f_probe, receipt_probe, gate_probe, PROVINCE.md) empty on 9676f52f..b7fee90f; frozen instruments blob-identical (P2 `8760ae57`, f_probe `ea42e6c2`, receipt_probe `7b51a021`, gate_probe `58816812`); whole range 551 insertions, 0 deletions (`reports/round-78/noharm-diff.txt`) | same | unchanged (no harm observed) |
| separability | C1-only tree (base archive + P3/negctl, no SKILL/SOURCES bytes): negctl green, registry still 3/0 (`c1-only.log`); C2-only tree (base archive + landing SKILL.md, no probe bytes): registry 5/2 holds, P2 still 11/11 (`c2-only.log`) | see the two logs | same | claims separable as frozen |
| depth / operability / adjacency | no claim; no engine readiness claimed (Q05: P3 resolves the recorded browser binaries' presence, exactly as the engine rows resolve theirs) | — | — | unchanged (ADJ-06 unchanged) |

Instrument pins: `reports/round-78/province_probe3.sh` sha256
`bde7ecd04ed8f9b7b2326f7e8fd7c4d129da73b7c3ad3ee6ef185b06bf77e1f4` (unchanged since
the freeze); `reports/round-78/p3_negctl.sh` sha256 `68b78ea1…9d17` at the freeze,
superseded by the disclosed post-freeze LEG4 correction — current sha256
`a7f0f6fd846784802a68011a1d3a6c56da660d35c473765bb47145c260a1f54f` (mistake row 3;
red-befores and the C1 predicate bytes unaffected). Sources: rows 448 → 450 (+S449
fleet PROTOCOL §Gate standard, +S450 the committed r77 routed items; both opened this
round; C1 and C2 are sourced claims). Census exit 0 at both ends, warning count
31 → 31 (same disclosed W01/W04 classes; literal form exit 2, old-host layout,
routed r74–r78 lineage); `reports/round-78/census-before.log`, `census-after.log`.
Mistakes mined (full table `corpus/lessons/round-78.md` `## Mistakes`): dropped
r75 fixture scaffolding (self-caught at the red-before), semantically impossible
LEG3 expectation (self-caught at the red-before), post-freeze LEG4 tree-resolution
defect (caught by the committed-bytes receipt run), SOURCES row written in prose
shape vs the census parser's grammar (caught by the round-end census receipt).

**planned:** next round — calibration: criterion R extension to the legacy
receipt-quoting registry rows (r76 routed), or criterion N's mutation-killed
attribution pair (r75 planned (b), still open), or criterion C repair (the two
failing replay verifiers, routed since r75; re-confirmed failing this round);
protocol: self-test modes for the two newly registered gates mean superseding
instrument revisions, not edits of the pinned bytes, and the criterion-instrument
registration class question (P/F/counters) stays routed to a future registering
round. Coverage: F android moves only if the caller-supplied `REA_JADX_MCP_JAR`
appears; K stays blocked until the operator rules on the filed L0.

## Round 79 (hyaku run 18) — a ninth F family moves through a real certificate-table producer run (criterion F2, `native-authenticode`); both registered gates gain §Gate-standard self-test modes (v2 supersessions)

Base `c205ef83ca3fa8e0c0e20488625d232cc3efc4c7`. Freeze
`34c2c5a1dc77424ab93044842e4161c87b23c818` (claims + sha-pinned instruments +
red-befores + pre-probe receipt). Landing
`95e50032a6484f42297a6072d39843cc0222887d` (fixture + producer record + SKILL
registry rows + S451–S453); final measured revision = the adjudication commit
carrying this section. Both claims causally separable, neither exploratory.
Carry-in dispositions (r78 non-author closure, all status-neutral): the gate
self-test routed debt is closed by supersession (C2's substance); the census
lineage L0 consolidation line landed; the class question and criterion C repair
stay routed. Full gate, receipts and mistake mining: `corpus/lessons/round-79.md`.

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| coverage — selected-family record presence (F2, registered mapping revision; supersedes the frozen f_probe as the criterion's counting instrument) | **7/8 (8.75) → 8/9 (8.89)** on the registered instrument; v1 frozen instrument holds **7/8 (8.75) → 7/8** on the unchanged frozen eight | before: `PYTHONUTF8=1 python -B reports/round-76/f_probe.py <base-archive>/corpus` + `PYTHONUTF8=1 python -B reports/round-79/f_probe2.py <base-archive>/corpus` (`f2-before.log`); after: same two over the landing archive (`f2-after.log`) | `c205ef83` → `95e50032` | **improved, C1 met** — one real `rea inspect-pe-certificates` run (6.8.0, built-in `rea-pe-certificates`) on an authored inert native PE32 certificate-table fixture (`corpus/fixtures/native-auth-r79/`, generator self-check, regen byte-identical, sha256 `813778b9…cf80`); identity oracle `ORACLE OK (27/27 checks)` over the archive bytes (`corpus/live/runs/round-79/`, Evidence `ev_3701e3a1…52fcc`). Honest boundary: numerator+denominator move together (had the record not landed, F2 prints 7/9 = 7.78 < 7/8) — the moved quantity is the in-province family with an oracle-checked record, not the print; android stays hard-gated (macho/signature ruled out on S453 `unsupported_host`) |
| calibration — §Gate-standard self-test modes for the two registered gates (routed debt closed by supersession) | `SELFTEST_MODE_PRESENT` **0/2 → 2/2**, `SELFTEST_MUTANT_KILLED_ATTRIBUTED` **0/2 → 2/2**, `USAGE_EXIT64` **0/2 → 2/2**; plain-mode value lines byte-equal to v1 (no verdict drift) | `bash reports/round-79/selftest_probe.sh <gate-script> <receipt-script>` (before: v1 pair → `selftest-before.log` exit 1; after: v2 pair over the landing archive → `selftest-after.log` exit 0; plain drift → `plain-equal.log`) | `c205ef83` (red) → `95e50032` | **improved, C2 met** — `gate_probe2.sh`/`receipt_probe2.sh` expose hermetic `--selftest` modes (no producer call — PATH-stripped leg in the receipt) asserting the exit code AND stable committed finding-ids per S452; frozen sed mutants die with the attributed last lines; unrecognized forms exit 64; criterion G/R scores hold **10.0 → 10.0** over identical verdict bytes; v1 bytes and registry rows stand |
| coverage — knowledge-map ground K | 8/15 (5.3) → 8/15; C05 uncovered, C10 partial, C15 uncovered | not re-run — no README/knowledge byte changed (no-harm diff below); operator-blocked route (r74 L0 unanswered, re-checked) | same | unchanged (blocked route, not attempted) |
| coverage — province surface accuracy (P3 hold) | 12/12 / 0 / 0 / 10.0 exit 0 → same (instrument untouched this round) | `bash reports/round-78/province_probe3.sh <lane-dir>` not re-run — probe and PROVINCE bytes unchanged (no-harm diff) | same | unchanged hold |
| freshness — stored-assertion proxy | 18/18 → 18/18 (seed 12 + readiness 6; knowledge files untouched) | `grep -cE '^\| [FK][0-9]+ .*\| (holds\|STALE)' corpus/knowledge/seed.md corpus/knowledge/2026-10-12-rea-readiness-checklist.md` (exit 0) | same | unchanged hold |
| calibration — C2–C8 receipt guards, exit-2 gate, runnability; C/N/R/G criteria bytes | untouched; no verifier, README or knowledge byte changed; v1 criterion instruments blob-identical (f_probe `e15a43af…`, receipt_probe `9315f8d8…`, gate_probe `a594b57f…`) | no-harm diff: protected paths empty on `c205ef83..95e50032` (`reports/round-79/noharm-diff.txt`) | same | unchanged (no harm observed) |
| separability | C1-only tree (base + fixture/record + f_probe2, no v2 scripts): F2 8/9, selftest probe red (`c1-only.log`); C2-only tree (base + v2 scripts + SKILL.md, no record): selftest probe green 2/2 ×3, F2 7/9 (`c2-only.log`) | see the two logs | same | claims separable as frozen |
| depth / operability / adjacency | no claim; no engine readiness claimed (Q05: the record demonstrates the built-in provider's structural read, not a general capability) | — | — | unchanged (ADJ-06 unchanged) |

Capabilities: none added (the fixture/oracle/F2 mapping and the v2 gates are
instruments and evidence; the certificate-table route is REA's built-in provider,
exercised once — not a new analysis family owned by this lane).

Sources: rows 450 → 453 (+S451 the record, +S452 the §Self-test/§Verdict clauses at
the S449 checkout, +S453 the producer capability surface; all opened this round; C1
and C2 are sourced claims). Census exit 0 at round end (sanctioned form, 31 W — same
disclosed W01/W04 classes as round start; literal form exit 2, unchanged r74–r79
lineage, L0 consolidation line landed). `reports/round-79/census-after.log`.
Mistakes mined (full table `corpus/lessons/round-79.md` `## Mistakes`): SOURCES rows
appended at EOF outside the Registry section (E12 ×3, caught by the round-end
census), non-8-aligned WIN_CERTIFICATE length (self-caught at the scratch
self-check), producer_expected drafted from the observed record instead of the
authored bytes (self-caught, Q06 — the generator now derives every fact the oracle
checks).

**planned:** next round — calibration: criterion R extension to the legacy
receipt-quoting rows, or criterion N's mutation-killed attribution pair (r75 planned
(b), still open), or criterion C repair (§9-ruled-out twice; needs the operator to
rule the fixture-chain re-authoring in scope). Coverage: F android moves only if the
caller-supplied `REA_JADX_MCP_JAR` appears; no other in-province producer family is
manufacturable on this host (S453: macho/signature `unsupported_host`) — a further F
move needs a new host surface. K stays blocked until the operator rules on the filed
L0. The criterion-instrument class question stays routed.

Routed forward: the class question (F2 was frozen as a claims revision, not a
registry row); criterion C repair; criterion R extension; criterion N attribution
pair; F android gate; K L0; census literal form (operator-side, lineage L0 landed).

## Round 80 (hyaku run 19) — a tenth F family moves through a real SQLite schema-inventory producer run (criterion F3, `sqlite`); the cited-evidence hygiene duty becomes a standing self-testing instrument (capability: orphan sweep)

Base `4eb2856a88514ae12e67337c1bb962197b4bd189`. Freeze
`f21e0d51a91a2ad5e941baa390132c6cf19bbaad` (claims + sha-pinned instruments +
red-befores + pre-probe receipt). Landing
`ef7d3ee34f547e3f1451d944135df8722cf902fd` (fixture + producer record + S454–S456 +
the committed form of the r79 SOURCES row-move fix — see Mistakes row 1 in
`corpus/lessons/round-80.md`); final measured revision = the adjudication commit
carrying this section. Two claims, distinct axes, causally separable, neither
exploratory; C2 is a capability acquisition. Carry-in dispositions (r79 non-author
closure, addressed first): the §Census 32W→31W correction filed as an appended
erratum in `corpus/lessons/round-79.md`; the orphaned-evidence hygiene duty executed
twice (hand sweep + the C2 instrument): 344 cited paths, **zero landable orphans**,
14 recorded dispositions. Full gate, receipts and mistake mining:
`corpus/lessons/round-80.md`.

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| coverage — selected-family record presence (F3, registered mapping revision; supersedes the frozen F2 mapping as the criterion's counting instrument) | **8/9 (8.89) → 9/10 (9.00)** on the registered instrument; frozen instruments hold: v1 `F_COVERAGE=7/8 (8.75)` unchanged, `F2_COVERAGE=8/9 (8.89)` unchanged on the frozen nine | before: `PYTHONUTF8=1 python -B reports/round-76/f_probe.py <base-archive>/corpus`, `…/reports/round-79/f_probe2.py`, `…/reports/round-80/f_probe3.py` → `f3-before.log` (8/10 = 8.00, sqlite absent); after: same three over the landing archive → `f3-after.log` | `4eb2856` → `ef7d3ee3` | **improved, C1 met** — one real `rea inspect-sqlite-database --schema-scope database --format json` run (rea 6.8.0, built-in `sqlite` provider, SQLite 3.53.4 worker) on the authored inert SQLite fixture (`corpus/fixtures/sqlite-r80/`, generator self-check derives every oracle-checked fact from the built bytes incl. a page-1 sqlite_master b-tree parse; regen byte-identical; sha256 `30703cce…8fbed8`); oracle `ORACLE OK (34/34 checks)` over the archive bytes (`corpus/live/runs/round-80/`, Evidence `ev_5e68ebfe…5f290`). Honest boundary: numerator+denominator move together (had the record not landed, F3 prints 8/10 = 8.00 < 8.89); android stays hard-gated — F3's honest exception is 9/10, not 10/10 (macho/signature `unsupported_host`, S453; jadx JAR absent) |
| calibration — capability acquisition: standing cited-evidence orphan sweep (the routed hygiene duty, institutionalized) | capability absent (hand-only; the r78 class) → present: `CITED=344 COMMITTED=330 LANDABLE_ORPHANS=0 ABSENT=14`, exit 0 on the real tree; `--selftest` 4 legs ok + `SWEEP_SELFTEST=pass` exit 0 with the mutant leg `SWEEP_SELFTEST_MUTANT_FLAGGED=ok` | before: `git cat-file -e 4eb2856:reports/round-80/orphan_sweep.py` → exit 128 (`orphan-before.log`); after: `PYTHONUTF8=1 python -B reports/round-80/orphan_sweep.py --selftest` → `selftest-after.log`; `… --lane <lane> --fleet <fleet-root>` → `sweep-real-after.log` | `4eb2856` → adjudication | **improved, C2 met** — `reports/round-80/orphan_sweep.py` (sha `f21f5e3d…890b`, declared exits 0/1/64) classifies every cited lane path against HEAD and disk, exits 1 naming any landable orphan; hermetic selftest proven by running it from the extracted archive outside any repo; the mutant leg kills a sabotaged blind classifier with the attributed vector; the 14 real-tree dispositions match the hand sweep one-for-one; enters the capabilities table this round. Known parser limitations named in claims §C2 (multi-line-ref remnants, dir-style cites) and dispositioned by hand |
| coverage — knowledge-map ground K | 8/15 (5.3) → 8/15; C05 uncovered, C10 partial, C15 uncovered | not re-run — no README/knowledge byte changed (no-harm diff below); operator-blocked route (r74 L0 unanswered, re-read at the fleet `.ufo/l0-questions.md:233`) | same | unchanged (blocked route, not attempted) |
| coverage — province surface accuracy (P3 hold) | 12/12 / 0 / 0 / 10.0 exit 0 → same (probe and PROVINCE bytes unchanged) | `bash reports/round-78/province_probe3.sh <lane-dir>` not re-run — no-harm diff | same | unchanged hold |
| freshness — stored-assertion proxy | 18/18 → 18/18 (seed 12 + readiness 6; knowledge files untouched) | `grep -cE '^\| [FK][0-9]+ .*\| (holds\|STALE)' corpus/knowledge/seed.md corpus/knowledge/2026-10-12-rea-readiness-checklist.md` (exit 0) | same | unchanged hold |
| calibration — C2–C8 receipt guards, exit-2 gate, runnability; G/R/N criteria bytes | untouched; no verifier, README or knowledge byte changed; v1/F2 criterion instruments blob-identical (f_probe `e15a43af…`, f_probe2 `0be0d8b5…`) | no-harm diff: protected paths empty on `4eb2856..ef7d3ee3` (`reports/round-80/noharm-diff.txt`) | same | unchanged (no harm observed) |
| separability | C1-only tree (base + fixture/record + f_probe3, no orphan_sweep): F3 9/10, instrument ABSENT (`c1-only.log`); C2-only tree (base + orphan_sweep, no fixture/record/f_probe3): selftest pass + real sweep exit 0, F2 prints 8/9 (`c2-only.log`) | see the two logs | same | claims separable as frozen |
| depth / operability / adjacency | no claim; no engine readiness claimed (Q05: the record demonstrates the built-in sqlite provider's schema-inventory read of one authored fixture, not general database forensics — rows unrequested, WAL/encrypted/forensics outside the producer's own profile) | — | — | unchanged (ADJ-06 unchanged) |

Capabilities: **one added** — cited-evidence orphan sweep (row above; demonstrated
running this round with its red-before and selftest receipts).

Sources: rows 453 → 456 (+S454 the sqlite capability surface [own-work, tier A],
+S455 the producer record [own-work, tier A], +S456 the r78 orphan-incident commit
[own-work, tier A]; C1 and C2 are both sourced claims). The landing also commits the
r79 SOURCES row-move fix that had existed only in the worktree (Mistakes row 1).
Census: round start — literal exit 2 (disclosed lineage), sanctioned exit 0, 31 W;
landing-tip archive census — no E12 (the fix is really committed), but `E01 S454
fields=13` (row-grammar pipes, fixed in the adjudication) and `E11 S455` used-by
preceding the lesson (resolved by it); round end — both worktree and final-tip
archive forms expected exit 0, receipts `reports/round-80/census-after.log`.
Mistakes mined (full table `corpus/lessons/round-80.md`): the worktree-only r79
E12 fix (caught by the no-harm pure-append check), SOURCES row-grammar pipes (caught
by the census), the r79 32W-vs-31W narrative count (caught by the r79 closure,
erratum filed), and a self-caught u16/u32 header-width parse bug (pre-freeze).

**planned:** next round — calibration: criterion R extension to the legacy
receipt-quoting rows, or criterion N's mutation-killed attribution pair (both
re-offered and re-superseded this round; N's negctl harness selftests since r75), or
the orphan_sweep tokenizer tightening (the named parser limitations). Coverage: F
android moves only if the caller-supplied `REA_JADX_MCP_JAR` appears; the remaining
uncovered producer surfaces are host-gated (macho/signature, S453) or outside the
declared families — a further F move needs a new host surface. K stays blocked until
the operator rules on the filed L0.

Routed forward: criterion R extension; criterion N attribution pair; criterion C
repair (§9); the class question (instruments vs registry rows — orphan_sweep lands
as a capability, not a row); F android gate; K L0; census literal form
(operator-side, lineage L0 landed r79).

## Erratum to the round-80 section (appended 2026-11-01, round 81 — the rows above stay as written)

erratum (r80 non-author closure routed item 1, root-caused first-hand in
`reports/round-81/preprobe-keyed-shape.log` §r80-corpus reconstruction): the
`CITED=344 COMMITTED=330 LANDABLE_ORPHANS=0 ABSENT=14` figures quoted in the
round-80 section's C2 row, the capabilities table's `cited-evidence orphan
sweep` row, the round-80 report and `reports/round-80/claims.md` are the
**landing-era citation corpus** (lane lessons at `ef7d3ee3` + fleet reports
through round-79) — reproduced exactly this round: 344 tokens → 330 committed +
6 absent-fleet + 8 absent, LANDABLE_ORPHANS=0, under the v1 tokenizer and
classification rules. The committed receipt `reports/round-80/
sweep-real-after.log` (regenerated at `b1e0c60e`) carries
`CITED=357 COMMITTED=343` — its corpus is the post-adjudication one (the
round-80 adjudication lesson + r79 erratum and the fleet round-80 report
joined; 357 also reproduced exactly). The current tree prints CITED=358 (the
r80 spot-check lesson, +1 net-new). Verdict-bearing values are identical in
every corpus: LANDABLE_ORPHANS=0, ABSENT=14, exit 0 — no verdict changes; the
drift is corpus membership, not measurement error. Standing rule (landed as
orphan_sweep2 change 3, round 81): a sweep receipt carries its count basis
(the `SWEEP_CORPUS fleet-reports=<n> lessons=<n>` header); a narrative count
is a `grep -c` of a named-corpus receipt, never a recalled or cross-corpus
number. The truncated receipt form (2 of the SWEEP lines, no stated filter)
is likewise superseded: round-81 receipts carry full output
(`sweep2-real-after.log`) or an in-output filter statement
(`--format summary`).

## Round 81 (hyaku run 20) — an eleventh F family moves through a real Foundation keyed-archive producer run (criterion F4, `artifact-graph`); the orphan sweep learns the r80 carry-in classes (v2 supersession)

Base `081f032fda9502ebfbceb295d7e097dd8803bce1`. Freeze
`8261a24cb806d60a47a640f948de339912dcc96b` (claims + sha-pinned instruments +
red-befores + preprobe receipt). Landing
`88b7e7cee2f07c77b7d9597e8d9e3159aed37f19` (fixture + producer record +
S457–S458); final measured revision = the adjudication commit carrying this
section. Two claims, distinct axes, causally separable, neither exploratory.
Carry-in dispositions (r80 non-author closure, addressed first): the
sweep-count drift corrected by the appended erratum above (first-hand
reproduction, per-revision citation corpora named); the truncated receipt
class closed inside v2 (full output + count basis); the SHONEN `[~]` reviewer
debt is operator-side — routed around, no SHONEN claim. Full gate, receipts
and mistake mining: `corpus/lessons/round-81.md`.

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| coverage — selected-family record presence (F4, registered mapping revision; supersedes the frozen F3 mapping as the criterion's counting instrument) | **9/10 (9.00) → 10/11 (9.09)** on the registered instrument; frozen instruments hold: v1 `F_COVERAGE=7/8 (8.75)`, `F2_COVERAGE=8/9 (8.89)`, `F3_COVERAGE=9/10 (9.00)` unchanged | before: `PYTHONUTF8=1 python -B reports/round-76/f_probe.py <base-archive>/corpus`, `…/reports/round-79/f_probe2.py`, `…/reports/round-80/f_probe3.py`, `…/reports/round-81/f_probe4.py` → `f4-before.log` (9/11 = 8.18, artifact-graph absent); after: same four over the landing archive → `f4-after.log` | `081f032` → `88b7e7ce` | **improved, C1 met** — one real `rea inspect-keyed-archive corpus/fixtures/keyed-r81/fixture.plist --format json` run (rea 6.8.0, built-in `rea-artifact-graph` provider) on the authored inert Foundation keyed-archive fixture (210 bytes, generator self-check derives every oracle-checked fact from the built bytes — roots, 6 objects, 4 references; regen byte-identical; sha256 `f0e02e64…37785c`); oracle `ORACLE OK (27/27 checks)` over the archive bytes (`corpus/live/runs/round-81/`, Evidence `ev_6eb77fb0…02af4b73`). Honest boundary: numerator+denominator move together (had the record not landed, F4 prints 9/11 = 8.18 < 9.00); android stays hard-gated — F4's honest exception is 10/11, not 11/11; the family's other two operations stay available-but-unrecorded |
| calibration — standing cited-evidence orphan sweep, v2 supersession (capability improvement, not a new capability) | red (`sweep-v1-red.log`: v1 full output — `CITED=358 COMMITTED=344 ABSENT=14`, NO count-basis line, the two parser-artifact tokens misdisposed absent, grep = 2; plus the committed r80 truncated receipt as the second red) → green: `SWEEP_SELFTEST=pass` 7/7 legs exit 0 (line-ref, dir-style, masked-absent-negative vectors + attributed mutant kill; hermetic archive run, `sweep2-selftest-after.log`); real tree FULL output + `SWEEP_CORPUS fleet-reports=21 lessons=42` + `CITED=357 COMMITTED=345 LANDABLE_ORPHANS=0 ABSENT=12` exit 0, parser-artifact grep = 0 (`sweep2-real-after.log`) | `PYTHONUTF8=1 python -B reports/round-81/orphan_sweep2.py --selftest` / `… --lane <lane> --fleet <fleet-root> [--format full\|summary]`; parser-artifact grep: `grep -cE '^SWEEP absent (corpus/knowledge/round-68-apk-axml-byte-evidence\.md:57\|corpus/lessons/round-64) ' <receipt>` | `081f032` (red) → adjudication | **improved, C2 met** — `reports/round-81/orphan_sweep2.py` (sha `30aa3527…93eb6`; v1 blob unchanged `f21f5e3d…1890b`): repeated line-ref stripping (the r80 `:57,:148,` false absent), dir-style cite normalization with the masked-absent negative (r80 `corpus/lessons/round-64`), the `SWEEP_CORPUS` count basis (the r80 CITED=344-vs-357 routed rule), and full-output receipts (the r80 2-of-357-lines class); declared exits 0/1/64 unchanged; counts remain per-revision-corpus (the erratum rule above). Supersession note for the capabilities table: the `cited-evidence orphan sweep` row's current instrument is v2 (this round's receipts), first-working round unchanged (r80) |
| coverage — knowledge-map ground K | 8/15 (5.3) → 8/15; C05 uncovered, C10 partial, C15 uncovered | not re-run — no README/knowledge byte changed (no-harm diff below); operator-blocked route (r74 L0 unanswered, re-read at the fleet `.ufo/l0-questions.md:233`) | same | unchanged (blocked route, not attempted) |
| coverage — province surface accuracy (P3 hold) | 12/12 / 0 / 0 / 10.0 exit 0 → same (probe and PROVINCE bytes unchanged) | `bash reports/round-78/province_probe3.sh <lane-dir>` not re-run — no-harm diff | same | unchanged hold |
| freshness — stored-assertion proxy | 18/18 → 18/18 (seed 12 + readiness 6; knowledge files untouched) | `grep -cE '^\| [FK][0-9]+ .*\| (holds\|STALE)' corpus/knowledge/seed.md corpus/knowledge/2026-10-12-rea-readiness-checklist.md` | same | unchanged hold |
| calibration — C2–C8 receipt guards, exit-2 gate, runnability; C/N/R/G criteria bytes | untouched; no verifier, README or knowledge byte changed; v1/F2/F3 criterion instruments blob/sha-identical (`noharm-diff.txt`: protected paths empty on `081f032..88b7e7ce`; content sha256s match their pins) | no-harm diff receipt `reports/round-81/noharm-diff.txt` | same | unchanged (no harm observed) |
| separability | C1-only tree (base + fixture/record + f_probe4, no orphan_sweep2): F4 10/11 + oracle 27/27, instrument ABSENT (`c1-only.log`); C2-only tree (base + orphan_sweep2, no fixture/record/f_probe4): selftest pass, F2 prints 8/9 (`c2-only.log`) | see the two logs | same | claims separable as frozen |
| depth / operability / adjacency | no claim; no engine readiness claimed (Q05: the record demonstrates the built-in artifact-graph provider's object-graph read of one authored 210-byte fixture — classes never instantiated per the producer's own limitation; NIB/dylib operations unrecorded) | — | — | unchanged (ADJ-06 unchanged) |

Capabilities: none added (the F4 mapping and v2 instrument are revisions of
existing registered ground; the supersession note above updates the r80
orphan-sweep row's current instrument, first-working round unchanged).

Sources: rows 456 → 458 (+S457 the artifact-graph capability surface
[own-work, tier A], +S458 the producer record [own-work, tier A]; both opened
this round; C1 is the sourced claim; C2 rests on the r80 closure's routed
rule, S456 lineage). Census: round start sanctioned exit 0, 31 W (21 W01 +
10 W04, same disclosed classes; literal exit 2, disclosed lineage); round end
receipts `reports/round-81/census-after.log`. Mistakes mined (full table
`corpus/lessons/round-81.md`): the generator's stale self-check constants
(caught by the Q06 derive-then-assert discipline), the oracle's None-vs-int
reference sort (caught by the first real run), the r80 corpus-drift class
(carry-in, root-caused first-hand), a recon corpus-isolation error
(self-caught by a tokenizer-vs-sweep count cross-check), a census
receipt prefix defect (self-caught before commit; disclosed in the receipt), and a
post-commit LOG.md CRLF whole-file rewrite (caught by the mandated diff check; corrected by the round's correction commit, append-only restored).

**planned:** next round — coverage: the artifact-graph family's two unrecorded
operations (`decode_interface_builder` on an authored compiled-NIB-shaped
fixture, or `trace_dylib-resolution` on a Mach-O-shaped one) are one bounded
round each, same shape as F2/F3/F4; calibration: criterion R extension or
criterion N's attribution pair (both stay routed). F android moves only if the
caller-supplied `REA_JADX_MCP_JAR` appears; K stays blocked until the operator
rules on the filed L0.

Routed forward: criterion R extension; criterion N attribution pair; criterion
C repair (§9); the class question (v2 lands as a capability supersession note,
not a registry row); F android gate; K L0; census literal form (operator-side,
lineage L0 landed r79); the six real sweep absents keep their recorded
dispositions (ScoutAmp misroot, round-73/votes, w1.ready, .pyc,
measurements.json, controls/A-H).

## Round 82 (hyaku run 21) — a second artifact-graph operation moves through a real dylib-resolution producer run (criterion A1, `trace_dylib_resolution`); the orphan sweep learns the counting-command fidelity class (v3 supersession)

Base `33764dd29aaab69457327618e2a2c14900d5b634`. Freeze
`ad74dc88342a7f3b314c786ad0bbea379df8af15` (claims + sha-pinned instruments +
red-befores + preprobe receipt). Landing
`9201d97a92ea6b355e8c9d713d2c3b0c8aa7a13b` (fixture + producer record +
S459–S461); final measured revision = the adjudication commit carrying this
section. Two claims, distinct axes, causally separable, neither exploratory.
Carry-in dispositions (r81 non-author closure, addressed first, all
status-neutral): the red-grep count reproduced first-hand (pasted trailing-space
pattern = 1, corrected = 2, prefixes 1 + 1 — `countgrep-red.log`) and closed
inside v3 as registered counting commands; the correction numstat convention
reproduced (raw `10 0` = 9 content lines + 1 blank separator —
`carryin-numstat.log`), correction appended in LOG; the basis-line comparison
rule adopted (every sweep receipt carries its `SWEEP_CORPUS` line). Full gate,
receipts and mistake mining: `corpus/lessons/round-82.md`.

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| coverage — artifact-graph operation record depth (criterion A1, registered this round; operation-record split from the family-presence criteria) | **1/3 (3.33) → 2/3 (6.67)** on the registered instrument; the family-level instrument holds: `F4_COVERAGE=10/11 score=9.09` unchanged | before: `PYTHONUTF8=1 python -B reports/round-82/ag_probe.py <base-archive>/corpus` → `ag-red.log` (1/3, only `inspect_keyed_archive=round-81`); after: same over the landing archive → `ag-after.log` (2/3 with `trace_dylib_resolution=round-82`) | `33764dd` (red) → `9201d97` (green) | **improved, C1 met** — one real `rea trace-dylib-resolution corpus/fixtures/macho-r82/image/main.dylib --format json` run (rea 6.8.0, built-in `rea-artifact-graph` provider) on the authored inert two-image Mach-O fixture (304 + 80 bytes, generator 15/15 self-check derives every byte-derived oracle fact from the built bytes — install names, rpaths, load list, 8-alignment, tree layout; regen byte-identical; shas `5f56d14d…9507d` / `bda3d4ff…bcf07`); oracle `ORACLE OK (47/47 checks)` = 37 BYTE + 10 pre-registered Q07 HYP checks over the archive bytes (`corpus/live/runs/round-82/`, Evidence `ev_851a7405…d514a`). Honest boundary: A1 is a NEW instrument (denominator disclosure pre-run); the moved quantity is the operation record, not family presence; `decode_interface_builder` stays unrecorded — A1's honest exception is 2/3, not 3/3 |
| calibration — standing cited-evidence orphan sweep, v3 supersession (capability improvement, not a new capability) | red (`sweep-v2-selftest-red.log`: committed v2 over the base archive — selftest exit 0, 7 legs, ZERO count-fidelity legs (`grep -c "SWEEP_SELFTEST_COUNT\|SWEEP_PARSER"` = 0); `countgrep-red.log`: pasted trailing-space pattern = 1 vs corrected = 2 over committed r81 bytes) → green: `SWEEP_SELFTEST=pass` 9/9 legs exit 0 (v2's seven + `SWEEP_SELFTEST_COUNT_FIDELITY=ok (truth=2, A=1, B=1)` + `SWEEP_SELFTEST_COUNTCMD_MUTANT_FLAGGED=ok (mutant=1 truth=2)`; hermetic archive run, `sweep3-selftest-after.log`); frozen sed mutant dies exit 1 with the attributed last line `selftest: counting-command fidelity drifted (trailing-space class)` (`sweep3-mutant-kill.log`); real tree FULL output + `SWEEP_PARSER_GREP_A=0 _B=0 _AB=0` (each reproduced by its registered grep over the receipt bytes) + `SWEEP_CORPUS fleet-reports=22 lessons=44` + `CITED=369 COMMITTED=357 LANDABLE_ORPHANS=0 ABSENT=12` exit 0 (`sweep3-real-after.log`) | `PYTHONUTF8=1 python -B reports/round-82/orphan_sweep3.py --selftest` / `… --lane <lane-dir> --fleet <fleet-root> [--format full\|summary]`; registered receipt greps: `grep -cE '^SWEEP absent corpus/knowledge/round-68-apk-axml-byte-evidence' <receipt>`, `grep -cE '^SWEEP absent corpus/lessons/round-64' <receipt>`, corrected alternation `^SWEEP absent (corpus/knowledge/round-68-apk-axml-byte-evidence\.md:57\|corpus/lessons/round-64)` — NO trailing space | `33764dd` (red) → adjudication | **improved, C2 met** — `reports/round-82/orphan_sweep3.py` (sha `af64b4c5…b8748`; v2 blob unchanged `30aa3527…93eb6` re-verified over the landing archive): the r81 closure's routed counting-command class closes inside the standing instrument (change 5: registered corrected greps + mutation-checked fidelity vector); the `SWEEP_CORPUS` count basis and full-output receipt rules stand (v2 changes 3–4); declared exits 0/1/64 unchanged; counts remain per-revision-corpus (basis lines cited first). Supersession note for the capabilities table: the `cited-evidence orphan sweep` row's current instrument is v3 (this round's receipts), first-working round unchanged (r80) |
| coverage — knowledge-map ground K | 8/15 (5.3) → 8/15; C05 uncovered, C10 partial, C15 uncovered | not re-run — no README/knowledge byte changed (no-harm diff below); operator-blocked route (r74 L0 unanswered, re-read this round) | same | unchanged (blocked route, not attempted) |
| coverage — selected-family record presence F4 | 10/11 (9.09) → 10/11; android hard-gated (`REA_JADX_MCP_JAR` UNSET, no jadx on PATH, re-probed 2026-11-01 — S448 stands); macho/signature providers `unsupported_host` re-probed (S453) | `PYTHONUTF8=1 python -B reports/round-81/f_probe4.py <landing-archive>/corpus` (`ag-after.log` tail) | same | unchanged hold (the r82 record is operation-level; the family was already present) |
| freshness — stored-assertion proxy | 18/18 → 18/18 (seed 12 + readiness 6; knowledge files untouched) | `grep -cE '^\| [FK][0-9]+ .*\| (holds\|STALE)' corpus/knowledge/seed.md corpus/knowledge/2026-10-12-rea-readiness-checklist.md` (`noharm-diff.txt` tail) | same | unchanged hold |
| calibration — C2–C8 receipt guards, exit-2 gate, runnability; C/R/G/N criteria bytes | untouched; no verifier, gate, README or knowledge byte changed; v1/v2 criterion instruments blob/sha-identical (v2 `30aa3527…93eb6` re-verified; f_probe4 unchanged in range) | no-harm diff receipt `reports/round-82/noharm-diff.txt` (protected paths empty on `ad74dc8..9201d97`; 10 files changed, 554 insertions, 0 deletions — additions only) | same | unchanged (no harm observed) |
| separability | C1-only tree (base + fixture/record/ag_probe, no orphan_sweep3): A1 2/3 + oracle OK 47/47, instrument ABSENT (`c1-only.log`); C2-only tree (base + orphan_sweep3, no fixture/record/ag_probe): selftest pass exit 0, ag_probe ABSENT (`c2-only.log`) | see the two logs | same | claims separable as frozen |
| depth / operability / adjacency | no claim; no engine readiness claimed (Q05/Q10: the record demonstrates the built-in provider's dyld load-path read of one authored inert two-image tree; nothing executed; the producer's `coverage: partial` semantics recorded as observed, not explained) | — | — | unchanged (ADJ-06 unchanged) |

Capabilities: none added (A1 and v3 are new/superseding measurement
instruments over existing registered ground; the trace route is REA's
built-in provider, exercised once — not a new analysis family owned by this
lane).

Sources: rows 458 → 461 (+S459 the dylib-resolution capability surface
[own-work, tier A], +S460 the producer record [own-work, tier A], +S461 the
r81 closure's routed repin rule [own-work, tier A]; all opened this round; C1
is sourced by S459+S460, C2 by S461). Census: round start sanctioned exit 0,
31 W (21 W01 + 10 W04, same disclosed classes; literal exit 2, disclosed
r74–r81 lineage); round end receipts `reports/round-82/census-after.log`
(landing-archive census fires the expected E11 ×3 for S459–S461 used-by the
lesson preceding it, resolved by this adjudication commit; worktree census
exit 0, zero E). Mistakes mined (full table `corpus/lessons/round-82.md`):
the LC_RPATH header-width draft error (caught by the builder's tiling assert),
the parser's cmdsize%8 constraint (caught by the M33 pre-probe), the
`\|`-in-double-quotes literal-pipe counting trap (self-caught on my own first
carry-in reproduction — 0 agreeing with neither 2 nor 1), and the CRLF
byte-check applied at freeze time (pins verified against `git show` blobs).

**planned:** next round — coverage: the artifact-graph family's third
operation (`decode_interface_builder`) needs an authored inert `.app` bundle
fixture (a larger, directory-shaped fixture than r79–r82's file-shaped ones —
one bounded round if attempted), or A1 holds at 2/3; calibration: criterion
R full extension to the legacy receipt-quoting rows, or criterion N's
mutation-killed attribution pair (both stay routed); criterion C repair stays
§9-ruled-out. F android moves only if the caller-supplied `REA_JADX_MCP_JAR`
appears; K stays blocked until the operator rules on the filed L0.

Routed forward: criterion R full extension; criterion N attribution pair;
criterion C repair (§9); the class question (v3 lands as a capability
supersession note, not a registry row); F android gate; K L0; census literal
form (operator-side, lineage L0 landed r79); the six real sweep absents keep
their recorded dispositions (ScoutAmp misroot, round-73/votes, w1.ready,
.pyc, measurements.json, controls/A-H).
## Round 83 (hyaku run 22) — the artifact-graph family's third operation moves through a real interface-builder producer run (criterion A1 completion, `decode_interface_builder`); the orphan sweep learns the bare-filename citation class (v4 supersession)

Base `60693f2ce6b086ea3f0ee84fe27a8f8a13d46f46` (r82 tip + non-author
spot-check). Carry-in landing = the same `60693f2` (the r82 non-author
closure's first obligation, addressed FIRST: the seven cited green
receipts landed via treecommit explicit paths, the b1e0c60e class; the
standing v3 sweep receipted both states, LANDABLE_ORPHANS=2 exit 1 → 0
exit 0, `.ufo/waves/round-83/sweep-{pre,post}-landing.log`). Freeze
`28e8c290235f2e6d588a9b81538b61ae50e533b7` (claims + sha-pinned v4
instrument + red-befores + preprobe receipt). Landing
`75298d427d97c5668753969fecf54d98630735b7` (fixture + producer record +
S462–S465); final measured revision = the adjudication commit carrying
this section. Two claims, distinct axes, causally separable, neither
exploratory. Full gate, receipts and mistake mining:
`corpus/lessons/round-83.md`.

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| coverage — artifact-graph operation record depth (criterion A1, registered r82, instrument unchanged) | **2/3 (6.67) → 3/3 (10.00)**; the family-level instrument holds: `F4_COVERAGE=10/11 score=9.09` unchanged | before: `PYTHONUTF8=1 python -B reports/round-82/ag_probe.py <base-archive>/corpus` → `ag-red.log` (2/3, `decode_interface_builder=unrecorded`); after: same over the landing archive → `ag-after.log` (3/3 with `decode_interface_builder=round-83`) | `60693f2` (red) → `75298d4` (green) | **improved, C1 met** — one real `rea decode-interface-builder corpus/fixtures/app-r83/R83Sample.app --format json` run (rea 6.8.0, built-in `rea-artifact-graph` provider) on the authored inert two-document `.app` bundle (root-layout Info.plist 313 + typed-NIBArchive documents 213 + 79 bytes; generator 18/18 SELFCHECK re-parses the built bytes and re-derives every oracle-checked fact — table offsets, terminator-bit varints, class names, per-object typed values; regen byte-identical across three scratch builds); oracle `ORACLE OK (44/44 checks)` = 26 BYTE + 18 pre-registered Q07 HYP checks over the archive bytes (`corpus/live/runs/round-83/`, Evidence `ev_260481425d1a43fbbc0327c2033aafda8d7a51599c520a74b9985c3c550610f8`). Honest boundary: A1 saturates at 3/3 (saturation line 7.0); the moved quantity is the operation record, not family presence; android stays hard-gated — F4's honest exception is 10/11, not 11/11 |
| calibration — standing cited-evidence orphan sweep, v4 supersession (capability improvement, not a new capability) | red (`v3-prelanding-recon.log`: committed v3 over the MINIMAL pre-landing reconstruction — fresh repo, HEAD=`c153e448` via fetch+update-ref, no checkout, disk = exactly the seven worktree receipts — exit 1, `LANDABLE_ORPHANS=2`, while SEVEN landable cited receipts exist on disk; five were cited by BARE filename, invisible to the lane-domain filter) → green: `SWEEP_SELFTEST=pass` 13/13 legs exit 0 (v3's nine + `SWEEP_SELFTEST_BARE_ORPHAN_FLAGGED` / `BARE_COMMITTED` / `BARE_UNMATCHED_SKIPPED` / `BARE_MUTANT_FLAGGED`; hermetic archive run, `sweep4-selftest-after.log`); frozen sed mutant dies exit 1 attributed (`selftest: bare-filename classification drifted (bare-token class)`, `sweep4-mutant-kill-after.log`, exactly one changed line 87); reconstruction resolved: v4 over the same tree with HEAD = the carry-in landing → `LANDABLE_ORPHANS=0` exit 0 (`v4-postlanding-recon.log`); real tree FULL output + `SWEEP_PARSER_GREP_A=0 _B=0 _AB=0` (each reproduced by its registered grep over the receipt bytes) + `SWEEP_BARE_TOKENS matched=291 unmatched_skipped=1366` + `SWEEP_CORPUS fleet-reports=23 lessons=46` + `CITED=677 COMMITTED=665 LANDABLE_ORPHANS=0 ABSENT=12` exit 0 (`sweep4-real-after.log`) | `PYTHONUTF8=1 python -B reports/round-83/orphan_sweep4.py --selftest` / `… --lane <lane-dir> --fleet <fleet-root> [--format full\|summary]`; bare-token normalization resolves each slash-less cited filename against the basename index of HEAD ∪ working tree; any never-committed candidate flags ORPHAN (conservative ambiguity: one committed match never launders a second uncommitted match under the same basename) | `60693f2`/`c153e448` (red) → adjudication | **improved, C2 met** — `reports/round-83/orphan_sweep4.py` (sha `f520f8d6…9701`; v3 blob unchanged `af64b4c5…b8748` re-verified over the landing archive): the class the r83 carry-in demonstrated live (five of seven cited receipts invisible to v3) closes inside the standing instrument (change 6: bare-filename receipt normalization + four mutation-checked vectors); the `SWEEP_CORPUS` count basis, full-output receipts and registered counting commands stand (v2 changes 3–4, v3 change 5); declared exits 0/1/64 unchanged; counts remain per-revision-corpus (basis lines cited first — this round's receipt discloses the corpus movements vs r82's: fleet-reports +1 = `round-82/revenger.md` landed 13:51 after the r82 receipt 13:28; lessons +2 = the live worktree carries the two r82 lesson files the r82 landing-archive extraction predated). Supersession note for the capabilities table: the `cited-evidence orphan sweep` row's current instrument is v4 (this round's receipts), first-working round unchanged (r80) |
| coverage — knowledge-map ground K | 8/15 (5.3) → 8/15; C05 uncovered, C10 partial, C15 uncovered | not re-run — no README/knowledge byte changed (no-harm diff below); operator-blocked route (r74 L0 unanswered, re-read this round) | same | unchanged (blocked route, not attempted) |
| coverage — selected-family record presence F4 | 10/11 (9.09) → 10/11; android hard-gated (`REA_JADX_MCP_JAR` UNSET, no jadx on PATH, re-probed 2026-11-01 — S448 stands); macho/signature providers `unsupported_host` re-probed | `PYTHONUTF8=1 python -B reports/round-81/f_probe4.py <landing-archive>/corpus` (`ag-after.log` tail) | same | unchanged hold (the r83 record is operation-level; the family was already present) |
| freshness — stored-assertion proxy | 18/18 → 18/18 (seed 12 + readiness 6; knowledge files untouched) | `grep -cE '^\| [FK][0-9]+ .*\| (holds\|STALE)' corpus/knowledge/seed.md corpus/knowledge/2026-10-12-rea-readiness-checklist.md` (`noharm-diff.txt` tail) | same | unchanged hold |
| calibration — C2–C8 receipt guards, exit-2 gate, runnability; C/R/G/N criteria bytes | untouched; no verifier, gate, README or knowledge byte changed; v1/v2/v3 criterion instruments blob/sha-identical (v3 `af64b4c5…b8748` re-verified over the landing archive; f_probe4 and ag_probe absent from the landing range) | no-harm diff receipt `reports/round-83/noharm-diff.txt` (protected paths empty on `28e8c29..75298d4`; 11 files changed, 757 insertions, 0 deletions — additions only) | same | unchanged (no harm observed) |
| separability | C1-only tree (pre-freeze base `60693f2` + fixture/record, no v4): A1 3/3 + oracle OK 44/44, instrument ABSENT (`c1-only.log`); C2-only tree (base + v4, no fixture/record): selftest pass exit 0, fixture ABSENT, A1 holds 2/3 (`c2-only.log`) | see the two logs | same | claims separable as frozen |
| depth / operability / adjacency | no claim; no engine readiness claimed (Q05/Q10: the record demonstrates the built-in provider's compiled-NIB decode of one authored inert two-document bundle; nothing executed; the producer's `hierarchy: unsupported` facet semantics recorded as observed, not explained) | — | — | unchanged (ADJ-06 unchanged) |

Capabilities: none added (A1 completed on the r82 instrument unchanged;
v4 is a superseding measurement instrument over the existing registered
capability; the decode route is REA's built-in provider, exercised once
— not a new analysis family owned by this lane).

Sources: rows 461 → 465 (+S462 the interface-builder capability surface
[own-work, tier A], +S463 the installed parser source [own-work, tier
A: the lane's own installed tool source, read to derive the fixture
layout], +S464 the producer record [own-work, tier A], +S465 the
carry-in class evidence [own-work, tier A]; all opened this round; C1
is sourced by S462+S463+S464, C2 by S465). Census: round start
sanctioned exit 0, 31 W (21 W01 + 10 W04, same disclosed classes;
literal exit 2, disclosed r74–r82 lineage); round end receipts
`reports/round-83/census-after.log` (landing-archive census fires the
expected E11 ×4 for S462–S465 used-by the lesson preceding it, resolved
by this adjudication commit; worktree census exit 0, zero E). Mistakes
mined (full table `corpus/lessons/round-83.md`): the LEB128 varint
drafting error (caught by the M33 pre-probe: "NIBArchive variable
integer is too long" — the terminator-bit encoding is the inverse of
LEB128), check-from-intent (the SELFCHECK's own varint leg + a
hardcoded 211-byte size were wrong while the bytes were right; the
derived sizes are 213/79), count-from-intent twice in one round (282→
313 plist bytes in the claims draft; 7507→9012 stdout bytes in the
LEDGER draft — both caught by measure-before-write), the CRLF-mutant
class (the scratch v4 was CRLF so the sed mutant silently normalized
line endings; normalized to LF first, mutant regenerated from the
committed bytes — exactly one changed line), the separability-tree base
error (first c1-only built from the freeze, which already contains v4;
rebuilt from the pre-freeze base), and the killed-run census receipt
artifact (backgrounded at a 120 s timeout → false exit 1 with a clean
"ok" output; re-run foreground, exit 0).

**planned:** next round — coverage: A1 is saturated (3/3); F android
moves only if the caller-supplied `REA_JADX_MCP_JAR` appears (F4's
honest exception stays 10/11); K stays blocked until the operator rules
on the filed L0; calibration: criterion R full extension to the legacy
receipt-quoting rows, or criterion N's mutation-killed attribution pair
(both stay routed); a possible sweep v5 corpus expansion (LOG.md as a
citation corpus) needs its own falsifiable red/green — routed, not
declared.

Routed forward: criterion R full extension; criterion N attribution
pair; criterion C repair (§9); the class question (v4 lands as a
capability supersession note, not a registry row); F android gate; K
L0; census literal form + census shell-timeout note (operator-side,
lineage L0 landed r79); the LOG.md corpus blind spot (v4 covers fleet
reports + lessons; LOG.md is still not scanned); the six real sweep
absents keep their recorded dispositions (ScoutAmp misroot,
round-73/votes, w1.ready, .pyc, measurements.json, controls/A-H).

## Round 84 (hyaku run 23) — the artifact-graph family's archive-side pair moves through real inventory/extraction producer records (criterion A1v2, the full available set); the orphan sweep learns the unmatched-bare-citation and LOG-corpus classes (v5 supersession)

Carry-in first (r83 non-author closure, three routed status-neutral
defects, all addressed before claim work — carry-in landing
`67e1470e5b2492df7b86632c5b3bafabfdd3e023`): (1)
`reports/round-83/v4-postlanding-recon.log` regenerated from committed
bytes only and landed (recon HEAD=`60693f2` via fetch+update-ref, disk =
the seven r82 receipts byte-verified 7/7,
`.ufo/waves/round-84/carryin-byteverify.log`; `LANDABLE_ORPHANS=0`
exit 0 — the load-bearing values the five citing surfaces carry
reproduce; full provenance + basis-movement header in the receipt);
(2) `reports/round-84/corrections.md` correction 1 — the five
`f520f8d6…9701` abbreviated-sha drift sites named (report ×1, lesson
×2, SCORECARD, LOG); the claims.md full sha
`f520f8d69875d1ca83eb8daeddbffecb5f471bf5f5e6aba43bd97029fc2ea701`
governs; append-only, no in-place rewrite; (3) corrections.md
correction 2 — the `census-round-start-sanctioned2.log` pointer
resolved three ways (the committed killed-run output body, the r83
verifier's independent re-run, this round's exit-0 re-run receipt
`.ufo/waves/round-84/census-round-start-sanctioned.log`).

| axis / criterion | before → after score | evidence / command | measured commits | last change |
|---|---|---|---|---|
| coverage — artifact-graph operation record depth, full available set (criterion A1v2, registered this round; supersedes the r82 A1 mapping as the criterion's counting instrument; the r82 instrument stays frozen) | **3/5 (6.00) → 5/5 (10.00)** on the registered instrument; frozen instruments hold: r82 `A1_RECORDED=3/3 (10.00)`, r81 `F4_COVERAGE=10/11 (9.09)` unchanged (the pair is operation-level; the family and the triple were already present/recorded) | before: `PYTHONUTF8=1 python -B reports/round-84/ag_probe2.py <base-archive 54a36bca>/corpus` → `ag2-red.log` / `ag2-red-v21.log` (3/5, `extract_artifact` + `inspect_artifact` unrecorded); after: same over the landing archive `8e21e8f2` → `ag2-after.log` (5/5 with both recorded; oracles re-run over archive bytes `ORACLE OK (36/36)` + `ORACLE OK (31/31)`; record stdout shas match the receipt pins; regen byte-identical from the archive generator) | `54a36bca` (red) → `8e21e8f2` (green) | **improved, C1 met** — two real producer records on the provider's archive-side pair (`rea inspect-artifact` Evidence `ev_753cfca9…138ba` 36/36; `rea extract-artifact` Evidence `ev_07e34a94…77467` 31/31; both exit 0, stderr 0 bytes) on the authored inert 508-byte three-entry ZIP_STORED fixture (`corpus/fixtures/arc-r84/`, generator 17/17 SELFCHECK re-derives every checked fact from the built bytes, no byte-size constants, regen byte-identical; truth.json Q07 hypotheses frozen pre-run). Denominator disclosure (pre-run): the provider declares FIVE available operations (S466); the r82 registration counted the no-effects triple only; `inspect_asset_catalog` excluded (`available: false` unsupported_host). Instrument erratum (pre-after-run): the freeze-time v2.0 scan shape could never see the landed `runs/round-84/<operation>/` layout — exposed by the c1-only dry-run printing 3/5 against landed records; v2.1 (rglob by name) re-pinned `f9772ab1…1990`, red re-run unchanged, erratum appended to claims.md; mined. Separability: `c1-only.log` (A1v2 5/5 + oracles OK with v5 ABSENT) / `c2-only.log` (selftest 18 legs pass with fixture/records/ag_probe2 ABSENT) |
| coverage — selected-family record presence F4 | 10/11 (9.09) → 10/11; android hard-gated (`REA_JADX_MCP_JAR` UNSET, no jadx on PATH, re-probed 2026-11-02 — S448 stands); the pair does not move F4 (the archives family was already present) | `PYTHONUTF8=1 python -B reports/round-81/f_probe4.py <landing-archive>/corpus` (`ag2-after.log`) | same | unchanged hold |
| calibration — standing cited-evidence orphan sweep, v5 supersession (capability improvement, not a new capability) | no criterion score moves; the moved quantity is citation visibility: red (`v4-invisible-red.log`: v4 over the pre-carry-in tree — ZERO instrument rows name the bare-cited `v4-postlanding-recon.log`; `SWEEP_BARE_TOKENS matched=302 unmatched_skipped=1408`) → recorded (`v5-red-unmatched-absent.log`: same tree, row `SWEEP absent v4-postlanding-recon.log` note bare-token unmatched, `unmatched_recorded_absent=47`, `SWEEP_CORPUS fleet-reports=24 lessons=48 log=1`, `CITED=987` vs v4's 705) → resolved (`sweep5-real-after.log`: the token bare-token-normalized committed, no absent row names it; the receipt's three LANDABLE_ORPHANS rows are the conservative-ambiguity rule firing on this round's own then-uncommitted same-basename adjudication receipts, resolved by the adjudication commit — post-run note in the receipt) | `PYTHONUTF8=1 python -B reports/round-84/orphan_sweep5.py --selftest` (18 legs + pass, exit 0, `sweep5-selftest-after.log` from the committed blob) / `… --lane <lane-dir> --fleet <fleet-root> [--format full|summary]`; v5 change 7: an unmatched extension-bearing bare token is RECORDED as an absent row (no `..`, not all digits+dots, tail extension; disclosed noise: dotted JSON field paths; absent never gates — exit codes 0/1/64 unchanged); v5 change 8: LOG.md joins the citation corpus (SWEEP_CORPUS gains log=); three mutation-checked switches with frozen one-substitution sed recipes, all three die exit 1 attributed from the committed blob (`sweep5-mutant-kill-after.log`) | `67e1470`/`45c8b42` (red) → adjudication | **improved, C2 met** — `reports/round-84/orphan_sweep5.py` (sha `d9a7ba17…46cb`; v4 blob unchanged `f520f8d6…c2ea701` — the FULL sha per corrections.md): the two gaps the r83 closure routed (a bare-cited token matching nothing was skipped invisible; LOG.md was a standing corpus blind spot) close inside the standing instrument. Counts remain per-revision-corpus (basis lines cited first — the red receipts ran over the pre-carry-in tree, the green receipt over the pre-adjudication-text worktree; movements disclosed in each receipt header). The recorded absent rows carry their disposition classes in the round lesson |
| freshness — stored-assertion proxy | 18/18 → 18/18 (seed 12 + readiness 6; knowledge files untouched) | `grep -cE '^\| [FK][0-9]+ .*\| (holds\|STALE)' corpus/knowledge/seed.md corpus/knowledge/2026-10-12-rea-readiness-checklist.md` (`noharm-diff.txt` tail) | same | unchanged hold |
| calibration — C2–C8 receipt guards, exit-2 gate, runnability; C/R/G/N criterion bytes | untouched; no verifier, gate, README or knowledge byte changed; v1–v4 sweep instruments + ag_probe + f_probe4 absent from the landing range (blob shas re-verified: v4 `f520f8d6…c2ea701` full) | no-harm diff receipt `reports/round-84/noharm-diff.txt` (protected paths empty on `45c8b42..8e21e8f2`; 15 files, 704 insertions, 0 deletions — additions only) | same | unchanged (no harm observed) |
| separability | C1-only tree (pre-freeze base `67e1470` + fixture/records/ag_probe2-v2.1, no v5): A1v2 5/5 + oracles OK 36/36 + 31/31, v5 ABSENT (`c1-only.log`); C2-only tree (base + v5 only): selftest pass exit 0, fixture/records/ag_probe2 ABSENT (`c2-only.log`) | see the two logs | same | claims separable as frozen |
| depth / operability / adjacency | no claim; no engine readiness claimed (Q05/Q10: the records demonstrate the built-in provider's zip inventory + regular-contents extraction of one authored inert archive; extraction output under the host temp area, nothing executed, nothing written inside the lane repo; DMG/PKG/nested-container surfaces unclaimed per the provider's own limitations) | — | — | unchanged (ADJ-06 unchanged) |

Capabilities: none added (A1v2 is a registered mapping revision over
the r82 criterion instrument; v5 is a superseding measurement
instrument over the existing registered capability; the inventory/
extract route is REA's built-in provider, exercised once — not a new
analysis family owned by this lane).

Sources: rows 465 → 468 (+S466 the A1v2 provider surface [own-work,
tier A], +S467 the two producer records + fixture [own-work, tier A],
+S468 the unmatched-bare-citation class evidence [own-work, tier A];
all opened this round; C1 is sourced by S466+S467, C2 by S468; all
appended inside the Registry after S465; NF checked mid-flight — S468's
quoted receipt row initially carried a literal pipe, fixed before the
landing, the r83 S465 class). Census: round start sanctioned exit 0
(21 W01 + 10 W04, same disclosed classes; first attempt hit the shell's
own 120 s default timeout and was re-run foreground with an explicit
generous timeout — the r83 mined class recurring, disclosed in the
lesson; literal exit 2, disclosed lineage); round end receipts
`reports/round-84/census-after.log`. Mistakes mined (full table
`corpus/lessons/round-84.md`): the record-layout vs scan-shape
instrument defect (caught by the c1-only separability dry-run before
any after-run receipt), the treecommit directory-args silent no-op
(caught by the mandated post-commit diff check — the first landing
commit carried only SOURCES.md), the census 120 s default-timeout
recurrence, the S468 literal-pipe NF defect (r83 S465 class, caught
mid-flight), and the count-from-intent placeholder in the first claims
draft (caught by measure-before-write before the freeze).

**planned:** next round — coverage: A1v2 is saturated (5/5); F android
moves only if the caller-supplied `REA_JADX_MCP_JAR` appears (F4's
honest exception stays 10/11); K stays blocked until the operator rules
on the filed L0; calibration: criterion R full extension to the legacy
receipt-quoting rows, or criterion N's mutation-killed attribution pair
(both stay routed); candidate sweep v6 vectors: the LOG-corpus
citation-sites accounting (per-source rows) and a fleet-side
basename resolution for absent-fleet bare tokens — each needs its own
falsifiable red/green; routed, not declared.

Routed forward: criterion R full extension; criterion N attribution
pair; criterion C repair (§9); the class question (v5 lands as a
capability supersession note, not a registry row); F android gate; K
L0; census literal form (operator-side, lineage L0 landed r79); the
v5 recorded-absent rows' standing dispositions (field-path noise,
fleet-root bare names, historical unresolvable pointers — dispositioned
in the round lesson; a standing disposition ledger is operator-side if
wanted); the six real sweep absents keep their recorded dispositions
(ScoutAmp misroot, round-73/votes, w1.ready, .pyc, measurements.json,
controls/A-H).

## Round 85 (hyaku run 23) — the managed provider's full available set moves through three real oracle-checked producer records (criterion M, the r76 oracle-gate gap exposed); the orphan sweep learns the fleet-root bare-token class (v6 supersession)

Carry-in first (r84 non-author closure, three routed status-neutral
defects, all addressed before claim work — carry-in landings `ac91c05`
EMPTY (treecommit absolute-path-args class, mined) → `9cadaed` →
`acfb3b4`): (1) D1 wording precision —
`reports/round-85/corrections.md` correction 1 (the bare-class rule:
zero holds of the bare-token class only; the PATH-form twin row exists
at `v4-invisible-red.log:637`; claims.md §C2 wording governs; no
in-place rewrite of any r84 surface); (2) D2 — the post-adjudication
sweep absolute landed as a committed file
(`.ufo/waves/round-85/postadjudication-sweep.log`, run from the
committed v5 blob over tip+fleet trees: `CITED=1024 COMMITTED=964
LANDABLE_ORPHANS=0 ABSENT=60` exit 0, basis `SWEEP_CORPUS
fleet-reports=25 lessons=50 log=1` cited first); (3) D3 — dual
round-start census receipts (sanctioned exit 0, 21 W01 + 10 W04, zero
E; literal exit 2, disclosed lineage), routed around.

| axis / criterion | before → after score | evidence / command | measured commits | last change |
|---|---|---|---|---|
| coverage — managed-operation record depth, full available set (criterion M, registered this round; instrument `reports/round-85/mg_probe.py`, scan shape born v2.1 — rglob `inspection.json` by name) | **0/3 (0.00) → 3/3 (10.00)** on the registered instrument; frozen holds: r84 `A1V2_RECORDED=5/5 (10.00)`, r82 `A1_RECORDED=3/3 (10.00)`, r81 `F4_COVERAGE=10/11 (9.09)` unchanged over the same landing archive | before: `PYTHONUTF8=1 python -B reports/round-85/mg_probe.py <base-archive 8cf92f0>/corpus` → `mg-red.log` (0/3, all three unrecorded — the r76 artifact record predates the oracle-receipt gate, its receipt carries no `oracle` field, disclosed pre-freeze); after: same over the landing archive `8b49e2d` → `mg-after.log` (3/3 with all three recorded; the three oracles re-run over archive bytes `ORACLE OK (20/20)` + `(47/47)` + `(39/39)`; record stdout shas match the receipt pins; regen byte-identical from the archive generator) | `8cf92f0` (red) → `8b49e2d` (green) | **improved, C1 met** — three real producer records on the provider's managed side (`rea inspect-managed-artifact` Evidence `ev_0eea92d7…f796e2` 20/20; `rea inspect-managed-members` Evidence `ev_e5d7a0b9…ae359f4` 47/47; `rea inspect-managed-native-boundaries` Evidence `ev_2115d335…063890ba` 39/39; all exit 0, stderr 0 bytes) on the authored inert 1048-byte IL-only PE/CLI fixture (`corpus/fixtures/managed-r85/`: six tables, one real 7-byte tiny-header IL body `ldstr 0x70000001; ret`, one P/Invoke ImplMap row declaring `RunNative` from a `native.dll` string that names no existing library; generator `self_check()` re-opens the built bytes and re-derives every premise — regen byte-identical across scratch and landed builds; `truth.json` Q07 hypotheses frozen pre-run; `oracle_check.py` re-derives every BYTE-check value from the fixture bytes with its own independent CLI-image parser, negative control demonstrated pre-run — one mutated field flips the members oracle to `ORACLE FAILED (46/47)`). Denominator disclosure (pre-run): the provider declares exactly three available operations (S469 — no unsupported group, unlike artifact-graph's `inspect_asset_catalog`). Four fixture-authoring defects + three oracle-parser bugs caught by the preprobe cross-check BEFORE any committed run; the ImplMap coded-index error (row 1 with an IL body vs the P/Invoke row 2) is mined. Honest boundary: M saturates at 3/3 (saturation line 7.0); the moved quantity is the oracle-checked operation record, not family presence (F4) and not the artifact-graph criteria (which hold); nothing is loaded or executed (Q10 notes in all three LEDGERs) |
| coverage — selected-family record presence F4 | 10/11 (9.09) → 10/11; android hard-gated (`REA_JADX_MCP_JAR` UNSET, no jadx on PATH, re-probed 2026-11-02 — S448 stands); the managed records do not move F4 (the managed family was already present) | `PYTHONUTF8=1 python -B reports/round-81/f_probe4.py <landing-archive>/corpus` | grep F4_COVERAGE (`mg-after.log`) | `8cf92f0` (red) → `8b49e2d` (green) | unchanged hold |
| calibration — standing cited-evidence orphan sweep, v6 supersession (capability improvement, not a new capability) | no criterion score moves; the moved quantity is citation attribution: red pair over the SAME pre-landing tree (`v5-full-prelanding.log`: 48 unmatched recorded absent rows, `SWEEP absent MISSION.md \| bare-token unmatched: no file named MISSION.md under HEAD or the working tree` → `v6-full-prelanding.log`: `unmatched_recorded_absent=26 fleet_resolved=22`, `SWEEP absent-fleet MISSION.md \| bare-token normalized: fleet/MISSION.md`, PROTOCOL.md disclosing two fleet matches; gating values identical CITED=1024 COMMITTED=964 LANDABLE_ORPHANS=0 ABSENT=60) → resolved: real-tree pair over the committed adjudication tip from the committed blobs (`sweep6-real-after.log`: v5 48 absent rows vs v6 26+22, gating identical 1025/965/0/60, both exit 0, LANDABLE_ORPHANS=0) | `PYTHONUTF8=1 python -B reports/round-85/orphan_sweep6.py --selftest` (21 legs + pass, exit 0, `sweep6-selftest-after.log` from the committed blob) / `… --lane <lane-dir> --fleet <fleet-root> [--format full\|summary]`; v6 change 9: an unmatched extension-bearing bare token whose basename exists under the fleet root resolves `absent-fleet` (bare-token normalized, up to 3 matches shown, (+N more) beyond) instead of an unmatched absent row; SWEEP_BARE_TOKENS gains an always-printed fleet_resolved= term (SWEEP_CORPUS shape unchanged); absent-fleet never gates — exit codes 0/1/64 unchanged; ONE frozen sed mutant dies exit 1 attributed from the committed blob (`sweep6-mutant-kill-after.log`: `FLEET_BARE_RESOLUTION` → `selftest: fleet-bare resolution drifted (fleet-bare class)`, exactly line 115, mutated copy `8a1706ee…05a78`) | `acfb3b4`/`d27cf95` (red) → adjudication | **improved, C2 met** — `reports/round-85/orphan_sweep6.py` (sha `b2db45b0…f12b7`; v5 blob unchanged `d9a7ba17…46cb` re-verified): the r84 lesson's routed v6 candidate vector 2 ("a fleet-side basename resolution for absent-fleet bare tokens") closes inside the standing instrument. Counts remain per-revision-corpus (basis lines cited first). Supersession note for the capabilities table: the `cited-evidence orphan sweep` row's current instrument is v6 (this round's receipts), first-working round unchanged (r80) |
| freshness — stored-assertion proxy | 18/18 → 18/18 (seed 12 + readiness 6; knowledge files untouched) | `grep -cE '^\| [FK][0-9]+ .*\| (holds\|STALE)' corpus/knowledge/seed.md corpus/knowledge/2026-10-12-rea-readiness-checklist.md` (`noharm-diff.txt` tail) | same | unchanged hold |
| calibration — C2–C8 receipt guards, exit-2 gate, runnability; C/R/G/N criterion bytes | untouched; no verifier, gate, README or knowledge byte changed; v1–v5 sweep instruments + ag_probe + ag_probe2 + f_probe4 absent from the landing range (blob shas re-verified: v5 `d9a7ba17…46cb`) | no-harm diff receipt `reports/round-85/noharm-diff.txt` (protected paths empty on `d27cf95..8b49e2d`; 20 files, 1226 insertions, 0 deletions — additions only) | same | unchanged (no harm observed) |
| separability | C1-only tree (pre-freeze base `acfb3b4` + fixture/records/mg_probe, no v6): M 3/3 (10.00) + oracle OK 47/47, v5/v6 ABSENT (`c1-only.log`); C2-only tree (base + v6 only): selftest 21 legs pass exit 0, fixture/records/mg_probe ABSENT (`c2-only.log`) | see the two logs | same | claims separable as frozen |
| depth / operability / adjacency | no claim; no engine readiness claimed (Q05/Q10: the records demonstrate the built-in managed provider's static metadata decode of one authored inert image; nothing loaded, nothing executed; the provider's own limitations — nothing loaded/decompiled, P/Invoke declarations only — recorded as observed) | — | — | unchanged (ADJ-06 unchanged) |

Capabilities: none added (M is a registered coverage criterion over the
existing provider surface; v6 is a superseding measurement instrument
over the existing registered capability — the `cited-evidence orphan
sweep` row's current instrument becomes v6, first-working round
unchanged r80; the managed records exercise REA's built-in
rea-dotnet-static provider once — not a new analysis family owned by
this lane).

Sources: rows 468 → 471 (+S469 the M provider surface [own-work, tier
A], +S470 the three records + fixture [own-work, tier A], +S471 the
fleet-root bare-token class evidence [own-work, tier A]; all opened
this round; C1 is sourced by S469+S470, C2 by S471; all appended inside
the Registry directly after S468, NF=13 checked mid-flight). Census:
round start sanctioned exit 0 (21 W01 + 10 W04, zero E — receipts
landed with the carry-in; literal exit 2, disclosed r74–r84 lineage);
round end receipts `reports/round-85/census-after.log`. Mistakes mined
(full table `corpus/lessons/round-85.md`): the treecommit
absolute-path-args empty commit (ac91c05 — caught by the mandated
post-commit diff check), the treecommit absent-file-args silent skip
(9cadaed carried 2 of 4 — same check, second catch), the ImplMap
coded-index authoring error (caught by the preprobe boundaries record:
member_token 0x06000001 + native_implementation_count 2 against one
authored import), the ECMA metadata authoring triple (blob
compressed-length prefixes; #US terminal flag 0x00; table numbers
0x1A/0x1C — all caught by the producer's own preprobe outputs), the
oracle-side parser bugs (rows at t+48; GUID (n-1)*16; table names —
caught by the oracle-vs-preprobe cross-check, negative control re-run
after the fixes), and the tail-line receipt assumption (f_probe4's
score line is not its last line — caught by the end-of-content check).

**planned:** next round — coverage: M is saturated (3/3); F android
moves only if the caller-supplied `REA_JADX_MCP_JAR` appears (F4's
honest exception stays 10/11); K stays blocked until the operator rules
on the filed L0; calibration: criterion R full extension to the legacy
receipt-quoting rows, or criterion N's mutation-killed attribution pair
(both stay routed); candidate v7 sweep vector: per-source citation-sites
accounting (the r84/r85 routed vector 1) — needs its own falsifiable
red/green; routed, not declared.

Routed forward: criterion R full extension; criterion N attribution
pair; criterion C repair (§9); the class question (v6 lands as a
capability supersession note, not a registry row); F android gate; K
L0; census literal form (operator-side, lineage L0 landed r79); the v6
recorded-absent rows' standing dispositions (field-path noise,
historical unresolvable pointers — dispositioned in the round lesson);
the treecommit repo-relative + file-exists + numstat-count rule (three
variants of one class mined r78/r84/r85).

## Round 86 (hyaku run 23, fresh start) — the used-by pointer-drift class becomes machine-caught (orphan_sweep v7, per-source citation-sites accounting, the routed r84/r85 vector); SKILL.md gains the pointer-hygiene decision rows and the M42 signature

Carry-in first (r85 non-author closure, three routed status-neutral
items, addressed before claim work — correction 2 in
`reports/round-85/corrections.md`; dual round-start census receipts in
`.ufo/waves/round-86/`; SHONEN routing recorded): (1) the mg_probe.py
docstring prediction-line ruling recorded (r86 does not touch the file;
the verified sha pin stands; the standing rule: a docstring prediction
line states the registration RULE, the registered red receipt governs);
(2) the census contract-literal form exit 2 persists (r74–r86 lineage,
operator-side, dual receipts again); (3) SHONEN non-author
re-confirmation of the CURRENT SKILL.md bytes stays operator-side.

| axis / criterion | before → after score | evidence / command | measured commits | last change |
|---|---|---|---|---|
| calibration — standing cited-evidence orphan sweep, v7 supersession (capability improvement, not a new capability); change 10: SOURCES.md used-by pointer accounting (per-source citation-sites accounting, the r84 lesson's routed candidate vector 1) | no criterion score moves; the moved quantity is pointer-truth: red pair over the SAME pre-fix tree at base `d7fd9d9` (`sweep7-v6-blind-prelanding.log`: `grep -c SWEEP_SRC` over the v6 summary → 0, the class does not exist in v6; `sweep7-red-prelanding.log`: `SWEEP_SRC registry=disk rows=451 sites=499 cited=493 mismatch=6 absent=0` with six SWEEP_SRC_MISMATCH rows — S448→reports/round-77/claims.md, S449→SKILL.md, S450→reports/round-78/province_probe3.sh, S451→reports/round-79/claims.md, S453→reports/round-79/claims.md, S456→reports/round-80/orphan-before.log; identical basis `SWEEP_CORPUS fleet-reports=26 lessons=52 log=1` + gating `CITED=1050 COMMITTED=988 LANDABLE_ORPHANS=0 ABSENT=62`, both exit 0) → resolved: six rule-2 in-place used-by pointer drops (old→new logged in `reports/round-86/usedby-fix-log.txt`, each row keeps its citing pointer so `mined` stays valid) → green from the committed blob over the adjudication tip (`sweep7-real-after.log`: `SWEEP_SRC … mismatch=0 absent=0`) | `PYTHONUTF8=1 python -B reports/round-86/orphan_sweep7.py --lane <lane-dir> --fleet <fleet-root> --format summary` then `grep -E '^SWEEP_SRC '`; blind leg: `… orphan_sweep6.py … --format summary` piped to `grep -c SWEEP_SRC` → 0 at both ends; v7 sha `f955cd7d…618` frozen at `2311400`; v6 blob unchanged `b2db45b0…f12b7` re-verified; exit codes 0/1/64 unchanged (change 10 non-gating); selftest 25 legs + pass exit 0 (`sweep7-selftest-after.log` from the committed blob; 21 v6 legs + SRC_PLACEHOLDER / SRC_CITEBACK_VECTORS / SRC_ABSENT_VECTOR / SRC_MUTANT_FLAGGED); ONE frozen one-substitution sed mutant dies exit 1 attributed from the committed blob (`sweep7-mutant-kill-after.log`: `USED_BY_ACCOUNTING` → `selftest: used-by accounting drifted (used-by class)`, diff exactly line 165, mutated copy `0bfe69a0…8c3`); the census existence check passes on all six drift pointers — the class was invisible to every standing instrument by construction; preprobe cross-check per pointer `grep -cw` all six CITES=0 (`freshstart-probes.log` probes 4-5) | `2311400`/`d7fd9d9` (red) → adjudication (green) | **improved, C1 met** — supersession note for the capabilities table: the `cited-evidence orphan sweep` row's current instrument is v7 (this round's receipts), first-working round unchanged (r80) |
| depth — SKILL.md pointer-hygiene decision ground (two new §3 rule rows + the census/sweep division-of-labor row + the M42 named error signature) | reds over base bytes (`skill-red-greps.log`: `grep -cE '^\| M[0-9]+ \|' SKILL.md` → 9 (M33–M41, no pointer-drift signature); `grep -c 'cite-back' SKILL.md` → 0; `grep -c 'used-by' SKILL.md` → 4) → greens over the landing archive (`skill-green-greps.log`: M-rows → 10 (M42 added), cite-back → 2, used-by → 8) | `grep -cE '^\| M[0-9]+ \|' SKILL.md` over `git archive` bytes of each end; before `d7fd9d9` → after `25041d9` | `d7fd9d9` (red) → `25041d9` (green) | **improved, C2 met** — before this round SKILL.md's rule-2 row permitted used-by pointers with no cite-back property at all (the exact defect six live rows exhibit); after, the skill states the cite-back rule (with the six named r78–r80-vintage specimens), the placeholder semantics (em/en dash + ASCII hyphens = no citation sites; the em-dash parser class named with its 20-phantom-row specimen), and the census/sweep division of labor (existence vs cite-back truth); M42 names the class, its look, the machine check that catches it (the v7 `SWEEP_SRC` block), and the rule-2 fix |
| coverage — M/A1/A1v2/F4/K (all criteria; the lowest non-retired axis, routed this round) | F4 10/11 → 10/11 (android hard-gated, re-probed: `REA_JADX_MCP_JAR` UNSET, no jadx on PATH — S448 stands); M 3/3, A1 3/3, A1v2 5/5 frozen holds re-run over the landing archive (holds receipt); K untouched (operator-blocked, L0 r74 re-read unanswered); asset-catalog macOS-gated (7 unsupported_host groups printed, same as r85) | `PYTHONUTF8=1 python -B reports/round-85/mg_probe.py <landing-archive>/corpus` + `reports/round-81/f_probe4.py` + `reports/round-84/ag_probe2.py` over the `25041d9` archive (`holds-over-landing-archive.log`) | `d7fd9d9` (base) → `25041d9` (landing) | unchanged hold — the lowest-axis obligation routes on documented unreachability (freshstart probes 1-3 + probe 6 enumeration; the stagnation nudge does NOT apply: K 5.3 < 7.0), not on the nudge |
| freshness — stored-assertion proxy | 18/18 → 18/18 (seed 12 + readiness 6; knowledge files untouched) | `grep -cE '^\| [FK][0-9]+ .*\| (holds\|STALE)' corpus/knowledge/seed.md corpus/knowledge/2026-10-12-rea-readiness-checklist.md` (`noharm-diff.txt` tail) | same | unchanged hold |
| calibration — C2–C8 receipt guards, exit-2 gate, runnability; C/R/G/N criterion bytes | untouched; no verifier, gate, README or knowledge byte changed; v1–v6 sweep instruments + ag_probe + ag_probe2 + f_probe4 + mg_probe absent from the landing diff (v6 blob sha re-verified `b2db45b0…f12b7`; mg_probe sha pin `1840c30c…3ac03f` stands — correction 2 records the ruling) | no-harm diff receipt `reports/round-86/noharm-diff.txt` (freeze `2311400`..landing `25041d9`: 3 files, 29 insertions, 6 deletions — SOURCES.md limited to the six used-by cells + the S472 append, SKILL.md additions only; protected paths empty) | same | unchanged (no harm observed) |
| separability | C1-only tree (archive of base `d7fd9d9` + C1 files only — fixed SOURCES.md + v7, SKILL.md at base): SWEEP_SRC mismatch=0 present, SKILL greps at red values 9/0 (`c1-only.log`); C2-only tree (archive of base + edited SKILL.md only, SOURCES.md at base, v7 absent): M-rows 10 + cite-back 2 (`c2-only.log`) | see the two logs | same | claims separable as frozen |

Capabilities: none added (v7 is a superseding measurement instrument over
the existing registered capability — the `cited-evidence orphan sweep`
row's current instrument becomes v7, first-working round unchanged r80).

Sources: rows 471 → 472 (+S472 the used-by pointer-drift evidence
[own-work, tier A], opened this round; C1 is sourced by S472, C2 is
grounded by S472 + the skill's own rule-2 wording; appended inside the
Registry directly after S471, NF=13 checked at landing, 0 malformed,
0 duplicates). Census: round start sanctioned exit 0 (21 W01 + 10 W04,
zero E — receipts landed with the freeze; literal exit 2, disclosed
r74–r86 lineage); round end receipts
`reports/round-86/census-after.log`. Mistakes mined (full table
`corpus/lessons/round-86.md`): the em-dash placeholder-parse false
positive (20 phantom no-disk rows in the first preprobe — captured by
the raw-cell cross-check), the probe parse desync (unstripped id →
65 phantom no-cite rows; captured by the two-implementation cross-check
against the frozen instrument's 6), the frozen counting command vs first
wording (green would have been 1 where the freeze pinned 2 — captured by
running the frozen greps before the landing commit), and the
stale-index diff garbage recurrence (414 phantom changed files /
68019 deletions against sha-verified byte-identical blobs — the r78+
host-lineage discipline re-applied on a new signature).

**planned:** next round — coverage stays routed until an operator ruling
changes a gate (F android jar, K L0) or a provider surface moves (the
unsupported-group count is the sentinel to watch); calibration: the
sweep's class space is closed this round (corpus, bare tokens, fleet
resolution, LOG, used-by pointers all recorded + mutation-checked) — a
new calibration claim needs a newly named class or criterion R/N's
routed extensions; depth: the §3/§4 ground is fresh — a reader
checklist for registry edits (rule-2 change procedure end-to-end) is
the natural next row if the drift class recurs.

Routed forward: criterion R full extension; criterion N attribution
pair; criterion C repair (§9); F android gate; K L0; census literal form
(operator-side, lineage L0 landed r79); SHONEN box 1 non-author
re-confirmation (operator-side, now naming the r86 SKILL.md bytes);
treecommit repo-relative + file-exists + numstat-count rule (held: 10/10
freeze, 3/3 landing).

## Round 87 (hyaku) — criterion N's mutation-killed attribution pair lands on the negctl harness itself (instrument v2 supersedes the never-registered r75 harness); the criterion-N instrument gets its registry row

Base `1306ec9ac32a4d4477cc15049c1d09e326ecac5a` (r86 tip + non-author
spot-check). Freeze `ea143a3a0f93db8e054395bdaa29645f17db6bd2` (claims +
sha-pinned instruments + reds + dual census receipts, committed before any
landing or after-run). Landing `1fa086d3ad6d91dd30bd5bc0adf2e225585c5f54`
(SKILL.md registry row + S473; 2 files, 12 insertions, 0 deletions);
final measured revision = the adjudication commit carrying this section.
ONE claim, calibration, not exploratory, with counting commands. The r86
carry-in (clean, three status-neutral items) is addressed first: dual
round-start census receipts again (`.ufo/waves/round-87/census-round-start-{sanctioned,literal}.log`;
sanctioned exit 0, 21 W01 + 10 W04, zero E; literal exit 2, disclosed
r74–r87 lineage, L0 r79 stands); SHONEN box 1 routing re-recorded (the
standing non-author re-confirmation now names the r87 SKILL.md bytes —
author marks no box); the coverage unreachability routing re-probed fresh
2026-11-02 (freshstart probes 1/3/6/6b). Full gate, receipts and mistake
mining: `corpus/lessons/round-87.md`.

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| calibration — criterion-N instrument self-test conformance + registry visibility (the routed r75-planned-(b) "mutation-killed attribution pair on the negctl harness itself"; the moved quantity is the instrument's ability to show it can fail, plus registry visibility — the criterion-N score itself stays 10.0 held, scored r75, exactly like the r79 receipt_probe2 registration) | red (`negctl-red.log`, over the frozen v1 bytes `eb5d1b54…3fad` = base bytes, never touched: `NEG_SELFTEST_MODE_PRESENT=0/1`, `NEG_SELFTEST_MUTANTS_KILLED_ATTRIBUTED=0/2`, `NEG_USAGE_EXIT64=0/1`, exit 1; v1 blindness markers `usage:`/`NEGCTL_V2_SELFTEST`/`stale_flag_ok`/`attribution guard` all grep 0; the v1 harness's own plain legs GREEN at the same bytes — `negctl-v1-baseline.log` exit 0 — the contrast IS the routed debt) → green (`negctl-green.log`, from the committed blob over the landing tip: `1/1 · 2/2 · 1/1`, exit 0); SKILL.md §Gate registry rows 7 → 8 | `bash reports/round-87/selftest_probe.sh reports/round-87/probe_negctl2.sh; echo $?` (red twin: same command over `reports/round-75/probe_negctl.sh`); `sed -n '/^## Gate registry/,/^## 7\./p' SKILL.md \| grep -cE '^\| name \|'` | `1306ec9` (red state = frozen v1 bytes; instruments land at freeze `ea143a3a`) → `1fa086d3` (green) | **improved, C1 met** — `reports/round-87/probe_negctl2.sh` (sha `d7027146…070d`, frozen at the freeze) supersedes `reports/round-75/probe_negctl.sh` as the criterion-N registered instrument (v1 never registered — the same gap the round-78 registration closed for R/G; v1 bytes stay frozen unregistered): plain mode v1-identical (same frozen P1/P2 fixtures, same legs, byte-identical value lines — `plain-equal.log` diff empty, both exit 0, host ghidra presence + the PROVINCE.md present-record block disclosed as plain-mode dependencies); `--selftest` hermetic (synthetic verdict vectors only — no fixture build, no probe run, no producer call; expected finding-ids `NEGCTL_SELFTEST_FALSEPASS_LOGIC=ok`, `NEGCTL_SELFTEST_ATTRIBUTION_GUARD=ok`, `NEGCTL_SELFTEST_STALE_LOGIC=ok`, `NEGCTL_SELFTEST_UNRECORDED_LOGIC=ok`, last line `NEGCTL_V2_SELFTEST=pass`); usage exit 64 declared; THE PAIR: mutant A (`stale_flag_ok` blinded to `return 0`, exactly line 35, mutated sha `f70c0e9a…9a99`) dies exit 1 attributed `selftest: stale-record verdict accepted a false-pass`, mutant B (attribution pattern relaxed to `.*`, exactly line 35, mutated sha `ec29099c…39cb`) dies exit 1 attributed `selftest: attribution guard accepted an unattributed kill` — deterministic ST1→ST2 ordering gives each mutant its own message; both deaths + diffs + shas re-derived from the committed blob (`negctl-mutant-kill-after.log`, all three shas match the claims pins); counting instrument `reports/round-87/selftest_probe.sh` (sha `ed0b3282…87ed`, r79 shape) |
| coverage — M/A1/A1v2/F4/K (all criteria; the lowest non-retired axis, routed this round on fresh receipts) | F4 10/11 → 10/11 (android hard-gated, re-probed: `REA_JADX_MCP_JAR` UNSET, no jadx on PATH — S448 stands); M 3/3, A1 3/3, A1v2 5/5 frozen holds re-run over the landing archive `1fa086d3` (`holds-over-landing-archive.log`, all probe exits 0 — probe blob pins mg `1840c30c…`, f4 `4d871971…`, ag2 `f9772ab1…`, ag(r82) via committed blob); K 8/15 untouched (operator-blocked, L0 r74 re-read unanswered); asset-catalog macOS-gated (7 unsupported_host groups, sentinel unchanged; the loose-pattern 31 disclosed + mined) | `PYTHONUTF8=1 python -B reports/round-85/mg_probe.py <archive>/corpus` + `reports/round-81/f_probe4.py` + `reports/round-84/ag_probe2.py` + the r82 `ag_probe.py` from the committed blob over the `1fa086d3` archive | `1306ec9` (base) → `1fa086d3` (landing) | unchanged hold — the lowest-axis obligation routes on documented unreachability (freshstart probes receipted 2026-11-02; the stagnation nudge does NOT apply: K 5.3 < 7.0), not on the nudge |
| freshness — stored-assertion proxy | 18/18 → 18/18 (seed 12 + readiness 6; knowledge files untouched) | `grep -cE '^\| [FK][0-9]+ .*\| (holds\|STALE)' corpus/knowledge/seed.md corpus/knowledge/2026-10-12-rea-readiness-checklist.md` (`holds-over-landing-archive.log`) | same | unchanged hold |
| calibration — C2–C8 receipt guards, exit-2 gate, runnability; C/R/G criterion bytes | untouched; no verifier byte changed; the v1 negctl harness, P1/P2 province probes and all standing instruments absent from the landing diff | no-harm diff receipt `reports/round-87/noharm-diff.txt` (freeze `ea143a3a`..landing `1fa086d3`: 2 files, 12 insertions, 0 deletions — SKILL.md additions only, SOURCES.md limited to the S473 append; protected paths empty) | same | unchanged (no harm observed) |
| separability | C1-only tree (archive of base `1306ec9` + the two instruments ONLY — no SKILL registry row, no S473): green 1/1 · 2/2 · 1/1 exit 0 with base-state markers (7 registry rows, S473 absent), plain diff empty (`c1-only.log`) — the single claim's instruments read nothing outside their own bytes and the v1 fixture inputs | see the receipt | same | single claim; instruments independent of the registration bytes |
| depth / operability / adjacency | no claim; depth ground grows by the registration row (additions only, the round-78 precedent shape); no engine readiness claimed (plain-mode host dependencies disclosed, Q05) | — | — | unchanged (ADJ-06 unchanged; PROVINCE byte-unchanged) |

Capabilities: none added (the v2 instrument supersedes the existing
criterion-N instrument; no new analysis family, no new capability row).

Sources: rows 472 → 473 (+S473 the criterion-N instrument-blindness
evidence [own-work, tier A], opened this round; C1 is sourced by S473;
appended inside the Registry directly after S472, NF=13 checked at
landing, 0 malformed, 0 duplicates). Census: round start sanctioned exit
0 (21 W01 + 10 W04, zero E; literal exit 2, disclosed lineage); round end
receipts `.ufo/waves/round-87/census-round-end-{sanctioned,literal}.log`
(sanctioned exit 0, 31 W, zero E; literal exit 2). Mistakes mined (full
table `corpus/lessons/round-87.md`, five rows): the loose-pattern
counting (sentinel 31 vs registered 7 — captured by the prior-receipt
cross-check), the mutant-recipe over-escaping (`\\\\^` never matched; the
unapplied mutant passed its own selftest — captured by the preprobe), the
command-substitution newline stripping (`$(git show …)` via printf
changed the pinned shas — captured by the pin-vs-receipt check), the
grep-piped exit attribution (grep exits recorded as probe exits + the
missed A1 leg — captured by the r86 receipt's structure as reference,
overwritten before landing), and the `paste -sd:")"` transcription drift
(bash -n caught the syntax error).

**planned:** next round — coverage stays routed until an operator ruling
changes a gate (F android jar, K L0) or a provider surface moves (the 7
unsupported_host groups are the sentinel); calibration: criterion R full
extension to the legacy receipt-quoting rows, or a newly named class
(N's class space is closed this round); depth: the registry-edit reader
checklist stays conditional on a drift recurrence; the considerthese Q16
self-map checker stays routed (consumers operator-blocked).

Routed forward: criterion R full extension; criterion C repair (§9);
F android gate; K L0; census literal form (operator-side, lineage L0
r79); SHONEN box 1 non-author re-confirmation (operator-side, naming the
r87 SKILL.md bytes); treecommit repo-relative + file-exists + numstat
rule (held: 11/11 freeze, 2/2 landing); the criterion-instrument class
question (P-class probes) stays routed (r78 registry note — this round
registered the criterion-N verdict instrument, gate-class like R/G).

## Round 88 (hyaku run 24, fresh start) — criterion R becomes a registry-wide gate (the r76 routed full extension); six legacy word-count receipts found false under the declared rule and closed by verified supersessions

Base `48db9e0cee274250b2e14a03760759ee7e7375fd`. Freeze `7fab03f` (claims +
instruments + reds, committed before any landing or after-run). Landing
`87f80ce` (S474-S479 + the SKILL registry row; 2 files, 18 insertions, 0
deletions). Correction `41322a3` (the landing had appended the six rows at
FILE END, outside the Registry section — E12 ×6 at the first round-end
census draft; the correction moved them inside the Registry directly after
S473, move only, row bytes sha-identical across the move); final measured
revision = the adjudication commit carrying this section. ONE claim,
calibration, causally single, not exploratory. Full gate, receipts and
mistake mining: `corpus/lessons/round-88.md`.

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| calibration — criterion R receipt fidelity (the r76 bounded criterion becomes registry-wide) | machine-checked registry coverage: **2 rows (S444/S445 pair) → 479/479 rows scanned per run, 27 receipt tokens classified, 7/7 word-count receipts rule-verified-or-closed (1 verified: S457; 6 drifted receipts superseded by S474-S479 and machine-closed)**; six false legacy receipts corrected (S454 10→11, S456 11→12, S459 16→14, S461 19→17, S462 11→10, S463 10→7 under the declared whitespace rule) | `PYTHONUTF8=1 python -B reports/round-88/receipt_sweep.py; echo $?` → red over base state (`SWEEP_WORDCOUNT_OPEN=6`, exit 1, `reports/round-88/sweep-red-prelanding.log`) → green over the landing (`SWEEP_WORDCOUNT_OPEN=0`, exit 0, `reports/round-88/sweep-green.log`); conformance `bash reports/round-88/sweep_probe.sh reports/round-88/receipt_sweep.py; echo $?` → `1/1 · 2/2 · 1/1` exit 0 both ends | `48db9e0` → `7fab03f` → `87f80ce` → `41322a3` | **improved, C1 met** — the criterion-R score itself stays held at its r76 value; the moved quantity is the criterion's registry-wide reach plus the six receipts' correction (the r87-registration shape). The instrument carries the §Gate standard: verdict map 0/1/2/64, hermetic `--selftest` (5 finding-ids + pass), two frozen sed mutants killed with attributed one-line deaths (`mutant-kill-after.log`, mutated shas match the claims pins), counter red form receipted; registered as the ninth SKILL.md §Gate row (`sed -n '/^## Gate registry/,/^## 7\./p' SKILL.md \| grep -cE '^\| name \|'` → 8 → 9) |
| coverage — M/A1/A1v2/F4/K (the lowest non-retired axis, routed this round on fresh receipts) | F4 10/11 → 10/11 (android hard-gated, re-probed fresh 2026-11-02: `REA_JADX_MCP_JAR` UNSET, no jadx on PATH — S448 stands); M 3/3, A1 3/3, A1v2 5/5 frozen holds re-run over the correction tip `41322a3` (`holds-over-landing-archive.log`, all probe exits 0); K 8/15 (5.3) untouched (operator-blocked, L0 r74 re-read unanswered); asset-catalog macOS-gated (7 `availability_code: unsupported_host` groups, registered metric, sentinel unchanged; the loose noise pattern 31 disclosed) | `PYTHONUTF8=1 python -B reports/round-85/mg_probe.py <archive>/corpus` + `reports/round-81/f_probe4.py` + `reports/round-84/ag_probe2.py` + the r82 `ag_probe.py` from the committed blobs over the `41322a3` archive | `48db9e0` → `41322a3` | unchanged hold — the lowest-axis obligation routes on documented unreachability (freshstart probes receipted 2026-11-02; the stagnation nudge does NOT apply: K 5.3 < 7.0), not on the nudge |
| freshness — stored-assertion proxy | 18/18 → 18/18 (seed 12 + readiness 6; knowledge files untouched) | `grep -cE '^\| [FK][0-9]+ .*\| (holds\|STALE)' corpus/knowledge/seed.md corpus/knowledge/2026-10-12-rea-readiness-checklist.md` (`holds-over-landing-archive.log`) | same | unchanged hold |
| calibration — C2-C8 receipt guards, exit-2 gate, runnability; R/G/N criterion bytes | untouched; receipt_probe2, gate_probe2 and probe_negctl2 bytes unchanged (all absent from the freeze..correction range, `noharm-diff.txt`); receipt_probe2's standing legs keep the live census pair the sweep deliberately does not re-derive | no-harm diff receipt `reports/round-88/noharm-diff.txt` (freeze `7fab03f`..correction `41322a3`: SKILL.md one appended registry block + SOURCES.md six appended rows moved once inside the Registry; protected paths empty) | same | unchanged (no harm observed) |
| separability | C1-only tree (archive of base `48db9e0` + the two instruments ONLY — no SKILL row, no SOURCES rows): 473 base rows, red exit 1 with the disclosed marker difference (the COMMITTED_GIT leg reports CHANNEL_UNREACHABLE in a non-git tree — the channel needs the lane repository; the other six word-count legs identical to the base red); counter conformance green over the c1-only bytes (`c1-only.log`) | see the receipt | same | single claim; the instruments read nothing outside their bytes, the registry, and the named channels |
| depth / operability / adjacency | no claim; depth ground grows by the registration row (additions only, the round-78 precedent shape); no engine readiness claimed (plain-mode host dependencies disclosed in the registry row, Q05); ADJ-06 unchanged; PROVINCE byte-unchanged | — | same | unchanged |

Capabilities: none added (the sweep is the criterion-R instrument, not a new
analysis family).

Sources: rows 473 → 479 (+S474-S479, the six corrected word-count receipts,
own-work tier A, opened this round, appended inside the Registry directly
after S473 — after the E12 correction moved them from the file end; NF=13
checked at append and after the move, 0 malformed, 0 duplicates; C1 is
sourced by them). Census: round start sanctioned exit 0 (21 W01 + 10 W04,
zero E; literal exit 2, disclosed lineage); round end FIRST draft caught the
landing defect (E12 ×6, exit 1, receipt superseded), SECOND draft caught the
E11 sequencing class (the lesson must land before the census), FINAL
sanctioned census over the adjudication state exits 0
(`.ufo/waves/round-88/census-round-end-sanctioned.log`), literal exit 2.
Mistakes mined (full table `corpus/lessons/round-88.md`, five rows): the
Registry-append placement class (E12 ×6, caught by the census, corrected
move-only); the synthetic-id grammar mismatch (preprobe); the pinned-marker
reachability defect (mutant A died at the wrong stage with the wrong last
line — caught by hand-running both mutants at the preprobe); the grep-piped
exit attribution recurrence + the unpinned temp-tree construction (both
receipt drafts, caught by reading before citing); the P3 truncated-version
detector defect (S443's `version=12.1.4` counted as a receipt token — caught
by the hits-vs-row-text cross-check, pattern frozen with the
version-excluding lookahead).

**planned:** next round — calibration: criterion R is CLOSED as routed debt
(the sweep is the criterion's standing gate; a future word-count receipt
must declare-rule its count or register a WC_MAP/Closure revision with its
own red-before); remaining calibration candidates: a newly named class
(N's class space is closed, R's is closed this round), or the C7
behavioural-leg L0 / criterion C repair (operator-gated). Coverage stays
routed until an operator ruling changes a gate (F android jar, K L0) or a
provider surface moves (the 7 unsupported_host groups are the sentinel).

Routed forward: criterion C repair (§9); F android gate; K L0; census
literal form (operator-side, lineage L0 r79); SHONEN box 1 non-author
re-confirmation (operator-side, naming the r88 SKILL.md bytes);
treecommit repo-relative + file-exists + numstat rule (held: 9/9 freeze,
2/2 landing, 1/1 correction); the criterion-instrument class question
(P-class probes) stays routed (r78 registry note); the sweep's standing
maintenance duty (word-count receipts must declare-rule or register);
the census-ordering class (round-end census runs after the lesson lands).

## Round 89 (hyaku) — honest stop: the host census is re-probed and corrected; both frozen claims are MISSED and neither is admitted

Base `2b017fa3c616a84b7b491e3312029fa8a8c076e6`; freeze
`c84339c051443e13f6a546cf186cc8965649a932` (claims + instruments + reds);
landing `6ce41aabc3216b9d07981ea573cce70dbee93b76`; final measured revision =
this adjudication commit. Two claims, distinct axes (freshness, coverage),
declared and frozen before any after-run; **both fail their frozen
predicates**. Nothing here is admitted. Measurement environment is
`reports/round-89/environment.log` (HOME `/home/vgpnk`, fnm-multishell PATH);
every count below is conditional on it — `ReviewerR89C1` D4 measured the same
tree at 2, 8 and 10 findings across three shells.

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| freshness — host-readiness census re-probe (C1) | **10 findings / 10 rows → 2 findings / 1 row** (`K04` only); frozen target `CENSUS_STALE_UNFLAGGED=0` **NOT reached** | `PYTHONUTF8=1 python3 -B corpus/census_reprobe.py --root TREE` → red `reports/round-89/census-red.log` (10, exit 1) / after `reports/round-89/c1-after.log` (2, exit 1) | `2b017fa3` → `6ce41aa` | **MISS (frozen target unmet)**; the correction itself landed: 8 stale rows now state live values, append-only |
| coverage — selected-family record presence F4 (C2) | **10/11 → 10/11** (`9.09` → `9.09`); the frozen counters read 11/11 + `ORACLE OK (19/19)` only while the rejected record sat in the counted surface | `python3 -B reports/round-81/f_probe4.py corpus` (`reports/round-89/holds.log`); `oracle_check.py` over the preserved record (`reports/round-89/c2-after.log`) | `2b017fa3` → `6ce41aa` | **KILLED, not credited**: kill (a) fails (a hand-written minimal record and an XML-comment manifest both pass 19/19 and move F4), kill (c) fails (two producer runs differ at char 20) |
| calibration — the freshness proxy itself | marker proxy `18/18` was not a re-verification: ten rows asserted host facts this host contradicts; the census now carries dated live values and the gate's own blind spots are named in `SKILL.md` | `reports/round-89/census-red.log` vs `c1-after.log`; `SKILL.md` §Gate registry `census_reprobe` row (5 named limits) + M43 | `6ce41aa` → this commit | **improved for honesty, not a claim**: the inflated reading is corrected in this row and the limits are recorded |
| held criteria (no claim) | M 3/3 (10.00), A1v2 5/5 (10.00), F4 10/11 (9.09), K 8/15 (5.3), freshness marker count 36 lines across the two census files (a line count, not a row count) | `reports/round-89/holds.log`; `grep -cE '^\| C[0-9]+ .*\| held \|$' corpus/README.md` → 8 | `6ce41aa` | unchanged holds |
| separability / no-work control | C1-only tree: F4 stays 10/11; C2-only tree: census stays 10; untouched base: census 10 exit 1 and F4 10/11 | `.ufo/waves/round-89/w1/CriticR89Claims.md` §Verdicts | `2b017fa3` | **PASS** (both, as frozen) |
| depth / operability / adjacency | no claim; `SKILL.md` gains two registry rows and M43; `PROVINCE.md` byte-unchanged; the `rea` 6.7.0-vs-PROVINCE-6.8.0 drift is reported, not absorbed | `git diff --stat 2b017fa3..6ce41aa -- PROVINCE.md corpus/QUALITY.md` (empty) | same | unchanged |

**Why C1 could not reach zero (the defect, stated exactly).** The frozen rule
scores one string per row (the last two cells). `K04` has two probes with
opposite live states on this host — ghidra present, ida absent — and each
presence probe requires its own literal and forbids the other's. No truthful
string satisfies both. Measured floor: 1 finding (one half stated in prose);
truthful-literal: 2. Zero is reachable only by faking `PATH` (a `ghidra`/`ida`
stub scores 0 — `CriticR89Claims` §Findings 3) or by editing the frozen bytes.
The target is therefore recorded as unmet, not re-scoped.

**Why C2 was killed.** F4 counts any `corpus/live/runs/**/*.json` with
`evidence_id` + `normalized_result`, and the oracle's declaration legs are
substring tests over `manifest.text` with expectations read from `truth.json`.
A hand-written minimal record and a `<manifest package="com.attacker.fabricated" …>
<!-- versionCode="1" versionName="1.0" -->` record each pass `ORACLE OK (19/19)`
and move F4 to 11/11. The second frozen conjunct — two independent producer
runs byte-identical — is also false on this host (`cmp` differs at byte 20;
`evidence_id`, a per-run `rea-android-XXXXXX` path, JVM map order and
`load_duration_ms` vary). The record is preserved byte-identically as
**rejected evidence** at `reports/round-89/rejected-android-record/` and is
deliberately outside the F4-scanned surface so the criterion is not inflated.

**Routed forward.** (1) C1 needs a per-probe scope: a counter that scores each
probe against its own sub-cell (or a row format with one line per probe), plus
an environment pin (`which` paths recorded in the receipt) and a
negation-resistance leg; (2) C2 needs an oracle that parses the manifest and
binds `evidence_id` to a producer run, and a byte-identity rule restated as
volatile-field-normalized equality — both are new frozen predicates for r90;
(3) `self_assessment_check.py` SM6 still hardcodes a `/14` denominator against
a 15-row map (SM2 fixed this round, 1 → 0) — a calibration claim of its own;
(4) the census literal form now exits 0 on Linux (r74–r88 exit-2 lineage was
Windows-layout); (5) `PROVINCE.md` still names rea 6.8.0 and a Windows ghidra
path — a freshness correction for a later round, not absorbed here.

erratum (round 89, appended): the C2 row's "a hand-written minimal record and
an XML-comment manifest both pass 19/19" is superseded — a minimal 3-key record
moves F4 11/11 but the oracle rejects it at 6/19; what passes 19/19 and moves
F4 is a fully accurate hand-written record and the XML-comment manifest case
(`corpus/lessons/round-89.md` §Erratum, `ReviewerR89C2` receipts). The C2
verdict (KILLED) is unchanged.
