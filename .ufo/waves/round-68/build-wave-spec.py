#!/usr/bin/env python3
"""Round-68 wave-spec generator (revenger L1, Kimi fresh L1).

Renders `.ufo/waves/round-68/wave-spec.json`: ONE v2 wave of exactly 64 seats
under scripts/hyaku/ufo-wave-policy-v2.json (band 64-128, maxLanes 256),
build items and attack items together, every item a distinct concrete work item
serving the round's two declared claims (C1 calibration, C2 coverage) plus the
frontier step and the r67 routed repairs.

The godspeed directive bytes are lifted byte-exact from the committed round-67
wave spec (`.ufo/waves/round-67/wave-spec.json`, item 0) so the host binding is
reproduced verbatim and never paraphrased.

Run from the lane root:  python3 -B .ufo/waves/round-68/build-wave-spec.py
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
WAVE_DIR = ROOT / ".ufo/waves/round-68"
R67_SPEC = ROOT / ".ufo/waves/round-67/wave-spec.json"

LANE = "/home/vgpnk/Projects/shokunin/revenger-shokunin"
ENTRY = f"{LANE}/corpus/knowledge/round-68-apk-axml-byte-evidence.md"
R67_ENTRY = f"{LANE}/corpus/knowledge/round-67-apk-axml-byte-evidence.md"
GATE = f"{LANE}/corpus/check_embedded_outputs.py"
DERIVE = f"{LANE}/corpus/derive_axml_anchors.py"
COUNTER = f"{LANE}/reports/round-68/measure.py"
CLAIMS = f"{LANE}/reports/round-68/claims.md"
BEFORE = f"{LANE}/reports/round-68/measure-before.log"
SNAPSHOT = f"{LANE}/.ufo/waves/round-65/source-snapshots/ResourceTypes.h"
SNAP_COPY = f"{LANE}/corpus/snapshots/ResourceTypes.h"
README = f"{LANE}/corpus/README.md"
SOURCES = f"{LANE}/corpus/SOURCES.md"
SKILL = f"{LANE}/SKILL.md"
QUALITY = f"{LANE}/corpus/QUALITY.md"
FIXTURE = f"{LANE}/corpus/fixtures/apk-r65"
REPORT_DIR = ".ufo/waves/round-68"


def godspeed_prefix():
    spec = json.loads(R67_SPEC.read_text(encoding="utf-8"))
    prompt = spec["items"][0]["prompt"]
    marker = "Act directly via tool calls."
    idx = prompt.index(marker) + len(marker)
    return prompt[:idx]


GODSPEED = godspeed_prefix()

CONTEXT = f"""# Goal
Revenger round 68 (hyaku, Kimi fresh L1) — ONE v2 wave of exactly 64 seats, build and attack together. Lane repo: {LANE} — ABSOLUTE paths only in every read and write (your tools start at the fleet root /home/vgpnk/Projects/shokunin).

# Frozen contract (read first — it overrides any summary here)
{LANE}/reports/round-68/claims.md — the two declared claims (C1 calibration, C2 coverage), their frozen predicates, kill rules, do-nothing controls, void conditions and admission order.
{LANE}/reports/round-68/measure.py — the frozen counter (sha256 0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766; never edited after pre-registration).
{LANE}/reports/round-68/measure-before.log — the red-before receipt on base f165908 (C7_MUTANT_KILLED_ATTRIBUTED=0/1, HOLDS_OK_V5=no, HOLDS_OK_V6=no, K_HELD_BACKED=8/14, C05 uncovered, counter exit 0).

# Build state landed by the L1 before this wave (your attack surface)
- C1: {GATE} — the registered embedded-output gate, REPAIRED: the attributed marker `drifted entry output accepted` is now reachable and is the LAST output line of a failed self-test run (round-67 M45 shadowing removed). Registry row in {SKILL} `## Gate registry`.
- C2: {ENTRY} — the C05 v3 candidate (`admission-status: candidate`; the README C05 row is NOT flipped, it stays `uncovered` until an all-criteria pass). It is the round-67 candidate plus the two `:244` -> `:245` anchor fixes, plus item 11 whose embedded command is `{DERIVE}`.
- {SNAP_COPY} — byte-exact copy of the lane's pinned snapshot {SNAPSHOT} (sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f, 86255 bytes).
- {SOURCES} — S046 (own-work, tier A, opened 2026-10-24) is the row C2 cites; it is the frontier step's sourced row.

# Counting command (measure over committed trees only)
git archive <commit> corpus | tar -x -C <tree>
cd / && TMPDIR=/tmp/revenger-r68-counter-XXXX python3 -B {COUNTER} <tree>

# Quality bar
{LANE}/corpus/QUALITY.md (Q01-Q13). The entry's own Q-map is at {ENTRY} `## §Q-map` — you are checking it, not trusting it.

# Bounds (hard)
Write ONLY your own report file at the absolute path named at the end of your brief (under {LANE}/{REPORT_DIR}/). Everything else is read-only for you: corpus/, reports/, LOG.md, SCORECARD.md, SHONEN.md, the fleet repo, sibling lane repos, {LANE}/.git, the lane jj state and the lane Git index. Do NOT run git/jj mutations. Do NOT edit any file another seat may own. Never write into /home/vgpnk/Projects/shokuknow (READ-ONLY: never write, commit, fetch-push or run campaign tools there). Do not touch {LANE}/corpus/live/ or {LANE}/corpus/fixtures/ (read-only; the fixture bytes are the claim surface). Read-only seats return findings without production edits. Never message other seats; never use agent://all. Every `Report:` trailer path is relative to {LANE} — write it at {LANE}/<that path>. Absolute paths everywhere.

