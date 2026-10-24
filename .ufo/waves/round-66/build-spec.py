#!/usr/bin/env python3
"""Build .ufo/waves/round-66/wave-spec.json — revenger r66 verification wave.

v2-band spec (64 seats): read-only verifiers of the round-66 landed work
(C05 disposition + C6 controls + gate marks + fleet report + ledger hygiene).
Prepared-but-undispatched per the accepted host mapping; the orchestrator
dispatches between rounds. Validation: ufo-swarm-wave.mjs plan under
scripts/hyaku/ufo-wave-policy-v2.json.
"""
import json, pathlib

LANE = "/home/vgpnk/Projects/shokunin/revenger-shokunin"
REPORT_DIR = ".ufo/waves/round-66"

GODSPEED = """---
name: godspeed
description: >
  Godspeed posture — name the axes, iterate cheap in parallel, keep moves that
  improve any axis and harm none, and don't aim (let the frontier walk itself).
  Stops clarifying questions and verbose planning in favor of large concurrent
  tool-call batches. Use for any task framed with godspeed. Triggers: "godspeed",
  "--with godspeed", "/skill:godspeed", or a task marked with godspeed framing.
---
You are a Godspeed-enabled subagent.

1. **Name the axes.**
2. **Iterate cheap, in parallel.**
3. **Keep moves that improve any axis and harm none.**
4. **Don't aim — let the frontier walk itself.**

## IMMEDIATELY STOP ASKING CLARIFYING QUESTIONS. Execute tool calls concurrently in large batches. Do not serialize what can run in parallel. Do not output philosophical reasoning or verbose plans. Act directly via tool calls.


Time-box: return within 15 minutes with your best findings+evidence; partial results are acceptable.
You are an independent leaf: never block on or wait for another seat; if a needed artifact is absent, record the dependency as a finding and return.
"""

CONTEXT = """# Goal
Revenger round 66 attempt 1 (hyaku) — ONE v2-band verification wave of exactly 64 seats over the LANDED round-66 tree. Lane repo: /home/vgpnk/Projects/shokunin/revenger-shokunin — ABSOLUTE paths only in every read/write (your tools start at the fleet root /home/vgpnk/Projects/shokunin). Frozen contract (read first): /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-66/claims.md; frozen counter: /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-66/measure.py (sha256 a59914e9199ac2fd49cf0bca40ea152a74823a63ecd300fae2fe45ee42ebf1da); receipts: reports/round-66/measure-before.log (base 8214e4dd, K 8/14, K_ROW C05=frontier, C05_REJECTED_MARKED=no, C6 0/4, HOLDS_OK_V4=no) and reports/round-66/measure-after.log (committed tip). Claims this wave audits: C1 = the frozen round-65 admission order executed (fresh Q01–Q13 named, C05 flipped frontier→uncovered on FALSIFIED, candidate retained rejected); C2 = C6 calibration (C6_RECEIPT_KILLED_ATTRIBUTED 4/4 on the committed tip). All seats are READ-ONLY: never write into corpus/, never commit, never flip any status, never touch .ufo/state/watchdog.log or sibling lanes. Every `Report:` trailer path is relative to /home/vgpnk/Projects/shokunin/revenger-shokunin — write it at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-66/<name>.md.

# Contract
- Re-verify by command; quote the command and its output tail in your report.
- A PASS needs reproduced evidence; a FAIL needs the exact divergent bytes.
- Attacks are encouraged: a falsification is a useful finding, never a failure of the seat.
"""

def seat(name, role, target, axes=("coverage", "calibration")):
    prompt = (GODSPEED
        + "\n# Target\nSeat brief: " + target + "\n\n"
        + "Report: " + REPORT_DIR + "/" + name + ".md — write your verdict + evidence at the ABSOLUTE path "
        + LANE + "/" + REPORT_DIR + "/" + name + ".md (the trailer path is relative to " + LANE + ").")
    return {"name": name, "role": role, "axes": list(axes), "prompt": prompt}

