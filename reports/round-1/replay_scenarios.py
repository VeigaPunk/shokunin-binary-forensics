#!/usr/bin/env python3
"""Deterministic saved-ledger replay scenario runner - fleet round-1.

Evidence-runner interface only, not production verifier scope. Invokes the real
named two-image PE saved-record verifier CLI in a fresh subprocess for every
scenario: no mocks, no imports of verifier internals. Positives run the CLI
from the corpus's lane-root equivalent, from an unrelated CWD, and from a
minimal corpus copy staged under a path containing spaces and non-ASCII.
Expected-rejection scenarios run the CLI inside isolated temporary copies
whose saved record or receipt was forged, regenerating ONLY the receipt
stdout_sha256 on saved-report mutations so each rejection is attributable to
semantic/path checking, never to an incidental raw-hash mismatch. Evidence IDs
are never changed; the runner re-reads each mutated tree and fails itself if
the forgery touched anything beyond the declared field. Original input bytes
are SHA-256 snapshotted before and after and never written. Temporary trees
are removed unless --keep-temp. Exit 0 only when every acceptance is met:
positives 3/3, expected rejections 6/6, inputs 9/9 unchanged, verifier script
unchanged, cleanup verified. Stdlib only; deterministic verdicts.
"""
import argparse
import copy
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LANE_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = "verify_named_multi_icon_states.py"
ROUNDS = (55, 56, 57)
TIMEOUT_SECONDS = 120
UNICODE_DIR = "replay 快照 ünïcode ✓"
HIST_PREFIX = "/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus"
INPUT_ROUNDS_NOTE = "inputs = 3 fixture + 3 inspection.raw.json + 3 receipt.json"


class RunnerError(RuntimeError):
    """The runner's own forgery/integrity expectation failed (scenario ERROR)."""


def emit(obj):
    print(json.dumps(obj, sort_keys=True, ensure_ascii=False))


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha_file(path):
    return sha_bytes(path.read_bytes())


def corpus_inventory(corpus):
    files = [corpus / SCRIPT]
    for r in ROUNDS:
        files += [
            corpus / "fixtures" / f"pe-r{r}" / "fixture.exe",
            corpus / "live" / "runs" / f"round-{r}" / "inspection.raw.json",
            corpus / "live" / "runs" / f"round-{r}" / "receipt.json",
        ]
    return files


def snapshot(corpus):
    return {str(p.relative_to(corpus)): sha_file(p) for p in corpus_inventory(corpus)}


def json_diff(a, b, path=""):
    """Dotted/bracketed JSON paths where two parsed documents disagree."""
    out = []
    if isinstance(a, dict) and isinstance(b, dict) and a.keys() == b.keys():
        for key in a:
            out += json_diff(a[key], b[key], f"{path}.{key}" if path else key)
    elif isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        for i, (x, y) in enumerate(zip(a, b)):
            out += json_diff(x, y, f"{path}[{i}]")
    elif a != b:
        out.append(path or "<root>")
    return out


def last_line(text):
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    return lines[-1] if lines else ""


def run_cli(script, cwd):
    proc = subprocess.run(
        [sys.executable, "-B", script],
        cwd=str(cwd),
        capture_output=True,
        text=True,
        timeout=TIMEOUT_SECONDS,
    )
    diag = last_line(proc.stderr) if proc.returncode != 0 else last_line(proc.stdout)
    return proc.returncode, diag


def stage(base, label, corpus):
    root = base / label
    staged = root / "corpus"
    for src in corpus_inventory(corpus):
        dst = staged / src.relative_to(corpus)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
    return root, staged


def saved_paths(corpus_dir, r):
    run = corpus_dir / "live" / "runs" / f"round-{r}"
    return run / "inspection.raw.json", run / "receipt.json"


