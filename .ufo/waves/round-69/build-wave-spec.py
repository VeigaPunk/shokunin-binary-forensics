#!/usr/bin/env python3
"""Round-69 wave-spec generator (revenger L1, hyaku run 6).

Renders `.ufo/waves/round-69/wave-spec.json`: ONE v2 wave of exactly 64 seats
under scripts/hyaku/ufo-wave-policy-v2.json (band 64-128, maxLanes 256),
build items and attack items together, every item a distinct concrete work item
serving the round's two declared claims (C1 coverage C05 v4 re-gate, C2
calibration Q15 criterion) plus the frontier step (quarantine slice hand-check,
considerthese proposal 2) and the round-68 routed repairs D1-D5.

The godspeed directive bytes are lifted byte-exact from the committed round-68
wave spec (`.ufo/waves/round-68/wave-spec.json`, item 0) so the host binding is
reproduced verbatim and never paraphrased.

Run from the lane root:  python3 -B .ufo/waves/round-69/build-wave-spec.py
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
WAVE_DIR = ROOT / ".ufo/waves/round-69"
R68_SPEC = ROOT / ".ufo/waves/round-68/wave-spec.json"

LANE = "/home/vgpnk/Projects/shokunin/revenger-shokunin"
ENTRY = f"{LANE}/corpus/knowledge/round-69-apk-axml-byte-evidence.md"
GATE = f"{LANE}/corpus/check_embedded_outputs.py"
DERIVE = f"{LANE}/corpus/derive_axml_anchors.py"
Q15 = f"{LANE}/corpus/q15_tree_id_check.py"
COUNTER = f"{LANE}/reports/round-69/measure.py"
CLAIMS = f"{LANE}/reports/round-69/claims.md"
BEFORE = f"{LANE}/reports/round-69/measure-before.log"
D1FIX = f"{LANE}/reports/round-69/d1-false-sentence.md"
SNAPSHOT = f"{LANE}/.ufo/waves/round-65/source-snapshots/ResourceTypes.h"
SNAP_COPY = f"{LANE}/corpus/snapshots/ResourceTypes.h"
README = f"{LANE}/corpus/README.md"
SOURCES = f"{LANE}/corpus/SOURCES.md"
SKILL = f"{LANE}/SKILL.md"
QUALITY = f"{LANE}/corpus/QUALITY.md"
FIXTURE = f"{LANE}/corpus/fixtures/apk-r65"
REGISTER = "/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md"
REPORT_DIR = ".ufo/waves/round-69"


def godspeed_prefix():
    spec = json.loads(R68_SPEC.read_text(encoding="utf-8"))
    prompt = spec["items"][0]["prompt"]
    marker = "Act directly via tool calls."
    idx = prompt.index(marker) + len(marker)
    return prompt[:idx]


GODSPEED = godspeed_prefix()

CONTEXT = f"""# Goal
Revenger round 69 (hyaku run 6) — ONE v2 wave of exactly 64 seats, build and attack together. Lane repo: {LANE} — ABSOLUTE paths only in every read and write (your tools start at the fleet root /home/vgpnk/Projects/shokunin).

# Frozen contract (read first — it overrides any summary here)
{CLAIMS} — the two declared claims (C1 coverage: C05 v4 re-gate; C2 calibration: Q15 tree-identity criterion), their frozen predicates, kill rules, do-nothing controls, void conditions and admission order.
{COUNTER} — the frozen counter (sha256 bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377).
{BEFORE} — the committed red-before receipt.

# Report paths (IMPORTANT)
Every `Report:` trailer in your prompt is RELATIVE to {LANE} — write your report at {LANE}/<that path> (e.g. a `.ufo/waves/round-69/…` trailer means {LANE}/.ufo/waves/round-69/…). Never write to the fleet root.

# Write scope
- You may write ONLY your own report file under {LANE}/.ufo/waves/round-69/ and scratch files under /tmp/revenger-r69-* (delete your /tmp scratch before returning).
- NEVER write, edit, commit or push inside: the fleet repo /home/vgpnk/Projects/shokunin, any sibling lane repo, {LANE}'s own corpus/ (read-only for seats), or /home/vgpnk/Projects/shokuknow (READ-ONLY campaign tree — quarantine work fetches and reads only).
- NEVER run a mutating git or jj command anywhere (no add/commit/stash/checkout/reset/pull/push/jj new/describe/squash/rebase/bookmark). Read-only git/grep/read is fine. A git-writing check runs on a sandbox clone in your seat scratch, never in the lane.
- A policy did NOT run on the host: all pacman transactions are PAUSED host-wide; do not install or update any package. If you need a tool, use an existing binary or a Python stdlib approach.

# Tooling authorization (operator, 2026-10-19)
You and every seat may install or upgrade tools that help the task — read /home/vgpnk/.omp/agent/RULES.md first (official channels, update-safety gate, record tool/version/channel/reason in the report). pacman guard: all pacman transactions are PAUSED host-wide — install via `uv tool`/`npx`/an official binary in `~/.local/bin`, or file an L0 question; never `-Sy`/`-Syu`/`-U`/`-R`/downgrade/restart a host service.

# Seat discipline
You are an independent leaf: never block on or wait for another seat; never spawn subagents; never message agent://all; if a needed artifact is absent, record the dependency as a finding and return. Time-box: return within 12 minutes with your best findings + evidence; partial results are acceptable. Put your verdict on the FIRST line of your report (PASS / FAIL / NOT-FALSIFIED / ADMIT / REJECT / CLEAN / PRESENT / HOLDS / FALSIFIED / CONCUR / DIVERGE + one-line reason), then evidence: commands with their actual output, file:line pointers, sha256 where relevant. Ground every claim in a resolvable pointer; a claim without one is not evidence."""


