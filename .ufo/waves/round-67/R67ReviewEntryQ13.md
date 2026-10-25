Q13 n/a (named reason confirmed on the bytes: no verifier, recheck command, comparison tool or automatic checker is credited beyond the entry's own readout recheck [entry:156], and the recheck's sole credited clause is exactly what its own run detects — re-run demonstrated at HEAD `7668510`)

Seat: R67ReviewEntryQ13 · 2026-10-24 · judged bytes: `corpus/knowledge/round-67-apk-axml-byte-evidence.md` as committed at `7668510ffc49733daf023e40ff3300ef387ebde5` (`git status --porcelain` clean for the entry, `corpus/fixtures/apk-r65/`, `corpus/SOURCES.md`, `corpus/README.md`; entry file sha256 `170df17d82452fef310749e43d7d11661a943e2185594ad1de8c8446d33d968a`). I am not the author; decision made independently on the committed bytes.

## Q13 decision

Criterion (`corpus/QUALITY.md:25`): a verifier or recheck command is credited only for clauses whose deletion its own run is shown to detect; other clauses are named as unguarded.

**Credit enumeration** (line-numbered grep over the entry for `recheck|verif|guard|detect|checker|credit|agree|automatic|check_embedded|C7|gate`; no LSP device is available in this seat's tool inventory, and the audit is byte/anchor-level, so line-numbered grep is the recorded fallback):

1. `entry:6` `recheck:` — the readout command, credited with exactly four clauses: (a) exits 0, (b) prints 15 stdout lines, (c) their SHA-256 is `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247`, (d) the per-value form prints the single JSON line for one named fact. All four exercised at HEAD `7668510`:
   - `python3 -B corpus/fixtures/apk-r65/readout.py` → `EXIT=0`, `wc -l` = **15**, sha256 of stdout = `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` (exact match);
   - `python3 -B corpus/fixtures/apk-r65/readout.py --fact eocd` → one JSON line, `EXIT=0`;
   - the §Reproduce embedded 15-line block diffs clean against the actual stdout (`EMBEDDED-STDOUT-VERBATIM`), so the stdout-hash clause detects deletion/drift of every embedded value line — the M39 transcription class this entry repairs is precisely inside its detection span. No clause is credited beyond run-detectable scope.
2. `entry:124` comparison with the authored oracle — not a command/verifier run; an author comparison statement whose enumerated shared fields all actually exist in `truth.json`: `image.sha256`+`image.size`; `members[].local_header_offset` / `compressed_size` / `uncompressed_size` / `crc32` for all three members; `axml_declared.strings` (9); `axml_declared.attributes` (3 rows); `axml_declared.resource_ids` with exactly `0x0101021b`/`0x0101021c` non-zero. Nothing is credited beyond the oracle's declared content, and no value is presented as *guarded* by an automatic check.
3. `entry:12` "no verifier source is read" — negative scope statement, verified: `readout.py:13-18` imports stdlib only (`hashlib, json, struct, sys, zlib, pathlib`), no verify_* source read.
4. No credit of the round-67 C2 probe anywhere in the entry (`check_embedded` has zero hits); `gate` appears only as "re-gate" process prose in `entry:8`.

**Named-reason accuracy:** the entry's Q-map row (`entry:156`) says n/a by construction with that reason. The reason is accurate: there is no credited guard whose scope needs trimming, so the unguarded-clause naming obligation never triggers. Even under the strictest reading — applying Q13 to the readout recheck itself — the entry passes, since its single credited clause is run-detected (demonstrated above, including the verbatim diff). Per the frozen predicate ("PASS (n/a only with the entry's named reason)"), this n/a carries the entry's named reason and it holds.

## Supporting anchor/digest checks (ground for the enumeration)

- Snapshot digests all match the entry's pins: `ResourceTypes.h` sha256 `56b88bc4…` 86255 B; `rea-android-applications.md` `412d9cb4…`; `dex-format.html` `c0428612…` 281157 B.
- S038 enum anchors (grep-numbered in the snapshot): `RES_STRING_POOL_TYPE` :239 ✓, `RES_XML_TYPE` :241 ✓, `RES_XML_END_NAMESPACE_TYPE` :246 ✓, `RES_XML_START_ELEMENT_TYPE` :247 ✓, `RES_XML_END_ELEMENT_TYPE` :248 ✓, `RES_XML_RESOURCE_MAP_TYPE` :253 ✓ (the routed repair lands; r65's :239-250 excluded it).
- S043 anchor: snapshot :7-8 is exactly "Start with `inspect_android_package` on the caller's APK path for package / identity, manifest declarations, coverage, and inline Evidence." ✓, and :5 is `older server.` ✓ — both routed corrections are exact.
- S045 quoted anchors all present in `dex-format.html`: adler32 clause :5949-50, SHA-1 signature clause :5956-57, `must be 0x70 (112) bytes` + `(v40 or earlier)` :5981-82, `ENDIAN_CONSTANT = 0x12345678` :5035 ✓.
- readout.py line cites: `payload_off = lh_off + 30 + lh_name_len + lh_extra_len` at :105 (inside cited :99-105) ✓; `flags & 0x100` at :166 ✓; attrExt-relative `aoff = base + 16 + attribute_start + i * attribute_size` at :203 (inside cited :200-203) ✓; `NO_INDEX = 0xFFFFFFFF` at :22 ✓.
- `QUALITY.md:23` (cited by the entry's Q08 row) is indeed the Q11 "Supersedes Q08" row ✓. No `### Code` pointer remains in the entry ✓.
- Fixture-surface digests match the S041 pins: fixture.apk `05d2280f…`, truth.json `27303bae…`, readout.py `92e347c3…` — the red-before surface is untouched as far as digests reach.

## OFF-criterion defects noticed

- OFF-1: `entry:1` cites `RES_XML_START_NAMESPACE_TYPE` :244; snapshot line :244 is `RES_XML_FIRST_CHUNK_TYPE` (same value `0x0100`); START_NAMESPACE is :245. Anchor-line off-by-one only — no value or claim affected (item 4's observed start-namespace type 256 = 0x0100 is correct per actual stdout, diff-verified). Touches the Q02 "exact anchor" posture; for the Q02 seat to weigh. Not a Q13 matter (no verifier credit involved).
- No other off-criterion defect found in the checks I ran; the repaired entry:42 hex `4d616e69666573742d56657273696f6e` is byte-identical to actual stdout ("Manifest-Version", 16 bytes) ✓.

## Residual risk / verification gaps

- I did not re-audit the S032/S034 APPNOTE field-width provenance or the full S045 row in `corpus/SOURCES.md` (Q01 seat surface); the entry's uses of them were only checked where they touch credited clauses.
- Recheck runs executed against the working tree at HEAD `7668510`; tree cleanliness for the audited paths (git status above) is what equates working tree with committed bytes.
- "unchanged since `c7b7cf98`" (`entry:5`) rests on digest equality with round-65-recorded pins, which I confirmed for the current bytes but not by diffing the r65 tree itself (Q09-scoped; no verifier-credit implication).

Tooling directive: no tools installed or upgraded (none needed); no pacman transactions; no writes outside this report file (scratch limited to `/tmp/r67q13_stdout.txt`).
