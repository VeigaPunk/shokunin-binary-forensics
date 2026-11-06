# ReviewerCapR100 — findings (round 100, wave w1)

Seat: capability reviewer (C2). Receipts: `.ufo/waves/round-100/w1/ReviewerCapR100/` (`pre/receipts/`, `post/logs/`,
attack assets under `post/`). Scratch `/fast/scratch/hyaku/revenger-r100/ReviewerCapR100/` removed before yield.

FROZEN observed: `.ufo/waves/round-100/w1/FROZEN` = `173abe91a80d79336ca9228643c63d41e0e7635c` (instrument freeze,
commit subject "round-100: instrument freeze …"; `cap_apk_probe.py` sha256 `b2c9d189…2c71a`,
`controls_c2.sh` sha256 `479f690e…e408`). Loop appeared at iteration 33 of 90 (`proc://frozen-wait-R100`, exit 0).
Frozen bytes extracted with `git archive` into scratch; all scored runs use that tree.

## Verdict

**holds** for the frozen C2 predicate, with one **non-blocking defect** recorded below (fixed-input memorization
of the tamper leg). The probe passes the genuine fixture with rc 0, both frozen controls refuse, and two of my three
attacks are refused for the right reason. The third attack (a PATH shim that memorizes the probe's deterministic
tampered digest) passes the probe; it is outside the frozen kill rule's literal wording but shows the tamper leg is
not an independent oracle against a hostile PATH.

## Part 1 — independent re-decode of apk-r65 (pre-FROZEN)

Fixture sha256 `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` = `truth.json` `image.sha256`.
All three members' sha256 recomputed from the container equal `truth.json` `members[*].sha256`.
(`pre/receipts/truth-crosscheck.txt`: `member_sha256_match_truth … True`.)

| reader | package | versionCode | versionName | receipt |
|---|---|---|---|---|
| androguard 4.1.4 `axml` (rc 0) | com.example.r65 | 1 | 1.0 | `pre/receipts/androguard-decode.xml` |
| apktool 3.0.3 `d -s` (rc 0) | com.example.r65 | 1 | 1.0 | `pre/receipts/apktool-manifest.xml` |
| own byte parser `pre/my_axml_parse.py` (rc 0) | com.example.r65 | 1 | 1.0 | `pre/receipts/my-axml-facts.json` |

All three agree with `truth.json`. My parser's pool strings, resource map (`versionCode`→0x0101021b,
`versionName`→0x0101021c) and the three attribute records `(ns_idx, name_idx, data_type, raw_value_idx, value)`
match `truth.json` `axml_declared` exactly (`attr_records_match_truth_declared: True`).
`readout.py` (`pre/receipts/readout-facts.jsonl`, rc 0) reads the same structures; its ZIP/chunk/attrExt offsets agree
with my parser. Its UTF-8 pool decode reads length fields as single bytes and does not handle the 2-byte long form;
sound for this fixture (all strings < 128 bytes, asserted), a robustness nit outside C2.

**Namespace-prefix quirk.** `versionCode`/`versionName` attribute records carry `ns_idx=0`, which indexes the string
`"android"` (the prefix), not index 1 (the URI). The START_NAMESPACE chunk correctly maps `android`→URI. Both decoders
therefore mint a synthetic prefix bound to the literal `"android"`:
- androguard: `xmlns:ns0="android"` … `ns0:versionCode="1" ns0:versionName="1.0"`
- apktool: `xmlns:n0="android"` … `n0:versionCode="1" n0:versionName="1.0"`

Attribute values are unaffected. The frozen probe handles it correctly (it compares local names via ElementTree and
the probe docstring documents this exact quirk). Any future consumer matching on `android:versionName` qnames would
false-fail on this fixture.

**Untracked file in the frozen corpus dir.** `corpus/fixtures/apk-r65/androguard.log` (mtime 19:39, before my first
run) is untracked in the lane working tree. Not created by me (my decoders ran with cwd in scratch). Not present in
the frozen archive. For the L1 to adjudicate.

## Part 2 — post-FROZEN re-run, frozen controls, attacks

All commands from the frozen tree, `PYTHONUTF8=1 python3 -B <frozen>/reports/round-100/cap_apk_probe.py --fixture <frozen>/corpus/fixtures/apk-r65 --work <scratch>`.

