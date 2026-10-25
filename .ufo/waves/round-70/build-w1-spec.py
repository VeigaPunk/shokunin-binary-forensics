#!/usr/bin/env python3
"""Round-70 wave-1 (build / pre-gate) spec generator (revenger L1, hyaku run 7).

Renders `.ufo/waves/round-70/w1-spec.json`: one v1 wave (policy band 32-64) of build and
pre-gate items serving the three frozen claims (reports/round-70/claims.md) plus the
frontier step. The godspeed directive bytes are lifted byte-exact from the committed
round-68 wave spec (item 0), never paraphrased. Run from the lane root:

    python3 -B .ufo/waves/round-70/build-w1-spec.py
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
WAVE_DIR = ROOT / ".ufo/waves/round-70"
R68_SPEC = ROOT / ".ufo/waves/round-68/wave-spec.json"

LANE = "/home/vgpnk/Projects/shokunin/revenger-shokunin"
CAND = "aa1842fac199aa524930e5565ed3715de5f84c6d"
BASE = "3f5edbc206351232a3d2d801334dd930499ccaf5"
PREREG = "dbacce212d798d1ec5bb59e03ff91d577eed0283"
ENTRY = f"{LANE}/corpus/knowledge/round-70-apk-axml-byte-evidence.md"
CLAIMS = f"{LANE}/reports/round-70/claims.md"
COUNTER = f"{LANE}/reports/round-70/measure.py"
QUALITY = f"{LANE}/corpus/QUALITY.md"
SOURCES = f"{LANE}/corpus/SOURCES.md"
GATE = f"{LANE}/corpus/check_embedded_outputs.py"
LINT = f"{LANE}/corpus/lint_entry.py"
SELFCHK = f"{LANE}/corpus/self_assessment_check.py"
ECHK = f"{LANE}/corpus/fixtures/apk-r65/entry_checks.py"
READOUT = f"{LANE}/corpus/fixtures/apk-r65/readout.py"
FIXDIR = f"{LANE}/corpus/fixtures/apk-r65"
PINS = f"{LANE}/corpus/embedded_output_pins.json"
REPORT_DIR = ".ufo/waves/round-70/w1"


def godspeed_prefix():
    spec = json.loads(R68_SPEC.read_text(encoding="utf-8"))
    prompt = spec["items"][0]["prompt"]
    marker = "Act directly via tool calls."
    return prompt[:prompt.index(marker) + len(marker)]


GODSPEED = godspeed_prefix()

CONTEXT = f"""# Goal
Revenger round 70 (hyaku run 7), WAVE 1 of 2 (build / pre-gate). Lane repo: {LANE} — use ABSOLUTE paths in every read and write (your tools start at the fleet root /home/vgpnk/Projects/shokunin; a relative path lands in the FLEET repo).

# Frozen contract (read first — it overrides any summary here)
{CLAIMS} — three declared claims (C1 coverage: C05 fifth pass, v5 candidate; C2 calibration: SELF_MISMATCH 9 -> 0 with a checker that is shown able to fail; C3 freshness: retained entry re-derives against a digest-pinned historical script), frozen predicates, kill rules, controls, landing order.
{COUNTER} — the frozen round-70 counter (sha256 488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76). Pre-registration commit {PREREG}; claim base {BASE}; the C05 v5 candidate under attack is lane commit {CAND} (file {ENTRY}, `admission-status: candidate`, README C05 row still `uncovered`).
Wave-1 findings are ADVISORY and drive repairs before the candidate is declared final; they are not kill-rule inputs. Wave 2 (fresh seats) gates the final bytes. Attack the bytes, not the author: a finding without a located defect (path:line + the command output that shows it) is not a finding.

# Stable targets
The working tree may gain README/SHONEN/SCORECARD/SOURCES edits while you run. For any file you judge as a TARGET read it with `git -C {LANE} show {CAND}:<repo-relative path>` (or from a `git archive {CAND}` extraction in your scratch); for a BASE comparison use `git -C {LANE} show {BASE}:<path>`. The entry, the readout, entry_checks.py, the gate, the lint and the checker will NOT change during this wave.

# Report paths (IMPORTANT)
Every `Report:` trailer in your prompt is RELATIVE to {LANE} — write your report at {LANE}/<that path> (a `.ufo/waves/round-70/w1/<Name>.md` trailer means {LANE}/.ufo/waves/round-70/w1/<Name>.md). Never write to the fleet root.

