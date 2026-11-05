#!/usr/bin/env python3
"""M21 census-line check (round 100, seat ExecControlsR100).

Given a round report (--report) and the census log it cites (--log, as
printed by scripts/sources-census.sh validate), require the report's
census line(s) to name every warning/error class the log contains, with
that class's exact count.

Log records: one per line, tab-separated, the class being a tab-delimited
field like `\\tW04\\t` (codes W01..W99 / E01..E99); the trailing
`# rc=... cmd=...` comment line carries no records.

Report census line(s): lines mentioning `census` (case-insensitive) that
carry at least one count token, where a count token is `<n> × <CODE>`
(the multiplication sign may also be written x, X or *) or
`<n> <CODE>-codes`. EVERY census line that reports counts must name
EVERY class with count > 0 in the log with exactly that count, so a
summary line that omits a class (round 99's after-census dropped
`13 × W04`) fails the check; a wrong count is as good as omitted.

Prints `CENSUS_LINE_CHECK=pass|fail missing=<classes>` (classes sorted,
comma-separated, `none` when the check passes). Exit 0 pass, 1 fail,
2 usage / unreadable inputs.

Usage:
    PYTHONUTF8=1 python3 -B census_line_check.py --report <md> --log <census log>
"""
import argparse
import re
import sys

CODE_FIELD = re.compile(r"\t([WE]\d{2})\t")
COUNT_TOKEN = re.compile(
    r"(\d+)\s*[×xX*]\s*([WE]\d{2})"        # 21 × W01 / 13 x W04 / 3*E03
    r"|(\d+)\s*([WE]\d{2})-?\s*codes?\b"   # 0 E-codes / 2 W01 codes
)
CENSUS_HINT = re.compile(r"census", re.IGNORECASE)


def log_class_counts(text):
    counts = {}
    for line in text.splitlines():
        for m in CODE_FIELD.finditer(line):
            counts[m.group(1)] = counts.get(m.group(1), 0) + 1
    return {code: n for code, n in counts.items() if n > 0}


def census_line_tokens(line):
    """(has_count_token, {code: [counts named on this line]})."""
    named = {}
    hit = False
    for m in COUNT_TOKEN.finditer(line):
        count = int(m.group(1) if m.group(1) is not None else m.group(3))
        code = m.group(2) if m.group(2) is not None else m.group(4)
        named.setdefault(code, []).append(count)
        hit = True
    return hit, named


def main():
    ap = argparse.ArgumentParser(description="check report census lines against a census log")
    ap.add_argument("--report", required=True, help="round report markdown")
    ap.add_argument("--log", required=True, help="census log (sources-census validate output)")
    args = ap.parse_args()
    try:
        with open(args.log, "r", encoding="utf-8", errors="replace") as fh:
            log_text = fh.read()
        with open(args.report, "r", encoding="utf-8", errors="replace") as fh:
            report_text = fh.read()
    except OSError as exc:
        print(f"census_line_check: cannot read inputs: {exc}", file=sys.stderr)
        sys.exit(2)

    required = log_class_counts(log_text)
    missing = set()
    census_lines = 0
    for line in report_text.splitlines():
        if not CENSUS_HINT.search(line):
            continue
        has_token, named = census_line_tokens(line)
        if not has_token:
            continue
        census_lines += 1
        for code, want in required.items():
            if want not in named.get(code, []):
                missing.add(code)
    if required and census_lines == 0:
        missing = set(required)

    if missing:
        print("CENSUS_LINE_CHECK=fail missing=" + ",".join(sorted(missing)))
        sys.exit(1)
    print("CENSUS_LINE_CHECK=pass missing=none")
    sys.exit(0)


if __name__ == "__main__":
    main()
