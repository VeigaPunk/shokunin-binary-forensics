#!/usr/bin/env python3
"""Assemble the revenger round-65 v2 wave spec (64 seats) and write
.ufo/waves/round-65/wave-spec.json. Run from the lane root."""
import json
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
WAVES = LANE / ".ufo/waves/round-65"

GODSPEED = Path("/home/vgpnk/.agents/skills/godspeed/SKILL.md").read_text()

CONTEXT = f"""# Goal
Revenger round 65 attempt 1 (hyaku) — ONE v2 wave of exactly 64 seats, build-and-attack together. Lane repo: {LANE} — ABSOLUTE paths only in every read/write (your tools start at the fleet root /home/vgpnk/Projects/shokunin). Frozen contract (read first): {LANE}/reports/round-65/claims.md; frozen counter: {LANE}/reports/round-65/measure.py; red-before receipt: {LANE}/reports/round-65/measure-before.log (K_HELD 8/14, K_ROW C05 status=frontier, C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED 0/2, HOLDS_OK_V3=no, probe exit 0). Claims: C1 coverage K — exactly one independently gated admitted entry {LANE}/corpus/knowledge/round-65-apk-axml-byte-evidence.md over authored fixture corpus/fixtures/apk-r65/ covering README row C05 (K_HELD 8/14 → 9/14; README C05 flips frontier → held only on all-criteria Q01–Q13 admission by named fresh seats, else frontier → uncovered); C2 calibration — new criterion C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED 0/2 → 2/2 via one in-script forged-evidence control per script in corpus/verify_icon_languages.py and corpus/verify_multi_icon_states.py (frozen mutant: delete the receipt['evidence_id'] conjunct; attributed iff mutant exit non-zero and last output line ends 'forged receipt evidence accepted'). Claims are causally separable: C1 touches corpus knowledge/SOURCES/README only; C2 touches the two verifier scripts only.

# Build state (landed by L1 before this wave — your attack surface)
Fixture corpus/fixtures/apk-r65/ (generator.py, truth.json, readout.py, fixture.apk 947 bytes sha256 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e); candidate entry corpus/knowledge/round-65-apk-axml-byte-evidence.md (admission-status: candidate); SOURCES.md rows S038–S041 appended; lesson corpus/lessons/round-65.md drafted; verifier controls landed (C5 patch); README C05 NOT flipped. Frozen counter labels to reproduce: after-state must print K_HELD=9/14, K_ROW C05 status=held, C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2, STRICT_REJECT_WINDOW_SELFTEST=pass, HOLDS_OK_V3=yes, exit 0.

# Contract
Read {LANE}/reports/round-65/claims.md fully before scoring anything; the frozen kill rule, predicate and admission order there override any summary in this prompt. Counting command: git archive <commit> corpus into a scratch tree, then from /: TMPDIR=<lane-owned scratch> python3 -B {LANE}/reports/round-65/measure.py <tree>. Measurements belong to committed trees only.

# Bounds (hard)
Write ONLY your own report file at the absolute path named in your seat brief (under {LANE}/.ufo/waves/round-65/). Everything else — corpus/, reports/, LOG.md, SCORECARD.md, SHONEN.md, the fleet repo, sibling lane repos, lane jj state, the lane Git index — is read-only for you; do NOT run git/jj mutations, do NOT edit any file another seat may own, do NOT write anywhere under /home/vgpnk/Projects/shokunin outside your own report path (no fleet-root files). Read-only seats return findings without production edits. Every `Report:` trailer path is relative to {LANE} — write it at {LANE}/<that path>. Absolute paths everywhere.

# Tooling authorization (operator, 2026-10-19)
You and every seat may install or upgrade tools that help the task — read /home/vgpnk/.omp/agent/RULES.md first (official channels, update-safety gate, record tool/version/channel/reason in your report). Pacman guard (orchestrator ruling 2026-10-20): all pacman transactions are PAUSED host-wide — install via uv tool/npx/an official binary in ~/.local/bin, or file an L0 question; never -Sy/-Syu/-U/-R, never restart a host service.

# Seat rules
Time-box: return within 15 minutes with your best findings + evidence; partial results are acceptable. You are an independent leaf: never block on or wait for another seat; never spawn subagents except one read-only labrat probe per executor card if your brief names one; if a needed artifact is absent, record the dependency as a finding and return. Put your verdict on the first line of your report (PASS / FAIL / NOT-FALSIFIED / ADMIT / REJECT / CLEAN + one-line reason), then evidence: commands with actual output, file:line pointers, sha256 where relevant. Ground every claim in a resolvable pointer; a claim without one is not evidence."""