def seat(name, role, axes, task):
    return {
        "name": name,
        "role": role,
        "axes": axes,
        "prompt": GODSPEED + "\n\n" + task,
    }


items = []

# ---------------------------------------------------------------- group A: Q01-Q15
Q_BASIS = f"""You are a fresh admission reviewer for {ENTRY} (the round-69 C05 v4 candidate, `admission-status: candidate`). Read {CLAIMS} §C1 first, then {QUALITY}, then the entry.

Your criterion: {{qid}} — {{qtext}}

Do: read the entry's own bytes (absolute path above). Decide PASS / FAIL / n/a **for this criterion only**, on these bytes. For a FAIL, name the exact line(s) and the exact value that is wrong, and say what the correct value would be. For PASS, say which command or which line proves it and quote the observed output. Re-derive every value you rely on: run the entry's own commands yourself and compare their actual stdout with the entry's embedded lines; a value that the command does not print is a FAIL for Q11 and a FAIL for the criterion that carries it. Never accept the entry's Q-map row as evidence for your own criterion. Do not edit any file. Report the criterion id, the verdict, the evidence commands and their outputs, then the entry lines at issue."""

Q_ITEMS = [
    ("Q01", "each load-bearing claim rests on a `corpus/SOURCES.md` row that is tier A for that claim's scope and was opened in the round that wrote it (a tier-C row is never sole support); verify S032/S034/S041/S043/S045/S047 rows exist with stated tiers and the opened dates match this round/entry"),
    ("Q02", "the entry opens with `source:` (its S### rows, URLs or paths, exact anchors), `verified-at:` (date or commit) and `recheck:` (the command or citation that re-verifies it), and names the coverage-map row it fills (C05); every header source row must resolve"),
    ("Q03", "expected values are derived independently — from bytes, a specification, or a pin fixed outside the record under test; nothing is copied from a saved producer record or from the oracle it claims to match"),
    ("Q04", "a tool claim names the tool, version and function exercised and scores the tool's own explicit output; manual analysis is labeled manual — here the readout is manual and the derivation script's credit must be bounded to the exact numbers its stdout prints (the round-68 v3 FAIL was a universal 'every line' credit)"),
    ("Q05", "a readiness or capability claim carries a probe against the real surface (command, date, observed exit/output); presence/configuration is not capability — the derivation script may be credited only as an own-work instrument whose output is demonstrated, never as a producer or parser capability"),
    ("Q06", "fixture premises are byte-verified against the built fixture after every edit and before any producer call; failed inputs are retained — confirm the fixture bytes/readout are the round-65 claim-tree bytes and the generator is pinned in the header"),
    ("Q07", "a predicted parser behavior (accept, refuse, cause) is a pre-registered hypothesis with spec-derived ground truth, recorded either way; a cause is stated only after independent reproduction — the namespace-resolution sentence must read as an observation of this readout on this fixture, not a prediction about other parsers"),
    ("Q08", "superseded by Q11 — verify the entry applies Q11, not Q08 (applying Q08 instead is itself a Q11 failure)"),
    ("Q09", "a digest or receipt is claimed only for the exact bytes it hashed; it does not establish producer origin, completeness or authenticity; saved records stay byte-preserved"),
    ("Q10", "a finding is scoped to the observed family, operation, version and input; cross-lane contested scope is reported, not absorbed — check the Limitations and Cross-lane scope note"),
    ("Q11", "every count, identifier, offset and digest carries, inside the entry, the command that derives it from the primary record and that command's output; constants are derived, not assumed; a recorded value is not presented as re-derived — re-run the entry's commands and diff every embedded output line verbatim"),
    ("Q12", "a rejected source row states a reject reason grounded in a located quote and a `flip` naming a source change or a scope the reason does not exclude (n/a if the entry writes no rejected-sources row)"),
    ("Q13", "a verifier or recheck command is credited only for clauses whose deletion its own run is shown to detect; other clauses are named unguarded — item 11's credit must be bounded to the printed set and clause parsed"),
    ("Q14", "a hex string quoted with a byte count in the same clause carries 2×N hex characters; an ellipsis-truncated run carries no length; an `ASCII …` rendering decodes from that same run — sweep the whole entry, including the MANIFEST hex clause and the item 11 hex values"),
    ("Q15", "a stated git object id or tree identity is re-derived with the command that names it — verify the new criterion row in {QUALITY} is well-formed, run {Q15} --self-test (must pass), and run {Q15} --scan on {D1FIX} (must exit non-zero: the D1 false sentence is killed). Do not edit anything."),
]
for qid, qtext in Q_ITEMS:
    role = "critic" if qid in ("Q02", "Q04", "Q05", "Q07", "Q11", "Q13", "Q14") else "reviewer"
    items.append(seat(f"R69ReviewEntry{qid}", role, ["coverage", "calibration", "depth"],
                      Q_BASIS.format(qid=qid, qtext=qtext)))

