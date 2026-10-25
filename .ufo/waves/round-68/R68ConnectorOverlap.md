# R68ConnectorOverlap — sibling adjacency scan of the round-68 claims

**CONTEST-NAMED** — the *province* is named and open (ADJ-06: kaidoku/revenger shipped-artifact overlap, unarbitrated at fleet `l0-questions.md`), but none of the three claim *subjects* is contested: the AXML chunk-type anchors are **NO-OVERLAP** (0 sibling hits), the C7 embedded-output gate concept is **CONTEST-NAMED** only at concept level via tameshi's `RevengerWitness` rule (partitionable, no absorption), and the APK container / dex declared-header ground is **CONTEST-UNNAMED** (kaidoku claims the noun through provider-mediated decode, never the bytes). Revenger's C1 and C2 **stay inside revenger's own province**.

Read-only seat. Nothing written outside this file; no lane, fleet, jj or Git mutation.

## 1. The province is named, and it is not about AXML

| pointer | text (verbatim excerpt) | what it names |
|---|---|---|
| `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` (tsukuroi round-1 row) | "arbitrate the **kaidoku/revenger shipped-artifact overlap** before an ADJ-06 analysis is routed" | fleet-level, **CONTEST-NAMED**, unresolved |
| `/home/vgpnk/Projects/shokunin/kaidoku-shokunin/PROVINCE.md:242` | "remain unheld/Adjacent; **kaidoku/revenger arbitration is still open**" | named |
| `/home/vgpnk/Projects/shokunin/kaidoku-shokunin/PROVINCE.md:274,305` | "Both live debugger verbs remain Adjacent/unheld; the **kaidoku/revenger** arbitration is open" | named — subject is **live debugger verbs**, not AXML |
| `/home/vgpnk/Projects/shokunin/kaidoku-shokunin/SKILL.md:677` | "The **kaidoku/revenger dynamic-analysis boundary** remains an open L0 question" | named — subject is **dynamic analysis** |
| `/home/vgpnk/Projects/shokunin/kaidoku-shokunin/.ufo/waves/round-29/w1/ConnectorSiblings.md:19` | "**Ownership contradiction:** `revenger-shokunin/PROVINCE.md:3-7` broadly claims the same shipped-artifact RE domain … **[Unknown]** Final route ownership" | named at the **domain** level (EVM/selector ground in that report) |
| `/home/vgpnk/Projects/shokunin/kaidoku-shokunin/SCORECARD.md:3172` | "Sibling overlap: the only substantive overlap is in **revenger**, which the lane cites and does not absorb" | named |
| `/home/vgpnk/Projects/shokunin/kaidoku-shokunin/SCORECARD.md:3207` | "sibling overlap: **revenger** direct overlap and an unresolved ADJ-06 ownership question, cited not absorbed" | named |

The existing contest is EVM/selector ground (rounds 28–29) plus live-debugger/dynamic-analysis verbs. **No sibling names revenger for AXML, for `AndroidManifest.xml` byte layout, or for a dex declared header.**

## 2. Zero-hit receipt for both round-68 claim surfaces

```
$ cd /home/vgpnk/Projects/shokunin && for d in <20 sibling lanes>; do \
    h=$(grep -rlE "RES_XML_|AXML|ResourceTypes\.h|check_embedded_outputs|drifted entry output accepted" \
        "$d/corpus/knowledge" "$d/SCORECARD.md" 2>/dev/null | wc -l); printf "%-24s %s\n" "$d" "$h"; done
audio-shokunin           0
chousa-shokunin          0
game-dev-2d-shokunin     0
game-dev-3d-shokunin     0
kagi-shokunin            0
kaidoku-shokunin         0
kake-shokunin            0
kama-shokunin            0
kasegi-shokunin          0
kengaku-shokunin         0
kotoba-shokunin          0
kotodama-shokunin        0
kumitate-shokunin        0
lore-shokunin            0
mado-shokunin            0
mori-shokunin            0
souji-shokunin           0
tabi-shokunin            0
tameshi-shokunin         0
tsukuroi-shokunin        0
```

