#!/usr/bin/env python3
"""Round-68 build script (revenger L1, Kimi fresh L1).

Builds the landed artifacts of round 68 and the frozen counter:

  1. corpus/snapshots/ResourceTypes.h  — byte-exact copy of the lane's pinned
     AOSP snapshot, so the anchor derivation runs from any corpus tree.
  2. corpus/check_embedded_outputs.py  — C7 repair: the attributed marker
     becomes reachable and is the killing line (round-67 M45 shadowing).
  3. corpus/knowledge/round-68-apk-axml-byte-evidence.md — the C05 v3
     candidate (round-67 candidate + the two :244 -> :245 anchor fixes +
     machine-derived anchors + the derivation item).
  4. reports/round-68/measure.py       — the frozen round-68 counter (the
     round-67 counter plus the C7 negative-spoof control, the v3 entry check
     and the C2 coverage aggregate).

Run from the lane root:  python3 -B .ufo/waves/round-68/build-r68.py
Exit 0 on success; non-zero with a message on any failed precondition.
The script is idempotent: it restores the gate from the lane branch tip
before patching, so it can be re-run from a clean state.
"""
import hashlib
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
PINNED = ROOT / ".ufo/waves/round-65/source-snapshots/ResourceTypes.h"
COPY = ROOT / "corpus/snapshots/ResourceTypes.h"
GATE = ROOT / "corpus/check_embedded_outputs.py"
R67_ENTRY = ROOT / "corpus/knowledge/round-67-apk-axml-byte-evidence.md"
V3_ENTRY = ROOT / "corpus/knowledge/round-68-apk-axml-byte-evidence.md"
R67_COUNTER = ROOT / "reports/round-67/measure.py"
R68_COUNTER = ROOT / "reports/round-68/measure.py"
DERIVE = ROOT / "corpus/derive_axml_anchors.py"

SNAPSHOT_SHA256 = "56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f"


def die(msg):
    print(f"build-r68: {msg}", file=sys.stderr)
    sys.exit(1)


def sub_once(text, old, new, what):
    n = text.count(old)
    if n != 1:
        die(f"{what}: expected 1 occurrence, found {n}")
    return text.replace(old, new, 1)


# ---------------------------------------------------------------- 1. snapshot
if not PINNED.is_file():
    die(f"pinned snapshot missing: {PINNED}")
raw = PINNED.read_bytes()
digest = hashlib.sha256(raw).hexdigest()
if digest != SNAPSHOT_SHA256:
    die(f"pinned snapshot digest {digest} != {SNAPSHOT_SHA256}")
COPY.parent.mkdir(parents=True, exist_ok=True)
COPY.write_bytes(raw)
if hashlib.sha256(COPY.read_bytes()).hexdigest() != SNAPSHOT_SHA256:
    die("copied snapshot digest mismatch")
print(f"copy: {COPY.relative_to(ROOT)} sha256={digest} bytes={len(raw)}")

# ------------------------------------------------------------------- 2. gate
restored = subprocess.run(
    ["git", "show", "refs/heads/main:corpus/check_embedded_outputs.py"],
    cwd=str(ROOT), capture_output=True, text=True)
if restored.returncode != 0:
    die(f"cannot restore the gate from the branch tip: {restored.stderr.strip()}")
gate = restored.stdout
old_block = '''    dproblems, dchecked = evaluate(drifted_entry, tmp)
    require(dproblems is not None and dchecked == 1 and dproblems
            and dproblems[0].startswith("drift entry:"),
            "self-test: drifted entry not caught")
    fproblems, fchecked = evaluate(full_entry, tmp)
    require(fproblems is not None and fchecked == 1 and not fproblems,
            "self-test: full-run entry not clean")
    # In-script forged control: the drifted case MUST be caught. If the
    # verbatim comparison is removed (or weakened), this fires with the
    # attributed marker as the last output line.
    require(not ok(dproblems), MARKER)
    print("SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired")
'''
new_block = '''    dproblems, dchecked = evaluate(drifted_entry, tmp)
    # Forged control (round-68 repair of M45): the drifted case MUST be
    # caught. If the verbatim comparison is removed (or weakened) the branch
    # below is taken, and the attributed marker is the LAST output line, so
    # the kill is attributable to the marker and not to some earlier require.
    caught = (dproblems is not None and dchecked == 1 and dproblems
              and dproblems[0].startswith("drift entry:"))
    if not caught:
        print("self-test: drifted entry not caught")
        print(MARKER)
        sys.exit(1)
    fproblems, fchecked = evaluate(full_entry, tmp)
    require(fproblems is not None and fchecked == 1 and not fproblems,
            "self-test: full-run entry not clean")
    print("SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired")
'''
gate = sub_once(gate, old_block, new_block, "gate self-test block")
gate = sub_once(gate, '''def ok(problems):
    return not problems


''', "", "gate ok() helper")
gate = sub_once(
    gate,
    "Probe, not a registered gate of the verify_* replay family: this file is",
    "Registered gate (SKILL.md `## Gate registry`, kind `gate`): a committed,\n"
    "re-runnable verdict script that can fail. It is deliberately OUTSIDE the\n"
    "verify_* replay family: this file is",
    "gate docstring kind")
