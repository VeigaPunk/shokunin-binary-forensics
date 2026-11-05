#!/usr/bin/env python3
"""ExecOracle r93w1: independent re-derivation of the round-77 record facts.

Runs every check itself via python3 -c (argv, cwd = lane root) and writes:
  derivations.txt    command -> verbatim output pairs
  ledger-check.tsv   LEDGER.md prose claim -> re-derivation -> match yes/no
  k-arithmetic.txt   coverage K 9/15 -> 10/15 arithmetic over the frozen README
Nothing here imports oracle_check.py; every value comes from the raw record
JSON and committed fixture bytes.
"""
import datetime
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
REV = "02050cb2a6758e3bd9cec696ff0e42df6f23511a"
WAVE = LANE / ".ufo/waves/round-93/w1/ExecOracle"
SCRATCH = Path("/fast/scratch/hyaku/revenger-r93/ExecOracle")
REC = "corpus/live/runs/round-77/inspection.json"
TL = "corpus/live/runs/round-77/target-listing.json"
RCPT = "corpus/live/runs/round-77/receipt.json"
FIX = "corpus/fixtures/browser-r77"

WAVE.mkdir(parents=True, exist_ok=True)


def run_py(code, cwd=LANE):
    assert "'" not in code, "code must stay single-quote-free for display"
    r = subprocess.run(["python3", "-c", code], cwd=str(cwd),
                       capture_output=True, text=True, timeout=60)
    return r


checks = []  # (id, code)


def C(cid, code):
    checks.append((cid, code))