# ------------------------------------------------------------- group B: entry integrity
items.append(seat("R69HeaderCheck", "reviewer", ["coverage", "depth"], f"""Entry header check (Q02/Q11) of the v4 candidate.

Do: read the entry's header block (the `source:`/`verified-at:`/`recheck:`/`coverage-map:`/`admission-status:` lines). For each of the five: state what it says and whether it is complete and honest on the CURRENT bytes. Specifically: does every `source:` row exist in {SOURCES} with the stated tier and scope (S032, S034, S038, S041, S043, S045, S047); does `recheck:` name commands that exist and run; does `verified-at:` match the round; does `admission-status:` describe the true state (candidate; README C05 row is still `uncovered`). Report each line with its entry line number and a verdict. Do not edit anything."""))
items.append(seat("R69QmapSelfCheck", "critic", ["coverage", "depth"], f"""Q-map self-consistency of the v4 candidate.

Do: read the entry's `## §Q-map` table and check it against the entry's own bytes: does each row's `basis` sentence point at something actually in the entry (a command, a line, a section)? Are the verdicts consistent with the content — in particular Q04 (manual-labeled widths), Q07 (observation-scoped namespace sentence), Q11 (every value carries its command), Q13 (bounded credit), Q14 (hex clauses swept)? Are any rows marked `n/a` that should not be? Report each row: id, verdict, basis pointer (entry line). Do not edit anything."""))
ITEM_TASKS = [
    ("1", "archive", "the archive digest/size fact"),
    ("2", "eocd", "the end-of-central-directory fact"),
    ("3", "member[AndroidManifest.xml]", "the AndroidManifest member fact"),
    ("3b", "member[classes.dex]", "the classes.dex member fact"),
    ("3c", "member[META-INF/MANIFEST.MF]", "the MANIFEST member fact"),
    ("4", "axml_chunk_table", "the AXML chunk-table fact"),
    ("5", "spec_derived_struct_widths", "the struct-widths fact"),
    ("6", "axml_string_pool", "the string-pool fact"),
    ("7", "axml_resource_map", "the resource-map fact"),
    ("8", "axml_start_element", "the start-element fact"),
    ("8b", "axml_start_namespace", "the start-namespace fact"),
    ("9", "dex_declared_header", "the dex declared-header fact"),
    ("10", "jar_manifest", "the jar-manifest fact"),
]
for gid, what, fact in ITEM_TASKS:
    items.append(seat(f"R69Item{gid}", "executor" if int(gid[0]) % 2 else "reviewer",
                      ["coverage", "depth"], f"""Per-item re-derivation ({fact}).

Do: from {LANE}, run `python3 -B corpus/fixtures/apk-r65/readout.py --fact {what}`. Capture the actual stdout and exit code. Then open {ENTRY}, find the block claiming this fact, and compare EVERY field of your actual output with the embedded line: name each field that differs. Then judge the entry's prose sentence about this fact: does it state anything the output does not support? Report the command, the actual output, the entry's embedded line (with its entry line number), and a field-by-field verdict. Verdict: MATCH or MISMATCH. Do not edit anything."""))
items.append(seat("R69OracleCorrespondence", "reviewer", ["coverage", "depth"], f"""Oracle correspondence of the v4 candidate.

Do: read {FIXTURE}/truth.json and the entry's `## Comparison with the authored oracle` section. Re-derive each shared field from the readout's actual stdout (run `python3 -B corpus/fixtures/apk-r65/readout.py` from {LANE} and use the full output) and compare with the oracle's declared value: image digest and size, the three members' offsets/sizes/CRC-32, the nine strings, the three attribute rows, the two non-zero resource ids. Report each shared field, oracle value, readout value, MATCH/MISMATCH. Do not edit anything."""))
items.append(seat("R69ReadmeFlipCheck", "executor", ["coverage"], f"""README C05 row and the flip precondition.

Do: read the C05 row of {README} and report its exact text and status cell. Then read {CLAIMS} §C1's precondition list and report, for each item, whether it holds on the current bytes: K_HELD_BACKED, K_HELD_BACKED_STRICT, C05 status, C05_SINGLE_V4, README_TOKEN_LEGEND_MISMATCH, HOLDS_C2_V4, C7_V4_CLEAN, the wave Q-decisions, the spot-check. Run the counter {COUNTER} over a scratch tree from `git -C {LANE} archive refs/heads/main corpus | tar -x -C <tree>` and quote the labels. Report which preconditions are met now. Verdict: FLIP-PRECONDITIONS-MET / NOT-MET (list the unmet ones). Do not edit anything."""))

# ------------------------------------------------------------- group C: derivation
items.append(seat("R69AnchorDerive", "executor", ["coverage", "operability"], f"""Re-derive the AXML spec anchors and enum values of {ENTRY} mechanically.

Do: run `python3 -B {DERIVE}` from {LANE} (cwd = lane root) and capture the exact stdout and exit code. Then extract EVERY line number and enum value the entry states for the AOSP source (the `source:` header anchor list, items 4/8/11 prose) and check each against the script's output. Report, per anchor, the entry's stated line, the derived line, and MATCH or MISMATCH. Also state exit code and whether the output is byte-identical across two runs. Verify the stdout sha256 (74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa for the script file; the stdout's 20 lines). Do not edit anything."""))
items.append(seat("R69AnchorBlind", "scout", ["coverage", "depth"], f"""Blind independent anchor derivation (no author's table).

Do NOT read {ENTRY} first. Open the pinned snapshot {SNAPSHOT} (sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f — verify it) and derive by your own search: line numbers of the seven structs; the enum block open/close lines and the eight enum constants (including RES_XML_FIRST_CHUNK_TYPE) with their hex values; the attributeStart comment and field lines. Then, and only then, open {ENTRY} and compare every number it states with your own derivation (items 4, 8, 11 and the header anchors). Report your derivation table, then the comparison, then CONCUR or DIVERGE (exact diverging numbers and lines). Do not edit anything."""))
items.append(seat("R69SnapshotFidelity", "executor", ["coverage", "freshness"], f"""Snapshot-copy fidelity.
Do: compute sha256 of {SNAP_COPY} and {SNAPSHOT}; report both, sizes, equality via `cmp`. Report `git -C {LANE} ls-files corpus/snapshots/` and `git -C {LANE} status --porcelain -- corpus/snapshots/`. State plainly: byte-identical, tracked. Do not edit anything."""))
items.append(seat("R69AnchorCritic", "critic", ["coverage", "depth"], f"""Attack the anchor derivation itself.

Do: read {DERIVE} and {ENTRY} item 11. Answer: (1) can the script print a line it did not find (trace the code path); (2) does the script's output pin the PROSE numbers, or only the embedded block — if someone edited prose `:245` to `:244` but left the block, would the registered gate {GATE} catch it? Run the gate on a scratch copy with such an edit (scratch only). (3) Can the snapshot copy drift without any check failing? (4) Is the enum-block bound logic (open 237 / close 263) robust — what does it do when the file has other `enum {{`/`}};` lines? Verdict: CLEAN or DEFECT with evidence. Do not edit anything."""))
items.append(seat("R69DeriveCritic", "critic", ["coverage", "depth"], f"""Attack the derivation script's failure behaviour.

Do: read {DERIVE}. In scratch copies only, corrupt the input three ways and report exit code/output for each: (1) truncate the snapshot copy; (2) change bytes so the digest differs; (3) duplicate one cited symbol (ambiguity). Report whether it refuses to print a line it did not find. Then state whether a corrupted `corpus/snapshots/` copy could make the v4 anchors wrong while the gate still passes (does the gate check the anchors or only reproducibility?). Verdict: FAILS-CLOSED or FAILS-OPEN. Do not edit the lane tree."""))