gate = sub_once(
    gate,
    "        Hermetic temp-tree cases plus the in-script forged control whose\n"
    "        attributed failure marker is `drifted entry output accepted`.",
    "        Hermetic temp-tree cases plus the in-script forged control whose\n"
    "        attributed failure marker is `drifted entry output accepted` — the\n"
    "        marker is the last output line of a failed run (round-68 repair of the\n"
    "        round-67 shadowing defect M45).",
    "gate docstring marker")
GATE.write_text(gate, encoding="utf-8")
print(f"gate: {GATE.relative_to(ROOT)} patched")

# ------------------------------------------------------- 3. the v3 entry text
entry = R67_ENTRY.read_text(encoding="utf-8")
entry = sub_once(entry, "`RES_XML_START_NAMESPACE_TYPE` :244,",
                 "`RES_XML_START_NAMESPACE_TYPE` **:245**,", "entry header anchor")
derive_sha = hashlib.sha256(DERIVE.read_bytes()).hexdigest()
entry = sub_once(
    entry,
    "source: S041 — Authored apk-r65 bundle",
    "source: S046 — AXML anchor derivation (own-work, tier A; row opened round 68 by this entry's "
    "author) — scope: the machine derivation of every S038 line number this entry cites, read from "
    "the pinned snapshot bytes; not the layout facts themselves, which rest on S038 — anchor: "
    f"`corpus/derive_axml_anchors.py` sha256 `{derive_sha}`, 17 output lines over "
    "`corpus/snapshots/ResourceTypes.h` sha256 "
    "`56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f` (exit 2 on a missing or "
    "ambiguous symbol); snapshot `.ufo/waves/round-65/source-snapshots/ResourceTypes.h` sha256 "
    "`56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`\n"
    "source: S041 — Authored apk-r65 bundle",
    "entry S046 source line")
entry = sub_once(
    entry,
    'its `attributeStart` field comment "Byte offset from the start of this structure '
    'where the attributes start." at lines 685-687',
    'its `attributeStart` field comment "Byte offset from the start of this structure '
    'where the attributes start." at line 686, with the field declaration '
    '`uint16_t attributeStart;` at line 687',
    "entry header attrExt comment")
entry = sub_once(
    entry,
    "pinned tag `android-15.0.0_r1`; snapshot `.ufo/waves/round-65/source-snapshots/"
    "ResourceTypes.h` sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`, 86255 bytes",
    "pinned tag `android-15.0.0_r1`; snapshot `.ufo/waves/round-65/source-snapshots/"
    "ResourceTypes.h` sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`, 86255 bytes "
    "— committed byte-exact as `corpus/snapshots/ResourceTypes.h` (same sha256) so the anchor derivation "
    "below runs from any corpus tree",
    "entry header snapshot copy")
entry = sub_once(entry, "`struct Res_value` (line 287);",
                 "`struct Res_value` (line 287); **every line number above is machine-derived by "
                 "`corpus/derive_axml_anchors.py` from the pinned snapshot — item 11**;",
                 "entry header derivation pointer")
entry = sub_once(
    entry,
    "verified-at: 2026-10-24 (round-67 re-derivation; the fixture, oracle and readout bytes are the "
    "round-65 claim-tree bytes, unchanged since `c7b7cf98`; every output line below was captured from the "
    "named command's actual stdout at build time, never transcribed by hand — the round-65 draft's entry:41 "
    "transcription drift is the M39 class this entry repairs)",
    "verified-at: 2026-10-24 (round-68 re-derivation; the fixture, oracle and readout bytes are the "
    "round-65 claim-tree bytes, unchanged since `c7b7cf98`; every output line below was captured from the "
    "named command's actual stdout at build time, never transcribed by hand — the round-65 draft's entry:41 "
    "transcription drift is the M39 class this entry repairs, and the round-67 draft's `:244` anchor is the "
    "M40/M44 class this entry repairs by deriving every spec line number from the pinned snapshot)",
    "entry verified-at")
