FAIL — lesson `corpus/lessons/round-65.md` survives its three attack prongs on substance (quotes verbatim and ≤25 words, M38 row complete with a real red receipt, wave-prep claim consistent with the spec + validated plan), but carries a fixable location defect: two of three Gate quotes carry wrong line pointers (S038 off-by-one range, S039 wrong line), and S040's word-count annotation is wrong (16 claimed, 14 actual).

Scope of review: read-only attack on `corpus/lessons/round-65.md` (sha-grounded, 42 lines) against (a) Gate quotes ≤25 words + located, (b) M38 fix row = evidence + captured-by + fix shown able to fail, (c) wave-preparation claim vs `.ufo/waves/round-65/wave-spec.json` existing and validated. Impacted axes if defects stand: calibration (annotation accuracy); coverage unaffected.

## Prong 1 — Gate quotes: verbatim, ≤25 words, but two locations wrong

Convention (fleet rule, `corpus/lessons/round-63.md:33-34`, `round-62.md:60`): each located quote ≤25 words, verbatim against the pinned snapshot; whitespace normalized, not words. All three quoted rows pass both hard gates:

- S038 (lesson:12): quote is verbatim in `source-snapshots/ResourceTypes.h` — snapshot sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f` matches the lesson's recorded digest. `grep -n` places "It is followed by a flat array" at line 607 and `RES_XML_START_ELEMENT_TYPE` (sentence continues onto line 610) at 609. **Counted words: 23 — matches the claimed "(23 words)".** Quote ends mid-sentence; the source continues "and corresponding RES_XML_END_ELEMENT_TYPE nodes in the array" (lines 609-610). Truncation is verbatim-faithful; acceptable but cuts a sentence.
- **DEFECT (location): lesson:12 cites "lines 608-611". The quoted span is lines 607-609** (the comment block `/**` starts 605; `struct ResXMLTree_header` opens line 612). The pointer's start line (608) is mid-quote and end line (611) is `*/` — off-by-one at both ends. The quote is located, but not where the lesson says.
- **DEFECT (location): lesson:13 cites "line 5" for the S039 quote. `grep -n inspect_android_package rea-android-applications.md` → line 7; the quote spans lines 7-8** ("...for package / identity, manifest declarations, coverage, and inline Evidence. Use"). Line 5 is "older server." — inside the preceding paragraph. Verbatim quote (18 words incl. the code span, under 25) confirmed by `sed -n '7,8p'`.
- S040 (lesson:14): quote present verbatim, twice, in `zipfile-docs.html` (sha256 `e7fe6715126a3be8e6ea7ca4d3dc2d8713b6c979bde13f8fa9d6c458a3c49c6a`, matches). **Counted words: 14 — lesson claims "(16 words)".** Under the 25-word cap either way, so the gate holds; the annotation itself is inaccurate (calibration nit, same class the round's own M38 polices: stated-from-intent numbers).
- S041 (lesson:15): own-work bundle, no quote — consistent with prior rounds treating own-work rows as non-quoted; not a defect.

## Prong 2 — M38 row (lesson:29): complete; red receipt real but exit code unrecorded

- Evidence pointer resolvable: `.ufo/waves/round-65/m38-red-before.log` exists; measured sha256 `aaba825263b5ce3613d8972831fa0e92bb7805547846056103e526293d814392` **exactly matches** the hash recorded in the row.
- The log shows the failure the row describes: 10 JSON facts end at `axml_start_namespace`, then `Traceback ... File "readout.py", line 179 ... ch = next(c for c in chunks if c["type"] == ctype) / StopIteration` (log:11-17). The chunk table (log:7) shows the desynced fourth chunk `{headerSize:0, offset:280, size:4294967295, type:1}` — consistent with the row's account of node size overstated by 8 (16+payload instead of 8+payload). Fixture archive recorded at 947 bytes, sha `df8c1361…` (pre-fix bytes differ from the landed `05d2280f…`, as expected).
- **Shown-able-to-fail gap (minor):** the log contains no explicit exit-code line (`grep -nE 'exit|status|rc='` → nothing). A Python traceback reaching EOF implies non-zero exit, but the receipt does not record it; the brief's "shows non-zero exit" is met only by inference. The fix-side green is claimed as "exits 0 with 15 lines (sha256 `507d79f8…`)" — truncated hash, no green log on disk under `.ufo/waves/round-65/`, so that half is unverifiable from the pointer given.
- `captured-by` column populated (Q06 gate + readout walk-end assertions); `fix` column populated (8+len(payload) derivation; pool width from five trailing u32s — confirmed by the log's own `spec_derived_struct_widths` showing ResStringPool_header 8 fields/28 bytes and ResXMLTree_node 5 fields/16 bytes). Row structure conforms to the M37 row and the claims.md:133 pre-registration.

## Prong 3 — Wave preparation claim: consistent, no falsification

- Lesson:42 claims "one v2 wave prepared (64 seats, ≥25% attack roles) under `.ufo/waves/round-65/wave-spec.json`, validated by `ufo-swarm-wave.mjs plan` exit 0; dispatch is the orchestrator's between-round act".
- `wave-spec.json` exists (sha256 `6f1f9742d97256dc3e4c365c5ddd4eef82ca288f82c4749410e2510d9252fb90`); `wave=revenger-r65-v2`; `items` = **exactly 64**. Roles: reviewer 20 + critic 10 + mutation-tester 7 = **37 attack seats = 57.8% ≥ 25%**. `axes: [coverage, calibration]`; milestone matches the wave's build-state receipt.
- Validation receipt exists: `plan-validated.json` (sha256 `1ead4c4f…`) records `schema: ufo-swarm-wave-v1`, `counts: {spawn:64, resume:0, total:64}`, `tasks` len 64 — a `plan`-run output artifact; it does not itself record an exit code, so "exit 0" is asserted by the lesson and consistent with the artifact's existence, not independently re-checkable. No counter-evidence found.
- Internal consistency with lesson:10 ("no L2 wave ran in-seat; the validated wave spec is prepared … for the orchestrator's between-round dispatch") — holds; the spec's `dispatch` block is unexecuted metadata.
- Note: lesson:42 calls the wave "64 seats" and claims "§3 planner seat held by the L1; no lane-side seat count claimed" — spec has one `revenger` role seat (the L1 planner), consistent.

## Smallest safe corrections (all fixable, none contract-level)

1. lesson:12 — change "lines 608-611" → "lines 607-609" (or quote through line 610 and count accordingly).
2. lesson:13 — change "line 5" → "lines 7-8".
3. lesson:14 — change "(16 words)" → "(14 words)".
4. Optional hardening: append an exit-code line to `m38-red-before.log`-style receipts in future rounds; a truncated `507d79f8…` green hash should either be full-width or point at a stored green log.

Canonical-judge note: these are annotation/pointer defects in a lesson document, not counter-spoofs — the C5 mutant attribution and C1 admission surfaces are untouched by any of this. Rejecting the round on these alone would over-punish; flag for L1 correction at integration.
