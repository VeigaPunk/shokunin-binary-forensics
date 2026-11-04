#!/usr/bin/env python3
"""MutR90Oracle mutation harness (scratch-only). Pristine -> mutant -> restored per mutant."""
import copy, hashlib, json, os, subprocess, sys
from pathlib import Path

S = Path("/fast/scratch/hyaku/revenger-r90/MutR90Oracle")
LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
BATTERY = LANE / "reports/round-90/oracle_battery.py"
TRUTH = LANE / "corpus/fixtures/apk-r65/truth.json"
ORC = S / "apk-r65/oracle_check2.py"
NE = S / "ne/norm_eq.py"
ENV = {**os.environ, "TMPDIR": str(S)}
sha = lambda b: hashlib.sha256(b).hexdigest()

ORACLE_MUTANTS = [
    ("O1", "drop root-tag check",
     'if root is not None and local(root.tag) == "manifest"', 'if root is not None'),
    ("O2", "accept a package attr equal to the authored one on ANY element",
     'root_pkg = [v for k, v in attrs if k == "package"]',
     '_any = [v for e in (root.iter() if root is not None else []) for k, v in e.attrib.items() if local(k) == "package"]; root_pkg = [pkg] if pkg in _any else _any'),
    ("O3", "`in` instead of `== [val]` for versions",
     'if got == [val]', 'if val in got'),
    ("O4", "skip package_name == parsed root package leg",
     'if root_pkg and nr.get("package_name") == root_pkg[0]', 'if True'),
    ("O5", "fall back to substring/regex attrs on parse error",
     '        root = None\n    local',
     '        root = ET.fromstring(("<manifest " + " ".join(re.findall(r\'\\w+="[^"]*"\', text)) + "/>").encode())\n    local'),
    ("O6", "ignore namespace-local split (raw {uri}name keys)",
     'local = lambda k: k.rsplit("}", 1)[-1]', 'local = lambda k: k'),
    ("O7", "versions read from any element (root.iter)",
     'got = [v for k, v in attrs if k == attr]',
     'got = [v for e in root.iter() for k, v in e.attrib.items() if local(k) == attr] if root is not None else []'),
    ("O8", "drop root package == [pkg] leg",
     'if root_pkg == [pkg]', 'if True'),
    ("O9", "drop record package_name == authored leg",
     'if nr.get("package_name") == pkg', 'if True'),
    ("O10", "first-match only for versions (got[:1])",
     'if got == [val]', 'if got[:1] == [val]'),
    ("O11", "drop manifest status complete leg",
     'if (nr.get("manifest") or {}).get("status") == "complete"', 'if True'),
    ("O12", "drop subject digest == fixture sha256 leg",
     'if (subj.get("digest") or {}).get("sha256") == truth["image"]["sha256"]', 'if True'),
    ("O13", "drop BOTH package_name legs (O4+O9): record package_name never compared",
     ('if nr.get("package_name") == pkg', 'if root_pkg and nr.get("package_name") == root_pkg[0]'), ('if True', 'if True')),
]

NORM_MUTANTS = [
    ("N1", "drop V3 canonicalisation of JSON-text strings",
     'if s[:1] in "{[":', 'if False:'),
    ("N2", "normalise every ev_<64hex> substring",
     'return RUNTIME.sub("<RUNTIME>/rea-android-X", x)',
     'return re.sub(r"ev_[0-9a-f]{64}", "<EVIDENCE_ID>", RUNTIME.sub("<RUNTIME>/rea-android-X", x))'),
    ("N3", "drop every key ending _ms",
     'if k not in DROP_KEYS}', 'if k not in DROP_KEYS and not k.endswith("_ms")}'),
    ("N4", "ignore list length",
     'if len(a) != len(b):', 'if False:'),
    ("N5", "normalise run2 with run1's evidence id",
     'norm(r2, r2.get("evidence_id"))', 'norm(r2, r1.get("evidence_id"))'),
    ("N6", "compare key intersection only (extra keys ignored)",
     'for k in sorted(set(a) | set(b)):', 'for k in sorted(set(a) & set(b)):'),
    ("N7", "V1 widened to any string starting ev_",
     'if evid and x == evid:', 'if evid and x.startswith("ev_"):'),
    ("N8", "V2 widened to any trailing path segment",
     'RUNTIME = re.compile(r"[^\\"\\s]*/rea-android-[A-Za-z0-9_]+")',
     'RUNTIME = re.compile(r"[^\\"\\s]*/[A-Za-z0-9_-]+")'),
    ("N9", "V3 keeps only keys of JSON-text payloads",
     'return {"<json-text>": norm(json.loads(s), evid)}',
     'return {"<json-text>": sorted(json.loads(s)) if isinstance(json.loads(s), dict) else None}'),
    ("N10", "drop the type(a) is not type(b) check",
     'if type(a) is not type(b):', 'if False:'),
]


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, cwd=S)
    return p.returncode, p.stdout