# ------------------------------------------------------------- group D: gate/counter
items.append(seat("R69MutC7Kill", "mutation-tester", ["calibration"], f"""Frozen-mutant attack on the C7 gate (hold, not a claim).

Do: copy {LANE}/corpus to a scratch temp dir. Apply the frozen mutant exactly: replace the single occurrence of `problems += drift(lines, stdout_set, lineno)` in {GATE} with `problems += []  # mutant: verbatim comparison removed`. Run `python3 -B corpus/check_embedded_outputs.py --self-test` in the scratch tree. Report exit code, full stdout+stderr, whether the LAST line ends with `drifted entry output accepted`. Verdict: KILLED-ATTRIBUTED / KILLED-UNATTRIBUTED / SURVIVED. Run the unmutated control too. Do not edit the lane tree."""))
items.append(seat("R69MutC7Spoof", "mutation-tester", ["calibration"], f"""Negative-spoof control (hold).

Do: scratch copy of {LANE}/corpus; apply BOTH the frozen mutant and the marker spoof (`MARKER = "drifted entry output accepted"` → `"drifted entry output accepted (spoofed)"`). Run the self-test there. Report exit code, full stdout+stderr, whether the LAST line ends with the registered marker (it must NOT). Verdict: NEGATIVE-CONTROL-AS-SPECIFIED or DEVIATION. Do not edit the lane tree."""))
items.append(seat("R69ReviewC7Gate", "reviewer", ["calibration", "depth"], f"""Review the C7 gate (hold).

Do: read {GATE} end to end. (1) Is the marker reachable on every `--self-test` failure path as the last line? (2) Does any require/exit fire before it on the frozen-mutant path? (3) Does the unmutated self-test still exit 0? Run it. (4) Does `--entry` still detect drift on the retained r65 candidate (exit 1 naming drift entry:41) and report clean on the v4 candidate? Verdict: CLEAN or DEFECT with lines. Do not edit anything."""))
items.append(seat("R69CriticC7Claim", "critic", ["calibration"], f"""Falsify C1's instrument hold as stated (the C7 L0 is OPEN: do not propose replacing marker-presence or editing V-labels).

Do: read {CLAIMS} §C1's C7 conjuncts and {GATE}. Try to show the frozen C7 predicate could pass without genuine drift detection (cosmetic marker, unconditional exit 1, marker on every run, counter edits). For each attempt: what you did in scratch, what the counter would print, whether the predicate would still pass. Report the counter's sha256 vs the pin in {CLAIMS}. Verdict: NOT-FALSIFIED or FALSIFIED (give the concrete path). Do not edit the lane tree."""))
items.append(seat("R69MutC7Entry", "mutation-tester", ["calibration", "coverage"], f"""Does the gate catch drift introduced into the v4 candidate?

Do: scratch copy of {LANE}/corpus; take the v4 candidate {ENTRY} into the scratch corpus tree, change ONE embedded output line (e.g. the archive byte count 947 → 948 in item 1's block), run `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-69-apk-axml-byte-evidence.md` there. Report exit code, drift message, named entry line. Then run the same on the UNMODIFIED v4 candidate (must be exit 0, 0 problems). Verdict: GATE-CATCHES-DRIFT or MISSES. Do not edit the lane tree."""))
items.append(seat("R69CriticC7Surface", "critic", ["calibration"], f"""Attack the gate's detection surface (open L0: report, do not change).
Do: read {GATE}. Enumerate what it does NOT catch: reordered/duplicated embedded lines, substring matches, empty blocks, non-first-line fences, changed stdout between runs. For each, state whether the gate would report it, from the code (file:line). State whether any could make the frozen C7 predicate pass while the gate is broken. Verdict: SURFACE-NOTED or CLAIM-AFFECTED. Do not edit anything."""))
items.append(seat("R69SimplifierGate", "simplifier", ["calibration", "depth"], f"""Simplify-review the C7 gate.
Do: read {GATE}. Report: (1) the smallest correct form of the self-test drift branch; (2) any now-dead code; (3) whether the public behaviour for a passing run is unchanged (exit 0, same SELFTEST OK). Verdict: SIMPLER-FORM or ALREADY-MINIMAL with quoted code. Do not edit anything."""))
items.append(seat("R69C7Hermetic", "reviewer", ["calibration", "operability"], f"""Hermeticity/determinism of the gate.

Do: run `python3 -B corpus/check_embedded_outputs.py --self-test` from {LANE} three times; report each exit and stdout (byte-identical?). Run with TMPDIR at a fresh dir and list what appeared there and whether anything appeared in {LANE} (`git -C {LANE} status --porcelain` before/after). Verdict: HERMETIC or NOT-HERMETIC. Do not edit anything."""))
items.append(seat("R69CounterReplay", "executor", ["calibration", "operability"], f"""Replay the frozen counter on the base tree (red-before).

Do: `git -C {LANE} archive refs/heads/main~1 corpus | tar -x -C <scratch tree>` (the base commit 222a7a702529fb60598633ebdf5e1442007bc15d — if `refs/heads/main~1` is not it, resolve with `git -C {LANE} log --format='%H %s' refs/heads/main -5` and pick the pre-registration's parent). Then from `/`: `TMPDIR=/tmp/r69-seat-replay python3 -B {COUNTER} <tree>`. Report FULL output and exit code. Compare labels against {BEFORE}: K_HELD_BACKED, C05_STATUS, C05_SINGLE_V4, HOLDS_C2_V4, Q15_PRESENT, Q15_*, C7_*, HOLDS_OK_V5/V6. Verdict: MATCH or MISMATCH (name differing labels). Do not edit anything."""))
items.append(seat("R69CounterIntegrity", "reviewer", ["calibration"], f"""Counter integrity.

Do: `sha256sum {COUNTER}` and compare with the pin in {CLAIMS} (bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377). `git -C {LANE} log --format='%H %s' -- reports/round-69/measure.py` — report every commit that touched it and whether the sha changed after the pre-registration commit e1d22caaf9a2fdc4c1c13d1f4a8a6813e7b07968 (it must not). Confirm the counter writes nothing outside TMPDIR (grep for writes). Verdict: INTACT or TAMPERED. Do not edit anything."""))
items.append(seat("R69HoldSweep", "executor", ["calibration"], f"""Prior-hold regression sweep.

Do: scratch tree from `git -C {LANE} archive refs/heads/main corpus | tar -x -C <tree>`; run all ten `verify_*.py` self-tests and report each exit; run the counter {COUNTER} over that tree and report HOLD_CALIBRATION, HOLD_REPLAY, FRESH_ROWS, F_COVERAGE, README_TOKEN_LEGEND_MISMATCH, STRICT_REJECT_WINDOW_SELFTEST, C2/C3/C4/C5/C6_*_ATTRIBUTED, C7_*, HOLDS_OK*. Verdict: NO-REGRESSION or REGRESSION (name label+value). Do not edit anything."""))
items.append(seat("R69CensusReplay", "executor", ["coverage", "freshness"], f"""Source-census replay.

Do: run `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`; report FULL output and exit. Report the row count of {SOURCES} (`grep -cE '^\\| S[0-9]+ ' {SOURCES}`), status/used-by of S046/S047, and whether any row other than S047 changed against the committed round-68 bytes (`git -C {LANE} diff refs/heads/main~2 -- {SOURCES}`). Verdict: CLEAN (exit 0, only disclosed W04s) or DEFECT. Do not edit anything."""))
items.append(seat("R69FixtureHold", "reviewer", ["coverage", "freshness"], f"""Fixture and live byte hold.

Do: `git -C {LANE} diff --stat 222a7a702529fb60598633ebdf5e1442007bc15d refs/heads/main -- corpus/live corpus/fixtures` (must be EMPTY). Also `git -C {LANE} diff --stat 222a7a7 refs/heads/main -- corpus` and list every changed/added path with a one-line reason. Verdict: HOLD-INTACT or HOLD-BROKEN. Do not edit anything."""))
items.append(seat("R69CorpusPathHygiene", "executor", ["coverage", "operability"], f"""Corpus path hygiene.

Do: report `git -C {LANE} ls-files corpus/ | sort`; identify paths this round added (round-69 entry, q15_tree_id_check.py). Check: tracked; size under the 1 MiB directory-commit rule; no __pycache__/ untracked artifacts (report `git -C {LANE} status --porcelain`); the `corpus/README.md` index mentions the new paths if needed. Verdict: HYGIENE-CLEAN or DEFECT with fixes. Do not edit anything."""))

