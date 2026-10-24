NOT-FALSIFIED — no sentence in the entry escapes both fixture-anchoring and the §Limitations/coverage-map fences; every generalization-capable sentence is either spec-sourced (S032/S034/S038), explicitly labeled Inference, or grammatically bound to this fixture, and §Limitations:131 explicitly names the exact generalization axes the seat brief probes (other APKs, other AXML producers, `inspect_android_package` provider).

# Scope-fence attack — corpus/knowledge/round-65-apk-axml-byte-evidence.md

Target axes per brief: parser behavior, other APKs, AXML producers, provider output. Fences available to the entry: coverage-map "Not covered" list (line 6), §Limitations (line 131), §Cross-lane scope note (line 135), §Observation/inference/unknown split (lines 125-127). Read all 162 lines of the entry.

## Risky sentences found and adjudicated

1. `round-65-apk-axml-byte-evidence.md:5` (recheck field): "the stdout carries only repo-relative paths, never the extraction root, so the same bytes give the same 15 lines from any checkout of the same commit."
   - Generalization: determinism across *any* checkout/host — beyond the single observed run on this host.
   - Rescue: PARTIAL. Not named in §Limitations' axis list, but this is the recheck contract itself (Q02 requires a re-runnable command + output digest); the claim is hedged to "the same bytes" and is about the readout script's determinism, not APK/parser semantics. Not an escape on the brief's axes.

2. `round-65-apk-axml-byte-evidence.md:71`: "Seven entries are `0x00000000` — S038's `ResXMLTree::getAttributeNameResID` semantics make 0 'no resource id' — and the entries for `versionCode` and `versionName` are **`0x0101021b`** and **`0x0101021c`**, the framework attribute ids the fixture declared"
   - Generalization: "the framework attribute ids" reads as a universal framework-id claim (0x0101021b IS versionCode's public attr id in Android generally); the entry's evidence is only the fixture generator's own declaration — S038 (ResourceTypes.h) does not assign public attribute ids.
   - Rescue: YES, but thin. The trailing qualifier "the fixture declared" grounds it in the authored oracle, and §Inference (line 126) re-lists exactly this as inference citing "the fixture generator declared". §Limitations:131's "other APKs ... would need its own evidence" covers any reader extension to real APK manifests. Closest thing to an escape; the "the fixture declared" tail is load-bearing — deleting it would make this sentence a FAIL.

3. `round-65-apk-axml-byte-evidence.md:103`: "Its declared checksum **`0x3d120c30`** equals the Adler-32 recomputed over the bytes from offset 12 on, and its declared 20-byte signature equals the SHA-1 recomputed over the bytes from offset 32 on."
   - Generalization: states the dex checksum/signature offset rule (Adler-32 from +12, SHA-1 from +32) — a general dex-format rule — with no external dex spec among the entry's sources (S038 is AXML; S032/S034 are ZIP).
   - Rescue: YES. Grammatically fixture-anchored ("Its declared checksum"), framed as a measured equality not a format rule, and coverage-map (line 6) scopes to "the `classes.dex` declared header" while §Limitations:131 declares the member "a header only ... intentionally not a valid dex program". A reader generalizing the offsets does so against an unsourced spec fact the sentence never asserts as general.

4. `round-65-apk-axml-byte-evidence.md:46`: "The child chunks are walked from offset 8 by adding each chunk's size, and the walk ends exactly at 416"
   - Generalization: chunk-walk-by-size is general AXML structure.
   - Rescue: YES — describes the readout's method on this payload and terminates in a fixture measurement ("ends exactly at 416"); the underlying `size` field semantics are S038-anchored via item 5 (line 55-62).

5. `round-65-apk-axml-byte-evidence.md:85`: "The `0xffffffff` namespace index on `package` and the element itself is the `ResStringPool_ref` null index"
   - Generalization: null-index semantics are spec-general.
   - Rescue: YES — attributed to the S038 type name and explicitly enumerated as Inference at line 126 ("that `0xffffffff` is the null string-pool index ... Each inference cites its byte evidence and its S038 anchor").

6. `round-65-apk-axml-byte-evidence.md:53`: "The six chunk types — `0x0001` string pool ... — are the values S038's chunk-type enum names at lines 239-250."
   - Generalization: type-value mapping is spec-general.
   - Rescue: YES — direct pinned-spec attribution with line anchors; re-flagged as Inference at line 126.

7. `round-65-apk-axml-byte-evidence.md:55`: "The fixed structure widths used by the readout are computed by summing the field widths of S038's own struct definitions ..., not assumed"
   - Generalization: struct widths are spec-general.
   - Rescue: YES — derived, attributed, and labeled inference.

8. `round-65-apk-axml-byte-evidence.md:11`: "The ZIP container field offsets are the APPNOTE 6.3.10 fixed record widths already mined as S032 (central directory header) and S034 (local file header)"
   - Generalization: APPNOTE fixed widths are spec-general; S032/S034 are prior corpus entries, not the spec itself.
   - Rescue: YES — registry-attributed spec widths; also the fixture walk's specifics (ZIP_STORED, no data descriptors) are fenced at §Limitations:131.

9. `round-65-apk-axml-byte-evidence.md:33`: "(46-byte fixed part per S032 §4.3.12)" — spec-sourced parenthetical; rescued by attribution. Same shape as #8.

10. `round-65-apk-axml-byte-evidence.md:135`: "The provider route (`inspect_android_package`, JADX prerequisites) is documented scope from S039 only; this lane ran no provider and makes no readiness claim (Q05 fence)."
    - Generalization risk: would-be provider-output claim — instead it is the fence itself. No escape.

## Sentences checked and cleared as fixture-anchored (sample)

- :19 archive size/digest; :26 EOCD offset arithmetic; :37-41 member facts; :64, :68 string-pool contents; :75 resource-map ids; :78, :82 attribute rows; :89, :96, :98 namespace/element chunks; :107 dex header facts; :116 MANIFEST.MF; :121 regeneration "on this host, Python 3.14.8" — all bound to named bytes/offsets of this one fixture.
- :131 §Limitations is itself well-formed: "One authored fixture, one manifest shape ... UTF-8 string pool only, no CDATA, no nested elements, no styles ... ZIP_STORED with no data descriptors ... Generalization to other APKs, other AXML producers or the `inspect_android_package` provider would need its own evidence." — names every axis the brief attacks.
- :6 coverage-map "Not covered: install/signature verification, dex validity or execution, provider ... readiness or output, general AXML or ZIP-parser behavior beyond this fixture." — the parser-behavior axis is fenced here even before §Limitations.
- Q-map :147 Q07 "no parser-behavior prediction is made or needed" is consistent with the body: every general-looking sentence is spec attribution, not parser prediction.

## Verdict basis

Strongest counterexample is #2 (framework attribute ids): the universal reading exists, but the sentence's own qualifier plus the §Inference enumeration and §Limitations axis list keep it inside the fence. #3 (dex offset rule) is the runner-up — a real spec fact asserted without a dex-spec source, rescued by fixture-anchored phrasing and the declared-header scope; noted for Q01/Q09 reviewers as the least-supported general rule in the entry, but not a scope escape. No sentence escapes both anchoring and §Limitations → the seat's FAIL condition is not met.

Smallest safe correction (optional, non-blocking): in :103 add "(the declared-header field layout the oracle records)" or similar to make the fixture-anchor explicit rather than grammatical; in :71 keep "the fixture declared" verbatim — it is load-bearing.
