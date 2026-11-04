# ReviewerR90C2 — attack on claim C2 instruments + producer record (round 90, w1)

Freeze: `c7767789fe9e96bcc0d50656ad4bdce69ba3a3a9`. Scratch: `/fast/scratch/hyaku/revenger-r90/ReviewerR90C2` (TMPDIR set to it; deleted before yield).
Receipts (all absolute, in `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ReviewerR90C2/`):
`c2-counter-candidate.log`, `c2-controls-repro.log`, `batteries.log`, `attacks.log` (+ `attack.py`), `independent-runs.log`.
No tool installed or upgraded. LSP not used: the targets are standalone Python scripts with no cross-file callers; checks are by direct execution.

## Results per step

1. **Oracle diff** (`diff /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65/oracle_check.py …/oracle_check2.py`): only the docstring, usage strings, `import xml.etree.ElementTree` and the manifest declaration legs changed. v1 has 19 checks, v2 has 22: v1's two substring legs (`versionCode="1"`, `versionName="1.0"` in the text) are replaced by root-attribute legs, and three legs are added (root parses/tag `manifest`, root `package` == authored, `package_name` == parsed root package). The other 17 v1 legs (premise ×5, identity ×6, `package_name`, status, class_count, resource_count, permissions, signature) are byte-identical. The claim's statement "only manifest legs changed" holds. Note: v2 does not imply v1. `Q1-single-quoted-equivalent` (XML-equivalent `'1'` quoting) is v2=accept, v1=reject. That is correct behaviour, not a defect.
2. **Batteries** (`batteries.log`): `oracle_battery.py --oracle oracle_check.py` gives `ORACLE_MISCLASS=5/9` (F1, F4, F5, F6, F7), the same as `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-90/c2-red-v1-battery.log`. `--oracle oracle_check2.py` gives `ORACLE_MISCLASS=0/9`, EXIT=0. `norm_eq.py --selftest` gives `NORM_SELFTEST=pass`, EXIT=0. The cases regenerated with `--write` match the committed `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-90/oracle-battery-cases/*` byte for byte (sha256 diff empty). All 18 rows of `instrument-pins.log` verify `OK`, both in the lane and in the candidate tree. **c2_counter vs claims.md:** I checked K1–K6 against claims.md for paths (`corpus/live/runs/round-90/inspection.json`, `reports/round-90/android-run2.json`, `reports/round-90/android-receipt.json`), exact strings (`F4_COVERAGE=11/11`, `ORACLE OK`+rc 0, `ORACLE_MISCLASS=0/9`, `NORM_EQ=identical`+rc 0, `runs[i].stdout_sha256`, the r89 id `ev_387c9e9c…a588e4` in full) and exit codes (0 iff 6/6). All match.
3. **Controls** (`c2-controls-repro.log`): I reproduced both on a fresh `git archive c7767789… corpus reports`. No-record gives `C2_CONJUNCTS=1/6` (only K3 passes), EXIT=1. Copy-r89 gives `5/6` (K6 FAIL), EXIT=1. Both match the L1 logs `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-90/c2-control-norecord.log` and `…/c2-control-copy89.log` line for line, except the scratch path.
4. **Producer record** (`ExecR90Producer/run1.json`, `run2.json`, `receipt.json` present). Candidate tree as specified, then `python3 -B <tree>/reports/round-90/c2_counter.py --tree <tree>` (`c2-counter-candidate.log`):
   - K1=pass `F4_COVERAGE=11/11 score=10.00`
   - K2=pass `ORACLE OK (22/22 checks)`
   - K3=pass `ORACLE_MISCLASS=0/9`
   - K4=pass `NORM_EQ=identical`
   - K5=pass `9d665ffbc8674d41`, `214094fbe04883e1` (= receipt digests)
   - K6=pass `ev_affae0e5ae0fb1ef2…` ≠ `ev_d4a34332e3ca12df7…`, neither is the r89 id
   - `C2_CONJUNCTS=6/6`, EXIT=0.

   The raw run1/run2 differences are only `$.evidence_id`, `raw_result.calls[0]` JVM-map text (key order), and `calls[1].input.path`, `calls[1]` text and `loaded.apk_path` (the `rea-android-*` dir). All of these fall in V1–V4; no difference lies outside the frozen set (kill rule b holds).
   - **Independent reproduction** (`independent-runs.log`). I made two of my own `rea 6.7.0 inspect-android-package` runs in scratch. They are `NORM_EQ=identical` to each other. Against producer run1, the only DIFFs are `$.parameters.path` and `$.subject.local_path`, caused by my different argv/cwd (non-volatile by design). My own run passes `ORACLE OK (22/22)`. Producer run1 vs the retained r89 record is `NORM_EQ=identical`. The producer output is therefore consistent with genuine, reproducible rea output.

## Findings (by severity)

**MEDIUM-1: C2 is satisfiable 6/6 with no producer run (the bound is stated, but now shown to be total).** `attacks.log`, "FORGE tree": the r89 record (or any content-accurate record) is landed with a hand-edited `ev_1…1` id. run2 is the same bytes with `evidence_id="run2-anything"`, and a one-field receipt holds the two sha256 values. Result: `C2_CONJUNCTS=6/6`, EXIT 0. claims.md concedes that "hand-edited distinct ids would pass K6" (Q09). Two further gaps widen it:
- (a) run2 is never shape-checked. K6 only needs it truthy, and norm_eq V1 maps any whole-string own id to `<EVIDENCE_ID>`, so a non-`ev_<64hex>` run2 passes (`N4`).
- (b) K5 is self-referential. The receipt is the only witness and needs no exit code, command line, timestamps or rea version.

