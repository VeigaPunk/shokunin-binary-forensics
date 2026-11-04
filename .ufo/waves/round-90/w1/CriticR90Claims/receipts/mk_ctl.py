import json, hashlib, shutil, sys, secrets
from pathlib import Path
S = Path(sys.argv[1]); mode = sys.argv[2]; dst = S / f"ctl-{mode}"
if dst.exists(): shutil.rmtree(dst)
shutil.copytree(S / "freeze", dst)
def sub(x, old, new):
    if isinstance(x, dict): return {k: sub(v, old, new) for k, v in x.items()}
    if isinstance(x, list): return [sub(v, old, new) for v in x]
    return new if x == old else x
if mode in ("idedit", "c2only"):
    src = dst / "reports/round-89/rejected-android-record/inspection.json"
    rec = json.loads(src.read_text()); old = rec["evidence_id"]
    runs = []
    for p in (dst / "corpus/live/runs/round-90/inspection.json", dst / "reports/round-90/android-run2.json"):
        p.parent.mkdir(parents=True, exist_ok=True)
        r = sub(rec, old, "ev_" + secrets.token_hex(32))
        b = (json.dumps(r, indent=2) + "\n").encode(); p.write_bytes(b)
        runs.append({"stdout_sha256": hashlib.sha256(b).hexdigest()})
elif mode == "stub":
    for rel, body in [("reports/round-81/f_probe4.py", 'print("F4_COVERAGE=11/11 score=10.00")'),
                      ("corpus/fixtures/apk-r65/oracle_check2.py", 'print("ORACLE OK (stub)")'),
                      ("reports/round-90/oracle_battery.py", 'print("ORACLE_MISCLASS=0/9")'),
                      ("reports/round-90/norm_eq.py", 'print("NORM_EQ=identical")')]:
        (dst / rel).write_text(body + "\n")
    runs = []
    for i, p in enumerate((dst / "corpus/live/runs/round-90/inspection.json", dst / "reports/round-90/android-run2.json")):
        p.parent.mkdir(parents=True, exist_ok=True)
        b = json.dumps({"evidence_id": f"ev_stub{i}"}).encode(); p.write_bytes(b)
        runs.append({"stdout_sha256": hashlib.sha256(b).hexdigest()})
if mode in ("idedit", "c2only", "stub"):
    (dst / "reports/round-90/android-receipt.json").write_text(json.dumps({"runs": runs}))
if mode in ("c1only",):
    rd = dst / "corpus/README.md"; rd.write_text(rd.read_text() + "\n- `self_assessment_check2.py` — SM gate v2 (control line)\n")
print("built", dst)