entry = sub_once(
    entry,
    "recheck: `python3 -B corpus/fixtures/apk-r65/readout.py` from the lane root",
    "recheck: `python3 -B corpus/derive_axml_anchors.py` from the lane root (every S038 line number "
    "this entry cites; exits 2 if a cited symbol is missing or ambiguous) and "
    "`python3 -B corpus/fixtures/apk-r65/readout.py` from the lane root",
    "entry recheck")
old_status = [l for l in entry.splitlines() if l.startswith("admission-status:")][0]
entry = sub_once(
    entry, old_status,
    "admission-status: candidate — the round-68 third-pass candidate: the round-67 v2 candidate's two "
    "`:244` anchors are corrected to `:245` (the derived table in item 11 is the machine proof), the spec "
    "line numbers are now derived by `corpus/derive_axml_anchors.py` rather than transcribed, and the "
    "readout bytes, oracle and fixture are unchanged since round 65. It is NOT admitted: the README C05 row "
    "stays `uncovered` until the dispatched wave's fresh seats return an all-criteria pass on these bytes "
    "(frozen order in `reports/round-68/claims.md` §C2); on a fail the row stays `uncovered` and this file is "
    "marked `rejected`.",
    "entry admission-status")
entry = sub_once(
    entry,
    "(string pool :239, start/end namespace :244/:246, start/end element :247/:248, resource map "
    "`RES_XML_RESOURCE_MAP_TYPE` :253)",
    "(string pool :239, start/end namespace :245/:246, start/end element :247/:248, resource map "
    "`RES_XML_RESOURCE_MAP_TYPE` :253 — every one of these line numbers is derived by item 11's command)",
    "entry item4 prose anchors")
entry = sub_once(
    entry,
    '"Byte offset from the start of this structure where the attributes start" (snapshot lines 685-687)',
    '"Byte offset from the start of this structure where the attributes start" (snapshot line 686; the '
    "field declaration `uint16_t attributeStart;` at line 687 — item 11 derives both)",
    "entry item8 attrExt comment")
entry = sub_once(entry, "with the round-65 corpus tree (bytes unchanged through round 67):",
                 "with the round-65 corpus tree (bytes unchanged through round 68):", "entry reproduce tree note")
entry = sub_once(
    entry,
    "- **Observation** — every value in items 1-10: read directly from the committed bytes by the "
    "§Reproduce script, which runs with the Python standard library only.",
    "- **Observation** — every value in items 1-10: read directly from the committed bytes by the "
    "§Reproduce script, which runs with the Python standard library only; and every spec line number in "
    "item 11, derived from the pinned snapshot bytes by a committed script that cannot print a line it did "
    "not find.",
    "entry observation section")
entry = sub_once(entry, "the fixed struct constants carry their S038 field-list derivation (item 5);",
                 "the fixed struct constants carry their S038 field-list derivation (item 5); the spec line "
                 "numbers carry their deriving command and output (item 11, machine-derived, not transcribed);",
                 "entry Q11 row")
entry = sub_once(
    entry,
    "Exit 0; 15 stdout lines; their SHA-256 is `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` "
    "(re-derived 2026-10-24).",
    "Exit 0; 15 stdout lines; their SHA-256 is `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` "
    "(re-derived 2026-10-24). Anchor derivation: `python3 -B corpus/derive_axml_anchors.py` — exit 0, 17 lines, "
    "one per cited symbol (item 11).",
    "entry reproduce sha")

proc = subprocess.run([sys.executable, "-B", str(DERIVE)], cwd=str(ROOT),
                      capture_output=True, text=True)
if proc.returncode != 0:
    die(f"derive_axml_anchors.py failed: {proc.stdout}{proc.stderr}")
derived = proc.stdout.rstrip("\n").splitlines()
if len(derived) != 17:
    die(f"derivation produced {len(derived)} lines, expected 17")