# ------------------------------------------------------------- group E: claims
items.append(seat("R69CriticClaimsC1", "critic", ["coverage"], f"""Attack C1's claim shape.

Do: read {CLAIMS} §C1 and {ENTRY}. Check: the target is one concrete value re-derivable with one command over committed bytes (K_HELD_BACKED 9/14); the do-nothing control cannot reach it without the new entry AND an all-pass; the kill rule reserves the flip to an all-criteria pass and forbids re-targeting; no acceptance condition is repairable after scoring; the claim is separable from C2 (C1's labels must not depend on Q15 artifacts). Name any untestable or self-fulfilling clause. Verdict: NOT-FALSIFIED or DEFECT (with the clause). Do not edit anything."""))
items.append(seat("R69CriticClaimsC2", "critic", ["calibration"], f"""Attack C2's claim shape.

Do: read {CLAIMS} §C2, {QUALITY} Q15, and {Q15}. Check: the criterion row exists and is well-formed; the checker's self-test passes; the D1 fixture is killed (`--scan` exit non-zero); the red-before cannot reach Q15_PRESENT=yes without the row; the restatement's verification is honest (it re-derives via `git rev-parse`). Name any clause that is untestable or could pass vacuously. Verdict: NOT-FALSIFIED or DEFECT. Do not edit anything."""))
items.append(seat("R69CriticSeparability", "critic", ["calibration", "coverage"], f"""Separability audit.

Do: check C1 and C2 are causally separable from the counter {COUNTER}: C1's labels read the README C05 row, knowledge column, and the gate's V4-clean run; C2's labels read QUALITY Q15, the lessons/round-69.md restatement, and the q15 checker. Does any C1 label depend on a Q15 artifact (or vice versa)? Name any shared label and how to read it. Verdict: SEPARABLE / SEPARABLE-WITH-NAMED-SHARED-LABEL / NOT-SEPARABLE. Do not edit anything."""))
items.append(seat("R69CriticEntryDeps", "critic", ["coverage", "depth"], f"""Silent-dependency audit of the v4 entry.

Do: read {ENTRY}. List every value it states and where each comes from; name any value whose source is NOT visible inside the entry (an undeclared file/fact/tool/hash). Pay attention to item 11 and `corpus/snapshots/ResourceTypes.h`, and to the S032/S034-derived payload offsets. Verdict: NO-SILENT-DEPS or a list of unnamed ones with entry lines. Do not edit anything."""))
items.append(seat("R69CriticEntryScope", "critic", ["coverage", "depth"], f"""Scope and limitation audit (Q10) of the v4 entry.

Do: read {ENTRY} `## Limitations`, `## Cross-lane scope note (Q10)`, and `## Observation / inference / unknown`. Check no claim exceeds: one authored fixture, one manifest shape, UTF-8 string pool only, ZIP_STORED, a dex header only, manual standard-library analysis, no provider call. Name any generalising sentence. Verdict: SCOPE-CLEAN or SCOPE-BLEED (sentence+line). Do not edit anything."""))
items.append(seat("R69KillRuleClosure", "critic", ["calibration", "coverage"], f"""Kill-rule closure review (routed D5 item 3).

Do: read {CLAIMS} §C1/§C2 kill rules. Verify every mechanical conjunct of the pass branch also appears in the kill rule (a conjunct that reads off-target leaves a claim neither PASS nor FALSIFIED). Name any conjunct in the predicate that has no kill-rule counterpart, and whether that is a real gap for THIS round's claims. Verdict: CLOSED or GAP (name the conjunct). Do not edit anything."""))
items.append(seat("R69SentinelScope", "sentinel", ["coverage", "calibration"], f"""Containment and write-scope audit.

Do: check landed changes stay inside the lane and declared write scope, no protected surface moved. Commands: `git -C {LANE} diff --name-status 222a7a702529fb60598633ebdf5e1442007bc15d refs/heads/main`, `git -C {LANE} status --porcelain`, `git -C /home/vgpnk/Projects/shokunin status --porcelain | head -40` (fleet root: report only; do NOT touch anything there), and `git -C /home/vgpnk/Projects/shokuknow status --porcelain | head -20` (READ-ONLY, never write there). Report every changed path in the lane, whether any lane change touches corpus/live or corpus/fixtures, whether the fleet root/campaign tree show writes attributable to this round, and whether any fleet-root file names revenger/round-69. Verdict: CONTAINED or LEAK (path). Do not edit anything."""))
items.append(seat("R69ConnectorOverlap", "connector", ["coverage", "adjacency"], f"""Sibling-overlap scan (adjacency).

Do: scan sibling lane repos under /home/vgpnk/Projects/shokunin/ for work overlapping revenger's round-69 claims: AOSP AXML chunk-type anchors/enum values, the C05 APK container/dex declared-header ground, or the Q15 tree-identity criterion. Look at sibling `corpus/knowledge/` and `SCORECARD.md` (read-only). Report each overlap with sibling path and CONTEST-NAMED/CONTEST-UNNAMED; state whether revenger's claims stay inside its province. Verdict: CONTEST-NAMED / CONTEST-UNNAMED / NO-OVERLAP. Do not edit anything."""))
items.append(seat("R69RevengerLedger", "revenger", ["calibration"], f"""Adversarial ledger check on this round's own claims.

Do: read {CLAIMS}, {BEFORE}, and the round-68 closure {LANE}/corpus/lessons/round-68-verifier-spotcheck.md. Find any place where the r69 pre-registration repeats an r68 failure mode or misstates a number (tree ids, counts, sha pins, base/label). Also confirm every number in {CLAIMS} matches the committed red-before receipt {BEFORE} and the counter pin. Report each finding with exact line. Verdict: LEDGER-HOLDS or LEDGER-BROKEN. Do not edit anything."""))

