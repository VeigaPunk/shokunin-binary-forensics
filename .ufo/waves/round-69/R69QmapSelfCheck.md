FAIL — the v4 §Q-map carries 8 decision rows for a 15-criterion bar (`corpus/QUALITY.md:9-24`), names a reason for none of the 7 omitted criteria, leaves Q15 (this round's own new criterion) undecided although entry:8 states a bare git object id (`c7b7cf98`) with no deriving command, and two `pass` rows are contradicted by the entry's own bytes: Q14's basis denies a length that entry:48 states, and Q11's basis scopes away five header digests that meet Q11's reject clause verbatim.

# R69QmapSelfCheck — §Q-map self-consistency of the C05 v4 candidate

Entry under test: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-69-apk-axml-byte-evidence.md`
(215 lines, sha256 `c1e7eaac9dba4c77e578c788755dec3e3499fd8795ad0e479c51b5be7deb11d5`).
Bar: `corpus/QUALITY.md:9-24` (Q01–Q15 + admission procedure `:26-28`), `reports/round-69/claims.md`
§C1 predicate ("every applicable Q01–Q15 decision … is PASS (n/a only with the entry's named reason)").
Read-only seat: nothing was edited; no file outside this report and `/tmp/revenger-r69-*` was written.

## 0. The map as landed

`entry:173` `## §Q-map`; table header `entry:175`; data rows `entry:177-184`. Row count: **8**
(`grep -c "^| Q" … → 8`). Decideable criteria per QUALITY.md: Q01–Q07, Q09–Q15 (13 rows; Q08 is
superseded by Q11) — so with Q15 the bar has 14 decideable rows and the map is **8/14, 6 short** (Q03, Q06, Q09, Q10, Q12, Q15), plus it carries no Q08 supersession record.

The round-68 v3 candidate carried 13 rows (`corpus/knowledge/round-68-apk-axml-byte-evidence.md:172-184`),
including `Q08 | superseded by Q11` at `:179` and `Q12 | n/a | no rejected source row…` at `:183`.
v4 dropped **Q03 (`v3:174`), Q06 (`v3:177`), Q08 (`v3:179`), Q09 (`v3:180`), Q10 (`v3:181`),
Q12 (`v3:183`), and never added Q15**. Q10 is the sharpest omission because the body still carries
`## Cross-lane scope note (Q10)` at `entry:169-171` — a Q10 heading with no Q10 decision row.

No row is marked `n/a`, so the brief's "rows marked n/a that should not be" has an empty set; the
inverse defect (rows absent without a named reason) is the live one, and `QUALITY.md:28` ("A criterion
marked `n/a` names why it cannot apply") plus admission-procedure step 1 make every one of the 7
omissions a self-consistency break, not a stylistic one.

## 1. Row-by-row: verdict, basis pointer, and whether the pointer resolves

Line numbers are entry lines; runs below are the re-executions I performed from the lane root.

| id | row | verdict | basis pointer the row names | self-check against the entry's own bytes |
|---|---|---|---|---|
| Q01 | `:177` | pass | entry:1 (S038 anchors, incl. "`ResChunk_header` (line 218)"), :2 (S043), :3 (S045), :4 (S032), :5 (S034), :6 (S047), :7 (S041) | Pointers resolve; tiers A per `corpus/SOURCES.md:46,48,52,55,57,59,61`. **Two stale provenance claims:** the row says S045 was "opened 2026-10-24 **this round**" — v4's `verified-at` is 2026-10-25 (`entry:8`) and `SOURCES.md:91` logs S045 as a *round-67* opening; and it says S038 was "**re-opened 2026-10-25**", but `SOURCES.md:52` records `opened 2026-10-24, status mined` and `SOURCES.md:92` is the only 2026-10-25 opening (S047). Also `SOURCES.md:52` anchors the enum block as "`:239-250`" while the entry states 237-263 (`entry:1`, `entry:59`) — the cited row's locator is stale against the entry's own (byte-correct) numbers. Verdict is precedent-consistent (`R68ReviewEntryQ01.md:1` passed the same mined-row structure), but the "this round" wording is false as written. |
| Q02 | `:178` | pass | entry:1-7 (`source:`), :8 (`verified-at:`), :9 (`recheck:`), :10 (`coverage-map: … C05`) | Resolves and holds. Re-ran both `recheck:` commands: readout → `exit=0`, `15` lines, stdout sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` = `entry:9`/`:194`; derive → `exit=0`, `20` lines = `entry:131-150`. Anchors are section/line/sha-specific, not bare homepages; snapshot files exist (`.ufo/waves/round-65/source-snapshots/ResourceTypes.h` = `56b88b…c56f`; `rea-android-applications.md` = `412d9c…a74c`; `.ufo/waves/round-67/source-snapshots/dex-format.html`, 281157 bytes). |
| Q04 | `:179` | pass | `entry:61` (manual label), `entry:127-129` (bounded derivation credit) | Substantive legs hold (analysis labeled manual at `entry:15`, `entry:61`; no tool credited with a result it did not print — all stated S038 numbers are in the derive run). **Two basis statements are false as written.** (a) "the **only** tool named is Python itself" — `entry:171` names `` `inspect_android_package` `` and "JADX prerequisites"; the S043 source line names the JADX/Java 17 prerequisite too. (b) "labeled manual (item 5 …)" — the pointer the row leans on, `readout.py:51-58`, carries the opposite claim in its own comment `readout.py:48-50`: "Every fixed offset the readout uses is computed here from the field widths in `ResourceTypes.h`'s own struct definitions, **not assumed**", and the emitted fact is named `spec_derived_struct_widths` with `source_anchor="S038 ResourceTypes.h struct field lists"`. That is the exact second leg of the round-68 Q04 FAIL (`R68ReviewEntryQ04.md:3`); v4 corrected the entry prose but the cited artifact still asserts a derivation that did not happen. |
| Q05 | `:180` | pass | `entry:171` (provider fence), `entry:131-150` (derivation stdout) | Provider-readiness fence is genuine (`entry:10` "Not covered: … provider (`inspect_android_package`) readiness or output"; `entry:171`). But "**no** readiness or capability claim is made" is over-broad: `entry:9` and `entry:127` claim a behaviour of the entry's own instrument — "The script refuses to print a line it did not find (a missing or ambiguous symbol is exit 2)". The branch exists (`corpus/derive_axml_anchors.py:28-29,71,79,104`), but the entry embeds no exit-2 probe (`grep -n "exit 2" entry` → only `:9`, `:127` prose). `QUALITY.md:13` requires "its command, date and observed exit" for a capability claim; asserted-but-unprobed is the reject shape. |
| Q07 | `:181` | pass | `entry:91` (item 8 namespace sentence), `entry:161-163` (§Observation/inference/unknown) | Resolves and holds. `entry:91`: "…an observation of how this readout resolves this fixture's bytes, not a prediction about any other parser" — the observation-scoped namespace sentence the brief names is present and correctly cited. The chunk-type/width readings are filed as **Inference** at `entry:162`, not as parser fact. `entry:77` scopes the resource-map correspondence to `truth.json`. Consistent row. |
| Q11 | `:182` | pass | `entry:23-124` (items 1-10 outputs), `entry:61` (item 5 manual), `entry:127-150` (item 11), `entry:91` (item 8) | Items 1-10 and item 11 legs hold byte-for-byte: all **30** embedded JSON lines are exact members of the re-run stdout (`embedded lines NOT in actual stdout: 0`), and the §Reproduce block `entry:200-214` is byte-identical to the re-run (`block exact match: True`). **The row does not cover five digests in the header, and Q11's criterion is entry-wide** (`QUALITY.md:23`: "Each count, identifier, offset and digest **in an entry** carries … the command that derives it"). Underived values: `truth.json 27303bae…f8173`, `generator.py eaa9444c…27c1a`, `readout.py 92e347c3…3976` (`entry:7`); S043 snapshot `412d9cb4…a74c` (`entry:2`); S047 script `74d4c0d9…aa` (`entry:6`). None is presented with a command+output, and none is labeled "recorded, not re-derived" (Q11's own escape). I re-derived all five (`sha256sum` output in §3) — they are correct, which is exactly Q11's reject clause "a value is correct when re-derived but the entry carries no derivation". Same class also at `entry:68`: "The **derived** 20-byte `ResXMLTree_attrExt` size" for a value item 5 calls a manual transcription. |
| Q13 | `:183` | pass | `entry:131-150` (20-line set), `entry:9` (readout recheck) | The round-68 defect is genuinely repaired: every S038 line number the entry states — 218 (`:1`), 237/239/241/244/245/246/247/248/253/263 (`:1`,`:59`), 677/686/687 (`:84`) — appears in the re-run 20-line stdout, so the `:237`/`:244` deletion-survival FAIL (`R68ReviewEntryQ13.md:1`) no longer reproduces. Two residual imprecisions: (a) `entry:129` calls the 20 printed lines "the complete set of S038 line numbers this entry states", but the output also prints 287, 461, 612, 621, 707 (`entry:133-138`) which the entry never states (grep shows those numbers only inside the output block) — the set is a strict superset, not the stated set; (b) `QUALITY.md:23`'s second leg ("other clauses are named as unguarded") is unaddressed — the nearest is item 5's "not a runtime derivation", which names manual provenance, not an unguarded clause. Verdict pass is defensible on the credit leg; the basis wording overstates exactness. |
| Q14 | `:184` | pass | `entry:48` (9-byte clause), `entry:30`/`:52`/`:109` (other hex clauses) | **Self-refuting.** The basis asserts "the ellipsis-truncated run `4d616e696673742d…` carries no length" — but `entry:48` reads "…recorded a **15-byte** `4d616e696673742d…` pair…", i.e. the same clause attaches a length to the truncated run, which is Q14's own middle clause (`QUALITY.md:24`: "an ellipsis-truncated run carries no length"). The quoted run is 16 hex chars = 8 bytes (`b'Manifst-'`), while "15-byte" describes the draft's *full* pair — `corpus/knowledge/round-65-apk-axml-byte-evidence.md:41` = `4d616e696673742d56657273696f6e`, 30 hex chars = 15 bytes = `b'Manifst-Version'` — so the number is right about round-65 and wrong against the bytes it is printed beside. Two of the three further examples do not carry a byte count either: `entry:30` says only "signature `504b0506` is located at file offset 925" (no N), and `entry:52` gives "headerSize 8" as a field value, not a byte count for the quoted run. The 9-byte clause itself is correct (`4d616e69666573742d` = 18 hex = `b'Manifest-'`). |

## 2. Missing rows — the coverage axis (7 criteria, no named reason)

Each has material in the entry today; the v3 wording is byte-available in the round-68 file, so
restoring them is a pointer edit, not new evidence.

- **Q03** — absent. Material: `entry:155-159` (oracle-declared expected values; item 7 `entry:77`) and the S038-derived widths; v3 `:174` passed it.
- **Q06** — absent. Material: items 1-3 (`entry:23-46`) are byte-verified against the built fixture; v3 `:177` passed it.
- **Q08** — absent. v3 `:179` carried the supersession row; dropping it removes the only record that Q08 is historical for this entry.
- **Q09** — absent. Material: `entry:8` ("bytes unchanged since"), `entry:19-27` (digest scope), `entry:167` (Limitations); v3 `:180` passed it.
- **Q10** — absent while the body has `## Cross-lane scope note (Q10)` (`entry:169-171`); v3 `:181` passed it. The heading now promises a decision the table does not contain.
- **Q12** — absent. v3 `:183` gave the n/a reason ("no rejected source row is written by this entry"); that reason is the *only* naming step for an n/a, and it is gone (`entry:6`/`:2` assert supersession of S046/S039, not a reject row).
- **Q15** — absent, and its target is in the entry: `entry:8` "the fixture, oracle and readout bytes are the round-65 claim-tree bytes, **unchanged since `c7b7cf98`**" — a stated git object id with no deriving command anywhere (`grep -n "rev-parse\|\bgit\b" entry` → no matches). Re-derivation (read-only):
  - `git rev-parse c7b7cf98` → `c7b7cf98ddeecbd5464e47396f224e6384b78905` (commit, 2026-10-24, "round-65: candidates — apk-r65 fixture+readout…") — the id resolves and the sentence's *substance* is true for the cited subtree: `git rev-parse c7b7cf98:corpus/fixtures/apk-r65` = `dd6615e67342a020fbd28b720ede0bf55f9d14c7` = `git rev-parse HEAD:corpus/fixtures/apk-r65`.
  - The wider tree does not: `c7b7cf98:corpus` = `861bd0749f9b1e1c0e3283e5b83c2c6acd7c0b4c` vs `HEAD:corpus` = `7aeabf218889dee89036de808573aacf11bd6e69` (expected — v4 is new), so a Q15 row must scope the identity to `corpus/fixtures/apk-r65`, not to "the round-65 claim tree" at large.
  - As landed it meets Q15's reject shape (`QUALITY.md:24`: "an identity sentence is asserted without the deriving command"). The round that *adds* Q15 therefore lands a candidate that would FAIL it, with no Q15 row to say so.

## 3. Commands and actual output (all read-only)

```
$ sha256sum corpus/knowledge/round-69-apk-axml-byte-evidence.md
c1e7eaac9dba4c77e578c788755dec3e3499fd8795ad0e479c51b5be7deb11d5  …round-69-apk-axml-byte-evidence.md
$ wc -l  → 215
$ python3 -B corpus/fixtures/apk-r65/readout.py ; echo exit=$?
exit=0 ; wc -l = 15
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  (stdout file)
$ python3 -B corpus/derive_axml_anchors.py ; echo exit=$?
exit=0 ; wc -l = 20        (entry:131-150 byte-identical: block==real → True)
$ sha256sum corpus/fixtures/apk-r65/readout.py corpus/derive_axml_anchors.py \
    corpus/fixtures/apk-r65/truth.json corpus/fixtures/apk-r65/generator.py corpus/fixtures/apk-r65/fixture.apk
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976   readout.py     (= entry:7,:15,:194)
74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa   derive_axml_anchors.py (= entry:6)
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173   truth.json     (= entry:7)
eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a   generator.py   (= entry:7)
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e   fixture.apk    (= entry:1,:7)
$ sha256sum .ufo/waves/round-65/source-snapshots/ResourceTypes.h .ufo/waves/round-65/source-snapshots/rea-android-applications.md
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  ResourceTypes.h  (= entry:6,:131)
412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c  rea-android-applications.md (= entry:2)
$ git rev-parse c7b7cf98 ; git rev-parse c7b7cf98:corpus ; git rev-parse HEAD:corpus
c7b7cf98ddeecbd5464e47396f224e6384b78905
861bd0749f9b1e1c0e3283e5b83c2c6acd7c0b4c
7aeabf218889dee89036de808573aacf11bd6e69
$ git rev-parse c7b7cf98:corpus/fixtures/apk-r65 ; git rev-parse HEAD:corpus/fixtures/apk-r65
dd6615e67342a020fbd28b720ede0bf55f9d14c7
dd6615e67342a020fbd28b720ede0bf55f9d14c7
$ python3 -c "…"   # hex widths
4d616e69666573742d  18 chars = 9 bytes  => b'Manifest-'
4d616e696673742d    16 chars = 8 bytes  => b'Manifst-'
4d616e696673742d56657273696f6e 30 chars = 15 bytes => b'Manifst-Version'   (round-65:41)
```

Cross-checks that came back clean (they keep the two "consistent" rows honest):
`embedded JSON lines: 30 | actual stdout lines: 15 | embedded lines NOT in actual stdout: 0`;
`§Reproduce block (entry:200-214) == actual stdout → True`; `readout.py:51-58` is the exact width
range (`:51` the w8/w16/w32 assignment, `:52-58` all six field lists) so that pointer is precise;
`entry:91` is the observation-scoped namespace sentence; `entry:171` is the Q10 fence.

## 4. Impact on the frozen predicates

- `reports/round-69/claims.md` §C1 requires "every applicable Q01–Q15 decision … PASS (n/a only with
  the entry's named reason)". The entry supplies no reason for 7 criteria and no Q15 decision at all,
  so the predicate cannot be satisfied from the landed bytes: a wave seat assigning `n/a` to Q12 or
  `pass` to Q15 has no entry-named reason to cite, and a strict reading makes Q15 a **FAIL on the
  v4 bytes** — the C1 kill branch ("any Q FAIL on the v4 bytes … → C05 stays `uncovered`, the v4
  entry marked `admission-status: rejected`"). That is a build-state defect, not an adjudication
  outcome; the map is the entry's own declaration and it is currently unusable as the predicate's
  evidence.
- The two false `pass` rows (Q14, Q11) are worse than the omissions because they *publish* a clean
  decision: any seat that echoes `entry:184` inherits a statement its own bytes contradict at
  `entry:48`, and any seat that echoes `entry:182` inherits the header-digest escape.

## 5. Smallest safe correction (per row, no re-derivation needed)

1. **Q15** — add a row and either (a) rewrite `entry:8` to `git rev-parse c7b7cf98:corpus/fixtures/apk-r65`
   = `git rev-parse HEAD:corpus/fixtures/apk-r65` = `dd6615e6…` (both verified above), or (b) drop the id
   and say "the round-65 fixture bytes (digests in `entry:7`)". Scope any identity to
   `corpus/fixtures/apk-r65`, not the corpus tree (`861bd0…` ≠ `7aeabf…`).
2. **Restore Q03/Q06/Q08/Q09/Q10/Q12** — copy the v3 rows (`round-68-…:174,177,179,180,181,183`) with
   v4 line pointers (Q03→`:155-159`, Q06→`:23-46`, Q09→`:8,:23-27,:167`, Q10→`:169-171`, Q12 n/a reason
   "no rejected source row is written by this entry").
3. **Q14** — delete "15-byte" from `entry:48` (or quote the full 30-hex-char run with its 15-byte count,
   which is what round-65:41 recorded) and restate `entry:184` to match; drop `504b0506` from the
   "carries byte counts" list (`entry:30` states none).
4. **Q11** — either embed the five `sha256sum` receipt lines (`truth.json`, `generator.py`,
   `readout.py`, S043 snapshot, S047 script — output in §3) or label them "recorded, not re-derived";
   change `entry:68` "The derived 20-byte …" to "The transcribed 20-byte …".
5. **Q04** — replace "the only tool named is Python itself" with "Python is the only tool credited with
   output; the provider/JADX names at `entry:171` are documented scope, not credited"; and note that
   `readout.py:48-50` still asserts a field-list derivation the code does not perform (the entry's
   item-5 label is correct, the artifact's comment is not).
6. **Q05** — replace "no readiness or capability claim is made" with "no provider claim; the
   derivation script's exit-2 behaviour is asserted from its source (`derive_axml_anchors.py:28-29`),
   not probed in this entry".
7. **Q01** — fix S045's "opened 2026-10-24 this round" (round 67 per `SOURCES.md:91`) and S038's
   "re-opened 2026-10-25" (unlogged; `SOURCES.md:52` says opened 2026-10-24), and either log the
   2026-10-25 re-open in `SOURCES.md`'s search log or drop the date.
8. **Q13** — narrow `entry:129` from "the complete set of S038 line numbers this entry states" to "the
   five anchor numbers this entry states plus five struct locators it does not" (or trim the script's
   unused struct lines), so the credit is stated as a subset, not as exact equality.

## 6. Tooling

No install or upgrade was made (the pacman guard was honoured). Verification used existing
`python3` (stdlib), `git` (read-only `rev-parse`), `sha256sum`, `grep`, `awk`. Scratch files
`/tmp/revenger-r69-qmap-*.txt` were deleted before returning.
