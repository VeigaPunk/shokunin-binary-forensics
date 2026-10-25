FAIL — Q05 on this entry: the derivation script's *refusal* capability ("a missing or ambiguous symbol is exit 2", :127, restated at :6 and :9) is credited three times with no probe of that branch — all 17 embedded `$ ` blocks are exit-0 success runs — and on the committed snapshot the advertised symbol guard is unreachable anyway, because the digest pin fires first (:107-108).

entry under test: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-69-apk-axml-byte-evidence.md`
sha256 `c1e7eaac9dba4c77e578c788755dec3e3499fd8795ad0e479c51b5be7deb11d5`, 215 lines, `admission-status: candidate`.
Criterion judged: Q05 only (`corpus/QUALITY.md:25`; operative text incl. "the derivation script may be credited only as an own-work instrument whose output is demonstrated"). The entry's own §Q-map Q05 row (:180) was not used as evidence for this verdict.

## 1. The claim Q05 has to cover

- `:127` — "The script refuses to print a line it did not find (**a missing or ambiguous symbol is exit 2**), and it reads `corpus/snapshots/ResourceTypes.h`…"
- `:9` (`recheck:`) — "`python3 -B corpus/derive_axml_anchors.py` from the lane root (…; **exits 2 if a cited symbol is missing or ambiguous**)"
- `:6` (`source: S047`) — "… 20 output lines over `corpus/snapshots/ResourceTypes.h` sha256 `56b88bc4…` (**exit 2 on a missing or ambiguous symbol**)"

That is a behavioural capability of an instrument, stated in the entry's header *and* its body. Q05's positive requirement is "its command, date and observed exit, output"; the derivation-script clause restricts the credit to output that is demonstrated. Neither is met for this clause.

## 2. What the entry actually demonstrates (only the success path)

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-69-apk-axml-byte-evidence.md; echo "checker_exit=$?"
checked_blocks=17 problems=0
checker_exit=0
```
```
$ grep -n '^\$ ' corpus/knowledge/round-69-apk-axml-byte-evidence.md
26/33/40/42/44/55/64/73/80/87/94/101/103/112/121,199  python3 -B corpus/fixtures/apk-r65/readout.py [--fact …]
130  python3 -B corpus/derive_axml_anchors.py
```
```
$ grep -n "EXIT=\|exit=\$\|; echo" corpus/knowledge/round-69-apk-axml-byte-evidence.md
(no output — no exit-code receipt is embedded anywhere)
```
17 blocks, every one a success-path invocation. The single derivation block (:130) is the 20-line table only; no exit code, no negative input. The two positive runs do reproduce, and the embedded 20 lines are byte-identical to live stdout:
```
$ diff -u <entry lines 131-150> /tmp/revenger-r69-q05-derive.txt  → IDENTICAL
$ python3 -B corpus/fixtures/apk-r65/readout.py | wc -l → 15 ; sha256 of stdout → 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247 (matches :9, :194)
$ sha256sum corpus/derive_axml_anchors.py corpus/snapshots/ResourceTypes.h corpus/fixtures/apk-r65/readout.py corpus/fixtures/apk-r65/fixture.apk
74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa  corpus/derive_axml_anchors.py
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk
```
(All four match the digests the entry states at :6 (derive script + snapshot), :7 (readout + fixture), :19 (readout sha) and :23 (fixture sha). The value leg of the claim is fine; the capability leg is not.)

## 3. Counterexample — I probed the advertised branch; it is real, unprobed, and unreachable as advertised

Scratch copies only (`/tmp/revenger-r69-q05-probe*`), lane files untouched:

(a) committed snapshot restored, **mutated snapshot** (one byte appended), pin intact:
```
$ python3 -B derive_axml_anchors.py ; echo EXIT=$?
derive_axml_anchors: snapshot digest 34d43d5b42f952402c67107b892559e90946c2b23f9386d616ff19391c545320 != pinned 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f
EXIT=2
```
(b) symbol renamed away, **pin re-pointed to the mutated bytes** (the only way past the digest guard):
```
derive_axml_anchors: enum RES_STRING_POOL_TYPE: not found
EXIT=2
```
(c) enum line duplicated, pin re-pointed:
```
derive_axml_anchors: enum RES_XML_RESOURCE_MAP_TYPE: ambiguous (2 hits at [253, 254])
EXIT=2
```
Findings:
1. The not-found/ambiguous guards exist and do refuse (`derive_axml_anchors.py:74-80`, `:98`), and emit **no partial table** (`:130` prints only at the end). The claim is *true*.
2. It is unprobed in the entry — the branch is never run there (§2).
3. It is unreachable *as described*: against the committed snapshot, every mutated input exits 2 at the digest pin (`:107-108`), never at the symbol guard. So `:127`'s clause names the symbol guard as the operative protection when the guard that actually protects the table from a mutated snapshot is the digest pin. Correct value: "a mutated or substituted snapshot exits 2 at the digest pin (`derive_axml_anchors.py:107-108`); the symbol not-found/ambiguous guards (`:76-79`) are reachable only with the pin re-pointed (probe: `enum RES_STRING_POOL_TYPE: not found`, exit 2)."

