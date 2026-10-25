#!/usr/bin/env python3
"""Generate the revenger round-67 v2 wave spec (64 seats, policy v2).

Writes .ufo/waves/round-67/wave-spec.json. Validate with ufo-swarm-wave.mjs
plan before any dispatch. Scratch tool; the spec JSON is the committed artifact.
"""
import json
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
WAVE = LANE / ".ufo/waves/round-67"
ROWS = json.loads((WAVE / "assimilation/register-rows.json").read_text())

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
"""

CONTEXT = """# Goal
Revenger round 67 attempt 1 (hyaku) — ONE v2 wave of exactly 64 seats, build-and-attack together (wave-4 quarantine-first under the 2026-10-24 assimilation directive: this round adopts NOTHING from /home/vgpnk/Projects/shokuknow — verdicts only). Lane repo: /home/vgpnk/Projects/shokunin/revenger-shokunin — ABSOLUTE paths only in every read/write (your tools start at the fleet root /home/vgpnk/Projects/shokunin). Frozen contract (read first): /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-67/claims.md; frozen counter: /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-67/measure.py (sha256 7933c060db4d9b8db889830e2e0b6e1da1724d94854201aac9552e2a49cbc07e); red-before receipt: /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-67/measure-before.log (K_HELD 8/14, K_ROW C05 status=uncovered, C7_* 0/no, HOLDS_OK_V5=no, probe exit 0).

# Build state (landed by the L1 before this wave — your attack surface)
- C1: NEW candidate entry /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-67-apk-axml-byte-evidence.md (admission-status: candidate) — the round-66 routed text-level repairs of the falsified round-65 candidate (corpus/knowledge/round-65-apk-axml-byte-evidence.md, retained REJECTED, byte-preserved, never cite as held): entry:41-class hex pair now captured from actual command output; S038 enum anchor lines 237-253 (resource map at :253); route scope via S043 anchor lines 7-8; dex declared header on NEW row S045 (AOSP DEX format spec, opened 2026-10-24, snapshot .ufo/waves/round-67/source-snapshots/dex-format.html); item-8 attrExt-relative provenance; Q08 Q-map row; no dangling pointers. README C05 is NOT flipped (still uncovered). Fixture corpus/fixtures/apk-r65/ bytes unchanged since round 65.
- C2: NEW probe /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/check_embedded_outputs.py (embedded-output verbatim gate, outside the verify_* replay family): --entry mode re-runs each fenced `$ cmd` block and requires every output line verbatim in that command's stdout; --self-test is hermetic with the in-script forged control whose marker is `drifted entry output accepted`. Its red-before is committed history: the retained r65 candidate still carries the drifted hex at its entry:41, so --entry over it exits 1 naming entry:41 (15/15 blocks, 1 problem).
- Registry: S045 appended (mined, used-by the v2 entry); census exit 0 at round start (44 rows).

# Contract
Read /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-67/claims.md fully before scoring anything; the frozen predicates, kill rules, admission order and void conditions there override any summary in this prompt. Counting command: git archive <commit> corpus into a scratch tree, then from /: TMPDIR=/tmp/revenger-r67-counter-XXXX python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-67/measure.py <tree>. Measurements belong to committed trees only. Quality bar: /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/QUALITY.md (Q01-Q13).

# Bounds (hard)
Write ONLY your own report file at the absolute path named in your item brief (under /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/). Everything else — corpus/, reports/, LOG.md, SCORECARD.md, SHONEN.md, the fleet repo, sibling lane repos, /home/vgpnk/Projects/shokuknow (READ-ONLY — never write, commit, fetch-push or run campaign tools there), lane jj state, the lane Git index — is read-only for you; do NOT run git/jj mutations, do NOT edit any file another seat may own, do NOT write anywhere under /home/vgpnk/Projects/shokunin outside your own report path and the one scratch subdir your brief names (no fleet-root files). Read-only seats return findings without production edits. Never message other seats; never use agent://all. Every `Report:` trailer path is relative to /home/vgpnk/Projects/shokunin/revenger-shokunin — write it at /home/vgpnk/Projects/shokunin/revenger-shokunin/<that path>. Absolute paths everywhere.