CORPUS = LANE + "/corpus"
items = [
    # --- core re-measurement + C6/C5/C4/C3/C2 attribution attacks ---
    seat("R66CounterReplay", "executor",
        "Re-run the registered measurement end-to-end on the committed tip: `git -C " + LANE + " archive <tip> corpus | tar -x -C /tmp/revenger-r66-counter-<rand>`; `cd / && TMPDIR=/tmp/revenger-r66-counter-<rand> python3 -B " + LANE + "/reports/round-66/measure.py /tmp/revenger-r66-counter-<rand>`; diff every label line against " + LANE + "/reports/round-66/measure-after.log; report any divergence byte-exact (expect K_HELD=8/14, K_ROW C05=uncovered, C05_REJECTED_MARKED=yes, C6_RECEIPT_KILLED_ATTRIBUTED=4/4, README_TOKEN_LEGEND_MISMATCH=0, HOLDS_OK_V4=yes, exit 0)."),
    seat("R66CounterBase", "executor",
        "Re-run the same frozen counter on the BASE archive `git -C " + LANE + " archive 8214e4dd corpus` under a distinct /tmp/revenger-r66-base-<rand>; diff labels against " + LANE + "/reports/round-66/measure-before.log — confirm the red-before (C05 frontier, C6 0/4) reproduces exactly."),
    seat("R66C6KillIconExit", "mutation-tester",
        "Copy " + LANE + "/corpus to /tmp; in verify_icon_languages.py delete the `exit_code==0` conjunct inside `receipt_ok` (exactly one regex match); `python3 -B verify_icon_languages.py --self-test` must exit non-zero, last line ending `forged receipt exit accepted`. Report command + last line verbatim."),
    seat("R66C6KillIconFix", "mutation-tester",
        "In a /tmp copy of " + LANE + "/corpus, delete the `fixture_sha256==expected_hash` conjunct inside `receipt_ok` in verify_icon_languages.py (one match); self-test must exit non-zero, last line ending `forged receipt fixture accepted`."),
    seat("R66C6KillMultiExit", "mutation-tester",
        "Same exit_code-conjunct deletion attack on a /tmp copy of " + LANE + "/corpus/verify_multi_icon_states.py; expect non-zero, last line `forged receipt exit accepted`; unmutated self-test green first."),
    seat("R66C6KillMultiFix", "mutation-tester",
        "Same fixture_sha256-conjunct deletion attack on a /tmp copy of " + LANE + "/corpus/verify_multi_icon_states.py; expect non-zero, `forged receipt fixture accepted`."),
    seat("R66C6InsertionAudit", "reviewer",
        "Diff `git diff 8214e4dd <tip> -- corpus/verify_icon_languages.py corpus/verify_multi_icon_states.py`: must be exactly 6 insertions / 0 deletions each, all inside check(); `receipt_ok` bodies untouched; controls placed AFTER the forged-evidence control. Report the diff verbatim."),
    seat("R66C5HoldIcon", "mutation-tester",
        "Regression: in a /tmp copy, delete the `evidence_id` conjunct in " + LANE + "/corpus/verify_icon_languages.py receipt_ok (one match); expect non-zero + `forged receipt evidence accepted`. Confirms the round-65 C5 control still kills after the C6 append."),
    seat("R66C5HoldMulti", "mutation-tester",
        "Same evidence_id-conjunct deletion on a /tmp copy of verify_multi_icon_states.py; expect `forged receipt evidence accepted`; unmutated green."),
    seat("R66C4HoldIcon", "mutation-tester",
        "Regression C4: delete the `stdout_sha256` conjunct in a /tmp copy of verify_icon_languages.py receipt_ok; expect non-zero + `forged receipt stdout accepted`."),
    seat("R66C4HoldMulti", "mutation-tester",
        "Regression C4: same stdout_sha256-conjunct deletion in verify_multi_icon_states.py; expect `forged receipt stdout accepted`."),
    seat("R66C3HoldIcon", "mutation-tester",
        "Regression C3: delete the `command==` conjunct in a /tmp copy of verify_icon_languages.py receipt_ok; expect non-zero + `forged receipt command accepted`."),
    seat("R66C3HoldMulti", "mutation-tester",
        "Regression C3: same command-conjunct deletion in verify_multi_icon_states.py; expect `forged receipt command accepted`."),
    seat("R66C2HoldIcon", "mutation-tester",
        "Regression C2: mutate one byte in a saved receipt's raw_bytes region used by verify_icon_languages.py self-test in a /tmp copy; the mutated receipt must be rejected (find the exact mutant the counter uses at reports/round-66/measure.py and re-run that single variant)."),
    seat("R66C2HoldMulti", "mutation-tester",
        "Same byte-mutation regression for verify_multi_icon_states.py using the counter's documented mutant."),
    # --- C05 disposition + candidate retention ---
    seat("R66ReadmeC05Row", "reviewer",
        "Byte-diff `git show 8214e4dd:corpus/README.md` vs committed-tip README: the C05 coverage-map row must read `uncovered`, the ## Frontier C05 paragraph must name fixtures/apk-r65 + the retained rejected candidate, and NO other row's status word may change. Report the full delta."),
    seat("R66RejectedMarker", "reviewer",
        "Verify " + CORPUS + "/knowledge/round-65-apk-axml-byte-evidence.md has `admission-status: rejected` AND differs from `git show c7b7cf9:corpus/knowledge/round-65-apk-axml-byte-evidence.md` only on that one line; verify the two round-61 retained rejects (list them via grep `admission-status: rejected` across corpus/knowledge) still carry their markers."),
    seat("R66AdmittedMarkers", "reviewer",
        "Verify `admission-status: admitted` now sits on " + CORPUS + "/knowledge/round-63-zip-central-directory-evidence.md and round-64-firmware-region-byte-evidence.md, each differing from its admitted-round blob only in the header line (the stale-`candidate` repair, claims.md §Registered)."),
    seat("R66GateFailReverify", "reviewer",
        "Re-run the three gate FAILs by command: (a) `python3 -B " + CORPUS + "/fixtures/apk-r65/readout.py --fact 'member[META-INF/MANIFEST.MF]'` prints payload_first16_hex 4d616e69666573742d56657273696f6e vs entry:41's 4d616e696673742d56657273696f6e; (b) RES_XML_RESOURCE_MAP_TYPE sits at snapshot ResourceTypes.h:253 not cited :239-250; (c) rea snapshot line 5 reads `older server.` not the quoted anchor. Confirm all three FALSIFY the candidate at committed bytes."),
    seat("R66GatePassReverify", "reviewer",
        "Spot-verify three PASS decisions from the lesson table: Q01 tier-A rows in " + CORPUS + "/SOURCES.md cover the entry's load-bearing claims; Q09 entry digests re-derive (recompute two sha256s the entry prints); Q13 no verifier is credited for unguarded value. Report reproduced evidence."),
    seat("R66OrderAudit", "critic",
        "Adversarial order check: read reports/round-65/claims.md:110-123 (frozen either-way order) + reports/round-66/claims.md. Did round-66 execute it faithfully — Q decisions fresh-seat (non-author) from the orchestrator-dispatched 64-seat wave, falsification branch flip, measurement AFTER the disposition on the committed tip? Find any order violation or missed honest-stop requirement."),
    seat("R66WaveCompleteness", "critic",
        "Enumerate " + LANE + "/.ufo/waves/round-65/: count R65*.md reports (expect 64 seats + spec + source-snapshots); confirm the spec's items count 64 and every item name has a non-empty report; list any missing/dead seat."),
    seat("R66SeatMixCheck", "critic",
        "Recompute the r65 wave-spec role mix from the committed spec (`python3 -c \"import json,collections;print(collections.Counter(i['role'] for i in json.load(open('" + LANE + "/.ufo/waves/round-65/wave-spec.json'))['items'])\"`) and compare against the mix printed in the fleet round-65 report — the round-66 lesson records the erratum (scribe 4, not 3)."),
    seat("R66C05UncoveredSemantics", "critic",
        "Attack the disposition semantics: is `uncovered` the right token (vs `frontier`) per the frozen order's falsification branch and corpus/README.md's own legend? Check the legend row for `uncovered`, confirm token is defined there, and that `README_TOKEN_LEGEND_MISMATCH=0` in measure-after.log agrees."),
    # --- SOURCES / citations ---
    seat("R66SourcesCensus", "scout",
        "Run the census: `grep -cE '^\\|[[:space:]]*S[0-9]{3,}[[:space:]]*\\|' " + CORPUS + "/SOURCES.md` (expect 44); the awk NF!=13 malformed-row scan (expect 0); `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --today 2026-10-24 " + LANE + "` exit 0; confirm S042/S043/S044 rows and that no prior row's status/tier changed vs `git show 8214e4dd:corpus/SOURCES.md`."),
    seat("R66S042RowAudit", "reviewer",
        "Audit the S042 row: source path `.ufo/waves/round-65/` exists with 64 reports; status wording is consistent with own-work/mined usage; the row cites the correct lane-relative path and the search-log retro note matches it."),
    seat("R66S043Anchor", "reviewer",
        "Verify S043's corrected anchor: re-open " + LANE + "/.ufo/waves/round-65/source-snapshots/rea-android-applications.md — lines 7-8 must contain the route-scope sentence S043 quotes; confirm the row declares `supersedes S039` and S039 is unchanged (immutability)."),
    seat("R66S044Title", "reviewer",
        "Verify S044's corrected title against " + LANE + "/.ufo/waves/round-65/source-snapshots/zipfile-docs.html <title> (Python 3.15.1); confirm `supersedes S040`, S040 unchanged, and the row is marked `queued` per the tier rule."),
    seat("R66SearchLog", "reviewer",
        "Verify SOURCES.md `## Search log` gained both the retro round-65 note (R65ReviewSources F3) and the round-66 note; dates 2026-10-24; the notes name the S-ids they touch."),
    seat("R66SkillCitePaths", "reviewer",
        "Existence-check every `exists at` path in " + LANE + "/SKILL.md §7 table at the committed tip (round-64/65/66 reports, fixtures/apk-r65 files, both knowledge entries, both lessons, S038/S041-S044 rows resolvable in corpus/SOURCES.md). List any dangling citation."),
    seat("R66SkillCounterBlock", "reviewer",
        "Audit " + LANE + "/SKILL.md §3: it must name reports/round-66/measure.py + sha256 a59914e9… and the r66 label set; §6.1 must name reports/round-66 paths + /tmp/revenger-r66-*; §6.2 must contain all seven census commands; §6.4 must carry the apk-r65 scratch-only regeneration warning."),
    seat("R66LessonAccuracy", "reviewer",
        "Audit " + LANE + "/corpus/lessons/round-66.md: the Q01–Q13 table names a seat report for each criterion and the verdicts match those reports' header lines; the Mistakes M39–M41 rows have evidence pointers that resolve; `## Gate — source rows` lists exactly S042–S044."),
    # --- fixture/evidence byte-holds ---
    seat("R66FixtureByteHold", "sentinel",
        "Verify `git diff 8214e4dd <tip> -- corpus/fixtures corpus/live` is EMPTY (no byte changed outside registered new paths — round-66 registers none under fixtures/live); list any offending path."),
    seat("R66ApkRegen", "executor",
        "Scratch regen: `cp -a " + CORPUS + "/fixtures/apk-r65 /tmp/revenger-r66-apkchk && (cd /tmp/revenger-r66-apkchk && python3 -B generator.py)`; byte-compare fixture.apk + truth.json against the committed pair (sha256 fixture 05d2280f…). Confirm identical; never run generator in place."),
    seat("R66FwRegen", "executor",
        "Scratch regen: `cp -a " + CORPUS + "/fixtures/firmware-r63 /tmp/revenger-r66-fwchk && (cd /tmp/revenger-r66-fwchk && python3 -B generator.py)`; byte-compare both outputs against committed originals."),
    seat("R66SavedRecordsHold", "sentinel",
        "Confirm `git diff 8214e4dd <tip> -- corpus/live` empty and SAVED_RECORDS still counts 59 at the after run (check measure-after.log); confirm FRESH_ROWS=18/18 unchanged."),
    seat("R66TenVerifierReplay", "executor",
        "Replay all ten corpus verifiers' `--self-test` from " + CORPUS + ": every exit 0; paste each exit code in order; flag any non-zero (the census probe label is HOLD_REPLAY=10/10 in measure-after.log)."),
    seat("R66LiveRunsHold", "sentinel",
        "Verify no corpus/live/runs/* file changed vs 8214e4dd (git diff --stat on that subtree must be empty); the oracle_check inputs are untouched."),
    seat("R66OracleReplay", "executor",
        "Run `python3 -B " + CORPUS + "/live/runs/round-63/oracle_check.py` from the lane root; expect `ORACLE OK` exit 0, five REGION lines (LEDGER.md O6 shape)."),
    seat("R66WatchdogIntact", "sentinel",
        "Confirm the lane did not touch fleet state: `git -C /home/vgpnk/Projects/shokunin status --porcelain .ufo/state/watchdog.log` must show no modification by this lane; `git diff` on other lanes' dirs from the tip must be empty."),
    # --- report / scorecard / LOG / SHONEN ---
    seat("R66FleetReportAudit", "reviewer",
        "Read /home/vgpnk/Projects/shokunin/.ufo/reports/round-66/revenger.md once landed: verify it cites the pushed lane tip hash, states C1 FALSIFIED→uncovered and C2 4/4, names the 64-seat r65 wave as decision authority, reports zero in-seat dispatch, and exceeds no evidence."),
    seat("R66ScorecardAudit", "reviewer",
        "Audit " + LANE + "/SCORECARD.md round-66 section: every before→after number matches measure-before.log vs measure-after.log (K 8/14→8/14, C05 frontier→uncovered, C6 0/4→4/4, holds 4/4+10/10, HOLDS_OK_V4 no→yes). Flag any drift or unmeasured claim."),
    seat("R66LogLine", "reviewer",
        "Check " + LANE + "/LOG.md newest entry names round 66, both claim dispositions, the measured commit, and the counter headline; no invented numbers vs measure-after.log."),
    seat("R66ShonenBox", "reviewer",
        "Check " + LANE + "/SHONEN.md box 1 state vs the SKILL.md it covers: box must stay `[~]`/honest (non-lane reviewer confirmation still routed, per r64/r65 routing); verify the SKILL changes this round did not silently self-claim `[x]`."),
    seat("R66LedgerConsistency", "connector",
        "Cross-file consistency: claims.md §Registered dispositions vs what actually landed (knowledge markers flipped, S043/S044 supersede lines, search-log notes, SKILL refresh, README C05); enumerate any registered item that did NOT land and any landed item not registered."),
    seat("R66EvidenceChain", "connector",
        "Trace the evidence chain: measure.py sha256 in claims.md == sha256sum reports/round-66/measure.py; base hash 8214e4dd exists in git log; measure-before.log labels match a fresh base-archive run's labels (cross-seat with R66CounterBase); report the chain end-to-end."),    # --- adversarial breadth ---
    seat("R66LabelSpoofAttack", "critic",
        "Attack: could the round-66 after-state be spoofed by a README/LOG-only edit with zero controls? Show the counter would catch it: run the counter on a /tmp corpus copy with README C05 flipped but markers absent — C05_REJECTED_MARKED must read `no` and HOLDS_OK_V4 `no`. This is the R65CriticCounter label-spoof surface; verify it now prints honest `no`."),
    seat("R66C6Asymmetry", "critic",
        "Adversarial asymmetry probe: are the new C6 mutants attributed only one-sidedly (as R65LabAttribution flagged for C5)? Check measure.py's C6 attribution rule: does a mutant killed by a DIFFERENT control's marker misattribute? Report the attribution clause verbatim + your verdict."),
    seat("R66UncoveredVsHeld", "critic",
        "Adversarial semantics: argue whether the honest disposition was `uncovered` vs keeping `frontier` (candidate retained → evidence exists, but falsified). Check the frozen order's text and README legend; report the ruling line."),
    seat("R66Q11DiffRecompute", "revenger",
        "Independent recompute of the decisive FAIL: produce readout.py full stdout to /tmp, diff against the entry's embedded output block; the ONLY differing line must be item 3's MANIFEST payload line; byte-quote both sides."),
    seat("R66DexSpecGap", "revenger",
        "Verify R65CriticEntryDeps' item-9 finding: the entry asserts dex-header semantics; confirm no SOURCES row covers dex headers (grep SOURCES.md for dex/DEX/dalvik); this is the named re-gate repair — confirm it stays unresolved but recorded."),    seat("R66S038Scope", "revenger",
        "Verify R65ReviewSourcesTier F: S038 (ResourceTypes.h) cited outside declared scope at entry:71/:126 — check the row's scope clause vs the entry's use; confirm recorded-not-repaired status for the rejected candidate."),
    seat("R66FrontierLegend", "simplifier",
        "Check corpus/README.md legend covers `uncovered` and its semantics differ from `frontier` correctly (candidate evidence exists but falsified); flag if the legend row needs a line and whether that absence is contract-loud."),
    seat("R66LedgerSweep", "simplifier",
        "Sweep for stale text: grep the lane for remaining `round-64/measure.py` as the CURRENT counter outside historical/pointer contexts in SKILL.md, PROVINCE.md, README.md — any line still instructing r64 counter use as current is a finding."),
    seat("R66MisrootSweep", "scout",
        "Repeat the misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` — any new untracked file naming revenger/round-66 outside the lane tree is a finding; the known /home/vgpnk/Projects/shokunin/unblob.log stays unclaimed (already adjudicated not-lane)."),    seat("R66PriorRejectIntegrity", "scout",
        "Byte-verify the two round-61 rejected candidates and the round-63/64 evidence files are unchanged vs their admitting commits; `git log --format='%h %s' -- corpus/knowledge/` to confirm only header repairs touched knowledge."),
    seat("R66FleetConfLanes", "scout",
        "Read /home/vgpnk/Projects/shokunin/shokunin.conf: confirm the revenger lane row's cwd/repo/axes unchanged; this lane's round touched only its own repo + fleet .ufo/reports + .ufo/waves paths."),
    seat("R66ClaimsDocSelf", "reviewer",
        "Self-consistency of reports/round-66/claims.md: pre-registered before measurement? (git show 16b9387 has claims+counter+before-log, no after); does §Frozen counter text match the committed measure.py labels; does §Registered list match landed diffs."),
    seat("R66TwoClaimSeparability", "critic",
        "Check causal separability of C1 vs C2: could C2's 4/4 land without the C05 flip? Could C1's flip land without C6? Demonstrate the counter lines that prove each independent of the other."),    seat("R66SkillNoSelfClaim", "sentinel",
        "Verify SKILL.md makes no unearned capability claim: §7 cites only existing paths; no `admitted` language on the rejected C05 candidate; the rejected entry is described as evidence, not held knowledge."),
    seat("R66LessonGateCompleteness", "critic",
        "Check lesson ## Gate completeness vs QUALITY.md admission procedure: every criterion has a decision, a named seat, and an L1 re-verification note; rejected entries recorded with reasons; no criterion silently n/a."),
    seat("R66AttributionLedger", "revenger",
        "Build the attribution table for all C-bands at the after state: C2 2/2, C3 2/2, C4 2/2, C5 2/2, C6 4/4 from measure-after.log; confirm each band's mutant count matches its control count in the two patched scripts (3 per script for C3-C6 = 6 mutants each? verify measure.py's own math)."),
    seat("R66FleetReportHash", "reviewer",
        "Cross-check the fleet report's cited lane hash equals `jj`/git tip actually pushed; confirm the helper's `landed <hash>` line was used (look for the hash in the report vs `git rev-parse HEAD`)."),    seat("R66LedgerScribe", "scribe",
        "Assemble the wave evidence ledger: every seat report path + its PASS/FAIL line + the lane tip hash + measure-after.log labels into " + LANE + "/" + REPORT_DIR + "/R66LedgerIndex.md; enumerate only, never judge; confirm all 64 reports non-empty."),
]

assert len(items) == 64, len(items)
spec = {
    "wave": "revenger-r66-v1",
    "milestone": "Round-66 landed work verified end-to-end: C05 disposition executed per frozen order, C6 4/4 attributed on committed tip, gate marks + fleet report + ledger hygiene audited; zero writes into corpus",
    "reportDir": REPORT_DIR,
    "axes": ["coverage", "calibration"],
    "context": CONTEXT,
    "items": items,
}
out = pathlib.Path(__file__).parent / "wave-spec.json"
out.write_text(json.dumps(spec, indent=1, ensure_ascii=False) + "\n")
print(f"wrote {out} with {len(items)} seats")