# Write scope
- You may write ONLY your own report file under {LANE}/.ufo/waves/round-70/w1/ and scratch files under /tmp/revenger-r70-<your seat name>* (delete your /tmp scratch before returning).
- NEVER write, edit, commit or push inside: the fleet repo /home/vgpnk/Projects/shokunin, any sibling lane repo, {LANE}'s own corpus/, reports/, SKILL.md, SHONEN.md, SCORECARD.md or LOG.md (read-only for seats), or /home/vgpnk/Projects/shokuknow (READ-ONLY campaign tree — read and fetch only; never run a campaign tool there).
- NEVER run a mutating git or jj command in the lane or the fleet (no add/commit/stash/checkout/reset/pull/push/jj new/describe/squash/rebase/bookmark). Read-only git/grep/read is fine. A check that needs git writes runs on a sandbox repo created as `D=$(mktemp -d /tmp/revenger-r70-XXXX) && git -C "$D" init -q` with EVERY later git call naming `-C "$D"`; verify `git -C "$D" rev-parse --show-toplevel` equals `$D` before the first commit; never use a throwaway identity anywhere else.
- All pacman transactions are PAUSED host-wide: do not install or update any package; use an existing binary or Python stdlib.
- A mutation or tamper test edits a COPY in your scratch (`cp -r` the files you attack), never the lane file.

# Tooling authorization (operator, 2026-10-19)
You and every seat may install or upgrade tools that help the task — read /home/vgpnk/.omp/agent/RULES.md first (official channels, update-safety gate, record tool/version/channel/reason in the report). pacman guard: all pacman transactions are PAUSED host-wide — install via `uv tool`/`npx`/an official binary in `~/.local/bin`, or file an L0 question; never `-Sy`/`-Syu`/`-U`/`-R`/downgrade/restart a host service.

# Seat discipline
You are an independent leaf: never block on or wait for another seat; never spawn subagents (the one executor-to-labrat exception is not used this wave); never message agent://all; if a needed artifact is absent, record the dependency as a finding and return. Time-box: return within 12 minutes with your best findings + evidence; partial results are acceptable. Put your verdict on the FIRST line of your report (PASS / FAIL / NOT-FALSIFIED / ADMIT / REJECT / CLEAN / HOLDS / FALSIFIED / CONCUR / DIVERGE / DRAFT-READY + one-line reason), then evidence: commands with their actual output, file:line pointers, sha256 where relevant. Ground every claim in a resolvable pointer; a claim without one is not evidence."""


def seat(name, role, axes, task):
    return {"name": name, "role": role, "axes": axes, "prompt": GODSPEED + "\n\n" + task}


items = []

# ------------------------------------------------------------------ C1 pre-gate
PRE = f"""You are a PRE-GATE reviewer of the C05 v5 candidate {ENTRY} (lane commit {CAND}). Read {CLAIMS} §C1 first, then {QUALITY} (criteria Q01-Q15), then the entry. Your findings drive repairs before the candidate is declared final; a defect you locate and the exact corrected text you propose is the most useful output.

Your scope: {{scope}}

Do: read the entry bytes; re-run the entry's own commands yourself from {LANE} (`cd {LANE} && python3 -B <script> ...`) and compare actual stdout with the embedded lines; decide PASS / FAIL / n/a per criterion in your scope on these bytes. For a FAIL name the exact entry line(s), the wrong value, the command output that shows it, and the corrected sentence. For PASS name the command or line that proves it and quote the observed output. Never accept the entry's own §Q-map row as evidence. Do not edit any file."""

pre = [
    ("R70W1PreQ01Q02", "reviewer", "Q01 (every load-bearing claim rests on a tier-A SOURCES row for its scope; verify S032/S034/S038/S041/S043/S045/S047 exist in {S} with the tiers, scopes and opened dates the entry's `source:` lines state — S043 is `queued` and S045 opened 2026-10-24) and Q02 (provenance trio + coverage-map; every `source:` row resolves, anchors are not bare homepages, recheck commands exist and run)".replace("{S}", SOURCES)),
    ("R70W1PreQ03Q06", "critic", "Q03 (expected values derived independently — from bytes, a spec, or a pin fixed outside the record under test; is the truth.json oracle independent of readout.py? read generator.py) and Q06 (fixture premises byte-verified: do the digests in item 14 match the files; does the entry say honestly that generator.py is not re-run?)"),
    ("R70W1PreQ04Q13", "reviewer", "Q04 (a tool claim names tool, version, function and scores the tool's own output; manual analysis labeled manual — check items 3, 5, 12) and Q13 (a verifier/recheck command credited only for clauses whose deletion its own run is shown to detect — the embedded-output gate credit and the MATCH/MISMATCH credit; try deleting a clause and see what notices)"),
    ("R70W1PreQ05Q07", "critic", "Q05 (a readiness/capability claim carries a probe against the real surface — find ANY sentence that implies a refusal path, exit status, provider readiness or capability not probed in the entry) and Q07 (a predicted parser behavior is a pre-registered hypothesis — find ANY sentence describing what a parser does rather than what this readout printed; item 8's namespace sentence and the inference list are the prime suspects)"),
    ("R70W1PreQ11Items1to8", "critic", "Q11 over the header, items 1-8 and the Observation/inference text: every count, identifier, offset and digest must carry the command that derives it from the primary record, with its output in the entry; a value in prose that no embedded command prints is a FAIL. Build a table of EVERY number/hex/identifier in those regions, with the command output line that prints it (or FAIL)"),
    ("R70W1PreQ11Items9to15", "critic", "Q11 over items 9-15, the Limitations, the Cross-lane note, the §Q-map and the Reproduce section: every count, identifier, offset and digest must carry the command that derives it, with its output in the entry. Build a table of EVERY number/hex/identifier in those regions, with the command output line that prints it (or FAIL). Also check each `readout.py:N` / snapshot-line citation resolves to what the sentence says (cat -n the file)"),
    ("R70W1PreQ09Q10Q12", "critic", f"Q09 (a digest is claimed only for the exact bytes it hashed; no origin/completeness/authenticity claim), Q10 (finding scoped to the observed family/operation/version/input; cross-lane contested scope reported, not absorbed; read {LANE}/PROVINCE.md) and Q12 (n/a unless a rejected-sources row is written — confirm none is)"),
    ("R70W1PreQ14Q15", "reviewer", f"Q14 (a hex string quoted with a byte count in the same clause carries 2xN hex chars; an ellipsis-truncated run carries no length; an ASCII rendering decodes from that same run — sweep EVERY clause of the whole file including header lines and the §Q-map) and Q15 (a stated git object id or tree identity is re-derived with the command that names it — find any git-looking token; run {LINT} --entry on the file and judge what it can and cannot see)"),
]
for name, role, scope in pre:
    items.append(seat(name, role, ["coverage", "calibration", "depth"], PRE.format(scope=scope)))