Wider sweep over the same lanes (corpus trees, `--exclude-dir=.git/.ufo/.scratch`) for `AOSP|ResourceTypes|chunk.?type|RES_XML|binary xml|AndroidManifest` returned only **format-unrelated** false friends, each checked and discarded:

- `game-dev-3d-shokunin/reports/round-98/r98-boundary.md:172` — GLB `chunk_type != 0x4E4F534A` (KHR binary glTF, not AXML).
- `game-dev-3d-shokunin/reports/frontier/bpy-boundary.md:45` — "PNG chunk inventory" (raster container).
- `kotodama-shokunin/corpus/SOURCES.md:451` — `legislation.gov.uk/aosp/1672/47` (a 1672 Scots statute path; `aosp` here is the archive prefix, not Android).

`REA`/`apktool`/`jadx` mentions elsewhere are provider rows, not AXML structure.

## 3. Per-subject verdicts

### 3.1 AXML chunk-type anchors (C2) — **NO-OVERLAP**

No sibling corpus entry or SCORECARD states a compiled-XML chunk-type enum value, a `ResChunk_header` layout, or an AOSP `ResourceTypes.h` line anchor (§2: 0/20). kaidoku is the nearest lane and its knowledge index carries **no** AXML/binary-XML claim: `grep -rniE "axml|binary xml|chunk header|RES_XML|offset table|string pool" kaidoku-shokunin/corpus/knowledge kaidoku-shokunin/corpus/README.md` returns one unrelated hit — `corpus/README.md:72` "legacy-layout Saber libapp headers complete but **string pool partial**" (Dart AOT layout, round 23).

### 3.2 APK container / dex declared header — **CONTEST-UNNAMED**

kaidoku claims the surface by **noun and by provider**, never by bytes:

- `kaidoku-shokunin/PROVINCE.md:56` — "`| APK surface (full) | rea inspect-artifact content graph; inspect-android-package (jadx-headless-mcp 0.7.1); decode-android-resources (apktool 3.0.3); … | Godot android_debug.apk: 120 nodes verified (r3-06); 1,925 classes + **full manifest decode** (r4u-02) |`" — the subject is *what the tool returns*.
- `kaidoku-shokunin/corpus/knowledge/2026-10-13-r3-apk-inventory.md` (Summary + node-format histogram) — "`file`×110 (dex, res, manifest — **dex/xml get no format-specific detection**)" and "Frontier: **dex/manifest semantics (blocked on jadx/apktool)**". kaidoku's own held artifact graph terminates *before* the byte layer revenger's C05 walks.
- No sibling claims a dex declared header: `grep -rniE "dex header|dex_header|classes\.dex.*header|declared.header"` across sibling corpus trees → only audio/WAV and GLB/GGUF **declared-header** rows in other formats (`audio-shokunin/reports/round-57/r57-reviewer.md:13`; `kama-shokunin/SKILL.md:659` `gguf-identity.py`) — methodology precedent, disjoint subject.