def battery(tag):
    d = S / "battery-runs" / tag
    rc, out = run([sys.executable, "-B", str(BATTERY), "--oracle", str(ORC), "--write", str(d)])
    return rc, out


def selftest():
    return run([sys.executable, "-B", str(NE), "--selftest"])


def apply(path, old, new):
    src = path.read_bytes()
    t = src.decode()
    olds, news = (old, new) if isinstance(old, tuple) else ((old,), (new,))
    for o, n in zip(olds, news):
        assert t.count(o) == 1, (path, o, t.count(o))
        t = t.replace(o, n)
    path.write_bytes(t.encode())
    return src


def probe(path, mutants, detector, kind):
    pristine = path.read_bytes()
    h0 = sha(pristine)
    rc0, out0 = detector(f"{kind}-pristine")
    rows = []
    for mid, desc, old, new in mutants:
        try:
            apply(path, old, new)
            hm = sha(path.read_bytes())
            rcm, outm = detector(f"{mid}-mutant")
        finally:
            path.write_bytes(pristine)
        hr = sha(path.read_bytes())
        rcr, outr = detector(f"{mid}-restored")
        bad = [l for l in outm.splitlines() if "MISCLASS" in l and not l.startswith("ORACLE_MISCLASS")] if kind == "oracle" \
            else [l for l in outm.splitlines() if l.endswith("=FAIL") and not l.startswith("NORM_SELFTEST=")]
        if rc0 != 0 or rcr != 0 or outr != out0:
            verdict = "inconclusive"
        else:
            verdict = "killed" if rcm != 0 else "survived"
        rows.append(dict(id=mid, desc=desc, old=old, new=new, mutant_sha=hm, restored_sha=hr,
                         restored_ok=hr == h0, rc_mutant=rcm, out_mutant=outm, rc_restored=rcr,
                         out_restored_equals_pristine=outr == out0, killers=bad, verdict=verdict))
    return dict(pristine_sha=h0, rc_pristine=rc0, out_pristine=out0, rows=rows)


# ---- direct killer probes for survivors -------------------------------------
P1 = json.loads((LANE / "reports/round-90/oracle-battery-cases/P1-real-r89-record.json").read_text())
GOOD = P1["normalized_result"]["manifest"]["text"]
NS = 'xmlns:android="http://schemas.android.com/apk/res/android"'


def rec(text=None, status=None, digest=None):
    r = copy.deepcopy(P1)
    if text is not None:
        r["normalized_result"]["manifest"]["text"] = text
    if status is not None:
        r["normalized_result"]["manifest"]["status"] = status
    if digest is not None:
        r["subject"]["digest"]["sha256"] = digest
    return r


ORACLE_KILLERS = {  # mutant -> (case id, label, record)
    "O1": ("K-O1-root-is-application", "reject", rec(GOOD.replace("<manifest ", "<application "))),
    "O2": ("K-O2-attacker-root-authored-pkg-in-child", "reject", rec(
        '<?xml version="1.0" encoding="utf-8"?>\n<manifest ' + NS + ' package="com.attacker.fabricated"'
        ' xmlns:ns1="android" ns1:versionCode="1" ns1:versionName="1.0">'
        '<application package="com.example.r65"/></manifest>')),
    "O8": ("K-O8-second-namespaced-package-on-root", "reject", rec(GOOD.replace(
        'ns2:versionName="1.0"/>', 'ns2:versionName="1.0"\n    xmlns:ns9="other" ns9:package="com.attacker.fabricated"/>'))),
    "O11": ("K-O11-manifest-status-partial", "reject", rec(status="partial")),
    "O12": ("K-O12-subject-digest-other-apk", "reject", rec(digest="0" * 64)),
    "O4": ("K-O4-none-possible (equivalence witness: battery F7)", "reject", rec(GOOD.replace("com.example.r65", "com.example.r66"))),
    "O9": ("K-O9-none-possible (equivalence witness: battery F2)", "reject", None),
    "O13": ("K-O13-package_name-forged-root-true", "reject",
            {**P1, "normalized_result": {**P1["normalized_result"], "package_name": "com.attacker.fabricated"}}),
}

