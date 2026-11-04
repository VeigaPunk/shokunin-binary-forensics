import json, copy, subprocess, sys, hashlib, shutil
from pathlib import Path
L=Path("/home/vgpnk/Projects/shokunin/revenger-shokunin"); S=Path("/fast/scratch/hyaku/revenger-r90/ReviewerR90C2")
P=L/".ufo/waves/round-90/w1/ExecR90Producer"
O2=L/"corpus/fixtures/apk-r65/oracle_check2.py"; O1=L/"corpus/fixtures/apk-r65/oracle_check.py"; TR=L/"corpus/fixtures/apk-r65/truth.json"
NE=L/"reports/round-90/norm_eq.py"
r1=json.loads((P/"run1.json").read_text())
G=r1["normalized_result"]["manifest"]["text"]; print("GOOD_TEXT:",repr(G))
NS='xmlns:android="http://schemas.android.com/apk/res/android"'
def orc(o,rec,name):
    p=S/f"atk-{name}.json"; p.write_text(json.dumps(rec,indent=2))
    return {0:"accept",1:"reject"}.get(subprocess.run([sys.executable,"-B",str(o),str(TR),str(p)],capture_output=True).returncode,"err")
def wt(t):
    r=copy.deepcopy(r1); r["normalized_result"]["manifest"]["text"]=t; return r
H='<?xml version="1.0" encoding="utf-8"?>\n'
atk=[
 ("A1-namespaced-package-only", H+'<manifest '+NS+' xmlns:x="urn:evil" x:package="com.example.r65" xmlns:ns1="android" ns1:versionCode="1" xmlns:ns2="android" ns2:versionName="1.0"/>'),
 ("A2-versions-in-foreign-namespace", H+'<manifest '+NS+' package="com.example.r65" xmlns:z="urn:evil" z:versionCode="1" z:versionName="1.0"/>'),
 ("A3-foreign-root-namespace", H+'<e:manifest xmlns:e="urn:evil" package="com.example.r65" xmlns:ns1="android" ns1:versionCode="1" ns1:versionName="1.0"/>'),
 ("A4-fabricated-permission-child", G[:-2]+'><uses-permission android:name="android.permission.SEND_SMS"/></manifest>'),
 ("A5-fabricated-component-child", G[:-2]+'><application><activity android:name="com.attacker.Evil" android:exported="true"/></application></manifest>'),
 ("A6-fabricated-root-attr-sharedUserId", G.replace('package="com.example.r65"','package="com.example.r65" android:sharedUserId="android.uid.system"')),
 ("A7-unnamespaced-versions", H+'<manifest package="com.example.r65" versionCode="1" versionName="1.0"/>'),
 ("Q1-single-quoted-equivalent", G.replace('"1"',"'1'").replace('"1.0"',"'1.0'")),
]
for n,t in atk:
    rec=wt(t); print(f"{n}: v2={orc(O2,rec,n)} v1={orc(O1,rec,n)}")
def ne(a,b,n):
    pa,pb=S/f"ne-{n}-a.json",S/f"ne-{n}-b.json"; pa.write_text(json.dumps(a)); pb.write_text(json.dumps(b))
    p=subprocess.run([sys.executable,"-B",str(NE),str(pa),str(pb)],capture_output=True,text=True); return p.stdout.split()[0]
# N1 greedy prefix
a=copy.deepcopy(r1); b=copy.deepcopy(r1)
a["normalized_result"]["note"]="pkg=com.example.r65:/s/rea-android-aa11/x"; b["normalized_result"]["note"]="pkg=com.attacker.fab:/s/rea-android-bb22/x"
print("N1-runtime-regex-eats-glued-prefix:",ne(a,b,"N1"))
# N2 duplicate keys in JSON text
a=copy.deepcopy(r1); b=copy.deepcopy(r1); a["normalized_result"]["t"]='{"x":1,"x":2}'; b["normalized_result"]["t"]='{"x":2}'
print("N2-json-text-duplicate-key-collapse:",ne(a,b,"N2"))
# N3 load_duration_ms dropped anywhere incl normalized_result
a=copy.deepcopy(r1); b=copy.deepcopy(r1); a["normalized_result"]["load_duration_ms"]=1; b["normalized_result"]["load_duration_ms"]="forged"
print("N3-load_duration_ms-any-depth-any-type:",ne(a,b,"N3"))
# N4 whole-string evid substitution: run2 field equal to its own id
a=copy.deepcopy(r1); b=copy.deepcopy(r1); b["evidence_id"]="not-an-ev-id"
print("N4-run2-arbitrary-id-string:",ne(a,b,"N4"))
# forgery tree: r89 record, two hand-edited ids, matching receipt
F="c7767789fe9e96bcc0d50656ad4bdce69ba3a3a9"; T=S/"forge"; shutil.rmtree(T,ignore_errors=True); T.mkdir()
subprocess.run(f"git -C {L} archive {F} corpus reports | tar -x -C {T}",shell=True,check=True)
src=json.loads((T/"reports/round-89/rejected-android-record/inspection.json").read_text())
x=json.dumps(src); old=src["evidence_id"]
b1=x.replace(old,"ev_"+"1"*64).encode(); b2=x.replace(old,"run2-anything").encode()
(T/"corpus/live/runs/round-90").mkdir(parents=True); (T/"corpus/live/runs/round-90/inspection.json").write_bytes(b1); (T/"reports/round-90/android-run2.json").write_bytes(b2)
(T/"reports/round-90/android-receipt.json").write_text(json.dumps({"runs":[{"stdout_sha256":hashlib.sha256(b1).hexdigest()},{"stdout_sha256":hashlib.sha256(b2).hexdigest()}]}))
p=subprocess.run([sys.executable,"-B",str(T/"reports/round-90/c2_counter.py"),"--tree",str(T)],capture_output=True,text=True)
print("### FORGE tree (r89 record, ids hand-edited, run2 id non-ev shape, 1-field receipt; no producer run):"); print(p.stdout.strip()); print("EXIT",p.returncode)
