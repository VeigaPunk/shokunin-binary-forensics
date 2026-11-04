import copy,json,subprocess,sys
from pathlib import Path
L=Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
rec=json.loads((L/"reports/round-89/rejected-android-record/inspection.json").read_text())
T=L/"corpus/fixtures/apk-r65/truth.json"
good=rec["normalized_result"]["manifest"]["text"]
cases={"FR1-comment-mentions-doctype": good.replace("<manifest","<!-- no <!DOCTYPE here -->\n<manifest",1),
       "FR0-unchanged-real": good}
for cid,t in cases.items():
    r=copy.deepcopy(rec); r["normalized_result"]["manifest"]["text"]=t
    p=Path(sys.argv[1])/f"{cid}.json"; p.write_text(json.dumps(r,indent=2)+"\n")
    for v in ["oracle_check2.py","oracle_check3.py"]:
        cp=subprocess.run([sys.executable,"-B",str(L/"corpus/fixtures/apk-r65"/v),str(T),str(p)],capture_output=True,text=True)
        print(f"CASE {cid} {v} rc={cp.returncode} {cp.stdout.strip().splitlines()[-1]}")
