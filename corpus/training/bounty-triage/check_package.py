#!/usr/bin/env python3
"""Validate one offline bounty-triage package against the module's rules.

A package is a directory holding the four artifacts the module requires:

    scope.json      the authorized-scope record (written authorization, dates,
                    methods, artifacts, disclosure channel)
    artifacts/...   the bytes named by scope.json, digest-bound
    ledger.md       evidence rows: id | artifact_sha256 | layer | statement | command
    report.md       the nine required sections, evidence-bound impact statements

The validator is a *training exercise instrument*, not an admission gate: it
checks structure and binding, and it cannot tell whether a statement is true.

Usage (from the lane root):

    python3 -B corpus/training/bounty-triage/check_package.py \
        --package corpus/training/bounty-triage/fixtures/exercise-r1/package \
        --as-of 2026-10-27

    python3 -B corpus/training/bounty-triage/check_package.py --self-test

Exit codes: 0 pass · 1 findings · 2 could-not-evaluate · 64 usage.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path
from urllib.parse import urlparse

REQUIRED_SECTIONS = (
    "scope",
    "artifact identity",
    "method",
    "evidence",
    "reproduction",
    "impact",
    "limitations",
    "stop conditions",
    "disclosure",
)
LAYERS = ("observation", "inference", "unknown")
PROVENANCE = ("program-provided", "authored")
LIVE_TERMS = ("live", "exploit", "dynamic", "network-scan")
OVERCLAIM = {
    "confirmed exploitable": re.compile(r"\bconfirmed\s+exploitable\b", re.I),
    "confirmed exploit": re.compile(r"\bconfirmed\s+exploit\b", re.I),
    "proven exploitable": re.compile(r"\bproven\s+exploitable\b", re.I),
    "full compromise": re.compile(r"\bfull\s+compromise\b", re.I),
    "guaranteed": re.compile(r"\bguaranteed\b", re.I),
    "affects all users": re.compile(r"\baffects\s+all\s+(?:users|accounts)\b", re.I),
    "remote code execution confirmed": re.compile(
        r"\bremote\s+code\s+execution\s+confirmed\b", re.I
    ),
}
EVIDENCE_ID = re.compile(r"\bE([0-9]{1,4})\b")


class Findings:
    def __init__(self) -> None:
        self.items: list[tuple[str, str]] = []

    def add(self, code: str, detail: str) -> None:
        self.items.append((code, detail))

    def codes(self) -> set[str]:
        return {code for code, _ in self.items}

    def sorted(self) -> list[tuple[str, str]]:
        return sorted(self.items)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_sections(text: str) -> dict[str, str]:
    """Return lower-cased H2 heading -> body text. First occurrence wins."""
    sections: dict[str, str] = {}
    current: str | None = None
    lines: list[str] = []
    for line in text.splitlines():
        match = re.match(r"^##\s+(.+?)\s*$", line)
        if match:
            if current is not None and current not in sections:
                sections[current] = "\n".join(lines).strip()
            current = match.group(1).strip().casefold()
            lines = []
        elif current is not None and re.match(r"^#\s+", line):
            if current not in sections:
                sections[current] = "\n".join(lines).strip()
            current = None
            lines = []
        elif current is not None:
            lines.append(line)
    if current is not None and current not in sections:
        sections[current] = "\n".join(lines).strip()
    return sections


def parse_ledger(text: str) -> tuple[list[dict[str, str]], list[int]]:
    rows: list[dict[str, str]] = []
    malformed: list[int] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if cells and cells[0].casefold() == "id":
            continue
        if not cells or not re.fullmatch(r"E[0-9]{1,4}", cells[0]):
            continue
        if len(cells) != 5:
            malformed.append(lineno)
            continue
        rows.append(
            {
                "id": cells[0],
                "digest": cells[1].strip("`"),
                "layer": cells[2].casefold(),
                "statement": cells[3],
                "command": cells[4].strip("`").strip(),
                "line": str(lineno),
            }
        )
    return rows, malformed


def validate(package: Path, as_of: _dt.date) -> tuple[Findings, dict[str, object]]:
    findings = Findings()
    stats: dict[str, object] = {}

    scope_path = package / "scope.json"
    try:
        scope = json.loads(scope_path.read_text(encoding="utf-8"))
        if not isinstance(scope, dict):
            raise ValueError("scope.json is not an object")
    except Exception as exc:  # noqa: BLE001 - report, never crash on learner input
        findings.add("B01", f"scope.json unreadable: {exc}")
        return findings, stats

    # ---- Stage 1: authorized scope -------------------------------------
    if scope.get("authorization") != "written":
        findings.add("B02", f"authorization={scope.get('authorization')!r}, expected 'written'")

    missing = [
        key
        for key in ("program", "policy_url", "authorized_by", "authorized_at", "expires_at")
        if not isinstance(scope.get(key), str) or not scope.get(key).strip()
    ]
    if missing:
        findings.add("B03", "missing/degenerate fields: " + ", ".join(missing))

    policy_url = scope.get("policy_url")
    if isinstance(policy_url, str) and policy_url.strip():
        parsed = urlparse(policy_url)
        if parsed.scheme not in ("http", "https") or not parsed.netloc:
            findings.add("B04", f"policy_url is not an http(s) URL: {policy_url!r}")
        elif parsed.path in ("", "/") and not parsed.fragment:
            findings.add("B04", f"policy_url is a bare homepage: {policy_url!r}")

    dates: dict[str, _dt.date] = {}
    for key in ("authorized_at", "expires_at"):
        value = scope.get(key)
        if isinstance(value, str):
            try:
                dates[key] = _dt.date.fromisoformat(value)
            except ValueError:
                findings.add("B03", f"{key} is not YYYY-MM-DD: {value!r}")
    if "expires_at" in dates and dates["expires_at"] < as_of:
        findings.add("B05", f"scope expired {dates['expires_at']} before as-of {as_of}")
    if "authorized_at" in dates and dates["authorized_at"] > as_of:
        findings.add("B05", f"authorization dated {dates['authorized_at']} after as-of {as_of}")

    if scope.get("live_target_activity") is not False:
        findings.add("B06", "live_target_activity must be false for this province")
    methods = scope.get("methods")
    if not isinstance(methods, list) or not methods:
        findings.add("B06", "methods is not a non-empty list")
        methods = []
    else:
        bad_methods = [
            m
            for m in methods
            if not isinstance(m, str) or any(term in m.casefold() for term in LIVE_TERMS)
        ]
        if bad_methods:
            findings.add("B06", f"live/dynamic methods declared: {bad_methods}")

    artifacts = scope.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        findings.add("B09", "no artifact declared in scope")
        artifacts = []
    declared: dict[str, str] = {}
    bound = 0
    for index, artifact in enumerate(artifacts):
        if not isinstance(artifact, dict):
            findings.add("B07", f"artifact[{index}] is not an object")
            continue
        rel = artifact.get("path")
        digest = artifact.get("sha256")
        if artifact.get("provenance") not in PROVENANCE:
            findings.add(
                "B08",
                f"artifact[{index}] provenance={artifact.get('provenance')!r} not in {PROVENANCE}",
            )
        if not isinstance(rel, str) or not rel:
            findings.add("B07", f"artifact[{index}] has no path")
            continue
        candidate = (package / rel).resolve()
        try:
            candidate.relative_to(package.resolve())
        except ValueError:
            findings.add("B07", f"artifact path escapes package: {rel!r}")
            continue
        if not candidate.is_file():
            findings.add("B07", f"artifact missing: {rel}")
            continue
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            findings.add("B07", f"artifact[{index}] sha256 is not 64 lowercase hex")
            continue
        actual = sha256_bytes(candidate.read_bytes())
        if actual != digest:
            findings.add("B07", f"artifact digest mismatch for {rel}: declared {digest}, actual {actual}")
            continue
        declared[digest] = rel
        bound += 1
    stats["artifacts"] = bound

    # ---- Stage 3: evidence ledger ---------------------------------------
    ledger_path = package / "ledger.md"
    rows: list[dict[str, str]] = []
    if not ledger_path.is_file():
        findings.add("L01", "ledger.md missing")
    else:
        rows, malformed = parse_ledger(ledger_path.read_text(encoding="utf-8"))
        for lineno in malformed:
            findings.add("L02", f"ledger row at line {lineno} does not have 5 cells")
        for row in rows:
            if row["layer"] not in LAYERS:
                findings.add("L03", f"{row['id']} layer={row['layer']!r} not in {LAYERS}")
            if row["digest"] not in declared:
                findings.add("L04", f"{row['id']} cites undeclared digest {row['digest']}")
            if row["layer"] == "observation" and row["command"] in ("", "—", "-"):
                findings.add("L05", f"{row['id']} is an observation with no deriving command")
        if not any(row["layer"] == "observation" for row in rows):
            findings.add("L06", "ledger holds no observation row")
    stats["ledger_rows"] = len(rows)
    stats["layers"] = {
        layer: sum(1 for row in rows if row["layer"] == layer) for layer in LAYERS
    }
    ids = {row["id"] for row in rows}

    # ---- Stage 4: report quality ----------------------------------------
    report_path = package / "report.md"
    if not report_path.is_file():
        findings.add("R01", "report.md missing")
        return findings, stats
    report_text = report_path.read_text(encoding="utf-8")
    sections = parse_sections(report_text)
    missing_sections = [name for name in REQUIRED_SECTIONS if name not in sections]
    if missing_sections:
        findings.add("R01", "missing sections: " + ", ".join(missing_sections))
    stats["sections"] = len(REQUIRED_SECTIONS) - len(missing_sections)

    scope_body = sections.get("scope", "")
    if isinstance(scope.get("program"), str) and scope["program"].casefold() not in scope_body.casefold():
        findings.add("R02", "Scope section does not name the program")
    if isinstance(policy_url, str) and policy_url not in scope_body:
        findings.add("R02", "Scope section does not carry the policy_url")

    identity = sections.get("artifact identity", "")
    for digest, rel in declared.items():
        if digest not in identity:
            findings.add("R09", f"Artifact identity does not carry {rel} digest")
        if rel not in identity:
            findings.add("R09", f"Artifact identity does not carry path {rel}")

    method_body = sections.get("method", "")
    if methods and not any(m in method_body for m in methods if isinstance(m, str)):
        findings.add("R10", "Method section names no method declared in scope")

    cited = {match.group(0) for match in EVIDENCE_ID.finditer(report_text)}
    if not cited:
        findings.add("R03", "report cites no evidence id")
    for evidence_id in sorted(cited, key=lambda value: int(value[1:])):
        if evidence_id not in ids:
            findings.add("R11", f"report cites {evidence_id}, absent from the ledger")

    impact_body = sections.get("impact", "")
    for line in impact_body.splitlines():
        entry = line.strip().lstrip("-*0123456789. ").strip()
        if not entry:
            continue
        folded = entry.casefold()
        if not EVIDENCE_ID.search(entry) and "unknown" not in folded and "not assessed" not in folded:
            findings.add("R04", f"Impact line lacks evidence/unknown: {entry[:80]!r}")

    for name, pattern in OVERCLAIM.items():
        if pattern.search(report_text):
            findings.add("R05", f"overclaim phrase present: {name!r}")

    if not sections.get("limitations", "").strip():
        findings.add("R06", "Limitations section is empty")

    disclosure = sections.get("disclosure", "")
    contact = scope.get("disclosure", {}).get("contact") if isinstance(scope.get("disclosure"), dict) else None
    window = scope.get("disclosure", {}).get("window_days") if isinstance(scope.get("disclosure"), dict) else None
    if not isinstance(contact, str) or contact not in disclosure:
        findings.add("R07", "Disclosure section lacks the program contact")
    if window is None or str(window) not in disclosure:
        findings.add("R07", "Disclosure section lacks the disclosure window")

    stop_body = sections.get("stop conditions", "")
    if not re.search(r"none triggered|no stop condition|STOP:", stop_body, re.I):
        findings.add("R08", "Stop conditions section records no decision ('none triggered' or 'STOP:')")

    return findings, stats


def run_self_test() -> int:
    """Build synthetic packages and assert every detector fires on a case built for it."""
    clean_scope = {
        "program": "Synthetic Program",
        "policy_url": "https://policy.example.test/program#scope",
        "authorization": "written",
        "authorized_by": "triage-roster",
        "authorized_at": "2026-10-01",
        "expires_at": "2026-12-31",
        "methods": ["static-artifact-analysis"],
        "live_target_activity": False,
        "artifacts": [{"path": "artifacts/a.zip", "sha256": "", "provenance": "authored"}],
        "disclosure": {"window_days": 90, "contact": "security@example.test"},
    }
    clean_ledger = (
        "# ledger\n\n"
        "| id | artifact_sha256 | layer | statement | command |\n"
        "|---|---|---|---|---|\n"
        "| E1 | {digest} | observation | digest bound | `sha256sum artifacts/a.zip` |\n"
        "| E2 | {digest} | inference | maybe | — |\n"
        "| E3 | {digest} | unknown | not tested | — |\n"
    )
    clean_report = """# report