# Tooling authorization (operator, 2026-10-19)
You and every seat may install or upgrade tools that help the task — read /home/vgpnk/.omp/agent/RULES.md first (official channels, update-safety gate, record tool/version/channel/reason in your report). Pacman guard (orchestrator ruling 2026-10-20): all pacman transactions are PAUSED host-wide — install via uv tool/npx/an official binary in ~/.local/bin, or file an L0 question; never -Sy/-Syu/-U/-R, never downgrade, never restart a host service.

# Seat rules
Time-box: return within 12 minutes with your best findings + evidence; partial results are acceptable. You are an independent leaf: never block on or wait for another seat; never spawn subagents; if a needed artifact is absent, record the dependency as a finding and return. Put your verdict on the FIRST line of your report (PASS / FAIL / NOT-FALSIFIED / ADMIT / REJECT / CLEAN / PRESENT / HOLDS / FALSIFIED + one-line reason), then evidence: commands with their actual output, file:line pointers, sha256 where relevant. Ground every claim in a resolvable pointer; a claim without one is not evidence."""


def seat(name, role, axes, task):
    return {
        "name": name,
        "role": role,
        "axes": axes,
        "prompt": f"{GODSPEED}\n\n{task}\n\nWrite your report at {LANE}/{REPORT_DIR}/{name}.md",
    }


items = []

# ---------------------------------------------------------------- group A: Q01-Q13
Q_BASIS = """You are a fresh admission reviewer for {entry} (the round-68 C05 v3 candidate, `admission-status: candidate`). Read {claims} §C2 first, then {quality}, then the entry.

Your criterion: {qid} — {qtext}

Do: read the entry's own bytes (absolute path above). Decide PASS / FAIL / n/a **for this criterion only**, on these bytes. For a FAIL, name the exact line(s) and the exact value that is wrong, and say what the correct value would be. For PASS, say which command or which line proves it and quote the observed output. Re-derive every value you rely on: run the entry's own commands yourself and compare their actual stdout with the entry's embedded lines; a value that the command does not print is a FAIL for Q11 and a FAIL for the criterion that carries it. Never accept the entry's Q-map row as evidence for your own criterion. Do not edit any file. Report the criterion id, the verdict, the evidence commands and their outputs, then the entry lines at issue."""

Q_ITEMS = [
    ("Q01", "each load-bearing claim rests on a `corpus/SOURCES.md` row that is tier A for that claim's scope and was opened in the round that wrote it (a tier-C row is never sole support)"),
    ("Q02", "the entry opens with `source:` (its `S###` row, URL or path, exact anchor), `verified-at:` and `recheck:`, and names the coverage-map row it fills — and every anchor it states is the right line of the cited document"),
    ("Q03", "expected values are derived independently — from bytes, a specification, or a pin fixed outside the record under test; nothing is copied from the record being checked"),
    ("Q04", "a tool claim names the tool, version and function exercised and scores the tool's own output; manual analysis is labeled as manual"),
    ("Q05", "a readiness or capability claim carries a probe against the real surface — command, date and observed exit, output or Evidence ID; presence or configuration is not capability"),
    ("Q06", "fixture premises are byte-verified against the built fixture after every edit and before any producer call; failed inputs are retained"),
    ("Q07", "a predicted parser behavior is a pre-registered hypothesis with spec-derived ground truth, recorded whichever way it falls"),
    ("Q08", "superseded by Q11 — apply Q11 and say so"),
    ("Q09", "a digest or receipt is claimed only for the exact bytes it hashed; it does not establish producer origin, acquisition completeness or authenticity"),
    ("Q10", "a finding is scoped to the observed family, operation, version and input; cross-lane contested scope is reported, not absorbed"),
    ("Q11", "each count, identifier, offset and digest carries, inside the entry, the command that derives it from the primary record and that command's output; constants such as header offsets are derived, not assumed; a value cited only to prose is labeled recorded, not re-derived"),
    ("Q12", "a rejected source row states a reject reason grounded in a located quote, and its `flip` names a change to the source or a scope the reject reason does not exclude"),
    ("Q13", "a verifier or recheck command is credited in an entry only for the clauses whose deletion its own run is shown to detect; other clauses are named as unguarded"),
]
for qid, qtext in Q_ITEMS:
    role = "critic" if qid in ("Q02", "Q11") else "reviewer"
    items.append(seat(f"R68ReviewEntry{qid}", role, ["coverage", "calibration", "depth"],
                      Q_BASIS.format(entry=ENTRY, claims=CLAIMS, quality=QUALITY, qid=qid, qtext=qtext)))

# ------------------------------------------------------------- group B: anchors
items.append(seat("R68AnchorDerive", "executor", ["coverage", "operability"], f"""Re-derive the AXML spec anchors of {ENTRY} mechanically.

