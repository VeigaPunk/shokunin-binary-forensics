# MutR90Oracle — round 90 w1: mutation test of the C2 instruments

Seat: MutR90Oracle (mutation tester). Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin` at HEAD
`c7767789fe9e96bcc0d50656ad4bdce69ba3a3a9` (the freeze commit). Scope: oracle v2 legs
(`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65/oracle_check2.py`) and norm_eq normalisation
(`/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-90/norm_eq.py`). No lane instrument was edited.

## Setup and pins

- The working-tree bytes equal the freeze-commit bytes (`git show c7767789…:<path> | sha256sum`) for `oracle_check2.py`
  (`de2b2ad2daf899ee…`), `norm_eq.py` (`06c7eac72ec81bc1…`), `oracle_battery.py` (`6b8c89ebb0ca0858…`), `fixture.apk`,
  `truth.json` and `reports/round-89/rejected-android-record/inspection.json`. The full pristine digests match
  `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-90/instrument-pins.log`.
- Scratch: `/fast/scratch/hyaku/revenger-r90/MutR90Oracle` (TMPDIR set to it). The whole `apk-r65/` dir was copied there
  so the mutant reads `fixture.apk` from its own directory. `norm_eq.py` was copied to `…/ne/norm_eq.py`.
- Oracle detector: `python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-90/oracle_battery.py --oracle <scratch oracle_check2.py> --write <scratch dir>`,
  i.e. the frozen battery with the lane `truth.json`. Norm detector: `python3 -B <scratch norm_eq.py> --selftest`.
- Protocol, per mutant: run on pristine, apply a single-occurrence text replacement (asserted), run, restore the exact
  pristine bytes, run again. Verdict: killed = mutant exit ≠ 0 while the pristine and restored runs exit 0 with identical
  output. Every restore was checked by sha256 against the pristine bytes (all 23: `restored_sha == pristine`), and every
  restored run's output equalled the pristine output. Inconclusive: 0.
- Pristine baselines: battery `ORACLE_MISCLASS=0/9` (all 9 cases ok); selftest `NORM_SELFTEST=pass` (all 5 legs ok).
- For each survivor, a killing case was built and run directly through the instrument's CLI on pristine, mutant and
  restored bytes. "Kills" = the pristine instrument gives the correct verdict (exit 1), the mutant gives the wrong one (exit 0),
  and the restored instrument gives exit 1 again.
- Harness: `harness.py`; full outputs: `results.json`; killing-case inputs: `killer-cases/` (all in this dir).
- Tools installed: none.

## Oracle mutants (battery: `oracle_battery.py --oracle <mutant>`)

| id | mutant (assigned O1–O6; O7–O13 extra) | mutant sha16 | battery output | verdict | killed by |
|---|---|---|---|---|---|
| O1 | drop root-tag check (`root is not None` only) | ac1a462259c8d33f | `ORACLE_MISCLASS=0/9` | **survived** | — |
| O2 | accept the authored `package` attr on ANY element (root.iter) | 1d52c78a8228c849 | `ORACLE_MISCLASS=0/9` | **survived** | — |
| O3 | `val in got` instead of `got == [val]` (versions) | ebfa89c4e359fff1 | `ORACLE_MISCLASS=1/9` | killed | F5-conflicting-duplicate-versionCode (reject→accept) |
| O4 | skip `package_name == parsed root package` leg | 1f0bec300d229fa1 | `ORACLE_MISCLASS=0/9` | survived (**equivalent**) | — |
| O5 | regex/substring fallback on ParseError | c2362891d7d50578 | `ORACLE_MISCLASS=1/9` | killed | F6-unparseable-text-with-fragments (reject→accept) |
| O6 | no namespace-local split (`local = lambda k: k`) | fa144d73a9bb1877 | `ORACLE_MISCLASS=2/9` | killed | P1-real-r89-record, P2-hand-written (accept→reject) |
| O7 | versions read from any element (root.iter) | ce5a7de0e3f353eb | `ORACLE_MISCLASS=1/9` | killed | F4-versions-smuggled-into-child (reject→accept) |
| O8 | drop `root package == [pkg]` leg | df079e181d05d369 | `ORACLE_MISCLASS=0/9` | **survived** | — |
| O9 | drop record `package_name == authored` leg | 4ef7754f2c07b317 | `ORACLE_MISCLASS=0/9` | survived (**equivalent**) | — |
| O10 | first match only for versions (`got[:1] == [val]`) | f0ae9b1d4f77f5df | `ORACLE_MISCLASS=1/9` | killed | F5 (reject→accept) |
| O11 | drop `manifest status complete` leg | debbfc228d9e75eb | `ORACLE_MISCLASS=0/9` | **survived** | — |
| O12 | drop `subject digest == fixture sha256` leg | eb7ce45f3e9f153e | `ORACLE_MISCLASS=0/9` | **survived** | — |
| O13 | O4+O9 together: record `package_name` never compared | 06b58f71941fbb57 | `ORACLE_MISCLASS=0/9` | **survived** | — |

Oracle score: 5 of 13 killed (O3, O5, O6, O7, O10); 2 equivalent (O4, O9); 6 non-equivalent survivors.
Of the six assigned mutants, O3/O5/O6 were killed and O1/O2 survived. O4 cannot be killed because it is equivalent.

### Oracle survivors and the case that kills each (all verified on pristine/mutant/restored)

| mutant | killing case (`killer-cases/<id>/case.json`, label `reject`) | pristine | mutant | failing pristine leg |
|---|---|---|---|---|
| O1 | `K-O1-root-is-application`: the good text with root `<application …>` instead of `<manifest …>` (same attrs) | `ORACLE FAIL (21/22)` | `ORACLE OK (22/22)` | `manifest text does not parse to a root <manifest> element` |
| O2 | `K-O2-attacker-root-authored-pkg-in-child`: root `package="com.attacker.fabricated"` with correct versions, child `<application package="com.example.r65"/>` | `FAIL (20/22)` | `OK (22/22)` | root package attribute; package_name vs parsed root |
| O8 | `K-O8-second-namespaced-package-on-root`: good root plus `xmlns:ns9="other" ns9:package="com.attacker.fabricated"` | `FAIL (21/22)` | `OK (22/22)` | `root package attribute ['com.example.r65', 'com.attacker.fabricated'] != authored` |
| O11 | `K-O11-manifest-status-partial`: P1 with `manifest.status="partial"` | `FAIL (21/22)` | `OK (22/22)` | `manifest status 'partial'` |
| O12 | `K-O12-subject-digest-other-apk`: P1 with `subject.digest.sha256 = 0×64` | `FAIL (21/22)` | `OK (22/22)` | `subject digest != the fixture bytes` |
| O13 | `K-O13-package_name-forged-root-true`: P1 with `normalized_result.package_name="com.attacker.fabricated"` and the true manifest text | `FAIL (20/22)` | `OK (22/22)` | both package_name legs |

Why the equivalent mutants cannot be killed: three legs relate `package_name`, the root package and `pkg`: L126
`package_name == pkg`, L139 `root_pkg == [pkg]`, L141 `package_name == root_pkg[0]`. Any two of them imply the third.
So dropping L141 (O4) or L126 (O9) alone changes no verdict. The witness `killer-cases/K-O4-equivalence-witness-F7`
shows this: on F7 the pristine oracle fails 2 legs and O4 still fails 1, so both reject. Each leg alone is redundant.
Dropping two of them together (O13) is not redundant, and no battery case catches it. That gap is the coverage finding.

## norm_eq mutants (detector: `norm_eq.py --selftest` on the mutant)

| id | mutant (assigned N1–N4; N5–N10 extra) | mutant sha16 | selftest output | verdict | killed by leg |
|---|---|---|---|---|---|
| N1 | drop V3 canonicalisation (`if False:`) | a7a04b5f91ff8764 | `NORM_SELFTEST=FAIL` | killed | volatile-only twin |
| N2 | normalise every `ev_<64hex>` substring | 472e718b11962ee7 | `NORM_SELFTEST=FAIL` | killed | evidence id leaks into a non-whole string |
| N3 | drop every key ending `_ms` | c5ed55d0deefef6d | `NORM_SELFTEST=pass` | **survived** | — |
| N4 | ignore list length (`if False:`) | c727c6f1a880c5b5 | `NORM_SELFTEST=pass` | **survived** | — |
| N5 | normalise run2 with run1's evidence id | 33ccc7ca476c0872 | `NORM_SELFTEST=FAIL` | killed | volatile-only twin |
| N6 | compare only the key intersection | d10604c854ff3279 | `NORM_SELFTEST=FAIL` | killed | extra key |
| N7 | V1 widened: any string starting `ev_` | 0cc4d350f101f10f | `NORM_SELFTEST=pass` | **survived** | — |
| N8 | V2 widened: any trailing path segment | 285a2bf1bf9b602e | `NORM_SELFTEST=pass` | **survived** | — |
| N9 | V3 keeps only the key set of JSON-text payloads | 4952b9847ab2d1c2 | `NORM_SELFTEST=pass` | **survived** | — |
| N10 | drop the `type(a) is not type(b)` check | 903f4bc3745356a8 | `NORM_SELFTEST=pass` | **survived** | — |

norm_eq score: 4 of 10 killed (N1, N2, N5, N6). Of the four assigned mutants, N1/N2 were killed and N3/N4 survived.

### norm_eq survivors and the case that kills each (`killer-cases/<id>/run{1,2}.json`; correct verdict DIFFER)

| mutant | killing pair | pristine | mutant |
|---|---|---|---|
| N3 | `K-N3-nonvolatile-timeout_ms-differs`: `timeout_ms` 1000 vs 5000 | `DIFF $.timeout_ms` (exit 1) | `NORM_EQ=identical` (exit 0) |
| N4 | `K-N4-list-gains-an-element`: `permissions` `[]` vs `["android.permission.INTERNET"]` | `DIFF $.permissions[len]` | `identical` |
| N7 | `K-N7-foreign-ev-id-field-differs`: `parent_evidence_id` ev_c… vs ev_d… | `DIFF $.parent_evidence_id` | `identical` |
| N8 | `K-N8-target-filename-differs-under-runtime`: `…/rea-android-ab12cd/a.apk` vs `…/rea-android-zz99yy/b.apk` | `DIFF $.p` | `identical` |
| N9 | `K-N9-text-payload-value-only-same-keys`: text `{"x":1,"y":2}` vs `{"y":2,"x":9}` | `DIFF $.t.<json-text>.x` | `identical` |
| N10 | `K-N10-int-vs-bool-leaf`: `class_count` `1` vs `true` | `DIFF $.class_count` | `identical` |

How the survivors bear on the real record (`reports/round-89/rejected-android-record/inspection.json`, walked read-only):
- **N3 matters in practice.** The real record carries a non-volatile `_ms` key,
  `$.raw_result.calls[1].response.content[0].text<json>.decompile_timeout_ms`, next to the volatile `load_duration_ms`.
  An `_ms` widening of V4 would silently hide a change to a producer configuration value, and the selftest would not notice.
- **N4 matters in practice.** The record has lists that could change length between runs: `raw_result.calls` (4),
  `limitations` (5), `locations` (1), `normalized_result.permissions` (0), `evidence_links` (0).
- **N9 exposes a confounded selftest leg.** The leg "non-volatile text payload value" changes the value `x:1→9` and also
  removes `load_duration_ms` from the text. A mutant that compares only the key set is therefore still caught by the key
  removal, not by the value change the leg is named for.
- The record contains no embedded or foreign `ev_` strings (N7) today, so N7 and N8 are latent widenings.

## Proposals (report only; the frozen instruments and batteries were not edited)

1. Oracle battery: add reject cases equivalent to K-O1, K-O2, K-O8 and K-O13. These are manifest-leg forgeries the v2
   design claims to stop, and the battery does not exercise them. K-O11 and K-O12 (identity/status legs) are lower
   priority because C2's stated v2 delta is the manifest legs.
2. norm_eq selftest: add legs equivalent to K-N3 (a non-volatile `*_ms` key, e.g. `decompile_timeout_ms`), K-N4 (list
   length), K-N9 (a value-only change inside a JSON-text payload with the same key set; this replaces or splits the
   confounded leg), K-N7, K-N8 and K-N10.
3. None of the survivors shows that the v2 instruments misjudge the actual round-90 inputs. Each one is a defect that the
   frozen detectors (the battery and the selftest) would not catch. The C2 kill rules (a) and (b) are only as strong as
   these detectors.

## Cleanup

Receipts are copied into this directory. The scratch dir `/fast/scratch/hyaku/revenger-r90/MutR90Oracle` is deleted
before yield. No lane bytes were changed outside `.ufo/waves/round-90/w1/MutR90Oracle/` and `.ufo/waves/round-90/w1/MutR90Oracle.md`.

VERDICT: C2 instruments are partially mutation-adequate. Oracle 5/13 killed (2 equivalent; O1, O2, O8, O11, O12, O13 survive and each has a verified killing case). norm_eq 4/10 killed (N3, N4, N7, N8, N9, N10 survive and each has a verified killing case). The detectors are under-covered; no frozen verdict was refuted.