# ------------------------------------------------- group F: frontier/quarantine/considerthese
items.append(seat("R69SpotcheckDiscern", "scribe", ["coverage", "calibration"], f"""Outside-discernment spot-check (adjudication aid, not a verdict).

Do: re-open ONE source row this round claims and check the row's anchor against the bytes it names. Use S047: open {DERIVE}, run it, confirm the located quote recorded in {SOURCES} for S047 (`enum RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100`) appears in the actual stdout, and that the row's script sha256 and snapshot sha256 match disk (`sha256sum {DERIVE} {SNAP_COPY}`). Then check ONE entry tier-A claim: confirm from {SNAPSHOT} that line 245 is RES_XML_START_NAMESPACE_TYPE, line 244 is RES_XML_FIRST_CHUNK_TYPE, the enum opens at 237 and closes at 263. Report both checks with outputs and AGREE/DISAGREE per check. Do not edit anything."""))
items.append(seat("R69ReviewSourcesS047", "reviewer", ["coverage", "calibration"], f"""Registry-row review for S047.

Do: read the S047 row in {SOURCES} and the registry contract in its header. Check: 11 columns, tier A justified for own-work, scope stated, anchor locatable, status/recheck/used-by legal, no literal or escaped `|` inside a cell, supersedes-S046 correctness, and the used-by cell consistent with the entry's state (candidate). Report each field with verdict and exact cell text. Verdict: ROW-CLEAN or ROW-DEFECT with fixes. Do not edit anything."""))
QUAR_BRIEF = f"""Quarantine register hand-check (wave-4; adoption stays closed). Read-only campaign tree.

Do: read {REGISTER} (the absent-defect register). Derive THIS LANE'S slice: data rows whose lane cell matches `revenger`, with a round cell and an S-id cell (summary rows print blanks — skip them). Your assigned rows: {{rows}}.

For EACH assigned row: fetch the cited source (curl -sL --max-redirs 15, read-only; PDFs/APKs saved as files), locate the register's quoted span in the fetched bytes (raw and every text rendering), and record a verdict: PRESENT (quote found verbatim — register wrong) / ABSENT (quote in none of the renderings — fabrication-class confirm) / UNREACHABLE (fetch failed, 404/timeout — not fabrication) / UNVERIFIED-REACHABLE (arrayse-class row: no locator, or the fetch succeeded but the quote cannot be located). Save fetched bytes under /tmp/revenger-r69-quarantine/<S-id>/ (delete before returning) and cite exact offsets. Do NOT edit the register or any campaign file. Verdict per row on separate lines: `<S-id> <VERDICT> <one-line reason>`; end with the tally for your rows."""
items.append(seat("R69QuarA", "scout", ["coverage", "calibration"], QUAR_BRIEF.format(rows="S053, S054, S055, S058, S060, S061, S062, S063, S064")))
items.append(seat("R69QuarB", "scout", ["coverage", "calibration"], QUAR_BRIEF.format(rows="S075, S081, S083, S085, S087, S089, S090, S092, S093")))
items.append(seat("R69QuarC", "scout", ["coverage", "calibration"], QUAR_BRIEF.format(rows="S094, S095, S098, S099, S100, S107, S108, S111, S113")))
items.append(seat("R69QuarD", "scout", ["coverage", "calibration"], QUAR_BRIEF.format(rows="any further revenger data rows in the register beyond the 27 named (re-derive the slice; if none remain, fetch the full register and confirm the row count and the register's `## By lane` summary mismatch)")))
items.append(seat("R69Considerthese", "scribe", ["coverage", "calibration"], f"""considerthese proposal implementation check.
Do: read {LANE}/considerthese/2026-10-24.md proposal 2 (provider refusals recorded as their own line). Verify this round's wave record will satisfy it: enumerate what data a wave record must carry to record provider-refusal seat losses as their own line (role, route, what was attacked, refusal text), and check whether the committed r68 wave record already carries it (read .ufo/waves/round-68/dispatch/plan-validated.json and R68WaveContractAudit.md if present). State what the r69 report must add. Verdict: REQUIREMENTS-STATE with the checklist. Do not edit anything."""))
items.append(seat("R69LessonCheck", "scribe", ["coverage", "calibration"], f"""Lesson and mistake-class requirements for round 69.

Do: read {CLAIMS} §Frontier step and the round-68 closure {LANE}/corpus/lessons/round-68-verifier-spotcheck.md §5. The round must mine one mistake into `corpus/lessons/round-69.md` `## Mistakes` (class · evidence pointer · captured-by · fix), a fix counts only shown able to fail, and the lesson must carry the D1 restatement (two tree-identity lines: a `tree-identity restatement:` line that re-derives, and a `tree-identity false-sentence:` line that fails — matching {Q15}'s parser). State which mistake class(es) round 69 should mine (candidates: M48 identity-sentence-without-re-derivation; M49 enum-block-bound number-drift) and what evidence pointers the lesson must carry. Verdict: REQUIREMENTS-STATE. Do not edit anything."""))

