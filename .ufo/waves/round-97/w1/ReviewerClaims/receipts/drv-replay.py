import importlib.util, json, os, shutil, sys
from pathlib import Path
LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
SCRATCH = Path("/fast/scratch/hyaku/revenger-r97/ReviewerClaims/driscr")
RECEIPTS = SCRATCH / "receipts"
os.environ["HYAKU_SCRATCH"] = "/fast/scratch/hyaku/revenger-r97/ReviewerClaims/dricounter"
os.environ["PYTHONUTF8"] = "1"
spec = importlib.util.spec_from_file_location("drv", LANE / ".ufo/waves/round-96/w1/CriticR96/receipts/drv.py")
drv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(drv)
drv.SCRATCH = SCRATCH
drv.RECEIPTS = RECEIPTS
work = SCRATCH / "fixtures"; work.mkdir(parents=True, exist_ok=True)
RECEIPTS.mkdir(parents=True, exist_ok=True)
summary = []
for name, fn, expect in drv.FORGERIES:
    root, want = drv.mod._fixture(work)
    fn(root)
    r, verdict, legs = drv.run_counter(root)
    exp_v, exp_leg = (expect.split(":") + [None])[:2] if ":" in expect else (expect, None)
    decided = (verdict == exp_v) and (exp_leg is None or exp_leg in legs)
    rec = {"delta": name, "expected": expect, "observed_verdict": verdict,
           "observed_failing_legs": legs, "rc": r.returncode, "decided": decided, "digest": want}
    (RECEIPTS / f"{name}.json").write_text(json.dumps(rec, indent=1), encoding="utf-8")
    summary.append(rec)
    shutil.rmtree(root, ignore_errors=True)
n_pass = sum(x["observed_verdict"]=="pass" for x in summary)
print(f"v5 accepted {n_pass}/{len(summary)}")
print(sorted(x["delta"] for x in summary if x["observed_verdict"]=="pass"))
print("undecided", [s["delta"] for s in summary if not s["decided"]])
