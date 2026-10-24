# W2VerifyWaveReceipts — wave-1 cohort receipt verification (round 63, falsify wave)

**Seat:** `revenger-r63.W2VerifyWaveReceipts` (scribe) · **Lane:** `/home/vgpnk/Projects/shokunin/revenger-shokunin`
**Date:** 2026-10-24 · **Axis:** calibration · **Scope:** wave-1 (build) cohort evidence only.
**Artifact:** `.ufo/waves/round-63/falsify/cohort.json` (cohort table: name, role, report sha256, one-line verdict, per-report defects).

This seat verified the *existence, non-emptiness, registry coverage and role agreement* of the 32 build-wave
reports. It does **not** judge C1/C2/C3; other falsify seats own those. Nothing under `corpus/` was read as
authority for a claim, no target was executed, and no `corpus/`, `.ufo/waves/*/spec` or registry file was
edited. The only file this seat wrote outside `/tmp` scratch is this report and the cohort table named above.

---

## 1. Verdict

**COHORT COMPLETE — 32/32 receipts present, non-empty, committed, and correctly registered.
Zero missing/empty seat receipts. Seven named receipt defects, all *stale-attestation* (not absence).**

| check | result |
|---|---|
| `R63*.md` files present at `.ufo/waves/round-63/build/` | **32 / 32** |
| each non-empty | **32 / 32** (min 1,931 B `R63SentinelScope.md`; max 34,303 B `R63SourceZipfileDocs.md` working tree) |
| each committed at the lane tip (`HEAD` = `db55bd6488e24e956df5818ae34c2a043d7ddc12`) | **32 / 32** blobs present, none zero-length |
| registry `members` count | **32** |
| registry name set == `build-spec.json` `items` name set | **identical** (0 registry-only, 0 spec-only) |
| registry `role` == spec `role` per member | **32 / 32 match** (0 mismatches) |
| registry `axes` == spec `axes` per member | **32 / 32 match** (0 mismatches) |
| reports present at build-state commit `2a34e45562d965f9c8d32f6a27d2f2efa2e7d04e` | **32 / 32** (cohort was not created by the later commit) |
| **missing reports** | **none** |
| **empty reports** | **none** |

**No seat receipt defect of the "missing / empty report" kind exists.** The defects found are of a different
class: receipts that exist but attest bytes that are *not* the bytes that landed. Those are located by name in
§3. They are calibration-relevant because a receipt that names the wrong object cannot be used as evidence
that the landed object was reviewed.

---

## 2. How this was measured (every counting command re-run by this seat)

```text
$ git ls-tree -r HEAD --name-only .ufo/waves/round-63/build/ | grep -cE 'R63.*\.md$'
32
$ git ls-tree -r 2a34e45562d965f9c8d32f6a27d2f2efa2e7d04e --name-only .ufo/waves/round-63/build/ | grep -cE 'R63.*\.md$'
32
$ git show HEAD:.ufo/waves/round-63/build/<name>.md | wc -c        # per-report size at HEAD
$ git show HEAD:.ufo/waves/round-63/build/<name>.md | sha256sum    # per-report committed digest
$ sha256sum .ufo/waves/round-63/build/<name>.md                   # per-report working-tree digest
```

Registry/spec cross-check was done programmatically on the parsed JSON (not by eyeballing):
`json.load(swarm-registry.json)` vs `json.load(build-spec.json)` → `set(registry.members) == set(spec.items)`
is `True`; per-member `role` and `axes` equality produced **zero** mismatches.

Cross-check of the falsify wave's own registry was also run (not required by the target, cheap):
`.ufo/waves/round-63/falsify/swarm-registry.json` has 32 members, name set identical to
`falsify-spec.json`'s 32 items, **zero** role mismatches, `wave: "revenger-r63-falsify"`, `reportDir`
`.ufo/waves/round-63/falsify`. By contrast the **build** registry has `"wave": null` (§4, non-blocking).

### Cohort role census (32 seats)

| role | seats | role | seats |
|---|---|---|---|
| executor | 8 | critic | 4 |
| scribe | 7 | scout | 3 |
| reviewer | 5 | connector / mutation-tester / revenger / sentinel / simplifier | 1 each |