def forge_report(corpus_dir, r, expect_diff, prepare):
    """Mutate inspection.raw.json, regenerate ONLY receipt stdout_sha256."""
    raw, rc = saved_paths(corpus_dir, r)
    before_bytes = raw.read_bytes()
    before_report = json.loads(before_bytes)
    before_receipt = json.loads(rc.read_bytes())
    eid = before_report["evidence_id"]
    if before_receipt["evidence_id"] != eid:
        raise RunnerError(f"r{r}: report/receipt Evidence IDs already disagree")
    mutated = prepare(copy.deepcopy(before_report))
    data = json.dumps(mutated, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    raw.write_bytes(data)
    after_report = json.loads(raw.read_bytes())
    if after_report != mutated:
        raise RunnerError(f"r{r}: mutated report failed JSON round-trip")
    report_diff = json_diff(before_report, after_report)
    if sorted(report_diff) != sorted(expect_diff):
        raise RunnerError(f"r{r}: forgery touched {report_diff}, expected {expect_diff}")
    receipt = dict(before_receipt)
    receipt["stdout_sha256"] = sha_bytes(data)
    rc.write_bytes(json.dumps(receipt, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))
    after_receipt = json.loads(rc.read_bytes())
    receipt_diff = json_diff(before_receipt, after_receipt)
    raw_now = raw.read_bytes()
    if sorted(receipt_diff) != ["stdout_sha256"]:
        raise RunnerError(f"r{r}: receipt touched {receipt_diff}, expected stdout_sha256 only")
    if after_receipt["evidence_id"] != eid:
        raise RunnerError(f"r{r}: Evidence ID changed")
    if after_receipt["stdout_sha256"] != sha_bytes(raw_now):
        raise RunnerError(f"r{r}: receipt stdout_sha256 does not match raw bytes")
    return {
        "forged": "inspection.raw.json",
        "round": r,
        "report_diff": sorted(report_diff),
        "receipt_diff": sorted(receipt_diff),
        "evidence_id_unchanged": True,
        "stdout_sha256_regenerated_only": True,
    }


def forge_receipt(corpus_dir, r, expect_diff, prepare):
    """Mutate receipt.json only; raw bytes and stdout_sha256 stay consistent."""
    raw, rc = saved_paths(corpus_dir, r)
    before_bytes = raw.read_bytes()
    before_receipt = json.loads(rc.read_bytes())
    eid = json.loads(before_bytes)["evidence_id"]
    mutated = prepare(copy.deepcopy(before_receipt))
    rc.write_bytes(json.dumps(mutated, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))
    after_receipt = json.loads(rc.read_bytes())
    diff = json_diff(before_receipt, after_receipt)
    if sorted(diff) != sorted(expect_diff):
        raise RunnerError(f"r{r}: forgery touched {diff}, expected {expect_diff}")
    if before_bytes != raw.read_bytes():
        raise RunnerError(f"r{r}: inspection.raw.json bytes changed")
    if after_receipt["evidence_id"] != eid:
        raise RunnerError(f"r{r}: Evidence ID changed")
    if after_receipt["stdout_sha256"] != sha_bytes(before_bytes):
        raise RunnerError(f"r{r}: receipt stdout_sha256 no longer matches untouched raw")
    return {
        "forged": "receipt.json",
        "round": r,
        "receipt_diff": sorted(diff),
        "raw_untouched": True,
        "evidence_id_unchanged": True,
        "stdout_sha256_regenerated_only": False,
    }


# --- forgery preparations -----------------------------------------------------

def prep_path_launder(staged_fixture):
    def prepare(report):
        artifact = report["normalized_result"]["artifact"]
        if not artifact["path"].startswith(HIST_PREFIX):
            raise RunnerError("saved r55 artifact path is not the historical producer path")
        artifact["path"] = str(staged_fixture)
        return report
    return prepare


def prep_command_launder(staged_fixture):
    def prepare(receipt):
        command = receipt["command"]
        prefix = "npx -y rea-agents@6.4.0 inspect-pe-resources "
        if not (command.startswith(prefix) and command.endswith(" --format json")
                and HIST_PREFIX in command):
            raise RunnerError("saved r55 receipt command is not the historical command")
        receipt["command"] = f"{prefix}{staged_fixture} --format json"
        return receipt
    return prepare


def prep_second_candidate(report):
    image = report["normalized_result"]["icon_groups"][0]["images"][1]
    if image["candidate_resource_indices"] != []:
        raise RunnerError("saved r56 image 1 candidate list is not []")
    image["candidate_resource_indices"] = [1]
    return report


def prep_size_match(report):
    image = report["normalized_result"]["icon_groups"][0]["images"][1]
    if image["size_matches"] is not False:
        raise RunnerError("saved r57 image 1 size_matches is not False")
    image["size_matches"] = True
    return report


def prep_unicode_name_location(report):
    location = report["normalized_result"]["resources"][2]["name"]["location"]
    if location != {"offset": 736, "bytes": 12}:
        raise RunnerError("saved r55 Unicode name location is not offset 736 bytes 12")
    location["offset"] = 700
    return report


def prep_ancestor_entry_location(report):
    entry = report["normalized_result"]["resources"][2]["entry_locations"][0]
    if entry != {"offset": 536, "bytes": 8}:
        raise RunnerError("saved r55 ancestor type-entry location is not offset 536 bytes 8")
    entry["offset"] = 520
    return report


# --- scenarios ----------------------------------------------------------------

def positive_scenario(sid, shape):
    def run(base, corpus, unrelated_cwd):
        if shape == "lane-root-cli":
            cwd, script = corpus.parent, str(Path(corpus.name) / SCRIPT)
        elif shape == "unrelated-cwd":
            cwd, script = unrelated_cwd, str(corpus / SCRIPT)
        elif shape == "spaces-nonascii-copy":
            cwd, _staged = stage(base, f"isolated-{sid}-{UNICODE_DIR}", corpus)
            script = str(Path("corpus") / SCRIPT)
        else:
            raise RunnerError(f"unknown positive shape {shape}")
        exit_code, diag = run_cli(script, cwd)
        return {
            "kind": "positive",
            "shape": shape,
            "cwd": str(cwd),
            "script": script,
            "expect": "exit 0 and stdout line starting PASS:",
            "exit": exit_code,
            "diag": diag,
            "met": exit_code == 0 and diag.startswith("PASS:"),
        }
    return run


def negative_scenario(sid, r, setup, expected_diag, location):
    def run(base, corpus, unrelated_cwd):
        cwd, staged = stage(base, f"isolated-{sid}", corpus)
        staged_fixture = staged / "fixtures" / f"pe-r{r}" / "fixture.exe"
        meta = setup(staged, staged_fixture)
        script = str(Path("corpus") / SCRIPT)
        exit_code, diag = run_cli(script, cwd)
        return {
            "kind": "expected-rejection",
            "shape": location,
            "round": r,
            "cwd": str(cwd),
            "script": script,
            "expect": f"exit 1 and stderr line {expected_diag!r}",
            "exit": exit_code,
            "diag": diag,
            "forgery": meta,
            "met": exit_code == 1 and diag == expected_diag,
        }
    return run


def build_scenarios():
    def launder(corpus_dir, staged_fixture):
        return forge_report(
            corpus_dir, 55,
            ["normalized_result.artifact.path"],
            prep_path_launder(staged_fixture),
        )

    def cmd_launder(corpus_dir, staged_fixture):
        return forge_receipt(
            corpus_dir, 55, ["command"], prep_command_launder(staged_fixture)
        )

    def second_candidate(corpus_dir, staged_fixture):
        return forge_report(
            corpus_dir, 56,
            ["normalized_result.icon_groups[0].images[1].candidate_resource_indices"],
            prep_second_candidate,
        )

    def size_match(corpus_dir, staged_fixture):
        return forge_report(
            corpus_dir, 57,
            ["normalized_result.icon_groups[0].images[1].size_matches"],
            prep_size_match,
        )

    def unicode_name_location(corpus_dir, staged_fixture):
        return forge_report(
            corpus_dir, 55,
            ["normalized_result.resources[2].name.location.offset"],
            prep_unicode_name_location,
        )

    def ancestor_entry_location(corpus_dir, staged_fixture):
        return forge_report(
            corpus_dir, 55,
            ["normalized_result.resources[2].entry_locations[0].offset"],
            prep_ancestor_entry_location,
        )

    return [
        ("P1 lane-root CLI", "positive",
         positive_scenario("P1-lane-root", "lane-root-cli")),
        ("P2 unrelated CWD", "positive",
         positive_scenario("P2-unrelated-cwd", "unrelated-cwd")),
        ("P3 minimal copy under spaces+non-ASCII path", "positive",
         positive_scenario("P3-spaces-nonascii", "spaces-nonascii-copy")),
        ("N1 forged historical artifact path relabeled to relocated copy",
         "expected-rejection",
         negative_scenario("N1-forged-artifact-path", 55, launder,
                           "AssertionError: r55 artifact", "isolated-copy")),
        ("N2 forged receipt command relabeled to relocated copy",
         "expected-rejection",
         negative_scenario("N2-forged-receipt-command", 55, cmd_launder,
                           "AssertionError: r55 receipt", "isolated-copy")),
        ("N3 second-candidate claim r56", "expected-rejection",
         negative_scenario("N3-second-candidate", 56, second_candidate,
                           "AssertionError: r56 normalized result", "isolated-copy")),
        ("N4 size-match claim r57", "expected-rejection",
         negative_scenario("N4-size-match", 57, size_match,
                           "AssertionError: r57 normalized result", "isolated-copy")),
        ("N5 Unicode name location claim r55", "expected-rejection",
         negative_scenario("N5-unicode-name-location", 55, unicode_name_location,
                           "AssertionError: r55 normalized result", "isolated-copy")),
        ("N6 ancestor entry location claim r55", "expected-rejection",
         negative_scenario("N6-ancestor-entry-location", 55, ancestor_entry_location,
                           "AssertionError: r55 normalized result", "isolated-copy")),
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--corpus", default=str(LANE_ROOT / "corpus"),
                        help="corpus root containing the verifier, fixtures/pe-rNN and "
                             "live/runs/round-NN records; point at an isolated git-archive "
                             "extraction for reproducible before measurements")
    parser.add_argument("--keep-temp", action="store_true",
                        help="keep staged temporary trees and print their paths")
    args = parser.parse_args()

    corpus = Path(args.corpus).resolve()
    inventory = corpus_inventory(corpus)
    missing = [str(p) for p in inventory if not p.is_file()]
    if missing:
        emit({"event": "setup", "met": False, "corpus": str(corpus),
              "missing": missing, "note": INPUT_ROUNDS_NOTE})
        print("RESULT FAIL exit=2 (missing corpus inputs)")
        return 2

    before = snapshot(corpus)
    emit({"event": "corpus-snapshot", "phase": "before", "corpus": str(corpus),
          "sha256": before, "inputs_note": INPUT_ROUNDS_NOTE})

    base = Path(tempfile.mkdtemp(prefix="shokunin-replay-r1-"))
    unrelated_cwd = base / "unrelated-cwd"
    unrelated_cwd.mkdir()
    records = []
    try:
        for title, kind, run in build_scenarios():
            sid = title.split()[0]
            try:
                record = {"event": "scenario", "id": sid, "title": title, **run(base, corpus, unrelated_cwd)}
            except Exception as error:
                record = {"event": "scenario", "id": sid, "title": title, "kind": kind,
                          "exit": "error", "diag": f"runner-internal: {error}", "met": False}
            records.append(record)
            emit(record)
    finally:
        if args.keep_temp:
            cleanup = {"event": "cleanup", "action": "kept", "path": str(base), "met": base.exists()}
        else:
            shutil.rmtree(base, ignore_errors=True)
            cleanup = {"event": "cleanup", "action": "removed",
                       "met": not base.exists()}
        emit(cleanup)

    after = snapshot(corpus)
    emit({"event": "corpus-snapshot", "phase": "after", "corpus": str(corpus), "sha256": after})
    input_keys = sorted(k for k in after if not k.endswith(SCRIPT))
    inputs_met = sum(after[k] == before[k] for k in input_keys)
    verifier_met = after[SCRIPT] == before[SCRIPT]

    positives = [r_ for r_ in records if r_["kind"] == "positive"]
    rejections = [r_ for r_ in records if r_["kind"] == "expected-rejection"]
    pos_met = sum(bool(r_.get("met")) for r_ in positives)
    rej_met = sum(bool(r_.get("met")) for r_ in rejections)
    for r_ in records:
        if not r_.get("met"):
            print(f"ACCEPTANCE-MISS scenario={r_['id']} kind={r_['kind']} "
                  f"exit={r_.get('exit')} diag={r_.get('diag')} expected={r_.get('expect')}")

    print(f"POSITIVES met={pos_met}/{len(positives)}")
    print(f"EXPECTED_REJECTIONS met={rej_met}/{len(rejections)}")
    print(f"INPUTS met={inputs_met}/{len(input_keys)} (SHA-256 unchanged before/after)")
    print(f"VERIFIER_SCRIPT met={1 if verifier_met else 0}/1 (unchanged)")
    print(f"CLEANUP met={1 if cleanup['met'] else 0}/1 ({cleanup['action']})")

    all_met = (pos_met == len(positives) == 3 and rej_met == len(rejections) == 6
               and inputs_met == len(input_keys) == 9 and verifier_met and cleanup["met"])
    exit_code = 0 if all_met else 1
    emit({"event": "summary", "positives": {"met": pos_met, "total": len(positives)},
          "expected_rejections": {"met": rej_met, "total": len(rejections)},
          "inputs_unchanged": {"met": inputs_met, "total": len(input_keys)},
          "verifier_unchanged": verifier_met, "cleanup": cleanup["met"],
          "all_acceptance_met": all_met, "exit": exit_code})
    print(f"RESULT {'PASS' if all_met else 'FAIL'} exit={exit_code}")
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