# Tooling authorization (operator, 2026-10-19)
You and every seat may install or upgrade tools that help the task — read /home/vgpnk/.omp/agent/RULES.md first (official channels, update-safety gate, record tool/version/channel/reason in your report). Pacman guard (orchestrator ruling 2026-10-20): all pacman transactions are PAUSED host-wide — install via uv tool/npx/an official binary in ~/.local/bin, or file an L0 question; never -Sy/-Syu/-U/-R, never downgrade, never restart a host service.

# Seat rules
Time-box: return within 15 minutes with your best findings + evidence; partial results are acceptable. You are an independent leaf: never block on or wait for another seat; never spawn subagents; if a needed artifact is absent, record the dependency as a finding and return. Put your verdict on the first line of your report (PASS / FAIL / NOT-FALSIFIED / ADMIT / REJECT / CLEAN / PRESENT / ABSENT / UNREACHABLE + one-line reason), then evidence: commands with actual output, file:line pointers, sha256 where relevant. Ground every claim in a resolvable pointer; a claim without one is not evidence. Network fetches (curl -sL --max-redirs 15) are allowed for your assigned URL only."""


def item(name, role, axes, brief):
    return {"name": name, "role": role, "axes": axes,
            "prompt": GODSPEED + "\n" + brief}


items = []

# --- 26 quarantine seats -----------------------------------------------------
roles_cycle = (["scribe"] * 18 + ["scout"] * 8)
qids = sorted(ROWS.keys(), key=lambda s: int(s[1:]))
for i, sid in enumerate(qids):
    r = ROWS[sid]
    role = roles_cycle[i]
    scratch = f"/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/{sid}"
    if r["quotes"]:
        brief = f"""Quarantine hand-check (wave-4, item 10): register row {sid} (campaign round {r['round']}, class `{r['class']}`). You hand-check ONE row of /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md (READ-ONLY file; also read-only: /home/vgpnk/Projects/shokuknow entirely). The register claims the quoted strings below are ABSENT from the cited source — re-derive that absence yourself.