items.append(seat("R70W1Prose", "critic", ["coverage", "depth"], f"""Overreach sweep of the C05 v5 candidate {ENTRY} (commit {CAND}).

Do: read the entry sentence by sentence. For each sentence that asserts something, classify it OBSERVED (a command output in the entry prints it), RECORDED (labeled transcription), INFERRED (labeled inference) or UNSUPPORTED. List every UNSUPPORTED or mislabeled sentence with its entry line and a corrected sentence. Pay special attention to: item 4 (chunk `type` to enum-name correspondence), item 8 ('does not consult'), item 9, the Limitations paragraph, and any word like 'every', 'all', 'complete', 'verified'. Verdict CLEAN or the list. Do not edit any file."""))
items.append(seat("R70W1Citations", "executor", ["operability", "depth"], f"""Citation resolver for the C05 v5 candidate {ENTRY}.

Do: extract EVERY `file:line`, `readout.py:N`, `lines N-M`, 'snapshot lines N-M' and 'first line N' citation in the entry (header lines, items, Q-map). For each, open the cited file at the cited line(s) ({READOUT} with `cat -n`; {LANE}/corpus/snapshots/APPNOTE.TXT; dex-format.html; ResourceTypes.h; rea-android-applications.md) and state whether the sentence's claim about that line is TRUE as written. Output a table: entry line | citation | what the file says there | TRUE/FALSE. Verdict ALL-RESOLVE or FAIL (list). Do not edit any file."""))
items.append(seat("R70W1GeneratorRerun", "executor", ["operability", "depth"], f"""Fixture premise (Q06): regenerate and compare.

Do: copy {FIXDIR}/generator.py to a scratch dir /tmp/revenger-r70-gen/, read it first to see what it writes and where, run it ONLY in the scratch dir (never in the lane), then byte-compare the regenerated fixture.apk with {FIXDIR}/fixture.apk (`cmp`, sha256) and compare the regenerated truth.json with {FIXDIR}/truth.json. The recorded build recipe says Python 3.14.8 and determinism; report the host `python3 --version`, the observed digests and whether the bytes are identical. Verdict IDENTICAL, DIFFERS (say where) or CANNOT-RUN. Do not edit any lane file."""))
items.append(seat("R70W1GateMutants", "mutation-tester", ["calibration", "operability"], f"""Mutate the entry, then see whether the gate notices (Q13 / M39 class).

Do: copy the lane's corpus/ at commit {CAND} into a scratch tree (`git -C {LANE} archive {CAND} corpus | tar -x -C <scratch>`). Apply EACH of these mutants to a fresh copy of {ENTRY} inside the scratch tree and run `python3 -B corpus/check_embedded_outputs.py --entry <mutated>` from the scratch root: (1) change one digit in one embedded JSON line; (2) delete one embedded line; (3) swap two hex characters in a `payload_first16_hex` value; (4) alter one `MATCH` line of the --zip-layout block to `MISMATCH`; (5) replace one `$ python3 -B ...` command's flag with a nonexistent flag; (6) append an extra output line not printed by its command. Report each mutant, the exit code and the last output lines. Verdict ALL-KILLED or SURVIVORS (list which survived and what clause it left unguarded). Do not edit any lane file."""))
items.append(seat("R70W1LintMutants", "mutation-tester", ["calibration", "operability"], f"""Attack the lint {LINT} (it is a pre-flight, not a gate — find what it cannot see).

Do: first run `python3 -B {LINT} --self-test`. Then, on scratch copies, (a) write a Q14-violating sentence of the HISTORICAL classes (e.g. a 9-byte hex run called a '16-byte prefix'; an ellipsis-truncated run with a count; an ASCII rendering that does not decode from its run) and report which ones the lint flags; (b) write a §Q-map missing 7 criteria and one with a blank decision; (c) cite a non-resolving commit after the words commit/base/tip/since/at and one after a word the lint does not know. Report each probe, the lint's output and exit code. Verdict LINT-SOUND-WITHIN-STATED-SCOPE or GAPS (list each class it misses and the sentence that slips through). Do not edit any lane file."""))
items.append(seat("R70W1EntryChecksMut", "mutation-tester", ["calibration", "operability"], f"""Mutate {ECHK} and see whether each subcommand can fail.

Do: copy {FIXDIR} (whole dir) and the corpus/snapshots files it reads into a scratch tree that keeps the same relative layout (`corpus/fixtures/apk-r65/`, `corpus/snapshots/`, `corpus/derive_axml_anchors.py`). On copies: (1) change one width in LOCAL_HEADER; (2) change a literal in the scratch readout.py (`eocd + 12` -> `eocd + 13`); (3) flip one byte of the scratch fixture.apk; (4) edit one quoted phrase in the scratch dex-format.html; (5) edit one truth.json value. For each, run the affected subcommand and report whether it printed MISMATCH and exited 1 (or otherwise changed). Verdict EACH-SUBCOMMAND-CAN-FAIL or SURVIVORS (list). Do not edit any lane file."""))
items.append(seat("R70W1Simplify", "simplifier", ["depth", "operability"], f"""YAGNI pass on the C05 v5 candidate {ENTRY}. Identify any block, sentence or header clause that can be deleted without losing a claim the entry needs for C05 coverage — each deletion removes attack surface (every prior pass failed on prose, not on bytes). Give exact line ranges and the reason each is safe to drop (what other line still carries the claim). Do not delete anything; do not propose new claims. Verdict: a numbered deletion list or NOTHING-TO-DROP."""))
items.append(seat("R70W1Sentinel", "sentinel", ["adjacency", "operability"], f"""Scope and safety review of the round-70 changes at commit {CAND} (diff {BASE}..{CAND} and the pre-registration commit {PREREG}).

Do: `git -C {LANE} diff --stat {BASE} {CAND}`; confirm every changed path is inside {LANE}; confirm {ECHK}, {GATE}, {LINT}, {SELFCHK} and the counter write nothing outside their own temp dirs, execute no fixture bytes, use no network at recheck time and take no path from input that escapes the tree (look at the pin rule's `use` path in {GATE}: can an entry name or a pins.json value reach outside the corpus?); confirm PROVINCE.md refusals (live-target execution, DRM, publishing reversed code) are untouched and the entry makes no cross-lane absorption (ADJ-06). Verdict CONTAINED or FINDINGS (list with path:line). Do not edit any file."""))