BUILD = ["coverage", "calibration"]
ADJ = ["adjacency"]


def item(name, role, axes, brief):
    axes = list(dict.fromkeys(axes))
    prompt = (
        GODSPEED
        + "\n\nTime-box: return within 15 minutes with your best findings+evidence; partial results are acceptable.\n"
        + "You are an independent leaf: never block on or wait for another seat; if a needed artifact is absent, record the dependency as a finding and return.\n\n"
        + "# Target\nSeat brief: "
        + brief
        + f"\n\nReport: .ufo/waves/round-65/{name}.md — write your verdict + evidence at the ABSOLUTE path {LANE}/.ufo/waves/round-65/{name}.md (the trailer path is relative to {LANE})."
    )
    return {"name": name, "role": role, "axes": axes, "prompt": prompt}


E = LANE / "corpus/knowledge/round-65-apk-axml-byte-evidence.md"
FX = LANE / "corpus/fixtures/apk-r65"
SRC = LANE / "corpus/SOURCES.md"

items = [
    # --- C1 build/verification seats (9) ---
    item("R65EntryCommands", "executor", BUILD,
         f"Re-execute every command block in {E} (all `python3 -B corpus/fixtures/apk-r65/readout.py --fact ...` lines plus the bare recheck command) from {LANE} and compare each output line for exact equality with the entry's embedded line. Report the count executed, count matching, and any mismatch verbatim. Also recompute the 15-line stdout sha256 and compare with 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247."),
    item("R65BlindDerive", "executor", BUILD,
         f"WITHOUT reading {FX}/readout.py or the entry's embedded outputs, derive from the raw bytes of {FX}/fixture.apk alone: (a) the archive size and sha256; (b) the three member names with local-header offsets, payload offsets and sizes, by walking the central directory and local headers at APPNOTE 6.3.10 field widths; (c) the AXML chunk table (offsets, types, sizes, headerSizes) by walking chunks from offset 8. Then compare your derivation against {FX}/truth.json and report agreement/divergence per value. This is the Q03 blind-independence seat."),
    item("R65FixtureRegen", "executor", BUILD,
         f"Copy {FX} into a scratch directory under /tmp, run `python3 -B generator.py` there, and byte-compare the regenerated fixture.apk and truth.json against the committed originals (truth.json may differ only in the embedded python_version field when the interpreter differs — record both versions). Report cmp results and sha256s. Never run the generator in place."),
    item("R65DexReprobe", "executor", BUILD,
         f"Independently re-derive the classes.dex declared header facts from {FX}/fixture.apk bytes: magic, Adler-32 over bytes 12.., SHA-1 over bytes 32.., file_size, header_size, endian_tag. Use only hashlib/zlib/struct. Compare with fact dex_declared_header in the readout output and the entry item 9. Report any divergence."),
    item("R65AxmlReprobe", "executor", BUILD,
         f"Independently re-parse the AndroidManifest.xml AXML bytes of {FX}/fixture.apk (extract the member by your own byte walk) and confirm: 9 strings in declared order, flags 0x100, resource-map non-zero entries 0x0101021b/0x0101021c at indices 5/6, start-element attributeStart 20 attributeSize 20 attributeCount 3, and the three attribute (name, typed value) pairs. Use only struct. Compare against truth.json axml_declared and the entry items 6-8."),
    item("R65EntryQmapDraft", "scribe", BUILD,
         f"Read {E} end to end and audit ONLY internal consistency: every value in the prose of items 1-10 against the JSON output printed beneath it (sizes, offsets, hex ids, string counts), the §Comparison-with-oracle claims against {FX}/truth.json, and the §Limitations against what the Observation items actually claim. Report each inconsistency verbatim with file:line."),
    item("R65ReadmeLegend", "scout", BUILD,
         f"Read {LANE}/corpus/README.md (coverage legend + C05 row + ## Frontier), {LANE}/corpus/knowledge/round-65-apk-axml-byte-evidence.md header, and {LANE}/reports/round-65/claims.md C1. Report the exact edit the README C05 row and Frontier section would need on admission (frontier → held naming only the new entry) and whether any other README text would go stale by the legend's own rules (cf. M36). Do not edit anything."),
    item("R65LessonDraft", "scribe", BUILD,
         f"Read {LANE}/corpus/lessons/round-65.md and check it against the round lesson rules (## Gate records URL/access date/≤25-word located quote per new SOURCES row; ## Mistakes rows carry class/evidence/captured-by/fix; fixes shown able to fail). Verify each quoted snapshot hash against .ufo/waves/round-65/source-snapshots/ and each ≤25-word quote against the snapshot bytes. Report violations verbatim."),
    item("R65SnapshotManifest", "executor", BUILD,
         f"Recompute sha256 of every file under {LANE}/.ufo/waves/round-65/source-snapshots/ and compare with the digests recorded in {SRC} rows S038/S039/S040 and lesson ## Gate. Then re-fetch each source (AOSP URL with ?format=TEXT base64; npm pack rea-agents@6.5.0 member; docs.python.org zipfile page) and byte-compare with the snapshots, recording HTTP status and any drift."),
    # --- C1 attack seats (13) ---
    item("R65ReviewEntryQ01", "reviewer", BUILD,
         f"Criterion Q01 on {E}: each load-bearing claim rests on a SOURCES row tier-A for its scope opened this round (S038 spec for AXML layout; S041 own-work for fixture bytes; S032/S034 registry tier-A for ZIP field offsets; S039 route-scope only). Check nothing load-bearing rests on tier C or on a row outside its scope. Verdict PASS/FAIL with per-claim support mapping."),
    item("R65ReviewEntryQ02", "reviewer", BUILD,
         f"Criterion Q02 on {E}: header carries source: rows with URLs/paths, exact anchors (struct names + line numbers) and snapshot digests; verified-at; recheck: with command AND stdout sha256; coverage-map row C05 named. Verify each anchor exists in the S038 snapshot bytes. Verdict PASS/FAIL per sub-item."),
    item("R65ReviewEntryQ03", "reviewer", BUILD,
         f"Criterion Q03 on {E}: expected values derived independently (authored oracle + spec-derived widths fixed outside the record under test). Confirm no expected value is copied from a saved producer record and no saved path is both identity and locator. Cross-check R65BlindDerive's report if present. Verdict PASS/FAIL."),
    item("R65ReviewEntryQ06", "reviewer", BUILD,
         f"Criterion Q06 on {E} + {FX}: fixture premises byte-verified against the built fixture; generator run only in scratch; regen byte-compare performed (see R65FixtureRegen). Verify the truth.json member measurements equal a fresh byte walk of fixture.apk. Verdict PASS/FAIL."),
    item("R65ReviewEntryQ09", "reviewer", BUILD,
         f"Criterion Q09 on {E}: digests claimed only for exact bytes hashed; no origin/completeness/authenticity claim; dex checksum/signature framed as inert self-consistency, not validity. Check every digest sentence. Verdict PASS/FAIL per instance."),
    item("R65ReviewEntryQ10", "reviewer", BUILD + ADJ,
         f"Criteria Q10 + cross-lane on {E}: finding scoped to one fixture/operation/version; §Limitations and §Cross-lane scope note complete; ADJ-06 reported-not-absorbed; no provider readiness claim (Q05 fence). Check the scope sentences against claims.md C1's declared scope. Verdict PASS/FAIL."),
    item("R65ReviewEntryQ11", "reviewer", BUILD,
         f"Criterion Q11 on {E}: every count/offset/identifier/digest carries its deriving command + output inside the entry; constants derived not assumed (item 5 width derivation); no recorded value presented as re-derived. Re-derive at least 5 values yourself by command. Verdict PASS/FAIL with the list checked."),
    item("R65CriticEntryDeps", "critic", BUILD,
         f"Attack {E} for dependency errors: does any Observation item rely on another's value without saying so; does the §Comparison-with-oracle claim agreement on fields truth.json does not actually contain; do the item cross-references (item 5 ↔ item 8 sizes) hold. Falsify aggressively; name every broken link."),
    item("R65CriticCounts", "critic", BUILD,
         f"Attack every number in {E}: recompute each of the 15 readout facts from fixture.apk bytes yourself (independent code, not the lane's readout.py) and compare. Any number in the prose (947, 925, 737, 188, 416, 196, 44, 24, 96, 0x0101021b, 0x3d120c30, 112, 69...) that fails re-derivation is a FAIL — list all."),
    item("R65MutEntry", "mutation-tester", BUILD,
         f"Mutation-test the entry/fixture pair: (a) flip ONE byte inside fixture.apk's AXML member (e.g. a string-pool byte) in a scratch copy and show the readout changes or fails on that copy; (b) edit ONE number in a copy of the entry's embedded JSON and show it no longer matches the readout stdout. Report both mutants' observed output deltas. If a mutation is NOT detected, that is a finding."),
    item("R65MutProbe", "mutation-tester", BUILD,
         f"Mutation-test {LANE}/corpus/fixtures/apk-r65/readout.py's self-consistency checks: in a scratch copy, weaken each walk-end assertion (off == xml_size; cursor == eocd; crc match; checksum match) one at a time and confirm a corresponding forged fixture would then pass undetected. Report which checks are load-bearing and which forgeries still escape."),
    item("R65SentinelScope", "sentinel", BUILD,
         f"Security/scope review of {E}, {FX}/generator.py and {FX}/readout.py: no credential material, no network writes, no execution of fixture content, generator writes only beside itself (HERE), no path traversal, lesson/snapshot files carry no secrets. Also confirm the fixture is inert (no code member is executed by any round-65 command). Verdict CLEAN/FINDINGS."),
    item("R65SimplifierDrift", "simplifier", BUILD,
         f"Minimality review of {E}: is any Observation item redundant given the others, any claim in §Inference not forced by the bytes, any §Limitations entry the legend already covers? Propose the smallest deletion set that loses no checkable content; if none, say so with the reason."),
    # --- C2 attack seats (8) ---
    item("R65MutC5", "mutation-tester", ["calibration"],
         f"Reproduce the frozen C5 kill rule on the landed scripts: in scratch tree copies, apply the frozen mutant (delete the receipt['evidence_id'] conjunct per the regex in {LANE}/reports/round-65/measure.py mutate_c5) to corpus/verify_icon_languages.py and corpus/verify_multi_icon_states.py and run --self-test. A kill is attributed iff exit is non-zero AND the last output line ends with 'forged receipt evidence accepted'. Report exit codes and last lines verbatim, plus red-before evidence the same mutants exit 0 at base commit 3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f."),
    item("R65ReviewC5Lang", "reviewer", ["calibration"],
         f"Patch-shape review of corpus/verify_icon_languages.py: diff the landed file against base commit 3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f (git diff, read-only). Confirm: insertions only, exactly one new control, placed after the forged-stdout control, receipt_ok untouched, the transplanted ID equals the round-42 saved evidence_id from corpus/live/runs/round-42/, message ends 'forged receipt evidence accepted'. Verdict PASS/FAIL per check."),
    item("R65ReviewC5Multi", "reviewer", ["calibration"],
         f"Same patch-shape review as R65ReviewC5Lang for corpus/verify_multi_icon_states.py against base 3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f, with the transplanted ID equal to corpus/live/runs/round-47/'s saved evidence_id. Verdict PASS/FAIL per check."),
    item("R65MutIcon", "mutation-tester", ["calibration"],
         f"Regression sweep: with the C5 patch landed, re-run the C2/C3/C4 frozen mutants per {LANE}/reports/round-65/measure.py on a scratch copy and confirm the attributed counts stay C2 2/2, C3 2/2, C4 2/2 and controls all pass. Any regression is a FAIL — this is the no-harm check for C2."),
    item("R65ReviewCounter", "reviewer", ["calibration"],
         f"Review {LANE}/reports/round-65/measure.py against the frozen claims: every round-64 label/formula unchanged; new labels C5_* and STRICT_REJECT_WINDOW_SELFTEST additive; HOLDS_OK_V3 = V2 ∧ C5 2/2 ∧ selftest; the mutate_c5 regex has exactly one match per script; the rejected-marker scan reads whole files (no [:2000]). Then run the counter on a scratch archive of the CURRENT committed tree and report every label line."),
    item("R65CriticCounter", "critic", ["calibration"],
         f"Attack the round-65 counter for spoof surfaces (cf. round-64 R64CriticCounter): can a tree with no real C1 work print K_HELD=9/14 (decoy rows, README flip without admission, fake knowledge file)? Can a tree print C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2 without the landed controls (C5_CONTROL_PRESENT says no — verify)? Demonstrate each attack you find on a scratch tree; attacks that fail, name the guard that stopped them."),
    item("R65CriticClaims", "critic", BUILD + ["calibration"],
         f"Attack the claims themselves as declared in {LANE}/reports/round-65/claims.md: is the C1 after-state one command re-derivable; is the C5 kill rule frozen before any after-measurement (check commit times: claims.md at 5a2e7a0 precedes any after-run); is the do-nothing control genuinely red; could a do-nothing control meet either target? Report each attack's outcome."),
    item("R65RevengerLedger", "revenger", ["calibration"],
         f"Reverse the round's own ledger discipline: the C5 control transplants a REAL FOREIGN evidence id (prong c). Attempt prongs (a) same-run id, (b) injectively fresh id, (d) cross-record stdout binding on a scratch receipt copy using the landed verifiers' receipt_ok — which are still uncaught, and does the round-63/64 routed ledger check (6-prong shape) name owners for them? Report the residual surface honestly; do NOT edit any verifier."),
    # --- Frontier / census / spotcheck seats (8) ---
    item("R65ScoutCensus", "scout", ["coverage"],
         f"Run the maintained census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger` from the fleet root and the seven frozen manual census commands from {LANE} (CORPUS.md §Census). Report every exit code and output. Expected: rows 41, malformed 0, no duplicates, no enum violations, no missing used-by paths, maintained census exit 0."),
    item("R65ReviewSources", "reviewer", ["coverage"],
         f"Review {SRC} rows S038-S041 against contract v1: 11 columns, no '|' inside cells, ids next-unused and never reused, tier scoped, anchor exact (not bare homepage), teaches grounded, queued/mined/rejected statuses legal, opened=2026-10-24. Verify S038's anchor line numbers against the snapshot bytes (struct names present at cited lines). Verdict PASS/FAIL per row."),
    item("R65ScoutFrontier", "scout", ["coverage"],
         f"Read {LANE}/corpus/README.md ## Frontier and Known gaps plus PROVINCE.md. Check the C05 fixture/entry move the frontier claim correctly: is anything left asserting C05 has 'no knowledge and no saved record'? Is the C07 firmware prose (now held) still accurate? Report required Frontier edits for the admission commit; do not edit."),
    item("R65ConnectorOverlap", "connector", ADJ,
         f"Sibling-overlap scan: which other lanes (kaidoku, tsukuroi, chousa) touch Android/AXML/APK ground this round? Read the fleet roster reports under /home/vgpnk/Projects/shokunin/.ufo/reports/round-65/ and .ufo/reports/round-64/ for overlaps with revenger C05/C10 ground. Anything contested goes reported-not-absorbed in the entry's cross-lane note; name what ADJ-06 (fleet .ufo/l0-questions.md:42) still binds."),
    item("R65CriticHarms", "critic", BUILD + ["calibration"],
         f"Harms sweep over the round diff (git diff base 3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f, read-only): any changed byte under corpus/live or pre-existing corpus/fixtures paths (void condition); any touched README row other than the C05 candidate line; any weakened Q01-Q13 text in QUALITY.md; any edit of retained rejected candidates; SCORECARD append-only. Report each violation or 'none' with the command output."),
    item("R65Preservation", "executor", ["coverage"],
         f"Byte-preservation check: `git diff --numstat 3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f -- corpus/live corpus/fixtures/firmware-r63 corpus/fixtures/archive-r2` must be empty, and every pre-existing verify_*.py self-test must still pass with its original exit code. Report the diff output and each self-test exit."),
    item("R65ScribeGate", "scribe", BUILD,
         f"Draft the ## Gate admission-decision addendum for corpus/lessons/round-65.md from the wave's verdict files present under {LANE}/.ufo/waves/round-65/ when you run: for each of C1 (Q01-Q13 rows) and C2 (patch shape + mutant attribution), record per-seat verdicts with file pointers, then the L1-shaped decision text (admit → README frontier → held naming only the new entry; falsify → frontier → uncovered). If verdict files are missing, record the dependency and return a skeleton. Do not edit the lesson itself."),
    item("R65SpotcheckDiscern", "reviewer", ["calibration"],
         f"Discernment spot-check: form an independent ADMIT/REJECT judgment on (1) the round-65 entry as a candidate and (2) the retained rejected candidates corpus/knowledge/commonjs-destructured-require-edges.md and corpus/knowledge/evm-saved-interface-candidates.md (should stay rejected). Name your agree/disagree with the lane's own gate so far and your reasons — this is the outside-discernment check LEARNING.md requires."),
    # --- Remaining build/analysis seats to 64 ---
    item("R65LabDoNothing", "mutation-tester", ["calibration"],
         f"Do-nothing control proof: on a scratch archive of base commit 3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f corpus (git archive), run the round-65 counter and confirm it meets NO target (K 8/14, C5 0/2, HOLDS_OK_V3=no). Then confirm a tree with ONLY the C5 patch (no C1 files) prints C5 2/2 but K_HELD stays 8/14, and a tree with ONLY C1 admission prints K 9/14 but C5 0/2 — the separability receipt."),
    item("R65LabAttribution", "mutation-tester", ["calibration"],
         f"Probe the attribution rule's exactness: construct a scratch variant of verify_icon_languages.py whose C5 control raises with a message NOT ending 'forged receipt evidence accepted' (e.g. 'evidence forged') and show the counter's endswith check scores it unattributed while the raw kill still fires. Report the two runs' counter lines; this probes rule sensitivity, do not edit the lane file."),
    item("R65ExecVerifiers", "executor", ["calibration"],
         f"Run all ten corpus/verify_*.py --self-test from {LANE} and record every exit code and last line, plus the SCORECARD census command C. Confirm HOLD_CALIBRATION 4/4 and HOLD_REPLAY 10/10 on the current tree, and identify precisely which scripts the C5 patch touches (must be exactly two)."),
    item("R65ReviewSeparability", "reviewer", BUILD + ["calibration"],
         f"Claim-separability review: construct the two single-claim trees from the current tree (strip C1 files / strip C2 patch) in scratch copies and run the counter on each; confirm each moves only its own labels. Also review the claims.md separability paragraph against what the counter actually measures. Verdict PASS/FAIL."),
    item("R65ScoutHost", "scout", ["coverage"],
         f"Re-verify the round's environment claims used in the entry/lesson: python3 --version, that no network was needed by the readout (it opens only fixture.apk beside it), and that jadx 1.5.6 presence is NOT cited anywhere as capability (Q05 fence). Report any citation of presence-as-capability as a finding."),
    item("R65ScoutMisroot", "scout", ["coverage"],
         f"Misroot sweep: run `git -C /home/vgpnk/Projects/shokunin status --porcelain` (fleet root) and list every untracked file plausibly written by a revenger round-65 seat outside the lane repo; for each, name the correct lane-relative path it should live at. Seats writing to the fleet root is the failure this seat detects; report even absence."),
    item("R65ScoutReadme", "scout", ["coverage"],
         f"README-index audit: every knowledge entry named in corpus/README.md coverage map exists as a file with matching admission status (candidate vs admitted); the C05 row's planned 'held' text will name round-65-apk-axml-byte-evidence.md — verify that filename matches the actual file. Report mismatches."),
    item("R65CriticEntryScope", "critic", BUILD,
         f"Attack the entry's scope fences: find any sentence in {E} that a reader could generalize beyond one fixture (parser behavior, other APKs, AXML producers, provider output). Quote each risky sentence with file:line and state whether §Limitations rescues it; if one escapes both, that is a FAIL."),
    item("R65CriticFixture", "critic", BUILD,
         f"Attack the fixture's fitness as known truth: could any member of fixture.apk be mistaken for a real artifact (real package name, real-looking dex)? Is the inertness legible from the bytes themselves? Is truth.json's axml_declared actually derivable from fixture.apk (not just from generator intent)? Report weaknesses with the exact byte evidence."),
    item("R65ScoutRecon", "scout", BUILD,
         f"Round-state recon: read {LANE}/LOG.md tail, SCORECARD.md round-64 section, reports/round-65/claims.md, corpus/lessons/round-64.md routed rows. Produce a one-page state map: what rounds 62-64 landed, what round 65 claims, which routed debts round 65 addresses (STRICT window, evidence-id prong c) and which it carries. This orients the other seats; cite file:line throughout."),
    item("R65ExecAfterMeasure", "executor", BUILD + ["calibration"],
         f"After-measurement dry run: on a scratch copy of the CURRENT working tree corpus plus the README C05 flip applied in the copy ONLY (held naming round-65-apk-axml-byte-evidence.md), run the round-65 counter and confirm it prints K_HELD=9/14, K_HELD_BACKED=9/14, K_HELD_BACKED_STRICT=9/14, K_ROW C05 status=held, README_TOKEN_LEGEND_MISMATCH=0, all C2/C3/C4/C5 lines green, HOLDS_OK_V3=yes, exit 0. This predicts the admission commit's measurement; do not edit the real README."),
    item("R65Distill", "scribe", BUILD,
         f"Deduplicate the wave: read every R65*.md report present under {LANE}/.ufo/waves/round-65/ when you run; group duplicate findings across seats, name the canonical pointer per finding, and list any seat whose verdict contradicts another's on the same evidence (adjudication queue for L1). If few reports exist yet, record the dependency and return."),
    item("R65ReviewSkillCites", "reviewer", ["coverage"],
         f"Citation sweep of {LANE}/SKILL.md against round-65 additions: does SKILL.md need a round-65 pointer (APK fixture family, C5 control shape) to stay current per its own §7 existence-checked table? Report the minimal edit set; do not edit SKILL.md (a later round owns the gate)."),
]

