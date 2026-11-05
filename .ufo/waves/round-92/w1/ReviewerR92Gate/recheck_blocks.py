import re, subprocess, sys, hashlib
entry="/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-92-managed-assembly-metadata-evidence.md"
lane="/home/vgpnk/Projects/shokunin/revenger-shokunin"
text=open(entry,encoding="utf-8").read()
lines=text.splitlines(); blocks=[]; inf=False; i=0
while i<len(lines):
    if lines[i].strip().startswith("```"): inf=not inf; i+=1; continue
    if inf and lines[i].startswith("$ "):
        cmd=lines[i][2:].strip(); out=[]; j=i+1
        while j<len(lines) and not lines[j].startswith("$ ") and not lines[j].strip().startswith("```"):
            if lines[j].strip(): out.append((lines[j], j+1))
            j+=1
        blocks.append((cmd,out,i+1)); i=j; continue
    i+=1
print(f"blocks={len(blocks)}")
allok=True
for cmd,out,lineno in blocks:
    p=subprocess.run(cmd,shell=False,cwd=lane,capture_output=True,text=True,
                     executable="/bin/bash") if "|" in cmd else subprocess.run(cmd.split(),cwd=lane,capture_output=True,text=True)
    stdout=p.stdout.splitlines()
    outset=set(stdout)
    missing=[l for l,_ in out if l not in outset]
    status="OK" if (p.returncode==0 and not missing) else "DRIFT"
    if status=="DRIFT": allok=False
    print(f"line {lineno}: rc={p.returncode} embedded={len(out)} stdout_lines={len(stdout)} missing={len(missing)} {status} :: {cmd[:90]}")
    for l in missing: print(f"   MISSING: {l}")
print("ALL_VERBATIM" if allok else "DRIFT_FOUND")