# --------------------------------------------------------------------------- C2
items.append(seat("R70W1ReadmeIndex", "executor", ["calibration", "coverage"], f"""C2 repair draft: README index (SM1, SM2). Target {LANE}/corpus/README.md as at {BASE}.

Do: run `python3 -B {SELFCHK} --root <archive of {BASE}: corpus SHONEN.md SCORECARD.md SKILL.md> --lane {LANE}` to reproduce SM1=1 and SM2=4. Then write the EXACT replacement/added README index lines (unified-diff style, lines 7-17 of README.md) that make SM1 and SM2 zero for THESE files only: the Q01-Q15 range, q15_tree_id_check.py, derive_axml_anchors.py, check_embedded_outputs.py, snapshots/ — and, as separate clearly labeled hunks (C1 owns lint_entry.py and entry_checks.py; C3 owns derive_axml_anchors_r68.py and embedded_output_pins.json; C2 owns self_assessment_check.py). Prove the draft by applying it to an archive COPY in scratch and re-running the checker (paste the output). Verdict DRAFT-READY with the diff in the report, or the reason it cannot be made. Do not edit any lane file."""))
items.append(seat("R70W1ShonenDraft", "scribe", ["calibration"], f"""C2 repair draft: SHONEN.md (SM3, SM4). Target {LANE}/SHONEN.md as at {BASE}; read it, {LANE}/corpus/lessons/round-69-verifier-spotcheck.md §6 V7 and {LANE}/corpus/lessons/round-69.md.

Do: audit all FOUR boxes against observed repo state (names a verifier? is the verifier a lane seat? do quoted digests/sizes match current bytes? does each pointer resolve?). Then write the exact replacement text of box 1 that is honest: `[~]` (the named verifier `revenger-r64.R64ReviewSkill` is a lane-dispatched seat, i.e. lane attestation), NO quoted byte count or digest for SKILL.md (so it cannot drift; point instead at `git -C <lane> show <commit>:SKILL.md` with the commit for the r64 bytes), and the routed need: a non-lane reviewer re-confirming the CURRENT bytes. Keep boxes 2-4 unless the audit finds a mismatch (then give exact text). The box COUNT must stay 4. Verify your draft by running {SELFCHK} against a scratch copy with your text applied (paste the output: SM3=0, SM4=0). Verdict DRAFT-READY. Do not edit any lane file."""))
items.append(seat("R70W1ErratumDraft", "scribe", ["calibration"], f"""C2 repair draft: SCORECARD errata (SM5) and the claim hit-rate ledger (considerthese 2026-10-24 proposal 3).

Do: (1) reproduce SM5=1 (which token, which SCORECARD line) with {SELFCHK}; find the correct full hash with `git -C {LANE} rev-parse` and write the appended erratum line in the exact form the checker reads: erratum: `bad` -> `good` (backticked 7-40 hex each; the line starts at column 0). (2) Draft the round-69 spot-check V3 and V4 corrections as appended prose (V3 wrong C1 table cell; V4 counting command as absolute path) — as text only. (3) Build the claim hit-rate ledger for lane rounds 61-69: one row per pre-registered claim (round, claim id, axis, verdict) derived by COMMAND from `{LANE}/SCORECARD.md` and `{LANE}/reports/round-6*/claims.md` — paste the command and its output, and a totals line (met / falsified / pending / honest-stop) with its counting command. If a verdict cannot be derived by command, mark it `recorded` with the line it was read from. Verdict DRAFT-READY with the ledger table in the report. Do not edit any lane file."""))
items.append(seat("R70W1SM5Sweep", "scout", ["calibration", "freshness"], f"""Find self-assessment mismatches the six SM classes do NOT count (named-unmeasured).

Do: sweep {LANE}/SCORECARD.md (sections Round 61 and later), {LANE}/SHONEN.md, {LANE}/corpus/README.md and {LANE}/LOG.md tail for statements that disagree with observed repo state by a command you run: commit hashes that do not resolve (`git -C {LANE} cat-file -e <h>^{{commit}}`), file paths that do not exist at the tip, counts that re-derive differently (K rows, source rows `grep -cE '^\\| S[0-9]+ ' corpus/SOURCES.md`, files in a directory), `[x]` boxes without a non-author verifier. For each candidate give file:line, the claim, the command and its output. Distinguish a TRUE MISMATCH from a false positive (a sha256 prefix is not a commit). Verdict: N true mismatches outside SM1-SM6 (list). Do not edit any file."""))
items.append(seat("R70W1ClassAttack", "critic", ["calibration"], f"""Attack the six mismatch classes of {SELFCHK} (read its docstring and code).

Do: for each of SM1..SM6 try to construct (a) a real mismatch the class would MISS and (b) a correct state the class would FLAG (false positive), on the real lane files at {BASE} and on scratch edits of them. Examples to try: SM2 with a hidden/underscore dir, a `.py` named only inside a longer name, `verify_*.py` glob abuse; SM3 with a box naming two files or a digest on a non-file; SM4 verifier named by a different pattern; SM5 with a hash after the word 'tip' inside a code span, a 40-hex sha256-looking token, an `erratum:` line whose good value resolves but is a different commit than the bad one intends; SM6 with two K statements on one line. Report each probe, command and output. Verdict CLASSES-SOUND or GAPS (list each, with a proposed one-line tightening that keeps the frozen predicate). Do not edit any lane file."""))
items.append(seat("R70W1SelfMut", "mutation-tester", ["calibration", "operability"], f"""Mutate {SELFCHK} and check the counter's fixtures kill each class (the checker must be shown able to fail).

Do: in a scratch copy, for each class SM1..SM6 neutralize that class's function (make it `return 0`) and then run the frozen counter {COUNTER} on a scratch tree built as `git archive {CAND} corpus SHONEN.md SCORECARD.md SKILL.md` with the mutated checker overlaid. Report, per mutant, the printed `SELF_MUTANTS_KILLED` and whether the counter attributes the loss to that class. Also neutralize the clean-fixture path (make the checker always print 1). Verdict ALL-SIX-KILLED or SURVIVORS (list). Do not edit any lane file."""))
items.append(seat("R70W1CounterReplay", "executor", ["calibration", "operability"], f"""Replay the frozen counter {COUNTER}.

Do: build two scratch trees with `git -C {LANE} archive <commit> corpus SHONEN.md SCORECARD.md SKILL.md | tar -x -C <dir>` for commits {BASE} and {CAND}; run the counter by absolute path on each, twice each (determinism: diff the two outputs); record every label and the exit code. Then probe the exit contract: (1) run it on a tree with `corpus/README.md` deleted (must be exit 2 with COUNTER_ERROR, never 1); (2) on a tree whose `corpus/check_embedded_outputs.py` is replaced by `raise SystemExit(3)` (report the labels). Compare the base-tree output with {LANE}/reports/round-70/measure-before.log (line for line, minus the HOLD verify lines). Verdict REPLAYS-AS-COMMITTED or DEVIATION. Do not edit any lane file."""))
items.append(seat("R70W1ControlAudit", "critic", ["calibration"], f"""Attack the do-nothing controls (prompt section 9: a target a do-nothing control can reach is a wrong target).

Do: read {CLAIMS} and the eight receipts in {LANE}/reports/round-70/controls/ and the builder {LANE}/reports/round-70/build-controls.py. For each of C1, C2 and C3 find the CHEAPEST move that skips the claimed work and still makes the claim's mechanical predicate print `yes` (try: README flip + a minimal entry whose blocks echo nothing; a SHONEN box rewritten to quote no digest AND a checker with SM3/SM4 removed but fixture stubs preserved; a pins.json entry mapping r68's command to a script that prints the 17 lines). Build each on a scratch archive of {BASE} and run the counter. Report which reach the target. Verdict TARGETS-UNREACHABLE or REACHED (list the exact control and counter output). Do not edit any lane file."""))