In practice the only control that separates honest from fabricated is K6, and K6 catches only *unedited* copies. Not a kill under the frozen predicate. The admission text must not claim more than "a content-accurate record plus a self-declared receipt".

**MEDIUM-2: oracle v2 false-accepts root-identity forgeries inside its own declared scope** (`attacks.log`; none is in the frozen 9-case battery, so K3 is unaffected):
- `A1-namespaced-package-only` is accepted. `local()` strips namespaces, so `x:package="com.example.r65"` in `urn:evil` counts as the manifest `package` attribute. In XML-namespace terms that is a different attribute.
- `A3-foreign-root-namespace` is accepted. `<e:manifest xmlns:e="urn:evil">` passes the "root tag manifest" leg.
- `A2-versions-in-foreign-namespace` (`z:versionCode` in `urn:evil`) and `A7-unnamespaced-versions` are accepted. The docstring declares "any namespace" deliberately, but nothing pins the producer's URI `android` or the Android schema URI.

Proposal for v3 (do not edit v2): require `package` with no namespace and the root tag with no namespace, and require version attributes in the namespace set `{"android", "http://schemas.android.com/apk/res/android"}`. Add A1/A2/A3 as battery cases labelled reject.

**LOW-1: the oracle accepts manifests that misstate the fixture outside the root identity attributes.**
- `A4-fabricated-permission-child` (`<uses-permission SEND_SMS>`, while `permissions == []`) is accepted.
- `A5-fabricated-component-child` (an exported `<activity>`) is accepted.
- `A6-fabricated-root-attr-sharedUserId` (`android:sharedUserId="android.uid.system"`) is accepted.

By the battery's own label rule ("`reject` = the record misstates the fixture's manifest") these would be reject. The oracle checks only root identity, which matches the claim's wording, so this is a coverage bound, not a defect against the frozen claim. Proposal: an exact-children / exact-root-attribute-set leg, derived from the fixture AXML.

**LOW-2: norm_eq normalises more than V1–V4 literally say** (`attacks.log`):
- `N1`: the V2 regex `[^"\s]*/rea-android-…` is greedy over any non-space prefix. `"pkg=com.example.r65:/s/rea-android-aa11/x"` and `"pkg=com.attacker.fab:/s/rea-android-bb22/x"` compare identical.
- `N2`: V3 parses JSON text with `json.loads`, which collapses duplicate keys. `{"x":1,"x":2}` equals `{"x":2}`.
- `N3`: V4 drops `load_duration_ms` at any depth and of any type, including under `normalized_result`.

None of these is exercised by the landed runs (the raw diff above shows only true V1–V4 differences). Proposal: anchor V2 to `(^|[\s"=])/…` or to a full absolute path, and use `object_pairs_hook` to reject duplicate keys.

**LOW-3: c2_counter runs the TREE's own copies of every instrument and does not verify pins.** The counter executes `t/reports/round-81/f_probe4.py`, `t/…/oracle_check2.py`, `t/…/oracle_battery.py` and `t/…/norm_eq.py`, and never checks `instrument-pins.log`. A landing tree that edits an instrument would be scored by the edited instrument. Closure must run `sha256sum -c` against the **freeze commit's** pins log over the landing tree. I did this for the candidate tree: all 18 rows `OK`.

**LOW-4: run selection is undisclosed in the receipt.** `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ExecR90Producer/discarded-attempt0-timing.log` records an earlier pair of runs (sha `5a20c0a0…`, `0529afc8…`, 22:01:54–22:02:05Z) that was discarded. Their bytes are not retained, and `receipt.json` lists only the landed pair. The L1 should state in the receipt or ledger that four runs happened and why attempt 0 was discarded. My own independent pair is norm-equal, so selection bias is unlikely, but it should be disclosed.

**INFO:**
- `c2_counter.py --tree` with no value raises `IndexError`, exit 1, not the documented 64.
- `oracle_check2.py` is mode 0644 while v1 is 0755. This is harmless because the counter invokes it through `sys.executable`.
- The lane working tree has an uncommitted `M corpus/README.md` that is not part of the C2 read set (`git status --short`). Flagged for the L1 because C1 reads README.

## Residual risk / verification gaps
- Kill rule (c), "landed record is run1's exact stdout", can only be checked through the self-declared receipt digest (K5). I could not observe the producer's stdout directly. My independent runs bound this: their content is equal under norm_eq apart from the argv path.
- I did not check the provenance of the landed bytes beyond the above; this is out of claim by Q09.
- The `SOURCES.md` rows for the v2 manifest legs were not in my target.

VERDICT: C2 holds as frozen. The candidate tree scores `C2_CONJUNCTS=6/6`, both controls reproduce as failing, oracle v1 5/9 → v2 0/9, and the norm_eq selftest passes. Out of battery, oracle v2 false-accepts namespaced-root forgeries, and the whole predicate is satisfiable with no producer run (MEDIUM). Admission must keep its claim to content plus self-declared receipt, and use v3 legs next round.
