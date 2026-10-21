GRADE: HOLDS — C04 header/Limitations version pins (`corpus/knowledge/commonjs-destructured-require-edges.md:1-4,8-10,69-71`)

Scope: lane archive ab58069 extracted to /tmp/revenger-r61w3-W3JsVersionPins (live-tree blobs of entry, `SOURCES.md`, both records, both LEDGERs all sha256-SAME as the archive). Read-only; no lane write except this report.

Findings (observation):

1. **6.4.0 is ledger-attested, and the entry says so.** `corpus/live/runs/20261012T164357Z/LEDGER.md:5`: "`npx -y rea-agents@6.4.0 analyze-javascript-application ... --format json` exited 0". `corpus/live/runs/round-7/LEDGER.md:6`: "`npx -y rea-agents@6.4.0 analyze-javascript-application <absolute v2 tree> --format json` exited 0; v2 parent saved once". Entry `:8-10` reads "(`rea-agents@6.4.0 analyze-javascript-application` per the round-3 and round-7 ledgers; recorded, not re-run)" — attribution matches exactly.

2. **The records' own version fields do not name 6.4.0 — they name schema `version: "1"`.** Both records: `provider = {"id":"rea-javascript-application","name":"REA JavaScript application analyzer","version":"1"}`, `operation = analyze_javascript_application`; every edge `evidence.extractor.version` = "1"; literal-string count of "6.4.0" and "6.7.0" in both files = 0. Shas: `20261012T164357Z/analysis.json` 7c3ba8c15673a7e48600bba3f42a6ca3935dbd75e30832569a631979e31ed452; `round-7/v2-analysis.json` 331ec252aefdc7715e49f039d7443736ff9560565f208f35b4c972bfe45d564e. So "one provider version" (entry `:70`) is true under either reading (records: both "1"; ledgers: both 6.4.0), and the entry nowhere claims the record carries the package pin. This is the same distinction build seat `SrcReaJsDocs.md:8-9` drew ("Record-internal version is schema, not package").

3. **"two saved runs from 2026-10-12" holds.** Round-3 dir name `20261012T164357Z`; `LOG.md:90` "## Round 7 declaration — calibration (2026-10-12)" and `LOG.md:97` "## Round 7 result — ... (2026-10-12)"; commits 0ddf650 (2026-10-12T13:44:53-03:00) and fd4ba3d (2026-10-12T14:06:20-03:00). Neither record has an internal timestamp (`environment` null), so the date is ledger/commit-attested; the entry's "recorded, not re-run" is the correct hedge.

4. **"host skill now names `rea-agents@6.7.0` (S002)" holds.** `~/.agents/skills/reverse-engineer-anything/SKILL.md:5` `version: "42"`, `:6` `tool_count: 207`, `:37/:51/:56` `npx -y rea-agents@6.7.0 ...`; file mtime 2026-10-20 13:35, read 2026-10-21. `corpus/SOURCES.md:16` (S002, tier A) anchors exactly "setup commands naming `rea-agents@6.7.0` (lines 37-56)". `seed.md:60`/`LOG.md:775` corroborate the 6.4.0→6.7.0 pin change with "6.4.0 remains the saved-record producer version".

5. **Header `verified-at` base is real and byte-consistent.** `e0a4b0c` = 2026-10-21T12:05:33-03:00 ("round-61: pre-register claims..."), ancestor of 0b6ddf0 and ab58069. `git rev-parse` of all six fixture files plus both record files at e0a4b0c vs ab58069: 8/8 SAME. The entry file itself is new at 0b6ddf0 (`git diff e0a4b0c ab58069` shows `new file`), but the header claims only "fixture bytes and saved records re-derived", which is what reproduces.

6. **Reproduce block re-run on the ab58069 archive: exit 0; all 29 output lines byte-identical to the `## Provenance` block** (`difflib` diff: IDENTICAL). S027 (`SOURCES.md:41`, own-work tier A, mined 2026-10-21) anchors both Evidence IDs the entry cites at `:1`.

Boundary observed, not a break:
- `SOURCES.md:16` (S002) says opened 2026-10-19, not round 61, and its `used-by` lists only `seed.md`; the 6.7.0 statement is still true and was re-read in round 61 (`build/SrcReaJsDocs.md:6`). C1's "at least one row opened in round 61, tier A" is met by S020-S023 and S027 (all opened 2026-10-21, `SOURCES.md:34-37,41`).
- Q04 basis wording "recorded version named" (`entry:Q04` row) is loose: the record's own version is "1"; the 6.4.0 named is the ledger's invocation pin. The entry's own prose does not conflate them.

No contradiction found between the header/Limitations and the ledgers, records, `SOURCES.md`, `LOG.md`, or the installed skill. No harm in the version-pin sentences; C04's K admission is not voided by this item.

VERDICT: HOLDS — 6.4.0 is correctly attributed to both ledgers (records themselves carry provider/extractor version "1"), 2026-10-12 is supported by LOG.md:90,97 and both commits, and the 6.7.0 skill pin is confirmed by SKILL.md:37/51/56 and S002.

Installs: none.