# --------------------------------------------------------------------------- C3
items.append(seat("R70W1PinMut", "mutation-tester", ["freshness", "calibration"], f"""Attack the digest-pin rule in {GATE} (`load_pins`, `apply_pin`) and {PINS}.

Do: on a scratch copy of corpus/ at {CAND}: (1) tamper one byte of corpus/derive_axml_anchors_r68.py -> the gate on the r68 entry must exit 1 with the text `pinned historical script digest mismatch`; (2) change the pin's `use` to `../README.md`, an absolute path and a symlink — what happens; (3) add a pins.json key for the r67 entry mapping to the extended script; (4) pin a script argument written differently (`./corpus/derive_axml_anchors.py`); (5) delete pins.json. Report each probe, exit code and output; say which are protected by the digest and which are only protected by convention. Verdict PIN-SOUND or HOLES (list with a proposed minimal tightening that keeps the registered comparison line byte-identical). Do not edit any lane file."""))
items.append(seat("R70W1PinCritic", "critic", ["freshness"], f"""Can the pin rule HIDE real drift? Attack claim C3 ({CLAIMS} §C3).

Do: confirm by command that `git -C {LANE} show {BASE}:corpus/derive_axml_anchors.py | sha256sum` equals the digest in {PINS} and in {LANE}/corpus/SOURCES.md row S046; run the gate on the r65, r67, r68, r69 entries at {CAND} and record (checked_blocks, problems). Argue whether reading the r68 entry against an OLDER script is honest (the entry's own text names the script it ran) or a way to pass a gate; state exactly what a reader may and may not conclude from `EMB_R68 problems=0`. Verdict HONEST-SCOPED or GAMEABLE (say how). Do not edit any lane file."""))
items.append(seat("R70W1FreshSweep", "executor", ["freshness", "coverage"], f"""Gate every knowledge entry that carries `$` command blocks.

Do: for every file under {LANE}/corpus/knowledge/*.md at commit {CAND} run `python3 -B corpus/check_embedded_outputs.py --entry <file>` from a `git archive {CAND} corpus` scratch root; record exit code and `checked_blocks`/`problems` (exit 2 = no `$` blocks). Also list which entries the pin file names. Verdict: a table entry | checked | problems | exit | pinned?; flag any entry other than r65 whose drift is unexplained. Do not edit any lane file."""))
items.append(seat("R70W1RegistryDraft", "scribe", ["operability", "calibration"], f"""Draft the registry text for the new instruments. Read {LANE}/SKILL.md `## Gate registry` (line ~272) and the existing rows for check_embedded_outputs.py and q15_tree_id_check.py.

Do: write the exact new registry rows (same columns and style) for corpus/self_assessment_check.py (kind gate, owner revenger, self-test command, what a red run means), corpus/lint_entry.py (kind pre-flight, NOT a gate: say what it cannot see), and the amended check_embedded_outputs.py row (pin rule, new self-test leg, attributed marker `pinned historical script digest mismatch`). Also draft the one-line additions for SKILL.md §4 SOURCES-census/Frozen-counter notes ONLY if they exist today and would otherwise be stale. Verdict DRAFT-READY with the exact text and insertion line numbers. Do not edit any lane file."""))