# pad with distinct attack seats to exactly 64
extra = [
    ("R65CriticCounts2", "critic", "Second independent count attack: recompute the census histograms (rows, tiers, statuses) of corpus/SOURCES.md by your own parser and compare with the maintained census output; any drift is a FAIL."),
    ("R65ReviewEntryQ04", "reviewer", "Criterion Q04 on the entry: no tool claim; the readout is labeled manual stdlib byte analysis; zipfile module named only as cross-check (S040 queued row), credited with nothing. Verify by reading the entry's Q-map and §Observation tool sentences."),
    ("R65ReviewEntryQ05", "reviewer", "Criterion Q05 on the entry: no readiness/capability claim anywhere; §Cross-lane scope note fences inspect_android_package to S039 documentation scope. Check also the lesson and README planned text for stray readiness claims."),
    ("R65ReviewEntryQ07", "reviewer", "Criterion Q07 on the entry: any predicted parser behavior must be pre-registered with spec-derived ground truth. The entry makes no provider/parser predictions — verify that absence is real, not implicit."),
    ("R65ReviewEntryQ12", "reviewer", "Criterion Q12: n/a for the entry (no rejected row written by it) — confirm the Q-map says so and that no S038-S041 row is a rejected row lacking reason+flip."),
    ("R65ReviewEntryQ13", "reviewer", "Criterion Q13: no verifier/recheck command credited for clauses beyond its shown detection; the entry cites only its own readout. Confirm no verify_*.py script is credited anywhere in the entry."),
    ("R65MutC5Regression", "mutation-tester", "Second C5 mutant path: transplant the OTHER script's real id (round-47 id into the multi script's control as authored is correct — verify) AND a made-up id ev_deadbeef...; confirm receipt_ok rejects both (foreign real and fabricated). Report both runs."),
    ("R65ScoutSources", "scout", "Re-open S038's chunk-type enum and Res_value Type enum in the snapshot; confirm the entry's 0x03/0x10 data-type names and chunk-type names match the enum member names at the cited lines (typo-level check, cf. S038's own 'occurrance' spelling preserved verbatim)."),
    ("R65CriticLesson", "critic", "Attack corpus/lessons/round-65.md: are the Gate quotes each ≤25 words and located; does the M38 fix row carry evidence + captured-by + a fix shown able to fail (m38-red-before.log exists and shows non-zero exit); is the lesson's claim about wave preparation consistent with .ufo/waves/round-65/wave-spec.json existing and validated?"),
    ("R65ExecCensusProbe", "executor", "Run the SCORECARD census C command (ten verifiers) from the lane root on the current tree and record all exits; confirm the probe's own exit is 0 even though constituent verifiers may fail, and that the four calibration scripts all exit 0."),
    ("R65ReviewSourcesTier", "reviewer", "Tier-inflation audit of S038-S041: is any row tier A outside its declared scope (S039 route-scope sentences tier A for route scope only — check the entry never cites it for format facts; S040 queued honestly non-load-bearing; S041 own-work scope bounded to the fixture bytes)? Report any inflation with the citing sentence."),
    ("R65ScoutC05Ground", "scout", "Coverage-ground check: read the C05 row's full history (git log -p -- corpus/README.md for the C05 line, read-only) and confirm the row has been frontier continuously since the map's a7acc20 freeze, so this entry is the first knowledge on that ground (no prior partial text to contradict)."),
    ("R65CriticAdmissionOrder", "critic", "Attack the admission order itself: read reports/round-65/claims.md §Admission order and check the L1 followed it — candidates landed with NO README flip, fresh-seat decisions are what flips the row, falsification flips to uncovered. Any deviation visible in the tree (e.g. README already flipped) is a FAIL of the frozen order."),
]
for name, role, brief in extra:
    items.append(item(name, role, BUILD if "census" not in name.lower() else ["coverage"], brief))

spec = {
    "wave": "revenger-r65-v2",
    "milestone": "C1 C05 candidate + C2 C5 patches landed as build state; README not flipped; wave provides fresh-seat Q decisions, mutant attribution and separability receipts",
    "reportDir": ".ufo/waves/round-65",
    "axes": ["coverage", "calibration"],
    "context": CONTEXT,
    "items": items[:64],
}
out = WAVES / "wave-spec.json"
out.write_text(json.dumps(spec, indent=1) + "\n")
roles = {}
for i in spec["items"]:
    roles[i["role"]] = roles.get(i["role"], 0) + 1
attack = sum(roles.get(r, 0) for r in ("reviewer", "critic", "mutation-tester", "sentinel", "labrat"))
print("seats:", len(spec["items"]), "roles:", roles, "attack:", attack, f"({100*attack/len(spec['items']):.0f}%)")
print("written:", out)