# ---- derivations: identity facts from record JSON + committed fixture bytes
C("D01", 'import hashlib;d=open("corpus/fixtures/browser-r77/index.html","rb").read();print("sha256",hashlib.sha256(d).hexdigest());print("bytes",len(d))')
C("D02", 'import hashlib;d=open("corpus/fixtures/browser-r77/app.js","rb").read();print("sha256",hashlib.sha256(d).hexdigest());print("bytes",len(d))')
C("D03", 'import json;r=json.load(open("corpus/live/runs/round-77/inspection.json"));print("operation",r["operation"])')
C("D04", 'import json;r=json.load(open("corpus/live/runs/round-77/inspection.json"));print("provider.id",r["provider"]["id"]);print("provider.name",r["provider"]["name"]);print("predicate_type",r["predicate_type"])')
C("D05", 'import json,re;r=json.load(open("corpus/live/runs/round-77/inspection.json"));e=r["evidence_id"];print("evidence_id",e);print("shape_ev_64hex",bool(re.fullmatch("ev_[0-9a-f]{64}",e)))')
C("D06", 'import json;r=json.load(open("corpus/live/runs/round-77/inspection.json"));t=r["normalized_result"]["target"];tr=json.load(open("corpus/fixtures/browser-r77/truth.json"))["run_pin"];print("target.url",t["url"]);print("target.origin",t["origin"]);print("url==run_pin.page_url",t["url"]==tr["page_url"]);print("origin==run_pin.http_origin",t["origin"]==tr["http_origin"]);print("parameters.cdp_endpoint",r["parameters"]["cdp_endpoint"]);print("parameters.allowed_origins",r["parameters"]["allowed_origins"])')
C("D07", 'import json,re;b=open("corpus/fixtures/browser-r77/index.html",encoding="utf-8").read();t=re.search("<title>(.*?)</title>",b,re.S).group(1);ins=re.search("<script>(.*?)</script>",b,re.S).group(1);lit=re.findall("\\x22([^\\x22]+)\\x22",ins);exp=t+"".join(lit);rt=json.load(open("corpus/live/runs/round-77/inspection.json"))["normalized_result"]["target"]["title"];print("static_title",repr(t));print("inline_literals",lit);print("expected_title",repr(exp));print("record_title",repr(rt));print("equal",exp==rt)')
C("D08", 'import json;r=json.load(open("corpus/live/runs/round-77/inspection.json"));s=r["normalized_result"]["scripts"];print("scripts.total",s["total"]);print("scripts.items",len(s["items"]));print("urls",[i["url"] for i in s["items"]])')
C("D09", 'import json;d=open("corpus/fixtures/browser-r77/app.js","rb").read();r=json.load(open("corpus/live/runs/round-77/inspection.json"));it=[i for i in r["normalized_result"]["scripts"]["items"] if i["url"].endswith("/app.js")][0];print("record_length",it["length"]);print("file_bytes",len(d));print("length==file_bytes",it["length"]==len(d));print("reconciliation",it["resource_reconciliation"]["status"]);print("reconciliation_resource_key",it["resource_reconciliation"].get("resource_key"))')
C("D10", 'import json,re;b=open("corpus/fixtures/browser-r77/index.html",encoding="utf-8").read();ins=re.search("<script>(.*?)</script>",b,re.S).group(1);r=json.load(open("corpus/live/runs/round-77/inspection.json"));it=[i for i in r["normalized_result"]["scripts"]["items"] if i["url"].endswith("/index.html")][0];print("record_length",it["length"]);print("inline_text_chars",len(ins));print("inline_text",repr(ins));print("length==inline_chars",it["length"]==len(ins));print("reconciliation",it["resource_reconciliation"]["status"],it["resource_reconciliation"].get("reason"))')
C("D11", 'import json,hashlib;d=open("corpus/fixtures/browser-r77/app.js","rb").read();h=hashlib.sha256(d).hexdigest();r=json.load(open("corpus/live/runs/round-77/inspection.json"));it=[i for i in r["normalized_result"]["scripts"]["items"] if i["url"].endswith("/app.js")][0];print("cdp_hash",it["cdp_hash"]);print("file_sha256",h);print("cdp_hash==file_sha256",it["cdp_hash"]==h)')
C("D12", 'import json,re,hashlib;b=open("corpus/fixtures/browser-r77/index.html",encoding="utf-8").read();ins=re.search("<script>(.*?)</script>",b,re.S).group(1);h=hashlib.sha256(ins.encode("utf-8")).hexdigest();r=json.load(open("corpus/live/runs/round-77/inspection.json"));it=[i for i in r["normalized_result"]["scripts"]["items"] if i["url"].endswith("/index.html")][0];print("cdp_hash",it["cdp_hash"]);print("inline_text_sha256",h);print("cdp_hash==inline_text_sha256",it["cdp_hash"]==h)')
C("D13", 'import json;r=json.load(open("corpus/live/runs/round-77/inspection.json"));rs=r["normalized_result"]["resources"];print("resource_count",len(rs));x=rs[0];print("url",x["url"]);print("type",x["type"]);print("mime_type",x["mime_type"]);print("content_size",x["content_size"]);n=len(open("corpus/fixtures/browser-r77/app.js","rb").read());print("content_size==app.js_bytes",x["content_size"]==n);rk=x["resource_key"];ait=[i for i in r["normalized_result"]["scripts"]["items"] if i["url"].endswith("/app.js")][0];print("script_reconciliation_exact",ait["resource_reconciliation"]["status"]=="exact" and ait["resource_reconciliation"]["resource_key"]==rk)')
C("D14", 'import json;r=json.load(open("corpus/live/runs/round-77/inspection.json"));m=r["normalized_result"]["metadata"]["dom_urls"];print("dom_urls_count",len(m));print("entries",[(e["node_index"],e["attribute"],e["url"]) for e in m]);b=open("corpus/fixtures/browser-r77/index.html",encoding="utf-8").read();print("index_html_has_src_app.js","src=\\x22app.js\\x22" in b)')
C("D15", 'import json,hashlib;tl=json.load(open("corpus/live/runs/round-77/target-listing.json"));ts=tl["normalized_result"]["targets"];print("operation",tl["operation"]);print("provider.id",tl["provider"]["id"]);print("evidence_id",tl["evidence_id"]);print("targets_count",len(ts));print("target_types",[t.get("type") for t in ts]);print("target_id",ts[0]["target_id"]);r=json.load(open("corpus/live/runs/round-77/inspection.json"));print("==record.parameters.target_id",ts[0]["target_id"]==r["parameters"]["target_id"]);print("==record.target.target_id",ts[0]["target_id"]==r["normalized_result"]["target"]["target_id"]);print("==record.frames[0].frame_id",ts[0]["target_id"]==r["normalized_result"]["frames"][0]["frame_id"]);h=hashlib.sha256(open("corpus/live/runs/round-77/target-listing.json","rb").read()).hexdigest();rc=json.load(open("corpus/live/runs/round-77/receipt.json"));print("listing_sha256",h);print("==receipt.target_listing_stdout_sha256",h==rc["target_listing_stdout_sha256"])')
C("D16", 'import json,hashlib;d=open("corpus/live/runs/round-77/inspection.json","rb").read();h=hashlib.sha256(d).hexdigest();rc=json.load(open("corpus/live/runs/round-77/receipt.json"));print("record_sha256",h);print("receipt.stdout_sha256",rc["stdout_sha256"]);print("==receipt.stdout_sha256",h==rc["stdout_sha256"]);print("receipt.exit_code",rc["exit_code"]);print("receipt.duration_seconds",rc["duration_seconds"]);print("receipt.stderr_bytes",rc["stderr_bytes"]);print("receipt.producer",rc["producer"][:60]);rid=json.load(open("corpus/live/runs/round-77/inspection.json"))["evidence_id"];print("record.evidence_id==receipt.evidence_id",rid==rc["evidence_id"])')
C("D17", 'import json,hashlib;a=json.load(open("corpus/live/runs/round-77/provider-gates/android-gate.json"));f=json.load(open("corpus/live/runs/round-77/provider-gates/firmware-gate.json"));print("android.details.operation",a["details"]["operation"]);print("android.details.provider_id",a["details"]["provider_id"]);print("android.code",a["code"]);print("firmware.details.operation",f["details"]["operation"]);print("firmware.details.provider_id",f["details"]["provider_id"]);print("firmware.code",f["code"]);pg=json.load(open("corpus/live/runs/round-77/provider-gates/receipt.json"));ah=hashlib.sha256(open("corpus/live/runs/round-77/provider-gates/android-gate.json","rb").read()).hexdigest();fh=hashlib.sha256(open("corpus/live/runs/round-77/provider-gates/firmware-gate.json","rb").read()).hexdigest();print("android_payload_sha==receipt_leg",ah==pg["legs"][0]["stdout_sha256"]);print("firmware_payload_sha==receipt_leg",fh==pg["legs"][1]["stdout_sha256"])')
C("D18", 'import json;r=json.load(open("corpus/live/runs/round-77/inspection.json"));b=r["normalized_result"]["browser"];tr=json.load(open("corpus/fixtures/browser-r77/truth.json"))["run_pin"];print("browser.product",b["product"]);print("product_in_run_pin.browser",b["product"] in tr["browser"])')