# ------------------------------------------------------------------ frontier step
for sid, what in (("S038", "S038 (AOSP ResourceTypes.h at tag android-15.0.0_r1, googlesource URL in the registry row)"),
                  ("S043", "S043 (REA reverse-engineer-anything skill reference 'Android application artifacts'; find the registry row URL and the pinned tag rea-agents-6.5.0)"),
                  ("S045", "S045 (https://source.android.com/docs/core/runtime/dex-format)"),
                  ("S032", "S032/S034 (https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT)")):
    items.append(seat(f"R70W1Open{sid}", "scout", ["freshness", "coverage"], f"""Re-open source {what} for the round-70 Gate block (CORPUS.md rule 1: the lesson records URL, access date, and a <=25-word located quote; non-author verification re-opens a sample).

Do: read the registry row in {SOURCES} first. Fetch the live source TODAY (2026-10-25; curl or the read tool), record the fetch time and sha256 of what you got, and compare with the lane's committed snapshot ({LANE}/corpus/snapshots/ — ResourceTypes.h, rea-android-applications.md, dex-format.html, APPNOTE.TXT). Report: byte-identical / differs (say how: whitespace, version, content) / unreachable (exact error). Locate and quote (<=25 words, with the line or heading it sits under) the sentence the C05 entry relies on: the quoted phrases in the entry's items 11-12 ({ENTRY}). A quote you cannot locate at the live source is a finding, not a pass. Verdict OPENED-QUOTE-PRESENT, OPENED-QUOTE-ABSENT (list), DIFFERS or UNREACHABLE. Do not edit any file."""))

