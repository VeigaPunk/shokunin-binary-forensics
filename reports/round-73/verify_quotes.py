#!/usr/bin/env python3
"""Re-fetch each corpus/SOURCES.md row's URL and check that a quoted string from its
`anchor` cell appears on the fetched page (whitespace/markup/quote-normalised substring).

usage: python3 -B reports/round-73/verify_quotes.py [--ids S110-S414] [--out FILE]

Scope: this proves only that the quote text is still reachable at the cited URL
(GitHub rows are fetched at the pinned ref when the URL carries one). It does not
prove the quote supports the row's `teaches` sentence, that the page is unchanged
since it was opened, or origin. Rows whose anchor carries `[single-opener` or
`[integrator re-opened` are expected to FAIL here when the host blocks scripted
fetches (HTTP 403, JS-rendered pages); they are reported as MANUAL, not OK.
Network is required. Exit 0 always; read the counts."""
import re, sys, html, json, subprocess, tempfile, argparse, os, urllib.request, concurrent.futures as cf

LANE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def norm(s):
    s = html.unescape(s)
    for a, b in (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'), ("\u2013", "-"), ("\u2014", "-"), ("\u00a0", " ")):
        s = s.replace(a, b)
    s = re.sub(r"[`*_]", "", s)
    return re.sub(r"\s+", " ", s).strip().lower()

def strip_html(t):
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    return re.sub(r"(?s)<[^>]+>", " ", t)

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (revenger-verify)"})
    with urllib.request.urlopen(req, timeout=40) as r:
        data = r.read(30_000_000)
    if data[:4] == b"%PDF":
        with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
            f.write(data); f.flush()
            return subprocess.run(["pdftotext", "-q", f.name, "-"], capture_output=True, text=True).stdout
    return data.decode("utf-8", "replace")

def rows(lo, hi):
    out = []
    for line in open(os.path.join(LANE, "corpus/SOURCES.md"), encoding="utf-8"):
        m = re.match(r"^\| S(\d{3}) \|", line)
        if not m or not (lo <= int(m.group(1)) <= hi):
            continue
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) != 11 or c[7] == "queued":
            continue
        out.append({"id": "S" + m.group(1), "source": c[1], "anchor": c[5], "status": c[7]})
    return out

def candidates(url):
    c = [url]
    m = re.match(r"https://github\.com/([^/]+)/([^/]+)/(?:tree|blob)/([^/]+)(?:/(.*))?$", url)
    if m:
        o, r, ref, p = m.groups()
        if "/blob/" in url and p:
            c.insert(0, f"https://raw.githubusercontent.com/{o}/{r}/{ref}/{p}")
        else:
            base = f"{p}/" if p else ""
            for rn in ("README.md", "README.rst", "README", "readme.md", "README.txt"):
                c.append(f"https://raw.githubusercontent.com/{o}/{r}/{ref}/{base}{rn}")
    return c

def check(row):
    mu = re.search(r"https?://[^\s)>\]`]+", row["source"])
    a = row["anchor"].replace("\u201c", '"').replace("\u201d", '"')
    qs = [norm(x) for x in a.split('"') if len(x.split()) >= 3 and len(x) >= 15 and "accessed" not in x and "integrator" not in x and "single-opener" not in x]
    manual = "[single-opener" in a or "[integrator re-opened" in a
    if not mu or not qs:
        return {**row, "verdict": "NOQUOTE"}
    err = None
    for u in candidates(mu.group(0).rstrip(".,;")):
        try:
            t = fetch(u)
            A, B = norm(strip_html(t)), norm(t)
            if any(q in A or q in B for q in qs):
                return {**row, "verdict": "OK-MANUAL-FLAG" if manual else "OK"}
            err = "quote-not-found"
        except Exception as e:
            err = type(e).__name__ + ":" + str(e)[:60]
    return {**row, "verdict": "MANUAL" if manual else "FAIL", "err": err}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids", default="S110-S414")
    ap.add_argument("--out")
    a = ap.parse_args()
    lo, hi = (int(x[1:]) for x in a.ids.split("-"))
    rs = rows(lo, hi)
    with cf.ThreadPoolExecutor(16) as ex:
        res = list(ex.map(check, rs))
    cnt = {}
    for r in res:
        cnt[r["verdict"]] = cnt.get(r["verdict"], 0) + 1
    print(f"rows={len(res)}", cnt)
    for r in res:
        if r["verdict"] not in ("OK", "OK-MANUAL-FLAG"):
            print(r["verdict"], r["id"], r.get("err", ""), r["source"][:80])
    if a.out:
        json.dump([{k: v for k, v in r.items() if k != "anchor"} for r in res], open(a.out, "w"), indent=1)
