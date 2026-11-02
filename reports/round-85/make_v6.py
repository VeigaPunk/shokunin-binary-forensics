#!/usr/bin/env python
"""make_v6.py - derive orphan_sweep6.py from the committed v5 blob.

Change 9 (the routed v6 candidate vector): an unmatched bare token that names
a file under the fleet root resolves absent-fleet (bare-token normalized)
instead of being recorded as an unmatched absent row.

Every replacement is exact-match and assert-guarded; the script refuses to
write unless every patch applied."""
import pathlib

SRC = pathlib.Path(r"C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae"
                   r"/fleet/shokunin-binary-forensics/reports/round-84/orphan_sweep5.py")
s = SRC.read_text(encoding="utf-8")


def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:60], s.count(old))
    s = s.replace(old, new)


# 1. usage identity (module docstring line 2, usage lines 89/571/576)
rep("orphan_sweep5.py", "orphan_sweep6.py", 5)
# 2. docstring change note (appended to the change-8 block)
rep("# v5 change 8: LOG.md joins the citation corpus.",
    "# v5 change 8: LOG.md joins the citation corpus.\n"
    "# v6 change 9: an unmatched bare token that names a file under the FLEET\n"
    "#     root resolves absent-fleet (bare-token normalized) instead of being\n"
    "#     recorded as an unmatched absent row - the fleet-root bare-name class\n"
    "#     the r84 lesson dispositioned as known noise. Non-gating either way;\n"
    "#     exit codes 0/1/64 unchanged.")
# 3. the switch
rep("LOG_CORPUS = True\n",
    "LOG_CORPUS = True\n"
    "# v6 change 9: fleet-root bare-token resolution. The frozen mutant flips\n"
    "# this to False (one sed substitution) and MUST be caught by the\n"
    "# fleet-bare selftest vectors.\n"
    "FLEET_BARE_RESOLUTION = True\n")
# 4. twin + classify_bare extension
rep("def classify_bare(cited, head_files, head_dirs, disk_files, disk_dirs):",
    "def classify_bare_fleet_disabled(cited, head_files, head_dirs, disk_files,\n"
    "                                 disk_dirs, fleet_files):\n"
    "    \"\"\"Defective twin used only by the selftest mutant leg: change 9\n"
    "    switched off - what the frozen sed mutant (FLEET_BARE_RESOLUTION =\n"
    "    False) makes every fleet-root bare token do: fall through to the v5\n"
    "    recorded-absent row.\"\"\"\n"
    "    if bare_token_fileish(cited):\n"
    "        return (\"absent\",\n"
    "                \"bare-token unmatched: no file named %s under HEAD or the \"\n"
    "                \"working tree\" % cited)\n"
    "    return None\n"
    "\n"
    "\n"
    "def classify_bare(cited, head_files, head_dirs, disk_files, disk_dirs,\n"
    "                  fleet_files=None):")
rep("""    if not candidates:
        if UNMATCHED_BARE_ABSENT and bare_token_fileish(cited):""",
    """    if not candidates:
        # v6 change 9: resolve against the fleet-root basename index first
        if FLEET_BARE_RESOLUTION and fleet_files and bare_token_fileish(cited):
            base = cited.replace("\\\\", "/").rsplit("/", 1)[-1]
            hits = sorted(p for p in fleet_files
                          if p.replace("\\\\", "/").rsplit("/", 1)[-1] == base)
            if hits:
                shown = ", ".join("fleet/" + h for h in hits[:3])
                more = " (+%d more)" % (len(hits) - 3) if len(hits) > 3 else ""
                return ("absent-fleet",
                        "bare-token normalized: %s%s" % (shown, more))
        if UNMATCHED_BARE_ABSENT and bare_token_fileish(cited):""")
# 5. run_sweep: build the fleet index and pass it
rep("""    head_files, head_dirs, disk_files, disk_dirs = sets
    cited, n_rep, n_les, n_log = collect_citations(lane_dir, fleet_root)""",
    """    head_files, head_dirs, disk_files, disk_dirs = sets
    fleet_files = set()
    if FLEET_BARE_RESOLUTION and fleet_root:
        for base, dirs, files in os.walk(fleet_root):
            dirs[:] = [d for d in dirs if d != ".git"]
            rel = os.path.relpath(base, fleet_root).replace("\\\\", "/")
            prefix = "" if rel == "." else rel + "/"
            for f in files:
                fleet_files.add(prefix + f)
    cited, n_rep, n_les, n_log = collect_citations(lane_dir, fleet_root)""")
rep("""            outcome = classify_bare(tok, head_files, head_dirs,
                                    disk_files, disk_dirs)""",
    """            outcome = classify_bare(tok, head_files, head_dirs,
                                    disk_files, disk_dirs, fleet_files)""")
