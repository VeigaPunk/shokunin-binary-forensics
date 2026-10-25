ABSENT — all three quoted strings re-derived missing from the fetched ApiDemos-debug.apk (real 6,521,217-byte APK, http 200); the register's absence claim for row S083 (revenger, round2, payload-absent) holds.

# Scope
Wave-4 quarantine hand-check, item 10: row S083 of
/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md (line 157:
`revenger` | round2 | S083 | `payload-absent` | cited APK URL | three quotes | "cited source, companion URLs and local artifacts were all checked; the quote is in none of them").
Source is READ-ONLY; verdict only, nothing adopted.

# Fetch receipt
- `curl -sL --max-redirs 15 -o source.bin -w ... https://github.com/appium/android-apidemos/releases/download/v6.0.18/ApiDemos-debug.apk`
- http_code=200, size_download=6521217 bytes
- effective URL: release-assets.githubusercontent.com (GitHub release asset; redirect carried `rscd=attachment; filename=ApiDemos-debug.apk` percent-encoded in the signed URL — present in the redirect, NOT in the payload bytes)
- sha256 a9eecf37b26cd084855c530db81c2bb1b91f4c1b095a04f47aa7c20e2791f686
- 6,521,217 bytes > 2 MB → payload deleted after hashing per brief; excerpt + sha256 kept at
  /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S083/source-excerpt.txt
  (valid ZIP/APK, 869 members: classes.dex..classes13.dex, resources.arsc, assets/HelloActivity.apk, etc.)

# Per-string checks (fixed-string, case-sensitive)

## 1. `filename=ApiDemos-debug.apk` — ABSENT
- `grep -aFbo 'filename=ApiDemos-debug.apk' source.bin` → zero matches (no output lines; pipeline rc came from `head`)
- html.unescape + tag-stripped rendering (latin-1 decode) → find() = -1; escaped variants `filename&#x3D;`, `filename&#61;` → -1
- all 869 zip member payloads → no member contains it
- Near-miss: token `filename` occurs once inside classes.dex @ member offset 5127718 as a DEX string constant among identifier names (`file_id`,`file_identifier`,`filename`,`filepath`) — unrelated to an HTTP Content-Disposition header. The true artifact the quote likely distorted: the asset is *delivered* as `filename=ApiDemos-debug.apk` via the Content-Disposition of the release-assets redirect (observed percent-encoded in url_effective), i.e. it is transport metadata, not document text.

## 2. `Best Practices for Digital Evidence Collection` — ABSENT
- raw bytes: `grep -aFbo` → no match
- rendered/unescaped/tag-stripped text → -1 (incl. `&#32;`-spaced variant)
- zip members → 0 hits; probes `Evidence`, `Digital Evidence` → 0 occurrences anywhere in the APK
- No near-miss: looks like a fabricated phrase borrowed from digital-forensics boilerplate (e.g., NIST/SWGI evidence-collection wording); nothing like it exists in this binary.

## 3. `Data Integrity` — ABSENT
- raw bytes: `grep -aFbo` → no match
- rendered/unescaped → -1; `Data&#32;Integrity` → -1
- zip members → 0 hits; probe `Integrity` → 0 occurrences in any member
- No near-miss found; likely distorted from the same forensics-boilerplate family as quote 2.

# Method notes
- Searched three ways: (a) raw byte grep (`grep -aFbo`), (b) Python `html.unescape` + tag-strip rendering of a latin-1 decode, (c) every ZIP member decompressed and searched individually (covers deflated content where plain grep would miss).
- Fetched once, single attempt — no retry needed (http 200, real APK bytes, ZIP structure parses, 869 members enumerated).

# Verdict detail
- `filename=ApiDemos-debug.apk`: ABSENT
- `Best Practices for Digital Evidence Collection`: ABSENT
- `Data Integrity`: ABSENT
- Row S083 verdict: **ABSENT** (register claim confirmed; fabrication-class payload-absent holds)

# Out of scope / limits
- Companion URLs named in the register note were not enumerated in the row; only the cited source URL was assigned to this seat and checked.
- No installs/updates needed; used system curl, grep, python3, unzip only.

# Artifacts
- Report: revenger-shokunin/.ufo/waves/round-67/R67QuarS083.md
- Excerpt+hash: revenger-shokunin/.ufo/waves/round-67/quarantine/S083/source-excerpt.txt