Per-seat report digest, byte count, one-line verdict, and defect flags are in
`.ufo/waves/round-63/falsify/cohort.json` (`reports[]`, 32 entries; every entry carries a 64-hex
`report_sha256` and a non-empty `verdict`).

---

## 3. Named receipt defects (the substantive finding)

Seven receipts do not attest the bytes that actually landed. Each is a **stale attestation**, not a missing
receipt. All are located by name; all were confirmed by re-deriving the digests myself.

### D1 — `R63EntryC06` attests a superseded candidate
* **Committed** receipt names candidate `630b974a51e0f6ab815a5806a0f415b3f07089df91923dde3a78b6fd49904c7e`
  (74,270 B) and readout stdout `e112d409…`. The **landed** entry
  `corpus/knowledge/round-63-zip-central-directory-evidence.md` at HEAD is
  `a0158e99d3fa4b3cec132e03f5738015c39ca3abb56437ae1bab81e88f2d1b53` and carries stdout `02b0f495…`
  (verified: `git show HEAD:corpus/knowledge/... | sha256sum`).
* **Working tree** copy of the receipt is correct (names `a0158e99…`, 80,126 B, H1–H7/N1–N3 corrections) —
  it is the *committed* blob that is stale.
* **Attacks:** C1 evidence provenance / receipt freshness.

### D2 — `R63ReviewC06Q` reviewed the superseded object
* The only committed fresh-seat Q01–Q13 pass decision names
  "Object reviewed: `/tmp/revenger-r63-entry/candidate.md`, sha256 `630b974a…`, 74,270 bytes, 672 lines" —
  i.e. the **pre-correction** draft, not the landed `a0158e99…` entry (80,126 B).
* Consequence for C1: the committed receipt set contains **no** Q-pass decision over the bytes that are
  actually in `corpus/`. The receipt's own text makes admission conditional on "fresh falsify-wave decisions",
  so this is consistent with the gate — but it means the landed entry is presently unattested by any
  committed Q-pass receipt.
* **Attacks:** C1 admission ordering / receipt freshness.

### D3 — `R63SourcesRows` contradicts the committed `corpus/SOURCES.md`
* Committed receipt still assigns the own-work row to **S034** and calls **S033** "unused", recommending a
  "reserved id went unused" note.
* The **committed** `corpus/SOURCES.md` has `S032` (PKWARE APPNOTE spec) and `S033` (**own-work**, archive-r2
  bytes + saved record) and **no `S034` row** (verified: `git show HEAD:corpus/SOURCES.md | grep -cE '^\| S034 '` → 0).