Do: run `python3 -B {DERIVE}` from {LANE} (cwd = lane root) and capture the exact stdout and exit code. Then extract EVERY line number the entry states for the AOSP source (the `source:` header's anchor list and the prose of items 4, 5 and 8) and check each against the script's output. Report, per anchor, the entry's stated line, the derived line, and MATCH or MISMATCH. Also state the exit code and whether the script's output is reproducible across two runs (byte-identical). Finally, quote the entry lines where you extracted the numbers (file:line). Do not edit anything."""))

items.append(seat("R68AnchorBlind", "scout", ["coverage", "depth"], f"""Blind independent anchor derivation (no author's table).

Do NOT read {ENTRY} first. Open the pinned snapshot {SNAPSHOT} (sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f — verify it) and derive, by your own search, the line numbers of: the `struct ResChunk_header`, `struct Res_value`, `struct ResStringPool_header`, `struct ResXMLTree_header`, `struct ResXMLTree_node`, `struct ResXMLTree_attrExt`, `struct ResXMLTree_attribute` declarations; the enum constants RES_STRING_POOL_TYPE, RES_XML_TYPE, RES_XML_START_NAMESPACE_TYPE, RES_XML_END_NAMESPACE_TYPE, RES_XML_START_ELEMENT_TYPE, RES_XML_END_ELEMENT_TYPE, RES_XML_RESOURCE_MAP_TYPE; the comment "Byte offset from the start of this structure where the attributes start" and the field declaration `uint16_t attributeStart;`. Then, and only then, open {ENTRY} and compare every number it states with your own derivation. Report your derivation table, then the comparison, then a verdict line: CONCUR or DIVERGE (with the exact diverging numbers and lines). Do not edit anything."""))

items.append(seat("R68SnapshotFidelity", "executor", ["coverage", "freshness"], f"""Snapshot-copy fidelity.

Do: compute sha256 of {SNAP_COPY} and of {SNAPSHOT}; report both, the byte sizes, and whether they are equal (use `cmp` as well). Then check `git -C {LANE} ls-files corpus/snapshots/` and report whether the copy is tracked, and run `git -C {LANE} status --porcelain -- corpus/snapshots/`. State plainly: is the committed copy byte-identical to the pinned snapshot, and is it tracked in the repository? Do not edit anything."""))

items.append(seat("R68AnchorCritic", "critic", ["coverage", "depth"], f"""Attack the anchor derivation itself (is it a real capture, or a tautology?).

Do: read {DERIVE} and {ENTRY} item 11. Answer: (1) can the derivation script print a line number it did not actually find in the bytes — trace the code path; (2) does the script's output actually pin the entry's PROSE numbers, or only the numbers in the embedded block — i.e. if someone edited the entry's prose from `:245` to `:244` and left the embedded block alone, would the registered gate {GATE} catch it? Run the gate on a scratch copy of the entry with such an edit (scratch only, never in the lane tree) and report what happens. (3) is the input copy {SNAP_COPY} able to drift from the upstream pinned snapshot without any check failing? Verdict: CLEAN or DEFECT, with the evidence. Do not edit anything."""))

# R68AnchorBlind2 dropped on the round-68 repair: the frozen wave contract
# registers EXACTLY 64 seats and the spec had grown to 66. The second blind
# derivation (a different enum slice by a second scout) is fully covered by
# R68AnchorBlind's independent derivation; the redundant seat goes, not the
# independent one.

# ---------------------------------------------------------------- group C: the gate
items.append(seat("R68MutC7Kill", "mutation-tester", ["calibration"], f"""Frozen-mutant attack on the repaired gate (C1's kill rule).

Do: copy {LANE}/corpus to a scratch temp dir (never modify the lane tree). In the copy, apply the frozen mutant exactly: replace the single occurrence of the line `problems += drift(lines, stdout_set, lineno)` in {GATE} with `problems += []  # mutant: verbatim comparison removed` (assert the regex matched exactly once). Run `python3 -B corpus/check_embedded_outputs.py --self-test` in the scratch tree. Report: exit code, the FULL stdout+stderr, and whether the LAST line ends with the exact string `drifted entry output accepted`. Verdict: KILLED-ATTRIBUTED (exit != 0 and last line ends with the marker) or KILLED-UNATTRIBUTED or SURVIVED. Also run the unmutated control in the same scratch tree and report its exit code and last line. Do not edit the lane tree."""))

items.append(seat("R68MutC7Spoof", "mutation-tester", ["calibration"], f"""Negative-spoof control (C1's negative control).

Do: in a scratch copy of {LANE}/corpus, apply BOTH the frozen mutant (the `problems += drift(...)` line replaced by `problems += []`) AND the marker spoof (the single occurrence of `MARKER = "drifted entry output accepted"` replaced by `MARKER = "drifted entry output accepted (spoofed)"`; assert each replacement matched exactly once). Run `python3 -B corpus/check_embedded_outputs.py --self-test` there. Report exit code, full stdout+stderr, and whether the LAST line ends with `drifted entry output accepted` (it must NOT — the last line ends with the spoofed text). Verdict: NEGATIVE-CONTROL-AS-SPECIFIED (exit != 0 AND last line does NOT end with the marker) or DEVIATION. Also report what the unspoofed frozen mutant does in the same scratch tree for contrast. Do not edit the lane tree."""))

items.append(seat("R68ReviewC7Gate", "reviewer", ["calibration", "depth"], f"""Review the C7 repair for reachability and shadowing.

Do: read {GATE} end to end. Answer precisely: (1) is the marker `drifted entry output accepted` reachable on EVERY failure path of `--self-test`, and specifically is it now the last output line when the verbatim comparison is removed? Trace the control flow and quote the lines; (2) is any other require or exit able to fire BEFORE the marker on that path (the round-67 defect was exactly such a shadowing require — name every require/exit on the path and its line); (3) does the unmutated self-test still exit 0 and print its SELFTEST OK line? Run it. (4) does `--entry` mode still detect drift? Run `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-65-apk-axml-byte-evidence.md` from {LANE} and report exit code + last line. Verdict: CLEAN or DEFECT with the exact lines. Do not edit anything."""))

items.append(seat("R68CriticC7Claim", "critic", ["calibration"], f"""Falsify C1 as stated.

Do: read {CLAIMS} §C1 and {GATE}. Try to show that the claim's predicate can be satisfied without a genuine repair — e.g. by a cosmetic marker print, by an unconditional exit 1, by a marker printed on every run including the passing control, by weakening the drift comparison in a way the mutant regex would not catch, or by editing the counter rather than the gate. For each attempt: state what you did (in a scratch copy), what the counter would print, and whether the frozen predicate would still pass. Report the counter's own sha256 (`sha256sum {COUNTER}`) and whether it still matches the pin in {CLAIMS}. Verdict: NOT-FALSIFIED (the predicate cannot be gamed) or FALSIFIED (a concrete gaming path exists — give it). Do not edit the lane tree."""))

items.append(seat("R68MutC7Entry", "mutation-tester", ["calibration", "coverage"], f"""Does the repaired gate actually catch drift introduced into the C05 candidate?

Do: in a scratch copy of {LANE}/corpus, take the v3 candidate {ENTRY} (copied into the scratch corpus tree), change ONE embedded output line of one of its `$ cmd` blocks (e.g. change the archive byte count 947 to 948 in the item-1 block), and run `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md` in the scratch tree. Report exit code, the drift message and its named entry line. Then run the same command on the UNMODIFIED v3 candidate in the scratch tree and report exit code + last line (it must be 0 with 0 problems). Verdict: GATE-CATCHES-DRIFT or GATE-MISSES-DRIFT. Do not edit the lane tree."""))

items.append(seat("R68CriticC7Surface", "critic", ["calibration"], f"""Attack the repaired gate's detection surface.

Do: read {GATE}. Enumerate what the gate does NOT catch and whether the round-68 repair changed that surface at all (it should not have): reordered or duplicated embedded output lines, an embedded output line that is a SUBSTRING of a real stdout line, a command whose stdout changes between runs, a `$ cmd` block whose output is empty, a block that is not the first line of the fence. For each, state whether the gate would report it, and give the reason from the code (file:line). Then state whether any of these could make the C1 predicate pass while the gate is broken. Verdict: SURFACE-NOTED with the list, or CLAIM-AFFECTED if a broken gate could still pass C1. Do not edit anything."""))

items.append(seat("R68SimplifierGate", "simplifier", ["calibration", "depth"], f"""Simplify-review the C7 repair.

Do: read {GATE}, specifically the self-test block that the round-68 repair rewrote. Report: (1) the smallest correct form of that block (quote it), (2) whether the now-unused helper `ok()` was correctly removed and whether anything else in the file is now dead, (3) whether the repair kept the file's public behaviour identical for a passing run (exit 0, same SELFTEST OK line). Give a one-line verdict: SIMPLER-FORM or ALREADY-MINIMAL, with the quoted code. Do not edit anything."""))

items.append(seat("R68C7Hermetic", "reviewer", ["calibration", "operability"], f"""Is the repaired gate hermetic and deterministic?

Do: run `python3 -B corpus/check_embedded_outputs.py --self-test` from {LANE} three times and report each exit code and stdout (byte-identical?). Then check the gate writes nothing outside its own temp dirs: run it with TMPDIR pointed at a fresh directory and list what appeared there and whether anything appeared in {LANE} (compare `git -C {LANE} status --porcelain` before and after). Report the before/after status output. Verdict: HERMETIC or NOT-HERMETIC, with the evidence. Do not edit anything."""))

# --------------------------------------------------- group D: counter and holds
items.append(seat("R68CounterReplay", "executor", ["calibration", "operability"], f"""Replay the frozen counter on the base tree (red-before).

Do: `git -C {LANE} archive refs/heads/main~2 corpus | tar -x -C <scratch tree>` (the base commit f165908aaffcf14798de53405fe788986bd33ff9 — if `refs/heads/main~2` is not it, resolve with `git -C {LANE} log --format='%H %s' refs/heads/main -5` and pick the commit whose subject is the round-68 pre-registration's parent). Then run from `/`: `TMPDIR=/tmp/r68-seat-replay python3 -B {COUNTER} <tree>`. Report the FULL output and the exit code. Check the printed labels against {BEFORE}: C7_MUTANT_KILLED_ATTRIBUTED, C7_NEG_SPOOF_KILLED, C7_NEG_SPOOF_KILLED_ATTRIBUTED, C7_V3_CLEAN, K_HELD_BACKED, C05_STATUS, HOLDS_OK_V5, HOLDS_OK_V6. Verdict: MATCH or MISMATCH (name every differing label). Do not edit anything."""))

# R68CounterReplay2 dropped on the same repair: R68HoldSweep already runs the
# frozen counter over the committed tree and reports every C7_*/C05_*/HOLDS_*/
# K_* label on it, so the second after-run replay was a duplicate seat.

items.append(seat("R68CounterIntegrity", "reviewer", ["calibration"], f"""Counter integrity.

Do: `sha256sum {COUNTER}` and compare with the pin in {CLAIMS} (0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766). Also `git -C {LANE} log --format='%H %s' -- reports/round-68/measure.py` and report every commit that touched it and whether the sha256 changed after the pre-registration commit f505526f7ecf4ac1ad51d99aa2d1dd5c57c0bae0 (it must not have). Also confirm the counter writes nothing outside TMPDIR: the counter creates temp dirs via tempfile; grep the file for any write outside a temp path (`grep -n "open(\\|write_text\|write_bytes" {COUNTER}`) and report the result. Verdict: INTACT or TAMPERED. Do not edit anything."""))

items.append(seat("R68HoldSweep", "executor", ["calibration"], f"""Prior-hold regression sweep.

Do: in a scratch tree from `git -C {LANE} archive refs/heads/main corpus | tar -x -C <tree>`, run every one of the ten `verify_*.py` self-tests (the replay family) and report each exit code. Then run the counter {COUNTER} over that same tree and report HOLD_CALIBRATION, HOLD_REPLAY, FRESH_ROWS, F_COVERAGE, README_TOKEN_LEGEND_MISMATCH, STRICT_REJECT_WINDOW_SELFTEST, C2/C3/C4/C5/C6_*_ATTRIBUTED and HOLDS_OK*. Verdict: NO-REGRESSION (all at the round-67 values) or REGRESSION (name the label and its value). Do not edit anything."""))

items.append(seat("R68CensusReplay", "executor", ["coverage", "freshness"], f"""Source-census replay.

Do: run `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger` and report the FULL output and the exit code. Then report the row count of {SOURCES} (`grep -cE '^\\| S[0-9]+ ' {SOURCES}`), the status of S046 and S045, and whether any row other than the new S046 changed against the committed round-67 bytes (`git -C {LANE} diff refs/heads/main~2 -- {SOURCES} | head -60`). Verdict: CLEAN (exit 0, only the disclosed W04 warnings plus an explained S046 W03) or DEFECT. Do not edit anything."""))

items.append(seat("R68FixtureHold", "reviewer", ["coverage", "freshness"], f"""Fixture and live byte hold.

Do: `git -C {LANE} diff --stat f165908aaffcf14798de53405fe788986bd33ff9 refs/heads/main -- corpus/live corpus/fixtures` and report the output (it must be EMPTY). Also report `git -C {LANE} diff --stat f165908aaffcf14798de53405fe788986bd33ff9 refs/heads/main -- corpus` and list every path that changed or was added, with a one-line reason each. Verdict: HOLD-INTACT (no live/fixture byte changed) or HOLD-BROKEN. Do not edit anything."""))

# ------------------------------------------------------- group E: claims and scope
items.append(seat("R68CriticClaimsC1", "critic", ["calibration"], f"""Attack C1's claim shape.

Do: read {CLAIMS} §C1 and {GATE}. Is the predicate falsifiable and correctly stated? Check: the mutant is exactly the frozen one; the attribution rule is "last output line ends with the marker"; the negative control is specified with its expected values (1/1 killed, 0/1 attributed); the kill rule has no clause that can be repaired after scoring; the do-nothing control genuinely cannot reach the target without changing the gate. Name any clause that is untestable, self-fulfilling, or that could be satisfied by editing the counter rather than the instrument. Verdict: NOT-FALSIFIED (the claim shape holds) or DEFECT (with the clause and the fix you would make). Do not edit anything."""))

items.append(seat("R68CriticClaimsC2", "critic", ["coverage"], f"""Attack C2's claim shape.

Do: read {CLAIMS} §C2 and {ENTRY}. Check: the target is one concrete value re-derivable with one command over committed bytes; the do-nothing control cannot reach 9/14 without the new entry AND an all-pass; the kill rule reserves the flip to an all-criteria pass and forbids re-targeting; no acceptance condition is repairable after scoring; the claim is separable from C1 (C1's counter labels must not be part of C2's predicate). Name any clause that is untestable or self-fulfilling. Verdict: NOT-FALSIFIED or DEFECT, with the clause. Do not edit anything."""))

items.append(seat("R68CriticSeparability", "critic", ["calibration", "coverage"], f"""Separability audit.

Do: check that C1 and C2 are causally separable — that each claim's counter labels move only when its own artifact moves. Reason from the counter {COUNTER} and the trees: C1's labels read {GATE} and the counter's own C7 labels; C2's labels read the README C05 row and the knowledge column. Does any C1 label depend on the v3 entry, or any C2 label on the gate's repair? (Note: `C7_V3_CLEAN` is claimed by BOTH — state whether that shared label breaks separability and how to read it.) Verdict: SEPARABLE / SEPARABLE-WITH-NAMED-SHARED-LABEL / NOT-SEPARABLE, with the reasoning. Do not edit anything."""))

items.append(seat("R68CriticEntryDeps", "critic", ["coverage", "depth"], f"""Silent-dependency audit of the v3 entry.

Do: read {ENTRY}. List every value the entry states and where each one comes from; then name any value whose source is NOT visible inside the entry (an undeclared dependency): a file it reads, a fact it assumes, a tool it needs, a hash it relies on. Pay attention to the new item 11 and to `corpus/snapshots/ResourceTypes.h`. For each candidate silent dependency, state whether the entry names it. Verdict: NO-SILENT-DEPS (or a list of the unnamed ones with entry lines). Do not edit anything."""))

items.append(seat("R68CriticEntryScope", "critic", ["coverage", "depth"], f"""Scope and limitation audit (Q10) of the v3 entry.

Do: read {ENTRY}, especially `## Limitations`, `## Cross-lane scope note (Q10)` and the `## Observation / inference / unknown` block. Check that no claim exceeds: one authored fixture, one manifest shape, UTF-8 string pool only, ZIP_STORED, a dex header only, manual standard-library analysis, no provider call. Name any sentence that generalises beyond that scope. Verdict: SCOPE-CLEAN or SCOPE-BLEED (with the sentence and the line). Do not edit anything."""))

items.append(seat("R68SentinelScope", "sentinel", ["coverage", "calibration"], f"""Containment and write-scope audit.

Do: check that this round's landed changes stay inside the lane repository and the declared write scope, and that no protected surface moved. Commands: `git -C {LANE} diff --name-status f165908aaffcf14798de53405fe788986bd33ff9 refs/heads/main`, `git -C {LANE} status --porcelain`, `git -C /home/vgpnk/Projects/shokunin status --porcelain | head -40` (the fleet root: report only; do NOT touch anything there), and `git -C /home/vgpnk/Projects/shokuknow status --porcelain | head -20` (READ-ONLY, never write there). Report: every changed path in the lane, whether any lane change touches corpus/live or corpus/fixtures, whether the fleet root and the campaign tree show any write attributable to this round, and whether any fleet-root file names revenger/round-68. Verdict: CONTAINED or LEAK (with the path). Do not edit anything."""))

items.append(seat("R68ConnectorOverlap", "connector", ["coverage", "adjacency"], f"""Sibling-overlap scan (adjacency).

Do: scan the sibling lane repos under /home/vgpnk/Projects/shokunin/ for work that overlaps revenger's round-68 claims — specifically: any sibling entry or report that also claims the AOSP AXML chunk-type anchors, the C7 embedded-output gate concept, or the Android APK container/dex declared-header ground. Look at the sibling `corpus/knowledge/` and `SCORECARD.md` files (read-only; do not edit any sibling repo). Report each overlap with the sibling path and whether it is CONTEST-NAMED (the sibling names revenger) or CONTEST-UNNAMED. State whether revenger's claims stay inside its own province. Verdict: CONTEST-NAMED / CONTEST-UNNAMED / NO-OVERLAP, with the pointers. Do not edit anything."""))

items.append(seat("R68RevengerLedger", "revenger", ["calibration"], f"""Adversarial ledger check on this round's own claims.

Do: read {CLAIMS} and the r67 closure {LANE}/corpus/lessons/round-67-verifier-spotcheck.md. Find any place where the r68 pre-registration repeats an r67 failure mode (a shadowed marker, an off-by-one anchor, a claim whose predicate is weaker than its prose, an assertion with no resolvable pointer). Also check that every number in {CLAIMS} §C1/§C2 matches the committed red-before receipt {BEFORE}. Report each finding with the exact line. Verdict: LEDGER-HOLDS or LEDGER-BROKEN (list them). Do not edit anything."""))

# ------------------------------------- group F: discernment, registry, r67 repairs
items.append(seat("R68SpotcheckDiscern", "scribe", ["coverage", "calibration"], f"""Outside-discernment spot-check (adjudication aid, not a verdict).

Do: re-open ONE source row this round claims and check the row's own anchor against the bytes it names, exactly as the r67 spot-check did for S055/S060. Use S046: open {DERIVE}, run it, and confirm the located quote recorded in {SOURCES} for S046 (`enum RES_XML_START_NAMESPACE_TYPE : 245`) is present in the script's actual output, and that the row's script sha256 and snapshot sha256 match the files on disk (`sha256sum {DERIVE} {SNAP_COPY}`). Then check ONE of the entry's tier-A claims: confirm from {SNAPSHOT} that the entry's `RES_XML_START_NAMESPACE_TYPE` anchor really is line 245 and that line 244 names a different constant. Report both checks with their actual outputs and an AGREE/DISAGREE verdict for each. Do not edit anything."""))

items.append(seat("R68ReviewSourcesS046", "reviewer", ["coverage", "calibration"], f"""Registry-row review for S046.

Do: read the S046 row in {SOURCES} and the surrounding registry contract in {SOURCES}'s header. Check: 11 columns, tier A justified for an own-work row, scope stated, anchor locatable, status/recheck/used-by values legal, no literal or escaped `|` inside a cell, and the row's used-by cell consistent with the entry's own state (the v3 entry is a CANDIDATE, not admitted — what does the cell currently say and is that honest?). Report each field with your verdict and the exact cell text. Verdict: ROW-CLEAN or ROW-DEFECT with the fixes you would make. Do not edit anything."""))

items.append(seat("R68ReviewSkillRegistry", "reviewer", ["calibration", "depth"], f"""Gate-registry row review (SKILL.md).

Do: read the `## Gate registry` section of {SKILL} and the gate itself {GATE}. Check the row against PROTOCOL §Gate standard as the lane's registry: name, kind (gate or probe) and whether the instrument now qualifies, entry command, verdict map (code -> class) with every nonzero code declared, self-test command and spelling, pinned-value path (does the pinned red snapshot still exist and still exit as the row claims? run it), measured-against (the counter), write scope, owner. Report every field with a verdict and the exact cell text; name any field that is stale after the round-68 repair. Verdict: ROW-CLEAN or ROW-DEFECT with the precise edits you would make. Do not edit anything."""))

items.append(seat("R68RepairD1", "critic", ["calibration"], f"""Routed defect D1 audit (round-67 closure item 1: attempt-1 abort evidence).

Do: read the D1 item in {LANE}/corpus/lessons/round-67-verifier-spotcheck.md (§7 item 1) and the round-67 wave evidence committed at {LANE}/.ufo/waves/round-67/ (dispatch-start-attempt1.txt, dispatch-run.log, dispatch-run-2.log). Decide: (1) what the COMMITTED bytes support about the attempt-1 abort (quote the timestamps and the exit lines), (2) whether the round-68 report's restatement is at exactly that strength, (3) what a non-author can still not verify from committed bytes (e.g. the per-seat stopReason transcripts, if they are not committed). Report the evidence lines and the precise wording a round-68 report may use. Verdict: RESTATEMENT-SOUND or OVERSTATED, with the sentence to use. Do not edit anything."""))

items.append(seat("R68RepairD2", "critic", ["calibration", "depth"], f"""Routed defect D2 audit (gate vs probe classification).

Do: read the D2 item in {LANE}/corpus/lessons/round-67-verifier-spotcheck.md (§7 item 2), the round-67 pre-registration {LANE}/reports/round-67/claims.md (its C2 registry sentence), the round-67 report {LANE}/../.ufo/reports/round-67/revenger.md if readable, and the `## Gate registry` row in {SKILL}. Decide which classification the authoritative registry carries and which the prose carries, state PROTOCOL's rule for gate vs probe in one sentence with its section name, and state whether the round-68 instrument still qualifies after the repair (it can now fail with an attributable marker — test that in a scratch copy). Report the exact conflicting sentences (file:line) and the reconciliation the round-68 report must make. Verdict: RECONCILE-AS-SPECIFIED or DEFECT. Do not edit anything."""))

items.append(seat("R68RepairD3", "scribe", ["coverage", "freshness"], f"""Routed defect D3 audit (S045 quote word count).

Do: read the D3 item in {LANE}/corpus/lessons/round-67-verifier-spotcheck.md (§7 item 3), then the S045 row in {SOURCES} and the round-67 lesson {LANE}/corpus/lessons/round-67.md (the S045 Gate block). Count the words of the located quote exactly (whitespace-separated tokens), both for the lesson's quoted string and for the row's own shorter variant. Report both counts, the strings you counted, and whether each is <= 25 words. Then state exactly what a correction must say (the count, and that both are conformant) and where it must land (an appended correction, never an in-place rewrite). Verdict: COUNT-CONFIRMED with the numbers, or DEVIATION. Do not edit anything."""))

items.append(seat("R68RepairD4", "critic", ["coverage", "calibration"], f"""Routed defect D4 audit (S045 `used-by` points at a rejected candidate).

Do: read the D4 item in {LANE}/corpus/lessons/round-67-verifier-spotcheck.md (§7 item 4) and the S045 row in {SOURCES}. Report the current `used-by` value and what it points at (the round-67 candidate carries `admission-status: rejected` — confirm by grepping the file). Then decide what the re-point must be in each possible adjudication outcome of C2: (a) C2 passes and the v3 entry is admitted; (b) C2 fails and the v3 entry is rejected. Give the exact cell value for each case and the rule that licenses the change (the registry contract's own rule on `used-by` changes). Verdict: RE-POINT-SPECIFIED with the two cases, or DEVIATION. Do not edit anything."""))

items.append(seat("R68ReviewSkillRefresh", "reviewer", ["depth", "operability"], f"""SHONEN box-1 refresh check.

Do: read {SKILL} end to end (it is the lane's decision tables, error patterns, checklists and cited sources) and judge whether box 1 ("SKILL.md contains real decision tables, error patterns, checklists, cited sources") is satisfied on the CURRENT bytes: are the tables decision-bearing (real thresholds/conditions), are the error patterns named with signatures, are the checklists executable commands, and does every cited source resolve (file exists / row exists in {SOURCES})? List every citation that does NOT resolve, with its line. Report your verdict as YES (box-1-ready) or NO (with the gaps). State explicitly that you are a lane-dispatched seat (not a non-author verifier) and that the box stays `[~]` unless a non-lane reviewer says otherwise. Do not edit anything."""))

# ------------------------------------- group G: per-item re-derivation (items 1-10)
ITEM_TASKS = [
    ("G1", "item 1 — the archive's byte count and SHA-256", "archive"),
    ("G2", "item 2 — the end-of-central-directory record", "eocd"),
    ("G3", "item 3 — the three central-directory members", "member"),
    ("G4", "item 4 — the AXML chunk table", "axml_chunk_table"),
    ("G5", "item 5 — the spec-derived struct widths", "spec_derived_struct_widths"),
    ("G6", "item 6 — the string pool", "axml_string_pool"),
    ("G7", "item 7 — the resource map", "axml_resource_map"),
    ("G8", "item 8 — the start-element chunk and its attributes", "axml_start_element"),
    ("G9", "item 9 — the dex declared header", "dex_declared_header"),
    ("G10", "item 10 — the text manifest", "jar_manifest"),
]
for gid, what, fact in ITEM_TASKS:
    items.append(seat(f"R68Item{gid[1:]}", "reviewer" if int(gid[1:]) % 2 else "executor",
                      ["coverage", "depth"], f"""Independent re-derivation of {what}.

Do: from {LANE}, run `python3 -B corpus/fixtures/apk-r65/readout.py --fact {fact}` (for the members, run it once per member: `member[AndroidManifest.xml]`, `member[classes.dex]`, `member[META-INF/MANIFEST.MF]`). Capture the actual stdout and exit code. Then open {ENTRY}, find the block that claims this fact, and compare EVERY field of your actual output with the embedded line: name each field that differs. Then judge the entry's prose sentence about this fact: does it state anything the output does not support? Report the command, the actual output, the entry's embedded line (with its entry line number), and a field-by-field verdict. Verdict: MATCH or MISMATCH (with the differing field and values). Do not edit anything."""))

# ------------------------------------- group H: residual, structural and provenance
items.append(seat("R68OracleCorrespondence", "reviewer", ["coverage", "depth"], f"""Oracle correspondence of the v3 entry.

Do: read {FIXTURE}/truth.json and the entry's `## Comparison with the authored oracle` section. Re-derive each shared field from the readout's actual stdout (run `python3 -B corpus/fixtures/apk-r65/readout.py` from {LANE} and use the full output) and compare it with the oracle's declared value: image digest and size, the three members' offsets/sizes/CRC-32, the nine strings, the three attribute rows, the two non-zero resource ids. Report each shared field, the oracle value, the readout value, and MATCH/MISMATCH. Then state whether the entry's oracle-comparison paragraph claims anything the two disagree on. Verdict: MATCH or MISMATCH. Do not edit anything."""))

items.append(seat("R68QmapSelfCheck", "critic", ["coverage", "depth"], f"""Q-map self-consistency of the v3 entry.

Do: read the entry's `## §Q-map` table and check it against the entry's own bytes: does each row's `basis` sentence point at something that is actually in the entry (a command, a line, a section)? Are the rows' verdicts consistent with the entry's content — in particular Q11 (does every count/identifier/digest carry its deriving command and output?) and Q02 (does the header carry source/verified-at/recheck and name the coverage row)? Are any rows marked `n/a` that should not be? Report each row: id, the basis sentence's pointer (entry line), and a verdict. Do not edit anything."""))

items.append(seat("R68HeaderCheck", "reviewer", ["coverage", "depth"], f"""Entry header check (Q02/Q11) of the v3 entry.

Do: read the entry's header block (the `source:`/`verified-at:`/`recheck:`/`coverage-map:`/`admission-status:` lines). For each of the five: state what it says and whether it is complete and honest on the CURRENT bytes. Specifically: does every `source:` row exist in {SOURCES} with the stated tier and scope; does the `recheck:` command exist and run; does the `verified-at:` date match the round this entry was written in; does the `admission-status:` line describe the entry's true state (it is a CANDIDATE, the README C05 row is still `uncovered`). Report each line with its entry line number and a verdict. Do not edit anything."""))

items.append(seat("R68ReadmeFlipCheck", "executor", ["coverage"], f"""README C05 row and the flip precondition.

Do: read the C05 row of {README} and report its exact text and its status cell. Then check the claim's own precondition list from {CLAIMS} §C2 and report, for each item, whether it holds on the current bytes: K_HELD_BACKED, K_HELD_BACKED_STRICT, the C05 status, C05_SINGLE_V3, README_TOKEN_LEGEND_MISMATCH, HOLDS_C2_V3, C7_V3_CLEAN, the wave's Q-decisions, the spot-check. Run the counter {COUNTER} over a scratch tree from `git -C {LANE} archive refs/heads/main corpus | tar -x -C <tree>` and quote the labels. Report which preconditions are met and which are NOT met right now, and what the README row must read if (and only if) all of them hold. Verdict: FLIP-PRECONDITIONS-MET / NOT-MET (list the unmet ones). Do not edit anything."""))

items.append(seat("R68CorpusPathHygiene", "executor", ["coverage", "operability"], f"""Corpus path hygiene for the new snapshot copy.

Do: report `git -C {LANE} ls-files corpus/ | sort` and identify every path this round added. Check: is `corpus/snapshots/ResourceTypes.h` tracked; does `git -C {LANE} check-ignore -v corpus/snapshots/ResourceTypes.h` ignore it; is its size inside the 1 MiB directory-commit rule; does the lane's own `corpus/README.md` index need to mention the new path (quote the index's `knowledge/` and `fixtures/` bullets); does `corpus/QUALITY.md` or `PROVINCE.md` constrain what may live under `corpus/` (quote the relevant sentences). Report each finding. Verdict: HYGIENE-CLEAN or DEFECT with the exact fix. Do not edit anything."""))

items.append(seat("R68WaveContractAudit", "sentinel", ["coverage", "calibration"], f"""Wave-contract audit.

Do: read {CLAIMS} §"Wave contract" and this wave's registry (the file {LANE}/.ufo/waves/round-68/swarm-registry.json if present, else the spec {LANE}/.ufo/waves/round-68/wave-spec.json). Check: exactly 64 seats, one batched dispatch call, >= 25% attack roles (count the roles reviewer/critic/mutation-tester/sentinel/revenger), every seat's item is a distinct concrete work item serving C1, C2, the frontier step or the r67 repairs (name any seat whose item is padding), the role mix covers the required minimum (a connector, executors, a scribe, a scout, reviewers, critics), and the §3 planner seat is held by the L1 because the validator rejects `planner` (check the validator's own message by running `node ~/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs plan --spec {LANE}/.ufo/waves/round-68/wave-spec.json` and quoting what it prints about planner). Report the counts, the attack-role percentage, and any padding seat. Verdict: CONTRACT-OK or CONTRACT-BROKEN. Do not edit anything."""))

items.append(seat("R68DeriveCritic", "critic", ["coverage", "depth"], f"""Attack the derivation script's failure behaviour.

Do: read {DERIVE}. In scratch copies only, corrupt the input in three ways and report the script's exit code and output for each: (1) truncate the snapshot copy; (2) change the snapshot's bytes so the digest differs; (3) make one cited symbol appear TWICE in the file (so the search is ambiguous). Report what the script does in each case and whether it refuses to print a line it did not find. Then state whether a corrupted corpus/snapshots copy could silently make the v3 entry's anchors wrong while the gate still passes (i.e. does the gate check the anchors, or only that the script's output is reproducible?). Verdict: FAILS-CLOSED or FAILS-OPEN, with the evidence. Do not edit the lane tree."""))

items.append(seat("R68LessonCheck", "scribe", ["coverage", "calibration"], f"""Lesson and mistake-class check for round 68.

Do: read {LANE}/corpus/lessons/round-67.md `## Mistakes` and the M40/M44/M45 entries, and {CLAIMS}. The round must mine one mistake into `corpus/lessons/round-68.md` `## Mistakes` with class, evidence pointer, captured-by (the criterion or rule that should have caught it) and fix, and a fix only counts once shown able to fail. State which mistake class round 68 should mine and what evidence pointer the lesson must carry (name the committed artifact that proves the fix can fail — e.g. the negative-spoof control). Also check that the round-67 lesson's S045 word count (18 vs 19) is still uncorrected in the committed bytes, and state exactly where the correction must land. Verdict: REQUIREMENTS-STATE with the two answers. Do not edit anything."""))

# ------------------------------------------------------------------- assemble
spec = {
    "wave": "revenger-r68-v2",
    "milestone": "C1 C7 attribution repair + C2 C05 v3 candidate with machine-derived anchors landed as build state; README not flipped; wave supplies Q01-Q13 decisions, C7 mutant/spoof attacks, anchor re-derivations, counter/census replays, r67 repairs",
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
print(f"seats={len(items)} roles={roles} attack={attack} ({100 * attack / len(items):.1f}%)")
WAVE_DIR.mkdir(parents=True, exist_ok=True)
out = WAVE_DIR / "wave-spec.json"
out.write_text(json.dumps(spec, indent=1), encoding="utf-8")
print(f"written: {out}")