# 6. counter + always-printed fleet_resolved term
rep("    bare_matched = bare_skipped = bare_unmatched_absent = 0",
    "    bare_matched = bare_skipped = bare_unmatched_absent = 0\n"
    "    bare_fleet_resolved = 0")
rep("""            if status == "absent":
                bare_unmatched_absent += 1
            else:
                bare_matched += 1""",
    """            if status == "absent":
                bare_unmatched_absent += 1
            elif status == "absent-fleet":
                bare_fleet_resolved += 1
            else:
                bare_matched += 1""")
rep("""    print("SWEEP_BARE_TOKENS matched=%d unmatched_skipped=%d "
          "unmatched_recorded_absent=%d" % (
              bare_matched, bare_skipped, bare_unmatched_absent))""",
    """    print("SWEEP_BARE_TOKENS matched=%d unmatched_skipped=%d "
          "unmatched_recorded_absent=%d fleet_resolved=%d" % (
              bare_matched, bare_skipped, bare_unmatched_absent,
              bare_fleet_resolved))""")
# 7. selftest legs (inserted before the attribution block)
rep("""    if fails:
        # Attribution order matters: the change-6 mutant (bare classification
        # fully off) also fails the change-7 legs as a consequence, so the
        # bare-token class is attributed before the unmatched-absent class.""",
    """    # v6 change 9 vector: a bare token naming a fleet-root file resolves
    # absent-fleet (bare-token normalized) - the r84 lesson's known-noise
    # class. Negative: a token under NEITHER pool still records absent.
    f_head = {"reports/round-1/claims.md"}
    f_dirs = {"reports", "reports/round-1"}
    f_fleet = {"MISSION.md", ".ufo/reports/round-9/revenger.md"}
    st_fb = classify_bare("MISSION.md", f_head, f_dirs, f_head, f_dirs, f_fleet)
    if st_fb is not None and st_fb[0] == "absent-fleet" and \\
            "fleet/MISSION.md" in st_fb[1]:
        print("SWEEP_SELFTEST_FLEET_BARE_RESOLVED=ok")
    else:
        print("SWEEP_SELFTEST_FLEET_BARE_RESOLVED=FAIL (got %s)" % (st_fb,))
        fails.append("fleet-root bare token not resolved (got %s)" % (st_fb,))
    st_fn = classify_bare("no-such-receipt.log", f_head, f_dirs, f_head,
                          f_dirs, f_fleet)
    if st_fn is not None and st_fn[0] == "absent" and \\
            "bare-token unmatched" in st_fn[1]:
        print("SWEEP_SELFTEST_FLEET_BARE_ABSENT_NEGATIVE=ok")
    else:
        print("SWEEP_SELFTEST_FLEET_BARE_ABSENT_NEGATIVE=FAIL (got %s)" % (st_fn,))
        fails.append("fleet resolution masked a real absent (got %s)" % (st_fn,))
    # v6 mutant leg: the change-9-off twin MUST disagree with the resolved
    # vector (recorded-absent row != absent-fleet); agreement proves vacuous.
    st_fm = classify_bare_fleet_disabled("MISSION.md", f_head, f_dirs, f_head,
                                         f_dirs, f_fleet)
    if st_fm is not None and st_fm[0] == "absent" and st_fb is not None \\
            and st_fb[0] == "absent-fleet":
        print("SWEEP_SELFTEST_FLEET_BARE_MUTANT_FLAGGED=ok "
              "(mutant=absent-row, vector=absent-fleet)")
    else:
        print("SWEEP_SELFTEST_FLEET_BARE_MUTANT_FLAGGED=FAIL (mutant=%s)" % (st_fm,))
        fails.append("fleet-bare mutant agreed with the vector (vacuous)")
    if fails:
        # Attribution order matters: the change-6 mutant (bare classification
        # fully off) also fails the change-7 legs as a consequence, so the
        # bare-token class is attributed before the unmatched-absent class.""")
# 8. attribution class (fleet-bare attributed first)
rep("""        if any("log-corpus" in f for f in fails):
            print("selftest: log-corpus collection drifted (log-corpus class)")""",
    """        if any("fleet" in f for f in fails):
            print("selftest: fleet-bare resolution drifted (fleet-bare class)")
        elif any("log-corpus" in f for f in fails):
            print("selftest: log-corpus collection drifted (log-corpus class)")""")

out = pathlib.Path(__file__).parent / "orphan_sweep6.py"
out.write_text(s, encoding="utf-8", newline="\n")
print("wrote %s lines=%d" % (out, s.count("\n")))