item11 = (
    "**Spec anchors (machine-derived)**\n"
    "\n"
    "11. Every S038 line number this entry states is printed by a committed derivation script that "
    "searches the pinned snapshot bytes for each cited symbol — no spec line number in this entry is "
    "transcribed by hand. The script refuses to print a line it did not find (a missing or ambiguous "
    "symbol is exit 2), and it reads `corpus/snapshots/ResourceTypes.h`, the byte-exact copy of the "
    "pinned snapshot (same sha256 as the row's snapshot):\n"
    "\n"
    "```\n"
    "$ python3 -B corpus/derive_axml_anchors.py\n"
    + "\n".join(derived) + "\n"
    "```\n"
    "\n"
    "The chunk-type enum block spans lines 237-253 and `RES_XML_START_NAMESPACE_TYPE` is line **245**; "
    "line 244 is `RES_XML_FIRST_CHUNK_TYPE`. That one-line off-by-one is what falsified the round-65 and "
    "round-67 drafts (M40/M44); the derivation above is the capture that makes it mechanical.\n"
)
entry = sub_once(entry, "## Comparison with the authored oracle",
                 item11 + "\n## Comparison with the authored oracle", "entry item 11 insert")
V3_ENTRY.write_text(entry, encoding="utf-8")
print(f"entry: {V3_ENTRY.relative_to(ROOT)} written ({len(entry.splitlines())} lines)")

# ---------------------------------------------------------- 4. the r68 counter
counter = R67_COUNTER.read_text(encoding="utf-8")
counter = sub_once(
    counter,
    """  C2  calibration target: C7 embedded-output verbatim gate
      (corpus/check_embedded_outputs.py, outside the verify_* replay family):
      GATE_PRESENT / SELFTEST / CONTROL_PASS / MUTANT_KILLED_ATTRIBUTED /
      RED_ON_R65_CANDIDATE / V2_CLEAN, plus HOLDS_OK_V5 = V4 ^ C7 targets.
All round-66 labels and formulas are byte-identical in semantics.""",
    """  C2  calibration target: C7 embedded-output verbatim gate
      (corpus/check_embedded_outputs.py, outside the verify_* replay family):
      GATE_PRESENT / SELFTEST / CONTROL_PASS / MUTANT_KILLED_ATTRIBUTED /
      RED_ON_R65_CANDIDATE / V2_CLEAN, plus HOLDS_OK_V5 = V4 ^ C7 targets.
  C1  round-68 additions: C7_NEG_SPOOF_KILLED / C7_NEG_SPOOF_KILLED_ATTRIBUTED
      (the frozen mutant with the marker TEXT spoofed: killed but not
      attributable, so the attribution rule reads 0/1 and cannot be satisfied
      by any non-zero exit), C7_V3_CLEAN (the round-68 candidate is clean
      under the repaired gate), C05_SINGLE_V3 and HOLDS_C2_V3 (the coverage
      aggregate), plus HOLDS_OK_V6 = V5 ^ the C7 negative control.
All round-66 and round-67 labels and formulas are byte-identical in semantics.""",
    "counter docstring")

counter = sub_once(
    counter,
    """print(f"C7_CONTROL_PASS={c7_control_ok}/1")
print(f"C7_MUTANT_KILLED={c7_mut_killed}/1")
print(f"C7_MUTANT_KILLED_ATTRIBUTED={c7_mut_attributed}/1")""",
    """print(f"C7_CONTROL_PASS={c7_control_ok}/1")
print(f"C7_MUTANT_KILLED={c7_mut_killed}/1")
print(f"C7_MUTANT_KILLED_ATTRIBUTED={c7_mut_attributed}/1")

# C7 negative control (round-68): the frozen mutant (the verbatim comparison
# removed) PLUS a spoofed marker text. The run must still be killed (exit 1)
# while the attribution rule reads 0 — the last line is no longer the
# registered marker. This is what makes the attribution rule meaningful: a
# repair that kills the mutant with any other message scores 0/1.
C7_SPOOF_CLAUSE = re.compile(r\'MARKER = "drifted entry output accepted"\')


def mutate_c7_spoof(text):
    hits = C7_SPOOF_CLAUSE.findall(text)
    if len(hits) != 1:
        return None
    return C7_SPOOF_CLAUSE.sub(\'MARKER = "drifted entry output accepted (spoofed)"\', text, count=1)


c7_neg_killed = c7_neg_attributed = 0
if c7_present:
    with tempfile.TemporaryDirectory(prefix="rev-r68-c7neg-") as tmp:
        work = pathlib.Path(tmp)
        shutil.copytree(TREE / "corpus", work / "corpus", symlinks=True)
        target = work / "corpus" / C7_GATE_REL
        text = target.read_text(encoding="utf-8")
        mutated = mutate_c7(text)
        if mutated is None:
            print("MUTANT check_embedded_outputs.py c7neg could-not-evaluate (clause match count != 1)")
            evaluable = False
        else:
            spoofed = mutate_c7_spoof(mutated)
            if spoofed is None:
                print("MUTANT check_embedded_outputs.py c7neg could-not-evaluate (spoof clause count != 1)")
                evaluable = False
            else:
                target.write_text(spoofed, encoding="utf-8")
                rc, last = run(work, C7_GATE_REL, "--self-test")
                state = "pass" if rc == 0 else "killed"
                print(f"MUTANT check_embedded_outputs.py c7neg exit={rc} {state} :: {last[:160]}")
                c7_neg_killed += rc != 0
                c7_neg_attributed += rc != 0 and last.endswith(C7_MARKER)
print(f"C7_NEG_SPOOF_KILLED={c7_neg_killed}/1")
print(f"C7_NEG_SPOOF_KILLED_ATTRIBUTED={c7_neg_attributed}/1")""",
    "counter C7 negative control")