| run | rc | output (verbatim contract lines) | receipt |
|---|---|---|---|
| genuine fixture, real decoders | **0** | `CAP_FIXTURE_SHA=pass`, `CAP_DECODER androguard version=androguard, version 4.1.4`, `CAP_DECODER apktool version=3.0.3`, `CAP_ANDROGUARD=pass`, `CAP_APKTOOL=pass`, `CAP_TAMPER_DETECTED=pass`, `CAP_APK_VERDICT=pass` | `post/logs/probe-genuine.{out,err,rc}` |
| frozen `controls_c2.sh` (stub + flip) | **0** | `C2_CTRL_STUB=refused`, `C2_CTRL_FLIP=refused`, `C2_CONTROLS=control-ok` | `post/logs/controls.{out,rc}`, `post/logs/controls/control-{stub,flip}.log` |
| attack 1: PATH shims that decode genuinely but rewrite only `versionName` to `1.0` | **1** | `CAP_ANDROGUARD=pass`, `CAP_APKTOOL=pass`, `CAP_TAMPER_DETECTED=fail`, `CAP_APK_VERDICT=fail`; stderr: `androguard echoed the truth value` | `post/logs/attack1.*`; shims `post/attack1-shim-*.sh` |
| attack 2: fixture copy with a second `AndroidManifest.xml` member (versionName `9.9`), digest updated in a new truth.json | **1** | `CAP_FIXTURE_SHA=pass`, `CAP_ANDROGUARD=fail`, `CAP_APKTOOL=fail`, `CAP_TAMPER_DETECTED=fail`, `CAP_APK_VERDICT=fail`; stderr: decoders report `9.9` vs truth `1.0`; tamper: `manifest members found: ['AndroidManifest.xml', 'AndroidManifest.xml']` | `post/logs/attack2.*`; builder `post/build_attack2.py`, `post/attack2-build.json` |
| attack 3: PATH shims that memorize the probe's deterministic tampered digest `d01df086…c528` → report `1.1`; genuine digest → `1.0`; otherwise real decoder | **0** | all seven lines `pass`, `CAP_APK_VERDICT=pass` | `post/logs/attack3.*`; shims `post/attack3-memo-*.sh`; digests `post/{genuine,tamper}.sha`, `post/logs/tamper-sha.txt` |

Real-decoder check on the same tampered bytes (`post/logs/real-*`): androguard rc 0 reports `ns0:versionName="1.1"`;
apktool rc 0 reports `versionName="1.1"`; `zipfile.testzip()` → `None`. So the tamper leg is sound for genuine decoders.

Attack 1 is refused for the intended reason (the tamper leg requires `1.1`; the shim echoes truth). Attack 2 is refused
by the probe's duplicate-member check and by decoder/truth disagreement. Both were built with my own code, not the
probe's.

## Defect (non-blocking, recorded for the L1)

**D1: the tamper leg is a fixed-input oracle that a hostile PATH decoder can satisfy.** `tamper_leg` produces a
deterministic `tampered.apk` (digest `d01df086…c528`, 947 bytes). A PATH-shimmed decoder that recognises that digest
and reports `1.1` for it, while echoing truth for the genuine digest, passes the entire probe (attack 3, rc 0). The
frozen predicate and kill rule only refuse a shim that "echoes the truth values for any input"; attack 3 does not do
that, so the frozen wording is met. The probe therefore does not prove that a decoder reads the bytes it is given.
The threat requires PATH control and knowledge of the probe source (the same threat class the frozen stub control
addresses), so I do not rate it blocking. Possible follow-ups, not in this round's frozen bytes: randomize the tamper
value per run from a seeded nonce, or tamper a second field and require both to change.

## Residual risk and verification gaps

- Only one authored fixture; no real-world APK (frozen scope boundary).
- The SCORECARD `apk-manifest-cross-decode` row is the L1's; I did not read it as evidence beyond the frozen
  `CAP_` predicate. I did not run `controls_c2.sh` against the lane working tree's probe; I ran only the frozen archive.
- The attack-2 fixture and attack-3 memorizing shims are my own constructions in scratch (not committed).
- No tools installed or upgraded by this seat. Versions observed: androguard 4.1.4, apktool 3.0.3 (both existing
  `~/.local/bin` binaries, unchanged). apktool wrote its framework cache under `~/.local/share/apktool` (allowed).
- Exit codes observed: probe genuine 0; controls 0; attack1 1; attack2 1; attack3 0; my parser 0; readout 0;
  apktool `d -s` 0; androguard `axml` 0; FROZEN wait loop 0 (iteration 33).
