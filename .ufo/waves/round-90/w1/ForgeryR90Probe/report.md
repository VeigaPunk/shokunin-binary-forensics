# ForgeryR90Probe — round 90 w1: forgeries against oracle v2

Hypothesis tested: *"oracle_check2 accepts no record whose root manifest misstates the fixture package or versions."*

**VERDICT: falsified by N17-x-package-only.** The root has no unprefixed `package` attribute, only `x:package` in `urn:evil`, and the oracle accepts it at 22/22. Six more root-manifest misstatements also get green verdicts: N04, N18, N25, N26, N27 and N31.

## Setup
- Lane HEAD is `c7767789fe9e96bcc0d50656ad4bdce69ba3a3a9`, the freeze commit. `git status` shows no changes under `corpus/fixtures/apk-r65` or `reports/round-90/oracle-battery-cases`.
- Oracle: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65/oracle_check2.py`, sha256 `de2b2ad2…e666d` (in `pins.log`, matches `reports/round-90/instrument-pins.log`).
- Source record: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-90/oracle-battery-cases/P1-real-r89-record.json`, sha256 `26093baf…8b1`.
- Each case is P1 with one change. Unless stated otherwise, the change is to `normalized_result.manifest.text` only. Each case was scored with `python3 -B …/oracle_check2.py …/truth.json <case>` (Python 3.14.8).
- Generator: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ForgeryR90Probe/gen.py`.
- Case files and per-case oracle logs: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ForgeryR90Probe/cases/` (40 `.json` files and 40 `.oracle.log` files).
- Table receipt: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ForgeryR90Probe/results.tsv`.
- Tools: nothing installed or upgraded.

## Ground truth used for labels
`truth.json` gives the fixture's AXML attributes as follows:
- `package`: `ns_idx=0xFFFFFFFF`, which means no namespace.
- `versionCode` and `versionName`: `ns_idx=0`, which is string 0, the literal URI `"android"`. This is why jadx emits `xmlns:ns1="android"`.
- The root element is the unnamespaced `manifest`.

A case is labelled `yes` (misstates) if it gives a different value, gives no value, or puts the attribute or element in a namespace other than the fixture's. That includes `urn:evil` and namespaces Android ignores.

A case is labelled `strict` if it misstates only under exact namespace or DTD semantics. The disagreement may be debatable in those cases.

## Results (40 cases)

| case | what it does | misstates? | oracle | result |
|---|---|---|---|---|
| N01 | DOCTYPE internal entity `&p;` → true pkg | no | ACCEPT 22/22 | ok |
| N02 | entity → `com.attacker.x`; package_name is true | yes | REJECT 20/22 | ok |
| N03 | no `package` attribute in the tag; DTD `ATTLIST` default supplies it | strict | ACCEPT 22/22 | **FALSE-GREEN (strict)** |
| N04 | root has no versions; DTD `ATTLIST` defaults add unnamespaced `versionCode="1"` and `versionName="1.0"` | yes | ACCEPT 22/22 | **FALSE-GREEN** |
| N05 | literal package fabricated, DTD `#FIXED` value is true | yes | REJECT 20/22 | ok |
| N06 | `SYSTEM` external entity for package | yes | REJECT 17/22 (does not parse) | ok |
| N07 | `package=" com.example.r65 "` | yes | REJECT 20/22 | ok |
| N08 | raw trailing newline in package (normalised to a space) | yes | REJECT 20/22 | ok |
| N09 | `&#10;` in package | yes | REJECT 20/22 | ok |
| N10 | trailing space in both root package and package_name | yes | REJECT 20/22 | ok |
| N11 | `versionCode=" 1"` | yes | REJECT 21/22 | ok |
| N12 | `&#99;om.example.r65` | no | ACCEPT 22/22 | ok |
| N13 | `&#x31;` / `1&#46;0` versions | no | ACCEPT 22/22 | ok |
| N14 | PI carries the true manifest; root fabricated | yes | REJECT 18/22 | ok |
| N15 | true root; trailing PI with a fabricated manifest | no | ACCEPT 22/22 | ok |
| N16 | second root element after the true root | yes | REJECT 17/22 (does not parse) | ok |
| N17 | **`xmlns:x="urn:evil" x:package="com.example.r65"`, no unprefixed `package`** | yes | ACCEPT 22/22 | **FALSE-GREEN** |
| N18 | only `android:package` (schema URI) | yes | ACCEPT 22/22 | **FALSE-GREEN** |
| N19 | plain package fabricated + `x:package` true | yes | REJECT 20/22 (two `package` values) | ok |
| N20 | U+FEFF BOM before the XML declaration | no | ACCEPT 22/22 | ok |
| N21 | BOM inside package value, package_name the same | yes | REJECT 20/22 | ok |
| N22 | trailing U+200B in package and package_name | yes | REJECT 20/22 | ok |
| N23 | CDATA child holds the true manifest; root fabricated | yes | REJECT 18/22 | ok |
| N24 | true root; CDATA child with fabricated text | no | ACCEPT 22/22 | ok |
| N25 | root `<x:manifest xmlns:x="urn:evil">` | yes | ACCEPT 22/22 | **FALSE-GREEN** |
| N26 | root `<manifest xmlns="urn:evil">` (default namespace) | yes | ACCEPT 22/22 | **FALSE-GREEN** |
| N27 | root `<android:manifest>` | yes | ACCEPT 22/22 | **FALSE-GREEN** |
| N28 | `versionCode="01"` | yes | REJECT 21/22 | ok |
| N29 | `versionCode="0x1"` | yes | REJECT 21/22 | ok |
| N30 | unnamespaced `versionCode` / `versionName` | strict | ACCEPT 22/22 | **FALSE-GREEN (strict)** |
| N31 | `e:versionCode` / `e:versionName` bound to `urn:evil` | yes | ACCEPT 22/22 | **FALSE-GREEN** |
| N32 | `android:versionCode` with the schema URI (the fixture binds `"android"`) | strict | ACCEPT 22/22 | **FALSE-GREEN (strict)** |
| N33 | `<Manifest>` | yes | REJECT 21/22 | ok |
| N34 | `Package=` | yes | REJECT 20/22 | ok |
| N35 | `ns1:versioncode` | yes | REJECT 21/22 | ok |
| N36 | `com.Example.r65` in root and package_name | yes | REJECT 20/22 | ok |
| N37 | text is true; `normalized_result.version_code="99"`, `version_name="9.9"` | yes (record, not root) | ACCEPT 22/22 | **FALSE-GREEN (adjacent)** |
| N38 | text is true; `raw_result` `get_app_info` says `com.attacker.x` 9.9/99 | yes (record, not root) | ACCEPT 22/22 | **FALSE-GREEN (adjacent)** |
| N39 | true root + nested child `<manifest package="com.attacker.x" versionCode="9">` | no (root is true) | ACCEPT 22/22 | ok |
| N40 | XML declaration says `utf-16`, bytes are UTF-8 | no | REJECT 17/22 (does not parse) | false-red (harmless) |

