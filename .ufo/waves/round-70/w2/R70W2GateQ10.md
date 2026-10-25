PASS — every finding in the landed candidate is scoped to the one observed fixture/operation/version/input, generalization is explicitly fenced, and the cross-lane contested scope (kaidoku ADJ-06) is reported, not absorbed; every pointer the scoping rests on resolves.

Seat R70W2GateQ10 · round-70 WAVE 2 (falsify) · criterion Q10 only · target bytes: lane commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd`, `corpus/knowledge/round-70-apk-axml-byte-evidence.md` (`admission-status: candidate`, entry line 11). Method: read `reports/round-70/claims.md` §C1, `corpus/QUALITY.md` Q10, `PROVINCE.md`; extracted the landed corpus via `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd corpus | tar -x -C /tmp/revenger-r70-R70W2GateQ10/extract` and re-ran the entry's own commands there. The entry's own §Q-map Q10 row (entry:307) was NOT used as evidence.

## Evidence

**1. Scope statements on the landed bytes (all re-read from the archive extraction, path `corpus/knowledge/round-70-apk-axml-byte-evidence.md` at `17ee7f87…`):**
- `:10` coverage-map — "Not covered: install/signature verification, dex validity or execution, provider (`inspect_android_package`) readiness or output, general AXML or ZIP-parser behavior beyond this fixture." Negative scope is stated, not just positive.
- `:178` (item 13) — "agreement shows the readout parses what the generator wrote; it does not show that a declared value (for example the two resource ids) is the Android framework's value for its name." Parse-fidelity only; no framework-semantics universal.
- `:283` — "Each inference cites its byte evidence and is scoped to this fixture."
- `:288` (Limitations, full line re-read) — "One authored fixture, one manifest shape (a single element with three attributes), UTF-8 string pool only, no CDATA, no nested elements, no styles" … "no conformance of the fixture to any producer's output is claimed" … "Generalization to other APKs, other AXML producers or the `inspect_android_package` provider would need its own evidence." This is the explicit anti-generalization fence Q10 demands.
- `:86` (item 8, full line) — the namespace sentence is attributed to the tool, not the format: "The readout resolves each attribute's namespace prefix string by indexing the string pool directly with the attribute's own `ns_index` … The start-namespace chunk is printed as a separate fact and the readout does not consult it when resolving attribute namespaces" — a description of this readout on these bytes, not a claim about AXML producers in general.
- `:101` (item 9) — "A match between a declared value and its recomputation shows the member's header is internally consistent, and nothing about dex program validity follows."
- `:292` (Cross-lane scope note, headed "(Q10)") — provider route fenced to S049 documented scope ("this lane ran no provider and makes no readiness claim"); ADJ-06 overlap "stays reported, not absorbed: the kaidoku lane's APK content-graph inventory and Android decode axis … are not restated, and this entry claims none of that surface."

**2. Cross-lane and source pointers resolve (commands run on the live trees, read-only):**
- `sed -n '40,44p' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` → line 42 is the open `tsukuroi | round-1` question "…arbitrate the kaidoku/revenger shipped-artifact overlap before an ADJ-06 analysis is routed?" — matches the note's "fleet `.ufo/l0-questions.md:42`, open".
- `sed -n '25,31p' /home/vgpnk/Projects/shokunin/kaidoku-shokunin/corpus/README.md` → line 27 row "Archives & packages … APK content graph (120 deduplicated content nodes; all 130 occurrences hash-verified)" and line 29 row "Android decode axis first-held on Godot APKs: `inspect-android-package` (manifest + class census, decompiles nothing) …" — exactly the two surfaces the note says it does NOT restate; the entry absorbs neither.
- S049 route sentence: `--spec-quotes` (below) prints `MATCH rea-android-applications.md: first line 7 … Start with `inspect_android_package` on the caller's APK path…`; `grep -c inspect_android_package` on the snapshot prints `1` — the entry's only provider citation is that single sentence, and no readiness/execution claim rides on it.
- S048 anchors (entry `:3`): `grep -n "Items and related structures" corpus/snapshots/dex-format.html` → `5921:<h2 id="items" …>Items and related structures</h2>`; `grep -n ENDIAN_CONSTANT` → `5023` heading, quoted phrase at 5035 (printed by `--spec-quotes`). Scope of the S048 row is fenced to the four quoted header-item phrases.

**3. Re-derivations (run from the `17ee7f87…` extraction; my stdout vs the embedded lines):**
- `python3 -B corpus/fixtures/apk-r65/readout.py` → exit 0, 15 lines, `sha256 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — equals item 15's printed digest (`:238`) and `--stdout-digest` re-printed the same line byte-identically.
- `--fact archive`, `--fact axml_start_element`, `--fact dex_declared_header` → byte-equal to embedded `:27`, `:90`, `:105` (e.g. `"element_name": "manifest"`, `res_id` 16843291/16843292, `endian_tag 0x12345678`).
- `entry_checks.py --pins` → all ten digests equal embedded `:222-231` (fixture `05d2280f…`, readout `92e347c3…`, entry_checks `2d4f25f6…`, ResourceTypes.h `56b88bc4…`).
- `--spec-quotes` → 6 MATCH lines byte-equal to embedded `:144-149`.
- `--oracle` → `grep -c MATCH` = 34, matching the 34 embedded lines `:182-215` (image, 3×5 member fields, strings, resource_ids, 3×5 attribute fields).
- `--container` → 3 MATCH lines byte-equal to embedded `:245-247` (flags 0x0000, method 0, bit 3 clear).
- Cited source locators confirmed: `readout.py:22` `NO_INDEX = 0xFFFFFFFF`, `:203` `aoff = base + 16 + attribute_start + i * attribute_size`, `:211` `"ns": None if ans == NO_INDEX else strings[ans]`, `generator.py:8` "…contains no classes and is not a valid dex program" — the sentences citing them describe exactly this scoped behavior.

**4. No one-family observation stated as universal.** Scanned every prose claim: the decimal/hex type mapping (`:54`) is labeled inference (`:61` handles the shared `0x0100` value explicitly); the resource-map layout is honestly marked "its source line is not among the lines item 11 prints" (`:79`); the APPNOTE widths are labeled recorded/manual, not derived (`:63`, `:152`); the "Unknown" block (`:284`) disclaims install validity, signature blocks, dex validity, producers. Nothing generalizes past `corpus/fixtures/apk-r65/fixture.apk` (947 bytes, `05d2280f…`).

## Verdict

Q10 = **PASS** on the landed candidate bytes at `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd`.

## Residual risk / verification gaps

- I verified the committed S049/S048 snapshot bytes and their digests, not upstream currency; the entry itself claims only snapshot-local anchoring (`:4` for S032, `:284`), so nothing in Q10 scope is exposed.
- Upstream `github.com/morluto/rea` S049 fetch and kaidoku-lane internal claims were taken from the committed snapshots + the kaidoku README rows; I did not re-fetch either remote (out of Q10 scope; time-box).
- The broken-pipe traceback in my own `--oracle | head -5` pipeline was an artifact of my shell, not the entry; the unpiped run printed all 34 MATCH lines.
- Other criteria (Q01, Q11, Q13…) are other seats'/lanes' calls; I did not judge them here beyond what Q10 needed.
