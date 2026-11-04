#!/usr/bin/env python3
"""Sensitivity scan of a producer record (read-only). Usage: scan.py FILE..."""
import json, os, re, sys

SCRATCH = "/fast/scratch/hyaku/revenger-r90/"
ENV_SKIP = {"PWD", "OLDPWD", "SHLVL", "_", "TERM", "LANG", "LC_ALL", "SHELL", "COLUMNS", "LINES"}
PATS = {
    "home-path": re.compile(r"/(?:home|root|Users)/[A-Za-z0-9._-]+"),
    "run-user": re.compile(r"/run/user/\d+[^\s\"']*"),
    "username": re.compile(r"\bvgpnk\b"),
    "ipv4": re.compile(r"(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])"),
    "ipv6": re.compile(r"\b(?:[0-9a-fA-F]{1,4}:){3,7}[0-9a-fA-F]{1,4}\b"),
    "url-host": re.compile(r"https?://[^/\s\"']+"),
    "fqdn-local": re.compile(r"\b[A-Za-z0-9-]+\.(?:local|lan|internal|home|corp)\b"),
    "aws-key": re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
    "gh-token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    "slack/openai/anthropic": re.compile(r"\b(?:xox[abpr]-[A-Za-z0-9-]+|sk-[A-Za-z0-9_-]{20,}|sk-ant-[A-Za-z0-9_-]+)"),
    "jwt": re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]+"),
    "pem": re.compile(r"-----BEGIN [A-Z ]*(?:PRIVATE KEY|CERTIFICATE)-----"),
    "kv-secret": re.compile(r"(?i)\b(?:password|passwd|secret|token|api[_-]?key|auth|bearer|credential)\b\s*[:=]"),
    "env-assign": re.compile(r"\b[A-Z][A-Z0-9_]{2,}=[^\s\"']+"),
    "email": re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.]+\b"),
}


def walk(x, p="$"):
    if isinstance(x, dict):
        for k, v in x.items():
            yield p + "." + k + "{key}", k
            yield from walk(v, p + "." + k)
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from walk(v, f"{p}[{i}]")
    elif isinstance(x, str):
        yield p, x
        s = x.strip()
        if s[:1] in "{[":
            try:
                yield from walk(json.loads(s), p + "<json>")
            except ValueError:
                pass
    else:
        yield p, x


def main():
    host = os.uname().nodename
    envvals = {k: v for k, v in os.environ.items() if k not in ENV_SKIP and len(v) >= 6}
    rc = 0
    for f in sys.argv[1:]:
        raw = open(f, "rb").read()
        print(f"== {f} bytes={len(raw)} nonascii={sum(b > 127 for b in raw)} ctl={sum(b < 32 and b not in (9, 10, 13) for b in raw)}")
        d = json.loads(raw)
        hits = 0
        for p, v in walk(d):
            if not isinstance(v, str):
                continue
            for name, rx in PATS.items():
                for m in rx.finditer(v):
                    tok = m.group(0)
                    tag = "(in-scratch)" if name in ("home-path",) and False else ""
                    print(f"HIT {name} {p} :: {tok!r} {tag}")
                    hits += 1
            if host and host in v:
                print(f"HIT hostname({host}) {p}"); hits += 1
            for k, ev in envvals.items():
                if ev in v and ev not in ("/home/vgpnk",):
                    print(f"HIT envval {k} {p} :: {ev[:80]!r}"); hits += 1
            for m in re.finditer(r"/[^\s\"'<>]+", v):
                path = m.group(0)
                if path.count("/") >= 2 and not path.startswith(SCRATCH) and not path.startswith("/rea-android"):
                    print(f"PATH-outside-scratch {p} :: {path!r}"); hits += 1
        print(f"TOTAL_HITS={hits}")
        rc |= bool(hits)
    return rc


sys.exit(main())