Totals:

| result | count | cases |
|---|---|---|
| ok | 27 | |
| FALSE-GREEN | 9 | 7 in the hypothesis's root-manifest scope: N04, N17, N18, N25, N26, N27, N31. 2 adjacent record fields: N37, N38 |
| FALSE-GREEN (strict) | 3 | N03, N30, N32 |
| false-red | 1 | N40 |

## Root causes in `oracle_check2.py`
1. **No namespace check on any leg.** `local = lambda k: k.rsplit("}", 1)[-1]` is applied to the root tag and every attribute key. The docstring makes versions accept any namespace on purpose, because the producer binds literal `"android"`. The same stripping also applies to `package` and to the root tag, which the docstring describes as "attribute `package`" and "local tag `manifest`".
   - So `{urn:evil}package` passes as the package (N17, N18).
   - `{urn:evil}manifest` passes as the root (N25, N26, N27).
   - Versions in any foreign namespace, or in none, pass (N31, N30, N32).
2. **DTD defaults are taken as declarations.** expat (through `xml.etree.ElementTree`) reports attributes defaulted by an internal-subset `ATTLIST` as if they were written on the element (N03, N04). `DOCTYPE` is not rejected.
3. **Record fields the oracle never checks.** `normalized_result.version_code`, `version_name`, `min_sdk` and `target_sdk`, and all of `raw_result`, are never compared (N37, N38). These sit outside the manifest-text hypothesis but are still record misstatements.

What the oracle gets right: whitespace, BOM and zero-width characters, character references, PIs, CDATA, second roots, comments, `01`/`0x1`, and case variants are all handled correctly. Every value comparison is exact on the decoded string.

## Proposed v3 changes
Proposals only. No frozen instrument was edited.
- Require the root tag to be exactly `"manifest"`, with no `{ns}` part.
- Require `package` to be exactly the unnamespaced key `"package"`.
- Require `versionCode` and `versionName` to be in the namespace the fixture's AXML gives: `{android}` (strings[ns_idx]). The other option is the set {`android`, the schema URI}, chosen and declared before data.
- Reject any text containing `<!DOCTYPE`, using `parser.StartDoctypeDeclHandler` or a pre-scan.
- Optionally require `normalized_result.version_code` and `version_name` to be null or equal to the authored values.

Frozen battery follow-up: none of N17, N25, N26, N31 or N04 is among the 9 frozen cases. F5 uses an `other` namespace but also changes the value, so it does not exercise these paths. Kill rule (a) only covers frozen battery cases, so it is not triggered. These gaps are new coverage for a later battery.