Cited source: {r['url']}
Quoted strings the register says are absent (check each, fixed-string, case-sensitive, AND after HTML-escaping/unescaping variants):
{r['quotes']}
Register note: {r['note']}
Do: mkdir -p {scratch}; fetch the URL with curl -sL --max-redirs 15 (record http code, byte size, sha256; save bytes under {scratch}/source.bin only if <= 2MB, else save sha256 + a 20-line excerpt). Search each quoted string in the fetched bytes (grep -F on raw and on a python html.unescape + tag-stripped rendering). Verdict rules — ABSENT: fetch succeeded (real document bytes) and every quoted string is missing (fabrication-class confirmation; name any near-miss you find, e.g. the true sentence it probably distorted); PRESENT: at least one quoted string IS in the fetched bytes (the register's absence claim is wrong — give byte offset + 15-word context); UNREACHABLE: fetch fails after 3 tries (record exact error). Report each string separately, then the row verdict on line 1.
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67Quar{sid}.md"""
    else:
        brief = f"""Quarantine hand-check (wave-4, item 10): register row {sid} (campaign round {r['round']}) is a PROSE-CLASS row ("{r['class']}") — the register's unchecked family: no quote was ever checked, so the row verdict is `unverifiable-unreachable` (never fabrication). Your job is the reachability + staged-quote evidence behind that verdict.
Cited source: {r['url']}
Also read the STAGED row for {sid} in /home/vgpnk/Projects/shokuknow/merge/revenger/SOURCES.append.md (read-only) and extract its anchor/quote cells.
Do: mkdir -p {scratch}; fetch the URL with curl -sL --max-redirs 15 (record http code, byte size, sha256; save under {scratch}/source.bin only if <= 2MB). Then check the staged row's own anchors against the fetched bytes: for {sid} that means the page <title> (or first heading), the footer "Last updated" date if present, and whether the named section ids/strings from the staged row occur (fixed-string). Verdict on line 1: UNVERIFIED-REACHABLE (fetch succeeded; staged anchors verified or not — say which), or UNREACHABLE (fetch failed; exact error). Never write to /home/vgpnk/Projects/shokuknow.
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67Quar{sid}.md"""
    items.append(item(f"R67Quar{sid}", role, ["coverage", "freshness"], brief))

# --- 13 Q-criteria seats on the v2 candidate ---------------------------------
V2 = "/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-67-apk-axml-byte-evidence.md"
R65 = "/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-65-apk-axml-byte-evidence.md"
SNAP = "/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-65/source-snapshots"
QTEXT = {
    "Q01": "Each load-bearing claim rests on a SOURCES row tier A for that claim's scope; a tier-C row is never sole support. Rows in play: S038 (re-opened this round from the committed snapshot — confirm the re-open), S043, S045 (new — verify the row in corpus/SOURCES.md), S041, S032/S034.",
    "Q02": "Header completeness: source:/verified-at:/recheck: with exact anchors (not bare homepages) and the coverage-map row named. Check every anchor against the committed snapshots: ResourceTypes.h enum block lines 237-253 with RES_XML_RESOURCE_MAP_TYPE at :253; route sentence at rea-android-applications.md lines 7-8; dex-format.html header_item field texts.",
    "Q03": "Expected values derived independently: from bytes, a spec, or a pin outside the record under test — nothing copied from the record being checked.",
    "Q04": "Tool claims name tool/version/function; manual analysis labeled manual. The entry claims a manual stdlib readout — verify no tool is credited with a result it did not output.",
    "Q05": "No readiness/capability claim without a probe. The entry fences the provider route to S043 documentation scope.",
    "Q06": "Fixture premises byte-verified against the built fixture; failed inputs retained. The fixture is the round-65 bundle (sha-pinned); verify the entry's sha256 claims against the actual files and that no fixture byte changed since round 65 (git log/diff on corpus/fixtures/apk-r65).",
    "Q07": "No parser-behavior prediction written as fact; no unreproduced cause used as support.",
    "Q08": "The entry's Q-map must carry a Q08 row marked `superseded by Q11` (QUALITY.md:23) — applying Q08 instead of Q11 is itself a Q11 failure. Verify the row exists and is correct.",
    "Q09": "Digests claimed only for the exact bytes hashed; no origin/completeness/authenticity; dex checksum/signature framed as inert declared-header self-consistency, not validity.",
    "Q10": "Scope bounded to the observed fixture/operation/version; cross-lane contested scope reported not absorbed (ADJ-06 note).",
    "Q11": "EVERY count, identifier, offset and digest carries, inside the entry, the deriving command and its actual output; constants derived, not assumed; recorded values labeled recorded. Re-run `python3 -B corpus/fixtures/apk-r65/readout.py` from the lane root and diff every embedded output line (this is the M39 check that killed the round-65 draft — the same class may recur here).",
    "Q12": "n/a expected (the entry writes no rejected source row) — confirm.",
    "Q13": "n/a expected (no verifier credited beyond the entry's own recheck) — confirm no verifier is credited for clauses its run does not detect.",
}
qroles = {"Q01": "reviewer", "Q02": "reviewer", "Q03": "reviewer", "Q04": "critic",
          "Q05": "critic", "Q06": "critic", "Q07": "critic", "Q08": "reviewer",
          "Q09": "reviewer", "Q10": "reviewer", "Q11": "reviewer", "Q12": "critic",
          "Q13": "reviewer"}
for qid in sorted(QTEXT):
    extra = ""
    if qid == "Q11":
        extra = "\nCross-check the retained round-65 draft for contrast: the SAME check over " + R65 + " must exit 1 naming entry:41 (that is the M39 baseline)."
    if qid == "Q06":
        extra = "\nAlso verify the round-65 candidate file is byte-preserved (only its admission-status line differs from its round-65 state is NOT required — it must be byte-identical to the round-66 tip version: git show 8362a235:corpus/knowledge/round-65-apk-axml-byte-evidence.md | cmp - " + R65 + ")."
    items.append(item(
        f"R67ReviewEntry{qid}", qroles[qid], ["coverage"],
        f"""Named fresh-seat admission decision {qid} on the LANDED v2 candidate bytes (round-66 routed C05 re-gate). Entry under test: {V2} — read it fully. Quality bar: /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/QUALITY.md criterion {qid} (read it there, not from memory). Decision {qid}: {QTEXT[qid]}{extra}
You are NOT the author; decide independently on the committed bytes. Verdict line 1: `{qid} PASS` / `{qid} FAIL (<failing fact>)` / `{qid} n/a (<named reason>)`. FAIL requires a file:line pointer and, for value mismatches, the command you ran and its actual output. Also report any OFF-criterion defect you notice (one line each, prefix OFF-).
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67ReviewEntry{qid}.md"""))

# --- C7 gate attacks ---------------------------------------------------------
items.append(item("R67MutC7Kill", "mutation-tester", ["calibration"],
  f"""Mutation-test the new probe {LANE}/corpus/check_embedded_outputs.py against the FROZEN mutant in reports/round-67/claims.md §C2: regex `problems \\+= drift\\(lines, stdout_set, lineno\\)` must match exactly once; apply it (python re.sub count=1, replacement `problems += []  # mutant: verbatim comparison removed`) to a TEMP COPY of corpus/ (never the lane tree), run `python3 -B corpus/check_embedded_outputs.py --self-test` in the temp copy, and verify: exit non-zero AND last output line ends `drifted entry output accepted` (attributed). Also run the UNMUTATED self-test (expect exit 0) and the --entry red check over corpus/knowledge/round-65-apk-axml-byte-evidence.md (expect exit 1 naming entry:41). Then try TWO adversarial mutants of your own design on temp copies (e.g. make drift() compare only the first embedded line; make evaluate() skip blocks with >1 output line) and report whether the self-test catches each (honest result either way — an escaped mutant is a finding, not a failure of yours). Report the exact commands and outputs.
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67MutC7Kill.md"""))
items.append(item("R67MutC7Surface", "mutation-tester", ["calibration"],
  """Adversarial-entry attack on the same probe: craft THREE temp-dir entries (with a temp reader.py you write under /tmp/revenger-r67-atk/) that a set-membership verbatim check may wrongly accept: (a) right lines in the WRONG ORDER, (b) a correct line DUPLICATED with one line replaced by another stdout line from the same command, (c) an EXTRA line that is not in stdout at all but is valid JSON from a DIFFERENT fact. Run corpus/check_embedded_outputs.py --entry on each from a scratch lane-root-like temp tree and report for each: caught or false-clean (exit 0). Honest results; a false-clean is a real finding about the gate's surface — name it as the recorded limitation it is, with the exact reproduction.
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67MutC7Surface.md"""))
items.append(item("R67CriticC7Claim", "critic", ["calibration"],
  f"""Falsify the C2 claim semantics in reports/round-67/claims.md (read it fully). Attack angles: (1) could a do-nothing control reach any C7 target label (the base receipt prints them 0/no — confirm from measure-before.log)? (2) is the C7 mutant regex unique in the gate file (count matches)? (3) is the marker attribution gameable (could the unmutated self-test print the marker and still exit 0 — check require() exits 1)? (4) does C7 gate placement outside the verify_* glob actually preserve HOLD_REPLAY=10/10 (read reports/round-67/measure.py's HOLD loop)? (5) counter substitution (M34): does any C7 label flip from prose alone without the gate file existing? Verdict line 1: NOT-FALSIFIED or FALSIFIED (<reason>).
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67CriticC7Claim.md"""))
items.append(item("R67ReviewC7Gate", "reviewer", ["calibration"],
  f"""Read-only review of {LANE}/corpus/check_embedded_outputs.py as a registered probe: verdict-map sanity (0 clean / 1 drift / 2 could-not-evaluate — does the code actually exit those codes on those paths?), self-test hermeticity (temp trees, no network, no lane-tree writes), command surface (argv list, no shell; python3 only — injection or arbitrary-command risk from a malicious entry?), and the SKILL.md registry row's accuracy (read the new `## Gate registry` section in {LANE}/SKILL.md — does every stated fact about the probe match the code?). Verdict CLEAN or issues found (file:line).
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67ReviewC7Gate.md"""))

# --- counter / census / fixture holds ----------------------------------------
items.append(item("R67CounterReplay", "executor", ["calibration", "coverage"],
  """Independent counter re-run: mkdir -p /tmp/revenger-r67-seat-counter && git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive fa0eb3eb33f22f56ebf066dea5440121a30d55a2 corpus | tar -x -C /tmp/revenger-r67-seat-counter && cd / && TMPDIR=/tmp/revenger-r67-seat-counter python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-67/measure.py /tmp/revenger-r67-seat-counter, then diff your key labels against /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-67/measure-before.log (K_HELD, K_ROW C05, C05_*, C7_*, C6_RECEIPT_KILLED_ATTRIBUTED, HOLD_CALIBRATION, HOLD_REPLAY, FRESH_ROWS, HOLDS_OK*, exit code). Also sha256sum the committed measure.py and confirm it equals the sha pinned in claims.md. Verdict MATCH or MISMATCH (<label>).
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67CounterReplay.md"""))
items.append(item("R67CensusReplay", "executor", ["freshness"],
  """Run the seven census commands from /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md §Census (contract v1 shape: rows, malformed=0, tier histogram, status histogram, duplicate ids empty, enum violations empty, mined used-by paths exist) against the CURRENT working tree, and also /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger. Record row count (expect 45 after S045), all zero/empty promises, and the fleet validator's exit code. Note: the S045 row is new this round — its status is `mined` and its used-by names corpus/knowledge/round-67-apk-axml-byte-evidence.md which must exist.
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67CensusReplay.md"""))
items.append(item("R67FixtureHold", "executor", ["calibration"],
  """Fixture immutability hold (void condition): cp -a /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65 /tmp/revenger-r67-seat-fixture && cd /tmp/revenger-r67-seat-fixture && python3 -B generator.py, then byte-compare generator outputs fixture.apk and truth.json against the committed originals (cmp; truth.json may differ ONLY in nothing at all on this host — record the sha256 of both before/after and any byte difference verbatim). Record python3 --version. Then verify the committed fixture.apk sha256 equals the entry header's 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e. Verdict: BYTE-IDENTICAL or DRIFTED (<evidence>).
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67FixtureHold.md"""))

# --- independent byte verifications ------------------------------------------
items.append(item("R67HexContainer", "executor", ["coverage"],
  f"""Independent hex verification (no lane counter involved): from the committed fixture bytes, decode and confirm the three payload_first16_hex values and the three member sha256s printed in {V2} item 3 (python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[...]' from the lane root is ALLOWED as the deriving command, but ALSO verify independently: python -c reading corpus/fixtures/apk-r65/fixture.apk with zipfile off the corpus tree in /tmp — copy the fixture to /tmp first, never write in the lane). Confirm the MANIFEST.MF first-16 decodes to ASCII `Manifest-` and that the entry's repair note about the round-65 draft's 15-byte transcription is accurate (compare {R65} entry line 41).
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67HexContainer.md"""))
items.append(item("R67HexDex", "executor", ["coverage"],
  f"""Independent dex-header verification: recompute (python stdlib, your own code, NOT readout.py) over the classes.dex member extracted from a /tmp copy of corpus/fixtures/apk-r65/fixture.apk: magic bytes, adler32(offset 12..), sha1(offset 32..), file_size and header_size u32s at offsets 32/36, endian tag at 40. Compare each with the values embedded in {V2} item 9. Then open the snapshot {LANE}/.ufo/waves/round-67/source-snapshots/dex-format.html and confirm the header_item field texts the entry quotes for checksum/signature/header_size/endian_tag actually occur there (fixed-string, tag-stripped rendering). Verdict: ALL-MATCH or MISMATCH (<field>).
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67HexDex.md"""))
items.append(item("R67PointerAudit", "scribe", ["depth"],
  f"""Pointer audit of {V2}: every file:line pointer the entry makes must resolve. Check: readout.py:99-105 (payload_offset derivation), :166 (UTF-8 flag test), :200-203 (attribute location comment + computation), :22 (0xffffffff null treatment); snapshot {SNAP}/ResourceTypes.h lines 218, 237-253 (with :239 :241 :244 :246 :247 :248 :253 named), 287, 461, 612, 621, 677, 685-687 (attributeStart comment text), 707; {SNAP}/rea-android-applications.md lines 7-8; {LANE}/.ufo/waves/round-67/source-snapshots/dex-format.html contains the three quoted field texts. Also confirm the entry's own 16 fenced blocks each carry a `$ ` command line (count them). Verdict: ALL-RESOLVE or list every dangling pointer.
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67PointerAudit.md"""))

# --- blind derivation ---------------------------------------------------------
items.append(item("R67BlindDerive", "scout", ["coverage"],
  """Blind independent derivation (Q03 independence): WITHOUT reading corpus/fixtures/apk-r65/readout.py or the v2 entry's Observation section, derive from /tmp-copy fixture bytes + the ResourceTypes.h snapshot (/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-65/source-snapshots/ResourceTypes.h) your own walk of the AXML member: chunk table (type/offset/headerSize/size), string-pool count/flags/strings, resource-map ids, start-element attribute rows. Write your own short python in /tmp. THEN open the v2 entry and diff your table against its items 4-8; report agreement and every divergence with bytes. Verdict: CONCUR or DIVERGE (<item>).
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67BlindDerive.md"""))

# --- separability --------------------------------------------------------------
items.append(item("R67ReviewSeparability", "reviewer", ["coverage", "calibration"],
  """Causal separability of the two round-67 claims (claims.md): run git -C /home/vgpnk/Projects/shokunin/revenger-shokunin diff --name-status fa0eb3eb..<build tip you see in .ufo/waves/round-67/build-commit.txt if present, else the working tree state via git status/diff HEAD> and verify: C1's surface = corpus/knowledge/round-67-*.md + corpus/SOURCES.md (S045) + (post-adjudication only) README C05 row; C2's surface = corpus/check_embedded_outputs.py + SKILL.md registry row + reports/round-67/counter. No file is touched by both; each claim verifies without the other (C7 labels need only the gate file; K labels need only knowledge/SOURCES/README). Verdict SEPARABLE or ENTANGLED (<file>).
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67ReviewSeparability.md"""))
items.append(item("R67CriticSeparability", "critic", ["coverage", "calibration"],
  """Attack the same separability from the counter side: in reports/round-67/measure.py, which labels does C1 depend on and which does C2 depend on? Could landing C2 alone (gate file present, no v2 entry) print HOLDS_OK_V5=yes? (Read the V5 formula — it requires c7_v2_clean, which requires the v2 file: is that an entanglement between C2's target and C1's artifact? Decide whether that makes the claims non-causally-separable under AXES.md, or an acceptable shared artifact with C2's predicate still self-standing via its other labels. Argue honestly either way; the frozen predicate stands either way — your ruling informs the report's disclosure.) Verdict: SEPARABLE / SHARED-ARTIFACT-ACCEPTABLE / ENTANGLED (<reason>).
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67CriticSeparability.md"""))

# --- connector / sentinel / simplifier / revenger ------------------------------
items.append(item("R67ConnectorOverlap", "connector", ["adjacency"],
  """Sibling-overlap scan (report-not-absorb): which sibling lane corpora already hold dex/APK/Android ground — grep -l -i 'dex\\|apk\\|android' over /home/vgpnk/Projects/shokunin/*/corpus/knowledge/*.md and the sibling READMEs (read-only). For each hit name the lane, the file, and one line proving the overlap or distinguishing it (revenger's C05 ground = manual byte-level declared-header readout of ONE authored fixture; no provider, no signing, no decompilation claims). List anything that looks like contested scope for the integrator. Verdict: NO-CONTEST or CONTEST-NAMED (<lane, pointer>).
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67ConnectorOverlap.md"""))
items.append(item("R67SentinelScope", "sentinel", ["calibration"],
  """Scope sweep (read-only): verify no seat-reachable path lets this wave write outside /home/vgpnk/Projects/shokunin/revenger-shokunin: read the wave context bounds + 3 sample seat briefs (quarantine, Q-gate, mutation) and confirm each names an absolute report path under the lane's .ufo/waves/round-67/ and forbids fleet-root writes; confirm the quarantine briefs mark /home/vgpnk/Projects/shokuknow READ-ONLY and never name a campaign tool (renumber-staged.py, merge-plan.py, quote-lint.py, absent-defect-register.py are campaign tools that WRITE into shokuknow — a brief must never ask a seat to run one). Also run git -C /home/vgpnk/Projects/shokunin status --porcelain and list any untracked fleet-root files (misroot candidates) — do NOT delete anything. Verdict: CLEAN or findings.
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67SentinelScope.md"""))
items.append(item("R67SimplifierGate", "simplifier", ["depth"],
  f"""Minimality review of {LANE}/corpus/check_embedded_outputs.py: could any function be deleted or merged without losing (a) the frozen-mutant kill (self-test forged control), (b) the entry-mode verbatim check, (c) exit-code contract? Name dead code, unused imports, or branches no caller reaches — each with a one-line justification. Do NOT edit the file; propose the minimal diff in your report. Verdict: MINIMAL or list.
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67SimplifierGate.md"""))
items.append(item("R67RevengerLedger", "revenger", ["calibration"],
  f"""Evidence-ledger discipline attack on {V2}: are observation/inference/unknown genuinely separated (does any inference masquerade as observation — check item 7's resource-map sentence and the 0xffffffff null treatment); does any digest claim scope beyond the exact bytes hashed (Q09); is the recheck's stdout-sha256 claim scoped to the 15 lines and nothing else; is the 'recorded' vs 're-derived' labeling honest in the Comparison section (the round-65 regeneration is now cited as S041 evidence, not re-run — is that stated plainly)? Verdict: HOLDS or findings (<item>).
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67RevengerLedger.md"""))

# --- discernment spot-check + sources-tier ------------------------------------
items.append(item("R67SpotcheckDiscern", "reviewer", ["calibration"],
  f"""Outside-discernment spot-check (LEARNING.md): sample THIS round's landed gate decisions as recorded so far — (a) ADMIT sample: the new S045 row in {LANE}/corpus/SOURCES.md — re-open the snapshot {LANE}/.ufo/waves/round-67/source-snapshots/dex-format.html yourself, verify the row's anchors/quotes are located and verbatim and the tier/scope are honest, then AGREE or DISAGREE with the admit; (b) REJECT sample: the retained round-65 candidate {R65} stays `admission-status: rejected` — re-run python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[META-INF/MANIFEST.MF]' from the lane root and confirm the entry:41 drift still justifies the reject, then AGREE or DISAGREE. Verdict line 1: `S045-ADMIT-<AGREE|DISAGREE>` + `R65-REJECT-<AGREE|DISAGREE>` with reasons.
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67SpotcheckDiscern.md"""))
items.append(item("R67ReviewSourcesS045", "reviewer", ["freshness"],
  f"""Tier/scope review of the new S045 row ({LANE}/corpus/SOURCES.md): is tier A honest for the declared scope (vendor-published format spec — primary for the dex header's DECLARED field semantics; confirm the row's scope does not overreach into dex validity or general parsing); is the anchor an exact located span (not a bare homepage); does the snapshot sha256 match the committed file; is the ≤25-word Gate quote (recorded in corpus/lessons/round-67.md when it lands — if absent, verify the quotes inside the v2 entry's S045 source header instead against the snapshot bytes). Also confirm census enum rules accept the row (kind=docs, tier=A, status=mined). Verdict PASS or findings.
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67ReviewSourcesS045.md"""))
items.append(item("R67ScoutDexReopen", "scout", ["freshness"],
  f"""Independent re-open of the dex spec (freshness): fetch https://source.android.com/docs/core/runtime/dex-format yourself (curl -sL --max-redirs 15), sha256 your fetch, and compare with the committed snapshot {LANE}/.ufo/waves/round-67/source-snapshots/dex-format.html (sha256 c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4) — byte drift is EXPECTED on hosted docs (last-updated footer); report whether the header_item field texts still match (tag-stripped fixed-string) so the row's recheck (180d) has a first data point. Save nothing in the lane; report hashes + the footer date you see. Verdict: STABLE or DRIFTED (<evidence>).
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67ScoutDexReopen.md"""))
items.append(item("R67ScoutSigningRecon", "scout", ["coverage"],
  """Frontier recon (no row, no claims): the APK Signing Block is the platform-owner-published spec adjacent to C05's uncovered ground (the retained r65 candidate's limitations name signature blocks as NOT covered). Locate (fetch) the official APK Signing Block description (source.android.com docs on APK signing schemes) and report: exact URL, the block's magic constant, one ≤25-word located quote on the block's placement in the file, and what a minimal byte-level fixture check of it would require. This is recon for a FUTURE round's frontier claim only — this round claims nothing from it. Save fetched bytes under /tmp only.
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67ScoutSigningRecon.md"""))

# --- claims critics --------------------------------------------------------------
items.append(item("R67CriticClaimsC1", "critic", ["coverage"],
  f"""Falsify the C1 claim shape in reports/round-67/claims.md: (1) universal clauses without a full-set enumeration? (2) do-nothing reachability — from the base receipt (measure-before.log) could any pass-branch label print without the v2 entry + wave all-pass (README label spoof: a one-line README edit prints K_ROW C05 status=held with zero entry work — the wave's named Q decisions are the defense; confirm the claims text makes the flip land in the SAME revision as the Gate decision and requires the named seats)? (3) predicate narrowing risk after landing? (4) is the either-way kill rule falsifiable as written (what exact observation makes C1 FALSIFIED)? Verdict: NOT-FALSIFIED or FALSIFIED (<reason>).
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67CriticClaimsC1.md"""))
items.append(item("R67CriticAssim", "critic", ["adjacency"],
  """Attack the quarantine posture (item 10, wave-4): the round adopts NOTHING from /home/vgpnk/Projects/shokuknow. Read reports/round-67/claims.md §Assimilation posture + the derived slice file .ufo/waves/round-67/assimilation/quarantine-slice (26 lines) + register-rows.json. Verify: (1) the slice re-derivation awk on the register yields exactly these 26 rows (re-run it); (2) no lane file appends or copies any package row or knowledge file (check git status + the working tree for new corpus/ files vs claims); (3) the id-collision evidence files exist (reg-ids 44 / staged-ids 146 / collisions 0) and the S045 collision-with-staged-space drift is correctly described as a by-document renumber obligation, not an error; (4) the two prose-class rows (S054, S099) are classified unverifiable-unreachable, not fabrication. Verdict: SOUND or findings.
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67CriticAssim.md"""))

# --- SHONEN box-1 re-attempt + entry-provenance --------------------------------
items.append(item("R67ReviewSkillRefresh", "reviewer", ["depth"],
  f"""SHONEN box-1 evidence refresh (routed from r64/r66): the round-64 non-author verifier `R64ReviewSkill` passed the pre-refresh SKILL.md bytes (sha 260ab2b4... — see .ufo/waves/round-64/R64ReviewSkill.md); SKILL.md was refreshed in r66 and gains a Gate-registry section this round. Read the CURRENT {LANE}/SKILL.md fully and re-state whether box 1 (`real decision tables, error patterns, checklists, cited sources`) is `[x]`-ready on THESE bytes: do the decision tables (§1-3) match the committed verifier bytes (spot-check two control line-ranges against the actual files), does §4 map M33-M41 to checks that exist, does the new `## Gate registry` row match {LANE}/corpus/check_embedded_outputs.py, and do §7's cited paths all resolve? (A lane-dispatched seat is still the lane — your YES records evidence; the [x] flip stays a non-lane duty.) Verdict: `[x]-ready YES` or `NO (<gaps>)`.
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67ReviewSkillRefresh.md"""))
items.append(item("R67CriticEntryDeps", "critic", ["coverage"],
  f"""Silent-dependency attack on {V2} (the round-65 draft failed this attack): find every value the entry uses that its own text does not derive and its cited sources do not state. Candidates to test: the eocd signature constant 504b0506 (S032/S034-derived? stated where?), the 46/30-byte fixed parts, the 0x100 UTF-8 flag bit (the r65 draft credited S038's flags enum — the v2 now cites the readout's own test instead: is that honest?), the resource-map entry width (one uint32 per string — derived where?), `737 + 188 == 925` arithmetic. For each: DERIVED (point to the entry's own derivation) or SILENT (<value>). Verdict: NO-SILENT-DEPS or list.
Write your report at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67CriticEntryDeps.md"""))

assert len(items) == 64, len(items)
from collections import Counter
print(Counter(i["role"] for i in items))

spec = {
    "wave": "revenger-r67-v2",
    "milestone": "C1 v2 C05 candidate + C2 C7 gate landed as build state; README not flipped; wave provides fresh-seat Q decisions, C7 mutant/surface attacks, 26 quarantine verdicts, separability and discernment receipts",
    "reportDir": ".ufo/waves/round-67",
    "axes": ["coverage", "calibration", "freshness", "depth", "adjacency"],
    "context": CONTEXT,
    "items": items,
}
(WAVE / "wave-spec.json").write_text(json.dumps(spec, indent=1, ensure_ascii=False))
print("wrote", WAVE / "wave-spec.json")