EV = lambda c: "ev_" + c * 64
NE_BASE = {"evidence_id": EV("a"), "p": "/s/x/rea-android-ab12cd/target.apk", "n": {"package_name": "com.example.r65"}}
NE_TWIN = {**NE_BASE, "evidence_id": EV("b"), "p": "/s/x/rea-android-zz99yy/target.apk"}
NORM_KILLERS = {  # mutant -> (case id, run1, run2) ; expected pristine verdict DIFFER (exit 1)
    "N3": ("K-N3-nonvolatile-timeout_ms-differs", {**NE_BASE, "timeout_ms": 1000}, {**NE_TWIN, "timeout_ms": 5000}),
    "N4": ("K-N4-list-gains-an-element", {**NE_BASE, "permissions": []}, {**NE_TWIN, "permissions": ["android.permission.INTERNET"]}),
    "N7": ("K-N7-foreign-ev-id-field-differs", {**NE_BASE, "parent_evidence_id": EV("c")}, {**NE_TWIN, "parent_evidence_id": EV("d")}),
    "N8": ("K-N8-target-filename-differs-under-runtime", {**NE_BASE, "p": "/s/x/rea-android-ab12cd/a.apk"}, {**NE_TWIN, "p": "/s/x/rea-android-zz99yy/b.apk"}),
    "N10": ("K-N10-int-vs-bool-leaf", {**NE_BASE, "class_count": 1}, {**NE_TWIN, "class_count": True}),
    "N9": ("K-N9-text-payload-value-only-same-keys",
           {**NE_BASE, "t": json.dumps({"x": 1, "y": 2})}, {**NE_TWIN, "t": json.dumps({"y": 2, "x": 9})}),
}


def killer_probe(path, mutants, survivors, killers, kind):
    out = []
    md = {m[0]: m for m in mutants}
    pristine = path.read_bytes()
    for mid in survivors:
        if mid not in killers or killers[mid][-1] is None:
            continue
        cid = killers[mid][0]
        d = S / "cases" / cid
        d.mkdir(parents=True, exist_ok=True)
        if kind == "oracle":
            label, body = killers[mid][1], killers[mid][2]
            (d / "case.json").write_text(json.dumps(body, indent=2) + "\n")
            cmd = [sys.executable, "-B", str(path), str(TRUTH), str(d / "case.json")]
        else:
            label = "DIFFER"
            (d / "run1.json").write_text(json.dumps(killers[mid][1], indent=2) + "\n")
            (d / "run2.json").write_text(json.dumps(killers[mid][2], indent=2) + "\n")
            cmd = [sys.executable, "-B", str(path), str(d / "run1.json"), str(d / "run2.json")]
        rp, op = run(cmd)
        try:
            apply(path, md[mid][2], md[mid][3])
            rm, om = run(cmd)
        finally:
            path.write_bytes(pristine)
        rr, orr = run(cmd)
        out.append(dict(mutant=mid, case=cid, label=label, rc_pristine=rp, rc_mutant=rm, rc_restored=rr,
                        last_pristine=op.strip().splitlines()[-1] if op.strip() else "",
                        last_mutant=om.strip().splitlines()[-1] if om.strip() else "",
                        fail_lines_pristine=[l for l in op.splitlines() if "FAIL" in l or l.startswith("DIFF")],
                        kills=(rp == 1 and rm == 0 and rr == 1),
                        restored_ok=sha(path.read_bytes()) == sha(pristine)))
    return out


if __name__ == "__main__":
    o = probe(ORC, ORACLE_MUTANTS, battery, "oracle")
    n = probe(NE, NORM_MUTANTS, lambda tag: selftest(), "norm")
    ok_ = killer_probe(ORC, ORACLE_MUTANTS, [r["id"] for r in o["rows"] if r["verdict"] == "survived"], ORACLE_KILLERS, "oracle")
    nk = killer_probe(NE, NORM_MUTANTS, [r["id"] for r in n["rows"] if r["verdict"] == "survived"], NORM_KILLERS, "norm")
    res = dict(oracle=o, norm=n, oracle_killers=ok_, norm_killers=nk)
    (S / "results.json").write_text(json.dumps(res, indent=2) + "\n")
    for k in ("oracle", "norm"):
        print(k, "pristine rc", res[k]["rc_pristine"], res[k]["pristine_sha"][:16])
        for r in res[k]["rows"]:
            print(f" {r['id']:4} {r['verdict']:12} rc={r['rc_mutant']} restored={r['restored_ok']} killers={r['killers']}")
    for r in ok_ + nk:
        print(" KILLER", r["mutant"], r["case"], "pristine", r["rc_pristine"], "mutant", r["rc_mutant"], "restored", r["rc_restored"], "kills", r["kills"])