# ---- run derivations, capture verbatim
lines = []
lines.append("derivations.txt — ExecOracle (round-93 w1) independent re-derivation")
lines.append("lane: %s" % LANE)
lines.append("freeze rev: %s (== lane HEAD at run time)" % REV)
lines.append("generated: %s" % datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
lines.append("method: each `$ python3 -c <code>` line below was executed verbatim with")
lines.append("cwd = lane root; printed output captured verbatim; exit status checked 0.")
lines.append("No oracle_check.py code is imported or reused; every value is derived")
lines.append("directly from the saved record JSON and the committed fixture bytes.")
lines.append("")
bad = []
for cid, code in checks:
    r = run_py(code)
    lines.append("## %s" % cid)
    lines.append("$ python3 -c '%s'" % code)
    out = r.stdout.rstrip("\n")
    lines.append(out if out else "(no stdout)")
    if r.returncode != 0:
        lines.append("(exit=%d stderr=%s)" % (r.returncode, r.stderr.strip()[:200]))
        bad.append(cid)
    lines.append("")
(WAVE / "derivations.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("derivations.txt written; failing commands:", bad or "none")

# ---- parse D-outputs back out for the ledger cross-check
dout = {}
cur = None
for ln in lines:
    m = re.match(r"^## (D\d+)$", ln)
    if m:
        cur = m.group(1)
        dout[cur] = []
    elif cur and ln.startswith("$ "):
        continue
    elif cur is not None:
        dout[cur].append(ln)

def dget(cid):
    return "\n".join(dout[cid])

# ---- oracle log facts (my own rerun, saved earlier this session)
olog = (WAVE / "oracle-rerun.log").read_text(encoding="utf-8").splitlines()
oks = [l for l in olog if l.startswith("check ok:")]
fixture_legs = [l for l in oks if "fixture index.html" in l or "fixture app.js" in l]
oracle_tail = olog[-2] if olog[-1].startswith("oracle_exit=") else olog[-1]
oracle_exit = olog[-1]

# ---- f_probe4 family set (frozen F probe source, read as bytes)
probe = (LANE / "reports/round-81/f_probe4.py").read_text(encoding="utf-8")
fams = dict(re.findall(r'"([\w-]+)": \{([^}]*)\}', probe))
fam_ops = {k: set(re.findall(r'"([\w_]+)"', v)) for k, v in fams.items()}

LC = []  # (id, claim, check_desc, derived, match)


def add(lid, claim, check, derived, ok):
    LC.append((lid, claim, check, derived, "yes" if ok else "NO"))


add("LC01", "fixture: corpus/fixtures/browser-r77/ - two authored static files + truth.json + oracle_check.py",
    "sorted(os.listdir(fixture dir)) via python3",
    ",".join(sorted(p.name for p in (LANE / FIX).iterdir())),
    sorted(p.name for p in (LANE / FIX).iterdir()) == ["app.js", "index.html", "oracle_check.py", "truth.json"])
d01 = dget("D01")
add("LC02", "index.html 316 bytes sha256 46e51761...b45", "D01",
    d01.replace("\n", "; "), ("bytes 316" in d01) and ("46e51761" in d01) and ("deb45" in d01))
d02 = dget("D02")
add("LC03", "app.js 101 bytes sha256 fb079fa2...593", "D02",
    d02.replace("\n", "; "), ("bytes 101" in d02) and ("fb079fa2" in d02) and ("aa593" in d02))
tk = json.loads((LANE / "corpus/fixtures/browser-r77/truth.json").read_text(encoding="utf-8"))
need = ["authored", "run_pin", "producer_expected", "volatile_not_compared"]
add("LC04", "truth.json = authored anchors + run pin + producer expectations + volatile-not-compared list",
    "top-level keys of truth.json", ",".join(sorted(tk.keys())),
    all(k in tk for k in need))
n_rec = len(oks) - len(fixture_legs)
add("LC05", "oracle: premise leg re-hashes fixture bytes; record leg checks 15 identity facts (total 17)",
    "count 'check ok' lines in ExecOracle/oracle-rerun.log",
    "total=%d premise=%d record=%d" % (len(oks), len(fixture_legs), n_rec),
    len(oks) == 17 and len(fixture_legs) == 2 and n_rec == 15)
rp = tk["run_pin"]
add("LC06", "serving: python -m http.server 8477 --bind 127.0.0.1 from the fixture directory",
    "truth.json run_pin.server contains the stated command",
    rp["server"], "python -m http.server 8477 --bind 127.0.0.1" in rp["server"])
d18 = dget("D18")
prod = json.loads((LANE / REC).read_text(encoding="utf-8"))["normalized_result"]["browser"]["product"]
add("LC07", "browser: the host's own Chrome/156.0.8078.74, headless",
    "record browser.product + run_pin.browser headless flag (D18)",
    "%s | headless_in_pin=%s" % (prod, "headless" in rp["browser"]),
    prod == "Chrome/156.0.8078.74" and "--headless=new" in rp["browser"])
d06 = dget("D06")
add("LC08", "loopback CDP --remote-debugging-port=9333; allowed origin 8477",
    "parameters.cdp_endpoint + allowed_origins vs run_pin (D06)",
    d06.replace("\n", "; "),
    "cdp_endpoint http://127.0.0.1:9333" in d06 and "url==run_pin.page_url True" in d06 and "origin==run_pin.http_origin True" in d06)
d15 = dget("D15")
add("LC09", "discovery: rea list-browser-targets -> exactly one page target F6A6B5C8E48625523BCEA0CE47F68B42, saved as target-listing.json",
    "D15 over target-listing.json + record ids",
    d15.replace("\n", "; "),
    ("operation list_browser_targets" in d15) and ("targets_count 1" in d15) and ("target_types ['page']" in d15)
    and ("==record.parameters.target_id True" in d15) and ("==receipt.target_listing_stdout_sha256 True" in d15))
add("LC10", "list_browser_targets is in no F family set (auxiliary); inspect_web_page is the browser-runtime op",
    "families dict parsed from frozen reports/round-81/f_probe4.py",
    "browser-runtime={" + ",".join(sorted(fam_ops.get("browser-runtime", set()))) + "}; list_browser_targets anywhere=" +
    str(any("list_browser_targets" in v for v in fam_ops.values())),
    ("inspect_web_page" in fam_ops.get("browser-runtime", set()))
    and not any("list_browser_targets" in v for v in fam_ops.values()))
rc = json.loads((LANE / RCPT).read_text(encoding="utf-8"))
add("LC11", "inspection.json = the exact stdout of rea inspect-web-page (rea 6.8.0, provider rea-cdp-browser)",
    "receipt.producer text + record provider.id (D04)",
    "rea 6.8.0 in receipt.producer=%s; provider.id=%s" % ("rea 6.8.0" in rc["producer"], "rea-cdp-browser"),
    "rea 6.8.0" in rc["producer"] and json.loads((LANE / REC).read_text(encoding="utf-8"))["provider"]["id"] == "rea-cdp-browser")
d16 = dget("D16")
add("LC12", "exit 0, 3.498 s, stderr empty", "receipt.json fields (D16)",
    d16.replace("\n", "; "),
    ("receipt.exit_code 0" in d16) and ("receipt.duration_seconds 3.498" in d16) and ("receipt.stderr_bytes 0" in d16))
add("LC13", "stdout sha256 b045a4ee...e868", "sha256(record bytes) == receipt pin (D16)",
    d16.replace("\n", "; "),
    "==receipt.stdout_sha256 True" in d16 and "b045a4ee" in d16 and d16.split("record_sha256 ")[1].split("\n")[0].endswith("e868"))
add("LC14", "Evidence ev_a0134e6f482424baa278ec374f9bf0e984738a113106556b9933d2fd403918fd",
    "record.evidence_id == receipt.evidence_id (D16, D05 shape)",
    d16.replace("\n", "; "),
    "record.evidence_id==receipt.evidence_id True" in d16 and bool(re.fullmatch(r"ev_[0-9a-f]{64}", rc["evidence_id"])))
add("LC15", "identity oracle -> ORACLE OK (17/17 checks), exit 0",
    "my own rerun saved as ExecOracle/oracle-rerun.log",
    "%s | %s" % (oracle_tail, oracle_exit),
    oracle_tail.strip() == "ORACLE OK (17/17 checks)" and oracle_exit.strip() == "oracle_exit=0")
d07 = dget("D07")
add("LC16", "the loaded title `r77 probe page [loaded]` re-derived from authored <title> + inline literal",
    "D07 independent byte derivation",
    d07.replace("\n", "; "), "equal True" in d07)
d14 = dget("D14")
add("LC17", "the app.js src dom-url (metadata.dom_urls == exactly the app.js src)",
    "D14", d14.replace("\n", "; "),
    "dom_urls_count 1" in d14 and ("http://127.0.0.1:8477/app.js" in d14) and ("index_html_has_src_app.js True" in d14))
d09 = dget("D09")
d10 = dget("D10")
add("LC18", "both script lengths (101/46) byte-derived from the committed files",
    "D09 (app.js) + D10 (inline)",
    "app.js: %s || inline: %s" % (d09.replace("\n", "; "), d10.splitlines()[0] + " " + d10.splitlines()[1]),
    ("length==file_bytes True" in d09) and ("length==inline_chars True" in d10))
d11 = dget("D11")
d12 = dget("D12")
add("LC19", "both CDP cdp_hash values equal the sha256 of the corresponding authored script text",
    "D11 (app.js bytes) + D12 (inline text from index.html bytes)",
    "app.js equal=%s; inline equal=%s" % (d11.splitlines()[-1].split()[-1], d12.splitlines()[-1].split()[-1]),
    d11.splitlines()[-1].endswith("True") and d12.splitlines()[-1].endswith("True"))
d13 = dget("D13")
add("LC20", "the single Script resource (content_size 101, text/javascript, reconciliation exact)",
    "D13", d13.replace("\n", "; "),
    ("resource_count 1" in d13) and ("content_size 101" in d13) and ("mime_type text/javascript" in d13)
    and ("content_size==app.js_bytes True" in d13) and ("script_reconciliation_exact True" in d13))
vn = tk["volatile_not_compared"]
joined = " | ".join(vn)
add("LC21", "volatile per-run: evidence_id, target_id/frame_id, script_key/cdp_hash, capture_window timestamps, completeness counters",
    "truth.json .volatile_not_compared entries", joined,
    all(s in joined for s in ["evidence_id", "target_id", "frame_id", "script_key", "cdp_hash", "capture_window", "completeness"]))
d17 = dget("D17")
add("LC22", "provider-gates/: snake_case details.operation inspect_android_package (jadx gate), inspect_firmware_regions (binwalk/Linux gate)",
    "D17 over the committed gate payloads + receipt legs",
    d17.replace("\n", "; "),
    ("android.details.operation inspect_android_package" in d17) and ("android.details.provider_id jadx" in d17)
    and ("firmware.details.operation inspect_firmware_regions" in d17) and ("firmware.details.provider_id binwalk" in d17)
    and ("android_payload_sha==receipt_leg True" in d17) and ("firmware_payload_sha==receipt_leg True" in d17))
add("LC23", "machine-checked by reports/round-77/gate_probe.sh", "path exists", "exists=%s" % (LANE / "reports/round-77/gate_probe.sh").is_file(),
    (LANE / "reports/round-77/gate_probe.sh").is_file())
add("LC24", "receipt in receipt.json", "file exists", "exists=%s" % (LANE / RCPT).is_file(), (LANE / RCPT).is_file())

rec_json = json.loads((LANE / REC).read_text(encoding="utf-8"))
comp = rec_json["normalized_result"]["completeness"]
add("LC25", "late-attach class (attach_limited) is why script source text is not retained in the record; identity rests on byte-derived hashes/lengths",
    "record completeness.conditions + scripts.items[].source.included",
    "conditions=%s; source.included=%s" % (",".join(comp["conditions"]),
        ",".join(str(i["source"]["included"]) for i in rec_json["normalized_result"]["scripts"]["items"])),
    "attach_limited" in comp["conditions"] and all(i["source"]["included"] is False for i in rec_json["normalized_result"]["scripts"]["items"]))
add("LC26", "discovery `rea list-browser-targets ... --format json` (exit 0) -> target-listing.json",
    "receipt.json: exit_code recorded only for the inspect-web-page leg; no listing exit-code field in committed bytes",
    "receipt.exit_code=%s (inspect-web-page leg); target_listing_stdout_sha256 present=%s; no listing exit-code field" % (rc["exit_code"], "target_listing_stdout_sha256" in rc),
    False)

with (WAVE / "ledger-check.tsv").open("w", encoding="utf-8") as f:
    f.write("id\tledger_claim\tcheck\tderived\tmatch\n")
    for lid, claim, check, derived, m in LC:
        cl = re.sub(r"\s+", " ", claim).replace("\t", " ")
        ck = re.sub(r"\s+", " ", check).replace("\t", " ")
        dv = re.sub(r"\s+", " ", derived).replace("\t", " ")
        f.write("%s\t%s\t%s\t%s\t%s\n" % (lid, cl, ck, dv, m))
nomatch = [l[0] for l in LC if l[4] != "yes"]
print("ledger-check.tsv written; NO-match rows:", nomatch or "none")

# ---- K arithmetic over the frozen README at REV
readme_base = subprocess.run(["git", "-C", str(LANE), "show", "%s:corpus/README.md" % REV],
                             capture_output=True, text=True, check=True).stdout
(SCRATCH / "readme-base.md").write_text(readme_base, encoding="utf-8")
K = []
K.append("k-arithmetic.txt — ExecOracle (round-93 w1)")
K.append("freeze rev: %s" % REV)
K.append("generated: %s" % datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
K.append("")
K.append("# KA01 rows/cells over corpus/README.md at the freeze rev (same parse as the")
K.append("# frozen counter: cells = strip('|').split('|') trimmed; row iff ^\\|\\s*C[0-9]+ and 5 cells)")
kcode = (
    'import re;lines=open("%s/readme-base.md",encoding="utf-8").read().splitlines();'
    "cells=lambda l:[x.strip() for x in l.strip().strip(\"|\").split(\"|\")];"
    'cov=[cells(l) for l in lines if re.match(r"^\\|[ \\t]*C[0-9]+ ",l) and len(cells(l))==5];'
    'held=[r[0] for r in cov if r[4]=="held"];'
    'c08=[r for r in cov if r[0]=="C08"][0];'
    'uncov=[r[0] for r in cov if r[4]=="uncovered"];'
    'print("rows",len(cov));print("ids",",".join(r[0] for r in cov));'
    'print("held",len(held),",".join(held));print("uncovered",len(uncov),",".join(uncov));'
    'print("C08cells",c08)'
) % SCRATCH.as_posix()
kr = run_py(kcode, cwd=SCRATCH)
K.append("$ python3 -c '%s'" % kcode)
K.append(kr.stdout.rstrip("\n"))
if kr.returncode != 0:
    K.append("(exit=%d stderr=%s)" % (kr.returncode, kr.stderr.strip()[:300]))
K.append("")
cov_parse = {}
for ln in kr.stdout.splitlines():
    k, _, v = ln.partition(" ")
    cov_parse[k] = v
K.append("# KA02 working computation: flip C08 uncovered -> held with the knowledge cell")
K.append("# citing corpus/knowledge/round-93-browser-cdp-runtime-evidence.md (the counter")
K.append("# counts held_backed = rows with r[4]==held AND every knowledge/....md named in")
K.append("# cell 2 existing under corpus/)")
base_held = int(cov_parse.get("held", "0").split()[0])
rows_total = int(cov_parse.get("rows", "0"))
K.append("rows_total=%d (claim needs 15); held_at_base=%d (claim needs 9); C08_at_base=%s"
         % (rows_total, base_held, cov_parse.get("C08cells", "?")))
K.append("flip: held %d -> %d (C08 uncovered -> held, entry exists at landing)" % (base_held, base_held + 1))
K.append("K_HELD_BACKED working value after flip: %d/15 == claim after 10/15: %s"
         % (base_held + 1, base_held + 1 == 10))
K.append("")
K.append("# KA03 worktree corpus/README.md vs the frozen blob (byte equality)")
wb = (LANE / "corpus/README.md").read_bytes()
K.append("worktree==freeze_blob: %s" % (wb.decode("utf-8") == readme_base))
K.append("")
K.append("# KA04 entry path at the freeze rev and in the worktree now")
e1 = subprocess.run(["git", "-C", str(LANE), "cat-file", "-e",
                     "%s:corpus/knowledge/round-93-browser-cdp-runtime-evidence.md" % REV],
                    capture_output=True)
K.append("entry at %s: present=%s (expected False at freeze)" % (REV, e1.returncode == 0))
e2 = (LANE / "corpus/knowledge/round-93-browser-cdp-runtime-evidence.md").exists()
K.append("entry in worktree now: present=%s (expected False pre-landing)" % e2)
(WAVE / "k-arithmetic.txt").write_text("\n".join(K) + "\n", encoding="utf-8")
print("k-arithmetic.txt written")
print("KA summary: rows=%s held=%s C08=%s flip=%s worktree_equal=%s entry_at_rev=%s entry_now=%s"
      % (rows_total, base_held, cov_parse.get("C08cells", "?"), base_held + 1 == 10,
         wb.decode("utf-8") == readme_base, e1.returncode == 0, e2))