items.append(seat("R70W1AssimUnblob", "scout", ["coverage", "freshness"], f"""Assimilation re-grounding (addendum section 10): package entry `digest-scope-versus-provenance-amendment-2026-10-23.md` (READ-ONLY at /home/vgpnk/Projects/shokuknow/merge/revenger/knowledge/corpus/knowledge/ and its rows in /home/vgpnk/Projects/shokuknow/merge/revenger/SOURCES.append.md; S099 unblob README). Never write there and never run a campaign tool there.

Do: for each of the entry's claims 3-5 (Unblob upstream: '78+ supported formats', the Python/uv/Rust requirement line, the install dependency line and `unblob --show-external-dependencies`) open https://raw.githubusercontent.com/onekey-sec/unblob/main/README.md YOURSELF today, record the fetch date and sha256, and locate each quote verbatim (<=25 words per quote, with the heading it sits under). Report each claim PRESENT / ABSENT / PARAPHRASE, and whether any sentence overreaches its source (e.g. 'authoritative'). Also read {LANE}/PROVINCE.md and judge each claim IN-SCOPE (firmware extraction tooling bearing on shipped-artifact evidence) or ADJACENT/GENERIC. Verdict per claim, plus a recommended admit/reject. Do not edit any file."""))
items.append(seat("R70W1AssimSwgde", "scout", ["adjacency", "coverage"], f"""Assimilation scope check (addendum section 10): package entry `swgde-custody-authority-and-normative-scope.md` and the SWGDE claims 1-2 of `digest-scope-versus-provenance-amendment-2026-10-23.md` (READ-ONLY under /home/vgpnk/Projects/shokuknow/merge/revenger/knowledge/corpus/knowledge/).

Do: read {LANE}/PROVINCE.md (Refuses; 'harness/evidence auditing'; the corpus/README.md Frontier bullet on custody 'enter only as it bears on shipped-artifact evidence ledgers') and {LANE}/corpus/QUALITY.md. Decide per entry: does SWGDE mobile-device/collection custody guidance bear on a shipped-artifact evidence ledger, or is it an adjacent sibling domain? Open the SWGDE document the entry cites yourself today (record date, sha256) and locate one quote of the 'shall' vs 'should' distinction (<=25 words, with its section). Verdict ADMIT-IN-SCOPE or REJECT-ADJACENT with the located quote and the PROVINCE sentence that decides it. Do not edit any file."""))
items.append(seat("R70W1AssimDraft", "scribe", ["coverage", "freshness"], f"""Assimilation draft (addendum section 10): write a re-grounded entry in THIS lane's schema from package entry `digest-scope-versus-provenance-amendment-2026-10-23.md` (read-only at /home/vgpnk/Projects/shokuknow/merge/revenger/knowledge/corpus/knowledge/), keeping ONLY claims 3-5 (Unblob upstream facts) — the SWGDE claims are out of scope for this lane's draft.

Do: open https://raw.githubusercontent.com/onekey-sec/unblob/main/README.md yourself today; quote each retained claim (<=25 words, located under its heading) with fetch date and sha256; write the draft at {LANE}/.ufo/waves/round-70/w1/R70W1AssimDraft.draft-entry.md with the header trio (`source:` S-row id + URL + anchor, `verified-at: 2026-10-25`, `recheck:`), `coverage-map: C07` (firmware images — held; this is a deepening, not a flip), `admission-status: candidate`, observation/inference/unknown, limitation, and a §Q-map with one honest row for each of Q01-Q15 against /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/QUALITY.md. Every number in it carries its command and output. Also draft the SOURCES row (11 columns, no `|` inside any cell, status `mined`, `used-by` naming the entry path) and its Gate-block lines. Put the verdict on the first line of the report: DRAFT-READY, or DRAFT-REFUSED with the reason. Do not edit any lane file other than your report and the draft file named above."""))
items.append(seat("R70W1MistakeSweep", "scout", ["calibration"], f"""Mine ONE mistake for corpus/lessons/round-70.md `## Mistakes` (class | evidence pointer | captured-by | fix; a fix counts only once shown able to fail).

Do: read {LANE}/corpus/lessons/round-69-verifier-spotcheck.md §6 (V1-V7) and {LANE}/corpus/lessons/round-69.md `## Mistakes`. Candidate: V1/V2/V4 — a report or scorecard cites a short hash that does not resolve or a command that does not run from the printed cwd (class `reference-drift` / `attribution`), plus the uncommitted seat edit after the tip commit (class `landing`). For the candidate: run the sweep commands that find every instance of the class in the lane's committed round-67..69 reports/SCORECARD/lessons (command + output pasted), and say which criterion or rule should have caught each (`captured-by`; `none` if none) and what fix would be shown able to fail. Verdict: the one mistake row, fully populated, with the sweep. Do not edit any file."""))

