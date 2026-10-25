PRESENT — quoted string 1 `非营利性质的技术交流平台` occurs verbatim in the fetched document at byte offset 875 (inside the `og:description` meta attribute); the register's absence claim for row S061 is falsified. Strings 2 and 3 are absent.

# Seat
R67QuarS061 — wave-4 quarantine hand-check, item 10. Register row: `revenger` / round1 / S061 / `payload-absent`, at `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md:151` (register is READ-ONLY; not modified).

# Fetch receipt
Cited source: `https://bbs.kanxue.com/thread-288487.htm`

- Try 0 (bare `curl -sL --max-redirs 15`, no UA): `HTTP=502 SIZE=5638` — a yunaq (知道创宇云防御) CDN error page ("504 / 连接超时 / 服务器状态未知", `Node:ed9237d`), not the document. Recorded, then retried.
- Try 1 (same curl flags + `-A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'`): `HTTP=200 SIZE=827934 FINAL_URL=https://bbs.kanxue.com/thread-288487.htm` — real document bytes.
- Saved (<= 2 MB): `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S061/source.bin` — 827934 bytes, sha256 `6f95a2988916207a2bb00801d5de578bd24b13b5308ca130a65df94ba701500f`.
- Document identity: `<title>[原创]安卓逆向的核心流程-Android安全-看雪安全社区｜专业技术交流与安全研究论坛</title>` — the cited thread on 看雪 (kanxue) bbs.

# Per-string results (fixed-string, case-sensitive; raw + html.unescape + tag-stripped renderings)

## String 1: `非营利性质的技术交流平台` — PRESENT
- `grep -F -bo '非营利性质的技术交流平台' source.bin` → `875:非营利性质的技术交流平台`, `count=1`.
- Python renderings: raw-doc count=1, unescaped count=1, tag-stripped count=0, whitespace-collapsed count=0. The string lives **inside an HTML tag attribute**, so a tag-stripped-only check would miss it — it is nonetheless in the fetched bytes.
- Byte-875 context (~15-word window), verbatim bytes 750..1050 decoded:

  `社区｜非营利性质的安全技术交流平台" />` (end of a `description` meta) then
  `<meta property="og:description" content="看雪安全社区是一个非营利性质的技术交流平台，致力于汇聚全球的安全研究者和开发者，专注于软件与系统安全、逆向工程、漏洞研究等领域的深度技术讨论与合作。" />`

- The containing sentence is the standard kanxue og:description boilerplate: "看雪安全社区是一个非营利性质的技术交流平台，致力于汇聚全球的安全研究者和开发者，专注于软件与系统安全、逆向工程、漏洞研究等领域的深度技术讨论与合作。"
- Near-miss named: byte 759 carries the sibling variant `非营利性质的安全技术交流平台` (安全 inserted) in the plain `description` meta — the exact register quote matches the `og:description` form at 875.

## String 2: `Android App Feature Extraction: A review of approaches for malware and app similarity detection` — ABSENT
- `grep -F -c` on raw bytes: 0. Python counts: raw-doc=0, unescaped=0, tag-stripped=0, collapsed=0, HTML-escaped-variant-in-raw=0.
- Near-miss hunt (raw, case-insensitive `grep -F -i`): `feature extraction`=0, `extraction`=0, `malware`=0, `similarity`=0, `approaches for`=0, `review of`=0, `Android App`=0. No near-miss exists in the document.

## String 3: `APK Decompiler and APK Analysis Tools` — ABSENT
- `grep -F -c` on raw bytes: 0. Python counts: raw-doc=0, unescaped=0, tag-stripped=0, collapsed=0, HTML-escaped-variant-in-raw=0.
- Near-miss hunt (raw, case-insensitive): `decompiler`=0, `analysis tools`=0; `APK` occurs 12× (case-insensitive) but never adjacent to decompiler/analysis phrasing. No near-miss exists.

# Commands exercised
```
mkdir -p /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S061
curl -sL --max-redirs 15 -o source.bin -w 'TRY=%i HTTP=%{http_code} SIZE=%{size_download} FINAL_URL=%{url_effective}\n' 'https://bbs.kanxue.com/thread-288487.htm'   # -> 502 yunaq error page
curl -sL --max-redirs 15 -A 'Mozilla/5.0 ... Chrome/124.0 Safari/537.36' -o source.try1.bin -w '%{http_code}' 'https://bbs.kanxue.com/thread-288487.htm'          # -> 200, 827934 bytes
sha256sum source.bin -> 6f95a2988916207a2bb00801d5de578bd24b13b5308ca130a65df94ba701500f
grep -F -bo '<each quoted string>' source.bin
python3: html.unescape(doc); re.sub(r'<[^>]+>','',...); count each string in raw/unescaped/stripped/collapsed; escaped-variant check; fragment hunt
grep -F -i -c '<fragment>' source.bin   # near-miss sweep
```

# Row verdict
PRESENT. The register claims all three quotes are absent from the cited source; string 1 is verbatim in the fetched bytes at offset 875 (`og:description` meta). The absence claim holds only for strings 2 and 3.

# Caveats / notes
- The 502 on a bare-UA-less fetch is a transient CDN gateway error (yunaq), not UNREACHABLE; a single retry with a browser UA returned 200.
- String 1 is inside a meta attribute, so checks that only search rendered/tag-stripped text (as a tag-stripped rendering does) would report it absent — the byte-level fixed-string check is the decisive one per the seat rules.
- Tooling: no installs performed; system curl/python3 sufficed.