## 4. Lineage: this is round-68's Q05 leg 2, unfixed

`.ufo/waves/round-68/R68ReviewEntryQ05.md:110-131` ruled the identical sentence (then `entry:125`) "**true but unprobed**" and prescribed the repair verbatim: "the repair is to embed one of these runs (command + observed exit 2 + its one-line stderr/stdout message) in item 11, not to retract anything." v4's item 11 (:127-150) still contains the success run only, so that leg survives unchanged; only round-68's *first* Q05 leg (17-line table missing `237`/`244`) is repaired — v4 derives both (:139, :142), and all 19 cited S038 numbers appear in the 20-line output (`218,237,239,241,244,245,246,247,248,253,263,287,461,612,621,677,686,687,707`), so the completeness sentence at `:127` is now accurate for S038.

## 5. Gate interaction that constrains the repair

`corpus/check_embedded_outputs.py:101-102` treats any `$ ` block with `rc != 0` as drift (`drift entry:{lineno} command exited {rc}`). So the round-68 prescription cannot be satisfied by adding a `$ `-prefixed exit-2 block: the registered gate would reject the entry. The probe must either be embedded outside a `$ ` block (and named as not covered by that checker, per Q13), or the claim must be withdrawn.

## 6. Smallest safe correction

Option A (fewest bytes, keeps every measured value): delete the capability clause.
- `:127` → "…is printed by a committed derivation script that searches the pinned snapshot bytes for each cited symbol — no spec line number in this entry is transcribed by hand. The credit is bounded to exactly the numbers the command prints: the 20-line stdout below … is the complete set of S038 line numbers this entry states:" (drop "The script refuses … exit 2"), or restate as code-structure presence explicitly not exercised: "a missing or ambiguous symbol is a hard error in the script's own logic (`derive_axml_anchors.py:76-79`); this entry did not exercise that branch."
- `:6` → drop "(exit 2 on a missing or ambiguous symbol)".
- `:9` → drop "exits 2 if a cited symbol is missing or ambiguous".
Option B (keeps the guarantee): add a non-`$` probe block after the 20-line table — the command (scratch copy with pin re-pointed), the observed one-line message, `EXIT=2` — plus the pin-ordering sentence from §3(3), and say the block is not re-run by `check_embedded_outputs.py`. Note B also changes no script byte (probe lives in the entry), so `S047`'s `74d4c0d9…` pin stays valid.

Recommended: A if the wave must land without a gate change; B if the hard-error guarantee is to be kept.

## 7. What Q05 does pass here (so the FAIL is narrow, not a blanket reject)

- Provider readiness leg does **not** fire: `:169-171` fences `inspect_android_package` to S043 documentation scope ("this lane ran no provider and makes no readiness claim"), and no producer/output capability is asserted anywhere.
- Both owned instruments are probed at the success surface with command + date + output: readout (exit 0, 15 lines, stdout sha256 reproduced) and derivation (exit 0, 20 lines, byte-identical).
- `:15` ("Nothing is extracted to disk, nothing is executed, no producer is called, no network is used, and no verifier source is read") and `:163` ("no producer was called") are process fences, not readiness claims; `readout.py:13-18` imports only `hashlib, json, struct, sys, zlib, pathlib`, consistent with them (unprobed in the entry, but not a Q05 capability claim).

## 8. Axes touched

- **coverage (C1)**: a Q FAIL on these landed v4 bytes is exactly C1's kill-rule trigger (`claims.md` §C1: "Any Q FAIL on the v4 bytes … → … C1 is reported FALSIFIED"). Adjudication is Main's; as the Q05 seat I report the FAIL on the current bytes. A pre-measurement repair (§6) is the only route that keeps C1 alive, and it is a three-line withdrawal — no measured value changes.
- **calibration (C2)**: unaffected by this verdict; the D1/Q15 surface was not touched here.
- Q11/Q13 boundary note (not my criterion): `:127`'s exit-2 clause is also a verifier-credit clause that `check_embedded_outputs.py` cannot detect (it never runs a failing input), i.e. unguarded.

## 9. Housekeeping

- No files edited in the lane; the only write is this report. Scratch under `/tmp/revenger-r69-q05-*` is deleted.
- No tool installed or upgraded (none needed; Python stdlib and the lane's own scripts sufficed). Pacman untouched.