counter = sub_once(
    counter,
    """c7_red = False
c7_v2_clean = False""",
    """c7_red = False
c7_v2_clean = False
c7_v3_clean = False""",
    "counter c7_v3_clean init")

counter = sub_once(
    counter,
    """    else:
        print("C7_V2_CLEAN=n/a (no v2 file)")
else:""",
    """    else:
        print("C7_V2_CLEAN=n/a (no v2 file)")
    v3 = TREE / "corpus/knowledge/round-68-apk-axml-byte-evidence.md"
    if v3.is_file():
        rc, last = run(TREE, C7_GATE_REL, "--entry",
                       "corpus/knowledge/round-68-apk-axml-byte-evidence.md")
        c7_v3_clean = rc == 0
        print(f"C7_V3_CLEAN={'yes' if c7_v3_clean else 'no'} exit={rc} :: {last[:160]}")
    else:
        print("C7_V3_CLEAN=n/a (no v3 file)")
else:""",
    "counter C7_V3_CLEAN")

counter = sub_once(
    counter,
    """print(f"C05_SINGLE_V2={'yes' if c05_single_v2 else 'no'}")""",
    """print(f"C05_SINGLE_V2={'yes' if c05_single_v2 else 'no'}")
c05_single_v3 = (len(c05_entries) == 1
                 and c05_entries[0] == "knowledge/round-68-apk-axml-byte-evidence.md")
print(f"C05_SINGLE_V3={'yes' if c05_single_v3 else 'no'}")""",
    "counter C05_SINGLE_V3")

counter = sub_once(
    counter,
    """print(f"README_TOKEN_LEGEND_MISMATCH={len(mismatch)} rows={mismatch}")""",
    """print(f"README_TOKEN_LEGEND_MISMATCH={len(mismatch)} rows={mismatch}")

# C2 coverage aggregate (round-68): the C05 row must be held, backed by the
# round-68 candidate alone, with the strict (no rejected candidate) reading
# and no legend mismatch.
c05_row_line = next((l for l in rows if l.startswith("| C05 ")), "")
c05_status = c05_row_line.rsplit("|", 2)[-2].strip() if c05_row_line else "absent"
c2_v3_ok = (len(backed) == 9 and len(strict) == 9 and c05_single_v3
            and c05_status == "held" and len(mismatch) == 0)
print(f"C05_STATUS={c05_status}")
print(f"HOLDS_C2_V3={'yes' if c2_v3_ok else 'no'}")""",
    "counter C2 aggregate")

counter = sub_once(
    counter,
    """print(f"HOLDS_OK_V5={'yes' if (holds_ok_v4 and c7_targets) else 'no'}")""",
    """holds_ok_v5 = (holds_ok_v4 and c7_targets)
print(f"HOLDS_OK_V5={'yes' if holds_ok_v5 else 'no'}")
holds_ok_v6 = (holds_ok_v5 and c7_neg_killed == 1 and c7_neg_attributed == 0
               and c7_v3_clean)
print(f"HOLDS_OK_V6={'yes' if holds_ok_v6 else 'no'}")""",
    "counter HOLDS_OK_V6")

R68_COUNTER.parent.mkdir(parents=True, exist_ok=True)
R68_COUNTER.write_text(counter, encoding="utf-8")
print(f"counter: {R68_COUNTER.relative_to(ROOT)} written "
      f"sha256={hashlib.sha256(R68_COUNTER.read_bytes()).hexdigest()}")
print("build-r68: OK")