## Scope
Synthetic Program at https://policy.example.test/program#scope.

## Artifact identity
`artifacts/a.zip` sha256 {digest}.

## Method
static-artifact-analysis only.

## Evidence
E1, E2, E3.

## Reproduction
sha256sum artifacts/a.zip

## Impact
- The archive declares one member (E1).

## Limitations
One authored artifact only.

## Stop conditions
None triggered.

## Disclosure
security@example.test, 90 days.
"""

    def build(root: Path, mutate=None) -> Path:
        package = root / "package"
        (package / "artifacts").mkdir(parents=True)
        payload = b"PK\x05\x06" + b"\x00" * 18
        (package / "artifacts" / "a.zip").write_bytes(payload)
        digest = sha256_bytes(payload)
        scope = json.loads(json.dumps(clean_scope))
        scope["artifacts"][0]["sha256"] = digest
        ledger = clean_ledger.format(digest=digest)
        report = clean_report.format(digest=digest)
        if mutate is not None:
            scope, ledger, report = mutate(scope, ledger, report, digest)
        (package / "scope.json").write_text(json.dumps(scope), encoding="utf-8")
        (package / "ledger.md").write_text(ledger, encoding="utf-8")
        (package / "report.md").write_text(report, encoding="utf-8")
        return package

    def mutate_scope(**changes):
        def apply(scope, ledger, report, digest):
            scope.update(changes)
            return scope, ledger, report

        return apply

    cases = [
        ("clean", None, None),
        ("B01", None, "B01"),
        ("B02", mutate_scope(authorization="verbal"), "B02"),
        ("B03", mutate_scope(program=""), "B03"),
        ("B04", mutate_scope(policy_url="https://policy.example.test/"), "B04"),
        ("B05", mutate_scope(expires_at="2026-10-01"), "B05"),
        ("B06", mutate_scope(live_target_activity=True), "B06"),
        ("B07", None, "B07"),
        ("B08", mutate_scope(artifacts=[{"path": "artifacts/a.zip", "sha256": "X", "provenance": "vendor"}]), "B08"),
        ("B09", mutate_scope(artifacts=[]), "B09"),
        ("L01", None, "L01"),
        ("L02", lambda s, l, r, d: (s, l + "| E4 | " + d + " | observation | extra cell | cmd | sixth |\n", r), "L02"),
        ("L03", lambda s, l, r, d: (s, l.replace("| observation |", "| guess |"), r), "L03"),
        ("L04", lambda s, l, r, d: (s, l.replace("| E1 | " + d + " |", "| E1 | " + "f" * 64 + " |"), r), "L04"),
        ("L05", lambda s, l, r, d: (s, l.replace("`sha256sum artifacts/a.zip`", "—"), r), "L05"),
        ("L06", lambda s, l, r, d: (s, l.replace("| observation |", "| inference |"), r), "L06"),
        ("R01", lambda s, l, r, d: (s, l, r.replace("## Disclosure", "## Closing")), "R01"),
        ("R02", lambda s, l, r, d: (s, l, r.replace("Synthetic Program at https://policy.example.test/program#scope.", "The program policy applies.")), "R02"),
        ("R03", lambda s, l, r, d: (s, l, re.sub(r"\bE[0-9]{1,4}\b", "the ledger", r)), "R03"),
        ("R04", lambda s, l, r, d: (s, l, r.replace("- The archive declares one member (E1).", "- The archive is dangerous.")), "R04"),
        ("R05", lambda s, l, r, d: (s, l, r.replace("One authored artifact only.", "Full compromise is guaranteed.")), "R05"),
        ("R06", lambda s, l, r, d: (s, l, r.replace("One authored artifact only.", "")), "R06"),
        ("R07", lambda s, l, r, d: (s, l, r.replace("security@example.test, 90 days.", "Program channel.")), "R07"),
        ("R08", lambda s, l, r, d: (s, l, r.replace("None triggered.", "Not reviewed.")), "R08"),
        ("R09", lambda s, l, r, d: (s, l, r.replace("`artifacts/a.zip` sha256 " + d, "`artifacts/a.zip` sha256")), "R09"),
        ("R10", lambda s, l, r, d: (s, l, r.replace("static-artifact-analysis only.", "Manual review.")), "R10"),
        ("R11", lambda s, l, r, d: (s, l, r.replace("E1, E2, E3.", "E1, E2, E3, E9.")), "R11"),
    ]

    def corrupt_scope(package: Path) -> None:
        (package / "scope.json").write_text("{ not json", encoding="utf-8")

    def tamper_artifact(package: Path) -> None:
        (package / "artifacts" / "a.zip").write_bytes(b"tampered")

    def drop_ledger(package: Path) -> None:
        (package / "ledger.md").unlink()

    specials = {"B01": corrupt_scope, "B07": tamper_artifact, "L01": drop_ledger}

    failures = 0
    detectors = 0
    with tempfile.TemporaryDirectory(prefix="bounty-triage-selftest-") as tmp:
        root = Path(tmp)
        for index, (name, mutate, expected) in enumerate(cases):
            case_root = root / f"case-{index}"
            case_root.mkdir()
            package = build(case_root)
            if name in specials:
                specials[name](package)
            elif mutate is not None:
                scope = json.loads((package / "scope.json").read_text(encoding="utf-8"))
                ledger = (package / "ledger.md").read_text(encoding="utf-8")
                report = (package / "report.md").read_text(encoding="utf-8")
                digest = scope["artifacts"][0]["sha256"] if scope.get("artifacts") else ""
                scope, ledger, report = mutate(scope, ledger, report, digest)
                (package / "scope.json").write_text(json.dumps(scope), encoding="utf-8")
                (package / "ledger.md").write_text(ledger, encoding="utf-8")
                (package / "report.md").write_text(report, encoding="utf-8")
            findings, _ = validate(package, _dt.date(2026, 10, 27))
            codes = findings.codes()
            if expected is None:
                if codes:
                    failures += 1
                    print(f"self-test: clean case emitted {sorted(codes)}")
                continue
            detectors += 1
            if expected not in codes:
                failures += 1
                print(f"self-test: detector {expected} did not fire (got {sorted(codes)})")
    if failures:
        print(f"self-test: {failures} failure(s)")
        print("VERDICT=FAIL")
        return 1
    print(f"self-test: {detectors}/{detectors} detectors fired as expected")
    print("self-test: clean package PASS")
    print("VERDICT=PASS")
    return 0


class Parser(argparse.ArgumentParser):
    def error(self, message: str) -> None:  # usage errors use the lane's 64
        self.print_usage(sys.stderr)
        print(f"error: {message}", file=sys.stderr)
        raise SystemExit(64)


def main(argv: list[str]) -> int:
    parser = Parser(add_help=True)
    parser.add_argument("--package", type=Path)
    parser.add_argument("--as-of", default=None)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)

    if args.self_test:
        return run_self_test()
    if args.package is None:
        parser.error("--package or --self-test is required")
    as_of = _dt.date.today()
    if args.as_of:
        try:
            as_of = _dt.date.fromisoformat(args.as_of)
        except ValueError:
            parser.error(f"--as-of is not YYYY-MM-DD: {args.as_of!r}")
    package = args.package.resolve()
    if not package.is_dir():
        print(f"package is not a directory: {package}", file=sys.stderr)
        print("VERDICT=ERROR")
        return 2

    findings, stats = validate(package, as_of)
    ordered = findings.sorted()
    if args.json:
        print(
            json.dumps(
                {
                    "package": str(package),
                    "as_of": as_of.isoformat(),
                    "stats": stats,
                    "findings": [{"code": code, "detail": detail} for code, detail in ordered],
                    "verdict": "FAIL" if ordered else "PASS",
                },
                indent=2,
            )
        )
    else:
        print(f"package: {package}")
        print(f"as-of: {as_of.isoformat()}")
        print(f"artifacts: {stats.get('artifacts', 0)} digest-bound")
        layers = stats.get("layers", {})
        print(
            "ledger: {n} rows (observation={o} inference={i} unknown={u})".format(
                n=stats.get("ledger_rows", 0),
                o=layers.get("observation", 0) if isinstance(layers, dict) else 0,
                i=layers.get("inference", 0) if isinstance(layers, dict) else 0,
                u=layers.get("unknown", 0) if isinstance(layers, dict) else 0,
            )
        )
        print(f"report: {stats.get('sections', 0)}/{len(REQUIRED_SECTIONS)} sections")
        print(f"findings: {len(ordered)}")
        for code, detail in ordered:
            print(f"  {code} {detail}")
        print("VERDICT=" + ("FAIL" if ordered else "PASS"))
    return 1 if ordered else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
