Q07 PASS — no parser-behavior prediction is written as fact and no unreproduced cause is used as support; every load-bearing sentence describes observed bytes, labeled inference, or authored-construction fact.

Seat: R67ReviewEntryQ07 (fresh, non-author). Entry under test: /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-67-apk-axml-byte-evidence.md (committed v2 candidate bytes, admission-status: candidate at entry:8). Criterion text applied verbatim from /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/QUALITY.md:19 — Q07 rejects when "a prediction is written as fact, or an unreproduced cause is used as support" (M07, M12).

## Sweep for predictive/causal language

Grep for `\b(would|will|accept|refus|reject|invalid|valid|parses|parser|cause|because|therefore|hence|predict)\b` over the entry returns hits only at lines 6, 7, 8, 134, 150, 151 — all fences, procedure, or self-referential Q-map text. None predicts what any parser (AOSP, JADX, `inspect_android_package`, ZIP reader, dex verifier) would accept or refuse.

## Closest calls examined and cleared

- entry:7 coverage-map and entry:134 Limitations fence OUT "general AXML or ZIP-parser behavior", "dex validity or execution", and provider output — the opposite of a prediction.
- entry:74 explicitly declines semantics: "the all-zero entries are recorded as observed, and no framework-wide semantics for a zero entry is claimed from this fixture" — the canonical M07/M12-avoidant phrasing.
- entry:67 "the UTF-8 flag position the readout tests (`flags & 0x100`, readout.py:166)" — attributes the constant to the reader's own test and to the spec-defined flag; it does not assert how any external parser reacts. The strings that follow are "decoded ... from the offsets the pool states" (observed decode, entry:71 output).
- entry:81 "so attribute *i* is at `chunk_base + 16 + attributeStart + i * attributeSize`" — derivation from S038's quoted field semantics ("Byte offset from the start of this structure where the attributes start"), and the values so derived match the embedded output at entry:85; a spec-derived reader invariant, not a predicted parser outcome.
- entry:106 tail "These are declared-header self-consistency facts about one inert member; dex validity is not claimed" — scopes the checksum/signature agreements to declared field semantics; no runtime acceptance is asserted.
- entry:45 "the round-65 draft recorded a 15-byte `4d616e696673742d…` pair at its entry:41; the deriving command prints the 16-byte pair" — a repair note about a committed retained artifact (the r65 candidate keeps its drifted entry:41 as the C7 red-before surface per reports/round-67/claims.md:96-98); attested history, not an unreproduced cause supporting the finding.
- entry:129 labels all spec-correspondence as **Inference** with anchors; entry:128 labels all values **Observation**; entry:130 labels the rest **Unknown** — the separation the criterion exists to protect.
- entry:150 Q-map row claims Q07 pass on exactly this ground; consistent with the body.

## OFF-criterion defects noticed (not Q07)

- OFF- entry:88 vs entry:85: "the same constant on `android`-carrying attributes resolves instead through the start-namespace chunk" reads as if the `android`-carrying attributes also carry `0xffffffff`; the embedded output two lines above shows `versionCode`/`versionName` carry `ns_index: 0` (resolved to `"android"`), while `package` and the element carry `4294967295`. "The same constant" is contradicted by the entry's own quoted stdout — phrasing defect, clarity/accuracy class not Q07.
- OFF- entry:134 vs entry:106/:130: the entry twice says dex validity "is not claimed" then asserts the member "is intentionally not a valid dex program". The assertion is authored-construction grounded (file_size 112 == header_size 112 leaves zero bytes for the mandatory id sections S045's file layout lists) and runs the conservative direction (disclaiming coverage), so I do not score it a Q07 failure — it is not used as support and is framed as design intent — but it is an internal fence inconsistency: a validity-flavored claim inside a fence that disclaims validity claims.

## Verdict basis

No accept/refuse/cause prediction appears anywhere as fact; the single validity-flavored sentence (entry:134) is authored-intent about the fixture's own construction, grounds in S041 own-work plus S045's file layout, and is used only to limit scope. Q07's two reject clauses both miss. PASS.

No tools installed (none needed: read + grep sufficed).