* The working-tree receipt is correct (renumbering to S033 recorded, "Finding 5 closed", "contiguous pair
  S032 + S033 with no id skipped"). The committed blob is stale.
* **Attacks:** C1 source-row provenance / id-space integrity.

### D4 — `R63LessonDraft` attests a third, non-existent draft digest
* Committed receipt: "sha256 of the draft = `7dda3ff86ab9c06eef760b3f72a211a6f913a1095ce47a3861699a4a59bcbf8d`".
* That digest resolves to **no** blob at HEAD and to **no** file on disk.
* Working-tree receipt names `ce04ac74…`, which **is** the current scratch draft
  (`sha256sum /tmp/revenger-r63-lesson/round-63.md` → `ce04ac74…`).
* The **landed** `corpus/lessons/round-63.md` at HEAD is `ce7b47e8…` — matching neither receipt. The receipt
  describes a *draft for L1 to land*; L1 landed different bytes. The receipt is therefore accurate about the
  draft, but the **committed** receipt's digest is stale and no receipt in the cohort pins the landed lesson.
* **Attacks:** lesson provenance / receipt freshness.

### D5 — `R63LedgerFirmware` touched-surface digest does not resolve
* Receipt table: `corpus/live/runs/round-63/LEDGER.md` — **created** — SHA-256 `cedc8f70…` (22,481 bytes).
* Actual committed file: `d41bbeaccff952800fa2779b0d1d8d626f57eadd79a92185387dc26e6332bb15`, **22,502 bytes**
  (working tree: `25a4a18b…`, 22,671 bytes — the file moved again after the commit).
* The digest `cedc8f70…` resolves to no blob at HEAD and to no file in the working tree.
* **Attacks:** C2 ledger provenance — the receipt cannot be used to identify the ledger bytes it reviews.

### D6 — `R63RevengerLedger` cites the same non-resolving ledger digest
* "LEDGER.md (sha256 `cedc8f70…`, 22,481 bytes, 119 lines): 23 classed rows (O1–O11, I1–I6, U1–U6)".
* Same mismatch as D5: committed ledger is `d41bbeac…` / 22,502 B. The row-count claim itself was not
  re-derived here (out of this seat's scope).
* **Attacks:** ledger discipline review provenance.

### D7 — `R63SourceZipfileDocs` committed blob still presents a landable contingency row
* Working-tree copy resolves the contingency: "**STATUS: not needed and not to be landed**", with L1's
  placement decision and the id note (a future zipfile-docs row would need **S034**).
* The **committed** blob still carries the §7 heading "Contingency S033 row (land ONLY if the integrated entry
  claims zipfile module behavior)" as landable; only the L1 "DROPPED" note in §6 is present in both.
* Consistent with the landed truth (the entry does not quote `truth.json`'s `build` field and asserts no
  zipfile behavior), but a reader of the committed bytes alone would take away a wrong action.
* **Attacks:** source-decision clarity / receipt freshness.

### Supporting observation (not a defect) — `R63CriticCounts` also reviewed `630b974a…`
* Its committed body names candidate `630b974a…` (672 lines) as the reviewed object, and its verdict is
  "numbers numerically SOUND, but the candidate still has Q11 derivation holes and a frozen-scope conflict".
  Those holes were then fixed in the `a0158e99…` revision (H1, H3, H5, H7 …). The critic's *committed*
  verdict therefore reads as an open blocker against an object that no longer exists.
  Recorded here as context for D1/D2; the fix belongs to whoever re-runs the Q-pass on the landed bytes.

### Cross-check: no receipt is unresolvable in the other direction
Of the 95 SHA-256 digests printed across the 32 committed receipts, 44 do not resolve to a blob at HEAD.
Every one was individually classified; none indicates a missing artifact:

| class | examples | status |
|---|---|---|
| digest of a **derived** value, not a file (inflated member bytes, decompressed zlib members) | `a5718481…`, `2d0d86aa…` | legitimate — not file digests |
| digest of an **external binary** | `5fc19aac…` = `/usr/bin/binwalk` (verified byte-for-byte) | legitimate |
| digest of a **scratch file** (candidate draft, readout stdout, `truth.json` variant) | `630b974a…`, `e112d409…`, `c6b54ccc…`, `7dc242eb…` (LF-normalised variant), `c7cf1fec…` (APPNOTE 6.3.9) | legitimate in context, but see D1/D2 |
| digest of a **mutated/false** record used as a negative control | `4653a32e…` (padding-flipped alternate image) | legitimate |
| digest of a **superseded file revision** | `cedc8f70…` (LEDGER.md), `7dda3ff8…` (lesson draft) | **defects D5/D6/D4** |

Only the last class is a defect. The receipt-existence contract itself is clean.

---

## 4. Non-blocking observations (recorded, not counted as defects)

1. **Build registry has `"wave": null`**; the falsify registry has `"wave": "revenger-r63-falsify"`. The build
   registry's `reportDir` is correct (`.ufo/waves/round-63/build`) and its 32 members are correct. Purely a
   metadata gap in the build registry; `falsify-spec.json` states the wave is `revenger-r63-build`.
2. **Registry and reports differ in file mode**: both registries are `0600`, every report is `0644`. Consistent
   within each kind; noted only so a later reader is not surprised.
3. **Nine receipts do not carry their own seat name in the body** (the title line carries a descriptive name
   instead, e.g. `# R63 C3 icon receipt fix` for seat `R63C3IconPatch`). All nine are registered correctly and
   cross-referenced by siblings, so no receipt is unattributable — but seat-name-in-body is not a
   uniform convention across the cohort.
4. **Registry `member` objects carry `"item": null`** for all 32 — the spec linkage is by name only. Name sets
   match exactly, so nothing is orphaned.
5. **Preservation cross-check (context, owned by other seats).** I re-ran the manifest comparison myself
   because it is cheap: `preservation-base.sha256` has 455 records (443 live/fixtures + 12 supplemental). Of
   the 443 baseline rows, **443 still hash identically** and **0 are missing**; the 9 files present in
   `corpus/live` + `corpus/fixtures` but absent from the manifest are exactly the new round-63 paths
   (`corpus/live/runs/round-63/{inspection.json,receipt.json,stdout.raw,stderr.txt,oracle_check.py,LEDGER.md}`,
   `corpus/fixtures/firmware-r63/{firmware-r63.bin,generator.py,truth.json}`). This corroborates
   `R63Preservation` and `R63CriticHarms` (whose finding that hash-only preservation is insufficient, and
   needs a path-delta allowlist, is confirmed by this re-run: the 9 additions are only detectable by path,
   not by digest).

---

## 5. Dependencies on other falsify seats (recorded, not blocking)

* **D1/D2 need a Q-pass over the landed bytes.** `R63ReviewC06Q` (committed) and `R63CriticCounts`
  (committed) both reviewed `630b974a…`. Seats owning the entry's Q01–Q13 re-check (`W2AttackEntryQ01`,
  `W2AttackEntryQ11`, `W2VerifyEntryRecheck`, `W2FinalIndependent`) hold the authority on whether the landed
  `a0158e99…` entry passes; this seat does not duplicate or pre-empt that.
