Q10 PASS — finding is scoped to the observed fixture/operation/version/input, and the contested cross-lane scope (ADJ-06, fleet l0-questions.md:42) is reported-not-absorbed; no observation is stated as a universal.

Criterion: `corpus/QUALITY.md` Q10 — "A finding is scoped to the observed family, operation, version and input. Cross-lane contested scope is reported, not absorbed. Reject when one family's observation is stated as a universal."

Entry under test: `corpus/knowledge/round-67-apk-axml-byte-evidence.md` (committed, `admission-status: candidate`, 187 lines). Decided on the committed bytes; I am not the author.

## Evidence — scope bounded

- Family/version/input pinned: header pins S038 to a named AOSP tag (`android-15.0.0_r1`, :1), S045 to a sha256-pinned snapshot (`.ufo/waves/round-67/source-snapshots/dex-format.html`, :3), S043 to `rea-agents-6.5.0` doc scope (:2), fixture/readout to sha256 pins (:4). `verified-at:` 2026-10-24 (:5).
- `coverage-map:` :7 — "one authored APK fixture … **Not covered:** install/signature verification, dex validity or execution, provider (`inspect_android_package`) readiness or output, general AXML or ZIP-parser behavior beyond this fixture."
- Scope :12 — one authored APK + authored oracle; analysis manual; "Nothing is extracted to disk, nothing is executed, no producer is called, no network is used, and no verifier source is read."
- §Limitations :134 — "One authored fixture, one manifest shape (a single element with three attributes), UTF-8 string pool only, no CDATA, no nested elements, no styles. … ZIP_STORED with no data descriptors … The dex member is a header only and is intentionally not a valid dex program. **Generalization to other APKs, other AXML producers or the `inspect_android_package` provider would need its own evidence.**"
- §Unknown :130 — "nothing about install validity, signature blocks, dex program validity or any provider's behavior is claimed; the fixture is inert and no producer was called."
- Inference bullet :129 — "each [inference] cites its byte evidence and its registry anchor, and each is scoped to this fixture."

## Evidence — no universal claim

- Items 1-10 (:16-:120) report only observed per-fixture values, each with its deriving `$ …` command block.
- Item 7 :74 — "the all-zero entries are recorded as observed, and **no framework-wide semantics for a zero entry is claimed from this fixture**." Explicitly declines the universal.
- Item 9 :106 — "These are declared-header self-consistency facts about **one inert member**; **dex validity is not claimed**."
- Item 3 :34 — `payload_offset` described as "derived by the readout … from the S034 §4.3.7 field list (readout.py:99-105), not assumed" — an operation-scoped derivation, not a universal ZIP law.
- Sweep for universal phrasing (`all/every/any APK`, `universal`, `in general`, `all providers`, etc.) across all non-output prose lines returned no match.

## Evidence — cross-lane contested scope reported, not absorbed

- `## Cross-lane scope note (Q10)` :136-:138 — "The provider route (`inspect_android_package`, JADX prerequisites) is documented scope from S043 only; this lane ran no provider and makes no readiness claim (Q05 fence). The kaidoku/revenger ADJ-06 overlap and fleet `l0-questions.md:42` remain **reported-not-absorbed, unchanged from round 64**."
- Pointer verified: `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:42` is verbatim the open ADJ-06 question — "… arbitrate the kaidoku/revenger shipped-artifact overlap before an ADJ-06 analysis is routed? … RE questions stay with the protocol integrator …" (read directly).
- Convention consistent: `SHONEN.md:23` and the retained round-64 (`corpus/knowledge/round-64-firmware-region-byte-evidence.md:203` "Reported, not absorbed") / round-65 (`corpus/knowledge/round-65-apk-axml-byte-evidence.md:135`) entries use the same stance; the v2 entry preserves it rather than absorbing the scope.
- Q-map row :153 — "Q10 | pass | scope is one fixture, one operation (manual readout), one artifact version; the §Limitations and §Cross-lane scope note name what is not claimed." Self-declared reason is accurate.

## OFF-criterion defects noticed
- OFF-1: none. (Spot-checks that also passed while auditing scope — res_id decimals 16843291/16843292 == 0x0101021b/0x0101021c; `payload_first16_hex` `4d616e69666573742d56657273696f6e` == "Manifest-Version" 16 bytes, the M39 repair; AXML chunk walk 8→204→248→272→368→392→416 sums exactly to the member size; S038 snapshot `.ufo/waves/round-65/source-snapshots/ResourceTypes.h` has `RES_STRING_POOL_TYPE` at :239 and `RES_XML_RESOURCE_MAP_TYPE` at :253, matching the claimed enum span 237-253. These are Q11/Q01 territory but are consistent.)

## Tooling
- No tools installed or updated. Standard `python3`, `awk`, `grep`, `sed` only. Pacman not touched (host-wide pause honored).

Verdict: **Q10 PASS**.