Adjacency to record, not absorb: the "declared header" *method* is a fleet pattern (kama's `tools/gguf-identity.py` probe, `SKILL.md:659`), so revenger's C05 dex-header leg is not methodologically novel. Its **subject** — one authored APK's `classes.dex` `header_item` fields against an authored oracle — is untouched fleet-wide.

### 3.3 C7 embedded-output gate concept — **CONTEST-NAMED** (concept level), partitionable

| pointer | what it holds | naming |
|---|---|---|
| `tameshi-shokunin/corpus/knowledge/witness-equivalence-rule.md:29` §"Why the set-blind predecessor was voidable (**RevengerWitness, round 33**)" | the fleet-general **set-aware witnessed-kill** rule: a `kill` copy whose only edit is inert "validated as a must-kill; the tool PASSes it → the claim voids with a blameless tool" | **CONTEST-NAMED** — names a revenger seat as the counter-example source |
| `tameshi-shokunin/corpus/knowledge/mutation-score-semantics.md` (Verdict vocabulary, shmutant column) | "**killed** only if the named witness fails; red elsewhere is **accidental**, not a kill … Tameshi records failing labels but **no per-mutant witness**, so its Killed cannot be split" | unnamed here, but it states exactly the gap `C7_MUTANT_KILLED_ATTRIBUTED` closes |
| `kama-shokunin/corpus/knowledge/self-assessment-at-writing.md:16` | claim class **Q — quoted output**: the span "must occur verbatim in a blob of the tree at `W`, excluding `SCORECARD.md`, `SHONEN.md`, `LOG.md`, and `corpus`" | **CONTEST-UNNAMED** |
| `kotodama-shokunin/corpus/lessons/round-20.md:138`; `reports/round-20/readme/{reconcile,verify}.md` | a verbatim comparison gate over corpus text — round-19's tool "never compared row text with file content", repaired to zero mismatches | **CONTEST-UNNAMED** |

Partition, stated so no seat can later claim absorption:

- **tameshi** owns the *rule* for sealed held-out mutation copies (witness must demonstrate the labelled behaviour, branching on the copy's set). Revenger's C1 is one **lane-local instance**: a gate's own self-test must fail *with its registered marker last*, and the spoof negative control (`C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1`) is tameshi's "red elsewhere is accidental, not a kill" applied to a marker string. Revenger's `reports/round-68/claims.md` C1 claims no novelty of the rule — only the repair of this lane's attribution — so nothing is absorbed and nothing is duplicated.
- **kama's Q class and revenger's C7 gate are complementary, not overlapping**: kama's check is `git grep -F` of a span in a tree blob at `W` and **explicitly excludes `corpus`**; revenger's gate *only* runs on `corpus/` entries and re-executes the entry's declared `$ <command>`, requiring every output line to appear in that command's stdout. Kama cannot verify the command prints it (its exclusion removes the corpus); revenger cannot verify a non-command quotation. Together they cover both halves; neither covers the other's.
- **kotodama's** verbatim comparison is over README-row ↔ entry `- topic:` text, not command output — same failure *class* (transcription drift), disjoint enforce mechanism.

Nothing in §3.3 intersects the fuel of C1 (`corpus/check_embedded_outputs.py`, its registry row, the counter labels). The gate is registered in the **revenger-owned** registry (`revenger-shokunin/SKILL.md:262-272`, `## Gate registry`, owner revenger); the fleet `## Gate registry — protocol lane registry home` (`/home/vgpnk/Projects/shokunin/SCORECARD.md:177`) is the *protocol-lane* home and holds only `closure-check` and `root-ledgers` — no sibling registers revenger's gate concept.

## 4. Do the claims stay inside revenger's province? — **Yes, on the byte layer; the reciprocity gap survives**

**C2 stays inside, on three independent grounds.**

1. Subject test (the discriminator already routed in `revenger-shokunin/.ufo/waves/round-61/build/ConnectorKaidokuOverlap.md:20`: "the noun is not the discriminator — the claim's *subject* must be"). kaidoku's subject is tool output on a real APK; the C05 v3 subject is byte layout of one authored fixture against an authored oracle.
2. The v3 entry fences the provider ground itself, five separate times:
   - `corpus/knowledge/round-68-apk-axml-byte-evidence.md:8` — "Not covered: … provider (`inspect_android_package`) readiness or output, general AXML or ZIP-parser behavior beyond this fixture."
   - `:158` — "nothing about install validity, signature blocks, dex program validity or **any provider's behavior** is claimed; the fixture is inert and no producer was called."
   - `:162` — "Generalization to other APKs, other AXML producers or the `inspect_android_package` provider would need its own evidence."
   - `:166` — "The provider route (`inspect_android_package`, JADX prerequisites) is documented scope from S043 only; this lane ran no provider and makes no readiness claim (Q05 fence). **The kaidoku/revenger ADJ-06 overlap and fleet `l0-questions.md:42` remain reported-not-absorbed**, unchanged from round 64."
   - `:176` Q05 — "pass | no readiness or capability claim is made".
3. `corpus/SOURCES.md` S046 is **own-work** (revenger's own `derive_axml_anchors.py`), and S038/S045 are AOSP upstream specs; no sibling corpus entry is used as source support (sibling knowledge is not tier-A).

**The gap that survives, reported and not applied (no edit made):** the split is adopted **one way only**. kaidoku `PROVINCE.md:66-71` takes revenger's r1 connector split as *its own routing authority* — "never stands for that lane's current runtime capability (routing: `../revenger-shokunin/reports/round-1/connector.md:25,33-36`)" — while `grep -c kaidoku revenger-shokunin/PROVINCE.md` → **0**. So every round in which revenger flips a row on a ground kaidoku also claims by noun (APK: `PROVINCE.md:56`), the reciprocal provenance line that would make the partition citable is still missing from revenger's own province text. A C2 flip would be the third such round (r61 C04/C09, r63–r64, now r68 C05).

Bounded move available to the L1, not taken here: one provenance line in `revenger-shokunin/PROVINCE.md` state that *provider capability/version/readiness claims on APK tooling are kaidoku's (`../kaidoku-shokunin/PROVINCE.md:56,127`); this lane's APK claims are authored-fixture byte facts; ADJ-06 is unarbitrated (`.ufo/l0-questions.md`)*. It is a `PROVINCE.md` edit — outside this seat's write bounds and outside `reports/round-68/claims.md`'s declared change surface (C1 touches only `corpus/check_embedded_outputs.py` + counter labels; C2 only a new knowledge entry + one README row), so it is **reported only**. Adding it would be a void-condition risk under the frozen contract (any write outside the lane repo + this round's report path is void) — flagging rather than applying is the safe call.

## 5. Risks

- **Naming debt, not claim debt.** The ADJ-06 contest is recorded at fleet `l0-questions.md` and in kaidoku's ledgers but has **zero occurrences in revenger's `PROVINCE.md`**. If an outside closure reads only revenger's side, the contest looks one-sided (§4).
- **Concept-collision risk on C1 wording.** `C7_MUTANT_KILLED_ATTRIBUTED` and the spoof control restate tameshi's `witness-equivalence-rule.md` at lane scope. Risk is presentation, not priority: if any seat writes C1 up as a *new* fleet rule for attributed kills, that seat is claiming tameshi's ground. The frozen claim text does not do this (§3.3).
- **False-friend on "round 68" + "gate".** `kotoba-shokunin/corpus/knowledge/client-trust-gates-round68.md` is a same-round, same-word artifact about *client skill trust gates* (`verifiers/check_client_trust_gates.py --rev <rev>`, `corpus/README.md:128`). It shares a round number and the word "gate" and nothing else; it must not be cited as either prior art or corroboration for C7.
- **Silence is not proof.** §2's sweep covers the 20 sibling lanes' `corpus/knowledge/` + `SCORECARD.md` plus corpus-wide `--exclude-dir=.git/.ufo/.scratch` sweeps. Unindexed synonyms, ignored binaries, `.ufo/` wave scratch and Git object history are outside the receipt — this is not fleet-wide novelty proof.

## 6. Axes

- **Adjacency (this seat's axis):** improved — three subject verdicts with pointers and a 0/20 receipt, plus the one-sided-split finding that no prior round recorded on the r68 surface.
- **Coverage (C2):** unaffected by this report; the added finding is that no sibling pre-owns the anchors, which strengthens the C05 admission basis without touching the counter.
- **Calibration (C1):** unaffected; the gate registry provenance is revenger-owned and no sibling registers the concept.
- **No axis harmed:** no file outside this report written, no counter edited, no claim text changed.

## 7. Tooling

No install or upgrade performed; pacman transactions paused host-wide and not needed. Commands used were stock `grep`/`ls`/`sed`, `python3` not invoked.