* **D3 needs the SOURCES-row truth.** `W2VerifySourcesTable` / `W2ReopenS032` / `W2ReopenS033` own the row
  content; this seat only establishes that the *committed* receipt and the *committed* `corpus/SOURCES.md`
  disagree about which id is the own-work row.
* **D5/D6 need the ledger's own owner.** `W2VerifyLedger` owns whether the landed LEDGER.md satisfies the
  ledger-discipline rules; this seat establishes only that the committed receipts name a digest
  (`cedc8f70…`) which is not the committed file's digest.
* **D4 needs the lesson gate.** `W2VerifyLessonGate` owns whether the landed `corpus/lessons/round-63.md`
  (HEAD `ce7b47e8…`) is the right bytes; the observation here is that no committed receipt pins them.
* The **build-wave reports are untracked-by-name in the falsify wave**: `.ufo/waves/round-63/falsify/` is
  entirely untracked at HEAD (`git ls-tree -r HEAD .ufo/waves/round-63/falsify/` → empty), so nothing in the
  falsify wave is yet committed. This seat wrote only its two named artifacts and made no git/jj mutation.

---

## 6. Out of scope (deliberately not done)

* No C1/C2/C3 judgement, no counter run, no target execution, no model arguments, no `~/.omp/agent/config.yml`
  edit, no `corpus/` edit, no `.ufo/waves` spec/registry edit, no git/jj mutation, no commit/push/publish.
* No pacman transaction (paused host-wide). **No tool was installed or upgraded by this seat**; `/home/vgpnk/.omp/agent/RULES.md`
  was read first and no install was needed — every check ran on `python3`, `git`, `sha256sum`, `find`,
  `grep` and `ls`, all already present.
* No `/tmp/revenger-r63-*` scratch was created by this seat, so no scratch cleanup is outstanding from here.

---

## 7. Final receipts

| artifact | path | bytes |
|---|---|---|
| this report | `.ufo/waves/round-63/falsify/W2VerifyWaveReceipts.md` | — |
| cohort table | `.ufo/waves/round-63/falsify/cohort.json` | 32 entries (`reports[]`) |

**Cohort table schema:** `reports[]` = `{name, role, axes, agentId, report_path, report_sha256,
report_bytes, worktree_sha256, worktree_bytes, committed_bytes_match_worktree, role_matches_build_spec,
axes_match_build_spec, present_at_head, non_empty, verdict}`; top level carries `totals` (including
`missing_reports: []`, `empty_reports: []`, `role_mismatches: []`, `axes_mismatches: []`,
`committed_vs_worktree_drift: [R63EntryC06, R63LessonDraft, R63SourceZipfileDocs, R63SourcesRows]`),
`receipt_defects[]` (7 named), `measured_revision = db55bd6488e24e956df5818ae34c2a043d7ddc12`,
`build_state_commit = 2a34e45562d965f9c8d32f6a27d2f2efa2e7d04e`, `verdict`, and the `evidence_commands` used.

`report_sha256` is the digest of the report **as committed at the lane tip**; `worktree_sha256` is the
digest of the file currently on disk. They differ for exactly the four drifted receipts, each flagged.