# --------------------------------------------------------------- independent byte read
items.append(seat("R70W1IndependentRead", "revenger", ["coverage", "depth"], f"""Independent reader of the fixture (Q03): cross-check readout.py's facts with a DIFFERENT implementation.

Do: read {FIXDIR}/fixture.apk with tools that do not share code with readout.py: python `zipfile` (member names, CRC-32, offsets via ZipInfo.header_offset), `unzip -lv`/`7z l -slt` if present, and any Android tool that exists on the host (`aapt2`, `aapt`, `apkanalyzer`, `jadx` 1.5.6, `apktool`: check `command -v`; read-only use, extraction ONLY into /tmp/revenger-r70-<seat>). Compare every fact the readout prints for items 1-3 and the AXML facts (strings, resource ids, attribute values) with what the independent tools report. Record tool, version, function exercised and exit status for each tool (Q04); manual analysis stays labeled manual. Report each comparison MATCH / DIVERGE with outputs, and name any tool that refuses the fixture (that is a finding about the fixture's inertness, not a failure of the readout). Verdict INDEPENDENT-AGREE, DIVERGE (list) or NO-INDEPENDENT-TOOL. Do not edit any lane file."""))

# ------------------------------------------------------------------------ connectors
items.append(seat("R70W1ConnSeparability", "connector", ["calibration", "adjacency"], f"""Cross-claim file-overlap scan for separability ({CLAIMS} §Separability).

Do: list every file each claim changes or names (C1: entry, entry_checks.py, lint_entry.py, snapshots, README C05 row + index lines for its own tools; C2: self_assessment_check.py, README index lines, SHONEN.md, SCORECARD erratum; C3: check_embedded_outputs.py, embedded_output_pins.json, derive_axml_anchors_r68.py, README index line). Find every file two claims both touch and every counter label one claim's change can move in another claim's tree (e.g. SM2 counting files README must name; SM6 reading the README held count; C3's pin rule reading the r68 entry). Propose the minimal per-claim README line split that keeps each single-claim tree's labels at or better than base. Verdict SEPARABLE (with the split) or ENTANGLED (list)."""))
items.append(seat("R70W1ConnSources", "connector", ["coverage", "adjacency"], f"""Cross-source pattern scan.

Do: across the S038, S043, S045, S032/S034 quotes the C05 entry uses ({ENTRY} items 11-12) and the lane's earlier rejected candidates (`corpus/knowledge/round-65-…`, `round-67-…`, `round-68-…`, `round-69-apk-axml-byte-evidence.md`), find recurring defect patterns in HOW the lane cites sources (line numbers typed by hand, quotes from folded HTML, digest pinned to a path outside corpus/, rows opened by the same author who writes the entry). Check each against v5 and report where the v5 candidate still carries the pattern. Also run the sibling-overlap scan: read {LANE}/PROVINCE.md and the fleet l0-questions.md line naming ADJ-06 (kaidoku/revenger shipped-artifact overlap) and confirm the v5 entry absorbs nothing. Verdict PATTERNS-CLEAR or PATTERNS-REMAIN (list)."""))
items.append(seat("R70W1ConnLedger", "connector", ["calibration", "adjacency"], f"""Bounded planning data-walk for the L1 (the validator rejects a planner role; this seat carries the planning walk).

Do: walk {LANE}/SCORECARD.md, {LANE}/LOG.md tail (last 3 round entries), {LANE}/corpus/lessons/round-67-verifier-spotcheck.md .. round-69-verifier-spotcheck.md and the fleet considerthese file {LANE}/considerthese/2026-10-24.md (proposals 3, 4, 5). Report: (a) which routed defects from the last three closures remain open at {BASE} and which of the three round-70 claims closes each (V1-V7, D1-D5, L0 items); (b) proposals 4 (undispatched-wave backlog) and 5 (burst-aware reporting): is either already satisfied by an existing artifact, with the pointer; (c) the stagnation-nudge state: SCORECARD `Saturation` section says line 7.0 and window N=3 — which axes sit at or above the line and whether a capability entered in the last 3 rounds (capabilities table pointer). Verdict PLAN-DATA-READY with the three tables."""))

spec = {
    "wave": "revenger-r70-w1",
    "milestone": "C1 C05 v5 candidate pre-gate + C2 self-assessment mismatch repair drafts + C3 pin attacks + frontier step (source re-opens, assimilation re-grounding, mistake sweep)",
    "reportDir": REPORT_DIR,
    "axes": ["coverage", "calibration", "freshness", "depth", "adjacency"],
    "context": CONTEXT,
    "items": items,
}

names = [i["name"] for i in items]
if len(names) != len(set(names)):
    print("duplicate seat names:", {n for n in names if names.count(n) > 1}, file=sys.stderr)
    sys.exit(1)
roles = {}
for i in items:
    roles[i["role"]] = roles.get(i["role"], 0) + 1
flash = sum(v for r, v in roles.items() if r in ("executor", "scribe", "critic", "revenger", "sentinel", "simplifier"))
print(f"seats={len(items)} roles={roles}")
print(f"m_flash roles={flash} ({100 * flash / len(items):.1f}%)")
WAVE_DIR.mkdir(parents=True, exist_ok=True)
out = WAVE_DIR / "w1-spec.json"
out.write_text(json.dumps(spec, indent=1), encoding="utf-8")
print(f"written: {out}")