# ------------------------------------------------------------- group G: residuals
items.append(seat("R69WaveContractAudit", "sentinel", ["coverage", "calibration"], f"""Wave-contract audit.

Do: read {CLAIMS} §Wave contract and this wave's spec {LANE}/.ufo/waves/round-69/wave-spec.json. Check: exactly 64 seats, one batched dispatch call, >= 25% attack roles under BOTH predicates (build-wave-spec.py's: reviewer/critic/mutation-tester/sentinel/revenger; prompt §2 v2 floor: reviewer/critic/mutation-tester/labrat — count both), every seat's item a distinct concrete work item serving C1/C2/frontier/D-repairs (name any padding), role mix covers connector + executors + scribe + scout + reviewers + critics, and the §3 planner seat is held by the L1 (the validator rejects `planner` — verify by running `node ~/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs plan --spec {LANE}/.ufo/waves/round-69/wave-spec.json` and quoting its output). Report counts, both attack percentages, any padding seat. Verdict: CONTRACT-OK or CONTRACT-BROKEN. Do not edit anything."""))
items.append(seat("R69MisrootSweep", "sentinel", ["coverage", "calibration"], f"""Misroot sweep (the fleet-root check).

Do: run `git -C /home/vgpnk/Projects/shokunin status --porcelain` and list every untracked/modified file at the fleet root; for each, decide whether it is a revenger/round-69 seat note that landed at the fleet root (content names revenger or round-69) — report each such file (path + first line); do NOT touch anything. Also confirm .ufo/state/ and .scratch/ are not touched. Verdict: NO-MISROOT or MISROOT (paths). Do not edit anything."""))
items.append(seat("R69Q15CheckerRun", "executor", ["calibration"], f"""Run the Q15 checker end-to-end.

Do: from {LANE}: `python3 -B {Q15} --self-test` (must exit 0); `python3 -B {Q15} --scan {D1FIX} --lane {LANE}` (must exit non-zero — the false sentence is killed); and build a scratch file with the TRUE restatement pairs (`1c34603:corpus` = `ddc6a4f6aea51ef34e0b7669832ff1a9cb2023f7`; `dddf147:corpus` = `51894d153a6e69487da2a273680d014abd240f61`) plus the false-sentence line, and run `--scan` on it (must exit 0). Record the three exit codes and outputs. Verdict: CHECKER-AS-SPECIFIED or DEVIATION. Do not edit anything."""))
items.append(seat("R69DeriveDeterminism", "executor", ["coverage", "operability"], f"""Derivation determinism.
Do: run `python3 -B {DERIVE}` twice from {LANE}; diff the two outputs (must be byte-identical); also run it from /tmp with absolute path arguments equivalent to the lane-root invocation and confirm the same stdout. Report both diffs and exit codes. Verdict: DETERMINISTIC or NOT. Do not edit anything."""))
items.append(seat("R69EntryHexAudit", "reviewer", ["coverage", "depth"], f"""Q14 hex sweep of the v4 entry.
Do: read {ENTRY}; extract every quoted hex string with an adjacent byte-count or ASCII-rendering clause; for each, verify 2×N hex chars vs the stated byte count and that the ASCII rendering decodes from the same run. Sweep items 1-11, the header digests (sha256 = 64 hex chars = 32 bytes, fine), and the MANIFEST clause. Report each clause, its hex length, stated count, PASS/FAIL. Verdict: ALL-CLEAN or Q14-FAIL (list lines). Do not edit anything."""))
items.append(seat("R69CounterShaAudit", "reviewer", ["calibration"], f"""Counter pin audit.
Do: `sha256sum {COUNTER}` → must equal bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377 (the claims.md pin). Also `git -C {LANE} diff e1d22caaf9a2fdc4c1c13d1f4a8a6813e7b07968 refs/heads/main -- reports/round-69/measure.py` must be empty. Verdict: PIN-INTACT or TAMPERED. Do not edit anything."""))
items.append(seat("R69D1RestateCheck", "reviewer", ["calibration"], f"""D1 restatement feasibility check.

Do: read {D1FIX} and the round-68 `reports/round-68/measure-after.log:102` (the false tree-identity sentence). Re-derive: `git -C {LANE} rev-parse 1c34603:corpus` and `git -C {LANE} rev-parse dddf147:corpus`; report both outputs and state which sentence the round-69 lesson must carry as the restatement (pairs that resolve) and which as the quoted false sentence (pairs that fail). Confirm the q15 checker parses both forms. Verdict: RESTATEMENT-SPECIFIED or DEVIATION. Do not edit anything."""))
items.append(seat("R69ShonenBox1", "reviewer", ["calibration", "depth"], f"""SHONEN box-1 reconciliation check (routed D4).

Do: read {LANE}/SHONEN.md and {SKILL} (the lane's decision tables, error patterns, checklists, cited sources) plus the round-68 SCORECARD paragraph that says box 1 "keeps its `[~]`-with-outside-verifier state". State what the committed SHONEN.md box 1 actually reads (`[x]` with named verifier `revenger-r64.R64ReviewSkill`), whether the ring-68 paragraph conflicts with it, and what the round-69 SCORECARD entry must append to reconcile (append-only). Also judge whether box 1 holds on the CURRENT bytes (decision-bearing tables, named error patterns, executable checklists, every citation resolves). Report your verdict and note you are a lane-dispatched seat (not a non-author verifier). Do not edit anything."""))
# The frozen wave contract registers EXACTLY 64 seats. The drafted item set grew
# to 76; twelve redundant seats drop (each covered by another seat's attack): the
# per-member/namespace item re-derivations R69Item3b/3c/8b (covered by the full-
# stdout diff in R69OracleCorrespondence and the hold sweep), R69Item5/7 (covered
# by Q04/Q11 + the oracle correspondence), R69SnapshotFidelity (covered by
# R69AnchorBlind and R69DeriveCritic), R69CriticC7Surface (covered by
# R69CriticC7Claim + R69ReviewC7Gate; the C7 L0 stays open), R69SimplifierGate
# (not a required role), R69Considerthese (the proposal-2 line is an L1 report
# item), R69DeriveDeterminism (covered by R69AnchorDerive's double-run),
# R69EntryHexAudit (covered by the Q14 seat), R69CounterShaAudit (covered by
# R69CounterIntegrity).
DROP = {
    "R69Item3b", "R69Item3c", "R69Item8b", "R69Item5", "R69Item7",
    "R69SnapshotFidelity", "R69CriticC7Surface", "R69SimplifierGate",
    "R69Considerthese", "R69DeriveDeterminism", "R69EntryHexAudit",
    "R69CounterShaAudit",
}
items = [i for i in items if i["name"] not in DROP]


