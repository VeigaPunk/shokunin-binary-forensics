FAIL — SKILL.md is stale against the round-65 build tree in five load-bearing blocks (§1 guarded/unguarded columns, §6.1+§3 counter and red-before, §6.5 round-close gate, §4 mistake table, header provenance); a round-65 pointer is required, and the minimal edit set is nine blocks (E1–E9), none of them cosmetic.

Seat question, answered directly: **yes, SKILL.md needs a round-65 pointer, but the mandatory part is correction, not addition.** The C5 control shape falsifies §1's `unguarded` column (the SKILL's own core decision table) and §1's control-insertion rule; the APK fixture family falsifies §2's single precedent, §6.4's scratch-only example list, and §6.5's literal void clause; the round-65 counter replaces the instrument §§3/6.1 point at. §7's own *existence* promise still holds (38 paths checked, zero missing), so the §7 work is three pointer rows, not a repair.

## Method and bounds

Read-only lane seat. No probe run (measurement belongs to committed trees and the frozen counter seat), no edits outside this file, no git/jj mutation, no tool installs. HEAD observed read-only: `8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0`, 11 dirty paths.

Path-existence sweep (every citation carrying a resolvable location in SKILL.md §7 plus the round-65 build artifacts):

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && for p in <38 paths>; do [ -e "$p" ] || echo "MISSING $p"; done
---sha---
b8e68d326c28690274be98ac35a518970d84aa8b9892b5736450a776210b9168  reports/round-64/measure.py
8a2c69c4b0e9a799592c90f0e974ffee05556db5667d7b90ada58f92cf590304  reports/round-65/measure.py
```

Zero `MISSING` lines. The only §7 identity row (`reports/round-64/measure.py` sha256 `b8e68d…`) still matches. So §7's stated rule ("every path in §7 resolves", SKILL.md:212) is satisfied; the failure is currency and one dead referent, listed below.

## Findings, by severity

**F1 (high) — §1:45-46: `evidence_id` is no longer unguarded in either script, and the new controls are absent from the table.** The C5 patch is present in the tree:

```
corpus/verify_icon_languages.py:155  forged_evidence=copy.deepcopy(receipt)
corpus/verify_icon_languages.py:156  forged_evidence['evidence_id']='ev_6e055332…'
corpus/verify_icon_languages.py:157  require(not receipt_ok(...), f'r{r}: forged receipt evidence accepted')
corpus/verify_multi_icon_states.py:154/155/156  same shape, 'ev_8ed88983…'
```

SKILL.md:45-46 lists only `command` and `stdout_sha256` as guarded and puts `evidence_id` in the "name, do not credit" column. Applying §1 verbatim (its own rule at :52-54) makes a round-65 entry call `evidence_id` unguarded — false at this tree and contrary to `reports/round-65/claims.md:32-38`. Credit stays conditional per SKILL.md:64-66: red-before is `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=0/2` (`reports/round-65/measure-before.log:45`), credited only at `2/2` at the landing commit (`claims.md:86-90`). All *existing* file:line cells in §1 still verify against the tree (languages `receipt_ok` :118-120, command :149-151, stdout :152-154; multi :121-123, :148-150, :151-153) because the C5 insert appends after the last control — so the fix is two cells per row, not a renumber.

**F2 (high) — §6.1:149-164 and §3:344-378 point at the wrong instrument and the wrong red-before.** Round-65's frozen counter is `reports/round-65/measure.py` (`reports/round-65/claims.md:69`, sha256 `8a2c69c4b0e9a799592c90f0e974ffee05556db5667d7b90ada58f92cf590304`); §6.1:156 hardcodes `reports/round-64/measure.py` and §3's committed snippet (:363-364) still names `reports/round-63/measure.py`. Label list at :158-162 lacks `K_ROW C05`, `STRICT_REJECT_WINDOW_SELFTEST`, `C5_CONTROLS_PASS`, `C5_RECEIPT_KILLED`, `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED`, `HOLDS_OK_V3` — all frozen in `claims.md:70-72,64-65`. Three quoted red-before values are false for this round: SKILL.md:160 says `README_TOKEN_LEGEND_MISMATCH` "1 at base" (round-65 base prints `=0 rows=[]`, measure-before.log:9); `:163-164` says the do-nothing base shows "K_HELD_BACKED 7/14, mismatch 1, C4 0/2" (round-65 base: `K_HELD_BACKED=8/14`, `C4_RECEIPT_KILLED_ATTRIBUTED=2/2`, `C5_…=0/2`, `HOLDS_OK_V3=no` — :1,:4,:35,:45,:60). §3's base table (:376-378) is round-64-era (`K_HELD=7/14`, `K_ROW C07 status=frontier`) and matches `reports/round-64/measure-before.log:1-2`, so it is honest for its era but unlabeled as historical and now the only base the SKILL shows. Worst practical effect: a seat following §6.1 measures the round-65 tree with the round-64 probe and cannot see the round's own target at all (no C05 row, no C5, no V3).

**F3 (high) — §6.5:214-220 round-close gate is unbound for round 65 and self-contradictory.** (a) It cites "claims.md §Harms": `grep -nE 'Harms|void' reports/round-65/claims.md` → **no matches**; the round-65 contract's analogues are §Frontier step conformance and §Routed inputs, and the void list is not restated. (b) "changed `corpus/live` or `corpus/fixtures` byte outside new **round-64** paths" read literally voids round 65 for landing its own registered fixture `corpus/fixtures/apk-r65/` (`fixture.apk` 947 B sha256 `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`). (c) The target list at :218-220 omits `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2` and `HOLDS_OK_V3=yes`, both required by `claims.md:64-65`.

**F4 (medium-high, destructive hazard) — §6.4:211 and §2:80 name only firmware-r63 as the in-place-overwrite hazard.** The apk-r65 generator rewrites its own fixture and oracle in place:

```
corpus/fixtures/apk-r65/generator.py:28  APK_PATH = HERE / "fixture.apk"
corpus/fixtures/apk-r65/generator.py:29  TRUTH_PATH = HERE / "truth.json"
corpus/fixtures/apk-r65/generator.py:197 APK_PATH.write_bytes(apk)
corpus/fixtures/apk-r65/generator.py:226 TRUTH_PATH.write_text(json.dumps(truth, …))
```

Running it inside `corpus/fixtures/apk-r65/` rewrites the C1 fixture bytes and the truth, and the truth embeds `platform.python_version()` — exactly the round-void condition §6.5 states, and exactly the failure mode §6.4's scratch-only rule exists to prevent, but the rule's example list stops at round 64.

**F5 (medium) — §4:109 title and table stop at M33–M36.** Round-65 registers M37 and M38 (`corpus/lessons/round-65.md:30`, `:29`). M38 is number-drift (layout constants stated from intent, not built bytes; red-before log sha256 `aaba8252…` cited in the lesson) — a class §4 does not carry, even though §2's `byte-verify` row (:82) is the check that catches it. M37 is the text-scan window spoof surface the new `STRICT_REJECT_WINDOW_SELFTEST` label measures. A seat that catches either has no id in the SKILL to cite.

**F6 (medium) — §1:59-61's prescribed control placement contradicts the round-65 frozen shape and would invalidate §1's own line column.** SKILL.md says the new control is "placed after the existing forged-command control"; `claims.md:35-36` freezes "immediately after the existing forged-stdout control". Legitimate as a location, but inserting between the two existing controls shifts the cited `stdout_sha256` ranges (:152-154 / :151-153) by the inserted line count — i.e. following SKILL.md makes SKILL.md's own `file:line` cells wrong. Round-65's append-after-last shape preserves them (verified above).

**F7 (medium) — §1:62-66 "Status at this draft" is stale in both directions.** It says C4 credit is still the working-tree fix with red-before `0/2`; at the round-65 base archive C4 is earned — `measure-before.log:35` prints `C4_RECEIPT_KILLED_ATTRIBUTED=2/2`. And it carries no C5 status line at all, while the same section now describes two scripts whose C5 control exists.

**F8 (medium) — header `verified-at:` (SKILL.md:6) describes a working tree that no longer exists.** It pins the two round-64 control ranges "at the uncommitted working tree on top of `a3d063f…` (the base scripts contain no `forged_stdout`)". Those controls are now committed (C4 `2/2` at the round-65 base, measure-before.log:35), and the tree at HEAD `8214e4dd` (11 dirty paths) adds the C5 inserts. The provenance split is honest about its era but presents itself as current; Q02 header discipline (which SKILL.md:127 enforces on entries) applies to this file too.

**F9 (medium-low) — §2:69-82 is single-precedent and its oracle-schema row is firmware-specific.** The only precedent (:71) and the `truth.json` shape row (:79) fix the zlib schema (`regions[]`, `fill_hex`, image/recipe constants). The round-65 oracle is a container schema: `image{path,sha256,size}`, `members[{local_header_offset,compressed_size,uncompressed_size,crc32,method,sha256}]`, `axml_declared{strings,attributes,resource_ids}`, `build_recipe{command,container,members,python_version,determinism}` (`corpus/fixtures/apk-r65/truth.json`, measured by `parse_members` in `generator.py`). A seat authoring a container fixture under §2 today is told the wrong schema, and nothing warns that AXML node `size` includes `headerSize` (M38).

**F10 (low) — §7:223-262 has no round-65 rows and no round-64 worked-entry row.** Missing: `corpus/fixtures/apk-r65/{generator.py,truth.json,readout.py}`; `corpus/knowledge/round-65-apk-axml-byte-evidence.md` (candidate — `admission-status: candidate`, must not be cited as held); `reports/round-65/{claims.md,measure.py,measure-before.log}` with probe sha256; S038/S039/S041 (and S040 `queued` — `corpus/SOURCES.md:52-55`). Also already missing one round back: `corpus/knowledge/round-64-firmware-region-byte-evidence.md`, though §2 rests on that fixture and `corpus/README.md:36` names it. §7's existence promise is unaffected; this is a pointer gap, not a broken citation.

## Minimal edit set (E1–E9) — do not apply here; a later round owns the gate

| # | anchor | edit |
|---|---|---|
| E1 | §1:45-46 | append to the controls cell: languages `; forged evidence_id :155-157 → forged receipt evidence accepted`, multi `; forged evidence_id :154-156 → forged receipt evidence accepted`; move `evidence_id` into guarded, annotated `credit at C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2 at the landing commit; red-before 0/2 (reports/round-65/measure-before.log:45)`. Change no other file:line cell — all verified unchanged. |
| E2 | §1:59-61 | replace "placed after the existing forged-command control" with "appended after the last existing control in `check()` (round-65 C5: after forged-stdout, `reports/round-65/claims.md:35-36`) — appending keeps the `file:line` column above valid; inserting between controls renumbers it". |
| E3 | §1:62-66 | rewrite the status block: C4 `2/2` earned at the round-65 base archive (`reports/round-65/measure-before.log:35`); C5 `0/2` at base (`:45`), credit at `2/2`. |
| E4 | header:6 | add the round-65 half of the split: "§1 ranges and the C5 controls re-read at HEAD `8214e4dd` (11 dirty paths on top); round-64 control ranges committed at `3eebcdd`". Keep the existing round-64-era split verbatim. |
| E5 | §4:109 + table | title → "M33–M38"; add M37 (stale text-scan window; check = whole-file scan + `STRICT_REJECT_WINDOW_SELFTEST`; source `corpus/lessons/round-65.md:30`) and M38 (number-drift; check = §2 byte-verify + derive constants from the spec's field lists; source `round-65.md:29`, `.ufo/waves/round-65/m38-red-before.log`). |
| E6 | §6.1:149-164, §3:344-378 | repoint the instrument to `reports/round-65/measure.py` (`claims.md:69`, sha256 `8a2c69c4…`), fix the §3 snippet's counter path (:363-364), add the six new labels at :158-162 with `HOLDS_OK_V3` = V2 ∧ C5==2/2 ∧ selftest pass, correct `:160` ("round-64 base 1; round-65 base 0") and the red-before values at `:163-164`, and label §3's :376-378 table "round-64 base" while adding the round-65 base row (`K_HELD 8/14`, `C05 frontier`, `8/14/8/14`, `0 rows`, `C4 2/2`, `C5 0/2`, `HOLDS_OK_V3=no`). |
| E7 | §6.4:211, §2:71/:79-80 | add `cp -a corpus/fixtures/apk-r65 /tmp/revenger-r65-apk && (cd /tmp/revenger-r65-apk && python3 -B generator.py)` then byte-compare `fixture.apk` and `truth.json`; state "never run in place — `generator.py:197` writes the fixture and `:226` the truth, and the truth embeds `platform.python_version()`"; add one §2 row for non-compressed container fixtures (sizes/offsets/CRC measured from built bytes; node `size` includes `headerSize` — M38). |
| E8 | §6.5:214-220 | replace the dead `claims.md §Harms` pointer with `reports/round-65/claims.md` §§Frozen counter/Admission order (no Harms section exists); parameterize "outside new round-64 paths" → "outside the current round's registered new paths (round 65: `corpus/fixtures/apk-r65/`, `corpus/knowledge/round-65-apk-axml-byte-evidence.md`, `corpus/lessons/round-65.md`, the C5 insertion lines in the two verifiers)"; add C5 `2/2` and `HOLDS_OK_V3=yes`. |
| E9 | §7:249-251 region | add rows: apk-r65 `generator.py`/`truth.json`/`readout.py` (fixture authoring + oracle shape + byte readout); `corpus/knowledge/round-64-firmware-region-byte-evidence.md` (worked fixture entry); `corpus/knowledge/round-65-apk-axml-byte-evidence.md` (candidate — conditional on admission, never cited as held); `reports/round-65/{claims.md,measure.py,measure-before.log}` + probe sha256 `8a2c69c4…`; S038 (AXML field layout), S039 (route scope), S041 (own-work fixture), S040 (`queued`). Leave every existing row untouched. |

Order matters only in that E1/E2/E6/E8 must land before any seat applies SKILL.md to round 65; E3–E5, E7, E9 complete currency.

## Residual risk and verification gaps

- **C5 after-state not measured here** (out of lane): E1's guarded classification is correct only with `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2` at the landing commit. If the round ends below target, the minimal honest wording is "control landed (:155-157 / :154-156); attribution pending", not "guarded".
- **Line-number drift:** E1/E4's numbers are this working tree's. `grep -n 'forged receipt' corpus/verify_icon_languages.py corpus/verify_multi_icon_states.py` before landing any later insert inside `check()`.
- **§7 content depth:** existence was checked by path presence for all 38 citations; content was re-read only for the citations this sweep used (`reports/round-64/claims.md:84` matches SKILL.md's verbatim quote, `measure.py` sha256 matches). Deeper re-reading of every round-64-era line range is the SKILL gate's job.
- **Not a defect, stated to prevent over-flip:** `corpus/README.md:34` still reads C05 `frontier` and the entry still reads `admission-status: candidate` — correct for build state under `claims.md` §Admission order (step 1 forbids the flip in the candidate commit). SKILL.md must not be edited to claim C05 held on the strength of the candidate.
- No installs or updates were made, so no tooling row applies.