# ------------------------------------------------------------------- assemble
spec = {
    "wave": "revenger-r69-v2",
    "milestone": "C1 C05 v4 re-gate + C2 Q15 criterion as build state (README not flipped); wave: Q01-Q15, C7 holds, derivation re-runs, counter replays, quarantine hand-checks, D1-D5 audits",
    "reportDir": REPORT_DIR,
    "axes": ["coverage", "calibration", "depth", "freshness", "adjacency"],
    "context": CONTEXT,
    "items": items,
}

names = [i["name"] for i in items]
if len(names) != len(set(names)):
    dupes = {n for n in names if names.count(n) > 1}
    print("duplicate seat names:", dupes, file=sys.stderr)
    sys.exit(1)
roles = {}
for i in items:
    roles[i["role"]] = roles.get(i["role"], 0) + 1
attack = sum(v for r, v in roles.items()
             if r in ("reviewer", "critic", "mutation-tester", "sentinel", "revenger"))
attack2 = sum(v for r, v in roles.items()
              if r in ("reviewer", "critic", "mutation-tester", "labrat"))
print(f"seats={len(items)} roles={roles}")
print(f"attack(lane predicate)={attack} ({100 * attack / len(items):.1f}%)")
print(f"attack(v2 floor list)={attack2} ({100 * attack2 / len(items):.1f}%)")
if len(items) != 64:
    print("WARNING: expected 64 seats", file=sys.stderr)
WAVE_DIR.mkdir(parents=True, exist_ok=True)
out = WAVE_DIR / "wave-spec.json"
out.write_text(json.dumps(spec, indent=1), encoding="utf-8")
print(f"written: {out}")
